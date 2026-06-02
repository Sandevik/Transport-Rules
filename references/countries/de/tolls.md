# Germany — Road Tolls (LKW-Maut)

**EU Baseline:** Not applicable — toll systems are purely national (EU Directive 2022/362/EU sets the framework but rates and systems are national).

**Sources:**
- https://www.balm.bund.de/EN/Topics/HGVTolls/hgvtolls.html — BALM: HGV Tolls overview
- https://www.toll-collect.de/en/ — Toll Collect: official toll collection system

**Last verified: 2026-06-01**

---

## Overview

Germany operates a distance-based HGV toll (LKW-Maut) on all federal motorways (Bundesautobahnen) and federal trunk roads (Bundesstraßen). Since December 1, 2023, the threshold was lowered from >7.5t to **>3.5t technically permissible maximum laden mass**. The system is administered by BALM and operated by Toll Collect GmbH.

---

## Which Vehicles Must Pay

- Motor vehicles and combinations with technically permissible maximum laden mass (F.1 on registration certificate) **exceeding 3.5 tonnes** used for goods transport
- Applies to foreign vehicles using the German road network
- Applies whether laden or unladen

---

## Roads Covered

- All **federal motorways** (Bundesautobahnen — A-roads)
- All **federal trunk roads** (Bundesstraßen — B-roads)
- Exception: short border sections of A6 (French/Swiss border to Saarbrücken/Müllheim) and some private-sector toll roads

---

## Rate Structure (effective July 1, 2024 to December 31, 2025)

Rates are distance-based and composed of four components (all rolled into a single per-km charge): infrastructure costs, air pollution, noise pollution, and CO₂ emissions.

Source: Official BALM rate table (BGBl. I Nr. 315, 24.11.2023) — all figures in **EUR/km**.

### CO₂ class EK 1 (all emission standards)

| Euro class | >3.5–7.5t | 7.5–12t | 12–18t | >18t ≤3 axles | >18t 4 axles | >18t 5+ axles |
|------------|-----------|---------|--------|---------------|--------------|----------------|
| Euro VI    | 0.151     | 0.177   | 0.238  | 0.303         | 0.324        | **0.348**      |
| Euro V/EEV | 0.189     | 0.205   | 0.275  | 0.353         | 0.363        | 0.389          |
| Euro IV     | 0.201     | 0.221   | 0.286  | 0.371         | 0.388        | 0.414          |
| Euro III    | 0.225     | 0.250   | 0.328  | 0.429         | 0.454        | 0.478          |
| Euro II     | 0.244     | 0.275   | 0.348  | 0.459         | 0.487        | 0.511          |
| Euro I/0    | 0.248     | 0.276   | 0.350  | 0.484         | 0.512        | 0.516          |

### CO₂ classes EK 2–4 (Euro VI only — progressively better CO₂ performance)

| CO₂ class | >3.5–7.5t | 7.5–12t | 12–18t | >18t ≤3 axles | >18t 4 axles | >18t 5+ axles |
|-----------|-----------|---------|--------|---------------|--------------|----------------|
| EK 2      | 0.147     | 0.173   | 0.234  | 0.297         | 0.318        | 0.340          |
| EK 3      | 0.144     | 0.169   | 0.228  | 0.290         | 0.310        | 0.332          |
| EK 4      | 0.114     | 0.137   | 0.188  | 0.242         | 0.258        | **0.269**      |

**EK 5 (zero-emission vehicles):** Fully **exempt** from LKW-Maut until 31 December 2025.

**Typical reference:** A 5-axle articulated HGV >18t with Euro VI (CO₂ class EK1) pays **€0.348/km**. The same truck with best CO₂ class (EK4) pays **€0.269/km**.

For current 2026+ rates: https://www.balm.bund.de/EN/Topics/HGVTolls/hgvtolls.html

---

## Payment Methods

**On-Board Unit (OBU):** Primary method. The Toll Collect OBU automatically records journeys via GPS and DSRC. Must be activated before entering tolled roads.

**Manual booking (Einbuchung):** Via Toll Collect website, app, or service terminals before journey. Must include route, date, and vehicle data. Less convenient, used when OBU unavailable.

**Toll Collect App:** Mobile booking for pre-planned routes.

**Service terminals:** Available at petrol stations and BALM service points across Germany.

---

## Registration

Foreign operators must register with Toll Collect:
- Online at https://www.toll-collect.de/en/
- Receive OBU or set up manual booking account
- Provide vehicle registration data, emission class certificate (Euro class), and payment method

---

## Enforcement

BALM operates the **Roadside Inspection Service** and **Toll Enforcement** division. Toll gantries (Kontrollbrücken) on motorways and spot checks at weighbridges verify OBU compliance. Violations result in fines and potential vehicle immobilisation.

**Advance payment:** Foreign carriers may be required to pay a security deposit (Sicherheitsleistung) on the spot before being allowed to continue.

---

## Penalties

| Violation | Penalty |
|-----------|---------|
| Using tolled roads without valid OBU/booking | Fine + substitute toll charge |
| OBU not correctly mounted/activated | Fine |
| Providing incorrect vehicle data (emission class) | Fine |

Full fine schedule: https://www.balm.bund.de/EN/Service/QuickService/CatalogueOfFines/catalogueoffines_node.html

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| BALM | HGV Toll overview and enforcement | https://www.balm.bund.de/EN/Topics/HGVTolls/hgvtolls.html |
| Toll Collect | Toll payment system, rates, OBU | https://www.toll-collect.de/en/ |
| BFStrMG | Bundesfernstraßenmautgesetz — legal basis | https://www.gesetze-im-internet.de/bfstrmg/ |

---

## Implementation Notes for Developers

```
DE_MAUT_THRESHOLD_T = 3.5          # TPMLM in tonnes (since Dec 1, 2023)
DE_MAUT_APPLIES_TO = ["Bundesautobahnen", "Bundesstraßen"]
DE_MAUT_ZEV_EXEMPT_UNTIL = "2025-12-31"   # EK5 fully exempt through end of 2025
# Reference rates (EUR/km), effective 01.07.2024–31.12.2025, 5-axle artic >18t:
DE_MAUT_RATE_5AX_EK1_EUROVI  = 0.348   # Euro VI, CO2 class EK1
DE_MAUT_RATE_5AX_EK4_EUROVI  = 0.269   # Euro VI, best CO2 class EK4
DE_MAUT_RATE_5AX_EK1_EUROIII = 0.478   # Euro III, CO2 class EK1
DE_MAUT_RATE_5AX_EK1_EURO0   = 0.516   # Euro I/0, CO2 class EK1
```
