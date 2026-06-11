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
| Chapters (10) | Content-complete; **redraft-compare campaign live**. Promoted: Ch 1 + Ch 2 (06-05), Ch 5 (06-09, PROMOTE-NEW-AFTER-FOLDIN; Polanyi/Fraser/Sandel in, $108T out, 0 em-dashes). Awaiting compare+promote (all redraft drafts 0 em-dashes): Ch 3 (v1/v2 06-05; father/boardwalk FACT-CORRECTION application unverified), Ch 4/6/7/8 (v1 06-06), Ch 9 (v1 06-06, 4,862w — re-check vs 06-09 scope correction). Ch 10 no redraft (register model). **Fable bake-off Ch 1–3 in flight 06-10** (PM session; 2 variants + judge per chapter → `research/story-drafts/ch{1,2,3}-fable-*_2026-06-10.md`). Dashboard **v2** (06-10) corrects v1 stale rows; numeric sweep UNBLOCKED (TA closeout + framework-core both merged) — Ch 6 needs sweep + M2-reader coherence check BEFORE its compare+promote | 06-10 (PM v2, verified on disk) | Numeric sweep → compare+promote queue → Ch 1 + Ch 5 Wave-1 samples |
| Technical Appendix | v2.0.0 closeout **merged to main `fd12275` 06-09**; internally consistent, invariants HIGH=0; render glyphs verified tofu-free 06-10 | 06-10 (this session) | Stage-4 PDF render audit before external circulation |
| Back matter (bib/glossary/notation) | Generated clean set **MERGED to main 06-10** (author ratified); regenerate via `tools/back-matter/build.py gen-all` | 06-10 (this session) | In-TA Notation section + Part 7 completeness → technical-review window |
| Bibliography master | Single source of truth (TA §18 folded in, 06-09); 41 orphan candidates flagged for prune review | 06-10 (this session) | Optional prune pass |

## Active workstreams (sessions/worktrees)

| Workstream | Owner branch | State | Verified |
|---|---|---|---|
| Redraft-compare campaign | `claude/redraft-campaign-resume-260606-f8216d` | **SUPERSEDED-CLOSED 06-10** (author: chapters get whole-cloth redo). Working state archived to `manuscript/archive/redraft-campaign-2026-06/`; fact-ground ledgers relocated to `manuscript/ledgers/`; stray newer ch6-blind-brief rescued from its worktree (33–122× retirement preserved + integral lens updated to 61–115×); worktree prunable (branch never pushed) | 06-10 |
| Book-proposal sprint | `claude/book-proposal-sprint-260603-e402b7` | LIVE — owns `publishing/book-proposal/` | 06-09 |
| Back-matter + repo reorg | `claude/refactor-bib-consolidation-260609-23c283` | **CLOSED — ratified + MERGED to main 06-10** (navigation spine + archive sweep + back-matter set) | 06-10 |
| **Framework-core revision** | `claude/ta-reverse-csd-260610-4fc8d1` | **MERGED to main 06-10 (author ratification + push authorization).** Architecture "three ways count the identity" applied (§3.4 M2=realized-Bond reader + §3.6 logic/table recompute + §15.1.3) + correctness pass (Himmelstein cite, §17 case-census, Def 1.7/§5.1 posted-vs-owed typing, §3.3 per-unit M1, §9 softening + Model renames, theorem-heading markup, V_option residues, +12 more) + ratified §3.4 hedonic/VSL note (Rosen 1974 + Viscusi 1993 → TA §18 + master §25) + calc engine `core/technical-appendix/calculations/` (21/21 reproductions; reef + reparations-test + 11-case bidirectional portfolio PASS). `gen-all` re-run ✓ (bib 281; ISS parking refiled §23.2 out of reader bib). Symbol registry: SYNCED 2026-06-10 (ws2-registry-sync) — B̂_M2 row enriched (strict lower bound, NOT an estimator; hat = reading-of, author kept over alternatives), CSD_M3 (§5.5) + ∩ (§3.6) added; section sweep §3.3/3.4/3.6/5.5/15.1.3/17.7 found no other gaps; gen-all clean (41 symbols); ς render-covered. §5.5 reverse-method prose + §17.7 generativity RATIFIED+APPLIED 06-10; coercion authorial note DECLINED-CLOSED. Leftover handoffs: 3 of 4 CLOSED 06-10 — WS2 registry rows (merged 18a3503), Stage-4 markup sweep (ratified+merged dc83644), Libby/Baotou/RCV-integral provenance (RATIFIED+APPLIED 471f19a; see tools/audits/ta-provenance-libby-baotou-integral_2026-06-10_RATIFIED-APPLIED.md; residuals: §6.3 ~$1,025–1,065/ton level undocumented → next provenance item; §10 LaTeX-ish integral forms queued; book-proposal 05_chapter-summaries still carries 67–134× → ROUTED to the live proposal sprint). Remaining: §11.12 reef [GATE-2] only — ROUTED to the book-completion plan/dashboard session (author direction 06-10): wire the trigger 'Ch3 restitution section RATIFIED → launch reverse-csd-leftovers PASTE-TEXT 1'; the Ch3 whole-cloth redraft brief should include the restitution-section pricing (using the merged backward apparatus: CSD_M3 + realized-B₁ reading) as a named deliverable, making the redraft itself the GATE-2 key; close with a Ch3 ↔ §11.12 consistency check. Reverse-CSD method itself: COMPLETE in TA prose. | 06-10 (this merge) |
| PM session | `claude/pm-book-completion-260610-07b75f` | Standing meta-tracker (dashboard 06-10 **v2** = detail layer; Fable bake-off Ch 1–3 + prose-findings verification workflows in flight) | 06-10 |
| TA sessions (closeout cluster) | `ta-*` worktrees | **DONE — merged via closeout `fd12275`**; worktrees prunable | 06-09 |
| ~30 essay-review worktrees dated 06-01 | various | Presumed closed (branches behind main) — PM verify + prune | 06-10 (listed) |

---
*Created 2026-06-10 (repo-reorg session), seeded from the 2026-06-04 PM dashboard + per-file
verification noted per row. Rows marked "(PM)" inherit the dashboard's 06-04 verification.*
