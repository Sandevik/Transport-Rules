# Rail Transport Interface — COTIF, CIM, RID, and EU Rail Freight

## Overview

Rail transport interfaces directly with road transport in two ways: as a **combined transport leg** (truck carried on flatcar, or container transferred to wagon) and as a **competing/complementary mode** in multimodal logistics chains. For transport operators and TMS developers, understanding the key rail conventions — COTIF, CIM, and RID — and the EU Rail Freight Corridor network is essential for multimodal compliance.

**Last verified: 2026-06-02**

**Sources:**
- OTIF (Intergovernmental Organisation for International Carriage by Rail): https://otif.org/en/
- COTIF Convention text: https://otif.org/en/?page_id=1105
- EU Rail Freight Corridors: https://ec.europa.eu/transport/modes/rail/freight_en
- ERA (European Union Agency for Railways): https://www.era.europa.eu/
- RID 2025 dangerous goods regulations: https://otif.org/en/?page_id=176
- Brenner ROLA: https://www.rola.at
- EU Regulation 913/2010 on European rail network for competitive freight

---

## COTIF — Convention Concerning International Carriage by Rail

### Overview

COTIF (Convention Concerning International Carriage by Rail) is the foundational international treaty for cross-border rail transport, administered by **OTIF** (Organisation Intergouvernementale pour les Transports Internationaux Ferroviaires), headquartered in Berne, Switzerland.

- **Original treaty**: Berne, 1980 (COTIF 1980)
- **Current version**: COTIF 1999 (Vilnius Protocol), entered into force 1 July 2006
- **Contracting states**: 51 member states + 1 associated member; includes all EU states, plus Switzerland, Norway, UK, Turkey, Middle Eastern and North African states, and former Soviet states on the western fringe
- **Secretariat**: Berne, Switzerland; Director General appointed by General Assembly

COTIF consists of a core convention and **seven appendices**, each constituting a separate sub-convention:

| Appendix | Code | Subject |
|----------|------|---------|
| A | CIV | Carriage of passengers and luggage |
| B | CIM | Carriage of goods |
| C | RID | Dangerous goods by rail |
| D | CUV | Use of wagons |
| E | CUI | Use of infrastructure |
| F | APTU | Technical standards |
| G | ATMF | Technical admission |

---

## CIM — Uniform Rules for International Rail Freight

### Scope

CIM (Appendix B to COTIF) governs the **contract of carriage** for international rail freight in COTIF member states. It is the rail equivalent of CMR for road transport.

CIM applies when:
- The contract involves carriage over the territory of at least two COTIF contracting states
- The carriage uses railway infrastructure included in the CIM list maintained by OTIF
- The consignment note designates CIM as applicable (in practice: always for international rail freight between COTIF states)

### CIM Consignment Note

The **CIM Consignment Note** (also called the CIM waybill) is the standard contract document for international rail freight:
- Issued by the carrier (railway undertaking or freight forwarder acting as carrier)
- Must accompany the wagon/container for the full journey
- Contains: sender/receiver details, stations of departure/destination, description of goods, weight, number of packages, declared value (if applicable), carriage instructions
- **CIM + SMGS**: a combined CIM/SMGS consignment note exists for rail transport between EU/COTIF states and CIS/former Soviet states (Russia, Kazakhstan, China via Trans-Siberian route)

### Carrier Liability Under CIM

**Loss or damage:**
- Carrier is liable unless it can prove: force majeure, inherent vice of goods, fault of sender/consignee, or one of the specified exculpatory circumstances (defective packing by sender, natural wastage in transit)
- Maximum liability: **SDR 17 per kg** of gross mass lost or damaged
  - Example: 1,000 kg lost → max liability SDR 17,000 ≈ €20,000 at current SDR rate
  - No overall limit per consignment (unlike CMR's SDR 8.33/kg for road)
- Declared interest in delivery: sender may declare a higher value; surcharge applies; carrier then liable up to declared amount

**Delay:**
- Carrier liable for delay if consignment not delivered within agreed time limit
- Default delivery time limits: Article 16 CIM — 24 hours per 400 km for wagon-load, 24 hours per 200 km for full trains (rounded up)
- Delay compensation: actual damage proven, up to amount of carriage charges (if no declared interest in delivery)
- Declared interest in timely delivery: compensation up to declared amount regardless of actual carriage charges

**Time limits for claims:**
- General: **1 year** from date of delivery (or date delivery should have occurred)
- Loss: 1 year from date carrier gave notice of loss
- Wilful misconduct or equivalent gross fault: **3 years**
- Written claim must be submitted to suspend limitation period

**Successive carriers:**
- In international rail transport, the **delivering carrier** (last in chain) is primarily liable to the consignee
- Any carrier in the chain can be sued by another for contribution

---

## RID — Regulations Concerning International Carriage of Dangerous Goods by Rail

### Scope and Update Cycle

RID (Appendix C to COTIF) is the rail equivalent of ADR. It applies to all international carriage of dangerous goods by rail in COTIF states, and is incorporated into EU law via **Directive 2008/68/EC** for domestic carriage within EU member states.

- RID is updated **every two years** (same cycle as ADR), using the same UNECE working party process
- Current edition: **RID 2025** (in force 1 January 2025; 1 July 2025 for new provisions)
- RID 2027 under preparation

### RID vs. ADR

RID uses the **same UN numbers, hazard classes, and packing groups** as ADR. Key differences:

| Aspect | ADR (Road) | RID (Rail) |
|--------|-----------|-----------|
| Transport units | Road vehicles | Railway wagons |
| Quantity thresholds | Per vehicle | Per wagon or train |
| Tank requirements | Tank vehicles/containers | Tank wagons, tank containers |
| Segregation | Vehicle/tunnel | Wagon/train composition rules |
| Exemptions | Art. 1.1.3 (limited quantities etc.) | Similar, with rail-specific exemptions |
| Supervision | Driver 24h | Shunting/yard rules |

### Wagon Classifications

- **Closed wagons** (type F, S): standard box/flat wagons; DG requirements per substance
- **Tank wagons** (type Z): liquids and gases in bulk; material/pressure specifications per substance
- **Container-carrying wagons**: ISO tank containers, portable tanks subject to RID chapter 6 requirements
- **Refrigerated wagons**: specific rules for flammable refrigerants

---

## EU Rail Freight Corridors (RFC)

### Legal Basis

**EU Regulation 913/2010** established the European rail network for competitive freight, creating **Rail Freight Corridors (RFCs)** to improve the attractiveness of international rail freight vs. road.

Nine RFCs are currently operational, each managed by a corridor management structure with a **One Stop Shop** (OSS) for international path requests.

### Key Corridors for Swedish/Nordic Operators

**RFC 3 — Scandinavian-Mediterranean Corridor** (most relevant for SE operators)
- Route: Stockholm → Malmö → Øresund Bridge → Copenhagen → Hamburg → Rotterdam/Antwerp → Lyon → Marseille/Genova
- Manages: priority access for international freight trains; track allocation via OSS
- Relevant for SE exports to Central and Southern Europe

**RFC 5 — Baltic-Adriatic Corridor**
- Route: Gdynia/Świnoujście → Warsaw → Katowice → Vienna/Bratislava → Ljubljana/Trieste
- Connects Baltic ports with Adriatic; CE → Poland rail connection

**RFC 1 — Rhine-Alpine Corridor**
- Route: Genova → Milan → Basel → Rotterdam (via Gotthard Base Tunnel from 2016)
- World's longest railway tunnel (Gotthard, 57 km)

**RFC 8 — North Sea–Baltic Corridor**
- Route: Wilhelmshaven/Bremerhaven/Hamburg → Berlin → Warsaw → Kaunas → Tallinn/Riga/Vilnius
- Rail Baltica project (new standard-gauge line through Baltics): under construction; expected completion ~2030

### Priority Access

On RFC corridors, **international freight trains have priority** in path allocation over domestic trains, except:
- Passenger services with statutory priority
- Infrastructure maintenance
- Emergency situations

Path requests through the One Stop Shop receive a response within **a specific timeframe** (agreed per corridor); binding paths are offered at the Annual Timetable or as ad hoc requests.

---

## ROLA — Rolling Road (Rollende Landstrasse)

### Concept

ROLA (**Ro**llende **La**ndstrasse, "rolling road") is a rail service where **complete trucks** (tractor + trailer/semi-trailer or solo truck) are loaded onto flat wagons and transported by train. The road vehicle drives on and off under its own power at the terminals.

ROLA is used primarily to:
- Avoid alpine road bans (AT and CH night/weekend sectoral bans)
- Reduce road congestion in sensitive alpine areas
- Comply with combined transport exemptions

### Brenner ROLA (Austria–Italy)

- **Route**: Wörgl (AT) ↔ Brennersee/Trento (IT) — crossing the Brenner Pass
- **Operator**: RoLa Brenner GmbH (https://www.rola.at)
- **Service**: daily departures; approximately 4 hours transit time
- **Why used**: the A13 Brenner Motorway has **sectoral bans** and night driving bans; ROLA avoids these; qualifies as combined transport → road legs exempt from cabotage restrictions
- **Booking**: online or via freight forwarder; wagon reservation required; advance booking recommended
- **Height limit**: 4.0m vehicle height (tunnel clearance constraint)
- **Driver**: driver travels in special passenger coach on the same train; passport/ID required; no sleeping in truck cab during ROLA

### Gotthard ROLA (Switzerland)

- **Route**: Freiburg im Breisgau (DE) / Novara (IT) — crossing Gotthard / via BLS Cargo
- **Operator**: BLS Cargo / Hupac
- **Alternative**: Lötschberg ROLA service also available
- **Restriction**: CH imposes weight limits on road; heavy combinations benefit from ROLA

### Other ROLA Services

- **Tauern ROLA**: Villach (AT) ↔ Salzburg/Innsbruck area — avoids Tauern alpine route
- **Karawanken**: Villach ↔ Ljubljana (SI)

---

## Eurotunnel Rail Freight (Le Shuttle Freight)

- **Service**: Eurotunnel Le Shuttle Freight — truck loaded onto dedicated freight shuttle train; Folkestone (UK) ↔ Coquelles/Calais (FR)
- **Operator**: Getlink (formerly Eurotunnel)
- **Different from Eurostar**: Le Shuttle Freight is a separate service; driver and truck travel together; no passenger Eurostar trains carry freight
- **Journey time**: approximately 35 minutes in tunnel
- **Booking**: required in advance; via https://www.eurotunnel.com/uk/freight/
- **Dangerous goods**: tunnel has specific DG restrictions (Class 1 explosives prohibited; Class 2 flammable gases restricted; advance declaration required for all DG)
- **Customs**: UK-EU border; full customs procedures apply since Brexit; GVMS (Goods Vehicle Movement Service) registration required for UK-bound trucks

---

## CIM vs. CMR in Multimodal Consignments

For road-rail multimodal shipments:

- **Road leg**: CMR applies; road carrier issues CMR consignment note
- **Rail leg**: CIM applies; railway undertaking or NVOCC issues CIM waybill
- **Multimodal through document**: FIATA FBL can cover both; operator takes on combined carrier liability

If a **single carrier** issues one consignment note covering both legs:
- If document is a CIM note: CIM rules apply throughout (carrier is responsible for road leg under CIM Article 5)
- If document is a CMR note: CMR applies throughout for the whole journey (carrier is responsible for rail leg under CMR Article 2 — known as the "truck on rail" article)

**CMR Article 2** (truck on ferry/rail): when a loaded truck is carried on a train (ROLA) or ferry without unloading, CMR applies to the entire journey, including the rail/sea leg, unless damage/loss was caused exclusively by rail/sea causes.

---

## Track Gauge Differences

A significant operational constraint for international rail:

| Network | Gauge | Countries |
|---------|-------|-----------|
| Standard gauge | 1,435 mm | Most EU, CH, NO, UK, CN (high-speed), Middle East |
| Broad gauge (RU) | 1,520 mm | Russia, Belarus, Ukraine, Finland, Baltic states* |
| Iberian gauge | 1,668 mm | ES, PT (being converted to standard gauge) |
| Metre gauge | 1,000 mm | Parts of CH (narrow mountain lines) |

*Baltic states (EE, LV, LT) currently use 1,520 mm Russian gauge; Rail Baltica project is building a new **1,435 mm standard gauge** line through the Baltics, expected to reach Tallinn by ~2030.

**Finland**: uses 1,520 mm gauge; wagon exchange or bogie change required at FI border; direct rail to SE/EU requires ferry (Helsinki–Tallinn–Riga–Warsaw corridor via Rail Baltica when complete).

---

## ERA — European Union Agency for Railways

- ERA issues **Single Safety Certificates** for railway undertakings operating internationally within the EU (mandatory since June 2020 under Fourth Railway Package)
- ERA maintains the **ERADIS** database of authorisations, certificates, and notifications
- ERA also manages the **Type Authorisation** process for new rolling stock (wagons, locomotives)
- Relevant for transport operators using rail carriers: ensures your rail carrier holds valid ERA safety certificate

---

## Penalties

### CIM Claims — Carrier Penalties

CIM sets liability limits (carrier's financial exposure), not administrative penalties. National enforcement of rail safety is via:
- ERA safety certificates: suspension or withdrawal for non-compliance
- National Safety Authorities (NSA): fines for safety violations; amounts set by national law

### RID Violations (via Directive 2008/68/EC)

Penalties set by each member state; comparable to ADR enforcement:
- **DE**: BALM enforces at loading facilities; fines €500–€5,000 per violation; wagon detention
- **AT**: Federal Rail Regulation Office; fines up to €10,000 for serious DG violations
- **CH**: FOT (Federal Office of Transport); fines up to CHF 20,000

### ROLA/Combined Transport

- Misuse of combined transport exemption (claiming CT relief without qualifying): national penalty; road ban infringement fines + back-payment of applicable road charges/tolls
- In AT: fine up to €10,000 for false CT declaration
