#!/usr/bin/env python3
"""
Transport-Rules verify pipeline.
Checks coverage, mandatory sections, stale dates, and URL reachability.
"""

import argparse
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests
import yaml

PIPELINE_DIR = Path(__file__).parent
SOURCES_DIR = PIPELINE_DIR / "sources"
REPO_ROOT = PIPELINE_DIR.parent
REFERENCES_DIR = REPO_ROOT / "references"
DATA_DIR = REPO_ROOT / "data"

REQUIRED_SECTIONS = ["## Overview", "**Last verified:", "**Sources:", "## Penalties"]
WARN_DAYS = 90
ERROR_DAYS = 180


def check_file(path: Path) -> list[str]:
    """Returns list of issues found in a reference file."""
    issues = []
    content = path.read_text(encoding="utf-8", errors="replace")

    for section in REQUIRED_SECTIONS:
        if section not in content:
            issues.append(f"missing section: {section!r}")

    # Check Last verified date
    m = re.search(r"\*\*Last verified: (\d{4}-\d{2}-\d{2})", content)
    if m:
        try:
            verified = datetime.strptime(m.group(1), "%Y-%m-%d")
            age = (datetime.today() - verified).days
            if age > ERROR_DAYS:
                issues.append(f"STALE ({age} days old — error threshold {ERROR_DAYS})")
            elif age > WARN_DAYS:
                issues.append(f"aging ({age} days old — warn threshold {WARN_DAYS})")
        except ValueError:
            issues.append("invalid Last verified date format")
    else:
        issues.append("no Last verified date found")

    return issues


def check_url(url: str) -> bool:
    try:
        resp = requests.head(url, timeout=15, allow_redirects=True,
                             headers={"User-Agent": "TransportRulesVerifier/2.0"})
        return resp.status_code < 400
    except requests.RequestException:
        return False


def check_data_files() -> list[str]:
    """Check data/ layer for required header fields and last_verified staleness."""
    issues = []
    required_fields = {"jurisdiction", "topic", "regulation", "last_verified"}
    if not DATA_DIR.exists():
        return ["data/ directory does not exist"]

    for yaml_file in sorted(DATA_DIR.rglob("*.yaml")):
        try:
            with open(yaml_file, encoding="utf-8") as f:
                content = yaml.safe_load(f)
            if not isinstance(content, dict):
                continue
            # Skip vehicle-classes.yaml (has different structure)
            if yaml_file.name == "vehicle-classes.yaml":
                continue
            missing = required_fields - set(content.keys())
            if missing:
                issues.append(f"data/{yaml_file.relative_to(DATA_DIR)}: missing fields {missing}")
            # Check last_verified staleness
            lv = content.get("last_verified")
            if lv:
                try:
                    age = (datetime.today() - datetime.strptime(str(lv), "%Y-%m-%d")).days
                    if age > ERROR_DAYS:
                        issues.append(f"data/{yaml_file.relative_to(DATA_DIR)}: STALE ({age} days old)")
                    elif age > WARN_DAYS:
                        issues.append(f"data/{yaml_file.relative_to(DATA_DIR)}: aging ({age} days)")
                except ValueError:
                    issues.append(f"data/{yaml_file.relative_to(DATA_DIR)}: invalid last_verified format")
        except Exception as e:
            issues.append(f"data/{yaml_file.relative_to(DATA_DIR)}: parse error — {e}")
    return issues


def print_data_coverage():
    """Print summary count of data/ structured files by topic."""
    if not DATA_DIR.exists():
        print("  data/ directory not found")
        return
    print("\n=== DATA LAYER COVERAGE ===")
    total = 0
    for topic_dir in sorted(DATA_DIR.iterdir()):
        if not topic_dir.is_dir():
            continue
        count = len(list(topic_dir.rglob("*.yaml")))
        total += count
        print(f"  {topic_dir.name:<25} {count} files")
    print(f"  {'TOTAL':<25} {total} data files")


def print_coverage():
    """Print which country files exist vs expected from manifests."""
    print("\n=== COVERAGE MAP ===")
    country_dir = SOURCES_DIR / "countries"
    manifests = sorted(country_dir.glob("*.yaml"))

    total_expected = 0
    total_found = 0

    for mp in manifests:
        with open(mp, encoding="utf-8") as f:
            manifest = yaml.safe_load(f)
        code = str(manifest.get("code", mp.stem))
        country = manifest.get("country", code.upper())
        topics = manifest.get("topics", {})
        ref_dir = REFERENCES_DIR / "countries" / code

        found = []
        missing = []
        for topic in topics:
            fp = ref_dir / f"{topic}.md"
            if fp.exists():
                found.append(topic)
            else:
                missing.append(topic)

        total_expected += len(topics)
        total_found += len(found)

        status = "✅" if not missing else f"⚠️  missing: {', '.join(missing)}"
        print(f"  {code.upper():4} {country:<25} {len(found)}/{len(topics)} topics  {status}")

    print(f"\n  Total: {total_found}/{total_expected} topic files exist")


def main():
    parser = argparse.ArgumentParser(description="Verify reference file coverage and quality")
    parser.add_argument("--urls", action="store_true", help="Check URL reachability (slow, rate-limited)")
    parser.add_argument("--coverage", action="store_true", help="Print coverage map only")
    args = parser.parse_args()

    if args.coverage:
        print_coverage()
        print_data_coverage()
        return

    issues_found = 0

    # Check EU files
    eu_dir = REFERENCES_DIR / "eu"
    if eu_dir.exists():
        print("\n=== EU BASELINE FILES ===")
        for f in sorted(eu_dir.glob("*.md")):
            issues = check_file(f)
            status = "✅" if not issues else f"❌ {'; '.join(issues)}"
            print(f"  eu/{f.name:<35} {status}")
            if issues:
                issues_found += len(issues)

    # Check AETR files
    aetr_dir = REFERENCES_DIR / "aetr"
    if aetr_dir.exists():
        print("\n=== AETR BASELINE FILES ===")
        for f in sorted(aetr_dir.glob("*.md")):
            issues = check_file(f)
            status = "✅" if not issues else f"❌ {'; '.join(issues)}"
            print(f"  aetr/{f.name:<33} {status}")
            if issues:
                issues_found += len(issues)

    # Check country files
    countries_dir = REFERENCES_DIR / "countries"
    if countries_dir.exists():
        print("\n=== COUNTRY FILES ===")
        for country_dir in sorted(countries_dir.iterdir()):
            if not country_dir.is_dir():
                continue
            code = country_dir.name
            for f in sorted(country_dir.glob("*.md")):
                issues = check_file(f)
                status = "✅" if not issues else f"❌ {'; '.join(issues)}"
                print(f"  {code}/{f.name:<33} {status}")
                if issues:
                    issues_found += len(issues)

    # Check data/ structured layer
    print("\n=== DATA LAYER CHECKS ===")
    data_issues = check_data_files()
    if data_issues:
        for issue in data_issues[:20]:   # cap output to first 20 issues
            print(f"  ❌ {issue}")
        if len(data_issues) > 20:
            print(f"  ... and {len(data_issues) - 20} more issues")
        issues_found += len(data_issues)
    else:
        print("  ✅ All data/ files have required header fields")
    print_data_coverage()

    print_coverage()

    if args.urls:
        print("\n=== URL REACHABILITY CHECK ===")
        checked = 0
        failed = 0
        country_dir = SOURCES_DIR / "countries"
        for mp in sorted(country_dir.glob("*.yaml")):
            with open(mp, encoding="utf-8") as f:
                manifest = yaml.safe_load(f)
            code = manifest.get("code", mp.stem)
            for topic, tdata in manifest.get("topics", {}).items():
                for source in tdata.get("sources", []):
                    url = source.get("url")
                    if not url:
                        continue
                    ok = check_url(url)
                    checked += 1
                    status = "✅" if ok else "❌ UNREACHABLE"
                    print(f"  {code}/{topic}: {status} {url}")
                    if not ok:
                        failed += 1
                    time.sleep(1)
        print(f"\n  {checked} URLs checked, {failed} unreachable")

    if issues_found:
        print(f"\n{issues_found} issue(s) found.")
        sys.exit(1)
    else:
        print("\nAll checks passed.")


if __name__ == "__main__":
    main()
