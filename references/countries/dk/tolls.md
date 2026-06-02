# Denmark — Road Tolls (KmToll)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://vejafgifter.dk/en/ — Færdselsstyrelsen: Road fees portal

**Last verified: 2026-05-30**

---

## Overview

Denmark introduced a distance-based **KmToll** (kilometre charge) for heavy vehicles in 2025. The system is being phased in: it currently covers trucks ≥12 tonnes and will expand to all trucks >3.5t from January 1, 2027. Rates are CO₂-differentiated.

---

## Current Scope (from January 1, 2025)

| Vehicle weight | Required to pay | From |
|---------------|----------------|------|
| **≥12 tonnes** | **YES** | January 1, 2025 |
| >3.5t to <12t | NO (not yet) | From **January 1, 2027** |

---

## Roads Covered

Currently covers the main part of the **state road network** plus parts of the municipal road network — approximately **10,900 km** total.

Planned expansion: entire Danish public road network by **January 1, 2028**.

---

## Rate Structure

Rates depend on:
- Distance driven (per km)
- CO₂ emissions class of the vehicle

Specific rates available at: https://vejafgifter.dk/en/

---

## Payment

Digital payment via the KmToll portal. The system uses GNSS-based on-board equipment (OBE) to track distance.

---

## Enforcement and Penalties

| Violation | Fine |
|-----------|------|
| KmToll non-payment | **DKK 9,000** (from July 1, 2025) |

As of July 1, 2025, enforcement authorities can **stop foreign trucks** with unpaid KmToll convictions at designated checkpoints.

---

## Other Danish Tolls

Denmark has no general motorway vignette for trucks. The only other tolls are:
- **Øresund Bridge** (SE↔DK): approx. DKK 400–1,000+ per crossing for HGVs depending on vehicle height
- **Great Belt Bridge** (connecting Funen and Zealand): approx. DKK 500–900+ for HGVs

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Færdselsstyrelsen | KmToll portal and rates | https://vejafgifter.dk/en/ |

---

## Implementation Notes for Developers

```
DK_KMTOLL_THRESHOLD_T_2025 = 12.0   # current threshold (≥12t)
DK_KMTOLL_THRESHOLD_T_2027 = 3.5    # expanding from Jan 1, 2027
DK_KMTOLL_FINE_DKK = 9000           # from July 1, 2025
```
