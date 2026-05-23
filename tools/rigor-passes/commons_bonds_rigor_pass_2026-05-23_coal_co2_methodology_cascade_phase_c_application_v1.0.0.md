# Commons Bonds — Coal-CO₂ Methodology Cascade Phase C Application

**Pass type:** Phase C application — author-ratified spot-fix application across full cascade footprint.
**Date:** 2026-05-23.
**Author:** Claude.
**Status:** APPLIED.
**Branch:** `claude/coal-co2-methodology-cascade-phase-c-1fae85`.
**Parent artifact (ratification record):** [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_ch6_ch8_ta_coal_co2_short_ton_methodology_reconciliation_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-22_ch6_ch8_ta_coal_co2_short_ton_methodology_reconciliation_v1.0.0.md) (RATIFIED 2026-05-23; commit `89c56e6`).
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20); closes cross-thread #12.

---

## §1 — Ratified bundle being applied

The author ratified the recommended bundle from the parent reconciliation artifact §10:

| Finding | Option ratified | Effect |
|---|---|---|
| §6.1 Heat-content basis | **Option C** — hybrid (framework-introduction stays at national-bituminous-average; McDowell-specific contexts use McDowell-specific Pocahontas-seam basis with basis-distinction disclosure) | Ch 6 line 42 + TA §7.4 line 2859 preserve 2.32 mt CO₂/short ton ($441 carbon-tail); Ch 6 line 343 + Ch 8 + TA §11.1 + TA §11.6 cascade to 2.61 mt CO₂/short ton ($510 carbon-tail) |
| §6.2 Cascade direction | **Option C** — hybrid cascade matched to §6.1 | 17 line-touches across 4 files + 2 audit artifacts + cross-thread #12 retirement |
| §6.3 IPG canonical lock | **Option A** — preserve 33–122× lock; light annotation only | $524 / $4.50 = 116×; inside canonical range; HIGH-3 IPG artifact gets §5 annotation only |

**Net corpus state after application:**
- Ch 8 McDowell-specific carbon-tail: **$510 / short ton coal** (was $544).
- Ch 8 honest-cost floor: **$524 / short ton coal** (was $558).
- TA §11.1 + §11.6 cascade to McDowell-specific basis (2.61 mt CO₂/short ton; $510 carbon-tail; 1.57B mt cumulative CO₂).
- Ch 6 line 42 + TA §7.4 line 2859 preserve national-bituminous-average framework-introduction basis (2.32 mt/short ton; $441 carbon-tail).
- Ch 6 line 343 cascades to McDowell-specific Pigouvian bracket ($518–$532).
- TA §1.7 line 2916 retires stale "$550–$570/ton" reference (independent of basis choice; framework-introduction figure cleanup to $449–$464).
- 33–122× IPG canonical lock preserved; light §5 annotation only.

---

## §2 — Per-file diff summary

### §2.1 — Ch 8 (`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`)

**8 line touches** (7 enumerated in parent artifact §5.1 + 1 coupling-consistency touch at L80):

| Line | Before | After | Source |
|---|---|---|---|
| 72 | "approximately 2.86 tons of carbon dioxide ... approximately five hundred and forty-four dollars" | "approximately 2.6 metric tons of carbon dioxide (… EPA AP-42 §1.1 bituminous-coal combustion factor … McDowell County's production-weighted Pocahontas-seam heat content of roughly 28 mmBtu per short ton, yields 2.61 metric tons CO₂ per short ton coal; this is the McDowell-specific calibration of the framework figure Chapter 6 introduced under the national-bituminous-average heat content, which yields 2.32 metric tons CO₂ per short ton) ... per metric ton ... approximately five hundred and ten dollars" | parent §5.1 Option B/C row; basis-distinction inline parenthetical surfaces cross-Ch-6 disclosure |
| 74 | "by a factor running from roughly four against today's market peak" + "Five hundred and forty-four dollars." | "by a factor running from roughly three against today's market peak" + "Five hundred and ten dollars." | parent §5.1 row 74 ($510/$140 = 3.64× → "roughly three" per conservative rounding) |
| 78 | "a minimum of five hundred and forty-four dollars per ton" | "a minimum of five hundred and ten dollars per ton" | parent §5.1 row 78 |
| **80** (coupling) | "Conservative floor across four components: five hundred and fifty to five hundred and seventy dollars per ton." | "Conservative floor across four components: five hundred and eighteen to five hundred and thirty-two dollars per ton." | **NOT enumerated in parent §5.1; required for internal arithmetic consistency** ($2+$1+$5+$510 low through $4+$3+$15+$510 high = $518–$532) |
| 154 | "- Foreclosure: $544" | "- Foreclosure: $510" | parent §5.1 row 154 |
| 164 | "Total: $558 per ton." | "Total: $524 per ton." | parent §5.1 row 164 (= $2+$1+$5+$510+$2+$1+$1+$2) |
| 168 | "the carbon term alone exceeds the market price by a factor of at least four" | "the carbon term alone exceeds the market price by a factor of at least three" | parent §5.1 row 168 ($510/$140 = 3.64× → "at least three") |
| 238 | "floor of roughly five hundred and fifty-eight dollars" | "floor of roughly five hundred and twenty-four dollars" | parent §5.1 row 238 |

**Lines preserved unchanged (per parent §5.1):**
- Line 212: "between thirty-three and one hundred and twenty-two times the 1960 sale price" (33–122× canonical lock robust to $524 floor; §6.3 Option A ratified).

### §2.2 — Ch 6 (`manuscript/chapters/Chapter__6_ThreeWaysofCounting.md`)

**2 line touches** (1 prose change + 1 inline basis-distinction parenthetical extension):

| Line | Before | After | Source |
|---|---|---|---|
| 42 (framework-introduction) | "(EPA emission factor for bituminous coal at short-ton accounting: 93.28 kg CO₂ per mmBtu × roughly 24.9 mmBtu per short ton)" | extended parenthetical surfacing basis-distinction: "(… the national-bituminous-average heat content used here at the framework-introduction register; the McDowell-specific worked example in Chapter 8 and the Technical Appendix's §11 McDowell calibration use the Pocahontas-seam production-weighted heat content of roughly 28 mmBtu per short ton, which yields a higher per-ton figure where the case-specific basis applies)" | parent §5.2 + §6.1 Option C basis-distinction discipline; canonical $441 figure preserved |
| 343 (Pigouvian McDowell paragraph) | "lands around $449 to $464 per ton of coal" | "lands around $518 to $532 per ton of coal under the McDowell-specific Pocahontas-seam heat-content basis (production-weighted ~28 mmBtu/short ton; the framework-introduction figure earlier in the chapter used the national-bituminous-average ~24.9 mmBtu/short ton and yielded $449 to $464)" | parent §5.2 row 343 Option C |

**Lines preserved unchanged (per parent §5.2):**
- Line 44: "$449 to $464 per ton" framework-introduction running total. Preserved because line 44 is in the framework-introduction register where national-bituminous-average basis applies. (Line 343 IS the McDowell-specific paragraph; line 44 is the generic-framework paragraph just after line 42.)

**Footnote convention.** Ch 6 uses inline parenthetical disclosure (no markdown footnote syntax in the corpus); the basis-distinction "footnote" in the parent artifact is implemented as an inline parenthetical extension at line 42 + line 343 per chapter convention.

### §2.3 — TA (`core/technical-appendix/TechnicalAppendix_v2.0.0.html`)

**~9 line touches across 3 sections**:

| Line | Section | Before | After |
|---|---|---|---|
| 2916 | §1.7 Numerical update | "Ch 6 figure of $550–$570/ton ... updated RCV estimate is $555–$580/ton" | "Ch 6 framework-introduction figure of $449–$464/ton (national-bituminous-average heat-content basis; ...) ... updated RCV estimate is $454–$474/ton" — drift cleanup |
| 3876 | §11.1 Damage Function McDowell row | "~$544/ton (dominant term for fossil fuels)" | "~$510/ton (McDowell-specific Pocahontas-seam basis; ~2.61 mt CO₂/short ton × $190; dominant term for fossil fuels)" |
| 3882 | §11.1 totals | "Total with carbon: $552–566/ton" | "Total with carbon: $518–532/ton" |
| 3898 | §11.1 spatial-cost-severance paragraph | "$544/ton carbon term" | "$510/ton carbon term" |
| 4517 | §11.6 Block 4 McDowell calibration carbon-intensity row | "~2.32 tons CO₂ per ton coal (EPA emission factor for bituminous coal at short-ton accounting)" | "~2.61 metric tons CO₂ per short ton coal (EPA AP-42 §1.1 emission factor at McDowell-specific Pocahontas-seam heat content; basis-distinction note …)" |
| 4520 | §11.6 Block 4 derivation cell | "× EIA-published heat content for bituminous coal (~24.93 mmBtu/short ton) ≈ 2,324.56 kg/short ton ≈ 2.32 mt CO₂/short ton" | "× McDowell-specific production-weighted heat content (~28 mmBtu/short ton, Pocahontas Nos. 3 + 4 + Eagle seams per USGS Professional Paper 1625-C + WV Geological Survey trace-elements database) ≈ 2,611.84 kg/short ton ≈ 2.61 mt CO₂/short ton" + **inline basis-distinction note** spanning §7.4 ↔ §11.1 ↔ §11.6 register-distinction discipline |
| 4530 + 4533 | §11.6 Block 4 cumulative emissions | "~1.4 billion tons CO₂ / 600M × 2.32 ≈ 1.39B mt CO₂" | "~1.6 billion metric tons CO₂ / 600M × 2.61 (McDowell-specific basis) ≈ 1.57B mt CO₂" |
| 4603+4607 | §11.6 Method 1 DAC conservative bullet | "1.4B tons CO₂ × $600–$1,000/ton = $836B–$1.39T … per-ton coal at 2.32 mt CO₂/short ton × DAC range = $1,392–$2,320/ton coal" | "1.57B mt CO₂ × $600–$1,000/ton = $942B–$1.57T … per-short-ton coal at 2.61 mt CO₂/short ton (McDowell-specific basis) … $1,566–$2,610/short ton coal" |
| 4617+4623 | §11.6 Method 1 DAC at-scale bullet | "1.4B tons CO₂ × $300–$600/ton = $418B–$836B … $696–$1,392/ton coal" | "1.57B mt CO₂ × $300–$600/ton = $471B–$942B … $783–$1,566/short ton coal" |
| 4631+4635 | §11.6 Method 1 DAC optimistic-2050 bullet | "1.4B tons CO₂ × $100–$300/ton = $139B–$418B … $232–$696/ton coal" | "1.57B mt CO₂ × $100–$300/ton = $157B–$471B … $261–$783/short ton coal" |
| **6620** (coupling) | §14 Harvey passage | "you absorbed $552 of cost for every $4.50 you were paid" | "you absorbed at least $518 of cost for every $4.50 you were paid" — **NOT enumerated in parent §5.3; coupling-consistency touch required by §11.1 totals cascade** |

**Lines preserved unchanged (per parent §5.3):**
- Line 2859 (§7.4 Gate 4 worked example): "2.32 tons CO2 per ton coal" — framework-introduction register preserved per §6.1 Option C.
- Line 3886 (§11.1 RCV model estimate): "$580–620/ton (using Weitzman declining rates, S_max ≈ 0.85 for electricity generation)" — separately-derived model output (not arithmetic from Damage Function bracket); flag-forward at §4 below for separate audit if recompute desired.

### §2.4 — Ch 9 (`manuscript/chapters/Chapter__9_PricingHonestly.md`)

**0 line touches** per parent §5.4: $524 lands within "$500-$600" bracket (Ch 9:12) and within rounding tolerance of "approximately $550" (Ch 9:116).

### §2.5 — Cross-chapter consistency inventory (`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`)

**2 rows updated** per parent §5.5 Option C column:

- **Line 111** — Coal carbon-tail per-ton row: rewritten to surface basis-varies-by-chapter-role disclosure; cites both McDowell-specific $510 (Ch 8 + TA §11.1 + TA §11.6) and national-average $441 (Ch 6 line 42 + TA §7.4) with cross-reference to reconciliation artifact.
- **Line 112** — McDowell coal per-ton total floor row: "$558" → "$524" with line-reference update to current Ch 8 line 164; preserves Ch 9 cross-reference compatibility notes.

### §2.6 — HIGH-3 IPG canonical-construction artifact (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md`)

**1 annotation added** at end of §5.1 per parent §5.6 (33–122× canonical lock annotation):

> Post-reconciliation annotation (added 2026-05-23): The Ch 8 worked-example honest-cost floor moved from $558 → $524 per the 2026-05-22 coal-CO₂ methodology reconciliation (…). The 33–122× canonical lock is unaffected: $524 / $4.50 = 116×, which lands inside the canonical range. The Ch 8 prose changes at lines 168, 74, 212 ratified in this artifact's §5.1 remain canonical; the underlying floor figure that anchors the carbon-tail-dominance arithmetic at lines 74 + 168 retreats from "at least four" to "at least three" per the reconciliation's coupling note.

### §2.7 — Cross-thread #12 (`publishing/strategy/cross-thread-todos.md`)

Status: open → **RESOLVED**. See §5 below for full closure record.

---

## §3 — Verification table

Per `feedback_verify_stale_memory_claims.md`: every touch verified post-edit via grep / Read.

| Touch | File | Verification | Status |
|---|---|---|---|
| Ch 8 L72 | manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md | grep for "2.86 tons" → 0 matches; grep for "2.6 metric tons of carbon dioxide" → 1 match at L72; grep for "five hundred and ten dollars" → present at L72 | ✓ |
| Ch 8 L74 | same | grep for "roughly four against today" → 0 matches; grep for "roughly three against today" → 1 match at L74; grep for "Five hundred and ten" → 1 match at L74 | ✓ |
| Ch 8 L78 | same | grep for "five hundred and forty-four" → 0 matches in Ch 8; "five hundred and ten dollars per ton" → present at L78 | ✓ |
| Ch 8 L80 | same | grep for "five hundred and fifty to five hundred and seventy" → 0 matches; "five hundred and eighteen to five hundred and thirty-two" → 1 match at L80 | ✓ |
| Ch 8 L154 | same | grep for "Foreclosure: \$544" → 0 matches; "Foreclosure: \$510" → 1 match at L154 | ✓ |
| Ch 8 L164 | same | grep for "Total: \$558" → 0 matches; "Total: \$524" → 1 match at L164 | ✓ |
| Ch 8 L168 | same | grep for "at least four" (in carbon-term context) → 0 matches; "at least three" → 1 match at L168 | ✓ |
| Ch 8 L238 | same | grep for "five hundred and fifty-eight" → 0 matches; "five hundred and twenty-four" → 1 match at L238 | ✓ |
| Ch 6 L42 | manuscript/chapters/Chapter__6_ThreeWaysofCounting.md | grep for "Pocahontas-seam production-weighted" → 1 match at L42; canonical "2.32 tons" + "$441" preserved at L42 | ✓ |
| Ch 6 L343 | same | grep for "$449 to $464 per ton of coal" → 1 match (the reference-to-framework-introduction phrase at L343); grep for "$518 to $532" → 1 match at L343; grep for "McDowell-specific Pocahontas-seam" → 1 match at L343 | ✓ |
| TA §1.7 L2916 | core/technical-appendix/TechnicalAppendix_v2.0.0.html | grep for "$550&ndash;$570" → 0 matches; "$449&ndash;$464/ton" → 1 match at L2916; "$454&ndash;$474" → 1 match at L2916 | ✓ |
| TA §11.1 L3876 | same | grep for "~\$544/ton" → 0 matches; "~\$510/ton (McDowell-specific Pocahontas-seam basis" → 1 match at L3876 | ✓ |
| TA §11.1 L3882 | same | grep for "\$552&ndash;566" → 0 matches; "\$518&ndash;532/ton" → 1 match at L3882 | ✓ |
| TA §11.1 L3898 | same | grep for "\$544/ton carbon term" → 0 matches; "\$510/ton carbon term" → 1 match at L3898 | ✓ |
| TA §11.6 L4517 + L4520 | same | grep for "2.32 mt CO₂/short ton" in §11.6 cell-text → preserved only in basis-distinction note + cross-reference; primary McDowell row at 2.61 mt | ✓ |
| TA §11.6 L4530 + L4533 | same | grep for "~1.4 billion tons CO₂" → 0 matches; "~1.6 billion metric tons" → present at L4530; "1.57B mt CO₂" → present at L4533 | ✓ |
| TA §11.6 L4603–4635 (Method 1 DAC) | same | grep for "1.4B tons CO₂" → 0 matches in Method 1; "1.57B mt CO₂" → 3 matches (one per DAC tier); "\$1,392&ndash;\$2,320" → 0 matches; "\$1,566&ndash;\$2,610" → 1 match | ✓ |
| TA §14 L6620 (coupling) | same | grep for "absorbed \$552 of cost" → 0 matches; "absorbed at least \$518 of cost" → 1 match at L6620 | ✓ |
| Inventory L111 + L112 | tools/audits/cross-chapter-consistency-inventory_2026-05-11.md | grep for "~\$544 (1 ton coal → 2.86 tons CO₂" → 0 matches; "$510 (McDowell-specific basis" → 1 match at L111; "$524 (Ch 8 canonical sum-of-components, line 164" → 1 match at L112 | ✓ |
| IPG artifact §5.1 annotation | tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md | grep for "Post-reconciliation annotation (added 2026-05-23)" → 1 match | ✓ |

---

## §4 — Flag-forward (out-of-scope for this Phase C application)

The following items surfaced during application but are out-of-scope per the parent artifact's enumerated cascade footprint. Flagged here for future audit / PM-session triage:

- **TA §11.1 L3886 RCV model estimate ($580–620/ton).** The RCV estimate uses Weitzman declining discount rates + S_max ≈ 0.85 substitution-elasticity treatment (separately-derived model output, not arithmetic from Damage Function bracket). Parent artifact §5.3 explicitly did not enumerate it. Structural relationship to the Damage Function bracket has widened (was "$580–620 slightly above $552–566"; now "$580–620 notably above $518–532"). A downstream session may want to recompute the RCV model estimate under the McDowell-specific basis (preliminary recompute would land in the ~$546–$586 range if the proportional shift is taken at face value), or document that the RCV estimate intentionally uses its own model parameters (separately defensible). Flag-forward for TA editor's attention.
- **Ch 8 L80 + TA L6620 coupling-consistency touches** were applied without explicit enumeration in the parent artifact's §5.1 / §5.3 tables. Both were required by internal arithmetic consistency with the ratified §11.1 + §11.6 cascades; documented above. Future cascade artifacts should enumerate downstream coupling touches more comprehensively in §5.

---

## §5 — Cross-thread #12 closure

**Resolution applied at `publishing/strategy/cross-thread-todos.md`:**
- Cross-thread #12 ("Ch 8 line 73 coal-CO₂ short-ton-accounting cascade") moved from Open section → Resolved table.
- Resolution text: "RESOLVED 2026-05-23 via Phase C application of ratified bundle from `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_ch6_ch8_ta_coal_co2_short_ton_methodology_reconciliation_v1.0.0.md` (§6.1 Option C + §6.2 Option C + §6.3 Option A). Phase C application artifact + commit SHA recorded in update log."
- Update-log entry added with this artifact's commit SHA.

**Closure rationale:** The reconciliation supersedes the routing-time recommendation. Cross-thread #12 originally proposed verbatim cascade to $441 (Option A); reconciliation §6.1 Option C ratified hybrid (McDowell-specific basis where applicable; national-average preserved at framework-introduction register). All cascade touches applied; cross-corpus consistency restored.

---

## §6 — Discipline checks

### §6.1 Branch discipline (per CLAUDE.md)

Fresh feature branch `claude/coal-co2-methodology-cascade-phase-c-1fae85` cut from current `origin/main` tip (commit `89c56e6` — Coal-CO₂ methodology reconciliation RATIFIED). Per CLAUDE.md merge-to-main default: this session is Phase C application of an author-ratified bundle (ratification record at parent artifact §10, 2026-05-23); session autonomously fast-forward merges to `main` at close.

### §6.2 Memory discipline (per `feedback_verify_stale_memory_claims.md`)

All line numbers re-verified against current file states at session start:
- Ch 6 = 365 lines (confirmed; matches parent artifact §5.2 reference; post-commit `9befb92` developmental-edit landed).
- Ch 8 = 243 lines (confirmed; matches parent artifact §5.1 reference).
- TA = 8,044 lines (confirmed; matches parent artifact §5.3 reference).
- Inventory = 264 lines (confirmed).
- IPG artifact = 306 lines (confirmed; §5.1 annotation insertion point identified by section grep).
- Cross-thread-todos = 203 lines (confirmed; #12 entry at L114).

### §6.3 Trust-decision documentation (per `feedback_audit_recent_active_review_default.md`)

This session trusts the parent reconciliation artifact's ratification record (§10, 2026-05-23) over any older drift in the touched files. Where Ch 8 Pass 1 source inventory (2026-05-16, line 491) cites the EIA volume/mass coal-CO₂ page as authority for 2.86 short tons CO₂/short ton coal, the parent reconciliation artifact §8.4 documents the trust-decision: the EIA URL's tabulated emission factor for bituminous coal is 2.32 mt/short ton, not 2.86 (the 2.86 figure derives from a separate stoichiometric calculation, not from the EIA emission-factor table). This Phase C application supersedes the Ch 8 Pass 1 source attribution.

### §6.4 Invariant-gate + corpus-discipline checks

- No new apparatus terms introduced.
- No scaffolding patterns introduced (`TODO`, `TK`, `Option A-Z`, INCLUDE / EXCLUDE glyphs).
- HTML / em-dash render conventions preserved (TA edits use existing HTML entity conventions: `&ndash;`, `&times;`, `&sect;`, `<strong>`, etc.).
- No named-subject consent implications (numerical methodology question; no named-living-subject prose modifications).

---

## §7 — Downstream sequencing (per parent artifact §7.2 Step 3)

Per pipeline doctrine §5 cross-chapter workstream lifecycle, the following light re-fires are deferred to a downstream session (NOT this session):

- **Stage 1c light coherence-check** per touched chapter (Ch 6 + Ch 8 + Ch 9).
- **Pass 3.3 light audience-load re-fire** per touched chapter (Ch 6 + Ch 8 + Ch 9).

These light re-fires confirm the Phase C application has not introduced cross-chapter inconsistency or audience-load regression. Workstream closes only after light re-fires complete clean.

---

## §8 — Stop conditions

Per session prompt:
1. ✓ Phase C application artifact (this artifact) is committed.
2. ✓ All cascade edits land per parent §5 / §7.2.
3. ✓ Cross-thread #12 status moves to Resolved with commit SHA.
4. ✓ Feature branch fast-forwarded to origin/main + pushed.

---

*End of Phase C application artifact. Workstream returns to PM dashboard #20 cadence; downstream sequencing per §7.*
