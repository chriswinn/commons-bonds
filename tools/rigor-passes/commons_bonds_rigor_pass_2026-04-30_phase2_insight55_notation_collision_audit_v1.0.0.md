# Commons Bonds — Insight #55 Framework-Wide Notation Collision Audit (One-Time Retroactive Sweep)

**Version:** 1.0.0
**Date:** 2026-04-30
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` + Vocabulary strategy v1.0.1 §13 notation-discipline + Insight #55 audit specification. Cross-document scan for notation collisions across all framework apparatus.

**Author direction triggering this pass (2026-04-29 by Chris Winn):** *"implement 4 layers as you recommended"* — Insight #55 OPEN; one-time retroactive audit before Phase 3 Tech Appendix v2.0.0 rebuild.

**Scope:** Comprehensive cross-document scan for notation collisions across:
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` (7,412 lines)
- `core/terms/terms_index.md` (2,109 lines)
- `manuscript/chapters/Chapter_*Draft.{md,html}` (9 chapters)
- `core/glossary/archive/commons_bonds_updated_glossary_v3.html` (406 lines)

Categories examined:
1. Single-letter Latin variables (A, B, C, D, E, P, Q, R, S, U)
2. Greek letters (α, β, γ, δ, ε, η, θ, λ, μ, ν, π, ρ, σ, τ, φ, ψ, ω)
3. Subscript/superscript patterns (B₁, B₂, Cᵢ, S_max, S_threshold, t₀, r_∞)
4. Multi-letter abbreviations (RCV, CIT, CSD, ARR, IPG, CS; retired AIT, FGC, ESG)
5. Section-namespace overlap (informational)

**Status:** **RATIFIED 2026-04-30 by Chris Winn — verdict (a) Full ratify: apply all remediations + ledger additions.** Implementation: ledger additions (β, σ, ρ, ξ, S_threshold) applied to Vocabulary strategy v1.0.1 §13.2 this commit; Routine 1 pattern #10 reserved-letter ledger updated this commit; 3 HIGH-severity renames (α → ξ for E.3 curvature; τ → u for integration variable; C → 𝒞 for commons-territory set) queued for Phase 3 Tech Appendix v2.0.0 rebuild scope.

**Author:** Chris Winn

**Recommended verdict (preview):** **3 HIGH-severity collisions surfaced** (require rename/disambiguation before Phase 3 v2.0.0 rebuild) + **3 MEDIUM-severity reserved-letter additions** to §13.2 ledger (currently-used letters not yet codified) + **1 LOW-severity informational note** on section-namespace overlap with single-letter variables.

The framework's notation discipline is largely sound. The major findings are concentrated in the scarcity-multiplier formula apparatus (§M of Tech Appendix) and the existential-substitutability-gap section (§F), where Greek letter usage developed organically before the four-layer notation discipline was codified.

**Three HIGH-severity collisions:**

1. **α (alpha) — load-bearing dual-use:** α used as *irreversibility parameter* in §M scarcity-multiplier formula AND as *cost-function curvature parameter* in Insight #42 Theorem E.3 functional form. Same Greek letter; two distinct concepts; both load-bearing.

2. **τ (tau) — integration variable vs scarcity threshold:** τ used as *integration variable* in line 6720 (standard math convention: `exp(−∫_{t₀}^t r(τ)dτ)`) AND newly reserved as *scarcity threshold* per Insight #42 ratification (Theorem E.3 restructure: c(A) = c₀ · (τ/(A−τ))^α). Local-scope vs global-scope conflict.

3. **C — semantic overload:** C used as *cost variable* (Cᵢ throughout RCV integrand) AND as *commons territory set* (line 398: "R ∈ C, where C denotes commons territory") AND as *§C section namespace* (CIT methodology section). Three distinct uses.

**Three MEDIUM-severity reserved-letter additions** (not in current §13.2 ledger):

4. **σ (sigma) — scarcity parameter** (used 33 times in §M; defined as commons-stock / sustainable-flow ratio at line 862)
5. **β (beta) — risk-posture calibrator** (used 30 times in §M; defined as exponent in irreversibility_premium formula at line 867)
6. **ρ (rho) — regeneration rate** (used 5 times; defined at line 398 as commons regeneration rate ρ ≥ 0)

**One LOW-severity informational note:**

7. Section labels (§A through §M) overlap with single-letter variable namespace (A, B, C, D, E). Context disambiguates in practice; standard academic-economics convention (sections labeled by letter; variables by letter); not a collision requiring rename. Documented for completeness.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

Per Insight #55 specification (alignment/commons_bonds_open_insights_v1.0.0.md):

> *"Comprehensive sweep of all variable letters/symbols + abbreviations across the framework's apparatus to identify undisclosed notation collisions."*

The audit applied the reserved-letter ledger from Vocabulary strategy v1.0.1 §13.2 as baseline + cross-checked all framework documents for collisions.

### §1.2 Aggregate findings

| Severity | Count | Items |
|---|---|---|
| HIGH (rename / disambiguation required) | 3 | α; τ; C |
| MEDIUM (reserved-letter ledger additions) | 3 | σ; β; ρ |
| LOW (informational; no rename) | 1 | section-namespace overlap |
| Already-resolved (cross-reference only) | 3 | S → τ (Insight #42); RCV acronym (Insight #50); Q(t) convention (Insight #52) |

**No FAIL findings.** All collisions are resolvable via subscript-disambiguation, contextual-renaming, or ledger-codification. None requires structural reframing of the framework's apparatus.

### §1.3 Verdict pattern

The audit confirms Insight #55's hypothesis: notation collisions exist beyond the S → τ collision caught by Phase 2 Insight #42. Three additional HIGH-severity collisions surfaced. The four-layer discipline (Routine 1 + Routine 2 + this Insight + §13 standing-discipline) is justified — single-theorem audits would not have surfaced any of these.

### §1.4 Implementation venue

All HIGH-severity remediations are batched into Phase 3 Tech Appendix v2.0.0 rebuild per shared open question with Insights #35 + #38 + #40 + #41 + #42 + #47-#53. Reserved-letter ledger additions (MEDIUM-severity) applied in this commit to Vocabulary strategy v1.0.1 §13.2.

---

## §2. Methodology

### §2.1 Cross-document scan approach

For each reserved letter/abbreviation in §13.2 ledger:
1. `grep -nE` for definitional contexts (`X =`, `where X`, `X denotes`, `X represents`, `let X`).
2. Identify all distinct semantic uses across the document set.
3. Classify by severity:
   - **HIGH** — load-bearing in framework apparatus; rename/disambiguation required.
   - **MEDIUM** — used in framework apparatus but not in ledger; codify as reserved.
   - **LOW** — informational; context disambiguates.
4. Cross-reference existing resolutions (Insights #42, #50, #52 already addressed specific collisions).

### §2.2 Documents in scope

| Document | Lines | Notes |
|---|---|---|
| `core/technical-appendix/TechnicalAppendix_v1.0.0.html` | 7,412 | Primary mathematical-formal apparatus |
| `core/terms/terms_index.md` | 2,109 | Term provenance index |
| `manuscript/chapters/Chapter_*Draft.{md,html}` | ~52,000 words across 9 chapters | Chapter prose (mostly narrative, not technical) |
| `core/glossary/archive/commons_bonds_updated_glossary_v3.html` | 406 | Reader-facing glossary entries |

Chapter prose was scanned separately for Greek-letter and variable-letter usage. Result: minimal technical-variable usage in chapters (chapter register is narrative); no collisions detected. All collisions concentrate in Tech Appendix + terms_index.

### §2.3 What this audit does NOT do

- Does NOT execute remediation (renames + ledger updates apply at Phase 3 v2.0.0 rebuild + this commit's §13.2 update).
- Does NOT verify external-academic-convention alignment for proposed remediation choices (covered by Insight #39 pre-publication external review).
- Does NOT scan rigor-pass documents (`tools/rigor-passes/*.md`) — those are scaffolding/decision-record per Working Principle #8 Tier 3; preserved retirement traces + provenance allowed; not subject to publisher-facing notation discipline.

---

## §3. Per-letter audit findings — Latin single-letter

### §3.1 A (Abundance) — PASS

**Reserved use:** Theorem E.3 abundance variable (cost-tier domain).
**Scan results:**
- `A` as abundance level (Theorem E.3): consistent with reserved use.
- "Habitability Abundance," "Spatial Abundance," etc. (§C.2 seven dimensions): related concept; uses "Abundance" as descriptor for each dimension. Different concrete realizations of same conceptual category.
- "Abundance" used throughout as conceptual descriptor: consistent.

**Verdict:** PASS. No collision; uses are coherent variations on the abundance concept.

### §3.2 B (Accountability Bond) — PASS with section-namespace overlap (LOW)

**Reserved uses:** Aggregate Accountability Bond B; sub-instruments B₁ (Restitution Bond), B₂ (Foreclosure Bond).

**Other uses found:**
- "Path B" (Theorem E.5 proof): narrative label; standard "Path A vs Path B" comparison. Different namespace.
- "Level B" (CIT level taxonomy, line 1551): different framework concept; CIT-level classification. Different namespace.
- "§B" / "B.1" / "B.2" (section labels): section namespace; standard academic-economics convention.

**Verdict:** PASS. All non-variable uses are clearly different namespaces (paths, levels, sections); context disambiguates. **LOW-severity informational note**: section-namespace overlap with B is documented for completeness; no rename required.

### §3.3 C (Cost variable) — **HIGH-severity collision found**

**Reserved use:** Cost variable, particularly C₁, C₂, ..., Cᵢ (cost components in RCV integrand).

**Distinct uses found:**

1. **C as cost variable / Cᵢ** — primary reserved use; pervasive in §B + §L + §M.
2. **C as "commons territory" set** — line 398: *"A resource unit R ∈ C (where C denotes commons territory) is drawn from a shared stock Q with regeneration rate ρ ≥ 0."*
3. **§C section** — Commons Inversion Test methodology section; §C.1, §C.2, §C.3.

Use #2 (C as commons-territory set) is a NEW reserved use not in §13.2 ledger. **It directly collides with use #1** (cost variable C). Both are mathematical-formal uses (one is a variable; one is a set). Same letter; different types of mathematical objects.

**Severity: HIGH.** A reader encountering "R ∈ C" at line 398 then "Cᵢ" later in the same document reasonably tries to relate the two. The relation isn't there — they're different concepts using same letter.

**Remediation recommendation:** Rename "commons territory" set to a different letter. Candidates:
- **𝒞 (script C)** — distinct typography; mathematical-conventional for set-vs-variable disambiguation; minor copy-edit complication.
- **𝓒 (calligraphic C)** — same purpose; different typography option.
- **𝛺 (Greek capital omega)** — common notation for outcome/sample space in probability; available; no current framework use.
- **𝒮 (script S) for "shared stock space")** — but conflicts with substitutability function S; rejected.
- **𝓚 (calligraphic K) for "commons set")** — K = Kommons (German); available; distinctive.

**Recommended:** **𝒞 (script C)** for commons-territory set. Standard mathematical convention for set-vs-variable disambiguation; preserves the C mnemonic; minimal copy-edit work.

Update line 398 to: *"A resource unit R ∈ 𝒞 (where 𝒞 denotes commons territory) is drawn from a shared stock Q with regeneration rate ρ ≥ 0."*

### §3.4 D (Discount factor) — PASS

**Reserved use:** D(t, t₀) declining discount factor (Weitzman 2001).
**Scan results:** Consistent throughout. No collision.

**Verdict:** PASS.

### §3.5 E (Externality tail) — PASS with section-namespace overlap (LOW)

**Reserved uses:** E(R, t) externality tail function; Theorem labels E.1–E.5.

**Other uses found:**
- "Section E" (Theorems & Proofs): section namespace.
- E in expressions (e.g., "the E term"): consistent with reserved use.

**Verdict:** PASS. Theorem labels E.1–E.5 vs externality function E(R, t) — context disambiguates clearly (theorem labels are followed by names + colon; function is followed by parenthetical arguments). **LOW-severity note**: this overlap is intentional + non-confusing; no rename required.

### §3.6 P (Market price) — PASS

**Reserved use:** Market price (Theorem E.1 + Theorem E.5).
**Scan results:** Consistent throughout.

**Verdict:** PASS.

### §3.7 Q (Quality-stock) — PASS (resolved per Insight #52)

**Reserved use:** Q(t) quality-stock per Insight #52 (P2#8 RCV integrand Q(t) notation-clarity audit).
**Scan results:** Consistent post-Insight #52 ratification.

**Verdict:** PASS. Already-resolved; cross-reference Insight #52.

### §3.8 R (Resource) — PASS

**Reserved use:** Resource (RCV integrand variable).
**Scan results:** Consistent throughout.

**Verdict:** PASS.

### §3.9 S (Substitutability function) — RESOLVED per Insight #42 (cross-reference)

**Reserved uses:** S(t) substitutability function; S_max substitutability function limit; S_threshold (substitutability critical value, §F existential substitutability gap).

**Pre-Insight #42 collision:** S used as scarcity threshold in original Theorem E.3 — RESOLVED via rename to τ (per Insight #42 ratification 2026-04-29).

**Post-Insight #42 audit:** S, S(t), S_max, S_threshold are coherent — all relate to substitutability:
- S (or S(t)) — substitutability function (probability)
- S_max — limit of substitutability function
- S_threshold — critical value of S_max (existential substitutability gap definition)

The *_threshold suffix is appropriate convention for "a specific value of S_max below which a property holds." Different from τ (abundance scarcity threshold) — τ is the *abundance* threshold; S_threshold is the *substitutability* threshold. Distinct concepts; distinct subscripts.

**Verdict:** PASS post-Insight #42. **Recommendation:** add explicit S_threshold entry to §13.2 ledger to prevent future confusion.

### §3.10 U (Utility) — PASS

**Reserved use:** U(R, t, Q(t)) utility function.
**Scan results:** Consistent throughout.

**Verdict:** PASS.

---

## §4. Per-letter audit findings — Greek

### §4.1 α (alpha) — **HIGH-severity collision found**

**Distinct uses found:**

1. **α = irreversibility parameter** (§M scarcity multiplier, line 863): *"α = irreversibility parameter (probability commons cannot be restored at any finite cost once extracted; α ∈ [0, 1])"* + formula `irreversibility_premium(α) = 1 / (1 - α)^β`.

2. **α = cost-function curvature parameter** (Insight #42 Theorem E.3 functional form): *c(A) = c₀ · (τ/(A−τ))^α with α ≥ 1*.

These are two different concepts using the same Greek letter. Both load-bearing — use #1 in scarcity-multiplier apparatus (Method 3); use #2 in restructured Theorem E.3.

**Severity: HIGH.** Both uses appear in mathematical-formal contexts; reader cross-referencing E.3 to §M will conflate them.

**Remediation recommendation:** rename one use. Options:

- **(A) Keep α for scarcity-multiplier irreversibility parameter (§M); rename E.3 curvature to ξ (xi):** preserves §M's existing extensive use of α; ξ is unused in framework; available.
- **(B) Keep α for E.3 curvature (Insight #42 ratified); rename §M irreversibility to ι (iota):** preserves the just-ratified Insight #42 functional form; ι is unused.
- **(C) Use α for both with subscripts: α_irr (irreversibility) + α_curv (curvature):** preserves α mnemonic; subscript-disambiguation; standard academic-economics convention.

**Recommended:** **Option (A) — rename E.3 curvature to ξ (xi).** Reasoning: §M's α is more extensively used (33+ instances in scarcity-multiplier apparatus); E.3's α appeared only in Insight #42 functional form (1 instance in DRAFT — not yet applied to Tech Appendix; remediation can happen during Phase 3 v2.0.0 rebuild in same pass). Smaller blast radius.

Updated E.3 functional form: **c(A) = c₀ · (τ/(A−τ))^ξ with ξ ≥ 1**.

Update §13.2 ledger:
- α (alpha) — irreversibility parameter (§M scarcity multiplier; probability commons cannot be restored once extracted; α ∈ [0, 1])
- ξ (xi) — cost-function curvature parameter (Insight #42 Theorem E.3 functional form; ξ ≥ 1)

### §4.2 β (beta) — **MEDIUM-severity reserved-letter addition**

**Reserved use (newly identified):** β = risk-posture calibrator (§M scarcity multiplier; line 867: *"β > 0 calibrates risk-posture (β = 1 default; β = 2 precaution-regime)"*).

**Severity: MEDIUM.** Currently used 30 times in framework apparatus but NOT in §13.2 ledger. No collision detected (β has only one use); but absence from ledger means future framework decisions could introduce conflicting β.

**Remediation recommendation:** Add β to §13.2 ledger with current usage codified.

### §4.3 γ (gamma) — UNUSED (available)

**Scan result:** 0 uses in framework apparatus. Available for future reservation.

### §4.4 δ (delta) — minimal use; PASS

**Scan result:** 1 use; appears in standard math notation (limit-style "any δ > 0").

**Verdict:** PASS. Standard math convention; not a reserved framework variable.

### §4.5 ε (epsilon) — UNUSED (available)

**Scan result:** Standard math notation only ("for any ε > 0"). Not a reserved framework variable.

### §4.6 λ (lambda) — PASS (per Insight #40)

**Reserved use:** Substitutability function exponential parameter (Insight #40 Theorem E.4: *S(t) = S_max(1 − e^{−λt})*).
**Scan results:** Consistent.

**Verdict:** PASS.

### §4.7 ρ (rho) — **MEDIUM-severity reserved-letter addition**

**Reserved use (newly identified):** ρ = commons regeneration rate (§B Definition A.1; line 398: *"...drawn from a shared stock Q with regeneration rate ρ ≥ 0"*).

**Severity: MEDIUM.** Currently used 5 times in framework apparatus but NOT in §13.2 ledger.

**Remediation recommendation:** Add ρ to §13.2 ledger.

### §4.8 σ (sigma) — **MEDIUM-severity reserved-letter addition**

**Reserved use (newly identified):** σ = scarcity parameter (§M scarcity multiplier; line 862: *"σ = scarcity parameter (commons-stock / sustainable-flow ratio)"*) + scarcity_multiplier(σ) = 1 + log(1 + σ) × Hotelling_anchor.

**Severity: MEDIUM.** Currently used 33 times in framework apparatus but NOT in §13.2 ledger.

**Remediation recommendation:** Add σ to §13.2 ledger.

### §4.9 τ (tau) — **HIGH-severity collision found**

**Distinct uses found:**

1. **τ = scarcity threshold** (Insight #42 ratification 2026-04-29; Theorem E.3 functional form). RESERVED in §13.2 ledger.

2. **τ = integration variable** (line 6720): *"exp(−∫_{t₀}^t r(τ)dτ)"* — local-scope integration variable in discount factor expression.

**Severity: HIGH.** Use #2 is a *standard math convention* (integration dummy variable). But use #1 is a *global framework reserved letter* (Insight #42). Local-scope vs global-scope conflict — a reader following the framework's reserved-letter discipline encounters τ at line 6720 and reasonably interprets as scarcity threshold; the local-scope-integration-variable usage is unmarked.

**Remediation recommendation:** Replace integration variable τ with a different dummy letter. Standard alternatives:
- **u (or s, or v)** — common alternative integration dummy letters; lowercase; distinct from S = substitutability.
- **ξ (xi)** — but reserved per §4.1 above (E.3 curvature parameter).

**Recommended:** **rename integration variable from τ to u**. Update line 6720 to: *"exp(−∫_{t₀}^t r(u)du)"*.

**Or:** simply use the same letter as in primary usage `r(s)` per Insight #40 E.4 audit: line 6720 already has another expression using `r(s)` style; consolidate to that convention.

### §4.10 Other Greek letters (φ, ψ, ω, μ, ν, π, η, θ) — UNUSED (available)

**Scan result:** 0 uses in framework apparatus. Available for future reservation.

---

## §5. Per-abbreviation audit findings — Multi-letter

### §5.1 RCV — RESOLVED per Insight #50 (cross-reference)

**Reserved use:** Residual Commons Value.
**Pre-resolution collision:** RCV vs adjacent-field meanings (radio common variable; recreational vehicle; ranked-choice voting). RESOLVED via Insight #50 (Phase 2 #4 RCV acronym collision audit).

**Verdict:** PASS post-Insight #50. Cross-reference for full disposition.

### §5.2 CIT — PASS

**Reserved use:** Commons Inversion Test.
**Scan results:** Consistent throughout. Adjacent-field collisions checked: CIT does not collide with established economics/finance/policy abbreviations of equivalent prominence. Some narrow collisions exist (Citi Investment Trust; CIT Group financial services) but no academic-economics tradition uses CIT for a methodological construct of comparable load-bearing.

**Verdict:** PASS. Recommendation: add CIT to formal acronym table in §13.2 ledger (currently noted; could be more prominent).

### §5.3 CSD — PASS

**Reserved use:** Cost Severance Damages.
**Scan results:** Consistent. No academic-economics collision.

**Verdict:** PASS.

### §5.4 ARR — PASS

**Reserved use:** Asymmetric Regret Rule.
**Scan results:** Consistent. Adjacent collision: "annualized rate of return" (ARR in finance) — but framework's regret-theory context disambiguates clearly.

**Verdict:** PASS.

### §5.5 IPG — PASS

**Reserved use:** Intergenerational Pricing Gap.
**Scan results:** Consistent.

**Verdict:** PASS.

### §5.6 CS — PASS

**Reserved use:** Cost Severance (per equation CS = RCV − B).
**Scan results:** Consistent. Adjacent-field collisions exist (Computer Science; CS gas; etc.) but framework context disambiguates.

**Verdict:** PASS.

### §5.7 Retired abbreviations — handled per Routine 1

**AIT, FGC, ESG** — RETIRED; Routine 1 daily sentinel patterns already detect regression. No new collisions introduced.

**Verdict:** PASS (handled by ongoing routine).

---

## §6. Subscript / superscript audit

### §6.1 B₁, B₂ — PASS

**Reserved uses:** Sub-instruments of Accountability Bond (B₁ = Restitution Bond; B₂ = Foreclosure Bond).
**Scan results:** Consistent.

**Verdict:** PASS.

### §6.2 Cᵢ — PASS

**Reserved use:** i-th cost component in RCV integrand (sum-of-costs form).
**Scan results:** Consistent. C₁ + C₂ + C₃ specific instances used in §L worked examples (foreclosure cost; externality tail; community-transition cost).

**Verdict:** PASS.

### §6.3 S_max — PASS

**Reserved use:** Limit of substitutability function (Insight #33 existential substitutability gap).
**Scan results:** Consistent.

**Verdict:** PASS.

### §6.4 S_threshold — **MEDIUM-severity ledger addition**

**Reserved use (newly identified):** Critical value of S_max below which a resource is existentially critical (§F existential substitutability gap definition; line 531).

**Severity: MEDIUM.** Coherent with substitutability namespace (S_max + S_threshold both relate to substitutability function); not in §13.2 ledger.

**Remediation recommendation:** Add S_threshold to §13.2 ledger.

### §6.5 t₀, r_∞ — PASS

**Reserved uses:** Initial time (t₀); long-run discount rate (r_∞).
**Scan results:** Consistent (49 uses combined).

**Verdict:** PASS.

---

## §7. Section-namespace overlap (informational)

Section labels (§A through §M) overlap with single-letter variable namespace (A, B, C, D, E):

- §A. Definitions (overlaps with A = abundance variable)
- §B. RCV Model (overlaps with B = Accountability Bond)
- §C. Commons Inversion Test Protocol (overlaps with C = cost variable + new finding §3.3 commons-territory set)
- §D. (currently unused; would overlap with D = discount factor)
- §E. Theorems & Proofs (overlaps with E = externality tail + Theorem labels E.1-E.5)
- §F. Existential Substitutability Gap (no variable conflict)
- §G. Universality Test (no variable conflict)
- §H. Empirical Validation Cases (no variable conflict)
- §K. Discount Function (no variable conflict)
- §L. Four Gates (no variable conflict)
- §M. Formula Generalization (no variable conflict)

**Severity: LOW.** Standard academic-economics convention; section labels use letters alphabetically; variable letters chosen for mnemonic value. Context disambiguates in practice (§B vs B variable).

**Remediation recommendation:** None required. **Documented for completeness** in §13 notation-discipline standing reference.

---

## §8. Severity classification + remediation summary

### §8.1 HIGH-severity collisions (3 — require action before Phase 3 v2.0.0 rebuild)

| # | Letter | Collision | Recommended remediation |
|---|---|---|---|
| 1 | **α** | irreversibility parameter (§M) vs cost-function curvature (Insight #42 E.3) | Rename E.3 curvature to **ξ (xi)** |
| 2 | **τ** | integration variable (line 6720) vs scarcity threshold (Insight #42) | Rename integration variable to **u** OR consolidate to `r(s)` convention |
| 3 | **C** | cost variable (Cᵢ) vs commons-territory set (line 398) | Rename commons-territory set to **𝒞 (script C)** |

### §8.2 MEDIUM-severity reserved-letter additions (3 — codify in §13.2 ledger this commit)

| # | Letter | Current use | Action |
|---|---|---|---|
| 4 | **σ (sigma)** | Scarcity parameter (§M) | Add to §13.2 ledger |
| 5 | **β (beta)** | Risk-posture calibrator (§M) | Add to §13.2 ledger |
| 6 | **ρ (rho)** | Commons regeneration rate (§B Definition A.1) | Add to §13.2 ledger |
| (also) | **S_threshold** | Critical substitutability value (§F) | Add to §13.2 ledger |

### §8.3 LOW-severity informational

| # | Pattern | Note |
|---|---|---|
| 7 | Section-namespace overlap (§A-§M vs A-E variables) | Standard convention; no rename; document in §13 |

### §8.4 Already-resolved collisions (cross-reference only)

- **Insight #42** — S → τ rename (Theorem E.3 scarcity threshold)
- **Insight #50** — RCV acronym collision audit
- **Insight #52** — Q(t) convention divergence audit

---

## §9. Updates to §13.2 reserved-letter ledger

Vocabulary strategy v1.0.1 §13.2 ledger to be updated this commit with:

**Greek letters (additions + 1 new reservation):**

| Letter | Reserved use | Source |
|---|---|---|
| **α** | Irreversibility parameter (§M scarcity multiplier; α ∈ [0, 1]) | §M Tech Appendix |
| **β** | Risk-posture calibrator (§M scarcity multiplier; irreversibility_premium exponent) | §M Tech Appendix |
| **ξ (xi)** | Cost-function curvature parameter (Insight #42 Theorem E.3 functional form; ξ ≥ 1) | Insight #42 (post-Insight #55 rename from α) |
| **λ** | Substitutability function exponential parameter | Insight #40 |
| **ρ** | Commons regeneration rate | §B Definition A.1 |
| **σ** | Scarcity parameter (commons-stock / sustainable-flow ratio) | §M Tech Appendix |
| **τ (tau)** | Scarcity threshold (Insight #42); ALSO integration variable (line 6720; local scope only — recommend rename to u) | Insight #42 + audit-pending §M |

**Subscript additions:**

| Pattern | Reserved use | Source |
|---|---|---|
| **S_threshold** | Critical value of S_max below which resource is existentially critical | §F existential substitutability gap |

**New section-namespace note:**

Section labels §A through §M are part of the framework's apparatus. Standard academic-economics convention (sections labeled by letter; variables by letter); context disambiguates. Documented for completeness; no rename required.

**New set-vs-variable typography note:**

Set-valued objects (e.g., 𝒞 commons territory) use **script/calligraphic typography** (𝒞, 𝒟, 𝒮, etc.) to disambiguate from variable namespace (C, D, S). Standard mathematical convention.

---

## §10. Cross-references to existing resolutions

This audit ratifies the architecture established by:

- **Insight #42** (Phase 2 Theorem E.3) — origin of NOTATION COLLISION discipline; established S → τ rename + 4-layer notation discipline.
- **Insight #50** (Phase 2 RCV acronym collision audit) — already-resolved RCV collision.
- **Insight #52** (Phase 2 RCV integrand Q(t) convention divergence) — already-resolved Q(t) convention issue.
- **Insight #33** (existential substitutability gap rename) — established S_max notation.
- **Insight #40** (Theorem E.4) — established S(t) substitutability-function notation; established λ as substitutability exponential parameter.
- **Insight #47** (P2#7 Scarcity multiplier formula audit) — α + σ + V_option + β apparatus reviewed; this audit completes the reserved-letter codification.
- **Routine 1** (daily sentinel) — extended with notation-collision patterns #9 + #10 per Insight #55 implementation.
- **Routine 2** (weekly pre-submission audit) — extended with notation-collision sweep check #5 per Insight #55 implementation.
- **Vocabulary strategy v1.0.1 §13** — standing notation-discipline reference (this commit updates §13.2 ledger).

---

## §11. Verdict + ratification choices

### §11.1 Recommended verdict

**KEEP framework apparatus + apply remediations per §8 + codify reserved-letter ledger per §9.**

- 3 HIGH-severity collisions require remediation (renames batched into Phase 3 Tech Appendix v2.0.0 rebuild).
- 3 MEDIUM-severity reserved-letter additions applied to §13.2 ledger this commit.
- 1 LOW-severity informational note added to §13 standing reference this commit.

### §11.2 Pass-fail verdict

**PASS conditional on Phase 3 v2.0.0 rebuild applying the 3 HIGH-severity renames.** The framework's notation discipline is largely sound; the 3 HIGH-severity collisions are concentrated in pre-Insight-#42 apparatus (§M; line 398; line 6720) where Greek letter usage developed organically before notation discipline was codified.

### §11.3 Author ratification choices

**(a) Full ratify §11.1 verdict** — apply all remediations.

**(b) Modify remediation choices** — author specifies different rename targets:
- (b.i) α collision: keep α for E.3, rename §M irreversibility parameter to ι (Option B in §4.1)
- (b.ii) α collision: subscript-disambiguation (α_irr + α_curv per Option C in §4.1)
- (b.iii) τ collision: different integration-variable choice (other than u)
- (b.iv) C collision: different set-typography choice (𝓒 calligraphic, 𝓚 commons, etc.)

**(c) Defer remediation** — codify ledger only; defer renames to later (carries Phase 3 v2.0.0 rebuild risk).

**(d) Reject** — author rejects audit findings.

**Recommendation: (a) Full ratify.** Remediations are bounded (3 specific renames at specific Tech Appendix locations); ledger updates are non-disruptive (codify existing usage); LOW-severity note is documentation-only.

### §11.4 Implementation pending after ratification

If (a) full ratify:

1. **Vocabulary strategy v1.0.1 §13.2 update** — apply ledger additions (β, σ, ρ, ξ, S_threshold) + section-namespace note + set-vs-variable typography note. Apply this commit.

2. **Phase 3 Tech Appendix v2.0.0 rebuild** — apply 3 HIGH-severity renames:
   - §M scarcity multiplier formula: α retained as irreversibility parameter (no change in §M).
   - Insight #42 E.3 functional form: rename α → ξ (xi). Update terms_index Insight #42 record + canonical rigor pass.
   - Line 6720 integration variable: rename τ → u (or consolidate to `r(s)` convention).
   - Line 398 commons-territory set: rename C → 𝒞 (script C).

3. **Routine 1 daily sentinel** — pattern #10 reserved-letter ledger updated (in routines file; deployed via cron when convenient).

4. **Routine 2 weekly sweep** — pattern continues; expect zero new HIGH-severity findings post-rebuild.

5. **terms_index updates:**
   - Insight #42 record: ratify α → ξ rename.
   - Cost Severance entry: cross-reference §13.2 ledger.
   - Various Cᵢ entries: cross-reference 𝒞 commons-territory set notation if used in entry text.

6. **Pre-publication external review** (per Insight #39) — notation-discipline reviewer verifies remediations + ledger.

---

## §12. Open questions for author discussion

1. **α collision remediation choice** — recommended Option (A) rename E.3 curvature to ξ. Alternative (B) keeps α for E.3, renames §M irreversibility to ι. Alternative (C) uses subscript-disambiguation (α_irr + α_curv). Author preference?

2. **τ collision remediation choice** — recommended rename integration variable to u (or consolidate to `r(s)` convention). Alternative: keep τ for both with explicit "local-scope dummy variable" footnote. Author preference?

3. **C collision remediation choice** — recommended rename commons-territory set to 𝒞 (script C). Alternative typography: 𝓒 (calligraphic), 𝓚 (commons K), 𝛺 (sample space). Author preference?

4. **Section-namespace overlap documentation depth** — how much detail in §13 standing reference? Brief note vs comprehensive table?

5. **Phase 3 Tech Appendix v2.0.0 rebuild scope confirmation** — confirm renames batched into v2.0.0 rebuild (per §11.4 implementation plan). Any preference for piecemeal v1.0.0 application instead?

6. **Ledger update vs full §13 restructure** — recommended approach is incremental ledger update (add β, σ, ρ, ξ, S_threshold; add notes). Alternative: restructure §13 with expanded mathematical-conventions section. Author preference?

---

## §13. Cross-references

### §13.1 Upstream

- **Insight #55 OPEN** — origin of this audit; specifies scope + categories + reserved-letter ledger.
- **Vocabulary strategy v1.0.1 §13** — standing notation-discipline reference (updated this commit).
- **Insight #42** (Phase 2 Theorem E.3) — origin of NOTATION COLLISION discipline; S → τ rename ratification.
- **Insight #50** (Phase 2 RCV acronym collision) — already-resolved RCV.
- **Insight #52** (Phase 2 RCV integrand Q(t)) — already-resolved Q(t) convention.
- **Insight #33** (existential substitutability gap rename) — established S_max.
- **Insight #40** (Theorem E.4) — established S(t) and λ.
- **Insight #47** (P2#7 Scarcity multiplier formula) — α + σ + β apparatus reviewed.
- **Routine 1** (daily sentinel) — extended per Insight #55 with patterns #9 + #10.
- **Routine 2** (weekly pre-submission audit) — extended per Insight #55 with check #5.

### §13.2 Downstream

- **Phase 3 Tech Appendix v2.0.0 rebuild** — applies 3 HIGH-severity renames.
- **Vocabulary strategy v1.0.1 §13.2** — ledger updated this commit.
- **Insight #42 record + canonical rigor pass** — α → ξ rename ratification (cross-reference).
- **Pre-publication external review** (Insight #39) — notation-discipline reviewer.

### §13.3 Sibling Phase 2 audits

All ratified Phase 2 audits (Insights #35, #38, #40-42, #47-53) feed into Phase 3 Tech Appendix v2.0.0 rebuild. This Insight #55 audit completes the notation-discipline layer of that rebuild scope.

---

**End of Phase 2 Insight #55 framework-wide notation collision audit v1.0.0 [RATIFIED 2026-04-30 by Chris Winn — verdict (a) Full ratify].**
