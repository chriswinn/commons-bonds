#!/usr/bin/env bash
# build-derivatives-alt.sh — alt-version derivative builder (Claude-tuned)
#
# Same external interface as build-derivatives.sh. Two differences from the
# baseline script:
#
#   (1) The .md → PDF path passes
#       --include-in-header=tools/scripts/fallback-header.tex to pandoc,
#       when that file exists. The header maps codepoints that the active
#       MAIN_FONT does not cover (currently U+2014 em-dash in bolded spans
#       and U+2248 ≈ in any weight, both gaps in EB Garamond 12) to a
#       fallback font (DejaVu Serif). Result: bolded run-in subheads like
#       "**Method 1 — Replacement Cost**" and approximations like
#       "CS ≈ 0" render as real glyphs rather than tofu boxes.
#
#       If tools/scripts/fallback-header.tex is missing the script silently
#       skips the include — running this alt script in an environment that
#       doesn't have the header file behaves identically to the baseline.
#
#       The header file is small (~15 lines) and editable; add more
#       \newunicodechar entries to it if other codepoints surface as tofu.
#
#   (2) MAIN_FONT defaults to "EB Garamond" (matching the baseline's
#       current value as of commit 3208619 on main).
#
# Everything else — flags, output paths, dependency checks, wkhtmltopdf .html
# path, .docx path via reference.docx — is identical to build-derivatives.sh.
#
# Why the parallel name: the author is iterating on the baseline script and
# this version is the side-by-side comparison artifact. Run whichever is
# cleaner. If this version converges with the baseline, the alt file can
# be removed.
#
# ── Style strategy ────────────────────────────────────────────────────────────
#
#   .docx (always):    pandoc + reference.docx (tools/scripts/reference.docx)
#                      Reference docx carries Garamond 12pt, US Letter, 1" margins,
#                      soft-gray accent on h2/h3. pandoc inherits these styles when
#                      converting either .md or .html.
#
#   .pdf from .html:   wkhtmltopdf (WebKit renderer)
#                      Preserves CSS-driven styling end-to-end.
#
#   .pdf from .md:     pandoc + xelatex
#                      With fallback-header.tex auto-included when present
#                      (mapping em-dash + ≈ to DejaVu Serif for codepoints
#                      EB Garamond doesn't cover).
#
# Usage:
#   tools/scripts/build-derivatives-alt.sh [-o OUT_DIR] [-f FORMATS] [-r REF_DOCX] [-H HEADER_TEX] [-v] [-h] FILE [FILE ...]
#
# Examples:
#   tools/scripts/build-derivatives-alt.sh manuscript/chapters/Chapter__5_*.md
#   tools/scripts/build-derivatives-alt.sh -o ~/sandy-packet core/technical-appendix/TechnicalAppendix_v2.0.0.html
#   tools/scripts/build-derivatives-alt.sh -H "" Chapter__6_*.md          # disable fallback header
#   tools/scripts/build-derivatives-alt.sh -H path/to/other.tex *.md       # custom header
#
# Dependencies:
#   - pandoc          all .docx + .md → PDF
#   - wkhtmltopdf     .html → PDF
#   - xelatex         .md → PDF only
#   - EB Garamond     font (or whatever MAIN_FONT is set to below)
#   - DejaVu Serif    fallback font (only used if fallback-header.tex is included)

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
FALLBACK_HEADER_DEFAULT="tools/scripts/fallback-header.tex"

# ── Runtime defaults ──────────────────────────────────────────────────────────
OUTPUT_DIR=""
FORMATS="docx,pdf"
REFERENCE_DOCX=""
FALLBACK_HEADER=""                             # empty = use default if it exists; -H "" disables
FALLBACK_HEADER_SET=0                          # tracks whether -H was passed at all
VERBOSE=0

# ── Helpers ───────────────────────────────────────────────────────────────────
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../.." && pwd)"

log() { [ "$VERBOSE" -eq 1 ] && echo "[build-derivatives-alt] $*" >&2 || true; }

usage() {
  awk '/^# /{ sub(/^# ?/,""); print; next } /^[^#]/{ exit }' "${BASH_SOURCE[0]}"
  exit "${1:-0}"
}

# ── Arg parsing ───────────────────────────────────────────────────────────────
while getopts ":o:f:r:H:vh" opt; do
  case "$opt" in
    o) OUTPUT_DIR="$OPTARG" ;;
    f) FORMATS="$OPTARG" ;;
    r) REFERENCE_DOCX="$OPTARG" ;;
    H) FALLBACK_HEADER="$OPTARG"; FALLBACK_HEADER_SET=1 ;;
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

# Resolve fallback header. Semantics:
#   - No -H flag passed         → use default if file exists, else skip silently
#   - -H "" passed              → disable fallback header (run vanilla xelatex)
#   - -H <path> passed          → use that path (error if file is missing)
if [ "$FALLBACK_HEADER_SET" -eq 0 ]; then
  if [ -f "${repo_root}/${FALLBACK_HEADER_DEFAULT}" ]; then
    FALLBACK_HEADER="${repo_root}/${FALLBACK_HEADER_DEFAULT}"
  else
    FALLBACK_HEADER=""
    log "No fallback header found at default path; skipping --include-in-header for .md → PDF."
  fi
elif [ -n "$FALLBACK_HEADER" ]; then
  if [ ! -f "$FALLBACK_HEADER" ]; then
    echo "Error: -H specified but '$FALLBACK_HEADER' not found." >&2
    exit 2
  fi
fi

# ── Tooling checks ────────────────────────────────────────────────────────────
command -v pandoc >/dev/null 2>&1 || {
  echo "Error: pandoc not found. Install from https://pandoc.org" >&2
  exit 2
}

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
# F-RP-TA-01 fix (2026-05-18): pandoc input-format override is CONDITIONAL
# on input file extension. For .md/.markdown: pandoc 3.x's default reader
# parses the chapter sources' top-of-file `---` separator as a YAML
# metadata block, fails on the "By Chris Winn" line as an undefined alias
# — the override is required. For .html/.htm: pandoc auto-detects HTML
# correctly + the override would corrupt parsing. The per-input conditional
# is built inside the loop. Matches build-derivatives.sh.

docx_args_base=()
if [ -n "$REFERENCE_DOCX" ]; then
  docx_args_base+=(--reference-doc="$REFERENCE_DOCX")
  log "Using reference docx: $REFERENCE_DOCX"
else
  log "No reference docx found at default path; using pandoc defaults for .docx."
fi

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
if [ -n "$FALLBACK_HEADER" ]; then
  pdf_pandoc_args_base+=(--include-in-header="$FALLBACK_HEADER")
  log "Using fallback header: $FALLBACK_HEADER"
fi

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

  # F-RP-TA-01 fix: pandoc input-format override conditional on extension.
  # See script-init comment block for full rationale.
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
