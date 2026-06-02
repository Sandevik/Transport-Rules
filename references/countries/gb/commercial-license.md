# United Kingdom — Operator's Licence (O-Licence)

**EU Baseline:** Not applicable — GB is Tier 3 standalone. GB retained EU 1071/2009 requirements as its own operator licensing regime, administered by Traffic Commissioners.

**Sources:**
- https://www.gov.uk/apply-for-a-standard-national-or-international-licence — GOV.UK: Apply for an operator's licence
- https://www.gov.uk/manage-vehicle-operator-licence — GOV.UK: Manage your operator's licence

**Last verified: 2026-05-30**

---

## Overview

Any operator using goods vehicles over **3.5 tonnes GVW** for commercial purposes in Great Britain must hold an **Operator's Licence (O-Licence)**, issued by Traffic Commissioners. The requirements mirror EU 1071/2009 but are administered entirely under UK domestic law.

---

## Licence Types

| Type | Scope |
|------|-------|
| **Standard National** | Goods transport for hire or reward within Great Britain only |
| **Standard International** | Goods transport for hire or reward including international operations |
| **Restricted** | Own goods transport only (not for hire or reward) |

---

## Requirements

Four requirements (mirrors EU 1071/2009):

1. **Establishment** — genuine business presence in Great Britain; operating centre with appropriate facilities
2. **Good Repute** — no serious criminal convictions; no serious transport-related violations; financial probity
3. **Financial Standing** — £8,000 first vehicle + £4,450 each additional vehicle (GB rates, set by Traffic Commissioners)
4. **Professional Competence** — Transport Manager must hold CPC (Certificate of Professional Competence for transport management)

---

## Transport Manager CPC

The Transport Manager (not driver CPC) must pass the Certificate of Professional Competence examination in:
- Civil and commercial law
- Social legislation
- Business and financial management
- Access to the market
- Technical standards

CPC is awarded by OCR or CILT (Chartered Institute of Logistics and Transport) in the UK.

---

## Traffic Commissioners

Seven Traffic Commissioners cover geographical areas of Great Britain. They issue licences, hold public inquiries, and can revoke or suspend licences.

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| GOV.UK | Apply for operator's licence | https://www.gov.uk/apply-for-a-standard-national-or-international-licence |
| GOV.UK | Manage operator's licence | https://www.gov.uk/manage-vehicle-operator-licence |
| Traffic Commissioners | Licence conditions and enforcement | https://www.gov.uk/traffic-commissioner |

---

## Implementation Notes for Developers

```
GB_OLICENSE_THRESHOLD_T = 3.5
GB_FINANCIAL_STANDING_FIRST_GBP = 8000
GB_FINANCIAL_STANDING_ADDITIONAL_GBP = 4450
```
