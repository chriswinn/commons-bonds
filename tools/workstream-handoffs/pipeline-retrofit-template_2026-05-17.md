# Pipeline-Doctrine Retrofit Template

**Date drafted:** 2026-05-17
**Status:** Canonical template referenced by all per-chapter retrofit handoffs.
**Parent doctrine:** [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md) (PROPOSED 2026-05-17; all 11 decisions ratified at session start).
**Triggered by:** ratified decision #9 (2026-05-17 brainstorm): all chapters run through the new pipeline once the doctrine cluster lands on `main`.

---

## §0. Purpose

Apply the **new-to-the-pipeline elements** to existing chapters that have already been through some or all of their Phase A cycles. Retrofit does NOT re-do every rigor pass from scratch — those are author-ratified + applied. Retrofit applies the elements introduced by v3.0:

- **Stage 1a invariant-gate scan** (corpus-hygiene check via `tools/scripts/check-corpus-invariants.sh`).
- **Stage 1c cross-artifact coherence check** (bibliography + AuthorsNote + sibling-chapter + rigor-pass coherence verification).
- **Pass 3.4 audience-load robustness test** against the adversarial / detractor character set (typically 5–10 characters; thread-pull synthesis is the diagnostic).
- **Stage 4 render + character-integrity audit** against derivative outputs (`.docx` + `.html` + `.pdf`).
- **Stage 5 academic-rigor + prose-quality sign-off + pre-publication review queue artifact generation.**

Per-chapter retrofit scope is specified in the per-chapter retrofit handoff stub that points to this template.

---

## §1. Branch discipline

Open fresh feature branch per the per-chapter handoff's recommended prefix:

```
git fetch origin
git checkout -b claude/<chapter-slug>-pipeline-retrofit-<harness-id> origin/main
```

Per CLAUDE.md merge-to-main default: retrofit sessions producing rigor-pass artifacts (internal scaffolding proposing spot-fixes without applying) autonomously fast-forward merge to main at session close. Sessions that **apply** spot-fixes to chapter source still require author ratification + are separate Phase C application sessions.

---

## §2. Read order

1. THIS template + the per-chapter retrofit handoff stub (which scopes the work).
2. [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md) — full architecture.
3. [`tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) — Stage 1 three-step structure.
4. [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) — Stage 4 render-integrity.
5. [`tools/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) — Stage 5 sign-off + pre-pub review queue template.
6. [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) (v3.0) — Pass 3.4 robustness section.
7. [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) (v3.0) §3 — adversarial / detractor character types + thread-pull synthesis canonical format.
8. **Per-chapter prior-cycle rigor-pass artifacts** in `tools/rigor-passes/` (the per-chapter handoff stub lists the specific files).
9. The chapter file under audit (in `manuscript/chapters/`).

---

## §3. Procedure (per retrofit scope)

The per-chapter handoff stub specifies which sub-steps fire. For each in-scope sub-step:

### §3.1 Stage 1a invariant-gate scan (always fires)

```bash
tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/<chapter-file> --verbose
```

Resolve any HIGH-severity findings (block proceeding). Review MEDIUM findings; either address or add to YAML registry allowlist with rationale. Record clean-baseline verification artifact at `tools/quality-gates/clean-baselines/<chapter-slug>_stage1a_<date>.md`.

### §3.2 Stage 1c cross-artifact coherence check (always fires)

Per Stage 1 doctrine §3.2:

1. Inventory bibliography entries touching chapter scope.
2. Inventory AuthorsNote framings touching chapter scope.
3. Inventory sibling-chapter cross-references.
4. Inventory prior rigor-pass artifacts for this chapter.
5. Inventory cross-chapter consistency-inventory items.

For each item: verify the chapter realizes the commitment / honors the framing / honors the prior finding's disposition. Record coherence verification artifact at `tools/quality-gates/coherence-checks/<chapter-slug>_stage1c_<date>.md`.

### §3.3 Pass 3.1 verify (if in retrofit scope)

For chapters that had Pass 1 PROPOSED but not yet RATIFIED + APPLIED: re-verify the Pass 1 findings against current chapter state. Output a brief "Pass 3.1 verify" artifact at `tools/rigor-passes/<chapter-slug>_stage3_pass_3_1_verify_<date>.md`. Confirms findings still valid or notes which have been superseded by other edits.

### §3.4 Pass 3.2 verify or fresh (if in retrofit scope)

Per Stage 3 template (v3.0). If Pass 2 PROPOSED but not yet RATIFIED + APPLIED: verify. Otherwise fresh Pass 3.2 voice-polish against current chapter state.

### §3.5 Pass 3.3 acceptance (if in retrofit scope)

Per Stage 3 template (v3.0) + audience-pressure-test-construction (v3.0). Build acceptance-test character set per the per-chapter venue + scope. Score per character; produce include-vs-exclude verdict.

### §3.6 Pass 3.4 robustness (always fires for retrofit)

Per Stage 3 template (v3.0) §"Pass 3.4: Audience-load (robustness)" + audience-pressure-test-construction (v3.0) §3 (adversarial / detractor character types) + §3.4 (thread-pull synthesis canonical diagnostic format model).

Build adversarial / detractor character set (typically 5–10 characters per §3.3 defaults table) drawn from:
- Industry-funded / financial-incentive adversaries
- Ideologically-opposed adversaries
- Trade-press / commercial-adversarial characters
- Cultural-adversarial characters
- Legal-adversarial characters

Score per character on the adversarial verdict scale (⚠ EXCLUDE → ⚠⚠⚠ EXCLUDE — verdict-floor is EXCLUDE; diagnostic value is in which threads adversaries find).

Produce thread-pull synthesis table (the canonical Pass 3.4 diagnostic format per Ch 1 REAUDIT v3 §5.3 model). Classify each thread as:
- (a) Load-bearing chapter claim — chapter must hold its ground; cross-chapter handoff if thread warrants further engagement elsewhere.
- (b) Procedural / cosmetic flag — spot-fix could disarm.

Final robustness verdict: ROBUST / CONDITIONALLY ROBUST / REQUIRES STRUCTURAL ENGAGEMENT. The third routes to a cross-chapter workstream per pipeline doctrine §5.

Output artifact: `tools/rigor-passes/<chapter-slug>_stage3_pass_3_4_robustness_<date>.md`.

### §3.7 Stage 4 render + character-integrity audit (always fires)

> **⚠ BLOCKER — canonical-pipeline decision pending.** Stage 4 audits should not fire until the render-pipeline-standardization workstream completes ([`render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md)). Author 2026-05-17 observed mobile-device renders are better than the laptop `build-derivatives.sh` pipeline; canonical-pipeline decision is pending comparison-render + author ratification. Stage 4 audit baselines must use the ratified canonical pipeline. PM session sequences retrofit Stage 4 sub-steps AFTER the standardization workstream lands on main.

Per Stage 4 doctrine. Run the **canonical pipeline** (per render-pipeline-standardization workstream's ratified decision — laptop `build-derivatives.sh` / `build-derivatives-alt.sh`, mobile-pipeline-specific workflow, or both per Option C). Audit derivative outputs against source per §2.2 (character diff) + §2.3 (formula integrity, if math content) + §2.4 (tables) + §2.5 (figures) + §2.6 (layout integrity).

Capture xelatex stderr to build log + grep for `Missing character` warnings (load-bearing per Stage 4 §3.3 discipline). Output artifact: `tools/rigor-passes/<chapter-slug>_stage_4_render_audit_<date>.md`.

### §3.8 Stage 5 sign-off + pre-pub review queue (always fires)

Per Stage 5 doctrine. Verify academic-rigor + prose-quality sign-offs (no drift through pipeline; cross-artifact coherence maintained; all Pass-3 findings resolved or held with rationale; Stage 4 verdict CLEAN or MEDIUM HOLD).

Generate **mandatory** pre-publication review queue artifact at `tools/pre-submission-reviews/<chapter-slug>_pre_pub_review_queue_v1.0.0.md` per Stage 5 §3 template. Contents:
- What has been internally verified
- What has NOT been externally verified
- Recommended external reviewer types (math reviewer / framework-methodology reviewer / domain experts)
- Highest-priority sections for external review

Output sign-off artifact at `tools/quality-gates/sign-offs/<chapter-slug>_stage5_signoff_<date>.md`.

---

## §4. Output deliverables

Per retrofit scope (per-chapter handoff stub):

| Stage | Output artifact path |
|---|---|
| 1a | `tools/quality-gates/clean-baselines/<chapter-slug>_stage1a_<date>.md` |
| 1c | `tools/quality-gates/coherence-checks/<chapter-slug>_stage1c_<date>.md` |
| 3.1 verify | `tools/rigor-passes/<chapter-slug>_stage3_pass_3_1_verify_<date>.md` (if in scope) |
| 3.2 verify/fresh | `tools/rigor-passes/<chapter-slug>_stage3_pass_3_2_voice_polish_<date>.md` (if in scope) |
| 3.3 | `tools/rigor-passes/<chapter-slug>_stage3_pass_3_3_audience_load_acceptance_<date>.md` (if in scope) |
| 3.4 | `tools/rigor-passes/<chapter-slug>_stage3_pass_3_4_audience_load_robustness_<date>.md` |
| 4 | `tools/rigor-passes/<chapter-slug>_stage_4_render_audit_<date>.md` |
| 5 | `tools/quality-gates/sign-offs/<chapter-slug>_stage5_signoff_<date>.md` + `tools/pre-submission-reviews/<chapter-slug>_pre_pub_review_queue_v1.0.0.md` |

All artifacts PROPOSED at retrofit-session close; author ratifies before any spot-fixes apply (Phase C application is a separate session).

---

## §5. Hard constraints

- Do NOT apply spot-fixes to chapter source during the retrofit session. Author ratifies first.
- Do NOT re-do prior-cycle work (Pass 1 / Pass 2 already RATIFIED + APPLIED). Reference for context only.
- If Pass 3.4 surfaces REQUIRES STRUCTURAL ENGAGEMENT (load-bearing adversarial thread that the chapter does not disarm), STOP + spin up a cross-chapter workstream per pipeline doctrine §5. Do not try to spot-fix structural issues at retrofit time.
- Stage 5 sign-off is **mandatory** and pre-publication review queue artifact is **mandatory**. No exception for "we'll add this later."
- Per Stage 1a invariant-scan output: any HIGH-severity match blocks proceeding to Stage 1c. Resolve before continuing.
- Living named subjects (if any new ones surface during Stage 1c bibliography sweep) require explicit author confirmation before naming in publisher-facing prose.

---

## §6. Sequencing across retrofit workstreams

Per pipeline-revision handoff §6.3:

- **First** (done 2026-05-17): doctrine cluster + initial registry population landed on main.
- **Second** (in-flight per retrofit workstreams): per-chapter retrofit (this template applies).
- **Third** (post-retrofit): Phase B whole-book audit absorbs Phase B work previously deferred.

Retrofit workstreams are **parallelizable across chapters**. PM session sequences spin-up. Cross-chapter cascades (per pipeline doctrine §5 lifecycle) fire when a retrofit Pass 3.4 surfaces a load-bearing structural thread crossing chapters.

---

## §7. Cross-thread items

After retrofit session merges to main:
- Add retrofit verdict summary to `publishing/strategy/cross-thread-todos.md` (or wherever the cross-thread tracking lives at that time).
- If Pass 3.4 surfaces a cross-chapter handoff: PM session drafts the cross-chapter workstream handoff per pipeline doctrine §5.
- If Stage 4 surfaces a render-failure pattern not in the registry: add to `tools/quality-gates/regressed-patterns.yaml` (render-failure category).
- If Stage 5 pre-publication review queue surfaces a recommended-external-reviewer that's worth adding to the publisher / agent pitch tracker: PM session captures.

---

*End of pipeline-doctrine retrofit template. Per-chapter handoff stubs reference this template + scope the per-chapter work.*
