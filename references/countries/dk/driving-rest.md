# Denmark — Driving and Rest Time

**EU Baseline:** [references/eu/driving-rest-time.md — EU Regulation 561/2006]

**Sources:**
- https://tachografservice.dk/en/toolbox/drive-and-rest-time/ — Tachografservice.dk: Drive and rest time rules
- https://tachografservice.dk/en/toolbox/exceptions-drive-and-rest-time/ — Tachografservice.dk: Exceptions

**Last verified: 2026-05-30**

---

## Overview

Denmark applies EU Regulation 561/2006 with a few notable national implementation specifics: stricter tachograph data download intervals, a de minimis threshold below which minor violations are not sanctioned, and a special ferry rest interruption rule. Enforcement is by the Danish Road Traffic Authority (Færdselsstyrelsen) and the police.

---

## Deviations from EU Baseline

| Topic | EU standard | Denmark |
|-------|------------|---------|
| Driver card download | Every 28 days | Every **21 calendar days** (stricter) |
| Vehicle unit download | Every 90 days | Every **60 calendar days** (stricter) |
| Data storage | 12 months | 12 months on **two independent servers/hard drives** |
| De minimis | Not defined in EU law | Violations **below 5%** of the limit are not sanctioned (unless >10 violations in 30 days) |
| Ferry/train rest | 2 interruptions, max 1h each | Regular daily rest may be interrupted twice for ferry/train, interruptions **not exceeding 1 hour combined** |

---

## Scope

Rules apply to:
- Goods vehicles exceeding **3,500 kg** permissible total weight
- Passenger vehicles designed to carry **more than 9 persons** including the driver

---

## Enforcement

| Authority | Role | Website |
|-----------|------|---------|
| Færdselsstyrelsen | Road Traffic Authority — tachograph checks, licencing | https://vejafgifter.dk/en/ |
| Rigspolitiet | Police — roadside checks | — |
| Tachografservice.dk | Authoritative guidance resource | https://tachografservice.dk/en/ |

---

## Penalties

Fines for driving/rest time violations are issued by the Police and the Danish Road Traffic Authority.

| Violation | Penalty |
|-----------|---------|
| KmToll non-payment (road toll) | **DKK 9,000** (from July 1, 2025) |
| Driving/rest time violations | Varies — see Tachografservice.dk penalty calculator |

Penalty calculator: https://tachografservice.dk/en/toolbox/boeder-og-sanktioner/

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Tachografservice.dk | Drive and rest time rules for Denmark | https://tachografservice.dk/en/toolbox/drive-and-rest-time/ |
| Tachografservice.dk | Exceptions to drive and rest time | https://tachografservice.dk/en/toolbox/exceptions-drive-and-rest-time/ |
| Tachografservice.dk | Fines and sanctions calculator | https://tachografservice.dk/en/toolbox/boeder-og-sanktioner/ |
| Færdselsstyrelsen | Road fees and weight portal | https://vejafgifter.dk/en/ |

---

## Implementation Notes for Developers

```
DK_DRIVER_CARD_DOWNLOAD_MAX_DAYS = 21   # stricter than EU 28 days
DK_VEHICLE_UNIT_DOWNLOAD_MAX_DAYS = 60  # stricter than EU 90 days
DK_DATA_STORAGE_COPIES = 2              # two independent servers required
DK_DEMINIMIS_THRESHOLD_PCT = 5          # violations <5% not sanctioned
DK_DEMINIMIS_MAX_VIOLATIONS_IN_30D = 10 # de minimis not applied if >10 violations
```
