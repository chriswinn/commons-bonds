#!/usr/bin/env bash
# session-start-orphan-lock-recovery.sh — SessionStart hook.
#
# Purpose: opportunistically clean up orphan-locked
# .claude/worktrees/agent-* worktrees left behind by harness-managed
# Agent-tool sub-sessions whose owning process has died. Empirical
# anchor:
#   - tools/workstream-handoffs/git-cleanup-sweep_2026-05-28.md §2.2
#       found 32 locked agent-* worktrees, ALL pids verified DEAD.
#   - tools/workstream-handoffs/git-cleanup-sweep-round-2_2026-05-30.md §4.1
#       (REINFORCED) — same failure mode produced 2 new orphan locks in
#       the 24h after Round 1 close. Both pids DEAD on re-check.
#
# This is the SessionStart side of the cleanup. Hook 1
# (session-end-worktree-cleanup.sh) prevents same-session orphans;
# this hook recovers from harness-managed orphans whose owning process
# is gone.
#
# Logic (per candidate worktree):
#   1. Restrict to .claude/worktrees/agent-* under the main repo.
#   2. Require a `locked` marker in .git/worktrees/<id>/locked.
#   3. Lock content is a PID per harness convention; verify with
#      kill -0 <pid>. If pid is ALIVE, skip — live session holds it.
#   4. Last commit time must be ≥ 1h ago (conservative — avoids racing
#      a session that just started).
#   5. ahead-of-origin/main count must be 0 (never auto-delete work).
#   6. Dirty check must be empty.
#   7. Skip-list: §5.1 contaminated branches.
#   8. Dry-run by default. Set COMMONS_BONDS_HOOK_DESTRUCTIVE=1 to
#      actually unlock + force-remove.
#
# Runs AFTER the existing worktree-isolation hook
# (session-start-worktree-isolation.sh); see .claude/settings.json
# ordering. Exits 0 always — never blocks session start.
#
# Test plan (manual):
#   a. Dry-run with no orphans present:
#        bash session-start-orphan-lock-recovery.sh
#      → silent (no candidates), exits 0.
#   b. Synthesize an orphan: create an agent worktree with lock content
#      pointing to a dead pid (e.g., pid 999999), touch HEAD time to
#      yesterday, then run dry-run:
#      → prints "would unlock+remove" line per candidate.
#   c. Same setup with a LIVE pid in the lock file (e.g., $$):
#      → prints "skip: lock pid alive" or nothing for that worktree.
#   d. Same setup but with ahead>0:
#      → "skip: ahead=N" line.
#   e. Same setup but lock-file content is non-numeric:
#      → "skip: lock content not a pid" (treats as live to be safe).
#   f. Destructive run on a synthesized DEAD-pid orphan:
#        COMMONS_BONDS_HOOK_DESTRUCTIVE=1 bash session-start-orphan-lock-recovery.sh
#      → runs unlock + force-remove + prints success line.

set -uo pipefail

MAIN_REPO="/Users/c17n/commons-bonds"
AGENT_WT_ROOT="$MAIN_REPO/.claude/worktrees"
MIN_AGE_SECONDS=3600  # 1 hour conservative threshold

CONTAMINATED_BRANCHES=(
  "claude/ch9-pass3-5-1fae85"
  "claude/ch9-stage5-pm-handoff-1fae85"
)

log() { echo "[orphan-lock-recovery] $*"; }

# Bail if main repo gone.
[ -d "$MAIN_REPO/.git" ] || exit 0
[ -d "$AGENT_WT_ROOT" ] || exit 0

# Refresh origin/main once so ahead-checks are accurate. Quiet + tolerant.
git -C "$MAIN_REPO" fetch --quiet origin main 2>/dev/null || true

# Iterate candidate worktree metadata dirs.
# git stores per-worktree metadata at .git/worktrees/<id>/. The locked file,
# if present, lives there. We pair it with the worktree path via
# `git worktree list --porcelain`.

# Build a map: gitdir-basename -> worktree path. Parse porcelain output.
declare -a wt_paths=()
declare -a wt_branches=()

current_path=""
current_branch=""
while IFS= read -r line; do
  case "$line" in
    "worktree "*)
      current_path="${line#worktree }"
      current_branch=""
      ;;
    "branch "*)
      current_branch="${line#branch refs/heads/}"
      ;;
    "")
      if [ -n "$current_path" ]; then
        wt_paths+=("$current_path")
        wt_branches+=("$current_branch")
      fi
      current_path=""
      current_branch=""
      ;;
  esac
done < <(git -C "$MAIN_REPO" worktree list --porcelain 2>/dev/null)

# Flush trailing entry.
if [ -n "$current_path" ]; then
  wt_paths+=("$current_path")
  wt_branches+=("$current_branch")
fi

now_epoch="$(date +%s)"
candidates_found=0

for i in "${!wt_paths[@]}"; do
  wt="${wt_paths[$i]}"
  br="${wt_branches[$i]}"

  # Restrict to .claude/worktrees/agent-* under main repo.
  case "$wt" in
    "$AGENT_WT_ROOT"/agent-*) ;;
    *) continue ;;
  esac

  # Skip main-claimant worktrees defensively.
  if [ "$br" = "main" ]; then
    continue
  fi

  # Locate the per-worktree metadata dir (.git/worktrees/<gitdir-basename>).
  wt_basename="$(basename "$wt")"
  meta_dir="$MAIN_REPO/.git/worktrees/$wt_basename"
  locked_file="$meta_dir/locked"

  # Only consider worktrees with an explicit lock marker.
  [ -f "$locked_file" ] || continue

  candidates_found=$((candidates_found + 1))

  # Read lock content; harness convention is "<pid>".
  lock_content="$(tr -d '[:space:]' < "$locked_file" 2>/dev/null || echo "")"

  # Lock content not a positive integer → treat as live (be safe).
  if ! [[ "$lock_content" =~ ^[0-9]+$ ]]; then
    log "skip: $wt — lock content not a pid ('$lock_content'); treating as live"
    continue
  fi

  # Liveness check.
  if kill -0 "$lock_content" 2>/dev/null; then
    log "skip: $wt — lock pid $lock_content is alive"
    continue
  fi

  # Last commit age check.
  last_commit_epoch="$(git -C "$wt" log -1 --format=%ct HEAD 2>/dev/null || echo "")"
  if [ -z "$last_commit_epoch" ]; then
    log "skip: $wt — could not read last commit time"
    continue
  fi
  age=$((now_epoch - last_commit_epoch))
  if [ "$age" -lt "$MIN_AGE_SECONDS" ]; then
    log "skip: $wt — last commit was ${age}s ago (< ${MIN_AGE_SECONDS}s threshold)"
    continue
  fi

  # Contamination skip-list.
  skip_branch=0
  for cb in "${CONTAMINATED_BRANCHES[@]}"; do
    if [ "$br" = "$cb" ]; then
      log "skip: $wt — branch '$br' on §5.1 contaminated skip-list"
      skip_branch=1
      break
    fi
  done
  [ "$skip_branch" = "1" ] && continue

  # Ahead check.
  ahead="$(git -C "$wt" rev-list --count origin/main..HEAD 2>/dev/null || echo "unknown")"
  if [ "$ahead" != "0" ]; then
    log "skip: $wt — branch is $ahead commits ahead of origin/main (would lose work)"
    continue
  fi

  # Dirty check.
  dirty="$(git -C "$wt" status --porcelain 2>/dev/null)"
  if [ -n "$dirty" ]; then
    log "skip: $wt — dirty working tree"
    continue
  fi

  # All guards passed.
  if [ "${COMMONS_BONDS_HOOK_DESTRUCTIVE:-0}" != "1" ]; then
    log "DRY-RUN — would unlock+remove orphan '$wt' (dead pid $lock_content, age ${age}s, branch '$br')"
    continue
  fi

  # Destructive path.
  git -C "$MAIN_REPO" worktree unlock "$wt" 2>/dev/null || true
  if git -C "$MAIN_REPO" worktree remove --force "$wt" 2>/dev/null; then
    log "removed orphan worktree '$wt' (dead pid $lock_content, age ${age}s)"
    # Optionally also delete the merged branch.
    if [ -n "$br" ] && [ "$br" != "main" ]; then
      git -C "$MAIN_REPO" branch -D "$br" >/dev/null 2>&1 \
        && log "deleted merged branch '$br'" \
        || true
    fi
  else
    log "warn: worktree remove --force '$wt' failed; leaving in place"
  fi
done

# Silent when no candidates and no actions — keep SessionStart output minimal.
if [ "$candidates_found" -eq 0 ]; then
  exit 0
fi

exit 0
