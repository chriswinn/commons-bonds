---
name: Portfolio triangulation discipline (drafter / prior-independent / fresh-second-independent)
description: Three-audit triangulation as the default discipline for Wave 2+ derivative essays at the Pass 3.3 + 3.4 + 3.5 explicit-gate cascade. Drafter's-self-audit + prior-independent + fresh-second-independent audits fire in parallel; §12 three-way cross-check is the author's primary ratification input. Codified 2026-06-01 from the Noema V-D second-independent empirical anchor.
type: feedback
---

# feedback_portfolio_triangulation_discipline

**Date ratified:** PROPOSED 2026-06-01
**Type:** feedback (operational discipline)
**Origin:** Noema V-D second-independent audit 2026-05-28 surfaced findings that any two-audit subset would have missed; portfolio-scope codification 2026-06-01 per `tools/workstream-handoffs/portfolio-triangulation-discipline-handoff_2026-06-01.md`.
**Canonical reference:** `tools/workstream-handoffs/portfolio-triangulation-discipline-handoff_2026-06-01.md` (full workstream-handoff with methodology spec + Wave 2 inventory + per-essay activation plan + PM-dashboard integration + cross-references).
**Layer:** scan-friendly summary; the canonical handoff carries the full architecture. Update the handoff when content changes; sync this summary via `tools/memory-updates/` spec for substantive amendments.

## Summary

Publisher-facing derivative essays at the Pass 3.3 + 3.4 + 3.5 explicit-gate cascade fire **three** audits, not one or two:

- **Drafter's-self-audit** — produced by the Stage 2 drafting session at draft completion; explicit drafter-bias caveat; documents expected per-character verdicts so the independents have a concrete cross-check target.
- **Prior-independent audit (audit #1)** — fresh CC session; do NOT read drafter's-self-audit until Phase 3 cross-check; covers Pass 3.3 + 3.4 + **fresh** Pass 3.5 (NOT "inherits clean" by assertion).
- **Fresh-second-independent audit (audit #2)** — fresh CC session; do NOT read drafter's-self-audit OR prior-independent until Phase 3 cross-check; covers Pass 3.3 + 3.4 + **fresh** Pass 3.5; §12 three-way cross-check is the load-bearing addition.

The two independents fire **in parallel** (`run_in_background`); independence is preserved by NOT reading each other's outputs until Phase 3 boundary. Phase 2 verdicts in each artifact are locked + filed BEFORE Phase 3 reads any prior artifact.

## Why this is the default (not the exception)

Under the 2026-05-28 ratified `feedback_token_cost_not_a_constraint.md`, the marginal token cost of triangulation (~100-300K per essay vs. 2-audit baseline) is bandwidth-cheap. Author-attention cost is near-zero (the author reads the compressed §12 cross-check, not the full per-pass tables). Clock-time cost is ~30-60 min if independents fire in parallel.

The cost that DOES bind: author attention at ratification disposition time. The §12 cross-check table compresses the three audits' findings into ~3-7 divergence points + a recommendation. Total cost is ~10-15 min author read per essay.

Failure modes of two-audit methodology (empirically observed in Wave 2):

- **Drafter-bias under-corrected.** Drafter expects draft to land well. Single-independent vs drafter = 1-vs-1 disagreement is ambiguous; the author has no convergence signal. Two independents agreeing against drafter = strong signal in independents' direction.
- **Pass 3.5 omission risk.** If the prior-independent's chip is under-specified (Pass 3.5 omitted), the gap is invisible; the prior-independent asserts "inherits clean" + ships. Aeon + Harper's + FA + NYRB V-D audits ALL hit this pattern; only V2 audits caught it. Triangulation prevents this structurally — the fresh-second-independent's scope ALWAYS includes Pass 3.5 fresh.
- **Single-auditor-lens-bias.** Any one independent audit has a particular reading the auditor brings. Two independents catch findings either alone would miss (e.g., Noema V-D F-DE-VD-H1 + F-DE-VD-M1 lineage-citation asymmetry).

## Cross-check convergence interpretation

- **3 audits converge** → strongest signal; ratify as recommended; close the finding.
- **2 audits converge against drafter** → strong signal in independents' direction; **default disposition: follow the independents.** Drafter-bias is structural.
- **2 audits converge against second-independent** → calibration question; reasonable readings differ; author surfaces directly + makes the call.
- **All 3 diverge** → genuine ambiguity; author surfaces directly + makes the call. Document all three positions + reasoning.

## When this fires (default + exceptions)

**Default:** every Wave 2+ derivative essay at Stage 2 drafted-prose completion + drafter's-self-audit filing. The triangulation chips spawn at that gate, in parallel.

**Exceptions:**
1. Essays already SUBMITTED (retroactive triangulation is moot).
2. Essays at Stage 1 brief without drafted prose (triangulation needs prose).
3. Author explicitly declines (override preserved).
4. Short-form pitches under ~500w with strong iterated control (per v2.0 Amendment C domain-of-applicability; Aeon V-E pitch is the empirical anchor — three-variant head-to-head sufficed without triangulation).
5. Long-form op-eds (~900w) DEFAULT TO TRIANGULATION (audience-load complexity matches essay-scope; Norway + McDowell op-eds were triangulated 2026-05-28).

## How to apply

### When firing a Stage 2 audience-blind drafting session

Update the kickoff paste-text to require, at Stage 2 completion:
- The drafted prose artifact.
- A **drafter's-self-audit** at `_archive/parallel-drafts_<DATE>/<essay>-essay_<variant>_drafters-self-audit.md` with explicit drafter-bias caveat.
- An end-of-session one-liner: `STATE: Stage 2 + drafter's-self-audit FILED; NEXT: prior-independent + fresh-second-independent audits spawn in parallel; AWAITING: author-spawn-of-triangulation-chips`.

### When spawning the two independent audit chips

Use the canonical paste-text templates at:
- `tools/workstream-handoffs/portfolio-triangulation-discipline-handoff_2026-06-01.md` §4.4.1 (prior-independent)
- `tools/workstream-handoffs/portfolio-triangulation-discipline-handoff_2026-06-01.md` §4.4.2 (fresh-second-independent)

Both fire with `run_in_background` from the PM session or the author's parallel-session-hop. Independence is preserved at the chip-paste-text level (explicit "do NOT read X until Phase 3" instructions).

### When reading the §12 cross-check at ratification time

The fresh-second-independent's §12 table compresses the three audits' findings:
- Per-character Pass 3.3 verdict three-way (you / drafter's / prior-independent's).
- Per-character Pass 3.4 thread-pull three-way.
- Per-finding Pass 3.5 three-way (with explicit "Pass 3.5 was run fresh: YES / NO" cell — load-bearing).
- Convergence/divergence categorization (a/b/c/d per §2.3 of the canonical handoff).
- Synthesis disposition recommendation (ratify-as-recommended / spot-fix / surface-bigger-issue / author-judgment).

Default ratification disposition: **follow the synthesis recommendation** unless the cross-check surfaces a 3-way divergence or a 2-of-3-against-second-independent calibration question the author wants to override.

### When updating the PM dashboard

Per `feedback_pm_dashboard_structure.md` v2.0, add per-essay columns:
- Drafter's-self-audit FILED (✅ / ⏳ / n/a)
- Prior-independent FILED (✅ / ⏳ / n/a)
- Fresh-second-independent FILED (✅ / ⏳ / n/a)
- Converged findings RATIFIED (✅ / ⏳ author-action)
- Convergence/divergence summary (3-way agreement count + 2-of-3-vs-drafter + 2-of-3-vs-2nd-independent + 3-way-divergence + YOU-only-Pass-3.5 count)

## Empirical anchors

### Noema V-D second-independent audit 2026-05-28 (THE METHODOLOGICAL ANCHOR)

`publishing/essays/noema-commons-bonds/rigor/pass-3-3-and-3-4-and-3-5-bundled_VERSION-D_SECOND-INDEPENDENT-AUDIT_2026-05-28.md` §12.

Specific 2-vs-1 findings:
- **T3.11 Chesapeake regional downgrade ✓✓✓ → ✓✓** — drafter said wash; both independents said downgrade. Under 2-audit methodology, this would be 1-vs-1 ambiguous; under 3-audit, 2-of-3 convergence drove SF-VD-1 spot-fix recommendation.
- **F-DE-VD-H1 HIGH (§VI cadence-arc broken)** — neither prior-independent nor drafter caught it. Prior-independent asserted "inherits clean" Pass 3.5 without running it. Fresh-second-independent ran Pass 3.5 fresh + surfaced HIGH-severity finding.
- **F-DE-VD-M1 MEDIUM (§Close lineage-citation asymmetry)** — YOU-only Pass 3.5 finding; neither prior audit surfaced it. Demonstrates the developmental-edit lens at the fresh-second-independent's scope catching findings outside the prior-independent's lens.

### Wave 2 V2-audit pattern repeated

Aeon V-D + Harper's V-D + Foreign Affairs V-D + NYRB V-D ALL had their prior-independent chips omit Pass 3.5 (asserted "inherits clean" without running). V2 audits caught the omission in each case. The pattern is structural (single-chip authoring tends to drop Pass 3.5 when bundled with 3.3 + 3.4); the triangulation prevents this by mandating Pass 3.5 fresh in BOTH independents.

### Drafter-bias bias-correction

Drafter's-self-audit on Noema V-D scored 7 ✓✓✓ + 5 ✓✓ + 2 ✓ at Pass 3.3 (most-positive). Fresh-second-independent scored 5 ✓✓✓ + 7 ✓✓ + 2 ✓ (most-conservative). Prior-independent scored 6 ✓✓✓ + 6 ✓✓ + 2 ✓ (between). All three produced 14/14 INCLUDE — the disagreement was on magnitude at 2 characters, not direction across the set. The discipline's value-add is calibration of magnitude at specific characters (T1.1 + T3.11), not full-set reorientation.

## Compatible with existing disciplines

- `feedback_audience_aware_drafting_discipline.md` (v3.1 pipeline doctrine) — triangulation is the v3.2-candidate amendment at the Pass 3.3 + 3.4 + 3.5 gate within Amendment A's explicit-gate cascade. Cross-references Amendment B Pass 3.5 (the fresh second-independent's load-bearing addition).
- `feedback_token_cost_not_a_constraint.md` — load-bearing rationale. Do not cite tokens as the cost in cost-benefit calculations for triangulation. The cost that binds is author attention at ratification time + cumulative pipeline clock-time.
- `feedback_parallel_session_ratification_cadence.md` — the two independents fire as parallel sub-sessions per the parallel-session-hop pattern. Each session presents findings one-at-a-time at its own Phase 3 cross-check; the §12 table is the compressed signal at author-ratification time.
- `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` — the hard rule benefits from triangulation amplification: §2.1-axis hard-rule verification runs through TWO independent reads, catching more invention near-misses than single-audit review. Harper's V-D V2 audit's §2.1 hard-rule axis is the canonical pattern.
- `feedback_pm_dashboard_structure.md` v2.0 — PM dashboard adds per-essay triangulation status columns per §5.1 of the canonical handoff.
- `feedback_merge_on_ratification.md` — auto-merge for internal scaffolding at session close. Triangulation chip artifacts are internal scaffolding; ratified spot-fixes ARE end-user-facing prose (auto-merge on author-ratification per the rule).

## Where to read more

- **Canonical handoff (full architecture):** `tools/workstream-handoffs/portfolio-triangulation-discipline-handoff_2026-06-01.md`
- **Methodological anchor:** `publishing/essays/noema-commons-bonds/rigor/pass-3-3-and-3-4-and-3-5-bundled_VERSION-D_SECOND-INDEPENDENT-AUDIT_2026-05-28.md` §12
- **Format precedents:** Aeon V-D drafter's-self-audit + prior-independent; Noema V-D + Harper's V-D V2 + FA V-D V2 + NYRB V-D V2
- **v3.1 pipeline doctrine:** `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`
- **Cost-framing:** `tools/memory/feedback_token_cost_not_a_constraint.md`

## Update log

- **2026-06-01.** Initial entry. PROPOSED status. Codifies the discipline + cross-references the canonical handoff + locks the empirical anchors (Noema V-D second-independent + Wave 2 V2-pattern + drafter-bias bias-correction). Awaits author ratification per the canonical handoff §9 state one-liner.

---

*End of portfolio-triangulation-discipline feedback entry.*
