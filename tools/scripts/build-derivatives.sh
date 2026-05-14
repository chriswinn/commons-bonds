#!/usr/bin/env bash
# build-derivatives.sh — generate standardized .docx + .pdf from .md / .html sources
#
# Style template: tools/scripts/reference.docx
#   Originally a copy of the Ch 6 packet-send .docx — Garamond 12pt, US Letter,
#   1" margins, 0.5" header/footer, soft-gray accent on h2/h3. PDF output mirrors
#   these values via pandoc variables. To re-anchor the style: replace
#   reference.docx with any approved .docx — pandoc inherits its styles section.
#
# Usage:
#   tools/scripts/build-derivatives.sh [-o OUT_DIR] [-f FORMATS] [-r REF_DOCX] [-v] [-h] FILE [FILE ...]
#
# Examples:
#   tools/scripts/build-derivatives.sh manuscript/chapters/Chapter__5_*.md
#   tools/scripts/build-derivatives.sh -o ~/sandy-packet manuscript/chapters/Chapter__6_*.md
#   tools/scripts/build-derivatives.sh -f docx core/technical-appendix/TechnicalAppendix_v2.1.0.html
#   tools/scripts/build-derivatives.sh -f pdf -r path/to/custom-reference.docx Chapter__5_*.md
#
# Inputs: .md or .html (or anything pandoc reads — pandoc auto-detects by extension).
# Outputs: <stem>.docx + <stem>.pdf alongside each input (or in -o OUT_DIR).
#
# Dependencies:
#   - pandoc    https://pandoc.org           (`brew install pandoc` / `apt install pandoc`)
#   - xelatex   TeX Live / MacTeX            (`brew install --cask mactex-no-gui` / `apt install texlive-xetex`)
#   - Garamond  available system-wide on Mac/Windows; on Linux: `apt install fonts-ebgaramond`
#               (the script falls back to a generic serif if Garamond isn't found by xelatex)

set -euo pipefail

# ── Style configuration (edit these to change defaults) ───────────────────────
MAIN_FONT="Garamond"
FONT_SIZE="12pt"
PAPER_SIZE="letter"
MARGIN="1in"
LINE_STRETCH=""                                # blank = pandoc/LaTeX default (Word-auto-equivalent)
REFERENCE_DOCX_DEFAULT="tools/scripts/reference.docx"

# ── Runtime defaults ──────────────────────────────────────────────────────────
OUTPUT_DIR=""
FORMATS="docx,pdf"
REFERENCE_DOCX=""
VERBOSE=0

# ── Helpers ───────────────────────────────────────────────────────────────────
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../.." && pwd)"

log() { [ "$VERBOSE" -eq 1 ] && echo "[build-derivatives] $*" >&2 || true; }

usage() {
  awk '/^# /{ sub(/^# ?/,""); print; next } /^[^#]/{ exit }' "${BASH_SOURCE[0]}"
  exit "${1:-0}"
}

# ── Arg parsing ───────────────────────────────────────────────────────────────
while getopts ":o:f:r:vh" opt; do
  case "$opt" in
    o) OUTPUT_DIR="$OPTARG" ;;
    f) FORMATS="$OPTARG" ;;
    r) REFERENCE_DOCX="$OPTARG" ;;
    v) VERBOSE=1 ;;
    h) usage 0 ;;
    \?) echo "Unknown option: -$OPTARG" >&2; usage 1 ;;
    :)  echo "Option -$OPTARG requires an argument." >&2; usage 1 ;;
  esac
done
shift $((OPTIND - 1))

[ "$#" -gt 0 ] || { echo "Error: no input files given." >&2; usage 1; }

# Resolve default reference relative to the repo, not cwd
if [ -z "$REFERENCE_DOCX" ]; then
  REFERENCE_DOCX="${repo_root}/${REFERENCE_DOCX_DEFAULT}"
fi
[ -f "$REFERENCE_DOCX" ] || REFERENCE_DOCX=""    # absent reference → fall back to pandoc defaults

# ── Tooling checks ────────────────────────────────────────────────────────────
command -v pandoc >/dev/null 2>&1 || {
  echo "Error: pandoc not found. Install from https://pandoc.org" >&2
  exit 2
}

if [[ ",${FORMATS}," == *",pdf,"* ]]; then
  command -v xelatex >/dev/null 2>&1 || {
    echo "Error: xelatex not found (needed for PDF). Install TeX Live / MacTeX," >&2
    echo "       or pass '-f docx' to skip PDFs." >&2
    exit 2
  }
fi

# ── Pandoc arg builders ───────────────────────────────────────────────────────
docx_args=()
if [ -n "$REFERENCE_DOCX" ]; then
  docx_args+=(--reference-doc="$REFERENCE_DOCX")
  log "Using reference docx: $REFERENCE_DOCX"
else
  log "No reference docx found at default path; using pandoc defaults for .docx."
fi

pdf_args=(
  --pdf-engine=xelatex
  --variable=mainfont:"$MAIN_FONT"
  --variable=fontsize:"$FONT_SIZE"
  --variable=papersize:"$PAPER_SIZE"
  --variable=geometry:"margin=$MARGIN"
  --variable=colorlinks:true
  --variable=pagestyle:plain
)
[ -n "$LINE_STRETCH" ] && pdf_args+=(--variable=linestretch:"$LINE_STRETCH")

# ── Conversion loop ───────────────────────────────────────────────────────────
errors=0

for input in "$@"; do
  if [ ! -f "$input" ]; then
    echo "Warning: '$input' not found, skipping." >&2
    errors=$((errors + 1))
    continue
  fi

  if [ -n "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
    out_dir="$OUTPUT_DIR"
  else
    out_dir="$(dirname "$input")"
  fi
  stem="$(basename "${input%.*}")"

  echo "→ $input"

  if [[ ",${FORMATS}," == *",docx,"* ]]; then
    out_docx="${out_dir}/${stem}.docx"
    log "  pandoc → $out_docx"
    if pandoc "$input" "${docx_args[@]}" -o "$out_docx"; then
      echo "    ✓ ${out_docx}"
    else
      echo "    ✗ ${out_docx} (pandoc failed)" >&2
      errors=$((errors + 1))
    fi
  fi

  if [[ ",${FORMATS}," == *",pdf,"* ]]; then
    out_pdf="${out_dir}/${stem}.pdf"
    log "  pandoc → $out_pdf"
    if pandoc "$input" "${pdf_args[@]}" -o "$out_pdf"; then
      echo "    ✓ ${out_pdf}"
    else
      echo "    ✗ ${out_pdf} (pandoc/xelatex failed — check that '$MAIN_FONT' is installed)" >&2
      errors=$((errors + 1))
    fi
  fi
done

if [ "$errors" -gt 0 ]; then
  echo "Done with $errors error(s)." >&2
  exit 3
fi
echo "Done."
