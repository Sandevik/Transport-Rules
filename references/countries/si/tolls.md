# Slovenia — Road Tolls (DarsGo + E-Vinjeta)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://www.darsgo.si — DarsGo: Electronic toll for HGVs
- https://evinjeta.dars.si/en — E-Vinjeta: Vignette for light vehicles

**Last verified: 2026-05-30**

---

## Overview

Slovenia uses a **dual system**:
- **DarsGo** — distance-based electronic toll for HGVs (>3.5t) on motorways and expressways
- **E-Vinjeta** — time-based vignette for light vehicles (≤3.5t) — not applicable for HGVs

---

## DarsGo (Heavy Vehicles >3.5t)

**OBU-based GNSS distance toll** for all vehicles >3.5t on Slovenian motorways (avtoceste) and expressways (hitre ceste).

**Registration:** https://www.darsgo.si
- Register online or at DARS toll points
- OBU device required (available at border crossings and petrol stations)
- EETS-compatible transponders accepted

**Rates:** Per-km rate by vehicle weight/axle category and emission class.

**Penalty:** Fine for non-payment or OBU tampering.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| DarsGo | HGV electronic toll system | https://www.darsgo.si |
| DARS | Slovenian motorway operator | https://www.dars.si |

---

## Implementation Notes for Developers

```
SI_DARSGO_THRESHOLD_T = 3.5
SI_OBU_REQUIRED = True
```
