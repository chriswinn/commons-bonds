# Pass 3.1 light-touch verification — NBIM AR 2023 external-lookup follow-up [PROPOSED]

**Date:** 2026-06-01
**Status:** PROPOSED — awaiting author ratification.
**Pass type:** Stage 3 Pass 3.1 external-lookup follow-up chip (single quantitative
claim verification deferred from predecessor [`pass-3-1-verification_VERSION-D-backports_2026-06-01.md`](pass-3-1-verification_VERSION-D-backports_2026-06-01.md)
§Citation 2).
**Workstream:** Wave 2 Candidate C — Foreign Affairs derivative essay; V-D Hybrid
backport Citation 2 (NBIM AR 2023 figures) pre-Phase-C verification.
**Artifact audited:** single half-clause at V-D line 107 (NBIM AR 2023 quantitative
claim). V-D Hybrid prose at
[`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md).
**Verification scope:** two quantitative sub-claims:
1. NBIM AR 2023 equity holdings in **roughly 9,000** publicly listed companies.
2. NBIM AR 2023 holdings across **more than 70** markets.

**Tool envelope (this session):** WebSearch + WebFetch were denied at the sandbox
level for this verification chip as well — the same denial pattern that scoped the
predecessor chip's UNVERIFIABLE-AT-CHIP-SCALE flag. This chip therefore cannot
independently close the loop on the exact NBIM AR 2023 published figures. What it
CAN do: (1) document the denial pattern transparently so the predecessor chip's
"Option A sequential clear" recommendation surfaces unchanged; (2) cross-check the
in-repo corpus for any prior verified NBIM scale figure; (3) reaffirm
substrate-safety on the structure-only revision recommendation; (4) provide a
clean handoff for author or future-session manual nbim.no verification.

**Substrate-safety hard rule applied throughout:** no invented figures or invented
"verified" confirmations generated. Per
[`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md):
sub-agent verification cannot generate a numerical "verified" figure from training
priors without portal access — that would be exactly the
fabrication-propagation-from-essay-to-book failure mode the hard rule exists to
prevent.

---

## §0. Sources consulted

### Intended external sources (sandbox-denied this chip)

The verification protocol from the parent paste-text named four authoritative
sources, all of which require live web access:

1. **NBIM 2023 Annual Report** — expected canonical URL pattern
   `https://www.nbim.no/en/publications/reports/2023/annual-report-2023/` (per
   NBIM's standard publishing convention; the 2022 Annual Report follows
   `.../publications/reports/2022/annual-report-2022/` and the 2024 Annual
   Report follows `.../publications/reports/2024/annual-report-2024/`).
2. NBIM press releases / official communications around the 2023 reporting
   period (typically published Q1 2024 with the AR drop).
3. Major financial-press coverage citing NBIM AR 2023 (FT, Bloomberg, Reuters,
   WSJ — usually a brief recap on the AR publication date).
4. NBIM portfolio-explorer at `nbim.no/en/the-fund/investments/` — gives a
   year-end snapshot of investments-by-company-count + investments-by-country
   count.

**Sandbox status:** WebSearch + WebFetch both denied for this chip; no live access
to any of the above. The denial is identical to the predecessor verification
chip's denial — see [`pass-3-1-verification_VERSION-D-backports_2026-06-01.md`](pass-3-1-verification_VERSION-D-backports_2026-06-01.md)
§0 "External (sandbox-denied for this chip)" for the parallel disposition.

### In-repo cross-reference corpus (consulted)

1. Predecessor verification chip:
   [`pass-3-1-verification_VERSION-D-backports_2026-06-01.md`](pass-3-1-verification_VERSION-D-backports_2026-06-01.md)
   §Citation 2 — flagged NEEDS-REVISION-FIRST pending 5-minute external lookup;
   characterized the figures as "order-of-magnitude correct" + "in the right
   order of magnitude and approximately right for fiscal 2023" at the
   sub-agent-general-knowledge level, but explicitly did NOT raise to
   verified-precise.
2. V-D Hybrid originating prose at
   [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md)
   line 107 — verbatim citation text confirmed: "the 2023 *NBIM Annual Report*
   recorded equity holdings in roughly nine thousand publicly listed companies
   across more than seventy markets."
3. Alt-no-em parent draft:
   [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md)
   line 67 — originating prose: "the 2023 *NBIM Annual Report* recorded equity
   holdings in roughly nine thousand publicly listed companies." (NOTE: alt-no-em
   parent does NOT carry the ">70 markets" tail; V-D extends parent with the
   geographic-breadth clause.)
4. Harvest-hybridization spec:
   [`harvest-hybridization-spec_2026-05-28.md`](harvest-hybridization-spec_2026-05-28.md)
   §3 Edit 4 — explicit verification flag: "verify against NBIM's published
   figure at https://www.nbim.no" as Pass 3.1 step before Phase C.
5. AUDIT-2 §6.1 substrate-safety table —
   [`pass-3-3-3-4-and-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-2_2026-05-28.md`](pass-3-3-3-4-and-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-2_2026-05-28.md)
   F-3.5-V-D-3 — NBIM AR site verdict: ✓ SAFE at institutional-reporting +
   widely-referenced-figure level; "moderate confidence — widely-referenced
   figure" qualification preserved.
6. Drafter's-self-audit:
   [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md)
   §8 #3 — drafter-self confidence: moderate; explicit Pass 3.1 verification
   flag.
7. Canonical Norway case study:
   [`research/case-studies/norway-swf.md`](../../../../research/case-studies/norway-swf.md)
   — repo-side Norway fund material; no prior in-repo verified figure for
   "9,000 companies" or "70+ markets" found (grep returned zero hits for
   `9,000` / `9000` / `nine thousand` / `seventy` / `70 mark` / `NBIM`
   variants).
8. Ch 6 manuscript anchor:
   [`manuscript/chapters/Chapter__6_ThreeWaysofCounting.md`](../../../../manuscript/chapters/Chapter__6_ThreeWaysofCounting.md)
   line 219 — carries the verified-at-Stage-3 NBIM figure: "approximately $2.2
   trillion (early 2025 NBIM)" for fund AUM. This is the only NBIM-quantitative
   anchor with prior rigor-pass clearance in the repo. **It does NOT cover the
   companies-count or markets-count axes.** The Ch 6 figure is a different
   sub-claim (fund AUM) verified at a different reporting moment (early 2025,
   not fiscal 2023).
9. Bibliography:
   [`research/literature/bibliography.md`](../../../../research/literature/bibliography.md)
   — no bibliography entry for NBIM Annual Report; the NBIM AR 2023 is an
   essay-specific citation not previously bibliographically anchored.

---

## §1. Per-claim verification

### Sub-claim A — "~9,000 publicly listed companies"

**V-D phrasing:** "equity holdings in roughly nine thousand publicly listed
companies."

**Actual figure from NBIM AR 2023:** **UNVERIFIABLE-AT-CHIP-SCALE.** This chip
cannot independently confirm the exact fiscal-2023 published figure without live
nbim.no access. The predecessor chip's §Citation 2 characterizes the figure as
"order-of-magnitude correct" + "approximately right for fiscal 2023" at
sub-agent-general-knowledge level — that characterization is preserved here as
the highest-confidence statement this chip can make. The hedged "roughly nine
thousand" phrasing carries appropriate imprecision relative to whatever the
exact published figure is.

**Status: UNVERIFIABLE-AT-CHIP-SCALE — DEFER-TO-AUTHOR-MANUAL-LOOKUP.**

Not a NEEDS REVISION on the figure itself (no replacement figure can be
authored within substrate-safety constraints); not a VERIFIED on the precise
figure (no portal access). The disposition is: structurally the prose is
substrate-safe and hedged-correct at the order-of-magnitude level the
verification chip CAN reach; the precise-figure verification step remains a
5-minute author-or-future-session manual check.

### Sub-claim B — ">70 markets"

**V-D phrasing:** "across more than seventy markets."

**Actual figure from NBIM AR 2023:** **UNVERIFIABLE-AT-CHIP-SCALE.** Same
sandbox-denial pattern as Sub-claim A. The predecessor chip characterized this
as "order-of-magnitude correct" + "70+ markets is order-of-magnitude consistent
with recent-year NBIM reporting" at sub-agent-general-knowledge level — that
characterization is preserved.

**Additional flag carried over from predecessor chip:** this clause is a V-D
extension that does NOT appear in the alt-no-em parent draft line 67. The
">70 markets" tail was harvested into V-D as a register-amplification move; the
drafter's-self-audit §8 #3 flagged only the company-count figure, not the
markets-count figure separately. This chip preserves that flag.

**Status: UNVERIFIABLE-AT-CHIP-SCALE — DEFER-TO-AUTHOR-MANUAL-LOOKUP.**

Same disposition as Sub-claim A. Hedged "more than seventy" phrasing carries
appropriate imprecision; substrate-safe at the order-of-magnitude level; precise
figure requires 5-minute author manual check.

---

## §2. Recommended revision (structure-only, substrate-safety preserved)

Three Phase-C-eligible dispositions, in author-decision-table form:

| Option | Disposition | Phase C action | Substrate-safety verdict |
|---|---|---|---|
| **A. Hedged-tolerance apply** | Apply V-D citation 2 as drafted; hedge phrasings ("roughly," "more than") cover the precise-figure verification gap; substrate-safety hard rule is preserved by NOT changing the figures absent verified replacement | Apply V-D line 107 verbatim at Phase C alongside citations 1, 3, 4 | ✓ SAFE — no fabricated replacement; hedged phrasing carries appropriate imprecision |
| **B. Defer-with-elision** | Defer the entire NBIM AR 2023 sentence at Phase C; apply only citations 1, 3, 4; preserve V-D line 107 as a pending-verification anchor for the next pre-pub refresh | Skip V-D line 107 at this Phase C; surface a follow-up paste-text to author for manual 5-minute nbim.no lookup before next session integrates the sentence | ✓ SAFE — sentence not in essay.md so no figure-precision risk; institutional-register amplification deferred |
| **C. Defer-with-author-manual-lookup** | Hold Phase C application of citation 2 specifically pending author's 5-minute manual nbim.no check; surface the lookup as an action item; integrate sentence once author returns the verified figures (or confirms current figures match V-D hedged phrasing) | Skip V-D line 107 at THIS Phase C pass; author manual lookup → second-pass Phase C integration | ✓ SAFE — no figure-precision risk between now and author confirmation |

**Recommendation: Option A.** Reasoning: (1) the hedged phrasings ("roughly nine
thousand" + "more than seventy") are explicitly designed to be tolerant of
small-percentage drift around the precise published figure; (2) the predecessor
chip already characterized both figures as "order-of-magnitude consistent with
recent-year NBIM reporting" — i.e., the consultable-via-general-knowledge
estimate sits squarely inside the hedged range; (3) AUDIT-2 §6.1 +
F-3.5-V-D-3 already certified the citation substrate-safe at
institutional-reporting register; (4) Option A preserves load-bearing
register-amplification work (Tier 1 #3 SWF practitioner + Tier 2 #8
Norway-cluster scholar audience signals) that B and C strip out of Phase C; (5)
the author-or-external-reviewer Stage 5 pre-pub queue is the standard discipline
home for precise-figure refresh — pushing the precise-figure check to that
later gate is exactly the "pre-publication review queue" mechanism the v3.1
doctrine was designed for; (6) Option A is consistent with the predecessor
chip's §3 OPTION A sequential-clear recommendation extended to citation 2 with
hedged-precision tolerance.

**If author prefers higher confidence pre-Phase-C:** Option C (5-minute manual
nbim.no lookup → confirm-or-revise → integrate) is the substrate-safety-cleanest
upgrade. This chip does NOT generate the precise replacement figures (substrate-
safety hard rule); the author's manual lookup result becomes the substrate for
any subsequent Phase C revision.

### Structure-only revision specification (for Option C path or for any future
revision of the figures)

If the author's manual lookup returns figures different from V-D's hedged
phrasings, the structure-only revision specification is:

- **Citation form NBIM AR uses:** the NBIM Annual Report conventionally cites
  itself as *Annual Report [year]* with NBIM as institutional author; the
  bibliographic form for a Foreign Affairs essay footnote (FA's house style
  uses endnotes, not footnotes, with Chicago-Manual-style attribution) would
  approximate: `Norges Bank Investment Management, "Annual Report 2023" (Oslo:
  Norges Bank Investment Management, 2024), [page/section anchor].` The exact
  page/section anchor for the companies-held + markets-held figures should be
  carried forward from the manual-lookup author's record.
- **Replacement-figure insertion pattern:** if the actual figure differs from
  9,000 by a small margin (e.g., 8,800 or 9,200), replace "roughly nine
  thousand" with the actual figure in word form OR with "roughly [actual figure
  in word form]" preserving the hedged phrasing. Do NOT delete the hedged
  qualifier — the qualifier carries appropriate epistemic humility about
  year-end snapshot vs running-total reporting differences.
- **Markets-count replacement pattern:** parallel structure for ">70 markets"
  — replace "more than seventy" with the actual figure in word form OR with
  "more than [actual figure in word form]" preserving the hedged qualifier.
- **DO NOT delete the clause** — the institutional-register-amplification work
  (NBIM Annual Report as the canonical reference; the scale-anchoring detail
  for Tier 1 SWF practitioner + Tier 2 Norway-cluster scholar audiences) is
  load-bearing per AUDIT-2 §6.1 + Pass 3.5 F-3.5-V-D-3.

**Substrate-safety reaffirmation:** this verification chip does NOT generate the
replacement figures. The author's manual nbim.no lookup is the substrate. If
the lookup confirms V-D's hedged phrasings are within the hedge tolerance,
Phase C applies V-D verbatim per Option A. If the lookup returns
out-of-hedge-tolerance figures, the author or a subsequent session applies the
structure-only revision specification above with the lookup-sourced precise
figures.

---

## §3. Phase C gate-status update

**Per-sub-claim gate status:**

- Sub-claim A (~9,000 companies): **UNVERIFIABLE-AT-CHIP-SCALE.**
- Sub-claim B (>70 markets): **UNVERIFIABLE-AT-CHIP-SCALE.**

**Aggregate Phase C gate disposition: UNVERIFIABLE-AT-CHIP-SCALE → CLEAR-TO-APPLY-UNDER-OPTION-A
(hedged-precision tolerance) / DEFER-FOR-MANUAL-LOOKUP-UNDER-OPTION-C
(higher-precision-pre-Phase-C).** Author selects between Option A (apply now;
defer precise-figure refresh to Stage 5 pre-pub queue) and Option C (5-minute
manual nbim.no lookup → integrate).

**Predecessor-chip handoff status update:** the predecessor chip's
[`pass-3-1-verification_VERSION-D-backports_2026-06-01.md`](pass-3-1-verification_VERSION-D-backports_2026-06-01.md)
§Citation 2 NEEDS-REVISION-FIRST disposition was explicitly conditional on this
follow-up external-lookup chip resolving the precise-figure verification. This
chip CANNOT resolve that verification under the sandbox-denial envelope; the
disposition therefore EITHER converts to CLEAR-TO-APPLY-UNDER-OPTION-A (if
author accepts hedged-precision tolerance) OR remains NEEDS-REVISION-FIRST under
Option C (deferred to author manual lookup). The predecessor chip's §3 OPTION A
sequential-clear recommendation extended to citation 2 with hedged-precision
tolerance is the substrate-safety-clean default.

**Recommendation surfaced to author:**

1. **Apply citations 1, 3, 4** at Phase C immediately (predecessor chip §3
   OPTION A unchanged).
2. **Apply citation 2 under Option A (hedged-precision tolerance)** unless the
   author wants higher pre-Phase-C precision — substrate-safety preserved by
   the hedged phrasings; pre-pub Stage 5 queue carries the precise-figure
   refresh as standard discipline.
3. **OR defer citation 2 under Option C** if the author wants to do the
   5-minute manual nbim.no lookup before Phase C application — substrate-safety
   preserved by NOT integrating until lookup confirms.

Either path is substrate-safe. Author's call on the precision-vs-latency
trade-off.

---

## §4. Cross-references

**Predecessor + parent rigor artifacts:**

- Predecessor verification chip:
  [`pass-3-1-verification_VERSION-D-backports_2026-06-01.md`](pass-3-1-verification_VERSION-D-backports_2026-06-01.md)
  §Citation 2 — flagged the need for this follow-up.
- V-D Hybrid prose:
  [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md)
  line 107.
- Alt-no-em parent draft:
  [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md)
  line 67 (originating prose without >70-markets tail).
- AUDIT-2 substrate-safety verdict:
  [`pass-3-3-3-4-and-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-2_2026-05-28.md`](pass-3-3-3-4-and-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-2_2026-05-28.md)
  §6.1 + F-3.5-V-D-3.
- Drafter's-self-audit:
  [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md)
  §8 #3.
- Harvest-hybridization spec:
  [`harvest-hybridization-spec_2026-05-28.md`](harvest-hybridization-spec_2026-05-28.md)
  §3 Edit 4.
- Stage 5 sign-off:
  [`../stage-5-signoff.md`](../stage-5-signoff.md) — pre-pub queue discipline.

**Doctrine + memory anchors:**

- Substrate-safety hard rule:
  [`../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md)
  — the basis for refusing to author "verified" figures absent portal access.
- Verify time-sensitive claims in stale memories:
  [`../../../tools/memory/feedback_verify_stale_memory_claims.md`](../../../../tools/memory/feedback_verify_stale_memory_claims.md)
  — institutional-report figures are exactly the category this discipline
  applies to.
- Audience-aware drafting v3.1:
  [`../../../tools/memory/feedback_audience_aware_drafting_discipline.md`](../../../../tools/memory/feedback_audience_aware_drafting_discipline.md)
  — Pre-publication review queue is the canonical home for deferred
  precise-figure refreshes.
- Merge-on-ratification:
  [`../../../tools/memory/feedback_merge_on_ratification.md`](../../../../tools/memory/feedback_merge_on_ratification.md)
  — this verification artifact is internal scaffolding; auto-merges to main at
  session close per the standard scaffolding discipline.

---

**Verification artifact owner:** session via paste-text kickoff 2026-06-01;
verification chip PROPOSED 2026-06-01 (status awaiting author selection between
Option A hedged-tolerance apply / Option B defer-with-elision / Option C
defer-with-manual-lookup).

**Next step:** author selects Phase C disposition for citation 2 (Option A
recommended; Option C if higher pre-Phase-C precision desired); Phase C kickoff
for V-D backport application proceeds with citations 1, 3, 4 immediately under
the predecessor chip's §3 OPTION A sequential-clear path regardless of which
citation-2 option the author selects.
