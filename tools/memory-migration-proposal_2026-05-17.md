# Memory Migration Audit — PROPOSAL 2026-05-17

**Date drafted:** 2026-05-17
**Status:** PROPOSED — pending author ratification. No migration applied in this session.
**Origin session:** post pipeline-doctrine-v1.0.0 landing on `origin/main` (commit `ed5f6cf`); branch `claude/memory-consolidation-audit-0056b8`.
**Framing:** mobile-session brainstorm about whether the author's local-machine memory directory at `~/.claude/projects/-Users-c17n-commons-bonds/memory/` should partially migrate into the repo at `tools/memory/`, modeled on the hybrid-versioning pattern established by ratified decision #8 (2026-05-17) for `feedback_audience_aware_drafting_discipline.md` v3.0.

**Hard constraints in force during this session.** Propose-only; no memory files moved; no memory files deleted; CLAUDE.md + AGENTS.md untouched beyond drafting the §3 proposed @import block; sensitive content (any flagged SENSITIVE in §2) defaults KEEP-LOCAL regardless of citation count.

---

## §1. Summary

**File count by verdict (17 files audited):**

| Verdict | Count | Files |
|---|---|---|
| **MIGRATE** | 14 | The discipline + reference + frequently-cited entries that should hold consistently across mobile + laptop sessions and that are already load-bearing for repo doctrine artifacts. |
| **KEEP-LOCAL** | 1 | `project_authors_grandfather_nasa_inventor.md` — family material; SENSITIVE-by-default per §1.5 rule. |
| **ARCHIVE** | 1 | `project_book1_state_2026-05-10.md` — superseded by AGENTS.md canonical-state index; the `project_book1_state_<DATE>` series is supersession-prone by design (the memory file's own footer notes its predecessor superseded). |
| **EDGE** | 1 | `feedback_git_workflow.md` — partially duplicates WP#9 + CLAUDE.md branch discipline + `tools/workstream-handoffs/README.md`; recommended MIGRATE for the operational nuance (iCloud incident, active-push expectation, pre-push reconciliation) not captured in those artifacts. Author may instead choose to fold the operational nuance into WP#9 + ARCHIVE the memory. |

**High-priority migration candidates** (highest citation counts; load-bearing for current rigor-pass + workstream-handoff infrastructure):

1. `feedback_audience_aware_drafting_discipline.md` (34 cites) — already wired to canonical doctrine artifact via hybrid versioning per §8 of `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`; migration moves the v3.0 summary into git.
2. `feedback_named_subject_consent.md` (30 cites) — already referenced by filename from `CLAUDE.md` line 53; named subjects (Phat / Biggie / Colden) already appear in repo under `research/outreach/subjects/`, so migration adds no new subject exposure.
3. `feedback_substance_drives_length.md` (21 cites) — pure drafting discipline; no sensitive content.
4. `feedback_verify_stale_memory_claims.md` (18 cites) — memory-hygiene discipline applied to every memory read.
5. `feedback_voice_polish_pipeline.md` (14 cites) — drafting-pipeline discipline (substrate → sift → polish).

**Context-cost delta estimate (if all MIGRATE candidates are also `@import`-ed from CLAUDE.md per the framework's stated discipline):**

| Layer | Lines / approx size | Loaded when |
|---|---|---|
| **Current local-memory `MEMORY.md` index** | ~17 lines / ~5 KB | every Claude Code session start (laptop only). |
| **Migrated `tools/memory/` files (14 × ~30 lines avg)** | ~470 lines / ~50 KB | only when read / @import-ed. |
| **If `@import` all 14 from CLAUDE.md** | adds ~50 KB to every session start | every session, regardless of relevance. |
| **If `@import` only the 2-3 highest-cite (audience-aware + named-subject + verify-stale)** | adds ~10-15 KB to every session start | every session; rest of memory still findable via `tools/memory/README.md` index. |

§3 proposes the import-pointer variant rather than blanket `@import`, with the per-file `@import` decision raised as an open question in §5. The migration framework's literal text says "MIGRATE = move into tools/memory/ in the repo + `@import` from CLAUDE.md"; the proposed variant honors the migration half + flags the `@import` half as a separate decision.

---

## §2. Per-file audit table

Length column reports rough `wc -l` per the live local files. Citation column counts repo files (excluding `.git/` + `.claude/`) referencing the memory file by name.

### MIGRATE verdicts (14)

| File | Lines | Last modified | Cited by | Verdict | Rationale | Proposed repo path | Hybrid-versioning note |
|---|---|---|---|---|---|---|---|
| `feedback_audience_aware_drafting_discipline.md` | ~245 (post-v3.0) | 2026-05-17 (Part A this session) | 34 across doctrine + rigor-passes + handoffs + drafting-templates | **MIGRATE** | Highest citation density; hybrid versioning already ratified per ratified decision #8 (2026-05-17); the memory entry IS the scan-friendly summary layer, the canonical full architecture is `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`. Migration puts the scan-friendly layer in git alongside the doctrine layer. | `tools/memory/feedback_audience_aware_drafting_discipline.md` | **Doctrine-side artifact already exists** — `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` is canonical full architecture; migrated memory file is scan-friendly summary. Future updates flow through `tools/memory-updates/` specs (established convention). |
| `feedback_named_subject_consent.md` | 17 | 2026-05-12 | 30 across rigor-passes + outreach-subject files + handoffs | **MIGRATE** | Already referenced from `CLAUDE.md` line 53 by filename. Discipline applies across all sessions. Subjects named in the file (Phat / Biggie) already appear in `research/outreach/subjects/` so migration adds no new git exposure. Should hold consistently mobile + laptop. | `tools/memory/feedback_named_subject_consent.md` | Memory file IS canonical — no separate doctrine artifact needed. Consider moving the CLAUDE.md §"Named-subject consent" reference to point at `tools/memory/feedback_named_subject_consent.md` instead of by bare filename. |
| `feedback_substance_drives_length.md` | 17 | 2026-05-02 | 21 across rigor-passes + handoffs | **MIGRATE** | Pure drafting discipline; widely cited. Applies to every chapter session. No sensitive content. | `tools/memory/feedback_substance_drives_length.md` | Memory file IS canonical. |
| `feedback_verify_stale_memory_claims.md` | 23 | 2026-05-10 | 18 across rigor-passes + handoffs + memory entries | **MIGRATE** | Meta-discipline about memory reads; companion to harness staleness reminder. Cross-cutting; should hold consistently mobile + laptop. | `tools/memory/feedback_verify_stale_memory_claims.md` | Memory file IS canonical. |
| `feedback_voice_polish_pipeline.md` | 43 | 2026-05-04 | 14 across rigor-passes + handoffs | **MIGRATE** | Substrate → sift → polish pipeline discipline; applied every drafting session. No sensitive content. | `tools/memory/feedback_voice_polish_pipeline.md` | Memory file IS canonical. |
| `feedback_two_layer_content_discipline.md` | 33 | 2026-04-30 | 8 across handoffs + decisions | **MIGRATE** | WP#10. Canonical discipline statement lives in `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #10; memory file adds operational guidance (companion-documents pointers + default-when-uncertain rule). | `tools/memory/feedback_two_layer_content_discipline.md` | **Doctrine-side artifact already exists** — WP#10 in working-principles doc is canonical statement; migrated memory file is operational-guidance scan-friendly summary. |
| `reference_ostrom_illustrative_register.md` | 20 | 2026-05-02 | 8 across rigor-passes + handoffs + memory entries | **MIGRATE** | Ratified during Ch 10 line 125 cost-component pass; no single canonical doctrine doc; memory entry IS the canonical statement. Cross-cuts all chapter audits + framework-positioning work. | `tools/memory/reference_ostrom_illustrative_register.md` | Memory file IS canonical. (Consider adding to FPD or alignment/-side doctrine in a future session if pattern emerges.) |
| `feedback_dual_audience_test.md` | 28 | 2026-05-11 | 7 across rigor-passes + handoffs | **MIGRATE** | Trade-press polish discipline; cross-cuts apparatus-register work + chapter Stage-3 audits. Codified in apparatus-register-decision rigor pass §"Reusable principles" item 1-2 (per memory's own footer), but memory entry generalizes beyond that one rigor pass. | `tools/memory/feedback_dual_audience_test.md` | **Doctrine-side artifact exists** — codification in `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`; migrated memory file is the generalized cross-session scan-friendly summary. |
| `feedback_audit_open_illustrative_default.md` | 19 | 2026-05-12 | 6 across rigor-passes + handoffs | **MIGRATE** | Audit-side application of Ostrom-path discipline; companion to `reference_ostrom_illustrative_register.md`. Cross-cuts all Stage-3 audit passes. | `tools/memory/feedback_audit_open_illustrative_default.md` | Memory file IS canonical (audit-side application). |
| `feedback_audit_recent_active_review_default.md` | 17 | 2026-05-12 | 5 across rigor-passes + handoffs | **MIGRATE** | Audit-conflict-resolution discipline; companion to `feedback_verify_stale_memory_claims.md`. Cross-cuts Stage-3 fact-check passes + cross-chapter consistency audits. | `tools/memory/feedback_audit_recent_active_review_default.md` | Memory file IS canonical. |
| `feedback_grammatical_role_cross_references.md` | 60 | 2026-05-11 | 4 across rigor-passes + handoffs | **MIGRATE** | Drafting discipline for chapter → appendix cross-references; cross-cuts Stage-3 voice-polish + Tech Appendix work. Per memory's own footer, applied to Ch 6 in commit `50ec90b`; principle generalizes apparatus Item 10. | `tools/memory/feedback_grammatical_role_cross_references.md` | **Doctrine-side artifact exists** — Phase 5 of appendix-numbering-reconciliation workstream; migrated memory file is the generalized cross-session scan-friendly summary. |
| `reference_pattern_2_register.md` | 54 | 2026-04-30 | 3 across rigor-passes + handoffs | **MIGRATE** | Pattern 2 (Doughnut/Mazzucato/Mine!) threaded-demonstration register for external-facing framework material. Per memory's own pointer, full literature-pattern audit lives in `core/methodology/decision_time_application_internal_v1.0.0.md`; memory entry is scan-friendly summary. | `tools/memory/reference_pattern_2_register.md` | **Doctrine-side artifact exists** — `core/methodology/decision_time_application_internal_v1.0.0.md` §3 is canonical full analysis; migrated memory file is scan-friendly summary. |
| `feedback_pm_dashboard_structure.md` | 39 | 2026-05-13 | 3 across rigor-passes + handoffs + cross-thread-todos | **MIGRATE** | PM session dashboard format v2.0; codified in `tools/workstream-handoffs/pm-session-handoff_2026-05-13.md`. Memory entry is the cross-session discipline summary that each successor PM handoff inherits. | `tools/memory/feedback_pm_dashboard_structure.md` | **Doctrine-side artifact exists** — `tools/workstream-handoffs/pm-session-handoff_2026-05-13.md` is the codified canonical structure; migrated memory file is the cross-session discipline summary. |
| `reference_sandel_hybrid_pattern.md` | 39 | 2026-05-11 | 3 across rigor-passes + handoffs | **MIGRATE** | Acronym-treatment discipline (Sandel hybrid pattern for RCV-class acronyms). Codified in apparatus-register-decision rigor pass Item 14 per memory's own footer; memory entry generalizes for future apparatus passes. | `tools/memory/reference_sandel_hybrid_pattern.md` | **Doctrine-side artifact exists** — apparatus-register-decision rigor pass Item 14 + §"Reusable principles" item 3; migrated memory file is the generalized cross-session scan-friendly summary. |

### EDGE verdict (1)

| File | Lines | Last modified | Cited by | Verdict | Rationale | Proposed repo path | Hybrid-versioning note |
|---|---|---|---|---|---|---|---|
| `feedback_git_workflow.md` | 27 | 2026-05-10 | 2 across handoffs + sessions | **MIGRATE (edge)** | WP#9 discipline statement lives in `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #9 + branch-discipline section of `CLAUDE.md` + `tools/workstream-handoffs/README.md`. Memory entry adds operational nuance not in those: iCloud-incident anchor, expected-error message text, active-push expectation (2026-05-10), pre-push reconciliation pattern. **Author may instead choose to fold operational nuance into WP#9 doc + ARCHIVE this memory** — flagged as open question in §5. | `tools/memory/feedback_git_workflow.md` | **Doctrine-side artifacts exist** but don't capture operational nuance; migrated memory file holds the operational layer until/unless author folds it into WP#9 doc. |

### KEEP-LOCAL verdict (1)

| File | Lines | Last modified | Cited by | Verdict | Rationale |
|---|---|---|---|---|---|
| `project_authors_grandfather_nasa_inventor.md` | 20 | 2026-05-04 | 5 across rigor-passes + manuscript guidance + workstream-handoffs | **KEEP-LOCAL (SENSITIVE)** | Family material: author's grandfather LaVern E. Winn (deceased 1987); two patents identified including a retrieval-key ("L. E. Winn" + before-1987 + NASA) for future patent searches. Patent records are public; grandfather is deceased. **However, the memory entry contains the family folk-memory nickname provenance ("The Pooh," "Pooh," "Winnie the Pook") and family-folk-memory framing about the lunar-module honeycomb crumple zone**, which are personal/family details rather than purely public-record. Per §1.5 of the framing's KEEP-LOCAL criteria — "Sensitive content (named-subject consent edge cases; private feedback; work-in-progress framings)" — the family-folk-memory layer reads as private even though the patents themselves are public. **Default KEEP-LOCAL; flag for author decision** — author may want to MIGRATE if family-folk-memory layer is judged not-private given the grandfather is deceased + this material is already partially in `manuscript/chapters/_BookLevelGuidance.md` + the Ch 10 / AI Statement framing. |

### ARCHIVE verdict (1)

| File | Lines | Last modified | Cited by | Verdict | Rationale |
|---|---|---|---|---|---|
| `project_book1_state_2026-05-10.md` | 65 | 2026-05-11 | 4 across handoffs + sessions | **ARCHIVE** | The `project_book1_state_<DATE>` series is supersession-prone by design — the memory file's own footer says *"Supersedes: project_book1_state_2026-05-02.md (now stale; can be archived/deleted)"*. Current canonical project state lives in `AGENTS.md` §"Current canonical state" + the per-workstream `tools/workstream-handoffs/` artifacts. The memory entry's content is fully captured (and more current) in those artifacts. Per the framing's ARCHIVE criteria: "Superseded by a later memory file" + "Already captured in a doctrine artifact (memory entry duplicates repo content)". Recommend ARCHIVE log entry in §4 + future-`project_book1_state_<DATE>` snapshots should not be created in memory; instead use `AGENTS.md` + workstream-handoffs as the canonical state index. |

---

## §3. Proposed CLAUDE.md @import block (DRAFT for author review)

The migration framework's literal text says "MIGRATE = move into tools/memory/ in the repo + `@import` from CLAUDE.md". The block below honors that pattern but proposes a **pointer-block variant** instead of blanket `@import`, motivated by the §1 context-cost-delta estimate (~50 KB of memory content added to every laptop session start if all 14 are `@import`-ed).

**Recommended (pointer-block variant):**

```markdown
## Project memory (cross-session discipline)

The project's cross-session discipline registry lives at `tools/memory/`. Each file
captures a ratified discipline (feedback / project / reference) that should hold
consistently across mobile + laptop sessions. Index at `tools/memory/README.md`.

Load specific files when relevant to the session's work; do not bulk-load. The
local `~/.claude/projects/-Users-c17n-commons-bonds/memory/` directory remains the
default-load layer for laptop sessions; `tools/memory/` is the in-repo mirror that
mobile sessions + future collaborators can read via the repo.

High-touch files (cite this directly when applicable):

- `tools/memory/feedback_audience_aware_drafting_discipline.md` — v3.0 pipeline
  doctrine summary; full architecture at `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`.
- `tools/memory/feedback_named_subject_consent.md` — naming defaults for living /
  deceased / public-record subjects in publisher-facing prose.
- `tools/memory/feedback_verify_stale_memory_claims.md` — staleness discipline
  for time-sensitive claims.
```

**Alternative (literal-framework @import variant) — flagged in §5 as open question:**

```markdown
## Project memory (cross-session discipline) — imported

@tools/memory/feedback_audience_aware_drafting_discipline.md
@tools/memory/feedback_named_subject_consent.md
@tools/memory/feedback_substance_drives_length.md
@tools/memory/feedback_verify_stale_memory_claims.md
@tools/memory/feedback_voice_polish_pipeline.md
@tools/memory/feedback_two_layer_content_discipline.md
@tools/memory/reference_ostrom_illustrative_register.md
@tools/memory/feedback_dual_audience_test.md
@tools/memory/feedback_audit_open_illustrative_default.md
@tools/memory/feedback_audit_recent_active_review_default.md
@tools/memory/feedback_grammatical_role_cross_references.md
@tools/memory/reference_pattern_2_register.md
@tools/memory/feedback_pm_dashboard_structure.md
@tools/memory/reference_sandel_hybrid_pattern.md
@tools/memory/feedback_git_workflow.md
```

**Per-file-decision-import variant** (subset for author selection — see §5 open
question 1): import only the highest-cite + most-cross-cutting files; let the
rest be findable via `tools/memory/README.md`.

---

## §4. Proposed ARCHIVE log entries

Add to a new file `tools/memory/ARCHIVE.md` (or fold into `archive/retirements/index.md` if author prefers consolidation).

```markdown
## Memory archive log

### 2026-05-17 — project_book1_state_2026-05-10.md

**Verdict:** ARCHIVE.

**Reason:** Supersession-prone snapshot; the `project_book1_state_<DATE>` series
chains supersessions (this entry's own footer notes it supersedes
`project_book1_state_2026-05-02.md`). Current canonical project state lives in
`AGENTS.md` §"Current canonical state" + `tools/workstream-handoffs/` per-workstream
artifacts. The memory entry duplicates repo content that is more current than the
snapshot.

**Action:** Local memory file moved to local archive directory or deleted (author
discretion); `MEMORY.md` index entry removed. No in-repo presence proposed.

**Discipline going forward:** Do not author future `project_book1_state_<DATE>`
snapshots in memory. Canonical project state is `AGENTS.md` + workstream-handoffs.
```

Optional second entry pending §5 open question 1 resolution:

```markdown
### 2026-05-17 — feedback_git_workflow.md (CONDITIONAL — pending author decision per §5 OQ4)

**If author chooses ARCHIVE (fold operational nuance into WP#9 doc):**

**Reason:** WP#9 discipline statement is canonical in
`alignment/commons_bonds_working_principles_v1.0.0.md` Principle #9. Operational
nuance (iCloud-incident anchor, active-push expectation, pre-push reconciliation
pattern) folded into WP#9 doc this session. Memory entry duplicates repo content.

**Action:** Operational-nuance edits applied to
`alignment/commons_bonds_working_principles_v1.0.0.md` Principle #9 + memory file
moved to local archive.

**If author chooses MIGRATE (default per §2 EDGE verdict):** no ARCHIVE entry.
```

---

## §5. Open questions / edge cases for author decision

1. **`@import` strategy.** Migration framework literal text says `@import` from CLAUDE.md. Context-cost estimate (~50 KB per session start if all 14 are imported) suggests the pointer-block variant in §3 may be preferable. **Three options:**
   - **(a)** Pointer-block only (recommended in §3) — context-cost neutral; relies on session-specific lookups.
   - **(b)** Selective `@import` — import 2-3 highest-cite files (audience-aware + named-subject + verify-stale ≈ 15 KB) so they always-load; rest via pointer.
   - **(c)** Full literal `@import` — all 14 always-load; ~50 KB session-start tax.

   Recommend **(b)** — selective `@import` for the 2-3 cross-cutting files that every session needs, pointer-block for the rest.

2. **Memory file as scan-friendly summary vs. memory file as canonical content.** For files where doctrine-side canonical exists (audience-aware → pipeline doctrine; two-layer → WP#10; pattern-2 → core/methodology; sandel-hybrid → apparatus-register rigor pass; pm-dashboard → pm-session-handoff_2026-05-13; dual-audience → apparatus-register rigor pass; grammatical-role → appendix-numbering-reconciliation Phase 5; git-workflow → WP#9), the migrated memory file is the **scan-friendly summary layer** and the doctrine artifact is the **canonical content layer**. **Question:** should migrated memory files include an explicit `**Canonical full content:** <repo path>` header pointing to the doctrine artifact, mirroring the v3.0 audience-aware pattern? **Recommend yes** — applies the established v3.0 hybrid-versioning convention uniformly.

3. **Memory-update spec convention.** v3.0 audience-aware update was authored as a spec under `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`, applied to local memory at session close. **Question:** should the migration apply the same convention — i.e., for each MIGRATE candidate, write an initial-migration spec under `tools/memory-updates/<filename>_initial-migration-2026-05-17.md` documenting the migration source + checksum, even though no content changes? **Recommend no** — initial migration is documented sufficiently by this audit + git diff at apply time. Reserve `tools/memory-updates/` for substantive content updates (v2.0 → v3.0-style).

4. **`feedback_git_workflow.md` MIGRATE vs ARCHIVE (EDGE verdict in §2).** Operational nuance not in WP#9 doc / CLAUDE.md / workstream-handoffs README. **Two options:**
   - **(a) MIGRATE** (default per §2 EDGE verdict) — keep operational layer in `tools/memory/`; WP#9 doc remains the canonical discipline statement.
   - **(b) ARCHIVE + fold operational nuance into WP#9 doc** — single canonical home; ARCHIVE entry in §4 conditional second entry.

   Recommend **(a)** — less doctrine-churn; operational layer stays scan-friendly. Author may prefer (b) for consolidation hygiene.

5. **`project_authors_grandfather_nasa_inventor.md` KEEP-LOCAL vs MIGRATE (SENSITIVE flag in §2).** Grandfather is deceased; patents are public record; family-folk-memory nicknames + lunar-module honeycomb framing read as private. **Author decision required.** Default KEEP-LOCAL per §1.5 sensitive-content rule unless author explicitly clears the family-folk-memory layer for git inclusion. If MIGRATE, proposed path: `tools/memory/project_authors_grandfather_nasa_inventor.md`; no separate doctrine artifact needed.

6. **`MEMORY.md` index handling.** Local `MEMORY.md` (the laptop-session quick-load index) currently has 17 entries. After migration:
   - **(a)** Local `MEMORY.md` retains all 17 entries (still loaded by laptop sessions); add a parallel `tools/memory/README.md` index for the in-repo mirror.
   - **(b)** Local `MEMORY.md` loses entries for the 14 MIGRATE files (rely on `@import` from CLAUDE.md to surface them); only KEEP-LOCAL entries remain.
   - **(c)** Local `MEMORY.md` stays as-is but adds a "[mirrored at tools/memory/]" annotation per migrated entry.

   Recommend **(a)** — least disruption; both indexes coexist.

7. **Multi-machine sync for any MIGRATE file that gets locally edited.** If author edits `tools/memory/<file>` locally during a session, the local-memory-copy and the in-repo copy can drift. Discipline: **the repo copy is canonical**; local-memory edits should be ratified into the repo copy via a `tools/memory-updates/` spec (as v3.0 was) or a direct repo edit at session close. **Question:** codify this as a working-principle amendment, or rely on existing WP#9 + branch discipline? **Recommend** flag as a working-principle amendment candidate but defer to a future session.

8. **Application-session sequencing.** This is propose-only. If author ratifies, application is a separate session that should:
   - Create `tools/memory/` directory.
   - Copy MIGRATE files from `~/.claude/projects/-Users-c17n-commons-bonds/memory/` to `tools/memory/`.
   - Add `tools/memory/README.md` (mirror of local `MEMORY.md`).
   - Apply chosen `@import` strategy to `CLAUDE.md` (§5 OQ1).
   - Apply ARCHIVE entries per §4.
   - Update local `MEMORY.md` per §5 OQ6 decision.
   - Verify each MIGRATE candidate has scan-friendly-summary-vs-canonical-content header per §5 OQ2 (if recommend-yes ratified).

   Recommend a single application session on a `claude/memory-migration-apply-<harness-id>` feature branch with author ratifying the migration table top-line + each OQ resolution before commits land.

---

## §7. Ratified decisions — 2026-05-17

All 8 open questions in §5 and the EDGE / KEEP-LOCAL flags in §2 were ratified by the author on 2026-05-17 via direct ratification of the recommendations as proposed ("ratify all as recommended and proposed"). Resolved positions, captured here as the spec for the apply session at [`tools/workstream-handoffs/memory-migration-apply-handoff_2026-05-17.md`](workstream-handoffs/memory-migration-apply-handoff_2026-05-17.md):

1. **Migration table (§2 top-line):** APPROVED. 14 MIGRATE + 1 KEEP-LOCAL (SENSITIVE) + 1 ARCHIVE + 1 EDGE-treated-as-MIGRATE → 15 files into `tools/memory/`.
2. **`@import` strategy (§5 OQ1):** **SELECTIVE `@import`** (option b). Three always-load files:
   - `tools/memory/feedback_audience_aware_drafting_discipline.md`
   - `tools/memory/feedback_named_subject_consent.md`
   - `tools/memory/feedback_verify_stale_memory_claims.md`

   Remaining 12 files (11 standard + 1 EDGE) discoverable via `tools/memory/README.md`; not auto-imported.
3. **`feedback_git_workflow.md` (§2 EDGE / §5 OQ4):** **MIGRATE.** Operational nuance (iCloud-incident anchor, active-push expectation, pre-push reconciliation) stays in `tools/memory/`; WP#9 doc unchanged.
4. **`project_authors_grandfather_nasa_inventor.md` (§2 / §5 OQ5):** **KEEP-LOCAL** (SENSITIVE family-folk-memory layer). Existing repo coverage in `manuscript/chapters/_BookLevelGuidance.md` for the retrieval-key discipline is sufficient; no migration.
5. **Canonical-pointer headers (§5 OQ2):** **YES**, apply uniformly per v3.0 audience-aware pattern. Each migrated file with doctrine-side canonical gets a `**Canonical full content:** <repo path>` header inserted between YAML frontmatter and H1.
6. **Local `MEMORY.md` (§5 OQ6):** **ANNOTATE** (option c). Migrated entries get `[mirrored at tools/memory/<file>]` annotation appended; structure unchanged. ARCHIVE entry for `project_book1_state_2026-05-10.md` removed from index; KEEP-LOCAL entry for `project_authors_grandfather_nasa_inventor.md` unchanged.
7. **Initial-migration `tools/memory-updates/` specs (§5 OQ3):** **NO.** Reserve `tools/memory-updates/` for substantive content updates (v2.0 → v3.0-style). Initial migration provenance lives in this audit + git diff at apply time.
8. **Multi-machine sync as WP amendment (§5 OQ7):** **DEFER.** Flag as candidate working-principle amendment in `alignment/commons_bonds_open_insights_v1.0.0.md` (next-free insight number — verify at apply time per AGENTS.md staleness); no codification yet.

Apply-session handoff at [`tools/workstream-handoffs/memory-migration-apply-handoff_2026-05-17.md`](workstream-handoffs/memory-migration-apply-handoff_2026-05-17.md) operationalizes these decisions into the 8-step ordered task list. Apply session should re-quote these decisions at session opening for ground-truth pinning.

---

## §8. References

- Originating mobile-session brainstorm (paste only; no artifact in repo; framing block at top of this session).
- `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` §8 — hybrid versioning per ratified decision #8 (the model this audit applies more broadly).
- `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md` — v3.0 update spec (applied locally in Part A of this session).
- `AGENTS.md` §"Current canonical state" — canonical-state index; doctrine + invariant-gate rows ground this audit's "doctrine artifact already exists" notes.
- `CLAUDE.md` §"Named-subject consent" — existing by-filename memory reference (line 53); proposed §3 pointer-block updates this convention.
- `~/.claude/projects/-Users-c17n-commons-bonds/memory/MEMORY.md` — local memory index (17 entries; ground truth for this audit's file list).
- `~/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md` — v3.0-updated 2026-05-17 (Part A of this session); historical record (v2.0 Amendment B) preserved beneath as audit-trail.

---

*End of memory migration proposal — PROPOSED 2026-05-17 + RATIFIED 2026-05-17 (§7). Propose-only; no migration applied in this session. Apply session fires from [`tools/workstream-handoffs/memory-migration-apply-handoff_2026-05-17.md`](workstream-handoffs/memory-migration-apply-handoff_2026-05-17.md).*
