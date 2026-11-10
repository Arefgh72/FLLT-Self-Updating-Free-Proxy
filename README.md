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
## 📡 Subscription Links

Import these raw URLs into any Xray-compatible client (v2rayN, v2rayNG, Hiddify, Streisand, NekoBox…).

| Subscription | Raw link |
|---|---|
| `SUB-DFF.txt` — curated & validated subscription links | https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/SUB-DFF.txt |
| `ALL-C2.txt` — tunnel-tested proxies only (≥ 2/3 sites) | https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/ALL-C2.txt |

### 🌍 By country — `country/`
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/AE.txt) · 5 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/AL.txt) · 3 proxies
- [AR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/AR.txt) · 1 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/AT.txt) · 5 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/AU.txt) · 4 proxies
- [BE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/BE.txt) · 1 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/BG.txt) · 8 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/BR.txt) · 3 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/CA.txt) · 19 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/CH.txt) · 14 proxies
- [CL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/CL.txt) · 2 proxies
- [CR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/CR.txt) · 1 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/CZ.txt) · 4 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/DE.txt) · 79 proxies
- [DK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/DK.txt) · 1 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/EE.txt) · 3 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/ES.txt) · 18 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/FI.txt) · 16 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/FR.txt) · 31 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/GB.txt) · 58 proxies
- [GR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/GR.txt) · 1 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/HK.txt) · 17 proxies
- [HR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/HR.txt) · 2 proxies
- [HU](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/HU.txt) · 1 proxies
- [ID](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/ID.txt) · 1 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/IE.txt) · 4 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/IL.txt) · 2 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/IN.txt) · 3 proxies
- [IR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/IR.txt) · 5 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/IT.txt) · 20 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/JP.txt) · 77 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/KR.txt) · 11 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/KZ.txt) · 3 proxies
- [LK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/LK.txt) · 2 proxies
- [LT](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/LT.txt) · 2 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/LV.txt) · 3 proxies
- [MX](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/MX.txt) · 3 proxies
- [MY](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/MY.txt) · 3 proxies
- [NG](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/NG.txt) · 1 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/NL.txt) · 131 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/NO.txt) · 1 proxies
- [NZ](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/NZ.txt) · 1 proxies
- [PE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/PE.txt) · 1 proxies
- [PK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/PK.txt) · 1 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/PL.txt) · 11 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/RO.txt) · 4 proxies
- [RS](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/RS.txt) · 4 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/RU.txt) · 3 proxies
- [SA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/SA.txt) · 1 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/SE.txt) · 15 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/SG.txt) · 35 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/TH.txt) · 4 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/TR.txt) · 6 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/TW.txt) · 4 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/UA.txt) · 1 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/US.txt) · 219 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/VN.txt) · 3 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/country/ZA.txt) · 4 proxies

### 🏢 By ISP / Organization — `isp/`
- [5g-network-operations-pty-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/5g-network-operations-pty-ltd.txt) · 1 proxies
- [ace-data-centers-ii-l-l-c](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ace-data-centers-ii-l-l-c.txt) · 1 proxies
- [adaptgroup-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/adaptgroup-llc.txt) · 1 proxies
- [aeza-group-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/aeza-group-llc.txt) · 1 proxies
- [airrabbit-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/airrabbit-llc.txt) · 4 proxies
- [akile-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/akile-ltd.txt) · 4 proxies
- [alexhost-s-r-l](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/alexhost-s-r-l.txt) · 1 proxies
- [alibaba-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/alibaba-cloud-llc.txt) · 1 proxies
- [alibaba-us-technology-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/alibaba-us-technology-co-ltd.txt) · 5 proxies
- [alice-networks-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/alice-networks-ltd.txt) · 4 proxies
- [amazon-com-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/amazon-com-inc.txt) · 3 proxies
- [amazon-technologies-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/amazon-technologies-inc.txt) · 5 proxies
- [anx](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/anx.txt) · 1 proxies
- [ap-interactive-solutions](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ap-interactive-solutions.txt) · 3 proxies
- [bage-cloud-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/bage-cloud-llc.txt) · 5 proxies
- [baovecas](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/baovecas.txt) · 2 proxies
- [baykov-ilya-sergeevich](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/baykov-ilya-sergeevich.txt) · 3 proxies
- [black-host-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/black-host-ltd.txt) · 1 proxies
- [brainshare-technologies-and-services-nig](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/brainshare-technologies-and-services-nig.txt) · 1 proxies
- [brainstorm-network-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/brainstorm-network-inc.txt) · 8 proxies
- [brainstorm-network](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/brainstorm-network.txt) · 1 proxies
- [centhost](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/centhost.txt) · 1 proxies
- [cgi-global-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cgi-global-limited.txt) · 1 proxies
- [china-mobile-hong-kong-company-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/china-mobile-hong-kong-company-limited.txt) · 1 proxies
- [choopa](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/choopa.txt) · 1 proxies
- [chunghwa-telecom-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/chunghwa-telecom-co-ltd.txt) · 2 proxies
- [cloudflare-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cloudflare-inc.txt) · 30 proxies
- [cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cloudflare.txt) · 30 proxies
- [clouvider-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/clouvider-limited.txt) · 2 proxies
- [cnservers-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cnservers-llc.txt) · 1 proxies
- [cogent-communications](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cogent-communications.txt) · 8 proxies
- [colocenter-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/colocenter-b-v.txt) · 1 proxies
- [contabo-asia-private-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/contabo-asia-private-limited.txt) · 8 proxies
- [contabo-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/contabo-gmbh.txt) · 3 proxies
- [contabo-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/contabo-inc.txt) · 8 proxies
- [cox-communications-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cox-communications-inc.txt) · 1 proxies
- [cyberzone-s-a](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/cyberzone-s-a.txt) · 2 proxies
- [da-international-group-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/da-international-group-ltd.txt) · 1 proxies
- [data-miners-s-a-racknation-cr](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/data-miners-s-a-racknation-cr.txt) · 1 proxies
- [datacamp-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/datacamp-limited.txt) · 35 proxies
- [dataforest-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/dataforest-gmbh.txt) · 5 proxies
- [datagio-systems-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/datagio-systems-ltd.txt) · 2 proxies
- [delta-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/delta-ltd.txt) · 1 proxies
- [digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/digital-llc.txt) · 1 proxies
- [digitalera-tech-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/digitalera-tech-ou.txt) · 1 proxies
- [digitalocean-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/digitalocean-llc.txt) · 7 proxies
- [dotro-telecom-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/dotro-telecom-srl.txt) · 1 proxies
- [ecl-mgzd1k598nbjb6a9](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ecl-mgzd1k598nbjb6a9.txt) · 1 proxies
- [ecl-o27ssnp8olk0am2f](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ecl-o27ssnp8olk0am2f.txt) · 1 proxies
- [edis-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/edis-gmbh.txt) · 1 proxies
- [egihosting](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/egihosting.txt) · 3 proxies
- [emil-vitukhnovskii-trading-as-great-flow](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/emil-vitukhnovskii-trading-as-great-flow.txt) · 1 proxies
- [enzu-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/enzu-inc.txt) · 1 proxies
- [eons-data-communications-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/eons-data-communications-limited.txt) · 3 proxies
- [eugamehost-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/eugamehost-ltd.txt) · 1 proxies
- [european-lease1](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/european-lease1.txt) · 10 proxies
- [evoxt-enterprise](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/evoxt-enterprise.txt) · 1 proxies
- [fdcservers-net](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/fdcservers-net.txt) · 3 proxies
- [fibacloud](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/fibacloud.txt) · 1 proxies
- [flame-networks-private-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/flame-networks-private-limited.txt) · 1 proxies
- [flokinet-ehf](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/flokinet-ehf.txt) · 1 proxies
- [fornex-hosting-s-l](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/fornex-hosting-s-l.txt) · 1 proxies
- [frontier-communications-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/frontier-communications-corporation.txt) · 1 proxies
- [g-core-labs-s-a](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/g-core-labs-s-a.txt) · 1 proxies
- [gf-dus](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/gf-dus.txt) · 1 proxies
- [global-connectivity-solutions-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/global-connectivity-solutions-llp.txt) · 6 proxies
- [globaltelehost-corp](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/globaltelehost-corp.txt) · 10 proxies
- [google-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/google-llc.txt) · 1 proxies
- [green-floid-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/green-floid-llc.txt) · 1 proxies
- [greenhost-bv](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/greenhost-bv.txt) · 54 proxies
- [gthost](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/gthost.txt) · 184 proxies
- [h1cloud-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/h1cloud-ltd.txt) · 4 proxies
- [h2nexus-cloud-services-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/h2nexus-cloud-services-fzco.txt) · 2 proxies
- [hetzner-online-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hetzner-online-gmbh.txt) · 17 proxies
- [hgc-global-communications-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hgc-global-communications-limited.txt) · 1 proxies
- [hivelocity-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hivelocity-inc.txt) · 1 proxies
- [hong-kong-cable-television-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hong-kong-cable-television-limited.txt) · 1 proxies
- [hostes-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hostes-llc.txt) · 1 proxies
- [hostes-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hostes-ltd.txt) · 1 proxies
- [hosthatch](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hosthatch.txt) · 2 proxies
- [hostkey-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hostkey-b-v.txt) · 8 proxies
- [hostmaniac](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hostmaniac.txt) · 8 proxies
- [hostpapa](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/hostpapa.txt) · 3 proxies
- [ilia-baikov](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ilia-baikov.txt) · 2 proxies
- [interkvm-host-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/interkvm-host-srl.txt) · 1 proxies
- [internetport-ab-bl](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/internetport-ab-bl.txt) · 1 proxies
- [ionos-se](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ionos-se.txt) · 1 proxies
- [iron-hosting-centre-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/iron-hosting-centre-ltd.txt) · 1 proxies
- [isif-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/isif-ou.txt) · 1 proxies
- [it7-networks-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/it7-networks-inc.txt) · 1 proxies
- [jurgita-jurgaitienei-trading-as-locotorp](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/jurgita-jurgaitienei-trading-as-locotorp.txt) · 1 proxies
- [kaopu-cloud-hk-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/kaopu-cloud-hk-limited.txt) · 5 proxies
- [karolio-it-paslaugos-uab](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/karolio-it-paslaugos-uab.txt) · 2 proxies
- [korea-telecom](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/korea-telecom.txt) · 1 proxies
- [latitude-sh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/latitude-sh.txt) · 2 proxies
- [layer6](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/layer6.txt) · 1 proxies
- [layer7-technologies-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/layer7-technologies-inc.txt) · 2 proxies
- [leaseweb-deutschland-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/leaseweb-deutschland-gmbh.txt) · 1 proxies
- [lg-dacom-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/lg-dacom-corporation.txt) · 1 proxies
- [light-node-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/light-node-limited.txt) · 5 proxies
- [linode](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/linode.txt) · 1 proxies
- [llp-kompaniya-hoster-kz](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/llp-kompaniya-hoster-kz.txt) · 1 proxies
- [m247-europe-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/m247-europe-srl.txt) · 3 proxies
- [mahdiar-rafiee](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/mahdiar-rafiee.txt) · 5 proxies
- [maxko-d-o-o](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/maxko-d-o-o.txt) · 9 proxies
- [melbikomas-uab](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/melbikomas-uab.txt) · 5 proxies
- [metrabyte-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/metrabyte-co-ltd.txt) · 1 proxies
- [microsoft-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/microsoft-corporation.txt) · 4 proxies
- [microsoft](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/microsoft.txt) · 1 proxies
- [mivocloud-srl](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/mivocloud-srl.txt) · 1 proxies
- [moack-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/moack-co-ltd.txt) · 1 proxies
- [moldtelecom-sa](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/moldtelecom-sa.txt) · 4 proxies
- [multacom-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/multacom-corporation.txt) · 1 proxies
- [myloc-managed-it-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/myloc-managed-it-ag.txt) · 2 proxies
- [need-l-l-c-fz](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/need-l-l-c-fz.txt) · 1 proxies
- [nekobyte-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/nekobyte-international-limited.txt) · 1 proxies
- [netcrafters-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/netcrafters-ou.txt) · 3 proxies
- [netcup-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/netcup-gmbh.txt) · 5 proxies
- [neth-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/neth-llc.txt) · 1 proxies
- [netlab-global](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/netlab-global.txt) · 1 proxies
- [new-jersey](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/new-jersey.txt) · 1 proxies
- [newserverlife-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/newserverlife-llc.txt) · 1 proxies
- [non-cloudflare](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/non-cloudflare.txt) · 856 proxies
- [novoserve-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/novoserve-b-v.txt) · 13 proxies
- [oneprovider](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/oneprovider.txt) · 6 proxies
- [oracle-corporation](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/oracle-corporation.txt) · 69 proxies
- [ovh-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ovh-sas.txt) · 42 proxies
- [oy-crea-nova-hosting-solution-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/oy-crea-nova-hosting-solution-ltd.txt) · 2 proxies
- [paul-sagov](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/paul-sagov.txt) · 2 proxies
- [peg-tech-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/peg-tech-inc.txt) · 1 proxies
- [pio-hosting-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/pio-hosting-gmbh.txt) · 2 proxies
- [play2go-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/play2go-fzco.txt) · 4 proxies
- [play2go-international-limited](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/play2go-international-limited.txt) · 3 proxies
- [racktech-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/racktech-co-ltd.txt) · 1 proxies
- [regxa-company-for-information-technology](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/regxa-company-for-information-technology.txt) · 3 proxies
- [reliablesite-net-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/reliablesite-net-llc.txt) · 2 proxies
- [rica-web-services](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/rica-web-services.txt) · 1 proxies
- [ripe](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/ripe.txt) · 2 proxies
- [rj-network-ou](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/rj-network-ou.txt) · 2 proxies
- [route-95-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/route-95-llc.txt) · 12 proxies
- [scalaxy-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/scalaxy-b-v.txt) · 1 proxies
- [scaleway-sas](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/scaleway-sas.txt) · 17 proxies
- [scaleway](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/scaleway.txt) · 1 proxies
- [senko-digital-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/senko-digital-llc.txt) · 2 proxies
- [serv-host-group-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/serv-host-group-ltd.txt) · 6 proxies
- [serva-one-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/serva-one-ltd.txt) · 2 proxies
- [servers-tech-fzco](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/servers-tech-fzco.txt) · 2 proxies
- [sia-veesp](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/sia-veesp.txt) · 3 proxies
- [sk-broadband-co-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/sk-broadband-co-ltd.txt) · 1 proxies
- [softbank-corp](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/softbank-corp.txt) · 1 proxies
- [sony-network-communications-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/sony-network-communications-inc.txt) · 2 proxies
- [southeast-asia-telecom-sg-pte-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/southeast-asia-telecom-sg-pte-ltd.txt) · 2 proxies
- [space-exploration-technologies-corporati](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/space-exploration-technologies-corporati.txt) · 1 proxies
- [the-constant-company-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/the-constant-company-llc.txt) · 4 proxies
- [the-constant-company](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/the-constant-company.txt) · 13 proxies
- [three-fourteen-sasu](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/three-fourteen-sasu.txt) · 1 proxies
- [timeweb-llp](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/timeweb-llp.txt) · 1 proxies
- [tm-technology-services-sdn-bhd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/tm-technology-services-sdn-bhd.txt) · 1 proxies
- [travchis-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/travchis-llc.txt) · 2 proxies
- [uab-cherry-servers](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/uab-cherry-servers.txt) · 2 proxies
- [unredacted-inc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/unredacted-inc.txt) · 1 proxies
- [vladislav-doniy](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/vladislav-doniy.txt) · 1 proxies
- [vpspay-networks-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/vpspay-networks-ltd.txt) · 3 proxies
- [vtdc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/vtdc.txt) · 1 proxies
- [waicore-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/waicore-ltd.txt) · 1 proxies
- [washington-dc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/washington-dc.txt) · 1 proxies
- [weyro-ltd](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/weyro-ltd.txt) · 37 proxies
- [wiit-ag](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/wiit-ag.txt) · 1 proxies
- [worldstream-b-v](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/worldstream-b-v.txt) · 1 proxies
- [wowrack-com](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/wowrack-com.txt) · 1 proxies
- [xtom-gmbh](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/xtom-gmbh.txt) · 1 proxies
- [yottasrc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/yottasrc.txt) · 2 proxies
- [zappie-host-llc](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/zappie-host-llc.txt) · 1 proxies
- [zappie-host](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/isp/zappie-host.txt) · 1 proxies

### 🚫 Non-Cloudflare, by country — `non-cloudflare/`
- [AE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/AE.txt) · 5 proxies
- [AL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/AL.txt) · 3 proxies
- [AR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/AR.txt) · 1 proxies
- [AT](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/AT.txt) · 4 proxies
- [AU](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/AU.txt) · 3 proxies
- [BE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/BE.txt) · 1 proxies
- [BG](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/BG.txt) · 8 proxies
- [BR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/BR.txt) · 3 proxies
- [CA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/CA.txt) · 19 proxies
- [CH](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/CH.txt) · 14 proxies
- [CL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/CL.txt) · 2 proxies
- [CR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/CR.txt) · 1 proxies
- [CZ](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/CZ.txt) · 4 proxies
- [DE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/DE.txt) · 74 proxies
- [DK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/DK.txt) · 1 proxies
- [EE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/EE.txt) · 3 proxies
- [ES](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/ES.txt) · 18 proxies
- [FI](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/FI.txt) · 13 proxies
- [FR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/FR.txt) · 31 proxies
- [GB](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/GB.txt) · 58 proxies
- [HK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/HK.txt) · 15 proxies
- [HR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/HR.txt) · 2 proxies
- [ID](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/ID.txt) · 1 proxies
- [IE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/IE.txt) · 4 proxies
- [IL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/IL.txt) · 1 proxies
- [IN](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/IN.txt) · 3 proxies
- [IR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/IR.txt) · 5 proxies
- [IT](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/IT.txt) · 20 proxies
- [JP](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/JP.txt) · 75 proxies
- [KR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/KR.txt) · 11 proxies
- [KZ](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/KZ.txt) · 3 proxies
- [LK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/LK.txt) · 2 proxies
- [LT](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/LT.txt) · 2 proxies
- [LV](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/LV.txt) · 3 proxies
- [MX](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/MX.txt) · 3 proxies
- [MY](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/MY.txt) · 3 proxies
- [NG](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/NG.txt) · 1 proxies
- [NL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/NL.txt) · 131 proxies
- [NO](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/NO.txt) · 1 proxies
- [NZ](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/NZ.txt) · 1 proxies
- [PE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/PE.txt) · 1 proxies
- [PK](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/PK.txt) · 1 proxies
- [PL](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/PL.txt) · 10 proxies
- [RO](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/RO.txt) · 4 proxies
- [RS](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/RS.txt) · 4 proxies
- [RU](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/RU.txt) · 3 proxies
- [SA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/SA.txt) · 1 proxies
- [SE](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/SE.txt) · 14 proxies
- [SG](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/SG.txt) · 30 proxies
- [TH](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/TH.txt) · 4 proxies
- [TR](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/TR.txt) · 6 proxies
- [TW](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/TW.txt) · 4 proxies
- [UA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/UA.txt) · 1 proxies
- [US](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/US.txt) · 213 proxies
- [VN](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/VN.txt) · 3 proxies
- [ZA](https://raw.githubusercontent.com/Arefgh72/FLLT-test/refs/heads/main/non-cloudflare/ZA.txt) · 4 proxies
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
