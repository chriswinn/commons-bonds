# Working Principle #7 — retroactive scan of past rigor passes

**Date:** 2026-04-26
**Purpose:** Per author direction 2026-04-26, scan past rigor passes for places where retired-term external-reception worries were inappropriately weighted (treated as rigor input rather than as scheduling-only observation). Companion to the formal Principle #7 ratification + rigor protocol §3.5 update.

---

## §1. Headline finding

**No clear Principle #7 violations identified.** The pre-publication-state discipline has been implicitly held across past rigor passes, just not formally named. Principle #7 codifies an already-operating practice rather than correcting widespread violations.

---

## §2. Methodology

Scanned all 47 rigor passes in `tools/rigor-passes/` for patterns suggestive of inappropriate weighting:

1. **Pattern A — rename-cost-as-rigor-argument.** Grep for "rename cost," "renaming cost," "cost of renaming," "rename will," "X chapter refs would need," "sweep cost." Inappropriate weighting would treat these as verdict inputs rather than as scheduling observations.

2. **Pattern B — retired-term reception worries.** Grep for "AIT users," "Value Capture users," "ARP users," etc. — phrases suggesting an existing audience for a retired term that doesn't actually exist (no external reader has used any of these terms).

3. **Pattern C — forward-simulation against retired terms.** Grep for collision-checks or critic-pressure-tests run on terms that had already been retired at the time of the rigor pass.

4. **Pattern D — Principle #1 violations adjacent to Principle #7 (effort-to-repair as rigor argument).** Grep for "rewrite cost...rigor," "effort...verdict," etc.

---

## §3. Findings

### §3.1 Pattern A — rename-cost-as-rigor-argument

**Found in:** Multiple rigor passes mention rename costs / sweep costs / chapter-ref counts.

**Verdict:** **Discipline consistently held.** In every case found, the rigor pass explicitly invokes Principle #1 (effort-to-repair-not-a-rigor-argument) to disclaim the cost as scheduling-only. Examples:

- `term_ait_v1.0.0.md`: *"Principle #1 — 439 AIT + 50 full-form uses represent massive sweep cost if rename chosen; this is scheduling observation, not verdict input."*
- `term_csg_v1.0.0.md`: *"Principle #1 — Ch 7 + Ch 9 rewrite cost is downstream scheduling."*
- `term_cost_severance_collision_v1.0.0.md`: *"Principle #1 — sweep cost of rename is scheduling, not verdict input."*
- `term_rcv_v1.0.0.md`: *"Principle #1 — RCV is the framework's most-used term (658 + 71 = ~730 references across 34 files); rename sweep cost is scheduling observation, not verdict input."*
- `term_cost_severance_vs_severed_cost_v1.0.0.md`: *"Principle #1 — whichever verdict lands, downstream sweep cost is scheduling, not rigor input."*
- `term_temporal_cost_severance_v1.0.0.md`: *"Principle #1 — any rewrite cost for the 6 existing references is a downstream scheduling note, not a verdict input."*
- The current `commons_bonds_rigor_pass_2026-04-26_term_consistency_gate_rename_v1.0.0.md`: *"Principle #1 — sweep cost is downstream scheduling, not verdict input."*

**No violations of Principle #1 found in current rigor passes.**

### §3.2 Pattern B — retired-term reception worries

**Found in:** `term_abundances_v1.0.0.md` and `term_cit_rename_v1.0.0.md` — phrases that involve "AIT" (now retired) appear in M6 / M11 / M12 contexts.

**Verdict:** **NOT violations.** These passes ran when AIT was the active term. The pass on AIT (`term_ait_v1.0.0.md`) tested AIT as a candidate-publication term against established academic priors — appropriate forward-simulation. The CIT-rename pass (`term_cit_rename_v1.0.0.md`) tested AIT vs CIT head-to-head — both candidate-publication terms at time of test. The abundances pass (`term_abundances_v1.0.0.md`) tested abundance-related vocabulary when those terms were still active.

**Per Principle #7's regime distinction:** these passes ran in the *active-term* regime (terms were candidate-publication), not in the *retired-term* regime. Forward-simulation at full weight was appropriate at the time.

**No Principle #7 violations identified for past passes that were testing terms that have since been retired.**

### §3.3 Pattern C — forward-simulation against retired terms

**Found in:** `vocabulary_footprint_meta_v1.0.0.md` had an initial recommendation that was self-corrected.

**Specifically:** the meta-pass initially recommended PROMOTE-CSG-to-Ring-2 with chapter-rewrite cost cited as a reason to avoid retiring. Chris caught this in real-time as a Principle #1 violation. The pass documents its own self-correction:

> *"**Initial (incorrect) recommendation:** PROMOTE CSG to Ring-2 (internal load-bearing), with chapter-rewrite cost cited as reason to avoid retiring."*
>
> *"**Correction per Chris Winn 2026-04-24 + now-ratified Principle #1 (effort-to-repair is not a rigor argument):** rewrite cost is not valid reasoning on a framework correctness decision. Redo the analysis on rigor-only grounds."*

**Verdict:** This is **Principle #1 working as designed** — the discipline caught the violation, documented it, and corrected the analysis. The self-correction is exactly the kind of in-pass discipline the working principles establish. Not a current violation; a documented past-and-corrected error preserved for provenance.

### §3.4 Pattern D — Principle #1 violations elsewhere

**Found in:** None.

**Verdict:** **No active Principle #1 violations** in the current rigor-pass archive.

---

## §4. One self-correction in this session's work

While running this scan I noticed an **inaccurate self-criticism in the supplemental Gate-2 M6 pass I just produced** (`commons_bonds_rigor_pass_2026-04-26_gate_2_naming_M6_supplement_v1.0.0.md` §8). I claimed the prior Gate-2-rename pass (`commons_bonds_rigor_pass_2026-04-26_term_consistency_gate_rename_v1.0.0.md`) had "Dimensional Consistency" in its §1.3 alignment table at full per-test weight. **This was inaccurate.** The prior pass references "Dimensional Consistency" in three places (§6.2 register-grounds note; §8.1 academic-literature established-vocabulary note; §22 cross-reference) — all appropriate provenance uses, not full-weight pressure tests. The prior pass has no §1.3 alignment table; my self-criticism conflated different sections.

**Action taken:** flagging this here for provenance; the supplement's broader argument about Principle #7 is unaffected (the principle is real and worth codifying), but the specific example I cited from the prior pass is wrong. The prior pass treated retired Dimensional Consistency appropriately (provenance use; no full-weight pressure testing).

---

## §5. Why no widespread violations exist

The framework's rigor protocol has Principle #1 (effort-to-repair-not-a-rigor-argument) ratified since 2026-04-24. That principle catches the most common Principle #7-adjacent violation pattern (treating internal repair cost as rigor input). Principle #7 extends Principle #1 by specifying that retired-term external-reception is similarly disqualified — but the underlying discipline (separate scheduling cost from rigor input) was already operating.

Principle #7's contribution is therefore:
1. **Codifying** an implicitly-held discipline as explicit rule
2. **Specifying** that the discipline applies to external-reception modules (M6 / M11 / M12) on retired terms
3. **Closing a small gap** in Principle #1's coverage (Principle #1 was about repair effort; Principle #7 is about retired-term forward-simulation — adjacent but distinct concerns)

The rigor protocol §3.5 addition operationalizes the discipline into module procedure (term-classification declared at module top per pass).

---

## §6. Recommended actions

1. **No retroactive revisions to past rigor passes needed.** The discipline has been held cleanly. Past rigor on terms that have since been retired ran when those terms were candidate-publication — the forward-simulation at full weight was appropriate at the time.

2. **One small correction recommended in the recent supplement pass:** the inaccurate self-criticism noted in §4 above. I'll add a footnote to the supplement's §8 acknowledging the inaccuracy. Effort: 1 small edit + commit.

3. **Going-forward discipline applies via rigor protocol §3.5.** All future rigor passes that run M6/M11/M12 will declare term-classification at module top per Principle #7 + protocol §3.5.

4. **Periodic re-scan recommended** as the framework approaches publication. If terms move from candidate-publication regime to published-and-then-retired regime (post-publication retirement), the discipline shifts; rigor on those retirements would need different weighting. Currently all retirements are pre-publication; this regime change is not operative.

---

## §7. Cross-references

- `alignment/commons_bonds_working_principles_v1.0.0.md` §1 — Principle #7 (ratified 2026-04-26).
- `tools/commons_bonds_rigor_protocol_v2.4.0.md` §3.5 — operational discipline for M6/M11/M12.
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-26_term_consistency_gate_rename_v1.0.0.md` — the original pass; spec checked above.
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-26_gate_2_naming_M6_supplement_v1.0.0.md` — the supplemental pass; one inaccurate self-criticism flagged above for correction.
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_vocabulary_footprint_meta_v1.0.0.md` — documents the discipline working as designed (in-pass self-correction on rewrite-cost-as-rigor-argument).

---

*End of Principle #7 retroactive scan, 2026-04-26. No widespread violations identified; discipline has been implicitly held; codification through Principle #7 + protocol §3.5 captures the practice formally going forward.*
