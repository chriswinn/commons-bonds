# Commons Bonds — Canonical Figure Ledger

**Status: RATIFIED 2026-06-04 (author). J1–J7 resolved below; J5 resolved to a framing pending a primary-source year-lock. This file is now the single source of truth for the book's shared figures.**
Once ratified, this file is the SINGLE SOURCE OF TRUTH for the book's shared figures. Every
chapter, the Technical Appendix, and every derivative essay/op-ed must match it. Built from the
cross-artifact number sweep (`publishing/essays/_pipeline/coal-figure-canonical-sweep_2026-06-04.md`)
and this session's McDowell reconciliation (book-amendment-candidate #5/#7).

**Provenance caveat:** the sweep ran (sandboxed) against the main repo working copy, which lagged
this session's pushed fixes, so its raw discrepancy table shows Ch8/Atlantic/op-ed in their
*pre-fix* state. The canonical set below is current; the "still needs editing" list is the live
cascade.

## Canonical set (McDowell coal / magnitude)

| Figure | Canonical value (pinned label) |
|---|---|
| Mine-mouth price, 1960 | **$4.50/ton** |
| CO₂ emission factor | **2.32 t/short ton** (framework / national-bituminous default) — **2.61** (McDowell-specific, Pocahontas seam). Ratified two-basis split; keep both with rationale. |
| Social cost of carbon | **$190/t** (EPA 2023 estimate; Rennert et al. 2022 *Nature*) |
| **Carbon term — McDowell** ("foreclosure component") | **$496** ( = 2.61 × $190 ). **Pins "$496" = carbon term.** Corrects the old $510. |
| Carbon term — national basis | **$441** ( = 2.32 × $190 ) |
| 4-component Pigouvian floor | **~$504–518** ( $496 + ~$8–22 non-carbon heads ). Corrects $518–532. |
| **8-component honest TOTAL** | **$510/ton**. **Pins "$510" = the TOTAL, never the carbon term.** Corrects the old $524. |
| RCV-model estimate (method-distinct) | **$580–620/ton** — Weitzman declining-rate model estimate; **NOT a damage-function total; never conflate with $510.** |
| **IPG (public headline)** | **33–122×** |
| IPG triangulated central | **~50×** (inflation-corrected; sits inside 33–122×) |
| IPG 555× | TA-internal full-triangulation ceiling only; **never quote bare** (TA §11.6 disowns it as an inflation artifact) |
| McDowell 2020 population | **~19,000 / "under 20,000"** (retire "18,000") |

### Label-pinning (the load-bearing discipline)
- **$496** = carbon term / foreclosure component (McDowell basis).
- **$510** = the 8-component honest TOTAL. The old error labeled $510 as the *carbon term*; corrected, $510 is the *total*. These are opposite meanings — always state which.
- **$504–518** = 4-component Pigouvian floor.
- **$580–620** = RCV-model estimate (method-distinct; keep out of the "total" slot).

## Judgment calls — RATIFIED 2026-06-04 (author)

- **J1. RATIFIED.** Carbon = **$496**, total = **$510**, book-wide (arithmetic-driven; more conservative). Already applied to Ch8 + Atlantic + the op-ed draft; cascade the rest (Technical Appendix, Ch6, Ch2, canonical `op-ed.md`, the 2026-05-11 inventory, the Ch8 pre-pub queue) — this is the execution of book-amendment-candidate #7.
- **J2. RATIFIED.** Public IPG = **33–122×**; **~50×** = triangulated central; **50–555× confined to the Technical Appendix; never quote 555× bare.**
- **J3. RATIFIED.** Harmonize Ch8 "$4–5/ton" → **$4.50**.
- **J4. RESOLVED.** Keep the dated **"$4.5B (2021)"** as a defensible vintage anchor (low-stakes); if a single current figure is later preferred, use the most recent DOL Black Lung Disability Trust Fund debt *with its year*.
- **J5. RESOLVED to a framing (hard-year still needs a primary source).** The U.S. Steel McDowell/Gary shutdown was a **phased wind-down across the 1980s into the early 1990s** (Gary closure often cited ~1986; broader U.S. Steel McDowell exit toward ~1992, ~1,200 jobs), not a single year — which is exactly why the artifacts disagree. **Canonical framing: harmonize every artifact to "across the 1980s" / "by the late 1980s,"** NOT a contested point-year. A specific hard year (1986 vs 1990) must not be stated as fact until locked against a primary source (a Gary/McDowell history, U.S. Steel records, or a contemporaneous news archive) — flagged for the gather/drafting stage.
- **J6. RATIFIED.** Ch6 national-basis carbon = **$441** (= 2.32 × $190); relabel the "$449–464" band accordingly (carbon $441 + non-carbon heads).
- **J7. RESOLVED.** The RCV-model **$580–620** band lives in the **Technical Appendix** (method-distinct, Weitzman declining-rate); chapters/essays use the **$510 total** and may point to the appendix for the higher model estimate. Never conflate $580–620 with the $510 total.

## Cascade targets (expands book-amendment-candidate #7)

- ✅ **Already fixed this session** (worktree + origin/main): **Ch8** ($496/$510/$504–518/IPG 120→ confirm), **Atlantic Ideas** ("more than $500"), **McDowell op-ed** fresh draft.
- ⛔ **Still need editing:** **Technical Appendix** §11.1/§11.6/§9.5/§11.11 (carbon $510, total $518–532, the stale "33–122× cited in Ch6/Ch8" attribution); **Ch6** (national-basis labels + $518–532); **Ch2** (IPG framing); the **canonical `op-ed.md`** (sweep found 2.86 factor / $544 carbon / $558 total — **highest exposure**, NYT/WaPo/PS target — verify and fix); **cross-chapter-consistency-inventory_2026-05-11**; **Ch8 pre-pub queue** (retract its "arithmetic verified" note).
- **Aeon candidate:** no edits ("more than $500" + the shown $496 are already correct).
