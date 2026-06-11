# Tech Appendix Numbering Audit Inventory — 2026-05-11

**Source file audited:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (7,817 lines as of HEAD commit `9db16ae`).

**Read-only audit; no edits applied.** Author ratification gate required before Phase 3 application.

**Verification stance:** All line numbers below verified via grep against the current file state on 2026-05-11. Each h2, h3, and h4 heading sampled directly. Cross-reference catalog assembled from `grep -oE "Section [A-Z](\.[0-9]+)?"` and `grep -oE "Theorem [A-Z]\.[0-9]+[a-z]?"` against the live file.

---

## Headline finding (changes scope from handoff)

The handoff approximated **two** parallel numbering systems (numeric §1–§9 vs. letter A–M). The actual situation is **four** intersecting schemes:

1. **Top-level numeric §1–§18** (clean) — TOC, all h2 headers, all HTML `id="sec-N-..."` anchors.
2. **Numeric h3 subsections §X.Y** (partial) — some sections use it (§2, §3, §4, §5, §6, §8, §11, §15), others don't.
3. **Letter h3 subsections** (legacy) — B/C/D/E/G/H/I/K/L/M sub-IDs; letters A, F, J are absent; letters do not align alphabetically with numeric ordering.
4. **Embedded "supplement" re-started §-numbering at h4/h5 level** (NEW finding, not flagged in handoff) — h4 headings inside §6.3 use §0–§8 as an enumerated walkthrough list; h4 headings inside §11.X clusters use locally restarted §1, §2, §3 for calibration-block internals; body prose references to "supplement §3.1" / "supplement §3.3" / "supplement §7" appear to be stale legacy pointers from a pre-merger state when validation cases lived in a separate "supplement" document.

The TOC + h2 + HTML anchors are coherent. The complications are at h3 + h4 + body-prose levels.

---

## Top-level inventory (§1–§18)

All 18 top-level sections use the numeric scheme cleanly in h2 + HTML anchor + TOC.

| § | Line | h2 title | HTML anchor | Letter alias (in body prose / h3 contamination) |
|---|---|---|---|---|
| §1 | 256 | Foundations — Formal Definitions and Primitives | `sec-1-foundations` | — (but contains an orphan h3 `C.2.1 Per-category profiles` at line 460 whose conceptual parent C.2 sits in §6) |
| §2 | 539 | Two-Instrument Architecture (CSD ↔ B₁; RCV ↔ B₂) | `sec-2-two-instrument-architecture` | — |
| §3 | 642 | RCV Quantification — Three Ways of Counting | `sec-3-rcv-quantification` | **Section B / B.1 / B.2** (h3s at lines 647, 670 use letter labels; methods §3.1–§3.4 use numeric) |
| §4 | 1044 | Hotelling Identity (extension of Hotelling 1931) | `sec-4-hotelling-identity` | — |
| §5 | 1118 | Accountability Bond Decomposition (B = B₁ + B₂; Restitution + Foreclosure Bonds) | `sec-5-accountability-bond-decomposition` | — |
| §6 | 1245 | Commons Inversion Test (CIT) | `sec-6-commons-inversion-test` | **Section C / C.1 / C.2 / C.3** (h3s at lines 1252, 1258, 1306) plus numeric §6.1, §6.1.1, §6.1.2, §6.2, §6.3 |
| §7 | 2315 | Four Gates Admission Apparatus | `sec-7-four-gates` | **Section L / L.1–L.7** (h3s at lines 2347–2718; gates L.1 = CIT-grounded, L.2 = units, L.3 = boundedness, L.4 = independence; L.5 protocol; L.6 worked example; L.7 prior-methodology bridge) |
| §8 | 2738 | Asymmetric Regret Rule (ARR) | `sec-8-asymmetric-regret-rule` | **G.2** orphan (h3 at line 2777 says "G.2 The Asymmetric Regret Decision Rule"; conceptual parent G sits in §13); plus numeric §8.1, §8.2 |
| §9 | 2838 | Three-Model Convergence Framework | `sec-9-three-model-convergence` | **Section D / D.1–D.6** (h3s at lines 2842–3049) |
| §10 | 3056 | Theorems and Proofs | `sec-10-theorems-and-proofs` | **Section E** by implication (theorems labelled E.1, E.1a, E.1b, E.2, E.3, E.4, E.5 — see Theorem section below); no h3 uses "E.X" as subsection label |
| §11 | 3633 | Empirical Validation Cases | `sec-11-empirical-validation` | **Section H / H.1–H.4** (case-preface h3s at lines 3643–3763) PLUS numeric §11.1–§11.7 (calibration-block h3s at lines 3797–5981); BOTH schemes coexist in one section |
| §12 | 6048 | Boundary-Awareness Scope Claim (Mars/Europa illustrations) | `sec-12-boundary-awareness-scope-claim` | — |
| §13 | 6164 | Substitutability Function (S) + Industrial-Existential Substitutability Gap | `sec-13-substitutability-function-and-gap` | **Section G / G.1 / G.3 / G.4** (h3s at lines 6175, 6286, 6292; note G.2 is missing here — it's the orphan in §8) |
| §14 | 6311 | Engagement with Existing Literature | `sec-14-literature-engagement` | **Section I / I.1–I.7** (h3s at lines 6321–6402) |
| §15 | 6412 | Limitations and Boundary Conditions | `sec-15-limitations` | — (uses numeric §15.1, §15.2 + sub-IDs §15.1.1–§15.1.9, §15.2.1–§15.2.3) |
| §16 | 7118 | Mathematical Extensions | `sec-16-mathematical-extensions` | **Section K / K.1–K.4** (h3s at lines 7122–7161) |
| §17 | 7313 | Formula Generalization — Sum-of-Costs Form | `sec-17-formula-generalization` | **Section M / M.0–M.7** (h3s at lines 7317–7491) |
| §18 | 7502 | Bibliography | `sec-18-bibliography` | — |

**Observations:**
- 10 of 18 sections carry a letter alias (B, C, D, E, G, H, I, K, L, M). Letters A, F, J are entirely absent from h3 labels.
- Letters do not align with numeric order at all: alphabetical "B → L → M" maps to numeric "§3 → §7 → §17". The letter scheme appears to be a *legacy organization* that pre-dated the current §1–§18 numeric reorganization.
- Six of those ten sections have h3 contamination *within* a single section (mix of letter + numeric h3 sequence): §3 (B.1, B.2, then §3.1–§3.4), §6 (C.1–C.3 + §6.1–§6.3), §8 (G.2 + §8.1–§8.2), §11 (H.1–H.4 + §11.1–§11.7).

---

## Cross-reference catalog (body prose)

Letter references found in body prose with target → numeric mapping inferred from context:

| Reference text | Occurrences | Numeric target | Confidence |
|---|---|---|---|
| `Section B` | 1 | §3 (or §2 — see open question) | medium |
| `Section B.1` | 9+ | §3 (h3 "B.1 Core Formula") | high |
| `Section C` | 1 (line 2724 "CIT") | §6 | high |
| `Section D` | 1 (line 3191 "Model Independence Defense") | §9 | high |
| `Section E` | 1 (line 2730 "Theorem E.4 in Section E on RCV integral convergence") | §10 | high |
| `Section F` | 4 occurrences (lines 3179, 3185, 3278, 3336) | §13 — but no h3 carries F.X label (the §13 h3s use G.1, G.3, G.4 instead). **"Section F" is an orphan pointer; conceptually it means §13 / Substitutability + Gap.** | medium |
| `Section H` | 8 occurrences | §11 (matches H.1–H.4 h3s) | high |
| `Section K.1` | 2 | §16.1 (h3 "K.1 RCV with Variable Discount Rates") | high |
| `Section K.3` | 2 | §16.3 (h3 "K.3 Spatial cost severance formalization") | high |
| `Section L` | 2 (line 347 "rhetorical anchor"; line 7321 "specifies four gates") | §7 (h3s L.1–L.7) | high |
| `Section L.6` | 1 (line 7480 "worked example") | §7 (h3 "L.6 Worked Example — Adding Community-Transition-Reserve Cost") | high |
| `Section M` | 2 (lines 2733, line 7321 "presents the corresponding mathematical generalization") | §17 (h3s M.0–M.7) | high |
| `Section M.5` | 1 (line 7354 "worked explicitly in Section M.5 below") | §17.5 (h3 "M.5 Worked Derivation") | high |

**Theorem references** (Section E content):

| Theorem | Body label | Numeric target if folded under §10 |
|---|---|---|
| Theorem E.1 (Structural Cost Severance) | line 679, 7167 | Theorem 10.1 |
| Theorem E.1a (lemma) | line 3167 | Theorem 10.1a |
| Theorem E.1b (empirical) | line 3173 | Theorem 10.1b |
| E.2 (acknowledged as empirical observation not theorem) | line 3209 | (no rename needed if labeled "Empirical Observation §10.2") |
| Theorem E.3 (Abundance Masking) | line 3251 + others | Theorem 10.3 |
| Theorem E.4 (RCV integral convergence under Weitzman discounting) | line 2730 + others | Theorem 10.4 |
| Theorem E.5 | line 3209 (referenced) | Theorem 10.5 |

---

## Orphan letters (cross-section letter-h3 misplacement)

Two cases where a letter-prefix h3 lives in the "wrong" numeric parent:

1. **`C.2.1 Per-category profiles`** at line 459–460 — sits inside §1 (Foundations). The parent C.2 ("The Seven Abundance Dimensions") is at line 1258 in §6 (CIT). Topically C.2.1's content (per-category commons profiles like Habitability, Bodily-integrity etc.) is more closely related to the §1 foundational primitives than to §6's CIT machinery — so the orphan is forward-looking (named C.2.1 because it surfaces categories that C.2 will later operate on). Either rename C.2.1 to §1.X, or move the content to §6 as §6.X, or accept the cross-section dependency.

2. **`G.2 The Asymmetric Regret Decision Rule`** at line 2777–2778 — sits inside §8 (ARR). Conceptual parent G ("Resource Classification" / Substitutability) is at §13. G.2 is the ARR's connection point to substitutability classification; the letter label is a stale cross-conceptual marker. Recommendation: drop the G.2 label; the §8.1 + §8.2 h3s already cover the same content.

---

## Embedded "supplement" §-numbering scheme (NEW — not flagged in handoff)

h4 headings inside §6.3 and §11.X clusters re-use the § symbol for *locally restarted* enumerations:

**Inside §6.3 (Worked Examples — Seven Walkthroughs):** h4 sequence §0, §1, §2, §3, §4, §5, §6, §7, §8 (lines 1620, 1664, 1716, 1766, 1829, 1913, 1978, 2050, 2149). These are the seven case walkthroughs plus a §0 system-overview and §8 cross-cutting findings. The §-symbol is a numbered-list bullet, not a section reference.

**Inside §11 (Empirical Validation Cases):** h4 sequence varies by sub-block — §11.1 has h4 §1 (Norway calibration); §11.2 has h4 §2 (Appalachian coal); §11.3 has h4 §3 (CSD-RCV correlation); §11.4 has h4 §3 (Sensitivity findings — COLLIDES with §11.3's §3); §11.5 has h4 §1 (DAC anchor); §11.6 has h4 §2 (Space-economics anchors). The numbering is incoherent across §11.

**Body prose references to "supplement":**
- Line 4086: `Method 3 prices the scarcity-adjusted option value per supplement §3.3 + sensitivity analysis §3.2 (calibrated parameters for Norway).`
- Line 4868 (THE PUZZLE): `the empirical companion to the Asymmetric Regret Rule's irreversibility-weighting (§8 / supplement §7).`
- Line 5003: `Method 3 estimates for the framework's three named calibration anchors per supplement §3.3 worked-example`
- Line 5201–5204: `Tech Appendix supplement §3.1 anchor` … `The supplement §3.1 (Method 1 Replacement Cost)`
- Line 5496: `§1.3 Recommended Method 1 anchor specification (for Tech Appendix supplement §3.1 + Ch 6 main-text integration)`

**Working interpretation:** "supplement §X.Y" appears to be a stale pointer to a previously separate Empirical Validation supplement document whose content was merged into §11 of the main appendix. Once merged, the "supplement §3.1" references should point to §11.X (whichever sub-block carries the DAC / Method 1 anchor — appears to be §11.5 at line 5189). The §11.4 internal h4 "§3. Sensitivity findings" is the local-bullet artifact, not the supplement target.

**Specific resolution proposed for line 4868 (the puzzle):** The sentence is contrasting ARR (top-level §8) against the empirical sensitivity analysis (§11.4 "Method 3 sensitivity analysis — α-dominance finding"). Best reading: `(§8 / §11.4)` — same structural insight at decision-rule level vs. sensitivity-analysis level. The "supplement §7" appears to be a stale legacy pointer to a §7 internal to a now-absorbed supplement structure; given that §11 has only seven h3 blocks (§11.1–§11.7), and §11.4 is the α-dominance finding, the "§7" likely meant "§11.7" or — more plausibly — was renumbered out of existence when the supplement merged in. **STOP and ask author** before resolving.

---

## Theorem numbering — observation + options

§10 (Theorems and Proofs) contains seven theorem-class statements: E.1, E.1a, E.1b, E.2 (acknowledged as empirical observation, not theorem), E.3, E.4, E.5. All carry the "E." letter prefix; no §10.X numbering currently in use for theorems.

**Two coherent options for the author to pick from:**

- **(a) Fold under numeric.** Rename to Theorem 10.1, 10.1a, 10.1b, 10.2 (observation), 10.3, 10.4, 10.5. Pure consistency with §1–§18; cleanest reader-side.
- **(b) Keep letter prefix as a deliberate semantic marker.** Theorems retain the "E.X" prefix where E corresponds to §10 explicitly (i.e., "Theorem E.1" with footnote/header note "Theorems are numbered E.X with E corresponding to §10 of this appendix"). Preserves the audit trail of where E.1 / E.3 are already cited externally (chapter cross-references, Noema essay draft) without requiring downstream re-citation.

The letter prefix has external-citation cost: chapter cross-references (Ch 7 line 119) currently use "Theorem E.3". External citations in the Noema essay and any pending publisher-facing material would need to update if option (a) is selected.

Recommendation: **option (b) — keep E.X with explicit alignment note.** Theorem-letter prefixes are a stable academic-citation convention; folding to numeric is gratuitous churn for the trade-press lookup affordance gain (small). The dual-audience layman+specialist test (per `feedback_dual_audience_test.md`) tilts toward (b): named theorems with stable identifiers serve both audiences.

---

## Canonical scheme — recommendation

**Adopt the numeric §1–§18 scheme as canonical for all section + subsection labels.** Specifically:

1. **Top-level h2** — no change. Already canonical.
2. **HTML anchor IDs** — no change. Already canonical.
3. **h3 subsections** — rename letter-prefix h3s to their numeric equivalent (B.1 → §3.1; C.2 → §6.X; D.1 → §9.1; G.1 → §13.1; H.1 → §11.X; I.1 → §14.1; K.1 → §16.1; L.1 → §7.1; M.0 → §17.0). Where a section already has *both* letter h3s and numeric h3s (§3, §6, §8, §11), the letter h3s integrate into the numeric sequence (e.g., §3's B.1 + B.2 + §3.1 + §3.2 + §3.3 + §3.4 becomes §3.1 Core Formula, §3.2 IPG, §3.3 Method 1, §3.4 Method 2, §3.5 Method 3, §3.6 Triangulation — preserves topical order).
4. **Body prose cross-references** — replace every "Section X" / "Section X.Y" letter reference with the numeric equivalent (e.g., "Section B.1" → "§3.1"; "Section L" → "§7"; "Section K.1" → "§16.1"). Update via grep+replace pass.
5. **Theorem labels** — recommend keeping "Theorem E.X" with explicit alignment note (per Option (b) above); author may override to Option (a).
6. **Embedded "supplement §X" body references** — resolve case-by-case to the correct §11.X target. Drop the word "supplement" from the reference (e.g., "supplement §3.1" → "§11.5" where §11.5 carries the DAC anchor). The h4 "§N" local bullets inside §6.3 + §11.X stay (they're a numbered-list convention, not section labels) — but consider switching the symbol from `§` to a plain number or letter to disambiguate.
7. **HTML anchor compatibility** — the existing `id="sec-N-..."` anchors stay; no backward-compatibility redirects needed (no external publications cite letter-system anchors as URLs).

---

## Open questions for author ratification (STOP gate)

Three judgment calls Phase 1 cannot resolve. STOP and ask the author before any Phase 3 editing:

### Q1. Line 4868 "supplement §7" intent

`(§8 / supplement §7)` at line 4868 sits inside §11.4 (Method 3 sensitivity analysis). Reading the surrounding paragraph, the sentence contrasts ARR irreversibility-weighting (§8) against the empirical α-dominance finding (Method 3 sensitivity). **Question:** does "supplement §7" mean:
- (a) §11.7 (IPG-table reconciliation) — the seventh §11.X block?
- (b) §7 (Four Gates Admission Apparatus) — top-level, if "supplement" was meant as a hedge word ("§8 alongside the §7 supplementary framing")?
- (c) A stale legacy pointer to a §7 in a now-absorbed pre-merger supplement document — should just be deleted?

Working hypothesis (c) but author judgment required.

### Q2. Theorem numbering — fold to numeric or keep E.X with alignment note?

Recommended Option (b) — keep "Theorem E.X" with explicit "(where E corresponds to §10 of this appendix)" alignment note. Author may override to Option (a) [fold to Theorem 10.1, 10.1a, etc.]. The cost of switching to (a) is updating Ch 7 line 119 and the Noema essay draft cross-references; the benefit is full numeric consistency.

### Q3. Orphan h3 `C.2.1 Per-category profiles` (in §1)

Three resolution options:
- (a) Rename the h3 to a §1 numeric label (e.g., §1.4 "Per-category commons profiles") and keep the content in §1.
- (b) Move the content out of §1 and into §6 (CIT) as §6.X (since C.2 = §6.2 "Seven Abundance Dimensions" topically parents it).
- (c) Both — split into a §1 foundational-categories overview and a §6 per-category profile mapping.

§1 is "Foundations — Formal Definitions and Primitives". The 460-line C.2.1 content is per-category commons profiles (Habitability, Bodily-integrity, etc.) — feels more like §1 foundational material than §6 methodology, so (a) is the lighter touch. Author judgment.

### (Lower-priority, can apply without separate gate)

- The orphan G.2 in §8 — recommend dropping the G.2 label since §8.1 + §8.2 already cover the content; the G.2 wrapper is purely vestigial.
- The "Section F" / "Section H" / etc. cross-reference replacements — mechanical once canonical scheme is ratified.

---

## Effort estimate

After author ratification:

- **Phase 3 (appendix-internal application):** ~60–90 minutes of focused editing. ~30 h3 renames + ~30 body-prose cross-reference replacements + 1 puzzle resolution (line 4868) + 1 orphan handling (C.2.1) + 1 G.2 cleanup.
- **Phase 4 (chapter cross-reference re-validation):** TBD — depends on how many chapter references the canonical scheme touches. Chapter file scan happens after Phase 3 lands.
- **Phase 5 (layman-lookup format application):** ~30 minutes assuming the format candidate `[Named Concept] (Technical Appendix §X.Y)` is ratified.

Recommend Phase 3 as one commit, Phase 4 as per-chapter chunked commits, Phase 5 as one final consistency commit.

---

## What I did NOT find (negative findings)

- No third-party / external documents currently cite letter-system anchors as URLs (verified by `grep` of letter references — all are internal). Backward-compatibility redirects unnecessary.
- No `<h3 id="...">` attributes carry letter-prefix IDs (verified at line 6752 `sec-15-2-methodological-framing` — the one h3 with an explicit ID uses numeric form). So Phase 3 doesn't need anchor-ID renames; only heading-text renames.
- No glossary references to letter sections (separate verification recommended once Phase 3 lands — glossary v4 audit is a downstream workstream).
- Theorem statements + proofs themselves untouched by this audit (per hard constraint).

---

*End of Phase 1 audit inventory. **STOP at the author ratification gate** before Phase 3 edits begin. Three judgment calls (Q1–Q3) require explicit author input. Canonical-scheme recommendation: numeric §1–§18, Option (b) theorem retention, Option (a) orphan resolution.*
