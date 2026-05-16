# Manuscript Stage-3 Phase A — Ch 8 Pass 1 (Fact-Check) paste-text

**Date drafted:** 2026-05-15
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20) — Phase A — Ch 8 — Pass 1 (fact-check)
**Phase scope:** Pass 1 ONLY. v2.0 Amendment B distinct-pass discipline + per-prompt serial cadence (Pass 1 → spot-fix → Pass 2 → spot-fix → Pass 3 → spot-fix; not bundled).
**Recommended branch at session start:** `claude/manuscript-stage-3-ch8-pass1-<harness-id>` from current `origin/main` (head verified at `7b4aa92` 2026-05-15) after `git fetch`.

---

## Why Ch 8 Pass 1 now

Ch 8 (What Things Actually Cost — per-ton McDowell coal arithmetic; 8 cost components; floor-conservative methodology) is the chapter where the framework's numerical climax lands. Pass 1 is the highest-stakes fact-check in the manuscript because every cost-component number is independently challengeable.

**Specific landmines for Ch 8:**
- **$4.50 / ton 1960 mine-mouth coal price.** Historical claim (Ch 8:25). Verify against 1960 BLS / EIA / industry price records.
- **Kennedy 1960 McDowell visit / mine scene.** Ch 8:25 ("the mine Kennedy stood near in 1960"). Verify date + location + scene specifics; cross-reference Ch 2's Kennedy/JFK content (Ch 2 Phase A Pass 1 already verified some JFK claims at commit `1130c67`).
- **Per-ton cost-component arithmetic.** Eight cost components (Cᵢ); each is a numerical claim that must roll up to the chapter's floor figure. Verify each Cᵢ value + the addition.
- **$44B Program-vs-Trust-Fund drift.** Ch 8 lines 35 + 39 corrected 2026-05-15 (`cacb82d`) to match Ch 5 line 226 / Ch 6 line 21 canonical (Program is umbrella; Trust Fund is within-Program funding mechanism that carries the debt). Verify the fix is intact. Verify no other Program-vs-Trust-Fund instances elsewhere in Ch 8 still carry drift.
- **$100 barrel reference at line 71.** Per workstream handoff line 70 ("Ch 8 line 71 stale `$100 barrel` reference (need to verify if patched by #10 or cross-thread #9 still pending)"). Verify current state of line 71.
- **Black-lung trust fund (Ch 2↔Ch 6↔Ch 8 lineage).** Cross-chapter consistency. Verify Ch 8's black-lung trust fund claims match Ch 2 + Ch 6.
- **Inline integral stripped per Item 1.** Commit `d1f6e2d` removed an inline integral; verify no regression (no integral symbols, no Greek apparatus in Ch 8 body prose).
- **Dunbar / Du Bois / Ellison / Fanon engagement.** Applied 2026-05-08. Verify each citation is accurate (dates of published works; titles; argument attributions).

---

## Filled paste-text — fire in a fresh session

```
You are running Phase A Pass 1 (fact-check) of the Manuscript Stage-3
Rigor Pass workstream (PM dashboard #20) for Chapter 8 — What Things
Actually Cost. Your job: apply v2.0 Amendment B fact-check discipline
(one distinct pass; not bundled with voice-polish or audience-load) to
the chapter file at
manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md. STOP at
verdict + spot-fix recommendations; do NOT apply spot-fixes to the
chapter file. A separate Phase C session applies ratified spot-fixes
after author ratification.

== v2.0 Amendment B discipline — Pass 1 only ==

Three DISTINCT passes (fact-check + voice-polish + audience-load), not
bundled. This session runs fact-check ONLY. Pass 2 (voice-polish) and
Pass 3 (audience-load) are separate subsequent sessions per the per-
prompt serial cadence. Pass-1-surfaced voice or audience concerns get
flagged forward in §6 / §7 sections of the output artifact.

== Mode: audit-existing-prose ==

Per tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Audit-
existing-prose mode": no Stage 1 brief exists for Ch 8. The chapter
file IS the prose under audit; fact-checks verify against external
canonical sources (historical records, BLS/EIA data, primary
literature, cross-chapter consistency inventory, apparatus register
decisions). Severity-tier classification per Pass 1 standard
(CRITICAL / HIGH / MEDIUM / LOW).

Ch 8 is the manuscript's numerical climax — every cost-component
number is independently challengeable. Pass 1 is the highest-stakes
fact-check in the manuscript.

== Read in order before doing any work ==

1. THIS paste (the framing).
2. manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md —
   the chapter under audit. Read in full. (~242 lines / ~6,026w per
   workstream handoff; verify line count at session start.)
3. tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Pass 1:
   Fact-check" — full severity scale + finding format.
4. tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
   — per-chapter table; Ch 8 row at line 70.
5. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md
   — Ch 4 Pass 1 artifact as canonical format model. Mirror this
   structure (§Canonical sources consulted → §Summary verdict →
   §Findings by severity → §Verified-no-findings table → §Apparatus
   regression check → §Path B contamination check → §Named-subject
   consent check → §Recommendations).
6. manuscript/chapters/Chapter__2_TheMiner__Draft.md — for cross-
   chapter consistency with Ch 8's McDowell coal + Kennedy 1960 +
   black-lung-trust-fund claims.
7. manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html —
   for cross-chapter consistency with Ch 8's black-lung-trust-fund
   claims + cost-severance apparatus.
8. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch2_theminer_factcheck_only_v1.0.0.md
   (or current Ch 2 Pass 1 artifact) — for Kennedy 1960 prior
   verifications. Do NOT re-litigate; cross-reference for consistency.
9. tools/audits/cross-chapter-consistency-inventory_2026-05-11.md —
   canonical-terms + named-cases + recurring-stats (black-lung-trust-
   fund canonical lock; $44B Program-vs-Trust-Fund canonical pattern;
   McDowell coal stats).
10. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md
    — apparatus register canonical decisions (cost severance, Cᵢ
    component register).
11. research/literature/bibliography.md §13 — comp + framework-adjacent
    entries with engagement-state flags (Dunbar, Du Bois, Ellison,
    Fanon citations — verify against bibliography entries).
12. core/terms/terms_index.md — canonical-form check for apparatus
    terms in Ch 8 body prose (cost severance; Cᵢ components;
    Commons Inversion Test / CIT; Four Gates).
13. Recent commits relevant to Ch 8 (verify each exists on origin/
    main):
    - `cacb82d` (2026-05-15) — Ch 2 + Ch 8 $44B Program-vs-Trust-Fund
      correction (Ch 8 lines 35 + 39)
    - `d1f6e2d` — inline integral stripped (Item 1)
    - 2026-05-08 commit — Dunbar/Du Bois/Ellison/Fanon engagement
14. Memory entries:
    - feedback_named_subject_consent.md
    - feedback_verify_stale_memory_claims.md
    - feedback_substance_drives_length.md
    - feedback_audience_aware_drafting_discipline.md

== Per-chapter context ==

**Chapter:** 8 — What Things Actually Cost
**File path:** manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md
**Word count target:** ~6,026w (~242 lines)
**Key named subjects (verify register + consent):** John F. Kennedy
(deceased, public-record historical figure); Dunbar / Du Bois /
Ellison / Fanon (deceased writers, named for engagement). Verify no
living named subjects appear without consent.
**Key named cases:** McDowell County 1960 coal; one ton coal
arithmetic; Cᵢ component examples; black-lung trust fund.

**Specific audit emphases (per workstream handoff line 70 + cross-
thread context):**

- **$4.50 / ton 1960 coal price (Ch 8:25).** Historical claim.
  Canonical sources: BLS Producer Price Index for bituminous coal
  1960; EIA historical coal price tables; industry-specific 1960
  records. Verify the $4.50 figure for mine-mouth bituminous coal in
  Appalachia 1960. If the figure is regionally / quality-tier
  imprecise, flag MEDIUM with proposed tightening.
- **Kennedy 1960 McDowell visit (Ch 8:25).** "The mine Kennedy stood
  near in 1960." Cross-reference Ch 2's Kennedy/JFK content (verified
  in Ch 2 Pass 1, commit `1130c67`). Verify: date, mine name (if
  named), whether Kennedy actually stood near a specific mine or
  whether the chapter's scene-composite is a representational
  framing. Severity HIGH if the scene attributes a specific Kennedy
  visit that didn't occur; MEDIUM if the framing is compressionally
  imprecise.
- **Per-ton cost-component arithmetic (8 components, Ch 8 §-by-§).**
  Each Cᵢ value is an independent fact-check item. Verify:
  - Health costs (black lung disability + healthcare costs per
    affected miner × incidence)
  - Environmental damage (mining-related land + water remediation
    estimates)
  - Community foreclosure costs (long-term economic underperformance
    per affected county)
  - Family / dispersal / knowledge-loss costs (where quantified)
  - Political-maintenance costs (where quantified)
  - Acceleration costs (centuries-into-decades resource consumption
    discount)
  - Any other Cᵢ surfaced in the chapter
  Verify the addition rolls up to the chapter's stated floor
  (likely the $500-$600/ton figure referenced in Ch 9:9).
  Severity HIGH for any cost-component whose underlying citation is
  missing or whose arithmetic doesn't reconcile.
- **$44B Program-vs-Trust-Fund (Ch 8 lines 35 + 39 — VERIFY FIX
  INTACT).** Per commit `cacb82d` (2026-05-15), Ch 8 lines 35 + 39
  were corrected from Trust-Fund-as-payer to Program-as-payer (with
  Trust Fund as the within-Program funding mechanism that carries
  the debt). Verify the fix is intact AND scan the rest of Ch 8 for
  any other Program-vs-Trust-Fund drift instances not caught by the
  2026-05-15 fix.
- **$100 barrel reference at line 71 (verify current state).** Per
  workstream handoff: "Ch 8 line 71 stale `$100 barrel` reference
  (need to verify if patched by #10 or cross-thread #9 still
  pending)." Read Ch 8 line 71 + surrounding context. Determine
  whether the reference is (a) already patched by a prior commit
  (find the commit if so), (b) still stale (flag HIGH if it's a
  Ch 2 $100-barrel residue), or (c) defensible-as-is (different
  context — e.g., a different oil-price-era illustrative figure
  that's accurate).
- **Black-lung trust fund (Ch 2↔Ch 6↔Ch 8 lineage).** Cross-chapter
  consistency. Verify Ch 8's black-lung trust fund claims (legal
  history; payout records; structural design) match Ch 2 + Ch 6
  treatment. Flag any divergence.
- **Inline integral stripped (Item 1, commit `d1f6e2d`).** Verify
  no integral symbols, no Greek-letter apparatus, no formal math
  notation in Ch 8 body prose (Cᵢ subscript usage is permitted per
  the apparatus register).
- **Dunbar / Du Bois / Ellison / Fanon engagement (applied 2026-05-08).**
  Each citation is a fact-check item:
  - Paul Laurence Dunbar — verify published work + year + relevant
    passage if quoted
  - W.E.B. Du Bois — verify published work + year + relevant passage
    if quoted
  - Ralph Ellison — verify published work + year + relevant passage
    if quoted
  - Frantz Fanon — verify published work + year + relevant passage
    if quoted
  Check against research/literature/bibliography.md §13.

== Pass 1: Fact-check ==

For every factual claim in the chapter, verify against canonical
sources. Flag findings by severity:

- **CRITICAL** — claim is factually wrong; publisher pre-publication
  review would flag.
- **HIGH** — claim is misleading or imprecise; could be challenged by
  a knowledgeable reader (Appalachian historian; coal-industry
  economist; black-lung disability researcher; literary scholar).
- **MEDIUM** — claim is technically defensible but loose.
- **LOW** — claim is accurate but framing could be sharpened.

For each finding: cite chapter line number + chapter text + canonical
truth + recommended spot-fix (Option A / B / C where appropriate).

Pay special attention to the $4.50/ton historical price, Kennedy 1960
scene, cost-component arithmetic, $44B fix verification, $100 barrel
line-71 disposition, and the four literary citations.

== Web verification — default mode ==

For numerical claims, dates, historical events, scholarly citations,
scientific facts: DEFAULT to WebSearch / WebFetch against
authoritative sources BEFORE flagging "verify against canonical X"
for later work. Authoritative sources for Ch 8 include:

- BLS (Bureau of Labor Statistics) Producer Price Index historical
  series for 1960 bituminous coal price
- EIA (Energy Information Administration) historical coal price
  tables; West Virginia coal-production records
- JFK Presidential Library + Library of Congress for the 1960
  Kennedy McDowell visit (campaign-trail records; specific dates;
  specific locations)
- NIOSH / OSHA / Department of Labor Black Lung Disability Trust Fund
  records (legal history; payout data; structural design)
- US Department of Labor / Office of Workers' Compensation Programs
  for trust-fund-canonical references
- Peer-reviewed health-economics literature for cost-per-affected-
  miner figures
- Library of Congress / authoritative literary editions for Dunbar
  (Lyrics of Lowly Life 1896; "We Wear the Mask"); Du Bois (The
  Souls of Black Folk 1903); Ellison (Invisible Man 1952); Fanon
  (Black Skin White Masks 1952; The Wretched of the Earth 1961)
- Wikipedia ONLY as a starting-point pointer to primary sources
  (verify the underlying citation; do not cite Wikipedia itself)

Fact-check pass DOES the verification, not "flag for later." If
WebSearch returns conflicting authoritative sources, document the
disagreement (which sources say what) and flag MEDIUM or HIGH per
severity scale.

Flag-for-later is reserved for:
- Internal-corpus-only claims (cross-chapter consistency; $44B fix
  verification against Ch 5/Ch 6 canonical pattern) where the
  verification target is another file in this repo
- Claims requiring manual judgment beyond WebSearch
- Claims where the relevant authoritative source isn't publicly
  indexed

== Apparatus / consistency / named-subject sub-checks (§5 in output) ==

- **Apparatus residue.** Verify post-Item-1 (commit `d1f6e2d`) state:
  no integrals, no Greek letters in body prose. Cᵢ subscript usage
  is permitted; verify it appears only where the apparatus register
  permits.
- **Path B contamination.** Verify no verbatim-clone passages from
  Ch 2 / Ch 6 / Ch 9.
- **Named-subject consent.** Kennedy (deceased, public record;
  no consent issue). Dunbar / Du Bois / Ellison / Fanon (deceased,
  named for engagement; no consent issue). Verify no living named
  subjects appear.
- **Cross-chapter consistency.** Black-lung-trust-fund lineage
  (Ch 2↔Ch 6↔Ch 8); $44B Program-vs-Trust-Fund canonical pattern
  (Ch 5/Ch 6 canonical); McDowell County stats consistency.

== Out-of-scope flagging (§6 + §7 in output) ==

- **§6 Pass-2 (voice-polish) future-session input.** Items that cross
  attention during Pass-1 reading but belong to voice-polish scope.
  Ch 8 voice-emphases will likely cluster around: cost-component
  enumeration cadence (rule-of-three / tidy-parallel risk in 8-
  component walkthrough); numerical-claim flatness (declarative-
  three-in-a-row risk in dollar-value passages); McDowell-scene
  memoir-register interludes vs. analytical-arithmetic register
  shifts.
- **§7 Pass-3 (audience-load) future-session input.** Tier-1
  Appalachian policy reader; Tier-1 quant/economist reader; Tier-1
  trade-press reader pressure-test on whether the $500-$600/ton
  floor figure lands as scholarly or as polemical; Tier-3 Black-
  Studies-resonance reader (Dunbar/Du Bois/Ellison/Fanon engagement
  lands or appropriates?).

== Verdict synthesis (§8 in output) ==

- **§8.1 Findings tally.** Table.
- **§8.2 Aggregate Pass-1 verdict.** READY AS-IS / READY AFTER SPOT-
  FIXES / STRUCTURAL REVISION NEEDED.
- **§8.3 Phase-C disposition recommendation.** Sequenced list.

== Output ==

Single atomic commit on feature branch:
- tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md

== Hard constraints ==

- Do NOT apply spot-fixes to the chapter file.
- Do NOT re-write paragraphs.
- Do NOT score Pass 2 or Pass 3 — flag-forward at §6 / §7.
- Do NOT contact named subjects.
- DO flag any cost-component arithmetic that doesn't reconcile to the
  chapter's stated floor.
- DO flag any apparatus regressions, named-subject consent issues, or
  Path B contamination.
- DO verify the 2026-05-15 $44B fix is intact AND scan for any other
  Program-vs-Trust-Fund drift in the chapter.

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-ch8-pass1-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. Report rigor-pass back to PM session
+ author. Author ratifies which spot-fixes to apply via separate Phase C
session.

== Verify-stale-memory-claims discipline ==

Before asserting any time-sensitive claim:
- Verify chapter file path exists at session start; verify line count.
- Verify commit `cacb82d` exists on origin/main (the $44B fix).
- Verify commit `d1f6e2d` exists on origin/main (Item 1 inline-
  integral strip).
- Verify cost-component canonical figures against current literature.
- Verify literary citations (Dunbar / Du Bois / Ellison / Fanon)
  against bibliography.md §13 + primary-source dates of publication.
- If any cited file does not exist where claimed, stop and ask before
  guessing.
```

---

*End of Ch 8 Pass 1 paste-text. Expect a heavy token budget — Ch 8 is the manuscript's numerical climax, with 8 cost-component claims to verify + multiple cross-chapter consistency checks + 4 literary citations + 2 prior-commit fix-verifications.*
