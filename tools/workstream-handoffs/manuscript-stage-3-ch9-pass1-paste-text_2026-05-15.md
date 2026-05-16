# Manuscript Stage-3 Phase A — Ch 9 Pass 1 (Fact-Check) paste-text

**Date drafted:** 2026-05-15
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20) — Phase A — Ch 9 — Pass 1 (fact-check)
**Phase scope:** Pass 1 ONLY. v2.0 Amendment B distinct-pass discipline + per-prompt serial cadence (Pass 1 → spot-fix → Pass 2 → spot-fix → Pass 3 → spot-fix; not bundled).
**Recommended branch at session start:** `claude/manuscript-stage-3-ch9-pass1-<harness-id>` from current `origin/main` (head verified at `7b4aa92` 2026-05-15) after `git fetch`.

---

## Why Ch 9 Pass 1 now

Ch 9 (Pricing Honestly — four-step framework Classify → Reserve → Invest → Reassess) is the policy-recommendation chapter. Pass 1 fact-checks the framework's claims against specific resource cases (rare earths, platinum group metals, helium-3, phosphorus, fossil aquifers) and verifies the Susskind / Christophers / Pistor engagement.

**Specific landmines for Ch 9:**
- **$500-$600 / ton coal figure (Ch 9:9).** Must reconcile with Ch 8's cost-component arithmetic. Cross-chapter consistency.
- **Rare earth element claims (Ch 9:27).** "Seventeen metals whose magnetic and optical properties underwrite nearly every piece of advanced electronics." Verify the 17-count + applications + geological concentration.
- **Helium-3 fusion / lunar regolith claim (Ch 9:27).** Cross-reference with Ch 7's lunar helium-3 framing.
- **Phosphorus claim (Ch 9:27).** "Essential for agriculture, exists in workable concentrations at only a few places on the planet and has no substitute." Verify against current phosphate-reserve literature.
- **Fossil aquifer claims (Ch 9:27).** "Ogallala, the North China Plain, the Guarani." Verify each as fossil-aquifer + regeneration timescales (millennia) + withdrawal timescales (decades).
- **Susskind (Growth: A Reckoning).** Citation accuracy; engagement applied 2026-05-08 (commit `d78872e`).
- **Christophers (Price is Wrong).** Citation accuracy; engagement applied 2026-05-08.
- **Pistor cross-reference.** Verify Pistor (Code of Capital) citation aligns with Ch 5's canonical reference.
- **Four-step framework name-stability.** Classify → Reserve → Invest → Reassess. Verify naming consistency throughout the chapter + alignment with terms_index.md if these are flagship terms.
- **Cross-chapter consistency batches.** Landed 2026-05-11. Verify no regression.

---

## Filled paste-text — fire in a fresh session

```
You are running Phase A Pass 1 (fact-check) of the Manuscript Stage-3
Rigor Pass workstream (PM dashboard #20) for Chapter 9 — Pricing
Honestly. Your job: apply v2.0 Amendment B fact-check discipline (one
distinct pass; not bundled with voice-polish or audience-load) to the
chapter file at
manuscript/chapters/Chapter__9_PricingHonestly__Draft.md. STOP at
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
existing-prose mode": no Stage 1 brief exists for Ch 9. The chapter
file IS the prose under audit; fact-checks verify against external
canonical sources (USGS reserve data, scientific literature on
specific resources, cross-chapter consistency inventory, primary
sources for Susskind / Christophers / Pistor).

== Read in order before doing any work ==

1. THIS paste (the framing).
2. manuscript/chapters/Chapter__9_PricingHonestly__Draft.md — the
   chapter under audit. Read in full. (~273 lines / ~10,178w per
   workstream handoff; verify line count at session start.)
3. tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Pass 1:
   Fact-check" — full severity scale + finding format.
4. tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
   — per-chapter table; Ch 9 row at line 71.
5. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md
   — Ch 4 Pass 1 artifact as canonical format model. Mirror this
   structure.
6. manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md —
   for cross-chapter consistency on $500-$600/ton figure (Ch 9:9
   must reconcile with Ch 8's cost-component arithmetic).
7. manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md —
   for Pistor (Code of Capital) canonical citation pattern.
8. research/literature/bibliography.md §13 — Susskind (Growth: A
   Reckoning), Christophers (Price is Wrong), Pistor (Code of
   Capital) canonical entries.
9. tools/audits/cross-chapter-consistency-inventory_2026-05-11.md —
   canonical-terms + named-cases + recurring-stats.
10. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md
    — apparatus register canonical decisions (Classify/Reserve/Invest/
    Reassess framework naming; cost severance; foreclosure component).
11. core/terms/terms_index.md — canonical-form check for apparatus
    terms in Ch 9 body prose (existential substitutability gap;
    foreclosure component; restitution bond; foreclosure bond; four-
    step framework).
12. Recent commits relevant to Ch 9:
    - `d78872e` (2026-05-08) — Christophers + Susskind engagement
    - 2026-05-11 cross-chapter consistency batches
13. USGS / scientific canonical sources for resource claims:
    - USGS Mineral Commodity Summaries (current year) for rare earths,
      platinum group metals, phosphate rock
    - USGS / NASA lunar regolith helium-3 abundance estimates
    - USGS / state-level reports on Ogallala Aquifer
    - World Bank / FAO reports on North China Plain aquifer
    - SAG (Sistema Acuífero Guaraní) hydrogeological studies
14. Memory entries:
    - feedback_named_subject_consent.md
    - feedback_verify_stale_memory_claims.md
    - feedback_substance_drives_length.md
    - feedback_audience_aware_drafting_discipline.md

== Per-chapter context ==

**Chapter:** 9 — Pricing Honestly
**File path:** manuscript/chapters/Chapter__9_PricingHonestly__Draft.md
**Word count target:** ~10,178w (~273 lines)
**Key named subjects (verify register + consent):** Susskind (Growth:
A Reckoning); Christophers (Price is Wrong); Pistor (Code of
Capital). All are scholars cited for argument-engagement; no consent
issue (academic citation register).
**Key named cases:** Rare earth elements (17 metals); platinum group
metals; helium-3 (lunar regolith / fusion); phosphorus; fossil
aquifers (Ogallala, North China Plain, Guarani); coal (low-existential-
substitutability-gap); iron (low-gap); the four-step Classify /
Reserve / Invest / Reassess framework.

**Specific audit emphases (per workstream handoff line 71 + cross-
thread context):**

- **$500-$600 / ton coal figure (Ch 9:9).** Must reconcile with
  Ch 8's cost-component arithmetic floor. Cross-check: does Ch 9's
  $500-$600 range match Ch 8's sum-of-Cᵢ? If Ch 8 lands a different
  floor figure (e.g., $400-$500 or $600-$700), flag as CROSS-CHAPTER
  CONSISTENCY issue (HIGH severity — these chapters are sequentially
  related and the figure must be identical).
- **Rare earth element claims (Ch 9:27).** Verify:
  - The 17-element count (yttrium + 15 lanthanides + scandium = 17;
    or 15 lanthanides only depending on convention)
  - "Magnetic and optical properties" — verify both apply to all 17
    or whether prose should be tightened (some lanthanides are
    primarily optical, some primarily magnetic)
  - "Nearly every piece of advanced electronics" — verify against
    industry usage data
  - Geological concentration — verify against USGS Mineral Commodity
    Summaries (China dominance, US deposits, other producers)
- **Helium-3 fusion / lunar regolith claim (Ch 9:27).** Cross-
  reference with Ch 7's lunar helium-3 framing. Verify:
  - Earth atmospheric abundance is essentially zero (confirmed
    technical claim)
  - Lunar regolith abundance estimates (5-20 ppb typical; varies by
    latitude; ITER / future-fusion contexts)
  - Fusion-reactor helium-3 dependence (D-He3 fusion is one of
    several proposed fusion pathways; D-T fusion does not require
    helium-3; verify Ch 9's framing is technically precise)
- **Phosphorus claim (Ch 9:27).** "Essential for agriculture, exists
  in workable concentrations at only a few places on the planet
  and has no substitute for the biological role it plays." Verify:
  - Morocco / Western Sahara dominance of phosphate rock reserves
    (~70% of global reserves per USGS)
  - "No substitute" claim — phosphorus has no chemical substitute
    in DNA/RNA/ATP; agricultural cycling (manure, bone meal) is
    recycling not substitution. Verify the framing is precise.
- **Fossil aquifer claims (Ch 9:27).** Three named aquifers:
  - Ogallala (High Plains Aquifer, US): verify "millennia"
    regeneration claim (most recharge dates from Pleistocene; modern
    recharge is negligible in much of southern Ogallala)
  - North China Plain: verify fossil-aquifer status (Hutuo /
    Quaternary aquifers; mixed fossil + slow-recharge)
  - Guarani (South America: Brazil / Argentina / Paraguay /
    Uruguay): verify fossil-aquifer status (largely fossil; some
    recharge zones)
  - "Withdrawn on timescales of decades" — verify against current
    overdraft rates (Ogallala saturated-thickness declines; NCP
    measurable subsidence)
- **Susskind (Growth: A Reckoning) — citation accuracy.** Verify:
  - Title (Growth: A Reckoning) and author (Daniel Susskind)
  - Publication year (2024)
  - Argument attribution — verify Ch 9's framing matches Susskind's
    actual argument (decoupling growth from environmental damage;
    growth-skeptic vs. growth-defender stance)
  - Engagement-state per bibliography.md §13 entry
- **Christophers (Price is Wrong) — citation accuracy.** Verify:
  - Title (The Price is Wrong: Why Capitalism Won't Save the Planet)
    and author (Brett Christophers)
  - Publication year (2024)
  - Argument attribution — verify Ch 9's framing matches
    Christophers's actual argument
- **Pistor cross-reference.** Verify Ch 9's Pistor reference aligns
  with Ch 5's canonical Pistor (Code of Capital) citation. Same
  edition / year / argument-attribution.
- **Four-step framework naming.** Classify → Reserve → Invest →
  Reassess. Verify:
  - Naming consistency throughout the chapter (no drift to
    Categorize / Allocate / Deploy / Review or similar)
  - Alignment with terms_index.md (if these are flagship terms,
    verify capitalization + register match)
  - Cross-chapter consistency (if Ch 10 references the framework,
    verify naming matches)
- **High-vs-low existential substitutability gap.** Per Ch 9:23 +
  Ch 9:27 — verify this is a canonical apparatus term (per
  apparatus register decision) and that its introduction-site is
  consistent with the apparatus register.
- **Cross-chapter consistency batches landed 2026-05-11.** Verify
  no regression in Ch 9 against the post-batch baseline.

== Pass 1: Fact-check ==

For every factual claim in the chapter, verify against canonical
sources. Flag findings by severity:

- **CRITICAL** — claim is factually wrong; publisher pre-publication
  review would flag.
- **HIGH** — claim is misleading or imprecise; could be challenged by
  a knowledgeable reader (resource economist, geologist,
  policy-mineral analyst, Susskind-Christophers-Pistor literate
  reader).
- **MEDIUM** — claim is technically defensible but loose.
- **LOW** — claim is accurate but framing could be sharpened.

For each finding: cite chapter line number + chapter text + canonical
truth + recommended spot-fix (Option A / B / C where appropriate).

Pay special attention to the $500-$600 cross-chapter reconciliation,
the resource-specific claims (rare earths, helium-3, phosphorus,
fossil aquifers), the four scholarly citations (Susskind, Christophers,
Pistor cross-reference), and the four-step framework naming.

== Web verification — default mode ==

For numerical claims, dates, scientific facts, geographic specifics,
scholarly citations: DEFAULT to WebSearch / WebFetch against
authoritative sources BEFORE flagging "verify against canonical X"
for later work. Authoritative sources for Ch 9 include:

- USGS Mineral Commodity Summaries (current year) for rare earths,
  platinum group metals, phosphate rock, helium reserves +
  geographic concentration data
- USGS Water Resources / state geological surveys for Ogallala
  Aquifer saturated-thickness + recharge data
- China Geological Survey / FAO AQUASTAT for North China Plain
  aquifer data
- SAG (Sistema Acuífero Guaraní) / IAEA hydrogeological studies
  for Guarani Aquifer
- NASA / DOE Fusion Energy Sciences for helium-3 lunar regolith
  abundance + D-He3 fusion pathway claims
- IFA (International Fertilizer Association) / Phosphate Forum
  for global phosphate-rock reserves + biological-substitution
  claims
- Publisher pages / WorldCat / Google Books for Susskind (Growth:
  A Reckoning, 2024, Allen Lane); Christophers (The Price is Wrong,
  2024, Verso); Pistor (The Code of Capital, 2019, Princeton UP) —
  verify titles, authors, publication years, edition + page-level
  argument-attribution where the chapter cites specific arguments
- Google Scholar for citation lookup + author-attribution
- Wikipedia ONLY as a starting-point pointer to primary sources
  (verify the underlying citation; do not cite Wikipedia itself)

Fact-check pass DOES the verification, not "flag for later." If
WebSearch returns conflicting authoritative sources (especially
common with reserve-estimate ranges where USGS / industry / academic
sources diverge), document the disagreement (which sources say what)
and flag MEDIUM or HIGH per severity scale; recommend the chapter
reflect the range or cite the most-conservative source.

Flag-for-later is reserved for:
- Internal-corpus-only claims (cross-chapter consistency; $500-$600
  reconciliation with Ch 8; Pistor citation pattern reconciliation
  with Ch 5) where the verification target is another file in this
  repo
- Claims requiring manual judgment beyond WebSearch (contested
  resource-substitutability claims; debated reserve-classification
  methodologies)
- Claims where the relevant authoritative source isn't publicly
  indexed

== Apparatus / consistency / named-subject sub-checks (§5 in output) ==

- **Apparatus residue.** Verify no formal apparatus regression
  (Greek letters, integrals) in body prose; verify Classify /
  Reserve / Invest / Reassess naming + capitalization matches
  apparatus register.
- **Path B contamination.** Verify no verbatim-clone passages from
  Ch 5 (Pistor) / Ch 6 (apparatus) / Ch 8 (coal arithmetic).
- **Named-subject consent.** All cited scholars are public-record
  academic citations; no consent issue.
- **Cross-chapter consistency.** $500-$600 figure (Ch 8 reconcile);
  Pistor citation pattern (Ch 5 reconcile); apparatus-term
  introduction sites.

== Out-of-scope flagging (§6 + §7 in output) ==

- **§6 Pass-2 (voice-polish) future-session input.** Items belonging
  to voice-polish scope. Ch 9 voice emphases will likely include
  policy-recommendation register consistency; multi-resource-
  enumeration cadence; scholarly-citation prose-density.
- **§7 Pass-3 (audience-load) future-session input.** Tier-1 policy
  reader; Tier-1 environmental-economics reader; Tier-1 trade-press
  reader (does the four-step framework land as actionable or as
  abstract?); Tier-2 Susskind / Christophers / Pistor-literate
  reader (does the engagement read as scholarly or as cursory?);
  Tier-3 Global-South reader (does the Morocco / Western Sahara
  phosphate framing handle the geopolitical context?).

== Verdict synthesis (§8 in output) ==

- **§8.1 Findings tally.** Table.
- **§8.2 Aggregate Pass-1 verdict.** READY AS-IS / READY AFTER SPOT-
  FIXES / STRUCTURAL REVISION NEEDED.
- **§8.3 Phase-C disposition recommendation.** Sequenced list.

== Output ==

Single atomic commit on feature branch:
- tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_ch9_pricing_honestly_stage3_fact_check_v1.0.0.md

== Hard constraints ==

- Do NOT apply spot-fixes to the chapter file.
- Do NOT re-write paragraphs.
- Do NOT score Pass 2 or Pass 3 — flag-forward at §6 / §7.
- Do NOT contact named subjects.
- DO flag any cross-chapter consistency issue (especially $500-$600
  reconcile with Ch 8) as a HIGH-severity finding.
- DO flag any apparatus regressions, named-subject consent issues, or
  Path B contamination.

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-ch9-pass1-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. Report rigor-pass back to PM session
+ author. Author ratifies which spot-fixes to apply via separate Phase C
session.

== Verify-stale-memory-claims discipline ==

Before asserting any time-sensitive claim:
- Verify chapter file path exists at session start; verify line count.
- Verify commit `d78872e` exists on origin/main (Christophers +
  Susskind engagement).
- Verify scholarly citation details (titles, years, authors) against
  bibliography.md §13.
- Verify USGS / scientific reserve estimates are current (current
  USGS Mineral Commodity Summaries year).
- Verify Ch 8 / Ch 5 / Ch 10 cross-references against current state
  of those files on origin/main.
- If any cited file does not exist where claimed, stop and ask before
  guessing.
```

---

*End of Ch 9 Pass 1 paste-text. Expect heavy token budget — Ch 9 has the densest scientific-claim verification load (rare earths, helium-3, phosphorus, three fossil aquifers) + three primary-source scholarly citations + cross-chapter $500-$600 reconciliation.*
