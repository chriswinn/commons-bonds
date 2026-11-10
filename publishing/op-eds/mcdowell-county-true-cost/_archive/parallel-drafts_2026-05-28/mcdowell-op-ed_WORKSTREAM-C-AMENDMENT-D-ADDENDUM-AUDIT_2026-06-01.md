# Workstream C — Amendment-D Retroactive Addendum Independent Audit — 2026-06-01

**Status:** **PROPOSED 2026-06-01 — REVERT-AND-REWORK.** Author ratification pending.
**Auditor:** Fresh CC chip (independent verification audit on Workstream C — McDowell op-ed Amendment-D §9 addendum).
**Audited artifact (claimed):** `publishing/op-eds/mcdowell-county-true-cost/_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md` §9 "Reception-chain audience weighting addendum (Amendment D retroactive application)" — claimed added at commit `1f64da1`.
**Headline finding:** **THE §9 ADDENDUM DOES NOT EXIST ON DISK AT THE CANONICAL PATH.** The McDowell fresh-three-pass audit file ends at line 877 with §8 Cross-references + the original 2026-05-28 closing block. There is no §9 anywhere in the file. Independent audits §1–§8 of the present audit therefore cannot evaluate parent-session-authored content; they evaluate whether the *doctrine* the §9 addendum claims to invoke exists on disk and whether the surrounding evidence supports the canonical-pattern claim.
**Permission constraint:** Used Read + Write only (no git, no bash beyond ls/grep/wc auxiliary calls). Used canonical project path `/Users/c17n/commons-bonds/` throughout.

---

## §0. Methodological framing

Workstream C kickoff describes a parent-session-authored §9 addendum to the V-D fresh three-pass independent audit. The addendum is claimed to:

1. Apply Amendment-D weight-tags to the existing 9-character V-D fresh-chip per-character data.
2. Re-aggregate the verdict under Amendment-D weighting.
3. Claim canonical-pattern role: "op-ed worked example for Amendment D, parallel to the Aeon editor-pitch worked example (commit `73c5764`, 2026-05-31)."

The audit was intended to verify §9 substance. The audit cannot verify §9 substance because **§9 is not present at the canonical path on disk**. This finding is reported in §9.H1 below as the load-bearing HIGH finding.

**What the audit CAN verify** (and does):

- Whether Amendment D doctrine exists on disk at the source location §9 cites.
- Whether the Aeon empirical anchor (commit `73c5764`) actually identifies itself as an Amendment-D worked example or whether the parent-session is retrofitting that framing.
- Whether the v3.1 pipeline doctrine memory has been updated to codify Amendment D.
- Whether a working Amendment-D-weighted audit exists elsewhere in the corpus (Atlantic Ideas) that could serve as the actual canonical pattern.

These verifications constitute §§1–8 below. The aggregate recommendation (§10) is REVERT-AND-REWORK on the grounds that the §9 addendum, the source doctrine, and the canonical-pattern claim cannot be jointly verified on disk.

---

## §1. Amendment D framing reminder accuracy (§9.1)

**Verdict: CANNOT-VERIFY — source doctrine not on disk at cited path.**

### §1.1 Read of the canonical Amendment D source

The §9 addendum claims to invoke "Amendment D (ratified 2026-05-31)" via `tools/drafting-templates/audience-pressure-test-construction.md` §"Reception-chain audience weighting (Amendment D, ratified 2026-05-31)".

Independent read of `tools/drafting-templates/audience-pressure-test-construction.md` confirms:

- File length: 296 lines.
- File ends at line 297: `*End of audience pressure-test construction guide (v3.0).*`
- File version label: **v3.0** (no v3.1 label).
- Grep for "Amendment D" returns 0 matches.
- Grep for "Reception-chain" returns 0 matches.
- Grep for "ratified 2026-05-31" returns 0 matches.
- Grep for "HIGH direct" / "MEDIUM consultant" / "LOW projected-downstream" weight-tier vocabulary returns 0 matches.

**The Amendment D section the parent-session's §9.1 cites does not exist at the cited path.** §9.1's framing reminder therefore cannot be cross-verified against source.

### §1.2 Read of v3.1 pipeline doctrine memory

Independent read of `tools/memory/feedback_audience_aware_drafting_discipline.md` confirms:

- Document identifies itself as v3.1.
- Codified Amendments: A (two-class cascade, 2026-05-18) + B (Pass 3.5 developmental-edit, 2026-05-18) + C (Interactive Ratification Protocol, 2026-05-19, referenced).
- **No Amendment D section.** Grep for "Amendment D" returns 0 matches.

### §1.3 Empirical anchor citation accuracy

§9 claims empirical anchor: "Aeon Option E.2 γ.1 opener-contingency audit addendum (commit `73c5764`, 2026-05-31)."

Independent read of `publishing/essays/aeon-mask-of-abundance/rigor/final-pre-submission-tweak_2026-05-31_pass-3-3-3-4-3-5-audit.md` (the Option E.2 γ.1 audit at that commit-window) confirms:

- File DOES exist and is the Option E.2 γ.1 opener-contingency Pass 3.3 + 3.4 + 3.5 audit.
- File contains zero instances of "Amendment D" or "reception-chain" in primary audit text (verified via grep).
- The audit does NOT identify itself as an Amendment-D worked example. It is a precautionary spot-fix audit on contingency text for the Aeon portal submission.

The Aeon audit is therefore being **retroactively reclassified** as an "Amendment-D worked example" by the parent session — that framing is not present in the Aeon audit itself.

### §1.4 Cross-check against Atlantic Ideas Amendment-D-weighted audit

A working Amendment-D-weighted audit DOES exist in the corpus at:
`publishing/essays/atlantic-ideas-pricing-honestly/rigor/cover-letter-pass-3-3-3-4-3-5-audit_AMENDMENT-D-WEIGHTED_2026-06-01.md`

This audit identifies Amendment D codification at commit `a1f88db` (not `1f64da1`) and treats the Aeon Option E.2 γ.1 audit (commit `73c5764`) as the empirical anchor — same framing the McDowell §9 addendum is described as using. The Atlantic Ideas audit also references the source doctrine at the same path the McDowell §9 cites, where the Amendment D section is likewise not findable on the current disk state.

**Hypothesis:** Amendment D may have been codified at a path / commit on origin/main that is not yet reflected in the worktree state available to this audit, OR the codification commit `a1f88db` did not include the Amendment D section in the file I read, OR there is path / file-state divergence between what the parent-session sees and what is on canonical disk.

**Verdict on §9.1 framing accuracy:**

- Three weight tiers (HIGH/MEDIUM/LOW): cannot verify against source doctrine (source doctrine section not on disk).
- Spot-fix discipline question: cannot verify.
- Ratification date 2026-05-31: cannot verify against source; Atlantic Ideas audit uses same date so the date is at least internally consistent with another Amendment-D-invoking audit.
- Empirical anchor citation `73c5764`: file exists at that path; the audit itself does NOT explicitly identify as an Amendment-D worked example (retrofitted framing).

---

## §2. McDowell op-ed reception-chain map (§9.2)

**Verdict: CANNOT-VERIFY § content; verify worked-examples table on disk supports the artifact-class classification claim.**

### §2.1 Worked-examples table check

The Workstream C kickoff asks: does the worked-examples table at `tools/drafting-templates/audience-pressure-test-construction.md` explicitly identify op-ed prose as "two-tier direct" or just "all audiences direct"?

Independent read of the doctrine file confirms: **the worked-examples table does not exist on disk at all.** The file's table of contents under §8 ("Quick-start: defaults by piece type") includes an op-ed row with character counts (Tier 1: 3 / Tier 2: 3 / Tier 3: 4 / Total: 10), but this is the Pass 3.3 acceptance-set sizing table — NOT a reception-chain weighting table that classifies audiences as direct/consultant/projected-downstream.

The parent-session's §9.2 invokes "the worked-examples table" as authority for classifying the McDowell op-ed in the "End-reader-facing essay / chapter / op-ed prose" class with "all theoretical audiences as direct readers." **This table does not exist on disk at the cited source.**

### §2.2 Direct-reader list spot-check (notional, based on Workstream C kickoff description)

If the §9.2 direct-reader list reads as kickoff describes:

- FT Opinion editor + Bloomberg Opinion editor as gating direct — defensible per Tier-1 conventions.
- FT/Bloomberg page deputy editors as "gating-adjacent direct" — **FLAG.** The Workstream C kickoff already notes that the Atlantic-Ideas-weighted audit treats deputy editors / screening assistants as **MEDIUM (consultants)** under Amendment D's editor-pitch class. Promoting deputy editors to "gating-adjacent direct" for the end-reader-facing op-ed class would constitute scope-expansion of HIGH weight beyond what the Atlantic Ideas precedent supports. If §9.2 does this, it is over-credited classification (flag in §3 below).
- FT/Bloomberg end readers as direct end-reader — defensible.

### §2.3 Consultants list spot-check

If §9.2 lists fact-checkers + external-policy-expertise consultants — defensible per Amendment D's general consultant-band semantics (verified via Atlantic Ideas audit §1 table).

### §2.4 Projected-downstream list spot-check

If §9.2 lists center-right policy aides + McDowell residents + center-left policy aides as "theoretical audience tags whose reception is editor-projected" — this is a category-error against the artifact class the §9 addendum claims for the op-ed.

Per the Atlantic Ideas audit's worked-examples table reading: end-reader-facing prose (essay / chapter / op-ed) treats theoretical audiences as **direct readers**, not as editor-projected downstream. The Atlantic Ideas audit applies projected-downstream-only to the cover-letter class (where the editor reads the cover letter and *projects* downstream essay reception). The McDowell op-ed is end-reader-facing prose — direct readers ARE the theoretical audiences.

If the McDowell §9.2 reframes the Tier 2 + Tier 3 acceptance-set characters as "projected downstream" rather than "direct end-reader" categories, this constitutes an **artifact-class misclassification**: the §9 addendum is applying cover-letter-class Amendment-D weighting semantics to an end-reader-facing op-ed.

**This is the load-bearing scope-creep risk in the canonical-pattern claim.** If the McDowell op-ed worked example reframes specialist characters + cultural-resonance characters as LOW-weight projected-downstream, the portfolio sweep would propagate that misclassification across ~10 essays + 2 op-eds.

---

## §3. Per-character weight-tag assignment (§9.3)

**Verdict: CANNOT-VERIFY (§9 absent from disk); structural concerns with the assignment scheme described in kickoff.**

If §9.3 assigns tags as Workstream C kickoff describes:

| Tag | §9.3 assignment | Auditor concern |
|---|---|---|
| T1.1 FT editor: HIGH | Defensible per direct-gating | OK |
| T1.2 Bloomberg editor: HIGH | Defensible per direct-gating | OK |
| T1.3 FT/Bloomberg reader: HIGH | Defensible per direct end-reader | OK but see T3.3 duplicate concern below |
| T2.1 Appalachian-policy specialist: MEDIUM-to-LOW | **FLAG MEDIUM**: ambiguous range; should the addendum commit to one tier? Specialist characters in the v3.0 doctrine §1.1 Tier 2 description ("pipeline-strengthening" — characters whose Yes vote amplifies) are described as substantive end-readers, not as editor-consulted second-opinion advisors. The MEDIUM-consultant tag downgrades their direct-reader status. | Likely **OVER-CREDITED as LOW / UNDER-CREDITED as HIGH-direct.** |
| T2.2 Black-Lung-policy specialist: MEDIUM-to-LOW | Same FLAG as T2.1 | Same |
| T2.3 Energy-economics analyst: MEDIUM-to-LOW | Same FLAG as T2.1 | Same |
| T3.1 Center-right policy aide: LOW | **FLAG MEDIUM**: Center-right policy aide is a Tier 3 cultural-resonance character per v3.0 doctrine §1.1. Whether op-ed editors consult policy-aide-network second opinions before running policy op-eds varies by editor practice; in any case, a Tier 3 character in end-reader-facing prose under Amendment D's straightforward reading (Atlantic Ideas precedent) would be **direct** end-reader, not LOW projected-downstream. | Likely **OVER-CREDITED as LOW.** |
| T3.2 McDowell County resident: LOW | Same FLAG: Tier 3 cultural-resonance character is direct end-reader per Amendment D's end-reader-facing prose semantics. | Likely **OVER-CREDITED as LOW.** |
| T3.3 General FT/Bloomberg subscriber: HIGH | **FLAG**: Is this a duplicate of T1.3? Both are described as FT/Bloomberg readers. If T1.3 = "sophisticated centrist intellectual" and T3.3 = "general subscriber without prior framework knowledge," they are distinct reader characters and both belong at HIGH-direct. But the addendum should explicitly note the distinction. | OK if distinction noted |

**Structural concern:** the "MEDIUM-to-LOW" range tag is methodologically unsound. Amendment D's weighting discipline requires committing to a tier so the re-aggregation math has defined inputs. A range tag is non-aggregateable.

**Cross-check against Atlantic Ideas precedent:** Atlantic Ideas audit §1 table commits each character to a single tier (HIGH / HIGH-MEDIUM / LOW). The McDowell §9.3's range tags would be a methodological regression from the Atlantic Ideas precedent.

**Over-crediting bias overall:** if §9.3 systematically tags Tier 2 + Tier 3 characters as MEDIUM-to-LOW or LOW, the re-aggregation will artificially concentrate weight on Tier 1 characters and report "more decisive than unweighted aggregate suggested." This is the §9.4 conclusion in the kickoff. The conclusion is mathematically driven by the tagging choice, which (per §2.4 above) appears to misapply cover-letter-class Amendment D semantics to end-reader-facing op-ed prose.

---

## §4. Re-aggregation math (§9.4)

**Verdict: CANNOT-VERIFY (§9 absent from disk); even if §9 exists as described, the conclusion claims do not necessarily follow.**

### §4.1 Math check on the tier-breakouts

If §9.4 aggregates as the kickoff describes:

- HIGH tier (T1.1 ✓✓✓ + T1.2 ✓✓✓ + T1.3 ✓✓ + T3.3 ✓✓) = 4 characters, all INCLUDE, two ✓✓✓ and two ✓✓ → DECISIVE INCLUDE on direct readers is supported by the breakdown.
- MEDIUM tier (T2.1 ✓✓ + T2.2 ✓✓ + T2.3 ✓✓✓) = 3 characters, all INCLUDE → STRONG INCLUDE on consultants is supported.
- LOW tier (T3.1 ✓✓ + T3.2 ✓✓) = 2 characters, both INCLUDE → MODEST INCLUDE on projected downstream is **technically supported but the framing diminishes the verdict**. T3.1 + T3.2 ✓✓ are not "MODEST" — they are full ✓✓ INCLUDE verdicts. Calling them "MODEST INCLUDE" because of the LOW weight is conflating weight with verdict strength.

### §4.2 Conclusion check

§9.4 conclusion 1: "Verdict is MORE decisive than unweighted aggregate suggested." This **does follow** from the weight distribution IF Tier 1 + T3.3 are correctly weighted HIGH and the Tier 2 specialists + Tier 3 cultural-resonance characters are correctly weighted MEDIUM / LOW. But per §2.4 + §3 above, the Tier 2 + Tier 3 weighting is likely artifact-class-misapplied. If the McDowell op-ed is end-reader-facing prose (it is), then ALL acceptance characters are direct end-readers and weighting is uniform. Under uniform weighting, the original 3 ✓✓✓ + 6 ✓✓ aggregate IS the correct verdict (NET INCLUDE — DECISIVE per §2.2 of the original 2026-05-28 audit). The §9 reweighting changes the verbal framing without changing the underlying signal.

§9.4 conclusion 2: "The single wash verdict (T3.1) is on a LOW-weight projected-downstream character." **PROBLEM**: T3.1 is wash relative to LOCKED — meaning V-D and LOCKED both got the same ✓✓ INCLUDE verdict, no change. This is not a "wash verdict" — it is "no improvement vs LOCKED." Calling it a "wash on LOW-weight character" misframes the original audit's careful Δ-vs-LOCKED analysis. The original §2.1 column was "Δ vs LOCKED-estimate," not absolute weight signal.

§9.4 conclusion 3: "Drafter-aggregate vs fresh-chip-aggregate magnitude divergence at T1.4 in the Aeon cross-check pattern does not appear here." Needs verification via reading the Aeon V-D independent audit §11 cross-check pattern. See §4.3.

### §4.3 Aeon cross-check pattern verification

Read of `publishing/essays/aeon-mask-of-abundance/rigor/pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` — verify whether a T1.4 magnitude divergence pattern actually exists in that file.

**Auditor did not read that file in this audit pass** due to time + permission constraints; the §9 absence-from-disk finding is the load-bearing recommendation driver and reading the Aeon cross-check would not change the recommendation. Flag for follow-up audit pass if the parent session restores §9 to disk.

---

## §5. Pass 3.4 + 3.5 Amendment-D check (§9.5)

**Verdict: CANNOT-VERIFY (§9 absent from disk).**

### §5.1 Pass 3.4 claim review

If §9.5 claims "Amendment D's weighting does not re-rank adversarial verdicts" — this is consistent with Amendment D's documented operational scope (acceptance-test character weighting only; adversarial-set has different verdict structure — floor is EXCLUDE by definition; thread-pull synthesis is the diagnostic, not per-character weight). **Defensible if asserted.**

### §5.2 Pass 3.5 finding reweighting

If §9.5 strengthens HOLD on F-3.5-M1 (three-responses graf), F-3.5-L1 (Wagner venue), and F-3.5-L2 (Walmart datum) by appealing to Amendment D directness-vs-mediation discipline:

- F-3.5-M1: HOLD recommendation strengthened on the reasoning "restructure would serve LOW-weight T3.1 at cost of HIGH-weight direct-reader directness." **CONDITIONAL on Tier weighting**: if T3.1 is actually direct end-reader (per §3 above), the directness-discipline argument inverts — the restructure would serve direct end-reader, not LOW-weight projected. The strengthening claim only holds if §3's weight-tags are correct.

- F-3.5-L1: HOLD unchanged — Wagner venue is a substrate-discipline call (no Amendment D bearing). **Defensible.**

- F-3.5-L2: HOLD strengthened on "Walmart serves LOW-weight McDowell-resident lived-recognition at cost of HIGH-weight direct-editor band-tolerance." **CONDITIONAL on Tier weighting**: if McDowell resident T3.2 is actually direct end-reader (per §3 above), Walmart serves direct end-reader, not LOW-weight projected. The strengthening claim only holds if §3's weight-tags are correct. Additionally, the Walmart-datum HOLD was originally driven by news-peg-activation template trim guidance (~15w; available at stretch-venue activation), which is **substance-drives-length + activation-headroom reasoning, not Amendment-D reasoning**. The §9.5 strengthening risks claiming Amendment D credit for a decision already settled on independent grounds.

---

## §6. SHIP V-D AS-IS strengthening claim (§9.6)

**Verdict: CANNOT-VERIFY (§9 absent from disk); risk of double-counting evidence if §9 exists as described.**

### §6.1 WVBLA "led by" retraction revalidation claim

If §9.6 claims the original §5.3 WVBLA "led by" framing (PASS at Harper's-RATIFIED-canonical-text level) is revalidated on Amendment-D directness-discipline grounds:

- The §5.3 resolution was originally argued via Harper's-RATIFIED-canonical-text supersession of inventory-strict-reading. That is a discipline-internal precedence argument, not an Amendment-D argument.
- Adding Amendment-D directness-discipline as a SECOND independent ground (fix-for-downstream-but-damage-direct) would be a co-supporting argument. **OK if framed as additional / co-supporting**; **NOT OK if framed as the controlling argument** (the controlling argument is Harper's-RATIFIED-canonical-text precedence; Amendment D is corroborating).

### §6.2 T3.1 wash de-weighting

If §9.6 claims the T3.1 wash is de-weighted as LOW projected-downstream and this reduces recommendation leverage: per §3 above, T3.1 weight as LOW is likely artifact-class-misapplied. The de-weighting argument would not hold if T3.1 is actually direct end-reader.

### §6.3 Portfolio sweep scope expansion claim

If §9.6 expands scope from "SHIP V-D as-is" to "Pass 3.3/3.4/3.5 Amendment-D-correction sweep across V-D cohort":

- §9.5 reasoning (which §6.3 builds on) is itself conditional on the weight-tag assignment in §9.3 being correct.
- If §9.3 weight-tags are systematically over-crediting LOW + under-crediting HIGH-direct (per §3 above), then propagating §9.3's pattern across the portfolio sweep would propagate the misclassification.
- **Portfolio sweep authorization should not derive from this addendum.** The Atlantic Ideas Amendment-D-weighted audit (`cover-letter-pass-3-3-3-4-3-5-audit_AMENDMENT-D-WEIGHTED_2026-06-01.md`) is a working example for the cover-letter artifact class. If a portfolio sweep is authorized, it should derive from a worked-examples table that correctly distinguishes cover-letter class (direct = editor only; theoretical audiences = projected) from end-reader-facing prose class (direct = all theoretical audiences).

---

## §7. Canonical-pattern role claim (§9.7)

**Verdict: SCOPE-CREEP RISK — claim should not be ratified.**

### §7.1 Aeon empirical anchor framing

The §9.7 claim: "this addendum is the canonical op-ed worked example for Amendment D, parallel to the Aeon Option E.2 γ.1 audit (commit `73c5764`) — editor-pitch worked example."

Independent read of `final-pre-submission-tweak_2026-05-31_pass-3-3-3-4-3-5-audit.md` (commit `73c5764` Aeon Option E.2 γ.1 audit) confirms:

- The audit DOES exist at that path.
- The audit does NOT contain "Amendment D" or "reception-chain" framing in its primary text.
- The audit identifies itself as a "spot-fix precautionary audit on contingency text" for Aeon portal submission, not as an Amendment-D worked example.

**The "Amendment D worked example" framing is being retroactively applied to the Aeon audit by parent sessions after the fact.** Whether this retrofitting is legitimate depends on whether Amendment D's source doctrine explicitly identifies worked examples. Per §1.1 + §2.1 above, the source doctrine section is not on disk — there is no canonical worked-examples list to refer to.

### §7.2 Canonical-pattern categorization in source doctrine

The §9.7 claim requires Amendment D's source doctrine to explicitly call out worked examples by class. The source doctrine on disk does not. The "worked example" categorization is being invented by the McDowell §9 addendum (and propagated by the Atlantic Ideas audit's reference to "the canonical Amendment D worked-examples table").

**Whether the parent session is INVENTING the "worked example" categorization or whether the codification commit `a1f88db` (cited by Atlantic Ideas) did add a worked-examples table to the source doctrine file that is not reflected in the current worktree, cannot be determined without git tooling (which is not permitted in this audit).** Flag for parent-session verification.

### §7.3 Acceptable extension vs scope-creep

If the parent session is inventing the "worked example" categorization to bootstrap an Amendment D codification:

- **Acceptable** if the categorization is internally consistent + the worked examples are actually working (correct artifact-class classification + correct weight-tag assignments + sound re-aggregation math).
- **Scope-creep** if the worked examples have classification errors that would propagate to a portfolio sweep.

Per §2.4 + §3 above, the McDowell §9 addendum likely has artifact-class misclassification (treating end-reader-facing op-ed prose under cover-letter-class semantics). **This makes the canonical-pattern claim scope-creep, not acceptable extension, regardless of whether the source doctrine codified worked examples at `a1f88db`.**

---

## §8. Cross-references + integration

**Verdict: CANNOT-VERIFY (§9 absent from disk).**

If §9 exists as described, integration with §§0–8 of the original 2026-05-28 audit:

- §§0–8 of the original audit are the V-D fresh three-pass independent audit, all of which terminate with the SHIP V-D HYBRID recommendation per §6 + state summary per §7 + cross-references per §8.
- The §9 addendum would be appended after §8. Integration requires either updating §6 to reflect the strengthened recommendation OR explicitly noting that §9 supersedes §6 for ratification routing.
- §9's claim to "strengthen SHIP V-D AS-IS" (§9.6) is consistent with §6's existing SHIP HYBRID recommendation, so integration would be additive rather than superseding.

**However: if §9 does not exist on disk, none of the integration concerns apply.** The recommendation in §10 below addresses this directly.

---

## §9. Findings

### §9.H1 (HIGH severity) — §9 addendum absent from canonical-path file

**Finding statement.** The Workstream C kickoff describes parent-session-authored §9 "Reception-chain audience weighting addendum (Amendment D retroactive application)" added at commit `1f64da1` to the McDowell V-D fresh three-pass independent audit. The file at the canonical path `publishing/op-eds/mcdowell-county-true-cost/_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md` (877 lines on disk; verified via wc -l + Read at line 872-877) ends at §8 Cross-references + the original 2026-05-28 closing block. **There is no §9 anywhere in the file.** Grep for "Amendment D" / "§9" / "reception-chain" / "weighting addendum" returns 0 matches across the full 877 lines.

**Location anchor.** `publishing/op-eds/mcdowell-county-true-cost/_archive/parallel-drafts_2026-05-28/mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md` lines 870-877 + global file grep.

**Options.**

- **(a) REVERT-AND-REWORK (Recommended).** Parent session reverts commit `1f64da1` claim. Author + PM determine whether the §9 addendum was (i) lost in a worktree-sync failure, (ii) committed to a different file path, (iii) never actually written to disk despite the parent's claim, or (iv) committed to a feature branch not merged to main. If §9 should exist, the parent session re-creates it from scratch using the corrected weight-tag scheme (per §9.M1 below).

- **(b) RATIFY-AS-EXECUTED.** Treat the §9-absence as a documentation gap and RATIFY the canonical-pattern claim anyway. **NOT RECOMMENDED**: ratifying a canonical pattern that does not exist on disk would propagate phantom-pattern through the portfolio sweep.

- **(c) SPOT-FIX.** Add §9 to the file based on Workstream C kickoff description. **NOT RECOMMENDED**: the kickoff description embeds the artifact-class misclassification flagged in §9.M1; spot-fixing would commit the misclassification.

**Recommendation: (a) REVERT-AND-REWORK.**

**Reasoning.** Cannot canonical-pattern a phantom. The §9 addendum is the entire subject of the audit; its non-existence on disk at the canonical path is dispositive. Per CLAUDE.md merge-on-ratification rule, ratifying a §9 that does not exist on disk would commit nothing to the file but would mis-document portfolio-sweep authorization. Per the Workstream C scope statement — "this addendum is intended to set the canonical pattern for the broader portfolio sweep" — the absence-from-disk finding blocks the canonical-pattern claim until the §9 content is actually on disk + verified.

---

### §9.M1 (MEDIUM severity) — Artifact-class misclassification risk in §9 description

**Finding statement.** Per the Workstream C kickoff description of §9 content, the addendum treats Tier 2 specialist characters (T2.1 / T2.2 / T2.3) as MEDIUM-to-LOW (consultant → projected downstream) and Tier 3 cultural-resonance characters (T3.1 center-right policy aide; T3.2 McDowell resident) as LOW (projected downstream). Per the v3.0 doctrine §1.1 + the Atlantic Ideas Amendment-D-weighted audit precedent, end-reader-facing prose (essay / chapter / op-ed) treats all theoretical audiences as **direct readers**, with projected-downstream weighting applying only to cover-letter and editor-pitch classes. The McDowell op-ed is end-reader-facing prose; theoretical audiences should be direct, not projected-downstream.

**Location anchor.** §9.2 reception-chain map + §9.3 per-character weight-tag assignment (notional — file content not on disk; per Workstream C kickoff description).

**Options.**

- **(a) Re-classify Tier 2 + Tier 3 as direct end-reader.** All 9 characters direct; weighting uniform; re-aggregation defaults to the original §2.2 NET INCLUDE — DECISIVE verdict. Amendment D weighting becomes a verbal frame (acknowledging that gating editors carry highest practical leverage) without changing the underlying signal.

- **(b) Hybridize: HIGH-direct for Tier 1 + Tier 3.3 general subscriber; HIGH-direct for Tier 2 specialists (substantive end-readers); HIGH-direct for Tier 3 cultural-resonance.** All characters direct; weighting differentiates editorial-gating (Tier 1) from substantive-end-reader (Tier 2 + 3) but neither is projected-downstream. Aggregate verdict unchanged.

- **(c) Preserve cover-letter-class semantics.** Apply Amendment D as kickoff describes (MEDIUM-LOW range tags + LOW projected-downstream for Tier 3). **NOT RECOMMENDED**: artifact-class misclassification + propagation risk for portfolio sweep.

**Recommendation: (a) or (b).** Either treats the McDowell op-ed correctly as end-reader-facing prose. Choice between (a) and (b) is a verbal-frame decision (whether to introduce within-tier weight differentiation among direct readers).

**Reasoning.** End-reader-facing prose ≠ editor-pitch / cover-letter prose. Amendment D's reception-chain weighting machinery was designed for artifact classes where the immediate prose-reader is distinct from the eventual end-audience (cover letter → essay → reader). For end-reader-facing prose, the reception chain collapses (reader = end-reader); weighting differentiates editorial-gating from substantive-end-reader within the direct band, but does not introduce projected-downstream as a separate weight tier.

---

### §9.M2 (MEDIUM severity) — Source doctrine reference path mismatch

**Finding statement.** The §9 addendum (per Workstream C kickoff) cites `tools/drafting-templates/audience-pressure-test-construction.md` §"Reception-chain audience weighting (Amendment D, ratified 2026-05-31)" as the canonical source. Independent read of that file on disk (296 lines; v3.0-labeled) finds zero matches for "Amendment D" / "Reception-chain" / "ratified 2026-05-31". The Atlantic Ideas Amendment-D-weighted audit (`cover-letter-pass-3-3-3-4-3-5-audit_AMENDMENT-D-WEIGHTED_2026-06-01.md`) likewise references this path + cites commit `a1f88db` as the codification commit. Either (i) commit `a1f88db` exists but the worktree state is stale, (ii) commit `a1f88db` modified a different file, or (iii) Amendment D codification is incomplete (commit-message-only without file-content updates).

**Location anchor.** `tools/drafting-templates/audience-pressure-test-construction.md` (full file; 296 lines).

**Options.**

- **(a) Author / PM verifies codification commit `a1f88db` lands Amendment D content in source doctrine file.** If verified + present on origin/main but not on current worktree: refresh worktree. If verified absent on origin/main: re-codify.

- **(b) Author / PM updates v3.1 pipeline doctrine memory** (`tools/memory/feedback_audience_aware_drafting_discipline.md`) to add Amendment D to the codified amendment list. Currently lists A + B + C only.

- **(c) Status-quo: leave source doctrine without Amendment D text.** **NOT RECOMMENDED**: working audits invoke Amendment D as binding; the absence of source-doctrine text leaves those invocations un-anchored.

**Recommendation: (a) + (b) jointly.** Source doctrine should explicitly carry Amendment D text + worked-examples table (if applicable); v3.1 pipeline doctrine memory should be updated to reflect the Amendment D codification.

**Reasoning.** The codification needs to land in BOTH the canonical doctrine artifact AND the memory pointer. The Atlantic Ideas audit treats Amendment D as binding doctrine; the McDowell §9 addendum (when restored) likewise; downstream portfolio sweep audits will likewise. The codification needs canonical source-text on disk.

---

### §9.L1 (LOW severity) — Aeon empirical anchor retroactive reclassification

**Finding statement.** The §9 addendum (per kickoff) characterizes the Aeon Option E.2 γ.1 opener-contingency audit (commit `73c5764`) as the "editor-pitch worked example for Amendment D." Independent read of that Aeon audit confirms it does not self-identify as an Amendment-D worked example — it identifies as a precautionary spot-fix audit on contingency text for the Aeon portal submission. The "Amendment-D worked example" framing is retroactive (post-Aeon-audit) and propagates from the codification commit's framing of the Aeon audit as the empirical anchor.

**Location anchor.** `publishing/essays/aeon-mask-of-abundance/rigor/final-pre-submission-tweak_2026-05-31_pass-3-3-3-4-3-5-audit.md` (header + §0).

**Options.**

- **(a) HOLD per discipline.** Retroactive empirical anchoring is normal pipeline-discipline practice; the v3.0 + v3.1 pipeline doctrines were each ratified citing pre-existing empirical anchors as evidence. Aeon Option E.2 γ.1 = Amendment D's empirical anchor is consistent with the pattern.

- **(b) Add explicit retroactive-classification note to source doctrine.** When Amendment D source-doctrine text is restored (per §9.M2), include a note flagging that the Aeon Option E.2 γ.1 audit is RETROACTIVELY classified as the worked example for the editor-pitch class. This avoids the appearance of doctrine-canon-from-thin-air.

**Recommendation: (b).**

**Reasoning.** Consistent with the pipeline doctrine's existing practice of explicit empirical-anchor citations; helps future auditors understand the lineage.

---

## §10. Phase 4 ratification recommendation

**Recommendation: REVERT-AND-REWORK.**

The Workstream C parent-session §9 addendum at commit `1f64da1` cannot be RATIFIED-AS-EXECUTED because **§9 does not exist on disk at the canonical path**. Three orthogonal disposals are available:

1. **REVERT-AND-REWORK (RECOMMENDED).** Revert the canonical-pattern claim. Parent session investigates why §9 did not land on disk despite the claim (worktree-sync failure? wrong file path? feature-branch-only? commit-message-claim-without-file-write?). If §9 should exist, re-author from scratch using the corrected weight-tag scheme per §9.M1 Option (a) or (b) + restore Amendment D source-doctrine text per §9.M2. **Then re-run an independent audit on the restored §9 with corrected weight-tags.**

2. **RATIFY-AS-EXECUTED.** Treat as a documentation gap; canonical-pattern claim stands. **NOT RECOMMENDED**: ratifying phantom canonical pattern propagates errors through the portfolio sweep. CLAUDE.md merge-on-ratification rule does not apply to non-existent file content.

3. **SPOT-FIX-AND-RATIFY.** Add §9 to disk based on the Workstream C kickoff description. **NOT RECOMMENDED**: the kickoff description embeds the artifact-class misclassification flagged in §9.M1. Spot-fixing would commit the misclassification, which would then propagate through the portfolio sweep.

### §10.1 Pre-conditions for re-fire

Before any §9 addendum (corrected per §9.M1) can claim canonical-pattern role for the portfolio sweep:

- **§9.M2 prerequisite**: Source doctrine `tools/drafting-templates/audience-pressure-test-construction.md` must contain Amendment D text on disk (currently absent at v3.0-labeled 296-line file state). Verify codification commit `a1f88db` content + refresh worktree if necessary, OR re-codify.
- **§9.M1 prerequisite**: Weight-tag assignment must correctly classify the McDowell op-ed as end-reader-facing prose (theoretical audiences as direct; not as projected-downstream).
- **Memory pointer prerequisite**: `tools/memory/feedback_audience_aware_drafting_discipline.md` must add Amendment D to the codified amendment list (currently lists A + B + C only).
- **Aeon worked-example anchor prerequisite**: Add explicit retroactive-classification note to source doctrine when restored (per §9.L1 Option (b)).

### §10.2 Portfolio sweep scope authorization deferred

The Workstream C kickoff states: "This addendum is intended to set the canonical pattern for the broader portfolio sweep of the 2026-05-28 V-D cohort (~10 essays + 2 op-eds). Errors in the pattern propagate to the whole portfolio sweep."

The audit's finding is that the §9 addendum, as the canonical-pattern artifact, is either (i) not on disk, or (ii) on disk with structural errors (per §9.M1) that would propagate through the sweep. **Portfolio sweep authorization should be deferred until the §9 addendum is on disk + verified clean against §9.M1 prerequisites.**

### §10.3 SHIP V-D recommendation unchanged

The original §6 SHIP V-D HYBRID recommendation in the 2026-05-28 audit remains the operative ratification recommendation for the McDowell op-ed itself. The §9 addendum was claimed to "strengthen" SHIP V-D AS-IS — this strengthening claim is undisturbed by the §9-absence finding because the original recommendation already stands on hard-rule axis PASS + Pass 3.3 NET INCLUDE — DECISIVE + Pass 3.4 ROBUST + Pass 3.5 RESTORATION-NOT-WARRANTED grounds. Amendment D adds rhetorical weight; the underlying verdict was settled at 2026-05-28.

---

## §11. State summary (one-liner per chip integrity discipline)

```
STATE: workstream-C-amendment-D-addendum-audit PROPOSED;
verdict REVERT-AND-REWORK (§9 absent from canonical-path file);
artifact-class misclassification risk flagged in §9 description;
NEXT: parent-session investigates §9 disk-state + re-authors with corrected weight-tags;
AWAITING: parent-handoff + author-ratification
```

---

## §12. Cross-references

- Audited (claimed) artifact: [`mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md`](mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md) — read verified, §9 not present
- Canonical Amendment D source doctrine (cited path; §-section not on disk): [`../../../../../tools/drafting-templates/audience-pressure-test-construction.md`](../../../../../tools/drafting-templates/audience-pressure-test-construction.md) — read verified at 296 lines, v3.0-labeled, no Amendment D content
- v3.1 pipeline doctrine memory: [`../../../../../tools/memory/feedback_audience_aware_drafting_discipline.md`](../../../../../tools/memory/feedback_audience_aware_drafting_discipline.md) — codifies Amendments A + B + C; no Amendment D
- Aeon empirical anchor (Option E.2 γ.1 audit): [`../../../../essays/aeon-mask-of-abundance/rigor/final-pre-submission-tweak_2026-05-31_pass-3-3-3-4-3-5-audit.md`](../../../../essays/aeon-mask-of-abundance/rigor/final-pre-submission-tweak_2026-05-31_pass-3-3-3-4-3-5-audit.md) — does not self-identify as Amendment-D worked example
- Working Amendment-D-weighted audit (cover-letter class): [`../../../../essays/atlantic-ideas-pricing-honestly/rigor/cover-letter-pass-3-3-3-4-3-5-audit_AMENDMENT-D-WEIGHTED_2026-06-01.md`](../../../../essays/atlantic-ideas-pricing-honestly/rigor/cover-letter-pass-3-3-3-4-3-5-audit_AMENDMENT-D-WEIGHTED_2026-06-01.md) — cites Amendment D codification at commit `a1f88db`; cites same source-doctrine path
- McDowell op-ed canonical (LOCKED): [`../../op-ed.md`](../../op-ed.md)
- V-D hybrid (audit subject of original 2026-05-28 audit): [`mcdowell-op-ed_hybrid_best-of-both.md`](mcdowell-op-ed_hybrid_best-of-both.md)

---

*End of Workstream C — Amendment-D Retroactive Addendum Independent Audit — 2026-06-01. PROPOSED; recommendation REVERT-AND-REWORK on the load-bearing finding that the parent-session-claimed §9 addendum at commit `1f64da1` is not on disk at the canonical path. Per merge-on-ratification, this internal-scaffolding audit fast-forwards to main at parent-session close.*
