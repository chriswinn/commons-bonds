# Git Cleanup Sweep — 2026-05-28

**Status:** Phase A + B PROPOSED 2026-05-28 → Phase C EXECUTED 2026-05-28 → Phase D RATIFIED 2026-05-28 (this artifact; auto-fast-forward to main per CLAUDE.md merge-to-main policy as internal scaffolding).
**Worktree:** `/Users/c17n/commons-bonds-git-cleanup-sweep-260528-451479` (branch `claude/git-cleanup-sweep-260528-451479` off `origin/main` `a5c7256`).
**Date:** 2026-05-28 morning.
**Scope:** comprehensive cleanup of 348 local branches + 66 worktrees accumulated during the parallel-session sprint of 2026-05-24 → 2026-05-27.

---

## §0. Headline numbers

| Object | Count | Notes |
|---|---|---|
| Local branches total | 348 | of which 320 are 0-commits-ahead of `origin/main` |
| Branches with commits ahead of main | **28** | per `git rev-list --count origin/main..<b>` |
| Worktrees total | 66 | per `git worktree list` |
| Top-level isolated session worktrees (`commons-bonds-<workstream>-<id>/`) | 25 | + 1 main repo = 26 |
| Locked `.claude/worktrees/agent-*` (harness-managed) | 32 | **ALL lock pids verified DEAD — every lock is orphan, safe to remove** |
| Unlocked legacy `.claude/worktrees/<non-agent>/` | 8 | older harness-managed worktrees pre-agent-naming |
| Prunable (auto-detected) worktrees | 0 | nothing has been deleted out-from-under git yet |

**Headline finding:** 320 of 348 branches (92%) are fully merged and prunable. ~58 of 66 worktrees (88%) are completed sessions that never closed their worktree. The cleanup mainly involves bulk-removal of the orphan-locked agent worktrees + a sweep of fully-merged feature branches.

---

## §1. Critical anomalies (flag for author before any prune action)

### §1.1 Main repo at `/Users/c17n/commons-bonds` is NOT on `main`

- Current state: HEAD = `b54822b` on branch `claude/atlantic-ideas-essay-pass-3-5-ratify-and-phase-c-61cef166-5c1` (0 ahead, 77 behind `origin/main`).
- Working tree has 1 dirty file: `tools/workstream-handoffs/nyrb-multi-book-review-essay-stage-2-drafting-kickoff_2026-05-27.md` (untracked).
- Per [`tools/memory/feedback_git_workflow.md`](../../memory/feedback_git_workflow.md) ("Chris's primary checkout … on `main`. Never touch"), the main repo working tree should sit on `main`. Some parallel session ran a checkout in the main cwd. The 0-ahead / 77-behind state means no work is at risk on the branch itself, but the dirty untracked file is sitting in the main cwd.
- **Recommendation:** the untracked file likely contains a kickoff paste-text drafted in a contaminated session. Either (a) move/commit it inside an isolated worktree, or (b) confirm it can be deleted. Then `git -C /Users/c17n/commons-bonds checkout main` to restore the main-repo HEAD. Do NOT do this destructive step without author OK.

### §1.2 Two worktrees claim `main`

- `/Users/c17n/commons-bonds` → branch `claude/atlantic-ideas-essay-pass-3-5-ratify-and-phase-c-61cef166-5c1` (see §1.1).
- `/Users/c17n/commons-bonds/.claude/worktrees/agent-aebd6c55548a18a45` → branch `main` (locked, pid 60987 **DEAD**). HEAD `697bcd2`, last commit 2026-05-25T22:51.
- Since the main repo is currently OFF `main` (it's on the Atlantic Ideas feature branch), this agent worktree IS the only worktree claiming `main` right now. Removing it via `git worktree remove --force` is safe (lock is orphan; content already on origin/main).
- **Recommendation:** include this in Batch 1 (orphan-locked agent worktree sweep). After Batch 1, `main` will have no worktree claimant, freeing `/Users/c17n/commons-bonds` to check back out to `main` per §1.1.

### §1.3 Contaminated worktree on `_scaffolding_push`

- `/Users/c17n/commons-bonds-ch2-harpers-pass3-2-voicepolish-260527-52a7ec` shows HEAD = `6366a17` on branch `_scaffolding_push` (a raw-named branch, NOT `claude/<workstream>-<id>` discipline). The worktree was created for the Ch 2 → Harper's Pass 3.2 voice-polish session but its HEAD has drifted to a different branch.
- The branch `claude/ch2-harpers-pass3-2-voicepolish-260527-52a7ec` still exists separately and is 9 commits ahead of main per Ch 2 → Harper's cascade history. But **all content from that cascade is now on `origin/main`** (verified — Pass 3.1, 3.2, 3.5 spot-fixes + Stage 5 sign-off + Pass 3.5 final-state header all present in main HEAD history `098abb9`, `1fed119`, `5fc1ad5`, `1ec19a0`, `dc737bb`, `6366a17`).
- **Recommendation:** worktree is removable. Both `_scaffolding_push` and `claude/ch2-harpers-pass3-2-voicepolish-260527-52a7ec` branches are removable once content-on-main is reconfirmed (one more verification step in Phase C).
- **Discipline note:** this is exactly the contamination class described in [`feedback_worktree_isolation_for_parallel_sessions.md`](../../memory/feedback_worktree_isolation_for_parallel_sessions.md) §"Triage discipline." The triage discipline says "cherry-pick wrong-branch commits onto their correct destination branches; leave the now-clean branch as the canonical record." In this case the content is already on main, so the contaminated branch can simply be deleted rather than triaged — no cherry-pick needed.

### §1.4 Two PM sessions on the cascade-v2-amend-morning workstream

- `/Users/c17n/commons-bonds-pm-cascade-v2-amend-morning-260527-1b419b` (last 2026-05-27T14:06; 0 ahead / 12 behind)
- `/Users/c17n/commons-bonds-pm-cascade-v2-amend-morning-260527-48a55d` (last 2026-05-27T12:42; 0 ahead / 21 behind)
- These look like a duplicate spawn collision — two PM sessions opened against the same workstream-slug on 2026-05-27. Both have merged all their content to main (0 ahead). Both are safe to remove.
- **Recommendation:** include both in Batch 2 (top-level isolated worktree sweep).

### §1.5 Polyworkstream-contaminated `claude/ch9-stage5-pm-handoff-1fae85` (known)

- Per [`feedback_worktree_isolation_for_parallel_sessions.md`](../../memory/feedback_worktree_isolation_for_parallel_sessions.md) §"Empirical anchors" — this branch is the 2026-05-26 contamination empirical anchor (Ch 9 + Stage 5 + PM handoff + Wave 2 Stage 0 file modifications entangled). Branch is NOT in any worktree right now (orphan branch).
- Companion branch `claude/ch9-pass3-5-1fae85` (1 commit ahead of main; 2026-05-25) is also part of the Ch 9 entanglement cluster.
- **Recommendation:** SKIP from Phase C destructive batch. Leave per-branch triage paste-text in §5 for a dedicated detective session.

### §1.6 Raw-named branches (violating `claude/<workstream>-<id>` discipline)

- `_essay_input_readonly`, `_pass3_1_input_readonly`, `_pass3_2_input_readonly`, `_scaffolding_push`, `_scaffolding_push_pass_3_3`, `_stage2_input_readonly`, `_stage5_ready_input` — seven raw-named branches all related to the Ch 2 → Harper's pipeline-orchestration worktree at `.claude/worktrees/ch2-harpers-pipeline-orchestration/`.
- These appear to be intentionally-created "snapshot input" branches the orchestrator session used as read-only inputs into per-pass cascades. Discipline-wise they should have been named `claude/ch2-harpers-pipeline-orchestration-<state>-<id>` but the convention wasn't applied. Substantively their content is now on main (Ch 2 → Harper's complete).
- **Recommendation:** confirm content-on-main, then prune in Batch 3 (stale branch sweep).

---

## §2. Per-worktree classification

### §2.1 Top-level isolated session worktrees (25 + main repo)

| Worktree (last segment) | Branch | Ahead | Behind | Last commit | Class | Disposition |
|---|---:|---:|---:|---|---|---|
| `commons-bonds` (main repo) | `claude/atlantic-ideas-essay-pass-3-5-ratify-and-phase-c-61cef166-5c1` | 0 | 77 | 2026-05-27T01:01 | **MAIN-REPO-OFF-MAIN** | §1.1 — author OK to checkout `main` after Batch 1 frees the main ref |
| `aeon-essay-evolution-audit-260527-76f504` | `claude/aeon-essay-evolution-audit-260527-76f504` | 0 | 1 | 2026-05-28T00:55 | **ACTIVE-IN-FLIGHT** (today's session) | LEAVE ALONE |
| `aeon-essay-file-org-fix-260527-191aef` | `claude/aeon-essay-file-org-fix-260527-191aef` | 0 | 22 | 2026-05-27T12:34 | MERGED-CLEAN | prune (Batch 2) |
| `aeon-pitch-reading-flow-review-260528-040968` | `claude/aeon-pitch-reading-flow-review-260528-040968` | **1** | 2 | 2026-05-28T01:13 | **ACTIVE-IN-FLIGHT** (today's session, work pending) | LEAVE ALONE |
| `atlantic-ideas-pitch-cover-260528-577e47` | `claude/atlantic-ideas-pitch-cover-260528-577e47` | 0 | 1 | 2026-05-28T00:55 (dirty=1) | **ACTIVE-IN-FLIGHT** (today's session, dirty WT) | LEAVE ALONE |
| `atlantic-ideas-stage5-signoff-260527-dcb316` | `claude/atlantic-ideas-stage5-signoff-260527-dcb316` | 0 | 70 | 2026-05-27T02:25 | MERGED-CLEAN | prune (Batch 2) |
| `ch2-harpers-pass3-2-voicepolish-260527-52a7ec` | `_scaffolding_push` | 0 | 3 | 2026-05-27T23:50 | **CONTAMINATED** (HEAD drifted; content on main) | §1.3 — prune in Batch 2 after content-on-main reconfirm |
| `ch2-harpers-pass3-3-audienceload-260527-9f6b6d` | `claude/ch2-harpers-pass3-3-audienceload-260527-9f6b6d` | **6** | 32 | 2026-05-27T11:37 | STALE-UNMERGED (Ch 2 cascade superseded; content on main) | prune (Batch 3 — verify supersession first) |
| `ch2-harpers-pass3-4-adversarial-260527-54318b` | `claude/ch2-harpers-pass3-4-adversarial-260527-54318b` | **6** | 28 | 2026-05-27T12:41 | STALE-UNMERGED (Ch 2 cascade) | prune (Batch 3) |
| `ch2-harpers-pass3-5-devedit-260527-19a634` | `claude/ch2-harpers-pass3-5-devedit-260527-19a634` | **6** | 20 | 2026-05-27T13:15 | STALE-UNMERGED (Ch 2 cascade) | prune (Batch 3) |
| `ch2-harpers-stage5-signoff-260527-7784a6` | `claude/ch2-harpers-stage5-signoff-260527-7784a6` | 0 | 5 | 2026-05-27T22:10 | MERGED-CLEAN | prune (Batch 2) |
| `ch3-atlantic-main-stage2-draft-260527-9fddf1` | `claude/ch3-atlantic-main-stage2-draft-260527-9fddf1` | **3** | 80 | 2026-05-27T03:05 | STALE-UNMERGED (Ch 3 cascade complete on main) | prune (Batch 3) |
| `ch3-atlantic-main-stage3-pass-3-1-fact-check-260527-3ab8c6` | `claude/ch3-atlantic-main-stage3-pass-3-1-fact-check-260527-3ab8c6` | 0 | 54 | 2026-05-27T09:32 | MERGED-CLEAN | prune (Batch 2) |
| `ch3-atlantic-pass32-260527-a92210` | `claude/ch3-atlantic-pass32-260527-a92210` | **5** | 54 | 2026-05-27T10:44 | STALE-UNMERGED (Ch 3 cascade) | prune (Batch 3) |
| `ch3-atlantic-pass33-260527-b68b63` | `claude/ch3-atlantic-pass33-260527-b68b63` | **2** | 36 | 2026-05-27T11:09 | STALE-UNMERGED (Ch 3 cascade) | prune (Batch 3) |
| `ch3-atlantic-pass34-260527-e8ca32` | `claude/ch3-atlantic-pass34-260527-e8ca32` | **2** | 34 | 2026-05-27T11:18 | STALE-UNMERGED (Ch 3 cascade) | prune (Batch 3) |
| `ch3-atlantic-pass35-260527-5f34a1` | `claude/ch3-atlantic-pass35-260527-5f34a1` | **3** | 32 | 2026-05-27T11:32 | STALE-UNMERGED (Ch 3 cascade) | prune (Batch 3) |
| `ch3-atlantic-stage5-260527-4c11e8` | `claude/ch3-atlantic-stage5-260527-4c11e8` | **4** | 30 | 2026-05-27T12:30 | STALE-UNMERGED (Ch 3 cascade) | prune (Batch 3) |
| `ch4-fa-pass3-1-factcheck-260527-c7af4e` | `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e` | **16** | 80 | 2026-05-27T10:23 | STALE-UNMERGED (FA merge LANDED on main `3ae1777`; branch superseded) | prune (Batch 3) — content verified on main per §1.0 |
| `cross-essay-portfolio-review-260527-910102` | `claude/cross-essay-portfolio-review-260527-910102` | 0 | 2 | 2026-05-28T00:53 | MERGED-CLEAN (session just closed) | prune (Batch 2) |
| `git-cleanup-sweep-260528-451479` | (this session) | 0 | 0 | 2026-05-28T01:14 | **THIS SESSION** | LEAVE ALONE |
| `memory-no-invented-facts-260528-790f09` | `claude/memory-no-invented-facts-260528-790f09` | 0 | 0 | 2026-05-28T01:14 | **ACTIVE-IN-FLIGHT** (today's parallel session, content already on main `a5c7256`) | LEAVE ALONE |
| `nyrb-multibook-stage2-260527-fd4cc6` | `claude/nyrb-multibook-stage2-260527-fd4cc6` | 0 | 40 | 2026-05-27T10:21 | MERGED-CLEAN | prune (Batch 2) |
| `pm-cascade-v2` | `claude/pm-session-cascade-v2-ratification-pm0525` | 0 | 81 | 2026-05-27T00:29 | MERGED-CLEAN | prune (Batch 2) |
| `pm-cascade-v2-amend-morning-260527-1b419b` | `claude/pm-cascade-v2-amend-morning-260527-1b419b` | 0 | 12 | 2026-05-27T14:06 | MERGED-CLEAN (§1.4 duplicate spawn collision) | prune (Batch 2) |
| `pm-cascade-v2-amend-morning-260527-48a55d` | `claude/pm-cascade-v2-amend-morning-260527-48a55d` | 0 | 21 | 2026-05-27T12:42 | MERGED-CLEAN (§1.4 duplicate spawn collision) | prune (Batch 2) |

### §2.2 Locked agent worktrees (32; ALL orphan locks)

Every locked agent worktree's lock pid is verified DEAD (no live process holds the lock). Per [`feedback_worktree_isolation_for_parallel_sessions.md`](../../memory/feedback_worktree_isolation_for_parallel_sessions.md) §"Session close" — these accumulated because session-end cleanup never ran. All are safe to unlock + remove. Removal command per worktree:

```bash
git worktree unlock <path>
git worktree remove --force <path>
```

| Worktree (basename) | Branch | Lock pid (dead) | Last commit | Class | Disposition |
|---|---|---:|---|---|---|
| `agent-a0eee61a8c1bea965` | `claude/ch8-stage5-signoff-pre-pub-queue-a0eee61a` | 9763 | 2026-05-27T01:02 | LOCKED-AGENT | unlock+remove (Batch 1) |
| `agent-a12ed7f85945ace53` | `worktree-agent-a12ed7f85945ace53` | 20043 | 2026-05-27T10:10 | LOCKED-AGENT | unlock+remove |
| `agent-a185e66fbbb404582` | `worktree-agent-a185e66fbbb404582` | 76235 | 2026-05-21T05:01 | LOCKED-AGENT | unlock+remove |
| `agent-a26d044bd1e7bfa28` | `worktree-agent-a26d044bd1e7bfa28` | 78442 | 2026-05-25T00:59 | LOCKED-AGENT | unlock+remove |
| `agent-a26f72eb97c2685fd` | `worktree-agent-a26f72eb97c2685fd` | 20043 | 2026-05-27T03:12 | LOCKED-AGENT | unlock+remove |
| `agent-a2922041f779c9c18` | `claude/manuscript-stage-3-ch7-pass2-phase-c-beta-a2922041f779c9c18` | 15244 | 2026-05-24T00:52 | LOCKED-AGENT | unlock+remove |
| `agent-a3390c00c9b9a4df0` | `worktree-agent-a3390c00c9b9a4df0` | 9569 | 2026-05-27T02:14 | LOCKED-AGENT | unlock+remove |
| `agent-a3a17ae703034fe7f` | `worktree-agent-a3a17ae703034fe7f` | 1405 | 2026-05-26T00:25 | LOCKED-AGENT | unlock+remove |
| `agent-a3a6c0dc4dc40a560` | `worktree-agent-a3a6c0dc4dc40a560` | 72160 | 2026-05-25T02:21 | LOCKED-AGENT | unlock+remove |
| `agent-a3f019d3ab9f25fff` | `claude/ch7-stage-3-4-5-closure-agent-a3f019d3ab9f25fff` | 60987 | 2026-05-26T01:08 | LOCKED-AGENT | unlock+remove |
| `agent-a545a471ff8fd1f6d` | `worktree-agent-a545a471ff8fd1f6d` | 61542 | 2026-05-25T21:07 | LOCKED-AGENT | unlock+remove |
| `agent-a58caac617cdfa278` | `worktree-agent-a58caac617cdfa278` | 1405 | 2026-05-26T01:00 | LOCKED-AGENT | unlock+remove |
| `agent-a780222e83724b34b` | `worktree-agent-a780222e83724b34b` | 60987 | 2026-05-26T01:13 | LOCKED-AGENT | unlock+remove |
| `agent-a7d30e478b051a782` | `worktree-agent-a7d30e478b051a782` | 20459 | 2026-05-24T11:11 | LOCKED-AGENT | unlock+remove |
| `agent-a87b9bdf41d1db808` | `claude/ch7-stage-4-5-closure-bundled-a87b9bdf41d1db808` | 88158 | 2026-05-26T23:38 | LOCKED-AGENT | unlock+remove |
| `agent-a92185d216c1bddd6` | `worktree-agent-a92185d216c1bddd6` | (no lock entry) | 2026-05-26T01:27 | LOCKED-AGENT (no lock marker but in `.claude/worktrees/`) | remove |
| `agent-a9384a5cf3f717c89` | `worktree-agent-a9384a5cf3f717c89` | 1405 | 2026-05-26T01:24 | LOCKED-AGENT | unlock+remove |
| `agent-a94da6ab6ce772b3d` | `claude/cross-corpus-ipg-canonical-construction-agent-a94da6ab6ce772b3d` | 51928 | 2026-05-21T01:10 | LOCKED-AGENT | unlock+remove |
| `agent-a961c6bdc8e46e1ba` | `worktree-agent-a961c6bdc8e46e1ba` | 87850 | 2026-05-26T22:33 | LOCKED-AGENT | unlock+remove |
| `agent-a9d9acb68b6144fe7` | `claude/ch8-pass3-4-audience-load-robustness-a9d9ac` | 83765 | 2026-05-26T01:13 | LOCKED-AGENT | unlock+remove |
| `agent-aa04af5d72e6e721f` | `claude/ch8-pass3-3-audience-load-acceptance-aa04af5d` | 83765 | 2026-05-26T00:24 | LOCKED-AGENT | unlock+remove |
| `agent-ab6aebab9c2e9ff85` | `worktree-agent-ab6aebab9c2e9ff85` | 81250 | 2026-05-25T21:12 | LOCKED-AGENT | unlock+remove |
| `agent-ac2fcad9ec570374b` | `worktree-agent-ac2fcad9ec570374b` | 72885 | 2026-05-14T00:22 | LOCKED-AGENT (oldest; 2-week-old) | unlock+remove |
| `agent-ac63459270ae49fc9` | `worktree-agent-ac63459270ae49fc9` | 1405 | 2026-05-25T23:53 | LOCKED-AGENT | unlock+remove |
| `agent-ac8b21b53febd4db9` | `claude/manuscript-stage-3-ch7-pass3-4-agent-ac8b21b53febd4db9` | 60987 | 2026-05-26T00:40 | LOCKED-AGENT | unlock+remove |
| `agent-ad1947d16476c939c` | `claude/ch8-pass2-voice-polish-ad1947d16476c939c` | 34120 | 2026-05-24T01:09 | LOCKED-AGENT | unlock+remove |
| `agent-adebb5b68af058397` | `claude/ch8-pass3-5-developmental-edit-851515` | 88392 | 2026-05-26T23:49 | LOCKED-AGENT | unlock+remove |
| `agent-ae4c69351f44ee166` | `worktree-agent-ae4c69351f44ee166` | 20459 | 2026-05-24T22:23 | LOCKED-AGENT | unlock+remove |
| `agent-ae92b994d743756fc` | `worktree-agent-ae92b994d743756fc` | 72160 | 2026-05-25T01:51 | LOCKED-AGENT | unlock+remove |
| **`agent-aebd6c55548a18a45`** | **`main`** | 60987 | 2026-05-25T22:51 | LOCKED-AGENT (§1.2 — second `main` claimant) | unlock+remove (frees `main` for the main repo) |
| `agent-af2f3d6b623a3210d` | `worktree-agent-af2f3d6b623a3210d` | 61542 | 2026-05-25T17:29 | LOCKED-AGENT | unlock+remove |
| `agent-af456e3721fd66e34` | `worktree-agent-af456e3721fd66e34` | 53264 | 2026-05-21T18:28 | LOCKED-AGENT | unlock+remove |
| `agent-afe3d6f29d7dc6eb9` | `worktree-agent-afe3d6f29d7dc6eb9` | 81250 | 2026-05-25T21:12 | LOCKED-AGENT | unlock+remove |

### §2.3 Legacy unlocked `.claude/worktrees/<non-agent>/` (8)

| Worktree (basename) | Branch | Last commit | Class | Disposition |
|---|---|---|---|---|
| `ch2-harpers-pipeline-orchestration` | `worktree-ch2-harpers-pipeline-orchestration` | 2026-05-27T00:25 | LEGACY (orchestrator session) | remove (Batch 1; content of Ch 2 → Harper's on main) |
| `ch3-pass3.1-phase-c` | `claude/ch3-stage3-pass3.1-fact-check-2026-05-25` | 2026-05-25T22:47 | LEGACY (Ch 3 cascade) | remove (Batch 1) |
| `ch3-pass3.5-isolated` | `claude/ch3-stage3-pass3.5-de-recover-2026-05-25` | 2026-05-26T00:54 | LEGACY (Ch 3 cascade) | remove (Batch 1) |
| `ch4-fa-ratify-663265` | `claude/wave-2-ch4-fa-ratify-663265` | 2026-05-26T23:51 | LEGACY (FA ratify; content now on main) | remove (Batch 1) |
| `ch6-pass-3-3-light-refire-1fae85-isolated` | `worktree-ch6-pass-3-3-light-refire-1fae85-isolated` | 2026-05-25T21:00 | LEGACY (post-1fae85 isolation rescue) | remove (Batch 1) |
| `foreign-affairs-essay-stage-2-draft` | `worktree-foreign-affairs-essay-stage-2-draft` | 2026-05-27T00:05 | LEGACY (FA Stage 2 draft; content on main) | remove (Batch 1) |
| `heuristic-kapitsa-bf57a5` | `claude/ta-phase-c-3-4-5-bf57a5` | 2026-05-14T00:32 | LEGACY (oldest unlocked; 2-week-old TA work) | remove (Batch 1) |

(7 listed; the 8th was double-counted earlier — actual count is 7.)

---

## §3. Per-branch classification (28 branches with commits ahead of main)

These are the 28 branches that aren't strictly fast-forward-mergeable. After Phase C Batch 2 worktree removal, branches still referenced by removed worktrees become deletable.

| Branch | Ahead | Worktree? | Last commit | Class | Disposition |
|---|---:|---|---|---|---|
| `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e` | 16 | yes | 2026-05-27T10:23 | STALE-UNMERGED (FA content on main via `3ae1777`) | delete after worktree removed (Batch 3) |
| `_essay_input_readonly` | 9 | no | 2026-05-27T13:40 | RAW-NAMED (§1.6; Ch 2 → Harper's orchestrator input) | delete (Batch 3) |
| `claude/ch2-harpers-pass3-2-voicepolish-260527-52a7ec` | 9 | no (worktree on `_scaffolding_push`) | 2026-05-27T13:40 | CONTAMINATED + STALE-UNMERGED (§1.3) | delete (Batch 3) |
| `_pass3_2_input_readonly` | 8 | no | 2026-05-27T11:17 | RAW-NAMED | delete (Batch 3) |
| `claude/unruffled-elbakyan-af5b16` | 6 | no | 2026-05-22T23:45 | STALE-UNMERGED (Ch 4 pipeline-retrofit Pass 3.4 PROPOSED) | **DEFER** — verify supersession before delete |
| `claude/ch2-harpers-pass3-5-devedit-260527-19a634` | 6 | yes | 2026-05-27T13:15 | STALE-UNMERGED (Ch 2 cascade on main) | delete after worktree removed (Batch 3) |
| `claude/ch2-harpers-pass3-4-adversarial-260527-54318b` | 6 | yes | 2026-05-27T12:41 | STALE-UNMERGED (Ch 2 cascade on main) | delete (Batch 3) |
| `claude/ch2-harpers-pass3-3-audienceload-260527-9f6b6d` | 6 | yes | 2026-05-27T11:37 | STALE-UNMERGED (Ch 2 cascade on main) | delete (Batch 3) |
| `worktree-agent-a12ed7f85945ace53` | 5 | yes (locked) | 2026-05-27T10:10 | LOCKED-AGENT | delete after worktree removed |
| `claude/ch3-atlantic-pass32-260527-a92210` | 5 | yes | 2026-05-27T10:44 | STALE-UNMERGED (Ch 3 cascade on main) | delete (Batch 3) |
| `_pass3_1_input_readonly` | 5 | no | 2026-05-27T10:10 | RAW-NAMED | delete (Batch 3) |
| `worktree-agent-a3390c00c9b9a4df0` | 4 | yes (locked) | 2026-05-27T02:14 | LOCKED-AGENT | delete after worktree removed |
| `worktree-agent-a26f72eb97c2685fd` | 4 | yes (locked) | 2026-05-27T03:12 | LOCKED-AGENT | delete after worktree removed |
| `claude/ch3-atlantic-stage5-260527-4c11e8` | 4 | yes | 2026-05-27T12:30 | STALE-UNMERGED (Ch 3 cascade on main) | delete (Batch 3) |
| `_stage2_input_readonly` | 4 | no | 2026-05-27T02:14 | RAW-NAMED | delete (Batch 3) |
| `claude/ch3-atlantic-pass35-260527-5f34a1` | 3 | yes | 2026-05-27T11:32 | STALE-UNMERGED (Ch 3 cascade on main) | delete (Batch 3) |
| `claude/ch3-atlantic-main-stage2-draft-260527-9fddf1` | 3 | yes | 2026-05-27T03:05 | STALE-UNMERGED (Ch 3 cascade on main) | delete (Batch 3) |
| `claude/ch10-insertion-placement-lucid-pike-cbf748` | 3 | no | 2026-05-13T23:12 | STALE-UNMERGED (Ch 10 revert work; 2-week-old) | **DEFER** — verify supersession before delete |
| `claude/ch8-pass2-voice-polish-ad1947d16476c939c` | 2 | yes (locked) | 2026-05-24T01:09 | LOCKED-AGENT (Ch 8 cascade) | delete after worktree removed |
| `claude/ch3-atlantic-pass34-260527-e8ca32` | 2 | yes | 2026-05-27T11:18 | STALE-UNMERGED (Ch 3 cascade on main) | delete (Batch 3) |
| `claude/ch3-atlantic-pass33-260527-b68b63` | 2 | yes | 2026-05-27T11:09 | STALE-UNMERGED (Ch 3 cascade on main) | delete (Batch 3) |
| `claude/ta-rcv-publication-stability-signoff-663265` | 1 | no | 2026-05-25T01:41 | STALE-UNMERGED ("TA RCV publication-stability sign-off — PROPOSED") | **DEFER** — verify if superseded by `claude/ta-phase-c-3-4-5-bf57a5` cascade |
| `claude/laughing-raman-8b4564` | 1 | no | 2026-05-18T23:59 | STALE-UNMERGED ("Invariant-gate scope filter — match renamed chapter files") | **DEFER** — verify if folded into invariant-gate scripts on main |
| `claude/christophers-single-book-review-stage-0-663265` | 1 | no | 2026-05-24T21:50 | STALE-UNMERGED (Wave 2 Stage 0 single-book review; superseded by NYRB multi-book essay) | **DEFER** — verify supersession |
| `claude/ch9-pass3-5-1fae85` | 1 | no | 2026-05-25T22:07 | **CONTAMINATED** (Ch 9 + Stage 5 + PM handoff entanglement per memory anchor) | **SKIP** — per-branch detective triage (§5) |
| `claude/atlantic-ideas-essay-pass-3-1-phase-c-application-a9e5554f-302` | 1 | no | 2026-05-25T00:24 | STALE-UNMERGED (Atlantic Ideas Pass 3.1 superseded by Pass 3.5 on main) | delete (Batch 3) — supersession confirmed by portfolio review §2.2 |
| `claude/aeon-pitch-reading-flow-review-260528-040968` | 1 | yes (today's active session) | 2026-05-28T01:13 | ACTIVE-IN-FLIGHT | LEAVE ALONE |

**Stale-branch summary (28 ahead branches):**
- 17 STALE-UNMERGED safe to delete after worktree removal (Ch 2 + Ch 3 + FA cascades on main + Atlantic Ideas Pass 3.1)
- 4 RAW-NAMED (Ch 2 → Harper's orchestrator inputs; content on main)
- 4 LOCKED-AGENT (handled via worktree removal Batch 1)
- 4 **DEFER** (need supersession verification): `unruffled-elbakyan-af5b16`, `ch10-insertion-placement-lucid-pike-cbf748`, `ta-rcv-publication-stability-signoff-663265`, `laughing-raman-8b4564`, `christophers-single-book-review-stage-0-663265` (actually 5 — note count drift)
- 1 CONTAMINATED (`claude/ch9-pass3-5-1fae85` — skip; per-branch detective triage)
- 1 ACTIVE-IN-FLIGHT (`aeon-pitch-reading-flow-review-260528-040968` — leave)
- 1 known polyworkstream-contaminated `claude/ch9-stage5-pm-handoff-1fae85` — not in this list because it's 0 ahead (renamed; commit-history-only). Skip from any prune.

### §3.2 The 320 fully-merged feature branches

The remaining `claude/*` branches (excluding the 28 above) are all 0 commits ahead of `origin/main`. They are merged content from completed work and safe to delete in bulk. Sample of patterns (full list available via `git branch | grep '^  claude/' | sed 's/^[* ] *//'`):

- `claude/100-barrel-essay-*` — Phenomenal World cascade (multiple harness IDs, all on main)
- `claude/aeon-*` — Aeon pitch + post-acceptance cascade (multiple)
- `claude/atlantic-ideas-essay-pass-3-{1,2,3,4,5}-*` — Atlantic Ideas full pipeline (Pass 3.5 RATIFIED + APPLIED on main per portfolio review §1.3 + §0.1)
- `claude/boston-review-essay-*` — BR cascade (8+ branches)
- `claude/ch{1..10}-*-<harness>` — per-chapter retrofit + rigor-pass cascades (~150 branches)
- `claude/cross-{chapter,corpus}-*` — cross-chapter workstreams
- Adjective+name harness IDs (`admiring-aryabhata-a8f6aa`, `flamboyant-clarke-359516`, etc.) — older naming convention from before `claude/<workstream>-<id>` discipline (predominant in 2026-05-08 → 2026-05-15 timeframe)

---

## §4. Batched prune proposal

### Batch 1 — Orphan-locked agent worktree sweep (LOWEST RISK)

Removes 32 locked `.claude/worktrees/agent-*` worktrees + 7 legacy unlocked `.claude/worktrees/<non-agent>/` worktrees = 39 worktrees total. ALL lock pids verified dead; no live session holds these.

Implementation:
```bash
# Per worktree: unlock then force-remove (force needed because of locked metadata)
for wt in /Users/c17n/commons-bonds/.claude/worktrees/agent-*; do
  git -C /Users/c17n/commons-bonds worktree unlock "$wt" 2>/dev/null || true
  git -C /Users/c17n/commons-bonds worktree remove --force "$wt"
done

# Legacy unlocked worktrees
for wt in ch2-harpers-pipeline-orchestration ch3-pass3.1-phase-c ch3-pass3.5-isolated ch4-fa-ratify-663265 ch6-pass-3-3-light-refire-1fae85-isolated foreign-affairs-essay-stage-2-draft heuristic-kapitsa-bf57a5; do
  git -C /Users/c17n/commons-bonds worktree remove --force "/Users/c17n/commons-bonds/.claude/worktrees/$wt"
done

git -C /Users/c17n/commons-bonds worktree prune
```

Expected delta: 66 → 27 worktrees. Also frees the `main` branch ref so the main repo can checkout `main` (§1.1 + §1.2).

### Batch 2 — Top-level isolated worktree sweep (MERGED-CLEAN only; LOW RISK)

Removes 8 top-level `commons-bonds-<workstream>-<id>` worktrees that are 0-ahead and dirty=0:

- `commons-bonds-aeon-essay-file-org-fix-260527-191aef`
- `commons-bonds-atlantic-ideas-stage5-signoff-260527-dcb316`
- `commons-bonds-ch2-harpers-pass3-2-voicepolish-260527-52a7ec` (CONTAMINATED on `_scaffolding_push`; content on main; safe to remove)
- `commons-bonds-ch2-harpers-stage5-signoff-260527-7784a6`
- `commons-bonds-ch3-atlantic-main-stage3-pass-3-1-fact-check-260527-3ab8c6`
- `commons-bonds-cross-essay-portfolio-review-260527-910102` (just-closed session)
- `commons-bonds-nyrb-multibook-stage2-260527-fd4cc6`
- `commons-bonds-pm-cascade-v2`
- `commons-bonds-pm-cascade-v2-amend-morning-260527-1b419b`
- `commons-bonds-pm-cascade-v2-amend-morning-260527-48a55d`

(10 worktrees — corrected count.)

Implementation:
```bash
for wt in commons-bonds-aeon-essay-file-org-fix-260527-191aef commons-bonds-atlantic-ideas-stage5-signoff-260527-dcb316 commons-bonds-ch2-harpers-pass3-2-voicepolish-260527-52a7ec commons-bonds-ch2-harpers-stage5-signoff-260527-7784a6 commons-bonds-ch3-atlantic-main-stage3-pass-3-1-fact-check-260527-3ab8c6 commons-bonds-cross-essay-portfolio-review-260527-910102 commons-bonds-nyrb-multibook-stage2-260527-fd4cc6 commons-bonds-pm-cascade-v2 commons-bonds-pm-cascade-v2-amend-morning-260527-1b419b commons-bonds-pm-cascade-v2-amend-morning-260527-48a55d; do
  git -C /Users/c17n/commons-bonds worktree remove "/Users/c17n/$wt"
done
```

Expected delta: 27 → 17 worktrees.

### Batch 3 — Stale-merged + stale-unmerged branch deletion (LOW-MED RISK)

After Batches 1 + 2, the following branches are no longer referenced by any worktree and can be deleted with `git branch -D`:

**Local-only delete (320 fully-merged + ~17 stale-unmerged-but-superseded):**

```bash
# Fully merged branches (320)
git -C /Users/c17n/commons-bonds for-each-ref --format='%(refname:short)' refs/heads/ | while read b; do
  ahead=$(git -C /Users/c17n/commons-bonds rev-list --count origin/main..$b 2>/dev/null)
  if [ "$ahead" = "0" ] && [ "$b" != "main" ]; then
    # Skip branches still in worktree
    in_wt=$(git -C /Users/c17n/commons-bonds worktree list --porcelain | grep -c "refs/heads/$b")
    if [ "$in_wt" = "0" ]; then
      git -C /Users/c17n/commons-bonds branch -D "$b"
    fi
  fi
done

# Specific stale-unmerged-but-superseded branches (17)
git -C /Users/c17n/commons-bonds branch -D \
  claude/ch4-fa-pass3-1-factcheck-260527-c7af4e \
  claude/ch2-harpers-pass3-2-voicepolish-260527-52a7ec \
  claude/ch2-harpers-pass3-3-audienceload-260527-9f6b6d \
  claude/ch2-harpers-pass3-4-adversarial-260527-54318b \
  claude/ch2-harpers-pass3-5-devedit-260527-19a634 \
  claude/ch3-atlantic-main-stage2-draft-260527-9fddf1 \
  claude/ch3-atlantic-pass32-260527-a92210 \
  claude/ch3-atlantic-pass33-260527-b68b63 \
  claude/ch3-atlantic-pass34-260527-e8ca32 \
  claude/ch3-atlantic-pass35-260527-5f34a1 \
  claude/ch3-atlantic-stage5-260527-4c11e8 \
  claude/atlantic-ideas-essay-pass-3-1-phase-c-application-a9e5554f-302 \
  _essay_input_readonly \
  _pass3_1_input_readonly \
  _pass3_2_input_readonly \
  _scaffolding_push \
  _scaffolding_push_pass_3_3 \
  _stage2_input_readonly \
  _stage5_ready_input

# Worktree-stub branches (worktree-agent-*; left over from harness worktree creation)
git -C /Users/c17n/commons-bonds branch -D $(git branch | grep '^  worktree-' | sed 's/^[* ] *//')
```

Expected delta: 348 → ~12 branches (main + ~5 deferred + ~6 active session branches).

**Skip from delete:** `claude/ch9-pass3-5-1fae85`, `claude/ch9-stage5-pm-handoff-1fae85` (CONTAMINATED — per-branch detective triage per §5).

**Defer to author judgment:** `claude/unruffled-elbakyan-af5b16` (Ch 4 retrofit Pass 3.4 PROPOSED — verify supersession by main-line FA cascade), `claude/ch10-insertion-placement-lucid-pike-cbf748` (Ch 10 revert work; 2-week-old), `claude/ta-rcv-publication-stability-signoff-663265` (TA RCV PROPOSED — verify supersession by TA Phase C cascade), `claude/laughing-raman-8b4564` (invariant-gate filter — verify if landed on main), `claude/christophers-single-book-review-stage-0-663265` (Wave 2 Stage 0 single-book; superseded by NYRB multi-book essay per portfolio review §3 + §5).

**Remote-delete:** NOT proposed in this pass. Origin/branches mirror local branches for tracked ones, but the sweep is local-only here. A separate `git push origin --delete <branch>` sweep can run after author confirms the local sweep is correct.

---

## §5. Deferred items (CONTAMINATED branches; per-branch detective triage paste-text)

### §5.1 `claude/ch9-pass3-5-1fae85` + `claude/ch9-stage5-pm-handoff-1fae85` triage

Per [`feedback_worktree_isolation_for_parallel_sessions.md`](../../memory/feedback_worktree_isolation_for_parallel_sessions.md) §"Empirical anchors" — this is the canonical contamination empirical anchor. Three workstreams entangled on one branch: Ch 9 Pass 3.5, Stage 5 sign-off, PM handoff + Wave 2 Stage 0 file modifications.

**Paste-text for detective session:**

```
You are a fresh CC session (worktree-isolated) doing per-branch detective
triage on two contaminated branches:

  1. claude/ch9-pass3-5-1fae85 (1 commit ahead of origin/main, 2026-05-25T22:07)
  2. claude/ch9-stage5-pm-handoff-1fae85 (0 commits ahead but RENAMED from
     claude/ch9-pass3-5-1fae85 — three workstream names entangled)

Triage steps:

  1. git log claude/ch9-pass3-5-1fae85 --stat -20
     git log claude/ch9-stage5-pm-handoff-1fae85 --stat -20
     Identify each commit's true workstream by inspecting the files touched.

  2. For commits that belong on a different workstream's branch, cherry-pick
     them onto that destination branch. (If destination branch is gone, skip.)

  3. For commits that belong on the Ch 9 workstream, verify they ARE on main
     (most likely already merged via parallel-session cascade).

  4. Once all commits are accounted for, delete both branches:
       git branch -D claude/ch9-pass3-5-1fae85
       git branch -D claude/ch9-stage5-pm-handoff-1fae85

Reference: tools/memory/feedback_worktree_isolation_for_parallel_sessions.md
§"Triage discipline for already-contaminated branches".
```

### §5.2 Suspected supersession — author verify

Four branches likely safe to delete but warrant a quick "is it on main?" verification:

- `claude/unruffled-elbakyan-af5b16` — Ch 4 pipeline-retrofit Pass 3.4 robustness PROPOSED 2026-05-22. The FA essay (= Ch 4 deriv) is now Stage 5 RATIFIED on main per portfolio review §1.7. Verify the Pass 3.4 PROPOSED artifact's content is reflected in the on-main Pass 3.4 RATIFIED artifact.
- `claude/ch10-insertion-placement-lucid-pike-cbf748` — Ch 10 revert polish (2026-05-13). Verify Ch 10 on main has the right state.
- `claude/ta-rcv-publication-stability-signoff-663265` — TA RCV sign-off PROPOSED 2026-05-25. Verify TA Phase C cascade on main supersedes.
- `claude/laughing-raman-8b4564` — Invariant-gate scope filter (2026-05-18). Verify `tools/quality-gates/` invariant scripts on main include the filter logic.
- `claude/christophers-single-book-review-stage-0-663265` — Wave 2 Stage 0 single-book Christophers review (2026-05-24). The NYRB multi-book review-essay (Pistor + Mazzucato + Christophers + Susskind) on main subsumes this. Likely safe to delete.

---

## §6. Branch-hygiene cadence recommendations going forward

Empirical pattern from this sweep:

1. **Session-end discipline gap.** Most worktrees got orphan-locked because session-close cleanup (`git worktree remove` per [`feedback_git_workflow.md`](../../memory/feedback_git_workflow.md) "Session close" + [`feedback_worktree_isolation_for_parallel_sessions.md`](../../memory/feedback_worktree_isolation_for_parallel_sessions.md) "Session close") never ran. **Recommendation:** add a session-close hook that runs `git worktree remove "${WORKTREE_PATH}"` after successful push, OR have the SessionStart hook do an opportunistic prune of orphan-locked worktrees from prior sessions when starting a new one (e.g., "if lock pid is dead, auto-unlock + remove").

2. **Spawn-collision detection.** The duplicate `pm-cascade-v2-amend-morning-260527-*` worktrees (§1.4) suggest two parallel sessions spawned against the same workstream slug within a short window. **Recommendation:** the SessionStart hook could check for existing worktrees matching the proposed workstream slug + warn before creating a duplicate.

3. **Branch-naming-discipline enforcement.** The raw `_essay_input_readonly` + `_scaffolding_push` + `worktree-agent-*` + `worktree-<descriptive>-*` branches all violate the canonical `claude/<workstream>-<id>` convention. **Recommendation:** add a pre-receive or pre-push hook (or just a discipline note) flagging branches that don't match the convention. The orchestrator pattern (Ch 2 → Harper's pipeline-orchestration creating snapshot input branches) is legitimate but should adopt the convention (`claude/ch2-harpers-orchestrator-essay-input-<id>` etc.).

4. **Main-repo HEAD discipline.** The main cwd has drifted to a feature branch (§1.1). **Recommendation:** the SessionStart hook (or a tighter variant) could check if `/Users/c17n/commons-bonds`'s HEAD is on `main`; if not, warn loudly (this is the canary for contamination from a session that ran `git checkout` in the main cwd).

5. **Quarterly branch sweep.** This is the first comprehensive sweep since project inception. **Recommendation:** quarterly cadence — author runs `tools/scripts/branch-hygiene-sweep.sh` (new) that lists branches by class and proposes a batched prune. Runtime: ~5 minutes for the read-only analysis.

---

## §7. Phase B action summary

**Author confirmation required before Phase C execution:**

| Batch | Risk | Scope | Object delta |
|---|---|---|---|
| 1 | LOW | Orphan-locked agent worktree sweep (32 locked + 7 unlocked legacy) | 66 → 27 worktrees; frees `main` ref |
| 2 | LOW | Top-level merged-clean session worktrees (10 worktrees) | 27 → 17 worktrees |
| 3 | LOW-MED | Stale local branch deletion (~340 branches; bulk + named) | 348 → ~12 branches |

**Skip / defer:**
- 2 CONTAMINATED Ch 9 branches → §5.1 per-branch detective session
- 5 STALE-UNMERGED branches → §5.2 author verification
- 4 ACTIVE-IN-FLIGHT worktrees → leave alone (this session + 3 other 260528 sessions)
- Main repo HEAD restore (§1.1) → author OK to checkout `main` after Batch 1 frees the ref

**Author decision:**
- ☐ OK to proceed with Batch 1 + Batch 2 + Batch 3?
- ☐ OK to restore main-repo HEAD to `main` after Batch 1?
- ☐ OK to remove the untracked `tools/workstream-handoffs/nyrb-multi-book-review-essay-stage-2-drafting-kickoff_2026-05-27.md` from main cwd (or want it preserved)?
- ☐ OK to defer the 5 STALE-UNMERGED branches at §5.2 to per-branch verification later (vs. delete them in Phase C)?

---

---

## §8. Phase C execution log (2026-05-28)

Author confirmed all four §7 decisions:
- ☑ All 3 batches
- ☑ Restore main repo HEAD to `main` after Batch 1
- ☑ Leave untracked NYRB kickoff paste-text alone in main cwd
- ☑ Defer the 5 §5.2 STALE-UNMERGED branches to per-branch verification later

### §8.1 Batch 1 — Orphan-locked + legacy unlocked worktree sweep

- 32 `.claude/worktrees/agent-*` worktrees: `git worktree unlock` + `git worktree remove --force`. 1 of 32 had no lock entry (`agent-a92185d216c1bddd6`) — unlock returned `fatal: not locked` (harmless) but remove succeeded.
- 7 `.claude/worktrees/<non-agent>/` worktrees: `git worktree remove --force`. All clean.
- Main repo HEAD restored: `git -C /Users/c17n/commons-bonds checkout main`; local `main` was 153 commits behind `origin/main`, fast-forwarded.

**Delta:** 66 → 26 worktrees.

### §8.2 Batch 2 — Merged-clean top-level isolated worktree sweep

- 10 worktrees proposed for removal.
- 9 removed cleanly.
- 1 (`commons-bonds-pm-cascade-v2-amend-morning-260527-1b419b`) RETAINED: mid-sweep dirty-state recheck revealed 2 → 3 uncommitted modifications by an active parallel PM session drafting a major workflow-discipline change ("merge-on-ratification" rule) — see §8.5.

**Delta:** 26 → 17 worktrees.

### §8.3 Batch 3a — STALE-UNMERGED top-level worktree sweep (content-on-main verified)

- 10 worktrees proposed (Ch 2 + Ch 3 + FA cascade artifacts; content all on `origin/main`).
- All 10 removed cleanly after per-worktree dirty-check (all dirty=0).

**Delta:** 17 → 7 worktrees.

### §8.4 Batch 3b — Bulk local-branch deletion

- Keep-list (14 branches): `main` + 5 active 260528 session branches + 1 active 260527 PM session (1b419b; §8.5) + 1 this-session branch + 2 CONTAMINATED (skip) + 5 deferred (§5.2).
- 334 branches queued for deletion; 334 successfully deleted via `git branch -D <name>` loop; 0 failed.

**Delta:** 348 → 14 branches.

### §8.5 In-flight work preservation event (worth a memory entry)

The `commons-bonds-pm-cascade-v2-amend-morning-260527-1b419b` worktree was initially classified MERGED-CLEAN in Phase A (`dirty=0`, `ahead=0`, last commit 2026-05-27T14:06). Between Phase A scan and Batch 2 execution, the worktree acquired 3 uncommitted modifications:

- Modified: `CLAUDE.md` (+~50 lines: new "merge-on-ratification" rule + escape hatches + revised rationale)
- Untracked: `tools/memory/feedback_merge_on_ratification.md` (97-line new memory entry)
- (one additional change appeared by the third re-check)

This was a parallel PM session actively drafting a substantive change to the project's branch-discipline doctrine — the kind of work that, if blown away by `--force` worktree removal, would have been catastrophic. The cleanup sweep correctly paused, investigated, and preserved.

The drafted memory entry explicitly references THIS git-cleanup-sweep session ("The git-cleanup-sweep session spawned 2026-05-28 covers this in its Phase A inventory + Phase C execution"). Two sessions, drafted concurrently, reference each other — symptomatic of the parallel-session sprint reality the new policy is trying to formalize.

**Disposition:** worktree + branch RETAINED. Author needs to finish ratifying the PM session's draft + commit it. Future cleanup sweeps should adopt the per-worktree dirty re-check at each batch as a hard discipline.

### §8.6 Phase D — final state

| Metric | Phase A | Phase D | Δ |
|---|---:|---:|---:|
| Total branches | 348 | 14 | **−334 (−96%)** |
| Total worktrees | 66 | 7 | **−59 (−89%)** |
| Locked agent worktrees | 32 | 0 | −32 (eliminated) |
| Legacy unlocked `.claude/worktrees/` | 8 | 0 | −8 (eliminated) |
| Branches ahead of main | 28 | 7 | −21 |
| Worktrees claiming `main` | 2 (drift) | 1 (canonical) | −1 |

**Surviving worktrees (7):**

1. `/Users/c17n/commons-bonds` (main repo, on `main` at `6c19ad8`)
2. `commons-bonds-aeon-essay-evolution-audit-260527-76f504` (active 260528)
3. `commons-bonds-aeon-pitch-reading-flow-review-260528-040968` (active 260528, 1 ahead)
4. `commons-bonds-atlantic-ideas-pitch-cover-260528-577e47` (just merged 260528)
5. `commons-bonds-git-cleanup-sweep-260528-451479` (this session)
6. `commons-bonds-memory-no-invented-facts-260528-790f09` (active 260528)
7. `commons-bonds-pm-cascade-v2-amend-morning-260527-1b419b` (active PM; §8.5 — drafting merge-on-ratification policy)

**Surviving branches (14):**

- `main` (canonical)
- 5 active 260528 session branches (aeon-essay-evolution-audit, aeon-pitch-reading-flow-review, atlantic-ideas-pitch-cover, memory-no-invented-facts, plus this session `git-cleanup-sweep`)
- 1 active 260527 PM session branch (`pm-cascade-v2-amend-morning-260527-1b419b` — §8.5)
- 2 CONTAMINATED (`ch9-pass3-5-1fae85`, `ch9-stage5-pm-handoff-1fae85` — §5.1 detective triage)
- 5 deferred-supersession-verification (`unruffled-elbakyan-af5b16`, `ch10-insertion-placement-lucid-pike-cbf748`, `ta-rcv-publication-stability-signoff-663265`, `laughing-raman-8b4564`, `christophers-single-book-review-stage-0-663265` — §5.2)

`git fsck --no-dangling` clean; no repo-corruption side-effects from the sweep.

---

## §9. Recommendations for future PM sessions

These should be considered for adoption (not all are this session's call):

1. **Session-close worktree cleanup hook.** Add a hook at session close that, after a successful `git push`, runs `cd /Users/c17n/commons-bonds && git worktree remove "${WORKTREE_PATH}"`. Eliminates the orphan-worktree accumulation pattern that produced 39 of the 59 removed worktrees in this sweep.

2. **Orphan-lock auto-recovery on SessionStart.** The SessionStart hook could scan `.claude/worktrees/agent-*/locked` lock files; if the lock pid is dead AND last commit is >24h old, auto-unlock + remove. (Conservative: only auto-prune worktrees with `ahead=0`; flag others for author confirmation.)

3. **Mid-sweep dirty re-check discipline.** This session's Phase A had `dirty=0` for the 1b419b worktree, but a parallel session was actively drafting work there. Adding per-worktree `git status --porcelain` re-check immediately before each `git worktree remove` call would catch all such in-flight work. Codified as a hard step in any future cleanup sweep.

4. **Branch-naming convention enforcement.** Pre-push hook (or session-start hook) that warns if a branch name doesn't match `^claude/[a-z0-9-]+$` or one of an allowed set of harness-managed prefixes. Eliminates the `_essay_input_readonly` / `_scaffolding_push` / `worktree-<descriptive>-*` raw-named branches that accumulated in this sweep.

5. **Spawn-collision detection on SessionStart.** Hook checks for existing worktrees matching the proposed workstream slug; warns before creating a duplicate. Catches the `pm-cascade-v2-amend-morning-260527-{1b419b,48a55d}` duplicate-spawn pattern.

6. **Main-repo HEAD canary.** Hook checks if `/Users/c17n/commons-bonds`'s HEAD is on `main`; if not, warns loudly. This sweep found the main repo had drifted to `claude/atlantic-ideas-essay-pass-3-5-ratify-and-phase-c-61cef166-5c1` — a contamination canary.

7. **Quarterly hygiene cadence.** This was the first comprehensive sweep. Suggest scheduling one at end of each major sprint (e.g., after each Wave 2 batch closes). Runtime: ~5 min read-only analysis + ~5 min destructive batch.

---

## §10. STATE marker

```
STATE: Git cleanup sweep RATIFIED + EXECUTED 2026-05-28 (Phase A
inventory + Phase B prune proposal + Phase C execution all complete;
348 → 14 branches; 66 → 7 worktrees; in-flight PM session work
preserved at §8.5 via mid-sweep dirty re-check); NEXT: §5.1
per-branch detective triage for Ch 9 contamination cluster (separate
session); §5.2 supersession verification for 5 STALE-UNMERGED
deferred branches (low priority, ad-hoc); §9 hook + discipline
recommendations to next PM session; AWAITING: nothing (autonomous
internal-scaffolding merge to main per CLAUDE.md merge-to-main).
```

---

*Cleanup sweep complete 2026-05-28.*
