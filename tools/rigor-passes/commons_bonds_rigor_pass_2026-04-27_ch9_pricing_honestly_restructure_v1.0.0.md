# Commons Bonds — Focused Rigor Pass: Ch 9 ("Pricing Honestly") Restructure

**Version:** 1.0.0
**Date:** 2026-04-27
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — full 12-module suite + §22 + §22.4 + all 6 Working Principles. Special focus on M3 (book content; publication-readiness; scaffolding-content discipline), M4 (craft / chapter-pacing), M6 (academic), M8 (long-term / test-of-time), M11 (critic survival), M12 (intellectual honesty).
**Scope:** Tests structural restructure for Ch 9 ("Pricing Honestly"; 10,608 words; 11 h3 sections in current draft). Ch 9 is the framework's policy-economy chapter — *"the set of practical moves a society would make if it decided to close the gap between what things cost and what we pay"* — with substantial counterargument-handling load given its policy-recommendation focus. Tests four interacting decisions:
1. **Preamble cleanup** (Decision 1: lines 1-9 model-output + scaffolding notes; remove / preserve / move-to-scaffolding-doc)
2. **Tier-vocabulary regression** (Decision 2: line 21 "tier by tier" cleanup)
3. **"Property rights, and their limits" section** (Decision 3: no restructure / lighter touch / full restructure)
4. **"The Nordic objection, taken seriously" section** (Decision 4: no restructure / lighter touch / full restructure)

Per author directive 2026-04-27: *"Focused Ch 9 rigor pass first — formal analysis before action."*

**Status:** rigor pass executed 2026-04-27; **ratified 2026-04-28 by Chris Winn** — full ratification of D1-A + D2-A + D3-N + D4-B. Implementation: 2-3 sequential commits per Phase 1-3 plan.
**Author:** Chris Winn

---

## §1. Executive summary

**RECOMMENDED:** Option **D1-A + D2-A + D3-N + D4-B** — Remove publication-blocker preamble entirely; fix line 21 tier-vocabulary regression; preserve "Property rights, and their limits" section as canonical inline-woven pattern; apply Ch 5-style lighter touch to "The Nordic objection, taken seriously" section.

**Decisive findings:**

1. **Lines 1-9 are publication-blocker scaffolding** — uncontroversial removal. Line 1 is preserved Claude/AI model-output (*"Let me connect to Google Drive..."*). Lines 3-9 are author/AI internal-process scaffolding notes including strikethrough editing markup (~~industrial-existential substitutability gap~~) + eight-tier vocabulary reference. Per architecture-rigor-pass discipline (publication-ready vs scaffolding split), this content does NOT belong in the chapter manuscript. **D1-A: REMOVE entirely.**

2. **Line 21 retired-vocabulary regression** — same eight-tier reference fixed in Ch 2 / Ch 5 / Ch 6 / Ch 8. Direct precedent established. **D2-A: APPLY same fix.**

3. **"Property rights, and their limits" section is canonical inline-woven.** Title is descriptive (engages property-rights tradition + identifies its limits), NOT explicitly counterargument-labeled. Body prose substantively engages Coase 1960 + Ostrom + free-market environmental tradition; provides three-part structural response (intergenerational foreclosure / transboundary externality / information asymmetry); closes with Adam Smith citation. Pattern matches Ch 4 ("Why Norway and not McDowell County" / "The part Norway has not solved") + Ch 7 ("Mars is a false analogy") + successful adjacent-framework books. **D3-N: NO restructure needed.**

4. **"The Nordic objection, taken seriously" section is Ch 5-style hybrid.** Title explicitly names "objection"; body uses defense-walkthrough register (*"The serious version of the objection has four load-bearing claims"* + *"Each of the four claims deserves specific engagement"* + per-claim sequencing labels at lines 173, 175, 177, 179). Same pattern as Ch 5's "first counterclaim / second counterclaim / etc." sequencing. Per Ch 5 ratification 2026-04-27, lighter-touch (B) is the proportional response: remove meta-framing language + sequencing labels; preserve rebuttal substance as continuation prose. **D4-B: LIGHTER TOUCH.**

5. **Cross-chapter precedent supports the recommendation:**
   - Ch 4 / Ch 7 verdict (no-restructure) → "Property rights" section
   - Ch 5 verdict (lighter touch) → "Nordic objection" section
   - Ch 2 / Ch 5 / Ch 6 / Ch 8 fixes (eight-tier-accounting cleanup) → line 21
   - Architecture rigor pass discipline (publication-ready vs scaffolding) → preamble

6. **Publication-readiness consequence is decisive.** Lines 1-9 preamble is a HARD publication-blocker — sending a chapter manuscript to a literary agent / publisher with the model-output preserved + author scaffolding notes intact + retired-vocabulary references is a basic professionalism failure. The remediation is uncontroversial and cannot be deferred.

7. **Implementation cost-benefit:** D1-A + D2-A + D3-N + D4-B requires ~2-3 commits across decisions; ~45-60 minutes of work. Disciplined response to clearly-identified findings; no rigor-pass-deferred decisions.

8. **M8 test-of-time analysis:** A book's policy chapter ages well when it foregrounds substantive engagement with serious objections (Property rights / Nordic conditions) and ages poorly when defensive register dates with the political moment. D3-N + D4-B preserve substantive engagement; remove defense register at the section that has it; align Ch 9 with the durable-policy-chapter pattern.

**Net verdict:** D1-A + D2-A + D3-N + D4-B. Multi-commit cleanup with clear precedent; no controversial decisions; publication-readiness restored.

---

## §2. The question under test

### §2.1 Author's directive

> *"Focused Ch 9 rigor pass first — formal analysis before action."*

Surfaced after Ch 9 cross-chapter sweep scope assessment found:
- Lines 1-9: model-output preamble + scaffolding notes (NOT belonging in chapter manuscript)
- Line 7: "eight tiers" retired-vocabulary reference within preamble
- Line 21: "tier by tier" retired-vocabulary regression in chapter body
- "Property rights, and their limits" h3 section (line 145+): substantive academic engagement
- "The Nordic objection, taken seriously" h3 section (line 165+): defense-walkthrough register

### §2.2 Four interacting decisions

**Decision 1 — Preamble cleanup:**
- **D1-A:** REMOVE lines 1-9 preamble entirely **— RECOMMENDED**
- **D1-B:** Move preamble to a separate scaffolding doc (e.g., `core/scaffolding/ch9_drafting_notes.md`); preserve internal-process record
- **D1-C:** Preserve preamble as-is; accept the scaffolding-in-publication-artifact pattern

**Decision 2 — Tier-vocabulary at line 21:**
- **D2-A:** APPLY same fix as Ch 2 / Ch 5 / Ch 6 / Ch 8 — replace "tier by tier" with current vocabulary **— RECOMMENDED**
- **D2-B:** Leave line 21 as-is

**Decision 3 — "Property rights, and their limits" section:**
- **D3-N:** NO restructure — canonical inline-woven pattern **— RECOMMENDED**
- **D3-B:** Lighter touch — soften any descriptive-but-defensive register
- **D3-A:** Full restructure — distribute substance to natural arising points

**Decision 4 — "The Nordic objection, taken seriously" section:**
- **D4-N:** NO restructure
- **D4-B:** Lighter touch — remove defense-walkthrough meta-framing + sequencing labels per Ch 5 precedent **— RECOMMENDED**
- **D4-A:** Full restructure — distribute substance to natural arising points + remove h3 wrapper

### §2.3 Falsifiers

- **D1-A falsified if:** preamble contains substantive content that belongs in the chapter (verified: it does not — pure scaffolding).
- **D2-A falsified if:** "tier by tier" prose is not actually retired-vocabulary regression (verified: 8-tier scheme RETIRED 2026-04-24 per tier-reframing rigor pass §11).
- **D3-N falsified if:** "Property rights, and their limits" section uses defense register on closer reading (verified: it does not — substantive academic engagement throughout).
- **D4-B falsified if:** removing meta-framing labels destroys the section's pedagogical effectiveness (verified by parallel Ch 5 ratification: lighter-touch preserves substance).

---

## §3. Findings inventory

### §3.1 Publication-blocker preamble (lines 1-9)

```
Line 1: "Let me connect to Google Drive to pull the Chapter 9 assessment and scaffold documents.I found the critical documents..."
Line 3: "Before writing, a few notes on what I applied from the consolidated project state across your chats, the assessment doc, and the scaffold:"
Line 5: "- ~~industrial-existential substitutability gap, not ESG. The acronym changed (Civilizational Substitutability Gap). I used industrial-existential substitutability gap throughout.~~ *(2026-04-24 M12 sweep: industrial-existential substitutability gap retired on parsimony grounds; chapter prose updated to use "industrial-existential substitutability gap" inline.)*"
Line 6: "- ~~"Value capture," not "value extraction."~~ *(2026-04-24 superseded: Value Extraction is the Ring-1 framework term; Value Capture retired. Chapter prose updated.)*"
Line 7: "- Book One scope. Per the Chapter 8 decision, Book One walks the McDowell County example through eight tiers."
Line 8: "- Register 2 entered through Register 1. Same pattern Chapter 8 established."
Line 9: "- The "framework, not blueprint" landing is deliberately placed as the last counterargument before the Chapter 10 transition, as the scaffold specifies."
```

**Type of content:**
- Line 1: Preserved Claude/AI model-output from drafting session (literal "Let me connect to Google Drive..." opening)
- Lines 3-9: Author/AI internal-process scaffolding notes (with strikethrough editing markup at lines 5-6)
- Line 7: Eight-tier retired-vocabulary reference

**Publication-readiness:** This is exactly the publication-blocker content that the architecture-rigor-pass discipline was authored to remove from publication artifacts. The architecture pass §B1 explicitly identified scaffolding-in-publication-artifacts as a problem; new `core/scaffolding/` directory was authorized for housing this internal-process content.

### §3.2 Line 21 tier-vocabulary regression

> *"One ton of McDowell County coal, sold at the mine mouth in 1960 for four dollars and fifty cents, actually cost — conservatively, floor-estimated, **tier by tier** — somewhere between five hundred and six hundred dollars when every severed cost was priced honestly."*

Direct parallel to Ch 2 line 123 ("through eight cost tiers" — fixed in commit `da04836`); Ch 5 line 209 ("the full eight-tier accounting" — fixed in commit `ec85a38`); Ch 6 line 837 ("the full eight-tier accounting" — fixed in commit `201ca17`); Ch 8 various references (~17 instances fixed in commit `323fd99`).

**Recommended replacement:** "*conservatively, floor-estimated, cost-component by cost-component*" (parallel to Ch 8 Phase 1 fix to line 21 of that chapter).

### §3.3 "Property rights, and their limits" section (lines 145-161)

**Title:** Descriptive — names the topic the section engages, not the defensive-handling register.

**Body register:** Substantive academic engagement. Opens with *"The most intellectually serious objection to anything like this framework comes from the property rights tradition, and it deserves an honest hearing before the chapter closes"* — single-sentence acknowledgment, then immediately into substantive engagement. NO sequenced "first counterclaim / second counterclaim" labeling. NO meta-framing batched defense-walkthrough.

**Structure of engagement:**
- Para 1: Acknowledgment + "deserves an honest hearing"
- Para 2: Steelman of the property-rights position (Coase 1960 + Ostrom + free-market environmental + empirical successes)
- Para 3: Framework's response — agrees with most of it; identifies three specific limits
- Paras 4-6: Three limits (intergenerational foreclosure / transboundary externality / information asymmetry at civilizational scale)
- Para 7: "This is not a refutation of property rights. It is an identification of the domain..."
- Para 8: Adam Smith citation closing

**Pattern match:**
- Ch 4 "Why Norway and not McDowell County" — same canonical inline-woven engagement
- Ch 7 "Mars is a false analogy" — same canonical pattern
- Successful adjacent-framework books (Smith / Marx / Keynes / Ostrom / Mazzucato) — canonical inline-woven engagement at substantive depth

**Verdict:** Canonical inline-woven pattern. NO restructure needed.

### §3.4 "The Nordic objection, taken seriously" section (lines 165-181)

**Title:** Explicitly labels "objection" — defense-handling register at section title.

**Body register:** Defense-walkthrough register with explicit sequencing.

Key meta-framing language:
- Line 165: *"the framework cannot earn the citation of Nordic examples without engaging it specifically. The objection is not that... The objection is that..."*
- Line 169: *"The serious version of the objection has four load-bearing claims. The first is scale... The second is demographic homogeneity... The third is the resource base. ... The fourth is historical contingency."*
- Line 173: *"Each of the four claims deserves specific engagement. On scale: ..."*
- Line 175: *"On demographic homogeneity, the steelman's strongest claim. Three responses pressure-test the claim. First, ... Second, ... Third, ..."*
- Line 177: *"On resource base..."*
- Line 179: *"On historical contingency..."*
- Line 181: *"The defeat does not claim... The defeat claims four things..."*

**Pattern match:**
- Ch 5 "2008 section" + "Social Security section" — same defense-walkthrough register with explicit sequencing labels ("first counterclaim / second counterclaim / third counterclaim / fourth counterclaim")
- Ch 5 ratified 2026-04-27 (Option B lighter touch): remove meta-framing language + sequencing labels; preserve rebuttal substance as continuation prose

**Verdict:** Ch 5-style hybrid pattern. Lighter-touch (D4-B) is the proportional response per established Ch 5 precedent.

---

## §4. Decision 1 — Preamble cleanup

### §4.1 D1-A (REMOVE) analysis — RECOMMENDED

Lines 1-9 contain zero substantive chapter content. The chapter actually begins at line 13 (`# Commons Bonds` / line 17 `## Chapter 9: Pricing Honestly`).

Removal cost: zero substantive content lost.

Removal benefit: chapter manuscript becomes publication-ready at the file's opening; no model-output preamble; no author scaffolding visible to literary agents / publishers / academic readers.

### §4.2 D1-B (move to scaffolding doc) analysis

Preserve preamble's internal-process record value (which retired-vocabulary decisions were applied; which scaffold notes were honored) by relocating to `core/scaffolding/ch9_drafting_notes.md` per architecture-rigor-pass §B1 scaffolding-doc discipline.

Pro: preserves drafting-process record.
Con: the preamble's value is mostly historical (records vocabulary decisions already documented elsewhere — terms_index, rigor passes, commit messages). Marginal value for relocation effort.

**Verdict on D1-B:** Acceptable but unnecessary. The chapter's drafting-process is fully recorded in commit messages + rigor passes + terms_index. The preamble itself is duplicative scaffolding.

### §4.3 D1-C (preserve as-is) analysis

Keeps the publication-blocker. **Rejected outright.**

### §4.4 Verdict on Decision 1

**D1-A (REMOVE) is dominant.** Pure publication-readiness fix; zero substantive loss; zero discipline-violation introduced.

---

## §5. Decision 2 — Line 21 tier-vocabulary

### §5.1 Cross-chapter precedent

| Chapter | Original phrase | Fix |
|---|---|---|
| Ch 2 | "through eight cost tiers" | "the framework's full cost-decomposition" |
| Ch 5 | "the full eight-tier accounting" | "the framework's full cost-decomposition" |
| Ch 6 | "the full eight-tier accounting" | "the framework's full cost-decomposition" |
| Ch 8 (line 13 scope) | "through the eight tiers" | "through the framework's full cost-decomposition" |
| Ch 8 (line 21 framing) | "tier by tier" | "cost-component by cost-component" |
| Ch 9 (line 21) | **"tier by tier"** | **"cost-component by cost-component"** |

### §5.2 Verdict on Decision 2

**D2-A (apply same fix) is dominant.** Direct precedent established across 5 prior chapters; pure substitution; zero controversy.

---

## §6. Decision 3 — "Property rights, and their limits" section

### §6.1 Canonical-pattern test

A section is canonical inline-woven when:
- (a) Title describes positive content engaged, NOT defense-handling register
- (b) Body prose engages substantively without batched-walkthrough sequencing labels
- (c) Engagement reads as continuation of chapter argument flow, not retrospective defense
- (d) Substance preserved at full depth without compression to defensive coda

**Ch 9 "Property rights, and their limits" against the test:**
- (a) ✓ — title descriptive
- (b) ✓ — three-limits structure flows as continuation prose (intergenerational / transboundary / information asymmetry); no "first counterclaim" sequencing
- (c) ✓ — opens *"deserves an honest hearing before the chapter closes"* and continues into Adam Smith citation; reads as substantive engagement
- (d) ✓ — full-depth engagement with Coase + Ostrom + free-market tradition

All four canonical-pattern criteria met. Pattern matches Ch 4 "Why Norway and not McDowell County" (no-restructure verdict 2026-04-27).

### §6.2 D3-N (no restructure) analysis — RECOMMENDED

Section is already compliant with B-2 inline-woven discipline. No edits needed.

### §6.3 D3-B (lighter touch) analysis

What would lighter-touch even change? The section has no meta-framing language to remove; no sequencing labels; no defense register. Lighter-touch becomes a no-op.

### §6.4 D3-A (full restructure) analysis

Distributing the section's three-limit response across the chapter would require finding where each limit naturally arises in chapter prose AND breaking up the substantive engagement that the chapter's policy-economy register benefits from having in one place.

Distribution candidates:
- Intergenerational foreclosure → Step 1 Classify? (no obvious natural fit)
- Transboundary externality → "The international dimension" section (possible)
- Information asymmetry → "Entering wedges" section (possible)

Cost: significant restructure with high risk of disrupting argumentative flow. Property-rights tradition deserves cohesive engagement; distributing fragments the philosophical argument. **REJECTED.**

### §6.5 Verdict on Decision 3

**D3-N (no restructure) is dominant.** Section is canonical inline-woven; matches Ch 4 + Ch 7 + adjacent-framework-book patterns.

---

## §7. Decision 4 — "The Nordic objection, taken seriously" section

### §7.1 Pattern match to Ch 5 ratification

Ch 5's "2008 section" + "Social Security section" both used:
- Meta-framing language: *"counter-positions deserve specific engagement here"* / *"engaging each at its strongest is what distinguishes a framework that survives review from one that survives only sympathetic reading"*
- Sequencing labels: *"first counterclaim / second counterclaim / third counterclaim / fourth counterclaim"* / *"first counter-position / second counter-position"*

Ch 5 ratification 2026-04-27 (Option B lighter touch):
- Removed meta-framing sentences
- Replaced sequencing labels with prose-continuation phrasing ("A careful reader will object that..." / "A second objection holds that..." / etc.)
- Preserved rebuttal substance verbatim
- Net change: ~70-110 words removed; argumentative arc preserved

Ch 9 "Nordic objection" parallel state:
- Meta-framing language: *"The serious version of the objection has four load-bearing claims"* + *"Each of the four claims deserves specific engagement"*
- Sequencing labels: per-paragraph "On scale: ..." / "On demographic homogeneity..." / "On resource base..." / "On historical contingency..."
- Closing: *"The defeat claims four things"* (sequenced 4-thing-list close)

Same structural pattern; same lighter-touch fix applies.

### §7.2 D4-B (lighter touch) analysis — RECOMMENDED

**Specific edits:**

1. **Section title** — keep "The Nordic objection, taken seriously" (descriptive AND honors substantive engagement; the parallel to Ch 5's "Counter-positions deserve specific engagement here" was at body-paragraph level, not title level — Ch 5's section h3s were also unmoved).

2. **Line 169 sequencing-list intro** — replace meta-framing:
   - OLD: *"The serious version of the objection has four load-bearing claims. The first is scale. ... The second is demographic homogeneity. ... The third is the resource base. ... The fourth is historical contingency. ..."*
   - NEW: *"The serious version of the objection rests on scale, demographic homogeneity, the resource base, and historical contingency."* (single sentence enumeration; preserves all four claims; removes "load-bearing claims" register)

3. **Line 173 sequencing-walkthrough intro** — replace meta-framing:
   - OLD: *"Each of the four claims deserves specific engagement. On scale: ..."*
   - NEW: *"On scale, the framework's response is..."* (drop "deserves specific engagement" framing; flow into per-claim response)

4. **Per-claim sequencing** at lines 173, 175, 177, 179 — keep "On scale" / "On demographic homogeneity" / "On resource base" / "On historical contingency" as continuation-prose markers; these are CLEAR pedagogical signposting (not defense-walkthrough register). Per Ch 5 lighter-touch precedent: descriptive transition phrases stay; defense-batching meta-framing goes.

5. **Closing line 181** — soften:
   - OLD: *"The defeat does not claim Nordic outcomes can be produced in the United States with current U.S. conditions. The defeat claims four things..."*
   - NEW: *"The framework's response to the Nordic objection is not that Nordic outcomes can be produced in the United States with current conditions. It is more specific..."* + the four substantive points retained as continuation prose.

**Net effect:** ~100-150 words touched; rebuttal substance preserved; defense register reduced.

### §7.3 D4-N (no restructure) analysis

Defense-walkthrough register persists. Under-applies discipline. Per ratified Ch 5 precedent: lighter-touch is proportional.

### §7.4 D4-A (full restructure) analysis

Distributing the four Nordic-objection responses to natural arising points throughout the chapter:
- Scale response → "Step 1 — Classify" (where state/municipal scale could arise)
- Demographic-homogeneity response → "Entering wedges" or earlier policy-architecture sections
- Resource-base response → "Step 2 — Reserve" (where revenue-base discussion arises)
- Historical-contingency response → "What a framework does" closing

Cost: significant restructure; loses cohesive engagement with the four-claim Nordic-not-replicable objection; chapter's policy-economy register benefits from cohesive engagement.

Per Ch 5 precedent: full restructure rejected; lighter-touch preferred for hybrid sections.

### §7.5 Verdict on Decision 4

**D4-B (lighter touch) is dominant.** Direct Ch 5 precedent; proportional response; preserves substantive engagement.

---

## §8. Cross-chapter precedent comparison

| Chapter | Pattern | Verdict | Magnitude |
|---|---|---|---|
| Ch 2 | 2 dedicated counterargument h3s + 1 retired-vocab line | Full restructure | Smaller |
| Ch 4 | Inline-woven canonical (descriptive section titles; substantive engagement) | No restructure | N/A |
| Ch 5 | Inline-but-meta-framed walkthroughs | Lighter touch | Smaller |
| Ch 6 | 4 dedicated h3 counterargument sections | Full restructure | Larger (defense cluster) |
| Ch 7 | Inline-woven canonical | No restructure | N/A |
| Ch 8 | Tier-vocabulary saturation + dedicated counterargument coda | Multi-decision restructure | Largest |
| **Ch 9** | **Preamble + 1 retired-vocab line + 1 canonical section + 1 hybrid section** | **D1-A + D2-A + D3-N + D4-B** | **Mid (preamble cleanup is non-trivial; restructure is small per-section)** |

Ch 9 sits between Ch 4/Ch 7 (no-restructure) and Ch 5 (lighter touch); plus has the unique preamble cleanup not seen in other chapters.

---

## §9. M1–M11 abbreviated module results

| Module | D1-A + D2-A + D3-N + D4-B performance |
|---|---|
| **M1 CORE math** | PASS — math unchanged; Ch 9 is policy-economy chapter, no formulas |
| **M2 Case study** | PASS — cases unchanged (Norway / Alaska / Mitchell-Lama / state programs preserved) |
| **M3 Book content** | **STRONGLY STRENGTHENS** — closes publication-blocker preamble; tier-vocabulary regression closed; defense-register reduced at "Nordic objection" |
| **M3.4 Counterargument coverage** | PRESERVED — both counterargument-handling sections retain substantive engagement; rebuttals woven inline (canonical "Property rights" pattern preserved; "Nordic objection" defense-register reduced but substance preserved) |
| **M4 Craft** | STRENGTHENS — chapter becomes publication-ready at file open; Nordic-objection section reads as continuation prose rather than batched defense |
| **M5 Dinner-table** | STRENGTHENS — preamble cleanup removes meta-process content that breaks reader-flow at chapter open |
| **M6 Academic** | STRONGLY STRENGTHENS — academic reviewer sees clean publication artifact; substantive Coase/Ostrom + Nordic-conditions engagement preserved at full depth |
| **M7 Originality** | UNCHANGED — chapter's policy-architecture contribution (4-step + entering wedges) preserved |
| **M8 Long-term / test-of-time** | **STRONGLY STRENGTHENS** — preamble removal closes scaffolding-in-publication regression that would date book-publication artifact within months; vocabulary aligned with current ratified framework |
| **M9 Risk** | LOW — restructure scope contained; substantive content preserved |
| **M10 Publishing** | **STRONGLY STRENGTHENS** — chapter manuscript becomes ready for literary-agent / publisher submission; preamble cleanup is publication-blocker close |
| **M11 Critic** | STRENGTHENS — academic reviewer surveying chapter for current-framework alignment finds it; counterargument coverage preserved at substantive depth |

**§22 alignment:** D1-A + D2-A + D3-N + D4-B positive on Primary Goals — Publishing Path; Academic Reception; Long-term Impact.

**§22.4 stand-test-of-time alignment:** STRONGLY POSITIVE.

---

## §10. M12 — Intellectual honesty audit

### §10.1 Per-decision M12

**D1-A (REMOVE preamble):** Honest about what's a chapter manuscript vs what's drafting scaffolding. The preamble's internal-process content is preserved in commit messages + terms_index + rigor passes — the canonical-source-of-truth locations for those decisions. Removing the preamble from publication artifact does NOT lose information; it relocates information to where it belongs. **PASSES.**

**D2-A (line 21 fix):** Honest about retired-vocabulary discipline. Same fix applied across 5 prior chapters. **PASSES.**

**D3-N (no restructure for Property rights section):** Honest about discipline application — section already compliant; no action required. **PASSES.**

**D4-B (lighter touch on Nordic objection):** Honest about defense-register reduction proportional to discipline-violation magnitude. Substance preserved; meta-framing removed. **PASSES.**

### §10.2 M12 verdict

**D1-A + D2-A + D3-N + D4-B is M12-optimal.** All four decisions honor framework-discipline + publication-readiness + counterargument-coverage simultaneously.

---

## §11. Verdict synthesis + recommendation

### §11.1 Recommended combination

**D1-A + D2-A + D3-N + D4-B.**

- **D1-A:** REMOVE lines 1-9 preamble (publication-blocker model-output + scaffolding notes; ~9 lines; zero substantive content)
- **D2-A:** APPLY tier-vocabulary fix to line 21 ("tier by tier" → "cost-component by cost-component")
- **D3-N:** NO restructure for "Property rights, and their limits" section (canonical inline-woven; matches Ch 4 + Ch 7 patterns)
- **D4-B:** LIGHTER TOUCH on "The Nordic objection, taken seriously" section (remove meta-framing language at lines 169, 173, 181; preserve per-claim signposting + substance; ~100-150 words touched)

### §11.2 Three rigor questions on Ch 9 sweep

| Question | Verdict |
|---|---|
| **Earns place?** | Substance YES (chapter's policy-architecture pedagogy is load-bearing). Preamble does NOT earn its place (publication-blocker scaffolding). Defense-register meta-framing in Nordic-objection section does NOT earn its place. Property-rights section earns its place fully. |
| **Would expansion strengthen?** | NO — chapter length appropriate for policy-economy register; expansion would dilute. |
| **Would compression strengthen?** | YES — preamble removal + Nordic-objection meta-framing removal compress surface area without losing substance. Net ~10-12 lines removed (preamble) + ~100-150 words touched (Nordic-objection) = clean compression. |

### §11.3 Implementation phases

**Phase 1 (1 commit):** Decision 1 — REMOVE lines 1-9 preamble.

**Phase 2 (1 commit, possibly bundled with Phase 1):** Decision 2 — fix line 21 "tier by tier" → "cost-component by cost-component."

**Phase 3 (1 commit):** Decision 4 — lighter-touch on "Nordic objection" section (3 specific edits at lines 169, 173, 181 per §7.2).

Total: ~2-3 commits / ~45-60 minutes.

### §11.4 Rejected alternatives + rationale

| Alternative | Rejected because |
|---|---|
| **D1-B (move preamble to scaffolding doc)** | Marginal value over D1-A; chapter's drafting-process is fully recorded in commit messages + rigor passes + terms_index; preamble is duplicative scaffolding |
| **D1-C (preserve preamble)** | Publication-blocker; sending a chapter with model-output preamble to a literary agent / publisher is a basic professionalism failure |
| **D2-B (leave line 21)** | Direct precedent across 5 prior chapters; no defensible reason to leave only Ch 9 with retired vocabulary |
| **D3-B (lighter touch on Property rights)** | Section has no meta-framing or sequencing labels to remove; lighter-touch becomes no-op |
| **D3-A (full restructure on Property rights)** | Would fragment cohesive philosophical engagement; chapter's policy-economy register benefits from cohesive engagement; HIGH chapter-quality risk |
| **D4-N (no restructure on Nordic objection)** | Defense-walkthrough register persists; under-applies ratified Ch 5 precedent |
| **D4-A (full restructure on Nordic objection)** | Would fragment cohesive engagement with four-claim Nordic-not-replicable objection; per Ch 5 precedent: lighter-touch preferred for hybrid sections |

---

## §12. Author-ratified resolutions

**[PENDING — author ratification 2026-04-27.]**

Once ratified:
- Apply D1-A + D2-A + D3-N + D4-B in 2-3 sequential commits per Phase 1-3 plan
- Mark Track B Ch 9 sweep complete (cross-chapter sweep todo)
- Cross-reference this rigor pass from terms_index entries that reference Ch 9 (none currently; eventual cross-references when terms_index Phase 2 restructure reaches relevant terms)

---

## §13. Rerun gate

Rerun if:
- D1-A preamble removal surfaces that some content WAS substantive chapter material (would push toward D1-B move-to-scaffolding-doc).
- D4-B lighter-touch edits surface that the Nordic-objection section's argumentative tightness depends on the meta-framing labels (would push toward D4-N no restructure).
- Future Ch 9 holistic review (per Insight #22 sweep discipline) reconsiders chapter scope or pedagogy.
- Ch 10 sweep finding pushes back on Ch 9's structural decisions retrospectively.

---

*End of focused rigor pass v1.0.0 on Ch 9 ("Pricing Honestly") restructure. D1-A + D2-A + D3-N + D4-B recommended (preamble removal + line 21 tier-vocabulary fix + no restructure for Property rights section + lighter touch on Nordic-objection section). All 12 modules examined; decision dominated by M3 + M8 + M10 publication-readiness + M12 discipline alignment + cross-chapter precedent (Ch 4/Ch 7 canonical + Ch 5 lighter-touch + Ch 8 vocabulary cleanup + architecture-rigor-pass scaffolding-doc discipline). Pending author ratification.*
