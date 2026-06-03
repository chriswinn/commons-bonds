# Commons Bonds — Pipeline Doctrine (v1.0.0)

**Date drafted:** 2026-05-17
**Status:** PROPOSED — pending author ratification at session close.
**Origin:** Pipeline-revision workstream (handoff at [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](../workstream-handoffs/pipeline-revision-handoff_2026-05-17.md)); 11 decisions, 11 ratified at session start of 2026-05-17 (decisions #7 + #9 + #10 ratified within the originating brainstorm; decisions #1 + #2 + #3 + #4 + #5 + #6 + #8 + #11 ratified at the doctrine-session opening per author confirmation).
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
| **0** | Author conception / topic decision | [`tools/drafting-templates/stage-0-publishing-strategy-rigor-test.md`](../drafting-templates/stage-0-publishing-strategy-rigor-test.md) |
| **1** | Ready-to-draft gate (three sub-steps: 1a invariant + 1b structure + 1c coherence) | [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) + [`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`](../drafting-templates/stage-1-audience-aware-structure-pass.md) + [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) |
| **2** | Audience-blind drafting | [`tools/drafting-templates/stage-2-audience-blind-flow-draft.md`](../drafting-templates/stage-2-audience-blind-flow-draft.md) |
| **3** | **Five-pass rigor audit** (3.1 fact-check + 3.2 voice-polish + 3.3 audience-load acceptance + 3.4 audience-load robustness + **3.5 developmental-edit per Amendment B 2026-05-18**) | [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) (v3.0 four-pass split + v3.1 Amendment B Pass 3.5 codification) |
| **4** | ~~Render + character(glyph)-integrity audit~~ **RELOCATED to toolchain (Amendment E refinement 2026-06-02 — §14.7); not a per-artifact stage** | [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) |
| **5** | Academic-rigor + prose-quality sign-off bookend + pre-publication review queue artifact | [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) |

> **Amendment E (2026-06-02) adds a Portfolio layer above this per-artifact pipeline and rebuilds the Stage 0–2 front-end as `gather → [material-readiness gate] → allocate → plan → generate (min-only, no maximum) → cut`.** See §14 + the detailed spec. The Stage 3 + Stage 5 cascade is unchanged; **Stage 4 (render/glyph integrity) is relocated out of the per-artifact pipeline to toolchain-level rendering sessions per §14.7.**

---

## §2. Continuous infrastructure — invariant gates

**Two invariant scans run continuously: pre-commit + every stage transition + CI.**

### §2.1 Scaffolding scan

Detects placeholders + drafting-template scaffolding + process-scaffolding vocabulary that should never appear in publisher-facing prose:

- Placeholders (`TODO`, `TK`, `FIXME`, `XXX`, `[BRACKET]`).
- Drafting-template scaffolding (*"Let me explain"*, *"In this section…"*, *"The plain definition is this:"*).
- Process-scaffolding vocabulary (`Option A` through `Option Z`, `ratified`, `Phase C-*`, `F-V*`, `INCLUDE`/`EXCLUDE` glyphs `✓✓✓` / `⚠⚠⚠` used as verdicts, `EXCLUDE` / `INCLUDE` as standalone tokens).
- Meta-commentary tics (*"That is the whole sentence."*, *"What I mean to say is…"*).

Registry: [`tools/quality-gates/scaffolding-patterns.yaml`](../quality-gates/scaffolding-patterns.yaml).

### §2.2 Regressed-pattern scan

Detects patterns previously fixed by rigor passes (corpus-wide institutional memory). Each entry traces back to the rigor-pass artifact + commit that surfaced + fixed the pattern.

Categories:
- **Named LLM tics** (F-V1 through F-V21 from the Pass 2 voice-polish inventory: nostalgia tic *"There are not many people like that anymore"*; cadence-repetition *"It changed me. It humbled me."*; etc.).
- **Deprecated terminology** (term-rename / synonym-drift / superseded-name patterns).
- **Gate-decision-banned patterns** (vendor names held OUT per CEO-era NDA gate; named-subject anonymization decisions; etc.).
- **Cross-chapter consistency-inventory items** (terminology + symbol + flagship-equation canonical-name commitments).
- **Render-failure patterns** (em-dash / approx-symbol tofu-box fixes; minus-into-box rendering artifacts; etc.).

Registry: [`tools/quality-gates/regressed-patterns.yaml`](../quality-gates/regressed-patterns.yaml).

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

Implementation: [`tools/scripts/check-corpus-invariants.sh`](../scripts/check-corpus-invariants.sh).

---

## §3. Change-cascade routing protocol

> **AMENDMENT A — Selective stage-firing (ratified 2026-05-18).** Original v1.0.0 cascade treated all stages as equally auto-firing on every relevant change. **Per author direction 2026-05-18, the cascade is now two-class:** automatic-on-edit (cheap-when-needed; fires on every prose edit) vs explicit-gate (expensive-or-out-of-scope-for-routine-edits; fires only on explicit author trigger at specific gates). The token-economy rationale: with the render-toolchain-containerization workstream landed (Docker on laptop or remote-container), Stage 4 renders cost ~0 Claude tokens because they happen outside of Claude sessions; the cascade should reflect that Stage 4 is cheap to defer and only needs to fire at author-specified gates rather than as part of automatic cascade after every prose edit. Pass 3.3 + Pass 3.4 (audience-load) are similarly heavy enough that automatic re-firing on every spot-fix is wasteful — they fire on venue-changes, audience-set-changes, or pre-publication, not on every cascade.

**Two cascade classes:**

### §3.1 Automatic-on-edit cascade (cheap; fires on every relevant change)

| Change type | Routes back to | Then auto-fires |
|---|---|---|
| Any source-file change (pre-commit) | Stage 1a invariant-gate scans (automatic) | Commit refused on HIGH match; otherwise proceeds |
| New fact discovered (interview; family conversation; external verification) | Stage 1b canonical-facts inventory update | Pass 3.1 fact-check for affected scope + Pass 3.2 voice-polish for affected prose |
| New audience character identified | Stage 1b audience pressure-test set update | (Pass 3.3 / 3.4 explicit-gate per §3.2) |
| Bibliography commitment lands | Stage 1c cross-artifact coherence update | (Pass 3.3 explicit-gate per §3.2) |
| Spot-fix applied (any phase / any pass) | Stage 1c cross-artifact coherence (light) | (No automatic re-fire of audience-load; per §3.2 explicit-gate) |
| Cross-chapter workstream applies content to multiple chapters | Stage 1c cross-artifact coherence for all affected chapters (automatic) | (Pass 3.3 light re-fire per §3.2 explicit-gate, batched at workstream close) |
| Render-failure pattern surfaces (in source) | Stage 1a (registry update) | (Stage 4 re-run per §3.2 explicit-gate) |

**Net effect:** every prose edit auto-fires Pass 3.1 + Pass 3.2 (the value-added prose rigor); cheap-enough Claude-token cost is justified by the quality return.

### §3.2 Explicit-gate cascade (heavy; fires only on author trigger at specific gates)

| Stage / Pass | Fires when | Reason for gating |
|---|---|---|
| **Stage 4 (render-integrity audit)** | Pre-external-review send (e.g., before shipping a chapter to a peer reviewer / publisher / agent); pre-publication; on author "build it now" trigger; any publishing-pipeline-script change | Render is ~0 Claude tokens (happens via Docker locally or remote-container), but the audit work (text-extract, character-diff, layout-check, formula-integrity) is heavy + only needs to fire when an artifact actually ships. |
| **Stage 5 (sign-off + pre-pub review queue)** | Pre-external-review send; pre-publication; before any external-reviewer engagement | Stage 5 generates the pre-publication review queue artifact (mandatory deliverable per pipeline doctrine §7); only valuable at distribution-readiness gates. |
| **Pass 3.3 (audience-load acceptance)** | New audience character added (Stage 1b update); venue change (artifact retargets to different publication); pre-external-review send; pre-publication | Per-character audience-load test is heavy (15-25 acceptance characters scored). Spot-fixes rarely shift acceptance verdicts; batching at venue-change / pre-publication gates avoids redundant re-fires. |
| **Pass 3.4 (audience-load robustness)** | New adversarial character added; cross-chapter workstream affects the chapter (post-merge batched re-fire); pre-publication for any artifact with adversarial-exposure risk | Adversarial-set thread-pull synthesis is the heaviest pass; only fires at venue-change / pre-publication / cross-chapter-cascade gates. |
| **Pass 3.5 (developmental-edit)** — *added by Amendment B 2026-05-18* | Per-chapter, after Pass 3.1 + 3.2 + 3.3 + 3.4 ratify-and-apply complete; before pre-publication; on author "developmental read-through" trigger | Whole-chapter scale; restoration-of-richness lens; catches emotional-arc continuity + scene-anchor density + sensory-detail restoration + voice-flow continuity + cumulative-LLM-cadence residue + reader-engagement at analytical pivots. Heavy (~50K-80K tokens per chapter); only valuable at chapter-level distribution-readiness gates. Light Pass 3.3 re-fire recommended after Phase C application of any ratified Pass 3.5 spot-fixes. |
| **Cross-chapter workstream cascade light re-fire (Stage 1c + Pass 3.3-light)** | After cross-chapter touches land on main (batched per pipeline doctrine §5 step 4) | Heavy when applied per-chapter immediately on every cross-chapter touch; cheap when batched at workstream close. |
| **External-reviewer finding integration** | When the finding lands; gated on author disposition | Heavy work routing back through multiple stages; only fires when the finding warrants it. |

**Author trigger forms:**
- Explicit instruction in a session: *"Fire Stage 4 audit for Ch 5"* or *"Run pre-publication Stage 5 sign-off"* or *"Re-run Pass 3.3 for Ch 6 — venue changed to Phenomenal World."*
- PM-session-handoff entry routing the trigger to a fresh session.
- Pre-publication gating: a chapter approaching submission readiness automatically queues all four explicit-gate items (Stage 4 + Stage 5 + Pass 3.3 + Pass 3.4) as a pre-pub-readiness batch.

### §3.3 Light re-fire definition

**Light re-fire** means: re-test only the specific characters / facts / sections affected by the change, not the full pass. Full re-fire only when the change is structural or invalidates the prior pass's assumptions.

### §3.4 Token-economy rationale

The two-class cascade reflects an underlying token-economy observation:

| Work item | Approx Claude tokens per fire (chapter-scale) |
|---|---|
| Stage 1a invariant scan (script-driven) | <100 (just running `check-corpus-invariants.sh`) |
| Stage 1b update (canonical-facts inventory / audience-set update) | 500-2000 (depends on scope of update) |
| Stage 1c coherence check | 500-3000 (depends on cross-artifact scope) |
| Pass 3.1 fact-check | 5,000-15,000 (chapter content into context + reasoning + finding-extraction) |
| Pass 3.2 voice-polish | 5,000-15,000 (similar scope to 3.1) |
| Pass 3.3 acceptance (15-25 characters) | 20,000-60,000 (per-character simulation + verdict + finding-extraction) |
| Pass 3.4 robustness (5-10 adversarial characters) | 15,000-40,000 (adversarial-character simulation + thread-pull synthesis) |
| **Pass 3.5 developmental-edit** *(added Amendment B)* | **50,000-80,000 (whole-chapter context + 3-4 prior rigor-pass artifacts + AuthorsNote + raw-substrate dumps + reasoning + per-finding restoration drafts + whole-chapter synthesis)** |
| Stage 4 (render-integrity audit, via Docker render) | 500-3,000 (Docker render is ~0 tokens; audit work is text-extract + diff + finding-extraction) |
| Stage 5 sign-off + pre-pub review queue generation | 3,000-10,000 (artifact-generation work) |

The automatic-on-edit cascade (Pass 3.1 + Pass 3.2 + Stage 1c-light) totals ~10K-30K tokens per prose-edit event — justified by the value-added prose rigor. The explicit-gate cascade (Pass 3.3 + Pass 3.4 + Stage 4 + Stage 5) totals 40K-110K tokens per pre-publication batch — appropriate cost amortized over many prose edits, not paid per spot-fix.

### §3.5 Backward-compatibility with v1.0.0-original cascade

Prior cascade rules (where Pass 3.3 / 3.4 / Stage 4 were folded into automatic cascade) are now Amendment-A-superseded but archived for audit-trail. Sessions that fired heavy cascades prior to 2026-05-18 remain valid; new sessions fire per Amendment A.

### §3.6 Amendment B — Pass 3.5 developmental-edit ratification (2026-05-18)

**Author ratification 2026-05-18: Pass 3.5 (developmental-edit) is codified as the fifth pass within Stage 3, per Option (a) of the developmental-edit workstream handoff §2.2.** Stage 3 is now a **five-pass** rigor audit: 3.1 fact-check → 3.2 voice-polish → 3.3 audience-load acceptance → 3.4 audience-load robustness → **3.5 developmental-edit**.

**§3.6.1 What Pass 3.5 catches that 3.1-3.4 cannot:**

| Pass | Scale | Catches | Misses |
|---|---|---|---|
| 3.1 fact-check | Per-fact | Factual drift; source-citation accuracy | Whole-chapter narrative arc |
| 3.2 voice-polish | Per-paragraph | LLM tics (named-inventory matches) | Cumulative effect of multiple tic-fixes; clipped-after-cutting feel |
| 3.3 acceptance | Per-character (per-audience) | Whether target audiences INCLUDE | Whether the chapter HOLDS reader attention through analytically-loaded passages |
| 3.4 robustness | Per-adversarial-character | Hostile-read thread-pull synthesis | Same as 3.3 — character-set tests rather than experience-of-reading |
| **3.5 developmental-edit** | **Whole-chapter** | **Emotional-arc continuity; scene-anchor density; sensory-detail restoration; voice-flow continuity; cumulative-LLM-cadence residue; reader-engagement at analytical pivots** | **Cross-chapter narrative arc (handled by separate cross-chapter developmental-coherence workstream)** |

**§3.6.2 Pass 3.5 remediation polarity is RESTORATION, not cutting.**

Empirically grounded by the Ch 1 PROPOSED + RATIFIED developmental-edit review (`tools/rigor-passes/ch1_developmental_edit_review_2026-05-18.md`) §5.1 cumulative diagnosis: *"Pass 2's chiseling produced a clipped feel in several places that the developmental-edit lens reads as flatness-by-omission. The remedy is targeted RESTORATION (scene-anchor re-entry; both/and reveal breath; framework-close breath; specificity-restoration; faithfulness-of-the-model lineage paragraph), not further cutting."*

This is the methodological-clarity argument for Pass 3.5's separation from Pass 3.2 (Option (a) over folding-into-3.2): Pass 3.2 cuts; Pass 3.5 restores. Different polarities; folding would lose the discipline each polarity needs.

**§3.6.3 Pass 3.5 cadence within Stage 3.**

Per-prompt serial cadence extends: 3.1 → 3.2 → 3.3 → 3.4 → 3.5. Pass 3.5 fires AFTER 3.1-3.4 have ratify-and-applied because empirically the flatness only surfaces post-3.2's chiseling — the cumulative effect of 3.2's correct cuts is what 3.5 catches. Pass 3.5 may also surface findings about 3.2's apply/hold dispositions (e.g., Ch 1 F-DE-Ch1-5: "F-V2's spot-fix genericized the 'particular look on a child's face' specificity"); these route back as a 3.2-reconsider follow-up if needed.

**§3.6.4 Pass 3.5 explicit-gate firing per Amendment A.**

Pass 3.5 is an explicit-gate cascade item per §3.2:
- Fires per-chapter, after Pass 3.1 + 3.2 + 3.3 + 3.4 ratify-and-apply complete.
- Fires before pre-publication (the developmental edit is gate-relevant to publication readiness).
- Does NOT fire on every prose edit (~50K-80K tokens per chapter; only valuable at chapter-level distribution-readiness gates).
- Light Pass 3.3 re-fire recommended after Phase C application of ratified Pass 3.5 spot-fixes (confirms acceptance verdicts hold; cumulative restoration may shift acceptance for some characters).
- Pass 3.4 re-fire NOT routinely warranted (restorations strengthen rather than weaken adversarial robustness; thread-pull surface unchanged).

**§3.6.5 Empirical-grounding posture.**

Author ratified Amendment B on the Ch 1 single-chapter empirical basis. The developmental-edit workstream handoff §2.3 recommended waiting for all 10 chapters + AuthorsNote before codification; author ratified early on the methodological-clarity argument + the Ch 1 finding-distribution (3 HIGH + 7 MEDIUM + 3 LOW; HIGH findings clustered around recurring patterns).

Cross-chapter empirical grounding still proceeds via the developmental-edit workstream (Ch 2 → Ch 10 + AuthorsNote per-chapter sessions). If cross-chapter data surfaces material refinements to Pass 3.5's scope / cadence / finding-format, those land as future amendments (Amendment C, etc.) without disturbing the codification of Pass 3.5 as a fifth pass.

**§3.6.6 Memory entry version bump.**

`feedback_audience_aware_drafting_discipline.md` becomes **v3.1.0** (was v3.0 base + Amendment A inline). The v3.1.0 entry summarizes Pass 3.5 ratification + points to this Amendment B for the full codification. Memory-update spec at `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md` should be revised to capture the v3.1.0 framing.

### §3.7 Amendment C — Interactive Ratification Protocol for Prose-Modifying Passes (Ratified 2026-05-19)

**Author ratification 2026-05-19:** the existing rigor-pass artifact lifecycle (PROPOSED commit auto-merges to main; author ratifies externally; Phase C application applies ratified dispositions) does not adequately ensure prose-modifying dispositions receive deliberate author engagement. Amendment C codifies an **interactive ratification protocol** that walks author through each finding with options + recommendation + reasoning before any prose change is applied to chapter source.

**§3.7.1 Scope**

Amendment C applies to any pass or session that proposes PROSE CHANGES:

- Pass 3.1 fact-check (factual corrections modify prose)
- Pass 3.2 voice-polish (cuts / edits modify prose)
- Pass 3.5 developmental-edit (restorations modify prose)
- Phase C application sessions for any of the above (now functionally redefined as interactive ratification + application combined per §3.7.6)
- Cross-chapter workstreams that propose prose touches (e.g., rent-seeking-engagement; spatial / temporal cross-chapter cascades)
- Stage 1c coherence-check spot-fixes when they propose new prose (rare; usually 1c just verifies existing prose realizes commitments, but when a bibliography commitment lands mid-cycle, 1c may propose new prose)

Amendment C does NOT apply to:

- Stage 1a invariant scan (no prose mod)
- Pass 3.3 audience-load acceptance + Pass 3.4 audience-load robustness (verification passes; surface findings as character-verdicts; don't directly propose prose — when their findings recommend a prose spot-fix, the spot-fix routes through Amendment C as a Stage 3 sub-action)
- Stage 4 render-integrity audit (audit only)
- Stage 5 sign-off + pre-pub queue (artifact generation; no prose mod)

**§3.7.2 Per-finding format requirements (mandatory for Amendment-C-scoped artifacts)**

Each finding in a prose-modifying-pass artifact MUST include:

| Field | Description |
|---|---|
| Finding ID | e.g., `F-DE-Ch1-3` (pass-letter + chapter-number + sequence) |
| Severity | HIGH / MEDIUM / LOW |
| Location | line number + verbatim current text |
| Diagnosis | what's wrong / flat / incorrect / lost-richness |
| **Options** | A / B / C / hold-as-is — concrete alternative prose or actions |
| **Recommendation** | Which option Claude recommends + why |
| **Reasoning** | Cross-pass + cross-character + cross-chapter considerations that informed the recommendation |
| Author disposition | Initially: TBD pending ratification; updated post-ratification with selected option + rationale |

The Options + Recommendation + Reasoning fields are LOAD-BEARING for Amendment C — they're what the interactive ratification session walks through.

**§3.7.3 Two-session workflow (post-Amendment-C)**

Per author ratification 2026-05-19 (separate discovery from ratification; combine ratification with application):

1. **Discovery session** (Stage 3 pass: 3.1, 3.2, or 3.5):
   - Reads chapter source + prior-pass artifacts + relevant context.
   - Surfaces findings per the §3.7.2 per-finding format requirements.
   - Produces PROPOSED artifact (e.g., `tools/rigor-passes/ch<N>_<pass>_review_<date>.md`).
   - Auto-merges to main per CLAUDE.md rigor-pass merge default.

2. **Interactive ratification + application session** (combined; redefined Phase C under Amendment C):
   - Reads PROPOSED artifact from session 1.
   - Walks author through each finding per the §3.7.4 format.
   - For each finding: author selects A / B / C / hold-as-is / other-prose / defer.
   - **Applies ratified spot-fixes to chapter source IN THE SAME SESSION** (combined).
   - Commits both updates in one or more commits: §"Disposition log" appended to the PROPOSED artifact + chapter source changes from applied spot-fixes.
   - Auto-merges to main per CLAUDE.md author-ratified content-change merge default.

This replaces the prior three-step pattern (Discovery → Author-external-review → Phase C application). Under Amendment C: two sessions per pass per chapter.

**§3.7.4 Interactive ratification session format**

Per-finding walkthrough:

```
Finding [ID] ([SEVERITY]) at line [N]: "[verbatim current text]"

Diagnosis: [summary]

Options:
  A. [concrete option A]
  B. [concrete option B]
  C. [concrete option C]
  D. hold-as-is

Recommendation: [letter] — [why]

Reasoning: [cross-pass + cross-character + cross-chapter considerations;
trade-offs across other options]

→ Author: ?
```

Author responses:

- `A` / `B` / `C` — apply the selected option
- `hold` or `D` — no change to chapter source for this finding
- `other: [prose]` — apply author-provided prose instead
- `defer` — leave undecided; revisit in a future session

Capture each disposition + any additional author rationale in the §"Disposition log" of the PROPOSED artifact.

**§3.7.5 Disposition log format**

Appended to the PROPOSED artifact under a new §"§X. Disposition log (YYYY-MM-DD interactive ratification + application session)":

| Finding | Severity | Selected option | Disposition | Author rationale | Commit |
|---|---|---|---|---|---|
| F-XXX-1 | HIGH | A | APPLY | "Recommendation matches; restoration aligns with framework-naming intent." | `<short-sha>` |
| F-XXX-2 | MEDIUM | hold | HOLD | "Substantive register hold; cadence works as drafted." | — |
| F-XXX-3 | LOW | Other | APPLY (modified) | "Used B's structure with sensory detail per discussion." | `<short-sha>` |

Each APPLY disposition cites the commit short-sha that applied the spot-fix. HOLD dispositions have no commit (no chapter source change).

**§3.7.6 Why combine ratification with application (vs separate)**

Author direction 2026-05-19: **combined**. Rationale:

- **Immediate feedback loop.** Author sees ratified spot-fix applied in context immediately; can correct if the application reveals a subtle issue the walkthrough didn't surface.
- **One session, one commit-batch.** Faster than two-session pattern; preserves cadence-momentum.
- **Pause-and-defer safety.** If a finding turns out to need more thought during the walkthrough, author can `defer` it; session continues with other findings; deferred findings revisit in a future session.

The separate-sessions pattern (ratification commits disposition log; Phase C application later applies spot-fixes) is RESERVED for edge cases where the author wants explicit review of the disposition log before any chapter source changes (e.g., heavy structural revisions where author wants to validate the disposition set as a whole before any application).

**§3.7.7 Retroactive scope**

Pre-Amendment-C ratifications remain valid (e.g., Ch 1 developmental-edit review ratified "as recommended and proposed" per commit `1f5c6ad` 2026-05-18 — this dispositioning is author-ratified per the prior workflow). However, per author direction 2026-05-19: **Ch 1 dev-edit's Phase C application (not yet fired) follows Amendment C interactive protocol** — author sees each restoration applied in context as it lands, even though dispositions are already ratified.

Net retroactive scope rule: if dispositions are ratified but application has not yet fired, the application session follows Amendment C interactive protocol. If both ratification + application are pre-Amendment-C, those stay archived as pre-Amendment-C work.

**§3.7.8 Token-economy positioning**

| Session type | Approx Claude tokens (chapter-scale) |
|---|---|
| Discovery session (Pass 3.1 / 3.2 / 3.5) | 50,000-80,000 (whole-chapter context + prior-pass artifacts + finding-extraction + per-finding drafting) |
| Interactive ratification + application session (combined; new under Amendment C) | 10,000-25,000 (read PROPOSED artifact + per-finding walkthrough + apply ratified spot-fixes) |
| Separate ratification-only session (edge case; for the §3.7.6 reserved pattern) | 5,000-15,000 |
| Separate Phase C application-only session (edge case) | 5,000-15,000 |

Net Amendment C overhead: ~10-15% increase per pass per chapter vs prior pattern. Disposition-quality gain is significant — every finding receives deliberate author engagement before any prose change lands.

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

5. **Source manifest (where the venue's citation norm is inline / no bibliography — the normal case for magazine essays + op-eds; Amendment E refinement §14.8, 2026-06-02).** A per-piece sheet mapping every inline citation / factual claim → its source → verification status (verified / needs-pin / soft / written-around / figure-currency). The **trigger is the venue's citation norm, not the piece type**: a magazine essay or an op-ed cites inline and ships NO bibliography, so it gets the manifest (the fact-check support sheet that travels with the submission package, which the venue's assigned fact-checker works from). A venue that instead expects a formal reference list gets that apparatus; the book carries a bibliography. Lives at `publishing/essays/<venue>/source-manifest.md`. Reference instance: the Atlantic Ideas manifest; template: [`tools/drafting-templates/source-manifest-template.md`](../drafting-templates/source-manifest-template.md).

### §7.2 Format

Pre-publication review queue artifact lives at `tools/pre-submission-reviews/[artifact-name]_pre_pub_review_queue_v1.0.0.md` (note: directory already exists per repository layout).

Template: see [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) §3.

### §7.3 Discipline

Transparent quality-control disclosure rather than overclaiming-verification posture. The queue is not a confession of weakness; it is a structural artifact identifying where external expertise adds value relative to internal verification capability.

External-reviewer engagement policy: per ratified decision #10 (2026-05-17 brainstorm), the author self-signs Stage 5 + explicitly flags at hand-off; college-tutors-as-bounded-bonus-capacity is the working arrangement for limited external review pre-publication. The pre-pub review queue is the structural artifact that surfaces what the publisher should engage post-acceptance.

---

## §8. Versioning + relationship to existing canonical artifacts

### §8.1 Hybrid versioning (per ratified decision #8)

- This doctrine artifact (`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`) is the **canonical reference** carrying the full architecture.
- The author's memory entry `feedback_audience_aware_drafting_discipline.md` is updated to **v3.0** with a concise summary + pointer to this artifact. Memory entry stays scan-friendly; doctrine artifact carries the full architecture. Memory-update spec is at [`tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`](../memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md).

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

Per-chapter retrofit scope: see [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](../workstream-handoffs/pipeline-revision-handoff_2026-05-17.md) §6.2.

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

- [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](../workstream-handoffs/pipeline-revision-handoff_2026-05-17.md) — the originating handoff
- [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) — Stage 1 doctrine (three-step structure)
- [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) — Stage 4 doctrine (render + character-integrity audit)
- [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) — Stage 5 doctrine + pre-publication review queue template
- [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) — Stage 3 four-pass template (v3.0 framing)
- [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) — character-set construction (acceptance + robustness)
- [`tools/quality-gates/scaffolding-patterns.yaml`](../quality-gates/scaffolding-patterns.yaml) — scaffolding-scan registry
- [`tools/quality-gates/regressed-patterns.yaml`](../quality-gates/regressed-patterns.yaml) — regressed-pattern-scan registry
- [`tools/scripts/check-corpus-invariants.sh`](../scripts/check-corpus-invariants.sh) — invariant-check script
- [`tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`](../memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md) — memory-entry update spec for v2.0 → v3.0

---

## §14. Amendment E — Two-level architecture + front-end rebuild (Ratified 2026-06-02)

**Canonical detailed spec:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_two-level-reorg_PROPOSED_2026-06-02.md`](commons_bonds_pipeline_doctrine_two-level-reorg_PROPOSED_2026-06-02.md) (RATIFIED 2026-06-02 — filename retains the `PROPOSED` slug for git-history continuity; the in-file status is RATIFIED). This §14 is the summary + pointer, mirroring the Amendment D codification pattern.

**Empirical anchor:** the Atlantic Ideas Pricing-Honestly iteration (2026-05-28 → 2026-06-01) + the archived per-chapter GuidanceDocs.

**§14.1 Root-cause reframe.** The compressed/clunky prose the cascade fought was a **generation-time failure**: imposing a maximum length *manufactured* compression at drafting. Fix: **min-only generation from abundance; no maximum ever reaches the drafter.**

**§14.2 Two levels.** The v1.0.0 Stage 0–5 pipeline is a *per-artifact assembly line*. Amendment E adds a **Portfolio layer** above it — a standing, compressed *map* (cross-corpus duplication matrix + per-artifact unique-contribution profiles + allocation decisions). It gives cross-artifact coherence without holding all artifact text in one context; each per-artifact session reads the map. Differentiation has **two axes**: internal-corpus (the matrix) and external-field (`publishing/essays/<essay>/research/differential-positioning.md` — what the piece says that the discourse doesn't).

**§14.3 Per-artifact front-end rebuilt** to **gather → [material-readiness gate] → allocate → plan → generate → cut → cascade → calibrate**:
- **Gather** — three-layer harvest: (1) collect-what-exists broadly (abundance + field-map of what's already been said → feeds external differentiation), (2) goal-directed overlay (tag what accomplishes landing), (3) outstanding-needs note. All harvested material runs the §5 two-state fabrication gate (tentative-with-provenance → confirmed-on-landing).
- **Material-readiness gate** — `READY-TO-ALLOCATE` is the common default (no citations needed / fair-use abundance exists / explicit thought-experiment register — guardrail: explicit register + no fabricated-as-real subject). `NOT-READY-NEEDS-X` requires a two-branch diagnosis (a: mis-diagnosed unrecognized-abundance → really READY; b: genuine gap → blocking/non-blocking + EV/cost-justification where the binding cost is real-world time/travel/clock, NOT tokens; non-blocking → 4 paths incl. ship-now-upgrade-later + reframe-as-thought-experiment). `RECONSIDER` = the X.5 substrate-question relocated to the front-end.
- **Allocate** = coarse pre-draft cut (which cases belong here, consulting the portfolio map). **Cut** = fine post-draft cut (write-long-then-cut; X.3).
- **Generate** = minimum floor anchored to venue, **no maximum**.
- **Calibrate** = running actual-vs-minimum tally, used *descriptively* to pick future floors — never as a target.

**§14.4 Supporting changes.**
- **Drafting-plan artifact** succeeds the per-chapter GuidanceDocs: disposable per-cycle, sectioned (source pool / allocation+scope incl. readiness-verdict preface / differential-positioning pointer / what-lands plan / counterarguments / register notes), points up to the portfolio map.
- **Per-venue submission-norms artifact** (`publishing/venues/<venue>/submission-norms.md`), **partitioned by a contamination firewall**: drafter-safe block (editorial brain, format, minimum) vs editorial-only block (maximum + calibration band, consulted by Cut + Stage 5 only, never injected into the generation prompt).
- **X.6 essay→book sub-cascade** (six steps, batched via `book-amendment-candidates.md`, hard (a)+(b)+(c) threshold, Cut-phase trigger). **Class-boundary flag:** step 3 touches chapter prose = merge-on-*ratification*, NOT the auto-merge governing scaffolding.

**§14.5 Disposition of handoff amendments X.1–X.6.** X.1 (fresh-start Stage 2) demoted to a legacy fallback for old-max-length-regime essays. X.2/X.3 = prose-craft made structural (brief §5 + the Cut phase). X.4 = standalone memory entry (`tools/memory/feedback_cost_constraint_removal_default_reset.md`). X.5 relocated to the readiness gate's `RECONSIDER`. X.6 widened (see §14.4).

**§14.6 Deferred (downstream work, not framework gaps).** Per-essay differentiation *criteria* (both axes); corpus-wide audit scope; Atlantic Ideas editorial cut/focus timing. See the detailed spec §7.

**§14.7 Stage 4 relocation (refinement, ratified 2026-06-02).** Stage 4 ("render + character-integrity audit") is **removed from the per-artifact pipeline.** "Character-integrity" there always meant **glyph/typography integrity** (em-dash/≈ tofu-boxes, accents, EB Garamond font naming, math-formula corruption) — not portrayal of named people. That is a **toolchain concern**, handled in dedicated rendering-pipeline sessions fired corpus-wide when render issues surface, NOT a per-essay gate. The author's actual practice already works this way: render problems are debugged in the rendering pipeline itself, not in the individual essay/chapter/op-ed. Effect: the per-artifact pipeline runs Stage 0–3 → Stage 5; the author's own read-through and sharing-for-human-review are author activities, not pipeline stages. The cascade is **3.1 → 3.2 → 3.3 → 3.4 → 3.5 → Stage 5.** (The `commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md` doc is retained as the rendering-pipeline reference, now toolchain-scoped rather than per-artifact.)

**§14.8 Source manifest as a standard pre-pub artifact (refinement, ratified 2026-06-02).** Where the **venue's citation norm is inline / no bibliography** — the normal case for **magazine essays and op-eds** — the Stage 5 pre-publication review queue includes a **source manifest** as a standard component (§7.1 item 5): a sheet mapping every inline citation / factual claim → source → verification status. **The trigger is the venue's norm, not a fixed piece-type list.** Rationale: a magazine essay cites inline and ships **no bibliography** (appending one reads as a category error to a magazine editor — bibliographies belong to books and academic journals); the manifest is the internal fact-check support sheet that travels with the submission package and is what the venue's assigned fact-checker works from. **Match the venue's actual apparatus where it differs:** a venue that expects a formal reference list gets that instead; the **book** carries the bibliography (`research/literature/bibliography.md`). The manifest and the bibliography stay distinct so per-piece citation tracking does not duplicate or drift from the master bibliography (the 2026-06-02 Marx-entry sync was the empirical anchor for that drift risk). Location: `publishing/essays/<venue>/source-manifest.md`; template: `tools/drafting-templates/source-manifest-template.md`; reference instance: the Atlantic Ideas manifest.

---

*End of Commons Bonds Pipeline Doctrine v1.0.0. PROPOSED 2026-05-17; Amendment B 2026-05-18; Amendment C 2026-05-19; Amendment D 2026-05-31; Amendment E 2026-06-02.*
