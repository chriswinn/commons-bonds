# Render-Toolchain Containerization — Workstream Handoff

**Date drafted:** 2026-05-18
**Workstream:** Render-toolchain containerization (canonical render-environment pinning via Docker + remote-container setup script)
**Status:** PROPOSED — awaiting author ratification + PM session spinup
**Recommended branch prefix:** `claude/render-toolchain-containerization-`
**Origin:** Author observation 2026-05-17 → 2026-05-18 standardization workstream: past remote-container sessions produced the best renders for the corpus, but the toolchain capture is partial (architecture documented in `e6ddf92`; specific versions captured ad-hoc in `build-environment.yaml` 2026-05-17). Reproducibility across sessions / machines / future-author / collaborators requires a canonical containerized environment that any context can spin up.
**Parent doctrine:** [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) §3.3
**Companion / predecessor:** [`render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md) — the canonical-pipeline-decision workstream this artifact operationalizes.

---

## §0. Background — how this surfaced

The 2026-05-17 standardization workstream surfaced two reproducibility weaknesses:

1. **Past remote-container sessions documented their toolchain partially.** Commit `e6ddf92` (Sandy packet, 2026-05-15) documented the rendering ARCHITECTURE (pandoc + xelatex + wkhtmltopdf + reference.docx + EB Garamond) but NOT specific versions (pandoc 2.x vs 3.x; xelatex from which TeX Live; wkhtmltopdf 0.12.6 with which Qt). Each new remote-container session apt-installs the toolchain fresh + version drift across sessions is possible.

2. **Laptop pipeline reproducibility is not pinned.** The build-environment.yaml stamp (2026-05-17) was the first specific-version capture; the laptop's Homebrew toolchain may drift from that stamp without explicit pinning.

Per 2026-05-18 author direction: "couldn't we do both [Docker container locally + setup script for remote-container] by creating a reusable setup script for a docker container?"

The answer is yes — one canonical installer script that's apt-based, then both Docker (local) + remote-container (Anthropic-cloud) invoke the same script. Single source-of-truth for the render toolchain; eliminates drift between contexts.

---

## §1. The substantive question this workstream answers

How does the project guarantee that the render toolchain is reproducible across:

- The author's laptop (via Docker)
- Anthropic's remote Claude Code containers (via session-start setup script)
- Future collaborators' machines
- CI render-verification workflows
- Six-months-from-now-rebuilds of the same source commit

— without per-session apt drift, without per-laptop Homebrew drift, and without re-deriving the toolchain stamp each time.

The answer is: **one canonical installer + a Dockerfile that consumes it + a remote-container setup hook that consumes it + a CI job that consumes it.** All four contexts derive from the same script.

---

## §2. Branch discipline

```
git fetch origin
git checkout -b claude/render-toolchain-containerization-<harness-id> origin/main
```

Per CLAUDE.md merge-to-main default: this workstream produces internal-scaffolding artifacts (`tools/scripts/`-side; no chapter content edits). Qualifies for autonomous fast-forward merge to main at session close per the doctrine-cluster pattern.

---

## §3. Read order

1. THIS handoff.
2. [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml) — current canonical toolchain stamp; the installer script's pinned-version targets.
3. [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) §3.3 — canonical-pipeline doctrine; OPEN flag context.
4. [`tools/workstream-handoffs/render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md) — the canonical-pipeline-decision workstream this artifact operationalizes.
5. [`tools/rigor-passes/render_pipeline_comparison_ta_2026-05-18.md`](../rigor-passes/render_pipeline_comparison_ta_2026-05-18.md) — TA Stage 4 comparison + canonical-decision verdict; specifically §13 + §13.1 for the wkhtmltopdf Qt 5.15.13 vs Qt 4.8.7 / OS-font-stack divergence that motivates pinning Linux containerization.
6. [`tools/scripts/build-derivatives.sh`](../scripts/build-derivatives.sh) + [`tools/scripts/build-derivatives-alt.sh`](../scripts/build-derivatives-alt.sh) + [`tools/scripts/fallback-header.tex`](../scripts/fallback-header.tex) — current scripts that the installer's toolchain supports.
7. Claude Code on the web docs section on environment setup scripts: <https://code.claude.com/docs/en/claude-code-on-the-web> — verify current contract for `.devcontainer/` or equivalent.

---

## §4. Mission

Produce a unified containerized render-toolchain installer + supporting artifacts. Deliverables enumerated in §5.

### §4.1 Architecture

```
tools/scripts/install-render-toolchain.sh   ← CANONICAL installer.
                                              Apt-based; targets Ubuntu/Debian 24.04.
                                              Pinned versions per build-environment.yaml.
                                              Idempotent; supports --check verification mode.

tools/scripts/Dockerfile.render             ← Docker image build:
                                              FROM --platform=linux/amd64 ubuntu:24.04
                                              + copy + run install-render-toolchain.sh.

.devcontainer/devcontainer.json             ← Claude Code on web auto-setup
  (or equivalent platform-specific file)    (invokes install-render-toolchain.sh at
                                              session start; per Claude Code on the
                                              web environment-config docs).

.github/workflows/render-verify.yml         ← CI job that builds the Docker image +
  (optional; per author preference)          renders a canonical test artifact +
                                              verifies byte-stable output across runs.
```

All four contexts derive from one script.

### §4.2 The installer script — `install-render-toolchain.sh`

Required behavior:

1. **Idempotent.** Running twice produces the same end-state; no errors.
2. **Pinned versions** per `build-environment.yaml`:
   - pandoc 3.1.3 (via apt)
   - texlive-xetex (TeX Live 2023 minimum)
   - wkhtmltopdf 0.12.6
   - fonts-ebgaramond + fonts-dejavu
   - Other dependencies as needed (e.g., python3 if pdftotext extraction or comparison scripts call it)
3. **Verification mode** (`--check` or `--verify`): does NOT install; reports whether the environment matches the canonical. Returns non-zero on mismatch. Useful as a pre-flight check at retrofit Stage 4 sessions + as a CI assertion.
4. **Capture-stamp mode** (`--capture-stamp`): writes the actually-installed toolchain versions to a target file path (default: `build-environment.yaml`-format snippet). Lets the installer auto-update the canonical stamp when apt versions advance.
5. **Required-fonts validation**: post-install verification that `fc-list` reports EB Garamond + DejaVu Serif.
6. **Optional Chrome handling**: documented as a known-open-item — Chrome via snap is blocked in some remote-container configurations; direct deb download may also be blocked by network policy. Either (a) include best-effort Chrome install with documented fallback to wkhtmltopdf, or (b) explicitly defer Chrome to a follow-up workstream + flag in canonical-decision artifact. PM session decides at spinup.

### §4.3 The Dockerfile — `Dockerfile.render`

Lean. ~10-15 lines:

```dockerfile
FROM --platform=linux/amd64 ubuntu:24.04
WORKDIR /work
COPY tools/scripts/install-render-toolchain.sh /tmp/
COPY tools/scripts/fallback-header.tex /tmp/
COPY tools/scripts/reference.docx /tmp/
RUN /tmp/install-render-toolchain.sh
# Optional: COPY in build-derivatives.sh + entrypoint for direct render invocation
```

Build:
```bash
docker build -t commons-bonds-render -f tools/scripts/Dockerfile.render .
```

Run a render:
```bash
docker run --rm \
  -v $(pwd):/work \
  -w /work \
  commons-bonds-render \
  tools/scripts/build-derivatives.sh manuscript/chapters/Chapter__1_TheQuietMath__Draft.md
```

Architecture pinning: `--platform=linux/amd64` ensures byte-level output reproducibility between local Docker + remote-container (which is x86_64). On Apple Silicon, runs under Rosetta with negligible CPU overhead (~5 seconds per render).

### §4.4 Remote-container setup hook

Per Claude Code on the web docs: configure the environment's session-start setup to invoke `tools/scripts/install-render-toolchain.sh`. Mechanism is platform-specific (`.devcontainer/` files; environment configuration UI; CLI flags); verify current contract at session-start.

The script's idempotency means re-running across session boundaries is safe.

### §4.5 CI render-verification (optional per §4.1)

A GitHub Actions workflow that:
1. Builds the Docker image (cached when Dockerfile unchanged).
2. Renders a small canonical test artifact (e.g., a known-good 1-page markdown + verify against checked-in expected output).
3. Asserts byte-stable rendering.
4. Runs on PRs that touch `tools/scripts/build-derivatives*.sh` + `tools/scripts/install-render-toolchain.sh` + `tools/scripts/Dockerfile.render` + `build-environment.yaml`.

Catches accidental toolchain drift in PRs.

### §4.6 README + docs

Update `tools/scripts/README.md` with sections covering:
- **How to install Colima + docker CLI on macOS** (canonical per author direction 2026-05-18; fully open-source). Quick path: `brew install colima docker`. Start: `colima start --arch x86_64 --cpu 4 --memory 4` (specific resource sizing TBD during session). Docker Desktop mentioned only as a "if you already have it" alternative.
- How to build + run the canonical render container.
- How to verify local environment matches canonical (via `--check` mode).
- How to update the canonical when toolchain advances (capture new stamp + commit).
- Reference to the Claude Code on web setup mechanism.

---

## §5. Output deliverables

| Artifact | Path |
|---|---|
| Canonical installer | `tools/scripts/install-render-toolchain.sh` |
| Dockerfile | `tools/scripts/Dockerfile.render` |
| Remote-container setup hook | `.devcontainer/devcontainer.json` (or platform-specific equivalent) |
| CI workflow (optional) | `.github/workflows/render-verify.yml` |
| Updated build-environment.yaml | Stamp includes pinned-version assertions + Docker recipe pointer |
| Updated tools/scripts/README.md | Sections for Docker invocation + setup-script reference + verification mode |
| Updated tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md §3.3 | Drop OPEN flag if Docker reproducibility resolves the canonical-pipeline decision via Option B; otherwise note Docker as the canonical infrastructure with Option-A/B/C decision still author-ratifiable |
| Verification test artifacts | `tools/scripts/render-verify-fixtures/` — small known-good markdown + expected `.docx` + `.pdf` for CI byte-comparison |

---

## §6. Sequencing + dependencies

**Prerequisites:**
- Canonical-pipeline decision (Option A/B/C) per render-pipeline-standardization-handoff §3.4 should ideally be ratified first. If Option A (laptop canonical Chrome HTML→PDF) is ratified, this workstream still produces value as a reproducibility layer + cross-check. If Option B (remote-container canonical), this workstream IS the operationalization. If Option C (dual-discipline), this workstream produces one of the two canonical pipelines explicitly.
- F-RP-TA-01 fix (conditional `--from=markdown-yaml_metadata_block`) per TA comparison §9.1 should be applied before this workstream's CI render-verification fires (otherwise CI catches the F-RP-TA-01 docx regression as a "drift" when it's actually a known bug).

**Sequencing recommendation:**
1. Ratify canonical-pipeline decision (Option A/B/C) — short author decision; could happen alongside or before this workstream fires.
2. Apply F-RP-TA-01 fix — one-line script change in build-derivatives.sh + build-derivatives-alt.sh (or in the merged-canonical script if that consolidation happens here).
3. Fire this workstream — produces the installer + Dockerfile + setup hook + (optional) CI workflow + README updates.
4. Verify on both architectures (ARM64 native + amd64-under-Rosetta on Apple Silicon Mac).
5. Update build-environment.yaml status to `RATIFIED` once Docker recipe verified.

**Estimated session length:** 1-2 hours of focused work. Primary cost: testing the installer in a fresh Ubuntu 24.04 container; verifying Dockerfile builds clean on first try (apt-cache may need refresh); testing on Apple Silicon if available.

**Can run in parallel with:**
- Remaining 9 retrofit workstreams (Ch 2 / Ch 3 / Ch 4 / Ch 7 / Ch 8 / Ch 9 / Ch 10 / AuthorsNote / Dedication). They use the current build-derivatives scripts; this workstream's deliverables become canonical once they land.
- Future per-chapter prose-flatness developmental-editing workstreams (separate concern; doesn't touch render pipeline).

**Blocked by:**
- Nothing structurally. Could fire immediately upon PM session ratification.

---

## §7. Hard constraints

- Do NOT touch chapter content. This is `tools/`-side scaffolding.
- Do NOT proceed if the apt-installed toolchain produces RENDERS that don't match the build-environment.yaml stamp from 2026-05-17. If they don't match, that's a "the canonical stamp needs updating" finding — flag + capture before proceeding.
- The Dockerfile MUST use `--platform=linux/amd64` for byte-level reproducibility with remote-container. If amd64 emulation on Apple Silicon proves too slow for the user's workflow, that's a follow-up; do NOT default to native arm64 without explicit author ratification.
- The installer script MUST be idempotent. Running twice = same outcome.
- The installer script MUST support `--check` verification mode (no install; reports mismatch).
- The installer script MUST handle apt failure modes gracefully (network policy 403; package not found; etc.) with clear error messages pointing at remediation.
- Per CLAUDE.md: never force-push main; this workstream auto-merges per doctrine-cluster pattern at session close.

---

## §8. Open decisions (for author at session start)

1. **Chrome installation strategy.** Include best-effort Chrome install in the script (preferred for HTML→PDF per F-RP-TA-05) with documented fallback to wkhtmltopdf, OR explicitly defer Chrome to a follow-up workstream + ship the installer + Dockerfile with wkhtmltopdf-only for now. Recommendation: defer Chrome to follow-up; document the gap; ship wkhtmltopdf-canonical container first. Chrome installability in the snap-blocked / network-restricted Anthropic container is itself an open follow-up per build-environment.yaml notes.

2. **CI render-verification scope.** Include it in this workstream, or defer to a separate "CI render-verification" workstream after the canonical artifacts land? Recommendation: include it; it's the single most useful drift-catcher long-term and the marginal effort vs the rest of the workstream is small.

3. **Docker Desktop vs Colima recommendation in README.** ~~Recommendation: document both equally...~~ **RATIFIED 2026-05-18 — Colima (fully open-source).** README documents Colima as the canonical Docker runtime for macOS author + collaborators; Docker Desktop is mentioned only as a "if you already have it installed" alternative. Install via `brew install colima docker` then `colima start --arch x86_64` (or `colima start` for native ARM64 + later override per-build). All `docker` CLI invocations in the README assume Colima context.

4. **Architecture pinning posture.** `--platform=linux/amd64` strict for byte-reproducibility (Rosetta on Apple Silicon; ~5 second cost per render), or default to native arm64 with amd64 build available as an opt-in flag? Recommendation: strict amd64 default; document the native-arm64 override path for power-users who don't need byte-reproducibility.

---

## §9. Cross-references

- Pipeline doctrine: [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)
- Stage 4 doctrine: [`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md)
- Canonical-pipeline standardization workstream: [`render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md)
- TA Stage 4 comparison + correction: [`tools/rigor-passes/render_pipeline_comparison_ta_2026-05-18.md`](../rigor-passes/render_pipeline_comparison_ta_2026-05-18.md)
- Build-environment stamp: [`tools/quality-gates/render-baselines/build-environment.yaml`](../quality-gates/render-baselines/build-environment.yaml)
- Existing scripts: [`tools/scripts/build-derivatives.sh`](../scripts/build-derivatives.sh) + [`tools/scripts/build-derivatives-alt.sh`](../scripts/build-derivatives-alt.sh) + [`tools/scripts/fallback-header.tex`](../scripts/fallback-header.tex)
- Comparison-renders dir layout: [`tools/scripts/comparison-renders/README.md`](../scripts/comparison-renders/README.md)

---

## §10. Cross-thread items

- **PM session task:** add cross-thread-todos entry flagging this workstream for spinup; tracking entry should reference the canonical-pipeline-decision dependency (§6).
- **Workstream-handoffs README registry update:** add this workstream to the "Added 2026-05-18" section (or whatever date the handoff gets ratified).
- **build-environment.yaml status update post-completion:** pipeline_canonical_status RATIFIED + Docker recipe pinned alongside toolchain stamp.
- **Stage 4 doctrine §3.3 update post-completion:** drop the OPEN flag (or partially close per canonical-pipeline decision); reference the canonical containerized environment as the reproducibility infrastructure.
- **AGENTS.md row update post-completion:** add a "Render toolchain" row pointing to the installer + Dockerfile.

---

## §11. PM session spinup metadata

**Workstream name:** Render-toolchain containerization
**Trigger to spin up:** PM session ratification + canonical-pipeline decision per render-pipeline-standardization-handoff §3.4 (concurrent ratification acceptable).
**Estimated session length:** 1-2 hours. Single substantial session.
**Branch:** `claude/render-toolchain-containerization-<harness-id>` from current `origin/main`.
**Merge-to-main default:** per CLAUDE.md, doctrine-cluster / tools-side scaffolding autonomously fast-forward merges to main at session close.

**Post-completion success criteria:**
- `tools/scripts/install-render-toolchain.sh` on main; idempotent; supports --check + --capture-stamp modes; tested in a fresh Ubuntu 24.04 container.
- `tools/scripts/Dockerfile.render` on main; builds cleanly with `--platform=linux/amd64`; verified to produce render output matching the 2026-05-17 build-environment.yaml stamp.
- Remote-container setup hook on main (.devcontainer/ or equivalent); next remote Claude Code session auto-runs the installer at session start.
- (Optional) CI render-verification workflow on main; passes against a known-good test fixture.
- README + Stage 4 doctrine §3.3 + build-environment.yaml + AGENTS.md updated.

---

*End of render-toolchain containerization workstream handoff. PROPOSED 2026-05-18. Awaiting PM session spinup ratification.*
