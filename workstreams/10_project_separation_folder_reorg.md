Commons Bonds — Workstream 10: Project Separation + Folder Reorganization


# Workstream 10 — Project Separation + Folder Reorganization

Commons Bonds project · Safe housekeeping · No content risk · Can run any time after the chapters that reference source files have been updated

**Prerequisite:** None, strictly speaking. But a few source files in this workstream are referenced by Workstreams 03, 04, 05, 06, 07. If this workstream runs first and moves those sources before the chapter workstreams have pulled content from them, the chapter workstreams will have to go fetch them from new locations. Recommended sequencing: run this workstream *after* the chapter workstreams that consume the source files, or at minimum verify each file's content has been migrated before archiving.

**Option C quick reference:** Two pillars (Cost Severance, RCV) + two methodologies (Abundance Inversion Test, Universality Test). Retired: V\_civ, Solidarity Architecture, Departure Liability, ESG.

## What this workstream does

Three jobs, all low-risk:

1. **Separate non–Book One projects** that have accumulated in the main Commons Bonds folder. Counter-Vance healthcare-extraction research, democratic-socialism discussion material, and the delegitimization satellite essay are all related intellectual projects but they are not Book One. They need their own folders so the Commons Bonds folder stays clean and focused.
2. **Archive session-dump files** once their content has been distributed to the cleaner April 19 consolidated files. These are working-session transcripts and brainstorm dumps; they served their purpose, and their continued presence in the active folder creates noise.
3. **Delete known duplicates** (one exact duplicate confirmed).

This workstream is deliberately scoped to operations that cannot break anything. No content is created or modified. Everything is moved, archived, or (in one case) deleted as duplicate.

## Target folder structure

```
/Commons Bonds/                          (root — Book One only)
├── Chapter drafts (1–10)
├── commons_bonds_updated_glossary.html
├── commons_bonds_technical_appendix_COMPLETE.html
├── Commons Bonds - Ripple Effects
├── Commons Bonds - Dedication
├── Commons Bonds - AUTHOR'S NOTE: ON WIND TUNNELS AND AI
├── Commons Bonds: Make It Better
├── Commons Bonds Publishing Strategy - Consolidated Plan
├── Commons Bonds: Book One - Commons Bonds - Path & Book Two - ...
│
├── /Berggruen Institute - Essay/       (untouched — competition prohibits AI)
├── /Noema/                              (untouched — submitted)
│
├── /Archives/                           (historical working material)
│   ├── Session dumps (April 19 and earlier)
│   ├── Superseded HTML artifacts
│   ├── Retired working documents from Workstream 09
│   └── Older versions of technical appendix, glossary, etc.
│
├── /Research/                           (scholarly background, not book content)
│   └── commons_bonds_economic_theory_reference 6.html
│
└── /_One Day Maybe/                     (satellite projects + Book Two seed)
    ├── /Book-Two-Subsidy-Economy/       (from Workstream 07 trim)
    │   ├── Chapter 8 trimmed material
    │   └── Counter-Vance Book-Two-adjacent content
    ├── /Counter-Vance/                  (healthcare extraction argument)
    ├── /Democratic-Socialism/           (book discussion notes)
    └── /Satellite-Essays/               (delegitimization essay + future satellites)
```

## File-by-file action table

### Move out of the Commons Bonds root

| File | Action | Destination | Why |
| --- | --- | --- | --- |
| `counter_vance_research_notes - consider including 5.html` | Move | `/_One Day Maybe/Counter-Vance/` | Separate project. Contains Unified Extraction Loop framework, GoFundMe data, tax-gap data, housing data, Butler/Quill end-of-life material. Book-Two-adjacent (see Workstream 07 note). |
| `democratic_socialism_book_discussion 7.html` (or similar title) | Move | `/_One Day Maybe/Democratic-Socialism/` | Separate intellectual project. Related to Book Two strategic thinking but not Book One content. |
| `commons_bonds_satellite_idea_delegitimization 8.html` | Move | `/_One Day Maybe/Satellite-Essays/` | Freestanding essay idea. Per publishing strategy (establish Commons Bonds vocabulary first before standalone application pieces), this is a "later" essay. Hold separately. |
| `commons_bonds_economic_theory_reference 6.html` | Move | `/Research/` | Scholarly background. Reference material for Technical Appendix literature engagement, not book content itself. |

### Archive (move to `/Archives/`)

| File | Condition for archiving |
| --- | --- |
| `session_notes_april_19_2026` (or similar session-dump title) | After verifying content captured in April 19 consolidated files (eight-tier, villain-analysis, vocabulary-additions, success-criteria, two-book-strategic-analysis, chapter-1-extension, commons-consider-including 12). |
| `new_material_april_19_2026 - Placeholder` (or similar) | Same condition. |
| `critical_impact_assessment` | Same condition. Verify its critical observations are captured in either Workstream 01 (decisions), Workstream 09 (old-material audit), or a consolidated file. |
| `new_material_from_sociology_chat` (or similar) | Same condition. The sociology-paper material should stay with the SOC200 paper; anything that seeded book content should be captured there. |
| Source files whose content has been migrated into chapter drafts / glossary / appendix | Archive only *after* the relevant workstream has completed and verified the migration: • `commons-bonds-eight-tier-decomposition 9.html` → after Workstreams 02, 03, 08 • `commons-bonds-vocabulary-additions 13.html` → after Workstream 02 • `commons-bonds-chapter-1-extension 14.html` → after Workstream 04 • `commons-bonds-villain-analysis 15.html` → after Workstream 06 • `commons-bonds-success-criteria 11.html` → after this is used to validate all other workstreams; can stay in root as reference • `commons-bonds-two-book-strategic-analysis 10.html` → after Workstream 07; consider keeping in `/_One Day Maybe/Book-Two-Subsidy-Economy/` as reference for the eventual Book Two • `Commons Bonds - Nigeria Contrast Case` → after Workstream 05 • `commons - consider including 12.html` → after Workstream 05 |
| Older versions of Technical Appendix (truncated 19,164-byte version per Session Archive) | After Workstream 08. The COMPLETE version is canonical. |
| Any document retired in Workstream 09 (likely `commons_bonds_integrated_framework.html` and `commons_bonds_chapter_assessment.html`) | Execute after Workstream 09 issues the retirement verdict. |

### Delete (confirmed duplicate)

| File | Reason |
| --- | --- |
| `commons - consider including 9.html` | Exact duplicate of `commons - consider including 12.html` (Social Security case). Verified during Workstream 05 preparation. Delete. No archive needed — duplicate content. |

### Keep in root, untouched

| File | Why |
| --- | --- |
| All chapter drafts (1–10) | Active book content. |
| `commons_bonds_updated_glossary.html` | Active after Workstream 02. |
| `commons_bonds_technical_appendix_COMPLETE.html` | Active after Workstream 08. |
| `Commons Bonds - Ripple Effects` | Active after Workstream 09 update. Master checklist doc. |
| `Commons Bonds - Dedication` | Book content. |
| `Commons Bonds - AUTHOR'S NOTE: ON WIND TUNNELS AND AI` | Book content. |
| `Commons Bonds: Make It Better` | Active working document; updated across sessions. |
| `Commons Bonds Publishing Strategy - Consolidated Plan` | Active after Workstream 07 update. |
| `Commons Bonds: Book One... & Book Two... Path` | Active after Workstream 07 update. |
| `$100 Barrel: Commons Bonds` | Companion piece. Verify vocabulary alignment (Workstream 06 sweep touches). |
| `/Berggruen Institute - Essay/` folder | Do not touch (competition prohibits AI content). |
| `/Noema/` folder | Do not touch (submitted). |
| `commons-bonds-success-criteria 11.html` | Reference for all workstreams. Useful to keep in root until the book is further along. |

## Subfolders to create

1. `/Archives/` — if not already present
2. `/Research/` — if not already present
3. `/_One Day Maybe/Book-Two-Subsidy-Economy/`
4. `/_One Day Maybe/Counter-Vance/`
5. `/_One Day Maybe/Democratic-Socialism/`
6. `/_One Day Maybe/Satellite-Essays/`

The `/_One Day Maybe/` parent folder already exists.

## Rigor check on the separated material

None of the material being moved needs rigor-testing against Option C, because none of it is being integrated into Book One. The only rigor question is scope: does it belong in Book One? For each item below, the answer is no — hence the move.

| Item | Why it is not Book One |
| --- | --- |
| Counter-Vance healthcare extraction argument | Applied policy argument targeting a specific political narrative. Book Two territory (named beneficiaries, advocacy exposure). |
| Butler / Quill end-of-life extraction | Healthcare-system critique. Raises nursing-career exposure (Two-Book Vulnerability 4). Defer. |
| GoFundMe / tax-gap / housing data clusters | Empirical advocacy material. Book Two data. |
| Democratic socialism book discussion | Political-system framework discussion. Book Two or standalone later project. |
| Delegitimization satellite essay | Freestanding essay pre-requires Commons Bonds vocabulary being established; per publishing strategy, hold until after Book One is in circulation. |
| Economic theory reference doc | Scholarly background, not book content. Useful for Technical Appendix literature engagement. Lives in `/Research/`. |

## Old material to test against current rigor

The files being archived were each produced under earlier rigor standards. None of them is being re-tested for inclusion in Book One — they are being archived because their useful content has been consolidated elsewhere or because they are being held for a later project. The test, such as it is, is: *has the useful content been captured elsewhere?*

That capture-verification is the only work this workstream does beyond file operations.

## New material to integrate

None. This workstream is purely organizational.

## Watch items

- **Do not delete anything except the confirmed duplicate.** Everything else moves or archives. The project is two months of intense intellectual work; archiving is cheap; deletion is irreversible. When in doubt, archive.
- **Do not move a source file before the workstream that consumes it has completed.** If the chapter workstreams haven't pulled content from (e.g.) `commons-bonds-eight-tier-decomposition 9.html`, moving it to `/Archives/` means the next chapter workstream session has to re-discover its location. The Google Drive path is the friction. Keep sources in root until consumed, then archive.
- **Do not rename anything in this workstream.** Renaming creates broken references in chapters, cross-file links, and your own mental map. Renaming is a separate operation to be done deliberately if ever.
- **Do not archive Ripple Effects, Make It Better, Publishing Strategy, or Success Criteria.** These are active working documents. Archiving them disables the checklist function they serve.
- **Do not move the Technical Appendix or Glossary.** These are book apparatus and belong in root with the chapters.
- **Do not touch `/Noema/` or `/Berggruen Institute - Essay/`.** Noema is submitted. Berggruen competition prohibits AI-generated content; commingling any AI-assisted file with that folder is a risk to the submission.
- **Archive does not mean hidden.** You should still be able to find archived material easily. Google Drive search crosses folders. If a file moves to `/Archives/`, note in your next-session context that the file was archived on (date) if you expect to reference it.

## Check before ending the session

1. Six new subfolders created.
2. Four separation moves executed (Counter-Vance, Democratic-Socialism, Satellite-Essays, Research).
3. Session-dump files verified against April 19 consolidated files; archived only if content captured.
4. Confirmed duplicate (`commons - consider including 9.html`) deleted.
5. Older Technical Appendix versions archived.
6. Documents retired in Workstream 09 moved to `/Archives/`.
7. Source files whose content was consumed in Workstreams 02–08 archived *only after* the consuming workstream completed.
8. `/Noema/` and `/Berggruen Institute - Essay/` untouched.
9. Root folder now contains only active Book One content: chapters, glossary, appendix, ripple effects, dedication, author's note, make it better, publishing strategy, path doc, success criteria, $100 barrel.

## After this workstream

The Commons Bonds folder is a clean Book One workspace. Satellite projects are organized for future work without cluttering the active drafting environment. Historical working material is preserved but out of the way. The path from "open folder" to "find the chapter you are working on" is short. That is the whole point.
