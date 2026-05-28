#!/usr/bin/env bash
#
# refresh-essay-dashboard.sh — regenerate per-essay README auto-derivable sections
#
# Scans publishing/essays/<venue>/ folders. For each, regenerates the section
# between `<!-- AUTO-REFRESHED:BEGIN -->` and `<!-- AUTO-REFRESHED:END -->`
# markers from filesystem state (post-2026-05-28 rigor consolidation).
# Manually-edited prose outside the markers is preserved verbatim.
#
# READMEs without markers are skipped with a hint showing where to add them
# (and the proposed block can be previewed via --dry-run).
#
# Per project review S1 recommendation ratified 2026-05-28.
#
# Usage:
#   tools/scripts/refresh-essay-dashboard.sh [OPTIONS]
#
# Options:
#   --essay <slug>     Refresh one essay (e.g. --essay foreign-affairs-existence-proof)
#   --all              Refresh every essay folder (default).
#   --dry-run          Print proposed block to stdout; do not modify files.
#   --check            Exit non-zero if any README is stale (CI use).
#   --verbose          Verbose output.
#   --help             Show this help.
#
# Exit codes:
#   0 — no changes needed (--check) or refresh applied (default).
#   1 — stale READMEs found (--check) OR fatal error.
#   2 — script error (no essays found, parse failure, etc.).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
ESSAYS_DIR="${REPO_ROOT}/publishing/essays"

MODE="all"
TARGET_SLUG=""
DRY_RUN=0
CHECK=0
VERBOSE=0

BEGIN_MARKER="<!-- AUTO-REFRESHED:BEGIN -->"
END_MARKER="<!-- AUTO-REFRESHED:END -->"

usage() {
  sed -n '/^# refresh-essay-dashboard/,/^$/p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit 0
}

log() {
  if [[ ${VERBOSE} -eq 1 ]]; then
    echo "[refresh-essay-dashboard] $*" >&2
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --essay)
      MODE="one"
      TARGET_SLUG="$2"
      shift 2
      ;;
    --all)
      MODE="all"
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --check)
      CHECK=1
      DRY_RUN=1
      shift
      ;;
    --verbose)
      VERBOSE=1
      shift
      ;;
    --help|-h)
      usage
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 2
      ;;
  esac
done

if [[ ! -d "${ESSAYS_DIR}" ]]; then
  echo "ERROR: essays dir not found at ${ESSAYS_DIR}" >&2
  exit 2
fi

# Resolve word count for an essay.md file.
word_count() {
  local file="$1"
  if [[ -f "${file}" ]]; then
    wc -w < "${file}" | tr -d ' '
  else
    echo "—"
  fi
}

# Parse the Status: line from a stage-5-signoff.md file (the canonical
# ratification record). Falls back gracefully if not present.
signoff_status() {
  local file="$1"
  if [[ ! -f "${file}" ]]; then
    echo "—"
    return
  fi
  # Pull the first line with "Status:" near the top (within first 15 lines).
  local raw
  raw=$(head -15 "${file}" | grep -m1 -i '^\*\*Status:\*\*' || true)
  if [[ -z "${raw}" ]]; then
    raw=$(head -15 "${file}" | grep -m1 -i 'Status:' || true)
  fi
  if [[ -z "${raw}" ]]; then
    echo "(present; no Status: line parsed)"
    return
  fi
  # Strip markdown bold + leading "Status:".
  echo "${raw}" | sed -e 's/\*\*Status:\*\*//' -e 's/^Status://' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | head -c 240
}

# git log -1 date for a file (YYYY-MM-DD). Empty if not tracked.
last_commit_date() {
  local file="$1"
  if [[ ! -e "${file}" ]]; then
    echo "—"
    return
  fi
  ( cd "${REPO_ROOT}" && git log -1 --format=%ad --date=short -- "${file}" 2>/dev/null ) || echo "—"
}

# Emit the auto-refreshed block for a single essay folder.
emit_block() {
  local essay_dir="$1"
  local slug
  slug="$(basename "${essay_dir}")"
  local today
  today="$(date +%Y-%m-%d)"

  local essay_md="${essay_dir}/essay.md"
  local cover="${essay_dir}/cover-letter.md"
  local signoff="${essay_dir}/stage-5-signoff.md"
  local rigor_dir="${essay_dir}/rigor"
  local editor_dir="${essay_dir}/editor-iteration"
  local archive_presub="${essay_dir}/_archive/pre-submission"

  local wc_essay
  wc_essay=$(word_count "${essay_md}")
  local cover_state="absent"
  [[ -f "${cover}" ]] && cover_state="present ($(word_count "${cover}")w; last commit $(last_commit_date "${cover}"))"
  local signoff_state="absent"
  [[ -f "${signoff}" ]] && signoff_state="$(signoff_status "${signoff}") [last commit $(last_commit_date "${signoff}")]"

  # Frozen pre-submission baseline.
  local presub_state="not yet captured"
  if [[ -d "${archive_presub}" ]]; then
    local presub_files
    presub_files=$(find "${archive_presub}" -maxdepth 1 -name 'essay_pre-editor_*.md' -type f 2>/dev/null | sort)
    if [[ -n "${presub_files}" ]]; then
      presub_state=$(echo "${presub_files}" | head -1 | xargs -I {} basename {})
    fi
  fi

  # Editor iteration rounds.
  local editor_state="none"
  if [[ -d "${editor_dir}" ]]; then
    local rounds
    rounds=$(find "${editor_dir}" -maxdepth 1 -type d -name 'round-*' 2>/dev/null | sort)
    if [[ -n "${rounds}" ]]; then
      editor_state=$(echo "${rounds}" | wc -l | tr -d ' ')" round(s): $(echo "${rounds}" | xargs -n1 basename | tr '\n' ' ')"
    fi
  fi

  printf '%s\n' "${BEGIN_MARKER}"
  printf '<!-- Generated by tools/scripts/refresh-essay-dashboard.sh — do not edit by hand. -->\n'
  printf '<!-- Last refresh: %s. -->\n\n' "${today}"

  printf '### Pipeline state (auto-refreshed)\n\n'
  printf -- '- **Essay word count:** %sw (`essay.md`)\n' "${wc_essay}"
  printf -- '- **Cover letter:** %s\n' "${cover_state}"
  printf -- '- **Stage 5 sign-off:** %s\n' "${signoff_state}"
  printf -- '- **Pre-submission frozen baseline:** %s\n' "${presub_state}"
  printf -- '- **Editor-iteration rounds:** %s\n\n' "${editor_state}"

  printf '### Rigor artifacts (auto-refreshed)\n\n'
  if [[ -d "${rigor_dir}" ]]; then
    printf '| Artifact | Last commit |\n'
    printf '|---|---|\n'
    # Top-level rigor files, sorted.
    local f
    while IFS= read -r f; do
      [[ -z "${f}" ]] && continue
      local rel="rigor/$(basename "${f}")"
      printf '| [`%s`](%s) | %s |\n' "${rel}" "${rel}" "$(last_commit_date "${f}")"
    done < <(find "${rigor_dir}" -maxdepth 1 -type f -name '*.md' 2>/dev/null | sort)

    # light-refires subdir, if present.
    if [[ -d "${rigor_dir}/light-refires" ]]; then
      printf '\n**Light re-fires** (`rigor/light-refires/`):\n\n'
      local r
      while IFS= read -r r; do
        [[ -z "${r}" ]] && continue
        local rel="rigor/light-refires/$(basename "${r}")"
        printf -- '- [`%s`](%s) — %s\n' "$(basename "${r}")" "${rel}" "$(last_commit_date "${r}")"
      done < <(find "${rigor_dir}/light-refires" -maxdepth 1 -type f -name '*.md' 2>/dev/null | sort)
    fi
  else
    printf '*No `rigor/` subdir present.*\n'
  fi

  printf '\n%s\n' "${END_MARKER}"
}

# Refresh one essay README in place. Idempotent.
refresh_one() {
  local essay_dir="$1"
  local slug
  slug="$(basename "${essay_dir}")"
  local readme="${essay_dir}/README.md"

  if [[ ! -f "${readme}" ]]; then
    log "skip ${slug}: no README.md"
    return 0
  fi

  local proposed
  proposed=$(emit_block "${essay_dir}")

  if [[ ${DRY_RUN} -eq 1 ]]; then
    printf '=== %s ===\n' "${slug}"
    if ! grep -qF "${BEGIN_MARKER}" "${readme}"; then
      printf 'MISSING MARKERS — add to README.md to opt-in:\n\n'
      printf '%s\n' "${proposed}"
      printf '\n'
      if [[ ${CHECK} -eq 1 ]]; then
        echo "STALE: ${slug} (missing markers)" >&2
        return 1
      fi
      return 0
    fi
    # Compare existing block to proposed.
    local current
    current=$(awk -v b="${BEGIN_MARKER}" -v e="${END_MARKER}" '
      $0 == b {flag=1}
      flag {print}
      $0 == e {flag=0}
    ' "${readme}")
    if [[ "${current}" == "${proposed}" ]]; then
      log "clean: ${slug}"
      printf 'CLEAN: %s\n' "${slug}"
      return 0
    else
      printf 'STALE: %s\n--- current ---\n%s\n--- proposed ---\n%s\n' "${slug}" "${current}" "${proposed}"
      if [[ ${CHECK} -eq 1 ]]; then
        return 1
      fi
      return 0
    fi
  fi

  # Mutation mode.
  if ! grep -qF "${BEGIN_MARKER}" "${readme}"; then
    log "skip ${slug}: no markers in README.md (run with --dry-run to preview block)"
    printf 'SKIP: %s (no markers — preview with --dry-run)\n' "${slug}"
    return 0
  fi

  # In-place replace between markers.
  local tmp
  tmp=$(mktemp)
  awk -v b="${BEGIN_MARKER}" -v e="${END_MARKER}" -v block="${proposed}" '
    BEGIN {in_block=0}
    {
      if ($0 == b) {
        print block
        in_block=1
        next
      }
      if ($0 == e) {
        in_block=0
        next
      }
      if (!in_block) print
    }
  ' "${readme}" > "${tmp}"
  mv "${tmp}" "${readme}"
  printf 'UPDATED: %s\n' "${slug}"
  return 0
}

# Discover essay folders.
discover_essays() {
  find "${ESSAYS_DIR}" -mindepth 1 -maxdepth 1 -type d \
    ! -name '_pipeline' ! -name '_shared' ! -name '_archive' \
    2>/dev/null | sort
}

main() {
  local exit_code=0
  if [[ "${MODE}" == "one" ]]; then
    local dir="${ESSAYS_DIR}/${TARGET_SLUG}"
    if [[ ! -d "${dir}" ]]; then
      echo "ERROR: essay folder not found: ${dir}" >&2
      exit 2
    fi
    refresh_one "${dir}" || exit_code=$?
  else
    local d
    while IFS= read -r d; do
      [[ -z "${d}" ]] && continue
      refresh_one "${d}" || exit_code=$?
    done < <(discover_essays)
  fi
  exit ${exit_code}
}

main "$@"
