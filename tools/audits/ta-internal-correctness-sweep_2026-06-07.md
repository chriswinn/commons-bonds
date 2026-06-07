# TA Internal-Correctness Sweep — Session C (2026-06-07)

**Status: PROPOSED — no edits applied. Present → ratify → apply.**
Branch `claude/ta-internal-fixes-260607-208b7b` (off HELD `claude/ta-rigor-audit-260606-f537b4`). Do NOT merge to main.

**Scope:** the rigor-ledger items where "defensible" = internal logical/mathematical correctness needing NO external sourcing. Eight items (ledger B1–B7, D3, D4). Each verified against the **current** file (line numbers below are current, not stale-ledger). Method-3 formula *structure* (§11.8/§3.5/§11.6) deliberately untouched — that is the M3 Path-B session's domain; only the §3.5 citation + α-dominance *framing* are touched here, neither of which is formula structure.

---

## 1 — §16.1 declining-rate form gives r(0)=r₀+r_min, not r₀ (ledger B4)

**Loc:** line 7341.
**Current:** `where r(t) = r₀ · e−δt + r_min`
**Error:** prose (7344) says r "starts at r₀ … declines to r_min." But r(0) = r₀·e⁰ + r_min = **r₀ + r_min**, and r(∞) = r_min. The form overshoots the stated initial rate by r_min.
**Options:**
- (A) `r(t) = (r₀ − r_min)·e−δt + r_min` → r(0)=r₀ ✓, r(∞)=r_min ✓.
- (B) Redefine the prose to say "starts at r₀+r_min." (Rejected — contradicts every downstream "~4–5% initial" usage.)
**Recommendation:** A.
**Reasoning:** Standard Weitzman/exponential-decay-to-floor form; makes formula match the prose and the ~4–5%→~1% numbers. Pure internal correctness.
**Adjacent (not bundled):** δ is undefined on first use here (ledger E5) — optional one-clause add while editing 7344; flagged, not applied without separate OK.

---

## 2 — §16.2 stock-dependent S(t): prose contradicts the suppression algebra (ledger B5)

**Loc:** formula 7350, prose 7356.
**Current formula:** `S(t | t₀, Q(t)) = S_base(t) · [1 − α · (Q_critical / Q(t))^β]`, α,β>0.
**Current prose (7356):** "When stock Q is large, innovators have low incentive to develop substitutes… As Q approaches Q_critical…, **innovation pressure increases and S_base rises faster.**"
**Error:** The bracket is a **suppression** term. Q large → ratio small → bracket ≈ 1 → S ≈ S_base. Q → Q_critical → bracket → (1−α) → S **falls**. So the formula *suppresses* S as the stock depletes; the prose claims S *rises* as Q→Q_critical. Opposite sign. (Note also: for Q < Q_critical the bracket can go negative — a separate boundedness gap; out of scope, flagged only.)
**Options:**
- (A) Rewrite the prose to match the formula's suppression direction (keep formula).
- (B) Change the formula to match the prose. (Rejected — scope says rewrite prose; the suppression reading is the one the closing "stranded-asset" sentences already want.)
**Recommendation:** A. Proposed replacement prose:
> When stock Q is large the suppression term α·(Q_critical/Q)^β is negligible and achieved substitutability sits at its baseline S_base — abundance keeps prices low and removes the economic pressure that would drive substitute development, but the penalty has not yet bitten. As Q falls toward Q_critical (the level at which scarcity becomes economically visible) the suppression term grows and achieved S is pulled below S_base: the substitutes that low-price abundance failed to call forth are not ready when depletion forces the issue. This is the mechanism behind "stranded asset risk" — industries that extracted too fast kept prices low long enough to delay substitute development, and so face a lower achieved S_max (a larger 1−S foreclosure weight) exactly when substitutes are most needed.
**Reasoning:** Restores sign-consistency with the algebra while preserving the intended stranded-asset economics, which the formula actually encodes.

---

## 3 — §9.5/§9.6 convergence narrative ordering contradicts the table (ledger B6)

**Loc:** line 3250.
**Current:** "…the Real Options model produces **systematically lower** estimates… the RCV model produces the **highest** estimates…"
**Error (verified against the table, columns = Damage Function | Real Options | RCV):**
| Case | DF | Real Options | RCV |
|---|---|---|---|
| McDowell | 33–122 | 45–89 | 67–134 |
| Deepwater | 15–17 | **12–21** | 16–19 |
| Libby | 55–82 | 48–76 | 61–91 |
| Baotou | 12–35 | **18–48** | 22–41 |

Real Options is NOT systematically lowest (it carries the **highest** upper bound in Deepwater, 21×, and Baotou, 48×). RCV is NOT highest in Deepwater (21>19) or Baotou (48>41). Both ordering claims fail in 2 of 4 cases.
**Options:**
- (A) Replace the ordering sentence with the defensible claim: ranges overlap within one order of magnitude in every case; no model is uniformly highest or lowest. Keep the (separate, uncontradicted) "carbon term dominates the Damage Function IPG for fossil fuels."
- (B) Re-rank the table. (Rejected — numbers are owned elsewhere/sourced; only the narrative is wrong.)
**Recommendation:** A. Proposed replacement for the contradicted clause:
> The carbon term dominates the Damage Function IPG for fossil fuels. Across cases no single model is uniformly highest or lowest: the RCV model gives the highest estimates for McDowell and Libby, while the Real Options model reaches the highest upper bound for Deepwater and Baotou. The load-bearing regularity is the overlap within one order of magnitude (Empirical Observation 10.2), not a fixed cross-model ordering.
**Reasoning:** Matches the table; preserves the convergence point, which is the actual claim §9.5 needs.

---

## 4 — §3.1 Definition 1.3 `U ≥ P(t)` is dimensionally inconsistent (ledger B3)

**Loc:** line 371 (formula), 743 (prose echo).
**Current:** "Bounded below by market price: U(R, t, Q(t)) ≥ P(t) for all t ≥ t₀"
**Error:** In the RCV integrand {[1−S]·U + E}·D dt, U is a **flow** [$·res⁻¹·time⁻¹]; market price P(t) is a **stock** [$·res⁻¹]. The inequality compares a flow to a stock. Needs annualization.
**Options:**
- (A) `U(R, t, Q(t)) ≥ P(t)/H` with H = amortization/holding horizon (matches ledger).
- (B) `U(R, t, Q(t)) ≥ r·P(t)` — annualized user-cost (flow value of holding an asset priced P(t)); cleaner economics, ties to the discount rate already in the model.
**Recommendation:** B (with a half-line gloss), falling back to A if you prefer the ledger's literal form.
Proposed 371: "Bounded below by the annualized market price: U(R, t, Q(t)) ≥ r·P(t) for all t ≥ t₀ (the stock price P(t) is converted to a per-period flow so the bound is dimensionally consistent with U)."
Proposed 743 echo: "…It is bounded below by the annualized (per-period) market price and rises as Q declines."
**Reasoning:** Fixes the flow-vs-stock mismatch the cleanest way; r is already defined in the model, so no new symbol unless you prefer H.

---

## 5 — Theorem 10.1b "Proof" restates premise P3 as its conclusion; statement over-scoped (ledger B1 + B2)

**Loc:** title 3306; statement 3362; "Proof." 3366; refs 248, 762, 3383, 3389, 3692; "the theorem" common-noun uses 3377, 3389; ∎ at 3371.
**Error (B1):** The Statement to prove is "aggregate B < aggregate RCV ⇒ CS>0." Premise **P3** already asserts "aggregate B is empirically less than aggregate RCV." The "Proof" therefore restates an empirical premise as its conclusion — it is not a derivation from primitive premises. (Exactly the 10.2 situation, which the document already relabeled Theorem → **Empirical Observation 10.2**.)
**Error (B2):** Statement (3362) claims "in **any jurisdiction** observed under current institutions," but the proof delivers only "the jurisdictions empirically validated in §11" (3371) — scope of statement exceeds scope of support.
**Options:**
- (A) Relabel **Theorem 10.1b → Empirical Observation 10.1b** throughout; "Proof." → "Supporting argument"; drop the ∎; add a short categorization note mirroring 10.2; narrow "any jurisdiction" → "the §11-characterized jurisdictions." Propagate the label to inline refs (248 TOC, 762, 3383, 3389, 3692) and change common-noun "the theorem"→"the observation"/"this result" (3377, 3389).
- (B) Keep "Theorem," fix only the circular proof + scope. (Rejected — the 10.2 precedent and the categorically-empirical claim form make relabel the consistent move.)
**Recommendation:** A. Specifics:
- 3306 title → `Empirical Observation 10.1b (Structural Cost Severance under Current Institutions)`
- 3362 → "…for non-renewable extraction R at time t₀ across **the §11-characterized jurisdictions** observed under current institutions, aggregate B(R, t₀) < aggregate RCV(R, t₀). Therefore by Theorem 10.1a, CS(R, t₀) > 0."
- 3366 `Proof.` → `Supporting argument.`; remove the ∎ at 3371.
- Add after 3371 a categorization note paralleling 10.2: "Presented as an empirical observation rather than a theorem: its load-bearing premise (P3, B < RCV across current institutions) is itself the empirical regularity, established by the §11 cases, not derived from primitive premises. The categorization difference is honored in the labeling, matching Empirical Observation 10.2."
- 762, 3383, 3389, 3692 "Theorem 10.1b" → "Empirical Observation 10.1b"; 248 TOC "10.1b" → "Empirical Observation 10.1b"; 3377/3389 common-noun "the theorem"/"theorem's domain" → "the observation"/"its domain."
**Reasoning:** Removes a genuine circularity, aligns label with claim form and with the existing 10.2 precedent, and right-sizes the universal-quantifier claim to the evidence.
**Note:** leaves Theorem 10.1a (3265, genuinely derivational from the CS identity) and its ∎ at 3303 untouched.

---

## 6 — §3.5 "α-dominance sensitivity finding" is a property of the chosen functional form, not an empirical finding (ledger B7)

**Loc:** header 922; implication 1029–1033.
**Current header:** "Sensitivity finding (cross-case dominance map):"
**Current implication:** "Earth-bound civilization-scale extractions cluster in α-dominance regime. The real debate about RCV for those cases is a debate about **irreversibility** — not about discount rates, scarcity, or option-value."
**Error:** The α-dominance result follows by construction from the posited `irreversibility_premium(α) = 1/(1−α)^β`, which diverges as α→1. In the high-α regime the α term must dominate the RCV_M3 product — that is a property of the chosen form, not an independent empirical finding. "Sensitivity finding" overclaims empirical content.
**Options:**
- (A) Reframe header → "Property of the chosen functional form (cross-case dominance map):" and soften the implication to acknowledge it follows from the posited form. (Does NOT touch the M3 formula structure — that's the M3 Path-B session's domain.)
- (B) Leave as-is. (Rejected — hostile-reviewer-exposed overclaim.)
**Recommendation:** A. Proposed:
- 922 → "**Property of the chosen functional form (cross-case dominance map):**"
- 1029–1033 → "Given the posited 1/(1−α)^β irreversibility premium, earth-bound civilization-scale extractions (high α) fall by construction into the regime where the irreversibility parameter dominates the RCV_M3 product. The implication the framework draws — that for those cases the substantive debate is about **irreversibility** rather than discount rates, scarcity, or option-value — therefore follows from the chosen functional form and should be read as a structural property of the model, not an independent empirical finding. So read, it is tractably empirical; aligned with the Asymmetric Regret Rule (§8.2) and the climate-tipping-point + biodiversity-collapse + cultural-loss literatures."
**Reasoning:** Keeps the (useful) regime map and the irreversibility emphasis, but stops it being read as a discovered fact about the world rather than a consequence of the modeling choice. Formula structure untouched.

---

## 7 — §14.6 Daly inversion (ledger D3)

**Loc:** line 6609.
**Current:** "Where Daly argues normatively that **S_max must equal 1** for strong sustainability to be achievable, RCV asks empirically: what is S_max for each resource class?…"
**Error:** Inverts Daly. Daly's strong-sustainability claim is the opposite: for critical natural capital there is **no adequate substitute (S_max < 1)**, therefore one must **maintain the physical stock** rather than rely on substitution. The text turns the premise into "S_max must equal 1." (Line 6606 already states the correct version — internal inconsistency.)
**Options:**
- (A) Reframe so Daly's claim is S_max < 1 for critical natural capital → maintain the physical stock.
- (B) Leave. (Rejected — misattributes the cited author's logic.)
**Recommendation:** A. Proposed 6609:
> RCV relationship: The RCV model operationalizes Daly's strong-sustainability criterion mathematically. Daly's claim, in the framework's terms, is that for critical natural capital S_max < 1 — there is no adequate substitute — so strong sustainability cannot be achieved by substituting capital for the natural stock and instead requires maintaining the physical stock itself. RCV asks empirically: what is S_max for each resource class? For high-existential-substitutability-gap resources (rare earths, platinum group metals, phosphorus) S_max < 1, confirming Daly's premise — substitution alone cannot meet the criterion. The RCV model quantifies the resulting cost, complementing Daly's qualitative argument with a measurable framework.
**Reasoning:** Restores Daly's actual logic (maintain the stock *because* S_max<1), removes the inversion, keeps the RCV operationalization. Daly already in the bibliography.

---

## 8 — §3.5 Solow misattribution (ledger D4)

**Loc:** line 917.
**Current:** "Adjacent intergenerational-equity lineage. **Solow 1956 *Quarterly Journal of Economics*** + Bergson 1938 … on long-horizon utility aggregation under intergenerational discounting…"
**Error:** Solow 1956 QJE is the growth-accounting paper ("A Contribution to the Theory of Economic Growth"), not about intergenerational equity. The intergenerational-equity + exhaustible-resources paper — which the "intergenerational-equity lineage" framing wants — is **Solow 1974, *Review of Economic Studies*** ("Intergenerational Equity and Exhaustible Resources"). Both are already in the bibliography (7981 Solow 1956; 7984 Solow 1974); 1974 is already cited correctly elsewhere (1282, 3801, 6710, 6723, 7163).
**Options:**
- (A) "Solow 1956 *Quarterly Journal of Economics*" → "Solow 1974 *Review of Economic Studies*" (keep Bergson 1938).
- (B) Leave. (Rejected — wrong paper for the point being made.)
**Recommendation:** A.
**Reasoning:** Pure citation correction; target already in bib; aligns the cite with the lineage being claimed.
**Flag for Session A (bib consolidation):** line 917 is the ONLY in-text use of Solow 1956; after this swap the Solow 1956 bib entry (7981) is orphaned. Bib cleanup is Session A's domain — flagged, not touched here.

---

### Ratification ask
All eight are clean internal-correctness fixes (no external sourcing). Recommend ratifying all with the recommended option. Batch "yes to all recommendations" is fine, or call out any you want to alter (e.g. item 4 A-vs-B, item 5 relabel-vs-minimal). On ratification I apply, verify, and commit to the branch only (no merge to main).
