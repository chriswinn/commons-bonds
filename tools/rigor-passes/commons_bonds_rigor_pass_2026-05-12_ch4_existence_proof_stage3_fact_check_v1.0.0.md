# Stage-3 Rigor Pass — Chapter 4 (The Existence Proof) — Pass 1: Fact-check

**Date:** 2026-05-12
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A (per-chapter audits)
**Chapter:** 4 — *The Existence Proof*
**File audited:** [Chapter__4_THEEXISTENCEPROOF__Draft.md](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md)
**Word count:** ~3,975w (per workstream handoff)
**Pass scope:** Pass 1 (Fact-check) only. Pass 2 (Voice-polish) and Pass 3 (Audience-load) NOT run in this session — author scoped to fact-check only.
**Hard constraint observed:** No spot-fixes applied to chapter file. Phase C session (post-author-ratification) applies recommended edits.

---

## Canonical sources consulted

1. [_inventory_norway-mcdowell-canonical-facts_2026-05-10.md](publishing/op-eds/_inventory_norway-mcdowell-canonical-facts_2026-05-10.md) — Stage-1-equivalent canonical-facts inventory from op-ed pipeline (commit `5167edd`); GOLD STANDARD for Norway facts.
2. [norway-sovereign-wealth-op-ed_2026-05-10.md](publishing/op-eds/norway-sovereign-wealth-op-ed_2026-05-10.md) — Op-ed pipeline draft whose Stage-3 fact-check originally caught the GPFG founding-date and Bondevik-coalition-timing drifts.
3. [research/case-studies/norway-swf.md](research/case-studies/norway-swf.md) — Case-study brief (notably copied from Ch 4 itself per its 2026-04-22 housekeeping note; consistency check, not independent verification).
4. [research/case-studies/nigeria-oil-contrast.md](research/case-studies/nigeria-oil-contrast.md) — Niger Delta contrast-case brief.
5. [research/case-studies/alaska-permanent-fund.md](research/case-studies/alaska-permanent-fund.md) — Alaska Permanent Fund canonical brief.
6. [research/case-studies/social-security.md](research/case-studies/social-security.md) — US Social Security case-study brief.
7. [research/literature/bibliography.md](research/literature/bibliography.md) §13 — framework-adjacent literature (Hartwick, Mazzucato, Pistor, Christophers, Susskind, Darity & Mullen).
8. [research/audits/cross-chapter-consistency-audit_2026-05-11.md](research/audits/cross-chapter-consistency-audit_2026-05-11.md) — Item N-1 (Norway SWF AUM drift; ratified 2026-05-11 with Ch 4 as canonical $1.9T).
9. [tools/audits/cross-chapter-consistency-inventory_2026-05-11.md](tools/audits/cross-chapter-consistency-inventory_2026-05-11.md) — recurring-stats canonical row for Norway SWF AUM + per-citizen.

---

## Summary verdict

**No CRITICAL findings.** The two specific drifts the workstream handoff flagged for verification — GPFG founding-date precision (1990 vs. 2006 rename conflation) and Bondevik-coalition timing — are **NOT** present in Ch 4. The op-ed pipeline's Stage-3 catch did not propagate as a regression.

| Severity | Count | Disposition |
|---|---|---|
| CRITICAL | 0 | — |
| HIGH | 0 | — |
| MEDIUM | 5 | Spot-fix recommended (author-ratify) |
| LOW | 3 | Verification flags / pre-publication refresh |

**Aggregate verdict:** **READY AFTER SPOT-FIXES** (Pass 1 only). MEDIUM findings tighten precision in places where canonical sources support a sharper claim than Ch 4 currently makes; none are factual errors of the kind a publisher fact-checker would block on. Voice-polish + audience-load passes still required for full Phase A completion.

---

## Findings

### MEDIUM-1: GPFG rename year (2006) not anchored in Ch 4 prose

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:21](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:21)

**Chapter text:**
> "...culminating in the formal establishment of the Government Petroleum Fund in 1990 (later renamed the Government Pension Fund Global)..."

**Canonical truth (op-ed canonical-facts inventory, line 23):**
> "Government Petroleum Fund formally established 1990. Renamed Government Pension Fund Global (GPFG) in 2006."

**Why this is the MEDIUM-1 finding:** The 1990 founding date is correctly anchored — this is the part the prior op-ed Stage-3 caught when its earlier draft conflated rename with founding, and Ch 4 has it right. But the rename year (2006) is dropped to a parenthetical "later renamed" without a year. For an existence-proof chapter that leans on Norway's institutional-design *chronology* as load-bearing evidence, the asymmetry is mild but visible — the founding gets a year, the rename does not. Op-ed inventory standardizes both. A fact-checker reading Ch 4 against the op-ed inventory would note the asymmetry.

**Recommended spot-fix:** Add the rename year inside the parenthetical.
```
(later renamed the Government Pension Fund Global in 2006)
```

**Severity rationale:** MEDIUM not HIGH because the underlying facts are correct; MEDIUM not LOW because parallel-structure precision is the standard the op-ed pipeline and case-study brief have set, and Ch 4 is the canonical existence-proof chapter.

---

### MEDIUM-2: Bondevik coalition disambiguation (Bondevik II not specified)

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:29](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:29)

**Chapter text:**
> "The 2001 fiscal rule was adopted under a Labour-led government (Jens Stoltenberg's first ministry) and has held through every administration since: Bondevik's center-right coalition, Stoltenberg's second Labour government, Solberg's Conservative coalition, Støre's subsequent Labour-Centre coalition."

**Canonical truth:** The Norwegian PM Bondevik (Kjell Magne Bondevik) led two distinct coalitions: **Bondevik I** (KrF/Sp/V, October 1997 – March 2000, *centrist*) immediately preceded Stoltenberg I; **Bondevik II** (KrF/V/H, October 2001 – October 2005, *centre-right*) immediately followed Stoltenberg I. The chapter's "every administration since" framing makes Bondevik II the unambiguous referent in context — Bondevik II is the centre-right coalition that succeeded the rule's adopter. So the *sequence* is correct (this is what the op-ed Stage-3 caught and corrected — the original op-ed had Bondevik out of sequence). What Ch 4 omits is the disambiguator that Bondevik headed two coalitions of different political character.

**Why this is the MEDIUM-2 finding:** A reader who knows Norwegian political history (a non-trivial subset of the policy-press audience the chapter targets) will parse "Bondevik's center-right coalition" and momentarily wonder whether the chapter has conflated I and II. The "center-right" qualifier *does* disambiguate (Bondevik I was centrist; Bondevik II was centre-right) — but only for readers who track that distinction. Adding "II" or a temporal marker forecloses the ambiguity for the broader audience.

**Recommended spot-fix:** Tighten to either:
- Option A (numeral disambiguator): `Bondevik II's center-right coalition`
- Option B (temporal disambiguator): `the center-right coalition that succeeded it under Bondevik`
- Option C (no edit): if the author's judgment is that "center-right" is a sufficient disambiguator for the trade audience, defensibly hold as-is.

**Severity rationale:** MEDIUM not HIGH because the sequencing is correct (the prior op-ed drift is NOT replicated). MEDIUM not LOW because this is the second-flagged drift in the workstream handoff — the audit emphasis specifically calls out "Bondevik-coalition timing" — and a politically-literate fact-checker would query.

---

### MEDIUM-3: UNEP 2011 Ogoniland cleanup figure — "$1 billion" framing oversimplified

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:79](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:79)

**Chapter text:**
> "...documented by the United Nations Environment Programme in a 2011 report whose conclusions have not been seriously contested. The UNEP report estimated that comprehensive cleanup of Ogoniland alone would cost on the order of one billion dollars and require thirty years of sustained remediation..."

**Canonical truth:** UNEP (2011), *Environmental Assessment of Ogoniland*: the $1 billion figure was the recommended **initial capital injection for the proposed Ogoniland Environmental Restoration Authority covering the first five years of operations** — not the total cleanup cost. Total restoration was projected at 25–30 years, with implied total costs significantly higher than $1B (subsequent estimates from civil-society groups and NGOs have ranged into the multi-billions). The op-ed canonical-facts inventory (line 44) phrases it as "Ogoniland cleanup alone at ~$1 billion and ~30 years," which carries the same simplification.

**Why this is the MEDIUM-3 finding:** Ch 4's "comprehensive cleanup... on the order of one billion dollars" reads as a total-cost figure when the canonical UNEP recommendation was specifically an initial-capitalization figure. A Niger Delta or environmental-policy specialist reader will catch this. The simplification is widely-cited in popular press (so not unique to Ch 4), but the trade-press audience the chapter targets includes readers who will recognize the gap.

**Recommended spot-fix:** Tighten to make the $1B figure scope-explicit:
```
The UNEP report estimated that initial capitalization of an Ogoniland Environmental Restoration Authority would require on the order of one billion dollars, with full restoration projected to require twenty-five to thirty years of sustained remediation; subsequent monitoring suggests cleanup progress has remained well short of that timeline...
```

**Severity rationale:** MEDIUM not HIGH because the underlying claim (UNEP 2011, ~$1B figure, ~30 years, slow actual progress) tracks the report; MEDIUM not LOW because the precision distinction (initial capitalization vs. total cleanup cost) is the kind of thing a publisher pre-publication-review fact-checker will query.

---

### MEDIUM-4: Alaska Permanent Fund founding year — "established the same year" (1976) glosses 1976→1977 distinction

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:9](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:9)

**Chapter text:**
> "Alberta's Heritage Trust Fund, established in 1976, was the closest North American attempt at the Norwegian model... Alaska's Permanent Fund, established the same year, captured petroleum royalties for distribution as annual citizen dividends..."

**Canonical truth:** Per [research/case-studies/alaska-permanent-fund.md](research/case-studies/alaska-permanent-fund.md) §2: "In November 1976, Alaska's voters approved the amendment by a roughly 75%-25% margin. **The Permanent Fund was established in 1977.** The Permanent Fund Dividend Program — direct annual distribution to each Alaska resident from the fund's earnings — was added in **1982**." The op-ed canonical-facts inventory (line 43) says "Alaska Permanent Fund (founded **1976** as well)" — so there is an *internal-source disagreement* between the case-study brief (1977 fund establishment) and the op-ed inventory (1976 founding).

**Why this is the MEDIUM-4 finding:** Strictly canonical, the constitutional amendment was 1976; the fund itself was established 1977; the dividend distribution started 1982. Ch 4's "established the same year" as Alberta (1976) compresses three distinct events into one, leaning on the constitutional-amendment date. Defensible loose-but-not-wrong — but a fact-checker familiar with Alaska's record will note the slip. The chapter's downstream claim that Alaska's fund "captured petroleum royalties for distribution as annual citizen dividends" is also slightly compressed: the dividend program is a 1982 add-on, not part of the 1976/1977 architecture.

**Recommended spot-fix:** Two options.
- Option A (precision): `Alaska's Permanent Fund, approved by voters the same year and operational from 1977, captured petroleum royalties for distribution as annual citizen dividends from 1982 onward...`
- Option B (preserve compression with hedging): `Alaska's Permanent Fund, established in the same period, eventually distributed petroleum royalties as annual citizen dividends...`
- Option C (resolve internal-source disagreement first): author ratifies whether canonical for the book's Alaska references is "1976" (constitutional amendment, op-ed inventory) or "1977" (fund operational, case-study brief). Currently both are cited differently across the corpus; this should be locked.

**Severity rationale:** MEDIUM because the underlying claim (Alaska built a different architecture than Norway, around the same time) is solid; the precision question is internal-corpus consistency, not a fact error.

**Cross-corpus follow-on:** The 1976/1977 ambiguity should be resolved in the next cross-chapter consistency sweep — neither Ch 4, the op-ed inventory, nor the case-study brief currently agree.

---

### MEDIUM-5: Bismarck-Germany "funded elements survived into the early twentieth century" — vague

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:101](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:101)

**Chapter text:**
> "Variations of the funded architecture had been proposed and partially implemented in other jurisdictions, including Bismarck's Germany, where some funded elements survived into the early twentieth century."

**Canonical truth:** Bismarck's social insurance system comprised three laws: **1883** Sickness Insurance, **1884** Accident Insurance, **1889** Old Age & Disability Insurance. The Old Age & Disability Insurance had partially funded elements in its early decades (capital reserves accumulated against future obligations). The reserves were destroyed largely by **WWI / Weimar hyperinflation** (peak 1923), after which the system pivoted to a fully pay-as-you-go basis. The funded elements thus "survived" until roughly 1923 — defensibly "the early twentieth century" but the chapter's framing is loose.

**Why this is the MEDIUM-5 finding:** The chapter sentence is the only deep-history-citation in the Social Security comparator passage and it does load-bearing work for the "1935 designers had alternative templates available" argument. A historian-of-pensions reader will want either (a) a tighter date (e.g., "until the post-WWI hyperinflation destroyed the reserves in 1923") or (b) a specific cite. As currently phrased, the sentence is correct but the reader cannot anchor it.

**Recommended spot-fix (author judgment which to apply):**
- Option A (date-tightened): `...Bismarck's Germany, where the partially-funded character of the 1889 Old Age and Disability Insurance system survived until the post-WWI hyperinflation of the early 1920s.`
- Option B (citation-tightened): retain prose as-is, add an endnote citing specifically to a German social-insurance history (e.g., Hentschel, Skocpol, or a specialist work).
- Option C (compression for trade-prose): preserve loose phrasing as fits the chapter's voice; accept the precision tradeoff.

**Severity rationale:** MEDIUM because the claim is accurate and the precision gap is small; not LOW because the chapter is a publisher-facing manuscript and Bismarck-era social-insurance history is well-documented enough that vagueness reads as authorial uncertainty rather than authorial choice.

---

### LOW-1: Ekofisk discovery date — "three days before Christmas" precision (Dec 22 vs canonical Dec 23)

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:7](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:7)

**Chapter text:**
> "In 1969, three days before Christmas, a drill bit in the North Sea struck oil on a Norwegian concession called Block 2/4."

**Canonical truth:** Sources vary. The Norwegian Petroleum Directorate dates the Ekofisk discovery to **23 December 1969** (the night before Christmas Eve). Equinor's official corporate history dates it to **Christmas Eve 1969 (Dec 24)**. Some Phillips Petroleum / ConocoPhillips historical records place initial oil-strike testing at **Dec 22**. "Three days before Christmas" = Dec 22; this is consistent with the earliest Phillips-internal date but not with the most-cited Norwegian governmental and Equinor-corporate dates.

**Why this is the LOW-1 finding:** The canonical-facts inventory (op-ed pipeline gold standard) accepts "three days before Christmas," so this phrasing is internally locked across the corpus. Author has settled on it. A fact-checker familiar with NPD or Equinor canonical dating may query; the underlying claim (Ekofisk was discovered just before Christmas 1969) is unimpeachable. Sources support Dec 22-24, depending on which event (oil-show, oil-strike confirmation, or commercial-discovery announcement) is being dated.

**Recommended action (author judgment):**
- Option A (no change): hold per canonical-facts inventory.
- Option B (hedge): `In 1969, just before Christmas, a drill bit in the North Sea struck oil...` — loses the specific "three days" texture but forecloses the precision query.
- Option C (precision per NPD): `In late December 1969, a drill bit in the North Sea struck oil...` — most defensible against any source variation.

**Severity rationale:** LOW because (a) the canonical-facts inventory has accepted "three days before Christmas," (b) the underlying claim is unimpeachable, (c) sources vary so the chapter's date is defensible against at least one canonical version. Flagged for awareness, not for required fix.

---

### LOW-2: Time-sensitive figures — pre-publication refresh required

**Locations:**
- [Chapter__4_THEEXISTENCEPROOF__Draft.md:23](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:23) — "more than one and nine-tenths trillion dollars in assets" + "roughly three hundred and forty thousand dollars" per citizen
- [Chapter__4_THEEXISTENCEPROOF__Draft.md:25](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:25) — "roughly three percent" expected real return
- [Chapter__4_THEEXISTENCEPROOF__Draft.md:45](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:45) — "seventy to eighty cents of every dollar of net petroleum wealth"

**Canonical truth (as of May 2026):** All accurate per op-ed canonical-facts inventory (commit `5167edd`, 2026-05-10). Cross-chapter consistency audit Item N-1 ratified the $1.9T figure as Ch 4 canonical (Ch 6 conformed via commit `9695b67`). The 3% expected-real-return reflects the 2017 downward revision from the original 4% (handlingsregelen).

**Why this is the LOW-2 finding:** GPFG AUM crossed $1.9T in mid-2025 and has been moving through the $1.7-2.0T range with market conditions; per-citizen figure derives directly from AUM ÷ population so moves with AUM. The expected-real-return rate is a policy parameter that can be revised again. The 70–80% state-capture rate is structural (78% effective petroleum tax + state ownership economics) and stable. **None of these need spot-fix now**; flag for pre-publication refresh pass (likely Q3 2026 or whenever the manuscript moves to copyedit).

**Recommended action:** No fix in Phase C. Add to a pre-publication-refresh checklist owned by the author. The cross-chapter consistency inventory ([tools/audits/cross-chapter-consistency-inventory_2026-05-11.md](tools/audits/cross-chapter-consistency-inventory_2026-05-11.md) line 247: "A statistic is updated (e.g., Norway SWF AUM moves materially)") already lists this as a re-trigger criterion; this finding extends that to expected-real-return + state-capture rate.

**Severity rationale:** LOW because the figures are accurate now; flagged because they will need verification at copyedit.

---

### LOW-3: Equinor / Statoil rename year not anchored

**Location:** [Chapter__4_THEEXISTENCEPROOF__Draft.md:23](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:23)

**Chapter text:**
> "...direct ownership of Equinor (formerly Statoil, the national oil company)..."

**Canonical truth:** Statoil renamed to Equinor on **16 May 2018** to reflect strategic diversification beyond pure oil-and-gas. The chapter's parenthetical correctly notes the rename but doesn't anchor the year — same asymmetry as MEDIUM-1 (GPFG rename), but lower-severity here because Equinor as an entity is less load-bearing in the chapter than GPFG.

**Why this is the LOW-3 finding:** Pure parallel-structure consistency with MEDIUM-1. If author ratifies adding "in 2006" to the GPFG rename parenthetical, consider also adding "in 2018" to the Equinor parenthetical for consistent treatment of corporate-rename anchoring. If MEDIUM-1 is held as-is, this is held as-is.

**Recommended action:** Coupled to MEDIUM-1. If MEDIUM-1 fix is ratified, add `(formerly Statoil, the national oil company, renamed in 2018)`. Otherwise no action.

**Severity rationale:** LOW because Equinor's rename is well-known business news and a reader unfamiliar with it will not be misled.

---

## Items verified — no findings (positive verifications)

The following claims were verified against canonical sources and require no spot-fix. Listed here so author can see the audit coverage.

| Claim | Location | Verification |
|---|---|---|
| 1969 Ekofisk discovery, North Sea, Block 2/4, Norwegian concession | Ch 4:7 | ✓ per canonical-facts inventory |
| Norway "fewer than four million people" at the time | Ch 4:7 | ✓ Norway population ~3.9M in 1969 |
| Government Petroleum Fund formally established 1990 | Ch 4:21 | ✓ per inventory + bibliography Hartwick entry |
| Fund invests outside Norway, diversified equities/bonds/real estate | Ch 4:23 | ✓ per inventory + actual GPFG strategy |
| 2001 fiscal rule (handlingsregelen) adopted under Stoltenberg I | Ch 4:29 | ✓ Stoltenberg I = March 2000 – October 2001; rule via St.meld. nr. 29 (2000-2001), March 2001 |
| Government chronology sequence: Stoltenberg I → Bondevik → Stoltenberg II → Solberg → Støre | Ch 4:29 | ✓ all sequencing correct (the prior op-ed drift NOT replicated here) |
| Stoltenberg's second Labour government | Ch 4:29 | ✓ Stoltenberg II (October 2005 – October 2013), Labour-led red-green coalition |
| Solberg's Conservative coalition | Ch 4:29 | ✓ Solberg (October 2013 – October 2021), Conservative-led |
| Støre's Labour-Centre coalition | Ch 4:29 | ✓ Støre (October 2021 – present), Labour + Centre Party |
| GPFG AUM "more than $1.9 trillion" | Ch 4:23 | ✓ Cross-chapter audit Item N-1 ratified Ch 4 as canonical 2026-05-11 |
| ~$340K per citizen | Ch 4:23 | ✓ ($1.9T ÷ ~5.55M population ≈ $342K) |
| Investment returns now exceed extraction revenue | Ch 4:27 | ✓ per multi-year GPFG annual reports |
| Alberta Heritage Trust Fund established 1976 | Ch 4:9 | ✓ Alberta Heritage Savings Trust Fund Act 1976 |
| Nigeria major oil producer since 1950s | Ch 4:77 | ✓ Oloibiri discovery 1956; commercial production from 1958 |
| Niger Delta operators: Shell, Chevron, ExxonMobil, Total | Ch 4:77 | ✓ historical operators (note recent divestitures by Shell + ExxonMobil; historical claim accurate) |
| UNEP 2011 report on Ogoniland (existence + non-contestation) | Ch 4:79 | ✓ *Environmental Assessment of Ogoniland*, UNEP 2011 |
| Ken Saro-Wiwa hanged 1995 | Ch 4:79 | ✓ executed 10 November 1995 (Ogoni Nine) |
| Nigeria temporarily suspended from Commonwealth post-1995 executions | Ch 4:79 | ✓ suspended 11 November 1995; reinstated May 1999 |
| US Social Security designed 1935 | Ch 4:99 | ✓ Social Security Act signed 14 August 1935 |
| US Social Security pay-as-you-go architecture, trust-fund as intra-government accounting record | Ch 4:95 | ✓ per [social-security.md](research/case-studies/social-security.md) §"The Structural History" |
| Climate-vulnerable populations: Bangladesh, Sahel, Pacific island states | Ch 4:117 | ✓ standard climate-vulnerability typology |

---

## Apparatus regression check (per Phase A hard constraints)

Verified that Ch 4 does **NOT** introduce framework apparatus terms that were ratified to drop from publisher-facing prose, per [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md).

Apparatus terms appearing in Ch 4 prose (all permitted in this analytical chapter per the apparatus register):
- "cost severance" — permitted lowercase prose phrase per Insight #61 / WP retirements; appears appropriately as Ch 4 builds toward formal apparatus introduction in Ch 5/6
- "accountability bond B" — permitted; introduced earlier in Ch 5 progression; Ch 4 uses correctly
- "residual commons value" — permitted lowercase prose; Ch 4 uses correctly
- "foreclosure component" / "externality tail" — permitted plain-language; not used as named-apparatus in Ch 4
- "Intergenerational Option Value" — single capitalized usage at Ch 4:121; this is the Ch 4 introduction site of the term; correct register

**No apparatus regression detected.**

---

## Path B contamination check

Verified Ch 4 does NOT carry verbatim-clone passages from other chapters. The case-study brief at [research/case-studies/norway-swf.md](research/case-studies/norway-swf.md) is *copied from Ch 4* (per its 2026-04-22 housekeeping note), so identity-text overlap with that file is expected and correct (Ch 4 is the source). No detectable text-clones from Ch 5, Ch 6, Ch 8, or Ch 9.

---

## Named-subject consent check

No living named subjects in Ch 4. Norwegian PMs (Stoltenberg, Bondevik, Solberg, Støre) named in their official capacity as office-holders (standard journalistic practice; no consent issue per [feedback_named_subject_consent.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_named_subject_consent.md)). Ken Saro-Wiwa is deceased (named with historical-record status). No named McDowell or Niger Delta residents; Ogoni and Ijaw named as peoples not as individuals.

**No named-subject consent issues.**

---

## Recommendations to PM session + author

**For author ratification (Phase C inputs):**

1. **MEDIUM-1 — GPFG rename year (2006).** Recommend RATIFY: adds 4 words; tightens parallel structure with the 1990 founding date.
2. **MEDIUM-2 — Bondevik II disambiguation.** Author judgment between Options A/B/C. Recommend Option A (numeral disambiguator) — minimal-prose-change + maximum-clarity.
3. **MEDIUM-3 — UNEP $1B framing.** Recommend RATIFY: tightens to scope-explicit phrasing without adding much prose; forecloses fact-checker query.
4. **MEDIUM-4 — Alaska 1976/1977.** Author judgment — but flag the **internal-source disagreement** between op-ed inventory (1976), case-study brief (1977), and Ch 4 (implicitly 1976) for cross-corpus resolution in next consistency sweep, regardless of how Ch 4 itself is treated.
5. **MEDIUM-5 — Bismarck-Germany.** Author judgment between Options A/B/C. Lowest priority of the MEDIUM-tier; can defer to Phase B (whole-book) audit.
6. **LOW-1 — Ekofisk Dec 22/23/24.** Author judgment. Likely "no change" given canonical-facts inventory has settled on "three days before Christmas."
7. **LOW-2 — Time-sensitive figures.** Defer to pre-publication refresh checklist; no Phase C fix.
8. **LOW-3 — Equinor 2018 rename year.** Couple to MEDIUM-1 disposition.

**For PM session:**
- Pass 2 (Voice-polish) and Pass 3 (Audience-load) for Ch 4 still required to complete Phase A coverage of this chapter. Schedule per pacing plan.
- The cross-corpus 1976/1977 Alaska Permanent Fund founding-year ambiguity (MEDIUM-4) should be added to the cross-chapter consistency inventory as a recurring-stat row to lock canonical for all chapters that reference it.

---

*End of Pass 1 (Fact-check) for Chapter 4. Pass 2 + Pass 3 deliverables to be produced in subsequent sessions per workstream #20 phasing.*

---

## Ratification record (closed 2026-05-12)

Author ratification: **All 5 MEDIUM findings RATIFIED as recommended** (2026-05-12 same-session). LOW findings unratified; remain as pre-publication / awareness items.

Phase C application — single atomic chunk applied 2026-05-12 in same session per WP#9 worktree workflow:

1. ✅ **MEDIUM-1 (Ch 4 line 21):** Ratified — added "in 2006" to GPFG rename parenthetical. Applied.
2. ✅ **MEDIUM-2 (Ch 4 line 29):** Ratified — "Bondevik's" → "Bondevik II's" (Option A: numeral disambiguator). Applied.
3. ✅ **MEDIUM-3 (Ch 4 line 79):** Ratified — UNEP $1B sentence rewritten to scope-explicit "initial capitalization of an Ogoniland Environmental Restoration Authority" + "twenty-five to thirty years" duration. Applied.
4. ✅ **MEDIUM-4 (Cross-corpus, NOT Ch 4):** Ratified — case-study brief [research/case-studies/alaska-permanent-fund.md](research/case-studies/alaska-permanent-fund.md) §2 updated to anchor 1976 as canonical (operational 1977); cross-chapter consistency inventory [tools/audits/cross-chapter-consistency-inventory_2026-05-11.md](tools/audits/cross-chapter-consistency-inventory_2026-05-11.md) Alaska row updated with 1976 canonical lock + Ch 4 reference site added. Ch 4 unchanged per recommendation. Applied.
5. ✅ **MEDIUM-5 (Ch 4 line 101):** Ratified — Bismarck-Germany sentence tightened to anchor "1889 Old Age and Disability Insurance system" + "post-WWI hyperinflation of the early 1920s" (Option A: date-tightened). Applied.

LOW items (initial state — see follow-up below):
- LOW-1 (Ekofisk Dec 22/23/24): initially HOLD; subsequently ratified for canonical-facts-inventory footnote (see follow-up).
- LOW-2 (Time-sensitive figures): deferred to pre-publication refresh; recommendation is to extend the cross-chapter consistency inventory at next revision rather than create a new file.
- LOW-3 (Equinor 2018 rename): coupled to MEDIUM-1 in original recommendation; subsequently ratified after MEDIUM-1 landed and made the Equinor-parenthetical asymmetry visible (see follow-up).

**LOW-1 + LOW-3 ratified follow-up (2026-05-13):**

After MEDIUM landed and the LOW items were re-evaluated, author ratified LOW-1 + LOW-3 (LOW-2 held per recommendation). Applied as small follow-up commit:

- ✅ **LOW-3 (Ch 4 line 23):** Equinor parenthetical updated to "(formerly Statoil, the national oil company, renamed in 2018)". Completes the corporate/institutional-rename anchoring symmetry alongside MEDIUM-1's GPFG 2006 anchor.
- ✅ **LOW-1 (canonical-facts inventory line 19):** Source-variation footnote added at [_inventory_norway-mcdowell-canonical-facts_2026-05-10.md:19](publishing/op-eds/_inventory_norway-mcdowell-canonical-facts_2026-05-10.md:19) documenting Phillips Dec 22 / NPD Dec 23 / Equinor Dec 24 source split, with "three days before Christmas" locked as corpus phrasing. Pure internal scaffolding (per WP#10); prevents future Stage-3 sessions from re-litigating.
- ⏸ **LOW-2 (time-sensitive figures):** held; recommendation is to extend the cross-chapter consistency inventory at next revision rather than create a new pre-publication-refresh file.

**Phase C complete for Ch 4 Pass 1 ratifications (5 MEDIUM + 2 LOW applied).** Pass 2 (Voice-polish) + Pass 3 (Audience-load) still required for full Phase A completion of this chapter.
