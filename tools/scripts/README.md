# tools/scripts/ — CLI utilities

Command-line utilities and any binary assets they depend on. Run from the repo root.

| File | Purpose |
|---|---|
| `build-derivatives.sh` | Generate standardized `.docx` + `.pdf` derivatives from `.md` and `.html` sources |
| `build-derivatives-alt.sh` | Alt-version of the above with `-H HEADER_TEX` flag for auto-including a xelatex fallback-font header on `.md` → PDF builds. Side-by-side comparison artifact while the canonical script is iterating. |
| `check-corpus-invariants.sh` | Invariant-gate corpus-hygiene scan (scaffolding + regressed-pattern registries). Per pipeline doctrine §2 in [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md). See `--help` for usage. |
| `install-pre-commit-hook.sh` | Install the corpus-invariants pre-commit hook into `.git/hooks/pre-commit`. Run once per repo clone. |
| `reference.docx` | Canonical .docx style template (Garamond 12pt, US Letter, 1" margins, soft-gray h2/h3 accent). pandoc reads its styles section automatically. Originally a copy of the Ch 6 packet-send `.docx`. |
| `fallback-header.tex` | xelatex header snippet (fontspec + `\newunicodechar`) mapping codepoints that EB Garamond doesn't cover (U+2014 em-dash in bolded weight, U+2248 `≈`) to DejaVu Serif. Used by `build-derivatives-alt.sh`; can be passed manually to `build-derivatives.sh` via pandoc's `--include-in-header`. |

---

## `check-corpus-invariants.sh`

Invariant-gate corpus-hygiene scan per the pipeline doctrine. Reads two YAML registries (`tools/quality-gates/scaffolding-patterns.yaml` + `tools/quality-gates/regressed-patterns.yaml`), greps against the in-scope corpus (chapter drafts + AuthorsNote + Dedication + essay-drafts + op-eds), exits non-zero on HIGH-severity match.

### Quick start

```bash
# Full scan (default: all severities)
tools/scripts/check-corpus-invariants.sh --verbose

# HIGH-severity only (block mode)
tools/scripts/check-corpus-invariants.sh --severity HIGH

# HIGH + MEDIUM (review mode)
tools/scripts/check-corpus-invariants.sh --severity HIGH+MEDIUM --no-fail

# Scoped to a single chapter
tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/Chapter__1_TheQuietMath__Draft.md

# Staged files only (used by pre-commit hook)
tools/scripts/check-corpus-invariants.sh --staged --severity HIGH
```

### Allowlist mechanism

Each pattern entry in the YAML registries supports a `allowlist:` list of `file: + line: + rationale:` tuples for known-legitimate substantive uses (e.g., `pressure-test` as a legitimate substantive verb in Ch 9 line 165; `settlement-ratified` in Ch 5 line 48).

### CI integration

The `.github/workflows/corpus-invariants.yml` workflow runs the scan on push (HIGH-severity gate) + pull request (HIGH + MEDIUM with PR report artifact upload).

### Registry expansion

Per pipeline doctrine §2.2, the regressed-pattern registry is incrementally populated by per-chapter retrofit workstreams. Initial seed entries live at the YAML; retrofit workstreams add ~80-120 expected total entries.

---

## `install-pre-commit-hook.sh`

Installs the corpus-invariants pre-commit hook. Run once per repo clone.

```bash
tools/scripts/install-pre-commit-hook.sh
```

The hook runs HIGH-severity invariant scans against staged files and refuses commit on HIGH match. To temporarily bypass for legitimate exceptions, use `git commit --no-verify` — but per CLAUDE.md, do NOT bypass hooks without explicit author direction.

---

## `build-derivatives.sh`

Generates a `.docx` and/or `.pdf` next to each input source (or in a chosen output directory). Picks the right PDF rendering engine based on the source extension so that HTML sources keep their CSS-driven styling and Markdown sources get clean book-style typography.

### Prerequisites

| Tool | Used for | Install (macOS) | Install (Debian/Ubuntu) |
|---|---|---|---|
| `pandoc` | All `.docx` output; `.md` → PDF | `brew install pandoc` | `apt install pandoc` |
| `wkhtmltopdf` | `.html` → PDF (CSS-preserving) | `brew install --cask wkhtmltopdf` | `apt install wkhtmltopdf` |
| `xelatex` | `.md` → PDF only | `brew install --cask mactex-no-gui` | `apt install texlive-xetex` |
| Garamond font | `xelatex` typography + reference docx | system-installed on Mac | `apt install fonts-ebgaramond` |

You only need `xelatex` if you build `.md` PDFs; you only need `wkhtmltopdf` if you build `.html` PDFs. The script detects what's installed and errors per-file with a hint if a needed engine is missing.

### Quick start

```bash
# Build .docx + .pdf for a single HTML source (e.g. the Technical Appendix)
tools/scripts/build-derivatives.sh core/technical-appendix/TechnicalAppendix_v2.0.0.html

# Build .docx + .pdf for every Chapter 5 Markdown draft, output alongside the .md files
tools/scripts/build-derivatives.sh manuscript/chapters/Chapter__5_*.md

# Build into a separate folder (e.g. an outreach packet directory)
tools/scripts/build-derivatives.sh -o research/outreach/subjects/darity \
  core/technical-appendix/TechnicalAppendix_v2.0.0.html

# Build .docx only (skip PDFs — useful if you don't have wkhtmltopdf or xelatex)
tools/scripts/build-derivatives.sh -f docx \
  core/technical-appendix/TechnicalAppendix_v2.0.0.html

# Build .pdf only
tools/scripts/build-derivatives.sh -f pdf manuscript/chapters/Chapter__6_*.md

# Use a custom reference docx (override the default tools/scripts/reference.docx)
tools/scripts/build-derivatives.sh -r path/to/custom-reference.docx Chapter__5_*.md

# Verbose mode — prints which engine + reference is being used per file
tools/scripts/build-derivatives.sh -v core/technical-appendix/TechnicalAppendix_v2.0.0.html

# Print full usage and exit
tools/scripts/build-derivatives.sh -h
```

### Flags

| Flag | Argument | Default | Effect |
|---|---|---|---|
| `-o` | `OUT_DIR` | *(alongside input)* | Write outputs to `OUT_DIR` instead of next to the source |
| `-f` | `FORMATS` | `docx,pdf` | Comma-separated list of formats to build: `docx`, `pdf`, or both |
| `-r` | `REF_DOCX` | `tools/scripts/reference.docx` | Path to the reference `.docx` whose styles seed `.docx` outputs |
| `-v` |  |  | Verbose mode — log which engine + reference is being used per file |
| `-h` |  |  | Print full inline usage docs and exit |

Positional args: one or more input files. `.md` and `.html` (and `.htm`) are supported; anything else pandoc reads will route to the Markdown PDF path.

### How the PDF engine is chosen

| Source extension | DOCX engine | PDF engine | Why |
|---|---|---|---|
| `.html` / `.htm` | `pandoc` + reference.docx | `wkhtmltopdf` | HTML sources carry hand-tuned CSS (run-in bolded headings, italic emphasis, list/table styling). wkhtmltopdf is a WebKit renderer — it draws the HTML *as styled*, preserving authoring intent. |
| `.md` (or any other pandoc-readable) | `pandoc` + reference.docx | `pandoc` + `xelatex` | Markdown carries no CSS, so the LaTeX path gives clean book-style typography matching the reference docx (Garamond 12pt, Letter, 1" margins). |

Both PDF paths target the same page geometry (US Letter, ~1" / 25 mm margins on all sides), so PDFs across input types come out with matching page sizes.

### Where outputs go

By default, outputs land **alongside the input**:

```
manuscript/chapters/Chapter__5_v2_0_0.md           # source
manuscript/chapters/Chapter__5_v2_0_0.docx         # generated
manuscript/chapters/Chapter__5_v2_0_0.pdf          # generated
```

With `-o OUT_DIR`, outputs go to that directory instead. The output stem is always the input stem — if you need a different output filename (e.g. for a packet with a renamed file), `mv` the generated artifact after the script runs.

### Reference docx

The default reference is `tools/scripts/reference.docx`, located via repo root (so the script works from any cwd). To re-anchor the project style, replace that file with any approved `.docx` — pandoc will inherit its styles section automatically. To use a one-off reference docx for a single run without changing the default, pass `-r path/to/custom.docx`.

### Troubleshooting

**"pandoc not found"** — install pandoc (see Prerequisites). The script needs it for all DOCX output and for Markdown → PDF.

**"wkhtmltopdf not installed; needed for .html → PDF"** — install wkhtmltopdf, or pass `-f docx` to skip PDFs for HTML sources. Note: wkhtmltopdf upstream releases stopped Jan 2023; the distributed binary remains stable for static HTML. If you ever need to migrate off it, `weasyprint` (`pip install weasyprint`) or headless Chrome (`chromium --headless --print-to-pdf`) are CSS-faithful alternatives.

**"xelatex not installed; needed for .md → PDF"** — install TeX Live / MacTeX, or pass `-f docx`. If you only ever build `.html` PDFs you can skip the MacTeX install entirely (~4 GB).

**"pandoc/xelatex failed — check that 'Garamond' is installed"** — install Garamond. On Linux: `apt install fonts-ebgaramond`. xelatex falls back to a generic serif if Garamond isn't found, but you'll get a warning.

**PDF content clipped on the right (HTML sources)** — wkhtmltopdf has no scroll affordance, so any HTML element with `overflow-x: auto; white-space: pre` (typically `<pre>` blocks) will silently drop content past the page edge. Fix at the source: add an `@media print` rule that applies `white-space: pre-wrap` and/or reduces font-size. (The Commons Bonds TA stylesheet already does this.)

**Reference docx not found** — script falls back to pandoc defaults silently if the file at the `-r` path (or the default `tools/scripts/reference.docx`) doesn't exist. Run with `-v` to see the resolved reference path.

### Diagnosing rendering issues

When a reviewer flags a rendering defect in a delivered artifact — tofu glyphs, clipped content, broken styling, wrong font weight — the input extension and output format together tell you which pipeline produced it, which narrows where to look:

| Defect surfaces in… | Pipeline that produced it | Where to investigate |
|---|---|---|
| `.html` source → `.pdf` | `wkhtmltopdf` (WebKit) | The HTML source's CSS — `@media print` rules, `overflow-x`, font fallback chains, page-break behavior. wkhtmltopdf renders what a browser would render; if it looks wrong in the PDF it'll look wrong in a browser too. Open the `.html` source in Chrome with print preview as a quick reproduction. |
| `.md` source → `.pdf` | `pandoc` + `xelatex` | The active font's Unicode coverage and any LaTeX header overrides. xelatex emits `[WARNING] Missing character: ...` lines on stderr for every missing glyph — those are load-bearing, not noise. Fix path: add a `--include-in-header` snippet (see `fallback-header.tex` for the pattern) or swap MAIN_FONT in the script. xelatex doesn't preserve CSS — only the LaTeX variables the script sets. |
| Any source → `.docx` | `pandoc` + `reference.docx` | The reference docx itself (`tools/scripts/reference.docx`). Open it in Word/LibreOffice and modify the underlying style definitions; pandoc inherits whatever's there. CSS in the HTML source is ignored on the DOCX path — only the reference docx's styles section applies. |

First-line triage when a reviewer flags an issue: ask **which document** (chooses pipeline) and **which page** (locates source line). The fix lands in one place, not three.

### Verifying the toolchain end-to-end

Quick sanity check that everything's wired up — should produce both outputs in `/tmp/check`:

```bash
mkdir -p /tmp/check && \
  tools/scripts/build-derivatives.sh -v -o /tmp/check \
    core/technical-appendix/TechnicalAppendix_v2.0.0.html && \
  ls -la /tmp/check/
```

You should see `TechnicalAppendix_v2.0.0.docx` (~130 KB) and `TechnicalAppendix_v2.0.0.pdf` (~580 KB), plus log lines confirming which reference docx and which PDF engine were used.
