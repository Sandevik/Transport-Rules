# Transport Cost Calculation and Freight Rate Structures

**Sources:**
- https://www.cnr.fr — CNR (Comité National Routier): French freight cost indices
- https://www.balm.bund.de — BALM: German operational cost and toll data
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L0362 — Eurovignette Directive 2022/362/EU

**Last verified: 2026-06-02**

---

## Overview

Understanding how transport costs are structured and how freight rates are calculated is essential for transport operators, logistics buyers, and developers building transport management systems. This file covers the cost components of road freight, standard freight rate structures, variable charge mechanisms (fuel surcharges, toll surcharges), and benchmarks. Note: actual rates are commercial and highly variable — figures here are indicative benchmarks based on published industry data.

---

## Cost Components (Carrier Perspective)

### Fixed Costs (per vehicle per year — indicative, 44t articulated, Euro VI, 2025/2026)

| Cost item | Typical range (EUR/year) | Notes |
|---|---|---|
| Vehicle depreciation (truck) | €15,000–25,000 | Depends on purchase price, residual value, depreciation period (typically 5–8 years) |
| Trailer depreciation | €4,000–8,000 | |
| Insurance (MTPL + comprehensive + cargo) | €8,000–15,000 | Varies hugely by claims history and coverage level |
| Road tax / HGV levy | €1,000–4,000 | Varies by country; SE: fordonsskatt; DE: Kraftfahrzeugsteuer; GB: HGV levy |
| Annual vehicle inspection | €500–1,000 | |
| Operator licence / O-licence fee | €200–500 | |
| Finance charges (if leased) | Variable | Often 20–35% of fixed cost total |

**Total fixed costs per vehicle:** approx. €30,000–55,000/year

### Variable Costs (per km — indicative, 44t articulated)

| Cost item | Typical range (EUR/km) | Notes |
|---|---|---|
| **Fuel** | €0.35–0.50 | Largest single variable cost; diesel at €1.40–1.80/litre; avg consumption 32–38 litres/100km |
| Driver wages + social costs | €0.30–0.50 | Including employer social contributions; varies by country |
| Tyres | €0.05–0.08 | Drive axle: 120,000–160,000 km; replace every 2–3 years |
| Maintenance and repairs | €0.05–0.10 | Preventive + corrective; increases with vehicle age |
| Tolls | €0.05–0.35 | Highly variable by route and country; DE: €0.19–0.35/km; AT: €0.17–0.22/km; FR: €0.10–0.20/km |
| AdBlue (DEF) | €0.01–0.02 | Euro VI: approx. 2–5% of fuel consumption |

**Total variable cost per km:** approx. €0.80–1.50/km

### Overhead / Indirect Costs

| Cost item | % of total cost |
|---|---|
| Management, admin, IT | 8–12% |
| Premises (depot, office) | 3–6% |
| Finance charges, insurance | Included in fixed |
| Sales and marketing | 2–4% |

**Typical total cost per km (loaded, 44t articulated, 2025):** €1.60–2.20/km

---

## Freight Rate Structures

### Full Truckload (FTL)

| Pricing basis | Description |
|---|---|
| Per km | Common for point-to-point; rate × distance = price |
| Per load | Fixed price per truck regardless of distance |
| Per tonne | Per tonne of cargo weight |

**Benchmark FTL rates (2025, indicative):**
- SE ↔ DE (1,000 km): €1,800–2,500 per truck
- SE → PL (1,400 km): €2,200–3,000 per truck
- DE ↔ FR (600 km): €1,200–1,800 per truck
- GB ↔ DE (1,100 km including Channel): €2,500–4,000 per truck (higher post-Brexit customs costs)

### Groupage / LTL (Less Than Truckload)

Charged per **pallet** or per **100 kg**:
- Domestic (e.g., SE internal): SEK 200–600 per pallet
- European groupage: €50–150 per pallet depending on distance, weight

### Spot vs. Contract Rates

| Type | Pricing | Stability |
|---|---|---|
| Contract (annual) | Agreed annual rate; typically lower | Volume committed by shipper |
| Spot market | Market rate at time of booking; typically 20–40% above contract in tight capacity | No commitment |

---

## Variable Surcharges

### Fuel Surcharge

The fuel surcharge adjusts freight rates with fluctuating diesel prices. Standard mechanism:

1. **Reference fuel price** established in contract (e.g., €1.30/litre diesel)
2. **Trigger band:** current price vs. reference price
3. **Surcharge %:** for every X cents above reference, rate increases by Y%
4. **Update frequency:** monthly or quarterly; published by CNR (FR), BALM (DE), TLN (NL)

**Published indices:**
- **FR:** CNR (Comité National Routier) — monthly fuel cost index for French road freight
- **DE:** BALM operational costs index — quarterly; includes toll and wage components
- **NL:** TLN cost model
- **SE:** Transportföretagen / Priceindex

### Toll Surcharge

Operators pass through actual toll costs. Methods:
- Route-specific toll cost added as line item on invoice
- Per-km toll surcharge added to base rate (e.g., +€0.20/km for DE Autobahn routes)
- Common on DE/AT/CH/FR/PL/BE routes

### ADR / Dangerous Goods Surcharge

| Goods type | Typical surcharge |
|---|---|
| ADR goods (general) | +15–25% on base rate |
| Tanker transport (liquids) | Separate pricing — ADR tanker rates typically 40–80% higher than standard due to equipment and training costs |
| Class 1 (explosives) | Highly specific; typically contracted separately |

### Temperature-Controlled (ATP) Surcharge

| Transport type | Typical surcharge vs. standard |
|---|---|
| Refrigerated (+2°C to +8°C) | +25–40% |
| Deep frozen (< –18°C) | +30–50% |
| Multi-temperature | +30–50% |

---

## Load Factor and Utilisation

Key metric for transport efficiency:

| Metric | Formula | Target |
|---|---|---|
| Load factor | Laden km / total km | > 80% |
| Utilisation | Revenue-generating hours / available hours | > 70% |
| Empty running | Empty km / total km | < 20% |
| Revenue per km | Total revenue / total km | > cost per km + margin |

**Backhaul rates:** Return journey rates often 50–70% of outbound rate due to market imbalance; operators seek backhaul cargo to improve load factor.

---

## Cost Index References

| Organisation | Index | Scope | URL |
|---|---|---|---|
| CNR (FR) | Monthly cost index (gazole, labour, tolls) | French road freight | https://www.cnr.fr |
| BALM (DE) | Operational cost development index | German road freight | https://www.balm.bund.de |
| TLN (NL) | CAO kostprijscalculator | Dutch road freight | https://www.tln.nl |
| Transportföretagen (SE) | Cost index | Swedish road freight | https://www.transportforetagen.se |

---

## Penalties

Not applicable — this is a commercial/operational topic, not a regulatory compliance topic. Underpayment of freight rates may lead to commercial disputes; see domestic freight contract files (`se/domestic-freight-contract.md`, `de/domestic-freight-contract.md`) for liability frameworks.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| CNR | French freight cost indices | https://www.cnr.fr |
| BALM | German operational cost data | https://www.balm.bund.de |
| Eurovignette Directive | Road charging EU framework | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L0362 |
