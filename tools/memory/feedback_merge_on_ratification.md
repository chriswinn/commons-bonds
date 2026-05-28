# feedback_merge_on_ratification

**Ratified:** 2026-05-28
**Supersedes:** 2026-05-16 "explicit author authorization before merge" gate for end-user-facing prose
**Canonical reference:** CLAUDE.md §"Branch discipline + merge-to-main"

## Summary

When author ratifies an end-user-facing prose change, the ratification IS the merge authorization. The session pushes the ratified commit to `origin/main` via the pre-push reconciliation pattern immediately after Phase C application, same mechanism as internal scaffolding. End-user-facing prose and internal scaffolding now share one merge discipline; only the trigger event differs (author-ratification vs session-close).

## Why this changed

The 2026-05-16 default had end-user-facing prose stay on its feature branch "until author ratifies + explicitly merges." Two pressures broke that default in practice:

1. **Active-push expectation (2026-05-10).** "As ratified chunks complete, push them promptly — don't accumulate ratified work on the feature branch waiting for explicit 'push now.'" Sessions doing the work couldn't simultaneously honor both rules.

2. **Parallel-session volume (2026-05-26 worktree-isolation discipline).** 20-35+ concurrent CC sessions means the author can't monitor every session's "ratified-but-not-merged" state. The explicit-merge gate assumed serial human attention; the actual workflow is heavily parallel.

The mismatch produced the failure mode: ratified prose stranded on feature branches indefinitely.

## Empirical anchor

**2026-05-27 Foreign Affairs essay situation.** The Ch 4 → Foreign Affairs essay completed its full Stage 3 (5-pass cascade) + Stage 4 + Stage 5 sign-off in a parallel session at `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e` between ~2026-05-27 07:00 and 13:15. 16 commits accumulated on the feature branch, including the 6,065-word ratified essay.md, the cover-letter.md, and Stage 5 RATIFIED status. The branch sat unmerged for ~6 hours.

The branch was only surfaced when the cross-essay portfolio review session ran at 2026-05-27 evening and inventoried which branches were ahead of main. The author then explicitly authorized merge via commit `3ae1777` ("Foreign Affairs essay — merge end-user-facing prose to main per author authorization 2026-05-27").

Net cost: ~6 hours of "what's the actual state of FA?" ambiguity across PM sessions; one extra commit + one extra author ratification step to clear a state that should have been default-merged the moment Stage 5 RATIFIED.

## The new rule

When the author ratifies an end-user-facing prose change, the session:

1. Applies the Phase C change locally (essay.md, cover-letter.md, op-ed.md, query-letter.md, etc. — any file under the end-user-facing-prose classification in CLAUDE.md).
2. Commits the ratified change with a normal message (no special tag needed).
3. Runs the pre-push reconciliation pattern: `git fetch origin main && git rebase origin/main`.
4. Pushes to `origin/main`: `git push origin HEAD:main`.

Same mechanism the session would use for internal scaffolding. No separate merge step. No waiting for a follow-up authorization.

## Escape hatches

Two commit-message body markers retain explicit-hold behavior for the rare cases where merge-on-ratification is the wrong default:

### `MERGE-HOLD: <reason>`

The session pushes to the feature branch only; `origin/main` is not touched. Use when:

- You want to inspect the merged state on the feature branch before further sessions touch the file.
- You're coordinating multiple parallel sessions that will conflict on the same file and want a specific merge ordering.
- You want to bundle several ratifications into one merge commit for atomicity.

The author surfaces a follow-up merge authorization when the hold reason clears (could be a separate session, or amended commit message that removes the marker).

### `MERGE-AFTER: <gate-description>`

The session waits for the named gate before merging. Use when the prose change is ratified but should not land until another condition fires (typically another session's ratification on a sibling file).

Example: "MERGE-AFTER: Ch 2 → Harper's Pass 3.5 RATIFIED on origin/main" — the session sets up the commit but defers merge until grep on origin/main confirms the gate fires.

## What still requires explicit author action (UNCHANGED)

**SUBMISSION** itself — sending the essay to the publisher / agent / editor; pressing submit on the portal; emailing the editor; uploading the cover-letter through the venue's portal.

Landing on `origin/main` is **not shipping**. It is syncing canonical repo state. The actual ship gate is the submission portal click / email send. This remains entirely author-controlled regardless of merge-to-main policy. The 2026-05-16 "irreversibility lives at the prose boundary" rationale still holds — but the prose boundary is at SUBMISSION, not at merge-to-main. 2026-05-28 relocates the gate to where it always belonged.

## How this interacts with existing disciplines

- **Pre-push reconciliation pattern (CLAUDE.md):** unchanged. Always rebase against `origin/main` before pushing.
- **Active-push expectation (2026-05-10):** reinforced. With merge-on-ratification, every ratification is an active-push event.
- **Worktree isolation (2026-05-26):** unchanged. Sessions still isolate before any commit.
- **Per-session protocol (CLAUDE.md):** updated. At session close, the session classifies its commits and auto-merges all ratified commits per merge-on-ratification, except those flagged with `MERGE-HOLD` or `MERGE-AFTER`.
- **Five-pass rigor cascade (v3.1 doctrine):** unchanged. Each pass's Phase C application is a ratification event; the merge happens after each one rather than accumulating to Stage 5.

## Migration of existing feature branches

Branches that ratified prose under the 2026-05-16 default but never merged should be swept and merged under the new policy. The git-cleanup-sweep session spawned 2026-05-28 covers this in its Phase A inventory + Phase C execution.

Per-branch decision rule for the sweep:
- Branch has ratified end-user-facing-prose commits ahead of main → merge per new policy + delete branch.
- Branch is mid-cascade (PROPOSED commits but not yet RATIFIED) → leave alone; the next session ratifies + merges normally.
- Branch is contaminated (multi-workstream entanglement) → per-branch detective session per `feedback_worktree_isolation_for_parallel_sessions.md`.

## Audit trail

- 2026-05-10: active-push expectation established.
- 2026-05-16: explicit-merge gate for end-user-facing prose established.
- 2026-05-24: internal scaffolding extended to auto-merge.
- 2026-05-26: worktree-isolation discipline ratified (20-35+ parallel sessions normalized).
- 2026-05-27: Foreign Affairs essay surfaces the failure mode (commit `3ae1777`).
- 2026-05-28: merge-on-ratification ratified; supersedes 2026-05-16 explicit-merge gate.

## How to apply

When firing a session that touches end-user-facing prose: at the moment of ratification + Phase C application, push to main immediately. No follow-up "now merge" session required. Document any hold reasons via `MERGE-HOLD:` / `MERGE-AFTER:` in the commit message body if the default is wrong for that ratification.

When orienting a fresh session: the merge-on-ratification rule is now CLAUDE.md canonical; sessions should not fall back to the 2026-05-16 explicit-merge gate. If a session asks "should I merge or wait for explicit authorization?", the answer is: ratify-then-merge is the default. Only wait if the commit message body carries a hold marker.
