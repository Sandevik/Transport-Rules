# EU Weights and Dimensions — Directive 96/53/EC

**Sources:**
- Directive 96/53/EC — laying down maximum dimensions and weights for road vehicles
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31996L0053
- Directive 2015/719/EU — amending Directive 96/53/EC (aerodynamics, alternative fuels)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015L0719
- Member state implementations: each country transposes Directive 96/53/EC via national road traffic regulations

**Last verified: 2026-03-19**

---

## Overview

**Directive 96/53/EC** (as amended) establishes EU-wide maximum dimensions and weights for heavy vehicles in international transport. Member states may set higher limits for domestic transport (and Sweden does, significantly — see `dimensions-weights.md`).

The directive governs **international** transport across EU member states. When a vehicle operates internationally, the lower EU directive limits apply on roads in other member states unless those countries also allow higher limits.

---

## Maximum Dimensions (Directive 96/53/EC)

### Length

| Vehicle type | EU maximum |
|-------------|-----------|
| Single motor vehicle | **12.00 m** |
| Articulated vehicle (tractor + semi-trailer) | **16.50 m** |
| Road train (lorry + trailer) | **18.75 m** |
| Bus/coach | **15.00 m** (rigid), **18.75 m** (articulated) |

**Nordic exception (Art. 4a — amended by 2015/719/EU):**
The Nordic countries (Sweden, Finland) may continue permitting modular combinations (EMS — 25.25 m / 34.5 m) on their national road networks. These cannot transit into other EU member states without the consent of those states.

### Width

| Vehicle type | EU maximum |
|-------------|-----------|
| Standard motor vehicles | **2.55 m** |
| Refrigerated/insulated vehicles | **2.60 m** |

### Height

| | EU maximum |
|-|-----------|
| All vehicles | **4.00 m** (Directive 96/53/EC) |

**Note:** Sweden's national limit is 4.5 m (higher than the EU directive). For international transport, the 4.0 m EU standard applies in most other member states — check destination country rules.

---

## Maximum Weights (Directive 96/53/EC)

### Gross vehicle weights

| Vehicle type | EU maximum |
|-------------|-----------|
| 2-axle lorry | **18 t** |
| 3-axle lorry | **25 t** (26 t with air suspension on drive axle) |
| 4-axle articulated | **36 t** |
| 5-axle articulated | **40 t** |
| 6-axle articulated | **44 t** |
| Road train (lorry + trailer) | **40 t** |
| Combined transport road train | **44 t** (see below) |

### Axle loads

| Axle type | EU maximum |
|-----------|-----------|
| Single axle (non-drive) | **10 t** |
| Single axle (drive) | **11.5 t** |
| Bogie (2 axles, spacing < 1.0 m) | **11 t** |
| Bogie (2 axles, spacing 1.0–1.3 m) | **16 t** |
| Bogie (2 axles, spacing > 1.3 m) | **18 t** (19 t with air/equivalent) |
| Triple axle (all spacings combined) | **24 t** |

### Why Sweden is different

Sweden's maximum domestic weights are significantly higher (up to **74 t** for EMS/BK4 combinations) because:
- Sweden successfully negotiated special provisions when joining the EU (1995)
- The forest and pulp industry requires high-weight combinations
- Sweden's road network design accommodates these loads on designated routes
- **These Swedish limits do NOT apply in other EU member states**

---

## Alternative Fuel / Aerodynamic Allowances (Directive 2015/719/EU)

Vehicles using **alternative fuels** (CNG, LNG, electric, hydrogen) or with **aerodynamic cabins** get additional weight/length allowances to account for:
- Heavier batteries or gas tanks
- Extended aerodynamic devices at front/rear

| Allow type | Additional allowance |
|-----------|---------------------|
| Weight for alt-fuel system | **+1 tonne** to gross weight limit |
| Length for aerodynamic cab/equipment | **+0.9 m** to rear overhang |
| Length for front aerodynamic deflectors | **+0.5 m** to front of combination |

---

## Cross-Border Operations

When a Swedish carrier drives into Germany, France, or any other EU member state:
- **Directive 96/53/EC limits apply** in those countries
- The Swedish 74t EMS combination is typically **not permitted** without special dispensation in most other EU states
- Standard maximum for most EU international routes: **40 t**, 18.75 m
- For 44 t: must be combined transport (rail/ferry leg involved — see `eu-combined-transport.md`)

**Action:** Before international trips, verify:
1. Vehicle weight vs destination country limits
2. Route restrictions (tunnel height, bridge weight)
3. Dispensation if carrying Swedish-sized combinations

---

## If Your Load Exceeds the Limits

### Discovered before departure

1. **Reduce the load** — redistribute to a second vehicle, leave behind non-essential cargo, or split the load to bring axle and gross weights within limits
2. **Apply for an exceptional transport permit** — if the load cannot be reduced (e.g. indivisible machinery), apply to the national road authority in each country on the route. Permits specify permitted routes, time windows, escort requirements, and speed limits. Processing time varies: days in some countries, weeks in others.
3. **Do not depart overloaded** — roadside weighbridges are common on major freight routes. An overloaded vehicle at a check results in: fine, mandatory reloading before continuing, and a record in the operator's ERRU risk profile.

### Discovered at a roadside weighbridge

| Overage | Typical consequence |
|---------|-------------------|
| Minor (under ~5%) | Fine; may continue if road structure permits |
| Moderate (5–20%) | Fine; may be required to reduce load before continuing |
| Serious (>20%) or axle overload | Vehicle immobilised until load reduced or redistributed; substantial fine; possible operator licence review |

The threshold for mandatory offloading varies by country — enforcement officers have discretion. Paying the fine does not authorise continuing the journey overloaded.

### Exceptional transport permits (overview)

Every EU member state has a permit system for indivisible loads exceeding directive limits. Common requirements:
- Application to the national road authority in advance (in some countries, weeks ahead)
- Route survey — bridges and structures on the route checked against the load
- Time restrictions — most permits restrict to daytime/weekday travel
- Escort vehicles — required above certain thresholds (varies by country)
- Speed limits — typically 50–80 km/h on motorways, lower in urban areas

For country-specific permit procedures, see `references/countries/{code}/oversize-loads.md` where available (e.g. SE, DE, FR, NL, AT, GB).

---

## Cross-Reference

- `references/countries/se/dimensions-weights.md` — Swedish domestic limits (higher than EU)
- `references/countries/se/bk-bearing-classes.md` — Swedish road bearing classes
- `references/countries/se/long-trucks.md` — 25.25 m and 34.5 m combinations (Nordic)
- `references/countries/se/transport-dispensation.md` — Swedish permit process
- `references/eu/combined-transport.md` — 44 t exception for rail/water combined transport
- Country `oversize-loads.md` files — per-country permit procedures
