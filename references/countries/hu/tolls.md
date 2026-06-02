# Hungary — Road Tolls (HU-GO)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://www.hu-go.hu/?language=eng — HU-GO: Hungarian electronic toll system
- https://nemzetiutdij.hu/en/e-toll/ — NTPS: National Toll Payment Service

**Last verified: 2026-06-01**

---

## Overview

Hungary operates the **HU-GO** electronic toll system for vehicles >3.5t on its motorway and main road network. The system is GNSS-based and administered by the National Toll Payment Service (NTPS). Hungary's HU-GO is one of the earlier established GNSS toll systems in Central Europe.

---

## Which Vehicles Must Pay

Vehicles with GVW **exceeding 3.5 tonnes** on:
- All **motorways (autópályák — M-roads)**
- All **expressways (autóutak)**
- Selected **national roads**

---

## Rate Structure

Rates differentiated by axle count, Euro emission class (J1–J5 categories), and road category (motorway vs national road).

**Emission class mapping:** J1 = Euro 0, J2 = Euro I–II, J3 = Euro III, J4 = Euro IV, J5 = Euro V and above (including Euro VI).

### Motorways and expressways (approximate rates in HUF/km)

| Vehicle | J1 (Euro 0) | J3 (Euro III) | J5 (Euro V+/VI) |
|---------|-------------|---------------|-----------------|
| 2-axle HGV | 62 | 50 | 36 |
| 3-axle     | 89 | 72 | 52 |
| 4-axle     | 107 | 86 | 62 |
| 5+ axle (artic) | 122 | 98 | **71** |

**Typical reference:** 5-axle artic, Euro VI = ~71 HUF/km ≈ **€0.18/km** (at ~400 HUF/EUR).
Same vehicle, Euro 0 = ~122 HUF/km ≈ €0.31/km.

*Note: These are indicative figures based on published NKHT tariff schedules. Use the HU-GO toll calculator at hu-go.hu for exact current rates.*

---

## OBU and Registration

**OBU required.** GNSS-based On-Board Unit.

**Registration options:**
1. Register at https://www.hu-go.hu/
2. Use an EETS-compatible service provider
3. Manual declaration (less common, higher cost)

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| HU-GO | Hungarian toll system | https://www.hu-go.hu/?language=eng |
| NTPS | National Toll Payment Service | https://nemzetiutdij.hu/en/ |

---

## Implementation Notes for Developers

```
HU_TOLL_THRESHOLD_T = 3.5
HU_OBU_REQUIRED = True
```
