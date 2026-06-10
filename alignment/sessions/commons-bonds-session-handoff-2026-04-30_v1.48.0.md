# Commons Bonds — Session Handoff v1.48.0

**Date:** 2026-04-29 → 2026-04-30 (multi-day session: Phase 2 deeper-dive completion + Group 1 ratification + framework-wide notation collision audit + Working Principle #4 refinement + scaffolding cleanup pass + Tier word-level collision capture)
**Branch:** `claude/serene-franklin-1d85a7` (worktree); ratified-chunk fast-forwarded to `origin/main` per Working Principle #9
**Status:** Largest single-session theorem-audit + vocabulary-discipline batch in project history. **All 8 Phase 2 flagged items resolved** (Insights #35, #38, #40–#47 with #41/#42 collision-resolved; #51 + #52 + #53 from parallel session). **All 3 Group 1 items resolved** (Insights #56, #57, #58). **No remaining blockers for Phase 3 Tech Appendix v2.0.0 rebuild.**

---

## §1. Copy-paste block for next session orientation

> *Copy the block below into the next session's first message to orient Claude with full project context.*

```
SESSION CONTEXT — Commons Bonds (Book 1)

PROJECT IDENTITY:
This is Chris Winn's Commons Bonds project — a framework book on cost-severance / value-extraction economics. Book 1 is framework-naming + framework-establishment; Book 2 (applied-advocacy) is explicitly NOT mentioned in Book 1 per Insight #24 closed-ratified 2026-04-27.

PROJECT PATH:
The project is at /Users/c17n/commons-bonds (NOT ~/Documents/___WorkingOn/commons-bonds — that location was iCloud-syncing and corrupted the working tree; relocated 2026-04-29). All work happens in /Users/c17n/commons-bonds going forward.

GIT WORKFLOW (Working Principle #9, ratified 2026-04-29):
Worktree-isolation discipline. Harness-issued feature branches during a session; ratified-chunk fast-forward to `main` via `git push origin HEAD:main` after each closed-ratified insight or atomic patch. Replaces the prior "direct-to-main" rule. NOT push-every-commit-to-main — push happens at insight-ratification or atomic-patch boundaries.

WHERE WE ARE (post-2026-04-30 v1.48.0 session):
Massive Phase 2 + Group 1 batch closed plus framework-wide notation collision audit (Insight #55) plus Working Principle #4 refinement (Insight #59) plus scaffolding cleanup pass (Insight #60). All 8 Phase 2 flagged items resolved across Insights #35, #38, #40, #41 (E.1), #42 (E.3), #43 (Externality Tail), #44 (RCV), #45 (E.2), #47 (E.5), #51, #52, #53; 3 OPEN Group 1 items resolved (#56 Lineage Labor Cost rename; #57 Intergenerational Option Value Tier B promotion; #58 intergenerational claims Hohfeldian-dual). Working Principle #9 added (worktree-isolation git workflow). Working Principle #4 refined to tiered retirement-trace policy + canonical retirement-archive index at `archive/retirements/index.md`. Insight #63 (NEW) captures Tier word-level conceptual collision; quick-fix applied (vocabulary strategy v1.0.1 §3.1 disambiguation note); focused rigor pass queued for pre-publication external review window.

FRAMEWORK STATE (post-v1.48.0):
- Ring-1 (7 terms — UNCHANGED): Commons Bonds · Cost Severance · Severed Cost · Value Extraction · CIT · RCV · Cᵢ.
- Ring-2 changes this session: "Dynastic Labor Cost" → "Lineage Labor Cost" (Insight #56; applied across 11 files); Intergenerational Option Value PROMOTED to Tier B Ring-2 with dedicated terms_index entry (Insight #57; Tech Appendix §L footnote queued for Phase 3); Theorem E.5 "Renewable Imperative" → "Substitution Dominance" (Insight #53; Tech Appendix HTML edit batched into Phase 3 v2.0.0 rebuild).
- Theorem restructures queued for Phase 3: E.1 split into E.1a + E.1b + premises P1–P3 + citations (Insight #41); E.2 categorization (Insight #45/#51); E.3 restructure + parallel-session integration (Insight #42 + retired #54); E.4 premises A1–A4 + restructured proof (Insight #40); E.5 Substitution Dominance + Corollary E.5.1 (Insight #53).
- Notation collision discipline (Insight #55): 3 HIGH severity renames queued for Phase 3 (α → ξ for E.3 cost-function curvature; τ → u for line 6720 integration variable; C → 𝒞 script for line 398 commons-territory set); 3 MEDIUM severity ledger additions (β; σ; ρ); section-namespace + script-typography notes added to vocabulary strategy §13.

PHASE 2 + GROUP 1 — ALL RESOLVED THIS SESSION:
- Phase 2 #1 Foreclosure Bond housing-crisis collision — Insight #38 RATIFIED (Full ratify; KEEP term)
- Phase 2 #2 Cost Severance + Severed Cost Tier 2d concern — Insight #35 RATIFIED (Full ratify; KEEP terms; Ch 1 Option C bridge planned)
- Phase 2 #3.1/#3.2/#3.3/#3.4 Theorems E.1/E.3/E.5/E.2 — Insights #41, #42, #47/#53, #45/#51 RATIFIED (theorem restructures queued for Phase 3)
- Phase 2 #4 RCV acronym collision — Insight #44/#50 RATIFIED (Full ratify with §15 Q5 Ranked-Choice Voting reorder)
- Phase 2 #5 Externality Tail statistics-tail collision — Insight #43/#49 RATIFIED (both enhancements)
- Phase 2 #6 Three Ways of Counting post-rename adoption-fit — Insight #42/#48 RATIFIED (Option A)
- Phase 2 #7 Scarcity multiplier formula academic-defensibility — Insight #41/#47 RATIFIED (Full ratify; bibliography expansion)
- Phase 2 #8 RCV integrand Q(t) notation-clarity — Insight #46/#52 RATIFIED (Full ratify; comprehensive bibliography)
- Group 1.1 Dynastic → Lineage Labor Cost rename — Insight #56 RATIFIED (applied 11 files)
- Group 1.2 Intergenerational Option Value Tier B — Insight #57 RATIFIED (terms_index Ring-2 entry added; Tech Appendix §L footnote queued)
- Group 1.3 intergenerational claims redundancy — Insight #58 RATIFIED (keep both — deliberate Hohfeldian-dual; documentation-only)

WORKING PRINCIPLES STATE:
- WP#1–#8 — UNCHANGED.
- WP#9 (NEW 2026-04-29) — Worktree isolation with session-end fast-forward to main. Not push-every-commit-to-main; ratified-chunk fast-forward via `git push origin HEAD:main`.
- WP#4 (REFINED 2026-04-30 per Insight #59) — Tiered retirement-trace policy. Per-document-type table: Open insights / pending rigor passes (full traces); Ratified rigor passes frozen (full traces); Working principles + vocabulary strategy (light traces; cross-reference archive); terms_index v1.0.0+ (summary-level traces; full traces in archive); Publisher-facing artifacts (no traces per WP#8); Tier-2 archived/superseded files (header-note only). Canonical retirement-archive at `archive/retirements/index.md`.

OPEN INSIGHTS POST-v1.48.0:
- #9 Framework as decision-time severance-detection tool (raised; no decision)
- #13 Book-scope creep monitoring (ongoing discipline)
- #14 Norway's sovereign wealth fund canonical exemplar (load-bearing for Book 1 voice)
- #21 Tech Appendix + Ch 6 HTML full-rewrite (Tech Appendix v1.0.0 done; Ch 6 HTML format conversion done; structural placement of supplementary passages PENDING)
- #36 Ch 1 + Ch 3 conversational drafting session (deferred; awaits prereqs)
- #37 Scaffolding-vs-publisher-facing separation pass (OPEN; pending decision; ~3-5 hrs)
- #39 Pre-publication external review for academic-rigor pass/fail gate (OPEN; downstream gate)
- #61 README.md comprehensive update (OPEN; obvious-stale entries done in #60 follow-on; broader sweep queued)
- #62 Archive folder consolidation (OPEN; 4+ archive locations to consolidate)
- #63 (NEW) Tier word-level conceptual collision (OPEN; quick-fix B applied; focused rigor pass D queued for pre-publication external review window)

KEY MEMORY RULES TO RESPECT:
- Worktree-isolation git workflow per Working Principle #9 (NEW 2026-04-29).
- Refined Working Principle #4 (per Insight #59) — tiered retirement-trace policy + canonical retirement-archive at `archive/retirements/index.md`.
- Chapter-by-chapter prose-sweep discipline + chapter titles + section headers in scope.
- Bibliography additions: add without asking if load-bearing on ratified decision.
- Terminology regression check on every read/edit.
- Handoff chapter-length tracking section in every session handoff.
- Personal stories drafting + Path K revisit gate.
- Working Principle #8: publisher-facing artifacts scrubbed of audit-trail / scaffolding content; reasoning chains preserved exclusively in scaffolding documents.
- Multi-audience matrix discipline (12 sub-audience cells per vocabulary strategy v1.0.1 §2 + §8).
- Routine 1 (terminology-regression sentinel) + Routine 2 (pre-submission readiness, Mon/Wed/Fri) — both extended this session for notation collision discipline + Lineage Labor Cost regression.

IMMEDIATE CANDIDATE NEXT MOVES (priority order):
1. Phase 3 Tech Appendix v2.0.0 rebuild (~20-30 hrs; all blockers cleared; batches all 11+ Phase 2 + Group 1 ratifications including theorem restructures E.1a/E.1b + E.2 + E.3 + E.4 + E.5; §L methodological footnotes for Cost Severance + Foreclosure Bond + Intergenerational Option Value; notation-collision rebuild α→ξ + τ→u + C→𝒞; bibliography expansion; absorption of `core/dimensions/` content into §C.2).
2. Phase 4 Glossary v4 rebuild (~3-5 hrs; derives from terms_index per S1 schema after terms_index v1.0.0 version bump).
3. terms_index v0.1.0 → v1.0.0 version bump (template + integration sections; applies summary-level retirement traces per refined WP#4; full traces in archive).
4. Insight #37 scaffolding-vs-publisher-facing separation pass (~3-5 hrs; informs accurate word-count gaps for Ch 1 + Ch 3 drafting under Insight #36).
5. Insight #36 Ch 1 + Ch 3 conversational drafting session (after #37 completes).
6. Insight #61 README.md comprehensive update (full sweep beyond obvious-stale entries fixed in #60 follow-on).
7. Insight #62 Archive folder consolidation (when authorized; ~10-20 path updates).
8. Insight #21 Ch 6 HTML structural placement of supplementary passages (~13 placements; ~5,000 words).
9. Pre-publication external review (Insight #39 — downstream gate; not blocking until manuscript reaches submission-ready state).
10. Insight #63 focused rigor pass on Tier word-level collision (queue for pre-publication external review window).
11. Pre-publication entire-book citations + attributions audit (per author direction 2026-04-28; tie to Phase 3 Tech Appendix v2.0.0 rebuild).

START THE NEXT SESSION BY:
1. Verify primary working directory is /Users/c17n/commons-bonds.
2. Read this handoff (alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md).
3. Read alignment/commons_bonds_working_principles_v1.0.0.md (WP#9 NEW; WP#4 REFINEMENT 2026-04-30 section).
4. Read alignment/commons_bonds_vocabulary_strategy_v1.0.1.md (§3.1 Tier disambiguation note added 2026-04-30; §13 reserved-letter ledger expanded).
5. Read archive/retirements/index.md (canonical retirement-archive established by Insight #59).
6. Surface one of the candidate next moves above for author confirmation before execution.
```

---

## §2. Latest session work — detailed summary

### §2.1 Insights closed-ratified this session (16 total: #35, #38, #40–#53 with renumbering, #54 retired, #55–#60)

#### Insight #35 — Phase 2 Cost Severance + Severed Cost Tier 2d cross-political-tradition (closed-ratified 2026-04-29)

Full 12-cell multi-audience matrix at Phase 2 depth + M6 + M11 from 5 critic positions + M12 + Ch 1 Option C bridge plan verification. **No cell FAILS.** Tier 2a + Tier 2d + Lived-oppression conditional STRONG-with-enhancement / WEAK-without. Full ratify all three enhancements + KEEP terms; rename rejected (6 alternatives tested).

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md`

#### Insight #38 — Phase 2 Foreclosure Bond housing-crisis collision (closed-ratified 2026-04-29)

12-cell matrix + 2026-04-24 b1_b2_naming pass verdict re-tested against 12-cell matrix. **No cell FAILS** (Tier 1 + 2b + 2d/Lived-oppression conditional STRONG-with-enhancement; Tier 3a + 3b ADEQUATE due to inherent trauma-affect on jacket-marketing — structural property). Rename rejected (6 alternatives tested at Phase 2 depth).

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md`

#### Insight #40 — Phase 2 Theorem E.4 Integral Convergence (closed-ratified 2026-04-29)

Premise enumeration A1–A4 + restructured proof + Weitzman 2001 academic-rigor citation expansion. **Methodology template** for sibling theorem audits (#41 E.1; #42 E.3; #45 E.2; #47 E.5). Tech Appendix HTML edit batched into Phase 3 v2.0.0 rebuild.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md`

#### Insight #41 — Phase 2 #7 Scarcity multiplier formula academic-defensibility (closed-ratified 2026-04-29)

Full ratify; comprehensive bibliography expansion (Pindyck 1978 + 2008; Dasgupta-Heal 1979; Hartwick 1977; Solow 1974; Hotelling 1931). Subsequently renumbered + re-ratified as canonical Insight #47.

#### Insight #41 (canonical) — Phase 2 Theorem E.1 Structural Cost Severance (closed-ratified 2026-04-29)

E.1 split into E.1a + E.1b + premises P1–P3 + citations. **Full ratify** verdict per `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e1_structural_cost_severance_v1.0.0.md`. Tech Appendix HTML edit batched into Phase 3 v2.0.0 rebuild.

#### Insight #42 (canonical) — Phase 2 Theorem E.3 Abundance Masking (closed-ratified 2026-04-29)

Formal derivation + notation disambiguation + domain restriction + citations. Subject-collision with parallel-session Insight #54 resolved by retiring #54 in favor of canonical #42; parallel-session findings integrated into expanded #42 (3 → 4 enhancements).

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e3_abundance_masking_v1.0.0.md`

#### Insight #43/#49 — Phase 2 #5 Externality Tail statistics-distribution-tail collision (closed-ratified 2026-04-29)

Full ratify both enhancements. Stern Review 2007 lineage citation reaffirmed; statistical-tail vs externality-tail framework distinction codified. Subsequently renumbered as canonical #49 in Phase 2 sweep #41–#47 → #47–#53 renumber.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_externality_tail_statistics_collision_v1.0.0.md`

#### Insight #44/#50 — Phase 2 #4 RCV acronym collision audit (closed-ratified 2026-04-29)

Full ratify with §15 Q5 Ranked-Choice Voting reorder. RCV (Residual Commons Value) primary acronym preserved with cross-reference disambiguation note (Ranked-Choice Voting; Recoverable Commodity Value). Renumbered as canonical #50.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_rcv_acronym_collision_v1.0.0.md`

#### Insight #45/#51 — Phase 2 #3.4 Theorem E.2 Convergence of Independent Models categorization (closed-ratified 2026-04-29)

Full ratify Option A (categorization audit verdict). Sibling theorem audit using #40 methodology template. Renumbered as canonical #51.

**Rigor pass:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e2_convergence_categorization_v1.0.0.md`

#### Insight #42/#48 — Phase 2 #6 Three Ways of Counting post-rename adoption-fit (closed-ratified 2026-04-29)

Full ratify Option A. Post-Insight #31 rename (Triangulated RCV Estimation → Three Ways of Counting) verification. Renumbered as canonical #48.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_three_ways_of_counting_adoption_fit_v1.0.0.md`

#### Insight #46/#52 — Phase 2 #8 RCV integrand Q(t) notation-clarity (closed-ratified 2026-04-29)

Full ratify with comprehensive bibliography + full cross-reference scope + Phase 3 v2.0.0 rebuild batching. Q(t) Definition A.3 expansion specifies quality-vs-quantity convention. Renumbered as canonical #52.

**Rigor pass:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_rcv_integrand_q_notation_v1.0.0.md`

#### Insight #47/#53 — Phase 2 #3.3 Theorem E.5 dual-scope (closed-ratified 2026-04-29)

Full ratify Option α + β COMBINED. Author election: **"Substitution Dominance"** as rename target (replacing "Renewable Imperative") per SC8 substantive-claim accuracy weighted higher than Tier 1 + Tier 2c-climate-progressive bold-framing rhetorical force. Audience-cell scoring 8-2 favoring Dominance + register-splitting insight (chapter title carries bold framing; theorem name carries technical precision). Plus Corollary E.5.1 added. Renumbered as canonical #53.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e5_dual_scope_v1.0.0.md`

#### Insight #54 — RETIRED (2026-04-29)

Parallel-session E.3 audit subject-collision with main-session #42. Resolved by retiring #54 in favor of canonical #42; #54 findings integrated into #42 expansion. (Phase 2 sweep insights #41-#47 renumbered to #47-#53 to preserve canonical-numbering for #41 + #42 from main session.)

#### Insight #55 — Framework-wide notation collision audit (one-time retroactive sweep) (closed-ratified 2026-04-30)

Cross-document collision audit hypothesis: cross-document audits surface collisions single-document audits miss. **Verified.** 3 HIGH-severity collisions found (S = scarcity threshold in E.3 ↔ S(t) = substitutability function in E.4; α = cost-function curvature in E.3 ↔ α = elsewhere; τ = elsewhere ↔ τ = E.4 integration variable line 6720); 3 MEDIUM-severity (β; σ; ρ); 1 LOW (section-namespace overlap). Full ratify: 3 HIGH-severity renames queued for Phase 3 (α → ξ for E.3 cost-function curvature; τ → u for line 6720 integration variable; C → 𝒞 script for line 398 commons-territory set); 3 MEDIUM-severity ledger additions (β; σ; ρ); section-namespace + script-typography notes added to vocabulary strategy §13.2.1 + §13.2.2. **Scope-extension note in pass:** methodology extends to word-level conceptual collisions, not just letter notation — surfaced as Insight #63 this session. **Hygiene pass applied:** `core/decomposition/` directory archived to `archive/decomposition/` (8-tier scheme RETIRED 2026-04-24; archived per this hygiene pass).

**Rigor pass:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_framework_wide_notation_collision_audit_v1.0.0.md`

#### Insight #56 — Group 1.1 Dynastic Labor Cost → Lineage Labor Cost rename (closed-ratified 2026-04-30)

Full-depth rigor pass on 6 rename candidates: Lineage / Generational / Family / Family-Lineage / Hereditary / Intergenerational Labor Cost. **"Lineage Labor Cost"** wins decisively per multi-audience matrix STRONG/STRONGEST across 12 cells; "Lineage" carries family-line semantics without ruling-class connotation that Dynastic carried (lived-oppression reading WEAK-RISK in original). Apply sweep across 11 files: terms_index + glossary v3 + Ch 1, 6, 8 chapter drafts + healthcare-end-of-life.md + opioid-extraction-appalachia.md + indigenous-land-dispossession.md + social-security.md research case studies + Cᵢ illustrative-list.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-30_group1_1_labor_cost_naming_v1.0.0.md`

#### Insight #57 — Group 1.2 Intergenerational Option Value Tier B promotion (closed-ratified 2026-04-30)

12-cell matrix: 9 STRONG + 3 ADEQUATE (Tier 2d Socialist/communitarian + Lived-oppression — option-value reads as detached/abstract for present-suffering positions; mitigable via Tech Appendix §L methodological footnote). Tier B clean — Henry 1974 + Arrow-Fisher 1974 + Dixit-Pindyck 1994 close-fit academic anchors; framework specializes intergenerational temporal-scope axis. **Decisive criterion:** Argument-load-bearing distinction. Ch 4 *The Existence Proof* frames the entire chapter argument via option-value reasoning. Verdict (a) Tier B promotion + dedicated terms_index entry. **Implementation applied:** terms_index Ring-2 entry added (Tier B; Henry/Arrow-Fisher/Dixit-Pindyck/Howarth-Norgaard lineage). Tech Appendix §L footnote queued for Phase 3.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-30_group1_2_intergenerational_option_value_v1.0.0.md`

#### Insight #58 — Group 1.3 intergenerational claims + intergenerational obligations Hohfeldian-dual (closed-ratified 2026-04-30)

Chapter-prose audit confirms framework deploys both terms as deliberate Hohfeldian jural-correlative pair (claim ↔ obligation per Hohfeld 1913). Verdict (α) Keep both — deliberate Hohfeldian-dual; documentation-only (no sweep needed). Three going-forward references cleaned up (question-framing → verdict-framing); historical question-framing preserved in original holistic strategy rigor pass.

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-30_group1_3_intergenerational_claims_v1.0.0.md`

#### Insight #59 — Working Principle #4 refinement: Tiered retirement-trace policy + retirement-archive index (closed-ratified 2026-04-30)

5 alternative disciplines tested: (A) Status quo / (B) Tiered retirement-trace policy / (C) Retirement-archive index / (D) Sunset clause / (E) Two-tier scaffolding. Verdict: **(B) + (C) COMBINED.** WP#4 refined to per-document-type policy table; canonical retirement-archive established at `archive/retirements/index.md` with initial population (16 vocabulary retirements + 2 methodology retirements + 3 file/artifact retirements).

**Rigor pass:** `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-30_working_principle_4_refinement_v1.0.0.md`

#### Insight #60 — Scaffolding cleanup pass: refined WP#4 application + broken-paths + stale-claims sweep (closed-ratified 2026-04-30)

13-file cleanup pass per refined WP#4: 7 broken-path fixes (post-iCloud + post-archive); 5 stale current-state claims; 1 header-note addition (canonical_term_regression_audit). Plus same-day follow-on (commit `47408e1`): 3 small items + (B) vocabulary strategy §3.1 disambiguation note + (D) Insight #63 capture. Insights #61 (README maintenance) + #62 (archive folder consolidation) raised as OPEN follow-on items.

### §2.2 Working Principle #9 added — Worktree isolation with session-end fast-forward to main (ratified 2026-04-29)

Resolves tension between "direct-to-main" rule (prior WP) and harness-issued feature branches. Discipline: commit on feature branch during session; ratified-chunk fast-forward to main via `git push origin HEAD:main` after each closed-ratified insight or atomic patch. NOT push-every-commit-to-main.

**Working Principle file:** `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #9
**Memory rule:** `feedback_git_workflow.md` updated 2026-04-29.

### §2.3 Insight #63 — "Tier" word-level conceptual collision (NEW 2026-04-30; OPEN)

Surfaced during Insight #60 scaffolding cleanup pass when author asked whether "vocabulary strategy worked examples §10.3 + §10.6 (pedagogical illustrations of the Tier framework)" referenced the retired 8-tier framework. **Two distinct "Tier" concepts:** (1) 8-tier decomposition (RETIRED 2026-04-24; number-qualified Tier 1–8); (2) Vocabulary strategy four-move tier ladder (RATIFIED 2026-04-28 per Insight #27; letter-qualified Tier A–D). First word-level conceptual collision surfaced by Insight #55 cross-document-audit methodology (which explicitly extended scope to word-level collisions in its scope-extension note).

**Quick-fix (B) applied 2026-04-30:** vocabulary strategy v1.0.1 §3.1 disambiguation note codifies always-include-qualifier discipline; flags standalone "Tier framework" as ambiguous-not-to-be-used.

**Deferred decision (D):** Focused rigor pass queued for pre-publication external review window. Three options: (α) qualifier-disambiguation-suffices / (β) rename vocabulary-strategy "Tier" to alternative (Move/Class/Level A/B/C/D) / (γ) rename retired 8-tier residual references.

### §2.4 Routine updates this session

**Routine 1 — Daily terminology-regression sentinel:**
- 4 path updates: `Documents/___WorkingOn/commons-bonds` → `commons-bonds` (post-iCloud relocation)
- Pattern #8a added: Dynastic Labor Cost regression (Insight #56)
- Pattern #10 reserved-letter ledger expanded per Insight #55 (β; σ; ρ; ξ; S_threshold)

**Routine 2 — Mon/Wed/Fri pre-submission readiness audit:**
- Check #5 added: notation-collision sweep per Insight #55 4-layer notation discipline

### §2.5 Tech Appendix v1.0.0 inline reference + path fixes (this session)

- Lines 720 + 3234: Theorem name canonicalization (10 edits — fix double-Theorem naming "X Theorem (E.N)" + §10 "Theorem E.N (X)" combined producing "Theorem ... Theorem" redundancy)
- Line 3007: path update for v0.0.5_supplement.md → archive/

### §2.6 Vocabulary strategy v1.0.1 updates (this session)

- §3.1 — Tier disambiguation note (Insight #63 quick-fix)
- §13.2 — reserved-letter ledger expanded (β; σ; ρ; ξ; S_threshold added per Insight #55)
- §13.2.1 — section-namespace note added
- §13.2.2 — script-typography note added (C → 𝒞 for commons-territory set)

### §2.7 terms_index updates (this session)

- Cost Severance Phase 2 lineage expansion (Coulthard, Tuck-Yang, Federici, Mian-Sufi, etc. per Insight #35)
- Foreclosure Bond Phase 2 lineage expansion (per Insight #38)
- Cᵢ illustrative-list updates (Lineage Labor Cost replaces Dynastic Labor Cost per Insight #56)
- Intergenerational Option Value Ring-2 entry added (Tier B; Henry/Arrow-Fisher/Dixit-Pindyck/Howarth-Norgaard lineage per Insight #57)

### §2.8 New canonical artifacts this session

- `archive/retirements/index.md` (NEW; 120 lines) — canonical retirement-archive established by Insight #59 (refined WP#4 implementation)
- `archive/decomposition/eight-tier-v10.html` — relocated from `core/decomposition/` per Insight #55 hygiene pass

---

## §3. Chapter length tracking

**Refreshed 2026-04-30 (Thread δ wrap)** via `wc -w` on `manuscript/chapters/Chapter*.md` + `Chapter*.html`. Counts below are RAW (include scaffolding annotations + audit-trail content + editorial notes still in chapter drafts). **Insight #37 scaffolding-vs-publisher-facing separation pass (Thread β) will produce *publisher-facing* word counts** that may differ materially. Use the publisher-facing counts (post-#37) for submission-readiness gates; raw counts here are useful for relative-size reasoning during drafting.

| Chapter | Status | Word count (RAW 2026-04-30) | Target | Status |
|---|---|---|---|---|
| Ch 1 (untitled) | partial draft | 1,446 | 5K-6K | 🚧 partial; awaits Insight #36 Ch 1 + Ch 3 conversational drafting session |
| Ch 2 *The Miner* | drafted | 5,276 | 5K-6K | ✅ within range |
| Ch 3 (TBD waterman) | not drafted | 0 (GuidanceDoc only) | 5K-6K | ❌ not started; awaits Insight #36 |
| Ch 4 *The Existence Proof* | drafted | 4,039 | 5K-6K | ⚠ slightly under target (raw); Intergenerational Option Value Tier B promotion (Insight #57) load-bearing on chapter argument |
| Ch 5 *The Accountability Gap* | drafted | 9,506 | 5K-6K | ⚠ over target (raw); likely to compress significantly under #37 separation pass; FLAGGED pre-submission review |
| Ch 6 *Three Ways of Counting* (HTML) | drafted | 10,941 | 6K-8K | ⚠ over (post-supplementary-passages integration); Insight #21 structural placement work pending may compress |
| Ch 7 *On Other Worlds* | drafted | 7,532 | 5K-6K | ⚠ over target (raw); likely to compress under #37 separation pass |
| Ch 8 *What Things Actually Cost* | drafted | 6,027 | 5K-6K | ⚠ slightly over target (raw); Lineage Labor Cost rename applied (Insight #56) |
| Ch 9 *Pricing Honestly* | drafted | 10,327 | 5K-6K | ⚠ over target (raw); likely to compress significantly under #37 separation pass |
| Ch 10 *Common Bonds* | drafted | 7,682 | 5K-7K | ⚠ slightly over target (raw); likely to compress under #37 separation pass |

**Total drafted (RAW):** 62,776 words across 9 files (Ch 1 partial + Ch 2 + Ch 4 + Ch 5 + Ch 6 + Ch 7 + Ch 8 + Ch 9 + Ch 10).

**Notable shifts vs prior estimates (carried from v1.47.0):**
- Ch 5 / Ch 7 / Ch 9 / Ch 10 are notably larger than the prior ~5,500-5,800 estimates — accumulated scaffolding annotations during 2026-04-26 → 2026-04-30 sweeps explain the gap
- Ch 4 is slightly smaller than prior ~5,400 estimate — possibly per-sweep prose tightening that wasn't tracked, or prior estimate was high
- Ch 1 + Ch 3 unchanged (partial / not-started)
- Ch 6 within ~1K of prior ~12K estimate — supplementary integration accounted for

**Implication for Thread β:** the #37 separation pass is more load-bearing than v1.47.0 framing suggested. Several chapters are 4-5K words over target in RAW form; publisher-facing counts (post-#37) may be much closer to targets. Don't take RAW counts as evidence of over-drafting; treat them as the upper bound until #37 produces publisher-facing counts.

---

## §4. Open Insights status (post-v1.48.0) — COMPREHENSIVE LIST

### §4.1 Open insights (all 10 — explicit comprehensive list)

| # | Title | Status | Todo |
|---|---|---|---|
| **#9** | Framework as decision-time severance-detection tool (not just ex-post analysis) | raised; no decision yet | "Surface for author decision: framework's role at decision-time vs ex-post analysis." |
| **#13** | Book-scope creep monitoring (Book 1 vs Book 2 vs Book 3 boundary) | raised · ongoing monitoring discipline | Cross-cutting; not a per-term decision. Continuous discipline. |
| **#14** | Norway's sovereign wealth fund as canonical intergenerational-CS mitigation exemplar + epistemic-humility discipline | raised · load-bearing for Book 1 authorial-voice calibration | "Surface Norway treatment in Ch 4 + Accountability Bond integration discussion." |
| **#21** | Tech Appendix v0.0.5 + Chapter 6 HTML full-rewrite (dedicated session) | partially-done; Tech Appendix v1.0.0 ✓; Ch 6 HTML format conversion ✓; **structural placement of supplementary passages PENDING** | "Schedule dedicated session for Ch 6 HTML structural integration of supplementary §6.5–§6.10 passages (~13 placements; ~5,000 words)." |
| **#36** | Ch 1 + Ch 3 conversational drafting session (deferred) | OPEN; deferred until prereqs complete | "Schedule conversational drafting session for Ch 1 + Ch 3 after Insight #37 completes." |
| **#37** | Scaffolding-vs-publisher-facing separation pass + word-count recompute | OPEN; pending decision (now vs at chapter pre-submission editing) | "Decide: do Insight #37 separation pass before Ch 1 + Ch 3 drafting? (~3-5 hrs; produces accurate publisher-facing word counts informing chapter target gaps.)" |
| **#39** | Pre-publication external review for academic-rigor pass/fail gate | OPEN; pre-publication-state work; not blocking until manuscript reaches submission-ready state | "Triggers Insight #63 focused rigor pass + entire-book citations audit + manuscript external review when submission-ready state reached." |
| **#61** | README.md comprehensive update | OPEN; obvious-stale entries done in #60 follow-on; broader sweep queued | "Schedule README full sweep — cross-section consistency, regenerate from current canonical state, integrate WP#9 + refined WP#4 + Insight #63 + retirement-archive references." |
| **#62** | Archive folder consolidation | OPEN; pending decision (consolidation strategy + execution timing) | "Decide: consolidate 4+ archive locations to single canonical `archive/{technical-appendix,manuscript-chapters,tools}/` structure? (~10-20 path updates.)" |
| **#63** | "Tier" word-level conceptual collision (vocabulary-strategy four-move ladder vs retired 8-tier decomposition) | OPEN; quick-fix (B) applied 2026-04-30; focused rigor pass (D) queued for pre-publication external review window | "Focused rigor pass on Tier word-level collision — schedule for pre-publication external review window (Insight #39)." |

### §4.2 Closed-ratified this session (16 + 1 retired)

#35 (Cost Severance + Severed Cost Tier 2d); #38 (Foreclosure Bond housing-crisis collision); #40 (E.4 methodology template); #41 (E.1 Structural Cost Severance — canonical); #42 (E.3 Abundance Masking — canonical, expanded with parallel-session findings); #43/#49 (Externality Tail); #44/#50 (RCV acronym); #45/#51 (E.2 categorization); #46/#52 (RCV integrand Q(t)); #47 (scarcity multiplier — early-numbering); #47/#53 (E.5 Substitution Dominance); #42/#48 (Three Ways of Counting adoption-fit); #54 RETIRED (subject-collision with #42); #55 (notation collision audit); #56 (Lineage Labor Cost rename); #57 (Intergenerational Option Value Tier B); #58 (intergenerational claims Hohfeldian-dual); #59 (WP#4 refinement); #60 (scaffolding cleanup pass).

---

## §5. Pending work — priority order (COMPREHENSIVE)

### §5.1 No remaining blockers for Phase 3

All previous Phase 3 prerequisites cleared this session:
- ✅ Phase 2 deeper-dive on 8 flagged items — DONE (#35, #38, #40–#53)
- ✅ Group 1 ratification (3 items) — DONE (#56, #57, #58)
- ✅ Notation collision audit (Insight #55) — DONE (3 HIGH renames queued for Phase 3)
- ✅ Refined WP#4 (Insight #59) — DONE (terms_index v1.0.0 version bump can apply summary-level traces cleanly)

### §5.2 Implementation pending (ratified but not yet applied)

**Refined WP#4 (Insight #59) implementation:**
- terms_index v0.1.0 → v1.0.0 version bump applies summary-level retirement traces (full traces moved to `archive/retirements/index.md`)
- Vocabulary strategy v1.0.1 §6 + §7 + §13 light-trace migration to cross-reference archive
- Working principles body cleanup (small; some inline traces could cross-reference archive)

**Notation discipline (Insight #55) implementation in Tech Appendix v2.0.0 rebuild:**
- α → ξ for E.3 cost-function curvature (HIGH)
- τ → u for line 6720 integration variable (HIGH)
- C → 𝒞 (script C) for line 398 commons-territory set (HIGH)
- β + σ + ρ ledger entries (MEDIUM — already applied in vocab strategy v1.0.1 §13.2)

**Theorem restructures queued for Phase 3 Tech Appendix v2.0.0 rebuild:**
- E.1 split into E.1a + E.1b + premises P1–P3 + citations (Insight #41)
- E.2 categorization (Insight #45/#51)
- E.3 restructure + parallel-session integration (Insight #42; replaces retired #54)
- E.4 premises A1–A4 + restructured proof (Insight #40)
- E.5 Renewable Imperative → Substitution Dominance + Corollary E.5.1 (Insight #53)

**§L methodological footnotes (Phase 3 batched):**
- Cost Severance + Severed Cost (Insight #35)
- Foreclosure Bond (Insight #38)
- Intergenerational Option Value (Insight #57)

**Mathematical apparatus (Phase 3 batched):**
- RCV integrand Definition A.3 expansion (Insight #52 Q(t) convention)
- Scarcity multiplier formula bibliography expansion (Insight #47)
- Externality Tail enhancements (Insight #49)
- Three Ways of Counting adoption-fit (Insight #48)
- RCV acronym disambiguation (Insight #50)

**Content absorption (Phase 3 batched):**
- core/dimensions/ content into §C.2 (then archive directory per Insight #62 candidate)

**Bibliography expansion (combined this session — Phase 3 batched):**
- Coase 1960; Pigou 1920; Brown Weiss 1989; Howarth & Norgaard 1990 + 1992; Stern Review 2007; Hartwick 1977; Solow 1974; Hotelling 1931; Weitzman 2001; Mian-Sufi 2014; Rothstein 2017; Taylor 2019; Coates 2014; Hyman 2011; Sugrue 1996; Desmond 2016; Wolfe 1999; Coulthard 2014; Tuck-Yang 2012; Federici 2004; Patel-Moore 2017; Hickel 2020; Darity-Mullen 2020; Anderson 2017; Pettit 1997; Demsetz 1967; Marshall 1890; Hamilton 2009; Kilian 2009; Pindyck 1978 + 2008; Dasgupta-Heal 1979; Barnosky et al. 2012; Lenton et al. 2008; Henry 1974; Arrow & Fisher 1974; Caudill 1962; Bell 2009; Becker 1981; Hohfeld 1913; Royden 1988 / Folland 1999 / Rudin 1987 (real analysis).

### §5.3 Insight-tracked OPEN work (with todo items)

| Item | Insight | Priority | Estimate |
|---|---|---|---|
| Schedule dedicated session for Ch 6 HTML structural integration of supplementary §6.5–§6.10 | #21 | medium | ~13 placements; ~5,000 words |
| Schedule conversational drafting session for Ch 1 + Ch 3 (after #37) | #36 | high | dedicated session |
| Decide: do scaffolding-vs-publisher-facing separation pass now vs at chapter pre-submission? | #37 | high | ~3-5 hrs |
| Schedule pre-publication external review (when submission-ready) | #39 | downstream | TBD |
| README.md full sweep — cross-section consistency, regenerate from canonical state | #61 | medium | ~1-2 hrs |
| Archive folder consolidation decision + execution | #62 | low | ~10-20 path updates |
| Focused rigor pass on Tier word-level collision (queued for #39 window) | #63 | low | dedicated rigor pass |

### §5.4 Architectural / scaffolding work

- terms_index v0.1.0 → v1.0.0 version bump (template + integration sections; applies summary-level retirement traces per refined WP#4)
- Phase 3 Tech Appendix v2.0.0 rebuild (~20-30 hrs; batches all 11+ Phase 2 + Group 1 ratifications; resolves scaffolding-scrub + multi-audience attribution-discipline + theorem academic-rigor audit + notation discipline + bibliography expansion in one pass)
- Phase 4 Glossary v4 rebuild (~3-5 hrs; derives from terms_index per S1 schema after terms_index v1.0.0)
- 4 nuanced Ring-2 entries: intergenerational cost severance lowercase; Temporal CS hybrid; Spatial CS hybrid; Accountability Bond UPDATE sub-instruments (B₁ + B₂ rendering fields)
- AIT → CIT regression cleanup in terms_index (line 1395 + Abundance Masking entry historical/current judgment)

### §5.5 Drafting work

- Ch 6 supplementary-passage structural integration (per Insight #21; ~13 placements; ~5,000 words)
- Ch 1 personal stories drafting cycle (per Insight #36)
- Ch 3 (waterman) draft (largest content gap; per Insight #36)
- Ch 5 pre-submission review (FLAGGED)
- Ch 2 interviews (3 INTERVIEW NEEDED placeholders per inventory)

### §5.6 Pre-publication audits

- Pre-publication entire-book citations + attributions audit (per author direction 2026-04-28; same rigor discipline as Hotelling Identity §12; ~10-30 hrs depending on scope; tie to Phase 3 Tech Appendix v2.0.0 rebuild)
- Pre-publication external review (Insight #39)
- Tier word-level collision focused rigor pass (Insight #63; bundle with #39)

---

## §6. Working Principles state (post-v1.48.0)

| # | Principle | Status |
|---|---|---|
| 1 | Vocabulary parsimony | UNCHANGED |
| 2 | Multi-audience matrix discipline | UNCHANGED |
| 3 | Two-path rigor (allocation symmetry + shield absence) | UNCHANGED |
| 4 | Retirement-trace discipline | **REFINED 2026-04-30 (Insight #59)** — tiered policy + canonical retirement-archive at `archive/retirements/index.md` |
| 5 | Merger gate + primitiveness gate | UNCHANGED |
| 6 | M12 attribution-honesty | UNCHANGED |
| 7 | Earning-its-place + Scaffolding-vs-book-worthy | UNCHANGED |
| 8 | Publisher-facing artifacts scrubbed of scaffolding | UNCHANGED |
| 9 | **Worktree isolation with session-end fast-forward to main** | **NEW 2026-04-29** |

---

## §7. Commits this session (chronological since v1.47.0 baseline `e2796c6`)

(All on feature branches; ratified-chunk fast-forwarded to `origin/main` per WP#9)

- `b8db72d` — Vocabulary strategy v1.0.1 file rename + version-marker sweep (cleanup of 304bff9)
- `9b614ae` — Working Principle #9 RATIFIED 2026-04-29 — Worktree isolation with session-end fast-forward to main
- `414a613` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Cost Severance + Severed Cost Tier 2d cross-political-tradition verification
- `a3a6e5e` — Insight #35 RATIFIED 2026-04-29 — Phase 2 Cost Severance + Severed Cost Tier 2d (Full ratify) + Insight #36 + #37 OPEN
- `9be55ef` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Foreclosure Bond housing-crisis connotation collision
- `1c0b11a` — Insight #38 RATIFIED 2026-04-29 — Phase 2 Foreclosure Bond housing-crisis collision (Full ratify)
- `d4fbc23` — Insight #39 OPEN — Pre-publication external review for academic-rigor pass/fail gate
- `b58bd70` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Theorem E.4 Integral Convergence (academic-rigor depth audit)
- `ea7655e` — Insight #40 RATIFIED 2026-04-29 — Phase 2 Theorem E.4 Integral Convergence (Full ratify)
- `a5c02e0` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — RCV integrand Q(t) notation-clarity (academic-rigor depth audit)
- `90af685` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Scarcity multiplier formula academic-defensibility (P2#7)
- `064ade3` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Three Ways of Counting post-rename adoption-fit verification (P2#6)
- `7f8faa5` — Insight #41 RATIFIED 2026-04-29 — Phase 2 #7 Scarcity multiplier formula academic-defensibility (Full ratify) [later renumbered #47]
- `66eb7e1` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Externality Tail statistics-distribution-tail collision audit (P2#5)
- `4cdb987` — Insight #42 RATIFIED 2026-04-29 — Phase 2 #6 Three Ways of Counting post-rename adoption-fit (Full ratify Option A) [later renumbered #48]
- `e6a028f` — Insight #43 RATIFIED 2026-04-29 — Phase 2 #5 Externality Tail statistics-distribution-tail collision (Full ratify both enhancements) [later renumbered #49]
- `6555bae` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — RCV acronym collision audit (P2#4 — final in reverse-priority sweep)
- `dabf412` — Insight #44 RATIFIED 2026-04-29 — Phase 2 #4 RCV acronym collision audit (Full ratify with §15 Q5 Ranked-Choice Voting reorder) [later renumbered #50]
- `5e5ed7f` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Theorem E.2 Convergence of Independent Models categorization audit (P2#3.4)
- `4859aa7` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Theorem E.3 Abundance Masking circular-proof audit (P2#3.2)
- `9e61e08` — Insight #45 RATIFIED 2026-04-29 — Phase 2 #3.4 Theorem E.2 categorization audit (Full ratify Option A) [later renumbered #51]
- `da5656e` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Theorem E.1 Structural Cost Severance (academic-rigor depth audit)
- `90cd3ef` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Theorem E.5 dual-scope audit: vocabulary collision + proof-structure (P2#3.3)
- `bece107` — Insight #41 RATIFIED 2026-04-29 — Phase 2 Theorem E.1 Structural Cost Severance (Full ratify: split + premises + scope + citations)
- `91a4d73` — Insight #46 RATIFIED 2026-04-29 — Phase 2 #8 RCV integrand Q(t) notation-clarity (Full ratify) [later renumbered #52]
- `35e3823` — Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED] — Theorem E.3 Abundance Masking (academic-rigor depth audit)
- `dcafa45` — Insight #42 RATIFIED 2026-04-29 — Phase 2 Theorem E.3 Abundance Masking (Full ratify)
- `b38651e` — Insight #47 RATIFIED 2026-04-29 — Phase 2 #3.3 Theorem E.5 dual-scope (Renewable Imperative → Substitution Dominance + Corollary E.5.1) [later renumbered #53]
- `636c589` — Renumber Phase 2 sweep insights #41-#47 → #47-#53 (Insight #41 collision resolution)
- `8971a8c` — Insight #54 RATIFIED 2026-04-29 — Phase 2 #3.2 Theorem E.3 Abundance Masking circular-proof + parallel-session findings integration
- `8e72e1c` — Merge remote-tracking branch 'origin/main' into claude/sharp-germain-574f2a
- `f4a46c8` — Subject-collision resolution: retire Insight #54 in favor of canonical #42 (other session's E.3 audit on main)
- `7e72f6f` — Insight #42 expanded post-ratification — Parallel-session E.3 findings integrated (3 → 4 enhancements)
- `74dcf79` — 4-layer notation discipline implementation per Insight #55 (Routines 1 + 2 extended; Insight #55 OPEN; Vocabulary strategy v1.0.1 §13 added)
- `25f36f9` — Insight #55 framework-wide notation collision audit v1.0.0 [PROPOSED] — 3 HIGH + 3 MEDIUM + 1 LOW findings
- `45e9c16` — Insight #55 RATIFIED 2026-04-30 — Framework-wide notation collision audit (Full ratify)
- `dac1ab3` — Archive core/decomposition + rename Insight #36 (Ch 1 + Ch 2 → Ch 1 + Ch 3) + cross-reference + path updates
- `e869b42` — Double-Theorem cleanup — fix Tech Appendix v1.0.0 internal naming inconsistency + sweep scaffolding for going-forward consistency
- `650d209` — Group 1.1 Labor Cost Naming full-depth rigor pass v1.0.0 [PROPOSED] — Lineage Labor Cost recommended over 6 other rename candidates
- `f046401` — Group 1 batch — Insight #56 RATIFIED 2026-04-30 (Lineage Labor Cost rename) + Group 1.2 + 1.3 rigor passes [PROPOSED]
- `a6b6d07` — Group 1.2 + 1.3 RATIFIED 2026-04-30 — Insights #57 + #58 closed-ratified (Intergenerational Option Value Tier B promotion + intergenerational claims Hohfeldian-dual)
- `fed1906` — Cleanup — sweep "intergenerational claims redundancy" question-framing → "Hohfeldian-dual" verdict-framing in going-forward references (3 instances)
- `8aa74fd` — Insight #59 RATIFIED 2026-04-30 — Working Principle #4 refinement: Tiered retirement-trace policy + retirement-archive index
- `3bf6aac` — Insight #60 RATIFIED 2026-04-30 — Scaffolding cleanup pass: refined WP#4 application + broken-paths + stale-claims sweep + Insights #61 + #62 OPEN
- `47408e1` — Insight #60 follow-on cleanup + Insight #63 capture (Tier collision)

---

## §8. iCloud-prevention reminder (continued from v1.47.0)

Project remains at `/Users/c17n/commons-bonds`. Do NOT move back to `~/Documents/` or `~/Desktop/` (both default-iCloud-synced in macOS). Safe locations: `~/commons-bonds`, `~/Projects/`, `~/code/`, `~/Repos/`, `/Volumes/`. Alternative: `.nosync` suffix is the macOS-recognized iCloud-exclusion pattern.

---

**End of session handoff v1.48.0.**

**Next session start: verify primary working directory is `/Users/c17n/commons-bonds`, read this handoff, then surface a candidate next move from §1 priority list.**
