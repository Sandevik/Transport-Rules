#!/usr/bin/env bash
# Transport-Rules update pipeline
# Usage:
#   ./pipeline/update.sh                        # update all countries
#   ./pipeline/update.sh de no dk fi            # update specific countries
#   ./pipeline/update.sh --eu-common            # update EU baseline files only
#   ./pipeline/update.sh --aetr-common          # update AETR baseline files only
#   ./pipeline/update.sh de --topics tolls      # one country, one topic
#   ./pipeline/update.sh --force de             # re-fetch and re-process even if files exist
#
# Requires: ANTHROPIC_API_KEY environment variable for process.py

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV=".venv"
if [ ! -f "$VENV/bin/python" ]; then
    echo "Creating virtualenv..."
    python3 -m venv "$VENV"
    "$VENV/bin/pip" install --quiet -r requirements.txt
fi

PYTHON="$VENV/bin/python"

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    echo "ERROR: ANTHROPIC_API_KEY is not set. process.py requires the Anthropic API." >&2
    exit 1
fi

echo "=== Fetching sources ==="
"$PYTHON" fetch.py "$@"

echo ""
echo "=== Processing into reference files ==="
"$PYTHON" process.py "$@"

echo ""
echo "=== Verifying ==="
"$PYTHON" verify.py --coverage

echo ""
echo "Done. Review changes with: git diff references/"
echo "Commit when satisfied: git add references/ && git commit -m 'update transport rules data'"
