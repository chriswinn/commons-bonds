# IPG data table from Workstream 12 (Visualization) — pending reconciliation

**Status:** Pending review — reconcile against current canonical case-study files

**Source:** `archive/workstreams/12_visualization_development.md` (April 19, 2026), Phase 2 "Figure 1: IPG Master Table" section. Captured 2026-04-23 during systematic project-folder review before retiring the Workstream 12 scaffolding file.

**Why preserved:** The 6-case IPG master table contains ratio numbers that differ from the current canonical case-study file framings. The ws12 table was prepared for pre-contract proposal visualization (a "signature figure" per the phased visualization plan); the case-study files have since moved to different — and in some cases simpler — canonical framings. When the case-study earning-its-place audit runs, this table should be one input for reconciling: are the ws12 numbers an intermediate estimate that was superseded, a rigor-distinct calculation worth preserving, or scaffolding that can be retired?

**Related files:**

- `research/case-studies/appalachian-coal.md` (McDowell: 33–122× canonical)
- `research/case-studies/libby-vermiculite.md` (40× cost-to-revenue canonical)
- `research/case-studies/deepwater-horizon.md` (40% cost recovery ratio canonical)
- `research/case-studies/nigeria-oil-contrast.md` (Niger Delta)
- `research/case-studies/opioid-extraction-appalachia.md` (the MTR context is separate from this)

---

## The table (verbatim from Workstream 12)

| Case | Resource | Market Price | RCV Estimate | Documented Costs | IPG Ratio |
|---|---|---|---|---|---|
| McDowell County | Coal (per ton) | $4.50 | $200–$600 | $150–$400 | 45×–133× |
| Deepwater Horizon | Oil (per barrel) | $85 | $180–$220 | $65B total damage | 2.1×–2.6× |
| Libby, Montana | Vermiculite (per ton) | $180 | $2,400–$4,800 | $555M health costs | 13×–27× |
| Baotou Rare Earths | Mixed REE (per kg) | $15 | $85–$130 | Toxic lake cleanup TBD | 5.7×–8.7× |
| Niger Delta | Oil (per barrel) | $65 | $320–$480 | $30B+ damages | 4.9×–7.4× |
| Appalachian MTR | Coal (per ton) | $12 | $280–$450 | $75B health/env. | 23×–38× |

## Ws12's design notes for the table

> Single comprehensive table showing all six backtested cases with market price, RCV estimate, documented costs, and IPG ratio. Color-code IPG ratios (green <5×, yellow 5–15×, orange 15–50×, red >50×). This becomes the table that gets reproduced in reviews and cited in papers.

## Reconciliation questions for case-study audit

1. **McDowell / Appalachian coal.** Canonical case-study file uses **33–122×**; ws12 table uses **45–133×** (overlapping but shifted higher). Which is ratified? Is this the same underlying calculation with different inputs, or a different calculation entirely?
2. **Libby, Montana.** Canonical case-study uses **40× cost-to-revenue ratio** ($100M revenue vs. $4B+ costs); ws12 table uses **13–27× IPG** on vermiculite (per-ton framing). The earlier `commons_bonds_chapter_assessment.md` used 55–82× IPG. Three framings for the same case. Cause may be: per-ton IPG (ws12) vs. lifetime-revenue ratio (canonical) vs. earlier IPG calculation (retired). Confirm which matches current rigor.
3. **Deepwater Horizon.** Canonical case-study uses **40% cost recovery ratio** (framing suited to one-event disasters); ws12 table uses **2.1–2.6× IPG** (a multiplier framing). `commons_bonds_chapter_assessment.md` used **15–17×**. Three different numerical framings for the same case.
4. **Niger Delta.** Canonical case-study file is qualitative comparative analysis (Norway mirror + Venezuela + Iran reference); ws12 table has per-barrel IPG 4.9–7.4×. Determine whether Niger Delta needs a quantitative IPG number in Book One, or the comparative framing is sufficient.
5. **Baotou rare earths.** No standalone canonical case-study file exists. Is Baotou captured elsewhere (Ch 5 draft? Ch 8 guidance?), or is the ws12 table the only numeric source? If the latter, either promote Baotou to a case-study file during the audit or retire the ws12 number.
6. **Appalachian MTR.** Mountaintop-removal coal; may be subsumed under `appalachian-coal.md` or may merit a distinct case-study file.

## Recommended next step

Surface this file during the pending **case-study earning-its-place audit**. For each of the six cases, decide:

- **Which number framing is canonical** (per-ton / per-barrel / per-ton IPG multiplier / cost-to-revenue ratio / cost-recovery percentage).
- **Whether the number belongs in Book One** (ratified inclusion) or stays as research-level detail for Technical Appendix.
- **Whether the ws12 table should be resurrected as Figure 1** after the audit settles the numbers, or retired as pre-audit scaffolding.
