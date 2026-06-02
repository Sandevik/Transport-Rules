# Austria — Road Tolls (ASFINAG GO Toll)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://www.asfinag.at/en/toll/ — ASFINAG: Austrian toll system overview
- https://www.asfinag.at/en/toll/go-toll/ — ASFINAG: GO Toll for trucks

**Last verified: 2026-06-01**

---

## Overview

Austria operates a distance-based **GO Toll** for heavy vehicles on all motorways and expressways, administered by **ASFINAG** (Autobahnen- und Schnellstraßen-Finanzierungs-Aktiengesellschaft). The system uses a GO-Box (OBU) with microwave technology. A separate vignette applies to vehicles ≤3.5t (not relevant for HGV).

---

## Which Vehicles Must Pay

All vehicles with a technically permissible maximum laden mass (TPMLM) **exceeding 3.5 tonnes**.

---

## Roads Covered

All Austrian **motorways (Autobahnen)** and **expressways (Schnellstraßen)** — the complete ASFINAG network.

---

## Rate Structure (2026)

Effective 1 January 2026. Source: go-maut.at official rate table.
All rates in **EUR/km, excluding 20% Austrian VAT**. Rates include infrastructure, air pollution, noise, and CO₂ cost components.

| CO₂/Emission Class | Emission Standard | 2 Axles | 3 Axles | 4+ Axles |
|--------------------|------------------|---------|---------|----------|
| Class 5            | Zero Emission    | 0.0587  | 0.0806  | 0.1189   |
| Class 4            | EURO VI          | 0.2486  | 0.3440  | 0.5091   |
| Class 3            | EURO VI          | 0.2724  | 0.3788  | 0.5625   |
| Class 2            | EURO VI          | 0.2740  | 0.3810  | 0.5657   |
| Class 1            | EURO VI          | 0.2774  | 0.3856  | 0.5724   |
| Class 1            | EURO V/EEV       | 0.2924  | 0.4086  | 0.6024   |
| Class 1            | EURO IV          | 0.3114  | 0.4296  | 0.6324   |
| Class 1            | EURO 0–III       | 0.3274  | 0.4536  | 0.6654   |

**Typical reference:** 5-axle artic, Euro VI (Class 1) = **€0.5724/km** (excl. VAT) = ~€0.687/km incl. VAT.

**Section toll surcharges (+25%)** apply on specific tunnel/mountain sections:
- Gleinalm Tunnel (A9)
- Tauern Tunnel (A10)
- Karawanken Tunnel (A11)
- A12 Lower Inn Valley (Brenner corridor)
- Arlberg Tunnel (A14)

---

## GO-Box (OBU)

- Required for all HGVs >3.5t
- Uses microwave technology (DSRC) to communicate with gantries
- Must be correctly mounted on the windscreen
- Available at 175+ sales points across Austria and at border crossings
- Can also be obtained via ASFINAG webshop: https://shop.asfinag.at/

---

## Registration for Foreign Operators

1. Purchase GO-Box at ASFINAG sales point, border crossing, or webshop
2. Activate GO-Box with vehicle data (registration, emission class)
3. Ensure payment method is linked
4. Mount GO-Box before entering Austrian motorways

---

## Penalties

| Violation | Consequence |
|-----------|------------|
| Using motorway without GO-Box | Substitute toll charge + fine |
| GO-Box not correctly mounted | Substitute toll charge |
| Incorrect emission class declared | Back-payment of difference + fine |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| ASFINAG | GO Toll overview and rates | https://www.asfinag.at/en/toll/go-toll/ |
| ASFINAG | Webshop (GO-Box purchase) | https://shop.asfinag.at/ |
| go-maut.at | Dedicated GO Toll information site | https://www.go-maut.at/ |

---

## Implementation Notes for Developers

```
AT_GO_TOLL_THRESHOLD_T = 3.5           # TPMLM above this triggers GO Toll
AT_GO_TOLL_VAT_PCT = 20                # rates on go-maut.at are excl. VAT
AT_GOBOX_REQUIRED = True
AT_TUNNEL_SURCHARGE_PCT = 25           # on 5 specific sections
# Reference rates (EUR/km excl. VAT), effective 1 January 2026:
AT_RATE_2AX_ZEV      = 0.0587
AT_RATE_2AX_EUROVI   = 0.2774         # Class 1 / worst CO2 subclass
AT_RATE_2AX_EURO0III = 0.3274
AT_RATE_4AX_ZEV      = 0.1189
AT_RATE_4AX_EUROVI   = 0.5724         # 5-axle artic, Euro VI Class 1
AT_RATE_4AX_EURO0III = 0.6654
```
