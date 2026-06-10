# STATE.md — live project status (single source for "where does X stand?")

**Discipline.** Any session that *changes* a status below updates that one line (with the date)
in the same commit. The PM session reconciles this file against per-unit READMEs + the newest
PM dashboard on each PM pass. Detail layer: newest `tools/workstream-handoffs/pm-session-handoff_<date>.md`
(currently **2026-06-10** — includes the book-completion plan + per-chapter table + author decision queue).
This file supersedes the snapshot table in `publishing/essays/README.md` as the live surface.
Status vocabulary: `tools/conventions/status-markers.md`. Orientation: [MAP.md](MAP.md).

**Wave-1 critical path (target: late June 2026):** book-proposal finalization → Ch 1 + Ch 5
polish (redraft campaign) → agent-query Wave 1 fires ~Jun 24 – Jul 1 (cascade plan v2 Amendment 6).

---

## Portfolio — essays

| Unit | Venue | State | Verified | Next action |
|---|---|---|---|---|
| $100 Barrel | Phenomenal World | **SUBMITTED** ~2026-06-03 | 06-04 (PM) | Await decision (4–8 wk) |
| Accountability Gap | ~~Boston Review~~ → Public Books | REJECTED 2026-06-03 → **cascading to Public Books**; cover letter in flight | 06-04 (PM) | Ratify PB cover letter → submit |
| Existence Proof | Foreign Affairs | **RATIFIED READY-TO-SUBMIT**; cover letter DRAFTED 05-27 | 06-04 (PM) | **Ratify cover letter → submit (critical path)** |
| Commons Bonds | Noema | RATIFIED-AWAITING-SUBMIT (05-24) — **AMBIGUOUS, PM verify:** V-D-prime cascade PROPOSED 06-01/02 not visibly closed | 06-04 (PM) | Author decides: submit ratified version vs close cascade |
| Mask of Abundance | Aeon | V-E canonical; **portal-watch** (maintenance page seen 06-03); Jul 1–5 fallback | 06-04 (PM) | Submit on portal open |
| Pricing Honestly | Atlantic Ideas | RATIFIED-AWAITING-SUBMIT (Amendment-D weighting 06-01) | 06-04 (PM) | Submit on author cadence |
| What the Bay Knows | The Atlantic (features) | RATIFIED-AWAITING-SUBMIT; V-D hybrid canonical 06-01 | 06-04 (PM) | Submit on author cadence |
| Architecture and Its Residue | NYRB | RATIFIED-AWAITING-SUBMIT; cover-letter chips in flight | 06-04 (PM) | Oct 8–Nov 15 window |
| What McDowell County Paid | Harper's | V-D hybrid canonical 06-01; author-substrate items pending | 06-04 (PM) | Q4 2026 window |
| Berggruen Prize 2026 | Berggruen | Placeholder; offline AI-free drafting | 06-04 (PM) | Deadline 2026-08-17 |

## Portfolio — op-eds + proposal + agents

| Unit | State | Verified | Next action |
|---|---|---|---|
| Norway op-ed (FT/Bloomberg/PS) | V-D′ canonical 06-01; news-peg pending | 06-04 (PM) | Opportunistic peg activation |
| McDowell op-ed (venue TBD) | V-D hybrid canonical 06-01; news-peg pending | 06-04 (PM) | Opportunistic peg activation |
| **Book proposal** | 00_overview **RATIFIED 06-09** (Stage 5); §00 + §05 recascaded to TA closeout figures 06-10; TA-indexed figures flagged for refresh before assembly (~Jun 14–20, pre-agent gate per dashboard §5) | 06-10 (PM + commits) | Sprint completes ~Jun 20; strip status header before send |
| Agent pipeline (Wave 1) | Scaffolded, **0 queries sent**; targets list at `publishing/agents/_pipeline/targets.md` | 06-04 (PM) | Fires ~Jun 24 – Jul 1 after proposal + Ch 1/5 |

## Book

| Unit | State | Verified | Next action |
|---|---|---|---|
| Chapters (10) | Content-complete; **redraft-compare campaign live**; per-chapter table in the 06-10 PM dashboard §3 — **Ch 5 + Ch 9 whole-cloth redrafts firing now** (briefs pre-written); Ch 8 spot-fix-vs-redraft = author decision #5; whole-book **prose-smoothing campaign PROPOSED** (dashboard §4, decision #7) | 06-10 (PM) | Author decision queue (dashboard §2) → Ch 1 + Ch 5 polish for Wave-1 samples |
| Technical Appendix | v2.0.0 closeout **merged to main `fd12275` 06-09**; internally consistent, invariants HIGH=0; render glyphs verified tofu-free 06-10 | 06-10 (this session) | Stage-4 PDF render audit before external circulation |
| Back matter (bib/glossary/notation) | Generated clean set **MERGED to main 06-10** (author ratified); regenerate via `tools/back-matter/build.py gen-all` | 06-10 (this session) | In-TA Notation section + Part 7 completeness → technical-review window |
| Bibliography master | Single source of truth (TA §18 folded in, 06-09); 41 orphan candidates flagged for prune review | 06-10 (this session) | Optional prune pass |

## Active workstreams (sessions/worktrees)

| Workstream | Owner branch | State | Verified |
|---|---|---|---|
| Redraft-compare campaign | `claude/redraft-campaign-resume-260606-f8216d` | LIVE — owns `manuscript/` `_`-files + chapters + bibliography.md | 06-09 |
| Book-proposal sprint | `claude/book-proposal-sprint-260603-e402b7` | LIVE — owns `publishing/book-proposal/` | 06-09 |
| Back-matter + repo reorg | `claude/refactor-bib-consolidation-260609-23c283` | **CLOSED — ratified + MERGED to main 06-10** (navigation spine + archive sweep + back-matter set) | 06-10 |
| PM session | `pm-portfolio-ratification-and-aeon-submission-260529-b4ac02` | Standing meta-tracker | 06-04 |
| TA sessions (closeout cluster) | `ta-*` worktrees | **DONE — merged via closeout `fd12275`**; worktrees prunable | 06-09 |
| ~30 essay-review worktrees dated 06-01 | various | Presumed closed (branches behind main) — PM verify + prune | 06-10 (listed) |

---
*Created 2026-06-10 (repo-reorg session), seeded from the 2026-06-04 PM dashboard + per-file
verification noted per row. Rows marked "(PM)" inherit the dashboard's 06-04 verification.*
