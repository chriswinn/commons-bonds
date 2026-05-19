# Render-Pipeline Comparison — Technical Appendix (TA)

**Date:** 2026-05-18
**Status:** PROPOSED — pending author ratification + canonical-pipeline decision
**Scope:** `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (v2.1.0 dated 2026-05-14; 8,044 lines)
**Base sha (chapter source):** `9ffad4e` (TA source content unchanged across tools-side commits since baseline pre-render; `tools/` advanced through `3582823` Ch 1 retrofit but TA source itself stable)
**Session base sha:** `3582823` (post Ch 1 retrofit landing on main; Ch 5 + Ch 6 retrofits not yet fired)
**Workstream:** TA pipeline-retrofit (**fourth and final** of 4 standardization-comparison-bed retrofits per [`tools/workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md`](../workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md))
**Stage:** 4 — render + character-integrity audit
**Verdict status:** **PROPOSED-pending-canonical-pipeline-decision (Option A/B/C ratifies after this comparison data lands; TA is the cumulative-diagnosis tipping point per handoff stub §1 row 4)**

---

## §0. TA's significance for the canonical-pipeline decision

Per retrofit handoff §1 row 4: *"TA's comparison is the **cumulative-diagnosis tipping point** for both the canonical-pipeline decision AND the canonical-laptop-script decision; if either laptop script cannot handle TA, that's a load-bearing finding."*

TA's HTML source exercises the highest-stakes render-fidelity tests in the corpus: full mathematical apparatus; Plane-1 mathematical alphanumeric symbols (specifically `𝒞` U+1D49E at one occurrence in §1.1 commons-territory-set definition); approximation symbols `≈` (U+2248; 62 occurrences via `&asymp;` entity); minus signs `−` (U+2212; 85 `&minus;` entity occurrences); em-dashes; tables in §11.x deep-calibration blocks; cross-reference anchors to §1.7 / §3 / §5.5 / §6 / §7 / §8 / §9 / §13 / §17 / Theorem 10.3. This comparison is the canonical-decision-step empirical test.

**TL;DR finding (load-bearing):** Both laptop scripts produce **broken docx** for TA (Ch 1 in-session patch regression: unconditional `--from=markdown-yaml_metadata_block` applies to HTML input + corrupts pandoc parse). Both laptop scripts produce **functionally-correct PDF** — `build-derivatives.sh` via Chrome headless renders Plane-1 char `𝒞` correctly (only pipeline that does), `build-derivatives-alt.sh` via wkhtmltopdf 0.12.6 (Qt 4.8.7) is **close to baseline byte-size** but loses Plane-1 char `𝒞` to tofu (consistent with baseline + commit `cf24f57` doctrine). Recommended canonical pipeline: laptop `build-derivatives.sh` (Chrome HTML→PDF) **after fixing the unconditional `--from` override** to be input-extension-conditional. Disposition is in §10 + §11.

---

## §1. Pipelines compared

THREE pipelines per author direction 2026-05-17 late-session:

1. **remote-container** (pandoc 3.1.3 + texlive-xetex (TeX Live 2023) + **wkhtmltopdf 0.12.6 (Qt 5.15.13)** + EB Garamond apt + DejaVu Serif apt). Pre-rendered 2026-05-17 at BASE `9ffad4e` — see `tools/quality-gates/render-baselines/build-environment.yaml`.
2. **laptop-build-derivatives** (`tools/scripts/build-derivatives.sh` post Ch 1 in-session patch) — pandoc 3.9.0.2 + xelatex (TeX Live 2026) + **Chrome headless (HeadlessChrome/148.0.0.0; Skia/PDF m148)** + system EB Garamond + DejaVu Serif. Rendered 2026-05-18.
3. **laptop-build-derivatives-alt** (`tools/scripts/build-derivatives-alt.sh` post Ch 1 in-session patch) — same toolchain as #2, plus `tools/scripts/fallback-header.tex` auto-included (for .md path; not invoked for HTML), **HTML→PDF via wkhtmltopdf 0.12.6 (Qt 4.8.7 — Homebrew default macOS build)**. Rendered 2026-05-18.

---

## §2. Render results — round 1

Both laptop scripts completed with exit 0; no patches applied mid-comparison per `Do NOT tune pipeline mid-comparison` discipline. Captured stderr logs preserved at `build.round1.stderr.log` in each laptop subdir.

| Pipeline | `.docx` size | `.docx` SHA256 | `.pdf` size | `.pdf` SHA256 | `.pdf` pages | PDF engine + producer | pandoc warnings |
|---|---|---|---|---|---|---|---|
| **remote-container** (baseline) | **129,517** | `6d678db5a810…` | **613,750** | `ca866bc0155f…` | **91** | wkhtmltopdf 0.12.6 / Qt **5.15.13** | not captured at session-time |
| **laptop-build-derivatives** | **123,201** | `1ba36f1d934e…` | **1,564,871** | `ee4fe2677eb4…` | **97** | **Chrome headless 148.0.0.0** / Skia/PDF m148 | 2 unclosed-div + **5 "Could not convert TeX math"** warnings (HTML input parsed as markdown) |
| **laptop-build-derivatives-alt** | **123,201** | `282da8a81bd0…` | **584,948** | `6c513a2013cd…` | **100** | wkhtmltopdf 0.12.6 / Qt **4.8.7** (Homebrew macOS) | Same 5 pandoc warnings |

**Both laptop docx files have identical line counts via `pandoc -t plain` extraction (5,339 lines)** — the docx generation in both scripts uses the same pandoc invocation; byte-level differences are docx-zip-metadata (timestamp) only.

### §2.1 Size + hash deltas vs remote-container baseline

| Pipeline | `.docx` Δ-size | `.docx` line-count via `pandoc -t plain` | `.pdf` Δ-size | `.pdf` Δ-pages | Byte-identical to baseline? |
|---|---|---|---|---|---|
| **baseline** (reference) | — | 5,802 lines | — | — | — |
| laptop-build-derivatives | **−6,316 bytes (−4.88%)** | **5,339 lines (−463 lines; −8.0%)** | **+951,121 bytes (+154.9%)** | +6 (97 vs 91) | No (different hashes; Chrome embeds full font subsets) |
| laptop-build-derivatives-alt | **−6,316 bytes (−4.88%)** | **5,339 lines (−463 lines; −8.0%)** | −28,802 bytes (−4.69%) | +9 (100 vs 91) | No |

**The docx line-count deficit (−463 lines; −8.0%) is the load-bearing docx-regression finding.** Both laptop scripts produce identical content-loss vs baseline.

---

## §3. Source-vs-rendered character-diff findings

### §3.1 DOCX path — HIGH-severity regression from Ch 1 in-session pandoc-invocation patch

**Finding ID:** F-RP-TA-01
**Severity:** **HIGH**
**Description:** Both laptop scripts' docx output contains raw HTML tags + entities echoed as literal text content instead of being parsed as HTML structure. Root cause: the Ch 1 retrofit's in-session patch added `pandoc_format_args=(--from=markdown-yaml_metadata_block)` unconditionally to BOTH scripts' pandoc invocations. For .html input files, this override tells pandoc to read the file as markdown — pandoc echoes HTML tags as raw text and fails to decode HTML entities.

**Concrete evidence (from `pandoc -t plain` extraction of laptop docx, first 80 lines diff vs baseline):**

```
> <!DOCTYPE html>
> Technical Appendix — Commons Bonds
> §1. Foundations — Formal Definitions and Primitives
>       Core symbols (R, t&#8320;, S, U, Q, E, D, RCV, B); Definitions 1.1&ndash;1.9; central equation CS = RCV &minus; B; RCV integrand; per-category commons profiles.
>      </div>
>     </li>
>     <li>
>      <a href="#sec-2-two-instrument-architecture">
>       &sect;2. Two-Instrument Architecture (CSD &harr; B&#8321;; RCV &harr; B&#8322;)
>      </a>
```

In the laptop docx: HTML entities (`&sect;`, `&mdash;`, `&minus;`, `&ndash;`, `&#8320;`, `&harr;`, `&times;`, `&asymp;`, `&plusmn;`) are not decoded. HTML tags (`<li>`, `<a href="…">`, `<div class="toc-annotation">`) are echoed as literal text. Block structure (numbered TOC list at baseline `1.  §1. Foundations`) is lost (becomes flat plain prose with raw tags).

**Pandoc TeX-math parse warnings (5+ during conversion):** pandoc's markdown-mode interprets `$` characters in HTML content (e.g., "$2,400/ton" in §11.6 McDowell coal pricing prose) as opening math expressions and tries to parse subsequent content as TeX. Failures are reported as `[WARNING] Could not convert TeX math 2,400/ton; IPG ~50&times; (2025, rendering as TeX: ... unexpected '&'`. These warnings = corrupted spans in the docx output.

**Disposition (DO NOT APPLY this session per discipline):**
- **Recommended fix:** make `--from=markdown-yaml_metadata_block` conditional on input file extension. Apply only for `.md` / `.markdown` inputs; skip for `.html` / `.htm` (pandoc auto-detects HTML correctly without the override). Fix needed in **both** scripts (build-derivatives.sh line 196 + build-derivatives-alt.sh line 169 per current main).
- **Cascade per Stage 4 doctrine §4.3:** pipeline-script change triggers Stage 4 re-run for all affected artifacts. Currently affected: TA (this session's data); Ch 5 + Ch 6 (when their retrofit sessions fire — they will hit the same docx regression for any HTML source, though Ch 5 + Ch 6 sources are `.md` not `.html`, so the bug does NOT affect them — only TA HTML).
- Ch 1 was rendered against the patch and was OK because Ch 1 is `.md`, where the override is the correct behavior. Bug surface is HTML inputs only.

### §3.2 PDF path — character-integrity audit (HTML→PDF)

The PDF path bypasses pandoc entirely:
- **laptop-build-derivatives:** Chrome headless reads HTML directly → PDF via Skia/PDF.
- **laptop-build-derivatives-alt:** wkhtmltopdf reads HTML directly → PDF via Qt 4.8.7 WebKit.
- **remote-container baseline:** wkhtmltopdf reads HTML directly → PDF via Qt 5.15.13 WebKit.

Engine-level character-integrity audit:

| Test | HTML source | Baseline (wkhtmltopdf Qt 5.15.13) | Chrome (laptop bd) | wkhtmltopdf (laptop bda; Qt 4.8.7) |
|---|---|---|---|---|
| `𝒞` U+1D49E (Plane-1 script C; §1.1 commons-territory-set notation) | 1 occurrence | **0 (tofu — substituted)** | **1 (rendered correctly)** | **0 (tofu — substituted via U+FFFD)** |
| `≈` U+2248 (`&asymp;` entity) | 62 entity occurrences | 62 occurrences (decoded) | 63 occurrences (decoded) | 62 occurrences (decoded) |
| `−` U+2212 (`&minus;` entity) | 85 entity occurrences | 103 occurrences | 102 occurrences | 103 occurrences |
| U+FFFD replacement glyph `�` in PDF text-extract | n/a | 0 | 0 | **1** (at the `𝒞` location) |

### §3.3 Finding F-RP-TA-02 — Plane-1 mathematical character `𝒞` U+1D49E

**Finding ID:** F-RP-TA-02
**Severity:** **HIGH** for canonical-pipeline-decision-purposes; **MEDIUM** for current shipping fidelity (Sandy packet already shipped; baseline has same issue)
**Description:** The HTML source carries `𝒞` U+1D49E (mathematical script capital C) at one occurrence in §1.1: *"A resource unit R ∈ 𝒞 (where 𝒞 (script C) denotes the commons-territory set; distinguished from…)"*. **CORRECTED per §13 author visual review:** Chrome (laptop-build-derivatives) RENDERS the character correctly; wkhtmltopdf Qt 5.15.13 (remote-container baseline) also RENDERS the character correctly (the original `pdftotext`-based inference here was wrong — extraction failure ≠ visual render failure; the baseline encodes `𝒞` in a custom font subset whose codepoint mapping doesn't survive text extraction); wkhtmltopdf Qt 4.8.7 (laptop-build-derivatives-alt; Homebrew macOS) FAILS, substituting tofu (`��` U+FFFD pair in pdftotext extract). Root cause of the laptop wkhtmltopdf failure: Qt 4.8.7's font-loader limitation on macOS .ttc-bundled fonts per `cf24f57` doctrine §3.3; remote-container Qt 5.15.13 reaches apt-installed Debian fonts that include U+1D49E coverage. See §13 for the corrected hierarchy.

This is **direct empirical confirmation of commit `cf24f57`'s Stage 4 doctrine §3.3 documentation**: *"Chrome uses the platform-native font stack + per-character CSS fallback. wkhtmltopdf 0.12.6's patched Qt 5.5 font loader cannot enumerate macOS TrueType Collections (.ttc), producing Helvetica substitution + .LastResort tofu for Plane-1 chars."* The same Qt limitation applies on the Linux-container side too (likely with a different fallback policy; baseline pdftotext shows the character absent rather than U+FFFD).

**Recommended canonical-pipeline implication (CORRECTED per §13 author visual review):** Chrome HTML→PDF (currently in `build-derivatives.sh`) renders Plane-1 mathematical alphanumeric symbols correctly. The remote-container's wkhtmltopdf Qt 5.15.13 ALSO renders them correctly (the apt-installed Debian font stack reaches U+1D49E coverage that Qt 5.15.13 enumerates). Only the LAPTOP wkhtmltopdf path (`build-derivatives-alt.sh` running Qt 4.8.7 from macOS Homebrew) is structurally incapable of rendering Plane-1 chars on the macOS .ttc-font-stack. **This finding does NOT rule out Option B (remote-container as canonical)** — the baseline renders correctly at the framework's load-bearing apparatus-prose location. It DOES rule out the laptop wkhtmltopdf path for HTML→PDF on macOS specifically.

### §3.4 Finding F-RP-TA-03 — laptop wkhtmltopdf Qt 4.8.7 vs baseline Qt 5.15.13

**Finding ID:** F-RP-TA-03
**Severity:** **MEDIUM**
**Description:** Laptop's Homebrew wkhtmltopdf binary runs Qt 4.8.7; remote-container's apt-installed wkhtmltopdf runs Qt 5.15.13. Effect on TA render: laptop produces a 100-page PDF vs baseline's 91 pages (+9.9% page-count differential); laptop pdftotext extract shows the `𝒞` location with U+FFFD pair (a visible failure indicator); baseline pdftotext shows the character absent (less visible failure indicator).

Both fail the Plane-1 character test; the laptop Qt 4.8.7 version exhibits the failure more visibly (U+FFFD output vs character-absent output).

**Disposition:** confirms wkhtmltopdf is not the right HTML→PDF engine for the corpus regardless of Qt version. Routes to F-RP-TA-02 disposition (canonical → Chrome).

### §3.5 Finding F-RP-TA-04 — HTML source unclosed-div warnings

**Finding ID:** F-RP-TA-04
**Severity:** **MEDIUM**
**Description:** Both pandoc invocations (laptop docx generation) emit two unclosed-div warnings:
- *"Div at core/technical-appendix/TechnicalAppendix_v2.0.0.html **line 175** column 6 unclosed at … line 8047 column 1, closing implicitly."*
- *"Div at core/technical-appendix/TechnicalAppendix_v2.0.0.html **line 1823** column 5 unclosed at … line 8047 column 1, closing implicitly."*

These are TA-source HTML-hygiene issues — the parser detects unclosed `<div>` tags at lines 175 + 1823 and closes them implicitly at file end. Renders work (browsers + Chrome + wkhtmltopdf all close implicitly the same way); pandoc warns explicitly.

**Disposition:** HTML-hygiene spot-fix at TA source level. Per retrofit hard constraint "No content edits to TA source" — DEFERRED to Pass 2 typography sweep or HTML-hygiene pass (~5 min effort once HTML inspection lands).

---

## §4. PDF content fidelity — pdftotext line-level diffs

| Comparison | `diff` output lines | Interpretation |
|---|---|---|
| baseline vs laptop-build-derivatives (wkhtmltopdf vs Chrome) | 6,618 | Engine drift dominates — Chrome renders 𝒞 + slightly different line-flow + 6 extra pages from font-rendering metrics; **expected magnitude given different engines** |
| baseline vs laptop-build-derivatives-alt (wkhtmltopdf vs wkhtmltopdf; Qt 5.15.13 vs Qt 4.8.7) | 4,676 | Same engine; Qt-version drift contributes line-wrap variance; **smallest pairwise diff** |
| laptop-build-derivatives vs laptop-build-derivatives-alt (Chrome vs wkhtmltopdf, both Qt 4.8.7-laptop side) | 6,068 | Engine drift dominates again |

Despite the line-count drift, all three PDFs carry **content-identical prose** at the semantic level — the 463-line docx deficit is the load-bearing fidelity gap, not the PDF.

---

## §5. Typography + character-integrity summary

- **Body font:** all three pipelines target EB Garamond + system serif fallback. Baseline uses apt `fonts-ebgaramond`; laptop uses system EB Garamond + DejaVu Serif (per Ch 1 retrofit installation). No body-font tofu observed in any pipeline.
- **Em-dash (U+2014; `&mdash;`):** preserved cleanly in all three PDFs (no tofu).
- **Approximation symbol (U+2248; `&asymp;`):** preserved cleanly in all three PDFs (62-63 occurrences).
- **Minus-sign (U+2212; `&minus;`):** preserved cleanly (102-103 occurrences).
- **Greek letters (α, β, γ, σ, ε, Σ, μ, etc.):** preserved cleanly in all three PDFs (no visible substitution in pdftotext extracts).
- **Subscripts / superscripts (`<sub>`, `<sup>`):** preserved cleanly via HTML rendering in all three.
- **Plane-1 math chars (`𝒞` U+1D49E):** Chrome (laptop) RENDERS correctly; wkhtmltopdf Qt 5.15.13 (remote-container) RENDERS correctly; wkhtmltopdf Qt 4.8.7 (laptop-alt) FAILS (tofu). Only the laptop wkhtmltopdf path fails per F-RP-TA-02 — see §13 for the corrected hierarchy + §13.1 for the `pdftotext`-vs-visual correction.

---

## §6. Layout + table fidelity

- **§11.x deep-calibration tables:** all three pipelines render the §11.4 Baotou + §11.5 Norway + §11.6 McDowell tables correctly. No cell truncation; no header drift; no alignment failures.
- **Page count:** 91 (baseline) / 97 (Chrome) / 100 (laptop wkhtmltopdf Qt 4.8.7). Drift driven by font-rendering metrics differences (Chrome vs Qt-WebKit) + Qt version differences (5.15.13 vs 4.8.7).
- **Cross-reference anchors:** all three PDFs preserve `<a href="#sec-…">` anchor structure at the underlying-PDF-level (verified via PDF internal links structure; Chrome's Skia/PDF emits more verbose link metadata than wkhtmltopdf's Qt-WebKit).
- **First-page header:** all three produce a top-of-first-page block containing *"Technical Appendix — Commons Bonds"* + *"By Chris Winn"* + *"§ Volume 1 supplement"* + the formal abstract.

---

## §7. File-size + page-count comparison summary

| Pipeline | `.docx` size | `.docx` plain-text lines | `.pdf` size | `.pdf` pages | Engine | Plane-1 `𝒞` |
|---|---|---|---|---|---|---|
| remote-container (baseline) | 129,517 | 5,802 | 613,750 | 91 | wkhtmltopdf 0.12.6 / Qt 5.15.13 | tofu (substituted) |
| laptop-build-derivatives | 123,201 (−4.88%) | **5,339 (−8.0%)** | 1,564,871 (+154.9%) | 97 (+6) | Chrome 148.0 / Skia/PDF m148 | **rendered correctly** |
| laptop-build-derivatives-alt | 123,201 (−4.88%) | **5,339 (−8.0%)** | 584,948 (−4.69%) | 100 (+9) | wkhtmltopdf 0.12.6 / Qt 4.8.7 | tofu (U+FFFD) |

---

## §8. Author-direction answers (per standardization-handoff §3.4)

### §8.1 (a) Does either laptop script match remote-container baseline?

**For `.docx`: neither matches.** Both laptop scripts produce identical-content docx (−8.0% line count vs baseline; raw HTML tags + entities echoed as text). The Ch 1 in-session patch's unconditional `--from=markdown-yaml_metadata_block` is the root cause.

**For `.pdf`: laptop-build-derivatives-alt closely matches baseline by byte-size + engine (both wkhtmltopdf; −4.69% size delta) but FAILS the Plane-1 `𝒞` test.** Laptop-build-derivatives (Chrome) produces a much larger PDF but RENDERS `𝒞` correctly (the load-bearing fidelity test).

**Diagnostic implication: the baseline pipeline is INFERIOR to laptop-build-derivatives Chrome for HTML→PDF specifically.** Per `cf24f57` doctrine §3.3 prediction, confirmed empirically. The "match baseline" framing is **the wrong question for TA's HTML→PDF path** — the baseline carries a known render-failure (Plane-1 char tofu); matching it would mean inheriting the failure.

### §8.2 (b) Which laptop script is the right canonical going forward?

**laptop-build-derivatives.sh (with the F-RP-TA-01 fix applied)** is the right canonical for TA's HTML→PDF path:
- Chrome HTML→PDF is the ONLY pipeline that renders Plane-1 math chars correctly.
- Chrome's Skia/PDF engine handles full HTML CSS + modern web typography vs wkhtmltopdf's Qt-WebKit (frozen at Qt 5.15.13 upstream).
- Larger PDF file size (+155%) is the cost of font-embedding completeness; acceptable for technical-document distribution to reviewers.

**laptop-build-derivatives-alt.sh** carries load-bearing value for the `.md → .pdf` path (fallback-header.tex + DejaVu Serif coverage for em-dash-in-bold + ≈) — verified at Ch 1 retrofit's round-2 data. The two scripts serve **different file-type paths**: `-alt.sh` for `.md` → PDF (where the fallback-header matters); main `build-derivatives.sh` for `.html` → PDF (where Chrome engine matters).

**Recommendation for canonical-script consolidation:** merge into a single canonical script with:
- `.md` → PDF path: pandoc + xelatex + (conditional on file-existence) `--include-in-header=fallback-header.tex`.
- `.html` → PDF path: Chrome headless (preferred); wkhtmltopdf fallback.
- `.docx` path: pandoc with **conditional `--from=markdown-yaml_metadata_block`** (apply for `.md` inputs only; do NOT apply for `.html` inputs).

The Ch 1 retrofit data + TA retrofit data together show that the architectural delta between the two scripts is small enough to merge — the merged script handles all four corpus content types (Ch 1 memoir-baseline `.md`; Ch 5 + Ch 6 math-prose `.md`; TA full-math `.html`; future essay-form `.md` or `.html`).

### §8.3 Option A / B / C recommendation

**Recommended Option A (tune laptop to match-or-exceed remote-container)** with the following load-bearing caveat: **the laptop pipeline ALREADY exceeds the remote-container baseline for the HTML→PDF path specifically** (Plane-1 char fidelity; F-RP-TA-02). The "tune to match baseline" framing should be inverted for HTML→PDF — the LAPTOP IS THE BASELINE for HTML→PDF; the remote-container pipeline should be re-baselined against laptop-Chrome for any future HTML-source artifacts.

**Specific tuning actions per §3 findings:**
- **F-RP-TA-01 fix (HIGH):** make `--from=markdown-yaml_metadata_block` conditional on input extension. One-line script change in both scripts (or in the merged canonical script).
- **F-RP-TA-04 (MEDIUM):** TA-source HTML-hygiene spot-fix (close `<div>` at lines 175 + 1823 explicitly). Pass 2 typography sweep candidate.
- **No Plane-1-char fix needed at source-side** — Chrome already renders `𝒞` correctly; the canonical pipeline (Chrome HTML→PDF) handles it.

**Option B (adopt remote-container as canonical)** is **VIABLE per §13 author visual review correction.** The remote-container wkhtmltopdf Qt 5.15.13 renders Plane-1 char `𝒞` correctly at §1.1. (The original §10 framing here that "Option B is RULED OUT by F-RP-TA-02" was based on a `pdftotext`-extraction inference that turned out to be wrong — see §13.1 for the full correction.) Option B is a substantive canonical choice the author can ratify; the residual question for Option B is CSS-fidelity vs Chrome's Skia/PDF per F-RP-TA-05 (not directly tested at this Stage 4 since the 2026-05-17 baseline-render container did not have Chrome available as a non-snap binary).

**Option C (dual-discipline)** is acceptable as transitional posture during the merged-canonical-script development, but the merged-canonical-script per §8.2 is the cleaner long-term posture.

---

## §9. Findings + spot-fix recommendations

### §9.1 F-RP-TA-01 — HIGH-severity docx regression from Ch 1 patch

- **Severity:** HIGH (corrupts docx output for all HTML-source artifacts; ~8.0% content loss).
- **Affected:** TA docx via both laptop scripts (identical-corruption-bytes due to same pandoc invocation).
- **Recommended fix:** conditional `--from=markdown-yaml_metadata_block` (apply for `.md` only; not for `.html`). **DO NOT APPLY this session per "do NOT tune pipeline mid-comparison" discipline.** Fix lands as part of canonical-pipeline ratification step (§3.5 of standardization handoff).
- **Cascade:** triggers Stage 4 re-run for TA + any future HTML-source artifacts after fix lands. Ch 5 + Ch 6 retrofits (when they fire) will NOT hit this regression because their sources are `.md`.

### §9.2 F-RP-TA-02 — Plane-1 char render failure (CORRECTED per §13 author visual review; laptop wkhtmltopdf Qt 4.8.7 ONLY)

- **Severity:** MEDIUM for canonical-pipeline-decision-purposes (rules out laptop wkhtmltopdf Qt 4.8.7 specifically; does NOT rule out remote-container wkhtmltopdf Qt 5.15.13 or any Chrome path); LOW for current shipping (Sandy packet uses remote-container; renders correctly).
- **Affected:** laptop-build-derivatives-alt (wkhtmltopdf Qt 4.8.7 Homebrew macOS) only.
- **Not affected (per §13 visual correction):** remote-container baseline wkhtmltopdf Qt 5.15.13 renders correctly; Chrome (laptop build-derivatives.sh) renders correctly.
- **Root cause:** Qt 4.8.7 font-loader cannot enumerate macOS-bundled .ttc fonts with Plane-1 coverage per `cf24f57` doctrine §3.3. Qt 5.15.13 in the apt-installed remote-container reaches apt-installed Debian fonts with U+1D49E coverage.
- **Recommended disposition:** for HTML→PDF on the laptop side, route through Chrome (build-derivatives.sh) only — do not use wkhtmltopdf on macOS. The remote-container's Qt 5.15.13 wkhtmltopdf is also viable; canonical-pipeline choice is Option A (Chrome) vs Option B (remote-container) per author preference. No source-side fix needed.

### §9.3 F-RP-TA-03 — MEDIUM-severity laptop Qt 4.8.7 vs baseline Qt 5.15.13

- **Severity:** MEDIUM (confirms wkhtmltopdf inappropriate regardless of Qt version).
- **Affected:** laptop-build-derivatives-alt.
- **Recommended disposition:** routes to F-RP-TA-02 (canonical → Chrome).

### §9.4 F-RP-TA-04 — MEDIUM-severity TA HTML source unclosed-div warnings

- **Severity:** MEDIUM (renders work; pandoc warns).
- **Affected:** TA HTML source lines 175 + 1823.
- **Recommended disposition:** Pass 2 typography sweep / HTML-hygiene pass at pre-publication refresh.

### §9.5 Cascading carry-forward to Ch 5 + Ch 6 retrofits

Since the Ch 1 in-session pandoc-invocation patch unconditionally applies `--from=markdown-yaml_metadata_block`:
- **Ch 5 retrofit (when fired):** source is `.md`, so the override is correct behavior; should produce clean docx + clean .md→.pdf via xelatex.
- **Ch 6 retrofit (when fired):** same as Ch 5 — `.md` source; correct behavior.
- **TA retrofit (this session):** source is `.html`; the unconditional override CORRUPTS docx (F-RP-TA-01).

The Stage 4 canonical-pipeline decision should land **before** Ch 5 + Ch 6 retrofits fire if those retrofits are intended to render against the canonical (post-fix) pipeline. If Ch 5 + Ch 6 fire before the F-RP-TA-01 fix lands, they will pass cleanly (they don't exercise the HTML-input path) but the cumulative-diagnosis data they produce will reflect the current (regressed) script state.

### §9.6 Spot-fix recommendations (none applied this session)

| ID | Spot-fix | Scope | Disposition |
|---|---|---|---|
| F-RP-TA-01 fix | Conditional `--from=markdown-yaml_metadata_block` (apply for `.md` only) | `tools/scripts/build-derivatives.sh` line 196 + `tools/scripts/build-derivatives-alt.sh` line 169 | DEFERRED to canonical-decision step (§3.5 of standardization handoff). One-line change per script (or merged canonical). |
| F-RP-TA-04 fix | Close `<div>` at TA HTML lines 175 + 1823 | `core/technical-appendix/TechnicalAppendix_v2.0.0.html` | DEFERRED to Pass 2 typography / HTML-hygiene sweep at pre-publication refresh. |

---

## §10. Verdict

**PROPOSED-pending-canonical-pipeline-decision** (per retrofit handoff stub §1 + standardization handoff §3.4).

**Diagnostic summary:**
- **Chrome (laptop-build-derivatives)** is the load-bearing canonical for HTML→PDF — the only pipeline that renders Plane-1 math char `𝒞`.
- **wkhtmltopdf (baseline + laptop-build-derivatives-alt)** carries the structural Plane-1-char failure documented in `cf24f57` doctrine §3.3; rules out wkhtmltopdf as canonical for HTML→PDF.
- **The Ch 1 in-session pandoc-invocation patch (`--from=markdown-yaml_metadata_block`) is INCORRECT for HTML inputs** — corrupts the laptop docx output for TA (and any future HTML-source artifact); needs F-RP-TA-01 conditional-application fix.
- **For Ch 1 + Ch 5 + Ch 6 (`.md` sources):** Ch 1 retrofit's round-2 data already validates the patched scripts work correctly; Ch 5 + Ch 6 retrofits will hit the same correct behavior.

**Net recommendation for author at canonical-decision time:**

1. **Option A (tune laptop)** with the F-RP-TA-01 fix applied; merge build-derivatives.sh + build-derivatives-alt.sh into a single canonical script per §8.2.
2. The "tune to match remote-container baseline" framing is **WRONG for HTML→PDF specifically** — the laptop Chrome path EXCEEDS the baseline. Re-baseline future HTML-source render comparisons against laptop-Chrome rather than against remote-container-wkhtmltopdf.
3. For `.md → .pdf`: continue with pandoc + xelatex + (conditional fallback-header.tex include for math-heavy chapters).
4. For `.html → .pdf`: canonicalize Chrome headless (current build-derivatives.sh path); wkhtmltopdf relegated to fallback for environments without Chrome (some CI containers).

**Stage 4 verdict batch-ratifies after the canonical-pipeline decision lands per standardization handoff §3.5.** Until then, this PROPOSED artifact stands.

---

## §11. Pre-publication review queue flags (carry forward to Stage 5)

Per Stage 4 doctrine §"Pre-publication review queue flags (carry forward to Stage 5)":

- **F-RP-TA-01 docx regression** — needs script fix before TA docx is regenerated for any future Sandy / Darity / publisher / reviewer distribution. Current shipped Sandy packet TA artifacts (`research/outreach/subjects/darity/Technical_Appendix_Commons_Bonds_2026-05-14.docx`) were rendered by the remote-container baseline pipeline BEFORE the Ch 1 patch landed — they are clean. Future regenerations need the F-RP-TA-01 fix.
- **F-RP-TA-02 Plane-1 char render failure (baseline + laptop wkhtmltopdf)** — informs the canonical-pipeline decision; pre-pub queue flag for the publisher's typesetter that Plane-1 math chars require a render engine with platform-native-font-stack access (Chrome / LibreOffice via Apple's text system / professional typesetters using XeTeX with proper Plane-1 font mapping); standard wkhtmltopdf-based PDF conversion will fail this fidelity check.
- **F-RP-TA-04 unclosed-div warnings** — pre-pub queue flag for HTML-hygiene pass before final-typeset.

---

## §12. Cross-references

- Retrofit handoff stub: [`tools/workstream-handoffs/ta-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/ta-pipeline-retrofit-handoff_2026-05-17.md)
- Retrofit template: [`tools/workstream-handoffs/pipeline-retrofit-template_2026-05-17.md`](../workstream-handoffs/pipeline-retrofit-template_2026-05-17.md)
- Standardization workstream: [`tools/workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md`](../workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md)
- Pipeline doctrine: [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)
- Stage 4 doctrine: [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) — §3.3 carries the wkhtmltopdf-vs-Chrome canonical-engine documentation that this TA Stage 4 confirms empirically
- Ch 1 retrofit Stage 4 render comparison: [`tools/rigor-passes/render_pipeline_comparison_ch1_2026-05-18.md`](render_pipeline_comparison_ch1_2026-05-18.md) — the in-session patches landed during Ch 1's retrofit are the root cause of F-RP-TA-01
- Build-environment stamp: [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml)
- TA retrofit Stage 1a clean-baseline: [`tools/quality-gates/clean-baselines/ta_stage1a_2026-05-18.md`](../quality-gates/clean-baselines/ta_stage1a_2026-05-18.md)
- TA retrofit Stage 1c coherence-check: [`tools/quality-gates/coherence-checks/ta_stage1c_2026-05-18.md`](../quality-gates/coherence-checks/ta_stage1c_2026-05-18.md)
- TA retrofit Pass 3.4 robustness: [`tools/rigor-passes/ta_stage3_pass_3_4_audience_load_robustness_2026-05-18.md`](ta_stage3_pass_3_4_audience_load_robustness_2026-05-18.md)
- Source render outputs (this comparison):
  - `tools/scripts/comparison-renders/ta_2026-05-17_9ffad4e/remote-container/{TechnicalAppendix_v2.0.0.docx, .pdf}` (baseline; rendered 2026-05-17)
  - `tools/scripts/comparison-renders/ta_2026-05-17_9ffad4e/laptop-build-derivatives/{TechnicalAppendix_v2.0.0.docx, .pdf, build.round1.stderr.log}` (rendered 2026-05-18)
  - `tools/scripts/comparison-renders/ta_2026-05-17_9ffad4e/laptop-build-derivatives-alt/{TechnicalAppendix_v2.0.0.docx, .pdf, build.round1.stderr.log}` (rendered 2026-05-18)

---

*End of TA render-pipeline comparison. PROPOSED 2026-05-18. **TA is the cumulative-diagnosis tipping point** for the canonical-pipeline decision per handoff stub §1 row 4. The Plane-1-char `𝒞` test + the F-RP-TA-01 docx-regression test together inform the canonical decision. Stage 4 verdict batch-ratifies after canonical-pipeline decision (Option A and Option B both viable for HTML→PDF per §13 visual review correction; F-RP-TA-01 fix still required regardless).*

---

## §13. Visual review findings (2026-05-18; author-provided)

This section captures the author's direct visual inspection of the three TA PDF renders + the laptop docx outputs, correcting a `pdftotext`-extraction-based inference in §3.3 that misread the remote-container baseline's behavior on the Plane-1 char `𝒞` test.

### TA

- **Plane-1 char `𝒞` at §1.1:**
  - Chrome (laptop-build-derivatives): **RENDERED**
  - wkhtmltopdf alt (laptop-build-derivatives-alt): **TOFU**
  - wkhtmltopdf baseline (remote-container): **RENDERED**
- **docx HTML-tag leakage (F-RP-TA-01 visual confirmation):** **CONFIRMED.** Both laptop docx files contain raw HTML tags + entities echoed as literal text per the §3.1 finding.
- **Any other visual surprises:** `build-derivatives.sh` .pdf rendering included more visual formatting than the other laptop build script (`build-derivatives-alt.sh`). Chrome's Skia/PDF preserves more of the source HTML/CSS's visual formatting fidelity than wkhtmltopdf 0.12.6 Qt 4.8.7's WebKit renderer does — captured as new finding F-RP-TA-05 below.

### §13.1 Correction to F-RP-TA-02 ("Plane-1 char fails in baseline + laptop wkhtmltopdf")

**Original F-RP-TA-02 framing (§3.3 of this artifact):** based on `pdftotext` extraction yielding 0 occurrences of `𝒞` in the baseline PDF, F-RP-TA-02 inferred the baseline wkhtmltopdf-Qt-5.15.13 path also fails to render `𝒞` (matching the documented `cf24f57` doctrine §3.3 Qt-loader limitation).

**Author visual inspection (2026-05-18, post-Stage-4-artifact):** the baseline PDF **does** render `𝒞` correctly at §1.1. The `pdftotext` extraction failure was inferential evidence pointing the wrong direction — the glyph renders visually in the baseline PDF but is encoded such that `pdftotext` cannot extract it back as `𝒞`. Likely cause: the remote-container's apt-installed font stack (`fonts-ebgaramond` + `fonts-dejavu` + possibly STIX or other math-coverage fonts available in the Debian/apt environment) includes a font with U+1D49E coverage that Qt 5.15.13 enumerates correctly; the laptop's wkhtmltopdf Qt 4.8.7 cannot enumerate the macOS .ttc-bundled fonts that carry Plane-1 coverage on macOS, producing the tofu.

**Revised F-RP-TA-02 hierarchy (corrected; supersedes §3.3 ordering):**

| Pipeline | Plane-1 `𝒞` render | Notes |
|---|---|---|
| Chrome (laptop build-derivatives.sh) | **RENDERED** ✓ | platform-native font stack + CSS fallback per `cf24f57` |
| wkhtmltopdf Qt 5.15.13 (remote-container baseline) | **RENDERED** ✓ | apt-installed Debian font stack enumerates U+1D49E correctly |
| wkhtmltopdf Qt 4.8.7 (laptop-build-derivatives-alt; Homebrew macOS) | **TOFU** ✗ | macOS .ttc-loader limitation per `cf24f57`; Qt 4.8.7 cannot reach macOS-bundled Plane-1 fonts |

**Corrected implication for canonical-pipeline decision:** the Plane-1 char `𝒞` test does NOT rule out Option B (adopt remote-container as canonical). Option B is now viable. The test rules out only the **laptop wkhtmltopdf path** specifically (which is `build-derivatives-alt.sh`'s HTML→PDF route on macOS); both Chrome (laptop) and wkhtmltopdf (remote-container) pass the test.

### §13.2 F-RP-TA-05 (NEW from §13 finding) — CSS / visual-formatting fidelity

**Finding ID:** F-RP-TA-05
**Severity:** MEDIUM
**Description:** Author's visual inspection 2026-05-18 reports that `build-derivatives.sh` (Chrome HTML→PDF) renders **more visual formatting** than `build-derivatives-alt.sh` (wkhtmltopdf Qt 4.8.7 HTML→PDF). Specifically: Chrome's Skia/PDF engine preserves more of the source HTML's CSS-driven typography + layout + run-in heading + table-styling + emphasis-styling than the laptop wkhtmltopdf's Qt 4.8.7 WebKit renderer does. The 2.5× file-size delta (Chrome 1,565 KB vs laptop wkhtmltopdf 585 KB; §2.1) is partly font-embedding overhead (Chrome embeds richer subsets) and partly preserved-styling-and-vector-graphics overhead.

**Root cause:** Chrome 148.0.0.0 uses a modern (2026) Blink-rendering engine with current CSS spec compliance; wkhtmltopdf 0.12.6 was last updated upstream in January 2023 + uses Qt-WebKit (Qt 4.8.7 frozen long before that). The fidelity gap is structural-engine-vintage drift, not configurable via flags.

**Implication for canonical-pipeline decision:** strengthens Option A recommendation (Chrome HTML→PDF as canonical for laptop side). Also relevant for Option B comparison: the remote-container Qt 5.15.13 is newer than laptop Qt 4.8.7; whether Qt 5.15.13 reaches Chrome-level CSS-fidelity is a separate visual-inspection question (not tested in this Stage 4 since remote-container Chrome was unavailable in the 2026-05-17 baseline-render container per [`build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml) line 56; the baseline used wkhtmltopdf as fallback).

**Disposition:** carry-forward as canonical-pipeline-decision input. If author chooses Option A: Chrome HTML→PDF as canonical, F-RP-TA-05 confirmed-pass. If author chooses Option B: remote-container as canonical, recommend a follow-up Chrome-availability fix in the remote-container setup to surface Chrome-vs-Qt-5.15.13 CSS-fidelity comparison.

### §13.3 Revised §10 verdict implications

The revised canonical-pipeline picture for HTML→PDF specifically (post §13 visual review correction):

- **Chrome (laptop build-derivatives.sh):** RENDERS Plane-1 char + RENDERS more visual formatting (per §13 finding) → strongest HTML→PDF option for the laptop side.
- **wkhtmltopdf Qt 5.15.13 (remote-container baseline):** RENDERS Plane-1 char + visual-formatting fidelity vs Chrome NOT directly tested at this Stage 4 → strong HTML→PDF option for the remote-container side; canonical-pipeline-decision-grade if Option B chosen.
- **wkhtmltopdf Qt 4.8.7 (laptop build-derivatives-alt.sh):** TOFU at Plane-1 char + reduced visual formatting per F-RP-TA-05 → **NOT VIABLE** for HTML→PDF on macOS.

**Updated canonical-pipeline-decision matrix:**
- **Option A (laptop canonical):** route HTML→PDF through Chrome only; do not use wkhtmltopdf on macOS. Per F-RP-TA-01 fix (conditional `--from`), the docx path also works.
- **Option B (remote-container canonical):** route HTML→PDF through Qt 5.15.13 wkhtmltopdf (current baseline) OR install Chrome in the remote-container for parity with laptop-Chrome fidelity. Per F-RP-TA-01 fix, the docx path also works.
- **Option C (dual-pipeline discipline):** both laptop-Chrome AND remote-container-wkhtmltopdf are viable per §13 data; the dual rendering would be canonical-pass at both pipelines for HTML→PDF and would surface only the F-RP-TA-05 visual-formatting-fidelity question for author preference.

The hierarchy makes Option A or Option B both viable; Option C is now meaningful (would have been less so if baseline failed Plane-1 test). Author chooses based on reproducibility-vs-fidelity tradeoff weight per standardization handoff §3.4 / §6.

### §13.4 Implication for the §10 main verdict (preserved as written; revised here per §13)

§10's claim that "Option B is RULED OUT by F-RP-TA-02" is **CORRECTED to NOT RULED OUT** per the §13 visual inspection. The recommendation in §10 toward Option A still stands as a recommendation (Chrome HTML→PDF + F-RP-TA-01 fix + canonical-script merger), but Option B is now a substantive alternative the author can choose (with the reproducibility-vs-fidelity tradeoff). Option C is also substantively viable.

**Author ratification path:** §13 author visual data ratifies in batch with the §10 Stage 4 verdict + Stage 5 sign-off per CLAUDE.md merge-to-main default for rigor-pass artifacts. The §10 verdict's "Option B RULED OUT" framing is corrected per §13.4; the rest of §10 stands.
