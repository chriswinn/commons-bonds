#!/usr/bin/env bash
#
# install-pre-commit-hook.sh — install / verify the corpus-invariants
# pre-commit hook in .git/hooks/.
#
# Per pipeline doctrine §2.4 (tools/commons_bonds_pipeline_doctrine_v1.0.0.md).
#
# Usage:
#   tools/scripts/install-pre-commit-hook.sh [--force]
#
# Options:
#   --force  Overwrite existing hook without prompting.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
HOOKS_DIR="${REPO_ROOT}/.git/hooks"
HOOK_FILE="${HOOKS_DIR}/pre-commit"

FORCE=0
[[ "${1:-}" == "--force" ]] && FORCE=1

if [[ ! -d "$HOOKS_DIR" ]]; then
  echo "ERROR: $HOOKS_DIR not found. Are you in a git repo?" >&2
  exit 1
fi

# Hook content
HOOK_CONTENT='#!/usr/bin/env bash
#
# pre-commit hook — corpus-invariants scan
#
# Installed by tools/scripts/install-pre-commit-hook.sh per pipeline
# doctrine §2.4.
#
# Runs HIGH-severity scan against staged files. Refuses commit on HIGH
# match. To bypass for an explicit exception, use --no-verify (but per
# CLAUDE.md, do not bypass hooks without explicit author direction).

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRIPT="${REPO_ROOT}/tools/scripts/check-corpus-invariants.sh"

if [[ ! -x "$SCRIPT" ]]; then
  echo "[pre-commit] WARN: $SCRIPT not found or not executable; skipping invariant scan."
  exit 0
fi

"$SCRIPT" --staged --severity HIGH
'

# Check existing hook
if [[ -f "$HOOK_FILE" && "$FORCE" -ne 1 ]]; then
  # Check if it's already our hook
  if grep -q "corpus-invariants" "$HOOK_FILE" 2>/dev/null; then
    echo "Pre-commit hook already installed at $HOOK_FILE; updating to current version."
  else
    echo "Pre-commit hook exists at $HOOK_FILE but is not the corpus-invariants hook." >&2
    echo "Refusing to overwrite. Run with --force to overwrite, or back up the existing hook." >&2
    exit 2
  fi
fi

# Write the hook
echo "$HOOK_CONTENT" > "$HOOK_FILE"
chmod +x "$HOOK_FILE"

echo "Pre-commit hook installed at $HOOK_FILE"
echo ""
echo "The hook will run HIGH-severity invariant-gate scans against staged files."
echo "To verify: stage a file with a HIGH-severity pattern (e.g., 'TODO') and try to commit."
echo "To temporarily bypass for legitimate exceptions: git commit --no-verify"
echo "Per CLAUDE.md: do not bypass hooks without explicit author direction."
