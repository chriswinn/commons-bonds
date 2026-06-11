# Publishing Pipeline — Workstream Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch to create at session start:** `claude/publishing-pipeline-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Status going in:** Not blocked. Can run any time. Best run AFTER major content changes have stabilized so the pipeline doesn't churn against moving source files.

---

## The substantive question this workstream answers

How does the project go from current source state (chapters in mixed `.md`/`.html`, Tech Appendix + Glossary in styled `.html`) to **publisher-ready submission artifacts** (US trade publishing convention: `.docx` manuscript-formatted for agent/publisher; technical apparatus as PDF supplement or embedded at end of `.docx`)?

This workstream builds a repeatable conversion pipeline so the question is answered with a `make manuscript` rather than a manual one-time export.

---

## Trigger context

2026-05-11 session (Tech Appendix numbering reconciliation Phases 3–5; commits `7002003` / `b903f0f` / `8f5c416` / `4b53320`) surfaced the publishing-artifact-format question after Phase 5 layman-lookup format discussion led into draft-format-vs-submission-format territory. The chapter cross-reference re-validation completed cleanly; the natural next infrastructure question is the conversion pipeline.

Current draft state:
- **9 narrative chapters as `.md`**: Ch 1, 2, 3, 4, 5, 7, 8, 9, 10 + `_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md` + `_Dedication.md` + `_BookLevelGuidance.md`
- **Ch 6 as `.html`** (`Chapter__6_ThreeWaysofCounting__Draft.html`): formula-rendering rationale; conversion to `.md` is a separate companion workstream candidate
- **Tech Appendix as styled HTML**: `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (7,815 lines; canonical numbering landed today)
- **Glossary as styled HTML**: `core/glossary/commons_bonds_updated_glossary_v4.html`

US trade publishing convention:
- Agent/publisher submission: `.docx` manuscript-formatted (double-spaced, 12pt Times New Roman or Garamond, 1-inch margins, indented paragraphs, running header, new chapter on new page)
- Technical apparatus: PDF supplement OR embedded at end of `.docx` (publisher's preference; varies)
- Book proposal stage (most likely first need): proposal `.docx` + 1–3 sample chapters `.docx` + Tech Appendix PDF supplement

---

## Workstream scope

### Phase 1 — Tooling setup (~30 min)

Verify or install required tools in the working environment:
- **Pandoc** (markdown → docx + docx ↔ html). Industry-standard converter.
- **Headless Chrome** (`chromium --headless --print-to-pdf` or equivalent). Best HTML → PDF fidelity for modern CSS.
- Optional: **LibreOffice** for alternative `.docx` validation render
- Optional: **wkhtmltopdf** as fallback HTML → PDF tool

### Phase 2 — Manuscript-formatted reference.docx template (~1 hour)

Build or source a `tools/publishing/reference.docx` template embodying US trade manuscript standards:
- Double-spaced body (2.0 line spacing)
- Times New Roman or Garamond, 12pt
- 1-inch margins all sides
- Paragraph: first-line indent 0.5", no space-before/after
- Running header: `Winn / Commons Bonds / [page#]` (or alternative author-ratified format)
- Chapter title: centered, ~1/3 down new page, 14pt bold
- Section breaks: `#` (or three centered asterisks) — needs format decision
- Page numbers: top-right or bottom-center

Test by running `pandoc -o test.docx --reference-doc=reference.docx sample_chapter.md` and opening in Word/LibreOffice; iterate until formatting matches industry standard.

### Phase 3 — Conversion script (~1 hour)

Build `tools/publishing/build_manuscript.sh` (or `Makefile`) with configurable targets:

```
make manuscript        # full book consolidated .docx
make proposal          # proposal package: proposal doc + sample chapters
make tech-appendix-pdf # HTML → PDF
make glossary-pdf      # HTML → PDF
make all               # all of the above
```

Implementation notes:
- **Markdown chapters → DOCX**: `pandoc --reference-doc=reference.docx -o output.docx ch1.md ch2.md ...`
- **Ch 6 HTML → DOCX path**: until separately converted to `.md`, use `pandoc -f html -t docx --reference-doc=reference.docx -o ch6.docx Chapter__6_ThreeWaysofCounting__Draft.html` OR convert HTML → MD first, then concatenate. Pick simplest that preserves formula fidelity.
- **HTML → PDF**: `chromium --headless --disable-gpu --no-margins --print-to-pdf=output.pdf input.html`. Add `@media print` CSS to source HTML if needed to suppress nav elements.
- **Order matters**: chapters concatenate in numeric order; appendix + glossary go last if embedded.

### Phase 4 — Validation pass (~1 hour)

Open each output artifact in Word (or LibreOffice if Word unavailable) and verify:
- Formatting matches US trade manuscript standard (double-spaced, indented paragraphs, header, page numbers)
- Em-dashes (—), en-dashes (–), special characters preserved (`&sect;` → §, `&mdash;` → —, `&ndash;` → –, subscripts/superscripts intact)
- Mathematical notation rendered correctly (especially Ch 6 RCV integral, three-methods comparison table, convergence table)
- Cross-references functional (page numbers populate; or named-references display correctly)
- Tech Appendix PDF renders annotated TOC + headings + theorems readably
- Glossary PDF renders the styled term entries with lineage notes intact

Iterate template/script until validation passes.

### Phase 5 — Documentation (~30 min)

Write `tools/publishing/README.md` covering:
- How to run the pipeline (commands + flags)
- How to update the reference template when industry conventions change
- Known issues / limitations
- Maintenance path when chapter source files change format (e.g., when Ch 6 converts to `.md`)
- How to add new output targets

---

## Deliverables

By end of workstream, `tools/publishing/` directory exists with:
- `reference.docx` — Pandoc reference template (US trade manuscript-formatted)
- `build_manuscript.sh` (or `Makefile`) — conversion script
- `README.md` — pipeline documentation
- `outputs/` (gitignored) — built artifacts not checked in

Plus: at least one end-to-end sample run producing `manuscript.docx` + `tech_appendix.pdf` + `glossary.pdf` for verification.

---

## Methodology / hard constraints

- **Do NOT modify chapter source content.** Pipeline reads source files; never writes to them. Conversion artifacts are derived; sources are canonical.
- **Preserve all formatting markers.** Em-dashes, en-dashes, ellipses, HTML entities, mathematical notation, subscripts/superscripts, italic/bold emphasis, footnote markers (if any).
- **Match US trade publishing standard precisely.** Submission with non-standard formatting damages credibility before the editor reads the first sentence. Cross-check against authoritative references (Shawn Coyne / Story Grid manuscript-formatting guidelines; Jane Friedman literary-agent submission conventions; sample reference.docx files from professional editorial sources).
- **Make the pipeline idempotent.** Running `make manuscript` twice produces the same output (no timestamp drift, no random ordering).
- **HTML → PDF**: prefer headless Chrome over wkhtmltopdf — Chrome renders modern CSS better and is more actively maintained.
- **Don't lock in tooling choices without testing.** Pandoc options matter (e.g., `--standalone`, `--toc`, `--top-level-division=chapter`, `--reference-doc`). Iterate.

---

## Open questions for author ratification

1. **Manuscript header format**: `Winn / Commons Bonds / [page#]`? Or `Chris Winn / Commons Bonds: Pricing What We're Losing / [page#]`? Or other?
2. **Tech Appendix submission format**: PDF supplement (separate file) vs. embedded at end of manuscript `.docx`? Industry varies; depends on agent/publisher target.
3. **Footnote convention**: Does the book use footnotes? If so, in-chapter or end-of-book? Pipeline configuration needed.
4. **Math typography**: How heavy is math content beyond Ch 6 + Tech Appendix? If significant in other chapters, may want MathJax → PDF rendering rather than basic Pandoc math support.
5. **Acknowledgments / Dedication / Front Matter**: Include `_Dedication.md`? Add Acknowledgments page (currently absent)? Standard front-matter structure: Title page → Dedication → Table of Contents → Foreword (if any) → Body → AuthorsNote → Acknowledgments → Tech Appendix → Glossary → Bibliography → Index.
6. **Chapter title formatting**: Chapter 1 currently titled "The Quiet Math"; should manuscript use "Chapter 1" + "The Quiet Math" on separate lines or combined as "Chapter 1: The Quiet Math"?

---

## Coordination

- **Distinct from but related to:**
  - **Ch 6 HTML → markdown conversion** — separate companion workstream candidate (~1–2 hour focused session). Eliminates Ch 6's hybrid-format anomaly. Independent of this pipeline; pipeline can handle Ch 6 in either format. Recommend scheduling Ch 6 conversion BEFORE pipeline if user wants unified `.md` drafting; AFTER if user wants pipeline ready for submission first.
  - **Book proposal handoff** (`book-proposal-handoff_2026-05-09.md`) — this pipeline produces the proposal `.docx` artifact when proposal content is ready.
  - **Agent prep handoff** (`agent-prep-handoff_2026-05-09.md`) — submission package format depends on this pipeline's output.
  - **Manuscript completion handoff** (`manuscript-completion-handoff_2026-05-09.md`) — once all 10 chapters drafted (already complete as of 2026-05-10), this pipeline produces the submission-ready manuscript.

- **No content dependencies.** Pipeline operates on existing source files; doesn't require any new content. Can run today; will produce a submission-ready package today if invoked.

---

## Estimated effort

**Medium.** ~3–5 hours for first pipeline build + validation. Once built, runs in seconds per artifact thereafter.

Breakdown:
- Phase 1 (tooling setup): ~30 min
- Phase 2 (reference.docx template): ~1 hour
- Phase 3 (conversion script): ~1 hour
- Phase 4 (validation pass): ~1 hour
- Phase 5 (documentation): ~30 min

Could split into two sessions if needed:
- (a) Phases 1–3 (build pipeline) as session 1
- (b) Phases 4–5 (validation + documentation) as session 2 after author reviews sample output

---

## Hard constraints — what NOT to do

- Do NOT modify chapter source content during conversion. Pipeline reads; doesn't write to source.
- Do NOT skip validation passes. A submission `.docx` with formatting issues damages credibility before content is read.
- Do NOT lock in tooling choices without sample-output testing. Pandoc + reference.docx is industry standard but specific options matter case-by-case.
- Do NOT commit built artifacts to git. `outputs/` directory gitignored; built artifacts are regeneratable.
- Do NOT make the pipeline depend on environment state outside the project. Should run anywhere Pandoc + headless Chrome are installed.

---

## Branch discipline (per `tools/workstream-handoffs/README.md`)

- Fresh feature branch `claude/publishing-pipeline-<harness-id>` from current `origin/main` after `git fetch`.
- Per WP#9: merge per ratified chunk via `git push origin HEAD:main`. Each phase's deliverable commits separately; user reviews + ratifies before push.
- Author ratification required on:
  - Manuscript header format (Q1)
  - Tech Appendix embedding decision (Q2)
  - Footnote convention (Q3)
  - Front-matter structure (Q5)

---

## Reference materials

- **Pandoc documentation**: `pandoc.org/MANUAL.html` (especially `--reference-doc` section)
- **Manuscript formatting standards**: Shawn Coyne (Story Grid), Jane Friedman blog, Writer's Digest manuscript-format guides
- **Sample reference.docx**: search "Pandoc manuscript reference.docx" — multiple open-source examples available
- **HTML → PDF**: headless Chrome documentation; wkhtmltopdf as fallback
- **Industry comp pipelines**: Stiglitz, Mazzucato, Kahneman authors publicly reported as markdown → pandoc → editor workflows

---

## Surfacing context (per WP#10 internal-scaffolding traceability)

This workstream was scoped during the 2026-05-11 Tech Appendix numbering reconciliation session after author asked the fresh-take question on Phase 5 layman-lookup format. The conversation pivoted from "how should chapter cross-references be formatted" to "what format should the book be in for draft + submission" to "build the pipeline that handles both." This handoff is the workstream-scoping deliverable from that conversation.

---

*End of workstream handoff. No blocker. Spin up when first submission package is needed (book proposal completion; sample-chapter request from agent; full manuscript request) OR earlier if author wants the pipeline ready before content stabilizes.*
