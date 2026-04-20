Commons Bonds — Workstream 03: Chapter 6 Integration


# Workstream 03 — Chapter 6 Integration

Commons Bonds project · The heaviest writing pass · Chapter 6 is where the framework fully lands

**Prerequisites:** Workstream 01 (Master Decisions), Workstream 02 (Glossary Reconciliation). The eight-tier canonical version and all new vocabulary must be settled before this chapter is integrated — otherwise the integration is rewritten when upstream decisions change.

**Option C quick reference:** Two pillars (Cost Severance, RCV) + two methodologies (Abundance Inversion Test, Universality Test). Retired: V\_civ, Solidarity Architecture, Departure Liability, ESG.

## What this workstream does

Integrates the Abundance Inversion Test (Methodology 1) and the Eight-Tier Decomposition of RCV into Chapter 6 — currently structured around the three convergent pricing approaches (bottom-up damage accounting, real options, full RCV integral). The integration adds a fourth section, *RCV Decomposed*, which is the chapter's accessibility bridge from formula to application.

This is the biggest single content gain in the April 19 batch because it converts RCV from "a formula an economist can check" into "a structure a coal miner or nurse can use on their own situation." Without this section, Pillar 2 stays as math; with it, Pillar 2 becomes usable.

## Where Chapter 6 stands now

The current Chapter 6 draft file (`Commons Bonds - Chapter 6 (Three Ways of Counting) - Draft v1.html`) contains the three convergent approaches and the backtesting table. The spine is intact. What is missing is the operationalization that makes non-economists able to work with the framework.

The Make It Better doc's scaffolding for this chapter says: "Present the convergence: three models, different foundations, same direction, similar magnitudes. The backtesting table showing CS > 0 in every case. The corrected McDowell County numbers. The key insight: the fight over the social cost of carbon is itself a proxy war over how much cost severance we're willing to tolerate." All of that stays.

## The new fourth section: RCV Decomposed

Title candidates: "RCV Decomposed" · "The Eight Columns" · "What RCV Actually Counts."

Position: after the three convergent approaches, before the counterargument engagement (the "pricing the unpriceable" and "unfalsifiable" objections). The structural logic is: here are three ways of computing RCV that converge → here is what RCV is actually *made of* when you decompose it → here are the objections and the responses.

### What the section covers

1. **Opening move:** The RCV integral is mathematically correct but operationally opaque to a non-economist. The same total can be broken into eight named, separable components, each of which a coal miner, a nurse, a rare-earth worker, or an asteroid miner can identify in their own situation.
2. **The Abundance Inversion Test (introduced as methodology, not afterthought):** The test says — to identify a tier that has been hidden by abundance, strip one abundance layer and ask what becomes visible. Costs visible when a layer is stripped and invisible when it is restored are tiers. Costs visible regardless of abundance layer are already priced by existing frameworks. Costs that never become visible under any stripping are not tiers. The test is what generates the eight tiers systematically; it is also what prevents them from proliferating arbitrarily. It is a falsifiable generator.
3. **The seven abundance layers:** atmospheric, geographic, temporal, institutional, demographic, ecological, political. Each is explained in one sentence with an everyday example. The asteroid-miner scenario strips all seven simultaneously — that is why it is clarifying, not exotic.
4. **The eight tiers, each as a paragraph:** Lifetime Survival, Individual Risk (with Mission Failure Reserve as sub-tier), Dynastic Labor, Foreclosure, Community Transition Reserve, Ecological Carrying, Knowledge and Culture, Political Capture. Each paragraph names the tier, maps it to the abundance layer that reveals it, gives one concrete example, and notes whether existing markets price it. Reference Workstream 02 glossary entries for canonical definitions.
5. **The summary table:** Tier / Abundance Layer / Already Priced — use the table from the April 19 eight-tier file verbatim (it is already tight and scannable).
6. **The closing move:** Tie the decomposition back to RCV. The integral still integrates. What changes is that non-economists can now *see what is being integrated*. That is the difference between a framework that can be engaged by the general public and one that can be engaged only by mathematically trained economists.

### Register

Register 2 (accessible-technical). Introduce every concept as a story or concrete example before it becomes a framework. Use the Mars colony water scenario as a recurring illustration — each tier, tested against that scenario, produces the obviously correct answer.

The Make It Better doc is explicit: "Chapter 6 is the hardest chapter to write because it must carry the most analytical weight while remaining accessible. Use the Register 1 → Register 2 approach rigorously. Every concept enters as a story or concrete example before it becomes a framework."

### Length target

The current chapter scaffolds at 5,000–6,000 words. The RCV Decomposed section adds ~1,500 words. Total target 6,500–7,500 words. If it starts drifting past 8,000, something non-essential needs to come out — probably the lower-tier paragraphs or the detailed abundance-layer enumeration. The table is the load-bearing element.

## Counterargument engagement in this chapter

Per the Make It Better doc and the counterargument-weaving plan, Chapter 6 is where two of the nine steelmanned counterarguments get addressed in-line:

1. **"You're pricing the unpriceable — the model is arbitrary."** Response: the model structures uncertainty rather than eliminating it; the alternative (market pricing with zero externality adjustment) is not neutral, it is a specific assumption that externalities are worth zero; the three-model convergence is evidence that the output is not driven purely by arbitrary parameter choices; parameters are becoming more estimable over time. 3–4 pages.
2. **"The model is unfalsifiable — it always produces CS > 0."** Response: the model *can* produce CS ≤ 0. Examples: sand mining under full reclamation bonding in a jurisdiction with strong environmental regulation (abundant stock, short externality tail, full accountability bond); sustainably managed plantation timber with full replanting obligations. CS > 0 for non-renewable extraction under *existing* accountability regimes is a structural prediction; that prediction would be falsified the first time a jurisdiction implements full intergenerational foreclosure pricing and measures CS ≤ 0. Analogy: the claim that no airplane could fly faster than sound was falsifiable in 1940 and was falsified in 1947. 1–2 pages.

These were already planned. Verify they're drafted correctly in the current chapter file; if not, draft during this workstream.

## Old material to re-test against current rigor

| Item | Test | Likely verdict |
| --- | --- | --- |
| The "Three Ways of Counting" framing (damage accounting / real options / RCV) | Does it still survive now that RCV is decomposed into eight tiers? | Yes. Decomposition is a property of the third approach; it does not collapse the distinction between the three methods. All three still converge. |
| The backtesting table (six cases, CS > 0 in all) | Is it still six cases, or has Social Security made it seven? Does it need Mars / asteroid as theoretical rows? | Keep six empirical cases. Social Security is Chapter 5's case, not a backtest row (different scale of mechanism). Mars / asteroid go in Chapter 7, not here. |
| The corrected McDowell County numbers (spatial cost severance distinction) | Still relevant post-eight-tier? | Yes, reinforced. Spatial cost severance shows up explicitly as part of the Community Transition Reserve and Lifetime Survival tiers' geographic concentration. |
| The "precisely wrong vs. approximately right" response | Still the right frame? | Yes. This is the strongest single line of defense for the whole framework and belongs in Chapter 6. |
| Any remaining ESG references in the current draft | Should all be CSG per Ripple Effects sweep. | Verify complete; if not, fix during this pass. |
| Theorem A.3 reference ("non-renewable extraction") | Needs scope note now that Definition A.1 accepts ρ ≥ 0. | Coordinate with Workstream 08 (Technical Appendix). Chapter 6 itself does not restate the theorem; it just uses the result. |

## New material to integrate

| Source | What to pull in | Where |
| --- | --- | --- |
| `commons-bonds-eight-tier-decomposition 9.html` | The Abundance Inversion Test definition (block quote); the seven abundance layers (table); the eight tier definitions (as paragraphs); the summary table. | New fourth section of Chapter 6. |
| Workstream 02 canonical glossary | The eight-tier names, definitions, and pricing status. Use these verbatim for consistency across the project. | Referenced but not repeated; main text uses the terms. |

## Files involved

| File | Action |
| --- | --- |
| `Commons Bonds - Chapter 6 (Three Ways of Counting) - Draft v1.html` | Heavy rewrite. Add fourth section. Verify counterargument engagement. Sweep any ESG → CSG. |
| `Commons Bonds - Chapter 6 (Three Ways of Counting)` (Google Doc) | If this doc exists as the canonical chapter draft in Docs, update it rather than the HTML file. Verify which is being worked from. |
| `commons-bonds-eight-tier-decomposition 9.html` | After content migrated into Chapter 6 draft + Glossary + Technical Appendix, archive (move to `/Archives/` per Workstream 10). |
| `commons_bonds_technical_appendix_COMPLETE.html` | Not touched in this workstream. Definitions A.11–A.14 are added in Workstream 08 once Chapter 6 is stable. |

## Watch items

- **Do not label Option C.** The chapter introduces Methodology 1 (Abundance Inversion Test) and completes Pillar 2 (RCV) without naming them as "Methodology 1" or "Pillar 2." Option C is invisible book architecture per Decision B. If the reader notices the structure, good; it shouldn't be pointed out.
- **Do not introduce the Universality Test here.** That's Chapter 7. This chapter completes RCV and introduces the Abundance Inversion Test. Keep the scope disciplined.
- **Do not discuss named industries or beneficiaries.** Coal, oil, rare earths are fine as resource categories. Named companies, executives, or lobbying expenditures are Book Two (Workstream 07's territory).
- **Do not let the chapter become a formal derivation.** The Technical Appendix is for that. Chapter 6 is Register 2, not Register 3.
- **Do not preempt Chapter 10's closing.** The institutional legibility prescription belongs in Chapter 10, not Chapter 6. Chapter 6 ends on the decomposition; Chapter 10 ends on what to do with it.

## Check before ending the session

1. Four sections present: three approaches → convergence → RCV Decomposed → counterargument engagement.
2. Abundance Inversion Test is introduced as methodology (not afterthought).
3. Eight tiers named consistently with Workstream 02 glossary.
4. Abundance-layer mapping present (table or integrated).
5. Counterarguments 1 and 2 from the nine-counterargument list are addressed.
6. Length 6,500–7,500 words.
7. ESG → CSG sweep complete.
8. No labels of "Pillar" or "Methodology."
