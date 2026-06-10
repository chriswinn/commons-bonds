# Pipeline-revision workstream handoff

**Date drafted:** 2026-05-17
**Workstream:** Pipeline-revision (drafting + fact-check + voice-polish + audience-load + rendering + sign-off pipeline doctrine — comprehensive revision)
**Status:** **PROPOSED** — awaiting PM session ratification of the remaining open decisions (§5) + spinup of dedicated drafting session. Origin: 2026-05-17 PM-session pipeline-revision brainstorm during the Ch 1 Pass 3 REAUDIT v3 closing window. **One decision ratified within this brainstorm:** decision #9 (retrofit policy) — author 2026-05-17 directed that *all chapters be run through the new pipeline once it is finished*. Remaining 10 decisions still pending author ratification (provisional answers captured).
**Recommended branch prefix:** `claude/pipeline-revision-`
**Recommended sequencing:** spin up after author ratifies the 10 remaining open decisions; produces the full doctrine artifact cluster (§4) in a single focused session.
**Origin commit:** session-close commit for the Ch 1 Pass 3 REAUDIT v3 workstream (commit family ending at `76ca8a6` + `779c0ef`; pipeline-revision brainstorm is the closing-window discussion after the rent-seeking workstream handoff landed).

---

## §0. Background — how this surfaced

During the Ch 1 Pass 3 REAUDIT v3 closing window (2026-05-17), the author proposed taking lessons from the NIH peer-review pipeline he ran early in his career to revise the current audience-aware-drafting-discipline pipeline. The NIH model:

> *"That pipeline had fact checks revisions and at the beginning. Then academic & peer review. Then consider the right artifact and associated verbiage based on the end audience. Then we had people looking at the prose flow and verbiage. Then we had people looking at the typography and layout. And then another final gate of peer reviews and anytime something was added or changed I you automatically got kicked backwards through the cycle to whichever stage was appropriate."*

The pipeline-revision conversation that followed identified several frictions in the current pipeline that the Ch 1 Pass 3 cycle itself made visible:

- **Bibliography §21 LOAD-BEARING Ch-1 chapter-relevance commitment was discovered mid-Pass-3** via a patent-verification search, not via a structured cross-artifact-coherence check. A pre-Pass-3 coherence gate would have made Item (iv) Dunbar/Du Bois "default-apply per existing bibliography commitment" rather than a 45-minute deliberation cycle.
- **Father conversation surfaced new facts mid-Pass-3** (lunar-lander honeycomb claim; pantograph patent; entire-career-at-NASA-Langley correction; roof-dropping factual error). We treated as ad-hoc Pass-1 follow-up + paragraph rewrite. A structured "new-fact-arrival routing protocol" would have routed each fact through Pass-1 verification first, then Pass-2 voice-polish, then back into Pass-3 audience-load.
- **Pass 3 audience-load character set expanded iteratively** (9 → 12 → 20 → 30 → 40 across four rounds in one session). A structured character-set construction step earlier in the pipeline would have built the full set upfront.
- **Public-Choice critique surfaced as a cross-chapter handoff** from the Pass 3.4 robustness test (the 40-character set's adversarial-detractor expansion). Cross-chapter workstreams emerging from per-chapter passes need a defined lifecycle that feeds back into per-chapter cycles.
- **Math + prose rendering risks** (per the existing repo's commit `d238f2c` for Ch 5 + Ch 6 tofu-box em-dash / ≈ fixes; Tech Appendix math-formula integrity concerns from the author's lived experience with rendered minus-into-box errors) require post-render content-integrity verification that the current pipeline doesn't structure.
- **Process-scaffolding vocabulary leakage** (Option A, ratified, Phase C, F-V1, INCLUDE/EXCLUDE glyphs, etc.) needs continuous invariant-gate scans across the corpus, not just per-stage checks.

This handoff captures the brainstorm + proposes the architecture + lists the artifacts the dedicated session needs to produce + flags the decisions still requiring ratification.

---

## §1. Current pipeline state (what exists)

Per memory entries + canonical templates:

- **Stage 0:** author conception / topic decision
- **Stage 1:** audience-aware structure pass (canonical-facts inventory + audience pressure-test character set construction); see [`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`](../../drafting-templates/stage-1-audience-aware-structure-pass.md) (if present) + [`tools/drafting-templates/audience-pressure-test-construction.md`](../../drafting-templates/audience-pressure-test-construction.md)
- **Stage 2:** audience-blind drafting (draft against the Stage 1 brief)
- **Stage 3:** three-pass rigor audit (Pass 1 fact-check + Pass 2 voice-polish + Pass 3 audience-load) per [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../../drafting-templates/stage-3-three-pass-rigor-audit.md)
  - Per-chapter cadence: Pass 1 → Phase C spot-fix → Pass 2 → Phase C spot-fix → Pass 3 → Phase C spot-fix
  - Per-prompt serial discipline (each pass author-ratified before next fires)
- **Phase A:** per-chapter rigor cycles (workstream #20)
- **Phase B:** whole-book audit (reads Ch 1 → Ch 10 in order; cross-chapter coherence; narrative-arc; reader-load arc)
- **Phase C:** per-chapter spot-fix application sessions (post-author-ratification)

**v2.0 Amendment B (current canonical):** fact-check + voice-polish + audience-load are three DISTINCT passes (not bundled); per-prompt serial cadence enforced.

**Publishing pipeline (currently separate):** markdown → .docx / HTML / PDF via `tools/scripts/build-derivatives.sh` (pandoc + xelatex / Chrome-headless / LibreOffice). Tofu-box rendering issues addressed ad-hoc per commits (`d238f2c` em-dashes / ≈ fix; `cf24f57` Chrome-vs-wkhtmltopdf switch; `3208619` EB Garamond font-family naming).

---

## §2. Friction points identified

From the 2026-05-17 brainstorm:

1. **No structured cross-artifact-coherence check.** Bibliography commitments, AuthorsNote framings, sibling-chapter cross-references, and existing rigor-pass artifacts are not surfaced systematically before rigor passes fire.

2. **No change-cascade routing protocol.** When new facts / new audience characters / new bibliography commitments / new spot-fixes land mid-stage, there is no formal routing rule for which prior stages re-fire.

3. **Audience-load conflates acceptance + robustness tests.** Pass 3 currently runs a single character set; today's Ch 1 REAUDIT v3 split into a 30-char acceptance set + 10-char adversarial-detractor set with different scoring scales. This split should be doctrine.

4. **Render-integrity not part of the rigor pipeline.** Typography / layout / character-integrity issues (tofu-box; font-fallback; math-formula corruption) emerge at the publishing-pipeline-scripts stage with no structured audit or sign-off.

5. **Cross-chapter workstreams lack a defined lifecycle.** Workstreams emerging from per-chapter passes (e.g., today's rent-seeking-engagement workstream) need a lifecycle that integrates with per-chapter cycles (each touched chapter re-fires affected stages after the cross-chapter touch).

6. **Process-scaffolding vocabulary leakage risk.** Process terms (`Option A`, `ratified`, `Phase C-ζ`, `F-V1`, `INCLUDE`/`EXCLUDE`, glyph verdicts) need continuous-scan invariant gates, not just per-stage manual review.

7. **Math + prose treated as parallel pipelines risks drift.** Single unified pipeline with content-type-aware sub-protocols at each stage is cleaner than parallel pipelines for math vs prose.

8. **No formal pre-publication-review handoff.** External review (math sign-off; framework methodology evaluation; domain experts) requires explicit flagging in the manuscript-submission package; currently ad-hoc.

---

## §3. Proposed pipeline architecture

**Single unified pipeline. Content-type-aware sub-protocols at each stage. Invariant gates enforced continuously. Change-cascade routing routes any change back to the appropriate prior stage.**

### §3.1 Stage structure

| Stage | Purpose | Content-type sub-protocols |
|---|---|---|
| **0** | Author conception / topic decision | (per current) |
| **1** | Ready-to-draft gate (three sub-steps below) | Prose + math + tables + figures |
| **1a** | Corpus-hygiene invariant gate (scaffolding scan + regressed-pattern scan) | All content types |
| **1b** | Canonical fact-ground + audience-aware structure + render-safe convention | Prose: canonical-facts inventory + audience pressure-test character set; Math: canonical-formula inventory + numerical-constants inventory + **baseline render test**; Tables: canonical-data inventory + baseline render test; Figures: source verification |
| **1c** | Cross-artifact coherence check | Verify against bibliography + AuthorsNote + sibling-chapter prose + cross-chapter consistency inventory + existing rigor-pass artifacts |
| **2** | Audience-blind drafting | Draft prose + math + tables + figures |
| **3** | Multi-pass rigor audit | (sub-passes below) |
| **3.1** | Fact-check pass | Prose: §6 + public-record verification; Math: formula + constants + derivation-chain verification; Tables: cell-by-cell data verification; Figures: source verification |
| **3.2** | Voice-polish pass | Prose: LLM-tic + register-consistency + rhythm; Math: notation + symbol-usage + inline-vs-display consistency; Tables: caption + header consistency; Figures: caption consistency |
| **3.3** | Audience-load acceptance pass | Pressure-test against acceptance character set (typically 15-25 characters across Tier 1 gating + Tier 2 pipeline-strengthening + Tier 3 cultural-resonance/accessibility/practitioner) |
| **3.4** | Audience-load robustness pass | Pressure-test against adversarial / detractor character set (typically 5-10 characters; thread-pull synthesis is the diagnostic, not pass/fail per character) |
| **4** | Render + character-integrity audit | All content types; automated source-vs-rendered character diff; formula-integrity audit; layout-integrity audit |
| **5** | Academic-rigor + prose-quality sign-off on rendered output | Bookend the Stage 1 sign-off; verify no drift through the pipeline; **Pre-publication review queue artifact** generated as mandatory hand-off deliverable |

### §3.2 Invariant-gate infrastructure

Two scans run continuously (pre-commit hook + every stage transition + CI):

- **Scaffolding scan:** placeholders (`TODO`, `TK`, `FIXME`); drafting-template scaffolding (*"Let me explain"*, *"In this section…"*); meta-commentary tics
- **Regressed-pattern scan:** patterns previously fixed by rigor passes (corpus-wide institutional memory); deprecated terminology; gate-decision-banned patterns (vendor names held OUT per CEO-era NDA gate); cross-chapter consistency-inventory items

Both registries in YAML format. Severity-tiered (HIGH = block; MEDIUM = flag) with per-file allowlist support for known-legitimate substantive uses of pattern-class terms (e.g., Ch 9 line 165's `pressure-test` as legitimate substantive verb).

### §3.3 Change-cascade routing protocol

Explicit routing rules:

| Change type | Routes back to | Then re-fires |
|---|---|---|
| New fact discovered (interview; family conversation; external verification) | Stage 1b canonical-facts inventory | Pass 3.1 fact-check for affected scope + Pass 3.2 voice-polish for affected prose + Pass 3.3/3.4 if claim-level material changed |
| New audience character identified | Stage 1b audience pressure-test set | Pass 3.3 / 3.4 audience-load re-fire |
| Bibliography commitment lands | Stage 1c cross-artifact coherence | Affected chapter's Pass 3.3 audience-load re-fire |
| Spot-fix applied (any phase) | Stage 1c cross-artifact coherence (light) | Pass 3.3 audience-load re-fire (light) — verify verdicts didn't shift |
| Cross-chapter workstream applies content | Stage 1c cross-artifact coherence for all affected chapters | Each affected chapter's Pass 3.3 audience-load re-fire (light) |
| Any source-file change | Stage 1a invariant-gate scans | (automatic; gates commit) |

### §3.4 Single-pipeline + content-type sub-protocols (not parallel pipelines)

Math + prose + tables + figures all go through the same pipeline. Each stage's work varies by content type via sub-protocols that fire based on the artifact's content-type inventory (a pre-processing step generates `lines X-Y: prose; lines Z-W: math; lines V-U: table` etc.). New content types added as new sub-protocols within existing stages.

### §3.5 Cross-chapter workstream lifecycle

Cross-chapter workstreams (those touching multiple chapters; e.g., today's rent-seeking-engagement workstream) get a first-class lifecycle:

1. Surfaces (typically from a Pass 3.4 robustness thread-pull, a Pass 1 cross-chapter-fact-drift, or an external trigger)
2. PM session ratifies + spins up
3. Workstream session applies cross-chapter touches in single feature branch
4. **Each touched chapter automatically triggers Stage 1c + Pass 3.3 light re-fire** (cascade routing)
5. Cross-chapter workstream closes only after all affected chapters' light re-fires complete clean
6. Cross-thread-todos entry resolved + workstream-handoff archived

### §3.6 Pre-publication review queue (Stage 5 mandatory deliverable)

A `Pre-publication review queue` artifact gets generated at Stage 5 sign-off for each artifact. Contents:

- What has been internally verified (by whom; against what sources)
- What has NOT been externally verified
- Recommended external reviewer types for publisher to engage (math: technical reviewer with quantitative-economics / applied-mathematics background; framework methodology: economist in an adjacent tradition; domain experts where applicable)
- Highest-priority sections for external review if publisher budget is limited

Goes to publisher / agent / editor with the manuscript submission package — transparent quality-control disclosure rather than overclaiming-verification posture.

---

## §4. Artifacts the dedicated session must produce

| Artifact | Type | Notes |
|---|---|---|
| **Pipeline doctrine doc** | New canonical reference | Likely lives at `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` or similar; captures the full §3 architecture |
| **Revisions to `stage-3-three-pass-rigor-audit.md`** | Amendment or supersession | Pass 3 split into Pass 3.3 + Pass 3.4; v2.0 Amendment B → v3.0 framing |
| **Updates to `audience-pressure-test-construction.md`** | Amendment | Acceptance vs robustness character-set distinction; adversarial-detractor character types; severity scales |
| **New: Stage 1 doctrine doc** | New | Three-step structure (1a invariant gate + 1b substantive + 1c cross-artifact coherence) |
| **New: Stage 4 doctrine doc** | New | Render + character-integrity audit; formula-integrity audit protocol; pre-render conventions |
| **New: Stage 5 doctrine doc + Pre-publication review queue template** | New | Bookend sign-off; mandatory hand-off artifact format |
| **Memory update: `feedback_audience_aware_drafting_discipline.md`** | Update v2.0 → v3.0 | Codifies the full pipeline revision as a canonical project-level memory |
| **`tools/quality-gates/regressed-patterns.yaml`** | New | Initial population from existing rigor-pass artifacts (see §6 retrofit plan); ~80-120 entries expected from Ch 1 + Ch 5 + Ch 6 + TA closed cycles + drafting-template named-tic inventory |
| **`tools/quality-gates/scaffolding-patterns.yaml`** | New | Drafting placeholders (`TODO`, `TK`, etc.) + process-scaffolding vocabulary (`Option A-Z`, `ratified`, `Phase C-*`, `F-V*`, `INCLUDE`/`EXCLUDE` glyphs, etc. — comprehensive list per 2026-05-17 leak-check survey) |
| **`tools/scripts/check-corpus-invariants.sh`** | New script | Bash; reads the two YAML registries; greps against `manuscript/chapters/*Draft*.md` + `manuscript/chapters/_AUTHORSNOTE*.md` + Tech Appendix sources + (configurable) essay sources; exits non-zero on HIGH-severity match; flags MEDIUM-severity for review |
| **Pre-commit hook setup** | New | Installs the invariant-check script as pre-commit; documents installation |
| **CI integration** | New | (Optional / per author preference) hooks the script into CI pipeline |
| **Workstream-handoffs/README.md update** | Amendment | Add the new pipeline structure reference; deprecate/archive any superseded handoffs |
| **`tools/workstream-handoffs/README.md` retrofit section** | Amendment | Add retrofit workstreams for Ch 1 + Ch 2 + Ch 5 + Ch 6 + Ch 7 + Ch 8 + Ch 9 + Ch 10 + Tech Appendix (per §6 retrofit plan) |

---

## §5. Ratification status (decisions for author)

| # | Decision | Provisional answer | Status |
|---|---|---|---|
| 1 | Pipeline structure | Stage 0 → 1 (three-step) → 2 → 3 (four-pass) → 4 → 5 (bookend) | **Pending ratification** |
| 2 | Single-pipeline architecture | Content-type-aware sub-protocols; no parallel pipelines | **Pending ratification** |
| 3 | Invariant-gate placement | Pre-commit hook + every stage transition + continuous CI | **Pending ratification** |
| 4 | Change-cascade routing protocol | Per §3.3 table | **Pending ratification** |
| 5 | Pre-publication review queue | Mandatory hand-off artifact in manuscript-submission package | **Pending ratification** |
| 6 | Bookend Stage-1 + Stage-5 sign-offs | Both academic-rigor + prose-quality at beginning + end | **Pending ratification** |
| 7 | Regressed-pattern + scaffolding registry format | YAML; severity-tiered with allowlist support | **RATIFIED 2026-05-17** (YAML format ratified by author) |
| 8 | Versioning | v3.0 of audience-aware-drafting-discipline (extends v2.0 Amendment B) | **Pending ratification** |
| 9 | Retrofit policy for already-cycled chapters | **All chapters run through the new pipeline once it is finished.** | **RATIFIED 2026-05-17** — author directed *"Let's go ahead and run all chapters through this same pipeline once it is finished."* See §6 retrofit plan. |
| 10 | External-reviewer policy | Self-sign + explicit flag at hand-off; college tutors as bounded bonus capacity | **RATIFIED earlier in 2026-05-17 brainstorm** (per author's framing about no funds for second reviewer + college tutor exploration + flag-at-handoff as risk-mitigation) |
| 11 | Cross-chapter workstream lifecycle | Formalize as first-class with per-chapter feedback re-fires (per §3.5) | **Pending ratification** |

**Three ratified (7 + 9 + 10); eight pending.** Dedicated session should NOT fire until the remaining eight are ratified or revised by author.

---

## §6. Retrofit plan for all chapters (per ratified decision #9)

Per author direction 2026-05-17: all chapters run through the new pipeline once it is finished. This is a substantial commitment; capturing scope here.

### §6.1 What "retrofit" means

Retrofit does NOT mean re-doing every rigor pass from scratch (those are author-ratified + applied). It means applying the **new-to-the-pipeline elements** to existing chapters:

- **Stage 1a invariant-gate scan** against current source (likely produces no leaks per the 2026-05-17 leak-check survey, but verify per-chapter and record clean baseline)
- **Stage 1c cross-artifact coherence check** against each chapter (likely surfaces small gaps similar to today's bibliography §21 / Ch-1 / Dunbar-Du-Bois mid-Pass-3 discovery — pre-existing commitments not realized in chapter prose)
- **Pass 3.4 audience-load robustness test** against each chapter (chapters that have closed cycles had only the original acceptance-test version of Pass 3; the adversarial-detractor robustness expansion is new)
- **Stage 4 render + character-integrity audit** against each chapter's derivative outputs
- **Stage 5 academic-rigor + prose-quality sign-off + Pre-publication review queue artifact generation** for each chapter

### §6.2 Per-chapter retrofit scope

| Artifact | Current state | Retrofit scope |
|---|---|---|
| Ch 1 | Three-pass cycle CLOSED (2026-05-17); REAUDIT v3 ratified-as-applied | 1a + 1c + 3.4 (already done; doc exists) + 4 + 5 |
| Ch 2 | Pass 1 RATIFIED + APPLIED 2026-05-12 | 1a + 1c + 3.2 + 3.3 + 3.4 + 4 + 5 |
| Ch 3 | Drafted 2026-05-09; Phase A not yet entered | Full new pipeline application |
| Ch 4 | Pass 1 PROPOSED 2026-05-12; Pass 2 PROPOSED 2026-05-15 | 1a + 1c + Pass 3 (3.1 verify + 3.2 verify + 3.3 + 3.4) + 4 + 5 |
| Ch 5 | Three-pass cycle CLOSED 2026-05-14 | 1a + 1c + 3.4 + 4 + 5 |
| Ch 6 | Three-pass cycle CLOSED 2026-05-15 | 1a + 1c + 3.4 + 4 + 5 |
| Ch 7 | Pass 1 PROPOSED 2026-05-15 (commit `ff9a89a`) | 1a + 1c + Pass 3 (3.1 verify + 3.2 + 3.3 + 3.4) + 4 + 5 |
| Ch 8 | Pass 1 PROPOSED 2026-05-16 (commit `210b02c`) | 1a + 1c + Pass 3 (3.1 verify + 3.2 + 3.3 + 3.4) + 4 + 5 |
| Ch 9 | Pass 1 PROPOSED 2026-05-15 (commit `9720da0`) | 1a + 1c + Pass 3 (3.1 verify + 3.2 + 3.3 + 3.4) + 4 + 5 |
| Ch 10 | Pass 1 PROPOSED 2026-05-16 (commit `c85c41d`) | 1a + 1c + Pass 3 (3.1 verify + 3.2 + 3.3 + 3.4) + 4 + 5 |
| Tech Appendix | Multiple verification rounds completed; full rigor-pass status per PM dashboard | 1a + 1c + 3.4 + 4 (highest stakes for math-content-density) + 5 (academic-rigor sign-off is most consequential here) |
| AuthorsNote | Paratextual; not previously through Phase A rigor cycle | Full new pipeline application (likely abbreviated given paratextual register) |

### §6.3 Retrofit sequencing

- **First:** complete the pipeline doctrine cluster (§4 deliverables). Until the doctrine exists, retrofit cannot begin.
- **Second:** populate the YAML registries from existing rigor-pass artifacts. This is the institutional-memory build.
- **Third:** spin up retrofit workstreams **per chapter** (parallelizable). Each retrofit workstream applies the new-to-pipeline elements (per §6.2 table) for one chapter. Author ratifies any spot-fixes per workstream.
- **Fourth:** Phase B (whole-book audit) post-retrofit absorbs Phase B work that was previously deferred.

Estimated total scope: ~10-12 retrofit sessions (one per chapter + TA + AuthorsNote), each lighter than a full Phase A cycle since core rigor work is already done. Phase B follows.

---

## §7. Sequencing + dependencies (this workstream)

**Before this workstream fires:**

- Author ratifies the 8 remaining open decisions (§5) — or revises provisional answers
- PM session updates `pm-session-handoff_2026-05-13.md` to include this workstream in the active queue
- Any in-flight per-chapter Phase A workstreams complete or pause (so the doctrine revision lands on a stable manuscript state)

**This workstream produces:**

- Pipeline doctrine cluster (§4) — single feature branch
- Initial registry populations from existing rigor-pass artifacts
- Author ratifies the doctrine cluster + the registries
- Doctrine cluster merges to main

**After this workstream completes:**

- Retrofit workstreams (§6) spin up per chapter
- Future per-chapter Phase A work uses the new pipeline doctrine

**Dependencies on other in-flight workstreams:**

- Cross-chapter rent-seeking-engagement workstream (handoff at [`tools/workstream-handoffs/archive/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)) — independent; can run in parallel
- Per-chapter Phase A workstreams in flight — should reach a clean stopping point before doctrine cluster lands
- Tech Appendix in-flight work — independent; can run in parallel

---

## §8. Open questions remaining (for PM session / author)

1. **Versioning + memory-entry naming** (decision #8). Is this v3.0 of `feedback_audience_aware_drafting_discipline.md` or a new doctrine artifact entirely (e.g., `commons_bonds_pipeline_doctrine_v1.0.0.md`)? Recommendation: hybrid — memory entry updates to v3.0 with summary + pointer; full doctrine lives in a new canonical artifact.

2. **CI integration scope.** Should the invariant-check script run on every push? Every PR? Only on merge-to-main? Author preference + tooling-cost decision.

3. **Pre-commit hook adoption.** Optional vs mandatory? Affects how the script is documented + installed.

4. **External-reviewer engagement timeline for Tech Appendix.** Decision #10 ratifies the flag-at-handoff approach but not the timing of any college-tutor engagement. Worth surfacing in PM session before retrofit hits Tech Appendix.

5. **Allowlist mechanism for the regressed-pattern + scaffolding scans.** Per-file allowlist? Per-pattern context-aware exclusion? YAML structure for allowlists. Implementation detail; resolve during dedicated session.

6. **Stage 5 sign-off mechanic for retrofit.** When existing chapters get retrofit Stage 5 sign-off, is the author's sign-off sufficient or should there be a parallel external-reviewer flag pass for high-math-content artifacts (Ch 6 + Ch 9 + Tech Appendix)?

---

## §9. Cross-thread items

- **PM session task:** add cross-thread-todos entry (#14 or next-available number) flagging this workstream for spinup; tracking entry should reference §5 ratification status + §6 retrofit plan.
- **Workstream-handoffs README registry update:** add this workstream to the appropriate "Added" section.
- **Memory entry cross-reference:** when the doctrine cluster lands, update `MEMORY.md` index to surface the new doctrine + the YAML registries.
- **Cross-thread coherence:** the rent-seeking-engagement workstream (cross-thread-todos #13) is in-flight independent of this workstream; no conflict.

---

## §10. PM session spinup metadata

**Workstream name:** Pipeline-revision (drafting + fact-check + voice-polish + audience-load + rendering + sign-off pipeline doctrine — comprehensive revision)
**Trigger to spin up:** author ratification of 8 remaining open decisions (§5) + PM session ratification of workstream.
**Estimated session length:** substantial single session (the doctrine cluster is the deliverable; ~12-15 artifacts to produce). Could be split into two sessions if scope is too heavy for one: session A (doctrine docs + memory update) + session B (registries + script + pre-commit + CI).
**Branch:** `claude/pipeline-revision-<harness-id>` from current `origin/main`.
**Merge-to-main default:** per CLAUDE.md, doctrine-revision sessions producing internal scaffolding (`tools/`-side work; no chapter content changes) autonomously fast-forward merge to main at session close. The registries themselves are internal scaffolding; their **application** to chapters (the retrofit workstreams) is what produces content changes and gets author-ratification cycles.
**Cross-thread items:** this handoff's cross-thread-todos entry + workstream-handoffs README update + (post-completion) MEMORY.md index update.

**Post-completion success criteria:**
- Pipeline doctrine cluster on `main`
- Registries populated from existing rigor-pass artifacts
- Invariant-check script working + documented
- Author ratifies the cluster
- Retrofit workstreams ready to spin up per chapter

---

*End of pipeline-revision workstream handoff — PROPOSED 2026-05-17. Awaiting author ratification of 8 remaining open decisions (§5) + PM session spinup.*
