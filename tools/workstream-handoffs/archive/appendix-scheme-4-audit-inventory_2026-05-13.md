# Tech Appendix Scheme-4 Cleanup — Phase 1 Audit Inventory — 2026-05-13

**Source file audited:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (post-#15 numbering reconciliation; HEAD commit `8873347` on `origin/main` as of audit start)

**Scope:** Locally-restarted §-symbol h4/h5 headers inside §6.6 (Worked Examples — Seven Walkthroughs) and §11.5–§11.11 (Empirical Validation Cases) + body cross-references that resolve to those local-restart labels rather than the canonical top-level §X.Y scheme.

**Read-only audit.** Author ratification gate required before Phase 3 application.

**Verification stance:** All line numbers verified via grep against current file state on 2026-05-13.

---

## Section 1 — §6.6 Worked Examples (h4 + h5 catalog)

§6.6 (Worked Examples: Seven Walkthroughs) sits at h3 line 1670. h4s inside it use a local-restart §0–§8 sequence:

| Line | Current label | Parent h3 | Topic |
|---|---|---|---|
| 1679 | §0. The Four Gates as a system | §6.6 | System-overview framing |
| 1723 | §1. McDowell County coal: Black Lung healthcare cost | §6.6 | Walkthrough — Appalachian coal |
| 1775 | §2. The commute trade (Personal Stories Candidate #1): foregone-life-time cost | §6.6 | Walkthrough — commute trade |
| 1825 | §3. Norwegian oil extraction: future-generation climate damage | §6.6 | Walkthrough — Norway oil |
| 1888 | §4. 2008 financial crisis: institutional-commons damage with multi-stream Independence-gate exercise | §6.6 | Walkthrough — 2008 crisis |
| 1972 | §5. The asteroid miner (Ch 7 Mars habitat / Europa thought-experiment): multi-commons absent simultaneously | §6.6 | Walkthrough — asteroid miner |
| 2037 | §6. Healthcare end-of-life (Butler pacemaker case): Commons-Consumption applied to medical-commons | §6.6 | Walkthrough — healthcare end-of-life |
| 2109 | §7. Opioid Appalachia (Sackler / Purdue Pharma): documented extraction with multi-commons damage + both CIT sub-forms simultaneously | §6.6 | Walkthrough — opioids |
| 2208 | §8. Cross-cutting findings across all 7 walkthroughs | §6.6 | Cross-cutting findings |

h5s nested under §6.6 §8 (lines 2211, 2246, 2328, 2342, 2351) are named-only — no §-prefix. **Already clean.** No action required for h5 in §6.6.

**§6.6 total: 9 h4 renames (no h5 renames needed).**

---

## Section 2 — §11.5–§11.11 Empirical Validation Cases (h4 + h5 catalog)

### §11.5 — Norway petroleum calibration (h3 line 3857)

| Line | Current label | Type |
|---|---|---|
| 3863 | §1. Norway calibration — Three Ways of Counting executed | h4 |
| 3866 | §1.1 Empirical anchors (Norway petroleum extraction, 1971–present) | h5 |
| 3998 | §1.2 Method 1 — Replacement Cost (lower-bound floor for Habitability commons) | h5 |
| 4073 | §1.3 Method 2 — Norway Revealed Preference (anchor; what Norway actually internalized) | h5 |
| 4138 | §1.4 Method 3 — Scarcity-Adjusted Option Value (upper bound) | h5 |
| 4211 | §1.5 Triangulation findings for Norway | h5 |

### §11.6 — Appalachian coal calibration (h3 line 4306)

| Line | Current label | Type |
|---|---|---|
| 4312 | §2. Appalachian coal calibration — Three Ways of Counting executed | h4 |
| 4315 | §2.1 Empirical anchors (McDowell County, West Virginia, 1900-2020) | h5 |
| 4452 | §2.2 Method 1 — Replacement Cost (lower-bound floor) | h5 |
| 4511 | §2.3 Method 2 — Revealed Preference (anchor) | h5 |
| 4566 | §2.4 Method 3 — Scarcity-Adjusted Option Value (upper bound) | h5 |
| 4636 | §2.5 Triangulation findings for McDowell coal | h5 |

### §11.7 — CSD-RCV correlation hypothesis test (h3 line 4745)

| Line | Current label | Type |
|---|---|---|
| 4753 | §3. CSD-RCV correlation hypothesis test (Open Insight #19) | h4 |
| 4764 | §3.1 The two-case test | h5 |
| 4803 | §3.2 What the two-case test shows | h5 |
| 4839 | §3.3 Implications | h5 |

### §11.8 — Method 3 sensitivity analysis (h3 line 4904)

**Collision case** — h4 §3 reused here despite §11.7 §3:

| Line | Current label | Type |
|---|---|---|
| 4930 | §3. Sensitivity findings | h4 |
| 4933 | §3.1 Dominance map | h5 |
| 5058 | §3.2 Worked-example application (using framework's three calibration cases) | h5 |
| 5139 | §3.3 Cross-case dominance pattern | h5 |
| 5181 | §3.4 Sensitivity to β (irreversibility-aversion calibration) | h5 |
| 5194 | §4. Implications for framework debate-narrowing | h4 |

### §11.9 — DAC three-horizon range (h3 line 5249)

| Line | Current label | Type |
|---|---|---|
| 5259 | §1. Direct-air-capture (DAC) cost per ton CO₂ — Tech Appendix supplement §3.1 anchor | h4 |
| 5265 | §1.1 Operational DAC facilities (2024-2025 cost figures) | h5 |
| 5414 | §1.2 Authoritative review-literature ranges | h5 |
| 5554 | §1.3 Recommended Method 1 anchor specification (for Tech Appendix supplement §3.1 + Ch 6 main-text integration) | h5 |

### §11.10 — Space-economics anchors (h3 line 5602)

| Line | Current label | Type |
|---|---|---|
| 5611 | §2. Space-economics numerical anchors — Ch 7 (asteroid miner) calibration | h4 |
| 5617 | §2.1 Launch-cost anchors (Earth-to-LEO and Earth-to-GTO) | h5 |
| 5736 | §2.2 Asteroid sample-return mission costs (per gram returned) | h5 |
| 5855 | §2.3 Asteroid-mining commercial-proposal cost estimates (for context) | h5 |
| 5937 | §2.4 Mars surface-operations cost reference (for thought-experiment grounding) | h5 |

### §11.11 — IPG-table reconciliation (h3 line 6041)

**No h4 or h5. Clean.**

**§11 total: 10 h4 renames + 22 h5 renames + the §11.9 h4 label carries a body-ref-style trailing pointer that also needs rewriting.**

---

## Section 3 — Body cross-reference catalog

References to Scheme-4 local-restart labels inside the Tech Appendix:

| Line | Context | Reference text | Resolves to |
|---|---|---|---|
| 837 | §3.4 Method 2 prose | `per Block 4 validation §1.3 numerical execution` | §11.5 §1.3 (Norway Method 2 calibration h5) |
| 4145 | §11.5 §1.4 Method 3 prose | `Method 3 prices the scarcity-adjusted option value per supplement §3.3 + sensitivity analysis §3.2 (calibrated parameters for Norway)` | `§3.3` and `§3.2` resolve to §11.8 §3.3 (Cross-case dominance pattern) + §11.8 §3.2 (Worked-example application). NOT the top-level §3.3 (Method 1: Replacement Cost) or §3.2 (IPG). |
| 5062 | §11.8 §3.2 Worked-example application prose | `Method 3 estimates for the framework's three named calibration anchors per supplement §3.3 worked-example` | §11.8 §3.3 (Cross-case dominance pattern) |
| 5260 | §11.9 §1 h4 trailing pointer | `Tech Appendix supplement §3.1 anchor` (part of the heading itself) | The "supplement §3.1" appears to point to §11.5 §1.2 (Method 1 — Replacement Cost for Norway), since the DAC anchor is the Method 1 substitution-side anchor. **Stale legacy pointer from pre-merger supplement document.** |
| 5263 | §11.9 §1 body prose | `The supplement §3.1 (Method 1 Replacement Cost) uses DAC cost-per-ton…` | Same as 5260 — refers to §11.5 §1.2 / §11.6 §2.2 (the Method 1 Replacement Cost h5s) or topically to top-level §3.3 (Method 1: Replacement Cost). |
| 5555 | §11.9 §1.3 h5 heading | `§1.3 Recommended Method 1 anchor specification (for Tech Appendix supplement §3.1 + Ch 6 main-text integration)` | "supplement §3.1" same as above |

**Total body refs to rewrite: 6 (one of which is embedded in an h4 heading; one in an h5 heading).**

---

## Section 4 — External (chapter-side) cross-reference scan

**Searched:** `manuscript/chapters/*Draft*` (active drafts only) for `supplement §`, `Tech Appendix §X.Y`, `Technical Appendix §X.Y`.

**Findings:** Zero active-draft chapter references to Scheme-4 local-restart labels. Only `Chapter__4___GuidanceDoc.md` references "Tech Appendix §L methodological footnote" — a residual letter-scheme reference left over from workstream #15 (§L → §7 in canonical scheme); this is meta-doc / internal-scaffolding, NOT a chapter draft. Out of Scheme-4 scope.

**Scheme-4 cleanup is fully internal to the Tech Appendix file.** No chapter-side coordination required.

---

## Section 5 — Collision + ambiguity findings

1. **§11.7 §3 vs §11.8 §3 collision** (confirmed in handoff). h4 §3 means "CSD-RCV correlation hypothesis test" inside §11.7 but "Sensitivity findings" inside §11.8. Body refs to "§3.X" inside §11.5–§11.8 cannot disambiguate from context alone without canonical-scheme rewrite.

2. **§3.1/§3.2/§3.3 collide with top-level §3.X subsections.** Top-level §3 (RCV Quantification) has §3.1 (Core Formula), §3.2 (IPG), §3.3 (Method 1: Replacement Cost), §3.4 (Method 2), §3.5 (Method 3), §3.6 (Triangulation). Local-restart §3.X labels inside §11.7 + §11.8 + §11.9 (and via "supplement §3.X" body refs) are formally ambiguous.

3. **§1.X / §2.X collide with top-level §1.X / §2.X.** Top-level §1 (Foundations) has §1.10 currently. Top-level §2 (Two-Instrument Architecture) has §2.1, §2.2. Local-restart §1.X labels inside §11.5 + §11.9; §2.X labels inside §11.6 + §11.10. Ambiguity is mostly latent (no top-level §1.1–§1.5 or §2.3–§2.5 currently exist), but the §-symbol still falsely suggests top-level pointer.

---

## Section 6 — Effort estimate (Phase 3)

- §6.6 h4 renames: 9 edits
- §11.5–§11.10 h4 renames: 10 edits (includes §11.7 §3, §11.8 §3 + §11.8 §4, §11.9 §1, §11.10 §2)
- §11.5–§11.10 h5 renames: 22 edits
- Body cross-ref rewrites: 6 edits (4 prose + 2 embedded in heading text)
- **Total mechanical edits: ~47**

Phase 3 should be 30–60 minutes of focused editing once the author ratifies the cleanup option + body-ref rewrite style.

---

## Section 7 — Open questions for author ratification (Phase 2 gate)

### Q1. Option A / B / C for §11.5–§11.10 sub-headers?

- **Option A** (recommended) — strip §-prefix entirely. `§1. Norway calibration` → `Norway calibration`; `§1.1 Empirical anchors` → `Empirical anchors`. Cleanest. Headers become named-only.
- **Option B** — renumber to hierarchical §X.Y.Z. `§1.1 Empirical anchors` → `§11.5.1 Empirical anchors`. Preserves enumeration but pushes notation to 4-deep numbering everywhere.
- **Option C** — letter prefix (Case A / Case B / …). Reintroduces letter scheme that workstream #15 rejected. Not recommended.

**Audit recommendation: Option A** for §11.5–§11.10 sub-headers. Eliminates ambiguity. Body refs then rewrite descriptively (e.g., "the cross-case dominance pattern documented in §11.8" rather than "supplement §3.3").

### Q2. §6.6 walkthrough headers handling?

- **Option A1** — strip §-prefix; named-only. `§1. McDowell County coal: Black Lung healthcare cost` → `McDowell County coal: Black Lung healthcare cost`.
- **Option A2** — descriptive enumeration prefix (recommended). `§1. McDowell County coal: Black Lung healthcare cost` → `Walkthrough 1. McDowell County coal: Black Lung healthcare cost`. Preserves the count-discipline ("seven walkthroughs") that the chapter title flags, without the false §-reference. `§0` and `§8` get `Overview.` and `Cross-cutting findings.` (descriptive, no enumeration number).

**Audit recommendation: Option A2** for §6.6 — "Walkthrough N. <case>" preserves the enumeration affordance that the section title ("Seven Walkthroughs") promises, with no §-symbol ambiguity.

### Q3. Body-ref rewrite style?

Six body refs to rewrite. Two styles:

- **Descriptive form** (recommended): rewrite each ref as a content-pointer, dropping the local-restart §X.Y label. Examples:
  - Line 837: `per Block 4 validation §1.3 numerical execution` → `per the Norway Method 2 calibration in §11.5 (Norway Revealed Preference)` or `per Norway Revealed Preference calibration (§11.5)`
  - Line 4145: `per supplement §3.3 + sensitivity analysis §3.2` → `per the cross-case dominance finding in §11.8 + worked-example application also in §11.8`
  - Line 5062: `per supplement §3.3 worked-example` → `per the cross-case dominance pattern in §11.8`
  - Line 5260 (in h4): trailing `— Tech Appendix supplement §3.1 anchor` → drop the trailing pointer (DAC anchor's role is established by the h3 + body prose); or rewrite to `— Method 1 Replacement Cost anchor for the Habitability commons`
  - Line 5263: `The supplement §3.1 (Method 1 Replacement Cost) uses DAC…` → `Method 1 (Replacement Cost; canonically defined in §3.3) uses DAC cost-per-ton as the worked-example anchor…` (rewrites the stale "supplement" pointer to the canonical Method 1 home in top-level §3.3)
  - Line 5555 (in h5): trailing `(for Tech Appendix supplement §3.1 + Ch 6 main-text integration)` → `(for Method 1 integration with Ch 6 main-text)`
- **Preserve-and-disambiguate form**: keep local labels but add disambiguating context every time. Verbose; preserves audit trail; not recommended.

**Audit recommendation: descriptive form** — cleaner; aligns with workstream #15's canonical-scheme adoption.

---

## Section 8 — Hard constraints recap

- Do NOT touch theorem statements or proofs (none in §6.6 / §11.X scope; precaution holds).
- Do NOT reintroduce a parallel scheme. Cleanup is canonical-numeric-only.
- Do NOT change content of h4/h5 sections; only labels + body refs.
- Two-layer content origination (WP#10) — Tech Appendix is internal-scaffolding; cleanup is internal hygiene. No external-publisher-facing impact.
- Verify-stale-memory-claims — line numbers above verified 2026-05-13.

---

*End of Phase 1 audit inventory. STOP at the author ratification gate. Three judgment calls (Q1–Q3) require explicit author input before Phase 3 editing begins.*
