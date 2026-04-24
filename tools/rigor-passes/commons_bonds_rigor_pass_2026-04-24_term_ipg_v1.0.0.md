# Commons Bonds — Full Rigor Pass: Intergenerational Pricing Gap (IPG)

**Version:** 1.0.0
**Date:** 2026-04-24
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — full 12-module suite including M12 Intellectual Honesty / Prior-Art Audit + §22 Path Comparison Mode + §22.4 goals alignment + all 6 Working Principles.
**Scope:** Ring-2 individual rigor pass on Intergenerational Pricing Gap (IPG = RCV / market_price). Meta-pass §12.1 item 10 flagged for individual rigor with option to demote to Ring 3. Tests Ring placement + distinctness from CS + load-bearing contribution.
**Status:** rigor pass executed 2026-04-24; pending author ratification.
**Author:** Chris Winn

**Applies Working Principles:**
- **Principle #1** (effort-to-repair not rigor argument).
- **Principle #1 Corollary B** (usage frequency alone not a rigor argument for retention).
- **Principle #2** (audit concept not phrase) — 97 total refs audited; ~15 in active chapter drafts/guidance + WS12 decision doc.
- **Principle #3** (derivation check — is IPG a distinct concept or derivable from components?).
- **Principle #6** (intellectual-honesty / M12 audit).

---

## §1. Executive summary

**RECOMMENDED: Option A — CONFIRM Ring 2 (internal load-bearing).** IPG earns its place despite being a derived quantity (ratio RCV / market_price) because it measures a DISTINCT gap from CS — the MARKET-PRICING gap vs CS's ACCOUNTABILITY gap — and because the framework makes a substantive empirical claim anchored in IPG (IPG ≫ 1 universally across tested cases).

**The decisive distinctness finding:** IPG and CS measure different phenomena even though both are "gap" quantities.

| Quantity | Measures | Uses | What it diagnoses |
|---|---|---|---|
| **CS = RCV − B** | Accountability gap (absolute-dollar) | RCV + B (Accountability Bond — dollars forced onto extractor via ALL accountability instruments) | How much true cost is not being internalized by accountability mechanisms |
| **IPG = RCV / market_price** | Market-pricing gap (ratio / factor) | RCV + market transaction price | How much markets underprice extraction at the POINT of transaction |

**Norway example illustrates why both matter:**
- Norway's CS may be small (sovereign wealth fund captures B ≈ RCV intergenerationally).
- Norway's IPG for oil may still be large (oil transacts at market prices that don't reflect its full intergenerational cost — the sovereign wealth fund captures the gap POST-transaction, not AT transaction).

**These are complementary diagnostics, not redundant.**

**Key distinction from the CSG retirement precedent:** CSG was retired as a derived scalar from framework primitives (S_max(industrial) − S_max(existential) — both S-derivations; internal-to-framework derivation). IPG combines a framework primitive (RCV) with an EXTERNAL reference (market_price, not framework-defined). Derivations that compose with ambient reality (external references) carry substantive empirical content that pure internal derivations don't — they position the framework against external reality.

**M12 classification:** Independent framework-specific composite diagnostic. "Intergenerational pricing gap" as a specific phrase was not found in the literature (per earlier audit commit `f643e59` + refresh below). The intergenerational-discounting literature (Ramsey formula; Stern; declining discount rate debate) is adjacent but doesn't use this specific ratio form against current market price.

**Options tested:**
- **A — CONFIRM Ring 2** (distinct-from-CS diagnostic; framework-specific empirical anchor). **RECOMMENDED.**
- **B — DEMOTE to prose** (describe in Ch 6 convergence table without named term). REJECTED — loses the empirical-anchor function + compression for 15+ active refs.
- **C — RETIRE entirely** (convergence table shows RCV + market price separately; reader computes ratio). REJECTED — "IPG ≫ 1 universally" is a substantive framework finding that deserves a handle.
- **D — RENAME.** Candidates: "Market-Pricing Gap," "Underpricing Factor," "Intergenerational Undercount Ratio." REJECTED — "Intergenerational" is load-bearing (specifies WHICH gap; differentiates from accounting-pricing gaps + other pricing-failure framings).

---

## §2. The question under test

### §2.1 V2 definition

> *"Intergenerational Pricing Gap (IPG): The ratio RCV/market price; the factor by which markets underprice extraction. Measures how much cost severance has occurred in numerical terms. IPG = 33 means the market price covers approximately 3% of the true intergenerational cost. All empirical cases tested yield IPG ≫ 1."*

### §2.2 Framework role

IPG is used in:
- **Ch 2 guidance + Ch 2 draft** — 2 refs. McDowell coal's IPG as demonstration.
- **Ch 5 guidance (Accountability Gap)** — 2 refs. IPG as the scalar form of the gap.
- **Ch 6 guidance + Ch 6 draft** — 6 refs. Convergence table presentation (4 approaches converge on IPG ≫ 1).
- **Ch 8 draft** — 1 ref. Civilizational-scale application.
- **Ch 7 guidance** — 1 ref. Asteroid-miner scenario (IPG in hypothetical extraction contexts).
- **3 case studies** — Deepwater (2), Libby (2), Appalachian coal (1). IPG empirically computed for each.
- **WS12 decision doc** — 9 refs. Dedicated "IPG data table for reconciliation" workstream. Strong signal of load-bearing.

Total in active framework content: **~15 refs + one dedicated decision doc.**

### §2.3 Options

As in §1.

### §2.4 Sub-claims

**Option A (confirm Ring 2):**
- SC-A1: IPG measures market-pricing gap (distinct from CS's accountability-pricing gap).
- SC-A2: Framework's empirical finding ("IPG ≫ 1 universally across cases") needs a named-anchor.
- SC-A3: Convergence-table pedagogy in Ch 6 depends on IPG as compressed scalar.
- SC-A4: Derivation test: combines framework primitive (RCV) with external reference (market price) — substantive empirical content, not pure internal derivation.

**Option B (demote to prose):**
- SC-B1: "Ratio of true cost to market price" is prose-expressible.
- SC-B2: Reduces vocabulary footprint.

**Option C (retire):**
- SC-C1: Convergence table could show RCV + market_price columns separately.
- SC-C2: Reader computes ratio.

**Option D (rename):**
- SC-D1: "Intergenerational" might be redundant with other framework terms.
- SC-D2: Shorter alternatives compress better.

### §2.5 Falsifiers

**Option A falsified if:**
- IPG collapses into CS under closer analysis (same thing, different form).
- The "IPG ≫ 1 universally" finding proves fragile or insufficiently precise.
- Convergence-table pedagogy survives without IPG as named term.

**Option C falsified if:**
- "IPG ≫ 1" empirical finding is load-bearing for framework's adoption argument AND can't be expressed without the named term.
- Case-study prose shows material readability loss without IPG.

---

## §3. Principle #3 derivation + distinctness check (decisive module)

### §3.1 Is IPG distinct from CS?

**CS = RCV − B** (absolute-dollar accountability gap)
**IPG = RCV / market_price** (ratio market-pricing gap)

Key compositional difference:
- **CS uses B** (Accountability Bond — sum of accountability-instrument dollars; framework primitive).
- **IPG uses market_price** (transaction price — external empirical reference).

These are different quantities in the real world:
- A good's market price reflects supply/demand/production economics at the point of sale.
- The accountability bond (B) reflects regulatory + policy + insurance + voluntary-remediation mechanisms that internalize cost.

These can diverge substantially:
- **Norway oil:** market_price ≈ ~$80/barrel (commodity market). B ≈ RCV (sovereign wealth fund captures full intergenerational value via post-transaction transfer). So CS ≈ 0 but IPG = RCV/$80 could be large if RCV includes intergenerational carbon damage + biosphere costs + etc.
- **US coal ~2015:** market_price ≈ $50/ton at mine mouth. B ≈ minimal (weak reclamation bonds, no carbon price, limited community-transition funds). So CS is large AND IPG is large — different diagnostics both pointing at the gap from different angles.

**Verdict:** IPG and CS measure different gaps. Distinctness confirmed.

### §3.2 Is IPG a pure derivation (like CSG was)?

CSG's retirement (commit `a9acf8e`) was on parsimony grounds: CSG was a derivation entirely from framework primitives (S_max internal × 2). The framework doesn't name internal-to-framework derivations (same reasoning that doesn't name S(t)−S(t−1)).

**IPG is different structurally:** it composes a framework primitive (RCV) with an EXTERNAL reference (market_price, not framework-defined). This is not internal-to-framework derivation — it's positioning the framework AGAINST external market reality.

Pattern in the framework:
- **Internal derivations** (not named): S_max, S(t)−S(t−1), sum-of-Cᵢ-in-subset, etc.
- **Framework-primitive-composed-with-external-reference** (earns naming where load-bearing): IPG (RCV vs market price); the "accountability gap" (B vs RCV); Norway's "fund growth rate" (fund-value vs extraction volume).

This distinction surfaces a sub-corollary to the parsimony principle: **compositions with external reality are different from internal derivations and can earn named-object status when load-bearing.**

### §3.3 Verdict on Principle #3

IPG PASSES derivation check (not a pure internal derivation; composes framework primitive with external empirical reference). Distinct from CS. Framework-specific empirical anchor.

---

## §4. M12 — Intellectual honesty / Prior-art audit

### §4.1 Exact-phrase search

"Intergenerational pricing gap" as a specific phrase — not found in adjacent economics literature per earlier audit (commit `f643e59`, research batch 2026-04-24).

### §4.2 Concept-level search

Adjacent frameworks for "market underprices intergenerational costs":

- **Ramsey social discount rate formula** (Ramsey 1928; extensively developed). Addresses discount-rate calibration but not a direct ratio of true cost to market price.
- **Stern Review** (Stern 2007). Argues low discount rate for intergenerational calibration; describes market failure qualitatively.
- **Nordhaus DICE / social cost of carbon** (Nordhaus & Boyer 2000). Social-cost-of-carbon vs market carbon price is analogous but single-externality-focused (not general-case).
- **Declining discount rate literature** (Weitzman; Gollier; Portney & Weyant). Addresses discount-rate structure, not ratio diagnostic.
- **Gowdy & Krall** ecological-economics literature on long-term-value pricing.

**Finding:** intergenerational-pricing-gap CONCEPT is adjacent-established (market underprices intergenerational costs is well-known). SPECIFIC FRAMING as named ratio RCV / market_price is framework-specific.

### §4.3 Classification

**Independent specialization / framework-specific diagnostic composite.** Specific form (ratio; intergenerational framing; uses RCV as numerator) is framework-novel; underlying CONCEPT (markets underprice intergenerational costs) is established.

### §4.4 Required action per M12 action ladder

**Level 1 — Tech Appendix methodological footnote.** Cite Ramsey + Stern + Nordhaus + declining-discount-rate literature as adjacent-established work; position IPG as framework-specific diagnostic composite with RCV-as-numerator.

---

## §5. The "IPG ≫ 1 universally" empirical finding (load-bearing rigor question)

The v2 definition says *"All empirical cases tested yield IPG ≫ 1."* This is a substantive framework claim — that every extraction case the framework has tested shows market prices systematically below true intergenerational cost.

Is this finding:
(a) A strong empirical claim that requires data rigor? OR
(b) A framework-design artifact (since RCV is built to capture intergenerational costs, and market prices typically don't, the framework's architecture guarantees IPG ≫ 1)?

**Rigor-honest answer: partly (b).** Because RCV is defined to include intergenerational foreclosure + externality tails that markets don't price, IPG ≫ 1 is largely inevitable by construction for extraction cases. The interesting empirical question is the MAGNITUDE (IPG = 5? 33? 100?), not the direction.

**Implication for the Tech Appendix:** the IPG ≫ 1 claim should be framed as "by construction, the framework expects IPG > 1 for extraction cases; the empirical work quantifies the MAGNITUDE." Presenting it as an open empirical finding would be overclaiming — it's more of an orientation plus quantitative calibration.

This is worth noting as an epistemic-honesty sub-finding for Ch 6 convergence-table framing.

---

## §6. M1–M11 abbreviated results

- **M1 CORE:** IPG is not CORE — RCV is. IPG is derived. But framework's empirical presentation depends on it. PASS (appropriate scope).
- **M2 Case study:** Every case computes IPG (McDowell, Deepwater, Libby, etc.). Convergence-table pattern depends on it.
- **M3 Book content:** 15+ refs in active drafts + dedicated decision doc (WS12). Load-bearing.
- **M4 Craft:** Ratio compresses well ("IPG = 33" reads cleanly in prose). Accounting register preserved.
- **M5 Dinner-table:** "The factor by which markets underprice extraction" parses for non-expert. IPG = 33 is memorable.
- **M6 Academic:** Tech Appendix citation of Ramsey + Stern + Nordhaus positions academically. Magnitude-not-direction framing (per §5) honest.
- **M7 Originality:** Specific ratio form + RCV-as-numerator is framework-specific. Contribution preserved.
- **M8 Long-term:** Convergence-table pedagogy + cross-case comparison capability supports durability. IPG gives readers a single-number handle across cases.
- **M9 Risk:** Minor — "IPG ≫ 1 universally" could be read as data claim rather than construction claim. Mitigable via §5 framing.
- **M10 Publishing:** Neutral. Convergence table is editorially pleasing (numerical center of gravity for Ch 6).
- **M11 Critic:** *"Isn't this just the social-cost-of-carbon gap renamed for extraction broadly?"* — Response: structurally parallel to SCC gap but generalized (not single-externality; uses RCV integrand with abundance-inversion discipline; applied to any extraction). Survives.

**§22.4 alignment:** Option A positive on Primary Goals (academic reception + success criterion — IPG gives empirical anchor for cross-case comparability).

---

## §7. Verdict

**OPTION A — CONFIRM Ring 2.** IPG earns Ring-2 internal-load-bearing status as framework-specific market-pricing-gap diagnostic distinct from CS's accountability-pricing-gap diagnostic.

### §7.1 What changes

- **Terms Index:** new CURRENT Ring-2 record for IPG (full provenance + M12 classification + distinction-from-CS note + "IPG ≫ 1 by construction" epistemic-honesty framing).
- **Glossary v3:** keep v2 definition; update "All empirical cases tested yield IPG ≫ 1" to clarify "by construction for extraction cases; empirical work quantifies magnitude."
- **Tech Appendix §L:** methodological footnote citing Ramsey + Stern + Nordhaus + declining-discount literature.
- **Ch 6 convergence-table framing:** emphasize MAGNITUDE quantification, not direction ("IPG ≫ 1 is framework-architectural; magnitude is the empirical finding").

### §7.2 What doesn't change

- CS = RCV − B equation — unchanged.
- RCV definition — unchanged.
- Case studies' IPG computations — unchanged.
- Convergence table structure — unchanged.

### §7.3 Sub-finding captured (parsimony principle refinement)

This pass establishes a corollary to the parsimony principle:
- **Internal derivations** (composed entirely from framework primitives): not named (per CSG retirement precedent — S_max, S(t)−S(t−1)).
- **External-composites** (framework primitive composed with external empirical reference): can earn named-object status when load-bearing (IPG example).

This refinement is worth capturing for future rigor passes evaluating derived quantities. Added to Terms Index IPG record's notes + flagged for possible Principle #6 sub-corollary promotion if pattern repeats.

---

## §8. Term Provenance Record

### Intergenerational Pricing Gap (IPG)

**Working definition:** Ratio IPG = RCV / market_price — the factor by which markets underprice extraction at the point of transaction. "IPG = 33" means the market price covers approximately 3% of the true intergenerational cost captured in RCV. Framework-specific market-pricing-gap diagnostic, distinct from Cost Severance (CS = RCV − B, accountability-pricing-gap diagnostic). By construction IPG > 1 for extraction cases (RCV includes intergenerational costs markets don't price); empirical work quantifies MAGNITUDE across cases.

**Status:** `CURRENT` at Ring 2 (recommended by this pass; pending author ratification).

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 + §12.1 item 10 (commit `46600bc`) — Ring-2 classification with flag for individual rigor to test demote-to-Ring-3 alternative.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_ipg_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) recommended. Principle-#3 derivation check PASSES (distinct from CS; external-composite not pure internal derivation). M12 classification: independent specialization / framework-specific diagnostic composite.

**M12 classification:** Independent specialization of adjacent intergenerational-pricing literature. Specific phrase "Intergenerational Pricing Gap" not found in prior literature. Concept (markets underprice intergenerational costs) adjacent-established in Ramsey / Stern / Nordhaus / declining-discount-rate work; specific ratio form with RCV-as-numerator is framework-specific.

**M12 citations (recommended for Tech Appendix §L methodological footnote):**
- Ramsey, Frank P. (1928). "A Mathematical Theory of Saving." (Foundational intergenerational-discount-rate framework.)
- Stern, Nicholas (2007). *The Stern Review* — already in bibliography for Externality Tail.
- Nordhaus, William D. (various) — already in bibliography for Externality Tail.
- Declining discount rate literature (Weitzman, Gollier, Portney & Weyant) — could be added if Tech Appendix reaches that depth.

**Why Ring 2 (not Ring 3 demote):**
- Distinct diagnostic from CS (measures market-pricing gap, not accountability-pricing gap).
- 15+ active chapter/guidance refs + dedicated WS12 decision doc + case-study computation across 3+ cases.
- Convergence-table pedagogy (Ch 6) depends on it.
- "IPG ≫ 1 universally" is a framework-architectural claim that deserves a handle.

**Why NOT demoted/retired:**
- Load-bearing for Ch 6 + case studies.
- Distinct content from CS (uses market_price not B).
- Compresses "factor by which markets underprice" into a single number.

**Distinguishing from CS:**
- CS uses B (Accountability Bond — all accountability-instrument dollars; framework primitive).
- IPG uses market_price (transaction price — external empirical reference).
- These can diverge: Norway has small CS (sovereign wealth fund captures B ≈ RCV) but potentially large IPG (oil market price below true intergenerational cost). Both diagnostics warranted.

**Parsimony sub-corollary surfaced:**
- Internal derivations (composed from framework primitives only): not named.
- External-composites (framework primitive composed with external reference): can earn named status when load-bearing. IPG is the canonical example.

**Epistemic-honesty note (for Ch 6 framing):**
The "IPG ≫ 1 universally" claim is PARTLY by construction — RCV includes intergenerational costs markets don't price, so IPG > 1 is architectural. The empirical work quantifies MAGNITUDE (IPG = 5? 33? 100?) not direction. Ch 6 convergence-table framing should reflect this.

**Depends on:**
- RCV definition (numerator).
- Market-price measurement (denominator — external empirical reference).
- Cost Severance (IPG is complementary diagnostic, not synonym).

**Pairs with:**
- CS = RCV − B (complementary gap diagnostic — different denominator, different diagnostic role).
- RCV (direct component).
- Accountability-gap narrative (IPG quantifies WHAT the gap looks like at market-transaction time; CS quantifies what accountability instruments cover post-transaction).

**Staleness triggers:**
- RCV definition restructured.
- Framework develops a more precise pricing-gap diagnostic that displaces IPG.
- Empirical work reveals "IPG ≫ 1" is not universal (would change both the framework's architectural claim and IPG's role).

**Commit trail:**
- Individual rigor pass: this commit.
- Ratification + Terms Index record: pending.

**Notes:**
- Convergence-table pedagogy in Ch 6: 4 approaches converge on IPG ≫ 1. This is the chapter's numerical center of gravity.
- IPG = 33 (McDowell coal) is the framework's canonical case-study computation. Readers remember "market covers 3%; framework says the real cost is 33× that" as the framework's core empirical claim-compression.
- WS12 IPG data table (alignment/decisions/ws12-ipg-data-table-for-reconciliation.md) is load-bearing for case-study cross-comparison.

---

## §9. Author-ratified resolutions

**Ratified 2026-04-24 by Chris Winn — Option A (CONFIRM Ring 2).** IPG earns Ring-2 internal-load-bearing status as framework-specific market-pricing-gap diagnostic distinct from CS's accountability-pricing-gap diagnostic. Principle-#3 derivation check PASSES (not a pure internal derivation; composes framework primitive RCV with external empirical reference market_price). M12 classification: independent specialization of adjacent intergenerational-pricing literature (Ramsey 1928, Stern 2007, Nordhaus DICE).

**Ratification also surfaces new parsimony-principle corollary (worth capturing in Principle #6):**
- **Internal derivations** (composed from framework primitives only): NOT named per parsimony discipline (CSG retirement precedent — S_max, S(t)−S(t−1)).
- **External-composites** (framework primitive composed with external empirical reference): CAN earn named-object status when load-bearing. IPG canonical example (RCV × market_price).
- Rationale: compositions with external reality position the framework AGAINST empirical reality — substantive content that internal derivations don't carry.

**Ch 6 + Tech Appendix framing update ratified:**
- "IPG ≫ 1 universally" reframed: architectural (by construction) + empirical (magnitude calibration). Prevents overclaiming.
- Tech Appendix §L footnote adds Ramsey/Stern/Nordhaus/declining-discount citations positioning IPG as framework-specific diagnostic composite.

---

## §10. Rerun gate

Rerun if:
- RCV definition restructures.
- "IPG ≫ 1 universally" empirical claim is revisited and found insufficient.
- A replacement diagnostic is developed that compresses market-pricing-gap more effectively.

---

*End of individual rigor pass v1.0.0. Option A (CONFIRM Ring 2) recommended. IPG earns its place as framework-specific market-pricing-gap diagnostic distinct from CS's accountability-pricing-gap diagnostic. External-composite exception to parsimony principle surfaced. Pending author ratification.*
