# Drafting-Session Templates

**Date drafted:** 2026-05-11
**Date last refreshed:** 2026-05-24 (v3.1 pipeline doctrine — Amendments A + B + C reflected)
**Discipline reference:** v3.1 audience-aware drafting + full pipeline doctrine at [`../memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) (canonical, mirrored from `~/.claude/projects/-Users-c17n-commons-bonds/memory/`); full doctrine artifact at [`../commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md).

**Purpose.** Reusable session-paste templates for any drafting task in the *Commons Bonds* project. Each template is a starting point: fill in the `[BRACKET PLACEHOLDERS]`, paste into a fresh session, the session executes.

Templates are organized by the v3.1 pipeline's stages. **Not every drafting task needs all stages** — see the decision tree below.

---

## Files in this directory

| File | When to use |
|---|---|
| `stage-0-publishing-strategy-rigor-test.md` | Substantial publisher-facing derivative work that hasn't been ratified yet. Decides go/no-go + sequencing against book-success criteria BEFORE any drafting begins. |
| `stage-1-audience-aware-structure-pass.md` | Pre-draft brief building: audience pressure-test + canonical-facts inventory + structural decisions + voice register + carry-forward inventory. **Required for any publisher-facing drafting.** Now structured as 3 sub-steps: 1a invariant-gate scan + 1b substantive brief + 1c cross-artifact coherence check. |
| `stage-2-audience-blind-flow-draft.md` | Fresh-session audience-blind drafting from the Stage 1 brief. **Required for any publisher-facing prose >~500w** that derives from chapter/source prose (Path B preemptive policy). |
| `stage-3-three-pass-rigor-audit.md` | Post-draft rigor — **five distinct passes** per v3.1 Amendment B (2026-05-18): **3.1** fact-check + **3.2** voice-polish + **3.3** audience-load acceptance + **3.4** audience-load robustness (adversarial) + **3.5** developmental-edit (chapter-scale; restoration polarity). **Required for any publisher-facing prose >~500w** before submission. (Filename preserved across v2.0 → v3.0 → v3.1 evolution for cross-reference stability.) |
| `audience-pressure-test-construction.md` | Guide for building the audience pressure-test set adapted per venue. Reference from Stage 1 templates. |
| `op-ed-news-peg-activation-template.md` | **News-peg-triggered short-form activation** for the two pipeline-ready op-eds (Norway sovereign-wealth + McDowell true-cost). When a news event surfaces, paste the relevant activation prompt into a fresh session for 1–2-day-turnaround submission. |

**Stage 4 + Stage 5** (render + character-integrity audit; academic-rigor + prose-quality sign-off + pre-pub review queue artifact) do not yet have dedicated templates in this directory — they are codified in `../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md` and `../commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`. **First chapter through each stage builds the template** (currently Ch 1 is queued to be first through Stage 5; will produce the template).

---

## The generic drafting-trigger paste-text scaffold

When you want to fire a new drafting workstream from scratch, this is the meta-template that scopes the session for the model. Customize the bracketed fields; paste into a fresh session.

```
You are a fresh session firing the [STAGE 0 / STAGE 1 / STAGE 2 / STAGE 3
PASS X.Y / STAGE 4 / STAGE 5 / specific custom task] for:

  Workstream: [name of the workstream — e.g., "Atlantic Ideas essay"]
  Artifact:   [path to the artifact OR "new artifact at <expected path>"]

CONTEXT — what you need to know to operate:

  - Source material: [chapter file path(s), interview transcript,
    Stage 1 brief, prior Stage 2 draft — be explicit]
  - Destination: [specific venue / chapter / file path]
  - Strategic purpose: [which book-success criterion or
    publishing-pipeline goal does this serve?]
  - Audience: [specific venue's editorial brain + reader; reference
    audience-pressure-test-construction.md venue table]
  - Length: [target band + ceiling — substance drives length per
    feedback_substance_drives_length.md]
  - Voice register: [memoir / literary-philosophical / op-ed /
    methods-note / academic / trade-publishing / institutional-policy]
  - Constraints: [no apparatus / no Path B / specific consent
    requirements / specific framing conditions / explicit-meta
    moves required per Condition 1]
  - Locked elements: [title / opening line / closing paragraph /
    specific named subjects — what cannot change]

REQUIRED READS (in order):

  1. CLAUDE.md (project workflow doctrine — branch discipline, merge
     defaults, hard constraints)
  2. tools/memory/feedback_audience_aware_drafting_discipline.md
     (v3.1 pipeline; this stage's role within the cascade)
  3. tools/memory/feedback_named_subject_consent.md (if any real
     person may be named or referenced)
  4. tools/memory/feedback_verify_stale_memory_claims.md (always)
  5. tools/memory/feedback_em_dash_overuse.md (if drafting prose)
  6. tools/memory/feedback_substrate_critical_editorial_input.md (if
     working from author-supplied substrate)
  7. tools/commons_bonds_pipeline_doctrine_v1.0.0.md (full doctrine)
  8. The stage-specific template from tools/drafting-templates/
     matching this session's stage
  9. [WORKSTREAM-SPECIFIC HANDOFF: tools/workstream-handoffs/
      <workstream>-handoff_<date>.md]
  10. [PRIOR ARTIFACTS: any PROPOSED / RATIFIED rigor passes,
      prior Stage drafts, source chapter, brief]

DO:

  - Follow per-prompt serial cadence (this prompt = one pass; do
    NOT bundle multiple Stage-3 passes into a single session)
  - Per v3.1 Amendment C, use Interactive Ratification Protocol
    format if this is a prose-modifying pass: for each finding,
    present Options + Recommendation + Reasoning; author ratifies
    in-session
  - Present findings/decisions ONE AT A TIME. Track the full
    findings list internally (organized by severity HIGH → MED →
    LOW). Show the author exactly ONE finding at a time in
    canonical format (Problem / Options / Recommendation /
    Reasoning). Wait for author disposition before showing the
    next. NEVER dump a full findings inventory in a single output
    — that breaks the parallel-session-hop cadence the author
    uses to work multiple rigor sessions concurrently. (See
    tools/memory/feedback_parallel_session_ratification_cadence.md.)
  - Severity-strict ordering: HIGH → MED → LOW; never interleave.
  - Use STANDARDIZED STATUS MARKERS in any output where the author
    needs to act, decide, or move stages:
      🔴 AUTHOR DECISION REQUIRED: [what specifically; brief]
      🟡 SUB-SESSION NEEDED: [what to fire; paste-text source or inline]
      🟢 NEXT STAGE READY: [what stage; what to confirm to advance]
      🔵 ESCALATION: [structural issue worth discussion before continuing]
  - End the session with a standardized one-line state summary:
    STATE: [PROPOSED|APPLIED|RATIFIED]; NEXT: [author-action-required|
    sub-session-fires|automatic]; AWAITING: [author-ratification|
    sub-session-X|external-X]
  - Verify all time-sensitive claims against current state (per
    feedback_verify_stale_memory_claims.md)
  - Apply Path B audit if drafting from chapter source
  - Apply named-subject consent discipline if any real person is
    named or referenced
  - PROPOSE — do not auto-apply prose-modifying changes unless
    this is an explicit Phase C application session

DO NOT:

  - Bundle stages (e.g., do Stage 1 and Stage 2 in same session)
  - Skip the discipline reads even if "I've read this before" —
    fresh session has no memory
  - Auto-merge to main without confirming this is an author-
    ratified change set (per CLAUDE.md merge-to-main default)
  - Use process-scaffolding vocabulary in publisher-facing prose
    ("Option A", "ratified", "Phase C-α", INCLUDE/EXCLUDE glyphs)
  - Use em-dashes as default punctuation (per
    feedback_em_dash_overuse.md — flag, restructure, default to
    commas/periods)

OUTPUT FORMAT:

  - This stage's canonical artifact format (see stage template)
  - PROPOSED suffix in filename if propose-only
  - Recommended commit message + git branch name
  - Pre-merge checklist:
    a. Pre-commit hook ran clean (check-corpus-invariants.sh)
    b. Artifact follows stage's canonical format
    c. All required reads documented
    d. No stage-bundling violations
    e. Author ratification required before next stage fires

BRANCH:

  - Open with: git checkout -b claude/[workstream-shortname]-<harness-id>
    from current origin/main after git fetch
  - Per CLAUDE.md: propose-only artifacts auto-fast-forward merge to
    main at session close; author-ratified content changes also
    auto-merge; direct content edits without prior ratification stop
    at feature branch
```

**How to use:** This scaffold is the umbrella that wraps any of the stage-specific templates. The stage template tells the session HOW to do the work; this scaffold tells the session WHAT to do + the context it needs. For complex sessions, both are paste-text inputs.

---

## Decision tree — which stages to fire

```
What are you drafting?
│
├── Body paragraph / section inside an existing manuscript chapter (<~500w)
│   → Skip Stage 0. Use a "mini Stage 1" (10-min audience-load
│     + canonical-facts check in your head). Stage 2 + Stage 3
│     compressed to a single session.
│   → Pass 3.5 (developmental-edit) typically NOT applicable
│     (chapter-scale only).
│   → Examples: flagship-term defense paragraphs (CIT / ARR /
│     Externality Tail).
│
├── New short-form publisher-facing piece (~700–1,200w op-ed,
│   blurb, short essay)
│   → Skip Stage 0 if the piece is already in cascade plan + the
│     venue is already cleared. Run Stage 0 if it's a new venue.
│   → Run Stage 1 + Stage 2 + Stage 3 (passes 3.1–3.4); Pass 3.5
│     is generally not applicable at this length.
│   → Example: op-ed pipeline drafts (Norway + McDowell, 2026-05-10);
│     subsequent news-peg activations are NOT a full pipeline fire
│     but a Stage-3-light activation per
│     op-ed-news-peg-activation-template.md.
│
├── New long-form publisher-facing essay (~3,000–5,000w magazine essay)
│   → Run Stage 0 if (a) it's a new venue OR (b) it would reveal
│     >15% of book apparatus OR (c) it could code Commons Bonds as
│     politically partisan.
│   → Always run Stage 1 (with all three sub-steps 1a/1b/1c) + Stage 2
│     + Stage 3 (all five passes 3.1 → 3.5 by chapter-scale; light
│     bundle 3.3+3.4 if essay is short and adversarial-robustness is
│     unlikely to surface findings).
│   → Stage 2 MUST be a fresh session (audience-blind discipline).
│   → Pass 3.5 (developmental-edit) IS applicable for essays
│     >~3,500w — surfaces emotional-arc continuity, scene-anchor
│     density, sensory-detail restoration, voice-flow continuity.
│   → Stage 4 + Stage 5 are explicit-gate (per v3.1 Amendment A
│     two-class cascade) — fire at venue change / pre-publication /
│     cross-chapter workstream close / author "build it now" trigger.
│   → Example: $100 Barrel essay for Phenomenal World; Boston Review
│     essay; Noema essay; Atlantic Ideas essay.
│
├── Book chapter (full Stage 3 cycle)
│   → All five passes per v3.1 (3.1 + 3.2 + 3.3 + 3.4 + 3.5).
│   → Per-prompt serial cadence: each pass fires in its own prompt;
│     author ratifies + Phase C application before next pass fires.
│   → Per v3.1 Amendment A: 3.1 + 3.2 auto-fire on every prose
│     edit; 3.3 + 3.4 + 3.5 are explicit-gate.
│   → Stage 4 + 5 explicit-gate (fire at distribution-readiness).
│
├── Book-proposal section (e.g., §00 overview, §01 market-and-audience,
│   §04 marketing plan)
│   → Skip Stage 0 (book proposal is in pipeline; no go/no-go).
│   → Run a modified Stage 1 (audience = literary agents + acquiring
│     editors; structural conventions = trade-publishing-norm).
│   → Stage 2 can be bundled with Stage 1 if the section is
│     non-derivative (no chapter source to contaminate against).
│   → Stage 3 audience-load passes only; fact-check + voice-polish
│     can be inline.
│
├── Manuscript revision / polish (existing chapter prose)
│   → Skip Stage 0 + Stage 1 + Stage 2 entirely. This is a Stage-3-
│     style five-pass audit applied to existing prose.
│   → Use Stage 3 template; specify "audit-existing-prose" mode.
│
├── Internal-scaffolding artifact (handoff doc, audit doc, decisions
│   log entry, glossary entry, PM session dashboard)
│   → Skip all stages. Use the internal-scaffolding register; no
│     audience-load rigor needed.
│
└── Email / correspondence / cover letter / pitch (short, personal)
    → Skip all stages for the email itself. The cover letter for a
      submission essay IS subject to a brief audience check (which
      editor at which venue? what tone matches the venue?).
    → Cover letters for active submissions: bundle with the
      submission packet's Stage 5 sign-off.
```

---

## How to scale up or down

The v3.1 discipline is the **maximum-rigor** path. For lower-stakes work, scale down:

| Stakes | Stage 0 | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 |
|---|---|---|---|---|---|---|
| Major publisher-facing essay (new venue, potential book-impact) | ✓ Full | ✓ Full (1a + 1b + 1c) | ✓ Full fresh-session | ✓ Five distinct passes (3.1 → 3.5) | ✓ at pre-pub | ✓ at pre-pub |
| Pipeline-already-cleared publisher-facing essay | Skip | ✓ Full | ✓ Full fresh-session | ✓ Five passes (3.5 confirm-applicable at length) | ✓ at pre-pub | ✓ at pre-pub |
| Op-ed / short publisher-facing piece (~900w) | Skip | ✓ Light | ✓ Fresh-session OK | ✓ Passes 3.1–3.4 (3.5 typically n/a at op-ed length) | Skip (no render-toolchain question) | ✓ Light at pre-pub |
| In-book defense paragraph (~300w) | Skip | ✓ Inline mini-brief | ✓ Bundled with Stage 1 | ✓ Single audience-load pass | Skip | Skip |
| Book-proposal section | Skip | ✓ Modified for trade-publishing audience | ✓ Bundlable | ✓ Light audience-load | Skip | ✓ at proposal-submission |
| Revision of existing prose | Skip | Skip | Skip | ✓ Apply audit-existing-prose mode | Skip | Skip |
| Internal scaffolding | Skip | Skip | Skip | Skip | Skip | Skip |

---

## v3.1 Amendment A — two-class cascade (token economy)

Per Amendment A (ratified 2026-05-18), Stage 3 passes split into two firing classes:

**Automatic-on-edit cascade (cheap; fires on every prose edit):**
- Pass 3.1 fact-check
- Pass 3.2 voice-polish
- Stage 1c-light cross-artifact coherence check
- Cost: ~10K–30K tokens per prose-edit event
- Justified by value-added prose rigor

**Explicit-gate cascade (heavy; fires only on author trigger at specific gates):**
- Pass 3.3 audience-load acceptance
- Pass 3.4 audience-load robustness
- Pass 3.5 developmental-edit
- Stage 4 render + character-integrity audit
- Stage 5 academic-rigor + prose-quality sign-off + pre-pub review queue artifact
- Trigger conditions: venue change · pre-publication · cross-chapter workstream close · author "build it now" / "developmental read-through" trigger
- Cost: ~40K–160K tokens per pre-pub batch; amortized over many prose edits

**Practical implication:** if you're firing a "polish" session on a chapter, the automatic cascade is fine (3.1 + 3.2). If you're preparing for submission or end of cross-chapter work, fire the explicit-gate cascade.

---

## v3.1 Amendment B — Pass 3.5 developmental-edit codified

**Restoration polarity, not cutting polarity.** Pass 3.2 cuts (verbosity, em-dashes, LLM tics); Pass 3.5 restores (emotional-arc continuity, scene-anchor density, sensory-detail restoration, reader engagement at analytical pivots, voice-flow continuity, cumulative-LLM-cadence residue). Folding 3.2 and 3.5 would lose the discipline each needs.

**When it fires:** AFTER Pass 3.1 + 3.2 + 3.3 + 3.4 ratify-and-apply complete. Whole-chapter scale; ~50K–80K tokens per chapter. Explicit-gate per Amendment A.

**Empirical grounding:** Ch 1 developmental-edit review 2026-05-18 (3 HIGH + 7 MEDIUM + 3 LOW findings). HIGH findings clustered around: scene-anchor restoration, sensory-detail restoration, both/and reveal breath, framework-close breath, faithfulness-of-the-model lineage.

**Post-3.5 routing:** Light Pass 3.3 re-fire recommended after Phase C application of ratified Pass 3.5 spot-fixes; Pass 3.4 re-fire NOT routinely warranted (restorations strengthen adversarial robustness rather than weaken it).

**Applicability test:** Pass 3.5 is applicable to chapter-scale work + long-form essays (~3,500w+). For ~900w op-eds, typically not applicable — verify at PROPOSED stage if a pass fires.

---

## v3.1 Amendment C — Interactive Ratification Protocol

For prose-modifying passes (3.1, 3.2, 3.5, Stage 5 sign-off rev, Phase C applications), the ratification cadence is **interactive** — author and Claude work in the same session.

**Per-finding format:**
- Finding description (location + nature of issue)
- **Options** — at least two; numbered; show each alternative phrasing
- **Recommendation** — Claude's pick + 1-line reason
- **Reasoning** — why this finding matters + why this option

Author responds with disposition (Option N / hold / cut / amend). Ratification + application combine in one session — no separate Phase C handoff needed.

**Where this changes prior practice:** older PROPOSED → Phase C → APPLIED pattern was sequential across multiple sessions. Amendment C compresses this into a single interactive session for fast cycles. Used in: Ch 6 Pass 3.5 (RATIFIED + APPLIED 2026-05-21 via single interactive session); $100 Barrel Pass 3.5 (RATIFIED + APPLIED 2026-05-23 via interactive); $100 Barrel Pass 3.2 (RATIFIED + APPLIED 2026-05-21).

---

## Picking the right rigor tests

Rigor tests beyond the v3.1 five-pass Stage 3:

| Test | When to apply |
|---|---|
| **Path B audit** | When draft derives from chapter prose. Test for verbatim sentences + structural close-paraphrase. Reference: `research/audits/cross-chapter-path-b-audit_2026-05-11.md`. |
| **Named-subject consent** | When draft uses real names of living subjects in publisher-facing prose. Reference: [`../memory/feedback_named_subject_consent.md`](../memory/feedback_named_subject_consent.md). |
| **Framework-positioning** | When draft engages framework apparatus terms (CS, RCV, Bond, CIT, ARR, etc.). Check FPD v1.0.0 alignment. Reference: `alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`. |
| **Apparatus register** | When draft uses framework symbols / Greek letters / acronyms. Trade-press body prose should be apparatus-light. |
| **Cross-chapter consistency** | When draft references named cases (Libby, McDowell, Mondragon, Norway, Chesapeake) or recurring statistics. |
| **Layman-lookup discipline** | When draft cross-references the Tech Appendix or theorem numbers. Format: "[Named Concept] (Technical Appendix §X.Y, Theorem X.Y)". |
| **Substance-drives-length** | Always. No padding to hit a number; no cutting to fit. Reference: [`../memory/feedback_substance_drives_length.md`](../memory/feedback_substance_drives_length.md). |
| **Verify-stale-memory-claims** | Always. Verify counts, dates, file paths, statuses against current ground truth. Reference: [`../memory/feedback_verify_stale_memory_claims.md`](../memory/feedback_verify_stale_memory_claims.md). |
| **Two-layer content origination** | Always. Classify draft as internal-scaffolding vs. external-publisher-facing before drafting begins. Reference: [`../memory/feedback_two_layer_content_discipline.md`](../memory/feedback_two_layer_content_discipline.md). |
| **Em-dash overuse** | When drafting prose. Treat em-dash use as a flag requiring active justification, not a default. Reference: [`../memory/feedback_em_dash_overuse.md`](../memory/feedback_em_dash_overuse.md). |
| **Dual-audience layman+specialist test** | When polishing register or apparatus. Test against BOTH audiences explicitly. Reference: [`../memory/feedback_dual_audience_test.md`](../memory/feedback_dual_audience_test.md). |
| **Invariant-gate scan** | Per Stage 1a; runs automatically via `tools/scripts/check-corpus-invariants.sh` pre-commit hook + every stage transition + CI. Catches scaffolding patterns + regressed patterns. |

---

## Audience picking — quick reference

**Default audience pressure-test set** for publisher-facing work: see [`audience-pressure-test-construction.md`](audience-pressure-test-construction.md).

**Venue-specific adaptations (current pipeline + parked venues):**

| Venue | Status | Audience adjustment from default |
|---|---|---|
| **Aeon** | In-pipeline (Aeon Pitch *The Mask of Abundance*) | Add literary-philosophical reader; weight thought-experiment toleration; lighter on policy-mechanism specificity |
| **Noema** | In-pipeline | Three-register weave (memoir + history/theory + reportage); add internationalist scope; named-sources-with-cited-public-record |
| **Boston Review** | In-pipeline (Ch 5 derivative) | Institutional / policy-centrist; add policy-economics reader; Condition 1 (non-partisan framing) dispositive — flag explicit-meta disarming moves at Stage 2 (per $100 Barrel comparative audit anchor) |
| **Phenomenal World** | In-pipeline ($100 Barrel essay) | Heterodox-econ / political-economy academic-adjacent; add center-right reader for non-partisan-framing test; Condition 1 dispositive |
| **Atlantic Ideas** | In-pipeline (Ch 9 derivative) | Name-recognition prestige; expects established bylines; long-form magazine voice |
| **Foreign Policy** | Alt reframe for Atlantic Ideas | International-policy reader; mechanism-focused; tighter than Atlantic Ideas |
| **Project Syndicate** | Parked (op-ed alt) | Financial / policy short-form; add international-reader |
| **Bloomberg Opinion / FT Opinion** | In-pipeline (op-eds, news-peg-triggered) | Markets-aren't-fake reader; explicit-meta-disarming for full-cost arguments; non-partisan register |
| **NYT / WaPo Opinion** | Stretch for op-eds | General educated reader; lighter on jargon; news-peg essential |
| **Guardian Long Read / Guardian Opinion** | Stretch for op-eds | International scope; reads true-cost / climate-damages arguments more readily than U.S. opinion pages |
| **Berggruen Prize** | Parallel AI-free track | Philosophical depth + accessibility; free brief; jury reads for argument originality |
| **Real-World Economics Review** | Parked (cascade-plan A3) | Heterodox-econ formalization; methods-note register |
| **Trade-publisher acquiring editor** | In-pipeline (book proposal) | Add commercial-arc reader; emphasize bookstore-buyer hook |
| **Literary agent** | In-pipeline (Wave 1 late Jul / early Aug 2026) | Add comp-titles-evaluator reader; pitch evaluates platform-paragraph rigor |

See [`audience-pressure-test-construction.md`](audience-pressure-test-construction.md) for the full construction guide.

---

## Giving context for what to draft (9 fields)

Every Stage 1 brief (and the generic drafting-trigger paste-text above) should specify:

1. **What** — the artifact (essay / paragraph / pitch / op-ed / etc.)
2. **Where** — the destination (specific venue / chapter / file path)
3. **Why** — strategic purpose (which book-success criterion does this serve?)
4. **Who** — audience (specific venue's editorial brain + reader)
5. **Length** — target band + ceiling (substance drives length within bounds)
6. **Voice** — register (memoir / literary-philosophical / op-ed / methods-note / academic)
7. **Source material** — what the draft draws on (chapter X, interview transcript, source essay, etc.)
8. **Constraints** — anything specific (no apparatus / no Path B / specific consent requirements / specific framing conditions; explicit-meta moves required per Condition 1)
9. **Locked elements** — what cannot change (title / opening line / closing paragraph / specific named subjects)

Stage 0 templates ask higher-level versions of these against book-success criteria.

---

## Canonical examples in the project

For each stage, recent worked examples (refreshed 2026-05-24):

| Stage / Pass | Worked example |
|---|---|
| Stage 0 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_100_barrel_essay_q1_go_no_go_v1.0.0.md` |
| Stage 0 (essay-side) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_boston_review_essay_stage_0_publishing_strategy_v1.0.0.md` |
| Stage 1 (long-form) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_atlantic_ideas_essay_pre_draft_audience_structure_v1.0.0.md` |
| Stage 1 (short-form) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_pre_draft_audience_structure_v1.0.0.md` |
| Stage 2 | `manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md` (Draft A; comparative-audit-winning execution) |
| Stage 2 (parallel-variant comparative) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_stage3_comparative_draft_audit_v1.0.0.md` |
| Stage 3 Pass 3.1 (fact-check) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_atlantic_ideas_essay_factcheck_v1.0.0.md` |
| Stage 3 Pass 3.2 (voice-polish) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_boston_review_essay_stage3_voice_polish_v1.0.0.md` |
| Stage 3 Pass 3.3 (audience-load acceptance) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_boston_review_essay_stage3_audience_load_v1.0.0.md` |
| Stage 3 Pass 3.3 (light re-fire after dev-edit) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_noema_essay_pass_3_3_light_rerefire_v1.0.0.md` |
| Stage 3 Pass 3.4 (adversarial robustness) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_100_barrel_essay_pass_3_4_audience_load_robustness_light_v1.0.0.md` |
| Stage 3 Pass 3.5 (developmental-edit) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_100_barrel_essay_pass_3_5_developmental_edit_v1.0.0.md` |
| Stage 5 sign-off (essay) | Boston Review essay Stage 5 RATIFIED 2026-05-23 (`d34214d`); $100 Barrel Stage 5 RATIFIED 2026-05-24 (`0266525`) |
| Bundled mini-pipeline (in-book paragraph) | `tools/drafts/why-bonds-paragraph_2026-05-11_v1.0.0.md` + audience-load rigor pass |
| Stage 3 comparative-draft audit (parallel variants) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_100_barrel_essay_stage3_comparative_draft_audit_v1.0.0.md` |
| Op-ed news-peg activation | (template at [`op-ed-news-peg-activation-template.md`](op-ed-news-peg-activation-template.md); first real activation pending news-peg trigger) |

Mirror these when adapting templates.

---

## Empirical anchors (drafting discipline)

Three load-bearing empirical anchors validate the discipline:

1. **Noema Path-B audit (2026-05-10)** — audience-blind Stage 2 dropped verbatim sentences from ~17–22 (Path-B-contaminated draft) to ~3–4. Validated audience-blind discipline.
2. **Ch 1 developmental-edit review (2026-05-18)** — 3 HIGH + 7 MEDIUM + 3 LOW findings; clustered around scene-anchor restoration, sensory-detail restoration, framework-close breath. Empirically grounded Pass 3.5 codification (Amendment B).
3. **$100 Barrel comparative-draft audit (2026-05-21)** — two parallel Stage-2 drafts of same brief; differential was execution choice (explicit-meta Condition-1-disarming moves vs embedded-disarming). Anchored Condition 1 explicit-meta flag for Stage 1 briefs with dispositive non-partisan audiences.

---

## Maintenance

This directory grows as drafting patterns evolve. When a new pattern emerges from a workstream (e.g., the op-ed news-peg activation pattern 2026-05-24; the comparative-draft audit pattern 2026-05-21), add it here.

**Updates to the v3.1 discipline** (memory file [`../memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md)) should propagate to this README within the same session.

---

## Refresh log

- **2026-05-11.** Initial README. v2.0 discipline.
- **2026-05-24.** Refresh to v3.1 (Amendments A + B + C). Added: generic drafting-trigger paste-text scaffold; Pass 3.5 + Stage 4 + Stage 5 entries throughout; two-class cascade explainer; Amendment C Interactive Ratification Protocol explainer; op-ed news-peg activation template entry; updated canonical examples (refreshed against 2026-05-21+ rigor-pass artifacts); updated venue table (in-pipeline vs parked); updated empirical anchors. Memory references switched from `~/.claude/projects/.../memory/` to `tools/memory/` mirror (canonical post-migration 2026-05-17).

---

*End of README.*
