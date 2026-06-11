# TA Method-3 (Scarcity-Adjusted Option Value) — input-parameter provenance audit

**Date:** 2026-06-06
**Scope:** Read-only provenance check on the five Method-3 input parameters in
`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` §3.5 (formula defs,
~lines 875–930) + §11.6 McDowell-coal build (~lines 4738–4799).
**Discipline:** HARD no-invented-claims. Only real sources with URLs cited
below; where no defensible source exists, the verdict is "posited assumption —
label as such." No citation was manufactured to make a parameter look sourced.
**Mandate:** determine SOURCED / DERIVABLE-FROM-CITED-INPUTS / POSITED-ASSUMPTION
per parameter. Nothing edited.

---

## Method summary

Method 3 formula (TA §3.5, line 889):

```
RCV_M3 = V_option × scarcity_multiplier(σ) × irreversibility_premium(α)
  scarcity_multiplier(σ)      = 1 + log(1 + σ) × Hotelling_anchor
  irreversibility_premium(α)  = 1 / (1 − α)^β   (β = 1 default; β = 2 precaution)
```

McDowell-coal calibration (TA §11.6, lines 4740–4753): σ ≈ 200–500;
α ≈ 0.85–0.95; V_option ≈ $50–500/ton; β = 1. Mid-range build (σ=300, α=0.9,
V_option=$200, β=1) → ~$2,580/ton; sensitivity $420–$13,100/ton at β=1.

### In-repo provenance trail (what actually exists)

1. **`manuscript/technical-appendix/method3_sensitivity_analysis_2026-04-25.md`** is
   the canonical in-repo source for all three parameter ranges. It presents them
   explicitly as **analytical sensitivity ranges**, NOT empirically sourced
   values. Status header: "Analytical sensitivity (not full Monte Carlo) —
   appropriate for the current formal-spec stage where Method 3 is sketch-form."
   §6 ("Open work flagged") lists as STILL-OPEN: "Hotelling_anchor empirical
   specification … Per-case Hotelling-anchor calibration is empirical work
   parallel to Block 4 validation" and "β-calibration empirical study … Currently
   β = 1 is methodological-default." The σ/α/V_option ranges are mapped to regimes
   by qualitative reasoning + named example cases, with no external citation
   attached to any numeric endpoint.
   - NB drift: that file gives McDowell **V_option ≈ $500–$2,000/ton** (line 139);
     the TA §11.6 build uses **$50–500/ton**. The ranges do not match — neither is
     sourced, but they are internally inconsistent across the two in-repo artifacts.
2. **`manuscript/ledgers/_DEEP-SOURCE-REPORT_2026-06-04.md`** (¶64–66) classifies the
   Method-3 per-ton range as an **INTERNAL-DERIVATION**: "the output is the book's
   own computation … none should be expected" externally. It names candidate INPUT
   citations — "Dixit & Pindyck 1994 (real-options); Arrow-Fisher-Hanemann-Henry
   quasi-option-value; Hotelling 1931 / Pindyck 1978" — and recommends labeling the
   output book-derived + footnoting inputs. Note: this report asserts the
   arithmetic "reproduces in-repo," which is true (the formula is deterministic
   given the parameters); it does NOT assert the parameter *values* are sourced.
3. **`research/literature/bibliography.md`**: Dixit & Pindyck 1994 is in the bib
   (line 695) but cited only as lineage for the Substitutability Function S(t|t₀),
   NOT for any irreversibility-fraction or option-value number. Hotelling 1931
   (line 831) is cited for the rent-path *identity* (RCV − Hotelling rent = Cost
   Severance), NOT for a 5%/yr rate. **Arrow & Fisher 1974 is NOT in the
   bibliography at all** despite being the canonical quasi-option-value source and
   being named in the deep-source report.
4. **`research/case-studies/appalachian-coal.md`**: narrative only; contains zero
   Method-3 parameter sourcing.
5. **`empirical_sourcing_pass_2026-04-25.md`**: addresses Method-1 SCC anchors
   only; does not touch Method-3 σ/α/V_option.

### §3.5 functional-form citation accuracy (separate defect found)

§3.5 (TA lines 904–918) justifies the `log(1+σ)` form by citing **Atkinson 1970
*JET*; Cobb & Douglas 1928 *AER*; Solow 1956 *QJE*; Bergson 1938 *QJE*.**

- Atkinson 1970 *Journal of Economic Theory* 2:244–263 — REAL, correctly cited as
  to existence (inequality measurement / log-utility). Topical fit to a *scarcity*
  multiplier is a stretch, but the citation is not fabricated.
  https://ideas.repec.org/a/eee/jetheo/v2y1970i3p244-263.html
- **Solow 1956 *QJE* is MISATTRIBUTED.** Solow 1956 QJE 70(1):65–94 is "A
  Contribution to the Theory of Economic Growth" (the neoclassical growth model) —
  NOT "long-horizon utility aggregation under intergenerational discounting" as
  §3.5 claims. The intergenerational-equity Solow is **Solow 1974 *Review of
  Economic Studies* 41:29–45**, which IS the entry in the project bibliography
  (line 900). §3.5 cites the wrong Solow paper for the claim it makes.
  https://ideas.repec.org/a/oup/qjecon/v70y1956i1p65-94..html
- Cobb & Douglas 1928 *AER* and Bergson 1938 *QJE* are real classic papers, but
  ground a production-function / social-welfare-function lineage, not a
  scarcity-cost-amplification form; they are decorative-lineage, not load-bearing.

The genuinely on-point literature for V_option + α — **Arrow & Fisher 1974,
"Environmental Preservation, Uncertainty, and Irreversibility," *QJE* 88(2):312–319**
(quasi-option value of preserving an irreversibly-losable resource under
uncertainty) — is the one source §3.5 does NOT cite.
https://ideas.repec.org/a/oup/qjecon/v88y1974i2p312-319..html

---

## Per-parameter verdicts

### 1. σ (scarcity parameter) ≈ 200–500 for coal
- **Value in TA:** σ ≈ 200–500 (effective scarcity; commons-stock / sustainable-flow).
- **Verdict: POSITED ASSUMPTION.** No external citation exists for a coal σ in this
  range or for the stock/sustainable-flow σ *definition* as a quantified construct.
  The 200–500 band is assigned by qualitative regime-mapping in
  method3_sensitivity_analysis (line 35: "100–1,000 … effectively non-renewable …
  coal seams"); the McDowell pick of 200–500 within that band is a judgment call.
- **Closest real anchor:** The *concept* — that coal is non-renewable on
  civilizational timescales (regenerates over geological time) — is uncontroversial
  and citable to standard resource economics (Hotelling 1931; any geology text). But
  that grounds "σ is large," not "σ = 200–500." The specific number is posited.
- **Recommended treatment:** Label σ ≈ 200–500 as a **posited modeling parameter**
  (a stock-to-flow ratio assigned by the framework's regime taxonomy), not an
  empirical measurement. Note that Method-3 output is near-insensitive to σ in this
  range anyway (scarcity_multiplier moves only 1.27→1.31 across 200→500), so the
  posited status carries little quantitative weight.

### 2. α (irreversibility fraction) ≈ 0.85–0.95 for coal
- **Value in TA:** α ≈ 0.85–0.95 (share of loss that is irreversible).
- **Verdict: POSITED ASSUMPTION.** No source provides an empirical irreversibility
  *fraction* for coal/MTR habitat. The real-options + quasi-option-value literature
  (Dixit-Pindyck 1994; Arrow-Fisher 1974) establishes that *irreversibility raises
  preservation value* and motivates an irreversibility premium — but supplies no
  calibrated α ∈ [0,1] for any specific resource. The 0.85–0.95 band is the
  framework's qualitative regime assignment (sensitivity file line 49: "0.9–0.99 …
  Mountaintop-removal Appalachian habitat").
- **Closest real anchor:** **Arrow & Fisher 1974 (QJE)** + Dixit & Pindyck 1994 —
  citable as the theoretical basis for *having* an irreversibility premium and for
  the qualitative claim that MTR habitat / atmospheric-carbon transitions sit at the
  high-irreversibility end. They do NOT ground the numeric 0.85–0.95.
- **Recommended treatment:** Label α as a **posited risk-posture parameter** with
  Arrow-Fisher 1974 cited for the *form/motivation*. Flag prominently: because
  irreversibility_premium = 1/(1−α)^β, the output is **extremely sensitive** to α in
  this range (0.85→0.95 swings the premium 6.7×→20×). The most load-bearing Method-3
  parameter is also the least sourced — this is the audit's highest-priority finding.

### 3. V_option ≈ $50–500/ton for coal
- **Value in TA:** $50–500/ton (per-ton option value of preserving coal for
  future non-energy uses + climate stability).
- **Verdict: POSITED ASSUMPTION.** No source publishes a per-ton coal option value.
  The sensitivity file itself gives a *different* posited band ($500–$2,000/ton),
  confirming the number is an internal judgment, not a measurement (and the two
  in-repo artifacts disagree).
- **Closest real anchor:** Arrow & Fisher 1974 (quasi-option value) + Dixit-Pindyck
  1994 (real-options option value) for the *construct*; for the climate-stability
  component, the EPA Social Cost of Carbon (~$190/ton CO₂, 2023) is a citable
  adjacent magnitude — but SCC prices CO₂ damage, not coal option value, so it is an
  analogy not a source.
- **Recommended treatment:** Label V_option as a **posited dimensional anchor**,
  cite Arrow-Fisher 1974 / Dixit-Pindyck 1994 for the option-value construct, and
  reconcile the $50–500 (TA) vs $500–2,000 (sensitivity file) discrepancy. Add the
  deep-source report's recommended caveat that the $13,100/ton high corner is a
  model corner, not an empirical/SCC price.

### 4. Hotelling_anchor ≈ 0.05 ("~5%/yr proxy")
- **Value in TA:** 0.05, used as the coefficient in scarcity_multiplier.
- **Verdict: POSITED ASSUMPTION, with a conventional anchor.** 5%/yr is a *standard
  illustrative* interest/discount rate in the Hotelling-rule literature (e.g., the
  Minneapolis Fed exposition uses a 5% interest rate as its worked example). But it
  is a textbook convention, NOT an empirically estimated coal Hotelling rent rate —
  and the empirical Hotelling literature largely *fails to confirm* that in-situ
  resource value rises at the interest rate at all (Cairns: scarcity rent ≤5% of
  metal value; broad rejection of the strong Hotelling prediction). The
  sensitivity file's §6.3 explicitly lists "Hotelling_anchor empirical
  specification" as OPEN WORK.
- **Closest real anchor:** Hotelling 1931 (JPE 39:137–175, already in bib) for the
  rule; the 5% figure is citable as a conventional proxy rate (Minneapolis Fed
  Economic Policy Paper 14-5) but should be flagged as illustrative-convention.
- **Recommended treatment:** Label as a **posited proxy rate** anchored to the
  Hotelling-rule convention; cite Hotelling 1931 + note the 5% is a standard
  illustrative rate, not a coal-specific empirical estimate, and that the empirical
  Hotelling literature is mixed-to-negative. Quantitatively this matters little
  (enters only through the log term).

### 5. β = 1 (default; β = 2 sensitivity)
- **Value in TA:** β = 1 default, β = 2 precaution-regime.
- **Verdict: POSITED MODELING CHOICE (correctly so).** β is explicitly a
  risk-posture calibration parameter, not an empirical quantity. The sensitivity
  file (line 108) states this directly: "β itself is a fourth sensitivity parameter
  — but its role is methodological (how risk-averse is the framework's posture?)
  rather than empirical." This is the one parameter already correctly framed as a
  choice rather than a measurement.
- **Closest real anchor:** Precautionary-principle / risk-aversion literature
  generally; no specific value needed since it is avowedly a modeling dial.
- **Recommended treatment:** No change needed beyond what the framework already
  does — keep presenting β as an explicit risk-posture choice with β=1 conservative
  default + β=2 precaution sensitivity reported.

---

## Bottom line

**All four empirical-looking parameters (σ, α, V_option, Hotelling_anchor) are
POSITED ASSUMPTIONS, not sourced values and not derivable-from-cited-inputs.** β is
a correctly-labeled modeling choice. None is fabricated-with-fake-citation; the
framework's own in-repo sensitivity file already treats them as analytical
sensitivity ranges and flags Hotelling_anchor + β as open work. The exposure is that
the *published* TA §3.5/§11.6 presents the numbers with qualitative rationale that
can read as empirical grounding, when the honest status is "posited modeling
parameters."

**Highest-priority items:**
1. **α is the most load-bearing and least sourced** parameter (output ∝ 1/(1−α)^β).
   Must be labeled a posited risk-posture parameter, with Arrow-Fisher 1974 cited
   for form/motivation only.
2. **Citation defect in §3.5:** Solow 1956 *QJE* is misattributed (it is the growth
   model; the intergenerational-equity paper is Solow 1974 *RES*, already in the
   bib). The genuinely on-point source — Arrow & Fisher 1974 *QJE* — is cited in the
   deep-source report but absent from §3.5 and from the bibliography.
3. **Internal inconsistency:** V_option = $50–500/ton (TA) vs $500–2,000/ton
   (sensitivity file). Reconcile.
4. Recommended framing (consistent with deep-source report): label the Method-3
   output an explicitly book-derived upper-bound estimate; footnote V_option/α to
   Arrow-Fisher 1974 + Dixit-Pindyck 1994 as *construct* sources; footnote
   Hotelling_anchor to Hotelling 1931 as a conventional proxy; state σ/α as posited
   regime parameters; keep β as an explicit risk dial.

## Sources (web-verified)
- Dixit & Pindyck, *Investment under Uncertainty* (1994): https://press.princeton.edu/books/hardcover/9780691034102/investment-under-uncertainty
- Arrow & Fisher 1974, "Environmental Preservation, Uncertainty, and Irreversibility," *QJE* 88(2):312–319: https://ideas.repec.org/a/oup/qjecon/v88y1974i2p312-319..html
- Hotelling's rule (overview + empirical mixed record): https://en.wikipedia.org/wiki/Hotelling's_rule ; Minneapolis Fed Economic Policy Paper 14-5 (5% illustrative rate): https://www.minneapolisfed.org/~/media/files/pubs/eppapers/14-5/eppaper14-5.pdf
- Atkinson 1970, *JET* 2:244–263: https://ideas.repec.org/a/eee/jetheo/v2y1970i3p244-263.html
- Solow 1956 *QJE* 70(1):65–94 (growth model — the misattributed cite): https://ideas.repec.org/a/oup/qjecon/v70y1956i1p65-94..html
