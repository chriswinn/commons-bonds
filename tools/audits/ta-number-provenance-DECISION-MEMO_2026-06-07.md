# TA Number-Provenance — DECISION MEMO

**Created:** 2026-06-07 (work 2026-06-07 → 2026-06-08)
**Companion to:** `tools/audits/ta-number-provenance-ledger_2026-06-07.md`
**Branch:** `claude/ta-provenance-260607-ad2dfc` (HELD; not merged).
**Purpose:** the class-4 / structural items the Foundation session **deliberately did NOT apply** because they need author judgment or belong to another session. Each item: the issue, options, recommendation, owner. Per the Interactive Ratification Protocol (options + recommendation + reasoning).

---

## Cross-session coordination (READ FIRST)

The **M3 Path-B rework session** (Session D, branch `ta-m3-pathb`) is live and overlaps this memo:

- It **reworked McDowell M3:** central $2,580 → **band ~$340–3,670 / central ~$1,160 (market-anchored).** This supersedes the prior `$2,500 mid` and the `V_option $50–500/ton` interim edit, and cascades into §11.6 / §3.6 M3, the implied CS (~$2,400/ton), and the McDowell IPG (~50×).
- It **added bib entries** on its branch: **§16.5** (α-irreversibility: Henry 1974, Palmer 2010, Bernhardt & Palmer 2011, Lindberg 2011, Solomon 2009, **IPCC AR6 SPM B.5, Archer 2009**) and **§23.1** ς/R-P data sources (**EIA coal R/P; Energy Institute / BP Statistical Review; USGS Appalachian/McDowell + Mineral Commodity Summaries**).

**Consequences for this memo:**
1. **Two of my class-4 sourcing flags are already being closed by Session D** — route them there, do NOT double-source:
   - Atmospheric CO₂ half-life ~100/1000 yr (§7.3, §17.6) → **Archer 2009 + IPCC AR6** (Session D §16.5).
   - McDowell disturbed-acreage / cumulative coal production / coal-price (§11.6, §7.6) → **USGS McDowell + EIA** (Session D §23.1).
2. **§23.1 merge coordination:** *both* this branch and `ta-m3-pathb` edited `research/literature/bibliography.md` §23.1. My edits = the **Falcon 9 update + NASA/KISS/Colvin space-economics entries**; Session D's = the **ς/R-P + USGS + EIA coal entries**. Different bullets, same list → should merge cleanly, but **merge sequentially and eyeball §23.1** (per the resume-doc divergent-edit caution).
3. **All §11.6/§3.6/§9.5 Method-3 numbers + the McDowell IPG belong to Session D.** This memo's 3C V_option/$300-RCV items are noted but **Session D owns the resolution.**

---

## Item 1 — The IPG / three-model-convergence apparatus (§9.5, §11.11, §3.2, §16.4) — **BIGGEST**

**Issue.** Every IPG multiple — the §9.5 twelve-cell table, the "canonical" 33–122×, the "triangulated" 50–555×, the §3.2 `IPG=33` illustration, the §16.4 33×–122× — is a CIT **model output**, currently presented with TA-internal backing ("canonical," "documented," "terms_index"). As **external facts** they are class-4. As **derived model outputs** they could be legitimate class-2 — *if* the derivation is shown and the "canonical/documented" framing (which reads as an external-authority claim) is dropped.

**Options.**
- **(A) Reframe as derived outputs (recommended).** Relabel "canonical/documented IPG" → "framework-computed IPG (per §11.x derivation)"; ensure each case's multiple traces visibly to its RCV÷price work; keep the numbers. Converts class-4-by-framing → class-2.
- **(B) Source-validate against external implicit-pricing literature.** Stronger but heavy; only some cases have external IPG analogues.
- **(C) Leave as-is.** Rejected — "canonical" reads as an external-authority claim the framework can't cash.

**Recommendation: (A).** It's the honest frame (these *are* the framework's outputs, and that's fine) and it's the cheapest. **Risk:** the §9.5 Deepwater 15–17× and the §11.2 inputs don't reproduce cleanly (numerator < component sum; see Item 4) — fix those *before* relabeling so the shown derivation actually reproduces.
**Owner:** correctness sweep (Session C) for the relabel; coordinate with Session E for Deepwater.

---

## Item 2 — Norway CS-reduction 84% → 16% (narrative inversion) — **HIGHEST-RISK**

**Issue.** The committed edit (84%→16%) is **arithmetically correct** ($48/$300 = 16%; the old "84%" mistakenly reported the *remaining* fraction). But it **inverts the framework's Norway story**: "16% CS-reduction" is not "dramatically reduced CS." And it rests on the disputed **$300 RCV** anchor (§11.5 body says $161–422/BOE; the $300 is the contested table figure).

**The deeper problem (already flagged in the resume doc).** Measuring Norway's architecture-benefit as `$48/$300` (realized rent-capture ÷ RCV) is arguably the **wrong model.** Per the M3 sensitivity doc, Norway's CS-reduction mechanism is **institutional architecture moving α from ~1 to ~0.5–0.75** (reducing *irreversibility*), plus a ~$2T restoration-optionality fund — not the $48/BOE rent number. Path B has no α dial, so this must be re-expressed.

**Options.**
- **(A) Defer to Session D Path-B rework (recommended).** Norway is explicitly the highest-risk Path-B open question; the GPFG-restoration-optionality / canonical-B₂ story must be re-expressed there with the reworked numbers.
- **(B) Quick narrative patch now.** Reword so "16% reduction" doesn't read as undercutting Norway. Rejected as premature — Session D may change the number again.

**Recommendation: (A). Do not touch the Norway CS-reduction framing in this session.** Leave the committed 84→16 edit as the interim arithmetic correction; Session D re-expresses.
**Owner:** Session D.

---

## Item 3 — Load-bearing posited per-unit anchors (§11.5 / §11.6 / §11.7)

**Issue.** Bare numbers that propagate into headline results (ledger Part 3C): Foreclosure +$50–200/BOE; the $50/$300-BOE pair behind "Norway 17% captured"; restoration $50–200K/acre; $200–500K/displaced-resident; the M2 back-outs ($5–8B / $5–10B / $3–5B). The input-provenance audit already found real anchors **far lower** for several (reclamation ~$12–15.5K/acre vs the posited $50–200K).

**Options.**
- **(A) Estimate-label + cite the real anchor (recommended for Eco/Cohesion/reclamation).** Relabel as explicit framework estimates; cite Appalachian Voices (reclamation), Isle de Jean Charles (relocation), Census (migration), OSMRE/GAO (bonds); state the functional-substitute-vs-reclamation assumption; route the non-substitutable remainder to M3. **No number change required** (input-provenance audit confirms the combined anchor is dominated ~50× by the Habitability term, so Eco/Cohesion sub-floor moves are immaterial to the headline).
- **(B) Re-peg to the documented anchors.** Would drop the Ecosystem floor to ~$1–4/ton — defensible but changes the number; immaterial to the combined anchor.

**Recommendation: (A) for Eco/Cohesion/reclamation/migration** — low-risk relabels with citations already in §23/§23.2. **The Foreclosure +$50–200/BOE, V_option, and $300-RCV items → Session D** (they move with the M3 rework). **Owner:** mostly this workstream's SOFT-batch (relabels), but stage *after* Session D lands so the M3-dependent ones don't thrash.

---

## Item 4 — Deepwater §11.2 internal inconsistencies (route to Session E)

**Issue.** Two non-class-4 defects the enumeration caught: (a) §11.2 "Total documented $20–30B" is **less than the sum of its own components** ($18.7B + $4B + $8–12B = $30.7–34.7B); (b) the 15–17× IPG **doesn't reproduce** from the stated inputs ($20–30B ÷ $1.1B ≈ 18–27×) — it matches the *real* reconciliation (~$61.6B ÷ ~$3–4B) only because numerator and denominator are *both* wrong in offsetting directions. The resume doc's Deepwater decision (cost $61.6B; rev ~$3–4B; **keep IPG 15–17×**) is the fix anchor.

**Recommendation:** route to **Session E** (Deepwater reconciliation closeout). Note the resume-doc "KNOWN FALSE POSITIVE: do NOT change the convergence-within-1.5× claim." **Owner:** Session E.

---

## Item 5 — §11.9 DAC three-horizon bands — **VERIFIED + FIXED 2026-06-08 (no longer parked)**

> **RESOLVED.** Author authorized the fix once verified, citable numbers were in hand. **Applied:** intro corrected from the unsupported $600–1,200 / $150–500 / $100–200 to the **source-confirmed** $600–1,000 / $300–600 / $100–300 (= the bands the body/facility/review-lit/anchor already carry, traceable to Fuss 2018/IPCC AR6/IEA/targets); added a **sourced Orca actual-cost caveat** (>$1,000/ton) to the facility table + intro + anchor. **Conservative cap kept at $1,000 → no cascade into §3.3/§11.5/§11.6** (verified untouched + still consistent). Four DAC/SCC bib entries added to §18 (Keith 2018, Realmonte 2019, House 2011, Rennert 2022), all citation details verified vs primary sources. §23 updated. The text below is retained as the provenance record.

---

**Issue + verification (done this session 2026-06-08).** The intro said $600–1,200 / $150–500 / $100–200; the body said $600–1,000 / $300–600 / $100–300. Rather than align intro→body, I verified all bands against the named authorities (per the author's point: *internal consistency ≠ correctness*). **Neither set is fully right, and the body is NOT a safe alignment target.** Verified verdict:

| Horizon | **Source-confirmed band** | What's wrong in the TA |
|---|---|---|
| Current operational | **~$600–1,000; leading plants ~$1,000–1,200+** (Climeworks Orca "over $1,000"/€929) | **Body's $1,000 cap understates; intro's $1,200 is the better bound.** The §11.9 facility table's "Orca $600–1,000" is ALSO stale. |
| At-scale ~2030 | **$300–600** (targets); near-term deployment may run $400–1,000 | Intro's $150 floor unsupported. |
| Optimistic 2050 | **$100–300** (IPCC AR6/Fuss 2018; IEA $125–335→<$100; NAS $100–600) | Intro's $200 cap understates. |

**Defensible target set: ~$600–1,200 / $300–600 / $100–300** (conservative upper from the intro; at-scale + optimistic from the body). **The whole DAC cost section is stale (2021-vintage), not merely internally inconsistent** — refresh the facility table + intro + consolidated bands against 2024–2026 Climeworks/IEA reporting.

**Materiality:** raising the conservative cap $1,000→$1,200 lifts the McDowell Habitability Method-1 conservative high ~20% ($2,610 → ~$3,130/ton). So this is NOT cosmetic — it moves a headline anchor.

**Decision (author 2026-06-08): leave the FIX to a parallel session; NOTE for next PM session.** The provenance work is done (above); the parallel session applies the *source-confirmed* targets, not a blind align. **Owner:** next PM session → route to whichever session owns §11.9 (Session C, or fold into the M3/Habitability-anchor work since it moves the M1 anchor).

**Sources (verified 2026-06-08):** [Canary Media — Climeworks halving costs](https://www.canarymedia.com/articles/carbon-capture/co2-removal-leader-climeworks-says-new-tech-can-halve-costs-energy-use); [OceanCare — Mammoth](https://www.oceancare.org/en/stories_and_news/climeworks-climate-crisis/); [IEA Direct Air Capture 2022 exec summary](https://www.iea.org/reports/direct-air-capture-2022/executive-summary); [Clean Energy Wire — DAC Q&A (IPCC AR6 $100–300; $400–1,000 near-term)](https://www.cleanenergywire.org/factsheets/qa-dac).

---

## Item 6 — §3D mechanical issues (fast)

- **`log` ambiguity:** `scarcity_multiplier = 1 + log(1+σ)×0.05` **reproduces only under natural log**; base-10 gives ~1.12 not ~1.27/1.31. Recommend writing `ln` explicitly (or stating the base). Affects every M3 scarcity_multiplier. **Coordinate with Session D** (it owns the M3 functional forms).
- **Hotelling 0.05 anchor:** the "5%/yr proxy" is unsourced. Either cite a Hotelling-rent empirical range or relabel as a posited calibration. **→ Session D.**
- **M3 midpoints** ($280 Norway, $2,500→now ~$1,160 McDowell) are **not arithmetic means** of their ranges and carry no weighting rule. **→ Session D** (already reworking).

---

## Item 7 — Norway USD vintage (minor)

**Issue.** The NOK anchor is solid (NOK 21,268B end-2025, NBIM). The USD "~$2.0T end-2025 with $2.2T peak" is FX-date-sensitive; current sources say the fund **exceeded $2.2T at end-2025**, so the TA arguably understates it.

**Recommendation:** lead with the NOK figure (FX-invariant); give USD with an explicit FX-date stamp rather than a number-change. Low priority. **Owner:** this workstream SOFT-batch or Session D (Norway).

---

## Item 8 — C3 Solow 1956 → 1974 (coordinate with correctness sweep)

**Verified facts (this session):** line 917 is the **only** "Solow 1956" use in the TA; the 1956 bib entry is at §18 L7981; "Solow 1974" is already in §18 (L7984) and used 5× elsewhere. Line 917's context ("intergenerational-equity lineage… long-horizon utility aggregation") fits **Solow 1974** (Intergenerational Equity & Exhaustible Resources), not the 1956 growth paper — the correctness sweep's misattribution diagnosis is sound.

**UPDATE 2026-06-08 — gating condition CONFIRMED MET.** The swap is **already applied on `ta-m3-pathb`** (§3.5 line 920 = "Solow 1974 *Review of Economic Studies*"; zero "Solow 1956" in-text there). Since the merged tree takes M3's §3.5, the §18 Solow-1956 entry (L7981) **is** orphaned post-merge.

**Decision: remove the §18 Solow-1956 entry — but at CLOSEOUT, against the MERGED tree, NOT on this branch.** Reason: **this branch's §3.5 still cites "Solow 1956"** (line 917 — untouched; §3.5 is M3's domain). Removing the bib entry on this branch in isolation would create a **dangling in-text citation** (citation with no entry) until the merge takes M3's §3.5 — strictly worse than the harmless orphan. So the safe sequence is: merge takes M3's §3.5 (Solow 1974, zero 1956 in-text) → **then** delete the §18 Solow-1956 line (`Solow, Robert M. "A Contribution to the Theory of Economic Growth." QJE 70, no. 1 (1956): 65–94.`). **Owner:** closeout (Session E) against the merged tree; verify `grep -c "Solow 1956"` = 0 in-text before deleting.

---

## Item 9 — Class-1 value-verification sweep follow-ups (2026-06-08)

The sweep (ledger Part 5b) confirmed SCC $190 (attribution fixed), Norway 78%, Black-Lung $5.1B debt, and all Baotou/USGS shares. Two items remain:

- **(9a) Black Lung "$44B cumulative payouts" — UNVERIFIED.** The $5.1B debt is confirmed; the $44B cumulative figure could not be located in accessible sources (CRS R45261 returned HTTP 403). **Action:** confirm via CRS R45261 (accessible mirror) or DOL OWCP / BLDTF annual financial report; if unconfirmable, relabel as an estimate or cut. Low materiality (it is one addend in the realized-B aggregate, not a headline). **Owner:** any session with source access; or closeout.
- **(9b) EIA 1960 coal price $4.50 → $4.71 — VERIFIED, not applied.** EIA confirms 1960 bituminous = $4.71/short ton (TA's $4.50 is low + sourced only to the internal Ch 6 table). The change cascades into the IPG ratios across **7 spots** (§3.3, §11.1, §11.6 ×3, §7.6, §14.7). **Owner:** Session C (IPG reframe) / Session D (§11.6) — apply $4.71 when they recompute the ratios, so it doesn't thrash mid-rework. (Effect is small: 555× → ~531×; inflation-corrected 50× → ~48×.)

## Summary of ownership

| Item | Owner | Apply when |
|---|---|---|
| 1 IPG apparatus reframe | Session C (+E for Deepwater repro) | after Item 4 |
| 2 Norway 84→16 narrative | **Session D** | Path-B rework |
| 3 Eco/Cohesion estimate-labels | this workstream SOFT | after Session D |
| 3 Foreclosure/V_option/$300-RCV | **Session D** | Path-B rework |
| 4 Deepwater repro | **Session E** | reconciliation closeout |
| 5 §11.9 DAC bands | **DONE 2026-06-08** | applied (source-confirmed; no cascade) |
| 6 log/Hotelling/midpoints | **Session D** | Path-B rework |
| 7 Norway USD FX stamp | **DONE (Session D, 0a50c68)** | merged into this branch |
| 8 Solow orphan | **Closeout (E), merged tree** | swap already on ta-m3-pathb; delete §18 1956 entry post-merge (grep-verify 0 in-text first) |
| 9a Black Lung $44B | any session w/ source access / closeout | verify CRS R45261 or DOL OWCP report; else relabel/cut |
| 9b EIA coal $4.50→$4.71 | Session C / Session D | verified; apply when IPG ratios are recomputed |

**Nothing in this memo is applied by the Foundation session.** The verified-safe fixes (§11.10, §18+§23 bib, B-collision) are in the ledger Part 1.
