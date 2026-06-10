# Book proposal — §00 + §05 recascade after TA closeout + canonical-ledger amendments (RATIFIED 2026-06-10)

**Date:** 2026-06-10 · **Trigger:** 135-commit advancement of `origin/main` (2026-06-09 TA closeout consolidation; canonical-figure-ledger amendments; Ch 1 author redline; Ch 5 coercion-deferral standing fix) · **Scope decision requested by author:** "step back and decide if you need a whole cloth redo of part / all of your work." · **Status:** RATIFIED — corrections implement already-author-ratified canonical decisions; applied + pushed per merge-on-ratification.

---

## Scope decision

**Surgical fixes + two whole-cloth summary blocks. NOT a full redo.**

Reasoning: the §00 overview was drafted against the current whole-cloth Ch 1 + Ch 5 drafts (only surgical line-edits landed on those files afterward — Ch 1: 4 lines; Ch 5: 2 lines). The §00's structure, hook, instrument definitions, lineage positioning, why-author, and why-now sections all survive. What went stale was (a) the figure-carrying convergence sentence, (b) two phrasings that author-ratified decisions retired in parallel, and (c) the §05 Ch 1 + Ch 5 summary blocks, which were written 2026-05-11 against the since-archived chapter versions.

## Delta findings + fixes applied

### §00_overview.md (5 fixes)

| # | Finding | Fix |
|---|---|---|
| R-1 | **Coercion-deferral standing-gatekeeping regression.** Pass 3.1 F-3.1-H4 added "leaving the moral weight of that question to those who hold the standing to carry it" — the exact pattern retired from Ch 5 by RATIFIED commit `99f8270` per `feedback_coercion_pricing_first_person_abstention.md` (author's stance: first-person abstention, NO gatekeeping of who may price coercion). | Aligned to Ch 5's ratified register: "one the reparations-economics field is already carrying forward and one this book does not undertake." |
| R-2 | **"Rhyme" metaphor diverged from author redline.** Ch 1 commit `0a9cb55` consolidated the Tubman-passage metaphor on "shape" (away from "rhyme"). §00 carried "pattern rhymes... naming the rhyme." | "The pattern repeats across a striking range of cases... naming the shape they share is not the same as making the cases equal." |
| R-3 | **Stale coal price.** $4.50 → canonical $4.71 (EIA Table 7.9, bituminous; ledger J3 + 2026-06-09 sharpening). | "just under five dollars" (prose register per ledger). |
| R-4 | **Stale total + retired convergence ranges.** $558 total (carried $544 carbon on the 2.86 factor); "five to a hundred-and-thirty-three times / nineteen to forty-seven times" = the retired 5–133× / 19–47× ranges; Libby "fifty-five to eighty-two / forty to eighty" inconsistent with new Ch 5's honest-band Libby treatment (~9-10× documented; low billions plausible). | Rebuilt lens-explicit: "roughly five hundred ten dollars per ton — over a hundred times the mine-mouth price by the carbon-externality measure, and eight and a half to twenty-six times even by the framework's most conservative lens, which prices only the foreclosure premium and does not depend on the price of coal at all. Libby returns the same direction: documented public costs an order of magnitude above the mine's lifetime revenue before a single uncompensated death is counted." |
| R-5 | **Status header.** | Recascade noted; date-modified bumped. |

### §05_chapter-summaries.md (4 fixes)

| # | Finding | Fix |
|---|---|---|
| R-6 | **Ch 1 block described the ARCHIVED chapter** (plane-at-sunrise opener; "quiet math we all eventually do"; Dunbar/Du Bois close — all from the pre-2026-06-05 version). | Whole-cloth redraft against the current chapter: colleague-on-rooftops recognition opener; DMV-lease method-formation; grandfather/father/NIH inheritance chain; no-villain discipline; Tubman + Underground Railroad with the shape-not-equal boundary; $400K-ceiling close; "empty columns" ledger ending. |
| R-7 | **Ch 5 block described the ARCHIVED chapter** — including the now-debunked "$108 trillion... largest intergenerational cost severance in human history" claim that the NEW Ch 5 explicitly names as dishonest and retires; missing the chapter's heaviest new sections (Polanyi/Fraser structural-commons identity; Sandel answer; Public Choice rent-seeking complement + AEI/Cato/Mercatus/GMU invitation; four-objection 2008 treatment; Sweden choice-proof; Exxon Valdez; first-person coercion deferral). | Whole-cloth redraft against the current chapter. The $108T claim now appears in the summary only as the thing the chapter retires. |
| R-8 | **Ch 6 block carried retired convergence figures** ("McDowell at 5–133× and 19–47×. Libby at 55–82× and 40–80×") — flagged open-cascade by the ledger itself. | Lens-explicit per ledger: carbon-externality >100×; RCV-integral 67–134×; M3 8.5–26× (center ~15×); Libby + marine cases degraded to direction-claims pending Ch 6 chapter edit. |
| R-9 | **Ch 8 block carried the stale triplet** ($4.50 mine-mouth; 2.86 factor "Rennert-anchored"; $544 carbon; $558 total) — same triplet the ledger flags at highest exposure in the op-ed. Also "the county the book opened with" (the book no longer opens on McDowell). | $4.71 / 2.61 (Pocahontas-seam, AP-42 + measured heat content; EPA-2023-not-Rennert attribution) / $496 / $510. "The county Chapter 2 walked through." |

### chapter-redraft-priority_2026-06-03.md (1 fix)

| # | Finding | Fix |
|---|---|---|
| R-10 | Historical handoff doc quotes $4.50/$558 — fine as audit trail, but quotable by a future session. | Figure-supersession note added at header pointing to the canonical ledger. |

## Residual-sweep verification

`grep -rnE '4\.50|\$558|\$544|2\.86|33.122|5–133|19–47|55–82|40–80|108 trillion|rhyme' publishing/book-proposal/*.md` → clean except the annotated historical handoff doc.

## What was checked and left unchanged

- **Ch 4 summary "rents have been internalized"** — describes Norway's fiscal architecture (true; Ch 4's own framing), not the retired Ch 6-backtest M3 "rent captured $48/BOE" framing. Left.
- **Ch 6 summary "Norway backtest: CS small but positive"** — consistent with the new irreversibility-reduction framing. Left.
- **§00 hook Deepwater "4.9 million barrels" + healthcare "$54/$461/ninety-percent"** — consistent with the new Ch 5. Left.
- **§00 "first food stamps in American history"** — McDowell County 1961; stands. Left.
- **Norway $1.9T** — still the pre-send re-verification gate (unchanged from Stage 5 sign-off).
- **Platform infrastructure** (03_author-platform anchor; platform-paragraph-snippets.md) — no figure dependence. Left.

## Stage 5 sign-off status

The 2026-06-09 Stage 5 sign-off remains in force with this recascade as its first amendment. The §00's three external gates are unchanged (Stage 4 render-audit offline; per-Wave platform refresh; Norway figure re-verification). The §05 summaries now carry a fourth, self-noted gate: Ch 2/3/4/7/9/10 blocks re-verify as those chapters' own redrafts land (Ch 2 IPG framing + Ch 6 chapter prose are still flagged for editing in the ledger; the summaries track the ledger's destination state).

## Process note (for the regression record)

R-1 is worth a line in the audit trail: this session's Pass 3.1 introduced standing-gatekeeping language in good faith on 2026-06-09 — the same day a parallel session was retiring that exact pattern from Ch 5. The Stage 1c cross-artifact coherence map caught it in the chapter corpus; this recascade caught it in the proposal. The discipline (`feedback_coercion_pricing_first_person_abstention.md`) is now in the always-load memory set, which is the right fix: sessions drafting publisher-facing prose will carry the abstention register from the start rather than learning it by collision.

## Update log

- **2026-06-10.** Recascade RATIFIED + applied + pushed. 10 fixes across 3 files; 2 whole-cloth summary blocks redrafted.
