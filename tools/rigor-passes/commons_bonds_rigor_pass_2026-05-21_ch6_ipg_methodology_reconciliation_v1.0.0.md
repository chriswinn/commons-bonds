# Stage-3 Rigor Pass — Ch 6 IPG Methodology-Reconciliation

**Date:** 2026-05-21
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A follow-on (per-chapter methodology-reconciliation deferred from Ch 8 Pass 1 Phase C application session, commit `5fe6af6`)
**Chapter file:** [manuscript/chapters/Chapter__6_ThreeWaysofCounting.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) — 341 lines total at session start.
**Mode:** Methodology-reconciliation artifact (Stage-3-style; not a full Ch 6 fact-check / voice-polish / audience-load pass). Scope is the in-Ch 6 McDowell IPG methodology drift surfaced by the cross-corpus IPG canonical-construction decision (commit `57575b1`, 2026-05-21) and flagged for separate Ch 6 session in §5.3 + §6.2 of that artifact.
**Hard constraint observed:** No chapter files modified in this session. Phase C application of ratified spot-fixes is a separate session.

---

## §1. Scope + canonical sources consulted

### §1.1. Scope

This session locates every McDowell IPG reference in current Ch 6 and reconciles each against the corpus-wide canonical lock (33–122× per the 1960 sale price, Option D ratified 2026-05-21 in the cross-corpus canonical-construction artifact). For each site, the session determines whether the figure is (a) consistent with the canonical, (b) methodologically distinct but legitimate at that site, or (c) drifted and in need of canonical alignment, and surfaces ratification options under the Amendment-C Interactive Ratification Protocol.

Out of scope: full Ch 6 fact-check (Pass 3.1); voice-polish (Pass 3.2); audience-load acceptance (Pass 3.3) or robustness (Pass 3.4); developmental-edit (Pass 3.5). Those are separate session types per the v3.1 pipeline doctrine. This session is a targeted methodology-reconciliation: the McDowell IPG figures only, narrowly enough that the recommended spot-fixes apply atomically without coupling into a chapter-wide audit.

### §1.2. Canonical sources consulted

1. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md) — parent canonical-construction decision; ratified Option D 2026-05-21; flags this Ch 6 work as deferred-to-separate-session in §5.3 + §6.2. Headline: **canonical McDowell IPG range = 33–122× the 1960 sale price.**
2. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md) — Ch 8 Pass 1 fact-check parent audit; HIGH-3 is the cross-corpus IPG canonical question that drove this whole work.
3. [tools/audits/cross-chapter-consistency-inventory_2026-05-11.md](tools/audits/cross-chapter-consistency-inventory_2026-05-11.md) line 89 — McDowell IPG canonical-lock row, updated 2026-05-21 to flag the Ch 6 line-reference drift for separate Ch 6 session (this session).
4. [manuscript/chapters/Chapter__2_TheMiner__Draft.md](manuscript/chapters/Chapter__2_TheMiner__Draft.md) line 121 — canonical home for the McDowell IPG framing ("between 33 and 122 times the price the coal actually sold for, depending on which cost categories you include and which social cost of carbon estimate you use for the combustion tail"; "the floor is 33 times"; "Chapter 8 walks the floor-estimate version . . . the per-ton honest price that chapter calculates lands at the upper end of this range").
5. [manuscript/chapters/Chapter__6_ThreeWaysofCounting.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) — full chapter; targeted lines 30, 34, 163, 175, 249 (verified via current-state grep — see §2.1).
6. [manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md](manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) lines 74 + 168 + 212 — applied canonical framings post commit `5fe6af6`. Lines verified per current-state read.
7. [core/technical-appendix/TechnicalAppendix_v2.0.0.html](core/technical-appendix/TechnicalAppendix_v2.0.0.html) §3.6 Block 4 (~line 1100) — Three Ways triangulation table showing McDowell IPG at "~$2,400/ton; IPG ~50× (2025$)"; §11.11 (line 6199) — **"IPG-table reconciliation (33-122x canonical → 50-555x triangulated range)"** — the Tech Appendix's own explicit reconciliation of the two ranges as different-time-horizon-attribution, with a named pedagogical implication for Ch 6: *"the canonical 33–122× report and the triangulated 50–555× range both correctly describe McDowell's IPG, at different time-horizons. The framework is not committed to a single number; it is committed to a method that makes the time-horizon attribution explicit."*
8. [tools/memory/feedback_audit_open_illustrative_default.md](tools/memory/feedback_audit_open_illustrative_default.md) — open/illustrative reading default for chapter-vs-framework audits.
9. [tools/memory/feedback_verify_stale_memory_claims.md](tools/memory/feedback_verify_stale_memory_claims.md) — verify line numbers in current file state rather than trusting inventory citations.

### §1.3. Verification of inventory line citations (verify-stale-memory-claims discipline)

The pre-session inventory line 89 entry (pre 2026-05-21 update) referenced Ch 6 line 486 ("per-case 33–122×") + Ch 6 line 625 ("IPG of 33") as the canonical reconciliation prose. Verification against current Ch 6 file state:

```
wc -l manuscript/chapters/Chapter__6_ThreeWaysofCounting.md
     341 manuscript/chapters/Chapter__6_ThreeWaysofCounting.md
```

Current Ch 6 file is **341 lines** total. Both prior inventory line citations (486 + 625) **do not exist** in the current file. The inventory citation is stale relative to the current file. Two possible explanations:

- (a) The inventory citation was always referencing a prior Ch 6 revision that has since been substantially rewritten; the "per-case 33–122×" reconciliation prose was lost in that rewrite.
- (b) The inventory citation referenced an earlier chapter-version with different line numbering and the substantive reconciliation prose was preserved at different line numbers; the line-number-only drift is a citation update rather than a substantive content loss.

Resolution: §2.1's full IPG-references-in-current-Ch 6 scan settles which explanation holds. **Result:** the current Ch 6 file contains no "per-case 33–122×" reconciliation prose at any line. Current Ch 6 carries the McDowell IPG at three distinct sites (lines 34 + 175 + 249); none of those sites carries the explicit 33–122 reconciliation the prior inventory citation expected. Explanation (a) holds. The reconciliation prose was lost in a prior Ch 6 rewrite. This finding is addressed in §3 below as a structural question: should the reconciliation prose be reintroduced.

---

## §2. Methodology

### §2.1. Full IPG-references scan of current Ch 6

Grep across the file for `(IPG|intergenerational pricing gap|times the|underprice|cost severance|true cost.*market price)` returned candidate sites. After filtering for McDowell-IPG-specific drift (rather than generic framework-vocabulary references), three load-bearing sites surface, plus one peripheral site:

**Load-bearing McDowell IPG sites:**

- **Line 34** — implicit IPG range derived from bottom-up Method 1 walkthrough. Prose: *"Include carbon, and the bottom-up total rises to roughly $449 to $464 per ton. Against $4.50, or even $140, the market is capturing roughly one to thirty percent of the actual cost. The carbon term dominates."* Implicit IPG arithmetic: $449/$4.50 ≈ 100×; $464/$4.50 ≈ 103× (≈ "100" at 1960 mine-mouth); $449/$140 ≈ 3.2× (≈ "3.3" at today's high market price). **Implicit IPG range ≈ 3–100×.**
- **Line 175** — explicit chapter IPG headline. Prose: *"McDowell coal's per-case implied IPG of approximately fifty times (per the Technical Appendix's implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate; the variance reflects time-horizon attribution (1960 nominal mine-mouth price versus 2025 real cost-severance) more than framework imprecision."* **Explicit IPG range = 50–555× triangulated; mid-range anchor "approximately fifty times."**
- **Line 249** — Parfit non-identity anchor. Prose: *"the framework's IPG of 33 (the McDowell-coal compression) is the empirical apparatus that prices what is owed under that commitment."* **Anchored at canonical floor only (IPG of 33; named "the McDowell-coal compression").**

**Peripheral McDowell-adjacent site:**

- **Line 30** — pre-carbon bottom-up framing. Prose: *"even without climate accounting the market has been capturing somewhere between roughly a quarter and a half of the actual cost. Not a rounding error. A factor."* Implicit IPG arithmetic (pre-carbon): 1/(1/4 to 1/2) = 2–4×. **Pre-carbon-only; explicitly bracketed as pre-carbon, not a McDowell-IPG headline drift.** Not a load-bearing site for this reconciliation; flagged for completeness.

**Non-McDowell other-case IPGs at lines 36 + 175 + Ch 6 convergence table (line 163):**

- Line 36 — Deepwater Horizon 15–17×, Libby 55–82×, Exxon Valdez 1,200–1,900× — non-McDowell; per cross-chapter inventory rows 91 + 93 + 94, these are consistent across the corpus and not in this reconciliation's scope.
- Line 163 (the convergence table) — per-method per-ton RCV figures, not ratio. Underlying anchor for line 175's "approximately fifty times" computation (M1 floor $261 / inflation-corrected 1960 $50 ≈ 50; mid-M3 $2,500 / nominal 1960 $4.50 ≈ 555). The table itself is methodologically a per-method estimate report, not an IPG headline.

### §2.2. The methodological question per site

For each load-bearing site, the reconciliation question is one of three forms:

- **Drift-from-canonical**: does the site report a McDowell-IPG number inconsistent with the 33–122× canonical?
- **Different-but-legitimate**: does the site report a number from a different-but-legitimate parameter-variation construction (different numerator components; different denominator era; different time-horizon attribution; etc.) that the corpus should preserve as a distinct construction rather than collapse into the canonical?
- **Missing-reconciliation**: does the site report a different range without explicit cross-reference to the canonical, in a way that risks the reader reading the two ranges as conflicting?

Per-site reading per these three forms is in §3 below.

### §2.3. The Tech Appendix's already-written reconciliation

A material discovery this session needs to surface at the methodology level: the Technical Appendix already contains an explicit reconciliation of the 33–122× canonical and the 50–555× triangulated range. [Tech Appendix §11.11](core/technical-appendix/TechnicalAppendix_v2.0.0.html) (line 6199 in the v2.0.0 HTML source) carries the heading *"IPG-table reconciliation (33-122x canonical → 50-555x triangulated range)"* and states three reconciliation findings:

1. *"The two ranges are not in tension."* The 33–122× canonical reflects Method-1-anchored estimates with conservative time-horizon attribution; the 50–555× triangulated range reflects Methods 1+2+3 with Method 3's α-irreversibility-premium for multi-generational time scale.
2. *"The variance reflects time-horizon attribution, not framework imprecision."* Method 1 (replacement-cost) anchors at engineering-time-scale (decades); Method 3 with α-dominance reflects multi-generational-time-scale irreversibility-premium. Both are correct RCV measurements at their respective time scales.
3. *Pedagogical implication for Ch 6:* "*when Ch 6 walks through the McDowell convergence table, the reconciliation should be made explicit — 'the canonical 33–122× report and the triangulated 50–555× range both correctly describe McDowell's IPG, at different time-horizons. The framework is not committed to a single number; it is committed to a method that makes the time-horizon attribution explicit.'*"

This is a load-bearing finding for §3 below: the Tech Appendix has already done the reconciliation work; what is missing is its surfacing in Ch 6's running prose. Ch 6 line 175 currently references the Tech Appendix §3.6 Block 4 (the triangulation table) but does NOT cross-reference Tech Appendix §11.11 (the explicit reconciliation of the two ranges) or the canonical 33–122 range itself. The reconciliation exists; it is not surfaced in Ch 6 in the form the appendix specifies.

---

## §3. Per-finding analysis

### §3.1. Finding 1 (HIGH) — Ch 6 line 175 lacks the explicit canonical reconciliation the Tech Appendix §11.11 prescribes

**Site:** Ch 6 line 175 — the chapter's explicit McDowell IPG headline.

**Current prose:**

> McDowell coal's per-case implied IPG of approximately fifty times (per the Technical Appendix's implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate; the variance reflects time-horizon attribution (1960 nominal mine-mouth price versus 2025 real cost-severance) more than framework imprecision.

**The drift, precisely:** the prose reports the triangulated 50–555× range as if it were the chapter's IPG headline without cross-reference to the corpus-canonical 33–122× range, which Ch 2 line 121 anchors as canonical home + Ch 8 line 168 carries as canonical headline + cross-chapter inventory line 89 carries as canonical lock. A reader who has Ch 2 in hand and arrives at Ch 6 line 175 carrying "33–122 times the 1960 sale price; floor 33" forward will encounter "approximately fifty times" + a much wider 50–555 range without explicit signposting that the two ranges are the SAME object computed two different ways (different methods + different time-horizon-attribution per Tech Appendix §11.11).

**Severity classification: HIGH.** Ch 6 is the methodology-introduction chapter; the IPG formula is defined on Ch 6 line 119 (`IPG = RCV / P_market`). The reader meets the IPG arithmetic for the first time IN this chapter. If the chapter's headline range silently diverges from the canonical without cross-reference, the reader receives the cross-corpus inconsistency at the moment they are being taught the methodology — exactly the worst pedagogical moment for the drift to land. The Tech Appendix §11.11's explicit prescription that this reconciliation should be made explicit in Ch 6 elevates this to HIGH: the doctrinal recommendation already exists in the corpus; what is missing is its surfacing.

**The drift is methodologically legitimate but pedagogically unsurfaced.** Per Tech Appendix §11.11, the 50–555× range is correct (Methods 1+2+3 with α-dominance applied at multi-generational time scale) and the 33–122× range is correct (Method-1-anchored with conservative engineering-time-scale attribution); both are valid RCV measurements at their respective time scales. The finding is not that Ch 6 reports the wrong number — it is that Ch 6 does not explain that the number it reports is a different time-horizon-attribution of the same underlying object the canonical Ch 2 + Ch 8 figures report.

**Options:**

- **Option A (light cross-reference)** — Add one sentence to line 175 that explicitly names the 33–122× canonical and cross-references Tech Appendix §11.11. Preserves the chapter's triangulated headline as primary; adds the canonical cross-reference as a one-sentence reconciliation. Smallest prose addition; preserves Ch 6's pedagogical flow.
- **Option B (full reconciliation paragraph)** — Add a new paragraph after line 175 (or restructure 173–179) that explicitly reproduces the Tech Appendix §11.11 reconciliation in the chapter's running prose: names both ranges, names the time-horizon-attribution difference, cross-references Ch 2 + Ch 8 + Tech Appendix §11.11. Matches what the Tech Appendix §11.11 explicitly prescribes for Ch 6 ("the reconciliation should be made explicit"). Larger prose addition; restores the kind of "per-case 33–122×" reconciliation prose the prior inventory citation expected to find at Ch 6 (per §1.3 above). This is the option Tech Appendix §11.11's pedagogical implication directly recommends.
- **Option C (lead-with-canonical restructure)** — Restructure line 175 to lead with the 33–122× canonical and introduce the triangulated 50–555× range as the chapter's value-add over the canonical. Largest rewrite; reorients the chapter's IPG headline around the canonical rather than around the triangulation. Risk: collapses Ch 6's distinctive triangulation contribution into a canonical-recap, losing the methodological novelty Ch 6 introduces.

**Recommendation: Option B.** Tech Appendix §11.11 explicitly prescribes this option ("when Ch 6 walks through the McDowell convergence table, the reconciliation should be made explicit"). The chapter has the room for a reconciliation paragraph at the point where the triangulation lands (right after lines 173–179, where the per-case figures are summarized); a paragraph-level addition restores the explicit reconciliation prose the prior inventory citation expected to find at Ch 6 line 486 + line 625, and it does so in the form the Tech Appendix itself recommends. The Option B prose preserves Ch 6's triangulation as the chapter's value-add (the 50–555 range is what Ch 6 contributes that Ch 2 + Ch 8 do not), while making the cross-corpus coherence explicit at the chapter's IPG-headline moment.

**Reasoning:**

- Option A is the lowest-friction option but is structurally under-specified relative to what the Tech Appendix §11.11 recommends. A one-sentence cross-reference would name the 33–122 canonical without doing the time-horizon-attribution work that the appendix specifically says is the pedagogical key. A reader who follows the cross-reference to Ch 2 will see 33–122 and to Ch 6 will see 50–555; without the time-horizon-attribution explanation in Ch 6's running prose, the reader has to consult Tech Appendix §11.11 to understand why both are correct. That makes the chapter's IPG headline depend on appendix consultation for coherence — a pedagogical anti-pattern in a methodology-introduction chapter.
- Option C overshoots the question. The chapter's triangulation is its substantive contribution; collapsing it into a 33–122-canonical lead loses what Ch 6 adds. The 50–555 range is methodologically more complete than the 33–122 range (more methods + α-dominance at multi-generational time scale); making it secondary to the conservative bottom-up range inverts the methodological hierarchy.
- Option B does the right pedagogical work: surfaces the reconciliation in the chapter's running prose, preserves the chapter's triangulation contribution as primary, restores explicit cross-corpus coherence, and matches the Tech Appendix's own prescription for how to do this exact reconciliation in Ch 6.

**Proposed Option B prose** (verbatim replacement for current line 175 + new paragraph after it):

> McDowell coal's per-case implied IPG of approximately fifty times — anchored at the Technical Appendix's three-method implied cost-severance summary in §3.6 Block 4 — falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate.
>
> A reader carrying Chapter 2's framing forward will notice a different number: Chapter 2 anchored the McDowell IPG at thirty-three to one hundred and twenty-two times the 1960 sale price; Chapter 8 walked the worked floor estimate to the upper end of that range. The two ranges are not in tension. The thirty-three-to-one-twenty-two-times canonical reflects Method 1 — Replacement Cost — alone, anchored to engineering-time-scale substitutability. The fifty-to-five-hundred-fifty-five-times triangulated range reflects all three methods including Method 3's scarcity-and-irreversibility premium at multi-generational time scale. Both correctly describe McDowell's intergenerational pricing gap; they differ in *which time horizon* the accounting is anchored to. The framework is not committed to a single number; it is committed to a method that makes the time-horizon attribution explicit. (Formal reconciliation in [Technical Appendix §11.11 — IPG-table reconciliation](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-11-11-ipg-reconciliation).)

The proposed prose replaces only line 175 + adds one paragraph between lines 175 and 177 (which currently runs "Libby's documented cost-to-revenue ratio of forty-times . . ."). Net Ch 6 prose change: ~150 words added; no prose removed.

---

### §3.2. Finding 2 (LOW) — Ch 6 line 249 anchors the Parfit reference at the canonical floor (IPG of 33) without naming the range

**Site:** Ch 6 line 249 — the Parfit non-identity passage's empirical anchor.

**Current prose:**

> The moral standing of future generations is, in Parfit's framework, a defensible philosophical commitment — and the framework's IPG of 33 (the McDowell-coal compression) is the empirical apparatus that prices what is owed under that commitment.

**Status: Consistent-at-floor with deliberate compression framing.** The site anchors only on the canonical floor (IPG of 33), explicitly named as "the McDowell-coal compression." The parenthetical "(the McDowell-coal compression)" signals to the reader that this is the compressed/floor anchor of the canonical range — i.e., the author has chosen the most-defensible single number from the canonical 33–122 range for the Parfit anchor. This is a deliberate rhetorical move: the Parfit non-identity argument is doing philosophical work, and anchoring on the canonical floor rather than the full range carries the empirical claim with maximum defensibility (the floor is the least-contested number; the ceiling would invite parameter-variation challenge at the philosophical-anchor moment).

**The legitimacy of the floor-only anchor:** the canonical 33–122 range's floor is the most-defensible single-number representation of the canonical, precisely because the range's parameter-variation surface (SCC + cost-category inclusion) has its bottom at 33 across plausible parameter choices. Anchoring on the floor is the conservative claim; it does not overclaim, and it survives any reader's parameter-variation skepticism. A reader who arrives at line 249 carrying "33–122" forward from Ch 2 will read "IPG of 33 (the McDowell-coal compression)" as the floor-anchor of the range they already know — which is exactly the pedagogical job the parenthetical does.

**Severity classification: LOW.** No drift from canonical; the floor-only anchor is a deliberate rhetorical choice; the "(the McDowell-coal compression)" parenthetical does the cross-reference work without requiring full-range explication at the philosophical-anchor moment.

**Options:**

- **Option A (no change)** — leave as-is. The current prose is consistent with the canonical floor + carries the deliberate compression framing that signals the floor-anchor choice. No spot-fix required.
- **Option B (range-with-floor restatement)** — change to "IPG of 33 to 122 (the McDowell-coal compression at 33 times)" or similar. Names the full canonical range; preserves the compression anchor; adds prose. Risk: makes the philosophical-anchor sentence longer at exactly the moment the argument is doing philosophical work and benefits from a clean empirical anchor.
- **Option C (light cross-reference)** — change to "IPG of 33 — the floor of the McDowell-coal canonical range Chapter 2 introduces — is the empirical apparatus . . ." Names the canonical home cross-reference; preserves the floor anchor; slightly more cross-corpus-coherent.

**Recommendation: Option A — no change.** The current prose is pedagogically correct as written. The "(the McDowell-coal compression)" parenthetical is doing the cross-reference work the philosophical-anchor sentence needs without overburdening it. Reader carrying 33–122 from Ch 2 reads "IPG of 33 (the McDowell-coal compression)" as floor-anchor of that range — coherence holds. The Finding 1 reconciliation paragraph (proposed for line 175) establishes the cross-corpus reading earlier in the chapter, so a reader arriving at line 249 has already encountered the explicit canonical-vs-triangulated reconciliation and can read the floor-anchor at line 249 as a deliberate compression choice. Option A relies on Finding 1's reconciliation having been applied first; the chain holds.

**Reasoning:**

- Option B's range-restatement makes the Parfit anchor sentence longer at the moment the argument needs maximum compression. The compression is rhetorical: the IPG-of-33 lands as the empirical anchor of an argument that has just walked through Parfit's non-identity problem. A single number lands better here than a range.
- Option C's cross-reference is structurally reasonable but redundant if Finding 1 is ratified (the cross-corpus reading is established at line 175 + the new reconciliation paragraph; line 249 doesn't need to re-establish it). If Finding 1 is *not* ratified, Option C becomes the recommendation here. Conditional recommendation: A if Finding 1 ratified, C if Finding 1 not ratified.

---

### §3.3. Finding 3 (LOW) — Ch 6 line 34 carries an implicit IPG range from the bottom-up Method 1 walkthrough that differs from the post-Option-D Ch 8 framing

**Site:** Ch 6 line 34 — the bottom-up Method 1 walkthrough's market-capture-share framing.

**Current prose:**

> Include carbon, and the bottom-up total rises to roughly $449 to $464 per ton. Against $4.50, or even $140, the market is capturing roughly one to thirty percent of the actual cost. The carbon term dominates.

**Implicit IPG arithmetic:** $449/$4.50 ≈ 100× (1960 mine-mouth); $449/$140 ≈ 3.2× (today's high market price). **Implicit IPG range ≈ 3–100×.**

**The construction:** this is the same parameter-variation construction Ch 8 line 168 *originally* carried (vary market price across eras, hold numerator fixed) that the canonical-construction decision (Option D, commit `5fe6af6`) resolved. After Option D, Ch 8 line 168 leads with the canonical 33–122× range + today-prices follow-up. Ch 6 line 34 still carries the vary-market-price construction implicitly, with a different numerator ($449–$464 bottom-up Method 1 stack with $190 SCC) than Ch 8's $558 8-component honest floor.

**Status: Methodologically distinct from the canonical, but legitimate at this site.** The construction at line 34 is pedagogical: the bottom-up Method 1 walkthrough has just enumerated cost components and added them ($449–$464), and the line-34 sentence is showing the reader how the bottom-up stack compares against the market price across eras. This is Method 1's own pedagogical output, not a chapter-IPG-headline claim. The chapter's IPG headline lives at line 175 (the triangulated 50–555 range, anchored on Tech Appendix §3.6 Block 4 + §11.11).

**The "1 to 30 percent of the actual cost" framing is making a different claim than an IPG headline:** it is showing that under bottom-up Method 1 accounting alone, the market captures only 1–30% of the cost across eras. The reader who follows the arithmetic gets the 3–100× implicit IPG range; the reader who follows the argument gets the structural finding (market captures a small fraction of the actual cost across every era).

**Severity classification: LOW.** Pedagogical-context-specific construction; not a chapter-IPG-headline drift; consistent with the Method-1-walkthrough framing the chapter is doing at lines 20–54. The "approximately fifty times" headline at line 175 is the chapter's actual IPG claim, anchored on the triangulated three-method result. Line 34's implicit 3–100× is Method 1 alone, which Tech Appendix §11.11 explicitly identifies as the more-conservative range that the 33–122 canonical reflects ("Method-1-anchored estimates with conservative time-horizon attribution").

**Options:**

- **Option A (no change)** — leave as-is. Line 34 is doing pedagogical Method 1 walkthrough work, not chapter-IPG-headline work. The implicit 3–100× range is consistent with Method 1's parameter-variation surface; the chapter's IPG headline arrives later (line 175) with the triangulated 50–555 range; the canonical 33–122 reconciliation lands at the new reconciliation paragraph (per Finding 1 Option B).
- **Option B (light disambiguation phrase)** — add a brief phrase to line 34 that signals "this is Method 1 alone; the chapter's full IPG headline includes Methods 2 + 3 and lands later." Example: "Include carbon, and the bottom-up total rises to roughly $449 to $464 per ton — and that is Method 1 alone, before Methods 2 and 3 add their own anchors." Adds methodological signposting; preserves the pedagogical flow.
- **Option C (rewrite to anchor on canonical 33–122)** — rewrite line 34's "1 to 30 percent" framing to reference the canonical 33–122 range directly. Risk: collapses the pedagogical Method 1 walkthrough into a canonical-recap at exactly the moment the chapter is teaching the reader how Method 1 works.

**Recommendation: Option A — no change.** The pedagogical-walkthrough context legitimizes the Method-1-specific implicit IPG. The chapter's actual IPG headline is at line 175 + the new reconciliation paragraph (per Finding 1); a reader arriving at line 34 carrying the canonical 33–122 framing forward from Ch 2 reads the "1 to 30 percent" as Method 1's specific output within the broader chapter argument that the next 140 lines build out. The chapter explicitly tells the reader at line 54 ("Even with this limitation, the bottom-up method gives a floor. It says that the market underprices extraction by at least a factor of several, and potentially by factors of tens or hundreds. It does not tell us the ceiling. For that, we need a method that does not rely on enumerating costs one by one.") that Method 1 is the floor and other methods come next — which is exactly the methodological signposting Option B would otherwise add.

**Reasoning:**

- Option B's disambiguation phrase is structurally reasonable but is already done by the chapter's own line-54 transition ("Even with this limitation, the bottom-up method gives a floor . . . For that, we need a method that does not rely on enumerating costs one by one"). Adding the same signposting at line 34 would be redundant.
- Option C's canonical-anchor rewrite would collapse Method 1's pedagogical walkthrough into a Ch 2 recap, losing the chapter's introduction-of-the-method work. The reader needs to see Method 1's specific arithmetic to understand the method; collapsing it into "see Ch 2's 33–122 canonical" deprives the reader of the methodology-walkthrough Ch 6 is doing.
- Option A trusts the chapter's existing pedagogical architecture — Method 1 walkthrough, then the line-54 transition that names Method 1 as the floor + signals more methods to come, then Methods 2 + 3 in their own sections, then the convergence table at line 163, then the triangulated IPG headline at line 175 + (per Finding 1 Option B) the explicit canonical reconciliation paragraph. The chapter's architecture handles the cross-corpus coherence without needing line 34 to redo it.

---

### §3.4. Finding 4 (MEDIUM) — The "per-case 33–122×" reconciliation prose previously referenced at Ch 6 lines 486 + 625 was lost in a prior Ch 6 rewrite

**Site:** Across-Ch-6 finding — the prior cross-chapter consistency inventory (line 89, pre 2026-05-21 update) referenced Ch 6 line 486 ("per-case 33–122×") and Ch 6 line 625 ("IPG of 33") as the canonical reconciliation prose. Current Ch 6 is 341 lines; neither line number exists.

**Verification:** per §1.3 above, the current Ch 6 file contains no "per-case 33–122×" reconciliation prose at any line. The inventory citation was always referencing a prior Ch 6 revision; the reconciliation prose was lost in a substantial Ch 6 rewrite that also reorganized the chapter from a per-case-reconciliation-anchored structure into the current three-methods-then-convergence-table structure.

**Status: Genuinely-missing reconciliation, but addressable by Finding 1.** The "per-case 33–122×" prose served two functions in the prior Ch 6 revision: (a) it made the canonical 33–122 reconciliation explicit in Ch 6; (b) it provided the inventory line 89 row's per-chapter-consistency anchor. Function (a) is exactly what Finding 1's Option B proposed prose does — surface the canonical reconciliation in Ch 6's running prose. Function (b) is satisfied once Finding 1's proposed prose is applied and the inventory line 89 row's "Ch 6 line 486" reference is updated to the new reconciliation paragraph's line number (post-Phase-C).

**Severity classification: MEDIUM.** The finding is genuinely-missing-prose at the corpus level — the inventory expected to find an explicit reconciliation in Ch 6 and could not — but the recommended Finding 1 spot-fix (Option B reconciliation paragraph after line 175) closes the gap. The MEDIUM severity reflects (a) the structural absence of the reconciliation prose is a real cross-corpus drift that the Tech Appendix §11.11 prescription has been waiting to be surfaced; (b) the gap is closed by Finding 1's spot-fix; (c) but if Finding 1 is not ratified, this finding becomes HIGH on its own merits because the corpus would carry an inventory citation pointing to nonexistent Ch 6 prose.

**Options:**

- **Option A (subsume into Finding 1)** — treat this finding as fully addressed by Finding 1's Option B (new reconciliation paragraph at line 175). The Phase C application of Finding 1 Option B also closes this Finding 4 gap. Inventory line 89's Ch 6 line-reference drift warning (added in commit `5fe6af6`) gets removed in the same Phase C touch.
- **Option B (separate Ch 6 reconciliation paragraph elsewhere in the chapter)** — add a separate reconciliation paragraph elsewhere in Ch 6 (e.g., near line 35 after the Method 1 walkthrough, or as a dedicated "Per-Case Cross-Chapter Reconciliation" subsection between current §"The Convergence" and §"The Norway Backtest"). Larger structural change; introduces a new chapter sub-section.
- **Option C (no action; trust the cross-chapter inventory annotation)** — leave Ch 6 without explicit reconciliation prose; trust that the inventory line 89's annotation ("Ch 6 carries 'IPG of 33' at line 249 + 'approximately fifty times' at line 175") handles the cross-chapter coherence. Risk: inventory is internal scaffolding; reader of the manuscript does not see it; the cross-corpus coherence depends on the inventory rather than on the manuscript itself.

**Recommendation: Option A.** Finding 1's Option B reconciliation paragraph is the natural home for the canonical reconciliation in Ch 6 — it lands at the chapter's IPG headline (line 175), exactly where the Tech Appendix §11.11 pedagogical implication says it should land. A separate reconciliation paragraph elsewhere (Option B) would duplicate the work; Option A consolidates Finding 1 and Finding 4 into a single Phase C touch.

**Reasoning:**

- Option B's separate-section reconciliation overshoots. Ch 6's structure is well-organized around the three-methods-then-convergence pattern; introducing a dedicated "Per-Case Cross-Chapter Reconciliation" sub-section would interrupt the chapter's pedagogical flow and would duplicate the reconciliation work that Finding 1 Option B already does at the natural site.
- Option C's no-action risks leaving the manuscript carrying a cross-corpus inconsistency that the cross-chapter inventory is silently patching. The inventory is internal scaffolding (per the two-layer content-origination discipline — WP#10); the manuscript itself should carry the cross-chapter coherence in its publisher-facing prose. Option C declines to do the work the Tech Appendix §11.11 explicitly says should be done in Ch 6.
- Option A consolidates the two findings into one spot-fix that does both functions (a) and (b) the prior inventory citation expected from Ch 6.

**Phase C consequence of Option A:** the same Phase C touch that applies Finding 1's Option B prose to Ch 6 line 175 + adds the new reconciliation paragraph after line 175 ALSO updates cross-chapter inventory line 89 to (a) remove the Ch 6 line-reference drift warning added in commit `5fe6af6`; (b) update the row's Ch 6 line citation to the new reconciliation paragraph's line number; (c) reflect that the Ch 6 reconciliation is now explicit in the manuscript's running prose. Inventory line 89 update prose is in §5.4 below.

---

## §4. Ratification summary

| Finding | Severity | Site | Recommended option | Phase C touch |
|---|---|---|---|---|
| **F1** — Line 175 lacks explicit canonical reconciliation | **HIGH** | Ch 6 line 175 | **Option B** (full reconciliation paragraph after line 175) | Ch 6 line 175 replacement + new paragraph; ~150 words added |
| **F2** — Line 249 anchors at canonical floor without naming range | LOW | Ch 6 line 249 | **Option A** (no change; conditional on F1 ratified) | None (if F1 ratified) |
| **F3** — Line 34 implicit Method-1 IPG range differs from canonical | LOW | Ch 6 line 34 | **Option A** (no change; chapter's existing line-54 transition does the signposting) | None |
| **F4** — Missing "per-case 33–122×" reconciliation prose (inventory citation stale) | MEDIUM | Across-Ch 6 | **Option A** (subsume into F1's spot-fix) | Subsumed into F1 |

**Net recommended Phase C touch:** one Ch 6 spot-fix (line 175 replacement + new paragraph) + one cross-chapter inventory line 89 update.

**Atomic-commit Phase C application surface:** Ch 6 + inventory. Two files. No Ch 2 or Ch 8 touches required (canonical home + canonical headline already align per commit `5fe6af6`).

---

## §5. Cross-chapter consequence list (recommended options only)

### §5.1. Ch 6 prose changes — line 175 replacement + new reconciliation paragraph (Finding 1 Option B)

**Current Ch 6 line 175:**

> McDowell coal's per-case implied IPG of approximately fifty times (per the Technical Appendix's implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate; the variance reflects time-horizon attribution (1960 nominal mine-mouth price versus 2025 real cost-severance) more than framework imprecision.

**Proposed verbatim replacement** (replaces the existing one paragraph with two paragraphs; line 175 becomes the first; the second is new):

> McDowell coal's per-case implied IPG of approximately fifty times — anchored at the Technical Appendix's three-method implied cost-severance summary in §3.6 Block 4 — falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate.
>
> A reader carrying Chapter 2's framing forward will notice a different number: Chapter 2 anchored the McDowell IPG at thirty-three to one hundred and twenty-two times the 1960 sale price; Chapter 8 walked the worked floor estimate to the upper end of that range. The two ranges are not in tension. The thirty-three-to-one-twenty-two-times canonical reflects Method 1 — Replacement Cost — alone, anchored to engineering-time-scale substitutability. The fifty-to-five-hundred-fifty-five-times triangulated range reflects all three methods including Method 3's scarcity-and-irreversibility premium at multi-generational time scale. Both correctly describe McDowell's intergenerational pricing gap; they differ in *which time horizon* the accounting is anchored to. The framework is not committed to a single number; it is committed to a method that makes the time-horizon attribution explicit. (Formal reconciliation in [Technical Appendix §11.11 — IPG-table reconciliation](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-11-11-ipg-reconciliation).)

**Net Ch 6 prose change:** ~150 words added; one paragraph becomes two; no prose removed.

**Note on Tech Appendix anchor link:** the proposed cross-reference `#sec-11-11-ipg-reconciliation` assumes the Tech Appendix HTML carries a section ID matching the §11.11 heading. The current Tech Appendix HTML (line 6199–6258) uses the heading text but the closest existing section ID at that scope is `id="sec-11-x-empirical-cases"` (per §11.1–§11.11 grouping). Phase C application should verify the exact anchor ID — if §11.11 does not carry its own ID, either add one in the same Phase C touch or use a parent-section anchor with text-fragment hint. This is a Phase-C-implementation detail; flagged here for the application session.

### §5.2. Ch 2 prose changes

**No change required.** Ch 2 line 121 already carries the canonical "between 33 and 122 times" + "the floor is 33 times" + the explicit anchor that "Chapter 8 walks the floor-estimate version . . . lands at the upper end of this range." The proposed Ch 6 reconciliation paragraph explicitly cross-references Ch 2's framing; no Ch 2 rewrite needed.

### §5.3. Ch 8 prose changes

**No change required.** Ch 8 line 168 already carries the canonical 33–122× framing as headline + today-prices follow-up (applied in commit `5fe6af6` per the canonical-construction decision Option D). The proposed Ch 6 reconciliation paragraph explicitly cross-references Ch 8's worked-floor-estimate-at-upper-end framing; no Ch 8 rewrite needed.

### §5.4. Cross-chapter consistency inventory line 89 update

**Current row text** (post commit `5fe6af6`):

> | **McDowell IPG range** | 33–122× (floor 33; Ch 6 compression 33) | Ch 2 line 121 | Ch 8 line 168 carries the canonical 33–122× framing as headline + today-prices follow-up ("even at today's $40–$140 prices, the carbon term alone exceeds market by ≥4×"; structural-finding beat, not competing canonical). Ch 6 carries "IPG of 33" at line 249 (Parfit non-identity passage) + "approximately fifty times" at line 175 (new triangulation register). **⚠ Ch 6 line-reference drift flagged:** prior row text referenced Ch 6 line 486 ("per-case 33–122×") + Ch 6 line 625, which do not appear in current Ch 6 file (341 lines total); separate Ch 6 methodology-reconciliation finding required. Canonical IPG headline range (33–122×) **Consistent** across Ch 2 + Ch 8. |

**Proposed verbatim replacement** (post Phase C application of Finding 1 Option B):

> | **McDowell IPG range** | 33–122× canonical (floor 33; the McDowell-coal compression) + 50–555× triangulated (Methods 1+2+3 with α-dominance at multi-generational time scale); per Tech Appendix §11.11 the two ranges differ in time-horizon attribution and both correctly describe McDowell's IPG | Ch 2 line 121 | Ch 8 line 168 carries the canonical 33–122× framing as headline + today-prices follow-up ("even at today's $40–$140 prices, the carbon term alone exceeds market by ≥4×"; structural-finding beat). Ch 6 line 175 carries the triangulated 50–555× range with explicit canonical-vs-triangulated reconciliation paragraph (post Ch 6 IPG methodology-reconciliation Phase C, 2026-05-XX) cross-referencing Tech Appendix §11.11. Ch 6 line 251 carries the Parfit-anchor "IPG of 33 (the McDowell-coal compression)" as floor-anchor of the canonical range (post-Phase-C line number; was line 249 pre-Phase-C, shifted by +2 lines due to the new reconciliation paragraph at line 175). **Consistent** across Ch 2 + Ch 6 + Ch 8 + Tech Appendix; the two ranges (canonical 33–122× + triangulated 50–555×) are coherent under Tech Appendix §11.11's time-horizon-attribution reconciliation, now surfaced in Ch 6's running prose. |

**Net inventory change:** the canonical-lock cell expands from "33–122× (floor 33; Ch 6 compression 33)" to the dual-range "33–122× canonical + 50–555× triangulated" framing with the time-horizon-attribution reconciliation noted; the per-chapter-consistency cell is rewritten to reflect that the Ch 6 reconciliation is now explicit in the manuscript (the "⚠ Ch 6 line-reference drift flagged" warning is removed because the gap is closed by the Phase C spot-fix); the canonical-home cell is unchanged (Ch 2 line 121 remains canonical home).

### §5.5. Tech Appendix update (optional, Phase-C-implementation-dependent)

The proposed Ch 6 cross-reference `#sec-11-11-ipg-reconciliation` (per §5.1's "Note on Tech Appendix anchor link") may require adding a section ID to the Tech Appendix HTML's §11.11 heading if one does not currently exist. This is a Phase C implementation detail; the Tech Appendix touch is one HTML anchor addition (no prose change). Optional; if §11.11 already carries a usable anchor, the touch is unneeded.

---

## §6. Phase C application sequencing

### §6.1. Recommended sequencing

The recommended Phase C work is a single atomic commit touching two files (plus an optional Tech Appendix anchor addition):

1. **Ch 6 line 175** — replace existing one-paragraph IPG-headline prose with the two-paragraph reconciliation per §5.1 Finding 1 Option B.
2. **Cross-chapter inventory line 89** — replace existing canonical-lock row with the dual-range row per §5.4.
3. *(Optional)* **Tech Appendix §11.11** — add `id="sec-11-11-ipg-reconciliation"` to the §11.11 `<h3>` heading if one does not already exist (or use the closest parent-section anchor with a text-fragment hint in the Ch 6 cross-reference link).

**Phase C session scope:** small. Two files (three if the optional Tech Appendix anchor touch is included). Single ratified finding (F1; F2, F3 are no-change; F4 is subsumed into F1). Per-prompt serial cadence does not apply because only one finding requires application.

**Phase C session prerequisite:** author ratification of §7 below.

### §6.2. Bundling opportunities

**No active bundling opportunities at session start.** The Ch 8 Pass 1 Phase C session (commit `5fe6af6`) is closed; no other Ch 6 spot-fix sessions are open at workstream-handoff session-start (verified: no `tools/workstream-handoffs/ch6-*` open).

**Potential future bundling:** if a Ch 6 Pass 1 fact-check / Pass 2 voice-polish / Pass 3 audience-load session opens later, the F1 Option B spot-fix could be bundled into that session's Phase C application. Recommendation: do not block on a future Ch 6 audit; apply F1 as standalone atomic spot-fix in its own Phase C session.

### §6.3. Canonical home for the IPG framing (preserved)

**Ch 2 line 121 remains the canonical home for the McDowell IPG framing**, per the cross-corpus canonical-construction artifact (commit `57575b1`) §6.3. The recommended Ch 6 reconciliation paragraph (Finding 1 Option B) explicitly cross-references Ch 2 line 121's "thirty-three to one hundred and twenty-two times the 1960 sale price" + Ch 8's "worked floor estimate to the upper end of that range." Subsequent chapters or op-eds citing the McDowell IPG continue to anchor on Ch 2's framing; the Ch 6 triangulated 50–555× range is Ch 6 local methodology (the chapter's value-add over the canonical bottom-up range).

---

## §7. Ratification record

**Author ratification:** **RATIFIED 2026-05-21** by author direct ratification ("as recommended"). Phase C application authorized in the same session per CLAUDE.md author-ratified-content-change merge-to-main default.

**Disposition (Finding 1 — Ch 6 line 175 lacks explicit canonical reconciliation):**

- Option A (light cross-reference): [ ]
- Option B (full reconciliation paragraph) — **recommended**: [x] **RATIFIED**
- Option C (lead-with-canonical restructure): [ ]
- Other / custom (specify): [ ]

**Disposition (Finding 2 — Ch 6 line 249 Parfit anchor framing):**

- Option A (no change; conditional on F1 ratified) — **recommended**: [x] **RATIFIED**
- Option B (range-with-floor restatement): [ ]
- Option C (light cross-reference; fallback if F1 not ratified): [ ]
- Other / custom (specify): [ ]

**Disposition (Finding 3 — Ch 6 line 34 implicit Method-1 IPG range):**

- Option A (no change) — **recommended**: [x] **RATIFIED**
- Option B (light disambiguation phrase): [ ]
- Option C (rewrite to anchor on canonical 33–122): [ ]
- Other / custom (specify): [ ]

**Disposition (Finding 4 — missing "per-case 33–122×" reconciliation prose):**

- Option A (subsume into F1's spot-fix) — **recommended**: [x] **RATIFIED**
- Option B (separate Ch 6 reconciliation paragraph elsewhere): [ ]
- Option C (no action; trust cross-chapter inventory annotation): [ ]
- Other / custom (specify): [ ]

**Cross-chapter consequence list ratified as written (§5):** [x] **Yes — Ch 6 line 175 replacement + new paragraph; cross-chapter inventory line 89 update; Tech Appendix §11.11 anchor addition.**

**Phase C bundling decision:**

- Apply F1 Option B as standalone single-atomic Phase C commit — **recommended**: [x] **RATIFIED standalone**
- Bundle with a future Ch 6 Pass 1 / 2 / 3 audit session: [ ]
- Other (specify): [ ]

**Tech Appendix §11.11 anchor touch:**

- Add `id="sec-11-11-ipg-reconciliation"` to the §11.11 heading in same Phase C touch — **recommended (if anchor not already present)**: [x] **RATIFIED + APPLIED** (verified §11.11 carried no anchor at Phase C session start; closest existing parent anchor was `sec-11-empirical-validation` at line 3845; anchor added directly to the §11.11 `<h3>` at HTML line 6199)
- Use parent-section anchor + text-fragment hint in Ch 6 cross-reference link: [ ]
- Verify anchor existence at Phase C session start; defer decision: [ ]
- Other (specify): [ ]

**Phase C application record (2026-05-21, same session as ratification):**

- Ch 6 line 175 replacement + new reconciliation paragraph applied per §5.1 verbatim proposed prose.
- Cross-chapter inventory line 89 updated per §5.4 verbatim proposed prose; Ch 6 line-reference drift warning removed.
- Tech Appendix §11.11 anchor `id="sec-11-11-ipg-reconciliation"` added to the `<h3>` heading at HTML line 6199.
- All four changes applied in a single atomic Phase C commit; per CLAUDE.md author-ratified-content-change default the session fast-forwards to `origin/main` at session close.

**Notes:**

The Ch 6 IPG methodology drift is structurally addressable by a single spot-fix at line 175 because (a) the Tech Appendix §11.11 has already done the reconciliation work and prescribed the pedagogical implication for Ch 6; (b) the chapter's existing architecture handles cross-corpus coherence everywhere except the IPG-headline moment; (c) the missing "per-case 33–122×" prose the inventory historically referenced is naturally restored by surfacing the Tech Appendix §11.11 reconciliation in Ch 6's running prose. Findings 2, 3, 4 collapse into either no-change (F2, F3) or subsumption (F4) under the F1 spot-fix.

Phase C application of HIGH-1's ratified Option B (recommended) is a small atomic spot-fix: two files (Ch 6 + inventory), optionally three (with Tech Appendix anchor touch). No cross-chapter content rewrites required.

---

*End of Ch 6 IPG methodology-reconciliation artifact. Phase C application sequencing in §6 awaits author ratification at §7. The chapter file is unchanged in this session; the artifact proposes spot-fixes for a separate Phase C application session.*
