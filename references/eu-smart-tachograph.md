# EU Smart Tachograph v2 — Requirements and Deadlines

**Sources:**
- Regulation (EU) 2020/1054 — amending Regulation 165/2014 on tachographs
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1054
- Regulation (EU) 165/2014 — tachographs in road transport (base regulation)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0165
- Commission Implementing Regulation (EU) 2016/799 — technical specifications for smart tachograph
- Commission Implementing Regulation (EU) 2021/1228 — specifications for smart tachograph v2
- https://www.transportstyrelsen.se/sv/vagtrafik/Yrkestrafik/Kor--och-vilotider/Fardsrivare/

**Last verified: 2026-03-19**

---

## Overview

The **smart tachograph** is the mandatory recording device for tracking driver working time in heavy commercial vehicles. There have been three generations:

| Generation | Name | Key feature |
|-----------|------|-------------|
| Analogue | Analogue tachograph | Paper disc |
| Digital | Digital tachograph (v1) | Digital chip card |
| Smart v1 | Smart tachograph v1 | GNSS + DSRC (remote communication) |
| Smart v2 | Smart tachograph v2 | Enhanced GNSS (Galileo OSNMA), border crossing, remote enforcement |

---

## Smart Tachograph v2 — Key Features

### Galileo OSNMA
Smart tachograph v2 uses **Galileo Open Service Navigation Message Authentication (OSNMA)** — satellite-based, tamper-resistant positioning. This makes location spoofing and manipulation significantly harder than v1.

### Border crossing recording
**Automatic border crossing recording** is a defining feature of v2. The tachograph automatically records when the vehicle crosses an EU member state border. This:
- Enables enforcement of cabotage rules without cab documentation checks
- Supports posting of workers enforcement (Directive 2020/1057/EU)
- Allows remote download of crossing data by enforcement authorities

### Remote communication
Smart tachograph v2 supports **DSRC (Dedicated Short-Range Communication)** — roadside antennas can download tachograph data remotely without stopping the vehicle, enabling:
- Remote roadside checks
- Targeted enforcement against high-risk operators

### Loading/unloading recording
Drivers must manually record the start and end of loading and unloading operations in the v2 tachograph, supporting working time monitoring.

---

## Installation Deadlines (Regulation EU 2020/1054)

### New vehicles

| Vehicle type | Smart tachograph v2 required from |
|-------------|----------------------------------|
| Vehicles > 3.5t newly registered | **2 August 2023** (v1 already required earlier) |
| New vehicles > 3.5t | v2 required **from 21 August 2023** |

### Retrofit deadlines for existing vehicles

| Vehicles currently fitted with | Retrofit deadline |
|-------------------------------|------------------|
| **Analogue or digital (v1) tachograph** | Must retrofit to smart tachograph v2 by **31 December 2024** |
| **Smart tachograph v1** | Must upgrade to v2 by **31 August 2025** |

**Critical deadline: 31 August 2025** — all vehicles subject to tachograph requirements that currently have smart tachograph v1 must be upgraded to v2.

### Light commercial vehicles (>2.5t)

**From 1 July 2026:** Vehicles between **2.5 and 3.5 tonnes** GVW used for **international transport** must be fitted with a smart tachograph.

This is a significant expansion of tachograph requirements — previously only vehicles >3.5t were covered for EU 561/2006 purposes.

---

## Tachograph Cards

Four types of tachograph cards (unchanged between v1 and v2):

| Card | Holder | Colour | Validity |
|------|--------|--------|---------|
| **Driver card** (förarkort) | Individual driver | White | 5 years |
| **Workshop card** | Approved workshop | Red | 1 year |
| **Control card** | Enforcement authority | Blue | 5 years |
| **Company card** | Transport company | Yellow | 5 years |

### Driver card obligations
- Driver must use their personal driver card at all times when driving
- Driver card inserted at start of shift, removed at end
- Driver must ensure the card is valid — apply for renewal before expiry
- Issued by Transportstyrelsen in Sweden
- Lost/stolen: report to Transportstyrelsen, apply for replacement

### Company card obligations
- Companies must use company card to lock in downloaded data
- Required when downloading data from vehicle unit
- Data download frequency: at least every **90 days** from vehicle unit, every **28 days** from driver card

---

## Data Download and Retention

| Data source | Minimum download frequency | Retention period |
|------------|--------------------------|-----------------|
| Vehicle unit (VU) | Every **90 days** | **12 months** (from download) |
| Driver card | Every **28 days** | **12 months** |

Companies must retain downloaded data for **at least 12 months** and make it available to enforcement authorities on request.

---

## Calibration

Tachographs must be calibrated at an approved workshop (verkstad med tillstånd från Transportstyrelsen):
- **Every 2 years**
- After any repair affecting measurement accuracy
- After vehicle modifications (tyre size change, axle change)
- After seal tampering is discovered

Calibration seal: must be intact. Broken seal = serious violation.

---

## Manipulation and Tampering

Tachograph manipulation is a criminal offence:
- Installing or using a manipulation device: criminal prosecution
- Driving with broken/bypassed tachograph: **körförbud** (prohibition from driving) + significant fine
- Using another person's driver card: criminal offence

Swedish enforcement: Polismyndigheten during roadside checks; Transportstyrelsen during company controls.

---

## Cross-Reference

- `driving-rest-time.md` — EU 561/2006 driving and rest time rules (what the tachograph records)
- `company-control.md` — Company obligations for tachograph data review
- `eu-vehicle-inspection.md` — Tachograph calibration during annual inspection
- `sanctions-penalties.md` — Fines for tachograph violations
