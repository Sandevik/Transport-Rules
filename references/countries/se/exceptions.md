# Undantag från kör- och vilotidsreglerna — Exceptions from Driving and Rest Time Rules

**Sources:**
- https://www.transportstyrelsen.se/sv/vagtrafik/yrkestrafik/kor-och-vilotider/regler-om-kor--och-vilotider/undantag-fran-kor--och-vilotider/
- https://www.transportstyrelsen.se/sv/vagtrafik/yrkestrafik/kor-och-vilotider/
- EU Regulation (EG) nr 561/2006, Article 3 (EU exceptions) and Article 13 (national exceptions)

**Last verified: 2026-03-19**

---

## EU Exceptions — Article 3 (Regulation 561/2006)

These vehicles and operations are **fully exempt** from EU driving and rest time rules:

1. **Public transport on short routes**
   - Buses used for passenger transport in scheduled services where route length does not exceed **50 km**

2. **Light vehicles for craftspeople / own use (≤7.5t)**
   - Vehicles ≤7.5t GVW carrying work materials or craft-produced goods to/from the driver's workplace
   - Within **100 km radius** of the company's base
   - Driving must NOT be the driver's main activity
   - No commercial transport compensation paid to the driver
   - Note: Mobility Package (2022) expanded craftsperson exemptions — this is a key derogation for tradespeople

3. **Low-speed vehicles**
   - Vehicles with maximum permitted speed not exceeding **40 km/h**

4. **Defense and emergency services**
   - Military vehicles, civil defense, fire services, rescue, and public order vehicles
   - Owned or rented without a driver, performing official duties

5. **Emergency and humanitarian operations**
   - Vehicles used in emergencies, natural disasters, or humanitarian aid (non-commercial)

6. **Specialized medical vehicles**
   - Ambulances and medical transport providing care during transport

7. **Recovery vehicles (bärgningsfordon)**
   - Specialized towing/breakdown vehicles
   - Within **100 km radius** of their home base

8. **Test and development vehicles**
   - Vehicles undergoing technical testing, repair, or maintenance
   - New or rebuilt vehicles not yet in service

9. **Non-commercial goods transport (≤7.5t)**
   - Private or hobby transport of goods — no payment or business purpose involved

10. **Small commercial vehicles (2.5–3.5t)**
    - Goods transport for own use, without commercial compensation
    - Note: From **1 July 2026**, these ARE covered for **international** transport even without exemption

11. **Historic vehicles (veteranfordon)**
    - Vehicles classified as heritage/veteran (generally 30+ years old)
    - Non-commercial transport only

---

## Swedish National Exceptions — Article 13 (Regulation 561/2006)

Sweden has exercised its right under Article 13 to grant national exceptions for **domestic transport only**. These do NOT apply when the vehicle crosses into another EU/EEA member state.

| Category | Condition / Radius |
|----------|--------------------|
| Agricultural and forestry operations | Within **100 km radius** of the farm or forest enterprise |
| Agricultural tractors (all uses) | Always exempt (all distances) |
| Island operations | Islands ≤**2,300 km²** with no fixed land bridge connection (e.g., Gotland is excluded — it has ferry connection but no bridge, so check current rules) |
| Driving instruction and license testing | All instructional driving, all distances |
| Infrastructure maintenance | Sewage, water, gas, electricity, road maintenance, waste collection, telecommunications, broadcasting — domestic only |
| Non-commercial passenger transport | Vehicles designed for max **10–17 persons** (including driver), non-profit basis |
| Milk collection/delivery from farms | Including return of containers and distribution of animal feed to farms |
| Animal waste transport | No radius limit stated |
| Live animal transport | To markets or slaughterhouses within **100 km radius** |
| Circus equipment transport | No specific radius |
| Eco-friendly vehicles | Natural gas, LPG, or electric-powered; ≤7.5t; within **100 km radius** of base |

**Important:** National exceptions apply **only within Sweden**. If the vehicle crosses into another EU country, EU 561/2006 rules apply in full for the entire journey.

---

## Light Vehicles in Domestic Transport

Vehicles ≤3.5t used **domestically** are NOT covered by EU 561/2006. They are instead governed by **Förordning 1994:1297** (rest time rules for light vehicles — vilotidsregler för lätta fordon). See `light-vehicles.md`.

Key rule: Drivers must have at least **11 hours rest** per 24-hour period, and must maintain a personal logbook (personlig tidbok).

Exception within light vehicles: Drivers whose driving time stays under **4 hours 30 minutes** per 24-hour period need not maintain logbooks.

---

## Change from 1 July 2026

From **1 July 2026**, international goods transport with vehicles weighing **2.5–3.5 tonnes** will fall under EU 561/2006 **unless covered by an exemption**. This means:
- Swedish light van drivers doing international runs (to Norway, Germany, etc.) will need tachographs and must follow EU driving/rest time rules
- The craft/own-use exemption and other Article 3 exemptions still apply even to 2.5–3.5t vehicles if conditions are met

---

## Interaction with AETR

If a journey passes through a non-EU country that has signed AETR (e.g., Turkey, Russia, Morocco, Kazakhstan), AETR rules apply for the **entire journey** — no national exceptions based on Article 13 apply when AETR governs.

EU Article 3 exemptions (universal exemptions) continue to apply even on AETR routes if the vehicle qualifies (e.g., defense vehicles, emergency services).

---

## Implementation Notes for Developers

Key exemption checks to implement:
- `vehicle_gvw <= 3500` AND `transport == 'domestic'` → light vehicle rules, not EU 561/2006
- `vehicle_gvw <= 7500` AND `craft_own_use == true` AND `radius_km <= 100` AND `not_main_activity == true` → Article 3 exemption
- `max_speed_kmh <= 40` → always exempt
- `is_military_or_emergency` → exempt
- `is_agricultural` AND `radius_km <= 100` → national exemption (domestic only)
- `is_historical_vehicle` AND `non_commercial` → exempt
- `route_passes_aetr_country` → AETR applies for entire journey, national exemptions do not apply
- From 2026-07-01: `vehicle_gvw >= 2500` AND `vehicle_gvw <= 3500` AND `international` → check for applicable Article 3 exemption, otherwise EU 561/2006 applies
