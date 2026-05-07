# AGENTS.md — Internal collaborator orientation

**Layer:** internal scaffolding (per Working Principle #10).
**Audience:** author + AI collaborator + future-Claude.

This document is the canonical internal-scaffolding orientation for the Commons Bonds project — current canonical state, working discipline, repository structure, session workflow, and operating rules. Per WP#10, this content lives at the internal layer; the publisher-facing landing page is [`README.md`](README.md).

---

## Current canonical state

| Component | Status | File |
|---|---|---|
| Rigor protocol | **v2.2.0** canonical — Pre-Submission Peer Review Suite (11 modules) + Path Comparison Mode + 6 informational goals (personal/ethical satisfaction + family wellbeing + career safety + time/capacity preservation + movement utility + financial sustainability — produce per-path findings without driving primary recommendations) | [`tools/commons_bonds_rigor_protocol_v2.2.0.md`](tools/commons_bonds_rigor_protocol_v2.2.0.md) |
| Working principles | **v1.0.0 canonical — 10 principles**; WP#4 REFINED 2026-04-30 (tiered retirement-trace policy + canonical retirement-archive per Insight #59); WP#9 NEW 2026-04-29 (worktree-isolation git workflow); WP#10 NEW 2026-04-30 (two-layer content origination discipline per Insight #9 generalization) | [`alignment/commons_bonds_working_principles_v1.0.0.md`](alignment/commons_bonds_working_principles_v1.0.0.md) |
| Vocabulary strategy | **v1.0.1 canonical** — §3.1 Tier disambiguation note added 2026-04-30 (Insight #63 quick-fix). §6 + §13 light-trace migration to retirement archive applied 2026-04-30 (α-thread Phase α.1); §7 remains queued. | [`alignment/commons_bonds_vocabulary_strategy_v1.0.1.md`](alignment/commons_bonds_vocabulary_strategy_v1.0.1.md) |
| Framework-positioning disciplines | **v1.0.0 canonical 2026-05-06** — 11 disciplines (FPD-1 through FPD-11) + canonical framework articulations + canonical Three Tiers / Live-call setup templates. Grounded in the project's success criterion (vocabulary adoption at scale per README). Disciplines: public-record screen, AI-disclosure first-contact-only, forwardability criterion, formality discipline, pre-read brief structure, two-artifact pair (pre-read + interview prep) with Three Tiers + Live-call setup canonical templates, attribution protocol with Q0 + four preference categories, scope-explicitness ("lead them to water"), substantive background brief (subject's body of work + stances + existing domain vocabulary), credibility-first question framing with axis-matched structure + fit/adoption/misuse failure-mode disambiguation, contingency planning for live interviews. Plus 7 canonical framework articulations (Hotelling, Ostrom, Polanyi, Mazzucato, Boyce, Marx/Harvey/Klein, reparations economics) — oral-friendly drop-in language for interview lineage-extension pivots. | [`alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`](alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md) |
| Terms index | **v1.0.0 canonical 2026-04-30** (α-thread Phase α.1 batched commit) — current-state registry; summary-level retirement traces per refined WP#4; full traces in retirement-archive index. UNBLOCKS Phase α.2 Tech Appendix v2.0.0 + Phase α.3 Glossary v4. | [`core/terms/terms_index.md`](core/terms/terms_index.md) |
| Decision-time application (internal) | **v1.0.0 canonical** — internal-scaffolding artifact preserving Pattern 1/2/3 literature analysis + two-layer framing rationale + worked-example seed material; per Insight #9 verdict (b) + WP#10. | [`core/methodology/decision_time_application_internal_v1.0.0.md`](core/methodology/decision_time_application_internal_v1.0.0.md) |
| Retirement archive | **canonical retirement-trace index** per refined WP#4 (Insight #59) — 16 vocabulary retirements + 2 methodology retirements + 3 file/artifact retirements + cross-references to ratifying rigor passes. | [`archive/retirements/index.md`](archive/retirements/index.md) |
| Open insights tracker | **6 OPEN** as of 2026-05-06: #36 (Ch 1 + Ch 3 conversational drafting — Ch 1 NOW DRAFTED 2026-05-04 as "The Quiet Math"; Ch 3 still queued behind Chesapeake fieldwork outreach), #39 (pre-publication external review), #63 (Tier word-level conceptual collision; quick-fix applied, focused rigor pass queued), #64 (unpriced subsidies — raised; capture-only), #65 (six-mechanism cost-severance enumeration — under-review 2026-05-04; full framework cascade pending), #66 (universal computational claim — under-review 2026-05-04; Ch 1 plant placed, Ch 7 three-case parallel pending). Closed since v1.51.0: #21 (Ch 6 supplementary placement — folded into Phase 3 Tech Appendix rebuild). Next free insight number: **#67**. | [`alignment/commons_bonds_open_insights_v1.0.0.md`](alignment/commons_bonds_open_insights_v1.0.0.md) |
| Routines | **v1.0.0 draft** — 4 sentinel-style scheduled-agent prompts: Routine 1 (daily terminology-regression sentinel) + Routine 2 (weekly pre-submission readiness audit) + Routine 3 (rigor pass status tracker) + Routine 4 (open insights status sync). | [`tools/routines/proposed_routines_v1.0.0.md`](tools/routines/proposed_routines_v1.0.0.md) |
| Abundance dimensions | **v1.3.0 — Path F reframing applied.** 10 abundances framed as organizational scaffolding over variables CIT has surfaced across 18 cases — illustrative, not ontological. Queued for absorption into Tech Appendix v2.0.0 §C.2 during Phase 3 rebuild; directory will archive at that point per Insight #55 hygiene pass. | [`core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md`](core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md) |
| Eight-tier decomposition | **RETIRED 2026-04-24** per tier-reframing rigor pass §11.2. Path F + Four Gates discipline supersedes. Archived 2026-04-30 per Insight #55 hygiene pass. | [`archive/decomposition/eight-tier-v10.html`](archive/decomposition/eight-tier-v10.html) |
| Chapter audit | **v1.0.6 canonical — Path F reframing applied** | [`core/chapters/commons_bonds_chapter_audit_v1.0.6.md`](core/chapters/commons_bonds_chapter_audit_v1.0.6.md) |
| Case-study audit | **v1.0.6 canonical — Path F reframing applied** | [`core/case-studies/commons_bonds_case_study_audit_v1.0.6.md`](core/case-studies/commons_bonds_case_study_audit_v1.0.6.md) |
| Technical appendix | **v1.0.0 canonical — Path F Section L (Four Gates discipline) + Section M (formula generalization) integrated.** Phase 3 v2.0.0 rebuild queued (~20–30 hrs; batches all Phase 2 + Group 1 ratifications: theorem restructures E.1a+E.1b / E.2 / E.3 / E.4 / E.5; §L methodological footnotes for Cost Severance + Foreclosure Bond + Intergenerational Option Value; notation discipline α→ξ + τ→u + C→𝒞; bibliography expansion; absorption of `core/dimensions/` content into §C.2). v0.0.3, v0.0.4, v0.0.5 superseded; supplements in `core/technical-appendix/archive/`. | [`core/technical-appendix/TechnicalAppendix_v1.0.0.html`](core/technical-appendix/TechnicalAppendix_v1.0.0.html) |
| Glossary | **v3 canonical** — Phase A3 framework structural-restructure ratifications integrated. Phase 4 v4 rebuild queued (~3–5 hrs; derives from terms_index v1.0.0+ per S1 schema; absorbs Phase 2 + Group 1 ratifications). | [`core/glossary/commons_bonds_updated_glossary_v3.html`](core/glossary/commons_bonds_updated_glossary_v3.html) |
| Book One scope | v1.0.3 canonical | [`tools/commons_bonds_book_scope_v1_0_3.md`](tools/commons_bonds_book_scope_v1_0_3.md) |
| Guiding constraints | v1.0.0 canonical | [`tools/commons_bonds_guiding_constraints_v1_0_0.md`](tools/commons_bonds_guiding_constraints_v1_0_0.md) |
| Framework-scope decision | **Path F selected** — variables-not-dimensions reframing. PCR v1.1.0 §8 confirmed 2026-04-24. Extreme-rigor pass PASSES-WITH-CONDITIONS; Phase A2 Conditions 1–4 materially implemented 2026-04-24. Rigor-pass rerun available per §11.7. | [`tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md`](tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md) · [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md) |
| Tier reframing decision | **Reframing claim FAILS SC-1 on §5.3 duplication check (2026-04-24); dissolution ratified.** Variables replace tiers at framework-specification level. Conditions 1–4 APPROVED (2026-04-24); Condition 5 (Tier 6 / E overlap) deferred. | [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md) |
| Macro-grouping decision | **Option A ratified (2026-04-24) — macro-groupings REJECTED at every level.** Pure variable enumeration with narrative pacing is the book's structural approach. | [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_macro_grouping_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_macro_grouping_v1.0.0.md) |
| Manuscript drafting state | **9 of 10 chapters drafted** as of 2026-05-04. Ch 1 ("The Quiet Math") drafted + title ratified per `commons_bonds_rigor_pass_2026-05-04_ch1_title_candidates_v2.0.0.md`; framework-felt-not-named discipline applied. Ch 2, 4, 5, 7, 8, 9, 10 audit-clean (post Phase 1 framework audit). Ch 6 HTML canonical (Phase 3 rebuild queued). **Ch 3 (Watermen / Chesapeake fishery) remains undrafted** — gated on Chesapeake fieldwork outreach (Colden via DiMarzio interview pending). | [`manuscript/chapters/`](manuscript/chapters/) |
| Aeon essay pitch | **First-pass draft 2026-05-04** in author review at [`manuscript/essay/aeon/aeon-pitch-commons-bonds-winn.md`](manuscript/essay/aeon/aeon-pitch-commons-bonds-winn.md). Working title: "The Quiet Math" displaced from book-title-only; pitch placeholder "Pricing the Air"; title workshop continued next session. Mars/universality cut (closed-habitat thought experiment + six abundance-masking mechanisms + bad-actor / no-bad-actor symmetry). Pitch ~290 words; submission target `aeon.co/pitch` first-week-of-month window. **Pending upstream revision:** revisit McDowell case-walk + universality framing after Darity interview (week of May 10). | [`manuscript/essay/aeon/`](manuscript/essay/aeon/) |
| Noema essay | **Withdrawn 2026-05-01** per consent-rejection scope decision (ex-wife medical material foreclosed); rewrite-plan ratified same day at [`manuscript/essay/Noema/rewrite-plan_2026-05-01.md`](manuscript/essay/Noema/rewrite-plan_2026-05-01.md). Path B (book-first, essay paraphrases) chosen: revise once Ch 1 substrate fills. Personal-narrative cut (distinct from Aeon's universality cut). §V third-anchor case GATED on Colden interview outcome. | [`manuscript/essay/Noema/`](manuscript/essay/Noema/) |
| Outreach pipeline (week of 2026-05-05) | **12 cold-outreach drafts sent 2026-05-05** per `interview-outreach-drafts_2026-05-01.md`; **Ch 3 fieldwork outreach** sent 2026-05-05 09:00 ET per `interview-outreach-drafts_2026-05-04_ch3-fieldwork.md`. **ACCEPTED:** William Darity Jr. (Duke) — interview week of May 10; reply scheduled 2026-05-06 08:00 ET; pre-read brief drafted at [`research/outreach/darity-prereadbrief_2026-05-05.md`](research/outreach/darity-prereadbrief_2026-05-05.md). **DECLINED + WARM-INTRO OFFERED 2026-05-06:** Kate Raworth (declined 2026-05-05 via EA Beth Ingledew; Beth followed up 2026-05-06 offering an introduction to the Amsterdam DEAL implementation team — meaningful upgrade since Amsterdam City Doughnut is the framework's cleanest live Pattern 2 case). **PENDING REVIEW:** Mariana Mazzucato (holding response 2026-05-06 from Adam Albrecht, Office of Prof. Mazzucato — UCL IIPP). **VAL DiMARZIO RESPONSE (CBF, on behalf of Allison Colden):** scheduled 2026-05-06 08:00 ET; Colden pre-read brief drafted at [`research/outreach/colden-prereadbrief_2026-05-06.md`](research/outreach/colden-prereadbrief_2026-05-06.md). Other 8 cold-outreach recipients: no response yet. | [`research/outreach/`](research/outreach/) |
| Bibliography | **§19.5 Chesapeake fieldwork tentative sources** added 2026-05-05 (Colden public record + CBF positions + Bay-restoration legislation). Phase 3 Tech Appendix v2.0.0 bibliography expansion still queued. | [`research/literature/bibliography.md`](research/literature/bibliography.md) |
| Current handoff | **v1.52.0** multi-thread state-snapshot (Ch 1 drafted · Aeon first-draft · cold-outreach round in flight · Darity ACCEPTED · Colden via DiMarzio in motion). Layered on **v1.51.0** Ch 1 + Ch 3 drafting handoff (Ch 1 work since superseded by completed draft). | [`v1.52.0`](alignment/sessions/commons-bonds-session-handoff-2026-05-06_v1.52.0.md) · [`v1.51.0`](alignment/sessions/commons-bonds-session-handoff-2026-05-03_v1.51.0.md) |

## Repository structure

- **[`tools/`](tools/)** — canonical working methodology (session upload set). See [`tools/README.md`](tools/README.md) for upload-set directory. Contains rigor protocol, book scope, guiding constraints, `routines/` (sentinel discipline draft), `rigor-passes/` (historical audit trail), `pre-submission-reviews/` (PSR + PCR records), `archive/` of superseded methodology versions.
- **[`manuscript/`](manuscript/)** — book content:
  - `chapters/` — 9 drafts (Ch 1, 2, 4, 5, 7, 8, 9, 10 in markdown + Ch 6 in HTML) + 10 guidance docs + dedication + author's note. Ch 3 outstanding (gated on Chesapeake fieldwork outreach). `chapters/archive/` holds Ch 6 supplementary drafts pending integration into Phase 3 Tech Appendix rebuild.
  - `essay/Noema/` — withdrawn 2026-05-01; rewrite-plan ratified same day (Path B: book-first, essay paraphrases). Active rewrite material lives in `Noema/rewrite-plan_2026-05-01.md`. Original submission docs preserved as historical record.
  - `essay/aeon/` — Aeon pitch first-draft 2026-05-04; in author review. Mars/universality cut (closed-habitat thought experiment); submission target `aeon.co/pitch` first-week-of-month window. **Pending upstream revision after Darity interview.**
  - `essay/berggruen/` — competition requires AI-free content (do not touch).
- **[`core/`](core/)** — canonical framework content:
  - `dimensions/` (v1.3.0; queued for Phase 3 absorption)
  - `glossary/` (HTML; v3 canonical, v4 rebuild queued)
  - `technical-appendix/` (math-heavy HTML; v1.0.0 canonical, v2.0.0 rebuild queued)
  - `terms/` (terms_index — single-source-of-truth pipeline for glossary derivation)
  - `methodology/` (internal-scaffolding methodology artifacts per WP#10; e.g. `decision_time_application_internal_v1.0.0.md`)
  - `chapters/` (chapter audit + supporting analysis)
  - `case-studies/` (per Insight #55: 8-tier `decomposition/` archived to [`archive/decomposition/`](archive/decomposition/))
- **[`alignment/`](alignment/)** — project-meta:
  - Top-level scaffolding files: working principles (v1.0.0), vocabulary strategy (v1.0.1), open insights tracker, personal-stories candidates
  - `decisions/` — ratified decisions + pending-review items (e.g. April 19 per-section captures, alternate 8-tier retired for tier-decision review)
  - `patches/pending-framework-review/` — C2/C3/C9 patches + 2 layer-era triage analyses, gated on tier-structure decision
  - `patches/archive/` — applied patches
  - `sessions/` — current handoff + `archive/` of prior handoffs
- **[`research/`](research/)** — `case-studies/` (17 files — see [README](research/case-studies/README.md)) + `literature/` (bibliography incl. §19.5 Chesapeake fieldwork sources added 2026-05-05) + `outreach/` (cold-outreach drafts + per-recipient response/scheduling tracking + interview pre-read briefs) + `story-drafts/` (Ch 1 substrate-capture files per author dumps)
- **[`publishing/`](publishing/)** — `essay-drafts/` (Noema/Berggruen source prose)
- **[`archive/`](archive/)** — deferred + retired material (see archive convention below):
  - `retirements/index.md` — canonical retirement-trace index per refined WP#4 (Insight #59)
  - `decomposition/` — retired 8-tier decomposition (per Insight #55 hygiene pass)
  - `_OneDayMaybe/book-two/` and `_OneDayMaybe/book-three/` — dumping grounds for Book Two / Book Three
  - `_OneDayMaybe/satellite-essays/` — framework-adjacent essays
  - `_OneDayMaybe/two-book-strategic-analysis.html` — strategic rationale for the books split

## Archive convention (Insight #62 ratified 2026-04-30)

The project uses a **hybrid archive structure**:

- **Top-level [`archive/`](archive/)** — cross-domain retirement material + multi-book seed material:
  - `archive/retirements/index.md` — single canonical retirement-trace index (refined WP#4)
  - `archive/decomposition/` — retired methodologies surfaced from any domain
  - `archive/_OneDayMaybe/` — Book 2 / Book 3 / satellite-essay seed material
- **Per-domain `<domain>/archive/`** — domain-specific historical predecessors kept adjacent to live work:
  - [`core/technical-appendix/archive/`](core/technical-appendix/archive/) — superseded TA versions + supplements
  - [`manuscript/chapters/archive/`](manuscript/chapters/archive/) — Ch 6 supplementary drafts pending integration
  - [`tools/archive/`](tools/archive/) — superseded methodology versions

**Rationale (per Insight #62 verdict (c)):** the actual cross-domain audit-trail need is solved by the canonical retirement-trace index. Per-domain archives encode origin context next to live work, which WP#10's "internal scaffolding can be rich" license endorses. Full consolidation (option (a)) was rejected for low marginal navigability gain vs. ~10–20 path-update cost + loss of domain-context proximity.

**Single search location for retirement provenance:** [`archive/retirements/index.md`](archive/retirements/index.md).

## Working discipline

10 working principles (v1.0.0 canonical). Selected:

- **WP#1** Vocabulary parsimony
- **WP#3** Two-path rigor — allocation symmetry + shield absence
- **WP#4** Retirement-trace discipline — REFINED 2026-04-30 (tiered policy by document type + canonical retirement-archive at [`archive/retirements/index.md`](archive/retirements/index.md))
- **WP#7** Earning-its-place + scaffolding-vs-book-worthy
- **WP#8** Publisher-facing artifacts scrubbed of scaffolding
- **WP#9** NEW 2026-04-29 — worktree-isolation git workflow with session-end fast-forward to `main`
- **WP#10** NEW 2026-04-30 — Two-layer content origination discipline (internal-scaffolding vs external-publisher-facing)

Full list + rationales: [`alignment/commons_bonds_working_principles_v1.0.0.md`](alignment/commons_bonds_working_principles_v1.0.0.md).

### WP#10 layer classification

| Layer | What lives here | Discipline |
|---|---|---|
| **Internal scaffolding** | `.claude/` · `tools/` · `core/methodology/` · `alignment/` · `research/` · `archive/` · this `AGENTS.md` | Rich; preserves methodology notes, worked examples, research-grade depth, literature audits, audit trail, decision-time-application drafts, Book 2 / Book 3 seed material, framework-supporting material that doesn't need publisher-facing exposure |
| **External publisher-facing** | `manuscript/chapters/*` · `core/glossary/*` · `core/technical-appendix/*` · `manuscript/essay/*` · `README.md` | Disciplined per WP#8 (scrubbed of audit-trail content) + Pattern 2 demonstration (threaded through cases rather than codified in dedicated how-to / methodology sections — the *Doughnut Economics* / *Mission Economy* / *Mine!* model) |

**Default behavior when uncertain:** classify new content as internal scaffolding. Easier to promote internal material to external (when it earns the slot via Pattern 2 demonstration) than to scrub publisher-facing artifacts of accumulated scaffolding.

## What's queued

**Active workstreams (in flight 2026-05-06):**

- **Darity interview** — week of May 10; phone Tue or Wed, in-person at Duke feasible Wed. Reply scheduled 2026-05-06 08:00 ET. Pre-read brief ready. **Mullen warm-intro deferred** to end of interview if conversation goes well. Outcomes feed Ch 5 (two-instrument decomposition validation), Ch 6 (Umbrellas methodology portability into extraction-community contexts), Noema (vocabulary precision), Aeon (McDowell case-walk + universality framing).
- **Colden interview pending Val DiMarzio response** — CBF / Maryland Executive Director. Response scheduled 2026-05-06 08:00 ET. Drives Ch 3 Watermen / Chesapeake fishery drafting (currently undrafted) + Noema §V third-anchor decision.
- **Aeon pitch revision** — author review continuing; title workshop continued next session. Submission target `aeon.co/pitch` first-week-of-month window (next: first week June). Revisit McDowell case-walk + universality framing after Darity interview.
- **Noema rewrite** — Path B (book-first, essay paraphrases): pivot to revised essay once Ch 1 substrate fills. Ch 1 now drafted; rewrite work cleared for activation.
- **Cold outreach pipeline** — 12 drafts sent 2026-05-05; 1 ACCEPTED (Darity); 1 DECLINED (Raworth); 9 awaiting response. Standard academic-response window 2-3 weeks before second outreach attempt.

**Framework / methodology workstreams (queued):**

- **Phase 3 — Tech Appendix v2.0.0 rebuild** (~20–30 hrs) — batches all Phase 2 + Group 1 ratifications (theorem restructures E.1a+E.1b / E.2 / E.3 / E.4 / E.5; §L methodological footnotes; notation discipline α→ξ + τ→u + C→𝒞; bibliography expansion incl. §19.5 Chesapeake fieldwork additions; absorption of `core/dimensions/` content into §C.2). Currently unblocked.
- **Phase 4 — Glossary v4 rebuild** (~3–5 hrs) — derives from terms_index v1.0.0+ per S1 schema. Sequenced after Phase 3.
- **Insight #65 framework cascade** — six-mechanism cost-severance enumeration (geographic / temporal / informational / power / normative / abundance-masking) replaces single-axis "distance" framing across Ch 1, 2, 5, 7, 9 + GuidanceDocs. Ratified 2026-05-04; cascade execution partially applied (Ch 1, 5 touches landed; further sweeping pending).
- **Insight #66 universality presentation gap** — Ch 1 plant placed; Ch 7 three-case parallel (asteroid iron / McDowell coal / commute lease) pending integration.
- **Pre-publication external review** (Insight #39) — academic-rigor pass/fail gate; triggers entire-book citations audit + Insight #63 Tier word-level collision focused rigor pass when manuscript reaches submission-ready state.

Detailed multi-thread state in [`v1.52.0`](alignment/sessions/commons-bonds-session-handoff-2026-05-06_v1.52.0.md); parallel-execution plan precedent in [`v1.49.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md) §3.

## Session workflow

When starting a new Claude session:

1. Grab the current session handoff from `alignment/sessions/` (top level).
2. Grab the session-upload set from `tools/` per [`tools/README.md`](tools/README.md).
3. Include `tools/rigor-passes/` current pass record.
4. Paste the copy-paste snippet (at the top of the current handoff) into the first message.

For parallel-session work (multiple concurrent threads): see [`v1.49.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md) §1 for thread-scoped copy-paste blocks (α architecture / β drafting / γ hygiene / δ discussion).

## Operating rules

- `manuscript/essay/Noema/` is in active rewrite under Path B (book-first; essay paraphrases). Original submission docs (`*.docx`, `*.pdf`) preserved as historical record — do not modify those. The withdrawal note + rewrite plan are working-state files. Never touch `manuscript/essay/berggruen/` (competition requires AI-free content).
- Math files stay `.html` (Ch 6, Technical Appendix, glossary). The eight-tier decomposition is RETIRED 2026-04-24 + archived 2026-04-30 (Insight #55); replaced by Cᵢ admission via Four Gates per Path F.
- Privacy: scrub personal financial specifics from external-facing outputs.
- `.DS_Store`, `.claude/`, `.chriswinn/` are in `.gitignore` — never commit.
- Worktree-isolation git workflow per WP#9: harness-issued feature branches during a session; ratified-chunk fast-forward to `main` via `git push origin HEAD:main` after each closed-ratified insight or atomic patch.
- Retirement traces per refined WP#4 (Insight #59): tiered policy by document type; canonical retirement audit-trail at [`archive/retirements/index.md`](archive/retirements/index.md).
- Content origination per WP#10: classify at origination as internal-scaffolding or external-publisher-facing; default to internal when uncertain.

## Key conceptual foundations (internal vocabulary)

- **Two-path rigor** — allocation symmetry + shield absence. Both paths must confirm.
- **Merger gate + primitiveness gate** — applied to any new or renamed dimension.
- **Commons Inversion Test (CIT)** — epistemic core; scarcity-grounded cost claims survive counterfactual inversion (CAI / CCI). Operates as a thought-experiment discrimination gate within the Four Gates admission apparatus (Path F per Insight #21 + tier-reframing). Renamed from AIT; replaces 8-tier decomposition discipline.
- **Earning-its-place + Scaffolding-vs-book-worthy** — standing book-integrity tests (Tests 28 + 29) applied at every rigor depth.
- **Canonical cases are dimension-inherent** — not incidental illustrations.
- **Single-dimension cost severance** — one-dimension cases are full instances; framework doesn't require multi-dimension co-occurrence.

## Ten dimensions (locked)

Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy.
