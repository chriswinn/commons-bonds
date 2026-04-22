# Commons Bonds — Rigor Pass Record · 2026-04-21

**Version:** 1.0.0 · **Date:** 2026-04-21 · **Status:** Proposed — awaiting ratification (pending abundance-layer rigor pass per handoff v1.24.0 Part 2)

## Purpose

Traceable record of the rigor passes applied during the 2026-04-21 scoping session. Documents what was tested, what was found, what survived, and what was corrected in each pass. Produced so that future rigor-pass work can reference this session's findings rather than re-derive them, and so that any decision that traces back to this session can be audited against the tests that produced it.

This document is **a record, not a protocol.** The protocol is `commons_bonds_rigor_protocol_v1_0_0.md`, which codifies what the 25 tests and 25 characters are. This document records how those were applied on a specific date and what each application produced.

Three rigor passes were run during the session, each producing a scope-document version: v1.0.1, v1.0.2, v1.0.3. Each pass is documented below with its testing target, findings, and the document revisions the findings produced.

---

## 1. Session context

**Date:** 2026-04-21

**Inputs at session start:**
- Session handoff v1.23.0 (which ratified memory v1.0.1 + preferences privacy-addendum application and sequenced book-scoping as top priority)
- Five uploaded files providing scoping context: publishing strategy (Apr 18), critical impact assessment (Apr 19), success criteria document (Apr 19), BookOneBookTwoPath conversation (source of Abundance Inversion Test derivation and Book Two deferral rationale), and the prior handoff itself
- Memory v1.0.1 applied (SGA presidency, four-tier boat budget framework, Loretta named, May academic gates, renewable marine propulsion watch, etc.)
- Preferences privacy-addendum applied (private-context-vs-external-output scrubbing rule)

**Outputs at session end (proposed, awaiting ratification):**
- `commons_bonds_book_scope_v1_0_0.md` (initial scoping; superseded)
- `commons_bonds_book_scope_v1_0_1.md` (first rigor pass outputs; superseded)
- `commons_bonds_book_scope_v1_0_2.md` (second rigor pass outputs; superseded)
- `commons_bonds_book_scope_v1_0_3.md` (third rigor pass outputs; current proposed-canonical)
- `commons_bonds_rigor_protocol_v1_0_0.md` (first formalization of 25-test + 25-character suite)
- `commons_bonds_chapter_guidance_addendum_ch6_7_8_v1_0_0.md` (focused addendum on worked-example requirements)
- This document
- Session handoff v1.24.0

**Critical gap surfaced at session close:** the abundance layers that the Abundance Inversion Test operates on were assumed canonical throughout all three rigor passes. They have not themselves been validated through the rigor framework. Next session's top priority runs the framework against itself on the abundance-layer set. All three of this session's rigor-pass outputs are therefore proposed-awaiting-ratification until the layer rigor pass completes.

---

## 2. Rigor Pass #1 — producing scope v1.0.1 from v1.0.0

### 2.1 Testing target

Scope document v1.0.0's key architectural moves:

- Three-book split (Book One / Book Two / Book Three scope)
- Abundance Inversion Test as canonical Book One content
- Chapter 8 trim (one worked example + aggregate signpost, not full simulation)
- Ch. 8 story choice (coal as the default)
- No pre-built reader tools
- Political Capture Cost (PCC) as a structural tier
- Publishing path as orthogonal to Book One scope
- Book Two deferral preconditions (three-of-five threshold)
- Success criteria with ten-year timeline

### 2.2 Tests applied

Full rigor per §1 of the protocol document. All 25 framework tests + all 25 characters applied to each move above.

### 2.3 Findings

**Findings that corrected v1.0.0:**

- **PCC as tier failed three gates.** Primitiveness gate failed — PCC decomposes into meta-level description of shielding operations on existing tiers; it's second-order content about how other costs get hidden, not first-order cost content. Merger gate failed in one direction — PCC does not exist without other tiers (alone it has no referent; it is always the suppression of something). Two-path test on PCC itself produced the cleanest finding: PCC is a shield. It fails the shield-absence path because political capture is *itself* the mechanism by which visibility is suppressed. **Correction applied in v1.0.1:** PCC reclassified as shielding condition (political-abundance layer of AIT), not tier. Glossary entry retained; eight-tier decomposition no longer contains PCC.

- **Publishing path orthogonal framing was wrong.** The v1.0.0 draft treated Noema / Berggruen cascade as timing-only, independent of Book One scope. The rigor pass traced the dependency chain explicitly: essay placement → vocabulary enters discourse → agent notices → publisher acquires → non-trivial distribution → 13+-year vocabulary adoption possible. Without essay placement, the chain breaks at step one. Every success criterion in §7 assumes non-trivial circulation. **Correction applied in v1.0.1:** publishing path reclassified as integral to Book One success criteria; §8 rewritten to document the dependency; scope v1.0.3 §9 trigger #1 subsequently updated to reflect that cascade outcomes carry scope-level implications.

- **Success criteria timeline was understated.** V1.0.0 used "ten years" for the canonical labor-lawyer sentence. Chris corrected during pass review: canonical is "thirteen or more years." **Correction applied in v1.0.1:** timeline updated throughout §1.8, §7.1, §7.2.

- **Book Two preconditions too loose.** V1.0.0's "three of five" heuristic permitted configurations that failed the two-path rigor test applied reflexively to authorship. Specifically, a Book Two written by a lone author without coauthor and without strong publisher would fail allocation symmetry (political costs borne by author while political benefits distribute to downstream users) and fail shield absence (no institutional distance from named beneficiaries). **Correction applied in v1.0.1:** preconditions restructured into necessary (coauthor OR institutional affiliation, AND strong publisher) vs. supporting (circulation, non-overlap, life stability). Both necessary conditions must be met.

- **Ch. 8 coal rationale was defaulted, not derived.** V1.0.0 used coal for Ch. 8's worked example because that was what the prior BookOneBookTwoPath conversation converged on, not because coal had been tested against alternatives. The rigor pass evaluated six candidates (coal, Social Security, IT/knowledge work, Libby asbestos, asteroid miner hypothetical, fresh case represented by lithium) across eight criteria (full eight-tier activation, empirical record, cross-spectrum positioning, paradigmatic status, individual-reader applicability, publisher/agent appeal, Noema/Berggruen placement fit, architectural cohesion). **Finding:** coal holds, but for three specific reasons that needed stating — full eight-tier activation is rare (most candidates exercise only 4–6 tiers cleanly); architectural continuity with Ch. 2 deepens rather than starts fresh; paradigmatic status (the most familiar extraction case) lets readers trust method transfers. Coal's real weakness (low individual applicability for non-miner readers) is not Ch. 8's problem — it's solved by Ch. 1 (narrative IT) and Ch. 6 (tier decomposition). **Correction applied in v1.0.1:** Ch. 8's coal rationale stated explicitly in §1.9; lithium named as pre-ratified drafting-stage fallback if Ch. 2-to-Ch. 8 redundancy surfaces during actual writing.

**Findings that held v1.0.0 positions:**

- Three-book split: held. Two-path test applied reflexively to authorship confirmed structural soundness of the split. Book One as framework-naming work by a lone author passes both paths (symmetric + shielded). Book Two applicative work by a lone author fails both paths. Book Three stands as distinct because audience, time horizon, and authorial configuration are bilaterally independent from Book Two.
- Abundance Inversion Test canonical in Book One: held. Primitiveness and merger gates both passed (meta-method, not decomposable into existing layers; bilaterally independent from the tier set).
- Chapter 8 trim (no full simulation): held. Scope test confirmed the simulation is book-length not chapter-length; cross-spectrum test confirmed the simulation pulls Book One toward Book Two's territory and loses neutral framework positioning.
- No pre-built reader tools: held. Confirmed that the framework is the tool; pre-built checklists would substitute the author's instance for the reader's, weakening extensibility.

### 2.4 Character suite highlights

- **Publisher's legal counsel** backed the three-book split for Book One (mechanism-naming, low defamation surface).
- **Tenured economics chair** said Book Two's claims need peer-reviewed empirical backing before a lone author names beneficiaries — reinforces the deferral.
- **Harvey/Klein reader** recognized the pattern (framework first, application second) — pattern-match validation.
- No single character produced red flags at this pass; most pressure was productive, surfacing the corrections listed above.

### 2.5 Cascade

All v1.0.1 corrections applied to the scope document in the same working pass. No downstream documents affected (rigor protocol and chapter guidance addendum were produced later in the session, on top of v1.0.1 findings).

---

## 3. Rigor Pass #2 — producing scope v1.0.2 from v1.0.1

### 3.1 Testing target

Configuration C for Ch. 6: two parallel individual-level worked applications, drawn from the author's career, representing the worker-perspective and CEO-perspective on the same cost-severance mechanism. Tested against the alternative configurations:

- Configuration A: one case in Ch. 8 only (v1.0.1 state)
- Configuration B: two cases concentrated in Ch. 8
- Configuration C: worked cases distributed across chapters (Ch. 6 carries the individual-scale dual case)

### 3.2 Tests applied

Full rigor suite against Configuration C. All 25 framework tests + all 25 characters.

### 3.3 Findings

**Configuration C passes all 25 framework tests.** Specific passes worth recording:

- Two-path rigor test passes cleanly: the dual case is allocation symmetry made visible (same person, different structural positions, same mechanism); first-person authorial proximity is shield-absent by definition.
- Merger gate passes: worker case and CEO case are bilaterally independent (each does distinct work the other cannot).
- Primitiveness gate passes: analytical tier treatment in Ch. 6 is not decomposable into the narrative treatment in Ch. 1.
- Cross-spectrum preservation **strengthens** under Config C — both left and right critics lose their easy attack (neither pure-victim narrative nor CEO-apologism).
- Direct-to-Goal-2 strengthens dramatically — two worked individual-scale cases vs. one is the largest win in the whole pass.

**Critical flag from the character suite — Character 23 (former subordinate from CEO days):**

If any specific person from the author's CEO history could identify themselves in the Ch. 6 CEO-case worked example, there is both ethical exposure (analyzing an individual without consent) and legal exposure (defamation risk even when factually accurate; potential contract / NDA issues). This is the one character in the suite that surfaced a concrete pre-drafting requirement rather than a tactical adjustment.

**Mitigation canonicalized in v1.0.2 §1.11, ordered by preference:**

1. Pattern description without identifiable specifics — the framework doesn't require named specifics to demonstrate tier activation.
2. Composite fictionalization with explicit author's note ("Details drawn from multiple engagements; no single subordinate is depicted.")
3. Explicit permission from any identifiable subordinate — highest authenticity, highest friction.

No specific subordinate is named or described identifiably without their explicit permission.

**Secondary flags from the character suite:**

- **Chapter length discipline.** Ch. 6 grows from current scaffold state by ~3–5K words with two parallel cases. Character 22 (MFA writing program critic) surfaced pressure on pacing. Mitigation: structural sub-sectioning discipline.
- **First-person proliferation.** Ch. 1, Ch. 6, and Ch. 8's closing signpost are three authorial touchpoints. Character 22 also surfaced pressure here. Mitigation: register separation (narrative voice in Ch. 1; analytical voice in Ch. 6; signpost in Ch. 8).
- **"Memoir dressed as framework"** — surfaced by Character 9 (tenured economics chair) and Character 22 (MFA critic) independently. Flags from multiple characters on the same weakness indicate structural rather than tactical concern. Mitigation canonicalized in §1.11 item 3: framework rigor on the author's own case must equal rigor on coal; counterargument coverage for "memoir dressed as framework" and "self-serving reframing" explicitly required.

### 3.4 Pre-drafting items surfaced

Three items that cannot be deferred to drafting-stage resolution:

1. **NDA review** from healthcare-IT CEO-era engagements. Required before Ch. 6 CEO-perspective case drafting.
2. **Subordinate anonymization protocol** applied. Preferred path: pattern description without identifiable specifics.
3. **First-person discipline** across Ch. 1 / Ch. 6 / Ch. 8 touchpoints. Register separation required by drafting time.

### 3.5 Cascade

- Scope document updated to v1.0.2: §1.2 Ch. 6 description expanded, §1.7 Ch. 7 description refined, new §1.10 (worked-applications distribution across scales), new §1.11 (pre-drafting items), audit table updated.
- Rigor protocol `commons_bonds_rigor_protocol_v1_0_0.md` produced in parallel with v1.0.2 to formalize the 25-test + 25-character suite that had been applied ad-hoc in v1.0.1 and explicitly here.
- Ch. 6 "villain who isn't a villain" frame flagged as open question: carries analytical weight or purely rhetorical? Resolution deferred to Ch. 6 draft gate-check per scope §11.5.

---

## 4. Rigor Pass #3 — producing scope v1.0.3 from v1.0.2

### 4.1 Testing target

Ch. 7 asteroid-miner case as the abundance-fully-stripped worked application. Also surfaced during this pass: the chapter-ordering question (asteroid before vs. after coal miner), which the rigor pass evaluated but did not resolve.

### 4.2 Tests applied

Full rigor suite on Ch. 7 asteroid-miner as full-tier-depth worked application. Full 25-test + 25-character pass.

### 4.3 Findings — Ch. 7 asteroid-miner

**All 25 framework tests pass.** Specific findings worth recording:

- Two-path rigor test passes cleanly. Path 1: allocation asymmetry present (miner bears, investors capture). Path 2 (shield-absence counterfactual): if distance were absent — asteroid miner hypothetically next door to investors — structural incentives would still produce severance. Distance makes severance durable; it doesn't create severance. Shield is a condition for severance persistence, not its cause.
- Merger and primitiveness gates pass. Asteroid-miner case is bilaterally independent from all other worked cases and non-decomposable (uniquely the abundance-fully-stripped case).
- Cross-spectrum positioning: no partisan baggage; space mining is politically neutral.

**Character suite highlights:**

- **Character 6 (Berggruen judge)** — strong positive pressure. Long-horizon institutional thinking with rigorous methodology is the Berggruen Prize's core concern. Strengthens Berggruen placement.
- **Character 25 (grandfather at NASA Langley, legacy coherence)** — positive. Writing rigorously about space extraction frameworks connects to the NASA legacy. Framework honors institutional integrity in a domain with personal resonance.
- **Character 9 (tenured economics chair)** — pressure on "where's the empirical grounding?" Mitigation: asteroid case is methodologically illustrative, not empirically grounded. Grounding comes from the mathematical framework in the Technical Appendix, not from data about an extraction that hasn't yet happened.
- **Character 22 (MFA critic)** — pressure on prose quality. Hypothetical scenarios can read dry or science-fictional. Existing Ch. 7 scaffold uses the Colony Administrator as a character (not just a scenario) — preserve in drafting.
- **Character 14 (Appalachian reader)** — yellow flag (not red). If the asteroid chapter reads as detour from real-world concerns, an Appalachian reader might feel sidelined. Flag connects to chapter-ordering question below. Mitigation: chapter framing must explicitly connect asteroid case back to terrestrial cases.

**Two pre-drafting items for Ch. 7:**

1. Tier activation verification. Claim: all 8 tiers activate cleanly in the asteroid-miner case because abundance is fully stripped. Needs empirical test during drafting — walk each tier explicitly; if any activates weakly, that's a finding about the tier (may not be abundance-gated; may have different activation conditions).
2. Earth-connection framing. The chapter must land the move "the tiers visible here were here all along on Earth, hidden by abundance." If the connection is weak, the chapter drifts toward science fiction.

### 4.4 Findings — chapter-ordering question (asteroid before vs. after coal)

The ordering question was surfaced by Chris's pushback on the Character 14 flag (attack-on-miners concern). The rigor pass evaluated two configurations:

**Option A: current order (coal Ch. 2, asteroid Ch. 7).** Preserves the Abundance Inversion Test's pedagogical arc — readers encounter abundance-present cases first (partial tier visibility), then encounter abundance-stripped case (full visibility), experiencing the *discovery* that hidden tiers were present on Earth all along.

**Option B: reordered (asteroid earlier, coal later).** Addresses the attack-on-miners concern directly. Starts with hypothetical space mining in neutral territory; coal becomes culmination rather than opener.

**Provisional finding: current order is architecturally stronger.** The Abundance Inversion Test's pedagogy is load-bearing on the framework's methodology. Reversed order replaces discovery with explanation. The attack-on-miners concern is real but addressable without reordering:

- Ch. 2 opening can explicitly frame the book's structure (coal is one case among many, not the target)
- Ch. 1 (Plane, IT/knowledge-worker) is the actual opener; readers don't meet miners first
- Ch. 6's dual-position case structurally demonstrates the framework is not one-directional
- Ch. 4 (Norway) follows miner-context within 2–3 chapters as existence-proof counterbalance

**Not ratified.** The ordering question is flagged in scope §11.5 for gate-check resolution after Ch. 2 and Ch. 7 drafts exist in current order. Read both, decide whether mitigations are sufficient; if not, reorder in v1.0.4 or later.

### 4.5 Cascade

- Scope document updated to v1.0.3: §1.2 updated, new §11 (gate-check process), §11.5 flags chapter-ordering as open, change log records Ch. 7 rigor pass.
- Chapter guidance addendum `commons_bonds_chapter_guidance_addendum_ch6_7_8_v1_0_0.md` produced to capture what Ch. 6, Ch. 7, Ch. 8 worked examples must accomplish given this session's scope-level decisions.
- Ch. 7 scaffold verification flagged as parallel task for Chris offline: confirm whether current Ch. 7 scaffold applies full eight-tier depth or only universality validation.

---

## 5. Consolidated findings across all three passes

**Corrections that would have become expensive drift if caught later:**

- PCC reclassification (tier → shielding condition). Would have rippled into the Technical Appendix and Ch. 6 tier decomposition.
- Publishing path reclassification (orthogonal → integral). Would have caused scope decisions to ignore cascade outcomes that should be scope-level revisit triggers.
- Book Two preconditions (three-of-five → necessary+supporting). Would have permitted Book Two authorial configurations that fail the two-path rigor test.
- Ch. 8 coal rationale explicit. Would have been relitigated each time someone asked "why coal for Ch. 8?"

**Pre-drafting items surfaced that would have been expensive to resolve mid-drafting:**

- Subordinate anonymization protocol (Ch. 6).
- NDA review (Ch. 6).
- First-person discipline across touchpoints (Ch. 1 / 6 / 8).
- Tier activation verification (Ch. 7).
- Earth-connection framing (Ch. 7).

**Open questions deferred to gate-check:**

- Ch. 6 "villain who isn't a villain" frame — load-bearing or rhetorical? Confirmed only after Ch. 6 draft exists.
- Ch. 2 + Ch. 7 chapter ordering — does current order hold or does attack-on-miners concern require reorder? Confirmed only after both drafts exist in current order.
- Ch. 8 coal vs. lithium fallback — does coal deepen Ch. 2 or repeat it? Confirmed during Ch. 8 drafting.

**Corrections that held — survived rigor without modification:**

- Three-book split
- Abundance Inversion Test canonical in Book One
- Chapter 8 trim (no full simulation)
- No pre-built reader tools
- Success-criteria canonical sentence (with 13+-year correction)

## 6. Unstated premise surfaced at session close

All three rigor passes above ran on the unstated premise that the abundance layers underlying the Abundance Inversion Test were canonical. That premise was never explicitly tested.

The layers in question (Claude's enumeration during the session): atmospheric, geographic, temporal, institutional, demographic, ecological, political. Chris flagged at session close that his recollection was "8 layers of abundance" — the discrepancy (7 vs. 8) has not been resolved.

The recursive-validation gap means every ratification in this session's outputs depends on an upstream premise that has not itself been ratified. Next session's top priority per handoff v1.24.0 Part 2 runs the framework against itself on the abundance-layer set. If the set changes, this session's outputs cascade (scope §1.4 AIT content, §1.5 PCC placement, Ch. 7 guidance addendum, potentially rigor protocol Group A — dependency order specified in handoff v1.24.0 Part 3).

**Implication for this record:** the three rigor passes documented above are honestly recorded as of 2026-04-21 but cannot be treated as settled until the abundance-layer rigor pass confirms the upstream premise. The passes above did real work and surfaced real corrections; they did not, however, test everything they needed to test.

The catch is itself an application of the operating discipline. Better to surface the recursive gap this session than three sessions from now after more content has been built on top of the unstated premise.

---

## 7. Cross-references

- **Operating core:** preferences, session handoffs through v1.24.0, C9 patch §3.
- **Rigor protocol (what tests exist):** `commons_bonds_rigor_protocol_v1_0_0.md`
- **Scope decisions produced:** `commons_bonds_book_scope_v1_0_3.md` (supersedes v1.0.2, v1.0.1, v1.0.0 from this session)
- **Chapter guidance produced:** `commons_bonds_chapter_guidance_addendum_ch6_7_8_v1_0_0.md`
- **Next session's top priority:** abundance-layer rigor pass (handoff v1.24.0 Part 2)
- **Inputs read during session:**
  - `CommonsBonds_BookOneCommonsBondsPathBookTwo.html` — source of Abundance Inversion Test derivation, Book Two deferral rationale, lone-author vulnerability analysis
  - `commons_bonds_critical_impact_assessment.html` — Apr 19 project-potential analysis
  - `commons-bonds-success-criteria_11.html` — Apr 19 success criteria
  - `CommonsBondsPublishingStrategyConsolidated.html` — Apr 18 publishing strategy
  - `commons-bonds-session-handoff_2026-04-21_1_23_0.html` — prior handoff

---

*End of v1.0.0.*
