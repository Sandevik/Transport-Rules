# EU Regulation Matrix — Cross-Reference by Country Tier

This file maps which framework baseline applies to each country and lists known national deviations.
**How to use:** Identify the country's tier → read the baseline file first → then read the country file for deviations.

---

## Tier 1 — EU Member States + EEA (baseline: `references/eu/`)

EU Regulations are directly binding. EEA members (NO, IS, LI) implement via EEA Agreement.

**EU Member States:** AT BE BG CY CZ DE DK EE ES FI FR GR HR HU IE IT LT LU LV MT NL PL PT RO SE SI SK
**EEA (non-EU):** NO IS LI

| Regulation | Baseline file | Known national deviations |
|-----------|--------------|--------------------------|
| EU 561/2006 — Driving/rest | `eu/driving-rest-time.md` | SE: agriculture exemption within 100km; FI: additional national exemptions; all others: no significant deviation |
| Directive 2002/15/EC — Working time | `eu/working-time.md` | SE: SFS 2005:395 (self-employed exempt from averages since 2019) |
| EU 165/2014 + Smart tachograph v2 | `eu/smart-tachograph.md` | Retrofit deadlines apply EU-wide uniformly; national enforcement approach varies |
| EU 1071/2009 — Operator licence | `eu/commercial-licensing.md` | No significant deviations; national licensing authorities vary |
| EU 1072/2009 — Cabotage (3-in-7 rule) | `eu/commercial-licensing.md` | No deviations; enforcement intensity varies |
| Directive 96/53/EC — Weights/dimensions | `eu/weights-dimensions.md` | **SE/FI: Nordic exception Art. 4a** → SE: 74t, 34.5m; FI: 76t, 34.5m; **NL: LZV** 25.25m, 60t (national permission); all others: EU limits |
| ADR 2025 — Dangerous goods | `eu/dangerous-goods.md` | Via Directive 2008/68/EC; national enforcement authority varies; SE: MSB |
| Directive 2003/59/EC — Driver CPC | `eu/professional-driver.md` | No deviations; national issuing authority varies |
| Directive 2014/45/EU — Roadworthiness | `eu/vehicle-inspection.md` | Test station setup varies; SE: Bilprovningen + private stations |
| Directive 2020/1057/EU — Posting | `eu/posting-workers.md` | **Portal per country:** BE=LIMOSA, FR=SIPSI, DE=FMS, PL=biznes.gov.pl, NL=DUOS, AT=EFZR; others=IMI (EU-wide) |
| Directive 2022/362/EU — Tolls | `eu/road-charging.md` | Framework only; toll systems are purely national: DE=BALM/Toll Collect, AT=ASFINAG, BE=Viapass, PL=e-TOLL, CZ=MYTO, SK=e-MYTO, HU=HU-GO, BG=BGTOLL, HR=HAC, SI=DarsGo, LT=ViaLietuva, LV=CSDD vignette, LU=e-vignette; DK/FI/NL/IE have no general motorway tolls |
| Regulation EC 1/2005 — Live animals | `eu/live-animals.md` | SE: Jordbruksverket (SJV) authorisation required |
| Regulation 2024/1610 — CO2 | `eu/emissions.md` | Manufacturer-facing; SE: bonus-malus scheme, Miljözoner; DE: Umweltzonen |
| Directive 92/106/EEC — Combined transport | `eu/combined-transport.md` | 44t weight allowance applies in all member states |

---

## Tier 2 — AETR-only (baseline: `references/aetr/` for driving/rest ONLY; all other topics standalone)

**Countries:** CH TR RU UA MA AZ KZ UZ TM and other non-EU/EEA AETR contracting parties

| Topic | Baseline | Notes |
|-------|---------|-------|
| Driving/rest time | `aetr/driving-rest-time.md` | Rules align with EU 561/2006; legal basis is AETR treaty not EU regulation |
| Tachograph | `aetr/tachograph.md` | AETR Annex 1B; no Smart v2 obligation; EU-issued driver cards valid |
| Tolls | **Standalone** | CH: LSVA (distance-based); TR: HGS/KGS motorway tolls; others: national |
| Licensing | **Standalone** | CH: Swiss transport permit; TR: Turkish operator licence |
| Dimensions/weights | **Standalone** | CH: own limits; TR: own limits |
| Penalties | **Standalone** | Local currency; national law only |
| **Advance payment at roadside** | AETR Art. 22ter | **PROHIBITED** — no cash payment at roadside for AETR violations (unlike EU) |

---

## Tier 3 — Standalone (no supranational baseline)

All rules are independent national law. Never cite EU or AETR as baseline.

| Country | Framework | Primary rules | Key authority |
|---------|-----------|--------------|---------------|
| **GB** | UK domestic (retained EU 561/2006 via EU Withdrawal Act) | GB SI 2005/639; own operator's licence via Traffic Commissioners | DVSA |
| **US** | FMCSA / 49 CFR | HOS: 11h driving / 14h window; ELD mandate; CDL | FMCSA (DOT) |
| **CA** | Transport Canada + provincial | SOR/2005-313 HOS; National Safety Code | Transport Canada |
| **AU** | NHVR + state | Chain of Responsibility; NHVR fatigue management rules | NHVR |

**GB note:** GB retained EU law as of Brexit date (31 Dec 2020). Rules largely mirror EU 561/2006 but GB is no longer bound by EU regulation updates (e.g., Mobility Package cab prohibition may not apply domestically). State GB divergences explicitly.

---

## AETR Signatory Status

For the full list of 56 AETR contracting parties: https://unece.org/transport/road-transport/aetr-agreement-and-status

Key non-EU AETR parties most relevant to international road transport:
CH (Switzerland), TR (Turkey), NO (Norway — also EEA), IS (Iceland — also EEA), LI (Liechtenstein — also EEA),
RU (Russia), UA (Ukraine), BY (Belarus), MD (Moldova), GE (Georgia), AM (Armenia), AZ (Azerbaijan),
KZ (Kazakhstan), UZ (Uzbekistan), TJ (Tajikistan), TM (Turkmenistan), MA (Morocco), TN (Tunisia),
BA (Bosnia-Herzegovina), RS (Serbia), ME (Montenegro), MK (North Macedonia), AL (Albania), SM (San Marino), MC (Monaco)

---

*See also: references/topics/country-index.md (which reference files exist per country), references/topics/url-index.md (master URL list)*
