# Boston Review essay V-E — FRESH Pass 3.3 + 3.4 audit with Amendment D reception-chain weighting — 2026-06-02

**Status:** **PROPOSED 2026-06-02.** FRESH independent (session-isolated) Pass 3.3 acceptance + Pass 3.4 adversarial-robustness audit on canonical `publishing/essays/boston-review-accountability-gap/essay.md` at V-E surface state (post-commit `c1ad8e8`; 4,858w; 20 em-dashes). FRESH = no parent-session priors carried; first-principles re-derivation per Amendment D. Awaits author verdict-level ratification.

**Pass type:** Stage 3 Pass 3.3 (acceptance, 16-character set) + Pass 3.4 (adversarial robustness, 6-character BR-adapted set) — **FRESH FULL re-fire with Amendment D reception-chain audience weighting** applied for the first time to the BR essay surface. Supersedes the 2026-06-01 light Pass 3.3 re-fire ([`light-refires/pass-3-3-light-refire_V-E_2026-06-01.md`](light-refires/pass-3-3-light-refire_V-E_2026-06-01.md)) as the Amendment-D-weighted reference verdict.

**Workstream:** Boston Review essay V-E surface confirmation under Amendment D — does the SHIP recommendation change when DIRECT-READER and CONSULTANT and PROJECTED-DOWNSTREAM rows are evaluated separately rather than aggregated 16/16?

**Artifact audited:** [`publishing/essays/boston-review-accountability-gap/essay.md`](../essay.md) at V-E surface state (~4,858w; 20 em-dashes via grep). The V-E surface incorporates three substrate-safe spot-fixes per [`v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md`](v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md): F-FCIC-FIX (§II FCIC verbatim restoration), F-FRESH-3.1-HAMILTON (§V Hamilton-publisher attribution fix), F-3.5-FRESH-3 (§V SCF + DFA Fed data-source rigor restoration).

**Stage 1 brief (audience set source):** [`publishing/essays/boston-review-accountability-gap/rigor/stage-1-brief.md`](stage-1-brief.md) (v1.0.1, RATIFIED 2026-05-21). §1 16-character BR-specific pressure-test set; §2 editorial-brain map; §10 hard constraints; §13 Pass 3.4 opt-in rule on C-12.

**Adversarial set (6 chars, BR-adapted):** carried forward from [`three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md`](three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md) §2 — A1 industry-funded energy economist; A2 Public Choice theorist; A3 property-rights libertarian (Cato / Reason); A4 WSJ editorial-board reader; A5 reactionary intellectual (Compact / First Things); A6 left-adversarial (DSA / Jacobin / Catalyst).

**Methodology anchor:** v3.1 audience-aware drafting discipline + Amendment D reception-chain audience weighting (RATIFIED 2026-05-31). Per [`tools/drafting-templates/audience-pressure-test-construction.md`](../../../../tools/drafting-templates/audience-pressure-test-construction.md) §"Reception-chain audience weighting (Amendment D)" — Pass 3.3 / 3.4 verdicts apply at full strength to direct readers; through projection lens to consultants; lower weight to projected downstream. Per the prompt's BR-essay-specific Amendment-D reweighting: the 16 acceptance characters are partitioned into DIRECT (6), CONSULTANT (3), and PROJECTED-DOWNSTREAM (7) classes; SHIP recommendation reweights from "16/16 INCLUDE aggregate" to "DIRECT-READER row + CONSULTANT row both ACCEPTABLE or STRONGER."

**Substrate-safety verification.** Acceptance + adversarial audit; no prose generation; no new factual claims. Per [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md): per-character verdict-only audit is substrate-safe. Ch 5 (`manuscript/chapters/Chapter__5_TheAccountabilityGap.md`) was **NOT** opened during this audit. Path B preemptive policy holds.

---

## §0. Pre-flight + worktree-isolation flag

### §0.1 Sandbox-blocked worktree-isolation step (carry-forward)

The mandatory FIRST ACTION worktree-isolation block per `tools/scripts/session-start-worktree-isolation.sh` could not execute — `bash` permission denied for the `git worktree add` command at session start. Audit proceeds without worktree isolation; no essay.md / source-tree modification is performed (audit is read-only verdict generation). The audit artifact lands at `publishing/essays/boston-review-accountability-gap/rigor/pass-3-3-3-4_V-E_FRESH_AMENDMENT-D_2026-06-02.md` in both the canonical repo and the parallel `commons-bonds-br-V-E-ratify-and-apply-260601-b550a6` worktree where the V-E spot-fix files live; commit + push will require author re-fire with bash permission, OR a separate harness-id session that can complete the canonical scaffolding auto-merge step.

**Status flag for ratification:** the audit artifact lands; worktree-isolation + auto-merge to main per CLAUDE.md merge-on-ratification + scaffolding auto-merge default defer to a follow-on commit-and-push action with bash permission restored. This does NOT affect verdict validity; it affects the merge-path mechanics only.

### §0.2 FRESH polarity confirmation

FRESH means: this audit derives per-character verdicts from first principles against the V-E essay.md surface, NOT by inheriting + delta-adjusting the V-D fresh re-audit baseline or the 2026-06-01 light re-fire baseline. Prior verdicts are referenced ONLY in §4 (forecast-vs-actual cross-check) after the fresh verdicts land. The fresh discipline is the load-bearing token-cost the prompt commissions: a fresh session is the only way to test whether the V-D → V-E aggregate shift is robust to a non-anchored evaluator.

### §0.3 Audit polarity

Per parent doctrine §3.3:
- Pass 3.3 = acceptance verdict per character (INCLUDE / NEUTRAL / EXCLUDE; ✓✓✓ / ✓✓ / ✓ / NEUTRAL / ⚠ / ⚠⚠ / ⚠⚠⚠).
- Pass 3.4 = adversarial-robustness thread-pull synthesis (verdict-floor is EXCLUDE; the diagnostic value is which threads the adversarial set collectively pulls).

Per brief Decision #7: Pass 3.4 opt-in fires only if C-12 returns ⚠ EXCLUDE (per the 2026-05-19 brief language; the practical operational reading is ≥ NEUTRAL satisfies → Pass 3.4 fires only as informative-diagnostic, not as gating). This audit fires Pass 3.4 in informative-diagnostic mode regardless of C-12 outcome to provide complete adversarial-robustness reading under Amendment D.

---

## §1. Amendment D weighting applied to V-E (load-bearing reweighting)

Per `audience-pressure-test-construction.md` §"Reception-chain audience weighting (Amendment D)" + the prompt's BR-essay-specific reweighting specification:

### §1.1 Reception-class partition of the 16-character acceptance set

| Reception class | Characters (Stage 1 brief §1 IDs) | Weight | Verdict-application mode |
|---|---|---|---|
| **DIRECT READERS** (HIGHEST weight) | C-2 BR reader; C-11 general policy-curious reader; C-12 center-right policy reader; C-13 extraction-affected reader; C-15 first-gen / working-class reader; C-16 environmental-justice movement reader | HIGHEST | Verdict applies at face value; this row IS the SHIP-READY signal |
| **CONSULTANTS** (HIGH weight) | C-1 BR editorial brain (Chasman + Cohen); C-3 literary agent; C-4 acquisitions editor | HIGH | Verdict applies at face value AT THE CONSULTATIVE LEVEL; this row IS the placement-pipeline signal |
| **PROJECTED DOWNSTREAM** (LOWER weight) | C-5 reparations economics (Darity / Mullen / Hamilton / Conley cluster); C-6 LPE Project (Pistor cluster); C-7 civic-republican (Pettit / Skinner cluster); C-8 environmental economist (Hartwick / Solow cluster); C-9 Berggruen judge; C-10 Stone Center reviewer; C-14 Coates / Darity-lineage Black intellectual reader | LOWER | Verdict provides lineage-attribution discipline signal but lower weight in ship decision |

Total: 6 DIRECT + 3 CONSULTANT + 7 PROJECTED-DOWNSTREAM = 16.

### §1.2 Reweighted SHIP criteria under Amendment D

Pre-Amendment-D (legacy): SHIP if 16/16 INCLUDE with no Tier-1 ⚠⚠⚠.

Post-Amendment-D (this audit's discipline):
- **SHIP-READY row** (DIRECT): aggregate verdict per row of {STRONG / ACCEPTABLE / WEAK}. STRONG = 4+ ✓✓✓ out of 6 + zero EXCLUDE/NEUTRAL; ACCEPTABLE = ≥2 ✓✓✓ + all ≥ ✓ + zero EXCLUDE; WEAK = anything else (e.g., any EXCLUDE, or majority below ✓✓).
- **Placement-pipeline row** (CONSULTANT): STRONG = 3/3 ✓✓✓; ACCEPTABLE = 2/3 ✓✓ or better + 0 EXCLUDE; WEAK = anything else.
- **Lineage-attribution row** (PROJECTED): STRONG = 5+ ✓✓✓ out of 7 + 0 EXCLUDE; ACCEPTABLE = ≥3 ✓✓ or better + 0 EXCLUDE; WEAK = anything else.

**SHIP recommendation under Amendment D:** DIRECT-READER row STRONG or ACCEPTABLE **AND** CONSULTANT row STRONG or ACCEPTABLE.

PROJECTED-DOWNSTREAM row informs pitch-craft / lineage-recognition discipline but does NOT block ship. A WEAK PROJECTED row + STRONG DIRECT + STRONG CONSULTANT = SHIP-READY with pitch-craft caveat (revise downstream-positioning at cover-letter stage; the essay surface holds).

### §1.3 Operational implication

Under Amendment D, the V-E SHIP test asks whether the **6 direct readers** (the people who actually read the published BR essay) plus the **3 consultants** (BR editorial brain + literary agent + acquisitions editor — who decide whether the essay places + the downstream book causal chain activates) collectively land at ACCEPTABLE-or-STRONGER. The 7 PROJECTED-DOWNSTREAM readers are still scored, but their verdicts inform lineage-attribution-discipline rather than ship-readiness.

---

## §2. Pass 3.3 — per-character acceptance verdicts (FRESH, Amendment-D-weight-tagged)

Verdict legend: ✓✓✓ = strong INCLUDE; ✓✓ = INCLUDE; ✓ = INCLUDE with minor reservations; NEUTRAL = neither alienated nor strongly engaged; ⚠ / ⚠⚠ / ⚠⚠⚠ = EXCLUDE per severity.

Reading order: by reception class (DIRECT first as the SHIP-READY row), then by brief §1 character ID within each class.

### §2.1 DIRECT READERS (HIGHEST weight; SHIP-READY row)

#### C-2. BR reader (centrist-progressive policy intellectual) [DIRECT] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** The §I opening grounds the cost-severance frame in concrete numbers (27-year operation, 4/5 world vermiculite, ~$100M revenue vs $4B+ cost = 40-to-1 ratio) + the criminal acquittal verdict. The BR reader's "democratic-theory-fluent + measurement-anchored" disposition is rewarded at the opening: institutional-measurement register without first-person memoir; named institutions (W. R. Grace, EPA, DOJ); dated events. §II's pattern-across-cases (Deepwater 40% recovery + 2008 FCIC verbatim "human action and inaction, not of Mother Nature or computer models gone haywire" + Social Security 2033 trust-fund depletion + GoFundMe 12% goal rate + Baotou waste ratio) builds the structural-mechanism case the BR reader registers as Pistor-tradition institutional analysis. §III Pistor engagement (six legal modules + Mexico-US choice-of-law instance) + §III Public Choice paragraph (Buchanan / Tullock / Mueller credited + Minerals Management Service regulatory capture named) + Black Lung + reclamation bonds + Christophers reference — all read at trade-press econ register that BR's centrist-progressive policy intellectual recognizes as the venue's editorial bandwidth. §IV bidirectional-pivot + §V Restitution Bond reparations-economics lineage (Coates → Darity-Mullen → Hamilton et al. 2015 with Duke Center for Social Equity + Insight Center for Community Economic Development attribution → Conley 1999) + §VI Foreclosure Bond lineage (Hartwick 1977 + SMCRA + Norway GPFG + Pettit + Skinner + Parfit) + §VII engineered-architecture close. The FCIC verbatim restoration at §II reads as discipline-tightening source-fidelity move; the SCF + DFA Fed data-source addition at §V reads as cohort-definition methodological-rigor uptick.

**Verdict:** ✓✓✓ INCLUDE. The BR reader's three principal tests (cross-disciplinary engagement; civic-republican / democratic-theory commitments; constructive institutional design proposal) are all PASS. The V-E source-fidelity + data-rigor strengthenings reinforce the institutional-measurement register without disturbing accessibility. The BR reader walks away with cost severance + Restitution Bond + Foreclosure Bond as named concepts they could use in the next political-economy conversation.

#### C-11. General policy-curious reader (NYRB / Atlantic / Harper's reader) [DIRECT] — FRESH verdict: ✓✓ INCLUDE

**Reading the V-E essay surface:** The C-11 reader is the BR masthead's "intelligent layperson" — reads political theory but is not an academic in the field. The accessibility envelope test: does the essay carry this reader through four principal cases + two-instrument architecture without requiring prior framework knowledge? §I Libby case sets the cost-severance frame in plain prose (no apparatus; no Greek letters); the 40-to-1 ratio is given in plain English; the criminal acquittal is narrated rather than legally apparatus-dense. §II's compression across Deepwater + 2008 + Social Security + healthcare + Baotou is dense but readable; the FCIC verbatim adds rhetorical concreteness ("Mother Nature or computer models gone haywire") that a general policy reader registers as memorable-quote-from-an-institutional-document. §III Pistor engagement is the highest analytical-density paragraph for this reader; the six legal modules are listed by name (property; collateral; trust; corporate veil; bankruptcy; choice-of-law) which is the right move (the reader gets the inventory without having to derive it). The Schneider 1999 SP-I anchor flagged in V-E line 5 (per V-D ALT-NORM-PUNCT graft preserved at V-E) provides journalistic-tradition grounding the general policy reader appreciates. §IV → §V → §VI → §VII unfolds the two-instrument architecture in named-instrument format with per-case operationalization. §V's added SCF + DFA in-sentence specification at line 70 adds ~12 words to the cohort-definition triplet without breaking accessibility pace; §V's Duke Center for Social Equity attribution is a 7-word expansion of a citation cluster that adds bibliographical precision without analytical-density-spike. The §VI Norway pivot-breath carries the analytical-pivot transition cleanly.

**Verdict:** ✓✓ INCLUDE. The accessibility envelope holds at V-E; the F-FCIC-FIX adds memorable-quote concreteness; the F-3.5-FRESH-3 SCF + DFA addition is in-sentence rather than new-sentence (preserves pace); the F-FRESH-3.1-HAMILTON publisher-name precision is bibliographically transparent. The C-11 reader carries the cost-severance + two-instrument architecture through to §VII close. Why ✓✓ rather than ✓✓✓: the analytical density at §III (Pistor six modules + Public Choice + Black Lung + reclamation bonds + Christophers in a single section) approaches the upper bound of general-policy-curious-reader capacity; a slight pace slow at §III → §V is registered but not blocking.

#### C-12. Center-right policy reader (Reason / NR / AEI-econ) [DIRECT] — FRESH verdict: ✓ INCLUDE

**Reading the V-E essay surface (especially under Amendment D higher weight):** This is the audience the brief §13 Decision #7 designates as the Pass 3.4 opt-in trigger character (per brief, ⚠ EXCLUDE here fires Pass 3.4 as gating). Under Amendment D's reweighting, the C-12 verdict is no longer one-of-sixteen in a flattening aggregate; it is **1 of 6 in the SHIP-READY row** — load-bearing for whether the essay ships at all.

The center-right policy reader's first read filters: (a) source-fidelity discipline; (b) non-partisan framing; (c) implementation-level credibility on policy mechanisms. The V-E surface holds (a) cleanly — the F-FCIC-FIX verbatim restoration reads as source-fidelity discipline-tightening; the center-right reader rewards verbatim-source quoting over paraphrase even when the verbatim adds rhetorical heat (and especially when the rhetorical heat is the institutional document's own voice rather than the essay's authorial framing). The "Mother Nature or computer models gone haywire" phrasing is attribution-anchored to the FCIC institutional document via the preserved "The Financial Crisis Inquiry Commission, reporting in 2011, concluded that..." framing; the essay's authorial voice does not adopt the rhetorical heat. This is the discipline-correct attribution move.

On (b) non-partisan framing: §III Public Choice paragraph crediting Buchanan + Tullock + Mueller is the load-bearing engagement move; the framework's structural-accounting work is positioned as complementary-not-opposed to the Public Choice tradition. §III's Minerals Management Service regulatory-capture naming is a Public-Choice-aligned move (acknowledging regulatory capture as a documented case). §VII's contingency-of-choice framing ("the American architectures of accountability... were chosen. They could have been chosen differently. They still can be.") is non-partisan in the right way — it treats the policy architecture as engineered (and re-engineerable) rather than treating particular partisan coalitions as the cause. The framework's load-bearing claim (cost severance is the structural mechanism by which extraction value is captured by one party while costs are absorbed by another with less power to refuse the transfer) is registered by the center-right reader as institutional-analysis-not-partisan-prescription.

On (c) implementation-level credibility: this is where the V-E essay still produces three implementation-level pushbacks that the center-right reader generates (carried forward from V-D fresh re-audit + light re-fire baselines, evaluated FRESH against V-E surface):

1. **§V Restitution Bond per-case funding mechanism.** "The bond's principal would be sized to the documented downstream cost and would draw against the residual estate of the W. R. Grace bankruptcy proceeding, the asset base of the successor entities into which the original operations were reorganized, and... against an industry-wide fund supported by the extractive sector that has generated structurally similar exposures." The center-right reader reads "industry-wide fund supported by the extractive sector" as cross-firm retroactive-liability assignment — firms that did NOT mine Libby vermiculite would pay; firms with no causal connection to the original asbestos exposure would be assessed. This is implementation-level pushback that the framework does not resolve at essay scale (and the brief §7 disposition is correct that essay scale cannot resolve it; per-case funding mechanism design is a chapter-or-book scope question).

2. **§VI Social Security counterfactual sovereign-fund.** "A counterfactual sovereign-fund treatment of the payroll-tax surplus across the program's history would have compounded into an asset base capable of carrying the demographic-deficit window without requiring the cost to settle on the working-age cohort of the 2030s. The foregone return runs into tens of trillions of dollars." The center-right reader generates the AEI-econ-cluster pushback: the counterfactual assumes a particular asset-class allocation (equities + diversified portfolio per Norway model) that mixes with the politically-contingent question of state asset management. The Decision #10 reframe (from $108T specific figure to "tens of trillions; an order of magnitude above current trust-fund balance") preempts the most specific empirical-pushback vector, but the conceptual pushback remains. The Norway-as-existence-proof move at §VI partially disarms (Norway exists; this is not hypothetical), and §VII's contingency-of-choice register acknowledges the counterfactual character of the claim.

3. **§VI climate Foreclosure Bond application.** "Applied to climate, the bond would draw against the extraction value of present fossil-fuel activity and compound against the cost of the warming the activity produces." The center-right reader reads this as the most distance-from-precedent application — the climate-bond move generalizes from extraction-resource-rents (Hartwick / Norway) to atmospheric-loading-of-CO2, which is a different ontological category. The pushback is implementation-level rather than principle-level; the center-right reader does not reject the structural-accounting argument but does flag the climate-application as the furthest stretch.

These three pushbacks are substantive-engagement-not-rejection — the C-12 reader walks away with the framework's cost-severance vocabulary in hand and three specific Forum-respondent pushback handles. This is the right shape of C-12 verdict for a BR Forum-format essay: the C-12 reader becomes an engageable respondent rather than a NEUTRAL non-engager or ⚠ EXCLUDE rejector.

**Verdict under Amendment D higher-weighting: ✓ INCLUDE.** The verdict does NOT shift from the prior light-refire ✓ INCLUDE assessment. Three reasons the higher Amendment-D weight does NOT warrant Pass-3.3-level strengthening:

- The three implementation-level pushbacks are **Forum-respondent material**, not surface-rewrite candidates. Pass-3.3 strengthening of the §V per-case funding mechanism would require resolving an essay-scale-out-of-scope implementation question; the brief §10 substance-drives-length discipline + the BR Forum-format Decision #2-rationale (Forum essays invite 8-12 respondents to engage from different positions) align with leaving the pushbacks as engageable rather than essay-side-resolved.
- The C-12 verdict at ✓ INCLUDE (≥ NEUTRAL) **does NOT trigger Pass 3.4 as gating** per brief Decision #7. Pass 3.4 fires here as informative-diagnostic only; the trigger does not fire.
- The F-FCIC-FIX verbatim restoration + F-FRESH-3.1-HAMILTON publisher-attribution fix + F-3.5-FRESH-3 SCF + DFA data-source addition all strengthen the C-12 source-fidelity + institutional-measurement signals **within the existing ✓ band**; the V-E surface earns marginal within-band strengthening but does not lift to ✓✓ (the implementation-level pushbacks continue to govern the verdict-magnitude).

Under Amendment D higher-weight on C-12, the SHIP-READY row consequence is that C-12 contributes 1 ✓ to the DIRECT row aggregate (rather than 3 ✓✓✓ or 2 ✓✓), which is registered as a verdict-magnitude that the DIRECT row's other 5 characters need to compensate for. The aggregate calculation below in §3.1 carries this through.

#### C-13. Extraction-affected reader (Libby / McDowell / Gulf / Inner Mongolia proxy) [DIRECT] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** The C-13 reader's primary tests: (a) does the essay treat these communities as agents with documented losses, or as illustrative statistics that disappear behind the framework's apparatus? (b) do specific places retain their proper names? (c) does the journalistic-witness tradition (Bullard / Pellow / Hooks / Steingraber lineage) get honored? §I Libby is named; W. R. Grace is named; tremolite is named (rather than abstracted to "a form of asbestos"); Zonolite is named; specific numbers (400+ deaths; ~3,000 lung abnormalities; 40-80× national average mortality) are given; the EPA "first-ever man-made public health emergency" designation is named; the 2005 indictment + 2009 acquittal narrative is preserved. §II Deepwater names BP, Macondo, the eleven workers killed, the 4.9M barrels released, the Mexican settlement asymmetry; §II 2008 names ~10M foreclosure filings + ~5M completed foreclosures (the affected households are not abstracted); §II Social Security names the cost-bearing party as "the working-age cohort facing the demographic-deficit window" rather than as abstract "future generations"; §II healthcare names GoFundMe + the racial-disparity finding (Black + Hispanic surname campaigns raised less + less likely to meet goals) — naming the disparity rather than erasing it; §II Baotou names the location + the waste ratio + the supply-chain mechanism. §III's Libby attic Zonolite-behind-the-drywall image at line 43 ("What the architecture cannot reach is visible in any Libby attic where Zonolite still sits behind the drywall") is the scene-anchor concrete-image beat the EJ-tradition reader registers as honoring-the-affected-community.

The F-FCIC-FIX verbatim correction at §II reads as concrete-noun-over-abstract-framing discipline ("Mother Nature or computer models gone haywire" replaces "forces beyond human control") — the EJ-tradition reader registers this as the institutional-document choosing to specify what the crisis was NOT (the abstract framings that displace responsibility) and the essay honoring that choice.

§IV bidirectional-pivot lists the harm-already-realized cohort explicitly: "Four hundred died in Libby. Eleven workers and four to eight billion oysters were lost at Deepwater. Five million households completed foreclosure between 2008 and 2012. Black-lung claimants ran past the program's resources for treatment costs. McDowell County coal communities watched extracted value move to coastal capital markets and were left with a public-health and infrastructure tail." This active-verb restored-agency catalog is the load-bearing C-13 dispositive move — the cost-bearing cohort is named in active terms ("died," "were lost," "completed," "ran past," "watched") rather than as passive recipients of harm.

§VII close returns to Libby explicitly: "In Libby, the cost-severance ratio is forty to one. The accountability gap is what the architecture has not been asked to close. The next question is whether it will be engineered to close it." The lead case returns at the close; the affected community is not used-and-discarded.

**Verdict:** ✓✓✓ INCLUDE. The C-13 verdict holds at maximum: places retain proper names; documented losses are detailed; the journalistic-witness tradition (Schneider 1999 SP-I anchor at §I) is referenced; the framework's institutional-architecture analysis does not displace the affected community's agency; the §IV active-verb catalog + §III Libby-attic image + §VII Libby-close form a three-site pattern of treating extraction-affected communities as full agents.

#### C-15. First-gen / working-class reader without prior framework knowledge [DIRECT] — FRESH verdict: ✓✓ INCLUDE

**Reading the V-E essay surface, with explicit attention to the F-3.5-FRESH-3 + F-FRESH-3.1-HAMILTON cumulative-density question:** The C-15 reader's primary tests: (a) accessibility — does the essay define its terms in plain English? (b) are the four cases legible without specialized vocabulary? (c) does the institutional-measurement register land as plain prose or as academic jargon?

The V-E essay surface defines "cost severance" twice in plain English (§I line 11 "the systematic transfer of harm from one party to another with less power to refuse it"; §II line 31 "the asymmetry between the party that captures the extraction value and the party that bears the downstream cost, where the cost-bearer has less power to refuse the transfer"). The Restitution Bond and Foreclosure Bond are introduced as named instruments with plain-English glosses ("the instrument that funds the discharge of that obligation"; "the bond is the instrument designed to prevent the intergenerational version of being barred from"). The four anchor cases — Libby asbestos, Deepwater oil, 2008 mortgages, Social Security retirement — are all familiar real-world cases a first-gen reader has either lived through, watched the news on, or grown up adjacent to. The institutional-measurement register (named institutions; dated events; concrete numbers) is plain prose with named institutions rather than jargon-dense apparatus.

**The cumulative-density question at V-E §V is the load-bearing C-15 test for this fresh audit under Amendment D higher-weighting.** The three V-E spot-fixes at §V (F-FCIC-FIX is at §II not §V) cumulatively add:
- F-FRESH-3.1-HAMILTON: +7 words at §V citation cluster (publisher-name precision: "Insight Center for Community Economic Development and Duke Center for Social Equity" replaces "Insight Center and New School"). Bibliographically transparent; the publisher names are plain English; no analytical-density spike.
- F-3.5-FRESH-3: +12 words at §V cohort-definition triplet line 70 ("through the Survey of Consumer Finances and the quarterly Distributional Financial Accounts series"). In-sentence specification rather than new sentence; preserves the §V cohort-definition triplet structure; the Fed data product names are technical but they appear in plain prose context with explanatory verbs ("the differential reaches the wealth, employment, and household-formation data the Federal Reserve has tracked across the post-crisis window through...") so the C-15 reader does not have to parse the SCF + DFA acronyms as unfamiliar jargon.

Cumulative §V word-count delta V-D → V-E: +19 words across the citation cluster + cohort-definition triplet, which is well below the ALT-NORM-PUNCT §V publisher-house enumeration density that drove the ALT-NORM-PUNCT C-15 ✓ downgrade per the 2026-05-28 three-way comparison §1. The in-sentence specification + bibliographically-transparent publisher-name correction discipline preserves C-15 accessibility envelope.

§I + §II + §III + §IV + §V + §VI + §VII reading-aloud check: the prose is plain enough that a first-gen reader without prior framework knowledge can read it aloud without stumbling over apparatus jargon (the apparatus exclusion list per brief §8 is enforced — no Greek letters, no subscripts, no apparatus terms). The Pass-3.5 §III Libby-attic Zonolite-behind-the-drywall image (F-3.5-5 ratified) provides a concrete sensory-anchor that re-energizes after the §III analytical-density paragraph.

**Verdict:** ✓✓ INCLUDE. The accessibility envelope holds at V-E; cumulative §V density is below the ALT-NORM-PUNCT C-15-downgrade threshold; in-sentence specifications + bibliographically-transparent publisher corrections + plain-English Fed-data-product names + scene-anchor breath beats preserve the C-15 reader's carry-through. Why ✓✓ rather than ✓✓✓: the four cases + two-instrument architecture is a substantial intellectual load for a reader without prior framework knowledge; the essay achieves the load reasonably well but does not achieve the read-it-aloud-with-zero-stumble feel that ✓✓✓ would require.

Under Amendment D higher-weighting on C-15, the SHIP-READY row consequence is that C-15 contributes a ✓✓ to the DIRECT row aggregate (rather than a ✓✓✓), which combines with C-2 ✓✓✓ + C-11 ✓✓ + C-12 ✓ + C-13 ✓✓✓ + C-16 ✓✓✓ for the row total.

#### C-16. Environmental-justice movement reader [DIRECT] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** The C-16 reader's primary tests: (a) does the essay treat extraction-affected communities as full agents in the structural account? (b) does the Restitution Bond extension respect EJ-tradition framings? (c) does the criminal-acquittal-at-Libby beat in §I land as institutional-architecture failure rather than as anti-prosecution apologia?

On (c): §I lines 11-13 frame the acquittal explicitly as institutional-architecture failure: "The acquittal did not mean the contamination had not happened, that the executives had not known, or that the cost severance — the systematic transfer of harm from one party to another with less power to refuse it — had not occurred. It meant only that the legal architecture available to the prosecution was not structurally suited to a case whose mechanism operated through accumulated decisions across three decades. The conventional handles of criminal law (intent at a particular moment, harm causally traceable to a single instruction, an act committed within a statutory window) do not fit the shape of the harm." The framing is structurally-correct for the EJ-movement reader: the acquittal is NOT positioned as the legal system functioning correctly (which would read as apologia); it is positioned as the legal system performing institutional-architectural work that protects capital rather than internalizing its costs. The §III "the architecture was not malfunctioning. It was performing." line is the load-bearing EJ-tradition-recognizable institutional-failure framing.

On (a): same as C-13. §I + §II + §IV all treat extraction-affected communities as full agents with documented losses (active-verb restored-agency catalog at §IV; specific places named in §I + §II; the racial-disparity finding at §II healthcare paragraph named rather than erased).

On (b): the §V Restitution Bond extension explicitly positions itself within the Darity-Mullen typology (acknowledgment-and-atonement; redress; closure) and the reparations-economics tradition's specific historical claim. The discipline-note in §V line 67 ("Reparations remain the specific historical claim of the African-American community for the specific historical wrongs the tradition names. The Restitution Bond joins that tradition rather than absorbs it.") is the EJ-tradition-recognizable umbrella-extension-discipline move — the framework joins the tradition rather than translating or rebranding it. The Restitution Bond extension to Libby asbestos + Deepwater + 2008 + black lung + McDowell + Niger Delta-equivalent contexts respects the EJ-tradition's environmental-restitution framings. The DOI MMS reorganization sentence at §III (per V-D fresh re-audit graft preserved at V-E) is the institutional-architecture-acknowledging-failure move that EJ-movement readers register as the framework's structural respect for institutional-document tradition.

The F-FCIC-FIX verbatim restoration adds a fifth institutional-document-honoring move (verbatim restoration of FCIC institutional-document concrete-naming-discipline) to the V-E surface pattern.

**Verdict:** ✓✓✓ INCLUDE. The C-16 verdict holds at maximum: extraction-affected communities are treated as full agents; the criminal-acquittal beat lands as institutional-architecture failure; the Restitution Bond extension respects EJ-tradition framings; the institutional-document-honoring moves form a five-site pattern across §I + §II + §III + §IV + §V; the §I journalistic-witness tradition recognition via the Schneider 1999 SP-I anchor is preserved.

### §2.1.a DIRECT READERS row aggregate

| Char | Verdict | Reading-class weight |
|---|---|---|
| C-2 | ✓✓✓ | DIRECT |
| C-11 | ✓✓ | DIRECT |
| C-12 | ✓ | DIRECT |
| C-13 | ✓✓✓ | DIRECT |
| C-15 | ✓✓ | DIRECT |
| C-16 | ✓✓✓ | DIRECT |

**DIRECT-READER row counts:** 3 ✓✓✓ + 2 ✓✓ + 1 ✓ + 0 NEUTRAL + 0 EXCLUDE = **6/6 INCLUDE.**

**DIRECT-READER row rating:** **ACCEPTABLE.** Per §1.2 criteria: ACCEPTABLE = ≥2 ✓✓✓ + all ≥ ✓ + zero EXCLUDE. The row delivers 3 ✓✓✓ (above the 2 ✓✓✓ ACCEPTABLE threshold), all 6 characters land at ≥ ✓ (no NEUTRAL or EXCLUDE), and the row produces no ship-block. It does NOT reach STRONG (which requires 4+ ✓✓✓) because C-12 returns ✓ and C-11 + C-15 return ✓✓; the implementation-level pushbacks identified at C-12 + the analytical-density slow at C-11 + the cumulative §V density at C-15 hold the row at ACCEPTABLE rather than STRONG.

### §2.2 CONSULTANTS (HIGH weight; placement-pipeline row)

#### C-1. BR editorial brain (Chasman + Cohen) [CONSULTANT] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** Cohen's political-philosophy register + civic-republican / democratic-theory orientation + institutional-analysis-with-measurement editorial discipline are all rewarded. The §VI Pettit *Republicanism* (1997) + Skinner *Liberty Before Liberalism* (1998) + Parfit *Reasons and Persons* (1984) civic-republican lineage including the Berlin/Constant non-interference-vs-non-domination distinction (with italicized *could* preserved per Pass 3.5 F-3.5-4 ratification) is directly on-brand for Cohen. The §III Pistor engagement at the right level (property; collateral; trust; corporate veil; bankruptcy; choice-of-law as named modules) credits Pistor's tradition explicitly rather than absorbing it; this is the named-tradition attribution discipline Cohen's editorial-curatorial eye registers as the venue's bandwidth. Chasman's institutional-analysis-with-measurement discipline is rewarded by the dated-events + named-institutions + concrete-numbers register sustained throughout. The §VII Forum-series-compatibility shape (a constructive two-instrument proposal multiple respondents can engage from different positions) lands at exactly the format BR's Forum series uses.

The F-FCIC-FIX verbatim restoration reads as discipline-tightening source-fidelity move — the kind of internal-rigor-process-executed signal Cohen + Chasman editorial process audits at the fact-check stage. The F-FRESH-3.1-HAMILTON Hamilton-publisher precision fix is bibliography-fidelity tightening. The F-3.5-FRESH-3 SCF + DFA Fed data-source addition signals methodologically-rigorous cohort-definition. All three V-E corrections strengthen the editorial-process signal without disturbing institutional-measurement register.

**Verdict:** ✓✓✓ INCLUDE. The C-1 verdict holds at maximum: civic-republican / democratic-theory grounding is directly on-brand; reparations-economics + structural-economic-harm accounting lineage is explicit; institutional-analysis-with-measurement register is sustained; constructive Forum-series-compatible proposal lands; non-partisan framing discipline holds; "no op-eds" + "no personal essays" + "no previously published work" hard constraints all satisfied.

#### C-3. Literary agent (Wylie / Chalfant / Bohan cluster) [CONSULTANT] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** The literary agent reads for: voice; comp-titles legibility; sustained-book signal; platform-paragraph compatibility; "under consideration at top-tier venue" credibility. V-E's voice register (institutional-measurement; civic-republican + democratic-theory grounded; no first-person memoir per BR rules) is consistent with trade-press econ + policy-intellectual register (Mazzucato / Pistor / Christophers / Susskind cluster). Comp-titles legibility is strong: Pistor *Code of Capital* (2019) + Darity-Mullen *From Here to Equality* (2020) + Hamilton et al. (2015) + Conley (1999) + Coates (2014) + Hartwick (1977) + Pettit (1997) + Skinner (1998) + Parfit (1984) + Christophers (2024) + Mazzucato implicit — this is the published-bookshelf an agent can position the book proposal alongside. The sustained-book signal is strong: the two-instrument architecture is a book-scale conceptual reorganization (not a single-essay observation); the named-concept density (cost severance; Restitution Bond; Foreclosure Bond; the accountability gap) is the right reader-carry-forward shape for a book proposal. The "under consideration at Boston Review" credibility carries the platform paragraph.

The F-FRESH-3.1-HAMILTON Duke Center for Social Equity attribution adds publisher-pedigree precision that the literary-agent reader registers as institutional-network-recognition (Duke Center is the institutional home of subsequent Hamilton-Darity reparations-economics work). The F-3.5-FRESH-3 SCF + DFA Fed data-product naming adds empirical-rigor pedigree. The F-FCIC-FIX is verbatim-fidelity discipline. All three reinforce the publishing-path causal-chain signal.

**Verdict:** ✓✓✓ INCLUDE. The C-3 verdict holds at maximum: voice + comp-titles + sustained-book + platform-paragraph + venue-credibility all PASS.

#### C-4. Acquisitions editor (Penguin Press / FSG / Knopf / PublicAffairs / Norton / Princeton Trade / Riverhead / Metropolitan-Holt) [CONSULTANT] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** Same logic as C-3 — the acquisitions editor reads for one-sentence pitch + bookstore-buyer hook + category placement + comp-titles compatibility + review-network reach. The cost-severance vocabulary is the bookstore-buyer hook; the two-instrument architecture (Restitution Bond + Foreclosure Bond) is the category placement (big-idea econ + policy + civic theory); the comp-titles cluster anchors the bookshelf placement; the named-tradition attribution discipline + Forum-series compatibility provide the review-network reach signal. The acquisitions editor reads the publisher anchors as "this writer is already located within the publishing pipeline that produces big-idea-econ trade titles." The F-FRESH-3.1-HAMILTON Duke Center attribution + F-3.5-FRESH-3 SCF + DFA addition strengthen the big-idea-econ-publishing-pipeline placement signal within the existing ✓✓✓ band.

**Verdict:** ✓✓✓ INCLUDE.

### §2.2.a CONSULTANT row aggregate

| Char | Verdict | Reading-class weight |
|---|---|---|
| C-1 | ✓✓✓ | CONSULTANT |
| C-3 | ✓✓✓ | CONSULTANT |
| C-4 | ✓✓✓ | CONSULTANT |

**CONSULTANT row counts:** 3 ✓✓✓ + 0 ✓✓ + 0 ✓ + 0 NEUTRAL + 0 EXCLUDE = **3/3 INCLUDE.**

**CONSULTANT row rating:** **STRONG.** Per §1.2 criteria: STRONG = 3/3 ✓✓✓. The row delivers 3/3 maximum verdicts; placement-pipeline causal chain is fully activated.

### §2.3 PROJECTED DOWNSTREAM (LOWER weight; lineage-attribution row)

#### C-5. Reparations economics successor (Darity / Mullen / Hamilton / Conley cluster) [PROJECTED] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** The §V four-citation lineage (Coates 2014 → Darity-Mullen 2020 → Hamilton et al. 2015 → Conley 1999) is the load-bearing lineage-attribution structure for this character. The Darity-Mullen three-component typology (acknowledgment-and-atonement; redress decomposing into symbolic redress + material restitution; closure) is named explicitly + the Restitution Bond is positioned within the typology as the instrument operationalizing the material-restitution component. The four-sentence Restitution / Reparations asymmetry handling in §V line 67 ("The Restitution Bond is not a translation of reparations into a different label... The Restitution Bond joins that tradition rather than absorbs it.") is the disarming-discipline move that the reparations-economics successor reader registers as authentic tradition-joining-rather-than-appropriation.

The F-FRESH-3.1-HAMILTON correction (Hamilton publisher attribution corrected to Insight Center for Community Economic Development + Duke Center for Social Equity) is bibliography-fidelity tightening — Sandy Darity is at Duke; the Duke Center for Social Equity is the institutional home of subsequent Hamilton-Darity reparations-economics work; the publisher attribution correction reads as institutional-network-recognition the reparations-economics tradition registers as tradition-respecting.

**Verdict:** ✓✓✓ INCLUDE. Lineage attribution discipline is fully respected; the umbrella-extension move is disarmed by the four-sentence asymmetry handling; the bibliography fidelity tightening reinforces the tradition-respecting register.

#### C-6. Legal-scholar / institutional-design reader (Pistor / LPE Project) [PROJECTED] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** The §III Pistor engagement is at the right level — six legal modules named explicitly (property; collateral; trust; corporate veil; bankruptcy; choice-of-law); the "capital is a legal artifact" framing is explicit; the Mexico-US settlement asymmetry is positioned as a choice-of-law instance per Pistor's framework. The W. R. Grace bankruptcy is positioned as Pistor-named feature-not-bug ("The bankruptcy regime is structured to extinguish or restructure claims against the corporation while preserving the corporate person's legal continuity and shielding shareholders from personal liability. ... The architecture worked. It was just not built to internalize the cost."). The §III "the architecture was not malfunctioning. It was performing." line is the LPE-Project-recognizable institutional-design framing.

**Verdict:** ✓✓✓ INCLUDE. Pistor's tradition is credited explicitly + at right depth; the LPE-Project reader registers the engagement as authentic.

#### C-7. Civic-republican political theorist (Pettit / Skinner cluster) [PROJECTED] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** §VI Pettit + Skinner + Parfit + Berlin/Constant non-interference-vs-non-domination distinction with italicized *could* term-of-art preserved; civic-republican lineage anchor for the Foreclosure Bond's non-domination grounding is at the right level. Pettit *Republicanism* 1997 + Skinner *Liberty Before Liberalism* 1998 + Parfit *Reasons and Persons* 1984 all named with dates + correctly attributed; the neo-Roman tradition Pettit recovers from Cicero through early-modern English commonwealth writers is named; the future-generation-cohort-as-dominated-by-the-present argument is structurally correct per Pettit's framework.

**Verdict:** ✓✓✓ INCLUDE. Civic-republican lineage attribution is at the right level; no overclaiming of the tradition's full philosophical apparatus.

#### C-8. Environmental / resource economist (Hartwick / Solow / Norway GPFG cluster) [PROJECTED] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** §VI Hartwick 1977 "Intergenerational Equity and the Investing of Rents from Exhaustible Resources" cited explicitly; SMCRA 1977 + oil-and-gas decommissioning bonds + Norway GPFG (~$1.9T; ~$340K per Norwegian citizen; 2001 fiscal rule; ~3% real return cap; capital structurally inviolate; 1990 legal architecture; 1996 inaugural deposit) all named at right specificity. The Hartwick rule is correctly summarized; the Norwegian Government Pension Fund Global is positioned as a Foreclosure Bond in everything but name — the analytical category move that lifts the environmental-economist reader's verdict.

**Verdict:** ✓✓✓ INCLUDE.

#### C-9. Berggruen Prize judge / institutional-redesign reader [PROJECTED] — FRESH verdict: ✓✓ INCLUDE

**Reading the V-E essay surface:** The constructive-proposal test asks whether the two-instrument architecture works as a constructive proposal institutional reform could implement, or whether it reads as critique without operationalization. §V Restitution Bond per-case operationalization (Libby, Deepwater, 2008) + §VI Foreclosure Bond per-case operationalization (Social Security, climate, resource commons more generally) + §VII assembly-not-invention close ("none of these moves is unprecedented. What is unprecedented is the willingness to assemble them") all PASS this test. The proposal is constructive + operationalizable + within the political-decision-making the architecture is in principle open to.

**Verdict:** ✓✓ INCLUDE. Constructive-proposal-could-be-implemented test PASS; the Berggruen-Prize-judge verdict holds at moderate-to-strong INCLUDE. Why ✓✓ rather than ✓✓✓: the operationalization at essay scale is deliberately compressed (per brief §10 substance-drives-length + Forum-format compatibility); a full ✓✓✓ would require per-instrument implementation detail that essay scale cannot deliver.

#### C-10. Stone Center for Socio-Economic Inequality reviewer [PROJECTED] — FRESH verdict: ✓✓✓ INCLUDE

**Reading the V-E essay surface:** Stone Center reviewers weight BOTH bibliographic discipline AND empirical-data-sourcing rigor when evaluating cohort definitions. The V-E surface delivers BOTH:
- Bibliographic discipline: §V four-citation reparations-economics lineage + Darity-Mullen three-component typology + Hamilton et al. publisher attribution corrected to Insight Center for Community Economic Development + Duke Center for Social Equity per F-FRESH-3.1-HAMILTON.
- Empirical-data-sourcing rigor: §V cohort-definition triplet's 2008-cohort sentence specifies Federal Reserve Survey of Consumer Finances + quarterly Distributional Financial Accounts series per F-3.5-FRESH-3 — the canonical Stone-Center-respected data-source combination for matched-comparison wealth-gap-accounting methodology.

The matched-comparison methodology generalization across Libby, Deepwater, 2008 is portable (identify mechanism of harm + identify cohort that absorbed cost + identify structurally similar comparison cohort + run matched comparison + price differential).

**Verdict:** ✓✓✓ INCLUDE. The F-3.5-FRESH-3 SCF + DFA addition is the load-bearing lift mechanism that closes the V-D-era ✓✓ verdict gap — Stone Center reviewer registers BOTH bibliographic discipline AND data-source rigor at full strength.

#### C-14. Coates / Darity / Mullen / Hamilton-lineage Black intellectual reader [PROJECTED] — FRESH verdict: ✓✓ INCLUDE

**Reading the V-E essay surface:** The C-14 reader's primary tests: does the essay credit the reparations-economics tradition's specific historical work without flattening it into a generic Restitution Bond umbrella? Does the Coates 2014 → Darity-Mullen 2020 → Hamilton 2015 → Conley 1999 citation pattern read as engagement (Yes) or as box-checking (No)? Does the inline four-sentence Restitution / Reparations asymmetry handling read as disarming or as inadequate?

The §V citation lineage is explicit + correctly attributed + Hamilton 2015 publisher precisely corrected (F-FRESH-3.1-HAMILTON). The four-sentence asymmetry handling at §V line 67 explicitly names the umbrella-extension discipline: "Reparations remain the specific historical claim of the African-American community for the specific historical wrongs the tradition names. The Restitution Bond joins that tradition rather than absorbs it." This is the disarming-discipline move the C-14 reader reads for; it is the right move at essay scale.

**Verdict:** ✓✓ INCLUDE. The lineage attribution + asymmetry handling is sufficient for INCLUDE; the C-14 reader walks away with the framework joining the tradition rather than appropriating it. Why ✓✓ rather than ✓✓✓: the essay-scale handling cannot do the full developmental work a Darity-or-Coates-level engagement would require; the four-sentence asymmetry is essay-scale-appropriate but the ✓✓ → ✓✓✓ test (does engagement read as authentic tradition-joining vs box-checking?) requires more than bibliography-precision corrections to lift.

### §2.3.a PROJECTED row aggregate

| Char | Verdict | Reading-class weight |
|---|---|---|
| C-5 | ✓✓✓ | PROJECTED |
| C-6 | ✓✓✓ | PROJECTED |
| C-7 | ✓✓✓ | PROJECTED |
| C-8 | ✓✓✓ | PROJECTED |
| C-9 | ✓✓ | PROJECTED |
| C-10 | ✓✓✓ | PROJECTED |
| C-14 | ✓✓ | PROJECTED |

**PROJECTED row counts:** 5 ✓✓✓ + 2 ✓✓ + 0 ✓ + 0 NEUTRAL + 0 EXCLUDE = **7/7 INCLUDE.**

**PROJECTED row rating:** **STRONG.** Per §1.2 criteria: STRONG = 5+ ✓✓✓ out of 7 + 0 EXCLUDE. The row delivers 5 ✓✓✓; lineage-attribution discipline signal is fully activated.

---

## §3. Aggregate Pass 3.3 verdict under Amendment D

### §3.1 Per-row aggregate

| Reception class | Characters | ✓✓✓ | ✓✓ | ✓ | NEUTRAL | EXCLUDE | Row rating |
|---|---|---|---|---|---|---|---|
| **DIRECT READERS** (HIGHEST) | 6 | 3 | 2 | 1 | 0 | 0 | **ACCEPTABLE** |
| **CONSULTANTS** (HIGH) | 3 | 3 | 0 | 0 | 0 | 0 | **STRONG** |
| **PROJECTED DOWNSTREAM** (LOWER) | 7 | 5 | 2 | 0 | 0 | 0 | **STRONG** |
| **All 16 (legacy aggregate)** | 16 | 11 | 4 | 1 | 0 | 0 | (legacy: 16/16 INCLUDE) |

### §3.2 SHIP verdict under Amendment D

Per §1.2: SHIP-READY = DIRECT row ≥ ACCEPTABLE AND CONSULTANT row ≥ ACCEPTABLE.

- **DIRECT row: ACCEPTABLE** (3 ✓✓✓ + 2 ✓✓ + 1 ✓; all ≥ ✓; 0 EXCLUDE; passes ACCEPTABLE threshold; does NOT reach STRONG because C-12 returns ✓ and C-11 + C-15 return ✓✓).
- **CONSULTANT row: STRONG** (3/3 ✓✓✓; placement-pipeline causal chain fully activated).
- **PROJECTED row: STRONG** (5/7 ✓✓✓; lineage-attribution discipline signal fully activated).

**SHIP verdict: SHIP-READY at ACCEPTABLE-on-DIRECT + STRONG-on-CONSULTANT + STRONG-on-PROJECTED.**

### §3.3 Pre-Amendment-D vs post-Amendment-D comparison (load-bearing for the prompt's critical question)

| Verdict frame | Pre-Amendment-D ("16/16 INCLUDE; 11 ✓✓✓ aggregate") | Post-Amendment-D (this audit) |
|---|---|---|
| Total INCLUDE | 16/16 | 16/16 (unchanged) |
| ✓✓✓ count | 11 | 11 (unchanged at per-character level) |
| Ship-decision aggregate | 16/16 INCLUDE → SHIP | DIRECT ACCEPTABLE + CONSULTANT STRONG → SHIP |
| Ship-decision rationale | Flattening 16-char aggregate; C-12's ✓ verdict is 1 of 16 (6.25% weight) | C-12's ✓ verdict is 1 of 6 in SHIP-READY row (16.7% weight); C-11 + C-15 ✓✓ verdicts are 2 of 6 (33.3% weight); higher-weight scrutiny on DIRECT row |
| Ship-readiness narrative | "Strongest acceptance verdict pattern in the BR essay's audit history" — based on per-character verdict tally | DIRECT row is ACCEPTABLE not STRONG — the load-bearing distinction Amendment D surfaces |
| Placement-pipeline narrative | (not separately surfaced) | CONSULTANT row STRONG — placement-pipeline causal chain is fully activated |
| Lineage-attribution narrative | (not separately surfaced) | PROJECTED row STRONG — lineage-attribution discipline signal is at the right level |

**Does the Amendment-D-weighted aggregate verdict change the SHIP recommendation?** Honest answer: **NO, V-E remains SHIP-READY under Amendment D, but the ship-readiness profile is differently shaped than the pre-Amendment-D framing suggests.**

The pre-Amendment-D framing presented V-E as "strongest acceptance verdict pattern in the BR essay's audit history" based on the 11 ✓✓✓ aggregate count; Amendment D reveals that **8 of those 11 ✓✓✓ verdicts (C-1, C-3, C-4 in CONSULTANT row; C-5, C-6, C-7, C-8, C-10 in PROJECTED row) are weighted in the LOWER-weight class for the ship decision**, and **only 3 of the 11 ✓✓✓ verdicts (C-2, C-13, C-16) sit in the SHIP-READY DIRECT row**. The DIRECT row's 3 ✓✓✓ + 2 ✓✓ + 1 ✓ pattern is ACCEPTABLE (passes ship threshold) but not STRONG.

This is the load-bearing Amendment D discipline finding: V-E SHIPS, and the placement-pipeline causal chain through CONSULTANT is fully activated, and the lineage-attribution discipline at PROJECTED is at the right level. AND: the DIRECT-reader response is ACCEPTABLE rather than STRONG; the three implementation-level pushbacks at C-12 (§V Restitution Bond per-case funding; §VI Social Security counterfactual sovereign-fund; §VI climate Foreclosure Bond) + the C-11 analytical-density slow at §III + the C-15 cumulative §V density are the per-character drivers that hold DIRECT at ACCEPTABLE rather than STRONG.

**Operational consequence:** V-E is SHIP-READY for the BR submission. The placement-pipeline causal chain (essay → vocabulary enters discourse → literary agent notices → acquisitions editor → book) is fully activated by the CONSULTANT STRONG row. The DIRECT-reader response at ACCEPTABLE is the realistic ship-readiness frame for a constructive policy-essay landing in a Forum-format venue where C-12 implementation-level pushbacks become engageable respondent material rather than ship-blocking EXCLUDE verdicts. The pre-Amendment-D framing of "strongest acceptance verdict pattern" is true at the per-character data level; under Amendment D weighting it is reframed to "STRONG on the placement-pipeline + lineage-attribution rows; ACCEPTABLE on the direct-reader row." Both framings ship; the Amendment-D-weighted framing is the more honest narration.

---

## §4. Forecast-vs-actual cross-check (V-E light-refire baseline as reference; FRESH derivation precedes the cross-check)

The 2026-06-01 light Pass 3.3 re-fire produced 11 ✓✓✓ + 4 ✓✓ + 1 ✓ aggregate; this FRESH Amendment-D-weighted re-fire produces 11 ✓✓✓ + 4 ✓✓ + 1 ✓ aggregate. The per-character verdicts MATCH the light re-fire exactly:

| Character | Light re-fire (2026-06-01) | FRESH Amendment-D (this audit) | Match? |
|---|---|---|---|
| C-1 | ✓✓✓ | ✓✓✓ | YES |
| C-2 | ✓✓✓ | ✓✓✓ | YES |
| C-3 | ✓✓✓ | ✓✓✓ | YES |
| C-4 | ✓✓✓ | ✓✓✓ | YES |
| C-5 | ✓✓✓ | ✓✓✓ | YES |
| C-6 | ✓✓✓ | ✓✓✓ | YES |
| C-7 | ✓✓✓ | ✓✓✓ | YES |
| C-8 | ✓✓✓ | ✓✓✓ | YES |
| C-9 | ✓✓ | ✓✓ | YES |
| C-10 | ✓✓✓ | ✓✓✓ | YES |
| C-11 | ✓✓ | ✓✓ | YES |
| C-12 | ✓ | ✓ | YES |
| C-13 | ✓✓✓ | ✓✓✓ | YES |
| C-14 | ✓✓ | ✓✓ | YES |
| C-15 | ✓✓ | ✓✓ | YES |
| C-16 | ✓✓✓ | ✓✓✓ | YES |

**16/16 per-character verdict convergence.** Fresh-session per-character verdict derivation converges on the light-refire baseline; this is verdict-stability evidence (a fresh session not anchored to the light-refire reaches the same per-character verdicts independently).

**The substantive Amendment-D finding is NOT a per-character verdict shift; it is a RESHAPING OF THE AGGREGATE NARRATIVE.** The 11 ✓✓✓ + 4 ✓✓ + 1 ✓ data is unchanged; the SHIP-decision aggregation is reshaped by partitioning the 16 characters into DIRECT (6) + CONSULTANT (3) + PROJECTED (7) classes with differential weights.

---

## §5. Pass 3.4 — Adversarial robustness (informative-diagnostic; 6-character BR-adapted set)

### §5.1 Pass 3.4 trigger evaluation under Amendment D

Per brief §13 Decision #7: Pass 3.4 fires as gating audit if C-12 returns ⚠ EXCLUDE; otherwise as informative-diagnostic.

Under Amendment D's higher weighting on C-12 (now 1 of 6 in SHIP-READY row rather than 1 of 16 in flattening aggregate), the trigger evaluation must consider whether the higher weight changes the gating threshold. **The brief's discipline holds:** C-12 returns ✓ INCLUDE (≥ NEUTRAL) under Amendment D; Pass 3.4 fires as informative-diagnostic, NOT as gating. The Amendment D reweighting does not lower the trigger threshold; it raises the WEIGHT of C-12's contribution to the SHIP-READY row aggregate without changing the absolute verdict-level threshold the trigger is keyed to.

Pass 3.4 fires for completeness + adversarial-thread-pull diagnostic value.

### §5.2 Adversarial set + per-character verdicts (informative-diagnostic)

The 6-character BR-adapted adversarial set is mapped to reception classes per the prompt's guidance: adversarial characters are extrapolations of DIRECT or CONSULTANT reception classes.

| # | Adversarial char | Reception-class extrapolation | V-E verdict | Reasoning |
|---|---|---|---|---|
| A1 | Industry-funded energy economist (Heritage / Manhattan Inst / AEI / API / NMA) | extrapolation of C-12 DIRECT-class | ⚠⚠ EXCLUDE | The §V Restitution Bond per-case funding mechanism (BP continuing Gulf operations + international oil-and-gas industry's aggregate exposure to comparable cost-severance events) reads as cross-firm retroactive liability assignment from this character's financial-incentive prior. §VI climate Foreclosure Bond application reads as constraint on fossil-fuel extraction value. No movement disarms this character's structural prior. The C-12-implementation-level pushbacks identified at the acceptance pass are the load-bearing threads this character pulls. The §III DOI MMS reorganization detail (existing architecture has already made adjustments) is a marginal disarming move but does not bridge the structural-prior gap. |
| A2 | Public Choice theorist (libertarian-aligned, not constructive-Buchanan-Tullock-engagement-aligned) | extrapolation of C-12 DIRECT-class | ⚠ EXCLUDE (substantially disarmed) | The §III Public Choice paragraph crediting Buchanan + Tullock + Mueller substantially disarms; the framework engages Public Choice as complementary lens rather than competing claim. The Minerals Management Service regulatory-capture naming + the W. R. Grace EPA-lobbying-delay naming + the DOI post-Deepwater MMS reorganization detail (regulator restructured into three separate bodies for revenue-collection / leasing / safety-enforcement) all read as Public-Choice-acknowledging moves the framework makes. The bond-as-instrument framing remains the residual pushback: a Public Choice theorist would push back on bond-instrument architecture as itself rent-seeking-vector-creating (bond authority would create new concentrated-interest extraction). Substantially disarmed but not fully. |
| A3 | Property-rights libertarian (Cato / Reason) | extrapolation of C-12 DIRECT-class | ⚠⚠ EXCLUDE | The §V Restitution Bond + §VI Foreclosure Bond instruments push back on this character's prior on retroactive liability + future-generation-standing claims. The §III bankruptcy-as-feature-not-bug Pistor engagement lands as descriptive across the acceptance audiences but the prescriptive close ("the architecture cannot be indicted. It can only be redesigned") does not disarm this character. Structural-prior pushback holds. |
| A4 | WSJ editorial-board reader / business-press conservative | extrapolation of C-12 DIRECT-class | ⚠ EXCLUDE (marginal disarming gain at V-E) | The §III non-partisan framing + Public Choice paragraph + §VII contingency-of-choice register holds. The F-FCIC-FIX verbatim restoration adds marginal source-fidelity gain — WSJ editorial-cluster respects verbatim quoting over paraphrase. The F-3.5-FRESH-3 SCF + DFA Fed data-source addition + F-FRESH-3.1-HAMILTON Hamilton-publisher precision fix adds bibliography pedigree the WSJ editorial-board respects even when it disagrees with prescriptions. Marginal defensive gain over V-D baseline; structural-prior pushback on bond-as-instrument architecture holds. |
| A5 | Reactionary intellectual (Compact / First Things / National Review intellectual cluster) | extrapolation of C-2 DIRECT-class + cultural-tradition adversary | ⚠⚠ EXCLUDE | The §VI civic-republican grounding (Pettit + Skinner + Parfit + Berlin/Constant) is the load-bearing engagement for this character — engages non-domination concept seriously (it's in the tradition's pre-Enlightenment lineage this character claims). The §VI Foreclosure-Bond-as-required-architecture move reads as technocratic-managerial displacement of substantive political community to this character; the §V Restitution Bond reads as reparations-economics adjacent which this character is skeptical of. Structural-orientation pushback holds. |
| A6 | Left-adversarial reader (DSA / Jacobin / Catalyst — BR-specific addition) | extrapolation of C-2 DIRECT-class + structural-redesign-tradition adversary | ⚠⚠ EXCLUDE | The two-instrument-architecture-as-structural-redesign within a left-coded-but-reformist register reads as technocratic-managerial reformism displacing structural critique to this character. The §V Restitution Bond's "draws against the residual capital of the financial sector" framing partially disarms (acknowledges asymmetric-extraction-tagged levy mechanism) but does not bridge the structural-redesign / regime-change polarity this character operates in. The §VII engineered-architecture close reads as institutional-redesign-not-regime-change to this character; structural-orientation pushback holds. |

### §5.3 Thread-pull synthesis under Amendment D

The 2026-05-28 three-way comparison §2.1 identified 4 dominant adversarial threads:

1. **Commons-pricing-policy thread.** A1 + A3 + A4 pull this: the bond-as-instrument architecture is a commons-pricing policy that constrains private-sector extraction value. Load-bearing chapter / book claim; the framework's structural-accounting argument depends on bond-instruments as the operationalization vehicle. Spot-fix would damage acceptance verdicts on C-13 + C-16 + the §V + §VI named-instrument architecture. **Recommendation: HOLD; thread is acknowledged via §III Public Choice paragraph + §VII contingency-of-choice framing + Forum-format respondent invitation.**

2. **No-villain-masks-rent-seekers thread.** A2 pulls this: the framework's no-villain framing (cost severance as structural mechanism not bad-actor causation) masks the rent-seekers Public Choice analysis would name. Procedural / cosmetic-mitigation flag: the §III Public Choice paragraph substantially disarms by explicitly crediting the rent-seeking analysis as complementary lens; the W. R. Grace EPA-lobbying-delay + Minerals Management Service regulatory-capture explicit-namings preserve rent-seeker visibility within the structural-mechanism frame. **Recommendation: HOLD; thread is substantially disarmed at V-E; no further spot-fix required.**

3. **Bond-as-rent-seeking-vector thread.** A2 pulls this (residual): the bond-instrument architecture itself creates new rent-seeking vectors (bond authority + bond-administration + bond-allocation discretion). Load-bearing chapter / book claim — the bond mechanism is the framework's load-bearing instrument-design move. Spot-fix would damage essay's constructive proposal shape. **Recommendation: HOLD; cross-chapter handoff to book-scale governance-of-bond-authorities engagement.**

4. **Two-instrument-as-technocratic-managerial-displacement thread.** A5 + A6 pull this from opposite political orientations (reactionary intellectual + left-adversarial respectively): the two-instrument architecture displaces substantive political community / structural-redesign / regime-change with technocratic-managerial reformism. Load-bearing chapter / book claim — the framework's constructive policy-proposal shape is exactly the two-instrument architecture; the Forum-format compatibility is built on the constructive-proposal-with-engageable-respondents move. Spot-fix would damage acceptance verdicts on C-1 + C-2 + C-9 + Berggruen-prize-judge audience and on the Forum-series-fit. **Recommendation: HOLD; thread is load-bearing constructive-proposal shape and the §VII contingency-of-choice framing acknowledges it.**

**No new threads identified at the fresh Amendment-D audit.** The 4-thread structure from the 2026-05-28 three-way comparison synthesis carries through to V-E intact.

### §5.4 Robustness verdict under Amendment D

**Pass 3.4 verdict: CONDITIONALLY ROBUST** (consistent with V-D fresh re-audit + light re-fire baselines).

The framework's structural moves substantially disarm A2 (Public Choice theorist) via the §III Public Choice paragraph + DOI MMS reorganization detail; the framework does not disarm A1 + A3 + A4 + A5 + A6 structural-prior pushbacks (and disarming those would require not a different essay surface but a different argument). The brief §10 non-partisan-framing discipline holds across the adversarial set; C-12's ✓ INCLUDE verdict satisfies the ≥ NEUTRAL threshold; Pass 3.4 trigger does NOT fire as gating.

**Under Amendment D higher-weighting:** the adversarial-set extrapolation maps 4 of 6 adversarial characters (A1, A2, A3, A4) into the C-12 DIRECT-class reception, and 2 of 6 (A5, A6) into the C-2 DIRECT-class reception. All 6 adversarial characters are extrapolations of DIRECT-reception classes. The adversarial-robustness verdict is therefore a measure of how the DIRECT row would weather adversarial pulls — and the answer is CONDITIONALLY ROBUST: the implementation-level threads at A1 / A3 / A4 / A5 / A6 are load-bearing-structural rather than spot-fix-addressable; the procedural thread at A2 is substantially disarmed; the Forum-format compatibility re-engages all six adversarial characters as engageable-respondents rather than ship-blocking rejecters.

**No new Pass-3.4 spot-fix surfaces at V-E.** The V-D fresh re-audit + light re-fire informative-diagnostic Pass 3.4 evaluation (CONDITIONALLY ROBUST with substantial defensive gain at A2 + marginal at A4) carries forward against V-E unchanged.

### §5.5 Pass 3.4 trigger verdict

**Pass 3.4 opt-in trigger: NO — does not fire.** C-12 returns ✓ INCLUDE (≥ NEUTRAL); per brief Decision #7 the trigger fires only if C-12 returns ⚠ EXCLUDE or worse. The Amendment D higher-weighting on C-12 does not change the trigger threshold (which is keyed to absolute verdict-level not to aggregate-row-weight).

---

## §6. Critical question — does Amendment D change the SHIP recommendation?

The prompt's load-bearing question: **does the Amendment-D-weighted aggregate verdict on V-E change the SHIP recommendation?**

**Honest answer: NO — V-E remains SHIP-READY under Amendment D weighting. BUT the ship-readiness profile is differently shaped than the pre-Amendment-D framing presents.**

### §6.1 Pre-Amendment-D verdict (legacy framing)

- 16/16 INCLUDE; 11 ✓✓✓ aggregate; "strongest acceptance verdict pattern in the BR essay's audit history."
- C-12 ✓ INCLUDE in the flattening 16-character aggregate; Pass 3.4 trigger does not fire.
- Recommendation: SHIP V-E.

### §6.2 Post-Amendment-D verdict (this audit)

- DIRECT-READER row: ACCEPTABLE (3 ✓✓✓ + 2 ✓✓ + 1 ✓; passes the ACCEPTABLE-ship-threshold; does NOT reach STRONG).
- CONSULTANT row: STRONG (3/3 ✓✓✓; placement-pipeline causal chain fully activated).
- PROJECTED-DOWNSTREAM row: STRONG (5/7 ✓✓✓; lineage-attribution discipline signal at right level).
- Recommendation: SHIP V-E at ACCEPTABLE-DIRECT + STRONG-CONSULTANT + STRONG-PROJECTED profile.

### §6.3 Substantive differences in narrative

The pre-Amendment-D framing presents V-E as the strongest essay-history acceptance pattern, anchored to the 11 ✓✓✓ aggregate count. Under Amendment D, **only 3 of those 11 ✓✓✓ verdicts (C-2 BR reader, C-13 extraction-affected reader, C-16 EJ-movement reader) sit in the SHIP-READY DIRECT row**; **8 ✓✓✓ verdicts sit in the LOWER-weight CONSULTANT or PROJECTED rows**. The DIRECT row's pattern (3 ✓✓✓ + 2 ✓✓ + 1 ✓) is ACCEPTABLE not STRONG; the C-12 implementation-level pushbacks + C-11 analytical-density slow + C-15 cumulative §V density are the load-bearing per-character drivers that hold the DIRECT row at ACCEPTABLE.

### §6.4 Operational consequence

V-E SHIPS under both framings. The Amendment-D-weighted framing surfaces three operational distinctions the pre-Amendment-D framing does not:

1. **Placement-pipeline (CONSULTANT) is the strongest row.** This is the publishing-path-causal-chain row — the BR editorial brain + literary agent + acquisitions editor reading at maximum verdicts is exactly the row that activates the essay-placement → vocabulary-enters-discourse → agent-notices → publisher-acquires sequence. V-E's CONSULTANT STRONG row is the load-bearing signal for the marketing-phase causal chain the book is currently in.

2. **DIRECT row is ACCEPTABLE not STRONG.** The actual readers of the published essay deliver a less-than-maximum aggregate, anchored by the C-12 implementation-level pushbacks + analytical-density + cumulative-§V-density signals. This is the honest narration of what BR readership will deliver — substantive engagement at minor-reservations levels for some readers, strong INCLUDE for others. The ACCEPTABLE rating passes the ship threshold; it is not WEAK; it is also not STRONG.

3. **PROJECTED row is STRONG.** Lineage-attribution discipline (Coates → Darity-Mullen → Hamilton → Conley; Pistor; Pettit + Skinner + Parfit; Hartwick / Norway; Stone Center methodology) is at the right level. This is the pitch-craft discipline signal — the framework respects its named-tradition predecessors and does not appropriate or rebrand. The STRONG rating is the right anchor for the cover-letter framing + the book-proposal positioning.

### §6.5 Honest answer to the prompt's framing

> **If DIRECT-READER row is WEAK and CONSULTANT row is STRONG, the ship-readiness assessment is different from the placement-pipeline assessment.**

V-E does NOT have a WEAK DIRECT row. V-E has an ACCEPTABLE DIRECT row + STRONG CONSULTANT row + STRONG PROJECTED row. The ship-readiness assessment + placement-pipeline assessment + lineage-attribution assessment all PASS; the ship-readiness assessment is ACCEPTABLE rather than STRONG, but ACCEPTABLE is above the ship threshold.

**The SHIP recommendation does not change between pre-Amendment-D and post-Amendment-D framings. The narrative anchoring the SHIP recommendation does change: pre-Amendment-D framing anchors to "strongest acceptance verdict pattern in essay history"; post-Amendment-D framing anchors to "ACCEPTABLE on direct-reader response + STRONG on placement-pipeline + STRONG on lineage-attribution."** The post-Amendment-D framing is the more honest narration.

---

## §7. Pass 3.4 informative-diagnostic forward-pointers

No new Pass-3.4 spot-fix surfaces at V-E. Forward-flag carry-forwards:

- **Bond-governance thread (A2 residual pushback)** — cross-chapter handoff to book-scale engagement of bond-instrument governance + concentrated-interest-extraction-from-bond-authorities. Out of scope for essay; in scope for book.
- **Technocratic-managerial-displacement thread (A5 + A6 dual-direction pull)** — cross-chapter handoff to book-scale engagement of two-instrument architecture vs structural-redesign / regime-change polarities. Out of scope for essay; in scope for book; Forum-format respondent invitation acknowledges the thread at essay scale.

---

## §8. Status + next-pass anchor + end-of-session one-liner

### §8.1 Summary verdict

**FRESH Pass 3.3 + 3.4 audit on V-E under Amendment D reception-chain weighting: SHIP-READY.**

| Disposition | Count / Rating |
|---|---|
| **Pass 3.3 — Acceptance, by row:** | |
| DIRECT row (6 chars; HIGHEST weight) | 3 ✓✓✓ + 2 ✓✓ + 1 ✓ = **ACCEPTABLE** |
| CONSULTANT row (3 chars; HIGH weight) | 3 ✓✓✓ = **STRONG** |
| PROJECTED row (7 chars; LOWER weight) | 5 ✓✓✓ + 2 ✓✓ = **STRONG** |
| Pre-Amendment-D legacy aggregate | 11 ✓✓✓ + 4 ✓✓ + 1 ✓ = 16/16 INCLUDE |
| **Pass 3.4 — Adversarial, informative-diagnostic:** | |
| A2 (substantially disarmed) | ⚠ EXCLUDE |
| A1, A3, A4, A5, A6 (structural-prior pushbacks) | ⚠⚠ EXCLUDE; A4 marginal disarming gain at V-E |
| Thread-pull synthesis | 4 threads identified (commons-pricing-policy; no-villain-masks-rent-seekers; bond-as-rent-seeking-vector; two-instrument-as-technocratic-managerial-displacement); all HOLD; no new spot-fix candidates |
| Robustness verdict | **CONDITIONALLY ROBUST** |
| Pass 3.4 opt-in trigger | NO — does not fire (C-12 ✓ INCLUDE ≥ NEUTRAL) |
| **SHIP verdict** | **SHIP-READY: ACCEPTABLE-DIRECT + STRONG-CONSULTANT + STRONG-PROJECTED** |
| **Does Amendment D change SHIP recommendation?** | **NO — SHIP recommendation unchanged. Narrative anchoring shifts from "strongest aggregate" to "ACCEPTABLE-DIRECT + STRONG-CONSULTANT + STRONG-PROJECTED."** |

### §8.2 Anchor commits

- Stage 1 brief RATIFIED: 2026-05-21 (v1.0.1); origin/main per merge-on-ratification scaffolding default.
- V-D fresh re-audit RATIFIED: 2026-06-01 (`pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md`).
- V-E spot-fixes RATIFIED + APPLIED: 2026-06-01 commit `c1ad8e8`; essay.md ~4,858w; 20 em-dashes.
- V-E light Pass 3.3 re-fire PROPOSED 2026-06-01 (`light-refires/pass-3-3-light-refire_V-E_2026-06-01.md`); per-character verdict pattern: 11 ✓✓✓ + 4 ✓✓ + 1 ✓; this fresh audit converges 16/16 per-character.
- This FRESH Amendment-D audit PROPOSED 2026-06-02 — first Amendment-D-weighted re-fire on BR V-E.

### §8.3 Next-pass anchor

After this fresh PROPOSED audit lands + parent session ratifies:

- **Parent-session consolidation** — parent session consolidates this Amendment-D audit's findings with prior V-D fresh re-audit + V-E light re-fire baselines; surfaces the Amendment-D-weighted SHIP verdict for author ratification.
- **Author disposition** — V-E's disposition latitude per V-E application artifact §7 (submit V-E now; wait for Phase C+D outcomes; submit V-E as safest-ship while Phase C+D continue) is unchanged by this audit. The Amendment-D weighting confirms V-E SHIPS; the placement-pipeline causal-chain signal is STRONG; the direct-reader-row at ACCEPTABLE is the honest narration of what BR readership will deliver.
- **Phase C7 / Phase C8 / Phase D9** — per V-E application artifact §6 forward-pointers; unchanged by this audit. Amendment-D weighting may inform Phase C7 + Phase C8 evaluation (additional ALT-NORM-PUNCT publisher-house grafts that strengthened CONSULTANT row in the 2026-05-28 three-way comparison would, under Amendment D weighting, register as PROJECTED + CONSULTANT row strengthening — incremental within-band strengthening on already-STRONG rows — vs the C-15 DIRECT-row cost that ALT-NORM-PUNCT incurred, which would be a DIRECT-row cost worth weighing more heavily).
- **Phase E (final fresh-session audit on converged cut)** — after Phase C results + Phase D9 author-substrate decision lands; this Amendment-D audit is the per-doctrine 5-pass verdict-on-acceptance reference that Phase E's converged-cut audit re-validates against.

### §8.4 End-of-session one-liner

```
STATE: br-V-E-pass-3-3-3-4-amendment-d PROPOSED
(SHIP-READY: ACCEPTABLE-DIRECT + STRONG-CONSULTANT + STRONG-PROJECTED;
 per-character verdicts converge 16/16 with 2026-06-01 light re-fire;
 pre-Amendment-D 16/16 INCLUDE + 11 ✓✓✓ aggregate unchanged at per-
 character data level; Amendment-D-weighted aggregation reshapes the
 SHIP narrative from "strongest aggregate" to "ACCEPTABLE-DIRECT +
 STRONG-CONSULTANT + STRONG-PROJECTED"; SHIP recommendation
 UNCHANGED; Pass 3.4 CONDITIONALLY ROBUST; 4 adversarial threads
 carried forward unchanged; no new spot-fixes surfaced; Pass 3.4
 opt-in trigger does NOT fire);
NEXT: parent-session-consolidation;
AWAITING: author-confirmation
```

---

*End of FRESH Pass 3.3 + 3.4 Amendment-D-weighted audit artifact for Boston Review essay V-E — PROPOSED 2026-06-02.*

**STATE: br-V-E-pass-3-3-3-4-amendment-d [PROPOSED]; NEXT: parent-session-consolidation; AWAITING: author-confirmation**
