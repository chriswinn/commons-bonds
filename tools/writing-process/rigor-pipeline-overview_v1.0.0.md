# Rigor Pipeline — Six-Stage Process Overview (v1.0.0)

**Date drafted:** 2026-05-19
**Status:** Living document. Captures the current state of a six-stage rigor pipeline developed for long-form publisher-facing writing (book manuscripts; long-form essays; whitepapers; reports).
**Portability:** Designed to be lift-and-reused. Lightly edit the project-specific examples and cross-references and this becomes a standalone writing-process reference for other projects. Could be extracted to its own repository as the process matures.

---

## §0. What this is + who it's for

A unified rigor pipeline for any writing that meets two conditions: (a) it goes to an external publisher, agent, reviewer, or client; and (b) factual accuracy, voice quality, and audience-aware register all matter.

The pipeline takes lessons from peer-review workflows in regulated environments (NIH grant pipelines, in this case) and adapts them for long-form non-academic writing. It assumes you are working with an AI writing assistant or human editor across multiple revision passes; it works equally well solo if you adopt the per-pass discipline.

**Core claim:** factual accuracy, prose quality, audience fit, and rendering integrity are *different problems with different remediation polarities*. Bundling them into a single editing pass produces mediocre results in all four dimensions. Separating them into five purpose-built passes — each with its own discipline, scale of attention, and remediation move — produces substantively better artifacts.

**Empirical anchor:** the discipline was validated by running parallel A/B drafts of a magazine essay (one drafted from source-chapter prose; one drafted audience-blind from a structured brief). The audience-blind draft, after passing through the five-pass discipline, was decisively the stronger submission across 13 of 14 substantive audit dimensions.

---

## §1. The architecture

Six sequential stages, each with sub-steps, plus two continuous infrastructure layers running underneath.

```
Stage 0   author conception / topic decision
Stage 1   ready-to-draft gate
          ├─ 1a  invariant-gate scan (corpus hygiene)
          ├─ 1b  canonical fact-ground + audience structure + render conventions
          └─ 1c  cross-artifact coherence check
Stage 2   audience-blind drafting
Stage 3   five-pass rigor audit
          ├─ 3.1  fact-check
          ├─ 3.2  voice-polish
          ├─ 3.3  audience-load acceptance
          ├─ 3.4  audience-load robustness (adversarial)
          └─ 3.5  developmental-edit
Stage 4   render + character-integrity audit
Stage 5   academic-rigor + prose-quality sign-off + pre-publication review queue

                  ─── continuous infrastructure ───
            ▲ invariant-gate scans     ▲ change-cascade routing
```

---

## §2. Stage-by-stage

### Stage 0 — Author conception

**Purpose:** the topic-and-form decision before any pipeline work fires.

You choose: what artifact (chapter / essay / whitepaper), what audience class (specialist / mixed / general), what venue (specific publication / submission target / client deliverable), what timeline.

**Output:** a lightweight decision record. Scratchpad notes, a workstream stub, a one-paragraph statement of intent. The point is to make the decision explicit before drafting, not to over-engineer it.

**Trigger for next stage:** author says "go."

---

### Stage 1 — Ready-to-draft gate

The pre-drafting hygiene + structure + coherence pass. **This is the first half of a bookend sign-off** (Stage 5 closes the loop).

#### Stage 1a — Corpus-hygiene invariant gate

A scripted scan that runs continuously (pre-commit, every stage transition, CI) and refuses to let scaffolding patterns leak into publisher-facing prose.

**What it catches:**
- **Placeholders** — `TODO`, `TK`, `FIXME`, `XXX`, `[BRACKET]`.
- **Drafting-template scaffolding** — *"Let me explain"*, *"In this section…"*, *"The plain definition is this:"*.
- **Process-scaffolding vocabulary** — option-labels, internal decision markers, finding-codes, internal-disposition glyphs.
- **Meta-commentary tics** — *"That is the whole sentence."*, *"What I mean to say is…"*.
- **Regressed patterns** — anything previously fixed by a prior rigor pass (corpus-wide institutional memory).

**Infrastructure:** two YAML registries — `scaffolding-patterns.yaml` + `regressed-patterns.yaml` — severity-tiered (HIGH = block; MEDIUM = flag; LOW = informational). Per-file allowlist mechanism for known-legitimate substantive uses, with line-number + rationale required.

**Placements:**
- **Pre-commit hook** — refuses commit on HIGH-severity match.
- **Stage-transition checklist** — both scans must be clean before transitioning.
- **CI workflow** — runs both + reports MEDIUM-severity findings.

**What Stage 1a is NOT:** substantive editing. It's hygiene. If a pattern needs substantive remediation, that's a later-stage problem.

#### Stage 1b — Canonical fact-ground + audience-aware structure + render conventions

Three coupled deliverables, all in one artifact (the "Stage 1 brief"):

1. **Canonical factual ground truth.** Inventory of names, scenes, etymologies, numbers, scene-roles, direction-of-action — every load-bearing fact the draft will reference. **This becomes the audit baseline for Pass 3.1 fact-check.** Do not skip this section: factual drift between draft sessions is one of the most common failure modes, and Stage 1's canonical-truth section is the one source-of-truth that audits trace back to.

2. **Audience-aware structure.** Editorial-brain map for the venue (what does this editor read every day? what register do they publish? what disqualifies? what excites?); audience pressure-test character set (see the companion `audience-character-roster_v1.0.0.md` — the canonical 40-character chapter-level set or a venue-calibrated subset); structural anchors (¶1 hook, closing-paragraph candidates, argumentative spine); apparatus exclusion list (every internal-jargon term the venue's readership won't tolerate, marked replace-with-translation or omit).

3. **Render-safe convention.** For math-content or specialized-typography artifacts: character conventions (em-dash, ≈ symbol, Greek letters), formula conventions, font convention with fallback-header mitigation, baseline render-test results. Caught at Stage 1b; verified at Stage 4.

**Output:** Stage 1 brief at a documented path (e.g., `rigor-passes/<DATE>_<artifact>_pre_draft_audience_structure_v1.0.0.md`).

#### Stage 1c — Cross-artifact coherence check

Catches mid-pipeline surprises that should have been resolved before drafting. Inventory the artifact's scope against:
- **Bibliography commitments** — any external citation the artifact will need.
- **Sibling-artifact framings** — what the prior or adjacent chapters/essays/sections commit to.
- **Author's-Note / framing-document positions** — any meta-document that scopes the artifact.
- **Prior rigor-pass artifacts** — canonical-name commitments; flagship-term decisions; cross-artifact consistency-inventory items.

Resolve open commitments **before drafting fires.** Mid-Pass-3 surprises (a bibliography commitment surfacing late; a sibling-chapter cross-reference noticed only in audit) are signals Stage 1c was under-fired.

**Output:** coherence-check artifact at a documented path.

---

### Stage 2 — Audience-blind drafting

**Purpose:** generate fresh prose from the Stage 1 brief **without looking at the source material** (prior drafts, source chapter, sibling artifacts, exemplar essays).

**Why audience-blind:** prevents "Path B contamination" — the failure mode where verbatim sentences and close-paraphrased paragraphs from the source material survive into the new artifact, producing a draft that reads as a derivative of the source rather than as new work calibrated to a new audience.

**Discipline:** the Stage 2 session must NOT open the source. Work only from Stage 1 brief beats + the canonical-truth section. If you must check a fact, look it up in the Stage 1 brief, not the source.

**Output:** Stage 2 draft at the artifact's working path. Single drafting move; no sub-steps. Serial-cadence friendly: one session per Stage 2 draft.

---

### Stage 3 — Five-pass rigor audit (the heart of the pipeline)

**Per-prompt serial cadence:** each pass fires in its own session. Findings are PROPOSED for author ratification; spot-fixes apply (Phase C application) before the next pass fires. Bundling passes loses the discipline each pass needs.

#### Pass 3.1 — Fact-check

**Scale:** per-fact.
**Catches:** factual drift; source-citation accuracy; canonical-truth-gap-flags (claims not traceable to Stage 1 brief AND lacking external citation).
**Audit baseline:** Stage 1b canonical factual ground truth. Do NOT use source material as ground truth — that re-introduces Path B contamination and is also self-defeating (the source may itself be wrong; only Stage 1 brief plus external citation is canonical).
**Findings format:** unique F-IDs per finding with severity (HIGH/MEDIUM/LOW), location (line + verbatim text), source-of-truth, proposed correction.

**Hard discipline:**
- Pass 3.1 does NOT propose register / voice / audience changes — those belong to other passes.
- If a fact-of-truth gap exists in the Stage 1 brief itself, flag the gap (the brief needs repair) rather than guessing.

#### Pass 3.2 — Voice-polish

**Scale:** per-paragraph.
**Catches:** LLM tics (rule-of-three exposures; em-dash crutches; hedge phrases; meta-commentary); expository flatness; cumulative cadence (multiple per-paragraph tics compounding to a generated-feeling rhythm); register mismatch; sentence-rhythm tics.
**Polarity:** **cuts.** Pass 3.2 chisels.
**Findings format:** unique F-IDs with severity, location, diagnosis (specific tic class), proposed rewrite(s) (verbatim replacement prose; multiple options for HIGH-severity).

**Hard discipline:**
- Test every proposed rewrite against the dual-audience set (layman + specialist where applicable). "Shorter = trade-press-friendly" is a wrong default; substance drives length.
- Cross-pass-impact discipline: do not propose tic-fixes that would re-corrupt facts Pass 3.1 corrected.
- Do not propose register shifts that break dual-audience hold.

#### Pass 3.3 — Audience-load acceptance

**Scale:** per-character (per-target-audience).
**Catches:** whether each target-audience character returns INCLUDE / NEUTRAL / EXCLUDE on the artifact. This is acceptance testing.
**Character set:** typically 15-30 acceptance characters constructed per construction discipline. (See `audience-character-roster_v1.0.0.md` for the canonical 40-character chapter-level set + construction discipline.)
**Verdict per character:** three-tier INCLUDE (with confidence sub-tiers), NEUTRAL, or EXCLUDE.
**Output:** PROPOSED artifact with per-character verdicts + aggregate verdict + recommended Phase C application order.

**Hard discipline:**
- Pass 3.3 is **non-prose-modifying** — produces verdicts + recommendations only, not direct prose changes. Spot-fixes route to Pass 3.2 / Pass 3.5 / Phase C application.
- Re-construct the character set at Stage 1b only if the venue, audience class, or load-bearing claim has materially changed.

#### Pass 3.4 — Audience-load robustness (adversarial)

**Scale:** per-adversarial-character (hostile readers).
**Catches:** thread-pull synthesis from hostile reads — what's the adversarial set able to attack? What threads pull on the artifact's load-bearing claims? Different question from acceptance: not "do they like it" but "where do they break it."
**Character set:** typically 5-10 adversarial characters spanning industry-funded experts, ideological adversaries, hostile reviewers, populist skeptics, business-press conservatives, legal defense-bar, etc.
**Verdict:** **thread-pull synthesis** — aggregate diagnosis matters more than per-character pass/fail. Common load-bearing threads across multiple adversaries = real artifact vulnerability. Scattered procedural threads = robust artifact with isolated cosmetic-flag exposure.
**Output:** robustness audit with thread-pull synthesis; routes adversarial findings to cross-artifact or cross-section workstreams if a thread requires substantive engagement (not a single-passage spot-fix).

#### Pass 3.5 — Developmental-edit

**Scale:** whole-artifact (chapter / essay / section).
**Catches:** emotional-arc continuity; scene-anchor density; sensory-detail restoration; voice-flow continuity; cumulative-LLM-cadence residue; reader-engagement at analytically-loaded passages.
**Polarity:** **restoration, not cutting.** Different polarity from Pass 3.2 — folding 3.5 into 3.2 would lose the discipline each polarity needs. Pass 3.2 cuts; Pass 3.5 restores.

**Why Pass 3.5 exists as a separate pass:** Pass 3.2's correct cuts produce a clipped-after-cutting feel in stretches where the chisel was right per-paragraph but the cumulative effect reads as flatness-by-omission. The remedy is **targeted restoration** — scene-anchor re-entry, sensory-beat reintroduction, breath at structural reveals, specificity restoration where genericized prose lost authorial voice. The whole-artifact scale is essential because the diagnosis is cumulative; per-paragraph passes cannot see it.

**Cadence:** fires AFTER 3.1 + 3.2 + 3.3 + 3.4 have ratify-and-applied. The flatness only surfaces post-3.2's chiseling. Pass 3.5 may also surface findings about 3.2's apply/hold dispositions; these route back as 3.2-reconsider follow-ups if needed.

**Findings format:** unique F-IDs with severity + per-finding restoration draft (NOT a cut). Some findings will be multi-option ("restore breath; restore scene-anchor; restore both") — author ratifies which option.

**Light follow-up:** a Pass 3.3 light re-fire is recommended after Phase C application of ratified Pass 3.5 spot-fixes — confirms acceptance verdicts hold; cumulative restoration may shift some.

**Token cost reality:** Pass 3.5 is the heaviest of the five passes (~50K-80K tokens per chapter / long essay in an AI-assisted pipeline). This is why it fires explicit-gate (see §3) rather than per-edit.

---

### Stage 4 — Render + character-integrity audit

**Purpose:** catch render-pipeline failures (tofu boxes; corrupted formulas; font-coverage gaps; layout drift) before the artifact ships externally.

**Sub-steps:**
- **4.1 Pre-render verification** — source compiles; render-toolchain version locked; baseline render-test (set at Stage 1b) passes.
- **4.2 Source-vs-rendered character diff** — character-by-character comparison source ↔ rendered; flag em-dash → tofu, ≈ → tofu, Greek-letter → missing-glyph, etc.
- **4.3 Formula-integrity audit** (if math content) — each formula's source ↔ rendered; subscript/superscript integrity; integral / summation / fraction layout.
- **4.4 Table-rendering audit** — alignment; overflow; column-merger artifacts.
- **4.5 Figure-rendering audit** — figure-references resolve; captions track; figure-content integrity.
- **4.6 Layout-integrity audit** — section-break drift; orphan/widow control; pagination; cross-reference resolution.

**Render conventions** (set at Stage 1b, verified here): character conventions; formula conventions; font convention with fallback-header mitigation; baseline render-test discipline.

**Verdict scale:** PASS / PASS-with-spot-fixes / FAIL.
**Fires:** explicit-gate (pre-external-send, pre-publication, on author trigger, on any pipeline-script change).

---

### Stage 5 — Sign-off bookend + pre-publication review queue

**Purpose:** the **closing bookend** to Stage 1's opening sign-off; verifies no drift through the pipeline + produces the mandatory pre-publication review queue artifact.

#### Sub-step 5.1 — Academic-rigor sign-off

Verifies: factual claims trace to ground truth or external citation; any math/framework claims are internally consistent; cross-artifact coherence holds; audience-load verdicts (Passes 3.3 + 3.4) closed-out; render integrity (Stage 4) closed-out.

**Output:** sign-off block (PASS / PASS-with-noted-gaps / HOLD).

#### Sub-step 5.2 — Prose-quality sign-off

Verifies: voice-polish (Pass 3.2) closed; developmental-edit (Pass 3.5) closed; cumulative restoration applied; no remaining LLM tics; invariant-gate scans clean.

**Output:** sign-off block (PASS / PASS-with-noted-gaps / HOLD).

#### Sub-step 5.3 — Pre-publication review queue artifact (MANDATORY)

**The transparency-by-design deliverable.** Handed to the publisher / agent / editor with the manuscript. Contents:

1. **What HAS been internally verified** — per-category check-mark inventory (factual; math/framework if applicable; cross-artifact coherence; audience-load; render integrity).
2. **What has NOT been externally verified** — factual claims that would benefit from external corroboration; math/framework claims warranting external technical review; audience-coverage gaps from Pass 3.4 thread-pull synthesis.
3. **Recommended external reviewer types** — subject-matter; technical; sensitivity; voice/style as appropriate.
4. **Highest-priority sections** — for external review if reviewer budget is limited.

**Format:** standalone artifact handed to the external reviewer / publisher. Replaces overclaiming-verification posture with explicit quality-control disclosure. This is the doctrine's strongest single move toward publisher trust: you tell them exactly what was internally verified, what wasn't, and what to look at first.

---

## §3. Change-cascade routing

Any change routes back to the appropriate prior stage. Two cascade classes by token-economy:

### Automatic-on-edit cascade (cheap; fires every relevant change)

| Change type | Routes to | Auto-fires |
|---|---|---|
| Any source-file change (pre-commit) | Stage 1a invariant scan | Commit refused on HIGH match |
| New fact discovered (interview / source / verification) | Stage 1b canonical-facts update | Pass 3.1 + Pass 3.2 for affected scope |
| New audience character identified | Stage 1b audience-set update | (Pass 3.3 / 3.4 explicit-gate) |
| Bibliography / external citation commitment | Stage 1c coherence update | (Pass 3.3 explicit-gate) |
| Spot-fix applied (any phase / any pass) | Stage 1c coherence (light) | (No automatic re-fire of audience-load) |
| Cross-artifact workstream touches multiple artifacts | Stage 1c for all affected artifacts | (Pass 3.3 light re-fire batched at workstream close) |

### Explicit-gate cascade (heavy; fires only on author trigger)

| Pass / Stage | Fires when | Reason for gating |
|---|---|---|
| **Stage 4 (render-integrity audit)** | Pre-external-send; pre-publication; "build it now" trigger; pipeline-script change | Render is cheap (Docker / CI); audit work is heavy; only valuable when artifact ships |
| **Stage 5 (sign-off + pre-pub review queue)** | Pre-external-send; pre-publication; before external-reviewer engagement | Generates mandatory pre-pub queue; only valuable at distribution-readiness |
| **Pass 3.3 (audience-load acceptance)** | New audience character; venue change; pre-publication | Per-character heavy; spot-fixes rarely shift acceptance |
| **Pass 3.4 (audience-load robustness)** | New adversarial character; cross-artifact cascade post-merge; pre-publication for any adversarial-exposure risk | Adversarial thread-pull synthesis is the heaviest pass |
| **Pass 3.5 (developmental-edit)** | Per-artifact after 3.1-3.4 ratify-and-apply complete; pre-publication; on author "developmental read-through" trigger | Whole-artifact scale; only valuable at artifact-readiness gates |

**Token-economy rationale:** automatic-on-edit cascade (Pass 3.1 + 3.2 + Stage 1c-light) totals ~10K-30K tokens per prose-edit event — justified by value-added prose rigor. Explicit-gate cascade (Pass 3.3 + 3.4 + Stage 4 + Stage 5 + Pass 3.5) totals 60K-150K tokens per pre-publication batch — appropriate cost amortized over many prose edits, not paid per spot-fix.

**Author trigger forms:** explicit instruction in a session, queue-management routing, or pre-publication gating queues all explicit-gate items as a batch.

---

## §4. Hard constraints (across all stages)

Discipline carry-forward from foundational rigor-discipline practice:

- **Per-prompt serial cadence.** Each pass fires in its own session. Author ratifies + spot-fixes apply before next pass fires. Bundling loses pass-specific discipline.
- **Path B preemptive policy.** Stage 2 sessions do NOT open source material. Pass 3.1 audits against the Stage 1 canonical-truth section, not against source prose.
- **Single source-of-truth.** Stage 1 brief is the audit baseline. Drift between draft and brief is signaled at Pass 3.1; never the other direction.
- **PROPOSED-then-ratify pattern.** All passes produce PROPOSED artifacts; author ratifies (or partially ratifies / defers). Spot-fixes apply in Phase C application sessions, not in the pass session itself.
- **Findings format discipline.** Unique F-IDs per finding; severity tier; location (line + verbatim text); diagnosis; proposed correction or rewrite; cross-pass impact note.
- **Cross-pass impact discipline.** Each pass notes whether its proposed corrections affect other passes' dispositions. Pass-3.1 fact-fixes may re-trigger Pass 3.2 voice-polish for the rewritten prose; Pass 3.5 restorations may shift Pass 3.3 acceptance verdicts.

---

## §5. How to adopt this for your own writing project

The pipeline assumes a few infrastructure pieces that can be lightweight or heavy depending on your project scale.

**Minimum-viable adoption (solo, short-form):**

1. **Stage 0 + Stage 1.** Write a one-paragraph statement of intent. Build a Stage 1 brief: canonical facts (in your head or on paper); editorial-brain map for your venue; a 5-character audience-pressure-test set (use the [audience-character-roster](audience-character-roster_v1.0.0.md) as a starting point, pick five characters most relevant to your venue).
2. **Stage 2.** Draft audience-blind from the Stage 1 brief.
3. **Stage 3 (compressed).** Fire Pass 3.1 fact-check; ratify-and-apply; fire Pass 3.2 voice-polish; ratify-and-apply; fire Pass 3.3 acceptance against your 5-character set; ratify-and-apply. (Skip 3.4 + 3.5 for short-form unless adversarial exposure is real.)
4. **Stage 4 + Stage 5.** Render-check (read it on the medium it will publish on); sign-off block + transparency disclosure to the editor if appropriate.

**Full adoption (book-length or multi-artifact projects):**

Use all six stages + sub-steps + all five passes + continuous infrastructure (invariant-gate scans + change-cascade routing). Build the YAML registries for your project's patterns. Wire pre-commit hooks. Run CI. The full doctrine pays off when you have many artifacts moving through the pipeline in parallel.

**Pattern variations:**

- **Short-form essays with strong iterated control.** The discipline may not beat carefully iterated A→B→C drafting for short-form material where you have a strong control to iterate against. Default to careful iteration; switch to the discipline if iteration isn't converging.
- **Long-form derived from source material with apparatus-tripwire risk.** This is the discipline's strongest regime. All five passes; full Stage 1 + Stage 2 + Stage 3 + Stage 4 + Stage 5.
- **Math / formula-heavy content.** Stage 1b render conventions + Stage 4 formula-integrity audit are load-bearing. The discipline catches font-coverage gaps + tofu-boxes + corrupted subscripts that would survive a normal "read it once more" review.

---

## §6. Why this works (the theory)

The discipline rests on a few empirically anchored observations:

1. **Factual accuracy, prose quality, and audience fit have different remediation polarities.** Bundling them produces compromise editing. Separating them allows each polarity to do its work cleanly.
2. **Audience-blind drafting protects against source contamination.** Path B contamination (verbatim sentences + close-paraphrase paragraphs from source material) is invisible to the drafter but immediately obvious to a Path B audit. The protection is structural: don't open the source.
3. **Per-paragraph LLM-tic cuts produce flatness-by-omission at whole-artifact scale.** Pass 3.2 is correct per-paragraph but cumulatively clipping. Pass 3.5 restores at whole-artifact scale.
4. **Adversarial reads are different from acceptance reads.** Acceptance testing asks "will they include?" Robustness testing asks "where do they break it?" Bundling them in a single character set produces confused verdicts.
5. **Render integrity is its own kind of failure.** Tofu boxes + corrupted formulas + font-coverage gaps survive content-level audits because they're not content failures. Stage 4 catches what the prose-level passes structurally cannot see.
6. **Transparency-by-design replaces overclaiming.** Stage 5's pre-publication review queue is the deliverable that says "here's what I verified; here's what I didn't; here's what to check first." Publishers + editors prefer this to authors who claim verification they didn't perform.

---

## §7. Origin + acknowledgments

The doctrine was developed in 2026-04 through 2026-05 in the course of writing a long-form non-fiction book, with iterative empirical validation through parallel A/B drafting experiments. The six-stage architecture is adapted from the NIH peer-review pipeline (which goes: fact-check + academic peer review + audience-shaping + prose flow + typography/layout + final-gate sign-off + automatic kick-backwards-on-change).

Amendments through 2026-05-19:
- **Amendment A — selective stage-firing** (2026-05-18). Cascade split into automatic-on-edit vs explicit-gate by token-economy.
- **Amendment B — Pass 3.5 developmental-edit** (2026-05-19). Codifies developmental-edit as the fifth Stage-3 pass.
- **Amendment C — Interactive Ratification Protocol** (2026-05-19). Author-Claude ratification cadence within prose-modifying passes.

---

## §8. Companion documents

- [`audience-character-roster_v1.0.0.md`](audience-character-roster_v1.0.0.md) — the canonical 40-character chapter-level audience-pressure-test set with construction discipline.
- (Future) `interview-prep-process_v1.0.0.md` — interview / sales-call / meeting-prep process derived from the same discipline, applied to live conversations rather than written artifacts.

---

## §9. Source-of-truth + license

This is a portable overview. The canonical project-internal doctrine lives at `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` + the Stage 1 / 4 / 5 sub-docs at `tools/commons_bonds_pipeline_doctrine_stage_{1,4,5}_v1.0.0.md`. For project-internal usage, treat those as canonical; this document is the externalized overview.

License: TBD by author for any extraction to standalone repository.

---

*End of rigor pipeline overview v1.0.0. Living document; refresh as the pipeline evolves.*
