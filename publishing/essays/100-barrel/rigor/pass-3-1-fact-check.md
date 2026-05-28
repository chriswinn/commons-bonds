# $100 Barrel Essay — Pass 3.1 Fact-Check Rigor Pass v1.0.0 — 2026-05-21

**Status:** PROPOSED. Pass 3.1 fact-check artifact for Draft A (canonical-path Stage 2 audience-blind flow draft, ratified routing to Stage 3 by author 2026-05-21 per comparative draft audit verdict). Author ratification + Phase C application is a separate session per v3.0 per-prompt serial cadence (preserved in v3.1).

**Audit target:** [`publishing/essays/100-barrel/essay.md`](../../publishing/essays/100-barrel/essay.md) (Draft A; 4,078w; on `main` commit `74953b9` 2026-05-21).

**Source of truth:** Stage 1 brief [`publishing/essays/100-barrel/rigor/stage-1-brief.md`](stage-1-brief.md) §7 canonical-facts inventory + [`research/literature/bibliography.md`](../../research/literature/bibliography.md). Per v2.0 Path B preemptive policy, withdrawn-Noema §III is NOT source-of-truth — the Stage 1 brief §7 is the single canonical baseline. Per v3.1 / Amendment B 2026-05-18, Stage 3 is a five-pass discipline (3.1 fact-check → 3.2 voice-polish → 3.3 audience-load acceptance → 3.4 audience-load robustness → 3.5 developmental-edit); this artifact is Pass 3.1.

**Prior pass cross-reference:** Comparative draft audit [`stage-3-comparative-draft-audit.md`](stage-3-comparative-draft-audit.md) §8.4 enumerated four pre-flagged verification items: Norway fund size, Norway per-citizen figure, Niger Delta "more than thirty billion barrels," pump-price hook §I. This pass verifies each + surfaces net-new findings against the full essay text.

**Methodology:** Section-by-section audit against Stage 1 brief §7 canonical-truth inventory. Per-finding format: F-FC-Barrel-K + severity (CRITICAL / HIGH / MEDIUM / LOW) + location + verbatim current text + source-of-truth + Stage 1 brief baseline + proposed correction + cross-pass impact + canonical-truth-gap (CTG-K) flag where applicable. External-citation verification performed for HIGH-severity calls.

**Hard constraint:** PROPOSED only. No spot-fixes applied to the essay file. Phase C application is a separate session post-author-ratification.

---

## 1. Findings — net-new (no prior-pass spot-fixes to re-verify)

Severity tiers per template:
- **CRITICAL** — factually wrong; fact-checker-flagged
- **HIGH** — misleading / imprecise; knowledgeable-reader-challengeable
- **MEDIUM** — technically defensible but loose; precision-sharpenable
- **LOW** — accurate but framing-sharpenable

### F-FC-Barrel-1 — Norway fiscal rule percentage attributed to 2001 — HIGH

**Location:** §VI, paragraph 2 (line 154 of the audit-target file).

**Verbatim current text:**
> Eleven years after the founding, in 2001, the Storting adopted a fiscal rule that limited annual government withdrawals to roughly three percent of the fund's expected real return.

**Source of truth (external citation):** Norway's fiscal rule (*handlingsregelen*) was adopted by the Stoltenberg I government in March 2001 with an **expected real return target of 4 percent**. The rate was **reduced to 3 percent in February/spring 2017** by the Solberg government, following analyses from the Thøgersen commission, the Mork commission, and Norges Bank that lowered expected long-run real return assumptions in a lower-global-interest-rate environment. (Sources: regjeringen.no — The Norwegian Fiscal Policy Framework; Norges Bank Investment Management — Annual Report sequence 2001–2024; Norwegian School of Economics — "When Norway rewrote the fiscal rule"; Wikipedia — *Handlingsregelen*.)

**Stage 1 brief baseline:** §7.2 says "Fiscal rule: Adopted 2001 under Stoltenberg I (Labour). Limits annual withdrawals to expected real return on capital (~3%). Capital itself inviolate." The Stage 1 brief itself **conflates the 2001 adoption with the 2017 revision** — Amendment A canonical-truth-gap (the same gap surfaced by the Noema Pass 3.1 fact-check, F-FC-Noema-1).

**Proposed correction (verbatim replacement prose):**
> Eleven years after the founding, in 2001, the Storting adopted a fiscal rule that limited annual government withdrawals to the fund's expected real return — initially set at four percent, lowered to three percent in 2017 as long-run return expectations declined.

**Cross-pass impact:** No impact on Pass 3.2 voice-polish (correction adds ~15 words; preserves cadence; no LLM-tic introduction). Negligible Pass 3.3 audience-load impact except that **Tier 1 #1 PW editorial brain**, **Tier 2 #6 Stone Center reviewer**, and **Tier 2 #10 Stern-tradition climate economist** characters all benefit from the 4%-to-3% rate-change context (signals familiarity with the policy mechanism + the recent history of fiscal-rule revision). The Tier 1 dispositive Condition 1 character (#3 center-right policy reader) is unaffected on substance but reads the increased precision as additional evidence of careful engagement — small positive.

**Canonical-truth-gap flag:** CTG-1 — Stage 1 brief §7.2 needs Amendment A repair to reflect the 4%→3% rate-change history. Recommend brief amendment as part of Phase C application, parallel to F-FC-Noema-1's CTG flag (same upstream gap).

**Empirical-anchor connection:** This is the same factual drift that the v2.0 Amendment B op-ed pipeline session (commit `5167edd`, 2026-05-10) caught at its Stage 3.1 (GPFG founding-date conflation + Bondevik-coalition timing). The fact-check pass's empirical justification — separating fact-check from audience-load because audience-load alone would miss this — is reaffirmed here.

---

### F-FC-Barrel-2 — Norway fund size figure — MEDIUM (submission-week re-verification required)

**Location:** §VI, paragraph 2 (line 154 of the audit-target file).

**Verbatim current text:**
> The fund holds, as of the most recent reporting, in excess of one and nine-tenths trillion U.S. dollars.

**Source of truth (external citation):** Norges Bank Investment Management (NBIM) publishes the fund's market value daily at [`nbim.no`](https://www.nbim.no/). As of recent reporting in late 2025 / early 2026, the fund's market value has fluctuated in the $1.7T–$2.0T range depending on global-market conditions + USD/NOK exchange rate. The Stage 1 brief §7.2 notes "the source draft cited $2.2T as of 2025 — Ch 4 cites >$1.9T." Draft A's ">$1.9T" framing is consistent with Ch 4 + conservative against the higher source-draft figure.

**Stage 1 brief baseline:** §7.2 explicitly flags this for Stage 2 / Stage 3 verification: "verify current figure at Stage 2 against ~late-2025 / early-2026 fund-published number; the source draft cited $2.2T as of 2025 — Ch 4 cites >$1.9T; Stage 2 should use the most recent Ch 4 figure or look up the official Norges Bank Investment Management figure at draft date." Draft A used the Ch 4 conservative figure.

**Proposed correction:** No prose change at this pass. **Submission-week verification required** (~2026-06-01 to ~2026-06-08): pull current NBIM figure; if the current figure has moved materially (e.g., now >$2.0T or <$1.85T), update Draft A to reflect the live number. The "as of the most recent reporting" hedge already protects against minor drift. Recommend the submission-week verifier note the exact NBIM-reported figure in the submission cover-note for editorial fact-check.

**Cross-pass impact:** None on Pass 3.2 or downstream passes. Submission-window-only verification item.

**Canonical-truth-gap flag:** No CTG; the brief explicitly flagged this as a verification-at-draft-time item, so the brief is not the gap-source.

---

### F-FC-Barrel-3 — Niger Delta production figure + decade-count timing — MEDIUM

**Location:** §VI, paragraph 3 (line 158 of the audit-target file).

**Verbatim current text:**
> Over five decades the Delta has produced, by various estimates, more than thirty billion barrels of crude.

**Source of truth (external citation):** Commercial oil production in Nigeria began in 1958 from the Oloibiri field in the Niger Delta (Royal Dutch Shell). As of 2024–2025, Nigeria's cumulative crude oil production since 1958 is reported in the range of 35–40 billion barrels (sources: OPEC Annual Statistical Bulletin sequence; U.S. Energy Information Administration — Nigeria Country Analysis Brief; Nigerian National Petroleum Corporation — Statistical Bulletin sequence). The "more than thirty billion barrels" figure is conservative and defensible — Draft A intentionally uses "more than" + "by various estimates" to hedge against the moving cumulative-total target.

**Timing issue:** "Over five decades" understates the actual span. 1958 → 2026 = 68 years = roughly **seven decades**. The phrase "over five decades" is technically true (it has been over five decades) but reads as imprecise when the actual span is closer to seven. A knowledgeable reader (Tier 2 #8 Mazzucato-cluster reader; Tier 3 #14 general policy economist) will flag this as loose.

**Stage 1 brief baseline:** §7.12 says "Niger Delta extraction since 1950s" without specifying a cumulative production figure or decade count. The "more than thirty billion barrels" figure was introduced by the Stage 2 drafter beyond the brief's inventory. Defensible per brief §11 ("Stage 2 reads this Stage 1 brief + the canonical facts inventory in §7 + the bibliography entries"), but Pass 3.1 verifies the figure against external sources.

**Proposed correction (verbatim replacement prose):**
> Over more than half a century the Delta has produced, by various estimates, more than thirty billion barrels of crude.

(Or, if author prefers higher precision:)

> Over nearly seven decades the Delta has produced, by various estimates, more than thirty-five billion barrels of crude.

The first option preserves the original "more than thirty billion" figure with a tighter decade-count framing; the second option updates both the time-span and the production figure to match more recent cumulative reporting. Author disposition: pick whichever balances precision against rhetorical economy.

**Cross-pass impact:** Pass 3.3 audience-load — Tier 2 #8 Mazzucato-cluster + Tier 2 #9 Ostrom-successor + Tier 3 #14 general policy economist all read tightened timing as additional precision. No Pass 3.2 voice-polish impact. Pass 3.4 adversarial — orthodox-econ adversarial reader (A5) may seize a loose decade-count as evidence of insufficient engagement with the primary literature; tightening the prose closes that thread proactively.

**Canonical-truth-gap flag:** No CTG; the brief did not commit to a specific figure here.

---

### F-FC-Barrel-4 — Pump-price hook §I (salience claim) — MEDIUM (submission-window re-verification required)

**Location:** §I, paragraph 1 (line 54 of the audit-target file).

**Verbatim current text:**
> The price of gasoline has crept up again. Anyone who has filled a tank this spring has watched the number on the display run past where it sat last year and pulled the nozzle out before the total settled into a figure worth a second look.

**Source of truth (external citation):** U.S. retail gasoline prices are published weekly by the U.S. Energy Information Administration (EIA). As of mid-May 2026, the U.S. average regular-gasoline retail price has been in the $3.60–$4.00 per gallon range — historically high but not unprecedented. The directional claim "crept up again" + "past where it sat last year" requires verification against EIA Weekly Retail Gasoline and Diesel Prices report at submission week.

**Stage 1 brief baseline:** §7.13 explicitly flags this for Stage 2 verification: "Stage 2 should verify current pump-price reference at draft time (2026-05-19 onward) against a specific source. Hook should be one-to-two sentences max, not a news-article register. Avoid implying a specific cause of the spike (geopolitical, refining, demand-side); the essay does not engage the proximate-cause analysis — the hook is the salience of pricing, not the explanation of the spike."

Draft A's hook is one-to-two sentences (compliant) and does not imply a specific proximate cause (compliant). The directional claim "crept up again" + "past where it sat last year" is the verification item.

**Proposed correction:** No prose change at this pass. **Submission-week verification required** (~2026-06-01 to ~2026-06-08): pull current EIA Weekly Retail Gasoline and Diesel Prices report; verify the directional claim against the report's national average + year-over-year trend. If the directional claim is wrong (prices flat or declining), Draft A's hook needs a salience-only rewrite that does not commit to a direction. Recommended safe phrasing for that contingency:

> The price of gasoline is, again, the number people watch when they fill the tank. Whether it has crept up or settled back since last year, it is high enough that the political class is arguing about it on cable news.

(This phrasing preserves the salience hook without committing to a direction; usable as a contingency rewrite if the directional claim fails verification.)

**Cross-pass impact:** None on Pass 3.2 or downstream passes. Submission-window-only verification item.

**Canonical-truth-gap flag:** No CTG; the brief explicitly flagged this as a verification-at-draft-time item.

---

### F-FC-Barrel-5 — Per-citizen figure derivation — LOW

**Location:** §VI, paragraph 2 (line 154 of the audit-target file).

**Verbatim current text:**
> That is roughly three hundred and forty thousand dollars for every Norwegian citizen alive.

**Source of truth (derivation check):** $1.9T / 5.55M (Norway's mid-2025 population per Statistics Norway) = ~$342K per citizen. Draft A's "roughly three hundred and forty thousand dollars" is mathematically consistent with the $1.9T fund-size claim + Norway's current population.

**Stage 1 brief baseline:** §7.2 cites "~$340,000 per Norwegian (Ch 4 canonical figure)." Draft A matches the brief.

**Proposed correction:** No prose change at this pass. The figure ratchets with the fund size (F-FC-Barrel-2). If the submission-week NBIM figure (F-FC-Barrel-2) moves materially, recalculate the per-citizen figure accordingly. Otherwise the "roughly three hundred and forty thousand dollars" hedge is durable across small drift.

**Cross-pass impact:** None.

**Canonical-truth-gap flag:** No CTG.

---

## 2. Verified clean (no findings; logged for completeness)

All canonical-fact items in the Stage 1 brief §7 inventory verified against Draft A's prose. Per-section walk:

### §I — The Barrel
- ✅ Hotelling rent gloss ("the scarcity premium on a non-renewable resource that the owner gives up by extracting today rather than tomorrow"). Accurate plain-language summary of Hotelling 1931 (*Journal of Political Economy* 39(2): 137–175), confirmed in Stage 1 brief §7.1 as adjacent canonical reference.
- ✅ Thought-experiment device (barrel underground → priced at one hundred dollars). Matches Stage 1 brief §8 locked element.
- ✅ Naming of *residual commons value* at end of §I. Matches Stage 1 brief §6 apparatus exclusion + §8 framework-naming move.

### §II — What Classical Economics Misses
- ✅ Substitution examples (coal→charcoal; whale-oil→kerosene; copper-fiber). Historically accurate; standard economic-history references.
- ✅ Lithium / cobalt / rare-earths non-renewable framing. Accurate.

### §III — The Lineage Map
- ✅ Marx — *Capital, Volume I* 1867. Per Stage 1 brief §7.10.
- ✅ Ostrom — *Governing the Commons* (Cambridge UP, 1990) + 2009 Nobel Memorial Prize (shared with Oliver Williamson, accurately rendered as "shared"). Per Stage 1 brief §7.6.
- ✅ Hardin "tragedy of the commons" reference. Garrett Hardin, *Science* 162(3859): 1243–1248 (1968). Standard reference; not in Stage 1 brief §7 but well-established intellectual reference.
- ✅ Daly — *Steady-State Economics* (W.H. Freeman 1977; rev. Island Press 1991). Per Stage 1 brief §7.7. Daly's death in 2022 correctly noted.
- ✅ Daly & Farley — *Ecological Economics: Principles and Applications* (Island Press, textbook). Per Stage 1 brief §7.7.
- ✅ Hartwick 1977 — *American Economic Review* 67(5): 972–974; "Intergenerational Equity and the Investing of Rents from Exhaustible Resources." Per Stage 1 brief §7.1. Volume / issue / page numbers all match.

### §IV — Rawls Across Time
- ✅ Rawls — *A Theory of Justice* (Harvard UP, 1971). Per Stage 1 brief §7.8.
- ✅ Sandel — *What Money Can't Buy: The Moral Limits of Markets* (FSG, 2012). Per Stage 1 brief §7.9.
- ✅ Parfit — *Reasons and Persons* (Oxford UP, 1984). Per Stage 1 brief §7.9. Parfit's non-identity problem characterization accurate.

### §V — The Existing Battleground
- ✅ Stern Review — released October 2006 as independent review to UK Government, published Cambridge UP 2007. Per Stage 1 brief §7.3.
- ✅ "UK Treasury" commissioning attribution — defensible. Gordon Brown (then Chancellor of the Exchequer) commissioned the review; Stern was at the Treasury during the review's preparation. Sometimes cited as "UK Government" more broadly; "UK Treasury" is the more specific institutional attribution.
- ✅ 700-page review length. Per Stage 1 brief §7.3.
- ✅ "Greatest and widest-ranging market failure ever seen" direct quote. Per Stage 1 brief §7.3.
- ✅ ~1% of global GDP per annum. Per Stage 1 brief §7.3.
- ✅ Stern's ~1.4% discount rate. Per Stage 1 brief §7.3.
- ✅ Stern's pure-rate-of-time-preference justification ("not discounted simply because they are future"; "only legitimate discount is for the small probability that the future will not exist"). Accurate to Stern's Chapter 2 framework — Stern uses 0.1% per year for catastrophe risk.
- ✅ ~$360/ton social cost of carbon. Per Stage 1 brief §7.3.
- ✅ Nordhaus — DICE (Dynamic Integrated Climate-Economy) model. Per Stage 1 brief §7.4.
- ✅ Nordhaus 2018 Nobel Memorial Prize "for integrating climate change into long-run macroeconomic analysis" (the Nobel committee's citation). Per Stage 1 brief §7.4.
- ✅ Nordhaus's ~4.3% discount rate in early DICE iterations. Per Stage 1 brief §7.4.
- ✅ Nordhaus's market-rate-of-return justification. Accurate to Nordhaus's standard methodology argument.
- ✅ ~$35/ton SCC in same comparison frame. Per Stage 1 brief §7.4.
- ✅ Discount-rate illustration: $100 a century out → ~$25 at 1.4%, ~$1.50 at 4.3%. Per Stage 1 brief §7.4 ($24.90 / $1.48; Draft A rounds accurately to $25 / $1.50 in prose-friendly form).
- ✅ Weitzman 2009 — *Review of Economics and Statistics* 91(1): 1–19; "On Modeling and Interpreting the Economics of Catastrophic Climate Change." Per Stage 1 brief §7.5. Volume / issue / page numbers all match.
- ✅ Weitzman's death in 2019 correctly noted (August 27, 2019).

### §VI — Honest Accounting
- ✅ Ekofisk discovery December 1969, Block 2/4, North Sea. Per Stage 1 brief §7.2. The "three days before Christmas" phrasing matches the brief (LOW-priority precision note: authoritative sources cite the discovery as December 23, 1969 = two days before Christmas Day; "three days before Christmas" is a rhetorical-resonance phrase inherited from the source-draft and the Stage 1 brief; defensible as approximate timing language).
- ✅ Government Petroleum Fund established 1990. Per Stage 1 brief §7.2.
- ✅ Renamed Government Pension Fund Global 2006. Per Stage 1 brief §7.2.
- ✅ Cross-coalition durability walk — Stoltenberg I (Labour) → Bondevik II (center-right coalition) → Stoltenberg II (Labour) → Solberg (Conservative coalition) → Støre (Labour-Centre). Per Stage 1 brief §7.2 / §7.11. All coalition-party characterizations verified accurate.
- ✅ Saro-Wiwa execution 1995 (Nov 10, 1995, by hanging) by the Abacha regime. Per Stage 1 brief §7.12.
- ✅ "Along with eight of his colleagues" — the Ogoni Nine. Accurate.
- ✅ Commonwealth suspension in protest. Suspension November 11, 1995; lifted 1999 after Abacha's death + civilian transition. Per Stage 1 brief §7.12.
- ✅ UNEP Ogoniland Environmental Assessment 2011 (August 4, 2011). Per Stage 1 brief §7.12.
- ✅ ~$1B initial capitalization estimate + 25–30 years projected restoration. Per Stage 1 brief §7.12.
- ✅ Operator joint-venture structure (Shell, Chevron, ExxonMobil, Total + NNPC). NNPC formed 1977; joint-venture model standard since then. "ExxonMobil" is anachronistic for pre-1999 operations (Mobil merged with Exxon in 1999) but standard contemporary usage.
- ✅ Architecture-fix-not-revolution locked register-anchor — "What I am calling for, then, is not revolution. I do not think revolution solves this." Verbatim match to Stage 1 brief §8 locked element.
- ✅ "Not a left-wing argument. It is not a right-wing argument. It is a principle of honest dealing." Matches Stage 1 brief §8 register-anchor.
- ✅ *Cost severance* inline definition — framework term; defined in plain language per Stage 1 brief §5 + §6 (lowercase noun phrase permitted; no formal "Cost Severance" capitalized framework term).

### §Close
- ✅ Lineage recap walks Marx → Ostrom → Daly → Hartwick → Rawls / Sandel / Parfit → Stern / Nordhaus / Weitzman. All previously verified.
- ✅ *Residual commons value* naming-and-leaving close. Matches Stage 1 brief §4 + §6.

---

## 3. Synthesis — cumulative diagnosis + Phase C application order

### 3.1 Findings by severity

| Severity | Count | Findings |
|---|---|---|
| CRITICAL | 0 | — |
| HIGH | 1 | F-FC-Barrel-1 (Norway fiscal rule 4%→3% history) |
| MEDIUM | 3 | F-FC-Barrel-2 (fund size submission-week verify); F-FC-Barrel-3 (Niger Delta production figure + decade-count timing); F-FC-Barrel-4 (pump-price hook submission-week verify) |
| LOW | 1 | F-FC-Barrel-5 (per-citizen figure derivation) |
| Canonical-truth-gap (CTG) | 1 | CTG-1 (Stage 1 brief §7.2 Norway fiscal rule history) |

### 3.2 Phase C-α (HIGH; load-bearing)

1. **F-FC-Barrel-1** — Norway fiscal rule 4%→3% history. Verbatim correction provided. Apply at Phase C-α.

### 3.3 Phase C-β (MEDIUM; precision-sharpening + submission-window verifications)

2. **F-FC-Barrel-3** — Niger Delta decade-count + production figure. Author selects between two proposed corrections; apply at Phase C-β.
3. **F-FC-Barrel-2** — Norway fund size submission-week verification. Apply at submission-week, not Phase C-β.
4. **F-FC-Barrel-4** — Pump-price hook submission-week verification. Apply at submission-week, not Phase C-β.

### 3.4 Phase C-γ (LOW; optional sharpening)

5. **F-FC-Barrel-5** — Per-citizen figure derivation. Auto-recalculated if F-FC-Barrel-2 produces a materially different fund-size figure at submission-week. Otherwise no change.

### 3.5 Stage 1 brief Amendment A repairs (separate cross-artifact workstream)

6. **CTG-1** — Repair Stage 1 brief §7.2 to reflect the 4%→3% rate-change history. Recommend a separate Amendment A repair session against the Stage 1 brief artifact post-Phase C application. Parallels the Noema Pass 3.1 CTG repair pattern.

### 3.6 Cross-pass impact summary

| Finding | Affects Pass 3.2 voice-polish? | Affects Pass 3.3 acceptance? | Affects Pass 3.4 robustness? | Affects Pass 3.5 developmental-edit? |
|---|---|---|---|---|
| F-FC-Barrel-1 | No | Marginal positive (PW editorial; Stone Center; Stern-tradition) | Marginal positive (orthodox-econ A5) | No |
| F-FC-Barrel-2 | No | None (submission-week only) | None | No |
| F-FC-Barrel-3 | No | Marginal positive (Mazzucato-cluster; Ostrom-successor; general policy economist) | Marginal positive (orthodox-econ A5 thread proactively closed) | No |
| F-FC-Barrel-4 | No | None (submission-week only) | None | No |
| F-FC-Barrel-5 | No | None | None | No |

**No Pass 3.2 voice-polish impact across any finding.** All corrections are surgical at the fact level; none require voice re-flow.

### 3.7 Submission-readiness verdict

**Phase C-α + Phase C-β corrections required before Pass 3.2 voice-polish fires.** Submission-week verifications (F-FC-Barrel-2 + F-FC-Barrel-4) are gated to submission week and do not block downstream Stage 3 passes.

The essay is **substantively submission-ready** after Phase C-α + Phase C-β apply. Pass 3.2 voice-polish, Pass 3.3 acceptance re-verification, Pass 3.4 robustness re-verification, and Pass 3.5 developmental-edit all fire in sequence per per-prompt serial cadence.

Compared to the Noema Pass 3.1 fact-check (4 HIGH + 4 MEDIUM findings), this pass surfaces a notably cleaner result (1 HIGH + 3 MEDIUM + 1 LOW). The cleaner outcome reflects two factors: (1) the Stage 1 brief §7 inventory for $100 Barrel was authored with the v3.0 / v3.1 discipline in view and embedded most factual ground truth at brief-construction time; (2) Draft A is a single derivative essay from a brief that is internally tighter on factual specifics than the Noema brief was at parallel maturity. The one HIGH finding (F-FC-Barrel-1) traces upstream to the same Norway-fiscal-rule canonical-truth-gap that the Noema Pass 3.1 caught — a known Amendment A gap, not a Draft A drift.

---

## 4. Methodology notes

### 4.1 Path B compliance — re-verified

Draft A's Stage 2 cover declarations report "0 verbatim sentences from withdrawn-Noema §III in body." Pass 3.1 did not re-open withdrawn-Noema §III as source-of-truth per v2.0 Path B preemptive policy + Stage 1 brief §9 hard constraint. Path B compliance is treated as established by Stage 2 declarations.

### 4.2 Audit-existing-prose mode applied

Per template §"Audit-existing-prose mode": Pass 3.1 fact-check applied for time-sensitive claims + canonical-truth verification per Amendment A discipline. Stage 1 brief §7 served as the canonical baseline. External-citation verification performed for HIGH-severity calls (F-FC-Barrel-1 Norwegian fiscal rule history).

### 4.3 v3.1 five-pass discipline compliance

Per v3.1 Amendment B 2026-05-18, Stage 3 is a five-pass discipline. Per-prompt serial cadence preserved: each pass fires in its own session; author ratifies + Phase C spot-fixes apply before next pass fires. This Pass 3.1 artifact stops at findings + proposed corrections; Phase C application is a separate session; Pass 3.2 voice-polish fires after Phase C application.

### 4.4 Stage 1 brief Amendment A canonical-truth-gap incidence

This pass surfaced **one** Stage 1 brief CTG (CTG-1, Norway fiscal-rule history). The Noema Pass 3.1 surfaced six CTGs. The lower incidence here is consistent with the more disciplined Stage 1 brief construction for $100 Barrel (post-Amendment-A codification of the canonical-truth-section discipline). Future Stage 1 briefs (Aeon post-acceptance; Boston Review) should embed a fact-check sub-pass at brief-construction time per the Noema Pass 3.1 §6.4 methodology recommendation.

---

## 5. Hand-off to author + Phase C application session

**Author actions required:**

1. **Ratify findings.** Review F-FC-Barrel-1 through F-FC-Barrel-5 + the CTG-1 canonical-truth-gap flag. For each finding, decide: (a) apply proposed correction as drafted; (b) modify correction; (c) reject (with reason). For F-FC-Barrel-3, choose between the two proposed correction options (preserve original figure + tighten time-span; or update both figure + time-span).
2. **Spin up Phase C application session** for ratified spot-fixes. Phase C-α (F-FC-Barrel-1 HIGH) → re-fire light Pass 3.1 spot-check on the corrected location → Phase C-β (F-FC-Barrel-3 MEDIUM) → Pass 3.2 voice-polish fires.
3. **Submission-week verifications** — schedule for ~2026-06-01 to ~2026-06-08:
   - F-FC-Barrel-2: pull current NBIM fund-value figure; update if materially different.
   - F-FC-Barrel-4: pull current EIA Weekly Retail Gasoline and Diesel Prices report; verify directional claim or apply contingency rewrite.
   - F-FC-Barrel-5: recalculate per-citizen figure if F-FC-Barrel-2 produces a materially different fund-size figure.
4. **Spin up Stage 1 brief Amendment A repair session** for CTG-1. Separate workstream from Phase C application against the essay file. Parallels F-FC-Noema-1's CTG repair.

**Submission-window coordination:** The $100 Barrel essay's target submission window is ~2026-06-01 to ~2026-06-08 (Stage 1 brief §11). The four-pass Stage 3 sequence (3.2 voice-polish → 3.3 acceptance re-verification → 3.4 robustness re-verification → 3.5 developmental-edit) needs to complete before submission. With this Pass 3.1 + Phase C-α + Phase C-β surgical (single HIGH + one MEDIUM prose-edit; the rest are submission-week verifications), Pass 3.2 should fire within the next session window and Pass 3.5 should complete before the submission window opens.

---

## 6. Hard-constraints adherence verification

- [x] No spot-fixes applied to the essay file. PROPOSED artifact only.
- [x] No named subjects contacted. (Public-record exception applies to all named subjects per Stage 1 brief §9 + `tools/memory/feedback_named_subject_consent.md`.)
- [x] No Pass 3.2 voice-polish, Pass 3.3 acceptance, Pass 3.4 robustness, or Pass 3.5 developmental-edit work performed. Separate sessions per v3.1 five-pass discipline.
- [x] Withdrawn-Noema §III NOT re-opened as source-of-truth. Stage 1 brief §7 IS the truth.
- [x] Canonical-truth gap in Stage 1 brief (CTG-1) flagged as Amendment A repair, not silently corrected.
- [x] Per-finding format: F-FC-Barrel-K + severity + location + verbatim text + source-of-truth + Stage 1 brief baseline + proposed correction + cross-pass impact + CTG flag where applicable.
- [x] Canonical-truth-gap flag for facts not traceable to Stage 1 brief + lacking external citation.
- [x] Whole-essay synthesis §: cumulative diagnosis + recommended Phase C-α + Phase C-β + Phase C-γ application order + cross-pass impact table.
- [x] v3.1 five-pass discipline acknowledged; per-prompt serial cadence preserved.

---

## 7. Cross-references

- **Audit target:** [`publishing/essays/100-barrel/essay.md`](../../publishing/essays/100-barrel/essay.md)
- **Stage 1 brief (source of truth):** [`publishing/essays/100-barrel/rigor/stage-1-brief.md`](stage-1-brief.md)
- **Prior pass (comparative draft audit):** [`stage-3-comparative-draft-audit.md`](stage-3-comparative-draft-audit.md)
- **Sibling Pass 3.1 (Noema; format precedent + parallel CTG-1):** [`pass-3-1-fact-check.md`](../../publishing/essays/noema-commons-bonds/rigor/pass-3-1-fact-check.md)
- **Bibliography:** [`research/literature/bibliography.md`](../../research/literature/bibliography.md)
- **v3.1 discipline reference:** [`tools/memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md)
- **Pipeline doctrine (five-pass Stage 3 codification):** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) §3.6 Amendment B 2026-05-18

---

## 8. Ratification record

**2026-05-21 — PROPOSED.** Pass 3.1 fact-check artifact for $100 Barrel Draft A. 1 HIGH + 3 MEDIUM + 1 LOW finding; 1 Stage-1-brief canonical-truth-gap. No Pass 3.2 voice-polish impact across any finding. Phase C-α + Phase C-β surgical (single HIGH + one MEDIUM prose-edit). Submission-readiness verdict: substantively submission-ready after Phase C-α + Phase C-β apply; submission-week verifications (F-FC-Barrel-2, F-FC-Barrel-4) gated to submission week.

Awaiting author ratification of:
1. **F-FC-Barrel-1 verbatim correction** (Norway fiscal rule 4%→3% history).
2. **F-FC-Barrel-3 correction option selection** (preserve figure + tighten time-span; or update both).
3. **Phase C-α session** spin-up after ratification.
4. **CTG-1 Stage 1 brief repair session** spin-up (separate workstream).
5. **Submission-week verification schedule** for F-FC-Barrel-2 + F-FC-Barrel-4 + F-FC-Barrel-5 (~2026-06-01 to ~2026-06-08).

---

*End of Pass 3.1 fact-check artifact. PROPOSED status. STOP. Author ratification + Phase C application is a separate session. Pass 3.2 voice-polish fires after Phase C-α + Phase C-β application per v3.1 per-prompt serial cadence.*
