# Rigor Pass — Ch 4 "The Existence Proof" Stage-3 Pass 2 (Voice-Polish)

**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A — Ch 4 — Pass 2 (voice-polish)
**Date drafted:** 2026-05-15
**Status:** PROPOSED — awaiting author ratification at a separate Phase C session.
**Mode:** Audit-existing-prose (post-Pass-1-spot-fix chapter is the baseline; v2.0 Amendment B voice-polish discipline as a distinct pass from Pass 1 fact-check and Pass 3 audience-load)
**Source chapter:** `manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md` — **138 lines** (post-spot-fix state verified 2026-05-15 against branch `claude/ch4-voice-polish-pass2-cpINa`, branched from current origin/main at `7b4aa92`).

**Pass 1 cross-reference:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md` (ratified 2026-05-12 — 5 MEDIUM spot-fixes applied: GPFG 2006 rename at Ch 4:21; Bondevik II disambiguation at Ch 4:29; UNEP $1B rewrite at Ch 4:79; cross-corpus Alaska 1976/1977 resolution; Bismarck 1889 + 1920s hyperinflation at Ch 4:101 — plus LOW-1 + LOW-3 follow-up ratified 2026-05-13 applying Equinor 2018 rename at Ch 4:23 + canonical-facts-inventory footnote).

**Pass 3 status:** deferred to a subsequent session per author's per-prompt serial cadence (workstream #20 Phase A: Pass-1 → spot-fix → Pass-2 → spot-fix → Pass-3 → spot-fix per chapter, not bundled).

**Format model:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md` — Ch 1 Pass-2 artifact (RATIFIED + APPLIED 2026-05-15 at commit `7b4aa92`). §0–§10 structure mirrored here; §11 disposition log added at Phase C.

---

## §0. Source artifacts read

1. `manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md` (post-Pass-1-spot-fix state; 138 lines verified)
2. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md` (Pass 1 artifact — context only; fact-check findings not re-litigated here)
3. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md` (Ch 1 Pass-2 artifact — canonical format model)
4. `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` §"Pass 2: Voice-polish" + §"Audit-existing-prose mode"
5. `tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` (per-chapter table; Ch 4 row line 66)
6. `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` (apparatus register canonical decisions for the informal Pass-4 consistency check)
7. `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` (canonical-terms inventory; Norway / GPFG / Cost Severance / Intergenerational Option Value cross-chapter rows)
8. `core/terms/terms_index.md` (canonical-form check for apparatus terms in body prose)
9. Memory: `feedback_voice_polish_pipeline.md` (dump → sift → polish; active editorial work expected)
10. Memory: `feedback_audience_aware_drafting_discipline.md` (v2.0 Amendment B — voice-polish is its own pass)
11. Memory: `feedback_substance_drives_length.md` (no padding; no cutting to fit)
12. Memory: `feedback_named_subject_consent.md` (named-subject discipline)
13. Memory: `feedback_verify_stale_memory_claims.md` (line count + cited commits verified against origin/main)

---

## §1. Pass-2 scope reminder

Pass 2 audits prose for LLM tics + voice issues a trade-press editor would flag. Per `stage-3-three-pass-rigor-audit.md` §"Pass 2," the named-inventory categories applied below:

- **Rule of three** — "A. B. C." constructions; HIGH risk for Ch 4 (comparative-case scaffolding).
- **Em-dash crutches** — em-dashes used as connective tissue rather than as deliberate parenthetical extension or punch. Watch paragraph-level density.
- **Tidy parallels** — "X did A. Y did B. Z did C." across countries / institutions / time periods. HIGH risk for Ch 4.
- **Hedge phrases** — "I will argue that…" / "It seems likely that…" / "Perhaps…" — register-break for analytical prose.
- **Connective-tissue clichés** — "in short" / "ultimately" / "moreover" / "furthermore" / "that being said" / "in this context" / "going forward" / "at the end of the day."
- **Meta-commentary** — "That is the whole sentence." / "What I mean to say is…" / "Let me explain…"
- **Expository flatness** — "The plain definition is this:" / "Here is what I think:" / "The argument is simple:"
- **Declarative-three-in-a-row** — three short declaratives in succession with no sentence-length variance. HIGH risk for Ch 4 (date-heavy / event-heavy chronology passages).
- **Nostalgia / sentimentality tics** — lower risk in analytical voice; possible at the Ekofisk-discovery scene-setting.
- **Cadence repetition** — "It changed everything. It humbled the industry. It made…" patterns.
- **Apparatus residue** — Greek letters, subscripts, integrals, capitalized flagship-term name-defenses in body prose where the chapter's apparatus register (per Pass-1 §"Apparatus regression check") prohibits.
- **Register-break to corporate / bureaucratic phrasing** — "at this time," "in this context," "going forward," "at the end of the day," "to that end."
- **Tense-consistency** — past-tense for historical chronology + present-tense for current-state analytical claims + conditional for counterfactual scaffolding; verify shifts are scene-cued.

Ch 4-specific emphasis (per chapter register per the paste-text framing):

- **Cross-country comparison structures** — three-state and four-state enumerations of petroleum-state outcomes are the chapter's primary argumentative scaffolding; flag where the cadence reaches beyond the substance.
- **Date-heavy chronologies** — institutional-architecture argument rests on chronological sequencing; flag chronology paragraphs that flat-line.
- **Counterfactual scaffolding** — "If Norway had done X, then Y" / "Other countries chose differently" constructions; flag where the framing-phrase replaces concrete-naming.
- **Apparatus residue** — Ch 4 permits lowercase prose use of "cost severance," "accountability bond B," "residual commons value," "foreclosure component," "externality tail," and a single capitalized "Intergenerational Option Value" at Ch 4:121 (introduction site).
- **Connective-tissue clichés** — higher risk in analytical voice than in memoir; default disposition for unearned instances is cut.
- **Named-figure register** — Norwegian PMs named in official capacity; Saro-Wiwa as historical-record figure; verify no informal nicknames; verify no biographical detail beyond what the argument requires.

---

## §2. Findings — HIGH severity

Issues that actively damage the prose (reader trips over named LLM tic; trade-press editor would flag).

### F-V1 — Five-declarative chronology cadence-flatness at political-consensus paragraph (HIGH)

**Line 29:**
> "A broad political consensus — spanning the center-left and the center-right — has treated the fund's integrity as a non-negotiable element of the national settlement. **Norwegian governments have changed. Economic crises have come and gone. Populist pressure to spend the money has surfaced repeatedly. Industry has argued for faster extraction. And the rules have held.**"

**Why this flags.** The five declaratives form the named *declarative-three-in-a-row* pattern extended to five. The cadence is verbatim against the paste-text's specific Ch-4 risk callout: *"Date-heavy prose risks cadence-flatness — declarative-three-in-a-row with no sentence-length variance ('X happened in Year. Y happened in Year. Z happened in Year.')"*. Sentence lengths are 4 / 6 / 7 / 6 / 5 words — minimal variance, all subject-first. The closing "And the rules have held" is a deliberate punch but the five-beat anaphoric chronology preceding it is precisely the cadence-burden trade-press editors flag as LLM-rhythm. The substance (institutional-discipline-held-through-stresses) is the chapter's load-bearing existence-proof beat; the cadence is the failure mode.

**Severity rationale.** (a) Named-inventory verbatim match (declarative-three-in-a-row extended to five). (b) Date-heavy chronology cadence-flatness — paste-text's Ch-4 specific high-risk callout. (c) §-internal position is structurally load-bearing — the cadence is the rhythm that carries the chapter's central claim (the rules held). (d) Trade-press editors in 2026 are calibrated to the LLM-cadence pattern; this paragraph is on the named list.

**Recommended spot-fix (author selects one option):**

- **A. Vary sentence-length across the five.** *"Norwegian governments have changed. Economic crises have come and gone. Populist pressure to spend the money has surfaced repeatedly, and industry has argued for faster extraction at nearly every drilling-permit-review cycle. The rules have held."* Compresses sentences 3+4 into one compound; gives sentence 3 substantive content (drilling-permit-review cycles); breaks the five-beat lockstep; ends on a four-word punch rather than the five-beat anaphoric closer.
- **B. Collapse to a two-sentence inventory + punch.** *"Through changes of government, oil-price downturns, populist spending pressure, and recurring industry argument for faster extraction, the rules have held."* Single sentence carries the four stresses as compound objects of "through"; the second sentence (or fragment) lands the punch. Two sentences instead of five.
- **C. Reorder + integrate.** *"Norwegian governments have changed; economic crises have come and gone; populist and industry pressure to spend faster has surfaced repeatedly. And the rules have held."* Semicolons inside one sentence break the period-declarative cadence while preserving the parallel-clause inventory; the punch lands as a deliberate two-sentence shift to short declarative.

Any of A/B/C dissolves the named pattern while preserving the institutional-discipline-held-through-stresses claim.

---

### F-V2 — Four-anaphoric "The same X" fragment block at Niger-Delta-pivot paragraph (HIGH)

**Line 81:**
> "**The same oil. The same market price. The same global demand curve.** Radically different outcomes for the communities whose commons the oil was drawn from. The framework's residual commons value for the Niger Delta is not a small figure. It is enormous. And the accountability bond — the actual revenue captured on behalf of the affected communities, through instruments that reach those communities rather than flowing around them — is, in comparison with Norway's, near zero."

**Why this flags.** Three sentence-fragments with strong "The same X" anaphora, followed by a fourth sentence-length closer (*"Radically different outcomes…"*) that completes the rhetorical pivot. The cadence is the named *tidy-parallel* + *declarative-three-in-a-row* pattern stacked into a four-fragment anaphoric block. Editors recognize this as the AI-prose reach for thematic-symmetry-as-rhetorical-punch — the cadence is doing the conceptual work (identical inputs / different outcomes) that the substance should carry on its own. Compare to Ch 1's flagged "The plane was past the cloud line. The sun was up. The day was beginning. I had work to do." closer (F-V21, held as defensible bookend) — but Ch 1's instance bookends the chapter (single occurrence, structurally load-bearing); Ch 4's instance is the chapter's rhetorical pivot, which makes the named cadence more editor-detectable than at a structural bookend position.

**Severity rationale.** (a) Named-inventory verbatim match (tidy-parallel four-fragment + declarative-three-extended). (b) Located at the chapter's central comparative-pivot moment (Niger-Delta-vs-Norway thesis-restate). (c) The cadence is the failure mode — the substance (identical-inputs / different-outcomes) is the chapter's spine claim. (d) The "The same X. The same Y. The same Z." fragment block is on the trade-press editor's standard LLM-cadence-watch list.

**Recommended spot-fix (author selects one option):**

- **A. Collapse to a single contrast sentence.** *"The oil, the market price, the demand curve — all the same as Norway's. The outcomes for the communities whose commons the oil was drawn from are not."* Two sentences replace four fragments + closer; the comparative pivot lands without the anaphoric drumbeat; em-dash carries the contrast.
- **B. Vary structure across the four.** *"The oil is the same as Norway's oil. The market price is the same. The global demand curve is the same. The outcomes for the communities whose commons it was drawn from are radically different."* Keeps four-sentence structure; varies sentence-length (long / short / short / longer); replaces fragments with full sentences; preserves anaphoric pivot but in clean-prose rather than fragment register.
- **C. Reorder + tighten.** *"The oil is comparable to Norway's. The market price is the same; the global demand curve is the same. The outcomes for the communities whose commons the oil was drawn from are not."* Three sentences instead of four; semicolon compresses the middle two; final sentence carries the contrast on bare-prose.

Any of A/B/C dissolves the named-fragment cadence while preserving the identical-inputs / different-outcomes thesis-pivot.

---

### F-V3 — Four-paragraph anaphoric "It does not…" block at "The part Norway has not solved" §-section (HIGH)

**Lines 115 / 117 / 119 / 121** — each paragraph opens with *"It does not [verb]…"*:
> "**It does not price permanent foreclosure.** The barrel is still gone. […]"
> "**It does not close the externality tail.** North Sea ecosystems recover slowly where they recover at all. […]"
> "**It does not address the distributional problem at the global scale.** Norway's fund compounds, in effect, on the productive output of the global economy. […]"
> "**It does not price the existence of the resource for its Intergenerational Option Value** — the possibility that future generations will need the oil not for the applications we currently use it for, but for applications we have not yet imagined. […]"

**Why this flags.** Paragraph-level tidy-parallel pattern carried across four sequential paragraphs. Each paragraph opens with "It does not [verb]" + object — the same syntactic shape, four times deep. This is the named *tidy-parallel* pattern operating at paragraph-opening scale, which is a higher cadence-burden than sentence-level anaphora because the structure repeats every time the reader crosses a paragraph break. A trade-press editor scanning for AI-prose structural-cadence patterns will register this section's paragraph-anaphora before reading the substance. The four-deep depth (not three; not five) is the rule-of-four extension of rule-of-three — the named tic at scale.

**Severity rationale.** (a) Named pattern (tidy-parallel + paragraph-level anaphora). (b) Four-deep depth at paragraph-opening scale — higher cadence-burden than sentence-level anaphora because each paragraph break re-cues the pattern. (c) Structurally load-bearing — this is the chapter's gap-naming section, where the four-part inventory carries the handoff to Ch 5+. (d) Content-driven justification: there are genuinely four distinct gaps Norway has not solved (foreclosure pricing, externality tail closure, global-scale distribution, option-value pricing), so a four-part inventory is substantively earned. The named pattern lives in the cadence-shape choice, not in the count.

**Recommended spot-fix (author selects one option):**

- **A. Break the anaphora on one paragraph.** Lines 115 / 117 / 119 / 121 keep three "It does not [verb]" openings (e.g., 115 / 117 / 121); the fourth (e.g., line 119) opens differently: *"The global-scale distributional problem is also unresolved. Norway's fund compounds, in effect, on the productive output of the global economy. […]"* Preserves the four-inventory structure; breaks the paragraph-anaphora by varying the third or fourth paragraph's opening sentence.
- **B. Convert one or two to embedded paragraphs.** Keep lines 115 + 121 as anaphoric openers (foreclosure-pricing + Intergenerational-Option-Value — the two most chapter-spine claims); convert lines 117 + 119 to integrated paragraphs that don't lead with "It does not." *Externality tail* and *global-scale distribution* become substantive paragraphs whose anaphoric thesis-claim is interior rather than at sentence-1 position.
- **C. Hold as-is — flag for register-justification.** Defensible as deliberate enumerative cadence at the chapter's most structurally load-bearing inventory moment (the gap-naming handoff to Ch 5+). The four-paragraph parallel signals "here are the four things still unresolved" rhythmically — a reader-aid rather than a cadence-burden. Author's call; trade-off is structural-clarity-via-anaphora vs. editor-detectable-paragraph-anaphora.

A/B reduce the chapter's most visible chapter-scale cadence-pattern; C preserves the deliberate enumerative architecture at the cost of one chapter-scale named-tic.

---

## §3. Findings — MEDIUM severity

Patterns that flag but don't stop the prose. Author discretion. Many are substantively-earned and defensible as analytical-cadence enacting comparative-argument content; flagged so each can be reviewed instance-by-instance to confirm it earns its space rather than reading as LLM-pattern in aggregate.

### F-V4 — Tidy-parallel "Some did X. Some did Y." petroleum-state survey at opening contrast paragraph (MEDIUM)

**Line 9:**
> "The decision the country faced at that moment is the decision every resource-rich jurisdiction faces, which is why the thing Norway did next is worth studying in detail. Most jurisdictions spend the money. **Some of them do it quickly and badly — Venezuela, Nigeria, early-phase Saudi Arabia. Some do it more carefully, with more to show for it — Texas, Alberta, Alaska.** Alberta's Heritage Trust Fund, established in 1976, was the closest North American attempt at the Norwegian model…"

**Why this flags.** The paste-text's Ch-4 specific emphasis calls out this exact pattern: *"Some did X. Some did Y. Some did Z." formulations where the three options are stylized rather than literally surveyed.* Here it's a two-element "Some did X. Some did Y." structure, with each carrying a three-country list (Venezuela/Nigeria/Saudi Arabia; Texas/Alberta/Alaska). The framing reads as stylized survey-by-tidy-parallel even though the paragraph does substantively develop Alberta and Alaska that follow. The named pattern is the framing-phrase ("Some did X… Some did Y…") rather than the substantive survey.

**Severity rationale.** Defensible as analytical-survey-setup (the paragraph does follow through with substantive Alberta + Alaska detail). Flagged because the named tidy-parallel pattern is explicitly the Ch-4 paste-text emphasis and the framing-phrase reads as stylized.

**Recommended spot-fix (optional):**

- **Hold as-is.** Substantive survey-follow-through earns the framing.
- **Alternative.** Replace the "Some did X / Some did Y" framing with direct enumeration: *"Most jurisdictions spend the money. Venezuela, Nigeria, and early-phase Saudi Arabia spent it quickly and badly. Texas, Alberta, and Alaska spent it more carefully, with more to show for it. Alberta's Heritage Trust Fund, established in 1976, was the closest North American attempt at the Norwegian model…"* Drops the "Some" framing; the named-country enumeration carries the contrast directly.

---

### F-V5 — Declarative-three negation-negation-affirmation at decision-was-not-obvious paragraph (MEDIUM)

**Line 11:**
> "**The decision was not obvious. It was not inevitable.** It was deliberately argued for, debated, and then structurally enforced across decades of subsequent governments by a set of rules that removed most of the discretion to undo it."

**Why this flags.** Three declaratives with the *not X → not Y → affirmation Z* cadence — the same negation-negation-affirmation shape Ch 1 flagged at F-V14 (line 103 framework-naming) and held as substantively-earned. Here the third sentence carries explicit variance in length (much longer; embedded clauses), which softens the named pattern relative to the Ch 1 case. The cadence rhetorically tightens to the "argued for / debated / structurally enforced" triad inside sentence 3.

**Severity rationale.** Defensible as deliberate definitional cadence at the chapter's existence-proof premise. The negation-negation-affirmation structure is rhetorically-earned (the chapter must say what the decision was-not before saying what it was). The named pattern is the cadence-shape, but the sentence-3 length-variance partially dissolves it.

**Recommended spot-fix (optional):**

- **Hold as-is.** Cadence earns the rhetorical punch; sentence-3 length-variance softens the named pattern.
- **Alternative.** Compound the negations: *"The decision was not obvious or inevitable. It was deliberately argued for, debated, and then structurally enforced across decades of subsequent governments by a set of rules that removed most of the discretion to undo it."* Two sentences instead of three; preserves substance.

---

### F-V6 — Double-anaphoric "X is one outcome. Y is another. The variable is not Z. The variable is W." at framework-claim paragraph (MEDIUM)

**Line 15:**
> "It proves, among other things, that cost severance is a policy choice. The same barrel of oil, extracted from roughly the same ocean, refined into roughly the same products, sold into roughly the same global market, can produce radically different outcomes for the community whose commons the oil was drawn from. **Appalachia is one outcome. Norway is another. The variable is not geology. The variable is the institutional architecture that decides who captures the value and who bears the cost.** That architecture is engineered, not accidental. And if it is engineered in one place, it can be engineered elsewhere — which is the claim the book needs to establish before asking what an honestly priced extraction regime would look like."

**Why this flags.** Two anaphoric sentence-pairs stacked. *"Appalachia is one outcome. Norway is another."* is a tidy-parallel two-statement. *"The variable is not geology. The variable is the institutional architecture…"* is a second tidy-parallel with stronger "The variable is" anaphora and negation-affirmation cadence. Two anaphoric pairs in four consecutive sentences is a higher cadence-density than a single instance; the named pattern is visible at scale.

**Severity rationale.** Substantively load-bearing — this is the chapter's first explicit thesis-claim about cost severance as policy choice + the Appalachia/Norway pivot. The cadence is doing real conceptual work (claim → contrast-by-pair → variable-identification → variable-affirmation). Named pattern lives in the stacked anaphora, not in any single sentence.

**Recommended spot-fix (optional):**

- **Hold as-is.** Cadence enacts the chapter's framework-introduction sequence.
- **Alternative.** Collapse the second anaphoric pair: *"Appalachia is one outcome. Norway is another. The variable is not geology — it is the institutional architecture that decides who captures the value and who bears the cost."* Three sentences instead of four; em-dash carries the contrast inside sentence 3; preserves the first anaphoric pair which is the conceptually-load-bearing pivot.

---

### F-V7 — Three-declarative "The X would be Y" architecture-design paragraph (MEDIUM)

**Line 31:**
> "Norway designed its architecture to close both failure modes at once. **The revenue would be captured by the state. The capture would be placed in a structure that could not be looted by any single government. And the spending would be rate-limited to the income the capital itself generated.**"

**Why this flags.** Three declaratives with strong *"The X would be Y"* passive-construction anaphora — the named tidy-parallel pattern. The "And" sentence-opener on sentence 3 is the deliberate cadence-tighten (signaling the three-part architecture is a unified design-program). All three sentences use passive voice with the same syntactic shape.

**Severity rationale.** Substantively-earned (the three design elements are real — revenue capture / structural protection / rate-limit). The named pattern is the cadence-vehicle for the three-part claim. Defensible as analytical-policy-prose enumerative cadence.

**Recommended spot-fix (optional):**

- **Hold as-is.** Three-part architecture-design substantively earns the three-part cadence.
- **Alternative.** Vary voice on sentence 3: *"The revenue would be captured by the state. The capture would be placed in a structure that could not be looted by any single government. Spending would be rate-limited to the income the capital itself generated."* Drops "And the" opener on sentence 3 + drops the article on "the spending" → "spending"; sentence becomes more direct. Minor change; breaks the named anaphora.

---

### F-V8 — Three-declarative "The X is Y" framework-claim paragraph at §"What the framework says about Norway" opening (MEDIUM)

**Line 39:**
> "The analytical question the book has been building toward — what is the cost severance of a given extraction — can now be asked of a case that looks, at first glance, like it should have no cost severance at all. **The rents are captured. The community is compensated. The institutional architecture is the best in the world.**"

**Why this flags.** Three short declaratives in succession with parallel "The X [verb-ed/is] Y" structure — the named *declarative-three-in-a-row* pattern at full strength. Sentence lengths 4 / 4 / 8 words (mild variance on sentence 3). The third sentence carries the chapter's most editor-detectable claim (*"best in the world"*) and the cadence-build to it makes the claim land as cadence-driven rather than substance-driven.

**Severity rationale.** Sets up the §-section's central question (does Norway-as-best have any residual cost severance?). The cadence does conceptual setup-work. But the named pattern is verbatim, and the "best in the world" claim is one of the chapter's strongest rhetorical reaches — the cadence amplifies that reach where a slightly varied structure would let the substance carry.

**Recommended spot-fix (optional):**

- **Hold as-is.** Three-part claim-build earns the three-part cadence; "best in the world" is substantively defensible.
- **Alternative.** Vary structure to break the anaphoric short-declarative: *"The rents are captured, the community compensated, and the institutional architecture the best in the world."* One sentence with three serial clauses; same three-element setup; named pattern dissolves.
- **Alternative 2.** Soften the third-sentence reach: *"The rents are captured. The community is compensated. The institutional architecture is widely judged the best in the world."* Drops the unhedged superlative; minor change; preserves the three-declarative cadence but addresses the cadence-amplification concern.

---

### F-V9 — Mega-em-dash parenthetical (78-word interjection) at petroleum-substitution paragraph (MEDIUM)

**Line 49:**
> "Future generations who have no viable substitute for petroleum in their particular application **— the specific chemistries, materials, and products for which no renewable alternative yet exists, including medical-grade plastics for surgical instruments and pharmaceutical packaging, aviation jet fuel for the present global commercial fleet, specialty petrochemistry for high-performance polymers and pharmaceutical synthesis, asphalt for road infrastructure, and the carbon-fiber and lubricant chemistries that underwrite both renewable-energy hardware and the manufacturing ecosystems that produce it —** do not regain access to it because the revenue was well-managed."

**Why this flags.** A 78-word interjection between em-dash pair, carrying a five-element list of petroleum applications (medical-grade plastics / aviation jet fuel / specialty petrochemistry / asphalt / carbon-fiber+lubricant). The named *em-dash crutch* pattern at maximal cadence-burden: the main clause (*"Future generations… do not regain access to it…"*) is broken by an interjection longer than most paragraphs in the chapter. The interjection's substance is content-rich (foreclosure-pricing's substantive grounding in concrete petroleum applications) but structurally heavy. A trade-press editor will flag this as an em-dash-crutch-burdened sentence regardless of the substantive value of the inset list.

**Severity rationale.** Substantively load-bearing (the list anchors the foreclosure-pricing argument in concrete petroleum-product realities). The em-dash-bracketed structure makes the substance recoverable but cadence-burdened. Compared to Ch 1's flagged F-V4 (13-word appositive between em-dashes), this is roughly 6× the interjection length.

**Recommended spot-fix (author selects one option):**

- **A. Break the interjection into its own sentence + summary.** *"Future generations who have no viable substitute for petroleum in their particular application do not regain access to it because the revenue was well-managed. The applications for which no renewable alternative yet exists include medical-grade plastics for surgical instruments and pharmaceutical packaging, aviation jet fuel for the present global commercial fleet, specialty petrochemistry for high-performance polymers and pharmaceutical synthesis, asphalt for road infrastructure, and the carbon-fiber and lubricant chemistries that underwrite both renewable-energy hardware and the manufacturing ecosystems that produce it."* Two sentences; main claim sits unburdened; substantive list moves to its own clean structure.
- **B. Compress the list to 3–4 representative elements.** *"Future generations who have no viable substitute for petroleum in their particular application — the specific chemistries for which no renewable alternative yet exists, including medical-grade plastics, aviation jet fuel, asphalt for road infrastructure, and the carbon-fiber chemistries that underwrite renewable-energy hardware — do not regain access to it because the revenue was well-managed."* Cuts the list from five to four elements; drops the parenthetical sub-amplifiers ("for surgical instruments and pharmaceutical packaging," "for high-performance polymers and pharmaceutical synthesis"); preserves em-dash-bracketed structure but ~40% shorter. The dropped substance can move to an endnote if author wants to keep it.
- **C. Hold as-is.** Defensible if the author wants the full enumeration in trade body; the substance is real and substantively grounds the foreclosure-pricing claim. Author's call; trade-off is substantive completeness vs. cadence-burden.

---

### F-V10 — Three-declarative "The mechanism… That is not… It is…" cadence at selection-criterion punch paragraph (MEDIUM)

**Line 63:**
> "Cost severance, the book has claimed from the beginning, is not a natural law. It is the operation of a mechanism — value extraction paired with the transfer of costs to communities with limited capacity to resist the transfer. That mechanism operates most efficiently in exactly the conditions Norway did not have: weak institutions, low administrative capacity, limited legal recourse for affected communities, fragmented political representation, and a population whose economic dependence on the extraction itself makes organized resistance practically impossible. **The mechanism preys on weakness. That is not a bug of the extraction economy. It is its selection criterion.**"

**Why this flags.** Three short declaratives at paragraph close with named *declarative-three-in-a-row* pattern + "That is not X. It is Y." anaphoric cadence on sentences 2–3. The closing "selection criterion" is a deliberate cadence-punch; the cadence-build to it follows the named LLM-rhetoric shape (predicate-flip then naming-affirmation).

**Severity rationale.** Substantively load-bearing (the "selection criterion" claim is the chapter's strongest mechanism-framing statement). Rhetorically earned cadence. Named pattern visible.

**Recommended spot-fix (optional):**

- **Hold as-is.** Cadence enacts the selection-criterion claim; rhetorically earned.
- **Alternative.** Compound sentences 2 + 3: *"The mechanism preys on weakness — not as a bug of the extraction economy but as its selection criterion."* One sentence; em-dash carries the contrast; preserves the substantive punch via direct claim rather than cadence-build.

---

### F-V11 — Stacked-tic paragraph (anaphoric pair + four-element list + five-declarative) at Niger-Delta cost-severance-decomposition paragraph (MEDIUM)

**Line 83:**
> "**The cost severance, in the framework's terms, is very large. It is large because B is small. It is not large because the oil is different. The geology, the extraction technology, the product, the market — all comparable.** The difference is entirely in the institutional architecture that determines where value flows after extraction."

**Why this flags.** Multiple named patterns stacked in five sentences: (a) "It is large because X. It is not large because Y." anaphoric negation-pair on sentences 2–3; (b) four-element comma-separated list "The geology, the extraction technology, the product, the market" + em-dash closer on sentence 4 (named tidy-parallel four-element pattern); (c) five-declarative cumulative density. The substance is the cost-severance decomposition (B-is-small not oil-is-different), which is conceptually important — but the cadence-stacking is the highest local LLM-tic density in the chapter outside F-V1/F-V2.

**Severity rationale.** Substantively earned (the decomposition is the framework's central explanatory move for the Niger Delta case). Cadence-stacking is the failure mode — three named patterns at once in five sentences make this paragraph one of the chapter's most editor-detectable cadence-clusters.

**Recommended spot-fix (author selects one option):**

- **A. Compress sentences 2 + 3.** *"The cost severance, in the framework's terms, is very large. It is large because B is small, not because the oil is different. The geology, the extraction technology, the product, the market — all comparable. The difference is entirely in the institutional architecture that determines where value flows after extraction."* Four sentences instead of five; the "because X, not because Y" inside sentence 2 dissolves the anaphoric negation-pair.
- **B. Break the four-element list to three.** *"The cost severance, in the framework's terms, is very large. It is large because B is small. It is not large because the oil is different. The geology, the extraction technology, the market — all comparable. The difference is entirely in the institutional architecture that determines where value flows after extraction."* Same five-sentence count; drops "the product" from sentence 4 (overlaps with "the market"); breaks the rule-of-four list to rule-of-three.
- **C. Combine A + B.** Two compressions applied together; densest cadence-reduction.
- **D. Hold as-is.** Substantively-earned; cadence-stacking carries the explanatory move. Author's call.

---

### F-V12 — Em-dash density (4 em-dashes / 2 parenthetical pairs) at US-Social-Security comparator paragraph (MEDIUM)

**Line 95:**
> "Consider, for a moment, the United States Social Security system. The system is, at its operational core, a different architecture for the same kind of intergenerational claim. Where Norway captures the revenue from petroleum extraction and compounds it in invested capital that funds the pensions of future generations, U.S. Social Security captures the revenue from payroll taxes paid by the current working generation and transfers it, in close-to-real-time, to the current retired generation. **The architectural sources differ — Norway's fund is fed by petroleum rents that are finite and geological; the U.S. system is fed by payroll taxes that are ongoing and labor-derived — but the question each architecture answers is structurally analogous: how does a society capture an intergenerational claim and deploy it across generations? Where Norway compounds, the U.S. transfers. Any surplus the U.S. system has generated over annual outflow has historically been invested in U.S. Treasury bonds whose proceeds the federal government has spent on general operations — wars, tax cuts, budget gaps, the fiscal pressures of the moment — meaning the system's 'trust fund' is an accounting record of intra-government debt rather than a compounding pool of external capital.** The future generation's pensions, in the U.S. system, depend on the next generation's workforce, not on a real reserve of saved-and-compounded wealth."

**Why this flags.** Four em-dashes in one paragraph, two of them forming a 16-word parenthetical pair (sentence 4: *"— Norway's fund is fed by petroleum rents that are finite and geological; the U.S. system is fed by payroll taxes that are ongoing and labor-derived —"*) and two forming a 13-word parenthetical pair (sentence 6: *"— wars, tax cuts, budget gaps, the fiscal pressures of the moment —"*). High em-dash density in a single paragraph. Comparable to Ch 1's flagged F-V4 + F-V8 paragraphs (3–4 em-dashes each).

**Severity rationale.** Each em-dash individually is defensible parenthetical-extension. The issue is the cumulative paragraph density + the chapter-wide pattern (Ch 4 has high em-dash density throughout — 50+ em-dashes in 138 lines). Trade-press editors with an em-dash-crutch lens will register this paragraph as a chapter-wide habit instance.

**Recommended spot-fix (author selects one option):**

- **A. Convert sentence-4's em-dash pair to semicolon-comma.** *"The architectural sources differ. Norway's fund is fed by petroleum rents that are finite and geological; the U.S. system is fed by payroll taxes that are ongoing and labor-derived. The question each architecture answers is structurally analogous: how does a society capture an intergenerational claim and deploy it across generations?"* Three sentences instead of one; em-dash pair dissolves; semicolon carries the parallel.
- **B. Convert sentence-6's em-dash pair to parenthesis or appositive.** *"Any surplus the U.S. system has generated over annual outflow has historically been invested in U.S. Treasury bonds whose proceeds the federal government has spent on general operations (wars, tax cuts, budget gaps, the fiscal pressures of the moment), meaning the system's 'trust fund' is an accounting record of intra-government debt rather than a compounding pool of external capital."* Parentheses instead of em-dashes; same content; em-dash count drops by 2.
- **C. Apply both A + B.** Drops em-dash count in this paragraph from 4 to 0 (or 1 if one em-dash retained as deliberate punch).

Any of A/B/C drops the paragraph's em-dash density; doing both reduces the chapter-wide pattern most.

---

### F-V13 — Three-anaphoric "Both are X" cadence at US-Social-Security comparator (MEDIUM)

**Line 97:**
> "**Both are retirement-security architectures. Both are intergenerational instruments. Both are responses to the same problem:** how does a society provide for its members' final decades when those members' productive working years have ended? The two countries answer the question differently, and the difference is not because one country is more virtuous than the other. It is because the institutional choices that produced the two architectures were made at different moments, in different political circumstances, with different available templates."

**Why this flags.** Three short declaratives with verbatim "Both are X" anaphora — the named *tidy-parallel* + *declarative-three-in-a-row* pattern at full strength. Sentence lengths 5 / 5 / 8 words. Substantively the three "Both" claims set up the comparator-question, but the cadence is on the named LLM-rhetoric pattern.

**Severity rationale.** Sets up the central US/Norway architectural-comparator question. The three "Both are X" formulations are substantively redundant (architecture / instrument / response-to-same-problem all converge on the same comparator-framing point); the third is the one that does conceptual work ("responses to the same problem:"). The cadence is the LLM-cadence shape; the substance can be compressed.

**Recommended spot-fix (author selects one option):**

- **A. Compress to one sentence.** *"Both are retirement-security architectures — intergenerational instruments responding to the same problem: how does a society provide for its members' final decades when those members' productive working years have ended?"* One sentence carries the three claims as compound noun-phrase + appositive; named anaphora dissolves; conceptual setup-work preserved.
- **B. Drop sentence 2.** *"Both are retirement-security architectures. Both are responses to the same problem: how does a society provide for its members' final decades when those members' productive working years have ended?"* Two sentences instead of three; drops the redundant "intergenerational instruments" beat; cadence becomes two-statement pivot rather than three-statement anaphoric.
- **C. Hold as-is.** Defensible as deliberate anaphoric setup. Author's call.

---

### F-V14 — Stacked-pattern "There are no X. There are only Y." + three-rules tidy parallel + chiastic constructed→reconstructed coda at architecture-is-engineered paragraph (MEDIUM)

**Line 105:**
> "What the comparison does add to the chapter's argument is this: when Norway proves that cost severance can be dramatically reduced by an institutional choice, and when the U.S. Social Security comparison proves that retirement-security architecture is itself a choice made in particular historical conditions, the broader claim emerges: every architecture that distributes value and cost across generations is engineered. **There are no naturally-occurring distributional outcomes. There are only the rules a generation builds, the rules it inherits, and the rules it agrees to maintain or replace.** Norway's existence proof is, in this larger sense, an existence proof for the universal proposition that architecture is constructed, not given — **and that what was constructed once can be reconstructed.**"

**Why this flags.** Three named patterns stacked: (a) "There are no X. There are only Y." anaphoric negation-affirmation pair; (b) "the rules X, the rules Y, the rules Z" three-element tidy-parallel inside sentence 2; (c) "what was constructed once can be reconstructed" chiastic-coda — the same kind of chiastic-flourish move flagged in Ch 1's F-V9 + F-V11 (fall-in-love/fall-out-of-love; to be there at the end). Two anaphoric structures + a chiastic coda in three sentences is editor-detectable.

**Severity rationale.** Substantively load-bearing — this is the chapter's broader-thesis emergence (architecture-is-constructed) + the bridge to the rest of the book. Cadence is rhetorically earned. But the stacking is the named-pattern density visible at the chapter's most theorem-like moment.

**Recommended spot-fix (author selects one option):**

- **A. Drop the chiastic coda.** *"…Norway's existence proof is, in this larger sense, an existence proof for the universal proposition that architecture is constructed, not given."* Cuts "— and that what was constructed once can be reconstructed." Preserves the constructed-not-given thesis; drops the chiastic flourish; the substance lands without the symmetry-reach.
- **B. Replace the chiastic coda with concrete forward-pointer.** *"…an existence proof for the universal proposition that architecture is constructed, not given — which the remaining chapters are about."* Drops the chiasmus; gains a chapter-handoff move; preserves the cadence-tightening.
- **C. Compress the three-rules tidy-parallel.** *"There are only the rules a generation builds, inherits, and agrees to maintain or replace."* One sentence with three serial verbs; same three-element substance; named anaphora dissolves.
- **D. Hold as-is.** Defensible as deliberate theorem-statement cadence at the chapter's broader-thesis-emergence moment. Author's call.

---

### F-V15 — Recurring "[Setup-clause] is this:" expository-frame pattern across three chapter-spine claims (MEDIUM)

**Line 53:**
> "**The framework's conclusion, applied to Norway, is this:** the cost severance is much smaller than Appalachia's because the accountability bond B is vastly larger, but it is not zero because no existing instrument in the world prices permanent foreclosure or closes the externality tail."

**Line 85:**
> "**This is what the framework needs to demonstrate to be credible:** that it differentiates correctly."

**Line 105:**
> "**What the comparison does add to the chapter's argument is this:** when Norway proves that cost severance can be dramatically reduced by an institutional choice, and when the U.S. Social Security comparison proves that retirement-security architecture is itself a choice made in particular historical conditions, the broader claim emerges: every architecture that distributes value and cost across generations is engineered."

**Why this flags.** Three instances across the chapter of the "*[Setup-clause] is this:* + colon-introduction of substantive thesis-claim" pattern — the named *expository-flatness* tic in the Pass-2 inventory (verbatim adjacent to *"The plain definition is this:" / "Here is what I think:" / "The argument is simple:"*). Each instance is at a chapter-spine claim site: the §"What the framework says about Norway" conclusion (line 53), the framework-credibility-demonstration claim (line 85), and the broader-thesis-emergence at the §"Architecture is a choice" close (line 105). Chapter-wide pattern, not a single instance.

**Severity rationale.** Each instance individually is mild; the cumulative chapter-wide density (three) makes the pattern visible to a trade-press editor scanning for AI-prose expository-frame habit. The three instances cluster the chapter's most editor-detectable expository-frame register-tells together.

**Recommended spot-fix (author selects one option):**

- **A. Cut all three "is this:" frames; replace with direct claim.**
  - Line 53: *"The framework's conclusion, applied to Norway: the cost severance is much smaller than Appalachia's because…"* (drop "is this")
  - Line 85: *"The framework needs to demonstrate that it differentiates correctly."* (drop expository frame entirely)
  - Line 105: *"The comparison adds this to the chapter's argument: when Norway proves…"* (compress) OR *"The comparison adds the following to the chapter's argument: when Norway proves…"*
- **B. Cut one or two of the three; hold the strongest as deliberate.** Author judgment which expository-frame moment most earns the cadence-introducer. Line 53's §-conclusion is the most-defensible (it explicitly closes a §-section); lines 85 and 105 are more vulnerable.
- **C. Hold as-is.** Defensible as analytical-policy-prose register where colon-introduced thesis-claims are register-appropriate. The three instances at three thesis-claim sites argue this is deliberate chapter-spine cadence rather than register-break. Author's call.

A/B drop the chapter-wide pattern visibility; C accepts the pattern as register-appropriate cadence.

---

## §4. Findings — LOW severity / style preferences

Patterns that are style preferences rather than stoppers. Author discretion; default recommendation is hold-as-is across the LOW set.

### F-V16 — Five-noun list at per-citizen flourish (LOW)

**Line 23:**
> "On a per-citizen basis, that is roughly three hundred and forty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."

Five-element comma-separated rhetorical-emphasis list. Defensible as universality-of-coverage flourish (every-citizen including non-earners). Some editors flag any 5+ element list; most read this as deliberate rhetorical close.

**Recommended action:** Hold as-is.

---

### F-V17 — Two-declarative "The oil will… The fund will…" closer (LOW)

**Line 27:**
> "The oil will eventually be gone. The fund will remain."

Tidy-parallel two-declarative chapter-architecture punch. Defensible: cadence enacts the central temporal-substitution claim (physical resource exhaustible / financial resource compounds). Bookends the §"The architecture" introduction with rhythmic balance.

**Recommended action:** Hold as-is.

---

### F-V18 — Meta-frame "None of this is magic" at §"The architecture" close (LOW)

**Line 33:**
> "None of this is magic. It is institutional design, maintained across generations by people who understood what they were preventing."

"None of this is magic. It is X" follows the same negation-affirmation pattern as the chapter's recurring *not X / is Y* cadence. Borderline meta-commentary ("none of this is magic" reads as authorial-frame-saying-what-it-isn't). Defensible as deliberate §-closer rhetorical move; the substantive affirmation in sentence 2 carries the load.

**Recommended action:** Hold as-is. Optional alternative: *"This is institutional design, maintained across generations by people who understood what they were preventing."* — drops the meta-frame on sentence 1; one sentence instead of two.

---

### F-V19 — Standalone-paragraph two-statement "It says X. It does not say Y." at framework-says-about-Norway pivot (LOW)

**Line 43:**
> "It says the cost severance has been dramatically reduced. It does not say the cost severance is zero."

One-sentence-each two-statement standalone paragraph. Tidy-parallel pattern with deliberate "says/does-not-say" rhetorical-symmetry. Defensible as deliberate-rhythmic-hinge between sections (the §-section's analytical-pivot moment). Compare to F-V3's four-paragraph anaphoric structure; this is a single-instance two-statement paragraph rather than chapter-wide pattern.

**Recommended action:** Hold as-is.

---

### F-V20 — "Similarly," sentence-opener + "No fund can." two-word closer at externality-tail paragraph (LOW)

**Line 51:**
> "**Similarly,** the externality tail persists. […] The fund does not extract that carbon from the sky. **No fund can.**"

Two minor tics in one paragraph: (a) "Similarly" as paragraph-opener — one instance of the named *connective-tissue cliché* pattern (lone instance, not a chapter-wide habit); (b) "No fund can" as two-word punch-closer — deliberate cadence-tighten, defensible as analytical-prose-punch.

**Recommended action:** Hold as-is. Optional alternative: drop "Similarly," at paragraph-opener; start the paragraph with "The externality tail persists." Cuts the connective-tissue cliché instance without affecting the substance.

---

### F-V21 — "with X, with Y, with Z" three-element tidy-parallel inside one sentence at architecture-defenses-built paragraph (LOW)

**Line 67:**
> "With different institutions — **with a deliberately constructed accountability bond, with a political settlement that treats the commons as belonging to the commons, with rules designed to outlast the generation that writes them** — the same physical extraction produces a radically different distribution of value and cost."

Three-element tidy-parallel "with X, with Y, with Z" serial enumeration inside one sentence. Content-driven (three real institutional-defense elements). Within-sentence enumeration rather than across-sentence anaphora softens the named-pattern visibility.

**Recommended action:** Hold as-is.

---

### F-V22 — Two-declarative "Neither outcome was inevitable. Both were engineered." chapter-spine punch (LOW)

**Line 131:**
> "Neither outcome was inevitable. Both were engineered."

Standalone two-declarative paragraph at chapter-close. Same shape as F-V17 but here at the chapter's penultimate substantive paragraph — the chapter-spine punch that distills the existence-proof claim into nine words. Structurally load-bearing as the chapter's thesis-distillation moment.

**Recommended action:** Hold as-is.

---

### F-V23 — Anaphoric "Each one tells…" two-statement bookend at chapter-handoff (LOW)

**Line 133:**
> "The next chapter takes that question into the industrial cases that have not been Norway: Libby, Deepwater Horizon, Exxon Valdez, Baotou. **Each one tells part of the answer. Each one tells part of the warning.**"

Two-sentence anaphoric coda with "Each one tells part of the X" repetition. Two-statement structure (not three) at chapter-handoff position. Defensible as deliberate-bookend transition to Ch 5. The "answer / warning" pairing is rhetorically earned (the four named cases — Libby, Deepwater Horizon, Exxon Valdez, Baotou — are factually both partial-answer and partial-warning).

**Recommended action:** Hold as-is.

---

## §5. Register / tense / apparatus / named-subject checks

Per the Pass-2 inventory's last few categories + the workstream handoff's Ch 4 emphasis (analytical-comparative voice consistency; date-heavy chronology tense-control; named-figure register; apparatus residue against Pass-1 baseline).

### §5.1 Register consistency — ✓ HOLDS

Voice is third-person-analytical throughout. The chapter speaks from the analyst's seat across all 138 lines. The inclusive-of-reader "we" at line 53 (*"any alternative we can point to"*) and line 105 (*"the variable we can actually change"*) is analyst-voice inclusive-of-reader, not first-person personal. The "this chapter is about that decision, and about what it proves" at line 13 is meta-textual analyst-voice register-edge but stays within analytical mode. No first-person-narrative or first-person-essayistic register-breaks observed. Comparative-scaffolding moments (Norway / Alberta / Alaska / Venezuela / Nigeria / Saudi Arabia / Texas / Bismarck-Germany / US Social Security) all hold third-person-analytical register; no slippage into first-person-essayistic voice.

### §5.2 Tense-consistency — ✓ HOLDS

Past tense for historical chronology (Ekofisk discovery 1969, GPF founding 1990, fiscal rule 2001, Alberta/Alaska 1976, SS 1935, Bismarck 1889+1920s, Saro-Wiwa 1995, Nigeria suspensions); present tense for current-state analytical claims (fund holdings, fiscal-rule mechanics, framework conclusions); conditional / future for counterfactual scaffolding (*"If a future application emerges…"*, *"If every country built a Norway-sized fund…"*).

Specific transitions reviewed:

- Lines 7–9 (Ekofisk historical) → lines 9–11 (analytical-present-tense). Cued by topic-shift ("The decision the country faced…" pivots to generic-present "Most jurisdictions spend the money").
- Line 23 (current-AUM present) ↔ line 25 (fiscal-rule mechanics present). Clean.
- Line 29 (perfect-tense chronology: "have changed / have come and gone / has surfaced repeatedly / has argued / have held") — clean perfect-tense throughout the five-declarative cadence (independent of F-V1's voice-polish concern).
- Lines 59–65 (Norway-vs-McDowell): past-tense for McDowell historical scenes ("was not poorly situated"); present-tense for mechanism-generic ("the structural conditions that produce severed costs"); clean.
- Lines 75–87 (Nigeria contrast): past + present mixed by content-cue; clean.
- Lines 95–105 (SS comparator): present-analytical with past-tense historical-design moments (1935 designers); clean.
- Lines 115–123 (Norway-not-solved): present-analytical with conditional ("If a future application emerges…"); clean.

No tense-leakage observed.

### §5.3 Apparatus residue — ✓ NONE BEYOND PASS-1 BASELINE

Verified against `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` + `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` + Pass-1's §"Apparatus regression check" baseline:

- **Lowercase "cost severance"** — appears at lines 15, 39, 43, 53, 63, 83, 85, 105, 129. All correct register (lowercase prose; consistent with Glossary canonical-form per inventory line 23). ✓
- **"accountability bond B" / "B"** — introduced at line 45 (full naming + variable-letter introduction); reused at lines 53, 67, 81, 83 (variable letter B). Permitted single-letter algebraic stand-in per apparatus register; consistent introduction-site convention. ✓
- **Lowercase "residual commons value"** — appears at lines 47, 53, 81, 85. All correct register. ✓
- **"foreclosure component" / "foreclosure"** — appears at lines 49, 115. Lowercase plain-language. ✓
- **"externality tail"** — appears at lines 47, 51, 77, 81, 117. Lowercase plain-language. ✓
- **"Intergenerational Option Value"** — single capitalized usage at line 121 (Ch 4's introduction site per cross-chapter consistency inventory line 40). ✓ matches Pass-1 baseline.

No Greek letters, no subscripts, no integral notation, no formal flagship-term name-defenses, no apparatus introduced from other chapters in body prose. No regression observed.

Standard non-apparatus terms appearing in body prose: GPFG (introduced full-name at line 21); UNEP (introduced full-name at line 79); WWI (standard abbreviation, line 101); Equinor/Statoil (introduced at line 23). All standard. ✓

### §5.4 Hedge phrases — ✓ CLEAN

No *"I will argue that…"* / *"It seems likely that…"* / *"Perhaps…"* patterns. The chapter speaks declaratively throughout.

Notes:
- *"almost uniquely"* at line 9 — substantive content claim (Norway's uniqueness is the chapter's existence-proof thesis); not a register-break hedge.
- *"on the order of one billion dollars"* at line 79 — precision-bounded estimator, not a hedge.
- *"in effect"* at lines 27, 95, 119 — three instances; mild qualifier appropriate to analytical-comparative register. Not a hedge; not a register-break.

### §5.5 Connective-tissue clichés — ✓ MOSTLY CLEAN (one instance flagged as LOW)

No *"in short"* / *"ultimately"* / *"moreover"* / *"furthermore"* / *"that being said"* / *"in this context"* / *"going forward"* / *"at this time"* / *"at the end of the day"* / *"to that end"* / *"as such"* patterns.

One instance flagged: *"Similarly,"* at line 51 — flagged under F-V20 as LOW (lone-instance, paragraph-opener cliché). Optional drop; not a chapter-wide habit.

### §5.6 Expository flatness — ⚠ ONE CHAPTER-WIDE PATTERN FLAGGED (F-V15)

No *"The plain definition is this:"* / *"Here is what I think:"* / *"The argument is simple:"* verbatim matches.

But: "[Setup-clause] is this:" pattern recurs at three chapter-spine claim sites (lines 53, 85, 105). Flagged under F-V15 as MEDIUM (chapter-wide expository-frame pattern density). See §3 above.

### §5.7 Named-subject register — ✓ HOLDS

Norwegian PMs named in official capacity (standard journalistic practice per `feedback_named_subject_consent.md`):

- **Jens Stoltenberg** — line 29 ("Jens Stoltenberg's first ministry"). Named in official capacity. ✓
- **Bondevik II** — line 29 ("Bondevik II's center-right coalition"). Numeral disambiguator applied per Pass-1 MEDIUM-2 ratification. Named in official capacity. ✓
- **Solberg / Støre** — line 29 (last-name-only references to current/recent PMs). Named in official capacity. ✓
- **Ken Saro-Wiwa** — line 79 ("the hanging of Ken Saro-Wiwa in 1995"). Historical-record status (deceased; executed 10 November 1995). Pass-1 consent-check verified clean. ✓

No informal nicknames applied to any political figure. No biographical detail beyond what the argument requires. Norwegian peoples (Ogoni, Ijaw) named as peoples not as individuals (line 77). International oil-companies (Shell, Chevron, ExxonMobil, Total) named in official capacity as historical operators (line 77).

No consent regressions caught in Pass 2.

---

## §6. Out-of-scope-for-Pass-2 — flagged for Pass 3 (audience-load) future-session input

Items that crossed Pass-2 attention during paragraph-by-paragraph read; flagged here so the Pass-3 (audience-load) session has them ready. **Not scored as Pass-2 findings.**

- **Norway-canonization cumulative tonal load.** Multiple chapter lines individually defensible but cumulatively tip toward exemplary-or-aspirational framing: line 21 ("extraordinary in the discipline required"); line 23 universal-per-citizen flourish; line 27 ("outgrown the physical resource that created it"); line 29 ("And the rules have held. … Each generation has declined, explicitly, to consume the capital"); line 33 ("None of this is magic"); line 45 ("no extraction community in the world has matched"); line 53 ("Even the best-managed extraction regime on the planet"). The chapter does load counter-weight at line 109 ("None of this is a blueprint. Norway is an existence proof, not a solution.") and at lines 115–123 ("The part Norway has not solved" §-section). Pass 3 should pressure-test whether the cumulative tonal load lands as exemplary-for-Tier-1-policy-INCLUDE without tipping to utopian-for-Tier-1-quant-EXCLUDE. Specifically: does the chapter's voice tip into Norway-canonization for a Tier-3 anti-petro-state critique reader? Does it land as institutional-realism for a Tier-1 dev-econ reader?

- **Petroleum-state-counterfactual ethics — Venezuela/Nigeria/Saudi Arabia "quickly and badly" framing at line 9.** The opening contrast paragraph groups Venezuela, Nigeria, and early-phase Saudi Arabia under "did it quickly and badly," followed by Texas/Alberta/Alaska under "more carefully." Pass 3 should pressure-test: does this read as analytical-comparison (Tier-1 dev-econ / policy-press INCLUDE) or as cherry-picked failure-case framing (Tier-3 Global-South or anti-imperial-development reader EXCLUDE)? The substantive Nigeria treatment at lines 77–87 is depth-developed (Pass-1-verified Niger Delta + UNEP + Saro-Wiwa anchoring), but the line 9 framing carries the cumulative-tonal-load setup.

- **Bismarck deep-history comparator at line 101.** The single-sentence Bismarck 1889 + 1920s hyperinflation mention (post-Pass-1 spot-fix) carries deep-historical scope-creep risk: does an existence-proof chapter focused on Norway earn a Bismarck-Germany side-mention? Pass-3 should pressure-test whether the comparator is scope-relevant (alternative-architecture-templates-existed argument support) or scope-creep (deep-history reach outside Ch 4's existence-proof scope).

- **US Social Security comparator at lines 91–105.** The funded-vs-pay-as-you-go contrast is substantively developed but politically charged. Lines 95 framings: *"the federal government has spent on general operations — wars, tax cuts, budget gaps, the fiscal pressures of the moment"* (politically-charged enumeration) + *"the system's 'trust fund' is an accounting record of intra-government debt rather than a compounding pool of external capital"* (technically defensible but contested). Pass-3 should pressure-test: does this land for Tier-1 US-policy reader as scholarly contrast (INCLUDE) or as politically-loaded (right-leaning-reader INCLUDE / left-leaning-reader EXCLUDE)? Cross-reference with the chapter's explicit defense at line 103: *"The framework's reading of this comparison is structural and not prescriptive. The framework does not say the U.S. should adopt Norway's architecture."* — does this defensive move pre-empt the political-loading flag?

- **Mega-list at line 49 (78-word petroleum-application enumeration).** Pass-2 flagged F-V9 as cadence-burden via em-dash crutch; Pass-3 should additionally test reader-load: does the five-element list of petroleum-substitution-impossible applications land as substantive-grounding (Tier-1 quant / chemistry-aware reader INCLUDE) or as technical-overwhelm (Tier-1 generalist-policy reader EXCLUDE)?

- **Cross-chapter context-load for Appalachia / McDowell County references.** Line 15 (*"Appalachia is one outcome. Norway is another."*) + line 65 (*"McDowell County was not poorly situated in 1960 because its residents were less deserving than Norwegians."*) reference content developed elsewhere in the book (Ch 1 personal lineage; Ch 2 mechanism introduction). Pass-3 should test whether a reader who has not read Ch 1 / Ch 2 can recover enough context to follow the Norway-vs-McDowell contrast, or whether Ch 4 needs more bridging.

- **F-V14 chiastic constructed→reconstructed coda + Ch 1 F-V9/F-V11 chiastic-emotional-coda pattern.** Pass-2 flagged F-V14's chiastic flourish individually. Under Pass-3 cumulative-chapter-pattern lens, this is the third chiastic-coda occurrence in the book (Ch 1 F-V9 + F-V11 + Ch 4 F-V14) — possible book-wide cadence-habit that an editor reading multiple chapters in sequence may register. Cross-chapter flag.

- **Line 105 "is this:" expository-frame at chapter-spine-emergence moment.** F-V15 flagged the chapter-wide three-instance pattern as Pass-2 voice-polish concern; Pass-3 should additionally test the cumulative analytical-policy-prose register-pressure: does the colon-introduced thesis-claim move land as analytical-confidence (policy-press INCLUDE) or as expository-flatness (literary-essay venue EXCLUDE)?

- **Section break density.** Six section breaks (after lines 17, 35, 55, 71, 89, 107, 125) in a ~3,975-word chapter is comparable to Ch 1's density (six breaks in ~3,800w, flagged under Ch 1 §6 for Pass-3 input). Pass-3 should test whether the break-rhythm supports the chapter's comparative-case-by-case structure or whether it fragments the cumulative argumentative arc.

---

## §7. Out-of-scope-for-Pass-2 — flagged for Pass-1 fact-check follow-up

Items that surfaced during Pass-2 reading but belong to Pass-1's fact-check scope. **Not scored as Pass-2 findings.**

- **Line 79 — "subsequent monitoring suggests cleanup progress has remained well short of that timeline."** Post-Pass-1 spot-fix prose. The "subsequent monitoring" claim is unspecified — no body-prose citation; likely intended to reference HYPREP (Hydrocarbon Pollution Remediation Project) progress reports + civil-society monitoring (Amnesty International, ERA/FoEN, SDN). A publisher fact-checker reading this may query whether the "well short of that timeline" claim is substantiable to a specific source or whether it reads as authorial generalization. Not a new fact-check concern — Pass-1 spot-fix (MEDIUM-3) was applied to scope-clarify the $1B figure, and the prose now hedges the cleanup-progress claim deliberately. **Flagged for Pass-1 follow-up disposition** if author wants to anchor "subsequent monitoring" to a specific source in body prose or endnote.

- **Line 95 — "the system's 'trust fund' is an accounting record of intra-government debt rather than a compounding pool of external capital."** Pass-1-verified per `research/case-studies/social-security.md` §"The Structural History" (Items-verified table at Ch 4:95). The framing is technically accurate but contested-in-popular-discourse — left-leaning policy readers may push back on the framing as right-leaning-coded. Not a new fact-check concern; more an audience-load concern flagged at §6. **No Pass-1 follow-up action recommended.**

- **Line 117 — "Bangladesh, the Sahel, low-lying Pacific island states."** Standard climate-vulnerable-populations typology per Pass-1 Items-verified table at Ch 4:117. **No follow-up action.**

Otherwise no new factual concerns surfaced during Pass-2 reading. Pass 1 + Phase C spot-fixes (MEDIUM-1 through MEDIUM-5 + LOW-1 + LOW-3) cover the externally-verifiable claim set comprehensively.

---

## §8. Verdict synthesis

### §8.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| HIGH | 3 | F-V1 (line 29 five-declarative chronology cadence-flatness); F-V2 (line 81 four-anaphoric "The same X" fragment block); F-V3 (lines 115/117/119/121 four-paragraph "It does not…" anaphoric block) |
| MEDIUM | 12 | F-V4 (line 9 "Some did X / Some did Y" petroleum-state survey); F-V5 (line 11 negation-negation-affirmation declarative-three); F-V6 (line 15 double-anaphoric outcome/variable); F-V7 (line 31 "The X would be Y" three-declarative); F-V8 (line 39 "The X is Y" three-declarative); F-V9 (line 49 78-word em-dash mega-parenthetical); F-V10 (line 63 "mechanism / not bug / selection criterion" three-declarative); F-V11 (line 83 stacked-tic decomposition paragraph); F-V12 (line 95 em-dash density — 4 em-dashes); F-V13 (line 97 "Both are X" three-anaphora); F-V14 (line 105 stacked-pattern + chiastic coda); F-V15 (chapter-wide "[Setup] is this:" expository-frame pattern at lines 53/85/105) |
| LOW | 8 | F-V16 (line 23 five-noun list); F-V17 (line 27 "The oil / The fund" closer); F-V18 (line 33 "None of this is magic" meta-frame); F-V19 (line 43 standalone two-statement paragraph); F-V20 (line 51 "Similarly" + "No fund can"); F-V21 (line 67 within-sentence "with X, with Y, with Z"); F-V22 (line 131 chapter-spine "Neither outcome was inevitable. Both were engineered."); F-V23 (line 133 "Each one tells…" bookend) |

**Total findings:** 23 (3 HIGH + 12 MEDIUM + 8 LOW).

### §8.2 Aggregate Pass-2 verdict

**READY AFTER SPOT-FIXES (THREE HIGH-SEVERITY).**

The chapter is fundamentally strong analytical-comparative policy prose. Voice holds third-person-analytical throughout; tense holds; no apparatus regression beyond Pass-1 baseline; named-subject register holds; hedge-phrase patterns are clean; connective-tissue cliché count is one (lone "Similarly" at line 51). The three HIGH-severity findings cluster around the chapter's primary cadence risks: (1) date-heavy chronology cadence-flatness at the political-consensus paragraph (line 29 five-declarative), (2) the chapter's central rhetorical-pivot four-fragment anaphoric block (line 81 "The same X" structure), and (3) the chapter-scale four-paragraph "It does not…" anaphoric block at the §"The part Norway has not solved" section. All three are addressable via spot-fixes with multiple low-risk option-paths.

The 12 MEDIUM findings cluster around four patterns: (a) tidy-parallel two-or-three-element anaphoric structures (F-V4, F-V6, F-V7, F-V8, F-V13) — many substantively-earned but cumulatively visible; (b) declarative-three-in-a-row negation-affirmation cadence (F-V5, F-V10) — rhetorically earned but on the named pattern; (c) em-dash density (F-V9, F-V12) — comparable to Ch 1's flagged paragraphs; (d) stacked-tic paragraphs at chapter-spine claims (F-V11, F-V14) where multiple named patterns co-occur; plus (e) the chapter-wide "[Setup-clause] is this:" expository-frame pattern (F-V15) recurring at three chapter-spine claim sites.

The 8 LOW findings are style preferences; hold-as-is is the recommendation across all 8.

**No structural voice revision needed.** All findings are addressable via spot-fixes; the chapter's analytical-comparative register and comparative-case scaffolding are sound. Chapter is on track for Phase-A completion after HIGH spot-fixes (+ any MEDIUM the author opts to apply) and the subsequent Pass-3 (audience-load) session.

### §8.3 Phase-C disposition recommendation

The author should ratify HIGH and MEDIUM findings via a separate Phase-C spot-fix session. Recommended sequencing:

1. **Apply F-V1 + F-V2 + F-V3 (all three HIGH).** All three are named-inventory verbatim matches; all three have multiple low-risk option-paths; all three sit at structurally load-bearing positions (line 29 political-consensus argument; line 81 Niger-Delta-vs-Norway rhetorical pivot; lines 115–121 §"The part Norway has not solved" gap-naming inventory). Resolving these removes the chapter's most editor-detectable cadence patterns.

2. **Review F-V12 + F-V9 (em-dash-density pair).** Two of the chapter's densest em-dash paragraphs — line 49 (78-word mega-parenthetical) and line 95 (4 em-dashes / 2 parenthetical pairs). Resolving them together addresses the chapter-wide em-dash habit comparable to Ch 1's F-V4 + F-V8 disposition.

3. **Review F-V15 (chapter-wide "[Setup] is this:" expository-frame pattern).** Three-instance chapter-wide pattern at lines 53 / 85 / 105. Resolving 1–2 of the three instances reduces the chapter-wide pattern visibility; resolving all three drops the pattern entirely. Author judgment on which instances most earn the cadence-introducer.

4. **Review F-V8 + F-V11 + F-V13 + F-V14 (the four MEDIUM findings most likely to flag for a trade-press editor scanning for AI-prose patterns).** The "rents/community/architecture" three-declarative at line 39; the stacked-tic cost-severance-decomposition at line 83; the "Both are X" three-anaphora at line 97; the stacked-pattern + chiastic coda at line 105.

5. **Hold F-V4 + F-V5 + F-V6 + F-V7 + F-V10 (the five MEDIUM findings most substantively-earned as analytical-cadence enacting comparative-argument content).** Author's call; these are defensible as cadence-enacting-content.

6. **Hold F-V16 through F-V23 (all 8 LOW findings).** Default LOW disposition; style preferences; structurally load-bearing as chapter-spine punches or content-determined enumeration.

---

## §9. What this pass did NOT do

Per author's per-prompt scoping + v2.0 Amendment B distinct-pass discipline:

- **Did NOT re-run Pass 1 (fact-check).** Pass 1 ratified 2026-05-12 + LOW follow-up 2026-05-13. The post-spot-fix prose (138 lines as of 2026-05-15) is the audit baseline; Pass-1 findings are not re-litigated. Three incidental fact-check observations surfaced (line 79 "subsequent monitoring" specificity; line 95 trust-fund-as-accounting-record contested framing; line 117 climate-vulnerability typology) and are flagged forward at §7 for Pass-1 disposition or noted as no-action-recommended.
- **Did NOT score Pass 3 (audience-load).** Pass 3 is a separate session per the workstream handoff per-prompt serial cadence. Pass-2-surfaced audience-load concerns (Norway-canonization cumulative tonal load; Venezuela/Nigeria framing ethics; Bismarck scope-creep; US-Social-Security political-loading; mega-list reader-load; cross-chapter context-load for Appalachia/McDowell; book-wide chiastic-coda cumulative pattern; "is this:" expository-frame audience-register-pressure; section-break density) are flagged at §6 for Pass-3 input but are not scored here.
- **Did NOT apply spot-fixes to the chapter file.** Phase C (per-chapter spot-fix application session) does that after author ratification.
- **Did NOT re-write paragraphs.** Findings + proposed revision options + STOP, per the Pass-2 template's hard constraint.
- **Did NOT contact named subjects.** Per consent discipline; no living named subjects in Ch 4 require consent gating.
- **Did NOT propose new framework concepts or meta-conclusions about the v2.0 discipline.** Per Pass-2 template's hard constraint.

---

## §10. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__4_THEEXISTENCEPROOF__Draft.md`.
- ✓ Did NOT re-run Pass 1 (fact-check) — referenced only for context; three incidental observations flagged forward at §7.
- ✓ Did NOT score Pass 3 (audience-load) — concerns flagged forward to that session.
- ✓ Did NOT re-write paragraphs — proposed-revision options offered without applying.
- ✓ Did NOT contact named subjects.
- ✓ Did NOT propose new framework concepts.
- ✓ Verified post-spot-fix chapter line count (138 lines, 2026-05-15) against current origin/main.
- ✓ Verified Pass-1 artifact exists at the cited path (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md`).
- ✓ Verified Ch 1 Pass-2 artifact exists at the cited path and used it as canonical format model (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md`).
- ✓ Verified apparatus register canonical decisions in `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` and confirmed no apparatus regression beyond Pass-1 baseline.
- ✓ Verified cross-chapter consistency inventory canonical-terms inventory in `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` (Norway / GPFG / Cost Severance / Intergenerational Option Value rows).
- ✓ Verified named-Norway-figure register (Stoltenberg, Bondevik II, Solberg, Støre, Saro-Wiwa) against Pass-1 §"Items verified" table; all hold consent-clean register.
- ✓ Built feature branch `claude/ch4-voice-polish-pass2-cpINa` from current origin/main per workstream handoff branch discipline.

---

*End of Ch 4 Stage-3 Pass 2 (Voice-Polish) rigor pass. PROPOSED — awaiting author ratification at a separate Phase C session. Pass 3 (audience-load) is the next session for this chapter per workstream #20 Phase A per-prompt serial cadence.*
