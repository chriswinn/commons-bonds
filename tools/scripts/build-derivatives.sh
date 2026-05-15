#!/usr/bin/env bash
# build-derivatives.sh — generate standardized .docx + .pdf from .md / .html sources
#
# ── Style strategy ────────────────────────────────────────────────────────────
#
#   .docx (always):    pandoc + reference.docx (tools/scripts/reference.docx)
#                      Reference docx carries Garamond 12pt, US Letter, 1" margins,
#                      soft-gray accent on h2/h3. pandoc inherits these styles when
#                      converting either .md or .html. (Originally a copy of the
#                      Ch 6 packet-send .docx. To re-anchor: replace reference.docx
#                      with any approved .docx — pandoc reads its styles section.)
#
#   .pdf from .html:   wkhtmltopdf (WebKit renderer)
#                      HTML sources (e.g. core/technical-appendix/*.html) contain
#                      hand-tuned CSS: run-in bolded headings, italic emphasis,
#                      list spacing, table styling, code-like terminology spans.
#                      wkhtmltopdf renders the HTML *as styled* — preserving
#                      everything the author saw in the browser.
#
#                      Why not pandoc+xelatex here? It routes HTML → LaTeX, which
#                      strips the CSS and applies generic LaTeX serif typography.
#                      Author preference (2026-05-15, post Darity-packet review):
#                      wkhtmltopdf output matches authoring intent for HTML
#                      sources, so PDF generation for HTML inputs uses
#                      wkhtmltopdf rather than pandoc+xelatex. This is the same
#                      tooling used by the sandboxed mobile sessions when
#                      regenerating Technical Appendix derivatives.
#
#   .pdf from .md:     pandoc + xelatex
#                      Markdown chapter sources don't carry CSS, so the LaTeX
#                      path gives clean book-style typography (Garamond 12pt,
#                      1" margins) consistent with the reference docx. No
#                      regression vs. the original script for these inputs.
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
#   - pandoc          https://pandoc.org
#                       brew install pandoc           # macOS
#                       apt install pandoc            # Debian/Ubuntu
#                     Used for: all .docx output, and .md → PDF.
#
#   - wkhtmltopdf     https://wkhtmltopdf.org
#                       brew install --cask wkhtmltopdf   # macOS
#                       apt install wkhtmltopdf            # Debian/Ubuntu
#                     Used for: .html → PDF (CSS-preserving render).
#                     Note: wkhtmltopdf upstream releases stopped Jan 2023, but
#                     the binary is stable and widely installed for static HTML.
#                     Alternatives if you ever need to migrate off it: weasyprint
#                     (`pip install weasyprint`) or headless Chrome (`chromium
#                     --headless --print-to-pdf`). Both also render CSS faithfully.
#
#   - xelatex         TeX Live / MacTeX
#                       brew install --cask mactex-no-gui   # macOS
#                       apt install texlive-xetex            # Debian/Ubuntu
#                     Used for: .md → PDF only. Not needed if you only build
#                     .docx, or only build .html-source PDFs.
#
#   - Garamond        font; system-wide on Mac/Windows.
#                       apt install fonts-ebgaramond         # Linux fallback
#                     Used by xelatex (.md → PDF) and by the reference docx.

set -euo pipefail

# ── Style configuration ───────────────────────────────────────────────────────
# xelatex path (used for .md → PDF)
MAIN_FONT="Garamond"
FONT_SIZE="12pt"
PAPER_SIZE="letter"
MARGIN="1in"
LINE_STRETCH=""                                # blank = pandoc/LaTeX default

# wkhtmltopdf path (used for .html → PDF)
WKHTMLTOPDF_PAGE_SIZE="Letter"                 # matches xelatex PAPER_SIZE
WKHTMLTOPDF_MARGIN="25mm"                      # ≈ 1in, applied to all four sides

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

# For PDF we may need either xelatex (for .md) or wkhtmltopdf (for .html).
# Detect what's available; we'll error per-file if a needed engine is missing.
have_xelatex=0
have_wkhtmltopdf=0
if [[ ",${FORMATS}," == *",pdf,"* ]]; then
  command -v xelatex      >/dev/null 2>&1 && have_xelatex=1
  command -v wkhtmltopdf  >/dev/null 2>&1 && have_wkhtmltopdf=1

  if [ "$have_xelatex" -eq 0 ] && [ "$have_wkhtmltopdf" -eq 0 ]; then
    echo "Error: PDF requested but neither xelatex nor wkhtmltopdf is installed." >&2
    echo "       Install at least one:" >&2
    echo "         brew install --cask mactex-no-gui   # xelatex (for .md → PDF)" >&2
    echo "         brew install --cask wkhtmltopdf     # wkhtmltopdf (for .html → PDF)" >&2
    echo "       Or pass '-f docx' to skip PDFs." >&2
    exit 2
  fi
fi

# ── Pandoc arg builders ───────────────────────────────────────────────────────
docx_args=()
if [ -n "$REFERENCE_DOCX" ]; then
  docx_args+=(--reference-doc="$REFERENCE_DOCX")
  log "Using reference docx: $REFERENCE_DOCX"
else
  log "No reference docx found at default path; using pandoc defaults for .docx."
fi

# pandoc+xelatex args (used for .md → PDF only)
pdf_pandoc_args=(
  --pdf-engine=xelatex
  --variable=mainfont:"$MAIN_FONT"
  --variable=fontsize:"$FONT_SIZE"
  --variable=papersize:"$PAPER_SIZE"
  --variable=geometry:"margin=$MARGIN"
  --variable=colorlinks:true
  --variable=pagestyle:plain
)
[ -n "$LINE_STRETCH" ] && pdf_pandoc_args+=(--variable=linestretch:"$LINE_STRETCH")

# wkhtmltopdf args (used for .html → PDF only)
pdf_wkhtml_args=(
  --quiet
  --enable-local-file-access
  --page-size "$WKHTMLTOPDF_PAGE_SIZE"
  --margin-top    "$WKHTMLTOPDF_MARGIN"
  --margin-bottom "$WKHTMLTOPDF_MARGIN"
  --margin-left   "$WKHTMLTOPDF_MARGIN"
  --margin-right  "$WKHTMLTOPDF_MARGIN"
)

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
  ext_lower="$(echo "${input##*.}" | tr '[:upper:]' '[:lower:]')"

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

    if [[ "$ext_lower" == "html" || "$ext_lower" == "htm" ]]; then
      # HTML → PDF via wkhtmltopdf (CSS-preserving)
      if [ "$have_wkhtmltopdf" -eq 0 ]; then
        echo "    ✗ ${out_pdf} (wkhtmltopdf not installed; needed for .html → PDF)" >&2
        echo "       brew install --cask wkhtmltopdf  /  apt install wkhtmltopdf" >&2
        errors=$((errors + 1))
      else
        log "  wkhtmltopdf → $out_pdf"
        if wkhtmltopdf "${pdf_wkhtml_args[@]}" "$input" "$out_pdf"; then
          echo "    ✓ ${out_pdf}"
        else
          echo "    ✗ ${out_pdf} (wkhtmltopdf failed)" >&2
          errors=$((errors + 1))
        fi
      fi
    else
      # .md (or other pandoc-readable) → PDF via pandoc+xelatex
      if [ "$have_xelatex" -eq 0 ]; then
        echo "    ✗ ${out_pdf} (xelatex not installed; needed for .${ext_lower} → PDF)" >&2
        echo "       brew install --cask mactex-no-gui  /  apt install texlive-xetex" >&2
        errors=$((errors + 1))
      else
        log "  pandoc → $out_pdf"
        if pandoc "$input" "${pdf_pandoc_args[@]}" -o "$out_pdf"; then
          echo "    ✓ ${out_pdf}"
        else
          echo "    ✗ ${out_pdf} (pandoc/xelatex failed — check that '$MAIN_FONT' is installed)" >&2
          errors=$((errors + 1))
        fi
      fi
    fi
  fi
done

if [ "$errors" -gt 0 ]; then
  echo "Done with $errors error(s)." >&2
  exit 3
fi
echo "Done."
