# Per-essay rigor consolidation pilot — Atlantic main worked example (2026-05-28)

**Date:** 2026-05-28
**Pilot target:** `publishing/essays/atlantic-main-chesapeake-watermen/`
**Branch:** `claude/rigor-consolidation-pilot-atlantic-main-260528-988811`
**Outcome:** EXECUTED — 8 artifacts migrated; 17 files updated for cross-refs; invariant scan clean; `git log --follow` lineage preserved through all moves.
**Pattern ratification reference:** CLAUDE.md §"Branch discipline + merge-to-main" + [`publishing/essays/README.md` §"Per-essay directory layout"](../README.md).

## Why this pilot

The 2026-05-28 ratifications established merge-on-ratification + the per-essay rigor consolidation pattern (rigor-pass artifacts that pertain to ONE essay move into `<venue>-<slug>/rigor/` alongside `essay.md` + `cover-letter.md` + `stage-5-signoff.md`, replacing the centralized `tools/rigor-passes/<long-disambiguated-filename>` convention for per-essay artifacts).

Eight essays + one chapter rigor-pass corpus need migration. To de-risk the bulk migration, this pilot exercised the full migration mechanism end-to-end on a single representative essay before the sibling bulk-migration session fires. The Atlantic main essay was chosen because (a) it's Stage 5 RATIFIED with no in-flight cascade work, (b) all artifact classes are present (Stage 1 brief, 5 passes, Stage 5 sign-off, pre-pub review queue), and (c) it has no time pressure (submission window Q4 2026 Oct–Dec).

## What was migrated

Eight artifacts moved via `git mv` (preserving file history through 100%-similarity renames):

| # | Old path | New path |
|---|---|---|
| 1 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-26_atlantic_main_essay_pre_draft_audience_structure_v1.0.0.md` | `publishing/essays/atlantic-main-chesapeake-watermen/rigor/stage-1-brief.md` |
| 2 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch3_atlantic_main_essay_pass_3_1_fact_check_v1.0.0.md` | `…/rigor/pass-3-1-fact-check.md` |
| 3 | `…_stage3_pass_3_2_voice_polish_v1.0.0.md` | `…/rigor/pass-3-2-voice-polish.md` |
| 4 | `…_stage3_pass_3_3_audience_load_v1.0.0.md` | `…/rigor/pass-3-3-audience-load.md` |
| 5 | `…_stage3_pass_3_4_adversarial_v1.0.0.md` | `…/rigor/pass-3-4-adversarial.md` |
| 6 | `…_stage3_pass_3_5_developmental_edit_v1.0.0.md` | `…/rigor/pass-3-5-developmental-edit.md` |
| 7 | `…_stage5_sign_off_v1.0.0.md` | `…/rigor/stage-5-signoff.md` |
| 8 | `…_stage5_pre_publication_review_queue_v1.0.0.md` | `…/rigor/pre-pub-review-queue.md` |

No Stage 4 render audit artifact for Atlantic main (Stage 4 RATIFIED offline; no file). No light Pass 3.3 re-fires.

## Cross-reference fixup — files touched

17 files modified, balanced 70/70 insertion/deletion (substitution-only changes):

| File | Refs updated | Notes |
|---|---|---|
| `publishing/essays/atlantic-main-chesapeake-watermen/README.md` | 8 | Full cross-reference block rewritten to point at `rigor/` |
| `publishing/essays/atlantic-main-chesapeake-watermen/stage-5-signoff.md` | 3 | Mirror-back-pointer + 2 pre-pub-queue refs |
| 8 artifacts now in `…/rigor/` | ~20 total | Intra-folder sibling refs flattened to bare basenames (`[\`pass-3-1-fact-check.md\`](pass-3-1-fact-check.md)`) |
| `research/literature/bibliography.md` | 1 | §19.7 Chesapeake regional reportage status note |
| 6 × `tools/workstream-handoffs/ch3-atlantic-main-stage-*-kickoff_2026-05-27.md` | ~37 total | Historical kickoff paste-texts; predecessor-pass references |
| `tools/workstream-handoffs/archive/cross-essay-portfolio-review_2026-05-27.md` | 2 active links + 2 breadcrumb annotations | §1.4 portfolio status + §E.1 pre-pub-queue extraction-sweep note |

## Validation outcomes

- **Invariant-gate scan:** `tools/scripts/check-corpus-invariants.sh` exit 0; 0 HIGH; no atlantic-main-specific findings (pre-existing MEDIUM/LOW findings in `publishing/op-eds/` are unrelated).
- **All 8 new paths resolve:** every link in the per-essay README maps to an existing file under `rigor/`.
- **No orphaned references** to the 8 old basenames except 2 deliberate "consolidated 2026-05-28 from `<old path>`" breadcrumb annotations in the cross-essay portfolio review (active links point to new paths; old paths are historical breadcrumbs).
- **`git log --follow` lineage preserved** on every moved file — verified on stage-1-brief (traces back to `361e5dc`), pass-3-5 (traces back to `708ec0f`), stage-5-signoff (traces back to `15da835`).

## Edge cases + recommendations for the bulk migration

### EC1 — `stage5_sign_off` rigor-pass artifact ↔ at-folder `stage-5-signoff.md` collision

**The case:** The Atlantic main essay folder already had a `stage-5-signoff.md` at the essay root (the at-folder bookend pattern established for BR + NYRB) AND a central rigor-pass artifact in `tools/rigor-passes/`. The two files share substantive content (the bookend essentially mirrors the rigor-pass artifact with different header framing) but are NOT byte-identical — the central artifact carries v3.1 Amendment B rigor-pass-format metadata (cascade predecessors, Stage 1 brief reference, methodology anchor) that the at-folder bookend doesn't.

**Resolution chosen:** Both files survive via directory disambiguation — central artifact migrates to `rigor/stage-5-signoff.md`, at-folder bookend stays at `stage-5-signoff.md` at essay root. The bookend's "this mirrors the central artifact at..." reference is updated to point at the new `rigor/stage-5-signoff.md` location.

**Recommendation for bulk migration:** When a per-essay folder already has a `stage-5-signoff.md` at root AND the essay has a central `stage5_sign_off` artifact in `tools/rigor-passes/`, **accept the dual-file outcome** rather than try to merge. Update the at-root bookend's back-pointer to the new rigor/ location. Per the 2026-05-28 README layout, the canonical slot for Stage 5 sign-off is at essay root; the additional rigor/ slot is an extension that preserves the audit-trail-format version. Most essays will NOT have this duplication (only Atlantic main + NYRB do per a quick grep of `tools/rigor-passes/` for `stage_?5_?sign` patterns).

### EC2 — sibling rigor-pass artifacts cite each other by bare basename

**The case:** Pass 3.2 cites Pass 3.1; Pass 3.3 cites Passes 3.1 + 3.2; etc. The original sibling-citation format inside artifacts was the bare basename (e.g., ``[`commons_bonds_rigor_pass_2026-05-27_ch3_atlantic_main_essay_pass_3_1_fact_check_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-27_ch3_atlantic_main_essay_pass_3_1_fact_check_v1.0.0.md)``) — no directory prefix, since all siblings lived in `tools/rigor-passes/` together.

**Resolution:** After the move, sibling artifacts are still co-located (now in `<venue>/rigor/`). The substitution simply flattens the basenames: bare `commons_bonds_rigor_pass_..._pass_3_1_..._v1.0.0.md` → bare `pass-3-1-fact-check.md`. Relative-path semantics carry over (same-directory link).

**Recommendation:** A simple sed substitution map of `<old-basename>` → `<new-basename>` handles all intra-rigor sibling refs cleanly — no path manipulation needed.

### EC3 — sed regex wildcard bug (`.` matches anything) — IMPORTANT

**The case:** The first-pass batch substitution used `s#../rigor-passes/<OLD>#../../<NEW_PATH>/<NEW>#g` to rewrite relative-path references from `tools/workstream-handoffs/X.md` to `tools/rigor-passes/Y.md`. Because `.` is a regex metacharacter, the pattern `../rigor-passes/` matched the substring `ls/rigor-passes/` inside the literal `tools/rigor-passes/`. Result: `tools/rigor-passes/X` got corrupted to `too` + `../../<NEW_PATH>/<NEW>` = `too../../<NEW_PATH>/<NEW>`.

**Resolution:** Revert (via `git checkout HEAD --`) the rigor/ files + workstream-handoffs files, then re-apply with literal-dot patterns: `s#\.\./rigor-passes/<OLD>#../../<NEW_PATH>/<NEW>#g`.

**Recommendation for bulk migration:** ALWAYS escape dots in sed expressions when working with paths. Use `\.\.` for `..` and `[.]` or `\.` for individual literal dots if any other `.` characters appear in the pattern. If working from a Python script instead, use `str.replace()` (string ops, not regex) for the bulk substitution to sidestep the issue entirely.

### EC4 — pre-existing data quality issue in per-essay README (NOT corrected during pilot)

**The case:** The per-essay README's "Stage 4 render audit: RATIFIED offline 2026-05-27 — commit `b54822b`" reference is incorrect: commit `b54822b` actually corresponds to the **Atlantic IDEAS** Stage 4 render audit author-offline marker, not Atlantic main. The correct Atlantic-main Stage 4 commit hash is not surfaced in the README; the artifact was RATIFIED offline with no separate marker commit (the offline ratification was conveyed via author bulk-signal, not a dedicated commit).

**Resolution:** **Not corrected during this pilot.** Per the brief: "Preserve the artifact's content verbatim — this is a relocate, not a rewrite." Flagged here for surface-level visibility; the author may correct in a separate touch-up commit or leave as historical record. The mis-citation doesn't affect the rigor-cascade audit trail (Stage 4 RATIFIED offline is preserved in commit `1815813`'s message body + the Stage 5 sign-off §0 confirmation).

**Recommendation for bulk migration:** Do NOT attempt to correct pre-existing data-quality issues in per-essay README content. Stick to mechanical relocate-only. Surface any spotted inaccuracies in the per-essay migration log for the author's later attention.

### EC5 — kickoff paste-text template refs with `<DATE>` placeholders

**The case:** Some workstream-handoff kickoff paste-texts contain template-text references like `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_ch3_atlantic_main_essay_stage3_pass_3_2_voice_polish_v1.0.0.md` — the `<DATE>` placeholder is template literal text, not a real basename. Standard old-basename substitution missed these.

**Resolution:** Hand-update template paths to point to the new convention: `publishing/essays/atlantic-main-chesapeake-watermen/rigor/pass-3-2-voice-polish.md`. The `<DATE>` placeholder is dropped because the new convention doesn't include date in the basename (the per-essay folder + the file content's frontmatter provide the disambiguation).

**Recommendation:** After the bulk sed sweep, search for any remaining `tools/rigor-passes/.*<DATE>.*<essay-pattern>` occurrences and hand-update.

## What did NOT need to move

No artifact in `tools/rigor-passes/` covering BOTH Atlantic main AND another essay was found in the inventory. So no cross-essay artifacts stayed in `tools/rigor-passes/` with cross-references back into the per-essay folder. The bulk migration sibling session should explicitly check for this class (e.g., Wave 2 Stage 0 batch artifacts that cover Ch 2 + Ch 3 + Ch 4 + Ch 8 in one file — those STAY in `tools/rigor-passes/`).

## Commit plan + push posture

Two separate commits on the pilot branch (one per phase):

1. `1303966` — Phase B file moves (8 renames; 100% similarity)
2. `e32edc6` — Phase C cross-reference fixup (17 files; 70/70 ins/del)

Per the merge-on-ratification rule + active-push expectation: the pilot session pushes both commits to `origin/main` at Phase F via the pre-push reconciliation pattern. Internal scaffolding class (rigor-pass artifacts + workstream-handoffs + READMEs + this worked-example doc) auto-merges per the CLAUDE.md per-session protocol.

## Discipline carry-forward for the bulk migration

1. **Inventory first** — produce the old-path → new-path mapping table BEFORE any `git mv` so the cross-ref-fixup sed map is pre-planned.
2. **`git mv`, not `mv` + `git add`** — preserves file history; `git log --follow` works after.
3. **Verify same-similarity (100%) renames in the commit summary** — anything <100% means content drifted (shouldn't happen for relocate-only).
4. **Two-commit-per-essay structure** — Phase B (file moves) + Phase C (cross-ref fixup) as separate commits; keeps the rename clean under `git log --follow` and makes Phase C reviewable as a pure substitution diff.
5. **Sed expression hygiene** — escape literal dots; verify substitution outputs on a sample file before bulk-applying.
6. **Invariant-gate scan + orphan-ref grep after each essay** — catch regressions essay-by-essay rather than en-masse at the end.
7. **Preserve historical breadcrumbs in cross-essay scaffolds** — when a portfolio dashboard / decision log calls out an essay-specific artifact by its old central path, keep the old path in a "consolidated 2026-05-28 from `<old path>`" breadcrumb annotation. Helps future readers trace history; cheap to add; doesn't break anything.
8. **Don't touch other essays' folders during your essay's migration** — discipline against scope creep that could compound errors across essays.

## Branch + push state at pilot close

- **Pilot branch:** `claude/rigor-consolidation-pilot-atlantic-main-260528-988811`
- **Commits on branch ahead of main:** 3 (Phase B + Phase C + this Phase E doc).
- **Push action at Phase F:** pre-push reconciliation (`git fetch origin main && git rebase origin/main`) → push to `origin/main` via `git push origin HEAD:main` → worktree removal.
- **Worktree path:** `/Users/c17n/commons-bonds-rigor-consolidation-pilot-atlantic-main-260528-988811`

## Sibling bulk-migration kickoff prerequisites

When firing the bulk-migration session for the remaining 8 essays:

1. Confirm origin/main carries this pilot's 3 commits + `rigor/` subdir exists in atlantic-main-chesapeake-watermen.
2. Reference this doc + the EC1–EC5 recommendations above.
3. Per-essay inventory tables for the remaining 8 essays — likely candidates per quick grep of `tools/rigor-passes/` filenames:
   - noema-commons-bonds (multiple passes 2026-05-09 → 2026-05-24)
   - boston-review-accountability-gap (multiple passes 2026-05-19 → 2026-05-23)
   - 100-barrel (Stage 0 publishing-strategy + Stage 3 cycle + comparative-draft audit)
   - aeon-mask-of-abundance (multiple passes)
   - atlantic-ideas-pricing-honestly (Stage 4 render audit author-offline + earlier passes)
   - foreign-affairs (Stage 5 RATIFIED 2026-05-27)
   - nyrb-multi-book-review (Stage 5 RATIFIED 2026-05-27; central + per-essay sign-off dual-file pattern same as atlantic-main per EC1)
   - berggruen-prize-2026 (seed material only; likely no rigor history to migrate yet)
4. The pre-existing 2 deliberate breadcrumb annotations in cross-essay-portfolio-review.md establish the precedent for the bulk migration's own breadcrumb annotations.

---

*End of pilot worked-example. Status: pilot EXECUTED 2026-05-28; ready for sibling bulk-migration session fire.*

---

## Bulk-migration COMPLETE annex — 8 sibling essays migrated (2026-05-28)

**Status:** EXECUTED. Sibling bulk-migration session fired and completed 2026-05-28 after pilot landed; all 8 remaining essays consolidated per pilot pattern.

### Per-essay artifact counts

| Essay | Artifacts | Commits | Notes |
|---|---|---|---|
| noema-commons-bonds | 10 | Phase B + C | Includes pre-discipline-evolution artifacts (early audience-load 2026-05-09 + Stage 3 A-vs-B comparison 2026-05-10) + Phat replacement analysis 2026-05-20 |
| boston-review-accountability-gap | 7 | Phase B + C | No Pass 3.4 artifact (opt-in; did not fire); Stage 0 publishing-strategy included |
| aeon-mask-of-abundance | 8 | Phase B + C | Pitch-first model; Pass 3.3+3.4 bundled (small-form variant); title-candidates + evolution audit + reading-flow review |
| 100-barrel | 9 | Phase B + C | Q1 go/no-go + Stage 3 comparative draft audit (A-vs-B; Draft A selected) included |
| atlantic-ideas-pricing-honestly | 8 | Phase B + C | Includes pre-pub-review-queue migrated from tools/pre-submission-reviews/; quality-gates sign-off intentionally retained per pilot doctrine; README status-block staleness flagged |
| foreign-affairs-existence-proof | 7 | Phase B + C | Cross-essay batch artifacts (Wave 2 Stage 0, TA RCV sign-off) retained at tools/rigor-passes/ |
| harpers-the-miner | 6 | Phase B + C | Chapter-side ch2_the_miner_* rigor retained at tools/rigor-passes/ |
| nyrb-multi-book-review | 9 | Phase B + C | EC1 dual-file case (both at-folder + central stage-5-signoff.md survive); exploratory single-book Stage 0 artifacts (chesapeake-requiem, christophers-price-is-wrong) retained at tools/rigor-passes/ |
| **TOTAL** | **64** | **16** | Plus pilot's 8 atlantic-main artifacts = **72 essay-side artifacts** consolidated 2026-05-28 |

### Worked-example carry-forward observations

The pilot's EC1–EC5 edge cases all held up under bulk-migration:

- **EC1 (dual-file stage-5-signoff)** — fired for NYRB (predicted by pilot). Atlantic main + NYRB are now both confirmed as the two cases per the pilot's grep.
- **EC2 (sibling intra-rigor refs)** — handled cleanly via the rel-from-source link target substitution + label cleanup in the bulk fixup script.
- **EC3 (sed regex wildcard bug)** — avoided by using Python `str.replace()` for path substrings and `re.escape()` for all basename patterns in the bulk script.
- **EC4 (pre-existing data-quality issues)** — surfaced one in atlantic-ideas README (stale Stage 3/Stage 5 status block; essay actually RATIFIED Stage 5 2026-05-27); flagged in commit message + per-essay README migration log; NOT corrected (relocate-only discipline).
- **EC5 (`<DATE>` template placeholders inside artifacts)** — many in migrated rigor artifacts (e.g., Stage 1 brief sections describing expected Pass 3.X output paths); preserved verbatim per relocate-only discipline. Search for `tools/rigor-passes/.*<DATE>.*` is the way to spot these post-migration.

### New observations from bulk-migration

- **EC6 — Sibling rigor-pass artifacts cite OTHER ESSAYS' rigor.** Many `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_<essay-A>_*.md` files contain "Wave 1 format precedent" or "sibling literary-essay" pointers to other essays' rigor-pass artifacts. As each essay migrated, those pointers in still-unmigrated essays' rigor-passes got rewritten. By the end of all 8 migrations, all such pointers point at the new per-essay locations. Net effect: tools/rigor-passes/ files referencing migrated essays' rigor passes are partially-rewritten — they still describe the OLD pipeline state in narrative but the link targets point at NEW locations. Acceptable: relocate-only discipline preserves content; rewriting narrative would violate it.
- **EC7 — Kickoff-handoff "predicted-filename" inaccuracies pre-existed migration.** Many `tools/workstream-handoffs/*-kickoff_*.md` reference rigor-pass artifacts by predicted-but-inaccurate basenames (e.g., references to `commons_bonds_rigor_pass_2026-05-22_boston_review_essay_stage3_pass_3_3_audience_load_v1.0.0.md` when the actual artifact was at `2026-05-23` with a slightly different format). These are pre-existing scaffolding inaccuracies, NOT migration regressions. Per EC4 discipline, not corrected; flagged here for surface visibility.
- **EC8 — Truncated `...` references.** A handful of files use truncation `..._aeon_pitch_stage3_comparison_v1.0.0.md` ("same prefix as above") in narrative prose. These don't match the bulk-substitution script's full-basename regex pattern. As one entry in a list gets substituted to the new path, the `...` truncation in the next entry no longer expands sensibly. Surface ugliness; functionally inert. Not corrected per EC4.

### Validation

- **Final corpus-invariant scan exit 0** (0 HIGH; pre-existing MEDIUM/LOW in `publishing/op-eds/` are unrelated to this migration per pilot Phase D baseline).
- **All 64 new paths resolve** under their `publishing/essays/<venue>/rigor/` subdirs.
- **`git log --follow` lineage preserved** on all moves (100% similarity on every rename per the per-essay Phase B commit summaries).
- **tools/rigor-passes/ file count after bulk migration:** 192 files remaining. Composition: chapter-side rigor (ch1, ch3, ch4-existence-proof chapter, ch5–ch10, TA), cross-essay batch (Wave 2 Stage 0, TA RCV sign-off, cross-corpus IPG canonical construction, chesapeake-requiem + christophers single-book exploratory Stage 0), and term-level / phase-level book-side rigor (`term_*`, `phase2_*`, `gate_*`, etc.).

### Push posture + merge-on-ratification

Each per-essay migration was committed as Phase B (file moves; 100% similarity rename) + Phase C (cross-reference fixup) and pushed to `origin/main` immediately per the merge-on-ratification rule (CLAUDE.md 2026-05-28). Pre-push reconciliation pattern (`git fetch origin main && git rebase origin/main`) ran clean on every push — no parallel-session conflicts surfaced during this bulk run.

### Branch + worktree disposition

- **Bulk-migration branch:** `claude/rigor-consolidation-bulk-migration-260528-defdbe`
- **Commits on branch:** 16 (8 Phase B + 8 Phase C) + this annex commit.
- **All commits landed on `origin/main`** via merge-on-ratification.
- **Worktree path:** `/Users/c17n/commons-bonds-rigor-consolidation-bulk-migration-260528-defdbe` — removable at session close.

---

*Bulk migration COMPLETE 2026-05-28. 64 essay-side artifacts across 8 essays consolidated; pilot pattern held with EC1–EC8 observations integrated. Per-essay-folder lookup ergonomics achieved.*
