# Lastsäkring — Load Securing (Sweden)

**Sources:**
- https://www.transportstyrelsen.se/sv/vagtrafik/yrkestrafik/gods-och-buss/matt-och-vikt/att-lasta-ratt/
- TSFS 2017:25 — Transportstyrelsens föreskrifter och allmänna råd om lastsäkring och kontroll av lastsäkring på och i fordon
- Trafikförordningen (SFS 1998:1276) — road traffic regulations
- EU Directive 2014/47/EU — Technical roadside inspection of commercial vehicles
- European Commission Best Practice Guidelines on Cargo Securing (EN 12195 series)

**Last verified: 2026-06-01**

---

## Overview

Load securing (lastsäkring) is mandatory for all vehicles on Swedish roads. Poorly secured cargo is a significant cause of serious accidents: "Dåligt förankrad last kan orsaka allvarliga olyckor" (poorly anchored cargo can cause serious accidents). The primary regulation is **TSFS 2017:25**, which specifies force requirements, securing methods, and inspection procedures.

---

## Legal Basis

| Instrument | Content |
|-----------|---------|
| TSFS 2017:25 | Transportstyrelsen regulations and general advice on cargo securing and cargo securing inspections on and in vehicles — the core technical standard |
| Trafikförordningen (SFS 1998:1276) | General road traffic law — vehicles must not be loaded in a way that creates danger |
| EU Directive 2014/47/EU | Technical roadside inspection — load securing is a mandatory check item |

---

## Minimum Force Requirements

Cargo must be secured so that it can withstand the following forces without shifting or falling:

| Direction | Minimum force resistance |
|-----------|------------------------|
| **Forward (framåt)** | **80%** of total cargo weight |
| **Backward (bakåt)** | **50%** of total cargo weight |
| **Sideways (sidledes)** | **50%** of total cargo weight |

These correspond to the deceleration/acceleration forces experienced in normal driving conditions and emergency braking.

*Example: A load of 10,000 kg must be secured to withstand at least 8,000 kg force forward, and 5,000 kg force backward and sideways.*

---

## Approved Securing Methods

### Direct Lashing (Direktlåsning)
Straps, chains, or rods attached directly between the cargo and vehicle anchor points. Typically used for heavy machinery, vehicles, and timber.

### Friction-Based Securing
Anti-slip mats (halkskyddsmattor) increase the friction coefficient between cargo and load floor. Can reduce the number of lashings required when friction is verified.

### Blocking and Bracing (Stoppning och stöttning)
Physical barriers — headboards, side stakes, posts — prevent cargo from shifting. Often combined with lashing.

### Containment (Behållarsäkring)
Cargo fully enclosed within the vehicle body (curtainsider/tarpaulin systems, rigid box bodies). Curtainsider covers alone are NOT sufficient securing — additional restraints are needed for most cargo.

---

## Technical Standards Referenced

The European standard **EN 12195** series applies in Sweden:

| Standard | Content |
|---------|---------|
| EN 12195-1 | Calculation of lashing forces — general |
| EN 12195-2 | Lashing webbing straps |
| EN 12195-3 | Lashing chains |
| EN 12195-4 | Lashing wire ropes and steel link chains |

Lashing equipment must be **CE-marked** and rated for the required securing force. The **lashing capacity (LC)** marked on the strap must be checked against the load requirements.

---

## Responsibility

### Driver Responsibility
The driver is responsible for ensuring the load is secured before departure and checking securing during the journey.

### Sender/Loader Responsibility
The party loading the vehicle also has responsibility for proper securing. Under Swedish transport law:
- The sender (avsändare) who loads the goods shares responsibility for securing
- Beställaransvar (orderer responsibility) — see `beställaransvar` provisions in the Yrkestrafiklag (2012:210)

### Carrier/Company Responsibility
The transport company must ensure drivers are trained in load securing and that vehicles are equipped with appropriate securing equipment.

---

## Inspection and Enforcement

### Roadside Checks
Police (Polismyndigheten) and Transportstyrelsen inspectors perform load securing checks during routine roadside inspections. Checks are triggered by:
- Visible cargo irregularities
- Routine professional transport checks
- Specific enforcement campaigns

### What Inspectors Check
- Whether cargo is secured in all three directions (forward, backward, sideways)
- Condition of lashing equipment (no cuts, abrasion, overloading above LC rating)
- Whether securing method is appropriate for the cargo type
- Whether cargo exceeds vehicle load area limits

### Outcome of Failed Inspection
- Vehicle may be **stopped from continuing** until the load is properly secured
- Fines (ordningsbot) or prosecutorial referral for serious cases
- Administrative reporting to Transportstyrelsen for systematic violations by transport companies

---

## Special Cargo Types

### Timber/Logs (Rundvirke)
Timber transport is subject to additional rules in TSFS 2017:25:
- Stanchions must be of approved design and strength
- Stakes/bolsters must be correctly positioned
- Top chains or wires required above load height
- Timber overhang at rear: maximum 3 m behind the last axle, marked with red warning flag/light

### Steel and Metal Products
Heavy, dense cargo requires direct lashing rather than friction-based securing. Edge protection required under lashing straps where sharp edges could damage the strap.

### Containers (ISO/swap-body)
Must be locked using twist-locks (vridlåsare) at all four corners. A container placed without proper corner locking is considered unsecured regardless of other lashings.

### Livestock
Livestock transport has separate requirements — see `live-animals.md` (EU reference). Securing focuses on partitions and density rather than lashing.

---

## Penalties

| Violation | Consequence |
|-----------|------------|
| Unsecured or inadequately secured cargo (driver) | Ordningsbot (fixed fine) or prosecutor referral |
| Cargo falls from vehicle causing accident | Criminal liability (negligence) possible |
| Systematic load securing violations (company) | Sanction fee from Transportstyrelsen |
| Non-compliant lashing equipment | Prohibition on use; may stop vehicle |

Specific fine amounts for ordningsbot are set by the Riksdag and updated periodically. Check Polismyndigheten's current fine schedule for current figures.

---

## Practical Notes for Transport Management Systems

- Load securing compliance cannot be verified remotely — it is a physical check at loading
- TMS systems can assist by: flagging cargo weight vs. vehicle lashing capacity, generating pre-departure checklists, recording driver sign-off on securing
- For multi-drop routes: driver must re-check securing after each unloading
- Digital load securing documentation (photos, driver sign-off) is increasingly used as evidence in disputes

---

## Cross-References

- `dimensions-weights.md` — Cargo load limits and overload rules
- `penalties.md` — Overlastavgift for weight violations
- `transport-dispensation.md` — Special requirements for oversized cargo
- `road-transport-leader.md` — When a road transport leader (escort) is required for wide/heavy loads
- `references/eu/vehicle-inspection.md` — EU technical roadside inspection (Directive 2014/47/EU)
