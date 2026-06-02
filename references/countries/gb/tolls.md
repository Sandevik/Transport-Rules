# United Kingdom — Road Tolls and HGV Levy

**EU Baseline:** Not applicable — Tier 3 standalone.

**Sources:**
- https://www.gov.uk/hgv-levy — GOV.UK: HGV Road User Levy
- https://www.gov.uk/dart-charge — GOV.UK: Dartford Crossing charge

**Last verified: 2026-05-30**

---

## Overview

The UK does not operate a general motorway toll for HGVs. Instead, a **mandatory annual HGV Road User Levy** applies to all HGVs ≥12,000 kg entering or operating in the UK. Foreign vehicles must pay before entering. A small number of specific road infrastructure charges (Dartford Crossing, M6 Toll, Mersey Gateway, etc.) also apply.

---

## HGV Road User Levy

| Parameter | Detail |
|-----------|--------|
| Applies to | HGVs with GVW **≥12,000 kg** |
| Foreign vehicles | Must pay **before entering the UK** |
| UK-registered vehicles | Paid as part of vehicle excise duty |
| Zero-emission HGVs | **Exempt** |

**Payment methods:** Credit/debit card, fuel card, prepayment account, bank transfer, PayPal, or phone (+44 33 0101 3725).

Rates vary by vehicle weight, number of axles, and suspension type. Full rate table: https://www.gov.uk/hgv-levy

---

## Specific Infrastructure Tolls

| Location | Applies to | Approximate HGV charge |
|----------|-----------|----------------------|
| Dartford Crossing (A282, Thames) | All vehicles | ~£6.00 per crossing for HGVs |
| M6 Toll (West Midlands) | All vehicles | ~£7–12 for HGVs |
| Mersey Gateway (Halton) | All vehicles | ~£2 per crossing |
| Humber Bridge | All vehicles | ~£12 for HGVs |
| Severn Crossings | Removed 2018 — now free | — |

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| GOV.UK | HGV Road User Levy | https://www.gov.uk/hgv-levy |
| GOV.UK | Dartford Crossing | https://www.gov.uk/dart-charge |

---

## Implementation Notes for Developers

```
GB_HGV_LEVY_THRESHOLD_KG = 12000
GB_HGV_LEVY_ZEV_EXEMPT = True
GB_GENERAL_MOTORWAY_TOLL = False   # No general motorway toll system
```
