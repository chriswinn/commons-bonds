---
artifact: Workstream A execution audit on the McDowell op-ed V-D canonical swap (commit `189f42b`)
date: 2026-06-01
session: fresh CC chip (Read+Write only; canonical path `/Users/c17n/commons-bonds/`)
audit_target: commit `189f42b` on `origin/main` — claimed to perform the V-D HYBRID canonical swap
status: PROPOSED 2026-06-01
verdict_top_line: **REVERT-AND-REWORK — the V-D canonical swap was NOT executed.** The canonical `op-ed.md` retains the LOCKED 2026-05-10 prose verbatim; no V-D HYBRID body content reached the canonical file; the LOCKED archive directory does not exist; the README was not updated.
---

# Workstream A Execution Audit — McDowell op-ed V-D Canonical Swap (commit `189f42b`) — 2026-06-01

## §0. Methodological framing

This audit is an independent incremental verification audit on Workstream A of the 2026-06-01 McDowell op-ed ratified bundle: the claimed V-D HYBRID canonical swap at commit `189f42b` on `origin/main`. The audit is **NOT** re-auditing the V-D HYBRID prose itself (which has been triple-audited per the drafter's-self-audit + prior independent audit + fresh three-pass independent audit, all in `_archive/parallel-drafts_2026-05-28/`). The scope is the **execution of the swap** — body byte-equality, LOCKED archive correctness, frontmatter prose, README prose, and §2.1 hard-rule re-confirmation.

**Independence.** Fresh chip; no prior context on Workstream A's execution. The body byte-equality check is the load-bearing axis because if it fails, the swap simply did not happen, and downstream frontmatter / README / archive checks become moot pending a corrective swap.

**Permission constraint observed.** All reads at canonical path `/Users/c17n/commons-bonds/`. No Bash invoked; Read + Write only.

---

## §1. Body byte-equality verification (op-ed.md body vs V-D HYBRID body)

### §1.1 Result top-line

**FAIL — body prose is NOT V-D HYBRID. The canonical `op-ed.md` body is the LOCKED 2026-05-10 prose verbatim.**

The V-D HYBRID canonical swap claimed by commit `189f42b` was NOT executed at the body-prose level.

### §1.2 Evidence — paragraph-by-paragraph diff against V-D HYBRID source

Direct comparison of canonical `publishing/op-eds/mcdowell-county-true-cost/op-ed.md` body (lines 19–39, between LEDE comment and sign-off) vs V-D HYBRID body at `_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_hybrid_best-of-both.md` (lines 51–73):

| Paragraph | Canonical op-ed.md (line) | V-D HYBRID source (line) | Match? | Diagnosis |
|---|---|---|---|---|
| LEDE opener | "The argument over what energy 'really costs' tends to surface in policy debates whenever an agency revises a number, a company files for bankruptcy, or a coal-region community appears in the headlines..." (line 21) | "Every few years, an argument resurfaces in U.S. policy about what energy actually costs. It tends to arrive when an agency revises a number, a coal company files for bankruptcy, or an Appalachian community lands in headlines..." (line 55) | **NO** | Canonical retains LOCKED conditional opener; V-D adopted the ALT-NORM-PUNCT sharper declarative opener. |
| Nut graf | Preserved nut-graf rhetorical signature ("It was paid, in lungs and watersheds..."); content matches but flows from LOCKED's opener (line 25) | Same rhetorical signature; flows from V-D's opener (line 59) | partial | Nut-graf signature is preserved across both; both versions inherited it from LOCKED. Not diagnostic alone. |
| McDowell graf | "The county where this is most visible is McDowell County, West Virginia... By 2020, fewer than 20,000 remained. The U.S. Steel mine closure in 1990 cut personal income... The last Walmart left in 2016." (line 27) | "McDowell County, West Virginia, is where the gap is most visible... When President Kennedy campaigned through the West Virginia primary in 1960, McDowell led the nation in coal production and its residents queued for federal surplus food. Mechanization cut the mining workforce by more than half within a decade. When U.S. Steel closed its McDowell mine in 1990, personal income across the county fell by two-thirds in a single year." (line 61) | **NO** | Canonical lacks the V-D substrate-expansion additions: Kennedy 1960 visit + federal surplus food queue + mechanization-cut-workforce sentence + active-voice U.S. Steel construction. Canonical retains LOCKED's Walmart 2016 datum (V-D dropped it per news-peg-activation template). |
| BLDTF graf | "Walk through what was left blank. The Black Lung Disability Trust Fund... has distributed more than $44 billion since its creation. It has never collected enough revenue to meet its obligations. The fund's debt stood at $4.5 billion in 2021 and is projected to exceed $15 billion by 2050. Bankruptcy by a coal-producing company moves the unpaid black-lung obligations onto the public balance sheet..." (line 29) | "Begin with what was left blank. The Black Lung Disability Trust Fund... has distributed more than $44 billion since Congress established it in 1969... Black lung was identifiable as an occupational disease early in the twentieth century; federal compensation came only in 1969, after a wildcat strike led by the West Virginia Black Lung Association forced the issue. The United Mine Workers under John L. Lewis had declined to press it earlier." (line 63) | **NO** | Canonical opens "Walk through what was left blank" (LOCKED) vs V-D's "Begin with what was left blank" (adopted from ALT-NORM-PUNCT). Canonical LACKS the entire V-D historical-anchor addition: 1969 establishment context + WVBLA wildcat-strike origin + UMW-under-Lewis prior-decline. This is the most distinctive V-D substrate addition; its absence is dispositive evidence the swap did not execute. |
| SMCRA graf | "Walk outside the mine and the same arithmetic continues..." (line 31) | "The arithmetic continues at the surface..." (line 65) | **NO** | Canonical retains LOCKED's "Walk outside the mine" framing; V-D adopted the ALT-NORM-PUNCT "The arithmetic continues at the surface" reframing. |
| Carbon graf | "The Environmental Protection Agency's most recent estimate of what each ton of CO₂ costs the world — what economists call the social cost of carbon, anchored to a 2022 *Nature* meta-analysis and adopted in the 2023 EPA update — is $190." (line 33) | "The Environmental Protection Agency's most recent estimate of what each ton of CO₂ costs the world, the social cost of carbon, is $190, anchored to the Rennert et al. 2022 *Nature* meta-analysis and adopted in the EPA's 2023 update." (line 67) | **NO** | Canonical retains LOCKED phrasing with em-dash parenthetical + anonymous "a 2022 *Nature* meta-analysis"; V-D adopted comma-restructure + explicit "Rennert et al. 2022 *Nature*" attribution. This is the inline-citation gain V-D's audits scored as the FT/Bloomberg analyst-level credibility lift; it is absent from canonical. |
| Three-responses graf | Three responses preserved; flows from LOCKED-version context (line 35) | Three responses preserved; flows from V-D context (line 69) | partial | Both preserve the LOCKED conversational rhythm. Not diagnostic. |
| Call graf | "The policy question facing the United States now is whether to continue treating these numbers as theoretical. The social cost of carbon has been revised four times by four administrations on grounds that have less to do with carbon physics than with which side of the political fight had more resources at the moment of revision. The Black Lung Trust Fund's structural deficit will not close itself..." (line 39) | "The policy question now is whether to keep treating these numbers as theoretical. The social cost of carbon has been revised four times by four administrations on grounds that have less to do with carbon physics than with which side of the political fight had more resources at the moment. The Obama-era figure of $42 per ton was cut to $1–7 under the Trump administration by restricting the externality calculation to U.S. borders — a methodological change Wagner, Anthoff, Cropper, and colleagues flagged in 2021 as ungrounded in standard cost-benefit practice. The Biden administration restored the global-scope methodology; the EPA's 2023 update raised the figure to $190..." (line 73) | **NO** | Canonical LACKS the entire V-D SCC variance enumeration ($42 Obama → $1–7 Trump → restoration → $190 EPA) + the Wagner/Anthoff/Cropper inline citation. This is the most distinctive V-D call-graf substrate addition; its absence is also dispositive. |

### §1.3 Body byte-equality verdict

**FAIL.** The canonical op-ed.md body matches the LOCKED 2026-05-10 prose verbatim (with the well-known LOCKED em-dash density and structural choices). It does NOT match the V-D HYBRID prose at the load-bearing distinctive sites:

- LEDE opener: LOCKED conditional, not V-D declarative.
- McDowell graf: LOCKED 6-sentence structure, not V-D 7-sentence Kennedy+mechanization+active-voice-U.S.-Steel expansion.
- BLDTF graf: LOCKED 5-sentence structure, not V-D 6-sentence WVBLA+Lewis historical anchor expansion.
- Carbon graf: anonymous "a 2022 *Nature* meta-analysis" not V-D's "Rennert et al. 2022 *Nature*" inline attribution.
- Call graf: LOCKED's no-inline-SCC-numbers call, not V-D's $42/$1–7/$51/$190 variance enumeration + Wagner/Anthoff/Cropper inline citation.

**The V-D HYBRID canonical swap claimed by commit `189f42b` was NOT executed at the body-prose level.**

### §1.4 Em-dash count on canonical body — cross-check

Counting em-dashes in canonical op-ed.md body (lines 21–39):

- Line 25 (nut graf): 2 em-dashes / 1 site (parenthetical "— once health damage, environmental destruction, community collapse, and atmospheric carbon are priced honestly —")
- Line 29 (BLDTF graf): 1 em-dash / 1 site ("— which is to say, onto everyone who isn't currently extracting coal.")
- Line 31 (SMCRA graf): 1 em-dash / 1 site ("— a shortfall of three and a half to six billion dollars sitting unfunded in the federal ledger.")
- Line 33 (carbon graf): 2 em-dashes / 1 site (parenthetical "— what economists call the social cost of carbon, anchored to a 2022 *Nature* meta-analysis and adopted in the 2023 EPA update —")
- Line 35 (three-responses graf): 1 em-dash / 1 site ("— primarily as obligations of the jurisdictions that benefited from the routing, not as new burdens on jurisdictions still industrializing.")

**Total: 7 em-dash characters / 5 sites.** This matches LOCKED's reported "~6 em-dashes" baseline (V-D frontmatter line 6 of `mcdowell-op-ed_hybrid_best-of-both.md` says LOCKED was 1,024w body / ~6 em-dashes); it does NOT match V-D's reported "3 chars / 2 sites" (frontmatter line 22). Em-dash count corroborates §1.2's paragraph-diff finding: canonical is LOCKED, not V-D.

### §1.5 Word count on canonical body — cross-check

Word count of canonical op-ed.md body (between LEDE HTML comment line 19 and sign-off line 43, excluding HTML-comment markers + sign-off):

By paragraph counting:
- LEDE graf (line 21): ~110 words
- Nut graf (line 25): ~115 words
- McDowell graf (line 27): ~165 words
- BLDTF graf (line 29): ~125 words
- SMCRA graf (line 31): ~170 words
- Carbon graf (line 33): ~95 words
- Three-responses graf (line 35): ~235 words
- Call graf (line 39): ~125 words

Approximate total: ~1,140 words by this paragraph-summing pass. The frontmatter at line 13 claims "1,024" words; V-D claims 1,029 words. The frontmatter "1,024" claim is LOCKED-aligned; the actual body sits within the reasonable range around LOCKED's published 1,024w. Either way, this is LOCKED-band, not V-D-band — though the word-count axis is not as diagnostic as the prose-content axis because the bands overlap (LOCKED 1,024w; V-D 1,029w; difference 5w).

---

## §2. LOCKED archive correctness

### §2.1 Result top-line

**FAIL — the LOCKED archive does NOT exist.** The expected file `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md` is not present on the canonical path; the `_archive/prior-versions/` subdirectory itself does not exist.

### §2.2 Evidence

Read attempt at `/Users/c17n/commons-bonds/publishing/op-eds/mcdowell-county-true-cost/_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md` returned `File does not exist`. Read attempt at the parent `_archive/prior-versions/` directory also returned `File does not exist`.

The only `_archive/` subdirectory that exists is `parallel-drafts_2026-05-28/`, which contains the three V-D audits + the V-D HYBRID source + the ALT-NO-EM + ALT-NORM-PUNCT sibling drafts + the drafter's-self-audit. No prior-versions archive subdirectory has been created.

### §2.3 Diagnosis

This is consistent with §1's finding: if the V-D swap had been executed, the LOCKED prose would have been displaced from `op-ed.md` and archived to `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md` per the standard swap pattern (parallel to Aeon V-C → V-D swap at commit `967c76e` per fresh three-pass independent audit §7.1). Neither the displacement (LOCKED still IS the canonical body) nor the archive (no archive subdirectory created) occurred. Both are missing from the same root cause: the swap was not executed.

### §2.4 LOCKED prose specifics — cross-check against prior independent audit

The task brief asks for cross-check against the prior independent audit's "quoted LOCKED phrasing." The prior independent audit at `mcdowell-op-ed_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` §1.1 lists the LOCKED→V-D diffs explicitly. Per its §1.1:

- LOCKED lede opener (quoted by prior audit): *"The argument over what energy 'really costs' tends to surface in policy debates whenever an agency revises a number, a company files for bankruptcy, or a coal-region community appears in the headlines for some reason it would prefer not to."*
- LOCKED McDowell graf structure (quoted by prior audit): "6 sentences; 1950 peak → 2020 → 1990 U.S. Steel income drop → 2016 Walmart → 2022 16th-poorest data → 2015 drug-induced death rate."
- LOCKED BLDTF graf structure (quoted by prior audit): "5 sentences; BLDTF $44b distributed → debt $4.5b 2021 + $15b 2050 → bankruptcy-to-public-balance-sheet → 'real cost all along; not on invoice.'"

Cross-checking the canonical op-ed.md body against these LOCKED specifics:

- Canonical line 21 matches LOCKED lede opener verbatim. **CONFIRMED LOCKED.**
- Canonical line 27 matches LOCKED 6-sentence McDowell structure (1950 peak → 2020 → 1990 U.S. Steel → 2016 Walmart → 2022 16th-poorest → 2015 drug-induced death). **CONFIRMED LOCKED.**
- Canonical line 29 matches LOCKED 5-sentence BLDTF structure (BLDTF $44b → debt → bankruptcy-to-public-balance-sheet → "real cost all along; not on invoice"). **CONFIRMED LOCKED.**

All three LOCKED markers are present in the canonical body. The canonical body IS the LOCKED 2026-05-10 prose. No swap occurred.

---

## §3. Frontmatter prose audit

### §3.1 Result top-line

**N/A — the frontmatter in canonical op-ed.md is the original LOCKED 2026-05-10 frontmatter, NOT a parent-session-written V-D swap frontmatter.** There is no NEW PROSE in the frontmatter to audit because the swap was not executed.

### §3.2 Evidence

Canonical op-ed.md frontmatter (lines 1–17) consists of:
- Title: "What a Ton of Coal Actually Cost"
- "Pipeline draft — opportunistic-submission readiness, not deadline-driven." (line 3)
- Created date 2026-05-10 + Author Chris Winn (lines 4–5)
- Target venue tier with Project Syndicate / Bloomberg / NYT / WaPo / Guardian breakdown (lines 6–9)
- News-peg activation note (line 11)
- Body word count "1,024" (line 13) — the LOCKED count, NOT the V-D 1,029 count
- Path B audit (line 14) — references LOCKED's Stage 3 fact-check pass
- Apparatus check (line 15) — references the LOCKED-era apparatus-exclusion verification

There is no:
- Rigor-lineage attribution to V-D's triple-audit cascade
- Hard-rule verification axis sentence naming Kennedy, Lewis, WVBLA, UMW, U.S. Steel, Rennert, Wagner/Anthoff/Cropper, Obama/Trump/Biden, EPA
- Em-dash discipline note claiming "3 chars / 2 sites; nut-graf parenthetical + call-graf appositive"
- Word count claim of "1,029w body"
- Phase 4 ratification metadata
- Any V-D-specific frontmatter content

The frontmatter is entirely the pre-swap LOCKED frontmatter. There is no V-D-related parent-session prose to audit.

### §3.3 Scaffolding-token discipline check

Canonical frontmatter (lines 1–17) contains no scaffolding tokens — no INCLUDE/EXCLUDE glyphs, no "Pass 3.x" / "Stage 4" / "Phase A-Z" / "ratified" / "Option A-Z" / "cluster-γ" / "Pattern 2" patterns. This is consistent with LOCKED-era frontmatter (pre-V-D-cascade era; scaffolding-token discipline was not yet a vocabulary the LOCKED frontmatter would have used). **PASS at the scaffolding-discipline axis — but the PASS is by-accident because the frontmatter is the older LOCKED one, not because parent-session frontmatter was correctly scrubbed.**

### §3.4 Counterfactual — what would have failed if the swap had executed

If commit `189f42b` had executed the swap including new frontmatter prose, this audit would have walked:
- Hard-rule lineage accuracy claims against the three audit artifacts.
- Em-dash discipline claim against the V-D body em-dash count (3 chars / 2 sites would have been verifiable against canonical body).
- Cross-reference paths from new frontmatter against actual file locations.
- Named-entities verification against canonical-facts inventory (Kennedy = §the-county; Lewis = §black-lung; WVBLA + UMW = §black-lung; U.S. Steel = §the-county; Rennert = §carbon-arithmetic; Wagner/Anthoff/Cropper = §political-history; Obama/Trump/Biden + EPA = §political-history — all confirmed inventory-anchored if the new prose had referenced them).
- Scaffolding-token discipline at the new prose level.

None of these axes can be evaluated because no new frontmatter prose was written. This whole §3 reduces to "the swap did not execute."

---

## §4. README prose audit

### §4.1 Result top-line

**N/A — the README in canonical state is the pre-swap README (4 short sections; no three-audit rigor lineage section).** There is no NEW PROSE in the README to audit because the README update did not execute.

### §4.2 Evidence

Canonical `publishing/op-eds/mcdowell-county-true-cost/README.md` (20 lines total) consists of:
- Title "McDowell County True Cost — op-ed" (line 1)
- Metadata block: Slug + Target venues TBD + State Draft (2026-05-10) + Last updated 2026-05-25 (lines 3–6)
- §"Op-ed status" with two bullets (canonical draft link + canonical-facts symlink) (lines 8–11)
- §"Shared canonical-facts inventory" with one paragraph (lines 13–15)
- §"News-peg activation" with one paragraph (lines 17–19)

There is no:
- Three-audit rigor lineage section (drafter's-self-audit + prior independent audit + fresh three-pass audit summaries)
- "WVBLA spot-fix recommendation issued" attribution to the prior independent audit
- "Retracted on Harper's-RATIFIED canonical-text grounds + Amendment-D directness-discipline grounds" claim about the fresh chip
- "PASS across all 7 verification axes" hard-rule axis claim
- At-activation guidance referencing trim sites / Walmart restoration / Wagner venue specificity
- Updated "Last updated" date past 2026-05-25 (pre-swap was 2026-05-25; post-V-D ratification would have triggered a 2026-05-28 or later refresh)
- Updated State past "Draft (2026-05-10)" (post-swap would have flagged the V-D ratification state)

The README is entirely the pre-V-D-cascade README. There is no parent-session-written README prose to audit.

### §4.3 Cross-reference: Amendment-D framing question

The task brief asked whether the README would incorrectly attribute Amendment-D reasoning to the fresh chip's original audit, given that Amendment D was ratified 2026-05-31 (retroactively) while the fresh chip filed 2026-05-28. **This question cannot be answered against the actual README because the README was not updated.**

Separately, the audit notes that the fresh three-pass independent audit at `mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md` ends at §8 (line 878) with no §9 Amendment-D retroactive addendum. The task brief's claim that the fresh audit "includes §9 Amendment-D addendum" is **not borne out by the actual file content**. If a future README refresh references "§9 Amendment-D addendum," that reference would not resolve against the current state of the fresh audit artifact.

### §4.4 Counterfactual — what would have failed if the README refresh had executed

Same counterfactual posture as §3.4: nothing to audit; the README update did not execute.

---

## §5. §2.1 hard-rule axis re-confirmation on canonical op-ed.md body

### §5.1 Result top-line

**PASS — but on the LOCKED body, not on V-D HYBRID body.** The canonical op-ed.md body (which IS the LOCKED 2026-05-10 prose, not V-D HYBRID) passes the §2.1 hard-rule axis. The V-D HYBRID body's PASS verdict (triple-audited in the prior three artifacts) is independently corroborated by its substrate-discipline architecture, but this §5 re-confirms only the LOCKED body because that is what canonical op-ed.md currently contains.

### §5.2 Named-subject walk on canonical (LOCKED) body

| Named subject | Location in canonical body | Inventory anchor | Hard-rule classification | Verdict |
|---|---|---|---|---|
| (none) — no named real persons in LOCKED body | n/a | n/a | LOCKED predates V-D's introduction of Kennedy + Lewis + Rennert + Wagner/Anthoff/Cropper | **PASS (by absence)** |
| U.S. Steel (organization; line 27) | "The U.S. Steel mine closure in 1990 cut personal income in the county by two-thirds in a single year." | §the-county anchored | Organization; public record | **PASS** |
| Black Lung Disability Trust Fund (line 29) | "The Black Lung Disability Trust Fund — the federal program that pays disabled miners and their widows — has distributed more than $44 billion since its creation." | §black-lung anchored | Federal program; public record | **PASS** |
| Surface Mining Control and Reclamation Act of 1977 (line 31) | "Across Appalachia, roughly 633,000 acres are awaiting reclamation under the 1977 Surface Mining Control and Reclamation Act." | §environmental anchored | Federal statute; public record | **PASS** |
| Environmental Protection Agency (line 33) | "The Environmental Protection Agency's most recent estimate..." | §carbon-arithmetic anchored | Federal agency; public record | **PASS** |

Note: LOCKED body has FEWER named subjects than V-D HYBRID body because LOCKED predates the V-D substrate-expansion (Kennedy + Lewis + Rennert + Wagner/Anthoff/Cropper). Hard-rule axis PASS is easier-to-achieve on LOCKED because the risk surface is smaller. This does NOT diminish V-D's separately-audited PASS verdict; it just notes that the present §5 re-confirmation is on LOCKED, not V-D.

### §5.3 Scene-render / quoted-speech / motivation-attribution walk

- **Scene-rendered encounters:** Zero in LOCKED body. Op-ed register throughout. **PASS.**
- **Invented quoted speech:** Zero in LOCKED body. Only quoted material is the rhetorical-frame "fake" — reader-anticipated counter-framing. **PASS.**
- **Motivation attributions:** Zero in LOCKED body. "The social cost of carbon has been revised four times by four administrations on grounds that have less to do with carbon physics than with which side of the political fight had more resources at the moment of revision" (line 39) characterizes structural-incentive geometry, not individual motives. **PASS.**
- **Period-specific civic-infrastructure detail:** Zero invented in LOCKED body. **PASS.**
- **Documentary-record specifics:** All canonical numbers ($558 total; $4.50 1960 mine-mouth; $44B BLDTF distributed; $4.5B 2021 debt; $15B 2050 projection; 633,000 acres; $3.8B bonds; $7.5-9.8B cleanup; 2.86 tons CO₂ per ton coal; $190 SCC; $544 implied damage; 38% poverty; $28K median income; $67K national median; 141/100K overdose death rate). All trace to canonical-facts inventory or public-record federal reporting. **PASS.**

### §5.4 §5 aggregate verdict

**LOCKED body §2.1 hard-rule axis: PASS.** This is unsurprising — LOCKED was the baseline that had been pipeline-sitting for ~3 weeks without surfaced flaws per fresh audit §0; the V-D parallel-drafts cascade was built on top of LOCKED's hard-rule-axis floor. The PASS here re-confirms what was already known about LOCKED, NOT what was being claimed at commit `189f42b` (which would have been V-D HYBRID's PASS).

---

## §6. Findings

### §6.1 HIGH

**F-EXEC-H1 (HIGH) — Body byte-equality fails: canonical op-ed.md retains LOCKED prose verbatim; V-D HYBRID swap NOT executed.**

The dominant finding of this audit. Canonical `publishing/op-eds/mcdowell-county-true-cost/op-ed.md` body (lines 19–43) matches LOCKED 2026-05-10 prose at every load-bearing distinctive site:

- LEDE opener: LOCKED conditional ("The argument over what energy 'really costs' tends to surface..."), not V-D declarative ("Every few years, an argument resurfaces..."). 
- McDowell graf: LOCKED 6-sentence structure with Walmart 2016 datum, not V-D 7-sentence Kennedy+mechanization+active-voice-U.S.-Steel expansion without Walmart.
- BLDTF graf: LOCKED 5-sentence structure with no historical anchor, not V-D 6-sentence WVBLA+Lewis 1969-establishment expansion.
- Carbon graf: anonymous "a 2022 *Nature* meta-analysis," not V-D's "Rennert et al. 2022 *Nature*" attribution.
- Call graf: LOCKED's no-inline-SCC-numbers call, not V-D's $42/$1–7/$51/$190 enumeration + Wagner/Anthoff/Cropper inline citation.

Em-dash count corroborates: canonical body has 7 em-dash characters / 5 sites (LOCKED baseline); V-D HYBRID body has 3 em-dash characters / 2 sites (per V-D frontmatter line 22).

Word count corroborates: canonical body ~1,024w (per frontmatter line 13) is LOCKED-band; V-D HYBRID body is 1,029w (per V-D frontmatter line 21). The 5w delta is small, but combined with the prose-content axis, body content is unambiguously LOCKED.

**Severity rationale.** This is HIGH because the swap claim by commit `189f42b` is the entire reason this audit exists. If the swap did not execute, then Workstream A's deliverable did not land; downstream audit axes (frontmatter prose, README prose, archive correctness) are all consequentially N/A or moot pending corrective swap.

**F-EXEC-H2 (HIGH) — LOCKED archive does NOT exist; the `_archive/prior-versions/` subdirectory was not created.**

The expected file `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md` does not exist; the `_archive/prior-versions/` parent directory itself does not exist. Read attempts at both paths return `File does not exist`. The only `_archive/` subdirectory present is `parallel-drafts_2026-05-28/` (which contains the V-D artifacts). No prior-versions archive was created at commit `189f42b`.

This is consistent with F-EXEC-H1: if the swap had executed, LOCKED prose would have been displaced from canonical op-ed.md and archived at `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md`. Neither side of that swap occurred.

**Severity rationale.** HIGH because the missing archive directory means even if the body swap is retroactively applied, the LOCKED safety-net fallback discipline (referenced explicitly in fresh audit §7.1: "LOCKED 2026-05-10 retained as safety-net fallback at `_archive/prior-versions/` (parallel to Aeon V-C archive pattern)") is currently broken — there is no archive copy of LOCKED on the canonical path. The LOCKED text is currently only present in the canonical `op-ed.md` itself. If the corrective swap is applied without first archiving LOCKED, the only canonical record of LOCKED would be in git history at commit `189f42b^` (parent commit); retrieval would require git operations rather than a tree-resident archive.

### §6.2 MEDIUM

**F-EXEC-M1 (MEDIUM) — README not updated; pre-swap README state retained.**

Canonical `publishing/op-eds/mcdowell-county-true-cost/README.md` is the 20-line pre-swap README (Last updated 2026-05-25; State Draft 2026-05-10). It contains no three-audit rigor lineage section, no Workstream A summary, no V-D ratification metadata, no at-activation guidance from the fresh audit's Phase 4 forward-flags (Walmart restoration on stretch venue; Wagner venue specificity verification; center-right news-peg sensitivity check on federal-surplus-food framing).

**Severity rationale.** MEDIUM because the README is internal scaffolding (per CLAUDE.md classification), not end-user-facing prose; missing README updates do not propagate to the published essay. But the absence is diagnostic of the same execution failure as F-EXEC-H1: the parent session that authored commit `189f42b` did not author the post-swap README content either.

**F-EXEC-M2 (MEDIUM) — Task-brief inaccuracy: fresh audit artifact does NOT contain "§9 Amendment-D retroactive addendum."**

The task brief stated the fresh three-pass independent audit "includes §9 Amendment-D addendum." Reading the fresh audit file (`mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md`) end-to-end: the file ends at line 878 with §8 Cross-references; there is no §9 section. If a downstream artifact (e.g., a README refresh) is written that references the §9 Amendment-D addendum, that reference will not resolve against the actual file content.

**Severity rationale.** MEDIUM because the task brief's claim is a parent-session-state misrepresentation, not a Workstream A execution failure per se. But it matters for accurate downstream prose — any artifact referencing "§9 Amendment-D addendum" of the fresh audit is making a claim that does not verify against the current state of the fresh audit file. Either §9 needs to be added to the fresh audit file, or downstream prose should not reference it.

### §6.3 LOW

**F-EXEC-L1 (LOW) — V-D HYBRID source file frontmatter status remains "PROPOSED" not "RATIFIED."**

The V-D HYBRID source at `_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_hybrid_best-of-both.md` frontmatter line 47 says: `status: PROPOSED (drafter's hybrid — methodologically suspect; independent audit chip recommended before submission decision)`. If V-D is the source of truth for the canonical body post-swap, the V-D source frontmatter should also reflect post-ratification status (e.g., `status: RATIFIED-AND-PROMOTED-TO-CANONICAL-2026-06-01` or similar). At present the V-D source is still in pre-ratification status.

**Severity rationale.** LOW because the V-D source is internal scaffolding; status markers on parallel-draft archive artifacts have minimal downstream impact. But if the corrective swap is applied, the V-D source status should refresh to reflect the swap's ratification.

### §6.4 Summary table

| ID | Severity | Finding |
|---|---|---|
| F-EXEC-H1 | HIGH | Body byte-equality FAIL — canonical op-ed.md retains LOCKED prose verbatim; V-D HYBRID swap NOT executed |
| F-EXEC-H2 | HIGH | LOCKED archive does NOT exist; `_archive/prior-versions/` subdirectory was not created |
| F-EXEC-M1 | MEDIUM | README not updated; pre-swap README state retained |
| F-EXEC-M2 | MEDIUM | Task-brief inaccuracy — fresh audit does NOT contain "§9 Amendment-D retroactive addendum" |
| F-EXEC-L1 | LOW | V-D HYBRID source file frontmatter status remains "PROPOSED" not "RATIFIED" |

---

## §7. Phase 4 ratification recommendation

**Recommendation: REVERT-AND-REWORK.**

This recommendation is the dispositive consequence of F-EXEC-H1 + F-EXEC-H2.

### §7.1 Rationale

Workstream A's deliverable was the V-D HYBRID canonical swap: promote V-D HYBRID prose to canonical `op-ed.md`, archive LOCKED at `_archive/prior-versions/`, refresh README with three-audit rigor lineage + at-activation guidance, update op-ed.md frontmatter with V-D rigor lineage. **None of these execution steps landed in commit `189f42b`.** The canonical body is still LOCKED; the archive is missing; the README is the pre-swap state; the frontmatter is the LOCKED-era frontmatter.

The three V-D audit artifacts (drafter's-self-audit + prior independent audit + fresh three-pass audit) are all present on the canonical path — those artifacts are intact internal scaffolding, and the V-D HYBRID source prose itself is intact at `_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_hybrid_best-of-both.md`. The substrate for the swap is fully ready. **What is missing is the swap execution itself.**

REVERT-AND-REWORK does NOT mean discarding the V-D ratification decision — the fresh audit's SHIP HYBRID recommendation + author ratification stand. It means: the parent session that produced commit `189f42b` should re-execute the swap properly. The corrective work is:

1. **Archive LOCKED.** Create `publishing/op-eds/mcdowell-county-true-cost/_archive/prior-versions/` directory. Copy the current canonical op-ed.md (which IS LOCKED) to `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md`. This is the safety-net fallback per fresh audit §7.1.

2. **Promote V-D HYBRID body to canonical op-ed.md.** Replace the body content of `op-ed.md` (lines 19–43, between LEDE comment and sign-off) with the V-D HYBRID body (lines 53–77 of `_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_hybrid_best-of-both.md`). Verify the body byte-equality post-swap.

3. **Refresh op-ed.md frontmatter** with V-D rigor lineage. Update body word count to 1,029. Update em-dash discipline note to "3 chars / 2 sites; nut-graf parenthetical + call-graf appositive." Add V-D ratification metadata + hard-rule verification axis lineage attribution. Apply scaffolding-token discipline check to the new prose.

4. **Refresh README** with three-audit rigor lineage section + Workstream A summary + at-activation guidance (Walmart restoration on stretch venue per F-3.5-L2; Wagner venue specificity verification per F-3.5-L1; center-right news-peg sensitivity check on federal-surplus-food framing). Update "Last updated" date. Update "State" past "Draft (2026-05-10)" to reflect V-D ratification.

5. **Update V-D HYBRID source frontmatter** (`_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_hybrid_best-of-both.md` line 47) to reflect post-ratification status.

6. **(Optional but recommended)** Resolve the task-brief inaccuracy F-EXEC-M2: either add §9 Amendment-D retroactive addendum to the fresh audit file (if such an addendum was intended), or remove any downstream prose claiming the §9 exists.

### §7.2 What this audit explicitly does NOT recommend

This audit does NOT recommend:
- Discarding V-D HYBRID prose. The triple-audited V-D prose is the right canonical body; the audit's REVERT-AND-REWORK is about re-executing the swap, not about reconsidering the V-D ratification decision.
- Reverting any internal-scaffolding artifacts. The three V-D audit artifacts + the V-D HYBRID source + the parallel-draft siblings should all remain in place.
- Force-pushing main to undo commit `189f42b`. Per CLAUDE.md hard constraints: never force-push main; never amend a commit already on origin/main. The corrective work is a NEW commit on top of `189f42b`, not a rewrite of `189f42b`.

### §7.3 Conditions for ratification path forward

After the corrective work (per §7.1 steps 1–6) is committed:
- This audit's verdict shifts from REVERT-AND-REWORK to RATIFY-AS-EXECUTED conditional on a fresh body byte-equality re-check + archive existence verification + frontmatter + README re-audit (which would be a follow-up Workstream A re-audit, parallel scale to the present audit but on the corrected state).
- The V-D HYBRID's triple-audited substantive ratification (Pass 3.3 NET INCLUDE DECISIVE; Pass 3.4 ROBUST; Pass 3.5 RESTORATION-NOT-WARRANTED; §2.1 hard-rule PASS) remains operative; this audit found no reason to reopen any of those verdicts.

---

## §8. State summary

```
STATE: mcdowell-op-ed-V-D-canonical-swap-workstream-A-execution-audit PROPOSED
(commit 189f42b did NOT execute the swap; canonical op-ed.md retains LOCKED prose
verbatim; LOCKED archive directory missing; README not updated; frontmatter not
refreshed; V-D HYBRID source prose + three audit artifacts intact in
parallel-drafts_2026-05-28 — substrate ready for corrective re-execution);
VERDICT: REVERT-AND-REWORK;
NEXT: parent-session-corrective-swap-re-execution per §7.1 steps 1-6;
AWAITING: parent-handoff
```

---

## §9. Cross-references

- Audit target (claimed swap commit): `189f42b` on origin/main
- Canonical op-ed (current state — LOCKED prose verbatim): [`../../op-ed.md`](../../op-ed.md)
- Canonical README (current state — pre-swap): [`../../README.md`](../../README.md)
- V-D HYBRID source (substrate ready for corrective swap): [`mcdowell-op-ed_hybrid_best-of-both.md`](mcdowell-op-ed_hybrid_best-of-both.md)
- Drafter's-self-audit on V-D: [`mcdowell-op-ed_hybrid_drafters-self-audit.md`](mcdowell-op-ed_hybrid_drafters-self-audit.md)
- Prior independent audit on V-D (Pass 3.3 + 3.4 scope; recommended SPOT-FIX-THEN-SHIP): [`mcdowell-op-ed_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`](mcdowell-op-ed_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md)
- Fresh three-pass independent audit on V-D (Pass 3.3 + 3.4 + 3.5 scope; recommended SHIP HYBRID; file ends at §8 with NO §9 Amendment-D addendum present): [`mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md`](mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md)
- Shared canonical-facts inventory (single source of truth): [`../../../_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md`](../../../_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md)
- No-invented-factual-claims hard rule: [`../../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md)
- LOCKED archive target path (currently MISSING): `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md`

---

*End of Workstream A execution audit — McDowell op-ed V-D canonical swap (commit `189f42b`) — 2026-06-01. PROPOSED; verdict REVERT-AND-REWORK; parent-session-handoff for corrective swap re-execution. Per merge-on-ratification, this internal-scaffolding artifact fast-forwards to main at parent-session close.*
