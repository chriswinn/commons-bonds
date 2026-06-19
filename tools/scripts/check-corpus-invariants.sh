#!/usr/bin/env bash
#
# check-corpus-invariants.sh — invariant-gate corpus-hygiene scan
#
# Runs scaffolding-pattern scan + regressed-pattern scan against scope
# (default: manuscript/chapters/Chapter_*.md + AuthorsNote +
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
#
# Note on essay frontmatter (2026-06-18):
#   publishing/essays/<venue>/essay.md files are scanned BODY-ONLY — their
#   audit-trail frontmatter (leading YAML, HTML-comment blocks, and the
#   aeon-style dossier wrapper) is stripped before pattern-matching, so the
#   process vocabulary in that frontmatter does not false-positive. See the
#   "Essay frontmatter-aware scanning" block below for the recognized shapes.

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
    # Match against default scope include patterns. Per publishing-pipeline reorg
    # 2026-05-24 (Session 2): scope matches live essay.md / op-ed.md files only
    # (not _archive/ historical drafts, cover letters, sign-offs, READMEs —
    # which are internal-scaffolding-adjacent and have their own discipline).
    case "$f" in
      # Chapters dropped the legacy __Draft suffix during the promotion
      # campaign (2026-06); scope now matches Chapter_*.md. The leading
      # `Chapter_` anchor keeps _AUTHORSNOTE/_Dedication out of this branch
      # (handled below) and the case `*` does not cross into archive/ (the
      # path segment after manuscript/chapters/ is `archive/`, not `Chapter`).
      manuscript/chapters/Chapter_*.md) echo "$f" ;;
      manuscript/chapters/_AUTHORSNOTE*.md) echo "$f" ;;
      manuscript/chapters/_BookLevelGuidance.md) echo "$f" ;;
      manuscript/chapters/_Dedication.md) echo "$f" ;;
      # essay.md re-enabled 2026-06-18 with frontmatter-aware scanning: the
      # audit-trail frontmatter is stripped before pattern-matching (see the
      # "Essay frontmatter-aware scanning" block further below). Exclude the
      # internal-scaffolding subtrees first (archived parallel drafts), then
      # match the live per-venue essay.md. Mirrors the default-scope block +
      # the YAML scope.include list.
      publishing/essays/*/_archive/*) ;;   # archived essay variants — excluded
      publishing/essays/_archive/*) ;;     # archived essays — excluded
      publishing/essays/*/essay.md) echo "$f" ;;
      publishing/op-eds/*/op-ed.md) echo "$f" ;;
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
    # Chapters dropped the legacy __Draft suffix during the 2026-06 promotion
    # campaign; the glob is now Chapter_*.md (matches Chapter_10_* + the
    # double-underscore Chapter__1_*…Chapter__9_*). The leading `Chapter_`
    # anchor excludes _AUTHORSNOTE*/_Dedication (globbed separately below) and
    # the non-recursive ls does not descend into archive/.
    ls manuscript/chapters/Chapter_*.md 2>/dev/null || true
    ls manuscript/chapters/_AUTHORSNOTE*.md 2>/dev/null || true
    ls manuscript/chapters/_Dedication.md 2>/dev/null || true
    # Canonical end-user op-ed drafts only (mirror the --staged include set):
    # one op-ed.md per directory. Exclude internal-scaffolding subtrees
    # (_archive/, _pipeline/, _shared/) + per-op-ed rigor briefs / READMEs.
    # NB: the prior `grep -v '/archive/'` did NOT exclude `_archive/` dirs and
    # scanned every op-ed *.md (rigor briefs, READMEs, archived parallel drafts),
    # producing hundreds of spurious HIGH matches on internal scaffolding.
    find publishing/op-eds -type f -name 'op-ed.md' 2>/dev/null \
      | grep -vE '/_archive/|/_pipeline/|/_shared/' || true
    # End-user essay drafts (one essay.md per venue dir). Re-enabled 2026-06-18
    # with frontmatter-aware scanning: each essay.md's audit-trail frontmatter
    # (leading YAML block, HTML-comment blocks anywhere, and the aeon-style
    # dossier wrapper) is stripped before pattern-matching, so only the prose
    # body is scanned (see the "Essay frontmatter-aware scanning" block below).
    # Exclude the internal-scaffolding subtrees, same as op-eds. Keep in sync
    # with the --staged include block above + the YAML scope.include list.
    find publishing/essays -type f -name 'essay.md' 2>/dev/null \
      | grep -vE '/_archive/|/_pipeline/|/_shared/' || true
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

# ===== Frontmatter / comment-aware scanning =====
#
# publishing/essays/<venue>/essay.md files co-locate audit-trail frontmatter
# (pipeline status, rigor-pass history, version pedigree) with the publisher-
# facing prose body. That frontmatter is dense in process vocabulary
# ("Pass 3.3", "RATIFIED", "Option A", INCLUDE/EXCLUDE glyphs, ...) which is
# exactly what the scaffolding/regressed registries flag — so scanning the
# whole file false-positives. We want to scan only the PROSE BODY.
#
# The same problem appears in CHAPTER files (and op-eds): the working drafts
# carry HTML-comment editorial annotations — STATUS/lineage headers, BEAT-rank
# markers, ENHANCE / RESTORED / contribution-matrix notes, "keep/trim/cut at
# redline" instructions — that never render but are dense in the same process
# vocabulary. Brought into scope 2026-06-18 (chapters dropped the __Draft
# suffix, so the gate had been silently scanning ZERO chapters), they would
# false-positive on every such comment. So every scope file gets HTML-comment
# stripping; essays additionally get the YAML-block + dossier-wrapper stripping.
#
# Rather than rewrite the grep pipeline, we precompute the set of audit-trail
# line numbers per file and skip any match landing on one (same mechanism as
# the per-pattern allowlist, just global). Skipping by line — instead of
# feeding grep a stripped copy — keeps the reported file:line numbers pointing
# at the real on-disk lines.
#
# CHAPTER/OP-ED comment stripping is deliberately CONSERVATIVE: it skips a line
# only when the line is WHOLLY comment (nothing but a block comment, possibly
# spanning multiple lines). A line that mixes prose with an inline `<!-- … -->`
# marker is NOT skipped — its prose stays under the scan (the inline comment's
# own process vocabulary surfaces only as non-blocking MEDIUM/LOW, which clears
# when the author resolves the marker at redline). This trades a little comment-
# noise for never silently dropping prose coverage on a redlined paragraph. (The
# essay stripper below is whole-line because essay audit-trail is block-shaped,
# not inline.)
#
# Three frontmatter shapes occur across the live essays (verified 2026-06-18);
# the stripper recognizes all three and leaves no-frontmatter essays untouched:
#   (A) HTML-comment blocks  <!-- ... -->  anywhere in the file
#       (foreign-affairs: a leading block + a trailing Stage-status block).
#   (B) A leading YAML block  ---<newline>...<newline>---  (atlantic-ideas,
#       atlantic-main, public-books).
#   (C) The aeon-style "dossier wrapper": the file opens with an H1 meta-title
#       immediately followed by **bold-label** lines, and the submission prose
#       is fenced between the first `---` horizontal rule and the next one
#       (everything outside that fence — the leading dossier and the trailing
#       "Rigor-pass application history" — is audit-trail).
# A no-frontmatter essay (opens straight into prose; e.g. 100-barrel, harpers,
# noema, nyrb) contributes no skip lines and is scanned in full.

# True for live per-venue essay packages; false for archived variants + the
# _pipeline/_shared scaffolding (those are kept out of scope upstream anyway).
is_essay_scope_file() {
  case "$1" in
    publishing/essays/*/_archive/*|publishing/essays/_archive/*) return 1 ;;
    publishing/essays/*/essay.md) return 0 ;;
    *) return 1 ;;
  esac
}

# awk: prints the 1-based line numbers of audit-trail / frontmatter lines in an
# essay.md (prose body = every line NOT printed). See the shape notes above.
FM_SKIP_AWK='
  { line[NR] = $0 }
  END {
    n = NR
    first = 0
    for (i = 1; i <= n; i++) { if (line[i] !~ /^[[:space:]]*$/) { first = i; break } }

    yaml_mode = (first > 0 && line[first] ~ /^---[[:space:]]*$/)

    dossier_mode = 0
    if (first > 0 && line[first] ~ /^# /) {
      for (j = first + 1; j <= n; j++) {
        if (line[j] !~ /^[[:space:]]*$/) { if (line[j] ~ /^\*\*/) dossier_mode = 1; break }
      }
    }

    # (A) HTML comment blocks, anywhere
    in_comment = 0
    for (i = 1; i <= n; i++) {
      L = line[i]
      if (in_comment) { skip[i] = 1; if (L ~ /-->/) in_comment = 0; continue }
      if (L ~ /<!--/) { skip[i] = 1; if (L !~ /-->/) in_comment = 1 }
    }

    # (B) leading YAML block
    if (yaml_mode) {
      skip[first] = 1
      for (i = first + 1; i <= n; i++) { skip[i] = 1; if (line[i] ~ /^---[[:space:]]*$/) break }
    }

    # (C) dossier wrapper: body strictly between the 1st and 2nd horizontal
    # rule (or after the 1st to EOF if there is no 2nd). If a dossier-mode file
    # somehow has no rule, nothing is skipped here (fail toward a visible
    # false-positive, never a silent miss).
    if (dossier_mode) {
      hr1 = 0; hr2 = 0
      for (i = 1; i <= n; i++) {
        if (line[i] ~ /^-{3,}[[:space:]]*$/) {
          if (hr1 == 0) hr1 = i; else { hr2 = i; break }
        }
      }
      if (hr1 > 0) {
        for (i = 1; i <= hr1; i++) skip[i] = 1
        if (hr2 > 0) for (i = hr2; i <= n; i++) skip[i] = 1
      }
    }

    for (i = 1; i <= n; i++) if (skip[i]) print i
  }
'

# awk: prints the 1-based line numbers of WHOLLY-COMMENT lines (chapters, op-eds,
# AuthorsNote/Dedication). A line is skipped only if, after removing every
# <!-- … --> span (comments may span multiple lines), nothing but whitespace
# remains. A line that still carries prose outside its inline comment is left in
# scope. See the conservative-stripping note above.
COMMENT_SKIP_AWK='
  BEGIN { in_comment = 0 }
  {
    L = $0
    rebuilt = ""
    n = length(L)
    i = 1
    while (i <= n) {
      if (in_comment) {
        p = index(substr(L, i), "-->")
        if (p > 0) { in_comment = 0; i = i + p + 2 } else { i = n + 1 }
      } else {
        p = index(substr(L, i), "<!--")
        if (p > 0) {
          rebuilt = rebuilt substr(L, i, p - 1)
          in_comment = 1
          i = i + p + 3
        } else {
          rebuilt = rebuilt substr(L, i)
          i = n + 1
        }
      }
    }
    if (L !~ /^[[:space:]]*$/ && rebuilt ~ /^[[:space:]]*$/) print NR
  }
'

# Build the global skip-set: one "file:line" key per audit-trail / wholly-comment
# line, checked in the match loop below (alongside the allowlist check). Essays
# get the full frontmatter stripper (A: HTML comments + B: YAML + C: dossier);
# every other scope file gets HTML-comment-only stripping.
SKIP_KEYS=$(mktemp)
trap 'rm -f "$PATTERN_RECORDS" "$SCOPE_FILES" "$SCOPE_VALID" "$SKIP_KEYS"' EXIT
while read -r f; do
  [[ -z "$f" ]] && continue
  if is_essay_scope_file "$f"; then
    awk "$FM_SKIP_AWK" "$f"
  else
    awk "$COMMENT_SKIP_AWK" "$f"
  fi | while read -r ln; do
    [[ -n "$ln" ]] && echo "${f}:${ln}"
  done
done < "$SCOPE_VALID" >> "$SKIP_KEYS"

if [[ "$VERBOSE" -eq 1 ]]; then
  echo "[corpus-invariants] Frontmatter/comment skip-lines: $(wc -l < "$SKIP_KEYS" | tr -d ' ')" >&2
fi

# ===== Run pattern matches =====

HIGH_COUNT=0
MEDIUM_COUNT=0
LOW_COUNT=0
FINDINGS_REPORT=$(mktemp)
trap 'rm -f "$PATTERN_RECORDS" "$SCOPE_FILES" "$SCOPE_VALID" "$SKIP_KEYS" "$FINDINGS_REPORT"' EXIT

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

    # Frontmatter / comment-aware skip: drop matches that land on a precomputed
    # audit-trail or wholly-comment line (essays: frontmatter; chapters/op-eds:
    # HTML comments). The skip-set is keyed by file:line, so the membership test
    # alone is authoritative — no per-file-type guard needed. Prose still scans.
    if [[ -s "$SKIP_KEYS" ]] && grep -qxF -- "$match_key" "$SKIP_KEYS"; then
      continue
    fi

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
