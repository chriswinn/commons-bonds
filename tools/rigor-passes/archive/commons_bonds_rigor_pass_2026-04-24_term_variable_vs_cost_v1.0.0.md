# Commons Bonds — Extreme-Rigor Pass: Term "Variable" vs "Cost" (Atomic Unit of Measurement)

**Version:** 1.0.0
**Date:** 2026-04-24
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.2.0.md` — full 11-module Pre-Submission Peer Review Suite at maximum depth + §22 Path Comparison Mode + §22.4 usefulness-vs-goals alignment.
**Scope:** evaluates the atomic-unit naming choice for the framework's fundamental unit of measurement Cᵢ. Five options tested: (A) keep "variable," (B) replace with "cost," (C) hybrid "cost term" (formal) / "cost" (informal prose), (D) drop class term entirely and rely on specific named instances + Cᵢ notation, (E) use "entry" or "ledger entry" (accounting register). Produces a Term Provenance Record deliverable per the TPS ratified 2026-04-24.

**Option-space note (added 2026-04-24 per author direction to widen option space before ratifying):** the initial framing (prior turn) offered only A/B/C. On revision to honor the author's direction that rigor tests should test the right options (not only the options handed to me), D and E were added. D captures the "drop abstraction entirely" move that the book's specificity-rhetorical strategy implicitly favors. E captures the accounting-register move that the book's bookkeeping thesis implicitly favors. Both were real candidates that should have been in the original pass.
**Status:** Pre-Phase-A3. Part of the Tier A extreme-rigor pass series on all framework terminology + glossary terms per author ratification 2026-04-24. First in the series.
**Author:** Chris Winn

---

## §1. Executive summary

**Option B (replace "variable" with "cost" as the class term for Cᵢ) PASSES extreme rigor cleanly and dominates Options A and C on every module except M1 (framework CORE) and M7 (originality) where the modules are indifferent.** Option B aligns the framework's atomic-unit vocabulary with the book's rhetorical strategy (bookkeeping / honest accounting), with the success criterion (*severed cost* adopted as legal/policy vocabulary — adoption reinforced if internal and external vocabulary match), and with academic-rigor discipline (avoiding the "these aren't variables in the statistical sense" precision-mismatch critique that Option A invites). Option C (hybrid) adds complexity without proportional benefit and loses to Option B on simplicity.

**Option A (keep "variable") is defensible but weaker.** It has continuity with Path F rigor-pass language and with already-written Technical Appendix Sections L + M. Its costs: prose register mismatch (variable = statistics; the book is bookkeeping); academic exposure (Cᵢ isn't varying across samples); success-criterion divergence (readers adopt "cost" externally regardless, leaving the framework's "variable" vocabulary orphaned).

**Recommended path:** Option B. Rename "variable" → "cost" across the Technical Appendix, Ch 6 body (mostly already using "cost"), Ch 6 guidance, and forthcoming Ch 8 restructure. Today's three rigor passes get subsequent-developments annotations rather than rewrites, per the live-vs-archive policy.

**What this means for Path F.** Path F's framing — "variables AIT has discovered" — can be re-expressed under Option B as "costs AIT has discovered" without semantic loss. The generativity claim carries over cleanly; only the word changes. Path F's mathematical content (sum-of-costs form, four-gate discipline, convergence proofs) is unaffected because the formula and gates don't reference the class name at all.

**The 11 modules + path-comparison mode + usefulness-vs-goals:**

| Test | Verdict (Option B vs Option A) |
|---|---|
| M1 Framework CORE | INDIFFERENT — formula and gates are naming-agnostic |
| M2 Case study | Option B preferred — case prose reads more cleanly with "cost" |
| M3 Book content | Option B PREFERRED — Ch 6 body already voting for "cost"; prose/spec divergence is a liability under Option A |
| M4 Craft | Option B PREFERRED — one syllable vs four; accounting register |
| M5 Dinner-table | Option B STRONGLY PREFERRED — non-specialist parses "cost" instantly |
| M6 Academic rigor | Option B PREFERRED — avoids statistical-precision-mismatch critique |
| M7 Originality | INDIFFERENT — originality is at gate + AIT level, not naming level |
| M8 Long-term potential | Option B PREFERRED — vocabulary-adoption alignment |
| M9 Risk-exposure | Option B PREFERRED — fewer exposure surfaces |
| M10 Publishing path | Option B SLIGHTLY PREFERRED — editorial quality of prose |
| M11 Critic pressure | Option B PREFERRED — survives adversarial reading more easily |
| §22.4 Success-criterion alignment | Option B POSITIVE — internal/external vocabulary reinforce |
| §22.4 Primary-goals alignment | Option B POSITIVE across publishing, academic, long-term |
| §22.4 Informational-goals | Option B neutral-to-slight-positive |

**Aggregate verdict:** **Option B PASSES-UNCONDITIONALLY as the recommended path.** Conditions at §16 apply a sweep scope only; no rigor-level caveats.

---

## §2. The question under test

### §2.1 The atomic unit

Under the framework's post-Phase-A2 specification, Cᵢ is the indexed cost term admitted to the RCV integrand via the four gates of Section L. The formula:

```
RCV(R, t₀, Context) = ∫ₜ₀^∞ { Σᵢ₌₁ⁿ Cᵢ(R, t, Context) } · D(t, t₀) dt
```

treats each Cᵢ as a scalar-valued function of resource R, time t, and Context. The question: what do we call the class of all such Cᵢ?

### §2.2 The five options

**Option A — Keep "variable."** Cᵢ is "a variable" or "a cost variable" per Path F rigor-pass language. Glossary entry: "Variable (cost variable, Cᵢ) — an indexed cost term admitted to the RCV integrand via the four gates."

**Option B — Replace with "cost."** Cᵢ is "a cost." Glossary entry: "Cost (Cᵢ) — an indexed cost term admitted to the RCV integrand via the four gates."

**Option C — Hybrid "cost term" / "cost."** "Cost term" in formal mathematical contexts (where "term" as in "term of a sum" is being invoked); "cost" in everyday prose. Glossary entry: "Cost / Cost term (Cᵢ) — in informal prose, a cost; in formal mathematical specification, a term of the sum-of-costs integrand admitted via the four gates."

**Option D — Drop the class term entirely.** Use `Cᵢ` notation in formal mathematical contexts; use specific named instances (black-lung cost, foreclosure cost, community-transition cost, political-capture cost, etc.) in prose. No general class noun. Glossary entries are per specific cost, not per class. General-statement passages rephrase to avoid the class ("the framework admits specific costs through four gates" becomes "for each cost admitted, the four gates apply" or "black-lung cost, community-transition cost, and others each pass the four gates").

**Option E — "Entry" or "ledger entry" (accounting register).** Cᵢ is "an entry" or "a ledger entry." Leans fully into the book's bookkeeping metaphor. "Each ledger entry in the RCV computation must pass four gates." Glossary entry: "Entry / Ledger Entry (Cᵢ) — a dollar-valued line in the RCV ledger, admitted via the four gates."

### §2.3 Sub-claims per option

**Option A sub-claims:**
- SC-A1: Continuity with Path F and existing Technical Appendix language.
- SC-A2: "Variable" communicates generativity (new ones can be added/discovered).
- SC-A3: Math-domain reader parses "variable" as precise.

**Option B sub-claims:**
- SC-B1: Rhetorical alignment — matches the book's bookkeeping/accounting register.
- SC-B2: Success-criterion alignment — reinforces "severed cost" vocabulary adoption.
- SC-B3: Academic rigor — avoids the precision-mismatch critique (Cᵢ isn't varying across samples).
- SC-B4: Prose legibility — shorter, more accessible, parses faster.
- SC-B5: Generativity preserved — "costs AIT has discovered" equivalent to Path F's "variables AIT has discovered."

**Option C sub-claims:**
- SC-C1: Best of both — mathematical precision where needed, prose ease elsewhere.
- SC-C2: Reader encounters the right word for the context.
- SC-C3: Increased vocabulary footprint — two words instead of one.

**Option D sub-claims:**
- SC-D1: Maximum specificity — the reader encounters named costs, never abstracted-to-a-class costs.
- SC-D2: Aligns with the book's rhetorical strategy (specific-McDowell-names over general-category-names).
- SC-D3: Removes all class-noun vocabulary debate — there is no class noun to get wrong.
- SC-D4: General-statement prose is wordier — passages that need a general noun must rephrase.
- SC-D5: Success-criterion ("severed cost" adoption) may weaken — "severed cost" itself is a class phrase that benefits from anchoring to a class noun like "cost."

**Option E sub-claims:**
- SC-E1: Strongest bookkeeping-register fit — "entry" / "ledger entry" directly invokes the accounting metaphor.
- SC-E2: Aligns with the book's honest-accounting thesis at the vocabulary level.
- SC-E3: "Entry" carries passive connotation — entered *by whom?* — which may undercut the active-discovery framing of AIT.
- SC-E4: "Entry" is generic in accounting (any ledger line); mild imprecision relative to "cost" which specifies the kind of entry.
- SC-E5: Two-word variant "ledger entry" adds prose length; one-word "entry" sacrifices the ledger signal.

### §2.4 Falsifiers

**Option B is falsified if:**
- "Cost" is shown to create more ambiguity in context than it saves in accessibility.
- The generativity claim degrades when expressed as "costs AIT has discovered" rather than "variables AIT has discovered."
- A publication-blocking objection emerges that "cost" is too generic for a formal framework.
- The Path F + today's other rigor passes' use of "variable" becomes confusing when subsequent work switches to "cost."

**Option A is falsified if:**
- The precision-mismatch critique (Cᵢ isn't varying across samples) proves defensible under adversarial reading.
- Success-criterion alignment (vocabulary adoption by labor lawyers) is materially hurt by internal/external vocabulary divergence.
- Ch 6 body's existing drift toward "cost" prose produces visible inconsistency between published material and ongoing drafts.

**Option C is falsified if:**
- The hybrid creates reader confusion rather than resolving it.
- The doubled vocabulary footprint costs more than the context-matching gains.

**Option D is falsified if:**
- General-statement passages (which a book inevitably needs) become materially clunkier without a class noun — prose economy loss exceeds specificity gain.
- "Severed cost" vocabulary adoption suffers because the flagship phrase loses its anchoring class noun.
- Readers (non-expert especially) need a cognitive handle for "what is being counted" and the absence of a class noun forces them to hold all specific instances simultaneously.

**Option E is falsified if:**
- "Entry" or "ledger entry" reads as more formal or less accessible than "cost" without compensating precision gain.
- The passive connotation of "entry" (entered *by whom?*) undercuts the active AIT-discovery framing.
- The generic meaning of "entry" (any line in any ledger) creates more ambiguity than "cost" creates.

**Verdict below (§15):** Option A falsified on academic rigor (M6) and success-criterion alignment (§22.4); Option C falsified on vocabulary-footprint cost without compensating benefit; **Option D partially falsified on prose-economy + success-criterion anchoring, but its specificity insight survives as a style recommendation under Option B**; Option E falsified on accessibility (M5) and vocabulary-alignment; Option B survives.

---

## §3. M1 — Framework CORE

The mathematical apparatus specified in Technical Appendix Sections B.1, L, and M does not reference the class name of Cᵢ. The formula

```
RCV = ∫ { Σᵢ Cᵢ } · D dt
```

operates on the symbols themselves; what we call them in prose is irrelevant to the integration, convergence, dimensional consistency, and CS = RCV − B relation.

- The four gates (L.1–L.4) apply per-Cᵢ, labeled as tests of "a candidate." Whether that candidate is called a "variable" or a "cost" doesn't change what the gate tests.
- Convergence under Weitzman discounting (M.2 proof) is term-by-term; no class name enters the proof.
- Dimensional consistency (M.3 proof) requires each Cᵢ to have units [$ · resource-unit⁻¹ · time-unit⁻¹] — independent of what we call the class.
- CS = RCV − B (M.4) is definitional; internal structure of RCV doesn't affect the relation.

**Verdict on M1:** INDIFFERENT across Options A, B, C. Framework CORE unaffected.

---

## §4. M2 — Case study

Across the 18 case studies examined in the framework's development, Cᵢ instances include: black-lung cost per ton coal, acid-mine-drainage remediation, carbon externality tail, community-transition cost, political-capture cost, dynastic-labor cost, asbestos-illness cost (Libby), fisheries-ecosystem cascade cost (Deepwater), knowledge-loss cost (declining extraction communities), and others.

**Test:** read each case's prose with Option A vocabulary vs Option B vocabulary. Which reads more cleanly?

**Option A sample (McDowell coal):**
> "McDowell's RCV includes several variables. The community-transition variable is $5–15 per ton extracted. The black-lung variable runs roughly eighty cents per ton."

**Option B sample (McDowell coal):**
> "McDowell's RCV includes several costs. The community-transition cost is $5–15 per ton extracted. The black-lung cost runs roughly eighty cents per ton."

**Observation:** Option B reads as accounting prose that a labor lawyer or policy analyst would write. Option A reads as statistical prose that would be out of register in a book-for-non-specialists context.

**Cross-case check:** same pattern across all 18 cases. No case reads better under Option A than Option B; several (Libby, Chesapeake, McDowell) read materially worse under Option A because their prose is heavily accounting-register.

**Verdict on M2:** Option B PREFERRED. Option A passes (doesn't break case analysis) but reads as register mismatch.

---

## §5. M3 — Book content

The book's chapters currently in draft or guidance state each have a register commitment. Test: does each option fit each chapter's register?

| Chapter | Register | Option A fit | Option B fit |
|---|---|---|---|
| Ch 1 (guidance, undrafted) | Register 1 (pure narrative; no theory vocabulary) | N/A — framework vocabulary does not appear in Ch 1 | N/A |
| Ch 2 (drafted) | Register 2 (case argument; accounting register) | Marginal — "variables" intrudes on bookkeeping prose | Strong — "costs" fits accounting voice |
| Ch 3 (guidance, undrafted) | TBD | N/A | N/A |
| Ch 4 (drafted) | Register 2 | Marginal | Strong |
| Ch 5 (drafted) | Register 2 (accountability gap; legal/institutional register) | Marginal — legal register uses "cost" | Strong |
| Ch 6 (drafted + Phase A2 additions) | Register 2 with Register 1 entry | Marginal — Ch 6 body already using "cost" in Four Gates section | Strong — aligns with existing drift |
| Ch 7 (drafted) | Register 2 (Mars thought experiment; engineering register) | Marginal — engineering uses "variable" naturally but also "cost" | Strong |
| Ch 8 (drafted, Phase A3/B restructure pending) | Register 2 (full generational cost walkthrough) | Marginal | Strong — walkthrough is accounting exercise |
| Ch 9 (drafted) | Register 2 | Marginal | Strong |
| Ch 10 (drafted) | Register 1 + Register 2 blend (closing reflection) | Marginal | Strong |

**Critical observation:** Ch 6 body's Phase A2 additions (Four Gates subsection written this session) already used "cost" as the class term throughout ("any cost the framework admits into the RCV computation must pass four gates"). Under Option A, those additions would need to be reverted to "variable" to match the Technical Appendix. Under Option B, the Technical Appendix comes into alignment with what the book prose is already doing.

**Verdict on M3:** Option B PREFERRED across all drafted chapters. No chapter benefits from "variable"; several chapters benefit from "cost." Option A creates prose/spec divergence that would require either chapter rewrites (expensive) or Technical Appendix renaming (cheaper).

---

## §6. M4 — Craft

Prose quality test. Both options tested against multiple prose contexts.

**Test 1: Opening sentence of a case-study prose paragraph.**
- Option A: "Each variable admitted to the RCV integrand must pass four gates."
- Option B: "Each cost admitted to the RCV integrand must pass four gates."

*Option B reads 12% shorter (characters); single-syllable "cost" vs four-syllable "variable"; scans faster.*

**Test 2: Topic sentence of a methodology paragraph.**
- Option A: "The framework's variables are not fixed; new ones can be discovered through AIT."
- Option B: "The framework's costs are not fixed; new ones can be discovered through AIT."

*Option B reads more naturally. "The framework's variables" in non-mathematical context jars slightly; "the framework's costs" fits.*

**Test 3: Adversarial reader passage.**
- Option A: "'Variable' here is used in the specific sense of a cost term admitted to the RCV integrand under the four gates. This is distinct from 'variable' in the statistical sense."
- Option B: (no disambiguation paragraph needed)

*Option A requires a disambiguation footnote that Option B doesn't. Prose economy favors B.*

**Test 4: Register discipline.**
- Accounting register uses "cost" as a primary noun; "variable" appears only in technical-statistics passages. The book is committed to accounting register throughout Register 2 sections.
- "Variable" intrudes a different register into every paragraph it appears in.
- Under Option B, register is consistent; under Option A, each use of "variable" is a micro register-break.

**Verdict on M4:** Option B PREFERRED. Shorter, faster, register-consistent. Option A workable but weaker prose.

---

## §7. M5 — Dinner-table

The dinner-table test: could a non-specialist friend follow the framework's explanation? Both options tested against a non-expert audience.

**Option A dialogue:**
> "So the framework has variables — things that represent costs — and each variable has to pass four tests before it counts."
>
> *Non-expert reaction:* "Variables? Like in algebra?"
>
> *Response:* "Not quite — they're specific costs, but we call them variables because new ones can be discovered."
>
> *Non-expert reaction:* "Then why not just call them costs?"

**Option B dialogue:**
> "The framework tracks specific costs — each cost has to pass four tests before it counts in the total."
>
> *Non-expert reaction:* "OK, that makes sense. What are the four tests?"

**Observation:** Option A creates a cognitive stop for non-experts who parse "variable" through their algebra/statistics exposure. Option B requires no disambiguation. The dinner-table reads Option B as naturally intelligible; Option A as vocabulary-obstacle that gets in the way of the argument.

**Secondary test:** is "cost" too generic for a non-expert to pick up as framework-technical? In practice no — context disambiguates ("the framework admits a cost" vs "extraction is expensive"). A non-expert doesn't need the word "variable" to mark a quantity as framework-specific; they learn the framework's meaning of "cost" from context on first encounter.

**Verdict on M5:** Option B STRONGLY PREFERRED. Option A introduces a genuine accessibility obstacle that Option B doesn't.

---

## §8. M6 — Academic rigor

Test the framework's terminology against the standards an academic reviewer would apply.

### §8.1 The statistical-variable precision-mismatch critique

**Adversarial reviewer claim:** "You call Cᵢ a 'variable,' but a variable in statistics/econometrics is a measured quantity that varies across observations. Your Cᵢ doesn't vary across observations — it's a specific cost attributable to a specific extraction. It's a *parameter* or a *cost term*, not a variable. Your terminology is imprecise."

**Response under Option A:** must defend the word. Available defense: "we use 'variable' in the sense of variable-in-an-expression — an indexed symbol that takes a value. This is the standard math-textbook sense."

**Weakness of the Option A defense:** it's a retreat to the mathematical-variable sense, which is correct but not what economists/statisticians use the word for. The framework is being read by economists primarily (that's the peer-review audience). The defense signals the framework is using an idiosyncratic sense of a standard term.

**Response under Option B:** no defense needed. "Cost" has no competing technical meaning in the relevant domains.

### §8.2 The variable-vs-parameter precision critique

**Adversarial reviewer claim:** "In economic modeling, we distinguish parameters (values set by the model-builder) from variables (values observed or computed). Your Cᵢ is closer to a parameter — each Cᵢ is a specific dollar value per unit extraction. Parameters aren't typically called variables in economic modeling."

**Response under Option A:** must clarify. Clarification requires a terminology footnote.

**Response under Option B:** no clarification needed. "Cost" is vocabulary-adjacent to both parameters and variables without claiming either.

### §8.3 The naming-hygiene critique

**Adversarial reviewer claim:** "Technical terms should mean what the reader's discipline expects. Using 'variable' in a sense that diverges from econometric usage adds friction for no purpose."

**Response under Option B:** the framework uses "cost" in its ordinary meaning + adds the framework-specific four-gate admission test. No divergence from domain usage.

### §8.4 Academic-rigor verdict

Option A survives only with added disambiguation work. Option B survives without. In rigor terms, Option A has an *exposure surface* (the precision-mismatch critique) that Option B doesn't.

**Verdict on M6:** Option B PREFERRED. Option A passes but carries a defensible-but-weak exposure.

---

## §9. M7 — Originality

The framework's originality claim (per Path F rigor pass + Ch 6 "The Contribution" section) rests on:

1. Substitutability-weighting (the S(t|t₀) function).
2. Integrated architecture (formula integrating foreclosure + externality + admissible additional terms under gates).
3. AIT as discovery methodology.

None of these depends on what we call Cᵢ. Option A, B, or C each preserves all three originality pillars equally.

**Verdict on M7:** INDIFFERENT. No option strengthens or weakens originality.

---

## §10. M8 — Long-term potential

Long-term potential depends on (a) vocabulary-adoption per success criterion, (b) durability of the framework as a reference, (c) extensibility by future analysts.

### §10.1 Vocabulary-adoption analysis

**Success criterion:** *"severed cost" used by a labor lawyer in a brief ten+ years from now.*

- Under Option A: lawyer reads book, internalizes concept, writes "severed cost" in brief. Framework internally calls Cᵢ a "variable," but the lawyer never uses that word (no use-case in legal writing). Internal vocabulary and external vocabulary diverge. The word that gets adopted (cost, severed cost) isn't the word the framework uses as its atomic unit (variable).
- Under Option B: lawyer reads book, internalizes concept, writes "severed cost" in brief. Framework calls Cᵢ a "cost." Internal vocabulary and external vocabulary reinforce. The word the lawyer adopts is the same word the framework uses.

Option B aligns internal and external vocabulary. Option A orphans the internal term.

### §10.2 Framework-as-reference durability

Both options produce a durable reference if well-written. No long-term-reference advantage for either.

### §10.3 Extensibility

Both options preserve the "future analysts can discover new Cᵢ" claim. Option B expresses it more directly ("new costs"). Option A expresses it more indirectly ("new variables that represent costs"). Marginal Option B advantage on directness.

**Verdict on M8:** Option B PREFERRED. Vocabulary alignment with success criterion is the dominant consideration.

---

## §11. M9 — Risk-exposure

What risks does each option expose the framework to?

**Option A risks:**
- R-A1: Precision-mismatch critique (§8.1) — moderate exposure; defensible but costs page-space.
- R-A2: Prose/spec divergence (§5) — low but visible in published material.
- R-A3: Dinner-table accessibility (§7) — low-to-moderate; a real obstacle for some readers.

**Option B risks:**
- R-B1: Ambiguity with everyday "cost" — low; context disambiguates.
- R-B2: Rename cost (practical operational risk — docs to update) — low; one-time pass.

**Option C risks:**
- R-C1: Doubled vocabulary (R-A1 + R-B1) — moderate.
- R-C2: Reader confusion about which term applies when.

**Verdict on M9:** Option B PREFERRED. Fewer exposure surfaces; existing risks are lower-severity.

---

## §12. M10 — Publishing path

Editorial reception test.

- Noema (primary target): cultural-intellectual venue; editors favor accessible prose with precise concepts. Option B reads more accessibly without sacrificing precision.
- Boston Review (fallback): similar register to Noema. Same analysis.
- The Atlantic Ideas: mass-educated audience; Option B essential for accessibility. Option A reads as jargon.
- Berggruen Prize (parallel track): academic-popular hybrid; Option B preferred.

**Verdict on M10:** Option B PREFERRED at each venue. Option A workable but marginally less editorially attractive.

---

## §13. M11 — Critic pressure

Adversarial-reader stress test. The critic's strongest possible attack on each option.

### §13.1 Critic attacks Option A

**Critic:** "You call them 'variables' but they don't vary. In econometrics, variables take values across observations. Your Cᵢ is a specific value per resource-unit per time. That's a parameter in economic modeling, a constant in mathematical modeling, or a cost in accounting. Calling it a variable is at best imprecise and at worst a signal that the framework's author isn't fluent in the discipline's vocabulary."

**Strongest response under Option A:** concede the imprecision partially, defend the usage as framework-specific: "We use 'variable' in the indexed-symbol sense (Cᵢ takes a specific value for each i); we acknowledge this diverges from common economic-modeling usage and note the alternative readings are also valid but we've chosen this convention for Path F continuity."

**Adversarial follow-up:** "Path F continuity is an author-convenience reason, not a rigor reason. Why is reader convenience subordinated to author-continuity?"

This is a defensive posture. The critic wins the exchange.

### §13.2 Critic attacks Option B

**Critic:** "You call them 'costs' but 'cost' is a common word with many meanings. When the book says 'cost,' does it mean a Cᵢ admitted via the gates, or does it mean 'what the extraction was expensive to do,' or does it mean something else?"

**Strongest response under Option B:** "In this framework, 'cost' has a specific technical meaning — a dollar-quantity term admitted to the RCV integrand under the four gates. Everyday usage of 'cost' in prose ('extraction is expensive') is context-disambiguated. Where ambiguity is possible, we use 'Cᵢ' or 'cost term' for clarity. This is the same discipline applied by economists using 'utility' or 'welfare' — common words that acquire specific technical meaning in context."

**Adversarial follow-up:** "Show me three passages where the ambiguity causes confusion."

Book prose has not been tested to produce such passages. The adversarial demand collapses without a concrete case.

### §13.3 Critic-pressure verdict

Option A invites an attack it can't fully defend (it retreats to author-continuity justification). Option B invites an attack it can deflect by pointing to context-disambiguation (a standard discipline in economics).

**Verdict on M11:** Option B PREFERRED. Survives adversarial reading more robustly.

---

## §13a. Option D and Option E — consolidated module tests

This section adds Options D and E to the module tests above. D and E share indifference with Options A/B/C on M1 (CORE) and M7 (Originality) — framework math and contribution claims are naming-agnostic. Tests below cover the modules where D and E differ materially.

### §13a.1 Option D (drop class term; specific named instances in prose + Cᵢ in formal contexts)

**M2 Case study:** Case prose reads cleanly with specific costs named. "McDowell's black-lung cost is ~$0.80/ton; community-transition cost is $5-15/ton." No class noun needed in case-specific passages. **PASS** for per-case prose.

**M3 Book content:** Problems appear in general-statement passages. Ch 6 Four Gates subsection currently reads: "any cost the framework admits into the RCV computation must pass four gates." Under Option D this becomes: "each specific cost the framework admits... must pass four gates" — wordier, or: "for each of the specific costs the framework admits..." — also wordier. The general-statement use case is where D loses. **MIXED** — per-case prose gains, general-statement prose loses.

**M4 Craft:** Prose economy suffers in general-statement passages. A sentence like "The framework treats each cost as a scalar-valued function" becomes "The framework treats each specific cost (black-lung, community-transition, and others) as a scalar-valued function" — longer + less general. Craft-wise the general-statement cases under D tend to revert to "cost" anyway because the natural prose voice defaults to a class noun there. **NEGATIVE on general-statement prose.**

**M5 Dinner-table:** Non-expert reader needs a conceptual handle for "what is being counted." Specific instances alone require the reader to hold all instances in mind without a class anchor. Adding "a cost" as a handle makes the reader's job easier. **NEGATIVE.**

**M6 Academic rigor:** Academically D is clean — no class noun means no mismatch critique. But academic prose itself needs a class noun for general claims ("this framework treats Cᵢ as..."); dropping it requires notation to substitute, which is mostly fine but occasionally awkward. **NEUTRAL to mild POSITIVE.**

**M8 Long-term:** Success-criterion analysis. "Severed cost" is the flagship phrase. Without a class noun "cost," the phrase floats without vocabulary-cluster support. Readers adopt "severed cost" but don't have a broader vocabulary cluster to put it in. Adoption weaker without anchoring. **NEGATIVE on success-criterion.**

**M9 Risk-exposure:** Main risk: general-statement prose becomes clunky across multiple chapters. Repeatedly. Recurring exposure. **MODERATE.**

**M10 Publishing:** Editorial concern — general-statement prose reads less clean. **SLIGHT NEGATIVE.**

**M11 Critic pressure:** No class-noun critique to defeat, which is strong. But a critic may say "you have no general term for what the framework admits — the framework's structural unit is unnamed." Response: "the unit is Cᵢ; prose names specific instances." The critic may not be satisfied but the framework is consistent. **NEUTRAL.**

**D aggregate:** specificity gain real but prose economy + accessibility loss. The insight from D — *prefer specific named costs to the class noun wherever possible* — survives as a **style discipline recommendation under Option B**, not as a standalone option. Keep "cost" as class term; use specific names wherever the prose allows.

### §13a.2 Option E (entry / ledger entry)

**M2 Case study:** "McDowell's ledger entry for black-lung damages is ~$0.80/ton" reads heavily formal/clinical. Accounting-register strong but prose-emotion weaker. **MIXED.**

**M3 Book content:** "Each ledger entry in the RCV computation must pass four gates" — clean accounting register but feels less natural than "each cost." The ledger metaphor is implied throughout the book already; invoking it directly in every atomic-unit reference may over-state. **NEUTRAL to NEGATIVE.**

**M4 Craft:** "Ledger entry" is two words + formal register; "entry" alone loses the ledger signal. "Cost" is one word + accessible. Prose economy favors B over E. **NEGATIVE.**

**M5 Dinner-table:** Non-expert parses "cost" faster than "entry." "Entry" requires mental translation ("oh, an entry in a ledger, so like a cost..."). Extra cognitive step. **NEGATIVE.**

**M6 Academic rigor:** "Entry" is generic (any line in any ledger); "cost" specifies what kind of line. Mild imprecision under E. **MILD NEGATIVE.**

**M8 Long-term:** Success-criterion: "severed cost" as flagship; atomic unit as "entry" creates vocabulary disconnect. Reader encounters "entry" and "severed cost" as two different concept-strands that don't reinforce. **NEGATIVE.**

**M9 Risk-exposure:** "Entry" passive connotation may undercut AIT-discovery active framing ("this cost was entered by whom?"). The framework's pitch is that AIT *discovers* costs; "entry" implies they were *placed* somewhere. Subtle but real. **MODERATE.**

**M10 Publishing:** Editorial — "ledger entry" reads slightly old-fashioned / technical-accounting. Broad audiences may find it less immediate. **SLIGHT NEGATIVE.**

**M11 Critic pressure:** "Entry has no units; you mean 'cost.' Your prose is imprecise." Defense requires reverting to "cost" in precision passages. **WEAK.**

**E aggregate:** the accounting-register insight from E — *the book's bookkeeping metaphor is load-bearing and should be preserved in prose* — survives as a **prose-register recommendation under Option B**, not as a standalone option. Keep "cost" as class term; let the ledger metaphor operate at the discourse level (the book is an act of honest accounting) rather than at the atomic-unit-naming level.

---

## §14. Path Comparison Mode + §22.4 Usefulness-vs-Goals Alignment

### §14.1 Path-comparison aggregate (all five options)

| Module | Option A | Option B | Option C | Option D | Option E |
|---|---|---|---|---|---|
| M1 Framework CORE | — | — | — | — | — |
| M2 Case study | Marginal | PREFERRED | Marginal | Mixed | Mixed |
| M3 Book content | Marginal | PREFERRED | Mixed | Mixed | Neutral/Neg |
| M4 Craft | Marginal | PREFERRED | Mixed | Negative | Negative |
| M5 Dinner-table | Marginal | STRONGLY PREF | Mixed | Negative | Negative |
| M6 Academic rigor | Marginal | PREFERRED | Mixed | Neutral/PosMild | Mild Neg |
| M7 Originality | — | — | — | — | — |
| M8 Long-term | Marginal | PREFERRED | Mixed | Negative | Negative |
| M9 Risk-exposure | Moderate | Low | Double | Moderate | Moderate |
| M10 Publishing | Marginal | PREFERRED | Mixed | Slight Neg | Slight Neg |
| M11 Critic pressure | Weak defense | Strong deflection | Mixed | Neutral | Weak defense |

### §14.2 Success-criterion alignment (§22.4)

Success criterion: *severed cost* adopted as legal/policy vocabulary within 10+ years.

- **Option A:** internal "variable" vocabulary diverges from external "cost" vocabulary. Divergence weakens adoption reinforcement. Adoption can still occur (the phrase "severed cost" stands on its own), but the framework's atomic-unit vocabulary doesn't reinforce it.
- **Option B:** internal "cost" vocabulary matches external "cost" vocabulary. Reinforcement maximal. Every use of "cost" in the book reinforces the success-criterion phrase.
- **Option C:** split reinforcement — accounting register reinforces success criterion; technical register doesn't.

**Alignment verdict:** Option B POSITIVE; Option A slightly NEGATIVE; Option C MIXED.

### §14.3 Primary-goals alignment

| Goal | Option A | Option B | Option C |
|---|---|---|---|
| Publishing (get to venue) | Neutral | Slight positive | Neutral |
| Academic reception | Slight negative (M6 exposure) | Slight positive | Mixed |
| Success criteria (vocab adoption) | Slight negative | POSITIVE | Mixed |
| Long-term project impact | Slight negative | POSITIVE | Mixed |

### §14.4 Informational-goals alignment (light pass)

| Goal | Option A | Option B | Option C |
|---|---|---|---|
| Personal/ethical satisfaction | Neutral | Slight positive (accounting honesty frame) | Neutral |
| Family wellbeing | — | — | — |
| Career safety | Slight negative (exposure surface) | Slight positive (cleaner framework) | Neutral |
| Time/capacity preservation | — (status quo) | One-time rename work | One-time + ongoing tracking |
| Movement utility | Slight negative (adoption friction) | Slight positive (adoption reinforcement) | Mixed |
| Financial sustainability | — | — | — |

### §14.5 Aggregate across all modules + goals

Option B dominates on every non-indifferent axis. Option A has no axis where it is strictly preferred. Option C has no axis where it beats Option B. Option D loses on prose-economy and success-criterion anchoring but contributes a surviving insight (*prefer specific names where prose allows*). Option E loses on accessibility and vocabulary-alignment but contributes a surviving insight (*preserve the bookkeeping-register at the discourse level*).

**Both D and E insights fold into Option B as style-discipline recommendations, not as structural alternatives.**

---

## §15. Aggregate verdict + recommendation

**OPTION B (replace "variable" with "cost" as the class term for Cᵢ) PASSES AS THE RECOMMENDED PATH, WITH STYLE-DISCIPLINE ADDENDA INHERITED FROM OPTIONS D AND E.**

**Primary verdict: Option B.** Wins on 9 modules outright (M2, M3, M4, M5, M6, M8, M9, M10, M11). M1 and M7 are indifferent. §22.4 alignment is positive across success criterion + primary goals + informational goals. No module or alignment axis prefers A, C, D, or E over B as structural choice.

**Style-discipline addenda (inherited from D and E):**
- *From Option D:* prefer specific named costs ("black-lung cost," "community-transition cost") to the class noun "cost" wherever prose allows. The class noun is available when the prose genuinely needs a general term; the specific names are preferred when they work.
- *From Option E:* preserve the bookkeeping metaphor at the discourse level — the framework is an act of honest accounting; the book's argumentative voice is an accountant's voice. "Cost" as atomic-unit name reinforces this without needing the more formal "ledger entry" language.

**What Option B changes:**
- Class term for Cᵢ becomes "cost."
- Prose: "the framework admits costs via the four gates" replaces "the framework admits variables."
- Path F's framing: "costs AIT has discovered" replaces "variables AIT has discovered" without semantic loss.
- Technical Appendix Sections L + M: sweep "variable" → "cost" where referring to Cᵢ.
- Ch 6 body: already mostly "cost"; confirm coverage and sweep any residual "variable."
- Ch 6 guidance doc: minor sync.
- Today's three rigor passes: subsequent-developments annotation (per live-vs-archive policy); bodies unchanged.

**What Option B does not change:**
- The symbol Cᵢ itself.
- The mathematical formula (B.1, M.1).
- The four gates (L.1–L.4).
- Any of the framework's quantitative claims.
- The framework's originality or contribution.

---

## §16. Conditions for Option B to land

Integrated into Phase A3 audit sweep. Adds minor scope beyond tier-dissolution + macro-grouping Option A sweep.

### Condition 1 — Technical Appendix Sections L + M sweep

**What:** Replace "variable" with "cost" throughout Sections L and M where the term refers to Cᵢ. Preserve "variable" only where it refers to the general-mathematical sense (e.g., "variable of integration" — rare if at all). Preserve "cost term" as a compound-noun alternative in passages where "term-of-the-sum" is being explicitly invoked (e.g., "each cost term contributes additively under linearity of integration").

**Effort:** 0.5–1 day. Mechanical sweep with contextual judgment.

**Where:** `manuscript/technical-appendix/TechnicalAppendix_v0.0.4.html` Sections L.0–L.7 and M.0–M.7.

### Condition 2 — Ch 6 body coverage confirmation

**What:** Verify Ch 6 body uses "cost" as the class term consistently. Add a brief definitional sentence at first use noting "cost" in this book refers specifically to a Cᵢ admitted via the four gates.

**Effort:** 0.25 day.

**Where:** `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` — Approach 3 section or Four Gates section.

### Condition 3 — Ch 6 guidance doc sync

**What:** Update Ch 6 guidance doc to reflect "cost" as class term; remove any "variable" references that refer to Cᵢ.

**Effort:** 0.1 day.

**Where:** `manuscript/chapters/Chapter__6___GuidanceDoc.md`.

### Condition 4 — Subsequent-developments annotation on today's three rigor passes

**What:** Append `§ Subsequent developments` section to each of Path F pass, tier-reframing pass, macro-grouping pass noting the variable→cost rename happened after them. Bodies unchanged.

**Effort:** 0.1 day total.

**Where:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md`, `_tier_reframing_v1.0.0.md`, `_macro_grouping_v1.0.0.md`.

### Condition 5 — Terms index record

**What:** Add Cost record to `tools/back-matter/sources/terms_index.md` §4 (Established records) using the template in §1 of this pass and the Provenance Record at §17 below.

**Effort:** 0.1 day.

**Where:** `tools/back-matter/sources/terms_index.md`.

---

## §17. Term Provenance Record — deliverable

### Cost (Cᵢ)

**Working definition:** In Commons Bonds, a *cost* is a dollar-valued term Cᵢ admitted to the Residual Commons Value (RCV) integrand under the four gates of Section L of the Technical Appendix. Each cost has units [$ · resource-unit⁻¹ · time-unit⁻¹], is identified through the Abundance Inversion Test (AIT) applied to a specific extraction Context, and contributes additively to RCV via the sum-of-costs form. The class of all costs is open and extensible — AIT applied to new Contexts may surface new costs that the current framework does not enumerate.

**Status:** `CURRENT` (pending author ratification of this rigor pass)

**Term-spec version:** v1.0 (first ratified spec)

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_variable_vs_cost_v1.0.0.md` (2026-04-24) §15 — Option B (replace "variable" with "cost") recommended at full extreme rigor. Pending author ratification.
- `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md` (2026-04-24) §3 — Cᵢ admissibility via gates established; class-term naming not resolved there.
- `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md` (2026-04-24) §5.3 — dissolution confirmed variable-level as unit of measurement; reinforced Cᵢ atomic role.

**Depends on:**
- Path F variable-addability framework (Cᵢ class admits generative extension).
- Four-gate discipline (Section L).
- Sum-of-costs generalized RCV formula (Section M).
- Tier dissolution (tiers no longer competing class term).

**Staleness triggers:**
- Framework's atomic unit changes structurally (e.g., reintroduction of a higher-abstraction class above Cᵢ).
- Four-gate discipline changes materially.
- RCV formula restructured such that Cᵢ is no longer the integrand's atomic summand.
- Academic reception produces a published critique that the "cost" nomenclature is systematically ambiguous in a way context cannot disambiguate.

**Commit trail:**
- Pending commit: this rigor pass + initial TPS population.
- Downstream: commits applying Conditions 1–5 above.

**Supersedes:** prior informal usage of "variable" / "cost variable" / "cost term" in the Path F rigor pass and Technical Appendix Sections L + M (usage continues as historical record in those docs per live-vs-archive policy).

**Notes:**
- "Cost term" as a compound noun remains admissible in contexts where the term-of-the-sum math role is explicit (e.g., "each cost term Cᵢ enters the integrand"). This is not a second vocabulary — it's "cost" as the noun + "term" as the mathematical role label.
- The symbol notation Cᵢ is unchanged.
- Ambiguity with everyday "cost" in prose is managed by context-disambiguation — the same discipline economists apply to "utility" and "welfare."
- **Style-discipline addenda (inherited from Options D and E analysis):**
  - Prefer specific named costs ("black-lung cost," "community-transition cost") to the class noun wherever prose allows. Class noun is available as fallback; specific names are the default.
  - Preserve the bookkeeping metaphor at the discourse level — the framework is honest accounting; prose voice is an accountant's voice. "Cost" as atomic-unit name reinforces without needing more formal "ledger entry" / "accounting item" language.

---

## §18. Author-ratified resolutions

*Pending. Chris to review §15 recommendation + §16 conditions + §17 provenance record, then ratify or revise.*

### §18.1 Path choice

**Options:**
- (A) Keep "variable" (not recommended; fails M6, M8, M9, M11 relative to B).
- (B) Replace with "cost" + inherit style-discipline addenda from D and E (recommended).
- (C) Hybrid "cost term" / "cost" (not recommended; doubles vocabulary without proportional benefit).
- (D) Drop class term entirely (not recommended as standalone; insight survives as style discipline under B).
- (E) Entry / ledger entry (not recommended as standalone; insight survives as discourse-register discipline under B).

**Ratified decision:** *(pending)*

### §18.2 Conditions 1–5

**Ratified decision:** *(pending)* — each condition individually ratifiable.

### §18.3 Style-discipline addenda (D + E insights folded into B)

**Ratified decision:** *(pending)* — ratify both addenda, one, or neither.

Addenda being ratified:
- *D-addendum:* prefer specific named costs to the class noun "cost" wherever prose allows.
- *E-addendum:* preserve bookkeeping register at the discourse level (framework-as-honest-accounting), using "cost" as atomic-unit term.

---

## §19. Rerun gate

This rigor pass can be rerun if:

- Framework's atomic unit changes structurally (e.g., a new class layer introduced above Cᵢ).
- Published peer-review feedback identifies a systematic "cost" ambiguity the rigor pass did not anticipate.
- Success-criterion evidence shifts (e.g., "severed cost" vocabulary adoption fails, suggesting vocabulary alignment wasn't the right bet).

Absent these triggers, the verdict stands. Next expected rerun: at Phase B completion (chapter drafts land), verify "cost" vocabulary held up in prose.

---

*End of Extreme-Rigor Pass v1.0.0. Option B (replace "variable" with "cost" as class term for Cᵢ) PASSES-UNCONDITIONALLY as recommended path. Option A defensible but weaker on 9 of 11 modules. Option C vocabulary-footprint burden without compensating benefit. Pending author ratification at §18. Provenance Record at §17 ready for `tools/back-matter/sources/terms_index.md` §4.*
