# Air Cargo Interface — Where Road Transport Meets Air Freight Regulation

## Overview

When a truck delivers cargo destined for an aircraft, two separate regulatory regimes must be satisfied simultaneously: the **road transport regime** (ADR for dangerous goods, CMR for contract of carriage) ends at the airport boundary, and the **air cargo regime** (IATA DGR, aviation security rules, Air Waybill liability) begins. Understanding the handover point and pre-departure obligations is critical for shippers, freight forwarders, and road carriers serving airports.

**Last verified: 2026-06-02**

**Sources:**
- IATA Dangerous Goods Regulations (DGR): https://www.iata.org/en/programs/cargo/dgr/
- EU Regulation 185/2010 (air cargo security): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32010R0185
- Montreal Convention 1999 (air cargo liability): https://www.icao.int/
- ICAO Annex 18 (safe transport of dangerous goods by air): https://www.icao.int/safety/DangerousGoods/Pages/annex-18.aspx
- EU Regulation 300/2008 (common rules in civil aviation security): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32008R0300
- IATA Known Consignor programme: https://www.iata.org/en/programs/security/cargo-security/

---

## Where ADR Ends and IATA DGR Begins

### The Regulatory Handover Point

**ADR** (road transport of dangerous goods) applies to the truck journey **until the vehicle reaches the air cargo facility boundary at the airport**. In practice this means:
- The truck is under ADR while driving on public roads, including airport access roads
- Once the truck enters the **airside or landside cargo terminal area** (the Regulated Agent's premises or the shipper's airside facility), the cargo transitions to IATA DGR jurisdiction
- The boundary varies by airport layout; some airports have cargo areas accessible without airside pass (landside handling); others require airside access for cargo delivery

**Practical implication**: a driver delivering DG cargo to an air freight forwarder's off-airport warehouse is still under ADR. The cargo transitions to IATA DGR when the forwarder processes and submits it as air cargo.

### Preparing Documentation Before the Truck Departs

The most important practical rule: **prepare all IATA documentation before the truck leaves the warehouse**. Unlike road transport (where the CMR accompanies the goods), air cargo requires:
- **Shipper's Declaration for Dangerous Goods (SDDG)** to be completed in advance
- **Known Consignor** or screening status confirmed
- Air Waybill (AWB) or pre-AWB reference issued by the forwarder

A truck turned back at an airport cargo terminal — because documentation is missing or incorrect — causes significant delays and may cause the cargo to miss its aircraft, resulting in contractual penalties and time-sensitive shipment failure.

---

## Shipper's Declaration for Dangerous Goods (SDDG)

### Legal Requirement

The **SDDG** is required for **ALL dangerous goods shipped by air**, without exception (unless the goods are below air transport exemption quantities — which are very small). It is the air equivalent of the ADR transport document but has a strictly prescribed IATA format.

### SDDG Format Requirements

The SDDG must contain (per IATA DGR and ICAO Technical Instructions):
- Shipper's name and address
- Consignee's name and address
- Air Waybill number (or pre-AWB reference)
- Page numbering
- Transport details (airport of departure, airport of destination, aircraft type — passenger or cargo only)
- Nature and quantity of dangerous goods:
  - UN number
  - Proper Shipping Name (not trade name)
  - Technical name (if required)
  - Hazard class / division
  - Subsidiary risk(s)
  - Packing group (I, II, III or Not Applicable)
  - Quantity and type of packing
  - Packing instruction (e.g. PI 965 for lithium ion batteries)
  - Authorisation (if required by IATA DGR)
- Certification statement: shipper certifies contents declared, classified, packed, marked, and labelled in accordance with IATA DGR
- Shipper's signature and date

The SDDG must be **typed or computer-generated** (handwritten not acceptable for commercial shipments). It must accompany the Air Waybill.

### Shipper Training Requirement

The shipper (or person completing the SDDG) must be trained in **IATA DGR Category 6 (Shipper)** or equivalent ICAO training:
- Initial training: approximately 3 days
- Recurrent training: every **2 years** (IATA requirement; some national authorities require annual refresher)
- Training providers: IATA-authorised training centres; freight forwarders often provide in-house
- Certificate of training must be kept; may be requested by Regulated Agent or airline

---

## Quantity Limits for DG by Air

Air transport permits far **smaller quantities** of dangerous goods than road transport. Key examples:

| Substance | Road (ADR) | Passenger aircraft | Cargo aircraft only |
|-----------|-----------|-------------------|-------------------|
| Petrol (UN1203, Class 3) | No limit (regulations apply) | Forbidden | 60 litres |
| Lithium ion batteries UN3480 (standalone) | No practical limit | 2.5 g lithium per cell; max 2.7 kg net | 35 kg net |
| Lithium ion batteries UN3481 (in equipment) | No practical limit | 100 Wh per battery; 2 spare batteries | No limit per cell, quantity limits apply |
| Dry ice UN1845 (Class 9) | Large quantities ADR | 2.5 kg per package as refrigerant | 200 kg |
| Aerosols (UN1950, Class 2.2) | No practical limit | 0.5 kg per package; total 2 kg | 35 kg |
| Infectious substance Cat A UN2814 (Class 6.2) | ADR P620 | Forbidden as cargo on passenger aircraft | Permitted under strict conditions |

**Consequence for road operators**: cargo that is perfectly legal under ADR (e.g. a pallet of lithium battery packs) may exceed air transport limits and require re-packing, or may be forbidden by air entirely. This must be assessed before road delivery to airport.

---

## Known Consignor and Regulated Agent (Air Cargo Security)

### EU Regulation 300/2008 and Implementing Rules

EU Regulation 300/2008 (common rules on civil aviation security) and its implementing regulation **EU Regulation 185/2010** establish the **air cargo security chain**. Only **screened** cargo may be loaded onto aircraft.

Two primary statuses in the security chain:

**Known Consignor (KC)**:
- A shipper who regularly despatches cargo by air and has been assessed and approved by the national aviation authority
- KC must implement security measures: access control to premises, cargo screening or protection from tampering, staff background checks and training, designated security manager
- KC status allows cargo to be accepted by Regulated Agents without re-screening (cargo is "known" to have been secured at origin)
- KC registration: shipper applies to national authority (in SE: Transportstyrelsen; in DE: Luftfahrtbundesamt); site audit required; approval valid typically 3 years with interim checks
- KC number: unique identifier; must be stated on documentation; checked by Regulated Agent at receipt

**Regulated Agent (RA)**:
- A freight forwarder, ground handler, or air carrier approved by the national authority to accept and handle air cargo
- RA may receive cargo from KCs and accept it without screening; must screen cargo from non-KC sources (unknown consignors)
- RA is responsible for maintaining the integrity of screened cargo until it is loaded
- RA number: stated on Air Waybill and security declaration

**Unknown Consignor**:
- Any shipper without KC status
- All cargo from unknown consignors must be **physically screened** by the RA (X-ray, explosive trace detection, physical search) before being tendered to the airline
- Screening costs are typically passed to the shipper

### Practical Workflow for Known Consignors

1. Shipper (KC) prepares cargo: packs, labels, secures against tampering; records seal numbers
2. Shipper prepares SDDG (if DG) and packing list
3. Driver collects cargo; consignment is sealed and protected from tampering during road transport
4. Driver delivers to Regulated Agent; RA verifies KC number and documentation
5. RA accepts cargo without screening; issues RA receipt
6. Cargo is air-freight ready; RA submits AWB details to airline

---

## Air Waybill (AWB) vs. CMR

| Feature | Air Waybill (AWB) | CMR Consignment Note |
|---------|------------------|---------------------|
| Mode | Air cargo | Road cargo |
| Convention | Montreal Convention 1999 | CMR Convention 1956 |
| Document type | Non-negotiable (cannot be transferred like a bill of lading) | Non-negotiable |
| Issued by | Carrier (airline) or its agent | Carrier (road) |
| Liability limit (loss/damage) | **17 SDR/kg** gross mass | **8.33 SDR/kg** gross mass |
| Liability limit (delay) | Actual damage; max = carriage charges | Actual damage; max = carriage charges |
| Time limit for claims | 2 years | 1 year (3 years wilful misconduct) |
| DG requirements | SDDG must accompany | ADR transport document |
| Jurisdiction | Montreal Convention | CMR Convention |

**Important**: CMR does **not** apply to air transport, even when the same goods previously moved by road. The road leg (CMR) ends at airport handover; the air leg is governed by the AWB and Montreal Convention.

### Master AWB vs. House AWB

- **MAWB** (Master Air Waybill): issued by the airline to the consolidating freight forwarder (Regulated Agent); covers the full consolidated shipment
- **HAWB** (House Air Waybill): issued by the freight forwarder to the individual shipper; covers the individual shipment within the consolidation
- For DG shipments: SDDG must be attached to the HAWB; the MAWB consolidation must declare DG contents to the airline

---

## Practical Tips for Road-to-Air Freight

1. **Classify before booking**: confirm UN number and packing instruction for IATA compliance before booking road pick-up; reclassification causes missed flights
2. **Check aircraft type**: passenger vs. cargo-only aircraft; forbidden items on passenger aircraft include many common DG; confirm aircraft type with forwarder at time of booking
3. **State of Charge (SoC) for lithium batteries**: many airlines require ≤30% SoC for bulk lithium battery shipments; charging at the warehouse before shipment and then partially discharging may be required
4. **Packaging**: IATA DGR-compliant packaging (UN specification packaging for most DG classes) must be verified; road-only packaging may not meet air standards
5. **Advance booking cut-off**: cargo must be at the RA/airline warehouse hours before flight departure (typically 3–6 hours for DG); plan road transport to meet cargo cut-off, not flight departure
6. **SDDG and KC documentation ready before truck departs warehouse**: never attempt to prepare documentation en route or at airport; airport cargo terminals do not have waiting space and will refuse non-compliant cargo
7. **Temperature-controlled cargo**: if cargo requires temperature-controlled trucking (GDP compliance), confirm the forwarder's handling facility is also temperature-controlled; cold chain must be maintained through to aircraft loading

---

## Penalties

### IATA DGR / ICAO Technical Instructions Violations

Penalties for violations are enforced by national aviation authorities under national aviation law:

- **Undeclared DG on aircraft (hidden DG)**: most serious offence; criminal prosecution; fines up to several hundred thousand euros (DE, UK, FR); potential imprisonment for responsible persons
  - ICAO and IATA maintain incident databases; airlines/forwarders flag repeat offenders
- **Incorrect or incomplete SDDG**: fine + rejection of shipment; in serious cases, suspension of KC or RA status; fines in DE up to €50,000 per occurrence (Luftsicherheitsgesetz)
- **Untrained shipper completing SDDG**: fine; civil liability if undeclared DG causes incident
- **Exceeding quantity limits**: shipment rejected; fine; if already on aircraft and discovered, aircraft returned to gate; major disruption; cost recovery from shipper

### Aviation Security Violations

- **Cargo accepted without screening from unknown consignor**: Regulated Agent faces suspension of RA status; national authority investigation; fine
- **Known Consignor submitting tampered or undeclared cargo**: loss of KC status; prosecution under national security law; IATA/carrier blacklist

### Montreal Convention Claims

Montreal Convention liability is a civil matter (carrier-to-shipper); no administrative penalty. Time limits:
- Damage: notice within **14 days** of receipt (or next working day)
- Delay: notice within **21 days** of delivery
- Loss: claim within **2 years** of date of arrival, actual or expected
