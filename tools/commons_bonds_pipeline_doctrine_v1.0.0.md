# Commons Bonds — Pipeline Doctrine (v1.0.0)

**Date drafted:** 2026-05-17
**Status:** PROPOSED — pending author ratification at session close.
**Origin:** Pipeline-revision workstream (handoff at [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](workstream-handoffs/pipeline-revision-handoff_2026-05-17.md)); 11 decisions, 11 ratified at session start of 2026-05-17 (decisions #7 + #9 + #10 ratified within the originating brainstorm; decisions #1 + #2 + #3 + #4 + #5 + #6 + #8 + #11 ratified at the doctrine-session opening per author confirmation).
**Supersedes nothing.** Extends the existing v2.0 Amendment B of `feedback_audience_aware_drafting_discipline.md` (memory entry stays current with summary + pointer to this artifact per ratified decision #8 hybrid approach).
**Canonical reference for:** all Phase A per-chapter rigor cycles + retrofit cycles + future drafting sessions for publisher-facing prose.

---

## §0. Purpose + framing

This doctrine codifies the **single unified pipeline** that every publisher-facing artifact moves through, from author conception (Stage 0) through pre-publication-ready sign-off (Stage 5). The structure is six stages with content-type-aware sub-protocols at each stage, continuous invariant-gate scans, and an explicit change-cascade routing protocol that routes any change back to the appropriate prior stage.

The architecture takes lessons from the NIH peer-review pipeline the author ran early in his career:

> *"That pipeline had fact checks revisions and at the beginning. Then academic & peer review. Then consider the right artifact and associated verbiage based on the end audience. Then we had people looking at the prose flow and verbiage. Then we had people looking at the typography and layout. And then another final gate of peer reviews and anytime something was added or changed I you automatically got kicked backwards through the cycle to whichever stage was appropriate."*

Specific frictions the doctrine resolves (surfaced by the Ch 1 Pass 3 REAUDIT v3 cycle):

- Bibliography commitments + AuthorsNote framings + sibling-chapter cross-references surfacing mid-Pass-3 rather than pre-Pass-3 (Stage 1c cross-artifact coherence resolves this).
- New facts arriving mid-pass without a structured routing protocol (change-cascade §3 resolves this).
- Audience-load conflating acceptance + robustness tests on a single character set (Pass 3.3 acceptance + Pass 3.4 robustness split resolves this).
- Render-integrity issues (tofu-box / formula corruption) emerging ad-hoc at publishing time (Stage 4 render-integrity audit resolves this).
- Cross-chapter workstreams lacking a defined lifecycle (Stage-1c-routed §3.5 lifecycle resolves this).
- Process-scaffolding vocabulary leakage risk (Stage 1a continuous invariant scans resolve this).
- Math + prose treated as parallel pipelines drifting (single-pipeline + content-type sub-protocols resolve this).
- Pre-publication external review handed off ad-hoc (Stage 5 pre-publication review queue as mandatory deliverable resolves this).

---

## §1. Stage architecture

| Stage | Purpose | Doctrine doc |
|---|---|---|
| **0** | Author conception / topic decision | [`tools/drafting-templates/stage-0-publishing-strategy-rigor-test.md`](drafting-templates/stage-0-publishing-strategy-rigor-test.md) |
| **1** | Ready-to-draft gate (three sub-steps: 1a invariant + 1b structure + 1c coherence) | [`tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) + [`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`](drafting-templates/stage-1-audience-aware-structure-pass.md) + [`tools/drafting-templates/audience-pressure-test-construction.md`](drafting-templates/audience-pressure-test-construction.md) |
| **2** | Audience-blind drafting | [`tools/drafting-templates/stage-2-audience-blind-flow-draft.md`](drafting-templates/stage-2-audience-blind-flow-draft.md) |
| **3** | Four-pass rigor audit (3.1 fact-check + 3.2 voice-polish + 3.3 audience-load acceptance + 3.4 audience-load robustness) | [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](drafting-templates/stage-3-three-pass-rigor-audit.md) (v3.0 codification of the four-pass split) |
| **4** | Render + character-integrity audit | [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) |
| **5** | Academic-rigor + prose-quality sign-off bookend + pre-publication review queue artifact | [`tools/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) |

---

## §2. Continuous infrastructure — invariant gates

**Two invariant scans run continuously: pre-commit + every stage transition + CI.**

### §2.1 Scaffolding scan

Detects placeholders + drafting-template scaffolding + process-scaffolding vocabulary that should never appear in publisher-facing prose:

- Placeholders (`TODO`, `TK`, `FIXME`, `XXX`, `[BRACKET]`).
- Drafting-template scaffolding (*"Let me explain"*, *"In this section…"*, *"The plain definition is this:"*).
- Process-scaffolding vocabulary (`Option A` through `Option Z`, `ratified`, `Phase C-*`, `F-V*`, `INCLUDE`/`EXCLUDE` glyphs `✓✓✓` / `⚠⚠⚠` used as verdicts, `EXCLUDE` / `INCLUDE` as standalone tokens).
- Meta-commentary tics (*"That is the whole sentence."*, *"What I mean to say is…"*).

Registry: [`tools/quality-gates/scaffolding-patterns.yaml`](quality-gates/scaffolding-patterns.yaml).

### §2.2 Regressed-pattern scan

Detects patterns previously fixed by rigor passes (corpus-wide institutional memory). Each entry traces back to the rigor-pass artifact + commit that surfaced + fixed the pattern.

Categories:
- **Named LLM tics** (F-V1 through F-V21 from the Pass 2 voice-polish inventory: nostalgia tic *"There are not many people like that anymore"*; cadence-repetition *"It changed me. It humbled me."*; etc.).
- **Deprecated terminology** (term-rename / synonym-drift / superseded-name patterns).
- **Gate-decision-banned patterns** (vendor names held OUT per CEO-era NDA gate; named-subject anonymization decisions; etc.).
- **Cross-chapter consistency-inventory items** (terminology + symbol + flagship-equation canonical-name commitments).
- **Render-failure patterns** (em-dash / approx-symbol tofu-box fixes; minus-into-box rendering artifacts; etc.).

Registry: [`tools/quality-gates/regressed-patterns.yaml`](quality-gates/regressed-patterns.yaml).

### §2.3 Severity tiers + allowlist mechanism

Both registries are severity-tiered:

- **HIGH** — block: commit / stage transition refused; author must address before proceeding.
- **MEDIUM** — flag: surface for review; do not block.
- **LOW** — informational: log only.

**Per-file allowlist** support for known-legitimate substantive uses of pattern-class terms. Allowlist format (per entry):

```yaml
- pattern: "pressure-test"
  files:
    - manuscript/chapters/Chapter__9_PricingHonestly__Draft.md:165  # line 165 — legitimate substantive verb
```

Allowlist entries must cite line number + rationale.

### §2.4 Scan placement

- **Pre-commit hook** (`.git/hooks/pre-commit`) — runs HIGH-severity check; refuses commit on HIGH match.
- **Stage-transition checklist** — every stage transition verifies both scans clean (per the doctrine docs for each stage).
- **CI workflow** — runs both scans + reports MEDIUM-severity findings; full registry update PRs trigger registry-validation step.

Implementation: [`tools/scripts/check-corpus-invariants.sh`](scripts/check-corpus-invariants.sh).

---

## §3. Change-cascade routing protocol

**Any change of any type routes back to the appropriate prior stage.** Explicit routing rules:

| Change type | Routes back to | Then re-fires |
|---|---|---|
| New fact discovered (interview; family conversation; external verification) | Stage 1b canonical-facts inventory update | Pass 3.1 fact-check for affected scope + Pass 3.2 voice-polish for affected prose + Pass 3.3 audience-load acceptance + (if claim-level material change) Pass 3.4 robustness |
| New audience character identified | Stage 1b audience pressure-test set update | Pass 3.3 audience-load acceptance + (if adversarial character) Pass 3.4 robustness |
| Bibliography commitment lands | Stage 1c cross-artifact coherence update | Affected chapter's Pass 3.3 audience-load (light) re-fire |
| Spot-fix applied (any phase / any pass) | Stage 1c cross-artifact coherence (light) | Pass 3.3 audience-load (light) re-fire — verify verdicts didn't shift |
| Cross-chapter workstream applies content to multiple chapters | Stage 1c cross-artifact coherence for all affected chapters | Each affected chapter's Pass 3.3 audience-load (light) re-fire |
| Render-failure pattern surfaces | Stage 1a (registry update) + Stage 4 audit protocol amendment | Stage 4 re-run for affected chapter |
| External-reviewer finding lands | Stage 1c cross-artifact coherence + Stage 5 sign-off re-fire | Affected stages per finding scope |
| Any source-file change (pre-commit) | Stage 1a invariant-gate scans (automatic) | Commit refused on HIGH match; otherwise proceeds |

**Light re-fire** means: re-test only the specific characters / facts / sections affected by the change, not the full pass. Full re-fire only when the change is structural or invalidates the prior pass's assumptions.

---

## §4. Single-pipeline architecture (not parallel pipelines)

Math, prose, tables, and figures all move through the same pipeline. **Content-type-aware sub-protocols at each stage** handle the type-specific work. A pre-processing step generates a content-type inventory for each artifact (`lines X-Y: prose; lines Z-W: math; lines V-U: table-data; etc.`) which then routes through stage-internal sub-protocols.

### §4.1 Content-type sub-protocols by stage

| Stage | Prose sub-protocol | Math sub-protocol | Tables sub-protocol | Figures sub-protocol |
|---|---|---|---|---|
| 1b | Canonical-facts inventory + audience pressure-test character set | Canonical-formula inventory + numerical-constants inventory + **baseline render test** | Canonical-data inventory + baseline render test | Source verification + caption verification |
| 1c | Cross-artifact coherence against bibliography + AuthorsNote + sibling-chapter prose | Cross-artifact formula consistency + Tech Appendix sync | Cross-chapter data consistency | Cross-chapter figure-numbering + cross-reference consistency |
| 2 | Audience-blind flow draft | Math composition with render-safety conventions | Table composition with render-safety conventions | Figure placement + caption composition |
| 3.1 | §6 + public-record fact-check | Formula + constants + derivation-chain verification | Cell-by-cell data verification | Source verification (re-check) |
| 3.2 | LLM-tic + register-consistency + rhythm | Notation + symbol-usage + inline-vs-display consistency | Caption + header consistency | Caption consistency + alt-text |
| 3.3 / 3.4 | Audience pressure-test (acceptance + robustness) | Math-content audience-load (does the apparatus carry the load it claims to carry, for the audiences that read it?) | Audience-load (does the table communicate cleanly?) | Audience-load (does the figure communicate cleanly?) |
| 4 | Source-vs-rendered character diff for prose | Formula-integrity audit (rendered formula matches source byte-for-byte; no minus-into-box; no Greek-letter substitution; no subscript-stripping) | Table-rendering audit (alignment; cell-integrity; no truncation) | Figure-rendering audit (no crop; no resolution-loss; alt-text fires) |
| 5 | Prose-quality sign-off + pre-pub review queue prose section | Math academic-rigor sign-off + pre-pub review queue math section (external-reviewer flag where applicable) | Table sign-off | Figure sign-off |

### §4.2 New content types

When a new content type arrives (e.g., embedded interactive figure; audio clip; data download), add it as a new sub-protocol within each stage. The pipeline structure does NOT branch into a parallel pipeline.

---

## §5. Cross-chapter workstream lifecycle

Cross-chapter workstreams (those touching multiple chapters; e.g., the rent-seeking-engagement workstream surfaced by Ch 1 Pass 3 REAUDIT v3's adversarial test) get a first-class lifecycle:

1. **Surfaces.** Typically from a Pass 3.4 thread-pull synthesis, a Pass 3.1 cross-chapter-fact-drift discovery, or an external trigger (peer-review feedback; external-reviewer finding; bibliography commitment landing).
2. **PM session ratifies.** PM session reviews the surfacing artifact + spins up the workstream in `tools/workstream-handoffs/` + creates a cross-thread-todos entry.
3. **Workstream session applies cross-chapter touches.** Single feature branch (`claude/<workstream>-<harness-id>`); all touched chapters edited in the same branch; author ratifies the cross-chapter touch set.
4. **Per-chapter re-fire cascade fires automatically.** Each touched chapter triggers Stage 1c cross-artifact coherence (light) + Pass 3.3 audience-load (light) re-fire. Each re-fire is its own session per branch discipline.
5. **Closure gate.** Workstream closes only after all affected chapters' light re-fires complete clean. If any re-fire surfaces new findings, the workstream re-opens for additional touches + the per-chapter re-fires re-run.
6. **Artifact disposition.** Cross-thread-todos entry resolved + workstream-handoff archived + memory + MEMORY.md index updated.

---

## §6. Bookend sign-offs (Stage 1 + Stage 5)

**Both academic-rigor AND prose-quality sign-offs at both ends of the pipeline.**

### §6.1 Stage 1 sign-off (ready-to-draft gate)

After Stage 1 (1a + 1b + 1c) completes, two sign-offs gate Stage 2 firing:

- **Academic-rigor sign-off.** Canonical-facts inventory complete + verified against sources; canonical-formula inventory complete + verified against Tech Appendix; cross-artifact coherence verified; bibliography commitments inventoried + scoped into the brief.
- **Prose-quality sign-off.** Audience pressure-test character set complete + venue-appropriate; voice-register specification complete; LLM-tic avoidance list complete; locked elements verified + reproduced verbatim where applicable.

Both sign-offs author-ratified before Stage 2 fires.

### §6.2 Stage 5 sign-off (pre-publication gate)

After Stage 4 completes, two sign-offs gate publication readiness:

- **Academic-rigor sign-off.** No drift through pipeline; rendered output matches canonical-facts inventory; rendered formulas match canonical-formula inventory; cross-artifact coherence maintained; bibliography commitments realized in final prose; pre-publication review queue artifact populated with what-has-been-verified + what-has-NOT-been-verified + recommended external reviewer types.
- **Prose-quality sign-off.** Pass 3.2 voice-polish findings resolved or held-with-rationale; rendered prose maintains voice register; no regressed-pattern matches; pre-publication review queue artifact captures any unresolved prose-quality items.

Both sign-offs author-ratified before manuscript ships to publisher / agent / editor.

---

## §7. Pre-publication review queue (mandatory Stage 5 deliverable)

**Generated at Stage 5 sign-off for each artifact.** Goes to publisher / agent / editor with the manuscript-submission package as transparent quality-control disclosure.

### §7.1 Contents

Each pre-publication review queue artifact contains:

1. **What has been internally verified.**
   - By whom (author + session log + PM session).
   - Against what sources (per the canonical-facts inventory § of the Stage 1 brief; cite specific sources where appropriate).
   - Through what passes (Pass 3.1 fact-check verdict; Pass 3.2 voice-polish verdict; Pass 3.3 audience-load acceptance verdict; Pass 3.4 robustness thread-pull synthesis verdict; Stage 4 render-integrity verdict).

2. **What has NOT been externally verified.**
   - Specific factual claims that would benefit from external corroboration (especially for archival material with limited public-record traces).
   - Specific mathematical / framework claims that would benefit from external technical review.
   - Specific framework-methodology claims that would benefit from external economist review in an adjacent tradition.

3. **Recommended external reviewer types** (for publisher to engage post-acceptance):
   - **Math reviewer:** technical reviewer with quantitative-economics / applied-mathematics background. For the Tech Appendix specifically: also flag formula-integrity post-render.
   - **Framework-methodology reviewer:** economist in an adjacent tradition (heterodox-econ; institutional-econ; resource-econ; Stern-tradition; Hartwick-tradition). Reads framework for methodological soundness vs adjacent traditions.
   - **Domain experts** where applicable: e.g., Chesapeake-watermen-history reader for Ch 3; coal-mining-history reader for Ch 2; etc.

4. **Highest-priority sections for external review if publisher budget is limited.** Per author preference, rank-ordered list.

### §7.2 Format

Pre-publication review queue artifact lives at `tools/pre-submission-reviews/[artifact-name]_pre_pub_review_queue_v1.0.0.md` (note: directory already exists per repository layout).

Template: see [`tools/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) §3.

### §7.3 Discipline

Transparent quality-control disclosure rather than overclaiming-verification posture. The queue is not a confession of weakness; it is a structural artifact identifying where external expertise adds value relative to internal verification capability.

External-reviewer engagement policy: per ratified decision #10 (2026-05-17 brainstorm), the author self-signs Stage 5 + explicitly flags at hand-off; college-tutors-as-bounded-bonus-capacity is the working arrangement for limited external review pre-publication. The pre-pub review queue is the structural artifact that surfaces what the publisher should engage post-acceptance.

---

## §8. Versioning + relationship to existing canonical artifacts

### §8.1 Hybrid versioning (per ratified decision #8)

- This doctrine artifact (`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`) is the **canonical reference** carrying the full architecture.
- The author's memory entry `feedback_audience_aware_drafting_discipline.md` is updated to **v3.0** with a concise summary + pointer to this artifact. Memory entry stays scan-friendly; doctrine artifact carries the full architecture. Memory-update spec is at [`tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`](memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md).

### §8.2 Extends, does not supersede

This doctrine **extends** v2.0 Amendment B; it does not supersede. v2.0 Amendment B's three-distinct-passes discipline (fact-check + voice-polish + audience-load) is preserved as the core of Stage 3. The new structure adds Pass 3.4 (audience-load robustness) as a fourth pass, splits Stage 1 into three sub-steps, adds Stage 4 + Stage 5, and codifies the change-cascade routing + the cross-chapter workstream lifecycle.

### §8.3 Existing template alignment

- `tools/drafting-templates/stage-1-audience-aware-structure-pass.md` — kept; this doctrine's Stage 1 sub-step 1b uses this template. Stage 1a + 1c are added as wrapper steps.
- `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` — **revised** to v3.0 framing (Pass 3 split into Pass 3.3 + 3.4; v2.0 Amendment B remains historical anchor).
- `tools/drafting-templates/audience-pressure-test-construction.md` — **amended** to add acceptance vs robustness character-set distinction + adversarial-detractor character types + severity scales for the adversarial test.
- `tools/drafting-templates/stage-0-publishing-strategy-rigor-test.md` — kept; Stage 0 doctrine unchanged.
- `tools/drafting-templates/stage-2-audience-blind-flow-draft.md` — kept; Stage 2 doctrine unchanged.

---

## §9. Retrofit policy (per ratified decision #9)

All chapters run through the new pipeline once the doctrine cluster lands. Retrofit does NOT mean re-doing every rigor pass from scratch — those are author-ratified + applied. Retrofit means applying the **new-to-the-pipeline elements** to existing chapters:

- Stage 1a invariant-gate scan (likely produces no leaks per the 2026-05-17 leak-check survey; verify per-chapter + record clean baseline).
- Stage 1c cross-artifact coherence check (likely surfaces small gaps similar to today's bibliography §21 / Ch-1 / Dunbar-Du-Bois mid-Pass-3 discovery).
- Pass 3.4 audience-load robustness test (chapters that have closed cycles had only the original acceptance-test version of Pass 3; adversarial-detractor robustness expansion is new).
- Stage 4 render + character-integrity audit.
- Stage 5 academic-rigor + prose-quality sign-off + pre-publication review queue artifact generation.

Per-chapter retrofit scope: see [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](workstream-handoffs/pipeline-revision-handoff_2026-05-17.md) §6.2.

Retrofit sequencing: see same handoff §6.3.

Retrofit workstreams spin up after this doctrine session merges to `main`. Per the cross-chapter workstream lifecycle (§5), each retrofit workstream is per-chapter; the doctrine cluster itself is not a cross-chapter workstream (it's tools/-side scaffolding).

---

## §10. Open questions captured as deferred items

This session ratified all 11 decisions; remaining open items (carry-forward from handoff §8 + this session):

1. **CI integration depth.** Initial CI workflow ships running both scans on push + on PR. Refinement (block-on-PR vs flag-only; merge-to-main run vs every-push run) deferred to first CI-iteration session.
2. **Pre-commit hook adoption.** Hook ships installable via `tools/scripts/install-pre-commit-hook.sh`. Mandatory-vs-optional adoption decision deferred to first usage cycle.
3. **External-reviewer engagement timeline for Tech Appendix.** Per ratified decision #10, flag-at-handoff is the policy. Timing of any college-tutor engagement is a PM-session decision after retrofit Tech Appendix Stage 5 fires.
4. **Allowlist mechanism refinement.** Initial allowlist format ships per §2.3. Refinement (regex contexts; AST-aware exclusion; pattern-class hierarchies) deferred to first allowlist-bottleneck case.
5. **Stage 5 sign-off mechanic for retrofit.** Author sign-off is sufficient for retrofit Stage 5; external-reviewer flag-pass for high-math-content artifacts (Ch 6 + Ch 9 + Tech Appendix) per author preference at retrofit time.

---

## §11. Quick-reference — when which stage fires

| Scenario | Stages that fire |
|---|---|
| New artifact from scratch (chapter; essay; pitch; op-ed) | 0 → 1 (1a + 1b + 1c) → 2 → 3 (3.1 → 3.2 → 3.3 → 3.4) → 4 → 5 |
| Chapter retrofit (already closed cycle) | 1a + 1c + 3.4 + 4 + 5 |
| Partial-cycle chapter retrofit | 1a + 1c + (passes not yet run) + 3.4 + 4 + 5 |
| Spot-fix application session | 1c (light) + 3.3 (light) — per change-cascade rule |
| Cross-chapter workstream | 1c (per affected chapter) + 3.3 (light, per affected chapter) — per §5 lifecycle |
| New fact arriving mid-pipeline | 1b update + 3.1 + 3.2 + 3.3 (+ 3.4 if material) — per change-cascade rule |
| New audience character arriving mid-pipeline | 1b update + 3.3 (+ 3.4 if adversarial) — per change-cascade rule |
| Bibliography commitment landing | 1c + 3.3 (light) — per change-cascade rule |
| External-reviewer finding landing | 1c + 5 sign-off re-fire (+ affected stages per finding scope) — per change-cascade rule |
| Source-file change | 1a (automatic via pre-commit hook) |

---

## §12. Hard constraints (recurring across all stages)

- Never force-push `main`; never amend a commit already on `origin/main`.
- Never skip hooks (`--no-verify`) without explicit author direction.
- Author ratifies all stage transitions for content-bearing artifacts. (Infrastructure-side artifacts — rigor-pass docs that propose spot-fixes without applying — autonomously merge per CLAUDE.md.)
- Named-subject consent gates Stage 1b (canonical-facts inventory) for any living named subject. Historical-record-only subjects do not require consent gating.
- Pre-publication review queue is **mandatory** at Stage 5; no exception for "we'll add this later."

---

## §13. References

- [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](workstream-handoffs/pipeline-revision-handoff_2026-05-17.md) — the originating handoff
- [`tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) — Stage 1 doctrine (three-step structure)
- [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) — Stage 4 doctrine (render + character-integrity audit)
- [`tools/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) — Stage 5 doctrine + pre-publication review queue template
- [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](drafting-templates/stage-3-three-pass-rigor-audit.md) — Stage 3 four-pass template (v3.0 framing)
- [`tools/drafting-templates/audience-pressure-test-construction.md`](drafting-templates/audience-pressure-test-construction.md) — character-set construction (acceptance + robustness)
- [`tools/quality-gates/scaffolding-patterns.yaml`](quality-gates/scaffolding-patterns.yaml) — scaffolding-scan registry
- [`tools/quality-gates/regressed-patterns.yaml`](quality-gates/regressed-patterns.yaml) — regressed-pattern-scan registry
- [`tools/scripts/check-corpus-invariants.sh`](scripts/check-corpus-invariants.sh) — invariant-check script
- [`tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`](memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md) — memory-entry update spec for v2.0 → v3.0

---

*End of Commons Bonds Pipeline Doctrine v1.0.0. PROPOSED 2026-05-17.*
