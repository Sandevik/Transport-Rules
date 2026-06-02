# Poland — Road Tolls (e-TOLL)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://etoll.gov.pl/en/ — e-TOLL: Polish electronic toll collection system
- https://etoll.gov.pl/en/e-toll-system/rates-and-payments/ — e-TOLL: Rates and payments

**Last verified: 2026-06-01**

---

## Overview

Poland operates the **e-TOLL** electronic system for distance-based tolls on national roads. As of 2021, e-TOLL replaced the earlier viaTOLL system. The system applies to trucks >3.5t on motorways (autostrady), expressways (drogi ekspresowe), and selected national roads.

---

## Which Vehicles Must Pay

- Vehicles with GVW **exceeding 3.5 tonnes** used for goods transport
- Buses with more than 9 seats
- Applies to Polish and foreign vehicles

---

## Roads Covered

- All **motorways (autostrady — A-roads)**
- All **expressways (drogi ekspresowe — S-roads)**
- Selected **national roads (drogi krajowe)** including some former toll-road sections

---

## Rate Structure (effective 1 February 2026)

Source: Official e-TOLL rate PDFs published by KAS/Ministerstwo Finansów. All rates in **PLN/km**.

### Class A and S roads (motorways and expressways)

| Vehicle category | max Euro 2 | Euro 3 | Euro 4 | min Euro 5 (incl. Euro 6) |
|-----------------|-----------|--------|--------|---------------------------|
| HGV 3.5t – <12t | 0.80      | 0.70   | 0.58   | **0.41**                  |
| HGV ≥12t        | 1.07      | 0.93   | 0.75   | **0.56**                  |
| Buses (all GVW) | 0.80      | 0.70   | 0.58   | 0.41                      |

### Class G and GP roads (main national roads — lower rates)

| Vehicle category | max Euro 2 | Euro 3 | Euro 4 | min Euro 5 (incl. Euro 6) |
|-----------------|-----------|--------|--------|---------------------------|
| HGV 3.5t – <12t | 0.66      | 0.58   | 0.47   | **0.34**                  |
| HGV ≥12t        | 0.83      | 0.75   | 0.60   | **0.42**                  |
| Buses (all GVW) | 0.66      | 0.58   | 0.47   | 0.34                      |

**Typical reference:** HGV ≥12t, Euro VI (min Euro 5 category), motorway = **0.56 PLN/km** (~€0.13/km at 4.25 PLN/EUR).

**Note:** Euro 5 and Euro 6 are grouped in the same "min Euro 5" rate category — no further differentiation. PDF sources: etoll.gov.pl rates & payments section.

---

## Payment Methods

**Prepaid accounts:**
- Payment card, fleet card, BLIK, PayByLink, cash at service centres, bank transfer

**Postpaid accounts (with collateral):**
- Debit notes issued within 7 business days after billing period; payable within 14 days

**OBU (On-Board Unit):**
- GNSS-based OBU required for electronic tracking
- Can also use the e-TOLL app (mobile GNSS)
- OBU/ELS devices available through e-TOLL registered service providers

---

## Registration for Foreign Operators

1. Create account at https://etoll.gov.pl/en/
2. Register vehicle(s)
3. Obtain OBU or activate mobile GNSS app
4. Fund prepaid account or set up postpaid with collateral

---

## Penalties

Non-payment or OBU failure results in:
- Administrative fines (kara administracyjna) issued by GITD
- Vehicle immobilisation possible for repeated violations

Penalty details: https://ebok.canard.gitd.gov.pl/

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| e-TOLL | Polish toll system — registration and rates | https://etoll.gov.pl/en/ |
| GITD | Administrative fines for e-TOLL violations | https://gitd.gov.pl/ |

---

## Implementation Notes for Developers

```
PL_ETOLL_THRESHOLD_T = 3.5
PL_ETOLL_APPLIES_TO = ["motorways (A)", "expressways (S)", "national roads G/GP"]
PL_OBU_REQUIRED = True              # or e-TOLL mobile GNSS app
# Reference rates (PLN/km), effective 1 February 2026:
# A/S roads (motorways & expressways):
PL_RATE_AS_HGV_12T_PLUS_EURO6  = 0.56   # min Euro 5 category
PL_RATE_AS_HGV_12T_PLUS_EURO0  = 1.07   # max Euro 2 category
PL_RATE_AS_HGV_UNDER12T_EURO6  = 0.41
# G/GP roads (main national roads):
PL_RATE_GP_HGV_12T_PLUS_EURO6  = 0.42
PL_RATE_GP_HGV_12T_PLUS_EURO0  = 0.83
```
