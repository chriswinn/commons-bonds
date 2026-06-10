# feedback_worktree_isolation_for_parallel_sessions (v1.0.0)

**Date ratified:** 2026-05-26
**Type:** feedback (operational discipline)
**Origin:** Author observation 2026-05-26 (PM cascade-v2-ratification session) — 350+ Claude Code branches accumulated with active cross-session branch contamination on `claude/ch9-stage5-pm-handoff-1fae85` and similar polyworkstream branches. PM session diagnosed root cause + proposed fix; author ratified the SessionStart hook + paste-text + memory-codification approach.
**Canonical reference:** this file. Companion artifacts: [`../scripts/session-start-worktree-isolation.sh`](../scripts/session-start-worktree-isolation.sh) (SessionStart hook), [`../drafting-templates/worktree-isolation-paste-text.md`](../drafting-templates/worktree-isolation-paste-text.md) (first-action paste-text), [`../drafting-templates/existing-session-checkin-paste-text.md`](../drafting-templates/existing-session-checkin-paste-text.md) (§0 upgrade for existing sessions).

## Summary

**Every fresh Claude Code session for the *Commons Bonds* project starts in an isolated git worktree.** Sessions never share the main repository's `.git/HEAD` with each other. The first tool call of every session is `git worktree add ... origin/main`. After that, all subsequent tool calls in that session use absolute paths inside the new isolated worktree.

This discipline prevents branch contamination — the failure mode where parallel sessions in the same physical working directory silently overwrite each other's branches via shared `.git/HEAD`.

## Root cause (why this discipline is necessary)

A single git working directory has exactly one `.git/HEAD` ref. When `N` Claude Code sessions all open Bash tool calls in the same physical cwd (`/Users/c17n/commons-bonds`), they all read + write the same `.git/HEAD`. When session A runs `git checkout claude/X`, every other session running in that cwd now sees its HEAD pointing to `claude/X` — and any uncommitted edits they had in working tree get attributed to `claude/X` on next commit.

Under low parallelism (3–6 sessions), this is rarely-fires (long gaps between checkouts; humans serialize their attention). Under sustained 20–35+ parallel sessions, the race conditions compound. The contamination isn't "random" — it's deterministic: whoever did the last `git checkout` wins HEAD; whoever does the next `git commit` lands on that branch.

**Empirical anchor (2026-05-26).** The session-start `gitStatus` snapshot for this PM session showed `claude/ch9-pass3-5-1fae85` with five modified files in working tree, including `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md` (+35-line addition: the Ch 2 Harper's ratification record). That record was authored by a Wave 2 Ch 2 ratification session — a totally separate workstream from Ch 9 Pass 3.5. The Ch 9 branch had also been renamed `claude/ch9-stage5-pm-handoff-1fae85` — three workstream names (Ch 9 + Stage 5 + PM handoff) entangled on one branch.

Across 350+ branches, the contamination pattern accumulated to the point where the author observed "sessions just swapping branches they were committing in seemingly at random."

## The discipline (going forward 2026-05-26)

### Fresh session start (mandatory)

Every fresh CC session's FIRST tool call is the worktree-isolation step:

```bash
HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
WORKSTREAM="<workstream-slug>"  # short descriptive slug
BRANCH="claude/${WORKSTREAM}-${HARNESS_ID}"
WORKTREE_PATH="/Users/c17n/commons-bonds-${WORKSTREAM}-${HARNESS_ID}"

git -C /Users/c17n/commons-bonds fetch origin main
git -C /Users/c17n/commons-bonds worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main
```

All subsequent tool calls use absolute paths inside `${WORKTREE_PATH}`. The session does NOT `cd` back to `/Users/c17n/commons-bonds` for any operation — that's the contamination attractor.

### Existing-session upgrade

Existing sessions started before 2026-05-26 are at contamination risk. The check-in paste-text at [`../drafting-templates/existing-session-checkin-paste-text.md`](../drafting-templates/existing-session-checkin-paste-text.md) §0 walks any existing session through migration to an isolated worktree, handling the uncommitted-work edge case.

### Defense in depth — three layers

1. **SessionStart hook** ([`../scripts/session-start-worktree-isolation.sh`](../scripts/session-start-worktree-isolation.sh)) — fires automatically on every session start. If `git rev-parse --show-toplevel` returns `/Users/c17n/commons-bonds` (the main cwd), the hook emits a strongly-worded session-context warning + ready-to-paste worktree command. If the session is already in an isolated worktree, the hook is silent.
2. **First-action paste-text** ([`../drafting-templates/worktree-isolation-paste-text.md`](../drafting-templates/worktree-isolation-paste-text.md)) — referenced from every kick-off paste-text template in `../drafting-templates/`. Every fresh session reading any template sees the FIRST ACTION requirement.
3. **Memory entry** (this file) — codifies the discipline for cross-session reference.

### Session close

When a session completes its work and prepares for merge-to-main per [CLAUDE.md](../../CLAUDE.md) policy:

```bash
# From inside the isolated worktree
git push -u origin "${BRANCH}"
git push origin HEAD:main   # only for internal-scaffolding per CLAUDE.md

# Clean up worktree (only after push succeeds)
cd /Users/c17n/commons-bonds
git worktree remove "${WORKTREE_PATH}"
```

Worktree cleanup at session close prevents `.claude/worktrees/agent-*` orphan accumulation (the project currently has 19 such orphans, locked from the Agent tool's `isolation: "worktree"` mechanism).

## Edge cases

### EC1 — Resuming an existing session

If a session is resuming AND that session already created an isolated worktree on a prior turn, the CC harness places the session back in that worktree. The SessionStart hook detects this (current toplevel != main cwd) and stays silent. No action required.

### EC2 — Session explicitly needs to inspect cross-worktree state

The PM session occasionally needs to scan branches/commits across all worktrees (e.g., the §10b parallel-session inventory refresh). This is fine to do from inside the PM session's isolated worktree using `git for-each-ref` / `git log --all` / `git worktree list` — those commands read the shared `.git` directory without needing the main cwd. They do not need the main cwd to be checked out at any particular branch.

### EC3 — Session author explicitly directs work in main cwd

If the author explicitly directs a session to work in `/Users/c17n/commons-bonds` (e.g., "do a quick `git status` from the main repo"), honor that — but only for read-only operations. Any write operation (commit, checkout, stash, etc.) in the main cwd risks contamination and should be flagged.

### EC4 — Agent tool sub-session with `isolation: "worktree"`

The Agent tool's `isolation: "worktree"` parameter creates a worktree under `.claude/worktrees/agent-<id>`. This is a parallel mechanism to top-level session isolation and continues to operate independently. Sub-sessions use the harness mechanism; top-level sessions use the paste-text + hook mechanism. Both produce isolated worktrees; both are safe.

## Triage discipline for already-contaminated branches

Per author direction 2026-05-26: "I'm working through and wrapping and closing all open sessions now." Contaminated branches require detective-work per-branch:

1. `git log <contaminated-branch> --oneline -50` — identify commit-by-commit which workstream each commit belongs to.
2. Cherry-pick wrong-branch commits onto their correct destination branches.
3. Leave the now-clean branch (which should only contain its original workstream's commits) as the canonical record for that workstream.
4. Branch-pruning of fully-merged historical branches is a separate hygiene pass.

Known polyworkstream-contaminated branches (PM cascade-v2-ratification session 2026-05-26 surfaced):
- `claude/ch9-stage5-pm-handoff-1fae85` (renamed from `claude/ch9-pass3-5-1fae85`) — Ch 9 Pass 3.5 + Stage 5 + PM handoff + Wave 2 Stage 0 file modifications all entangled.

Additional contaminated branches likely exist; surface them as the author closes open sessions and inspects branch histories.

## How to apply

### For every fresh session firing from a paste-text scaffold

1. The kick-off paste-text already includes the FIRST ACTION worktree-isolation reference (per templates updated 2026-05-26).
2. Session's first tool call is the `git worktree add` block from [`../drafting-templates/worktree-isolation-paste-text.md`](../drafting-templates/worktree-isolation-paste-text.md).
3. All subsequent tool calls use absolute paths in the isolated worktree.

### For every existing session you re-enter

1. If the SessionStart hook's warning surfaces in the conversation context on session resume, honor it.
2. If you're picking up a session from a stale context, paste [`../drafting-templates/existing-session-checkin-paste-text.md`](../drafting-templates/existing-session-checkin-paste-text.md) — §0 walks the session through the migration.

### For PM session coordination

1. The PM session's §10b parallel-session inventory tracks contamination status per branch.
2. When new contamination is detected (cross-workstream files in working tree on a wrong-workstream branch), surface in §10b notes column.
3. Branch-naming convention: a branch name like `claude/<workstream-A>-<workstream-B>-<harness>` is a sentinel for contamination — flag.

## Empirical anchors

- **2026-05-26 author observation.** "I have 350 branches and earlier today I had 35 sessions and for some reason the sessions started contaminating each others branches and just swapping branches they were committing in seemingly at random. I have no idea." — surfaced the failure mode; PM cascade-v2-ratification session diagnosed it as shared `.git/HEAD` contention.
- **2026-05-26 PM session worktree-isolation choice.** This PM session created an isolated worktree at `/Users/c17n/commons-bonds-pm-cascade-v2` (branch `claude/pm-session-cascade-v2-ratification-pm0525`) at session start precisely because the session-start gitStatus showed the suspect Wave 2 Stage 0 file modification on Ch 9's branch. The isolation prevented this session's edits to PM dashboard files from being attributed to Ch 9's branch. Worked example of the discipline operating as designed.
- **`.claude/worktrees/` directory** — already contains 19 harness-managed worktrees from the Agent tool's `isolation: "worktree"` parameter (e.g., `worktree-agent-a3a6c0dc4dc40a560`). The discipline above extends the same isolation pattern to top-level sessions that don't automatically get it from the Agent tool wrapper.
- **2026-05-27 Ch 2 → Harper's Phase C ratification session — wrong-path-edit self-incident (bounded; reconciled mid-session).** Session was correctly placed in agent worktree `agent-a3390c00c9b9a4df0` by harness on resume; SessionStart hook fired its main-cwd warning regardless (the session recognized it as a resumed-session false-positive per EC1 and proceeded). First-batch operations (PC-2 commit + Stage 1a invariant scan + clean-baseline `Write`) correctly used absolute paths under the agent worktree root. **The contamination crept in at the §18.4 ratification-record `Edit` calls against the Stage 1 brief**: tool calls used `/Users/c17n/commons-bonds/tools/rigor-passes/...` (main repo) instead of `/Users/c17n/commons-bonds/.claude/worktrees/agent-a3390c00c9b9a4df0/tools/rigor-passes/...` (agent worktree). Main repo at the time was on `claude/atlantic-ideas-essay-pass-3-5-ratify-and-phase-c-61cef166-5c1` (Atlantic Ideas Pass 3.5 parallel session); the Atlantic Ideas session's active modifications (`publishing/essays/atlantic-ideas-pricing-honestly/essay.md` + Pass 3.5 rigor-pass artifact + sign-off files) were disjoint from the Ch 2 → Harper's brief, so contamination was bounded — no parallel-session collision realized. Reconciled mid-session via `cp <main-path> <agent-worktree-path>` to move the edits + `git -C /Users/c17n/commons-bonds checkout -- <brief-path>` to restore the main repo brief. **Discipline lesson:** the SessionStart hook + paste-text discipline + per-session worktree creation prevent the *checkout/commit* contamination class (the load-bearing failure mode at the 350-branch-scale incident 2026-05-26), but they do NOT prevent *Edit/Write-tool drift* if the operator hand-constructs absolute paths against the main repo rather than the worktree root. Defense-in-depth options worth considering: (i) a session-resume reminder that explicitly states the worktree root + recommends Edit/Write call construction relative to it; (ii) hook-layer validation that warns when Edit/Write target paths fall outside the session's known-worktree-root (would catch this drift before it lands); (iii) per-session shell convenience variable `$WT=/Users/c17n/commons-bonds/.claude/worktrees/<id>` referenced in all tool calls instead of bare absolute paths. Logged 2026-05-27 by Ch 2 → Harper's Phase C session; companion PC-4 ratification artifact §3b at `publishing/essays/harpers-the-miner/rigor/stage-2-ratification-2026-05-27.md` carries the per-incident detail.

## Why this layer of friction is the right tradeoff

Cost of contamination (sessions writing to each other's branches; manual triage to untangle multiple workstreams from a single branch; "branches I have no idea what's in them" cleanup at scale) exceeds the friction of every session creating a worktree at start (~5 seconds; one `git worktree add` command).

Author throughput at 20–35+ parallel sessions is bounded by cognitive switching ceiling (per [`feedback_parallel_session_ratification_cadence.md`](feedback_parallel_session_ratification_cadence.md)), not by Bash command latency. A 5-second worktree-creation step is below the noise floor of session-start orientation overhead.

## Update log

- **2026-05-26 (v1.0.0).** Initial entry. Captured by PM cascade-v2-ratification session 2026-05-26 in response to author-surfaced branch-contamination observation. Companion artifacts (SessionStart hook + paste-text + existing-session-checkin upgrade + per-template FIRST ACTION references) created same session.
- **2026-05-27 (v1.0.1).** Empirical-anchors update: appended Ch 2 → Harper's Phase C ratification session 2026-05-27 wrong-path-edit self-incident (bounded; reconciled mid-session). Surfaces a distinct failure mode (Edit/Write-tool drift to main-repo absolute paths) that the v1.0.0 hook + paste-text infrastructure does NOT prevent. Three defense-in-depth options proposed; deferred to next PM session for evaluation. Captured by Ch 2 → Harper's Phase C session 2026-05-27 + author ratification "ratify all as recommended and proposed" 2026-05-27.

## Where to read more

- [`../drafting-templates/worktree-isolation-paste-text.md`](../drafting-templates/worktree-isolation-paste-text.md) — canonical first-action paste-text
- [`../drafting-templates/existing-session-checkin-paste-text.md`](../drafting-templates/existing-session-checkin-paste-text.md) — §0 upgrade for existing sessions
- [`../scripts/session-start-worktree-isolation.sh`](../scripts/session-start-worktree-isolation.sh) — SessionStart hook (defense in depth)
- [`../../.claude/settings.json`](../../.claude/settings.json) — hooks wiring
- [`feedback_parallel_session_ratification_cadence.md`](feedback_parallel_session_ratification_cadence.md) — companion cadence discipline
- [`feedback_git_workflow.md`](feedback_git_workflow.md) — branch + merge-to-main discipline

---

*End of worktree-isolation discipline entry.*
