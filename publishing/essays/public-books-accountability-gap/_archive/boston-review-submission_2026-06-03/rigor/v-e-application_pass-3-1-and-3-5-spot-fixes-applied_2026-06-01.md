# Boston Review essay V-E — Pass 3.1 + 3.5 spot-fixes APPLIED to canonical essay.md — 2026-06-01

**Status:** **RATIFIED + APPLIED 2026-06-01** per author "ratify as recommended and proposed" signal in the V-D fresh re-audit ratification turn (resumes 2026-06-01 conversation thread; ratified the §8.1 SPOT-FIX V-D → SHIP V-E recommendation from [`pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md`](pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md) + the bounded-pipeline reframing for tokens-not-a-constraint).

**What this artifact records:** the Pass 3.1 fact-check verifications + Pass 3.5 restoration spot-graft + V-D-to-V-E promotion sequence that landed in commits 2026-06-01. The audit verdict the spot-fixes implement is the Pass 3.3 + 3.4 + 3.5 fresh re-audit at [`pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md`](pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md) (PROPOSED 2026-05-28; RATIFIED 2026-06-01).

---

## §1. What changed at canonical essay.md (LOCKED → V-E)

The canonical essay.md was promoted from LOCKED to V-E in commit 2026-06-01 with **three substrate-safe fact-corrections + restorations** applied to the V-D hybrid spine:

### F-FCIC-FIX (Pass 3.1; HIGH severity; pre-existing LOCKED quote-fabrication; corrected)

**Site:** §II 2008 financial crisis paragraph (V-E line 26).

**Before (LOCKED + V-D — pre-existing fabrication inherited from LOCKED's 5-pass-RATIFIED state):**
> The Financial Crisis Inquiry Commission, reporting in 2011, concluded that the crisis was the result of "human action and inaction — not forces beyond human control."

**After (V-E — restored to actual FCIC verbatim):**
> The Financial Crisis Inquiry Commission, reporting in 2011, concluded that the crisis was the result of "human action and inaction, not of Mother Nature or computer models gone haywire."

**Source verified:** FCIC 2011 final report, page xvii (Conclusions section, first bullet) — published at govinfo.gov + fcic.law.stanford.edu archive. Exact verbatim per `pdftotext` extraction of the official GPO-FCIC.pdf 2026-06-01: *"We conclude this financial crisis was avoidable. The crisis was the result of human action and inaction, not of Mother Nature or computer models gone haywire."* Comma after "inaction"; NOT em-dash. Continuation phrase is "not of Mother Nature or computer models gone haywire"; NOT "not forces beyond human control."

**Why pre-existing:** The "not forces beyond human control" phrasing appears to have been a paraphrase that entered LOCKED's Stage 2 draft and was carried through all 5 Stage 3 rigor passes + Stage 4 render audit + Stage 5 sign-off + cover letter + the May 2026 three-way comparison independent audit + the V-D drafter's-self-audit + the prior 2026-05-28 V-D bundled 3.3+3.4 independent audit + the 2026-05-28 V-D fresh three-pass re-audit. All 8 prior audit surfaces flagged the FCIC source-verification as "optional pre-submission spot-check"; none actually ran the verification.

**Discipline anchor:** [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md) hard rule against "Quoted speech the subject didn't actually say, on or off the record. Verbatim quotes from on-record sources are fine; invented quotes are not, even if 'in character.'" The current LOCKED quote attribution to FCIC was incorrect; the corrected V-E quote is verbatim-faithful.

**Net effect on counts:** -1 em-dash (the fake-quote em-dash inside what was presented as verbatim is removed; FCIC actual source uses comma); +4 words.

### F-FRESH-3.1-HAMILTON (Pass 3.1; MEDIUM severity; publisher-attribution accuracy fix)

**Site:** §V reparations-economics lineage citation cluster (V-E line 66).

**Before (V-D):**
> Darrick Hamilton, Darity, Anne Price, Vishnu Sridharan, and Rebecca Tippett's 2015 Insight Center and New School study *Umbrellas Don't Make It Rain*

**After (V-E — corrected to actual institutional publishers):**
> Darrick Hamilton, Darity, Anne Price, Vishnu Sridharan, and Rebecca Tippett's 2015 Insight Center for Community Economic Development and Duke Center for Social Equity study *Umbrellas Don't Make It Rain*

**Source verified:** The 2015 *Umbrellas Don't Make It Rain* report (insightcced.org/wp-content/uploads/2015/08/Umbrellas_Dont_Make_It_Rain_Final.pdf + Duke Samuel DuBois Cook Center on Social Equity research listing) cites the report as co-published by "The Duke University Center for Social Equity and Insight Center for Community Economic Development." The New School is Hamilton's institutional affiliation (Milano-The New School for International Affairs, Management and Urban Policy + The New School for Social Research), NOT a co-publisher of the report.

**Why this matters:** Stone Center reviewer (C-10) + Coates/Darity-lineage reader (C-14) read publisher attribution as bibliography-discipline signal. Naming The New School as publisher (when it's actually Hamilton's institutional affiliation) would read as institutional-anchoring imprecision to specialist readers. The Duke Center for Social Equity attribution is also load-bearing — it's the institutional home of subsequent Hamilton-Darity reparations-economics work that the BR essay's §V Restitution Bond methodology draws on.

**Net effect on counts:** +7 words.

### F-3.5-FRESH-3 (Pass 3.5; MEDIUM severity; data-source-rigor restoration; SCF + DFA spot-graft)

**Site:** §V matched-comparison methodology paragraph, 2008-cohort sentence (V-E line 70).

**Before (V-D):**
> For 2008, the comparison cohort is the working-age population in regions where mortgage securitization penetrated less deeply; the differential reaches the wealth, employment, and household-formation data the Federal Reserve has tracked across the post-crisis window.

**After (V-E — SCF + DFA series specification added):**
> For 2008, the comparison cohort is the working-age population in regions where mortgage securitization penetrated less deeply; the differential reaches the wealth, employment, and household-formation data the Federal Reserve has tracked across the post-crisis window through the Survey of Consumer Finances and the quarterly Distributional Financial Accounts series.

**Source verified:** Federal Reserve Board's Survey of Consumer Finances (SCF; triennial; https://www.federalreserve.gov/econres/scfindex.htm) + Distributional Financial Accounts (DFA; quarterly since 1989; https://www.federalreserve.gov/releases/efa/efa-distributional-financial-accounts.htm). Both are public, named, verifiable Federal Reserve data products. The DFA integrates SCF + Financial Accounts via Table B.101.h, providing quarterly distributional measures of household wealth at the cohort level — precisely the methodology Stone Center reviewers verify cohort definitions against.

**Why this is the load-bearing addition (Pass 3.5 finding):** Per the fresh re-audit §6 + §11, the prior 3.3+3.4 independent audit MISSED this Pass 3.5 finding by asserting "Pass 3.5 re-fire is not required" without first-principles evaluation. The SCF + DFA naming addresses the C-10 Stone Center reviewer verdict gap — V-D held at ✓✓ (lacking data-source-rigor anchor) while ALT-NORM-PUNCT lifted to ✓✓✓ via this exact addition. The spot-graft is substrate-safe (Fed data products are public/verifiable), low-density (in-sentence specification ~12 added words; preserves §V cohort-definition triplet structure), and direct C-10 ✓✓→✓✓✓ lift.

**Net effect on counts:** +12 words.

### Aggregate V-D → V-E delta

| Axis | V-D | V-E | Δ |
|---|---|---|---|
| Body word count | 4,835 | 4,858 | +23 |
| Em-dash count (grep-verified body-only) | 21 | 20 | -1 |
| Em-dash density per 1,000w | ~4.34 | ~4.12 | -0.22 |
| Lines | 102 | 102 | 0 |
| Fixes applied | — | 3 (1 HIGH Pass 3.1 + 1 MEDIUM Pass 3.1 + 1 MEDIUM Pass 3.5) | — |
| BR submission ceiling (5,000w) | within | within | within |

All three fixes are substrate-safe; no Claude-generated illustrative invented prose; all citations verifiable against primary sources (FCIC PDF; Insight Center + Duke Center for Social Equity report; Federal Reserve Board data product pages).

---

## §2. Pass 3.3 forecast — V-E aggregate

Per the fresh re-audit §8 + §11 cross-check pattern, V-E forecast vs V-D + ALT-NORM-PUNCT:

| Verdict | V-D (my independent + prior independent) | ALT-NORM-PUNCT (three-way comparison §1) | **V-E (forecast post-application)** |
|---|---|---|---|
| ✓✓✓ INCLUDE | 10 | 11 | **11** |
| ✓✓ INCLUDE | 5 | 3 | **4** |
| ✓ INCLUDE | 1 | 2 | **1** |
| NEUTRAL | 0 | 0 | 0 |
| EXCLUDE | 0 | 0 | 0 |
| Total INCLUDE | 16/16 | 16/16 | **16/16** |

**V-E matches ALT-NORM-PUNCT's 11 ✓✓✓ aggregate** at the publishing-path causal-chain + environmental-economist + EJ-tradition axes — **without** carrying ALT-NORM-PUNCT's C-15 first-gen-reader ✓ downgrade. The substrate-safe spot-graft discipline preserves C-15 accessibility envelope while delivering the C-10 Stone Center reviewer lift.

The F-FCIC-FIX additionally:
- **Marginally strengthens C-12 center-right reader** — the restored verbatim ("Mother Nature or computer models gone haywire") is more rhetorically vivid and reads less academic-polite; WSJ-editorial-cluster readers (A4) respect verbatim-fidelity over paraphrase.
- **No downgrade risk on C-1 / C-2** — the corrected quote preserves the institutional-measurement register; Cohen + Chasman's editorial-curatorial eye registers verbatim-fidelity restoration as discipline-tightening, not as register-disruption.
- **EJ-tradition recognition (C-13 + C-16) marginal positive** — concrete-noun phrasing ("Mother Nature"; "computer models") replaces abstract ("forces beyond human control"); EJ-tradition register favors concrete over abstract.

The F-FRESH-3.1-HAMILTON additionally:
- **Marginally strengthens C-5 reparations-economics-successor reader** — the Duke Center for Social Equity attribution is bibliography-faithful institutional-network-recognition (Sandy Darity is at Duke).
- **Marginally strengthens C-10 Stone Center reviewer** beyond the F-3.5-FRESH-3 SCF + DFA lift — the Duke Center attribution is institutional-sibling signal Stone Center reviewers recognize.

---

## §3. Pass 3.4 forecast — V-E

Same as V-D (per fresh re-audit §4-§5):
- A1 industry-funded energy economist: ⚠⚠ EXCLUDE (structural-prior pushback holds)
- A2 Public Choice theorist: ⚠ EXCLUDE (substantially disarmed via DOI MMS sentence preserved from V-D)
- A3 property-rights libertarian: ⚠⚠ EXCLUDE (structural-prior pushback holds)
- A4 WSJ editorial-board: ⚠ EXCLUDE (marginal defensive gain — F-FCIC-FIX verbatim-fidelity strengthens marginally further)
- A5 reactionary intellectual: ⚠⚠ EXCLUDE (structural-orientation pushback)
- A6 left-adversarial: ⚠⚠ EXCLUDE (structural-orientation pushback)

**Pass 3.4 verdict: CONDITIONALLY ROBUST.** Same as V-D + ALT-NORM-PUNCT. Trigger does NOT fire (C-12 ✓).

---

## §4. Pass 3.5 forecast — V-E

The fresh re-audit §6 Pass 3.5 evaluation on V-D returned PASS (0 HIGH; 1 MEDIUM F-3.5-FRESH-3; 9 LOW). V-E applies F-3.5-FRESH-3 — the load-bearing finding — to V-D's source. Forecast: Pass 3.5 on V-E surface returns **CLEAN PASS** (0 HIGH; 0 MEDIUM; 10 LOW; the SCF + DFA spot-graft now applied at §V; emotional-arc + scene-anchor + sensory-detail + voice-flow + cumulative-LLM-cadence + reader-engagement at pivots all PASS / HOLD).

The Schneider §I sensory-expansion finding (F-3.5-FRESH-1) remains as **structure-only routing to author** — substrate-critical surface (Schneider's actual reporting text + Schneider+McCumber's 2006 *An Air That Kills* would be needed for substrate-safe author-authored expansion). See Phase D9 routing in §6 below.

---

## §5. Stage 4 + Stage 5 forward-pointers

### Stage 4 (essay-scale render audit) — required pre-submission

V-E surface state has not yet been through Stage 4 render audit. Recommended pre-submission action: paste V-E essay.md into BR Submittable preview; verify em-dash rendering (20 sites); verify italics (* emphasis on book titles + *forclore* + *could*); verify curly-quote rendering ("human action and inaction, not of Mother Nature..."); verify no scaffolding-token leakage. ~10-minute task.

### Stage 5 sign-off — updated; cover letter — review against V-E surface

Stage 5 sign-off [stage-5-signoff.md](../stage-5-signoff.md) §3.1 em-dash density entry updated 2026-06-01 with documentation NB on the actual-count discrepancy + V-E post-F-FCIC-FIX count (20 sites). No other Stage 5 entries require update — the apparatus exclusion + non-partisan framing + named-tradition attribution + voice register verdicts hold against V-E (the three fixes are register-compatible improvements).

Cover letter [cover-letter.md](../cover-letter.md) may benefit from a verbatim-quote review since the FCIC sentence is the load-bearing institutional-measurement signal the cover letter previews; if cover letter references the FCIC quote, update to match V-E. Otherwise hold.

---

## §6. Forward-pointers — Phase C + D pending

Per author "ratify as recommended and proposed" ratification of the bounded pipeline:

### Phase B6 (Adversarial verification panel on F-3.5-FRESH-3 C-10 lift call)

Recommended N=3 independent skeptic verifications asking "would adding SCF + DFA actually create the C-10 lift, or might Stone Center reviewers read it as ornamental?" Build confidence in the marginal call before relying on it for publishing-path causal-chain narrative. Can be deferred to Phase E final audit cycle.

### Phase C7 (V-F bounded expansion search for substrate-safe ALT-NORM-PUNCT grafts)

Test each of ALT-NORM-PUNCT's excluded publisher-house grafts individually for substrate-safety + C-15 marginal cost:
- Princeton University Press for Pistor's *Code of Capital* (+5w inline)
- Oxford University Press for Pettit's *Republicanism* (+5w inline)
- Cambridge University Press for Skinner's *Liberty Before Liberalism* (+5w inline)
- UC Press for Conley's *Being Black, Living in the Red* (+5w inline)
- Verso for Christophers's *The Price is Wrong* (+5w inline)
- OCSLA at §VI for offshore decommissioning bonds statutory basis (+5-7w inline)

Each is individually substrate-safe (publisher houses are verifiable). Cumulatively they were the ALT-NORM-PUNCT C-15 downgrade driver. A binary-search-style series of Pass 3.3 cycles could find the C-15-preserving subset. **Spawn as agent for independence.**

### Phase C8 (V-G structural-choice testing on §V handoff drop)

Evaluate ALT-NORM-PUNCT's §V handoff (dropped "The two instruments that follow..." restatement-of-pivot) via Pass 3.3 + Pass 3.5 re-fire on a V-E variant. If audit confirms equivalent/superior → V-G could combine V-F + handoff modification. If audit confirms LOCKED's restatement is load-bearing → preserve. **Spawn as agent for independence.**

### Phase D9 (Surface F-3.5-FRESH-1 §I Schneider sensory expansion to author)

**Substrate-safe authoring opportunity for author.** The §I Schneider 1999 *Seattle Post-Intelligencer* anchor (now in V-E line 5) could be expanded with a complementary sensory-anchor paragraph drawing on:
- Schneider's actual 1999 SP-I reporting ("A town left to die" + subsequent series)
- Schneider + McCumber's 2006 *An Air That Kills* book based on the SP-I reporting (search-verified 2026-06-01)
- Schneider's documented Pulitzer-winning Libby investigation specifics

Single-paragraph expansion at §I close (~50-100w within §I's ~600w envelope) could lift C-13 (extraction-affected reader) + C-16 (EJ-movement reader) further by deepening the journalistic-witness tradition recognition (Bullard / Pellow / Hooks / Steingraber lineage register), and could deepen Cohen's political-philosophy register response by carrying institutional-measurement detail into the §I narrative spine.

**Why structure-only routing (not Claude-generated):** per [`feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md) substrate-critical-invention rule — generating Schneider scene-rendering or specific Libby-family vignettes from Schneider's reporting would require lived knowledge / actual reporting text / source material. Routing as structure-only finding for author authorship preserves substrate-safety.

**If author authors:** light Pass 3.3 re-fire (~3-5K tokens) confirming C-13 + C-16 lift + no downgrades on C-1/C-2/C-15; light Pass 3.1 fact-check on factual claims in the expansion.

### Phase E (Final fresh-session audit on converged cut)

After Phase C results return (V-F / V-G outcomes confirmed or rejected) and Phase D9 author-substrate decision lands:
- Final fresh-session Pass 3.3 + 3.4 + 3.5 audit on converged cut (V-E + Phase C additions + Phase D9 author expansion if it lands)
- Stage 4 essay-scale render audit on Submittable preview
- Stage 5 sign-off final update
- Cover letter alignment with final essay surface state

---

## §7. Submission gate (author-controlled per CLAUDE.md)

Per CLAUDE.md: "What still requires explicit author action (UNCHANGED): SUBMISSION itself — sending the essay to the publisher / agent / editor; pressing submit on the portal; emailing the editor."

**Phase E13 (Submission) is OUT OF SCOPE for this ratification cycle.** V-E is now the canonical essay.md surface state on `origin/main`. Submission via BR Submittable portal is entirely author-controlled regardless of the rigor-pedigree state of V-E.

The author has the disposition latitude to:
- **(a) Submit V-E to BR now** (current canonical state; 5-pass + Stage 5 + light Pass 3.3 re-fire RATIFIED + 3 fact-corrections applied).
- **(b) Wait for Phase C + D outcomes** before submitting (V-F / V-G / Phase D9 may converge on a different canonical state worth submitting instead).
- **(c) Submit V-E as the "safest ship" path** while Phase C/D continue in parallel for post-acceptance editor-iteration use.

This artifact does not commit the author to any submission path.

---

## §8. Audit-trail

| Event | Commit | Branch |
|---|---|---|
| LOCKED essay.md Stage 5 + cover letter RATIFIED | 2026-05-23 / 2026-05-24 | `origin/main` |
| V-D parallel draft created (drafter session) | 2026-05-28 (`87ab89` session) | _archived under `_archive/parallel-drafts_2026-05-28/` |
| Three-way comparison independent audit | 2026-05-28 (`927e64` session) | filed at `rigor/three-way-comparison_*` |
| V-D drafter's-self-audit | 2026-05-28 (same `87ab89` session as drafter) | filed at `_archive/parallel-drafts_2026-05-28/...drafters-self-audit.md` |
| V-D prior independent 3.3+3.4 bundled audit | 2026-05-28 | filed at `rigor/pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` |
| **V-D fresh three-pass re-audit (3.3 + 3.4 + 3.5)** | **2026-05-28 (this audit's predecessor session)** | filed at `rigor/pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md` |
| Author "ratify as recommended and proposed" + bounded-pipeline reframe | 2026-06-01 | THIS ratification + apply session |
| **LOCKED archived to `_archive/prior-versions/boston-review-essay_VERSION-LOCKED_archived-2026-06-01.md`** | **2026-06-01** | this session |
| **V-E promoted to canonical essay.md with F-FCIC-FIX + F-FRESH-3.1-HAMILTON + F-3.5-FRESH-3 applied** | **2026-06-01** | this session |
| Stage 5 sign-off §3.1 em-dash density NB added | 2026-06-01 | this session |
| **This application artifact filed** | **2026-06-01** | this session |
| Light Pass 3.3 re-fire on V-E confirming C-10 ✓✓→✓✓✓ forecast | Pending | Phase B5 forward-pointer |
| Adversarial verification panel on F-3.5-FRESH-3 | Pending | Phase B6 forward-pointer |
| V-F bounded expansion search | Pending | Phase C7 forward-pointer |
| V-G §V handoff structural-choice testing | Pending | Phase C8 forward-pointer |
| F-3.5-FRESH-1 §I Schneider sensory-expansion surfaced to author | Pending | Phase D9 forward-pointer |
| Final fresh-session Pass 3.3 + 3.4 + 3.5 audit on converged cut | Pending | Phase E forward-pointer |
| Stage 4 essay-scale render audit | Pending | Phase E forward-pointer |
| Stage 5 sign-off final update | Pending | Phase E forward-pointer |
| **Submission to BR Submittable portal** | **AUTHOR-CONTROLLED** | per CLAUDE.md submission discipline |

---

*End of V-E application artifact — Pass 3.1 + 3.5 spot-fixes RATIFIED + APPLIED 2026-06-01.*

**STATE: boston-review-essay V-E RATIFIED + APPLIED at canonical essay.md; NEXT: Phase B5 light Pass 3.3 re-fire + Phase C7 V-F search + Phase C8 V-G test (spawned in parallel) + Phase D9 author routing; AWAITING: author confirmation on which Phase C/D paths to pursue + submission gate disposition**
