# EU — Load Securing (Cargo Securing)

**Sources:**
- EN 12195-1:2010 — Load restraining on road vehicles — Safety — Part 1: Calculation of securing forces
- EN 12195-2:2001 — Load restraining on road vehicles — Lashing webbing
- EN 12195-3:2001 — Load restraining on road vehicles — Lashing chains
- EN 12195-4:2004 — Load restraining on road vehicles — Lashing steel wire ropes
- https://transport.ec.europa.eu/transport-modes/road/road-safety/cargo-securing_en — EC DG MOVE: Cargo securing
- https://www.balm.bund.de/EN/Tasks/MandatoryCheckLoads/mandatorycheckloads_node.html — German Federal Logistics Office (BALM): Mandatory load checks
- Council Directive 2014/47/EU — roadside technical inspections (Art. 13: load securing as inspection item)

**Last verified: 2026-06-01**

---

## Overview

Load securing in road transport is governed by the **EN 12195 standard series** (European Norm), which provides the legal and technical framework for calculating and applying cargo restraint forces. Member states enforce load securing under their national road traffic laws. Unsecured or inadequately secured loads are a leading cause of serious road accidents and are subject to administrative and criminal sanctions across the EU.

The key principle: the securing system must be able to withstand defined **acceleration forces** in all directions (forward, rearward, lateral) without the cargo moving, tipping, or shifting. EN 12195-1 is the calculation standard; EN 12195-2 through -4 define the webbing, chain, and wire rope products used.

---

## Legal Framework

Load securing is not governed by a single EU regulation but by a combination of:

| Instrument | Content | Relevance |
|---|---|---|
| EN 12195-1:2010 | Calculation of securing forces | Technical standard; courts and authorities treat compliance as meeting "due care" |
| VDI 2700 | German guidelines (widely referenced across EU) | Supplements EN 12195 in practice |
| Directive 2014/47/EU | Roadside technical inspections | Art. 13: cargo securing is an explicit inspection item |
| National road traffic law | Germany §22 StVO; Sweden Trafikförordning 4:10; FR Code de la route | Carrier's duty to ensure cargo does not fall, shift, or create danger |
| CMR Convention Art. 17 | Carrier liable for damage from poor packing/loading by sender | Civil liability |

**Germany** (BALM/BAG) is the most active enforcer in the EU and has produced detailed guidelines based on EN 12195. German enforcement practice shapes de facto EU standards.

---

## Core Concepts and Definitions

| Term | Definition |
|---|---|
| **G** (gravity force) | Weight of cargo × g (9.81 m/s²); in practice, G = m × g where m = mass in tonnes |
| **µ (mu)** | Coefficient of friction between cargo and load surface |
| **D** | Dimension/rating value — the total securing force a lashing can exert considering the lashing angle |
| **STF** (Securing Tension Force) | Force applied to lashing strap by the tensioner; in Newtons (N) or daN. For standard ratchet lashings, typically 250–500 daN STF |
| **LC** (Lashing Capacity) | Maximum permitted force of the lashing in use; marked on the lashing. LC = SHF (Standard Hand Force) × 2 for ratchet straps |
| **MSL** (Maximum Securing Load) | Maximum force the lashing may exert on the cargo; usually 75% of LC to provide a safety margin. For EN 12195-2 webbing, MSL = 0.5 × MBL |
| **MBL** (Minimum Breaking Load) | Force at which the lashing breaks; must be stated on the label/marking |
| **daN** | DekaNewton; 1 daN ≈ 1 kg force. Commonly used for strap ratings |

---

## Friction Coefficients (µ) — EN 12195-1 Table 2

Friction between the load bottom surface and the vehicle floor is a key variable. Higher friction reduces the number of lashings required.

| Contact surfaces | µ (friction coefficient) |
|---|---|
| Raw wood on rough wooden floor | **0.50** |
| Smooth wood on smooth wood | **0.20** |
| Wood on steel (no coating) | **0.20** |
| Rubber on rough steel | **0.60** |
| Rubber on smooth steel | **0.40** |
| Steel on steel (smooth) | **0.10** |
| Wet surfaces (all types) | **Reduce µ by ~0.2** |
| Anti-slip mats (rubber-coated mesh) | **0.60–0.80** (product-specific; use certified value) |
| Concrete block on metal | **0.40** |

**Important:** Only certified friction-enhancing materials (anti-slip mats, dunnage bags) with documented µ values may be used to claim higher friction coefficients. Using uncertified materials is not permitted as a substitute for proper lashing.

---

## Acceleration Values (EN 12195-1 Table 1)

The securing system must withstand the following acceleration forces (expressed as multiples of g):

| Direction | Acceleration requirement |
|---|---|
| **Forward** (braking) | **0.8 g** |
| **Rearward** (forward jolt) | **0.5 g** |
| **Lateral** (cornering/wind) | **0.5 g** |
| **Vertical** (road shock) | **1.0 g** (must not leave the vehicle floor upward) |

These values come from EN 12195-1:2010 and are the minimum standards. Hazardous goods transport (ADR) applies higher safety factors.

---

## Securing Methods

### 1. Blocking (Form-Fitting Restraint)
The cargo is physically prevented from moving by load-bearing vehicle structures (front headboard, side walls) or blocks/wedges placed against it. No lashing tension required for the blocked direction.

- **Front headboard:** Typically rated 50% of the maximum load on the vehicle (check manufacturer rating). If cargo weight × 0.8 g < headboard rating, front lashing may not be needed.
- **Side boards/stanchions:** Must be load-rated; vehicle body Code L (reinforced) or Code XL (extra reinforced) per EN 12642.
- **Wedges/chocks:** Must be secured themselves; used for cylinders, wheels, barrels.

### 2. Tie-Down Lashing (Friction-Based)
Lashings run over the top of the cargo and are tensioned, increasing the normal force on the contact surface and thus the frictional force holding the cargo. Used where the load can bear the downward lashing pressure.

**Minimum number of tie-down lashings (n):**

For a load on a flat bed (no blocking):

```
n ≥ (m × a) / (2 × STF × µ × cos(α))
```

Where:
- **m** = mass of cargo (kg)
- **a** = acceleration in the relevant direction (0.8 g forward, 0.5 g lateral)
- **STF** = securing tension force of each strap (N)
- **µ** = friction coefficient
- **α** = lashing angle from horizontal (typically 0–30° for tie-down)
- The factor **2** accounts for the two contact points per lashing (over-the-top lashing has two legs)

**Simplified formula for forward securing (most critical direction):**

```
n ≥ (m × 0.8 × g) / (2 × STF × µ)
```

*Example: 5,000 kg cargo, µ = 0.30, STF = 500 daN (5,000 N) per strap:*
*n ≥ (5,000 × 0.8 × 9.81) / (2 × 5,000 × 0.30) = 39,240 / 3,000 = 13.1 → 14 lashings*

This example illustrates why low-friction surfaces (µ=0.30) and heavy loads require many straps. Anti-slip mats (µ=0.60) would halve this requirement.

### 3. Direct Lashing (Restraint Lashing)
The lashing connects the cargo directly to the vehicle via tie-down points, pulling in the direction of anticipated movement. Used for heavy machinery, vehicles on transports, and loads that cannot take tie-down pressure.

**Minimum number of direct lashings (n):**

```
n ≥ (m × a) / (LC × cos(β) × cos(γ))
```

Where:
- **β** = horizontal angle from direction of travel
- **γ** = vertical angle from horizontal
- **LC** = lashing capacity of each lashing

Direct lashings work best when the lashing angle is optimised (as close to the direction of potential movement as possible).

### 4. Loop Lashing (Envelope/Box Lashing)
A combination method where the lashing wraps entirely around the cargo. Provides restraint in multiple directions simultaneously. Commonly used for coils, rolls, and pallets.

---

## Vehicle Body Strength — EN 12642

Vehicle body strength is rated under **EN 12642**:

| Code | Standard | Required strength | Application |
|---|---|---|---|
| **Code L** | EN 12642 (basic) | Front wall: 40% of payload; side walls: 30% | Standard curtainsiders; general freight |
| **Code XL** | EN 12642 (reinforced) | Front wall: 50% of payload; side walls: 30% min + dynamic test | Enhanced curtainsiders; allows greater reliance on body for lateral restraint |

Vehicles with **Code XL** certification can claim body strength as part of the securing calculation, reducing the number of lashings needed. XL coding must be marked on the vehicle.

---

## Lashing Equipment Markings (EN 12195-2)

All lashing straps must be permanently marked with:

| Marking | Meaning |
|---|---|
| **LC** | Lashing Capacity (daN) |
| **SHF** | Standard Hand Force (daN) |
| **Width** | Strap width (mm) |
| **Colour** | Force class indicator (e.g., blue = 1,000 daN LC) |
| **CE mark** | Conformity with EN 12195-2 |

**Common LC force classes:**

| LC (daN) | Colour |
|---|---|
| 500 | Blank (no colour) |
| 1,000 | Blue |
| 2,000 | Red |
| 4,000 | Orange |

**Maximum permitted lashing per strap is MSL = 0.5 × MBL.** Straps with visible wear, cuts, or damage must not be used.

---

## Dunnage, Anti-Slip Mats, and Accessories

| Equipment | Purpose | Note |
|---|---|---|
| Anti-slip mats | Increase µ to 0.6–0.8 | Must be certified; µ value from test certificate |
| Dunnage bags (air bags) | Fill voids between cargo; prevent movement by blocking | Must fill gap completely; not a substitute for lashing |
| Edge protectors | Protect lashing strap from cargo edges | Required when sharp edges contact strap |
| Load bars | Lateral blocking between cargo and side walls | Rated for specific force |
| Timber packing | Protect cargo from vehicle floor vibration; increase friction on wood-to-wood contact | Must be stable |

---

## Roadside Inspection — Directive 2014/47/EU

Cargo securing is an explicit inspection item under Directive 2014/47/EU (Technical Roadside Inspections). Inspectors assess:

1. Is the cargo secured to prevent shifting, falling, rolling?
2. Are lashing straps, chains, or ropes of adequate capacity and in good condition?
3. Is there evidence of recent cargo movement (marks, loosened straps)?
4. Is the vehicle body rated sufficiently (Code L/XL)?

---

## Enforcement Across EU Member States

| Country | Primary authority | Enforcement focus |
|---|---|---|
| **Germany** | BALM (Bundesamt für Logistik und Mobilität) | Most active enforcer; BALM has dedicated cargo check units |
| **Sweden** | Polisen, Transportstyrelsen | Roadside checks at known inspection points |
| **France** | DREAL, Gendarmerie | Combined tachograph and cargo checks |
| **Netherlands** | ILT (Inspectie Leefomgeving en Transport) | Port and road checks |
| **Belgium** | Police fédérale, SPF Mobilité | Highway patrol |

**German BALM practice:** Vehicles with demonstrably insufficient cargo securing are immobilised until the load is properly secured. The responsible driver and transport operator are both subject to fines. Germany publishes detailed cargo securing guidelines ("Richtlinien") aligned with EN 12195 and VDI 2700.

---

## Penalties

Penalties are set under national law. Typical ranges across EU:

| Violation | Typical penalty range |
|---|---|
| Load not secured / risk of falling | EUR 100–2,000 per violation (driver); EUR 200–5,000 (operator) |
| Immobilisation until load secured | — (no monetary penalty, but delays) |
| Serious deficiency causing accident | Criminal prosecution; loss of transport licence |
| Driver contributing to accident due to unsecured load | Criminal negligence charge |

**Germany:** §22 StVO and §69a StVZO; load securing deficiency is an OWi (Ordnungswidrigkeit) with fines starting at EUR 60 (minor) up to EUR 2,000+ (serious risk). Operator liability under §31 StVZO.

**Sweden:** Trafikförordning (SFS 1998:1276) 4 kap. 10 §; unsecured load is a traffic violation; driver's licence suspension possible for serious violations; sanktionsavgift under yrkestrafiklagen for operators.

**France:** Code de la route Art. R312-21; fine of 4th class (up to EUR 750); immobilisation authorised.

**Civil liability:** Under CMR Art. 17(4), if packing or loading was performed by the sender and the inadequate securing caused damage, the carrier's liability may be reduced. If the carrier was responsible for loading and securing, the carrier bears full liability.

---

## Key Regulatory Sources

| Source | Content | URL |
|---|---|---|
| CEN | EN 12195-1:2010 (calculation) | Available from national standards bodies (e.g. SIS, DIN, BSI) |
| CEN | EN 12195-2:2001 (webbing) | Available from national standards bodies |
| EC DG MOVE | Cargo securing — road safety page | https://transport.ec.europa.eu/transport-modes/road/road-safety/cargo-securing_en |
| BALM | Mandatory load check guidance (Germany) | https://www.balm.bund.de/EN/Tasks/MandatoryCheckLoads/mandatorycheckloads_node.html |
| EUR-Lex | Directive 2014/47/EU (roadside inspections) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0047 |

---

*See also: references/eu/vehicle-inspection.md (Directive 2014/47/EU — roadside inspections), references/eu/cmr-liability.md (Art. 17 carrier liability for loading defects), references/eu/dangerous-goods.md (ADR — higher securing standards for hazardous goods)*
