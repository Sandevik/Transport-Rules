# EU — Commercial Traffic Licensing (Operator Licence + Cabotage)

**EU Baseline:** This IS the EU baseline file. References: EU Regulation 1071/2009 (access to occupation), EU Regulation 1072/2009 (access to market, cabotage).

**Sources:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009R1071 — EU Regulation 1071/2009 (access to occupation of road transport operator)
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009R1072 — EU Regulation 1072/2009 (access to market for international goods transport, cabotage)

**Last verified: 2026-03-19**

---

## Operator Licence — Four Requirements (EU 1071/2009, Art. 3)

Every company conducting professional road transport must satisfy all four conditions:

### 1. Establishment (Art. 5)
The company must be genuinely and stably established in a member state:
- Must have premises where it keeps core business documents
- Must have at least one vehicle registered or authorized in that member state
- Must effectively and continuously manage transport operations from those premises

### 2. Good Repute (Art. 6)
The company and its transport manager must have no disqualifying convictions:
- No serious criminal convictions (fraud, trafficking, drug offences, etc.)
- No serious road traffic violations (repeated speeding, dangerous driving, DUI, etc.)
- No serious violations of road transport regulations (working time, weights, cabotage, etc.)
- Tax compliance

### 3. Financial Standing (Art. 7)

| Vehicle count | Required capital |
|--------------|-----------------|
| First vehicle | **9,000 EUR** |
| Each additional vehicle | **5,000 EUR** |

Demonstrated by: bank guarantee, insurance policy, or certified annual accounts showing net assets.

### 4. Professional Competence (Art. 8)
The company must have at least one **transport manager** who:
- Has passed the approved CPC examination for transport managers
- Is genuinely responsible for the transport operations
- Has a real link to the undertaking (employed, director, owner, or authorised representative)

The transport manager CPC exam covers: civil/commercial law, social law, fiscal law, business and financial management, access to the market, technical standards, road safety.

---

## Types of Authorisation

| Authorisation | Scope | Document |
|--------------|-------|---------|
| National licence | Domestic goods/passenger transport within the member state | National licence document |
| Community licence | International goods transport within EU/EEA (vehicles ≥3.5t) | Community licence + certified true copy per vehicle |
| Driver authorisation | Non-EEA national drivers employed in international transport | Driver authorisation card |

Community licence required for international goods transport by vehicles ≥3.5t (or ≥2.5t from 21 May 2022 under Mobility Package).

---

## Cabotage Rules (EU 1072/2009, Art. 8 — "3-in-7" Rule)

After completing an international delivery into a member state, a carrier may perform up to:
- **3 cabotage operations** within **7 days** of the international delivery in that country
- After the 7-day period: **4-day cooling-off** before the same vehicle can perform cabotage in the same country again (from 21 February 2022)

**Key restrictions:**
- Cabotage must use the same vehicle that performed the international delivery
- All cabotage operations must take place in the destination member state of the international transport
- Combined transport: same cabotage restrictions apply (Mobility Package 2022)

---

## Posting of Workers and Cabotage

Cabotage operations always trigger posting of workers obligations — see `eu/posting-workers.md`.

---

## Enforcement

Member states enforce via:
- ERRU (European Register of Road Transport Undertakings) — shared EU database tracking serious infringements
- National licensing authorities (revoke licence for serious infringements)
- Roadside enforcement (advance payment for missing/incorrect documents varies by country)

---

## Key Regulatory Sources

| Source | Content | URL |
|--------|---------|-----|
| EU Regulation 1071/2009 | Access to occupation | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009R1071 |
| EU Regulation 1072/2009 | Cabotage + Community licence | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009R1072 |

---

## Implementation Notes for Developers

```
FINANCIAL_STANDING_FIRST_VEHICLE_EUR = 9000
FINANCIAL_STANDING_ADDITIONAL_VEHICLE_EUR = 5000
CABOTAGE_MAX_OPERATIONS = 3
CABOTAGE_MAX_DAYS_WINDOW = 7
CABOTAGE_COOLING_OFF_DAYS = 4         # from 21 Feb 2022 (Mobility Package)
COMMUNITY_LICENCE_MIN_WEIGHT_T = 3.5  # reduced to 2.5t from 21 May 2022 for international ops
```

---

*See also: references/eu/posting-workers.md (cabotage triggers posting obligations)*
