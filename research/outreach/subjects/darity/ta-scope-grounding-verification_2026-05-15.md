# TA scope/grounding verification — Ch 6 MI-3 + SI-3 mirrors

**Verified:** 2026-05-15 by Claude per author direction.
**Status:** CLEAN — both mirrors present in `TechnicalAppendix_v2.0.0.html` with `(Darity 2026)` attribution. No targeted-paragraph additions needed; no bundle into Sandy outreach required.
**Branch:** `claude/schedule-call-val-david-jjQvD` → auto-merged to main per workflow default (author-ratified verification task; result is a no-op log close).

---

## Task

Per `tools/workstream-handoffs/archive/pm-session-handoff_2026-05-13.md` §2 (Wed May 13 row) + §9 (This week by Sun May 17):

> Optional ~30min TA scope/grounding verification session — confirm Technical Appendix §1.10 names heterogeneous-stakeholder commons (MI-3) as in-scope alongside the coercion-vector legacy-effects pathway (MI-2 already cited), and confirm wherever the TA grounds the valuation methodology philosophically that it cites Sen's capability framework (SI-3) as Ch 6 line 250 now does. If both present: log + close. If either missing: small targeted paragraph addition; counts as "minor revisions since send" item Sandy should be told about when the Q0 note goes out (one combined Sandy outreach rather than two).

The proactive Q0 note already shipped 2026-05-15 (citations email); this verification trails it. If clean → no further Sandy outreach. If gap surfaced → would have required a "minor revisions since send" note. Result: clean.

---

## Findings

### Mirror 1 — MI-3 (heterogeneous-stakeholder commons / stratification economics)

- **Ch 6 anchor:** `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:262`. Names the second break-point Ostrom's framework does not address; connects to *stratification economics (Darity, Hamilton, and collaborators)*. No inline `(Darity 2026)` citation in prose yet — pending Sandy Q0 ratification per the proactive citations email; not a defect of this verification scope.
- **TA mirror:** `core/technical-appendix/TechnicalAppendix_v2.0.0.html:604`. §1.10 second scope-of-applicability boundary paragraph. Quoted verbatim of the load-bearing sentence: *"This break-point connects the framework to the analytical apparatus of stratification economics (Darity, Hamilton, and collaborators), which analyzes structural-extraction operating through hierarchical group-divisions of race, class, and ethnicity (Darity 2026)."*
- **Attribution discipline:** `(Darity 2026)` present inline in the TA paragraph. Bibliographic entry confirmed at TA line 7792 (Chicago author-date interview form, post-`f6d6281` cite-form swap).
- **Verdict:** ✓ PRESENT + ATTRIBUTED.

### Mirror 2 — SI-3 (Sen capability grounding for valuation methodology)

- **Ch 6 anchor:** `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:250`. Sen paired with Parfit as philosophical grounding; Parfit grounds the *standing* question, Sen grounds the *valuation* question; RCV described in Sen's capability-set vocabulary. No inline `(Darity 2026)` citation in prose yet — same pending-Sandy-ratification status as MI-3.
- **TA mirror:** `core/technical-appendix/TechnicalAppendix_v2.0.0.html:1342`. §5.4 (Intergenerational moral grounding). Quoted verbatim of the load-bearing sentence: *"The Parfit / Sen pairing — Parfit grounding the standing, Sen grounding the valuation — is what makes the framework's intergenerational-pricing claim defensible across the moral-philosophy and welfare-economics traditions simultaneously rather than within only one (Darity 2026)."*
- **Attribution discipline:** `(Darity 2026)` present inline. Same bibliographic anchor as MI-3.
- **Verdict:** ✓ PRESENT + ATTRIBUTED.

---

## What this verification did NOT cover (intentionally)

- **Ch 6 prose inline-citation propagation.** Pending Sandy Q0 ratification per `research/outreach/subjects/darity/proactive-q0-citation-questions_2026-05-15.md` (commit `a5ef643`). When Sandy ratifies citation language for the three flagged paragraphs (Ch 5 line 220 already carries `(informed by Darity 2026)`; Ch 6 line 124 + Ch 6 line 262 + Ch 6 line 250 await), inline-citation lands in Ch 6 prose at that point.
- **Other TA scope/grounding sections.** This verification was scoped to MI-3 + SI-3 mirrors only; broader TA audit lives in §7 Apparatus Phase A (per PM handoff) and is gated on per-chapter #20 voice-polish + audience-load completion.
- **Cite-form consistency across all uses of Darity 2026 in the TA.** Cite-form swap landed in commit `f6d6281`; spot-checks during this verification surfaced no inconsistencies but a full grep-sweep of all `(Darity 202` matches is a separate sub-task if Sandy redlines any phrasing in his reply.

---

## Pipeline-tracker / handoff updates

- `tools/workstream-handoffs/archive/pm-session-handoff_2026-05-13.md` §9 "This week (by Sun May 17)" — TA verification row marked complete with cross-reference to this note.
- No further Sandy outreach generated (verification clean; no bundle needed).

---

## Cross-references

- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` §1.10 (line 604) + §5.4 (line 1342) + §18 bibliography (line 7792)
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md` line 250 + line 262
- `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` line 220 (`(informed by Darity 2026)` already present)
- `research/outreach/subjects/darity/proactive-q0-citation-questions_2026-05-15.md` — the proactive Q0 note Sandy is responding to
- `research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md` — MI-3 + SI-3 synthesis items
- Commits: `6d28f4e` (TA MI-3 + SI-3 incorporations) + `f6d6281` (cite-form swap) + `e6ddf92` (with-citations derivatives regen)
