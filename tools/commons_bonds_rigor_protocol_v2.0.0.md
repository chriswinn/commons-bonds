# Commons Bonds — Canonical Rigor Protocol

**Version:** 2.0.0 — Pre-Submission Peer Review Suite
**Date:** 2026-04-23
**Status:** Canonical. **Major bump.** Structural reorganization from test-type groups (v1.3.0) to purpose-driven peer-review modules. Every module is runnable standalone; running the full suite constitutes a comprehensive pre-submission peer review the author can hand to the reviewer who comes next.
**Supersedes:** v1.3.0 (2026-04-22) and all prior. See §0 below for the v1.3.0 → v2.0.0 mapping and §20 for the change log.
**Absorption:** All v1.3.0 tests are preserved; none dropped. Numbering reorganized from Tests 1-29 into Modules 1-11 with mapping at §0.2.

---

## §0. The v1.3.0 → v2.0.0 rationale + mapping

### §0.1 Why the restructure

v1.3.0 was organized by test type (Group A framework / §5A standing / Groups B-F / 25-character suite). That organization reflected how the tests evolved, not how the author uses them. When the author asks "is this academically rigorous?" the answer is scattered across Test 26 + Test 27 + Test 18 + Characters 9, 12, 17 + M1-M4. Running rigor produced a dump of findings across all groups when the author usually wanted targeted findings in one domain.

**The v2.0.0 framing:** the suite IS the pre-submission peer review. The author is a first-time book author whose entire pre-submission review process is this suite. Running it in full should give enough confidence to hand the manuscript to a real peer reviewer, editor, publisher, academic audience — without those reviewers finding something the suite missed.

**Module output format shift:** each module produces a **review memo in the voice of a pre-submission peer reviewer** for that domain, not a test-verdict table. The memos aggregate into a **Pre-Submission Peer Review Report** the author can attach to any submission or share with the next reviewer.

### §0.2 Mapping from v1.3.0 → v2.0.0

Every v1.3.0 test is absorbed. Some appear in multiple modules (preserved with cross-references rather than deduplicated — each module must be runnable alone).

| v1.3.0 location | v1.3.0 test | v2.0.0 module |
|---|---|---|
| §5.1 | Test 1 (AIT) | M1 Framework integrity |
| §5.2 | Test 2 (Two-path) | M1 + M2 (case-level) |
| §5.3 | Test 3 (Merger / Primitiveness) | M1 + M6 (academic-methodology) |
| §5.4 | Test 4 (Multi-scale × 2 environments) | M1 + M2 (case-level) |
| §5A.1 | Test 28 (Earning-its-place) | **Standing gate** — §5 |
| §5A.2 | Test 29 (Scaffolding-vs-book-worthy) | **Standing gate** — §5 |
| §6 Test 6 | Trying-to-do-too-much | M3 Book content |
| §6 Test 7 | Cross-spectrum preservation | M3 + M10 (publishing-path reception) |
| §6 Test 8 | Load-bearing vs. scaffolding | M3 (subsumed under standing gates for dimensions) |
| §6 Test 9 | Displacement | M3 Book content |
| §7 Test 10 | Lone-author vulnerability | M9 Risk / exposure |
| §7 Test 11 | Legal exposure | M9 Risk / exposure + M10 (publisher fit) |
| §7 Test 12 | Cross-spectrum attack surface | M10 + M11 (Critics Group G) |
| §7 Test 13 | Career-risk compatibility | M9 Risk / exposure |
| §8 Test 14 | Publisher appeal | M10 Publishing path |
| §8 Test 15 | Noema / Berggruen placement fit | M10 Publishing path |
| §8 Test 16 | Agent interest | M10 Publishing path |
| §8 Test 17 | Target reader recognition | M5 Dinner-table + M10 (audience fit) |
| §8 Test 18 | Competitor / overlap | M7 Originality |
| §8 Test 19 | Decade-out durability | M8 Long-term potential |
| §9 Test 20 | Vocabulary portability | M5 Dinner-table + M8 Long-term |
| §9 Test 21 | Upstream-of-Goal-1 | M8 Long-term potential |
| §9 Test 22 | Direct-to-Goal-2 | M5 Dinner-table + M8 |
| §9 Test 23 | Labor-lawyer-in-2039 | M8 Long-term potential |
| §10 Test 24 | Counterargument coverage | M3 Book content + M6 (academic steelmannability) |
| §10 Test 25 | Steelmannability | M3 + M6 + M7 (originality defense) |
| §10 Test 26 | Falsifiability | M1 + M6 (academic methodology) |
| §10 Test 27 | Empirical grounding | M3 + M6 |
| §11 | 25-character pressure suite | M11 Critic pressure (preserved whole; cross-references to other modules documented) |
| §11.7-11.9 | Sub-batteries (Methodological / Stakeholder / Meta) | M11 sub-batteries (preserved) |

### §0.3 What's new in v2.0.0 (beyond reorganization)

- **M2 Case study tests** — formalized from the case-study audit's implicit procedure. Standalone module. NEW.
- **M4 Craft tests** — structure, narrative arc, prose voice, register consistency, chapter handoffs, flow, line-edit concerns. v1.3.0 had only Character 22 (MFA critic); insufficient for pre-submission peer review. NEW.
- **M9 Risk / exposure tests** — consolidates legal + reputational + career + anonymization + sensitivity-reader into a single pre-submission risk review. v1.3.0 scattered these across Tests 10, 11, 13 + Characters 7, 23 + the indigenous-case §7.1 gates. NEW as consolidated module.
- **M10 Publishing path additions** — comp titles, jacket copy, pitch clarity, platform-and-bio review. v1.3.0 didn't have these. NEW sub-tests.
- **Review-memo output format** per module — replaces test-verdict tables as primary output. Author gets a peer-reviewer's memo, not a matrix.
- **Running modes** — single-module / combined / full / light. v1.3.0 had only full / light. NEW.
- **Sensitivity-reader engagement** elevated to standing gate for content involving marginalized / named / living parties. Previously only in indigenous-case file.

---

## §1. Purpose & perspective

### §1.1 The perspective this protocol operates from

The author is a first-time book author whose entire pre-submission peer-review process is this suite. The AI running the suite is positioned as the reviewer team the author would otherwise have to assemble: a commons-governance-successor academic, a literary agent, a publisher's legal counsel, a Noema / Berggruen editor, a craft reviewer, a sensitivity reader, a critic from each structural reader type the book will encounter.

Running the suite in full should produce enough confidence that:

- The framework claims are defensible under peer review.
- The case studies are doing their specific chapter-level work.
- The content earns its place without scope bloat.
- The prose is at a craft level that will survive editorial review.
- The argument is accessible to intelligent general readers.
- The academic contribution is defensible and the literature is engaged correctly.
- The originality claim holds against existing work.
- The vocabulary is cascade-durable and will still hold in 13+ years.
- The risk profile (legal, reputational, ethical) is known and mitigated where needed.
- The publishing path is viable and marketable in the target venues.
- The 25-character critic pressure surface has been stress-tested.

### §1.2 What the suite does not do

- **Replace actual peer review + editorial review + sensitivity readers.** The suite is pre-submission — it catches what AI review can catch before human reviewers see the work. Sensitivity-reader engagement for marginalized / named parties is a standing gate; the suite cannot perform that engagement itself.
- **Replace legal review.** M9 surfaces legal exposure and flags items for counsel review. It does not provide legal counsel.
- **Guarantee publishability or academic reception.** The suite raises the floor; cascade reception is its own empirical question.

### §1.3 Output: the Pre-Submission Peer Review Report

A full-suite run produces a single deliverable: a **Pre-Submission Peer Review Report** (naming pattern: `commons_bonds_psr_YYYY-MM-DD_v#.#.#.md`). The report contains one review memo per module + a consolidated findings section + pre-submission action items.

---

## §2. How to use

### §2.1 Session start

Upload this file alongside the current session handoff and any relevant context files (chapter drafts, case-study files, audits). The protocol is reference material; it is not modified within a session. If the operating core has been updated since the canonical protocol version, flag the delta before running modules.

### §2.2 Running modes

Four modes supported:

1. **Single-module** — `run: M#` or `run: <module name>`. Produces that module's review memo only. Examples: "run academic rigor tests" (M6), "run originality tests" (M7), "run case study tests for indigenous case" (M2).
2. **Combined** — `run: M# + M#` or list of modules. Produces unioned review memos. Example: "run originality + publishing" (M7 + M10).
3. **Full suite** — `run: full rigor` or `run: pre-submission peer review`. Produces all 11 modules in the standard sequence (§3.2). Output: complete Pre-Submission Peer Review Report.
4. **Light rigor** — `run: light`. Mandatory standing gates (§5) + framework integrity on framework claims + module-appropriate quick-hit questions based on claim type. Abbreviated output.

### §2.3 Standard sequence for full-suite runs

Running order matters. If an earlier module returns major findings, later modules may be deprioritized or the run paused for remediation.

1. **M1 Framework integrity** — if the framework itself doesn't hold, later modules don't matter.
2. **M2 Case study tests** — case-level rigor; runs per-case or per-chapter-case-set.
3. **M3 Book content tests** — does each piece earn its place; serves the argument.
4. **M4 Craft tests** — structural integrity + prose + voice + register.
5. **M5 Dinner-table tests** — accessibility check.
6. **M6 Academic rigor tests** — peer-review survivability.
7. **M7 Originality tests** — novelty claim defense.
8. **M8 Long-term potential tests** — 13+ year durability.
9. **M9 Risk / exposure tests** — legal + reputational + ethical + sensitivity-reader.
10. **M10 Publishing path tests** — cascade viability + marketability.
11. **M11 Critic pressure tests** — final attack-surface review.

### §2.4 A finding is a finding, not a veto

The suite surfaces findings. The author decides response: refine to close the gap, accept as known limitation with explicit handling, or reject the claim/content. All three are legitimate. Silence is illegitimate — a finding that appears in a review memo must be explicitly handled in the author's response.

### §2.5 Pre-Submission Peer Review Report pattern

Each substantial full-suite run produces its own Report. Naming: `commons_bonds_psr_YYYY-MM-DD_v#.#.#.md`. The Report lives in `tools/pre-submission-reviews/` (new folder; parallel to existing `tools/rigor-passes/`). Individual-module runs may be recorded as rigor-pass records in the existing `tools/rigor-passes/` folder if substantial, or kept session-internal if routine.

---

## §3. Standing gates (mandatory at every rigor depth, every module)

Two standing gates apply to **every** piece of content run through **any** module, at **every** rigor depth including light. These are not full modules; they are gates that every module re-runs on its own content as part of module procedure.

### §3.1 Standing Gate A — Earning-its-place (formerly v1.3.0 Test 28)

**Core question:** Does this content, claim, structural element, or finding advance Book One's stated goals (Goal-1 vocabulary adoption / Goal-2 individual-reader use) sufficiently to earn its position against the cost of reader attention and authorial effort?

**Procedure:**

1. **Name the book-scope function.** What specific function does this content serve in Book One (or Book Two / Three where applicable)? "It's useful" is not a function; "it grounds Ch 5's accountability-gap argument at a specific quantitative case" is.
2. **Identify the consumer.** Which chapter / appendix / case file / reader archetype consumes this content?
3. **Verify load-bearing.** Is the content load-bearing on its consumer, or could the consumer function without it?
4. **Apply the removal test.** If removed, would the gap be identifiable (specific argument lost, specific finding lost, specific pattern-match lost) or trivially-filled (sentence reworded, footnote renumbered)?

**Verdicts:**

- **EARNS PLACE** — serves named function for named consumer, load-bearing, identifiable gap on removal.
- **EARNS PLACE WITH REFINEMENT** — specify the refinement.
- **DOES NOT EARN PLACE** — demote to scaffolding, retire, or defer.

### §3.2 Standing Gate B — Scaffolding-vs-book-worthy (formerly v1.3.0 Test 29)

**Core question:** Is this content canonical framework material readers encounter directly (book-worthy — belongs in `core/` or `manuscript/chapters/`), or process / methodology / decision-trail material produced during framework development (scaffolding — belongs in `tools/` or `archive/`)?

**Procedure:**

1. **Identify the audience.** Readers encountering the framework → book-worthy. Future Claude instances, methodology contributors, rigor-pass writers, author-revisiting-decisions → scaffolding.
2. **Check value location.** Is the content's value in-the-content (what it says, defines, teaches) → book-worthy? Or in-the-reasoning-trail (why we decided, what we rejected, what assumptions were made) → scaffolding?
3. **Apply placement principle.** Scaffolding → `tools/` (active), `tools/archive/`, `alignment/decisions/`, `alignment/sessions/archive/`. Book-worthy → `core/`, `manuscript/chapters/`, `research/case-studies/`, `research/literature/bibliography.md`.
4. **Handle mixed content.** Many working documents contain both. Identify each section's type; extract or justify-keep-together.

**Verdicts:**

- **BOOK-WORTHY** — place in `core/` or `manuscript/`.
- **SCAFFOLDING** — place in `tools/` or `archive/`.
- **MIXED — extract + split.**
- **MIXED — keep together with justification.**

### §3.3 Standing Gate C — Sensitivity-reader engagement (NEW v2.0.0)

**Core question:** Does this content involve marginalized peoples, named living individuals, or communities the author is not a member of — in a way that warrants sensitivity-reader engagement before publication?

**Procedure:**

1. **Name the engagement surface.** Which communities / individuals / marginalized positions does the content engage? (Indigenous nations, racial minorities, specific named persons, professional communities the author belongs to, et al.)
2. **Assess the author's standing.** Is the author a member, adjacent member, or non-member of the community being engaged?
3. **Identify the engagement mode.** Is the engagement primary (case study, anchor, dedicated chapter) or secondary (brief reference, illustrative mention)?
4. **Apply the gate.**
   - **Primary engagement + non-member author** → sensitivity-reader engagement non-optional before publication.
   - **Primary engagement + member author** → sensitivity-reader engagement recommended.
   - **Secondary engagement + non-member author** → brief reader engagement recommended; flag for counsel if legal exposure present.
   - **Secondary engagement + member author** → standard pre-submission discretion.

**Verdicts:**

- **CLEAR** — no sensitivity-reader engagement required beyond standard editorial review.
- **ENGAGEMENT RECOMMENDED** — identify candidate readers; engagement happens before publication.
- **ENGAGEMENT NON-OPTIONAL** — specific candidate readers identified; engagement is a pre-publication gate; manuscript does not submit to publisher without it.

**Precedent:** Indigenous land dispossession case (Ch 10 anchor) — Lakota Nation sensitivity reader flagged as non-optional per `research/case-studies/indigenous-land-dispossession.md` §7.1.

### §3.4 Module procedure: running the standing gates

Every module's procedure begins with a one-line application of each standing gate to the content being evaluated, in the form:

> **Standing gates:** Earning-its-place [EARNS / REFINES / FAILS]; Scaffolding-vs-book-worthy [BOOK-WORTHY / SCAFFOLDING / MIXED]; Sensitivity-reader [CLEAR / RECOMMENDED / NON-OPTIONAL].

If any standing gate returns a blocking verdict, the module surfaces that at the top of its review memo and recommends resolution before submission.

---

## §4. Claim classification (simplified from v1.3.0)

The full suite applies to any non-trivial book content. For targeted runs, classify the claim to select the right module(s):

| Claim type | Primary modules | Secondary modules |
|---|---|---|
| **Framework claim** (dimension / tier / methodology) | M1 Framework integrity | M6 Academic rigor + M7 Originality |
| **Case study integration** (case into chapter) | M2 Case study | M3 Book content + M9 Risk / exposure |
| **Content addition** (section / paragraph in chapter) | M3 Book content | M4 Craft + M5 Dinner-table |
| **Prose revision** (line-edit, voice, register) | M4 Craft | M5 Dinner-table |
| **Submission readiness** (manuscript → publisher / agent / academic) | Full suite | — |
| **Pre-publication clearance** | M9 Risk + M10 Publishing path + M11 Critic pressure | M6 Academic + M7 Originality |
| **Novelty / contribution claim** | M7 Originality | M6 Academic rigor |
| **Vocabulary / naming / key term** | M5 Dinner-table + M8 Long-term | M7 Originality |
| **Chapter-level structural change** | Full suite | — |

**Unioning rule:** When multiple categories apply, union the modules. Example: adding a new dimension is framework claim (M1) + content addition (M3) + originality work (M7) + could pressure academic-rigor and long-term modules (M6 + M8). Full suite recommended.

---

## §5. The 11 modules — overview

| # | Module | Core question | Reviewer voice | Output format |
|---|---|---|---|---|
| 1 | Framework integrity (CORE) | Do the equations, AIT methodology, and formal vocabulary hold? | Commons-governance-successor academic | Hybrid (verdict table + reviewer-judgment) |
| 2 | Case study | Does this case do its work for the specific chapter? | Empirical social scientist reviewing a mixed-methods chapter | Hybrid (verdict table per axis + reviewer-judgment) |
| 3 | Book content | Does this content earn its place and serve the argument? | Trade-press editor | Hybrid (verdict table + reviewer-judgment) |
| 4 | Craft | Structure, narrative arc, prose voice, register consistency | Literary craft reviewer / developmental editor | Peer-reviewer memo (prose) |
| 5 | Dinner-table | Can an intelligent non-specialist understand this? | General reader with graduate-school education but no field specialty | Verdict table + brief judgment |
| 6 | Academic rigor | Does this survive peer review in the relevant fields? | Senior academic in the field (political economy / sociology / commons governance) | Peer-reviewer memo (prose) |
| 7 | Originality | What's genuinely new vs. restating existing literature? | Review-article author benchmarking the field | Hybrid (contribution-claim prose + competitor verdict table) |
| 8 | Long-term potential | Will this hold in 13+ years? Cascade durability? | Intellectual-history reader looking back from 2045 | Hybrid (interpretive-lean) |
| 9 | Risk / exposure | Legal, reputational, ethical risks for the author and third parties | Publisher's legal counsel + sensitivity-reader-protocol expert | **Risk register** — finding / reviewer-voice / consequence / solve / mitigate / show-stopper |
| 10 | Publishing path | Cascade viability + marketability + venue fit across 4 endpoint types | Literary agent preparing submission | Hybrid (4-endpoint verdict table + pitch / comps / jacket-copy prose) |
| 11 | Critic pressure | 25-character attack-surface review | The 25 characters from v1.3.0, preserved | Character-voice memos + structural-flag aggregate |

Each module below follows the same template:

- **Reviewer voice + core question.**
- **When to run this module.**
- **Sub-tests within the module** (each with a short procedure).
- **Standing gates line.**
- **Output format** (module-specific per table above).
- **Light-mode abbreviation.**
- **Cross-references to other modules.**

### §5.1 Framework core vs. framework elaboration — critical scope note

**The CORE of the Commons Bonds framework (tested by M1):**

1. **AIT methodology** — abundance-inversion test for identifying scarcity-grounded cost.
2. **RCV formula** — `RCV(R, t₀) = ∫ₜ₀^∞ {[1 − S(t | t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt`
3. **CS equation** — `CS = RCV − B` (cost severance as residual commons value minus accountability bond).
4. **Formal vocabulary** — cost severance / severed cost / residual commons value / accountability bond / civilizational substitutability gap.

**Framework elaboration (NOT tested by M1 — tested by other modules):**

- **10 abundance dimensions** (Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political, Cohesion, Epistemic, Autonomy) — useful taxonomy for chapter organization; not load-bearing on the book's contribution. Tested by M3 (do they earn their place in the book?) + M7 (are they original contributions or restating existing taxonomies?) + M2 (do cases activate them cleanly?).
- **8-tier decomposition** — useful per-case accounting structure. Same treatment as dimensions — tested by M3 + M7 + M8 (does the specific tier structure hold cascade-durable?).
- **Two-path rigor protocol** — primary diagnostic method for case-level analysis. Tested as part of M2 (case study).
- **Merger / primitiveness gates** — dimension-distinctness checks. Tested conditionally when new dimensions are proposed (sub-test within M3 or M7, not a standing M1 gate).
- **Multi-scale × 2 environments** — applied to test universality of the CORE. Tested by M1.5 (universality of core) + M2 (universality of case-level findings).

**Why the distinction matters:** conflating core with elaboration inflates the framework's scope, invites attack on peripheral elements as if they were load-bearing, and obscures which parts of the book the author must defend vs. which parts are useful illustrations the book can compress or restructure. M1 tests the part that must hold for the book to be the book; other modules test whether the elaborations earn their place.

**C9 canonical positioning (preserved from v1.3.0):** AIT is the framework's epistemic core. Dimensions are organizational scaffolding, not load-bearing structure. Dimension additions, mergers, or renames are organizational revisions, not framework-integrity events.

---

## §6. M1 — Framework integrity tests (CORE only)

### §6.1 Reviewer voice

A commons-governance-successor academic — someone in the Ostrom tradition with training in political economy and methodology. Evaluates whether the framework's CORE elements (AIT methodology + RCV formula + CS equation + formal vocabulary + universality claim) are internally coherent, mathematically defensible, and survive methodological peer review.

### §6.2 Core question

Does the framework's CORE — AIT methodology + RCV formula + CS equation + formal vocabulary + universality across scales and environments — hold under methodological peer review?

**Critical scope note:** M1 tests CORE only. The 10 dimensions, 8-tier decomposition, two-path rigor protocol, and merger/primitiveness gates are framework elaboration tested by other modules (M2 / M3 / M7). See §5.1 for the core/elaboration distinction.

### §6.3 When to run

- Pre-submission to any venue where the framework's core claims are load-bearing.
- Methodology-appendix + Ch 6 (methodology chapter) review.
- Any revision to the equations, AIT methodology, or canonical vocabulary.
- Whenever the originality / academic-rigor modules surface contribution-claim concerns that depend on core integrity.
- **Default first gate** in any full-suite run.

### §6.4 Sub-tests

#### M1.1 AIT Falsifiability Gate

**Core question:** Does the AIT methodology hold? Can it correctly distinguish scarcity-grounded cost from non-scarcity-grounded claim?

**Procedure:**

1. Apply AIT to a claim-under-evaluation: name the scarcity the claim depends on; imagine that scarcity inverted (abundance); ask whether the claim persists.
2. If the claim persists under abundance → not scarcity-grounded → **FAIL AIT**.
3. If the claim evaporates under abundance → scarcity-grounded → **PASS AIT**.
4. Cross-check via worked examples (canonical set):
   - Tier 6 Ecological under ecosystem-service abundance → evaporates → PASS.
   - Tier 3 Dynastic under no-temporal-separation → evaporates → PASS.
   - "Existential/Meaning Cost" under abundance → persists → FAIL (not scarcity-grounded).
   - "Immediate Survival Cost" under abundance → redundant with Tier 1 → FAIL (redundancy variant).

**Methodological defense (what a peer reviewer will press):**

- "AIT is unfalsifiable in Popperian sense — inverting scarcity is not observable." Response: AIT is a thought-experiment falsification gate, not an empirical falsification gate. Its function is to discriminate scarcity-grounded cost claims from non-scarcity-grounded claims by counterfactual inversion. Empirical falsification of any specific cost claim (e.g., "Appalachian coal extracted X dollars") is the work of M3.7 + M6.3 + M6.4, not M1.1.
- "AIT could be gamed — call something scarcity that isn't." Response: paired with M1.2 (RCV formula) and M2 (case-level two-path), gaming is exposed because the gamed claim cannot be priced or located in real cases.

**Verdict:** PASS / FAIL / CORROBORATIVE (used alongside other tests as cross-check).

#### M1.2 RCV formula integrity (NEW v2.0.0)

**Core question:** Does the RCV equation `RCV(R, t₀) = ∫ₜ₀^∞ {[1 − S(t | t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt` hold mathematically and produce defensible output against worked-example cases?

**Procedure:**

1. **Mathematical coherence.** Does the integral converge under reasonable parameter assumptions? Does it produce finite, comparable output? Are the units consistent (dollars per resource unit per time unit, integrated to produce dollars per resource unit)?
2. **Variable definition rigor.** For each variable in the formula:
   - **R** (resource): defined precisely; specifies what's being valued.
   - **t₀** (extraction time): defined precisely.
   - **S(t | t₀)** (substitutability function): defined as probability that a functionally-adequate substitute exists at time t given extraction at t₀. Has bounded interpretation [0, 1]. Methodologically defensible (an empirical question, not philosophical).
   - **U(R, t, Q(t))** (stock-dependent utility): defined as utility per unit of remaining resource at time t given remaining stock Q(t). Has documented monotone behavior (rises as Q falls).
   - **E(R, t)** (externality flow): ongoing externality cost at time t. Independent of substitutability.
   - **D(t, t₀)** (discount factor): Weitzman declining-rate framework; bounded behavior under uncertainty.
3. **Worked-example agreement.** Apply formula to canonical cases (McDowell coal, Norway oil with backtest, Deepwater Horizon, Libby vermiculite). Does the formula's output agree with the convergent results from bottom-up damage accounting + real-options pricing? Per Ch 6's three-method convergence: yes, within order-of-magnitude. Document any case where convergence fails.
4. **Boundary case behavior.** Does the formula produce sensible output at boundaries:
   - Perfect substitute (S → 1): foreclosure cost vanishes; only externality tail E remains. Correct.
   - No substitute (S → 0): full foreclosure cost integrated forward. Correct.
   - No externality (E → 0): only foreclosure cost. Correct.
   - Norway-style well-managed extraction with large B: CS small but positive. Correct (per Ch 6 backtest).

**Methodological defense (what a peer reviewer will press):**

- "S(t) is doing enormous work and is unobservable." Response: S(t) is empirically estimable (engineers, materials scientists, energy economists produce substitution timeline estimates routinely). The value of moving from discount-rate framing (philosophical, contested for a century) to substitutability framing (empirical, error bars shrink with research) is an explicit methodological move. Acknowledged at Ch 6 as the framework's most novel and most vulnerable variable; M1.2 confirms it is defensible.
- "U(R, t, Q(t)) requires future-utility estimation." Response: yes — the framework is explicit that future-generation valuation is inherent to the problem; the formula structures the inherent uncertainty rather than eliminating it.
- "The integral may not converge for some parameter sets." Response: the appendix derives convergence conditions; the formula is finite under reasonable assumptions; cases where the integral does not converge are themselves diagnostic of resource categories where the framework is structurally telling us extraction is socially impossible at honest pricing.

**Verdict:** PASS / FAIL / PASS-WITH-REFINEMENT (specify variable / boundary case requiring strengthening).

#### M1.3 CS = RCV − B coherence (NEW v2.0.0)

**Core question:** Does the cost-severance equation `CS = RCV − B` hold structurally? Is the accountability bond B defined precisely enough to apply in real cases?

**Procedure:**

1. **Structural coherence.** CS is defined as the residual after subtracting accountability already in place from the residual commons value. Does the subtraction make conceptual sense? (Yes: if you've already bonded for the cost, your severance is what's left unbonded.)
2. **B definition rigor.** For each canonical case, specify what counts as B:
   - Mining reclamation bonds (pre-extraction posted security).
   - Sovereign wealth funds (Norway GPFG; Alaska Permanent Fund).
   - Litigation settlement funds (Libby asbestos; Deepwater Horizon Gulf restoration).
   - Health-impact trust funds (Black Lung Disability Trust Fund).
   - Insurance reserves.
   - Government-mandated remediation programs.
3. **B = 0 baseline.** For most extraction historically, B = 0 (no bonding instrument was ever required). The formula correctly returns CS = RCV in those cases.
4. **B partial.** For partial-bonding cases, the formula returns CS = RCV − B, capturing the unbonded remainder. Norway backtest: B is large (the GPFG); CS is small but nonzero (the barrel is still gone; the externality tail is still present even if smaller).
5. **Boundary cases.**
   - Sustainably managed renewable resource with full ecosystem accountability: CS ≈ 0. Falsifiable.
   - Highly abundant non-renewable extracted under stringent accountability (construction sand): CS ≈ 0. Falsifiable.
   - Standard fossil-fuel extraction under existing accountability regimes: CS > 0. Empirically observed in every case tested.

**Methodological defense (what a peer reviewer will press):**

- "B is too narrow — should include voluntary corporate provisions, NGO-led mitigation, philanthropic remediation." Response: B is defined as accountability mechanisms that actually flow to cost-bearers. Voluntary provisions count if and only if they reach cost-bearers; otherwise they are extraction-side capture (per blood-diamonds simulated-reattachment pattern in Ch 7).
- "CS could be negative if B exceeds RCV." Response: the framework allows for over-bonding in principle. Empirically, no canonical case shows CS < 0 under existing instruments. If a future jurisdiction over-bonds (e.g., extreme insurance requirements), the formula correctly returns negative CS — this is socially valuable over-investment in accountability, not a framework failure.

**Verdict:** PASS / FAIL / PASS-WITH-REFINEMENT (specify B-definition refinement needed).

#### M1.4 Formal vocabulary integrity (NEW v2.0.0)

**Core question:** Are the framework's canonical terms precisely defined, internally consistent, and doing distinct work?

**Procedure:**

For each canonical term, verify:

1. **Precise definition.** Term has a one-sentence formal definition that distinguishes it from adjacent vocabulary.
2. **Internal consistency.** Term used the same way across chapters, methodology appendix, and case-study files.
3. **Distinct work.** Term cannot be replaced by adjacent vocabulary (existing externality theory, Ostrom commons-governance vocabulary, Harvey accumulation-by-dispossession vocabulary) without loss of precision.
4. **Citability.** Term has the compression to be cited in scholarship without requiring redefinition.

**Canonical terms tested (current set):**

- **Cost severance** — "the act of cutting the cost of extraction loose from the profit of extraction and transferring it to people who had no say in the transaction" (Ch 2 working definition). Tests: distinct from "externality" (cost severance specifies the structural transfer + absent shield; externality is purely economic-theoretic). Distinct from "extraction" (extraction is the act; cost severance is what happens to the costs of the act).
- **Severed cost** — noun form: "a cost that has been detached from its source and displaced onto a third party" (Ch 2). Tests: noun form of the verb construction; carries the specific compression Harvey/Klein/Raworth demonstrate.
- **Residual commons value (RCV)** — defined by the formula. Tests: distinct from Pigouvian externality cost (RCV integrates over time with substitutability weighting; Pigou is point-in-time externality price). Distinct from option-value (RCV includes the externality tail in addition to the foreclosure-option-value).
- **Accountability bond (B)** — "the actual-accountability resources available to cost-bearers" (working definition). Tests: distinct from regulatory penalty (B is what flows to cost-bearers; regulatory penalty may or may not).
- **Civilizational substitutability gap (CSG)** — "the difference between a resource's substitutability for current applications and its substitutability for possible long-term civilizational applications." Tests: distinct from "criticality" in critical-minerals literature (CSG is about temporal and civilizational substitutability, not present strategic priority).
- **Value capture** — paired with cost severance; "the act of extracting worth from a system while declining to absorb the full cost of extraction." Tests: distinct from "profit" (profit is accounting; value capture is structural).
- **Foreclosure cost** — within RCV: cost of permanent unavailability of the resource to future generations.
- **Externality tail** — within RCV: ongoing externality cost after extraction ends.
- **Substitutability function S(t)** — within RCV; defined as probability of adequate substitute existing at time t.

**Methodological defense (what a peer reviewer will press):**

- "These terms restate Pigou / Ostrom / Harvey." Response: M7 Originality test handles this in depth. M1.4 confirms internal consistency only.
- "Vocabulary is too dense; reader can't carry all of it." Response: M5 Dinner-table test handles this. M1.4 confirms precision; M5 confirms portability.

**Verdict:** PASS / FAIL / PASS-WITH-REFINEMENT (specify terms requiring sharpening).

#### M1.5 Universality across scales × environments (rescoped from v1.3.0 Test 4)

**Core question:** Does the CORE (equations + AIT + vocabulary) hold across all relevant scales and both environment types?

**Procedure:**

Apply the CORE at each scale × environment combination. For each cell, ask: can this person / body / firm apply the equations + AIT + vocabulary to identify and price cost severance in their actual situation?

| Scale | Earth exemplar | Off-Earth exemplar | Core works? |
|---|---|---|---|
| Individual | Worker evaluating job; student evaluating career; cost-burdened renter | Asteroid miner; Mars-colony crew | [PASS / FAIL] |
| Community | Commons administrator; tribal council; HOA; CBF | Mars-colony administrator; orbital-habitat civic authority | [PASS / FAIL] |
| Government | Legislature; sovereign wealth fund; regulator; municipal broadband authority | Outer Space Treaty signatory; celestial-mining oversight | [PASS / FAIL] |
| Corporate | Board; CEO; sustainability officer | Asteroid-mining firm; orbital-services operator | [PASS / FAIL] |

**Failure handling:**

- A claim that passes at all Earth scales but fails at any off-Earth scale → fails the universality claim.
- A claim that fails at one Earth scale → either (a) fixable within the claim (refine), (b) fundamental (reject or scope explicitly), or (c) at a scale the framework does not claim to serve (document scoping).

**Do not silently drop scales.** A claim scoped to individual-only should say so; a claim that happens to fail at government scale but silently presents as universal is a framework-integrity violation.

**Verdict:** PASS-AT-ALL-SCALES / SCOPED (specify which scales) / FAIL (specify scale + nature of failure).

### §6.5 What M1 does NOT test (relocated to other modules)

- **Two-path rigor (allocation-symmetry + shield-absence)** — primary diagnostic for case-level analysis. Tested by **M2** (case study tests).
- **Merger / primitiveness gates** — dimension-distinctness checks. Tested conditionally when new dimensions are proposed; absorbed as sub-test in **M3** or **M7** depending on whether the proposal is content-addition or originality-claim.
- **10 dimensions + 8-tier decomposition** — framework elaboration. Tested by **M2** (do cases activate them cleanly?) + **M3** (do they earn their place in the book?) + **M7** (are they original contributions or restating existing taxonomies?) + **M8** (cascade-durability of specific tier names).
- **Empirical grounding of specific cases** — tested by **M2** (case study) + **M3** (book content) + **M6** (academic rigor).

### §6.6 Standing gates (run per §3)

Apply Earning-its-place + Scaffolding-vs-book-worthy + Sensitivity-reader to the framework content being evaluated.

### §6.7 Output format — Hybrid (verdict table + reviewer-judgment)

> **M1 Framework Integrity Review (CORE) — [content / claim being evaluated]**
>
> **Standing gates:** [one-line verdict on each of three gates].
>
> **Verdict table:**
>
> | Sub-test | Verdict | Notes |
> |---|---|---|
> | M1.1 AIT falsifiability | [PASS / FAIL / CORROB] | |
> | M1.2 RCV formula integrity | [PASS / FAIL / PASS-WITH-REFINEMENT] | |
> | M1.3 CS = RCV − B coherence | [PASS / FAIL / PASS-WITH-REFINEMENT] | |
> | M1.4 Formal vocabulary integrity | [PASS / FAIL / PASS-WITH-REFINEMENT] | |
> | M1.5 Universality across scales × environments | [PASS / SCOPED / FAIL] | |
>
> **Reviewer's judgment (commons-governance academic voice):**
>
> One-paragraph synthesis. Does the CORE hold? Are the equations defensible? Is the methodology citable? Where does the strongest peer-review pressure land?
>
> **Findings warranting cross-cutting format (per §17):** Any sub-test result that warrants the FINDING / Reviewer voice / What this means / SOLVE / MITIGATE / SHOW-STOPPER format goes here as a separate section. Default for findings rated PASS-WITH-REFINEMENT or FAIL.
>
> **Recommendation:** [Pass / Pass-with-refinement (list refinements) / Refer-back-to-author / Fail].

### §6.8 Light mode

M1.1 + M1.4 mandatory; M1.5 abbreviated to "does the CORE work at individual + government Earth scale, with an off-Earth sanity check"; M1.2 + M1.3 only if equation-level revision is on the table.

### §6.9 Cross-references

- M2 Case study runs two-path rigor at case level (relocated from v1.3.0 framework-level testing).
- M3 Book content tests whether dimensions and tiers earn their place in the book.
- M6 Academic rigor re-reviews the methodological defense of AIT + RCV against field-specific peer-reviewer pressure.
- M7 Originality asks: is the AIT methodology + RCV formulation a distinctive contribution, or extension of Polanyi / Ostrom / externality theory?
- §5.1 framework core vs. elaboration scope note — load-bearing context for M1.

---

## §7. M2 — Case study tests

### §7.1 Reviewer voice

An empirical social scientist reviewing a mixed-methods chapter that deploys case studies to support a structural claim. Evaluates dimension activation, case-level rigor (AIT + two-path at case level), chapter fit, register fit, and legal / ethical exposure of named parties.

### §7.2 Core question

Does this case do its specific work for the specific chapter it inhabits?

### §7.3 When to run

- Any new case-study file enters the canonical set.
- Any case-study integration into a chapter draft (full or brief anchor).
- Chapter rewrite where case use is being revised.
- Before submission where any case carries argumentative weight.

### §7.4 Sub-tests

#### M2.1 Dimension activation

Which of the 10 canonical dimensions does the case activate, at what intensity?

**Procedure:** Name primary dimensions (2-4 typically). Name secondary dimensions. Flag any case activating fewer than 3 dimensions — may be under-weight for anchor use. Flag any case activating 7+ primarily — may be over-weight and risking chapter scope bloat (unless explicitly load-bearing, like Appalachian coal or indigenous dispossession).

**Verdict:** COVERAGE-APPROPRIATE / UNDER-WEIGHT (flag chapter consequences) / OVER-WEIGHT (flag scope consequences).

#### M2.2 AIT at case level

Does the case demonstrate scarcity-grounded cost severance? Apply M1.1 procedure at case-level specificity.

**Verdict:** PASS / FAIL / PARTIAL (specify which dimensions / tiers fail AIT at this case's parameters).

#### M2.3 Two-path rigor at case level (PRIMARY case-level diagnostic — relocated from v2.0.0 M1 in mid-revision)

**Source:** Originated in `alignment/patches/c5_two_path_rigor.md` (C5 patch, 2026-04-20). v1.3.0 placed two-path in framework-level Group A; v2.0.0 mid-revision relocates it here as the primary case-level diagnostic, since two-path's actual function is per-case analysis, not framework-level testing.

**Canonical statement:** The Commons Bonds rigor test operates on two paths. Path 1 (allocation symmetry) tests whether the claim correctly identifies who captures value and who bears cost, and whether that asymmetry is structural. Path 2 (shield absence) tests whether the claim correctly identifies the distance condition that prevents the asymmetry from being recognized or corrected. A claim that passes Path 1 but not Path 2 identifies a real harm but cannot explain why it persists. A claim that passes Path 2 but not Path 1 names a structural condition but cannot locate the cost. Rigor requires both paths.

**Path 1 — Allocation Symmetry.** For the case under evaluation:

- Who captures value? (Identify explicitly — a person, role, firm, or class; not an abstraction.)
- Who bears cost? (Identify explicitly, at the same level of specificity.)
- Is the asymmetry structural? (Yes if derived from allocation architecture; no if reducible to individual moral failure, bad luck, or transient market condition.)
- Is the tier assignment unambiguous? (Ambiguous-by-design = FAIL.)

**Verdict on Path 1:** PASS / FAIL / CONDITIONAL.

**Path 2 — Shield Absence.** For the case under evaluation:

- What is the shield? Types: epistemic, institutional, political, fiduciary, spatial, temporal, **consent-normalization**.
- Is the shield structural? (Persists with full knowledge = structural.)
- Does the chapter / case-file correctly name the shield? (Unnamed shields cannot be dissolved.)
- Does the architecture of the case-presentation itself create a new shield? (Serious failure — e.g., case framed in a way that lets reader switch-argue between tiers.)

**Consent-normalization shield (preserved from v1.2.1):** Individual consent, when treated by the surrounding social/legal/institutional framework as terminally closing the accounting — "they chose it, no one owes them anything" — operates as a structural social shield even when individual awareness is complete. Particularly relevant for Institutional, Temporal, and Autonomy dimension cases (knowledge-worker case, miner-chose-that-work case, cost-burdened-renter case).

**Verdict on Path 2:** PASS / FAIL / CONDITIONAL.

**Combined verdict:** Both paths PASS → passes two-path. Either path FAIL → fails two-path. Both CONDITIONAL → define the execution condition measurably.

**Failure signature worth remembering:** The worst kind of Path 2 failure is when the architecture of the claim itself creates a new shield (e.g., parallel taxonomies that enable switch-arguing). In the case-level application: when the case is presented in a way that lets the reader reassign the cost to a different actor, the case has accidentally generated a new shield.

#### M2.3a Merger / primitiveness conditional (NEW — applies only when case work is proposing a new dimension)

When a case study is being used to argue for a new dimension addition (rare; e.g., during naming-cohort work), the merger and primitiveness gates apply:

- **Merger gate (outward):** Does the candidate dimension substantially overlap with an existing dimension? Test by searching for bilateral independence cases — instances where one is abundant and the other scarce, in both directions. If independence cases don't exist in both directions, merger is indicated.
- **Primitiveness gate (inward):** Does the candidate reduce to a composition of existing dimensions? Test by decomposing revealed costs and checking whether each is already priced by an existing dimension. Clean decomposition = redundant.

**When this sub-test does NOT apply:** standard case-study integration into existing dimension structure. Most M2 runs skip M2.3a entirely.

**Verdict (when applied):** PASS / FAIL.

#### M2.4 Chapter fit

Does the case serve the chapter's specific function? Alternatives the case-study audit uses:

- **Anchor:** primary demonstrator; chapter's central worked example. (McDowell coal in Ch 2.)
- **Mirror:** structural parallel to the anchor at a different geography / industry. (Nigeria / Niger Delta in Ch 4.)
- **Stress-test entry:** universality or edge-case exemplar. (Asteroid iron, blood diamonds in Ch 7.)
- **Brief anchor:** 1 paragraph + referenced cross-links. (Feudalism / Egypt / Qin in Ch 7; indigenous Lakota in Ch 10.)
- **Reachable-horizon companion:** demonstrates the architecture is operationally achievable. (Alaska / Chattanooga / Mondragon / Vienna in Ch 9.)
- **Cross-chapter thread:** appears in multiple chapters serving different functions. (McDowell coal in Ch 2 anchor + Ch 6 convergence table + Ch 8 tier-worked.)

**Procedure:** Name the intended function. Verify the case actually performs it. Flag cases inflated beyond their function (scope bloat) or under-developed for their function (chapter carries weight the case doesn't support).

**Verdict:** FITS / FITS WITH REFINEMENT / MISFIT (recommend relocation or removal).

#### M2.5 Register fit

Does the case-prose register match the chapter's register? Ch 10 is Register 1 (pure voice, no data); Ch 5 + Ch 6 are Register 2 (data-bearing); Ch 7 is mixed (Register 2 with Register 1 entry points). A case whose prose breaks register for its chapter will jar the reader.

**Procedure:** Read the case prose as it appears in the chapter. Does it match surrounding voice? Does it use data where the chapter is Register 1? Does it omit data where the chapter is Register 2?

**Verdict:** REGISTER-FIT / REQUIRES REVISION (specify) / REGISTER-MISMATCH (relocate).

#### M2.6 Legal / ethical exposure per case

Per case, identify:

- **Named living persons.** Each requires clearance: direct consent, public-figure doctrine coverage, or anonymization.
- **Named corporations / institutions.** Defamation risk assessment. Standard: public records + cited sources adequate; internal-documents-from-author's-professional-history require NDA review.
- **Marginalized communities.** Sensitivity-reader engagement gate (Standing Gate C). Non-optional for non-member primary engagement.
- **Tribal nations / indigenous peoples.** Treaty-specific and community-specific considerations. Engagement mode protocols per `research/case-studies/indigenous-land-dispossession.md` §7.1.

**Verdict:** CLEAR / CLEARS-WITH-PRE-PUBLICATION-WORK (specify) / BLOCKS-SUBMISSION-WITHOUT-REMEDIATION.

#### M2.7 Cross-spectrum per case

Does the case invite attack from specific political / industry / academic directions that the chapter doesn't anticipate? Different from M11 Critic pressure (which runs per-chapter); this is per-case check on the cross-spectrum positioning.

**Procedure:** Name the most likely attack directions for this case. Verify chapter handles them or the case file flags them for handling elsewhere.

**Verdict:** HANDLED / NEEDS HANDLING (specify where) / STRUCTURAL WEAKNESS (requires chapter revision or case replacement).

### §7.5 Standing gates (run per §3)

Earning-its-place per case + Scaffolding-vs-book-worthy (case-study files are book-worthy; rigor-pass records about cases are scaffolding) + Sensitivity-reader (specific to cases engaging marginalized / named parties).

### §7.6 Review memo output format

> **M2 Case Study Review — [case name] in [chapter]**
>
> **Standing gates:** [one-line each].
>
> **Dimension activation:** [primary / secondary / intensity]. Verdict: [coverage].
>
> **AIT at case level:** [scarcity / abundance-inversion result]. Verdict.
>
> **Two-path at case level:** Path 1 / Path 2 findings. Verdict.
>
> **Chapter fit:** [function served / performed?]. Verdict.
>
> **Register fit:** [match? revision needed?]. Verdict.
>
> **Legal / ethical exposure:** [per named party]. Verdict + pre-publication items.
>
> **Cross-spectrum:** [attack-direction check]. Verdict.
>
> **Reviewer's judgment:** Peer-review-voice summary. Whether the case does what the chapter needs it to do, and what would strengthen its placement.
>
> **Recommendation:** [Integrated-as-is / Refine-before-submission / Relocate / Remove from chapter].

### §7.7 Light mode

Dimension activation + chapter fit + standing gates mandatory; AIT + two-path at case level only if case is new; register-fit by reading one paragraph of case prose in the chapter; legal / ethical exposure by named-party scan.

### §7.8 Cross-references

- M1 Framework integrity re-runs framework tests on the canonical-framework-level material the case is instantiating.
- M3 Book content re-asks: does the case earn its place in the chapter.
- M9 Risk / exposure formalizes the named-party and marginalized-community exposure analysis.

---

## §8. M3 — Book content tests

### §8.1 Reviewer voice

A trade-press editor reading a manuscript for scope, argument progression, counterargument coverage, and content-quality. Evaluates whether each section earns its place, whether chapters stay focused without scope bloat, and whether the content is at a level of quality the editor will be comfortable sending to copy-edit.

### §8.2 Core question

Does each piece of content earn its place and advance the book's argument?

### §8.3 When to run

- Any new content addition to a drafted chapter.
- Any chapter-level structural change (new section, section removal, sequencing change).
- Full-suite submission readiness.

### §8.4 Sub-tests

#### M3.1 Trying-to-do-too-much (formerly v1.3.0 Test 6)

Does this increase chapter or book load without proportionate utility? A scope expansion must earn its position against displacement.

**Procedure:** Name what is added. Name what it displaces (attention, length, cross-reference burden). Compare utility added vs. displacement cost.

**Verdict:** PROPORTIONATE / OVER-WEIGHT (recommend compression or removal) / UNDER-WEIGHT (flag whether more development is warranted).

#### M3.2 Displacement test (formerly v1.3.0 Test 9)

What currently-planned content gets pushed out to make room for this? An addition without displacement is rare; most require something to shrink or move.

**Procedure:** Identify the displacement. Confirm the displaced content is either retirement-appropriate (scope reduction) or relocation-appropriate (moves to another chapter / Book 2 / scaffolding).

**Verdict:** DISPLACEMENT IDENTIFIED AND HANDLED / NO DISPLACEMENT IDENTIFIED (likely scope-bloat risk) / DISPLACEMENT AMBIGUOUS (specify).

#### M3.3 Load-bearing vs. scaffolding within content (formerly v1.3.0 Test 8)

Some content is structural (argumentative); some is organizational (section headers, cross-references, signposting). Organizational content is cheap; structural content requires a higher bar.

**Procedure:** Per content block, assess: is this structural (advances an argument, introduces a term, supports a claim) or organizational (helps the reader navigate)?

**Verdict:** STRUCTURAL (holds to structural standard) / ORGANIZATIONAL (light touch; trim if not needed) / MIXED.

#### M3.4 Counterargument coverage (formerly v1.3.0 Test 24)

Are the counterarguments this material invites identified and addressed? Especially: "memoir dressed as framework," "self-serving reframing," "selective case selection," "left / right partisan critique," "cheap energy lifted billions," "miners chose that work."

**Procedure:** Name the likely counterarguments for this content. Verify each is handled: either within the content, cross-referenced to where it's handled, or flagged as deliberate-out-of-scope.

**Verdict:** COVERED / PARTIAL (specify gaps) / UNCOVERED (recommend addition or scoping).

#### M3.5 Empirical grounding (formerly v1.3.0 Test 27)

Is each claim documented or asserted? Asserted claims require either explicit scoping ("illustrative," "argued") or upgrade to documented.

**Procedure:** Scan content for specific numbers, dates, attributions. For each, verify source is cited or citable. For each un-grounded claim, flag for either citation addition or explicit scoping.

**Verdict:** GROUNDED / GAPS IDENTIFIED (list) / REQUIRES SOURCING PASS BEFORE SUBMISSION.

#### M3.6 Steelmannability within content (formerly v1.3.0 Test 25 at content level)

Can the strongest critic engage with this content, or does it rely on opponents being weaker than they would be?

**Procedure:** Identify the content's strongest critic. Read the content from that critic's position. Does the content handle the critic's best version of the objection?

**Verdict:** STEELMAN HANDLED / STRAWMAN ONLY (requires strengthening) / CRITIC WOULD WIN (structural weakness — recommend content revision or scoping).

#### M3.7 Falsifiability of content-level claims (formerly v1.3.0 Test 26, content-level)

Can specific content claims be tested empirically? What would disconfirm them?

**Procedure:** Per claim, state what would disconfirm. If nothing could disconfirm, flag — the claim is making a definitional or rhetorical move, not an empirical one. Both are legitimate, but the claim should be scoped accordingly.

**Verdict:** FALSIFIABLE / DEFINITIONAL (scope explicitly) / UNFALSIFIABLE-AND-UNCLEAR (flag for revision).

### §8.5 Standing gates (run per §3)

Earning-its-place (per content block) + Scaffolding-vs-book-worthy (especially when audit surfaces a case-study file's decision trail bleeding into a chapter) + Sensitivity-reader (per Standing Gate C).

### §8.6 Review memo output format

> **M3 Book Content Review — [content block being evaluated]**
>
> **Standing gates:** [one-line each].
>
> **Trying-to-do-too-much (M3.1):** [added / displaced]. Verdict.
>
> **Displacement (M3.2):** [displacement identified / handling]. Verdict.
>
> **Load-bearing vs. scaffolding (M3.3):** Verdict.
>
> **Counterargument coverage (M3.4):** [counterarguments named / handled where]. Verdict.
>
> **Empirical grounding (M3.5):** [grounded / gaps]. Verdict.
>
> **Steelmannability (M3.6):** [strongest critic / content handles their best version?]. Verdict.
>
> **Falsifiability (M3.7):** Verdict.
>
> **Reviewer's judgment:** Editor-voice summary.
>
> **Recommendation:** [Publication-ready / Refine before submission / Substantial revision required].

### §8.7 Light mode

Standing gates + M3.1 + M3.4 mandatory. Others conditional on content type.

### §8.8 Cross-references

- M4 Craft re-reviews for prose / structure / voice at a different register.
- M6 Academic rigor re-asks: does this content pass methodological peer review in the field.
- M9 Risk / exposure handles named-party exposure.

---

## §9. M4 — Craft tests (NEW v2.0.0)

### §9.1 Reviewer voice

A literary craft reviewer / developmental editor evaluating the book as a work of narrative non-fiction. Reads for: structural integrity of the argument arc, chapter-to-chapter handoffs, prose voice consistency, register consistency within and across chapters, scene-and-summary balance, flow, line-edit concerns, the difference between writing-that-serves-the-argument and writing-that-is-clear-but-mechanical.

### §9.2 Core question

Is the book at a craft level that will survive editorial review and land with readers as a work of non-fiction prose, not a research report?

### §9.3 When to run

- Whole-manuscript or chapter-level submission readiness.
- After substantial content additions (new sections may break register or flow).
- Before Noema / Berggruen / trade-press submission.
- When Character 22 (MFA critic) flags pressure in M11.

### §9.4 Sub-tests

#### M4.1 Argumentative arc

Does the book's argument build across chapters? Does each chapter advance the argument, or are there chapters that repeat / digress / could be compressed?

**Procedure:** State each chapter's argumentative contribution in one sentence. Flag any chapter whose contribution is opaque or duplicative.

**Verdict:** ARC-SOUND / REORDERING NEEDED (specify) / CHAPTER-LEVEL COMPRESSION / CHAPTER-LEVEL EXPANSION.

#### M4.2 Chapter-to-chapter handoffs

Does each chapter's close set up the next? Does each chapter's open reward readers who followed from the prior chapter?

**Procedure:** Read the last ¶ of chapter N and the first ¶ of chapter N+1 as a pair. Does the handoff work?

**Verdict:** HANDOFF-STRONG / HANDOFF-ADEQUATE / HANDOFF-ROUGH (specify revision).

#### M4.3 Prose voice consistency

Does the book read as written by one author, in one voice? A book with voice-shifts between chapters (some sections read like academic prose, others read like memoir, others read like policy memo) fractures the reader's experience.

**Procedure:** Read one paragraph from each of three chapters. Does a shared voice emerge? Does any chapter read as imported-from-elsewhere?

**Verdict:** VOICE-CONSISTENT / DRIFT DETECTED (specify chapter / section) / MULTIPLE-VOICE (specify whether structural or editorial-cleanup).

#### M4.4 Register consistency

Book 1's register architecture:
- **Register 1:** Voice-led, scene-and-observation-based, no data / formulas / tables. Ch 1, Ch 3, Ch 10. Entry points in other chapters.
- **Register 2:** Data-bearing, argument-focused, with Register 1 entry points for each new concept. Ch 2, Ch 4, Ch 5, Ch 8, Ch 9.
- **Register 3:** Methodological / formal. Ch 6 (heaviest); methodology-appendix sections.

**Procedure:** Per chapter, verify register matches its chapter-type. Flag register drifts. Verify Register 2 and Register 3 chapters have Register 1 entry points at each new concept.

**Verdict:** REGISTER-ALIGNED / DRIFT (specify) / ENTRY-POINTS MISSING (flag).

#### M4.5 Scene-and-summary balance

Narrative non-fiction works when scene and summary are balanced. Too much summary → reads as textbook. Too much scene → argumentative build is lost.

**Procedure:** Per chapter, estimate scene-vs-summary ratio. Flag imbalance.

**Verdict:** BALANCED / SCENE-HEAVY / SUMMARY-HEAVY.

#### M4.6 Prose quality (line-edit readiness)

Sentence-level concerns that will slow a copy-editor: repetition, mechanical-grammar tics, overuse of em-dashes, paragraphs that could compress or split, sentences that could clarify.

**Procedure:** Sample three paragraphs from each chapter. Line-edit-level notes. Aggregate common patterns.

**Verdict:** PROSE-READY / LINE-EDIT-READY-AFTER-SMALL-REVISIONS / REQUIRES SUBSTANTIVE PROSE PASS.

#### M4.7 Draft preamble / postamble / AI-commentary check (Commons-Bonds-specific)

Several drafts in `manuscript/chapters/` were generated inline and retain AI-produced preambles or postambles ("Here's the chapter. I noted these things..."). These are scaffolding, not chapter prose; they inflate word counts and must be stripped before submission.

**Procedure:** Scan each chapter draft file for preamble / postamble / inline-commentary. Identify content-to-strip.

**Verdict:** CLEAN / STRIP-REQUIRED (list specific sections) / MIXED-REQUIRES-EXTRACTION.

### §9.5 Standing gates (run per §3)

Earning-its-place + Scaffolding-vs-book-worthy (especially M4.7 — drafts contain scaffolding that needs extraction) + Sensitivity-reader (register discipline around marginalized-party content; per indigenous case §7.1 humane-and-precise discipline, register is a sensitivity-reader concern).

### §9.6 Review memo output format

> **M4 Craft Review — [chapter or whole manuscript]**
>
> **Standing gates:** [one-line each].
>
> **Argumentative arc (M4.1):** [sentence per chapter]. Verdict.
>
> **Handoffs (M4.2):** [per-handoff findings]. Verdict.
>
> **Voice consistency (M4.3):** Verdict + drift flags.
>
> **Register consistency (M4.4):** Verdict + drift flags.
>
> **Scene-and-summary balance (M4.5):** [per chapter]. Verdict.
>
> **Prose quality (M4.6):** Sample-paragraph notes + patterns. Verdict.
>
> **Preamble / postamble strip (M4.7):** [per chapter]. Verdict.
>
> **Reviewer's judgment:** Craft-reviewer voice summary.
>
> **Recommendation:** [Editorial-ready / Substantive prose pass before submission / Developmental-edit pass before submission].

### §9.7 Light mode

M4.4 register consistency + M4.7 preamble strip mandatory; others by judgment.

### §9.8 Cross-references

- M5 Dinner-table re-asks whether accessibility is preserved under the craft register.
- M11 Critic pressure Character 22 (MFA critic) is this module's external cross-check.

---

## §10. M5 — Dinner-table tests

### §10.1 Reviewer voice

A general reader with graduate-school-level education but no specialty in the book's field. Smart, curious, unwilling to grind through prose that doesn't earn its difficulty. Willing to learn new vocabulary if it arrives with enough scaffolding.

### §10.2 Core question

Can an intelligent non-specialist understand this, and can the vocabulary compress cleanly enough to travel beyond the book?

### §10.3 When to run

- Any new term, dimension name, or tier name entering canonical vocabulary.
- Introduction, conclusion, and chapter-opener prose.
- Any essay / op-ed / pitch derived from the book.
- Before Noema submission (Noema's audience is the dinner-table reader at high intelligence).

### §10.4 Sub-tests

#### M5.1 Dinner-table test (core)

Can this be explained at a dinner table in 60 seconds?

**Procedure:** Compress the content to a 2-4 sentence explanation. Verify the explanation is stand-alone (doesn't require another 60 seconds of back-reference). Verify it says something new to the listener (not a truism).

**Verdict:** DINNER-TABLE-READY / REQUIRES TWO-LAYER EXPLANATION (flag as accessibility concern) / REQUIRES FRAMEWORK-PRIMED LISTENER (flag as non-general-reader content).

#### M5.2 Vocabulary portability (formerly v1.3.0 Test 20)

Can the content's key terms be compressed into citable phrases that travel?

**Procedure:** Identify the content's key terms. Can each be stated in ≤3 words in a way that retains meaning? Harvey: "accumulation by dispossession" (3 words); Klein: "disaster capitalism" (2 words); Raworth: "doughnut economics" (2 words); Commons Bonds candidates: "cost severance" (2 words), "severed cost" (2 words), "residual commons value" (3 words).

**Verdict:** PORTABLE / NEARLY-PORTABLE (recommend compression) / UNPORTABLE (flag vocabulary concern).

#### M5.3 Target reader recognition (formerly v1.3.0 Test 17)

Can the intended reader pattern-match their situation to this content?

**Procedure:** Name 2-3 intended reader archetypes (labor lawyers, community organizers, graduate students, individual workers, knowledge workers). For each, verify the content contains a moment of pattern-match recognition.

**Verdict:** RECOGNIZES / PARTIAL (specify which archetypes don't recognize) / DOES NOT RECOGNIZE (structural accessibility problem).

#### M5.4 Jargon vs. scaffolded-vocabulary check

Is every new term introduced with enough context that a reader encountering it for the first time can carry it forward? Or does the content assume reader-knowledge the reader may not have?

**Procedure:** Per new term, verify there is a plain-English definition or ostensive example at or before first use.

**Verdict:** SCAFFOLDED / PARTIAL (list unscaffolded terms) / ASSUMES SPECIALIST KNOWLEDGE.

### §10.5 Standing gates (run per §3)

Standard three gates.

### §10.6 Review memo output format

> **M5 Dinner-Table Review — [content being evaluated]**
>
> **Standing gates:** [one-line each].
>
> **Dinner-table test (M5.1):** [60-second compression]. Verdict.
>
> **Vocabulary portability (M5.2):** [per key term: 3-word compression possible?]. Verdict.
>
> **Target reader recognition (M5.3):** [per archetype]. Verdict.
>
> **Jargon / scaffolded-vocabulary (M5.4):** [per new term]. Verdict.
>
> **Reviewer's judgment:** General-reader voice summary. Can the reader walk away able to explain this to a friend? If not, what's in the way?
>
> **Recommendation:** [Accessible / Scaffolding needed / Simplification pass required].

### §10.7 Light mode

M5.1 + M5.2 mandatory.

### §10.8 Cross-references

- M4 Craft — register discipline (Register 1 entry points at each new concept) is how dinner-table accessibility is preserved.
- M8 Long-term potential — vocabulary portability is load-bearing on cascade durability.

---

## §11. M6 — Academic rigor tests

### §11.1 Reviewer voice

A senior academic in the field (political economy / sociology / commons governance / intergenerational-justice philosophy). Has reviewed for top journals and one university press in the field. Evaluates methodological rigor, literature engagement, empirical grounding, and whether the work contributes to the field or restates existing arguments.

### §11.2 Core question

Will this survive peer review in the relevant academic fields, and will it be citable by future scholars in the tradition?

### §11.3 When to run

- Pre-submission to any academic-adjacent venue (Noema, Berggruen, academic press).
- Methodology-appendix + Ch 6 (methodology chapter) review.
- Before soliciting blurbs from academic figures.
- Any time M11 Character 9 (tenured econ chair), 12 (grad student), or 17 (Ostrom scholar) flags pressure.

### §11.4 Sub-tests

#### M6.1 Methodological defense

Does the methodology — AIT + two-path + merger/primitiveness + multi-scale — hold as methodology (not just as framework)? Can the author defend the choice of these specific tests, against a reviewer asking "why these and not X?"

**Procedure:** Per methodology element, state the defense: what problem the element solves, what alternatives were considered, why this one was chosen. Engage the reviewer's likely alternatives (e.g., for AIT: revealed preference; for two-path: allocation-only or shield-only; for multi-scale: Earth-only; for merger/primitiveness: composition-indifferent dimensioning).

**Verdict:** DEFENSIBLE / PARTIAL (specify which elements lack defense) / WEAK DEFENSE (requires methodology-appendix revision).

#### M6.2 Literature engagement

Does the book engage the correct literatures correctly? Key fields:

- **Commons governance (Ostrom tradition):** Ostrom's *Governing the Commons*, Harvey's *New Imperialism*, Heller's *Tragedy of the Anticommons*. The author positions as extending Ostrom into intergenerational scale.
- **Externality theory / environmental economics:** Pigou, Coase, Nordhaus, Stern, Weitzman. Ch 6 engages Nordhaus, Stern, Weitzman directly.
- **Political economy of extraction:** Harvey, Klein, Raworth. Ch 10 positions relative to Harvey's "accumulation by dispossession."
- **Intergenerational justice:** Rawls, Parfit, Broome, Gosseling. Ch 10 engages Camus; should explicitly engage Parfit on personal identity / future-generation moral status at some point.
- **Settler-colonial studies (indigenous dispossession):** Dunbar-Ortiz, Wolfe, Coulthard, Simpson, Kimmerer. Ch 10 names these.

**Procedure:** Per relevant field, verify the canonical sources are engaged. Flag any field where engagement is absent or weak.

**Verdict:** ENGAGED / GAPS IDENTIFIED (specify) / ENGAGEMENT-WEAK (requires literature-review pass).

#### M6.3 Falsifiability (beyond AIT) (formerly v1.3.0 Test 26)

AIT (M1.1) is the framework's falsifiability gate. M6.3 asks: beyond AIT, are the book's empirical claims falsifiable? What would disconfirm them?

**Procedure:** Per empirical claim (e.g., Ch 2's 33-122× IPG for McDowell coal; Ch 5's 10M foreclosure figure; Ch 6's convergence table), state what evidence would disconfirm. Flag any claim without a disconfirmation condition.

**Verdict:** FALSIFIABLE / UNFALSIFIABLE BUT SCOPED CORRECTLY / UNFALSIFIABLE AND UNCLEAR (flag).

#### M6.4 Empirical grounding (formerly v1.3.0 Test 27)

At the academic-rigor level, empirical grounding means: every quantitative claim has a primary source; every secondary source has a primary-source trace possible; every named case has citable documentation.

**Procedure:** Pass-through the book / content. Per number / date / attribution: traceable to primary source? Flag gaps.

**Verdict:** GROUNDED / SOURCING-PASS-NEEDED / INADEQUATE (peer reviewer would reject without further documentation).

#### M6.5 Steelmannability at peer-review depth (formerly v1.3.0 Test 25 at academic level)

Does the content steelman the strongest peer-reviewer version of its counterarguments? Distinct from M3.6 (which steelmans general critic objections); M6.5 tests against academic-field-specific objections.

**Procedure:** Per key claim, state the strongest academic-field-specific counterargument and verify the book handles it. Examples:
- To the framework: "Commons Bonds is a restatement of Pigouvian externality theory with new vocabulary." Strongest academic form.
- To the methodology: "AIT is not falsifiable in Popperian sense; inverting scarcity is not observable." Strongest.
- To the indigenous case: "Framework imposes settler-colonial analytic categories on non-settler-colonial cosmologies." Strongest.

**Verdict:** STEELMAN HANDLED / PARTIAL / NOT HANDLED (requires engagement).

#### M6.6 Citability and method-portability

Can a future graduate student building on this book cite it cleanly? Does the method port to cases not in the book?

**Procedure:** Hand the book to a hypothetical graduate student. Can they: (a) cite a specific theorem or claim? (b) apply the method to a case not in the book? Does the methodology-appendix provide enough to enable this?

**Verdict:** CITABLE AND PORTABLE / PARTIALLY (specify) / NOT YET.

### §11.5 Standing gates (run per §3)

Standard three gates. M6 especially surfaces sensitivity-reader for indigenous / marginalized-community engagement per Standing Gate C.

### §11.6 Review memo output format

> **M6 Academic Rigor Review — [content being evaluated]**
>
> **Standing gates:** [one-line each].
>
> **Methodological defense (M6.1):** Verdict.
>
> **Literature engagement (M6.2):** [per field]. Verdict.
>
> **Falsifiability beyond AIT (M6.3):** Verdict.
>
> **Empirical grounding (M6.4):** Verdict + sourcing gaps.
>
> **Steelman at peer-review depth (M6.5):** [per key claim]. Verdict.
>
> **Citability and portability (M6.6):** Verdict.
>
> **Reviewer's judgment:** Senior-academic voice summary. Would this reviewer endorse the book for peer review at a top journal or university press? What would need strengthening?
>
> **Recommendation:** [Submission-ready for academic venue / Requires literature pass / Requires methodology strengthening / Requires substantive revision].

### §11.7 Light mode

M6.2 + M6.4 mandatory at light.

### §11.8 Cross-references

- M1 Framework integrity is this module's primary methodological-defense engine.
- M7 Originality asks the contribution question; M6 asks the defensibility question.
- M11 Characters 9, 12, 17, M1-M4 are this module's attack-surface.

---

## §12. M7 — Originality tests

### §12.1 Reviewer voice

A review-article author benchmarking the field — someone writing a review of intergenerational-justice / commons-governance / political-economy-of-extraction scholarship. Their job is to place new work against existing work. Asks: what does this book add that the field doesn't already have?

### §12.2 Core question

What's genuinely new vs. restating existing literature? Can the claim of contribution defend itself?

### §12.3 When to run

- Pre-submission; any venue requiring contribution claim.
- Introduction + conclusion review.
- Agent-pitch and jacket-copy development.
- When M11 Character 12 (grad student) or 18 (Harvey/Klein reader) flags pressure.

### §12.4 Sub-tests

#### M7.1 Contribution claim articulation

Can the author state, in 2-3 sentences, what the book contributes that existing work does not?

**Procedure:** Produce the contribution claim. Example for Commons Bonds (candidate articulation): "Ostrom's polycentric commons-governance framework operates at present-day scales; Harvey's accumulation-by-dispossession operates at structural-critique scales. Neither prices permanent foreclosure of non-renewable resources via substitutability-weighted intergenerational cost. Commons Bonds extends the commons-governance tradition into intergenerational pricing by introducing (a) the AIT methodology for scarcity-grounded cost identification, (b) the RCV formula for pricing foreclosure under substitutability uncertainty, and (c) the two-path rigor protocol for distinguishing real severance from institutional capture."

**Verdict:** CLAIM ARTICULABLE / REQUIRES SHARPENING / UNCLEAR CLAIM (serious problem).

#### M7.2 Competitor / overlap analysis (formerly v1.3.0 Test 18)

Does substantially similar work already exist that would reduce this material's distinctiveness?

**Procedure:** For each field identified in M6.2, state: closest existing work / the overlap / the distinctive addition. Key candidates:

- vs. **Pigouvian externality theory:** adds intergenerational-foreclosure via substitutability; adds allocation-shield structural analysis.
- vs. **Ostrom:** extends to intergenerational scale; adds AIT methodology; operates where no standing commons-governance body exists.
- vs. **Harvey (accumulation-by-dispossession):** names the mechanism at finer structural resolution (severance mechanism vs. accumulation pattern); prices rather than critiques.
- vs. **Klein (disaster capitalism):** broader scope (extraction not only disaster); operates year-round not only in crisis.
- vs. **Raworth (doughnut economics):** Raworth is system-level framing; CB is case-level pricing.
- vs. **Stern / Nordhaus / Weitzman:** integrates their work into RCV but reframes carbon-discount-rate debate as substitutability-function debate.
- vs. **Graeber (*Debt*):** adjacent but different — Graeber tracks obligation-severance in money forms; CB tracks obligation-severance in extraction forms.

**Verdict:** DISTINCTIVE / PARTIAL OVERLAP (specify; contribution-claim needs sharpening in that area) / SUBSTANTIVE OVERLAP (requires contribution revision).

#### M7.3 Novelty-critic steelman

What would the strongest novelty-skeptic say? Possibilities: "CB is Polanyi for the climate era"; "CB is Ostrom plus math"; "CB rediscovers externality theory with better PR"; "CB's RCV is a relabeled discount-rate-adjusted NPV."

**Procedure:** State the 3-5 strongest novelty-skeptic positions. Respond to each, either by: accepting the position and scoping the contribution claim accordingly, or defending the contribution against the position with specific differentiating claims.

**Verdict:** DEFENDED / SCOPING NEEDED / CONTRIBUTION WEAKER THAN CLAIMED.

#### M7.4 Harvey / Klein / Raworth compression test

Can CB's key vocabulary compress to a 2-3-word phrase that travels in the way "accumulation by dispossession," "disaster capitalism," and "doughnut economics" travel?

**Procedure:** Per candidate compression: "cost severance" (2 words, portable); "severed cost" (2 words, portable); "residual commons value" (3 words; abbreviation to "RCV" potential); "civilizational substitutability gap" / "CSG" (abbreviation). Test each: does it travel when dropped into a paragraph without definition?

**Verdict:** TRAVELS / PARTIAL (specify which terms need work) / DOES NOT TRAVEL (major contribution-framing concern).

### §12.5 Standing gates (run per §3)

Standard three gates.

### §12.6 Review memo output format

> **M7 Originality Review — [content or book-level]**
>
> **Standing gates:** [one-line each].
>
> **Contribution claim (M7.1):** [claim statement]. Verdict.
>
> **Competitor overlap (M7.2):** [per closest competing work]. Verdict.
>
> **Novelty-critic steelman (M7.3):** [per strongest novelty skeptic]. Verdict.
>
> **Vocabulary compression (M7.4):** [per candidate term]. Verdict.
>
> **Reviewer's judgment:** Review-article-author voice summary. Does this work belong in a review of the field? What's the one-line placement?
>
> **Recommendation:** [Contribution defensible / Sharpen contribution / Substantial rework of positioning].

### §12.7 Light mode

M7.1 + M7.2 mandatory.

### §12.8 Cross-references

- M6 Academic rigor re-reviews the methodology-level contribution claim.
- M8 Long-term potential re-asks: will this contribution still seem distinctive in 13+ years.

---

## §13. M8 — Long-term potential tests

### §13.1 Reviewer voice

An intellectual-history reader in 2045 looking back at 2020s social theory. Evaluates which works from the period entered discourse and lasted, which faded, and why.

### §13.2 Core question

Will this book's core vocabulary and claims hold in 13+ years? Will a reader in 2040 find the book's arguments intact, or will they read as period-specific?

### §13.3 When to run

- Final paragraph selection + chapter-title decisions.
- Key-vocabulary naming decisions.
- Before Berggruen submission (Berggruen explicitly judges for long-term institutional thinking).
- Introduction-and-conclusion review.

### §13.4 Sub-tests

#### M8.1 Decade-out durability (formerly v1.3.0 Test 19)

Will this claim still hold in 13+ years?

**Procedure:** Read content asking: what time-bound anchors does this depend on? (Specific political regime? Specific technology? Specific legal regime? Specific economic context?) Flag anchors whose durability is uncertain. For each, assess whether the claim survives anchor-failure (scoping holds) or fails (requires revision).

**Verdict:** DURABLE / DURABILITY-SCOPED (specify; acceptable) / FRAGILE (requires revision or explicit scoping).

#### M8.2 Vocabulary cascade-potential (formerly v1.3.0 Test 20 at long-term depth)

Will this vocabulary be cited in 13+ years? Does it have the compression-and-precision that "accumulation by dispossession" (40+ years of citation) and "doughnut economics" (10+ years of citation) demonstrate?

**Procedure:** Per key term, state: compression (word count); precision (definitional clarity); memorable-phrase-fit (will it live in the reader's working vocabulary?). Test by reading a paragraph using the term in a context 10 years hence (2036). Does it still work?

**Verdict:** CASCADE-POTENTIAL HIGH / MODERATE / LOW (term unlikely to carry).

#### M8.3 Labor-lawyer-in-2039 test (formerly v1.3.0 Test 23)

The canonical success sentence: *a labor lawyer uses "severed cost" in a brief or open court in 2039 without needing to explain it.* Does this specific content strengthen that canonical-2039 use, neutralize it, or weaken it?

**Procedure:** State the 2039 brief. Does the content's vocabulary / argument / claim support the brief's use?

**Verdict:** STRENGTHENS / NEUTRAL / WEAKENS (flag as scope concern).

#### M8.4 Goals alignment (formerly v1.3.0 Tests 21-22)

- **Upstream-of-Goal-1:** Does this strengthen the book's contribution to "future generations compensated more fairly"?
- **Direct-to-Goal-2:** Does this strengthen "people accept a job or project with open eyes and honest accounting"?

**Procedure:** Per content, name Goal-1 and Goal-2 contribution. Verify not-dilutive.

**Verdict:** ALIGNED / DILUTES GOAL-N (specify).

#### M8.5 Rousseau-test

Rousseau's *Discourse on Inequality* (1754) took decades to produce visible policy change. The American and French revolutions were downstream. The mechanism: Rousseau made hierarchy feel *contingent* rather than *natural*. Once the distinction was named, elites who wanted to dismantle the existing order had intellectual scaffolding Rousseau had built.

Does this book's naming work operate at the Rousseau level? Does it make the extraction mechanism feel structural-and-interruptible rather than natural?

**Procedure:** State what the book makes visible that was invisible. State the downstream political work that becomes possible once the mechanism is named. Assess whether the naming is compression-ready for the Rousseau-level move.

**Verdict:** ROUSSEAU-LEVEL POTENTIAL / PARTIAL (specify) / DOES NOT REACH THIS LEVEL (scope accordingly).

### §13.5 Standing gates (run per §3)

Standard three gates.

### §13.6 Review memo output format

> **M8 Long-term Potential Review — [content or book-level]**
>
> **Standing gates:** [one-line each].
>
> **Decade-out durability (M8.1):** [anchors / scoping]. Verdict.
>
> **Vocabulary cascade (M8.2):** [per key term]. Verdict.
>
> **Labor-lawyer-2039 (M8.3):** Verdict.
>
> **Goals alignment (M8.4):** Verdict.
>
> **Rousseau-test (M8.5):** Verdict.
>
> **Reviewer's judgment:** 2045-reader voice summary. Does this book live in 2045's intellectual history, or does it fade? What would strengthen its durability?
>
> **Recommendation:** [Cascade-durable / Some sharpening needed / Durability concerns require revision].

### §13.7 Light mode

M8.2 + M8.3 mandatory.

### §13.8 Cross-references

- M5 Dinner-table — vocabulary portability is the near-term version of cascade-durability.
- M7 Originality — contribution claim feeds long-term potential.

---

## §14. M9 — Risk / exposure tests (NEW v2.0.0 as consolidated module)

### §14.1 Reviewer voice

A publisher's legal counsel reading for pre-submission risk, combined with a sensitivity-reader-protocol expert reading for ethical exposure. Identifies risks the author and publisher need to handle before submission, not after.

### §14.2 Core question

What are the legal, reputational, career, and ethical risks for the author and for third parties named in the book? Which require mitigation before submission?

### §14.3 When to run

- Pre-submission to any venue.
- Any chapter involving named third parties, living persons, CEO-era material, or marginalized communities.
- After M2 Case study tests flag named-party exposure.

### §14.4 Sub-tests

#### M9.1 Legal exposure (formerly v1.3.0 Test 11)

**Procedure:** Per content block, identify:

- **Defamation risk.** Named living individuals: public figures (doctrine permits; standard cite + source adequate) vs. private individuals (higher standard). Named corporations (standard differs by jurisdiction; US permits wide latitude for criticism of corporate conduct).
- **Privacy risk.** Private facts about private individuals without consent. Consent documentation required.
- **Contract / NDA compatibility.** Any CEO-era material must pass NDA review. Any consulting-era material (NASA / JH / NIH) must pass institutional-confidentiality review.
- **Copyright / attribution.** Direct quotations require fair-use analysis or permission.

**Verdict:** CLEAR / PRE-SUBMISSION LEGAL REVIEW REQUIRED (list items) / BLOCKS-SUBMISSION-WITHOUT-COUNSEL.

#### M9.2 Career-risk compatibility (formerly v1.3.0 Test 13)

Does content create exposure through the author's current professional channels (nursing licensing, employer networks, credentialing bodies)?

**Procedure:** Per content, assess whether industries discussed (pharmaceutical, tobacco, healthcare finance, coal) have mechanisms to route backlash through the author's current employment. Dimensions especially relevant: Informational (industry data-suppression cases), Political (regulatory capture + healthcare financing interlocks), Institutional (CEO-era cases).

**Verdict:** LOW / MODERATE (specify mitigation) / HIGH (requires content revision or explicit career-risk acknowledgment).

#### M9.3 Lone-author vulnerability (formerly v1.3.0 Test 10)

A framework-level book by a lone author is structurally more vulnerable to targeted response than an institutionally-affiliated author's equivalent work.

**Procedure:** Per content likely to invite targeted response (industry pushback, academic-field pushback, political-apparatus pushback), assess: does the author have institutional backing (affiliation) mitigating this? If not, what's the fallback protocol?

**Verdict:** MITIGATED / SOME VULNERABILITY (specify mitigation plan) / HIGH VULNERABILITY (requires explicit content scoping or institutional-affiliation work).

#### M9.4 Anonymization / third-party mitigation

Per case-study or content block involving former colleagues, subordinates, specific clients, or identifiable third parties: what mitigation is in place?

**Procedure:** Per named / near-named third party, verify one of: public-record standing, explicit consent, anonymization, or scope-limitation. Flag anyone without mitigation.

**Verdict:** MITIGATED / ITEMS PENDING (list + protocol) / BLOCKS-SUBMISSION-WITHOUT-MITIGATION.

#### M9.5 Sensitivity-reader engagement (Standing Gate C applied as sub-test)

Per content involving marginalized / named / living-third-party communities: is sensitivity-reader engagement in place or planned?

**Procedure:** Per engagement surface (indigenous peoples, racial minorities, specific communities), verify status. Current standing: Lakota Nation sensitivity reader non-optional for Ch 10 indigenous anchor per `research/case-studies/indigenous-land-dispossession.md` §7.1.

**Verdict:** ENGAGEMENT CONFIRMED / ENGAGEMENT PLANNED (list candidate readers + timeline) / ENGAGEMENT NOT YET INITIATED (blocks submission for non-optional-gate content).

#### M9.6 Publisher-level risk surface

What does the book ask the publisher to carry? Defamation insurance? Contract indemnity? Editorial-standard verification?

**Procedure:** Per material risk, state the publisher-level exposure. Flag anything that narrows publisher options (some university presses carry less than trade houses; some venues have specific risk-tolerance profiles).

**Verdict:** STANDARD / NARROWED-PUBLISHER-POOL (specify) / SUBSTANTIAL-PUBLISHER-RISK (may require specific publisher-type or additional pre-submission work).

### §14.5 Standing gates (run per §3)

Sensitivity-reader gate is this module's own work. Earning-its-place is still relevant (risky content that doesn't earn its place should be removed, not mitigated).

### §14.6 Review memo output format

> **M9 Risk / Exposure Review — [content or manuscript-level]**
>
> **Standing gates:** [one-line each].
>
> **Legal (M9.1):** [per risk type]. Verdict + pre-submission legal items.
>
> **Career-risk (M9.2):** Verdict + mitigation.
>
> **Lone-author vulnerability (M9.3):** Verdict + mitigation.
>
> **Anonymization / third-party (M9.4):** Verdict + pending items.
>
> **Sensitivity-reader engagement (M9.5):** Verdict + engagement plan.
>
> **Publisher-level risk (M9.6):** Verdict + publisher-pool notes.
>
> **Reviewer's judgment:** Counsel + sensitivity-expert voice. Consolidated pre-submission risk picture. Items that cannot be deferred to drafting or post-submission resolution.
>
> **Recommendation:** [Submission-cleared / Pre-submission items (list) / Blocks submission until remediation].

### §14.7 Light mode

M9.1 + M9.4 + M9.5 mandatory.

### §14.8 Cross-references

- M2 Case study — per-case risk assessment feeds M9.
- M10 Publishing path — publisher-level risk profile informs venue fit.
- M11 Character 7 (legal counsel) + Character 23 (former subordinate) are M9's external cross-checks.

---

## §15. M10 — Publishing path tests

### §15.1 Reviewer voice

A literary agent preparing to submit the manuscript — or an intellectual-platform editor (Noema / Berggruen) evaluating whether the work fits their venue. Evaluates marketability, venue fit, cascade strategy, commercial viability, and submission readiness.

### §15.2 Core question

Is this viable for the intended publishing cascade, and what's the submission path?

### §15.3 When to run

- Pre-submission.
- Agent outreach preparation.
- Before cascade venue selection or sequencing.
- When cascade feedback (e.g., Noema response) requires pivot assessment.

### §15.4 Sub-tests

#### M10.1 Publisher appeal (formerly v1.3.0 Test 14)

Does the work strengthen or weaken a publisher pitch? Publisher-appeal and framework-rigor can diverge; when they diverge, rigor wins, but the divergence must be named.

**Procedure:** Per publisher-type (academic press, trade, hybrid / small press, essay cascade venues), assess appeal. Note any divergence from rigor findings.

**Verdict:** APPEALING (specify to which publisher types) / NARROWED APPEAL (specify) / LOW APPEAL (requires positioning work or publisher-type narrowing).

#### M10.2 Cascade venue fit (formerly v1.3.0 Test 15)

For each venue in the cascade (Noema / Berggruen / Boston Review / The Atlantic Ideas / longer-term trade press):

- **Noema** — intellectual-platform fit, cross-spectrum long-form, originality of contribution. Dinner-table-intelligent-reader audience.
- **Berggruen Prize (essay, Aug 17 2026 deadline)** — long-horizon institutional thinking, methodological rigor, philosophical depth, lived-experience grounding. AI-free manuscript required.
- **Boston Review** — progressive intellectual, policy-adjacent, argument-centered.
- **The Atlantic Ideas** — general-interest intellectual, narrative-carried.
- **Trade press book (post-cascade)** — dependent on cascade traction; candidates: Beacon Press, PublicAffairs, Chelsea Green, Bloomsbury, FSG.

**Procedure:** Per venue, verify content fits. Flag content that cascades well vs. specific-venue-only.

**Verdict:** FITS CASCADE / FITS SPECIFIC VENUES (specify) / MISFIT.

#### M10.3 Agent interest (formerly v1.3.0 Test 16)

Commercial viability + media-appeal + pitch clarity. Does the work lend itself to an agent taking it on?

**Procedure:** Produce a one-sentence elevator pitch for the book. Produce a one-paragraph description. Produce a comp-title list. Each should be sharp enough to send cold.

**Verdict:** PITCH-READY / PITCH-NEEDS-SHARPENING / PITCH-UNCLEAR.

#### M10.4 Comp titles (NEW v2.0.0)

What are the 3-5 comp titles? A comp title is a recent (last 5-10 years) trade-published book in the adjacent conceptual-space that succeeded (sold well, entered discourse). Comp titles anchor the publisher's expectation of the book.

**Procedure:** Propose 3-5 comp titles. Assess each for recency (last 5-10 years ideal), sales (trade-proven preferred), intellectual adjacency. Candidate comps for Commons Bonds (author to refine):

- Matthew Desmond, *Evicted* (2016) — Pulitzer; structural-mechanism-visible-in-human-lives model.
- Kate Raworth, *Doughnut Economics* (2017) — heterodox-economics-for-general-audience model.
- Thomas Piketty, *Capital in the Twenty-First Century* (2014) — structural-economics-trade-book model; very high bar.
- Anne Case + Angus Deaton, *Deaths of Despair and the Future of Capitalism* (2020) — mortality-data-structural-argument model.
- Roxanne Dunbar-Ortiz, *An Indigenous Peoples' History of the United States* (2014) — settler-colonial-structural-history model.
- Naomi Klein, *The Shock Doctrine* (2007) or *This Changes Everything* (2014) — disaster-capitalism-style framework-naming.

**Verdict:** COMP-SET STRONG / COMP-SET NEEDS WORK / NO VIABLE COMPS IDENTIFIED (serious pitch problem).

#### M10.5 Jacket copy (NEW v2.0.0)

Can the book be described in ~200-word jacket copy that: names the argument, names the author credibly, invites the reader, and avoids over-claiming?

**Procedure:** Produce a 200-word jacket copy draft. Verify it does not claim what the book doesn't deliver.

**Verdict:** JACKET-COPY-READY / NEEDS-DRAFT / UNCLEAR WHAT TO CLAIM (signals positioning concern).

#### M10.6 Pitch clarity (NEW v2.0.0)

Can the author pitch the book in 30 seconds to an agent / editor / interviewer?

**Procedure:** Produce a 30-second pitch. Test against the dinner-table standard (M5). Does it name: what the book is, why now, why this author?

**Verdict:** PITCH-CLEAR / SHARPENING NEEDED / PITCH-UNCLEAR.

#### M10.7 Platform and bio (NEW v2.0.0)

Does the author have a platform that will support the book? Bio, credentialing, lived-experience claims.

**Procedure:** Produce a one-paragraph author bio. Assess: is the author's credibility visible? Does the bio match the book's claims (first-time-author + framework-originality + nursing-student + IT-consulting-background + Hampton-sailboat-writer = distinctive positioning)? Any gaps?

**Verdict:** PLATFORM SUPPORTS BOOK / PARTIAL (specify gaps) / PLATFORM UNDERDEVELOPED (cascade-first-then-book sequencing recommended).

#### M10.8 Target reader recognition (formerly v1.3.0 Test 17, at publishing depth)

From a publisher's perspective: who buys this? M5 Dinner-table asks whether readers can understand; M10.8 asks whether there are enough of them to justify publication.

**Procedure:** Estimate the reader pool. Adjacent book sales figures. Specific audience segments (labor-law professionals, commons-governance scholars, extraction-community residents + allies, knowledge-worker readers interested in structural critique, academic-adjacent general readers).

**Verdict:** DEFINED READERSHIP / DIFFUSE READERSHIP (may reduce publisher appeal) / UNCERTAIN.

### §15.5 Standing gates (run per §3)

Standard three gates.

### §15.6 Review memo output format

> **M10 Publishing Path Review — [content or manuscript-level]**
>
> **Standing gates:** [one-line each].
>
> **Publisher appeal (M10.1):** [per publisher type]. Verdict.
>
> **Cascade venue fit (M10.2):** [per venue]. Verdict.
>
> **Agent interest (M10.3):** [pitch / description / comps]. Verdict.
>
> **Comp titles (M10.4):** [3-5 comps with fit notes]. Verdict.
>
> **Jacket copy (M10.5):** [draft]. Verdict.
>
> **Pitch clarity (M10.6):** [30-second pitch]. Verdict.
>
> **Platform and bio (M10.7):** [bio draft + assessment]. Verdict.
>
> **Readership (M10.8):** Verdict.
>
> **Reviewer's judgment:** Agent-voice summary. Submission sequence recommended. Risks to the pitch.
>
> **Recommendation:** [Submission-ready / Sharpening work required (list) / Positioning work required (list)].

### §15.7 Light mode

M10.2 + M10.6 mandatory.

### §15.8 Cross-references

- M7 Originality feeds the contribution claim that the pitch depends on.
- M9 Risk / exposure feeds publisher-level risk profile in M10.1.
- M11 Characters 5 (Noema), 6 (Berggruen), 7 (legal), 8 (agent) are this module's external cross-checks.

---

## §16. M11 — Critic pressure tests

### §16.1 Reviewer voice

25 characters representing the book's full reader surface — critics, gatekeepers, intended users, cultural readers, personal / proximal readers, ethical / legacy readers. Each character represents a structurally-different reading position. The battery is preserved from v1.3.0 whole; individual characters cross-reference other modules where their pressure naturally feeds (e.g., Character 9 tenured econ chair → M6 Academic rigor).

### §16.2 Core question

Does the book hold up under the full range of reader-position pressures it will encounter?

### §16.3 When to run

- Pre-submission full-suite run.
- Any chapter-level or book-level major revision.
- When cascade feedback surfaces reader-reception patterns not anticipated.

### §16.4 The 25 characters

#### Group G — Critics (attacking)

- **C1. Hostile coal-industry defender.** Attacks coal case, carbon-pricing implication, anti-fossil-fuel moralism framing. Typical pressure: "cheap energy lifted billions out of poverty"; miner-dignity framing; claim-of-bias.
- **C2. Left critic ("reformed capitalism").** Attacks as insufficiently radical; soft-pedaling exploitation; legitimizing extraction by reforming its accounting rather than ending it.
- **C3. Right critic ("anti-market").** Attacks as hostile to markets; regulation in disguise; redistribution dressed as accounting.
- **C4. Journalist looking for hit-piece angle.** Looks for contradiction, self-serving framing, selective data, ad hominem opportunities.

#### Group H — Gatekeepers (evaluating) → cross-ref M10 Publishing path + M6 Academic rigor

- **C5. Noema editor.** Evaluates intellectual-platform fit, cross-spectrum reach, long-form coherence, originality of contribution.
- **C6. Berggruen Prize judge.** Evaluates long-term institutional thinking, methodological rigor, philosophical depth, lived-experience grounding.
- **C7. Publisher's legal counsel.** Evaluates defamation exposure, privacy risk, NDA compatibility, identifiability of third parties. → M9.
- **C8. Literary agent evaluating representation.** Evaluates commercial viability, media-pitch clarity, author-platform potential. → M10.
- **C9. Tenured economics chair.** Evaluates methodological rigor, mathematical grounding, empirical base, academic usability. → M6.

#### Group I — Intended users → cross-ref M8 Long-term potential + M5 Dinner-table

- **C10. Labor lawyer in 2039.** Group E canonical-sentence reader. Evaluates whether vocabulary is usable in a brief without explanation. → M8.3.
- **C11. Community organizer.** Evaluates whether framework gives language for negotiation without requiring demonization.
- **C12. Graduate student building on the work.** Citability, method-portability, extendability. → M6.6 + M7.
- **C13. Policy researcher at a think tank.** Applied-scholarship fit, connection to existing policy discourse.

#### Group J — Cultural readers

- **C14. Appalachian reader** (Ch 2's implied audience). Evaluates whether framework respects miner-dignity or subtly condescends.
- **C15. Young worker** (Ch 1's implied audience). Evaluates whether framework makes visible something they recognize.
- **C16. Fellow former IT consultant.** Evaluates authenticity of knowledge-worker material.
- **C17. Ostrom successor scholar.** Evaluates compatibility with and extension of commons-governance literature. → M6.
- **C18. Harvey / Klein reader.** Evaluates vocabulary compression relative to "accumulation by dispossession" / "disaster capitalism." → M7.

#### Group K — Personal / proximal readers

- **C19. Family-member reader.** Accessibility to non-specialist. → M5.
- **C20. SGA constituent.** Coherence with author's current public role.
- **C21. Nursing colleague.** Professional-context compatibility — does this enhance or conflict with nursing identity?
- **C22. MFA writing program critic.** Prose quality, register consistency, structural discipline. → M4.

#### Group L — Ethical and legacy tests → cross-ref M9 Risk / exposure + M8 Long-term

- **C23. Former subordinate from CEO days.** Anonymization pressure. → M9.4.
- **C24. Reader in 2040 looking back.** Durability test. → M8.1.
- **C25. Personal legacy coherence — Chris's grandfather at NASA Langley.** Evaluates whether book honors institutional integrity (existence-proof side) as much as it names institutional failure. The framework is not purely critical — it recognizes what honest institutions can do.

#### Optional sub-batteries

- **Methodological Defense (M1-M4):** M1 Analytic Philosopher · M2 AI Adversary · M3 Novelty Critic · M4 Completeness. Activate when methodology is being defended in an academic venue. → M6 + M7.
- **Stakeholder (S1-S5):** Legislator, Corporate Executive, Commons Administrator, Individual Worker, Tribal Elder. Activate for stakeholder-facing material.
- **Meta (X1-X2):** Meta-Critic, Self-Dissolution Critic. Activate for claims about the framework's own architecture.

### §16.5 Sub-test procedure per character

For each character:

1. What would this character press on?
2. What's the weakest point of the proposal from this character's perspective?
3. What mitigation exists, or is required before ratification?

**Red-flag rules:**

- A single critical flag warrants mitigation before submission.
- Flags from multiple characters on the same weakness indicate structural weakness (not idiosyncratic); require structural mitigation.
- Flags requiring pre-drafting work (legal review, anonymization, permissions) are tracked as pre-submission items and cannot be deferred to drafting-stage resolution.

### §16.6 Standing gates

Applied per character-pressure finding where relevant.

### §16.7 Review memo output format

> **M11 Critic Pressure Review — [content or manuscript-level]**
>
> **Standing gates:** [one-line each].
>
> Per character (25 + activated sub-batteries): [pressure point / strength / mitigation / cross-reference to other modules where applicable].
>
> **Structural flags:** [any finding from multiple characters on the same weakness]. Structural mitigation required.
>
> **Decisive flags:** [any single character whose pressure is strong enough to gate submission]. Submission-gate items.
>
> **Reviewer's judgment:** Aggregate across all characters. Identify the 2-3 most significant pressure patterns. Map to other modules for remediation.
>
> **Recommendation:** [Clear / Structural mitigation required / Substantive revision required before submission].

### §16.8 Light mode

Groups G (critics) + H (gatekeepers) mandatory; others by judgment. Sub-batteries skipped.

### §16.9 Cross-references

Already documented per-character above.

---

## §17. Output — the Pre-Submission Peer Review Report

### §17.1 Naming

`commons_bonds_psr_YYYY-MM-DD_v#.#.#.md`

Stored at: `tools/pre-submission-reviews/` (new folder). Module-level runs that aren't full-suite may be stored as rigor-pass records per v1.3.0 convention.

### §17.2 Template

```markdown
# Commons Bonds — Pre-Submission Peer Review Report

**Date:** YYYY-MM-DD
**Version:** #.#.#
**Protocol version applied:** commons_bonds_rigor_protocol_v2.0.0.md
**Run mode:** [full suite / modules M# + M# / single module M#]
**Manuscript state:** [chapter list + word counts at run time]

---

## Executive summary

[One paragraph: is the manuscript pre-submission-ready? Which modules pass cleanly? Which need work?]

## Consolidated pre-submission action items

[Bulleted, sequenced. Items that block submission at the top; items that would strengthen submission below.]

---

## Module reviews

### M1 — Framework integrity
[Full review memo per §6.6]

### M2 — Case study
[Per-case memos per §7.6]

### M3 — Book content
[Per-content-block memos per §8.6]

### M4 — Craft
[Full review memo per §9.6]

### M5 — Dinner-table
[Per-content-block memos per §10.6]

### M6 — Academic rigor
[Full review memo per §11.6]

### M7 — Originality
[Full review memo per §12.6]

### M8 — Long-term potential
[Full review memo per §13.6]

### M9 — Risk / exposure
[Full review memo per §14.6]

### M10 — Publishing path
[Full review memo per §15.6]

### M11 — Critic pressure
[Full review memo per §16.7]

---

## Standing-gate audit

[Aggregate all Standing Gate findings across modules. Any ENGAGEMENT NON-OPTIONAL item from Gate C that is not yet in motion is a submission blocker.]

## Cross-module patterns

[Any finding that appeared in 3+ modules on the same weakness. Structural; likely requires book-level rather than chapter-level remediation.]

## Submission readiness verdict

[One of: READY FOR SUBMISSION TO (venue) / READY AFTER LISTED ITEMS / NOT READY (substantive revision required)].
```

---

## §18. Worked examples (preserved from v1.3.0)

### §18.1 First worked example — C6 Decision Memo v2.0.0

`alignment/decisions/commons_bonds_c6_decision_memo_2_0_0.html` — the first complete application of the multi-test battery. Evaluates four options (retire FGC / parallel dimensions / reconcile / collapse via manifestations) against two-path + four scales + AIT + 10-critic + success criteria.

**Lesson:** The first v1.0.0 memo applied AIT + 10-critic without two-path. The rerun with two-path surfaced the decisive Tier 8 absence. Running only some applicable tests produced a recommendation defensible on the narrow battery but missing a decisive finding.

**v2.0.0 translation:** In v2.0.0 terms, the v1.0.0 memo ran M1.1 + M11 without M1.2. Running M1 as a complete module (all four sub-tests) would have caught it.

### §18.2 Second worked example — Layer and Tier Stress Test v1.0.0

`commons_bonds_layer_tier_stress_test_1_0_0.md` — conducted v1.19.0 after off-Earth exemplar drafted.

**Lesson:** Added off-Earth exemplar to Test 3 (→ M1.4 in v2.0.0). The "Planetary" candidate name passed at Earth-individual scale but failed at off-Earth-individual. Earth-only exemplars silently approved the failure.

### §18.3 Third worked example — v1.24.0 scope rigor passes

`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-21_v1_0_0.md` — three rigor passes during v1.24.0 scope session.

**Lesson:** v1.24.0 produced a parallel-lineage protocol (v1.0.0) without awareness that v1.1.0 was canonical. The parallel-lineage artifact had expanded coverage but silently dropped AIT + multi-scale + procedural template. Lineage-drift.

### §18.4 Fourth worked example — 8-tier rigor pass v1.0.6

`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-22_v1.0.6.md` — full-rigor pass on each of 8 tiers applying Tests 28 + 29 (standing gates) + all Group A tests. Per-tier earning-its-place verdicts. All 8 tiers EARNED PLACE with specific book-scope functions named.

**v2.0.0 translation:** In v2.0.0 terms, v1.0.6 was a M1 + Standing Gates pass on each tier. All 8 would be preserved in v2.0.0.

### §18.5 Fifth worked example (v2.0.0) — case-study audit v1.0.5

`core/case-studies/commons_bonds_case_study_audit_v1.0.5.md` — 18 cases profiled; per-case rigor + routing. This is the implicit M2 that v2.0.0 formalizes. Post-v2.0.0, case-study audits are explicit M2 runs with the module-level procedure documented.

### §18.6 Sixth worked example (v2.0.0) — chapter audit v1.0.5

`core/chapters/commons_bonds_chapter_audit_v1.0.5.md` — 10 chapter profiles + integration catalog. This draws from M3 + M4 + M5 + M6 (scattered across the audit's rigor applications). Post-v2.0.0, chapter audits draw from explicit module runs rather than implicit ones.

---

## §19. Protocol governance

### §19.1 Session-start verification

At session start, verify canonical protocol version against operating core. If canonical has drifted from what the session is using, flag before running.

### §19.2 Upload pattern

Upload this file alongside current session handoff. Do not modify within-session.

### §19.3 Version numbering

- **Patch (2.0.1, 2.0.2):** clarifications, typo fixes, worked-example additions, test-procedure sharpening.
- **Minor (2.1.0, 2.2.0):** new module, new sub-test within a module, new sub-battery, new worked example promoted to reference.
- **Major (3.0.0):** structural change to the module set (module added / removed / substantially reorganized), fundamental change to running-mode architecture, overhaul of standing-gate framework.

### §19.4 When to revise

1. A new type of decision emerges that doesn't fit module routing cleanly.
2. A sub-test proves systematically redundant with another across multiple applications.
3. A character type emerges as standardly important that is not currently on the list.
4. A character type on the list proves systematically non-differentiating.
5. Operating core is revised in a way that affects framework tests (M1).
6. Cascade-reception feedback reveals a missing test or reader-position.
7. A worked example reveals a protocol gap.

### §19.5 When not to revise

- A single decision fails. That's a finding, not a protocol problem.
- A sub-test produces an unexpected verdict. Document and move on.
- Stylistic or formatting preferences change. Use the session handoff.

### §19.6 Revisitability

A sub-test or character that fails to differentiate on one pass may differentiate on another. Rejection is a finding about the tested application, not a permanent verdict.

---

## §20. Change log

### v2.0.0 (2026-04-23) — major bump

**Structural reorganization** from test-type groups (v1.3.0) to purpose-driven peer-review modules. Every v1.3.0 test preserved; none dropped. Every module runnable standalone; running the full suite constitutes a Pre-Submission Peer Review.

**Changes:**

1. **Reorganization.** v1.3.0's Group A / §5A / Groups B-F / 25-character suite → v2.0.0's 11 purpose-driven modules (M1-M11).
2. **Standing gates.** v1.3.0's §5A Tests 28 + 29 promoted to Standing Gates (§3), plus new Standing Gate C (Sensitivity-reader engagement). Standing gates apply to every module at every depth.
3. **New modules.**
   - **M2 Case study tests** (NEW) — formalizing implicit procedure from case-study audit.
   - **M4 Craft tests** (NEW) — structure, arc, voice, register, prose, preamble-strip.
   - **M9 Risk / exposure** (NEW consolidated) — legal + reputational + career + anonymization + sensitivity-reader.
4. **Module content additions.**
   - **M5 Dinner-table test** — formalized standalone (was scattered in v1.3.0 Tests 17, 20 + Character 19).
   - **M7 Originality contribution claim articulation** (M7.1) — explicit procedure for stating contribution (was implicit in Test 18).
   - **M10 Publishing path additions** — comp titles (M10.4), jacket copy (M10.5), pitch clarity (M10.6), platform and bio (M10.7). None in v1.3.0.
5. **Output format shift.** Each module produces a review-memo in peer-reviewer voice, not test-verdict table. Full-suite output = Pre-Submission Peer Review Report.
6. **Running modes.** Single-module / combined / full / light. v1.3.0 had only full / light.
7. **Sensitivity-reader engagement** elevated from case-file-specific (indigenous case §7.1) to Standing Gate C applicable to all content.
8. **Worked examples 18.5 + 18.6** added (case-study audit + chapter audit as v2.0.0 retrospective examples).

**Mapping from v1.3.0 → v2.0.0** at §0.2. Complete: every v1.3.0 test location now has a v2.0.0 location.

### Prior versions (summary)

- **v1.3.0 (2026-04-22 evening):** Added §5A standing tests (Tests 28 + 29). Minor bump.
- **v1.2.2 (2026-04-22 afternoon):** Container-term rename patch ("layer" → "dimension").
- **v1.2.1 (2026-04-22 morning):** Clarifications patch + Test 13 correction + consent-normalization shield typology.
- **v1.2.0 (2026-04-21, ratified 2026-04-22):** Lineage reconciliation (v1.0.0 parallel-lineage absorbed into v1.1.0 canonical).
- **v1.1.0 (2026-04-20):** Multi-scale × 2 environments + off-Earth exemplars.
- **v1.0.0 (2026-04-20):** Initial canonical protocol. AIT + two-path + multi-scale + 10-critic + success criteria.

Full v1.3.0 change log preserved at `tools/archive/commons_bonds_rigor_protocol_v1.3.0.md` (if archived) or via git history.

---

## §21. Appendix — cross-references

- **Operating core:** preferences, session handoffs, C9 patch §3 (AIT canonical positioning).
- **AIT source:** `core/decomposition/eight-tier-v10.html`.
- **Two-path source:** `alignment/patches/pending-framework-review/c2_scale_abstract_patch.md`, `...c3_mechanism_shield_patch.md`, `...c5_two_path_rigor.md` (preserved paths; c5 archived).
- **Success criteria source:** `tools/commons_bonds_book_scope_v1_0_3.md` + `tools/commons_bonds_guiding_constraints_v1_0_0.md`.
- **Scaffolding-vs-load-bearing canonical:** `alignment/patches/pending-framework-review/c9_ait_canonical_positioning_patch.md`.
- **Case-study audit (M2 worked example):** `core/case-studies/commons_bonds_case_study_audit_v1.0.5.md`.
- **Chapter audit (M3 + M4 worked example):** `core/chapters/commons_bonds_chapter_audit_v1.0.5.md`.
- **Indigenous case sensitivity-reader protocol:** `research/case-studies/indigenous-land-dispossession.md` §7.1.
- **Worked rigor-pass records:** `tools/rigor-passes/` (v1.0.1–v1.0.6).
- **Superseded protocol:** v1.3.0 (retired via git history; see §0.2 for mapping).

---

*End of Commons Bonds Canonical Rigor Protocol v2.0.0 — Pre-Submission Peer Review Suite.*
