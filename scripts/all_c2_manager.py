#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ALL-C2 manager - real Xray live-testing pipeline.

Pipeline
  1. Sources: the raw ALL-C2 file itself (ALWAYS, so proxies that survived
     previous rounds are re-tested every run) + every http(s) line of
     SUB_FILE (SUB-DFF.txt). Fetch them all and extract EVERY supported
     proxy URI (vmess / vless / trojan / ss) - no limit. Protocols Xray-core
     does not implement (ssr, hysteria, tuic, ...) are skipped.
  2. Simple TCP ping: plain TCP connect latency to server:port for every
     proxy; unreachable ones are dropped, the rest are sorted fastest-first.
  3. Real-time test: download the latest Xray-core release, PREVALIDATE every
     candidate's outbound config with `xray run -test` (parallel) so one bad
     node can never kill a whole batch, then run xray as one process per
     batch with one SOCKS inbound per proxy, and through each proxy request
     3 sites over the REAL tunnel:
       youtube     https://www.youtube.com/generate_204
       google      https://www.google.com/generate_204
       cloudflare  https://www.cloudflare.com/cdn-cgi/trace
     A proxy passes when at least PASSES_REQUIRED (default 2) of the 3
     sites answer through it.
  4. Survivors are written to ALL_C2_FILE (created if missing); the workflow
     commits and pushes it.

No user secrets required.
"""

from __future__ import annotations

import asyncio
import base64
import itertools
import json
import os
import platform
import re
import socket
import subprocess
import sys
import tempfile
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import parse_qs, unquote, urlsplit

import requests

# --------------------------------------------------------------------------- #
# Configuration (env-overridable)
# --------------------------------------------------------------------------- #
SUB_FILE       = os.environ.get("SUB_FILE", "SUB-DFF.txt")
ALL_C2_FILE    = os.environ.get("ALL_C2_FILE", "ALL-C2.txt")
ALL_C2_SELF_URL = os.environ.get(
    "ALL_C2_SELF_URL",
    "https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/ALL-C2.txt",
)
MAX_XRAY_TEST  = int(os.environ.get("MAX_XRAY_TEST", "2000"))
BATCH_SIZE     = int(os.environ.get("BATCH_SIZE", "200"))
XRAY_WORKERS   = int(os.environ.get("XRAY_WORKERS", "16"))
PV_WORKERS     = int(os.environ.get("PV_WORKERS", "16"))
JOB_BUDGET_MIN = float(os.environ.get("JOB_BUDGET_MIN", "55"))
TCP_TIMEOUT    = float(os.environ.get("TCP_TIMEOUT", "4"))
TCP_CONCURRENCY = int(os.environ.get("TCP_CONCURRENCY", "800"))
CURL_MAX_TIME  = int(os.environ.get("CURL_MAX_TIME", "10"))
PASSES_REQUIRED = int(os.environ.get("PASSES_REQUIRED", "2"))
CONNECT_TIMEOUT = float(os.environ.get("CONNECT_TIMEOUT", "10"))
READ_TIMEOUT    = float(os.environ.get("READ_TIMEOUT", "25"))
MAX_BODY_BYTES  = int(os.environ.get("MAX_BODY_BYTES", str(10 * 1024 * 1024)))

WORKDIR = tempfile.mkdtemp(prefix="allc2-")
BASE_PORT = int(os.environ.get("BASE_PORT_START", "31000"))  # fallback start; the actual base is probed at runtime

# 3 sites tested through every proxy (2 of 3 must answer)
TEST_SITES = [
    ("youtube", "https://www.youtube.com/generate_204"),
    ("google", "https://www.google.com/generate_204"),
    ("cloudflare", "https://www.cloudflare.com/cdn-cgi/trace"),
]
OK_CODES = {200, 204, 301, 302, 303, 307, 308}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "v2rayNG/1.8.23",
    "V2rayN/6.45",
]

SCHEME_RE = re.compile(
    r"\b(?:vmess|vless|trojan|ssr|ss|socks5|socks4|socks|hysteria2|hysteria|hy2|"
    r"tuic|juicity|brook|naive|snell|anytls|mieru)://",
    re.IGNORECASE,
)
# Only protocols Xray-core can actually dial are extracted and tested.
PROXY_URI_RE = re.compile(r"\b(?:vmess|vless|trojan|ss)://[^\s\"'<>\\)\]]+", re.IGNORECASE)
HTTP_RE = re.compile(r"^https?://", re.IGNORECASE)

# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
_session = requests.Session()


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def _headers() -> dict:
    import random

    return {"User-Agent": random.choice(USER_AGENTS), "Accept": "*/*"}


def fetch(url: str, max_bytes: int = MAX_BODY_BYTES):
    """GET a URL, return decoded body (capped) or None on non-200."""
    try:
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
    except requests.exceptions.RequestException:
        return None
    raw = b"".join(buf)
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("utf-8", "ignore")


def b64_any(s: str):
    """Robust base64: standard/urlsafe, with or without padding, whitespace."""
    s = re.sub(r"\s+", "", s or "")
    for variant in (s, s.replace("-", "+").replace("_", "/")):
        padded = variant + "=" * (-len(variant) % 4)
        try:
            return base64.b64decode(padded, validate=True)
        except Exception:
            continue
    return None


def smart_decode(text: str) -> str:
    """Decode base64 subscription payloads to plain proxy lists."""
    stripped = text.strip()
    if SCHEME_RE.search(stripped):
        return text
    for variant in (
        re.sub(r"\s+", "", stripped),
        re.sub(r"\s+", "", stripped).replace("-", "+").replace("_", "/"),
    ):
        padded = variant + "=" * (-len(variant) % 4)
        try:
            decoded = base64.b64decode(padded, validate=True).decode("utf-8", "ignore")
        except Exception:
            continue
        if SCHEME_RE.search(decoded):
            return decoded
    return text

# --------------------------------------------------------------------------- #
# Proxy URI parsing
# --------------------------------------------------------------------------- #
def parse_node(uri: str):
    """Parse one proxy URI into {proto, host, port, ident, uri} or None."""
    u = (uri or "").strip()
    low = u.lower()
    try:
        if low.startswith("vmess://"):
            raw = b64_any(u[8:].split("#", 1)[0])
            if raw is None:
                return None
            try:
                data = json.loads(raw.decode("utf-8", "ignore"))
            except Exception:
                return None
            host = str(data.get("add") or "").strip()
            try:
                port = int(data.get("port") or 0)
            except (TypeError, ValueError):
                port = 0
            if not host or not (0 < port < 65536):
                return None
            return {
                "proto": "vmess", "host": host, "port": port,
                "ident": str(data.get("id") or ""), "uri": u,
            }
        if low.startswith("vless://"):
            sp = urlsplit(u)
            if not sp.hostname or not sp.port:
                return None
            return {
                "proto": "vless", "host": sp.hostname, "port": sp.port,
                "ident": unquote(sp.username or ""), "uri": u,
            }
        if low.startswith("trojan://"):
            sp = urlsplit(u)
            if not sp.hostname or not sp.port:
                return None
            return {
                "proto": "trojan", "host": sp.hostname, "port": sp.port,
                "ident": unquote(sp.username or ""), "uri": u,
            }
        if low.startswith("ss://"):
            body = u[5:].split("#", 1)[0]
            main = body.split("?", 1)[0]
            if "@" in main:
                userinfo, _, hostport = main.rpartition("@")
                raw = b64_any(userinfo)
                if raw is not None:
                    mp = raw.decode("utf-8", "ignore")
                else:
                    mp = unquote(userinfo)
                if ":" not in mp:
                    return None
                sp = urlsplit("//" + hostport)
                if not sp.hostname or not sp.port:
                    return None
                return {
                    "proto": "ss", "host": sp.hostname, "port": sp.port,
                    "ident": mp, "uri": u,
                }
            # legacy: whole body is base64(method:password@host:port)
            raw = b64_any(main)
            if raw is None:
                return None
            mp, _, hostport = raw.decode("utf-8", "ignore").rpartition("@")
            if not mp or ":" not in hostport:
                return None
            host, _, port = hostport.rpartition(":")
            try:
                port = int(port)
            except ValueError:
                return None
            if not host or not (0 < port < 65536):
                return None
            return {
                "proto": "ss", "host": host, "port": port, "ident": mp, "uri": u,
            }
    except Exception:
        return None
    return None  # unsupported scheme


def node_key(node) -> tuple:
    return (node["proto"], node["host"].lower(), node["port"], node["ident"])


def extract_nodes(text: str):
    """Extract every supported proxy URI from a payload, deduped by node key."""
    found, order, skipped = {}, [], 0
    for m in PROXY_URI_RE.finditer(text or ""):
        uri = m.group(0).rstrip(".,;")
        node = parse_node(uri)
        if node is None:
            skipped += 1
            continue
        key = node_key(node)
        if key not in found:
            found[key] = node
            order.append(key)
    return [found[k] for k in order], skipped

# --------------------------------------------------------------------------- #
# Xray outbound builders (one JSON outbound per proxy URI)
# --------------------------------------------------------------------------- #
def _qs(uri: str) -> dict:
    return {k: v[-1] for k, v in parse_qs(urlsplit(uri).query).items()}


def _net_settings(net: str, params: dict, host: str):
    """Stream settings for the chosen transport network."""
    net = {"raw": "tcp"}.get((net or "").lower(), (net or "").lower())
    stream = {"network": net}
    if net == "ws":
        ws = {"path": params.get("path") or "/"}
        if params.get("host"):
            ws["headers"] = {"Host": params["host"]}
        stream["wsSettings"] = ws
    elif net == "grpc":
        stream["grpcSettings"] = {"serviceName": (params.get("serviceName") or params.get("path") or "").strip("/")}
    elif net in ("h2", "http"):
        stream["network"] = "http"
        stream["httpSettings"] = {
            "host": [params.get("host") or host],
            "path": params.get("path") or "/",
        }
    elif net == "tcp" and (params.get("headerType") or params.get("type")) == "http":
        stream["tcpSettings"] = {"header": {"type": "http", "request": {
            "path": [params.get("path") or "/"],
            "headers": {"Host": [params.get("host") or host]},
        }}}
    return stream


def vmess_outbound(node, tag, allow_insecure=True):
    raw = b64_any(node["uri"][8:].split("#", 1)[0])
    data = json.loads(raw.decode("utf-8", "ignore"))
    host = str(data.get("add") or "").strip()
    port = int(data.get("port") or 0)
    if not host or not (0 < port < 65536):
        raise ValueError("bad vmess address")
    params = {"path": data.get("path"), "host": data.get("host"),
              "type": data.get("type"), "headerType": data.get("type")}
    net = (data.get("net") or "tcp").lower()
    stream = _net_settings(net, params, host)
    tls = (data.get("tls") or "").lower()
    if tls in ("tls", "reality"):
        stream["security"] = "tls"
        # NOTE: recent Xray-core removed "allowInsecure"; the current key is "insecure".
        stream["tlsSettings"] = {
            "insecure": allow_insecure,
            "serverName": data.get("sni") or data.get("host") or host,
            "fingerprint": data.get("fp") or "chrome",
        }
        if data.get("alpn"):
            stream["tlsSettings"]["alpn"] = [a for a in str(data["alpn"]).split(",") if a]
    # sanitize the vmess cipher: unknown values make xray reject the whole config
    scy = str(data.get("scy") or "auto").strip().lower()
    if scy not in ("auto", "none", "zero", "aes-128-gcm", "chacha20-poly1305", "chacha20-ietf-poly1305"):
        scy = "auto"
    return {
        "tag": tag, "protocol": "vmess",
        "settings": {"vnext": [{"address": host, "port": port, "users": [{
            "id": data.get("id") or "",
            "alterId": int(data.get("aid") or 0),
            "security": scy,
            "level": 8,
        }]}]},
        "streamSettings": stream,
    }


def vless_outbound(node, tag, allow_insecure=True):
    u = urlsplit(node["uri"])
    q = _qs(node["uri"])
    if not u.hostname or not u.port:
        raise ValueError("bad vless address")
    net = (q.get("type") or "tcp").lower()
    sec = (q.get("security") or "").lower()
    stream = _net_settings(net, q, u.hostname)
    if sec == "reality":
        stream["security"] = "reality"
        stream["realitySettings"] = {
            "serverName": q.get("sni") or u.hostname,
            "fingerprint": q.get("fp") or "chrome",
            "publicKey": q.get("pbk") or "",
            "shortId": q.get("sid") or "",
            "spiderX": q.get("spx") or "/",
        }
    elif sec == "tls":
        stream["security"] = "tls"
        ts = {
            "insecure": allow_insecure,
            "serverName": q.get("sni") or u.hostname,
            "fingerprint": q.get("fp") or "chrome",
        }
        if q.get("alpn"):
            ts["alpn"] = [a for a in q["alpn"].split(",") if a]
        stream["tlsSettings"] = ts
    user = {"id": unquote(u.username or ""), "encryption": "none", "level": 8}
    # vision flow is only valid on plain TCP; attaching it to ws/grpc makes
    # xray reject the whole config, so keep it only where it is legal
    flow = (q.get("flow") or "").strip().lower()
    if flow and net in ("tcp",) and flow.startswith("xtls-rprx-vision"):
        user["flow"] = flow
    return {
        "tag": tag, "protocol": "vless",
        "settings": {"vnext": [{"address": u.hostname, "port": u.port, "users": [user]}]},
        "streamSettings": stream,
    }


def trojan_outbound(node, tag, allow_insecure=True):
    u = urlsplit(node["uri"])
    q = _qs(node["uri"])
    if not u.hostname or not u.port:
        raise ValueError("bad trojan address")
    net = (q.get("type") or "tcp").lower()
    stream = _net_settings(net, q, u.hostname)
    stream["security"] = "tls"
    stream["tlsSettings"] = {
        "insecure": allow_insecure,
        "serverName": q.get("sni") or q.get("peer") or u.hostname,
        "fingerprint": q.get("fp") or "chrome",
    }
    return {
        "tag": tag, "protocol": "trojan",
        "settings": {"servers": [{
            "address": u.hostname, "port": u.port,
            "password": unquote(u.username or ""), "level": 8,
        }]},
        "streamSettings": stream,
    }


def ss_outbound(node, tag):
    u = node["uri"][5:].split("#", 1)[0]
    main = u.split("?", 1)[0]
    if "@" in main:
        userinfo, _, hostport = main.rpartition("@")
        raw = b64_any(userinfo)
        mp = raw.decode("utf-8", "ignore") if raw is not None else unquote(userinfo)
        method, password = mp.split(":", 1)
        sp = urlsplit("//" + hostport)
        if not sp.hostname or not sp.port:
            raise ValueError("bad ss address")
        address, port = sp.hostname, sp.port
    else:
        raw = b64_any(main)
        if raw is None:
            raise ValueError("bad ss payload")
        mp, _, hostport = raw.decode("utf-8", "ignore").rpartition("@")
        if not mp or ":" not in mp:
            raise ValueError("bad ss payload")
        method, password = mp.split(":", 1)
        host, _, port = hostport.rpartition(":")
        address, port = host.strip("[]"), int(port)
    if not ss_supported(method, password):
        raise ValueError(f"unsupported ss cipher: {method}")
    return {
        "tag": tag, "protocol": "shadowsocks",
        "settings": {"servers": [{
            "address": address, "port": port,
            "method": method.strip(), "password": password, "level": 8,
        }]},
    }


def make_outbound(node, tag):
    proto = node["proto"]
    if proto == "vmess":
        return vmess_outbound(node, tag)
    if proto == "vless":
        return vless_outbound(node, tag)
    if proto == "trojan":
        return trojan_outbound(node, tag)
    if proto == "ss":
        return ss_outbound(node, tag)
    raise ValueError(f"unsupported protocol {proto}")


# Ciphers current Xray-core still accepts ("aes-256-cfb" & other stream
# ciphers were removed). Values = required key byte length for the 2022
# family; None = password is free-form text.
SS_METHODS = {
    "aes-128-gcm": None,
    "aes-256-gcm": None,
    "chacha20-poly1305": None,
    "chacha20-ietf-poly1305": None,
    "xchacha20-poly1305": None,
    "xchacha20-ietf-poly1305": None,
    "2022-blake3-aes-128-gcm": 16,
    "2022-blake3-aes-256-gcm": 32,
    "2022-blake3-chacha20-poly1305": 32,
    "none": None,
}


def ss_supported(method: str, password: str) -> bool:
    key = (method or "").strip().lower().replace("_", "-")
    need = SS_METHODS.get(key)
    if key not in SS_METHODS:
        return False
    if need:  # 2022 family: password must be a base64 key of exact length
        raw = b64_any(password)
        if raw is None or len(raw) != need:
            return False
    return True

# --------------------------------------------------------------------------- #
# Step 2: TCP ping
# --------------------------------------------------------------------------- #
async def tcp_ping_all(nodes):
    sem = asyncio.Semaphore(TCP_CONCURRENCY)
    results = {}

    async def one(node):
        async with sem:
            t0 = time.perf_counter()
            try:
                _, writer = await asyncio.wait_for(
                    asyncio.open_connection(node["host"], node["port"]),
                    timeout=TCP_TIMEOUT,
                )
                writer.close()
                try:
                    await writer.wait_closed()
                except Exception:
                    pass
                results[node["uri"]] = round((time.perf_counter() - t0) * 1000)
            except Exception:
                results[node["uri"]] = None

    await asyncio.gather(*(one(n) for n in nodes))
    return results

# --------------------------------------------------------------------------- #
# Xray core setup
# --------------------------------------------------------------------------- #
def ensure_xray(workdir: str) -> str:
    sysname = platform.system().lower()
    is_win = "windows" in sysname
    asset = "Xray-windows-64.zip" if is_win else "Xray-linux-64.zip"
    wanted = "xray.exe" if is_win else "xray"
    for root, _dirs, files in os.walk(workdir):
        for f in files:
            if f.lower() == wanted:
                path = os.path.join(root, f)
                os.chmod(path, 0o755)
                return path
    url = f"https://github.com/XTLS/Xray-core/releases/latest/download/{asset}"
    log(f"downloading latest Xray-core ({asset}) ...")
    zip_path = os.path.join(workdir, "xray.zip")
    last_exc = None
    for attempt in (1, 2):  # release CDN hiccups happen; one retry is cheap
        try:
            with requests.get(url, timeout=(15, 300), stream=True) as r:
                r.raise_for_status()
                with open(zip_path, "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            last_exc = None
            break
        except requests.exceptions.RequestException as exc:
            last_exc = exc
            time.sleep(3)
    if last_exc is not None:
        raise last_exc
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(workdir)
    os.remove(zip_path)
    for root, _dirs, files in os.walk(workdir):
        for f in files:
            if f.lower() == wanted:
                path = os.path.join(root, f)
                os.chmod(path, 0o755)
                return path
    raise RuntimeError("xray binary not found after extraction")


# --------------------------------------------------------------------------- #
# Prevalidation: drop nodes whose config xray rejects BEFORE batching
# --------------------------------------------------------------------------- #
PV_DUMMY_INBOUND = {
    "tag": "dv", "listen": "127.0.0.1", "port": 54321,
    "protocol": "socks", "settings": {"udp": False},
}


def _win_flags():
    return {"creationflags": getattr(subprocess, "CREATE_NO_WINDOW", 0)} if os.name == "nt" else {}


def _xray_test(xray: str, cfg_path: str):
    """`xray run -test` validates the config without launching the server."""
    try:
        r = subprocess.run(
            [xray, "run", "-test", "-c", cfg_path],
            capture_output=True, text=True, timeout=25, **_win_flags(),
        )
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, ""
    except OSError as exc:
        return 1, str(exc)


def prevalidate_nodes(xray: str, nodes):
    """Validate every node's outbound with `xray run -test`, in parallel.

    One config xray cannot build kills the WHOLE batch (that is what caused
    the split-storm), so poisoned nodes are dropped here, before batching.
    Nodes are returned in their original (latency-sorted) order.
    """
    if not nodes:
        return nodes
    sanity = {
        "inbounds": [PV_DUMMY_INBOUND],
        "outbounds": [{"tag": "v", "protocol": "freedom", "settings": {}}],
        "routing": {"domainStrategy": "AsIs", "rules": []},
    }
    path = os.path.join(WORKDIR, "pv-sanity.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(sanity, fh)
    rc, _out = _xray_test(xray, path)
    if rc != 0:
        log(f"prevalidate: 'xray -test' unavailable (rc={rc}) - skipping prevalidation")
        return nodes

    tagged, skipped = [], 0
    for node in nodes:
        try:
            ob = make_outbound(node, "v")
            tagged.append((node, ob))
        except Exception:
            skipped += 1

    log(f"prevalidating {len(tagged)} outbound config(s) with 'xray -test' "
        f"({PV_WORKERS} parallel workers) ...")

    def test_one(idx: int, node, ob) -> bool:
        cfg = {
            "inbounds": [PV_DUMMY_INBOUND],
            "outbounds": [ob],
            "routing": {"domainStrategy": "AsIs", "rules": []},
        }
        fp = os.path.join(WORKDIR, f"pv-{idx}.json")
        with open(fp, "w", encoding="utf-8") as fh:
            json.dump(cfg, fh)
        try:
            rc, _out = _xray_test(xray, fp)
        finally:
            try:
                os.remove(fp)
            except OSError:
                pass
        return rc == 0

    ok_flags = [False] * len(tagged)
    done = rejected = 0
    with ThreadPoolExecutor(max_workers=PV_WORKERS) as pool:
        futures = {
            pool.submit(test_one, i, node, ob): i
            for i, (node, ob) in enumerate(tagged)
        }
        for fut in as_completed(futures):
            i = futures[fut]
            try:
                ok_flags[i] = fut.result()
            except Exception:
                ok_flags[i] = False
            done += 1
            rejected += 0 if ok_flags[i] else 1
            if done % 250 == 0 or done == len(tagged):
                log(f"  prevalidated {done}/{len(tagged)} ({rejected} rejected)")
    good = [node for (node, _ob), ok in zip(tagged, ok_flags) if ok]
    extra = f", {skipped} unbuildable in python" if skipped else ""
    log(f"prevalidation done: {len(good)} valid, {rejected} rejected by xray{extra}")
    return good

# --------------------------------------------------------------------------- #
# Step 3: real Xray live test
# --------------------------------------------------------------------------- #
_cfg_counter = itertools.count(1)


def build_config(batch, base_port):
    """One xray config: a SOCKS inbound + dedicated outbound per proxy."""
    inbounds, outbounds, rules, pairs = [], [], [], []
    for node in batch:
        i = len(pairs)  # tag/port only for nodes that actually build
        try:
            out = make_outbound(node, f"t{i}")
        except Exception:
            continue
        port = base_port + i
        inbounds.append({
            "tag": f"in{i}", "listen": "127.0.0.1", "port": port,
            "protocol": "socks", "settings": {"udp": False},
        })
        outbounds.append(out)
        rules.append({"inboundTag": [f"in{i}"], "outboundTag": f"t{i}"})
        pairs.append((node, port))
    cfg = {
        "inbounds": inbounds,
        "outbounds": outbounds,
        "routing": {"domainStrategy": "AsIs", "rules": rules},
    }
    return cfg, pairs


def curl_code(port: int, url: str) -> int:
    cmd = [
        "curl", "-sS", "-o", os.devnull, "-w", "%{http_code}",
        "--socks5-hostname", f"127.0.0.1:{port}",
        "--connect-timeout", "6", "--max-time", str(CURL_MAX_TIME), url,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=CURL_MAX_TIME + 6)
        return int(r.stdout.strip() or 0)
    except Exception:
        return 0


def test_through_port(port: int):
    return [name for name, url in TEST_SITES if curl_code(port, url) in OK_CODES]


def _wait_port_ready(port: int, timeout: float = 6.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.2)
    return False


def _last_err_line(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            lines = [ln.strip() for ln in fh.read().splitlines() if ln.strip()]
        return lines[-1][:180] if lines else ""
    except OSError:
        return ""


_free_base = {"port": None, "size": 0}


def find_free_base(count: int) -> int:
    """Find a contiguous free TCP port range for the inbound pool.

    Fixed ports can be blocked by Windows Hyper-V exclusions, zombie
    listeners, or other local proxy apps - so probe at runtime.
    """
    if _free_base["port"] is not None and _free_base["size"] >= count:
        return _free_base["port"]
    for start in range(BASE_PORT, 65000 - count):
        socks, ok = [], True
        for p in range(start, start + count):
            s = socket.socket()
            try:
                s.bind(("127.0.0.1", p))
                socks.append(s)
            except OSError:
                s.close()
                ok = False
                break
        for s in socks:
            s.close()
        if ok:
            _free_base["port"] = start
            _free_base["size"] = count
            return start
    raise RuntimeError("no contiguous free TCP port range found")


def run_batch(xray: str, batch, results_out: dict) -> None:
    """Run one xray process for the batch; if it fails, split and retry."""
    if not batch:
        return
    base = find_free_base(len(batch))
    cfg, pairs = build_config(batch, base)
    if not pairs:
        return
    if len(pairs) < len(batch):
        log(f"  {len(batch) - len(pairs)} proxy(ies) skipped: unbuildable/unsupported config")
    cfg_path = os.path.join(WORKDIR, f"cfg-{next(_cfg_counter)}.json")
    err_path = cfg_path + ".err"
    with open(cfg_path, "w", encoding="utf-8") as fh:
        json.dump(cfg, fh)
    with open(err_path, "wb") as err_fh:
        proc = subprocess.Popen(
            [xray, "run", "-c", cfg_path],
            stdout=err_fh, stderr=subprocess.STDOUT, **_win_flags(),
        )
        try:
            # poll() first: an instant config-build death must not wait 6s
            if proc.poll() is not None or not _wait_port_ready(pairs[0][1], timeout=6.0):
                tail = _last_err_line(err_path)
                if tail:
                    log(f"  xray: {tail}")
                _free_base["port"] = None  # re-probe ports for the retries
                if len(batch) >= 4:
                    mid = len(batch) // 2
                    log(f"  xray failed on batch of {len(batch)} - splitting ...")
                    run_batch(xray, batch[:mid], results_out)
                    run_batch(xray, batch[mid:], results_out)
                else:
                    log(f"  xray failed on tiny batch - skipping {len(batch)} proxy(ies)")
                return
            done = 0
            with ThreadPoolExecutor(max_workers=XRAY_WORKERS) as pool:
                futures = {pool.submit(test_through_port, port): (node, port) for node, port in pairs}
                for fut in as_completed(futures):
                    node, _port = futures[fut]
                    try:
                        results_out[node["uri"]] = fut.result()
                    except Exception:
                        results_out[node["uri"]] = []
                    done += 1
                    if done % 25 == 0 or done == len(futures):
                        log(f"  live-tested {done}/{len(futures)}")
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

# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def write_summary(sources, extracted, tcp_ok, tested, passed, total, changed, rejected=0):
    lines = [
        "## ALL-C2 live-test report",
        "",
        "| مرحله | تعداد |",
        "|---|---|",
        f"| منابع استخراج (ساب‌ها + خود ALL-C2) | {sources} |",
        f"| پروکسی یکتای استخراج‌شده | {extracted} |",
        f"| TCP پینگ موفق | {tcp_ok} |",
        f"| کانفیگ ردشده در پیش‌ولیدیشن Xray | {rejected} |",
        f"| تست ریل‌تایم با Xray | {tested} |",
        f"| قبول‌شده ({PASSES_REQUIRED} از ۳ سایت) | {passed} |",
        f"| تعداد نهایی خط‌های {ALL_C2_FILE} | {total} |",
        f"| فایل تغییر کرد؟ | {'بله ✅' if changed else 'خیر'} |",
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

# --------------------------------------------------------------------------- #
# Main pipeline
# --------------------------------------------------------------------------- #
def load_own_links():
    if not os.path.exists(SUB_FILE):
        log(f"'{SUB_FILE}' not found - using discovery-free sources (self URL only).")
        return []
    with open(SUB_FILE, "r", encoding="utf-8-sig") as fh:
        return [ln.strip() for ln in fh.read().splitlines() if ln.strip()]


def main() -> int:
    started = time.time()
    log(
        f"ALL-C2 manager start (sub={SUB_FILE}, out={ALL_C2_FILE}, "
        f"tcp_conc={TCP_CONCURRENCY}, max_xray_test={MAX_XRAY_TEST}, "
        f"batch={BATCH_SIZE}, workers={XRAY_WORKERS}, passes={PASSES_REQUIRED}/3)"
    )

    # ---- step 1: gather sources + extract ALL proxies ---------------------- #
    all_nodes, all_keys = [], set()

    def add_text(text, label):
        nodes, skipped = extract_nodes(smart_decode(text))
        fresh = 0
        for n in nodes:
            k = node_key(n)
            if k not in all_keys:
                all_keys.add(k)
                all_nodes.append(n)
                fresh += 1
        log(f"  source '{label}': +{fresh} new proxies "
            f"({len(nodes)} found, {skipped} unparsable skipped)")

    old_text = ""
    if os.path.exists(ALL_C2_FILE):
        with open(ALL_C2_FILE, "r", encoding="utf-8-sig") as fh:
            old_text = fh.read()
    had_old = bool(old_text.strip())
    if old_text.strip():
        add_text(old_text, f"local {ALL_C2_FILE}")

    log(f"fetching self URL: {ALL_C2_SELF_URL}")
    self_text = fetch(ALL_C2_SELF_URL)
    if self_text:
        add_text(self_text, "self ALL-C2 (remote)")
    else:
        log("  self URL not available yet (first run?) - continuing")

    own_links = load_own_links()
    uniq_links, seen_links = [], set()
    for line in own_links:
        if HTTP_RE.match(line):
            n = normalize_link(line)
            if n and n not in seen_links and n != ALL_C2_SELF_URL:
                seen_links.add(n)
                uniq_links.append(n)
    log(f"step 1: {len(uniq_links)} subscription link(s) from {SUB_FILE}")
    for link in uniq_links:
        text = fetch(link)
        if not text:
            log(f"  source '{link}': unreachable")
            continue
        add_text(text, link)
    log(f"step 1 done: {len(all_nodes)} unique proxies extracted (no limit)")

    if not all_nodes:
        log("nothing extracted - keeping existing file untouched.")
        return 0 if had_old else 1

    # ---- step 2: TCP ping everyone ----------------------------------------- #
    log(f"step 2: TCP ping on {len(all_nodes)} proxies "
        f"(timeout {TCP_TIMEOUT}s, concurrency {TCP_CONCURRENCY}) ...")
    tcp = asyncio.run(tcp_ping_all(all_nodes))
    alive = [(ms, n) for n in all_nodes if (ms := tcp.get(n["uri"])) is not None]
    alive.sort(key=lambda x: x[0])
    dead = len(all_nodes) - len(alive)
    log(f"step 2 done: {len(alive)} reachable, {dead} unreachable")

    if not alive:
        log("no proxy answered TCP - keeping existing file untouched.")
        return 0 if had_old else 1

    # ---- step 3: real Xray live test ---------------------------------------- #
    budget = JOB_BUDGET_MIN * 60
    candidates = [n for _ms, n in alive[:MAX_XRAY_TEST]]
    if len(alive) > len(candidates):
        log(f"capping live test to the {len(candidates)} fastest proxies "
            f"(MAX_XRAY_TEST); {len(alive) - len(candidates)} skipped by budget")
    log(f"step 3: live-testing with real Xray core ...")
    xray = ensure_xray(WORKDIR)
    log(f"xray binary ready: {xray}")

    # Prevalidate every candidate config with `xray -test` so one bad node
    # can never kill a whole batch (the split-storm seen in the first run).
    candidates = prevalidate_nodes(xray, candidates)
    if not candidates:
        log("no proxy survived prevalidation - keeping existing file untouched.")
        return 0 if had_old else 1
    pv_rejected = min(len(alive), MAX_XRAY_TEST) - len(candidates)

    passed_uris = set()
    batches = [candidates[i:i + BATCH_SIZE] for i in range(0, len(candidates), BATCH_SIZE)]
    for idx, batch in enumerate(batches, 1):
        if time.time() - started > budget:
            log(f"WARNING: job budget ({JOB_BUDGET_MIN} min) reached - "
                f"testing {idx - 1}/{len(batches)} batches only.")
            break
        log(f"batch {idx}/{len(batches)} ({len(batch)} proxies) ...")
        results = {}
        run_batch(xray, batch, results)
        fresh_pass = sum(1 for sites in results.values() if len(sites) >= PASSES_REQUIRED)
        passed_uris.update(u for u, sites in results.items() if len(sites) >= PASSES_REQUIRED)
        log(f"batch {idx} done: +{fresh_pass} passed, total {len(passed_uris)}")

    log(f"step 3 done: {len(passed_uris)} proxy(ies) passed "
        f"({PASSES_REQUIRED}/{len(TEST_SITES)} sites)")

    # ---- step 4: write ALL-C2 (old survivors first, then new ones) ---------- #
    key_of_uri = {n["uri"]: node_key(n) for n in all_nodes}
    passed_keys = {key_of_uri[u] for u in passed_uris if u in key_of_uri}
    final, seen = [], set()
    for n in all_nodes:  # extraction order = old ALL-C2 content first
        k = node_key(n)
        if k in passed_keys and k not in seen:
            seen.add(k)
            final.append(n["uri"])

    old_norm = old_text.strip()
    new_text = "\n".join(final) + "\n"
    if not final:
        # Free proxies are flaky; a zero-pass round must NOT wipe the list.
        log("no proxy passed the live test - keeping existing file untouched.")
        return 0 if had_old else 1
    if new_text.strip() == old_norm and old_norm:
        log("result identical to current file - no update needed.")
    else:
        with open(ALL_C2_FILE, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(new_text)
        log(f"'{ALL_C2_FILE}' written: {len(final)} proxies "
            f"(previous survivors kept in order, new ones appended)")

    write_summary(
        sources=1 + len(uniq_links),
        extracted=len(all_nodes),
        tcp_ok=len(alive),
        tested=len(candidates),
        passed=len(passed_uris),
        total=len(final),
        changed=new_text.strip() != old_norm or not old_norm,
        rejected=pv_rejected,
    )
    return 0


def normalize_link(u: str) -> str:
    u = (u or "").strip().strip('"').strip("'").rstrip(",;")
    return u.split("#", 1)[0].strip() if HTTP_RE.match(u) else ""


if __name__ == "__main__":
    sys.exit(main())
