# United States — Hours of Service (HOS)

**EU Baseline:** Not applicable — Tier 3 standalone. Governed by FMCSA (Federal Motor Carrier Safety Administration), 49 CFR Part 395. Completely different framework from EU 561/2006 or AETR.

**Sources:**
- https://www.fmcsa.dot.gov/regulations/hours-of-service — FMCSA: Hours of Service regulations
- https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395 — eCFR: 49 CFR Part 395 (full text)

**Last verified: 2026-05-30**

---

## Overview

The US **Hours of Service (HOS)** rules govern driving time for commercial motor vehicle (CMV) drivers operating in interstate commerce. The rules are administered by the **FMCSA** (Federal Motor Carrier Safety Administration) under the Department of Transportation (USDOT). HOS is fundamentally different from EU 561/2006 — it uses a rolling 14-hour on-duty window rather than a fixed 24-hour period, and weekly limits are based on duty cycles of 7 or 8 consecutive days.

---

## Scope — Which Vehicles / Drivers

HOS applies to **Commercial Motor Vehicles (CMVs)** in interstate commerce:
- Vehicles with GVW or GVWR ≥ **26,001 lbs** (~11.8t)
- Vehicles transporting hazardous materials in quantities requiring placarding
- Vehicles designed to transport ≥ 16 passengers (including driver)

**CDL requirement:** Drivers of CMVs ≥26,001 lbs must hold a **Commercial Driver's License (CDL)**.

---

## Property-Carrying CMV Drivers (49 CFR §395.3)

| Rule | Limit |
|------|-------|
| **11-Hour Driving Limit** | May drive max **11 hours** after 10 consecutive hours off duty |
| **14-Hour On-Duty Window** | May not drive beyond the **14th hour** after coming on duty — even if the full 11h of driving hasn't been used |
| **10-Hour Off-Duty Minimum** | Must take **10 consecutive hours** off duty before next driving period |
| **60/70-Hour Weekly Limit** | May not drive after 60h on-duty in 7 consecutive days OR 70h in 8 consecutive days |
| **34-Hour Restart** | May restart the 7/8-day cycle with ≥34 consecutive hours off duty |
| **30-Minute Break** | If 8 hours have passed since the last off-duty or sleeper berth period of ≥30 min: must take a 30-min break before driving |

---

## Sleeper Berth Provision

Drivers using a sleeper berth may split the 10-hour off-duty requirement:

| Split | Rule |
|-------|------|
| Option 1: 7h/3h | **≥7 hours** in sleeper berth + **≥3 hours** off duty (either order) |
| Option 2: 8h/2h | **≥8 hours** in sleeper berth + **≥2 hours** off duty (either order) |

Neither period alone counts as the required off-duty rest — they must be paired.

---

## Short-Haul Exemption (§395.1(e))

A driver is exempt from the ELD requirement and driving window rules if:
- Operates within a **100 air-mile** radius of normal work reporting location
- Returns to normal work location within **14 consecutive hours**
- Not required to use a CDL: **150 air-mile** radius exemption available

---

## Adverse Driving Conditions (§395.1(b))

If a driver encounters unexpected adverse conditions (snow, ice, fog, accident), may extend:
- **Driving time by 2 hours** (to 13h)
- **On-duty window by 2 hours** (to 16h)

---

## Passenger-Carrying CMV Drivers (§395.5)

| Rule | Limit |
|------|-------|
| Driving limit | **10 hours** |
| On-duty window | **15 hours** |
| Off-duty minimum | **8 consecutive hours** |
| Weekly limit | **60h/7 days or 70h/8 days** |

---

## ELD (Electronic Logging Device)

**Mandatory** for most CMV drivers since December 2017 (49 CFR Part 395, Subpart B). Replaces paper logbooks for drivers required to keep Records of Duty Status (RODS).

**ELD exemptions:**
- Short-haul drivers (100/150 air-mile exemption)
- Drivers operating under oil field exemption
- Vehicles manufactured before model year 2000
- Driveaway-towaway operations (vehicle being delivered as the cargo)

---

## Enforcement

| Authority | Role | Website |
|-----------|------|---------|
| FMCSA | Federal enforcement — carrier safety ratings, compliance reviews | https://www.fmcsa.dot.gov/ |
| State Police / DOT | Roadside inspections at weigh stations and checkpoints | — |
| CVSA | Commercial Vehicle Safety Alliance — standardized roadside inspection procedures | https://cvsa.org/ |

**No advance payment system** — violations result in out-of-service orders and civil penalties billed later.

---

## Penalties

| Violation | Civil penalty |
|-----------|--------------|
| HOS violations (driver) | Up to **$16,000 per violation** |
| HOS violations (carrier) | Up to **$16,000 per violation** |
| ELD non-compliance | Up to **$16,000 per violation** |
| Falsification of records | Criminal prosecution possible |

FMCSA penalty schedule: https://www.fmcsa.dot.gov/regulations/penalties

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| FMCSA | HOS regulations and guidance | https://www.fmcsa.dot.gov/regulations/hours-of-service |
| eCFR | 49 CFR Part 395 — full text | https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395 |
| FMCSA | Civil penalties | https://www.fmcsa.dot.gov/regulations/penalties |

---

## Implementation Notes for Developers

```
US_HOS_DRIVING_MAX_H = 11             # property-carrying
US_HOS_ONDUTY_WINDOW_H = 14          # hard 14h cutoff
US_HOS_OFFDUTY_MIN_H = 10            # consecutive
US_HOS_WEEKLY_LIMIT_60H_IN_7D = 60
US_HOS_WEEKLY_LIMIT_70H_IN_8D = 70
US_HOS_RESTART_HOURS = 34            # consecutive off-duty for cycle reset
US_HOS_BREAK_TRIGGER_H = 8           # 30-min break if 8h since last 30-min off
US_SHORT_HAUL_RADIUS_MILES = 100     # CDL drivers
US_SHORT_HAUL_RADIUS_MILES_NON_CDL = 150
US_ADVERSE_DRIVING_EXTENSION_H = 2
US_ELD_MANDATORY = True              # since Dec 2017
US_CMV_GVW_THRESHOLD_LBS = 26001
```
