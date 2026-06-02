# Warehouse Interface — Where Transport Law Meets Warehouse Operations

## Overview

The loading dock is where transport law and warehouse law intersect. The legal allocation of responsibility between carriers, senders, and consignees for loading, unloading, overloading, and cargo damage is complex. Understanding these interfaces is critical for both compliance and liability management in transport management systems.

**Last verified: 2026-06-02**

**Sources:**
- EU Regulation 561/2006 Art. 10–11: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006R0561
- CMR Convention: https://unece.org/transport/road-transport/cmr-convention-and-protocols
- EU Directive 2012/18/EU (SEVESO III): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32012L0018
- EU Customs Code Regulation 952/2013: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0952
- EU Regulation 852/2004 (Food Hygiene): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0852
- EPAL (European Pallet Association): https://www.epal-pallets.org/
- EN 1398 (Loading bay equipment): CEN standard

---

## Chain of Responsibility for Overloading and Loading Operations

### EU Regulation 561/2006 — Responsibilities Beyond the Driver

Regulation 561/2006 does not only bind drivers — it also places obligations on **transport undertakings** and **other parties** in the supply chain:

**Article 10 — Transport undertaking obligations:**
- The transport undertaking must not give drivers financial incentives (per-km bonuses, speed bonuses) that could endanger road safety or encourage hours violations
- The undertaking must organise work schedules to allow compliance; a driver who cannot comply due to the undertaking's scheduling is not the primary violator

**Article 11 — Obligations of senders and other parties:**
- **Shippers, freight forwarders, tour operators, principal contractors, subcontractors, and driver agencies** must not instruct drivers in a manner that could cause violations of Regulation 561/2006
- National enforcement authorities may hold these parties liable in addition to (or instead of) the driver/undertaking

### Responsibility for Overloading

Legal responsibility for an overloaded vehicle is allocated by both national road traffic law and CMR:

| Party | When liable |
|-------|------------|
| **Carrier/driver** | If carrier accepted the vehicle/load without verifying weight; if driver had opportunity to weigh and did not |
| **Sender/shipper** | If sender loaded the vehicle and carrier could not reasonably verify the weight (e.g. sealed containers, covered pallets where weighing would require unloading) |
| **Consignee** | If consignee's delay at the delivery point caused the driver to exceed driving hours to make the delivery window |

**Sealed containers (ISO/swap bodies)**: Under both CMR Art. 17(4)(b–c) and the weight-verification principle, the carrier is generally not liable for overloading if the container was sealed by the sender and the carrier had no reasonable means to verify contents without breaking the seal. The sender bears liability. Carriers should request sender's declaration of gross weight and keep records.

### CMR Carrier Exemptions at Loading

**CMR Article 17(4)(b)**: carrier exempt from liability for loss or damage resulting from **defective packing** not externally visible that was done by the sender.

**CMR Article 17(4)(c)**: carrier exempt from liability for loss or damage resulting from **handling, loading, stowage, or unloading** done by the sender, consignee, or persons acting on behalf of either.

Practical implications:
- If **warehouse staff load** a truck (own loading): any damage caused by improper loading = sender's liability
- If **driver loads** the truck: damage from improper loading = carrier's liability (unless driver notes defects on CMR)
- **Reservation on CMR**: driver who notices defective loading or damaged goods **must note reservations** on the CMR consignment note before signing; otherwise carrier may be presumed to have accepted goods in good condition

---

## SEVESO III Directive — Dangerous Substance Warehouses

### Scope

**EU Directive 2012/18/EU** (SEVESO III, replacing SEVESO II) applies to establishments where **dangerous substances** are present above defined threshold quantities. It affects warehouses, tank farms, chemical depots, fuel storage facilities, and fertiliser stores.

SEVESO III establishes a **two-tier system** based on quantity thresholds:

**Lower tier** (quantities above lower threshold but below upper threshold):
- Notification to competent authority required
- Major Accident Prevention Policy (MAPP) document required
- Internal emergency plan required
- Cooperation with emergency services required

**Upper tier** (quantities above upper threshold):
- All lower tier requirements, plus:
- Full **Safety Report** required (analysis of risks, scenarios, mitigation measures)
- **External emergency plan** prepared by competent authority (based on operator information)
- Land-use planning requirements around the establishment
- Inspection by competent authority at least every 4 years

### Interface with ADR

SEVESO thresholds are **separate from and additional to** ADR quantity limits. A warehouse may:
- Handle quantities well within ADR exemptions (limited quantities) but still exceed SEVESO lower tier thresholds
- Require SEVESO compliance even for goods not transported by road

Practically: any warehouse regularly receiving/storing ADR-classified goods should verify whether SEVESO thresholds are exceeded. Common SEVESO-affected warehouses:
- **Chemical warehouses** (solvents, acids, bases)
- **Fuel depots** (petrol, diesel, LPG)
- **Fertiliser stores** (ammonium nitrate — very low SEVESO threshold: 350 tonnes lower tier)
- **LPG storage** (above 50 tonnes = lower tier)

### Notification and Planning

Transport undertakings delivering to SEVESO establishments:
- Must follow site-specific procedures (induction, DG declaration, parking zones, emergency contacts)
- Driver must be briefed on emergency procedures before entering site
- Vehicle must comply with site access requirements (spark arrestors, bonding points for tankers)

---

## EPAL Pallet System

### EUR/EPAL Pallet Standard

The **EUR/EPAL pallet** (800 × 1,200 mm, 4-way entry) is the de facto standard for European road transport and warehousing. EPAL (European Pallet Association) licenses manufacturers and repair workshops to produce and repair EPAL-marked pallets.

Key specifications:
- Dimensions: 800 × 1,200 × 144 mm
- Rated load: static 4,000 kg; dynamic (forklift) 1,000 kg; racking 1,500 kg
- Material: heat-treated (HT) wood per ISPM 15 (phytosanitary standard for international shipments)
- EPAL mark: branded on centre block (both sides); indicates licensed production

### Pallet Exchange System

EPAL pallets are **exchangeable goods** — they have an agreed exchange value and are swapped one-for-one at delivery:
- **At delivery**: consignee returns the same number of EPAL pallets to the driver
- If consignee has no pallets to exchange: a **pallet receipt** (Palettenschein, bon palette, palletsedel) is issued; this is a debt document; consignee owes pallets or their cash equivalent
- **Pallet receipt** must accompany the CMR or be noted on the CMR; it constitutes a legally enforceable obligation
- Cash equivalent: approximately €8–12 per EUR/EPAL pallet (market-variable)

### Damaged Pallets

- **Damaged pallets are not exchangeable**: a pallet with broken boards, missing blocks, or split stringers is not an EPAL pallet for exchange purposes
- Driver **must refuse damaged pallets in exchange** and note the refusal on the CMR
- If driver accepts damaged pallets without noting, the transport undertaking may not be able to claim the exchange debt
- **Repair**: only licensed EPAL repair workshops may repair pallets and re-stamp them as EPAL

### Forgery

EPAL brand forgery (unstamped pallets, fake EPAL markings) is a criminal offence in most EU jurisdictions. EPAL conducts market surveillance; forged pallets must be destroyed.

### TMS Integration

Pallet tracking in transport management systems:
- Pallet accounts per customer (open/outstanding pallet debts)
- Pallet exchange recorded on consignment; positive = pallets received, negative = pallet debt
- Reconciliation at period end; invoice for pallet debt if not returned within agreed period (typically 30–90 days)
- EDI message types for pallet exchange: DESADV (despatch advice) including pallet count

---

## Loading Time and Demurrage at Docks

### CMR Provisions

**CMR Article 18**: if the carrier incurs costs or suffers delays due to the sender/consignee's failure to load or unload within the agreed time:
- Carrier is entitled to claim costs as additional charges
- If the delay is so long that the carrier's interests are seriously at stake, the carrier may unload the goods at the sender's expense and store them or arrange for their carriage by a different means

CMR does not specify a free loading/unloading time or demurrage rate — these are agreed between the parties or governed by applicable collective agreements.

### National Collective Agreements and Industry Standards

**Germany — ADSp (Allgemeine Deutsche Spediteurbedingungen)**:
- ADSp 2017: standard terms used by most German freight forwarders and carriers
- Free loading/unloading time: agreed per contract; if not agreed, ADSp §19 applies
- Demurrage: **€45 per started hour** beyond free time (ADSp standard; parties may agree different rates)
- Demurrage applies separately for loading and unloading

**Netherlands — CAO Beroepsgoederenvervoer (collective labour agreement for road freight)**:
- Free loading time: **30 minutes** for solo driver (no trailer); **1 hour** for driver with trailer
- After free time: driver entitled to compensation; exact rates set by the CAO in force
- Dutch freight condition (Fenex/TLN conditions): supplement CMR with specific waiting time claims

**Sweden — no specific statutory loading time**:
- Commercial practice: typically 1–2 hours free; negotiated in freight contracts
- Swedish general conditions for transport (NSAB 2015 §22): carrier may claim damages for unreasonable delay caused by sender/consignee

**France — CNR index and LOTI**:
- Loi d'Orientation des Transports Intérieurs (LOTI): general framework
- Decree on loading/unloading times: free time 30 minutes to 2 hours depending on vehicle category; beyond this: tariff of waiting compensation (indexed)

---

## Customs Bonded Warehouses

### Legal Framework

**EU Customs Code — Regulation (EU) 952/2013**, Arts. 237–242, establishes the **customs warehouse procedure**:
- Goods placed in a customs warehouse are in **temporary storage** pending customs clearance; import duties and VAT are **suspended** (not yet due)
- Both EU and non-EU goods may be held in a customs warehouse
- Two main types: **public customs warehouse** (Type I, II, III — open to any depositor) and **private customs warehouse** (Type IV — reserved for warehouse keeper's own goods)

### Transit Documents

When goods move between customs warehouses or from a bonded warehouse to a free-circulation delivery:

- **T1 transit document**: covers **non-EU goods** (third-country goods) moving through EU without paying customs duties; discharged when goods arrive at destination customs office
- **T2 transit document**: covers **EU goods** moving to/from non-EU EFTA/TCA countries (e.g. CH, NO, UK) to confirm their EU customs status and prevent re-importation duties
- **T2L/T2LF**: proof of EU status for goods; not a movement document (no route prescribed)

### NCTS — New Computerised Transit System

**NCTS** (New Computerised Transit System) is the EU's electronic transit management system — it replaces paper T forms for intra-EU and common transit country movements:
- Principal (usually the carrier or freight forwarder) lodges an **electronic transit declaration** in NCTS
- NCTS issues a **MRN** (Movement Reference Number) and a **TAD** (Transit Accompanying Document) — this is the document accompanying the truck
- At destination: consignee's customs office confirms arrival electronically; transit is discharged
- **Common Transit Convention (CTC)**: extends NCTS to non-EU countries (CH, NO, IS, LI, UK, MK, RS, TR)

Practical implications for transport management:
- All movements of non-EU goods (including from bonded warehouses) must be covered by NCTS transit
- Driver must carry printed TAD if electronic verification not possible at destination
- Failure to discharge transit = customs debt becomes due (guarantee is called)

### Exiting a Bonded Warehouse for EU Delivery

Sequence for delivering non-EU goods from a bonded warehouse to an EU customer:
1. Import declaration lodged in customs system (ATLAS in DE, HMRC in UK, etc.)
2. Import duties and VAT paid (or deferred)
3. Goods released from customs warehouse: T1 transit discharged
4. Transport document updated: CMR now covers free-circulation goods
5. Truck may proceed to delivery without further customs stop (within the EU Single Market)

---

## Temperature-Controlled Storage

### Food: EU Regulation 852/2004 (General Food Hygiene)

- All food business operators (including transport operators and warehouse operators handling food) must implement **HACCP** (Hazard Analysis and Critical Control Points)
- Temperature requirements: chilled food typically +2°C to +8°C; frozen ≤−18°C; specific products may have stricter requirements
- **Temperature records**: continuous monitoring required; records kept minimum 2 years
- **Cleaning records**: cleaning and disinfection schedule; records of cleaning activities
- **Pest control**: regular pest control by certified contractor; documentation required

### Pharma: GDP (Good Distribution Practice)

- **EU GDP Guidelines** (2013/C 343/01): binding for wholesale distributors of medicinal products
- Warehouses must maintain mapped temperature profiles; validate storage areas; maintain cold chain continuity during transport
- **Temperature excursions**: any excursion from specified range must be documented; risk assessment conducted; product may need to be quarantined
- GDP audits by competent authorities; non-compliant warehouses can lose authorisation

---

## Loading Dock Safety

### EN 1398 — Dock Levellers

European Standard **EN 1398** (Loading bays — Safety requirements) covers:
- **Dock levellers**: mechanical or hydraulic platforms bridging gap between dock and truck bed; rated capacity must match expected loads; annual inspection required
- **Vehicle restraints**: mechanical or hydraulic hooks/clamps securing truck during loading/unloading; prevent truck creep (vehicle moving away from dock during loading); EN 1398 recommends vehicle restraint systems for all active loading docks
- **Safety markings**: yellow/black hazard markings on dock edge; minimum 1,000 lux lighting at dock face

### Wheel Chocks and Strapping

- **Wheel chocks**: minimum requirement where no mechanical restraint fitted; driver places chocks before loading begins; documented in site procedure
- **Strap restraint systems**: increasingly common on modern docks; connect to truck chassis; release only after loading complete

### Visibility

- Traffic management: separate pedestrian/forklift/truck routes required in warehouses under EU Directive 89/654/EC (Workplace Safety) and associated national regulations
- Reversing cameras/sensors on dock: best practice; required by some customers' supplier codes of conduct
- Banksman (spotter): required for reversing manoeuvres in busy areas per health and safety regulations

---

## Penalties

### Overloading

Overloading penalties apply to the driver/carrier on public roads; at loading premises, responsibility may attach to the loader under Regulation 561/2006 Art. 11 — but enforcement varies by member state.

### SEVESO Violations

- **Lower tier**: failure to notify = fine up to €50,000 (national law varies); regulatory notice requiring immediate compliance
- **Upper tier**: operating without safety report = site closure order; fines up to €500,000 in some member states; criminal liability of management for serious accidents resulting from non-compliance
- **EU enforcement**: ultimately national; but European Commission can pursue infringement proceedings against member states that fail to enforce SEVESO III

### Customs Violations

- **Goods removed from bonded warehouse without clearance**: customs debt immediately due (duties + VAT); penalty up to 100% of customs duty evaded; in serious cases: criminal prosecution
- **T1/T2 not discharged**: guarantee called; surety liable for duties; carrier/principal fined
- **NCTS manipulation/fraud**: criminal offence; prison sentence possible for systematic fraud

### EPAL Forgery

- Criminal offence (trademark infringement + fraud) in DE, NL, BE, FR; fines and imprisonment possible; civil damages to EPAL e.V.
