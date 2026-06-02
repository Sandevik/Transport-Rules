# Australia — Work and Rest Requirements (Heavy Vehicle Fatigue Management)

**EU Baseline:** Not applicable — Tier 3 standalone. Governed by NHVR (National Heavy Vehicle Regulator) under the Heavy Vehicle National Law (HVNL). Fundamentally different framework based on accumulated fatigue risk, not simple daily driving limits.

**Sources:**
- https://www.nhvr.gov.au/safety-accreditation-compliance/fatigue-management/work-and-rest-requirements — NHVR: Work and rest requirements
- https://www.nhvr.gov.au/safety-accreditation-compliance/chain-of-responsibility — NHVR: Chain of Responsibility

**Last verified: 2026-05-30**

---

## Overview

Australia's heavy vehicle fatigue management is governed by the **NHVR** (National Heavy Vehicle Regulator) under the **Heavy Vehicle National Law (HVNL)**, applicable in Queensland, New South Wales, Victoria, South Australia, Tasmania, and the ACT. The system is unique in using **accumulated work/rest thresholds** across multiple time windows (5.5h, 8h, 11h, 24h, 7 days, 14 days) rather than a single daily driving limit.

Three options exist with increasing flexibility: **Standard Hours**, **Basic Fatigue Management (BFM)**, and **Advanced Fatigue Management (AFM)**.

---

## Standard Hours — Solo Driver

| Time window | Maximum work | Minimum rest |
|-------------|-------------|--------------|
| 5.5 hours | **5.25 hours** work | **15 continuous minutes** |
| 8 hours | **7.5 hours** work | **30 minutes** (15-min blocks) |
| 11 hours | **10 hours** work | **60 minutes** (15-min blocks) |
| **24 hours** | **12 hours** work | **7 continuous hours stationary** |
| **7 days** | **72 hours** work | **24 continuous hours stationary** |
| **14 days** | **144 hours** work | 2 night rest breaks on consecutive days |

---

## Standard Hours — Two-Up (Two Drivers)

| Time window | Maximum work | Minimum rest |
|-------------|-------------|--------------|
| **24 hours** | **12 hours** work | **5 continuous hours stationary** (or sleeper berth while moving) |
| 52 hours | — | **10 continuous hours stationary** |
| **7 days** | **60 hours** work | **24 continuous hours stationary** |
| **14 days** | **120 hours** work | 2 night rest breaks on consecutive days |

---

## Basic Fatigue Management (BFM)

Available to NHVR-accredited carriers. Allows greater flexibility:

**Solo driver (24h):** Max **14 hours** work, min **7 continuous hours stationary** rest.

---

## Advanced Fatigue Management (AFM)

Individually tailored work/rest plans based on fatigue risk management systems. Used by accredited carriers with demonstrated safety management capability.

---

## Chain of Responsibility (CoR)

A defining feature of Australian law: **all parties in the supply chain** (schedulers, consignors, consignees, loading managers) share legal responsibility for preventing fatigue-related offences. It is not sufficient to only hold the driver responsible.

Parties must take "all reasonable steps" to prevent fatigue breaches, including not imposing schedules that require drivers to exceed limits.

---

## Key Differences from EU/US

| Feature | EU 561/2006 | US FMCSA HOS | Australia HVNL |
|---------|------------|-------------|----------------|
| Daily drive limit | 9h (10h extended) | 11h | 12h (in 24h window) |
| Weekly limit | 56h | 60/70h | 72h (7-day) |
| Off-duty required | 11h daily | 10h consecutive | 7h continuous |
| Supply chain liability | Company obligations | Carrier only | **Full CoR — all parties** |
| Framework | EU Regulation (uniform) | FMCSA (federal) | State-based + NHVR (national) |

---

## Enforcement

| Authority | Role | Website |
|-----------|------|---------|
| NHVR | National Heavy Vehicle Regulator | https://www.nhvr.gov.au/ |
| State police | Roadside enforcement | varies by state |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| NHVR | Work and rest requirements | https://www.nhvr.gov.au/safety-accreditation-compliance/fatigue-management/work-and-rest-requirements |
| NHVR | Chain of Responsibility | https://www.nhvr.gov.au/safety-accreditation-compliance/chain-of-responsibility |
| HVNL | Heavy Vehicle National Law (Queensland as template) | https://www.legislation.qld.gov.au/ |

---

## Implementation Notes for Developers

```
AU_STANDARD_MAX_WORK_24H = 12          # hours in any 24-hour window
AU_STANDARD_MIN_REST_24H = 7           # continuous stationary hours
AU_STANDARD_MAX_WORK_7D = 72
AU_STANDARD_MIN_REST_7D = 24           # continuous stationary
AU_TWO_UP_MAX_WORK_24H = 12
AU_TWO_UP_MIN_REST_24H = 5             # continuous (stationary or sleeper berth)
AU_BFM_MAX_WORK_24H = 14
AU_CHAIN_OF_RESPONSIBILITY = True      # all supply chain parties liable
```
