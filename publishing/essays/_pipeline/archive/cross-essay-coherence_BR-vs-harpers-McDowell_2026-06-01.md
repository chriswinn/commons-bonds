# Cross-portfolio coherence audit — Boston Review Ch 5 essay vs Harper's Ch 2 → *What McDowell County Paid* essay — McDowell collision check

**Date:** 2026-06-01
**Workstream:** cross-portfolio-boston-review-harpers-McDowell-collision
**Branch:** `claude/cross-portfolio-boston-review-harpers-McDowell-collision-<harness-id>` (worktree-isolation creation denied at session start; audit performed in-place from primary working tree; commit + push deferred until author session-close ratification)
**Status:** **PROPOSED 2026-06-01.**

## §0. Audit scope

Brief §9.3 (Harper's Ch 2 *The Miner* Stage 1 brief, [`publishing/essays/harpers-the-miner/rigor/stage-1-brief.md`](../../harpers-the-miner/rigor/stage-1-brief.md) line 387) declared the BR Ch 5 essay scope **Coherent + scope-distinct** with the Harper's Ch 2 essay scope at brief level. This audit verifies the brief-level coherence holds against the canonical end-user-facing prose now sitting on `origin/main`:

- **Boston Review essay:** [`publishing/essays/boston-review-accountability-gap/essay.md`](../../boston-review-accountability-gap/essay.md) — Stage-3-cascaded end-user-facing prose, 7-section structure, ~4,500w body. Ch 5 derivative; institutional-measurement register; named-instrument architecture (Restitution Bond + Foreclosure Bond).
- **Harper's essay (canonical):** [`publishing/essays/harpers-the-miner/essay.md`](../../harpers-the-miner/essay.md) — Stage-5-RATIFIED READY-TO-SUBMIT 2026-05-27, 7,121w body, 8-section structure. Ch 2 derivative; literary-essay register, first-person Option B limited frame; apparatus excluded per brief §8.
- **Harper's V-D candidate:** [`publishing/essays/harpers-the-miner/_archive/parallel-drafts_2026-05-28/ch2-harpers-essay_hybrid_best-of-both.md`](../../harpers-the-miner/_archive/parallel-drafts_2026-05-28/ch2-harpers-essay_hybrid_best-of-both.md) — PROPOSED-PHASE-2-LOCKED 2026-05-28, 7,211w body; seven surgical hybridization insertions (HC-1 through HC-6 + MC-4) applied to the LOCKED Stage-5-RATIFIED submission cut. Independent audit V2 verdict at [`publishing/essays/harpers-the-miner/rigor/pass-3-3-3-4-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md`](../../harpers-the-miner/rigor/pass-3-3-3-4-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md).

Audit covers **both** the canonical state (essay.md 7,121w) and the V-D candidate (7,211w) so the conclusion holds whichever state ships.

---

## §1. Per-coherence-axis verification

### §1.1 Scope distinction — BR institutional-measurement vs Harper's literary-essay-of-McDowell

**Verdict: COHERENT-AND-DISTINCT.**

BR essay structural register:
- Third-person throughout (no first-person memoir) per BR brief §5 + BR's "no unsolicited personal essays" rule.
- Institutional-measurement voice: named institutions (W.R. Grace; BP; EPA; SEC; Norway GPFG); dated events; concrete numerical magnitudes anchored to institutional decisions.
- Seven-section structure (I Libby → II pattern across cases → III architecture-cannot-reach → IV two-directions → V Restitution Bond → VI Foreclosure Bond → VII engineered).
- Lead case: Libby (W.R. Grace asbestos; 40-to-1 cost-to-revenue ratio; 2009 criminal acquittal of seven named executives). McDowell appears only at compression depth as one item in §IV's four-case backward-direction enumeration (essay.md line 55).

Harper's essay structural register:
- First-person Option B limited frame (opening scene §I + occasional structural returns + third-person reportage spine) per Stage 1 brief §18.4 HIGH-2 RATIFIED.
- Literary-essay-of-McDowell voice: scene-anchored opening (driving down Route 52 on an October afternoon); courthouse-in-Welch place-density; named-miner voices (Robert Bailey 5-word black-lung quote; Ted Latusek "I always thought Consol would take care of me"); regional-organizing-tradition crediting (UMWA + Black Lung Association 1969 wildcat strike + Miners for Democracy + Yablonski murder).
- Eight-section structure with three-asterisk-ornament scene-shifts (no subheads); first-person opening + closing-scene return.
- Lead case: McDowell County (full-essay scope; one-county arithmetic walk across health + land + community + children + intergenerational columns). Libby appears nowhere in the Harper's essay text (verified via grep; zero hits).

**Differential map:**

| Axis | BR essay | Harper's essay |
|---|---|---|
| Lead case | Libby (asbestos) | McDowell (coal) |
| Voice | Third-person institutional-measurement | First-person Option B literary-essay |
| Named instruments | Restitution Bond + Foreclosure Bond surface explicitly | Apparatus excluded per brief §8; concept-level only ("cost severance" + "severed cost" + "value extraction" + "spatial cost severance" surface; no bond names) |
| Section structure | 7 sections; numbered headers (I, II, III...) with noun-phrase subheads | 8 sections; no subheads (three-asterisk-ornament scene-shifts only) per brief §10 |
| Lineage anchors | Pistor *Code of Capital*; Buchanan/Tullock + Public Choice; Mazzucato; Christophers; Darity-Mullen + Hamilton + Conley + Coates; Hartwick + Parfit + Pettit + Skinner | Mazzucato + Harvey + Hamby + Catte (+ Eller in V-D); regional-history (Caudill / Stoll lineage); Keefe *Empire of Pain*; Kennedy 1960 / Yablonski / Bailey / Latusek named-voice rendering |
| Engagement with reparations-economics tradition | §V develops Coates → Darity-Mullen → Hamilton → Conley at Restitution-Bond-genesis depth; Darity-Mullen typology cited; Restitution/Reparations asymmetry handled in 2-3 sentences | Reparations-economics tradition NOT engaged in body prose (Tier 2 #6 brief-flag at compression depth without surfacing apparatus name) |

The two essays are derivatives of **different chapters** (Ch 5 and Ch 2 respectively), drafted from **different briefs**, into **different venues** (institutional-policy quarterly vs literary monthly), under **different audience-set construction** (BR 16-character set Tier 1 BR-editor / BR-reader / Wylie-Bohan-cluster agent / trade-press econ-policy acquisitions editor vs Harper's 16-character set Tier 1 Beha / Harper's-reader / Wylie literary-essay cluster / trade-press literary acquisitions editor). The McDowell-at-essay-scope vs McDowell-at-compression-depth handling is **the intentional venue-tailoring**, not an unmanaged collision.

### §1.2 McDowell references in BR essay — depth + content

**Verdict: COHERENT (compression depth; consistent factual ground).**

BR essay carries exactly **one** McDowell reference. Located at §IV line 55 (within the "two directions of accountability" pivot section):

> *"There is the harm already realized. Four hundred died in Libby. Eleven workers and four to eight billion oysters were lost at Deepwater. Five million households completed foreclosure between 2008 and 2012. Black-lung claimants ran past the program's resources for treatment costs. **McDowell County coal communities watched extracted value move to coastal capital markets and were left with a public-health and infrastructure tail.** This is backward-looking accountability: the cost has been borne, the question is whether it can still be priced and discharged."*

Depth analysis:
- **One sentence** of compression depth (~28 words), embedded in a five-element list-form enumeration of backward-direction harms.
- **No quantitative McDowell anchors leak** (no 13-year life-expectancy gap; no 141/100k overdose rate; no 1961 first food stamps; no 100K → <20K population). The numerical specifics that anchor the Harper's essay's McDowell arithmetic are entirely absent from the BR essay.
- **No Bailey, Latusek, or any named McDowell-resident voice** appears in the BR essay (verified via grep — zero hits).
- **No engagement with the Kennedy 1960 visit** (verified — zero hits).
- Framing claim ("extracted value move to coastal capital markets" + "public-health and infrastructure tail") is consistent with both the Harper's essay's structural argument (the coal that came out of those mountains was not consumed in those mountains; it heated New York apartments, powered Pittsburgh steel mills, lit Chicago streetcars; the cheap energy flowing through their lives had a cost being concentrated, in real time, in a single county four hundred miles away) and with the Ch 5 source (line 198: "the coal industry's political-economic dominance in West Virginia legislative and regulatory architecture is a multi-generational rent-seeking history"; line 208: "the McDowell life-expectancy gap, the Libby asbestos deaths").

The compression-depth handling matches exactly what Harper's brief §9.3 forecast: *"Ch 5 references McDowell at compression depth (life-expectancy + community-restitution-application); Ch 2 → Harper's essay carries the full McDowell case at essay scope. No collision."*

### §1.3 Restitution Bond / Foreclosure Bond naming — apparatus discipline

**Verdict: COHERENT (clean apparatus separation; no instrument-name leakage in either direction).**

BR essay carries named instruments per BR brief §8 (which explicitly **KEEPS** "Restitution Bond" + "Foreclosure Bond" as concepts BR readers should learn from the essay):
- "Restitution Bond" appears as load-bearing §V title + extensive development (lines 61–73).
- "Foreclosure Bond" appears as load-bearing §VI title + extensive development (lines 61, 75–89).
- "cost severance" appears as load-bearing framework concept (lines 11, 23, 29, 31, 36, 37, 51, 53, 55, 59, 65, 67, 69, 71, 73, 81, 95, 97, 99, 101) — translated from Ch 5's "Cost Severance Damages / CSD" apparatus to plain-prose concept per BR brief §8 ("REPLACE WITH TRANSLATION").

Harper's essay (canonical 7,121w) verification:
- `grep -i "restitution bond\|foreclosure bond"` against `essay.md` returns **zero hits**.
- `grep -i "restitution bond\|foreclosure bond"` against V-D candidate (`ch2-harpers-essay_hybrid_best-of-both.md`) returns **zero hits**.
- Apparatus exclusion per Harper's brief §8 RATIFIED + APPLIED through Pass 3.1 → Pass 3.5 cascade (per Stage 5 sign-off §2 + V-D Independent Audit V2 §"Audit Polarity Discipline").

The "cost severance" + "severed cost" + "value extraction" plain-prose concept register Harper's essay carries at brief §8 RING-1 reveal cap (~18-22% effective per Pass 3.3 verification) is the framework-conceptual common ground; the named-instrument architecture (Restitution Bond + Foreclosure Bond) is BR-essay-exclusive scope. **No instrument-name leakage in either direction.**

### §1.4 Bailey + Latusek references — biographical-specifics check

**Verdict: COHERENT (BR does not engage; no biographical conflict possible).**

`grep -i "bailey\|latusek"` against BR essay.md returns **zero hits**. The named-miner voice rendering (Bailey 36-year tenure + 5-word "*It's almost like drowning*" black-lung quote + double-lung-transplant + Feb 2019 death + two-Congressional-testimonies; Latusek 19-year Consol litigation + Fourth-Circuit reversal + Oct 2022 death + "*I always thought Consol would take care of me*" closing quote) is **Harper's-essay-exclusive scope**.

No biographical-specifics conflict is possible because BR does not engage these subjects at any depth. Harper's named-subject-consent discipline (per Stage 1 brief §11 closed-at-Stage-0) and verbatim-quote preservation (six brief-§6-permitted verbatim quotes: Kennedy Canton ×1 + Bailey ×2 + Latusek ×3) carry forward to submission without BR-side coordination requirement.

### §1.5 Cross-essay numerical anchors — coherence verification

**Verdict: COHERENT (canonical-facts anchors consistent across essays where they appear in both; no contradiction surfaced).**

| Anchor | BR essay value | Harper's essay value | Coherence |
|---|---|---|---|
| Black Lung Benefits Program cumulative payout | "roughly forty-four billion dollars across half a century" (line 45) | "forty-four billion dollars in benefits over half a century" (line 81); "forty-four billion dollars that has been paid out" (line 83) | **IDENTICAL.** Both pegged to ~$44B; both anchored to half-century timeframe. |
| Black Lung Trust Fund outstanding debt | "As of September 2024, the program's trust fund carried roughly five billion dollars in outstanding debt" (line 45) | "the program's Trust Fund is currently about four and six tenths of a billion dollars in debt, and that debt is on track to reach roughly fifteen billion dollars by the year 2050" (line 81); "The four-and-six-tenths-of-a-billion-dollar shortfall in the federal Black Lung Trust Fund is a severed cost" (line 67) | **COHERENT (rounding differential, not contradiction).** BR uses "roughly five billion" rounded up; Harper's uses $4.6B specific. Both derive from Pass 3.1 F-3.1-4 ratification (BR brief §7.9 + Harper's brief §7.6 carry-forward). Underlying source: DOL annual Trust Fund reports as of Sept 2024. Both rounded-up "five billion" and specific "four and six tenths" are within standard journalism accuracy band; not a fact-check flag. |
| Reclamation-bonding gap | "four to six billion dollars less than the actual cost of reclamation" (line 45) | "Four to six billion dollars is not what gets called a rounding error" (line 93); "the available bond money totals three and eight tenths of a billion. Four to six billion dollars" (line 93) | **IDENTICAL.** $4-6B gap; both consistent. Harper's adds detail (633K acres + $7.5-9.8B cleanup cost + $3.8B available bond + $865M 2014-2016 bankruptcy transfer); BR keeps at compression. No conflict. |
| Federal Black Lung program funding mechanism | "supported largely by an excise tax on coal" (line 45) | "The program is funded largely by an excise tax on the coal industry, a tax that was supposed to make the polluting party pay for the cleanup, in the classic Pigouvian framing" (line 81) | **COHERENT.** Both pegged to coal-extraction excise tax; both anchor the structural-contrast argument (intended design = extraction-tagged; actual financing = general-revenue-absorbing). |
| Coal industry bankruptcy transfers 2014-2016 | NOT engaged | "Between 2014 and 2016, three major coal companies declared bankruptcy in succession, and in doing so transferred eight hundred and sixty-five million dollars in environmental liabilities directly to taxpayers" (line 93) | **NO CONFLICT.** Harper's-exclusive scope (specific to coal industry); BR engages the Trust-Fund-debt anchor at compression. |
| McDowell life expectancy gap (13 years) | NOT in BR essay (verified via grep — zero hits) | "The male life expectancy in McDowell County now is sixty-three and a half years. The national male average is seventy-six and a half. The gap is thirteen years" (line 51); "The thirteen-year life-expectancy gap between McDowell County and the national average" (line 67) | **NO CONFLICT.** Harper's-exclusive scope. Note: Ch 5 source (line 208) names "the McDowell life-expectancy gap" at compression as one of the four backward-direction harms; BR essay's §IV one-sentence McDowell reference is the BR derivative of that Ch 5 compression-depth handling, without the specific 13-year quantification. |
| McDowell overdose rate (141/100k) | NOT in BR essay (verified via grep — zero hits) | "The drug death rate in McDowell County, last time it was measured, ran at a hundred and forty-one per hundred thousand, against a national rate, that year, of about sixteen" (line 53); "The hundred and forty-one overdose deaths per hundred thousand in McDowell County" (line 127) | **NO CONFLICT.** Harper's-exclusive scope. |
| Libby cost-to-revenue ratio | "ratio is forty to one at the low end" (line 7) | NOT in Harper's essay (verified via grep — zero hits for "libby") | **NO CONFLICT.** BR-exclusive scope (Libby is BR lead case; Harper's lead case is McDowell). |
| Deepwater 40% recovery ratio | "Sixty billion against one hundred fifty billion. A forty percent recovery against documented total cost" (line 23) | NOT in Harper's essay | **NO CONFLICT.** BR-exclusive scope. |
| McDowell coal arithmetic (33-122× multiple) | NOT in BR essay | "between thirty-three and a hundred and twenty-two times the price the coal actually sold for. The range is wide... The floor of the range is the part that nobody serious disputes. Thirty-three times" (line 117) | **NO CONFLICT.** Harper's carries the 33-122× framework-multiple range with floor anchor at 33× per Ch 2 chapter framing. Atlantic Ideas Ch 9 essay (cross-essay coherence flagged at Harper's brief §9.3 #4) carries 116× McDowell-specific upper end + $520-$600/ton honest cost per Ch 8 post-cascade. **Cross-essay-coherence between Atlantic Ideas + Harper's is a separate verification item flagged at brief §9.6 #4 and is NOT in scope for this BR-vs-Harper's audit.** |
| Sackler / Big Three opioid settlements | NOT in BR essay (verified via grep — zero hits for "sackler\|purdue") | "The Sackler family, before Purdue filed for bankruptcy, extracted approximately eleven billion dollars from the company. The Big Three pharmaceutical distributors (McKesson, Cardinal Health, AmerisourceBergen) eventually settled, in 2022, for twenty-one billion dollars" (line 127) | **NO CONFLICT.** Harper's-exclusive scope. |

**No numerical anchor surfaces a conflict.** Where both essays carry the same anchor (Black Lung $44B paid; Trust Fund debt ~$5B / $4.6B; reclamation gap $4-6B; coal-excise-tax funding mechanism), values are consistent within standard journalism accuracy bands and both derive from the same Pass 3.1 F-3.1-4 ratification + canonical-facts inventory (BR brief §7.9 + Harper's brief §7.6). Where anchors are essay-exclusive, the scope-separation prevents collision.

### §1.6 HC-1 Eller in V-D — does BR cite Eller? required coordination?

**Verdict: NO REQUIRED COORDINATION (Eller is Harper's-essay-exclusive scope; BR's lineage anchors are different).**

V-D candidate HC-1 adds Ronald Eller, *Uneven Ground: Appalachia since 1945* (2008), to the §V lineage paragraph (V-D line 138; ~52w insertion) as Appalachian-regional-history scholar anchoring the named-tradition fluency the Harper's literary-essay register requires. V-D Independent Audit V2 §6 (Tier 1 #2 Harper's reader) lifts the Pass 3.3 verdict ✓✓ → ✓✓✓ on this single character via Eller addition; V-D Independent Audit V2 §"Audit Polarity Discipline" §2.1 confirms Eller substrate: published-work attribution (Eller *Uneven Ground* 2008; University Press of Kentucky) — substrate-safe per hard-rule discipline.

BR essay lineage anchors (verified by grep):
- §III: Pistor *Code of Capital* (2019) — six legal modules. Buchanan + Tullock + Mueller (Public Choice). Christophers *The Price is Wrong* (2024) — single-sentence reference.
- §V: Coates "The Case for Reparations" (2014); Darity + Mullen *From Here to Equality* (2020); Hamilton/Darity/Price/Sridharan/Tippett *Umbrellas Don't Make It Rain* (2015); Conley *Being Black, Living in the Red* (1999).
- §VI: Hartwick 1977; Norway GPFG; Pettit *Republicanism* (1997); Skinner *Liberty Before Liberalism* (1998); Parfit *Reasons and Persons* (1984).

`grep -i "uneven ground\|appalachi"` against BR essay.md returns **zero hits**; `grep -i "eller"` returns 2 hits, both substring-matches inside other words ("Mueller" at line 47; "seller" at line 77) — Ronald Eller as standalone author name does NOT appear. Eller; *Uneven Ground*; Appalachia all absent from BR essay as load-bearing references.

**Eller is not a BR-essay lineage anchor.** BR engages financial-capitalism (Mazzucato — note: BR essay does not explicitly cite Mazzucato by name either; Mazzucato grounds Ch 5 source's value-extraction discipline but the BR essay's compression carries it as "cost severance" plain-prose concept), legal-architecture (Pistor), political-economy-of-rent-seeking (Buchanan + Tullock + Public Choice), reparations-economics (Coates → Darity-Mullen → Hamilton → Conley), civic-republicanism (Pettit + Skinner + Parfit), and intergenerational-equity (Hartwick + Norway GPFG) lineages. Appalachian regional-history (Eller; Caudill; Stoll; Catte) is **Harper's-essay-exclusive** territory per the literary-essay-of-McDowell register.

**Required coordination: none.** Eller addition to V-D does not surface a coordination item for BR; BR's center-of-gravity lineages are different traditions entirely.

### §1.7 HC-2 / HC-3 / HC-4 / HC-5 / HC-6 / MC-4 V-D additions — shared-territory conflict check

**Verdict: NO COLLISION (all V-D additions are Harper's-essay-exclusive scope).**

V-D Independent Audit V2 §3 inventory of seven surgical hybridization candidates applied to LOCKED:

| V-D candidate | Site in V-D | Content | BR-essay shared territory? |
|---|---|---|---|
| **HC-1 Eller** (HIGH) | §V line 138 | Eller *Uneven Ground* 2008 attribution (~52w) | **No.** Per §1.6 above. |
| **HC-2 Yablonski wife+daughter** (MEDIUM) | §V line 140 | "after the murder, on the last night of 1969, of the reform candidate Joseph Yablonski and his wife and daughter" (~12w) | **No.** BR essay does not engage Miners for Democracy / Yablonski / UMWA history at any depth (verified via grep; zero hits for "yablonski\|miners for democracy\|umwa"). Harper's-essay-exclusive scope per Stage 1 brief §V regional-organizing-tradition crediting. |
| **HC-3 Farmington Mine 1968** (MEDIUM) | §IV line 108 | "The 1969 statute the program rests on was passed after the Farmington Mine disaster of November 1968 killed seventy-eight men" (~21w) | **No.** BR essay does not engage Farmington Mine disaster or the Federal Coal Mine Health and Safety Act enabling-history (verified via grep; zero hits for "farmington\|federal coal mine health and safety act"). |
| **HC-4 Federal Coal Mine Health and Safety Act** (LOW) | §IV line 104 | Statute name added (Public Law 91-173) (~5w) | **No.** Per HC-3. BR engages the federal Black Lung Benefits Program at §III line 45 institutional-measurement level only (excise-tax-funding + Trust-Fund-debt), not the statute's enabling-history. |
| **HC-5 Tug Fork** (LOW) | §I line 72 | Tug Fork geographic anchor at orange-creek scene (~12w) | **No.** BR essay does not engage McDowell geography. |
| **HC-6 Three rivers (Tug + Levisa + Guyandotte)** (LOW) | §VI line 158 | Three drainage systems at acid-mine-drainage paragraph (~13w) | **No.** Per HC-5. |
| **MC-4 1968 → 1969 wildcat strike** (MED) | §V line 140 | Fact-check correction (Derickson 1998 substrate) | **No.** BR essay does not engage Black Lung Association's wildcat-strike chronology (verified via grep; zero hits for "wildcat strike\|black lung association"). |

**All seven V-D candidates land in Harper's-essay-exclusive structural territory** (regional-scholarship lineage paragraph; McDowell-resident geographic-fluency anchors; coal-extraction regulatory-history; Appalachian organizing-tradition history). BR essay's structural moves (Libby lead case; Deepwater + 2008 + Social Security pattern-across-cases; Pistor + Public Choice + Christophers legal-architecture analysis; Restitution Bond + Foreclosure Bond two-instrument architecture) operate at a different scope-axis entirely. No content shares load-bearing prose surface between the two essays.

---

## §2. Aggregate verdict

**STATUS: NO-COLLISION-COHERENT-ACROSS-PORTFOLIO.**

All seven verification axes (scope distinction; BR McDowell-reference depth; instrument-name discipline; Bailey + Latusek non-engagement; numerical-anchor coherence; Eller non-coordination; HC-1 through HC-6 + MC-4 non-conflict) resolve to coherent + scope-distinct handling. No coordination items surfaced.

**Brief-level prediction confirmed.** Harper's brief §9.3 (line 387) declared *"Coherent. Ch 5 references McDowell at compression depth; Ch 2 → Harper's essay carries the full McDowell case at essay scope. No collision with Ch 5's BR-derivative scope (different chapter; different essay; different framing — BR is the institutional-measurement-of-bonds-architecture register; Harper's is the literary-essay-of-McDowell register)."* This audit verifies the prediction against the canonical end-user-facing prose on `origin/main` (BR essay.md; Harper's essay.md) AND against the V-D candidate state (Harper's `ch2-harpers-essay_hybrid_best-of-both.md`). The brief's call holds in both states.

**Whichever Harper's state ships** (LOCKED 7,121w essay.md currently RATIFIED on origin/main; or V-D 7,211w if ratified to canonical), the cross-portfolio coherence relative to the BR essay remains intact.

---

## §3. Items not in scope for this audit (forward-flag)

Per Harper's brief §9.6 flag-forward list, the following cross-essay coherence items are **separate verification workstreams** not addressed here:

1. **Numerical-anchor coherence between Atlantic Ideas Ch 9 essay + Harper's Ch 2 essay** (McDowell hook + 33-122× multiple framing) — flagged at brief §9.6 #4 + #4 + already verified at brief-level coherent per brief §9.4 Atlantic-Ideas-brief row. Submission-time re-verification advised if Ch 8 cascade-state updates between Atlantic Ideas Pass 3.1 RATIFIED (2026-05-24) and Harper's submission (Q4 2026 Oct-Nov window per cascade plan v2 Phase 2-β).
2. **Rights-register submission-time verification** — flagged at brief §9.6 #3. Per `publishing/essays/_pipeline/rights-register.md` current state, BR (Ch 5) + Harper's (Ch 2) are different chapter derivatives at low-conflict status. Re-verify at submission gate.
3. **Wave 1 Ch 8 McDowell op-ed scope** — flagged at brief §9.3 Ch 8 row + §9.6 #3. The op-ed format differential (short-form news-pegged) vs Harper's literary-essay differential (long-form Q4 2026 submission) keeps the two formats distinct; verify rights-register at op-ed submission time.
4. **Ch 10 PROPOSED → RATIFIED ripple risk** — flagged at brief §9.6 #2. Ch 10 ALT Stage 2 PROPOSED state at brief ratification time; if Ch 10 ratifies in ways that touch Harper's §VIII closing-return handling, re-verify the brief's §VIII structural decision.

---

## §4. Status one-liner

`STATE: cross-portfolio-BR-harpers-McDowell-collision NO-COLLISION; NEXT: none; AWAITING: none.`

---

*End of cross-portfolio coherence audit. PROPOSED 2026-06-01. Per CLAUDE.md merge-on-ratification scaffolding auto-merge default, this artifact (internal-scaffolding class) merges to origin/main at session close per the pre-push reconciliation pattern.*
