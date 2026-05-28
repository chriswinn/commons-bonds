# Stage 1c Cross-Artifact Coherence Check — Ch 5 + TA §1.10 Public Choice Sibling-Coherence (D-3 firing)

**Date:** 2026-05-25
**Pass:** Stage 1c (cross-artifact coherence check) per pipeline doctrine v1.0.0 §3.1
**Scope:** D-3 deferred sibling-coherence-check (per Stage 1c §8 deferred queue, 2026-05-21). Ch 5 line 202 "Architecture and rent-seeking: who shaped the system?" closing paragraph + Tech Appendix §1.10 "Scope: complementarity with Public Choice / rent-seeking analysis" paragraph, both checked against Ch 9 Reading C v3 framing (lines 134–148) + Ch 8:122 Stage 1c Option A canonical post-cascade state.
**Trigger:** Author ratification 2026-05-25: "ratify Pass 3.3 Character 15 Option A as recommended; fire the Stage 1c D-3 deferred sibling-coherence-check." D-3 deferred per Stage 1c §8 (2026-05-21 commit `cbef9bd`) covering IF-2 (sibling-chapter cross-chapter touches from same rent-seeking-engagement workstream) + IF-3 (verb-frame drift "does the work cleanly" vs "supplied the vocabulary for"). Pass 3.4 §5.2 + §6.1 additionally surfaced MacLean consolidation as new D-3 sub-scope.
**Status:** PARTIAL FIRING — D-3a (MacLean consolidation, Char 15 Option A) **APPLIED in this commit** to all three sites; D-3b (symmetric-vs-asymmetric framing alignment, original IF-2 + IF-3 scope) **PROPOSED** options offered, AWAITING author ratification before Phase C application.
**Branch:** `claude/ch9-pass3-4-phase-c-1fae85` (feature branch from current origin/main; rigor-pass artifacts + author-ratified end-user-facing prose auto-merges to main per CLAUDE.md merge default).

---

## §0. Source artifacts read

| Artifact | Path | Line count | Commit verification |
|---|---|---|---|
| Ch 5 — *The Accountability Gap* | `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` | (post-D-3a-application; rent-seeking section at lines 186–202) | Rent-seeking section inserted by `a1e54d9` (2026-05-17), ratified `bc02767` (2026-05-18) |
| Ch 9 — *Pricing Honestly* (canonical reference) | `manuscript/chapters/Chapter__9_PricingHonestly.md` | 294 lines (post-D-3a-application) | Reading C v3 substantive rewrite at `78a26c2` (2026-05-21); lines 134–148 |
| Ch 8 — *What Things Actually Cost* (canonical reference) | `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` | (post-Option-A) | Stage 1c Phase C Option A applied at `cbef9bd` (2026-05-21) |
| Tech Appendix v2.0.0 | `core/technical-appendix/TechnicalAppendix_v2.0.0.html` | (post-D-3a-application; §1.10 PC paragraph at line 610) | Public Choice scope-of-applicability paragraph inserted by `a1e54d9` (2026-05-17), ratified `bc02767` (2026-05-18) |
| Stage 1c Ch 8 artifact (D-3 origin) | `tools/rigor-passes/commons_bonds_stage_1c_coherence_check_2026-05-21_ch8_rent_seeking_v1.0.0.md` | 310 lines | §6.2 IF-2 + IF-3 + §8 D-3 deferral; canonical D-3 framing source |
| Pass 3.3 acceptance (Ch 9) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md` | 688 lines | §2 Char 15 Option A canonical sentence at lines 414–417; §6.3 default hold-as-is |
| Pass 3.4 robustness (Ch 9) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md` | (commit `f47dd1c`) | §3 T3 + §5.2 D-3 MacLean consolidation scope expansion; §7.3 Phase-C disposition recommendation |
| Pipeline doctrine v1.0.0 | `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` | (§3 + §3.1 + §3.3 verified) | Stage 1c position + change-cascade routing |
| Memory: [audience-aware drafting](../memory/feedback_audience_aware_drafting_discipline.md) | | v3.0 + Amendment A two-class cascade | Pre-publication review queue framing |
| Memory: [verify-stale-memory-claims](../memory/feedback_verify_stale_memory_claims.md) | | (heeded staleness reminder; all date / file / commit / line claims verified) | n/a |
| Memory: [named-subject consent](../memory/feedback_named_subject_consent.md) | | public-record exception | Scholarly citation discipline (Buchanan, Tullock, MacLean) |

**Commit verification (all referenced hashes confirmed on `origin/main`):**
- `a1e54d9` — cross-chapter rent-seeking engagement PROPOSED (2026-05-17)
- `bc02767` — cross-chapter rent-seeking engagement workstream RATIFIED (2026-05-18)
- `78a26c2` — Ch 9 Pass 2 Phase C + Reading C v3 (2026-05-21)
- `cbef9bd` — Ch 8 Stage 1c Phase C Option A (2026-05-21)
- `a6b7df5` — Ch 9 Pass 3.3 acceptance PROPOSED (2026-05-23)
- `f47dd1c` — Ch 9 Pass 3.4 robustness PROPOSED (2026-05-23)

---

## §1. Coherence-check scope

### §1.1 What is being checked

Two parallel sites where the cross-chapter rent-seeking-engagement workstream (`a1e54d9` → `bc02767`) inserted Public-Choice-engagement content under the older symmetric framing the Reading C v3 rewrite of Ch 9 subsequently superseded:

**Site A — Ch 5 line 202** (closing paragraph of "Architecture and rent-seeking: who shaped the system?" section). Current verbatim text (post D-3a application):
> The framework's accounting of who bore the cost is therefore compatible with — and depends on — the Public Choice tradition's analysis of who shaped the architecture. Read together, the two questions describe the same systems from complementary angles. Read apart, each is partial. The remainder of this chapter develops the framework's response apparatus; readers who want the architecture-shaping analysis the framework's apparatus does not perform should read Buchanan and Tullock and their successors in parallel. The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project.

**Site B — TA §1.10 line 610** ("Scope: complementarity with Public Choice / rent-seeking analysis" paragraph). Current verbatim text (post D-3a application), with key framing-relevant clauses extracted:
> The framework's cost-severance accounting operates at the architecture level — identifying which parties absorb which costs given an institutional architecture's distributive properties. A complementary analytical question — who shaped the institutional architecture, by what political-economic process, with what rent-seeking expenditure — is the domain of Public Choice analysis (Buchanan & Tullock 1962; Tullock 1967; Mueller 2003 and successors). **The framework is compatible with Public Choice analysis layered on top of it, and depends on it for cases where the architecture's origins are part of the substantive analytical work.** The framework does not attempt to replicate Public Choice's actor-identification methodology; the framework's apparatus is calibrated for cost-bearing-party identification + magnitude, not for political-coalition-of-architecture-shapers analysis. Applicability conditions: [...] Readers in the Public Choice tradition should read the framework's cost-bearing-party identification as a foundation their apparatus can apply to, not as an alternative to their apparatus. The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this Appendix draws on the vocabulary rather than endorsing the project.

(Bold sentence is the framing-relevant load-bearing clause for the audit.)

### §1.2 What it is being checked against

**Reference 1 — Ch 9 Reading C v3 (lines 134–148).** Canonical asymmetric-framing source-of-truth per author ratification 2026-05-21. Key Reading C v3 moves:

1. **Asymmetric framework-vs-Public-Choice positioning.** Public Choice = the extractor's reasoning under incomplete cost-visibility (Ch 9:138). Framework = the complete ledger that changes what the extractor is reasoning about (Ch 9:138, 142). Not symmetric mutual-citation; not "complementary accounting."
2. **Verb-frame discipline.** *"Public Choice **supplied the vocabulary** for analyzing the extractor's reasoning; the framework **supplies the accounting** that changes what the extractor is reasoning about"* (Ch 9:144). Two parallel verb-frames; framework supplies the ledger to which Public Choice's analytical chain can be applied.
3. **Asymmetric closing — *"the angles are not symmetric"*** (Ch 9:144). Explicit rejection of mutual-symmetry framing.

**Reference 2 — Ch 8:122 Stage 1c Phase C Option A (commit `cbef9bd`).** Post-cascade canonical Ch 8 framing that brought Ch 8 into alignment with Reading C v3. The Option A spot-fix replaced the symmetric *"Both readings illuminate McDowell. The framework's apparatus contributes the cost-bearing magnitudes; both adjacent traditions contribute the actor-and-coalition analysis the framework does not attempt"* with asymmetric "supplies the vocabulary for" parallels.

### §1.3 What is explicitly NOT in scope

- Re-litigating Ch 9 Reading C v3 framing or Ch 8:122 Option A. Both are fixed canonical references.
- Asking whether the asymmetric framing itself is correct. The author ratified asymmetric framing 2026-05-21; this audit only checks sibling-coherence with the ratified canonical form.
- Apparatus / register audits beyond the rent-seeking-engagement paragraphs (incidental flags surfaced in §6 but not the primary scope).
- T7 (hard-left ideological-accommodation thread, Pass 3.4 §5.1) Ch 10 cross-chapter cascade — out of D-3 scope per Pass 3.4 §6.1; routes to Ch 10 Pass 3.4 future-session.

---

## §2. D-3a — MacLean consolidation (Char 15 Option A) — APPLIED

### §2.1 Sibling-coherence finding

**All three rent-seeking-engagement sites (Ch 5 line 202 + Ch 9 line 144 + TA §1.10 line 610) operated without explicit MacLean (*Democracy in Chains*) engagement in their pre-D-3a state.** The audit confirms: no site mentioned MacLean, no site engaged the Buchanan-political-project controversy, all three sites recommended reading Buchanan + Tullock without acknowledging the contested-political-project critique. The pre-D-3a coherence state was therefore *uniformly MacLean-silent*; the Pass 3.4 §5.2 hypothesis that the MacLean gap is sibling-consistent across all three sites is confirmed.

### §2.2 Ratification source

Author ratification 2026-05-25: "ratify Pass 3.3 Character 15 Option A as recommended." Per Pass 3.3 Char 15 §2 (lines 414–417), the canonical Option A sentence:

> The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project.

Pass 3.4 §6.1 (Char 7 cross-chapter cascade flag) + §7.3 (Phase-C disposition recommendation) offered two coordinated approaches:
- **Option A1.** Apply at Ch 9-only level (per Pass 3.3 Char 15 Option A original recommendation).
- **Option A2.** Apply as consolidated cross-chapter MacLean-acknowledgment note across Ch 5 + Ch 9 + TA §1.10 sites (per Pass 3.4 §5.2; routes through D-3 firing).

Author's "fire the Stage 1c D-3 deferred sibling-coherence-check" instruction selects **Option A2** (consolidated cross-chapter application). D-3a applied in this Phase C session.

### §2.3 Per-site application

| Site | Pre-application closing | Post-application addition | Voice register adaptation |
|---|---|---|---|
| **Ch 9 line 144** | *"should read Buchanan and Tullock alongside this book."* | + *"The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project."* | None — canonical Char 15 Option A form. |
| **Ch 5 line 202** | *"should read Buchanan and Tullock and their successors in parallel."* | + same sentence as Ch 9 | None — canonical form fits Ch 5's expository-policy register. |
| **TA §1.10 line 610** | *"...as a foundation their apparatus can apply to, not as an alternative to their apparatus."* | + *"The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this **Appendix** draws on the vocabulary rather than endorsing the project."* | Single-word substitution: *"this book"* → *"this Appendix"* to match the Tech Appendix self-reference register (TA elsewhere uses *"the Appendix does not develop this apparatus..."*). |

### §2.4 D-3a sibling-coherence verdict — ✓ APPLIED

Post-application coherence state: all three rent-seeking-engagement sites now carry the same Char 15 Option A MacLean-acknowledgment sentence (with single-word voice-register adaptation at TA). A reader proceeding Ch 5 → Ch 9 → TA §1.10 will encounter the methodological-vs-political distinction consistently at each Public-Choice-engagement site. Pass 3.4 §3 T3 (Buchanan implicit endorsement insufficient) is **disarmed** at all three sites by the application; the MacLean-sympathetic adversarial-read pressure-test that produced ⚠⚠ EXCLUDE in Pass 3.4 Char 2 verdict is now structurally addressed across the corpus.

### §2.5 Acceptance-test impact verification

Pass 3.3 §6.3 noted the Option A spot-fix would shift Pass 3.3 Char 15 (MacLean-sympathetic) from ✓ INCLUDE toward ✓✓ INCLUDE. Acceptance-test impact on the other 17 Pass 3.3 characters is verified neutral-to-positive:

- **Char 1 (trade-press), 2 (Ostrom-successor), 3 (environmental-economics):** Single-sentence addition; no register-friction. Pass 3.3 ✓✓ INCLUDE unchanged.
- **Char 5 (Lindsey & Teles center-left PC):** The methodological-vs-political distinction substantively aligns with Lindsey & Teles' own move; if anything strengthens the ✓✓ INCLUDE verdict.
- **Char 6 (libertarian PC, qualified ✓ INCLUDE):** Sentence reads as scholarly courtesy; does not soften the explicit "should read Buchanan and Tullock alongside this book" recommendation. Verdict unchanged at qualified ✓ INCLUDE.
- **Char 7 (reparations-tradition):** Methodological-vs-political distinction reinforces the framework's structural-injustice politics; ✓✓ INCLUDE unchanged.
- **Char 14 (left-progressive natural-fit):** Sentence reads as the framework declining to endorse Buchanan's broader project; aligns with natural-fit audience's political orientation. ✓✓ INCLUDE unchanged or strengthened.
- **Tier-3 characters (8, 9-13, 16-18):** Sentence is a single-clause scholarly courtesy; no acceptance-verdict shift.

**No Pass 3.3 acceptance verdict shifts from INCLUDE toward NEUTRAL or EXCLUDE.** D-3a application is acceptance-test-neutral-to-positive.

---

## §3. D-3b — Symmetric-vs-asymmetric framing alignment (original IF-2 + IF-3 scope) — PROPOSED

### §3.1 Sibling-coherence finding

The pre-Ch-9-Reading-C-v3 framing the rent-seeking-engagement workstream operated under (per Stage 1c §6.2 IF-2: "the symmetric 'complementary accounting' framing the Reading C v3 rewrite supersedes would have informed those Ch 5 + TA touches as well") still informs Ch 5 line 202 + TA §1.10 line 610 prose. Specifically:

#### §3.1.1 Ch 5 line 202 — symmetric-framing markers

| Symmetric-framing marker | Pre-D-3b text | Reading C v3 / Option A asymmetric counterpart |
|---|---|---|
| *"compatible with — and depends on"* | "compatible with — and depends on — the Public Choice tradition's analysis of who shaped the architecture" | "supplies the accounting that changes what the extractor is reasoning about" (Ch 9:144) — framework as upstream; PC's analysis can be applied to it, not vice versa |
| *"complementary angles"* | "Read together, the two questions describe the same systems from complementary angles" | "the angles are not symmetric" (Ch 9:144) — explicit rejection |
| *"each is partial"* | "Read apart, each is partial" | Reading C v3 does not frame the framework as "partial" relative to PC; the framework's ledger is the complete ledger (Ch 9:138, 142). PC and framework address *different layers of the same political-economy question*, not *each-partial-and-mutually-completing*. |

**Verdict for Ch 5:** ⚠⚠ INCOHERENT with Reading C v3 / Option A canonical form. The three symmetric markers above all enact the framing Reading C v3 abandoned. A reader proceeding Ch 5:202 → Ch 9:144 sequentially will experience framing-shift at *"the angles are not symmetric"* — identical to the framing-shift Ch 8:122 produced before its Option A application.

#### §3.1.2 TA §1.10 line 610 — partial symmetric-framing markers

| Symmetric-framing marker | Pre-D-3b text | Reading C v3 / Option A asymmetric counterpart |
|---|---|---|
| *"compatible with Public Choice analysis layered on top of it, and depends on it"* | "The framework is compatible with Public Choice analysis layered on top of it, and depends on it for cases where the architecture's origins are part of the substantive analytical work" | Two semi-asymmetric framings co-occur in tension: "layered on top of it" implies framework-as-base-layer / PC-as-overlay (asymmetric in framework's favor); *but* "depends on it" implies framework-needs-PC (asymmetric in PC's favor). Reading C v3 asymmetric direction: framework supplies the ledger; PC's actor-identification analysis can be applied to it. The "depends on" direction-of-dependency contradicts that. |
| *"as a foundation their apparatus can apply to, not as an alternative to their apparatus"* | (preserved as-is in current TA) | ✓ Already aligned with Reading C v3 asymmetric direction. This clause is the existing TA equivalent of Ch 9:148's *"the ledger then shows what they designed has been costing, and to whom"*. |

**Verdict for TA:** ⚠ DRIFT (partial). One framing-relevant clause (*"depends on it"*) operates in the contradicted direction; the closing clause is already aligned. Cleaner fix than Ch 5; one clause-level rewrite vs Ch 5's three-marker realignment.

#### §3.1.3 Verb-frame drift (IF-3) — does not surface at either site

Stage 1c §6.2 IF-3 flagged the "does the work cleanly" verb-frame at Ch 8:122 (pre-Option-A) as the verb-frame that implied Public Choice does the analytical work itself rather than supplying vocabulary the framework uses. Ch 5 line 202 + TA §1.10 line 610 do **not** carry this specific verb-frame drift in their current prose. Ch 5 uses "depends on" and "complementary angles" (different drift category, captured in §3.1.1 above); TA uses "compatible with" and "layered on top of" + "depends on" (also different drift category, captured in §3.1.2).

The IF-3 verb-frame drift was Ch-8-specific to the pre-Option-A "does the work cleanly" phrasing. D-3b does not need to address IF-3 separately at Ch 5 or TA; the IF-2 framing-alignment scope subsumes the verb-frame realignment requirement at both sibling sites.

### §3.2 Proposed options for Ch 5 line 202 realignment

The author should ratify one of the options below before Phase C application. Default per per-prompt serial cadence: D-3b PROPOSED state awaits ratification; no application in this session.

**Option A — Substantive paragraph-level realignment (parallel in scope to Ch 8:122 Option A).** Replace the three symmetric-framing markers with asymmetric framing matching Reading C v3 + Ch 8:122. Preserves all other paragraph content (the McDowell + Libby + Deepwater + 2008 + healthcare case-walks above; the read-B&T recommendation; the D-3a MacLean acknowledgment).

Proposed Ch 5 line 202 replacement prose:

> The framework's accounting of who bore the cost supplies the ledger to which the Public Choice tradition's analysis of who shaped the architecture can be applied. Where Public Choice supplies the vocabulary for analyzing how rent-seeking-shaped architectures come to be, the framework supplies the accounting of what those architectures have cost and to whom. The two traditions describe the same political-economy phenomenon from two angles, but the angles are not symmetric: the framework's apparatus is the upstream layer the Public Choice tradition's actor-identification analysis is best equipped to apply to. The remainder of this chapter develops the framework's response apparatus; readers who want the architecture-shaping analysis the framework's apparatus does not perform should read Buchanan and Tullock and their successors in parallel. The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project.

Key moves:
- Replace "compatible with — and depends on" with "supplies the ledger to which... can be applied" (asymmetric).
- Replace "Read together, the two questions describe the same systems from complementary angles. Read apart, each is partial" with "describe the same political-economy phenomenon from two angles, but the angles are not symmetric" (asymmetric per Ch 9:144 canonical form).
- Preserve "read Buchanan and Tullock and their successors in parallel" — the recommendation is intact; the framing around it is realigned.
- Preserve the D-3a MacLean acknowledgment sentence as the paragraph close.

**Option B — Light-touch (single-sentence realignment).** Replace only the *"Read together / Read apart / each is partial"* symmetric closure with an asymmetric closure; preserve "compatible with — and depends on" as-is. Lower-touch; partial alignment.

Proposed Ch 5 line 202 lighter replacement (only the middle two sentences change):

> The framework's accounting of who bore the cost is therefore compatible with — and depends on — the Public Choice tradition's analysis of who shaped the architecture. The two traditions describe the same political-economy phenomenon from two angles, but the angles are not symmetric: the framework supplies the cost-ledger that the Public Choice tradition's actor-identification analysis can be applied to. The remainder of this chapter develops the framework's response apparatus; readers who want the architecture-shaping analysis the framework's apparatus does not perform should read Buchanan and Tullock and their successors in parallel. The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project.

Trade-off: preserves "compatible with — and depends on" which carries residual symmetric framing; closer alignment than the pre-D-3b state but not full Option A alignment.

**Option C — Hold-as-is.** Ch 5's apparatus-introduction register may justify retaining the *"depends on"* + *"complementary angles"* framing because Ch 5 is the chapter that introduces the rent-seeking complementarity for the first time; the symmetric framing may be appropriate for the introduction-context (asymmetric framing belongs in the Ch 9 policy-architecture context where the framework's substantive contribution is at stake). Rationale: Ch 5 is naming a complementarity-question; Ch 9 is operationalizing the framework's asymmetric contribution. The two chapters can carry different framings if the chapter-role-difference justifies it.

Trade-off: leaves cross-chapter framing-shift in place. A reader proceeding Ch 5 → Ch 8 → Ch 9 sequentially will experience the framing-shift at Ch 9:144 (and to a lesser extent at Ch 8:122 post-Option-A). The Pass 3.4 Char 1 (libertarian PC hostile reviewer) ⚠⚠ EXCLUDE verdict noted that the cross-pressure structure between Ch 5 + Ch 9 framings could re-arm the libertarian-PC adversarial read.

**Recommended option for Ch 5:** **Option A** (substantive paragraph-level realignment). Brings Ch 5 into full sibling-coherence with Ch 8:122 + Ch 9 Reading C v3; eliminates the cross-chapter framing-shift risk Pass 3.4 Char 1 flagged. Trade-off: ~70-word substantive rewrite of the closing paragraph; preserves all McDowell + Libby + case-walk content above.

### §3.3 Proposed options for TA §1.10 line 610 realignment

**Option A — Single-clause replacement.** Replace the *"compatible with Public Choice analysis layered on top of it, and depends on it for cases where the architecture's origins are part of the substantive analytical work"* clause with asymmetric-direction framing.

Proposed TA §1.10 line 610 replacement (only the framing-relevant sentence changes; surrounding sentences preserved):

> The framework's cost-severance accounting operates at the architecture level — identifying which parties absorb which costs given an institutional architecture's distributive properties. A complementary analytical question — who shaped the institutional architecture, by what political-economic process, with what rent-seeking expenditure — is the domain of Public Choice analysis (Buchanan & Tullock 1962; Tullock 1967; Mueller 2003 and successors). **The framework supplies the cost-bearing-party accounting that Public Choice analysis can be applied to where the architecture's origins are part of the substantive analytical work; the framework does not depend on Public Choice methodology for its own apparatus.** The framework does not attempt to replicate Public Choice's actor-identification methodology; the framework's apparatus is calibrated for cost-bearing-party identification + magnitude, not for political-coalition-of-architecture-shapers analysis. Applicability conditions: [...] Readers in the Public Choice tradition should read the framework's cost-bearing-party identification as a foundation their apparatus can apply to, not as an alternative to their apparatus. The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this Appendix draws on the vocabulary rather than endorsing the project.

Key moves (bold sentence):
- Replace "compatible with Public Choice analysis layered on top of it, and depends on it" with "supplies the cost-bearing-party accounting that Public Choice analysis can be applied to" (asymmetric direction).
- Add explicit non-dependency clarification: "the framework does not depend on Public Choice methodology for its own apparatus" (Reading C v3 alignment).
- Preserve applicability-conditions list + closing clause (already aligned per §3.1.2).
- Preserve D-3a MacLean acknowledgment as paragraph close.

**Option B — Hold-as-is.** TA §1.10's "scope-of-applicability" voice register may justify a more deferential framing toward Public Choice analysis because the Tech Appendix's audience includes specialist readers who expect respectful scholarly-tradition-citation. The "depends on it for cases where the architecture's origins are part of the substantive analytical work" framing acknowledges scope-boundary honestly (the framework's apparatus does not handle architecture-origins analysis; that requires PC). Rationale: TA's methodological-precision register may earn the deferential framing the prose chapters cannot.

Trade-off: leaves the framing-shift between TA §1.10 + Ch 9:144 in place. A specialist reader cross-referencing TA → Ch 9 may notice the direction-of-dependency mismatch.

**Recommended option for TA:** **Option A** (single-clause replacement). Lighter-touch than Ch 5 Option A (one clause vs three markers); preserves applicability-conditions detail; brings TA into asymmetric-direction alignment with Ch 9 + post-Option-A Ch 8. The methodological-precision register accommodates the asymmetric framing because the asymmetric framing is itself the more precise methodological statement (the framework does not depend on PC for its core apparatus; specialists will register the precision).

---

## §4. Verdict summary

### §4.1 D-3a (MacLean consolidation) — **APPLIED**

| Site | Verdict | Status |
|---|---|---|
| Ch 9 line 144 | ✓ APPLIED (canonical Char 15 Option A sentence) | Phase C complete; commit this session |
| Ch 5 line 202 | ✓ APPLIED (canonical Char 15 Option A sentence) | Phase C complete; commit this session |
| TA §1.10 line 610 | ✓ APPLIED (canonical sentence with "this Appendix" voice adaptation) | Phase C complete; commit this session |
| Sibling coherence | ✓ COHERENT — all three sites carry the MacLean acknowledgment consistently | D-3a sub-scope CLOSED |

### §4.2 D-3b (symmetric-vs-asymmetric framing alignment) — **PROPOSED, AWAITING RATIFICATION**

| Site | Verdict | Recommended Option | Status |
|---|---|---|---|
| Ch 5 line 202 | ⚠⚠ INCOHERENT with Reading C v3 + Ch 8:122 Option A canonical | **Option A** (substantive paragraph-level realignment) | PROPOSED; awaits author ratification before Phase C |
| TA §1.10 line 610 | ⚠ DRIFT (partial; one clause-level rewrite) | **Option A** (single-clause replacement) | PROPOSED; awaits author ratification before Phase C |
| Cross-chapter coherence post-D-3b application | ✓ COHERENT (under Option A at both sites) | — | Achievable upon author ratification |

### §4.3 Pass 3.4 thread-impact

- **T3 (Buchanan implicit endorsement insufficient).** **Disarmed by D-3a application** at all three sites. Pass 3.4 Char 2 (MacLean-sympathetic) ⚠⚠ EXCLUDE pressure-point now structurally addressed; verdict would shift toward ⚠ EXCLUDE (push-back but chapter holds against push-back) on adversarial re-read.
- **T1 (decision-tool framing implies prescriptive direction).** Unaffected by D-3 application; remains HOLD per Pass 3.4 §3.
- **T7 (hard-left ideological accommodation).** Unaffected by D-3 application; remains HOLD + Ch 10 cross-chapter forward-flag per Pass 3.4 §6.1.
- **Cross-chapter coherence post-D-3b (if Option A ratified at both Ch 5 + TA):** Full sibling-coherence across Ch 5 + Ch 8 + Ch 9 + TA §1.10. Eliminates the Pass 3.4 Char 1 (libertarian PC) cross-chapter cross-pressure risk; eliminates the specialist-reader Ch 5 → Ch 9 framing-shift risk.

### §4.4 What is NOT changed by this firing

- Reading C v3 Ch 9 framing (lines 134–148) — canonical reference; unchanged.
- Ch 8:122 Option A post-cascade state — canonical reference; unchanged.
- D-2 (book-wide "honest" → "complete" sweep) — separately deferred per Stage 1c §8; not addressed by this firing.
- T7 → Ch 10 Pass 3.4 forward-flag — separately routed per Pass 3.4 §6.1; not addressed by this firing.

---

## §5. Out-of-scope flagging

### §5.1 D-2 (book-wide "honest" → "complete" sweep) — separately deferred

Stage 1c §8 D-2 (book-wide "honest" → "complete" sweep at apparatus-describing positions) remains deferred. Pass 3.3 §4.3 + Pass 3.4 §6.2 verified no new urgency. D-3 firing does not pre-empt or accelerate D-2.

### §5.2 T7 (hard-left thread) → Ch 10 Pass 3.4 forward-flag

Pass 3.4 §6.1 routes T7 (ideological accommodation of capital at Ch 9:170 *"completion of the market mechanism"* + structural-observation-not-advocacy discipline) to Ch 10's Pass 3.4 future-session input. Ch 10 closing-reflection register touches the framework-as-honest-accounting close; whether the hard-left thread re-triggers there is a Ch 10 question. **Not addressed by D-3 firing.**

### §5.3 Pass 3.5 (developmental-edit) Ch 9 readiness

Pass 3.4 §7.4 noted Pass 3.5 can fire after Pass 3.4 ratify-and-apply. D-3a application (this session) is the Phase C application for the only required Pass 3.4 spot-fix (T3). Pass 3.5 readiness is therefore advanced one step: Pass 3.5 fires after author confirms D-3a application + (optionally) ratifies D-3b options OR ratifies D-3b deferral.

### §5.4 Pass 3.3 acceptance test re-fire

Per pipeline doctrine §3 change-cascade routing: "Spot-fix applied → Stage 1c (light) → Pass 3.3 (light) re-fire." D-3a application is a prose-modifying spot-fix at three sites; per discipline, a Pass 3.3 light re-fire is warranted. §2.5 above verified D-3a application is acceptance-test-neutral-to-positive; a formal Pass 3.3 light re-fire would document the verdict for the corpus's pre-publication review queue. **Flagged for separate Pass 3.3 light re-fire session** — not blocking this artifact's Phase C application.

If D-3b is also ratified for Phase C application, both Ch 5 + TA §1.10 would warrant their own Pass 3.3 light re-fire (Ch 5 has a 30-character acceptance test; TA §1.10 inherits relevant scholarly-engagement characters). Recommended sequencing: ratify D-3b → Phase C apply → Pass 3.3 light re-fire across Ch 5 + Ch 9 + TA (post-D-3b) in one consolidated session.

---

## §6. Incidental observations (out-of-scope for primary audit)

### §6.1 Apparatus / hyphenation discipline — clean across all three sites

D-3a application preserves all apparatus + hyphenation + italicization disciplines at each site. Single-sentence insertion; no register-level changes; no apparatus tokens (Greek letters, subscripts, integrals) in inserted prose. Verdict: clean.

### §6.2 Named-subject consent — clean per public-record exception

Buchanan named at all three sites (already pre-D-3a); D-3a adds Buchanan-political-project gesture without new biographical claim. *Democracy in Chains* / MacLean implicit at all three sites (the "many readings of Buchanan's broader political project" gesture acknowledges the controversy without naming it). Public-record exception per [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md) applies: scholarly citation of contested-interpretation literature is on-record scholarly discourse. No consent gating required.

### §6.3 Reading-cycle observation — D-3a sentence becomes a sibling-recurrence anchor

Across all three sites, the D-3a sentence reads at the close of the Public-Choice-engagement passage. A sibling-coherent reader (cross-referencing Ch 5 ↔ Ch 9 ↔ TA §1.10) will encounter the same sentence three times — a recurrence-pattern that doubles as the framework's standing methodological-vs-political distinction across the corpus. The recurrence is structurally appropriate (each occurrence belongs at its site's PC-engagement close); not register-flat (the surrounding prose at each site differs); not over-anchored (three occurrences across 294 + 296 + ~700-line range is sparse). No reading-cycle concern.

---

## §7. Hard constraints honored

- ✓ Did NOT re-litigate Reading C v3 Ch 9 framing — canonical per author ratification 2026-05-21.
- ✓ Did NOT re-litigate Ch 8:122 Option A post-cascade state — canonical per Stage 1c Phase C 2026-05-21 (commit `cbef9bd`).
- ✓ Did NOT apply D-3b options to Ch 5 line 202 or TA §1.10 line 610 — PROPOSED state; awaits author ratification.
- ✓ DID apply D-3a (Char 15 Option A) to all three sites per author's 2026-05-25 explicit ratification.
- ✓ Did NOT contact named subjects (Buchanan, Tullock, MacLean cited via public-record scholarly-discourse exception).
- ✓ Verified pre-application file state for all three sites + commit hashes for all cited references.
- ✓ Built feature branch `claude/ch9-pass3-4-phase-c-1fae85` from current origin/main per workstream-handoff branch discipline.
- ✓ Bundled D-3a Phase C application + D-3 sibling-coherence-check artifact + Pass 3.4 §10 disposition log + cross-thread-todos D-3 update in a single atomic commit per author-ratified Phase-C session pattern.

---

## §8. Session-close protocol

Per pipeline doctrine + CLAUDE.md rigor-pass merge default + author-ratified end-user-facing-prose merge:

1. ✓ D-3 sibling-coherence-check artifact (this document) produced.
2. ✓ Ch 9 line 144 + Ch 5 line 202 + TA §1.10 line 610 D-3a spot-fix applied.
3. Pending: Pass 3.4 artifact §10 disposition log appended.
4. Pending: cross-thread-todos D-3 entry updated (D-3a CLOSED; D-3b PROPOSED awaiting ratification).
5. Pending: single atomic commit + fast-forward merge to `main`; push to `origin/main`.
6. Pending: report back to author per the closing summary format.

**Author decisions needed (post-session):**

- **D-3b-Ch5.** Which Ch 5 line 202 realignment option to ratify (Option A substantive / Option B light-touch / Option C hold-as-is / other). **Recommended:** Option A.
- **D-3b-TA.** Which TA §1.10 line 610 realignment option to ratify (Option A single-clause / Option B hold-as-is / other). **Recommended:** Option A.
- **Pass 3.3 light re-fire scheduling.** Whether to schedule the Pass 3.3 light re-fire (for D-3a application only, or for D-3a + D-3b post-ratification consolidated). Recommended sequencing: ratify D-3b → apply D-3b → consolidated Pass 3.3 light re-fire across Ch 5 + Ch 9 + TA.
- **Pass 3.5 sequencing for Ch 9.** Whether Pass 3.5 (developmental-edit) fires next on Ch 9 (per Pass 3.4 §7.4 readiness) or after D-3b consolidation completes.

---

*End of Stage 1c D-3 sibling-coherence-check — partial firing 2026-05-25. D-3a APPLIED (Char 15 Option A consolidated across Ch 5 + Ch 9 + TA §1.10). D-3b PROPOSED options for Ch 5 + TA §1.10 framing-alignment; awaits author ratification. Cross-chapter coherence is partially restored (MacLean dimension complete; framing-dimension PROPOSED).*

---

## §9. Disposition log (2026-05-25 Phase C — D-3b ratification + application)

**Author ratification 2026-05-25 (same session, immediately after Pass 3.4 verdict ratification):**

> "ratify all outstanding decisions as recommended"

### §9.1 D-3b ratification

Author selected the recommended Option A at both sites per §4.2 + §3.2 + §3.3:
- **D-3b-Ch5:** Option A (substantive paragraph-level realignment) RATIFIED.
- **D-3b-TA:** Option A (single-clause replacement) RATIFIED.

### §9.2 Phase C application

| Site | Pre-D-3b clause | Post-D-3b clause |
|---|---|---|
| **Ch 5 line 202** | *"compatible with — and depends on... Read together... Read apart, each is partial."* (three symmetric markers) | *"supplies the ledger to which... can be applied... supplies the vocabulary for analyzing how rent-seeking-shaped architectures come to be... the framework supplies the accounting of what those architectures have cost and to whom... the angles are not symmetric: the framework's apparatus is the upstream layer the Public Choice tradition's actor-identification analysis is best equipped to apply to."* (asymmetric per Option A) |
| **TA §1.10 line 610** | *"compatible with Public Choice analysis layered on top of it, and depends on it..."* (one symmetric clause) | *"supplies the cost-bearing-party accounting that Public Choice analysis can be applied to where the architecture's origins are part of the substantive analytical work; the framework does not depend on Public Choice methodology for its own apparatus."* (asymmetric per Option A) |
| **Ch 9 line 144** | (unchanged — canonical per Reading C v3 + D-3a) | (unchanged) |

D-3a MacLean acknowledgment sentence preserved at all three sites.

### §9.3 D-3b verdict closure

| Site | Pre-D-3b verdict | Post-D-3b verdict |
|---|---|---|
| Ch 5 line 202 | ⚠⚠ INCOHERENT | ✓ COHERENT with Reading C v3 + Ch 8:122 Option A canonical |
| TA §1.10 line 610 | ⚠ DRIFT (partial) | ✓ COHERENT |
| Cross-chapter sibling-coherence | partial (post-D-3a only) | ✓ FULL COHERENT across Ch 5 + Ch 8 + Ch 9 + TA §1.10 |

### §9.4 Pass 3.3 light re-fire consolidated post-D-3b

Per pipeline doctrine §3.3 + §5.4 recommended sequencing: consolidated Pass 3.3 light re-fire across Ch 5 + Ch 9 + TA fired same session. Verdict: **✓ ACCEPTANCE-TEST DEFENSIBLE**; no INCLUDE → NEUTRAL/EXCLUDE shifts at any site for any character; several verdicts trend strengthened (natural-fit, reparations-tradition, MacLean-sympathetic, EJ-movement, libertarian-PC cross-pressure reduced). Artifact at [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_pass_3_3_light_refire_ch5_ch9_ta_post_d3b_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-25_pass_3_3_light_refire_ch5_ch9_ta_post_d3b_v1.0.0.md) (this commit).

### §9.5 Pass 3.4 cross-chapter cross-pressure structural improvement

Per Pass 3.4 §3.1 synthesis observation + §9.4: cross-pressure structure between Char 1 (libertarian-PC hostile) and Char 7 (hard-left hostile) now operates without cross-chapter framing-shift compounding that Char 1's pre-D-3b ⚠⚠ EXCLUDE pressure-point depended on. Cross-pressure-positioning diagnostic operates at strongest possible posture — chapter positioned correctly + position structurally coherent across the corpus.

### §9.6 What D-3b closure does NOT do

- Does NOT re-fire Pass 3.4 — Pass 3.4 §11.5 closure discipline holds; D-3b reinforces rather than re-litigates CONDITIONALLY ROBUST verdict.
- Does NOT pre-empt Pass 3.5 (developmental-edit) Ch 9.
- Does NOT pre-empt T7 → Ch 10 Pass 3.4 forward-flag.
- Does NOT update Ch 9 prose (already canonical).

### §9.7 What D-3b closure advances

- **Stage 1c D-3 sibling-coherence-check fully CLOSED** across both sub-scopes.
- **Cross-thread-todos #16 moves to RESOLVED** (this commit).
- **Pass 3.5 (developmental-edit) Ch 9 fully unblocked at all upstream gates.**
- **Cross-chapter sibling-coherence for Public-Choice-engagement now uniformly asymmetric** across Ch 5 + Ch 8 + Ch 9 + TA §1.10.
- **Cross-pressure positioning diagnostic validated at strongest posture.**

---

*End of D-3 sibling-coherence-check — FULLY CLOSED 2026-05-25 (Phase C). D-3a + D-3b both RATIFIED + APPLIED + Pass 3.3 light re-fire ✓ ACCEPTANCE-TEST DEFENSIBLE. Cross-chapter sibling-coherence ✓ COHERENT across all four Public-Choice-engagement sites. Pass 3.5 (developmental-edit) Ch 9 fully unblocked for next session.*
