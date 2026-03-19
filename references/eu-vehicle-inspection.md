# EU Vehicle Inspection — Roadworthiness and Roadside Checks

**Sources:**
- Directive 2014/45/EU — periodic roadworthiness tests for motor vehicles
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0045
- Directive 2014/47/EU — roadside inspection of commercial vehicles
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0047
- Directive 2014/46/EU — vehicle registration documents (related)
- Swedish implementation: Fordonslagen (SFS 2002:574), Trafikverket TSFS
- https://www.transportstyrelsen.se/sv/vagtrafik/Fordonsregler/Fordonsbesiktning/

**Last verified:** March 2026

---

## Overview

EU Directive 2014/45/EU harmonises periodic roadworthiness testing across member states. Directive 2014/47/EU establishes minimum standards for roadside technical inspections of commercial vehicles. Sweden implements both through national legislation and Trafikverket regulations.

---

## Periodic Roadworthiness Tests (Besiktning) — Directive 2014/45/EU

### Mandatory vehicle categories

| Category | Description | Test frequency |
|----------|------------|---------------|
| **M2** | Buses/coaches > 8 seats, ≤ 5 000 kg | Annually |
| **M3** | Buses/coaches > 8 seats, > 5 000 kg | Annually |
| **N2** | Goods vehicles 3 500 – 12 000 kg GVW | Annually |
| **N3** | Goods vehicles > 12 000 kg GVW | Annually |
| **O3** | Trailers 3 500 – 10 000 kg | Annually |
| **O4** | Trailers > 10 000 kg | Annually |

**Note:** Light vehicles (M1, N1 below 3 500 kg) have less frequent testing — 4 years first test, then 2 years. Commercial vehicles (N2/N3/M2/M3) are annual.

### What is tested (Directive 2014/45/EU, Annex II)

- **Braking systems** — service brake, parking brake, brake lines
- **Steering** — play, condition, power steering
- **Visibility** — windscreen, wipers, mirrors, lights
- **Lights and electrical** — headlights, direction indicators, brake lights, markers
- **Axles, wheels, tyres** — tread depth, tyre condition, wheel nuts
- **Chassis and bodywork** — frame condition, corrosion
- **Noise and emissions** — exhaust, CO/HC levels (diesel opacity test)
- **Tachograph** — calibration validity, seals (for applicable vehicles)
- **Speed limiter** — presence and calibration (for applicable N2/N3/M2/M3)
- **Other safety items** — fire extinguisher, warning triangle, first aid kit (per national rules)

### Defect classification

| Class | Consequence |
|-------|------------|
| Minor (Mindre anmärkning) | Vehicle passes; repair required by next test |
| Major (Anmärkning) | Vehicle fails; repair and retest required within 2–3 months |
| Dangerous (Trafikfarlig) | Vehicle prohibited from road immediately |

### Swedish implementation — Bilprovning

In Sweden, roadworthiness testing is performed by:
- **Bilprovningen** (state company, partial market)
- Approved private testing stations (after market liberalisation in 2010)

Operators must ensure all N2/N3 vehicles pass annual **kontrollbesiktning**. Reminder issued by Transportstyrelsen based on registration date.

---

## Roadside Inspections — Directive 2014/47/EU

### Target

Member states must inspect at least **5% of the total number of commercial vehicles** (N2/N3/M2/M3) in operation within their territory annually.

Sweden: Polismyndigheten and Transportstyrelsen conduct roadside checks.

### Risk rating system

Commercial vehicles are assigned a **risk rating** based on:
- **Company safety rating** — number of previous violations, frequency
- **Vehicle age and origin**
- **Last inspection date and result**

High-risk vehicles are targeted for more frequent checks.

**EU-wide risk rating database:** Transportstyrelsen participates in EU's ERRU (European Register of Road Transport Undertakings) which links to vehicle safety data.

### What is checked at roadside

Initial visual check:
- Tachograph card/record, driver hours compliance
- Driver's licence and CPC card
- Vehicle registration and roadworthiness certificate (besiktningsbevis)
- Load securing
- Tyre condition (visible check)
- Lights, mirrors

If initial check raises concerns, full technical roadside inspection:
- Braking performance (decelerometer)
- Emissions (smoke test)
- Under-vehicle inspection (at mobile inspection unit)
- Coupling devices condition

### Immobilisation

A vehicle found to be **dangerous** can be immobilised (belagd med körförbud) on the spot until repaired. The driver/operator bears costs.

---

## Tachograph Calibration (Related Requirement)

Tachographs must be calibrated/inspected:
- Every **2 years** at an approved workshop
- After any repair or replacement
- After alteration to the vehicle that affects tachograph accuracy

Calibration seals must be intact — tampering is a serious offence. See `eu-smart-tachograph.md` for smart tachograph v2 requirements.

---

## Speed Limiters

Required on (per EU Regulation 2002/85/EC and national rules):
- **N3 vehicles** (>12 000 kg): limited to **90 km/h**
- **M3 buses** (>5 000 kg): limited to **100 km/h**

Speed limiters must be calibrated and sealed. Checked during annual inspection.

---

## Cross-Reference

- `eu-smart-tachograph.md` — Smart tachograph v2 requirements and deadlines
- `driving-rest-time.md` — Hours compliance checked during roadside inspections
- `sanctions-penalties.md` — Penalties for vehicle defects and test failures
