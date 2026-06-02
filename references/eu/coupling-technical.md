# EU — Vehicle Coupling: Technical Specifications

**EU Baseline:** This IS the EU/UN-ECE baseline file. References: UN-ECE Regulation 55, ISO 337, ISO 1102, ISO 1728, ISO 7638, ISO 11446.

**Sources:**
- https://unece.org/transport/vehicle-regulations/wp29-world-forum-harmonization-vehicle-regulations — UNECE WP.29 World Forum for Harmonization of Vehicle Regulations
- https://unece.org/transport/vehicle-regulations — UN-ECE Regulation 55: Uniform provisions concerning the approval of mechanical coupling components of combinations of vehicles (R055)
- https://www.transportstyrelsen.se/sv/vag/Fordon/fordonsregler/tunga-fordon/ — Transportstyrelsen: Swedish heavy vehicle technical regulations

**Last verified: 2026-06-01**

---

## Overview

Vehicle coupling specifications for commercial road transport are governed primarily by UN-ECE Regulation 55 (R055), which provides uniform provisions for the type-approval of mechanical coupling components used in combinations of vehicles. R055 is adopted by EU member states, EEA states, and most AETR signatories under the 1958 Agreement on vehicle type approvals. It covers fifth-wheel couplings, drawbar couplings, ball couplings, and related connectors. Pneumatic (air) connections are standardised under ISO 1728. Electrical connectors are standardised under ISO 7638 and ISO 11446.

All coupling devices installed on vehicles used in international road transport within the UNECE region must bear the relevant type-approval mark (E/e mark) and comply with the applicable standard. Country-specific deviations exist primarily for domestic operations.

---

## Fifth-Wheel (Saddle) Coupling

The fifth-wheel is the primary coupling for articulated lorries (tractor unit + semi-trailer). It consists of a fifth-wheel plate mounted on the tractor and a kingpin mounted on the semi-trailer.

### Kingpin Standards (ISO 337 / UN-ECE R55)

| Class | Kingpin diameter | Typical application |
|-------|-----------------|---------------------|
| Standard (Class A) | **50 mm** | Road tractors up to ~40 t GCW |
| Heavy haul (Class G) | **90 mm** | Heavy haulage, off-highway, high-stress applications |

- The 50 mm kingpin is universal across EU/EEA road transport.
- The 90 mm kingpin is used for heavy-haul combinations (typically >60 t GCW or abnormal load trailers).
- Kingpin height above ground and coupling height are specified in R055 Annex 6.
- Fifth-wheel jaw clearance around the kingpin must not exceed 10 mm when measured with no trailer load applied.

### D-Value (Design Load) Formula

The D-value is the characteristic value for a coupling device, representing the theoretical reference load under dynamic horizontal forces:

```
D = g × (mc × ms) / (mc + ms)
```

Where:
- **D** = characteristic value in **kN**
- **g** = gravitational acceleration = 9.81 m/s²
- **mc** = technically permissible maximum mass of the motor vehicle (tonnes)
- **ms** = technically permissible maximum mass of the trailer/semi-trailer (tonnes)

The D-value of the coupling device must be equal to or greater than the D-value calculated for the vehicle combination. The D-value is stamped on the coupling device alongside the type-approval number.

---

## Drawbar Coupling

Drawbar couplings connect a rigid motor vehicle to a drawbar (centre-axle or converter dolly) trailer.

### Hook Coupling (ISO 1102)

ISO 1102 hook couplings (towing hooks) are the standard form of drawbar coupling. They come in two main classes:
- **Class D** (standard hook): For vehicles up to ~18 t drawbar pull
- **Class E** (heavy hook): For vehicles with higher drawbar forces

The D-value formula is the same as for fifth-wheel couplings.

### S-Value (Vertical Static Load)

The **S-value** is the vertical static load transferred from the drawbar trailer onto the coupling. It represents the nose load of the trailer on the coupling point.

- The S-value is expressed in **kg** (or kN).
- The coupling device must be rated for an S-value equal to or greater than the actual static nose load.
- Typical drawbar trailer S-values: 1,000–4,000 kg for standard combinations.
- Exceeding the S-value rating constitutes an overloading violation.

### V-Value (Vertical Dynamic Load for Drawbar)

The **V-value** applies to drawbar couplings where significant vertical oscillation is expected (e.g., off-road or rough-road applications):

```
V = D × a/g
```

Where:
- **V** = vertical oscillation load in kN
- **D** = characteristic D-value of the coupling (kN)
- **a** = vertical acceleration coefficient (m/s²) derived from test conditions
- **g** = gravitational acceleration 9.81 m/s²

The V-value is used in type-approval testing to verify the coupling's resistance to vertical dynamic forces.

---

## Ball Coupling (Tow Ball)

Ball couplings are used primarily for light vehicles and lighter trailers, but are relevant for commercial transport combinations at the lighter end of the weight spectrum.

| Class | Ball diameter | Maximum application |
|-------|--------------|---------------------|
| Class A | **50 mm** | Light passenger vehicles, trailers up to ~750 kg |
| Class B | **50 mm** | Passenger vehicles, trailers up to 3,500 kg trailer mass |
| Class G | **80 mm** | Heavier vehicles, trailer mass up to ~6,000 kg |

**Country deviation — Sweden:** Swedish regulations require 80 mm ball coupling (Class G) for vehicle combinations where the trailer mass exceeds 3,500 kg. For combinations with a trailer mass of 3,500 kg or less, a 50 mm ball coupling (Class A/B) is permissible if the D-value is sufficient.

Ball couplings must bear an E-mark showing the D-value and, where applicable, S-value rating.

---

## Air (Pneumatic) Connections (ISO 1728)

Air connections between towing vehicle and trailer use two standardised glad-hand couplings under ISO 1728:

| Line | Colour | Function | Operating pressure |
|------|--------|----------|--------------------|
| **Supply / Emergency** | **Red** | Charges trailer reservoir; loss of pressure triggers emergency brake | **8.5 bar** (max) |
| **Service / Control** | **Yellow** | Modulates trailer service brakes under driver control | **8.5 bar** (max) |

- The red and yellow coupling heads are physically identical (ISO 1728 specifies size and thread), but are colour-coded to prevent cross-connection.
- Cross-connection (red to yellow or vice versa) causes loss of trailer braking and is extremely dangerous — a significant roadside inspection defect.
- Coupling heads must be fitted with dust caps when disconnected.
- ISO 7775 specifies colour coding in addition to ISO 1728.

---

## Electrical Connections

### ISO 7638 — ABS/EBS Connector (7-pin, 24V)

ISO 7638 is the mandatory electrical connection for trucks and trailers equipped with ABS (Anti-lock Braking System) or EBS (Electronic Braking System):

| Pin | Function |
|-----|----------|
| 1 | +24V supply (ignition-controlled) |
| 2 | Ground (return) |
| 3–7 | ABS/EBS data (CAN bus / J1587 depending on generation) |

- 7-pin, **24V DC** for heavy vehicles.
- Required on all new vehicles with ABS fitted since Directive 71/320/EEC amendments.
- The 7-pin ISO 7638 connector is physically keyed and coloured to prevent confusion with other connectors.
- A 5-pin variant (ISO 7638-2) exists for lighter applications, but is not common in heavy commercial transport.

### ISO 11446 — Multiplex / Auxiliary Connector (15-pin)

ISO 11446 (15-pin) carries auxiliary electrical signals — lighting, TPMS data, additional CAN channels, and auxiliary power:

| Signal group | Pins | Function |
|-------------|------|----------|
| Lighting | 1–7 | Position/tail, indicators, reverse, brake lights |
| Auxiliary power | 8–9 | 24V power supply for trailer accessories |
| Data bus | 10–15 | CAN, additional vehicle data |

- Increasingly standard on modern tri-axle and refrigerated trailers.
- Enables the driver display to show trailer ABS status, door sensor, temperature monitoring (ATP trailers), and load information.

### ISO 3731 (formerly 24N/24S) — Legacy 7-pin Connectors

Older 7-pin connectors (24N for normal functions, 24S for supplementary) are still found on vehicles manufactured before approximately 2005. They carry basic lighting and a limited set of auxiliary functions. These are being phased out in favour of ISO 11446.

---

## Type-Approval and Markings

Under UN-ECE R55, every coupling device must be marked with:
1. **E-mark** or **e-mark**: Approval by a UNECE contracting party (capital E = UNECE 1958 Agreement; lowercase e = EU type approval)
2. **Country code** (e.g., E1 = Germany, E5 = Sweden)
3. **Approval number**
4. **D-value** (kN)
5. **S-value** (kg) — for coupling devices designed to bear vertical static loads
6. **V-value** (kN) — where applicable

The markings must be permanently affixed, legible, and not on components that can be removed without tools.

---

## Inspection Requirements

Coupling devices on commercial vehicles are inspected:
- At **periodic roadworthiness tests** (EU Directive 2014/45/EU): inspectors check for excessive jaw wear, cracked fifth-wheel plates, kingpin wear, missing locking indicators, and damaged air/electrical connections.
- At **roadside technical inspections** (EU Directive 2014/47/EU): DVSA/BALM/DKMT etc. include coupling condition in roadside checks.
- **Annual**: Most EU member states require annual inspection for HGV trailers.

A coupling with jaw clearance exceeding 10 mm around the kingpin, or a cracked fifth-wheel plate, is classified as a **major defect** that prohibits further operation.

---

## Penalties

Penalties for coupling violations are applied at the national level. Common categories:

| Violation | Typical severity |
|-----------|-----------------|
| Coupling device without valid E-mark | Vehicle prohibition; significant fine |
| Worn coupling (jaw clearance >10 mm) | Roadworthiness failure; prohibition to drive |
| Cross-connected air lines | Immediate prohibition; safety-critical defect |
| Missing or damaged air line dust caps | Minor defect; advisory notice |
| D-value rating exceeded by combination | Fine; load restriction order |

Specific fine amounts vary by country (see country-specific files).
