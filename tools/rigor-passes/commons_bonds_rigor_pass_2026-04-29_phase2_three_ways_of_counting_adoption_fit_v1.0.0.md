# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: Three Ways of Counting Post-Rename Adoption-Fit Verification

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — adoption-fit verification per author direction 2026-04-29 (reverse-priority Phase 2 sweep). Phase 1 §10 #5 flagged this as "minor; can defer until pre-submission review." Tests applied: surface-by-surface adoption check (terms_index + glossary + chapter prose + chapter title + Tech Appendix sections + GuidanceDoc); preserved-form discipline ("the triangulated three-method range" inline result); supersession-record discipline; cross-reference adoption; legitimate-historical-reference vs adoption-gap distinction.

**Scope:** Phase 2 adoption-fit audit on the **Three Ways of Counting** (TWoC) Ring-2 methodology name post the 2026-04-28 rename from "Triangulated RCV Estimation" (Insight #31 RATIFIED). Phase 1 §10 #5 flagged: *"Three Ways of Counting — post-rename adoption-fit verification (minor; can defer until pre-submission review)."*

**Status:** **RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify (Option A clean drop).** Tech Appendix HTML edit timing (apply 2-line edit to v1.0.0 now vs batch into Phase 3 v2.0.0 rebuild) — pending author choice on §6 Q2 (same open question as Insights #35 + #38 + #40 + #47). Insight #48 closed-ratified entry added to `alignment/commons_bonds_open_insights_v1.0.0.md`.

**Author:** Chris Winn

**Recommended verdict (preview):** **PASS conditional on one minor adoption-gap fix** at Tech Appendix v1.0.0 §3 section title (TOC + section header inversion). All other publisher-facing surfaces (chapter title, chapter prose, glossary v3, terms_index, GuidanceDoc, Block 4 validation, Tech Appendix Block 4 chapters) cleanly adopt TWoC as primary methodology name with "the triangulated three-method range" preserved as inline result phrasing per Option B verdict.

The single adoption gap is structural-but-minor: Tech Appendix v1.0.0 lines 225 (TOC) + 678 (§3 section header) read *"§3. RCV Quantification — Triangulated Estimation (Three Ways of Counting)"* — inverting the Option B verdict's primary/parenthetical hierarchy. Repair is a 2-line edit; recommended replacement: *"§3. RCV Quantification — Three Ways of Counting"*.

The audit's scope-honesty conclusion: this candidate was correctly classified as "minor" at Phase 1 §10. The rename has propagated cleanly through the framework's high-leverage publisher-facing surfaces; the one residual gap is a Tech Appendix section-title inversion that affects ~2 lines of HTML. No deeper structural concerns.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

Surface-by-surface adoption check across all framework surfaces touching Three Ways of Counting / Triangulated RCV Estimation:

1. **Chapter 6 chapter title** (publisher-facing top surface).
2. **Chapter 6 prose** (chapter body — descriptive usage of "Triangulation" as concept-noun + preserved-form "the triangulated three-method range" as inline result phrasing).
3. **Chapter 6 GuidanceDoc** (writing-guidance scaffolding).
4. **terms_index entry** (canonical term record — primary entry name + supersession record discipline).
5. **Glossary v3 entry** (publisher-facing glossary — term name + cross-references).
6. **Tech Appendix v1.0.0 §3 section title** (TOC line 225 + section header line 678) — high-leverage academic-publisher-facing surface.
7. **Tech Appendix v1.0.0 Block 4 + worked-example sections** (lines 1669, 3478, 3492, 3934, 3952, 4350, 4380) — body-text usage.
8. **Block 4 validation document** (`core/technical-appendix/block4_validation_2026-04-25.md`) — methodological scaffolding doc.
9. **Bibliography references** (rigor-pass file-name references using historical name — legitimate-historical, not adoption-gap).
10. **Older rigor passes** (file-internal historical references — legitimate-historical, not adoption-gap).

### §1.2 Phase 2 outcomes

| Surface | Adoption status | Note |
|---|---|---|
| Ch 6 chapter title | ✓ ADOPTED | "Three Ways of Counting" — was always TWoC; drove rename direction |
| Ch 6 chapter prose | ✓ ADOPTED | "Three Ways" 3x in headings; "Triangulation" 1x as concept-noun (legitimate); "the triangulated three-method range" preserved per Option B |
| Ch 6 GuidanceDoc | ✓ ADOPTED | "Three Ways of Counting" used consistently |
| terms_index entry | ✓ ADOPTED | Primary entry titled "Three Ways of Counting (formerly 'Triangulated RCV Estimation'; renamed 2026-04-28)"; full supersession record |
| Glossary v3 | ✓ ADOPTED | Term entry titled "Three Ways of Counting"; inline preserved-form "the triangulated three-method range"; cross-reference listings clean |
| **Tech Appendix v1.0.0 §3 TOC + section header** | **△ ADOPTION GAP** | Lines 225 + 678 read *"Triangulated Estimation (Three Ways of Counting)"* — inverts Option B primary/parenthetical hierarchy |
| Tech Appendix Block 4 sections + body | ✓ ADOPTED | "Three Ways of Counting executed" / "triangulated across Three Ways" / "triangulation-confirmed" — clean |
| Block 4 validation doc | ✓ ADOPTED | Headers + body use TWoC primary; "triangulated" as descriptor only |
| Bibliography refs | ✓ LEGITIMATE-HISTORICAL | "Triangulated RCV Estimation rigor pass (commit 4f48c48)" — refers to historical rigor-pass file by its 2026-04-24 name; correct disciplinary practice |
| Older rigor passes | ✓ LEGITIMATE-HISTORICAL | Internal references to "Triangulated RCV Estimation" predate rename; correct |

**Aggregate verdict: PASS conditional on one Tech Appendix §3 section-title fix.**

The rename has propagated cleanly through 9 of 10 audited surfaces. The one gap (Tech Appendix v1.0.0 §3 section title) is a 2-line HTML edit. No deeper structural concerns; no chapter-prose regressions; no terms_index inconsistencies; no glossary mismatches.

### §1.3 One concrete adoption-fix

**ENHANCEMENT: Tech Appendix v1.0.0 §3 section-title inversion fix.**

Current (lines 225 + 678):

> §3. RCV Quantification — Triangulated Estimation (Three Ways of Counting)

Recommended replacement:

> §3. RCV Quantification — Three Ways of Counting

Or alternative if "triangulated" descriptor is desired in section title:

> §3. RCV Quantification — Three Ways of Counting (triangulated three-method range)

The first option (drop "Triangulated Estimation" entirely) is cleanest and most aligned with Option B verdict. The second option preserves the "triangulated" descriptor inline, matching the chapter-title style used throughout the framework. **Recommended:** first option (clean drop) — Option B says drop "Triangulated RCV Estimation" as primary, and section titles should follow that discipline.

Internal section reference at line 684 ("old §B 'The RCV Model' (B.1 Core Formula + B.2 IPG) merged with partial integration §3 (Three Ways of Counting; Methods 1+2+3 + triangulation logic)") is already clean and does not need change — it references the §3 section by its content + already names TWoC primary.

### §1.4 Why this verdict pattern

The rename was straightforward (Insight #31 Option B: drop redundant formal name; promote pedagogical alias) and the framework's ratified-decision discipline applied automatically across most surfaces because:

- **The chapter title was already TWoC** — driving the rename direction means most downstream references organically aligned.
- **The "triangulated three-method range" inline phrasing was explicitly preserved** as preserved-form — meaning legitimate uses of "triangulated" as descriptor remain correct.
- **The supersession-record discipline** (Working Principle #1 vocabulary parsimony + retirement-trace discipline) ensured terms_index + glossary v3 entries cleanly transitioned with proper provenance.

The one surface that didn't auto-update is the Tech Appendix v1.0.0 §3 section title, which was structured as "old [section name] (new [section name])" pairing during a prior consolidation pass and never got the post-rename inversion fix. This is a stale-formatting artifact, not a substantive disagreement with the rename.

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 1 full framework audit §10 #5](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"5. Three Ways of Counting — post-rename adoption-fit verification (minor; can defer until pre-submission review)"*

[Triangulated RCV Estimation naming review §11 verdict](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_triangulated_rcv_estimation_naming_review_v1.0.0.md) — RATIFIED Insight #31:

> *"Option B verdict — drop 'Triangulated RCV Estimation' as separate Ring-2 term; promote 'Three Ways of Counting' from pedagogical-alias to primary methodology name; preserve 'the triangulated three-method range' as inline result description."*

Phase 2 (this rigor pass) executes the screening-recommended adoption-fit verification.

### §2.2 What this audit produces

For pass/fail academic-rigor gate at top-tier journals + academic-trade hybrid presses, the post-rename adoption must meet the following standards:

- All publisher-facing surfaces use TWoC as primary methodology name.
- The preserved-form "triangulated three-method range" appears only as inline result phrasing, not as primary methodology name.
- Supersession record is discoverable from any entry-point (terms_index; glossary; rigor-pass cross-references).
- Historical references (in rigor passes / bibliography / older docs) are legitimate provenance traces, not stranded usage that would confuse a reader.

This audit produces:
1. Surface-by-surface adoption verdict.
2. Distinction between adoption-gap (needs fix) vs legitimate-historical (correct as-is) usage.
3. Concrete fix recommendation for the one identified adoption gap.

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic rigor for vocabulary discipline including post-rename adoption-fit. This audit applies the same standard to the TWoC rename that prior rename audits applied to other Ring-1 / Ring-2 retirements (Triangulated RCV Estimation → TWoC; existential substitutability gap; Severed Cost; etc.).

### §2.4 What this pass does NOT cover

- **Re-litigation of Option B verdict** — Insight #31 RATIFIED 2026-04-28; this audit verifies adoption, not the rename decision itself.
- **Method 1 / 2 / 3 sub-method audits** — separate rigor passes (e.g., commit `1c8e4dd` Three Ways + RCV Formal-Model rigor pass) covered the sub-methods; not in scope.
- **Block 4 numerical validation** — separate work item per `block4_validation_2026-04-25.md`; not adoption-fit territory.
- **Tech Appendix HTML edit timing** — same open question as Insights #35 + #38 + #40 + Phase 2 #8 + Phase 2 #7: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild.
- **Cross-coordination with theorem session** — Three Ways of Counting does not appear in Theorems E.1/E.3/E.4/E.5/Renewable Imperative; clean separation.

---

## §3. Methodology

### §3.1 Adoption-fit audit framework

For each surface, the audit (a) reads current state via grep + targeted Read; (b) classifies usage as ADOPTED (TWoC primary) / ADOPTION-GAP (TWoC missing or inverted) / LEGITIMATE-HISTORICAL (correct provenance trace); (c) flags concrete repair work where ADOPTION-GAP.

### §3.2 Surfaces tested

- Publisher-facing top-tier: Ch 6 chapter title; glossary v3; terms_index; Tech Appendix v1.0.0 §3 section title.
- Publisher-facing body: Ch 6 prose; Tech Appendix Block 4 sections + worked examples; Tech Appendix non-§3 cross-references.
- Methodological scaffolding: Ch 6 GuidanceDoc; Block 4 validation document; sensitivity analysis docs.
- Provenance scaffolding: bibliography references; older rigor pass internal references; supersession records.

### §3.3 Distinction discipline (ADOPTED vs LEGITIMATE-HISTORICAL vs ADOPTION-GAP)

- **ADOPTED:** TWoC is primary methodology name; "triangulated" appears only as descriptor or preserved-form phrasing.
- **LEGITIMATE-HISTORICAL:** "Triangulated RCV Estimation" appears in:
  - Bibliography references citing the 2026-04-24 rigor pass file by its historical name.
  - Internal references in older rigor passes that predate the 2026-04-28 rename.
  - Supersession records (terms_index + glossary) explicitly noting the rename as provenance.
  - Insight #31 ratification record itself.
- **ADOPTION-GAP:** "Triangulated RCV Estimation" or "Triangulated Estimation" appears as a primary methodology name in current publisher-facing or framework-canonical content, in ways that would confuse a reader by misrepresenting the post-rename state.

### §3.4 What the audit does NOT do

- Does NOT re-evaluate the Option B verdict (Insight #31 RATIFIED).
- Does NOT audit Method 1 / 2 / 3 individual sub-methodologies.
- Does NOT extend to other rename audits (separate adoption-fit checks if needed for existential substitutability gap, Severed Cost, etc.).

---

## §4. Surface-by-surface audit

### §4.1 Chapter 6 chapter title

**Current state:** "Chapter 6 — Three Ways of Counting" (Chapter__6_ThreeWaysofCounting__Draft.html lines 7, 116, 170).

**Verdict:** ✓ **ADOPTED.** TWoC is primary; was always TWoC (chapter title drove the rename direction); zero "Triangulated" instances in chapter title or section headers.

**Repair:** None.

### §4.2 Chapter 6 chapter prose

**Current state:**
- "Three Ways" 3x (in headings/title repetitions per chapter draft).
- "Triangulation" 1x (line 384) — *"Triangulation is the standard scientific-method response to estimation under uncertainty: produce three independent estimates from three independent epistemological angles, report the convergence range, treat divergence as informative rather than as failure."* — used as **concept-noun** describing the methodological practice (legitimate per Option B preserved-form discipline).
- "the triangulated three-method range" 1x (line 534) — *"The Block 4 validation work cross-confirms the case-file canonical forms at the lower end of the triangulated three-method range."* — used as **inline result phrasing** (legitimate per Option B preserved-form discipline).

**Verdict:** ✓ **ADOPTED.** Both "Triangulation" (concept-noun) and "the triangulated three-method range" (inline result phrasing) are explicitly preserved-form usages per Option B. Neither functions as a primary methodology name. The chapter prose cleanly distinguishes "Three Ways of Counting" (the methodology) from "triangulation" (what the methodology does as a practice).

**Repair:** None.

### §4.3 Chapter 6 GuidanceDoc

**Current state:** `manuscript/chapters/Chapter__6___GuidanceDoc.md` — uses "Three Ways of Counting" or "THREE WAYS OF COUNTING" consistently in 3+ places (lines 9, 23, 128). No "Triangulated" appearances.

**Verdict:** ✓ **ADOPTED.**

**Repair:** None.

### §4.4 terms_index entry

**Current state:** `core/terms/terms_index.md` line 1930 onwards:

> **### Three Ways of Counting (formerly "Triangulated RCV Estimation"; renamed 2026-04-28)**
>
> **Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — methodology unchanged; renamed 2026-04-28 by Chris Winn from "Triangulated RCV Estimation" to "Three Ways of Counting" per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_triangulated_rcv_estimation_naming_review_v1.0.0.md` Option B verdict — drop redundant formal name; promote pedagogical alias to primary methodology name; preserve "the triangulated three-method range" as inline result description; vocabulary footprint reduces by one Ring-2 term per Working Principle #1 parsimony).
>
> **Supersession record:** "Triangulated RCV Estimation" (proper-noun coined 2026-04-24) RETIRED 2026-04-28 as redundant with "Three Ways of Counting" pedagogical name. Methodology, three sub-methods (Replacement Cost / Revealed Preference / Scarcity-Adjusted Option Value), convergence/divergence diagnostic, reporting discipline all preserved unchanged. Tier verdict reaffirmed at Ring 2 / Tier D under "Three Ways of Counting" (chapter title pattern-matches accessible academic-trade convention per Mazzucato / Raworth / Anderson lineage).

**Verdict:** ✓ **ADOPTED with exemplary supersession-record discipline.** Primary entry titled TWoC; full provenance trace; rename rationale recorded; methodology preservation explicit.

**Repair:** None.

### §4.5 Glossary v3 entry

**Current state:** `core/glossary/archive/commons_bonds_updated_glossary_v3.html`:
- Line 235-236: term entry titled "Three Ways of Counting" with definition that includes inline preserved-form *"described inline as 'the triangulated three-method range.'"*
- Line 288: cross-reference under RCV — *"forward-looking; resource permanent-foreclosure; triangulated estimation; pairs with B2 (Foreclosure Bond)"* — uses "triangulated estimation" descriptively (legitimate).
- Line 392: index entry — *"**Three Ways of Counting** — Ring 2 estimation methodology with three sub-methods (renamed 2026-04-28 from 'Triangulated RCV Estimation'; methodology unchanged)."*

**Verdict:** ✓ **ADOPTED.** Term entry primary; preserved-form inline; cross-references descriptive; index entry includes rename note for reader-discoverability.

**Repair:** None.

### §4.6 Tech Appendix v1.0.0 §3 section title — ADOPTION GAP

**Current state:** `core/technical-appendix/TechnicalAppendix_v1.0.0.html`:

- **Line 225 (TOC):** *"§3. RCV Quantification — Triangulated Estimation (Three Ways of Counting)"*
- **Line 678 (section header H2):** *"§3. RCV Quantification — Triangulated Estimation (Three Ways of Counting)"*

**Issue:** Inverts Option B primary/parenthetical hierarchy. Per Insight #31 Option B verdict, TWoC is primary methodology name; "Triangulated [Estimation/RCV Estimation]" was retired as redundant. The current section title makes "Triangulated Estimation" primary and TWoC parenthetical — opposite of the ratified discipline.

**Verdict:** △ **ADOPTION GAP — needs 2-line fix.**

**Repair recommendation:** Replace section title at lines 225 + 678 with one of:
- **Option A (clean drop, recommended):** *"§3. RCV Quantification — Three Ways of Counting"*
- **Option B (preserved-form descriptor):** *"§3. RCV Quantification — Three Ways of Counting (triangulated three-method range)"*

Option A is cleanest and aligns most directly with the Insight #31 ratified discipline. Option B preserves the "triangulated" descriptor inline, matching glossary v3's term-definition pattern. **Recommended: Option A.**

### §4.7 Tech Appendix v1.0.0 Block 4 sections + worked examples + non-§3 body

**Current state:** Tech Appendix lines 1669, 3478, 3492, 3934, 3952, 4350, 4380:
- Line 1669: *"CIT + Three Ways + B = B₁ + B₂ are the framework apparatus for extraction commons"* — TWoC primary.
- Line 3478: *"§11.1 Block 4 — Norway petroleum calibration (Three Ways of Counting executed)"* — TWoC primary; section header.
- Line 3492: *"§1. Norway calibration — Three Ways of Counting executed"* — TWoC primary; section header.
- Line 3934: *"Even Norway, the framework's canonical-existing-B2 exemplar, carries a residual CS of approximately $10–15 trillion when triangulated across Three Ways"* — body text; "triangulated" as adverb describing Three Ways execution.
- Line 3952: *"§2. Appalachian coal calibration — Three Ways of Counting executed"* — TWoC primary.
- Line 4350: *"...the 'accountability gap' is real, large, and triangulation-confirmed"* — body text; "triangulation-confirmed" as compound descriptor.
- Line 4380: *"The 50× IPG ratio is empirically grounded by triangulation across three independent methods"* — body text; "triangulation" as concept-noun.

**Verdict:** ✓ **ADOPTED throughout.** All section headers use TWoC primary; all body-text uses of "triangulated" / "triangulation" are descriptive (adverb / concept-noun / preserved-form), not primary methodology naming.

**Repair:** None.

### §4.8 Block 4 validation document

**Current state:** `core/technical-appendix/block4_validation_2026-04-25.md`:
- Line 1: *"# Block 4 validation — Norway + Appalachian coal Three Ways estimates + sensitivity"*
- Line 12: *"## §1. Norway calibration — Three Ways of Counting executed"*
- Line 105: *"## §2. Appalachian coal calibration — Three Ways of Counting executed"*
- Body: TWoC + "triangulated" (as descriptor) consistently.

**Verdict:** ✓ **ADOPTED.** Headers + body align with Option B verdict.

**Repair:** None.

### §4.9 Bibliography references

**Current state:** `research/literature/bibliography.md` lines 797, 802, 805, 811, 814, 829, 832, 838, 841 — all reference "Triangulated RCV Estimation rigor pass" by its historical 2026-04-24 file name.

**Verdict:** ✓ **LEGITIMATE-HISTORICAL.** Bibliography entries cite the 2026-04-24 rigor pass file by its filename (`commons_bonds_rigor_pass_2026-04-24_term_triangulated_rcv_estimation_v1.0.0.md`) and reference the pass by its 2026-04-24 name. This is correct disciplinary practice — file references should reference by file-name-at-the-time, and bibliography provenance traces should reflect historical naming. No reader is misled because the bibliography itself is provenance-tracking.

**Repair:** None.

### §4.10 Older rigor passes (internal references)

**Current state:** Multiple rigor passes from 2026-04-24 + 2026-04-25 reference "Triangulated RCV Estimation" internally (e.g., `commons_bonds_rigor_pass_2026-04-24_three_ways_rcv_formal_model_v1.0.0.md`).

**Verdict:** ✓ **LEGITIMATE-HISTORICAL.** Older rigor passes predate the 2026-04-28 rename; their internal naming is historical and should not be retroactively edited (per Working Principle on retirement-trace discipline + audit-trail integrity).

**Repair:** None.

---

## §5. Aggregate verdict + ratification choices

### §5.1 Recommended verdict

**KEEP TWoC adoption state with one minor adoption-fix at Tech Appendix v1.0.0 §3 section title (lines 225 + 678).** All other surfaces have cleanly adopted TWoC as primary methodology name with "the triangulated three-method range" preserved as inline result phrasing per Option B verdict. The one identified gap is a stale-formatting artifact, not a substantive disagreement with the rename.

One concrete fix:

**ENHANCEMENT (sole):** Tech Appendix v1.0.0 §3 section title inversion fix at lines 225 (TOC) + 678 (section header).

- Replace: *"§3. RCV Quantification — Triangulated Estimation (Three Ways of Counting)"*
- With: *"§3. RCV Quantification — Three Ways of Counting"*

(Alternative preserved-form variant: *"§3. RCV Quantification — Three Ways of Counting (triangulated three-method range)"* — author preference if descriptor in title is desired.)

### §5.2 Pass-fail verdict on as-currently-written TWoC adoption state

**ADEQUATE.** 9 of 10 audited surfaces cleanly adopt TWoC. The Tech Appendix §3 section-title inversion is a 2-line gap that affects the academic-publisher-facing TOC + section header — high-leverage surface, low-cost fix. Without the fix, an academic-publisher reviewer scanning the TOC would see "Triangulated Estimation (Three Ways of Counting)" and infer that "Triangulated Estimation" is the primary term, contradicting the chapter title + body + glossary + terms_index discipline.

### §5.3 Pass-fail verdict on enhanced TWoC adoption state per §5.1

**STRONG.** With Tech Appendix §3 section-title fix applied, all 10 audited surfaces present TWoC as primary methodology name. Adoption is uniform across publisher-facing top-tier + body + scaffolding surfaces; legitimate-historical references in bibliography + older rigor passes are correctly preserved as provenance traces.

### §5.4 Author ratification choices

**(a) Full ratify §5.1 enhancement (Option A clean drop)** — Tech Appendix v1.0.0 lines 225 + 678 edited from *"Triangulated Estimation (Three Ways of Counting)"* to *"Three Ways of Counting"*. **Recommended.** 2-line edit.

**(b) Ratify with preserved-form descriptor variant (Option B)** — Tech Appendix v1.0.0 lines 225 + 678 edited from *"Triangulated Estimation (Three Ways of Counting)"* to *"Three Ways of Counting (triangulated three-method range)"*. Preserves descriptor inline; matches glossary v3 pattern.

**(c) Defer ratification** — accept Phase 1's "minor; can defer until pre-submission review" framing; track as TODO for pre-publication sweep.

**(d) Modify verdict** — author specifies different fix language.

**(e) Reject** — author judges current Tech Appendix §3 section-title acceptable; would require justifying why the inversion of Option B verdict's primary/parenthetical hierarchy is acceptable in a publisher-facing TOC.

**Recommendation: (a) Full ratify (Option A clean drop).** The fix is 2 lines; alignment with Insight #31 Option B verdict is direct; clean drop is more parsimonious than preserved-form variant; section-title clarity is improved.

### §5.5 Implementation pending after ratification

If (a) full ratify:
1. Tech Appendix v1.0.0 HTML lines 225 + 678 — replace section title text per §5.1.
2. terms_index — append Phase 2 verdict entry; cross-reference to this rigor pass.
3. Open Insights — new Insight # closed-ratified entry capturing Phase 2 #6 verdict (number TBD; coordinate with sibling Phase 2 + theorem-rigor passes).

**Same open question as Insights #35 + #38 + #40 + Phase 2 #8 + Phase 2 #7 Tech Appendix HTML edit timing:** apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Possible unification:** all Phase 2 Tech Appendix changes batched into Phase 3 v2.0.0 rebuild as single coordinated update.

### §5.6 Pre-publication external review (Insight #39)

This rigor pass produces Claude's adoption-fit assessment for Three Ways of Counting. Per Insight #39, eventual external review by economics PhD or formal-methods expert is warranted before publication. For TWoC adoption specifically, an external reviewer scanning the publication-ready Tech Appendix should encounter consistent TWoC primary naming across TOC + section headers + body + bibliography + glossary; the §3 section-title fix is the discipline-completing edit that closes the one gap.

This rigor pass does NOT replace external review; it produces the substrate that external review would test.

---

## §6. Open questions for author discussion

1. **Section-title fix variant choice.** §5.1 offers Option A (clean drop) vs Option B (preserved-form descriptor in title). Author preference?

2. **Tech Appendix HTML edit timing.** Same open question as Insights #35 + #38 + #40 + Phase 2 #8 + Phase 2 #7: apply now to v1.0.0 (single 2-line edit) vs batch into Phase 3 v2.0.0 rebuild. **Recommended:** batch with the other Phase 2 Tech Appendix edits — even though this one is a 2-line fix that could be applied immediately, batching maintains coordinated-update discipline.

3. **Cross-coordination with Insights #35 + #38 + #40 + Phase 2 #7 + Phase 2 #8 ratification.** All Phase 2 audits accumulate Tech Appendix edits. The combined patch (per-audit verdicts ratified) would be substantially larger than any single audit's footprint, suggesting the Phase 3 v2.0.0 rebuild is the natural batching point. Confirm?

4. **Phase 2 #5 [ExtTail-collision] interaction.** Externality Tail uses suffix similar to "tail" in statistics-distribution; Phase 2 #5 will audit that collision next. No direct interaction with TWoC adoption-fit, but both audits sit adjacent in vocabulary-discipline territory. Note for sequential reading.

---

## §7. Cross-references

### §7.1 Upstream rigor passes

- [Phase 1 full framework audit §10 #5](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md) — flagged Three Ways of Counting post-rename adoption-fit verification for Phase 2 (minor).
- [Triangulated RCV Estimation Naming Review (Insight #31)](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_triangulated_rcv_estimation_naming_review_v1.0.0.md) — RATIFIED 2026-04-28; Option B verdict; original rename decision this pass verifies adoption against.
- [Triangulated RCV Estimation original promotion rigor pass](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_triangulated_rcv_estimation_v1.0.0.md) — RATIFIED 2026-04-24 commit `4f48c48`; Ring-2 promotion under historical name; preserved as provenance trace.
- [Three Ways + RCV Formal Model rigor pass](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_three_ways_rcv_formal_model_v1.0.0.md) — RATIFIED 2026-04-24 commit `1c8e4dd`; methodology blocks 1-4; preserved as provenance trace.
- [Phase 2 Theorem E.4 Integral Convergence](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #40); methodology template.
- [P2#8 RCV integrand Q(t) notation-clarity](commons_bonds_rigor_pass_2026-04-29_phase2_rcv_integrand_q_notation_clarity_v1.0.0.md) — [PROPOSED] sibling.
- [P2#7 Scarcity multiplier formula academic-defensibility](commons_bonds_rigor_pass_2026-04-29_phase2_scarcity_multiplier_academic_defensibility_v1.0.0.md) — [PROPOSED] sibling.
- [Phase 2 Foreclosure Bond housing-crisis collision](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #38); methodology template.
- [Phase 2 Cost Severance + Severed Cost Tier 2d](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #35); methodology template.

### §7.2 Sibling Phase 2 candidates (concurrent + remaining)

- **Phase 2 #3 Theorems E.1, E.3, E.5, Renewable Imperative academic-rigor proof-structure audit** — sibling session in progress 2026-04-29. No interaction with TWoC adoption-fit (theorems do not reference Three Ways of Counting methodology naming).
- **P2#8 [Q(t)] RCV integrand Q(t) notation-clarity** — [PROPOSED] 2026-04-29 (this session).
- **P2#7 [scarcity-multiplier] Scarcity multiplier formula academic-defensibility** — [PROPOSED] 2026-04-29 (this session); Method 3 is one of the three Three Ways sub-methods, but the audit is on functional-form defensibility, not on naming.
- **P2#5 [ExtTail-collision] Externality Tail statistics-distribution-tail collision** — pending in this session (next).
- **P2#4 [RCV-acronym] RCV acronym collision audit** — pending in this session.

### §7.3 Downstream artifacts (this pass would update on ratification)

- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` lines 225 + 678 — section-title fix per §5.1 (single 2-line edit).
- `core/terms/terms_index.md` — append Phase 2 verdict entry; cross-reference to this rigor pass.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight # closed-ratified entry capturing Phase 2 #6 verdict (number TBD; coordinate with sibling passes).

### §7.4 Pre-publication external review (Insight #39)

This rigor pass + 4 sibling Phase 2 deeper-dive passes (#8, #7, #5, #4) + 4 sibling theorem rigor passes (E.1, E.2, E.3, E.5) produce Claude's pre-external-review assessment substrate. Per Insight #39, eventual external review by economics PhD + formal-methods expert is warranted before publication. The TWoC adoption-fit verdict here is comparatively low-stakes (one section-title fix); external review will more naturally focus on the heavier audits (theorems; functional-form defensibility; notation discipline).

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED — pending author ratification].**
