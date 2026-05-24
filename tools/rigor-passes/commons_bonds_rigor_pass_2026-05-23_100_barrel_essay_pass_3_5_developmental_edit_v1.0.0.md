# $100 Barrel Essay — Pass 3.5 Developmental-Edit (Restoration Polarity) v1.0.0 — 2026-05-23

**Status:** RATIFIED + APPLIED 2026-05-24 (Amendment A applied; all 6 findings interactively ratified + Phase C-α/β applied to essay file). Pass 3.5 developmental-edit artifact fired after Pass 3.4 RATIFIED 2026-05-23 (commit `63e149a`). Whole-essay restoration-polarity audit per v3.1 Amendment B + pipeline doctrine §3.6.3. Polarity is restoration (adds back richness, scenes, sensory detail), NOT cutting.

**Amendment A — 2026-05-24. RATIFICATION + APPLICATION.** All 6 findings interactively ratified + applied per v3.1 Amendment C Interactive Ratification Protocol. Per-finding dispositions:

| Finding | Severity | Disposition | Net delta |
|---|---|---|---|
| F-DE-Barrel-1 | MEDIUM | Option A as recommended (3-figure scene-anchor) | +24w |
| F-DE-Barrel-2 | MEDIUM | Option A as recommended (Sandel signature-example anchor) | +28w |
| F-DE-Barrel-3 | MEDIUM | Option A as recommended ("That is Rawls applied across time." bridge); **directly resolves Pass 3.3 light flag #2** | +5w |
| F-DE-Barrel-4 | LOW | **Option B author-selected** (2-example + analytical close; not Pass 3.5's Option A 3-example recommendation). Author preferred conservative-on-rule-of-three reading + the analytical-close sentence ("system that consumes faster than it regenerates eventually breaks") which generalizes the two examples up to a principle | +20w |
| F-DE-Barrel-5 | LOW | Option A as recommended (Nordhaus methodological-position framing); marginal Tier 1 #3 + A5 lift | +21w |
| F-DE-Barrel-6 | LOW | Option A as recommended (verb texture variance: looked at / showed / framed / proved a rule for / asked / fought about) | -8w |
| **NET** | | | **+90w** |

Body word count: 4,145w (post-Pass-3.2-Phase-C) → 4,248w (post-Pass-3.5-Phase-C). Within Stage 1 brief §10 window (3,500–4,500w).

One finding where applied disposition differs from Pass 3.5's original recommendation transparently logged: F-DE-Barrel-4 (Option B selected over recommended Option A). Reasoning recorded in §3 Synthesis updates below.

Phase C application committed to essay file (`manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md`) in same session; artifact + essay updates batched into single commit per atomic Phase C standard.

Active-findings count post-Amendment-A: 0 (all 6 findings APPLIED).

**Audit target:** [`manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md`](../../manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md) (4,145w post-Pass-3.2-Phase-C + post-Pass-3.3-light-RATIFIED + post-Pass-3.4-light-RATIFIED; on `main` commit `63e149a`).

**Source of truth for restoration discipline:** v3.1 Amendment B per [`tools/memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) + Ch 1 developmental-edit empirical anchor (2026-05-18; 3 HIGH + 7 MEDIUM + 3 LOW findings on a ~9,000w chapter).

**Restoration-polarity scan categories:**
- Emotional-arc continuity (less applicable for intellectual essay)
- Scene-anchor density (Norway / Nigeria / Appalachia scenes; §II Lithium/cobalt vignette)
- Sensory-detail restoration (places where description is too abstract)
- Voice-flow continuity (breaks introduced by Pass 3.2 chiseling)
- Cumulative-LLM-cadence residue (patterns surviving Pass 3.2)
- Reader-engagement at analytical pivots (§I→II→III→IV→V→VI→Close transitions)
- Faithfulness-of-the-model lineage (consistency with Stage 1 brief structural decisions)

**Empirical-anchor calibration:** Essay (~4,145w) is roughly half the length of a chapter; restoration findings expected ~half the chapter count. Estimate 0–1 HIGH + 2–4 MEDIUM + 2–3 LOW. **Actual count:** 0 HIGH + 3 MEDIUM + 3 LOW = **6 findings.** Consistent with calibration.

---

## 1. Findings

Severity tiers per template:
- **HIGH** — load-bearing restoration that compounds across the essay; submission-blocking if not addressed
- **MEDIUM** — register-level finding; localized restoration
- **LOW** — sharpening / texture option; defensible either way

### F-DE-Barrel-1 — §II thirty-years-of-people abstraction missing scene-anchor — MEDIUM

**Location:** §II ¶6 (line 117).

**Verbatim current text:**
> And here is the part the rest of this essay turns on. Even when the substitution does arrive, no mechanism in the system compensates the people who lived through the gap. If the substitution arrives in 2080 and the resource runs out in 2050, then thirty years of people get poorer transportation, poorer healthcare, poorer everything that depended on the missing resource.

**Finding:** "Thirty years of people" is the load-bearing intergenerational-cost claim of §II — the rhetorical pivot that lifts the essay from technical-economic discussion ("substitutability assumption") to the moral pivot the rest of the essay turns on. But "thirty years of people" is faceless. "Poorer transportation, poorer healthcare, poorer everything" is a three-fold abstraction list. The sentence is doing the load-bearing work that the rest of the essay relies on, but the reader experiences it as analytical claim rather than concrete loss.

**Restoration polarity:** Add one specific human-scale moment to anchor the thirty-years-of-people abstraction. The §II close is where the reader needs to *feel* the intergenerational-cost claim, not just process it.

**Proposed correction (verbatim replacement prose):**

> And here is the part the rest of this essay turns on. Even when the substitution does arrive, no mechanism in the system compensates the people who lived through the gap. If the substitution arrives in 2080 and the resource runs out in 2050, then thirty years of people — the child born in 2055, the grandparent who outlives the resource by a decade, the working family that loses the input their livelihood depends on — get poorer transportation, poorer healthcare, poorer everything that depended on the missing resource.

(Inserts a three-figure anchor between "thirty years of people" and "get poorer transportation." Net: +24w. Restoration polarity: makes the faceless abstraction visible as specific people without losing the analytical structure.)

**Alternative correction (single-figure anchor; more compressed):**

> If the substitution arrives in 2080 and the resource runs out in 2050, then thirty years of people get poorer transportation, poorer healthcare, poorer everything that depended on the missing resource. The child born in 2055 will be thirty when the substitute finally arrives, and never have known the world the missing resource built.

(Adds a single concrete-figure sentence after the abstraction. Net: +23w. The single-figure version foregrounds time-and-arc (the child grows up in the gap) where the three-figure version foregrounds breadth (three generations affected). Author disposition.)

**Cross-pass impact:** No Pass 3.1 fact-check impact (no factual claim being made; concrete-figure restoration is rhetorical anchoring). Marginal Pass 3.3 lift for Tier 3 #16 working-class reader + #17 extraction-zone reader + #18 first-gen reader (concrete figures land harder than abstractions). No Pass 3.4 robustness impact (the analytical claim is unchanged; the restoration adds anchor without changing the structural argument).

---

### F-DE-Barrel-2 — Sandel paragraph project-description without anchor — MEDIUM

**Location:** §IV ¶4 (line 153; post-F-VP-Barrel-4-Option-D opening).

**Verbatim current text:**
> Michael Sandel, in *What Money Can't Buy: The Moral Limits of Markets*, published by Farrar, Straus and Giroux in 2012, has spent a career arguing that some goods cannot be priced without being corrupted by the pricing, and that markets have a moral domain beyond which their application produces distortion rather than allocation. The permanent foreclosure of a non-renewable resource sits squarely inside Sandel's territory. So does the question of whether discounting an unborn person's welfare is a category error rather than a calculation.

**Finding:** Sandel's project is described abstractly ("some goods cannot be priced without being corrupted by the pricing") but the paragraph never anchors with a Sandel example. Readers who know Sandel will fill in the gap from memory; readers who don't will register the description as authorial assertion without specific content. Sandel has signature examples (paid kidney donation; paid school admission slots; the GDR fertilizer-for-blood scheme; paid line-standing in Disney) that are exactly the move readers need to feel the market-moral-limits claim.

**Restoration polarity:** Add one Sandel example to anchor the abstract project-description. The Condition 1 convergent-intuition move depends on the reader feeling Sandel's argument as a real alternative philosophical frame; absent a concrete Sandel anchor, the convergent-intuition claim reads as authorial assertion.

**Proposed correction (verbatim replacement prose):**

> Michael Sandel, in *What Money Can't Buy: The Moral Limits of Markets*, published by Farrar, Straus and Giroux in 2012, has spent a career arguing that some goods cannot be priced without being corrupted by the pricing, and that markets have a moral domain beyond which their application produces distortion rather than allocation. Sandel's signature examples — the paid kidney donor, the wealthy parent who pays for the priority school admission slot — work because the pricing changes what the thing is, not just who can have it. The permanent foreclosure of a non-renewable resource sits squarely inside Sandel's territory. So does the question of whether discounting an unborn person's welfare is a category error rather than a calculation.

(Inserts one Sandel-example sentence between project-description and territory-claim. Net: +28w. Restoration polarity: anchors abstract project-description with concrete signature examples.)

**Alternative correction (single Sandel example, more compressed):**

> Michael Sandel, in *What Money Can't Buy: The Moral Limits of Markets*, published by Farrar, Straus and Giroux in 2012, has spent a career on the puzzle Sandel illustrates with paid kidney donation: pricing the thing changes what the thing is, not just who can have it. The permanent foreclosure of a non-renewable resource sits squarely inside Sandel's territory...

(Restructures the first sentence to embed the Sandel example. Net: +5w. Tighter; loses the project-summary scope claim.)

**Cross-pass impact:** No Pass 3.1 fact-check impact (the Sandel examples are common-knowledge from *What Money Can't Buy*). Marginal Pass 3.3 lift for Tier 1 #1 PW editorial + #2 PW reader (better Sandel engagement signal) + Tier 3 #16 working-class + #18 first-gen (concrete examples land). Possible Pass 3.4 robustness lift on A4 reactionary intellectual reader (Sandel's market-moral-limits work is well-known on conservative-philosophy register; anchored treatment may strengthen disarming).

---

### F-DE-Barrel-3 — §IV ¶4 entry-point scene-bridge after Pass-3.2 throat-clearing drop — MEDIUM

**Location:** §IV ¶3 close + §IV ¶4 open (lines 151–153 boundary).

**Verbatim current text (transition):**

> [§IV ¶3 close, line 151] ...You cannot, behind the veil, agree to a discount rate that values that future person's wellbeing at a hundredth of your own. You would not be sure who you were going to be.
>
> [§IV ¶4 open, line 153] I am using Rawls as one frame among several that produce the same intuition. Other traditions converge on the same point.

**Finding:** Per Pass 3.3 light's audit-trail flag #2 — F-VP-Barrel-4 Option D dropped the throat-clearing "I want to name what I am doing here." prefix from §IV ¶4 opening. The Pass 3.3 light verdict accepted this as HOLDS on Tier 1 #3 (possibly with margin reduction) because the substantive first-person methodological language carries the meta-load.

The §IV ¶3 close ends inside-the-veil voice ("You would not be sure who you were going to be."). The §IV ¶4 open is outside-the-veil meta-commentary ("I am using Rawls as one frame..."). The voice-mode shift is abrupt. The throat-clearing wrapper Pass 3.2 dropped was doing voice-bridge work as well as meta-flagging.

**Restoration polarity:** Add a brief transitional sentence that does voice-bridge work without re-introducing throat-clearing tic. The bridge should name what the prior paragraph just did (Rawlsian application across time) before moving to meta-commentary about Rawls being one of several frames.

**Proposed correction (verbatim replacement prose):**

> [§IV ¶3 close, unchanged] ...You cannot, behind the veil, agree to a discount rate that values that future person's wellbeing at a hundredth of your own. You would not be sure who you were going to be.
>
> [§IV ¶4 open] **That is Rawls applied across time.** I am using Rawls as one frame among several that produce the same intuition. Other traditions converge on the same point.

(Inserts a 5-word transitional sentence at the start of §IV ¶4. Net: +5w. Restoration polarity: names the move that just happened in the prior paragraph; provides scene-bridge for the voice-mode shift; preserves F-VP-Barrel-4 Option D's removal of the throat-clearing wrapper.)

**Alternative correction (longer bridge with framing):**

> [§IV ¶4 open] **The Rawlsian veil applied across time is the intuition I am building on here.** I am using Rawls as one frame among several that produce the same intuition. Other traditions converge on the same point.

(13-word bridge; more explicit framing. Net: +13w. Slightly heavier; brings the meta-move closer to the prior throat-clearing register without re-introducing the tic. Author disposition.)

**Option C — keep as-is (reject):**

Leave §IV ¶4 opening with no bridge. The abrupt voice-mode shift is acceptable; the substantive first-person methodological language carries the meta-load per Pass 3.3 light verdict.

**Recommendation:** Option A ("That is Rawls applied across time."). The 5-word bridge does scene-bridge work without re-introducing throat-clearing. It names what just happened in §IV ¶3 (Rawls applied across time) before transitioning to outside-the-veil meta-commentary. The opening "That is" gives the §IV ¶4 reader a back-reference anchor; "Rawls applied across time" makes explicit the move the prior paragraph performed implicitly. Note: this finding addresses Pass 3.3 light's audit-trail flag #2 directly; if applied, the "Notice the move." retrofit option Pass 3.3 light reserved as backup becomes unnecessary.

**Cross-pass impact:** Pass 3.3 light flag #2 directly addressed; the §IV ¶4 entry-point skim-read concern Pass 3.3 light surfaced is resolved by this bridge. Tier 1 #3 (center-right policy reader) skim-read protection lifts slightly from this restoration. No Pass 3.4 robustness impact (A4-defense moves were never anchored at §IV ¶4). No Pass 3.1 fact-check impact.

---

### F-DE-Barrel-4 — Daly throughput abstraction without concrete example — LOW

**Location:** §III ¶7 (line 133).

**Verbatim current text:**

> Herman Daly, who died in 2022, came closer than anyone. Daly's *Steady-State Economics*, originally published by W. H. Freeman in 1977 and reissued by Island Press in 1991, framed the economy as a subsystem of the biosphere rather than the other way around. The economy lives inside the ecology; the ecology has finite capacity to absorb waste and finite capacity to regenerate stocks. Throughput — the flow of matter and energy from environment through economy and back — must stay within the regenerative limits of the biosphere or the system overshoots. Daly's contribution was foundational, and the field that grew up around him (ecological economics, as Daly and Joshua Farley named it in their textbook of that title) has been doing serious work for half a century.

**Finding:** Daly's throughput concept is defined abstractly ("the flow of matter and energy from environment through economy and back"). The paragraph names the concept and the field but doesn't anchor throughput with a concrete instance. Compare the surrounding paragraphs: Marx is anchored with "the worker who creates more value than he is paid"; Ostrom is anchored with "fisheries that did not collapse"; Hartwick is anchored with "roads, schools, factories, productive plant." Daly is the only lineage figure whose contribution is described entirely at the framework level.

**Restoration polarity:** Add one concrete throughput example to bring Daly's contribution into the same scene-anchor register as his neighbors in the lineage map.

**Proposed correction (verbatim replacement prose):**

> Herman Daly, who died in 2022, came closer than anyone. Daly's *Steady-State Economics*, originally published by W. H. Freeman in 1977 and reissued by Island Press in 1991, framed the economy as a subsystem of the biosphere rather than the other way around. The economy lives inside the ecology; the ecology has finite capacity to absorb waste and finite capacity to regenerate stocks. Throughput — the flow of matter and energy from environment through economy and back — must stay within the regenerative limits of the biosphere or the system overshoots. **A fishery that takes more than it regrows is overshoot; an atmosphere that takes more carbon than it can absorb is overshoot; an aquifer drawn faster than it recharges is overshoot.** Daly's contribution was foundational, and the field that grew up around him (ecological economics, as Daly and Joshua Farley named it in their textbook of that title) has been doing serious work for half a century.

(Inserts one rule-of-three concrete-throughput sentence between the abstract definition and the field-recognition close. Net: +29w. Restoration polarity: anchors abstract throughput with concrete examples that mirror the §II substitution examples (coal/whale oil/copper) for stylistic continuity.)

**Concern with the proposed correction:** The added sentence is a rule-of-three. Pass 3.2 chiseled rule-of-three triplets elsewhere in the essay (F-VP-Barrel-2 §II "may" parallel; F-VP-Barrel-3 §III close "Each X-ing"). Adding a new rule-of-three under restoration polarity risks contradicting the chiseling discipline. The trade-off: the rule-of-three here is doing concrete-anchor work (three throughput examples) which is exactly the function Pass 3.2 protected when it preserved the §III "fisheries / forests / irrigation" rule-of-three for Ostrom. Defensible but borderline.

**Alternative correction (two-example version; reduces rule-of-three concern):**

> Throughput — the flow of matter and energy from environment through economy and back — must stay within the regenerative limits of the biosphere or the system overshoots. **A fishery taken faster than it regrows; an atmosphere given more carbon than it can absorb. The system that consumes faster than it regenerates eventually breaks.**

(Two parallel examples + one analytical close. Net: +20w. Avoids the rule-of-three concern by structurally separating examples from analytical close.)

**Cross-pass impact:** None on Pass 3.1 (no factual claim). Marginal Pass 3.3 lift for Tier 3 readers (concrete examples help). No Pass 3.4 impact.

**Recommendation:** Author disposition. LOW severity; defensible to apply or hold.

---

### F-DE-Barrel-5 — Nordhaus paragraph one-sided framing (rate without moral position) — LOW

**Location:** §V ¶3 (line 171).

**Verbatim current text:**

> William Nordhaus, who received the 2018 Nobel Memorial Prize in Economic Sciences for integrating climate change into long-run macroeconomic analysis, has argued in the other direction. Nordhaus's DICE model (Dynamic Integrated Climate-Economy) has used a discount rate in the region of 4.3 percent in its early iterations, on the grounds that the rate should reflect observed market rates of return on capital. From that higher rate followed a much lower social cost of carbon, in the range of thirty-five dollars per ton in the same comparison frame.

**Finding:** Stern's paragraph gives both the rate AND the moral position ("the welfare of future generations should not be discounted simply because they are future"). Nordhaus's paragraph gives the rate AND the empirical rationale ("the rate should reflect observed market rates of return on capital") but stops short of the moral or methodological position behind that rationale. The asymmetry is small but real — Stern is humanized in the essay (a moral position credited); Nordhaus is technicalized (an empirical claim only).

For a Condition 1 reader (center-right policy reader who may sympathize with Nordhaus's lower-rate position), the asymmetry could read as the essay tilting toward Stern's moral framing while reducing Nordhaus to a technical observation. Restoration polarity could add a brief Nordhaus-position phrase to symmetrize the engagement.

**Restoration polarity:** Add one phrase that gives Nordhaus's methodological-or-moral position behind the discount-rate choice, so the §V engagement reads as symmetric inventory rather than one-sided framing.

**Proposed correction (verbatim replacement prose):**

> William Nordhaus, who received the 2018 Nobel Memorial Prize in Economic Sciences for integrating climate change into long-run macroeconomic analysis, has argued in the other direction. Nordhaus's DICE model (Dynamic Integrated Climate-Economy) has used a discount rate in the region of 4.3 percent in its early iterations, on the grounds that **a credible cost-benefit analysis must reflect the rate at which the economy actually trades present for future — observed market rates of return on capital, not a rate chosen on first principles**. From that higher rate followed a much lower social cost of carbon, in the range of thirty-five dollars per ton in the same comparison frame.

(Inserts methodological-position framing between "on the grounds that" and "observed market rates of return on capital." Net: +21w. Restoration polarity: symmetrizes §V engagement; gives Nordhaus methodological weight comparable to Stern's moral weight.)

**Cross-pass impact:** Marginal Pass 3.3 lift for Tier 1 #3 center-right policy reader (Nordhaus methodologically credited; reduces asymmetry that could read as left-academic framing). Marginal Pass 3.4 lift for A5 orthodox-econ reader (the Nordhaus methodological framing engages the orthodox-econ tradition directly). No Pass 3.1 fact-check impact (Nordhaus's position is well-documented in the cited NBER paper).

**Recommendation:** Author disposition. LOW severity; the asymmetry is small and defensible either way. Pass 3.4 light already confirmed Stern-Nordhaus engagement holds at ROBUST.

---

### F-DE-Barrel-6 — §Close "looked at" parallel structure (rule-of-six recap) — LOW

**Location:** §Close ¶3 (line 209).

**Verbatim current text:**

> The lineage that has done the work on adjacent territory has been doing real work for centuries. Marx looked at the surplus and where it went. Ostrom looked at renewable commons and how communities sustained them. Daly looked at the biosphere as the system inside which the economy actually lives. Hartwick looked at how to keep consumption going when a resource has run out. Rawls and Sandel and Parfit looked at what is owed across time. Stern and Nordhaus and Weitzman looked at how much the climate damage of consumption is worth in present dollars.

**Finding:** Six sentences with identical opening structure ("[Name] looked at..."). The parallel does recap work — each tradition gets one summary sentence at the §Close before the framework's load-bearing piece is named. The parallel is functional (skim-readers can scan the lineage at a glance) but also tic-adjacent (six-fold parallel is more than the LLM-tic-three threshold from Stage 1 brief §5).

**Restoration polarity tension:** Pass 3.5 polarity is restoration, NOT chiseling. The rule-of-six is functional and shouldn't be cut to reduce parallel structure. But the function could be served with texture variance — varying the verb or syntactic structure across the six sentences while preserving the recap function.

**Proposed correction (verbatim replacement prose; texture-variance version):**

> The lineage that has done the work on adjacent territory has been doing real work for centuries. Marx looked at the surplus and where it went. Ostrom showed how communities sustained renewable commons. Daly framed the biosphere as the system inside which the economy lives. Hartwick proved a rule for keeping consumption going when a resource runs out. Rawls, Sandel, and Parfit asked what is owed across time. Stern, Nordhaus, and Weitzman fought about how much climate damage is worth in present dollars.

(Varies the verb across six sentences: "looked at / showed / framed / proved / asked / fought about." Recap function preserved; parallel-cadence flattened. Net: -8w; slight tightening.)

**Concern with the proposed correction:** Texture variance may lose the recap function's primary value — that skim-readers can scan six identical-structure sentences quickly. The "looked at" parallel is what makes the recap scannable. Varying the verbs makes the §Close marginally more textured but marginally less scannable.

**Recommendation:** Author disposition. LOW severity; the rule-of-six is borderline-tic but doing real recap work. Defensible to apply texture variance or to preserve the parallel.

**Cross-pass impact:** Marginal Pass 3.3 trade-off (Tier 1 #1 PW editorial brain may prefer texture variance; Tier 3 #16 working-class reader may prefer scannable parallel). No Pass 3.4 impact.

---

## 2. Verified clean (no findings; logged for completeness)

The following Pass 3.5 restoration-polarity categories were scanned and **no findings surfaced**:

- ✅ **Norway scene (§VI ¶3–¶5):** Scene-anchor density is excellent. "Three days before Christmas" + "The country was small, the find was enormous" + the five-government-list (Stoltenberg I / Bondevik II / Stoltenberg II / Solberg / Støre) + the >$2T / ~$400K-per-citizen figures + "constitutional in a way nothing else has." Strong sensory, narrative, and quantitative anchoring.
- ✅ **Nigeria scene (§VI ¶6–¶7):** Scene-anchor density is excellent. "More than thirty billion barrels" + Saro-Wiwa 1995 + Commonwealth suspension + UNEP 2011 / $1B / 25-30 years + "The revenue went elsewhere. The costs stayed." Strong narrative and quantitative anchoring.
- ✅ **§I thought-experiment opener:** "Permian sandstone or some North Sea seabed or some Niger Delta wetland, in the dark" — strong sensory + geographic + temporal anchoring. No restoration needed.
- ✅ **§III lineage map (Marx, Ostrom, Hartwick):** Marx anchored with "the worker who creates more value than he is paid"; Ostrom anchored with "Fisheries that did not collapse. Forests that were not clearcut. Irrigation systems that did not dry."; Hartwick anchored with "roads, schools, factories, productive plant." Three of four lineage figures fully scene-anchored. (Daly is the exception — see F-DE-Barrel-4.)
- ✅ **§III close interactive spot-fix passage (line 143):** The post-2026-05-23 spot-fix passage already added "not seated at the table" + "the bill comes due in their lifetimes rather than ours" — strong scene anchors for the cost-severance image.
- ✅ **§V discount-rate illustration (§V ¶5):** "At Stern's rate, a hundred-dollar benefit a century from now is worth about twenty-five dollars today. At Nordhaus's, the same hundred dollars a century out is worth about a dollar and a half. The same future event ... registers as either an emergency or a rounding error depending on which rate goes into the denominator." Excellent concrete-numerical anchoring + memorable rhetorical close.
- ✅ **§VI architecture-fix close (§VI ¶7, LOCKED):** "What I am calling for, then, is not revolution. I do not think revolution solves this. ... is not a left-wing argument. It is not a right-wing argument. It is a principle of honest dealing." Preserved verbatim per Stage 1 brief §8 locked-element discipline.
- ✅ **§Close closing sentences (§Close ¶4–¶5):** "There is no shortcut. There is also no longer a missing word for what we are trying to build." Vibrant closing sentences with concrete-image work.
- ✅ **Voice-flow continuity at Pass 3.2 spot-fix sites (F-VP-Barrel-1.1, 1.2, 1.3, 2):** Reads cleanly post-collapse. No flatness residue surfaces from Pass 3.2 chiseling at these sites.
- ✅ **Reader-engagement at §II→§III pivot:** "Several traditions have noticed pieces of that absence. None of them has named the piece that survives all of their analyses." Clean analytical-bridge transition.
- ✅ **Reader-engagement at §III→§IV pivot:** "The piece that survives them all is a question of obligation across time. To name it requires a different lineage than the one just walked. It requires a tradition of moral philosophy." Strong genre-transition signal.
- ✅ **Reader-engagement at §V→§VI pivot:** "A framework that names a gap and stops is half a framework. The question that follows — what would it look like to close the gap, in practice, in actual jurisdictions — is the next piece of work." Excellent forward-moving transition.

---

## 3. Synthesis — Phase C application order + cross-pass impact

### 3.1 Findings by severity

| Severity | Count | Findings |
|---|---|---|
| HIGH | 0 | (none) |
| MEDIUM | 3 | F-DE-Barrel-1 (§II thirty-years-of-people anchor); F-DE-Barrel-2 (Sandel example anchor); F-DE-Barrel-3 (§IV ¶4 entry-point scene-bridge — addresses Pass 3.3 light flag #2) |
| LOW | 3 | F-DE-Barrel-4 (Daly throughput anchor); F-DE-Barrel-5 (Nordhaus symmetric framing); F-DE-Barrel-6 (§Close rule-of-six texture variance) |

### 3.2 Phase C application order (recommended)

1. **F-DE-Barrel-3** (MEDIUM; addresses Pass 3.3 light flag #2). Highest-priority MEDIUM because it directly resolves a flagged concern from a prior pass.
2. **F-DE-Barrel-1** (MEDIUM; §II load-bearing pivot anchor). Anchors the essay's central intergenerational-cost claim.
3. **F-DE-Barrel-2** (MEDIUM; Sandel example anchor). Strengthens Condition 1 convergent-intuition move + Pass 3.4 A4 robustness.
4. Optional LOW findings per author disposition:
   - F-DE-Barrel-5 (Nordhaus symmetric framing) — Condition 1 + A5 robustness lift.
   - F-DE-Barrel-4 (Daly throughput anchor) — stylistic-continuity lift in §III.
   - F-DE-Barrel-6 (§Close texture variance) — borderline; defensible either way.

### 3.3 Net word-count impact

| Finding | Net delta |
|---|---|
| F-DE-Barrel-1 (proposed) | +24w |
| F-DE-Barrel-2 (proposed) | +28w |
| F-DE-Barrel-3 (recommended Option A) | +5w |
| F-DE-Barrel-4 (proposed) | +29w |
| F-DE-Barrel-5 (proposed) | +21w |
| F-DE-Barrel-6 (proposed; texture variance) | -8w |
| **Net (all applied):** | **+99w** |
| **Net (MEDIUMs only):** | **+57w** |
| **Net (MEDIUMs + F-DE-Barrel-5):** | **+78w** |

Body word count post-application:
- All findings applied: 4,145 + 99 = **4,244w** (well within Stage 1 brief §10 ceiling 4,500w)
- MEDIUMs only: 4,145 + 57 = **4,202w**
- Sweet spot if author selects MEDIUMs + F-DE-Barrel-5: 4,223w

### 3.4 Cross-pass impact summary

| Finding | Pass 3.1 fact-check | Pass 3.3 acceptance | Pass 3.4 robustness | Pass 3.2 polarity-conflict |
|---|---|---|---|---|
| F-DE-Barrel-1 | None | Marginal lift Tier 3 #16, #17, #18 | None | None (adds concrete; doesn't conflict with chiseling) |
| F-DE-Barrel-2 | None (Sandel examples are common-knowledge) | Marginal lift Tier 1 #1, #2 + Tier 3 #16, #18 | Possible lift A4 (Sandel is well-known on conservative-philosophy register) | None |
| F-DE-Barrel-3 | None | **Resolves Pass 3.3 light flag #2** (§IV ¶4 entry-point skim-read); marginal lift Tier 1 #3 | None (A4 defense unchanged) | None ("That is Rawls applied across time" is NOT throat-clearing; it's a back-reference scene-bridge) |
| F-DE-Barrel-4 | None | Marginal lift Tier 3 readers | None | **Possible** (added 3-example sentence is rule-of-three; alternative 2-example version avoids this concern) |
| F-DE-Barrel-5 | None (Nordhaus position is well-documented) | Marginal lift Tier 1 #3 (Nordhaus methodologically credited) | Marginal lift A5 orthodox-econ reader | None |
| F-DE-Barrel-6 | None | Trade-off: Tier 1 #1 may prefer texture variance; Tier 3 #16 may prefer parallel | None | **Inverse-polarity-adjacent** (Pass 3.5 polarity is restoration but this finding reduces parallel; defensible if framed as texture-variance restoration rather than chiseling) |

### 3.5 Pass 3.4 robustness re-verification carry-forward

Per v3.1 doctrine + Pass 3.2 §3.5 cross-pass impact methodology: after Pass 3.5 Phase C application, **Pass 3.4 light re-fire is NOT routinely warranted** (restorations strengthen rather than weaken adversarial robustness; the comparative draft audit memo explicitly notes this for Pass 3.5 carry-forward). However, if F-DE-Barrel-5 (Nordhaus symmetric framing) is applied, a brief A5-specific re-verification confirms the orthodox-econ engagement is strengthened, not weakened.

### 3.6 Pass 3.3 light re-fire carry-forward

Per Pass 3.5 doctrine: **Pass 3.3 light re-fire recommended after Phase C application of ratified Pass 3.5 spot-fixes**. The re-fire would confirm:
- F-DE-Barrel-3 resolves the §IV ¶4 entry-point flag (Pass 3.3 light's audit-trail flag #2)
- F-DE-Barrel-1 + F-DE-Barrel-2 add Tier 3 marginal lift without shifting Tier 1 verdicts
- F-DE-Barrel-5 (if applied) marginally lifts Tier 1 #3 (Condition 1 symmetric framing)
- Overall PASS verdict unchanged (still 18 INCLUDE; 0 ⚠ flags)

### 3.7 Submission-readiness verdict

**Submission-ready after Phase C application of ratified Pass 3.5 spot-fixes + Pass 3.3 light re-fire (light) + Stage 4 render + character-integrity audit + Stage 5 bookend sign-off + pre-publication review queue.**

No Pass 3.5 finding is submission-blocking. The MEDIUM findings strengthen the essay (anchor restoration polarity); the LOW findings are sharpening options.

---

## 4. Methodology notes

### 4.1 Restoration polarity discipline observed

Per pipeline doctrine §3.6.3 and v3.1 Amendment B 2026-05-18: Pass 3.5 polarity is **restoration (adds back richness, scenes, sensory detail)**, not chiseling. All 6 findings are restoration-type:

- F-DE-Barrel-1: adds 3-figure scene-anchor to §II abstraction → +24w
- F-DE-Barrel-2: adds Sandel-example anchor to §IV Sandel-paragraph abstraction → +28w
- F-DE-Barrel-3: adds 5-word scene-bridge transitional sentence to §IV ¶4 opening → +5w
- F-DE-Barrel-4: adds throughput-example concrete-anchor to Daly paragraph → +29w
- F-DE-Barrel-5: adds Nordhaus methodological-position framing to §V Nordhaus paragraph → +21w
- F-DE-Barrel-6: texture-variance restoration to §Close rule-of-six (this finding is on the polarity boundary — varies verbs across the parallel structure; technically reduces parallel-cadence by -8w but reads as texture-restoration not chiseling)

Net word-count delta: +99w if all applied (restoration polarity preserved). Net +57w to +78w if author selects MEDIUMs + selective LOWs.

### 4.2 Ch 1 empirical-anchor calibration check

Ch 1 developmental-edit review (2026-05-18, the empirical anchor that drove v3.1 Amendment B) found 3 HIGH + 7 MEDIUM + 3 LOW = 13 findings on a ~9,000w chapter (~1 finding per 690w).

This Pass 3.5 found 0 HIGH + 3 MEDIUM + 3 LOW = 6 findings on a 4,145w essay (~1 finding per 691w). Density matches the empirical anchor almost exactly.

The absence of HIGH findings is consistent with:
- The essay has been through more pre-publication discipline than Ch 1 had at the empirical-anchor stage (Stage 1 brief + comparative draft audit + Pass 3.1 + Pass 3.2 + Pass 3.3 light + Pass 3.4 light).
- The essay is structurally simpler than a chapter (single argument arc vs. multi-section book chapter).
- Pass 3.2 chiseling was disciplined enough that flatness-residue is minimal.

### 4.3 Polarity-conflict-with-Pass-3.2 check

Per pipeline doctrine §3.6.2: Pass 3.5 restoration should not conflict with Pass 3.2 chiseling. The two passes operate at different polarities and should be complementary, not contradictory.

Two findings have minor polarity-conflict concerns:
- F-DE-Barrel-4 proposed correction includes a rule-of-three; alternative 2-example version avoids this.
- F-DE-Barrel-6 reduces parallel-cadence (technically chiseling polarity); framed as texture-variance restoration, defensible.

All other findings (F-DE-Barrel-1, -2, -3, -5) are pure restoration without polarity conflict.

### 4.4 Cross-pass-impact discipline

Per pipeline doctrine: Pass 3.5 should not introduce findings that worsen Pass 3.1 fact-check, Pass 3.3 acceptance, or Pass 3.4 robustness verdicts. All 6 findings tested:
- F-DE-Barrel-1, -2, -3, -5: marginal lifts across Pass 3.3 / Pass 3.4 verdicts; no degradation.
- F-DE-Barrel-4: marginal Tier 3 lift; no degradation.
- F-DE-Barrel-6: trade-off between Tier 1 #1 (texture variance) and Tier 3 #16 (scannable parallel); not a clean lift, but no degradation.

---

## 5. Hand-off to author + Phase C application session

**Author actions required:**

1. **Ratify findings.** Review F-DE-Barrel-1 through F-DE-Barrel-6. For each finding, decide: (a) apply proposed correction; (b) apply alternative correction (where offered); (c) modify; (d) hold/reject. Per v3.1 Amendment C Interactive Ratification Protocol, ratification + application combine in one session.

2. **Phase C application session.** Recommended order: Phase C-α (MEDIUMs: F-DE-Barrel-3 first per Pass 3.3 light flag resolution priority, then F-DE-Barrel-1, then F-DE-Barrel-2). Phase C-β (LOWs per author disposition): F-DE-Barrel-5, F-DE-Barrel-4, F-DE-Barrel-6.

3. **After Phase C application:**
   - Pass 3.3 acceptance light re-fire (recommended per §3.6) — confirms restorations don't shift verdicts and addresses Pass 3.3 light's flag #2 if F-DE-Barrel-3 applied
   - Pass 3.4 robustness light re-fire (NOT routinely warranted per §3.5; only if F-DE-Barrel-5 applied)
   - Stage 4 render + character-integrity audit (user handling offline per session direction)
   - Stage 5 academic-rigor + prose-quality sign-off bookend + pre-publication review queue

**Submission-window coordination:** Target submission 2026-06-01 to 2026-06-08. Remaining sessions: Pass 3.5 Phase C (1 session) + Pass 3.3 light re-fire (1 session, optional) + Stage 5 (1 session) = 2–3 sessions. Within window.

---

## 6. Hard-constraints adherence verification

- [x] No spot-fixes applied to the essay file. PROPOSED artifact only.
- [x] No named subjects contacted.
- [x] Comparative draft audit + Pass 3.1 + Pass 3.2 + Pass 3.3 light + Pass 3.4 light verdicts cross-referenced; no Pass-3.5 finding contradicts prior-pass canonical verdicts.
- [x] Per-finding format: F-DE-Barrel-K + severity + location + verbatim text + finding + proposed correction (and alternatives where applicable) + cross-pass impact.
- [x] Polarity discipline observed: restoration (adds back), not chiseling. Boundary cases (F-DE-Barrel-4, F-DE-Barrel-6) explicitly flagged.
- [x] Condition 1 disarming protection preserved (F-DE-Barrel-3 directly addresses Pass 3.3 light's §IV ¶4 entry-point flag; F-DE-Barrel-5 marginally strengthens Tier 1 #3 symmetric framing).
- [x] Locked elements preserved verbatim (title; §I opener device; §VI ¶7 architecture-fix-not-revolution register-anchor; §V ¶7 dispositive Stern-Nordhaus axis-exit second cadence). No Pass 3.5 finding modifies any locked element.
- [x] v3.1 five-pass discipline acknowledged; Pass 3.5 fires AFTER Pass 3.2 + Pass 3.3 + Pass 3.4 per per-prompt serial cadence + pipeline doctrine §3.6.3.
- [x] Whole-essay synthesis §: cumulative diagnosis + recommended Phase C application order + cross-pass impact table + Pass 3.3 + Pass 3.4 re-fire guidance.
- [x] Empirical-anchor calibration check against Ch 1 developmental-edit (2026-05-18; finding-density matches almost exactly).

---

## 7. Cross-references

- **Pass 3.4 robustness light (prior pass):** [`commons_bonds_rigor_pass_2026-05-23_100_barrel_essay_pass_3_4_audience_load_robustness_light_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-23_100_barrel_essay_pass_3_4_audience_load_robustness_light_v1.0.0.md) — RATIFIED 2026-05-23.
- **Pass 3.3 acceptance light (prior pass):** [`commons_bonds_rigor_pass_2026-05-23_100_barrel_essay_pass_3_3_audience_load_acceptance_light_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-23_100_barrel_essay_pass_3_3_audience_load_acceptance_light_v1.0.0.md) — RATIFIED 2026-05-23. **F-DE-Barrel-3 addresses Pass 3.3 light flag #2** (§IV ¶4 entry-point skim-read concern).
- **Pass 3.2 voice-polish:** [`commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_pass_2_voice_polish_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_pass_2_voice_polish_v1.0.0.md) — RATIFIED + APPLIED 2026-05-23 (commit `8b2614a`).
- **Pass 3.1 fact-check:** [`commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_pass_1_factcheck_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_pass_1_factcheck_v1.0.0.md) — RATIFIED + APPLIED 2026-05-21 (commit `cf5db97`).
- **Comparative draft audit:** [`commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_stage3_comparative_draft_audit_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_stage3_comparative_draft_audit_v1.0.0.md).
- **Stage 1 brief:** [`commons_bonds_rigor_pass_2026-05-19_100_barrel_essay_pre_draft_audience_structure_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-19_100_barrel_essay_pre_draft_audience_structure_v1.0.0.md) §4 structural decisions + §7 canonical facts.
- **v3.1 Amendment B (restoration polarity discipline):** [`tools/memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md).
- **Pipeline doctrine (Pass 3.5 spec):** [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md) §3.6.2 + §3.6.3.
- **Ch 1 developmental-edit empirical anchor (2026-05-18):** drives v3.1 Amendment B; finding-density calibration source.
- **Audit target:** [`manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md`](../../manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md) (4,145w; on `main` commit `63e149a`).

---

## 8. Ratification record

**2026-05-23 — PROPOSED.** Pass 3.5 developmental-edit (restoration polarity) artifact for $100 Barrel Draft A (post-Pass-3.1-Phase-C, post-Pass-3.2-Phase-C, post-Pass-3.3-light-RATIFIED, post-Pass-3.4-light-RATIFIED). 0 HIGH + 3 MEDIUM + 3 LOW = 6 findings. All findings are restoration-type per Pass 3.5 polarity discipline.

~~Awaiting author ratification of:~~ ALL FINDINGS RATIFIED + APPLIED 2026-05-24 per Amendment A (see top of artifact). Original finding-by-finding ratification queue (preserved below for audit-trail completeness) is closed.

1. ✅ **F-DE-Barrel-1 disposition** — APPLIED 2026-05-24 as Option A (3-figure scene-anchor).
2. ✅ **F-DE-Barrel-2 disposition** — APPLIED 2026-05-24 as Option A (Sandel signature-example anchor).
3. ✅ **F-DE-Barrel-3 disposition** — APPLIED 2026-05-24 as Option A ("That is Rawls applied across time."). Resolves Pass 3.3 light flag #2.
4. ✅ **F-DE-Barrel-4 disposition** — APPLIED 2026-05-24 as **Option B** (author selected over Pass 3.5's Option A recommendation; 2-example + analytical-close version avoids rule-of-three concern + the analytical close generalizes examples up to principle).
5. ✅ **F-DE-Barrel-5 disposition** — APPLIED 2026-05-24 as Option A as recommended.
6. ✅ **F-DE-Barrel-6 disposition** — APPLIED 2026-05-24 as Option A as recommended (verb texture variance).
7. ✅ **Phase C application session** — completed in same session as ratification per v3.1 Amendment C Interactive Ratification Protocol. Single commit per atomic Phase C standard.

**Amendment A 2026-05-24 ratification + application record:**
- Pass 3.5 PROPOSED → **Pass 3.5 RATIFIED + APPLIED (Amendment A applied)**.
- All 6 findings ratified + applied in single interactive Phase C session.
- One departure from Pass 3.5's original recommendation logged transparently: F-DE-Barrel-4 (Option B author-selected over recommended Option A).
- Per-finding dispositions logged in Amendment A table at top of artifact.
- Body word count: 4,145w (post-Pass-3.2-Phase-C) → 4,248w (post-Pass-3.5-Phase-C). Within Stage 1 brief §10 window.
- Next session: per author direction, Pass 3.3 light re-fire recommended but optional; user handling Stage 4 (render + character-integrity audit) offline; Stage 5 sign-off bookend + pre-publication review queue queued after Stage 4 completion.

**Hard-constraints adherence:**
- [x] No spot-fixes applied to the essay file in this session.
- [x] Comparative audit + Pass 3.1 + Pass 3.2 + Pass 3.3 + Pass 3.4 verdicts cross-referenced.
- [x] Restoration polarity observed for all 6 findings.
- [x] Condition 1 disarming protection preserved (F-DE-Barrel-3 strengthens; F-DE-Barrel-5 strengthens; no other finding weakens).
- [x] Locked elements preserved verbatim (no Pass 3.5 finding modifies any locked element).
- [x] v3.1 per-prompt serial cadence preserved (Pass 3.5 fires after Pass 3.4 RATIFIED).
- [x] No named subjects contacted (audit pass only).
- [x] Empirical-anchor calibration verified (Ch 1 finding-density matches; finding count proportional to essay/chapter length ratio).
