# EU Smart Tachograph v2 — Requirements and Deadlines

**Sources:**
- Regulation (EU) 2020/1054 — amending Regulation 165/2014 on tachographs
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1054
- Regulation (EU) 165/2014 — tachographs in road transport (base regulation)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0165
- Commission Implementing Regulation (EU) 2016/799 — technical specifications for smart tachograph
- Commission Implementing Regulation (EU) 2021/1228 — specifications for smart tachograph v2
- https://transport.ec.europa.eu/transport-modes/road/social-provisions/tachograph_en — EC DG MOVE: tachograph overview

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
- Issued by the national transport authority in the driver's country of residence (e.g. Transportstyrelsen in Sweden, DVLA in UK, KBA in Germany)
- Lost/stolen: report immediately to the issuing national authority and apply for replacement; a written statement (declaration) must be carried in the vehicle until replacement arrives

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

Tachographs must be calibrated at a workshop approved by the national authority (EU Reg. 165/2014 Art. 24):
- **Every 2 years**
- After any repair affecting measurement accuracy
- After vehicle modifications (tyre size change, axle change)
- After seal tampering is discovered

Calibration seal: must be intact. A broken seal is a **Very Serious Infringement (VSI)** under EU enforcement classification.

---

## Printouts (Tachograph Remsa / Utskrift) — When and What to Write

**Legal basis:** EU Regulation 165/2014 Art. 35; Commission Implementing Regulation (EU) 2016/799 Annex II (technical specifications for printout content).

### When must a printout be produced?

| Situation | Obligation | Basis |
|-----------|-----------|-------|
| **Driver card lost, stolen, or damaged** | Print from the vehicle unit at the **start** and **end** of each daily working period for as long as the card is unavailable | Art. 35(2) |
| **Driver card malfunctioning** | Same as lost/stolen — print start and end of each day until card is replaced | Art. 35(2) |
| **Tachograph malfunction** (vehicle unit fault) | Driver must record activities manually on paper; if the printer still works, produce a printout and annotate it | Art. 36(2) |
| **Requested by an enforcement officer** | Driver must produce printouts covering the current day and preceding 28 days on request | Art. 36(1) |
| **Manual activity entry** | After entering a manual record (e.g., rest taken away from vehicle, activities before joining a vehicle), the driver should produce a printout to verify correct entry | Best practice; Annex II |

> **Note:** Under normal operation with a functioning driver card and vehicle unit, there is **no obligation to routinely print** — the driver card stores the records. Printouts are required mainly when the card is unavailable or on officer request.

---

### What must be written on the printout?

When a printout is used to replace or supplement driver card records (card missing, malfunctioning, or per officer request), the driver must **manually write** the following on each printout:

| Field | Requirement |
|-------|------------|
| **Surname and first name** | Full name — must be legible |
| **Driver card number** | Card number from the missing/damaged card (if known) |
| **Or: driving licence number** | If driver card number is not known (e.g., card never existed, stolen before number noted) |
| **Date** | Date of the printout (if not auto-printed by the device) |
| **Reason** | Why the printout was made (e.g., "card stolen", "card malfunctioning", "officer request") |
| **Signature** | Driver's signature |

**Basis:** EU Reg. 165/2014 Art. 35(2): *"The driver shall enter on the printout their name and the details of the driver licence or driving licence and shall add, where required, the reasons for such a printout, as well as their signature."*

---

### Printout for the current day — practical sequence

When the card is unavailable and the driver must produce a start-of-day printout:

1. Insert company card (or press print without card if device allows)
2. Select "Print daily activities" or equivalent menu
3. Once printed, **immediately write** name, licence/card number, and reason on the printout
4. **Sign** the printout
5. Keep it accessible throughout the day — it must be presented at any roadside check
6. At the **end of the day**, repeat: produce an end-of-day printout, annotate, and sign it

Both the start and end printouts for the day must be kept and presented together.

---

### How long must printouts be retained by the driver?

| Records | Carry period |
|---------|-------------|
| Current day (from midnight) | Always |
| Preceding **28 calendar days** | Must be carried and presented on request |

After the 28-day carry window, printouts must be handed to the employer, who retains them for **at least 12 months**.

---

### Tachograph malfunction — what to record manually

If the vehicle unit breaks down (printer and display both fail), the driver must write activity records on **paper**, covering:
- Name and driving licence number
- Date
- Vehicle registration number
- All activity periods (driving / other work / availability / rest) with start and end times
- Using standard tachograph symbols where possible (steering wheel = driving; briefcase = other work; horizontal bars = availability; bed = rest) — or written text descriptions

The vehicle must be repaired within **7 days** of returning to the home base, or sooner if repair is possible at the current location.

---

## Manipulation and Tampering

Tachograph manipulation is a criminal offence under **EU Regulation 165/2014 Art. 32–33** and constitutes a **Most Serious Infringement (MSI)** in every EU member state:

| Act | EU classification | Typical consequences |
|-----|------------------|---------------------|
| Installing or using a manipulation device | MSI | Criminal prosecution; operator licence review; vehicle immobilisation |
| Driving with broken or bypassed tachograph | MSI | Prohibition from driving until rectified; substantial fine |
| Using another person's driver card | MSI | Criminal offence; driver card suspension; fine |
| Damaged/missing calibration seal | VSI | Fine; mandatory calibration before vehicle may continue |

**Enforcement authority:** Each EU member state designates its own enforcement bodies. Roadside checks are carried out by police, transport inspectorates, or customs depending on the country. MSI findings are logged in **ERRU** (European Register of Road Transport Undertakings) and affect the operator's risk rating EU-wide.

For country-specific enforcement bodies and fine amounts, see the relevant country file (e.g. `references/countries/se/driving-rest.md`, `references/countries/de/driving-rest.md`).

---

## Cross-Reference

- `driving-rest-time.md` — EU 561/2006 driving and rest time rules (what the tachograph records)
- `company-control.md` — Company obligations for tachograph data review
- `eu-vehicle-inspection.md` — Tachograph calibration during annual inspection
- `sanctions-penalties.md` — Fines for tachograph violations
