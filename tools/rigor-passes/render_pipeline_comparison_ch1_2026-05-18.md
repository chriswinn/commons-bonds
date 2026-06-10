# Render-Pipeline Comparison — Ch 1 (The Quiet Math)

**Date:** 2026-05-18
**Status:** PROPOSED — pending author ratification + canonical-pipeline decision
**Scope:** `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md`
**Base sha (chapter source):** `9ffad4e` (same Ch 1 source content as the remote-container baseline; chapter content unchanged across the laptop-side commits since `9ffad4e`)
**Session base sha:** `bc02767` (post-fast-forward into worktree at session-mid; remote-container baseline at `9ffad4e` predates by 5 commits, all `tools/`-side)
**Workstream:** Ch 1 pipeline-retrofit (first of 4 standardization-comparison-bed retrofits per [`tools/workstream-handoffs/archive/render-pipeline-standardization-handoff_2026-05-17.md`](../workstream-handoffs/archive/render-pipeline-standardization-handoff_2026-05-17.md))
**Stage:** 4 — render + character-integrity audit
**Verdict status:** PROPOSED-pending-canonical-pipeline-decision (Option A/B/C — author ratifies after all 4 first-retrofit chapters' comparisons land + tuning rounds plateau, per standardization handoff §3.4)

---

## §0. Author-directed in-session tuning actions

This session executed two author-directed pipeline-tuning actions mid-comparison (deviating from the standardization-handoff §5 "do NOT tune mid-comparison" default; authorized verbatim by author in-session 2026-05-18):

1. **Patched both `build-derivatives.sh` + `build-derivatives-alt.sh`** to pass `--from=markdown-yaml_metadata_block` to all pandoc invocations. Rationale: pandoc 3.x interprets the chapter sources' top-of-file `---` separator as a YAML metadata block and fails on the "By Chris Winn" line as an undefined alias. The remote-container baseline used the same override at session-time; landing it in the laptop scripts is the documented fix per `tools/quality-gates/render-baselines/build-environment.yaml` line 70–82 + open-follow-up #2 (line 158) + standardization-workstream handoff §3.1.

2. **Installed DejaVu Serif** on the laptop via `brew install --cask font-dejavu`. Rationale: `build-derivatives-alt.sh` auto-includes `tools/scripts/fallback-header.tex` which defines `\newfontfamily\fallbackfont{DejaVu Serif}`; without the font, xelatex errors at PDF generation with "Package fontspec Error: The font 'DejaVu Serif' cannot be found." The remote-container baseline has `fonts-dejavu` apt-installed; the laptop did not.

Both actions are recorded as **§3.5 apply-decision step actions taken in-session under author direction**, NOT as discipline-trap violations. Per Stage 4 doctrine §4.3.2, the pipeline-script change is a publishing-pipeline-script change that triggers Stage 4 re-run for all affected artifacts (the round-2 renders ARE that re-run for Ch 1; Ch 5 + Ch 6 + TA still need re-render against the patched scripts in their respective retrofit sessions).

---

## §1. Pipelines compared

THREE pipelines per author direction 2026-05-17 late-session:

1. **remote-container** (pandoc 3.1.3 + texlive-xetex (TeX Live 2023) + wkhtmltopdf 0.12.6 + EB Garamond apt + DejaVu Serif apt, with `-f markdown-yaml_metadata_block` invocation override applied at session-time). Pre-rendered 2026-05-17 at BASE `9ffad4e` — see `tools/quality-gates/render-baselines/build-environment.yaml`.
2. **laptop-build-derivatives** (`tools/scripts/build-derivatives.sh` post in-session patch) — pandoc 3.9.0.2 + XeTeX (TeX Live 2026) + Chrome headless / wkhtmltopdf 0.12.6 + system EB Garamond. Rendered 2026-05-18.
3. **laptop-build-derivatives-alt** (`tools/scripts/build-derivatives-alt.sh` post in-session patch) — same toolchain as #2, plus `tools/scripts/fallback-header.tex` auto-included (maps U+2014 em-dash + U+2248 ≈ to DejaVu Serif) + DejaVu Serif (Homebrew cask) newly installed in-session. Rendered 2026-05-18.

---

## §2. Render results — round 1 (laptop scripts AS-IS, pre-patch)

Both laptop scripts failed at pandoc-parse time. Captured stderr logs preserved at `build.round1.stderr.log` in each laptop subdir.

| Pipeline | `.docx` | `.pdf` | Failure mode |
|---|---|---|---|
| remote-container (baseline) | 19,732 bytes | 49,980 bytes | n/a (rendered cleanly at session-time) |
| laptop-build-derivatives | ✗ none (exit 3) | ✗ none (exit 3) | `Error parsing YAML metadata at "Chapter__1_TheQuietMath__Draft.md" (line 1, column 1): Unknown alias \`By\`` |
| laptop-build-derivatives-alt | ✗ none (exit 3) | ✗ none (exit 3) | Same parse-time failure as build-derivatives — pandoc front-end is identical between the two scripts; the alt's fallback-header inclusion never fires because pandoc terminates before reaching the xelatex stage. |

**Round-1 finding (preserved as audit-trail):** Both laptop scripts as-of-base-sha `bc02767` with pandoc 3.9.0.2 fail to render Ch 1 entirely. Fix is known per `build-environment.yaml` line 158; applied in round 2 below.

---

## §3. Render results — round 2 (laptop scripts POST in-session patch + DejaVu Serif install)

| Pipeline | `.docx` size | `.docx` SHA256 | `.pdf` size | `.pdf` SHA256 | `.pdf` pages | PDF producer | xelatex `Missing character` warnings |
|---|---|---|---|---|---|---|---|
| remote-container (baseline; session-time render) | **19,732** | `14f6af7cf0be7208…` | **49,980** | `c4a84ffe482005c1…` | **6** | `xdvipdfmx (20220710)` | not captured baseline-side |
| laptop-build-derivatives | **19,639** | `c89332d22b41e748…` | **47,361** | `db518be7ebf95278…` | **6** | `xdvipdfmx (20260317)` | **0** |
| laptop-build-derivatives-alt | **19,640** | `804b4b46415f72db…` | **53,524** | `e8d931ef7bd12749…` | **6** | `xdvipdfmx (20260317)` | **0** |

All three pipelines produce **6-page** US-Letter PDFs. No replacement glyphs detected (no U+FFFD); no `?` substitution; em-dashes (U+2014) + curly apostrophes (U+2019) preserved through all three.

### §3.1 Size + hash deltas vs remote-container baseline

| Pipeline | `.docx` Δ-size | `.pdf` Δ-size | Byte-identical to baseline? |
|---|---|---|---|
| laptop-build-derivatives | -93 bytes (−0.47%) | -2,619 bytes (−5.24%) | No (different hashes both files) |
| laptop-build-derivatives-alt | -92 bytes (−0.47%) | +3,544 bytes (+7.09%) | No (different hashes both files) |

No pipeline reproduces the baseline byte-for-byte. The size deltas trace to (a) pandoc version drift (3.1.3 vs 3.9.0.2) affecting docx XML structure; (b) xdvipdfmx version drift (20220710 vs 20260317) affecting PDF stream encoding; (c) for the `-alt` script specifically, the fallback-header inclusion embeds DejaVu Serif glyph references in the PDF even when the chapter source contains no codepoints the fallback maps (Ch 1 has no bolded em-dashes and no ≈), inflating the PDF.

### §3.2 pdftotext-diff (line-level layout-flow comparison)

`pdftotext` extracts produce 240–245-line text outputs per pipeline. `diff`-line counts pairwise:

| Comparison | `diff` output lines |
|---|---|
| remote-container vs laptop-build-derivatives | 118 |
| remote-container vs laptop-build-derivatives-alt | **78** |
| laptop-build-derivatives vs laptop-build-derivatives-alt | 42 |

**The `-alt` script's PDF text-extraction is closer to the remote-container baseline (78-line diff) than the canonical-in-repo `build-derivatives.sh` script's is (118-line diff).** Both diffs are predominantly **line-wrap layout-flow differences** (same words, different line breaks) — not content drift, not character corruption, not formula misrendering. Sample diff hunks at §3.4 below.

### §3.3 docx XML-level comparison

`pandoc -t plain` extraction from all three docx files produces **identical visible content** (verified prose-side; no character drift; "Pou it is" / "Pooh" / "L. E. Winn"-free per Ch 1's deliberate anonymization-register; em-dashes preserved). However, `word/document.xml` structural diff between remote-container and laptop docx is **substantial** (60+ lines of XML-element drift) — likely pandoc-version-driven (pandoc 3.1.3 vs 3.9.0.2 generate slightly different docx XML layouts for the same source). Both laptop docx files share identical `word/document.xml` (the fallback-header argument applies to xelatex only, not docx).

DOCX content-fidelity verdict: all three pipelines produce content-identical docx with structural-XML drift between pandoc versions. The drift is invisible to a human reader opening the docx; visible only to byte-level / XML-level diff tools.

### §3.4 Sample pdftotext-diff hunks (laptop-build-derivatives vs remote-container)

Diff is predominantly line-wrap deltas:

```
remote-container baseline:                          laptop-build-derivatives:
< maker in the wind tunnels — a title he was proud  > maker in the wind tunnels — a title he was proud
<   of — and an inventor with his name in the         >   of — and an inventor with his name in the patent
<   patent record.                                    >   record. He had a way of solving things, my
< He had a way of solving things, my father said,     >   father said, things that other people would just
<   things that other people would just give up on,   >   give up on, walk past, or simply avoid because
<   walk past, or simply avoid because they were      >   they were too difficult.
<   too difficult.
```

Same prose; line-wrap variance. No character substitution, no replacement glyph, no formula misrender, no Greek-letter drift, no minus-into-box artifact, no subscript-stripping. This is the **good** kind of diff — typography-flow variance under near-identical-but-not-quite toolchain versions, not a fidelity failure.

---

## §4. Typography differences

- **Body font:** all three pipelines target EB Garamond. Remote-container uses apt `fonts-ebgaramond`; laptop uses system EB Garamond. Subtle metric / hinting differences are possible but no font-substitution or tofu-box artifact visible in any pdftotext extraction.
- **Em-dash (U+2014):** preserved cleanly in all three pipelines. No Bold-weight em-dash test for Ch 1 (no bolded em-dashes in Ch 1 prose); test deferred to Ch 5 / Ch 6 / TA where bolded run-in subheads with em-dashes occur.
- **Curly quotes (U+2018 / U+2019):** preserved cleanly in all three pipelines.
- **Approximation symbol (U+2248):** not exercised by Ch 1 (Ch 1 has no ≈ in source); test deferred to Ch 6 / TA.
- **Greek letters / math symbols:** not exercised by Ch 1 (Ch 1 is pure memoir; no math); test deferred to Ch 6 / Ch 9 / TA.

---

## §5. Character-integrity differences

None detected for Ch 1 across the three pipelines. The chapter's memoir register lacks the apparatus-density that surfaces character-integrity failures in the math-heavy chapters; Ch 1's character-integrity test is essentially a baseline-cleanliness check + a verification that the publishing pipeline handles plain prose without artifact. **All three pipelines pass this baseline check.**

---

## §6. Layout differences

- **Page count:** identical (6 pages) across all three pipelines.
- **Page size:** identical (US Letter 612 × 792 pts) across all three pipelines.
- **Margins:** all three use `MARGIN="1in"` → pandoc `--variable=geometry:margin=1in`.
- **Line-wrap flow:** differs across all three pipelines per §3.2 — pdftotext diffs at 42–118 lines (out of ~485 combined total lines per pairwise diff). The differences are line-end positioning; same paragraph count; same content per paragraph.
- **First-page header:** all three produce a top-of-first-page block containing "Commons Bonds / By Chris Winn / Chapter 1: The Quiet Math" — the chapter source's `---`/`*By Chris Winn*`/`---`/`## Chapter 1...`/`---` envelope (lines 1–9) is interpreted identically across pipelines (with `--from=markdown-yaml_metadata_block` disabling YAML detection) as a title-block paragraph + heading.

---

## §7. File-size + page-count comparison

| Pipeline | `.docx` size | `.pdf` size | `.pdf` pages |
|---|---|---|---|
| remote-container | 19,732 bytes | 49,980 bytes | 6 |
| laptop-build-derivatives | 19,639 bytes (−0.47%) | 47,361 bytes (−5.24%) | 6 |
| laptop-build-derivatives-alt | 19,640 bytes (−0.47%) | 53,524 bytes (+7.09%) | 6 |

Layout / typography are functionally equivalent across all three; size deltas trace to toolchain version drift + (for `-alt`) fallback-header embedding overhead.

---

## §8. Author-direction answers

### §8.1 (a) Does either laptop script match remote-container baseline?

**Both match functionally, neither byte-for-byte.** Post-patch, both `build-derivatives.sh` and `build-derivatives-alt.sh` produce content-identical 6-page PDFs + content-identical .docx files vs the remote-container baseline. Byte-level fidelity is impossible without identical toolchain versions (pandoc 3.1.3 vs 3.9.0.2; TeX Live 2023 vs 2026; xdvipdfmx 20220710 vs 20260317). At the byte-level diff side, no laptop script reproduces baseline byte-for-byte; at the content-fidelity side, both do.

Quantitatively, **`build-derivatives-alt.sh` is the closer match to baseline** per pdftotext-diff (78 lines vs `build-derivatives.sh`'s 118 lines).

### §8.2 (b) Which laptop script is the right canonical going forward?

**Three candidate answers; tradeoffs:**

- **`build-derivatives.sh` (canonical-in-repo)** has the **smallest output footprint** + **no DejaVu Serif dependency** + tightest line-wrap delta vs baseline (~5% PDF size smaller). For chapters with no bolded em-dashes / no ≈ / no math (Ch 1, Ch 2, Ch 3, Ch 10), this script suffices.

- **`build-derivatives-alt.sh` (Claude-tuned alt)** has the **closer pdftotext layout-flow match to baseline** (78-line diff vs 118-line) + **handles bolded em-dash + ≈ via DejaVu Serif fallback** + larger output footprint + requires DejaVu Serif installed. For chapters with bolded run-in subheads (Ch 5 + Ch 6) or apparatus-density (Ch 4 + Ch 7 + Ch 8 + Ch 9 + TA), this script is the load-bearing path.

- **A merged canonical script** (the actual recommendation if both work cleanly across the 4 first-retrofit chapters): add DejaVu Serif as a documented dependency in the canonical script + conditionally include the fallback-header for chapters that need it (or include unconditionally — Ch 1 demonstrates that fallback-header inclusion has no negative effect when the chapter source contains no codepoints the fallback maps). The architectural difference between the two scripts is small (one `--include-in-header` flag); merging them is a one-line change to the canonical script + documentation update.

**Recommendation for author at canonical-decision time:** Option A (tune laptop to match remote-container) is now viable per Ch 1's data — the patched `build-derivatives.sh` (or `-alt.sh`) renders content-identical output to the remote-container baseline. **Caveat:** Ch 1's baseline cleanliness does NOT generalize to Ch 5 + Ch 6 + TA; the math-heavy chapters carry the load-bearing render-failure tests (em-dash-in-bold, ≈, Greek-letter, formula-integrity). Defer canonical-script ratification until Ch 5 + Ch 6 + TA comparisons land.

---

## §9. Findings + spot-fix recommendations

### §9.1 HIGH-severity finding (round 1; resolved in round 2)

**Finding ID:** F-RP-CH1-01
**Severity:** HIGH (round 1; resolved in round 2)
**Description:** Both `build-derivatives.sh` and `build-derivatives-alt.sh` as-of-base-sha `bc02767` failed at pandoc-parse time on Ch 1 source under pandoc 3.9.0.2 due to the YAML-metadata-block detection issue.
**Disposition:** **RESOLVED in round 2** via in-session patch to both scripts adding `--from=markdown-yaml_metadata_block` to all pandoc invocations. Both scripts now render Ch 1 cleanly.

### §9.2 MEDIUM-severity finding (round 2)

**Finding ID:** F-RP-CH1-02
**Severity:** MEDIUM (resolved in-session)
**Description:** `build-derivatives-alt.sh` PDF generation failed initially with `Package fontspec Error: The font "DejaVu Serif" cannot be found` because the laptop did not have DejaVu Serif installed (the fallback-header.tex requires it).
**Disposition:** **RESOLVED in round 2** via `brew install --cask font-dejavu`. Recorded as a **new dependency** of the canonical `-alt.sh` path; should be documented in `tools/scripts/README.md` + `tools/quality-gates/render-baselines/build-environment.yaml`'s laptop-side toolchain stamp.

### §9.3 LOW-severity finding (round 2)

**Finding ID:** F-RP-CH1-03
**Severity:** LOW (cosmetic; informational)
**Description:** `-alt.sh` PDF is +7% larger than baseline despite Ch 1 containing no codepoints the fallback-header maps. The fallback-header's `\newfontfamily\fallbackfont{DejaVu Serif}` + `\newfontfamily\fallbackfontbold` declarations embed DejaVu Serif font references in the PDF even when unused.
**Recommended disposition:** Hold for canonical-script consolidation decision. If the canonical path is `-alt`-as-default, the +7% size overhead is the cost of em-dash-in-bold + ≈ coverage and is acceptable. If the canonical path is `build-derivatives.sh`-as-default + opt-in to `-alt` per math-heavy chapter, the size overhead only applies where the coverage is needed.

### §9.4 Spot-fix recommendations for laptop scripts (now landed in-session)

1. **DONE — `--from=markdown-yaml_metadata_block`** added to all pandoc invocations in both `build-derivatives.sh` and `build-derivatives-alt.sh`. (Patches in this session's commit.)
2. **DONE — DejaVu Serif installed** on laptop via `brew install --cask font-dejavu`. (Not a tracked-in-repo action; recorded here + recommended for `tools/scripts/README.md` + `build-environment.yaml` laptop-toolchain stamp.)
3. **DEFERRED to canonical-decision step (§3.5):** the laptop scripts now have a new font-dependency. Should be documented in `tools/scripts/README.md` dependencies section + `build-environment.yaml` should add a laptop-toolchain stamp YAML stanza.

### §9.5 What this comparison cannot yet answer

- **Ch 5 / Ch 6 / TA character-integrity behavior** — the load-bearing render-failure tests for em-dash-in-bold + ≈ + Greek-letter + formula-integrity live in those chapters. Ch 1's clean baseline does NOT generalize; the canonical-script + canonical-pipeline decisions hinge on those subsequent rounds' findings.
- **Chrome-headless `.html → .pdf` path** — Ch 1 source is `.md`, so this comparison only exercises the pandoc + xelatex path. The TA retrofit (4th of the 4) will exercise the HTML → PDF path against Chrome (laptop) vs wkhtmltopdf (remote-container).

---

## §10. Verdict

**PROPOSED-pending-canonical-pipeline-decision** (per retrofit handoff stub §1 + standardization handoff §3.4).

Ch 1 Stage 4 round-2 data demonstrates that the laptop pipeline — with two in-session patches landed (pandoc invocation override + DejaVu Serif install) — produces 6-page content-identical output to the remote-container baseline across both `build-derivatives.sh` and `build-derivatives-alt.sh` paths. No character-integrity failures, no replacement glyphs, no formula corruption, no font-fallback artifacts. Layout-flow differs at ~5–7% PDF-size delta + ~16–24% pdftotext-line-wrap variance; visually equivalent.

**Recommended sequencing:**
1. Carry the patched scripts + DejaVu Serif laptop dependency forward to Ch 5 retrofit (next session); render via all three pipelines + capture pdftotext-diff + Missing-character grep for each. Ch 5 carries the load-bearing test for em-dash-in-bold (Method 1 — Replacement Cost style run-in subheads).
2. Ch 6 retrofit: render via all three pipelines; Ch 6 carries the math-content + ≈ test.
3. TA retrofit: render via all three pipelines; TA carries the full-math + Plane-1 chars + Chrome-vs-wkhtmltopdf HTML→PDF test.
4. After all 4 comparisons land + diagnose cumulative pattern, author ratifies canonical-pipeline (Option A / B / C) AND canonical-laptop-script (build-derivatives.sh vs build-derivatives-alt.sh vs merged-default).

The Ch 1 round-2 data weighs **toward Option A** (tune-laptop-to-match-remote-container) AND **toward consolidating the two laptop scripts into a single canonical script** (the `--include-in-header` toggle is the only architectural delta + can be conditionally applied or made default-on). Both ratifications batch with Ch 5 + Ch 6 + TA data.

---

## §11. Pre-publication review queue flags (carry forward to Stage 5)

- No render-integrity findings to flag for the pre-publication review queue specific to Ch 1 prose. All three pipelines produce content-identical 6-page output with em-dashes preserved and no character drift. Stage 5 sign-off for Ch 1 can proceed at full PASS verdict pending the canonical-pipeline ratification.
- Pre-pub review queue Ch 1 artifact updated separately at [`tools/pre-submission-reviews/ch1_pre_pub_review_queue_v1.0.0.md`](../pre-submission-reviews/ch1_pre_pub_review_queue_v1.0.0.md) — Stage 4 verdict cross-reference now reflects round-2 data.

---

## §12. Cross-references

- Retrofit handoff stub: [`tools/workstream-handoffs/archive/ch1-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/archive/ch1-pipeline-retrofit-handoff_2026-05-17.md)
- Retrofit template: [`tools/workstream-handoffs/archive/pipeline-retrofit-template_2026-05-17.md`](../workstream-handoffs/archive/pipeline-retrofit-template_2026-05-17.md)
- Standardization workstream: [`tools/workstream-handoffs/archive/render-pipeline-standardization-handoff_2026-05-17.md`](../workstream-handoffs/archive/render-pipeline-standardization-handoff_2026-05-17.md)
- Pipeline doctrine: [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)
- Stage 4 doctrine: [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md)
- Build-environment stamp: [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml)
- Ch 1 retrofit Stage 1a clean-baseline: [`tools/quality-gates/clean-baselines/ch1_stage1a_2026-05-18.md`](../quality-gates/clean-baselines/ch1_stage1a_2026-05-18.md)
- Ch 1 retrofit Stage 1c coherence-check: [`tools/quality-gates/coherence-checks/ch1_stage1c_2026-05-18.md`](../quality-gates/coherence-checks/ch1_stage1c_2026-05-18.md)
- Source render outputs (this comparison):
  - `tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/remote-container/{Chapter__1_TheQuietMath__Draft.docx, .pdf, .pdf.txt}` (baseline; rendered 2026-05-17)
  - `tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/laptop-build-derivatives/{Chapter__1_TheQuietMath__Draft.docx, .pdf, .pdf.txt, build.round1.stderr.log, build.round2.stderr.log}` (rendered 2026-05-18)
  - `tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/laptop-build-derivatives-alt/{Chapter__1_TheQuietMath__Draft.docx, .pdf, .pdf.txt, build.round1.stderr.log, build.round2.stderr.log}` (rendered 2026-05-18)
- In-session pipeline-script patches: `tools/scripts/build-derivatives.sh` + `tools/scripts/build-derivatives-alt.sh` (added `--from=markdown-yaml_metadata_block` to all pandoc invocations).

---

*End of Ch 1 render-pipeline comparison. PROPOSED 2026-05-18. Stage 4 verdict batch-ratifies after canonical-pipeline decision lands (post Ch 5 + Ch 6 + TA comparison rounds + tuning rounds plateau).*
