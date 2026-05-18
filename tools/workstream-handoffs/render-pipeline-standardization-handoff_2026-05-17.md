# Render-Pipeline-Standardization Workstream Handoff

**Date drafted:** 2026-05-17
**Branch prefix:** `claude/render-pipeline-standardization-`
**Status:** PROPOSED — comparison-render baseline in hand from remote-container pre-renders (2026-05-17, BASE `9ffad4e`); awaiting laptop-pipeline-tuning runs during the first 4 retrofit sessions + author's canonical-pipeline decision after tuning rounds plateau. The retrofit Stage-4 dual-render work IS the resumption of the author's laptop-pipeline-improvement effort (Chrome render in progress, hours invested at the time of the Sandy packet send); explicit intent is to give the laptop pipeline another shot at matching or beating the remote-container baseline before any canonical ratification.
**Parent doctrine:** [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) (Stage 4 §3.3 marks canonical-pipeline question as OPEN pending this workstream)
**Companion / predecessor:** [`publishing-pipeline-handoff_2026-05-11.md`](publishing-pipeline-handoff_2026-05-11.md) (built the original `tools/scripts/build-derivatives.sh` toolchain).
**Origin trigger:** Author observation 2026-05-17: document conversions performed via remote-container Claude Code sessions are rendering better than the current laptop-side `build-derivatives.sh` toolchain. (Earlier draft of this handoff used the term "remote-container pipeline" — corrected 2026-05-17 late-session after author clarification: the better-rendering output came from past remote-container sessions, specifically the Sandy packet artifacts at `research/outreach/subjects/darity/` generated in commit `e6ddf92`, not from the user's remote-container session.)

---

## §0. The substantive question

The pipeline doctrine's Stage 4 (render + character-integrity audit) requires a **canonical build pipeline** so that:

- Every Stage 4 audit verifies against the same render baseline.
- Reproducibility holds across time (same source rebuilt months later produces the same artifact).
- Reviewers + publishers + future-author can verify renders consistently.

Two pipelines compared:

| Pipeline | Where it runs | Toolchain | Authority status |
|---|---|---|---|
| **`tools/scripts/build-derivatives.sh`** (canonical-in-repo) | Laptop (author's macOS) | pandoc + xelatex (`.md` → PDF); pandoc + reference.docx (`.docx`); Chrome headless or wkhtmltopdf (`.html` → PDF) | Stage 4 doctrine §3.3 default-canonical |
| **Remote-container pipeline** | Anthropic's cloud container during Claude Code sessions | Same script architecture (pandoc + xelatex + wkhtmltopdf/Chrome); apt-installed toolchain (pandoc 3.1.3 + TeX Live 2023 + fonts-ebgaramond + fonts-dejavu); see `tools/quality-gates/render-baselines/build-environment.yaml` for full stamp | Currently the source of the Sandy packet artifacts (`research/outreach/subjects/darity/`) that author observed to be the best most error-free renders |

The author has observed remote-container renders are better than current laptop renders. This workstream resolves whether to:

- **(A)** Bring laptop pipeline up to remote-container's render quality (tune fonts / engine / pandoc version / fallback-header until match)
- **(B)** Adopt the remote-container pipeline as canonical + document the reproduction workflow + relegate laptop to secondary-check
- **(C)** Maintain dual-pipeline discipline (both run; differences are diagnostic signals for Stage 4 audits)

**Strong evidence already in hand for the comparison:** the standardization-workstream pre-renders performed 2026-05-17 (BASE commit `9ffad4e`) produced byte-level-identical .docx + .md→.pdf output to the Sandy packet artifacts at `research/outreach/subjects/darity/` for Ch 5 + Ch 6 + TA (markdown-side renders matched exactly; HTML→PDF via wkhtmltopdf produced different file size than Sandy's Chrome-rendered TA PDF, which is the one open render-engine question for HTML→PDF specifically). See `build-environment.yaml` "byte-level match table" + comparison-renders directory.

Until this workstream resolves with author ratification, the canonical-pipeline question is **PROPOSED-pending-decision**. Per author direction 2026-05-17, the standardization workstream fires in parallel with the first 4 retrofit workstreams (Ch 1 + Ch 5 + Ch 6 + TA), using their Stage 4 sub-steps as the comparison-render test bed.

---

## §1. Branch discipline

Open fresh feature branch per:

```
git fetch origin
git checkout -b claude/render-pipeline-standardization-<harness-id> origin/main
```

Per CLAUDE.md merge-to-main default: this workstream produces a comparison-render artifact + a canonical-pipeline decision artifact + doctrine update. The comparison-render is internal scaffolding (no chapter content edits); autonomously fast-forward merges to main at session close per the doctrine-cluster pattern. The canonical-pipeline decision requires author ratification before applying to the Stage 4 doctrine.

---

## §2. Read order

1. THIS handoff.
2. [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) — current Stage 4 doctrine with OPEN canonical-pipeline flag.
3. [`tools/scripts/README.md`](../scripts/README.md) — laptop pipeline documentation (incl. defect-triage section).
4. [`tools/scripts/build-derivatives.sh`](../scripts/build-derivatives.sh) + [`tools/scripts/build-derivatives-alt.sh`](../scripts/build-derivatives-alt.sh) + [`tools/scripts/fallback-header.tex`](../scripts/fallback-header.tex).
5. Recent render-related commits surfacing friction:
   - `d238f2c` — Ch 5 + Ch 6 PDF tofu-box fix (EB Garamond em-dash / ≈ coverage)
   - `cf24f57` — Chrome headless preferred over wkhtmltopdf (macOS .ttc font issue)
   - `e183953` — alt-script with fallback-header.tex inclusion
   - `c4eb93c` — defect-triage README section
   - `3208619` — EB Garamond font-family naming
6. [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml) — placeholder for canonical build-environment versions; this workstream populates.
7. `tools/quality-gates/render-baselines/build-environment.yaml` — canonical-pipeline toolchain stamp populated 2026-05-17 from this session's pre-renders.

---

## §3. Mission

### §3.1 The remote-container pipeline — identified + characterized

**Identified as of 2026-05-17 late-session pre-render work.** The remote-container pipeline is the Anthropic-hosted Linux container running during Claude Code sessions, with toolchain installed via apt:

- pandoc 3.1.3 (`pandoc + pandoc-data`)
- TeX Live 2023 with xelatex (`texlive-xetex`)
- wkhtmltopdf 0.12.6 (HTML→PDF, when Chrome unavailable as non-snap binary; Chrome is preferred per `cf24f57` but in this specific container's apt repos only the snap version is available)
- EB Garamond (`fonts-ebgaramond`)
- DejaVu Serif (`fonts-dejavu`) — for fallback-header mapping per `tools/scripts/fallback-header.tex`

Pandoc invocation requires `-f markdown-yaml_metadata_block` to disable YAML metadata block detection for the chapter sources' `---` separator (pandoc 3.x parses the `---` as YAML start; this fails for the chapter "By Chris Winn" line). This invocation tweak should be added to `build-derivatives.sh` per the apply-decision step (§3.5).

Full canonical stamp recorded at: [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml).

This pipeline was the source of the Sandy packet artifacts at `research/outreach/subjects/darity/` (Ch 5 + Ch 6 + TA `.docx` + `.pdf` rendered in commit `e6ddf92` 2026-05-14) which the author observed to be the best most error-free renders to date.

**Reproducibility caveat.** The remote-container is ephemeral: each new session may need to re-apt-install the toolchain. This is a reproducibility weakness compared to a fully version-pinned local laptop pipeline. Two mitigations possible: (1) commit a setup script (`tools/scripts/install-render-toolchain.sh`) that future remote sessions invoke at start; (2) accept that the canonical-pipeline is "the build script + the build-environment.yaml stamp" and any environment matching that stamp produces canonical output. Decision is part of the canonical-pipeline-ratification step (§3.4).

### §3.2 Comparison-render — fires *in parallel with* the first 4 retrofit workstreams

**Sequencing model: parallel-with-retrofits, NOT serial-before-retrofits.** Per author direction 2026-05-17, this workstream fires in parallel with the first 4 retrofit workstreams — **Ch 1 + Ch 5 + Ch 6 + TA** — which span the corpus's render-difficulty spectrum naturally (Ch 1 memoir-baseline → Ch 5 mixed prose-and-analytical-apparatus → Ch 6 highest-math-content outside TA → TA full-math + Plane-1 chars + formulas).

For each of the 4 first-retrofit chapters, the retrofit session's Stage 4 sub-step renders the source through **both pipelines** (laptop `build-derivatives-alt.sh` + remote-container-pipeline-per-§3.1) without ratifying a Stage 4 verdict yet. Comparison-renders accumulate on this workstream's feature branch as the retrofit sessions land.

Render-comparison artifacts captured per chapter:

1. Laptop-rendered derivative outputs (`.docx` + `.pdf` per `build-derivatives-alt.sh`).
2. Remote-container-rendered derivative outputs (`.docx` + `.pdf` per §3.1 identification + toolchain stamp in `build-environment.yaml`).
3. Side-by-side comparison capture at `tools/scripts/comparison-renders/<chapter-slug>_<date>/` (file structure TBD; consider gitignored binaries + thumbnails / page-images committed).
4. Per-chapter comparison artifact at `tools/rigor-passes/render_pipeline_comparison_<chapter-slug>_<date>.md` covering the differences spectrum (per §3.3 below).

### §3.3 Diagnose the gap (cumulative across the 4 first-retrofit chapters)

For each observed difference across the 4 comparison renders, classify root cause:

- **Font-coverage gap** (laptop's xelatex missing a glyph that remote-container renders cleanly via system-font fallback)
- **Engine-choice gap** (xelatex vs whatever-the-remote-container-pipeline-uses rendering the same source differently)
- **CSS / styling gap** (HTML source's @media print rules behaving differently)
- **Toolchain version gap** (remote-container uses a newer pandoc / different reference docx)
- **Fundamental rendering-architecture gap** (e.g., Apple's text-rendering vs xelatex's text-rendering — closeable only by adopting one or the other)

The cumulative diagnosis across the 4 chapters is the load-bearing artifact. Each chapter contributes a different stress: Ch 1 surfaces baseline body-text rendering quality; Ch 5 surfaces mixed prose + apparatus density (em-dashes; analytical run-in subheads); Ch 6 surfaces math content + tables + Method-1/2/3 bolded em-dash patterns; TA surfaces full math + Plane-1 chars + cross-reference anchors + formula-integrity.

### §3.4 Author decision: canonical pipeline (after all 4 first-retrofit comparisons land)

After all 4 first-retrofit chapters have comparison-render data on the workstream branch, author selects:

- **Option A — Tune laptop to match remote-container.** Specific tuning actions per §3.3 diagnosis: add fallback-header entries; swap fonts; upgrade pandoc; etc. Laptop pipeline remains canonical.
- **Option B — Adopt the remote-container pipeline as canonical.** Document the remote-container-pipeline-as-canonical workflow in `tools/scripts/README.md` + populate `build-environment.yaml` with remote-container pipeline identifiers. Laptop pipeline relegated to secondary-check / CI-render / disaster-recovery role.
- **Option C — Dual-pipeline discipline.** Both render every artifact; Stage 4 audit compares the two; differences are diagnostic findings. Most rigorous; most overhead.

### §3.5 Apply the decision; batch-ratify Stage 4 verdicts for the first 4 chapters

Per author's Option-A/B/C ratification:

- Update Stage 4 doctrine §3.3 to canonicalize the decision (drops the OPEN flag).
- Populate `tools/quality-gates/render-baselines/build-environment.yaml` with the canonical toolchain.
- Update `tools/scripts/README.md` with the canonical-pipeline section + (if Option B/C) remote-container-pipeline workflow.
- Update pipeline doctrine §11 quick-reference if any stage-firing implications change.
- If Option A: update `build-derivatives.sh` (or `-alt.sh`) per the tuning actions; possibly add new `fallback-header.tex` entries.
- If Option B/C: document the remote-container reproduction procedure in enough detail that any reviewer can reproduce.
- **Re-render and batch-ratify Stage 4 verdicts for Ch 1 + Ch 5 + Ch 6 + TA using the ratified canonical pipeline.** Each chapter's Stage 4 verdict artifact converts from PROPOSED-pending-canonical to RATIFIED.
- **Then proceed** to the remaining 9 retrofit workstreams using the ratified canonical pipeline as the default Stage 4 build path.

---

## §4. Output deliverables

| Artifact | Path |
|---|---|
| Remote-container pipeline identification | `tools/scripts/README.md` (new section) |
| Comparison-render artifacts | `tools/scripts/comparison-renders/<date>/` (file structure TBD per §3.2) |
| Comparison + diagnosis artifact | `tools/rigor-passes/render_pipeline_comparison_<date>.md` |
| Canonical-pipeline decision | Author-ratified verdict captured in this handoff's §6 + applied in artifacts below |
| Updated Stage 4 doctrine §3.3 | `tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md` |
| Populated build-environment.yaml | `tools/quality-gates/render-baselines/build-environment.yaml` |
| (If Option A) Tuning commits | `build-derivatives.sh` / `build-derivatives-alt.sh` / `fallback-header.tex` |

---

## §5. Hard constraints

- Do NOT make the canonical-pipeline decision unilaterally. Author ratifies after seeing the comparison-render + diagnosis across all 4 first-retrofit chapters.
- Do NOT pin a specific render environment's version unless author confirms it's stable + reproducible across the publication window.
- Do NOT delete or deprecate `build-derivatives.sh` even under Option B — it remains the open-source / version-pinnable / publisher-distributable fallback per the reproducibility tradeoff.
- Do NOT touch chapter content (`manuscript/chapters/*Draft*.md`). Render-pipeline work is `tools/`-side only.
- Comparison-renders should use a fixed source commit (record short-sha in each per-chapter comparison artifact) so that re-runs are reproducible.
- **Discipline-trap to avoid: do NOT tune the pipeline mid-comparison.** Render once per chapter per pipeline; capture the diff; move to the next chapter. Tuning the laptop pipeline between Ch 1 comparison and Ch 5 comparison contaminates the "is the pipeline correct?" question — you end up with comparison data drawn from a moving baseline. The right loop is: render all 4 → diagnose cumulatively → author decides canonical → THEN apply tuning (Option A) or canonical-adoption (Option B) or dual-discipline (Option C). Stage 4 verdicts for the first 4 chapters are PROPOSED-pending-canonical and batch-ratify after the canonical decision lands.

---

## §6. Open decisions captured (for author at session start)

To be filled in at session-start author conversation:

1. **Remote-container pipeline identification.** Which specific remote-container pipeline produces the better-rendering output the 2026-05-17 observation cited?
2. **Comparison scope.** Which source artifacts to compare-render? (Recommended: Ch 1 + Ch 6 + TA excerpt. Author confirms or adjusts.)
3. **Specific render differences observed.** What does "better" mean concretely? Examples: em-dash-in-bold renders cleanly without fallback-header; math formulas have better spacing; Greek letters use a different font; layout is tighter.
4. **Reproducibility priority weight.** If remote-container pipeline is opaque (e.g., uses Apple's system text-rendering which differs across iOS versions), how much does reproducibility-vs-fidelity trade-off matter for this project's publication timeline?
5. **Reviewer-distribution scenarios.** When the manuscript ships to Sandy / Darity / future reviewers + publisher: does the reviewer need to be able to *re-render* the source themselves (Option A favored) or just view the pre-built artifact (Option B viable)?

---

## §7. Sequencing — when this workstream fires

**This workstream fires in parallel with the first 4 retrofit workstreams** (Ch 1 + Ch 5 + Ch 6 + TA). Sequence:

1. **Ch 1 retrofit** (lightest; memoir baseline) — Stage 1a + 1c + Stage 4 render via BOTH pipelines + capture per-chapter comparison artifact on this workstream's branch. Stage 4 verdict = PROPOSED-pending-canonical-decision; Stage 5 sign-off deferred until verdict ratifies.
2. **Ch 5 retrofit** (mixed prose+analytical) — same dual-render + comparison capture.
3. **Ch 6 retrofit** (highest math-content outside TA) — same.
4. **TA retrofit** (full math; hardest case) — same.
5. **Canonical-pipeline decision** (this workstream §3.4) — author ratifies Option A/B/C after all 4 comparisons in hand.
6. **Apply decision** (this workstream §3.5) — doctrine update + build-environment.yaml population + tooling-or-workflow updates + batch-ratify Stage 4 verdicts for the 4 first-retrofit chapters.
7. **Roll forward** to the remaining 9 retrofit workstreams (Ch 2 + Ch 3 + Ch 4 + Ch 7 + Ch 8 + Ch 9 + Ch 10 + AuthorsNote + Dedication-conditional) using the ratified canonical pipeline.

**Practical implication:**
- The first retrofit session opens a feature branch for the chapter retrofit AND opens this workstream's branch (or the comparison-render artifacts land on the chapter retrofit branch + are migrated to this workstream's branch at sessions-3-4 batch-merge).
- PM-session task: decide whether each comparison-render lives on the per-chapter retrofit branch or on this workstream's branch. Recommended: per-chapter branch produces both the chapter retrofit artifacts AND the comparison artifact; the latter is consolidated into a single decision artifact on this workstream's branch at step 5.

**After this workstream completes:**
- 4 first-retrofit Stage 4 verdicts batch-ratified.
- The TA pre-publication refresh (F-7 cumulative oil/gas split CSV download + Pass 2 typography sweep) can fire against the canonical pipeline.
- CI workflow (`.github/workflows/corpus-invariants.yml`) may need a render-comparison job added per Option B/C.

---

## §8. Cross-references

- Stage 4 doctrine: [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md)
- Original publishing pipeline handoff: [`publishing-pipeline-handoff_2026-05-11.md`](publishing-pipeline-handoff_2026-05-11.md)
- Existing build scripts: [`tools/scripts/build-derivatives.sh`](../scripts/build-derivatives.sh) + `build-derivatives-alt.sh` + `fallback-header.tex`
- Defect-triage README: [`tools/scripts/README.md`](../scripts/README.md) §"Diagnosing rendering issues"
- Build-environment placeholder: [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml)
- Render-failure registry entries: [`tools/quality-gates/regressed-patterns.yaml`](../quality-gates/regressed-patterns.yaml) (render-failure category)

---

## §9. Cross-thread items

- **PM session task:** add cross-thread-todos entry flagging this workstream as HIGH priority (blocks Stage 4 retrofit audits).
- **Workstream-handoffs README registry:** add this workstream to the appropriate "Added" section.
- **Retrofit handoff updates:** once canonical pipeline is ratified, all 13 retrofit handoff stubs that reference "build-derivatives.sh" should be reviewed for accuracy (some may need to switch references to the new canonical remote-container-pipeline workflow per Option B).
- **Pipeline doctrine §11 quick-reference:** review for any stage-firing implications.

---

*End of render-pipeline-standardization workstream handoff. PROPOSED 2026-05-17. Blocks retrofit Stage 4 audits until resolved.*
