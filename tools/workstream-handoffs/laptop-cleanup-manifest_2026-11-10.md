# Laptop cleanup manifest — 2026-11-10

Local session on the Mac at `/Users/c17n/commons-bonds` (confirmed `pwd` +
`uname=Darwin`). Goal: every piece of uncommitted work saved to GitHub, main
checkout back on `main`, stale worktree folders removed. **Nothing was lost.**

Safety rules honored throughout: no `--force`, no `git reset --hard`, no
`git clean`, no `git worktree remove --force`, no `git branch -D`, no
`--no-verify`. Nothing deleted until its content was committed to a rescue
branch, pushed, and confirmed with `git ls-remote`.

## 1. Rescue branches pushed to origin (all `ls-remote`-confirmed)

| Rescue branch | Source folder | Tip | What was saved |
|---|---|---|---|
| `claude/rescue-main-checkout-20261110` | main checkout (`commons-bonds`) | `17b5a3ed` | 2 modified READMEs + 13 new: proposal redrafts, `_pipeline` notes, stage-1 brief, `research/citations/`, `research/permissions/`, ch2 brief, portfolio-triangulation memo + handoffs |
| `claude/rescue-br-V-E-20261110` | br-V-E | `c70e6b01` | Boston Review accountability-gap rigor passes + parallel drafts (9 files) |
| `claude/rescue-ch5-rebuild-20261110` | ch5-rebuild | `a7db1ea5` | Chapter 5 edits + regressed-patterns.yaml + 3 floor drafts (9k/12k/16k) |
| `claude/rescue-mcdowell-recs-20261110` | mcdowell-recs | `762af030` | 7 McDowell op-ed audit/archive files |
| `claude/rescue-noema-draft-20261110` | noema-draft | `1aaa31e9` | `noema-commons-bonds/redraft_2026-06/` (5 files) |
| `claude/rescue-noema-vd-cascade-20261110` | noema-vd-cascade | `e73b585c` | Noema hybrid best-of-both draft edit |
| `claude/rescue-public-books-cover-letter-20261110` | public-books-cover-letter | `6fb5600c` | Public Books accountability-gap stage-1 brief |
| `claude/rescue-redraft-campaign-resume-20261110` | redraft-campaign-resume | `c30b71e1` | ch6 blind brief edit |
| `claude/rescue-ta-bibconsol-20261110` | ta-bibconsol | `fb256fe6` | `tools/back-matter/citation-crossref-index.md` (`__pycache__` junk skipped) |
| `claude/rescue-ta-reverse-csd-20261110` | ta-reverse-csd | `59afba3c` | reverse-CSD fresh-session paste text |
| `claude/rescue-ta-stage4-markup-20261110` | ta-stage4-markup | `80ce7ee6` | `.rendercheck/` before/after PNG + HTML |
| `claude/rescue-tolerance-spot-fix-20261110` | tolerance-spot-fix | `be373a7b` | The branch's **unpushed** commit ("AuthorsNote + 00_overview item-G invented-tolerance spot-fix") + ancestry — rescued without touching the in-progress rebase |
| `claude/rescue-agent-worktrees-20261110` | 7 `.claude/worktrees/agent-*` | `053a90dd` | 8 differing/new files consolidated (see §4 for per-file source) |

The two clean sibling worktrees (aeon-pitch, ch1-ch3-redline-prep) had no
uncommitted work; their feature-branch tips were already on origin, so they
needed no rescue.

## 2. Worktrees removed (11 — clean + fully on origin, no `--force`)

Each verified clean and with its branch tip `ls-remote`-confirmed on origin
immediately before `git worktree remove`; `git worktree prune` run after.

| Removed folder | Branch it was on | Tip (on origin) |
|---|---|---|
| commons-bonds-aeon-pitch-reading-flow-review-260528-040968 | `claude/aeon-pitch-reading-flow-review-260528-040968` | `0a00cbcf` |
| commons-bonds-br-V-E-ratify-and-apply-260601-b550a6 | `claude/rescue-br-V-E-20261110` | `c70e6b01` |
| commons-bonds-ch1-ch3-redline-prep-260619-2e62ec | `claude/ch1-ch3-redline-prep-260619-2e62ec` | `dc8821c7` |
| commons-bonds-ch5-rebuild-260625-563db9 | `claude/rescue-ch5-rebuild-20261110` | `a7db1ea5` |
| commons-bonds-mcdowell-recs-review-vs-audience-weighting-260601-27aa9e | `claude/rescue-mcdowell-recs-20261110` | `762af030` |
| commons-bonds-noema-draft-260619-424976 | `claude/rescue-noema-draft-20261110` | `1aaa31e9` |
| commons-bonds-noema-vd-cascade-ratified-260601-23c017 | `claude/rescue-noema-vd-cascade-20261110` | `e73b585c` |
| commons-bonds-public-books-cover-letter-accountability-gap-260604-ea56a9 | `claude/rescue-public-books-cover-letter-20261110` | `6fb5600c` |
| commons-bonds-redraft-campaign-resume-260606-f8216d | `claude/rescue-redraft-campaign-resume-20261110` | `c30b71e1` |
| commons-bonds-ta-reverse-csd-260607-1efd85 | `claude/rescue-ta-reverse-csd-20261110` | `59afba3c` |
| commons-bonds-ta-stage4-markup-260610-70c0bf | `claude/rescue-ta-stage4-markup-20261110` | `80ce7ee6` |

The local branches these worktrees were on (both rescue branches and the two
original feature branches) still exist locally and on origin; none were
deleted.

## 3. Removed in follow-up (author-approved, 2026-11-10) — all 17 dirty worktrees + 1 empty orphan

After the initial 11-worktree batch, the author approved removing all remaining
dirty folders. Each was removed WITHOUT `--force` and WITHOUT `git clean`: every
dirty file was re-verified safe on origin (identical to `origin/main`, or captured
in `claude/rescue-agent-worktrees-20261110`, or `__pycache__` junk), then the
confirmed-safe files were cleared (`git restore` for tracked mods; literal-path
`rm` for untracked; tolerance via `git rebase --abort`) and the worktree dropped
with plain `git worktree remove` (no `--force`).

| Folder | How removed | Content status |
|---|---|---|
| `.claude/worktrees/agent-*` (15 worktrees) | cleared confirmed-safe files, then `git worktree remove` | 12 untracked files already identical to origin/main; 8 rescued (`053a90dd`) |
| commons-bonds-ta-bibconsol-21deaf | removed `__pycache__/.pyc` junk, then `git worktree remove` | Real file rescued (`fb256fe6`) |
| commons-bonds-tolerance-spot-fix-260611-2c3b1b | `git rebase --abort` (→ `be373a7b`, clean), then `git worktree remove` | Unpushed commit rescued (`be373a7b`) |
| `.claude/worktrees/exciting-heyrovsky-327780` | `rmdir` (empty skeleton, 0 files) | Nothing to save — empty leftover dirs from May 26 |

Local branch refs for these worktrees were NOT deleted (branch pruning deferred —
see §7). Final worktree state: only the main checkout at
`/Users/c17n/commons-bonds` remains.

## 4. Agent-worktree rescue detail (§1 branch `claude/rescue-agent-worktrees-20261110`)

Triage: 20 dirty files across the 15 agent worktrees → 12 already identical to
`origin/main` (no rescue needed), 8 differing/absent → rescued:

| Source worktree | File |
|---|---|
| agent-a13ec2c7d877a8372 | `publishing/essays/foreign-affairs-existence-proof/rigor/pass-3-1-verification_VERSION-D-backports_2026-06-01.md` |
| agent-a17470f3fb5b18067 | `publishing/essays/atlantic-main-chesapeake-watermen/rigor/stage-5-signoff_V-D-LIGHT-RE-SIGNOFF_2026-06-01.md` |
| agent-a22cf927843184c2a | `publishing/essays/foreign-affairs-existence-proof/rigor/pass-3-1-verification_NBIM-AR-2023_external-lookup_2026-06-01.md` |
| agent-a3a3658e8a38ab87e | `publishing/essays/atlantic-main-chesapeake-watermen/rigor/cover-letter-AMENDMENT-D-RE-AUDIT_2026-06-01.md` |
| agent-a4095b5996da840ab | `publishing/essays/atlantic-main-chesapeake-watermen/rigor/pass-3-2-voice-polish_V-D-LIGHT-RE-FIRE_2026-06-01.md` |
| agent-a6351d157c19ff740 | `publishing/essays/_pipeline/cross-essay-norway-consistency_2026-06-01.md` (new; 287 lines) |
| agent-a6b89efbc5ab386ee | `publishing/essays/foreign-affairs-existence-proof/rigor/audit-3-tournament_V-D-vs-V-E-alpha-vs-V-E-beta_2026-06-01.md` |
| agent-a86872d955ba19036 | `publishing/essays/noema-commons-bonds/rigor/cover-letter-pass-3-3-3-4-3-5-audit_AMENDMENT-D-WEIGHTED_2026-06-01.md` |

## 5. Skipped as junk (not rescued)

- `commons-bonds-ta-bibconsol-21deaf/tools/back-matter/__pycache__/build.cpython-314.pyc` — Python bytecode cache.

(No `.DS_Store` or `node_modules` were present. `.rendercheck/` PNG+HTML was
treated as real work and rescued, not skipped, since it is not in the junk
allowlist.)

## 6. Main checkout

Returned to `main` and fast-forwarded (683 commits) earlier in the session;
clean. Note: `origin/main` advanced during the session (observed
`b1c73a9a → 0714871b → 7658ead2`) from outside this session.

## 7. Not done — waiting on the author

- **Dirty-but-safe folders + tolerance-spot-fix:** DONE — all removed in the
  author-approved follow-up (see §3). Final worktree state: only the main
  checkout at `/Users/c17n/commons-bonds` remains.
- **Local branch pruning:** 60+ stale `claude/*` branches remain (including the
  13 `claude/rescue-*-20261110` snapshots). `git branch -d` would safely delete
  those fully on origin and refuse any with unpushed commits (several exist,
  e.g. `book-proposal-tier1` +87, `atlantic-ideas-package-ratification` +39).
  Not run — treat as its own reviewed batch.

---
Rescue branches are preservation snapshots, not merge requests. Decide per
branch later whether each is worth merging or can be deleted once its content
is confirmed captured elsewhere.
