#!/usr/bin/env python3
"""
Transport-Rules fetch pipeline.
Reads YAML source manifests and fetches pages to pipeline/raw/{code}/{topic}/source_NN.txt
"""

import argparse
import sys
import time
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup

PIPELINE_DIR = Path(__file__).parent
SOURCES_DIR = PIPELINE_DIR / "sources"
RAW_DIR = PIPELINE_DIR / "raw"
DELAY = 2  # seconds between requests — be polite to government servers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; TransportRulesFetcher/2.0; +https://github.com/Sandevik/Transport-Rules)"
}


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def fetch_url(url: str) -> str | None:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"    ERROR {url}: {e}", file=sys.stderr)
        return None


def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.find_all(["nav", "header", "footer", "aside", "script", "style"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.find(role="main")
    target = main or soup.body or soup
    return target.get_text(separator="\n", strip=True)


def save_raw(code: str, topic: str, idx: int, text: str):
    dest = RAW_DIR / code / topic
    dest.mkdir(parents=True, exist_ok=True)
    path = dest / f"source_{idx:02d}.txt"
    path.write_text(text, encoding="utf-8")
    print(f"    saved → {path.relative_to(PIPELINE_DIR)}")


def process_manifest(manifest_path: Path, topics_filter: list[str] | None, force: bool):
    manifest = load_yaml(manifest_path)
    code = manifest.get("code", manifest_path.stem)
    country = manifest.get("country", code.upper())
    print(f"\n{'='*60}\nFetching: {country} ({code})\n{'='*60}")

    for topic_name, topic_data in manifest.get("topics", {}).items():
        if topics_filter and topic_name not in topics_filter:
            continue
        sources = topic_data.get("sources", [])
        if not sources:
            continue
        print(f"\n  [{topic_name}] {len(sources)} source(s)")
        for idx, source in enumerate(sources):
            url = source.get("url")
            if not url:
                continue
            out_path = RAW_DIR / code / topic_name / f"source_{idx:02d}.txt"
            if out_path.exists() and not force:
                print(f"    skip (exists) {url}")
                continue
            print(f"    fetch [{idx+1}/{len(sources)}] {url}")
            html = fetch_url(url)
            if html:
                text = extract_text(html)
                if len(text.strip()) > 100:
                    save_raw(code, topic_name, idx, text)
                else:
                    print(f"    SKIP — extracted text too short ({len(text)} chars)")
            time.sleep(DELAY)


def main():
    parser = argparse.ArgumentParser(description="Fetch transport regulation sources")
    parser.add_argument("countries", nargs="*", help="Country codes (e.g. de fr no). Omit for all.")
    parser.add_argument("--eu-common", action="store_true", help="Fetch EU common sources")
    parser.add_argument("--aetr-common", action="store_true", help="Fetch AETR common sources")
    parser.add_argument("--topics", nargs="*", help="Limit to specific topics")
    parser.add_argument("--force", action="store_true", help="Re-fetch even if raw file already exists")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if args.eu_common:
        p = SOURCES_DIR / "eu-common.yaml"
        if p.exists():
            process_manifest(p, args.topics, args.force)
        else:
            print("eu-common.yaml not found", file=sys.stderr)

    if args.aetr_common:
        p = SOURCES_DIR / "aetr-common.yaml"
        if p.exists():
            process_manifest(p, args.topics, args.force)
        else:
            print("aetr-common.yaml not found", file=sys.stderr)

    manifests = sorted((SOURCES_DIR / "countries").glob("*.yaml"))
    if args.countries:
        manifests = [m for m in manifests if m.stem in args.countries]

    for manifest_path in manifests:
        process_manifest(manifest_path, args.topics, args.force)


if __name__ == "__main__":
    main()
