# RCV Block 4 — Validation Strategy — April 19, 2026

**Status:** Pending review

**Source:** April 19, 2026 session, File 2 (`archive/Consider Including/commons_bonds_new_material_april_19_2026 - Placeholder to consider for inclusion 2.html`), Block 4. Captured 2026-04-23 as a per-section pending-review item in `alignment/decisions/`.

**Integration target (if accepted):** Technical Appendix validation section. Case-study stubs already exist per the linked files below.

**Priority:** Medium–High — determines whether the triangulated estimation framework is falsifiable.

**Related case-study captures:** `research/case-studies/canadian-tar-sands.md`, `research/case-studies/chesapeake-fisheries.md`, `research/case-studies/indigenous-land-dispossession.md` — all sourced from this Block 4. Appalachian coal + Niger Delta already have fuller treatment.

---

**Calibration case — Norway:** Calculate all three RCV estimates for North Sea oil. Method 2 (revealed preference) is the anchor — it IS the Norway data. Methods 1 and 3 should produce numbers that bracket the Norway figure. If Method 1 (replacement cost) comes in below Norway's per-barrel captured value and Method 3 (scarcity-adjusted option value) comes in above, the triangulation is working. If any method produces a wildly inconsistent number, something is wrong with that method's assumptions.

**Primary test cases — Appalachian coal, Niger Delta oil, Canadian tar sands:** Different resource types, different institutional contexts, different depletion levels. The model should produce RCV estimates that rank in an order consistent with qualitative assessment. Appalachian coal (extraction essentially complete, communities devastated) should show very high uncaptured RCV. Niger Delta similar. Canadian tar sands (extraction ongoing, some regulatory framework) should show a different profile.

**Boundary test — Chesapeake fisheries:** A renewable resource pushed past its regenerative capacity — effectively converted into a non-renewable one through overharvesting. The model should handle this gracefully: when S(t) drops below the regeneration threshold, the resource effectively becomes non-renewable and RCV should spike. If the formula captures that transition, it handles a case it wasn't specifically designed for — a strong validity signal.

**Cross-domain test — Indigenous land dispossession:** Land is non-extractable in the oil sense but was permanently transferred. The resource isn't consumed — it's enclosed. Tests whether the model is truly about permanent foreclosure or only about physical depletion. If it can't accommodate enclosure, it's too narrow. If it can, it's more general than initially scoped.

**Sensitivity analysis:** For each case, vary σ, α, and V_option across plausible ranges and map how the output changes. If one parameter dominates — if the answer is always 80% determined by σ regardless of other parameters — that's critical to know. It means the real debate about RCV is a debate about substitutability, and you can focus the intellectual argument there rather than letting people argue about discount rates.
