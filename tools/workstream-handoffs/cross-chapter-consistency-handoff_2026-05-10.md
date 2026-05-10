# Cross-Chapter Consistency Audit — Workstream Handoff (2026-05-10)

**Date drafted:** 2026-05-10
**Branch to create at session start:** `claude/cross-chapter-consistency-<harness-id>` (branch from current `origin/main`)
**Status going in:** No project-wide consistency audit has been run since 2026-05-02 manuscript completion (per `project_book1_state_2026-05-02.md` memory). Drift is expected after that interval; chapters have been edited individually since.

---

## Workstream scope

Run a project-wide consistency audit across all 10 drafted chapters of *Commons Bonds* + the Tech Appendix + the Glossary. Identify:

1. **Terminology drift.** Same concept named differently across chapters (e.g., "cost severance" vs. "cost-severance" vs. "severed costs"). Style and hyphenation should match.
2. **Framework definition drift.** Same concept defined slightly differently in multiple chapters; readers reach apparently different definitions in the same book.
3. **Numerical inconsistency.** Same statistic cited with slightly different numbers in different chapters (e.g., Norway sovereign wealth fund — different totals in different places; Mondragon worker-count drift; oyster-population trajectory).
4. **Case description inconsistency.** Same case (Libby, McDowell, Mondragon, Norway, Chesapeake) described with overlapping but inconsistent details across chapters.
5. **Cross-reference integrity.** "See Ch X" references are accurate; pointed-at content actually exists in the named chapter.
6. **Citation consistency.** Same source cited the same way every time. Bibliography entries match in-text references.
7. **Italicization / formatting consistency.** Italicized terms italicized everywhere; quoted speech formatted consistently; em-dash usage consistent.
8. **Author voice consistency.** First-person narrative voice consistent; tense usage consistent within scenes.

For each finding, propose a fix: which chapter holds the canonical version; which chapter is updated to match.

---

## Why this matters

A book with terminology drift, conflicting numbers, or contradictory case descriptions reads as poorly edited. Trade-press editors and copyeditors flag these as red marks. Agents reading sample chapters (or full manuscript on submission) lose confidence in the author's discipline.

Coordinating with the Path B audit and apparatus register sweep: those workstreams handle *structural* consistency (no sentence-level reuse; apparatus register policy) — this workstream handles *surface* consistency (terminology, numbers, formatting).

---

## Methodology

1. **Build the canonical-terms inventory.** List every load-bearing framework term, every named case, every recurring statistic. Mark which chapter is the canonical home for each.
2. **Scan for drift.** Use `git grep` for each canonical term — verify every occurrence matches the canonical spelling/format. Verify every case-description is consistent with its canonical home.
3. **Verify numerical consistency.** Build a stats table: every recurring number with its source. Cross-check every chapter's use of each number.
4. **Verify cross-references.** Every "see Ch X" / "as discussed in Ch Y" / "earlier" reference — confirm the pointed-at content actually exists.
5. **Verify citation consistency.** Cross-check bibliography entries against in-text references. (This dovetails with the bibliography engagement-pending → engaged flag-update workstream in `manuscript-completion-handoff_2026-05-09.md` cross-thread item #3.)
6. **Apply fixes.** Edit chapters with surface-level corrections.
7. **Update the canonical-terms inventory** as a standing reference document.

**Per-issue effort:** small (<5 min per fix once the audit is done). **Total estimated effort:** ~6–10 hours of focused session time, mostly in the audit/scan phase.

---

## Current state

**Last whole-manuscript review:** 2026-05-02 per `project_book1_state_2026-05-02.md`. Since then:
- Ch 5 + Ch 9 Pistor/Christophers/Susskind engagement landed (commit `d78872e`)
- Bibliography engagement-pending → engaged flag updates pending (cross-thread item #3)
- Tech Appendix Phase 3 v2.0.0 rebuild queued
- Glossary v4 rebuild queued

**Coordination:**
- The bibliography flag-update is already in scope of `manuscript-completion-handoff_2026-05-09.md`. This consistency audit covers the in-text citation-reference side.
- The Glossary v4 rebuild interacts with the canonical-terms inventory built here — the Glossary should reflect the canonical decisions from this audit.
- The apparatus register decision sweep (separate handoff) interacts where terminology decisions become register decisions.

---

## Deliverables

1. **`research/audits/cross-chapter-consistency-audit_2026-05-10.md`** — audit findings: per-finding flag with severity, recommended fix, status.
2. **`manuscript/canonical-terms-inventory.md`** — standing reference: every load-bearing term, case, statistic, with canonical spelling/format and home chapter.
3. **Edits applied to chapter files** in `manuscript/chapters/`. Surface-level fixes are commit-batchable (one commit per category: terminology / numbers / cross-refs / citations / formatting).
4. **Updated Glossary** to reflect canonical decisions.

---

## First actions for fresh session

1. Read this handoff end-to-end.
2. Read `manuscript/_BookLevelGuidance.md` if it exists — may already encode some canonical conventions.
3. Read the Glossary (current state).
4. Build the canonical-terms inventory by walking each chapter's GuidanceDoc (`Chapter__N___GuidanceDoc.md`) — these were the per-chapter intent docs and likely already encode canonical framing.
5. Run grep scans for the highest-frequency framework terms and named cases.
6. Confirm inventory + drift findings with user before applying fixes.

---

## What NOT to do

- Do not rewrite content for prose-flow reasons during this audit — surface-level only. Prose polish is a separate workstream.
- Do not change framework definitions to "improve" them. This audit canonicalizes existing decisions; it does not relitigate them.
- Do not extend the audit to typo/grammar checks — that's a copyediting pass, separate workstream, post-acquisition.

---

## Reference files

- `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md` through `Chapter_10_CommonBonds__Draft.md`
- `manuscript/chapters/Chapter__N___GuidanceDoc.md` for each chapter (per-chapter intent docs)
- `manuscript/chapters/_BookLevelGuidance.md`
- Glossary (location varies; check `manuscript/`)
- Tech Appendix
- `research/literature/bibliography.md`
- `tools/workstream-handoffs/manuscript-completion-handoff_2026-05-09.md` (overlapping bibliography flag-update workstream)

---

*End of handoff.*
