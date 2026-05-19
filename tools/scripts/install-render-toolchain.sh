#!/usr/bin/env bash
# install-render-toolchain.sh — canonical apt-based render-toolchain installer.
#
# Targets Ubuntu / Debian 24.04. Idempotent: re-running on an environment that
# already has the toolchain produces the same end-state. Two consumers:
#   - tools/scripts/Dockerfile.render (laptop / CI Docker image build)
#   - .claude/settings.json SessionStart hook (Anthropic remote-container session,
#     gated on CLAUDE_CODE_REMOTE=true so it skips local laptop sessions).
#
# Single canonical source for the render toolchain. Whatever this script
# installs is what the publisher-facing pipeline targets. The
# build-environment.yaml stamp records what versions actually landed; --check
# mode asserts the local environment matches.
#
# Usage:
#   tools/scripts/install-render-toolchain.sh                    # install (default)
#   tools/scripts/install-render-toolchain.sh --check            # verify only; non-zero on mismatch
#   tools/scripts/install-render-toolchain.sh --capture-stamp    # write versions to stdout in build-environment.yaml format
#   tools/scripts/install-render-toolchain.sh --capture-stamp <path>  # write to <path>
#   tools/scripts/install-render-toolchain.sh --help
#
# Hard constraints (per workstream handoff §7):
#   - Idempotent — running twice produces same end-state.
#   - apt-only — no snap, no direct .deb downloads (network policy blocks
#     both in the remote-container; matching that constraint is the
#     whole point of the canonical pipeline).
#   - Chrome NOT installed — Docker context mirrors remote-container which
#     uses wkhtmltopdf for HTML→PDF per the Sandy packet pipeline (e6ddf92).
#     Chrome availability in remote-containers is a separate follow-up.
#   - Required-fonts validation post-install: fc-list must report EB Garamond
#     + DejaVu Serif. Either absent is a failure.
#
# Failure modes handled:
#   - Non-root invocation: re-execs under sudo if sudo is available; otherwise
#     errors with the apt command the user should run.
#   - Non-apt OS: errors with the supported OS list.
#   - apt failure (network policy 403, package not found, etc.): preserves
#     apt's stderr + exits with the apt exit code.
#
# Reference: tools/quality-gates/render-baselines/build-environment.yaml is
# the canonical version stamp; tools/workstream-handoffs/render-toolchain-
# containerization-handoff_2026-05-18.md is the workstream handoff.

set -euo pipefail

# ── Apt package set ───────────────────────────────────────────────────────────
# Packages required to reproduce the remote-container Sandy-packet pipeline.
# Versions are whatever apt offers on Ubuntu 24.04; the build-environment.yaml
# stamp records the actual installed versions for later --check comparison.

APT_PACKAGES=(
  pandoc                # markdown → docx + markdown → PDF (via xelatex)
  texlive-xetex         # xelatex engine for .md → PDF
  texlive-fonts-recommended
  texlive-latex-recommended
  texlive-latex-extra   # newunicodechar package required by fallback-header.tex
  lmodern               # Latin Modern font (lmodern.sty) — pandoc's default xelatex preamble loads it
  wkhtmltopdf           # HTML → PDF (Sandy packet's canonical HTML→PDF engine)
  fonts-ebgaramond      # EB Garamond — canonical body font
  fonts-dejavu          # DejaVu Serif — fallback for EB Garamond's U+2014-bold + U+2248 coverage gaps
  poppler-utils         # pdftotext for render-audit text extraction
  ca-certificates       # apt over HTTPS
)

# ── Mode parsing ──────────────────────────────────────────────────────────────
MODE="install"
CAPTURE_PATH=""

usage() {
  awk '/^# /{ sub(/^# ?/,""); print; next } /^[^#]/{ exit }' "${BASH_SOURCE[0]}"
  exit "${1:-0}"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --check|--verify)
      MODE="check"
      shift
      ;;
    --capture-stamp)
      MODE="capture-stamp"
      shift
      if [ "$#" -gt 0 ] && [[ "$1" != --* ]]; then
        CAPTURE_PATH="$1"
        shift
      fi
      ;;
    -h|--help)
      usage 0
      ;;
    *)
      echo "Error: unknown argument '$1'." >&2
      usage 1
      ;;
  esac
done

# ── Helpers ───────────────────────────────────────────────────────────────────

is_root() { [ "$(id -u)" -eq 0 ]; }

apt_runner() {
  if is_root; then
    "$@"
  elif command -v sudo >/dev/null 2>&1; then
    sudo "$@"
  else
    echo "Error: must run as root or have sudo available. Tried: $*" >&2
    return 2
  fi
}

# Extract pandoc version (e.g., "3.1.3"). Pandoc prints "pandoc 3.1.3" on first line.
pandoc_version() {
  pandoc --version 2>/dev/null | awk 'NR==1 {print $2; exit}'
}

# xelatex version is multi-word; capture the line. Example output:
# "XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian) (preloaded format=xelatex)"
xelatex_version() {
  xelatex --version 2>/dev/null | head -1
}

wkhtmltopdf_version() {
  wkhtmltopdf --version 2>/dev/null | awk '{print $2; exit}'
}

font_present() {
  # Bash-native substring match against a captured fc-list snapshot.
  # Earlier piping (fc-list | grep) failed to detect "DejaVu Serif" inside
  # a Docker RUN despite fc-list clearly emitting the line — likely a
  # pipe buffering / locale corner case. Capture-then-test is robust.
  local query="$1"
  local fc_output
  fc_output="$(fc-list 2>/dev/null)"
  [[ "$fc_output" == *"$query"* ]]
}

# Verify a single required-font signature is present. On failure dumps
# a snippet of fc-list output around the failure for debuggability —
# the apt package name differs from the fc-list-reported family name
# in some Ubuntu releases (e.g., fonts-dejavu vs DejaVu Serif), so when
# the check fails it helps to see what fc-list actually returned.
verify_font() {
  local font_name="$1"
  if font_present "$font_name"; then
    echo "  ✓ ${font_name} present"
    return 0
  else
    echo "  ✗ ${font_name} NOT present" >&2
    echo "    fc-list returned $(fc-list 2>/dev/null | wc -l) entries; first 10:" >&2
    fc-list 2>/dev/null | head -10 | sed 's/^/      /' >&2
    return 1
  fi
}

# ── Stamp emission ────────────────────────────────────────────────────────────
# Emit the actually-installed versions in build-environment.yaml's
# build_environment subset format. Consumer pipes this into
# tools/quality-gates/render-baselines/build-environment.yaml when the
# toolchain advances + the canonical stamp needs to be re-anchored.

emit_stamp() {
  local pandoc_v xelatex_v wkhtml_v
  pandoc_v="$(pandoc_version || true)"
  xelatex_v="$(xelatex_version || true)"
  wkhtml_v="$(wkhtmltopdf_version || true)"

  cat <<EOF
# build-environment stamp snippet — generated by install-render-toolchain.sh --capture-stamp
# Date: $(date -u +%Y-%m-%d)
# Source: $(uname -s -m)
build_environment:
  last_verified: "$(date -u +%Y-%m-%d)"
  pipeline_class: "docker-or-remote-container"
  pandoc_version: "${pandoc_v}"
  xelatex_version: "${xelatex_v}"
  wkhtmltopdf_version: "${wkhtml_v}"
  fonts:
    primary_body: "EB Garamond"
    primary_body_verified: "fonts-ebgaramond (apt)"
    math_font_verified: "DejaVu Serif via fonts-dejavu (apt)"
EOF
}

# ── --check mode ──────────────────────────────────────────────────────────────
# Verify that the apt-installed toolchain is on PATH + fonts present. Does
# NOT diff against build-environment.yaml's pinned versions (apt-on-Ubuntu-
# 24.04 is the pin; comparing version strings character-by-character is
# brittle when apt point-releases). The check is "the toolchain is here +
# the required fonts are here"; the stamp comparison is a deliberate
# author-driven step via --capture-stamp + manual diff.

run_check() {
  local rc=0
  echo "[install-render-toolchain --check] verifying canonical toolchain..."

  for cmd in pandoc xelatex wkhtmltopdf fc-list pdftotext; do
    if command -v "$cmd" >/dev/null 2>&1; then
      echo "  ✓ ${cmd} on PATH"
    else
      echo "  ✗ ${cmd} NOT on PATH" >&2
      rc=1
    fi
  done

  if command -v pandoc >/dev/null 2>&1; then
    echo "  ℹ pandoc:      $(pandoc_version)"
  fi
  if command -v xelatex >/dev/null 2>&1; then
    echo "  ℹ xelatex:     $(xelatex_version)"
  fi
  if command -v wkhtmltopdf >/dev/null 2>&1; then
    echo "  ℹ wkhtmltopdf: $(wkhtmltopdf_version)"
  fi

  echo "[install-render-toolchain --check] verifying fonts..."
  verify_font "EB Garamond"  || rc=1
  verify_font "DejaVu Serif" || rc=1

  if [ "$rc" -eq 0 ]; then
    echo "[install-render-toolchain --check] CLEAN."
  else
    echo "[install-render-toolchain --check] FAILED. Run without --check to install missing packages." >&2
  fi
  return "$rc"
}

# ── Install mode ──────────────────────────────────────────────────────────────

run_install() {
  echo "[install-render-toolchain] installing canonical render toolchain..."

  # OS sniff. apt-get is the load-bearing tool; if absent, error.
  if ! command -v apt-get >/dev/null 2>&1; then
    echo "Error: apt-get not found. This script targets Ubuntu / Debian 24.04." >&2
    echo "       On macOS, use Docker via Colima — see tools/scripts/README.md." >&2
    exit 2
  fi

  # apt-get update — preserves stderr on failure.
  echo "[install-render-toolchain] apt-get update..."
  if ! apt_runner apt-get update; then
    echo "Error: apt-get update failed. If running in a network-restricted environment," >&2
    echo "       verify allowed-domains includes archive.ubuntu.com + security.ubuntu.com." >&2
    exit 2
  fi

  # NOTE: --no-install-recommends is deliberately NOT set. The canonical
  # 2026-05-17 remote-container pre-render was built with the default
  # apt-recommends-on behavior; missing recommends (e.g., lmodern's pull-in
  # of dependent fonts) cause cryptic xelatex "File `lmodern.sty' not found"
  # failures on .md→PDF builds. Bytes match the baseline only with
  # recommends installed.
  echo "[install-render-toolchain] apt-get install ${APT_PACKAGES[*]}..."
  if ! apt_runner apt-get install -y "${APT_PACKAGES[@]}"; then
    echo "Error: apt-get install failed. See output above for package-specific cause." >&2
    exit 2
  fi

  # Refresh fontconfig cache so fc-list sees the newly-apt-installed fonts.
  if command -v fc-cache >/dev/null 2>&1; then
    echo "[install-render-toolchain] fc-cache -f..."
    fc-cache -f || true
  fi

  # Post-install verification: re-use --check mode.
  echo "[install-render-toolchain] post-install verification..."
  if ! run_check; then
    echo "Error: post-install verification failed. Inspect the per-tool messages above." >&2
    exit 3
  fi

  echo "[install-render-toolchain] DONE."
  echo ""
  echo "ℹ To capture the actually-installed version stamp, run:"
  echo "    $0 --capture-stamp"
  echo "ℹ See tools/quality-gates/render-baselines/build-environment.yaml for the canonical stamp."
}

# ── Dispatch ──────────────────────────────────────────────────────────────────

case "$MODE" in
  install)
    run_install
    ;;
  check)
    run_check
    ;;
  capture-stamp)
    if [ -n "$CAPTURE_PATH" ]; then
      emit_stamp > "$CAPTURE_PATH"
      echo "Stamp written to: $CAPTURE_PATH" >&2
    else
      emit_stamp
    fi
    ;;
esac
