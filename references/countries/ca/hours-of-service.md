# Canada — Hours of Service (HOS)

**EU Baseline:** Not applicable — Tier 3 standalone. Governed by Transport Canada under SOR/2005-313. Different from both EU 561/2006 and US FMCSA rules.

**Sources:**
- https://tc.canada.ca/en/road-transportation/motor-vehicle-safety/commercial-driver-hours-service-regulations — Transport Canada: HOS Regulations
- https://laws-lois.justice.gc.ca/eng/regulations/SOR-2005-313/fulltext.html — Justice Laws: SOR/2005-313 (full text)

**Last verified: 2026-05-30**

---

## Overview

Canada's **Hours of Service Regulations (SOR/2005-313)** govern driving time for commercial motor vehicle (CMV) drivers. Federal rules apply to interprovincial and international operations; provinces may add stricter rules for intraprovincial operations. The framework is broadly similar to (but distinct from) the US FMCSA HOS rules. Canada adopted **ELD (Electronic Logging Device)** requirements in 2023.

---

## Scope

Applies to drivers of CMVs:
- Vehicles with GVW or GVWR ≥ **4,500 kg** in federal/international operations
- Provincial thresholds may vary

---

## Core HOS Limits

| Rule | Limit |
|------|-------|
| **Driving limit** | Max **13 hours** driving after 8+ consecutive hours off-duty |
| **On-duty cycle** | May not drive after **14 consecutive hours** on duty |
| **Off-duty minimum** | **8 consecutive hours** off duty required before new driving period |
| **Cycle 1 (South of 60°)** | Max **70 hours on-duty** in any 7 consecutive days |
| **Cycle 2 (South of 60°)** | Max **120 hours on-duty** in any 14 consecutive days + mandatory 24h off after 70h in 7 days |
| **North of 60° latitude** | Modified rules apply — higher limits for remote operations |

**Daily off-duty reset:** 10 consecutive hours off-duty resets the daily driving period.

---

## Sleeper Berth

Drivers with a sleeper berth may split the 10-hour off-duty requirement:
- One period ≥ 8 hours in sleeper berth
- One period ≥ 2 hours off-duty (either in or out of berth)
- Combined total ≥ 10 hours

---

## Short-Term (2-Driver) Exception

With two qualified drivers sharing a vehicle:
- Each may drive up to 10 hours in any 24-hour period
- Combined driving not to exceed 20 hours in 24 hours

---

## ELD (Electronic Logging Device)

Canada's ELD mandate came into effect **June 12, 2021** (full enforcement from January 1, 2023). Applies to:
- CMVs subject to HOS regulations
- Operating in federal jurisdiction

Exemptions: Short-haul, vehicles manufactured before 2000, certain agriculture.

---

## Enforcement

| Authority | Role | Website |
|-----------|------|---------|
| Transport Canada | Federal regulations and policy | https://tc.canada.ca/ |
| CVSA (Canada) | Roadside inspection standards (same as US CVSA) | https://cvsa.org/ |
| Provincial police (OPP, SQ, RCMP, etc.) | Roadside enforcement | varies |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Transport Canada | HOS Regulations overview | https://tc.canada.ca/en/road-transportation/motor-vehicle-safety/commercial-driver-hours-service-regulations |
| Justice Laws | SOR/2005-313 full text | https://laws-lois.justice.gc.ca/eng/regulations/SOR-2005-313/fulltext.html |

---

## Implementation Notes for Developers

```
CA_HOS_DRIVING_MAX_H = 13            # after 8h consecutive off-duty
CA_HOS_ONDUTY_WINDOW_H = 14         # consecutive daily limit
CA_HOS_OFFDUTY_MIN_H = 8            # consecutive (daily reset)
CA_HOS_OFFDUTY_RESET_H = 10         # 10h resets daily driving period
CA_CYCLE1_MAX_70H_IN_7D = 70
CA_CYCLE2_MAX_120H_IN_14D = 120
CA_ELD_MANDATORY = True             # since Jan 2023
CA_CMV_THRESHOLD_KG = 4500
```
