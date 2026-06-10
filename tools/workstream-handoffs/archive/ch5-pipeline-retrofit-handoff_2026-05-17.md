# Ch 5 Pipeline-Retrofit Handoff

**Date drafted:** 2026-05-17
**Branch prefix:** `claude/ch5-pipeline-retrofit-`
**Chapter:** Ch 5 — *The Accountability Gap* (`manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md`)
**Status going in:** Three-pass cycle CLOSED 2026-05-14. Phase C-β applied.
**Template:** [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
**Parent doctrine:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)

---

## §1. Retrofit scope

Per the retrofit table in [`README.md`](README.md): **1a + 1c + 3.4 + 4 + 5**

Sub-steps to fire this session:

| Sub-step | Fire? | Notes |
|---|---|---|
| 1a invariant gate | YES | Expected CLEAN per current registry. The "settlement-ratified" use at line 48 is allowlisted. |
| 1c coherence check | YES | Verify Ch 5's $44B / $108T / 2008-foreclosure / Deepwater Horizon canonical anchors against current cross-chapter state + Ch 6 + Tech Appendix. Verify Darity-Mullen reparations-typology framing (per MI-1 incorporation) holds against current Ch 6 + TA §5.5 articulation. |
| 3.1 verify | NO | Pass 1 ratified + applied (incl. MUST-FIX-2 $108T misattribution + MEDIUM-2 NOAA biological-magnitude + MEDIUM-3 OASI-2033 + MEDIUM-4 BP-Mexico 2018 + N-3 foreclosure measure tightening). |
| 3.2 verify | NO | Pass 2 PROPOSED at commit `dd3c684`; Phase C-β applied at `c35cb03`. Includes F-V1 inverted-logic + F-V2 "not Ponzi scheme" article + F-V3 Ohio-comparison rebuild + F-V4 line 138 OASI-2033 alignment + F-V5 116-124 opportunity-cost framing + F-V6/V7 NOAA + CBO + F-V8 GAO 2011 cumulative-not-peak + F-V9 coerced-cases legacy-effects. |
| 3.3 acceptance | NO | Original Pass 3 acceptance ratified per Pre-Phase-C work. Adversarial test was not run under pre-v3.0 framing. |
| 3.4 robustness | YES — fresh | First Pass 3.4 robustness test (adversarial set). Highest-priority retrofit element for Ch 5. Anticipate Public Choice + libertarian + WSJ-business-press + tort-reform-lawyer adversarial reads on the 2008-rescue-asymmetry + Social-Security-as-cost-severance arguments. |
| 4 render-integrity | YES — **TRIPLE-RENDER (comparison-mode)** | Ch 5 is the **second** of 4 chapters firing in parallel with the render-pipeline-standardization workstream. Render via THREE pipelines: (1) remote-container baseline (pre-rendered 2026-05-17 at BASE `9ffad4e`); (2) laptop `build-derivatives.sh`; (3) laptop `build-derivatives-alt.sh` — both laptop scripts active per author direction 2026-05-17. Drop outputs in `tools/scripts/comparison-renders/ch5_2026-05-17_9ffad4e/laptop-build-derivatives/` + `.../laptop-build-derivatives-alt/`. Test specifically: $108T / $4.6B dollar-figure renderings; em-dash density at lines 116-124 (opportunity-cost framing); Method 1/2/3 bolded section heads at line 214 (em-dash in bold; fallback-header.tex coverage critical here, so `build-derivatives-alt.sh` likely shows the bigger improvement vs `build-derivatives.sh` for the bolded em-dashes). Capture per-chapter comparison artifact. Stage 4 verdict = **PROPOSED-pending-canonical-decision**. Laptop tuning per round; do NOT tune mid-render. |
| 5 sign-off + pre-pub queue | DEFERRED | Stage 5 deferred until Stage 4 verdict ratifies (post canonical-pipeline decision). Pre-pub queue drafted PROPOSED with recommended external reviewer types: labor-economics reviewer (Darity-Mullen tradition); financial-system / Federal-Reserve emergency-lending scholar; reparations-economics methodologist. Ratifies in batch with Stage 4. |

---

## §2. Prior cycle status

- Pass 1 fact-check: RATIFIED + APPLIED via Phase C-α commit `da26bdc`. Authoritative-source verification round commit `999bd73` (Amendment 2, 2026-05-13).
- Pass 2 voice-polish: PROPOSED at `dd3c684`; RATIFIED + APPLIED at Phase C-β `c35cb03`. Sandy-Darity-send-ready.
- Pass 3 audience-load: acceptance per original 20-character set was run + integrated through MI-1/MI-2 incorporation. Pre-v3.0 framing did NOT include adversarial-detractor robustness test; the v3.0 retrofit fires Pass 3.4 to close that gap.
- Sandy-Darity packet shipped 2026-05-13 (Ch 5 + Ch 6 + TA derivatives).

---

## §3. Chapter-specific notes

- **Sandy interview completed 2026-05-13.** Sandy's response material may be in `research/outreach/subjects/darity/` and informs MI-1 / MI-2 / SI-1 incorporation. Stage 1c coherence check verifies Ch 5 reflects post-interview canonical framing.
- **Cross-chapter rent-seeking handoff readiness.** Ch 5 is one of the touched chapters in the cross-chapter rent-seeking-engagement workstream (per `cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`). Retrofit sequencing: prefer AFTER rent-seeking workstream touches land.
- **Bidirectional methodology framing (Approach B ratified).** Ch 5 contains the ~620w "Restitution and Foreclosure" section + Ch 10 summary echo (~100w) per TA §5.5 bidirectional articulation. Stage 1c verifies the chapter prose aligns with TA §5.5.
- **2008-rescue-asymmetry adversarial exposure.** The chapter's 2008-financial-crisis cost-severance argument is the highest-adversarial-exposure passage. Pass 3.4 should specifically test:
  - WSJ editorial-board reader / business-press conservative (reads framework-promise + no-villain framing as preparation for business-blame regulation)
  - Tort-reform / fiduciary-protection lawyer (reads bond-instruments as litigation-amplification threat)
  - Orthodox-econ reader (Chicago School): does the cost-severance framing land vs Friedman-tradition counter-argument?
  - Public Choice theorist: cross-chapter handoff thread (Ch 1 REAUDIT v3 §5.3 disposition recommends Ch 5 as one engagement site).
- **$108T figure framing**. The MUST-FIX-2 opportunity-cost reframe at line 112 + the surrounding 116-124 paragraphs are load-bearing post-Phase-C-β work. Stage 1c + Pass 3.4 should verify both that the framing holds + that the adversarial set engages it cleanly.

---

## §4. Cross-references

- Pipeline doctrine: [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)
- Retrofit template: [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
- Cross-chapter rent-seeking workstream: [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)
- Pass 1 + Phase C-α verification: `tools/rigor-passes/commons_bonds_ch5_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md`
- Pass 2 + Phase C-β application: `tools/rigor-passes/commons_bonds_ch5_stage_3_pass_2_voice_polish_2026-05-14_PROPOSED.md`

---

*End of Ch 5 pipeline-retrofit handoff. PROPOSED 2026-05-17. Lightest-of-the-already-closed-cycle retrofits + **SECOND** of the 4 standardization-comparison-bed retrofits (Ch 1 → Ch 5 → Ch 6 → TA). Stage 4 verdict batch-ratifies post canonical-pipeline decision per [`render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md). Sequence AFTER cross-chapter rent-seeking workstream lands.*
