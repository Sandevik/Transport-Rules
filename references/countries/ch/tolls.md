# Switzerland — Road Tolls (LSVA — Heavy Vehicle Fee)

**EU Baseline:** Not applicable — standalone Swiss national rule. Switzerland is Tier 2 (AETR); all topics except driving/rest are standalone.

**Sources:**
- https://www.bazg.admin.ch/bazg/en/home/informationen-firmen/verkehrsabgaben-und-strassenverkehrsrecht/schwerverkehrsabgaben-lsva-und-psva.html — BAZG: Heavy vehicle charges (LSVA and PSVA)
- https://www.ezv.admin.ch/ezv/en/home/information-companies/transport--travel-documents--road-taxes/heavy-vehicle-charges--performance-related-and-lump-sum-.html — EZV: LSVA overview

**Last verified: 2026-06-01**

---

## Overview

Switzerland operates the **LSVA (Leistungsabhängige Schwerverkehrsabgabe — Performance-related Heavy Vehicle Charge)** — a distance-based charge for all heavy vehicles using Swiss roads. This is completely separate from the EU Eurovignette framework. The LSVA applies to all HGVs >3.5t and is one of the world's most comprehensive heavy vehicle charges, covering **all Swiss roads** (not just motorways).

---

## Which Vehicles Must Pay

- Vehicles with GVW **exceeding 3.5 tonnes**
- Applies to Swiss and foreign vehicles
- Both laden and unladen journeys

---

## Roads Covered

**All Swiss roads** — not limited to motorways or expressways. The LSVA applies on every public road in Switzerland.

---

## Rate Structure

The LSVA rate is calculated as:

**LSVA = Distance (km) × Maximum GVW (t) × Emissions factor (CHF/tkm)**

The LSVA uses a three-tier emission category structure (set by Federal Council ordinance, SVAV SR 641.811):

| Emission category | Vehicles included | Rate (CHF per tonne-km) |
|-------------------|------------------|------------------------|
| **Category 1** (highest) | Pre-Euro / Euro 0 | CHF 0.0369/tkm |
| **Category 2** | Euro I, Euro II, Euro III, Euro IV | CHF 0.0276/tkm |
| **Category 3** (lowest) | Euro V, EEV, Euro VI | CHF 0.0184/tkm |
| **Zero Emission (ZEV)** | Electric / hydrogen | CHF 0.00/tkm (exempt) |

*Note: Exact rates are set by Federal Council ordinance and subject to periodic revision. LSVA III (digital system, introduced 2025) may carry updated rate structures. Always verify current rates at bazg.admin.ch.*

**Calculation examples:**
- 40t truck, Euro VI, 100km: 40 × 100 × 0.0184 = **CHF 73.60**
- 40t truck, Euro VI, 300km (full transit): 40 × 300 × 0.0184 = **CHF 220.80**
- 40t truck, Euro 0 (old), 100km: 40 × 100 × 0.0369 = **CHF 147.60**
- 26t rigid HGV, Euro VI, 200km: 26 × 200 × 0.0184 = **CHF 95.68**

---

## PSVA (Flat-Rate Heavy Vehicle Charge)

For vehicles not equipped with the LSVA on-board unit, a flat-rate charge (**PSVA — Pauschale Schwerverkehrsabgabe**) applies. The PSVA is significantly more expensive than the LSVA and is intended as the exception, not the norm.

---

## OBU Requirement

- A **LSVA on-board unit (OBU)** is required for all HGVs
- The OBU automatically records distance in Switzerland (GPS-based) and reports to Swiss Customs (BAZG)
- Foreign operators must obtain an OBU before entering Switzerland or at the border
- Available at BAZG border offices and via authorized distributors

---

## Registration

Foreign operators must register with BAZG:
1. Apply for LSVA account at https://www.bazg.admin.ch/
2. Obtain OBU or declare for PSVA flat rate
3. Ensure vehicle GVW and emission class are correctly registered

---

## Penalties

Non-payment or fraudulent OBU data results in:
- Retroactive LSVA charges + penalty surcharge
- Criminal sanctions possible under Swiss customs law

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| BAZG | LSVA — heavy vehicle charges overview | https://www.bazg.admin.ch/bazg/en/home/informationen-firmen/verkehrsabgaben-und-strassenverkehrsrecht/schwerverkehrsabgaben-lsva-und-psva.html |
| EZV | LSVA and PSVA information | https://www.ezv.admin.ch/ezv/en/home/information-companies/transport--travel-documents--road-taxes/heavy-vehicle-charges--performance-related-and-lump-sum-.html |

---

## Implementation Notes for Developers

```
CH_LSVA_THRESHOLD_T = 3.5            # all public roads, not just motorways
CH_LSVA_ALL_ROADS = True
CH_LSVA_FORMULA = "distance_km × max_gvw_t × rate_chf_per_tkm"
CH_LSVA_CAT1_EURO0_RATE       = 0.0369   # CHF/tkm — pre-Euro / Euro 0
CH_LSVA_CAT2_EUROI_IV_RATE    = 0.0276   # CHF/tkm — Euro I through Euro IV
CH_LSVA_CAT3_EUROV_PLUS_RATE  = 0.0184   # CHF/tkm — Euro V, EEV, Euro VI
CH_LSVA_ZEV_RATE              = 0.0       # Zero-emission vehicles exempt
CH_OBU_REQUIRED = True                    # LSVA III digital OBU from 2025
# Example: 40t Euro VI truck, 300km = 40 × 300 × 0.0184 = CHF 220.80
```
