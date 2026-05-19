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
#   .pdf from .html:   headless Chrome (preferred) or wkhtmltopdf (fallback)
#                      HTML sources (e.g. core/technical-appendix/*.html) contain
#                      hand-tuned CSS: run-in bolded headings, italic emphasis,
#                      list spacing, table styling, code-like terminology spans.
#                      Both engines render the HTML *as styled* — preserving
#                      everything the author saw in the browser.
#
#                      Why Chrome preferred: wkhtmltopdf 0.12.6 ships with a
#                      patched Qt 5.5 whose font loader cannot enumerate macOS
#                      TrueType Collections (.ttc). On macOS, that means Georgia,
#                      Times, Charter, etc. are silently substituted with
#                      Helvetica, and Plane-1 chars (e.g. 𝒞 U+1D49E) fall to
#                      .LastResort tofu glyphs. Chrome uses the platform-native
#                      font stack, honors per-character CSS fallback, and
#                      produces output that matches the in-browser render and
#                      the sandboxed mobile session render. Discovered
#                      2026-05-15 during Technical Appendix v2.0.0 build.
#
#                      wkhtmltopdf is kept as a fallback for environments
#                      without Chrome (some CI containers, headless servers).
#                      On Linux it works fine — fontconfig sees individual .ttf
#                      files where macOS hides them inside .ttc collections.
#
#                      Why not pandoc+xelatex here? It routes HTML → LaTeX, which
#                      strips the CSS and applies generic LaTeX serif typography.
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
#   - Chrome          https://www.google.com/chrome/   (preferred for .html → PDF)
#                       brew install --cask google-chrome   # macOS
#                       apt install google-chrome-stable    # Debian/Ubuntu
#                     Also accepted: Chromium, Microsoft Edge.
#                     Used for: .html → PDF (matches in-browser render).
#
#   - wkhtmltopdf     https://wkhtmltopdf.org   (fallback for .html → PDF)
#                       brew install --cask wkhtmltopdf   # macOS
#                       apt install wkhtmltopdf            # Debian/Ubuntu
#                     Used only if Chrome is not installed. On macOS this
#                     produces poor output (Helvetica-only substitution; see
#                     comment block above) — install Chrome instead.
#                     wkhtmltopdf upstream releases stopped Jan 2023.
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
MAIN_FONT="EB Garamond"
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

# For PDF we may need xelatex (for .md), Chrome (preferred for .html), or
# wkhtmltopdf (fallback for .html). Detect what's available; we'll error
# per-file if a needed engine is missing.
have_xelatex=0
have_chrome=0
have_wkhtmltopdf=0
CHROME_BIN=""
if [[ ",${FORMATS}," == *",pdf,"* ]]; then
  command -v xelatex      >/dev/null 2>&1 && have_xelatex=1
  command -v wkhtmltopdf  >/dev/null 2>&1 && have_wkhtmltopdf=1

  # Chrome detection — try common binary locations on macOS and Linux.
  for candidate in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
    "$(command -v google-chrome 2>/dev/null)" \
    "$(command -v google-chrome-stable 2>/dev/null)" \
    "$(command -v chromium 2>/dev/null)" \
    "$(command -v chromium-browser 2>/dev/null)" \
    "$(command -v microsoft-edge 2>/dev/null)"; do
    if [ -n "$candidate" ] && [ -x "$candidate" ]; then
      CHROME_BIN="$candidate"
      have_chrome=1
      break
    fi
  done

  if [ "$have_xelatex" -eq 0 ] && [ "$have_chrome" -eq 0 ] && [ "$have_wkhtmltopdf" -eq 0 ]; then
    echo "Error: PDF requested but no PDF engine is installed." >&2
    echo "       Install at least one:" >&2
    echo "         brew install --cask mactex-no-gui   # xelatex (for .md → PDF)" >&2
    echo "         brew install --cask google-chrome   # Chrome (for .html → PDF, preferred)" >&2
    echo "         brew install --cask wkhtmltopdf     # wkhtmltopdf (for .html → PDF, fallback)" >&2
    echo "       Or pass '-f docx' to skip PDFs." >&2
    exit 2
  fi
fi

# ── Pandoc arg builders ───────────────────────────────────────────────────────
# Disable YAML-metadata-block detection — pandoc 3.x parses the chapter
# sources' top-of-file `---` separator as a YAML metadata block, which
# F-RP-TA-01 fix (2026-05-18): pandoc input-format override is CONDITIONAL
# on input file extension. For .md/.markdown sources, pandoc 3.x's default
# reader parses the chapter sources' `---` separator as a YAML metadata
# block, fails on the "By Chris Winn" line as an undefined alias — the
# override is required. For .html/.htm sources, pandoc auto-detects HTML
# correctly + this override would corrupt parsing (echoes HTML tags as
# literal text + fails to decode entities + breaks TOC structure). The
# original unconditional override (landed during Ch 1 retrofit) was
# correct for .md but broke TA docx generation (~8% content loss per
# tools/rigor-passes/render_pipeline_comparison_ta_2026-05-18.md F-RP-TA-01).
# Per-input conditional resolves the regression.
# See tools/quality-gates/render-baselines/build-environment.yaml for the
# canonical toolchain stamp + this fix's reproducibility implications.

docx_args_base=()
if [ -n "$REFERENCE_DOCX" ]; then
  docx_args_base+=(--reference-doc="$REFERENCE_DOCX")
  log "Using reference docx: $REFERENCE_DOCX"
else
  log "No reference docx found at default path; using pandoc defaults for .docx."
fi

# pandoc+xelatex args (used for .md → PDF only). The pandoc_format_args
# get prepended per-input inside the loop based on file extension.
pdf_pandoc_args_base=(
  --pdf-engine=xelatex
  --variable=mainfont:"$MAIN_FONT"
  --variable=fontsize:"$FONT_SIZE"
  --variable=papersize:"$PAPER_SIZE"
  --variable=geometry:"margin=$MARGIN"
  --variable=colorlinks:true
  --variable=pagestyle:plain
)
[ -n "$LINE_STRETCH" ] && pdf_pandoc_args_base+=(--variable=linestretch:"$LINE_STRETCH")

# wkhtmltopdf args (fallback for .html → PDF)
pdf_wkhtml_args=(
  --quiet
  --enable-local-file-access
  --page-size "$WKHTMLTOPDF_PAGE_SIZE"
  --margin-top    "$WKHTMLTOPDF_MARGIN"
  --margin-bottom "$WKHTMLTOPDF_MARGIN"
  --margin-left   "$WKHTMLTOPDF_MARGIN"
  --margin-right  "$WKHTMLTOPDF_MARGIN"
)

# Chrome headless args (preferred for .html → PDF). Page size + margins
# come from the HTML's @page CSS (e.g. `@page { size: letter; margin: 1in; }`).
pdf_chrome_args=(
  --headless
  --disable-gpu
  --no-pdf-header-footer
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

  # F-RP-TA-01 fix: pandoc input-format override conditional on extension.
  # See block above (script-init comment) for full rationale.
  if [[ "$ext_lower" == "md" || "$ext_lower" == "markdown" ]]; then
    pandoc_format_args=(--from=markdown-yaml_metadata_block)
  else
    pandoc_format_args=()
  fi
  docx_args=("${pandoc_format_args[@]}" "${docx_args_base[@]}")
  pdf_pandoc_args=("${pandoc_format_args[@]}" "${pdf_pandoc_args_base[@]}")

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
      # HTML → PDF: prefer Chrome headless (matches in-browser render), fall
      # back to wkhtmltopdf only if Chrome is unavailable.
      if [ "$have_chrome" -eq 1 ]; then
        # Chrome wants a file:// URL with an absolute path.
        input_abs="$(cd "$(dirname "$input")" && pwd)/$(basename "$input")"
        log "  chrome → $out_pdf"
        if "$CHROME_BIN" "${pdf_chrome_args[@]}" --print-to-pdf="$out_pdf" "file://${input_abs}" >/dev/null 2>&1; then
          echo "    ✓ ${out_pdf}"
        else
          echo "    ✗ ${out_pdf} (chrome headless failed)" >&2
          errors=$((errors + 1))
        fi
      elif [ "$have_wkhtmltopdf" -eq 1 ]; then
        log "  wkhtmltopdf → $out_pdf  (Chrome not found; using fallback engine)"
        if wkhtmltopdf "${pdf_wkhtml_args[@]}" "$input" "$out_pdf"; then
          echo "    ✓ ${out_pdf}  (wkhtmltopdf fallback — install Chrome for better fidelity)"
        else
          echo "    ✗ ${out_pdf} (wkhtmltopdf failed)" >&2
          errors=$((errors + 1))
        fi
      else
        echo "    ✗ ${out_pdf} (no HTML→PDF engine installed)" >&2
        echo "       brew install --cask google-chrome   # preferred" >&2
        echo "       brew install --cask wkhtmltopdf     # fallback" >&2
        errors=$((errors + 1))
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
