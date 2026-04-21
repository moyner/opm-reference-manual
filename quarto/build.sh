#!/usr/bin/env bash
# build.sh - Generate QMD wrappers and render the Quarto book.
#
# Usage:
#   ./build.sh          # Render all formats (HTML + PDF)
#   ./build.sh html     # Render HTML only
#   ./build.sh pdf      # Render PDF only
#   ./build.sh preview  # Live-preview HTML in browser

set -euo pipefail
cd "$(dirname "$0")"

echo "==> Generating .qmd wrapper files ..."
python3 generate_qmd.py

run_quarto() {
  if command -v quarto >/dev/null 2>&1; then
    quarto "$@"
    return
  fi

  if command -v powershell.exe >/dev/null 2>&1; then
    # Fallback for Git Bash on Windows where Quarto is installed but not on bash PATH.
    powershell.exe -NoProfile -Command "quarto $*"
    return
  fi

  echo "Error: Quarto CLI not found on PATH."
  echo "Install Quarto or make sure the 'quarto' command is available."
  exit 1
}

FORMAT="${1:-all}"

case "$FORMAT" in
  html)
    echo "==> Rendering HTML ..."
    run_quarto render --to html
    ;;
  pdf)
    echo "==> Rendering PDF ..."
    run_quarto render --to pdf
    ;;
  preview)
    echo "==> Starting live preview ..."
    run_quarto preview
    ;;
  all)
    echo "==> Rendering all formats ..."
    run_quarto render
    ;;
  *)
    echo "Unknown format: $FORMAT"
    echo "Usage: $0 [html|pdf|preview|all]"
    exit 1
    ;;
esac

echo "==> Done! Output is in _book/"
