# EU — Driving and Rest Time Rules

**EU Baseline:** This IS the EU baseline file. References: EU Regulation 561/2006, EU Regulation 2020/1054 (Mobility Package).

**Sources:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006R0561 — EU Regulation 561/2006 (full text)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1054 — EU Regulation 2020/1054 (Mobility Package amendments)
- https://transport.ec.europa.eu/transport-modes/road/social-provisions/driving-time-and-rest-periods_en — EC DG MOVE summary

**Last verified: 2026-03-19**

---

## Scope — Who Must Follow These Rules

EU Regulation 561/2006 applies to:
- Vehicles (including trailers/semi-trailers) with combined total weight exceeding **3.5 tonnes**
- All **buses** regardless of weight
- From **1 July 2026**: international goods transport with vehicles weighing **2.5–3.5 tonnes** (Mobility Package)

Light vehicles (≤3.5 tonnes) used in domestic transport are subject to national rules. See each country's `light-vehicles.md` or equivalent.

**AETR note:** For journeys passing through non-EU/EEA countries that have signed AETR, AETR rules apply for the entire journey. AETR rules are substantially identical to EU 561/2006. See `references/aetr/driving-rest-time.md`.

---

## Daily Driving Time — Article 6

| Rule | Limit |
|------|-------|
| Normal daily driving | **9 hours** |
| Extended daily driving (max 2×/week) | **10 hours** |

- Applies within any 24-hour period starting from the end of the last weekly rest.
- Extension to 10 hours is allowed at most **twice per calendar week** (Mon–Sun).

---

## Weekly Driving Time — Article 6

| Rule | Limit |
|------|-------|
| Maximum per week | **56 hours** |
| Maximum over any 2 consecutive weeks | **90 hours** |

---

## Breaks — Article 7

After **4 hours 30 minutes** of driving, a mandatory break must be taken **before** continuing:

| Option | Details |
|--------|---------|
| Single break | At least **45 minutes** |
| Split break | First: ≥ **15 minutes** + Second: ≥ **30 minutes** (in that order only) |

- Breaks may not be spent on other work.
- The second part of a split break must be at least 30 minutes; reversed order (30+15) is NOT valid.

---

## Daily Rest — Article 8

| Type | Requirement |
|------|-------------|
| Regular daily rest | **11 consecutive hours** within each 24-hour period |
| Reduced daily rest | **9 consecutive hours** (allowed max **3 times** between weekly rests) — no compensation required |
| Split daily rest | First period: ≥ 3 hours + Second period: ≥ 9 hours = **minimum 12 hours total** |

- The 24-hour period starts from the end of the previous daily or weekly rest.

---

## Weekly Rest — Articles 8 & 9

| Type | Requirement |
|------|-------------|
| Normal weekly rest | **45 consecutive hours** |
| Reduced weekly rest | Minimum **24 consecutive hours** |
| Over 2 consecutive weeks | Must include at least **one normal (45h) weekly rest** |

**Compensation for reduced weekly rest:**
- The shortfall (45h minus actual rest taken) must be compensated by attaching it to a rest period of ≥9h
- Must be compensated **within 3 weeks** of the reduced rest week
- Compensation rest may NOT be taken in the vehicle cab (Mobility Package 2022 rule)

**Cab prohibition (from 21 February 2022):** Drivers may NOT take regular weekly rest (≥45h) in the vehicle cab. Employers must provide suitable accommodation at own cost. Reduced weekly rest (24h) may be taken in the cab.

**Return home requirement (Mobility Package):** Companies must plan routes enabling drivers to return home or to the company's operational centre at least **every four weeks**.

---

## Multi-Crew Operations

When two drivers share a vehicle:
- Each driver is entitled to a daily rest period within any **30-hour period** (not 24h)
- First driver may drive for maximum **1 hour** before the second driver joins
- Minimum 9 hours rest required for each within the 30-hour period

---

## Exceptional Circumstances — Article 12

In exceptional circumstances (emergencies, unforeseen events), a driver may extend daily or weekly driving time:
- By **up to 1 hour** to reach the employer's operational centre or driver's home for weekly rest
- By **up to 2 hours** (after a 30-minute break) to reach centre/home for **regular weekly rest** only
- Driver must note the reason on the tachograph or an attached sheet
- Applicable only when road safety is not compromised

---

## If You Accidentally Exceed Limits

**This section covers accidental overdriving — not deliberate manipulation (which is a criminal offence, see `eu/smart-tachograph.md`).**

### Step 1 — Stop and rest (immediate priority)

The moment you realise a limit has been exceeded, stop driving at the first safe and legal opportunity and take the required rest. Continuing to drive after recognising the violation turns a single infringement into a continuing and more serious one.

| Situation | Minimum action |
|-----------|---------------|
| Break violation (drove >4h30m without a break) | Take the required break (45 min, or 30 min if 15 min was already taken) before continuing |
| Daily driving exceeded (>9h or >10h) | Do not drive again until the required daily rest is completed (min 9 or 11 hours) |
| Weekly driving limit approaching or exceeded | Do not begin a new daily shift; take a regular weekly rest (45h) before resuming |

### Step 2 — Record the reason

If the exceedance was caused by an unforeseen emergency (traffic accident, road closure, medical situation), annotate the tachograph — either using the manual input function or by attaching a signed written statement. This records the exceptional circumstance under **Article 12** and is considered during enforcement assessment.

If there was no genuine emergency, do not fabricate a reason — incorrect entries are a separate infringement.

### Step 3 — What happens at a roadside check

EU enforcement officers classify violations under a standard four-tier system (Regulation 2020/1054):

| Category | Driving time threshold example | Consequence at roadside |
|----------|-------------------------------|------------------------|
| **Minor Infringement (MI)** | Exceeded daily limit by ≤1 hour | Warning or small local fine; no immobilisation |
| **Serious Infringement (SI)** | Exceeded daily limit by 1–2 hours | Fine; ERRU entry; possible immobilisation until rest taken |
| **Very Serious Infringement (VSI)** | Exceeded daily limit by 2–3 hours; missing driver card | Higher fine; mandatory immobilisation; operator notified |
| **Most Serious Infringement (MSI)** | Exceeded daily limit by >3 hours; no tachograph | Criminal referral possible; immediate prohibition from driving; ERRU impact |

**Vehicle immobilisation:** Officers may immobilise the vehicle until sufficient rest has been taken. Once rest is complete, the journey may resume. Immobilisation solely for non-payment of a fine is **not** permitted under EU rules.

**Country-specific fines:** Fine amounts are set by each member state in its own currency. See the relevant country file for amounts (e.g. `references/countries/de/penalties.md`, `references/countries/fr/penalties.md`).

### Step 4 — Company obligations

The transport company (not just the driver) is legally responsible for scheduling compliance under EU 561/2006 Art. 10. When a violation is discovered:
- Review tachograph data for the relevant driver and period
- Correct the schedule to prevent recurrence
- If enforcement identifies a systemic pattern, the company risk rating in ERRU is upgraded, leading to more frequent checks EU-wide
- The company's operator licence (standard authorisation) may be reviewed if violations are repeated

### Article 12 Emergency Checklist

If you used the Article 12 extension, confirm all three conditions were met:
- [ ] The reason was genuinely unforeseeable (not a scheduling error)
- [ ] Road safety was not compromised
- [ ] The reason was noted on or with the tachograph immediately

Article 12 is a **narrow exception** — enforcement officers are trained to distinguish genuine emergencies from routine scheduling failures.

---

## Coach/Bus Special Rules (Occasional International Passenger Services)

Drivers of coaches on single occasional international passenger services may:
- Postpone weekly rest for **up to 12 days** (instead of the normal 6-day cycle)
- Required compensation: deferred rest must be taken immediately after the 12-day period
- Special break rules: breaks may be split into 15-minute increments

---

## Smart Tachograph Retrofit Deadlines (Mobility Package)

| Vehicle type | Deadline |
|---|---|
| New heavy vehicles (>3.5t) | **21 August 2023** (must have Smart v2) |
| Existing vehicles with analogue/digital tacho | Retrofit to Smart v2 by **31 December 2024** |
| Existing vehicles with Smart v1 | Upgrade to v2 by **18 August 2025** |
| Light vehicles (2.5–3.5t) international | Smart v2 required by **1 July 2026** |

**Lookback period at roadside checks:** 56 days (changed from 28 days effective 31 December 2024)

---

## Implementation Notes for Developers

```
DAILY_DRIVING_NORMAL_H = 9
DAILY_DRIVING_EXTENDED_H = 10
DAILY_DRIVING_EXTENDED_MAX_TIMES_PER_WEEK = 2
WEEKLY_DRIVING_MAX_H = 56
BIWEEKLY_DRIVING_MAX_H = 90
BREAK_REQUIRED_AFTER_H = 4.5
BREAK_MIN_SINGLE_MIN = 45
BREAK_SPLIT_FIRST_MIN = 15
BREAK_SPLIT_SECOND_MIN = 30
DAILY_REST_NORMAL_H = 11
DAILY_REST_REDUCED_H = 9
DAILY_REST_REDUCED_MAX_TIMES_BETWEEN_WEEKLY = 3
DAILY_REST_SPLIT_FIRST_MIN_H = 3
DAILY_REST_SPLIT_SECOND_MIN_H = 9
WEEKLY_REST_NORMAL_H = 45
WEEKLY_REST_REDUCED_H = 24
WEEKLY_REST_COMPENSATION_WITHIN_WEEKS = 3
TACHOGRAPH_LOOKBACK_DAYS = 56
MULTI_CREW_REST_PERIOD_H = 30
MULTI_CREW_DAILY_REST_H = 9
```

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| EU Regulation 561/2006 | Core rules — Art. 6, 7, 8, 9, 12 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006R0561 |
| EU Regulation 165/2014 | Tachograph requirements | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0165 |
| Mobility Package 2020/1054 | Updates effective 21 Feb 2022 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1054 |
| EC DG MOVE summary | Plain-language guide | https://transport.ec.europa.eu/transport-modes/road/social-provisions/driving-time-and-rest-periods_en |

---

*See also: references/aetr/driving-rest-time.md (AETR framework for non-EU journeys), references/eu/smart-tachograph.md (full tachograph spec)*
