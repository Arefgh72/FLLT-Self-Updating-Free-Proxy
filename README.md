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
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AE.txt) · 1 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AL.txt) · 6 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AT.txt) · 5 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AU.txt) · 1 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BG.txt) · 2 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BR.txt) · 2 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BY.txt) · 2 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CA.txt) · 20 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CH.txt) · 16 proxies
- [CY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CY.txt) · 4 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CZ.txt) · 5 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/DE.txt) · 106 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/EE.txt) · 1 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ES.txt) · 26 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FI.txt) · 13 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FR.txt) · 28 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GB.txt) · 17 proxies
- [GR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GR.txt) · 1 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/HK.txt) · 13 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IE.txt) · 1 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IL.txt) · 8 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IT.txt) · 15 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/JP.txt) · 53 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KR.txt) · 14 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KZ.txt) · 5 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LV.txt) · 1 proxies
- [MK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/MK.txt) · 1 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NL.txt) · 195 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NO.txt) · 1 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/PL.txt) · 9 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RU.txt) · 10 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SE.txt) · 55 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SG.txt) · 22 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TH.txt) · 2 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TR.txt) · 6 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TW.txt) · 1 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/UA.txt) · 3 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/US.txt) · 233 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/VN.txt) · 1 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ZA.txt) · 4 proxies
- [UNKNOWN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/unknown.txt) · 9 proxies

### 🏢 By ISP / Organization — `isp/`
- [1gservers-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/1gservers-llc.txt) · 1 proxies
- [2e-telekomunikasyon-ltd-sti](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/2e-telekomunikasyon-ltd-sti.txt) · 1 proxies
- [adaptgroup-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/adaptgroup-llc.txt) · 1 proxies
- [aeza-group-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/aeza-group-llc.txt) · 2 proxies
- [akamai-technologies-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akamai-technologies-inc.txt) · 1 proxies
- [akenai-products-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akenai-products-ltd.txt) · 3 proxies
- [alibaba-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-cloud-llc.txt) · 7 proxies
- [alibaba-com-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-com-llc.txt) · 1 proxies
- [alibaba-us-technology-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-us-technology-co-ltd.txt) · 2 proxies
- [amazon-com-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/amazon-com-inc.txt) · 1 proxies
- [andris-jakovlevs](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/andris-jakovlevs.txt) · 1 proxies
- [anx](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/anx.txt) · 1 proxies
- [ap-interactive-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ap-interactive-solutions.txt) · 18 proxies
- [big-hosting-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/big-hosting-ltd.txt) · 1 proxies
- [black-host-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/black-host-ltd.txt) · 2 proxies
- [bluevps-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bluevps-ou.txt) · 1 proxies
- [brainstorm-network-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/brainstorm-network-inc.txt) · 3 proxies
- [centhost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/centhost.txt) · 1 proxies
- [cloud-solutions-global-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloud-solutions-global-ltd.txt) · 1 proxies
- [cloudflare-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare-inc.txt) · 8 proxies
- [cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare.txt) · 8 proxies
- [clouvider-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/clouvider-limited.txt) · 11 proxies
- [cogent-communications](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cogent-communications.txt) · 10 proxies
- [colocation-america-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/colocation-america-corporation.txt) · 1 proxies
- [colocenter-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/colocenter-b-v.txt) · 1 proxies
- [company-64d34574ljq8kk64](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/company-64d34574ljq8kk64.txt) · 3 proxies
- [contabo-asia-private-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-asia-private-limited.txt) · 5 proxies
- [contabo-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-inc.txt) · 13 proxies
- [ctg-server-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ctg-server-ltd.txt) · 1 proxies
- [datacamp-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datacamp-limited.txt) · 41 proxies
- [datacheap-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datacheap-llc.txt) · 1 proxies
- [digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digital-llc.txt) · 1 proxies
- [digitalocean-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digitalocean-llc.txt) · 9 proxies
- [digitalvirt](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digitalvirt.txt) · 1 proxies
- [dpkgsoft-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dpkgsoft-international-limited.txt) · 3 proxies
- [eclipse-4au69i22hw9nohs6](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/eclipse-4au69i22hw9nohs6.txt) · 1 proxies
- [edge-core-fze](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/edge-core-fze.txt) · 4 proxies
- [egihosting](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/egihosting.txt) · 3 proxies
- [emil-vitukhnovskii-trading-as-great-flow](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/emil-vitukhnovskii-trading-as-great-flow.txt) · 3 proxies
- [enzu-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/enzu-inc.txt) · 1 proxies
- [european-lease1](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/european-lease1.txt) · 10 proxies
- [expresshost-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/expresshost-ltd.txt) · 1 proxies
- [fastnet-data-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fastnet-data-inc.txt) · 1 proxies
- [fdcservers-net](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fdcservers-net.txt) · 9 proxies
- [frantech-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/frantech-solutions.txt) · 2 proxies
- [global-connectivity-solutions-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/global-connectivity-solutions-llp.txt) · 21 proxies
- [globaltelehost-corp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/globaltelehost-corp.txt) · 12 proxies
- [google-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/google-llc.txt) · 1 proxies
- [green-floid-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/green-floid-llc.txt) · 3 proxies
- [greenhost-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/greenhost-bv.txt) · 66 proxies
- [gsl-networks-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gsl-networks-pty-ltd.txt) · 2 proxies
- [gthost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gthost.txt) · 160 proxies
- [h1cloud-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h1cloud-ltd.txt) · 22 proxies
- [h2nexus-cloud-services-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h2nexus-cloud-services-fzco.txt) · 5 proxies
- [hetzner-online-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hetzner-online-gmbh.txt) · 10 proxies
- [hong-kong-lightlayer-technology-co-limit](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hong-kong-lightlayer-technology-co-limit.txt) · 1 proxies
- [host-telecom-com-s-r-o](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/host-telecom-com-s-r-o.txt) · 1 proxies
- [host-telecom-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/host-telecom-ltd.txt) · 2 proxies
- [hostes-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostes-ltd.txt) · 10 proxies
- [hostinger-us](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostinger-us.txt) · 1 proxies
- [hostkey-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostkey-b-v.txt) · 1 proxies
- [hostman-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostman-ltd.txt) · 18 proxies
- [hostpapa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostpapa.txt) · 5 proxies
- [ilia-baikov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ilia-baikov.txt) · 4 proxies
- [interconnects](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interconnects.txt) · 1 proxies
- [interserver-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interserver-inc.txt) · 9 proxies
- [ionos-se](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ionos-se.txt) · 2 proxies
- [ivanov-vitaliy-sergeevich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ivanov-vitaliy-sergeevich.txt) · 1 proxies
- [jsc-timeweb](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/jsc-timeweb.txt) · 7 proxies
- [kabat-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kabat-ou.txt) · 3 proxies
- [kaopu-cloud-hk-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kaopu-cloud-hk-limited.txt) · 2 proxies
- [kyonix-networks-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kyonix-networks-limited.txt) · 2 proxies
- [latitude-sh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/latitude-sh.txt) · 2 proxies
- [layer6](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/layer6.txt) · 1 proxies
- [linode](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/linode.txt) · 1 proxies
- [llc-baxet](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-baxet.txt) · 1 proxies
- [llc-hostoff-csl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-hostoff-csl.txt) · 4 proxies
- [llc-vash-internet-partner](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-vash-internet-partner.txt) · 2 proxies
- [m247-europe-infra](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-europe-infra.txt) · 1 proxies
- [m247-europe-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-europe-srl.txt) · 4 proxies
- [mdsco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mdsco.txt) · 1 proxies
- [melbikomas-uab](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/melbikomas-uab.txt) · 5 proxies
- [microsoft-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/microsoft-corporation.txt) · 2 proxies
- [multacom-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/multacom-corporation.txt) · 1 proxies
- [myloc-managed-it-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/myloc-managed-it-ag.txt) · 1 proxies
- [netcrafters-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcrafters-ou.txt) · 1 proxies
- [netcrew](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcrew.txt) · 1 proxies
- [netcup-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcup-gmbh.txt) · 8 proxies
- [neth-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/neth-llc.txt) · 2 proxies
- [netlab-global](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netlab-global.txt) · 2 proxies
- [new-jersey](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/new-jersey.txt) · 1 proxies
- [newserverlife-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/newserverlife-llc.txt) · 1 proxies
- [nls-kazakhstan-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nls-kazakhstan-llc.txt) · 1 proxies
- [non-cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/non-cloudflare.txt) · 910 proxies
- [novoserve-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/novoserve-b-v.txt) · 7 proxies
- [oc-networks-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oc-networks-limited.txt) · 1 proxies
- [oracle-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oracle-corporation.txt) · 56 proxies
- [orion-network-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/orion-network-limited.txt) · 2 proxies
- [ovh-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ovh-sas.txt) · 51 proxies
- [oy-crea-nova-hosting-solution-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oy-crea-nova-hosting-solution-ltd.txt) · 2 proxies
- [panstar-cloud-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/panstar-cloud-limited.txt) · 1 proxies
- [parsun-network-solutions-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/parsun-network-solutions-pty-ltd.txt) · 1 proxies
- [paul-sagov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/paul-sagov.txt) · 5 proxies
- [pe-fedinyak-sergey-vyacheslavovich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pe-fedinyak-sergey-vyacheslavovich.txt) · 1 proxies
- [play2go-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/play2go-international-limited.txt) · 5 proxies
- [private-layer-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/private-layer-inc.txt) · 1 proxies
- [psychz-networks](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/psychz-networks.txt) · 1 proxies
- [realcloud-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/realcloud-ou.txt) · 1 proxies
- [regxa-company-for-information-technology](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/regxa-company-for-information-technology.txt) · 21 proxies
- [route-95-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/route-95-llc.txt) · 6 proxies
- [royalehosting-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/royalehosting-bv.txt) · 1 proxies
- [sakura-link-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/sakura-link-limited.txt) · 1 proxies
- [scalaxy-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scalaxy-b-v.txt) · 2 proxies
- [scaleway-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway-sas.txt) · 18 proxies
- [scaleway](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway.txt) · 1 proxies
- [serv-host-group-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serv-host-group-ltd.txt) · 46 proxies
- [serva-one-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serva-one-ltd.txt) · 1 proxies
- [servers-tech-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/servers-tech-fzco.txt) · 2 proxies
- [shenzhen-tencent-computer-systems-compan](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/shenzhen-tencent-computer-systems-compan.txt) · 8 proxies
- [soulful-hosting-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/soulful-hosting-ltd.txt) · 1 proxies
- [stormycloud-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/stormycloud-inc.txt) · 1 proxies
- [takehost-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/takehost-ou.txt) · 1 proxies
- [teknosos-bilisim-hizmetleri-ve-tic-ltd-s](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/teknosos-bilisim-hizmetleri-ve-tic-ltd-s.txt) · 3 proxies
- [tempest-hosting-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tempest-hosting-llc.txt) · 23 proxies
- [tencent-cloud-computing-beijing-co](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tencent-cloud-computing-beijing-co.txt) · 1 proxies
- [the-constant-company](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/the-constant-company.txt) · 1 proxies
- [timeweb-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/timeweb-llp.txt) · 1 proxies
- [turing-group-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/turing-group-limited.txt) · 2 proxies
- [uab-cherry-servers](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/uab-cherry-servers.txt) · 1 proxies
- [unknown](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/unknown.txt) · 14 proxies
- [upcloud-usa-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/upcloud-usa-inc.txt) · 1 proxies
- [uscloud-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/uscloud-inc.txt) · 1 proxies
- [viewqwest-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/viewqwest-pte-ltd.txt) · 1 proxies
- [vladislav-doniy](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/vladislav-doniy.txt) · 3 proxies
- [wap-ac-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wap-ac-llc.txt) · 1 proxies
- [washington-dc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/washington-dc.txt) · 1 proxies
- [wedeploy-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wedeploy-sas.txt) · 1 proxies
- [weyro-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/weyro-ltd.txt) · 3 proxies
- [wiit-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wiit-ag.txt) · 1 proxies
- [yottasrc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yottasrc.txt) · 4 proxies
- [yuusei-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yuusei-ltd.txt) · 1 proxies
- [zoner](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/zoner.txt) · 1 proxies

### 🚫 Non-Cloudflare, by country — `non-cloudflare/`
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AE.txt) · 1 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AL.txt) · 6 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AT.txt) · 4 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AU.txt) · 1 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BG.txt) · 2 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BR.txt) · 2 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BY.txt) · 2 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CA.txt) · 20 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CH.txt) · 16 proxies
- [CY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CY.txt) · 4 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CZ.txt) · 5 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/DE.txt) · 106 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/EE.txt) · 1 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/ES.txt) · 26 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FI.txt) · 13 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FR.txt) · 28 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/GB.txt) · 17 proxies
- [GR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/GR.txt) · 1 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/HK.txt) · 13 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IE.txt) · 1 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IL.txt) · 3 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IT.txt) · 15 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/JP.txt) · 52 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KR.txt) · 14 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KZ.txt) · 5 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LV.txt) · 1 proxies
- [MK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/MK.txt) · 1 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NL.txt) · 194 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NO.txt) · 1 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/PL.txt) · 9 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RU.txt) · 10 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SE.txt) · 55 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SG.txt) · 22 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TH.txt) · 2 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TR.txt) · 6 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TW.txt) · 1 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/UA.txt) · 3 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/US.txt) · 228 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/VN.txt) · 1 proxies
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
