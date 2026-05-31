# tools/scripts/ — CLI utilities

Command-line utilities and any binary assets they depend on. Run from the repo root.

| File | Purpose |
|---|---|
| `install-render-toolchain.sh` | Canonical apt-based render-toolchain installer (Ubuntu/Debian 24.04). Idempotent; supports `--check` verification and `--capture-stamp` modes. Consumed by `Dockerfile.render` (laptop + CI) and by the `.claude/settings.json` SessionStart hook (remote-container). |
| `Dockerfile.render` | Canonical render image — `FROM --platform=linux/amd64 ubuntu:24.04` + run the installer. Mirrors the remote-container workflow (no Chrome; wkhtmltopdf is canonical for HTML→PDF). |
| `docker-render.sh` | Convenience wrapper around `docker run … commons-bonds-render … build-derivatives-alt.sh`. Pre-flights Colima + the image; bind-mounts repo root + `$HOME`; pass-through for all `build-derivatives-alt.sh` flags. Recommended primary invocation path for laptop renders. |
| `session-start-render-toolchain.sh` | SessionStart hook wrapper invoked by `.claude/settings.json`. Gates on `CLAUDE_CODE_REMOTE=true`; fast no-op when the toolchain is already present. |
| `session-start-worktree-isolation.sh` | SessionStart hook (ordered before the others). Emits the red 🔴 banner instructing the session to spawn a worktree before any other tool call, if cwd is the main repo. Per [`../memory/feedback_worktree_isolation_for_parallel_sessions.md`](../memory/feedback_worktree_isolation_for_parallel_sessions.md). |
| `session-start-orphan-lock-recovery.sh` | SessionStart hook (ordered after worktree-isolation). Scans `.claude/worktrees/agent-*/locked` markers; if pid is dead + last commit ≥1h ago + ahead=0 + dirty=0 + not on §5.1 skip-list → `git worktree unlock` + `git worktree remove --force` + best-effort `git branch -D`. Dry-run by default; set `COMMONS_BONDS_HOOK_DESTRUCTIVE=1` to enable. Resolves the orphan-lock-from-killed-agent failure mode that drove the 2026-05-28 + 2026-05-30 cleanup sweeps. |
| `session-end-worktree-cleanup.sh` | SessionEnd hook. **G1 session-end branch-delete default** — if cwd is a top-level isolated worktree on a `claude/<slug>-<harness>` branch AND ahead=0 vs origin/main AND dirty=0 AND HEAD body has no `MERGE-HOLD:`/`MERGE-AFTER:` marker AND branch is not on the §5.1 contaminated skip-list → `cd /Users/c17n/commons-bonds && git worktree remove + git branch -D`. Dry-run by default; set `COMMONS_BONDS_HOOK_DESTRUCTIVE=1` to enable. Honors merge-on-ratification escape hatches per CLAUDE.md. |
| `build-derivatives.sh` | Generate standardized `.docx` + `.pdf` derivatives from `.md` and `.html` sources. Laptop-native default (commercial Garamond + Chrome-preferred). Not the canonical Docker pipeline. |
| `build-derivatives-alt.sh` | Canonical script inside Docker + the remote-container. Defaults to `MAIN_FONT="EB Garamond"`; auto-includes `fallback-header.tex` on `.md` → PDF builds. |
| `check-corpus-invariants.sh` | Invariant-gate corpus-hygiene scan (scaffolding + regressed-pattern registries). Per pipeline doctrine §2 in [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md). See `--help` for usage. |
| `refresh-essay-dashboard.sh` | Regenerate the auto-derivable sections of each `publishing/essays/<venue>/README.md` (pipeline state + rigor-artifact pointer block) from filesystem state. Opt-in per README via `<!-- AUTO-REFRESHED:BEGIN/END -->` markers. See §refresh-essay-dashboard below for usage. |
| `install-pre-commit-hook.sh` | Install the corpus-invariants pre-commit hook into `.git/hooks/pre-commit`. Run once per repo clone. |
| `reference.docx` | Canonical .docx style template (Garamond 12pt, US Letter, 1" margins, soft-gray h2/h3 accent). pandoc reads its styles section automatically. Originally a copy of the Ch 6 packet-send `.docx`. |
| `fallback-header.tex` | xelatex header snippet (fontspec + `\newunicodechar`) mapping codepoints that EB Garamond doesn't cover (U+2014 em-dash in bolded weight, U+2248 `≈`) to DejaVu Serif. Used by `build-derivatives-alt.sh`; can be passed manually to `build-derivatives.sh` via pandoc's `--include-in-header`. |
| `render-verify-fixtures/` | Small known-good fixture + expected outputs for CI render-verification (`.github/workflows/render-verify.yml`). |

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

## `refresh-essay-dashboard.sh`

Regenerates the auto-derivable sections of `publishing/essays/<venue>/README.md` from filesystem state. Manually-edited prose stays manually edited.

### Opt-in via markers

A README opts in to auto-refresh by including two HTML-comment markers somewhere in its body:

```
<!-- AUTO-REFRESHED:BEGIN -->
(anything between these lines is regenerated by the script)
<!-- AUTO-REFRESHED:END -->
```

On every invocation the script replaces the content between those markers with a freshly-generated block (pipeline state + rigor-artifact pointer table). Content outside the markers is preserved verbatim. READMEs without markers are skipped (the script prints `SKIP:` and a hint to preview via `--dry-run`).

### Generated block contents

- **Pipeline state:** essay word count; cover-letter presence; Stage 5 sign-off status (parsed from `stage-5-signoff.md`); pre-submission frozen-baseline presence (`_archive/pre-submission/essay_pre-editor_*.md`); editor-iteration round count.
- **Rigor artifacts:** table of every `rigor/*.md` file with its last-commit date; light-refire subdir, if present, listed separately.

### Quick start

```bash
# Preview proposed block for every essay (no writes)
tools/scripts/refresh-essay-dashboard.sh --dry-run

# Refresh every opted-in README in place
tools/scripts/refresh-essay-dashboard.sh

# Refresh one essay
tools/scripts/refresh-essay-dashboard.sh --essay foreign-affairs-existence-proof

# CI-style staleness check (exit non-zero if any opted-in README has stale block)
tools/scripts/refresh-essay-dashboard.sh --check
```

### When to run

- After any commit that touches `publishing/essays/<venue>/` (especially rigor artifacts, sign-offs, cover letters, editor-iteration rounds).
- At session close on any essay-pipeline workstream.
- Before a cross-essay portfolio review, so the dashboards reflect current state.

The script is idempotent — re-running with no filesystem changes produces no diff.

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

---

## Render-output policy

Ratified 2026-05-19. Renders (`.docx` + `.pdf`) are **derived artifacts** — markdown sources stay the source of truth. The discipline:

| Where renders live | Committed? | When |
|---|---|---|
| Per-recipient outreach packets — `research/outreach/subjects/<name>/<artifact>_<date>.{docx,pdf}` | Yes | When the file ships to a named recipient (e.g., the Sandy/Darity packet 2026-05-14). The exact bytes that went out are committed as evidence-of-delivery. |
| Per-venue submission packets — `research/submissions/<venue>/<artifact>_<date>.{docx,pdf}` | Yes | When shipping to a publisher / agent / book reviewer. (Create the dir on first use.) |
| Per-venue essay submissions — `publishing/essays/<venue>/<artifact>.{docx,pdf}` | Yes | When the file goes to an editor at that venue. |
| CI render-verify expected outputs — `tools/scripts/render-verify-fixtures/expected/*.{docx,pdf}` | Yes | Tracked as the byte-stable comparison baseline. |
| Canonical style template — `tools/scripts/reference.docx` | Yes | Pandoc's `--reference-doc=` target. |
| Stage 4 audit renders (in-session verification) | No | Render to `/tmp` (or any throwaway dir), audit, discard. The audit findings list goes to `tools/rigor-passes/`; the render itself doesn't need committing. |
| Author proofing renders (read on screen, mark up locally) | No | Render to wherever convenient; don't commit. |

`.gitignore` enforces this: `*.docx` and `*.pdf` are globally ignored, with explicit allowlist entries for the committed-evidence locations above. A render written alongside a chapter source (e.g., `manuscript/chapters/Chapter__5_*.docx`) won't be committed by accident.

When a new venue ships its first render, add the dir to the `.gitignore` allowlist if it's outside the existing patterns.

---

## Render-toolchain canonical pipeline (Docker via Colima)

Per pipeline doctrine Stage 4 §3.3 + the render-toolchain-containerization workstream ([`render-toolchain-containerization-handoff_2026-05-18.md`](../workstream-handoffs/render-toolchain-containerization-handoff_2026-05-18.md)), the canonical render pipeline is apt-installed pandoc + xelatex + wkhtmltopdf + EB Garamond + DejaVu Serif on Ubuntu 24.04. One installer ([`install-render-toolchain.sh`](install-render-toolchain.sh)) is consumed by three contexts:

- **Laptop** via Docker (Colima runtime). This README's primary path.
- **Remote-container** via `.claude/settings.json` SessionStart hook OR the Anthropic-web-UI setup script.
- **CI** via the [`render-verify.yml`](../../.github/workflows/render-verify.yml) workflow.

### Install Colima + docker on macOS

Colima is the canonical Docker runtime (fully open-source). Docker Desktop is only an alternative if you already have it. On Apple Silicon (M-series), QEMU emulates x86_64 to match the remote-container architecture — about a 5-second overhead per render.

```bash
brew install colima docker qemu lima-additional-guestagents
colima start --arch x86_64 --cpu 4 --memory 4
```

Verify:

```bash
docker version            # client + server should both report a version
colima status             # should show "arch: x86_64" and "runtime: docker"
```

Stop / restart later:

```bash
colima stop
colima start              # re-uses the saved instance
```

### Build the canonical image

From the repo root:

```bash
docker build --platform=linux/amd64 -t commons-bonds-render \
  -f tools/scripts/Dockerfile.render .
```

The first build can take ~10 minutes on Apple Silicon (texlive packages under QEMU). Subsequent builds are seconds when nothing in `tools/scripts/install-render-toolchain.sh` or `tools/scripts/Dockerfile.render` changed.

Verify the toolchain in the image:

```bash
docker run --rm commons-bonds-render             # runs --check, prints ✓/✗ for each component
```

### Render a chapter via Docker

Use the wrapper script `tools/scripts/docker-render.sh` — a transparent passthrough to `build-derivatives-alt.sh` inside the canonical image, with `--platform=linux/amd64` + repo-root bind-mount already set. It pre-flights Colima + the image being present, so failures surface as actionable errors rather than silent misbehavior. The wrapper honors your current working directory: bare filenames + cwd-relative globs work the same as any local tool.

Symlinking into your PATH is supported:

```bash
ln -s "$(pwd)/tools/scripts/docker-render.sh" ~/.local/bin/docker-render
```

From there, the examples assume `docker-render` is on your PATH. Use `tools/scripts/docker-render.sh` if you prefer to invoke it directly.

```bash
# From the repo root, repo-relative path:
docker-render manuscript/chapters/Chapter__1_TheQuietMath.md

# From inside manuscript/chapters/, bare filename + cwd-relative glob:
cd manuscript/chapters/
docker-render Chapter__1_TheQuietMath.md
docker-render Chapter__*.md                  # render every chapter at once
docker-render -f pdf Chapter__*.md           # PDFs only, all chapters, for the weekend annotation pass

# Output to an ephemeral $HOME-side dir for proofing:
docker-render -o ~/proof Chapter__5_*.md

# Output into a committed-evidence dir for a delivery (Colden-style):
docker-render -o ../../research/outreach/subjects/colden Chapter__3_TheWaterman.md

# Multiple files / mixed types at once (TA HTML is included here):
docker-render \
  Chapter__5_*.md \
  Chapter__6_*.md \
  ../../core/technical-appendix/TechnicalAppendix_v2.0.0.html
```

Output-path constraint: `-o` must be repo-relative or under `$HOME`. Colima only bind-mounts `$HOME` into the container by default; the wrapper adds the repo root. Absolute paths outside both areas (e.g., `/tmp` on macOS) are rejected up-front with a fix-it hint, rather than letting the bytes silently die when the `--rm` container exits.

All flags + positional args pass through to `build-derivatives-alt.sh`. See `tools/scripts/build-derivatives-alt.sh -h` for the full inventory.

If invoking `build-derivatives.sh` (the laptop-native variant) inside Docker is ever needed, pass `MAIN_FONT="EB Garamond"` via env-var — its default of `Garamond` (commercial macOS-system) isn't apt-installed.

#### What the wrapper does under the hood

For debugging or one-off use without the wrapper, here is the raw invocation (assuming cwd is the repo root):

```bash
docker run --rm --platform=linux/amd64 \
  -v "$(pwd):/work" -v "$HOME:$HOME" -w /work \
  commons-bonds-render \
  /work/tools/scripts/build-derivatives-alt.sh \
    manuscript/chapters/Chapter__1_TheQuietMath.md
```

The wrapper additionally translates your host cwd to the corresponding container path before setting `-w`, so a bare filename invoked from inside `manuscript/chapters/` resolves correctly. The `-v "$HOME:$HOME"` mount is what makes `-o ~/proof`-style paths work.

### Why not run apt-installed pandoc directly on macOS?

The canonical pipeline targets Ubuntu 24.04. macOS Homebrew offers different pandoc / xelatex / wkhtmltopdf versions, different default fonts, and different fontconfig behavior. Output diverges from the remote-container's. Docker (or Colima) is the way to get the canonical-pipeline output on a laptop.

---

## Local environment verification

The installer's `--check` mode reports whether the canonical toolchain is present without installing anything. Use it as a pre-flight check before retrofit Stage 4 sessions on a fresh remote-container, or as a sanity check inside Docker:

```bash
# Inside Docker
docker run --rm commons-bonds-render

# Inside a remote-container session (after install)
tools/scripts/install-render-toolchain.sh --check
```

A clean check looks like:

```
[install-render-toolchain --check] verifying canonical toolchain...
  ✓ pandoc on PATH
  ✓ xelatex on PATH
  ✓ wkhtmltopdf on PATH
  ✓ fc-list on PATH
  ✓ pdftotext on PATH
  ℹ pandoc:      3.1.3
  ℹ xelatex:     XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian) (preloaded format=xelatex)
  ℹ wkhtmltopdf: 0.12.6
[install-render-toolchain --check] verifying fonts...
  ✓ EB Garamond present
  ✓ DejaVu Serif present
[install-render-toolchain --check] CLEAN.
```

Anything other than `CLEAN.` is a setup problem — either the installer hasn't run yet (run it without `--check`), or something is wrong with apt's package resolution.

---

## Updating the canonical when the toolchain advances

When Ubuntu 24.04's apt advances (pandoc, xelatex, wkhtmltopdf, or font versions), the canonical stamp at [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml) needs to be re-anchored. Procedure:

1. Build a fresh image (no Docker layer cache):
   ```bash
   docker build --platform=linux/amd64 --no-cache \
     -t commons-bonds-render -f tools/scripts/Dockerfile.render .
   ```

2. Capture the new stamp:
   ```bash
   docker run --rm commons-bonds-render \
     /tmp/install-render-toolchain.sh --capture-stamp
   ```

3. Re-render the canonical Stage 4 baselines + verify outputs are still acceptable (per change-cascade routing — any toolchain change re-fires Stage 4 for affected artifacts).

4. Update the `pandoc_version` + `xelatex_version` + `wkhtmltopdf_version` fields in `build-environment.yaml`. Bump `last_verified` to today's date. Commit.

5. Re-render the CI fixture (`tools/scripts/render-verify-fixtures/`) under the new toolchain and update the checked-in expected outputs.

---

## Reference: Claude Code on web setup-script mechanism

Per the [Claude Code on web docs](https://code.claude.com/docs/en/claude-code-on-the-web), there are **two** ways to install the canonical toolchain in a remote-container session:

| Mechanism | Where it lives | Pros | Cons |
|---|---|---|---|
| **Cloud-environment setup script** (recommended) | Anthropic web UI per-environment | Cached via environment snapshot — subsequent sessions start with the toolchain already present | UI-only; not in the repo; one-time configuration step per environment |
| **SessionStart hook** (fallback) | [`.claude/settings.json`](../../.claude/settings.json) — committed to repo | Carries with the repo; no UI configuration needed | Runs on every session start; not cached across sessions (the wrapper's `--check` fast-path mitigates this when the toolchain is already present) |

For the **recommended primary mechanism**, paste the contents of [`install-render-toolchain.sh`](install-render-toolchain.sh) (or simply `bash -c '"$CLAUDE_PROJECT_DIR"/tools/scripts/install-render-toolchain.sh'`) into the **Setup script** field of the cloud-environment configuration dialog. The script runs as root on Ubuntu 24.04 — no `sudo` prefix needed. Anthropic snapshots the filesystem after a successful run; subsequent sessions in that environment start with the toolchain already on disk.

The **fallback SessionStart hook** at [`.claude/settings.json`](../../.claude/settings.json) is wired up automatically — no configuration required. It gates on `CLAUDE_CODE_REMOTE=true` so it only fires in cloud sessions, and uses `--check` as a fast-path skip when the toolchain is already present.

Replacing the cloud session's base image with `Dockerfile.render` is **not yet supported** by Claude Code on the web (per the docs). The Docker image is for laptop renders + CI; the remote-container uses the installer directly on top of Anthropic's provided base image.
