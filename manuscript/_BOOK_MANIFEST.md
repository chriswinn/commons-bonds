# Commons Bonds — Book Manifest

**Purpose.** The single canonical list of every component that constitutes *the book*.
Any whole-book operation (coherence map, render, rigor sweep, literary-agent sample set,
cross-chapter consistency pass) MUST include every component listed here.

**Why this file exists.** The Technical Appendix lives *outside* `manuscript/` (in `core/`),
and on 2026-06-04 a chapter-scan that read only `manuscript/chapters/` missed it. The book is
not just the `manuscript/chapters/` directory. This manifest prevents that recurrence: when in
doubt about "what is the book," this file is the authority.

---

## Components

### Front matter (in `manuscript/chapters/`)
- `_Dedication.md` — dedication
- `_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md` — Author's Note (end-user-facing; part of the book)
- `_BookLevelGuidance.md` — internal book-level guidance (NOT end-user-facing; scaffolding)

### Chapters (in `manuscript/chapters/`)
1. `Chapter__1_TheQuietMath_Draft.md` — **whole-cloth redraft, working draft (redline pending), 2026-06-05.** Prior month-of-iteration version regressed to `_archive/Chapter__1_TheQuietMath_REGRESSED_2026-06-05.md`. Drop the `_Draft` suffix when the redline is finalized + ratified.
2. `Chapter__2_TheMiner_Draft.md` — **whole-cloth redraft, working draft (redline pending), 2026-06-05.** Prior version regressed to `_archive/Chapter__2_TheMiner_REGRESSED_2026-06-05.md`. Drop the `_Draft` suffix when redline finalized + ratified.
3. `Chapter__3_TheWaterman.md`
4. `Chapter__4_TheExistenceProof.md`
5. `Chapter__5_TheAccountabilityGap.md`
6. `Chapter__6_ThreeWaysofCounting.md`
7. `Chapter__7_OnOtherWorlds.md`
8. `Chapter__8_WhatThingsActuallyCost.md`
9. `Chapter__9_PricingHonestly.md`
10. `Chapter_10_CommonBonds.md`

### Technical Appendix (in `core/technical-appendix/` — OUTSIDE `manuscript/`)
- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` — **canonical**, ~376 KB (100+ pages).
  The formal backbone of the book: the full apparatus reserved from the essays (CS = RCV − B,
  the two-term forward/reverse form, the integral RCV(R, t₀) = ∫…, the Cᵢ components, the Four
  Gates), proofs, theorems, worked methods. Chapters 5, 6, and 10 reference it directly; it is a
  major payoff/grounding target in the book's setup→payoff structure.
- Supporting (validation / sourcing): `block4_validation_2026-04-25.md`,
  `empirical_sourcing_pass_2026-04-25.md`, `method3_sensitivity_analysis_2026-04-25.md`.

### Back matter / apparatus (NEWLY CATALOGUED 2026-06-05 — components the manifest had omitted)
- **Glossary** — `core/glossary/` — **THREE versions exist and the canonical pointer is ambiguous:** v2 is marked SUPERSEDED → v3; **v3 self-declares "Canonical Vocabulary Glossary"** (2026-04-24, 29 terms); **v4 is later and larger** (40 terms) but carries NO canonical / supersede marker. **OPEN DECISION: confirm the canonical version (v3 vs v4) and retire the others.** *(NB: the Ch2 severance-term-choice rationale was added to v4 on 2026-06-05 assuming v4 is latest; if v3 is canonical, move it there.)* The glossary is **back matter** — at assembly it becomes a back-matter section of the book, not a permanently separate document.
- **Bibliography / source apparatus — GAP (do NOT design as multiple bibliographies).** The only existing reference list is **TA §18**, explicitly scoped to "academic citations referenced inline throughout this Tech Appendix." The chapters' journalism / interview / primary / litigation sources (Kennedy, Bailey/Lilly, Latusek/Hamby, Van Zee, GAO reports, Purdue litigation, etc.) have **no apparatus home yet.** **The book should have ONE unified source apparatus:** per-chapter endnotes for inline citations + a single back-matter Bibliography; the TA's references fold into / feed that master rather than competing with it. Building this is a deliberate assembly-stage task. Chapter sources are currently captured in the per-chapter source lists (Ch2 brief §5 + `ch2-v1-redline`) pending the apparatus.
- **Also needed at assembly:** an index; acknowledgments (seed at `manuscript/chapters/_ACKNOWLEDGMENTS.md`).

---

## Structure note + PROPOSED relocation (2026-06-04)

The Technical Appendix is part of the book but sits in `core/`, not `manuscript/`.

**PROPOSED (not yet executed):** relocate `core/technical-appendix/` → `manuscript/technical-appendix/`
so `manuscript/` *is* the complete book. This is the cleaner end-state but is a **deliberate,
audited workstream**, not a casual move: the path `core/technical-appendix/` is referenced by the
render toolchain, by rigor artifacts under `tools/rigor-passes/` and `tools/workstream-handoffs/`,
and by the book-scope doc (`tools/commons_bonds_book_scope_v1_0_3.md`) and various READMEs. The
move must (1) audit every reference to the old path, (2) update them, (3) verify the render
toolchain still builds, before/with the move. Until executed, **this manifest is the authority on
book completeness** and tooling should read the appendix from its current `core/` path.

## Coherence map (2026-06-04)

The book-coherence-map run launched 2026-06-04 covered the 10 chapters + Author's Note only. The
Technical Appendix is being folded into that map (its role + the chapter↔appendix reference
threads) as a follow-on, so the map reflects the whole book per this manifest.
