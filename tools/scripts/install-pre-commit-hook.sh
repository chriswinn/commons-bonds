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
# Use the COMMON git dir so this works from linked worktrees too (where
# <worktree>/.git is a file, not a dir). All worktrees share these hooks.
HOOKS_DIR="$(cd "$(git -C "$REPO_ROOT" rev-parse --git-common-dir)" && pwd)/hooks"
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
# Runs (1) the HIGH-severity corpus-invariants scan and (2) the prose-clarity
# regression gate against staged files. Refuses commit on a HIGH invariant
# match or a HIGH prose-clarity regression. To bypass for an explicit
# exception, use --no-verify (but per CLAUDE.md, do not bypass hooks without
# explicit author direction).

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCRIPT="${REPO_ROOT}/tools/scripts/check-corpus-invariants.sh"

if [[ ! -x "$SCRIPT" ]]; then
  echo "[pre-commit] WARN: $SCRIPT not found or not executable; skipping invariant scan."
else
  "$SCRIPT" --staged --severity HIGH
fi

# Prose-clarity regression gate (tools/conventions/prose-clarity-contract.md):
# blocks ONLY a HIGH-clunk regression in a baselined file. Regression-only
# (pre-existing clunk does not block) and fail-safe (any error / missing
# baseline / unbaselined file -> exit 0, never blocks).
PROSE="${REPO_ROOT}/tools/scripts/check-prose-clarity.py"
if [[ -f "$PROSE" ]]; then
  python3 "$PROSE" --check-staged
fi
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
echo "The hook runs the HIGH-severity invariant-gate scan and the prose-clarity"
echo "regression gate against staged files."
echo "To verify: stage a file with a HIGH-severity pattern (e.g., 'TODO') and try to commit."
echo "To temporarily bypass for legitimate exceptions: git commit --no-verify"
echo "Per CLAUDE.md: do not bypass hooks without explicit author direction."
