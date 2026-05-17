#!/usr/bin/env bash
#
# check-corpus-invariants.sh — invariant-gate corpus-hygiene scan
#
# Runs scaffolding-pattern scan + regressed-pattern scan against scope
# (default: manuscript/chapters/Chapter_*Draft*.md + AuthorsNote +
# essay-drafts + op-eds). Exits non-zero on HIGH-severity match.
# Reports MEDIUM-severity findings for review. LOW logged only.
#
# Per pipeline doctrine §2 (tools/commons_bonds_pipeline_doctrine_v1.0.0.md).
#
# Usage:
#   tools/scripts/check-corpus-invariants.sh [OPTIONS]
#
# Options:
#   --scope <path>       Override scope (single file or directory).
#                        Default: per-registry scope configuration.
#   --severity <level>   ALL | HIGH | HIGH+MEDIUM (default: ALL).
#                        Controls which severities are reported.
#   --no-fail            Do not exit non-zero on HIGH match (for stage-
#                        transition / review use; default = fail on HIGH).
#   --registry <type>    scaffolding | regressed | both (default: both).
#   --staged             Scan only staged files (for pre-commit hook use).
#   --verbose            Verbose output.
#   --help               Show this help.
#
# Exit codes:
#   0 — no HIGH matches; clean.
#   1 — HIGH match(es) found; commit / stage transition refused.
#   2 — script error (registry missing, parse failure, etc.).
#
# Note on YAML parsing:
#   Uses a flat-record awk parser. Schema assumes each pattern is a
#   top-level list entry under `patterns:` with consistent indentation.
#   Do not change registry schema without updating this parser.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
REGISTRY_DIR="${REPO_ROOT}/tools/quality-gates"
SCAFFOLDING_YAML="${REGISTRY_DIR}/scaffolding-patterns.yaml"
REGRESSED_YAML="${REGISTRY_DIR}/regressed-patterns.yaml"

# Defaults
SCOPE_OVERRIDE=""
SEVERITY_FILTER="ALL"
NO_FAIL=0
REGISTRY_TYPE="both"
STAGED_ONLY=0
VERBOSE=0

usage() {
  sed -n 's/^# \{0,1\}//p' "$0" | sed -n '/^check-corpus-invariants/,/^Exit codes:$/p; /^Exit codes:$/,/^$/p'
  exit 0
}

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope) SCOPE_OVERRIDE="$2"; shift 2 ;;
    --severity) SEVERITY_FILTER="$2"; shift 2 ;;
    --no-fail) NO_FAIL=1; shift ;;
    --registry) REGISTRY_TYPE="$2"; shift 2 ;;
    --staged) STAGED_ONLY=1; shift ;;
    --verbose|-v) VERBOSE=1; shift ;;
    --help|-h) usage ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

# Verify registries exist
if [[ "$REGISTRY_TYPE" == "scaffolding" || "$REGISTRY_TYPE" == "both" ]]; then
  if [[ ! -f "$SCAFFOLDING_YAML" ]]; then
    echo "ERROR: Scaffolding registry not found at $SCAFFOLDING_YAML" >&2
    exit 2
  fi
fi
if [[ "$REGISTRY_TYPE" == "regressed" || "$REGISTRY_TYPE" == "both" ]]; then
  if [[ ! -f "$REGRESSED_YAML" ]]; then
    echo "ERROR: Regressed-pattern registry not found at $REGRESSED_YAML" >&2
    exit 2
  fi
fi

# ===== Parse YAML registries =====
#
# Output format per pattern (one record per line, tab-separated):
#   <registry>\t<id>\t<pattern>\t<type>\t<severity>\t<category>\t<allowlist_json>
#
# Uses awk to extract from the flat YAML structure. Assumes:
#   - Each pattern entry begins with `  - id: ...`
#   - Indented fields follow until next `  - id:` or end of `patterns:` list
#   - Allowlist is captured as a JSON-ish array of strings (or [] empty).

parse_yaml() {
  local yaml_file="$1"
  local registry_tag="$2"
  awk -v REG="$registry_tag" '
    BEGIN {
      in_patterns = 0
      in_entry = 0
      in_allowlist = 0
      id = ""; pattern = ""; ptype = ""; severity = ""; category = ""
      allowlist = ""
    }
    /^patterns:/ { in_patterns = 1; next }
    /^scope:/ {
      if (in_entry) {
        print REG "\t" id "\t" pattern "\t" ptype "\t" severity "\t" category "\t" allowlist
      }
      in_patterns = 0; in_entry = 0
      next
    }
    /^[^[:space:]]/ { in_patterns = 0; next }
    !in_patterns { next }

    /^  - id:[[:space:]]/ {
      if (in_entry) {
        print REG "\t" id "\t" pattern "\t" ptype "\t" severity "\t" category "\t" allowlist
      }
      in_entry = 1
      in_allowlist = 0
      id = $0; sub(/^  - id:[[:space:]]+/, "", id)
      pattern = ""; ptype = ""; severity = ""; category = ""; allowlist = ""
      next
    }

    in_entry {
      if (match($0, /^    pattern:[[:space:]]+/)) {
        in_allowlist = 0
        pattern = substr($0, RSTART + RLENGTH)
        gsub(/^[\047"]|[\047"]$/, "", pattern)
        next
      }
      if (match($0, /^    type:[[:space:]]+/)) {
        in_allowlist = 0
        ptype = substr($0, RSTART + RLENGTH)
        next
      }
      if (match($0, /^    severity:[[:space:]]+/)) {
        in_allowlist = 0
        severity = substr($0, RSTART + RLENGTH)
        next
      }
      if (match($0, /^    category:[[:space:]]+/)) {
        in_allowlist = 0
        category = substr($0, RSTART + RLENGTH)
        next
      }
      if (match($0, /^    allowlist:/)) {
        in_allowlist = 1
        # check for inline empty allowlist
        rest = substr($0, RSTART + RLENGTH)
        sub(/^[[:space:]]+/, "", rest)
        if (rest == "[]") { allowlist = "[]"; in_allowlist = 0 }
        next
      }
      if (in_allowlist) {
        # Capture allowlist content. Each allowlist entry is structured:
        #   - file: "path/to/file.md"
        #     line: NNN
        #     rationale: "..."
        # We extract file:line tuples for filtering. Format in output:
        #   file:line|file:line|...
        if (match($0, /^      - file:[[:space:]]+/)) {
          alfile = substr($0, RSTART + RLENGTH)
          gsub(/^[\047"]|[\047"]$/, "", alfile)
          gsub(/[\047"][[:space:]]*$/, "", alfile)
          next
        }
        if (match($0, /^        line:[[:space:]]+/)) {
          alline = substr($0, RSTART + RLENGTH)
          gsub(/[[:space:]]+$/, "", alline)
          entry = alfile ":" alline
          if (allowlist == "" || allowlist == "[]") allowlist = entry
          else allowlist = allowlist "|" entry
          next
        }
      }
    }

    END {
      if (in_entry) {
        print REG "\t" id "\t" pattern "\t" ptype "\t" severity "\t" category "\t" allowlist
      }
    }
  ' "$yaml_file"
}

# Build combined registry of patterns
PATTERN_RECORDS=$(mktemp)
trap 'rm -f "$PATTERN_RECORDS"' EXIT

if [[ "$REGISTRY_TYPE" == "scaffolding" || "$REGISTRY_TYPE" == "both" ]]; then
  parse_yaml "$SCAFFOLDING_YAML" "scaffolding" >> "$PATTERN_RECORDS"
fi
if [[ "$REGISTRY_TYPE" == "regressed" || "$REGISTRY_TYPE" == "both" ]]; then
  parse_yaml "$REGRESSED_YAML" "regressed" >> "$PATTERN_RECORDS"
fi

PATTERN_COUNT=$(wc -l < "$PATTERN_RECORDS" | tr -d ' ')

if [[ "$VERBOSE" -eq 1 ]]; then
  echo "[corpus-invariants] Loaded $PATTERN_COUNT patterns from registries" >&2
fi

# ===== Determine scope =====

SCOPE_FILES=$(mktemp)
trap 'rm -f "$PATTERN_RECORDS" "$SCOPE_FILES"' EXIT

if [[ "$STAGED_ONLY" -eq 1 ]]; then
  # Pre-commit mode: scan only staged files matching scope patterns
  cd "$REPO_ROOT"
  git diff --cached --name-only --diff-filter=ACMR | while read -r f; do
    # Match against default scope include patterns (manuscript/chapters/*Draft*.md etc.)
    case "$f" in
      manuscript/chapters/*Draft*.md) echo "$f" ;;
      manuscript/chapters/_AUTHORSNOTE*.md) echo "$f" ;;
      manuscript/chapters/_BookLevelGuidance.md) echo "$f" ;;
      manuscript/chapters/_Dedication.md) echo "$f" ;;
      publishing/essay-drafts/*.md) echo "$f" ;;
      publishing/op-eds/*.md) echo "$f" ;;
    esac
  done > "$SCOPE_FILES"
elif [[ -n "$SCOPE_OVERRIDE" ]]; then
  # User-supplied scope
  cd "$REPO_ROOT"
  if [[ -d "$SCOPE_OVERRIDE" ]]; then
    find "$SCOPE_OVERRIDE" -type f -name '*.md' > "$SCOPE_FILES"
  elif [[ -f "$SCOPE_OVERRIDE" ]]; then
    echo "$SCOPE_OVERRIDE" > "$SCOPE_FILES"
  else
    # Treat as glob
    eval "ls $SCOPE_OVERRIDE 2>/dev/null" > "$SCOPE_FILES" || true
  fi
else
  # Default scope: per registry YAML scope config (include / exclude lists).
  # Hardcoded here to match the YAML; if YAML scope changes, update here too.
  cd "$REPO_ROOT"
  {
    ls manuscript/chapters/Chapter_*Draft*.md 2>/dev/null || true
    ls manuscript/chapters/_AUTHORSNOTE*.md 2>/dev/null || true
    ls manuscript/chapters/_Dedication.md 2>/dev/null || true
    find publishing/essay-drafts -type f -name '*.md' 2>/dev/null \
      | grep -v '/archive/' \
      | grep -v '/templates/' \
      | grep -v '/_inventory_' || true
    find publishing/op-eds -type f -name '*.md' 2>/dev/null \
      | grep -v '/archive/' \
      | grep -v '/_inventory_' || true
  } > "$SCOPE_FILES"
fi

# Filter scope files: keep only files that exist + are readable
SCOPE_VALID=$(mktemp)
trap 'rm -f "$PATTERN_RECORDS" "$SCOPE_FILES" "$SCOPE_VALID"' EXIT
while read -r f; do
  [[ -z "$f" ]] && continue
  [[ -r "$f" ]] && echo "$f"
done < "$SCOPE_FILES" > "$SCOPE_VALID"

SCOPE_COUNT=$(wc -l < "$SCOPE_VALID" | tr -d ' ')

if [[ "$VERBOSE" -eq 1 ]]; then
  echo "[corpus-invariants] Scanning $SCOPE_COUNT files" >&2
fi

if [[ "$SCOPE_COUNT" -eq 0 ]]; then
  if [[ "$VERBOSE" -eq 1 ]]; then
    echo "[corpus-invariants] No files in scope; nothing to scan." >&2
  fi
  exit 0
fi

# ===== Run pattern matches =====

HIGH_COUNT=0
MEDIUM_COUNT=0
LOW_COUNT=0
FINDINGS_REPORT=$(mktemp)
trap 'rm -f "$PATTERN_RECORDS" "$SCOPE_FILES" "$SCOPE_VALID" "$FINDINGS_REPORT"' EXIT

severity_in_filter() {
  local sev="$1"
  case "$SEVERITY_FILTER" in
    ALL) return 0 ;;
    HIGH) [[ "$sev" == "HIGH" ]] && return 0 || return 1 ;;
    HIGH+MEDIUM) [[ "$sev" == "HIGH" || "$sev" == "MEDIUM" ]] && return 0 || return 1 ;;
  esac
  return 0
}

# For each pattern, scan all scope files
while IFS=$'\t' read -r REG ID PATTERN PTYPE SEVERITY CATEGORY ALLOWLIST; do
  [[ -z "$PATTERN" ]] && continue
  severity_in_filter "$SEVERITY" || continue

  # Determine grep flags based on pattern type
  GREP_FLAGS="-Hn"
  case "$PTYPE" in
    string) GREP_FLAGS="-Hn -F" ;;
    word)   GREP_FLAGS="-Hn -E"; PATTERN="\\b${PATTERN}\\b" ;;
    regex)  GREP_FLAGS="-Hn -E" ;;
    *)      GREP_FLAGS="-Hn -F" ;;  # default: string match
  esac

  # Run grep across scope files
  MATCHES=$(xargs grep $GREP_FLAGS -- "$PATTERN" < "$SCOPE_VALID" 2>/dev/null || true)
  [[ -z "$MATCHES" ]] && continue

  # Output findings, filtering by allowlist (file:line tuples)
  while IFS= read -r match_line; do
    [[ -z "$match_line" ]] && continue

    # Extract file:line from match (grep -Hn output: file:line:match-content)
    match_file=$(echo "$match_line" | cut -d: -f1)
    match_lineno=$(echo "$match_line" | cut -d: -f2)
    match_key="${match_file}:${match_lineno}"

    # Allowlist check
    if [[ -n "$ALLOWLIST" && "$ALLOWLIST" != "[]" ]]; then
      # Allowlist is pipe-separated file:line entries
      if echo "|${ALLOWLIST}|" | grep -qF "|${match_key}|"; then
        # Allowlisted; skip
        continue
      fi
    fi

    echo "[$SEVERITY] [$REG/$ID] $match_line" >> "$FINDINGS_REPORT"

    case "$SEVERITY" in
      HIGH)   HIGH_COUNT=$((HIGH_COUNT + 1)) ;;
      MEDIUM) MEDIUM_COUNT=$((MEDIUM_COUNT + 1)) ;;
      LOW)    LOW_COUNT=$((LOW_COUNT + 1)) ;;
    esac
  done <<< "$MATCHES"

done < "$PATTERN_RECORDS"

# ===== Report findings =====

TOTAL=$((HIGH_COUNT + MEDIUM_COUNT + LOW_COUNT))

if [[ "$TOTAL" -eq 0 ]]; then
  if [[ "$VERBOSE" -eq 1 ]]; then
    echo "[corpus-invariants] CLEAN BASELINE — no matches across $PATTERN_COUNT patterns x $SCOPE_COUNT files" >&2
  fi
  exit 0
fi

# Report header
echo "=== check-corpus-invariants — findings ===" >&2
echo "Patterns scanned: $PATTERN_COUNT" >&2
echo "Files scanned:    $SCOPE_COUNT" >&2
echo "HIGH:   $HIGH_COUNT" >&2
echo "MEDIUM: $MEDIUM_COUNT" >&2
echo "LOW:    $LOW_COUNT" >&2
echo "" >&2

# Report findings, sorted by severity
echo "--- Findings ---" >&2
{
  grep '^\[HIGH\]'   "$FINDINGS_REPORT" 2>/dev/null || true
  grep '^\[MEDIUM\]' "$FINDINGS_REPORT" 2>/dev/null || true
  grep '^\[LOW\]'    "$FINDINGS_REPORT" 2>/dev/null || true
} >&2

echo "" >&2

if [[ "$HIGH_COUNT" -gt 0 && "$NO_FAIL" -eq 0 ]]; then
  echo "FAIL: $HIGH_COUNT HIGH-severity match(es) found; resolve before proceeding." >&2
  exit 1
fi

if [[ "$HIGH_COUNT" -gt 0 ]]; then
  echo "WARN: $HIGH_COUNT HIGH-severity match(es) — exit non-zero suppressed via --no-fail." >&2
fi

exit 0
