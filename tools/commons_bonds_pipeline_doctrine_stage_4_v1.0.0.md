# Pipeline Doctrine — Stage 4 (v1.0.0)

**Date drafted:** 2026-05-17
**Status:** PROPOSED — pending author ratification at session close.
**Parent doctrine:** [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](commons_bonds_pipeline_doctrine_v1.0.0.md) §1
**Relates to existing publishing pipeline:** [`tools/scripts/build-derivatives.sh`](scripts/build-derivatives.sh) (markdown → .docx + HTML + PDF via pandoc + xelatex + Chrome-headless + LibreOffice).

---

## §0. Purpose

Stage 4 is the **render + character-integrity audit**: verify that rendered output (markdown → .docx + HTML + PDF) matches the source content byte-for-byte at the character level + that math formulas + tables + figures render correctly without artifact corruption.

Specific friction Stage 4 resolves (per pipeline-revision handoff §0):

- Tofu-box em-dash / approx-symbol rendering issues (commit `d238f2c` Ch 5 + Ch 6 fix).
- Chrome-vs-wkhtmltopdf rendering divergence (commit `cf24f57`).
- EB Garamond font-family naming for cross-platform render consistency (commit `3208619`).
- Author's lived-experience math-formula corruption: minus-into-box rendering at NIH-era publications + later publishing experience; well-known categorical failure for math-heavy artifacts.
- Subscript / superscript stripping in font-fallback paths.
- Greek-letter substitution under inadequate font coverage.

Stage 4 catches these before pre-publication sign-off (Stage 5). Without Stage 4 as a doctrine-level audit, these issues surface ad-hoc at publishing time — too late for clean disposition.

---

## §1. When Stage 4 fires

**Per v1.0.0 Amendment A (selective stage-firing, ratified 2026-05-18): Stage 4 is an EXPLICIT-GATE pass — fires only on author trigger, NOT on automatic cascade after every prose edit.**

Stage 4 fires at:
- **Pre-external-review send** — before any chapter / TA / essay artifact ships to a peer reviewer / Sandy / publisher / agent.
- **Pre-publication** — before the artifact ships to the final publication venue.
- **On author "build it now" trigger** — explicit instruction like *"Fire Stage 4 audit for Ch 5"* in a session, or PM-session-handoff entry routing the trigger.
- **Any publishing-pipeline-script change** — change-cascade routing: change to `build-derivatives.sh` / `build-derivatives-alt.sh` / `install-render-toolchain.sh` / `Dockerfile.render` / `fallback-header.tex` / `reference.docx` → Stage 4 re-run for all affected artifacts.
- **For first-cycle retrofits** — fires as part of the retrofit (the retrofit itself IS an explicit-gate trigger).

Stage 4 does **NOT** auto-fire on:
- Prose edits / spot-fix applications (the render itself is ~0 Claude tokens via Docker / remote-container, but the audit work is heavy + only valuable at distribution-readiness; spot-fix applications batch their Stage 4 deferral until pre-publication).
- Pass 3.1 / Pass 3.2 findings dispositions (those auto-fire per §3.1 of the canonical doctrine; Stage 4 stays gated).
- Stage 1c coherence-check updates (those route to ⚡ automatic cascade per §3.1; Stage 4 stays gated).

After Stage 3 closes (all five passes complete + spot-fixes applied + author ratified — per v1.0.0 Amendment B 2026-05-18, Stage 3 is a **five-pass** rigor audit including Pass 3.5 developmental-edit), Stage 4 fires before Stage 5 sign-off.

For retrofit cycles: after Pass 3.5 (developmental-edit) completes; Stage 4 fires on the retrofit-targeted derivative outputs.

---

## §2. Procedure

### §2.1 Pre-render verification

1. Source artifact at the version that closed Stage 3 (post-spot-fix; author-ratified).
2. Verify build environment is current:
   - Pandoc version match against the known-good version stored in `tools/quality-gates/render-baselines/build-environment.yaml`.
   - xelatex availability + LaTeX package set match.
   - Chrome / LibreOffice binary version match.
   - Fonts: EB Garamond + math font set installed + version-matched.
3. Run `tools/scripts/build-derivatives.sh` against the source artifact.
4. Produce three derivative outputs: `.docx`, `.html`, `.pdf`.

### §2.2 Source-vs-rendered character diff

For each derivative output:

1. Extract text content (e.g., `pdftotext` for PDF; `pandoc -t plain` for docx + html).
2. Diff against the source markdown's text content (after stripping markdown syntax tokens).
3. Flag any character-level divergence:
   - Tofu-box `□` / replacement glyph U+FFFD `�` / question-mark substitution `?` for missing characters.
   - Em-dash / en-dash / hyphen-minus drift (`—` rendered as `–` or `-`).
   - Approximation symbol drift (`≈` rendered as `□` or `?` or `~`).
   - Greek-letter drift (e.g., `α` rendered as `a`).
   - Subscript / superscript stripping (`x_i` rendered as `xi`).
   - Currency / typographic-symbol drift (`$` → `£` is real for some fonts).

### §2.3 Formula-integrity audit (math content)

For each math span (inline + display):

1. Extract the source formula text (LaTeX source for display math; markdown-embedded for inline).
2. Render the formula in isolation through the pipeline.
3. Compare rendered formula against canonical-formula inventory in Stage 1b brief.
4. Flag any divergence:
   - Minus-sign rendering as box / minus-into-box.
   - Subscript / superscript misalignment.
   - Bracket / parenthesis font-fallback issues.
   - Operator-spacing drift (e.g., `\cdot` rendering as `.` due to font-fallback).
   - Greek-letter substitution.
   - Integral / sum / product symbol corruption.

For the Tech Appendix specifically: every formula audited. For Ch 6 + Ch 9: every display math span audited; inline math sampled at 100% if length permits, otherwise sampled at the ratio that gives 99% confidence in formula-integrity.

### §2.4 Table-rendering audit

For each table:

1. Extract rendered table content.
2. Verify:
   - Cell alignment matches source.
   - No cell truncation (wide tables that overflow page boundaries).
   - Header rows render as expected (bold + borders per stylesheet).
   - Cell-content character-level integrity (per §2.2).

### §2.5 Figure-rendering audit

For each figure:

1. Verify image source file present + resolves cleanly.
2. Verify rendered image:
   - No crop / no resolution-loss vs source.
   - Caption renders correctly.
   - Alt-text fires (HTML output).
   - Figure-numbering matches cross-references.

### §2.6 Layout-integrity audit

1. Page-break behavior: no orphaned headers; no widow lines; no header / caption split from content.
2. Cross-references resolve: every `[Chapter X §Y]` / figure-number / table-number reference resolves to a real target.
3. Footnotes render correctly: numbering matches source; footnote text not truncated.
4. Table of contents (if generated) matches source structure.

---

## §3. Render-safety conventions (set at Stage 1b for math content)

Stage 4 catches render-failure patterns; Stage 1b establishes the conventions that prevent them. Specifically, for math content, Stage 1b brief should specify:

### §3.1 Character conventions

- Use `—` (em-dash U+2014) and `–` (en-dash U+2013) deliberately; avoid hyphen-minus `-` for parenthetical extension.
- Use `≈` (U+2248) for approximation; verify font coverage in Stage 1b baseline render test.
- Use `·` (U+00B7) for multiplication where typographically appropriate; avoid `*` in body prose.
- Use proper Greek letters (`α` `β` `γ` … not `a` `b` `c` italicized).
- Use proper minus sign `−` (U+2212) for math expressions; reserve hyphen-minus `-` for word-internal hyphenation.

### §3.2 Formula conventions

- Display math always wrapped in `$$ … $$` or `\[ … \]` (per source-format preference).
- Inline math wrapped in `$ … $`.
- Subscripts always braced when multi-character (`x_{ij}` not `x_ij`).
- Avoid mixing inline-and-display in the same paragraph where layout-flow risks orphaned single-symbol-on-a-line.
- Operators: prefer `\cdot` for multiplication in formulas; `+` `-` direct for addition / subtraction.

### §3.3 Font convention

> **⚠ CANONICAL-PIPELINE QUESTION OPEN (as of 2026-05-17).** Past renders via the laptop `build-derivatives.sh` pipeline have had more render-failure findings (em-dash-in-bold tofu; ≈ coverage; Greek letter / math formula issues) than past renders via the remote-container pipeline that produced the Sandy packet artifacts (`research/outreach/subjects/darity/`, commit `e6ddf92` 2026-05-14). The author had a Chrome-rendering effort in progress on the laptop pipeline at the time of the Sandy packet send and had spent significant time tuning it. **The retrofit Stage-4 dual-render work IS the resumption of that laptop-pipeline-improvement effort** — the explicit intent is to give the laptop pipeline another shot at matching or beating the remote-container pipeline before any canonical-pipeline ratification.
>
> Until that tuning effort completes + author ratifies, the convention below is **DEFAULT BUT NOT-YET-RATIFIED canonical**. The remote-container pipeline serves as the *baseline to match* during the laptop-improvement work, not as the pre-decided canonical.
>
> **Sequencing per author direction 2026-05-17: parallel-with-retrofits.** The standardization workstream fires in parallel with the first 4 retrofit workstreams (Ch 1 + Ch 5 + Ch 6 + TA). Each of those 4 retrofit sessions runs Stage 4 via BOTH pipelines (laptop `build-derivatives-alt.sh` + remote-container-per-§3.1) without ratifying a Stage 4 verdict yet. The laptop pipeline gets tuning attention each round — author iterates on what's tunable (fonts, fallback-header entries, pandoc invocation, Chrome configuration, CSS for HTML→PDF, etc.) — to see whether the laptop pipeline can be brought up to or past the remote-container baseline.
>
> After all 4 comparisons accumulate + tuning rounds plateau, author ratifies one of:
> - **Option A** — laptop pipeline tuned successfully to match-or-exceed remote-container; laptop becomes canonical (the in-repo / version-pinnable / reproducible-by-anyone option).
> - **Option B** — laptop pipeline cannot be tuned to match remote-container within reasonable effort; remote-container becomes canonical; laptop relegated to secondary-check.
> - **Option C** — dual-pipeline discipline; both pipelines canonical with comparison-as-audit.
>
> **2026-05-17 pre-render data point (remote-container pipeline, BASE `9ffad4e`):** at [`tools/scripts/comparison-renders/`](../scripts/comparison-renders/). Byte-level match with Sandy packet (commit `e6ddf92`, 2026-05-15) for markdown-side renders (.docx + .md→.pdf via pandoc + xelatex + EB Garamond + fallback-header). TA PDF reproduces Sandy pipeline within ~5% (this container: 614KB wkhtmltopdf 0.12.6; Sandy canonical with-citations: 583KB wkhtmltopdf, unknown version). **Note:** the Sandy packet TA PDF was wkhtmltopdf, NOT Chrome (per `e6ddf92` commit message; the Chrome-preferred update at `cf24f57` landed 39 minutes AFTER `e6ddf92` and applies to FUTURE renders, not the Sandy packet itself). Earlier framing in this doctrine conflated wkhtmltopdf-vs-Chrome with remote-container-vs-laptop; correction recorded.

Default-canonical conventions (subject to the canonical-pipeline decision above):

- EB Garamond as primary body font; math font with matching Greek-letter + operator coverage.
- For PDF: xelatex with EB Garamond + a math-font with U+2212 / U+2248 / Greek-letter coverage.
- For HTML / docx: same font stack with web-safe fallbacks documented.
- For HTML → PDF path: prefer Chrome headless over wkhtmltopdf (per commit `cf24f57`). wkhtmltopdf 0.12.6's patched Qt 5.5 font loader cannot enumerate macOS TrueType Collections (.ttc), producing Helvetica substitution + .LastResort tofu for Plane-1 chars. Chrome uses the platform-native font stack + per-character CSS fallback.

#### Known EB Garamond coverage gaps + fallback-header mitigation

Per commit `d238f2c` (Ch 5 + Ch 6 tofu-box fix, 2026-05-15):

- **EB Garamond 12-Bold lacks U+2014 (em-dash).** Em-dashes inside bold spans — section headers, `**bolded run-in subheads**` like `**Method 1 — Replacement Cost**` — render as tofu boxes in `.md` → PDF builds without a fallback header.
- **EB Garamond Regular + Bold both lack U+2248 (≈).** Any approximation symbol in markdown sources destined for `.md` → PDF render fails the same way.
- **Greek letter α (U+03B1) is covered** in EB Garamond Regular. (No fix needed for Greek-letter coverage.)

Mitigation: `tools/scripts/fallback-header.tex` maps the missing codepoints to DejaVu Serif. Build via `tools/scripts/build-derivatives-alt.sh` (auto-includes the header) OR pass `--include-in-header=tools/scripts/fallback-header.tex` to pandoc on the canonical script. Adding new fallback codepoints: edit `fallback-header.tex` with additional `\newunicodechar{X}{{\fallbackfont X}}` entries.

#### xelatex warning-verification discipline

xelatex emits `[WARNING] Missing character: There is no — (U+2014) in font EB Garamond 12 Bold` (or similar) to stderr for every uncovered glyph. **These warnings are load-bearing — not noise.** Any Stage 4 audit on a `.md` → PDF build must:

1. Capture stderr from the build (`pandoc ... 2>&1 | tee build.log`).
2. Grep for `Missing character` in the build log.
3. Any match is a HIGH-severity finding: either add the codepoint to `fallback-header.tex` and re-build, or change MAIN_FONT for the affected weight.

Verifying PDF text via `pdftotext` is **insufficient** — the Unicode codepoint is recorded correctly in the PDF text stream even when the glyph is tofu in the rendered page. Visual page inspection + the xelatex warning log are the load-bearing signals.

### §3.4 Baseline render test (Stage 1b)

Before Stage 2 drafts, run a tiny baseline render test with:
- One paragraph of prose containing em-dash + en-dash + approx-symbol.
- One display math span using `−` + Greek letter + subscript + operator.
- One inline math span similar.

Verify all three render cleanly through all three derivative outputs. Record the test artifact at `tools/quality-gates/render-baselines/<scope-slug>_stage1b_baseline_<date>.md`.

If the baseline test fails: resolve the publishing-pipeline issue **before** drafting begins. Drafting against a known-bad render baseline produces work that has to be re-rendered after fix; cheaper to fix upstream.

---

## §4. Stage 4 verdict + spot-fix protocol

### §4.1 Verdict scale

- **CLEAN.** No HIGH-severity render-failure findings. MEDIUM findings may exist; each disposed.
- **MEDIUM HOLD.** No HIGH; ≥1 MEDIUM held with rationale (e.g., "Greek-letter font-fallback in HTML output is acceptable for current stage of publication; pre-publication review queue flags for publisher's typesetter").
- **HIGH BLOCK.** ≥1 HIGH-severity finding; cannot proceed to Stage 5.

### §4.2 Severity scale

- **HIGH** — rendered output is incorrect (claims something different from source; produces tofu-box or replacement glyph; formula misrenders such that reader sees wrong content).
- **MEDIUM** — rendered output is suboptimal but still correct (e.g., en-dash where em-dash intended; spacing-tight Greek letter).
- **LOW** — cosmetic preference (e.g., font-weight subtle drift).

### §4.3 Spot-fix protocol

Stage 4 findings route to spot-fixes in three places:

1. **Source-level fix.** Edit source markdown to use render-safe convention (e.g., replace `~` with `≈`). Re-render + re-audit.
2. **Pipeline-script fix.** Edit `tools/scripts/build-derivatives.sh` (or its dependencies — pandoc args, xelatex template, CSS) to handle the pattern correctly. Cascade: this change triggers Stage 4 re-run for **all** affected artifacts (change-cascade routing rule).
3. **Convention update.** If a new render-failure pattern surfaces (one not in current registry), add to `tools/quality-gates/regressed-patterns.yaml` (render-failure category) + add convention to §3 above. Cascade: update Stage 1b baseline render test to include the new pattern.

---

## §5. Output artifact format

```
# Stage 4 Render + Character-Integrity Audit — [SCOPE]

**Date:** [YYYY-MM-DD]
**Scope:** [path/to/artifact]
**Stage 3 close commit:** [short-sha]
**Build environment:** [pandoc version + xelatex version + Chrome version + font versions]

## §1. Pre-render verification
[Build environment check results]

## §2. Source-vs-rendered character diff
[Per derivative output: findings table with line + source-text + rendered-text + severity]

## §3. Formula-integrity audit (if math content)
[Per formula: source + rendered + verdict + severity]

## §4. Table-rendering audit
[Per table: source + rendered + verdict + severity]

## §5. Figure-rendering audit
[Per figure: source + rendered + verdict + severity]

## §6. Layout-integrity audit
[Findings table]

## §7. Spot-fix recommendations
[Per finding: spot-fix type (source / pipeline / convention) + recommended edit + cascade implications]

## §8. Verdict

CLEAN / MEDIUM HOLD / HIGH BLOCK

## §9. Pre-publication review queue flags (carry forward to Stage 5)

[Per finding to flag: what publisher's typesetter / external reviewer should re-verify]
```

Artifact path: `tools/rigor-passes/<chapter-slug>_stage_4_render_audit_<date>.md`.

---

## §6. Retrofit-mode notes

For chapters already through prior pipeline cycles:

- Stage 4 fires on the retrofit-targeted derivative outputs.
- Particular attention to math-heavy chapters (Ch 6 + Ch 9 + Tech Appendix) given pre-existing tofu-box history (commit `d238f2c` Ch 5 + Ch 6 em-dash / ≈ fix is the canonical example of a render-failure that surfaced post-cycle and required spot-fix).
- Retrofit Stage 4 verdict is typically CLEAN given the pipeline-script fixes already on main; the audit confirms cleanness rather than discovering new patterns.

---

## §7. Hard constraints

- Stage 4 must complete before Stage 5 sign-off.
- HIGH-severity findings block proceeding to Stage 5.
- Pipeline-script changes trigger Stage 4 re-run for affected artifacts (change-cascade routing).
- Render baselines (`tools/quality-gates/render-baselines/`) are commit-tracked; the build environment is a doctrine-level commitment, not a per-session assumption.

---

*End of Stage 4 doctrine.*
