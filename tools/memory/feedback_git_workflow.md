---
name: Git workflow — worktree isolation with session-end fast-forward to main
description: Commons Bonds project uses harness worktree on feature branch + ratified-chunk fast-forward merge to main, NOT push-every-commit-to-main
type: feedback
originSessionId: 80ad4adb-2fd4-4856-a660-ec55f1ce325e
---
**Canonical full content:** `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #9 + `CLAUDE.md` "Branch discipline + merge-to-main" section + `tools/workstream-handoffs/README.md`
**Layer:** scan-friendly summary; this file is the cross-session discipline pointer. Update the canonical artifact when content changes; sync this summary via `tools/memory-updates/` spec for substantive amendments.

The Commons Bonds project uses **worktree isolation with session-end fast-forward to main**, ratified 2026-04-29 as Working Principle #9 (`alignment/commons_bonds_working_principles_v1.0.0.md`).

**Why:** the iCloud incident 2026-04-29 (working tree at `~/Documents/___WorkingOn/commons-bonds` corrupted mid-session by iCloud sync, ~70 files deleted while being edited) plus the harness worktree pattern made the previous "direct-to-main, push each commit as it lands" rule fragile. Single-checkout discipline can't survive concurrent author + Claude operation. The new pattern preserves direct-to-main *linear history* (fast-forward only, no merge commits) but adds worktree isolation during the session.

**How to apply:**

- Chris's primary checkout: `/Users/c17n/commons-bonds` on `main`. Never touch.
- Claude's worktree: `/Users/c17n/commons-bonds/.claude/worktrees/<session-name>` on `claude/<session-name>` branch (harness-issued).
- During session: commits land on the feature branch in Claude's worktree. Do NOT push to main per commit.
- Session-end ritual (only when Chris ratifies a chunk):
  1. `git push -u origin claude/<session-name>` (record the session)
  2. `git push origin HEAD:main` (fast-forward origin/main to branch HEAD)
  3. Tell Chris to `git pull` in the primary checkout
- Cadence: merge per ratified chunk (one commit OR many), not per commit. Ratification by Chris is the gate.
- Expected error: `git fetch origin main:main` from Claude's worktree fails with "refusing to fetch into branch refs/heads/main checked out at /Users/c17n/commons-bonds" — by design. Treat `origin/main` as source of truth.
- If the chunk is small and pre-ratified by context (e.g., user explicitly approved the change), Claude can execute the merge ritual immediately without re-asking.
- **Active-push expectation (added 2026-05-10):** As ratified chunks complete, push them promptly — don't accumulate ratified work on the feature branch waiting for explicit "push now." Default behavior is push-on-chunk-completion. Author flagged 2026-05-10 mid-session after observing 3 ratified chunks sitting on the feature branch unpushed.
- **Pre-push reconciliation pattern:** Before fast-forwarding to main, `git fetch origin main` and `git rebase origin/main` to inherit any parallel-session work. If a parallel session resolved or contradicts something in the chunk being pushed, add a small reconciliation commit so what lands on main is consistent. Then push.

**Supersedes** the earlier session-handoff memory rule "Direct-to-main git workflow; push each commit as it lands." Direct-to-main is preserved at the ratified-chunk level, not the commit level.
