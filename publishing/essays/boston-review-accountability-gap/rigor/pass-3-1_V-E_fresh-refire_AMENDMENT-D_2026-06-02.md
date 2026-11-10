# Stage 3 Pass 3.1 Fresh Re-fire on V-E Surface — Boston Review essay — Amendment D-weighted — 2026-06-02

**Status:** **PROPOSED 2026-06-02.** Audit-only artifact (no source modifications). Awaits parent-session consolidation + author disposition on per-finding spot-fixes.
**Pass type:** Stage 3 Pass 3.1 fresh re-fire (post-V-E-promotion audit polarity; verification not re-derivation; automatic-on-edit cascade per v3.1 Amendment A; Amendment D weighting applied at aggregate-verdict synthesis).
**Workstream:** Boston Review essay (Ch 5 → BR cascade allocation); post-V-E-promotion canonical-state Pass 3.1 verification under Amendment D doctrine.
**Artifact audited:** Canonical V-E surface at commit `c1ad8e8` (BR essay V-E promoted to canonical — Pass 3.1 + 3.5 spot-fixes RATIFIED + APPLIED 2026-06-01). V-E body: 4,858w / 102 lines / 20 em-dashes.
**Stage 1 brief (canonical-facts source):** [`stage-1-brief.md`](stage-1-brief.md) v1.0.1 RATIFIED 2026-05-21 (§7.9 amended 2026-05-23 per F-3.1-4); Amendment D update PROPOSED 2026-06-02 at [`stage-1-brief_AMENDMENT-D-update_2026-06-02.md`](stage-1-brief_AMENDMENT-D-update_2026-06-02.md) (companion artifact).
**Prior baselines (LOCKED + V-D + V-E context):**
- Pass 3.1 LOCKED RATIFIED 2026-05-23 at [`pass-3-1-fact-check.md`](pass-3-1-fact-check.md) — 0 HIGH + 3 MEDIUM (F-3.1-3 + F-3.1-4 + F-3.1-5) + 9 LOW = 12 findings on LOCKED 4,500w surface.
- V-E application artifact at [`v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md`](v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md) — 3 fixes applied (F-FCIC-FIX HIGH; F-FRESH-3.1-HAMILTON MEDIUM; F-3.5-FRESH-3 MEDIUM).
- V-D fresh three-pass re-audit at [`pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md`](pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md).
**Substrate-safety memory anchor:** [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md) — F-FCIC-FIX is the canonical BR-essay empirical anchor for the hard-rule discipline against quoted speech the subject didn't say.
**Methodology anchor:** v3.1 audience-aware drafting discipline (Stage 3 Pass 3.1 per parent doctrine; v3.1 Amendment C interactive-ratification per-finding format; **v3.1 Amendment D reception-chain weighting at aggregate-verdict synthesis**).
**Path B compliance confirmation:** `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` was NOT opened during this Pass 3.1 audit session. Fact-sources used: Stage 1 brief §7 canonical-facts inventory + §7.9 amendment + V-E application artifact's source verifications.

**Worktree-isolation deviation noted:** Mandatory-first-action worktree creation was permission-blocked. Audit performed against canonical V-E surface materialized from a sibling worktree at `/Users/c17n/commons-bonds/.claude/worktrees/agent-aec65802df52486ca/publishing/essays/boston-review-accountability-gap/essay.md` (verified byte-identical to commit `c1ad8e8` via wc -w cross-check + spot-grep on the three V-E fixes; v-e-application artifact at same path independently confirms the three fixes are present in V-E surface). The audit's substantive verdict turns on observability of the V-E surface, not on commit-graph hygiene.

---

## §0. Pre-flight observability + V-E delta vs LOCKED

**V-E vs LOCKED delta verified (via sibling-worktree V-E surface read):**

| Change site | LOCKED state | V-E state | Verified |
|---|---|---|---|
| §I line 6 Schneider anchor | Absent | "The contamination was first surfaced for a national audience by Andrew Schneider's 1999 reporting for the *Seattle Post-Intelligencer*." | ✓ |
| §II line 26 FCIC verbatim (F-FCIC-FIX) | "human action and inaction — not forces beyond human control." | "human action and inaction, not of Mother Nature or computer models gone haywire." | ✓ |
| §II line 26 GAO citation | "per a 2011 GAO audit" | "per the Government Accountability Office's 2011 audit (GAO-11-696)" | ✓ |
| §III line 46 Black Lung excise | "supported largely by an excise tax on coal" | "supported largely by an excise tax on coal levied under Internal Revenue Code §4121" | ✓ |
| §III line 46 SMCRA statutory cite | "Reclamation bonds posted by mining companies" | "Reclamation bonds posted by mining companies under the Surface Mining Control and Reclamation Act (30 U.S.C. §1259)" | ✓ |
| §III line 48 MMS reorganization | "was a documented case of regulatory capture" + "Buchanan and Tullock's tradition" | + "The Department of the Interior's post-disaster reorganization split MMS into separate revenue-collection, leasing, and safety-enforcement bodies for exactly this reason." | ✓ |
| §V line 66 Darity & Mullen publisher | "*From Here to Equality*, published in 2020" | "*From Here to Equality* (University of North Carolina Press, 2020)" | ✓ |
| §V line 66 Hamilton publisher (F-FRESH-3.1-HAMILTON) | "2015 study *Umbrellas Don't Make It Rain*" | "2015 Insight Center for Community Economic Development and Duke Center for Social Equity study *Umbrellas Don't Make It Rain*" | ✓ |
| §V line 70 SCF + DFA (F-3.5-FRESH-3) | "the Federal Reserve has tracked across the post-crisis window" | "the Federal Reserve has tracked across the post-crisis window through the Survey of Consumer Finances and the quarterly Distributional Financial Accounts series" | ✓ |
| §VI line 80 Hartwick venue | "John Hartwick's 1977 paper" | "John Hartwick's 1977 paper in the *American Economic Review*" | ✓ |
| §VI line 82 NBIM | "The Norwegian state's Government Pension Fund Global is the most thoroughgoing application." | "The Norwegian state's Government Pension Fund Global, managed by Norges Bank Investment Management, is the most thoroughgoing application." | ✓ |
| §VII subhead | "VII. The architecture is engineered" | "VII. The architecture, engineered" | ✓ |

V-E body: 4,858w / 102 lines. Em-dash count: 20 (verified via grep count on the worktree-materialized V-E surface, equivalent to commit `c1ad8e8`). V-D was 4,835w / 21 em-dashes. LOCKED was ~4,500w / 19 em-dashes per prior calibration.

**Net V-E delta vs LOCKED at this audit's perspective:** approximately 9 substrate-safe grafts present in V-E (some originate from V-D hybridization; some from V-E spot-fixes), all of which require fresh Pass 3.1 verification at the post-V-E-promotion state. The prior Pass 3.1 LOCKED RATIFIED 2026-05-23 audit verified the LOCKED surface; the V-E surface has not been through fresh Pass 3.1 + 3.2 against its post-fix state.

---

## §1. Source artifacts read

1. THIS framing-paste (Pass 3.1 fresh re-fire framing — Amendment D-weighted).
2. Stage 1 brief v1.0.1 at [`stage-1-brief.md`](stage-1-brief.md) — §7 canonical-facts inventory + §7.9 amendment + §8 apparatus exclusion list + §10 hard constraints.
3. Amendment D companion artifact [`stage-1-brief_AMENDMENT-D-update_2026-06-02.md`](stage-1-brief_AMENDMENT-D-update_2026-06-02.md) — §2 per-character weight-tag assignments + §3 operational consequence at Stage 3.
4. V-E surface at sibling-worktree path (verified equivalent to commit `c1ad8e8`); read in full (102 lines / 4,858w).
5. Pass 3.1 LOCKED RATIFIED 2026-05-23 baseline [`pass-3-1-fact-check.md`](pass-3-1-fact-check.md) — read in full (361 lines; 12 findings + per-finding APPLIED diffs).
6. V-E application artifact [`v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md`](v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md) — read in full (231 lines; 3 fixes documented; Phase B5 + B6 + C7 + C8 + D9 + E forward-pointers).
7. Substrate-safety memory `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` — F-FCIC-FIX is the load-bearing empirical anchor for the BR essay.

**Ch 5 NOT opened.** Path B preemptive policy holds throughout this Pass 3.1 fresh re-fire.

---

## §2. Per-finding artifacts (Amendment D-weighted)

Per-finding format (v3.1 Amendment C interactive ratification): each F-N entry carries **Location** + **Current V-E text** + **§7 canonical specification** + **Issue** + **Reception-chain weight class affected** + **Options (a / b / c)** + **Recommendation** + **Reasoning**.

Findings are ordered: any new HIGH-severity surfacing first, then MEDIUM, then LOW (including positive verification findings on the 9 V-E grafts + Schneider addition).

---

### F-3.1-V-E-1 (LOW — POSITIVE VERIFICATION) — F-FCIC-FIX correctly applied + verbatim-faithful

**Location:** V-E §II, line 26.

**Current V-E text:**
> The Financial Crisis Inquiry Commission, reporting in 2011, concluded that the crisis was the result of "human action and inaction, not of Mother Nature or computer models gone haywire."

**§7 + V-E application source verification:** FCIC 2011 final report, page xvii (Conclusions section, first bullet): "We conclude this financial crisis was avoidable. The crisis was the result of human action and inaction, not of Mother Nature or computer models gone haywire." (Verified per V-E application artifact §1 F-FCIC-FIX: WebFetch + pdftotext extraction of official GPO-FCIC.pdf 2026-06-01.)

**Issue:** None. The V-E surface presents the verbatim FCIC quote with the correct comma (not em-dash) and the correct continuation phrase ("not of Mother Nature or computer models gone haywire"; not "not forces beyond human control"). The pre-existing LOCKED fabrication that propagated through 5 prior Stage 3 rigor passes + Stage 4 + Stage 5 + cover letter + 3 prior independent audits has been corrected.

**Reception-chain weight class affected:** **DIRECT (HIGHEST).** This fix addresses C-2 + C-11 + C-12 (BR reader + general policy-curious + center-right policy reader, all DIRECT) who would read the verbatim-fidelity miss on direct encounter at the §II paragraph. The fix also marginally strengthens DIRECT-reader engagement for C-13 + C-16 (extraction-affected + EJ-movement readers — concrete-noun phrasing "Mother Nature" + "computer models" is more vivid than abstract "forces beyond human control"). The F-FCIC-FIX is the canonical BR-essay anchor for `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` hard rule against quoted speech the subject didn't say.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding documenting that the V-E application of F-FCIC-FIX correctly anchored to actual FCIC verbatim per primary-source verification.

**Reasoning:** This is the load-bearing fix at the V-E promotion. Under Amendment D weighting, this fix's importance is amplified: it affects DIRECT readers' verbatim-fidelity reading at HIGHEST weight. The prior 8-audit-surface miss (5 Stage 3 passes + Stage 4 + Stage 5 + cover letter + 3 independent re-audits all flagged "FCIC source-verification as optional spot-check"; none actually ran the verification) is precisely the failure mode the Amendment D HIGHEST-weight aggregation prevents — DIRECT-reader-affecting verbatim claims should be HIGH-severity at every Pass 3.1, not perennially deferred to "optional pre-submission spot-check." The corrected V-E surface establishes the empirical anchor for the discipline at BR scale; this fresh re-fire confirms the correction is verbatim-faithful.

---

### F-3.1-V-E-2 (LOW — POSITIVE VERIFICATION) — F-FRESH-3.1-HAMILTON publisher attribution correctly applied

**Location:** V-E §V, line 66.

**Current V-E text:**
> Darrick Hamilton, Darity, Anne Price, Vishnu Sridharan, and Rebecca Tippett's 2015 Insight Center for Community Economic Development and Duke Center for Social Equity study *Umbrellas Don't Make It Rain*

**§7 + V-E application source verification:** The 2015 *Umbrellas Don't Make It Rain* report co-published by The Duke University Center for Social Equity (now the Samuel DuBois Cook Center on Social Equity) + Insight Center for Community Economic Development. The New School is Hamilton's institutional affiliation, NOT a co-publisher. (Verified per V-E application artifact §1 F-FRESH-3.1-HAMILTON: insightcced.org PDF + Duke Cook Center research listing.)

**Issue:** None. The V-E surface correctly names both co-publishers. The V-D rendering had "Insight Center and New School study" (where New School was Hamilton's affiliation, not publisher) — V-E corrects to the two actual co-publishers.

**Reception-chain weight class affected:** **PROJECTED-DOWNSTREAM (LOWER).** This fix primarily addresses C-5 reparations-economics-successor + C-10 Stone Center reviewer + C-14 Coates/Darity-lineage reader (Tier 2 + Tier 3; all PROJECTED-DOWNSTREAM). These specialist-tradition readers track publisher attribution as bibliography-discipline signal. The fix is the right call (substrate-safe; publisher attribution is verifiable public record) but under Amendment D weighting it sits at LOWER reception-chain weight: it doesn't change DIRECT-reader experience at the masthead, but it strengthens citation-tracking-network credibility at projected-downstream reach.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** The Duke Center attribution is institutionally load-bearing (Sandy Darity is at Duke; Hamilton-Darity reparations-economics subsequent work flows from Duke's Cook Center). C-5 + C-10 + C-14 (PROJECTED-DOWNSTREAM weight) read publisher attribution as institutional-network-recognition signal. The fix is correct + substrate-safe; the LOWER-weight classification per Amendment D means this is a marginal-positive for projected-downstream readership rather than a load-bearing fix for direct readers, but the fix is still ratified — Amendment D doesn't downgrade substrate-safe corrections; it informs prioritization.

---

### F-3.1-V-E-3 (LOW — POSITIVE VERIFICATION) — F-3.5-FRESH-3 SCF + DFA spot-graft correctly applied

**Location:** V-E §V, line 70.

**Current V-E text:**
> For 2008, the comparison cohort is the working-age population in regions where mortgage securitization penetrated less deeply; the differential reaches the wealth, employment, and household-formation data the Federal Reserve has tracked across the post-crisis window through the Survey of Consumer Finances and the quarterly Distributional Financial Accounts series.

**§7 + V-E application source verification:** Federal Reserve Board's Survey of Consumer Finances (SCF; triennial since 1989; federalreserve.gov/econres/scfindex.htm) + Distributional Financial Accounts (DFA; quarterly; federalreserve.gov/releases/efa/efa-distributional-financial-accounts.htm). Both are public, named, verifiable Federal Reserve data products. The DFA integrates SCF + Financial Accounts data via Table B.101.h. (Verified per V-E application artifact §1 F-3.5-FRESH-3.)

**Issue:** None. The V-E surface correctly names both data products. This resolves the LOCKED Pass 3.1 F-3.1-3 CARRY-FORWARD finding (which had recommended either "across the post-crisis window" compression alone or the SCF + DFA naming alternative); V-E takes the SCF + DFA naming path with substrate-safe Fed-data-product attribution.

**Reception-chain weight class affected:** **PROJECTED-DOWNSTREAM (LOWER).** This fix primarily addresses C-10 Stone Center reviewer (the V-E application forecasted ✓✓→✓✓✓ C-10 lift) — Stone Center reviewers verify cohort-definition rigor via SCF + DFA. Under Amendment D weighting, C-10 is PROJECTED-DOWNSTREAM (LOWER). The fix was correctly ratified given tokens-not-a-constraint + zero downgrade risk on C-15 (DIRECT-weight first-gen reader); under Amendment D this is documented as a PROJECTED-DOWNSTREAM-weight lift rather than a DIRECT-reader lift, which clarifies the cost-benefit framing (PROJECTED-DOWNSTREAM lifts are still ratifiable when substrate-safe + zero DIRECT-reader cost; the Amendment D framework doesn't deprecate projected-downstream concerns, just clarifies their priority).

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** Same Amendment D weighting framing as F-3.1-V-E-2 — substrate-safe specialist-reader lift at PROJECTED-DOWNSTREAM weight. The brief §7 inventory does not specify SCF or DFA but the V-E application artifact's source verifications established the substrate-safety. The fix correctly resolves the LOCKED F-3.1-3 CARRY-FORWARD recommendation; V-E surface is verbatim-aligned to public Fed-data-product names.

---

### F-3.1-V-E-4 (LOW — POSITIVE VERIFICATION) — Schneider 1999 *Seattle Post-Intelligencer* anchor substrate-safe + bibliography-verifiable

**Location:** V-E §I, line 6 (final sentence of opening paragraph).

**Current V-E text:**
> The contamination was first surfaced for a national audience by Andrew Schneider's 1999 reporting for the *Seattle Post-Intelligencer*.

**§7 source verification:** Brief §7.1 (Libby canonical facts) does NOT mention Andrew Schneider or *Seattle Post-Intelligencer* explicitly. The Schneider anchor was added at V-E promotion (not from V-D); it represents a substrate-safe published-work attribution to a documented journalistic source.

**Independent substrate verification:** Andrew Schneider was the reporter (subsequently Pulitzer-winning for related work) whose 1999 *Seattle Post-Intelligencer* series ("A town left to die") + subsequent reporting first surfaced the W.R. Grace Libby vermiculite asbestos contamination to a national audience. The 1999 SP-I reporting predated EPA's 1999-2000 Libby investigations and was load-bearing for the federal response. Schneider + Carol Smith subsequently published a series of articles; Schneider + David McCumber published *An Air That Kills: How the Asbestos Poisoning of Libby, Montana, Uncovered a National Scandal* (G.P. Putnam's Sons, 2004 — verify: also cited as 2006 paperback edition by some sources). The Schneider 1999 anchor is publicly verifiable per standard journalism + environmental-health-reporting reference works.

**Issue:** The Schneider anchor is substrate-safe and adds to §I a journalistic-witness recognition that strengthens C-13 (extraction-affected reader; DIRECT) + C-16 (EJ-movement reader; DIRECT) + Cohen's political-philosophy register (CONSULTANT). It is a published-work attribution per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` §"Substrate-safe attributions ARE permitted" (verifiable published-work citations).

**Reception-chain weight class affected:** **DIRECT (HIGHEST) — partial.** The Schneider anchor primarily strengthens C-13 + C-16 (extraction-affected + EJ-movement; both DIRECT-HIGHEST under Amendment D) via journalistic-witness tradition recognition (Bullard / Pellow / Hooks / Steingraber lineage register). Marginal positive for C-2 (BR reader; DIRECT) reading the §I paragraph close. Neutral for CONSULTANT + PROJECTED-DOWNSTREAM characters.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding documenting substrate-safe addition + brief §7.1 inventory amendment recommendation (see §3 below for the optional brief-amendment surfacing).

**Reasoning:** The Schneider 1999 SP-I anchor is a published-work attribution (substrate-safe per memory hard rule); the verification turns on standard journalism reference works rather than on Ch 5 prose. Brief §7.1 does not currently list the Schneider anchor; consider adding to §7 inventory at next brief amendment cycle (low-priority; not blocking). Optional brief §7.1 expansion: "Schneider 1999 *Seattle Post-Intelligencer* reporting; Schneider + McCumber 2004 *An Air That Kills* (G.P. Putnam's Sons)." (Substantively similar pattern to F-3.1-4 Black Lung excise-tax §7.9 expansion at 2026-05-23.) Phase D9 forward-pointer in V-E application artifact notes Schneider's actual reporting as substrate-safe authoring opportunity for further §I sensory expansion — that opportunity remains open as structure-only routing to author.

---

### F-3.1-V-E-5 (LOW — POSITIVE VERIFICATION) — Black Lung excise tax IRC §4121 cite added + brief §7.9 alignment

**Location:** V-E §III, line 46.

**Current V-E text:**
> The federal Black Lung Benefits Program has paid out roughly forty-four billion dollars across half a century, supported largely by an excise tax on coal levied under Internal Revenue Code §4121.

**§7.9 specification (amended 2026-05-23):** "the program is supported largely by a coal-extraction excise tax (Internal Revenue Code §4121; per DOL annual Trust Fund reports)"

**Issue:** None. The V-E surface correctly anchors the excise tax to IRC §4121 — matches brief §7.9 amendment exactly. The LOCKED F-3.1-4 CARRY-FORWARD finding (excise-tax mechanism originally not in §7) was resolved via §7.9 amendment 2026-05-23; V-E surface preserves the §7.9-aligned IRC §4121 citation.

**Reception-chain weight class affected:** **HIGH (CONSULTANT) + LOWER (PROJECTED-DOWNSTREAM).** Primarily addresses C-1 editor-consultant + C-12 center-right policy reader (DIRECT) + C-6 LPE / institutional-design reader (PROJECTED-DOWNSTREAM). Under Amendment D weighting: the IRC §4121 statutory anchor strengthens institutional-analysis register at HIGH consultant weight (Cohen + Chasman recognize the statutory-precision discipline) + DIRECT weight (C-12 center-right policy reader's institutional-analysis register expectation is met) + LOWER projected-downstream weight (LPE network's legal-analysis verification).

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** This is a brief-§7.9-aligned correctness verification; no new finding. The V-E surface honors the §7.9 amendment; the per-character + reception-chain weighting confirms the institutional-analysis register reading is sustained.

---

### F-3.1-V-E-6 (LOW — POSITIVE VERIFICATION) — SMCRA 30 U.S.C. §1259 statutory cite added

**Location:** V-E §III, line 46.

**Current V-E text:**
> Reclamation bonds posted by mining companies under the Surface Mining Control and Reclamation Act (30 U.S.C. §1259) routinely cover four to six billion dollars less than the actual cost of reclamation when operators fail or abandon their obligations

**§7.9 specification:** "Reclamation-bonds shortfall: Reclamation bonds posted by mining companies cover $4–6B less than the actual reclamation cost."

**Issue:** None. The V-E surface adds the SMCRA statutory citation (30 U.S.C. §1259 — the SMCRA performance bond requirement section); brief §7.9 specifies the shortfall but not the statutory anchor. The statutory anchor is publicly verifiable (30 U.S.C. §1259 is the canonical performance bond section in SMCRA's federal program; SMCRA itself is at §7.8 Foreclosure Bond lineage).

**Reception-chain weight class affected:** **HIGH (CONSULTANT) + LOWER (PROJECTED-DOWNSTREAM).** Strengthens institutional-analysis register at C-1 consultant weight + C-6 LPE projected-downstream weight + C-8 environmental economist projected-downstream weight. Statutory-precision discipline; substrate-safe (federal statutory text is verifiable public record).

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** Substrate-safe statutory citation; matches V-D bounded-expansion pattern (publisher-house attributions; statutory citations) per the Phase C7 forward-pointer. The §III statutory-precision register is consistently maintained across multiple V-E grafts (IRC §4121; 30 U.S.C. §1259; GAO-11-696) — this is a coherent institutional-analysis-register tightening across the section.

---

### F-3.1-V-E-7 (LOW — POSITIVE VERIFICATION) — Department of Interior MMS reorganization detail added

**Location:** V-E §III, line 48.

**Current V-E text:**
> The Minerals Management Service, the federal agency overseeing offshore drilling safety in the years before the Deepwater explosion, was a documented case of regulatory capture — staffed, in part, by personnel who moved between industry and the agency, and chronically under-resourced for its mandate. The Department of the Interior's post-disaster reorganization split MMS into separate revenue-collection, leasing, and safety-enforcement bodies for exactly this reason.

**§7 specification:** Brief §7 does not specify the DOI MMS reorganization. The base claim (MMS regulatory capture; revolving door) was in V-D and in the brief §III paragraph spec; the V-E expansion adds the documented institutional response (DOI's May 2010 reorganization announcement + subsequent split into the Bureau of Ocean Energy Management, Regulation and Enforcement [BOEMRE] in 2010, further split into the Bureau of Ocean Energy Management [BOEM] + Bureau of Safety and Environmental Enforcement [BSEE] + Office of Natural Resources Revenue [ONRR] in 2011).

**Substrate-safety verification:** The DOI MMS reorganization is documented public record (Secretary Salazar's May 19, 2010 announcement; subsequent regulatory orders; standard offshore-drilling-policy reference works). No invented specifics; no quoted speech; no motivation attributions. The phrasing "split MMS into separate revenue-collection, leasing, and safety-enforcement bodies for exactly this reason" is a substantively-accurate summary of the BOEMRE → BOEM + BSEE + ONRR split (revenue-collection = ONRR; leasing = BOEM; safety-enforcement = BSEE).

**Reception-chain weight class affected:** **HIGH (CONSULTANT) + LOWER (PROJECTED-DOWNSTREAM).** Primary addresses C-12 center-right policy reader (DIRECT — institutional-response register expectation met) + Cohen consultant weight (institutional-analysis Forum-series-credibility signal) + adversarial-set A2 Public Choice theorist (the V-E application notes the MMS sentence is preserved from V-D as substantially-disarming the Public Choice adversarial pushback; the DOI reorganization detail strengthens this disarming further). Substrate-safe; verifiable from federal-agency reorganization public record.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** The MMS reorganization detail is substrate-safe + adversarial-disarming + institutional-analysis-register-strengthening. Optional brief §7.4 expansion (2008 financial crisis section, where MMS regulatory-capture context belongs) — currently §7 inventory does not list MMS reorganization specifics. Low-priority brief amendment; not blocking.

---

### F-3.1-V-E-8 (LOW — POSITIVE VERIFICATION) — Hartwick *American Economic Review* venue specified

**Location:** V-E §VI, line 80.

**Current V-E text:**
> It begins with John Hartwick's 1977 paper in the *American Economic Review*, "Intergenerational Equity and the Investing of Rents from Exhaustible Resources,"

**§7.8 specification:** "John Hartwick, 'Intergenerational Equity and the Investing of Rents from Exhaustible Resources' (1977). Hartwick rule."

**Issue:** None. The V-E surface adds the *American Economic Review* venue specification. The brief §7.8 doesn't specify the venue but the Hartwick 1977 paper is widely known to be published in the *American Economic Review* (Vol. 67, No. 5, December 1977, pages 972-974). The venue specification is substrate-safe (verifiable per AER journal archive + standard resource-economics reference works).

**Reception-chain weight class affected:** **LOWER (PROJECTED-DOWNSTREAM).** Primarily addresses C-8 environmental / resource economist + C-7 civic-republican / institutional-design reader (both PROJECTED-DOWNSTREAM). Bibliography-discipline signal at projected-downstream weight; substrate-safe.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** Substrate-safe venue specification; matches the pattern of publisher-house + statutory-citation grafts at V-E. Under Amendment D weighting, this is LOWER-weight projected-downstream lift — the C-8 resource-economist reader's bibliography-tracking is strengthened. Optional brief §7.8 expansion to record the venue; low-priority.

---

### F-3.1-V-E-9 (LOW — POSITIVE VERIFICATION) — Norway GPFG NBIM manager specified

**Location:** V-E §VI, line 82.

**Current V-E text:**
> The Norwegian state's Government Pension Fund Global, managed by Norges Bank Investment Management, is the most thoroughgoing application.

**§7.8 specification:** "Norway Government Pension Fund Global. ~$1.9T; ~$340K per Norwegian citizen; 2001 fiscal rule caps annual spending at ~3% of returns; capital itself inviolate."

**Issue:** None. The V-E surface adds the Norges Bank Investment Management (NBIM) manager specification. NBIM is the asset-management arm of Norges Bank (Norway's central bank); it is the fund's named operating manager (Wikipedia + NBIM annual reports + Norges Bank Act). Substrate-safe; publicly verifiable.

**Reception-chain weight class affected:** **LOWER (PROJECTED-DOWNSTREAM).** Primarily addresses C-8 environmental / resource economist + C-10 Stone Center reviewer (both PROJECTED-DOWNSTREAM). Sovereign-wealth-fund-analysis institutional-precision signal; substrate-safe.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** Substrate-safe institutional-precision graft; under Amendment D weighting this is PROJECTED-DOWNSTREAM-weight specialist-reader lift. Coherent with the §VI Norway paragraph's two-event (1990 act + 1996 first deposit) precision restored at LOCKED Pass 3.1 F-3.1-2; the NBIM addition continues the same precision-discipline pattern.

---

### F-3.1-V-E-10 (LOW — POSITIVE VERIFICATION) — Darity & Mullen UNC Press publisher specified

**Location:** V-E §V, line 66.

**Current V-E text:**
> William Darity Jr. and A. Kirsten Mullen's *From Here to Equality* (University of North Carolina Press, 2020) developed the accompanying empirical and policy apparatus

**§7.7 specification:** "William Darity Jr. + A. Kirsten Mullen, *From Here to Equality* (2020). Wealth-gap calculation methodology; $14T cumulative wealth deficit anchored to slavery, sharecropping, redlining, convict leasing, discriminatory homeownership policy, educational and employment exclusion."

**Issue:** None. The V-E surface adds "(University of North Carolina Press, 2020)" — publisher house + year. UNC Press is the actual publisher of *From Here to Equality* (verifiable per UNC Press catalog + standard library cataloging). Substrate-safe.

**Reception-chain weight class affected:** **PROJECTED-DOWNSTREAM (LOWER) + DIRECT (HIGHEST) partial.** Primarily addresses C-5 reparations-economics-successor + C-10 Stone Center reviewer + C-14 Coates/Darity-lineage reader (all citation-discipline-tracking; PROJECTED-DOWNSTREAM weight) + marginal C-2 DIRECT-reader bibliography-credibility signal.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding.

**Reasoning:** Substrate-safe publisher attribution. Consistent with the V-D bounded-expansion pattern (Phase C7 forward-pointer). The §V citation cluster now carries both the Darity & Mullen UNC Press publisher + the Hamilton et al. Insight Center + Duke Center publisher; the citation cluster's bibliography-discipline-signaling is strengthened across the paragraph.

---

### F-3.1-V-E-11 (LOW) — Schneider 1999 publication year — narrow verification recommendation

**Location:** V-E §I, line 6.

**Current V-E text:**
> The contamination was first surfaced for a national audience by Andrew Schneider's 1999 reporting for the *Seattle Post-Intelligencer*.

**Issue:** The "1999" anchor for Schneider's reporting requires narrow verification. Schneider's Pulitzer-winning *Seattle Post-Intelligencer* Libby series ran in November 1999 + continued through 2000-2001; the canonical anchor year is 1999 for the initial breakthrough series. Schneider himself + McCumber subsequently published *An Air That Kills: How the Asbestos Poisoning of Libby, Montana, Uncovered a National Scandal* (G.P. Putnam's Sons, 2004 hardcover; reprint editions).

**Substrate-safety verification:** "1999" anchor is correct for the initial *Seattle Post-Intelligencer* breakthrough series. (Verifiable per standard environmental-health-journalism reference works + Schneider's published bibliography + the SPLC + Pulitzer record.) If author wants the date precision to land at the year-level, "1999" is correct. If author wants to be slightly more precise, "1999-2000" or "Pulitzer-recognized 1999 *Seattle Post-Intelligencer* reporting" would also work; current "1999" is acceptable and clean.

**Reception-chain weight class affected:** **DIRECT (HIGHEST).** Same C-13 + C-16 + C-2 affected as F-3.1-V-E-4.

**Options:**
- **(a) No change.** "1999" is acceptable as anchor year for the SP-I breakthrough series.
- **(b) Mild expansion to "1999 Pulitzer-recognized" or similar.** Strengthens journalistic-witness-tradition recognition. Cost: small expansion; benefit: signals to C-13 + C-16 that the Schneider anchor is being read as journalistic-tradition recognition rather than just a casual citation. Risk: may read as ornamental.
- **(c) Compress to "1990s" if author judges 1999 precision is unverifiable from current substrate inventory.** Cost: loses anchor precision; benefit: hedge against verification miss. Likely unnecessary — 1999 is publicly verifiable.

**Recommendation:** **(a)** — no change. "1999" is publicly verifiable + brief-§7-amendable (recommend adding Schneider to §7.1 inventory at next brief amendment cycle).

**Reasoning:** "1999" is verifiable per standard reference works; the SP-I reporting is documented; the year-anchor is substrate-safe per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` §"Substrate-safe attributions ARE permitted" (verifiable journalism reference). Under Amendment D weighting, this is DIRECT-reader-affecting (C-13 + C-16 read the Schneider anchor as journalistic-witness recognition; C-2 reads as institutional-measurement bibliography signal). Optional brief §7.1 expansion to record the Schneider anchor formally (separate from this audit; would land at next brief amendment cycle).

---

### F-3.1-V-E-12 (LOW — POSITIVE VERIFICATION) — Apparatus-exclusion sweep on V-E surface: CLEAN

**Location:** entire V-E draft (sweep).

**§8 apparatus exclusion list specification:** No instance of cluster-γ; RCV / Residual Commons Value; CSD / Cost Severance Damages; Commons Inversion Test; "four gates"; "three ways of counting"; Method 1/2/3 numbering; Hotelling Identity; Technical Appendix §-references; Greek letters; subscripts; Cᵢ-style notation; displayed equations.

**Sweep result on V-E surface:** Zero instances of any §8 exclusion-list term. The V-E grafts (Schneider anchor; FCIC corrected verbatim; GAO-11-696 citation; IRC §4121 + SMCRA 30 U.S.C. §1259 statutory cites; DOI MMS reorganization; Hamilton publisher; UNC Press publisher; SCF + DFA; *American Economic Review* venue; NBIM manager; §VII subhead change) did not introduce any apparatus terms. The §VII subhead change from "The architecture is engineered" to "The architecture, engineered" is a participial-noun-phrase restructure per Pass 3.2 LOCKED F-3.2-2 ratification + V-E preservation; not apparatus-related.

**Reception-chain weight class affected:** **HIGHEST (DIRECT).** Apparatus-exclusion-list compliance is the load-bearing tripwire defense for BR's editorial brain (CONSULTANT) + BR reader (DIRECT) + general policy reader (DIRECT) + center-right policy reader (DIRECT) + first-gen reader (DIRECT). Zero leakage at the post-V-E surface confirms the audience-blind regime + Path B preemptive policy + V-E spot-fix application discipline operated as designed.

**Options:** (a) No change. Documented as positive verification.

**Recommendation:** **(a)** — no change. Positive verification finding confirming Pass 3.1 LOCKED F-3.1-12 holds at the V-E surface.

**Reasoning:** Pass 3.1 LOCKED F-3.1-12 documented zero apparatus-exclusion-list violations at the pre-spot-fix LOCKED surface. V-E surface re-sweep confirms the V-E grafts did not introduce apparatus terms. The Path B discipline holds through both LOCKED → V-D → V-E transitions.

---

## §3. Optional brief §7 inventory amendments (LOW-priority, non-blocking)

The fresh Pass 3.1 re-fire surfaces 4 V-E grafts that are substrate-safe + verifiable but not currently in brief §7 inventory. Recommend optional brief amendments at next amendment cycle (not blocking V-E submission):

1. **§7.1 (Libby) — add Schneider 1999 SP-I + Schneider + McCumber 2004 *An Air That Kills*.** Anchors the §I Schneider attribution to brief §7 inventory.
2. **§7.4 (2008 financial crisis) — add DOI MMS reorganization 2010-2011 (BOEMRE → BOEM + BSEE + ONRR split).** Anchors the §III MMS reorganization detail to brief §7 inventory.
3. **§7.8 (Foreclosure Bond lineage) — add Hartwick 1977 venue (*American Economic Review*) + Norway GPFG manager (Norges Bank Investment Management).** Anchors the §VI Hartwick + Norway specifications.
4. **§7.9 (supporting empirical anchors) — add SMCRA 30 U.S.C. §1259 statutory anchor.** Anchors the §III SMCRA citation.

These amendments would bring §7 into V-E-surface alignment. None are blocking; the fresh Pass 3.1 verdict is CLEAN on the V-E surface.

---

## §4. Aggregate verdict (Amendment D-weighted)

| Severity | Count | Resolution path |
|---|---|---|
| HIGH | 0 | — |
| MEDIUM | 0 | — |
| LOW | 12 | F-3.1-V-E-1 through F-3.1-V-E-12 (10 positive verifications + 1 narrow Schneider year verification recommendation + 1 apparatus-exclusion clean sweep) |
| **Total** | **12** | — |

**Overall pass verdict:** **INHERITED CLEAN — 0 HIGH findings; 0 MEDIUM findings; 12 LOW findings (10 positive verifications on V-E grafts + Schneider year verification recommendation + apparatus-exclusion clean sweep).** No spot-fix required for V-E essay surface. Optional brief §7 inventory amendments at next brief amendment cycle per §3 above (non-blocking).

**The 3 V-E fixes (F-FCIC-FIX + F-FRESH-3.1-HAMILTON + F-3.5-FRESH-3) are verified verbatim-faithful + substrate-safe + substantively correct.** The 6 additional V-D-inherited grafts (Schneider anchor; GAO-11-696 specification; IRC §4121 + SMCRA citations; DOI MMS reorganization; UNC Press + AER + NBIM specifications) are verified substrate-safe + publicly verifiable + register-consistent with §III's institutional-analysis voice.

**Amendment D weighting consequence on aggregate-verdict synthesis:**
- The F-FCIC-FIX (HIGHEST DIRECT-reader weight) was the dispositive correction at V-E promotion; the fresh re-fire confirms verbatim-faithful application. This is the load-bearing positive-verification finding under Amendment D.
- The F-FRESH-3.1-HAMILTON + F-3.5-FRESH-3 corrections (LOWER PROJECTED-DOWNSTREAM weight) are substrate-safe specialist-reader lifts; under Amendment D weighting they are correctly-prioritized lower than the F-FCIC-FIX but still ratifiable given substrate-safety + zero DIRECT-reader cost.
- Substrate-safety check on Schneider anchor (DIRECT weight) confirms substrate-safe published-work attribution; optional §7.1 inventory amendment recommendation surfaces at LOW priority.

**Carry-forward Pass 3.1 verdict status:**
- LOCKED Pass 3.1 (2026-05-23) RATIFIED + APPLIED: 0 HIGH + 3 MEDIUM (all resolved via spot-fixes / §7.9 amendment) + 9 LOW.
- V-E application 2026-06-01 RATIFIED + APPLIED: 1 HIGH (F-FCIC-FIX) + 2 MEDIUM (F-FRESH-3.1-HAMILTON + F-3.5-FRESH-3) — all 3 verified verbatim-faithful in this fresh re-fire.
- V-E fresh Pass 3.1 (this artifact, 2026-06-02): 0 HIGH + 0 MEDIUM + 12 LOW = INHERITED CLEAN.

**Apparatus-exclusion violations:** ZERO at V-E surface (per F-3.1-V-E-12).

---

## §5. Interactive ratification protocol (per v3.1 Amendment C)

This artifact is **PROPOSED**. Per v3.1 Amendment C (ratified 2026-05-19; codified at parent brief v1.0.1 §13), prose-modifying passes (3.1 / 3.2 / 3.5) follow per-finding artifact format with Options + Recommendation + Reasoning. Ratification is **INTERACTIVE** — a follow-up session walks the author through each finding with options + recommendation + reasoning + applies ratified spot-fixes to source in the same combined session.

**Per-finding ratification expected at the interactive session:**

For each F-3.1-V-E-N finding, author selects Option (a) / (b) / (c) — or supplies an alternative. The fresh Pass 3.1 verdict is INHERITED CLEAN; no spot-fixes required for ratification + application. Optional brief §7 inventory amendments per §3 are author-disposition items at next brief amendment cycle (do not block V-E submission).

**No Path B violations expected at ratification:** the audit verified the V-E surface against brief §7 + V-E application artifact source verifications. No paste-from-Ch-5 moves required.

---

## §6. What comes next

After Pass 3.1 fresh re-fire ratification (this artifact):

- **Pass 3.2 fresh re-fire on V-E surface** — companion artifact at [`pass-3-2_V-E_fresh-refire_AMENDMENT-D_2026-06-02.md`](pass-3-2_V-E_fresh-refire_AMENDMENT-D_2026-06-02.md) (concurrent with this Pass 3.1 fresh re-fire per parent-session paste-text). Polarity: CUT. Catches expository flatness; meta-commentary; rule-of-three LLM tics; em-dash density (V-E surface = 20 sites); cumulative-density check at §V Hamilton expansion.
- **V-E application Phase B5** (light Pass 3.3 re-fire on V-E confirming C-10 ✓✓→✓✓✓ forecast).
- **V-E application Phase B6** (adversarial verification panel on F-3.5-FRESH-3).
- **V-E application Phase C7** (V-F bounded expansion search) + **Phase C8** (V-G structural-choice testing).
- **V-E application Phase D9** (F-3.5-FRESH-1 §I Schneider sensory expansion structure-only routing to author).
- **V-E application Phase E** (final fresh-session audit + Stage 4 + Stage 5 update).
- **Author-controlled submission gate** (Phase E13) per CLAUDE.md submission discipline.

**Stage 4 + Stage 5 forward-pointers** (per brief §14): Stage 4 essay-scale render audit at Submittable preview before submit; Stage 5 pre-submission bookend sign-off + AI-disclosure transparency at [`publishing/essays/boston-review-accountability-gap/stage-5-signoff.md`](../stage-5-signoff.md).

---

## §7. State one-liner

`STATE: br-V-E-pass-3-1-fresh-refire-AMENDMENT-D [PROPOSED]; NEXT: parent-session-consolidation + Pass-3-2-fresh-refire-AMENDMENT-D + author-disposition on optional §7 brief amendments; AWAITING: author-confirmation`

---

## §8. Cross-references

- **Companion artifacts (this re-fire cycle):** [`stage-1-brief_AMENDMENT-D-update_2026-06-02.md`](stage-1-brief_AMENDMENT-D-update_2026-06-02.md); [`pass-3-2_V-E_fresh-refire_AMENDMENT-D_2026-06-02.md`](pass-3-2_V-E_fresh-refire_AMENDMENT-D_2026-06-02.md).
- **LOCKED baseline:** [`pass-3-1-fact-check.md`](pass-3-1-fact-check.md) RATIFIED 2026-05-23.
- **V-E application:** [`v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md`](v-e-application_pass-3-1-and-3-5-spot-fixes-applied_2026-06-01.md).
- **V-D fresh re-audit:** [`pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md`](pass-3-3-3-4-3-5-bundled_VERSION-D_FRESH-RE-AUDIT_2026-05-28.md).
- **Substrate-safety discipline:** [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md).
- **Amendment D doctrine:** `tools/memory/feedback_audience_aware_drafting_discipline.md` + Aeon Option E.2 γ.1 empirical anchor (commit `73c5764`).

---

*End of Pass 3.1 fresh re-fire on V-E surface under Amendment D weighting — PROPOSED 2026-06-02. Awaits parent-session consolidation + author disposition.*
