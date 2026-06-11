# tools/back-matter/ — reader-facing back-matter generator + scaffolding companions

**Created 2026-06-09 (back-matter consolidation session).** This directory holds the
INTERNAL scaffolding for the book's reader-facing back matter: the generator, the citation
cross-reference index, and the glossary consolidation ledger. The CLEAN, zero-scaffolding,
reader-facing outputs live in **`manuscript/back-matter/`** and are GENERATED from here.

## The two-layer model

```
INTERNAL source-of-truth (.md/.html, scaffolding kept)        →  generator  →  READER-FACING (.html, clean, anchored)
  research/literature/bibliography.md   (superset master)     →  gen-bib     →  manuscript/back-matter/bibliography.html
  core/glossary/...v4.html              (canonical glossary)  →  gen-glossary→  manuscript/back-matter/glossary.html
  manuscript/technical-appendix/symbol-registry_2026-06-07.md       →  gen-notation→  manuscript/back-matter/symbol-registry.html
```

Reader-facing files carry **no** scaffolding: no SUPERSEDED/RETIRED/PROPOSED markers, no
Status/Confidence/Where-cited/Rigor-provenance fields, no internal-ledger pointers. Each
bibliography entry and glossary term carries a stable `id=` anchor so a TA / chapter / essay
citation link can deep-link straight to it.

> **Source files stay in their current homes for now** (build-new / defer-moves decision,
> 2026-06-09): a live redraft campaign reads `bibliography.md`. Relocating the source files
> into this directory is a deferred post-campaign pass (see the deferred-moves handoff in
> `tools/workstream-handoffs/`).

## Files here

- `build.py` — the generator (stdlib only). Commands below.
- `citation-crossref-index.md` — per bib entry: where it is cited across the corpus
  (TA / chapters / essays / op-eds), with ORPHAN flags for prune candidates. Review aid.
- `glossary-consolidation-ledger.md` — v2/v3/v4 lineage, canonicity decision, retired-terms
  inventory (kept out of the reader-facing glossary), v3→v4 regression check.

## Usage

```bash
python3 tools/back-matter/build.py gen-all       # regenerate all three reader-facing .html
python3 tools/back-matter/build.py gen-bib        # bibliography.html only
python3 tools/back-matter/build.py gen-glossary   # glossary.html only
python3 tools/back-matter/build.py gen-notation   # symbol-registry.html only
python3 tools/back-matter/build.py fold-report    # diff TA §18 vs master (review aid)
python3 tools/back-matter/build.py crossref       # rebuild the citation cross-ref index
```

Re-run `gen-all` after editing any source file; the reader-facing outputs are derived,
never hand-edited.

## Known limitations (first generated pass — author review pending)

- The bibliography includes the cleanly `*Backs:*`-delimited primary-data/agency sources
  (§23.1 + §24A–J). The **compact claim-led §23.3 sources are EXCLUDED** (their format leads
  with the backed claim, not a citation) and need a source-format normalization or manual
  curation before they can be generated cleanly. §23.2 (candidates) and §24K (pending) are
  intentionally excluded.
- Surname/anchor slugs for institutional authors are heuristic (first 4 tokens).
- Generated HTML is a first pass; author reviews the diff before any merge to main.
