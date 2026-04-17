#!/usr/bin/env bash
# build.sh — Generate QMD wrappers and render the Quarto book.
#
# Usage:
#   ./build.sh          # Render all formats (HTML + PDF)
#   ./build.sh html     # Render HTML only
#   ./build.sh pdf      # Render PDF only
#   ./build.sh preview  # Live-preview HTML in browser

set -euo pipefail
cd "$(dirname "$0")"

echo "==> Generating .qmd wrapper files …"
python3 generate_qmd.py

FORMAT="${1:-all}"

case "$FORMAT" in
  html)
    echo "==> Rendering HTML …"
    quarto render --to html
    ;;
  pdf)
    echo "==> Rendering PDF …"
    quarto render --to pdf
    ;;
  preview)
    echo "==> Starting live preview …"
    quarto preview
    ;;
  all)
    echo "==> Rendering all formats …"
    quarto render
    ;;
  *)
    echo "Unknown format: $FORMAT"
    echo "Usage: $0 [html|pdf|preview|all]"
    exit 1
    ;;
esac

echo "==> Done! Output is in _book/"
