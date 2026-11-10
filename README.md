# FLLT-test — Self-Updating Free Proxy Pipeline

This repository runs **three fully automated GitHub Actions** that keep a fresh and **verified** pool of Xray proxy subscriptions — with zero secrets and zero manual work. Everything runs on GitHub's own infrastructure using the built-in `GITHUB_TOKEN`.

Built with the well-known **GLM 5.3 Flash** model (ZCode).

| # | Workflow | Schedule (UTC) | Output |
|---|----------|----------------|--------|
| 1 | **FLLT-test** | every 24 h (06:23) + manual | `SUB-DFF.txt` — curated & validated subscription links |
| 2 | **ALL-C2** | every 12 h (03:23 / 15:23) + manual | `ALL-C2.txt` — proxies that passed a real Xray tunnel test |
| 3 | **ALL-C2-INFO** | every 8 h (01:37 / 09:37 / 17:37) + manual | `country/` · `isp/` · `non-cloudflare/` — classified by live browserleaks data |

## 📡 Subscription Links

Import these raw URLs into any Xray-compatible client (v2rayN, v2rayNG, Hiddify, Streisand, NekoBox…).

<!-- SUB-LINKS:START -->
_This section regenerates automatically on every run of the **ALL-C2-INFO** workflow —
links are added or removed as the `.txt` files inside `country/`, `isp/` and
`non-cloudflare/` appear or disappear._
<!-- SUB-LINKS:END -->

## ⚙️ How It Works

### 1. Subscription Searcher & Checker — `FLLT-test` (every 24 h)

1. **Check what we already have** — every `http(s)` link inside `SUB-DFF.txt` is fetched and must still respond **and** still serve proxies (`vmess` / `vless` / `trojan` / `ss` payloads, plus clash & sing-box YAML). Dead links are dropped.
2. **Discover new collectors — 100 % dynamically, zero hardcoded links** — the public GitHub search API finds active aggregator/collector repositories; the action then walks *inside each repo's own file tree* (git trees API) to pick its actual subscription files (`.txt` / `.yaml` / `.json`), plus the endpoints advertised in each repo's README. Between **10 (target) and 40 (cap)** collectors are kept, and every candidate passes the same validation before it is accepted.
3. **Merge & push** — surviving links + new collectors are merged, deduplicated, and `SUB-DFF.txt` is pushed back to the repository (only when it really changed).

### 2. Proxy Tester — `ALL-C2` (every 12 h)

1. **Extract everything** — every `vmess` / `vless` / `trojan` / `ss` URI from all subscriptions in `SUB-DFF.txt` (no limit), plus the raw `ALL-C2.txt` itself so that survivors of previous rounds are re-tested every run.
2. **TCP ping** — a plain TCP-connect latency check on every proxy (async, ~800 concurrent); unreachable ones are dropped, the rest are sorted fastest-first.
3. **Real tunnel test** — the latest **Xray-core** release is downloaded; every candidate config is pre-validated with `xray run -test` (so one broken node can never kill a batch), then Xray runs with **one dedicated SOCKS inbound per proxy**, and the three sites below are requested *through the real tunnel*:
   - YouTube — `https://www.youtube.com/generate_204`
   - Google — `https://www.google.com/generate_204`
   - Cloudflare — `https://www.cloudflare.com/cdn-cgi/trace`

   A proxy is accepted when **at least 2 of 3** sites answer through it. Survivors are written to `ALL-C2.txt` and pushed.

### 3. Proxy Info Finder — `ALL-C2-INFO` (every 8 h)

1. Every proxy inside the raw `ALL-C2.txt` is loaded through its own Xray tunnel.
2. For each one, **exactly `https://browserleaks.com/ip`** is fetched as a full, real page load. **Country, ISP and Organization are taken only from that page's own HTML response** — no IP-range databases, no local GeoIP, nothing else. The site's answer is the single source of truth. A proxy whose page does not load is dead and skipped.
3. Three folders are rebuilt from scratch and pushed — a new country or ISP automatically creates its own file:
   - `country/<CC>.txt` — every proxy, split by country code
   - `isp/<isp>.txt` — every proxy, split by ISP / Organization (plus the `isp/cloudflare.txt` and `isp/non-cloudflare.txt` aggregates)
   - `non-cloudflare/<CC>.txt` — only non-Cloudflare exits, split by country

   The **Subscription Links** section above regenerates itself on every run.

### Repository layout

```text
SUB-DFF.txt                    curated & validated subscription links   (workflow 1)
ALL-C2.txt                     tunnel-tested proxies                    (workflow 2)
country/<CC>.txt               by country                               (workflow 3)
isp/<isp>.txt                  by ISP / organization                    (workflow 3)
non-cloudflare/<CC>.txt        non-Cloudflare, by country               (workflow 3)
.github/workflows/             the three workflows
scripts/                       the three Python managers
```

**Setup (one time):** upload the files at the exact paths above, then enable
*Settings → Actions → General → Workflow permissions → **Read and write permissions***
(required for the automated pushes). Every workflow can also be triggered manually from the **Actions** tab.
