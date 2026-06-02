# Belgium — Road Tolls (Viapass Kilometre Charge)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://www.viapass.be/en/ — Viapass: Belgian km-charge system

**Last verified: 2026-06-01**

---

## Overview

Belgium operates a **distance-based kilometre charge** for heavy goods vehicles, administered by **Viapass** — an interregional entity covering all three Belgian regions. The charge applies to all HGVs >3.5t on Belgian roads, making it one of the broadest toll coverage systems in Europe (not limited to motorways).

---

## Which Vehicles Must Pay

- All motor vehicles and combinations used for goods transport with GVW **exceeding 3.5 tonnes**
- Applies to Belgian and foreign vehicles alike

---

## Roads Covered

The km-charge applies to:
- **Flemish Region** roads
- **Brussels Capital Region** roads
- **Walloon Region** roads managed by SOFICO

Covers motorways, national roads, and a significant part of regional roads.

---

## Rate Structure (effective 1 January 2026)

Source: viapass.be official rate table. All rates in **EUR/km** (ex-VAT for Wallonia; Flanders and Brussels rates are taxes, VAT-exempt).

### Wallonia

| Euro class | 3.5–12t | 12–32t | >32t  |
|------------|---------|--------|-------|
| Euro 0–2   | 0.113   | 0.220  | 0.251 |
| Euro 3     | 0.113   | 0.220  | 0.251 |
| Euro 4     | 0.084   | 0.191  | 0.222 |
| Euro 5     | 0.070   | 0.177  | 0.208 |
| Euro 6     | 0.056   | 0.163  | 0.194 |
| ZEV        | 0.056   | 0.163  | 0.194 |

### Flanders

| Euro class | 3.5–12t | 12–32t | >32t  |
|------------|---------|--------|-------|
| Euro 0–2   | 0.158   | 0.268  | 0.301 |
| Euro 3     | 0.132   | 0.242  | 0.275 |
| Euro 4     | 0.089   | 0.200  | 0.233 |
| Euro 5     | 0.074   | 0.184  | 0.217 |
| Euro 6     | 0.060   | 0.171  | 0.204 |
| ZEV        | 0.009   | 0.031  | 0.038 |

### Brussels Capital Region — Highway / Urban

| Euro class | Highway 3.5–12t | Highway >32t | Urban 3.5–12t | Urban >32t |
|------------|-----------------|--------------|----------------|------------|
| Euro 0–2   | 0.192           | 0.263        | 0.247          | 0.384      |
| Euro 3     | 0.166           | 0.237        | 0.214          | 0.351      |
| Euro 4     | 0.125           | 0.196        | 0.174          | 0.310      |
| Euro 5     | 0.110           | 0.181        | 0.156          | 0.293      |
| Euro 6     | 0.097           | 0.168        | 0.130          | 0.267      |
| ZEV        | 0.017           | 0.031        | 0.023          | 0.050      |

**Typical reference:** 40t 5-axle artic (>32t category), Euro 6, Wallonia = **€0.194/km**; same in Flanders = €0.204/km.

**From 1 July 2026:** Additional CO₂ surcharge applies to Flemish rates. Check viapass.be for updated figures.

---

## OBU Requirement

An **On-Board Unit (OBU)** is required. The OBU automatically records distance and vehicle category for billing.

**Important:** As of **January 1, 2026**, blue Axxès OBU devices (models Kapsch S5310 and S3290) are **no longer supported**. Using these on Belgian roads results in a fine. All operators must use compliant OBU hardware.

**OBU providers (Toll Service Providers):**
- Axxès (new devices only)
- Satellic
- DKV
- EETS-compatible OBUs

---

## Registration

Foreign operators must:
1. Obtain a compliant OBU from an authorized Toll Service Provider
2. Register the vehicle and OBU before entering Belgium
3. Ensure the OBU is activated and functioning

---

## Enforcement

LIDAR-based and overhead gantry checks verify OBU compliance across the Belgian road network. Non-compliance results in fines.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Viapass | Belgian km-charge — rates, OBU, registration | https://www.viapass.be/en/ |

---

## Implementation Notes for Developers

```
BE_TOLL_THRESHOLD_T = 3.5            # GVW above this requires km-charge
BE_TOLL_APPLIES_TO = "all Belgian public roads in all 3 regions"
BE_OBU_REQUIRED = True
BE_LEGACY_KAPSCH_S5310_INVALID_FROM = "2026-01-01"
# Reference rates (EUR/km), effective 1 January 2026:
BE_RATE_WALLONIA_EURO6_OVER32T     = 0.194
BE_RATE_FLANDERS_EURO6_OVER32T     = 0.204
BE_RATE_BRUSSELS_URBAN_EURO6_32T   = 0.267
BE_RATE_WALLONIA_EURO0_OVER32T     = 0.251
BE_RATE_FLANDERS_ZEV_OVER32T       = 0.038
BE_CO2_SURCHARGE_FLANDERS_FROM     = "2026-07-01"
```
