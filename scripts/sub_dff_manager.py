#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SUB-DFF manager.

Pipeline
  1. Read SUB-DFF from the repository (one subscription link per line).
  2. Test every http(s) link: it must still respond AND still serve proxy
     configs (vmess/vless/ss/trojan/hysteria/tuic/... or clash/sing-box YAML).
     Healthy links are kept, dead ones are dropped. Lines that are not
     http(s) URLs (e.g. raw node URIs) are preserved untouched.
  3. Discover public collectors dynamically - NO hardcoded links: query the
     GitHub public search API for active aggregator/collector repos, then
     list the files INSIDE each repo (git trees API) and take its actual
     subscription files (.txt/.yaml/.json/raw), plus the endpoints advertised
     in each repo's README. Every candidate is validated exactly like step 2
     before it is accepted; at most MAX_DISCOVERED are kept (aim:
     MIN_DISCOVERED).
  4. Merge, deduplicate and rewrite SUB-DFF.

No user secrets are required. GH_TOKEN (the automatic github.token) only
raises the GitHub search rate limit; everything also works without it.
"""

from __future__ import annotations

import base64
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.parse import quote, urlsplit

import requests

# --------------------------------------------------------------------------- #
# Configuration (all overridable through environment variables)
# --------------------------------------------------------------------------- #
SUB_FILE        = os.environ.get("SUB_FILE", "SUB-DFF.txt")
MIN_PROXIES     = int(os.environ.get("MIN_PROXIES", "2"))
MIN_DISCOVERED  = int(os.environ.get("MIN_DISCOVERED", "10"))
MAX_DISCOVERED  = int(os.environ.get("MAX_DISCOVERED", "50"))
WORKERS         = int(os.environ.get("WORKERS", "24"))
CONNECT_TIMEOUT = float(os.environ.get("CONNECT_TIMEOUT", "10"))
READ_TIMEOUT    = float(os.environ.get("READ_TIMEOUT", "25"))
MAX_BODY_BYTES  = int(os.environ.get("MAX_BODY_BYTES", str(10 * 1024 * 1024)))
GH_TOKEN        = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")

SEARCH_QUERIES = [
    q.strip()
    for q in os.environ.get(
        "SEARCH_QUERIES",
        "v2ray aggregator,v2ray configs,free proxy subscription,"
        "vless configs,clash subscription,v2ray nodes collector",
    ).split(",")
    if q.strip()
]

MAX_REPOS            = 30    # repos kept from GitHub search
FILES_PER_REPO       = 8     # subscription files kept per repo file-tree
README_REPOS         = 15    # repos whose README is scraped for sub links
PER_REPO_README_URLS = 6     # candidate URLs kept per README
CHUNK_SIZE           = 40    # candidates validated per batch
RETRIES              = 2     # attempts per URL
SEARCH_SLEEP         = 2.0   # seconds between search-API calls

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "v2rayNG/1.8.23",
    "V2rayN/6.45",
    "clash-verge/v1.6.6",
]

# Proxy URI schemes recognised inside subscription payloads.
SCHEME_RE = re.compile(
    r"\b(?:vmess|vless|trojan|ssr|ss|socks5|socks4|socks|hysteria2|hysteria|hy2|"
    r"tuic|juicity|brook|naive|snell|anytls|mieru)://",
    re.IGNORECASE,
)
# clash/mihomo YAML entries: "- name: ..." or "- {name: ...}"
YAML_NODE_RE = re.compile(r"^\s*-\s*(?:\{[^}]*?)?name\s*:", re.MULTILINE)
# sing-box style JSON outbounds
JSON_NODE_RE = re.compile(
    r'"type"\s*:\s*"(?:vmess|vless|trojan|ss|ssr|hysteria2|hysteria|tuic|socks|wireguard)"',
    re.IGNORECASE,
)
HTTP_RE = re.compile(r"^https?://", re.IGNORECASE)
README_URL_RE = re.compile(r"https?://[^\s\"'<>\\)\]]+", re.IGNORECASE)
SUB_HINT_RE = re.compile(
    r"(sub|subscribe|configs?|nodes?|v2ray|clash|proxy|links?|base64|merge|pool|all)",
    re.IGNORECASE,
)

# Heuristics for picking likely subscription files out of a repo's own file
# tree (no hardcoded repo/file addresses anywhere in this file).
TREE_HINT_RE = re.compile(
    r"(sub|subscribe|configs?|nodes?|proxies?|v2ray|clash|sing-?box|"
    r"merge|mix|all|links?|base64|pool|free)",
    re.IGNORECASE,
)
TREE_EXCLUDE_RE = re.compile(
    r"(^|/)(\.github|\.ci|\.idea|\.vscode|docs?|assets?|images?|screenshots?|"
    r"test|tests|scripts?|tools?|sources?|modules?)(/|$)",
    re.IGNORECASE,
)
TREE_BAD_EXT = (
    ".md", ".html", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
    ".py", ".js", ".ts", ".php", ".sh", ".zip", ".gz", ".rar", ".pdf",
    ".db", ".sqlite", ".lock", ".mod", ".sum",
)

# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
_session = requests.Session()
_adapter = requests.adapters.HTTPAdapter(
    pool_connections=WORKERS + 4, pool_maxsize=WORKERS + 4
)
_session.mount("https://", _adapter)
_session.mount("http://", _adapter)


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def _headers() -> dict:
    return {"User-Agent": random.choice(USER_AGENTS), "Accept": "*/*"}


def fetch(url: str, max_bytes: int = MAX_BODY_BYTES):
    """GET a URL, return the decoded body (capped) or None on non-200.

    Network errors are raised; callers handle them (they are retried there).
    """
    with _session.get(
        url,
        headers=_headers(),
        timeout=(CONNECT_TIMEOUT, READ_TIMEOUT),
        stream=True,
        allow_redirects=True,
    ) as resp:
        if resp.status_code != 200:
            return None
        buf, total = [], 0
        for chunk in resp.iter_content(chunk_size=65536):
            total += len(chunk)
            buf.append(chunk)
            if total >= max_bytes:
                break
    raw = b"".join(buf)
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("utf-8", "ignore")


def smart_decode(text: str) -> str:
    """Return the payload as a plain proxy list; decode base64 blobs."""
    stripped = text.strip()
    if (
        SCHEME_RE.search(stripped)
        or YAML_NODE_RE.search(text)
        or JSON_NODE_RE.search(text)
    ):
        return text
    compact = re.sub(r"\s+", "", stripped)
    for variant in (compact, compact.replace("-", "+").replace("_", "/")):
        padded = variant + "=" * (-len(variant) % 4)
        try:
            decoded = base64.b64decode(padded, validate=True).decode("utf-8", "ignore")
        except Exception:
            continue
        if (
            SCHEME_RE.search(decoded)
            or YAML_NODE_RE.search(decoded)
            or JSON_NODE_RE.search(decoded)
        ):
            return decoded
    return text


def count_nodes(text: str) -> int:
    n = len(SCHEME_RE.findall(text))
    if n:
        return n
    return len(YAML_NODE_RE.findall(text)) + len(JSON_NODE_RE.findall(text))


def normalize_url(u: str) -> str:
    """Clean up a URL; returns '' for anything that is not an http(s) link."""
    u = (u or "").strip().strip('"').strip("'")
    u = u.rstrip(",;")
    u = u.split("#", 1)[0].strip()
    if not HTTP_RE.match(u):
        return ""
    return u


def dedupe_key(u: str):
    """Two links are 'the same' when scheme/host/path match (query ignored)."""
    try:
        parts = urlsplit(u)
        host = parts.netloc.lower()
        scheme = parts.scheme.lower()
        if scheme == "https" and host.endswith(":443"):
            host = host[:-4]
        if scheme == "http" and host.endswith(":80"):
            host = host[:-3]
        return (scheme, host, parts.path.rstrip("/"))
    except ValueError:
        return (u.lower(), "", "")

# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #
def validate_url(url: str):
    """Return (ok, reason, node_count) for one subscription URL."""
    reason = "unreachable"
    for attempt in range(1, RETRIES + 1):
        try:
            text = fetch(url)
            if text is not None:
                nodes = count_nodes(smart_decode(text))
                if nodes >= MIN_PROXIES:
                    return True, f"{nodes} nodes", nodes
                return False, f"no usable payload ({nodes} nodes)", nodes
            reason = f"http error (status != 200)"
        except requests.exceptions.Timeout:
            reason = "timeout"
        except requests.exceptions.ConnectionError:
            reason = "connection error"
        except requests.exceptions.RequestException as exc:
            reason = type(exc).__name__
        if attempt < RETRIES:
            time.sleep(1.5)
    return False, reason, 0


def validate_many(urls):
    results = {}
    if not urls:
        return results
    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(validate_url, u): u for u in urls}
        for fut in as_completed(futures):
            u = futures[fut]
            try:
                results[u] = fut.result()
            except Exception as exc:  # defensive: never let one URL kill the run
                results[u] = (False, f"internal: {exc}", 0)
            done += 1
            if done % 20 == 0 or done == len(futures):
                log(f"  tested {done}/{len(futures)}")
    return results

# --------------------------------------------------------------------------- #
# Discovery of public collectors
# --------------------------------------------------------------------------- #
def recently_active(pushed_at: str, max_age_days: int = 120) -> bool:
    if not pushed_at:
        return False
    try:
        dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - dt).days <= max_age_days
    except ValueError:
        return True


def _gh_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "sub-dff-updater",
    }
    if GH_TOKEN:
        headers["Authorization"] = f"Bearer {GH_TOKEN}"
    return headers


def github_repos():
    """Query the public GitHub repo search API for aggregator/collector repos.

    Returns [(full_name, default_branch, stars)] sorted by stars, best first.
    """
    repos = {}
    for query in SEARCH_QUERIES:
        try:
            resp = _session.get(
                "https://api.github.com/search/repositories",
                params={"q": query, "sort": "updated", "order": "desc", "per_page": 15},
                headers=_gh_headers(),
                timeout=20,
            )
        except requests.exceptions.RequestException as exc:
            log(f"  search '{query}' failed: {type(exc).__name__}")
            continue
        if resp.status_code != 200:
            log(f"  search '{query}' -> HTTP {resp.status_code} (rate limit? continuing)")
            continue
        try:
            items = resp.json().get("items", [])
        except ValueError:
            items = []
        for item in items:
            name = item.get("full_name") or ""
            if not name or item.get("archived"):
                continue
            if not recently_active(item.get("pushed_at") or ""):
                continue
            repos[name] = (
                item.get("stargazers_count") or 0,
                (item.get("default_branch") or "").strip(),
            )
        log(f"  search '{query}': {len(repos)} unique active repos so far")
        time.sleep(SEARCH_SLEEP)
    ranked = sorted(repos.items(), key=lambda kv: -kv[1][0])[:MAX_REPOS]
    log(f"github search: {len(ranked)} candidate repos")
    return [(name, branch or "main", stars) for name, (stars, branch) in ranked]


def _fetch_tree(full_name: str, branch: str):
    """List all files inside a repo via the git trees API (None on failure)."""
    try:
        resp = _session.get(
            f"https://api.github.com/repos/{full_name}/git/trees/{branch}",
            params={"recursive": "1"},
            headers=_gh_headers(),
            timeout=25,
        )
        if resp.status_code != 200:
            return None
        return resp.json().get("tree", [])
    except (ValueError, requests.exceptions.RequestException):
        return None


def repo_sub_file_candidates(full_name: str, branch: str):
    """Pick the likely subscription files from the repo's OWN file tree."""
    branches, seen_b = [], set()
    for b in ((branch or "").strip(), "main", "master"):
        if b and b not in seen_b:
            seen_b.add(b)
            branches.append(b)
    tree, used_branch = None, None
    for br in branches:
        tree = _fetch_tree(full_name, br)
        if tree:
            used_branch = br
            break
    if not tree:
        return []
    scored = []
    for item in tree:
        if item.get("type") != "blob":
            continue
        path = item.get("path") or ""
        if not path or TREE_EXCLUDE_RE.search(path):
            continue
        low = path.lower()
        if low.endswith(TREE_BAD_EXT):
            continue
        size = item.get("size")
        if size is not None and (size < 500 or size > 30_000_000):
            continue
        score = 0
        if TREE_HINT_RE.search(low):
            score += 2
        if "/" not in low:
            score += 1
        if low.count("/") <= 1:
            score += 1
        scored.append((-score, path))
    scored.sort()
    return [
        f"https://raw.githubusercontent.com/{full_name}/{used_branch}/{quote(path, safe='/')}"
        for _s, path in scored[:FILES_PER_REPO]
    ]


def readme_candidates(full_name: str, branch: str):
    """Scrape the repo README for advertised subscription endpoints."""
    for readme in ("README.md", "readme.md"):
        try:
            text = fetch(
                f"https://raw.githubusercontent.com/{full_name}/{branch}/{readme}",
                max_bytes=1_000_000,
            )
        except requests.exceptions.RequestException:
            continue
        if not text:
            continue
        cands = []
        for u in README_URL_RE.findall(text):
            u = normalize_url(u)
            if not u:
                continue
            low = u.lower()
            if (
                SUB_HINT_RE.search(low)
                or low.endswith((".txt", ".yaml", ".yml"))
                or "raw.githubusercontent" in low
                or "jsdelivr" in low
            ):
                cands.append(u)
        cands.sort(key=lambda x: 0 if "raw.githubusercontent" in x.lower() else 1)
        return cands
    return []


def build_candidates(excluded_keys):
    """Build the discovery candidate pool, 100% dynamically.

    1. subscription files taken straight out of each searched repo's file tree
       (round-robin so one repo does not monopolize the first chunks),
    2. endpoints advertised in each repo's README.
    """
    repos = github_repos()  # best (highest stars) first
    ordered, seen = [], set(excluded_keys)

    def add(url):
        url = normalize_url(url)
        if not url:
            return
        key = dedupe_key(url)
        if key in seen:
            return
        seen.add(key)
        ordered.append(url)

    pools = [repo_sub_file_candidates(name, branch) for name, branch, _stars in repos]
    for i in range(3):  # top 3 files of every repo, mixed across repos
        for pool in pools:
            if i < len(pool):
                add(pool[i])
    for pool in pools:  # remaining files
        for url in pool[3:]:
            add(url)
    for name, branch, _stars in repos[:README_REPOS]:
        for url in readme_candidates(name, branch)[:PER_REPO_README_URLS]:
            add(url)
    return ordered


def discover(candidates):
    """Validate candidates in priority order; keep at most MAX_DISCOVERED."""
    found = []
    total_chunks = (len(candidates) + CHUNK_SIZE - 1) // CHUNK_SIZE
    for i in range(0, len(candidates), CHUNK_SIZE):
        if len(found) >= MAX_DISCOVERED:
            break
        chunk = candidates[i : i + CHUNK_SIZE]
        log(
            f"  validating discovery chunk {i // CHUNK_SIZE + 1}/{total_chunks} "
            f"({len(chunk)} urls), accepted so far: {len(found)}"
        )
        results = validate_many(chunk)
        for u in chunk:
            ok, reason, nodes = results.get(u, (False, "not tested", 0))
            if ok:
                found.append(u)
                log(f"  [+COLLECTOR] {u} ({nodes} nodes)")
                if len(found) >= MAX_DISCOVERED:
                    log(f"  discovery cap reached ({MAX_DISCOVERED}); stopping.")
                    break
    return found

# --------------------------------------------------------------------------- #
# Main pipeline
# --------------------------------------------------------------------------- #
def load_own_lines():
    if not os.path.exists(SUB_FILE):
        log(f"'{SUB_FILE}' not found in repo - starting empty (file will be created).")
        return []
    with open(SUB_FILE, "r", encoding="utf-8-sig") as fh:
        return [ln.strip() for ln in fh.read().splitlines() if ln.strip()]


def write_summary(alive, dead, collectors, total, changed):
    lines = [
        f"## {SUB_FILE} update report",
        "",
        "| مرحله | تعداد |",
        "|---|---|",
        f"| لینک‌های موجود که سالم ماندند | {alive} |",
        f"| لینک‌های مرده که حذف شدند | {dead} |",
        f"| کالکتورهای عمومی تازه‌پیدا‌شده | {collectors} |",
        f"| تعداد نهایی خط‌های {SUB_FILE} | {total} |",
        f"| فایل تغییر کرد؟ | {'بله ✅' if changed else 'خیر'} |",
        "",
        f"_هدف کالکتور: حداقل {MIN_DISCOVERED}، حداکثر {MAX_DISCOVERED}_",
    ]
    text = "\n".join(lines)
    print(text, flush=True)
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        try:
            with open(path, "a", encoding="utf-8") as fh:
                fh.write(text + "\n")
        except OSError:
            pass


def main() -> int:
    log(
        f"SUB-DFF manager start (file={SUB_FILE}, min_proxies={MIN_PROXIES}, "
        f"discover {MIN_DISCOVERED}..{MAX_DISCOVERED}, workers={WORKERS})"
    )

    own_lines = load_own_lines()
    http_links, passthrough = [], []
    for line in own_lines:
        (http_links if HTTP_RE.match(line) else passthrough).append(line)
    if passthrough:
        log(f"keeping {len(passthrough)} non-http line(s) untouched")

    # ---- step 1: validate the links we already have ----------------------- #
    uniq = {}
    for line in http_links:
        u = normalize_url(line)
        if u and u not in uniq:
            uniq[u] = line
    http_links = list(uniq)
    log(f"step 1: validating {len(http_links)} existing subscription link(s) ...")
    results = validate_many(http_links)
    healthy = [u for u in http_links if results.get(u, (False, "not tested", 0))[0]]
    dead = [u for u in http_links if not results.get(u, (False, "not tested", 0))[0]]
    for u in dead:
        log(f"  [-DEAD] {u} -> {results[u][1]}")
    log(f"step 1 done: {len(healthy)} alive, {len(dead)} dead")

    # ---- step 2: discover public collectors -------------------------------- #
    log("step 2: dynamic discovery (github search -> repo file trees -> READMEs) ...")
    excluded = {dedupe_key(u) for u in healthy}
    excluded |= {dedupe_key(u) for u in dead}  # do not re-test known-dead links
    excluded |= {dedupe_key(u) for u in passthrough}
    candidates = build_candidates(excluded)
    log(f"step 2: {len(candidates)} unique candidate endpoints")
    discovered = discover(candidates)
    log(f"step 2 done: {len(discovered)} collector(s) accepted")
    if len(discovered) < MIN_DISCOVERED:
        log(
            f"WARNING: only {len(discovered)} collectors found "
            f"(target minimum {MIN_DISCOVERED}); continuing with what we have."
        )

    # ---- step 3: merge + dedupe + write ------------------------------------ #
    final, seen = [], set()
    for u in passthrough + healthy + discovered:
        key = dedupe_key(u)
        if key in seen:
            continue
        seen.add(key)
        final.append(u)

    if not final:
        log("nothing survived - keeping the existing file untouched.")
        return 1

    old = ""
    if os.path.exists(SUB_FILE):
        with open(SUB_FILE, "r", encoding="utf-8-sig") as fh:
            old = fh.read()
    new = "\n".join(final) + "\n"
    if new == old:
        log("result is identical to the current file - no update needed.")
    else:
        with open(SUB_FILE, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new)
        log(
            f"'{SUB_FILE}' written: {len(final)} links "
            f"(own alive {len(healthy)}, own dead dropped {len(dead)}, "
            f"collectors {len(discovered)}, passthrough {len(passthrough)})"
        )

    write_summary(len(healthy), len(dead), len(discovered), len(final), new != old)
    return 0


if __name__ == "__main__":
    sys.exit(main())
