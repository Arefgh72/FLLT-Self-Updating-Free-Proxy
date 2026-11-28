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
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AL.txt) · 5 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AT.txt) · 5 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/AU.txt) · 2 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BG.txt) · 1 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BR.txt) · 2 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/BY.txt) · 1 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CA.txt) · 19 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CH.txt) · 11 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/CZ.txt) · 2 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/DE.txt) · 90 proxies
- [DK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/DK.txt) · 1 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/EE.txt) · 1 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ES.txt) · 13 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FI.txt) · 12 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/FR.txt) · 36 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/GB.txt) · 28 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/HK.txt) · 13 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IE.txt) · 2 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IN.txt) · 1 proxies
- [IQ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IQ.txt) · 1 proxies
- [IR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IR.txt) · 3 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/IT.txt) · 16 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/JP.txt) · 126 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KR.txt) · 9 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/KZ.txt) · 4 proxies
- [LI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LI.txt) · 1 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/LV.txt) · 2 proxies
- [MD](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/MD.txt) · 2 proxies
- [MK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/MK.txt) · 1 proxies
- [MY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/MY.txt) · 1 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NL.txt) · 178 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/NO.txt) · 2 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/PL.txt) · 11 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RO.txt) · 1 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/RU.txt) · 7 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SE.txt) · 11 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/SG.txt) · 22 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TH.txt) · 2 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/TW.txt) · 2 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/US.txt) · 205 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/VN.txt) · 4 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/country/ZA.txt) · 2 proxies

### 🏢 By ISP / Organization — `isp/`
- [2e-telekomunikasyon-ltd-sti](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/2e-telekomunikasyon-ltd-sti.txt) · 1 proxies
- [ace-data-centers-ii-l-l-c](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ace-data-centers-ii-l-l-c.txt) · 1 proxies
- [adaptgroup-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/adaptgroup-llc.txt) · 1 proxies
- [aeza-group-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/aeza-group-llc.txt) · 3 proxies
- [akamai-technologies](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akamai-technologies.txt) · 1 proxies
- [akenai-products-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akenai-products-ltd.txt) · 2 proxies
- [akile-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/akile-ltd.txt) · 4 proxies
- [alexhost-s-r-l](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alexhost-s-r-l.txt) · 1 proxies
- [alibaba-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-cloud-llc.txt) · 13 proxies
- [alibaba-com-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-com-llc.txt) · 6 proxies
- [alibaba-us-technology-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/alibaba-us-technology-co-ltd.txt) · 43 proxies
- [altushost-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/altushost-b-v.txt) · 1 proxies
- [amazon-com-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/amazon-com-inc.txt) · 2 proxies
- [amazon-technologies-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/amazon-technologies-inc.txt) · 1 proxies
- [andris-jakovlevs](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/andris-jakovlevs.txt) · 2 proxies
- [anton-levin](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/anton-levin.txt) · 1 proxies
- [anx](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/anx.txt) · 1 proxies
- [ap-interactive-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ap-interactive-solutions.txt) · 21 proxies
- [as51430-network](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/as51430-network.txt) · 1 proxies
- [ava-host-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ava-host-srl.txt) · 1 proxies
- [bangmod-enterprise-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bangmod-enterprise-co-ltd.txt) · 1 proxies
- [beafort-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/beafort-limited.txt) · 1 proxies
- [beanfield-technologies-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/beanfield-technologies-inc.txt) · 1 proxies
- [black-host-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/black-host-ltd.txt) · 2 proxies
- [bluevps-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/bluevps-ou.txt) · 1 proxies
- [brainstorm-network-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/brainstorm-network-inc.txt) · 3 proxies
- [catixs-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/catixs-ltd.txt) · 1 proxies
- [cgi-global-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cgi-global-limited.txt) · 1 proxies
- [cloudflare-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare-inc.txt) · 21 proxies
- [cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cloudflare.txt) · 21 proxies
- [clouvider-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/clouvider-limited.txt) · 11 proxies
- [cogent-communications](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/cogent-communications.txt) · 11 proxies
- [colocenter-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/colocenter-b-v.txt) · 1 proxies
- [contabo-asia-private-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-asia-private-limited.txt) · 9 proxies
- [contabo-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-gmbh.txt) · 3 proxies
- [contabo-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/contabo-inc.txt) · 9 proxies
- [corenet-cloud-sdn-bhd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/corenet-cloud-sdn-bhd.txt) · 1 proxies
- [ctg-server-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ctg-server-ltd.txt) · 1 proxies
- [datacamp-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/datacamp-limited.txt) · 36 proxies
- [dataforest-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dataforest-gmbh.txt) · 1 proxies
- [dedicated-com](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dedicated-com.txt) · 2 proxies
- [dedik-services-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dedik-services-limited.txt) · 1 proxies
- [digital-hosting-provider-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digital-hosting-provider-llc.txt) · 2 proxies
- [digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digital-llc.txt) · 1 proxies
- [digitalocean-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digitalocean-llc.txt) · 11 proxies
- [digitalvirt](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/digitalvirt.txt) · 1 proxies
- [dpkgsoft-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/dpkgsoft-international-limited.txt) · 3 proxies
- [eclipse-gyn2bxikpfppjhl7](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/eclipse-gyn2bxikpfppjhl7.txt) · 1 proxies
- [egihosting](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/egihosting.txt) · 4 proxies
- [enzu-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/enzu-inc.txt) · 1 proxies
- [european-lease1](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/european-lease1.txt) · 10 proxies
- [expresshost-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/expresshost-ltd.txt) · 4 proxies
- [fasthosts-internet-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fasthosts-internet-ltd.txt) · 1 proxies
- [fastnet-data-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fastnet-data-inc.txt) · 1 proxies
- [fdcservers-net](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/fdcservers-net.txt) · 8 proxies
- [forestsnet-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/forestsnet-ltd.txt) · 1 proxies
- [frantech-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/frantech-solutions.txt) · 2 proxies
- [g-core-labs-s-a](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/g-core-labs-s-a.txt) · 2 proxies
- [global-connectivity-solutions-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/global-connectivity-solutions-llp.txt) · 22 proxies
- [globaltelehost-corp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/globaltelehost-corp.txt) · 5 proxies
- [green-floid-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/green-floid-llc.txt) · 1 proxies
- [greenhost-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/greenhost-bv.txt) · 65 proxies
- [gsl-networks-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gsl-networks-pty-ltd.txt) · 2 proxies
- [gthost](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/gthost.txt) · 105 proxies
- [h1cloud-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h1cloud-ltd.txt) · 8 proxies
- [h2nexus-cloud-services-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/h2nexus-cloud-services-fzco.txt) · 2 proxies
- [hetzner-online-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hetzner-online-gmbh.txt) · 7 proxies
- [host-telecom-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/host-telecom-ltd.txt) · 2 proxies
- [hostes-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostes-ltd.txt) · 7 proxies
- [hostinger-us](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostinger-us.txt) · 1 proxies
- [hostpapa](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/hostpapa.txt) · 1 proxies
- [ilia-baikov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ilia-baikov.txt) · 3 proxies
- [interconnects](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interconnects.txt) · 1 proxies
- [interserver-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/interserver-inc.txt) · 5 proxies
- [ionos-se](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ionos-se.txt) · 4 proxies
- [itldc-latvia-network](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/itldc-latvia-network.txt) · 1 proxies
- [jsc-timeweb](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/jsc-timeweb.txt) · 5 proxies
- [kaopu-cloud-hk-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/kaopu-cloud-hk-limited.txt) · 1 proxies
- [latitude-sh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/latitude-sh.txt) · 2 proxies
- [layer6](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/layer6.txt) · 1 proxies
- [leaseweb-canada-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-canada-inc.txt) · 2 proxies
- [leaseweb-deutschland-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-deutschland-gmbh.txt) · 1 proxies
- [leaseweb-netherlands-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-netherlands-b-v.txt) · 2 proxies
- [leaseweb-singapore-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/leaseweb-singapore-pte-ltd.txt) · 1 proxies
- [lg-dacom-kidc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/lg-dacom-kidc.txt) · 1 proxies
- [linkless-communications-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/linkless-communications-limited.txt) · 1 proxies
- [linode](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/linode.txt) · 1 proxies
- [llc-baxet](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-baxet.txt) · 1 proxies
- [llc-vash-internet-partner](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-vash-internet-partner.txt) · 1 proxies
- [llc-vk](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/llc-vk.txt) · 1 proxies
- [lsw](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/lsw.txt) · 2 proxies
- [lucidacloud-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/lucidacloud-limited.txt) · 1 proxies
- [m247-europe-infra](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-europe-infra.txt) · 1 proxies
- [m247-europe-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-europe-srl.txt) · 4 proxies
- [m247-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/m247-ltd.txt) · 1 proxies
- [mabna](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mabna.txt) · 3 proxies
- [mdsco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mdsco.txt) · 2 proxies
- [melbikomas-uab](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/melbikomas-uab.txt) · 1 proxies
- [microsoft-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/microsoft-corporation.txt) · 2 proxies
- [mivocloud-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/mivocloud-srl.txt) · 1 proxies
- [multacom-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/multacom-corporation.txt) · 1 proxies
- [myloc-managed-it-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/myloc-managed-it-ag.txt) · 2 proxies
- [ncr-voyix-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ncr-voyix-corporation.txt) · 1 proxies
- [nekobyte-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nekobyte-international-limited.txt) · 1 proxies
- [netcrafters-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcrafters-ou.txt) · 2 proxies
- [netcup-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netcup-gmbh.txt) · 8 proxies
- [netlab-global](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/netlab-global.txt) · 2 proxies
- [new-jersey](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/new-jersey.txt) · 1 proxies
- [newserverlife-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/newserverlife-llc.txt) · 1 proxies
- [nls-kazakhstan-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/nls-kazakhstan-llc.txt) · 1 proxies
- [node-host-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/node-host-limited.txt) · 4 proxies
- [non-cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/non-cloudflare.txt) · 837 proxies
- [novoserve-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/novoserve-b-v.txt) · 5 proxies
- [ophl](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ophl.txt) · 1 proxies
- [oracle-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oracle-corporation.txt) · 75 proxies
- [ovh-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/ovh-sas.txt) · 56 proxies
- [oy-crea-nova-hosting-solution-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/oy-crea-nova-hosting-solution-ltd.txt) · 2 proxies
- [paul-sagov](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/paul-sagov.txt) · 23 proxies
- [play2go-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/play2go-fzco.txt) · 11 proxies
- [play2go-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/play2go-international-limited.txt) · 3 proxies
- [private-layer-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/private-layer-inc.txt) · 1 proxies
- [psychz-networks](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/psychz-networks.txt) · 6 proxies
- [regxa-company-for-information-technology](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/regxa-company-for-information-technology.txt) · 1 proxies
- [reliablesite-net-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/reliablesite-net-llc.txt) · 2 proxies
- [route-95-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/route-95-llc.txt) · 9 proxies
- [royalehosting-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/royalehosting-bv.txt) · 1 proxies
- [salimgareyev-vladislav-pavlovich](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/salimgareyev-vladislav-pavlovich.txt) · 3 proxies
- [scalaxy-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scalaxy-b-v.txt) · 1 proxies
- [scaleway-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway-sas.txt) · 18 proxies
- [scaleway](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/scaleway.txt) · 2 proxies
- [serva-one-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/serva-one-ltd.txt) · 1 proxies
- [servers-tech-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/servers-tech-fzco.txt) · 2 proxies
- [shenzhen-tencent-computer-systems-compan](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/shenzhen-tencent-computer-systems-compan.txt) · 1 proxies
- [soulful-hosting-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/soulful-hosting-ltd.txt) · 1 proxies
- [stormycloud-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/stormycloud-inc.txt) · 3 proxies
- [tabunscic-anatoli](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tabunscic-anatoli.txt) · 3 proxies
- [takehost-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/takehost-ou.txt) · 1 proxies
- [tempest-hosting-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tempest-hosting-llc.txt) · 15 proxies
- [tencent-cloud-computing-beijing-co](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tencent-cloud-computing-beijing-co.txt) · 1 proxies
- [three-fourteen-sasu](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/three-fourteen-sasu.txt) · 1 proxies
- [timeweb-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/timeweb-llp.txt) · 1 proxies
- [tino-group-joint-stock-company](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/tino-group-joint-stock-company.txt) · 2 proxies
- [turing-group-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/turing-group-limited.txt) · 1 proxies
- [uab-cherry-servers](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/uab-cherry-servers.txt) · 1 proxies
- [upcloud-usa-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/upcloud-usa-inc.txt) · 1 proxies
- [viewqwest-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/viewqwest-pte-ltd.txt) · 1 proxies
- [vladislav-doniy](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/vladislav-doniy.txt) · 2 proxies
- [voxility-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/voxility-llp.txt) · 1 proxies
- [vuedge-tech-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/vuedge-tech-llc.txt) · 4 proxies
- [wap-ac-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wap-ac-llc.txt) · 1 proxies
- [washington-dc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/washington-dc.txt) · 1 proxies
- [wedeploy-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wedeploy-sas.txt) · 1 proxies
- [weyro-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/weyro-ltd.txt) · 1 proxies
- [wiit-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/wiit-ag.txt) · 1 proxies
- [worktitans-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/worktitans-b-v.txt) · 2 proxies
- [xtom-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/xtom-gmbh.txt) · 2 proxies
- [yuusei-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/yuusei-ltd.txt) · 1 proxies
- [zenlayer-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/zenlayer-inc.txt) · 1 proxies
- [zillion-network-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/isp/zillion-network-inc.txt) · 1 proxies

### 🚫 Non-Cloudflare, by country — `non-cloudflare/`
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AL.txt) · 5 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AT.txt) · 5 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/AU.txt) · 2 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BG.txt) · 1 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BR.txt) · 2 proxies
- [BY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/BY.txt) · 1 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CA.txt) · 19 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CH.txt) · 11 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/CZ.txt) · 2 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/DE.txt) · 89 proxies
- [DK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/DK.txt) · 1 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/EE.txt) · 1 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/ES.txt) · 13 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FI.txt) · 12 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/FR.txt) · 35 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/GB.txt) · 27 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/HK.txt) · 13 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IE.txt) · 2 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IN.txt) · 1 proxies
- [IQ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IQ.txt) · 1 proxies
- [IR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IR.txt) · 3 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/IT.txt) · 15 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/JP.txt) · 124 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KR.txt) · 9 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/KZ.txt) · 4 proxies
- [LI](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LI.txt) · 1 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/LV.txt) · 2 proxies
- [MD](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/MD.txt) · 2 proxies
- [MK](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/MK.txt) · 1 proxies
- [MY](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/MY.txt) · 1 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NL.txt) · 171 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/NO.txt) · 2 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/PL.txt) · 11 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RO.txt) · 1 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/RU.txt) · 7 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SE.txt) · 10 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/SG.txt) · 22 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TH.txt) · 2 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/TW.txt) · 2 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/US.txt) · 198 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/VN.txt) · 4 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-Self-Updating-Free-Proxy/refs/heads/main/non-cloudflare/ZA.txt) · 2 proxies
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
