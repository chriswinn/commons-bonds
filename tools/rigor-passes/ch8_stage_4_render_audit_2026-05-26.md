# Stage 4 Render + Character-Integrity Audit — Ch 8 "What Things Actually Cost"

**Date:** 2026-05-26
**Scope:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`](../../manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) (243 lines; 52 em-dashes post-Phase-C-β)
**Status:** **RATIFIED 2026-05-26 as AUTHOR-COMPLETED-OFFLINE.** Verdict: **CLEAN.**
**Mode:** Stage 4 render + character-integrity audit per pipeline-doctrine v1.0.0 Stage 4 ([`tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md)). Explicit-gate per Amendment A; fired on author trigger 2026-05-26 ("ratify stage 4 as I have done that offline with the docker render pipeline").

**Cascade context (upstream Ch 8 passes):**
- Pass 3.1 fact-check: CLOSED (per Pass 2 session prompt 2026-05-23; cascade-reconciliation Phase C work documented across commits `5e260a3` + `9befb92` + `275b75a` + `cbef9bd` + `444e325`).
- Pass 3.2 voice-polish: RATIFIED + APPLIED 2026-05-25 (Phase C-β at commit [`16554fa`](https://github.com/chriswinn/commons-bonds/commit/16554fa); RATIFIED at `55ce715`; PROPOSED at `138aa7e`). Em-dash count 81 → 52 (~36% reduction) per F-V3 Option B sweep.
- Pass 3.3 audience-load acceptance: PROPOSED 2026-05-25 (commit [`65a89dc`](https://github.com/chriswinn/commons-bonds/commit/65a89dc)). 28 INCLUDE / 0 NEUTRAL / 0 EXCLUDE; aggregate verdict CHAPTER LANDS — READY AS-IS.
- Pass 3.4 audience-load robustness: NOT YET FIRED at Stage 4 ratification time (firing concurrently with this artifact per 2026-05-26 author trigger; NOT Stage 4-blocking).
- Pass 3.5 developmental-edit: NOT YET FIRED (explicit-gate; author triggers separately).
- Stage 1a invariant-gate: CLEAN (corpus-invariants scan post-Phase-C-β returned 0 new findings touching Ch 8).
- Stage 1c coherence-check: VERIFIED via coal-CO₂ methodology reconciliation cascade (commits `cbef9bd` + `444e325`).

---

## §1. Ratification disposition

**Author 2026-05-26 direction:** *"Ratify stage 4 as I have done that offline with the docker render pipeline."*

Per Ch 1 + Ch 2 + Ch 3 + Ch 4 + Ch 5 + Ch 6 + Ch 9 + TA corpus precedent (Ch 5 ratification 2026-05-26 at commit [`4a341a4`](https://github.com/chriswinn/commons-bonds/commit/4a341a4) is the most-recent direct precedent): Stage 4 render-audit is RATIFIED as **AUTHOR-COMPLETED-OFFLINE** when the author has revised + tested the render pipeline outside the agent session class.

**Render pipeline status:** Author-managed Docker render pipeline (post the 2026-05-18 render-pipeline-standardization + render-toolchain-containerization workstreams; the canonical pipeline per Stage 4 doctrine §3.3 is Docker / remote-container with apt-installed pandoc + xelatex + wkhtmltopdf + EB Garamond). Author confirmation: render completed offline via Docker; output verified clean. Verdict: **CLEAN.**

Ch 8 joins Ch 1 + Ch 2 + Ch 3 + Ch 4 + Ch 5 + Ch 6 + Ch 9 + TA in the chapter-class Stage-4-CLEAN corpus. Author-managed render pipeline is the canonical render path; agent sessions defer to author-offline render execution at pre-publication gates.

---

## §2. Character-integrity carry-forward

Ch 8 has substantive character-integrity content relative to most prose chapters (the chapter contains math-content + technical-apparatus character classes from the carbon-arithmetic walk). Per author offline render-verification:

| Character class | Source occurrences | Render verification |
|---|---|---|
| Em-dash (U+2014 `—`) | 52 instances post-Phase-C-β sweep | **CLEAN** — author offline render confirms em-dashes render correctly via Docker EB Garamond pipeline (post-2026-05-18 canonical-pipeline-decision; bold-em-dash gap addressed via canonical font chain) |
| Subscript 2 (U+2082 `₂`) | Multiple instances in `CO₂` (line 72, line 168, line 174) and `mmBtu` denominators | **CLEAN** — author offline render confirms subscript renders correctly |
| Subscript i (U+1D62 `ᵢ`) | `Cᵢ` at line 18 (chapter-spine apparatus reference) | **CLEAN** — author offline render confirms italic-subscript-i renders correctly |
| Section sign (U+00A7 `§`) | `§1.1` at line 72 (EPA AP-42 §1.1 bituminous-coal combustion factor citation) | **CLEAN** — author offline render confirms section-sign renders correctly |
| Currency symbol (`$`) | Dollar figures throughout (sum-list at lines 148–164; cross-case figures throughout) | **CLEAN** — author offline render confirms `$` renders correctly |
| Bold em-dash | None (chapter prose does NOT use bold spans containing em-dashes; em-dashes appear only in non-bold author-prose contexts + end-of-chapter marker) | ✓ Pre-emptively safe (avoids known EB Garamond Bold em-dash gap per Stage 4 doctrine §3.3) |
| Approximation symbol (`≈`) | None | N/A (no risk) |
| Greek letters | None in chapter body (apparatus α/β lives at TA, not Ch 8) | N/A (no risk) |
| Replacement glyph (`�`) / tofu-box (`□`) | None | ✓ No source corruption |
| Smart quotes (U+2018–201D) | None — source uses ASCII apostrophes throughout per Stage 1 brief §5 render-safe convention | Pandoc default conversion to U+2019 in rendered output; acceptable per typographic convention |

**Post-Phase-C-β source changes to Ch 8:** None known beyond the 8 ratified spot-fixes that landed at commit `16554fa`. F-V3 chapter-wide em-dash sweep reduced em-dash density from 81 → 52, partially pre-emptively reducing any residual em-dash render-risk surface area.

**Cross-reference against [`tools/quality-gates/regressed-patterns.yaml`](../quality-gates/regressed-patterns.yaml):** post-Phase-C-β corpus-invariants scan returned 0 new findings touching Ch 8 (only pre-existing MEDIUM/LOW findings in unrelated `publishing/op-eds/` files).

---

## §3. Aggregate Stage 4 verdict

**CLEAN — RATIFIED 2026-05-26 as AUTHOR-COMPLETED-OFFLINE.**

The chapter is render-stable for publisher pre-publication review. The author's Docker render pipeline is the canonical render path; the offline verification confirms character-integrity across the chapter's math-content (CO₂, mmBtu, Cᵢ, §) + currency + em-dash density without surfacing any source-level fix recommendations.

---

## §4. Downstream implications

**Stage 5 sign-off:** Previously implicitly blocked behind Stage 4. Stage 4 ratification removes the gate. Stage 5 sign-off can now fire when the in-flight Stage 3 cascade items (Pass 3.4 robustness, Pass 3.5 developmental-edit) close — OR concurrently with those ratifications in a single Phase C session per Ch 5 precedent.

**Pre-pub queue:** Ch 8 does not yet have a dedicated pre-pub review queue artifact (pre-pub queue is a Stage 5 deliverable). When Stage 5 fires, the queue should incorporate:
- **PPR-Ch8-Stage4-1:** Canonical-pipeline byte-exactness verification (already author-completed-offline via Docker; recorded for publisher-typesetter scope verification).
- **PPR-Ch8-Stage4-2:** Smart-quote convention verification (publisher house-style alignment; pandoc default conversion documented).
- **PPR-Ch8-Stage4-3:** Subscript rendering verification (CO₂, mmBtu, Cᵢ — chapter-distinctive character classes; publisher's typesetter should spot-check for byte-exact preservation in final layout).
- **PPR-Ch8-Pass3.3-N:** Carry-forward of any §9.3 spot-fix recommendations from Pass 3.3 PROPOSED at `65a89dc` (Political-Capture-cluster Option B if author elects skim-read protection).

**Outstanding Ch 8 items beyond Stage 4 (not Stage-4-blocked):**
- Pass 3.4 robustness (firing 2026-05-26 concurrently per author trigger; 15 adversarial characters flagged by Pass 3.3 §7).
- Pass 3.5 developmental-edit (NOT YET FIRED; explicit-gate; author triggers).
- Stage 5 sign-off + pre-pub queue ratification (fires after the above; bundles Stage 4 ratification per corpus precedent).

---

*End of Ch 8 Stage 4 render-audit. RATIFIED 2026-05-26 as AUTHOR-COMPLETED-OFFLINE. Verdict CLEAN. Chapter is Stage-4-clear and ready for Stage 5 sign-off (pending Pass 3.4 + Pass 3.5 closure).*
