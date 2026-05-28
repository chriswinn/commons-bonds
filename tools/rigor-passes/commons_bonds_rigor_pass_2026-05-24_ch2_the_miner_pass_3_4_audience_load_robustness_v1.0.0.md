# Commons Bonds — Ch 2 *The Miner* — Stage 3 Pass 3.4 (Audience-Load Robustness)

**Date drafted:** 2026-05-24
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard); Ch 2 first-round-review explicit-gate cascade close
**Chapter file:** [`manuscript/chapters/Chapter__2_TheMiner.md`](../../manuscript/chapters/Chapter__2_TheMiner.md) — current post-Phase-C-ε state, **226 lines / ~5,367 words** (verified `wc -l` 2026-05-24).
**Discipline:** v3.1 Amendment B 5-pass + Amendment A two-class cascade. Pass 3.4 (audience-load robustness; adversarial / detractor character set; thread-pull synthesis verdict; verdict-floor EXCLUDE per character) per [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)".
**Mode:** audit-existing-prose (does NOT apply spot-fixes).
**Format model:** [Ch 9 Pass 3.4 §3 thread-pull synthesis](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) + [$100 Barrel Pass 3.4 light §4 aggregate](../../publishing/essays/100-barrel/rigor/pass-3-4-adversarial.md) + canonical [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) thread-pull canonical format.
**Status:** **RATIFIED 2026-05-25** (author ratified as-recommended; ROBUST verdict + RECORD-ONLY Phase C action accepted; T8 carries forward as Pass 3.5 restoration-site candidate; T4/T6 carry forward as Ch 7/Ch 8 Pass 3.4 forward-flags; T5+T8 carry forward as Stage 1c sibling-coherence-check potential). Per Amendment A explicit-gate cascade: this was the first time Ch 2's pre-publication-readiness adversarial robustness was tested per the v3.0 / v3.1 five-pass architecture. (The original 2026-05-13 audit operated under v2.0 Amendment B three-pass discipline; the 20-character set was a full-spectrum acceptance set with no adversarial-character partition.)

**Trigger context.** Author triggered Pass 3.4 explicitly 2026-05-24 ("build it now" trigger per v3.1 Amendment A explicit-gate cascade). Ch 2's review cycle has now completed:
- Pass 3.1 fact-check ✓ (commits `5bc6edb` + `3dcb15d`)
- Pass 3.2 voice-polish ✓ (commit `fa08c10`)
- Pass 3.3 audience-load acceptance LIGHT RE-FIRE **RATIFIED 2026-05-24** (commit `e39d4e4`; 19/20 INCLUDE + 1 NEUTRAL; READY AS-IS; two ↑ uplifts confirmed)
- Phase C α/β/γ/δ/ε applied (18 cumulative spot-fixes)
- `__Draft` dropped; chapter renamed `Chapter__2_TheMiner.md` (commit `4d860e8` 2026-05-21).

---

## §0. Source artifacts read + verification

1. [Chapter__2_TheMiner.md](../../manuscript/chapters/Chapter__2_TheMiner.md) — 226 lines (verified).
2. [Pass 3.3 LIGHT RE-FIRE RATIFIED artifact 2026-05-24](commons_bonds_rigor_pass_2026-05-24_ch2_the_miner_pass_3_3_light_refire_v1.0.0.md) — §3 per-character verdicts (19/20 INCLUDE; 1 NEUTRAL); §1 Phase C-δ + C-ε impact table; §5 Pass 3.4 future-session note.
3. [Original Ch 2 Pass 3 audience-load 2026-05-13 + appendices through 2026-05-21](commons_bonds_rigor_pass_2026-05-13_ch2_the_miner_stage3_audience_load_v1.0.0.md) — 20-character acceptance baseline + Tier 1 #4 (Coasean/welfare-economics reviewer) + Tier 2 #9 (Coasean/mainstream-econ skeptic) acceptance reads carried forward as adversarial-direction context.
4. [Ch 9 Pass 3.4 PROPOSED 2026-05-23](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) — chapter-scale Pass 3.4 format precedent + thread-pull synthesis table structure.
5. [$100 Barrel Pass 3.4 LIGHT RATIFIED 2026-05-23](../../publishing/essays/100-barrel/rigor/pass-3-4-adversarial.md) — aggregate verdict format precedent (ROBUST).
6. [Noema Pass 3.4 2026-05-22](../../publishing/essays/noema-commons-bonds/rigor/pass-3-4-adversarial.md) — CONDITIONALLY ROBUST format precedent.
7. [Stage-3 template](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)".
8. [Audience-pressure-test-construction](../drafting-templates/audience-pressure-test-construction.md) §3 adversarial character types.
9. [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 + Amendment A two-class cascade.
10. [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md) + [feedback_verify_stale_memory_claims.md](../memory/feedback_verify_stale_memory_claims.md).

**Verification (per `feedback_verify_stale_memory_claims.md`):**
- ✓ Chapter file path `manuscript/chapters/Chapter__2_TheMiner.md` confirmed (no `__Draft` suffix; renamed commit `4d860e8` 2026-05-21).
- ✓ Chapter line count 226 verified on current worktree.
- ✓ Pass 3.3 RATIFIED commit `e39d4e4` exists on origin/main (HEAD).
- ✓ Phase C-δ commit `46080d8` and Phase C-ε commit `34a5433` referenced in Pass 3.3 RATIFIED §1.
- ✓ Reference Pass 3.4 artifacts (Ch 9 + $100 Barrel + Noema) exist in `tools/rigor-passes/`.

---

## §1. Pass-3.4 scope reminder

Pass 3.4 applies the **adversarial / detractor character set** to the chapter. **Verdict-floor for adversarial characters is EXCLUDE; INCLUDE / NEUTRAL are not in scope.** All adversarial characters return EXCLUDE — that is expected and required per the Stage-3 template + audience-pressure-test-construction §3.2. **The diagnostic is NOT pass/fail per character.** The diagnostic is **which threads they collectively find** (§3 thread-pull synthesis) and whether those threads are (a) load-bearing chapter claims the chapter must hold against (acknowledge in pre-pub review queue; cross-chapter handoff if warranted), (b) procedural / cosmetic flags (spot-fixable without damaging Pass 3.3 acceptance verdicts), or (c) predisposed-hostile-by-financial-or-ideological-commitment threads that are not chapter-disarmable (mitigation at reception-cycle level only).

**Specifically tested under hostile read.** Ch 2's load-bearing claims that adversarial characters can pull on:

- **L1.** *Cost severance vocabulary defense* (lines 132–150): the framework's central move; the four-alternatives rejection (externality / displacement / transfer / appropriation each fails) + Mazzucato + Harvey lineage paragraphs.
- **L2.** *33–122× honest-cost multiple* (line 126): the chapter's quantitative claim — the gap between priced compensation and honest cost was an order of magnitude or more.
- **L3.** *Constrained-choice rebuttal to voluntary-trade frame* (lines 188–192): the chapter's structural reply to the "miners chose this work" + libertarian-bootstrap objection.
- **L4.** *Mechanism-not-motive frame* (lines 173–196): the chapter's structural anti-villainization + pro-industrialization preemption surface.
- **L5.** *Spatial cost severance / Distance section* (lines 154–162): the chapter's geographic-gap structural claim.
- **L6.** *Purdue second-cycle as cultural-pathology rebuttal* (lines 200–210): the chapter's structural reply to "Appalachian character / learned helplessness / cultural pathology" framings.
- **L7.** *Information-asymmetry argument* (lines 184, 190): "the industry knew — the pathology had been documented for decades — but companies resisted dust regulations and disputed the science with the same playbook the tobacco industry would later make famous and the climate industry would later use again."
- **L8.** *Implicit bonds-architecture framing* (line 100): "capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail... was never built."

**Adversarial set:** 8 characters drawn from the categorical hostile-read positions per [audience-pressure-test construction](../drafting-templates/audience-pressure-test-construction.md) §3.2, scoped to Ch 2's specific argumentative surface and chosen for **maximum coverage of distinct attack vectors**:

1. **A1.** Coal-industry-aligned economist / former industry-veteran econ-consultant
2. **A2.** Free-market libertarian / Reason-or-Cato-tradition reader
3. **A3.** Pigouvian-orthodoxy welfare economist
4. **A4.** Coal-state Republican policy aide / Manchin-or-Justice-aligned reader
5. **A5.** Trumpian-populist / Vance-coded reader
6. **A6.** Industrial-history triumphalist / Pinker-tradition optimist
7. **A7.** Pollyannish-policy reader / "we already fixed that"
8. **A8.** Skeptical Appalachian academic (Eller / Catte / Stoll-tradition)

Set construction rationale: the eight cover distinct attack vectors — methodological / cost-attribution (A1); ideological-libertarian on instrument choice (A2); methodological-orthodox on instrument choice (A3); regional-political (A4); populist-cultural (A5); historiographic / counterfactual (A6); already-solved-problem (A7); scholarly-regional / instrumentalization (A8). Cross-pressure pairs designed in: A2 vs A3 (libertarian-rejects-bond vs Pigouvian-prefers-tax — opposite-direction critique of the same bonds-architecture framing at line 100); A4 vs A8 (defends-region-by-defending-industry vs defends-region-by-resisting-instrumentalization — opposite-direction regional protection); A5 vs A6 (elite-Left ressentiment vs net-welfare-gain — opposite-direction frames of the same industrialization material).

---

## §2. Per-character adversarial verdicts

### Character A1 — Coal-industry-aligned economist / former industry-veteran econ-consultant

**Verdict: ⚠⚠⚠ EXCLUDE.** A1 is the canonical predisposed-hostile-by-financial-incentive case per Ch 9 Pass 3.4 §2 Character 3 framing — the framework's apparatus IS the threat to A1's prior consulting relationships. Chapter does not try to land A1 and cannot land A1 without abandoning the book's purpose. Mitigation is reception-cycle-level only (supportive reception from non-industry-funded venues offsets industry-aligned hostility — a normal cost of doing structural-economic-critique work).

**Hostile-read posture.** Pressure-tests every cost-attribution number against confounder hypotheses; pressure-tests the 33–122× multiple as IAM-modeling-dependent; pressure-tests SMCRA framing as legitimate-rather-than-failed bonding; pressure-tests Black Lung Trust Fund framing as transfer-payment-rather-than-deficit; rejects "cost severance" framing as politicized rhetorical reframing of standard externality vocabulary; recommends industry-funded counter-research and citation of industry-friendly economists (Stavins / Nordhaus in narrow framings; Heritage / Cato energy policy clusters).

**Threads pulled.**

- **L2 (33–122× multiple at line 126).** *"The total arrives at something between 33 and 122 times the price the coal actually sold for, depending on which cost categories you include and which social cost of carbon estimate you use for the combustion tail. The range is wide because some of the costs are contested and some are genuinely uncertain. But the floor is 33 times."* A1 reads this as IAM-modeling-dependent + social-cost-of-carbon-anchored; the SCC anchoring is itself contested IAM territory (Pindyck 2017 "the climate-policy literature... in a sea of unknowns"); the floor estimate could itself be moved by parameter choices.
- **L1 + L8 implicit-bond architecture (line 100).** *"The architecture that would have closed the gap — capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail — was never built."* A1 reads as ideologically-loaded rephrasing of standard externality vocabulary; "rent capture" framing is policy-prescriptive disguised as accounting.
- **Black Lung Trust Fund framing at lines 70–74.** *"The fund that was supposed to make the accounting honest has been running a deficit for forty-five years. Someone is paying the difference. It is not the coal companies."* A1 contests the framing: the $44B distributed is a successful federal-benefit transfer mechanism; the $4.6B deficit + projected $15B by 2050 is a normal federal-trust-fund actuarial gap that exists across many transfer programs (Social Security; Medicare; etc.) and does not specifically prove industry shirking.
- **SMCRA reclamation bond framing at lines 80–86.** A1 reads as bond-design-failure (regulatory under-pricing of bonds) rather than industry-shirking — a procedural critique of SMCRA implementation, not a structural critique of extraction. The $865M bankruptcy-driven transfer is read as expected feature of any bankruptcy regime, not evidence of cost severance.
- **Purdue litigation at lines 204–208.** A1 challenges the geographic-overlay claim as cherry-picked retrospective causal-attribution; the Sackler $11B + Big Three $21B settlements are framed as evidence that the legal system worked rather than evidence of cost severance.

**Chapter's structural moves that disarm.**

- **L4 "Mechanism, Not the Motive" section** (lines 173–196) explicitly preempts the "coal companies were evil" attack-surface A1 would normally weaponize. *"It does not prove that the coal companies were evil."* (line 178) and *"It does not prove that industrialization was a mistake."* (line 180) close off two common A1 counter-attacks.
- **Cross-chapter routing.** Chapter explicitly forwards the 33–122× detail-walk to Ch 8 (*"Chapter 8 walks the floor-estimate version of this calculation through the framework's full cost-decomposition for one specific ton of McDowell County coal in 1960"* line 126). Ch 2 itself does not stand on the methodology — Ch 8 does.
- **Floor-estimate framing.** *"the floor is 33 times"* — chapter does not stand on the upper-end estimate; A1's parameter-choice attack is targeted at the wide range, not at the floor.
- **L1 *"perfectly legal"* framing at line 140.** *"Value extraction is not theft. It is not fraud. In most cases, it is perfectly legal. It is what happens when the accounting system does not require honest pricing."* Pre-empts industry-friendly defense that frames cost severance as malfeasance; the chapter substantively concedes it is not.

**Net read.** Industry-aligned hostile reviewer would write a hostile review regardless of chapter structural moves; the framework-promise IS the threat to A1's funders or prior consulting relationships. ⚠⚠⚠ EXCLUDE: would weaponize chapter by demanding each cost-attribution claim survive industry-funded counter-narratives; would publish in industry-aligned venue (Heritage *Backgrounder* / *RealClearEnergy* / industry-association policy paper / *Issues in Science and Technology*). Not chapter-disarmable; reception-cycle mitigation only.

---

### Character A2 — Free-market libertarian / Reason-or-Cato-tradition reader

**Verdict: ⚠⚠ EXCLUDE.** A2 reads the chapter's implicit bonds-architecture framing at line 100 + constrained-choice rebuttal at lines 188–192 as substantive challenges to voluntary-trade economics; the chapter's structural moves (Mechanism-Not-Motive section + pro-industrialization preemption + Mazzucato/Harvey lineage transparency) operate within a register A2 can engage at scholarly-disagreement level but do not eliminate A2's load-bearing objection. A2 would write a critical review; the critique would land within Reason / Cato / *National Affairs* register rather than chapter-disqualification level.

**Hostile-read posture.** Reads bonds-architecture as expropriation of property rights; reads structural-compensation framing as redistribution dressed up as accounting; reads "constrained choice" rebuttal as paternalist denial of worker agency; reads cost-severance vocabulary as redistributive policy disguise. The Pass 3.3 Tier 3 #18 center-right policy reader (✓✓ INCLUDE) was the *non-libertarian* center-right wing (AEI / *National Review* / Reason but on the empirical / scholarly-inventory side); A2 is the more-purely-libertarian wing that pushes harder.

**Threads pulled.**

- **L3 constrained-choice argument (line 188).** *"In McDowell County at the industry's peak, the coal company was not one employer among many: it owned the land, the company store, the houses miners rented. When the alternative was leaving everything you knew, the choice to stay was not the unconstrained choice free-market theory assumes. Constrained choices are still choices, but they are not the same thing as free choices."* A2 reads as paternalist denial of worker agency; arguments about "constraint" can be made about any labor contract; the historical company-town structure does not invalidate the voluntary-trade frame for modern labor markets. The 2024-renter-bootstrap extension at line 192 *"the company town has returned in distributed form"* extends the constrained-choice argument beyond what A2 will concede.
- **L8 bonds-architecture framing at line 100.** *"capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail."* A2 reads as expropriation: bonds-architecture is property-rights-violation by another name; "rent capture" presupposes a state-claim on extracted value that A2 rejects categorically.
- **L1 "value extraction is not theft... it is what happens when the accounting system does not require honest pricing" at line 140.** A2 reads as rhetorical reframing that smuggles redistributive policy into accounting register. "Honest pricing" is doing work that should be done by markets, not by accounting fiat.
- **Information-asymmetry argument (line 190).** *"The industry knew — the pathology had been documented for decades — but companies resisted dust regulations and disputed the science with the same playbook the tobacco industry would later make famous and the climate industry would later use again."* A2 reads as guilt-by-association rhetorical move; the comparison to tobacco-industry science-denial is doing rhetorical work that A2 reads as substituted for argument.

**Chapter's structural moves that disarm.**

- **L4 Mechanism-Not-Motive section** *"It does not prove that mining communities were helpless or passive. They were not — they organized, they struck, they fought for wages and safety standards and benefits, and they won many of those fights. The miners had agency, and honoring that agency is essential."* (line 186) — substantive honoring of worker agency; pre-empts the paternalist-denial-of-agency attack at its first move.
- **Pro-industrialization preemption.** *"It does not prove that industrialization was a mistake. Cheap coal was essential to industrialization, and industrialization did reduce global poverty dramatically. Coal — American coal, Appalachian coal, McDowell County coal — was part of the energy system that made that possible. The people who made it possible had something to be proud of, and the framework does not dispute that."* (line 180) — substantive concession to A2's load-bearing pro-market frame.
- **Mazzucato + Harvey lineage paragraphs at lines 146 + 150** — explicit lineage-naming. A2 reads this register as confirming the framework's intellectual placement (it is *not* a neutral-accounting move; it has political genealogy) but the explicitness disarms the bad-faith-disguise critique.
- **Latusek's first-person voluntary-choice acknowledgment at line 170.** *"I went in that mine and ate that dust and knew better. I should have known better, but I thought I was invincible."* — the miner's own voice articulating the informed-consent-was-incomplete argument from inside the lived position. This is structurally precise: A2 cannot easily reject the constrained-choice argument when the miner himself articulates it.
- **"perfectly legal" concession at line 140.** Chapter concedes value extraction is not theft / not fraud — substantively narrows the dispute to instrument-choice and architecture, not legality.

**Net read.** A2 finds load-bearing thread in L3 + L8 (constrained-choice argument + implicit bonds architecture) but the chapter's substantive concessions on worker agency + pro-industrialization + legal-not-illegal + miner-voice-articulates-constraint hold against the chapter-disqualification level. A2 would publish a critical review within Reason / Cato / *National Affairs* register; the critique operates at scholarly-disagreement-within-shared-domain level. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (L3 + L8) the chapter's structural moves partially defuse but do not eliminate at the ideological-commitment level. **The cross-pressure with A3 (Pigouvian-orthodoxy: bonds-architecture rejected from the *other* direction in favor of price-internalization) suggests Ch 2 is positioned correctly in the political-economy debate.**

---

### Character A3 — Pigouvian-orthodoxy welfare economist

**Verdict: ⚠⚠ EXCLUDE.** A3 substantially agrees with the chapter's diagnostic claim (cost severance exists; market price did not internalize the externality) but rejects the chapter's implicit instrument choice (bonds-architecture at line 100) in favor of Pigouvian tax internalization. Chapter routes the tax-vs-bond debate explicitly to Ch 5 (per Pass 3.3 Tier 1 #4 ✓ verdict on this very basis); for Ch 2-in-isolation, A3 finds an instrument-choice methodology gap the chapter does not address.

**Hostile-read posture.** A3 is intellectually-aligned with the chapter's diagnostic (the framework names cost severance; A3 names "negative externalities") but methodologically-aligned against the framework's instrument-choice posture. A3 wants Pigouvian tax (price the externality at marginal social cost; let the market clear); A3 reads bonds-architecture as inferior to tax because bonds risk-shift to bondholder solvency + transfer-cost-to-administrator + create rent-seeking opportunity at bond-pricing layer.

**Threads pulled.**

- **L8 implicit bonds-architecture (line 100).** *"capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail."* A3 asks: why not just price the externality through Pigouvian tax and let the market clear? Routing-to-bearers via bond-architecture introduces administrative complexity Pigouvian tax does not require.
- **Black Lung Trust Fund framing at lines 70–74.** *"The fund that was supposed to make the accounting honest has been running a deficit for forty-five years."* A3 reads as evidence of the bond-architecture failure mode: trust fund is a quasi-bond mechanism, and it failed to fully self-fund. Pigouvian tax on coal at marginal social cost would have generated revenue without trust-fund actuarial-gap risk.
- **SMCRA reclamation bond framing at lines 80–86.** A3 reads the $4–6B bonding gap as evidence the bond-design didn't work — and would not have worked even if bonds had been larger, because the bond-pricing layer always under-estimates the long-tail. Pigouvian tax on extraction at marginal social cost would have generated revenue at the time of extraction, avoiding the bankruptcy-driven transfer problem.
- **L1 cost-severance-vs-externality framing at line 144.** *"Other names were available — externality, displacement, transfer, appropriation — and each fails to carry the specific structural feature severance names."* A3 reads the four-alternatives-rejection as gratuitous rhetorical reframing: "externality" is the standard Pigouvian vocabulary; the chapter's "and each fails" structural-defense is unnecessary for diagnostic purposes; introducing new vocabulary increases inter-disciplinary translation cost.

**Chapter's structural moves that disarm.**

- **Cross-chapter routing.** Pass 3.3 Tier 1 #4 verdict noted: *"Ch 2 does not engage the Pigouvian-tax-vs-bond question directly — that's Ch 5's territory per the Why-Bonds defense paragraph."* Chapter does not stand on the bonds-architecture choice; it forwards the debate to Ch 5 + Ch 6 + Ch 9. For Ch 2-in-isolation, this is a partial defense (the cross-reference is implicit, not explicit).
- **L1 four-alternatives-rejection at line 144** *"Externality names a cost that falls outside the transaction; it does not name who the cost falls on, or that someone specific is now carrying it, or that an architecture for accounting the carrying is missing."* — substantive engagement with A3's preferred vocabulary; chapter argues "externality" is insufficient *for the diagnostic purpose the framework needs*, not that "externality" is wrong as a Pigouvian concept. A3 reads this as scope-disagreement rather than methodological-disqualification.
- **Mazzucato + Harvey lineage transparency.** Chapter explicitly names that its framework extends Mazzucato + Harvey; A3 reads this as confirmation the framework operates within heterodox-econ tradition rather than Pigouvian mainstream. The transparency makes the methodological disagreement clean rather than disguised.
- **"perfectly legal" concession at line 140** — chapter does not stake the diagnostic on illegality; A3 can engage on instrument-choice level.

**Net read.** A3 substantially agrees on diagnostic + disagrees on instrument-choice. The chapter's cross-chapter routing of instrument-choice to Ch 5 partially defuses but the Ch 2-in-isolation read leaves the methodological gap exposed. A3 would publish a critical review within environmental-economics / welfare-economics register; the critique operates at scholarly-disagreement-within-shared-domain level. ⚠⚠ EXCLUDE: would actively reject the chapter-in-isolation; would qualify the rejection in the context of the broader book once Ch 5 + Ch 6 + Ch 9 are read. **Cross-pressure with A2 (libertarian rejects bond as expropriation) confirms Ch 2 is positioned correctly in the political-economy debate — both directional adversaries pull on the same passage from opposite ideological positions.**

---

### Character A4 — Coal-state Republican policy aide / Manchin-or-Justice-aligned reader

**Verdict: ⚠ EXCLUDE.** A4 is the canonical "regional-political defender of cheap-energy + working-class identity" hostile read. Chapter's L4 Mechanism-Not-Motive section + pro-industrialization preemption + Bailey + Latusek named-miner voices substantively disarm at structural-claim level; the cultural-pathology rebuttal at line 208 directly engages A4's own constituency-defensive register. A4 would push back on bonds-architecture and on the implicit-but-unstated "the next century should not extract this way" register; pushback at scholarly-disagreement level rather than chapter-disqualification level.

**Hostile-read posture.** Defends Appalachian working-class identity AND the extraction economy as both legitimate-and-honored. Reads any outside-the-region progressive framing as condescending. Resists framings that treat McDowell as a case-study without acknowledging McDowell's continuing political-economic stakes (current mining employment; current pension obligations; current state political-economy of the energy transition). Pushes back on bonds-architecture as Washington-imposed regulatory burden.

**Threads pulled.**

- **L8 implicit bonds-architecture at line 100.** A4 reads bonds-architecture as additional regulatory burden on already-struggling extraction industry; the framing does not engage with current state-level energy-policy stakes (post-coal transition in WV / KY / OH).
- **L5 spatial cost severance (line 158).** *"This is spatial cost severance: the geographic gap between where value is extracted and where costs are borne. Distance enabled ignorance, and ignorance made the accounting invisible."* A4 reads as outside-the-region observation; the framing assumes the *consumer* is the appropriate cost-bearer-by-default, which sidesteps A4's preferred frame (the consumer paid market price + paid taxes + paid for federal energy subsidies that flowed back; the cost severance frame double-counts the consumer's contribution).
- **Trust Fund deficit framing at line 72.** *"Someone is paying the difference. It is not the coal companies."* A4 reads as anti-industry framing; the actual answer (the federal general fund) is a transfer-pattern A4's policy-economy frame defends rather than opposes (federal subsidization of coal-region health-care is a normal cost of regional-economic transition that A4 wants to *increase*, not decrease).
- **Bonds-architecture would have hurt employment.** A4 reads the implicit framework as: if rent-capture bonds had been imposed at extraction, the marginal-cost-of-coal would have risen + employment at the mine would have fallen earlier + McDowell's transition would have been *more* abrupt rather than less. A4 reads this as policy-naive counterfactual.

**Chapter's structural moves that disarm.**

- **L4 Mechanism-Not-Motive section** *"the framework does not dispute that"* (the people who made cheap-coal industrialization possible had something to be proud of) — substantive concession that A4's working-class-pride frame is correct.
- **Bailey + Latusek named-miner voices** at lines 30–36 and 166–170 — the chapter operates *with* rather than *about* the coal-mining experience; A4 reads this as honoring rather than instrumentalizing.
- **Pro-industrialization preemption at line 182.** *"You can believe extraction was necessary — it was — and simultaneously believe the miners who developed black lung and the communities that absorbed the transition costs should have been made whole. If you believe industrialization was worth doing, the case for compensation is stronger, not weaker."* This is structurally precise for A4 — the chapter is *not* asking A4 to abandon the pro-industrialization frame; it is asking A4 to extend the frame to cost-compensation.
- **Cultural-pathology rebuttal at line 208.** *"The culture did not choose the opioid crisis. A corporation identified the crisis as a market opportunity and supplied it with a product engineered to create dependency."* This directly defends A4's constituency against the "Appalachian-character / learned-helplessness" framing A4's voters routinely encounter from outside-the-region progressive press. A4's load-bearing constituency-defensive register is operating *with* the chapter at this passage.
- **The chapter does NOT prescribe energy transition policy.** A4's worry about implicit "the next century should not extract this way" is left open by the chapter (Ch 9's pricing-architecture work is downstream); Ch 2 stops at diagnostic.

**Net read.** A4 finds threads on L8 + L5 + Trust Fund framing but the chapter's substantive concessions on pro-industrialization + working-class-pride + cultural-pathology-rebuttal hold against the chapter-disqualification level decisively. A4 would publish a critical review at scholarly-disagreement-within-shared-domain level; the chapter's anti-instrumentalization moves leave A4 with substantive partial agreement. ⚠ EXCLUDE: would push back but chapter holds against the pushback. **The chapter's L4 + cultural-pathology-rebuttal + named-miner-voices structural surface is the canonical "anchored in regional respect" disarm pattern; A4 is the audience this surface was built to land partial agreement with.**

---

### Character A5 — Trumpian-populist / Vance-coded reader

**Verdict: ⚠⚠ EXCLUDE.** A5 is the "elite-Left ressentiment" hostile read — sees framework as outside-the-region progressive condescension against working-class Appalachian dignity *despite* the chapter's explicit anti-villainization moves. The chapter's structural moves (Mechanism-Not-Motive section + Bailey + Latusek voices + cultural-pathology rebuttal) operate within a register A5 reads as performative-rather-than-substantive. A5 cannot be fully disarmed at chapter-claim level because A5's hostile-read register is meta-hermeneutic (reads the chapter for its political tribe rather than for its arguments).

**Hostile-read posture.** A5 reads the chapter's authorial position (outside-the-region observer with Mazzucato + Harvey lineage commitments) as politically-pre-loaded against the working-class Appalachian dignity register Vance's *Hillbilly Elegy* contests in one direction and *American Compass* contests in another. A5 reads the framework as the regional-progressive-elite recycling Sandel / Goodhart anywheres-vs-somewheres critique with cost-accounting vocabulary. The chapter's explicit honoring of work-was-real, miner-was-proud, industrialization-was-net-positive moves are read as performative-disarming (the chapter says these things but is doing redistributive-policy work *despite* saying them).

**Threads pulled.**

- **Mazzucato + Harvey lineage paragraphs at lines 146 + 150.** A5 reads this as confirming what the chapter's structural disarm-moves were trying to deny: the framework operates within outside-the-region progressive intellectual tradition. The transparency-of-lineage paragraphs make A5's tribe-reading easier, not harder.
- **L4 anti-villainization moves at lines 178 + 180 + 186.** A5 reads as performative — the chapter says coal companies were not evil + industrialization was not a mistake + miners had agency, but the framework's downstream work (bonds-architecture + rent-capture) is anti-extraction in policy effect *despite* the rhetorical disarm. The disarm is read as bait-and-switch.
- **L7 information-asymmetry argument at line 190.** *"The industry knew — the pathology had been documented for decades — but companies resisted dust regulations and disputed the science with the same playbook the tobacco industry would later make famous and the climate industry would later use again."* A5 reads the tobacco-industry + climate-industry chained analogy as the chapter's actual ideological commitment leaking through — the framework is in the tobacco / climate liability-architecture coalition; the rest is positioning.
- **L5 spatial cost severance at line 158** — A5 reads as outside-the-region observer claiming epistemic authority over the region: the *consumer* is framed as ignorant-and-not-villainous, but the framework still authorizes the outside-the-region observer to know what the consumer didn't know, which Vance-tradition treats as the central elite-Left epistemic conceit.
- **JFK opening at line 10.** A5 reads JFK 1960 framing as canonical-Democratic-Party-history move; the framing tribe-codes the chapter without saying so.

**Chapter's structural moves that disarm.**

- **L6 Purdue cultural-pathology rebuttal at line 208.** *"The culture did not choose the opioid crisis. A corporation identified the crisis as a market opportunity and supplied it with a product engineered to create dependency."* This is the most direct available structural defense of A5's constituency against the cultural-pathology framing — and it operates from within the framework, not from outside it. A5 reads the rebuttal substantively; the alignment with Vance's own targeting of Big Pharma is real.
- **Bailey + Latusek named-miner voices** — the chapter's body prose is *of* the miner, not just *about* the miner; A5 reads this as the chapter doing-not-saying the honoring-of-work register. The Latusek "loyalty wasn't there for me" register particularly lands the betrayed-by-corporate-employer beat that the populist-tradition validates.
- **Pro-industrialization preemption.** *"The people who made it possible had something to be proud of, and the framework does not dispute that."* The substantive concession is direct.
- **Cross-chapter routing of policy.** Ch 2 stops at diagnostic; Ch 9 carries the policy-architecture. For Ch 2-in-isolation, A5 cannot stake the "bait-and-switch" charge on prescriptive policy moves the chapter does not make.

**Net read.** A5's hostile read is meta-hermeneutic; the chapter cannot fully disarm meta-hermeneutic reads because the chapter operates within a tradition A5 reads as politically pre-loaded regardless of the chapter's explicit disarming. The chapter's Bailey + Latusek voices + Purdue rebuttal + pro-industrialization preemption are real partial-disarms — A5 reads them substantively, not just performatively, and the chapter lands partial-agreement (a real, not negligible, achievement against this hostile-read register). But A5 cannot follow the chapter all the way to the framework's implicit bonds-architecture; the political-tradition gap holds. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (meta-hermeneutic tribal-tradition reading) the chapter's substantive moves partially disarm but cannot fully eliminate at the political-tradition level. **The Purdue cultural-pathology rebuttal at line 208 is the chapter's single strongest A5-disarm move and is the closest the chapter comes to landing A5 partial-agreement.**

---

### Character A6 — Industrial-history triumphalist / Pinker-tradition optimist

**Verdict: ⚠ EXCLUDE.** A6 substantively agrees with the chapter's L4 pro-industrialization preemption (industrialization-reduced-global-poverty) but pushes back on the framework's implicit accounting of the residual unpriced costs as outweighing the priced benefits. The chapter's 33–122× multiple at line 126 is the load-bearing claim A6 contests. A6 would publish a critical review at scholarly-disagreement-within-domain level; the critique operates within shared pro-industrialization frame and contests methodology + counterfactual rather than the diagnostic itself.

**Hostile-read posture.** Reads from Pinker (*Enlightenment Now*) / Deaton (*The Great Escape*) / Roser-tradition pro-progress / Steven Radelet-tradition global-development-optimism. Accepts that local-cost-bearers like McDowell paid real costs; argues the *net welfare gain* from industrialization (lives extended globally; childhood mortality collapsed; literacy rates; nutrition; female mortality in childbirth) is *vastly* larger than the framework's residual-cost accounting acknowledges. Pushes back on counterfactual: how would McDowell have fared if coal had been priced at honest cost? Would the mines have opened at all? Would the global energy transition have happened later? Would global-poverty reduction have been slower?

**Threads pulled.**

- **L2 33–122× multiple at line 126.** A6 reads as one-sided accounting: the framework adds up the unpriced costs but does not add up the unpriced *benefits* — the diffuse global welfare gain from cheap-energy industrialization that flowed to the same consumers the chapter cites at line 158. The 33–122× multiple is the unpriced costs divided by the priced price; A6 wants the comparable multiple for unpriced benefits divided by priced price (consumer surplus from cheap energy; downstream productivity gains; mortality reductions from industrial-era public-health infrastructure).
- **L5 spatial cost severance (line 158).** *"This is spatial cost severance: the geographic gap between where value is extracted and where costs are borne... The consumers were not villains. Most of them would have been horrified by McDowell County if they had seen it."* A6 reads this as missing the upside-spatial-severance: the *benefits* of cheap coal flowed to consumers who never met the miners but whose lives were extended by the industrial public-health infrastructure cheap-coal funded. The chapter's framing makes spatial-cost-severance load-bearing but spatial-benefit-severance invisible.
- **Counterfactual gap at line 182.** *"You can believe extraction was necessary — it was — and simultaneously believe the miners who developed black lung and the communities that absorbed the transition costs should have been made whole. If you believe industrialization was worth doing, the case for compensation is stronger, not weaker."* A6 reads as posing the wrong counterfactual: the actual counterfactual is "if coal had been priced at honest cost, the mines would have opened later or not at all" — in which case McDowell would not have boomed-and-busted but the consumers who got the cheap-energy benefits would have been worse off. The chapter elides this trade-off.
- **L7 information-asymmetry (line 190).** A6 reads as moralizing-where-economics-suffices: in 1900, no industrial society had the public-health science to require honest pricing of long-tail externalities. The information-asymmetry argument retrospectively imposes 2026-era informed-consent standards on 1900-era industrial society.

**Chapter's structural moves that disarm.**

- **Pro-industrialization preemption at line 180–182.** *"It does not prove that industrialization was a mistake. Cheap coal was essential to industrialization, and industrialization did reduce global poverty dramatically."* — substantive concession to A6's load-bearing frame. *"the framework does not dispute that"* (line 180) is the structural disarm move.
- **L4 Mechanism-Not-Motive frame.** The chapter explicitly distinguishes "should extraction have happened" (the answer is yes) from "should the people who bore the costs have been compensated" (the diagnostic question). A6 can engage on the second question without abandoning the first.
- **Floor estimate (33×, not 122×).** Chapter does not stand on the upper-end estimate; A6's counterfactual-pricing-elasticity attack lands more on the upper end than the floor.
- **Cross-chapter routing of detail.** Chapter forwards the per-ton arithmetic to Ch 8; A6's methodology-pressure-test routes there.
- **L6 second-cycle Purdue framing** — A6's pro-progress register splits at the opioid second-cycle. Pinker tradition treats the opioid crisis as a regulatory-failure that has nothing to do with the industrialization-success narrative; the chapter's framing of opioid crisis as engineered-on-top-of-extraction-damage is a charge A6 must engage rather than dismiss. The chapter introduces a thread the optimist register has trouble handling without conceding the framework's claim.

**Net read.** A6 finds threads on L2 + L5 counterfactual + L7 retrospective-moralizing but the chapter's pro-industrialization preemption + Mechanism-Not-Motive frame + Ch 8 cross-routing of arithmetic hold against the chapter-disqualification level. The Purdue second-cycle at L6 is harder for A6 to handle and pulls a substantive partial-concession (A6 would have to engage rather than dismiss). A6 would publish a critical review at scholarly-disagreement-within-shared-domain level; the chapter's pro-progress concessions buy substantial common ground. ⚠ EXCLUDE: would push back but chapter holds against the pushback substantively. **The cross-pressure with A5 (elite-Left ressentiment reads framework as anti-industrialization; A6 reads framework as insufficient pro-industrialization accounting) shows Ch 2 is correctly positioned in the political-economy debate — both opposite-direction adversaries pull on the framework's industrialization-handling from opposite ideological positions.**

---

### Character A7 — Pollyannish-policy reader / "we already fixed that"

**Verdict: ⚠⚠ EXCLUDE.** A7 reads the chapter's L1 cost-severance framing as substantively redundant — SMCRA + Black Lung Trust Fund + post-OxyContin litigation already addressed the gap; the framework solves a problem that's already-solved. The chapter's own framing of the SMCRA bonding gap + Trust Fund deficit + Purdue $11B + Big Three $21B settlements directly refutes A7's claim, but A7's hostile-read posture reads the chapter's data as evidence-of-progress-toward-the-fix rather than as evidence-of-the-gap-still-open.

**Hostile-read posture.** Reads Pew Charitable Trusts / Brookings / Niskanen Center / Aspen Institute incremental-progress framing. The black-lung benefits program has paid $44B; the SMCRA reclamation regime exists and has $3.8B in bonds; the Purdue litigation has clawed back $11B from Sacklers + $21B from distributors. Each gap the chapter cites is met with "and here's the policy response that addressed it." A7 reads the cost-severance framing as either (a) overstating the gap because it does not credit the existing remedies sufficiently, or (b) presenting a problem whose policy response is sufficiently in-flight that the framework's instrument-architecture is not yet necessary.

**Threads pulled.**

- **L1 Trust Fund deficit framing at lines 70–74.** *"As of this writing, the Program has distributed $44 billion in benefits. That number sounds large until you hear what comes next: the Program's Trust Fund is $4.6 billion in debt."* A7 reads: $44B distributed is the success story; the $4.6B deficit is the work-in-progress portion; the framing as failure-mode is overclaim. The 2050 projected $15B deficit is concerning but is itself the subject of current policy revision (excise-tax rate adjustments; coal-tax base broadening).
- **SMCRA reclamation framing at lines 80–86.** *"The estimated cleanup cost runs between $7.5 billion and $9.8 billion. The available bond money totals $3.8 billion."* A7 reads: SMCRA is the institutional response; bonding gap is a fixable parametric problem (raise bond amounts; extend bonding requirements; reform bankruptcy treatment of mining liabilities). The framework's bonds-architecture is what SMCRA already is; the policy debate is about scope and pricing within the existing architecture rather than about whether the architecture exists.
- **Purdue litigation at lines 204–208.** *"The Sackler family extracted approximately eleven billion dollars from the company before it filed for bankruptcy. The Big Three pharmaceutical distributors — McKesson, Cardinal Health, AmerisourceBergen — settled for twenty-one billion dollars in 2022 for their role in shipping volumes that no legitimate medical demand could explain."* A7 reads: $11B + $21B = $32B clawed back through litigation; the legal-architecture worked; framing as cost-severance-still-operating is overclaim relative to the recovery's actual scale.
- **L8 implicit bonds-architecture at line 100.** *"The architecture that would have closed the gap... was never built."* A7 reads as factually inaccurate: SMCRA bonds + Black Lung Trust Fund + state-pension-asset bonding for coal-pension obligations already constitute the bonds-architecture. The framework's claim that the architecture was "never built" elides what was built (imperfectly).
- **2008 financial-crisis architecture (implicit in chapter cross-references; Ch 9 territory).** A7 reads Dodd-Frank + post-2008 capital-buffer regulation as the architectural-response to the 2008 cost-severance episode; the framework's claim that the architecture is missing is again over-stated.

**Chapter's structural moves that disarm.**

- **The numbers as stated.** The chapter's actual data is structurally precise: $44B distributed vs $4.6B deficit + $15B projected; $7.5–9.8B cleanup cost vs $3.8B bonds; $865M bankruptcy-driven transfer 2014–2016. The numbers themselves are the chapter's defense — A7 has to take a position on whether $4.6B running deficit + $15B projected by 2050 is "running deficit for forty-five years" (chapter framing) or "in-flight policy revision" (A7 framing). The substantive disagreement is real.
- **Line 86 framing.** *"The gap — somewhere between $4 billion and $6 billion — is not a rounding error. It is not a paperwork problem."* — anticipates A7's "it's just a parametric problem to be fixed" framing and rejects it.
- **L8 implicit-bonds framing at line 100.** *"The architecture that would have closed the gap — capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail — was never built. The community absorbed the full cost of transition alone. It is still absorbing it."* The "full life cycle of the externality tail" framing distinguishes between piecemeal remedies (which A7 cites) and structural lifecycle-architecture (which the chapter argues does not yet exist). A7 must engage at this level: does SMCRA + Black Lung Trust Fund constitute lifecycle-architecture or piecemeal remedies?
- **L6 Purdue cultural-pathology rebuttal at line 208** — Purdue litigation has clawed back ~$32B, but the chapter's framing is that *the corporation identified the crisis as a market opportunity and supplied it with a product engineered to create dependency*. The chapter's framing is structural — the litigation-after-the-fact is the *evidence* of cost severance, not the *resolution* of it. A7 has to engage: did the litigation actually compensate the cost-bearers (McDowell's 141-per-100,000 drug death rate continues)?
- **Cross-chapter routing.** Bonds-architecture-as-instrument is developed in Ch 5 / Ch 6 / Ch 9; A7's policy-redundancy critique partially routes to those chapters.

**Net read.** A7 reads the chapter's data as evidence-of-incremental-progress rather than evidence-of-structural-gap. The chapter's framing of the SMCRA + Trust Fund + Purdue numbers directly contests A7's read; the substantive disagreement is whether "$4.6B deficit running for 45 years + projected $15B" + "$4–6B reclamation gap" + "$32B Purdue clawback vs 141-per-100,000 drug deaths still operating" constitute structural gap or in-flight remedy. The chapter's framing is structurally precise; A7's pollyannish read requires denying the chapter's numerical framing at the line-by-line level. ⚠⚠ EXCLUDE: would actively reject the structural-gap framing; would publish a critical review at center-policy register (Niskanen / Aspen / Pew); the critique operates at the level of "framework overclaims relative to current policy state." **The chapter's L8 lifecycle-architecture framing at line 100 is the canonical disarm — A7 has to engage with lifecycle-vs-piecemeal at structural-claim level rather than just citing remedies; this engagement is harder than the surface read suggests.**

---

### Character A8 — Skeptical Appalachian academic (Eller / Catte / Stoll-tradition)

**Verdict: ⚠ EXCLUDE.** A8 is the canonical scholarly-regional-self-determination hostile read — defends McDowell's right to be place-rather-than-case-study; flags any rhetorical move that treats the region as evidence-for-framework rather than as subject-in-itself. Chapter's structural moves (Bailey + Latusek named-miner voices + McDowell-resident anchoring + cultural-pathology rebuttal at line 208 + Catte / Stoll-adjacent register implicit in tone) substantively disarm at structural-claim level. A8 would push back on instrumentalization at scholarly-engagement level rather than chapter-disqualification level. Pass 3.3 Tier 3 #11 McDowell-resident reader uplifted ✓✓ → ✓✓✓ on the same structural anchor; A8 (scholar-rather-than-resident) tightens the verdict by one increment but does not flip the disarm.

**Hostile-read posture.** Reads from Ron Eller (*Uneven Ground: Appalachia Since 1945*) / Elizabeth Catte (*What You Are Getting Wrong About Appalachia*) / Steven Stoll (*Ramp Hollow: The Ordeal of Appalachia*) regional-scholarship-tradition. Flags any move that treats McDowell as case-study-for-an-outside-the-region-framework rather than as place-in-itself; flags any move that uses McDowell's data without crediting the region's own self-narration tradition; flags any move that positions outside-the-region observer as epistemically-authoritative over the region.

**Threads pulled.**

- **L5 spatial cost severance framing at line 158.** *"This is spatial cost severance: the geographic gap between where value is extracted and where costs are borne. Distance enabled ignorance, and ignorance made the accounting invisible."* A8 reads as outside-the-region observer claiming epistemic authority: the framework names what the region knew first and named first (Caudill *Night Comes to the Cumberlands* 1962; Eller; Catte; Stoll). The chapter does not cite the regional scholarship that has been doing this work for 60+ years.
- **L1 cost-severance vocabulary at lines 132–144.** *"At this point the book needs a word for what we've been describing"* — A8 reads as outside-the-region naming-act for a region that has its own naming tradition. Caudill's "colonial-economy" framing; Cheryl LaRoche's "internal-colonialism" framing; the Highlander Center's organizing-vocabulary tradition. The chapter's framework-vocabulary work substitutes outside-the-region vocabulary for regional-tradition vocabulary without explicit acknowledgment.
- **L4 Mechanism-Not-Motive section's structural-not-personal framing.** A8 reads as missing the regional-tradition emphasis on specific institutional actors (Norfolk & Western Railway; Pocahontas Fuel; Consolidation Coal; U.S. Steel) whose specific decisions over a century-long timeline shaped McDowell. The "structural not personal" framing erases the specific-institutional-actor narrative the regional scholarship has developed.
- **JFK opening at lines 10–16.** A8 reads JFK 1960 as classic outside-the-region narrative device — McDowell becomes legible to non-regional readers through the lens of a Massachusetts senator discovering it on a campaign visit. The framing privileges outside-the-region discovery-narrative over inside-the-region continuous-self-knowledge.
- **L7 information-asymmetry at line 190.** *"The industry knew — the pathology had been documented for decades — but companies resisted dust regulations and disputed the science."* A8 reads as missing the regional-organizing-tradition: the miners *also* knew (or knew approximately), and the regional organizing tradition (UMWA; Black Lung Association 1968–69; Disabled Miners and Widows organization; Miners for Democracy) was the actual mechanism by which the regulatory framework got built. The framing emphasizes industry-knew-and-hid rather than miners-organized-and-fought.

**Chapter's structural moves that disarm.**

- **L6 Purdue cultural-pathology rebuttal at line 208.** *"A familiar political narrative interprets these outcomes as cultural pathology — a failure of Appalachian character, a learned helplessness, a deficit in the people who live there. The Purdue litigation record is the most direct available refutation."* — direct engagement with the cultural-pathology framing the regional-scholarship-tradition has been fighting for decades. A8 reads this as the chapter operating *with* the regional tradition rather than against it.
- **Bailey + Latusek named-miner voices.** The chapter is anchored in named miners' own words on body experience + lived consequence; A8 reads as the chapter doing the with-the-people work rather than the about-the-people work.
- **L4 Mechanism-Not-Motive section's miner-agency paragraph.** *"It does not prove that mining communities were helpless or passive. They were not — they organized, they struck, they fought for wages and safety standards and benefits, and they won many of those fights. The miners had agency, and honoring that agency is essential."* (line 186) — direct concession to A8's load-bearing concern about regional-agency.
- **Specific town names + seam attribution at line 22.** *"The towns had names — Welch, Keystone, Kimball, War — and the towns had everything towns are supposed to have... The county sat on top of some of the richest metallurgical coal seams in the world, the kind of coal that made steel hard enough to build the Golden Gate Bridge, the Empire State Building, the aircraft carriers that turned the Pacific war."* — place-specificity register; A8 reads this as the chapter knowing the place rather than instrumentalizing the place.
- **Line 20 framing.** *"Before we look at what happened to McDowell County, we need to understand what McDowell County was."* — explicit prioritization of place-in-itself before place-as-case-study.

**Net read.** A8 finds threads on L5 + L1 + JFK opening + L7 (regional-scholarship and regional-organizing under-acknowledged) but the chapter's substantive moves on miner-agency + Bailey + Latusek voices + Purdue cultural-pathology rebuttal + specific town names hold against the chapter-disqualification level decisively. A8 would publish a critical review at scholarly-engagement level (Eller / Catte / Stoll-adjacent venue: *Journal of Appalachian Studies*; *Appalachian Heritage*) and the critique would operate within shared regional-respect framing rather than chapter-disqualification. The chapter's cultural-pathology rebuttal at line 208 specifically lands the regional-self-determination disarm that A8's tradition cares most about. ⚠ EXCLUDE: would push back on instrumentalization-by-outside-observer at academic-engagement level; chapter holds against the pushback substantively. **Flag for Pass 3.5 developmental-edit attention: line 184's "the structural mechanism by which the severance operated" is an analytical pivot that could absorb a scene-anchor restoration crediting the regional-organizing tradition (Black Lung Association 1968–69; UMWA's role in SMCRA passage) within the existing prose. Not a Pass 3.4 blocking concern; Pass 3.5 attention item.**

---

### §2.x — Per-character verdict tally

| Character | Verdict | Type |
|---|---|---|
| A1 — Coal-industry economist | ⚠⚠⚠ EXCLUDE | Predisposed-hostile-by-financial-incentive; non-chapter-disarmable |
| A2 — Free-market libertarian (Reason/Cato) | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T1 + T2) at ideological-tradition level |
| A3 — Pigouvian welfare economist | ⚠⚠ EXCLUDE | Active rejection on instrument-choice; intellectually-aligned on diagnostic; cross-chapter routing partial defuse (T3) |
| A4 — Coal-state Republican / Manchin-aligned | ⚠ EXCLUDE | Acknowledged thread; chapter holds substantively (T4) |
| A5 — Trumpian-populist / Vance-coded | ⚠⚠ EXCLUDE | Meta-hermeneutic tribal-tradition read; partially disarmable (T5) |
| A6 — Industrial-history triumphalist (Pinker) | ⚠ EXCLUDE | Acknowledged thread; chapter holds (T6); cross-pressure with A5 |
| A7 — Pollyannish "we already fixed that" | ⚠⚠ EXCLUDE | Active rejection on structural-gap framing; chapter holds at structural-claim level (T7) |
| A8 — Skeptical Appalachian academic (Eller/Catte/Stoll) | ⚠ EXCLUDE | Acknowledged thread; chapter holds substantively (T8) — Pass 3.5 attention item |

**All 8 EXCLUDE as expected per template verdict-floor.** Per-character verdicts are inputs to the §3 thread-pull synthesis, not the diagnostic itself.

---

## §3. Thread-pull synthesis (the central diagnostic)

Per canonical [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) + [Ch 9 Pass 3.4 §3](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) format. Threads found, ranked by adversarial-character pull-frequency.

| Thread | Pulled by adversarial chars # | Type | Recommendation |
|---|---|---|---|
| **T1.** Implicit bonds-architecture framing at line 100 (*"capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail — was never built"*) reads as policy-prescriptive expropriation under hostile right-libertarian read AND as inferior-to-Pigouvian-tax under hostile orthodox-welfare-econ read. **The cross-pressure structure (A2 reads as too much architecture; A3 reads as wrong architecture) is the canonical sign of a load-bearing claim positioned correctly in the political-economy debate.** | A1 (industry); A2 (libertarian); A3 (Pigouvian); A4 (coal-state R); A7 (pollyannish) | **Load-bearing chapter claim.** Bonds-architecture framing is the chapter's load-bearing structural-observation move that sets up Ch 5 + Ch 6 + Ch 9. Spot-fixing toward weaker framing would damage Pass 3.3 Tier 1 #3 (Mazzucato/Pistor/Christophers ✓✓✓), Tier 2 #7 (Stern/Hartwick-tradition ✓✓), Tier 2 #10 (reparations-economics ✓✓) acceptance verdicts. The chapter's L8 framing positions the framework as architecture-not-yet-built, which is the substantive contribution. | **HOLD.** Cross-chapter routing of instrument-choice to Ch 5 + Ch 6 + Ch 9 + Pass 3.3 Tier 1 #4 acceptance verdict at ✓ (tax-vs-bond is downstream) handles Pass 3.4's surfaced thread structurally. Acknowledge in pre-pub review queue. |
| **T2.** L3 constrained-choice rebuttal at lines 188–192 reads as paternalist denial of worker agency under libertarian-tradition hostile read; the 2024-renter-bootstrap extension at line 192 (*"the company town has returned in distributed form"*) extends the argument beyond what libertarian-tradition will concede. | A2 (libertarian); A4 (partial; constrained-choice extension into modern renter case is the partial pull) | **Load-bearing chapter claim.** Constrained-choice rebuttal is the chapter's load-bearing reply to the voluntary-trade frame. Spot-fixing would damage Pass 3.3 Tier 1 #4 (Coasean/welfare-econ ✓), Tier 2 #9 (Coasean/mainstream-econ skeptic ✓✓), Tier 3 #18 (center-right policy ✓✓) acceptance verdicts that the structural precision of this passage is what landed. | **HOLD.** Latusek first-person voluntary-choice articulation at line 170 (*"I went in that mine and ate that dust and knew better"*) is the structural disarm — the constrained-choice argument is articulated from inside the lived position, not imposed from outside; A2's paternalism critique cannot land cleanly against the miner's own voice. Acknowledge in pre-pub review queue. |
| **T3.** Pigouvian-tax-vs-bond instrument-choice methodology gap (Ch 2 does not engage tax-vs-bond directly; cross-chapter routing is implicit not explicit). | A3 (Pigouvian; primary); A1 (partial); A2 (partial — though A2 rejects both) | **Cross-chapter routing — already-resolved.** Chapter explicitly routes to Ch 5 per Pass 3.3 Tier 1 #4 acceptance verdict at ✓ (*"Ch 5 picks it up... acceptable for chapter-in-context"*). The instrument-choice debate is properly Ch 5 + Ch 6 + Ch 9 territory. | **HOLD with cross-chapter routing acknowledged.** No Ch 2 spot-fix required; routing is correct. Acknowledge in pre-pub review queue. |
| **T4.** L5 spatial cost severance framing at lines 154–162 reads as outside-the-region observer claiming epistemic authority over the region under regional-scholarship hostile read AND as missing upside-spatial-benefit-severance under pro-progress hostile read. | A5 (populist meta-read); A6 (industrialization-triumphalist); A8 (regional academic) | **Load-bearing chapter claim with cross-pressure structure.** Spatial cost severance is the framework's introduction of an abstract category (intergenerational + spatial cost severance) the rest of the book extends; spot-fixing would damage Pass 3.3 Tier 2 #6 (Aeon Philosophy ✓✓), Tier 3 #20 (public-philosophy generalist ✓✓) acceptance verdicts that this section is what landed. **Cross-pressure between A6 (framework misses upside-spatial-benefit-severance) and A8 (framework's epistemic-authority-over-region) is opposite-direction adversarial pressure on the same passage — canonical sign of correct positioning.** | **HOLD.** *"The consumers were not villains. Most of them would have been horrified by McDowell County if they had seen it."* (line 160) provides structural disarm against the elite-Left ressentiment read; cultural-pathology rebuttal at line 208 provides structural disarm against the epistemic-authority-over-region read. Acknowledge in pre-pub review queue. |
| **T5.** Mazzucato + Harvey lineage paragraphs at lines 146 + 150 + JFK opening at lines 10–16 + tobacco-industry/climate-industry analogy at line 190 are read as politically-pre-loaded tribal tradition signals under populist-meta-hermeneutic hostile read. | A5 (Trumpian-populist; primary); A2 (libertarian; secondary) | **Load-bearing chapter claim.** Mazzucato + Harvey lineage paragraphs are the chapter's load-bearing intellectual-history honesty move; spot-fixing would damage Pass 3.3 Tier 1 #1 + #2 + #3 (trade editor + literary agent + Mazzucato/Pistor/Christophers ✓✓ / ✓✓ / ✓✓✓) acceptance verdicts. The transparency-of-lineage IS what those readers value. | **HOLD.** L6 Purdue cultural-pathology rebuttal at line 208 is the chapter's strongest A5-disarm; the chapter does meaningful partial-landing against this hostile-read register (Bailey + Latusek voices + pro-industrialization preemption). Full disarm against meta-hermeneutic tribal-tradition reads is not achievable at chapter-claim level. Acknowledge in pre-pub review queue. |
| **T6.** L2 33–122× honest-cost multiple at line 126 reads as IAM-modeling-dependent + SCC-anchored under industry-aligned hostile read AND as one-sided accounting (counts unpriced costs but not unpriced consumer-surplus benefits) under industrial-history-triumphalist hostile read. | A1 (industry); A6 (Pinker-tradition); A7 (pollyannish partial) | **Cross-chapter routing — already-resolved + load-bearing chapter claim.** Chapter explicitly forwards the per-ton detail-walk to Ch 8 (*"Chapter 8 walks the floor-estimate version of this calculation through the framework's full cost-decomposition for one specific ton of McDowell County coal in 1960"* line 126). Ch 2 stands on the floor estimate (33×, not 122×); the cross-chapter routing is correct. | **HOLD.** Floor-estimate framing + Ch 8 routing handle T6 structurally. Acknowledge in pre-pub review queue + flag Ch 8 Pass 3.4 future-session input: industrial-history triumphalist (A6 here) is an adversarial-character Ch 8 Pass 3.4 should pressure-test against the per-ton arithmetic + counterfactual-pricing-elasticity Ch 8 detail-walk. |
| **T7.** L1 "we already fixed that" pollyannish counter-read against SMCRA + Black Lung Trust Fund + Purdue-litigation framing. | A7 (pollyannish; primary); A1 (industry; partial); A4 (coal-state R; partial — defends-existing-policy-architecture rather than denies-the-need-for-fix) | **Load-bearing chapter claim.** The chapter's framing of SMCRA bonding gap + Trust Fund deficit + Purdue clawback-vs-141-per-100,000-drug-deaths is structurally precise; "lifecycle architecture vs piecemeal remedies" is the chapter's substantive distinction. | **HOLD.** Line 86 *"The gap... is not a rounding error. It is not a paperwork problem"* + L8 *"never built... still absorbing it"* + L6 cultural-pathology rebuttal handle T7 structurally. A7's pollyannish read requires denying the chapter's numerical framing at the line-by-line level. Acknowledge in pre-pub review queue. |
| **T8.** Regional-scholarship + regional-organizing-tradition under-acknowledgment (chapter does not cite Caudill *Night Comes to the Cumberlands* / Eller / Catte / Stoll regional-scholarship lineage; chapter does not foreground UMWA / Black Lung Association 1968–69 / Miners for Democracy regional-organizing tradition that produced the existing regulatory architecture). | A8 (regional academic; primary); A4 (partial — defends-region-but-from-political-side) | **Pass 3.5 developmental-edit attention item.** Not a Pass 3.4 blocking concern. The chapter's substantive moves (Bailey + Latusek voices + cultural-pathology rebuttal + specific town names + line 20 *"Before we look at what happened... we need to understand what McDowell County was"* place-in-itself prioritization) disarm A8 at structural-claim level. But line 184's *"the structural mechanism by which the severance operated"* analytical pivot is a Pass 3.5 candidate site that could absorb a scene-anchor restoration crediting the regional-organizing tradition without inflating chapter length materially. | **HOLD for Pass 3.4. FLAG FOR PASS 3.5 DEVELOPMENTAL-EDIT.** Per the v3.1 Amendment B Pass 3.5 attention discipline. The chapter's existing Mechanism-Not-Motive section's miner-agency paragraph at line 186 (*"they organized, they struck, they fought for wages and safety standards and benefits"*) is the closest existing scene-anchor; Pass 3.5 should consider whether a more specific institutional-naming (UMWA / Black Lung Association 1968–69) at that paragraph would compound the existing disarm without crowding the chapter's existing structural-claim work. |

### §3.1 Synthesis observation — cross-pressure positions chapter correctly

The diagnostic value of running the 8-character adversarial set is in the **cross-pressure structure** the synthesis reveals:

- **T1 cross-pressure.** A2 (libertarian) reads bonds-architecture as *too much* architecture (expropriation); A3 (Pigouvian) reads bonds-architecture as *wrong* architecture (inferior to tax). Both adversarial reads point at line 100 from opposite ideological positions. **This is the canonical sign of a load-bearing claim positioned correctly in the political-economy debate** — a chapter whose framework is calibrated to the ledger-discipline middle ground will produce exactly this cross-pressure pattern. (Format precedent: Ch 9 Pass 3.4 §3.1 T1 cross-pressure between libertarian-PC and hard-left positions on the same Ch 9:144 passage.)
- **T4 cross-pressure.** A6 (industrial-history triumphalist) reads the framework as missing upside-spatial-benefit-severance; A8 (regional academic) reads the framework as outside-the-region epistemic authority. Opposite-direction adversarial pressure on the same Distance section.
- **T5 + T6 cross-pressure.** A5 (Trumpian-populist) reads framework as anti-industrialization-elite-tribal-coding; A6 (Pinker-tradition) reads framework as insufficient pro-industrialization accounting. Opposite-direction adversarial pressure on the same industrialization-handling.
- **T7 cross-pressure.** A1 (industry-aligned) reads chapter as overclaiming the gap; A7 (pollyannish) reads chapter as overclaiming the gap (but from opposite-direction policy-optimism rather than industry-defense); meanwhile pro-cost-severance readers like Pass 3.3 Tier 1 #3 ✓✓✓ Mazzucato/Pistor/Christophers cluster validate the framing decisively. The chapter's calibration is between opposite-direction skeptical reads.

**Across the eight adversarial characters, the chapter does NOT surface a load-bearing thread that compounds into a structural problem.** The threads found are either: (a) load-bearing claims the chapter is correctly making with cross-pressure structure as the diagnostic confirmation (T1, T2, T4, T5, T6, T7); (b) cross-chapter routed (T3 — Pigouvian tax-vs-bond methodology routes to Ch 5 + Ch 6 + Ch 9); (c) procedural Pass 3.5 attention items (T8 — regional-scholarship under-acknowledgment is a Pass 3.5 candidate restoration, not a Pass 3.4 spot-fix); or (d) predisposed-hostile-by-financial-incentive (A1 industry-aligned) that is not chapter-disarmable and routes to reception-cycle mitigation only.

---

## §4. Apparatus / consistency / named-subject sub-checks

Pass 3.3 RATIFIED §6 verified apparatus + named-subject consent + Path B contamination + scaffolding all clean post-Phase-C-ε. Pass 3.4 incidental check:

- **§4.1 No new apparatus thread surfaced by adversarial set.** No adversarial character flagged a register / convention / named-subject thread the Pass 3.3 acceptance test missed.
- **§4.2 Adversarial-reviewer institutional affiliations cited via public-record exception.** Reason, Cato, AEI, Heritage, Niskanen, Brookings, *Issues in Science and Technology*, *National Affairs*, *American Compass*, *RealClearEnergy*, *Journal of Appalachian Studies*, *Appalachian Heritage* institutional affiliations cited in framing context per [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md) public-record exception (institutional positions stated on-the-record in institutional capacity). No living-named-subject consent issue.
- **§4.3 Pinker / Deaton / Roser / Vance / Manchin / Caudill / Eller / Catte / Stoll / Sandel / Goodhart citations are public-record references to published-author work + public-figure institutional positions; consent discipline satisfied via public-record exception. No outreach contemplated (hard-constraint honored).**
- **§4.4 No new regressed-pattern surfaced.** Scaffolding scan clean per Pass 3.3 §6.4; Pass 3.4 surfaces no new placeholder / TK / TODO / drafting-template-vocabulary residue.

---

## §5. Cross-chapter coherence sub-check

Pass 3.3 RATIFIED §6.3 verified Path B contamination clean; Ch 5 / Ch 6 / Ch 9 cross-references coherent post-Phase-C-ε. Pass 3.4 incidental check for cross-chapter thread that adversarial-direction read surfaces:

- **§5.1 T1 + T3 — instrument-choice cross-chapter routing.** Tax-vs-bond debate routes to Ch 5 + Ch 6 + Ch 9 per Pass 3.3 Tier 1 #4 acceptance read. Ch 5 + Ch 6 + Ch 9 Pass 3.4 audits should test whether the cross-chapter cascade absorbs A2 (libertarian) + A3 (Pigouvian) hostile threads at the chapters that explicitly carry the instrument-architecture work. Ch 9 Pass 3.4 (RATIFIED 2026-05-23) already addressed A2-adjacent thread via Char 1 (libertarian PC) and A3-adjacent via Char 6 (IAM-tradition). **Confirmed: Ch 9 Pass 3.4 thread-pull synthesis carries the instrument-architecture load.** No new cross-chapter incoherence; routing is correct.
- **§5.2 T6 — 33–122× multiple Ch 8 routing.** Industrial-history triumphalist (A6) + industry-aligned (A1) adversarial pressure on the per-ton arithmetic routes to Ch 8. Ch 8 Pass 3.4 has not yet fired per the v3.0 / v3.1 architecture (Ch 8 is Stage-3-in-flight per workstream dashboard); **flag for Ch 8 Pass 3.4 future-session input: A1 industry-aligned + A6 industrial-history triumphalist as adversarial characters that should pressure-test Ch 8's per-ton cost-decomposition arithmetic + counterfactual-pricing-elasticity engagement.**
- **§5.3 T4 — spatial cost severance Ch 7 routing.** Chapter forwards spatial-cost-severance broader treatment to Ch 7 (line 162 *"Chapter 7 walks through more of them, by examining what happens when all of them collapse at once"*). Ch 7 Pass 3.4 has not yet fired per the v3.0 / v3.1 architecture (Ch 7 first-round review status per workstream dashboard); **flag for Ch 7 Pass 3.4 future-session input: A5 Trumpian-populist meta-hermeneutic + A6 industrial-history triumphalist + A8 regional-academic adversarial characters that should pressure-test Ch 7's spatial-and-intergenerational-cost-severance handling.**
- **§5.4 T5 — Mazzucato + Harvey lineage cross-chapter coherence.** Mazzucato + Harvey + Caudill / Eller / Catte / Stoll lineage handling across Ch 1 + Ch 2 + Ch 3 + Ch 5 is a Stage 1c coherence question for the Ch 2 + Ch 3 + Ch 5 sibling-coherence-check (analogous to Ch 9's Stage 1c D-3 deferred sibling-coherence-check on MacLean engagement across Ch 5 + Ch 9 + TA §1.10). **Pass 3.4 surfaces lineage-handling cross-chapter coherence as a question but does not block Ch 2's Pass 3.4 verdict on it.** Flag for Stage 1c sibling-coherence-check if Ch 5 Pass 3.4 surfaces analogous A5 / A8 threads.
- **§5.5 T8 — regional-organizing-tradition cross-chapter coherence.** UMWA + Black Lung Association 1968–69 + Miners for Democracy organizing-tradition handling across Ch 2 + Ch 3 (watermen-organizing) + Ch 5 (broader-labor-organizing) is a Stage 1c coherence question. **Pass 3.5 attention item per §3 T8 finding; not Pass 3.4 blocking.**

---

## §6. Out-of-scope flagging

### §6.1 Cross-chapter cascade flags

- **T6 (A1 + A6 industrial-history pressure on the 33–122× multiple) → Ch 8 Pass 3.4 future-session input.** Ch 8 carries the per-ton arithmetic; Ch 8 Pass 3.4 should pressure-test against A1 + A6 hostile reads. **Not blocking Ch 2 Pass 3.4 verdict.**
- **T4 (A5 + A6 + A8 pressure on the spatial / Distance section) → Ch 7 Pass 3.4 future-session input.** Ch 7 carries the broader treatment of cost-hiding mechanisms; Ch 7 Pass 3.4 should pressure-test the spatial-cost-severance handling against these adversarial characters. **Not blocking Ch 2 Pass 3.4 verdict.**
- **T8 (A8 regional-scholarship under-acknowledgment) → Ch 2 Pass 3.5 developmental-edit attention.** Per v3.1 Amendment B Pass 3.5 attention discipline. **Not blocking Ch 2 Pass 3.4 verdict.**
- **T5 (A5 meta-hermeneutic + A8 regional-scholarship) → Stage 1c D-cross-chapter lineage-handling sibling-coherence-check.** If Ch 5 Pass 3.4 surfaces analogous threads, consolidated cross-chapter lineage-acknowledgment note may be more coherent than Ch 2-only spot-fix. **Not blocking; not routing per pipeline doctrine §5 absent Ch 5 Pass 3.4 surface.**

### §6.2 Pass 3.5 developmental-edit future-session input

Per per-prompt serial cadence: Pass 3.5 fires after Pass 3.4 ratify-and-apply per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 Amendment B. Pass 3.4 incidental check for whole-chapter restoration-of-richness items surfaced by adversarial reads:

- **T8 restoration candidate.** Line 184's analytical pivot (*"the structural mechanism by which the severance operated"*) could absorb a scene-anchor restoration crediting the regional-organizing tradition (UMWA / Black Lung Association 1968–69) within the existing Mechanism-Not-Motive section. Pass 3.5 attention item.
- **A6 / A8 cross-pressure restoration candidate at the Distance section (lines 154–162).** Pass 3.5 should consider whether the Distance section can absorb a scene-anchor that grounds spatial-cost-severance in a specific bilateral observation (e.g., Pittsburgh-steel-mill-worker + McDowell-miner relational beat) without inflating chapter length materially. Pass 3.5 attention item.
- **Bailey + Latusek voices already function as scene-anchors.** Pass 3.5 should verify cumulative-LLM-cadence residue remains zero post-Phase-C-ε (Pass 3.3 §6.4 confirmed at acceptance level; Pass 3.4 adversarial read does not surface a new cadence concern).
- **No cumulative-LLM-cadence residue surfaced.** Adversarial reads operated at structural-claim level rather than scene-anchor level; chapter holds voice across 226 lines.
- **One incidental observation for Pass 3.5.** The vocabulary section (lines 132–150) is the chapter's analytically-densest passage; Pass 3.5 whole-chapter read should verify reader-engagement at this pivot does not flatten cumulatively. Pass 3.4 does not surface a gap; flagged as low-priority Pass 3.5 attention item.

### §6.3 Pre-publication review queue items (Stage 5 input)

Per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 Pre-publication review queue: load-bearing adversarial threads the chapter holds against (with structural disarm) but warrant acknowledgment in the pre-pub review queue for transparency to publisher / agent / editor:

- **T1 acknowledgment.** Bonds-architecture framing at line 100 invites cross-pressure from libertarian-tradition (rejects bonds as expropriation) AND Pigouvian-orthodoxy (prefers tax). Chapter's L4 Mechanism-Not-Motive frame + L1 four-alternatives-rejection + cross-chapter routing of instrument-choice to Ch 5 + Ch 6 + Ch 9 provide structural disarm.
- **T2 acknowledgment.** Constrained-choice rebuttal at lines 188–192 invites libertarian-tradition pushback on worker-agency-paternalism + 2024-renter-bootstrap extension. Latusek first-person voluntary-choice acknowledgment + L4 miner-agency paragraph provide structural disarm.
- **T3 acknowledgment.** Pigouvian-tax-vs-bond methodology gap in Ch 2-in-isolation; cross-chapter routing to Ch 5 carries the methodology-engagement.
- **T4 acknowledgment.** Spatial cost severance section invites cross-pressure from pro-progress (misses upside-spatial-benefit-severance) AND regional-scholarship (outside-the-region epistemic authority). Chapter's *"The consumers were not villains"* + cultural-pathology rebuttal + Ch 7 cross-routing provide structural disarm.
- **T5 acknowledgment.** Mazzucato + Harvey lineage paragraphs + JFK opening + tobacco-industry analogy invite populist-meta-hermeneutic tribal-tradition pressure; chapter's L6 Purdue cultural-pathology rebuttal + Bailey + Latusek voices + pro-industrialization preemption provide substantial partial-disarm; full disarm against meta-hermeneutic reads not achievable at chapter-claim level.
- **T6 acknowledgment.** 33–122× multiple at line 126 invites scholarly-engagement pressure-test from industrial-history triumphalist (one-sided accounting) + industry-aligned (IAM-modeling-dependent) reads; Ch 8 carries the per-ton arithmetic + counterfactual-pricing-elasticity engagement.
- **T7 acknowledgment.** Pollyannish-policy read frames SMCRA + Black Lung Trust Fund + Purdue-litigation as evidence of in-flight policy response; chapter's L8 "lifecycle architecture vs piecemeal remedies" distinction + line 86 *"not a rounding error"* + L6 cultural-pathology rebuttal handle structurally.
- **T8 acknowledgment.** Regional-scholarship lineage (Caudill / Eller / Catte / Stoll) + regional-organizing tradition (UMWA / Black Lung Association 1968–69) under-acknowledgment in Ch 2 prose; chapter's Bailey + Latusek voices + cultural-pathology rebuttal + place-in-itself framing at line 20 + miner-agency paragraph at line 186 provide structural disarm; Pass 3.5 candidate restoration site identified at line 184.
- **A1 reception-cycle note.** Industry-aligned reviewer reception is predisposed-hostile-by-financial-incentive (per Ch 9 Pass 3.4 §2 Char 3 canonical framing); chapter is not designed to land this reception; mitigation is reception-cycle level (supportive reception from non-industry-aligned venues offsets industry-aligned hostility).

---

## §7. Verdict synthesis

### §7.1 Per-character tally — full 8-character adversarial set

| Verdict | Count | Characters |
|---|---|---|
| ⚠ EXCLUDE | 3 | A4 (coal-state R / Manchin-aligned); A6 (industrial-history triumphalist); A8 (Appalachian academic) |
| ⚠⚠ EXCLUDE | 4 | A2 (libertarian); A3 (Pigouvian); A5 (Trumpian-populist); A7 (pollyannish) |
| ⚠⚠⚠ EXCLUDE | 1 | A1 (industry-aligned) — predisposed-hostile-by-financial-incentive; non-chapter-disarmable |
| **Total** | **8 EXCLUDE** | **As expected per template verdict-floor — all adversarial characters selected for hostile read** |

### §7.2 Aggregate Pass-3.4 robustness verdict

**ROBUST.**

- **No ⚠⚠⚠ chapter-disqualifying threads found that are chapter-disarmable.** A1 (industry-aligned ⚠⚠⚠ EXCLUDE) is predisposed-hostile-by-financial-incentive per the Ch 1 REAUDIT v3 §5.3 + Ch 9 Pass 3.4 §2 Char 3 canonical framing; not chapter-disarmable; mitigation is reception-cycle level. This is the normal cost of doing structural-economic-critique work.
- **Common load-bearing threads (T1, T2, T4, T5, T6, T7) found; chapter's structural moves disarm sufficiently at structural-claim level.** Each thread is acknowledged in the pre-publication review queue (§6.3) for publisher / agent / editor transparency.
- **One cross-chapter routed thread (T3) on instrument-choice methodology** is already-resolved via Ch 5 + Ch 6 + Ch 9 cascade; Pass 3.3 Tier 1 #4 ✓ verdict and Ch 9 Pass 3.4 CONDITIONALLY ROBUST verdict confirm the routing carries the load downstream.
- **One Pass-3.5 attention-item thread (T8)** on regional-scholarship + regional-organizing-tradition under-acknowledgment is flagged for Pass 3.5 developmental-edit candidate restoration but is NOT a Pass 3.4 blocking concern; chapter's existing structural disarm moves (Bailey + Latusek voices + cultural-pathology rebuttal + place-in-itself framing + miner-agency paragraph) hold at acceptance level (Pass 3.3 Tier 3 #11 ✓✓✓ + #15 ✓✓ confirm).
- **Cross-pressure structure across the 8-character set indicates correct positioning.** T1 + T4 + T5 + T6 + T7 each show opposite-direction adversarial pressure on the same chapter passages — the canonical sign of load-bearing claims positioned correctly in the political-economy debate. The chapter is correctly calibrated to the ledger-discipline middle ground.

**Why ROBUST rather than CONDITIONALLY ROBUST.** The comparison with Ch 9 Pass 3.4 (CONDITIONALLY ROBUST) is instructive: Ch 9's verdict was CONDITIONALLY ROBUST because (a) Ch 9 carries the explicit instrument-architecture work where the bonds-vs-tax debate is load-bearing on the chapter itself, and (b) T3 (MacLean engagement) was a procedurally-spot-fixable thread the chapter could absorb. Ch 2 by contrast routes the instrument-choice debate cleanly to Ch 5 + Ch 6 + Ch 9 (T3 here is cross-chapter routed rather than chapter-resident), and Ch 2's surfaced thread T8 (regional-scholarship under-acknowledgment) is a Pass 3.5 attention item rather than a Pass 3.4 spot-fix candidate. The chapter's structural disarm surface (L4 Mechanism-Not-Motive section + L6 Purdue cultural-pathology rebuttal + named-miner voices + pro-industrialization preemption + place-in-itself framing) is unusually substantive for a diagnostic chapter — and it absorbs the adversarial pressure at structural-claim level without requiring spot-fix retrofits. **The chapter is the canonical example of a Stage-3 chapter whose Pass 3.3 acceptance verdict (READY AS-IS at 19/20 INCLUDE) is corroborated rather than complicated by the Pass 3.4 robustness pressure-test.**

**Does NOT require structural engagement.** No common load-bearing thread surfaces where the chapter does NOT disarm; no cross-chapter workstream needed beyond the existing Ch 7 + Ch 8 + Ch 5 Pass 3.4 forward-flags (which were already on the workstream cascade independently).

### §7.3 Phase-C disposition recommendation

**RECORD-ONLY.** No required Phase C spot-fix application session from Pass 3.4.

- All load-bearing threads (T1, T2, T4, T5, T6, T7) are hold-as-is with pre-pub-review-queue acknowledgment.
- T3 is cross-chapter routed (Ch 5 + Ch 6 + Ch 9; already carries the load).
- T8 is Pass 3.5 attention item (not Pass 3.4 spot-fix candidate).
- A1 (industry-aligned ⚠⚠⚠ EXCLUDE) is reception-cycle mitigation only.
- **No optional spot-fix candidates surfaced.** Pass 3.4 corroborates the Pass 3.3 RATIFIED first-round-close disposition (commit `e39d4e4` 2026-05-24) — the chapter holds against adversarial pressure at the structural-claim level the Pass 3.3 acceptance verdict predicted.

### §7.4 Pass 3.5 readiness

Pass 3.5 (developmental-edit) **can fire** per v3.1 Amendment B per-prompt serial cadence after Pass 3.4 ratify (or hold-as-is ratification if no Phase C applies). Pass 3.4 surfaced one Pass 3.5 candidate restoration site:

- **Line 184 analytical pivot + scene-anchor candidate** for regional-organizing-tradition acknowledgment (UMWA / Black Lung Association 1968–69 / Miners for Democracy) within the existing Mechanism-Not-Motive section's miner-agency paragraph at line 186. Pass 3.5 should consider whether this restoration would compound the chapter's existing A8 + A5 disarm without crowding the existing structural-claim work.
- **Distance section (lines 154–162) scene-anchor candidate** for bilateral observation that grounds spatial-cost-severance in a relational beat (e.g., Pittsburgh-steel-mill-worker + McDowell-miner). Pass 3.5 attention item if it does not inflate chapter length materially.
- **Vocabulary section (lines 132–150) cadence verification.** Pass 3.5 should verify the analytically-densest passage does not flatten cumulatively after Phase-C-γ voice-polish chiseling. Pass 3.3 §6.4 already confirmed clean at acceptance level.

**Recommended next session for Ch 2:** Author ratification of Pass 3.4 ROBUST verdict + acknowledgment of T8 Pass 3.5 attention item. After ratification, Pass 3.5 (developmental-edit) fires per per-prompt serial cadence per v3.1 Amendment B (3.1 → 3.2 → 3.3 → 3.4 → 3.5; each in its own prompt).

---

## §8. What this pass did NOT do

Per framing's hard constraints + v3.1 Amendment B per-prompt serial cadence:

- **Did NOT apply spot-fixes to the chapter file.** Phase C (per-chapter spot-fix application session) does that after author ratification; no required Phase C spot-fixes from Pass 3.4.
- **Did NOT re-run Pass 3.1 / 3.2 / 3.3.** All RATIFIED (commits `5bc6edb` + `3dcb15d` + `fa08c10` + `e39d4e4`).
- **Did NOT re-write paragraphs.** Findings + thread-pull synthesis + STOP, per the Pass-3.4 template hard constraint.
- **Did NOT contact named subjects.** Per consent discipline; public-record exception applies for citation of adversarial-reviewer institutional affiliations + published-scholar references (Pinker / Deaton / Roser / Eller / Catte / Stoll / Caudill / Vance / Manchin) but not for outreach per hard constraint.
- **Did NOT return INCLUDE or NEUTRAL verdicts for adversarial characters.** Verdict-floor is EXCLUDE per template; adversarial characters are SELECTED for hostile read.
- **Did NOT re-litigate the Pass 3.3 RATIFIED first-round-close disposition.** Pass 3.3 RATIFIED 2026-05-24 (commit `e39d4e4`) is canonical input + corroborated baseline for this pass.
- **Did NOT pre-empt Pass 3.5 (developmental-edit).** Pass 3.5 fires per per-prompt serial cadence after Pass 3.4 ratification. T8 is flagged for Pass 3.5 attention but Pass 3.5 itself is a separate session.
- **Did NOT initiate cross-chapter workstreams.** T1 + T3 + T4 + T6 forward-flag Ch 5 + Ch 6 + Ch 7 + Ch 8 + Ch 9 Pass 3.4 attention but do not spin up cross-chapter workstreams; routing is per-existing-cascade.

---

## §9. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `manuscript/chapters/Chapter__2_TheMiner.md`.
- ✓ Did NOT re-write paragraphs.
- ✓ Did NOT re-score Pass 3.1 / Pass 3.2 / Pass 3.3 — all ratified + Phase C applied; referenced for context only.
- ✓ Did NOT re-litigate Pass 3.3 RATIFIED 2026-05-24 first-round-close disposition.
- ✓ Did NOT contact named subjects (including adversarial-reviewer institutional affiliations + published-author references — public-record exception applies for citation but not for outreach).
- ✓ Did NOT return INCLUDE or NEUTRAL verdicts for adversarial characters — verdict-floor EXCLUDE per template.
- ✓ DID produce a thread-pull synthesis table as the central diagnostic (§3); per-character verdicts (§2) are inputs to the synthesis, not the diagnostic itself.
- ✓ DID flag cross-chapter incoherence surfaced by adversarial-direction read beyond what Pass 3.3 §6 cleared — T6 (Ch 8 Pass 3.4 forward-flag) + T4 (Ch 7 Pass 3.4 forward-flag) + T5 (Stage 1c lineage-handling sibling-coherence flag) per §5 + §6.1.
- ✓ Verified post-Phase-C-ε chapter line count (226 lines, verified 2026-05-24) against current worktree.
- ✓ Verified Pass 3.3 RATIFIED commit `e39d4e4` exists on origin/main (HEAD).
- ✓ Verified Phase C-δ commit `46080d8` + Phase C-ε commit `34a5433` referenced in Pass 3.3 RATIFIED §1.
- ✓ Verified reference Pass 3.4 artifacts (Ch 9 + $100 Barrel + Noema) exist in `tools/rigor-passes/`.
- ✓ Applied [Ch 9 Pass 3.4 §3 thread-pull synthesis](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) format model + [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) canonical thread-pull synthesis structure.
- ✓ Set construction per [audience-pressure-test construction §3.2](../drafting-templates/audience-pressure-test-construction.md) adversarial character types; 8 characters selected from the prompt's 12-candidate set for maximum coverage of distinct attack vectors.

---

## §10. Cross-references

- **Chapter under audit:** [`manuscript/chapters/Chapter__2_TheMiner.md`](../../manuscript/chapters/Chapter__2_TheMiner.md) — current post-Phase-C-ε state (226 lines / ~5,367w).
- **Pass 3.3 RATIFIED baseline (this Pass 3.4 pairs with):** [`commons_bonds_rigor_pass_2026-05-24_ch2_the_miner_pass_3_3_light_refire_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-24_ch2_the_miner_pass_3_3_light_refire_v1.0.0.md) — RATIFIED 2026-05-24 (commit `e39d4e4`).
- **Original Pass 3 audience-load:** [`commons_bonds_rigor_pass_2026-05-13_ch2_the_miner_stage3_audience_load_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-13_ch2_the_miner_stage3_audience_load_v1.0.0.md) — RATIFIED 2026-05-13 + appendices through 2026-05-21.
- **Format model — chapter-scale Pass 3.4:** [`commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) — PROPOSED 2026-05-23 (CONDITIONALLY ROBUST verdict).
- **Format model — essay-scale Pass 3.4 light:** [`pass-3-4-adversarial.md`](../../publishing/essays/100-barrel/rigor/pass-3-4-adversarial.md) — RATIFIED 2026-05-23 (ROBUST verdict).
- **Format model — Noema essay Pass 3.4:** [`pass-3-4-adversarial.md`](../../publishing/essays/noema-commons-bonds/rigor/pass-3-4-adversarial.md) (commit `35307ba` CONDITIONALLY ROBUST).
- **Canonical thread-pull synthesis format:** [`commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) §5.3.
- **v3.1 discipline reference:** [`tools/memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) — Amendment A two-class cascade + Amendment B 5-pass.
- **Stage-3 template:** [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)".
- **Audience-pressure-test construction:** [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) §3.2 adversarial character types.
- **Named-subject consent discipline:** [`tools/memory/feedback_named_subject_consent.md`](../memory/feedback_named_subject_consent.md) — public-record exception for institutional positions + published-author references.
- **Verify-stale-memory-claims discipline:** [`tools/memory/feedback_verify_stale_memory_claims.md`](../memory/feedback_verify_stale_memory_claims.md).

---

## §11. Ratification record

**2026-05-24 — PROPOSED.** Pass 3.4 audience-load robustness rigor pass for Ch 2 (The Miner) — post-Phase-C-ε state. Aggregate verdict **ROBUST** — thread-pull synthesis confirms chapter survives adversarial pressure at structural-claim level; no thread compounds into structural problem; cross-pressure structure across 8 adversarial characters confirms correct positioning in the political-economy debate.

Awaiting author ratification of:

1. **Aggregate ROBUST verdict.** Closing pass of Ch 2's first-round-review explicit-gate cascade per v3.1 Amendment A.
2. **No Phase C application required (RECORD-ONLY disposition).** Pass 3.4 corroborates Pass 3.3 RATIFIED first-round-close (commit `e39d4e4`).
3. **T8 (regional-scholarship + regional-organizing-tradition under-acknowledgment) flagged for Pass 3.5 developmental-edit attention** at line 184 analytical pivot + line 186 miner-agency paragraph. Not Pass 3.4 spot-fix candidate; Pass 3.5 candidate restoration site.
4. **Cross-chapter forward-flags acknowledged:**
   - T6 (33–122× multiple per-ton arithmetic) → Ch 8 Pass 3.4 future-session input.
   - T4 (spatial cost severance broader treatment) → Ch 7 Pass 3.4 future-session input.
   - T1 + T3 (instrument-choice tax-vs-bond) → already carried by Ch 5 + Ch 6 + Ch 9 cascade (Ch 9 Pass 3.4 RATIFIED 2026-05-23 confirmed).
   - T5 + T8 (Mazzucato + Harvey + regional-scholarship lineage handling) → Stage 1c sibling-coherence-check consideration if Ch 5 Pass 3.4 surfaces analogous threads.
5. **Pre-publication review queue items recorded** (§6.3) per Stage 5 input discipline.
6. **Pass 3.5 developmental-edit queued as next session** for Ch 2 per v3.1 Amendment B per-prompt serial cadence (3.1 → 3.2 → 3.3 → 3.4 → 3.5).

**Hard constraints adherence:**

- [x] No spot-fixes applied to the chapter file.
- [x] Pass 3.3 RATIFIED treated as canonical Pass 3.4 input.
- [x] Adversarial set construction per [audience-pressure-test construction §3.2](../drafting-templates/audience-pressure-test-construction.md); 8 characters selected for maximum coverage.
- [x] Per-character verdicts (§2) inputs to thread-pull synthesis (§3); §3 is the central diagnostic, NOT per-character pass/fail.
- [x] Pass 3.1 (fact-check) NOT re-run.
- [x] Pass 3.2 (voice-polish) NOT re-run.
- [x] Pass 3.3 (audience-load acceptance) NOT re-run.
- [x] Pass 3.5 (developmental-edit) NOT pre-empted; flagged for separate session.
- [x] No named subjects contacted.
- [x] Verbatim quotes only when citing chapter text.
- [x] Verdict format thread-pull synthesis (NOT pass/fail per character).
- [x] Cross-chapter coherence concerns flagged for PM-session cross-thread tracking (§6.1 + §11.4).
- [x] v3.1 per-prompt serial cadence preserved (Pass 3.4 fires after Pass 3.3 RATIFIED, in its own prompt).
- [x] Locked elements preserved verbatim (chapter file unchanged by this pass).

---

*End of Ch 2 Stage-3 Pass 3.4 (Audience-Load Robustness) rigor pass — PROPOSED 2026-05-24. Aggregate verdict ROBUST; no required Phase C spot-fixes; T1–T7 hold-as-is with pre-pub-review-queue acknowledgment per §6.3; T3 cross-chapter routed; T8 Pass 3.5 attention item; A1 industry-aligned reception-cycle mitigation only; T6 → Ch 8 Pass 3.4 forward-flag; T4 → Ch 7 Pass 3.4 forward-flag; T5 + T8 → Stage 1c sibling-coherence-check potential. Pass 3.5 (developmental-edit) is the next session for this chapter per per-prompt serial cadence after Pass 3.4 ratification. After this artifact lands on main: STOP. Report back to PM session + author per workstream branch discipline + rigor-pass artifact auto-merge-to-main discipline (per `CLAUDE.md` §"rigor-pass artifacts also autonomously fast-forward merge to main at session close").*

---

## Ratification — 2026-05-25

Author ratified the PROPOSED artifact as-recommended 2026-05-25.

**Ratified:**
- Aggregate verdict ROBUST (chapter holds at structural-claim level against full 8-character adversarial pressure).
- Per-character verdicts as recorded (1 × ⚠⚠⚠ A1 + 4 × ⚠⚠ A2/A3/A5/A7 + 3 × ⚠ A4/A6/A8 EXCLUDE-floor per template).
- Thread-pull synthesis T1–T7 hold-as-is structurally.
- T8 (regional-scholarship + UMWA / Black Lung Association 1968–69 / Miners for Democracy under-acknowledgment) carries forward as Pass 3.5 developmental-edit restoration-site candidate at line 184 analytical pivot + line 186 miner-agency paragraph.
- T4 → Ch 7 Pass 3.4 forward-flag (spatial cost severance pressure).
- T6 → Ch 8 Pass 3.4 forward-flag (per-ton arithmetic pressure).
- T5 + T8 → Stage 1c sibling-coherence-check potential if Ch 5 Pass 3.4 surfaces analogous threads.
- Phase C action: RECORD-ONLY (no chapter-text changes required).

**Pass 3.4 audience-load robustness — CLOSED for Ch 2's explicit-gate cascade.** Two of five Pass 3 sub-passes now ratified (3.3 acceptance + 3.4 robustness).

**Outstanding for Ch 2 explicit-gate cascade:**
- Pass 3.5 developmental-edit — T8 already pre-identified as restoration-site candidate; per Amendment B Amendment B per-prompt serial cadence, this is the natural next session.
- Stage 4 render-audit — author does offline.
- Stage 5 bookend pre-submission sign-off — gate-triggered (pre-pub / Wave 1 cascade / venue change).

---

*Ratification rev. 2026-05-25. Pass 3.4 closed; chapter holds adversarially-robust at structural-claim level. Pass 3.5 developmental-edit is the queued next session per Amendment B Amendment B 5-pass serial cadence.*
