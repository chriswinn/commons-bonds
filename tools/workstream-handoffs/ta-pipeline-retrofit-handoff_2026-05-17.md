# Tech Appendix Pipeline-Retrofit Handoff

**Date drafted:** 2026-05-17
**Branch prefix:** `claude/ta-pipeline-retrofit-`
**Artifact:** Technical Appendix (`core/technical-appendix/TechnicalAppendix_v2.0.0.html` — 8,038 lines; v2.1.0 dated 2026-05-14)
**Status going in:** Pass 1 math/proof audit RATIFIED + APPLIED via Phase C Tracks 1-5 (commits `0f62704` + `0af3ff1` + `d1410d9` + `eaf4c19` + `36073ca`). 2026-05-14 verification round ratified. Sandy-Darity-send-ready.
**Template:** [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
**Parent doctrine:** [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)

---

## §1. Retrofit scope

Per the retrofit table in [`README.md`](README.md): **1a + 1c + 3.4 + 4 (highest stakes math-content) + 5 (academic-rigor sign-off most consequential)**

| Sub-step | Fire? | Notes |
|---|---|---|
| 1a invariant gate | YES | Scan applies to HTML source (currently outside default registry scope; extend scope or scan via explicit --scope flag). Anticipated MEDIUM finds: F-13 "commons categorys" (RESOLVED by Scheme-4 cleanup commit `2c880bc`); LOW-severity Pass 2 typography items (F-11 log/ln; F-12 P-overload; F-14 seven-vs-ten dimensions; F-17 "existential substitutability gap" capitalization). |
| 1c coherence check | YES | Verify against Ch 5 + Ch 6 + Ch 9 cross-references (all use the framework apparatus the TA formally specifies); verify Darity-Mullen reparations-typology framing post-MI-1 + MI-2 incorporation; verify TA §5.5 bidirectional articulation alignment with Ch 5 §"Restitution and Foreclosure" + Ch 10 summary echo. |
| 3.1 verify | NO | Pass 1 math/proof audit RATIFIED + APPLIED across Phase C Tracks 1-5. Substantive findings (F-1 through F-19) all resolved. 2026-05-14 verification round (anchors B-1 through B-10) ratified. |
| 3.2 voice-polish | NO | Pass 2 typography sweep deferred per I-2 in 2026-05-14 verification round (F-11 + F-12 + F-14 + F-17 + cosmetic items; ~45 min total; not Sandy-blocking). Schedule as separate pre-publication refresh workstream. |
| 3.3 acceptance | NO | TA's primary audience is technical-rigor reviewer (Sandy + downstream); acceptance test is implicit in the Pass 1 + verification rounds. Pre-pub queue captures recommended external math + framework-methodology reviewers. |
| 3.4 robustness | YES — fresh | First Pass 3.4 robustness test on TA. Anticipate orthodox-econ + Chicago School + libertarian + industry-funded energy economist adversarial reads on the framework's central derivations (CS = RCV − B; the bidirectional decomposition; the substitution-dominance theorem; the four-gates apparatus; the Three Methods triangulation). |
| 4 render-integrity | YES — **HIGHEST STAKES IN THE CORPUS** | TA is the highest-math-content artifact; render-integrity audit is load-bearing. Verify: every formula renders correctly through HTML → PDF (Chrome headless preferred per cf24f57); Greek letters render (α covered in EB Garamond; verify Plane-1 chars like 𝒞 U+1D49E require fallback-header); ≈ renderings; minus-sign vs hyphen-minus in math contexts; sub/superscript HTML markup consistency (§3.5 mixed `<sub>` issue per F-11/F-12 punted items); table cell-integrity in §11.x deep-calibration blocks. Capture xelatex stderr for any `.md`-derived TA build path. |
| 5 sign-off + pre-pub queue | YES — **MOST CONSEQUENTIAL Stage 5 sign-off in the corpus** | Academic-rigor sign-off is the gating disposition here. Pre-pub review queue mandatory items: math reviewer (quantitative-economics / applied-math); framework-methodology reviewer (Stern-tradition / Hartwick-tradition / heterodox-econ); reparations-economics reviewer (Darity-Mullen-tradition successor; Darity already engaged per Sandy-packet); post-typesetter formula-integrity re-verification (the typesetter is the highest-risk pre-publication render step for TA specifically); F-7 cumulative oil/gas split exact-percentage refresh (per I-1 deferred item; ~15 min effort; CSV download from sodir.no). |

---

## §2. Prior cycle status

- Pass 1 math/proof audit: PROPOSED 2026-05-13 at commit `ab9fa22`; Amendment 2026-05-13 ratified (Approach B + Darity MI-1/MI-2 incorporation). All MUST-FIX + SHOULD-FIX findings (F-1 through F-19) resolved via Phase C Tracks 1-5:
  - Track 1 commit `0f62704`: Tier 1 spot-fixes (F-3, F-6, F-8, F-9, F-10, F-18, F-19)
  - Track 2 commit `0af3ff1`: Tier 2 spot-fixes (F-2 + Theorem 10.1b symmetric addendum)
  - Track 3 commit `d1410d9`: F-7 Norway gas-emissions Path A units correction
  - Track 4 commit `eaf4c19`: §11 calibration updates from verification round
  - Track 5 commit `36073ca`: bibliography expansion + v2.0.0 → v2.1.0 version bump
  - MEDIUM-11 cascade commit `45eb6e3`: coal-CO₂ short-ton-accounting (2.32 mt/short ton)
  - Post-publication refresh commit `aec033c`: Norway cumulative 8.9 + GPFG range refresh + Bayan Obo range refresh
- 2026-05-14 verification round (10 anchors B-1 through B-10): RATIFIED.
- Pass 2 typography sweep: NOT YET RUN. Deferred to pre-publication refresh (I-2 per verification round §I).
- Pass 3 audience-load: NOT YET RUN under v3.0 framing. Sandy-acceptance is implicit in Pass 1 + verification work; adversarial test is new.

---

## §3. Chapter-specific notes

- **Sandy interview completed 2026-05-13** + post-interview synthesis applied. Stage 1c verifies post-interview canonical framing holds.
- **CS = RCV − B canonical attribution.** TA §1.7 + §5 + §5.5 articulate the dual-form discipline (forward shorthand + full bidirectional). New paste-in errors that route "Per §3.1" → CS context get caught by registry entry `regressed-ta-cs-cross-reference-wrong-section`.
- **Plane-1 mathematical characters.** TA contains Plane-1 mathematical alphanumeric symbols (e.g., 𝒞 U+1D49E at 1 occurrence per current scan). Stage 4 audit must verify Chrome headless render (cf24f57); wkhtmltopdf would substitute .LastResort tofu glyphs.
- **F-7 working assumption (Norway 50/50 oil/gas cumulative split).** Pre-publication refresh I-1 item; ~15 min effort; resolved by CSV download from Norwegian Offshore Directorate. Magnitude impact: ~2% on cumulative emissions, within M1/M2/M3 method-range resolution.
- **External reviewer engagement post-Sandy.** Pre-pub queue should formally list recommended external math reviewer types per Sandy-already-engaged precedent. Per ratified decision #10: author self-signs Stage 5 + flags at handoff; college-tutors-as-bounded-bonus-capacity working arrangement.
- **Cross-chapter rent-seeking handoff.** TA is one of the touched artifacts in the cross-chapter rent-seeking-engagement workstream. Sequencing: prefer AFTER rent-seeking workstream touches land (rent-seeking analysis material may land in TA §5.5 or new section).
- **HTML source scope question.** Current YAML registry scope is markdown-only; TA is HTML. Either extend scope to include TA HTML source OR scan via `--scope` flag for retrofit only. PM session decides scope-extension decision before retrofit fires.

---

## §4. Cross-references

- Pipeline doctrine: [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)
- Retrofit template: [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
- TA Pass 1 math audit: `tools/rigor-passes/tech_appendix_rigor_pass_2026-05-13_pass_1_math_audit.md`
- TA verification round: `tools/rigor-passes/tech_appendix_verification_round_2026-05-14.md`
- TA §5.5 bidirectionality proposal: `tools/rigor-passes/ta_section_5_5_bidirectionality_proposal_2026-05-13.md`
- Cross-chapter rent-seeking workstream: [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)

---

*End of Tech Appendix pipeline-retrofit handoff. PROPOSED 2026-05-17. Highest math-content render stakes + most consequential Stage 5 sign-off in the corpus; sequence AFTER rent-seeking workstream + scope-extension decision.*
