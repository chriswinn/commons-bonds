# Commons Bonds — Session Handoff v1.46.0

**Date:** 2026-04-27 (continuation of same calendar day as v1.45.0)
**Branch:** `claude/hardcore-golick-8920ec` (worktree pushing to `origin/main`)
**Status:** Open Insight #21 Path B — all 7 Tech Appendix scope items complete (v0.0.5 → v1.0.0, `CURRENT` status); Chapter 6 HTML format conversion complete + Phase B supplementary passages appended; structural placement of Ch 6 supplementary passages pending author next-pass work. Open Insight #22 closed-ratified (chapter-titles-in-sweep-scope memory rule + Open Insights file updated).

---

## §1. Copy-paste block for next session orientation

> *Copy the block below into the next session's first message to orient Claude with full project context.*

```
SESSION CONTEXT — Commons Bonds (Book 1)

PROJECT IDENTITY:
This is Chris Winn's Commons Bonds project — a framework book on cost-severance / value-extraction economics. Book 1 is framework-naming + framework-establishment; Book 2 (applied-advocacy) is explicitly NOT mentioned in Book 1 per Insight #24 closed-ratified 2026-04-27.

WHERE WE ARE (post-2026-04-27 v1.46.0 session):
Tech Appendix v1.0.0 is the CURRENT publication-ready document (replacing v0.0.5; archived v0.0.3 + v0.0.5_supplement.md). Open Insight #21 Path B all 7 scope items complete; Insight #22 closed-ratified (chapter-titles in sweep scope). Drafted-chapter holistic reviews remain at the post-2026-04-27_v1.45.0 state for Ch 2 / Ch 4 / Ch 5 / Ch 7 / Ch 8 / Ch 9 / Ch 10 (per v1.45.0 handoff §3).

CHAPTER 6 STATE:
- Format conversion to Option A pretty-printed semantic HTML complete (Scope 7 of Path B).
- Phase B supplementary passages from `manuscript/chapters/Chapter__6___SupplementaryDrafts_2026-04-24.md` appended in a clearly-marked "phase-b-supplementary-passages" section at end of file.
- 13 passages staged: Passage A (CIT intro replacing AIT); Passage B (10 commons as examples); Passage C (political-philosophical acknowledgment); Passage D (autonomy-as-commons); Passage E (commons-governance lineage); Passage F (Tech Appendix reference); §6.5 Parfit engagement; §6.6 CIT-vs-empirical falsifiability; §6.7 IPG-table reconciliation; §6.8 DAC three-horizon; §6.9 Ostrom-vs-extraction; §6.10 reparations-economics; §6.11 methodology defense.
- Structural placement of the 13 passages within chapter body is pending author judgment (~5,000 words of staged content; placement guidance in supplementary drafts §N.M.2 integration notes).

NOT YET DRAFTED:
- Ch 1 (untitled) — 1,446 words, partial; awaits author personal-stories drafting cycle (Path F per memory rule).
- Ch 3 (TBD — waterman protagonist) — not drafted; cross-referenced from Ch 8/9/10.

OPEN INSIGHTS STATUS (post-v1.46.0):
- #21 (Tech Appendix v0.0.5 + Ch 6 HTML full-rewrite, Option A pretty-printed semantic HTML) — Tech Appendix v1.0.0 (CURRENT) ✓; Ch 6 HTML format conversion ✓; structural integration of Ch 6 supplementary passages into chapter body PENDING author placement work.
- #22 (chapter-titles-in-sweep-scope) — closed-ratified 2026-04-27 (memory rule updated).
- #23 (CTR boundary question) — closed-ratified 2026-04-27 (Path 2: Version G integrated Book-2-mention-free).
- #24 (Book 1 references to Book 2) — closed-ratified 2026-04-27 (Scenario B: all Book 2 references removed).

KEY MEMORY RULES TO RESPECT:
- Direct-to-main git workflow; push each commit as it lands.
- Chapter-by-chapter prose-sweep discipline (every prose element through three rigor questions; chapter titles + section headers in scope per Insight #22 update).
- Bibliography additions: add without asking if load-bearing on ratified decision.
- Terminology regression check on every read/edit.
- Handoff chapter-length tracking section in every session handoff.
- Personal stories drafting + Path K revisit gate.
- "Canonical" itself is RETIRED as truth-claim language per terms_index §0; use status indicators (CURRENT / PENDING-RIGOR / UNDER-REVIEW / SUPERSEDED / RETIRED) with rigor provenance instead.

IMMEDIATE CANDIDATE NEXT MOVES:
- Ch 6 supplementary-passage structural integration (place each passage into chapter body per supplementary drafts §N.M.2 integration notes; per-passage commits; resolves vocabulary clashes with existing prose; ~13 small commits).
- Ch 6 holistic review (per the chapter-by-chapter prose-sweep discipline; would happen after structural integration lands).
- Project-wide vocabulary sweep continuation (Tier B research/case-studies/* + literature + remaining current docs from v1.45.0 §5.3 deferred list).
- Ch 3 (waterman) draft (largest content gap).
- Author personal stories drafting cycle (per memory rule; ongoing).
- Ch 2 interviews (3 INTERVIEW NEEDED placeholders).

RATIFIED FRAMEWORK STATE (reaffirmed):
- Ring-1 (7 terms): Commons Bonds · Cost Severance · Severed Cost · Value Extraction · CIT · RCV · Cᵢ.
- Ring-2 (key terms): Accountability Bond (B = B₁ + B₂) · CSD · Three Ways of Counting (Triangulated RCV Estimation) · Hotelling Identity · Asymmetric Regret Rule · Substitutability Function.
- Two-instrument architecture: CSD ↔ B₁ Restitution Bond (backward-looking; reparations-economics lineage); RCV ↔ B₂ Foreclosure Bond (forward-looking; option-value economics + Hartwick rule lineage).
- 8-tier scheme RETIRED 2026-04-24 (tier-reframing rigor pass §11; macro-grouping rejected per macro_grouping pass Option A).
- Commons categories: 10 examples (Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political, Cohesion, Epistemic, Autonomy) — UNIVERSALITY of method, EXAMPLES of application; Option C' political-philosophical-accommodation.

START THE NEXT SESSION BY: reading this handoff file (alignment/sessions/commons-bonds-session-handoff-2026-04-27_v1.46.0.md) for full context, then surfacing one of the candidate next moves above for author confirmation before execution.
```

---

## §2. Latest session work — detailed summary

### §2.1 Insight #22 closed-ratified

Memory rule `feedback_always_expand_rule.md` updated to add chapter titles + section headers to the chapter-by-chapter prose-sweep discipline. Three explicit checks specified for chapter titles: (1) Book-1/Book-2-split carry-over, (2) applied-advocacy vs framework-establishment register drift, (3) vocabulary regressions. When a title concern surfaces, a full chapter-title rigor pass is run following the same protocol as the Ch 7 + Ch 9 title rigor passes. MEMORY.md index hook updated. `alignment/commons_bonds_open_insights_v1.0.0.md` updated to mark Insight #22 closed-ratified.

Verification sweep across remaining chapter titles (Ch 2 / Ch 4 / Ch 5 / Ch 6 / Ch 8 / Ch 10) confirmed clean per the Ch 9 title rigor pass §10 set-rigor analysis at the time of raising. Ch 1 + Ch 3 titles will be rigor-tested when those chapters are drafted.

**Commit:** `f7532b2`.

### §2.2 Open Insight #21 Path B — Tech Appendix v0.0.5 → v1.0.0

All seven scope items completed across seven per-scope-item commits. Tech Appendix is now `CURRENT` at v1.0.0 with full Option A pretty-printed semantic HTML throughout, current architecture-aligned §1–§19 TOC, all retired vocabulary swept (FGC + Universality Test + Spatial CS proper-noun + AIT residue + L.1 "Abundance Inversion" + L.2 "Dimensional Consistency" + capitalized "Canonical" + Eight-Tier), §C.4 8-tier excised entirely (per Q3 = (a) excise), §K Mathematical Extensions verified clean of tier-coupled passages, §11 Empirical Validation expanded to seven sub-sections covering Block 4 + Method 3 + DAC + IPG-table + space-economics + CSD-RCV correlation hypothesis test, and the Phase B Ch 6 supplementary Tech-Appendix-marked passages integrated.

**Pre-flight ratifications** (author 2026-04-27):
- Q1 = (a) single linear TOC organized around current architecture
- Q2 = merges-as-proposed with Hotelling Identity attribution discipline (cite Hotelling 1931 as his work; framework's identity-articulation as framework's contribution)
- Q3 = (a) excise entirely (both §C.4 8-tier and tier-coupled §K passages)
- Q4 = file disposition as recommended (rename via `git mv`; archive v0.0.3 + v0.0.5_supplement; update supplement with retirement note)
- Q5 = duplicate (the seven CIT worked examples integrated into §6.3 of Tech Appendix as full-content embed; cit_examples_v1_0_0.md remains source-of-truth for maintenance per Working Principle #4)

**Per-scope commits:**

| Scope | Commit | Title |
|---|---|---|
| 1 | `fab0895` | Tech Appendix v0.0.5 → v1.0.0 (Option A pretty-printed semantic HTML; format-only conversion). File rename via `git mv`; archive setup; retired-classes-and-styles strip; clean semantic HTML throughout. |
| 2 | `bd2f662` | TOC restructure into §1–§19 architecture-aligned TOC + partial-integration block reconciled into proper structural locations + seven CIT worked examples embedded in §6.3. |
| 3 | `bc2d2cf` | Retired-vocabulary passage rewrites: L.1/L.2 gate headings to current names (CIT + Units Consistency); M.3 + M.5 + K.3 heading rewrites; §1 + §11 + §12 + §17 body passage cleanups. |
| 4 | `835bf7c` | §C.4 (8-tier FGC Decomposition) excised entirely (23 elements removed); §K Mathematical Extensions verified clean of tier-coupled passages. |
| 5 | `a9ace93` | §11 Empirical Validation Cases expanded with §11.1 Block 4 Norway + §11.2 Block 4 McDowell + §11.3 CSD-RCV correlation hypothesis + §11.4 Method 3 sensitivity (α-dominance) + §11.5 DAC three-horizon + §11.6 space-economics + §11.7 IPG-table reconciliation. |
| 6 | `8cade87` | Phase B Ch 6 supplementary integration into Tech Appendix: §5.4 Parfit footnote + §6.1.2 Domain distinction (verified) + §15.1 Methodology Defense Consolidation (compact summary; full academic-depth queued). |
| 7 | `86e3eea` | Chapter 6 HTML conversion to Option A semantic HTML + 13 Phase B supplementary passages appended in marked block pending author placement refinement. |

**Tech Appendix v1.0.0 final TOC:**

| § | Title | Provenance |
|---|---|---|
| §1 | Foundations — Formal Definitions and Primitives | old §A |
| §2 | Two-Instrument Architecture (CSD ↔ B₁; RCV ↔ B₂) | partial-integ §2 |
| §3 | RCV Quantification — Triangulated Estimation (Three Ways of Counting) | old §B + partial-integ §3 |
| §4 | Hotelling Identity (extension of Hotelling 1931) | partial-integ §5 |
| §5 | Accountability Bond Decomposition (B = B₁ + B₂; Restitution + Foreclosure Bonds) [+ §5.4 Parfit footnote per Scope 6] | partial-integ §4 + Phase B supplementary §6.5.2 |
| §6 | Commons Inversion Test (CIT) [+ §6.1.2 Domain distinction; §6.3 worked examples embedded] | old §C minus §C.4 + partial-integ §6 + supplementary §6.1.2 + cit_examples_v1_0_0.md |
| §7 | Four Gates Admission Apparatus | old §L |
| §8 | Asymmetric Regret Rule (ARR) | old §G.2 + partial-integ §7 |
| §9 | Three-Model Convergence Framework | old §D |
| §10 | Theorems and Proofs | old §E |
| §11 | Empirical Validation Cases [+ §11.1–§11.7 Block 4 + Method 3 + DAC + IPG] | old §H + Block 4 + Method 3 + empirical-sourcing pass docs |
| §12 | Boundary-Awareness Scope Claim (Mars/Europa illustrations) | old §F reframed |
| §13 | Substitutability Function (S) + industrial-existential substitutability gap | old §G.1 + G.3 + G.4 |
| §14 | Engagement with Existing Literature | old §I |
| §15 | Limitations and Boundary Conditions [+ §15.1 Methodology Defense Consolidation] | old §J + supplementary §6.11.2 |
| §16 | Mathematical Extensions | old §K |
| §17 | Formula Generalization — Sum-of-Costs Form | old §M |
| §18 | Working Principles + Open Insights Cross-Reference | synthesized |
| §19 | Provenance & Cross-References | synthesized; terms_index pointers |

**Tech Appendix v1.0.0 file size progression:**
- v0.0.5 baseline: 207 KB
- After Scope 1 (format conversion, A-M body in clean HTML; partial integration block preserved): 158 KB
- After Scope 2 (TOC restructure + cit_examples embedded): 212 KB
- After Scope 3 (retired-vocabulary rewrites): 211 KB
- After Scope 4 (§C.4 excise + §K verification): 201 KB
- After Scope 5 (§11 Empirical expanded with rigor-source-doc content): 270 KB
- After Scope 6 (Parfit + Methodology Defense): 278 KB

**Vocabulary regression discipline applied throughout:** "Canonical" retired as truth-claim language per terms_index §0 — every framework term carries explicit status indicators with rigor provenance instead.

### §2.3 Chapter 6 HTML format conversion + Phase B supplementary passages appended (Scope 7)

`Chapter__6_ThreeWaysofCounting__Draft.html` converted from Google Docs export styling to clean Option A pretty-printed semantic HTML matching Tech Appendix v1.0.0 conventions. All 12 chapter sub-sections preserved (Approach 1 — Bottom-Up Damage Accounting; Approach 2 — The Real Options Model; Approach 3 — The RCV Model; The Substitutability Function; The Convergence; The Norway Backtest; The Four Gates; The Contribution; What the Critics Will Say; The Carbon Concession; Reproducibility and the Range of Defensible Estimates; What the Chapter Leaves for Later).

Phase B supplementary passages from `manuscript/chapters/Chapter__6___SupplementaryDrafts_2026-04-24.md` appended as a clearly-marked `phase-b-supplementary-passages` section at end of file:

| § | Title | ~Words |
|---|---|---|
| §1 Passage A | CIT introduction (replaces existing AIT introduction) | 150 |
| §2 Passage B | The 10 commons categories presented as examples (NOT canonical scaffolding) | 150 |
| §3 Passage C | Political-philosophical acknowledgment (load-bearing for Option C') | 150 |
| §4 Passage D | Autonomy-as-commons specifically (most-contested example) | 150 |
| §5 Passage E | Commons-governance lineage extension to The Contribution section | 200 |
| §6 Passage F | Reference to Tech Appendix for full per-commons detail | 80 |
| §6.5 Passage G | Parfit engagement (intergenerational moral status) | 450 |
| §6.6 Passage H | CIT-vs-empirical falsifiability distinction (closes M11 Char 18) | 200 |
| §6.7 Passage I | IPG-table reconciliation | 280 |
| §6.8 Passage J | DAC three-horizon + SCC-vs-DAC distinction | 320 |
| §6.9 Passage L | Ostrom-vs-extraction-context distinction (closes M11 Char 17) | 520 |
| §6.10 Passage M | Reparations-economics main-text engagement (closes M11 Char 19) | 360 |
| §6.11 Passage N | Methodology defense consolidation (8 rationales) (closes M6.1) | 2000 |

Total ~5,000 words of framework-current Ch 6 main-text content staged. Author next-pass work: structural placement within chapter body per the per-passage `§N.M.2 Integration notes for Phase B` subsections in the supplementary drafts file.

**File size:** 61 KB → 130 KB (+69 KB Phase B supplementary passages appended).

---

## §3. Standing chapter-length tracking

| Ch | Title | Words | Pages | Target | Status | What's missing |
|---|---|:---:|:---:|:---:|---|---|
| 1 | (TBD) | 1,446 | ~5 | 5,000-6,000 | **PARTIAL DRAFT** | Personal-stories integration; awaits author drafting cycle (Path F per memory rule). |
| 2 | The Miner | 5,707 | ~21 | 5,000-6,000 | **COMPLETE — interviews pending** | 3 INTERVIEW NEEDED placeholders. |
| 3 | (TBD — waterman) | 0 | 0 | 5,000-6,000 | **NOT DRAFTED** | Full chapter draft; Chesapeake waterman protagonist per Ch 9 + Ch 10 cross-references. |
| 4 | The Existence Proof | 4,039 | ~15 | 5,000-6,000 | **COMPLETE — below target** | Could expand Norway/Nigeria detail; not blocking. |
| 5 | The Accountability Gap | 9,677 | ~36 | 5,000-6,000 | **COMPLETE — above target** | Nothing blocking. |
| 6 | Three Ways of Counting | 7,310 + ~5,000 staged supplementary = ~12,310 transitional | ~46 transitional | 6,000-8,000 | **FORMAT CONVERTED + SUPPLEMENTARY APPENDED** | Structural placement of 13 supplementary passages into chapter body (Scope 7 next-pass work). After placement, net word-count gain will be smaller (Passages A/B/C/D/E/F replace existing prose; §6.5–§6.11 additions are additive). |
| 7 | On Other Worlds | 7,404 | ~28 | 5,000-6,000 | **COMPLETE — above target** | Nothing pending. |
| 8 | What Things Actually Cost | 5,946 | ~22 | 5,000-6,000 | **COMPLETE — within target** | Nothing pending. |
| 9 | Pricing Honestly | 10,608 | ~39 | 5,000-6,000 | **COMPLETE — substantially above target** | Nothing pending. |
| 10 | Common Bonds | 7,661 | ~28 | 5,000-7,000 | **COMPLETE — within target** | Nothing pending. |
| **Total drafted (post-v1.46.0; transitional Ch 6 form)** | | **~64,798** | **~242** | | | |
| **Projected final (with Ch 1 + Ch 3; Ch 6 placement-resolved)** | | **~70-78K** | **~260-290** | | | |

---

## §4. Open Insights status

| # | Title | Status | Notes |
|---|---|:---:|---|
| 1 | Framework may be naming too many things | closed-ratified | (closed in earlier work; vocabulary footprint discipline) |
| 2 | Gate names are inconsistent in convention | closed-ratified | (closed 2026-04-26) |
| 3 | "Severance" vocabulary cluster | closed-ratified | (closed 2026-04-26) |
| 4 | "Commons Bonds" book title rigor | closed-ratified | (closed in earlier work) |
| 5 | Glossary v2 Foreclosure Cost duplicate | closed-ratified | |
| 6 | 31 individual rigor passes structural approach | closed-ratified | |
| 7 | Value Capture vs Value Extraction | closed-ratified | |
| 8 | Audit methodology failure risk | closed-ratified | (Working Principle #2 origin) |
| 9 | Framework as decision-time severance-detection | open | |
| 10 | Framework vocabulary literature audit | closed-ratified | |
| 11 | Cost Severance semantic collision | closed-ratified | |
| 12 | ARP→ARR rename | closed-ratified | (closed 2026-04-24) |
| 13 | Book-scope creep monitoring | open | Ongoing. |
| 14 | Norway sovereign wealth fund | open | Ongoing engagement. |
| 15 | Chapter revision thread | open | Ongoing. |
| 16 | Two CIT sub-forms placement | closed-ratified | (closed 2026-04-26) |
| 17 | Option C' political-philosophical positioning | closed-ratified | |
| 18 | Autonomy-as-commons placement | open | |
| 19 | CSD–RCV correlation hypothesis | open with reframing finding | Block 4 §3 surfaced positive-correlation severity-signature with structural orthogonality (post-v1.46.0 §11.3 Tech Appendix integration). |
| 20 | Cost Severance Ring-1 | closed-ratified | |
| **21** | **Tech Appendix v0.0.5 + Ch 6 HTML full-rewrite** | **MOSTLY-CLOSED 2026-04-27** | Tech Appendix v1.0.0 ✓ (CURRENT); Ch 6 HTML format conversion ✓; Ch 6 supplementary-passage structural integration into chapter body PENDING author placement work. |
| 22 | Chapter-titles-in-sweep-scope | **closed-ratified 2026-04-27** | Memory rule + Open Insights file updated. |
| 23 | CTR Book-1-vs-Book-2 boundary | closed-ratified 2026-04-27 (Path 2) | Version G integrated Book-2-mention-free. |
| 24 | Book 1 references to Book 2 | closed-ratified 2026-04-27 (Scenario B) | All Book 2 references removed. |

---

## §5. Pending decisions / open questions

### §5.1 Top priority — Ch 6 supplementary-passage structural integration

The 13 Phase B supplementary passages are currently appended to Ch 6 as a `phase-b-supplementary-passages` block. Each passage has placement guidance in `manuscript/chapters/Chapter__6___SupplementaryDrafts_2026-04-24.md` `§N.M.2 Integration notes for Phase B`. Per-passage placement work + per-passage commit cadence per memory rule. After all 13 passages land structurally, the marker block is removed.

Vocabulary clashes to resolve during integration:
- Existing AIT references in Ch 6 → CIT (per Passage A integration)
- Existing "10 abundances / 10 dimensions" framing → "10 commons categories" presented as examples (per Passages B + C)
- Existing Counterargument 4 falsifiability response → augment with Passage H CIT-vs-empirical distinction
- Existing convergence-table presentation → augment with Passage I IPG-table reconciliation
- Method 1 Replacement Cost walkthrough → replace placeholder with Passage J DAC three-horizon
- Methodology section → insert Passage L Ostrom-vs-extraction distinction (before Four Gates apparatus)
- Restitution Bond first introduction → insert Passage M reparations-economics engagement
- Methodology section → insert Passage N methodology defense consolidation (before Counterargument-handling)

### §5.2 Follow-up — Tech Appendix Methodology Defense academic-reviewer-depth elaboration

§15.1 of Tech Appendix v1.0.0 currently carries the compact summary of the eight alternative-tested methodology defenses. The full academic-reviewer-depth elaboration (with full lineage citations + technical alternative-specifications + rigor-pass cross-references) is queued for follow-up authoring per supplementary drafts §6.11.2 integration note. ~1,500–2,000 words of fresh academic-reviewer-depth prose to author.

### §5.3 Continuation — Project-wide vocabulary sweep

Tier B docs deferred from earlier sessions:
- research/case-studies/alaska-permanent-fund.md
- research/case-studies/ancient-egypt-pyramids.md
- research/case-studies/blood-diamonds.md
- research/case-studies/feudalism.md
- research/case-studies/housing-enforced-immobility.md
- research/case-studies/qin-dynasty-monumental-extraction.md
- research/case-studies/tax-tradeoff-us-sweden.md
- research/case-studies/indigenous-land-dispossession.md
- research/literature/bibliography.md (verify all chapter-relevance refs current)
- alignment/commons_bonds_personal_stories_candidates_v1.0.0.md
- core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md
- tools/commons_bonds_rigor_protocol_v2.2.0.md
- tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md

### §5.4 Author personal stories cycle

Per memory rule: drafting under Path F (no pre-fit-to-framework concern); once 3-5 stories exist, suite evaluates per-story (M3+M4+M5+M9+M11) and Path K integration depth gets revisited. Status: ongoing author work; not blocking other progress.

### §5.5 Ch 3 (waterman) draft

Largest content gap. Cross-referenced from Ch 8 + Ch 9 + Ch 10. Needs full chapter draft (~5,000-6,000 words). Could be tackled before or after Ch 6 supplementary-passage structural integration.

### §5.6 Ch 2 interviews (3 INTERVIEW NEEDED placeholders)

Author-execution items at Ch 2 lines 30-31, 199-200, 204-205. Not blocking other work.

### §5.7 Ch 6 holistic review

Per chapter-by-chapter prose-sweep discipline (Insight #22 updated to include chapter titles + section headers in scope), Ch 6 holistic review is due once supplementary-passage structural integration lands. Three-test per-element rigor (earns place / would expansion strengthen / would compression strengthen) + chapter-title check (Book-1/Book-2 carry-over; applied-advocacy register; vocabulary regressions) + section-header sweep.

---

## §6. Recent commits (this session, in order)

| Commit | Subject |
|---|---|
| `f7532b2` | Insight #22 closed-ratified — chapter titles + section headers added to chapter-by-chapter prose-sweep scope |
| `fab0895` | Path B Scope 1 — Tech Appendix v0.0.5 → v1.0.0 (Option A pretty-printed semantic HTML; format-only conversion) |
| `bd2f662` | Path B Scope 2 — TOC restructure + partial-integration reconciliation + CIT worked examples embedded |
| `bc2d2cf` | Path B Scope 3 — Retired-vocabulary passage rewrites |
| `835bf7c` | Path B Scope 4 — §C.4 8-tier excise + §K verified clean |
| `a9ace93` | Path B Scope 5 — §11 Empirical Validation expanded with Block 4 + Method 3 + DAC + IPG-table |
| `8cade87` | Path B Scope 6 — Phase B Ch 6 supplementary integration into Tech Appendix |
| `86e3eea` | Path B Scope 7 — Chapter 6 HTML conversion + Phase B supplementary passages appended |
| (this commit) | Session handoff v1.46.0 |

---

## §7. Bibliography additions this session

None this session. The Tech Appendix v1.0.0 references all use existing bibliography entries (per terms_index records and per the rigor-source-doc citations that were already integrated into bibliography in earlier sessions).

Confirmed-present bibliography references load-bearing for v1.0.0:
- Hotelling 1931 (§4 Hotelling Identity)
- Savage 1951 + Loomes & Sugden 1982 + Lempert et al. 2003 (§8 ARR)
- Mazzucato 2018 + Harvey 2003 (Value Extraction)
- Ostrom 1990 + Hess & Ostrom 2007 + Lewis 1973 (CIT)
- Pigou 1920 + Balboa 2016 + Yang & Davis 2021 + OSMRE + GAO 2017 (Accountability Bond)
- Darity & Mullen 2020 + Bullard 1990 + Chetty et al. + Esping-Andersen 1990 (CSD / B₁)
- Hartwick 1977 + Solow 1974 (B₂)
- Costanza 1997 + Dixit & Pindyck 1994 + Brennan-Schwartz 1985 + Black-Scholes 1973 (Triangulated RCV methods)
- Weitzman (§16 K.1 Variable Discount Rates)
- Parfit 1984 (§5.4 — confirmed in bibliography §18.9 per supplementary drafts §6.5 reference)
- Climeworks Orca/Mammoth + Carbon Engineering Stratos + IEA DAC 2022 + IPCC AR6 WG III + Rennert et al. 2022 (§11.5 DAC three-horizon + SCC-vs-DAC distinction)
- Anderson 2017 *Private Government* (autonomy / civic-republican)

---

## §8. Files modified this session (working state)

**Tech Appendix (Open Insight #21 Path B):**
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` (renamed from v0.0.5; full restructure to v1.0.0 architecture)
- `manuscript/technical-appendix/archive/TechnicalAppendix_v0.0.3.html` (moved from technical-appendix/)
- `manuscript/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md` (moved from technical-appendix/; retirement note added)

**Chapter 6:**
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` (format conversion + Phase B supplementary passages appended)

**Memory + open insights:**
- `/Users/c17n/.claude/projects/-Users-c17n-Documents----WorkingOn-commons-bonds/memory/feedback_always_expand_rule.md` (chapter-titles-in-sweep-scope clause added)
- `/Users/c17n/.claude/projects/-Users-c17n-Documents----WorkingOn-commons-bonds/memory/MEMORY.md` (index hook updated)
- `alignment/commons_bonds_open_insights_v1.0.0.md` (Insight #22 closed-ratified)

**Session handoff:**
- `alignment/sessions/commons-bonds-session-handoff-2026-04-27_v1.46.0.md` (this file)

---

## §9. Known issues / things to watch

1. **Ch 6 transitional state.** Word count is inflated (~12,310) because the 13 Phase B supplementary passages are currently appended rather than placed inline. Once structural integration lands, Passages A/B/C/D/E/F will replace existing prose (net replacement, not addition); §6.5–§6.11 will be additive (~5,000 words). Final post-integration Ch 6 word count will be closer to ~10,000 words depending on author compression decisions.

2. **§15.1 Methodology Defense compact-only.** The Tech Appendix v1.0.0 §15.1 carries the compact eight-defense summary; full academic-reviewer-depth elaboration is queued (§5.2 of this handoff). Not blocking but flagged.

3. **Bibliography Parfit entry verification.** Supplementary drafts §6.5 cites bibliography §18.9 for Parfit 1984. Confirmed during Scope 6 integration but worth re-verifying when next bibliography sweep happens.

4. **Open Insight #19 reframing not yet propagated.** The Block 4 finding that CSD-RCV positive-correlate (severity-signature) rather than inversely-correlate landed in Tech Appendix §11.3, but the Open Insights file still carries Insight #19 in its original "test the inverse-correlation hypothesis" framing. Open Insight #19 update or closure should land in next-session work.

5. **Phase B supplementary drafts file disposition.** Once all 13 Ch 6 main-text passages are placed structurally into Ch 6 body, the supplementary drafts file's role as a holding-document is complete. Decision pending: (a) preserve as historical record per Principle #4 Tier-2; (b) retire / move to archive. Author judgment after structural integration lands.

6. **Author personal stories drafting** is ongoing per memory rule; will trigger Ch 1 holistic review when sufficient stories exist.

---

*End of session handoff v1.46.0. Generated 2026-04-27 by Claude Opus 4.7 (1M context) at Chris Winn's direction. Successor session should begin by reading this document for full context, then surface one of the §1 candidate next moves for author confirmation before execution.*
