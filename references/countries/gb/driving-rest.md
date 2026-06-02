# United Kingdom — Drivers' Hours Rules (Goods Vehicles)

**EU Baseline:** Not applicable — GB is Tier 3 standalone. GB retained EU 561/2006 as domestic law via EU Withdrawal Act 2018 (now called "assimilated rules"). GB is no longer subject to EU regulation updates.

**Sources:**
- https://www.gov.uk/guidance/drivers-hours-goods-vehicles — GOV.UK / DVSA: Drivers' hours rules for goods vehicles (full guidance)
- https://www.gov.uk/guidance/drivers-hours — GOV.UK / DVSA: Drivers' hours overview

**Last verified: 2026-05-30**

---

## Overview

The UK applies **assimilated EU rules** (retained EU 561/2006) for goods vehicle drivers' hours — rules are substantively identical to EU 561/2006 as of the Brexit date (31 December 2020). The UK has not adopted subsequent EU Mobility Package 2022 amendments domestically, so there may be divergence over time. Enforcement is by DVSA (Driver and Vehicle Standards Agency) and the police.

---

## Core Rules (Assimilated Rules — mirror EU 561/2006)

| Rule | Limit |
|------|-------|
| Daily driving (normal) | **9 hours** |
| Daily driving (extended, max 2×/week) | **10 hours** |
| Weekly driving | **56 hours** |
| Two-consecutive-week driving | **90 hours** |
| Break after 4.5h driving | **45 minutes** (or 15+30 split) |
| Regular daily rest | **11 consecutive hours** |
| Reduced daily rest (max 3×/week) | **9 consecutive hours** |
| Split daily rest | 3h + 9h = minimum 12h total |
| Normal weekly rest | **45 consecutive hours** |
| Reduced weekly rest | **24 consecutive hours** (compensation required within 3 weeks) |
| Multi-manning: rest within | **30 hours** |
| Fixed week | Monday 00:00 – Sunday 24:00 |

---

## Deviations from EU 561/2006 (Post-Brexit)

| Topic | EU 561/2006 (as amended) | GB assimilated rules |
|-------|-------------------------|---------------------|
| Cab prohibition for weekly rest | YES (from Feb 2022 Mobility Package) | **Status unclear** — Mobility Package not adopted into GB domestic law |
| Return home every 4 weeks | YES (Mobility Package) | **Not confirmed** as adopted |
| 2.5–3.5t from July 2026 | YES (EU scope extension) | **Not adopted** — GB threshold remains >3.5t |

Operators should check DVSA guidance for the latest position on any Mobility Package provisions.

---

## Scope (Which Vehicles)

**In scope (assimilated rules):**
- Goods vehicles exceeding **3.5 tonnes** maximum permissible weight (laden or unladen)
- Including trailers and dual-purpose vehicles
- UK-only journeys and UK-EU journeys

**Exempt:**
- Vehicles under 40 km/h maximum speed
- Emergency/rescue services
- Vehicles ≤7.5t for non-commercial carriage
- Specialist breakdown vehicles operating within 100 km radius
- (See DVSA guidance for full list)

---

## AETR Rules (International Journeys)

For journeys involving AETR countries, AETR rules apply for the **entire journey**. AETR largely mirrors the assimilated rules with minor differences on ferry/train rest interruptions.

---

## Enforcement

| Authority | Role | Website |
|-----------|------|---------|
| DVSA (Driver and Vehicle Standards Agency) | Main HGV enforcement: roadside checks, operator compliance | https://www.gov.uk/dvsa |
| Traffic Commissioners | Operator licensing (O-licence), company enforcement | https://www.gov.uk/traffic-commissioner |
| Police | Roadside spot checks | — |

**Deposit system for foreign drivers:** Drivers without a verifiable UK address who commit a violation can be required to pay a **deposit equal to the fixed penalty** before continuing. Vehicle may be immobilised until paid.

**Lookback period at roadside:** 56 days (same as EU standard).

---

## Penalties

| Violation level | Court fine level | Examples |
|----------------|----------------|---------|
| Driving time/rest period violations | **Level 4** fine (up to £2,500) | Exceeding daily driving, insufficient rest |
| Tachograph installation/use failures | **Level 5** fine (unlimited) | Failure to use tachograph, record tampering |
| False entries / seal tampering | Up to **2 years imprisonment** (indictment) | Tachograph fraud |

DVSA graduated fixed penalty system also applies at roadside for less serious violations.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| GOV.UK / DVSA | Full drivers' hours guidance (goods vehicles) | https://www.gov.uk/guidance/drivers-hours-goods-vehicles |
| GOV.UK / DVSA | Enforcement and penalties | https://www.gov.uk/guidance/drivers-hours-goods-vehicles/6-enforcement-and-penalties |
| Transport Act 1968 | UK primary legislation for drivers' hours | — |

---

## Implementation Notes for Developers

```
GB_DAILY_DRIVING_NORMAL_H = 9
GB_DAILY_DRIVING_EXTENDED_H = 10
GB_WEEKLY_DRIVING_MAX_H = 56
GB_BIWEEKLY_DRIVING_MAX_H = 90
GB_BREAK_AFTER_H = 4.5
GB_BREAK_MIN_MIN = 45
GB_DAILY_REST_NORMAL_H = 11
GB_DAILY_REST_REDUCED_H = 9
GB_WEEKLY_REST_NORMAL_H = 45
GB_WEEKLY_REST_REDUCED_H = 24
GB_THRESHOLD_T = 3.5               # >3.5t in scope (NOT extended to 2.5t)
GB_WEEK = "Mon 00:00 – Sun 24:00"  # fixed week definition
```
