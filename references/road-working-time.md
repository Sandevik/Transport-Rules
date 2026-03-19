# Vägarbetstid — Road Working Time

**Sources:**
- https://www.transportstyrelsen.se/sv/vagtrafik/yrkestrafik/vagarbetstid/
- SFS 2005:395 — Lag om arbetstid vid vissa vägtransporter: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2005395-om-arbetstid-vid-vissa-vagtransporter_sfs-2005-395/
- SFS 2005:399 — Associated ordinance
- EU Directive 2002/15/EG — Road transport working time

**Last verified: 2026-03-19**

---

## Scope — Who Is Covered

The Road Working Time Act (SFS 2005:395) applies to:

- **Mobile workers** (förare and other crew) employed by companies in EU member states conducting road transport subject to EU Regulation 561/2006 or AETR
- **Self-employed drivers** (egenföretagare) conducting such transport
- Overseen by **Transportstyrelsen** (Swedish Transport Agency)

**Definition of mobile worker (§1a):** "any worker who is part of the mobile workforce" and employed by transport companies.

**Definition of self-employed driver (§1b):** Person whose main activity involves road transport with proper licensing, who works independently, controls operations, earns based on profit, and maintains multiple client relationships.

The law applies to vehicles subject to EU 561/2006 (>3.5t and buses). Drivers of light vehicles (≤3.5t) are **not** covered by this law but may be covered by general working time legislation (Arbetstidslagen SFS 1982:673).

**Since 1 July 2019:** Self-employed operators are exempt from aggregate working time averages and night work restrictions (but not the record-keeping obligations).

---

## Definition of "Work"

Work encompasses the entire period from start to finish of the working day, including all of the following:

| Activity | Counted as work? |
|---------|-----------------|
| Driving | Yes |
| Loading and unloading | Yes |
| Assisting passengers | Yes |
| Vehicle cleaning and maintenance | Yes |
| Regulatory compliance documentation | Yes |
| Security oversight tasks | Yes |
| Waiting time driver cannot freely dispose of | Yes |
| Standby time at worksite (must remain ready) | Yes |
| Breaks (raster) | No |
| Daily rest (dygnsvila) | No |
| Leisure time | No |

Administrative time "not directly connected with the transport" may be excluded from working time calculation for self-employed drivers (§1b).

---

## Maximum Working Hours

| Rule | Limit | Legal basis |
|------|-------|-------------|
| Ordinary weekly working time | Maximum **40 hours/week** | §5 |
| Permissible overtime / additional hours | Up to **200 hours/year** | §7 |
| Average weekly hours (over 4-month calculation period) | Maximum **48 hours/week** | §12 |
| Absolute weekly ceiling | **60 hours** in any single week | §12 |

- The 48-hour average is calculated over a rolling or fixed 4-month period
- No individual week may ever exceed **60 hours** regardless of the averaging period
- Both employers and self-employed (before 2019 exemption) subject to these limits

**Multiple employers:** When workers serve multiple employers under this law, each employer shares the 48-hour weekly maximum. Employers must verify whether employees work for others and document this.

---

## Break Requirements (Raster under vägarbetstidslagen)

Breaks must be taken **before** continuing work after reaching the threshold (§18):

| Continuous working time | Minimum break |
|------------------------|---------------|
| Under 6 hours | No mandatory break |
| 6–9 hours | ≥ **30 minutes** |
| More than 9 hours | ≥ **45 minutes** |

**Split breaks:** Breaks may be divided into periods of **at least 15 minutes** each, taken at appropriate intervals during the shift.

**Interaction with EU 561/2006:** Driving breaks under EU 561/2006 (45 min after 4h30 driving) must also be observed. Where both sets of rules apply, the more restrictive applies in each situation.

---

## Night Work (Nattarbete)

**Definition of night period (§14):** Any part of the period **01:00–05:00**.

| Rule | Requirement | Legal basis |
|------|------------|-------------|
| Maximum night work | **10 hours** within any 24-hour period containing night work | §15 |
| Prerequisite | Must be preceded by an approved rest period per driving regulations | — |

**Collective agreement option:** The night period definition may be modified by central collective agreement to the period 00:00–07:00 instead.

---

## Overtime and Emergency Provisions

| Type | Limit | Legal basis |
|------|-------|-------------|
| General overtime | Maximum **200 hours/year** | §7 |
| Emergency overtime | Unlimited — unforeseeable natural disasters/emergencies | §8 |
| Additional exemption (no collective agreement) | Up to **150 additional hours/year** via Transportstyrelsen permit | §21 |

Emergency overtime requires:
- Notification to local worker organizations
- Transportstyrelsen approval after 2 days if continuing more than 2 days

---

## Calculation Period

- Standard calculation period: **4 months** (may be adjusted by collective agreement)
- Some collective agreements can extend the calculation period up to **6 months**
- Self-employed drivers (before 2019 exemption): same 4-month calculation period applies

---

## Record-Keeping Obligations (§20)

Both employers and self-employed must:
- **Register all working time** covered by the act
- Retain records for **at least 2 years**
- Records must cover ordinary hours, overtime, aggregate time, and break periods
- Records must be accessible to Transportstyrelsen inspectors and connected to tachograph data where applicable

---

## Advance Notice of Schedule Changes (§16)

Employers must inform workers of changes in ordinary working hour scheduling **at least 2 weeks in advance**, unless unexpected circumstances make this impossible.

---

## Enforcement and Penalties

| Violation | Consequence | Legal basis |
|-----------|------------|-------------|
| Employer violates working hour limits | Fines | §26 |
| Self-employed driver exceeds permitted hours | Fines | §26 |
| Unauthorized overtime per hour per worker | **1% of annual price base amount** per hour | §28 |
| Failure to maintain records | Fines | §26 |
| Failure to provide required breaks | Fines | §26 |
| Providing false information to Transport Board | Fines | §26a |
| Violation of Board directives with vite | Up to **1 year imprisonment** | §25 |

Police have authority to monitor maximum weekly working hours at roadside checks and report violations to Transportstyrelsen.

---

## Key Legal References

| Law | Content |
|-----|---------|
| SFS 2005:395 | Primary Swedish road transport working time law |
| SFS 2005:399 | Implementing regulations |
| EU Directive 2002/15/EG | Harmonizing road transport working time across EU |
| EU Regulation 561/2006 | Driving and rest times (separate from but related to working time) |

---

## Implementation Notes for Developers

```
ORDINARY_WEEKLY_HOURS = 40
OVERTIME_MAX_PER_YEAR_H = 200
EMERGENCY_OVERTIME_MAX_H = None  # unlimited for genuine emergencies
ADDITIONAL_OVERTIME_VIA_PERMIT_H = 150  # if no collective agreement
AVERAGE_WEEKLY_MAX_H = 48
CALCULATION_PERIOD_MONTHS = 4  # extendable to 6 by collective agreement
ABSOLUTE_WEEKLY_MAX_H = 60
BREAK_REQUIRED_AFTER_H = 6
BREAK_MIN_FOR_6_TO_9H = 30  # minutes
BREAK_MIN_FOR_OVER_9H = 45  # minutes
BREAK_SPLIT_MIN_PERIOD_MIN = 15
NIGHT_PERIOD_START = '01:00'
NIGHT_PERIOD_END = '05:00'
NIGHT_WORK_MAX_H_IN_24H = 10
RECORDS_RETENTION_YEARS = 2
OVERTIME_FINE_PER_HOUR = 0.01  # × annual price base amount
SELF_EMPLOYED_EXEMPT_FROM_AVERAGES_SINCE = '2019-07-01'
```
