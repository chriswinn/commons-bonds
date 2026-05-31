---
name: Git workflow — pointer (superseded; see canonical sources)
description: Pointer entry. The branch-discipline + merge-to-main + worktree-isolation content this file once carried has been superseded; canonical sources listed below. Historical anchor (iCloud incident 2026-04-29) preserved here.
type: feedback
originSessionId: 80ad4adb-2fd4-4856-a660-ec55f1ce325e
---
**Canonical content lives at:**
- `CLAUDE.md` §"Branch discipline + merge-to-main" — current rule (merge-on-ratification 2026-05-28; auto-merge-internal-scaffolding 2026-05-24; pre-push reconciliation pattern; escape-hatch commit markers `MERGE-HOLD:` / `MERGE-AFTER:`).
- [`feedback_worktree_isolation_for_parallel_sessions.md`](feedback_worktree_isolation_for_parallel_sessions.md) — worktree-isolation discipline (2026-05-26), which superseded this file's earlier `.claude/worktrees/<session-name>` pattern when parallel-session operation (20-35+ concurrent CC sessions) made shared-`.git/HEAD` branch-contamination the failure mode to design against.
- [`feedback_merge_on_ratification.md`](feedback_merge_on_ratification.md) — merge-on-ratification rule (2026-05-28), which superseded this file's session-end-merge cadence by making ratification itself the merge authorization.

**Historical anchor (preserved 2026-05-31):** the originating empirical anchor for Working Principle #9 was the **iCloud incident 2026-04-29** — the working tree at `~/Documents/___WorkingOn/commons-bonds` was corrupted mid-session by iCloud sync, ~70 files deleted while being edited. The fragility of single-checkout direct-to-main discipline under concurrent author + Claude operation drove the original ratification of worktree isolation + ratified-chunk fast-forward to main. Subsequent amendments (2026-05-10 active-push expectation; 2026-05-24 internal-scaffolding auto-merge; 2026-05-26 parallel-session worktree isolation; 2026-05-28 merge-on-ratification) all extend this lineage rather than replace it. This pointer preserves the *why* even though the operational details now live in the canonical sources above.

**Discipline reminder.** Hard constraints (unchanged across all amendments): never force-push `main`; never amend a commit already on `origin/main`; never skip hooks (`--no-verify`) without explicit author direction.

---

Collapsed 2026-05-31 per memory-process-review_2026-05-28.md §5 A.4 ratification (Option D1: collapse to 3-line pointer; preserve iCloud-incident historical anchor). Prior content carried 31 lines of canonical-rule duplication; canonical rule now lives in `CLAUDE.md`. The retained material is the pointer + historical anchor only.
