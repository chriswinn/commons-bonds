# Boston Review Essay — Workstream Handoff (2026-05-09)

**Date drafted:** 2026-05-09 · **v2.0 drafting-discipline application appended 2026-05-10**
**Branch to create at session start:** `claude/boston-review-essay-<harness-id>` (branch from current `origin/main`)
**Status going in:** Pitch + essay both not yet drafted. Source chapter Ch 5 is drafted with Pistor + Christophers engagement landed (commit `d78872e`).

---

## ★ v2.0 two-stage drafting discipline applies to this workstream (2026-05-10)

The two-stage audience-aware drafting discipline ratified at v2.0 on 2026-05-10 is the **default methodology for this essay**. Any fresh session opening this workstream must apply v2.0 in full. Authoritative reference: `feedback_audience_aware_drafting_discipline.md` (memory). Empirical basis: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md` and `..._aeon_pitch_stage3_comparison_v1.0.0.md`.

**Regime fit.** This workstream is a long-form (~4,500w) publisher-facing essay derived from Ch 5 *The Accountability Gap* — a chapter that contains Pistor / Christophers / Susskind engagement plus the Restitution-and-Foreclosure two-instrument decomposition. The v2.0 domain-of-applicability rule clauses fire as follows:

- **(a) Path B contamination risk applies.** The essay derives from Ch 5 prose; drafting from the chapter as source text reproduces the Noema-essay-A failure pattern (verbatim sentences + close-paraphrase paragraphs). The audience-blind Stage 2 protects against this; Path B preemptive policy must hold (do NOT open Ch 5 as source text in Stage 2).
- **(b) Apparatus tripwire risk applies.** Ch 5 uses internal apparatus terms (Restitution Bond / Foreclosure Bond definitions, possible cluster-γ-class jargon, accountability-mechanism schematics) that Boston Review's institutional/measurement-frame general readership does not tolerate. The Stage 1 brief's apparatus exclusion list must hold through Stage 2.
- **(c) No strong iterated control exists.** Neither the BR pitch nor the BR essay has been drafted before. There is no Version-C-style ratified control to iterate against. Audience-blind Stage 2 from a Stage 1 brief is the right shape.

All three clauses fire — apply v2.0, no exceptions.

**Required v2.0 actions for fresh sessions opening this workstream:**

1. **Build a Stage 1 brief before any prose drafting.** Save as `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_boston_review_essay_pre_draft_audience_structure_v1.0.0.md`. The brief must include: BR editorial-brain map (institutional/measurement frame; Submittable Essays-and-Book-Reviews stream; ~$300–$500 web-piece pay; "no previously published work" rule; "no op-eds, no unsolicited personal essays" rule); BR-specific 14-character audience pressure-test set adapted from the Aeon/Noema sets; structural anchors (Restitution Bond + Foreclosure Bond two-instrument decomposition as the spine); apparatus exclusion list (every Ch 5 internal term that the BR general readership wouldn't tolerate, marked for replacement-with-translation or omission); **canonical factual ground truth for any memoir-register material that lands in the essay** (per Amendment A — names, scenes, etymologies, numbers, scene-roles, direction-of-action of pivotal moments — even if memoir register is light in this essay). Do not skip the canonical-truth section: the Noema test produced 5+ factual drift points where a Stage 1 brief had only beats.
2. **Trigger a fresh-session Stage 2 audience-blind flow draft.** Path B preemptive policy: do NOT open Ch 5, prior pitches, or any other source text. Work only from the Stage 1 brief. Output: `publishing/essays/boston-review-accountability-gap/boston-review-essay-fresh-session-draft_<DATE>.md`.
3. **Run Stage 3 as three distinct passes (per Amendment B), in this order:**
   - **(a) Fact-check pass.** Audit the draft against the Stage 1 brief's canonical factual ground truth. Spot-fix factual drift by generating fresh prose from brief anchors — do NOT paste from Ch 5 (re-introduces Path B contamination).
   - **(b) Voice-polish pass.** Catch expository flatness, meta-commentary ("The plain definition is this:" / "That is the whole sentence." patterns), rule-of-three LLM tics, em-dash crutches, hedge phrases.
   - **(c) Audience-load pass.** Audit against the BR-specific audience pressure-test set. Save as `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_boston_review_essay_audience_load_v1.0.0.md`.

   Three distinct passes. Bundling is the failure mode v2.0 prohibits.
4. **Path B preemptive policy throughout.** No Ch 5 prose in front of any drafting session. Any sentence that reads as a Ch 5 echo at Stage 3 fact-check gets rewritten freshly, not pasted from Ch 5.

**Cross-references.** v2.0 memory: `feedback_audience_aware_drafting_discipline.md`. Noema Stage 3 verdict (per-test basis for Amendments A + B): `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md` §3.8 (factual-fidelity drift catalog) + §7 (materials handed to meta-verdict). Aeon Stage 3 verdict (per-test basis for Amendment C — confirms the discipline's regime is long-form-without-strong-control, not short-form-with-strong-control): `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_stage3_comparison_v1.0.0.md` §5–§6.

---

## Workstream scope

Draft Boston Review pitch (~1pp mini-prospectus) + full essay (~4,500w from Ch 5). BR's model: pitch first via Submittable; some pitches get accepted on the strength of the pitch alone, others request the full essay. Best practice: pitch first, then have essay drafted soon after.

## Current state

**Complete:**
- Source chapter (Ch 5 *The Accountability Gap*) — drafted, ~9,574 words; "Restitution and Foreclosure: Two Directions of Accountability" section is the natural argumentative spine
- Ch 5 Pistor + Christophers paragraph engagement landed on main (commit `d78872e`)
- AI disclosure template (generic variant)
- Author bio (medium ~85w version)

**Incomplete:**
- BR pitch (~1pp single-spaced)
- BR essay first draft (~4,500w)
- Cover letter (uses bio + AI disclosure)

## Next moves

1. **Draft pitch** (~1pp mini-prospectus, NOT a list of topics or questions) — institutional/measurement frame; "Restitution and Foreclosure" two-instrument decomposition (Restitution Bond + Foreclosure Bond) as the argumentative spine. Demonstrate the argument's substance + writing voice.
2. **Draft essay** (~4,500w) sourced from Ch 5 paraphrased per Path B no-overlap discipline — same arc / same ideas / different sentences.
3. **Cover letter** — brief intro + medium bio (`03_author-platform.md`) + AI disclosure (generic variant from template).
4. **Submit via Submittable** — `bostonreview.submittable.com/submit`, Essays and Book Reviews stream.
5. **Track receipt** — Submittable shows status changes; expect days-to-weeks for first signal.

## Files to read first

- `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` — source chapter (~9,574w)
- `publishing/essays/_shared/templates/ai-disclosure-paragraph.md` — generic variant for BR
- `publishing/book-proposal/03_author-platform.md` — medium bio paragraph (drafted 2026-05-09)
- `publishing/essays/_pipeline/cascade-plan_2026-05-06.md` — Boston Review timing + venue allocation
- `publishing/essays/_pipeline/rights-register.md` — confirm no Aeon/Noema rights conflict with Ch 5 frame

## Constraints / disciplines

- **Pitch form:** ~1pp single-spaced; mini-prospectus / précis with substantive argumentation, NOT a list of topics or questions
- **Essay length:** 2,500–5,000 words (min 2,000 hard floor)
- **BR exclusions:** does NOT publish op-eds; does NOT consider unsolicited personal essays; does NOT consider previously published work (including Substack/blogs) — Ch 1 vignette material doesn't fit BR; institutional/measurement frame is the right cut
- **Path B no-overlap:** no sentence reuse with Ch 5; same arc + same ideas + different sentences
- **Submission method:** Submittable (`bostonreview.submittable.com/submit` Essays and Book Reviews stream)
- **Pay (per BR's stated rates):** $300–$500 web pieces

## Cross-thread dependencies

- None blocking. Ch 5 is current; Pistor + Christophers engagement landed; no upstream blockers.

## Out of scope

- Aeon pitch / essay (separate workstream)
- Personal-narrative framing (use institutional/measurement instead — Ch 1 material doesn't fit BR)
- Atlantic Ideas / Phenomenal World pitch (different workstream + slot 3)
- Noema essay (separate workstream)

## Watch items

- BR's "no previously published work" rule — verify essay isn't accidentally overlapping with Aeon (different chapter, different frame, but worth a double-check).
- Pitch ≠ topics list. BR's stated guidance is explicit. Read 1–2 BR essays before drafting pitch to calibrate voice.

---

*End of Boston Review essay handoff. Update or supersede when state materially changes.*
