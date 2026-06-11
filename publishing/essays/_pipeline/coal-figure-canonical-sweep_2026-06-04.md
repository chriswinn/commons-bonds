---
artifact: coal-figure-canonical-sweep
date: 2026-06-04
status: PROPOSED-awaiting-ratification
scope: McDowell County coal / magnitude figures — cross-artifact number sweep + proposed canonical figure ledger
expands: book-amendment-candidate #7 (carbon-term label ambiguity + arithmetic)
inputs:
  - manuscript/chapters/Chapter__2_TheMiner.md
  - manuscript/chapters/Chapter__6_ThreeWaysofCounting.md
  - manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md
  - manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html (§3.6 / §9.5 convergence table, §7.4, §11.1, §11.6, §11.11)
  - publishing/essays/atlantic-ideas-pricing-honestly/essay.md
  - publishing/op-eds/mcdowell-county-true-cost/op-ed.md (NB: task named a "_archive/fresh-newpipe-draft_2026-06-03.md" that does not exist in this snapshot; swept the canonical op-ed.md instead)
  - publishing/essays/aeon-mask-of-abundance/essay.md (NB: task named a "_archive/aeon-final-candidate-assembled_2026-06-03.md" that does not exist in this snapshot; swept the canonical essay.md instead)
prior-canonical-lock-history:
  - tools/audits/cross-chapter-consistency-inventory_2026-05-11.md (§3 recurring-statistics rows; carbon-tail + total-floor + IPG rows)
  - tools/pre-submission-reviews/ch8_pre_pub_review_queue_v1.0.0.md
  - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_ch6_ch8_ta_coal_co2_short_ton_methodology_reconciliation_v1.0.0.md (referenced; the 2026-05-23 §6.1 Option C basis-split lock)
---

# Coal-figure canonical sweep — McDowell County (PROPOSED)

## 0. Headline finding (the load-bearing error)

**The carbon term `$510/ton` is arithmetically wrong on its own stated basis.**
Every artifact that carries `$510` labels it as `2.61 mt CO₂/short ton × $190/mt`.
But `2.61 × 190 = $495.9 ≈ $496`, not $510. The corpus has propagated a ~$14/ton
carbon-term error (and the Ch 8 pre-pub queue at line 132 asserts "Internal
arithmetic verified" for exactly this product, so the verification itself is wrong).

The $510 number appears to be a residue of an earlier `2.68 mt × $190 = $509`
or `~2.685 × 190` calibration that predates the 2026-05-23 lock to the
Pocahontas-seam 2.61 figure. When the emission factor was tightened to 2.61, the
downstream products ($510 carbon, $524 total, $518–532 four-component floor) were
never re-derived. **The label and the arithmetic disagree in Ch 8, TA §11.1, TA §11.6,
and the 2026-05-11 consistency inventory.**

Corrected products at the locked 2.61 basis and $190 SCC:
- Carbon term: **$496/ton** (2.61 × 190 = 495.9).
- Eight-component total: $2+$1+$5+**$496**+$2+$1+$1+$2 = **$510/ton** (note the
  delicious collision: the corrected *total* equals the old *carbon-term* label —
  a strong argument for pinning labels so "$510" is never ambiguous).
- Four-component conservative floor: was "$518–532"; the construction is
  $5 (community-low) + $496 (carbon) + small heads ≈ ; see §2 for what the
  $518–532 band actually denotes and how it must move.

---

## 1. DISCREPANCY TABLE (figure × artifact × value)

Line/section references are exact. "—" = figure not present in that artifact.

### 1a. Mine-mouth price, 1960

| Artifact | Value | Ref |
|---|---|---|
| Ch 2 | (not stated numerically for 1960; "the price the coal actually sold for") | — |
| Ch 6 | **$4.50/ton** | line 38, 80, 173 (table) |
| Ch 8 | **"roughly four to five dollars"** | line 24, 40, 64, 170, 242 |
| TA §11.1 | **$4.50–$18/ton** (mine mouth, nominal, period average) | line 3860 |
| TA §11.6 / §9.5 | $4.50 (1960 nominal); $50 (2025-inflation-corrected) | 4892, 4896 |
| Atlantic essay | **"four dollars and fifty cents"** ($4.50) | line 3 |
| Op-ed | **"about $4.50"** | line 25 |
| Aeon | — (qualitative only) | line 35 |

**Drift:** Ch 8 alone uses the "$4–5" band; everyone else uses the point value
$4.50. TA §11.1 additionally carries a "$4.50–$18" *period-average* band that is
a different quantity (period average, not 1960 specifically) and is a frequent
reader-confusion source.

### 1b. CO₂ emission factor (mt CO₂ per short ton coal)

| Artifact | Value | Basis | Ref |
|---|---|---|---|
| Ch 6 | **2.32** | national-bituminous-average (24.9 mmBtu/short ton) | line 42 |
| Ch 8 | **2.61** | McDowell-specific Pocahontas-seam (~28 mmBtu/short ton) | line 72 |
| TA §7.4 Gate 4 | **2.32** | national-bituminous-average (24.93 mmBtu) | line 2859 |
| TA §11.1 | **~2.61** | McDowell-specific | line 3876 |
| TA §11.6 | **2.61** (≈2,611.84 kg) | McDowell-specific Pocahontas | 4517, 4520, 4533 |
| Op-ed | **2.86** ⚠ | (no basis stated) | line 33 |
| Atlantic essay | — | (carbon folded into $520–600 band) | line 3 |
| Aeon | — | — | — |

**Drift:** the chapter/TA split (2.32 national vs 2.61 McDowell) is a *ratified,
documented* basis-split (2026-05-23 §6.1 Option C) — NOT drift; it is coherent.
**The op-ed's 2.86 is genuine, unreconciled drift** — it matches neither basis
and has no stated derivation. (2.86 corresponds to neither 24.9 nor 28 mmBtu at
the AP-42 factor; it looks like a generic "burning coal ≈ 2.86× its mass in CO₂"
popular figure imported during audience-blind drafting. The op-ed Path-B note at
line 14 even records rewriting "the 2.86-tons-of-CO₂ sentence" for verbatim
de-duplication but left the *number* unreconciled to the book's basis.)

### 1c. Social cost of carbon (SCC)

| Artifact | Value | Dating / source | Ref |
|---|---|---|---|
| Ch 6 | **$190** | "EPA's 2023 estimate" | line 42 (also $42 Obama / $1–7 Trump / $190 Biden chronology at 48, 153) |
| Ch 8 | **$190** | "Rennert et al. 2022 *Nature*… grounded the 2023 EPA update" | line 74 (chronology incl. $42 Obama / $1–7 Trump / $51 Biden / $190 EPA-2023 at 122) |
| TA | **$190** | EPA SCC | 3876, 5727, 6620 |
| Op-ed | **$190** | "anchored to a 2022 *Nature* meta-analysis and adopted in the 2023 EPA update" | line 33 |
| Atlantic | (implicit in $520–600) | — | — |

**No drift on the SCC value ($190) or its provenance.** Consistent. (Discount rate
is not pinned to a single number anywhere — deliberately; the corpus treats the
discount-rate choice as the contested parameter, Stern 1.4% / Nordhaus ~4–5.5% /
Weitzman declining, TA §10/§14.)

### 1d. Carbon term ($/ton coal) — national-average basis

| Artifact | Value | Stated construction | Ref |
|---|---|---|---|
| Ch 6 | **"~$441"** | "$190 × 2.32" (implied) | line 42 |
| Ch 6 | **"$449 to $464"** | national-bituminous-average four-component Pigouvian | line 343 |
| TA §7.4 | (2.32 basis cited; product not stated as $ in the grep'd cell) | — | 2859 |
| Inventory (2026-05-11) | **"$441"** | "2.32 × $190" | line 111 |

**Internal tension:** $190 × 2.32 = **$441.4** ✓ (Ch 6 line 42 + inventory agree).
But Ch 6 line 343 reports the national-average *four-component Pigouvian total* as
"$449 to $464" — i.e. carbon $441 + health/env/community heads. That is internally
plausible IF the heads add $8–23; but note line 343's own parenthetical computes the
national-average carbon as the driver of "$449 to $464," which only works if the
carbon term is ~$441 and the non-carbon heads are compressed. The $449–464 band is
*defensible* as carbon-plus-small-heads at the national basis, but it is never
explicitly decomposed, so a reader cannot tell whether $449–464 is "carbon alone"
or "carbon + heads." **Label ambiguity, flagged in §2.**

### 1e. Carbon term ($/ton coal) — McDowell-specific basis

| Artifact | Value | Stated construction | Correct product | Ref |
|---|---|---|---|---|
| Ch 8 | **$510** | "2.61 mt × $190" | ✗ should be **$496** | line 74, 80, 158 |
| TA §11.1 | **~$510** | "~2.61 mt × $190" | ✗ should be **$496** | line 3876, 3898 |
| TA §11.6 | (2.61 basis; DAC/M-method ranges, not a single $190-SCC carbon line) | — | — | 4517–4637 |
| Inventory | **~$510** | "2.61 × $190" | ✗ should be **$496** | line 111 |
| Ch 8 pre-pub queue | **~$510** ("Internal arithmetic verified") | "2.61 × $190" | ✗ should be **$496** | line 85, 132 |

**Drift / error:** uniform $510 across Ch 8 + TA + inventory + queue, all
mislabeled as 2.61 × 190. The correct product is **$496**. This is the single
highest-priority fix.

### 1f. Honest TOTAL ($/ton coal)

| Artifact | Value | What it denotes | Ref |
|---|---|---|---|
| Ch 8 | **$524** | eight-component sum: $2+$1+$5+$510+$2+$1+$1+$2 | line 168, 242 |
| Ch 8 | **$518–532** | "conservative floor across FOUR components" (health+env+community+carbon) | line 82 |
| Ch 6 | **$518–532** | "standard Pigouvian… under McDowell-specific Pocahontas basis" | line 343 |
| Ch 6 | **$449–464** | same, under national-bituminous-average basis | line 343 |
| TA §11.1 | **$518–532** | "Total with carbon" | line 3882 |
| Ch 9 (per inventory) | **$500–600** (bracket) / **~$550** (rhetorical) | cross-reference | inventory line 112 |
| Atlantic essay | **"$520 to $600"** | honest price band | line 3 |
| Op-ed | **$558** ⚠ | "roughly $558" honest cost (built on 2.86 × 190 = $544 carbon) | line 25, 33 |
| Aeon | — | — | — |

**Drift:**
- $524 (Ch 8 eight-component) vs $518–532 (Ch 8/Ch 6/TA four-component) — these are
  *different quantities* (8 components vs 4) that happen to overlap; not strictly a
  contradiction but the corpus never says "$524 is the 8-component sum; $518–532 is
  the 4-component sub-floor." All are built on the erroneous $510 carbon term, so
  all move down ~$14 once corrected (see §3).
- **Op-ed $558 is genuine drift** — it is built on the op-ed's own 2.86 factor and
  $544 carbon, neither of which matches the book.
- Atlantic "$520–600" band is a deliberately loose rhetorical band that *contains*
  the book numbers; it is the most defensible essay treatment (a band, not a false-
  precision point) but its low end ($520) is below the corrected $510 total and
  above the corrected $496 carbon — needs a glance (see §3).

### 1g. Carbon term ($544) and CO₂ factor (2.86) — op-ed only

Already captured in 1b/1f. The op-ed is the most-drifted artifact: **2.86 mt
(vs 2.61/2.32), $544 carbon (vs $496/$441), $558 total (vs $510/$524).** It is also
the highest-exposure artifact (NYT/WaPo/Project Syndicate target). Highest edit priority.

### 1h. IPG / magnitude multiple

| Artifact | Value | What it denotes | Ref |
|---|---|---|---|
| Ch 2 | **33 to 122×** | headline range; "floor is 33×"; "Ch 8 lands at upper end" | line 126 |
| Ch 6 | **~50×** (per-case implied) | TA §3.6 Block 4 three-method implied CS summary | line 185 |
| Ch 6 | **50 to 555×** | triangulated M1+M2+M3 aggregated estimate-by-estimate | line 185, 187 |
| Ch 6 | **33 to 122×** | explicitly attributed to Method 1 (Replacement Cost) alone | line 187 |
| Ch 6 | **33** | "IPG of 33 (the McDowell-coal compression)" Parfit anchor | line 267 |
| Ch 8 | **33 to 122×** | headline; "even today carbon-term alone ≥3× market" | line 172, 216 |
| TA §3.2 | IPG=33 example ("market covers ~3%") | line 762 | |
| TA §9.5 table | **33–122×** (Damage Fn) / **45–89×** (Real Options) / **67–134×** (RCV) | convergence row | 3148–3158 |
| TA §11.1 | **33–122×** (without carbon) / "substantially higher with carbon" | line 3889 | |
| TA §11.6 | **555×** (1960-nominal RCV/price) → **50×** (inflation-corrected) | 4892–4900 | |
| TA §11.11 | reconciles **33–122× canonical** ↔ **50–555× triangulated** (time-horizon attribution) | 6200–6257 | |
| TA §1108 (case table) | **~50×** | summary | 1120 |
| TA §16 sensitivity | **33× to 122×** central; "≥5× even under most conservative params" | 7434, 7521 |
| Atlantic essay | **"two orders of magnitude"** (~100×) | line 3 | |
| Op-ed | (no multiple stated; gives $558 vs $4.50 ≈ 124×, unstated) | — | |
| Aeon | — | — | — |

**The 33 / 50 / 120 / 122 / 555 spread explained:**
- **33** = floor of the canonical Method-1 (Replacement Cost / Damage-Function-anchored)
  range, "the McDowell-coal compression," used as the Parfit moral anchor.
- **122** = ceiling of that same canonical Method-1 range.
- **33–122×** = canonical headline (Ch 2 + Ch 8 + TA §9.5 Damage-Function column +
  TA §11.1 "without carbon"). This is the book's public-facing number.
- **~50×** = the *inflation-corrected* triangulated central case (TA §11.6: $2,500
  RCV ÷ $50 2025-inflation-adjusted 1960 price). Also the TA case-table summary
  (~50×). It is NOT a contradiction of 33–122×; it sits inside it.
- **555×** = the *uncorrected* mixing of 2025-dollar RCV ($2,500) against the
  1960-*nominal* $4.50 price. TA §11.6 itself flags this as an inflation artifact
  and corrects it to ~50×. The 555× should NOT appear as a standalone claim.
- **50–555×** = the triangulated M1+M2+M3 range (Ch 6 line 185–187 + TA §11.11),
  whose top end carries Method 3's α-irreversibility premium at multi-generational
  scale and whose bottom mixes scales. **This range is the corpus's biggest
  reader-confusion liability** because its top end (555×) is the very number TA
  §11.6 disowns as an inflation artifact.

### 1i. Supporting magnitude figures (population, life-expectancy, black lung, reclamation)

| Figure | Ch 2 | Ch 6 | Ch 8 | TA | Op-ed | Atlantic | Canonical (inventory) |
|---|---|---|---|---|---|---|---|
| Peak population (1950) | ~100,000 (l.22, 42) | — | ~100,000 (l.58) | ~100,000 (2895) | ~100,000 (l.27) | — | 100,000 |
| 2020 population | "under 20,000" (l.42) | — | "fewer than 20,000" (l.58) | "~19,000" (2895) / **"18,000"** (3892) | "fewer than 20,000" (l.27) | — | **DRIFT: 18k vs 19k vs <20k** |
| Life-expectancy gap | 13 yrs (63.5 vs 76.5) (l.44) | 13 yrs (l.32, 34) | ">a decade" (l.36) | 13 yrs (4578, 7371) | (not stated) | "longevity gap" (qual.) | **~13 yrs (locked, inventory l.83)** |
| Drug death rate | 141/100k vs ~16 nat'l 2015 (l.46) | — | 141/100k vs ~16 (l.58) | 141/100k (2265) | 141/100k "~10× nat'l" (l.27) | — | 141/100k (2015 denom locked) |
| Black Lung program distributed | $44B (l.70) | ~$44B thru 2009 (l.28) | $44B (l.34 via x-ref) | (referenced) | "more than $44B" (l.29) | — | $44B |
| BL Trust Fund debt | $4.6B; →$15B by 2050 (l.70, 138) | — | (x-ref) | — | **$4.5B in 2021**; →$15B by 2050 (l.29) | — | **DRIFT: $4.6B vs $4.5B** |
| Reclamation shortfall | $4–6B ($7.5–9.8B need vs $3.8B bonds) (l.84) | $3.7–6B (l.30) | $3.5–6B; $7.5–9.8B vs $3.8B (l.48) | $3.7–6B (3892) | $3.5–6B; $7.5–9.8B vs $3.8B (l.31) | (qual.) | **near-consistent; $3.5–6B / $3.7–6B / $4–6B minor drift** |
| Reclamation acreage | "633,000 acres" (l.84) | — | "hundreds of thousands; ~million nationwide" (l.48) | "~150,000 acres McDowell disturbed" (4649) | "633,000 acres" (l.31) | — | **633,000 (Appalachia) — Ch 8 vaguer; TA 150k is McDowell-only, different scope** |
| Personal-income drop after Gary/U.S.Steel closure | "two-thirds in a single year" (l.40) | — | "two-thirds in a single year" (l.58) | — | "two-thirds in a single year" (l.27) | — | two-thirds (consistent) |
| Gary/U.S.Steel closure year | "late 1980s" / "1,200 jobs" (l.40) | — | **"1986"** (l.58) | — | **"1990"** (l.27) | — | **DRIFT: late-1980s vs 1986 vs 1990** |

---

## 2. LABEL AMBIGUITY ANALYSIS — what does "$510" denote?

The string `$510` is doing **two incompatible jobs** in the corpus, and the
arithmetic underneath it is wrong in the first job:

1. **In Ch 8, TA §11.1, the inventory, and the Ch 8 queue: "$510" = the carbon term**
   (Foreclosure component), labeled `2.61 mt CO₂ × $190`. But that product is
   **$496**, not $510. So "$510" here is (a) mislabeled arithmetically, and
   (b) a quantity (carbon-only) that should not be confused with any total.

2. **Once the carbon term is corrected to $496, the Ch 8 eight-component TOTAL
   becomes exactly $510** ($2+$1+$5+$496+$2+$1+$1+$2). So after the fix, "$510"
   would denote the *honest total*, not the carbon term — the opposite of its
   current meaning. **This is precisely why the label must be pinned**: leaving
   "$510" floating guarantees a future reader (or drafter) conflates carbon-term
   and total.

Defensible relationship among the three families of numbers:

| Quantity | National-average basis (2.32) | McDowell-specific basis (2.61) |
|---|---|---|
| **Carbon term alone** ($190 × factor) | $441 | **$496** (currently mislabeled $510) |
| **4-component Pigouvian floor** (health $2 + env $1 + community $5 + carbon) | ~$449–464 (Ch 6 l.343) | ~$504–510 (currently stated $518–532) |
| **8-component honest total** (Ch 8 full decomposition) | (not computed at national basis) | **$510** corrected (currently $524) |
| **RCV-model estimate** (M3 / Weitzman declining rate) | — | **$580–620/ton** (TA §11.1 l.3886) — a *different method*, higher than the damage-function total |

The RCV $580–620 band is **not** the same object as the damage-function total. It
is the residual-commons-value estimate using Weitzman declining discount rates and
S_max≈0.85 — a method-distinct, higher figure. It must never be summed with or
conflated against the $510/$524 damage-function total; it is an alternative
accounting that the convergence-table presents alongside (TA §9.5: RCV-model IPG
column 67–134× vs Damage-Function 33–122×).

**The four-component "$518–532" band is the most quietly wrong number** because it
inherits the $510 carbon error AND its construction is undocumented. With carbon at
$496 and the stated heads (health $2, env $1, community $5 = $8 low end), the
4-component low end is $496+$8 = **$504**; the high end depends on whether the band's
$532 used the high heads (health $4 + env $3 + community $15 = $22 → $496+$22 = $518).
So the corrected 4-component band is **~$504–518**, not $518–532. (The current
$518–532 = old-$510-carbon + $8…$22 heads. New = $496-carbon + $8…$22 = $504–518.)

---

## 3. PROPOSED CANONICAL SET (for author ratification)

Honoring (a) conservative-floor discipline ("where estimates have a range, use the
lower figure; where contested, omit"), and (b) corrected arithmetic
$190 × 2.61 = $496 / $190 × 2.32 = $441. Labels are PINNED so no string is ambiguous.

### CANONICAL FIGURE LEDGER — McDowell County coal

| # | Figure | CANONICAL value + pinned label | Basis | Replaces / corrects |
|---|---|---|---|---|
| C1 | **Mine-mouth price, 1960** | **$4.50/ton** (point value; reserve "$4–5" only where a deliberately loose register is wanted) | 1960 nominal | Ch 8's "$4–5" → harmonize to $4.50; keep TA's "$4.50–$18 period average" clearly labeled as *period average*, not 1960 |
| C2 | **CO₂ emission factor — framework-introduction register** | **2.32 mt CO₂/short ton** | national-bituminous-average (24.9 mmBtu, EPA AP-42 §1.1) | (no change; ratified basis-split) |
| C3 | **CO₂ emission factor — McDowell worked-example register** | **2.61 mt CO₂/short ton** | McDowell Pocahontas-seam (~28 mmBtu, AP-42 §1.1) | (no change; ratified basis-split) — **but op-ed's 2.86 → must change to 2.61** |
| C4 | **Social cost of carbon** | **$190/mt CO₂** (EPA 2023 update, anchored to Rennert et al. 2022 *Nature*) | EPA 2023 | (no change; consistent) |
| C5 | **Carbon term — national-average basis** | **$441/ton** (= $190 × 2.32) | C2 × C4 | (consistent; keep) |
| C6 | **Carbon term — McDowell basis** ("Foreclosure / carbon-tail component") | **$496/ton** (= $190 × 2.61) | C3 × C4 | **corrects $510** everywhere (Ch 8 l.74/80/158; TA §11.1; inventory l.111; queue l.85/132) |
| C7 | **4-component Pigouvian floor — McDowell basis** | **~$504–518/ton** (carbon $496 + health $2–4 + env $1–3 + community $5–15) | sum | **corrects "$518–532"** (Ch 6 l.343; Ch 8 l.82; TA §11.1 l.3882) |
| C8 | **8-component honest TOTAL (the headline floor)** | **$510/ton** (= $2+$1+$5+$496+$2+$1+$1+$2) | Ch 8 full decomposition | **corrects $524** (Ch 8 l.168/242); flows to Ch 9 "$500–600 / ~$550" which still holds |
| C9 | **RCV-model estimate (method-distinct, NOT a damage-function total)** | **$580–620/ton** (Weitzman declining rate, S_max≈0.85) | TA §11.1 l.3886 | (keep; pin label "RCV-model estimate," never call it "the total") |
| C10 | **IPG — canonical headline** | **33–122×** (Method-1 / damage-function-anchored; floor 33 = "the McDowell-coal compression"; ceiling 122) | RCV/P_market, near-term horizon | (keep as the public-facing number, Ch 2 + Ch 8 + essays) |
| C11 | **IPG — triangulated central case** | **~50×** (inflation-corrected, $2,500 RCV ÷ $50 2025-adjusted 1960 price) | TA §11.6 | (keep as TA/Ch 6 triangulated central; sits inside C10) |
| C12 | **IPG — triangulated full range** | **50–555× (TA-internal only; DO NOT surface 555× as a standalone claim)** | M1+M2+M3, α-dominance ceiling | keep TA §11.11 reconciliation; the 555× top end is an inflation-scale artifact TA §11.6 itself disowns — never quote bare |
| C13 | **Peak population (1950)** | **100,000** | — | consistent |
| C14 | **2020 population** | **under 20,000** (or "~19,000" where precision wanted) | — | **retire "18,000"** (TA §11.1 l.3892) → harmonize to ~19,000/"under 20,000" |
| C15 | **Life-expectancy gap** | **13 years (63.5 male vs 76.5 national)** | — | consistent (locked) |
| C16 | **Drug death rate** | **141/100,000 (2015) vs ~16/100,000 national 2015 ≈ 10×** | 2015 denom | consistent (locked) |
| C17 | **Black Lung program distributed** | **$44 billion** | — | consistent |
| C18 | **BL Trust Fund debt** | **$4.6B (current) → ~$15B by 2050** | — | **op-ed's "$4.5B in 2021"** should align to $4.6B unless the 2021-vintage point is deliberately wanted (judgment call J4) |
| C19 | **Reclamation shortfall** | **$4–6B** ($7.5–9.8B need vs $3.8B bonds posted) | — | harmonize "$3.5–6B"/"$3.7–6B" → state as "$4–6B" rounded or pin "$3.8B bonds vs $7.5–9.8B need" precisely |
| C20 | **U.S. Steel / Gary closure year** | **JUDGMENT CALL (J5)** — sources differ; "late 1980s" (Ch 2) vs "1986" (Ch 8) vs "1990" (op-ed) | — | needs author fact-decision; recommend verify against U.S. Steel Gary closure record and lock one year |

### Artifacts requiring edits to match canonical (expands book-amendment-candidate #7)

| Artifact | Edits needed |
|---|---|
| **manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md** | l.74/80/158: carbon term $510 → **$496**; l.82: "$518–532" → **"$504–518"**; l.168/242: total $524 → **$510** (and re-verify the bullet sum); l.24/40/64/170/242: "$4–5" → consider harmonizing to $4.50 (C1) |
| **manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html** | §11.1 l.3876/3898: "~$510" → **$496**; l.3882 "$518–532" → **"$504–518"**; l.3892: "18,000" → **"~19,000"**; verify §11.6 / §9.5 columns inherit corrected carbon; §11.11: add note that 555× is an inflation-scale artifact not for standalone use |
| **manuscript/chapters/Chapter__6_ThreeWaysofCounting.md** | l.343: "$518 to $532" → **"$504–518"** (McDowell basis); confirm "$449 to $464" national-average band is intended as carbon+heads and label it; l.42: "$441" is correct — keep |
| **publishing/op-eds/mcdowell-county-true-cost/op-ed.md** | l.33: **2.86 → 2.61** mt CO₂; carbon **$544 → $496**; l.25: honest cost **$558 → $510** (or "$500–600" band); l.27: closure year "1990" → reconcile (J5); l.29: "$4.5B in 2021" → reconcile (J4). **HIGHEST PRIORITY — highest-exposure artifact.** |
| **publishing/essays/atlantic-ideas-pricing-honestly/essay.md** | l.3: "$520 to $600" band — low end ($520) is now slightly above corrected $510 total. Recommend **"$500 to $600"** so the band cleanly contains the $510 floor and the $580–620 RCV band. "two orders of magnitude" (~100×) is within 33–122× — fine. |
| **publishing/essays/aeon-mask-of-abundance/essay.md** | No numeric figures present — **no edits needed**. |
| **tools/audits/cross-chapter-consistency-inventory_2026-05-11.md** | §3 rows: carbon-tail "$510" → **$496**; total-floor "$524" → **$510**; update the basis-split note to record the arithmetic correction |
| **tools/pre-submission-reviews/ch8_pre_pub_review_queue_v1.0.0.md** | l.85/86/94/132/134: correct "$510"→$496, "$510-532"→"$504-518", "$524"→$510; **retract the "Internal arithmetic verified" claim at l.132** (the verification was wrong) |

---

## 4. OPEN JUDGMENT CALLS (cannot resolve without author decision)

- **J1 — Does the author accept that the carbon term is $496, not $510, and that
  the honest total is therefore $510, not $524?** This is arithmetic, not judgment —
  $190 × 2.61 = $495.9 — but it cascades to the book's most-quoted number, so the
  author should ratify the correction explicitly rather than have a sub-agent change
  the headline figure silently. (Recommendation: ratify; the corrected numbers are
  *more* conservative, which strengthens the floor discipline.)

- **J2 — How to present the McDowell IPG publicly: 33–122× vs ~50× vs the
  50–555× range.** Recommendation: keep **33–122×** as the single public headline
  (Ch 2 + Ch 8 + essays + op-ed); confine 50–555× to TA §11.11 with the explicit
  time-horizon-attribution reconciliation; never surface **555×** as a bare claim
  (it is the inflation-scale artifact TA §11.6 already disowns). But whether to keep
  the triangulated range visible in Ch 6 prose at all is an author call.

- **J3 — Mine-mouth: harmonize Ch 8's "$4–5" to the corpus-standard $4.50, or keep
  the band as a deliberate register softening?** Recommendation: harmonize to $4.50
  for the point claim; a band invites "which is it?" Minor.

- **J4 — BL Trust Fund debt: $4.6B (Ch 2 / corpus) vs op-ed's "$4.5B in 2021."**
  Is the op-ed deliberately date-anchoring to a 2021 vintage figure? If so, keep
  with the year label; if not, align to $4.6B. Author/fact call. (Both are
  pre-publication-refresh-trigger candidates against the latest DOL/GAO figure.)

- **J5 — U.S. Steel / Gary mine closure year: "late 1980s" vs "1986" vs "1990."**
  Genuine factual discrepancy across three artifacts. Needs a verified single year
  locked against the U.S. Steel Gary Works / Gary District closure record. (The
  "1,200 jobs" and "two-thirds income drop in a single year" are consistent; only
  the year drifts.) Cannot resolve from internal corpus alone.

- **J6 — National-average four-component band "$449–464" (Ch 6 l.343): is this
  carbon-alone or carbon-plus-heads?** The number only reconciles as carbon ($441) +
  compressed heads. Author should confirm the intended decomposition so the band is
  pinned and re-derivable; otherwise it is the national-basis twin of the $518–532
  ambiguity. (Recommendation: relabel as "≈$441 carbon + $8–22 heads ≈ $449–463.")

- **J7 — RCV-model band $580–620 (C9): keep in main-text Ch 8/Ch 6 or confine to
  TA?** It is method-distinct and higher than the damage-function total; surfacing it
  next to "$510 honest total" risks readers treating $510–620 as one fuzzy range.
  Recommendation: keep in TA convergence table + Ch 6 triangulation; if used in
  Ch 8, label explicitly "RCV-model estimate (a different method), $580–620." Author call.

---

## 5. Summary of what is CONSISTENT (no edit needed)

SCC $190 + Rennert/Nature/EPA-2023 provenance; the 2.32-vs-2.61 basis-split (ratified,
documented); life-expectancy 13 yrs; drug rate 141/100k (2015); $44B BL distributions;
peak population 100,000; "two-thirds income drop in a single year"; reclamation
$3.8B bonds vs $7.5–9.8B need (the $4–6B gap rounds consistently); Deepwater 15–17×,
Libby 40–80×/55–82×, Exxon Valdez 1,200–1,900× (cross-case IPGs, reconciled at Ch 6 l.486).
