# EU — Professional Driver Competence (CPC)

**EU Baseline:** This IS the EU baseline file. Reference: Directive 2003/59/EC (initial qualification and periodic training).

**Sources:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003L0059 — Directive 2003/59/EC (full text)
- https://transport.ec.europa.eu/transport-modes/road/professional-drivers_en — EC DG MOVE summary

**Last verified: 2026-03-19**

---

## Scope

Directive 2003/59/EC requires professional drivers of heavy vehicles to hold a Certificate of Professional Competence (Driver CPC). Applies in all 27 EU member states and EEA (NO, IS, LI).

**Applies to drivers of:**
| Licence category | Vehicle type |
|----------------|-------------|
| C1, C1E | Light goods vehicles 3.5–7.5t |
| C, CE | Heavy goods vehicles >7.5t |
| D1, D1E | Minibuses |
| D, DE | Buses and coaches |

**Grandfathering (acquired rights):** Drivers who held the relevant licence before the cutoff dates and have held it continuously are exempt from initial qualification requirements:
- Passenger transport (D/D1): cutoff **10 September 2008**
- Goods transport (C/C1): cutoff **10 September 2009**

---

## Initial Qualification

New professional drivers must complete initial training and pass a knowledge test before driving professionally.

| Element | Details |
|---------|---------|
| Certificate validity | **5 years** |
| Knowledge test | Required to obtain initial certificate |
| Mutual recognition | CPC certificates are mutually recognised across all EU/EEA member states |

---

## Periodic Training

After the initial 5-year certificate, drivers must complete periodic training to renew:

| Requirement | Details |
|------------|---------|
| Total training | **35 hours** per 5-year renewal cycle |
| Module format | Modules of at least 7 hours each |
| Distance learning | Maximum 12 hours per cycle via distance learning (max 1 module) |
| Combined CPC | Drivers holding both goods (C) and passenger (D) licences: one 35-hour program satisfies both |

---

## Driver CPC Card / Licence Marking

- CPC status is marked on the driver's licence or a separate card (Qualification Card)
- The card is issued by the national authority in the driver's country of residence
- Format: EU harmonised code 95 on the driving licence, or a separate Driver Qualification Card (DQC)

---

## Enforcement

- Driving without valid CPC: national sanctions (varies by country — see country penalty files)
- Roadside checks: enforcement authorities check CPC card at the same time as driving licence
- Companies must verify CPC status before assigning drivers to professional driving duties

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Directive 2003/59/EC | Initial qualification and periodic training | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003L0059 |
| EC DG MOVE | Professional drivers overview | https://transport.ec.europa.eu/transport-modes/road/professional-drivers_en |

---

## Implementation Notes for Developers

```
CPC_CERTIFICATE_VALIDITY_YEARS = 5
CPC_PERIODIC_TRAINING_HOURS = 35
CPC_MODULE_MIN_HOURS = 7
CPC_DISTANCE_LEARNING_MAX_H = 12
CPC_DISTANCE_LEARNING_MAX_MODULES = 1
GOODS_CPC_CUTOFF_DATE = '2009-09-10'   # grandfathering cutoff for C/C1 drivers
PASSENGER_CPC_CUTOFF_DATE = '2008-09-10'  # grandfathering cutoff for D/D1 drivers
```

---

*See also: references/countries/se/professional-driver.md (Swedish YKB implementation with SEK fees and national details)*
