# Ch 8 MED-3 + MED-6 Cascade Reconciliation — Stage-3 Pass-1 Phase C Residuals

**Artifact:** Stage-3 Pass-1 Phase C cascade-reconciliation, v1.0.0
**Chapter:** Ch 8, *What Things Actually Cost*
**Cascade source:** MED-3 ($0.80/ton → $1–$1.50/ton range-based R1) + MED-6 ($4.50 → "four to five dollars" hedge); both applied per Ch 8 Pass 1 Phase C
**Date drafted:** 2026-05-21
**Date modified:** 2026-05-21
**Status:** **PROPOSED** (artifact-only; author ratification gates Phase C application)
**Parent audit:** [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md)
**Parent application commit:** [`5fe6af6`](https://github.com/) — *Ch 8 Pass 1 Phase C — 16 ratified Ch 8 edits + 1 Ch 2 + 1 Ch 6 + 5 inventory rows* (2026-05-21)
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20)
**Cross-chapter consistency inventory row affected:** [`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`](tools/audits/cross-chapter-consistency-inventory_2026-05-11.md) §3 line 88 (BLP per-ton arithmetic — R1 range $1–$1.50 canonical lock).

---

## §1. Scope

This artifact reconciles three internal-chapter residual sites that the Ch 8 Pass 1 Phase C application session (`5fe6af6`) explicitly surfaced for follow-up rather than silently extending scope. The two ratified Phase C touches that drive the cascade are:

- **MED-3 (R1 range-based; ratified in-session 2026-05-21):** Black Lung Program per-ton allocation shifted from a single-point figure ("eighty cents per ton") to a range ("between one and one and a half dollars per ton"), with denominator harmonized to "since the Program's 1969 establishment" at both Ch 8 lines 34 + 38 and Ch 6 line 24. Inventory row §3 line 88 was updated to lock the new range as the canonical figure.
- **MED-6 (Option C hedge):** 1960 McDowell mouth-price shifted from "$4.50" to "roughly four to five dollars" at Ch 8 line 24.

Three Ch 8 prose sites continue to reference the prior figures verbatim or to make arithmetic / rhetorical claims that depended on them. Each is reconciled below per the Amendment-C Interactive Ratification Protocol (Options + Recommendation + Reasoning per finding).

### In-scope

- **Site 1 — Line 40:** "Two to four dollars. Against a market price of four-fifty in 1960. Direct health alone — the most documented component — returns roughly as much as the coal sold for."
- **Site 2 — Line 52:** "Conservatively allocated per ton: one to three dollars. Which, added to direct health, already places the national severed cost at three to seven dollars — already above the 1960 market price, before any foreclosure pricing at all."
- **Site 3 — Line 166:** "Against a market price of $4.50 in 1960. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for."

### Out-of-scope (do NOT extend audit to; per session prompt)

- **MED-8 (today coal market price $40–$140):** HELD per conservative discipline. The line-166 `$40 to $140 today` segment is untouched; this artifact addresses only the `$4.50 in 1960` portion of line 166.
- **HIGH-3 cross-corpus IPG canonical lock (33–122× at line 168):** Already canonized via cross-corpus IPG canonical-construction artifact + Option D ratification (commit `5fe6af6` per §12.6 of the parent audit). The ratio remains corpus-canonical; this artifact does not propose changes to line 168.
- **LOW-2 (Dunbar 1895/1896), LOW-4 (SCC EO 12866), LOW-7 (Fort McKay Treaty 8), LOW-8 (Conley rent-seeking):** HELD per ratified parent disposition.
- **Any new fact-check or voice-polish findings beyond the three named cascade sites:** Surface as flag-forward in §6 only; do NOT bundle into this artifact's ratification scope.

### Mirror site flagged but not in ratification scope

- **Line 238:** "The gap between that number and the four-dollar-and-fifty-cent invoice is the severed cost." — Same cascade pattern as Site 3 (climactic restatement of the 1960 mine-mouth figure). The session prompt explicitly names three cascade sites, and the substance-drives-length / scope-discipline rule applies. This artifact treats line 238 as a §6 flag-forward downstream consideration that the author may bundle into Phase C application of Site 3 if they choose, OR defer to a subsequent Pass-2 voice-polish session. **§6 documents the option; §3 does NOT propose options for line 238.**

---

## §2. Cascade-trace methodology

### §2.1 Cascade taxonomy

Three distinct cascade-failure modes appear across the three sites:

| Mode | Description | Site occurrence |
|---|---|---|
| **A. Verbatim-figure residual** | Prior point-figure ($4.50, $0.80) appears in adjacent prose; no arithmetic dependency on the prior figure; pure harmonization needed | Site 1 (line-40 market-price phrase); Site 3 (entire $4.50 reference) |
| **B. Arithmetic-sum holds; rhetorical-claim stretches** | The cost-component sum still arithmetically reconciles under the new range, but a rhetorical / comparative claim built on the prior sum-vs-market relationship is stretched or contradicted at one end of the new range | Site 1 ("returns roughly as much"); Site 2 ("already above") |
| **C. Arithmetic-sum holds independently** | The cost-component sum is internally re-derivable from the new component ranges without disturbance | Site 1 (DH total $2–$4); Site 2 (sum $3–$7) — both still arithmetically hold |

Mode A is mechanical (verbatim replacement). Mode B is the substantive reconciliation question: hedge the rhetorical claim, or tighten the arithmetic? Mode C is the positive result the cascade leaves intact (no arithmetic damage).

### §2.2 Arithmetic-coherence framework

The chapter's discipline (line 28) is: *"Where estimates have a range, I use the lower figure. Where an externality is contested, I omit it. The goal is not a ceiling. The goal is a floor."* The post-cascade per-component bounds are:

| Component | Pre-cascade | Post-cascade | Sum-bound preserved? |
|---|---|---|---|
| BLP (line 34/38, lower line of direct health) | $0.80/ton (single) | $1.00–$1.50/ton (range; MED-3 R1) | Yes (range absorbed) |
| Direct health total (line 38/40) | $2–$4/ton | $2–$4/ton (preserved per parent ratification) | Yes (verified §3.1) |
| Environmental (line 52) | $1–$3/ton | $1–$3/ton (untouched) | Yes |
| 1960 market price (line 24) | $4.50/ton (single) | $4–$5/ton (range; MED-6) | N/A (denominator side) |

**Direct-health-total preservation rationale** (verified §3.1 below): The pre-cascade composition was BLP ($0.80) + other-direct-health ($1.20–$3.20) = $2–$4. Post-cascade with BLP $1.00–$1.50, the other-direct-health component re-bounds at $1.00–$2.50 to preserve the headline $2–$4 hedge. Both old and new "other-direct-health" ranges are themselves estimates of Medicare/Medicaid-shifted costs + uncompensated care + private medical bills; the $1.20-vs-$1.00 lower-bound shift and $3.20-vs-$2.50 upper-bound shift are inside the imprecision band of those estimators. The parent ratification of MED-3 R1 + the chapter discipline jointly preserve "two to four" as the canonical direct-health-total hedge.

### §2.3 Rhetorical-coherence framework

For each rhetorical / comparative claim, this artifact checks whether the claim holds at:
- **Conservative-floor case:** lower-bound severed cost vs upper-bound market price (the "weakest" position of the argument).
- **Conservative-ceiling case:** upper-bound severed cost vs lower-bound market price (the "strongest" position of the argument).
- **Mid-case:** midpoint vs midpoint (the "expected" position).

A claim that holds across all three is *preserved*. A claim that holds at the ceiling but fails at the floor is *stretched* and needs one of: (a) rhetorical hedge that accommodates the floor case; (b) arithmetic tightening that lifts the floor above the comparator; (c) directional reframing that drops the strict inequality.

### §2.4 Verification protocol

Per `feedback_verify_stale_memory_claims.md` (recent + load-bearing): all line numbers below verified against current `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` (line counts as of `aa04a4a` 2026-05-21 origin/main; Phase C application at `5fe6af6` is the most recent Ch 8 prose-modifying commit).

---

## §3. Per-site findings

### §3.1 Site 1 — Line 40: Direct-health total + market-price phrase + "returns roughly as much" claim

**Location:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:40`](manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:40)

**Current chapter text:**
> "Two to four dollars. Against a market price of four-fifty in 1960. Direct health alone — the most documented component — returns roughly as much as the coal sold for."

**Three sub-issues identified:**

| Sub-issue | Mode | Description |
|---|---|---|
| §3.1.A — "four-fifty" verbatim residual | A | Verbatim residual of the pre-MED-6 figure $4.50. Direct contradiction with line 24's new "four to five dollars" hedge. |
| §3.1.B — "Two to four dollars" arithmetic check | C | Whether the direct-health-total hedge still re-derives from BLP $1–$1.50 + other-direct-health implicit range. Verified holds (per §2.2 above). |
| §3.1.C — "returns roughly as much" rhetorical claim | B | The comparative claim (direct-health total ≈ 1960 market price) is stretched at the conservative-floor case ($2 DH vs $5 market = 40%) and clean at the conservative-ceiling case ($4 DH vs $4 market = 100%). |

#### §3.1.A — "four-fifty in 1960" verbatim residual

The phrase reads as a direct point-figure carryover from pre-MED-6 prose. Line 24 now reads "for roughly four to five dollars"; line 40 says "four-fifty"; an attentive reader notices the same chapter offering two different mouth-price figures three subheadings apart.

#### §3.1.B — "Two to four dollars" arithmetic verification

Verified per §2.2: direct-health-total hedge "two to four dollars" continues to re-derive from the new BLP range ($1.00–$1.50) + the implicit other-direct-health component ($1.00–$2.50 post-cascade re-bounding of the pre-cascade $1.20–$3.20). The hedge holds and requires no rewrite.

#### §3.1.C — "returns roughly as much" claim under post-cascade ranges

Three rhetorical-coherence cases:

| Case | DH | Market | Ratio | "Roughly as much"? |
|---|---|---|---|---|
| Conservative-floor | $2 | $5 | 40% | ✗ — significantly less than market |
| Mid | $3 | $4.50 | 67% | ⚠ — closer to "two-thirds of" than "roughly as much" |
| Conservative-ceiling | $4 | $4 | 100% | ✓ — exactly "roughly as much" |

The claim holds cleanly only at the conservative-ceiling case. The conservative-floor case ($2 DH vs $5 market) reads as a 60% gap — neither "roughly" nor "as much." The rhetorical claim is stretched.

#### §3.1 Spot-fix options

**Option 1A (mechanical hedge — recommended):** Address §3.1.A by mirroring line 24's hedge; address §3.1.C by softening the comparative to one that holds across the full range.

> *Proposed:* "Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone — the most documented component — already returns most of what the coal sold for."

Three-case re-check under Option 1A:
- Floor case ($2 vs $5): 40% — "most of" still stretched; better than "roughly as much" but not perfect.
- Mid case ($3 vs $4.50): 67% — "most of" reads cleanly.
- Ceiling case ($4 vs $4): 100% — "most of" understates slightly but does not overclaim.

**Option 1B (directional / fractional reframing):** Address §3.1.A by mirroring; address §3.1.C by replacing the comparative with a directional fractional claim that holds across the range.

> *Proposed:* "Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone — the most documented component — already accounts for between two-fifths and the full price the coal sold for."

This is arithmetically precise (40% to 100%) but the awkward "two-fifths to the full" register breaks the chapter's conversational voice. Defensible-but-clunky.

**Option 1C (preserve "roughly as much" with explicit upper-bound framing):** Address §3.1.A by mirroring; preserve §3.1.C by adding a parenthetical that anchors the claim to the upper bound + a low-end hedge inline.

> *Proposed:* "Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone — the most documented component — returns roughly as much as the coal sold for at the upper end of the range, half as much at the lower end. Either way, the smallest documented externality is already in the same order of magnitude as the price that cleared the market."

This preserves the punchy "roughly as much" while honestly disclosing the range. Adds ~20 words; substantive but slightly belabored for a paragraph-end punctuation line.

**RECOMMENDATION: Option 1A.**

**Reasoning:**
- The conservative-discipline framing at line 28 ("the goal is a floor — the smallest honest number") makes "most of" the appropriate hedge — it accurately characterizes the relationship across the full range without overclaiming at the floor.
- Option 1A is closest to a single-sentence mechanical swap (verbatim "four-fifty" → "four to five dollars"; rhetorical "roughly as much as" → "most of what"); minimum prose disturbance preserves Pass-2 voice-polish optionality for the entire passage.
- Option 1B is arithmetically precise but breaks voice. Option 1C is honest but adds load to a punctuation line that the rest of the section (line 64's "approaching twice the 1960 market price" running total) is designed to *build on*. Keeping line 40 tight maintains the cumulative-build effect.
- The "most of what" hedge is *defensible* at the floor case ($2 vs $5 = 40%) when read as "most of *what coal cost*" — the floor returns nearly half of the market price as direct-health-only externality, which under the chapter's conservative-discipline framing is precisely the rhetorical point the line is making (even the smallest documented externality approaches the market price).

#### §3.1 Edit specification

**Edit Site 1 (current line 40):**

**Old:**
> Two to four dollars. Against a market price of four-fifty in 1960. Direct health alone — the most documented component — returns roughly as much as the coal sold for.

**New:**
> Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone — the most documented component — already returns most of what the coal sold for.

**Change-spec:**
- "four-fifty" → "four to five dollars" (mirror line 24 MED-6 hedge)
- "returns roughly as much as the coal sold for" → "already returns most of what the coal sold for" (rhetorical hedge accommodating the full $2–$4 vs $4–$5 range)

---

### §3.2 Site 2 — Line 52: Environmental + direct-health sum + "already above" market-price claim

**Location:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:52`](manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:52)

**Current chapter text:**
> "Conservatively allocated per ton: one to three dollars. Which, added to direct health, already places the national severed cost at three to seven dollars — already above the 1960 market price, before any foreclosure pricing at all."

**Two sub-issues identified:**

| Sub-issue | Mode | Description |
|---|---|---|
| §3.2.A — "three to seven dollars" arithmetic check | C | Environmental ($1–$3) + Direct health ($2–$4) = $3 floor to $7 ceiling. Verified holds. |
| §3.2.B — "already above the 1960 market price" rhetorical claim | B | Floor case ($3 sum vs $5 market) — sum is BELOW market, contradicting "already above." Ceiling case ($7 sum vs $4 market) — sum is comfortably above. Floor case fails. |

#### §3.2.A — Arithmetic verification

Verified: Environmental $1–$3 + Direct health $2–$4 = $3 floor + $7 ceiling. The arithmetic itself reproduces cleanly from the per-component figures the chapter has already chosen. No change needed to the per-component figures or to the $3–$7 sum.

#### §3.2.B — "already above the 1960 market price" claim under post-cascade ranges

Three rhetorical-coherence cases:

| Case | Sum | Market | Claim "above"? |
|---|---|---|---|
| Conservative-floor | $3 | $5 | ✗ — sum $1 BELOW market floor |
| Mid | $5 | $4.50 | ⚠ — sum $0.50 above market mid (marginally above) |
| Conservative-ceiling | $7 | $4 | ✓ — sum $3 comfortably above market ceiling |

The claim is contradicted at the conservative-floor case. The mid case is only marginally above ($5 sum vs $4.50 market) — a 11% margin that does not support the line's confident "already above" framing. The claim is stretched and at one bound *contradicted*.

This contradiction is sharper than Site 1's because Site 1's stretched claim ("roughly as much") admits hedging at the floor without semantic injury, while Site 2's "already above" is a strict inequality — either the sum is above the market price or it is not, and at the floor case it is *not*. A reader doing the arithmetic on the chapter's own per-component figures will see the contradiction immediately.

#### §3.2 Spot-fix options

**Option 2A (approximate-hedge — recommended):** Replace strict inequality with directional approximation that holds across the full range.

> *Proposed:* "Conservatively allocated per ton: one to three dollars. Which, added to direct health, already brings the national severed cost up to the 1960 market price — at three to seven dollars per ton, comparable to what the coal cleared for at the mine mouth — before any foreclosure pricing at all."

Three-case re-check:
- Floor case ($3 vs $5): "up to" / "comparable to" reads as approaching-from-below; defensible.
- Mid case ($5 vs $4.50): "up to" / "comparable to" reads as approximately-at; defensible.
- Ceiling case ($7 vs $4): "up to" / "comparable to" understates the margin slightly; defensible.

Holds across all three cases. Slightly longer than the original line.

**Option 2B (range-explicit dual-bound framing):** Make the floor / ceiling explicit and let the reader see the directional gap.

> *Proposed:* "Conservatively allocated per ton: one to three dollars. Which, added to direct health, already places the national severed cost at three to seven dollars per ton — approaching the 1960 market price at the low end of the range, well above it at the high end, before any foreclosure pricing at all."

Three-case re-check:
- Floor case: "approaching" reads cleanly ($3 below $4–$5 market is "approaching").
- Ceiling case: "well above" reads cleanly ($7 vs $4 market ≈ 1.75×).
- The dual-bound framing is honest about which end of the range supports which claim.

Slightly longer; substantive disclosure.

**Option 2C (arithmetic-tightening — DEPRECATED):** Lift the floor of the sum so "already above" holds. Would require revising the per-component figures (environmental, direct health, or both). REJECTED because the per-component figures are corpus-canonical and ratified; revising them to make the running-total comparator hold would back-propagate inconsistency to lines 38 + 48 + §3.1.B + the cross-chapter inventory. Not a viable option without re-opening the per-component ratification.

**Option 2D (directional-reframe — alternative):** Drop the strict-inequality claim and replace with a directional one that doesn't require comparison to market price at all.

> *Proposed:* "Conservatively allocated per ton: one to three dollars. Which, added to direct health, already places the national severed cost at three to seven dollars per ton — and we haven't yet priced foreclosure."

This avoids the comparator entirely; the magnitude $3–$7 is left to the reader, who already has line 64 ("approaching twice the 1960 market price") as the next cumulative reference. Shorter; clean; loses the punch of the cross-comparison at this paragraph's exit.

**RECOMMENDATION: Option 2A.**

**Reasoning:**
- The strict-inequality claim ("already above") is contradicted at the conservative-floor case and only marginally supported at the mid case; preserving it would require Option 2C's deprecated arithmetic-tightening or would simply be a known-stretched claim, neither of which serves the chapter's conservative-discipline framing.
- Option 2A's "comparable to" / "brings the cost up to" hedge is the minimum semantic shift that accommodates the full range honestly. The directional point of the paragraph (even before foreclosure, the cost is in the same neighborhood as the market price) is preserved.
- Option 2B is also defensible and arguably more arithmetically transparent, but adds ~12 words and the dual-bound disclosure may be more than this paragraph-exit line needs — line 64 will handle the next cumulative comparison; this line's job is the directional pivot ("environmental cost is the second component to land near the market price").
- Option 2D drops the comparator entirely, which is the safest path but loses the cumulative-build the chapter is constructing across §Direct Health → §Environmental → §Community Disruption → §Foreclosure. The comparator is doing rhetorical work; Option 2A preserves the rhetorical work while honoring the arithmetic.

#### §3.2 Edit specification

**Edit Site 2 (current line 52):**

**Old:**
> Conservatively allocated per ton: one to three dollars. Which, added to direct health, already places the national severed cost at three to seven dollars — already above the 1960 market price, before any foreclosure pricing at all.

**New:**
> Conservatively allocated per ton: one to three dollars. Which, added to direct health, already brings the national severed cost up to the 1960 market price — at three to seven dollars per ton, comparable to what the coal cleared for at the mine mouth — before any foreclosure pricing at all.

**Change-spec:**
- "already places the national severed cost at three to seven dollars — already above the 1960 market price" → "already brings the national severed cost up to the 1960 market price — at three to seven dollars per ton, comparable to what the coal cleared for at the mine mouth"
- Drops the strict-inequality "already above"; substitutes "brings . . . up to" + "comparable to" which hold across the full $3–$7 sum vs $4–$5 market range.

---

### §3.3 Site 3 — Line 166: Climactic IPG market-price reference (1960 segment)

**Location:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:166`](manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:166)

**Current chapter text:**
> "Against a market price of $4.50 in 1960. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for."

**Single sub-issue identified:**

| Sub-issue | Mode | Description |
|---|---|---|
| §3.3.A — "$4.50 in 1960" verbatim residual | A | Verbatim residual of pre-MED-6 figure. The "$40 to $140 today" segment is held per MED-8 conservative discipline and is not in cascade scope; only the "$4.50 in 1960" segment requires harmonization. |

This site sits at the chapter's climactic § "The sum" — line 164's *"Total: $558 per ton"* leads directly into the three-line market-price comparator. The IPG paragraph at lines 168–170 (already canonized at 33–122× per HIGH-3 + cross-corpus IPG canonical-construction artifact) reads off this site. Harmonization here is high-visibility.

**Register consideration:** Line 166 uses digit-notation ("$4.50", "$40 to $140") rather than the spelled-out register at lines 24 + 40 ("four to five dollars"). This is the only digit-notation appearance of the 1960 market price in the chapter body prose. Two reasonable harmonization registers are available — spelled-out (matching lines 24 + 40 + 238) or digits (matching the line's own internal $40–$140 register).

#### §3.3 Spot-fix options

**Option 3A (spelled-out register; matches lines 24 + 40):** Mirror the MED-6 hedge in the chapter's prose register.

> *Proposed:* "Against a 1960 market price of four to five dollars. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for."

Reads consistently with lines 24 + 40; introduces a register-mix inside the three-line passage (spelled "four to five" + digit "$40 to $140"). Defensible as deliberate — the 1960 figure is foreground prose; the today range is reference-table register.

**Option 3B (digit register; matches the line's $40–$140 internal register):** Preserve internal-line register-consistency.

> *Proposed:* "Against a market price of $4 to $5 in 1960. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for."

Reads consistently with the line's own internal register but introduces a register-mismatch with lines 24 + 40 (spelled "four to five dollars" there; digits here).

**Option 3C (compound; explicit anchor):** Carry the full register-discipline both intra-line and across-chapter.

> *Proposed:* "Against a 1960 market price between four and five dollars at the mine mouth. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for."

Adds "at the mine mouth" — explicit, slightly redundant with line 24's same phrase. Mid-length.

**RECOMMENDATION: Option 3A.**

**Reasoning:**
- The chapter's body-prose register for the 1960 market price is spelled-out at every other appearance (line 24 "four to five dollars"; line 40 "four-fifty" → "four to five dollars" under Site 1 recommendation; line 238 "four-dollar-and-fifty-cent" — see §6 flag-forward). Maintaining the spelled-out register at the climactic restatement preserves chapter-internal voice consistency.
- The intra-line register-mix ("four to five dollars" + "$40 to $140 today") is *deliberate* in the chapter's existing patterns: the $40–$140 today range is the only currency-figure in body prose using digits, and it does so because the range spans an order of magnitude that reads less awkwardly in digits ("forty to one hundred forty dollars" would expand a tight three-line passage). The asymmetric register reads as "the 1960 mouth-price is voice; the today range is reference-data."
- Option 3B's digit register internally consistent for the line but creates a register-conflict with two preceding lines in the same chapter (lines 24 + 40 + 238). Option 3C's "at the mine mouth" anchor is redundant with line 24.
- Option 3A is the minimum-disturbance harmonization that preserves the chapter's established register-asymmetry and matches the MED-6 hedge in the chapter's body-prose register.

#### §3.3 Edit specification

**Edit Site 3 (current line 166):**

**Old:**
> Against a market price of $4.50 in 1960. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for.

**New:**
> Against a 1960 market price of four to five dollars. Against a market price of $40 to $140 today, depending on grade. Against every price coal has ever sold for.

**Change-spec:**
- "$4.50 in 1960" → "1960 market price of four to five dollars" (mirror line 24 MED-6 hedge; preserve spelled-out body-prose register; preserve the line's intra-passage register asymmetry between 1960 prose and today reference-data).
- Sentence-structure shift from "market price of $4.50 in 1960" to "1960 market price of four to five dollars" — moves the year-anchor forward to match the natural prose flow of the new hedge.

---

### §3.4 Mirror site (FLAG-FORWARD, not in §3 ratification scope)

#### §3.4.A — Line 238: closing-paragraph $4.50 invoice reference

**Location:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:238`](manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:238)

**Current chapter text:**
> "For now, what this chapter gives the reader is the one worked example: a ton of coal, priced honestly, at a floor of roughly five hundred and fifty-eight dollars. The gap between that number and the four-dollar-and-fifty-cent invoice is the severed cost. The invoice is what McDowell County was paid. The severed cost is what McDowell County bore."

**Cascade pattern:** Same Mode-A verbatim-residual as Site 3 (climactic restatement of the 1960 mine-mouth price; spelled-out register matching lines 24 + 40; appears in the chapter's penultimate paragraph "The closing line").

**Why flagged but not in ratification scope:** Per the session prompt's explicit scope (three named cascade sites: lines 40, 52, 166) and the substance-drives-length / scope-discipline rule, this artifact does NOT extend the ratification ask to include line 238. The author may:
- (i) bundle line 238 into Phase C application of Site 3 as a coupled spot-fix at the application session's discretion (the harmonization is mechanical: "four-dollar-and-fifty-cent" → "four-to-five-dollar" or equivalent spelled-out hedge);
- (ii) defer to a subsequent Pass-2 voice-polish session, treating the line 238 cascade as a flagged residual after Sites 1 + 2 + 3 application;
- (iii) leave as-is if the author judges that the closing-paragraph diction "four-dollar-and-fifty-cent invoice" carries rhetorical weight that the hedge would dilute (an aesthetic judgment, not an arithmetic one — the figure $4.50 is now a single-point reference inside a corpus that has hedged the same figure at three other body-prose locations).

**Recommended disposition:** Bundle into Site 3 Phase C application (option i above). The line 238 closing-paragraph harmonization is a one-touch change that mirrors line 24's hedge; deferring it to a separate session pays per-session overhead for a mechanical change that the Site 3 application is already opening that prose neighborhood for. **However, this recommendation is contingent on author direction** — the prompt explicitly bounds scope to the three named sites, and the author may have a deliberate reason for the closing-paragraph diction.

**Proposed Phase C edit IF author bundles (presented for author option only; not in §4 ratification table):**

**Old:**
> The gap between that number and the four-dollar-and-fifty-cent invoice is the severed cost.

**New:**
> The gap between that number and the four-to-five-dollar invoice is the severed cost.

OR (alternative compact form):

> The gap between that number and the four-to-five-dollar mine-mouth price is the severed cost.

(The second form replaces "invoice" with "mine-mouth price"; the first form preserves "invoice" diction. Author judgment.)

---

## §4. Ratification summary

### §4.1 Findings ratification table

| Site | Line | Issue | Recommended option | Author ratifies? |
|---|---|---|---|---|
| **Site 1** | 40 | "four-fifty" residual + "roughly as much" stretched claim | **Option 1A** — mirror "four to five dollars" + "most of what" hedge | ☐ |
| **Site 2** | 52 | "already above" claim contradicted at floor case | **Option 2A** — "brings . . . up to" / "comparable to" hedge | ☐ |
| **Site 3** | 166 | "$4.50 in 1960" verbatim residual at climactic IPG | **Option 3A** — spelled-out "four to five dollars" matching lines 24 + 40 | ☐ |

### §4.2 Post-application arithmetic-consistency table

After Phase C application of all three recommended options, the chapter's cost-vs-market-price comparators stand as:

| Line | Comparator | Sum/comparator value | Market price | Claim | Holds? |
|---|---|---|---|---|---|
| 24 | (mouth-price anchor) | — | $4–$5 | (sets the baseline) | ✓ |
| 40 (post 1A) | Direct health vs market | $2–$4 | $4–$5 | "most of what" | ✓ across full range |
| 52 (post 2A) | DH + Env vs market | $3–$7 | $4–$5 | "comparable to" / "brings . . . up to" | ✓ across full range |
| 64 | First-three-components vs market | ~$8 | $4–$5 | "approaching twice" | ✓ ($8/$4 = 2.0; $8/$5 = 1.6) |
| 74 | Carbon-tail vs market | $544 | $4 (life-of-industry floor) | "more than a hundred against the 1960 mine-mouth" | ✓ ($544/$5 = 108.8; $544/$4 = 136) |
| 166 (post 3A) | (climactic restatement) | (uses $558 total at line 164) | $4–$5 (1960); $40–$140 (today) | (sets the IPG-paragraph denominator) | ✓ |
| 168 | IPG ratio | $558 | $4.50 (legacy anchor; HIGH-3 canonical lock at 33–122× preserved per cross-corpus artifact) | "between thirty-three and one hundred and twenty-two times the 1960 sale price" | ✓ (HIGH-3 cross-corpus canonical; not in cascade scope) |

**Note on line 168:** The 33–122× canonical ratio uses the legacy $4.50 figure as its denominator anchor implicitly ($558/$4.50 ≈ 124, rounded to 122 in canonical text; $558/$5 = 111.6 and $558/$4 = 139.5 widen the range slightly under MED-6 hedge). The HIGH-3 + cross-corpus IPG canonical-construction artifact resolved 33–122× as the cross-corpus locked range; this artifact does NOT propose changes to that lock. A future cross-corpus audit may want to verify whether the 33–122× range should widen marginally under MED-6 (to e.g. 33–139×) or whether the canonical lock should formally cite a $4.50 anchor; that is a §6 flag-forward only.

### §4.3 Cross-chapter consequences (post-ratification)

**None.** All three Phase C edits land inside Ch 8 only. No cross-chapter cascade is created by any of the three recommendations.

The MED-3 + MED-6 originating cascade has already propagated to Ch 6 line 24 (MED-3 cross-chapter alignment per `5fe6af6`) and the cross-chapter consistency inventory §3 line 88 (BLP canonical lock updated). No further cross-chapter touches are required by the three recommended cascade-reconciliation edits.

### §4.4 Discipline checks

| Discipline | Status |
|---|---|
| Apparatus regression (Greek letters, integrals, Cᵢ-class) | ✓ All three edits are body-prose hedge changes; no apparatus touched |
| Path B contamination | ✓ All three edits are intra-chapter; no cross-artifact verbatim cloning |
| Named-subject consent | ✓ No new subjects introduced; no living-private subject status changed |
| Scaffolding scan (placeholders, INCLUDE/EXCLUDE glyphs, etc.) | ✓ None introduced |
| Regressed-pattern scan (deprecated terminology, vendor names per CEO-era NDA) | ✓ None introduced |
| Numerical-coherence with the chapter's "low-end discipline" | ✓ All three edits preserve or strengthen low-end / floor framing |
| Voice register (chapter's first-person conversational + spelled-out 1960-price) | ✓ Options 1A + 2A + 3A all preserve register |

---

## §5. Phase C application sequencing

This artifact is PROPOSED. **Phase C application of ratified cascade spot-fixes is a separate session** that fires after author ratification. The application-session sequencing below is the recommended order when that session spins up.

### §5.1 Pre-application verification

The Phase C session should:

1. Verify `origin/main` tip has not advanced past `5fe6af6` in a way that would shift the three target lines. Use the `grep` anchor strings in §5.3 below rather than line numbers; safer against drift.
2. Verify the three sites still match the §3 chapter-text quotations verbatim (no further edits have landed). If any has drifted, halt and reconcile against current Ch 8 state before applying.
3. Confirm author ratification record is captured (preferably as a recorded ratification entry in the §4.1 table above, signed in by author with date and Option-letter selection per site).

### §5.2 Recommended application order

In order of lowest-risk-to-highest-substance:

1. **Site 3 (line 166) — Option 3A:** Pure Mode-A verbatim-residual replacement. Single mechanical swap. Apply first as a low-risk warm-up.
2. **Site 1 (line 40) — Option 1A:** Mixed Mode-A + Mode-B (residual swap + rhetorical hedge). Two coupled changes in one line.
3. **Site 2 (line 52) — Option 2A:** Pure Mode-B rhetorical reframing of a strict-inequality claim. Highest substance shift; apply last so prior touches have settled.

After all three apply, the application session should:
- Re-verify lines 24 + 40 + 52 + 64 + 74 + 166 + 168 read coherently as a sequence.
- Re-verify the cumulative-build narrative (DH → Env → Community → Foreclosure → Sum) reads cleanly.
- Run the corpus-invariant scan (`tools/scripts/check-corpus-invariants.sh`) to confirm no scaffolding / regressed-pattern issues introduced.

### §5.3 Edit anchor strings (preferred over line numbers — `grep`-safe)

For the application session's Edit-tool unique-context matches:

**Site 1 anchor (current line 40):**
> "Two to four dollars. Against a market price of four-fifty in 1960. Direct health alone"

**Site 2 anchor (current line 52):**
> "already places the national severed cost at three to seven dollars — already above the 1960 market price, before any foreclosure pricing at all."

**Site 3 anchor (current line 166):**
> "Against a market price of $4.50 in 1960. Against a market price of $40 to $140 today"

(Line 238 anchor for the optional bundled application of §3.4.A, if author chooses to bundle: `"the four-dollar-and-fifty-cent invoice is the severed cost"`.)

### §5.4 Post-application commit-message sketch

Suggested commit message structure for the application session:

```
Ch 8 MED-3 + MED-6 cascade reconciliation Phase C — 3 ratified spot-fixes

Phase C application of three cascade residuals from Ch 8 Pass 1 Phase C
(commit 5fe6af6, 2026-05-21). Cascade source: MED-3 R1 ratification
($0.80/ton → $1-$1.50/ton range; BLP canonical lock) + MED-6 hedge
($4.50 → "four to five dollars"); both applied 2026-05-21 to lines
24 + 34 + 38 + Ch 6 line 24 in 5fe6af6 left three adjacent prose sites
in internal-chapter tension. This commit applies the three author-
ratified reconciliation edits.

Source artifact:
- tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch8_med3_med6_cascade_reconciliation_v1.0.0.md
  (Stage-3 cascade-reconciliation; 3 cascade sites; Option 1A + 2A + 3A
   author-ratified)

Ch 8 edits (3) — manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md:
- Site 1 (line 40, Option 1A): "four-fifty" → "four to five dollars" +
  "returns roughly as much as" → "already returns most of what".
- Site 2 (line 52, Option 2A): "already places . . . at three to seven
  dollars — already above the 1960 market price" → "already brings . . .
  up to the 1960 market price — at three to seven dollars per ton,
  comparable to what the coal cleared for at the mine mouth".
- Site 3 (line 166, Option 3A): "market price of $4.50 in 1960" →
  "1960 market price of four to five dollars".

[OPTIONAL — if author bundles §3.4.A line 238]
- Site 4 (line 238, bundled): "four-dollar-and-fifty-cent invoice"
  → "four-to-five-dollar invoice" (closing-paragraph mirror harmonization).

Discipline:
- All edits are intra-chapter body-prose hedge changes; no apparatus,
  no cross-chapter cascade, no named-subject consent impact.
- Per CLAUDE.md content-edit-with-prior-ratification discipline:
  fast-forward merge to origin/main + push at session close.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

---

## §6. Post-application flag-forward items (out-of-scope this session; surface for separate Pass-2 / Pass-3 / cross-corpus work)

Items that surfaced during cascade trace but lie outside the named-three-sites scope. **None require ratification this session.** Each is captured for future-session prioritization.

### §6.1 — Line 238 closing-paragraph $4.50 mirror residual

Per §3.4 above. The author may bundle into Site 3's Phase C application or defer to Pass-2 voice-polish. **Recommended:** bundle into Site 3 application (one-touch mechanical mirror; would otherwise pay per-session overhead for a single edit).

### §6.2 — HIGH-3 IPG ratio (33–122×) — MED-6 sensitivity check

Line 168's canonical IPG ratio "thirty-three and one hundred and twenty-two times the 1960 sale price" uses an implicit $4.50 denominator anchor ($558/$4.50 ≈ 124, canonical-rounded to 122). Under MED-6 hedge, the upper bound widens slightly to $558/$4 = 139.5; the lower bound narrows slightly to $558/$5 = 111.6.

The 33–122× lock is cross-corpus canonical per HIGH-3 + the cross-corpus IPG canonical-construction artifact (`5fe6af6` Option D); a Phase B (whole-book) cross-corpus audit may want to verify whether the lock should formally widen or remain at 33–122× as a stipulated canonical-anchor. **Not in cascade scope; flag-forward only.**

### §6.3 — Line 74 carbon-tail-vs-market-price comparator — MED-6 robustness verified

Verified in §4.2 above: line 74's "more than a hundred against the 1960 mine-mouth" holds under MED-6 hedge ($544/$5 = 108.8; $544/$4 = 136; both ≥ 100). The HIGH-3 carbon-tail-only ratification at line 74 is already MED-6-robust. **No action required; positive verification logged here for completeness.**

### §6.4 — Line 64 running-total-vs-market-price comparator — MED-6 robustness verified

Verified in §4.2 above: line 64's "approaching twice the 1960 market price" holds under MED-6 hedge ($8/$4 = 2.0; $8/$5 = 1.6; both within the "approaching twice" register). The MED-4 ratification at line 64 is already MED-6-robust. **No action required; positive verification logged here for completeness.**

### §6.5 — Pass-2 voice-polish carry-forward (informational; from parent audit §9)

Parent audit §9 (Pass 2 voice-polish future-session input) flagged the "numerical-claim declarative-three-in-a-row" pattern at line 41 (current line 40) as a voice-polish target: *"three short declaratives in succession with no sentence-length variance."* Option 1A's edit preserves the three-declarative structure ("Two to four dollars. Against a market price of four to five dollars in 1960. Direct health alone . . ."); a Pass-2 voice-polish session may want to vary sentence-length across the three declaratives. **Not a Pass-1 cascade issue; carried forward to Pass-2 voice-polish session for that chapter.**

---

## §7. Provenance + audit-trail

- **Author of artifact:** Claude (Opus 4.7) working on commons-bonds repo under PM dashboard #20 (Manuscript Stage-3 Rigor Pass workstream).
- **Triggering session:** Ch 8 Pass 1 Phase C application session 2026-05-21 (commit `5fe6af6`), which surfaced these three cascade sites in its commit-message "Residuals" section and explicitly deferred them to this follow-up session.
- **Cross-validation against parent audit:** All three site analyses cross-checked against parent audit findings MED-3 (§3 lines 214–239) + MED-6 (§3 lines 288–305) + MED-4 (§3 lines 243–263; running-total robustness) + HIGH-3 (canonical IPG cross-corpus artifact).
- **Branch:** `claude/ch8-med3-med6-cascade-reconciliation-focused-colden-cfea1f` (fresh feature branch from `origin/main` per CLAUDE.md branch-discipline; rigor-pass artifact will autonomously fast-forward to `main` at session close per CLAUDE.md merge-to-main default for rigor-pass artifacts that propose-but-do-not-apply prose changes).
- **Stage / pass placement:** Stage 3 Pass 1 (fact-check) residual-reconciliation; the cascade-reconciliation work is Pass-1-scoped because the originating findings (MED-3 + MED-6) are Pass-1 fact-check items. Voice-polish considerations (e.g. §6.5 declarative-three-in-a-row) are correctly carried forward to Pass-2.

---

*End of Ch 8 MED-3 + MED-6 cascade-reconciliation artifact — PROPOSED. Author ratification of §4.1 table gates Phase C application; Phase C is a separate session.*
