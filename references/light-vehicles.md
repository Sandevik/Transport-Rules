# Vilotidsregler för lätta fordon — Rest Time Rules for Light Vehicles

**Sources:**
- https://www.transportstyrelsen.se/sv/vagtrafik/yrkestrafik/vilotidsregler-for-latta-fordon/
- Förordning (1994:1297) om vilotid för vissa förare

**Last verified: 2026-03-19**

---

## Scope — Which Vehicles Are Covered

These rules apply to vehicles used for **domestic Swedish transport** where the vehicle's maximum permitted total weight (including trailer) does **not exceed 3.5 tonnes**. Specifically:

| Transport type | Covered |
|---------------|---------|
| Goods transport (excluding mail) — max weight ≤3.5t | Yes |
| Taxi services under the Taxi Traffic Act | Yes |
| School transport — max 9 persons including driver | Yes |
| Milk transport from farms; return of containers; animal feed | Yes |

**Not covered:** These rules do NOT apply if the vehicle and driver are subject to EU Regulation 561/2006 (heavy vehicles >3.5t or buses). From **1 July 2026**, light vehicles (2.5–3.5t) conducting **international** transport will instead fall under EU 561/2006.

**Logbook exemption:** Drivers whose driving time is under **4 hours 30 minutes** per 24-hour period need not maintain a personal logbook.

---

## Daily Rest Requirements

Drivers must have **at least 11 hours of rest** during each 24-hour period before performing transport.

**Split rest option:** Daily rest may be divided into two periods:
- First period: any length
- Second period: minimum **8 consecutive hours**
- Total must equal at least **11 hours**

The split option means the driver can have a shorter initial period as long as one block is ≥8 hours and the total ≥11 hours.

There is no weekly rest requirement defined in the light vehicle rules (unlike EU 561/2006). The 11h daily rest is the primary obligation.

---

## Documentation — Personal Logbook (Personlig tidbok)

Drivers must maintain a **personal logbook** (personlig tidbok) during all covered transport.

### What the logbook must contain

- Driver's name and address on each page
- Start and end times of each daily rest period
- Records covering the **7 most recent calendar days** when entries are required

### How to make corrections

- Cross out errors; write the correct information above or below the crossed-out text
- Do not use correction fluid or stickers

### Driver obligations

| Obligation | Detail |
|-----------|--------|
| Carry logbook | Must be present during all transport |
| Present on request | Must show to police or vehicle inspectors |
| Return completed books | Return to employer within one week of completion |
| Return immediately on leaving employment | Even if logbook is incomplete |

### Employer obligations

| Obligation | Detail |
|-----------|--------|
| Provide logbooks | Must include company name, address, and phone number pre-printed |
| Record issuance | Note issue date and driver name for each logbook |
| Record return | Note return date |
| Maintain register | Keep a registry of all driver logbooks issued |
| Retain records | Minimum **12 months** after return/completion |
| Produce on request | Must provide to authorities on demand |

---

## Tachograph as Alternative

If the vehicle is equipped with an **approved and functioning tachograph**, it may replace the personal logbook. Requirements vary by tachograph type:
- **Analog tachograph (diagramblad):** Driver must set the mode switch correctly; charts must be labelled with driver name, date, start/end locations
- **Digital tachograph:** Driver card must be inserted; mode switch used correctly
- **Smart tachograph:** Driver card inserted; border crossing recording active

The driver must still follow all tachograph operating rules (correct mode selection, card insertion, etc.).

---

## Relationship to Taxi Rules

Taxi drivers (under taxitrafiklagen) are covered by these light vehicle rest rules — not EU 561/2006 — since taxis use vehicles ≤3.5t. Both the driver and the employer share responsibility for compliance. See `taxi.md` for taxi-specific rules.

---

## Relationship to Road Working Time

Drivers of light vehicles (≤3.5t) are **NOT** covered by the Road Working Time Act (SFS 2005:395), which only applies to vehicles subject to EU 561/2006. However, they may be covered by the general Swedish Working Hours Act (Arbetstidslagen, SFS 1982:673) if employed.

---

## Penalties

Violations of the light vehicle rest rules are subject to sanctions under the Yrkestrafik framework:
- Drivers failing to maintain or carry logbooks: fines
- Employers who fail to maintain logbook registries or comply with documentation obligations: fines
- See `sanctions-penalties.md` for the general sanction framework

---

## Implementation Notes for Developers

```
LIGHT_VEHICLE_MAX_GVW_KG = 3500
DAILY_REST_MIN_H = 11
DAILY_REST_SPLIT_SECOND_PERIOD_MIN_H = 8
LOGBOOK_LOOKBACK_DAYS = 7
LOGBOOK_RETENTION_MONTHS = 12
LOGBOOK_EXEMPT_IF_DRIVING_UNDER_H = 4.5
TACHOGRAPH_CAN_REPLACE_LOGBOOK = true
INTERNATIONAL_COVERED_FROM = '2026-07-01'  # 2.5-3.5t international transport → EU 561/2006
```
