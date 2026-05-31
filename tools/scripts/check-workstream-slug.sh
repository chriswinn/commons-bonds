#!/usr/bin/env bash
# check-workstream-slug.sh — G4 pre-check guard against duplicate
# workstream-slug spawns. Read-only; never modifies state.
#
# Usage:
#   tools/scripts/check-workstream-slug.sh <workstream-slug>
#
# Exit codes:
#   0 — slug clear; safe to `git worktree add -b`
#   1 — slug collision detected; review WARN output before proceeding
#   2 — input-validation or other error
#
# Purpose: complementary to the existing SessionStart hooks
# (session-start-worktree-isolation.sh + session-start-orphan-lock-recovery.sh)
# + the SessionEnd hook (session-end-worktree-cleanup.sh). Those handle
# isolation + orphan cleanup. This script catches the parallel-session
# failure mode where two independent sessions pick the same workstream
# slug, which fragments work across distinct harness-id-suffixed branches
# (or, rarely, hard-collides if both happen to pick the same date+hex
# harness).
#
# Empirical anchor: ~50-60 active worktrees per sprint day (per the
# 2026-05-28 + 2026-05-30 cleanup sweeps). Collision probability is
# non-negligible even with random harness IDs, and slug-near-collisions
# (e.g., `aeon-pitch-review` vs `aeon-pitch-final-review`) hide work
# fragmentation that the existing hooks cannot catch.
#
# Discipline: invoked from the canonical worktree-isolation paste-text
# at tools/drafting-templates/worktree-isolation-paste-text.md BEFORE
# `git worktree add -b`. If a collision is detected, the model surfaces
# the WARN block to the author + offers options (pick a more specific
# slug; clean up a stale match; resume an existing worktree; or set
# FORCE_SLUG_COLLISION=1 for intentional intra-slug sub-sessions).
#
# §5.1 contaminated-branch list: referenced indirectly. The canonical
# list lives in session-end-worktree-cleanup.sh and
# session-start-orphan-lock-recovery.sh. This script flags any match
# as such by name-comparison against the same list (kept in sync
# manually; the list rarely changes — per git-cleanup-sweep_2026-05-28.md).
#
# Test plan (manual; document results in commit message body):
#   a. Clear slug (definitely unused):
#        ./check-workstream-slug.sh "definitely-not-an-existing-slug-9z2k4"
#      → exit 0, prints "OK: slug 'definitely-...' is clear".
#   b. Collision with active worktree:
#        ./check-workstream-slug.sh "pm-portfolio-ratification-and-aeon-submission"
#      → exit 1, prints WARN block listing the matching branch + worktree
#        path + ahead/dirty state + classification.
#   c. Invalid input:
#        ./check-workstream-slug.sh ""               → exit 2 (missing arg)
#        ./check-workstream-slug.sh "slug with spaces" → exit 2 (invalid chars)
#        ./check-workstream-slug.sh "slug_with_underscores" → exit 2 (no underscores)
#   d. Stale collision (no commits >24h + ahead=0 + dirty=0):
#        ./check-workstream-slug.sh "<known-stale-slug>"
#      → exit 1, prints WARN with "STALE" classification + cleanup
#        suggestion.

set -uo pipefail

MAIN_REPO="/Users/c17n/commons-bonds"
STALE_AGE_SECONDS=86400  # 24h threshold for stale classification

# §5.1 contaminated branches — kept in sync with the canonical lists in
# session-end-worktree-cleanup.sh + session-start-orphan-lock-recovery.sh.
# Sourced from tools/workstream-handoffs/git-cleanup-sweep_2026-05-28.md §5.1.
CONTAMINATED_BRANCHES=(
  "claude/ch9-pass3-5-1fae85"
  "claude/ch9-stage5-pm-handoff-1fae85"
)

# Logging helpers.
log()  { echo "[check-workstream-slug] $*"; }
warn() { echo "[check-workstream-slug] WARN: $*"; }
err()  { echo "[check-workstream-slug] ERROR: $*" >&2; }

# --- Argument validation -----------------------------------------------------

if [ "$#" -ne 1 ]; then
  err "usage: $(basename "$0") <workstream-slug>"
  exit 2
fi

slug="$1"

# Slug rules: lowercase letters + digits + hyphens; no leading/trailing
# hyphen; 3-50 chars.
if ! [[ "$slug" =~ ^[a-z0-9][a-z0-9-]{1,48}[a-z0-9]$ ]]; then
  err "invalid slug '$slug'"
  err "rules: lowercase letters + digits + hyphens only; 3-50 chars;"
  err "       no leading/trailing hyphen; no underscores; no spaces."
  exit 2
fi

# --- Main-repo presence check ------------------------------------------------

if [ ! -d "$MAIN_REPO/.git" ]; then
  err "main repo not found at $MAIN_REPO; cannot check collisions."
  exit 2
fi

# --- Branch enumeration ------------------------------------------------------

# Match liberally:
#   - modern canonical: claude/<slug>-YYMMDD-XXXXXX (6 digits + 6 hex)
#   - legacy:          claude/<slug>-XXXXXX        (just 6 hex)
# Anchored at slug boundary to prevent false positives on near-name slugs
# (e.g., "ch4" must not match "ch4-stage5-260530-abcdef").
match_re="^claude/${slug}-([0-9]{6}-[a-f0-9]{6}|[a-f0-9]{6})$"

# Collect local branches.
local_branches="$(
  git -C "$MAIN_REPO" branch --format='%(refname:short)' 2>/dev/null \
    | grep -E "$match_re" || true
)"

# Collect remote branches (tolerate offline / no-origin).
remote_branches=""
if git -C "$MAIN_REPO" remote get-url origin >/dev/null 2>&1; then
  remote_branches="$(
    git -C "$MAIN_REPO" ls-remote --heads origin "refs/heads/claude/${slug}-*" 2>/dev/null \
      | awk '{print $2}' \
      | sed 's|^refs/heads/||' \
      | grep -E "$match_re" || true
  )"
fi

# Union + deduplicate. Use printf so empty strings collapse cleanly.
all_branches="$(
  { printf '%s\n' "$local_branches"; printf '%s\n' "$remote_branches"; } \
    | grep -v '^$' \
    | sort -u || true
)"

if [ -z "$all_branches" ]; then
  log "OK: slug '$slug' is clear (no matching branches local or remote)."
  exit 0
fi

# --- Collision: build a worktree-path map ------------------------------------

# Parse `git worktree list --porcelain` once.
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

if [ -n "$current_path" ]; then
  wt_paths+=("$current_path")
  wt_branches+=("$current_branch")
fi

# Lookup helper: branch -> worktree path (or empty if no active worktree).
lookup_worktree_path() {
  local target_branch="$1"
  local i
  for i in "${!wt_branches[@]}"; do
    if [ "${wt_branches[$i]}" = "$target_branch" ]; then
      echo "${wt_paths[$i]}"
      return 0
    fi
  done
  return 1
}

# Refresh origin/main once so ahead/behind reflects current upstream.
# Tolerate offline.
git -C "$MAIN_REPO" fetch --quiet origin main 2>/dev/null || true

# --- Per-match reporting -----------------------------------------------------

now_epoch="$(date +%s)"
match_count=0
contaminated_seen=0

warn "slug '$slug' collides with existing branch(es). Detail:"
echo ""

while IFS= read -r branch; do
  [ -z "$branch" ] && continue
  match_count=$((match_count + 1))

  # Contamination skip-list awareness.
  is_contaminated=0
  for cb in "${CONTAMINATED_BRANCHES[@]}"; do
    if [ "$branch" = "$cb" ]; then
      is_contaminated=1
      contaminated_seen=$((contaminated_seen + 1))
      break
    fi
  done

  # Resolve worktree path.
  wt_path=""
  wt_path="$(lookup_worktree_path "$branch" || true)"

  # Determine the ref we can query for ahead/dirty/age. Prefer the local
  # branch name if it exists locally; otherwise fall back to the remote-
  # tracking ref `origin/<branch>`.
  query_ref="$branch"
  if ! git -C "$MAIN_REPO" rev-parse --verify --quiet "refs/heads/$branch" >/dev/null 2>&1; then
    if git -C "$MAIN_REPO" rev-parse --verify --quiet "refs/remotes/origin/$branch" >/dev/null 2>&1; then
      query_ref="origin/$branch"
    else
      query_ref=""
    fi
  fi

  ahead="unknown"
  last_commit_age_label="unknown"
  if [ -n "$query_ref" ]; then
    ahead="$(git -C "$MAIN_REPO" rev-list --count "origin/main..$query_ref" 2>/dev/null || echo "unknown")"
    last_epoch="$(git -C "$MAIN_REPO" log -1 --format=%ct "$query_ref" 2>/dev/null || echo "")"
    if [ -n "$last_epoch" ]; then
      age=$((now_epoch - last_epoch))
      if   [ "$age" -lt 3600 ];   then last_commit_age_label="$((age / 60))m ago"
      elif [ "$age" -lt 86400 ];  then last_commit_age_label="$((age / 3600))h ago"
      else                              last_commit_age_label="$((age / 86400))d ago"
      fi
    fi
  fi

  # Dirty check if there's an active worktree.
  dirty_label="n/a"
  dirty_count=0
  if [ -n "$wt_path" ] && [ -d "$wt_path" ]; then
    dirty_raw="$(git -C "$wt_path" status --porcelain 2>/dev/null || true)"
    if [ -n "$dirty_raw" ]; then
      dirty_count="$(printf '%s\n' "$dirty_raw" | grep -c '.' || true)"
      dirty_label="$dirty_count uncommitted/untracked"
    else
      dirty_label="clean"
    fi
  fi

  # Stale vs active classification:
  #   stale = no worktree dirty + ahead=0 + last commit >24h ago
  classification="ACTIVE"
  if [ "$is_contaminated" = "1" ]; then
    classification="CONTAMINATED (§5.1 skip-list)"
  elif [ "$ahead" = "0" ] && { [ "$dirty_label" = "n/a" ] || [ "$dirty_label" = "clean" ]; }; then
    if [ -n "$last_epoch" ] && [ "$((now_epoch - last_epoch))" -ge "$STALE_AGE_SECONDS" ]; then
      classification="STALE"
    fi
  fi

  # Per-match output block.
  echo "  - Branch:        $branch"
  if [ -n "$wt_path" ]; then
    echo "    Worktree:      $wt_path"
  else
    echo "    Worktree:      (branch only; no active worktree)"
  fi
  echo "    Last commit:   $last_commit_age_label"
  echo "    Ahead origin/main: $ahead"
  echo "    Dirty:         $dirty_label"
  echo "    Class:         $classification"
  echo ""
done <<< "$all_branches"

# --- Suggestions block -------------------------------------------------------

echo "Options:"
echo "  - Pick a more specific slug (e.g., '${slug}-rerun', '${slug}-v2',"
echo "    '${slug}-followup', or refine the slug to name THIS session's work)."
if [ -n "$all_branches" ] && [ "$contaminated_seen" -lt "$match_count" ]; then
  echo "  - If a match above is classified STALE, clean it up first:"
  echo "      git -C $MAIN_REPO worktree remove <stale-path> 2>/dev/null"
  echo "      git -C $MAIN_REPO branch -D <stale-branch>"
  echo "    (Verify ahead=0 + clean before deleting; do NOT clean up CONTAMINATED entries — they require detective triage per git-cleanup-sweep_2026-05-28.md §5.1.)"
fi
echo "  - If you intend to RESUME an existing workstream listed above,"
echo "    attach to the existing worktree path instead of spawning a new"
echo "    one. cd into the path and continue work there."
echo "  - To proceed anyway despite the collision (rare; intentional"
echo "    intra-slug sub-session), set FORCE_SLUG_COLLISION=1 in the"
echo "    calling shell before running 'git worktree add -b'."
echo ""

exit 1
