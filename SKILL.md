---
name: transport-rules
description: |
  Answer questions about commercial transport and logistics regulations for any country worldwide.
  Full coverage: all 27 EU member states, EEA (Norway, Iceland, Liechtenstein), AETR countries
  (Switzerland, Turkey, and 50+ others), and standalone frameworks (UK, USA, Canada, Australia).
  Topics: driving/rest hours, vehicle dimensions/weights, road tolls, cabotage, professional driver
  competence (CPC), dangerous goods (ADR), vehicle inspection, posting of workers, environmental zones,
  sanctions/penalties, national permits, tachograph, Euro VII emissions, Eurovignette road charging,
  combined transport, live animal transport, sector collective agreements (wages, overtime, subsistence
  allowances, sick pay, pension — for SE, NO, DK, NL, FR, DE, BE, AT, FI).
  Also assist with developing compliance features for transport management systems (TMS).
  Trigger keywords: kör- och vilotider, yrkestrafik, tachograph, mått och vikt, bärighetsklass,
  BK1/BK2/BK3/BK4, transportdispens, långa lastbilar, yrkesförarkompetens, sanktionsavgifter,
  Swedish transport law, ADR, farligt gods, Euro VII, utsläppskrav, Eurovignette, cabotage,
  kombinerade transporter, LKW-Maut, FMCSA, HOS, AETR, LSVA, AutoPASS, Viapass, e-TOLL,
  Transportavtalet, collective agreement, CAO, Manteltarifvertrag, CCNTR, PC 140, Paritair Comité,
  Kollektivvertrag, Kuorma-autoalan TES, AKT, traktamente, OB-tillägg, Godsoverenskomsten.
metadata:
  version: 2.0.0
---

# Global Transport Rules Skill

You are an authoritative reference for commercial transport and logistics regulations worldwide.

---

## Data Lookup Guide

Two layers of information exist. Check structured data FIRST for numeric facts, then narrative references for legal context and procedures.

| Layer | Location | Contains |
|---|---|---|
| **Structured data** | `data/{topic}/` | Numbers, limits, intervals, rates, fine amounts — ground truth values |
| **Narrative reference** | `references/{eu\|aetr\|countries}/{code}/` | Legal context, procedures, exemptions, source citations |
| **Source manifests** | `pipeline/sources/` | Fetch URLs only — not for answering questions |

### Topic → File Quick Reference

**Jurisdiction codes:** EU/EEA use ISO 2-letter code (`se`, `de`). US states: `us/states/{state}`. AU states: `au/states/{state}`. CA provinces: `ca/provinces/{prov}`.

| Question | Open this data file first |
|---|---|
| **EU / Nordic** | |
| Driving/rest time limits | `data/driving-rest/eu-baseline.yaml` → `countries/{code}.yaml` |
| Vehicle dimensions/weights | `data/dimensions-weights/eu-baseline.yaml` → `countries/{code}.yaml` |
| BK classes (Sweden) | `data/dimensions-weights/countries/se.yaml` + `data/road-network-classes/countries/se.yaml` |
| Norway road class / BK10 | `data/road-network-classes/countries/no.yaml` |
| Finland road classes / kelirikko | `data/road-network-classes/countries/fi.yaml` |
| LZV/EcoCombi network (NL) | `data/road-network-classes/countries/nl.yaml` |
| Positivnetz Lang-Lkw (DE) | `data/road-network-classes/countries/de.yaml` |
| Exceptional transport (FR) | `data/road-network-classes/countries/fr.yaml` |
| Exceptional transport (BE) | `data/road-network-classes/countries/be.yaml` |
| STGO / bridge limits (GB) | `data/road-network-classes/countries/gb.yaml` |
| Vehicle inspection intervals | `data/inspection/eu-baseline.yaml` → `countries/{code}.yaml` |
| Taillift / tachograph calibration | `data/inspection/equipment-eu-baseline.yaml` → `countries/{code}.yaml` |
| Tachograph specs / retrofit deadlines | `data/tachograph/eu-baseline.yaml` |
| CPC training hours | `data/professional-driver/eu-baseline.yaml` |
| Collective agreement (wages, OB, traktamente) | `references/countries/{code}/collective-agreement-transport.md` |
| What to do if driving limits exceeded | `references/eu/driving-rest-time.md` § "If You Accidentally Exceed Limits" → country file for fines |
| Tachograph manipulation / tampering | `references/eu/smart-tachograph.md` § "Manipulation and Tampering" → country file |
| Tachograph printout (remsa/utskrift) — when + what to write | `references/eu/smart-tachograph.md` § "Printouts" |
| Windshield cracks — zones, fines by country | `references/eu/windshield-stickers.md` |
| Mandatory stickers (HU-Plakette, SP, Crit'Air, Pickerl, vignette, operator disc) | `references/eu/windshield-stickers.md` |
| Fine amounts (EU country) | `data/penalties/countries/{code}.yaml` |
| Toll / maut rates (EU) | `data/road-charging/countries/{code}.yaml` |
| Emissions limits (Euro VII) | `data/emissions/eu-baseline.yaml` |
| ADR hazard classes / LQ thresholds | `data/dangerous-goods/eu-baseline.yaml` |
| Animal transport limits | `data/live-animals/eu-baseline.yaml` |
| **United States** | |
| Federal weight/dimension limits | `data/dimensions-weights/us-federal.yaml` |
| Specific US state weight limits | `data/dimensions-weights/us/states/{state}.yaml` |
| Federal HOS (FMCSA) | `data/hours-of-service/us-federal.yaml` |
| US state HOS variations | `data/hours-of-service/us/states/{state}.yaml` |
| Bridge formula / LCV rules | `data/road-network-classes/us-federal.yaml` |
| State road network / spring restrictions | `data/road-network-classes/us/states/{state}.yaml` |
| US federal vehicle inspection | `data/inspection/us-federal.yaml` |
| US state inspection program | `data/inspection/us/states/{state}.yaml` |
| US state fines | `data/penalties/us/states/{state}.yaml` |
| US state tolls | `data/road-charging/us/states/{state}.yaml` |
| **Australia** | |
| NHVR national mass limits | `data/dimensions-weights/au-federal.yaml` |
| AU state-specific limits | `data/dimensions-weights/au/states/{state}.yaml` |
| NHVR vehicle classes / road networks | `data/road-network-classes/au-federal.yaml` → `au/states/{state}.yaml` |
| AU state inspection | `data/inspection/au/states/{state}.yaml` |
| AU state tolls | `data/road-charging/au/states/{state}.yaml` |
| **Canada** | |
| NSC national limits baseline | `data/dimensions-weights/ca-federal.yaml` |
| Province-specific weight limits | `data/dimensions-weights/ca/provinces/{prov}.yaml` |
| Federal HOS (NSC Standard 9) | `data/hours-of-service/ca-federal.yaml` |
| Provincial HOS variations | `data/hours-of-service/ca/provinces/{prov}.yaml` |
| Spring restrictions | `data/road-network-classes/ca/provinces/{prov}.yaml` |
| Provincial fines | `data/penalties/ca/provinces/{prov}.yaml` |

### Inheritance Rule (3 tiers — most specific wins)
1. **State/province file** (`us/states/ca.yaml`) — listed fields override federal
2. **Federal baseline** (`us-federal.yaml`) — listed fields override EU/AETR
3. **EU/AETR baseline** (`eu-baseline.yaml`) — ultimate fallback for EU Tier 1

If no file exists at a level, the parent level applies unchanged.

---

## Framework Tiers — Read This First

Every country belongs to one of three tiers. The tier determines which baseline file(s) to read.

### Tier 1 — EU Member States + EEA
Baseline: `references/eu/` (EU Regulations bind directly; EEA via EEA Agreement)

**EU (27):** AT BE BG CY CZ DE DK EE ES FI FR GR HR HU IE IT LT LU LV MT NL PL PT RO SE SI SK
**EEA (non-EU):** NO IS LI

### Tier 2 — AETR-only (non-EU/EEA AETR signatories)
Baseline for driving/rest + tachograph ONLY: `references/aetr/`
All other topics (tolls, licensing, dimensions, penalties): **standalone national rules** — no baseline

Key countries: **CH** (Switzerland), **TR** (Turkey), RU, UA, MA, AZ, KZ, BY, RS, BA, ME, MK, AL, MD, GE, AM, UZ, TJ, TM, TN, SM, MC

### Tier 3 — Standalone
No supranational baseline. All rules are independent national law.

Key countries: **GB** (UK, post-Brexit), **US** (FMCSA), **CA** (Transport Canada), **AU** (NHVR)

---

## Workflow

### Step 1 — Identify country and topic

**First: infer the user's likely base country from context.** Use this to apply the most relevant lookup by default, while still answering EU-general questions correctly.

| Signal | Inferred base country |
|--------|----------------------|
| Writing in Swedish | Sweden (SE) — default to SE-specific files unless another country is mentioned |
| Writing in Norwegian | Norway (NO) |
| Writing in Danish | Denmark (DK) |
| Writing in Finnish | Finland (FI) |
| Writing in German | Germany (DE) or Austria (AT) or Switzerland (CH) — apply DE as default unless CH/AT context clues present |
| Writing in Dutch | Netherlands (NL) or Belgium (BE) |
| Writing in French | France (FR) or Belgium (BE) |
| Writing in Polish | Poland (PL) |
| Mentions company name with SE/NO/DK/FI reg context | That country |
| Mentions specific road/permit/system by name | See implicit country signals below |
| No language or country signal | Answer at EU baseline level; offer to refine for a specific country |

**Implicit country signals from terminology:**

| Term | Country |
|------|---------|
| LKW-Maut, Toll Collect, BALM, Transportstyren (German), Berufskraftfahrer | DE |
| Viapass, LIMOSA, PC 140, Febetra | BE |
| FMCSA, HOS, ELD, CMV | US |
| AutoPASS, YTF, Arbeidstilsynet | NO |
| LSVA, ASTRA | CH |
| e-TOLL, Główny Inspektorat Transportu Drogowego (GITD) | PL |
| MYTO, CzechToll | CZ |
| HU-GO, Nemzeti Útdíjfizetési | HU |
| BGTOLL | BG |
| DarsGo | SI |
| ViaLietuva | LT |
| Transportstyrelsen, YKB, bärighetsklass, BK1/BK2/BK3/BK4, traktamente, sanktionsavgift, körförbud | SE |
| DTL, 3F Transport, Godsoverenskomsten | DK |
| AKT, Trafi, Traficom | FI |
| TLN, CAO BGV, ILT, RDW | NL |
| FNTR, DREAL, DREETS, CCNTR | FR |

**When the inferred country differs from the topic's country:** always state which country you are assuming and offer to switch ("Assuming you're asking about Sweden — let me know if you need another country").

Parse the question for:
- **Explicit country**: "rules in Germany", "driving to Poland", "Austrian toll"
- **Implicit country**: use terminology table above
- **Multi-country route**: "SE → DE via DK" → read SE + DK + DE files for the topic
- **EU-general question** (no specific country): read `references/eu/` only

### Step 2 — Select reference files by tier

**Tier 1 (EU/EEA member):**
1. Read `references/eu/{topic}.md` — the EU baseline
2. Check `references/topics/eu-regulation-matrix.md` for known national deviations
3. If deviation exists for this country+topic: also read `references/countries/{code}/{topic}.md`
4. Answer: "EU baseline applies ([Regulation]). [Country] specifics: ..."

**Tier 2 (AETR-only):**
- For driving/rest or tachograph: read `references/aetr/{topic}.md` as baseline, then `references/countries/{code}/{topic}.md`
- For all other topics: read `references/countries/{code}/{topic}.md` directly (standalone, no baseline)
- State: "AETR applies for driving/rest. [Country] national rules for [topic]: ..."
- Note: advance payment at roadside is **PROHIBITED** for AETR violations (AETR Art. 22ter)

**Tier 3 (standalone):**
- Read `references/countries/{code}/{topic}.md` directly
- Never cite EU or AETR as baseline — state the national framework (FMCSA, Transport Canada, NHVR, GB retained law, etc.)

**Multi-country route:**
- Read each country's files for the topic
- Clearly state which rules apply on which segment of the route

### Step 3 — Answer with law reference

- Cite exact law and article number (e.g. "Art. 6 EU Reg. 561/2006", "§34 StVZO", "49 CFR §395.3")
- Always include the source URL as a clickable link
- State penalties in **local currency** of the country where the rule applies — never convert
- Distinguish EU-uniform rule from national deviation

### Step 4 — Update mode

If the user explicitly asks to refresh, update, or verify a specific country+topic:
1. WebFetch the source URLs from that country's reference file
2. Compare with existing content
3. Update the file content and set "Last verified" to today's date

### Step 5 — Development mode

For TMS/compliance feature questions:
- State which rules are EU-uniform (safe to hardcode EU-wide) vs national (require per-country config)
- Provide implementation constants from the Implementation Notes section of relevant files
- Flag Tier 2/3 countries that use completely different frameworks requiring separate implementation

### Step 6 — Language

Answer in the same language the user writes in.
When quoting legal text in a foreign language, always translate or explain.

---

## EU Regulation Cross-Reference Matrix

See `references/topics/eu-regulation-matrix.md` for the full table.

**Quick reference — known national deviations from EU baseline:**

| Topic | EU file | Country deviations |
|-------|---------|-------------------|
| Weights/dimensions | `eu/weights-dimensions.md` | SE/FI: Nordic exception (74t/76t, 34.5m); NL: LZV (25.25m, 60t) |
| Posting portals | `eu/posting-workers.md` | BE=LIMOSA, FR=SIPSI, DE=FMS, PL=biznes.gov.pl, NL=DUOS, AT=EFZR |
| Tolls | `eu/road-charging.md` | Each country has own system — see country tolls file |
| Driving/rest | `eu/driving-rest-time.md` | SE: 100km agriculture exemption; FI: national exemptions; others no deviation |

---

## Reference File Structure

```
references/
  eu/                       ← EU baseline (13 files, Tier 1 baseline)
    driving-rest-time.md    EU 561/2006 + Mobility Package
    working-time.md         Directive 2002/15/EC
    commercial-licensing.md 1071/2009 (operator licence) + 1072/2009 (cabotage)
    professional-driver.md  Directive 2003/59/EC (CPC)
    dangerous-goods.md      ADR 2025 + Directive 2008/68/EC
    vehicle-inspection.md   Directive 2014/45/EU + 2014/47/EU
    posting-workers.md      Directive 2020/1057/EU
    smart-tachograph.md     EU 165/2014 + smart v2
    emissions.md            Euro VII + CO2 2024/1610
    weights-dimensions.md   Directive 96/53/EC
    road-charging.md        Directive 2022/362/EU (Eurovignette)
    combined-transport.md   Directive 92/106/EEC
    live-animals.md         Regulation EC 1/2005

  aetr/                     ← AETR baseline (2 files, Tier 2 driving/rest only)
    driving-rest-time.md    AETR Agreement (aligned with EU 561/2006)
    tachograph.md           AETR Annex 1B

  countries/
    se/                     ← Sweden (full coverage — 20 files)
      driving-rest.md       National deviations + SE enforcement + warning system
      exceptions.md         Undantag från kör- och vilotider
      light-vehicles.md     Vilotidsregler lätta fordon (Förordning 1994:1297)
      working-time.md       Vägarbetstid SFS 2005:395
      company-control.md    Företagskontroll
      taxi.md               Taxitrafiklag 2012:211
      penalties.md          Sanktionsavgifter (SEK amounts)
      international-transport.md Internationell godstrafik
      dimensions-weights.md SE limits (BK, 74t, 34.5m)
      bk-bearing-classes.md BK1–BK4 TSFS 2018:40
      transport-dispensation.md L/XL/XXL Trix system
      long-trucks.md        25.25m EMS + 34.5m LCV TSFS 2025:17
      road-transport-leader.md Vägtransportledare
      professional-driver.md YKB (yrkesförarkompetens)
      commercial-license.md Yrkestrafiktillstånd
      collective-transport.md Kollektivtrafik SFS 2010:1065
      collective-agreement-transport.md Transportavtalet (wages, OB, traktamente)
      environment-law.md    Miljöbalken SFS 1998:808
      tax-procedures.md     F-skatt, energiskatt, trängselskatt

    de/  no/  dk/  fi/  pl/  nl/  be/  fr/  at/  gb/
    (and all other countries — generated by pipeline as content is found)
    Collective agreements: SE NO DK NL FR DE BE AT FI

  topics/
    url-index.md            Master URL index by country + topic
    country-index.md        Coverage map (which files exist, what gaps remain)
    eu-regulation-matrix.md Full cross-reference: EU rules → countries → deviations
```

---

## Always

- Read the framework baseline file FIRST, then the country file for deviations
- Cite exact article/paragraph numbers for every rule stated
- State penalties in LOCAL CURRENCY — never convert
- Link to official source URLs
- Distinguish EU-uniform rules from national deviations
- Tier 2 countries: AETR is baseline for driving/rest only; everything else is standalone
- Tier 3 countries: no EU/AETR baseline — state the national framework explicitly
- Only fetch live URLs when user explicitly asks to update/refresh a file
