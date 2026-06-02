# EU — Road Transport Working Time

**EU Baseline:** This IS the EU baseline file. Reference: Directive 2002/15/EC.

**Sources:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0015 — Directive 2002/15/EC (full text)
- https://transport.ec.europa.eu/transport-modes/road/social-provisions/road-transport-working-time_en — EC DG MOVE summary

**Last verified: 2026-03-19**

---

## Scope

Directive 2002/15/EC applies to:
- **Mobile workers** employed by transport companies performing road transport subject to EU 561/2006 or AETR
- **Self-employed drivers** performing such transport
- Applies to vehicles >3.5t and buses (same scope as EU 561/2006)

Drivers of light vehicles (≤3.5t) are not covered by this directive.

---

## Maximum Working Hours

| Rule | Limit | Directive Article |
|------|-------|-----------------|
| Average weekly working time | **48 hours/week** | Art. 4 |
| Absolute weekly ceiling (single week) | **60 hours** | Art. 4 |
| Calculation period for average | **4 months** (extendable to 6 by collective agreement) | Art. 4 |

---

## Break Requirements

After reaching the following cumulative working time thresholds, a break must be taken:

| Cumulative work | Minimum break |
|----------------|---------------|
| 6 hours | ≥ 30 minutes |
| 9 hours | ≥ 45 minutes |

Breaks may be divided into periods of at least 15 minutes each (Art. 5).

**Interaction with EU 561/2006:** Driving breaks (45 min after 4h30 driving) also apply. Where both sets of rules apply, the more restrictive rule governs.

---

## Night Work

| Rule | Requirement | Article |
|------|------------|---------|
| Night work maximum | **10 hours** within any 24-hour period containing night work | Art. 7 |

Night period definition: varies by member state implementation; typically a period of at least 7 hours including the hours 00:00–05:00 (Art. 1(6)).

---

## Record-Keeping

- Working time must be recorded (Art. 9)
- Records accessible to enforcement authorities
- Retention period: minimum 2 years (varies by national implementation)

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Directive 2002/15/EC | Full directive text | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32002L0015 |
| EC DG MOVE | Working time in road transport | https://transport.ec.europa.eu/transport-modes/road/social-provisions/road-transport-working-time_en |

---

## Implementation Notes for Developers

```
AVERAGE_WEEKLY_MAX_H = 48
CALCULATION_PERIOD_MONTHS = 4      # extendable to 6 by collective agreement
ABSOLUTE_WEEKLY_MAX_H = 60
BREAK_REQUIRED_AFTER_H = 6
BREAK_MIN_FOR_6_TO_9H = 30         # minutes
BREAK_MIN_FOR_OVER_9H = 45         # minutes
BREAK_SPLIT_MIN_PERIOD_MIN = 15
NIGHT_WORK_MAX_H_IN_24H = 10
RECORDS_RETENTION_YEARS = 2        # minimum; national law may require more
```

---

*See also: references/eu/driving-rest-time.md (EU 561/2006 — driving/rest time rules, related but separate)*
