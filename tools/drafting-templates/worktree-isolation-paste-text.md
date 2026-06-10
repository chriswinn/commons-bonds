# Worktree-isolation paste-text (FIRST-ACTION block for every fresh session)

**Date drafted:** 2026-05-26
**Purpose.** Canonical first-action block to be embedded at the TOP of every kick-off paste-text. Prevents the branch-contamination failure mode documented in [`../memory/feedback_worktree_isolation_for_parallel_sessions.md`](../memory/feedback_worktree_isolation_for_parallel_sessions.md): multiple parallel CC sessions sharing the same physical working directory (`/Users/c17n/commons-bonds`) silently overwrite each other's `HEAD` and commit each other's working-tree changes to the wrong branches.

**When to use.** Embed the copy-paste block below as the FIRST instruction in any fresh-session kick-off paste-text. The session's first tool call MUST be the worktree-isolation step before any other work.

**Defense-in-depth pair.** The `SessionStart` hook at [`../scripts/session-start-worktree-isolation.sh`](../scripts/session-start-worktree-isolation.sh) emits a session-context warning that mirrors this paste-text. Either mechanism alone reduces the contamination risk; both together close it.

**Session-lifecycle companion hooks (added 2026-05-31; G1 + orphan-lock-recovery + G4 slug-collision).** Three additional hooks / scripts run automatically around the worktree-isolation discipline:

- **`SessionStart` orphan-lock recovery** ([`../scripts/session-start-orphan-lock-recovery.sh`](../scripts/session-start-orphan-lock-recovery.sh)) — at session start, ordered after the isolation hook, scans `.claude/worktrees/agent-*/locked` markers; if the locking pid is dead + ahead=0 vs origin/main + dirty=0 + not on the §5.1 contaminated skip-list, auto-runs `git worktree unlock` + `git worktree remove --force` + best-effort `git branch -D`. Resolves the orphan-lock-from-killed-agent failure mode.
- **`SessionEnd` worktree cleanup (G1 session-end branch-delete default)** ([`../scripts/session-end-worktree-cleanup.sh`](../scripts/session-end-worktree-cleanup.sh)) — at session close, if cwd is a top-level isolated worktree on a `claude/<slug>-<harness>` branch AND the same safety gates pass (ahead=0; dirty=0; no `MERGE-HOLD:`/`MERGE-AFTER:` commit-body markers; not contaminated), auto-runs `git worktree remove + git branch -D`. The session does not need to manually clean up its worktree at close — this hook does it. Honors merge-on-ratification escape hatches per CLAUDE.md §Branch discipline.
- **Slug-collision pre-check (G4)** ([`../scripts/check-workstream-slug.sh`](../scripts/check-workstream-slug.sh)) — invoked from the copy-paste block below BEFORE `git worktree add -b`. Read-only. Catches the parallel-session failure mode where two independent sessions pick the same workstream slug, fragmenting work across distinct harness-id-suffixed branches (most common) or, rarely, hard-colliding on a shared date+hex harness. On collision, exits non-zero + prints matching branch(es) + worktree path(s) + STALE/ACTIVE/CONTAMINATED classification + suggested resolutions. Escape hatch for intentional intra-slug sub-sessions: `FORCE_SLUG_COLLISION=1` in the calling shell. Resolves PM-handoff G4 per [`../workstream-handoffs/archive/pm-session-handoff_2026-05-28.md`](../workstream-handoffs/archive/pm-session-handoff_2026-05-28.md) project-review backlog.

The two session-lifecycle hooks (orphan-lock + SessionEnd) are dry-run by default and require `COMMONS_BONDS_HOOK_DESTRUCTIVE=1` to actually run. The G4 pre-check is always read-only (no destructive mode exists; it only reports). All three complement (do not replace) the isolation hook + the paste-text discipline.

---

## Copy-paste block

```
FIRST ACTION — WORKTREE ISOLATION (MANDATORY before any other tool call).

Branch-contamination root cause: parallel Claude Code sessions running
in the same physical working directory (`/Users/c17n/commons-bonds`)
share the same `.git/HEAD`. When session A runs `git checkout`, every
other session running in that same cwd now sees HEAD pointing to
session A's branch. Any uncommitted edits in working tree get
attributed to the wrong branch on the next `git commit`. Multiple
workstreams entangle on a single branch.

Discipline: every fresh session creates an isolated git worktree at
session start, before any other work. Worktrees share the `.git`
directory but have INDEPENDENT working trees + HEAD refs — no cross-
session HEAD interference.

Execute as your FIRST tool call (substitute <workstream-slug> with a
descriptive short slug for this session's work; harness ID auto-
generated from a timestamp + random suffix):

```bash
# Run this from anywhere — the worktree gets created at an absolute path
HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
WORKSTREAM="<workstream-slug>"  # e.g. "ch4-stage5", "wave-2-ch4-fa-ratify", "pm-cascade-v2-amend"
BRANCH="claude/${WORKSTREAM}-${HARNESS_ID}"
WORKTREE_PATH="/Users/c17n/commons-bonds-${WORKSTREAM}-${HARNESS_ID}"

# G4 — slug-collision pre-check (added 2026-05-31). Read-only. Catches
# the parallel-session failure mode where two sessions pick the same
# workstream slug. On collision, the script prints matching branch(es) +
# worktree path(s) + STALE/ACTIVE/CONTAMINATED classification, and this
# block aborts so the model can surface options to the author.
if ! /Users/c17n/commons-bonds/tools/scripts/check-workstream-slug.sh "${WORKSTREAM}"; then
  echo ""
  echo "🔴 G4 PRE-CHECK: workstream slug '${WORKSTREAM}' appears to collide with existing branches."
  echo "Review the warnings above. Options:"
  echo "  - Pick a more specific slug (e.g., '${WORKSTREAM}-rerun', '${WORKSTREAM}-v2',"
  echo "    or refine to name THIS session's work)."
  echo "  - If existing matches are STALE (no recent commits, ahead=0, clean), clean them up first:"
  echo "      git -C /Users/c17n/commons-bonds worktree remove <stale-path> 2>/dev/null"
  echo "      git -C /Users/c17n/commons-bonds branch -D <stale-branch>"
  echo "    Do NOT clean up CONTAMINATED entries — those require detective triage per"
  echo "    git-cleanup-sweep_2026-05-28.md §5.1."
  echo "  - If resuming an existing workstream, attach to that worktree instead of spawning new."
  echo "  - To proceed anyway (rare; intentional intra-slug sub-session), set FORCE_SLUG_COLLISION=1."
  if [ "${FORCE_SLUG_COLLISION:-0}" != "1" ]; then
    echo ""
    echo "Aborting worktree creation. Re-run with a refined slug, or set FORCE_SLUG_COLLISION=1 to override."
    return 1 2>/dev/null || exit 1
  fi
  echo "FORCE_SLUG_COLLISION=1 set; proceeding despite warning."
fi

git -C /Users/c17n/commons-bonds fetch origin main
git -C /Users/c17n/commons-bonds worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main

# All subsequent tool calls in this session use absolute paths inside
# ${WORKTREE_PATH}. The session does NOT cd back to
# /Users/c17n/commons-bonds for any operation — that's the contamination
# attractor.
echo "Worktree-isolated at: ${WORKTREE_PATH}"
echo "Branch: ${BRANCH}"
```

After the worktree is created, all subsequent Read/Edit/Write/Bash
operations in this session use paths under `${WORKTREE_PATH}`. The
session-end push is from this branch to `origin/main` via
`git push -u origin ${BRANCH}` then `git push origin HEAD:main` per
CLAUDE.md merge-to-main discipline.

If you are RESUMING an existing worktree (e.g., the session-start
context already shows you in /Users/c17n/commons-bonds-<existing>),
skip this step — you're already isolated.

If you encounter a SessionStart hook warning telling you about this,
that warning is the system's defense-in-depth catch and it agrees
with this paste-text.
```

---

## Where this block is embedded

Every kick-off paste-text MUST embed the block above as its first
instruction (before required-reads, before workstream-specific
guidance). The current set of templates:

- [`README.md`](README.md) — generic drafting-trigger scaffold
- [`existing-session-checkin-paste-text.md`](existing-session-checkin-paste-text.md) — upgrade paste-text for sessions started before 2026-05-26
- [`stage-0-publishing-strategy-rigor-test.md`](stage-0-publishing-strategy-rigor-test.md)
- [`stage-1-audience-aware-structure-pass.md`](stage-1-audience-aware-structure-pass.md)
- [`stage-2-audience-blind-flow-draft.md`](stage-2-audience-blind-flow-draft.md)
- [`stage-3-three-pass-rigor-audit.md`](stage-3-three-pass-rigor-audit.md)
- [`audience-pressure-test-construction.md`](audience-pressure-test-construction.md)
- [`op-ed-news-peg-activation-template.md`](op-ed-news-peg-activation-template.md)
- [`../workstream-handoffs/wave-2-derivative-kickoffs_2026-05-24.md`](../workstream-handoffs/wave-2-derivative-kickoffs_2026-05-24.md) — Wave 2 candidate kick-offs (bundle)
- Future kick-off paste-text bundles inherit this requirement

**Rule:** if a kick-off paste-text DOESN'T embed the worktree-isolation block as its first instruction, that template is broken and needs immediate update.

---

## Why this layer of friction is the right tradeoff

Author observation 2026-05-26: under sustained 20–35 parallel sessions, the cost of contamination (sessions writing to each other's branches; manual triage to untangle multiple workstreams from a single branch) exceeds the friction of every session creating a worktree at start (~5 seconds; one `git worktree add`).

The `worktree-agent-*` branches under `.claude/worktrees/agent-<id>` show that the Claude Code Agent tool's `isolation: "worktree"` parameter already creates isolated worktrees for sub-agent invocations. This paste-text extends the same discipline to top-level sessions which don't automatically isolate.

## Update log

- **2026-05-26.** Initial draft. Created in response to author observation that 350+ branches accumulated with active cross-session contamination on `claude/ch9-stage5-pm-handoff-1fae85` and similar polyworkstream branches. PM session diagnosis: root cause is shared `.git/HEAD` across parallel sessions in same physical cwd; fix is mandatory worktree isolation per fresh session.
- **2026-05-31.** G4 slug-collision pre-check added — copy-paste block now invokes [`../scripts/check-workstream-slug.sh`](../scripts/check-workstream-slug.sh) before `git worktree add -b`. Resolves PM-handoff G4 (MED) per [`../workstream-handoffs/archive/pm-session-handoff_2026-05-28.md`](../workstream-handoffs/archive/pm-session-handoff_2026-05-28.md) project-review backlog. Escape hatch: `FORCE_SLUG_COLLISION=1` for intentional intra-slug sub-sessions.

---

*End of worktree-isolation paste-text.*
