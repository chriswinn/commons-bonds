# Book Proposal — Workstream Handoff (2026-05-09)

**Date drafted:** 2026-05-09
**Branch to create at session start:** `claude/book-proposal-sprint-<harness-id>` (branch from current `origin/main`)
**Status going in:** Skeletons stood up; comp-titles substantive; bio polished. Late-June 2026 sprint target (~3-week focused effort).

---

## Workstream scope

Assemble the agent-facing book proposal — overview + market + comp titles + author platform + marketing plan + chapter summaries + sample chapters + master assembly. Target completion: late June 2026.

## Current state — per file

| File | Status | Notes |
|---|---|---|
| `00_overview.md` | Skeleton | Section sketch + open questions; ~10–15pp prose to write |
| `01_market-and-audience.md` | Skeleton | Section sketch only; needs comp-title BookScan trajectories + Publishers Marketplace research |
| `02_comp-titles.md` | **Substantive** | Tier 1 (Mazzucato + Pistor + Christophers) / Tier 2 (Mission Economy + Susskind) / Tier 3 (Sassen / Patel & Moore / Rodrik); selection rule drafted (lead with Tier 1; round out with ≤1 Tier 3); ~80% of final |
| `03_author-platform.md` | **Bios polished** (commit `2beb640`) | Three lengths: short ~50w / medium ~85w / long ~135w. Placements + Interview tables seeded. Updates as essays place / interviews land. |
| `04_marketing-plan.md` | Skeleton | Section sketch only |
| `05_chapter-summaries.md` | Skeleton | Source-mapping table corrected to drafted chapters (NOT GuidanceDocs); summaries not yet written |
| `06_sample-chapters/` | Empty `.gitkeep` | Recommended samples: Ch 7 + Ch 5 (per cascade plan decision item #4) |
| `proposal-master.md` | Assembly spec | Concatenation order documented; assembly happens at sprint completion |

## Next moves (June 2026 sprint, ~3 weeks focused)

1. **`00_overview.md` draft** (10–15pp) — Hook + thesis + why-this-book + why-this-author + why-now. Lead with one of: McDowell true-cost gap / Mars closed-habitat reversal / plane-at-sunrise vignette. Use Ch 1 / Ch 7 / Ch 8 prose voice (paraphrased per Path B no-overlap).
2. **`01_market-and-audience.md`** — comp-title BookScan trajectories (where accessible); Publishers Marketplace deals tagged "big idea / economics" 2023–2026; course-adoption potential (heterodox econ syllabi, environmental-econ seminars, commons / governance studies); international rights signal.
3. **`04_marketing-plan.md`** — pre-publication essay cascade is the spine; named interview/quote partners (Darity confirmed; Mazzucato pending; Colden/Moore via public record; Dagan via Beth); academic adoption outline; cross-disciplinary readings.
4. **`05_chapter-summaries.md`** — one page per chapter (10pp total), sourced from drafted chapters in `manuscript/chapters/Chapter__N_*Draft.md` — NOT from GuidanceDocs. Read each chapter; write summary from actual prose. Lead each with the *argument move*, not the topic.
5. **`02_comp-titles.md`** — finalize 5–6 selection (recommend Mazzucato + Pistor + Christophers + Susskind + 1 Tier 3 round-out).
6. **Sample chapters** — copy Ch 7 + Ch 5 drafts into `06_sample-chapters/`.
7. **`proposal-master.md`** — assemble single PDF (concatenation order: 00 → 01 → 02 → 03 → 04 → 05 → 06_sample-chapters/). Date-stamp filename: `proposal-master_YYYY-MM-DD.md`.
8. **Update `03_author-platform.md`** as essay placements / interviews land throughout the sprint.

## Files to read first

- `publishing/book-proposal/*.md` (all 7 sections + assembly spec)
- `publishing/book-proposal/06_sample-chapters/.gitkeep` (placeholder)
- `manuscript/chapters/Chapter__N_*Draft.md` (source for chapter summaries; Ch 7 + Ch 5 for samples)
- `publishing/essays/_pipeline/cascade-plan_2026-05-06.md` (Decisions due section + sprint timing)
- `publishing/essays/_pipeline/cross-thread-todos.md` (item #3: bibliography flag updates as engagement-pending → engaged)
- `research/literature/bibliography.md` (§13 comp-title entries with engagement notes)

## Constraints / disciplines

- **Sprint target:** late June 2026 completion (~3-week focused effort).
- **Chapter summaries source:** drafted chapters, NOT GuidanceDocs (resolved 2026-05-08 cleanup; reflected in `05_chapter-summaries.md` source-mapping table).
- **Comp-titles aligned to bibliography:** Mazzucato + Pistor + Christophers + Susskind in `research/literature/bibliography.md` §13; Ch 5 + Ch 9 paragraph engagement landed (commit `d78872e`).
- **Path B no-overlap discipline** if any prose paraphrases from chapter material.
- **Bio variants:** use medium (~85w) for proposal-paragraph contexts; long (~135w) for the dedicated `03_author-platform.md` page.

## Cross-thread dependencies

- **Bio polish complete** (commit `2beb640`) — read `03_author-platform.md` for ready-to-use bios.
- **Bibliography engagement-pending updates** (cross-thread item #3) — would be nice-to-have before proposal sprint so chapter summaries can cite current engagement state. Not blocking, but if updated mid-sprint, summaries gain accuracy.
- **Essay placements** that land between sprint-start and sprint-end go into `03_author-platform.md` Placements section + medium/long bios get a "Recent essays in [venue]" clause.

## Out of scope

- Agent queries (separate workstream — proposal feeds agent prep)
- Essay drafting (separate workstreams per venue)
- Manuscript chapter drafting (separate workstream)

## Watch items

- **Ch 3 status at sprint time** — if Ch 3 not drafted by late June, the chapter summary frames it as work-in-progress; lead with Ch 7 + Ch 5 as the two sample chapters.
- **Aeon submission June 1–7** likely lands in editor-review during the sprint; that's a soft clip for the platform page (medium + long bios get "under consideration at Aeon" updates).
- **Boston Review submission** target mid-July may overlap end of sprint; if so, soft clip available for proposal too.

---

*End of book proposal handoff. Update or supersede when state materially changes.*
