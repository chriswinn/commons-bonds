#!/usr/bin/env bash
# session-end-worktree-cleanup.sh — SessionEnd hook for top-level
# isolated worktree cleanup.
#
# Purpose: eliminate the orphan-top-level-worktree accumulation pattern
# empirically documented by:
#   - tools/workstream-handoffs/git-cleanup-sweep_2026-05-28.md §9 (Round 1)
#       348 → 14 branches, 66 → 7 worktrees in a single sweep
#   - tools/workstream-handoffs/git-cleanup-sweep-round-2_2026-05-30.md §4.1
#       (REINFORCED) — same failure mode regrew 60 worktrees in 24h after
#       Round 1 close. Identical session-close-discipline gap. The hook
#       would have prevented essentially all of the Round 2 regrowth.
#
# Logic:
#   1. Determine current worktree path. If it's the main repo, exit.
#   2. Verify path matches the canonical top-level isolated worktree
#      pattern /Users/c17n/commons-bonds-<workstream>-<harness>.
#   3. Determine current branch. Verify it matches claude/<workstream>-<harness>.
#   4. Skip-list check: refuse to touch §5.1 contaminated branches.
#   5. Skip if dirty (uncommitted/untracked changes).
#   6. git fetch origin main, then check ahead-count. Skip if ahead > 0.
#   7. Scan commit-message bodies on the branch for MERGE-HOLD: or
#      MERGE-AFTER: markers. Skip if present (CLAUDE.md escape hatch).
#   8. Dry-run by default. Set COMMONS_BONDS_HOOK_DESTRUCTIVE=1 to actually
#      remove worktree + delete branch.
#
# Test plan (manual):
#   a. Dry-run from inside a clean merged worktree:
#        bash session-end-worktree-cleanup.sh
#      → prints "would remove" line, exits 0.
#   b. Dry-run from main repo (cwd=/Users/c17n/commons-bonds):
#      → exits 0 with "skip: main repo" line.
#   c. Dry-run from a worktree with uncommitted changes:
#      → exits 0 with "skip: dirty" line.
#   d. Dry-run from a worktree with commits ahead of main:
#      → exits 0 with "skip: ahead=N" line.
#   e. Dry-run from a worktree whose HEAD commit body contains
#      MERGE-HOLD: → exits 0 with "skip: merge-hold marker" line.
#   f. Destructive run from a clean merged worktree:
#        COMMONS_BONDS_HOOK_DESTRUCTIVE=1 bash session-end-worktree-cleanup.sh
#      → runs git worktree remove + git branch -D, prints success.
#
# Exit code 0 always — never block session end.

set -uo pipefail

MAIN_REPO="/Users/c17n/commons-bonds"

# §5.1 contaminated branches per git-cleanup-sweep_2026-05-28.md (must never
# auto-delete; require per-branch detective triage).
CONTAMINATED_BRANCHES=(
  "claude/ch9-pass3-5-1fae85"
  "claude/ch9-stage5-pm-handoff-1fae85"
)

# Helper: emit log line to stdout (becomes session-end hook output).
log() { echo "[session-end-cleanup] $*"; }

# Determine current worktree's toplevel. If not in a git repo, exit.
if ! current_top="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  exit 0
fi
current_top="$(cd "$current_top" && pwd -P 2>/dev/null || echo "$current_top")"

# Guard A — never touch main repo.
main_canon="$(cd "$MAIN_REPO" && pwd -P 2>/dev/null || echo "$MAIN_REPO")"
if [ "$current_top" = "$main_canon" ]; then
  log "skip: cwd is main repo ($current_top)"
  exit 0
fi

# Guard B — only act on the canonical top-level isolated worktree pattern.
# Pattern: /Users/c17n/commons-bonds-<slug>-<harness>
case "$current_top" in
  /Users/c17n/commons-bonds-*) ;;
  *)
    log "skip: cwd not a top-level isolated worktree ($current_top)"
    exit 0
    ;;
esac

# Determine current branch.
if ! current_branch="$(git -C "$current_top" symbolic-ref --short HEAD 2>/dev/null)"; then
  log "skip: HEAD is detached in $current_top"
  exit 0
fi

# Guard C — only act on canonical claude/<workstream>-<harness> branch names.
case "$current_branch" in
  claude/*) ;;
  main)
    log "skip: branch is main"
    exit 0
    ;;
  *)
    log "skip: branch '$current_branch' not canonical claude/<slug>-<harness>"
    exit 0
    ;;
esac

# Guard D — contaminated skip-list.
for b in "${CONTAMINATED_BRANCHES[@]}"; do
  if [ "$current_branch" = "$b" ]; then
    log "skip: branch '$current_branch' on §5.1 contaminated skip-list"
    exit 0
  fi
done

# Guard E — must be clean (no dirty/untracked files).
dirty="$(git -C "$current_top" status --porcelain 2>/dev/null)"
if [ -n "$dirty" ]; then
  log "skip: dirty worktree ($current_top); $(printf '%s\n' "$dirty" | wc -l | tr -d ' ') uncommitted/untracked entries"
  exit 0
fi

# Guard F — refresh origin/main and verify branch is fully merged (ahead=0).
if ! git -C "$current_top" fetch --quiet origin main 2>/dev/null; then
  log "skip: git fetch origin main failed (offline?)"
  exit 0
fi

ahead="$(git -C "$current_top" rev-list --count origin/main..HEAD 2>/dev/null || echo "unknown")"
if [ "$ahead" != "0" ]; then
  log "skip: branch '$current_branch' is $ahead commits ahead of origin/main (would lose work)"
  exit 0
fi

# Guard G — honor MERGE-HOLD: / MERGE-AFTER: commit-message markers per
# CLAUDE.md merge-on-ratification policy. Scan all commits unique to the
# branch (origin/main..HEAD). For a fully-merged branch (ahead=0) this is
# empty, but the branch may also have markers in its merged history reachable
# from main — we only care about UNMERGED markers, which by definition
# don't exist when ahead=0. Belt-and-braces: also scan the tip commit body
# in case the worktree closes immediately after a MERGE-HOLD commit that
# already landed on main but the author still wants inspection time.
tip_body="$(git -C "$current_top" log -1 --format=%B HEAD 2>/dev/null || true)"
if echo "$tip_body" | grep -qE '^(MERGE-HOLD|MERGE-AFTER):'; then
  log "skip: HEAD commit body contains MERGE-HOLD/MERGE-AFTER marker"
  exit 0
fi

# All guards passed. Proceed with cleanup (or dry-run).
worktree_path="$current_top"
branch_to_delete="$current_branch"

if [ "${COMMONS_BONDS_HOOK_DESTRUCTIVE:-0}" != "1" ]; then
  log "DRY-RUN — would remove worktree '$worktree_path' and delete branch '$branch_to_delete'"
  log "set COMMONS_BONDS_HOOK_DESTRUCTIVE=1 to enable destructive cleanup"
  exit 0
fi

# Destructive path — operate from main repo so we can remove this worktree.
if ! git -C "$main_canon" worktree remove "$worktree_path" 2>/dev/null; then
  log "warn: git worktree remove '$worktree_path' failed (may be locked or in use); leaving in place"
  exit 0
fi

if git -C "$main_canon" branch -D "$branch_to_delete" >/dev/null 2>&1; then
  log "cleaned up worktree '$worktree_path' and branch '$branch_to_delete'"
else
  log "removed worktree '$worktree_path' but branch '$branch_to_delete' delete failed (already gone or in use)"
fi

exit 0
