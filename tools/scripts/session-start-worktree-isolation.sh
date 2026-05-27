#!/usr/bin/env bash
# session-start-worktree-isolation.sh — SessionStart hook for worktree
# isolation.
#
# Purpose: prevent parallel-session branch contamination (multiple
# sessions sharing /Users/c17n/commons-bonds/.git/HEAD overwriting each
# other's branches). When a fresh session starts in the main repo
# working directory, emit a strongly-worded reminder + ready-to-paste
# worktree-creation block. The LLM is responsible for executing the
# worktree-isolation step as its first tool call.
#
# Companion paste-text: tools/drafting-templates/worktree-isolation-paste-text.md
# Companion memory: tools/memory/feedback_worktree_isolation_for_parallel_sessions.md
#
# Detection logic:
#   - If `git rev-parse --show-toplevel` returns the main project
#     directory ($CLAUDE_PROJECT_DIR or its symlink-resolved form),
#     the session is in the MAIN cwd → emit warning.
#   - If `git rev-parse --show-toplevel` returns a path under
#     `.claude/worktrees/` or a sibling absolute path
#     (`/Users/c17n/commons-bonds-*`), the session is ALREADY in a
#     worktree → no-op.
#
# Per CC SessionStart hook docs: stdout content is added to session
# context; the LLM reads it as a system message at session start.
#
# Exit code 0 always — SessionStart hooks should not block session
# start on non-zero exit.

set -euo pipefail

# Resolve project root: prefer $CLAUDE_PROJECT_DIR, fall back to the
# script's grandparent.
project_dir="${CLAUDE_PROJECT_DIR:-}"
if [ -z "$project_dir" ]; then
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  project_dir="$(cd "${script_dir}/../.." && pwd)"
fi

# Canonicalize to handle symlinks / trailing slashes.
project_dir="$(cd "$project_dir" && pwd -P)"

# Determine current worktree's toplevel. If not in a git repo at all,
# skip silently — render-toolchain hook handles that case for its own
# install path.
if ! current_top="$(git rev-parse --show-toplevel 2>/dev/null)"; then
  exit 0
fi
current_top="$(cd "$current_top" && pwd -P)"

# If the current toplevel != the main project directory, we're already
# in an isolated worktree. No-op.
if [ "$current_top" != "$project_dir" ]; then
  exit 0
fi

# We're in the main cwd. Emit a strongly-worded reminder to stdout
# (which Claude Code adds to session context as a system-reminder).

# Read the canonical paste-text from disk for the message body.
paste_text="${project_dir}/tools/drafting-templates/worktree-isolation-paste-text.md"

cat <<'EOF'
================================================================
🔴 SESSION-START WORKTREE-ISOLATION WARNING (2026-05-26)
================================================================

This session has started in the MAIN repository working directory
(/Users/c17n/commons-bonds). Under sustained parallel-session
operation (20-35+ concurrent CC sessions, per author observation
2026-05-26), running fresh sessions in the main cwd causes
BRANCH CONTAMINATION: all parallel sessions share the same
.git/HEAD, so checkouts and commits from one session corrupt
the branch state of every other session.

MANDATORY FIRST ACTION: create an isolated git worktree BEFORE
any other tool call. Use the canonical paste-text at:

  tools/drafting-templates/worktree-isolation-paste-text.md

Quick template (substitute <workstream-slug> with a short
descriptive slug for THIS session's work; harness ID
auto-generated from timestamp + random suffix):

```bash
HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
WORKSTREAM="<workstream-slug>"  # e.g. "ch4-stage5", "pm-refresh"
BRANCH="claude/${WORKSTREAM}-${HARNESS_ID}"
WORKTREE_PATH="/Users/c17n/commons-bonds-${WORKSTREAM}-${HARNESS_ID}"

git -C /Users/c17n/commons-bonds fetch origin main
git -C /Users/c17n/commons-bonds worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main

echo "Worktree-isolated at: ${WORKTREE_PATH}"
echo "Branch: ${BRANCH}"
```

After running the worktree-add command, every subsequent tool
call in this session must use absolute paths inside the new
${WORKTREE_PATH}. The session does NOT cd back to
/Users/c17n/commons-bonds for any operation.

If you are intentionally working in the main cwd (e.g., to
inspect cross-worktree state from a PM session that has already
isolated itself elsewhere), ignore this reminder — but be aware
that any commit you make in the main cwd is racing every other
parallel session's HEAD.

If you are RESUMING a session that is already worktree-isolated
elsewhere, the harness should have placed you in that worktree;
if you're seeing this reminder, something is off — verify before
proceeding.

Reference: tools/memory/feedback_worktree_isolation_for_parallel_sessions.md
================================================================
EOF

exit 0
