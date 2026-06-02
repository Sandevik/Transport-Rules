# ATP — Agreement on the International Carriage of Perishable Foodstuffs

**Sources:**
- https://unece.org/transport/road-transport/atp-perishable-foodstuffs — UNECE: ATP Agreement text and signatories
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:41970A0901 — ATP Agreement (published in OJ)
- https://www.iru.org/resources/iru-library/atp-handbook — IRU: ATP Handbook

**Last verified: 2026-06-01**

---

## Overview

The **ATP Agreement** (Agreement on the International Carriage of Perishable Foodstuffs and on the Special Equipment to be Used for Such Carriage) is a UNECE multilateral treaty governing the technical requirements for vehicles, containers, and equipment used to transport perishable foodstuffs internationally. It sets equipment classes, temperature performance requirements, inspection and certification procedures, and markings. All EU member states plus many AETR countries are ATP signatories. ATP certification is mandatory for **international** transport of perishable food; member states may also apply ATP nationally.

---

## Scope

ATP applies to the **international carriage of perishable foodstuffs by road, rail, or inland waterway** when the transport involves at least two signatory countries. Quick-frozen foodstuffs, ice cream, dairy products, fish, meat, fruit, vegetables, and other temperature-sensitive foods are covered.

**Not required for:** domestic carriage (within one signatory country), non-perishable goods, or transport below the exemption thresholds.

---

## Equipment Classes

ATP defines equipment by **insulation performance** (thermal coefficient K) and **refrigeration capacity**:

### Insulated Equipment (I)

| Class | Code | K value | Description |
|---|---|---|---|
| Insulated Normal | IN | K ≤ 0.70 W/m²K | Basic insulation; no refrigeration |
| Insulated Reinforced | IR | K ≤ 0.40 W/m²K | Better insulation; no refrigeration |

### Refrigerated Equipment (F — Isotherme Réfrigéré)

| Class | Code | Temp range | Description |
|---|---|---|---|
| Fresh A | FNA | +12°C to 0°C | Refrigerated with ice/eutectic plates |
| Fresh B | FNB | +12°C to –10°C | Refrigerated with ice/eutectic, lower temp |
| Fresh C | FNC | +12°C to –20°C | Refrigerated, very low temp |

### Mechanically Refrigerated Equipment (F — Frigorifique)

| Class | Code | Interior temp | Description |
|---|---|---|---|
| Fresh A | FRA | Max +7°C (air) | Mechanically cooled; common for chilled meat, dairy |
| Fresh B | FRB | Max 0°C (air) | Mechanically cooled; chilled fish |
| Fresh C | FRC | Max –10°C (air) | Mechanically cooled; frozen products |
| Deep frozen A | FDA | Max –20°C | Mechanically cooled; deep frozen goods |
| Deep frozen B | FDB | Max –20°C (+ 3-phase loading exception) | Deep frozen with loading allowance |

### Heated Equipment (C)

| Class | Code | Min temp | Description |
|---|---|---|---|
| Heated A | CNA | Min +12°C | Heated equipment (winter transport of food) |
| Heated B | CNB | Min +12°C (to –20°C ambient) | Higher performance heated |

---

## Required Transport Temperatures

| Food category | Required temperature | ATP class needed |
|---|---|---|
| Quick-frozen food | ≤ –18°C | FDA or FDB |
| Ice cream | ≤ –20°C | FDA or FDB |
| Frozen fish | ≤ –18°C | FDA |
| Chilled beef/veal | 0°C to +2°C | FRA minimum |
| Chilled poultry | 0°C to +4°C | FRA minimum |
| Chilled dairy (milk) | 0°C to +6°C | FRA minimum |
| Butter | 0°C to +6°C | FRA minimum |
| Hard cheese | 0°C to +6°C | FRA minimum |
| Fresh fish (non-frozen) | 0°C to +2°C | FRA minimum |
| Eggs | +5°C to +8°C | FNA or FRA |
| Fruit and vegetables | +2°C to +12°C | FNA minimum |

---

## ATP Certificate and Inspection

### Certificate Requirements

Every piece of ATP-certified equipment must carry a valid ATP certificate issued by the national competent authority. The certificate must:
- Specify the equipment class (e.g., FRC, FRA, FDA)
- Show the effective temperature maintained
- Include the equipment serial number and chassis number
- Show issue date and **expiry date**
- Be referenced on the transport document (CMR consignment note)

### Inspection Intervals

| Equipment age | Inspection type | Interval |
|---|---|---|
| New equipment (0–6 years) | Initial test + first periodic test | Every **3 years** |
| Equipment > 6 years old | Subsequent periodic tests | Every **3 years** (some countries: annually for older equipment) |
| After major repair/modification | Recertification | Immediately after repair |

**Note:** Certificates issued to equipment > 6 years old are typically valid for 3 years but some national competent authorities apply annual inspection requirements for equipment in poor condition.

---

## Markings on Vehicle

ATP-certified equipment must display a **distinctive marking plate** on the outside showing:

- Letters **ATP**
- Equipment class code (e.g., **FRC**, **FRA**, **FDA**)
- Expiry date of the certificate (month/year)
- Country code of issuing authority
- Certificate number

Example marking: `ATP FRC 03-28 D 12345678`
(ATP class FRC, valid until March 2028, Germany, certificate no.)

---

## Signatory Countries

All EU member states, plus: Norway, Switzerland, Turkey, Ukraine, Belarus, Russia, Morocco, Kazakhstan, Uzbekistan, Tajikistan, Kyrgyzstan, Georgia, Azerbaijan, Albania, Montenegro, North Macedonia, Serbia, Bosnia-Herzegovina, and others. Full list at UNECE.

---

## Enforcement

| Situation | Requirement |
|---|---|
| International transport of perishable food | Valid ATP certificate required on vehicle |
| Certificate presented on request | Must be shown to inspectors at border crossings |
| Temperature recording | Temperature loggers/recorders required for most classes; records available for inspection |
| CMR consignment note | ATP certificate number should be noted on CMR |

---

## Penalties

| Violation | Consequence |
|---|---|
| Transporting without valid ATP certificate | Prohibition from continuing transport; unloading required; national fine |
| Equipment operating outside certified temperature range | Product seizure; fine; carrier liability for goods loss |
| Expired ATP certificate | Same as no certificate — prohibition + fine |

National fines vary. See country-specific files for amounts in local currency.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| UNECE | ATP Agreement and protocols | https://unece.org/transport/road-transport/atp-perishable-foodstuffs |
| UNECE | ATP contracting parties | https://treaties.un.org/ |
| IRU | ATP Handbook | https://www.iru.org/resources/iru-library/atp-handbook |
| EU Official Journal | ATP Agreement text (EU version) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:41970A0901 |

## Implementation Notes for Developers

```
ATP_INSPECTION_INTERVAL_YEARS = 3          # both new and older equipment
ATP_CERTIFICATE_REFERENCE = "note_in_cmr"  # must appear on CMR waybill
ATP_CLASSES_FROZEN = ["FDA", "FDB"]        # deep frozen ≤ -20°C
ATP_CLASSES_FROZEN_LIGHT = ["FRC", "FNB"]  # ≤ -10°C to -20°C
ATP_CLASSES_CHILLED = ["FRA", "FNA"]       # 0°C to +7°C
ATP_MAX_TEMP_FROZEN_C = -18                # minimum quick-frozen requirement
ATP_MAX_TEMP_DEEP_FROZEN_C = -20           # ice cream, some fish
```
