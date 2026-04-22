# research/case-studies/

**Purpose:** Staging for standalone case-study writeups that may eventually support the book beyond what fits in the main chapter drafts.

## Current state (as of 2026-04-22)

This folder is intentionally empty. All canonical case-study content for Book One lives **inline in the chapter drafts**:

| Case | Current home |
|---|---|
| Appalachian coal (McDowell County) | `manuscript/chapters/Chapter__2_TheMiner__Draft.md` |
| Norway sovereign wealth fund | `manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md` |
| Libby vermiculite (W.R. Grace asbestos) | `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` |
| Deepwater Horizon (BP oil spill) | `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` |
| Exxon Valdez | `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` |
| Baotou rare earths | `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` |
| Mars / off-Earth thought experiment | `manuscript/chapters/Chapter__7_TheColonyAdministrator__Draft.md` |

The chapter-inline approach is canonical for Book One — the framework is applied directly in each chapter as the mechanism is introduced, rather than catalogued separately here.

## When new content lives here

Use this folder for case-study material that is **not (yet) committed to a specific chapter**. Typical reasons:

- A case you want to write up but haven't decided which chapter integrates it (e.g., Nigeria contrast case for Ch. 4, Social Security case for Ch. 5 — currently living in `archive/Consider Including/` and `archive/_One Day Maybe/` pending integration).
- Scholarly extension material beyond Book One's chapter scope — longer-form writeups for academic audiences, supplementary materials for reviewers, reference cases for Book Two.
- Cases being researched but not yet ready for chapter integration — working notes, data collection, early drafting.

## Relationship to chapter drafts

When a case is ready for chapter integration, its content migrates from here (or from `archive/Consider Including/` / `archive/_One Day Maybe/`) into the relevant chapter draft. The standalone writeup either (a) stays here as a longer-form companion piece that the chapter compresses, or (b) moves to `archive/` as a source document that's been consumed.

## Intake workflow (for new case-study material)

1. **Capture:** raw notes, data, interviews, scholarly references land in a dated subfile (e.g., `2026-MM-DD-case-name-notes.md`).
2. **Draft:** a standalone case-study writeup following a consistent template (scope / mechanism demonstration / data / counterarguments / framework fit / implications).
3. **Extract:** identify what the relevant chapter needs from the case — the paragraphs, examples, or numbers that carry the chapter's argument.
4. **Integrate:** migrate the extracted portions into the chapter draft with appropriate framing. Cross-reference the full case-study file here for any reader who wants the longer version.
5. **Retain or archive:** the standalone case-study file stays here if it has continuing value (companion piece, scholarly reference); archives if fully consumed.

## Related subfolders (pattern extension)

This same staging-and-extract pattern applies to other research subfolders being considered:

- **`research/interviews/`** — raw and processed interview material (watermen at Fort Monroe, potential McDowell County residents, potential Norway fund contacts, etc.). Same intake workflow: capture → transcribe → extract relevant passages → integrate into chapters → retain original for reference.
- **`research/authors-stories/`** — Chris's own lived experience as raw material for Ch. 1 (plane, IT career, wife's illness, 120-hour weeks, Savannah), Ch. 7 (NASA Langley grandfather, healthcare IT transitions), Ch. 10 (harbor, watermen visible from living situation, meaning-making). Same workflow adapted for first-person material.
- **`research/literature/`** — scholarly background (currently holds `commons_bonds_economic_theory_reference - consider including 6.html` moved from `archive/Consider Including/`).
- **`research/methodology/`** — methodology-specific research (currently holds `commons_bonds_full_economy_simulation.html`).

Each subfolder serves the same two-step function: preserve the raw source material long enough to work with it properly, then extract what the book needs while keeping the source available for future reference.

## Watch items

- **Privacy rule applies** (per `tools/claude_prefs.md`): personal financial specifics scrubbed from external-facing outputs. For `authors-stories/` especially, scrub before integrating into external manuscripts.
- **Subordinate-anonymization and NDA constraints apply** to any CEO-era material integrated from `authors-stories/` into Ch. 6 or elsewhere — see handoff v1.28.0 deferred queue for pre-drafting gates.
- **Interview consent and attribution:** when adding `research/interviews/`, establish consent protocol up front (permission to use, attribution preference, review of draft quotes before publication).

---

*This README documents the research-folder staging pattern. Same structure replicable for sibling subfolders.*
