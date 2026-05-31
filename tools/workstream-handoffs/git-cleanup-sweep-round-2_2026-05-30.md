# Git Cleanup Sweep — Round 2 — 2026-05-29 → 2026-05-30

**Status:** Phase A inventory + Phase B prune proposal **PROPOSED** (this artifact). Author authorization for Phase C destructive execution requested in §7.
**Worktree:** `/Users/c17n/commons-bonds-git-cleanup-sweep-2-260529-2f296e` (branch `claude/git-cleanup-sweep-2-260529-2f296e` off `origin/main`).
**Round 1 reference:** [`git-cleanup-sweep_2026-05-28.md`](git-cleanup-sweep_2026-05-28.md) (still on main; verified via `git ls-tree`).
**Round 1 close:** 348 → 14 branches, 66 → 7 worktrees. Round 2 inventories the regrowth across ~24h + reissues recommendations.

---

## §0. Headline numbers

| Object | Round 1 close | Round 2 start | Δ in ~24h |
|---|---:|---:|---:|
| Local branches | 14 | **76** | **+62** |
| Worktrees | 7 | **67** | **+60** |
| Locked agent worktrees | 0 | 2 | +2 (both pids DEAD) |
| Branches ahead of main | 7 | 7 | 0 — **identical set** as Round 1 close (5 §5.2 deferred + 2 §5.1 contaminated) — 0 new ahead branches |
| Worktrees claiming `main` | 1 | 1 | 0 (canonical) |

**Headline:** the Round 1 §9 hook recommendations are still not adopted at the harness layer. The same session-close-discipline gap produced 60 new orphan worktrees in 24h. However, **one session executed proper session-close mid-sweep** (commit `b1c17da` "PM session handoff 2026-05-28 evening" + worktree auto-removal at 13:38) — confirming the per-session discipline IS being internalized; the gap is at hook/automation.

**What drove the regrowth:** a 2026-05-28 portfolio-wide Aeon-pattern application sprint produced a structured grid: 10 publication units × ~6 variants each = ~55 worktrees, plus ~5 non-essay workstreams. Substantive work was legitimate (parallel-comparison audits supporting V-D-vs-LOCKED ratification — see new PM dashboard `pm-session-handoff_2026-05-28-portfolio-aeon-pattern-complete.md`, commit `b1c17da` on origin/main). The cleanup gap is purely that ~60 sessions never ran their session-close ritual.

---

## §1. Critical anomalies (none new)

Round 1 §1 flagged 6 anomalies (main-repo HEAD drift, two-main-claimants, contamination, duplicate spawns, raw-named branches, Ch 9 contamination). All except Ch 9 contamination (§5.1; still deferred) **remain resolved** from Round 1. **No new anomalies in Round 2.**

**One in-flight preservation event was detected AND resolved itself mid-sweep:**

- The `pm-cascade-v2-amend-morning-260527-1b419b` worktree initially had `dirty=1` (untracked 256-line, 16,913-byte PM dashboard `tools/workstream-handoffs/pm-session-handoff_2026-05-28-portfolio-aeon-pattern-complete.md`).
- This sweep paused, read the file, considered preserving via copy+commit per Round 1 §8.5 discipline.
- Within ~30 seconds of inspection, the active 1b419b PM session executed its own session-close ritual: committed the dashboard to origin/main as `b1c17da` at `2026-05-29T13:38:12`, removed its own worktree, spawned successor `pm-portfolio-ratification-and-aeon-submission-260529-b4ac02`.
- Net validation: Round 1 §8.5 mid-sweep dirty re-check works at the sweep layer, AND the proper session-close ritual works at the per-session layer. The gap is between the two: sessions that don't *trigger* session-close (e.g., session crashes, harness disconnects, sessions never reaching their natural end) leave orphan worktrees that this sweep then has to clean up.

---

## §2. Per-worktree classification

### §2.1 PRESERVE (5 worktrees)

| Worktree | Reason |
|---|---|
| `/Users/c17n/commons-bonds` (main repo) | canonical; NYRB untracked file unchanged since May 27 (author elected leave-alone) |
| `commons-bonds-pm-portfolio-ratification-and-aeon-submission-260529-b4ac02` | active PM session (successor to 1b419b) |
| `commons-bonds-git-cleanup-sweep-2-260529-2f296e` | this session |
| `commons-bonds-ch2-harpers-essay-version-d-independent-audit-260528-09dc93` | possibly-live; per-worktree dirty re-check at remove time |
| `commons-bonds-ch2-harpers-essay-version-d-independent-audit-v2-260528-c3e6b8` | same — possibly live |

### §2.2 Defer (1 worktree)

- `commons-bonds-aeon-pitch-reading-flow-review-260528-040968` — 1 commit ahead ("Aeon pitch reading-flow review script v1.0.0 — PROPOSED 2026-05-28"; 48+ hours sitting unmerged). Add to §5.2 deferred set (now 6 branches).

### §2.3 REMOVE in Batch 1 — Orphan-locked agent worktrees (2)

| Worktree | Lock pid | Notes |
|---|---:|---|
| `.claude/worktrees/agent-a8073769a8718aed0` | 74779 (DEAD) | untracked rigor artifact ALREADY on origin/main (blob `6ee5254d`); safe to remove |
| `.claude/worktrees/agent-aaeb0d21013fe38be` | 73742 (DEAD) | clean; safe to remove |

### §2.4 REMOVE in Batch 2 — Merged-clean top-level worktrees (59)

All `ahead=0`, `dirty=0`, last commit ≥24h old. All leftovers from the 2026-05-28 portfolio-wide sprint.

**Grouped by unit:**

| Unit | Variant worktree count |
|---|---:|
| 100-barrel | 6 |
| atlantic-ideas | 6 + `atlantic-ideas-pitch-cover-260528-577e47` (Round 1 carry-over) = 7 |
| boston-review | 6 |
| ch2-harpers | 4 (V-D worktrees preserved per §2.1) |
| ch3-atlantic-main | 5 |
| ch4-foreign-affairs | 5 |
| noema | 6 |
| nyrb-multi-book | 5 |
| mcdowell-op-ed | 5 |
| norway-op-ed | 5 |
| Other (Round 1 carry-over + 2026-05-28 non-essay) | 5 (`aeon-essay-evolution-audit-260527-76f504`, `memory-no-invented-facts-260528-790f09`, `memory-process-review-260528-67ca7b`, `consent-tracker-creation-260528-879220`, `rigor-consolidation-bulk-migration-260528-4d4635`) |

**Total Batch 2: ~59 worktrees.**

Per-worktree dirty re-check immediately before each `git worktree remove` (Round 1 §9.3 discipline; vindicated this round by the 1b419b live-edit detection).

### §2.5 BULK-DELETE in Batch 3 — Stale local branches (~63)

Keep-list (13 branches): `main` + 4 active session branches (pm-portfolio-ratification, this session, 2× Ch 2 V-D audit) + 1 deferred 1-ahead (aeon-pitch-reading-flow) + 2 CONTAMINATED §5.1 (Ch 9 cluster) + 5 deferred-supersession §5.2 (unruffled-elbakyan, ch10-insertion-placement, ta-rcv, laughing-raman, christophers).

Delete everything else (76 − 13 = ~63 branches) via `git branch -D` loop.

---

## §3. Deferred items (carrying forward from Round 1)

### §3.1 CONTAMINATED branches §5.1 — UNCHANGED

- `claude/ch9-pass3-5-1fae85` (1 ahead; 2026-05-25)
- `claude/ch9-stage5-pm-handoff-1fae85` (0 ahead; renamed; 2026-05-25)

Round 1 §5.1 paste-text for per-branch detective triage remains authoritative.

### §3.2 STALE-UNMERGED supersession-verification §5.2 — NOW 6 BRANCHES

- `claude/unruffled-elbakyan-af5b16` (6 ahead; Ch 4 retrofit Pass 3.4 PROPOSED 2026-05-22)
- `claude/ch10-insertion-placement-lucid-pike-cbf748` (3 ahead; Ch 10 REVERT polish 2026-05-13)
- `claude/ta-rcv-publication-stability-signoff-663265` (1 ahead; TA RCV sign-off PROPOSED 2026-05-25)
- `claude/laughing-raman-8b4564` (1 ahead; Invariant-gate scope filter 2026-05-18)
- `claude/christophers-single-book-review-stage-0-663265` (1 ahead; Wave 2 Stage 0 single-book Christophers 2026-05-24; subsumed by NYRB multi-book on main)
- **NEW** `claude/aeon-pitch-reading-flow-review-260528-040968` (1 ahead; Aeon pitch reading-flow review script PROPOSED 2026-05-28; 48h+ unmerged)

---

## §4. Recommendations — REINFORCED from Round 1 §9

Round 1 issued 7 recommendations. Round 2 empirically validates the same failure mode at the same scale. Reissuing with reinforcement + 1 new:

### §4.1 SHOULD-ADOPT THIS WEEK (failure mode actively recurring)

1. **🔴 Session-close worktree cleanup hook.** Empirically validated twice now (Round 1 found 39 orphans; Round 2 found 60 in 24h). A hook running `git worktree remove "${WORKTREE_PATH}"` after successful `git push` would have prevented essentially all of Round 2's regrowth.

2. **🔴 Orphan-lock auto-recovery on SessionStart.** Both new agent worktrees (a8073769 + aaeb0d2) acquired orphan locks in last 14h. A SessionStart hook verifying lock-pid liveness and auto-removing (if pid dead AND last_commit ≥1h AND ahead=0) would clear these.

### §4.2 ALREADY EFFECTIVE (per-session, not harness)

3. **Mid-sweep dirty re-check discipline.** Round 1 §8.5 + Round 2 §1 both confirm. Should be HARD step in any future sweep script — no `git worktree remove` without an immediately-prior `git status --porcelain` check. This sweep follows the discipline; works correctly.

4. **Proper session-close ritual.** The 1b419b session demonstrated this works per-session (commit dashboard → push to main → remove worktree → spawn successor session with new slug). The pattern is correct; just isn't universal.

### §4.3 SHOULD-ADOPT WITHIN MONTH (latent)

5. **Branch-naming convention enforcement** (advisory) — no new violations in Round 2.
6. **Spawn-collision detection on SessionStart** — no Round 2 collisions but worth prophylactic implementation.
7. **Main-repo HEAD canary** — Round 1 fix held; continue monitoring.

### §4.4 SHOULD-ADOPT QUARTERLY (cadence)

8. **Hygiene sweep cadence.** Round 2 evidence: ~60 orphan worktrees per 24h during sprint-mode operations. Suggested cadence: **daily** during sprint mode + weekly otherwise. A `tools/scripts/branch-hygiene-sweep.sh` doing Phase A read-only + producing a short delta-report would minimize per-sweep author attention.

### §4.5 NEW recommendation (Round 2 surfacing)

9. **Comparison-batch archive collapse.** The 2026-05-28 portfolio-wide sprint produced ~55 worktrees with a structured pattern (`<unit>-<variant>-<harness>`). Once such a sprint completes (verdicts ratified per the PM dashboard), an "archive batch" script could collapse the 55 worktrees + 55 branches into a single closed-batch artifact: `tools/workstream-handoffs/comparison-batches/<sprint-name>-<date>.md` (1 line per worktree-branch with HEAD + summary), then bulk-prune. **Pattern-aware tooling, not just per-worktree cleanup.**

---

## §5. Phase B action summary — author authorization request

| Batch | Risk | Scope | Δ |
|---|---|---|---|
| 1 | LOW | 2 orphan-locked agent worktrees | 67 → 65 worktrees |
| 2 | LOW | ~59 merged-clean top-level worktrees (with per-worktree dirty re-check) | 65 → ~6 worktrees |
| 3 | LOW-MED | ~63 stale local branches (bulk delete) | 76 → ~13 branches |

**Skips / defers:** 2 Ch 2 V-D worktrees (live re-check), 1b419b (auto-closed), 6 §5.2-deferred branches, 2 §5.1-contaminated branches, 4 active sessions (main repo + this + pm-portfolio + Ch 2 V-D ×2).

**Author decisions requested:**

- ☐ Proceed with all 3 batches?
- ☐ Spawn separate task chip for §4.1 hook adoption (session-close cleanup hook + orphan-lock auto-recovery)?
- ☐ §4.5 comparison-batch archive script — defer to a separate session, or include in this sweep?
- ☐ Six §5.2 deferred branches — bulk-verify-and-delete now, or continue deferring?

---

## §6. STATE marker

```
STATE: Round 2 Phase A inventory + Phase B prune proposal PROPOSED
(76 branches + 67 worktrees inventoried 24h after Round 1 close;
identical failure mode produced 60-worktree regrowth driven by
2026-05-28 portfolio-wide parallel-comparison sprint; same 7
ahead-of-main branches as Round 1 close + 1 new 1-ahead defer; 1
mid-sweep in-flight preservation event detected AND resolved itself
via active PM session executing proper session-close ritual; 9
recommendations reissued with §4.1 reinforced + new §4.5
comparison-batch archive proposal); NEXT: author confirms Round 2
Phase B; AWAITING: author OK to proceed with Phase C.
```

---

*Round 2 inventory complete; awaiting author confirmation.*
