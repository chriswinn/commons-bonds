---
artifact: workstream-handoff
type: corpus-hygiene-spot-check
scope: cross-essay-publishing-pipeline
date: 2026-05-27
status: PROPOSED (awaiting author fire post-Aeon-submission)
trigger-source: 2026-05-27 Aeon pitch evolution audit F-EVO-AUDIT-1
---

# Cross-essay corpus-hygiene spot-check — workstream handoff (2026-05-27)

**Trigger.** 2026-05-27 Aeon pitch evolution audit discovered that
`publishing/essays/aeon-mask-of-abundance/essay.md` contains the
REJECTED audience-blind Pitch B Stage 2 draft, not the canonical
submission text. Root cause: 2026-05-21 publishing-pipeline reorg
(commit `52fde31`, "50 file moves + 10 READMEs") placed the loser of
the Stage 3 comparison at the canonical `essay.md` slot instead of
the winner. The same reorg touched every essay directory under
`publishing/essays/`, so the same loser-takes-canonical-slot pattern
may exist in other venues that ran the two-stage drafting discipline
experiment.

**Cross-references:**
- Triggering audit: `publishing/essays/aeon-mask-of-abundance/rigor/evolution-audit_2026-05-27.md` F-EVO-AUDIT-1
- Reorg commit: `git show 52fde31` (50 file moves)
- Two-stage discipline doctrine: `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`

**When to fire.** POST-AEON-SUBMISSION (after Sun May 31 14:01 UTC).
Aeon-only file-org remediation (audit §7.1 paste-text) is the
PRE-SUBMIT priority; this cross-essay sweep is the broader audit
that follows.

**Session role.** Corpus-hygiene spot-check across every essay
directory under `publishing/essays/`. Identify whether the same
loser-takes-canonical-slot pattern exists in other venues; apply the
same file-org fix where it does; report findings.

---

## Scope

Every directory under `publishing/essays/`:

- `publishing/essays/aeon-mask-of-abundance/` (= the one Aeon audit
  already covers; verify the Aeon-only fix from §7.1 has been
  applied; skip if so)
- `publishing/essays/noema-commons-bonds/`
- `publishing/essays/boston-review-essay/` (verify exact path)
- `publishing/essays/100-barrel-essay/` (verify exact path)
- `publishing/essays/atlantic-ideas-essay/` (verify exact path)
- Any Wave 2 candidate directories
- Any other `publishing/essays/<venue>/` directories that exist

Per-essay check protocol:

1. **Open `<venue>/essay.md`** (if exists; if not, note absence —
   the venue may use a different filename convention).
2. **Read the header.** Does it self-identify as the canonical current
   submission cut? Or as an experimental/rejected/audience-blind
   variant?
3. **Inventory `<venue>/_archive/prior-versions/`** if exists. Are
   there sibling files claiming ratified-submission status that
   conflict with what's at `<venue>/essay.md`?
4. **Inventory `<venue>/submission-day-package_*.md`** if exists.
   Where does the §"Cross-references" or §"Pitch source" point —
   at `essay.md` or at `_archive/prior-versions/...`?
5. **Cross-reference rigor-pass artifacts.** Search
   `tools/rigor-passes/` for `*<venue>*` artifacts. Which file path
   do they identify as the audit target? Does that path match the
   current `essay.md`?

Per-essay verdict:

- **CLEAN** — `essay.md` is the canonical current submission cut;
  cross-references resolve correctly; no fix needed.
- **CONFUSED** — `essay.md` is an experimental/rejected variant; a
  sibling under `_archive/` is the actual canonical text. Apply
  Aeon-pattern file-org fix.
- **INCONSISTENT** — cross-references point at conflicting files
  (e.g., submission-day-package points at `essay.md` but rigor-pass
  artifacts audit `_archive/...`). Surface for author disposition;
  do not auto-fix.

---

## DO

1. Create isolated worktree per session-start discipline (workstream
   slug: "cross-essay-file-org-audit").
2. Build the full essay inventory FIRST via
   `find publishing/essays/ -maxdepth 2 -type d` and report which
   venues exist.
3. Per-essay check protocol per §"Scope" above. For each venue,
   produce a one-paragraph verdict (CLEAN / CONFUSED /
   INCONSISTENT).
4. Drip-feed findings to author ONE-AT-A-TIME per parallel-session
   cadence discipline. Each CONFUSED finding gets author disposition
   before fix applies.
5. For each CONFUSED finding the author ratifies, apply the
   Aeon-pattern fix:
   a. `git mv <venue>/essay.md <venue>/_archive/prior-versions/<descriptive-archive-name>.md`
   b. Create new `<venue>/essay.md` with canonical current submission
      text + appropriate header.
   c. Update cross-references (submission-day-package + README +
      carry-forward-inventory).
   d. Verify all paths resolve.
6. For each INCONSISTENT finding, surface to author + pause; do not
   auto-fix.
7. Commit per-venue (one venue per commit, or grouped by tier if
   multiple CLEAN). Fast-forward to main per CLAUDE.md
   merge-to-main default (this is internal-scaffolding work).
8. Produce a final summary report: which venues were CLEAN /
   CONFUSED / INCONSISTENT; which fixes applied; any remaining
   author-decision items.

---

## DO NOT

- Modify any essay's prose. File-org fix only.
- Apply fixes without author ratification per finding.
- Delete archived experimental drafts. They're historical record.
- Touch any rigor-pass artifacts (these reference older file paths
  intentionally as historical record of what was audited at the time;
  the artifact's audit target stays pointing at the path that existed
  at the time of the audit).
- Auto-fix INCONSISTENT findings.

---

## Expected output

- Per-venue verdict (CLEAN / CONFUSED / INCONSISTENT) — drip-fed.
- Per-CONFUSED-venue fix applied (with author ratification).
- Per-INCONSISTENT-venue escalation to author (no auto-fix).
- Final corpus-hygiene summary report.
- All file-org changes auto-merged to main per CLAUDE.md default.

**Expected session length:** ~30-80K tokens (depending on how many
venues need fixes; ~5-12 venues likely; per-venue check + fix is
~5-10K tokens).

**Author ratification load:** ~5-12 per-venue dispositions + any
INCONSISTENT escalations.

---

## Notes

- This is internal-scaffolding work (file organization), not
  end-user-facing prose modification. Auto-merge to main at session
  close per CLAUDE.md merge-to-main default.
- Rigor-pass artifacts under `tools/rigor-passes/` reference older
  file paths AT THE TIME of the audit. Do NOT update those — they're
  historical records of audit targets, and the path-at-time is a
  load-bearing part of the audit's chain of custody.
- This handoff itself is the durable record of the cross-essay
  spot-check scope. Update it with findings + actions as the
  workstream fires.
