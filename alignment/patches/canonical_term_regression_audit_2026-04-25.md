# Canonical-term regression audit — 2026-04-25

**Header note (added 2026-04-30 per Insight #60 scaffolding cleanup pass):** This audit was performed against the framework's state on 2026-04-25, including references to `manuscript/technical-appendix/TechnicalAppendix_v0.0.5.html` — an interim Tech Appendix state that has since been superseded by v1.0.0 (current canonical) + v0.0.5_supplement.md (archived to `manuscript/technical-appendix/archive/`). References to v0.0.5.html in this audit's content describe what was true on 2026-04-25; per Working Principle #4 + Insight #59 retirement-trace discipline, this audit document preserves the historical state. Current Tech Appendix is `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html`; supplement at `manuscript/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md`.

**Scope:** Repository-wide sweep across `research/`, `core/`, `manuscript/` for retired truth-claim usage of "canonical" per the discipline established in `tools/back-matter/sources/terms_index.md` lines 4–18 (canonical-as-truth-claim-about-taxonomy/finality retired in favor of provenance/current-state language; canonical-as-adjective-for-source/exemplar/case preserved).

**Trigger:** User-flagged regression during 2026-04-25 session (`research/case-studies/README.md` line 7 use of "canonical case-study content"). Sweep extended at user direction to cover `core/` and `manuscript/` directories.

**Discipline reference:** `tools/back-matter/sources/terms_index.md` §0 (lines 4–18) + Working Principle #2 (audit-concept-not-phrase).

---

## §1. What was swept (this commit cluster)

### research/

| File | Fix |
|---|---|
| `research/case-studies/README.md` | "All canonical case-study content for Book One lives inline" + "chapter-inline approach is canonical" + "intentionally empty" (factually stale) replaced with current-state overview pointing at audit doc; integration-state summary refreshed for all 22 standalone case files. |
| `research/case-studies/chesapeake-fisheries.md` | "canonical Tier 6 + Tier 3 case" (referenced retired 8-tier scheme) → Ecosystem-commons + Cohesion-commons paradigm case per current 10-commons discipline. "canonical case" (Ch. 3) → "anchor case". |
| `research/case-studies/libby-vermiculite.md` | "current canonical framing" → "current ratified framing" (40× cost-to-revenue ratio). |
| `research/case-studies/deepwater-horizon.md` | Same fix (40% cost recovery ratio). |

### core/

| File | Fix |
|---|---|
| `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` | File-level "Status: Canonical" → "Current methodology reference (v1.4.0 Tier-1 update)". "What changes in this canonical doc" (lines 26 + 61) → "What changes in this doc". "(canonical, v1.4.0 reframing of C9 patch §3)" parentheticals (lines 29, 95) → "(v1.4.0 reframing of C9 patch §3)". "the canonical methodology source" + "the canonical synthesis" + "the internal canonical source" (Purpose section + §7) → current-state language. "Defines the 10 canonical dimensions" → "Defines the 10 commons categories surfaced to date". "Five candidates tested against the canonical 10" → "against the working 10". "All 10 dimensions are full-rigor-verified under canonical names" → "under their current ratified names". "eight-tier-v10.html: CIT canonical source" + "c9_ait_canonical_positioning_patch.md: Scaffolding-vs-load-bearing canonical" → reframed as retired-precursor + lineage-reference. |
| `tools/audits/commons_bonds_case_study_audit_v1.0.6.md` | File-level "Status: Canonical reference for Book One chapter drafting" → "Current integration-tracking reference for Book One chapter drafting". |
| `manuscript/technical-appendix/TechnicalAppendix_v0.0.5.html` | "v1.3.0 canonical cohort" (2 instances, current-cohort-as-canonical truth-claim) → "v1.3.0 ratified cohort". |

### manuscript/

| File | Fix |
|---|---|
| `manuscript/chapters/Chapter_10___GuidanceDoc.md` | "current framework canonical state" (Path-dependency note) → "current framework state" + 2026-04-25 update note that Path F has been ratified and superseded by Option C'. |
| `manuscript/chapters/Chapter__6___GuidanceDoc.md` | "the canonical authorial-voice positioning" → "the ratified authorial-voice positioning" (Register 2 prose for Option C' political-philosophical accommodation). |
| `manuscript/chapters/Chapter__8___GuidanceDoc.md` | "canonical guidance-doc location" → "standard guidance-doc location" (filesystem-parity description). |

---

## §2. What was deliberately left alone (and why)

### Approved canonical-as-adjective-for-source/scholarship usages (preserved across multiple files)

Per terms_index.md discipline, "canonical" survives as an adjective in specific approved patterns. Examples retained:

- **"Norway is the canonical existing B2 exemplar"** — explicit approved usage in terms_index. Retained in glossary v3, supplement, multiple guidance docs, bibliography entry for Hartwick.
- **"McDowell coal IPG = 33 is the framework's canonical empirical compression"** — approved in terms_index. Retained in glossary v3.
- **"Anderson is the canonical scholarly anchor for the autonomy dimension"** — canonical-as-source-descriptor for established literature. Retained in Ch 1 GuidanceDoc + bibliography.
- **"Ostrom is the canonical intellectual ancestor for collective-management-of-commons arguments"** — canonical-as-source-descriptor. Retained in bibliography.
- **"Pigou is the canonical 20th-century source on externalities"** — same pattern. Retained.
- **"Fricker's *Epistemic Injustice* is now canonical in philosophy, sociology, legal theory, AI ethics"** — descriptive of literature's status. Retained.
- **"Weston, *Families We Choose* — primary canonical [chosen-family scholarship]"** — canonical-as-scholarly-anchor for a Kindred-dimension subscope. Retained in bibliography + dimensions doc + indigenous case file.
- **"Kimmerer / Simpson / Coulthard are canonical figures"** (indigenous scholarship) — canonical-as-adjective-for-scholars. Retained in indigenous case file + sociology-source draft.
- **"the Kimberley Process certification is the canonical case [of simulated-reattachment]"** — case-as-canonical-example. Retained in Ch 7 draft.
- **"Chesapeake oysters and blue crabs are the canonical renewable-past-regeneration cases"** — case-as-canonical-example. Retained in Ch 3 GuidanceDoc.
- **"NYC consulting-years isolation case is canonically a single-dimension case by design"** — pedagogical-design-choice description. Retained in dimensions doc.
- **"Federal-agency canonical source for how reclamation bonds operate in practice"** (OSMRE 2020) — regulatory-authority-canonical-as-source. Retained in bibliography.
- **"DICE is the canonical framework for pricing cumulative climate damage as externality"** (Nordhaus) — framework-as-canonical-in-its-own-literature. Retained in bibliography.
- **"Darity & Mullen's wealth-gap calculation methodology is canonical for the CSD instrument"** — methodology-as-canonical-source. Retained in bibliography.
- **Per-dimension "canonical cases" usage throughout dimensions doc** (Test 13 case-clusters, naming-cohort case-as-anchor pattern, "canonical 20th-century case for tobacco internal-research suppression," etc.) — all case-as-canonical-example usage, retained as the dimensions-doc methodology depends on this case-anchoring pattern.

### Quoted-retired-framing usages (preserved as appropriate provenance)

Several files explicitly quote the retired "canonical" framing as part of describing what was retired. These are appropriate:

- `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` line 46: "the 10 abundances stop being 'the canonical taxonomy of cost severance'" — quoting retired claim.
- Same file line 64: "ten canonical dimensions of cost severance as a definitive ontological taxonomy" — quoting retired framing.
- Same file line 75: "the ten canonical dimensions" — Phase A2 decision-point preserved for author authorial-voice deliberation; the surrounding context already frames it as the retired framing.
- `tools/audits/commons_bonds_chapter_audit_v1.0.6.md` line 26 + multiple: "v1.0.5 framing (ontological): 'these are the canonical 10 dimensions...'" — explicit retired-framing quote.
- `tools/audits/commons_bonds_case_study_audit_v1.0.6.md` line 37: "v1.0.5 framing (ontological): 'each activating specific canonical dimensions per the 10-abundance taxonomy'" — explicit retired-framing quote.
- `manuscript/technical-appendix/TechnicalAppendix_v0.0.5.html`: "the seven commons categorys below reflect the earlier canonical cohort, with the four renamed members updated" — describes retired-cohort migration. Retained.

### Math-canonical-form usages (preserved as standard mathematical idiom)

- `manuscript/technical-appendix/TechnicalAppendix_v0.0.5.html`: multiple "canonical two-term formula" / "canonical n = 2 special case" / "canonical externality profile" / "canonical instance" of Weitzman discounting — these use "canonical" in the sense familiar from mathematics ("canonical form," "canonical example") which is distinct from the truth-claim-about-taxonomy usage the discipline retired. Retained.
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`: "the two-term formula is the canonical n = 2 special case under the four gates" — same math-canonical-form pattern. Retained.

### Per-case "Canonical draft in [chapter]" status descriptors (preserved as descriptive)

`tools/audits/commons_bonds_case_study_audit_v1.0.6.md` lines 174 + 239 + 302 + 359: "Status: Canonical draft in `manuscript/chapters/Chapter__N_*__Draft.md`" — describing where the active/authoritative chapter draft lives. Borderline (could read as truth-claim) but functionally descriptive of file location for ongoing draft work. Retained pending author decision; flagged here for visibility.

---

## §3. Borderline cases for author review

The following hits sit on the edge between approved usage and regression. Surfaced for ratified decision:

| File | Line | Usage | Surface concern | Recommended disposition |
|---|---|---|---|---|
| `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` | 17 | "v1.4.0 Tier-1 update header is canonical-source-of-truth pointer" | Doc-as-canonical-source claim (file-level) | KEEP — describes pointer role for transitional period; the supplement and terms_index use the same pattern. |
| `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` | 66 | "Per-case dimension activation (canonical in chapter audit + case-study audit)" | Audits-as-canonical claim | KEEP — descriptive of where activation tracking lives. |
| `tools/audits/commons_bonds_case_study_audit_v1.0.6.md` | multiple | "Book 1 — Ch N canonical" placement-verdict labels in §1 cross-case summary table | Placement-as-canonical labeling (15+ rows) | KEEP for now — the audit's category column uses "canonical" as a placement-verdict shorthand; reframing requires audit-doc structural pass. Flag for Phase B audit-doc revision. |
| `tools/audits/commons_bonds_case_study_audit_v1.0.6.md` | 174, 239, 302, 359 | "Status: Canonical draft in [chapter]" per-case status | Draft-as-canonical descriptor | KEEP — describes where the authoritative draft lives. Borderline; flag for author. |
| `tools/audits/commons_bonds_chapter_audit_v1.0.6.md` | multiple | "canonical 8 tiers" / "canonical 10-dimension" in chapter-specific terminology-propagation lines | References retired schemes in transitional context | KEEP — explicitly references retired schemes for chapter-rewrite tracking; reframing risks erasing the migration paper trail. Flag for Phase B chapter-audit-doc revision. |
| `manuscript/technical-appendix/TechnicalAppendix_v0.0.5.html` | multiple | "canonical two-term formula" math idiom | Math canonical-form vs framework canonical-claim | KEEP — math-canonical-form is a distinct usage from the retired truth-claim discipline. |

---

## §4. Phase B follow-up items surfaced

1. **Tech Appendix HTML §K Decomposition Layer cluster:** the "v1.3.0 ratified cohort" passage (now swept) is part of a broader §K passage that still carries 8-tier-vintage acronym (FGC × 15 instances per supplement §1). Phase B HTML rewrite addresses both together.
2. **Chapter audit v1.0.6 + case-study audit v1.0.6 placement-verdict columns:** "Book 1 — Ch N canonical" labels function as shorthand. Consider Phase B audit-doc structural revision to "Book 1 — Ch N (current placement)" or similar non-truth-claim language.
3. **Dimensions doc Phase B full rewrite** (already queued — see line 17): file rename + restructure for commons-categories framing + Three Ways of Counting integration. Will reabsorb the v1.4.0 Tier-1 update header into the revised structure.

---

## §5. Discipline-strengthening note

This sweep was triggered by an inline finding (case-studies README line 7 echoed during user-facing text). Confirms the standing memory rule (`feedback_terminology_regression_check`) is operating: regressions get surfaced inline rather than waiting for a sweep. The sweep is the periodic clean-up; the inline finding was the front-line catch.

---

*End of canonical-term regression audit, 2026-04-25.*
