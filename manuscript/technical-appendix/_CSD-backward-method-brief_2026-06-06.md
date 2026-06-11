# TA Backward Part — "Computing CSD: The Restitution Direction" — TENTATIVE DRAFTING BRIEF (2026-06-06)

**Status:** TENTATIVE. Input for a dedicated session to VALIDATE and refine into its own brief, then draft. Ratified at the *architecture* level (author, 2026-06-06): add a backward CSD computation method + reef worked case + coercion-deferral note to the TA as a NEW standalone Part (graft, NOT a TA whole-cloth). Section-level beats below are recommendations to validate, not ratified text.

## 0. What this Part is / is not
- **IS:** a new additive Part formalizing the backward CSD computation method (the twin of the forward RCV "three ways"), a fully worked case (the Chesapeake reef = the backward analog of Ch8's $510/ton coal), and the explicit coercion-deferral boundary.
- **IS NOT:** a whole-cloth redraft of the TA. The verified core stays intact (CS = RCV − B; B = B₁ + B₂; the theorem structure; the 18-case apparatus; §11.7 CSD–RCV correlation). This Part bolts on.
- **WHY:** the forward instrument has a full worked number (Ch8 coal). The backward instrument (CSD / B₁ Restitution Bond, already named + grounded in TA §2/§4) has a formal definition but no worked *computation method* and no worked *case*. This closes the book's single biggest structural loop (per `_book-coherence-map` "Loops to close": "BACKWARD-INSTRUMENT EMPIRICAL CASE NEVER FULLY RUN").

## 1. The conceptual reversal (forward → backward)
The forward apparatus exists to handle UNCERTAINTY about the future: option value, declining (Weitzman) discount rates, the substitutability FUNCTION S — all because future generations cannot bid and the future is unknown. Backward, the future has ARRIVED:
- value is realized (you know what was taken and what was lost),
- the cost-bearers are known (not hypothetical future people),
- the substitutability question is ANSWERED — the substitutability *function* collapses to a substitutability *outcome* (for the reef: no substitute emerged).

So the backward method uses realized facts + observed counterfactuals, not forecasts. This is the core simplification and the source of the backward direction's greater empirical defensibility.

## 2. The three ways, reversed — WITH the audit correction (CRITICAL — validate first)
The TA rigor audit (branch `claude/ta-rigor-audit-260606-f537b4`, finding **E12**, PROPOSED) flags that the forward "three independent methods" framing is an overclaim: **M2 (Norway revealed-preference) is the realized-B comparator in CS = RCV − B, not a third independent RCV estimator.** That directly shapes the reversal. Corrected backward structure:

- **M1 (bottom-up / replacement) → RESTORATION COST.** A CSD estimator (cost-to-cure). The reef's worked method (foreclosed AREA × installed restoration cost/acre). Clean; arguably cleaner backward than forward.
- **M3 (scarcity-adjusted option value) → REALIZED FORECLOSURE.** A CSD estimator (compensation / loss). Collapse the forward distribution-of-futures to the single REALIZED path; price what the commons would have produced absent destruction, using the now-OBSERVED scarcity outcome. Needs a defensible counterfactual baseline (comparator reefs + documented decline). The least-clean method — validate.
- **M2 (revealed-preference) → REALIZED B₁ COMPARATOR (NOT a CSD estimator).** Per E12, M2 reverses to "what restitution is actually being POSTED" — the public-dime restoration already happening. CS = CSD − B₁(public) = the severance still borne by the public; the Restitution Bond shifts B₁ onto the beneficiary. M2 is the benchmark, not a third estimate.
- **Disgorgement / realized extracted value (the Darling take) → a SEPARATE gain-based anchor.** Not RCV/CSD, not B; the unjust-enrichment measure. Using it as an alternative CSD anchor (restitution-law "greater of") is a normative choice (see §4).

The session must VALIDATE this mapping against the actual forward §3 "Three Ways" definitions + the E12 finding, and resolve M2's reversal cleanly. This is the single highest-risk design point.

## 3. Convergence → divergence (a feature, not a bug)
Forward, the methods triangulate ONE RCV (Campbell-Fiske convergence = the value is real). Backward, M1 (restoration) and M3 (realized foreclosure) measure DISTINCT quantities and may diverge; disgorgement is distinct again. They map onto the three canonical restitution/damages measures:
- restoration / reinstatement (M1),
- compensation for loss (M3),
- disgorgement of gain (extracted value).

The SPREAD between them is informative (a large gap between gain and restoration cost is a measure of irreplaceability). This grounds the backward instrument in established restitution & damages law — strengthening the existing Darity-Mullen 2020 + Hicks 1932 lineage rather than inventing a novel apparatus.

## 4. Design decisions (recommendations — validate)
1. **Compounding.** Realized historical flows (esp. the disgorgement / extracted-value measure) compounded to present value at a DISCLOSED real rate — adopt the Ch5 net-Social-Security precedent for consistency. Restoration cost (M1) is priced at present cost, so compounding bears mainly on the gain measure.
2. **Bond-anchoring rule when the three diverge.** Anchor on RESTORATION-WHERE-FEASIBLE (M1) over the "greater of" (disgorgement vs compensation): it funds a fix rather than litigating a transfer, and sidesteps the political fight the "greater of" invites. (The reef's ratified methodology already does this.)
3. **Irreplaceable residual.** Price PARTIAL restoration + NAME the unpriceable remainder explicitly (consistent with Ch7's Europa / non-denominable handling), rather than forcing a number. For the reef the residual is small (restoration largely feasible); the formula must still carry a residual term for cases where it is not. (Resolve D3 here: Daly's strong-sustainability claim is S_max < 1 for critical natural capital → maintain the stock — the correct grounding for the residual term.)

## 5. The worked case — the Chesapeake reef (the backward Ch8-coal analog)
Source: `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md` (5-agent research result, methodology-locked).
- **Methodology:** foreclosed reef AREA × realized installed restoration cost/acre; the bond FUNDS RESTORATION (paid into the reef, not cash to people).
- **Foreclosed extent:** 2,738 acres (James River high-quality oyster-rock lost 1910→1981: 7,047 → 4,309 ac, −38.9%; Schulte 2017, *Frontiers in Marine Science* 4:127, citing Moore 1910 / Haven et al. 1981).
- **Installed restoration cost/acre + the three postures:**
  - $7,300/ac (Great Wicomico realized) → **FLOOR ≈ $20M**.
  - $13,500/ac (documented light-shell/stone construction, natural recruitment) → **≈ $37M** (better *headline* floor; method-explicit, primary-sourced).
  - $77,000/ac (bay-wide completed-program average, construction + seeding) → **≈ $211M** (robust central / cherry-pick-proof).
- **Darling 200,000-bushel shell-mountain = NARRATIVE anchor only, NOT the number** (raw shell is cheap ~$0.8–1.0M/peak-year; the full-run multiplication is the single biggest adversarial vulnerability).
- **KILLER FACT:** restoration is ALREADY happening on the public dime = the realized B₁ posted by the public = the severance made visible. Name the public payer.
- **CS = CSD − B₁ for the reef:** CSD (≈$20–37M restoration) − B₁ (currently public) = the severance the public bears; the Restitution Bond shifts B₁ to the extractor/beneficiary.

## 6. The coercion / standing boundary (place prominently)
The CSD formula is GENERAL — it can price any already-realized cost severance. The book WORKS only the reef: a domain where the author has community standing (Fox Hill / Hampton / J.S. Darling), the extraction is ecological, and there is no coercion to price. For coercion-based restitution (slavery → Darity-Mullen reparations economics), the framework ENABLES the computation and hands it to the affected communities and their economists; the author explicitly DECLINES to set that number. A STATED principled boundary, not an omission — "uses their language inside their typology, not against it." Honors the standing concern; stronger than a gesture. (This is the author's ratified posture, 2026-06-06.)

## 7. Lineage + audit fixes to fold in
- Add **Polanyi** (*The Great Transformation*, fictitious commodities) + **Fraser** (expropriation vs exploitation) to the TA lineage/bibliography (§14/§15) — closes the "biggest positioning gap"; matches the Ch5 prose exposition.
- Resolve the two CSD-relevant audit findings IN this Part: **E12** (§11.6 three-methods overclaim → state M2 = realized-B comparator) and **D3** (§14.6 Daly inversion → S_max < 1 for critical natural capital → maintain the stock).
- Connect to existing **§11.7** (CSD–RCV correlation hypothesis, Open Insight #19) and **§2** (Two-Instrument Architecture).

## 8. Seams
- **Ch3** names the reef as the backward/restitution ARCHETYPE + headline number ($20–37M floor; ~$211M robust-central), points here for the full math (SG-1).
- **Ch4** receives the FORWARD oyster question (Norway-style fund for the remaining living fishery; brief Chesapeake beat) (SG-2 / D9).
- **Ch5** (already names the backward instrument) + **Ch8** (forward worked number) echo.
- The compounding precedent ties to **Ch5**'s net-Social-Security calc.

## 9. Output + constraints
- A new standalone TA Part, grafted onto `TechnicalAppendix_v2.0.0`. CONFIRM the editable source (HTML vs a markdown source the HTML renders from) before drafting.
- Match the TA's existing formal register, notation (CS = RCV − B; B = B₁ + B₂; CSD; B₁), and theorem/section conventions.
- ADDITIVE ONLY. Do NOT regenerate the verified core.
- **v2 fallback (author-approved 2026-06-06):** if the graft reads clunky, or the parallel rigor audit surfaces enough that the TA needs broader rework, escalate to a NON-blind v2 TA draft (a v2 with inputs, explicitly not a blind whole-cloth). Default remains: graft this Part now.
