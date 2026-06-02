# Germany — Road Transport Working Time

**EU Baseline:** references/eu/working-time.md — Directive 2002/15/EC. National deviations apply.

**Last verified: 2026-06-02**

**Sources:**
- https://www.gesetze-im-internet.de/arbzg/ — ArbZG (Arbeitszeitgesetz) full text
- https://www.gesetze-im-internet.de/fahrpersv/ — Fahrpersonalverordnung (FahrpersonalV)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0015 — Directive 2002/15/EC
- https://www.balm.bund.de/EN/Topics/Controls/ — BALM enforcement
- https://www.baua.de/DE/Themen/Arbeitsgestaltung-im-Betrieb/Arbeitszeit/ — BAuA working time guidance

---

## Overview

Germany implements Directive 2002/15/EC (road transport working time) through two primary instruments:

1. **ArbZG — Arbeitszeitgesetz** (Working Hours Act, BGBl I 1994 p. 1170) — the general working time law covering all employees
2. **FahrpersonalV — Fahrpersonalverordnung** (Driving Personnel Regulation, BGBl I 1987 p. 1442, as amended) — the specific regulation for professional drivers implementing both EU 561/2006 and Directive 2002/15/EC in German law

The two instruments interact: ArbZG sets general rules; FahrpersonalV implements the EU-specific mobile worker provisions and prevails where it covers the same ground.

---

## Maximum Working Hours

| Rule | Limit | Legal basis |
|------|-------|-------------|
| Average weekly working time | **48 hours/week** | ArbZG §3; Directive 2002/15/EC Art. 4 |
| Absolute weekly ceiling | **60 hours** | ArbZG §3 + Directive 2002/15/EC Art. 4 |
| Calculation (reference) period | **16 weeks** (extendable to 26 weeks by collective agreement) | ArbZG §7(1); Directive 2002/15/EC Art. 4 (4 months, extended by German law) |
| Maximum daily working time | **10 hours** (standard); 12 hours possible with works council agreement | ArbZG §3 |

**Note on reference period:** Germany uses a 16-week reference period as standard (longer than the EU baseline of 4 months = ~17 weeks, so effectively aligned). Works councils (Betriebsrat) may negotiate extensions up to 26 weeks via collective agreement.

---

## Night Work

| Rule | Requirement | Legal basis |
|------|------------|-------------|
| Night period definition | **00:00–04:00** (as defined under German implementation) | ArbZG §2 |
| Maximum working time during night period | **10 hours** within any 24-hour period containing night work | Directive 2002/15/EC Art. 7; ArbZG §6 |
| Night worker health assessment | Employer must offer health check for regular night workers | ArbZG §6(3) |

Under ArbZG §6, night workers are entitled to:
- Transfer to daytime work if health requires it
- Special occupational health protection
- Night work must be compensated by either additional rest or financial compensation per collective agreement

---

## Breaks

| Cumulative working time | Required break |
|------------------------|----------------|
| After 6 hours | ≥ 30 minutes (may be split into two 15-min periods) |
| After 9 hours | ≥ 45 minutes total |

Breaks dovetail with EU 561/2006 driving breaks. The more restrictive rule governs.

---

## Self-Employed Drivers

Self-employed drivers were brought within scope of Directive 2002/15/EC from **August 2020** (after a transitional exclusion). In Germany:
- Self-employed drivers performing road transport subject to EU 561/2006 or AETR are subject to the same 48-hour average weekly working time limit
- FahrpersonalV applies to self-employed drivers as mobile workers
- Enforcement is more complex; self-employed drivers must maintain working time records

---

## Works Council (Betriebsrat) Deviations

Under ArbZG §7, where a works council (Betriebsrat) exists (companies with ≥5 permanent employees), the following deviations may be agreed via works agreement (Betriebsvereinbarung) or collective agreement (Tarifvertrag):

| Parameter | Standard rule | Possible deviation |
|-----------|--------------|-------------------|
| Reference period | 16 weeks | Up to **26 weeks** |
| Daily working time | 10 hours | Up to **12 hours** |
| Daily working time including overtime | 10 hours | Up to **12 hours** |

Deviations require a formal written Betriebsvereinbarung or applicable Tarifvertrag. Without such agreement, the standard ArbZG limits apply.

---

## Record-Keeping

| Requirement | Detail | Legal basis |
|-------------|--------|-------------|
| Working time records | Must be maintained for all mobile workers | ArbZG §16(2); FahrpersonalV |
| Retention period | **2 years** minimum (ArbZG); tachograph records per EU 165/2014 | ArbZG §16(2) |
| Format | Paper or electronic; tachograph data counts for driving time | FahrpersonalV §1 |
| Accessibility | Must be available for inspection at company premises and at roadside | FahrpersonalV |

---

## Enforcement

| Authority | Role |
|-----------|------|
| **Zoll — Finanzkontrolle Schwarzarbeit (FKS)** | Primary enforcement body for working time violations in road transport; roadside and company inspections |
| **BALM (Bundesamt für Logistik und Mobilität)** | Roadside checks for driving/rest time (EU 561/2006); also checks working time records |
| **Polizei** | Roadside document checks; refers working time violations to Zoll |
| **Bundesagentur für Arbeit** | Administrative oversight; audit-based checks at company level |
| **Gewerbeaufsicht (Länder)** | State-level occupational safety authorities; company inspections |

---

## Penalties

| Violation | Fine | Legal basis |
|-----------|------|-------------|
| Exceeding maximum working hours (per violation) | Up to **€15,000** per violation | ArbZG §22 |
| Failing to grant required breaks | Up to **€15,000** | ArbZG §22 |
| Failure to maintain working time records | Up to **€2,500** | ArbZG §22 |
| Systematic or repeated violations | Higher fines; possible criminal prosecution | ArbZG §23 |
| Failure to comply with night work protection | Up to **€15,000** | ArbZG §22 |

Both the **employer (operator)** and in some cases the **manager responsible** (verantwortliche Person) can be fined personally.

---

## Interaction with EU 561/2006

Working time (Directive 2002/15/EC / ArbZG) and driving/rest time (EU 561/2006 / FahrpersonalV) are **separate regulatory systems** that overlap:
- Driving time counted under EU 561/2006 also counts as working time under Directive 2002/15/EC
- "Other work" (loading, administration, waiting) counts as working time but not as driving time
- "Availability time" (known rest period, waiting at border): may or may not count depending on circumstances
- When both sets of rules impose a limit, **the more restrictive limit governs**

---

## Implementation Notes for Developers

```python
# Germany — Working Time Constants
AVERAGE_WEEKLY_MAX_H = 48
ABSOLUTE_WEEKLY_MAX_H = 60
REFERENCE_PERIOD_WEEKS = 16        # standard; extendable to 26 by works council/collective agreement
DAILY_MAX_H = 10                   # standard; 12 with works council agreement
NIGHT_PERIOD_START = "00:00"
NIGHT_PERIOD_END = "04:00"
NIGHT_WORK_MAX_H_IN_24H = 10
BREAK_AFTER_6H_MIN = 30            # minutes
BREAK_AFTER_9H_MIN = 45            # minutes
RECORDS_RETENTION_YEARS = 2
SELF_EMPLOYED_COVERED = True       # from August 2020
WORKS_COUNCIL_CAN_EXTEND_REFERENCE = True  # up to 26 weeks
PRIMARY_ENFORCEMENT_AUTHORITY = "Zoll FKS / BALM"
MAX_FINE_PER_VIOLATION_EUR = 15_000
```

---

*See also: references/eu/working-time.md (EU baseline), references/eu/driving-rest-time.md (EU 561/2006), references/countries/de/driving-rest.md (German driving/rest specifics), references/countries/de/posting-workers.md*
