# EU — Spring Thaw Weight Restrictions (Seasonal Load Limits)

**EU Baseline:** There is no EU directive mandating spring thaw restrictions. EU Directive 96/53/EC sets annual maximum weights; member states may impose lower limits seasonally under Article 4(4) of that directive.

**Last verified: 2026-06-02**

**Sources:**
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31996L0053 — Directive 96/53/EC (weights and dimensions)
- https://transport.ec.europa.eu/transport-modes/road/road-safety/weights-and-dimensions_en — EC DG MOVE
- https://www.unece.org/trans/main/wp29/wp29wgs/wp29gen/wp29pub.html — UNECE road transport publications

---

## Overview

Spring thaw weight restrictions (known by various national terms: tjällossning in Swedish, bæreevneperiode in Norwegian, kelirikko in Finnish) are **seasonal reductions in permitted vehicle weights** applied when winter frost leaves the ground and road subbase layers thaw unevenly.

During spring thaw, the bearing capacity of unpaved, lightly constructed, and secondary roads can drop to **30–50% of their summer value**. This is because:
- Ice crystals in the soil melt from the top downward
- The upper layer becomes saturated and plastic while the lower layer remains frozen
- This "sandwich" condition dramatically reduces load-bearing capacity
- Standard vehicles that are legal all year can cause severe, costly road damage in this period

### EU Legal Basis

EU Directive 96/53/EC establishes maximum permitted weights and dimensions for vehicles operating internationally within the EU. Article 4(4) explicitly permits member states to impose:
- **Lower weight limits** on roads with insufficient bearing capacity
- **Seasonal restrictions** when road conditions require it

Member states are not required to notify the Commission in advance for routine seasonal restrictions. The restrictions are a recognised national prerogative.

### Affected Regions

Spring thaw restrictions are most significant in countries with harsh winters and roads built on frost-susceptible soils:

| Region | Countries | Typical period | Severity |
|--------|-----------|---------------|----------|
| Nordic | Sweden, Finland, Norway | March–June (varies by latitude) | High — significant network coverage |
| Baltic | Estonia, Latvia, Lithuania | March–May | Moderate to high |
| Central-Eastern Europe | Poland, parts of Belarus, Russia | March–April | Moderate — primarily forest and secondary roads |
| Mountain regions | Parts of Austria, Slovakia | April–May | Localised |

### What Is Restricted

Restrictions typically apply to:
- Axle loads (reduced from standard maximums)
- Total vehicle weight (may be reduced to 50–75% of normal limit)
- Specific road categories (local, forest, and secondary roads most affected; motorways rarely restricted)
- The restrictions are road-specific and published on maps by national road authorities

### What Is NOT Restricted at EU Level

The EU does not:
- Require spring thaw restrictions
- Set minimum or maximum restriction levels
- Mandate a harmonised exemption list
- Specify a seasonal window

All of these are left to national discretion.

---

## National Implementation

For country-specific rules see:
- references/countries/se/spring-weight-restrictions.md — Swedish tjällossning
- references/countries/no/spring-weight-restrictions.md — Norwegian bæreevneperiode
- references/countries/fi/kelirikko.md — Finnish kelirikko (spring thaw restrictions)
- references/countries/lv/spring-weight-restrictions.md — Latvian restrictions
- references/countries/lt/spring-weight-restrictions.md — Lithuanian restrictions
- references/countries/ee/spring-weight-restrictions.md — Estonian restrictions

---

## Penalties

Penalties for violating spring thaw weight restrictions are the same as standard overload penalties in the relevant country. Operators should assume:
- Standard overload fee schedule applies
- Vehicle may be immobilised until compliant
- No separate "spring thaw penalty" category — it is treated as an overload violation

See references/countries/{country}/penalties.md for national penalty amounts.

---

## Implementation Notes for Developers

```
SPRING_THAW_EU_MANDATE = false      # No EU directive requires these restrictions
DIRECTIVE_PERMITS_RESTRICTIONS = true  # Directive 96/53/EC Art. 4(4) allows member state seasonal limits
AFFECTED_REGIONS = ["SE", "FI", "NO", "EE", "LV", "LT", "PL"]  # primary affected countries
TYPICAL_BEARING_CAPACITY_DROP = "30-50%"  # of summer value during thaw
# Always check national authority maps for current restrictions before dispatch
```
