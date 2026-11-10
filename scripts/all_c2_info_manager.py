#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ALL-C2 INFO manager - classifies proxies by what browserleaks.com/ip says.

Pipeline
  1. Read the raw ALL-C2 list (the live-tested proxy subscription).
  2. Run a real Xray core (same mechanism as the ALL-C2 action): one SOCKS
     inbound per proxy, and through EACH proxy load exactly
     https://browserleaks.com/ip (full page, real load). Country / ISP /
     Organization are taken ONLY from that page's own HTML response - no
     IP-range databases, no local geo lookup, nothing else. A proxy whose
     page does not load is dead and skipped.
  3. Classify into three folders, rebuilt from scratch every run:
       country/<CC>.txt          every proxy, split by country code
       isp/<isp-slug>.txt        every proxy, split by ISP/Organization
       isp/cloudflare.txt        aggregate: Cloudflare exits (and
       isp/non-cloudflare.txt    aggregate: everything else)
       non-cloudflare/<CC>.txt   non-Cloudflare proxies, split by country
     A page that loads but cannot be parsed lands in country/unknown.txt and
     isp/unknown.txt and is excluded from the non-cloudflare view.
  4. The workflow commits and pushes the three folders.
"""

from __future__ import annotations

import html as html_mod
import json
import os
import random
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from all_c2_manager import (  # same scripts/ directory
    WORKDIR,
    USER_AGENTS,
    fetch,
    smart_decode,
    extract_nodes,
    node_key,
    build_config,
    ensure_xray,
    find_free_base,
    _wait_port_ready,
    _win_flags,
    log,
)

ALL_C2_URL   = os.environ.get(
    "ALL_C2_URL",
    "https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/ALL-C2.txt",
)
PAGE_URL      = "https://browserleaks.com/ip"
PAGE_MAX_TIME = int(os.environ.get("PAGE_MAX_TIME", "30"))
INFO_WORKERS  = int(os.environ.get("INFO_WORKERS", "24"))
BATCH_SIZE    = int(os.environ.get("BATCH_SIZE", "100"))
JOB_BUDGET_MIN = float(os.environ.get("JOB_BUDGET_MIN", "35"))

COUNTRY_DIR, ISP_DIR, NONCF_DIR = "country", "isp", "non-cloudflare"

README_FILE = os.environ.get("README_FILE", "README.md")
RAW_BASE = os.environ.get(
    "RAW_BASE",
    "https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main",
)
LINKS_START = "<!-- SUB-LINKS:START -->"
LINKS_END = "<!-- SUB-LINKS:END -->"

# --------------------------------------------------------------------------- #
# browserleaks parsing - the site response is the single source of truth
# --------------------------------------------------------------------------- #
def _row_value(h: str, label: str) -> str:
    m = re.search(
        r"<tr><td>\s*" + re.escape(label) + r"\s*</td>\s*<td>(.*?)</td>",
        h, re.IGNORECASE | re.DOTALL,
    )
    return m.group(1) if m else ""


def _strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html_mod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def parse_browserleaks(h: str):
    """Country / ISP / Organization - extracted only from the page response."""
    info = {"country_code": "", "country": "", "isp": "", "org": ""}
    row = _row_value(h, "Country")
    if row:
        m = re.search(r'<img class="flag-icon"[^>]*title="([^"]+)"', row)
        if m:
            t = html_mod.unescape(m.group(1))
            m2 = re.match(r"\s*(.*?)\s*\(\s*([A-Za-z]{2})\s*\)\s*$", t)
            if m2:
                info["country"], info["country_code"] = m2.group(1).strip(), m2.group(2).upper()
            else:
                info["country"] = t.strip()
        else:
            info["country"] = _strip_tags(re.sub(r'<span class="row-tag">.*', "", row, flags=re.DOTALL))
        if not info["country_code"]:
            mc = re.search(r'data-iso_code="([A-Za-z]{2})"', row)
            if mc:
                info["country_code"] = mc.group(1).upper()
    info["isp"] = _strip_tags(_row_value(h, "ISP"))
    info["org"] = _strip_tags(_row_value(h, "Organization"))
    return info


def looks_like_real_page(h: str) -> bool:
    low = (h or "").lower()
    return ("browserleaks" in low) or ("browser leaks" in low) or ("my ip address" in low)


def fetch_page_via_proxy(port: int) -> str:
    """Really load https://browserleaks.com/ip through this proxy's tunnel."""
    cmd = [
        "curl", "-sS", "-L",
        "-A", random.choice(USER_AGENTS),
        "--socks5-hostname", f"127.0.0.1:{port}",
        "--connect-timeout", "8",
        "--max-time", str(PAGE_MAX_TIME),
        PAGE_URL,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=PAGE_MAX_TIME + 10, **_win_flags())
        return (r.stdout or b"").decode("utf-8", "ignore")
    except Exception:
        return ""

# --------------------------------------------------------------------------- #
# Classification
# --------------------------------------------------------------------------- #
def slugify(name: str, max_len: int = 40) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return (s[:max_len].rstrip("-")) or "unknown"


def is_cloudflare(info) -> bool:
    return "cloudflare" in f"{info['isp']} {info['org']}".lower()


def country_key(info) -> str:
    cc = (info["country_code"] or "").strip().upper()
    if cc:
        return cc
    return slugify(info["country"]) if info["country"] else "unknown"


def isp_key(info) -> str:
    name = info["isp"] or info["org"]
    return slugify(name) if name else "unknown"


def reset_dirs():
    for d in (COUNTRY_DIR, ISP_DIR, NONCF_DIR):
        if os.path.isdir(d):
            for f in os.listdir(d):
                if f.lower().endswith(".txt"):
                    try:
                        os.remove(os.path.join(d, f))
                    except OSError:
                        pass
        os.makedirs(d, exist_ok=True)


def write_files(base_dir: str, mapping: dict) -> int:
    for fname, lines in sorted(mapping.items()):
        with open(os.path.join(base_dir, fname), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines) + "\n")
    return len(mapping)


def classify(entries):
    """entries: list of {uri, country_code, country, isp, org} dicts."""
    country_files, isp_files, noncf_files = {}, {}, {}
    cf_count = 0
    for e in entries:
        uri = e["uri"]
        ckey = country_key(e)
        ikey = isp_key(e)
        country_files.setdefault(f"{ckey}.txt", []).append(uri)
        isp_files.setdefault(f"{ikey}.txt", []).append(uri)
        if is_cloudflare(e):
            cf_count += 1
            isp_files.setdefault("cloudflare.txt", []).append(uri)
        else:
            isp_files.setdefault("non-cloudflare.txt", []).append(uri)
            if ikey != "unknown":  # CF-ness of unknown-ISP exits is unknowable
                noncf_files.setdefault(f"{ckey}.txt", []).append(uri)
    return country_files, isp_files, noncf_files, cf_count

# --------------------------------------------------------------------------- #
# Auto-updating "Subscription Links" section of README.md
# --------------------------------------------------------------------------- #
def count_lines(path: str) -> int:
    try:
        with open(path, "r", encoding="utf-8-sig") as fh:
            return sum(1 for ln in fh if ln.strip())
    except OSError:
        return 0


def _files_in(directory: str):
    if not os.path.isdir(directory):
        return []
    return sorted(f for f in os.listdir(directory) if f.lower().endswith(".txt"))


def build_links_section() -> str:
    """Regenerate the whole Subscription-Links block: links appear or vanish
    together with the .txt files inside the three folders."""
    def bullets(directory: str, label_fn):
        files = _files_in(directory)
        if not files:
            return ["_(empty right now)_"]
        return [
            f"- [{label_fn(f[:-4])}]({RAW_BASE}/{directory}/{f}) · {count_lines(os.path.join(directory, f))} proxies"
            for f in files
        ]

    return "\n".join([
        "## 📡 Subscription Links",
        "",
        "Import these raw URLs into any Xray-compatible client (v2rayN, v2rayNG, Hiddify, Streisand, NekoBox…).",
        "",
        "| Subscription | Raw link |",
        "|---|---|",
        f"| `SUB-DFF.txt` — curated & validated subscription links | {RAW_BASE}/SUB-DFF.txt |",
        f"| `ALL-C2.txt` — tunnel-tested proxies only (≥ 2/3 sites) | {RAW_BASE}/ALL-C2.txt |",
        "",
        f"### 🌍 By country — `country/`",
        *bullets(COUNTRY_DIR, str.upper),
        "",
        f"### 🏢 By ISP / Organization — `isp/`",
        *bullets(ISP_DIR, str),
        "",
        f"### 🚫 Non-Cloudflare, by country — `non-cloudflare/`",
        *bullets(NONCF_DIR, str.upper),
    ])


def update_readme(section_md: str) -> bool:
    """Splice the regenerated block between the SUB-LINKS markers."""
    if not os.path.exists(README_FILE):
        return False
    with open(README_FILE, "r", encoding="utf-8") as fh:
        content = fh.read()
    block = f"{LINKS_START}\n{section_md}\n{LINKS_END}"
    if LINKS_START in content and LINKS_END in content:
        pre, rest = content.split(LINKS_START, 1)
        _, post = rest.split(LINKS_END, 1)
        new = pre + block + post
    else:
        new = content.rstrip("\n") + "\n\n" + block + "\n"
    if new == content:
        return False
    with open(README_FILE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new)
    return True


# --------------------------------------------------------------------------- #
# Main pipeline
# --------------------------------------------------------------------------- #
def load_proxies():
    text = fetch(ALL_C2_URL)
    if not text and os.path.exists("ALL-C2.txt"):
        log("raw ALL-C2 unreachable - falling back to the local checkout copy")
        with open("ALL-C2.txt", "r", encoding="utf-8-sig") as fh:
            text = fh.read()
    if not text:
        return []
    return extract_nodes(smart_decode(text))[0]


def test_batch(xray: str, batch, results: list, dead: list) -> None:
    """One xray process; every proxy gets its own browserleaks page load."""
    if not batch:
        return
    base = find_free_base(len(batch))
    cfg, pairs = build_config(batch, base)
    if not pairs:
        return
    cfg_path = os.path.join(WORKDIR, f"info-{int(time.time() * 1000)}.json")
    err_path = cfg_path + ".err"
    with open(cfg_path, "w", encoding="utf-8") as fh:
        json.dump(cfg, fh)
    with open(err_path, "wb") as err_fh:
        proc = subprocess.Popen(
            [xray, "run", "-c", cfg_path],
            stdout=err_fh, stderr=subprocess.STDOUT, **_win_flags(),
        )
        try:
            if proc.poll() is not None or not _wait_port_ready(pairs[0][1], timeout=6.0):
                log(f"  xray failed to start for info batch ({len(batch)} proxies) - splitting")
                if len(batch) >= 4:
                    mid = len(batch) // 2
                    test_batch(xray, batch[:mid], results, dead)
                    test_batch(xray, batch[mid:], results, dead)
                return
            done = 0
            with ThreadPoolExecutor(max_workers=INFO_WORKERS) as pool:
                futures = {pool.submit(fetch_page_via_proxy, port): node for node, port in pairs}
                for fut in as_completed(futures):
                    node = futures[fut]
                    html = ""
                    try:
                        html = fut.result()
                    except Exception:
                        html = ""
                    if looks_like_real_page(html):
                        info = parse_browserleaks(html)
                        info["uri"] = node["uri"]
                        results.append(info)
                    else:
                        dead.append(node["uri"])
                    done += 1
                    if done % 10 == 0 or done == len(futures):
                        log(f"  loaded {done}/{len(futures)} pages "
                            f"({len(results)} parsed, {len(dead)} dead so far)")
        finally:
            proc.terminate()
            try:
                proc.wait(5)
            except Exception:
                proc.kill()
            try:
                os.remove(cfg_path)
                os.remove(err_path)
            except OSError:
                pass


def write_summary(read, dead, parsed, unknown, cf, countries, isps, files):
    lines = [
        "## ALL-C2 INFO report",
        "",
        "| مرحله | تعداد |",
        "|---|---|",
        f"| پروکسی خوانده‌شده از ALL-C2 | {read} |",
        f"| مرده (صفحه لود نشد) | {dead} |",
        f"| لود موفق با اطلاع کامل | {parsed} |",
        f"| لود موفق بدون اطلاعات (unknown) | {unknown} |",
        f"| خروجی Cloudflare | {cf} |",
        f"| تعداد کشورها | {countries} |",
        f"| تعداد ISP ها | {isps} |",
        f"| تعداد فایل‌های ساخته‌شده | {files} |",
        "",
        f"_منبع اطلاعات: پاسخ HTML دقیقاً `https://browserleaks.com/ip` از تونل هر پروکسی_",
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
    started = time.time()
    log(f"ALL-C2 INFO manager start (source={ALL_C2_URL}, page={PAGE_URL}, "
        f"workers={INFO_WORKERS}, batch={BATCH_SIZE}, page_timeout={PAGE_MAX_TIME}s)")

    nodes = load_proxies()
    log(f"step 1: {len(nodes)} proxy(ies) read from ALL-C2")
    if not nodes:
        log("nothing to classify - ALL-C2 is empty/unreachable.")
        return 1

    xray = ensure_xray(WORKDIR)
    log(f"xray binary ready: {xray}")

    results, dead = [], []
    batches = [nodes[i:i + BATCH_SIZE] for i in range(0, len(nodes), BATCH_SIZE)]
    for idx, batch in enumerate(batches, 1):
        if time.time() - started > JOB_BUDGET_MIN * 60:
            log(f"WARNING: job budget ({JOB_BUDGET_MIN} min) reached - "
                f"classifying {idx - 1}/{len(batches)} batches only.")
            break
        log(f"step 2: batch {idx}/{len(batches)} ({len(batch)} proxies) ...")
        test_batch(xray, batch, results, dead)

    parsed = [e for e in results if e["isp"] or e["org"] or e["country_code"]]
    unknown = len(results) - len(parsed)
    cf_count = sum(1 for e in parsed if "cloudflare" in f"{e['isp']} {e['org']}".lower())
    log(f"step 2 done: {len(results)} page(s) loaded, {len(dead)} dead skipped, "
        f"{len(parsed)} with info, {unknown} unknown, {cf_count} cloudflare")

    if not results:
        log("no page could be loaded - keeping existing folders untouched.")
        return 1 if not os.path.exists(os.path.join(COUNTRY_DIR, "unknown.txt")) else 0

    # ---- step 3: classify into the three folders --------------------------- #
    log("step 3: classifying into country/ isp/ non-cloudflare/ ...")
    reset_dirs()
    country_files, isp_files, noncf_files, cf_count = classify(results)
    n_files = write_files(COUNTRY_DIR, country_files)
    n_files += write_files(ISP_DIR, isp_files)
    n_files += write_files(NONCF_DIR, noncf_files)
    log(f"step 3 done: {n_files} file(s) written "
        f"({len(country_files)} country, {len(isp_files)} isp, {len(noncf_files)} non-cloudflare)")

    # step 4: refresh the auto-updating Subscription-Links section in README
    try:
        changed = update_readme(build_links_section())
        log(f"step 4: README subscription-links section {'updated' if changed else 'unchanged'}")
    except Exception as exc:
        log(f"step 4: README update skipped ({type(exc).__name__}: {exc})")

    write_summary(
        read=len(nodes), dead=len(dead), parsed=len(parsed), unknown=unknown,
        cf=cf_count, countries=len(country_files), isps=len(isp_files), files=n_files,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
