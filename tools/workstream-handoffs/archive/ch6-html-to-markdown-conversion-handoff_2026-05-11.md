# Chapter 6 HTML → Markdown Conversion — Workstream Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch to create at session start:** `claude/ch6-html-to-markdown-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Status going in:** Not blocked. Surfaced during 2026-05-11 session (Tech Appendix numbering reconciliation) when format-discipline question pivoted into draft-format-vs-submission-format territory. Flagged as companion workstream candidate in `publishing-pipeline-handoff_2026-05-11.md`.

---

## The substantive issue

Chapter 6 (`manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`) is the **only chapter in HTML format**; all 9 other narrative chapters + AuthorsNote are markdown. The hybrid-format anomaly creates:

- **Editing friction** — every apparatus sweep, rigor pass, or polish edit on Ch 6 happens against HTML markup rather than clean prose. The friction is small per edit but recurring; Ch 6 has been edited heavily during 2026-04 → 2026-05 (apparatus register sweep Items 9 + 10 + 14, Path B audit, flagship-equation defense sweep, cross-chapter consistency batches).
- **Pipeline complication** — the publishing pipeline (queued workstream `publishing-pipeline-handoff_2026-05-11.md`) needs a Ch6-specific HTML → DOCX path until conversion happens; with conversion, the pipeline is uniform Pandoc-markdown-to-DOCX for all chapters.
- **Diff readability** — git diffs on Ch 6 show HTML tag noise alongside content changes; reviewers (and your future self) see `<p>`, `<em>`, `<strong>` tags in addition to the substantive text.

The original rationale for Ch 6 being HTML was formula rendering (Ch 6 carries the canonical RCV integral, the Three Methods comparison, the convergence table). In 2026, that rationale is weak: Pandoc + LaTeX-style markdown math (`$...$` inline, `$$...$$` block) plus KaTeX/MathJax for HTML render covers the formula cases cleanly.

---

## Workstream scope

### Phase 1 — Initial conversion (~30 min)

Run Pandoc HTML → markdown conversion:

```
pandoc -f html -t markdown_strict+pipe_tables+yaml_metadata_block \
  -o Chapter__6_ThreeWaysofCounting__Draft.md \
  Chapter__6_ThreeWaysofCounting__Draft.html
```

Variations to test (Pandoc flags matter):
- `markdown_strict` vs `gfm` vs `commonmark_x` — pick output flavor that round-trips cleanest
- `--wrap=none` to avoid hard line breaks mid-paragraph
- `--atx-headers` for `##` style headers (markdown convention)

Save initial output; don't replace source yet.

### Phase 2 — Cleanup pass (~45–60 min)

Manual cleanup on the Pandoc output:

**Math notation** — Pandoc converts HTML formulas to text or to its own format; convert to LaTeX-style:
- Inline math: `$RCV(R, t_0) = \int_{t_0}^{\infty} [(1 - S(t|t_0)) \cdot U(R, t, Q(t)) + E(R, t)] \cdot D(t, t_0) \, dt$`
- Block math: surround with `$$ ... $$`
- Subscripts/superscripts: `t_0` (not `t₀` if math context; unicode OK if prose context)
- Greek letters: `\alpha`, `\beta`, `\sigma`, etc. (in math); `α`, `β`, `σ` (in prose)
- Decide: math-mode-only vs unicode-everywhere convention (recommend math-mode for formulas, unicode for inline mentions)

**Tables** — verify Pandoc converted HTML tables to markdown pipe tables correctly:
- Convergence table (Methods 1/2/3 × per-case rows) — usually the trickiest
- Sub-form tables (CAI / CCI distinction tables) — should be straightforward
- Alignment markers (`:---:`, `:---`, `---:`) preserved

**HTML entities → unicode**:
- `&sect;` → `§`
- `&mdash;` → `—`
- `&ndash;` → `–`
- `&rsquo;` → `'`
- `&ldquo;` / `&rdquo;` → `"` / `"`
- `&hellip;` → `…`
- `&times;` → `×`
- `&harr;` → `↔`
- `&minus;` → `−`
- etc.

**Hyperlinks** — verify the appendix-anchor hyperlinks added in Phase 5 (commit `50ec90b`) survived conversion:
- `[Four Gates Admission Apparatus section](../../../manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-7-four-gates)`
- `[Formula Generalization section](../../../manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-17-formula-generalization)`
- `[§8, Asymmetric Regret Rule](../../../manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-8-asymmetric-regret-rule)`

**Inline emphasis** — verify `<strong>` → `**bold**` and `<em>` → `*italic*` round-tripped cleanly; manually fix any false positives.

**Lists** — verify ordered + unordered lists preserved; check nesting depth.

**Block quotes** — verify any block quotes preserved with `>` markers.

**Headings hierarchy** — h2 → `##`, h3 → `###`, etc. Verify ATX-style consistent throughout.

### Phase 3 — Validation render (~15–30 min)

Render the markdown back to HTML via Pandoc and compare against original:

```
pandoc -f markdown -t html5 --mathjax \
  -o /tmp/ch6_roundtrip.html \
  Chapter__6_ThreeWaysofCounting__Draft.md
```

Open both in browser; visually verify:
- Math renders correctly (KaTeX/MathJax via `--mathjax` flag)
- Tables align correctly
- Hyperlinks functional
- Emphasis preserved
- No structural drift

Spot-check key passages:
- The canonical RCV integral definition
- The Three Methods comparison
- The convergence table
- The Four Gates discussion (with hyperlink)
- The Asymmetric Regret Rule paragraph (with hyperlink)

### Phase 4 — Replace source file (~5 min)

Once Phase 3 validation passes:
- Delete `Chapter__6_ThreeWaysofCounting__Draft.html`
- Commit the new `Chapter__6_ThreeWaysofCounting__Draft.md`

Pipeline downstream (publishing pipeline + apparatus sweeps + cross-chapter audits) now operates on Ch 6 as markdown like other chapters.

---

## Deliverables

By end of workstream:
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md` — converted file
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` — DELETED
- Validation round-trip render saved to `/tmp/` (not committed) demonstrating fidelity preservation

Plus: commit message documenting:
- Pandoc command used (so future conversion attempts can replicate)
- Notable manual cleanup steps applied
- Any fidelity compromises (if any — should be none for substantive content)

---

## Methodology / hard constraints

- **Substance-preserving conversion.** Content must round-trip with zero substantive drift. Visual styling may differ (HTML had CSS; markdown renders via downstream tooling); content does not.
- **Math notation discipline.** Pick LaTeX-style for formulas; unicode for inline prose mentions. Don't mix within a single passage.
- **Hyperlinks must survive.** The Phase 5 appendix-anchor hyperlinks (commit `50ec90b`) are the only cross-references in Ch 6 that need careful preservation. Verify each.
- **Don't lose the convergence table or formula tables.** These are the highest-fidelity-risk elements in the conversion.
- **Validate before deleting source.** Phase 4 deletion is irreversible-ish (git history preserves but practical recovery is friction); validate Phase 3 thoroughly first.

---

## Open questions for author ratification

1. **Math notation style** — LaTeX `$...$` (recommended; academic standard, readable in code editors with extensions, renders via KaTeX/MathJax in HTML and via Pandoc's math support in DOCX) OR alternative (unicode-only; AsciiMath; etc.)? Author judgment.
2. **Greek letters in prose** — when discussing parameters informally (e.g., "the α-dominance finding"), use unicode `α` or LaTeX `$\alpha$`? Recommend unicode for prose, LaTeX for formulas. Consistency matters.
3. **Hyperlink format** — keep inline `[text](path#anchor)` (Pandoc-friendly; cleanest in source) OR use named-reference style (`[text][1]` + `[1]: path#anchor` later)? Recommend inline.
4. **Pandoc output flavor** — `markdown_strict+pipe_tables` (most portable) OR `gfm` (GitHub-flavored; familiar) OR `commonmark_x` (CommonMark + extensions)? Recommend `markdown_strict+pipe_tables` for portability across renderers including Pandoc DOCX downstream.

---

## Coordination

- **Distinct from but related to:**
  - **Publishing pipeline (queued, `publishing-pipeline-handoff_2026-05-11.md`)** — pipeline can handle Ch 6 in either format. Sequencing: Ch 6 conversion BEFORE pipeline is cleaner (uniform Pandoc path for all chapters); pipeline could also be built first and updated to drop Ch6-specific path once conversion lands. Either order works.
  - **Tech Appendix Scheme-4 cleanup (`appendix-scheme-4-cleanup-handoff_2026-05-11.md`)** — independent; can run in any order. No file overlap.
  - **Apparatus sweeps / cross-chapter audits / Path B audits** — these workstreams routinely edit Ch 6. Schedule Ch 6 conversion in a window where no Ch6-editing workstream is mid-flight to avoid merge conflicts.

- **Dependency on:** None. Format conversion is independent.

---

## Estimated effort

**Small to medium.** ~1.5–2 hours.

Breakdown:
- Phase 1 initial conversion: ~30 min (includes Pandoc flag experimentation)
- Phase 2 cleanup pass: ~45–60 min (math + tables + entities + links + emphasis)
- Phase 3 validation render: ~15–30 min (visual comparison, spot-checks)
- Phase 4 replace source: ~5 min (delete .html, commit .md)

Could run in a single focused session.

---

## Hard constraints — what NOT to do

- Do NOT modify Ch 6 content during conversion. Only the format changes; substance is invariant.
- Do NOT delete the source `.html` until Phase 3 validation passes.
- Do NOT skip math-notation cleanup. Pandoc HTML → markdown often produces ugly intermediate math representation; manual cleanup to LaTeX is required.
- Do NOT lose the hyperlinks added in Phase 5 of the appendix-numbering-reconciliation workstream. Verify each survives.
- Do NOT schedule this workstream while another workstream is mid-edit on Ch 6 (merge conflict risk).

---

## Branch discipline

Fresh feature branch `claude/ch6-html-to-markdown-<harness-id>` from current `origin/main` after `git fetch`. Per WP#9: merge per ratified chunk via `git push origin HEAD:main`.

Single commit at end of Phase 4 (one big diff: .html deletion + .md addition) is appropriate; the file is renamed in spirit.

---

## Reference files

- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` — source file (target of conversion)
- Other markdown chapters as format reference: `Chapter__7_OnOtherWorlds__Draft.md`, `Chapter__5_THEACCOUNTABILITYGAP__Draft.md`, etc.
- `tools/workstream-handoffs/archive/publishing-pipeline-handoff_2026-05-11.md` — companion workstream; either order works
- Pandoc documentation: `pandoc.org/MANUAL.html` (HTML reader + markdown writer sections)

---

## Surfacing context (per WP#10 internal-scaffolding traceability)

This workstream was scoped during the 2026-05-11 Tech Appendix numbering reconciliation session when the author asked the question of draft format vs. submission format. Conversation surfaced that Ch 6 being HTML was a 2024-era constraint that 2026 tooling has relaxed. This handoff is the workstream-scoping deliverable from that conversation.

---

*End of workstream handoff. No blocker. Independent of publishing pipeline; either order works. ~1.5–2 hour focused session.*
