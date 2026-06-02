#!/usr/bin/env python3
"""
Transport-Rules process pipeline.
Reads raw fetched content and uses Claude API to synthesise structured reference markdown files.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

import anthropic
import yaml

PIPELINE_DIR = Path(__file__).parent
SOURCES_DIR = PIPELINE_DIR / "sources"
RAW_DIR = PIPELINE_DIR / "raw"
REPO_ROOT = PIPELINE_DIR.parent
REFERENCES_DIR = REPO_ROOT / "references"
DATA_DIR = REPO_ROOT / "data"

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

EU_FILE_MAP = {
    "driving-rest": "driving-rest-time",
    "hours-of-service": None,  # standalone (US/CA/AU)
    "dimensions-weights": "weights-dimensions",
    "commercial-license": "commercial-licensing",
    "professional-driver": "professional-driver",
    "dangerous-goods": "dangerous-goods",
    "vehicle-inspection": "vehicle-inspection",
    "posting-declaration": "posting-workers",
    "emissions": "emissions",
    "tolls": "road-charging",
    "live-animals": "live-animals",
    "combined-transport": "combined-transport",
}

SYNTHESIS_PROMPT = """\
You are building a transport regulations reference file for the Transport-Rules knowledge base.

Country: {country} ({code})
Framework tier: {tier}
Topic: {topic}
Baseline: {baseline_note}
Today's date: {today}

Raw content scraped from official sources (may include multiple pages separated by ---):
{raw_content}

Source URLs used:
{source_urls}

Write a structured markdown reference file following this EXACT template structure.
Keep it focused and concise. Do NOT duplicate content already in the baseline file.
Only include what is country-specific, different from the baseline, or essential context.

---TEMPLATE---
# {country} — {topic_title}

**{baseline_header}**

**Sources:**
- [list each source URL with description]

**Last verified: {today}**

---

## Overview
[2-3 sentences: what framework applies, who enforces it, one notable national feature]

## [Regulatory sections — use H2 for each major area]
[Tables for limits/fees/thresholds; every number must have inline legal citation]

## Deviations from Baseline
*(Omit this section entirely if no deviations from the baseline exist — just say so in Overview)*

## Enforcement
| Authority | Full name | Website |
[Include advance payment rules if applicable — YES/NO and method]

## Penalties
| Violation | Penalty ({currency}) | Legal basis |

## Key Regulatory Sources
| Source | Content | URL |

## Implementation Notes for Developers
*(Only include if concrete extractable constants exist — omit otherwise)*
---END TEMPLATE---

Rules:
- Cite exact law references (e.g. "§23 StVZO", "Art. 6 EU 561/2006", "49 CFR §395.3")
- Use local currency for penalties — NEVER convert to EUR or SEK
- If EU/AETR baseline fully applies with no national deviation, state that clearly in Overview and keep the file short
- "Last verified" must be: {today}
- Minimum meaningful content: 200 words. If the raw content is insufficient to write 200 words of accurate content, output exactly: INSUFFICIENT_CONTENT
"""


def load_raw(code: str, topic: str) -> tuple[str, list[str]]:
    topic_dir = RAW_DIR / code / topic
    if not topic_dir.exists():
        return "", []
    files = sorted(topic_dir.glob("source_*.txt"))
    texts = [f.read_text(encoding="utf-8", errors="replace")[:10000] for f in files]
    return "\n\n---\n\n".join(texts), [f.name for f in files]


def load_source_urls(manifest: dict, topic: str) -> list[str]:
    sources = manifest.get("topics", {}).get(topic, {}).get("sources", [])
    return [s.get("url", "") for s in sources if s.get("url")]


def determine_baseline(manifest: dict, topic: str) -> tuple[str, str]:
    """Returns (baseline_header, baseline_note) strings for the prompt."""
    tier = manifest.get("framework_tier", 1)
    topic_data = manifest.get("topics", {}).get(topic, {})
    eu_applies = topic_data.get("eu_baseline_applies", False)
    aetr_applies = topic_data.get("aetr_baseline_applies", False)
    standalone = topic_data.get("standalone", False)

    if eu_applies:
        eu_file = EU_FILE_MAP.get(topic, topic)
        header = f"EU Baseline: [references/eu/{eu_file}.md — EU Regulation applies]"
        note = f"EU baseline applies. Only document national deviations, penalties, and enforcement authority."
    elif aetr_applies:
        header = "AETR Baseline: [references/aetr/driving-rest-time.md — AETR Agreement applies for driving/rest]"
        note = "AETR governs driving/rest time. Document how this country implements/enforces AETR plus any national specifics."
    elif standalone or tier == 3:
        header = "Not applicable — standalone national framework (no EU or AETR baseline)"
        note = "This is a standalone national framework. Document it completely — do not reference EU or AETR as baseline."
    else:
        # Default: check tier
        if tier == 1:
            eu_file = EU_FILE_MAP.get(topic, topic)
            header = f"EU Baseline: [references/eu/{eu_file}.md]"
            note = "EU baseline applies. Only document national deviations."
        elif tier == 2:
            header = "Standalone (non-driving/rest topics for AETR countries are standalone national rules)"
            note = "This topic has no supranational baseline for this country. Document national rules fully."
        else:
            header = "Not applicable — standalone national framework"
            note = "Document fully as standalone national rules."

    return header, note


def load_data_facts(topic: str, code: str) -> dict | None:
    """
    Load structured data facts for a jurisdiction, resolving through 3-tier inheritance:
    state/province -> federal -> EU baseline.

    code examples: "se", "us", "us-ca", "au-nsw", "ca-on"
    Topic slug maps to data/{topic}/ directory.
    """
    # Map pipeline topic slugs to data/ directory names
    topic_dir_map = {
        "driving-rest": "driving-rest",
        "dimensions-weights": "dimensions-weights",
        "hours-of-service": "hours-of-service",
        "vehicle-inspection": "inspection",
        "tolls": "road-charging",
        "penalties": "penalties",
        "emissions": "emissions",
        "dangerous-goods": "dangerous-goods",
        "commercial-license": "professional-driver",
    }
    data_topic = topic_dir_map.get(topic, topic)
    base = DATA_DIR / data_topic

    country, _, state = code.partition("-")
    candidates = []
    if state:
        # e.g. "us-ca" -> look in us/states/ca.yaml or us/provinces/ca.yaml
        candidates += [
            base / country / "states" / f"{state}.yaml",
            base / country / "provinces" / f"{state}.yaml",
            base / f"{country}-federal.yaml",
        ]
    else:
        candidates += [
            base / "countries" / f"{code}.yaml",
            base / f"{code}-federal.yaml",
        ]
    candidates += [
        base / "eu-baseline.yaml",
        base / "aetr-baseline.yaml",
    ]

    for path in candidates:
        if path.exists():
            with open(path, encoding="utf-8") as f:
                return yaml.safe_load(f)
    return None


def synthesise(manifest: dict, topic: str, raw_content: str, source_urls: list[str]) -> str:
    code = str(manifest["code"])   # guard against YAML bool coercion (e.g. "no" → False)
    country = manifest["country"]
    currency = manifest.get("currency", "local currency")
    tier = manifest.get("framework_tier", 1)
    today = datetime.today().strftime("%Y-%m-%d")
    baseline_header, baseline_note = determine_baseline(manifest, topic)

    # Load structured data facts for this jurisdiction and inject as ground truth
    data_facts = load_data_facts(topic, code)
    data_facts_block = ""
    if data_facts:
        import json
        data_facts_block = (
            "\n\nStructured data facts (GROUND TRUTH — ensure all tables and values in your output "
            "exactly match these where applicable; do not hallucinate different numbers):\n"
            + "```yaml\n"
            + yaml.dump(data_facts, allow_unicode=True, default_flow_style=False)
            + "```"
        )

    prompt = SYNTHESIS_PROMPT.format(
        country=country,
        code=code,
        tier=tier,
        topic=topic,
        topic_title=topic.replace("-", " ").title(),
        baseline_header=baseline_header,
        baseline_note=baseline_note,
        today=today,
        raw_content=raw_content[:25000] + data_facts_block,
        source_urls="\n".join(f"- {u}" for u in source_urls),
        currency=currency,
    )

    msg = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def process_country(manifest_path: Path, topics_filter: list[str] | None, force: bool):
    manifest = load_yaml(manifest_path)
    code = str(manifest["code"])   # guard against YAML bool coercion (e.g. "no" → False)
    country = manifest["country"]
    print(f"\nProcessing {country} ({code})")

    out_dir = REFERENCES_DIR / "countries" / code
    out_dir.mkdir(parents=True, exist_ok=True)

    for topic in manifest.get("topics", {}):
        if topics_filter and topic not in topics_filter:
            continue

        out_file = out_dir / f"{topic}.md"
        if out_file.exists() and not force:
            print(f"  skip {topic} (file exists — use --force to regenerate)")
            continue

        raw, _ = load_raw(code, topic)
        if not raw:
            print(f"  skip {topic} — no raw content (run fetch.py first)")
            continue

        source_urls = load_source_urls(manifest, topic)
        print(f"  synthesising {topic}...")
        content = synthesise(manifest, topic, raw, source_urls)

        if content.strip() == "INSUFFICIENT_CONTENT":
            print(f"  SKIP {topic} — insufficient content (pipeline returned INSUFFICIENT_CONTENT)")
            continue

        if len(content.strip()) < 200:
            print(f"  SKIP {topic} — output too short ({len(content)} chars)")
            continue

        out_file.write_text(content, encoding="utf-8")
        print(f"  wrote → {out_file.relative_to(REPO_ROOT)}")


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Process raw content into reference markdown")
    parser.add_argument("countries", nargs="*", help="Country codes to process")
    parser.add_argument("--eu", action="store_true", help="Process EU common baseline files")
    parser.add_argument("--aetr", action="store_true", help="Process AETR common baseline files")
    parser.add_argument("--topics", nargs="*", help="Limit to specific topics")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files")
    args = parser.parse_args()

    if args.eu:
        p = SOURCES_DIR / "eu-common.yaml"
        if p.exists():
            process_country(p, args.topics, args.force)

    if args.aetr:
        p = SOURCES_DIR / "aetr-common.yaml"
        if p.exists():
            process_country(p, args.topics, args.force)

    manifests = sorted((SOURCES_DIR / "countries").glob("*.yaml"))
    if args.countries:
        manifests = [m for m in manifests if m.stem in args.countries]

    for mp in manifests:
        process_country(mp, args.topics, args.force)


if __name__ == "__main__":
    main()
