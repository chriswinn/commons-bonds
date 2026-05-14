# TA §5.5 Bidirectionality — Findings + Proposal Note (2026-05-13)

**Workstream:** Add §5.5 (Bidirectionality of the Apparatus) to Technical Appendix v2.0.0.
**Branch:** `claude/ta-section-5-5-bidirectionality-youthful-noyce-daa38c`
**Status:** PROPOSED — superseded by parallel-session work. NO further §5.5 commit recommended.
**Author ratification required on:** §5.4 B₁-direction moral-grounding coordination flag (see §6 below).

---

## §1. Originating need

Cross-reference verification surfaced that Ch 5's CSD-application paragraph (committed `ccaac20` 2026-05-13, [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:224](../../manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:224)) closes with:

> *"This is by design. The book demonstrates the framework forward; the backward application is structurally identical methodology, carried in formal articulation in the Technical Appendix (§5.5). Voices in the reparations-economics tradition — Darity, Mullen, Hamilton, Coates, Anderson, and the broader field — have been doing this work for years; the framework recognizes and defers to their work in identifying and pricing the variables."*

That paragraph is the prose-side promise §5.5 must keep: the apparatus's bidirectional reach must be formalized in TA §5.5.

The Ch 10 in-flight insertion paragraph (anticipated in the workstream prompt) does NOT exist yet in [Chapter_10_CommonBonds__Draft.md](../../manuscript/chapters/Chapter_10_CommonBonds__Draft.md) at session start. The operative cross-reference to §5.5 is in Ch 5, not Ch 10. The Ch 10 insertion-placement session (when it runs) is downstream of §5.5, not upstream.

---

## §2. Bidirectionality content inventory in TA §5 (at session-start view)

Before discovering the parallel-session work, the inventory of bidirectionality content scattered in TA §5 was:

| Where | Content carried | Bidirectionality named explicitly? |
|---|---|---|
| §5 intro (post-#19 lines ≈1183-1191) | Decomposition equation `total CS = (CSD − B₁) + (RCV − B₂)` IS the bidirectional partition. | No — presented as decomposition, not as bidirectionality claim. |
| §5.1.1 (B₁ Restitution Bond definition) | B₁ explicitly tagged "backward-looking sub-instrument." | Half — names B₁ direction. |
| §5.1.2 (B₂ Foreclosure Bond definition) | B₂ explicitly tagged "forward-looking sub-instrument." | Half — names B₂ direction. |
| §5.3 (Independence note) | Bidirectional cases enumerated (high-CSD-low-RCV; low-CSD-high-RCV; both). | Implicit — bidirectionality presupposed by independence-of-directions claim. |
| §5.4 (Intergenerational moral grounding) | Title explicitly scopes to "B₂ Foreclosure Bond direction." Parfit framing maps impersonal-outcomes → B₂; person-affecting reading mapped implicitly to B₁ but unstated. | No — section is B₂-only. |

**Gap (at session-start view):** §5 did not name "the apparatus is bidirectional" as a structural property; did not articulate how each apparatus component (Four Gates §7, Three Ways of Counting §3, central equation) runs in both directions; did not specify domain-of-applicability where the symmetry is clean vs requires care.

---

## §3. (A) vs (B) approach decision — ratified before parallel-session discovery

Two approaches surfaced and decision ratified by author:

- **(A) — Add §5.5 as fresh consolidating subsection.** Keep §5.1-§5.4 unchanged; insert §5.5 between §5.4 and §6. ~300-500w synthesizing bidirectionality structural claim + apparatus-component articulation + domain-of-applicability.
- **(B) — Restructure §5 with bidirectionality as the spine.** Repromote bidirectionality from implicit-in-decomposition to the named framing of §5; rewrites the section's frame; creates downstream ripples.

**Author ratification:** Approach (A) — ratified verbatim in chat as "ratify as recommended" 2026-05-13.

This ratification stands as the canonical answer for the (A) vs (B) decision, even though execution is now moot per §4 below.

---

## §4. Parallel-session discovery — §5.5 already landed on main

After branch creation from origin/main and TOC-annotation edit attempt, the session discovered that origin/main had advanced 5 commits during the read-through phase. The relevant commits (chronologically):

| Commit | Title | What it did |
|---|---|---|
| `be334f5` | Tech Appendix Approach B — bidirectional reach articulation + Darity MI-1/MI-2 | **Added §5.5** at TA HTML lines 1318-1373. |
| `8ed36ac` | Tech Appendix Approach B follow-up — §1.7 ↔ §5.5 cross-reference + §17.5 bidirectional preservation | Added cross-references from §1.7 (line 470: forward-pricing-shorthand vs full-bidirectional-form note) and added §17.5 "Corollary — bidirectional preservation" cross-referencing §5.5. |
| `02b264d` | Pass 1 findings doc — Amendment 2026-05-13 (Approach B ratification + status update) | Pass 1 math/proof audit amendment. "Approach B" in this commit message refers to F-18's proof-fix Approach B (tighten hypothesis (b) from r_∞ = 0 to ∫r ds < ∞), **NOT** to this session's (A) vs (B) for §5.5. |
| `5a7ecbc` / `3452de5` / `c605f23` / `86382ce` | WP#10 scaffolding cleanup §§2-17 + final TOC pass | TOC annotation for §5 updated (line 206) to mention bidirectional application: *"Restitution Bond + Foreclosure Bond sub-instrument definitions; Darity-Mullen reparations-typology positioning for B₁; independence note; Parfit (1984) intergenerational moral grounding for B₂; bidirectional application of the framework apparatus (forward Book 1 scope; backward subsequent-work scope; Three Ways applied in reverse for legacy-effect pricing)."* |

**The work this session was scoped to do has already landed on main.**

---

## §5. Assessment — existing §5.5 vs Ch 5:224 promise and approach-(A) plan

The existing §5.5 (TA HTML 1318-1373) is **substantively complete** against the Ch 5:224 promise and against the approach-(A) draft plan. Item-by-item assessment:

| Approach-(A) plan element | Existing §5.5 delivers? | Notes |
|---|---|---|
| Bidirectionality as a structural property | ✅ Yes | First paragraph: *"The framework's apparatus — Commons Inversion Test (§6), Four Gates admission (§7), and Three Ways of Counting triangulation (§3) — is direction-agnostic in its formal statement. Theorem 10.3 (Abundance Masking) operates whether the abundance being stripped is forward-projected or backward-realized."* |
| Bidirectional form of central equation | ✅ Yes | `total CS = (CSD − B₁) + (RCV − B₂)` with both summands explicated; high-level `CS = RCV − B` framed as forward-pricing shorthand exact when (CSD − B₁) ≈ 0 or in pure-forward analysis. |
| Apparatus component-by-component (Four Gates §7) | ✅ Yes | "The Four Gates filter both directions of cost claim identically." |
| Apparatus component-by-component (Three Ways of Counting §3) | ✅ Yes — and more thoroughly than my draft | Method 1 / Method 2 / Method 3 forward/backward mapping explicit, with named exemplars: Norway GPFG (Method 2 forward); Darity & Mullen 2020 + Holocaust reparations + 1988 Civil Liberties Act + Black Lung Trust Fund + South African TRC (Method 2 backward); etc. |
| Domain of applicability — epistemic asymmetry | ⚠ Partial | Forward/backward scope discipline is established (Book 1 forward empirical; backward subsequent-work) but the *epistemic asymmetry* point (backward often empirically anchored; forward requires modeling) is implicit rather than named. Acceptable; not a blocker. |
| Domain of applicability — coercion vector boundary | ✅ Yes | Bulleted ul entry: *"The coercion vector itself. Slavery and forced-labor cases are structurally distinct from the framework's information-asymmetry analytical case-class… The framework names the variable and extends to coerced-extraction cases through the legacy-effects pathway above; it does not claim to have priced the coercion vector directly."* |
| Darity & Mullen lineage + reparations-economics positioning | ✅ Yes | Bulleted ul entries on racial wealth gap + longevity gap as legacy-effect pricing, with Darity & Mullen 2020 named as primary contemporary development. |
| Cross-references to §1.7, §3, §6, §7, §12, §1.10, Ch 6 | ✅ Yes | All present. |
| Coordination flag: §5.4 is B₂-only; B₁-direction moral-grounding companion methodologically needed | ⚠ NOT FLAGGED | This is the one residual item the existing §5.5 does not explicitly carry. See §6 below. |

**Aggregate verdict:** the existing §5.5 satisfies the Ch 5:224 promise. The one residual coordination flag (§5.4 B₂-only / B₁-companion) is logged for future-session ratification but is NOT a blocker for downstream Sandy-send or Ch 10 insertion work.

---

## §6. Residual coordination flag — §5.4 B₁-direction moral-grounding companion

**Observation.** §5.4 is currently titled "Intergenerational moral grounding (Parfit 1984; B₂ Foreclosure Bond direction)" and scoped explicitly to the forward direction. The Parfit framing within §5.4 maps impersonal-outcomes evaluation → B₂ and person-affecting evaluation → B₁, so the B₁-direction moral grounding is *implicit* in the §5.4 framing but is not given its own section, paragraph, or named treatment.

The existing §5.5 cites the reparations-economics tradition (Darity, Mullen, Hamilton, Coates, Anderson) as the canonical contemporary developers of backward-direction methodology — which is the operational answer to "what is the framework's B₁-direction moral grounding?" But §5.5 does not explicitly flag that §5.4's B₂-only scoping has a B₁-direction companion to develop, and does not propose where that development should live (a §5.4 expansion? a new §5.6? a stand-alone subsection in §5.5 itself?).

**Recommendation (for author ratification, NOT for this session's execution):**

Option (i) — **No-action.** §5.5's depth of treatment of Darity & Mullen and the reparations-economics tradition is operationally sufficient. The §5.4 B₂-only scoping is a defensible scope-discipline choice; expanding it later is optional rather than required.

Option (ii) — **Expand §5.4 in a subsequent session.** Rename §5.4 to "Intergenerational moral grounding (Parfit 1984; B₁ + B₂ directions)" and add a paragraph mapping the Parfit person-affecting reading to backward-direction realized harm, positioned in dialogue with Darity & Mullen + the reparations-economics tradition. Adds ~150-300 words; preserves §5.4's structure.

Option (iii) — **Add §5.6 (B₁ moral grounding) as a sibling to §5.4 and §5.5.** Cleanest separation of concerns: §5.4 = B₂ moral grounding (Parfit-IV impersonal-outcomes); §5.5 = bidirectionality apparatus; §5.6 = B₁ moral grounding (Parfit-IV person-affecting × Darity-Mullen). Adds ~300-500 words; expands §5 by one subsection.

**Recommended default:** Option (i) — no-action. The existing §5.5's treatment of the reparations-economics tradition (with named contemporary developers + lineage of historical exemplars) operationally delivers what a B₁-direction moral grounding would carry. If the author later judges that §5.4's explicit B₂-only scoping creates a structural imbalance, Option (ii) or (iii) can fire as a small follow-up workstream.

**Not in scope for this session.** This session does not execute any of (i), (ii), (iii). Future-session ratification only.

---

## §7. Cross-reference impact analysis (for downstream sessions)

For sessions consuming §5.5 downstream of this finding:

| Downstream artifact | Cross-reference status to §5.5 | Action needed |
|---|---|---|
| Ch 5 line 224 `(§5.5)` cross-reference | ✅ Resolves cleanly. §5.5 exists; substantively delivers what the prose-side promise made. | None. |
| Ch 6 (Three Ways of Counting canonical) | ⚠ No forward-reference to §5.5 currently. Ch 6 already references §7 (Four Gates) at [Chapter__6_ThreeWaysofCounting__Draft.md:263](../../manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:263). | Flag for Ch 6 Stage-3 audit / Phase A audit: consider adding a forward-reference to §5.5 alongside the §7 reference (parallel-formal-articulation pointer for the bidirectionality structural claim). Optional, not a blocker. |
| Ch 10 (in-flight insertion paragraph) | N/A — paragraph not yet drafted. | Ch 10 insertion-placement session: §5.5 is available; draft Ch 10 paragraph wording such that its "the same apparatus runs in reverse" claim points at TA §5.5 for formal articulation. |
| TA TOC annotation for §5 | ✅ Already updated. | None. |
| Glossary v4 (queued rebuild) | ⚠ Bidirectionality-of-apparatus is a candidate glossary entry. | Flag for Glossary v4 rebuild session (workstream #7 dependency). |
| TA Pass 1 math-audit (commit `02b264d` Amendment 2026-05-13) | N/A — different scope (F-18 + F-19 findings on Theorem 10.4 + §16.3 SCS formula). | None. |
| Sandy send package | ✅ §5.5 exists; Ch 5 + Ch 6 + TA can be packaged consistently. | None. |

---

## §8. Workstream finding — process-level

The parallel-session workstream (commits `be334f5` + `8ed36ac`) was running approximately concurrently with this session's read-through. The work landed before this session reached the apply-edit phase. This is a friction signal in the parallel-session coordination layer, not a process failure — both sessions independently identified the same gap (§5.5 missing) and converged on similar consolidating-subsection structures (consistent with approach (A)).

**Coordination observation.** Per Working Principle #9 (worktree-isolation + session-end fast-forward to main), the discipline correctly handled the convergence: both sessions branched from origin/main; the parallel session merged first; this session's read-through caught the change before duplicate work landed. The discipline worked as designed.

**Lesson worth saving (TBD by author):** when a workstream is announced for a small additive change to a heavily-trafficked file (e.g., TA HTML), a quick `git log --since="<recent date>" --oneline -- <file>` check during the surface-decision phase would catch concurrent work before approach decisions are surfaced. Not a hard rule — the existing discipline caught the convergence — but a future-session efficiency knob.

---

## §9. Verdict + deliverables

**Initial verdict (before author enhancement request).** §5.5 substantively complete. The originating Ch 5:224 promise satisfied. No further §5.5 commit recommended; this session did NOT produce a duplicate §5.5 draft.

**Author follow-up request (2026-05-13, same session).** Author asked: *"add any additional value that you can to what the parallel session wrote, can you update section 5.5 to make it better?"* — explicit request to extend the parallel-session §5.5 with value-adds identified during the assessment in §5 + §6 above.

**Enhancements applied (this session, second commit).** Four surgical additions landed against the parallel-session §5.5:

| # | Addition | Placement | Source of value-add |
|---|---|---|---|
| 1 | **Four Gates direction-agnosticism (gate-by-gate)** strong-tagged paragraph | After Backward application paragraph, before Total CS decomposed | §5 assessment table flagged "Four Gates: single sentence" in existing §5.5; new paragraph articulates Gate 1 (CIT scarcity-grounding), Gate 2 (Units), Gate 3 (Boundedness — the operational asymmetry: backward integration bounded by construction at analysis time; Gate 3 trivially satisfied for backward Cᵢ), Gate 4 (Independence) individually. Also removes the now-redundant single-sentence Four Gates claim from inside the Backward application paragraph. |
| 2 | **Epistemic asymmetry across directions** strong-tagged paragraph | After Four Gates paragraph, before Total CS decomposed | §5 assessment flagged "Domain of applicability — epistemic asymmetry: ⚠ Partial" in existing §5.5; new paragraph names epistemic asymmetry explicitly as a structural feature, distinguishes backward Cᵢ (empirically anchored: longevity-gap years, wealth-gap dollars, production-record extraction-portfolio) from forward Cᵢ (modeled counterfactual: U, E, S(t) trajectory), and articulates the different sensitivity-analysis disciplines each direction is subject to. |
| 3 | **Sibling-section structure (§5.3 / §5.5)** strong-tagged paragraph | After Example backward variables bulleted list, before Book 1 scope discipline | §5 assessment flagged no §5.3 cross-reference; new paragraph frames §5.3 (structural independence) and §5.5 (structural symmetry) as sibling consequences of the B = B₁ + B₂ decomposition. |
| 4 | **Coordination note (B₁-direction moral grounding)** strong-tagged paragraph | After Book 1 scope discipline paragraph, before closing </section> | §6 above flagged the §5.4 B₂-only / B₁-companion question with Options (i)/(ii)/(iii); new in-section coordination note moves the flag from this findings doc *into §5.5 itself*, logging the question for subsequent revision without prescribing the resolution. This is Option (i) "no-action / log in-section" applied as the operational answer; Options (ii) §5.4 expansion and (iii) new §5.6 sibling remain available for future-session ratification if the in-section logging proves insufficient. |

**Aggregate verdict after enhancements.** §5.5 now carries: (a) bidirectionality structural claim; (b) Forward / Backward / Total-CS framing; (c) gate-by-gate Four Gates articulation; (d) explicitly-named epistemic asymmetry; (e) Three Ways of Counting forward/backward mapping with named exemplars; (f) example backward variables (racial wealth gap, longevity gap, coercion vector, Indigenous etc.); (g) sibling-section structure framing §5.3 ↔ §5.5; (h) Book 1 scope discipline; (i) in-section coordination note for the §5.4 B₁-companion question.

**Deliverables produced by this session (final):**
- This findings note (commit `013abd4`): `tools/rigor-passes/ta_section_5_5_bidirectionality_proposal_2026-05-13.md` (PROPOSED).
- §5.5 enhancements applied to `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (this commit): four surgical additions per table above (PROPOSED).

**Author action requested (residual, post-enhancements):**
- Ratify the in-section B₁-companion coordination note as the operational resolution (Option (i) "log in-section"). If preferred, ratify Option (ii) §5.4 expansion or Option (iii) new §5.6 sibling for a follow-up session.
- Optional: ratify the four §5.5 enhancements en bloc, or call out any of the four for revision/revert.

---

*End of findings note. PROPOSED, awaits ratification.*
