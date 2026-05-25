# Stage-3 Rigor Pass — Boston Review essay — Pass 3.2: Voice-polish [PROPOSED]

**Date:** 2026-05-23
**Status:** **RATIFIED + APPLIED 2026-05-23** via author "as recommended" signal. All 9 ratified spot-fixes + 2 consistency-completion drops applied to draft, landed in commit `b31ee2d`. Pass 3.5 forward-pointers (F-3.2-3 + F-3.2-14) carried + resolved at Pass 3.5 (commit `18d8f56`). Header ratification flag added via author "(A)" signal 2026-05-23 (file-header hygiene pass). (Originally PROPOSED 2026-05-23 in commit `7cd4444`; v3.1 Amendment C interactive ratification cycle complete.)
**Pass type:** Stage 3 Pass 3.2 — Voice-polish (second of five passes per v3.1 doctrine).
**Workstream:** Boston Review essay (Ch 5 → BR cascade allocation per `publishing/essays/_pipeline/cascade-plan_2026-05-06.md`).
**Artifact audited:** [`publishing/essays/boston-review-accountability-gap/essay.md`](../../publishing/essays/boston-review-accountability-gap/essay.md) (Stage 2 audience-blind flow draft, POST-Pass-3.1-spot-fix-application state, ratified 2026-05-23 per commit `fda6500`).
**Stage 1 brief (canonical voice register source):** [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_boston_review_essay_pre_draft_audience_structure_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-19_boston_review_essay_pre_draft_audience_structure_v1.0.0.md) (v1.0.1, ratified 2026-05-21; §7.9 amended 2026-05-23). §5 voice register + §8 apparatus exclusion + §13 Stage 3 protocol are load-bearing.
**Methodology anchor:** v3.1 audience-aware drafting discipline (Stage 3 Pass 3.2 per parent doctrine; v3.1 Amendment C interactive-ratification per-finding format with Options + Recommendation + Reasoning). Polarity: **CUT** (opposite to Pass 3.5's RESTORATION polarity).
**Path B compliance confirmation:** `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` was **NOT opened** during this Pass 3.2 audit session. Voice-polish calibration is grounded in Stage 1 brief §5 voice register + §8 apparatus exclusion list + the draft surface itself. No Ch 5 prose has been pasted into any proposed spot-fix in this artifact; all spot-fix prose is freshly generated from the brief's register.

---

## §0. Why this pass matters now

Pass 3.2 is the voice-polish pass in v3.1's five-pass Stage 3 cycle. It fires after Pass 3.1 fact-check ratification + spot-fix application (commit `fda6500`, 2026-05-23) and before Pass 3.3 audience-load acceptance. Its polarity is CUT: catch LLM-tic patterns, meta-commentary, rule-of-three cadence, em-dash crutches, hedge phrases, and sentence-length-variance failures that audience-load (Pass 3.3) and restoration polish (Pass 3.5) both miss.

The Boston Review essay's voice register is the most disciplined in the cascade. Brief §5 specifies third-person institutional-measurement throughout, no first-person memoir, no rule of three, no em-dash crutches, no "in short" / "ultimately" / "at its heart" connective tissue, no "the framework's response is..." meta-commentary, sentence-length variance (mix 5w and 25w), and a specific drop of the "framework" repeated self-reference. Brief §8 specifies the apparatus exclusion list that Pass 3.1 already swept clean (F-3.1-12 documented zero leakage). Pass 3.2 audits whether the prose surface delivers the §5 register without the LLM-tic patterns the discipline is calibrated to catch.

Three Stage-2-flagged structural decisions also surface for evaluation: the §I closing image ("The architecture reached for the throat of the case and closed on air"); the §VII subhead ("The architecture is engineered"); the §VI Norway compression ("Norway's fund is a Foreclosure Bond in everything but name"). The audit treats each as a discrete F-3.2-N finding.

One content-addition consideration surfaces: the four-traditions / supply-and-demand-blind-spot-on-permanent-foreclosure argument, recently routed to the Aeon essay carry-forward inventory (commit `1c5bcce`, 2026-05-22). The verbatim prose is Aeon-allocated. The conceptual move is fungible across essays; Pass 3.2 evaluates whether a fresh-prose §VI-opening (or §IV-pivot-opening) addition is voice-polish-scoped or whether it is Pass 3.5 developmental-edit territory.

---

## §1. Source artifacts read

1. THIS framing-paste (Pass 3.2 framing).
2. Stage 1 brief [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_boston_review_essay_pre_draft_audience_structure_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-19_boston_review_essay_pre_draft_audience_structure_v1.0.0.md) — read in full; §5 voice register + §8 apparatus exclusion list + §13 Stage 3 protocol are load-bearing for this pass.
3. Stage 2 audience-blind draft (POST-Pass-3.1-spot-fix-applied) [`publishing/essays/boston-review-accountability-gap/essay.md`](../../publishing/essays/boston-review-accountability-gap/essay.md) — read in full (109 lines).
4. Pass 3.1 fact-check artifact [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_boston_review_essay_stage3_fact_check_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-21_boston_review_essay_stage3_fact_check_v1.0.0.md) — context only (status RESOLVED via commit `fda6500`).
5. Stage 1c coherence verification [`tools/quality-gates/coherence-checks/boston-review-essay-workstream_stage1c_2026-05-21.md`](../../tools/quality-gates/coherence-checks/boston-review-essay-workstream_stage1c_2026-05-21.md) — context only.
6. Format reference (NOT a prose source): [`tools/rigor-passes/commons_bonds_ch5_stage_3_pass_2_voice_polish_2026-05-14_PROPOSED.md`](commons_bonds_ch5_stage_3_pass_2_voice_polish_2026-05-14_PROPOSED.md) — Ch 5 Pass 3.2 artifact for per-finding format reference; adapted to v3.1 Amendment C interactive-ratification format.
7. Aeon four-traditions commit `1c5bcce` — read commit message via `git log --format=full -1`. No verbatim text from the Aeon entry has been copied into this artifact's proposed prose.
8. Memory `feedback_em_dash_overuse.md` (ratified 2026-05-21 during Ch 3 Pass 3.2 F-V3 ratification) — em-dash use treated as a flag requiring active justification; default to commas/periods/restructure.

**Ch 5 (`manuscript/chapters/Chapter__5_TheAccountabilityGap.md`) was NOT opened.** Path B preemptive policy holds.

---

## §2. Per-finding artifacts

Per-finding format (v3.1 Amendment C interactive ratification): each F-3.2-N entry carries **Location** + **Current draft text** + **Voice register issue** + **Options (a / b / c)** + **Recommendation** + **Reasoning**.

Findings are organized by the three Stage-2-flagged structural decisions first (F-3.2-1 §I image; F-3.2-2 §VII title; F-3.2-3 §VI Norway compression), then HIGH / MEDIUM / LOW voice-polish findings, then the apparatus-exclusion re-sweep verification, then the four-traditions consideration.

---

### F-3.2-1 (MEDIUM) — §I closing image: "reached for the throat of the case and closed on air"

**Location:** draft §I, line 23 (paragraph close).

**Current draft text:**
> The conventional handles of criminal law (intent at a particular moment, harm causally traceable to a single instruction, an act committed within a statutory window) do not fit the shape of the harm. The architecture reached for the throat of the case and closed on air.

**Voice register issue:** Stage 2 Agent flagged for Pass 3.2 evaluation. The image is grammatically third-person and apparatus-clean, but the diction ("reached for the throat... closed on air") is at the rhetorical-image register rather than the institutional-measurement register the brief §5 specifies. The question is whether the image lands as institutional-analysis prose that uses a controlled metaphor or as too-rhetorical-for-BR. Two considerations push in opposite directions: (i) BR essays do permit controlled imagery at paragraph closes (Pettit, Anderson, Forrester, and Sandel all use figurative closes within institutional-analysis essays), and the image is functionally accurate to the legal-architectural argument (criminal law's grasp could not close on the structural harm); (ii) "reached for the throat" reads as crime-fiction or violence-imagery rather than legal-architectural register, and Joshua Cohen's political-philosophy register may register it as overheated.

**Options:**
- **(a) Keep verbatim.** The image lands as deliberate paragraph-close punctuation; the §I section closes on a structural-image beat that earns its rhetorical weight against the preceding clinical inventory of cost-to-revenue ratios. Risk: center-right reader (Tier 3 #12) or Cohen registers as overheated.
- **(b) Chisel to lower-temperature legal-architectural register.** Replace with: *"The conventional handles did not close around the harm."* Cost: loses the throat/air contrast that earned the image its punctuating force; benefit: holds institutional-measurement register through the §I close without rhetorical escalation.
- **(c) Replace with a structural-image at the same temperature as the rest of §I.** Possible: *"The architecture closed on absent ground."* or *"The architecture had no handle that fit the harm's shape."* Cost: loses the image's audible cadence; benefit: keeps the structural-failure beat in legal-architectural diction.

**Recommendation:** **(b)** — chisel to lower-temperature register. The §I close is doing load-bearing work establishing the section's institutional-measurement voice; an image that reads as violence-imagery rather than legal-architectural register risks the very register-break the brief §5 specifies against. The "conventional handles... did not close around the harm" formulation preserves the figurative beat (a hand closing around something) without the throat-violence reading, and reads as the kind of controlled metaphor BR's editorial brain ratifies.

**Reasoning:** Brief §5 specifies institutional-measurement register; the §I close should land in that register, not at rhetorical-flight altitude. Pettit and Cohen both write civic-republican essays that use figurative language sparingly and only when the figure is structurally faithful to the institutional argument. The "throat of the case" diction reads as crime-fiction rather than legal-architecture; the chiseled version preserves the structural-failure beat (the architecture had no purchase on the harm) without the temperature spike. Option (a) risks register-break; option (c) is a viable alternative if author prefers preserving the figurative beat structurally.

---

### F-3.2-2 (LOW) — §VII subhead: "The architecture is engineered"

**Location:** draft §VII, line 99 (subhead) + line 101 (echoed in opening) + line 109 (echoed in close).

**Current draft text:**
> ## VII. The architecture is engineered
>
> The accountability gap is not a force of nature. It is the residual produced by an architecture that was designed to do other work. The architecture is engineered. It can be engineered differently.
> [...]
> In Libby, the cost-severance ratio is forty to one. The accountability gap is what the architecture has not been asked to close. The architecture is engineered. The next question is whether it will be engineered to close it.

**Voice register issue:** Stage 2 Agent flagged the subhead for Pass 3.2 evaluation. Brief §9 allows Stage 2 to surface noun-phrase subheads; the question is whether the chosen subhead lands cleanly. Three issues: (i) the subhead is a declarative sentence, not a noun phrase — brief §9 specifies "Noun-phrase subheads (2-4 words) anchored to a scene, concept, or case"; the existing subhead is 4 words but is a verb-bearing sentence-clause; (ii) the phrase repeats three times in §VII (line 99 subhead + line 101 within first paragraph + line 109 within final paragraph), which is a deliberate rhetorical refrain but reads as cadence-heavy on close audit; (iii) the phrase echoes Pistor's "capital is a legal artifact" rhetorical shape (subject-is-Past-Participle structure) without crediting the source, which the civic-republican-tradition reader and Pistor-cluster reader (Tier 2 #6) may register.

**Options:**
- **(a) Keep verbatim subhead, reduce in-body repetitions from 3 → 2.** Drop the line-109 repetition; keep the subhead + the line-101 first-paragraph anchor. Reduces cadence-heaviness without losing the structural-refrain function.
- **(b) Replace subhead with a true noun-phrase per §9.** Candidates: *"The architecture, engineered"* (3w, participial noun phrase); *"An engineered architecture"* (3w, noun phrase); *"A residual by design"* (4w, noun phrase). Then keep one in-body anchor (line 101) and drop line 109. Cost: subhead loses some of its declarative-call-to-action weight; benefit: complies with §9 noun-phrase discipline + reduces refrain density.
- **(c) Keep subhead and all three repetitions.** Treats the three-fold repetition as a deliberate rhetorical refrain (subhead → opening → close echo). Cost: high cadence density that close audit registers as LLM-tic-adjacent; benefit: preserves the call-to-action structure the section is building toward.

**Recommendation:** **(b)** — replace subhead with true noun phrase per §9 ("The architecture, engineered" — 3w participial noun phrase), and reduce in-body repetitions from 3 → 2 by dropping line 109. The §9 noun-phrase discipline is explicit; the subhead should comply. The participial-noun-phrase form preserves the declarative weight (the architecture *is* engineered → the architecture, engineered) while satisfying the noun-phrase constraint.

**Reasoning:** Brief §9 is explicit: "Noun-phrase subheads (2-4 words) anchored to a scene, concept, or case." The current "The architecture is engineered" is a sentence, not a noun phrase. The participial-noun-phrase reformulation ("The architecture, engineered") preserves the rhetorical weight while complying with §9. Reducing the in-body repetition density from 3 → 2 (subhead + line 101 anchor; drop line 109) addresses the cadence-heaviness without losing the structural-refrain function. The Pistor-echo concern (Pistor's "capital is a legal artifact" rhetorical shape) is minor and resolves with the participial form. Option (a) preserves the declarative form but does not comply with §9; option (c) escalates the cadence density that close audit already flags.

---

### F-3.2-3 (MEDIUM) — §VI Norway compression: "Norway's fund is a Foreclosure Bond in everything but name"

**Location:** draft §VI, line 91 (paragraph close).

**Current draft text:**
> The Foreclosure Bond is the instrument designed to prevent the intergenerational version of being barred from. It is a bond posted against a future commitment, drawn against the extracted-value side of present activity, structured so that the option-value of the underlying stock — the rare earths in the deposit, the carbon budget in the atmosphere, the actuarial integrity of the intergenerational program — remains available to the future generation. Norway's fund is a Foreclosure Bond in everything but name.

**Voice register issue:** Stage 2 Agent flagged the compression for Pass 3.2 evaluation. The single-sentence claim ("Norway's fund is a Foreclosure Bond in everything but name") does load-bearing pivot work: it converts the abstract definition of the Foreclosure Bond into a concrete operating example, then immediately moves to the civic-republican grounding in the next paragraph. The voice-polish question is whether the compression lands or whether the §VI pivot is thin at the moment the essay names its most important comparative case. Three considerations: (i) the brief's §VI word budget (~850w; Decision #8 expansion) supports modest expansion; (ii) Pass 3.1 F-3.1-2 already restructured the surrounding Norway prose to two-event (1990 act + 1996 first deposit) rendering, so the lineage is well-anchored; (iii) the compression-to-one-sentence move *is* the rhetorical punch the paragraph is building toward — expanding it would dilute the claim's force.

**Options:**
- **(a) Keep compression.** The single-sentence claim lands as the paragraph's rhetorical pivot; expansion would dilute. The §VII Pass 3.5 developmental-edit lens can re-evaluate at the restoration-polarity pass if scene-anchor density needs work.
- **(b) Light expansion.** Replace with: *"Norway's fund is a Foreclosure Bond in everything but name. The legal architecture is in place; only the analytical category has been missing."* Adds a single follow-on sentence that names what's already done and what's missing without expanding the lineage. Cost: minor cadence shift; benefit: tightens the pivot to the §VII close ("the architecture is engineered").
- **(c) Defer to Pass 3.5.** Voice-polish acceptable as-is; flag for Pass 3.5 developmental-edit if scene-anchor density at the pivot is judged thin under the restoration-polarity lens.

**Recommendation:** **(c)** — defer to Pass 3.5. The compression is voice-polish-acceptable as-is; the question of whether the §VI pivot wants scene-anchor expansion is a restoration-polarity question that Pass 3.5 is built to handle. Pass 3.2's CUT polarity is the wrong instrument for expansion; flagging for Pass 3.5 pickup is the discipline-correct routing.

**Reasoning:** Brief §13 specifies Pass 3.2's polarity as CUT (opposite to Pass 3.5's RESTORATION). The §VI Norway compression is a candidate for expansion if expansion is needed, which is a Pass 3.5 lens question, not a Pass 3.2 lens question. The compression is not register-broken; it does not introduce LLM-tic patterns; it does not require chiseling. Option (b)'s light expansion is acceptable as a voice-polish-scoped move if author wants the §VII pivot tightened, but the discipline-correct routing is Pass 3.5. The Stage 2 Agent's original flag specified Pass 3.5 as the candidate venue; that flag is honored.

---

### F-3.2-4 (MEDIUM) — Em-dash density across the draft

**Location:** draft-wide. 29 em-dashes across ~4,500w body (~6.4 per 1,000w). Memory `feedback_em_dash_overuse.md` (ratified 2026-05-21 during Ch 3 Pass 3.2 F-V3 ratification) treats em-dash use as a flag requiring active justification rather than default punctuation.

**Distribution by section:**
- §I (lines 19, 23): 4 em-dashes (one inventory list at line 19; one paired-parenthetical at line 23)
- §II (lines 37, 39, 43): 6 em-dashes (one in quoted FCIC text at line 37, one paired-parenthetical at line 39, one paired-parenthetical + one stand-alone at line 43)
- §III (lines 47, 49, 55, 57): 6 em-dashes (one paired-parenthetical at 47; one stand-alone at 49; one stand-alone at 55; one paired-parenthetical at 57)
- §IV (lines 67, 69): 3 em-dashes (one paired-parenthetical at 67; one paired-parenthetical at 69)
- §V (lines 75, 79, 81): 4 em-dashes (one stand-alone at 75; one stand-alone at 79; one paired-parenthetical at 81)
- §VI (line 91): 2 em-dashes (one paired-parenthetical)
- §VII (lines 103, 105): 4 em-dashes (one paired-parenthetical at 103; one paired-parenthetical at 105)

**Voice register issue:** Brief §5 specifies "no em-dash crutches." Memory `feedback_em_dash_overuse.md` reinforces: em-dash use should be actively justified, not defaulted. The current draft's density is moderately high. Most paired-parenthetical em-dashes are doing legitimate work (introducing definitional asides like "the systematic transfer of harm from one party to another with less power to refuse it" at line 23, or list-restatements like "the rare earths in the deposit, the carbon budget in the atmosphere, the actuarial integrity of the intergenerational program" at line 91). But three subsets read as crutch usage:

1. **Inventory dashes at line 19** ("Medical care, environmental remediation, legal settlements, lost property values, ongoing health monitoring — the inventory has been compiled..."). A colon or restructure would serve.
2. **Editorial-comment dashes at line 49** ("body of law engineered to recognize, protect, and accumulate capital across borders and across generations") — wait, line 49 has no em-dash there; the dash at line 49 introduces "six legal instruments, each independently legitimate, each historically defensible, each refined over centuries of jurisprudence." This is a paired-parenthetical doing legitimate restatement work; leave.
3. **Stand-alone connector dashes at lines 55 and 75** ("supported largely by an excise tax on coal — and as of September 2024, the program's trust fund carried..." line 55; "name the mechanism, name the harm, name the debt" line 75 — the rule-of-three is preceded by colon, not em-dash, so this is misidentified; only line 55 is a stand-alone connector dash).

**Options:**
- **(a) Targeted reduction.** Identify ~6-8 specific em-dashes for restructure (line 19 inventory; line 55 connector; the line 67 + line 69 + line 105 + line 103 paired-parentheticals that could become commas without loss); leave the rest. Reduces density to ~4-5 per 1,000w (within memory's calibration range). Cost: light per-instance restructure work; benefit: voice-register tightening per §5 + memory discipline.
- **(b) Aggressive reduction.** Cut em-dash density to ≤3 per 1,000w (≤14 total) by restructuring all paired-parentheticals that could become commas. Cost: substantial restructure work; potential loss of cadence-variance benefit em-dashes provide; benefit: maximal §5 compliance.
- **(c) Hold.** The current density is moderate, not egregious; most em-dashes are doing legitimate paired-parenthetical work; the inventory-dash at line 19 and the connector at line 55 are individual cases that can be addressed at Pass 3.5 if developmental-edit surfaces them. Cost: residual em-dash-overuse-memory tension; benefit: preserves the cadence-variance the em-dashes contribute.

**Recommendation:** **(a)** — targeted reduction. Six specific em-dash conversions at ratification:

1. **Line 19** inventory dash → colon: *"the inventory of which has been compiled across decades..."* (or restructure to put the inventory after the categorical statement).
2. **Line 55** stand-alone connector dash → period + new sentence: *"...supported largely by an excise tax on coal. As of September 2024, the program's trust fund carried..."*
3. **Line 67** paired-parenthetical → commas: *"The foreclosed future-generation commons across resource extraction, the rare earths, the aquifers, the topsoil, the marine fisheries, being drawn down..."* (or restructure to standalone sentence).
4. **Line 69** paired-parenthetical → restructure: integrate the "reparations economics for the backward-looking case, environmental and sovereign-wealth bond traditions for the forward-looking case" into the surrounding sentence with comma-bounded apposition or split to a new sentence.
5. **Line 103** paired-parenthetical → restructure: *"The two-instrument framing, the Restitution Bond for the harm already done and the Foreclosure Bond for the harm not yet done, does not propose..."* (commas replacing em-dashes).
6. **Line 105** paired-parenthetical → restructure: *"The American architectures of accountability, for the asbestos in the attic, for the oil in the Gulf, for the foreclosure in the household, for the obligation in the actuarial table, were chosen."* (commas replacing em-dashes).

The remaining ~17 em-dashes can hold; most are doing legitimate paired-parenthetical or definitional-aside work that comma-bounded apposition would not serve as cleanly.

**Reasoning:** Memory `feedback_em_dash_overuse.md` (ratified 2026-05-21) treats em-dash use as requiring active justification. 29 em-dashes across ~4,500w is moderate-but-tight against the memory's calibration. Brief §5 specifies "no em-dash crutches" — the targeted reductions address the specific cases that read as crutch usage rather than as deliberate punctuation. Option (b)'s aggressive reduction would cost the cadence-variance em-dashes contribute when used sparingly; option (c) leaves the most visible crutch cases unaddressed. Option (a)'s six targeted cuts preserve the deliberate paired-parenthetical work while addressing the specific crutch instances.

---

### F-3.2-5 (LOW) — Rule-of-three cadence at line 75 ("name the mechanism, name the harm, name the debt")

**Location:** draft §V, line 75.

**Current draft text:**
> Ta-Nehisi Coates's 2014 essay "The Case for Reparations" set the argument-architecture: name the mechanism, name the harm, name the debt.

**Voice register issue:** The colon-introduced rule-of-three ("name X, name Y, name Z") is the most visible rule-of-three pattern in the draft. Brief §5 specifies "No rule of three." Two considerations push in opposite directions: (i) the rule-of-three here is doing structural-citation work — it characterizes Coates's argument-architecture in Coates's own rhetorical register; the parallelism is a citation move rather than an LLM-tic move; (ii) it nonetheless is a rule-of-three; brief §5 is strict.

**Options:**
- **(a) Keep.** The rule-of-three is doing structural-citation work; it characterizes Coates's argument by reproducing Coates's own rhetorical shape. The discipline against rule-of-three is calibrated against LLM-tic instances, not citation-shape moves. Cost: technical §5 violation; benefit: preserves the citation's argumentative function.
- **(b) Restructure to drop the third element.** Replace with: *"Ta-Nehisi Coates's 2014 essay 'The Case for Reparations' set the argument-architecture: name the mechanism and name the harm; the debt is what follows."* Cost: loses Coates's tripartite rhetoric; benefit: §5 compliance.
- **(c) Restructure to a four-element parallelism.** Replace with: *"Ta-Nehisi Coates's 2014 essay 'The Case for Reparations' set the argument-architecture: name the mechanism that produced the harm, name the cohort that bore it, name the debt, and name the party against whom the debt stands."* Cost: substantial reformulation; benefit: breaks the three-element cadence into a four-element parallel that does not read as rule-of-three.

**Recommendation:** **(a)** — keep. The rule-of-three is doing citation-shape work, not LLM-tic work; it characterizes Coates's argument-architecture by reproducing Coates's own rhetorical register; the brief's §5 discipline is calibrated against generative LLM-tic instances rather than citation-shape moves. The brief's named-tradition attribution discipline (§10) supports preserving Coates's own rhetorical shape when citing his argument-architecture.

**Reasoning:** Brief §5 specifies "No rule of three" — but the discipline-relevant test is whether the rule-of-three is generative LLM-cadence or whether it is faithful to a cited source's own rhetoric. Coates's "The Case for Reparations" deploys exactly this naming-rhetoric across the essay; the three-element parallelism is structurally faithful to the citation. The Sandy Darity / Coates-tradition reader (Tier 2 #5 + Tier 3 #14) will recognize the citation-shape move as honoring Coates rather than as LLM-cadence. Option (b) sacrifices the citation faithfulness; option (c) over-engineers around a non-problem. Brief §5's discipline holds against generative rule-of-three (LLM-cadence), not against citation-faithful rule-of-three.

---

### F-3.2-6 (MEDIUM) — Rule-of-three cadence at line 69 ("Both directions are real. Both have measurable magnitudes. Both have specific legal instruments...")

**Location:** draft §IV, line 69.

**Current draft text:**
> Both directions are real. Both have measurable magnitudes. Both have specific legal instruments that the existing architecture has already developed for analogous purposes — reparations economics for the backward-looking case, environmental and sovereign-wealth bond traditions for the forward-looking case — and that have been deployed in narrow contexts without being generalized to the case-class the accountability gap describes.

**Voice register issue:** "Both X. Both Y. Both Z." is the canonical declarative-three-in-a-row LLM-cadence brief §5 specifies against ("It changed me. It humbled me. It made..." declarative-three-in-a-row). The three-clause anaphoric repetition is generative-LLM-cadence rather than citation-faithful. This is the clearest rule-of-three violation in the draft.

**Options:**
- **(a) Break the anaphora; collapse to two parallel clauses + one expanded clause.** Replace with: *"Both directions are real, and both have measurable magnitudes. The existing architecture has already developed specific legal instruments for analogous purposes — reparations economics for the backward-looking case, environmental and sovereign-wealth bond traditions for the forward-looking case — and has deployed them in narrow contexts without generalizing to the case-class the accountability gap describes."* Cost: loses the "Both Z" anaphoric beat; benefit: removes the declarative-three-in-a-row cadence.
- **(b) Restructure to single complex sentence.** Replace with: *"Both directions are real and have measurable magnitudes, and for each the existing architecture has already developed specific legal instruments — reparations economics for the backward-looking case, environmental and sovereign-wealth bond traditions for the forward-looking case — deployed in narrow contexts without being generalized to the case-class the accountability gap describes."* Cost: a single long sentence; benefit: complete removal of the anaphoric cadence.
- **(c) Keep.** The three-clause anaphora is doing structural-paragraph-opening work that signals the §IV pivot's bidirectional symmetry. Cost: the most visible rule-of-three in the draft remains.

**Recommendation:** **(a)** — break the anaphora to two parallel + one expanded. The cadence-break removes the LLM-cadence reading while preserving the bidirectional-symmetry pivot the paragraph is doing. The expanded final clause ("The existing architecture has already developed specific legal instruments...") sustains the §IV pivot's argumentative function without the declarative-three-in-a-row cadence.

**Reasoning:** This is the clearest rule-of-three violation in the draft per brief §5. The "Both X. Both Y. Both Z." structure is declarative-three-in-a-row LLM-cadence; the brief's §5 register-discipline is precisely calibrated to catch it. Option (a) preserves the bidirectional-symmetry signal (which the paragraph needs) while removing the cadence; option (b) over-restructures into a single long sentence that loses sentence-length-variance benefit; option (c) leaves the most visible violation unaddressed.

---

### F-3.2-7 (MEDIUM) — Anaphoric five-clause cadence at line 65 (§IV backward-harm catalog)

**Location:** draft §IV, line 65.

**Current draft text:**
> There is the harm already realized. The four hundred dead in Libby. The eleven on the Deepwater rig and the four to eight billion oysters in the Gulf below it. The five million households who completed foreclosure between 2008 and 2012. The black-lung claimants whose conditions were diagnosed under federal program rules and whose treatment costs ran past the program's resources. The McDowell County coal communities whose extracted value moved to coastal capital markets and left behind a public-health and infrastructure tail. This is backward-looking accountability: the cost has been borne, the question is whether it can still be priced and discharged.

**Voice register issue:** Five-clause anaphoric sentence-fragment cadence ("The four hundred... The eleven... The five million... The black-lung... The McDowell..."). Each clause is a noun-phrase fragment introduced by "The," and the parallel structure compounds. This is rule-of-five rather than rule-of-three, but the brief §5 register-discipline against declarative-anaphora applies a fortiori. The cadence is the most visible parallel-clause stack in the draft.

**Options:**
- **(a) Convert to a complete-sentence inventory with cadence-break.** Replace with: *"There is the harm already realized. Four hundred dead in Libby. Eleven on the Deepwater rig and four to eight billion oysters in the Gulf below it. Five million households who completed foreclosure between 2008 and 2012; black-lung claimants whose conditions were diagnosed under federal program rules and whose treatment costs ran past the program's resources; McDowell County coal communities whose extracted value moved to coastal capital markets and left behind a public-health and infrastructure tail. This is backward-looking accountability..."* Cost: still some parallel structure; benefit: breaks the five-clause anaphora ("The..." → "The..." → "The...") by dropping the leading article on each clause and using semicolons to chain the longer clauses.
- **(b) Restructure to mixed sentence types.** Replace with: *"There is the harm already realized. Four hundred died in Libby. Eleven workers and four to eight billion oysters were lost at Deepwater. Five million households completed foreclosure between 2008 and 2012. Black-lung claimants ran past the program's resources for treatment costs. McDowell County coal communities watched extracted value move to coastal capital markets and left behind a public-health and infrastructure tail. This is backward-looking accountability..."* Converts each fragment into a complete sentence with active verb. Cost: loses the inventory-cadence the paragraph is building; benefit: removes the anaphoric "The..." stack and introduces sentence-length variance.
- **(c) Keep as deliberate parallel-clause inventory.** The five-clause inventory is doing structural work — each clause names a different cost-bearer cohort across the cases the essay has already established. The anaphoric cadence is faithful to the §IV pivot's inventory function. Cost: most visible parallel-clause stack remains; benefit: preserves the inventory's argumentative density.

**Recommendation:** **(b)** — restructure to mixed sentence types with active verbs. The anaphoric five-clause cadence is the most visible declarative-LLM-cadence pattern in the draft; sentence-length variance per brief §5 is the discipline-correct response. Each cohort gets a complete sentence rather than a noun-phrase fragment; the inventory function is preserved without the cadence stack. Active verbs ("died," "were lost," "completed," "ran past," "watched... move") restore agency to the cost-bearers, which is also the §IV paragraph's structural intent.

**Reasoning:** Brief §5 specifies "Mix 5w and 25w sentences" and "declarative-three-in-a-row cadence should be broken." Five-clause anaphoric sentence-fragment stack ("The four hundred... The eleven... The five million... The black-lung... The McDowell...") is the most visible cadence stack in the draft. Option (b)'s active-verb restructure removes the cadence stack, restores agency to the cost-bearers, and introduces sentence-length variance. Option (a) preserves more of the inventory feel but still reads as parallel-clause stack; option (c) leaves the LLM-cadence pattern unaddressed. The extraction-affected reader (Tier 3 #13) is precisely the pressure-test character for whom restoring agency to the cost-bearers (rather than rendering them as noun-phrase fragments) matters most.

---

### F-3.2-8 (MEDIUM) — Anaphoric four-clause cadence at line 67 (§IV forward-harm catalog)

**Location:** draft §IV, line 67.

**Current draft text:**
> And there is the harm not yet realized. The climate cost of present emissions, which compounds against future-generation balance sheets. The intergenerational obligation under Social Security, structurally guaranteed to fall on whichever cohort is in working age when the demographic window closes. The foreclosed future-generation commons across resource extraction — the rare earths, the aquifers, the topsoil, the marine fisheries — being drawn down against the option-value of leaving them intact. The decommissioning liabilities for thousands of offshore platforms, abandoned wells, surface mines, whose bonded coverage runs systematically short of their reclamation cost. This is forward-looking accountability: the cost has not yet been borne, the question is whether the architecture can be made to carry it before the bill matures.

**Voice register issue:** Same pattern as F-3.2-7 (anaphoric four-clause sentence-fragment stack mirroring the backward-harm inventory at line 65). "The climate cost... The intergenerational obligation... The foreclosed future-generation commons... The decommissioning liabilities..." The §IV paragraph pair (lines 65 + 67) is the most cadence-heavy moment in the draft.

**Options:**
- **(a) Restructure to mixed sentence types with active verbs (parallel to F-3.2-7 Option b).** Replace with: *"And there is the harm not yet realized. The climate cost of present emissions compounds against future-generation balance sheets. Social Security's intergenerational obligation is structurally guaranteed to fall on whichever cohort is in working age when the demographic window closes. The foreclosed future-generation commons across resource extraction — the rare earths, the aquifers, the topsoil, the marine fisheries — are being drawn down against the option-value of leaving them intact. Decommissioning liabilities for thousands of offshore platforms, abandoned wells, and surface mines run systematically short of their reclamation cost in bonded coverage. This is forward-looking accountability..."* Each fragment becomes a complete sentence with active verb. Symmetric with F-3.2-7 Option (b).
- **(b) Hybrid restructure.** Keep the first one or two fragments but break to complete sentences for the last two. Cost: asymmetric with F-3.2-7; benefit: preserves some of the inventory cadence.
- **(c) Keep.** Treats the parallel-fragment cadence as deliberate bidirectional-symmetry signaling (the §IV paragraph pair lines 65 + 67 mirrors each other in cadence as well as structure). Cost: leaves both cadence stacks unaddressed.

**Recommendation:** **(a)** — restructure symmetrically with F-3.2-7. The bidirectional symmetry the §IV paragraph pair signals can be preserved through symmetric restructure (active verbs in both paragraphs) without preserving the anaphoric cadence stack. The §IV pivot is the essay's structural-symmetry moment; symmetric handling of both catalogs is the discipline-correct move.

**Reasoning:** Symmetric reasoning to F-3.2-7. The §IV pivot paragraph pair is the most cadence-heavy moment in the draft; addressing both catalogs (line 65 + line 67) symmetrically preserves the bidirectional-symmetry signaling while removing the LLM-cadence pattern. Brief §5 sentence-length-variance discipline supports the active-verb restructure on both catalogs.

---

### F-3.2-9 (LOW) — Repetition cadence at line 97 ("It does not require... It does not require... What it requires...")

**Location:** draft §VI, line 97 (paragraph open).

**Current draft text:**
> The Foreclosure Bond does not require new philosophical foundations. The civic-republican tradition has supplied them. It does not require new financial instruments. The sovereign-wealth funds, the reclamation bonds, the decommissioning bonds, and the actuarial-trust mechanisms have all been built, refined, and operated at industrial scale. What it requires is the institutional decision to bind the present's extractive activity to the forward-funded preservation of the option-value the activity draws against. The decision is contingent. Norway made it. The American policy architecture has, repeatedly, declined to.

**Voice register issue:** The "X does not require A... [B]. It does not require... What it requires is..." cadence is a three-part rhetorical structure that lands as deliberate rather than as LLM-cadence (the third element inverts the polarity, which marks it as crafted rather than generative). Two close-audit notes: (i) the "Norway made it. The American policy architecture has, repeatedly, declined to." close lands as the §VI rhetorical-punctuation beat (4w + 9w sentence-length variance is exactly the §5-prescribed mix); (ii) the cadence is not declarative-three-in-a-row in the LLM-tic sense — the inverted-third-element structure ("X does not... X does not... what X does require...") is a classical rhetorical move.

**Options:**
- **(a) Keep.** The three-part structure with inverted-third-element is deliberate rhetoric, not LLM-cadence; the §VI close earns its rhetorical weight against the preceding analytical argument.
- **(b) Light tighten.** Combine the first two clauses: *"The Foreclosure Bond does not require new philosophical foundations — the civic-republican tradition has supplied them — or new financial instruments..."* Cost: introduces another em-dash pair (against F-3.2-4); benefit: tightens the cadence.
- **(c) Restructure to flow.** Replace with: *"The Foreclosure Bond does not require new philosophical foundations or new financial instruments. The civic-republican tradition has supplied the foundations; the sovereign-wealth funds, the reclamation bonds, the decommissioning bonds, and the actuarial-trust mechanisms have built, refined, and operated the instruments at industrial scale. What it requires is the institutional decision..."* Cost: minor restructure; benefit: removes the parallel-clause stack while preserving the inverted-third-element structure.

**Recommendation:** **(a)** — keep. The three-part structure with inverted-third-element is deliberate rhetoric that earns its weight; the §VI close lands cleanly. The cadence is distinguishable from generative LLM-tic by the inverted-third-element move. Option (b) trades a rule-of-three concern for an em-dash concern; option (c) over-restructures around a non-problem.

**Reasoning:** Brief §5's rule-of-three discipline is calibrated against generative LLM-cadence (declarative-three-in-a-row identical-structure). The "X does not require A... X does not require B... What X requires is C..." structure inverts polarity in the third element, which is a classical rhetorical move (negation-negation-affirmation) rather than LLM-tic. The §VI paragraph close lands as the section's rhetorical-punctuation beat with the prescribed sentence-length variance ("The decision is contingent. Norway made it. The American policy architecture has, repeatedly, declined to."). Option (a) preserves the deliberate rhetoric.

---

### F-3.2-10 (LOW) — "this account" repetition (compressed "the framework" surrogate)

**Location:** draft §IV line 71; §VI line 91. Two instances.

**Current draft text (line 71):**
> The two instruments that follow are not new categories invented for the occasion. They are the names this account uses to gather the existing legal-architectural moves into a coherent two-instrument architecture: one looking backward at the harm already done, one looking forward at the harm not yet done. The Restitution Bond. The Foreclosure Bond.

**Current draft text (line 91):**
> The Foreclosure Bond is the name this account uses for the generalization of this architecture to the full forward-looking case-class.

**Voice register issue:** Brief §8 specifies "compress 'the framework' as repeated self-reference; reserve naming for the section where the two-instrument architecture is introduced." The draft uses "this account" as the compressed surrogate. Pass 3.1 F-3.1-12 documented this as the apparatus-exclusion-compliant approach. Voice-polish question: is "this account" doing meta-commentary work that the brief §5 discipline against "the framework's response is..." catches? Two considerations: (i) "this account" is a less-loaded surrogate than "the framework" (no Ch 5 apparatus tail); (ii) two instances across the draft is light usage; the §VII close avoids the surrogate entirely.

**Options:**
- **(a) Keep both instances.** The surrogate is doing minimal-load self-reference work; two instances across ~4,500w is light usage; brief §8 compression discipline is satisfied.
- **(b) Drop one instance.** Restructure line 91 to: *"The Foreclosure Bond is the name for the generalization of this architecture to the full forward-looking case-class."* Cost: removes a small self-reference; benefit: minor tightening.
- **(c) Drop both instances.** Restructure line 71 to: *"The two instruments that follow are not new categories invented for the occasion. They gather the existing legal-architectural moves into a coherent two-instrument architecture..."*; line 91 as in (b). Cost: requires minor sentence restructure; benefit: removes all "this account" self-reference, aligning with brief §5's "no meta-commentary" register at the strictest reading.

**Recommendation:** **(c)** — drop both instances. The brief §5 discipline against meta-commentary tics is strict; even minimal-load self-reference reads as authorial-presence in third-person institutional-measurement register. The restructured sentences read more cleanly without the "this account" surrogate.

**Reasoning:** Brief §5 specifies third-person institutional-measurement register; brief §8 specifies compression of "the framework" repeated self-reference. The "this account" surrogate is compliant with §8's letter but minor meta-commentary by §5's spirit. Two instances is light, but the §5 discipline is calibrated tight for BR's editorial brain. Option (c)'s cleaner restructure aligns with the strictest reading. The reformulation costs nothing argumentatively.

---

### F-3.2-11 (LOW) — Hedge phrase sweep: CLEAN

**Location:** entire draft (sweep).

**§5 hedge-phrase specification:** No "it might be argued that..." / "one might say that..." / "in some sense..." / "to a certain extent..." / academic-defensive-register.

**Sweep result:** Zero instances of any §5 hedge-phrase pattern. The draft's voice is direct and declarative throughout. Closest near-hedges are:
- Line 47 "Both readings have force. The deeper reading is more uncomfortable." (Not a hedge — explicit comparative-claim register.)
- Line 23 "It meant only that the legal architecture available to the prosecution was not structurally suited..." (Not a hedge — load-bearing precision claim.)

**Options:**
- **(a) No change.** Hedge-phrase sweep is clean.

**Recommendation:** **(a)** — no change. Positive verification finding documenting that Stage 2 audience-blind drafting + Pass 3.1 spot-fix application operated within the §5 register without hedge-phrase residue.

**Reasoning:** Brief §5 specifies direct, plain prose without academic hedging. The draft sweep returns zero violations. Counted as LOW for completeness.

---

### F-3.2-12 (LOW) — Meta-commentary tic sweep: CLEAN

**Location:** entire draft (sweep).

**§5 meta-commentary specification:** No "the framework's response is..." / "what the framework names is..." / "the framework's choice of X as the umbrella term is deliberate..." / "the plain definition is this:" / "that is the whole sentence" / "this is the point at which X" / similar self-commentary patterns.

**Sweep result:** Zero instances of any §5 meta-commentary pattern. The "this account" surrogate (covered in F-3.2-10) is the closest pattern to meta-commentary in the draft. The Stage 2 drafter's discipline of avoiding meta-commentary tics held through the audience-blind drafting + Pass 3.1 spot-fix application.

**Options:**
- **(a) No change.** Meta-commentary tic sweep is clean (modulo the F-3.2-10 "this account" handling).

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** The meta-commentary discipline operating cleanly through the audience-blind regime is empirical confirmation that the §5 register is internalized in the Stage 2 drafter's output. Counted as LOW for completeness.

---

### F-3.2-13 (LOW) — Apparatus-exclusion re-sweep: CLEAN (confirms Pass 3.1 F-3.1-12)

**Location:** entire draft (sweep, post-Pass-3.1-spot-fix-application state).

**§8 apparatus exclusion list re-sweep:** Zero instances of cluster-γ; RCV / Residual Commons Value; CSD / Cost Severance Damages; Commons Inversion Test; "four gates"; "three ways of counting"; Method 1/2/3 numbering; Hotelling Identity; Technical Appendix §-references; Greek letters; subscripts; Cᵢ-style notation; displayed equations.

**Sweep result:** Apparatus-exclusion-list compliance remains CLEAN post-Pass-3.1-application. Pass 3.1 spot-fixes (F-3.1-1 Hamilton flag close; F-3.1-2 Norway two-event rendering; F-3.1-3 fifteen-years → post-crisis-window; F-3.1-4 Black Lung excise-tax + §7.9 brief amendment; F-3.1-5 Pettit neo-Roman tightening) did not introduce any apparatus terms. The Path B preemptive policy held through both Stage 2 + Pass 3.1.

**Options:**
- **(a) No change.** Apparatus-exclusion-list compliance is clean.

**Recommendation:** **(a)** — no change. Positive verification finding confirming Pass 3.1 F-3.1-12 still holds.

**Reasoning:** Pass 3.1 F-3.1-12 documented zero apparatus-exclusion-list violations at the pre-spot-fix-application state. The Pass 3.2 re-sweep confirms the post-spot-fix-application state remains clean — Pass 3.1's spot-fixes were prose-additive (Norway two-event clause, Black Lung excise-tax structural-contrast clause, Pettit neo-Roman tightening) without introducing apparatus terms. Counted as LOW for completeness; the audit is unambiguously positive.

---

### F-3.2-14 (MEDIUM) — Four-traditions argument consideration: PASS 3.5 DEFERRAL

**Location:** candidate §VI opening or §IV bidirectional-pivot opening.

**Voice register issue context:** Author + PM session surfaced a candidate content-addition consideration: a passage articulating the four-traditions (Marx / Ostrom / Daly / Hartwick) + supply-and-demand-blind-spot-on-permanent-foreclosure argument as motivation for the Foreclosure Bond. The verbatim prose is Aeon-allocated per upstream commit `1c5bcce` (Aeon essay carry-forward inventory Entry #1). The argument is fungible across essays; the prose is not (per cascade plan single-venue prose allocation + Path B "same arc + same ideas + different sentences" discipline extended cross-essay).

**Pass 3.2 evaluation:**

The voice-polish-scoped vs. Pass 3.5-scoped question turns on whether the §VI/§IV opening currently feels motivationally thin in a way that voice-polish (CUT polarity) would address.

Reading the current §IV pivot (line 63) and §VI opening (line 87):
- §IV opening (line 63): *"Once the architecture is in view, the accountability gap becomes legible as a bidirectional structure."* — establishes the bidirectional frame; no theoretical-tradition motivation needed for the pivot to land.
- §VI opening (line 87): *"The forward-looking instrument has a different lineage. It begins with John Hartwick's 1977 paper..."* — the Hartwick anchor is the lineage opener; the four-traditions move would add a *broader* theoretical frame (why supply-and-demand cannot price what's not present at the moment of sale) that the Hartwick + Norway + Pettit lineage anchors but does not itself articulate.

The four-traditions move is **adding content**, not chiseling existing content. Brief §13 specifies Pass 3.2's polarity as CUT; Pass 3.5's polarity is RESTORATION/EXPANSION. A new theoretical-frame opening at §VI or §IV is structurally a restoration / expansion move, not a chiseling move. It is Pass 3.5-scoped.

Two additional considerations strengthen the Pass 3.5 routing:
1. The Aeon carry-forward inventory caveat explicitly flags drafting concerns: *"define 'permanent foreclosure' explicitly (crystallization move); Marx-tradition completeness flag (Foster metabolic-rift extension); verify Hartwick + Daly + Ostrom attribution glosses; reconcile literal-future-generations reading with present-day-structurally-excluded analog (McDowell case)."* Each of these would need fresh handling for the BR essay (different audience: civic-republican / democratic-theory readers; different lineage anchors: Pettit / Skinner / Parfit already in §VI rather than the four-traditions framing). The drafting is non-trivial.
2. The center-right pressure-test reader (Tier 3 #12) and Public-Choice tradition reader cluster will read a Marx-inclusive four-traditions framing closely; the brief's non-partisan-framing discipline (§10) requires the framing to land as institutional analysis rather than as left-coded scholarship. This is a Pass 3.4 adversarial-robustness question that fires only if Pass 3.3 raises it.

**Options:**
- **(a) Voice-polish-scoped: propose fresh-prose §VI-opening (or §IV-pivot-opening) addition now.** Generate fresh BR-register prose articulating the four-traditions / permanent-foreclosure-supply-demand-blind-spot argument as motivation. Different prose from the Aeon-allocated verbatim. Add as F-3.2-N spot-fix proposal at ratification.
- **(b) Pass 3.5 deferral.** Flag for Pass 3.5 developmental-edit pickup; do not propose voice-polish-scoped prose. Pass 3.5's RESTORATION polarity is the discipline-correct routing for new theoretical-frame content; Pass 3.5 also has the budget (50K-80K tokens per chapter / essay) to handle the non-trivial drafting concerns the Aeon carry-forward inventory flags.
- **(c) Out-of-scope; do not pursue.** The §VI Hartwick opening + §VII civic-republican close land sufficiently without the broader theoretical-tradition framing; the four-traditions argument is genuinely Aeon-allocated rather than fungible.

**Recommendation:** **(b)** — Pass 3.5 deferral. Pass 3.2's polarity (CUT) is the wrong instrument for new theoretical-frame content; Pass 3.5 (RESTORATION) is the correct routing. The Aeon carry-forward inventory's drafting caveats indicate the four-traditions move requires fresh handling for BR's civic-republican / democratic-theory readership (different lineage anchors than the Aeon framing) that exceeds voice-polish scope. The §VI opening should be revisited at Pass 3.5 with the developmental-edit lens: does the section's analytical pivot benefit from a broader theoretical-frame anchor (four-traditions / supply-and-demand-blind-spot-on-permanent-foreclosure) before launching into the Hartwick lineage, or does the Hartwick anchor stand on its own?

**Reasoning:** Brief §13 specifies Pass 3.2's polarity as CUT, opposite to Pass 3.5's RESTORATION. New theoretical-frame content is structurally a RESTORATION move (the §VI opening currently moves from the §IV bidirectional pivot directly into the Hartwick lineage; the four-traditions / supply-and-demand-blind-spot move would *add* a layer of theoretical motivation between the §IV pivot and the §VI Hartwick anchor). The discipline-correct routing is to flag this as a Pass 3.5 candidate finding rather than to propose voice-polish-scoped prose now. The Aeon carry-forward inventory caveats reinforce this — the four-traditions framing requires audience-specific fresh handling for BR's civic-republican-tradition readership that voice-polish scope cannot accommodate.

**Pass 3.5 forward-pointer language for the artifact:**
- Candidate finding: "Should §VI opening (line 87) be expanded to include a four-traditions / permanent-foreclosure-supply-demand-blind-spot theoretical-frame motivation before the Hartwick lineage anchor, or does the §IV→§VI structural pivot (bidirectional accountability → forward-looking instrument lineage) hold without the intermediate theoretical-frame?"
- Constraint: fresh BR-register prose; **must not paste the Aeon-allocated verbatim passage from `publishing/essays/aeon-mask-of-abundance/carry-forward-inventory.md`**; same arc + same ideas + different sentences per Path B extended cross-essay.
- Lineage anchors for BR-specific reframe: civic-republican tradition (Pettit / Skinner already in §VI) + reparations-economics tradition (Darity-Mullen already in §V) + Hartwick + Norway already in §VI. The four-traditions framing for BR would substitute Pettit-Skinner-Parfit for Marx where the BR essay's existing lineage scaffolding already does the political-philosophy work.

---

## §3. Aggregate verdict

| Severity | Count | Resolution path |
|---|---|---|
| HIGH | 0 | — |
| MEDIUM | 6 | F-3.2-1 (§I image chisel); F-3.2-3 (§VI Norway compression — Pass 3.5 deferral); F-3.2-4 (em-dash density — targeted reduction); F-3.2-6 (line 69 "Both X. Both Y. Both Z." rule-of-three); F-3.2-7 (line 65 five-clause anaphora); F-3.2-8 (line 67 four-clause anaphora); F-3.2-14 (four-traditions consideration — Pass 3.5 deferral) |
| LOW | 7 | F-3.2-2 (§VII subhead noun-phrase); F-3.2-5 (line 75 Coates rule-of-three — keep as citation-shape); F-3.2-9 (line 97 inverted-third-element — keep); F-3.2-10 ("this account" surrogate — drop both); F-3.2-11 (hedge-phrase sweep — clean); F-3.2-12 (meta-commentary sweep — clean); F-3.2-13 (apparatus-exclusion re-sweep — clean) |
| **Total** | **14** | — |

(Note: F-3.2-14 surfaces as MEDIUM because it carries a forward-pointer disposition for Pass 3.5; F-3.2-3 similarly. The remaining four MEDIUM findings — F-3.2-1, F-3.2-4, F-3.2-6, F-3.2-7, F-3.2-8 — are direct voice-polish spot-fix proposals at ratification. F-3.2-2 sits at LOW because the subhead-form change is small but structurally important.)

**Overall pass verdict:** **CONDITIONAL — 0 HIGH findings; 6 MEDIUM findings requiring author disposition (4 direct spot-fixes + 2 Pass 3.5 deferrals); 7 LOW findings (1 subhead-form change + 1 surrogate-drop + 5 positive verifications / keeps).**

**Stage-2-flagged structural-decision dispositions:**
- **§I closing image (F-3.2-1):** chisel to lower-temperature register. Recommendation Option (b): replace "The architecture reached for the throat of the case and closed on air" with "The conventional handles did not close around the harm."
- **§VII title (F-3.2-2):** replace with true noun phrase per brief §9. Recommendation Option (b): "The architecture, engineered" (3w participial noun phrase) + reduce in-body repetition density from 3 → 2.
- **§VI Norway compression (F-3.2-3):** Pass 3.5 deferral. Voice-polish acceptable as-is; restoration-polarity expansion question for Pass 3.5.

**Four-traditions argument disposition (F-3.2-14):** **PASS 3.5 DEFERRAL.** Voice-polish polarity (CUT) is the wrong instrument for new theoretical-frame content. Flagged as Pass 3.5 candidate finding with forward-pointer language for the developmental-edit session.

**Apparatus-exclusion re-sweep (F-3.2-13):** **0 violations.** Confirms Pass 3.1 F-3.1-12; the Pass 3.1 spot-fix application did not introduce apparatus terms.

**Em-dash density:** 29 em-dashes across ~4,500w (~6.4 / 1,000w); recommendation: six targeted reductions per F-3.2-4 Option (a), bringing density to ~5 / 1,000w (within memory `feedback_em_dash_overuse.md` calibration).

**Rule-of-three / declarative-anaphora findings:** Line 65 five-clause stack + line 67 four-clause stack + line 69 "Both X. Both Y. Both Z." are the three most visible cadence stacks; all three recommended for restructure at ratification (F-3.2-6, F-3.2-7, F-3.2-8). Line 75 Coates rule-of-three preserved as citation-shape (F-3.2-5); line 97 inverted-third-element preserved as deliberate rhetoric (F-3.2-9).

---

## §4. Interactive ratification protocol (per v3.1 Amendment C)

This artifact is **PROPOSED**. Per v3.1 Amendment C (ratified 2026-05-19; updated 2026-05-21 in Boston Review brief v1.0.1 §13), prose-modifying passes (3.1 / 3.2 / 3.5) follow per-finding artifact format with Options + Recommendation + Reasoning. Ratification is **INTERACTIVE** — a follow-up session walks the author through each finding with options + recommendation + reasoning, applies ratified spot-fixes to source in the same combined session.

**Per-finding ratification expected at the interactive session:**

For each F-3.2-N finding, author selects Option (a) / (b) / (c) — or supplies an alternative. The session then applies ratified spot-fixes to [`publishing/essays/boston-review-accountability-gap/essay.md`](../../publishing/essays/boston-review-accountability-gap/essay.md) directly.

**Pass 3.5 forward-pointers carried out of this session:**
- F-3.2-3 (§VI Norway compression — restoration-polarity expansion question).
- F-3.2-14 (four-traditions / permanent-foreclosure-supply-demand-blind-spot theoretical-frame motivation — restoration-polarity addition question).

These forward-pointers fire at the Pass 3.5 session as candidate findings under the developmental-edit lens.

**No Path B violations expected at ratification:** all spot-fixes generate fresh prose from §5 voice register + draft surface. No paste-from-Ch-5 moves required. F-3.2-14 explicitly requires fresh BR-register prose distinct from the Aeon-allocated verbatim passage at `publishing/essays/aeon-mask-of-abundance/carry-forward-inventory.md`.

---

## §5. What comes next

After Pass 3.2 interactive ratification + spot-fix application:

- **Pass 3.3 — Audience-load acceptance** fires in a separate session (per v3.1 per-prompt serial cadence). Applies brief §1 16-character BR-specific pressure-test set; per-character INCLUDE / NEUTRAL / EXCLUDE verdict; per-tier aggregate; Tier-1 strong-EXCLUDE blocks submission. Output: `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_boston_review_essay_stage3_pass_3_3_audience_load_v1.0.0.md`.
- **Pass 3.4 — Adversarial robustness (OPT-IN per Decision #7).** Fires only if Pass 3.3 surfaces center-right reader (#12) as EXCLUDE or worse.
- **Pass 3.5 — Developmental-edit (BY DEFAULT per Decision #7).** Fires after 3.1 + 3.2 + 3.3 (and 3.4 if it fired) have ratify-and-applied. Restoration polarity. Picks up F-3.2-3 + F-3.2-14 forward-pointers under the developmental-edit lens.

**Stage 4 + Stage 5 forward-pointers** (per brief §14): Stage 4 essay-scale render audit at Submittable preview before submit; Stage 5 pre-submission bookend sign-off + AI-disclosure transparency at `publishing/essays/boston-review-accountability-gap/stage-5-signoff.md`.

---

*End of Stage 3 Pass 3.2 voice-polish rigor pass artifact for Boston Review essay — PROPOSED 2026-05-23. Awaits interactive ratification per v3.1 Amendment C.*
