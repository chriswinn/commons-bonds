# Chapter 5 rebuild — round 2 (2026-11-09)

Three fresh versions, drafted after the author's redline of the round-1 printouts. They follow the
round-2 amendment in `tools/workstream-handoffs/ch5-rebuild-brief_2026-10-31_v1.0.0.md` and the
amended one-pass readability rule (`tools/memory/feedback_em_dash_overuse.md`). Round 1 (Variants A
and B in the parent folder) is **superseded**.

## Files

| File | What it is |
|---|---|
| `ch5-out-and-back_2026-11-09.md` | **Out and back.** Starts in Butler's father's room with no roadmap; outward by scale; into time and the unborn; back to the room. |
| `ch5-roadmap-first_2026-11-09.md` | **Roadmap first (the house).** The author's sentence plus a concrete preview; each case enters through an object in the reader's home; ends on the reader at home. |
| `ch5-earned-roadmap_2026-11-09.md` | **Earned roadmap (the distance closes).** Opens on a Baotou scene, then the author's sentence and the roadmap; each case brings the people paying closer to the reader. |
| `_shared-argument-sections.md` | The four argument sections. Word for word in Roadmap first and Earned roadmap; reordered for the zoom in Out and back. |
| `SEALED_claude-assessment_read-after-your-pick.md` | Claude's pick and reasons, committed before the author reads. **Open it after giving your own pick.** |

**How to read:** first three pages of all three back to back, then each in full. The argument
sections are the same everywhere, so read them once.

## Readability, before and after (`tools/scripts/check-prose-clarity.py`)

| | words | avg sentence | sentences > 35 words | > 45 words | HIGH paragraphs | interrupted clauses | comma-stacked |
|---|---|---|---|---|---|---|---|
| Current Ch 5 | 14,168 | 22.0 | 107 | 40 | 12 | 6 | 37 |
| Round-1 A | 14,162 | 22.2 | 107 | 41 | 8 | 6 | 38 |
| Round-1 B | 14,653 | 22.2 | 113 | 45 | 12 | 6 | 39 |
| **Out and back** | 12,592 | 14.0 | 0 | 0 | 0 | 0 | 0 |
| **Roadmap first** | 12,704 | 14.1 | 0 | 0 | 0 | 0 | 0 |
| **Earned roadmap** | 12,584 | 14.1 | 0 | 0 | 0 | 0 | 0 |
| Ch 1 (author-redlined) | 6,542 | 18.1 | 44 | 17 | 3 | 0 | 20 |
| NYRB essay | 8,301 | 24.5 | 70 | 33 | 8 | 3 | 22 |

Watch item: 14 words is shorter than the author's own Ch 1 (18). Some passages may read clipped.

## Fact-check (against `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` and TA §11.2)

- **34 of 34** canonical figures and facts present in each version; no retired figures.
- **Corrections from round 1:**
  - Darity and Mullen's framework is **ARC: acknowledgment, redress, closure** (no "atonement").
  - The **1977** Social Security amendments **raised taxes and trimmed benefits**, and **1983** brought
    another rescue (SSA; CRS). Round 1 wrongly said 1977 declined to raise taxes.
  - **Deepwater** now follows TA §11.2: BP paid about **$61.6 billion** (passing **$65 billion** by
    2018), the largest payment in the book's cases, with **$8–12 billion** of ongoing damage
    unrecovered. The old "recovery ratio well below one hundred percent" overstated this.
- **Flags for the author or a TA pass (not blocking):**
  - The ledger's "NRDA ≈ $17B" for Deepwater doesn't match TA §11.2 ($18.7B for the whole 2015
    settlement). The drafts don't use either number.
  - The Mexico comparison "measured against comparable lengths of damaged coastline" is carried from
    the current chapter and the NYRB essay. It isn't in the ledger; verify at redline.
  - The gate's MEDIUM flag on "$44 billion" (black-lung program vs trust-fund labeling) matches the
    ledger's 2026-06-09 relabel; review only.

## Promotion notes (after the author picks)

Copy the winner into `manuscript/chapters/Chapter__5_TheAccountabilityGap.md`. Then re-pin the
gate allowlist entries for `regressed-term-reparations-bond` (HIGH, the name-and-reject passage) and
check `regressed-figure-108-trillion-social-security` (MEDIUM, the rejection passage). Finally run
`tools/scripts/check-corpus-invariants.sh` → HIGH=0.
