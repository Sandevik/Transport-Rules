# Norway — Spring Thaw Weight Restrictions (Bæreevneperiode)

**EU Baseline:** references/eu/spring-weight-restrictions.md — Norway is not an EU member but applies EEA transport rules; spring thaw restrictions are a national matter governed by Vegtrafikkloven and Vegvesen regulations.

**Last verified: 2026-06-02**

**Sources:**
- https://www.vegvesen.no/trafikkinformasjon/drivstoff-miljo-og-teknologi/baerevne/ — Statens vegvesen bæreevne overview
- https://www.vegvesen.no/kjoretoy/yrkestransport/spesialtransport-og-dispensasjon/begrensning-av-kjoretoy-pa-grunn-av-telelosning/ — Teleløsning restrictions
- https://vegkart.atlas.vegvesen.no/ — Nasjonal vegdatabank / Vegkart (road condition map)
- Vegtrafikkloven (Lov om vegtrafikk) 1965-06-18-4, §13
- Forskrift om bruk av kjøretøy (FOR-1990-01-25-92)
- https://lovdata.no/lov/1965-06-18-4 — Vegtrafikkloven full text

---

## Overview

**Bæreevneperiode** (bearing capacity period) — also commonly called **teleløsningsperiode** or **teleløsning** — refers to the seasonal period in Norway when frost thaws out of road subbase layers, temporarily reducing road bearing capacity. During this period, Statens vegvesen (Norwegian Public Roads Administration) imposes reduced weight limits on affected roads.

Norway's road network varies significantly in construction standard. Many county roads (fylkesveier), municipal roads, and forest roads are built on frost-susceptible soils and experience significant bearing capacity reduction. Main roads (riksveier) and motorways are generally less affected.

The restrictions are announced by Fylkeskommunen (county authorities) for county roads and by Statens vegvesen for national roads. Each road section may have a different restriction level announced separately.

---

## Timing

| Region | Typical period start | Typical period end | Notes |
|--------|--------------------|--------------------|-------|
| Lowland southern Norway (Østlandet south) | Mid-February–March | April–early May | Earliest thaw in the country |
| Inland Norway (innlandet, Trøndelag) | March–April | May | Frost goes deeper; longer restriction period |
| Western Norway (Vestlandet) | February–March | April | Milder climate; shorter restriction period |
| Northern Norway (Nord-Norge) | April–May | June–July | Latest thaw; restrictions can persist into summer |
| Mountain roads (fjellveier) | May–June | June–August | Some mountain roads restricted or closed the entire winter season |

Restrictions vary year to year depending on frost depth and spring temperature patterns. A cold, dry spring extends the period; a warm, wet spring shortens it.

---

## How Restrictions Are Announced

### Statens vegvesen — Vegtrafikksentralen

The national traffic management centres (Vegtrafikksentralen, VTS) coordinate real-time road information including bæreevneperiode restrictions:
- **VTS contact:** 175 (from Norway); +47 175 (from abroad)
- **Website:** https://www.vegvesen.no/trafikkinformasjon/
- **Vegkart (road map tool):** https://vegkart.atlas.vegvesen.no/

### Fylkeskommunen (County Authorities)

From 2020, many county roads (fylkesveier) were transferred from Statens vegvesen to Fylkeskommunen management. Contact the relevant Fylkeskommune for restrictions on county roads:
- Viken, Innlandet, Vestfold og Telemark, etc. — each publishes own restriction information
- Links vary by county; search "[fylke] bæreevneperiode [year]"

### Road Signs

Restriction signs are posted at the entry point of restricted road sections. The sign shows the maximum permitted axle load and/or total weight for the period. Legally binding regardless of online information.

---

## Weight Restriction Levels

Norway does not use a simple BK-class system for spring thaw (unlike Sweden). Instead, Statens vegvesen announces specific weight limits per road section:

| Restriction level | Typical max axle load | Typical max total weight | Notes |
|-----------------|----------------------|-------------------------|-------|
| Light restriction | 8t per axle | 40–50t total | Applied to roads with moderate frost susceptibility |
| Moderate restriction | 6t per axle | 20–40t total | Standard restriction for many county roads |
| Severe restriction | ≤4t per axle | ≤12t total | Lightly built roads; effectively closes to heavy traffic |
| Road closed | — | — | Some forest and mountain roads closed entirely |

The specific limits are road-specific and announced annually. Always verify for the planned route.

---

## Exemptions

Similar to other Nordic countries, Norway provides exemptions for certain transport categories:

| Category | Exemption basis | Notes |
|----------|----------------|-------|
| **Milk collection** (melketransport) | Vegvesen dispensation | Route-specific; must be applied for in advance via Statens vegvesen |
| **Emergency services** | Blanket exemption | Police, fire, ambulance, rescue |
| **Snowploughing / road maintenance** | Operational exemption | Active operations only |
| **Utility vehicles** (water, electricity, gas) | Dispensation-based | For urgent repairs; apply to Vegvesen or Fylkeskommune |

**Dispensation (dispensasjon):** Operators who need to move heavy loads on restricted roads during bæreevneperiode can apply for dispensation from Statens vegvesen. Applications are processed by the relevant road authority (Vegvesen for national roads; Fylkeskommune for county roads). Lead time varies; emergency dispensations can be granted quickly, routine ones may take days to weeks.

---

## Penalties

Overload violations during bæreevneperiode are treated as standard weight violations under Vegtrafikkloven §13 and the associated overload regulation.

| Violation | Fine (NOK) | Legal basis |
|-----------|-----------|-------------|
| Overload < 5% of restriction limit | NOK 1,000–3,000 | Vegtrafikkloven §31; FOR-1990-01-25-92 |
| Overload 5–10% of restriction limit | NOK 3,000–7,000 | Vegtrafikkloven §31 |
| Overload 10–20% of restriction limit | NOK 7,000–15,000 | Vegtrafikkloven §31 |
| Overload > 20% of restriction limit | NOK 15,000–25,000 + possible prosecution | Vegtrafikkloven §31 |
| Repeat or systematic overloading | Up to NOK 100,000 (operator) | Vegtrafikkloven §31b |

**Important:** Overload is calculated against the **restriction limit**, not the normal permitted weight for the road. A 60t vehicle on a road restricted to 40t is a 50% overload.

Additional consequences:
- Vehicle may be immobilised until overload is resolved (cargo offloaded or vehicle returned)
- Statens vegvesen can require proof of compliance before allowing the vehicle to continue
- Foreign vehicles must be able to pay; advance deposit (depositum) may be required

See also references/countries/no/penalties.md for full penalty schedule.

---

## Practical Guidance for Operators

1. **Check before dispatch:** Consult Vegkart (https://vegkart.atlas.vegvesen.no/) and the VTS website before scheduling runs on secondary roads in spring.
2. **Plan alternative routes:** Motorways (E-roads, major riksveier) are rarely subject to bæreevneperiode restrictions.
3. **Apply for dispensation early:** Milk transport and similar recurring essential transport should apply for dispensation at the start of the season.
4. **Keep documentation:** If operating under dispensation, carry the dispensation document in the vehicle.
5. **Contact VTS 175:** For real-time information about specific road sections.

---

## Implementation Notes for Developers

```
BAEREEVNEPERIODE_START_MONTHS = [2, 3, 4, 5]  # varies by region; Feb–May
BAEREEVNEPERIODE_END_MONTHS = [4, 5, 6, 7]    # varies; April–July
MAP_URL = "https://vegkart.atlas.vegvesen.no/"
VTS_PHONE = "175"
# No standardised national BK system for spring thaw; restrictions are road-specific weight limits
MILK_TRANSPORT_EXEMPTION = true   # dispensation required; route-specific
OVERLOAD_REFERENCE = "restriction limit, not normal road limit"
OVERLOAD_LAW = "Vegtrafikkloven §13 + §31"
```
