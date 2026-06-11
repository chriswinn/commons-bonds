# Technical Appendix — Confirmed-Findings Ledger (2026-06-06)

**Status: PROPOSED — no edits applied. For author review before any fix touches the file.**
Branch `claude/ta-rigor-audit-260606-f537b4`, held from `main`. Review scope: `git diff origin/main -- manuscript/technical-appendix/`.

**Method.** Loop-until-dry verification workflow (`tools/scripts/ta-rigor-verification-workflow.js`): 4 rounds, 9 diverse discovery lenses + completeness critic per round, adversarial confirm (every candidate re-derived at source / re-checked against live external source by a separate refuter). 130 agents, ~7.4M tokens. Raw: workflow `wb11ll6xt`.

**Result.** 81 confirmed catches → **~45 distinct issues** after merging duplicate independent catches (de-dup notes inline). 8 refuted (false positives killed), 1 uncertain. Severity split among confirmed: 46 HARD / 35 SOFT.

**One workflow caveat (honest):** one finder slot in one round failed to return structured output (lost ~1 of 130 agent-slots). 4 rounds + completeness critic + cross-validation make this low-risk, but it is a known gap.

Legend — **HARD** = numerically/logically wrong; **SOFT** = imprecise label / units / notation / citation. "Seed" = pre-confirmed by the two prior audits and independently re-validated here. "New" = surfaced by this run.

---

## A. HARD — numeric / arithmetic (cascading figures)

### A1. §11.1 carbon term: 2.61 × $190 = $496, not $510  — Seed (4× independent)
- **Loc:** line 3876. `2.61 × 190 = 495.9 ≈ $496`, stated `$510`. Factor 2.61 and SCC $190 both verified correct; pure multiplication error.
- **Fix:** 3876 `$510/ton` → `$496/ton`; 3882 `Total with carbon: $518–532/ton` → `$504–518/ton`; 3898 `$510/ton carbon term` → `$496/ton`.
- **Cascade:** §14.7 line 6620 `at least $518` → `at least $504`.

### A2. §11.1 IPG "(without carbon)" label is backwards  — Seed (3×)
- **Loc:** line 3889. `IPG: 33–122× (without carbon) / substantially higher with full carbon pricing`. The 33–122× band is the carbon-*inclusive* true-RCV ratio; the without-carbon damage-floor ratio is ~0.4–5×.
- **Fix:** → `IPG: 33–122× (with full carbon pricing); without-carbon damage-floor ratio is under ~5×`.
- **Cascade:** none — lines 3148/4504/4900/6203/6217/6238/6570/7434 already treat 33–122× as carbon-inclusive; only 3889 is mislabeled.

### A3. §11.5 Norway "CS-reduction ~84%" mislabels the residual  — Seed (2×)
- **Loc:** line 4440. `1 − $48/$300 = 0.84` is the fraction of CS that *remains*; the reduction is `$48/$300 = 16%`. Contradicts §11.7 line 4943 "captured ~17%".
- **Fix:** `~84%` → `~16%`; "84-percentage-point gap" → "~16-percentage-point gap". (Reframe as residual: "~84% of baseline CS remains.")
- **Cascade:** line 4440 only (do NOT touch the correct §11.7 line 4943).

### A4. §11.6 Method-1 combined anchor < its own component  — Seed (3×)
- **Loc:** line 4674. Combined `Habitability+Ecosystem+Cohesion` stated $1,421–2,412 (conservative) etc., but each is **less than the Habitability-only component** ($1,566–2,610) — Ecosystem ($12–50) + Cohesion ($17–42) were omitted from the sum.
- **Fix:** conservative → **$1,595–2,702**; at-scale → **$812–1,658**; optimistic → **$290–875**.
- **Cascade:** line 4827 (triangulation M1 row), 4869, 4871 (convergence), and §3.6 line 1111 (see A12).

### A5. §11.2 Deepwater IPG 15–17× doesn't reproduce  — Seed (5×)
- **Loc:** line 3924. `$20–30B / $1.1B = 18–27×`, stated `15–17×`.
- **Fix:** `15–17×` → `18–27×`.
- **Cascade:** §9.5 table line 3175 (same `15–17×` cell).
- **Related (New, n21):** the listed components ($18.7B + $4B + $8–12B = $30.7–34.7B) **exceed** the stated "$20–30B total documented" at line 3920 — either the total is understated or there's double-counting to resolve. Author call on which anchor is canonical.

### A6. §11.8 scarcity_multiplier "≈6–7" drops the ×0.05 Hotelling_anchor  — Seed (5×)
- **Loc:** line 5245. Canonical formula (§3.5 line 896) is `1 + log(1+σ)×0.05`; worked values 1.23 (σ=100) and 1.29 (σ=300) confirm the ×0.05. For σ=200–500 the correct multiplier is **1.27–1.31**; "6–7" results only from omitting ×0.05.
- **Fix:** `≈6–7 via log(1+200..500)` → `≈1.27–1.31 via 1 + log(1+200..500)×0.05`.
- **Note:** does NOT weaken §11.8's α-dominance conclusion — the smaller multiplier strengthens it.

### A7. §11.9 intro DAC bands mismatch the canonical bands  — Seed (2×)
- **Loc:** lines 5412–13. Stated `$600–1,200 / $150–500 / $100–200`; canonical (everywhere else, e.g. §3.3 lines 801/807/813) is `$600–1,000 / $300–600 / $100–300`.
- **Fix:** replace intro bands with canonical trio.
- **Cascade:** none — only the intro is off.

### A8. §11.10 Falcon 9 $/kg: $67M / 22.8t = $2,939, not $2,700  — Seed (2×)
- **Loc:** line 5807. `$2,700/kg` → **$2,900/kg** (or $2,939).
- **Cascade:** none (single occurrence).

### A9. §3.4 / §3.6 Norway vintage mismatch vs §11.5  — Seed (6× across keys)
- **Loc:** §3.4 line 859 cites "§11.5" with the *superseded* chain `$1.9T / $2.5T / 50B BOE / $50/BOE`; §11.5 canonical is `$2.0T / $2.67T / 55B BOE / $48/BOE`. §3.6 table line 1097 `$50/BOE` and line 1103 `$12.5T cumulative`.
- **Fix:** §3.4 line 859 → `$2.0T / $2.67T / ~55B BOE / ~$48/BOE`; §3.6 1097 `$50` → `$48`; 1103 `$12.5T` → `$13.75T` (55B × $250).
- **Note:** the §11.7 "$50/BOE" instance was **refuted** as a fix target — leave it (see Refuted list).

### A10. §11.6 Method-1 table cell $300–650 contradicts derived $161–422 (Norway M1)  — New (3×)
- **Loc:** §11.5 table line 4374 M1 cell `~$300–650` vs derived anchor $161–422 (lines 4205–09, 4416–18).
- **Fix:** line 4374 → `~$161–422` (mid-range DAC full scope). **Cascade:** §3.6 line 1094 same cell.

### A11. §11.6 Method-2 per-ton figures don't reproduce  — New
- **n34/35 (HARD):** line 4721 `industry-paid ~$8–15/ton` — $8B/600M = $13.33 → `$8–13/ton`. Cascade 4840, 4907.
- **n37 (HARD):** `societally-paid $50–88/ton` low-end underived — $53–60B/600M = `$88–100/ton`. Cascade 4729, 4840, 4883, 4907.

### A12. §3.6 McDowell Method-1 band $310–1,800 vs §11.6's derived band  — Seed
- **Loc:** line 1111. `$310–1,800/ton` → `$261–2,412/ton` (matches §11.6 line 4827). [At-scale alt: $725–1,484.]

### A13. §11.8 V_option range $500–2,000 vs §11.6 canonical $50–500  — New (2×)
- **Loc:** §11.8 lines 5236, 5245. → `$50–500/ton` to match §11.6 (line 4748).

### A14. §11.10 commercial cost: per-gram vs per-kg unit mismatch  — New
- **Loc:** line 6012. `$1–100/gram` contradicts the section's kg-anchor; orders-of-magnitude figure off.
- **Fix:** → `$50–500/kg (≈$0.05–0.50/g)`; `5–7 orders` → `7–8 orders`.

---

## B. HARD — proofs / logic / dimensional

### B1. Theorem 10.1b proof restates premise P3 as its conclusion  — New
- **Loc:** 3306/3366. The "Proof" derives CS>0 from an empirical premise that *is* the conclusion. Recommend relabel **Theorem → Empirical Observation 10.1b** (matching the 10.2 precedent at 3415–19) and "Proof." → "Supporting argument."

### B2. Theorem 10.1b statement claims "any jurisdiction"; proof delivers only §11 jurisdictions  — New
- **Loc:** 3362. Scope of statement exceeds scope of proof. Narrow the statement to the §11-characterized jurisdictions (per P3).

### B3. §3.1 Definition 1.3 `U ≥ P(t)` is dimensionally inconsistent  — New
- **Loc:** 371. U is a flow `[$·res⁻¹·time⁻¹]`; market price P(t) is a stock `[$·res⁻¹]`. Bound needs annualization `P(t)/H`. Cascade: prose echo line 743.

### B4. §16.1 declining-rate form gives r(0)=r₀+r_min, not r₀  — New
- **Loc:** 7341. `r(t)=r₀·e^−δt + r_min` → should be `(r₀−r_min)·e^−δt + r_min` so r(0)=r₀, r(∞)=r_min.

### B5. §16.2 stock-dependent S(t): prose contradicts the algebra  — New
- **Loc:** 7356. The verbal description of innovation-pressure direction is opposite to the suppression term in the formula (7350). Rewrite prose to match.

### B6. §9.5/§9.6 convergence narrative ordering contradicts the table  — New
- **Loc:** 3250. Text claims Real Options systematically lowest / RCV highest, but the table doesn't support that ordering. Reconcile narrative to table.

### B7. §3.5 "α-dominance sensitivity finding" is a property of the chosen functional form, not an empirical finding  — New (hostile-reviewer)
- **Loc:** 922, 1029–33. Reframe header "Sensitivity finding" → "Property of the chosen functional form"; soften "the real debate is irreversibility" to acknowledge it follows from the posited form.

---

## C. SOFT — proofs / theorem framing (§10, §17, §7)

- **C1 (n3) §10.2 case-set mismatch:** line 3395 names Norway in the "empirical four"; §9.5 table rows are McDowell/Deepwater/Libby/**Baotou**. Swap Norway→Baotou.
- **C2 (n4) §10.3 parts restate Assumption A2:** relabel as Definition-Consequence or add scope note.
- **C3 (n5) §10.3 "without loss of generality":** misapplied to a *posited* functional form (3449). Reword to "one admissible realization."
- **C4 (n6) §10.4 SC1 cites Lebesgue dominated convergence** where the comparison test / monotonicity is what's used (3636). *(Exactly the misapplied-convergence-theorem class you flagged.)* NB: the §17.3 DCT use (7587) is correct — do not change.
- **C5 (n7) Corollary 10.5.1 "proof" is non-derivational** (3816–19) — "direct application," no marginal argument. Supply one or relabel.
- **C6 (n8) §10.5 ΔForeclosure_cost vs _avoided** label mismatch (3747 vs 3766).
- **C7 (n9) §10.5 weak dominance needs only P2–P4**, not P1–P4 (3717).
- **C8 (n76) §7.3 Weitzman convergence claim** needs `r_min > 0` qualifier (2726).

## D. SOFT — citations / literature (§14, §3.5)

- **D1 (n50) §14.1 Hotelling:** `P(t)=P(0)·e^{rt}` is the zero-extraction-cost special case; the Hotelling result is the **rent** path `[P−c]` rising at r (6542).
- **D2 (n51/52) §14.4 Rawls:** paraphrase presented as a verbatim quote (6581). Either real §45 quote or drop quote-marks.
- **D3 (n53) §14.6 Daly inversion:** attributes "S_max must equal 1" to Daly (6609). Daly's claim is S_max<1 for critical natural capital → maintain the stock. **HARD-adjacent** (it inverts the cited author's logic); listed SOFT per fix being a rewording. **Directly relevant to our standing/CSD discussion.**
- **D4 (n69) §3.5 "Solow 1956 QJE"** → "Solow 1974 Review of Economic Studies" (917).
- **D5 (n65/66) §3.5 Hotelling_anchor:** "~5%/yr proxy" applied as a dimensionless coefficient; "conjugate that linearizes" overclaim (908).

## E. SOFT — notation / units / labels

- **E1 (n67/80) "log" never defined as natural log**  — Seed. Add "log = natural logarithm (ln)" at §3.5 line 896; affects worked values at 4311/4761/5245 (all already require ln).
- **E2 (n68) §3.5 σ defined as a dimensioned ratio** but used inside `log(1+σ)` which needs σ dimensionless (892).
- **E3 (n56) §16.2 α,β collide with §3.5's α,β** (7350/7353) — rename or add local-notation note.
- **E4 (n74) §5.4 S(τ|t₀) overloads τ** (also the scarcity threshold) — use t (1348).
- **E5 (n55) §16.1 δ undefined on first use** (7341).
- **E6 (n58) §16.4 "IPG Range" column** holds percentage sensitivities, not IPG ranges (7404).
- **E7 (n59) §16.4 S_max row Low/High cases inverted** vs the ascending convention (7449–58).
- **E8 (n75) §6.7 Gate-2 units phrase** "Dollars × time-domain. PASSES." is loose (1891, 1943).
- **E9 (n41) §11.7 "M3 mid-range $300"** should be $280, or relabel the denominator (4943).
- **E10 (n30) §11.5 M2 caveat bullet $50** → $48 (4258).
- **E11 (n33) §11.6 β-sensitivity xref to "§3.4"** → §3.5/§11.8 (4751).
- **E12 (n36) §11.6 "three independent methods" overclaim** — M2 is the realized-B comparator in CS=RCV−B, not a third RCV estimator (4907). *(Relevant to the CSD-method discussion.)*
- **E13 (n10) §11.1 reclamation shortfall $3.7B** vs §11.6 $4B low-end (3892).
- **E14 (n77/78) §9.1 "six tested cases" / model-independence overclaim** — 4 empirical + 2 thought-experiments; and all three models share the SCC input for fossil cases, qualifying the independence defense (3064).
- **E15 (n81) §11.1 McDowell population endpoint** 18,000 → ~19,000 (matches §7.6 + Census 2020) (3892).

---

## Refuted (false positives the adversarial pass killed — do NOT fix)

1. `9.5/convergence_ordering_artifact` — distinct from B6; the convergence-as-artifact framing didn't hold.
2. `11.7/norway-m2-50-vs-48-stale` — the §11.7 $50/BOE is fine as-is.
3. `10.5/welfare-decomposition-double-count` — no double-count at source.
4. `10.2/hong-page-citation-stretch` — citation supports the claim.
5. `9/dual-three-method-triple-conflation` — did not reproduce.
6. `11.10/falcon-heavy-price-capacity-mode-mismatch` — capacity-mode reading is consistent.
7. `10.4/weitzman-title-attribution-vs-knife-edge-divergence` — attribution is fine.
8. `9.5/carbon-dominates-df-vs-table-without-carbon` — table is consistent.
- Plus the pre-flagged known false positive (Deepwater convergence 1.5×→1.75×) — not reported, as instructed.

## Uncertain (needs author judgment)

- `11.10/mars-colony-low-bound` — the low bound on the Mars-colony anchor couldn't be confirmed or refuted from the stated inputs; flag for author review of the source assumption.
