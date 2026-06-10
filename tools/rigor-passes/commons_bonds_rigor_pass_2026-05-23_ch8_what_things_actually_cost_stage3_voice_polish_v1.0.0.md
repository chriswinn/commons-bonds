# Rigor Pass — Ch 8 "What Things Actually Cost" Stage-3 Pass 2 (Voice-Polish)

**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A — Ch 8 — Pass 2 (voice-polish)
**Date drafted:** 2026-05-23
**Status:** **RATIFIED 2026-05-25** (author ratify-as-recommended per §10.1 record; Phase C-β spot-fix application is a separate downstream session).
**Mode:** Audit-existing-prose (post-Pass-1 Phase-C-α + residual-hedge-alignment chapter is the baseline; v2.0 Amendment B voice-polish discipline as a distinct pass from Pass 1 fact-check and Pass 3 audience-load).
**Source chapter:** `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` — **243 lines** (post-Phase-C + post-cascade-reconciliation `9befb92` state verified 2026-05-23 against feature branch `claude/ch8-pass2-voice-polish-ad1947d16476c939c`, branched from `origin/main` at `b31ee2d`).

**Pass 1 cross-reference:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md` — RATIFIED + APPLIED via commit `5fe6af6` (Phase C — 16 Ch 8 edits + cross-chapter consequences) + commit `275b75a` (MED-6 Phase C-β follow-through — 2 residual hedge-alignment fixes). All HIGH-1 through HIGH-4 + MED-1 through MED-8 + LOW-1 + LOW-3 RATIFIED + APPLIED; remaining LOW findings held for pre-publication refresh. Pass 1 fact-check now functionally closed.

**Pass 3 status:** deferred to a subsequent session per author's per-prompt serial cadence (workstream #20 Phase A: Pass-1 → spot-fix → Pass-2 → spot-fix → Pass-3 → spot-fix per chapter, not bundled). Pass-2-surfaced audience-load concerns flagged forward at §7 below.

**Related cross-chapter context (relevant to Pass 2 scope):**
- Front-matter render-fix (commit `e1a533e`, 2026-05-18): byline italicization + horizontal-rule separator. Body-prose scope unaffected.
- File rename (commit `a09e319`, 2026-05-18): `Chapter__8_WhatThingsActuallyCost_Draft.md` → `Chapter__8_WhatThingsActuallyCost.md`.
- Rent-seeking paragraph insertion at line 122 (commit `a1e54d9` → ratified `bc02767`, 2026-05-17 → 2026-05-18) — cross-chapter rent-seeking-engagement workstream (Public Choice complementarity). The rent-seeking workstream's routing explicitly says Ch 8 + Ch 9 Pass 2 will absorb the rent-seeking-paragraph voice verification as standard pass scope; this Pass 2 honors that routing (§3 F-V12 below specifically audits the line 122 paragraph for voice-register match + LLM-tic surface).
- Cross-corpus IPG canonical construction (commit `57575b1`, 2026-05-22) — Option D ratified + applied. Affects the IPG numerical claim at line 168; Pass 2 verifies the prose form at line 168 holds clean as analytical-finance register.

---

## §0. Source artifacts read

1. `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` (post-Phase-C state; 243 lines; verified `wc -l`).
2. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md` — Pass 1 fact-check + §9 (Pass-2 future-session input) + §12 update note (rent-seeking paragraph fact-check coverage) + ratification record.
3. `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` §"Pass 2: Voice-polish" + §"Audit-existing-prose mode" (LLM-tic inventory + severity scale).
4. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md` — canonical Pass-2 artifact format model (F-V1 through F-V21 named-tic inventory; §0–§11 structure model).
5. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch7_on_other_worlds_stage3_voice_polish_v1.0.0.md` — most-recent analytical-register Pass 2 cross-reference; F-V13 chapter-wide em-dash density disposition (Option A hold-as-is per substance-drives-length); F-V12 chapter-closing rhetorical-pivot disposition (Option A hold per Ch 1 F-V14 cousin).
6. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_ch9_pricing_honestly_stage3_voice_polish_v1.0.0.md` — analytical-companion-chapter Pass 2 reference; F-V15 em-dash density + F-V6/F-V12 anaphoric-cadence dispositions used as calibration anchors.
7. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-20_ch3_thewaterman_stage3_pass3.2_voice_polish_v1.0.0.md` — most-recent Pass 3.2 artifact format reference + F-V3 ratification (anchor for em-dash-overuse discipline ratification 2026-05-21).
8. `tools/workstream-handoffs/archive/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` (per-chapter table; Ch 8 row — analytical-quantitative register + arithmetic-load risk + multi-component walk cadence).
9. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` — canonical apparatus register decisions (Item 1 inline-integral strip from Ch 8 ✓ intact; Item 14 Cᵢ via Four Gates ✓; Item 7 CIT acronym dropped; Item 12 ARR full-name; Item 13 IPG full-name + acronym).
10. `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` — canonical-terms / named-cases / recurring-stats inventory.
11. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md` — Option D ratified + applied for IPG construction across Ch 2 / Ch 6 / Ch 8.
12. Memory: `tools/memory/feedback_audience_aware_drafting_discipline.md` (v3.1; Pass 2 voice-polish discipline; em-dash discipline ratified 2026-05-21 as load-bearing).
13. Memory: `tools/memory/feedback_em_dash_overuse.md` (em-dash discipline ratified 2026-05-21 during Ch 3 Pass 3.2 F-V3 ratification — "treat em-dash use as a flag requiring active justification, not a default punctuation choice; default to commas/periods/restructure for smoother prose"). **Load-bearing for Ch 8 — 80 em-dashes in 6,375 words is among the corpus's highest densities.**
14. Memory: `feedback_voice_polish_pipeline.md` (dump → sift → polish; active editorial work expected).
15. Memory: `feedback_substance_drives_length.md` (no padding; no cutting to fit; cadence-enacts-content can earn the LLM-pattern flag).
16. Memory: `feedback_named_subject_consent.md` (named-subject discipline — confirmed clean for Ch 8 in Pass 1 §7; no Pass-2 voice-polish moves touch consent).
17. Memory: `feedback_dual_audience_test.md` (layman + specialist; substance-drives-length).
18. Memory: `feedback_verify_stale_memory_claims.md` (verification discipline — chapter line count + cited commits verified against current `origin/main`: 243 lines confirmed; `5fe6af6` + `275b75a` + `cbef9bd` + `bc02767` + `a1e54d9` + `57575b1` + `9befb92` (Ch 8 MED-3 + MED-6 cascade reconciliation Phase C) all resolve on `origin/main`).

**Verification at session start + mid-session re-verification (verify-stale-memory-claims discipline):**
- Session start: `git fetch origin main` → fetched cleanly; `origin/main` HEAD at that point was `57575b1`.
- Mid-session: additional commits landed on `origin/main` while Pass 2 was being drafted, including `9befb92` (Ch 8 MED-3 + MED-6 cascade reconciliation Phase C; 4 ratified spot-fixes at lines 40, 52, 166, 238). Feature branch was rebased onto current `origin/main` HEAD `b31ee2d`; F-V6 line 40 + line 166 verbatim quotations + Option B/C proposed rewrites were updated to reflect the post-`9befb92` cascade-reconciliation Phase C text.
- `wc -l manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` → 243 lines ✓ unchanged by `9befb92` (cascade-reconciliation was in-place word-substitution; no line-count delta).
- All findings below cite line numbers verified via `grep` against the current chapter file (post-`9befb92` cascade-reconciliation state).

---

## §1. Pass-2 scope reminder

Pass 2 audits prose for the LLM tics + voice issues trade-press editors flag. The named-inventory categories applied below:

- **Rule of three** — "A. B. C." constructions across sentence-units; flag if >2 in chapter.
- **Em-dash crutches** — em-dashes used as connective tissue rather than as deliberate parenthetical extension or punch. **Em-dash discipline ratified 2026-05-21 (Ch 3 Pass 3.2 F-V3): treat em-dash use as a flag requiring active justification; default to smoother prose with commas/periods/restructure; cumulative chapter-wide density is itself a voice-polish concern even when individual instances are defensible.**
- **Tidy parallels** — "X did A. Y did B. Z did C." structures across sentences / sections / scenarios.
- **Hedge phrases** — "I will argue that…" / "It seems likely that…" / "Perhaps…"
- **Connective-tissue clichés** — "in short" / "ultimately" / "moreover" / "furthermore" / "that being said" / "going forward" / "at the end of the day" / "to that end".
- **Meta-commentary** — "That is the whole sentence." / "What I mean to say is…" / "Let me explain…"
- **Expository flatness** — "The plain definition is this:" / "Here is what I think:" / "The argument is simple:"
- **Declarative-three-in-a-row** — three short declaratives in succession with no sentence-length variance.
- **Nostalgia / sentimentality tics** — "There are not many people like that anymore" / "Back when…"
- **Cadence repetition** — "It changed me. It humbled me. It made…" patterns.
- **Apparatus residue** — Greek letters, subscripts, integrals, acronyms appearing in body prose where the chapter's analytical-quantitative register prohibits.
- **Register-break to corporate / bureaucratic phrasing** — "at this time," "in this context," "going forward," "at the end of the day," "to that end."
- **First-person register drift** — Ch 8's analytical voice is largely third-person; mid-paragraph "I'll" / "I want" / "I am going to" interjections should be audited for cadence-justification.
- **Section-header parallelism** — multiple "[Adjective] [Noun] Cost" headers in succession can read as tidy-parallel at chapter-architecture scale.

Ch 8's specific emphasis per the Pass 1 §9 carry-forward + the workstream handoff + the chapter's analytical-quantitative-walkthrough register:
(a) Cost-component enumeration cadence at chapter-opening + per-section walk (line 12 "Price the X" five-imperative; section-header parallelism — 8 of 14 headers follow "[Adjective] [Noun] Cost" pattern);
(b) Numerical-claim declarative-three-in-a-row at section conclusions (line 40 "Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone — the most documented component — returns roughly as much as the coal sold for.");
(c) "Different X. Different Y. Different Z. Different W" construction at line 176;
(d) First-person "I" interjections at lines 62, 96, 108, 124, 138, 198, 222 — mid-paragraph register-drift candidates;
(e) Em-dash density chapter-wide (80 em-dashes in 6,375 words; 7 paragraphs with ≥3 em-dashes; line 60 reaches 5 em-dashes — highest single-paragraph density);
(f) "What honest pricing does not mean" three-misreading paragraph-opener anaphora (lines 200, 202, 206);
(g) Closing-section short-declarative cadence (lines 230–240);
(h) YIMBY-engagement passage hedge-phrase + meta-commentary density (lines 180–190);
(i) Rent-seeking paragraph (line 122) voice-register match audit per `bc02767` workstream routing.

---

## §2. Findings — HIGH severity

Issues that actively damage the prose (reader trips over named LLM tic; trade-press editor would flag; copy-editor would catch convention violation).

### F-V1 — Chapter-opening "Price the X" five-fold imperative anaphora at universality-claim site (HIGH)

**Line 12:**
> "Ask the question without political coding, without ideology, and the framework we've been building starts answering it before the argument even begins. Not from preference. From arithmetic. Take one extraction — any extraction, though the one we've been tracing since Chapter 2 will do — and walk it through the full accounting the previous chapters made legible. **Price the health costs. Price the environmental damage. Price the community that bore the weight. Price the foreclosure carried forward to every generation that follows. Price the families dispersed, the knowledge lost, the political work required to keep the whole operation invisible, the acceleration that compressed centuries of resource use into decades.** Add them together. Look at the number. Look at the price on the invoice. Notice the gap."

**Why this flags.** Five consecutive imperative sentences open with "Price the [cost component]," anaphorically setting up the chapter's eight-component walk. Five-in-a-row strict-anaphora with imperative-opener pattern is the chapter's first explicit cadence-pattern at maximum-visibility chapter-opening claim-site position, and the fifth sentence is a four-element compressed catalogue ("the families dispersed, the knowledge lost, the political work required to keep the whole operation invisible, the acceleration that compressed centuries of resource use into decades") that adds substantive bulk without breaking the named-pattern anaphora. The paragraph then continues with three more short declaratives ("Add them together. Look at the number. Look at the price on the invoice. Notice the gap." — four imperatives if "Notice the gap" counts as imperative, three if it counts as declarative). Cumulative: five "Price the X" anaphora + three-or-four short imperatives in the SAME paragraph at the chapter's literal opening.

**Severity rationale.** (a) Chapter-opening claim-site position — sets the chapter's voice register on page 1; trade-press tic-scanner hits this in the first paragraph and registers the cadence before reading the substantive promise. (b) Five-fold strict-anaphora is at the upper end of the chapter's tidy-parallel inventory (the Ch 1 F-V2 cadence-repetition tic was a three-fold; Ch 9 F-V12 was a six-fold; Ch 7 F-V7 was a seven-fold — Ch 8's five-fold sits in the same HIGH-to-MEDIUM band but at chapter-opening, the visibility penalty is amplified). (c) The five-fold + the secondary three-or-four-fold ("Add them together. Look at the number. Look at the price on the invoice. Notice the gap.") in the same paragraph stack two named patterns at the chapter-opening — cumulative-pattern visibility. (d) The chapter's title is "What Things Actually Cost"; the first paragraph's job is to land the universality claim ("everything cost what it actually costs" — the question of line 10), and the five-fold imperative drumbeat is the reach for rhetorical-pivot punch that the verbatim Pass-2 inventory flags as a named LLM-prose move. (e) Direct cadence-cousin to Ch 7 F-V7 (seven-fold "Free X" anaphora — MEDIUM there, held-as-substantively-earned per Mars-ambient-abundance demonstration) and Ch 9 F-V12 (six-fold "the [X] that already exist" — MEDIUM there, Option C compress-to-colon-list recommended); the Ch 8 instance is calibrated HIGH (not MEDIUM) because of the chapter-opening claim-site position + the stacking with the secondary "Add them together / Look / Look / Notice" cluster in the same paragraph.

**Recommended spot-fix (author selects one option):**

- **A. Compress the five "Price the X" anaphora into one colon-list sentence.** *"Take one extraction — any extraction, though the one we've been tracing since Chapter 2 will do — and walk it through the full accounting the previous chapters made legible: price the health costs, the environmental damage, the community that bore the weight, the foreclosure carried forward to every generation that follows, the families dispersed, the knowledge lost, the political work required to keep the whole operation invisible, the acceleration that compressed centuries of resource use into decades. Add them together. Look at the number. Look at the price on the invoice. Notice the gap."* Single colon-list-introduced sentence; preserves all seven enumerated cost-categories; drops the five-fold "Price the" anaphora; the subsequent "Add them together / Look / Look / Notice" cluster remains as cadence-punch-closer that the colon-list earns.
- **B. Break to two sentences with three-then-two anaphora pattern.** *"Price the health costs. Price the environmental damage. Price the community that bore the weight. Then price the foreclosure carried forward to every generation that follows — and price the families dispersed, the knowledge lost, the political work required to keep the whole operation invisible, the acceleration that compressed centuries of resource use into decades."* Drops the strict five-fold to three "Price the X" + one "Then price the X" + one "and price the X" — same imperative-pivot rhythm but breaks the strict anaphoric shape via mid-sentence "Then" + "and" connectives.
- **C. Smoother prose / no anaphora.** *"Take one extraction — any extraction, though the one we've been tracing since Chapter 2 will do — and walk it through the full accounting the previous chapters made legible. Begin with the health costs, then the environmental damage, then the community that bore the weight, then the foreclosure carried forward to every generation that follows. After that come the families dispersed, the knowledge lost, the political work required to keep the whole operation invisible, the acceleration that compressed centuries of resource use into decades. Add them together. Look at the number. Look at the price on the invoice. Notice the gap."* Drops the imperative "Price the X" anaphora entirely; replaces with "Begin with / then / then / then / After that come" sequential-progression frame; preserves the substantive eight-component preview; reads as analytical-walkthrough rather than imperative-drumbeat. Honors the em-dash discipline by not adding em-dashes; uses the em-dash that's already there at "any extraction — though…".
- **D. Hold as-is.** Defensible as deliberate chapter-opening cadence-pivot enacting the chapter's "what follows is a walkthrough" promise; substantively justified by the chapter's eight-component architecture; substance-drives-length governs. **NOT RECOMMENDED** because the chapter-opening claim-site visibility amplifies the named-pattern visibility, and the cumulative stacking with the immediately-following three-or-four-imperative cluster in the same paragraph makes this the chapter's highest-visibility LLM-cadence pattern.

**Recommendation:** Option A (collapse to colon-list). Cleanest drop of the named five-fold anaphoric drumbeat at the chapter-opening claim-site; preserves all substantive content (the seven enumerated cost-categories appear in the same order); preserves the subsequent three-imperative-closer cluster ("Add them together. Look at the number. Look at the price on the invoice. Notice the gap.") which gains rhetorical force from following a flowing colon-list rather than a five-fold drumbeat. Option B is the second-cleanest if author prefers preserving more of the imperative-pivot rhythm.

---

### F-V2 — Four-fold "Different X" + "The same X" cross-scenario sweep closer at line 176 (HIGH)

**Line 176:**
> "**Different industries. Different geographies. Different decades. Different resources. The same mechanism. The same structural gap between what the invoice said and what the extraction actually cost.**"

**Why this flags.** Standalone one-line paragraph; four-fold "Different X" anaphora immediately followed by two-fold "The same X" anaphora — six consecutive short declaratives with strict-parallel single-noun cadence and no sentence-length variance. The "Different X" pattern is a verbatim cousin to the Pass-2 inventory's named tidy-parallel pattern ("He did X. She did Y. They did Z."), extended to four-fold with single-noun completers (industries / geographies / decades / resources). The "The same X" closer is a paired-mirror structure that doubles the named-pattern visibility (six-in-a-row instead of four-in-a-row). The standalone-paragraph framing at line 176 amplifies the cadence-isolation: the prior paragraph (line 174) is a 200+ word dense cross-case-walk (Deepwater / Libby / Baotou / Valdez); line 176 functions as the cross-scenario-summary rhetorical-pivot, and the six-fold strict-parallel-cadence is the named LLM-prose reach for resonance at the rhetorical-pivot moment.

**Severity rationale.** (a) Six-in-a-row strict-parallel anaphora is the chapter's highest declarative-cadence density (excluding F-V1's chapter-opening). (b) Standalone-paragraph framing isolates the cadence-burden — there is nothing else in the paragraph to absorb attention from the pattern. (c) Pass 1 §9 explicitly flagged this construction as a Pass-2 candidate. (d) Direct cadence-cousin to Ch 1 F-V2 ("It changes you. It humbles you. It makes the work feel like the kind of work worth not sleeping for." — HIGH; applied F-V2 cut in Phase C). The Ch 8 instance is calibrated HIGH for the same reason: verbatim shape-match to a named LLM-tic inventory pattern at maximum-visibility rhetorical-pivot position. (e) Trade-press editors with the AI-prose-cadence lens calibrated for 2026 will flag this paragraph specifically; the cadence is recognizable before the substance.

**Recommended spot-fix (author selects one option):**

- **A. Compress to one substantive sentence.** *"Across different industries, geographies, decades, and resources, the same mechanism produces the same structural gap between what the invoice said and what the extraction actually cost."* Single sentence; preserves all six elements (four-fold "Different X" + two-fold "The same X") via comma-serial + main-clause structure; drops the strict-parallel six-fold drumbeat entirely. Reads as cross-scenario-summary in analytical-third-person register.
- **B. Two sentences with internal varied cadence.** *"Different industries, different geographies, different decades, different resources — the same mechanism, and the same structural gap between what the invoice said and what the extraction actually cost."* Single sentence (effectively) with em-dash pivot; preserves the contrastive force of "Different X / The same X"; drops the strict six-sentence pattern. **CAUTION:** uses one em-dash; em-dash discipline ratified 2026-05-21 says treat em-dash as flagged choice — but this em-dash is the load-bearing rhetorical pivot (contrastive "different → same" turn), which is the named justified use; defensible.
- **C. Smoother prose / no em-dashes / no anaphora.** *"The industries differ. The geographies differ. The decades differ. The resources differ. The mechanism does not, and neither does the structural gap between what the invoice said and what the extraction actually cost."* Drops the "Different X" anaphora to "The X differ" anaphora (still parallel but with verb-action rather than adjective-noun); collapses the closing two declaratives into one compound sentence. Drops six-sentence pattern to five (four + one compound); breaks the strict cadence at the closer. Defensible cadence-relief with no em-dashes.
- **D. Cut the line entirely.** Drop line 176 entirely; let the cross-case walk at line 174 carry the cross-scenario-summary work directly into line 178's "The pattern does not stop at what conventionally counts as extraction" sentence. The "Different X / The same X" summary is implicit in the cases already walked at line 174; the rhetorical-pivot punch was the only added work. **CAUTION:** loses the cross-scenario-summary rhetorical pivot — the rest of the chapter assumes the reader has consolidated the same-mechanism-different-context claim by this point. Cut is high-risk for chapter-architecture.

**Recommendation:** Option A (compress to one substantive sentence). Cleanest drop of the named-pattern six-sentence shape; preserves the contrastive "different industries / same mechanism" substantive payoff; reads as analytical cross-scenario summary in the chapter's third-person register; aligns with em-dash discipline (no em-dash introduced). Option C is the second-cleanest if author wants to preserve some of the cadence-pivot force via the "The X differ" anaphora.

---

### F-V3 — Chapter-wide em-dash density — 80 em-dashes in 6,375 words; 7 paragraphs ≥3 em-dashes; max 5 in one paragraph (HIGH)

**Distributed across the chapter.** Quantitative scan:

- **Total em-dashes:** **80** (verified via `grep -c "—"`).
- **Chapter word count:** ~6,375.
- **Density:** ~12.5 em-dashes per 1,000 words — among the highest in the corpus's Pass-2-audited chapters.
- **Paragraphs with ≥3 em-dashes:** 7 (lines 34, 48, 60, 122, 178, 188, 200).
- **Highest single-paragraph density:** **5 em-dashes** at line 60 ("A community doesn't drop to twenty percent..."):
  > "A community doesn't drop to twenty percent of its population without carrying costs. There are infrastructure costs **—** schools, fire departments, water systems, hospitals **—** that must be maintained at some minimum regardless of headcount and whose per-capita burden rises as the headcount falls. There are economic multiplier losses **—** every local business that closed, every institution that couldn't sustain itself, every dollar that didn't circulate locally because the earner left. There are public program costs **—** food stamps, disability payments, Medicaid **—** absorbed by federal and state government in a county that had once generated billions of dollars in coal revenue, almost none of which stayed."

- **Other dense paragraphs:**
  - **Line 188** (4 em-dashes): "What is producing it is the framework's subject. Asset-class consolidation — the rise of institutional landlords; the financialization of single-family rental as an asset class; the documented pricing-coordination patterns that property-management software has enabled across markets, which the U.S. Department of Justice has been investigating since 2022 — operates on top of whatever supply elasticity each local market has. ... The cost severance the chapter prices — the surplus that would otherwise have funded mobility, accumulation, and dynastic transfer, transferred instead to asset owners who are not present at the scale of the local community — is a different mechanism from the supply-side question."
  - **Line 34** (3 em-dashes): "Black lung is the most completely documented externality coal has ever produced — federally tracked, specifically attributable, and severally accumulated onto the public ledger when coal-company bankruptcies discharge the original liability. Chapter 2 walks the federal Black Lung Benefits Program's Trust Fund — its funding gap, debt trajectory, and mechanism of severance — in detail."
  - **Line 48** (3 em-dashes): "Hundreds of thousands of acres across Appalachia are awaiting cleanup — close to a million nationwide. ... The gap — four to six billion — is the severed cost sitting in the federal ledger in plain sight, waiting for a funding source that the law assumed would exist and doesn't."
  - **Line 122** (3 em-dashes, rent-seeking paragraph): "It was shaped, generation after generation, by coal-industry political-economic actors — operators, absentee-mineral-rights holders, industry trade associations — whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record. ... the ledger that counts what those traditions described has been costing, and to whom — the cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number rather than as an actor-attribution problem."
  - **Line 178** (3 em-dashes): "The housing-market pattern Chapter 2 named — nearly half of American renters cost-burdened, the landlord class capturing the surplus that would otherwise have funded mobility — produces the same shape at the household scale. ... The same holds for the Canadian tar sands — Alberta's bitumen operations priced against heavy-crude markets while the ecological damage falls on boreal forests and peatlands, the treaty violations fall on indigenous First Nations whose territories host the operations, and the atmospheric carbon tail follows the combustion wherever the barrels are burned."
  - **Line 200** (3 em-dashes): "Cheap energy — even severely mispriced energy — lifted billions of human beings out of poverty... ... the generations that will absorb the climate costs — these are not hypothetical entities."

**Why this flags.** Per the em-dash discipline ratified 2026-05-21 (Ch 3 Pass 3.2 F-V3): "treat em-dash use as a flag requiring active justification, not a default punctuation choice. Default toward smoother prose with commas/periods/restructure. Cumulative chapter-wide em-dash density is itself a voice-polish concern even when individual instances are defensible." Ch 8's 80-em-dash chapter-wide count is among the highest in the corpus's Pass-2-audited chapters; Ch 7 (the most recent analytical-register chapter audited) had F-V13 chapter-wide em-dash density flagged at MEDIUM with a hold-as-is recommendation. Ch 8's count materially exceeds Ch 7's (Ch 7 reported "at least 25–30" paragraphs with single em-dashes + a handful of ≥3-em-dash paragraphs; Ch 8 has 80 em-dashes total + 7 paragraphs with ≥3 em-dashes + a 5-em-dash paragraph at line 60). The cumulative density is elevated to HIGH per the discipline's explicit guidance that cumulative chapter-wide count IS the voice-polish concern even when individual instances are defensible.

**Per-instance defensibility check:**
- Most em-dashes ARE substantively defensible — appositive-introduction ("Chapter 2 walks the federal Black Lung Benefits Program's Trust Fund — its funding gap, debt trajectory, and mechanism of severance — in detail"), parenthetical-extension ("Hundreds of thousands of acres across Appalachia are awaiting cleanup — close to a million nationwide"), rhetorical-pivot ("Estimates of the annual lobbying spend of the fossil fuel industry alone run into the hundreds of millions of dollars, and that figure captures only the visible fraction" — actually no em-dash; substantive sentence already preserved).
- A few em-dashes are doing connective-tissue work that comma or period would do equally well — e.g., line 200 ("The miners who developed black lung, the communities that collapsed when the coal was exhausted, the children born into a county whose economic future had been extracted before their birth, the generations that will absorb the climate costs **— these are not hypothetical entities.**") — the em-dash here introduces a result-clause that a period + new sentence ("...These are not hypothetical entities.") would carry without loss.
- Line 60's 5 em-dashes are the highest single-paragraph density: three of them are appositive-pair em-dashes (school/fire/water/hospital list; food-stamp/disability/Medicaid list; "every local business that closed..." inset). The middle pair-of-em-dashes pattern is the most reducible (three lists with three em-dash-bracketed insets in a single paragraph reads as repeated formula).

**Severity rationale.** (a) Cumulative chapter-wide count is among the corpus's highest at ~12.5 per 1,000 words. (b) Em-dash discipline ratified 2026-05-21 explicitly says cumulative density is the concern even when individual instances defensible. (c) Line 60's 5-em-dash density is the chapter's most editor-visible single-paragraph flag. (d) Multiple ≥3-em-dash paragraphs cluster across the chapter (lines 34, 48, 60, 122, 178, 188, 200) — pattern is chapter-wide habit, not isolated incident. (e) Ch 7 F-V13 was calibrated MEDIUM at hold-as-is; Ch 8's count materially exceeds Ch 7's, calibrated to HIGH. (f) Trade-press editors with em-dash-discipline lens will flag this chapter specifically; the analytical-quantitative register the chapter requires can do its appositive-clarification work through colon, comma, or restructured sentences.

**Recommended spot-fix (author selects one option):**

- **A. Targeted reduction at the four highest-density paragraphs.** Audit and reduce em-dash count at lines 60 (5 → 2 or 3), 188 (4 → 2), and lines 34 + 48 + 122 + 178 + 200 (3 → 2 each) by converting em-dash-bracketed insets to colon-list, comma-clause, or split-sentence forms wherever the work would be carried equally well. Estimated chapter-wide drop: 80 → ~55–60. Sample fixes:
  - **Line 60 (5 → 3):** Convert two of the three appositive-pair em-dashes to colon-list form. *"There are infrastructure costs: schools, fire departments, water systems, hospitals — costs that must be maintained at some minimum regardless of headcount and whose per-capita burden rises as the headcount falls. There are economic multiplier losses — every local business that closed, every institution that couldn't sustain itself, every dollar that didn't circulate locally because the earner left. There are public program costs: food stamps, disability payments, Medicaid — absorbed by federal and state government in a county that had once generated billions of dollars in coal revenue, almost none of which stayed."* Drops 5 em-dashes to 3; preserves all substantive content; uses colon-for-list-introduction (the most analytical-register-appropriate alternative).
  - **Line 200 (3 → 1):** Convert two of the three em-dashes to comma + period. *"Cheap energy, even severely mispriced energy, lifted billions of human beings out of poverty, and no responsible reader of this book should accept an account that pretends otherwise. ... The miners who developed black lung, the communities that collapsed when the coal was exhausted, the children born into a county whose economic future had been extracted before their birth, the generations that will absorb the climate costs. These are not hypothetical entities."* Drops 3 em-dashes to 1; the "Cheap energy — even severely mispriced energy" pair becomes a comma-pair (parenthetical hedge can carry equally well in commas); the closing "climate costs — these are not hypothetical entities" becomes period + new sentence.
  - **Line 188 (4 → 2):** Convert two of the four em-dash pairs to semicolon or parenthetical-comma. *"What is producing it is the framework's subject. Asset-class consolidation (the rise of institutional landlords; the financialization of single-family rental as an asset class; the documented pricing-coordination patterns that property-management software has enabled across markets, which the U.S. Department of Justice has been investigating since 2022) operates on top of whatever supply elasticity each local market has. ... The cost severance the chapter prices — the surplus that would otherwise have funded mobility, accumulation, and dynastic transfer, transferred instead to asset owners who are not present at the scale of the local community — is a different mechanism from the supply-side question."* Drops 4 em-dashes to 2; the asset-class-consolidation inset becomes parenthetical-comma-bracketed (the inset is information-dense and parenthesis is the analytical-register-appropriate form for dense information that doesn't carry pivot-weight); the cost-severance pair stays em-dash-bracketed (the pivot weight is the chapter's load-bearing claim — the parenthetical here IS the chapter's policy-implication thesis, so em-dash punch is justified). Estimated total chapter drop: ~25 em-dashes.

- **B. Comprehensive sweep: target ~30% chapter-wide reduction (80 → ~55).** Audit every em-dash and convert to comma / period / restructure wherever the work would be carried equally well by smoother prose. Preserve em-dashes only at: (i) load-bearing rhetorical pivots (chapter-spine claim-pivots like line 122's "the cost-bearing magnitudes... — the cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number rather than as an actor-attribution problem"); (ii) parenthetical-pair information that genuinely needs strong visual offset; (iii) sentence-final-clause-punch where the em-dash is the only way the rhythm works. Heavier rewrite; affects ~25–30 sentences. Reads as smoother analytical prose chapter-wide.

- **C. Spot-audit the three highest-density paragraphs only (lines 60, 122, 188).** Apply the line-60 (5 → 3) + line-188 (4 → 2) + line-122 (3 → 2) fixes only; hold lines 34 + 48 + 178 + 200 + other em-dash usages as-is. Estimated chapter-wide drop: 80 → ~74. Light-touch reduction targeted at the densest instances only; addresses the most editor-visible density flags without chapter-wide rewrite.

- **D. Hold as-is per substance-drives-length + Ch 7 F-V13 cousin disposition.** Cite Ch 7 F-V13's recommendation Option A hold-as-is as precedent. **NOT RECOMMENDED** per the em-dash discipline ratified 2026-05-21, which explicitly distinguishes Ch 8-style chapter-wide cumulative density as the concern even when individual instances defensible. The Ch 7 F-V13 disposition cited substance-drives-length + Ch 9 F-V15 calibration; the em-dash discipline ratification post-dates both and updates the calibration. Holding as-is reads as not heeding the explicit discipline that ratified during Ch 3 Phase C-β.

**Recommendation:** Option B (comprehensive sweep). Honors the em-dash discipline ratified 2026-05-21 most directly; reduces chapter-wide cumulative density to ~55 (~30% reduction); preserves em-dashes only at load-bearing rhetorical-pivot + parenthetical-pair + sentence-final-punch sites; reads as smoother analytical prose chapter-wide. Option A is the second-best if author prefers targeted-paragraph reduction (lower-cost; addresses ~5–8 highest-density paragraphs only; estimated drop to ~55–60). Option C is the lightest-touch if author prefers minimum-rewrite (addresses only the three highest-density paragraphs; drop to ~74).

---

### F-V4 — "I'll [verb]" mid-paragraph first-person interjection cadence — 5 instances at conservative-placeholder sites (HIGH)

**Five instances** at cost-component conservative-floor-assignment sites:

- **Line 62:** *"Economists who study regional collapse have methodologies for pricing this; the figures they produce for sustained regional decline sit in the range of five to fifteen dollars per ton of extracted coal when allocated to the extraction that drove the collapse. **I'll use the low end. Five dollars per ton.**"*
- **Line 96:** *"**I'll use two dollars per ton as a conservative placeholder.** The reader can decide whether two dollars per ton of coal, multiplied across sixty years of extraction, represents anything like a fair accounting for what it cost a generation to be born in a county that had been priced at nothing."*
- **Line 108:** *"**I'll price this component at one dollar per ton.** It is not the point of the chapter. But it belongs in the accounting because the Commons Inversion Test surfaces it..."*
- **Line 124:** *"**I'll assign one dollar per ton to this component** — a floor so low it is almost certainly an undercount, chosen to keep the running total conservative. The reader who has followed the argument this far can adjust."*
- **Line 138:** *"**I'll assign this component two dollars per ton.** Again, conservative, almost certainly an undercount."*

**Why this flags.** Five mid-paragraph first-person interjections with strict-parallel "I'll [verb] [number] dollar(s) per ton" shape across five of the eight cost-component sections (the four "harder components" sections — Lineage Labor, Knowledge and Cultural, Political Capture, Temporal Displacement — plus Community Disruption). Pass 1 §9 explicitly flagged the first-person register as a Pass-2 audit candidate: cross-chapter inventory §8 marks Ch 8 as "0 first-person line-starts" — but the chapter does have mid-paragraph "I'll use" / "I'll price" / "I'll assign" first-person interjections that read as a chapter-wide habit. Five-instance occurrence with strict-parallel imperative cadence ("I'll [verb] [number]") at the chapter's eight-component-walk's conservative-floor-assignment moments is the named tidy-parallel pattern.

The five-fold "I'll" interjections enact the chapter's "conservative-throughout" methodological discipline (line 28: "What follows is conservative throughout. Where estimates have a range, I use the lower figure"). The cadence is rhetorically purposeful — each interjection performs the author's accountability-on-the-page move (the author personally vouching for the chosen floor). But the five-fold occurrence shifts register from analytical-third-person to first-person-conversational at five widely-spaced points across the chapter, and the strict-parallel shape ("I'll [verb] [number]") reads as a tic-pattern at chapter-wide scale.

**Severity rationale.** (a) Five-fold occurrence of the same first-person interjection cadence across five different sections is a chapter-wide pattern, not isolated incidents. (b) The strict-parallel "I'll [verb] [number] dollar(s) per ton" shape across all five instances is the named tidy-parallel pattern at section-conclusion sites. (c) Pass 1 §9 explicitly flagged the first-person register as a Pass-2 candidate. (d) Cross-chapter inventory §8 marked Ch 8 as "0 first-person line-starts" — the count missed the mid-paragraph register-drift; the actual register-load is substantial. (e) The chapter's voice elsewhere is largely third-person analytical (the cost-component walks; the cross-case sweep; the YIMBY engagement; the misreading-defenses); the "I'll" interjections are register-drift away from the dominant voice. (f) Calibrated HIGH (not MEDIUM) because the five-fold count + the strict-parallel cadence + the chapter-wide distribution combine into a chapter-architecture-visible pattern that trade-press editors will register as accumulating habit.

**Recommended spot-fix (author selects one option):**

- **A. Convert all five to third-person analytical register.** Replace "I'll use" / "I'll price" / "I'll assign" with "The chapter uses" / "The chapter prices" / "The accounting assigns" or with passive-voice constructions ("This component is priced at..." / "This component is assigned..." / "This component is conservatively floored at..."). Sample fixes:
  - Line 62: *"The chapter uses the low end. Five dollars per ton."*
  - Line 96: *"This component is priced at two dollars per ton as a conservative placeholder."*
  - Line 108: *"This component is priced at one dollar per ton."*
  - Line 124: *"This component is conservatively assigned one dollar per ton — a floor so low it is almost certainly an undercount, chosen to keep the running total conservative."*
  - Line 138: *"This component is conservatively assigned two dollars per ton. Again, almost certainly an undercount."*
  
  Drops the five-fold first-person interjection cadence chapter-wide; aligns Ch 8 with its dominant analytical-third-person voice; preserves the conservative-floor-assignment substantive payoff at each section conclusion.
- **B. Vary the five interjections — retain one or two; convert the others.** Hold the first (line 62 "I'll use the low end. Five dollars per ton.") as the chapter's establishing first-person-accountability move; convert the other four to third-person analytical. Drops the strict-parallel cadence chapter-wide; preserves one first-person voice-token at the section where it has the strongest substantive payoff (Community Disruption Cost is the chapter's first non-numerically-anchored conservative-floor moment; the first-person interjection establishes the chapter's accountability discipline).
- **C. Compress the five interjections into a single methodological statement upstream.** Add a sentence at line 28 (the chapter's existing methodological-statement paragraph): *"What follows is conservative throughout. Where estimates have a range, I use the lower figure. Where an externality is contested, I omit it. **For each cost component below, the chapter assigns the conservative floor and notes the methodological judgment behind the assignment.**"* Then convert all five mid-paragraph "I'll [verb] [number]" interjections to third-person ("This component is assigned [number]"). Most-aggressive sweep; restructures the chapter's voice-architecture around the methodological statement at line 28; eliminates the five-fold pattern entirely.
- **D. Hold as-is.** Defensible as deliberate authorial-accountability voice-move; the five-instance pattern enacts the chapter's "conservative throughout" methodological discipline at each section conclusion; cross-chapter inventory §8's "0 first-person line-starts" count is technically accurate (line-START is the inventory's measure); cumulative register-drift at chapter scale is genuine but defensible as memoir-adjacent analytical voice. **NOT RECOMMENDED** because the five-fold strict-parallel pattern is the named tidy-parallel tic at chapter-wide scale, and the register-drift away from the chapter's dominant analytical-third-person voice is itself a voice-polish concern.

**Recommendation:** Option B (retain one; convert the other four). Cleanest balance: preserves the chapter's accountability-on-the-page move at one strong site (line 62, the first non-numerically-anchored conservative-floor moment); converts the four subsequent interjections to analytical-third-person; drops the strict-parallel five-fold cadence; preserves chapter-architecture-voice consistency. Option A is the simplest if author wants total register-cleanup. Option C is the most architectural if author wants to restructure the methodological framing entirely.

---

## §3. Findings — MEDIUM severity

Patterns that flag but don't stop the prose. Author discretion. Many are substantively-earned and defensible as analytical-accounting cadence enacting the chapter's eight-component walk; flagged so each can be reviewed instance-by-instance to confirm it earns its space rather than reading as LLM-pattern in aggregate.

### F-V5 — Section-header parallelism — 8 of 14 headers follow "[Adjective] [Noun] Cost" pattern (MEDIUM)

**Section headers in Ch 8 (14 total):**

1. ### The coal, again (line 22) — narrative
2. ### Direct Health **Cost** (line 32) — pattern
3. ### Environmental Degradation **Cost** (line 44) — pattern
4. ### Community Disruption **Cost** (line 56) — pattern
5. ### Foreclosure **Cost** (line 68) — pattern
6. ### Lineage Labor **Cost** (line 84) — pattern
7. ### Knowledge and Cultural **Cost** (line 100) — pattern
8. ### Political Capture **Cost** (line 112) — pattern
9. ### Temporal Displacement **Cost** (line 128) — pattern
10. ### The sum (line 142) — narrative
11. ### The pattern made legible (line 172) — narrative
12. ### What honest pricing does *not* mean (line 196) — narrative
13. ### The brief extrapolation (line 210) — narrative
14. ### The closing line (line 226) — narrative

**Why this flags.** Eight of fourteen section headers follow the "[Adjective] [Noun] **Cost**" pattern — a clear chapter-architecture parallel. Each of the eight cost-component sections gets its own header in the same shape: an analytical-taxonomy convention that helps the reader navigate the eight-component walk. The remaining six section headers (narrative-register) break the pattern at structural pivot points (chapter-opening reframe; sum-up; cross-case sweep; misreading-defenses; civilizational extrapolation; closing). The parallel is structurally load-bearing — it IS the eight-component walk's navigation.

But: eight headers in strict-parallel cadence across a single chapter is the named tidy-parallel pattern at chapter-architecture scale. A trade-press editor scanning the table of contents or the chapter's structural cadence will register the eight-in-a-row repetition; the parallelism reads as analytical-taxonomy-rigorous on the page but as formulaic-list at chapter-architecture scale.

**Severity rationale.** (a) Substantively load-bearing — the eight-parallel headers ARE the eight-component walk's navigation; the cost-categorization taxonomy depends on the parallel form. (b) Pattern enacts content (each header names a Cost; the parallel signals "this is one of the framework's admitted Cᵢ components"). (c) The header-as-taxonomy convention is editor-tolerable in analytical chapters; a trade-press editor accustomed to academic-adjacent analytical prose will read the parallel as discipline rather than as tic. (d) MEDIUM (not HIGH) because the parallel is content-enactive + structurally load-bearing; breaking it would weaken the eight-component walk's navigation; substance-drives-length governs.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively load-bearing chapter-architecture parallel; the eight-component walk's navigation depends on the parallel shape; substance-drives-length governs. Trade-press-defensible as analytical-taxonomy convention.
- **B. Vary 1–2 headers for cadence-relief.** Convert "Lineage Labor Cost" to "Lineage Labor" (drops "Cost"; the chapter opens with "Now the harder components" so the "Cost" suffix isn't strictly necessary on every header); convert "Knowledge and Cultural Cost" to "Knowledge and Culture" (drops "Cost" + adjective-noun symmetry). Two-header break across the eight; preserves the parallel as default with deliberate variation. **CAUTION:** breaks the analytical-taxonomy convention; the eight-component walk's framework-Cᵢ register is partially encoded in the consistent "Cost" suffix — author judgment on whether the consistency is more valuable than the variance.
- **C. Restructure the eight headers to numbered analytical-list form.** *"### 1. Direct Health" / "### 2. Environmental Degradation" / "### 3. Community Disruption" / ..." Drops the "Cost" suffix; replaces analytical-taxonomy parallelism with numbered-list register. Heavier restructure; reads more academic-textbook than analytical-essay. **NOT RECOMMENDED** for trade-press register.

**Recommendation:** Option A (hold as-is). Substantively load-bearing chapter-architecture parallel; the parallel IS the eight-component walk's navigation; substance-drives-length governs. Trade-press-defensible as analytical-taxonomy convention. If Pass 3 audience-load testing surfaces the parallel-cadence as a flag for any specific trade-press reader, revisit at that point.

---

### F-V6 — Multi-instance "Numerical figure. Against a market price. [Conclusion]." declarative-three at section-conclusion sites (MEDIUM)

**Three instances** at section-conclusion synthesizing moments:

- **Line 40:** *"**Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone — the most documented component — already returns most of what the coal sold for.**"* (post-cascade-reconciliation `9befb92`).
- **Line 74:** *"**Five hundred and forty-four dollars. Against a market price that has oscillated between four dollars and a hundred and forty dollars over the life of the industry.** The carbon term alone — before any of the other seven components are added — exceeds every era's market price for a ton of coal, by a factor running from roughly four against today's market peak to more than a hundred against the 1960 mine-mouth."*
- **Line 166:** *"Total: $558 per ton. **Against a 1960 market price of four to five dollars. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for.**"* (post-cascade-reconciliation `9befb92`).

**Why this flags.** Three section-conclusion sites use the same numerical-rhetorical-pivot cadence: *"[Number/total]. Against [market-price comparison]. [Conclusion]."* The pattern is the chapter's signature analytical-pivot move (compare honest cost against market price; name the gap). Pass 1 §9 flagged line 40's instance specifically as a Pass-2 candidate.

The cadence is substantively earned at each site — the comparison-against-market-price IS the chapter's load-bearing argument (cost severance = honest cost - market price). But three instances of the same numerical-pivot rhythm across three different sections (lines 40, 74, 166) is the named tidy-parallel pattern at chapter-architecture scale: the chapter trains the reader to expect "[Number]. Against [market price]. [Gap]" at every section-conclusion, and a trade-press reader will pick up the cadence repetition.

The line 166 instance is the most concentrated: three "Against [market price]" anaphoric sentences in a row, immediately following the headline "$558 per ton" total — six declaratives in succession at the chapter's headline numerical-climax moment. Direct cadence-cousin to F-V2's "Different X / The same X" six-fold at line 176 (which sits 10 lines later in the chapter — the chapter has TWO six-fold declarative-cadence sites within 10 lines at the chapter's two rhetorical-pivot peaks).

**Severity rationale.** Substantively-earned analytical-pivot cadence at each site; each instance does the chapter's load-bearing cost-severance-against-market-price comparison work. But three instances of the same numerical-pivot rhythm across three sections is the named pattern at chapter-scale. The line 166 instance + the line 176 instance create a chapter-climax-region cadence-density cluster that compounds the visibility. MEDIUM (not HIGH) because each instance is substantively earned + the comparison-against-market-price IS the chapter's load-bearing analytical move; not LOW because three-in-a-chapter + the line 166 concentration warrant author review.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively earned numerical-pivot cadence at each site; the comparison-against-market-price IS the chapter's load-bearing analytical move; substance-drives-length governs. Calibrated as chapter-signature analytical-pivot rather than as LLM-cadence reach.
- **B. Vary the line 166 instance only (the highest-density of the three).** Convert the three "Against [market price]" anaphoric sentences to a single compound sentence. *"Total: $558 per ton. Against a 1960 market price of four to five dollars, $40 to $140 today depending on grade — against every price coal has ever sold for."* Drops three sentences to one (with em-dash pivot to "against every price"); preserves the substantive claim; drops the three-fold anaphoric drumbeat at the chapter's headline-figure moment. **CAUTION:** uses one em-dash; the em-dash here is the rhetorical-pivot punch (the universalizing "every price" turn), which is the named justified use. Reduces F-V3 chapter-wide em-dash count by 0 (line 166 currently has no em-dashes, so this adds 1).
- **C. Vary the line 166 instance, no em-dash version.** *"Total: $558 per ton. Against a 1960 market price of four to five dollars, $40 to $140 today depending on grade, and against every price coal has ever sold for."* Single sentence with comma-serial; drops the three-fold pattern; no em-dash introduced. Less rhetorical punch than Option B but cleaner em-dash discipline.
- **D. Vary line 40 OR line 74 to break the chapter-wide pattern.** Hold line 166 (the headline-figure moment); vary one of the two earlier instances (line 40 OR line 74) to break the cross-section pattern at chapter scale. Sample: line 40 *"That figure — two to four dollars per ton — already approaches the four-to-five-dollar market price the coal cleared at in 1960. Direct health alone, the most documented component, returns roughly as much as the coal sold for."* Drops the strict numerical-pivot cadence at line 40 while preserving lines 74 + 166 as the load-bearing instances. **CAUTION:** uses two em-dashes; defensible parenthetical-pair work but contributes to F-V3 em-dash count.

**Recommendation:** Option C (vary line 166 only, no em-dash). Lightest-touch fix targeting the highest-density instance (the three-fold "Against [market price]" cluster); honors em-dash discipline; preserves the chapter-signature numerical-pivot cadence at lines 40 + 74 where it's load-bearing without compounding to chapter-headline three-fold. Option A is defensible if author calibrates the chapter-signature cadence as analytically load-bearing.

---

### F-V7 — Methodological-statement parallel-structure paragraph at line 28 (MEDIUM)

**Line 28:**
> "**What follows is conservative throughout. Where estimates have a range, I use the lower figure. Where an externality is contested, I omit it. The goal is not a ceiling. The goal is a floor — the smallest honest number the framework can defend — and to show that even the floor sits orders of magnitude above the price that cleared the market.**"

**Why this flags.** Pass 1 §9 explicitly flagged this paragraph as a Pass-2 candidate ("Methodological-statement framings. ... multiple parallel-structure clauses + tidy-parallel risk"). The paragraph contains: (a) a methodological-statement opener ("What follows is conservative throughout"); (b) two anaphoric "Where [conditional], I [action]" sentences in succession (the named tidy-parallel pattern); (c) two anaphoric "The goal is [X]" sentences in succession (named declarative-parallel pattern); (d) the closing extended sentence with one em-dash pair. Cumulative: five declarative sentences with two anaphoric pairs + one mixed-cadence closer.

The methodological-statement IS the chapter's discipline-disclosure paragraph (line-28 is the explicit conservative-floor commitment that the chapter's eight-component arithmetic depends on). The cadence enacts the methodological-commitment force: "this is conservative; here are two ways it's conservative; here is the goal; here is the goal again, sharpened." But the two-fold + two-fold + closer shape is the named tidy-parallel pattern; substantively earned + visibly cadenced.

**Severity rationale.** Substantively load-bearing — the methodological-disclosure is what the chapter's arithmetic stands on; the cadence enacts methodological commitment. The two short anaphoric pairs ("Where X, I Y" + "The goal is X. The goal is Y") + closer are the named pattern but each does substantive disciplinary work. MEDIUM (not HIGH) because the substantive payoff (chapter's methodological commitment) justifies the cadence; not LOW because the two-fold + two-fold + closer stacking in a single paragraph is the kind of pattern that compounds with F-V1 (chapter-opening five-fold) + F-V4 (five-fold first-person interjections) at chapter scale.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively load-bearing methodological-disclosure; cadence enacts methodological commitment; the two-fold + two-fold + closer shape is the chapter's discipline-statement signature. Substance-drives-length governs.
- **B. Collapse the two "Where X, I Y" sentences into one compound.** *"What follows is conservative throughout. Where estimates have a range I use the lower figure, and where an externality is contested I omit it. The goal is not a ceiling but a floor — the smallest honest number the framework can defend — and to show that even the floor sits orders of magnitude above the price that cleared the market."* Drops two-fold to one compound; collapses the "The goal is not X. The goal is Y" two-fold to one "not X but Y" contrastive; preserves all substantive content; reads as smoother methodological-statement.
- **C. Smoother prose / no em-dashes.** *"What follows is conservative throughout. Where estimates have a range, the chapter uses the lower figure, and where an externality is contested, the chapter omits it. The goal is not a ceiling but a floor: the smallest honest number the framework can defend. The point is to show that even the floor sits orders of magnitude above the price that cleared the market."* Drops two-fold anaphora; converts to "the chapter" third-person (cross-reference with F-V4 register-conversion recommendation); converts em-dash pair to colon + period; preserves substantive content. Single combined fix addressing F-V4 + F-V3 + F-V7 patterns at this paragraph.

**Recommendation:** Option B (collapse two-fold pairs). Lightest-touch fix preserving methodological-commitment substance + first-person register; drops the strict parallel-cadence shape; preserves the em-dash pair (defensible as the chapter's load-bearing methodological-claim pivot). If author ratifies F-V4 Option A (third-person register-conversion chapter-wide), Option C provides a coordinated fix that also converts this paragraph to third-person.

---

### F-V8 — YIMBY-engagement passage hedge-phrase + meta-commentary density (lines 180–190) (MEDIUM)

**Five-paragraph passage** at the chapter's most argumentative engagement:

- **Line 180:** *"The housing finding above will encounter a serious objection from a particular direction, and the framework cannot earn the integration without engaging it specifically. The objection is that housing costs are driven by zoning restrictions on supply, not by landlord-surplus capture..."*
- **Line 182:** *"The serious form of the objection is not weak. The empirical literature on housing-supply restriction is substantial..."*
- **Line 184:** *"Each of these claims is sound on its own terms. The framework's response is not to deny supply restrictions or to treat zoning reform as unimportant; it is to recognize that supply-side analysis and rent-extraction analysis are operating at different levels of the same case, and that engaging only one of them produces incomplete diagnosis."*
- **Line 186:** *"Supply restrictions explain why total housing units have not grown in proportion to demand in high-cost metropolitan areas. They do not explain why, when units exist, the rent the units command captures a structurally larger share of household income than housing rent captured fifty years ago..."*
- **Line 188:** *"What is producing it is the framework's subject. ... A framework that treats them as the same mechanism would be wrong; a framework that prices only one of them would be incomplete."*
- **Line 190:** *"What survives engagement with the YIMBY objection is the chapter's structural finding. Supply restriction is real and zoning reform is the appropriate response to it; rent-extraction is also real and a different accountability architecture is the appropriate response to it; the two are operating simultaneously and the policy response has to address both. The housing finding the chapter prices is the second mechanism, and it does not collapse into the first."*

**Why this flags.** Pass 1 §9 explicitly flagged this passage as a Pass-2 candidate ("YIMBY-engagement passage (lines 179–189). This is the chapter's most argumentative passage. Pass 2 should test voice for: hedge-phrase density ('the framework cannot earn the integration without engaging it specifically'), connective-tissue clichés ('Each of these claims is sound on its own terms'), and meta-commentary ('the framework's response is not to deny ...')").

Pass 2 verification:
- **Hedge-phrase density:** "the framework cannot earn the integration without engaging it specifically" (line 180) — borderline; reads as load-bearing methodological-commitment, not hedge-uncertainty. Distinct from named hedge inventory ("I will argue that…" / "It seems likely that…" / "Perhaps…"). **NOT a HIGH hedge-tic;** the phrasing is substantive.
- **Connective-tissue clichés:** "Each of these claims is sound on its own terms" (line 184) — borderline; reads as deliberate concessive-pivot before counter-argument. NOT a named connective-tissue cliché ("in short" / "ultimately" / "moreover" / "furthermore" / "that being said"). Defensible.
- **Meta-commentary:** "The framework's response is not to deny supply restrictions or to treat zoning reform as unimportant; it is to recognize that..." (line 184) + "What survives engagement with the YIMBY objection is the chapter's structural finding" (line 190) — both are chapter-spine self-reference (the framework + the chapter as analytical subjects). Reads on the edge of the named meta-commentary pattern but each does substantive structural-engagement work; the chapter is performing an argument-with-an-objector and the meta-commentary IS the argument-performance.

Cumulative pattern across the five-paragraph passage: the chapter shifts to argumentative-engagement register, and the cumulative effect of multiple "the framework cannot..." / "the framework's response..." / "the chapter's structural finding..." / "the housing finding the chapter prices..." / "what survives engagement..." reads as chapter-spine self-reference density. Each instance does substantive argument-with-objector work; the cumulative-density is the flag.

**Severity rationale.** Substantively earned — the YIMBY engagement is the chapter's most direct argument-with-an-objector; the chapter-spine self-reference is the genre-conventional analytical-essay engagement-with-objection move. No instances match the named hedge / connective-tissue / meta-commentary verbatim inventory. MEDIUM (not HIGH) because the chapter-spine-self-reference cumulative density is the named pattern at five-paragraph passage scale, but each instance is substantively earned + the cadence enacts the chapter's argument-with-objector posture; not LOW because Pass 1 §9 explicitly flagged the passage for Pass-2 testing.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively earned argument-with-objector engagement; the chapter-spine self-reference IS the argument-performance; no instance matches the named verbatim hedge / cliché / meta-commentary inventory. Substance-drives-length governs. Pass 1 §9's flag was for testing, not for required spot-fix; Pass 2 verifies the passage holds clean against the named tic-inventory.
- **B. Vary 1–2 of the chapter-spine self-references for cadence-relief.** Convert "the framework cannot earn the integration without engaging it specifically" (line 180) to a more concrete framing: *"This objection has to be engaged specifically before the housing finding can be integrated into the chapter's cost-severance argument."* Drops "the framework cannot earn the integration" abstract-self-reference to concrete-argumentative-engagement. Single-paragraph fix; addresses the most-abstract self-reference; preserves the rest of the passage's chapter-spine-self-reference cadence at sites where it's substantively earned.
- **C. Compress line 184 to drop the connective-tissue near-cliché.** *"The framework's response is to recognize that supply-side analysis and rent-extraction analysis are operating at different levels of the same case, and that engaging only one of them produces incomplete diagnosis."* Drops "Each of these claims is sound on its own terms. The framework's response is not to deny supply restrictions or to treat zoning reform as unimportant; it is to recognize..." opening (which is the most concessive-hedge-flavored framing); preserves the substantive engage-with-difference move. Two-sentence compression at the passage's argumentative pivot.

**Recommendation:** Option A (hold as-is). Substantively earned argument-with-objector engagement; chapter-spine self-reference cumulative density is the genre-conventional move; no instance matches the named verbatim inventory. Pass 3 audience-load testing will surface whether the cumulative-density flags for any specific Tier-1 trade-press / YIMBY-aware reader (per §7 forward-flag); if Pass 3 surfaces a flag, revisit at that point. Option B is the lightest-touch fix if author wants to address the most-abstract chapter-spine self-reference at line 180.

---

### F-V9 — Closing-section short-declarative + "These questions are real" cadence at lines 228–236 (MEDIUM)

**Closing-section three-paragraph passage:**

- **Line 228 (chapter-rhetorical-question opening):** *"What happens if an entire global economy begins to reprice at honest rates? Resource by resource, sector by sector, country by country? What happens to energy costs in the short term, and in the medium term, and in the new equilibrium? Who absorbs the transition? What happens to a household in the bottom forty percent of the income distribution when essentials rise by forty percent? Where does the pricing surplus go, and who decides? What does the economy look like on the other side, and is that economy still recognizably capitalist?"*
- **Line 230:** *"**These questions are real.** The framework answers them — the mathematics produces specific results, the simulations run in recognizable directions, the distributional crisis and the structural necessity of a universal floor emerge with a clarity that is neither ideological nor optional. They are, all of them, consequences of the pricing exercise this chapter has just performed on a single ton of coal."*
- **Line 232:** *"**They are also outside the scope of this book.**"*
- **Line 234:** *"This book's job is to make the invisible visible. Chapter 1 through Chapter 8 have done that. Chapter 9 sketches the direction a civilization committed to honest accounting would move. Chapter 10 closes with the miner, the waterman, and the off-world administrator recognizing each other across the distance the mechanism was designed to maintain."*

**Why this flags.** Pass 1 §9 explicitly flagged the closing section as a Pass-2 candidate ("Closing section (lines 225–241) — strong rhetorical close + many short declaratives ('Resource by resource, sector by sector, country by country'; 'is that economy still recognizably capitalist?'; 'These questions are real'; 'They are also outside the scope of this book'").

Multiple cadence-patterns stacked in the closing section:
- **Line 228:** six-question rhetorical sequence with internal three-fold "Resource by resource, sector by sector, country by country" (tidy-parallel) + two-fold "in the short term, and in the medium term" (compressed-tidy-parallel).
- **Line 230:** "These questions are real" three-word standalone-sentence opener + extended explanatory sentence with three-element comma-serial ("the mathematics produces specific results, the simulations run in recognizable directions, the distributional crisis and the structural necessity of a universal floor emerge with a clarity that is neither ideological nor optional").
- **Line 232:** "They are also outside the scope of this book" — standalone-sentence one-line paragraph (high-visibility cadence-isolation).
- **Line 234:** "Chapter 1 through Chapter 8 have done that. Chapter 9 sketches... Chapter 10 closes with..." — chapter-reference rule-of-three at chapter-forward-pointing site.

Cumulative: the closing section's analytical-rhetorical register depends on the short-declarative cadence to land the "questions presuppose the framework / answers are outside scope" structural move. The cadences are substantively earned but cumulatively dense. The "Resource by resource, sector by sector, country by country" three-fold + the line 232 standalone + the line 234 Chapter-rule-of-three are the most editor-visible flags.

**Severity rationale.** Substantively earned closing-section rhetorical-close cadence; each instance does load-bearing structural work (rhetorical questions raise the civilizational-scale implication; standalone declarative lands the scope-limit; Chapter rule-of-three closes the chapter with a forward-pointer to Ch 9 + Ch 10). MEDIUM (not HIGH) because each instance is substantively earned + the cumulative density is the chapter-architecture pivot's rhetorical-close signature; not LOW because Pass 1 §9 explicitly flagged + the cumulative count of cadence-patterns in the closing section is high.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively earned closing-section rhetorical-close cadence; each instance does load-bearing structural work; the cumulative density is the chapter-architecture's rhetorical-close signature. Substance-drives-length governs. Direct cadence-cousin to Ch 7 F-V12 (chapter-closing three-imperative — held in Ch 7 Pass 2 recommendation per Ch 1 F-V14 cousin).
- **B. Vary the line 228 "Resource by resource, sector by sector, country by country" three-fold.** *"What happens if an entire global economy begins to reprice at honest rates, resource by resource and sector by sector?"* Drops three-fold to two-fold; compresses six-question opening to five-question; preserves the rhetorical-question structure but breaks the three-fold pattern. Single-paragraph fix.
- **C. Vary the line 234 "Chapter 1 / Chapter 9 / Chapter 10" rule-of-three.** *"Chapter 1 through Chapter 8 have done that. The next two chapters sketch the direction a civilization committed to honest accounting would move, and close with the miner, the waterman, and the off-world administrator recognizing each other across the distance the mechanism was designed to maintain."* Drops "Chapter 9 sketches... Chapter 10 closes with..." anaphoric chapter-reference pair to a single compound sentence; preserves the substantive forward-pointer; breaks the chapter-rule-of-three. Two-sentence compression.

**Recommendation:** Option A (hold as-is). Closing-section rhetorical-close cadence is substantively earned + cadence-as-content; Ch 7 F-V12 chapter-closing-cadence calibration applies (held in Ch 7 Pass 2). If author wants targeted relief, Option B is lightest-touch (single-paragraph fix at the most cadence-dense rhetorical-question instance).

---

### F-V10 — "So I am not going to compress it. I am going to name it and leave it." declarative-pair at line 222 (MEDIUM)

**Line 222:**
> "**So I am not going to compress it. I am going to name it and leave it.**"

**Why this flags.** Standalone two-sentence paragraph; first-person declarative-pair with "I am [not] going to [verb]" anaphora. Pass 1 §9 flagged this line as a Pass-2 candidate ("'So I am not going to compress it. I am going to name it and leave it.' (line 221 audit-time). Declarative-pair with first-person voice — Pass 2 candidate.").

The line functions as the chapter's deliberate scope-limit-statement after the civilizational-extrapolation paragraph (line 220's GDP-vs-welfare clarification). The first-person declarative-pair enacts the author's deliberate non-compression-of-scope move (the chapter is not going to spell out the civilizational-scale policy implications; it's going to name the $10–$15T figure and stop). The cadence is substantively purposeful but the standalone-paragraph framing + the strict first-person anaphoric-pair structure is the named tidy-parallel pattern at maximum-visibility chapter-pivot site.

Compounds with F-V4 (five-fold "I'll" interjections chapter-wide): the line 222 declarative-pair is part of the chapter's first-person register-drift cluster, but at a different cadence (declarative-pair rather than imperative-single). Two-sentence compression + first-person + chapter-pivot-position makes it more visible than the F-V4 interjections individually.

**Severity rationale.** Substantively load-bearing — the line is the chapter's deliberate scope-limit-statement at the civilizational-extrapolation paragraph's close; the first-person declarative-pair enacts the non-compression discipline. But the strict-parallel "I am [not] going to [verb]" anaphoric-pair structure + standalone-paragraph + first-person register-drift compounds with F-V4 at chapter scale. MEDIUM (not HIGH) because the line's substantive scope-limit-statement is load-bearing + the cadence enacts the author's deliberate non-compression discipline; not LOW because Pass 1 §9 explicitly flagged + the line's standalone-paragraph framing amplifies cadence-visibility.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively load-bearing scope-limit-statement; first-person declarative-pair enacts non-compression discipline; standalone-paragraph framing is the chapter's deliberate cadence-pivot move. Defensible as memoir-adjacent analytical voice.
- **B. Compress to single sentence.** *"So this book is not going to compress the figure: it names it and leaves it."* OR *"So the chapter names the figure and leaves it, without compressing it into policy implications it cannot honestly deliver."* Drops the declarative-pair; drops first-person register (per cross-reference with F-V4 Option A); preserves the substantive scope-limit-statement; reads as analytical-third-person.
- **C. Retain first-person; vary the declarative-pair structure.** *"So I am not going to compress it; I will name the figure and leave it there."* Drops the strict-parallel "I am going to [verb]" anaphora to "I will [verb]"; reduces the named-pattern visibility; preserves first-person register; preserves declarative-emphasis.
- **D. Cut the line entirely.** Drop line 222; let the preceding line 220 paragraph carry the scope-limit-statement implicitly. **CAUTION:** the line 222 declarative-pair is the chapter's explicit scope-limit-statement; cutting it would leave the civilizational-scale implication paragraph (line 220) without an explicit scope-limit closer. High-risk cut.

**Recommendation:** Option B (compress to single sentence, third-person). Aligns with F-V4 Option A chapter-wide register-conversion; drops the strict-parallel first-person declarative-pair; preserves substantive scope-limit-statement. If author ratifies F-V4 Option B (retain one first-person interjection), Option C provides a coordinated first-person-preserving fix at line 222.

---

### F-V11 — Three-fold "The first / The second / The third misreading" anaphoric paragraph-opener (lines 200, 202, 206) (MEDIUM)

**Three paragraph-opener anaphora:**

- **Line 200:** *"**The first misreading** is that honest pricing is a claim that the extraction should never have happened. It isn't. Cheap energy — even severely mispriced energy — lifted billions of human beings out of poverty..."*
- **Line 202:** *"**The second misreading** is that honest pricing is a claim that the market is fake. It isn't. Prices cleared transactions. The money changed hands. Real coal left McDowell County on real rail cars..."*
- **Line 206:** *"**The third misreading** is that honest pricing is a tool by which already-industrialized nations pull up the ladder behind developing economies. This is the objection that has to be taken seriously..."*

**Why this flags.** Three paragraph-openers with strict-parallel "The [Nth] misreading is that..." anaphora across consecutive paragraphs. Each paragraph follows the same structural template: (a) name the misreading; (b) "It isn't" two-word standalone rebuttal sentence; (c) extended explanation; (d) chapter's actual position. The "The Nth X is..." paragraph-opener anaphora is the named tidy-parallel pattern at chapter-section scale.

The three-fold structure IS the chapter's section-architecture for the "What honest pricing does not mean" section (line 196 section header). The reader is told at line 198 ("Three misreadings have followed this argument every time I've offered it, and I want to name them before the chapter ends") that three misreadings will follow; the paragraph-opener anaphora delivers the three-fold. Substantively load-bearing — the section's argument-structure depends on the parallel form.

But: three paragraph-openers with strict-anaphora across consecutive paragraphs + each paragraph internally repeating the "It isn't" + extended-rebuttal pattern stacks named-pattern visibility. A trade-press editor will register the three-fold paragraph-anaphora as the section's section-architecture-revealing-itself move — substantively defensible, cadence-visible.

**Severity rationale.** Substantively load-bearing — the three-fold IS the section's argument-structure; the line 198 setup explicitly promises three misreadings; the parallel-paragraph-opener anaphora delivers them. Cadence-enacts-content + section-architecture-revealing. MEDIUM (not HIGH) because the parallel is substantively earned + the section explicitly promises the three-fold; not LOW because the strict paragraph-opener anaphora at three consecutive sites is the named tidy-parallel pattern at section-scale.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively load-bearing section-architecture parallel; the three-fold IS the section's structure; line 198 explicitly promises three misreadings; the parallel-paragraph-opener anaphora delivers them. Cadence-enacts-content. Substance-drives-length governs.
- **B. Vary one of the three paragraph-openers for cadence-relief.** Convert line 206 to *"The third — and most important — misreading is that honest pricing is a tool by which already-industrialized nations pull up the ladder behind developing economies."* Drops strict "The third misreading is that" to "The third — and most important — misreading is that"; preserves the three-fold counting; breaks the strict-anaphora at the third instance (which is also the chapter's most substantively load-bearing misreading-defense). **CAUTION:** adds an em-dash pair; contributes to F-V3 chapter-wide em-dash count.
- **C. Vary the line 200 "It isn't" pattern.** Each paragraph's "It isn't" rebuttal-sentence is itself the named declarative-cadence pattern (two-word standalone rebuttal across three consecutive paragraphs). Vary one or two: line 200 *"It isn't, in any responsible sense."*; line 202 *"It isn't — and the chapter's argument has never made that claim."*; line 206 retain as-is. Drops the three-fold "It isn't" standalone-pair pattern; preserves the misreading-rebuttal force. **CAUTION:** line 202 fix uses em-dash; contributes to F-V3.

**Recommendation:** Option A (hold as-is). Substantively load-bearing section-architecture parallel; the three-fold IS the section's structure per line 198's explicit setup; cadence-enacts-content. Pass 3 audience-load testing will surface whether the three-fold parallel reads as section-architecture-rigorous or as formulaic-three-pattern (per §7 forward-flag); if Pass 3 surfaces a flag, revisit at that point.

---

### F-V12 — Rent-seeking paragraph (line 122) voice-register match + LLM-tic surface audit (MEDIUM)

**Line 122 (rent-seeking paragraph, inserted via commit `a1e54d9` → ratified `bc02767`):**
> "The architecture that produced McDowell County's specific form of post-extraction collapse was not impersonal. It was shaped, generation after generation, by coal-industry political-economic actors — operators, absentee-mineral-rights holders, industry trade associations — whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record. The cost-bearing-party analysis the framework performs (who absorbed what; over what timeframe; against what counterfactual) operates on top of an architecture that specific identifiable actors shaped. The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) supplies the actor-and-coalition vocabulary for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning that shaped the political-coalition record on the books. The framework's contribution is different in kind: the ledger that counts what those traditions described has been costing, and to whom — the cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number rather than as an actor-attribution problem. Chapter 9 develops the framework-Public-Choice relationship at greater length."

**Why this flags.** Per the rent-seeking workstream's own routing (`bc02767` §9 Ratification log): "Ch 8 + Ch 9 have Pass 1 PROPOSED only; their forthcoming Pass 2/3 cycles will absorb the rent-seeking-section verification as standard pass scope." This Pass 2 honors that routing. The commit's voice-register-match claim was: "Ch 8 touch register-matched to chapter's first-person conversational voice." Pass 2 audit verifies + surfaces.

**Voice-register-match verdict:** The rent-seeking paragraph is **NOT first-person conversational** — it reads as **analytical-third-person** with framework-spine references ("The framework performs..."; "The framework's contribution is different in kind..."). This MATCHES Ch 8's dominant register (analytical-third-person), but does NOT match the commit's stated "first-person conversational" voice-register-match. Pass 2 verdict: the paragraph's actual voice IS register-matched to Ch 8's dominant analytical-third-person voice (which is the correct match); the commit message's "first-person conversational" characterization was inaccurate but the voice-register-match itself is clean. The chapter's first-person voice ("I'll use" / "I'll price" — F-V4 register-drift) appears at section-conclusion sites, not in this analytical-engagement paragraph; the rent-seeking paragraph correctly stays in analytical-third-person voice consistent with the surrounding Political Capture Cost section.

**LLM-tic surface scan:**
- **Em-dashes:** 3 em-dashes in the paragraph (cited at F-V3 as one of the seven ≥3-em-dash paragraphs). Each em-dash is substantively earned: first pair brackets the cost-bearer actor-list (operators / absentee-mineral-rights holders / industry trade associations); second em-dash introduces the result-clause "the cost-bearing magnitudes...". Defensible parenthetical-pair + rhetorical-pivot use. Contributes to F-V3 chapter-wide em-dash density.
- **Tidy-parallel:** the two-paragraph-middle sentences ("The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) supplies the actor-and-coalition vocabulary for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning...") are paired with anaphoric "The [tradition name] supplies the vocabulary" + parenthetical-author-list structure. Two-sentence anaphoric-pair, NOT a named tidy-parallel three-pattern. Defensible.
- **Hedge / cliché / meta-commentary:** Clean — no named hedge / cliché / meta-commentary inventory patterns.
- **Apparatus residue:** Clean per Pass 1 §12.3 verification (no Greek letters, no integrals, no Cᵢ-class regressions; Title-case "Public Choice" is the tradition-name conventional form; "reparations-economics" lowercase is the chapter's discipline-name conventional form).
- **Named-subject consent:** Clean per Pass 1 §12.3 + §7 — all named subjects (Coates / Darity / Mullen / Hamilton / Conley / Buchanan / Tullock) are public-record academics named in their professional / published-author capacity. The LOW-8 Conley grouping concern (Pass 1 §12.4) is HELD per the rent-seeking workstream's stated routing.

**Voice-register-match verdict overall: ✓ HOLDS** for Ch 8's analytical-third-person dominant register. The commit message's "first-person conversational" characterization was inaccurate description but the paragraph's actual voice integration into Ch 8 is clean.

**Severity rationale.** The rent-seeking paragraph reads as substantively earned framework-vs-adjacent-tradition analytical-engagement work; voice register matches Ch 8's analytical-third-person dominant; LLM-tic scan returns clean apart from the 3-em-dash contribution to F-V3 chapter-wide density (each em-dash individually defensible). MEDIUM rather than LOW only because the paragraph is the chapter's newest content (post-Pass-1 audit) and the explicit Pass 2/3 verification routing warrants the explicit pass-coverage record at MEDIUM severity-tier. **No spot-fix recommended on the paragraph itself** apart from any em-dash reductions adopted via F-V3 (which may or may not touch the line 122 em-dashes depending on author option-choice).

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Voice register matches; LLM-tic scan clean; em-dashes individually defensible; LOW-8 Conley grouping disposition deferred per workstream routing. No paragraph-internal spot-fix recommended; em-dash count handled at F-V3.
- **B. Coordinate with F-V3 disposition.** If author ratifies F-V3 Option A (targeted reduction at high-density paragraphs) or Option B (comprehensive sweep), the line 122 paragraph's 3 em-dashes may be reduced. Sample fix: convert the cost-bearer actor-list em-dash pair to parenthetical-comma. *"It was shaped, generation after generation, by coal-industry political-economic actors (operators, absentee-mineral-rights holders, industry trade associations) whose lobbying expenditure..."* Drops 2 em-dashes; preserves substantive content.

**Recommendation:** Option A (hold as-is at the paragraph level; coordinate with F-V3 disposition if author chooses chapter-wide em-dash sweep). The rent-seeking paragraph's voice-register-match verification was the explicit Pass 2 routing target; verification verdict is ✓ HOLDS.

---

### F-V13 — Anaphoric "There are X costs" three-fold + appositive-pair triple at line 60 (MEDIUM)

**Line 60 (most em-dash-dense paragraph):**
> "A community doesn't drop to twenty percent of its population without carrying costs. **There are infrastructure costs — schools, fire departments, water systems, hospitals — that must be maintained at some minimum regardless of headcount and whose per-capita burden rises as the headcount falls. There are economic multiplier losses — every local business that closed, every institution that couldn't sustain itself, every dollar that didn't circulate locally because the earner left. There are public program costs — food stamps, disability payments, Medicaid — absorbed by federal and state government** in a county that had once generated billions of dollars in coal revenue, almost none of which stayed."

**Why this flags.** Three-sentence "There are [X] costs/losses" anaphora across consecutive sentences with strict-parallel structure: "There are [adjective] [noun] — [appositive list] — [extended clause]." Each sentence carries an em-dash-bracketed inset (the appositive list). Three-fold anaphora + three-em-dash-pair pattern in one paragraph stacks two named patterns at chapter's highest-em-dash-density paragraph.

The three-fold names three distinct Community Disruption sub-categories (infrastructure / economic multiplier / public program). Substantively earned — the three-fold IS the section's substantive-categorization of community disruption costs. But the strict-parallel form + the appositive-pair-em-dash triple compounds with F-V3's chapter-wide em-dash density flag.

Cumulative pattern: line 60 is the chapter's single highest-density LLM-cadence + em-dash paragraph (the chapter's worst-case-cadence-and-em-dash paragraph by both measures).

**Severity rationale.** Substantively earned three-categorization of community disruption costs; the three-fold parallel is the section's substantive-categorization move. But the cumulative stacking (three-fold anaphora + three em-dash pairs in one paragraph) makes this paragraph the chapter's highest-density LLM-cadence + em-dash flag. MEDIUM (not HIGH) because each instance is substantively earned + the three-categorization is load-bearing; not LOW because the cumulative density compounds with F-V3.

**Recommended spot-fix (author selects one option):**

- **A. Hold as-is.** Substantively earned three-categorization; pattern enacts content (three sub-categories of community disruption); load-bearing for the Community Disruption Cost section's substantive walk. Em-dash density handled at F-V3.
- **B. Vary the appositive-pair-em-dash triple to colon-list (per F-V3 Option A sample fix).** *"There are infrastructure costs: schools, fire departments, water systems, hospitals — costs that must be maintained at some minimum regardless of headcount and whose per-capita burden rises as the headcount falls. There are economic multiplier losses — every local business that closed, every institution that couldn't sustain itself, every dollar that didn't circulate locally because the earner left. There are public program costs: food stamps, disability payments, Medicaid — absorbed by federal and state government in a county that had once generated billions of dollars in coal revenue, almost none of which stayed."* Drops two em-dash pairs to colons; preserves three-fold anaphora; F-V13 + F-V3 paragraph-level coordination.
- **C. Compress three-fold to one sentence with three-element serial.** *"A community doesn't drop to twenty percent of its population without carrying costs: infrastructure (schools, fire departments, water systems, hospitals) that must be maintained at some minimum regardless of headcount, economic multiplier losses (every local business that closed, every institution that couldn't sustain itself, every dollar that didn't circulate locally), and public program costs (food stamps, disability payments, Medicaid) absorbed by federal and state government in a county that had once generated billions of dollars in coal revenue."* Drops three-fold anaphora to one colon-list-introduced sentence; converts em-dash pairs to parenthesis-pairs; preserves substantive three-categorization; heavier rewrite.

**Recommendation:** Option B (vary appositive-pair-em-dashes to colons; coordinate with F-V3 Option A sample fix). Preserves the substantive three-categorization anaphora at the Community Disruption Cost section walk; reduces em-dash density at the chapter's highest-density single-paragraph site; addresses F-V13 + F-V3 at the same paragraph. Drops paragraph em-dash count from 5 to 3.

---

## §4. Findings — LOW severity / style preferences

Patterns that are style preferences rather than stoppers. Author discretion; default recommendation is hold-as-is across the LOW set.

### F-V14 — "Begin with X / Walk outside the X" two-fold section-opener cadence at lines 34 + 46 (LOW)

**Two instances** at the first two cost-component-section openings:

- **Line 34 (Direct Health Cost):** *"**Begin with the lungs.** Black lung is the most completely documented externality coal has ever produced..."*
- **Line 46 (Environmental Degradation Cost):** *"**Walk outside the mine.** The creek running orange with acid mine drainage is not a metaphor..."*

Imperative-opener cadence at the first two section-walks; sets up a tour-guide register that subsequent sections don't sustain (Community Disruption opens with "The county peaked near one hundred thousand residents in 1950" — descriptive; Foreclosure opens with "This is the cost component Chapter 2 named through the cost-walkthrough" — analytical-self-reference; etc.). The two-fold imperative-opener establishes a tour-guide cadence the chapter then drops.

**Recommended spot-fix:** Hold as-is. The two-instance cadence-pair is defensible as section-opener tour-guide rhetoric for the first two (most concrete; lung-and-creek) cost-component sections; subsequent sections shift to analytical register as the harder-to-tour components arrive. Substantively earned section-walk pivot.

---

### F-V15 — "Not from preference. From arithmetic." two-word + three-word standalone-pair at line 12 (LOW)

**Line 12:** *"Ask the question without political coding, without ideology, and the framework we've been building starts answering it before the argument even begins. **Not from preference. From arithmetic.**"*

Two-sentence cadence-pair with short-short declarative shape (3 words / 2 words). Pass-2 inventory's *declarative-three-in-a-row* pattern requires three short declaratives; this is two. Mild — but in the chapter-opening paragraph, contributes to F-V1's chapter-opening cadence-density flag.

**Recommended spot-fix:** Hold as-is per pattern-threshold (two short declaratives, not three). If F-V1 Option A is applied (colon-list compression), this two-fold may need to be retained at the new sentence position. Light coordination only.

---

### F-V16 — "Add to that: the option-value foreclosure not captured..." colon-list introduction at line 76 (LOW)

**Line 76:**
> "Add to that the option-value foreclosure not captured by the carbon number: every future metallurgical application that cannot be served by a non-existent substitute, every future chemical feedstock application, every use case we cannot yet imagine for a carbon resource whose existing stock is being burned for electricity in a world where electricity can now be generated from sources that don't require combustion at all."

Long compound-sentence with three-element comma-serial inside a colon-list. The within-sentence three-fold ("every future metallurgical application...; every future chemical feedstock application...; every use case we cannot yet imagine...") is the named within-sentence rule-of-three; per Pass-2 template, this is structurally different from cross-sentence three-fold and is defensible as analytical enumeration.

**Recommended spot-fix:** Hold as-is. Within-sentence rule-of-three serial is defensible analytical enumeration per Pass-2 template guidance.

---

### F-V17 — Numerical-pivot one-sentence standalone-paragraph at line 164 ("Total: $558 per ton.") (LOW)

**Line 164:** *"Total: $558 per ton."*

One-sentence standalone paragraph following the eight-cost-component bullet-list (lines 148–162). Functions as the chapter's headline-figure numerical-climax moment. The standalone-paragraph framing is high-visibility but the substantive payoff (the chapter's headline number) earns the cadence-pivot. Direct calibration with Ch 7 F-V12 (chapter-closing three-imperative — held in Ch 7 Pass 2).

**Recommended spot-fix:** Hold as-is. Chapter-headline numerical-pivot moment; standalone-paragraph framing earns the cadence-isolation; substance-drives-length governs.

---

### F-V18 — "These are not hypothetical entities. They are people. They paid. They are still paying." four-declarative cluster at line 200 (LOW)

**Line 200 (first-misreading paragraph close):**
> "The miners who developed black lung, the communities that collapsed when the coal was exhausted, the children born into a county whose economic future had been extracted before their birth, the generations that will absorb the climate costs — **these are not hypothetical entities. They are people. They paid. They are still paying.** The question the framework asks is not whether extraction occurred. The question is who paid for it and whether they consented."

Four-sentence cluster: "[hypothesis-rebuttal]. [identification]. [past-tense]. [present-tense]." with strict-parallel declarative shape and ascending temporal cadence (people → paid → still paying). The four-fold IS the chapter's rhetorical-emphasis moment honoring named-but-unnamed cost-bearers; cadence enacts the moral-weight-of-the-claim.

Direct cadence-cousin to Ch 1 F-V21 (four-declarative chapter-close held as substantively-earned). Same calibration applies.

**Recommended spot-fix:** Hold as-is. Substantively-earned rhetorical-emphasis cadence at the chapter's first-misreading-rebuttal moral-weight moment; the four-fold ascending-temporal pattern enacts the "they paid and are still paying" moral claim. Direct Ch 1 F-V21 cousin disposition.

---

### F-V19 — "They are people. They paid." + line 222 "I am going to name it and leave it." — first-person + third-person register-toggle pattern (LOW)

**Cross-instance pattern observation:** The chapter's most rhetorically-charged moments toggle between third-person plural ("They are people. They paid. They are still paying." at line 200) and first-person singular ("I am going to name it and leave it." at line 222) within a span of 22 lines at the chapter's closing-section. Both are substantively earned: the third-person plural honors the cost-bearers; the first-person singular performs the author's deliberate non-compression discipline. The cross-instance register-toggle within the closing section is the chapter's deliberate voice-architecture move.

**Recommended spot-fix:** Hold as observation only. Not a finding requiring spot-fix; flagged for Pass 3 audience-load testing whether the register-toggle reads as deliberate voice-architecture or as register-drift (per §7 forward-flag).

---

### F-V20 — "the framework adds the cost-accounting mechanism by which the mask remains structurally necessary" at line 92 (LOW)

**Line 92 (Lineage Labor Cost section, post-MEDIUM-1 ratified-and-applied Dunbar quotation fix + LOW-1 ratified-and-applied Du Bois / Ellison / Fanon parallel-citation expansion):**
> "Dunbar named the strategy of survival. Du Bois named the structural condition that required it in *The Souls of Black Folk* (1903). Fanon extended the analysis into the colonial-economic register the framework's extraction-community cases sit closest to in *Black Skin, White Masks* (1952). Ellison gave the long-form narrative of life under the mask in *Invisible Man* (1952). **The framework adds the cost-accounting mechanism by which the mask remains structurally necessary.**"

The "The framework adds X" closer follows four parallel-citation sentences (Dunbar / Du Bois / Fanon / Ellison each named with work + year, per LOW-1 ratified-and-applied parallel-citation expansion). The closer is the chapter-spine self-reference that integrates the lineage-citation parallel into the framework's contribution. Substantively earned — the four-fold lineage citation IS the chapter's joining-the-tradition move; the closer names what the framework adds. Cadence-cousin to F-V8's chapter-spine self-reference cluster.

**Recommended spot-fix:** Hold as-is. Substantively earned lineage-tradition + framework-contribution structure; closer is the chapter's integration-move. Pass 3 audience-load testing will specifically test whether the lineage-roll-call + "what the framework adds" closer reads as joining the tradition vs appropriating it for a different-domain framework — per Pass 1 §10 Tier-3 Black-Studies-resonance reader pressure-test.

---

## §5. Apparatus / consistency / italicization / named-subject sub-checks

Per the Pass-2 inventory's last few categories + the workstream handoff's Ch 8 emphasis + Pass 1 §5 verifications carry-forward.

### §5.1 Register consistency — ✓ HOLDS (with F-V4 + F-V10 first-person register-drift observations)

Chapter holds analytical-quantitative voice throughout cost-component walks (lines 24–166). Voice shifts at section-conclusion sites where first-person interjections appear ("I'll use" / "I'll price" / "I'll assign" — F-V4 five-fold pattern + line 222 declarative-pair — F-V10). Closing-section (lines 198–240) maintains analytical voice with rhetorical-pivot interpolations.

Cross-case sweep section (lines 174–192) holds analytical-third-person; YIMBY-engagement passage (lines 180–190) maintains analytical-argumentative register with chapter-spine self-reference (per F-V8). Misreading-defense section (lines 196–206) maintains analytical-third-person with declarative-rebuttal cadence (per F-V11 + F-V18).

No third-person-analytical → memoir-narrative register-breaks observed (the chapter is analytical-quantitative throughout, not memoir). The F-V4 first-person interjections + F-V10 first-person declarative-pair ARE the chapter's deliberate first-person-accountability voice-architecture move; whether this is preserved or converted-to-third-person is a Pass-2 disposition question (F-V4 + F-V10 author choice).

### §5.2 Tense-consistency — ✓ HOLDS

- **Present-tense analytical:** most of chapter ✓
- **Past-tense historical:** Kennedy 1960 (line 24); McDowell County peak / U.S. Steel 1986 (line 58); SCC trajectory by administration (line 118) — all scene-cued ✓
- **Conditional / counterfactual:** "Had coal been priced closer to its honest cost in 1960..." (line 134); "If full-cost pricing would raise those revenues..." (line 214) — scene-cued ✓

All shifts scene-cued. No tense-leak observed.

### §5.3 Apparatus residue — ✓ HOLDS (Pass 1 §5 verification intact)

Per Pass 1 §5 apparatus regression check (confirmed intact at session start):
- **Integrals (∫):** 0 hits in chapter prose. ✓ Item 1 (commit `d1f6e2d`) intact.
- **Greek letters (μ, σ, θ, λ, β, γ, δ, ε, τ, ω, α, ∂, ∑):** 0 hits in chapter prose. ✓
- **Cᵢ subscript:** 1 hit at line 18 (apparatus-introduction passage). ✓ Permitted per inventory.
- **Commons Inversion Test (CIT):** Full name at lines 18, 86, 130 — verified ✓; no CIT acronym anywhere in chapter prose.
- **Four Gates:** Title-case at line 18. ✓
- **Intergenerational Pricing Gap (IPG):** Full-name expansion at line 168 with parenthetical-gloss-first style. ✓
- **Other apparatus terms (Residual Commons Value, Accountability Bond, etc.):** Not introduced in chapter prose. Cross-references at line 70 ("residual commons value integral") use lowercase prose form. ✓
- **Title-case framework terms:** "Direct Health Cost," "Environmental Degradation Cost," "Community Disruption Cost," "Foreclosure Cost," "Lineage Labor Cost," "Knowledge and Cultural Cost," "Political Capture Cost," "Temporal Displacement Cost" — all Title-case at section-header sites (F-V5 parallelism). ✓
- **Public Choice:** Title-case at line 122 (tradition-name conventional form). ✓
- **Black Lung Benefits Program:** Title-case at line 34 (institutional-name conventional form). ✓
- **"reparations-economics":** lowercase at line 122 (discipline-name conventional form). ✓
- **"residual commons value integral":** lowercase prose at line 70. ✓

No apparatus regression observed. No retired-term regression observed.

### §5.4 Hedge phrases — ✓ CLEAN

Verified absent (grep audit): no "I will argue that..." / "It seems likely that..." / "Perhaps..."-as-sentence-opener patterns. F-V8's borderline hedge-phrase observations ("the framework cannot earn the integration without engaging it specifically") are substantive methodological-commitment phrasings, not named hedge-tics.

### §5.5 Connective-tissue clichés — ✓ CLEAN

Verified absent (grep audit): no "in short" / "ultimately" / "moreover" / "furthermore" / "that being said" / "going forward" / "at the end of the day" / "to that end" patterns. Transitions managed via section-headers + `---` separators + substantive-pivot sentences ("Walk outside the mine" at line 46; "Now the harder components" at line 86; "If this were an isolated case" at line 174; "The pattern does not stop at what conventionally counts as extraction" at line 178) rather than editorial-connective clichés.

### §5.6 Expository flatness + meta-commentary — MOSTLY ✓ CLEAN (with F-V8 chapter-spine self-reference observation)

No verbatim "The plain definition is this:" / "Here is what I think:" / "The argument is simple:" colon-introduction patterns. F-V8 captures the YIMBY-engagement passage's chapter-spine self-reference density at MEDIUM (recommendation Option A hold-as-is per substantively-earned argument-with-objector engagement). F-V11 captures the misreading-defense section's three-fold structural parallel (held as substantively-earned). No other expository-flatness or meta-commentary concerns surface.

### §5.7 Named-subject register — ✓ HOLDS (Pass 1 §7 verification intact)

Per Pass 1 §7 named-subject consent check (intact):
- John F. Kennedy (line 24) — deceased + public-record historical figure ✓
- John L. Lewis (line 116) — deceased + public-record historical figure ✓
- Paul Laurence Dunbar (line 92) — deceased + public-domain literary record ✓
- W.E.B. Du Bois (line 92) — deceased + public-domain scholarly record ✓
- Ralph Ellison (line 92) — deceased + public-record literary work ✓
- Frantz Fanon (line 92) — deceased + public-record scholarly work ✓
- Atif Mian + Amir Sufi (line 192) — living; published-author capacity ✓
- Edward Glaeser, Joseph Gyourko, Jenny Schuetz (line 182) — living; published-author capacity ✓
- Wagner, Anthoff, Cropper, et al. 2021 (line 118) — living; published-author capacity ✓
- Rennert and colleagues 2022 (line 72) — living; published-author capacity ✓
- Coates, Darity, Mullen, Hamilton, Conley (line 122) — living-academics; published-author capacity ✓
- Buchanan, Tullock (line 122) — Buchanan + Tullock deceased; public-record academic figures ✓
- Communities + places (McDowell / Libby / Baotou / Prince William Sound / Alberta / Athabasca Chipewyan + Mikisew Cree + Fort McKay First Nations) — place / community names ✓

No new living-private named subjects added in Ch 8 since Pass 1 audit. No consent regressions caught in Pass 2. LOW-8 Conley grouping concern (Pass 1 §12.4) deferred per workstream routing; Pass 2 does not re-litigate.

### §5.8 Italicization discipline — ✓ HOLDS

- **Book titles:** *We Wear the Mask*, *The Souls of Black Folk*, *Black Skin, White Masks*, *Invisible Man*, *House of Debt* — all italicized at line 92 / line 192 ✓.
- **Journal titles:** *Nature* at line 72 ✓.
- **Term-emphasis italics:** *when* at line 130 (Temporal Displacement Cost first-introduction); *not* at line 196 section header — both deliberate emphasis ✓.
- **No book-title italicization regressions** ✓.

### §5.9 Number formatting — ✓ HOLDS (mostly)

Chapter's prevailing convention is spelled-out for narrative-flow ("four to five dollars" at line 24; "two and a half dollars" implied via "$558"); digits for technical/precise figures ($558 at line 164; $40-$140 at line 168; $190 at line 72). Mixed at line 168 (cross-corpus IPG canonical-construction artifact ratified Option D — uses both ranges with explicit framework reconciliation). Holds clean.

### §5.10 Section-break rhythm — ✓ HOLDS

14 `###` subsection headers + 15 `---` separators across 243 lines. Every `###` subsection is preceded by a `---` separator (verified). Front-matter render-fix (commit `e1a533e`) added the line 9 `---` after the chapter-title header. No missing separators; no `###` nested mid-paragraph. Structurally clean.

### §5.11 Chapter-cross-reference capitalization — ✓ HOLDS

All "Chapter N" references Title-case (Chapter 1, 2, 5, 6, 8, 9, 10) per inventory §7. Verified ✓.

---

## §6. Cadence / sentence-length / declarative-rhythm summary

Quantitative observations to anchor the qualitative findings above.

| Metric | Count | Notes |
|---|---|---|
| Total em-dashes | 80 | ~12.5 per 1,000 words; among corpus's highest densities; F-V3 HIGH |
| Paragraphs ≥3 em-dashes | 7 | Lines 34, 48, 60, 122, 178, 188, 200; F-V3 + F-V13 |
| Max em-dashes in one paragraph | 5 | Line 60 (Community Disruption Cost section); F-V13 + F-V3 |
| First-person "I'll [verb]" interjections | 5 | Lines 62, 96, 108, 124, 138; F-V4 HIGH |
| First-person declarative-pair (line 222) | 1 | "So I am not going to compress it. I am going to name it and leave it."; F-V10 |
| Total first-person mid-paragraph instances | 7 | F-V4 (5) + F-V10 (1) + line 198 "I've offered it, and I want to name them" (1) |
| Section-header "[Adj] [Noun] Cost" pattern | 8 of 14 | F-V5; chapter-architecture parallel |
| Chapter-opening "Price the X" anaphora | 5-fold | Line 12; F-V1 HIGH |
| "Different X / The same X" cross-scenario sweep | 6-fold | Line 176 (4-fold "Different X" + 2-fold "The same X"); F-V2 HIGH |
| "Numerical figure. Against [market price]" cadence | 3 sections | Lines 40, 74, 166; F-V6 |
| Misreading paragraph-opener three-fold | 3 paragraphs | Lines 200, 202, 206; F-V11 |
| "Begin with X / Walk outside the X" section-opener | 2-fold | Lines 34, 46; F-V14 LOW |
| Methodological-statement parallel-structure paragraph | 1 (5-sentence) | Line 28; F-V7 |
| YIMBY-engagement chapter-spine self-reference density | 5 paragraphs | Lines 180–190; F-V8 |
| Closing-section short-declarative cluster | 3 paragraphs | Lines 228–234; F-V9 |
| Hedge-phrase named patterns | 0 | ✓ Clean |
| Connective-tissue cliché patterns | 0 | ✓ Clean |
| Meta-commentary verbatim patterns | 0 | ✓ Clean |
| Apparatus residue | 0 | ✓ Clean (Pass 1 §5 intact) |
| Named-subject consent issues | 0 | ✓ Clean (Pass 1 §7 intact) |
| Three-short-declarative candidates (≤40-char each) | 6 instances | "Price the health costs. Price the environmental damage. Price the community..." (line 12); "Add them together. Look at the number. Look at the price..." (line 12); "A buyer paid. A seller was paid. The transaction cleared." (line 24); "Different industries. Different geographies. Different decades." (line 176); "They are people. They paid. They are still paying." (line 200); "It isn't. Prices cleared transactions. The money changed hands." (line 202) — most covered by F-V1, F-V2, F-V18 |

**Cadence-density narrative:**
- Chapter-opening (lines 10–18): F-V1 five-fold + F-V15 two-fold + F-V3 cumulative em-dash burden start the chapter at high cadence-density.
- Cost-component walks (lines 22–138): F-V4 five first-person interjections + F-V5 eight parallel section-headers + F-V6 three numerical-pivot cadences + F-V7 methodological-statement parallel + F-V13 line-60 three-fold + cumulative F-V3 em-dashes. Highest single-paragraph density at line 60 (F-V13).
- Chapter sum (lines 142–168): F-V6's line 166 three-fold "Against [market price]" + F-V17 line 164 standalone-paragraph headline-pivot. Chapter-headline-figure cadence-cluster.
- Cross-case sweep + YIMBY (lines 170–192): F-V2 line 176 six-fold + F-V8 YIMBY chapter-spine-self-reference five-paragraph density. Chapter-climax-region cadence cluster.
- Misreading defenses (lines 196–206): F-V11 three-fold paragraph-opener parallel + F-V18 line 200 four-declarative cluster. Section-architecture parallel.
- Closing (lines 226–240): F-V9 rhetorical-question + standalone + Chapter-rule-of-three cluster. Closing-section signature cadence.

The chapter's cadence-density profile is bi-modal: high-density at chapter-opening + chapter-sum + chapter-climax + section-architecture pivots; analytical-third-person low-density during the cost-component walks themselves. The two highest-density regions are (a) line 60 (F-V13 + F-V3), and (b) lines 166–176 (F-V6 + F-V2 — two six-fold patterns within 10 lines at the chapter's headline-numerical-climax + cross-scenario-sweep pivot region).

---

## §7. Out-of-scope-for-Pass-2 — flagged for Pass 3 (audience-load) future-session input

Items that crossed Pass-2 attention during paragraph-by-paragraph read; flagged here so the Pass-3 (audience-load) session has them ready. **Not scored as Pass-2 findings.** Pass 1 §10 already enumerated the Ch-8-specific audience-character set comprehensively; these are Pass-2-surfaced additions or sharpenings.

- **Cumulative cadence-density chapter-wide (per F-V1 + F-V2 + F-V4 + F-V6 + F-V11 + F-V18).** Pass 3 trade-press editor pressure-test: does the cumulative density read as analytical-rigor-enacted (the eight-component walk IS rigorous; the parallel cadences enact the rigor) or as LLM-cadence reach-for-resonance? Cumulative-cadence diagnostic is a Pass 3 strength, not a Pass 2 paragraph-by-paragraph strength. Especially: the chapter-headline-climax region (lines 166–176) has TWO six-fold cadence patterns within 10 lines — does the cumulative effect amplify or dilute the chapter's headline-figure rhetorical-impact for Tier-1 trade-press readers?
- **Em-dash density chapter-wide (F-V3 ratification choice).** Whichever option the author ratifies (Option B comprehensive sweep / Option A targeted reduction / Option C spot-audit / Option D hold-as-is), Pass 3 should re-test how the post-F-V3 chapter's em-dash discipline reads against Tier-1 trade-press editor (the em-dash-discipline lens). The em-dash discipline ratified 2026-05-21 is a recent corpus-wide voice-polish discipline; Ch 8's 80-em-dash count may flag for any tic-scanning publisher-side editor regardless of individual-instance defensibility.
- **First-person register-architecture (F-V4 + F-V10 ratification choice).** Whichever option the author ratifies (F-V4 Option A all-third / Option B retain-one / Option C upstream-statement-restructure / Option D hold-as-is), Pass 3 should re-test how the post-F-V4 + post-F-V10 chapter's voice-architecture reads against Tier-1 quant/economist + Tier-1 trade-press + Tier-3 Appalachian-policy readers. The first-person interjections enact the author's accountability-on-the-page move; whether this lands as principled or as register-drift depends on reader expectation.
- **YIMBY-engagement passage (F-V8 + Pass 1 §10 Tier-2 YIMBY-aware reader).** Pass 1 §10 specifically flagged the YIMBY engagement at lines 180–190 as a Pass-3 audience-load priority: "does a Glaeser-Gyourko-citing housing-economics reader (the YIMBY position the chapter engages) read lines 179–189 as a fair engagement or as a strawman?" Pass 2 verifies the passage holds clean against the named LLM-tic inventory (no hedge / cliché / meta-commentary verbatim matches); Pass 3 should test substantive engagement quality, not just voice register.
- **Misreading-defense three-fold parallel (F-V11 + Pass 1 §10).** Pass 3 specific test: does the three-misreading-defense section's strict-parallel paragraph-opener anaphora read as section-architecture-rigorous (the chapter promised three; here are three) or as formulaic-three-pattern (LLM-cadence reach for resonance via parallel)? Cross-reference with Tier-1 trade-press reader's pattern-scanning calibration.
- **Lineage-tradition + framework-contribution structure at line 92 (F-V20 + Pass 1 §10 Tier-3 Black-Studies-resonance reader).** Pass 3 specific test: does the four-author parallel-citation (Dunbar + Du Bois + Fanon + Ellison each with work + year, per LOW-1 ratified-and-applied) + "The framework adds the cost-accounting mechanism by which the mask remains structurally necessary" closer read as joining the tradition or as appropriating it for a different-domain framework? Bibliography.md §13 specifically distinguishes "joining" from "borrowing"; Pass 3 should test against that lineage commitment.
- **"I am not going to compress it. I am going to name it and leave it" register-toggle at line 222 (F-V10 + F-V19).** Pass 3 specific test: does the first-person scope-limit-statement at the closing-section position land as deliberate authorial-discipline-naming or as authorial-register-drift? Cross-reference with whether F-V4 first-person interjections are converted-to-third-person (then line 222 stands alone as the chapter's only first-person closer, which amplifies its scope-limit-statement force) or retained-in-first-person (then line 222 is part of a chapter-wide first-person voice-architecture).
- **Chapter-closing forward-pointer at line 234 ("Chapter 9 sketches the direction... Chapter 10 closes with...") (F-V9).** Pass 3 specific test: does the Chapter rule-of-three forward-pointer land as cumulative-arc-naming (Chapter 1 → 8 done; 9 → 10 ahead) or as structural-scaffold-revealing (LLM-prose forward-pointer move)?
- **Rent-seeking paragraph (line 122) audience-load (F-V12 + Pass 1 §10 + cross-chapter rent-seeking workstream routing).** Pass 3 specific test: does the framework-vs-Public-Choice + framework-vs-reparations-economics analytical-engagement land as substantive cross-tradition-engagement or as defensive-claim-staking? Specifically for: Tier-2 Public-Choice-aware reader (the workstream's primary motivating audience); Tier-2 reparations-economics-aware reader; Tier-1 quant-economist reader. The LOW-8 Conley grouping concern (Pass 1 §12.4) defers to this Pass 3 session per workstream routing.
- **Cross-corpus IPG canonical-construction (commit `57575b1`) reader-acceptance at line 168.** Cross-corpus IPG artifact ratified Option D applied at line 168 (verified via current chapter state). Pass 3 specific test: does the Option D-style IPG framing ("$558 / $4.50 = 124× at 1960 mine-mouth; the carbon term alone exceeds today's market price by at least four") land for Tier-1 quant-economist + Tier-1 trade-press readers as analytical-rigorous or as methodologically-complicated? The Option D ratification was the cross-corpus solution; Pass 3 audience-load testing tests reader-side reception.

---

## §8. Out-of-scope-for-Pass-2 — flagged for fact-check follow-up

Items that surfaced during Pass-2 reading but belong to Pass-1's fact-check scope. **No new factual concerns surfaced.** Pass 1 ratification + Phase C application (commit `5fe6af6`) + Phase C-β residual hedge-alignment (commit `275b75a`) + cross-corpus IPG canonical-construction (commit `57575b1`) cover the externally-verifiable + cross-chapter-consistency claim set comprehensively.

One incidental observation worth flagging only as a possible pre-publication refresh item:

- **DOJ RealPage investigation status at line 188** ("investigating since 2022"): Pass 1 LOW-6 (time-sensitive figures) flagged DOJ RealPage as moving from investigation (Nov 2022) → antitrust complaint (2024) → proposed settlement (Nov 2025). Pre-publication refresh checklist already captures this; no Pass-2 action.

---

## §9. Verdict synthesis

### §9.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| HIGH | 4 | F-V1 (line 12 chapter-opening five-fold "Price the X" anaphora); F-V2 (line 176 six-fold "Different X / The same X" cross-scenario sweep); F-V3 (chapter-wide em-dash density — 80 em-dashes; 7 paragraphs ≥3; max 5 at line 60); F-V4 (line 62/96/108/124/138 five-fold "I'll [verb] [number]" first-person interjection cadence) |
| MEDIUM | 9 | F-V5 (8 of 14 section headers in "[Adj] [Noun] Cost" parallel — chapter-architecture); F-V6 (line 40/74/166 three-fold numerical-pivot "Against [market price]" cadence); F-V7 (line 28 methodological-statement parallel-structure paragraph); F-V8 (lines 180–190 YIMBY-engagement chapter-spine self-reference density); F-V9 (lines 228–234 closing-section short-declarative + Chapter-rule-of-three cluster); F-V10 (line 222 "So I am not going to compress it. I am going to name it and leave it." first-person declarative-pair); F-V11 (lines 200/202/206 three-fold "The [Nth] misreading is that..." paragraph-opener anaphora); F-V12 (line 122 rent-seeking paragraph voice-register-match + LLM-tic audit per workstream routing); F-V13 (line 60 anaphoric "There are X costs" three-fold + appositive-pair em-dash triple — paragraph-level pattern + F-V3 contribution) |
| LOW | 7 | F-V14 (lines 34/46 "Begin with X / Walk outside the X" section-opener two-fold); F-V15 (line 12 "Not from preference. From arithmetic." two-word + three-word standalone-pair); F-V16 (line 76 within-sentence rule-of-three colon-list); F-V17 (line 164 "Total: $558 per ton." one-sentence standalone-paragraph headline-pivot); F-V18 (line 200 "These are not hypothetical entities. They are people. They paid. They are still paying." four-declarative cluster); F-V19 (cross-instance third-person → first-person register-toggle observation; closing-section); F-V20 (line 92 lineage-tradition + framework-contribution structure closer) |

**Total findings:** 20 (4 HIGH + 9 MEDIUM + 7 LOW).

### §9.2 Aggregate Pass-2 verdict

**READY AFTER SPOT-FIXES (FOUR HIGH-SEVERITY).**

The chapter is fundamentally strong analytical-quantitative prose. Voice register holds analytical-third-person dominant throughout (with deliberate first-person register-architecture interjections at section-conclusion sites — F-V4 + F-V10). Apparatus residue: clean (Pass 1 §5 intact). Hedge phrases: clean. Connective-tissue clichés: clean. Meta-commentary verbatim patterns: clean. Named-subject consent: clean (Pass 1 §7 intact). Italicization: clean. Number formatting: clean. Section-break rhythm: clean. Chapter-cross-reference capitalization: clean. Cross-corpus IPG canonical-construction (commit `57575b1`) intact at line 168. Rent-seeking paragraph (line 122) voice-register-match verification ✓ HOLDS per F-V12.

The four HIGH-severity findings cluster around three patterns:
- **(a) Chapter-opening + chapter-climax cadence density** (F-V1 five-fold imperative anaphora at line 12; F-V2 six-fold "Different X / The same X" at line 176) — both at high-visibility rhetorical-pivot positions; both compounding to chapter-architecture cadence-density flag.
- **(b) Chapter-wide em-dash density** (F-V3 — 80 em-dashes; cumulative density flagged per em-dash discipline ratified 2026-05-21) — Ch 8 materially exceeds Ch 7's em-dash count; calibrated HIGH per the explicit discipline guidance that cumulative density IS the concern even when individual instances defensible.
- **(c) First-person register-drift chapter-wide** (F-V4 — five "I'll [verb] [number]" interjections across five cost-component sections) — chapter-wide pattern + strict-parallel cadence; calibrated HIGH because cumulative chapter-architecture-visible pattern.

The 9 MEDIUM findings cluster around four patterns:
- **(d) Tidy-parallel anaphoric cadence at chapter-architecture + section-architecture sites** (F-V5 section-header parallelism; F-V6 numerical-pivot cadence at three sections; F-V11 misreading-defense three-fold paragraph-opener) — most substantively earned + held-as-cadence-enacts-content per Ch 7 / Ch 9 calibration.
- **(e) Argumentative-engagement cadence** (F-V7 methodological-statement parallel paragraph; F-V8 YIMBY chapter-spine self-reference density; F-V9 closing-section short-declarative + Chapter-rule-of-three) — substantively earned analytical-essay engagement; most held-as-substantively-earned.
- **(f) First-person interjection cadence** (F-V10 line 222 declarative-pair) — coordinated with F-V4 disposition.
- **(g) Single-paragraph density flags** (F-V13 line 60 three-fold + appositive-pair em-dash triple; F-V12 line 122 rent-seeking paragraph audit ✓ HOLDS) — line 60 is the chapter's highest single-paragraph density; coordinated with F-V3 disposition.

The 7 LOW findings are style preferences; hold-as-is is the recommendation across all 7.

**No structural voice revision needed.** All findings are addressable via spot-fixes; the chapter's analytical-quantitative register, eight-component walk discipline, cross-case sweep + YIMBY engagement + misreading-defenses + closing-section structure are all sound. Chapter is on track for Phase-A completion after HIGH spot-fixes (+ any MEDIUM the author opts to apply) and the subsequent Pass-3 (audience-load) session.

The cumulative HIGH-finding-cluster (F-V1 chapter-opening + F-V2 chapter-climax + F-V3 chapter-wide em-dash + F-V4 first-person register-drift) is more substantial than Ch 7's Pass-2 HIGH-finding count (Ch 7 returned 0 HIGH); the difference reflects Ch 8's denser analytical-quantitative-walk register (the eight-component walk requires more imperative + parallel + appositive structure than Ch 7's analytical-thought-experiment walk) AND the em-dash discipline ratified 2026-05-21 (post-Ch 7 Pass 2) elevating the chapter-wide em-dash density to HIGH calibration. Ch 8 is therefore in the band that needs HIGH spot-fixes before submission-readiness, where Ch 7 needed only optional MEDIUM polish.

### §9.3 Phase-C disposition recommendation (sequenced)

For author ratification, in recommended sequence (lowest-risk to highest):

1. **F-V12 (line 122 rent-seeking paragraph audit — ✓ HOLDS verdict):** No spot-fix required at the paragraph level; verification verdict satisfies the rent-seeking workstream's Pass 2/3 routing. Em-dash count handled at F-V3. LOW-8 Conley grouping (Pass 1 §12.4) defers to Pass 3.
2. **F-V1 (chapter-opening five-fold "Price the X" anaphora):** Recommend RATIFY Option A (compress to colon-list). Cleanest drop of the named-pattern at chapter-opening claim-site; single-paragraph fix; preserves substantive eight-component preview.
3. **F-V2 (line 176 six-fold "Different X / The same X" cross-scenario sweep):** Recommend RATIFY Option A (compress to one substantive sentence). Cleanest drop of the six-fold standalone-paragraph cadence; reads as analytical cross-scenario summary in third-person register; no em-dash introduced.
4. **F-V4 (five-fold "I'll [verb] [number]" first-person interjection cadence):** Author judgment Option A (all-third-person) vs Option B (retain-one-convert-four) vs Option C (upstream-statement-restructure); recommend Option B as the lightest-touch balance. Cross-chapter consequence: aligns Ch 8 with its dominant analytical-third-person voice while preserving the chapter's accountability-on-the-page move at one strong site.
5. **F-V3 (chapter-wide em-dash density):** Author judgment Option A (targeted reduction) vs Option B (comprehensive sweep) vs Option C (spot-audit highest-density only). Recommend Option B (comprehensive sweep) per em-dash discipline ratified 2026-05-21; Option A is the second-best for targeted reduction. Cross-chapter consequence: Ch 8 alignment with em-dash discipline; sets calibration for any subsequent Phase B chapter re-audits.
6. **F-V10 (line 222 first-person declarative-pair):** Coordinate with F-V4 disposition. If F-V4 Option A applied → F-V10 Option B (compress to single third-person sentence). If F-V4 Option B applied → F-V10 Option C (retain first-person, vary structure).
7. **F-V13 (line 60 three-fold + appositive-pair em-dash triple):** Coordinate with F-V3 disposition. Recommend Option B (vary appositive-pair-em-dashes to colons; preserve three-fold anaphora) — reduces line 60 em-dash count from 5 to 3 while preserving the substantive three-categorization.
8. **F-V6 (three-fold numerical-pivot "Against [market price]" cadence):** Author judgment Option A (hold) vs Option C (vary line 166 only, no em-dash). Recommend Option C as the lightest-touch fix targeting the highest-density instance.
9. **F-V7 (methodological-statement parallel-structure paragraph at line 28):** Author judgment Option A (hold) vs Option B (collapse two-fold pairs) vs Option C (coordinate with F-V4). Recommend Option B if F-V4 Option B; Option C if F-V4 Option A.
10. **F-V5 + F-V8 + F-V9 + F-V11:** All recommended HOLD per substantively-earned + cadence-enacts-content + Ch 7 / Ch 9 cousin dispositions. Substance-drives-length governs.
11. **F-V14 + F-V15 + F-V16 + F-V17 + F-V18 + F-V19 + F-V20 (all 7 LOWs):** All recommended HOLD per Pass-2 default (style preferences; cadence-enacts-content; structurally load-bearing; F-V19 observation only — no spot-fix required).

**Cross-chapter consequence consolidated list (post-ratification work):**
- F-V3 (em-dash discipline): chapter-wide alignment sets precedent for any subsequent Phase B chapter re-audits.
- F-V4 (first-person register-architecture): cross-chapter inventory §8 "first-person line-starts" count may need methodological refinement to capture mid-paragraph interjections.
- Pass 3 (audience-load) is the next session for this chapter per per-prompt serial cadence.

**Estimated Phase C-β session scope:** 4 HIGH spot-fix decisions + 9 MEDIUM spot-fix decisions + 7 LOW hold-decisions = 20 total dispositions. Phase C-β session is moderate-to-heavy in size; chapter line-count post-application may net -10 to -15 lines (compression from F-V1 + F-V2 + F-V3 + F-V4 + F-V13 reductions) or +0 to -5 lines (lighter dispositions).

---

## §10. Ratification record

### §10.1 Author disposition — RATIFIED 2026-05-25

Author ratified all 20 §9.3 sequenced recommendations as recommended (ratify-as-recommended pattern; consistent with cascade-reconciliation 2026-05-21 ratification cadence + Amendment-C Interactive Ratification Protocol). All coordination dependencies resolved per the artifact's §9.3 conditional clauses (F-V7 → Option B given F-V4 → Option B; F-V10 → Option C given F-V4 → Option B).

| Finding | Severity | Ratified Option | Disposition |
|---|---|---|---|
| F-V1 (line 12 chapter-opening five-fold) | HIGH | **A** (compress to colon-list) | RATIFY APPLY |
| F-V2 (line 176 six-fold cross-scenario) | HIGH | **A** (compress to one substantive sentence) | RATIFY APPLY |
| F-V3 (chapter-wide em-dash density) | HIGH | **B** (comprehensive sweep) | RATIFY APPLY |
| F-V4 (five-fold "I'll" first-person) | HIGH | **B** (retain one strong site; convert four to third-person) | RATIFY APPLY |
| F-V5 (section-header parallelism) | MEDIUM | **A** (hold as-is) | RATIFY HOLD |
| F-V6 (numerical-pivot three-fold) | MEDIUM | **C** (vary line 166 only, no em-dash) | RATIFY APPLY |
| F-V7 (methodological-statement paragraph) | MEDIUM | **B** (collapse two-fold pairs; coordinated with F-V4 Option B) | RATIFY APPLY |
| F-V8 (YIMBY-engagement self-reference) | MEDIUM | **A** (hold as-is) | RATIFY HOLD |
| F-V9 (closing-section cadence) | MEDIUM | **A** (hold as-is) | RATIFY HOLD |
| F-V10 (line 222 first-person declarative-pair) | MEDIUM | **C** (retain first-person, vary structure; coordinated with F-V4 Option B) | RATIFY APPLY |
| F-V11 (misreading three-fold) | MEDIUM | **A** (hold as-is) | RATIFY HOLD |
| F-V12 (line 122 rent-seeking audit) | MEDIUM | **A** (hold as-is at paragraph level; em-dash count handled at F-V3) | RATIFY HOLD |
| F-V13 (line 60 three-fold + em-dash) | MEDIUM | **B** (vary appositive-pair em-dashes to colons; preserve three-fold anaphora; coordinated with F-V3) | RATIFY APPLY |
| F-V14 (section-opener two-fold) | LOW | HOLD (default) | RATIFY HOLD |
| F-V15 (line 12 standalone-pair) | LOW | HOLD (default) | RATIFY HOLD |
| F-V16 (within-sentence rule-of-three) | LOW | HOLD (default) | RATIFY HOLD |
| F-V17 (line 164 standalone headline-pivot) | LOW | HOLD (default) | RATIFY HOLD |
| F-V18 (line 200 four-declarative cluster) | LOW | HOLD (default) | RATIFY HOLD |
| F-V19 (register-toggle observation) | LOW | observation only (no spot-fix) | RATIFY HOLD |
| F-V20 (line 92 lineage-tradition closer) | LOW | HOLD (default) | RATIFY HOLD |

**Tally:** 8 RATIFY APPLY (F-V1, F-V2, F-V3, F-V4, F-V6, F-V7, F-V10, F-V13) + 12 RATIFY HOLD = 20 total dispositions.

**Phase C-β application scope:** 8 ratified spot-fixes applying to lines 12, 28, 40, 60, 62, 74, 96, 108, 122 (partial — F-V3 sweep only), 124, 138, 166, 176, 222 + chapter-wide em-dash sweep per F-V3 Option B (full pass through all 80 em-dashes, retaining only load-bearing rhetorical-pivot + parenthetical-pair + sentence-final-punch sites). Estimated post-application chapter line-count: 243 → 228–238 lines (net compression from F-V1 + F-V2 + F-V3 + F-V4 + F-V13 reductions; partial offset from F-V6 + F-V7 + F-V10 light edits). Cross-chapter cascade: none (all spot-fixes intra-Ch 8).

### §10.2 Phase C application (downstream session — to be filled in post-application)

- Application commit SHA: *(pending downstream Phase C-β session)*
- Chapter line-count post-application: *(pending)*
- Cross-chapter cascade required: **N** (all 8 spot-fixes intra-Ch 8 body prose)
- Pass 3 (audience-load) session ready: **Y** (after Phase C-β application lands)
- Stage 1c light coherence-check + Pass 3.3 light re-fire from coal-CO₂ methodology cascade (cross-thread #12 closure entry): still queued separately; can fire before, after, or in parallel with Phase C-β (no shared line touches)

---

## §11. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`.
- ✓ Did NOT re-run Pass 1 (fact-check) — referenced only for context; one incidental observation flagged forward at §8 (DOJ RealPage time-sensitive, already in pre-publication refresh checklist).
- ✓ Did NOT score Pass 3 (audience-load) — concerns flagged forward to that session at §7.
- ✓ Did NOT re-write paragraphs — proposed-revision options offered without applying.
- ✓ Did NOT contact named subjects.
- ✓ Did NOT propose new framework concepts.
- ✓ Verified chapter line count (243 lines, 2026-05-23) via `wc -l`.
- ✓ Verified all cited commits exist on `origin/main`: `5fe6af6` (Phase C application), `275b75a` (residual hedge-alignment), `cbef9bd` (Stage 1c Phase C cross-chapter cascade), `bc02767` (rent-seeking ratification), `a1e54d9` (rent-seeking proposal), `57575b1` (cross-corpus IPG canonical-construction artifact), `d1f6e2d` (Item 1 inline integral strip), `cacb82d` ($44B Program-vs-Trust-Fund correction).
- ✓ Built feature branch `claude/ch8-pass2-voice-polish-ad1947d16476c939c` from `origin/main`; rebased to current HEAD `b31ee2d` mid-session per fresh `origin/main` fetches (including `9befb92` Ch 8 cascade-reconciliation Phase C that landed mid-session) per CLAUDE.md branch discipline.
- ✓ Em-dash discipline ratified 2026-05-21 (Ch 3 Pass 3.2 F-V3) loaded as load-bearing; F-V3 calibration explicit per discipline guidance.
- ✓ Substrate-critical-editorial-input discipline applied (per memory entry ratified 2026-05-21) — chapter's existing prose audited as substrate; improvements surfaced before any application.
- ✓ All findings cite line numbers verified via `grep` against current chapter file state (post-Phase-C + post-Phase-C-β + post-rent-seeking-insertion + post-cross-corpus-IPG-ratification).

---

*End of Ch 8 Stage-3 Pass 2 (Voice-Polish) rigor pass — PROPOSED. Author ratification + Phase C-β spot-fix application is the next session for this chapter; Pass 3 (audience-load) follows per workstream #20 Phase A per-prompt serial cadence.*
