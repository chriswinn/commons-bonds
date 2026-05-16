# Manuscript Stage-3 Phase A — Ch 7 Pass 1 (Fact-Check) paste-text

**Date drafted:** 2026-05-15
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20) — Phase A — Ch 7 — Pass 1 (fact-check)
**Phase scope:** Pass 1 ONLY. v2.0 Amendment B distinct-pass discipline + per-prompt serial cadence (Pass 1 → spot-fix → Pass 2 → spot-fix → Pass 3 → spot-fix; not bundled).
**Recommended branch at session start:** `claude/manuscript-stage-3-ch7-pass1-<harness-id>` from current `origin/main` (head verified at `7b4aa92` 2026-05-15) after `git fetch`.

---

## Why Ch 7 Pass 1 now

Ch 7 (On Other Worlds — Mars thought-experiment + asteroid/lunar/comet/Europa/exoplanet scenarios + commute-lease coda) is one of four chapters (Chs 7–10) without Pass 1 yet. Critical-path bottleneck on the Phase A serial cadence per predecessor §3.

**Specific landmines for Ch 7:**
- **Mars mission chronology.** Ch 7:17 enumerates "Viking I and II, Mars 3, Pathfinder, Spirit and Opportunity, Phoenix, Curiosity, InSight, Perseverance, with sample return and crewed proposals on the active near-term agenda." Each mission requires verified launch / arrival year + national agency + operational status.
- **Aeon "Mask of Abundance" verbatim/near-verbatim overlap.** Ch 7 is the source material for the Aeon pitch Version C (firing Sun May 31 14:01 UTC). Pass 1 should flag any passage that risks "thunder-stealing" — i.e., a key Aeon-pitch sentence or scene that appears verbatim or near-verbatim in Ch 7, which would weaken the Aeon submission's freshness. Per cross-thread #9.
- **Abundance Masking definitional surfacing.** Defense paragraph applied at commit `2a7c336`. Verify the in-chapter introduction of the Abundance Masking term aligns with the canonical defense paragraph + the apparatus register decision.
- **Six cost-hiding patterns / Ostrom-path light-de-formalize.** Item 15 (commit `b1c17d8`). Verify framing matches current apparatus register; no formal Ostrom-path apparatus residue.
- **Off-world scientific claims.** Helium-3 lunar regolith abundance; rare-earth scarcity references; asteroid iron composition; Europa subsurface ocean status; closed-habitat life-support physics. Each scientific claim needs canonical-source verification.

---

## Filled paste-text — fire in a fresh session

```
You are running Phase A Pass 1 (fact-check) of the Manuscript Stage-3
Rigor Pass workstream (PM dashboard #20) for Chapter 7 — On Other
Worlds. Your job: apply v2.0 Amendment B fact-check discipline (one
distinct pass; not bundled with voice-polish or audience-load) to the
chapter file at manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md.
STOP at verdict + spot-fix recommendations; do NOT apply spot-fixes to
the chapter file. A separate Phase C session applies ratified spot-fixes
after author ratification.

== v2.0 Amendment B discipline — Pass 1 only ==

Three DISTINCT passes (fact-check + voice-polish + audience-load), not
bundled. This session runs fact-check ONLY. Pass 2 (voice-polish) and
Pass 3 (audience-load) are separate subsequent sessions per the per-
prompt serial cadence. Pass-1-surfaced voice or audience concerns get
flagged forward in §6 / §7 sections of the output artifact.

== Mode: audit-existing-prose ==

Per tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Audit-
existing-prose mode": no Stage 1 brief exists for Ch 7. The chapter
file IS the prose under audit; fact-checks verify against external
canonical sources (mission records, scientific literature, apparatus
register decisions, cross-chapter consistency inventory). Severity-tier
classification per Pass 1 standard (CRITICAL / HIGH / MEDIUM / LOW).

== Read in order before doing any work ==

1. THIS paste (the framing).
2. manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md — the chapter
   under audit. Read in full. (~248 lines / ~8,537w per workstream
   handoff; verify line count at session start.)
3. tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Pass 1:
   Fact-check" — full severity scale + finding format.
4. tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
   — per-chapter table; Ch 7 row at line 69.
5. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md
   — Ch 4 Pass 1 artifact as canonical format model (5 MEDIUM + 3 LOW
   findings; severity-rationale paragraphs; verified-items table at end).
   Mirror this structure.
6. publishing/op-eds/aeon-mask-of-abundance-version-c-*.md (search for
   the current Version C draft) — for thunder-stealing check. Flag any
   Ch 7 passage that overlaps verbatim or near-verbatim with the Aeon
   pitch Version C, since the pitch fires Sun May 31 14:01 UTC and
   needs to preserve novelty.
7. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md
   — apparatus register canonical decisions (Abundance Masking framing;
   Ostrom-path light-de-formalize per Item 15).
8. tools/audits/cross-chapter-consistency-inventory_2026-05-11.md —
   canonical-terms + named-cases + recurring-stats.
9. research/literature/bibliography.md §13 — comp + framework-adjacent
   entries with engagement-state flags (Ostrom in particular).
10. core/terms/terms_index.md — canonical-form check for apparatus
    terms appearing in Ch 7 body prose (Abundance Masking; cost
    severance; foreclosure component; externality tail; RCV).
11. Memory entries:
    - feedback_named_subject_consent.md (named-subject discipline)
    - feedback_verify_stale_memory_claims.md (verification discipline)
    - feedback_substance_drives_length.md
    - feedback_audience_aware_drafting_discipline.md

== Per-chapter context ==

**Chapter:** 7 — On Other Worlds
**File path:** manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md
**Word count target:** ~8,537w (~248 lines)
**Key named cases:** Mars habitat thought-experiment; asteroid iron;
lunar helium-3; comet volatiles; Europa ice; exoplanet ecosystems;
commute-lease earthside coda.
**Mission chronology (Ch 7:17 — verify each):** Viking I and II
(1975 launch / 1976 arrival, NASA); Mars 3 (1971 launch, Soviet);
Pathfinder (1996 launch / 1997 arrival, NASA); Spirit and Opportunity
(2003 launches / 2004 arrivals, NASA); Phoenix (2007 launch / 2008
arrival, NASA); Curiosity (2011 launch / 2012 arrival, NASA); InSight
(2018 launch / 2018 arrival, NASA); Perseverance (2020 launch / 2021
arrival, NASA).

**Specific audit emphases (per workstream handoff line 69 + cross-
thread context):**

- **Mars mission chronology.** Verify each mission name, launch year,
  arrival year (where distinct), and national agency. Spirit and
  Opportunity were paired but distinct missions; Viking I and II were
  paired but distinct missions. Order matters chronologically.
- **Aeon "Mask of Abundance" thunder-stealing check.** Compare key
  Ch 7 passages against the Aeon pitch Version C. Flag any verbatim
  or near-verbatim sentence/scene/anchor. Aeon fires Sun May 31 14:01
  UTC; thunder-stealing risk peaks if a flagship Aeon scene already
  appears verbatim in Ch 7 prose that publisher / agent / venue
  readers will have access to. Severity HIGH if verbatim match; MEDIUM
  if near-verbatim scene-anchor; LOW if conceptual overlap only.
- **Abundance Masking definitional surfacing.** Verify the in-chapter
  introduction of Abundance Masking aligns with the canonical defense
  paragraph at commit `2a7c336` + the apparatus register decision
  (capitalized-flagship-term register; introduction-site discipline).
- **Six cost-hiding patterns / Ostrom-path framing.** Per Item 15
  (`b1c17d8`), Ostrom-path light-de-formalized. Verify Ch 7 prose
  doesn't carry formal Ostrom-path apparatus (Greek letters,
  subscripts, integrals); the framing should be plain-language.
- **Off-world scientific claims.** Each requires canonical-source
  verification:
  - Helium-3 abundance on lunar regolith (canonical: NASA / ISRO
    lunar geology studies; abundance estimates vary 1-50 ppb)
  - Asteroid iron composition (canonical: meteorite analyses; M-type
    asteroid Fe abundance ~80-90%)
  - Comet volatile composition (canonical: Rosetta / Stardust
    mission data on 67P, Wild 2)
  - Europa subsurface ocean status (canonical: Galileo / Europa
    Clipper preliminary findings; ocean inferred but not confirmed)
  - Mars subsurface water ice (canonical: Mars Reconnaissance
    Orbiter / SHARAD / Phoenix / Curiosity / Perseverance findings;
    extensive subsurface ice confirmed)
  - Closed-habitat life-support physics (canonical: ISS / Biosphere 2 /
    MELiSSA project studies on water recycling, oxygen generation,
    food production cycles)
- **Devon Island / HI-SEAS analog references.** If Ch 7 names these,
  verify operational status + research-program attribution (Devon
  Island = Haughton-Mars Project, Mars Institute; HI-SEAS = Hawaii
  Space Exploration Analog and Simulation, University of Hawaii).
- **Off-world resource pricing claims.** Verify any "fifty-year supply"
  / "twenty-year horizon" / "ten thousand people" arithmetic that the
  chapter's Mars-habitat scenario depends on for internal consistency.
  These are thought-experiment parameters not external facts, but the
  internal arithmetic must hold.

== Pass 1: Fact-check ==

For every factual claim in the chapter, verify against canonical
sources. Flag findings by severity:

- **CRITICAL** — claim is factually wrong; publisher pre-publication
  review would flag.
- **HIGH** — claim is misleading or imprecise; could be challenged by
  a knowledgeable reader (planetary scientist, space mission historian,
  habitability researcher).
- **MEDIUM** — claim is technically defensible but loose; acceptable in
  trade prose but worth tightening.
- **LOW** — claim is accurate but framing could be sharpened.

For each finding: cite chapter line number + chapter text + canonical
truth + recommended spot-fix (Option A / B / C where appropriate).

Pay special attention to Mars mission chronology (Ch 7:17 — high prior
probability of small drift in a long enumeration), Aeon-pitch verbatim
overlap, and the Abundance-Masking introduction site.

== Web verification — default mode ==

For numerical claims, dates, mission chronologies, scientific facts,
geographic specifics, scholarly citations: DEFAULT to WebSearch /
WebFetch against authoritative sources BEFORE flagging "verify against
canonical X" for later work. Authoritative sources for Ch 7 include:

- NASA / NSSDC (National Space Science Data Center) for Mars mission
  launch dates, arrival dates, agency attribution, operational status
- ESA / Roscosmos / ISRO for non-NASA mission attribution
- USGS Astrogeology / Planetary Data System for Mars geological
  surface claims
- Peer-reviewed planetary-science literature (Icarus; JGR Planets;
  Nature Astronomy) for asteroid composition, lunar regolith helium-3
  abundance, comet volatile composition, Europa subsurface ocean
- ITER / DOE Fusion Energy Sciences for fusion pathway claims
- Mars Institute / Haughton-Mars Project for Devon Island
- University of Hawaii HI-SEAS for Hawaii analog
- Wikipedia ONLY as a starting-point pointer to primary sources
  (verify the underlying citation; do not cite Wikipedia itself)

Fact-check pass DOES the verification, not "flag for later." If
WebSearch returns conflicting authoritative sources, document the
disagreement (which sources say what) and flag MEDIUM or HIGH per
severity scale.

Flag-for-later is reserved for:
- Internal-corpus-only claims (cross-chapter consistency; manuscript-
  internal references) where the verification target is another file
  in this repo
- Claims requiring manual judgment beyond WebSearch (subjective
  historical interpretation; contested scholarly debates)
- Claims where the relevant authoritative source isn't publicly
  indexed

== Apparatus / consistency / named-subject sub-checks (§5 in output) ==

Mirror Ch 4 Pass 1 §"Apparatus regression check" + §"Path B
contamination check" + §"Named-subject consent check" structure:

- **Apparatus residue.** Verify Ch 7 doesn't carry formal apparatus
  (Greek letters, subscripts, integrals) where the apparatus register
  prohibits. Verify Abundance Masking introduction is canonical.
- **Path B contamination.** Verify no verbatim-clone passages from
  other chapters (Ch 6 RCV apparatus passages especially).
- **Named-subject consent.** Ch 7's main named characters are
  thought-experiment composites (the Mars administrator, the trading
  consortium representative, the commute-lease tenant). Verify no
  living named subjects appear without consent.

== Out-of-scope flagging (§6 + §7 in output) ==

- **§6 Pass-2 (voice-polish) future-session input.** Items that cross
  attention during Pass-1 reading but belong to voice-polish scope
  (LLM tics; em-dash density; cadence patterns).
- **§7 Pass-3 (audience-load) future-session input.** Tier-1 quant /
  planetary-science reader pressure-test concerns; Tier-1 policy
  reader Mars-canonization concerns; Tier-2 SF-literate reader
  thought-experiment register; Tier-3 environmental-philosophy reader
  off-world-extraction-ethics concerns.

== Verdict synthesis (§8 in output) ==

- **§8.1 Findings tally.** Table: severity × count × finding-IDs.
- **§8.2 Aggregate Pass-1 verdict.**
  - READY AS-IS — 0 CRITICAL; 0 HIGH.
  - READY AFTER SPOT-FIXES — CRITICAL/HIGH findings spot-fixable.
  - STRUCTURAL REVISION NEEDED — fact-checks reveal structural error
    that can't be addressed by spot-fixes.
- **§8.3 Phase-C disposition recommendation.** Sequenced list:
  CRITICAL/HIGH first; MEDIUM clustered; LOW deferred.

== Output ==

Single atomic commit on feature branch:
- tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_ch7_on_other_worlds_stage3_fact_check_v1.0.0.md

== Hard constraints ==

- Do NOT apply spot-fixes to the chapter file.
- Do NOT re-write paragraphs.
- Do NOT score Pass 2 or Pass 3 — flag-forward at §6 / §7.
- Do NOT contact named subjects.
- DO flag any Aeon-pitch verbatim overlap as a HIGH-severity finding
  given the Sun May 31 14:01 UTC fire window.
- DO flag any apparatus regressions, named-subject consent issues, or
  Path B contamination.

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-ch7-pass1-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. Report rigor-pass back to PM session
+ author. Author ratifies which spot-fixes to apply via separate Phase C
session.

== Verify-stale-memory-claims discipline ==

Before asserting any time-sensitive claim:
- Verify chapter file path exists at session start; verify line count.
- Verify cited apparatus-register commits exist on origin/main.
- Verify Mars mission dates against NASA / NSSDC / ESA canonical records.
- Verify Aeon pitch Version C draft exists at the cited path.
- If any cited file does not exist where claimed, stop and ask before
  guessing.
```

---

*End of Ch 7 Pass 1 paste-text. Expect ~similar token budget to Ch 4 Pass 1 (Mars mission chronology + Aeon verbatim check + multiple off-world scientific claims = heavy fact-check load).*
