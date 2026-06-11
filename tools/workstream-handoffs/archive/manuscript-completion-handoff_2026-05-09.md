# Manuscript Completion — Workstream Handoff (2026-05-09)

**Date drafted:** 2026-05-09
**Date modified:** 2026-05-10 (stale-header fix: Ch 3 drafted 2026-05-09 via commit `3a8b096`; "9 of 10 chapters" + "excluding Ch 3" framing removed)
**Branch to create at session start:** `claude/manuscript-completion-<harness-id>` (branch from current `origin/main`)
**Status going in:** All 10 chapters drafted (Ch 3 landed 2026-05-09 via commit `3a8b096`); Ch 5 + Ch 9 Pistor/Christophers/Susskind engagement landed (commit `d78872e`); Tech Appendix + Glossary rebuilds queued.

---

## Workstream scope

Manuscript-side work (Ch 3 drafting now complete):
- Bibliography engagement-pending → engaged flag updates (cross-thread item #3)
- Tech Appendix Phase 3 v2.0.0 rebuild
- Glossary v4 rebuild
- GuidanceDoc per-section staleness audits (Insight #37 follow-up)
- Insight #39 pre-publication external review (post-completion)

## Current state — chapters

| Ch | Title | State |
|---|---|---|
| 1 | The Quiet Math | **Drafted 2026-05-04** (~3,400w; tentatively final; sunrise bookend with Ch 10) |
| 2 | The Miner | Drafted (~4,957w); 3 INTERVIEW NEEDED placeholders flagged per weekly-audit-2026-04-28 |
| 3 | The Waterman | Drafted 2026-05-09 (commit `3a8b096`); unblocked 2026-05-08 via Colden + Moore public-record briefs |
| 4 | The Existence Proof | Drafted (~3,975w) |
| 5 | The Accountability Gap | Drafted (~9,574w); Pistor + Christophers paragraph engagement landed (commit `d78872e`) |
| 6 | Three Ways of Counting | Drafted (HTML, semantic; ~75KB); Insight #21 closed 2026-05-04 |
| 7 | On Other Worlds | Drafted (~8,537w); Aeon source material |
| 8 | What Things Actually Cost | Drafted (~6,026w); Dunbar/Du Bois/Ellison/Fanon engagement applied 2026-05-08 |
| 9 | Pricing Honestly | Drafted (~10,178w); Christophers + Susskind paragraph engagement landed (commit `d78872e`) |
| 10 | Common Bonds | Drafted (~7,366w); sunset close (sunrise bookend with Ch 1) |

## Current state — non-chapter manuscript work

- **Bibliography (`research/literature/bibliography.md`)**: comprehensive (~18,312w; 156 sections); §13 has Mazzucato (load-bearing) + Pistor / Christophers / Susskind (added 2026-05-08; "engagement pending" flags pending update to "engaged in Ch X §Y" per cross-thread item #3)
- **Tech Appendix Phase 3 v2.0.0 rebuild**: queued (~20–30 hrs estimated)
- **Glossary v4 rebuild**: queued (post-Phase-3-Tech-Appendix)
- **Insight #21**: closed 2026-05-04 (Ch 6 supplementary placement folded into Phase 3 rebuild)
- **Insight #39 pre-publication external review**: pending post-completion

## Next moves (priority order)

1. **Bibliography engagement-pending flag updates** (cross-thread item #3) — Pistor / Christophers / Susskind entries in §13: "engagement pending" → "engaged in Ch X §Y" with specific section references. Quick (~1–2 hrs); high-leverage for proposal sprint accuracy.
2. **Ch 6 stale-reference sweep** — several scaffolding files still describe Ch 6 as "single-line HTML pending Insight #21 rewrite"; Insight #21 closed 2026-05-04 + Ch 6 is now clean semantic HTML. Per-section staleness audit batch.
3. **Tech Appendix Phase 3 v2.0.0 rebuild** (~20–30 hrs; post-proposal-sprint timing reasonable)
4. **Glossary v4 rebuild** (post-Phase-3-Tech-Appendix)
5. **GuidanceDoc per-section staleness audits** (Insight #37 follow-up; can be batched per chapter)
6. **Insight #39 pre-publication external review** (post-completion; triggers entire-book citations audit + Insight #63 focused rigor pass)

## Files to read first

- `research/literature/bibliography.md` — especially §13 Pistor / Christophers / Susskind entries
- `manuscript/chapters/Chapter__N_*Draft.md` — all 10 drafted chapters (9 MD + Ch 6 HTML)
- `manuscript/chapters/Chapter__N___GuidanceDoc.md` — internal-scaffolding files (WP#10 layer-classification + staleness disclaimers)
- `manuscript/technical-appendix/` — Phase 3 rebuild target
- `core/glossary/` — Glossary v4 target
- `alignment/commons_bonds_open_insights_v1.0.0.md` — Insights #21 (closed), #39 (pending), #63 (queued)
- `alignment/commons_bonds_working_principles_v1.0.0.md` — WP#10 layer-classification; WP#9 worktree-isolation

## Constraints / disciplines

- **Substance drives length** (per session-handoff v1.51.0+ + author direction 2026-05-08) — don't pad chapters to hit minimum word counts; cuts and additions are content-driven; venue word-limits are constraints to fit, not floors.
- **WP#10 layer-classification:** GuidanceDocs are scaffolding (internal-scaffolding layer; preserved with staleness disclaimers per 2026-05-08 decision); chapter Drafts are publisher-facing (publication layer).
- **Path B no-overlap rule:** chapter prose feeds essay paraphrases (Aeon / Noema / BR), not direct sentence reuse.
- **GuidanceDoc archive position** (decisions-log 2026-05-08): GuidanceDocs stay in place; per-section staleness audit deferred to Insight #39 pre-publication external review (not a sweep — case-by-case if real friction surfaces).

## Cross-thread dependencies

- **Bibliography flag updates** (cross-thread item #3) feed proposal sprint — chapter summaries cite current engagement state
- **Ch 5 + Ch 9 paragraph engagement landed** (commit `d78872e`) — bibliography flags now stale; that's the ~1–2 hr cleanup
- **Ch 3 drafting** — completed 2026-05-09 (commit `3a8b096`); unblocked 2026-05-08 from Colden + Moore briefs. Now part of all-10-chapters drafted set.

## Out of scope

- Essay drafting (separate workstreams per venue)
- Outreach (separate workstream)
- Berggruen essay (separate workstream; AI-free)

## Watch items

- **Ch 6 GuidanceDoc + AGENTS.md + multiple session-handoffs** still carry stale "Insight #21 pending rewrite" language — Insight #21 closed 2026-05-04. Stale-reference sweep (separate from this handoff's bibliography updates) is a smaller cleanup batch.
- **Tech Appendix Phase 3 rebuild** is ~20–30 hrs; needs dedicated session-block, not piecemeal between other work.
- **Insight #39 pre-publication external review** triggers a large audit (entire-book citations + Insight #63 focused rigor pass) — schedule when manuscript stabilizes (Ch 3 now drafted; pending post-essay-cascade-progress).

---

## Update log

- **2026-05-10** — Stale-header fix: Ch 3 drafted 2026-05-09 (commit `3a8b096`). Removed "(excluding Ch 3 draft)" qualifier from title; replaced "9 of 10 chapters drafted" + "Ch 3 draft is excluded" framing with "All 10 chapters drafted"; updated Ch 3 row in chapter-state table; updated workstream-scope sentence; reconciled Files-to-read-first + Cross-thread-dependencies + Out-of-scope sections. Per PM session handoff §9 todo. Source state-change commit: `3a8b096`. Fix commit: see `git log` on this file's most recent change.

---

*End of manuscript completion handoff. Update or supersede when state materially changes.*
