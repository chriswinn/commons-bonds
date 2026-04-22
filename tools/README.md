# tools/ — Canonical Working Methodology

This folder holds the canonical methodology documents for the Commons Bonds project — the set of files uploaded to Claude at the start of each work session.

**Convention:** `tools/` top-level = session upload set. Subfolders = session-upload-adjacent material (recent pass records, triage inputs, superseded versions).

---

## Session-start upload set

For any substantive session work, upload these files plus the current session handoff (from `alignment/sessions/`):

| File | What it does |
|---|---|
| `tools/claude_prefs.md` | Operating preferences, file-format rules, privacy rules, Commons Bonds operating core |
| `tools/commons_bonds_rigor_protocol_v1.2.2.md` | Canonical rigor protocol — test battery (~26 tests), 25-character pressure suite, routing rule, full/light rigor axis |
| `tools/commons_bonds_guiding_constraints_v1_0_0.md` | Canonical Group D (strategic / publishing-path) + Group E (success criteria) inputs |
| `tools/commons_bonds_abundance_dimensions_v1_1_0.md` | Methodology document for the 10 abundance dimensions (retitled from `abundance_layers_v1_0_0.md` 2026-04-22; Priority-1 naming cohort complete — Habitability, Kindred, Ecosystem locked) |
| `tools/commons_bonds_book_scope_v1_0_3.md` | Canonical Book One scope |
| `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-22_v1_0_1.md` | Most recent rigor pass record (Part 2, session v1.28.0) |

Plus the current session handoff from `alignment/sessions/`.

---

## Subfolders

### `tools/rigor-passes/`

Historical audit trail of rigor passes. The most recent pass record is part of the session-upload set; older records stay here for lineage. Naming pattern: `commons_bonds_rigor_pass_YYYY-MM-DD_v#_#_#.md`.

### `tools/triage/`

Triage files that fed specific rigor passes — one-session inputs that may be referenced if returning to the pass's topic. Upload at session start only if working on the triage's topic. Naming pattern: `commons_bonds_{topic}_triage_v#_#_#.md`.

### `tools/archive/`

Superseded versions of canonical methodology docs — older book scope versions, older rigor protocol versions, older pass records, deprecated candidates. Not uploaded; retained for lineage.

---

## Related content outside tools/

These are referenced from `tools/` content but live elsewhere:

| Location | What's there |
|---|---|
| `alignment/patches/` | **Architectural C-patches** (c2 scale-abstract, c3 mechanism-shield, c4 decision-A-sweep, c5 two-path-rigor, c9 AIT-canonical-positioning, tier-2a rename). Referenced by the rigor protocol as source material for specific tests. Not typically uploaded at session start; protocol incorporates their content operationally. |
| `alignment/sessions/` | Session handoffs (current at top level; older in `archive/`). Current handoff is first upload at session start. |
| `alignment/decisions/` | Project-meta decisions — housekeeping reviews, workstreams-superseded mapping, sociology-paper-to-book transition, c6 decision memos. Uploaded on demand when relevant. |
| `core/` | Canonical framework content (eight-tier decomposition, glossary, technical appendix — math-heavy `.html` that stays `.html` per watch items). |
| `manuscript/chapters/` | Chapter drafts + guidance docs. Uploaded on demand when drafting/revising. |
| `research/case-studies/` | Standalone case study files (Appalachian coal, Norway SWF, Libby, Deepwater Horizon, opioid-extraction-Appalachia, 2008-financial-crisis, healthcare-end-of-life, housing-enforced-immobility, tax-tradeoff-US-Sweden). Uploaded on demand. |
| `research/literature/bibliography.md` | Consolidated bibliography with support/contradict annotations. Upload when scholarly engagement is active. |

---

## Copy-paste session-start block (from handoff v1.28.0)

```
Please read these files before responding:
- commons-bonds-session-handoff-2026-04-22_v1_28_0.html
- commons_bonds_rigor_protocol_v1.2.2.md
- commons_bonds_guiding_constraints_v1_0_0.md
- commons_bonds_abundance_dimensions_v1_1_0.md
- commons_bonds_rigor_pass_2026-04-22_v1_0_1.md
```

(Add `claude_prefs.md` and `commons_bonds_book_scope_v1_0_3.md` if they're not already session-implicit context.)

---

## Naming conventions

| Type | Pattern |
|---|---|
| Methodology / handoff / scope | `commons_bonds_{topic}_v#_#_#.md` or `.html` |
| Rigor pass records | `commons_bonds_rigor_pass_YYYY-MM-DD_v#_#_#.md` |
| Triage files | `commons_bonds_{topic}_triage_v#_#_#.md` |
| Architectural patches | `c{N}_{topic}_patch.md` or `{topic}_patch.md` (in `alignment/patches/`) |
| Session handoffs | `commons-bonds-session-handoff-YYYY-MM-DD_v#_#_#.html` (in `alignment/sessions/`) |
| Chapter drafts / guidance | `Chapter_#_Title_Draft.md` / `Chapter_#___GuidanceDoc.md` (in `manuscript/chapters/`) |

Versioned files: `_v#_#_#` suffix; increment rightmost digit per minor update.

---

## Notes for agents working in this folder

- **Math files stay `.html`** — never convert `.html` to `.md` for math-heavy content (eight-tier decomposition, technical appendix, error-out, glossary).
- **Privacy rule active** — scrub personal financial specifics from external-facing outputs by default.
- **Never write to Google Drive.** Drive-specific heredoc truncation risk. Drive uploads are manual on Chris's side.
- **Worktree writes + merges + pushes** are validated workflow as of 2026-04-22 (session v1.28.0). See `claude_prefs.md` §1 for current collaboration rules.
- **Hard rules** — never touch `/Noema/` or `/Berggruen Institute - Essay/` Drive folders; never rename Drive files.
