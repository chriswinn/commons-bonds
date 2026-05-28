# Pipeline-Doctrine Retrofit Template

**Date drafted:** 2026-05-17
**Status:** Canonical template referenced by all per-chapter retrofit handoffs.
**Parent doctrine:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) (PROPOSED 2026-05-17; all 11 decisions ratified at session start).
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
2. [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) — full architecture.
3. [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) — Stage 1 three-step structure.
4. [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) — Stage 4 render-integrity.
5. [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) — Stage 5 sign-off + pre-pub review queue template.
6. [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) (v3.0) — Pass 3.4 robustness section.
7. [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) (v3.0) §3 — adversarial / detractor character types + thread-pull synthesis canonical format.
8. **Per-chapter prior-cycle rigor-pass artifacts** in `tools/rigor-passes/` (the per-chapter handoff stub lists the specific files).
9. The chapter file under audit (in `manuscript/chapters/`).

---

## §3. Procedure (per retrofit scope)

The per-chapter handoff stub specifies which sub-steps fire. For each in-scope sub-step:

> **Selective stage-firing per v1.0.0 Amendment A (2026-05-18).** Retrofit sub-steps are now classified as **automatic-on-edit cascade** (fire on every retrofit session) vs **explicit-gate cascade** (fire only on explicit author trigger, typically pre-external-review or pre-publication). Markers below: ⚡ = automatic-on-edit; 🚪 = explicit-gate. For first-cycle retrofits + standardization-comparison-bed retrofits, ALL sub-steps fire regardless of class (the retrofit itself is an explicit-gate trigger for the heavy passes). For subsequent maintenance retrofits + spot-fix follow-ups, only ⚡ sub-steps fire automatically; 🚪 sub-steps fire only when the author explicitly triggers them per §3 of the canonical doctrine.

### §3.1 ⚡ Stage 1a invariant-gate scan (always fires)

```bash
tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/<chapter-file> --verbose
```

Resolve any HIGH-severity findings (block proceeding). Review MEDIUM findings; either address or add to YAML registry allowlist with rationale. Record clean-baseline verification artifact at `tools/quality-gates/clean-baselines/<chapter-slug>_stage1a_<date>.md`.

### §3.2 ⚡ Stage 1c cross-artifact coherence check (always fires)

Per Stage 1 doctrine §3.2:

1. Inventory bibliography entries touching chapter scope.
2. Inventory AuthorsNote framings touching chapter scope.
3. Inventory sibling-chapter cross-references.
4. Inventory prior rigor-pass artifacts for this chapter.
5. Inventory cross-chapter consistency-inventory items.

For each item: verify the chapter realizes the commitment / honors the framing / honors the prior finding's disposition. Record coherence verification artifact at `tools/quality-gates/coherence-checks/<chapter-slug>_stage1c_<date>.md`.

### §3.3 ⚡ Pass 3.1 verify (if in retrofit scope)

For chapters that had Pass 1 PROPOSED but not yet RATIFIED + APPLIED: re-verify the Pass 1 findings against current chapter state. Output a brief "Pass 3.1 verify" artifact at `tools/rigor-passes/<chapter-slug>_stage3_pass_3_1_verify_<date>.md`. Confirms findings still valid or notes which have been superseded by other edits.

### §3.4 ⚡ Pass 3.2 verify or fresh (if in retrofit scope)

Per Stage 3 template (v3.0). If Pass 2 PROPOSED but not yet RATIFIED + APPLIED: verify. Otherwise fresh Pass 3.2 voice-polish against current chapter state.

### §3.5 🚪 Pass 3.3 acceptance (explicit-gate; fires at first-cycle retrofit + venue-change + pre-publication)

Per Stage 3 template (v3.0) + audience-pressure-test-construction (v3.0). Build acceptance-test character set per the per-chapter venue + scope. Score per character; produce include-vs-exclude verdict.

### §3.6 🚪 Pass 3.4 robustness (explicit-gate; fires at first-cycle retrofit + adversarial-set change + cross-chapter-cascade batch + pre-publication)

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

### §3.6b 🚪 Pass 3.5 developmental-edit (explicit-gate; fires per-chapter after Pass 3.1-3.4 ratify-and-apply complete; pre-publication; on author "developmental read-through" trigger) — added by pipeline-doctrine v1.0.0 Amendment B 2026-05-18

Per pipeline doctrine §3.6 (Amendment B). Whole-chapter scale; restoration-of-richness lens; catches what per-paragraph + per-character passes miss (emotional-arc continuity + scene-anchor density + sensory-detail restoration + voice-flow continuity + cumulative-LLM-cadence residue + reader-engagement at analytical pivots).

For retrofit context: Pass 3.5 fires per-chapter, EXPLICITLY GATED (not auto-fire on retrofit). Author triggers via the developmental-edit workstream (`tools/workstream-handoffs/developmental-edit-workstream-handoff_2026-05-18.md`); per-chapter sessions sequence Ch 1 → Ch 2 → ... → Ch 10 → AuthorsNote (Dedication skipped).

Light Pass 3.3 (acceptance) re-fire recommended after Phase C application of any ratified Pass 3.5 spot-fixes. Pass 3.4 re-fire NOT routinely warranted.

**Per Amendment C (ratified 2026-05-19):** Pass 3.5 follows the interactive ratification protocol per pipeline doctrine §3.7. Per-finding format MUST include Options + Recommendation + Reasoning. Two-session workflow: (1) discovery session produces PROPOSED artifact + auto-merges to main; (2) interactive ratification + application session walks through findings + applies ratified spot-fixes to chapter source in the same combined session.

Output artifact (discovery session): `tools/rigor-passes/<chapter-slug>_developmental_edit_review_<date>.md`.

Output artifacts (interactive ratification + application session): §"Disposition log" appended to the same artifact + chapter source changes committed to main.

### §3.7 🚪 Stage 4 render + character-integrity audit (explicit-gate; fires at pre-external-review send + pre-publication + on author "build it now" trigger + any publishing-pipeline-script change)

> **⚠ CANONICAL-PIPELINE — sequencing differs for the first 4 retrofits vs the remaining 9.** Author direction 2026-05-17: the render-pipeline-standardization workstream ([`render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md)) fires **in parallel with** the first 4 retrofits (Ch 1 + Ch 5 + Ch 6 + TA), using them as the comparison-render test bed. Sequencing:
>
> **First 4 retrofits (Ch 1, Ch 5, Ch 6, TA):**
> - Render Stage 4 via THREE pipelines:
>   - remote-container pipeline (baseline; pre-rendered 2026-05-17 at BASE `9ffad4e`)
>   - laptop `build-derivatives.sh` (canonical-in-repo script with default `MAIN_FONT="Garamond"`)
>   - laptop `build-derivatives-alt.sh` (Claude-tuned alt with `MAIN_FONT="EB Garamond"` + fallback-header.tex)
> - **The laptop-side renders ARE the active laptop-pipeline-tuning effort.** Per author direction 2026-05-17 late-session, the retrofit Stage-4 work is explicitly the moment to resume the laptop-pipeline-improvement effort (Chrome render was in progress; hours invested at the time of the Sandy packet send). Each round, tune what's tunable on the laptop side (fonts, fallback-header entries, pandoc invocation, Chrome configuration, CSS for HTML→PDF) to bring the laptop pipeline closer to the remote-container baseline.
> - **Run BOTH laptop scripts each round.** Author direction 2026-05-17: canonical script between `build-derivatives.sh` and `build-derivatives-alt.sh` not yet ratified; both surface in the comparison so the laptop-tuning rounds can identify which (or which tuned variant of which) is the right canonical.
> - Capture per-chapter comparison artifact at `tools/rigor-passes/render_pipeline_comparison_<chapter-slug>_<date>.md`. Each artifact should record differences across ALL THREE pipelines + the laptop-tuning actions attempted that round + their effect. Cumulative diagnosis answers: (a) does either laptop script match remote-container baseline closely, (b) which laptop script is the right canonical going forward.
> - Do NOT ratify Stage 4 verdict yet — mark as **PROPOSED-pending-canonical-decision**. Canonical decision (Option A tuned-laptop / B remote-container-canonical / C dual-discipline) AND canonical-laptop-script decision (`build-derivatives.sh` vs `build-derivatives-alt.sh` vs merged) both come after tuning rounds plateau.
> - Stage 5 sign-off deferred until Stage 4 verdict ratifies.
> - Do NOT tune the pipeline mid-comparison (discipline-trap; tuning Ch 1 → Ch 5 contaminates the moving-baseline question; render → diagnose → defer-decision → next chapter).
>
> **Remaining 9 retrofits (Ch 2, Ch 3, Ch 4, Ch 7, Ch 8, Ch 9, Ch 10, AuthorsNote, Dedication-conditional):**
> - Use the ratified canonical pipeline (Option A: tuned laptop; Option B: remote-container-canonical; Option C: dual-pipeline) per the standardization workstream's §3.4 ratified decision.
> - Stage 4 verdicts ratify normally.

Per Stage 4 doctrine. Run the **canonical pipeline** (per render-pipeline-standardization workstream's ratified decision — laptop `build-derivatives.sh` / `build-derivatives-alt.sh`, remote-container-pipeline-specific workflow, or both per Option C). Audit derivative outputs against source per §2.2 (character diff) + §2.3 (formula integrity, if math content) + §2.4 (tables) + §2.5 (figures) + §2.6 (layout integrity).

Capture xelatex stderr to build log + grep for `Missing character` warnings (load-bearing per Stage 4 §3.3 discipline). Output artifact: `tools/rigor-passes/<chapter-slug>_stage_4_render_audit_<date>.md`.

### §3.8 🚪 Stage 5 sign-off + pre-pub review queue (explicit-gate; fires at pre-external-review send + pre-publication)

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
- Add retrofit verdict summary to `publishing/essays/_pipeline/cross-thread-todos.md` (or wherever the cross-thread tracking lives at that time).
- If Pass 3.4 surfaces a cross-chapter handoff: PM session drafts the cross-chapter workstream handoff per pipeline doctrine §5.
- If Stage 4 surfaces a render-failure pattern not in the registry: add to `tools/quality-gates/regressed-patterns.yaml` (render-failure category).
- If Stage 5 pre-publication review queue surfaces a recommended-external-reviewer that's worth adding to the publisher / agent pitch tracker: PM session captures.

---

*End of pipeline-doctrine retrofit template. Per-chapter handoff stubs reference this template + scope the per-chapter work.*
