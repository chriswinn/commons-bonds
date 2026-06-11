# TA convergence-claim scope correction — PROPOSED 2026-06-11

**Status:** PROPOSED (author ratification required — end-user-facing TA prose; NOT auto-applied)
**Target file:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`
**Base:** `origin/main` tip `f197c97` (post reef-migration)
**Gate baseline (unchanged worktree):** `check-corpus-invariants.sh --severity HIGH` → exit 0; `csd_rcv_calculations.py` → 0 FAIL (21 values, 0 mismatches, PORTFOLIO VERDICT PASS)
**Touches numbers?** Only descriptive *case-count* words (six → three, four → three). No computed dollar/IPG/parameter figure validated by `csd_rcv_calculations.py` is altered by any option below. The applying session should still re-run both gates per discipline.

---

## 1. The tension (as flagged, verified against current tip)

The §10.2 convergence census (Empirical Observation 10.2; search `tested calibration case landscape`) states:

> "…four forward empirical cases (McDowell coal; Norway oil; Deepwater Horizon; Libby vermiculite) plus two thought-experiment scenarios (asteroid mining; lunar regolith — §13) plus one backward calibration (Chesapeake oyster reef — §11.12): seven cases total — the Damage Function approach, Real Options approach, and RCV model produce IPG estimates within one order of magnitude **across the six forward cases**."

But the §9.5 "Three-Model Convergence Table" (search `Three-Model Convergence Table`) contains only **McDowell, Deepwater Horizon, Libby, Baotou** — and the paragraph immediately after it (search `three cases with computable IPGs`) states the three-model result holds for **three** cases (McDowell, Deepwater, Libby); Baotou supports "a remediation-only floor rather than a full IPG (§11.4)." Norway is **absent** from the §9.5 table — it lives in §11.5 as a *different* kind of calibration.

So "convergence … across the six forward cases" overstates the demonstrated result: the three-model convergence is shown for **3** cases, not 6. **Confirmed:** the reef migration did not introduce this — the loose scope predates it and was inherited verbatim.

---

## 2. Root cause — a two-sense terminology collision on "three"

The TA carries **two distinct "three"-structured apparatuses** that the census sentence conflates:

| | **Three Ways of Counting** | **Three-Model Convergence** |
|---|---|---|
| Members | Method 1 (replacement-cost floor) / Method 2 (revealed-preference) / Method 3 (scarcity-adjusted option value) | Damage Function / Real Options / RCV model |
| Scope | **RCV-internal** — three ways to price *one* model's RCV | **Cross-model** — three *independent* models cross-checked |
| Where worked | Norway (§11.5), McDowell (§11.6), DAC/reef | §9.5 table + §11.1/11.2/11.3 |
| Defined at | §3 / §5 | §9.1 (search `The three models are`) |

The census makes the **Three-Model** claim ("the Damage Function approach, Real Options approach, and RCV model produce IPG estimates within one order of magnitude") but scopes it across the **six forward cases** — a set whose members mostly do *not* carry a three-**model** IPG. Norway carries a three-**ways** triangulation; asteroid/lunar are single-model abundance calibrations; Baotou is a floor. Only McDowell, Deepwater, and Libby carry computable IPGs in all three *models*.

---

## 3. What each case actually demonstrates (verified)

| Case | §  | Role in the apparatus | Three-MODEL IPG? |
|---|---|---|---|
| **McDowell coal** | 11.1 | Forward empirical; full three-model IPG | ✅ computable |
| **Deepwater Horizon** | 11.2 | Forward empirical; "All three models agree within a factor of 1.5" (§11.2) | ✅ computable |
| **Libby vermiculite** | 11.3 | Forward empirical; full three-model IPG | ✅ computable |
| **Baotou rare earths** | 11.4 | In §9.5 table but **remediation-only floor**; IPG "not computable on documented inputs"; floor (tailings liability = 1.2–7.5 yrs export revenue) alone implies CS > 0 | ❌ floor only |
| **Norway oil** | 11.5 | **Deep Three-Ways-of-Counting (M1/M2/M3) triangulation**; the "canonical-existing-B₂ exemplar" — CS reduced (α→0.50–0.75 via GPFG restoration optionality) but not eliminated (~$13–15T residual). NOT in the three-MODEL table. | ❌ different test |
| **Asteroid iron / lunar** | 13, 11.8, 11.10 | **Thought-experiment / boundary calibrations**: RCV model in the abundance regime — asteroid iron returns RCV ≈ market (correct null); lunar helium-3 demonstrates the existential-substitutability gap. Not a three-model IPG comparison. | ❌ single-model calibration |
| **Chesapeake reef** | 11.12 | Single **backward CSD** calibration (M1 floor / M2 corroboration; M3 Open). Already correctly carved out of the IPG comparison by the census parenthetical. | ❌ (correctly excluded) |

**Accurate convergence scope:** the three-model convergence is demonstrated for **the three forward cases with computable three-model IPGs — McDowell, Deepwater Horizon, Libby.** This is exactly what the §9.5 paragraph already says; §10.2 (and two siblings) drift from it.

---

## 4. Every affected location (not just §10.2)

The sweep found the loose scope in **three** places, plus **one** sibling looseness. A coherent fix should address all four together (or the document will contradict itself line-to-line).

| # | Line ~ | Section | Current text | Issue |
|---|---|---|---|---|
| **L1** | 3546 | §10.2 census | "…across the **six forward cases**." | **PRIMARY.** Three-model convergence shown for 3, not 6. |
| **L2** | 3212 | §9.1 Model Independence Defense | "…IPG estimates within one order of magnitude **across six tested cases**." | Same overstatement, in the §9 setup. |
| **L3** | 3552 | §10.2 supporting argument | "…within one order of magnitude **across the tested case landscape**." | Vaguer; not wrong, but should be made explicitly consistent with the corrected 3-case scope so it doesn't re-import the ambiguity. |
| **L4** | 4002 | §11 intro | "validates the three-model convergence. **All four cases show IPG ≫ 1**…" | **SIBLING.** "Four" reads as the §9.5 table (incl. Baotou); Baotou's IPG is not computable, so "all four show IPG ≫ 1" overstates by one. |

**Already-correct anchors (do NOT change — use as the model):** §9.5 paragraph "**The three cases with computable IPGs** produce IPG ≫ 1 across all three models" (line 3398); §11.2 "All three models agree within a factor of 1.5" (line 4084).

---

## 5. Wording options for the PRIMARY (§10.2 census, line 3546)

All options preserve the accurate **seven-case landscape census** (it is correct *as a census*); they differ in how they scope the **convergence claim** within it. HTML entities shown as they appear in-file.

### Option A — minimal scope-narrowing (smallest faithful edit)
Keep the sentence structure; just correct the scope number and append the role distinction.

Replace `across the six forward cases` with:

> `across the three forward cases that carry computable IPGs in all three models (McDowell coal, Deepwater Horizon, Libby vermiculite &mdash; &sect;9.5)`

…and append before the closing sentence:

> ` Norway enters the landscape as the deep Three-Ways-of-Counting calibration and realized-B&#8322; exemplar (&sect;11.5), and Baotou as a remediation-only floor rather than a full IPG (&sect;11.4); neither enters the three-model IPG comparison, and the asteroid and lunar scenarios exercise the RCV model in the abundance regime (&sect;13) rather than the cross-model test.`

**Pro:** one-line scope fix + one clause; lowest disturbance. **Con:** the seven-vs-three distinction stays slightly buried in a long sentence.

### Option B — role-explicit single rewrite
Rewrite the census sentence so each case's role is named inline, then state the convergence claim scoped to the three. (Full prose drafted in §6 of the file co-located note below; structurally similar to Option C but kept to one paragraph.)

### Option C — two-move split (RECOMMENDED): census, then scoped claim
Separate "what the landscape contains" from "what the cross-model test demonstrates." Replace the entire census paragraph (line 3546) with:

> `The framework's tested calibration case landscape spans seven cases &mdash; four forward empirical (McDowell coal; Norway oil; Deepwater Horizon; Libby vermiculite), two forward thought-experiment scenarios (asteroid mining; lunar regolith &mdash; see &sect;13), and one backward calibration (Chesapeake oyster reef &mdash; &sect;11.12) &mdash; but they do not all enter the cross-model test in the same way. The three-model convergence claim proper &mdash; that the Damage Function approach, Real Options approach, and RCV model produce IPG estimates within one order of magnitude &mdash; is demonstrated for the three forward cases that carry computable IPGs in all three models: McDowell coal, Deepwater Horizon, and Libby vermiculite (&sect;9.5). The remaining cases corroborate the framework along other axes rather than entering that comparison: Norway is the deep Three-Ways-of-Counting calibration (Methods 1+2+3) and the canonical realized-B&#8322; exemplar, where institutional architecture has reduced but not eliminated CS (&sect;11.5); Baotou's documented inputs support a remediation-only floor rather than a full IPG, and that floor alone implies CS &gt; 0 (&sect;11.4); the asteroid-iron and lunar scenarios exercise the RCV model in the abundance regime, where it correctly returns RCV &asymp; market price (&sect;13, &sect;11.8); and the reef calibration exercises the &sect;5.5 Method-1-floor / Method-2-corroboration form with Method 3 deliberately Open, demonstrating the apparatus's backward reach rather than entering the three-approach IPG comparison (&sect;11.12). The convergence regularity &mdash; across the three computable cases &mdash; is consistent with the underlying cost severance structure being approximately characterized by all three approaches.`

**Pro:** eliminates the collision at its source; the seven-case census survives intact and accurate; each case's role is explicit and matches §9.5/§11.x; reads as deliberate scoping discipline rather than a hedge. **Con:** longest (one short paragraph → one slightly longer paragraph); subsumes the existing reef parenthetical (folded in, not lost).

### Companion edits (apply with whichever primary option is chosen)

- **L2 (line 3212, §9.1):** replace `across six tested cases` → `across the three cases with computable three-model IPGs (&sect;9.5)`. (Keeps the Model Independence Defense's statistical-improbability argument scoped to the cases it actually rests on.)
- **L3 (line 3552, §10.2 supporting argument):** replace `across the tested case landscape` → `across the three computable convergence cases`. (Optional but recommended for line-to-line consistency; current wording is not false, only vague.)
- **L4 (line 4002, §11 intro):** replace `All four cases show IPG &gg; 1; all four show the same structural pattern (value dispersed, costs concentrated); all four involve B &asymp; 0 relative to RCV.` → `The three cases with computable IPGs show IPG &gg; 1; all four §9.5-table cases show the same structural pattern (value dispersed, costs concentrated) and B &asymp; 0 relative to RCV, with Baotou entering on its remediation-only floor (&sect;11.4) rather than a full IPG.` (Surgically separates the IPG claim, which is true of 3, from the structural-pattern claim, which is true of all 4.)

---

## 6. Recommendation

**Adopt Option C for the §10.2 census (L1), plus the L2 + L3 + L4 companion edits.**

Rationale:
1. The defect is a *scope* defect rooted in a terminology collision; Option C fixes it at the source by separating the **landscape census** (accurate at seven) from the **cross-model convergence claim** (accurate at three), so the two senses of "three" can no longer be conflated.
2. It brings §10.2 into line with the already-correct §9.5 paragraph and §11.2 row — making the document internally consistent rather than self-contradicting line-to-line.
3. It strengthens the claim for the adversarial/peer-review reader: a precisely-scoped "convergence across the three computable cases, with these other cases corroborating along other axes" is *more* defensible than a loosely-scoped "six," not less — it pre-empts the exact reviewer objection that the §9.5 table only shows three.
4. The companion edits are required for coherence: fixing only §10.2 would leave §9.1 (L2) and §11 intro (L4) still asserting six/four.

**If the author prefers minimal disturbance:** Option A (L1) + the L2/L4 companion edits is a sufficient and faithful fallback; L3 can be left as-is (vague but not false).

**Do not change** the §9.5 paragraph (line 3398) or the §11.2 convergence row (line 4084) — they are already the correct model.

---

## 7. Application checklist (for the post-ratification session — NOT done here)

1. Apply the ratified option to the four locations above.
2. `bash tools/scripts/check-corpus-invariants.sh --scope manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html --severity HIGH` → confirm exit 0.
3. `python3 manuscript/technical-appendix/calculations/csd_rcv_calculations.py` → confirm 0 FAIL (expected unchanged: no computed figure is touched; this is a prose-scope correction).
4. Visually confirm no stray render-glyph regressions (em-dash / &asymp; / B&#8322; subscript) in the edited paragraphs.
5. Merge-on-ratification per CLAUDE.md (end-user-facing TA prose): push the ratified commit to `origin/main` via the pre-push reconciliation pattern.

**Until ratified, no change is applied to the TA HTML.** This file is the proposal only.
