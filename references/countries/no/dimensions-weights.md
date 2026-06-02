# Norway — Vehicle Dimensions and Weights

**EU Baseline:** [references/eu/weights-dimensions.md — Directive 96/53/EC] with Nordic exception deviations.

**Sources:**
- https://www.vegvesen.no/en/vehicles/professional-transport/list-of-roads-and-dimensions/ — Statens vegvesen: Roads and dimensions
- https://www.vegvesen.no/en/vehicles/professional-transport/list-of-roads-and-dimensions/modular-vehicle-combinations/ — Statens vegvesen: Modular vehicle combinations

**Last verified: 2026-05-30**

---

## Overview

Norway applies the EU Directive 96/53/EC limits for international transport but, as an EEA member benefiting from the Nordic exception (Article 4a), also permits heavier and longer modular vehicle combinations on a designated national road network. Maximum permitted combination: **25.25m length, 60 tonnes GVW**.

---

## Standard Limits (EU Directive 96/53/EC)

For international transport, standard EU limits apply — see `references/eu/weights-dimensions.md`.

---

## Norwegian Modular Vehicle Combinations (Vogntog)

| Parameter | Limit |
|-----------|-------|
| Maximum length | **25.25 metres** |
| Maximum GVW | **60 tonnes** |
| Conformity | Must comply with Directive 96/53/EC structural requirements |

**Approved configurations (three types):**
1. N2/N3 motor vehicle + converter dolly + O3/O4 semi-trailer
2. N2/N3 motor vehicle + O3/O4 semi-trailer + O3/O4 simple trailer
3. N2/N3 motor vehicle + O3/O4 semi-trailer (with swap body/container) + O3/O4 semi-trailer

---

## Approved Road Network

Modular combinations **may only operate on the approved road network** — they are not permitted on general public roads outside the designated network.

The approved network comprises **22 main road sections** plus connecting sections, drawing from European routes (E-roads), national highways, county roads, and municipal roads.

**Check current approved network:** https://www.vegvesen.no/en/vehicles/professional-transport/list-of-roads-and-dimensions/

---

## Deviations from EU Baseline

| Topic | EU standard (96/53/EC) | Norway |
|-------|----------------------|--------|
| Maximum GVW | 44t (international), 40t general | **60t** (on approved network, Nordic exception) |
| Maximum length | 18.75m (road train) | **25.25m** (on approved network) |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| Statens vegvesen | Dimensions overview and approved network map | https://www.vegvesen.no/en/vehicles/professional-transport/list-of-roads-and-dimensions/ |
| Statens vegvesen | Modular vehicle combination rules | https://www.vegvesen.no/en/vehicles/professional-transport/list-of-roads-and-dimensions/modular-vehicle-combinations/ |
| Directive 96/53/EC | EU baseline weights/dimensions | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31996L0053 |

---

## Implementation Notes for Developers

```
NO_MAX_LENGTH_MODULAR_M = 25.25
NO_MAX_GVW_MODULAR_T = 60
NO_MODULAR_APPROVED_NETWORK_ONLY = True   # not permitted on general roads
NO_MODULAR_CONFIGS_COUNT = 3
```
