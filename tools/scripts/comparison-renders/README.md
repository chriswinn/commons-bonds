# tools/scripts/comparison-renders/

Per [`tools/workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md`](../../workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md).

Holds side-by-side render outputs from the laptop pipeline + the remote-container pipeline for the first 4 standardization-comparison-bed retrofit chapters (Ch 1, Ch 5, Ch 6, TA).

## Directory layout

```
<chapter-slug>_<date>_<base-sha>/
  remote-container/       # rendered in Anthropic cloud container during a Claude Code session
    *.docx
    *.pdf
  laptop/                 # rendered locally on author's laptop via tools/scripts/build-derivatives.sh
    *.docx
    *.pdf
```

`<base-sha>` is the short-sha of the `origin/main` commit at the time of rendering. Both pipelines must render against the SAME `base-sha` so the comparison is pipeline-driven, not content-driven.

## Current state (2026-05-17)

| Chapter | base-sha | remote-container | laptop | comparison artifact |
|---|---|---|---|---|
| Ch 1 | 9ffad4e | ✓ rendered | (pending laptop run) | — |
| Ch 5 | 9ffad4e | ✓ rendered (byte-exact match to Sandy packet docx + with-citations PDF) | (pending laptop run) | — |
| Ch 6 | 9ffad4e | ✓ rendered (byte-exact match to Sandy packet docx + with-citations PDF) | (pending laptop run) | — |
| TA | 9ffad4e | ✓ rendered (docx byte-exact match to Sandy packet; PDF differs — wkhtmltopdf used here vs Chrome for Sandy original) | (pending laptop run) | — |

Sandy packet canonical-remote-container artifacts (alternative reference; generated commit `e6ddf92` 2026-05-14): `research/outreach/subjects/darity/`.

## Toolchain stamp

See [`tools/quality-gates/render-baselines/build-environment.yaml`](../../quality-gates/render-baselines/build-environment.yaml) for the canonical pipeline's toolchain versions.

## How to populate the `laptop/` subdir

On the author's laptop:

```bash
cd ~/commons-bonds
git checkout 9ffad4e   # or whichever base-sha is current
tools/scripts/build-derivatives.sh -o tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/laptop/ \
    manuscript/chapters/Chapter__1_TheQuietMath__Draft.md
# repeat for Ch 5, Ch 6, TA
```

For the comparison artifact at `tools/rigor-passes/render_pipeline_comparison_<chapter-slug>_<date>.md`: per standardization-workstream §3.2 procedure, capture typography differences, character-integrity differences, layout differences, file-size + page-count.
