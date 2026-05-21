# Stage-3 Rigor Pass — Cross-Corpus IPG Canonical-Construction Decision

**Date:** 2026-05-21
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A follow-on (cross-corpus methodology decision)
**Scope:** Cross-corpus methodological decision artifact addressing HIGH-3 of the Ch 8 Stage-3 Pass 1 (fact-check) audit (2026-05-16). Surfaces the question of which IPG construction is canonical for McDowell County coal and proposes a recommendation the author can ratify.
**Mode:** Decision-artifact (not a per-chapter rigor pass). Proposes verbatim replacement prose; does NOT apply spot-fixes to any chapter file.
**Hard constraint observed:** No chapter files modified. Phase C session (post-author-ratification) applies recommended edits.

---

## §1. Canonical sources consulted

**Internal corpus — current state on `origin/main` as of session start:**

1. [CLAUDE.md](CLAUDE.md) — project workflow defaults, especially the 2026-05-16 merge-to-main extension for rigor-pass artifacts.
2. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md) — parent audit; §3 HIGH-3 statement of the question + Options A/B/C as originally sketched; §10 spot-fix scope/sequencing; §11 audience-pass framing.
3. [manuscript/chapters/Chapter__2_TheMiner__Draft.md](manuscript/chapters/Chapter__2_TheMiner__Draft.md) — canonical McDowell County case-walk; canonical IPG framing at line 121.
4. [manuscript/chapters/Chapter__6_ThreeWaysofCounting.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) — three-methods triangulation (line 119 formula; lines 159–171 convergence table; line 175 "approximately fifty times"; line 249 "IPG of 33"). **Note:** the parent audit cites Ch 6 line 486 ("per-case 33–122×") and Ch 6 line 625 ("IPG of 33") as the canonical reconciliation; the current Ch 6 file is 342 lines long, so those line references are stale relative to a prior file version. Current Ch 6 carries the "IPG of 33" anchor only at line 249, and the McDowell-coal IPG appears at line 175 as "approximately fifty times." The 33–122 reconciliation prose the inventory line 89 entry references does not appear in the current file. This stale-reference finding is addressed in §3 below as a downstream consequence the canonical-construction decision must reckon with.
5. [manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md](manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) — current "between four and a hundred and twenty" framing at line 168; carbon-tail-only "between four and a hundred and thirty" framing at line 74; extrapolation echo at line 212.
6. [tools/audits/cross-chapter-consistency-inventory_2026-05-11.md](tools/audits/cross-chapter-consistency-inventory_2026-05-11.md) — McDowell IPG canonical-lock row at line 89 ("33–122×; floor 33; Ch 6 compression 33. Canonical home Ch 2 line 123 . . . Consistent"); SCC anchor row at line 109 ($190); coal carbon-tail per-ton ~$544 at line 110.
7. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md) — apparatus register (Item 3: shorthand identities `CS = RCV − B` and `IPG = RCV / Pmarket` carried in Ch 6 with function arguments stripped; Item 13: IPG acronym discipline — full name with plain-English gloss before deploying acronym).
8. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md) — format model (mirrored: canonical-sources / summary verdict / findings-and-analysis / recommendations / ratification record).
9. [tools/memory/feedback_audit_open_illustrative_default.md](tools/memory/feedback_audit_open_illustrative_default.md) — open/illustrative reading default for chapter-vs-framework audits (Ostrom-path discipline applied to audit-side resolution).
10. [tools/memory/feedback_substance_drives_length.md](tools/memory/feedback_substance_drives_length.md) — substance drives length; not optimizing prose length to hit a trade-press target.
11. [tools/memory/feedback_dual_audience_test.md](tools/memory/feedback_dual_audience_test.md) — Tier-1 quant/economist + Tier-1 trade-press dual-audience test for every register/apparatus rewrite.

**Bundling-opportunity sources (per parent audit cross-references):**

12. Parent audit §10 spot-fix sequencing — HIGH-4 (McDowell drug-rate multiplier) requires a Ch 2 line 41 touch; MED-3 ($0.80/ton denominator) ratified Option C (full Ch 6 + Ch 8 reconciliation). Bundling opportunity flag: both HIGH-3 and HIGH-4 may share a Ch 2 + Ch 6 + inventory touch surface; this artifact flags that opportunity in §6 without prejudging it.

---

## §2. The methodological question

### §2.1. The arithmetic both ranges are defensibly computing

The Intergenerational Pricing Gap is defined in [Chapter__6_ThreeWaysofCounting.md:119](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md:119) as:

> IPG = RCV / P_market

Both the numerator and denominator are functions of multiple parameters. The "range" reported in publisher-facing prose depends on which parameters are varied and which are held fixed:

| Construction | Numerator (RCV) | Denominator (P_market) | Result |
|---|---|---|---|
| **Ch 2 / Ch 6 canonical-inventory framing** | Varies: total-cost depends on which cost-categories the accounting admits + which SCC anchor it uses for the combustion tail | Fixed: 1960 mine-mouth sale price ($4.50/ton) | **33× (low) to 122× (high)** |
| **Ch 8 current framing** | Fixed: $558/ton honest floor (low end of every component as computed in the chapter's 8-component cost-decomposition) | Varies: market price across eras ($4.50/ton 1960 mine-mouth → $40–$140/ton recent) | **~4× (low) to ~124× (high)** |

Both are mathematically valid applications of `IPG = RCV / P_market`. Each is a one-parameter slice of a two-parameter sensitivity surface. The ceiling (~122 vs ~124) coincides because both end up dividing a high-end RCV against the 1960 low-end market price; the floors (33 vs 4) differ because they are answering different questions.

### §2.2. Why this is a methodology-disclosure question, not a fact error

Neither construction is wrong. The drift is a **corpus-consistency** drift, not a fact drift:

- Ch 2 line 121 says "33 and 122 times" with the floor at 33×. Ch 2 also already explicitly anchors that "Chapter 8 walks the floor-estimate version of this calculation through the framework's full cost-decomposition for one specific ton of McDowell County coal in 1960; the per-ton honest price that chapter calculates lands at the upper end of this range." That is, Ch 2 already commits to Ch 8 being a worked-floor-estimate that lands at **the upper end of 33–122×** — i.e., near 122×, the ceiling. A reader who has Ch 2 in hand expects Ch 8 to anchor its per-ton arithmetic near 122×, not at 4×.
- Ch 8 line 168 says "between four and a hundred and twenty." The "and twenty" is approximately the same number as Ch 2's 122 (modulo $558 vs the implicit-from-Ch-2 ~$549 = $4.50 × 122); the "four" is a different number from a different parameter-variation construction.
- The cross-chapter consistency inventory line 89 documents "McDowell IPG range — 33–122× (floor 33; Ch 6 compression 33). Canonical home Ch 2 line 123 . . . Consistent." Ch 8's "4–120" silently diverges; the inventory has not been updated to reflect it.

The question facing the corpus is *not* "which arithmetic is right" — both are. The question is *what construction the publisher-facing prose canonicalizes*. Three further wrinkles tighten the question:

- **Ch 6's current state has drifted from the inventory's reference.** The inventory references Ch 6 line 486 ("per-case 33–122×") and Ch 6 line 625 ("IPG of 33") as reconciliation prose. The current Ch 6 file is 342 lines long; the "per-case 33–122×" reconciliation does not appear in the current text. Ch 6 currently anchors the McDowell IPG at "approximately fifty times" (line 175, against the new triangulated 50–555× M1+M2+M3 aggregate range) and "IPG of 33" (line 249, in the Parfit non-identity passage as the McDowell-coal compression anchor). The corpus already carries two different McDowell IPG headlines (50× and 33×) inside Ch 6 alone, plus the 33–122× canonical range cited in Ch 2 and inventoried as canonical, plus the new 4–120× framing introduced in Ch 8. Whatever this decision does about Ch 8 also has to reckon with the in-Ch 6 drift.
- **Ch 8 line 74 has a separate carbon-tail-only range** ("factor somewhere between four and a hundred and thirty"). That sentence is computing $544 / market-price-range, which is the foreclosure-term-alone IPG — not the full-stack IPG. The parent audit explicitly verifies line 74 is correct (cross-chapter inventory line 110 confirms the $544 SCC × 2.86 = ~$544 coal-carbon-tail anchor). Line 74's "4–130" range is **the same construction as line 168's "4–120"** with a slightly different ceiling (because the numerator is $544 vs $558, and the denominator low end is $4.50 in both cases: $544/$4.50 = 121×; $558/$4.50 = 124×). Whatever this decision does to line 168, it should also do consistently to line 74 + line 212 — the chapter would otherwise carry two methodologically inconsistent "vary the market price" framings inside itself.
- **Apparatus discipline.** The apparatus register Item 13 locks the IPG-acronym discipline as full-name-with-gloss before acronym deployment, not a methodology-disclosure discipline for parameter variation. There is no existing corpus discipline for how to construct the IPG range — only for how to introduce the term. This decision is the first instance of the corpus needing to declare which parameter-variation slice is canonical.

### §2.3. What this decision is choosing between

The decision is choosing the publisher-facing canonical framing for McDowell IPG, the cross-corpus prose touches required to maintain consistency, and the cost-of-change against future-drift risk. The four candidate options are evaluated in §3 below.

---

## §3. Per-option analysis

### Option A — Canonical alignment

**What it does:** Rewrite Ch 8 line 168 to use the canonical Ch 2 / inventory 33–122× range. Mention today-prices in a follow-up sentence as supporting beat. Update Ch 8 lines 74 + 212 for consistency with the headline framing. No structural change to Ch 2, Ch 6, or the inventory.

**Cross-chapter consequence:**
- **Ch 8:** Rewrite line 168 (headline); rewrite line 74 (foreclosure-term-alone framing) to align the multiplier; rewrite line 212 (extrapolation echo) to align the multiplier. Three Ch 8 touches.
- **Ch 2:** No change.
- **Ch 6:** No change to the canonical-construction decision per se. The Ch 6 in-chapter drift (line 175 "fifty times" + line 249 "IPG of 33") remains. (See §6 below for whether to bundle a Ch 6 reconciliation.)
- **Cross-chapter inventory line 89:** Optionally annotate Ch 8 has been brought back into 33–122× alignment after the brief Pass-1-detected drift. Low-priority annotation; the row is still "Consistent" after the spot-fix.

**Voice/register impact on Ch 8:** Reads as the most assertive headline of the chapter's numerical climax (33 to 122 is the load-bearing range Ch 2 already locked; the chapter doesn't ask the reader to re-thread a different parameter variation). Loses the today-prices structural insight if the follow-up sentence is purely supporting; preserves it if the follow-up sentence carries comparable weight to the headline. The headline as currently drafted in Option A's Ch 8 prose preserves the today-prices insight as "the carbon term alone exceeds the market price by a factor of at least four" — which does the structural-finding work without making "four" the headline floor.

**Methodological honesty:** Maximally honest about which construction is canonical. Lower honesty about the parameter-variation choice itself — Ch 8 doesn't tell the reader that *another* construction exists. Defensible because Ch 2 already does the parameter-variation disclosure ("depending on which cost categories you include and which social cost of carbon estimate you use for the combustion tail") and Ch 8's role is to walk the floor-estimate worked example; the methodological disclosure lives in Ch 2.

**Cost-of-change:** Lowest. Three Ch 8 touches (lines 74, 168, 212), no Ch 2 / Ch 6 / inventory touches.

**Risk of future drift:** Lowest. Single canonical construction across the corpus; the inventory line 89 row continues to function as the canonical lock.

---

### Option B — Dual-construction transparency

**What it does:** Keep Ch 8's "4–120" framing for the floor (i.e., the current chapter prose at line 168 stands at the multiplier level) but add explicit prose disclosing the parameter-variation choice and naming the alternative construction. Update lines 74 + 212 for consistency. Update cross-chapter inventory line 89 with a new dual-framing row. Ch 2 and Ch 6 remain unchanged.

**Cross-chapter consequence:**
- **Ch 8:** Rewrite line 168 with the dual-construction disclosure prose (e.g., the concrete Option B prose the author drafted mid-walkthrough); rewrite line 74 to anchor the foreclosure-term-only multiplier as a varying-market-price construction; rewrite line 212 to maintain consistency. Three Ch 8 touches; the line 168 touch is materially larger than Option A's (adds ~3 sentences of methodological disclosure).
- **Ch 2:** No change. Ch 2's "Chapter 8 walks the floor-estimate version . . . lands at the upper end of this range" needs *no* update because the upper end (~122 vs ~124) remains aligned; the worked floor estimate is still the upper-end anchor, the new prose just discloses the dual construction.
- **Ch 6:** No change. Same reasoning as Ch 2.
- **Cross-chapter inventory line 89:** **Add a new row** documenting the dual framing (e.g., "McDowell IPG range — canonical 33–122× per Ch 2 line 121 + cross-chapter inventory lock; Ch 8 line 168 reports a parallel ~4–124× range varying market price across eras while holding the $558 honest floor; both ranges agree on the structural finding (carbon term dominates) and on the ~120 ceiling against 1960 mine-mouth; the floors differ because the constructions vary different parameters"). Or expand the existing row 89 to document both constructions inline.

**Voice/register impact on Ch 8:** Most academically transparent; preserves the today-prices insight structurally (it is the headline framing); reads slower in the chapter's numerical climax (adds methodological-disclosure prose at the moment the reader most expects a single headline number). For a trade-press reader, the methodological-disclosure prose risks reading as hedging; for a Tier-1 quant reader, it reads as appropriately disciplined parameter-variation disclosure.

**Methodological honesty:** Highest. Discloses the parameter-variation choice explicitly. Names both constructions, names what each varies, names the structural-finding agreement. The kind of disclosure a publisher fact-checker familiar with sensitivity-analysis conventions would specifically value.

**Cost-of-change:** Medium. Three Ch 8 touches (one large); one cross-chapter inventory touch. No Ch 2 / Ch 6 touches.

**Risk of future drift:** Medium. Two ranges canonical for the same case opens a future-drift surface: a later chapter or op-ed citing the McDowell IPG has to decide which range to cite. The inventory row would have to carry the disambiguation cleanly enough that a fact-checker reading the inventory understands when to cite which.

---

### Option C — Full corpus update

**What it does:** Update Ch 2, Ch 6, Ch 8, and the cross-chapter inventory to document the dual-construction methodology corpus-wide. Lock both constructions as canonical; specify the rules for when each is cited. Adds methodology-disclosure prose to every chapter that touches the McDowell IPG.

**Cross-chapter consequence:**
- **Ch 8:** Same as Option B's Ch 8 touches (three Ch 8 lines), possibly with shorter disclosure prose if the methodology-disclosure work is also being done in Ch 2 and Ch 6.
- **Ch 2:** Rewrite line 121 to introduce the dual-construction framing at the canonical-home site. Currently Ch 2 says: "The total arrives at something between 33 and 122 times the price the coal actually sold for, depending on which cost categories you include and which social cost of carbon estimate you use for the combustion tail . . . the floor is 33 times." The new prose would need to anchor that "33 to 122" is the SCC-and-cost-category-varied construction holding 1960 price fixed; that an alternative construction (varying market price across eras at the honest floor) is also methodologically valid and produces a range with a different floor; that both agree on the carbon-term-dominance finding. **Material rewrite of the canonical IPG prose** at the canonical home — high-stakes prose change.
- **Ch 6:** Rewrite to lock the dual construction as part of the formal apparatus. The Ch 6 in-chapter drift (line 175 "fifty times" + line 249 "IPG of 33" + absent "33–122×" reconciliation) becomes a coupled cleanup; the chapter needs to reconcile the new triangulated 50–555× range against the canonical 33–122× per-case range, against the Parfit-passage "IPG of 33" anchor, against the new dual-construction methodology. **Substantial Ch 6 rewrite.**
- **Cross-chapter inventory line 89:** Rewrite the row to document the dual-construction lock + cite-rule (when to cite 33–122× vs when to cite 4–124×). Add cross-references to the new Ch 2 + Ch 6 + Ch 8 disclosure prose.

**Voice/register impact:** Most structurally correct; most prose-cost. Every chapter that touches the IPG now carries methodological-disclosure prose. For a Tier-1 quant reader, this is the gold-standard treatment; for a Tier-1 trade-press reader, it risks turning the McDowell case-walk into a methodology seminar across three chapters. The author's substance-drives-length discipline cuts against this: the methodology disclosure is necessary if the dual construction is real, but does the dual construction *need* to be canonical, or is it sufficient for the corpus to canonicalize one construction and treat the other as the worked-example angle?

**Methodological honesty:** Highest in principle (full disclosure across the corpus). But: opens a question of whether *this* is the right corpus methodology decision to make at this audit pass. The Ch 6 file has already substantially drifted from the inventory's reference (the 33–122× reconciliation prose no longer exists in the current Ch 6); locking dual-construction canonical now also requires re-establishing what Ch 6 currently says about the per-case 33–122× range, which is a separate (and bigger) Ch 6 reconciliation. Doing both at once risks scope creep.

**Cost-of-change:** Highest. Touches Ch 2 (canonical-home IPG prose), Ch 6 (methodology + reconciliation), Ch 8 (three lines), inventory row. Possibly couples to the broader Ch 6 reconciliation the in-chapter "fifty times" / "IPG of 33" / "33–122×" drift implies.

**Risk of future drift:** Lowest in principle (canonical lock is fully specified); highest in practice (two canonical constructions with cite-rules is itself a discipline future audits have to enforce).

---

### Option D — Canonical headline + today-prices follow-up

**What it does:** Rewrite Ch 8 line 168 to lead with the canonical "between 33 and 122 times the 1960 sale price" framing (Ch 2 alignment), then add a follow-up sentence preserving the today-prices structural insight: today's higher market prices still leave the carbon term exceeding the market price by at least 4×; the structural finding holds across every era. Update lines 74 + 212 for consistency with the headline. Optionally annotate the inventory row that Ch 8 carries a today-prices framing in the body for ceiling-pressure-test reasons.

**Cross-chapter consequence:**
- **Ch 8:** Rewrite line 168 (headline + follow-up sentence); rewrite line 74 to align the foreclosure-term-only multiplier with the canonical-headline construction; rewrite line 212 to align with the headline. Three Ch 8 touches; line 168 touch is materially smaller than Option B's (no methodological-disclosure prose) but larger than Option A's (a follow-up sentence preserving today-prices).
- **Ch 2:** No change. Ch 2 already anchors "Chapter 8 walks the floor-estimate version . . . lands at the upper end of this range"; Option D's Ch 8 prose makes good on that anchor explicitly by leading with the canonical-range headline.
- **Ch 6:** No change to the canonical-construction decision per se. The in-Ch 6 "fifty times" / "IPG of 33" drift remains as a separate finding to address in a subsequent Ch 6 audit (see §6 bundling note).
- **Cross-chapter inventory line 89:** Optionally add a small annotation that Ch 8 includes a today-prices structural-finding beat in the body (i.e., "carbon term alone exceeds market price by at least 4× even at today's prices") for completeness. Not load-bearing; the row remains structurally Consistent.

**Voice/register impact on Ch 8:** Preserves the chapter's numerical-climax architecture (a single canonical headline range, the way Ch 2 and the inventory expect) while preserving the today-prices structural-finding insight as a supporting beat. The headline reads decisively for both audiences; the follow-up does the structural-finding work without burdening the headline with the dual-construction disclosure. The "structural finding holds across every era the industry has operated" is the load-bearing sentence — it carries the today-prices insight forward without requiring the reader to track two parameter-variation constructions.

**Methodological honesty:** Honest about which construction is canonical (the 33–122× range). Less explicitly honest about the parameter-variation choice than Option B — the follow-up sentence implies the today-prices construction is *the same* IPG re-anchored, not a different parameter-variation slice. Defensible because the structural-finding agreement *is* the methodologically important point; the choice of which parameter to vary is bookkeeping. A Tier-1 quant reader who wants to know what the floor multiplier becomes at today's prices gets that answer in the follow-up; the methodological-disclosure work happens at Ch 2 line 121 (which is canonical-home and where it belongs).

**Cost-of-change:** Low-to-medium. Three Ch 8 touches; no Ch 2 / Ch 6 touches; optional small inventory annotation.

**Risk of future drift:** Low. Single canonical construction (33–122×); the today-prices follow-up is a structural-finding beat, not a competing canonical range. Future chapters / op-eds citing the McDowell IPG cite 33–122× per the inventory canonical lock; the today-prices beat is Ch 8 local color.

---

## §4. Recommendation

**RATIFY Option D — Canonical headline + today-prices follow-up — for the McDowell IPG cross-corpus canonical-construction question, with the cross-chapter consequences enumerated in §5.**

### §4.1. Why Option D over Option A

Option D and Option A differ only in whether the today-prices insight is preserved as a follow-up sentence (D) or compressed into a methodological note (A). The today-prices structural finding — *the carbon term alone exceeds the market price by at least 4× even at today's prices* — is genuinely load-bearing for the chapter's climactic claim about civilizational-scale mispricing. It is also the part of Ch 8's new framing that a careful trade-press reader will remember (a coal market that has run between $4.50 and $140 across the industry's life, and the honest cost has always exceeded the high end). Option A's compression risks losing that. Option D preserves it as a structural beat without making it the canonical headline.

The chapter's voice is also better served by Option D. Ch 8 is the manuscript's numerical climax; the headline range needs to land assertively. "Between 33 and 122 times the 1960 sale price" is a sentence that lands; "between four and a hundred and twenty" is a sentence that asks the reader to do a parameter-variation calculation in their head. Option D leads with the assertion and follows with the structural-finding beat.

### §4.2. Why Option D over Option B

Option B's dual-construction transparency is the most academically honest option, but the dual-disclosure prose lands at exactly the moment in Ch 8 — the IPG headline — where the chapter most needs a single, assertive number. The methodology-disclosure work belongs at the canonical-home site (Ch 2 line 121), where the parameter-variation language already exists ("depending on which cost categories you include and which social cost of carbon estimate you use for the combustion tail"). Ch 8's job is to walk the worked floor-estimate — which Ch 2 already commits to as the upper-end anchor. Option D makes good on Ch 2's anchor explicitly without re-litigating the parameter-variation question at Ch 8's climax.

The dual-canonical inventory row Option B would create also opens a discipline-enforcement surface that the corpus currently does not have to maintain. A single canonical lock (Option D) is cleaner; the cite-rule is simpler ("cite 33–122× per the canonical lock; today-prices framing is Ch 8 local color").

### §4.3. Why Option D over Option C

Option C is structurally the most correct response to a real two-construction methodology. The dual construction is real; both arithmetics are valid; the corpus could legitimately canonicalize both with a cite-rule. But three things cut against Option C at this audit pass:

- **Scope creep into a Ch 6 reconciliation that is itself unresolved.** Ch 6 has already substantially drifted from the inventory's reference: the "per-case 33–122×" reconciliation prose no longer exists in the current Ch 6 file; Ch 6 carries "approximately fifty times" (line 175) and "IPG of 33" (line 249) without internal reconciliation. Option C's Ch 6 touch can't just add dual-construction disclosure — it has to *first* reconcile the in-Ch 6 multi-headline drift, then layer the dual-construction discipline on top of that reconciliation. That is a substantial Ch 6 audit in itself, and properly belongs to a separate Ch 6 fact-check / methodology-reconciliation session.
- **The substance-drives-length discipline cuts against gratuitous methodology disclosure.** The dual-construction methodology is interesting but is not the chapter's substantive point. The substantive point (carbon term dominates every era's market price) is already captured by Option D's follow-up sentence. Option C's full-corpus methodology disclosure adds prose-cost without adding substantive insight — it would be the kind of treatment a Tier-1 quant reader values and a Tier-1 trade-press reader skims past.
- **Ch 2 line 121 already does the methodology disclosure work.** Ch 2's "depending on which cost categories you include and which social cost of carbon estimate you use" is exactly the parameter-variation disclosure Option C would add across the corpus. It is already there at canonical-home; Option C's marginal addition is naming the alternative parameter-variation choice (vary market price holding floor) explicitly. That naming is valuable but is not load-bearing for the framework's argument.

### §4.4. The dual-audience pass-test

- **Tier-1 quant/economist reader:** Option D passes the test if and only if the reader can recover the dual-construction sensitivity from Ch 2 line 121 + Ch 8's today-prices follow-up. A reader who wants to see "what happens to the IPG if you hold the floor and vary the market price" gets the answer at Ch 8's follow-up ("the carbon term alone exceeds the market price by at least 4× even at today's prices"). A reader who wants the full sensitivity surface gets it via the parameter-variation language at Ch 2 line 121 + Ch 8's worked floor estimate at $558. The reader who wants formal sensitivity analysis goes to the Technical Appendix. ✓ Passes.
- **Tier-1 trade-press reader:** Option D passes the test if the headline range (33–122×) lands as decisive and the today-prices follow-up lands as a structural-finding beat that reinforces rather than complicates the headline. The author's draft prose for Option D ("Even at today's higher market prices ($40 to $140 per ton depending on grade), the carbon term alone exceeds the market price by a factor of at least four. The structural finding holds across every era the industry has operated.") meets this test — the follow-up reads as the next sentence after the climax, not as a methodological hedge. ✓ Passes.
- **Tier-2 careful-reader-of-both-chapters:** This is the reader most at risk under the current Ch 8 line 168 prose (the reader carrying Ch 2's "floor 33×" forward to Ch 8 and finding "floor 4×"). Option D resolves the risk by aligning Ch 8's headline with Ch 2's headline; the today-prices follow-up does not contradict Ch 2 because Ch 2 holds 1960 price fixed and the follow-up explicitly says "at today's higher market prices." ✓ Passes.

### §4.5. Verdict

**RATIFY Option D with the cross-chapter consequences in §5.** Recommendation is defensible against all three audience tiers; preserves Ch 8's today-prices structural insight as a non-headline beat; aligns Ch 8 with Ch 2's canonical-home framing; aligns Ch 8 with the cross-chapter inventory canonical lock; requires no Ch 2 or Ch 6 prose changes; requires only an optional small inventory annotation; lowest-friction methodologically-honest option that preserves the new chapter's structural insight.

---

## §5. Cross-chapter consequence list (recommended option only)

### §5.1. Ch 8 prose changes

**Ch 8 line 168 — the canonical IPG headline.**

Current prose:

> The Intergenerational Pricing Gap — the ratio of honest price to market price — for McDowell County coal, at the low end of every component, is somewhere between four and a hundred and twenty. The range is wide because the market price varies by era. The floor is high because the carbon term dominates anything the market has ever paid for a ton of coal.

Proposed verbatim replacement (mirrors the author's mid-walkthrough Option D draft, with light prose tightening for chapter voice):

> The Intergenerational Pricing Gap — the ratio of honest price to market price — for McDowell County coal sits somewhere between thirty-three and one hundred and twenty-two times the 1960 sale price, depending on which cost categories the accounting admits and which social cost of carbon anchor it uses. Even at today's higher market prices ($40 to $140 per ton depending on grade), the carbon term alone exceeds the market price by a factor of at least four. The structural finding holds across every era the industry has operated: the honest cost of a ton of McDowell County coal has always exceeded what the market paid for it, often by more than two orders of magnitude.

**Ch 8 line 74 — the foreclosure-term-only IPG framing.**

Current prose:

> Five hundred and forty-four dollars. Against a market price that has oscillated between four dollars and a hundred and forty dollars over the life of the industry. The foreclosure term alone exceeds the market price of every ton of coal ever mined in the United States by a factor somewhere between four and a hundred and thirty, depending on the era.

This is computing a different (legitimate) quantity from line 168's full-stack IPG — the carbon-tail-alone-to-market-price ratio, which Ch 2 / inventory have no canonical lock on (and Ch 8 is canonical-home for the carbon-tail-alone computation, per the chapter's 8-component cost decomposition). The "4 to 130" range at line 74 is the *carbon-tail-alone* IPG, which is structurally a different ratio from the full-stack IPG at line 168.

**Recommended treatment:** Light alignment to make the parameter-variation choice explicit at the carbon-tail-alone framing too. Proposed verbatim replacement:

> Five hundred and forty-four dollars. Against a market price that has oscillated between four dollars and a hundred and forty dollars over the life of the industry. The carbon term alone — before any of the other seven components are added — exceeds every era's market price for a ton of coal, by a factor running from roughly four against today's market peak to more than a hundred against the 1960 mine-mouth.

This preserves line 74's standalone-foreclosure-term-dominance finding (the structural point of the sentence) while disclosing the parameter-variation explicitly ("from today's peak to the 1960 mine-mouth") rather than implicitly ("depending on the era"). Aligns the prose-form with Ch 8's line 168 headline.

**Ch 8 line 212 — the extrapolation echo.**

Current prose:

> If coal is mispriced locally by a factor somewhere between four and a hundred and twenty, and if the same pattern appears across every extraction case the book has examined, then the aggregate global severed cost across all resource extraction sits in a range the framework can bound but cannot fully specify from here.

Proposed verbatim replacement:

> If coal is mispriced locally by between thirty-three and one hundred and twenty-two times the 1960 sale price — and if the same pattern appears across every extraction case the book has examined — then the aggregate global severed cost across all resource extraction sits in a range the framework can bound but cannot fully specify from here.

Aligns the extrapolation's premise multiplier with the chapter's headline (line 168) and the cross-chapter canonical lock.

### §5.2. Ch 2 prose changes

**No change required.** Ch 2 line 121 already canonically anchors "between 33 and 122 times" + "the floor is 33 times" + the explicit anchor that "Chapter 8 walks the floor-estimate version of this calculation through the framework's full cost-decomposition for one specific ton of McDowell County coal in 1960; the per-ton honest price that chapter calculates lands at the upper end of this range." Option D makes good on that anchor; no Ch 2 rewrite is needed.

### §5.3. Ch 6 prose changes

**No change required for the IPG canonical-construction decision.** The in-Ch 6 multi-headline drift ("approximately fifty times" at line 175; "IPG of 33" at line 249; the missing "per-case 33–122×" reconciliation prose the inventory line 89 row references but is not in current Ch 6) is a **separate finding** that belongs to a dedicated Ch 6 fact-check / methodology-reconciliation session. Flagging it here is sufficient for cross-corpus PM awareness; it is not part of the canonical-construction-decision Phase C application.

### §5.4. Cross-chapter inventory line 89 update

Current row text:

> | **McDowell IPG range** | 33–122× (floor 33; Ch 6 compression 33) | Ch 2 line 123 | Ch 6 line 486 reconciles "5–133× damage-function method, 19–47× RCV model, per-case 33–122×"; Ch 6 line 625 ("IPG of 33"). **Consistent.** |

Proposed verbatim replacement (preserves the canonical lock; adds a Ch 8 today-prices-framing annotation; flags the Ch 6 line-reference-stale issue for separate action):

> | **McDowell IPG range** | 33–122× (floor 33; Ch 6 compression 33) | Ch 2 line 121 | Ch 8 line 168 carries the canonical 33–122× framing as headline + today-prices follow-up ("even at today's $40–$140 prices, the carbon term alone exceeds market by ≥4×"; structural-finding beat, not competing canonical). Ch 6 carries "IPG of 33" at line 249 (Parfit non-identity passage) + "approximately fifty times" at line 175 (new triangulation register). **⚠ Ch 6 line-reference drift flagged:** prior row text referenced Ch 6 line 486 ("per-case 33–122×") + Ch 6 line 625, which do not appear in current Ch 6 file (342 lines total); separate Ch 6 methodology-reconciliation finding required. Canonical IPG headline range (33–122×) **Consistent** across Ch 2 + Ch 8. |

---

## §6. Phase C application sequencing

### §6.1. Recommended sequencing for the canonical-construction decision

Three Ch 8 touches + one inventory annotation. Apply in a single atomic Phase C commit:

1. Ch 8 line 168 (canonical IPG headline + today-prices follow-up).
2. Ch 8 line 74 (carbon-tail-only foreclosure framing alignment).
3. Ch 8 line 212 (extrapolation echo alignment).
4. Cross-chapter inventory line 89 update (canonical lock annotated; Ch 6 line-reference drift flagged for separate action).

No Ch 2 or Ch 6 prose changes required for this decision. Single-file-plus-inventory atomic commit; lowest Phase C application risk.

### §6.2. Bundling opportunities

The parent audit cross-references two other findings whose Phase C application may bundle with this one:

- **HIGH-4 (McDowell drug-rate multiplier).** Parent audit §3 HIGH-4 was ratified Option A (denominator-explicit 2015 alignment) with a Ch 2 line 41 touch required to align "roughly five times the national average" to the 2015 national-rate denominator + add the multiplier lock to the cross-chapter inventory. **HIGH-3's canonical-construction recommendation (Option D) requires no Ch 2 touch.** No bundling opportunity at the Ch 2 file level; HIGH-4 is a self-contained Ch 2 line 41 + Ch 8 line 58 + inventory touch. The two findings can apply in the same Phase C session but do not share a touch surface.
- **MED-3 ($0.80/ton denominator inconsistency).** Parent audit §3 MED-3 was ratified Option C (full Ch 6 + Ch 8 reconciliation), meaning Ch 6 is being touched in Phase C anyway. **Potentially relevant bundling opportunity:** if Phase C is already opening Ch 6 for the $0.80/ton denominator reconciliation, the in-Ch 6 IPG drift ("fifty times" at line 175 + "IPG of 33" at line 249 + missing "per-case 33–122×" reconciliation prose) flagged in §5.3 above could potentially be bundled into the same Ch 6 touch surface. **Author judgment whether to bundle:** the IPG drift is a methodology-reconciliation finding separate from the $0.80/ton arithmetic-reconciliation finding; bundling them risks scope creep into a Ch 6 audit that has not been formally run; but the file is being opened either way and the marginal cost of a small annotation in Ch 6 line 175 or 249 may be low. **Recommendation:** flag for author judgment at Phase C session start; do not bundle by default.

### §6.3. Canonical home for the IPG framing

For posterity / future-audit reference: **Ch 2 line 121 remains the canonical home for the McDowell IPG framing** (the parameter-variation language already lives there; the inventory line 89 row points there; the recommended Ch 8 rewrite explicitly defers to it). Subsequent chapters or op-eds citing the McDowell IPG should anchor to Ch 2's "33 and 122 times the 1960 sale price, depending on which cost categories you include and which social cost of carbon estimate you use." Today-prices framing is Ch 8 local color for the carbon-term-dominance structural finding; not canonical at the corpus level.

---

## §7. Ratification record

*Placeholder — author fills in post-decision.*

**Author ratification:** [PENDING]

**Disposition:**
- Option A (canonical alignment): [ ]
- Option B (dual-construction transparency): [ ]
- Option C (full corpus update): [ ]
- Option D (canonical headline + today-prices follow-up) — **recommended**: [ ]
- Other / custom (specify): [ ]

**Cross-chapter consequence list ratified as written:** [ ] Yes [ ] No (note variations below)

**Phase C bundling decision:**
- Apply HIGH-3 as standalone single-atomic Phase C commit: [ ]
- Bundle HIGH-3 with HIGH-4 (no shared touch surface; same Phase C session): [ ]
- Bundle HIGH-3 with MED-3 (Ch 6 file already opening for $0.80/ton reconciliation; opportunity to annotate Ch 6 IPG drift): [ ]
- Other (specify): [ ]

**Ch 6 in-chapter IPG drift (line 175 "fifty times" + line 249 "IPG of 33" + missing "per-case 33–122×" reconciliation):**
- Defer to dedicated Ch 6 methodology-reconciliation session: [ ]
- Bundle with MED-3 Phase C if Ch 6 file is opening: [ ]
- Other (specify): [ ]

**Notes:**

---

*End of cross-corpus IPG canonical-construction decision artifact. Phase C application sequencing in §6 awaits author ratification at §7.*
