# FLLT — Self-Updating Free Proxy Pipeline

This repository runs **three fully automated GitHub Actions** that keep a fresh and **verified** pool of Xray proxy subscriptions — with zero secrets and zero manual work. Everything runs on GitHub's own infrastructure using the built-in `GITHUB_TOKEN`.

Built with the well-known **GLM 5.3 Flash** model (ZCode).

| # | Workflow | Schedule (UTC) | Output |
|---|----------|----------------|--------|
| 1 | **FLLT-test** | every 24 h (06:23) + manual | `SUB-DFF.txt` — curated & validated subscription links |
| 2 | **ALL-C2** | every 12 h (03:23 / 15:23) + manual | `ALL-C2.txt` — proxies that passed a real Xray tunnel test |
| 3 | **ALL-C2-INFO** | every 8 h (01:37 / 09:37 / 17:37) + manual | `country/` · `isp/` · `non-cloudflare/` — classified by live browserleaks data |


<!-- SUB-LINKS:START -->
## 📡 Subscription Links

Import these raw URLs into any Xray-compatible client (v2rayN, v2rayNG, Hiddify, Streisand, NekoBox…).

| Subscription | Raw link |
|---|---|
| `SUB-DFF.txt` — curated & validated subscription links | https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/SUB-DFF.txt |
| `ALL-C2.txt` — tunnel-tested proxies only (≥ 2/3 sites) | https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/ALL-C2.txt |

### 🌍 By country — `country/`
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AE.txt) · 8 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AL.txt) · 2 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AT.txt) · 5 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AU.txt) · 4 proxies
- [BE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BE.txt) · 1 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BG.txt) · 2 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BR.txt) · 3 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BY.txt) · 2 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CA.txt) · 26 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CH.txt) · 17 proxies
- [CL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CL.txt) · 1 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CZ.txt) · 3 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/DE.txt) · 93 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ES.txt) · 22 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FI.txt) · 20 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FR.txt) · 38 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GB.txt) · 36 proxies
- [GE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GE.txt) · 1 proxies
- [GR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GR.txt) · 1 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/HK.txt) · 11 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IL.txt) · 2 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IN.txt) · 6 proxies
- [IQ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IQ.txt) · 1 proxies
- [IR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IR.txt) · 5 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IT.txt) · 17 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/JP.txt) · 91 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KR.txt) · 10 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KZ.txt) · 6 proxies
- [LK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LK.txt) · 2 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LV.txt) · 3 proxies
- [NG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NG.txt) · 3 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NL.txt) · 151 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NO.txt) · 1 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/PL.txt) · 12 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RO.txt) · 6 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RU.txt) · 10 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SE.txt) · 14 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SG.txt) · 32 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TH.txt) · 1 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TR.txt) · 12 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TW.txt) · 1 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/UA.txt) · 3 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/US.txt) · 278 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ZA.txt) · 4 proxies

### 🏢 By ISP / Organization — `isp/`
- [5g-network-operations-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/5g-network-operations-pty-ltd.txt) · 1 proxies
- [ace-data-centers-ii](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ace-data-centers-ii.txt) · 3 proxies
- [aeza-group-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/aeza-group-llc.txt) · 2 proxies
- [akamai-technologies](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akamai-technologies.txt) · 1 proxies
- [akenai-products-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akenai-products-ltd.txt) · 2 proxies
- [akile-lax](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akile-lax.txt) · 2 proxies
- [akile-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akile-ltd.txt) · 3 proxies
- [alibaba-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-cloud-llc.txt) · 4 proxies
- [alibaba-com-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-com-llc.txt) · 1 proxies
- [alibaba-us-technology-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-us-technology-co-ltd.txt) · 1 proxies
- [anx](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/anx.txt) · 1 proxies
- [ap-interactive-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ap-interactive-solutions.txt) · 6 proxies
- [bage-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bage-cloud-llc.txt) · 2 proxies
- [baykov-ilya-sergeevich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/baykov-ilya-sergeevich.txt) · 2 proxies
- [binary-networks-solutions-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/binary-networks-solutions-llc.txt) · 1 proxies
- [bl-networks](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bl-networks.txt) · 3 proxies
- [black-host-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/black-host-ltd.txt) · 1 proxies
- [brainstorm-network-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/brainstorm-network-inc.txt) · 3 proxies
- [bytevirt-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bytevirt-llc.txt) · 1 proxies
- [centhost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/centhost.txt) · 1 proxies
- [cgi-global-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cgi-global-limited.txt) · 1 proxies
- [choopa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/choopa.txt) · 1 proxies
- [cloudflare-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare-inc.txt) · 57 proxies
- [cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare.txt) · 57 proxies
- [clouvider-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/clouvider-limited.txt) · 5 proxies
- [cogent-communications](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cogent-communications.txt) · 8 proxies
- [colocenter-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/colocenter-b-v.txt) · 1 proxies
- [contabo-asia-private-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-asia-private-limited.txt) · 13 proxies
- [contabo-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-gmbh.txt) · 4 proxies
- [contabo-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-inc.txt) · 10 proxies
- [cyberzone-s-a](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cyberzone-s-a.txt) · 2 proxies
- [datacamp-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datacamp-limited.txt) · 29 proxies
- [dataforest-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dataforest-gmbh.txt) · 1 proxies
- [datagio-systems-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datagio-systems-ltd.txt) · 2 proxies
- [datawagon-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datawagon-llc.txt) · 1 proxies
- [dedfiberco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dedfiberco.txt) · 2 proxies
- [dedicated-com](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dedicated-com.txt) · 2 proxies
- [digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digital-llc.txt) · 1 proxies
- [digitalocean-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digitalocean-llc.txt) · 12 proxies
- [dotro-telecom-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dotro-telecom-srl.txt) · 2 proxies
- [dpkgsoft-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dpkgsoft-international-limited.txt) · 1 proxies
- [eclipse-j715cigqxknzg646](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/eclipse-j715cigqxknzg646.txt) · 1 proxies
- [eclipse-oprknef735zr5bnl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/eclipse-oprknef735zr5bnl.txt) · 1 proxies
- [egihosting](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/egihosting.txt) · 4 proxies
- [emil-vitukhnovskii-trading-as-great-flow](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/emil-vitukhnovskii-trading-as-great-flow.txt) · 1 proxies
- [enzu-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/enzu-inc.txt) · 1 proxies
- [european-lease1](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/european-lease1.txt) · 10 proxies
- [evolus-it-solutions-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/evolus-it-solutions-gmbh.txt) · 1 proxies
- [fdcservers-net](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fdcservers-net.txt) · 2 proxies
- [fornex-hosting-s-l](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fornex-hosting-s-l.txt) · 1 proxies
- [frantech-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/frantech-solutions.txt) · 2 proxies
- [g-core-labs-s-a](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/g-core-labs-s-a.txt) · 7 proxies
- [gf-dus](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gf-dus.txt) · 1 proxies
- [global-connectivity-solutions-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/global-connectivity-solutions-llp.txt) · 6 proxies
- [globaltelehost-corp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/globaltelehost-corp.txt) · 12 proxies
- [google-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/google-llc.txt) · 2 proxies
- [green-floid-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/green-floid-llc.txt) · 2 proxies
- [greenhost-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/greenhost-bv.txt) · 60 proxies
- [gthost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gthost.txt) · 204 proxies
- [gtt-americas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gtt-americas.txt) · 1 proxies
- [guest-s-r-l-guestfarm-riccione](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/guest-s-r-l-guestfarm-riccione.txt) · 2 proxies
- [h1cloud-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h1cloud-ltd.txt) · 19 proxies
- [h2nexus-cloud-services-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h2nexus-cloud-services-fzco.txt) · 1 proxies
- [hetzner-online-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hetzner-online-gmbh.txt) · 25 proxies
- [hong-kong-lightlayer-technology-co-limit](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hong-kong-lightlayer-technology-co-limit.txt) · 1 proxies
- [host-africa-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/host-africa-pty-ltd.txt) · 1 proxies
- [hosthatch](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hosthatch.txt) · 5 proxies
- [hostinger-us](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostinger-us.txt) · 1 proxies
- [hostkey-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostkey-b-v.txt) · 14 proxies
- [hostmaniac](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostmaniac.txt) · 11 proxies
- [hostox-group-s-r-l](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostox-group-s-r-l.txt) · 4 proxies
- [hostpapa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostpapa.txt) · 3 proxies
- [hz-hosting-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hz-hosting-ltd.txt) · 1 proxies
- [ilia-baikov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ilia-baikov.txt) · 2 proxies
- [innova-communications-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/innova-communications-limited.txt) · 1 proxies
- [interconnects](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interconnects.txt) · 1 proxies
- [interkvm-host-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interkvm-host-srl.txt) · 2 proxies
- [internetport-ab-bl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/internetport-ab-bl.txt) · 1 proxies
- [interserver-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interserver-inc.txt) · 4 proxies
- [ionos-se](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ionos-se.txt) · 2 proxies
- [ip-network](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ip-network.txt) · 1 proxies
- [iron-hosting-centre-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/iron-hosting-centre-ltd.txt) · 1 proxies
- [jsc-selectel](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/jsc-selectel.txt) · 1 proxies
- [jsc-timeweb](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/jsc-timeweb.txt) · 7 proxies
- [kaopu-cloud-hk-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kaopu-cloud-hk-limited.txt) · 1 proxies
- [latitude-sh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/latitude-sh.txt) · 2 proxies
- [layer6](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/layer6.txt) · 1 proxies
- [leaseweb-singapore-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-singapore-pte-ltd.txt) · 2 proxies
- [linode](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/linode.txt) · 1 proxies
- [llc-baxet](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-baxet.txt) · 1 proxies
- [llc-vash-internet-partner](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-vash-internet-partner.txt) · 2 proxies
- [m247-europe-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-europe-srl.txt) · 3 proxies
- [mahdiar-rafiee](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mahdiar-rafiee.txt) · 5 proxies
- [matteo-martelloni-trading-as-deluxhost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/matteo-martelloni-trading-as-deluxhost.txt) · 2 proxies
- [melbikomas-uab](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/melbikomas-uab.txt) · 10 proxies
- [microsoft-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/microsoft-corporation.txt) · 6 proxies
- [multacom-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/multacom-corporation.txt) · 5 proxies
- [myloc-managed-it-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/myloc-managed-it-ag.txt) · 2 proxies
- [nekobyte-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nekobyte-international-limited.txt) · 1 proxies
- [netcrafters-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcrafters-ou.txt) · 2 proxies
- [netcup-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcup-gmbh.txt) · 8 proxies
- [neth-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/neth-llc.txt) · 2 proxies
- [netlab-global](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netlab-global.txt) · 3 proxies
- [netranex-technologies-india-private-limi](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netranex-technologies-india-private-limi.txt) · 2 proxies
- [new-jersey](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/new-jersey.txt) · 1 proxies
- [newserverlife-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/newserverlife-llc.txt) · 3 proxies
- [non-cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/non-cloudflare.txt) · 910 proxies
- [ntt-america-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ntt-america-inc.txt) · 1 proxies
- [nutraver-as](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nutraver-as.txt) · 1 proxies
- [oracle-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oracle-corporation.txt) · 90 proxies
- [ovh-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ovh-sas.txt) · 69 proxies
- [oy-crea-nova-hosting-solution-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oy-crea-nova-hosting-solution-ltd.txt) · 2 proxies
- [pe-fedinyak-sergey-vyacheslavovich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pe-fedinyak-sergey-vyacheslavovich.txt) · 1 proxies
- [pfcloud-ug-haftungsbeschrankt](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pfcloud-ug-haftungsbeschrankt.txt) · 1 proxies
- [pio-hosting-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pio-hosting-gmbh.txt) · 1 proxies
- [pixoof-teknoloji-anonim-sirketi](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pixoof-teknoloji-anonim-sirketi.txt) · 1 proxies
- [play2go-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/play2go-fzco.txt) · 3 proxies
- [powerhouse-management-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/powerhouse-management-inc.txt) · 1 proxies
- [raul-ghita-trading-as-ghita-telekom](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/raul-ghita-trading-as-ghita-telekom.txt) · 4 proxies
- [regxa-company-for-information-technology](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/regxa-company-for-information-technology.txt) · 5 proxies
- [route-95-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/route-95-llc.txt) · 10 proxies
- [sakura-link-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/sakura-link-limited.txt) · 1 proxies
- [scalaxy-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scalaxy-b-v.txt) · 1 proxies
- [scaleway-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway-sas.txt) · 18 proxies
- [scaleway](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway.txt) · 1 proxies
- [senko-digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/senko-digital-llc.txt) · 1 proxies
- [serv-host-group-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serv-host-group-ltd.txt) · 1 proxies
- [serva-one-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serva-one-ltd.txt) · 1 proxies
- [servers-tech-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/servers-tech-fzco.txt) · 4 proxies
- [sh-online-iletisim-anonim-sirketi](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/sh-online-iletisim-anonim-sirketi.txt) · 4 proxies
- [sia-veesp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/sia-veesp.txt) · 2 proxies
- [snowd-security-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/snowd-security-ou.txt) · 1 proxies
- [start2-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/start2-llc.txt) · 1 proxies
- [stealthnet](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/stealthnet.txt) · 1 proxies
- [tabunscic-anatoli](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tabunscic-anatoli.txt) · 2 proxies
- [takehost-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/takehost-ou.txt) · 1 proxies
- [tempest-hosting-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tempest-hosting-llc.txt) · 3 proxies
- [the-constant-company-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/the-constant-company-llc.txt) · 2 proxies
- [the-constant-company](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/the-constant-company.txt) · 9 proxies
- [three-fourteen-sasu](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/three-fourteen-sasu.txt) · 1 proxies
- [timeweb-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/timeweb-llp.txt) · 3 proxies
- [travchis-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/travchis-llc.txt) · 1 proxies
- [uab-cherry-servers](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/uab-cherry-servers.txt) · 2 proxies
- [verixi-sa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/verixi-sa.txt) · 1 proxies
- [viewqwest-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/viewqwest-pte-ltd.txt) · 1 proxies
- [vladislav-doniy](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/vladislav-doniy.txt) · 2 proxies
- [waicore-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/waicore-ltd.txt) · 2 proxies
- [washington-dc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/washington-dc.txt) · 1 proxies
- [weyro-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/weyro-ltd.txt) · 16 proxies
- [xtom-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/xtom-gmbh.txt) · 1 proxies
- [yottasrc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yottasrc.txt) · 1 proxies

### 🚫 Non-Cloudflare, by country — `non-cloudflare/`
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AE.txt) · 8 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AL.txt) · 2 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AT.txt) · 4 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AU.txt) · 3 proxies
- [BE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BE.txt) · 1 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BG.txt) · 2 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BR.txt) · 3 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BY.txt) · 2 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CA.txt) · 25 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CH.txt) · 17 proxies
- [CL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CL.txt) · 1 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CZ.txt) · 2 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/DE.txt) · 86 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/ES.txt) · 22 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FI.txt) · 17 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FR.txt) · 37 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/GB.txt) · 36 proxies
- [GR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/GR.txt) · 1 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/HK.txt) · 7 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IL.txt) · 1 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IN.txt) · 6 proxies
- [IQ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IQ.txt) · 1 proxies
- [IR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IR.txt) · 5 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IT.txt) · 17 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/JP.txt) · 89 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KR.txt) · 9 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KZ.txt) · 6 proxies
- [LK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LK.txt) · 2 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LV.txt) · 3 proxies
- [NG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NG.txt) · 3 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NL.txt) · 151 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NO.txt) · 1 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/PL.txt) · 12 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RO.txt) · 6 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RU.txt) · 10 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SE.txt) · 14 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SG.txt) · 28 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TH.txt) · 1 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TR.txt) · 12 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TW.txt) · 1 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/UA.txt) · 3 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/US.txt) · 249 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/ZA.txt) · 4 proxies
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
