# Chapter 5 rebuild — 2026-10-31 session output (drafted + judged; author picks in December)

**What this folder is.** The Fall-plan W1 Chapter 5 rebuild, fired inline in one session per the lean
pipeline. The approved brief is `tools/workstream-handoffs/ch5-rebuild-brief_2026-10-31_v1.0.0.md`;
the 2008 first-person substrate is `research/story-drafts/ch5-2008-anchor-author-note_2026-10-31.md`.
**The author picks the winner in December.** Nothing here is promoted to the chapter file.

## Files

| File | What it is |
|---|---|
| `ch5-ssa-1972-verification_2026-10-31.md` | The SSA 1972 fact base used for the Social Security rung. **Confirmed:** the 20% increase (effective Sept 1972, checks early Oct, a month before the Nov election), the deferred payroll-tax funding, the automatic COLA (first payable 1975), the flawed indexing + 1977 partial fix. **Could NOT confirm:** that 1972-era Trustees reports already named the deficit window — so that claim (present in candidate C) was removed from A and B. |
| `ch5-variant-A-scale-narrative_2026-10-31.md` | **Variant A** — scale-narrative, out-and-back. Opens + closes on a single body; full zoom-out between; Social Security = the turn from space into time. ~14,160w. |
| `ch5-variant-B-grounded-scatter_2026-10-31.md` | **Variant B** — grounded scattered-cases. Current chapter's architecture (unlike cases, by surprise; register climbs to the dying body), rebuilt fresh with the anchors + insertions. ~14,650w. |
| `ch5-judge-A-B-C_2026-10-31.md` | The judge: A vs B vs current (candidate C) on brief §6.5 (grounding diagnostic + scale-vs-scatter) + fidelity/positioning/voice/non-regression, with the recommendation. |
| `ch5-winner-factcheck-critic-devread_2026-10-31.md` | Lean-pipeline steps 3–5 on the winner: ledger fact-check, one strongest-critic read (4 readers), developmental read phrased as questions, Darity Tier-S inventory. |

## Recommendation (one line)

**Variant A** is the strongest chapter on the brief's own criteria and the freshest sample for
Darity; **Variant B** is the strong, low-risk fallback (it is C's proven architecture with all the
upgrades folded in). **Candidate C should not win as-is** — keeping it still requires folding in
Insertions B/C/G, the Kapp credit, the first-person 2008 beat, and the Social Security fix, which is
the work B already contains. The real choice is **A (bold/on-thesis) vs B (safe/proven arc)**; the
deciding question is whether the author wants the scale-zoom conceit and is willing to open on the
dying body rather than climb to it. Full reasoning + the author's developmental questions in the judge
and fact-check files.

## How A and B differ from the current chapter (candidate C)

Both A and B carry three upgrades C lacks: (1) **Insertions B/C/G** placed (Broome re-assignment;
Fanning & Hickel / CARICOM / Loss and Damage atmospheric-debt tributary, credit-only no figure;
Pistor's four attributes / non-convertible + non-transferable); (2) the **first-person 2008 beat**
(rendered only from the substrate note, no figures, role at "in sales," ending on "reset to starting
over"); (3) the **documented 1972 Social Security anchor** without the unverified "every actuarial
report named the deficit window" claim. Both also add the **Kapp (1950) + Martínez-Alier/Bullard**
asymmetry-diagnosis credit (brief §2) that C only gestures at.

## Promotion steps for the December session (after the author picks)

1. **Copy the winning variant into** `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` (drop
   the candidate header comment; keep the working-draft header convention).
2. **Re-pin the gate allowlist.** The `regressed-term-reparations-bond` HIGH pattern
   (`tools/quality-gates/regressed-patterns.yaml`) is allowlisted at `Chapter__5...md:202` for the
   legitimate name-and-reject passage. The promoted winner's "Reparations Bond" line will be at a new
   line number — **re-pin that allowlist entry's `line:` in the same commit**, or the gate blocks
   (HIGH). (Same discipline note already in the allowlist rationale: "re-pin if Ch 5 shifts.")
3. **Apply the one Tier-W citation fix.** Confirm Darity & Mullen's redress framework wording against
   *From Here to Equality* — it is widely cited as **ARC: Acknowledgment, Redress, Closure**; all three
   candidates currently say "acknowledgment and atonement, then redress, then closure." Fix before the
   chapter goes to Darity (he authored the framework). See the fact-check file §1a.
4. **Run the gate** (`tools/scripts/check-corpus-invariants.sh`) on the promoted chapter → confirm
   HIGH=0.
5. Then the author's hand redline → grammar-and-punctuation polish → Ch 5 to Darity Jan 4–5.

## Open flags carried forward

- **SSA actuarial-warning element unresolved at the source.** If the author wants to strengthen the
  Social Security rung with a *verifiable* contemporaneous Trustees-report line, that needs SSA's
  pages readable (they 403 the fetch tool's bot filter even though the host resolves) or a primary
  source in hand. Not a blocker; A/B stand on the confirmed record.
- **Darity Tier-S:** every Darity reference in the winner is Tier W (published); nothing from the
  2026-05-13 call is quoted. One consent-tracker flag open: confirm the *citation form* of *From Here
  to Equality* / *Umbrellas* against the 2026-05-15 packet before send.
