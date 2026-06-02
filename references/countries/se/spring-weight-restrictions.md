# Sweden — Spring Thaw Weight Restrictions (Tjällossning)

**EU Baseline:** references/eu/spring-weight-restrictions.md — national deviations apply.

**Last verified: 2026-06-02**

**Sources:**
- https://bransch.trafikverket.se/for-dig-i-branschen/vag/tjallossning/ — Trafikverket tjällossning overview
- https://www.trafikverket.se/resa-och-trafik/vagar/vagarbete-och-vagstangning/tjallossning/ — Public tjällossning information
- TSFS 2018:40 — Trafikverkets föreskrifter om bärighetsklass
- Trafikförordningen (SFS 1998:1276) 4 kap. — road classification and weight rules
- SFS 1972:435 — Lag om överlastavgift (overload fee law)

---

## Overview

**Tjällossning** (spring thaw) refers to the seasonal period when frost leaves Swedish roads and ground, causing the road subbase to temporarily lose bearing capacity. During this period, Trafikverket and some municipalities impose reduced weight limits on roads that would otherwise carry higher loads under their standard BK classification.

The restrictions are applied road by road and year by year — there is no fixed national start or end date. Trafikverket publishes an updated interactive restriction map (kartan för tjällossningsperioden) each year, and affected roads are also signed on-site.

**Who is affected:** Long-distance hauliers, forest industry (timber transport), agriculture, bulk goods operators. Restrictions apply to all vehicles above the reduced weight limit, regardless of origin country.

---

## Timing

| Factor | Typical range | Notes |
|--------|--------------|-------|
| Restriction period start | Late February–late March | Earlier in southern Sweden; later in Norrland |
| Restriction period end | April–June | Varies significantly by region and year |
| Announcement | Rolling — road by road | Trafikverket updates the online map continuously |
| Duration per road | 4–10 weeks typically | Depends on depth of frost and spring temperatures |

The southern half of Sweden (Götaland, southern Svealand) typically exits tjällossning by mid-April. Northern Sweden (Norrland, upper Norrland) may see restrictions persist into June.

---

## BK Classes During Tjällossning

Sweden's standard **BK1** roads normally permit:
- Total vehicle weight: up to 74 tonnes (with special permit), standard 64 tonnes
- Axle loads: up to 11.5t (standard), 12t (BK1 with conditions)

During tjällossning restrictions, affected roads are reclassified temporarily:

| Normal BK class | During tjällossning | Effective weight limit |
|----------------|--------------------|-----------------------|
| BK1 | Reduced to BK2-equivalent | 51.4t total; axle ≤10t |
| BK1 | Reduced to BK3-equivalent | 37.0t total; axle ≤8t |
| BK2 | Reduced to BK3-equivalent | 37.0t total; axle ≤8t |
| BK3 | May be closed entirely | — |

The specific reduction applied to each road is published on the Trafikverket restriction map. Operators must check the map before dispatch.

**Note on BK4:** BK4 roads (special permit roads for Nordic heavy combinations) are not downgraded to the same spring thaw restrictions as BK1/BK2/BK3 in the same way — BK4 designations are based on road construction specifications that account for seasonal variation. However, individual BK4 roads may still have tjällossning restrictions; check the map.

---

## How to Check Current Restrictions

1. **Trafikverket online map:** https://bransch.trafikverket.se/for-dig-i-branschen/vag/tjallossning/
   - Updated in near real-time as restrictions are imposed or lifted
   - Colour-coded by restriction level
   - Downloadable as data feed for TMS integration

2. **Road signs:** Restriction signs (bearing class reduction signs) are posted at the start of affected road sections. These are legally binding regardless of whether the operator has checked the map.

3. **Trafikverket Kundservice:** +46 10 123 10 00

---

## Forest Industry (Timber Transport)

Tjällossning is a critical operational constraint for the Swedish forest industry. Timber transport from forest roads to mills is typically suspended or severely curtailed during the restriction period:
- Forest roads (skogsbilvägar) are almost always unclassified or BK3 and are the first to be closed
- Many sawmills and pulp mills stockpile timber in autumn specifically to bridge the tjällossning gap
- Some forest roads have weight limits of 16t or less during tjällossning
- Trafikverket and Skogsstyrelsen coordinate on forest road conditions

---

## Exemptions

The following vehicle categories may be exempt from tjällossning weight restrictions under certain conditions:

| Vehicle/cargo type | Exemption basis | Notes |
|-------------------|----------------|-------|
| **Milk transport** (mjölktransport) | Trafikverket exemption decision | Applies only to roads where the milk transport route has been specifically approved; operator must carry exemption document |
| **Emergency vehicles** (räddningsfordon) | General exemption | Police, fire, ambulance |
| **Snow clearing vehicles** during active operations | Operational exemption | Restricted to active operations |
| **Vehicles under dispensation** | Transportdispens from Trafikverket | Must be applied for in advance; see references/countries/se/transport-dispensation.md |

Milk transport exemptions are the most practically significant. Dairy collection routes that rely on BK3 roads can apply to Trafikverket for a named exemption covering the specific roads. The exemption is granted per route, not per operator, and must be renewed each year.

---

## Penalties

Violations of tjällossning weight limits are treated as standard overload violations under SFS 1972:435 (Lag om överlastavgift):
- The overload fee (överlastavgift) is charged based on the degree of overload as a percentage of the restriction limit (not the normal BK limit)
- The vehicle owner (ägaren) is liable for the overload fee
- Police may weigh vehicles at roadside; Transportstyrelsen inspectors may also conduct checks
- Vehicles may be ordered to offload excess cargo or return to origin

For the overload fee schedule, see references/countries/se/penalties.md.

**Important:** During tjällossning, the permitted weight is the restriction limit (e.g., 37t on a BK3-restricted road), not the normal BK1 limit. Operating at 50 tonnes on such a road is a 35% overload relative to the restriction, not relative to the normal 64t limit.

---

## Implementation Notes for Developers

```
TJALLOSSNING_SEASON_START_MONTH = 2   # February (southern SE); March–April for northern SE
TJALLOSSNING_SEASON_END_MONTH = 6     # June (northern SE); April–May for southern SE
MAP_URL = "https://bransch.trafikverket.se/for-dig-i-branschen/vag/tjallossning/"
# Restrictions are road-specific; no fixed national weights — always query the map
MILK_TRANSPORT_EXEMPTION = true       # route-specific, requires advance approval
EMERGENCY_VEHICLE_EXEMPTION = true
OVERLOAD_FEE_LAW = "SFS 1972:435"
# Overload calculated against RESTRICTION limit, not normal BK limit
```
