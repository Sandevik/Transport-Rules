# Finland — Vehicle Dimensions and Weights

**EU Baseline:** [references/eu/weights-dimensions.md — Directive 96/53/EC] with Nordic exception deviations.

**Sources:**
- https://www.traficom.fi/sites/default/files/media/file/76%20t%2034,5%20m%20in%20Finland.pdf — Traficom: 76 tonne 34.5m vehicles in Finland (PDF)
- https://www.traficom.fi/en/transport/road/road-traffic-act2020 — Traficom: Road Traffic Act 2020

**Last verified: 2026-05-30**

---

## Overview

Finland applies the EU Directive 96/53/EC for international transport but uses the Nordic exception (Art. 4a) domestically to permit very heavy and long combinations. Finnish domestic limits are among the highest in Europe: **76 tonnes GVW** and **34.5 metres** for modular combinations. These limits are comparable to Sweden's (74t/34.5m) but slightly higher on maximum weight.

---

## Finnish Domestic Limits (Standard Roads)

| Parameter | Finnish standard | EU Directive 96/53/EC |
|-----------|----------------|----------------------|
| Maximum GVW (domestic, 9+ axles) | **76 tonnes** | 40–44t |
| Maximum vehicle length (modular) | **34.5 metres** | 18.75m (road train) |
| Maximum width | 2.60m (standard) / 3.0m (forestry) | 2.55m |
| Maximum height | 4.4m | 4.0m |

---

## International Transport

For international transport (crossing into/from another EU member state), **EU Directive 96/53/EC limits apply**. The Finnish 76t/34.5m limits are not valid in other EU member states.

---

## Deviations from EU Baseline

| Topic | EU standard | Finland |
|-------|------------|---------|
| Maximum GVW | 44t (combined transport), 40t general | **76t** (domestic, Nordic exception) |
| Maximum vehicle length | 18.75m | **34.5m** (modular combinations) |
| Height | 4.0m | **4.4m** |

---

## Requirements for 34.5m / 76t Operations

Vehicles operating at Finnish maximum limits must comply with technical requirements set by Traficom including:
- Approved vehicle combination types
- Electronic braking systems (EBS)
- Air suspension or equivalent
- Specific coupling approvals

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Traficom | 76t 34.5m vehicles in Finland (PDF) | https://www.traficom.fi/sites/default/files/media/file/76%20t%2034,5%20m%20in%20Finland.pdf |
| Traficom | Road Traffic Act 2020 | https://www.traficom.fi/en/transport/road/road-traffic-act2020 |

---

## Implementation Notes for Developers

```
FI_MAX_GVW_DOMESTIC_T = 76      # Nordic exception; international = EU 96/53/EC limits
FI_MAX_LENGTH_DOMESTIC_M = 34.5
FI_MAX_HEIGHT_M = 4.4
FI_INTERNATIONAL_USES_EU_LIMITS = True
```
