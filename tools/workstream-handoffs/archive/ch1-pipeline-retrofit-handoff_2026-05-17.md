# Ch 1 Pipeline-Retrofit Handoff

**Date drafted:** 2026-05-17
**Branch prefix:** `claude/ch1-pipeline-retrofit-`
**Chapter:** Ch 1 — *The Quiet Math* (`manuscript/chapters/Chapter__1_TheQuietMath__Draft.md`)
**Status going in:** Three-pass cycle CLOSED (2026-05-17); REAUDIT v3 PROPOSED + ratified-as-applied for Items (i) + (iv).
**Template:** [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
**Parent doctrine:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)

---

## §1. Retrofit scope

Per the retrofit table in [`README.md`](README.md): **1a + 1c + 3.4 (already done; REAUDIT v3 PROPOSED) + 4 + 5**

Sub-steps to fire this session:

| Sub-step | Fire? | Notes |
|---|---|---|
| 1a invariant gate | YES | First invariant scan against Ch 1 source. Expected CLEAN per 2026-05-17 leak-check survey expectation. |
| 1c coherence check | YES | Verify bibliography §21 LOAD-BEARING Dunbar/Du Bois commitment realized post-REAUDIT v3 Item (iv) application; verify AuthorsNote alignment. |
| 3.1 verify | NO | Pass 1 RATIFIED + APPLIED (commit chain `a29f3f4` → `13faa0f`). |
| 3.2 verify | NO | Pass 2 RATIFIED + APPLIED (commit `7b4aa92`). |
| 3.3 acceptance | NO | Pass 3 acceptance ratified per REAUDIT v3 (40-character set covered both acceptance + robustness in single artifact). |
| 3.4 robustness | NO | Already done as part of REAUDIT v3 (10-char adversarial set + thread-pull synthesis §5.3). Reference artifact: `tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`. |
| 4 render-integrity | YES — **TRIPLE-RENDER (comparison-mode)** | Ch 1 is the **first** of 4 chapters firing in parallel with the render-pipeline-standardization workstream. Render via THREE pipelines: (1) remote-container baseline (pre-rendered 2026-05-17 at BASE `9ffad4e`); (2) laptop `build-derivatives.sh`; (3) laptop `build-derivatives-alt.sh` — both laptop scripts active per author direction 2026-05-17 (canonical between them not yet ratified). Drop outputs in `tools/scripts/comparison-renders/ch1_2026-05-17_9ffad4e/laptop-build-derivatives/` + `.../laptop-build-derivatives-alt/` respectively. Capture per-chapter comparison artifact covering all three pipelines. Stage 4 verdict = **PROPOSED-pending-canonical-decision** (batch-ratifies after standardization workstream §3.4 author decisions on canonical-pipeline AND canonical-laptop-script). Laptop tuning per round; do NOT tune mid-render. |
| 5 sign-off + pre-pub queue | DEFERRED | Stage 5 deferred until Stage 4 verdict ratifies (post canonical-pipeline decision). Pre-publication review queue artifact drafted PROPOSED at retrofit session close; ratifies in batch with Stage 4. |

Effectively this is the lightest retrofit in the set: 1a + 1c + 4 + 5 only (3.4 already complete).

---

## §2. Prior cycle status

- Pass 1 fact-check: PROPOSED `afddeed`; RATIFIED + APPLIED via Phase C commit chain (`a29f3f4` F-1, `6594107` F-2, `008ac3f` F-3, `4a03f2f` F-5+F-6, `cfb08ce` F-7, `99e17fe` F-8, `fb1595b` F-9, `13faa0f` F-10+F-11+F-12).
- Pass 2 voice-polish: PROPOSED `0b78449`; RATIFIED + APPLIED at `7b4aa92` (10 spot-fixes including F-V1 nostalgia tic + F-V2 cadence-repetition).
- Pass 3 audience-load: original 20-character PROPOSED at `tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_2026-05-15_PROPOSED.md`; REAUDIT v3 40-character (30 acceptance + 10 adversarial) PROPOSED at `tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`; Items (i) + (iv) RATIFIED + APPLIED at `013415f` + `f692164`; Item (iv) bibliography commitment work landed.

---

## §3. Chapter-specific notes

- **Memoir register.** Ch 1 is the only chapter in fully-memoir register (no apparatus); Stage 4 render-integrity audit is straightforward (no math content, no formulas).
- **Cross-chapter handoff from REAUDIT v3 Pass 3.4.** The Public Choice rent-seeking-engagement thread (#33 adversarial character pulled by 5 chars) became the rent-seeking-engagement cross-chapter workstream (handoff: [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)). Ch 1 spot-fix not warranted (would damage acceptance verdicts); the cross-chapter handoff is the disposition. Pre-pub review queue should flag this for publisher transparency.
- **Bibliography commitments to verify.** Item (iv) Dunbar/Du Bois at line 103 (post-spot-fix at line 105) carries the bibliography §21 LOAD-BEARING commitment. Stage 1c coherence check verifies the commitment is realized in current prose.
- **AuthorsNote register-split.** Ch 1 anonymizes father / son / grandfather; AuthorsNote names grandfather formally (LaVern E. Winn). The register-split is deliberate + Pass 1 §3 consent-verified. Stage 1c verifies consistency with current AuthorsNote.
- **Named-subject consent.** No new living named subjects in Ch 1 retrofit scope.

---

## §4. Cross-references

- Pipeline doctrine: [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)
- Retrofit template (procedure + read order): [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
- REAUDIT v3 artifact (canonical 3.3/3.4 split): `tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`
- Cross-chapter rent-seeking workstream: [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)

---

*End of Ch 1 pipeline-retrofit handoff. PROPOSED 2026-05-17. Lightest retrofit in the set; fires **FIRST** of the 4 standardization-comparison-bed retrofits (Ch 1 → Ch 5 → Ch 6 → TA). Stage 4 verdict batch-ratifies post canonical-pipeline decision per [`render-pipeline-standardization-handoff_2026-05-17.md`](render-pipeline-standardization-handoff_2026-05-17.md).*
