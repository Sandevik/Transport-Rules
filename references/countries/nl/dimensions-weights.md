# Netherlands — Vehicle Dimensions and Weights (LZV)

**EU Baseline:** [references/eu/weights-dimensions.md — Directive 96/53/EC] with national LZV exception.

**Sources:**
- https://www.government.nl/topics/freight-transportation/requiremenst-for-lorries — Government.nl: Requirements for lorries
- https://www.rdw.nl/ — RDW: Vehicle authority

**Last verified: 2026-05-30**

---

## Overview

The Netherlands permits **LZV (Langere en Zwaardere Vrachtautocombinaties — Longer and Heavier Vehicle Combinations)** under a national dispensation scheme. LZVs allow combinations up to **25.25 metres long and 60 tonnes GVW** on a designated road network, making the Netherlands one of the most permissive countries for long vehicles alongside the Nordic states.

---

## Standard EU Limits (International Transport)

For international transport, Directive 96/53/EC limits apply — see `references/eu/weights-dimensions.md`.

---

## Dutch LZV (Longer and Heavier Combinations)

| Parameter | LZV limit | EU 96/53/EC (international) |
|-----------|-----------|---------------------------|
| Maximum length | **25.25 metres** | 18.75m (road train) |
| Maximum GVW | **60 tonnes** | 40t general / 44t combined transport |
| Permitted on | **Designated LZV road network** only | All roads |

**LZV operation requires:**
- Vehicle combination must meet specific technical requirements (coupling, axle spacing, braking)
- Operation limited to the designated LZV network
- Drivers must have appropriate competence

**LZV network:** Extensive national network covering major freight corridors. Managed by RDW and the Ministry of Infrastructure.

---

## Standard Dutch Limits (Non-LZV)

| Parameter | Netherlands | EU 96/53/EC |
|-----------|-----------|-------------|
| Maximum GVW (5-axle artic) | 50t | 40t |
| Axle load (single drive) | 11.5t | 11.5t |
| Width | 2.55m / 2.60m reefer | 2.55m |
| Height | 4.0m | 4.0m |

*Note: Dutch domestic limits for standard combinations may vary from EU minimums — always check RDW for current rules.*

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Government.nl | Requirements for lorries in the Netherlands | https://www.government.nl/topics/freight-transportation/requiremenst-for-lorries |
| RDW | Vehicle registration authority and LZV approval | https://www.rdw.nl/ |

---

## Implementation Notes for Developers

```
NL_LZV_MAX_LENGTH_M = 25.25
NL_LZV_MAX_GVW_T = 60
NL_LZV_DESIGNATED_NETWORK_ONLY = True
NL_INTERNATIONAL_USES_EU_LIMITS = True  # EU 96/53/EC for cross-border
```
