# Commons Bonds — Housekeeping Review

**Date:** 2026-04-22
**Version:** 1.0.0
**Status:** Proposed — for Chris's review and action decisions.
**Scope:** Folder-by-folder deep-dive of the local project tree, flagging canonical / superseded / rename-propagation-target / housekeeping items.
**Referenced from:** `alignment/sessions/commons-bonds-session-handoff-2026-04-22_v1_28_0.html` TOP PRIORITY §7.
**Context for the review:** The v1.28.0 session ratified container-term "dimensions" (from "layers") and pair-rename {Atmospheric → Habitability, Ecological → Ecosystem}. Full naming cohort still in progress (Demographic, Priority-2 cohort, Priority-3 confirm pending). This review anticipates the propagation sweep and catalogs supporting housekeeping.

---

## 1. Method

For each folder and subfolder: inventoried contents, read key files to determine canonical vs. superseded status, cross-referenced against the v1.27.0 → v1.28.0 canonical state. Findings are structured by action-type:

- **KEEP** — canonical, no action (may still need eventual rename-propagation patching).
- **PATCH** — active canonical file that needs rename-propagation updates (layer→dimension, etc.).
- **ARCHIVE** — superseded by later canonical version; move to an archive location.
- **NORMALIZE** — naming / permission / metadata inconsistency worth fixing.
- **INVESTIGATE** — unclear status; needs a specific decision before action.
- **DELETE** — duplicates, `.DS_Store`, unambiguous cleanup.

---

## 2. Cross-cutting observations (apply broadly)

### 2.1 `.DS_Store` files throughout the tree

Every subdirectory has a `.DS_Store` (macOS metadata file). Several are tracked in git per earlier status check. **Recommended action:** add `.DS_Store` to `.gitignore` at project root, then `git rm --cached` all existing `.DS_Store` files. Standard macOS hygiene — low risk.

### 2.2 Google-Drive-export artifacts with " NN" suffix

Several files have trailing-space-number suffixes like `commons-bonds-success-criteria 11.html`, `commons-bonds-vocabulary-additions 13.html`, `commons - consider including 9.html`, `commons-bonds-villain-analysis 15.html`, `commons-bonds-two-book-strategic-analysis 10.html`. These are Google Drive's auto-numbering when multiple exports hit the same filename. **Recommended action:** rename to drop the space-number suffix where the file is canonical; leave as-is in archive locations.

### 2.3 File-permission anomaly — 0600 vs 0644

A set of files have mode 0600 (owner-only) vs. the project default 0644: several `alignment/decisions/` files, Ch. 1 / 1a / 3 guidance docs, `core/decomposition/eight-tier-v10.html`, `archive/commons_bonds_chapter_assessment.md`, `alignment/commons-bonds-handoff-template.html`, some `workstreams/` files, `tools/archive/preferences_privacy_addendum_v1_0_1.md`. **Recommended action:** verify whether this is intentional privacy-sensitive marking or accidental (the pattern looks more random than deliberate). If accidental, normalize to 0644 for consistency with git-tracked content.

### 2.4 Migration-era documents (April 19–20, 2026) are largely superseded

A cluster of documents from the Google-Drive → GitHub migration window describe a *planned* structure that was only partially implemented, or workstream state that has been consumed by the rigor-protocol / naming-cohort work. These are lineage-valuable but should move to archive so they stop appearing as "active canonical" in search.

### 2.5 Rename-propagation targets

Any file containing "layer," "Atmospheric," "Ecological," or (eventually) the other 5 priority-2 old names will need patching once the naming cohort completes. This review flags which files contain active canonical content (needs patching) vs. archive content (patch not needed).

---

## 3. `tools/` + `tools/archive/`

### 3.1 `tools/` (active canonical working docs)

| File | Status | Action |
|---|---|---|
| `.DS_Store` | macOS artifact | **DELETE + .gitignore** |
| `.gitkeep` | standard | KEEP |
| `claude_prefs.md` | Active canonical preferences — **contains outdated "layer" terminology** | **PATCH** (rename propagation: §3 "layer" → "dimension"; update operating core block to match v1.28.0 handoff) |
| `commons_bonds_abundance_layers_v1_0_0.md` | Superseded by retitle + patch 2026-04-22 | **DONE** — retitled to `commons_bonds_abundance_dimensions_v1_1_0.md`; §2 dimension-name propagation carried (Habitability, Kindred, Ecosystem locked); §5.5 availability-absence severity-marker + §5.6 lived-experience-canonical-case methodology still pending for a follow-up v1.1.1 patch. |
| `commons_bonds_book_scope_v1_0_3.md` | Canonical Book One scope | **PATCH** (rename propagation throughout; Part 3 audit target) |
| `commons_bonds_character_suite_vs_layers_triage_v1_0_0.md` | Triage file — used as input to Part 2 rigor pass | KEEP (history value); rename to `..._vs_dimensions_triage...` optional |
| `commons_bonds_guiding_constraints_v1_0_0.md` | Canonical Group D/E inputs | **PATCH** (terminology: layer → dimension) |
| `commons_bonds_layer_tier_stress_test_1_0_0.md` | **Superseded** — dated 2026-04-20, references rigor protocol v1.1.0 and pre-10-dimension state; its findings (Atmospheric → Life-support candidate, Geographic → Spatial surface) absorbed into later work | **ARCHIVE** (to `tools/archive/`) |
| `commons_bonds_rigor_pass_2026-04-22_v1_0_0.md` | Part 1 pass record. Currently listed in `tools/archive/` **AND** referenced as canonical in abundance-layers doc §1 — a contradiction | **INVESTIGATE** (see §3.2 below) |
| `commons_bonds_rigor_pass_2026-04-22_v1_0_1.md` | Part 2 pass record (promoted from Downloads/ this session — first worktree-write) | KEEP canonical |
| `commons_bonds_rigor_protocol_v1.2.2.md` | Canonical rigor protocol | **PATCH** (layer → dimension throughout; bump to v1.2.2 for terminology patch only) |
| `commons_bonds_rigor_vs_layers_triage_v1_0_0.md` | Triage file — used as input to Part 2 | KEEP (history value); optional rename |
| `userMemories_proposed_2026-04-21_v1_0_1.md` | **Proposed** — personal-context memory file; status unclear; some content already stale (references Tier 2a "to be verified" — may already be done; references eight-tier terminology pre-dimensions) | **INVESTIGATE** — is this proposed-for-Claude-to-adopt as preference block? If ratified, apply + archive; if not ratified, archive-as-proposed. |

### 3.2 `tools/archive/`

| File | Status | Action |
|---|---|---|
| `commons_bonds_book_scope_v1_0_0.md` | Superseded by v1.0.3 | KEEP (archived lineage) |
| `commons_bonds_book_scope_v1_0_1.md` | Superseded by v1.0.3 | KEEP (archived lineage) |
| `commons_bonds_book_scope_v1_0_2.md` | Superseded by v1.0.3 | KEEP (archived lineage) |
| `commons_bonds_rigor_pass_2026-04-21_v1_0_0.md` | v1.24.0 session's rigor pass record | KEEP (archived lineage) |
| `commons_bonds_rigor_pass_2026-04-22_v1_0_0.md` | Part 1 pass record — **contradiction flag** | **INVESTIGATE** — this is referenced as "canonical" in multiple places (abundance layers doc §1, rigor protocol v1.2.1 §5.2 footnote, Part 2 pass record references). Should be in `tools/` or it was prematurely archived. |
| `commons_bonds_rigor_protocol_1_1_0.md` | Superseded by v1.2.1 | KEEP (archived lineage) |
| `commons_bonds_rigor_protocol_v1_0_1.md` | Superseded by v1.2.1 | KEEP (archived lineage) |
| `commons_bonds_rigor_protocol_v1_2_0.md` | Superseded by v1.2.1 | KEEP (archived lineage) |
| `preferences_privacy_addendum_v1_0_1.md` | Mode 0600 — small privacy-rule draft | **INVESTIGATE** permission + status (is content consumed into `claude_prefs.md` already? If so KEEP archived; if pending, PATCH and promote.) |

**Action priority for tools/:** Promote Part 1 rigor pass (v1_0_0) back to `tools/` (or confirm it's canonically archived and patch the references that call it "canonical"). PATCH `claude_prefs.md` with v1.28.0 dimensions + operating-core updates. ARCHIVE `commons_bonds_layer_tier_stress_test_1_0_0.md`. Decide `userMemories_proposed_2026-04-21_v1_0_1.md` status.

---

## 4. `research/` + subfolders

### 4.1 `research/` (top-level)

Only `.DS_Store` and `.gitkeep`. **DELETE `.DS_Store`**.

### 4.2 `research/methodology/`

| File | Status | Action |
|---|---|---|
| `commons_bonds_full_economy_simulation.html` (2026-04-19, 15KB) | Pre-migration simulation doc; likely Book Two territory per workstream 10's separation guidance | **INVESTIGATE** — is this still Book One relevant, or does it belong in `archive/_One Day Maybe/`? Read content to determine. |

### 4.3 `research/case-studies/` — **EMPTY** (only placeholder)

Per `repository-structure.md`, this was intended to hold Appalachian-coal, Deepwater-Horizon, Libby-vermiculite, Norway-SWF case-study docs. **INVESTIGATE** — was this skipped intentionally (case-study material lives inline in chapter drafts), or is it pending content? If skipped, remove subfolder; if pending, keep as intentional staging.

### 4.4 `research/literature/` — **EMPTY** (only placeholder)

Per `repository-structure.md`, intended for literature-review content. Same INVESTIGATE question as case-studies.

**Action priority for research/:** Decide whether empty subfolders are intentional-staging (keep) or abandoned-plan (remove). If kept, add README.md to each describing intended content. Verify `commons_bonds_full_economy_simulation.html` scope.

---

## 5. `publishing/` + `publishing/targets/`

### 5.1 `publishing/`

| File | Status | Action |
|---|---|---|
| `.DS_Store` | macOS artifact | **DELETE + .gitignore** |
| `CommonsBondsPublishingStrategyConsolidated.html` (2026-04-20, 35KB) | Canonical publishing strategy — referenced in `guiding_constraints_v1_0_0.md` | KEEP canonical |
| `CommonsBonds_BookOneCommonsBondsPathBookTwo.html` (2026-04-20, 78KB) | Book One / Book Two path document | KEEP canonical; **INVESTIGATE** — does content still reflect current Book One scope (v1.0.3) and the 10-dimension framework? Likely needs a Part 3-era update. |
| `commons-bonds-success-criteria 11.html` (2026-04-18) | Earlier success-criteria doc; now superseded by `guiding_constraints_v1_0_0.md` §1 | **ARCHIVE** (to `publishing/archive/` or `tools/archive/`) after verifying content captured. Drop " 11" suffix if kept. |
| `commons_bonds_critical_impact_assessment.html` (2026-04-18, 11KB) | Pre-migration impact assessment; unclear current relevance | **INVESTIGATE** status — is this still active or should it be archived? |

### 5.2 `publishing/targets/` — **EMPTY** (only `.DS_Store`)

Per `repository-structure.md`, intended for noema-submission, boston-review-plan, academic-journals. Empty. **INVESTIGATE** — is this deliberately empty (targeting info lives in `CommonsBondsPublishingStrategyConsolidated.html`), or is it pending content?

**Action priority for publishing/:** Archive `commons-bonds-success-criteria 11.html`. Decide `commons_bonds_critical_impact_assessment.html` status. Confirm `CommonsBonds_BookOneCommonsBondsPathBookTwo.html` is still current or queue for Part 3 update. Decide `targets/` intent.

---

## 6. `manuscript/` + `manuscript/chapters/` + `manuscript/essay/`

### 6.1 `manuscript/` (top-level)

Only `.DS_Store` and `.gitkeep`. **DELETE `.DS_Store`**.

### 6.2 `manuscript/chapters/` — 19 files (substantial)

**Draft chapters (8):**

| Chapter | File | Size | Status | Action |
|---|---|---|---|---|
| 2 | `Chapter__2_TheMiner__Draft.md` | 27KB | Canonical draft | **PATCH** (rename propagation) |
| 4 | `Chapter__4_THEEXISTENCEPROOF__Draft.md` | 19KB | Canonical draft | **PATCH** (rename propagation) |
| 5 | `Chapter__5_THEACCOUNTABILITYGAP__Draft.md` | 18KB | Canonical draft | **PATCH** (rename propagation) |
| 6 | `Chapter__6_ThreeWaysofCounting__Draft.html` | 45KB | Canonical draft (.html per math content) | **PATCH** (rename propagation + verify MathJax rendering after) |
| 7 | `Chapter__7_TheColonyAdministrator__Draft.md` | 31KB | Canonical draft | **PATCH** (rename propagation; Ch. 7 is the off-Earth layer-stripping exemplar; possibly 9–10 dimensions activate per handoff queue item) |
| 8 | `Chapter__8_WhatThingsActuallyCost_Draft.md` | 29KB | Canonical draft | **PATCH** (rename propagation; Ch. 8 coal integrates Irreversibility-as-severity content per v1.28.0) |
| 9 | `Chapter__9_TheRenewableImperative__Draft.md` | 41KB | Canonical draft | **PATCH** (rename propagation; Ch. 9 absorbs civilization-scale availability-absence territory per v1.28.0) |
| 10 | `Chapter_10_CommonBonds__Draft.md` | 38KB | Canonical draft | **PATCH** (rename propagation) |

**Guidance docs (10):**

| Chapter | File | Perm | Status | Action |
|---|---|---|---|---|
| 1 | `Chapter__1___GuidanceDoc.md` | 0600 | Guidance doc; **draft pending** | **NORMALIZE** permission to 0644 if not intentional; **PATCH** (rename propagation) |
| 1a | `Chapter__1a__GuidanceDoc.md` | 0600 | Secondary/sub-chapter guidance | **INVESTIGATE** — is the 1/1a split intentional (two-part chapter) or a refactor-in-progress? **NORMALIZE** permission. **PATCH**. |
| 2 | `Chapter__2___GuidanceDoc.md` | 0644 | Canonical | **PATCH** |
| 3 | `Chapter__3___GuidanceDoc.md` | 0600 | Guidance doc; **draft pending** | **NORMALIZE** permission; **PATCH** |
| 4 | `Chapter__4___GuidanceDoc.md` | 0644 | Canonical | **PATCH** |
| 5 | `Chapter__5___Guidance.md` | 0644 | Canonical | **NORMALIZE name** — should be `Chapter__5___GuidanceDoc.md` for consistency; **PATCH** |
| 6 | `Chapter__6___GuidanceDoc.md` | 0644 | Canonical (37KB — largest guidance doc) | **PATCH** |
| 7 | `Chapter__7___GuidanceDoc.md` | 0644 | Canonical | **PATCH** |
| 9 | `Chapter__9___GuidanceDoc.md` | 0644 | Canonical | **PATCH** |
| 10 | `Chapter_10___GuidanceDoc.md` | 0644 | Canonical; note single-underscore pattern differs slightly | **NORMALIZE name** if double-underscore is the standard; **PATCH** |

**Missing:** Ch. 8 has no guidance doc. **INVESTIGATE** — intentional (draft preceded guidance) or missing?

**Special files:**

| File | Status | Action |
|---|---|---|
| `_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md` | Canonical | **PATCH** (if it uses dimension vocabulary) |
| `_Dedication.md` | Canonical | KEEP (likely no dimension vocabulary) |

**Action priority for chapters/:** This is the big-ticket rename propagation work — 8 drafts + 10 guidance docs + author's note. Grep-based sweep post-cohort. Separately, normalize Ch. 5 guidance filename, verify Ch. 1/1a/3 permission intent, verify Ch. 1a split intent, decide Ch. 8 guidance status.

### 6.3 `manuscript/essay/`

| Subfolder | Status | Action |
|---|---|---|
| `Noema/` (5 files — .pdf + .docx) | **HARD RULE: do not touch per watch items** | KEEP untouched |
| `Berggruen Institute - Essay/` (1 .docx) | **HARD RULE: do not touch per watch items** | KEEP untouched |
| `.DS_Store` | macOS artifact | **DELETE + .gitignore** |

---

## 7. `core/` + subfolders

### 7.1 `core/` (top-level)

| File | Status | Action |
|---|---|---|
| `.DS_Store` | macOS artifact | **DELETE + .gitignore** |
| `commons_bonds_integrated_framework.html` (2026-04-20, 19KB) | **Master framework document** — Workstream 09 was to audit/potentially retire this | **INVESTIGATE** — is this still canonical or has its content been consumed? The rigor-protocol-centric architecture (protocol v1.2.1, abundance-layers doc) may have superseded it. Read fully + cross-check; likely ARCHIVE candidate. |

### 7.2 `core/decomposition/`

| File | Perm | Status | Action |
|---|---|---|---|
| `.DS_Store` | | macOS artifact | **DELETE** |
| `eight-tier-v10.html` | 0600 | Canonical eight-tier decomposition | **NORMALIZE** permission; **PATCH** (rename propagation if uses layer terminology) |
| `error-out-v10.html` | 0644 | Referenced in watch items ("math files stay .html"); active canonical | **PATCH** (rename propagation) |

### 7.3 `core/glossary/`

| File | Status | Action |
|---|---|---|
| `commons-bonds-vocabulary-additions 13.html` (2026-04-18) | Pre-migration vocabulary-additions doc; status unclear — may have been consumed into `commons_bonds_updated_glossary_v2.html` | **INVESTIGATE** — if content absorbed, archive; drop " 13" suffix if kept |
| `commons_bonds_updated_glossary_v2.html` (2026-04-20, 26KB, 0600 perm) | Canonical glossary v2 | **NORMALIZE** permission; **PATCH** (rename propagation — substantial; glossary is dense vocabulary territory) |

### 7.4 `core/technical-appendix/`

| File | Status | Action |
|---|---|---|
| `.DS_Store` | macOS artifact | **DELETE** |
| `TechnicalAppendix_v0.0.2.html` (2026-04-20, 123KB) | Canonical technical appendix; v0.0.2 metadata inconsistency flagged in v1.28.0 deferred queue | **PATCH** (rename propagation; resolve v0.0.2 metadata inconsistency) |

**Action priority for core/:** Decide `commons_bonds_integrated_framework.html` status (likely archive). Normalize file permissions on `eight-tier-v10.html` and glossary v2. Archive `commons-bonds-vocabulary-additions 13.html` if consumed. Major PATCH target: the glossary and technical appendix both carry the framework's formal vocabulary — the rename propagation there is load-bearing.

---

## 8. `archive/` + subfolders

### 8.1 `archive/` (top-level)

| File | Status | Action |
|---|---|---|
| `.DS_Store` | macOS artifact | **DELETE + .gitignore** |
| `.gitkeep` | standard | KEEP |
| `commons-bonds-villain-analysis 15.html` | Pre-migration villain-analysis doc | KEEP (already archived); drop " 15" suffix optional |
| `commons_bonds_chapter_assessment.md` (0600 perm) | Chapter-by-chapter assessment doc; superseded by current chapter draft state | KEEP archived; **NORMALIZE** permission (archive content shouldn't need 0600) |

### 8.2 `archive/Consider Including/`

10 files, all dated 2026-04-18, named with "consider including N" suffixes. These are Chris's pre-migration brainstorm / session-note dumps from the Google Drive era.

| File | Notes |
|---|---|
| `Commons Bonds - Nigeria Contrast Case...docx` | Nigeria case content for Ch. 5 per workstream 05 |
| `commons - consider including 9.html` AND `commons - consider including 12.html` | Per workstream 10: these are EXACT DUPLICATES (Social Security case) — confirmed. The workstream 10 plan said delete 9.html. **DELETE** one of them. |
| `commons_bonds_economic_theory_reference - consider including 6.html` | Economic theory reference; workstream 10 scheduled this for `/Research/` — but it's still here. **MOVE** to `research/literature/`? |
| `commons_bonds_new_material_april_19_2026...2.html` | Session dump; status unclear |
| `commons_bonds_new_material_from_sociology_chat...4.html` | Sociology-chat session dump |
| `commons_bonds_satellite_idea_delegitimization - consider including 8.html` | Satellite essay per workstream 10; scheduled for `_One Day Maybe/Satellite-Essays/` |
| `commons_bonds_session_notes_april_19_2026 - Consider Including 3.html` | Session dump |
| `counter_vance_research_notes - consider including 5.html` | Counter-Vance material; workstream 10 scheduled for `_One Day Maybe/Counter-Vance/` |
| `democratic_socialism_book_discussion_april_19_2026 - consider including 7.html` | Democratic-socialism notes; workstream 10 scheduled for `_One Day Maybe/Democratic-Socialism/` |

**Action priority:** Execute the workstream-10-planned moves (Counter-Vance / Democratic-Socialism / Satellite-Essays / economic-theory-reference to their intended homes). **DELETE** the confirmed duplicate (9.html vs 12.html). Verify session-dump content has been consumed elsewhere, then keep-archived-as-history.

### 8.3 `archive/_One Day Maybe/`

| File | Status | Action |
|---|---|---|
| `Book Three_ Pricing the Final Frontier.docx` | Book Three seed — relevant to availability-absence / cosmic content per v1.28.0 | KEEP |
| `Book Two_ The Subsidy Economy.docx` | Book Two seed | KEEP |
| `commons-bonds-two-book-strategic-analysis 10.html` | Strategic analysis; per workstream 10 should be kept here as Book-Two reference | KEEP; drop " 10" suffix optional |

### 8.4 `archive/prototypes/`

| File | Status | Action |
|---|---|---|
| `100Barrel_CommonsBonds.html` | Companion piece prototype | KEEP |
| `commons-bonds-multi-scale-revision-prototype.html` | Multi-scale revision prototype | KEEP |

**Action priority for archive/:** Execute the `Consider Including/` separations per workstream 10's plan. Delete the confirmed duplicate. Drop Google-Drive-export number suffixes.

---

## 9. `alignment/` + subfolders

### 9.1 `alignment/` (top-level)

| File | Perm | Status | Action |
|---|---|---|---|
| `.DS_Store` | | macOS artifact | **DELETE + .gitignore** |
| `.gitkeep` | | standard | KEEP |
| `commons-bonds-handoff-template.html` | 0600 | Handoff template for future sessions | **NORMALIZE** permission if not intentional; KEEP |

### 9.2 `alignment/decisions/`

**Major finding:** this folder is substantially stale. Most files are April 19–20 migration-era documents describing a planned structure that was only partially implemented, or superseded by later work.

| File | Status | Action |
|---|---|---|
| `Commons Bonds — Session Archive & Decision Log.docx` | Pre-migration log | **INVESTIGATE** — is this still being referenced? Likely archive. |
| `commons-bonds-README.md` (0600) | **Stale** — references 9-tier list (wrong; canonical is 8-tier v10), "Decision A ratified" as current work (historical), old workstream status, references to `core/decomposition/eight-tier-v10.md` (actual file is `.html`) | **ARCHIVE** or REWRITE as current project README |
| `commons-bonds-github-design.md` (0600) | **Stale** — describes GitHub Issues workflow that was never implemented as designed | **ARCHIVE** |
| `commons-bonds-migration-plan.md` (0600) | **Stale** — migration is complete | **ARCHIVE** |
| `commons-bonds-workflow-guide.md` (0600) | **Stale** — GitHub Issues workflow that was discarded in favor of the rigor-pass-record pattern | **ARCHIVE** |
| `commons_bonds_c6_decision_memo_1_0_0.html` (0600) | C6 first attempt (v1); also duplicated in `issues/` | **INVESTIGATE** — pick canonical location (decisions/ is correct); remove from issues/ |
| `commons_bonds_c6_decision_memo_2_0_0.html` (0600) | C6 second attempt (canonical v2); also duplicated in `issues/` | **INVESTIGATE** — same as above; remove from issues/ |
| `eight-tier-decomposition-v10.md` (0600) | **Duplicate** — different format of `core/decomposition/eight-tier-v10.html` | **INVESTIGATE** — if content is equivalent, archive the .md (core/ .html is canonical per "math files stay .html"); if distinct content (prose version), rename to disambiguate |
| `repository-structure.md` (0600) | **Stale** — describes theoretical structure never fully implemented (references `definitions/`, `case-studies/*.md` files, `workstreams/WS02-glossary/status.md` etc. — most don't exist) | **ARCHIVE** |
| `session-handoff-2026-04-19.md` (0600) | Orphan handoff — belongs in `alignment/sessions/archive/` | **MOVE** to `alignment/sessions/archive/` |

### 9.3 `alignment/issues/`

| File | Status | Action |
|---|---|---|
| `c3_mechanism_shield_patch.md` | Canonical C3 patch | KEEP |
| `c9_ait_canonical_positioning_patch.md` | Canonical C9 patch (scaffolding-vs-load-bearing) | KEEP |
| `commons-bonds-c2-scale-abstract-patch.md` (0600) | C2 patch | **NORMALIZE** permission; KEEP |
| `commons-bonds-c4-decision-a-sweep.md` (0600) | C4 sweep | **NORMALIZE**; KEEP |
| `commons-bonds-c5-two-path-rigor.md` | Canonical C5 patch (two-path rigor source) | KEEP |
| `commons_bonds_c6_decision_memo_1_0_0.html` (0600) | **Duplicate** of file in `decisions/` | **DELETE** (canonical location is `decisions/`) |
| `commons_bonds_c6_decision_memo_2_0_0.html` (0600) | **Duplicate** of file in `decisions/` | **DELETE** (canonical location is `decisions/`) |
| `phase-1-migration-complete.md` (0600) | Migration-phase-1 completion note | **ARCHIVE** (migration complete — historical) |
| `tier-2a-rename-changes.md` (0600) | Tier 2a "Individual Risk" → "Actuarial Risk" rename changelog | **INVESTIGATE** — is the rename fully applied across the project? If yes, archive as changelog; if pending (per handoff queue), keep active. |

### 9.4 `alignment/sessions/`

| File / Folder | Status | Action |
|---|---|---|
| `.DS_Store` | macOS artifact | **DELETE** |
| `archive/` (30 files — handoffs v1.0.0 through v1.26.0) | Correctly archived lineage | KEEP |
| `commons-bonds-session-handoff-2026-04-22_v1_27_0.html` | Prior handoff (superseded this session by v1.28.0) | **MOVE** to `archive/` per pattern |
| `commons-bonds-session-handoff-2026-04-22_v1_28_0.html` | **Current canonical handoff** (written this session) | KEEP |

**Action priority for alignment/:** Archive 4 stale migration-era decisions docs. Move `session-handoff-2026-04-19.md` to sessions/archive/. Delete duplicated c6 memos from issues/. Move v1.27.0 handoff to sessions/archive/. Normalize 0600 permissions where not intentional.

---

## 10. `workstreams/` — 17+ files

This folder is a cross-cutting finding worth its own section. Not in Chris's explicit folder list but directly relevant.

**Files 01–17 (April 19–20, 2026):**
- `01_master_decisions.md` — Decision A/B/C/D ratification framework
- `02_glossary_reconciliation.md` through `17_honest_concession_section.md` — individual workstream plans

**Status:** These are the *original workstream plan* from the migration era (April 19–20). Reading them reveals they describe a state that has been substantially superseded by: (a) the rigor-protocol v1.2.1 canonicalization; (b) the 10-dimension framework (workstreams talk in terms of 7 layers); (c) the Option C two-pillar / two-methodology architecture (the framework now runs on AIT + two-path + merger/primitiveness gates); (d) the rigor-pass-record pattern (replaces parts of the workstream tracking).

**Some workstreams may have residual active content:**
- WS02 (glossary reconciliation) — glossary patching still pending per Part 3
- WS03 (Chapter 6 integration) — Ch. 6 drafted; may need Part 3 updates
- WS08 (Technical Appendix) — still pending per handoff deferred queue
- Others (WS04 Ch. 1 extension, WS05 Ch. 4/5 cases, WS06 villain landing, WS07 Ch. 8 trim, WS09 old-material rigor, WS10 folder reorg, WS11–17) — mostly consumed by later work

**Action priority:** **INVESTIGATE** — workstreams folder status overall. Candidates: (a) archive the whole folder as "historical planning documents"; (b) keep active workstreams that map to pending deferred-queue items; (c) write a short superseding doc that maps old workstream IDs to current handoff queue items.

---

## 11. Summary — recommended action sequence

**Low-risk, immediate (can run any time):**

1. Add `.DS_Store` to `.gitignore`; remove tracked instances.
2. Delete the confirmed `commons - consider including 9.html` duplicate.
3. Move `alignment/decisions/session-handoff-2026-04-19.md` → `alignment/sessions/archive/`.
4. Move `alignment/sessions/commons-bonds-session-handoff-2026-04-22_v1_27_0.html` → `alignment/sessions/archive/`.
5. Delete duplicated c6 memos from `alignment/issues/` (keep in `alignment/decisions/`).
6. Normalize `Chapter__5___Guidance.md` → `Chapter__5___GuidanceDoc.md` (naming consistency).
7. Execute the `archive/Consider Including/` moves per workstream 10's intended plan (Counter-Vance, Democratic-Socialism, Satellite-Essays, economic-theory-reference).

**Needs Chris's decision first:**

8. **Investigate: `tools/commons_bonds_rigor_pass_2026-04-22_v1_0_0.md` (Part 1) — archived or canonical?** Either promote back to `tools/` or patch references to treat it as canonically-archived.
9. **Investigate: `core/commons_bonds_integrated_framework.html` status.** Read fully and decide retain / archive.
10. **Investigate: `tools/userMemories_proposed_2026-04-21_v1_0_1.md` status.** Ratified, pending, or obsolete?
11. **Investigate: `tools/commons_bonds_layer_tier_stress_test_1_0_0.md` — archive now (I recommended) or keep?**
12. **Investigate: Ch. 1/1a split intent** (intentional two-part chapter or refactor-in-progress?).
13. **Investigate: Ch. 1/1a/3 guidance 0600 permission** (intentional privacy or accidental?).
14. **Investigate: Ch. 8 missing guidance doc** (intentional or missing?).
15. **Investigate: workstreams/ overall status** — archive folder or keep as superseded-but-referenced?
16. **Investigate: empty `research/case-studies/`, `research/literature/`, `publishing/targets/` folders** — intentional staging or abandoned plans?
17. **Investigate: migration-era stale docs in `alignment/decisions/`** — archive the 4 superseded files (README, github-design, migration-plan, workflow-guide, repository-structure)?
18. **Investigate: `alignment/decisions/eight-tier-decomposition-v10.md` vs. `core/decomposition/eight-tier-v10.html` relationship** — duplicate or complementary?

**After naming cohort completes (PATCH sweep — the main rename propagation):**

19. Patch `tools/claude_prefs.md` operating core with v1.28.0 terminology.
20. ~~Retitle `tools/commons_bonds_abundance_layers_v1_0_0.md` → abundance dimensions v1.1.0; propagate renames in §2;~~ **DONE 2026-04-22** as `commons_bonds_abundance_dimensions_v1_1_0.md` (Habitability, Kindred, Ecosystem locks propagated; container-term sweep completed). §5.5 and §5.6 notes (availability-absence severity-marker + lived-experience-canonical-case methodology per v1.28.0) **still pending** for a v1.1.1 patch.
21. Patch `tools/commons_bonds_rigor_protocol_v1.2.2.md` terminology → v1.2.2.
22. Patch `tools/commons_bonds_guiding_constraints_v1_0_0.md` terminology.
23. Patch `tools/commons_bonds_book_scope_v1_0_3.md` terminology (Part 3 target).
24. Patch `core/decomposition/eight-tier-v10.html` terminology.
25. Patch `core/decomposition/error-out-v10.html` terminology.
26. Patch `core/glossary/commons_bonds_updated_glossary_v2.html` terminology — **load-bearing; glossary is where framework vocabulary lives**.
27. Patch `core/technical-appendix/TechnicalAppendix_v0.0.2.html` terminology; resolve v0.0.2 metadata inconsistency per deferred queue.
28. Patch all 8 chapter drafts (Ch. 2, 4, 5, 6, 7, 8, 9, 10).
29. Patch all 10 guidance docs.
30. Patch `manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md` if applicable.
31. Patch `publishing/CommonsBondsPublishingStrategyConsolidated.html` if dimension terminology used.
32. Patch `publishing/CommonsBonds_BookOneCommonsBondsPathBookTwo.html` (also Part 3 target).

**Sequencing note:** Steps 1–7 can run in the current session or as a dedicated housekeeping mini-session. Steps 8–18 need Chris's answers. Steps 19–32 run after the naming cohort ratifies the remaining 7 dimension renames.

---

## 12. Files verified this review but not read fully

- `workstreams/02` through `workstreams/17` — sampled 01 and 10 only; recommendation is workstream-folder-level archival decision rather than file-by-file.
- `publishing/CommonsBonds_BookOneCommonsBondsPathBookTwo.html` (78KB) — size-skipped; should be read during Part 3.
- `publishing/CommonsBondsPublishingStrategyConsolidated.html` (35KB) — same.
- `core/technical-appendix/TechnicalAppendix_v0.0.2.html` (123KB) — size-skipped; Part 3 audit target.
- `core/glossary/commons_bonds_updated_glossary_v2.html` (26KB) — header-only read; Part 3 target.
- `core/decomposition/eight-tier-v10.html` (34KB) — not read; Part 3 target.
- `core/decomposition/error-out-v10.html` (32KB) — not read; Part 3 target.
- `research/methodology/commons_bonds_full_economy_simulation.html` — header-only; investigate.
- `core/commons_bonds_integrated_framework.html` — header-only; investigate.
- Several `archive/Consider Including/` files — status flagged by workstream 10's plan, verification read not done.

---

## 13. Cross-references

- `alignment/sessions/commons-bonds-session-handoff-2026-04-22_v1_28_0.html` — references this review at TOP PRIORITY §7.
- `tools/commons_bonds_rigor_protocol_v1.2.2.md` — canonical rigor protocol (PATCH target).
- `tools/commons_bonds_abundance_dimensions_v1_1_0.md` — canonical methodology doc (retitle + patch DONE 2026-04-22; §5.5 / §5.6 additions pending).
- `tools/commons_bonds_guiding_constraints_v1_0_0.md` — canonical constraints doc (PATCH target).
- `workstreams/10_project_separation_folder_reorg.md` — original archive/Consider-Including reorganization plan (partially executed; this review prompts completion).

---

*End of Commons Bonds Housekeeping Review 2026-04-22 v1.0.0.*
