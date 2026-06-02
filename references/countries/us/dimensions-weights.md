# United States — Vehicle Dimensions and Weights

**Not applicable — standalone national framework (FHWA/FMCSA)**

**Sources:**
- [FHWA: Federal Truck Size and Weight Laws](https://ops.fhwa.dot.gov/freight/policy/rpt_congress/truck_sw_laws/index.htm)
- [Bridge Formula Weights (FHWA)](https://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/)
- [23 CFR Part 658 — Truck Size and Weight](https://www.ecfr.gov/current/title-23/part-658)
- [23 USC 127 — Vehicle Weight Limitations](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title23-section127)

**Last verified: 2026-05-31**

---

## Overview

US federal truck size and weight rules apply on the **Interstate System and Federal-aid National Highway System (NHS)**. The federal government limits gross vehicle weight to **80,000 lbs (36.3t)** on the Interstate, with axle limits enforced via the Federal Bridge Formula. States control weight and dimension limits on non-Interstate roads and may set higher (grandfathered) or lower limits. All 50 states + DC have their own regulations for state roads — see `data/dimensions-weights/us/states/` for individual state files.

## Federal Limits (Interstate System)

| Parameter | Federal limit | Legal basis |
|---|---|---|
| Gross Vehicle Weight | 80,000 lbs (36,287 kg) | 23 USC 127 |
| Single axle | 20,000 lbs (9,072 kg) | 23 USC 127 |
| Tandem axle | 34,000 lbs (15,422 kg) | 23 USC 127 |
| Width | 102 inches (2.59m) | 23 CFR Part 658 |
| Semi-trailer length (minimum allowed by states) | 48 ft (14.6m) | 23 CFR Part 658 |
| Twin trailer each | 28 ft (8.5m) | 23 CFR Part 658 |
| Height | No federal limit | States typically 13'6" (4.11m) or 14'0" (4.27m) |

*Note: No federal length limit on single vehicles (tractors/straight trucks); states set their own.*

## Federal Bridge Formula (Bridge Formula B)

All multi-axle weight groups must comply with the formula:

**W = 500 × [ LN / (N-1) + 12N + 36 ]**

Where:
- **W** = maximum weight (lbs) on any group of 2 or more consecutive axles
- **L** = distance (ft) between outer axles of the group
- **N** = number of axles in the group

The more restrictive of the bridge formula result or the axle/GVW limit applies.

## Longer Combination Vehicles (LCVs)

Federal law (ISTEA 1991 Section 1023) **froze** LCV routes and weights as of June 1, 1991. States that allowed LCVs before that date may continue:

| LCV type | States permitted | Typical limits |
|---|---|---|
| **Triple trailers** (3×28ft) | AZ, CO, ID, IN, KS, MT, NE, NV, ND, OH, OK, OR, SD, UT, WY + others | 95–105ft; designated Interstate routes only |
| **Turnpike doubles** (2×48ft) | FL, IN, KS, MA, NY, NJ, OH, PA, NV, WY + others | On turnpikes/designated roads |
| **Rocky Mountain doubles** | Western states | Long semi + short pup trailer |

States that did not allow LCVs in 1991 **cannot** add them without federal law change.

## STAA National Network

The Surface Transportation Assistance Act (STAA) 1982 established the **National Network** — all Interstate highways plus many other NHS routes — where 53ft semitrailers and 28.5ft twin trailers must be allowed regardless of state default limits.

## Spring Weight Restrictions

16+ northern/mountain states impose seasonal weight reductions (typically 25–35% reduction) from approximately February–June during spring thaw. Federal law does not require or govern these — states manage independently. Key states: MN, WI, MI, ND, SD, MT, ME, VT, NH, NY, PA, OH, IA, ID, WY.

## State Variations

Each state sets its own limits on non-Interstate roads. Notable examples:
- **Texas**: Up to 84,000 lbs GVW on non-Interstate with TxDMV permit
- **Iowa**: Up to 105,500 lbs on non-Interstate routes with state permit
- **Oregon**: Up to 105,500 lbs on certain routes with permit
- **California**: 80,000 lbs standard; CARB emissions rules add compliance layer

*See `data/dimensions-weights/us/states/{state}.yaml` for all 50 states + DC.*

## Enforcement

| Authority | Full name | Website |
|---|---|---|
| FHWA | Federal Highway Administration — weight rules | https://ops.fhwa.dot.gov |
| FMCSA | Federal Motor Carrier Safety Administration | https://www.fmcsa.dot.gov |
| State DOTs + police | Enforcement on all roads | Varies by state |
| CVSA | Commercial Vehicle Safety Alliance — inspections | https://cvsa.org |

## Penalties

| Violation | Penalty (USD) | Legal basis |
|---|---|---|
| Overweight (Interstate) | Up to $10,000 per violation + per-lb overcharge | 23 USC 127; State law |
| Bridge formula violation | Fines vary by state; civil liability for bridge damage | State law + common law |
| Operating in excess of permit | Up to $10,000 + permit revocation | State law |

*Penalties are set by individual states for state roads. Federal civil penalties apply for Interstate violations.*

## Key Regulatory Sources

| Source | Content | URL |
|---|---|---|
| FHWA Bridge Formula | Bridge Formula B guide | https://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/ |
| 23 USC 127 | Federal weight limitations statute | https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title23-section127 |
| 23 CFR Part 658 | Federal size/weight regulations | https://www.ecfr.gov/current/title-23/part-658 |
| FHWA Truck Size and Weight | Policy summary | https://ops.fhwa.dot.gov/freight/policy/rpt_congress/truck_sw_laws/ |
