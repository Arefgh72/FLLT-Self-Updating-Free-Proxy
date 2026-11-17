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
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AL.txt) · 4 proxies
- [AM](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AM.txt) · 1 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AT.txt) · 4 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AU.txt) · 5 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BG.txt) · 3 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BR.txt) · 3 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BY.txt) · 2 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CA.txt) · 30 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CH.txt) · 13 proxies
- [CL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CL.txt) · 1 proxies
- [CY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CY.txt) · 1 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CZ.txt) · 3 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/DE.txt) · 131 proxies
- [DK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/DK.txt) · 1 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/EE.txt) · 1 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ES.txt) · 28 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FI.txt) · 30 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FR.txt) · 36 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GB.txt) · 36 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/HK.txt) · 16 proxies
- [HU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/HU.txt) · 1 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IE.txt) · 1 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IL.txt) · 21 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IN.txt) · 4 proxies
- [IQ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IQ.txt) · 2 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IT.txt) · 17 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/JP.txt) · 79 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KR.txt) · 6 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KZ.txt) · 5 proxies
- [LT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LT.txt) · 3 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LV.txt) · 3 proxies
- [MX](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/MX.txt) · 1 proxies
- [MY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/MY.txt) · 1 proxies
- [NG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NG.txt) · 8 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NL.txt) · 161 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/PL.txt) · 23 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RO.txt) · 3 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RU.txt) · 13 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SE.txt) · 15 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SG.txt) · 39 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TH.txt) · 1 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TR.txt) · 9 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TW.txt) · 1 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/UA.txt) · 2 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/US.txt) · 296 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/VN.txt) · 2 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ZA.txt) · 4 proxies
- [UNKNOWN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/unknown.txt) · 8 proxies

### 🏢 By ISP / Organization — `isp/`
- [1gservers-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/1gservers-llc.txt) · 1 proxies
- [ace-data-centers-ii-l-l-c](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ace-data-centers-ii-l-l-c.txt) · 3 proxies
- [ace-data-centers-ii](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ace-data-centers-ii.txt) · 5 proxies
- [aeza-group-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/aeza-group-llc.txt) · 3 proxies
- [akamai-technologies](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akamai-technologies.txt) · 1 proxies
- [akenai-products-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akenai-products-ltd.txt) · 2 proxies
- [akile-lax](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akile-lax.txt) · 2 proxies
- [akile-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akile-ltd.txt) · 1 proxies
- [alexhost-s-r-l](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alexhost-s-r-l.txt) · 2 proxies
- [alibaba-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-cloud-llc.txt) · 6 proxies
- [alibaba-us-technology-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-us-technology-co-ltd.txt) · 3 proxies
- [amazon-com-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/amazon-com-inc.txt) · 1 proxies
- [amazon-technologies-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/amazon-technologies-inc.txt) · 1 proxies
- [andris-jakovlevs](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/andris-jakovlevs.txt) · 3 proxies
- [anx](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/anx.txt) · 1 proxies
- [ap-interactive-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ap-interactive-solutions.txt) · 12 proxies
- [axarnet-comunicaciones-s-l](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/axarnet-comunicaciones-s-l.txt) · 1 proxies
- [bage-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bage-cloud-llc.txt) · 3 proxies
- [baovecas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/baovecas.txt) · 1 proxies
- [baykov-ilya-sergeevich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/baykov-ilya-sergeevich.txt) · 3 proxies
- [benthost-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/benthost-llc.txt) · 3 proxies
- [binary-networks-solutions-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/binary-networks-solutions-llc.txt) · 1 proxies
- [black-host-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/black-host-ltd.txt) · 1 proxies
- [bluevps-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bluevps-ou.txt) · 1 proxies
- [brainstorm-network-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/brainstorm-network-inc.txt) · 2 proxies
- [brainstorm-network](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/brainstorm-network.txt) · 1 proxies
- [bytevirt-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bytevirt-llc.txt) · 1 proxies
- [centhost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/centhost.txt) · 1 proxies
- [cgi-global-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cgi-global-limited.txt) · 1 proxies
- [choopa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/choopa.txt) · 2 proxies
- [cloud-network](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloud-network.txt) · 3 proxies
- [cloud-solutions-global-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloud-solutions-global-ltd.txt) · 1 proxies
- [cloudflare-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare-inc.txt) · 2 proxies
- [cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare.txt) · 2 proxies
- [cloudlayer8-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudlayer8-limited.txt) · 1 proxies
- [clouvider-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/clouvider-limited.txt) · 8 proxies
- [cogent-communications](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cogent-communications.txt) · 9 proxies
- [colocenter-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/colocenter-b-v.txt) · 1 proxies
- [colocrossing](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/colocrossing.txt) · 1 proxies
- [contabo-asia-private-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-asia-private-limited.txt) · 7 proxies
- [contabo-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-gmbh.txt) · 4 proxies
- [contabo-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-inc.txt) · 15 proxies
- [datacamp-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datacamp-limited.txt) · 30 proxies
- [dataforest-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dataforest-gmbh.txt) · 22 proxies
- [datagio-systems-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datagio-systems-ltd.txt) · 2 proxies
- [dedik-services-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dedik-services-limited.txt) · 1 proxies
- [digital-hosting-provider-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digital-hosting-provider-llc.txt) · 3 proxies
- [digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digital-llc.txt) · 2 proxies
- [digitalocean-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digitalocean-llc.txt) · 25 proxies
- [dmit-cloud-services](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dmit-cloud-services.txt) · 3 proxies
- [edge-core-fze](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/edge-core-fze.txt) · 1 proxies
- [egihosting](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/egihosting.txt) · 3 proxies
- [emil-vitukhnovskii-trading-as-great-flow](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/emil-vitukhnovskii-trading-as-great-flow.txt) · 1 proxies
- [enzu-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/enzu-inc.txt) · 1 proxies
- [estoxy-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/estoxy-ou.txt) · 2 proxies
- [european-lease1](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/european-lease1.txt) · 10 proxies
- [expresshost-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/expresshost-ltd.txt) · 4 proxies
- [fdcservers-net](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fdcservers-net.txt) · 21 proxies
- [fiba-cloud-operation-company-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fiba-cloud-operation-company-llc.txt) · 1 proxies
- [frantech-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/frantech-solutions.txt) · 2 proxies
- [g-core-labs-s-a](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/g-core-labs-s-a.txt) · 1 proxies
- [gf-dus](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gf-dus.txt) · 1 proxies
- [gigagroup-sp-z-o-o](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gigagroup-sp-z-o-o.txt) · 1 proxies
- [global-connectivity-solutions-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/global-connectivity-solutions-llp.txt) · 13 proxies
- [global-internet-solutions-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/global-internet-solutions-llc.txt) · 1 proxies
- [globaltelehost-corp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/globaltelehost-corp.txt) · 11 proxies
- [google-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/google-llc.txt) · 3 proxies
- [green-floid-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/green-floid-llc.txt) · 1 proxies
- [greenhost-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/greenhost-bv.txt) · 65 proxies
- [gsl-networks-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gsl-networks-pty-ltd.txt) · 1 proxies
- [gthost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gthost.txt) · 203 proxies
- [gtt](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gtt.txt) · 1 proxies
- [h1cloud-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h1cloud-ltd.txt) · 39 proxies
- [h2nexus-cloud-services-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h2nexus-cloud-services-fzco.txt) · 5 proxies
- [hetzner-online-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hetzner-online-gmbh.txt) · 13 proxies
- [hong-kong-lightlayer-technology-co-limit](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hong-kong-lightlayer-technology-co-limit.txt) · 1 proxies
- [host-telecom-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/host-telecom-ltd.txt) · 1 proxies
- [hostcrest-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostcrest-limited.txt) · 1 proxies
- [hostes-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostes-ltd.txt) · 6 proxies
- [hosthatch](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hosthatch.txt) · 3 proxies
- [hosting-technology-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hosting-technology-ltd.txt) · 1 proxies
- [hostingbazis-beteti-tarsasag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostingbazis-beteti-tarsasag.txt) · 1 proxies
- [hostinger-us](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostinger-us.txt) · 1 proxies
- [hostkey-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostkey-b-v.txt) · 13 proxies
- [hostmaniac](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostmaniac.txt) · 10 proxies
- [hostpapa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostpapa.txt) · 4 proxies
- [hostup-ab](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostup-ab.txt) · 3 proxies
- [ilia-baikov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ilia-baikov.txt) · 5 proxies
- [imad-nabil-daher-trading-as-id-performan](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/imad-nabil-daher-trading-as-id-performan.txt) · 1 proxies
- [interconnects](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interconnects.txt) · 1 proxies
- [interkvm-host-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interkvm-host-srl.txt) · 1 proxies
- [internetport-ab-bl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/internetport-ab-bl.txt) · 1 proxies
- [interserver-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interserver-inc.txt) · 11 proxies
- [intezio-worldwide-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/intezio-worldwide-limited.txt) · 1 proxies
- [iron-hosting-centre-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/iron-hosting-centre-ltd.txt) · 1 proxies
- [itldc-latvia-network](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/itldc-latvia-network.txt) · 1 proxies
- [jsc-timeweb](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/jsc-timeweb.txt) · 5 proxies
- [kamatera](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kamatera.txt) · 3 proxies
- [kaopu-cloud-hk-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kaopu-cloud-hk-limited.txt) · 1 proxies
- [latitude-sh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/latitude-sh.txt) · 2 proxies
- [layer6](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/layer6.txt) · 1 proxies
- [leaseweb-canada-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-canada-inc.txt) · 2 proxies
- [leaseweb-deutschland-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-deutschland-gmbh.txt) · 1 proxies
- [leaseweb-singapore-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-singapore-pte-ltd.txt) · 3 proxies
- [linode](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/linode.txt) · 1 proxies
- [llc-baxet](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-baxet.txt) · 1 proxies
- [llc-hostoff-csl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-hostoff-csl.txt) · 1 proxies
- [llc-vash-internet-partner](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-vash-internet-partner.txt) · 1 proxies
- [llc-vk](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-vk.txt) · 1 proxies
- [m247-europe-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-europe-srl.txt) · 1 proxies
- [matteo-martelloni-trading-as-deluxhost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/matteo-martelloni-trading-as-deluxhost.txt) · 1 proxies
- [mdsco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mdsco.txt) · 1 proxies
- [melbikomas-uab](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/melbikomas-uab.txt) · 15 proxies
- [mevspace-sp-z-o-o](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mevspace-sp-z-o-o.txt) · 1 proxies
- [microsoft-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/microsoft-corporation.txt) · 3 proxies
- [muhammed-fatih-asan](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/muhammed-fatih-asan.txt) · 1 proxies
- [multacom-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/multacom-corporation.txt) · 1 proxies
- [myloc-managed-it-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/myloc-managed-it-ag.txt) · 3 proxies
- [n963](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/n963.txt) · 1 proxies
- [netcrafters-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcrafters-ou.txt) · 2 proxies
- [netcup-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcup-gmbh.txt) · 7 proxies
- [neth-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/neth-llc.txt) · 2 proxies
- [netlab-global](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netlab-global.txt) · 1 proxies
- [netlen-internet-hizmetleri-ltd-sti](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netlen-internet-hizmetleri-ltd-sti.txt) · 3 proxies
- [netranex-technologies-india-private-limi](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netranex-technologies-india-private-limi.txt) · 1 proxies
- [new-jersey](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/new-jersey.txt) · 1 proxies
- [newserverlife-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/newserverlife-llc.txt) · 2 proxies
- [nls-kazakhstan-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nls-kazakhstan-llc.txt) · 1 proxies
- [node-host-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/node-host-limited.txt) · 2 proxies
- [non-cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/non-cloudflare.txt) · 1084 proxies
- [ntt-america-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ntt-america-inc.txt) · 1 proxies
- [nutraver-as](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nutraver-as.txt) · 1 proxies
- [ophl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ophl.txt) · 1 proxies
- [oracle-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oracle-corporation.txt) · 97 proxies
- [ouiheberg-sarl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ouiheberg-sarl.txt) · 1 proxies
- [ovh-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ovh-sas.txt) · 74 proxies
- [oy-crea-nova-hosting-solution-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oy-crea-nova-hosting-solution-ltd.txt) · 2 proxies
- [packet-star-networks-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/packet-star-networks-limited.txt) · 4 proxies
- [panstar-cloud-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/panstar-cloud-limited.txt) · 1 proxies
- [paul-sagov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/paul-sagov.txt) · 1 proxies
- [pe-fedinyak-sergey-vyacheslavovich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pe-fedinyak-sergey-vyacheslavovich.txt) · 1 proxies
- [peg-tech-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/peg-tech-inc.txt) · 1 proxies
- [petrosky-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/petrosky-cloud-llc.txt) · 1 proxies
- [pio-hosting-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/pio-hosting-gmbh.txt) · 2 proxies
- [play2go-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/play2go-fzco.txt) · 3 proxies
- [play2go-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/play2go-international-limited.txt) · 1 proxies
- [rackcorp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/rackcorp.txt) · 1 proxies
- [railway](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/railway.txt) · 1 proxies
- [regxa-company-for-information-technology](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/regxa-company-for-information-technology.txt) · 4 proxies
- [route-95-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/route-95-llc.txt) · 7 proxies
- [sakura-link-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/sakura-link-limited.txt) · 1 proxies
- [scaleway-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway-sas.txt) · 18 proxies
- [serv-host-group-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serv-host-group-ltd.txt) · 1 proxies
- [serva-one-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serva-one-ltd.txt) · 1 proxies
- [servers-tech-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/servers-tech-fzco.txt) · 4 proxies
- [shabalov-grigoriy-pavlovich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/shabalov-grigoriy-pavlovich.txt) · 2 proxies
- [soulful-hosting-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/soulful-hosting-ltd.txt) · 6 proxies
- [stealthnet](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/stealthnet.txt) · 1 proxies
- [tabunscic-anatoli](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tabunscic-anatoli.txt) · 18 proxies
- [tempest-hosting-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tempest-hosting-llc.txt) · 14 proxies
- [the-constant-company-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/the-constant-company-llc.txt) · 2 proxies
- [the-constant-company](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/the-constant-company.txt) · 3 proxies
- [timeweb-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/timeweb-llp.txt) · 5 proxies
- [travchis-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/travchis-llc.txt) · 1 proxies
- [uab-cherry-servers](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/uab-cherry-servers.txt) · 8 proxies
- [unknown](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/unknown.txt) · 9 proxies
- [verycloud-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/verycloud-sas.txt) · 1 proxies
- [viewqwest-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/viewqwest-pte-ltd.txt) · 1 proxies
- [vladislav-doniy](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/vladislav-doniy.txt) · 4 proxies
- [waicore-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/waicore-ltd.txt) · 1 proxies
- [washington-dc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/washington-dc.txt) · 1 proxies
- [wedeploy-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wedeploy-sas.txt) · 3 proxies
- [weyro-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/weyro-ltd.txt) · 15 proxies
- [xtom-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/xtom-gmbh.txt) · 1 proxies
- [yandex-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yandex-cloud-llc.txt) · 1 proxies
- [yottasrc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yottasrc.txt) · 1 proxies
- [yuusei-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yuusei-ltd.txt) · 1 proxies
- [zhilian-technology-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/zhilian-technology-co-ltd.txt) · 1 proxies
- [zoner](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/zoner.txt) · 1 proxies

### 🚫 Non-Cloudflare, by country — `non-cloudflare/`
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AE.txt) · 8 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AL.txt) · 4 proxies
- [AM](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AM.txt) · 1 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AT.txt) · 4 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AU.txt) · 5 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BG.txt) · 3 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BR.txt) · 3 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BY.txt) · 2 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CA.txt) · 30 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CH.txt) · 13 proxies
- [CL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CL.txt) · 1 proxies
- [CY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CY.txt) · 1 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CZ.txt) · 3 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/DE.txt) · 130 proxies
- [DK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/DK.txt) · 1 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/EE.txt) · 1 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/ES.txt) · 28 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FI.txt) · 30 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FR.txt) · 36 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/GB.txt) · 36 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/HK.txt) · 16 proxies
- [HU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/HU.txt) · 1 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IE.txt) · 1 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IL.txt) · 21 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IN.txt) · 4 proxies
- [IQ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IQ.txt) · 2 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IT.txt) · 17 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/JP.txt) · 78 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KR.txt) · 6 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KZ.txt) · 5 proxies
- [LT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LT.txt) · 3 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LV.txt) · 3 proxies
- [MX](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/MX.txt) · 1 proxies
- [MY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/MY.txt) · 1 proxies
- [NG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NG.txt) · 8 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NL.txt) · 161 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/PL.txt) · 23 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RO.txt) · 3 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RU.txt) · 13 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SE.txt) · 14 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SG.txt) · 39 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TH.txt) · 1 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TR.txt) · 9 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TW.txt) · 1 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/UA.txt) · 2 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/US.txt) · 296 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/VN.txt) · 2 proxies
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
