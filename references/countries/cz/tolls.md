# Czech Republic — Road Tolls (MYTO)

**EU Baseline:** Not applicable — toll systems are national.

**Sources:**
- https://myto.gov.cz/en/ — MYTO: Czech electronic toll system
- https://myto.gov.cz/en/customer-services/toll-calculator — MYTO: Toll calculator

**Last verified: 2026-05-30**

---

## Overview

The Czech Republic operates the **MYTO** electronic toll system for heavy vehicles on motorways and selected first-class roads. As of January 2024, the threshold was lowered from >12t to **>3.5t** GVW. The system is GNSS-based and operated by CzechToll.

---

## Which Vehicles Must Pay

Vehicles with GVW **exceeding 3.5 tonnes** on:
- All **motorways (dálnice — D-roads)**
- All **expressways (rychlostní silnice — R-roads)**
- Selected **first-class roads (silnice I. třídy)**

---

## Rate Structure

Rates differentiated by:
- Vehicle weight category
- Euro emission class (CO₂-differentiated since July 2025, aligned with EU Eurovignette Directive)
- Road type (motorways vs first-class roads)

As of January 2024, new road sections were added expanding the network. Use the MYTO calculator for exact rates: https://myto.gov.cz/en/customer-services/toll-calculator

---

## Payment and Registration

**OBU (On-Board Unit):** GNSS-based device required for automated distance measurement.
- Register at MYTO portal: https://myto.gov.cz/en/
- Prepaid account (most common) or postpaid with collateral

**EETS:** Czech MYTO is compatible with EETS transponders from authorized service providers.

---

## Penalties

Non-payment or OBU fraud results in fines issued by INSID. Enforcement via fixed GNSS checkpoints and mobile units.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| MYTO | Czech toll system | https://myto.gov.cz/en/ |
| MYTO | Toll calculator | https://myto.gov.cz/en/customer-services/toll-calculator |

---

## Implementation Notes for Developers

```
CZ_MYTO_THRESHOLD_T = 3.5    # lowered from 12t in Jan 2024
CZ_OBU_REQUIRED = True
```
