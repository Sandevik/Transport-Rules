# Germany — Vehicle Dimensions and Weights

**EU Baseline:** [references/eu/weights-dimensions.md — Directive 96/53/EC (as amended by Directive 2015/719/EU)]

**Sources:**
- https://www.bmwk.de/Redaktion/DE/Artikel/Verkehr/lang-lkw.html — BMWK: Long trucks (Lang-Lkw) in Germany
- https://www.stvo.de/strassenverkehrsordnung/anlage-9-masse-und-gewichte/ — StVZO Anlage 9
- https://www.balm.bund.de/EN/Topics/Oversize-Loads/oversize-loads.html — BALM: Oversize loads

**Last verified: 2026-05-31**

---

## Overview

Germany applies EU standard weights and dimensions (Directive 96/53/EC) as the baseline. The national implementing regulation is §34 StVZO (Straßenverkehrs-Zulassungs-Ordnung). Germany has a national programme for Lang-Lkw (long trucks up to 25.25m) on a designated positive network (Positivnetz), which is additional to EU standard rules.

---

## Standard EU Limits (Apply in Germany)

| Parameter | Limit | Legal basis |
|-----------|-------|-------------|
| Max GVW (general) | **40 tonnes** | §34 StVZO / Directive 96/53/EC |
| Max GVW (combined transport, 5+ axles) | **44 tonnes** | Directive 92/106/EEC |
| Max GVW (bimodal — rail/road, 5+ axles) | **44 tonnes** | Directive 96/53/EC Art. 4(4) |
| Max width (general) | **2.55 m** | §32 StVZO |
| Max width (refrigerated superstructure) | **2.60 m** | §32 StVZO |
| Max height | **4.00 m** | §32 StVZO |
| Max length (articulated vehicle) | **16.50 m** | §32 StVZO |
| Max length (road train) | **18.75 m** | §32 StVZO |

---

## Axle Weight Limits

| Axle type | Max load |
|-----------|----------|
| Single driving axle | 11.5 t |
| Non-driving single axle | 10.0 t |
| Tandem axle group | 18.0 t (steel springs) / 19.0 t (air suspension) |
| Tridem axle group | 24.0 t |

---

## Lang-Lkw (Long Truck Programme) — National Addition

Germany operates a **Positivnetz** (positive network) of designated roads where Lang-Lkw (long trucks) up to **25.25m** may operate:
- Max weight: 40t (same as standard; no extra weight allowance for Lang-Lkw)
- Requires prior route approval on the Positivnetz network
- Not permitted on all roads — must check BALM/BMWK Positivnetz map

The Positivnetz is managed by BMWK and is available at: https://www.bmwk.de/Redaktion/DE/Artikel/Verkehr/lang-lkw.html

---

## Oversize/Overweight Loads

Loads exceeding standard limits require a transport permit (Erlaubnis or Ausnahmegenehmigung):
- **Erlaubnis** (up to 5m wide, 70t): issued by Landesbehörden (state road authorities)
- **Ausnahmegenehmigung**: for extreme dimensions
- National permit application: via VEMAGS system (https://www.vemags.de/)

Escort vehicles (Begleitfahrzeuge) required for widths >3.0m or lengths >30m.

---

## Deviations from EU Baseline

- **Lang-Lkw programme** (25.25m): additional national programme on designated network
- **Axle weight details** set by §34 StVZO (closely aligned with EU)

---

## Enforcement

| Authority | Full name | Website |
|-----------|-----------|---------|
| BALM | Bundesamt für Logistik und Mobilität | https://www.balm.bund.de/EN/ |
| Polizei | State police — roadside dimension/weight checks | — |
| Landesbehörden | State road authorities — permit issuance | varies |

**Advance payment at roadside:** YES — BALM can demand security deposits (Sicherheitsleistung) from foreign carriers for overweight violations.

---

## Penalties

| Violation | Penalty (EUR) | Legal basis |
|-----------|--------------|-------------|
| Exceeding max GVW (up to 5%) | €135–€395 | §69a StVZO |
| Exceeding max GVW (>20%) | €855 + immobilisation | §69a StVZO |
| Exceeding max width/length without permit | €255–€1,530 | §69a StVZO |
| Operating Lang-Lkw off Positivnetz | €305 | §69a StVZO |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| BALM | Oversize load permits and enforcement | https://www.balm.bund.de/EN/Topics/Oversize-Loads/oversize-loads.html |
| BMWK | Lang-Lkw Positivnetz | https://www.bmwk.de/Redaktion/DE/Artikel/Verkehr/lang-lkw.html |
| VEMAGS | National permit application system | https://www.vemags.de/ |
| EUR-Lex | Directive 96/53/EC | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31996L0053 |

---

## Implementation Notes for Developers

```
DE_MAX_GVW_T = 40.0
DE_MAX_GVW_COMBINED_TRANSPORT_T = 44.0
DE_MAX_WIDTH_M = 2.55
DE_MAX_WIDTH_REEFER_M = 2.60
DE_MAX_HEIGHT_M = 4.00
DE_MAX_LENGTH_ARTIC_M = 16.50
DE_MAX_LENGTH_ROAD_TRAIN_M = 18.75
DE_LANG_LKW_LENGTH_M = 25.25   # on designated Positivnetz only
```
