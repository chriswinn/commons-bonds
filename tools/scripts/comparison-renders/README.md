# tools/scripts/comparison-renders/

Per [`tools/workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md`](../../workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md).

Holds side-by-side render outputs from the laptop pipeline + the remote-container pipeline for the first 4 standardization-comparison-bed retrofit chapters (Ch 1, Ch 5, Ch 6, TA).

## Directory layout

```
<chapter-slug>_<date>_<base-sha>/
  remote-container/                 # rendered in Anthropic cloud container during a Claude Code session
    *.docx
    *.pdf
  laptop-build-derivatives/         # rendered locally on author's laptop via tools/scripts/build-derivatives.sh
    *.docx
    *.pdf
  laptop-build-derivatives-alt/     # rendered locally on author's laptop via tools/scripts/build-derivatives-alt.sh
    *.docx
    *.pdf
```

`<base-sha>` is the short-sha of the `origin/main` commit at the time of rendering. All laptop renders must use the SAME `base-sha` as the remote-container baseline so the comparison is pipeline-driven, not content-driven.

**Why both `build-derivatives.sh` and `build-derivatives-alt.sh`?** Per author direction 2026-05-17: the canonical script between the two has not yet been ratified. Both run during each chapter's Stage 4 dual-render to surface which one (or which combination of script + tuning) reproduces the remote-container baseline closest. The two scripts differ in:

- **`build-derivatives.sh`** (per current `tools/scripts/`): canonical-in-repo script. Default `MAIN_FONT="Garamond"` (commercial macOS-system Garamond on author's laptop). HTML→PDF prefers Chrome headless over wkhtmltopdf (per `cf24f57`).
- **`build-derivatives-alt.sh`** (per `e183953`): Claude-tuned alt. Default `MAIN_FONT="EB Garamond"` (matches sandbox). Passes `--include-in-header=tools/scripts/fallback-header.tex` to pandoc for .md→PDF (fills EB Garamond's U+2014-bold + U+2248 coverage gaps via DejaVu Serif).

Same external interface; outputs may differ depending on font availability on laptop + whether fallback-header coverage matters for that chapter's content.

## Current state (2026-05-17)

| Chapter | base-sha | remote-container | laptop-build-derivatives | laptop-build-derivatives-alt | comparison artifact |
|---|---|---|---|---|---|
| Ch 1 | 9ffad4e | ✓ rendered | (pending laptop run) | (pending laptop run) | — |
| Ch 5 | 9ffad4e | ✓ rendered (byte-exact match to Sandy packet docx + with-citations PDF) | (pending laptop run) | (pending laptop run) | — |
| Ch 6 | 9ffad4e | ✓ rendered (byte-exact match to Sandy packet docx + with-citations PDF) | (pending laptop run) | (pending laptop run) | — |
| TA | 9ffad4e | ✓ rendered (docx byte-exact match to Sandy packet; PDF ~5% delta — both wkhtmltopdf; minor bibliography/layout difference) | (pending laptop run) | (pending laptop run) | — |

Sandy packet canonical-remote-container artifacts (alternative reference; generated commit `e6ddf92` 2026-05-14): `research/outreach/subjects/darity/`.

## Toolchain stamp

See [`tools/quality-gates/render-baselines/build-environment.yaml`](../../quality-gates/render-baselines/build-environment.yaml) for the canonical remote-container pipeline's toolchain versions. A `laptop-environment.yaml` capturing the laptop's version stamp should be added at session-start of each retrofit; place at `<chapter-slug>_<date>_<base-sha>/laptop-environment.yaml`.

## How to populate the laptop subdirs

On the author's laptop:

```bash
cd ~/commons-bonds
git checkout 9ffad4e   # or whichever base-sha is current

# build-derivatives.sh path (canonical-in-repo)
tools/scripts/build-derivatives.sh \
  -o tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/laptop-build-derivatives/ \
  manuscript/chapters/Chapter__1_TheQuietMath__Draft.md

# build-derivatives-alt.sh path (Claude-tuned)
tools/scripts/build-derivatives-alt.sh \
  -o tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/laptop-build-derivatives-alt/ \
  manuscript/chapters/Chapter__1_TheQuietMath__Draft.md

# repeat for Ch 5, Ch 6, TA
```

For the comparison artifact at `tools/rigor-passes/render_pipeline_comparison_<chapter-slug>_<date>.md`: per standardization-workstream §3.2 procedure, capture typography differences, character-integrity differences, layout differences, file-size + page-count, across all three pipelines (remote-container + laptop-build-derivatives + laptop-build-derivatives-alt). The cumulative comparison answers two questions: (a) does either laptop script match remote-container baseline closely, (b) which laptop script is the right canonical going forward.
