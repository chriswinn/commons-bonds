# Back-matter consolidation — DEFERRED MOVES handoff (QUEUED)

**Date:** 2026-06-09. **Routed by:** `claude/refactor-bib-consolidation-260609-23c283`.
**Status:** 🚧 QUEUED. The back-matter consolidation session built the clean reader-facing
outputs + generator + indexes and made `bibliography.md` the single source of truth, but
**deferred all file MOVES** (author-ratified "build-new / defer-moves," 2026-06-09) because a
live redraft campaign reads/writes the affected files. This handoff lists the deferred work for a
follow-up session to execute once the blockers clear.

## What already shipped (on branch / under author diff review — NOT a move)

- `manuscript/back-matter/{bibliography,glossary,symbol-registry}.html` — clean reader-facing, generated.
- `tools/back-matter/{build.py, citation-crossref-index.md, glossary-consolidation-ledger.md, README.md}`.
- `research/literature/bibliography.md` — §25 fold-in (now the superset master).
- `core/technical-appendix/symbol-registry_2026-06-07.md` — synced to merged TA.
- TA §18 — Himmelstein fix + unified-bib pointer.
- `core/technical-appendix/notation-alignment-proposal_2026-06-09_PROPOSED.md` — WS3 (apply nothing).

## Deferred move 1 — relocate source-of-truth files into `tools/back-matter/`

Currently the sources stay in their historical homes (many live references):
`research/literature/bibliography.md`, `core/terms/terms_index.md`,
`core/technical-appendix/symbol-registry_2026-06-07.md`, `core/glossary/...v4.html`.
**When safe:** move these under `tools/back-matter/sources/` (or co-locate), update `build.py`
paths + every handoff/README/CLAUDE.md reference to the old paths, and re-run `gen-all` to confirm.
Blast radius is wide (the redraft campaign + many handoffs cite `research/literature/bibliography.md`)
— audit references first (`grep -rl 'research/literature/bibliography.md'`).

## Deferred move 2 — reorganize the `_`-prefixed scaffolding out of `manuscript/` — ✅ EXECUTED 2026-06-10 (campaign superseded; see manuscript/README.md for the ledgers/ + archive/ layout)

~35 underscore-prefixed files sit directly in `manuscript/`. ~30 are **REDRAFT-CAMPAIGN-WORKING
(HIGH collision)** — moving them breaks campaign continuity. Safe-to-move-now subset (LOW collision):
`_CANONICAL_FIGURE_LEDGER.md` (author-owned, keep or → `tools/quality-gates/`),
`_CANDIDATE-BEATS-AND-DEVICES.md` (→ `tools/drafting-templates/`), the Ch1 comparison pair
(Ch1 redraft done → archive). Everything else waits for the redraft campaign to close, then:
per-chapter `_CH*-COMPARISON`/`_CH*-COHERENCE` → per-chapter rigor or `archive/`; lens/ledger files
(`_contribution-matrix-*`, `_cross-chapter-ledger`, `_essay-reveal-*`, `_book-coherence-*`,
`_CITATION_EVIDENCE_*`, `_RESEARCH-RESULTS-*`, `_DANGLING-REFERENCE-*`, `_SEAM-MAP-*`) →
`tools/rigor-passes/redraft-campaign/`; control docs (`_BOOK-REDRAFT-ACTION-LIST`,
`_REDRAFT-CAMPAIGN-RESUME`, `_REDRAFT-COMPARISON-SUMMARY`) → `tools/workstream-handoffs/` as record.
Keep `_BOOK_MANIFEST.md` discoverable (it is the "what is the book" authority).

## Deferred move 3 — execute the manifest's TA → `manuscript/technical-appendix/` relocation

`_BOOK_MANIFEST.md` already proposes relocating `core/technical-appendix/` → `manuscript/`
(currently a symlink points back). This needs a render-toolchain + rigor-artifact + README path
audit before executing (per the manifest). Independent of the back-matter work; sequence whenever.
When done, the back-matter set could also sit under `manuscript/` as full book back matter (it
already does: `manuscript/back-matter/`).

## Deferred coverage 4 — §23.3 primary-data sources into the reader-facing bibliography

The generator includes the cleanly `*Backs:*`-delimited data sources (§23.1 + §24A–J) but EXCLUDES
the compact claim-led §23.3 sources (their bullets lead with the backed claim, not a citation).
To include them: normalize each §23.3 bullet to lead with the citation (source-first), then re-run
`gen-bib`; or curate them manually. §23.2 (candidates) + §24K (pending) stay excluded by design.

## Deferred fix 5 — book-proposal `00_overview.md` status-header leak

Per the WS4 audit (`tools/audits/back-matter-scaffolding-audit_2026-06-09.md`):
`publishing/book-proposal/00_overview.md:5` opens with a `**Status.** RATIFIED … Pass 3.x … Stage 5`
block that must not ship to agents/editors. Owned by the live `book-proposal-sprint` session — let
that session strip it (or confirm package-assembly strips status headers).

## Deferred verify 6 — glossary "Abundance Dimension" disposition

Per the consolidation ledger: "Abundance Dimension" is in glossary v3 but absent from v4 with no
obvious rename. Confirm intentional (likely folded into the commons-categories + abundance-state
framing) and record the disposition; not a reader-facing blocker (the glossary follows v4).

## Deferred apparatus 7 — in-TA "Notation" section (technical-review window, NOT Wave 1)

Author-confirmed direction (2026-06-10): symbols live in the TA PDF, so the reader-facing notation
belongs **at the top of the TA itself** (same document as the formulas; anchored for flip-and-follow),
separate from the Glossary, cross-linked on the ~9 dual entries (B, RCV, CSD, CS, S, E, IPG, CIT, SCS).
Generate it from registry **Part 7** (the deduplicated canonical list) and insert near the TA top.
Keep the standalone `manuscript/back-matter/symbol-registry.html` as a mirror. **Deferred:** not on the
Wave-1 (literary-agent) path — the apparatus does not ship to agents; this serves the technical reviewer
+ eventual publisher. Render verified tofu-free 2026-06-10 (`tools/scripts/check-glyph-coverage.py`).

## Deferred apparatus 8 — Part 7 completeness fold-in (~20 compound/subscripted symbols)

Registry Part 7 currently bundles some compound forms. For an exhaustive notation key (any formula
symbol findable), add the standalone subscripted/compound symbols: S_max, S_base(t), S_threshold, S*,
Q_critical, t₀, t, r_min, r_∞, D_∞, A_ε, U₀, E₀, c₀, C(x,t), V(x,t), SW, g(t), k, m, x, n, i. Then
re-run `gen-notation`. Pairs with item 7 (same technical-review window).

## Spawn-readiness check (run before executing moves 1–2)

```bash
git -C /Users/c17n/commons-bonds worktree list | grep -iE "redraft-campaign|book-proposal"
# Expect NO active redraft-campaign worktree before moving the _-prefixed manuscript files
# or relocating research/literature/bibliography.md.
```
