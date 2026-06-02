# Framework-to-Country Mapping

Which regulatory framework governs international road transport for each country.

**Last verified: 2026-05-31**

---

## Framework Summary

| Framework | Governing law | Applies when |
|-----------|--------------|-------------|
| **EU Tier 1** | EU Regulations (561/2006, 165/2014, 1071/2009, etc.) | Journey stays entirely within EU/EEA member states |
| **AETR Tier 2** | AETR Agreement (UNECE, 2010 revision) | Journey crosses at least one non-EU AETR contracting party |
| **Standalone Tier 3** | National law only | Country not party to AETR (e.g., US, CA, AU) |

> When AETR applies, it governs the **entire journey** including EU segments — not just the non-EU legs. See `references/aetr/scope.md`.

---

## EU / EEA Countries — Tier 1

EU Regulation 561/2006 and related EU transport law apply directly. All are also AETR signatories but AETR is only triggered when the journey includes a non-EU AETR country.

| Country | Code | EU member | EEA | Notes |
|---------|------|-----------|-----|-------|
| Austria | AT | ✅ | ✅ | |
| Belgium | BE | ✅ | ✅ | |
| Bulgaria | BG | ✅ | ✅ | |
| Croatia | HR | ✅ | ✅ | |
| Cyprus | CY | ✅ | ✅ | Island; no land border with other EU states |
| Czechia | CZ | ✅ | ✅ | |
| Denmark | DK | ✅ | ✅ | |
| Estonia | EE | ✅ | ✅ | |
| Finland | FI | ✅ | ✅ | |
| France | FR | ✅ | ✅ | |
| Germany | DE | ✅ | ✅ | |
| Greece | GR | ✅ | ✅ | Land access via Albania/North Macedonia (AETR triggers) or ferry |
| Hungary | HU | ✅ | ✅ | |
| Ireland | IE | ✅ | ✅ | Island; ferry/air connections |
| Italy | IT | ✅ | ✅ | |
| Latvia | LV | ✅ | ✅ | |
| Lithuania | LT | ✅ | ✅ | |
| Luxembourg | LU | ✅ | ✅ | |
| Malta | MT | ✅ | ✅ | Island |
| Netherlands | NL | ✅ | ✅ | |
| Poland | PL | ✅ | ✅ | |
| Portugal | PT | ✅ | ✅ | |
| Romania | RO | ✅ | ✅ | Borders Ukraine, Moldova (non-EU AETR) |
| Slovakia | SK | ✅ | ✅ | |
| Slovenia | SI | ✅ | ✅ | |
| Spain | ES | ✅ | ✅ | Land border with Morocco (ferry required in practice) |
| Sweden | SE | ✅ | ✅ | |
| Iceland | IS | ❌ | ✅ | EEA; EU rules apply via EEA Agreement |
| Liechtenstein | LI | ❌ | ✅ | EEA; shares customs with Switzerland (AETR) |
| Norway | NO | ❌ | ✅ | EEA; EU rules apply via EEA Agreement |

---

## Non-EU AETR Countries — Tier 2

AETR applies to international operations involving these countries. These are the countries that, when included in a route, trigger AETR for the whole journey.

| Country | Code | EU candidate | Notes |
|---------|------|-------------|-------|
| Albania | AL | ✅ | Western Balkans candidate |
| Armenia | AM | ❌ | South Caucasus; Middle Corridor |
| Azerbaijan | AZ | ❌ | Middle Corridor; Caspian ferry link |
| Belarus | BY | ❌ | ⚠️ EU/UK sanctions since 2022; operations severely restricted |
| Bosnia-Herzegovina | BA | ✅ | Western Balkans candidate |
| Georgia | GE | ✅ | South Caucasus; EU candidate since Dec 2023 |
| Kazakhstan | KZ | ❌ | Middle Corridor; large transit country |
| Kyrgyzstan | KG | ❌ | Central Asia |
| Liechtenstein | LI | ❌ | Note: EEA + AETR; EU rules via EEA for intra-EEA, AETR triggers if route includes non-EU AETR country |
| Moldova | MD | ✅ | EU candidate since Jun 2022; key Ukraine transit corridor |
| Monaco | MC | ❌ | Micro-state; AETR signatory |
| Montenegro | ME | ✅ | Western Balkans candidate (advanced negotiations) |
| Morocco | MA | ❌ | North Africa; EU Association Agreement; ferry crossings to/from Spain |
| North Macedonia | MK | ✅ | Corridor X transit country |
| Russia | RU | ❌ | ⚠️ EU/UK sanctions since 2022; EU-Russia road transport suspended |
| San Marino | SM | ❌ | Micro-state; AETR signatory |
| Serbia | RS | ✅ | Corridor X; key Western Balkans transit country |
| Switzerland | CH | ❌ | Most commonly encountered non-EU AETR trigger for EU operators |
| Tajikistan | TJ | ❌ | Central Asia |
| Tunisia | TN | ❌ | North Africa; EU Association Agreement |
| Turkey | TR | ❌ | Major freight corridor; TIR/bilateral permits |
| Turkmenistan | TM | ❌ | Central Asia |
| Ukraine | UA | ✅ | EU candidate since Jun 2022; major EU-UA freight corridor |
| Uzbekistan | UZ | ❌ | Central Asia |

---

## Standalone Tier 3 Countries

Not AETR signatories. National law only governs; no EU or AETR baseline applies.

| Country | Code | Notes |
|---------|------|-------|
| Australia | AU | National HOS rules (NHVL) |
| Canada | CA | Federal + provincial hours of service |
| United Kingdom | GB | Retained EU law (post-Brexit); similar to EU rules but national framework |
| United States | US | Federal Motor Carrier Safety Regulations (FMCSR) |

> **UK note:** Post-Brexit, the UK retained equivalent rules to EU 561/2006 under national law. AETR applies on UK-EU journeys through a non-EU AETR country (e.g., via Switzerland). Direct UK-EU Channel routes are covered by equivalent UK national rules that mirror AETR/EU standards in practice.

---

## Route Examples

| Route | Framework | Why |
|-------|-----------|-----|
| Stockholm → Copenhagen → Hamburg | EU (561/2006) | All EU countries |
| Stockholm → Oslo → Hamburg | EU (561/2006) | NO is EEA; all Tier 1 |
| Stockholm → Copenhagen → Basel (CH) → Milan | **AETR** | Switzerland triggers AETR for entire route |
| Warsaw → Kyiv | **AETR** | Ukraine is non-EU AETR signatory |
| Munich → Salzburg → Ljubljana → Zagreb | EU (561/2006) | All EU countries |
| Berlin → Belgrade → Skopje → Athens | **AETR** | Serbia + North Macedonia trigger AETR |
| Madrid → Algeciras → (ferry) → Tangier → Casablanca | **AETR** | Morocco triggers AETR; even the Spanish segment |

---

*See also: references/aetr/scope.md (detailed AETR application rules), pipeline/sources/aetr-common.yaml, pipeline/sources/eu-common.yaml*
