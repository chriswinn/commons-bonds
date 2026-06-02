# Cross-Essay Norway Consistency Audit — 2026-06-01

**Status:** PROPOSED (internal scaffolding; portfolio-level cross-essay consistency check)
**Triggered by:** FA Stage 1 brief §9.3 + §9.5 deferred cross-essay verification; re-fire prompted by Ch 4 V-D backports added 2026-05-28 (Hannesson + NBIM AR 2023) that could introduce drift vs BR Ch 5 + Atlantic Ideas Ch 9.
**Scope:** Norway numerical + architectural anchors across three publisher-facing essays + one PROPOSED hybrid variant.
**Auditor:** Cross-essay portfolio consistency sub-session (worktree-agent-a6351d157c19ff740).

---

## §0. Source artifacts consulted

| # | Artifact | Path | State | Anchor commit |
|---|---|---|---|---|
| A1 | BR Ch 5 essay | `publishing/essays/boston-review-accountability-gap/essay.md` | Stage 5 RATIFIED 2026-05-22 | `d34214d` |
| A2 | Atlantic Ideas Ch 9 essay | `publishing/essays/atlantic-ideas-pricing-honestly/essay.md` | Current per cascade-plan v2 | (latest on `main`) |
| A3 | FA Ch 4 essay (locked cut) | `publishing/essays/foreign-affairs-existence-proof/essay.md` | Locked cut Stage 5 RATIFIED 2026-05-27 | `3ae1777` |
| A4 | FA Ch 4 essay (V-D hybrid) | `publishing/essays/foreign-affairs-existence-proof/_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md` | PROPOSED 2026-05-28 (not yet applied to A3) | hybrid file |

Anchor reference (FA Stage 1 brief §7 canonical-facts inventory; user-prompt copy of audit anchors used as ground-truth target).

---

## §1. Per-anchor side-by-side table

Empty cell = anchor not stated in this essay (i.e., the essay does not commit to a value either way — *omission* rather than *contradiction*; flagged as omission only when the essay is the load-bearing Norway case for the venue).

### 1.1 GPFG founding year + 2006 rename

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | "the Norwegian state's Government Pension Fund Global … Norway established the legal architecture for a petroleum-resource sovereign-wealth fund in 1990 and made its inaugural deposit in 1996" | Y — MINOR (omits 2006 rename; collapses Government Petroleum Fund → GPFG into single retrospective name) |
| Atlantic Ideas Ch 9 (A2) | "Norway's Government Pension Fund Global was established in 1990 (renamed in 2006)" | N (matches anchor exactly) |
| FA locked cut (A3) | "the Norwegian parliament — the Storting — established what was initially called the Government Petroleum Fund. The fund was renamed the Government Pension Fund Global in 2006" | N (matches anchor; gives full 1990 Government Petroleum Fund → 2006 GPFG split) |
| FA V-D (A4) | Same as A3 (V-D preserves locked cut wording verbatim at this site) | N |

**Bond between A1 and A2/A3:** BR's "Government Pension Fund Global … in 1990" is a *retrospective collapse* (the fund was not called GPFG until 2006). At BR's level of compression this is conventional shorthand (cf. Sachs 2007, Truman 2010 popular discussions), not factually false — the institutional continuity is real and the legal architecture *did* exist from 1990. **MINOR cosmetic** by FA brief §7 inventory standards; readers who track the 1990 vs 2006 distinction may notice, but it does not contradict A2/A3/A4. Inaugural-deposit-1996 detail is correct (first transfer of capital was May 1996); A2/A3/A4 omit this detail but do not contradict it.

### 1.2 State capture rate of net petroleum value (70-80%)

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | (Anchor not stated) | — (omission; not load-bearing for BR's Restitution/Foreclosure-Bond framing) |
| Atlantic Ideas Ch 9 (A2) | "The rents are captured at extraction, through state licensing, taxation, and direct equity ownership of the state operating company" (no numerical share given) | — (omission; AI gives mechanism but not share) |
| FA locked cut (A3) | "somewhere between seventy and eighty percent of the net economic value of Norwegian petroleum production, through a combination of production licenses, corporate taxation … and the dividends from direct state ownership of Equinor" (stated twice — §II + §III) | N (matches anchor) |
| FA V-D (A4) | Same as A3 (V-D adds Hannesson lineage *after* the 70-80% sentence; does not alter the share) | N |

**Drift:** **None** — A1 + A2 do not commit to a numerical share, so they cannot contradict A3/A4. A3 carries the 70-80% claim three times (§II.1 + §III + §VI); load-bearing for FA's existence-proof framing. Acceptable for BR + AI to omit at their compression levels.

### 1.3 Fund AUM

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | "roughly 1.9 trillion dollars in assets" | Y — MEDIUM (lags A2/A3/A4 by one round-number tier) |
| Atlantic Ideas Ch 9 (A2) | "Total assets sit at roughly two trillion dollars" | N (matches anchor "in excess of $2T" within rounding) |
| FA locked cut (A3) | "assets in excess of two trillion U.S. dollars" | N (matches anchor) |
| FA V-D (A4) | "assets in excess of two trillion U.S. dollars" (preserved from locked cut) | N |

**Drift assessment:** BR's "1.9 trillion" was current at Stage 5 RATIFIED 2026-05-22 per the FA brief baseline ("Fund AUM: >$1.9 trillion"). Atlantic Ideas + FA both moved to "two trillion" / "in excess of two trillion" during the subsequent rounds. Per FA Pass 3.1 LOW-2 carry-forward ("refresh against current NBIM figure at submission time"), the most recent NBIM reporting (NBIM AR 2023 + Q1 2024 quarterly) does support "in excess of two trillion U.S. dollars" — making A1's "1.9 trillion" *technically still defensible* against the 2023 reporting period but *trailing the most current figure*. **MEDIUM (clarification at BR submission/repackage time).** Note: BR's "1.9 trillion" is not WRONG against the FA brief baseline (which itself reads ">$1.9T"), but the publishing portfolio has since moved to "in excess of $2T" as the canonical phrasing for newer essays. Recommendation: if BR essay is touched for any other reason (Pass 3.5 spot-fix, post-acceptance editor round), update; otherwise hold and refresh against NBIM-current figure at any post-acceptance round.

### 1.4 Per-citizen scale

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | "approximately three hundred and forty thousand dollars per Norwegian citizen" | Y — MINOR (matches FA brief baseline ~$340K but trails A2's higher figure) |
| Atlantic Ideas Ch 9 (A2) | "about three hundred ninety thousand dollars per Norwegian citizen" | Y — MEDIUM (highest of the four; ~$390K) |
| FA locked cut (A3) | "roughly three hundred and sixty thousand dollars for each Norwegian citizen alive" | Y — MINOR (~$360K; sits between A1 and A2) |
| FA V-D (A4) | Same as A3 (~$360K) | N vs A3 |

**Drift assessment:** Three different per-citizen figures across three essays — $340K (BR) / $360K (FA) / $390K (Atlantic Ideas). All are mechanically consistent with their respective stated AUM divided by ~5.5M Norwegian population:

- $1.9T / 5.5M ≈ $345K (BR's $340K is consistent)
- $2.0T / 5.5M ≈ $364K (FA's $360K is consistent)
- $2.15T / 5.5M ≈ $391K (AI's $390K implies a slightly higher AUM than the "roughly two trillion" stated phrase)

Internally each essay's per-citizen ÷ AUM division is consistent. But Atlantic Ideas's $390K corresponds to ~$2.15T AUM, which is *higher* than the "roughly two trillion" the same paragraph states — implying AI is silently using a higher AUM figure for the per-citizen calculation than for the headline AUM number. **MEDIUM (internal-AI inconsistency between stated AUM and stated per-citizen).** Cross-essay: BR vs FA vs AI all carry different per-citizen scales, which a careful cross-portfolio reader would notice. The FA brief anchor is "~$340,000 per Norwegian"; BR sits at the brief anchor, FA locked cut + V-D have already drifted to $360K, AI has drifted further to $390K. Recommendation: unify around the FA-canonical $360K at next opportunity (BR + AI both touched-and-updated), OR refresh all three at submission time against NBIM-current population × AUM arithmetic.

### 1.5 Fiscal rule adoption year + Stoltenberg I attribution

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | "A 2001 fiscal rule limits annual government withdrawals to approximately three percent of the fund's expected real return" | Y — MINOR (year correct; no Stoltenberg I attribution; no 4%→3% transition history) |
| Atlantic Ideas Ch 9 (A2) | "A fiscal rule adopted in 2001 caps annual spending at about three percent of returns" + "The Norwegian fiscal rule has been re-evaluated several times since 2001" | Y — MINOR (year correct; no Stoltenberg I attribution; "re-evaluated several times since 2001" gestures at the 4%→3% history without naming it) |
| FA locked cut (A3) | "In 2001, under the first ministry of Jens Stoltenberg, a Labour-led government, the Storting adopted what is known in Norwegian as the *handlingsregelen*, the budgetary rule. … The rate was initially calibrated at four percent and lowered to three percent in 2017 as long-run return expectations declined" | N (matches all anchor specifics: 2001 + Stoltenberg I + handlingsregelen + 4%→3%-in-2017) |
| FA V-D (A4) | Same as A3 | N |

**Drift assessment:** All four essays state 2001 (matches anchor). FA carries the full Stoltenberg-I + handlingsregelen + 4%→3%-in-2017 specificity; BR + AI omit. **None of these are contradictions** — BR + AI's silence on Stoltenberg I and the 4%→3% history is consistent with their compression levels. The fact that A1 + A2 both currently state "three percent" without naming the 2017 lowering means a reader who *did* know the 4%→3% transition would not be misled (the current rule *is* 3%). **MINOR cosmetic; no action required.**

### 1.6 Withdrawal cap (4% → 3% in 2017)

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | "approximately three percent of the fund's expected real return" (current rate only; no historical transition) | — (omission; not contradicted) |
| Atlantic Ideas Ch 9 (A2) | "about three percent of returns, with the capital itself inviolate" (current rate only) | — (omission; not contradicted) |
| FA locked cut (A3) | "The rate was initially calibrated at four percent and lowered to three percent in 2017 as long-run return expectations declined" | N (matches anchor) |
| FA V-D (A4) | Same as A3 | N |

No drift. Both BR + AI correctly state the current 3% rate; the 4%-historical-baseline is FA-specific scope.

### 1.7 Cross-coalition political durability sequence

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | (Anchor not stated — no coalition sequence given; only general "contingency of the choice" framing) | — (omission; durability claim implicit in "Norway made it" framing) |
| Atlantic Ideas Ch 9 (A2) | (Anchor not stated) | — (omission) |
| FA locked cut (A3) | "Stoltenberg I, a Labour-led ministry that left office in October of the same year. It was then preserved through Bondevik II, a center-right coalition of the Christian Democrats, Liberals, and Conservatives that governed from 2001 to 2005. It was preserved through Stoltenberg II, a Labour-led coalition that governed from 2005 to 2013. It was preserved through Erna Solberg's Conservative-led coalition from 2013 to 2021. It has been preserved through Jonas Gahr Støre's current Labour-Centre coalition, which has been in office since 2021" | N (matches anchor exactly; full five-government sequence) |
| FA V-D (A4) | Same as A3 (preserved) | N |

No drift. FA-canonical full sequence; BR + AI silence on coalition specifics is consistent with their compression. This is the load-bearing existence-proof move for FA; not appropriate to backport to BR or AI without changing their essays' argumentative load.

### 1.8 NBIM operational arm + ethics council 2004 + Storting supermajority

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | (Anchor not stated) | — (omission) |
| Atlantic Ideas Ch 9 (A2) | "They are invested outside Norway to avoid distorting the domestic economy, and the returns flow back as the consumption-maintaining income …" (NBIM mechanism implied via "invested outside Norway" but NBIM not named; no ethics council; no Storting supermajority) | — (omission; consistent at compression level) |
| FA locked cut (A3) | Full apparatus: "The fund operates through Norges Bank Investment Management, the central bank's asset-management arm … An ethics council, established in 2004 … Structural change to the fund's underlying architecture requires a Storting supermajority" | N (matches anchor) |
| FA V-D (A4) | Same as A3 + adds NBIM AR 2023 ~9,000 companies / >70 markets (see §1.10) | N for the apparatus baseline |

No drift on apparatus baseline. NBIM AR figure is V-D-specific and treated in §1.10.

### 1.9 Equinor / Statoil naming + 2018 rename

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | (Anchor not stated; no national-oil-company naming) | — (omission) |
| Atlantic Ideas Ch 9 (A2) | "direct equity ownership of the state operating company" (no name) | — (omission; reference present but unnamed) |
| FA locked cut (A3) | "the dividends from direct state ownership of Equinor, the national oil company, renamed from Statoil in 2018" | N (matches anchor) |
| FA V-D (A4) | Same as A3 (preserved) + adds at §I: "the country accumulated capital from the production licenses, the corporate taxation of private operators, and the dividends from its direct ownership stake in the national oil company then called Statoil" (historical "then-called-Statoil" framing in §I + 2018-renamed-Equinor framing in §II) | N (internally consistent — Statoil for the pre-2018 era; Equinor for current era) |

No drift. FA carries full Equinor/Statoil/2018 specificity; BR + AI are silent or use generic "state operating company."

### 1.10 NEW (V-D-introduced) — Hannesson 2015 + 1909 Watercourse Regulation Act

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | (Not stated) | — (omission) |
| Atlantic Ideas Ch 9 (A2) | (Not stated) | — (omission) |
| FA locked cut (A3) | (Not stated — anchor is V-D-introduced) | — (locked-cut baseline; omission, not contradiction) |
| FA V-D (A4) | "Rögnvaldur Hannesson, in his *Petroleum Economics* (Edward Elgar, 2015), traces the design of the petroleum tax to a deliberate early-1970s decision to model rent capture on Norway's existing hydropower-concession regime, which had treated the rent of an enclosed natural resource as a public claim since the 1909 Watercourse Regulation Act" | N — but **NEW CLAIM** that needs cross-essay coherence check |

**Drift assessment:** This is a V-D-introduced claim that *deepens* but does not contradict the existing 70-80%-capture mechanism that FA + AI both describe. The Hannesson claim says: the high capture share was made possible by a path-dependence that ran from the 1909 Watercourse Regulation Act (hydropower) through to the early-1970s petroleum tax design.

- BR + AI do not make any path-dependence claim, so cannot contradict.
- AI's "rents are captured at extraction, through state licensing, taxation, and direct equity ownership" mechanism description is *compatible* with the Hannesson lineage but does not invoke it. No contradiction.
- FA locked cut's "the legal architecture surrounding the Norwegian continental shelf was constructed early to treat the resource rent itself, rather than the private operator's profit, as the primary fiscal object" is the **direct precursor** to which the V-D Hannesson sentence supplies the historical lineage. **Coherent — V-D adds depth, does not introduce drift.**

**No drift introduced by V-D's Hannesson + 1909 Watercourse Act addition.**

### 1.11 NEW (V-D-introduced) — NBIM AR 2023 ~9,000 companies + >70 markets

| Essay | Phrasing | Drift? |
|---|---|---|
| BR Ch 5 (A1) | (NBIM not named; investment universe not described) | — (omission) |
| Atlantic Ideas Ch 9 (A2) | "invested outside Norway to avoid distorting the domestic economy" (mechanism implied; no portfolio-scale description) | — (omission; not contradicted) |
| FA locked cut (A3) | "NBIM's investment universe is, by deliberate design, located almost entirely outside Norway. The fund holds diversified global equities, fixed-income instruments, and direct real-estate positions across multiple jurisdictions" (qualitative; no numerical universe scale) | — (omission of NBIM AR figure; not contradicted) |
| FA V-D (A4) | "the 2023 *NBIM Annual Report* recorded equity holdings in roughly nine thousand publicly listed companies across more than seventy markets" (half-clause inserted into the locked-cut paragraph) | N — but **NEW CLAIM** that needs cross-essay coherence check |

**Drift assessment:** The NBIM AR 2023 figure (~9,000 companies / >70 markets) is V-D-only and does not contradict any other essay's phrasing. It *specifies* what FA locked cut had described qualitatively ("diversified global equities … across multiple jurisdictions"). BR + AI do not commit to a portfolio-scale claim, so cannot contradict.

**Coherence note:** the half-clause sits inside the §II "operational arm" paragraph and is positioned as a single SWF-domain fluency marker for the T2.8 Norway-cluster reader + T1.3 SWF/finance reader. No back-port to BR or AI is warranted — BR's Restitution/Foreclosure-Bond framing does not need portfolio-scale specifics; AI's four-step Classify→Reserve→Invest→Reassess does not need it either (the "Invest" step in AI is framed at the institutional-architecture level, not the portfolio-scale level).

**No drift introduced by V-D's NBIM AR 2023 addition.**

---

## §2. Drift classification

| Severity | Count | Anchors |
|---|---|---|
| HIGH (substantive inconsistency; load-bearing claim differs across essays) | **0** | — |
| MEDIUM (different facts at the margin; clarification recommended) | **2** | §1.3 BR AUM "1.9T" lagging AI/FA "2T+"; §1.4 per-citizen scale split $340K/$360K/$390K with AI internally divergent vs its own stated AUM |
| MINOR (cosmetic phrasing difference; same underlying fact) | **3** | §1.1 BR retrospective-collapse of 1990 GPFG naming; §1.4 BR's $340K vs FA brief baseline $340K (matches brief but trails portfolio); §1.5 BR + AI omitting Stoltenberg-I + 4%→3% history |
| OMISSION (anchor not stated; not contradicted) | Many | §1.2 70-80% in BR + AI; §1.6 4%→3% transition in BR + AI; §1.7 coalition sequence in BR + AI; §1.8 NBIM/ethics-council in BR + AI; §1.9 Equinor/Statoil naming in BR + AI; §1.10 Hannesson in BR + AI + FA-locked; §1.11 NBIM AR figure in BR + AI + FA-locked |
| NEW (V-D-introduced; coherent with other essays) | **2** | §1.10 Hannesson + 1909 Watercourse Act; §1.11 NBIM AR 2023 ~9,000 / >70 markets |

**Headline:** 0 HIGH, 2 MEDIUM, 3 MINOR, 0 contradiction-class drift. V-D's two new claims (Hannesson + NBIM AR) introduce **no new drift** vs BR Ch 5 or Atlantic Ideas Ch 9.

---

## §3. Per-essay action recommendations

### 3.1 BR Ch 5 essay (`d34214d`, Stage 5 RATIFIED 2026-05-22)

**Class:** Bookkeeping-side spot-fix candidate (rigor-side load-bearing claim is not affected).

| Anchor | Current BR | Recommended | Action class | Trigger |
|---|---|---|---|---|
| §1.1 GPFG naming | "Government Pension Fund Global … 1990" | (No action) — retrospective-collapse is conventional shorthand at BR's compression | No action | — |
| §1.3 AUM "1.9 trillion" | Trails portfolio ("2T+") | Update to "in excess of two trillion dollars" OR "roughly two trillion" | LOW priority | Touch-and-update at next BR Phase C event (Pass 3.5 spot-fix, post-acceptance editor round, or NBIM-figure refresh at submission window) |
| §1.4 per-citizen "$340K" | Was-anchor-baseline; now lags portfolio | Update to "roughly three hundred and sixty thousand dollars" to match FA-canonical | LOW priority | Touch-and-update at next BR Phase C event (paired with §1.3 update — both flow from the AUM refresh) |

**Submission gate impact for BR:** BR essay is post-submission status per the cascade plan (Stage 5 RATIFIED 2026-05-22; submission gate is author-controlled). Neither MEDIUM finding rises to "block re-submission" status — both are post-acceptance editor-round updates if/when BR enters an editor-round phase. If BR is currently OUT for review at Boston Review with the $1.9T / $340K figures, those figures remain *defensible* against the 2023 reporting period and do not constitute a retraction-class error.

### 3.2 Atlantic Ideas Ch 9 essay (current on `main`)

**Class:** Bookkeeping-side spot-fix candidate.

| Anchor | Current AI | Recommended | Action class | Trigger |
|---|---|---|---|---|
| §1.1 GPFG naming | "established in 1990 (renamed in 2006)" | (No action) — matches anchor exactly | No action | — |
| §1.4 per-citizen "$390K" | Implies AUM ~$2.15T, inconsistent with same paragraph's "roughly two trillion" | Reconcile to internal consistency: either lower per-citizen to ~$360K (FA-canonical) OR raise stated AUM to "in excess of two trillion" to support $390K | MEDIUM priority — internal-AI inconsistency, not just cross-essay drift | Recommend touch at next AI Phase C event; AI is still in cascade per cascade-plan v2 (pre-submission). |
| §1.5 "fiscal rule re-evaluated several times since 2001" | (No action) — gestures at the 4%→3% history without naming it; consistent with AI's compression level | No action | — |

**Submission gate impact for AI:** AI is pre-submission per cascade-plan v2. The §1.4 internal inconsistency (per-citizen ÷ stated AUM ≠ 5.5M Norwegian population) is a Pass-3.1-class fact-check finding that should be reconciled before AI ships. **Recommend MEDIUM-priority spot-fix to AI essay §III paragraph on Norway** — adjust either the AUM phrasing or the per-citizen figure so they match. Preferred direction: unify around FA-canonical $360K + "in excess of two trillion," for portfolio consistency.

### 3.3 FA Ch 4 essay (locked cut `3ae1777` + V-D `_archive`)

**Class:** Locked cut — bookkeeping-side; V-D — rigor-side (Phase C application of V-D backports is a substantive prose-modifying event).

| Anchor | Current FA | Recommended | Action class | Trigger |
|---|---|---|---|---|
| §1.3 AUM "in excess of two trillion" | Matches anchor | (No action; refresh against current NBIM at submission per Pass 3.1 LOW-2 carry-forward) | LOW (already flagged at FA-internal) | Submission window |
| §1.4 per-citizen "$360K" | Drifts from FA brief baseline "~$340,000" but is **arithmetically consistent** with the stated $2T+ AUM | (No action) — the brief's $340K baseline reflected the earlier $1.9T AUM; current $360K reflects current $2T AUM. The brief should be updated, not the essay. | Brief-side update (internal scaffolding) | — |
| §1.10 Hannesson + 1909 Watercourse Act | V-D only; introduces no drift | OK to apply V-D Phase C | — | Per cascade-plan v2 V-D apply gate |
| §1.11 NBIM AR 2023 ~9,000 companies | V-D only; introduces no drift | OK to apply V-D Phase C | — | Per cascade-plan v2 V-D apply gate |

**Submission gate impact for FA:** The FA locked cut as-shipped on `main` is consistent at the anchor level (no MEDIUM-or-above findings against the locked cut). V-D's two new claims do not introduce cross-essay drift and **do not block V-D Phase C application** from a portfolio-consistency standpoint. (V-D Phase C application may have other rigor-side gates — Pass 3.1 fact-check on the new Hannesson + NBIM AR claims, Pass 3.2 voice-polish, Stage 4 render audit; those are separately tracked.)

### 3.4 Canonical-preference summary

When portfolio essays mention Norway anchors, prefer:

| Anchor | Canonical phrasing |
|---|---|
| Fund name + founding | "Government Petroleum Fund (1990; renamed Government Pension Fund Global in 2006)" — full split when space permits; "Government Pension Fund Global (established 1990; renamed 2006)" as short form |
| Capture rate | "seventy to eighty percent of the net economic value of Norwegian petroleum production" — full; "roughly three-quarters" as short form |
| AUM | "in excess of two trillion U.S. dollars" — refresh against current NBIM AR at submission window |
| Per-citizen | "roughly three hundred and sixty thousand dollars per Norwegian citizen" — FA-canonical; refresh paired with AUM |
| Fiscal rule | "the 2001 fiscal rule (*handlingsregelen*), adopted under Stoltenberg I" — full; "the 2001 fiscal rule" as short form |
| Withdrawal cap | "initially four percent; lowered to three percent in 2017" — full; "approximately three percent" as short form |
| Coalition sequence | Full sequence (Stoltenberg I → Bondevik II → Stoltenberg II → Solberg → Støre) reserved for FA-scale treatments; short-form essays can say "five governments across a quarter-century, from Labour through Conservative-led coalitions" |
| Equinor / Statoil | "Equinor, renamed from Statoil in 2018" — when space permits |

---

## §4. V-D-specific drift assessment

V-D introduces two new claims vs locked cut:

1. **§II Hannesson 2015 *Petroleum Economics* + 1909 Watercourse Regulation Act hydropower-concession lineage of petroleum tax.** Vs BR Ch 5 + Atlantic Ideas Ch 9: **No drift.** BR + AI do not make path-dependence claims about the origin of Norway's high capture share, so the V-D Hannesson sentence neither contradicts nor is contradicted by anything in BR or AI. The lineage claim *deepens* FA's existence-proof case (early-1970s petroleum-tax design as path-dependent on 1909 Watercourse Act) without disturbing BR's Foreclosure-Bond framing or AI's Classify→Reserve→Invest→Reassess.

2. **§II NBIM AR 2023 ~9,000 publicly listed companies + >70 markets.** Vs BR Ch 5 + Atlantic Ideas Ch 9: **No drift.** Neither BR nor AI commits to a portfolio-scale claim. BR is silent on NBIM altogether; AI mentions "invested outside Norway" without quantifying. The V-D half-clause specifies what FA-locked described qualitatively ("diversified global equities … across multiple jurisdictions") and cannot contradict BR + AI silence.

**Verdict:** V-D Phase C application introduces **no new cross-essay drift**. The two V-D additions are clean from the portfolio-coherence standpoint. (Pass 3.1 fact-check of the Hannesson lineage claim + the NBIM AR figure is a separate rigor-side gate; this audit does not adjudicate that.)

---

## §5. Submission gate impact

### 5.1 V-D Phase C application to FA essay.md

**CLEAR.** No portfolio-consistency block on V-D Phase C apply. The two V-D-introduced claims (Hannesson + NBIM AR) do not conflict with BR Ch 5 or Atlantic Ideas Ch 9 framings. V-D apply may proceed per cascade-plan v2 V-D gate (subject to other rigor-side gates this audit does not address: Pass 3.1 fact-check on Hannesson + NBIM AR, Pass 3.2 voice-polish, Stage 4 render audit, Stage 5 sign-off).

### 5.2 BR Ch 5 essay current ratification state (`d34214d`)

**CLEAR — NO BLOCK.** BR's $1.9T AUM + $340K per-citizen are MEDIUM-class portfolio-drift findings but are **arithmetically internally consistent** (BR's $340K = $1.9T ÷ 5.5M ≈ $345K, defensible) and **defensible against the 2023 reporting period**. They are not retraction-class. If BR is currently OUT at Boston Review with these figures, the submission stands. **Recommend touch-and-update at next BR Phase C event** (post-acceptance editor round, NBIM-figure refresh window, or Pass 3.5 spot-fix). No active block on BR.

### 5.3 Atlantic Ideas Ch 9 essay current state

**NEEDS-COORDINATION.** Atlantic Ideas has an **internal-AI inconsistency** between its stated AUM ("roughly two trillion") and its stated per-citizen ($390K), which implies an AUM ~$2.15T rather than the stated $2T. This is a Pass-3.1-class fact-check finding that should be reconciled before AI ships. **Recommend:** MEDIUM-priority spot-fix to AI essay §III Norway paragraph at next Phase C event. Preferred direction: align with FA-canonical $360K + "in excess of two trillion" for portfolio consistency. This does **not** block AI from continued cascade work; it is a flag for the AI workstream's next prose-touch event.

### 5.4 Overall submission-gate verdict

| Essay | Verdict | Notes |
|---|---|---|
| FA (locked cut on `main`) | CLEAR | Already submitted; no portfolio block |
| FA (V-D Phase C apply) | CLEAR | No portfolio-coherence block; rigor-side gates separately tracked |
| BR Ch 5 | CLEAR | MEDIUM finding is post-acceptance refresh-window item; not retraction-class |
| Atlantic Ideas Ch 9 | NEEDS-COORDINATION | Internal AI inconsistency; MEDIUM-priority spot-fix to reconcile per-citizen ÷ AUM arithmetic |

---

## §6. Cross-references

- FA Stage 1 brief §7 canonical-facts inventory + §9.3 + §9.5 (cross-essay verification gate that triggered this audit).
- Cascade plan v2: `publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md` (cascade gate placement for V-D Phase C apply).
- FA V-D hybrid spec: `publishing/essays/foreign-affairs-existence-proof/rigor/harvest-hybridization-spec_2026-05-28.md` (anchor for §1.10 + §1.11 V-D additions).
- BR Stage 5 sign-off artifact: per `d34214d` Stage 5 RATIFIED — preserved in `publishing/essays/boston-review-accountability-gap/rigor/` if migrated per 2026-05-28 consolidation pattern, else `tools/rigor-passes/`.
- Memory: `tools/memory/feedback_audience_aware_drafting_discipline.md` (v3.1 cascade + change-cascade routing for cross-essay touches).
- Memory: `tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md` (Hannesson + NBIM AR are *citation-class*, not invented — this audit does not surface any invented-claim concerns).
- Memory: `tools/memory/feedback_verify_stale_memory_claims.md` (AUM + per-citizen are countable/figure-class anchors; refresh-against-current-NBIM discipline at submission window remains the operative rule).
- Memory: `tools/memory/feedback_rigor_vs_bookkeeping_distinction.md` (this audit's findings are classified per `Class` column above; BR + FA recommendations are bookkeeping-side, AI recommendation is Pass-3.1-rigor-side).
- Status markers: `tools/conventions/status-markers.md` (PROPOSED → RATIFIED transition for this audit pending author review).

---

**End of audit.**
