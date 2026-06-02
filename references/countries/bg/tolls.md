# Bulgaria — Road Tolls (BGTOLL)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://www.bgtoll.bg/en/ — BGTOLL: Bulgarian toll system

**Last verified: 2026-05-30**

---

## Overview

Bulgaria operates **BGTOLL**, an electronic system combining e-vignettes (for lighter vehicles and older-style charges) and a distance-based toll for HGVs >3.5t introduced in 2019.

---

## Which Vehicles Must Pay

- **Vignette**: Passenger cars and light vehicles on national road network
- **Distance toll**: Vehicles with GVW **exceeding 3.5 tonnes** on motorways, expressways, and first-class roads

---

## Road Network

Distance toll covers:
- Motorways (автомагистрали)
- Expressways (скоростни пътища)
- First-class roads (първокласни пътища)

---

## Payment

- OBU device for distance-based toll
- E-vignette purchasable online at https://web.bgtoll.bg/ or mobile apps
- Available via EETS-compatible providers

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| BGTOLL | Bulgarian toll system | https://www.bgtoll.bg/en/ |
| BGTOLL web | E-vignette and account portal | https://web.bgtoll.bg/ |

---

## Implementation Notes for Developers

```
BG_TOLL_THRESHOLD_T = 3.5
BG_EUR_BGN_FIXED_RATE = 1.95583   # fixed currency board rate
```
