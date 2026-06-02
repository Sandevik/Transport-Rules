# Digital Transport Systems and Regulatory Technology

**Sources:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1056 — EU Regulation 2020/1056 (eFTI)
- https://unece.org/transport/road-transport/cmr-convention-and-protocols — UNECE: eCMR Protocol
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679 — GDPR (EU Regulation 2016/679)

**Last verified: 2026-06-02**

---

## Overview

Digital technology is transforming road transport compliance and operations. Several EU regulations now mandate or enable digital systems: eFTI creates the framework for digital freight documents; eCMR provides a legally equivalent electronic consignment note; smart tachograph v2 enables automated data exchange with authorities; and GDPR governs how driver data must be handled. This file covers the regulatory technology landscape for transport operators and TMS developers.

---

## eFTI — Electronic Freight Transport Information

**EU Regulation 2020/1056 on electronic freight transport information (eFTI)**

| Parameter | Detail |
|---|---|
| Mandatory from | **21 August 2024** — competent authorities must accept digital transport documents |
| What it covers | Any regulatory information that transport operators must present to authorities (CMR data, ADR documents, driver hours records, customs data) |
| Who must comply | Transport operators AND member state authorities (both must have eFTI-compatible systems) |
| Architecture | Operator stores data on an eFTI platform; authority accesses via standardised API |
| Certification | eFTI platforms must be certified by national competent authority |

**eFTI vs eCMR distinction:**
- **eFTI** = the regulatory framework for authority access to transport data
- **eCMR** = the electronic consignment note (commercial document between carrier and shipper)
- These are separate systems; eFTI can carry eCMR data but is broader

---

## eCMR — Electronic Consignment Note

**CMR Additional Protocol (Geneva 2008) — legally equivalent to paper CMR**

| Parameter | Detail |
|---|---|
| Legal basis | Additional Protocol to CMR (2008); national enabling legislation in each signatory state |
| Countries with eCMR legislation | NL, SE, CH, LU, LT, LV, EE, BG — leading implementations; FR, DE, PL adopting |
| Requirement | Both sender AND carrier must agree to use eCMR |
| Authentication | Electronic signature required (EU Regulation 910/2014 — eIDAS compliant) |
| Format | Typically PDF/XML with QR code for authority verification |
| Status check | Authority scans QR code → verifies document on eCMR platform |
| Platforms | e-CMR.eu, Transfollow, Portbase, carrier-specific solutions (Transics, Trimble) |

---

## TMS — Transport Management System

A TMS is software for routing, load planning, driver dispatch, and real-time tracking. Not regulated by EU law but increasingly expected by customers and necessary for eFTI compliance.

**Core TMS functions:**
- Route optimisation (considering driving time limits, tolls, driving bans)
- Load planning (weight/axle calculation, BK class compliance)
- Driver dispatch and assignment
- Real-time GPS tracking
- Document management (CMR, ADR, ATP)
- Tachograph data integration
- Customer portal (track-and-trace)

**Regulatory integration requirements:**
- Must calculate driving/rest time compliance (EU 561/2006)
- Must flag driving ban periods (DE, AT, PL etc.)
- Must track tachograph download deadlines (90-day VU, 28-day driver card)
- Must support eFTI data export from 2024

---

## FMS — Fleet Management System (Telematics)

Telematics hardware + software for vehicle monitoring.

**Capabilities:**
- Real-time GPS location
- CAN-bus data (fuel consumption, speed, engine hours, idle time)
- Driver behaviour scoring (harsh braking, acceleration, cornering)
- Geofencing (alerts when vehicle enters/leaves zones)
- Remote tachograph download (via DSRC or cellular)
- Eco-driving coaching (visual + audio in-cab)

**EU-required data (smart tachograph v2 — IR 2021/1228):**
- Smart tachograph v2 (retrofit deadline 21 August 2025 for international vehicles) broadcasts data to roadside DSRC units, enabling drive-by tachograph checks without stopping the vehicle

---

## GDPR in Transport

**EU Regulation 2016/679 (GDPR)** applies to all personal data processing, including fleet/driver data.

| Data type | Personal data? | GDPR implications |
|---|---|---|
| Tachograph records (driver card data) | YES — linked to individual driver | Must have legal basis; retention 12 months minimum under EU 561/2006; GDPR retention policy needed |
| GPS location of company vehicle | YES — driver inferred from vehicle location | Must inform drivers; cannot track outside working hours without consent |
| Driver behaviour scoring | YES — individual performance data | Must have legal basis (typically legitimate interest for safety); can be used in employment decisions with notice |
| Camera footage (dashcam) | YES — images of people inside/outside cab | Must be disclosed; retention limits; cannot share with third parties without basis |
| Route data shared with customers | Depends — if driver name removed, not personal data | Pseudonymisation recommended |

**Key GDPR obligations for transport operators:**
1. Inform drivers of all data collection (privacy notice)
2. Legal basis for each processing activity (contract, legitimate interest, legal obligation)
3. Retention limits for all data categories
4. Data sharing agreements with TMS/telematics providers
5. Respond to driver data access requests within 30 days

---

## Smart Tachograph v2 — Digital Interface

Smart tachograph v2 (regulation IR 2021/1228, mandatory for new trucks from August 2023):
- GNSS (GPS) position recording every 3 hours
- DSRC (short-range communication) broadcasts vehicle/driver data to roadside units
- Automated border crossing recording (country code automatically logged)
- ITS-G5 interface for future V2I communication
- Remote early detection capability: authorities detect issues without stopping vehicle

**For TMS integration:**
- Smart tachograph can export data via CAN-bus or dedicated port
- Automated download via remote download unit (RDU) or on-board platform
- Data format: DDD (legacy) and TGD (new format for smart v2)

---

## Penalties

| Violation | Consequence | Legal basis |
|---|---|---|
| Non-compliance with eFTI from 2024 | Administrative fine (varies by member state) | Regulation 2020/1056 |
| GDPR violation (driver data misuse) | Up to €20M or 4% of global annual turnover | GDPR Art. 83 |
| Failing to provide eFTI data to authority when requested | Fine (national implementation) | Regulation 2020/1056 |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| EUR-Lex | Regulation 2020/1056 (eFTI) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1056 |
| UNECE | eCMR Additional Protocol | https://unece.org/transport/road-transport/cmr-convention-and-protocols |
| EUR-Lex | GDPR (Regulation 2016/679) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679 |
| EUR-Lex | IR 2021/1228 (smart tachograph v2) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R1228 |
