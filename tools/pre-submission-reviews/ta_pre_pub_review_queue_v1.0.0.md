# Pre-Publication Review Queue — Technical Appendix

**Date generated:** 2026-05-18
**Status:** PROPOSED-DEFERRED — ratifies in batch with Stage 4 verdict after canonical-pipeline decision lands (per retrofit handoff stub §1 + standardization-handoff §3.5)
**Artifact:** Technical Appendix v2.1.0 (`core/technical-appendix/TechnicalAppendix_v2.0.0.html`; dated 2026-05-14; 8,044 lines)
**Stage 5 sign-off commit:** PENDING (Stage 5 sign-off itself deferred until Stage 4 verdict ratifies)
**Rendered outputs (current baseline):** `tools/scripts/comparison-renders/ta_2026-05-17_9ffad4e/remote-container/TechnicalAppendix_v2.0.0.{docx,pdf}` (rendered 2026-05-17 against `9ffad4e`; laptop renders captured at this session per [`tools/rigor-passes/render_pipeline_comparison_ta_2026-05-18.md`](../rigor-passes/render_pipeline_comparison_ta_2026-05-18.md))
**Sandy-packet artifacts (canonical-shipped):** `research/outreach/subjects/darity/Technical_Appendix_Commons_Bonds_2026-05-14.{docx,pdf}` (rendered via remote-container at commit `e6ddf92` 2026-05-14; clean prior to Ch 1 in-session patch)
**Manuscript-submission package context:** for-publisher / for-agent / for-editor (TA is the formal-academic-register apparatus; pre-pub queue is **most consequential in the corpus** per handoff stub §1 row 5)

---

## §1. What has been internally verified

### §1.1 Factual verification

Per TA Pass 1 math/proof audit (PROPOSED `ab9fa22` 2026-05-13; Amendment 2026-05-13 RATIFIED; all MUST-FIX + SHOULD-FIX findings F-1 through F-19 APPLIED via Phase C Tracks 1-5: commits `0f62704` + `0af3ff1` + `d1410d9` + `eaf4c19` + `36073ca`; MEDIUM-11 cascade `45eb6e3`; refresh `aec033c`) + 2026-05-14 verification round (10 anchors B-1 through B-10; RATIFIED):

- **Norway petroleum + production anchors (§11.5):**
  - 8.9 billion Sm³ o.e. cumulative production through 2024 — verified per Norwegian Offshore Directorate / norskpetroleum.no (anchor B-1).
  - 56–57% of 15.6 billion Sm³ o.e. recoverable resources produced — verified per norskpetroleum.no resource-accounts (B-1).
  - 0.43 t CO₂/barrel oil; 0.31 t CO₂/BOE-equivalent natural gas (Path A units correction per F-7) — verified per EPA emission factors / EIA / IPCC AR6 (B-4 + B-5; D-2 derivation in verification round).
  - F-7 50/50 oil/gas cumulative split — **defensibly bounded** per verification round §C qualitative-evidence catalog; exact-percentage hardening (~15 min CSV download from sodir.no) deferred to pre-publication refresh per I-1.
  - ~20.35 billion tons CO₂ cumulative emissions (mixed oil/gas weighted) — derived figure per F-7 working assumption.
  - 70–80% Norwegian-state capture rate of net petroleum wealth — autobiographical/historical-record framework figure.
- **GPFG / Norway sovereign wealth fund anchors (§11.5):**
  - $2.0T end-2025 fund value (21,268 billion NOK); $2.2T April 2025 peak — verified per NBIM (anchor B-2).
  - $356K–$391K per-Norwegian-citizen share at population 5.62M per Statistics Norway 2025 (range refresh per B-3; D-1 derivation in verification round).
- **Coal CO₂ emission factor (§11.6):**
  - 2.32 mt CO₂/short ton bituminous coal — verified per EPA AP-42 §1.1 + EIA short-ton-accounting (B-7; D-3 derivation; MEDIUM-11 cascade applied commit `45eb6e3`).
- **Black Lung Disability Trust Fund (§11.6):**
  - ~$44 billion cumulative payouts; $5.1B outstanding debt September 2024 — verified per CRS R45261 + DOL OWCP / industry-press (B-8).
- **Rare-earth anchors (§11.4):**
  - China 69.2% of global REE mine production 2024 — verified per USGS *Mineral Commodity Summaries 2025* (B-9).
  - Bayan Obo ~37–40% of global REE reserves (range refresh per B-10; USGS-derivable 39%; published-estimate range 30–40+%); D-4 derivation in verification round.
- **External citations (§14 literature engagement + §18 bibliography):**
  - Hotelling 1931; Hartwick 1977; Solow 1974; Coase 1960; Pigou 1920; Ostrom 1990; Weitzman 2001; Brennan & Schwartz 1985; Dixit & Pindyck 1994; Parfit 1984; Savage 1951; Loomes & Sugden 1982; Lempert / Popper / Bankes 2003 — all verified per Pass 1 §6 external-citation-accuracy verification; no misrepresentations surfaced.
  - Darity & Mullen 2020 *From Here to Equality* — verified per Pass 1 Amendment 2026-05-13 + Sandy interview ratification 2026-05-13.
  - Hamilton, Darity, Price, Sridharan, Tippett 2015 *Umbrellas Don't Make It Rain* — verified per bibliography expansion commit `36073ca`.

**TA Pass 1 math/proof audit verdict:** all 19 findings (F-1 through F-19) APPLIED via Phase C Tracks 1-5 + Track 2 Theorem 10.1b symmetric addendum. Math academic-rigor APPLIED.

**TA verification round verdict:** 10 anchors B-1 through B-10 RATIFIED with 2 small calibration refreshes applied via `aec033c` (Norway cumulative 8.7→8.9 Sm³; per-citizen share $356K–$391K range; Bayan Obo 37→37–40%). Six judgment-call ratifications (R-1 through R-6) ACCEPTED 2026-05-14.

### §1.2 Math / framework verification

- **Canonical-formula inventory** internally verified:
  - Central equation `CS = RCV − B` (forward shorthand per §1.7) + `total CS = (CSD − B₁) + (RCV − B₂)` (full bidirectional articulation per §5 + §5.5) — coexist as different-scope statements per Pass 1 Amendment 2026-05-13 (Approach B ratification).
  - RCV integrand as discounted integral of sum-of-costs (§3 + §17.6 generalization).
  - Hotelling Identity (§4) as extension of Hotelling 1931 rent-path rule.
  - Two-instrument architecture B = B₁ + B₂ (§5) — B₁ Restitution Bond (backward-looking; Darity-Mullen reparations-typology positioning per §5.1.1 MI-1 incorporation); B₂ Foreclosure Bond (forward-looking; Parfit 1984 intergenerational moral grounding per §5.4).
- **Theorem inventory** internally verified:
  - Theorem 10.1a (Cost Severance Identity) — proof valid per Pass 1 §3.
  - Theorem 10.1b (Structural Cost Severance under Current Institutions) — proof valid per Pass 1 §3; symmetric-application addendum APPLIED per Track 2 commit `0af3ff1`.
  - Empirical Observation 10.2 (Cross-Model Convergence) — correctly self-categorized as observation rather than theorem.
  - Theorem 10.3 (Abundance Masking) — proof valid; F-8 statement-vs-proof bridge APPLIED.
  - Theorem 10.4 (RCV Integral Convergence; SC1 + SC2 + knife-edge corollary) — F-10 LDC simplification APPLIED; F-18 knife-edge corollary hypothesis-strengthening APPLIED (commit `0f62704`).
  - Theorem 10.5 (Substitution Dominance) — F-2 P1 RCV-vs-CS equivocation cleanup APPLIED per Track 2 commit `0af3ff1`.
  - Corollary 10.5.1 (Optimal Extraction Sequencing) — follows from Theorem 10.5 post-F-2 cleanup.
- **Numerical-example verification** per Pass 1 §5:
  - §11.5 Norway Method 3 mid-range ($281/BOE), low ($72), high ($1,016) — arithmetic verified.
  - §11.6 McDowell Method 3 mid-range ($2,580/ton) — arithmetic verified.
  - §11.6 McDowell Method 1 — F-6 DAC-range label vs band mismatch APPLIED.
  - §11.5 Norway cumulative emissions — F-7 oil-vs-gas factor APPLIED (Path A units correction; 50/50 working assumption for cumulative split).
- **Derivation-chain integrity** verified by author + Pass 1 + verification round + Stage 4 formula-integrity audit:
  - All theorem statements + proofs verified valid as derived.
  - Theorem 10.5 substitution-dominance algebra cleaned per F-2.
  - §16.3 Spatial Cost Severance formula restated per F-19 (now uses consumption-region letter K with R-2 ratification).

### §1.3 Cross-artifact coherence

Per Stage 1c coherence-check verdict ([`tools/quality-gates/coherence-checks/ta_stage1c_2026-05-18.md`](../quality-gates/coherence-checks/ta_stage1c_2026-05-18.md) — COHERENCE VERIFIED):

- **Bibliography commitments touching scope:** ~72 entries with TA / methodology-appendix relevance; 13 load-bearing flagship entries inventoried; all REALIZED in TA prose. 1 MEDIUM-FLAG (bibliography line 519 Mazzucato Ch 1 staleness; bibliography-side spot-fix, not TA-side).
- **AuthorsNote framings:** 0 TA-direct commitments. No coherence verification needed.
- **Sibling-chapter cross-references:** 22 TA-direct cross-references across Ch 5 + Ch 6 + Ch 7 + Ch 8 + Ch 10; all 22 REALIZED. Every cited TA anchor resolves to a real section.
- **Prior rigor-pass artifacts:** Pass 1 (RATIFIED + APPLIED) + verification round (RATIFIED + APPLIED via refresh commit) + §5.5 bidirectionality proposal (SUPERSEDED by parallel-session work) + Pass 2 typography sweep (DEFERRED per I-2) + Pass 3 acceptance (DEFERRED per I-3) — all REALIZED or appropriately DEFERRED.
- **Cross-chapter consistency-inventory items:** 9 inventoried; 8 REALIZED; 1 stale name-drift (Theorem E.3 → 10.3 in inventory line 42; inventory-side spot-fix, not TA-side).

### §1.4 Audience-load verification

- **Pass 3.3 audience-load acceptance verdict:** NOT FIRED FRESH per handoff stub §1 row 3.3 — *"TA's primary audience is technical-rigor reviewer (Sandy + downstream); acceptance test is implicit in the Pass 1 + verification rounds."* Pre-pub queue captures recommended external math + framework-methodology reviewers as the structural acceptance-test handoff.
- **Pass 3.4 audience-load robustness verdict (this session):** **CONDITIONALLY ROBUST** per [`tools/rigor-passes/ta_stage3_pass_3_4_audience_load_robustness_2026-05-18.md`](../rigor-passes/ta_stage3_pass_3_4_audience_load_robustness_2026-05-18.md). 10-character adversarial set: industry-funded energy + pharma; Chicago orthodox-econ; Public Choice theorist; libertarian/Rothbardian; reparations-economics methodological-skeptic; tort-reform / corporate-fiduciary lawyer; technical-rigor skeptic; reactionary intellectual technical-reader; WSJ editorial-board. Aggregate: 10/10 EXCLUDE (expected; adversarial verdict-floor is EXCLUDE). Thread-pull synthesis: 9 threads classified (6 load-bearing-chapter-claims + 2 procedural/cosmetic + 1 by-design-scope-boundary). **Amendment 2026-05-18:** Pass 3.4 artifact §A Amendment corrects an original-framing error — the cross-chapter rent-seeking-engagement workstream is RATIFIED 2026-05-18 (commit `bc02767`) with substantive material APPLIED via commit `a1e54d9` to TA §1.10 lines 606–611 + Ch 5 line 184 + Ch 9 line 133 + Ch 8 line 123. Σ1 (T4 Public Choice thread) is **load-bearing-with-disposition** (not chapter-disqualifying); T4 per-character verdict ⚠⚠⚠ → ⚠⚠. Residual extension opportunity at §5 Accountability Bond architecture + §15.1 limitations (bond-design-rent-seeking-vulnerability engagement) is procedural / extension-opportunity, not chapter-blocking. CONDITIONALLY ROBUST verdict preserved under strict verdict-scale reading (Σ2-Σ6 + Σ9 remain common load-bearing threads independent of Σ1).

### §1.5 Render integrity

- **Stage 4 render-integrity audit verdict:** PROPOSED-pending-canonical-pipeline-decision per [`tools/rigor-passes/render_pipeline_comparison_ta_2026-05-18.md`](../rigor-passes/render_pipeline_comparison_ta_2026-05-18.md). Triple-render summary:
  - **remote-container baseline (BASE `9ffad4e`):** wkhtmltopdf 0.12.6 (Qt 5.15.13); 129,517-byte DOCX (5,802-line pandoc-plain extraction); 613,750-byte PDF; 91 pages. Plane-1 char `𝒞` U+1D49E **fails to render** (substituted; absent from pdftotext extract).
  - **laptop-build-derivatives:** Chrome headless 148.0; 123,201-byte DOCX (5,339-line plain extraction; **−463 lines vs baseline, −8.0%**); 1,564,871-byte PDF; 97 pages. **Plane-1 char `𝒞` RENDERS CORRECTLY** (only pipeline that does). 2 unclosed-div + 5 "Could not convert TeX math" pandoc warnings.
  - **laptop-build-derivatives-alt:** wkhtmltopdf 0.12.6 (Qt 4.8.7 Homebrew macOS); 123,201-byte DOCX (5,339-line plain extraction; identical content to build-derivatives docx); 584,948-byte PDF; 100 pages. Plane-1 char `𝒞` fails (U+FFFD in pdftotext extract). Same 2+5 pandoc warnings.
  - **HIGH-severity finding F-RP-TA-01:** both laptop scripts' docx output contains raw HTML tags + entities echoed as literal text (Ch 1 in-session patch's unconditional `--from=markdown-yaml_metadata_block` applies to HTML input incorrectly). One-line script-fix recommended (conditional-on-input-extension); DEFERRED to canonical-pipeline decision step per "do NOT tune pipeline mid-comparison" discipline.
  - **HIGH-severity finding F-RP-TA-02:** Plane-1 char `𝒞` renders correctly ONLY via Chrome HTML→PDF; both wkhtmltopdf paths (baseline + laptop -alt) fail per `cf24f57` doctrine §3.3 prediction. Rules out wkhtmltopdf as canonical for HTML→PDF.
  - **MEDIUM findings:** F-RP-TA-03 (laptop wkhtmltopdf Qt 4.8.7 vs baseline Qt 5.15.13 page-count drift); F-RP-TA-04 (TA HTML source unclosed-div at lines 175 + 1823; Pass 2 typography candidate).
  - **Canonical-pipeline recommendation (per Stage 4 §10):** Option A (tune laptop) with F-RP-TA-01 fix applied; merge build-derivatives.sh + build-derivatives-alt.sh per Stage 4 §8.2. **The baseline pipeline is INFERIOR for HTML→PDF** (Plane-1 char failure); re-baseline against laptop-Chrome going forward.

---

## §2. What has NOT been externally verified

### §2.1 Factual claims that would benefit from external corroboration

- **F-7 Norway cumulative oil/gas split — exact-percentage hardening.** Current TA v2.1.0 carries 50/50 working assumption per §11.5 anchor table + F-7 weighted-factor calc + cumulative-emissions cell. Defensibility bounded per 2026-05-14 verification round §C qualitative-evidence catalog (gas ~51.5% 2024 annual; gas ~50% 2025 annual; "more gas than oil" over last decade; "1985–2005 oil dominant"). Magnitude impact of plausible refinement: ~2% on cumulative emissions, well within M1/M2/M3 method-range resolution. **Hardening path:** download Norwegian Offshore Directorate production-figures CSV from sodir.no; compute exact cumulative percentage; update §11.5 anchor + F-7 weighted-factor + cumulative-emissions cell. Estimated effort: ~15 min. **Disposition:** apply at pre-publication refresh regardless of external probe (carry-forward I-1 from 2026-05-14 verification round).

- **§11.x deep-calibration block-by-block external verification.** All 10 anchors (B-1 through B-10) internally verified via 2026-05-14 verification round against primary public sources. **Not cross-verified by independent external economist** (Norwegian Offshore Directorate primary-source readings; USGS / EPA / EIA / DOL / NBIM official-data readings — each verified once via web-search of source documents during the verification round). External-reviewer scope: any anchor-by-anchor re-verification by an independent economist would add a second-pair-of-eyes layer to the source-of-record verification. LOW priority for argumentative load (anchors are not the framework's load-bearing analytical claims; they're empirical calibration); MEDIUM priority for transparency / source-of-record fidelity.

- **§10 theorem proofs.** All proofs internally verified per Pass 1 math/proof audit (Theorem 10.1a + 10.1b + 10.3 + 10.4 SC1/SC2/knife-edge + 10.5 + Corollary 10.5.1 + §17.5 directional-monotonicity + §17.5 bidirectional preservation corollary). **Not externally verified by an academic quantitative-economics referee.** Pass 1 internal audit caught real findings (F-2 P1 equivocation; F-18 knife-edge corollary hypothesis gap); all applied. External referee would test the proofs against journal-publication-standard rigor (e.g., JPE / QJE / Journal of Economic Theory referee standards). **HIGH priority for academic-publication readiness** (the TA's load-bearing claims rest on the theorems being publication-grade).

- **Darity-Mullen reparations-typology extension to broader case-class (§5.1.1 + §5.5).** Internally verified via Darity interview 2026-05-13 + Sandy ratification of MI-1 + MI-2 positioning + Pass 1 Amendment 2026-05-13 Approach B ratification. **Not externally verified by a Darity-Mullen-tradition successor outside Darity himself.** Sandy/Darity engagement (1–2 week TA + Ch 6 read commitment as of Sandy packet ship 2026-05-14) is the structural disposition for this concern. Pre-pub queue flag: additional Darity-Mullen-tradition successor reviewer (Hamilton; Price; Sridharan; Tippett; Anderson; Coates-cluster economic-theorist) would extend the deference-posture verification beyond Darity's single-source ratification.

- **§16.3 Spatial Cost Severance formula choice of consumption-region letter K** (per F-19 restatement + R-2 ratification). Internally verified per Pass 1 Amendment 2026-05-13. **Not externally verified against literature-conventional notation** (literature uses Ω, S, D for spatial-region letters; K is the framework-specific choice). MEDIUM priority for typography-clarity; flagged for Pass 2 typography sweep.

### §2.2 Math / framework claims that would benefit from external technical review

- **Derivation-chain claims (theorems 10.1a/b + 10.3 + 10.4 + 10.5 + corollaries + §17 generalization + §16.3 SCS):** **recommend external math reviewer with quantitative-economics / applied-mathematics background.** Specific scope per Pass 1 audit §1-§8: definition well-formedness; derivation correctness; theorem proof validity; corollary derivability; numerical-example arithmetic; external-citation accuracy; cross-reference resolution; notation consistency. Math reviewer should test the framework against journal-publication-standard rigor.

- **Framework-methodology claims:**
  - **CS = RCV − B / total CS = (CSD − B₁) + (RCV − B₂) two-form discipline (§1.7 + §5):** recommend framework-methodology reviewer in adjacent tradition (Stern-tradition / Hartwick-tradition / heterodox-econ / resource-econ). Specific concern: does the forward-shorthand-vs-full-bidirectional dual-form discipline read as methodologically sound vs. as obscuring a single canonical form?
  - **Four Gates apparatus (§7):** recommend framework-methodology reviewer (institutional-econ / Ostrom-successor). Specific concern: does the CIT-Units-Boundedness-Independence gate filter read as analytically rigorous filtering vs. as a control mechanism for excluding inconvenient cost terms?
  - **Three Methods triangulation (§3.3 + §3.4 + §3.5):** recommend framework-methodology reviewer (resource-econ / Dixit-Pindyck-tradition real-options successor; Norway GPFG empirical-validation specialist). Specific concern: does the Replacement Cost + Revealed Preference + Scarcity-Adjusted Option Value triangulation read as sound methodology vs. as one-of-three-arbitrary-choices that anchors to a desired range?
  - **Substitution Dominance theorem (§10.5):** recommend math reviewer + framework-methodology reviewer jointly. Specific concern: the welfare-comparison algebra is technically correct under stated premises; the premises (RCV > P; Investment_cost ≤ P) are non-trivial empirical claims that the case-library validates; the theorem's *application* range needs reviewer verification.
  - **§5.5 bidirectional articulation:** recommend reparations-economics reviewer (Darity-Mullen-tradition successor; Hamilton; Anderson). Specific concern: does the "structurally identical methodology" framework-claim land as analytically sound vs. as overreaching application of reparations-economics methods?

- **Render-integrity post-typesetter:** **the typesetter is the highest-risk pre-publication render step for TA specifically.** Per Stage 4 F-RP-TA-02: wkhtmltopdf-based PDF conversion (the publisher's typesetter may or may not use this engine) fails the Plane-1 char `𝒞` U+1D49E test at §1.1 commons-territory-set definition. Recommend: **post-typesetter formula-integrity re-verification** by a math reviewer or by an automated character-fidelity check. Specific failure modes to test:
  - Plane-1 mathematical alphanumeric symbols (`𝒞` U+1D49E; broader U+1D400-U+1D7FF range if any).
  - Inline math `$…$` spans (engine-specific handling).
  - Subscripts / superscripts via `<sub>` / `<sup>` (HTML-source) or `_` / `^` (markdown-source).
  - Greek-letter character coverage (α, β, γ, σ, ε, Σ, μ — all critical for TA prose).
  - Em-dash `—` U+2014 (broader corpus issue per `d238f2c` Ch 5 + Ch 6 fix history; less critical for TA where em-dashes are not in bold spans).
  - Approximation symbol `≈` U+2248 (verified 62 occurrences via `&asymp;` entity; render-tested at this Stage 4).
  - Minus sign `−` U+2212 (verified ~85-103 occurrences via `&minus;` entity).

### §2.3 Audience-coverage gaps (per Pass 3.4 thread-pull synthesis)

- **Σ1 Public Choice rent-seeking complementarity (§5 Accountability Bond architecture; corrected per Pass 3.4 §A Amendment):** TA §1.10 lines 606–611 carries the framework's Public Choice complementarity engagement — cites Buchanan & Tullock 1962, Tullock 1967, Mueller 2003; articulates framework's scope (cost-bearing-party identification + magnitude) vs Public Choice's scope (rent-seeking-actor identification); specifies applicability conditions (sharpest / blurred / out-of-scope); tells Public Choice readers how to engage the framework. Material applied via commit `a1e54d9` + cross-chapter rent-seeking-engagement workstream RATIFIED 2026-05-18 (`bc02767`). Pre-pub queue flag for external Public-Choice-tradition reviewer (technical-economics + Virginia-School-tradition affiliation; Mercatus / GMU cluster or similar) to (a) verify the §1.10 complementarity engagement reads as substantive, and (b) advise on whether §5 Accountability Bond architecture + §15.1 limitations should be extended at a future session with bond-design-rent-seeking-vulnerability engagement (author discretion; not chapter-blocking).

- **Σ2 §10.5 substitution-dominance theorem premises:** RCV > P + Investment_cost ≤ P premises are non-trivial empirical claims tested against the case-library (§11). Pre-pub queue flag for external math + framework-methodology reviewers to engage the premises empirically.

- **Σ3 §11 case-library framing (Norway as existence-proof; McDowell as failure-case):** the juxtaposition is the framework's load-bearing empirical claim. Pre-pub queue flag for external policy-economics reviewer (framework-vs-finding verification — does the framing read as analytical finding rather than as policy-conclusion-presupposed?).

- **Σ4 §1.10 ten-commons-categories taxonomy:** the Option C' (commons-as-examples) modesty + the ten-commons enumeration are intentionally framed per §15.1.6. Pre-pub queue flag for external framework-methodology reviewer in adjacent tradition (Ostrom-successor / Hartwick / heterodox-econ) to verify the Option C' framing is methodologically coherent.

- **Σ5 §5.1.1 + §5.5 + §1.10 reparations-economics-positioning depth:** Darity-Mullen extension to broader case-class is asserted methodologically. Sandy/Darity engagement in flight; additional Darity-Mullen-tradition successor reviewer flagged in §3.2 below.

- **Σ6 §10.5 + §5.5 + §11 litigation-architecture concern:** the apparatus is technically rigorous which is the precise tort-defense concern; expected at publication time + flagged for legal-adversarial context-awareness.

- **Σ9 §5.5 backward-application empirical deferral:** by-design scope-boundary. Pre-pub queue flag for external reparations-economics reviewer (deference-posture verification).

---

## §3. Recommended external reviewer types

### §3.1 Math reviewer (HIGHEST PRIORITY for TA specifically)

**Profile:** Technical reviewer with quantitative-economics / applied-mathematics background. Specifically: PhD economist or applied mathematician with publication record in journal-of-economic-theory tradition; familiarity with Lebesgue integration, real-options theory, Hotelling rent-rules, intergenerational discount-rate literature.

**Scope of review:** every theorem statement + proof (10.1a, 10.1b, 10.3, 10.4 SC1/SC2/knife-edge, 10.5 + Corollary 10.5.1, §17.5 directional-monotonicity, §17.5 bidirectional preservation); every derivation in §3 + §4 + §10 + §17; every numerical-example arithmetic in §11.x. **For TA specifically: also flag formula-integrity post-typesetter** per F-RP-TA-02.

**What to look for:**
- Derivation-chain correctness at journal-publication-standard rigor.
- Notation conventions consistency (subscripts, superscripts, integral bounds, summation indices).
- Inline-vs-display math rendering integrity.
- Formula-integrity post-typesetter (Plane-1 chars + Greek letters + minus signs + em-dashes).
- F-7 50/50 Norway oil/gas working assumption — verify defensibility holds against published exact-percentage data (post-CSV-download).
- §10.5 substitution-dominance premises — verify RCV > P + Investment_cost ≤ P are non-trivial empirical claims testable against §11 case library.
- §10.4 knife-edge corollary — verify hypothesis-strengthening (per F-18 application) closes the proof-gap (slow-decaying r case).

### §3.2 Framework-methodology reviewer (HIGHEST PRIORITY)

**Profile:** Economist in an adjacent tradition. Specifically:
- **Heterodox-econ:** Stone Center / Levy Institute / JFI / IIPP network successor — for framework-positioning against heterodox-econ tradition.
- **Stern-tradition:** quantitative-climate-economics reviewer familiar with Stern Review discount-rate framing — for §3 RCV / §10.4 integral convergence / §16.1 declining-rate discount.
- **Hartwick-tradition:** resource-economist familiar with Hartwick 1977 + Solow 1974 — for §4 Hotelling + §5 two-instrument + §14 lineage.
- **Ostrom-successor:** institutional-econ familiar with commons governance literature — for §6 CIT + §1.10 ten-commons + §6.6 coordination-vs-extraction-commons + §1.10-second-paragraph heterogeneous-stakeholder-commons scope.
- **Dixit-Pindyck-tradition:** real-options-successor familiar with investment-under-uncertainty framework — for §3.5 Method 3 + §15.1.5 two-instrument-architecture rationale.

**Scope of review:** framework-methodology claims throughout TA; lineage-handling at §14; methodological soundness vs adjacent traditions; defensibility against Pass 3.4 adversarial threads documented in §2.3 above.

**What to look for:**
- Methodological soundness vs adjacent traditions.
- Lineage attribution clarity at §14.
- Framework-claim defensibility (specifically against Public-Choice + Chicago-orthodox + libertarian adversarial reads).
- §15.1 limitations section completeness (the Pass 3.4 finding that §15.1 does not engage Public-Choice critique).
- Option C' (commons-as-examples) framing methodological coherence (§15.1.6).

### §3.3 Reparations-economics reviewer (HIGHEST PRIORITY; Sandy/Darity already engaged)

**Profile:** Darity-Mullen-tradition successor. Specifically:
- **William Darity Jr.** himself (engagement in flight per Sandy packet 2026-05-14 ship + 1–2 week TA + Ch 6 read commitment).
- **Additional Darity-Mullen-tradition successors** for second-pair-of-eyes layer:
  - **A. Kirsten Mullen** (co-author *From Here to Equality*).
  - **Darrick Hamilton** (co-author *Umbrellas Don't Make It Rain*; New School / Bootstrap Cooperative).
  - **Anne E. Price** (Insight Center for Community Economic Development).
  - **Khaing Zaw Sridharan + Jhumpa Bhattacharya + Wendy Tippett** (per *Umbrellas Don't Make It Rain* + *Bootstrap-style* methodology).
  - **Elizabeth Anderson** (philosopher; *Private Government*; intersection with §1.10 Autonomy commons).
  - **Ta-Nehisi Coates** (rhetorical-companion-tradition per §5.1.1 + §14 lineage).

**Scope of review:** §5.1.1 Restitution Bond Darity-Mullen positioning; §1.10 Autonomy commons coercion-vector scope-of-applicability boundary; §5.5 bidirectional articulation + backward-application; §10.5 substitution-dominance theorem applied to reparations-economics case-class; §14 reparations-economics lineage; bibliography expansion (commit `36073ca`) covering Darity-Mullen-tradition entries.

**What to look for:**
- Does §5.1.1's "operationalizing the restitution-as-redress component within Darity-Mullen's reparations framework, extended to the broader case-class" land authentically vs as appropriation?
- Does §1.10 coercion-vector single-source attribution (Darity 2026) hold as methodologically sufficient vs. require broader reparations-economics-field engagement?
- Does §5.5 "structurally identical methodology" claim read as analytically sound vs. as overreach?
- Does §14 lineage attribution properly credit the reparations-economics tradition the framework extends?

### §3.4 Public-Choice-tradition reviewer (NEW; surfaced from Pass 3.4)

**Profile:** Public Choice theorist in Buchanan/Tullock / Virginia-School tradition. Specifically: PhD economist with publication record in Public Choice / Constitutional Political Economy / institutional-rent-seeking literature; affiliation with Mercatus Center / GMU economics / Cato / Public Choice Society.

**Scope of review:** TA §1.10 Public Choice complementarity paragraph (lines 606–611; landed `a1e54d9` → ratified `bc02767`); cross-chapter material at Ch 5 line 184 + Ch 9 line 133 + Ch 8 line 123; framework-vs-Public-Choice scope articulation across the corpus.

**What to look for:**
- Does §1.10 Public Choice complementarity paragraph read as substantive engagement (lineage citations + applicability conditions + scope clarity) vs cursory reference?
- Does the framework's "Readers in the Public Choice tradition should read the framework's cost-bearing-party identification as a foundation their apparatus can apply to, not as an alternative to their apparatus" framing land authentically with Public-Choice tradition readers?
- Are the applicability conditions (sharpest / blurred / out-of-scope) correctly drawn?
- **Open question for reviewer judgment:** should TA §5 Accountability Bond architecture and/or §15.1 limitations be extended at a future session to carry bond-design-rent-seeking-vulnerability engagement at instrument-design level (beyond the §1.10 scope-level engagement already present)? This is the residual Pass 3.4 thread Σ1 extension opportunity — author discretion, not chapter-blocking.

### §3.5 Post-typesetter formula-integrity re-verification

**Profile:** technical reviewer with character-fidelity-test responsibility. Could be: (a) the math reviewer (§3.1) executing a post-typesetter pass; (b) an automated character-fidelity check (e.g., `pdftotext` extraction + character-class diff vs HTML source); (c) the typesetter's own pre-publication QA process.

**Scope of review:** post-typesetter TA artifact (whichever rendered form the publisher's typesetter produces). Specific failure-mode tests:
- Plane-1 mathematical alphanumeric symbols rendered correctly.
- Greek letters rendered correctly (no character-substitution).
- Inline + display math rendering integrity.
- Em-dash + en-dash + minus sign distinction preserved.
- `&` entity decoding (TA HTML source uses extensive HTML entities; typesetter MUST decode correctly).

**What to look for:** any character drift between pre-typeset HTML source (or pre-typeset markdown) and post-typesetter rendered artifact. **HIGH priority because TA carries the framework's load-bearing analytical apparatus — any character corruption at typesetting time would damage the framework's formal claims.**

### §3.6 Domain expert(s) for TA specifically

**Norway petroleum-economics specialist** (e.g., Norwegian Statistics economist; Norwegian Offshore Directorate technical staff; NBIM economist) — for §11.5 anchor verification + F-7 cumulative oil/gas split hardening + GPFG capture-rate verification.

**McDowell County coal-economics historian** (e.g., West Virginia Mining and Reclamation Association historian; Coal Authority historian) — for §11.6 anchor verification (coal CO₂ + Black Lung Trust Fund + DAC band ranges).

**Rare-earth mining specialist** (e.g., USGS Mineral Resources Program economist; CTIA China rare-earth analyst) — for §11.4 anchor verification (Bayan Obo share; China REE production share).

**Climate-economics + DAC-cost specialist** (e.g., Climeworks economist; Stripe Climate technical staff; IEA DAC analyst) — for §3.3 DAC band specifications + §11.6 DAC-band-vs-coal-cost arithmetic.

---

## §4. Highest-priority sections for external review if publisher budget is limited

Per author preference, rank-ordered for TA specifically:

1. **§10 theorem proofs (Theorems 10.1a, 10.1b, 10.3, 10.4 SC1+SC2+knife-edge, 10.5 + Corollary 10.5.1) + §17.5 corollaries.** Rationale: TA's load-bearing claims rest on these theorems. The framework's external-academic-acceptability depends on the proofs holding at journal-publication-standard rigor. Math reviewer's verdict here is the most consequential single external check for TA. (Pass 1 internal audit already caught real findings — F-2 + F-18 — and applied fixes; external referee tests at the next-stricter-level.)

2. **§5.1.1 + §5.5 + §1.10 reparations-economics-positioning.** Rationale: the framework's deference posture to Darity-Mullen reparations methodology is methodologically load-bearing. Sandy/Darity engagement (in flight) is the structural first-pair-of-eyes; additional Darity-Mullen-tradition reviewer adds robustness to the deference-posture verification.

3. **§3 RCV quantification + §3.3-3.5 Three Methods (Replacement Cost + Revealed Preference + Scarcity-Adjusted Option Value) + §11.x case-library calibration.** Rationale: the framework's empirical-validation work rests on the Three Methods triangulation applied across the case library. Framework-methodology reviewer in resource-econ / Dixit-Pindyck-tradition tests the triangulation's analytical soundness; domain experts (Norway / McDowell / Baotou) verify the calibration anchors.

4. **§7 Four Gates + §6 CIT + §1.10 ten commons categories.** Rationale: the framework's methodological apparatus rests on the Four Gates filter + CIT discovery methodology. Framework-methodology reviewer in Ostrom-successor / institutional-econ tradition tests the apparatus against adjacent commons-governance traditions.

5. **§5 Accountability Bond architecture (post cross-chapter rent-seeking-engagement workstream landing).** Rationale: the cross-chapter workstream surfaces the framework's institutional-political-economy work. Public-Choice-tradition reviewer tests the post-workstream §5 material.

6. **§14 literature engagement + §18 bibliography.** Rationale: the framework's lineage-handling is a methodological claim about intellectual honesty. Framework-methodology reviewers across multiple traditions (Stern + Hartwick + Ostrom-successor + Dixit-Pindyck) verify the lineage attribution accuracy.

7. **Post-typesetter formula-integrity re-verification.** Rationale: the typesetter is the highest-risk pre-publication render step for TA per Stage 4 F-RP-TA-02. Even if all other reviews pass, a typesetter that uses a wkhtmltopdf-class engine would silently corrupt the Plane-1 char `𝒞`.

---

## §5. Cross-references

- Stage 1b brief: N/A — retrofit mode (no Stage 1b brief artifact; existing TA prose serves as canonical reference per Stage 1 doctrine §5).
- Stage 1c coherence-check: [`tools/quality-gates/coherence-checks/ta_stage1c_2026-05-18.md`](../quality-gates/coherence-checks/ta_stage1c_2026-05-18.md)
- Stage 1a clean-baseline: [`tools/quality-gates/clean-baselines/ta_stage1a_2026-05-18.md`](../quality-gates/clean-baselines/ta_stage1a_2026-05-18.md)
- Pass 1 math/proof audit: [`tools/rigor-passes/tech_appendix_rigor_pass_2026-05-13_pass_1_math_audit.md`](../rigor-passes/tech_appendix_rigor_pass_2026-05-13_pass_1_math_audit.md)
- 2026-05-14 verification round: [`tools/rigor-passes/tech_appendix_verification_round_2026-05-14.md`](../rigor-passes/tech_appendix_verification_round_2026-05-14.md)
- §5.5 bidirectionality proposal (superseded by parallel-session work): [`tools/rigor-passes/ta_section_5_5_bidirectionality_proposal_2026-05-13.md`](../rigor-passes/ta_section_5_5_bidirectionality_proposal_2026-05-13.md)
- Pass 3.4 audience-load robustness (this session): [`tools/rigor-passes/ta_stage3_pass_3_4_audience_load_robustness_2026-05-18.md`](../rigor-passes/ta_stage3_pass_3_4_audience_load_robustness_2026-05-18.md)
- Stage 4 render-integrity audit (PROPOSED-pending-canonical-pipeline-decision): [`tools/rigor-passes/render_pipeline_comparison_ta_2026-05-18.md`](../rigor-passes/render_pipeline_comparison_ta_2026-05-18.md)
- Stage 5 sign-off: PENDING (deferred until Stage 4 verdict ratifies)
- Cross-chapter workstream touching scope: [`tools/workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](../workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md) (rent-seeking-engagement workstream — substantive engagement lands in TA §5.5 or new section per workstream §0 framing)
- Sandy-Darity packet: `research/outreach/subjects/darity/Technical_Appendix_Commons_Bonds_2026-05-14.{docx,pdf}` (clean baseline; rendered before Ch 1 in-session patch)

---

## §6. PROPOSED-DEFERRED status — what locks in vs what stays open

**LOCKED IN as of this PROPOSED-DEFERRED draft (will not change at ratification):**
- §1.1 factual verification list (per Pass 1 RATIFIED + APPLIED + 2026-05-14 verification round RATIFIED).
- §1.2 math / framework verification list (per Pass 1 + Amendment 2026-05-13 + Phase C Tracks 1-5 applied).
- §1.3 cross-artifact coherence list (per Stage 1c COHERENCE VERIFIED).
- §1.4 audience-load verification list (per Pass 3.4 CONDITIONALLY ROBUST + cross-chapter rent-seeking-engagement workstream disposition).
- §2.1 + §2.2 + §2.3 external-corroboration + math-review + audience-coverage-gap inventories.
- §3.1 through §3.6 recommended-reviewer inventories.
- §4 priority-rank list.

**STAYS OPEN until canonical-pipeline decision lands:**
- §1.5 Stage 4 render-integrity verdict (currently PROPOSED-pending-canonical-pipeline-decision; ratifies post canonical-pipeline decision — Option A/B/C; recommended Option A per Stage 4 §10).
- Stage 5 sign-off (currently PENDING; ratifies after Stage 4 verdict ratifies).
- §3.5 post-typesetter formula-integrity re-verification scope (currently flagged HIGH; specific execution method — manual vs automated — open).
- Pre-publication refresh I-1 + I-2 application timing (currently DEFERRED; ratifies at pre-pub refresh session).

**Ratification path:** This artifact ratifies in batch with Stage 4 verdict ratification, after all 4 first-retrofit chapters' (Ch 1 + Ch 5 + Ch 6 + TA) Stage 4 comparison rounds complete + author selects Option A/B/C. At that ratification, §1.5 + the Stage 5 sign-off cross-reference + the Stage 4 audit-trail update populate; the rest of this artifact carries forward as drafted.

---

## §7. Mandatory pre-pub queue items checklist (per retrofit handoff stub §1 row 5)

Per handoff stub §1 row 5 mandatory items + verification at this artifact:

- ✓ **Math reviewer** (§3.1) — drafted with profile + scope + what-to-look-for.
- ✓ **Framework-methodology reviewer** (§3.2) — drafted across 5 adjacent traditions (heterodox-econ; Stern; Hartwick; Ostrom-successor; Dixit-Pindyck).
- ✓ **Reparations-economics reviewer (Darity-Mullen-tradition successor; Darity already engaged per Sandy-packet)** (§3.3) — drafted with Sandy/Darity in flight + 7 additional Darity-Mullen-tradition successors.
- ✓ **Post-typesetter formula-integrity re-verification (the typesetter is the highest-risk pre-publication render step for TA specifically)** (§3.5) — drafted with execution method options + failure-mode test list.
- ✓ **F-7 cumulative oil/gas split exact-percentage refresh (per I-1 deferred item; ~15 min effort; CSV download from sodir.no)** (§2.1) — drafted with hardening path + magnitude impact + estimated effort.
- ✓ **Public-Choice-tradition reviewer (NEW; surfaced from Pass 3.4)** (§3.4) — added beyond the mandatory items per Pass 3.4 thread Σ1 disposition.

All mandatory pre-pub queue items addressed in this PROPOSED-DEFERRED artifact.

---

*End of pre-publication review queue artifact (Technical Appendix). PROPOSED-DEFERRED 2026-05-18. Ratifies in batch with Stage 4 verdict per retrofit handoff stub §1 + standardization-handoff §3.5. **Most consequential Stage 5 pre-pub queue in the corpus** per handoff stub §1 row 5.*
