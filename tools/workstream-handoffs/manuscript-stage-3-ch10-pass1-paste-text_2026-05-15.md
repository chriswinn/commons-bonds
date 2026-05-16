# Manuscript Stage-3 Phase A — Ch 10 Pass 1 (Fact-Check) paste-text

**Date drafted:** 2026-05-15
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20) — Phase A — Ch 10 — Pass 1 (fact-check)
**Phase scope:** Pass 1 ONLY. v2.0 Amendment B distinct-pass discipline + per-prompt serial cadence (Pass 1 → spot-fix → Pass 2 → spot-fix → Pass 3 → spot-fix; not bundled).
**Recommended branch at session start:** `claude/manuscript-stage-3-ch10-pass1-<harness-id>` from current `origin/main` (head verified at `7b4aa92` 2026-05-15) after `git fetch`.

---

## Why Ch 10 Pass 1 now

Ch 10 (Common Bonds — sunrise/sunset bookend with Ch 1; harbor scene at Old Point Comfort; cross-cuts to McDowell miner / Baotou processing worker / Niger Delta fisherman / Texas Panhandle aquifer farmer / off-world administrator) is the framework-synthesis chapter. Pass 1 has a smaller fact-checkable surface than Ch 8 or Ch 9 (the chapter is more literary-meditative) but the cross-references it makes back to Chs 1, 7, and 8 all need consistency verification.

**File path note:** Ch 10 uses single-underscore-prefix `Chapter_10_CommonBonds__Draft.md` (NOT `Chapter__10_` like the other chapters — the workstream handoff line 72 lists the wrong filename; the actual file is `manuscript/chapters/Chapter_10_CommonBonds__Draft.md`).

**Specific landmines for Ch 10:**
- **Old Point Comfort / Hampton, VA geography.** Ch 10:9 + Ch 10:15. Verify geographic accuracy (Old Point Comfort is in Hampton, VA at the mouth of the James/Hampton Roads; the author's harbor placement should match).
- **Author's personal-life claims (Ch 10:15).** "My wife had died once on a hospital bed" — verify against AuthorsNote / dedication / prior chapter framings; consent + memoir-accuracy. Also: "be close to my parents," "twenty years helping institutions move value across ledgers."
- **Cross-cut figures (Ch 10:21, 23, 25, 27).** Each is composite/anonymous but each touches real geographies + industries:
  - McDowell County, WV coal miner (Ch 10:21) — verify consistency with Ch 2 + Ch 8 McDowell content
  - Hampton, VA waterman (Ch 10:9, 11, 13) — verify consistency with Ch 3 Fox Hill / Chesapeake content
  - Baotou rare-earth processing line (Ch 10:25) — verify Baotou as the canonical Chinese rare-earth processing center; consistency with Ch 9 rare-earth claims
  - Niger Delta fisherman (Ch 10:25) — verify consistency with Ch 4's Nigeria/Niger Delta content (Ch 4 Pass 1 verified Ogoniland + Saro-Wiwa; verify no regression)
  - Texas Panhandle aquifer farmer (Ch 10:25) — verify consistency with Ch 9 Ogallala aquifer claims
- **Mars administrator scene cross-reference (Ch 10:29).** Must align with Ch 7's Mars thought-experiment. Cross-chapter consistency.
- **Ch 1 sunrise / Ch 10 sunset bookend.** Verify bookend coherence — Ch 1 opens at dawn flying out of Savannah; Ch 10 closes the day-symbolic arc.
- **Framework-synthesis claims.** "Nine chapters trying to name what happens" (Ch 10:13). Verify the synthesis claims match the actual chapter content (no overpromising or misattribution).

---

## Filled paste-text — fire in a fresh session

```
You are running Phase A Pass 1 (fact-check) of the Manuscript Stage-3
Rigor Pass workstream (PM dashboard #20) for Chapter 10 — Common Bonds.
Your job: apply v2.0 Amendment B fact-check discipline (one distinct
pass; not bundled with voice-polish or audience-load) to the chapter
file at manuscript/chapters/Chapter_10_CommonBonds__Draft.md (note the
single-underscore prefix on this chapter's filename). STOP at verdict +
spot-fix recommendations; do NOT apply spot-fixes to the chapter file.
A separate Phase C session applies ratified spot-fixes after author
ratification.

== v2.0 Amendment B discipline — Pass 1 only ==

Three DISTINCT passes (fact-check + voice-polish + audience-load), not
bundled. This session runs fact-check ONLY. Pass 2 (voice-polish) and
Pass 3 (audience-load) are separate subsequent sessions per the per-
prompt serial cadence. Pass-1-surfaced voice or audience concerns get
flagged forward in §6 / §7 sections of the output artifact.

== Mode: audit-existing-prose ==

Per tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Audit-
existing-prose mode": no Stage 1 brief exists for Ch 10. The chapter
file IS the prose under audit. Ch 10's fact-check surface is smaller
than mid-book chapters (Ch 10 is literary-meditative synthesis) but
cross-reference accuracy to Chs 1, 2, 3, 4, 7, 8, 9 is high-leverage —
the synthesis chapter cannot misrepresent what the earlier chapters
established.

== Read in order before doing any work ==

1. THIS paste (the framing).
2. manuscript/chapters/Chapter_10_CommonBonds__Draft.md — the chapter
   under audit. Read in full. (~151 lines / ~7,366w per workstream
   handoff; verify line count at session start.)
3. tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Pass 1:
   Fact-check" — full severity scale + finding format.
4. tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
   — per-chapter table; Ch 10 row at line 72.
5. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md
   — Ch 4 Pass 1 artifact as canonical format model.
6. manuscript/chapters/Chapter__1_TheQuietMath__Draft.md — for
   sunrise/sunset bookend coherence with Ch 1's opening.
7. manuscript/chapters/Chapter__2_TheMiner__Draft.md — for McDowell
   miner cross-cut consistency (Ch 10:21).
8. manuscript/chapters/Chapter__3_TheWaterman__Draft.md — for Fox Hill
   / Chesapeake waterman cross-cut consistency (Ch 10:9, 11, 13).
9. manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md — for
   Niger Delta cross-cut consistency (Ch 10:25); verify Ch 4's post-
   Pass-1 prose state (Ogoniland + Saro-Wiwa references).
10. manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md — for
    Mars administrator scene cross-reference (Ch 10:29).
11. manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md —
    for cost-severance synthesis claims.
12. manuscript/chapters/Chapter__9_PricingHonestly__Draft.md — for
    Texas Panhandle aquifer (Ogallala) consistency (Ch 10:25) +
    Baotou rare-earth consistency (Ch 10:25).
13. manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md — for
    author personal-history register (especially the wife's near-
    death / hospital reference in Ch 10:15; cross-check with any
    AuthorsNote framing).
14. tools/audits/cross-chapter-consistency-inventory_2026-05-11.md —
    canonical-terms + named-cases + recurring-stats.
15. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md
    — apparatus register canonical decisions.
16. core/terms/terms_index.md — canonical-form check for apparatus
    terms in Ch 10 body prose.
17. Memory entries:
    - feedback_named_subject_consent.md (named-subject discipline —
      Ch 10:15 references the author's wife; verify register)
    - feedback_verify_stale_memory_claims.md
    - feedback_substance_drives_length.md
    - feedback_audience_aware_drafting_discipline.md

== Per-chapter context ==

**Chapter:** 10 — Common Bonds
**File path:** manuscript/chapters/Chapter_10_CommonBonds__Draft.md
  (note: SINGLE-underscore prefix; differs from Chs 1-9 which use
  double-underscore prefix)
**Word count target:** ~7,366w (~151 lines)
**Key named subjects:** Author's wife (Ch 10:15, anonymized as
"my wife"); author's parents (Ch 10:15, anonymized as "my parents").
Verify register holds — first-person memoir frame; no living named
subjects beyond the author himself.
**Key named cases / geographies:** Old Point Comfort (Hampton, VA);
McDowell County, WV; Baotou (China — rare-earth processing); Niger
Delta; Texas Panhandle (Ogallala); Mars habitat (Ch 7 cross-
reference).

**Specific audit emphases (per workstream handoff line 72 + cross-
thread context):**

- **Old Point Comfort / Hampton, VA geography (Ch 10:9, 15).**
  Verify: Old Point Comfort is in the city of Hampton, VA, at the
  mouth of the James River / Hampton Roads. The "harbor" the author
  describes is identifiable; verify any specific landmarks (Fort
  Monroe? specific marina?) for accuracy if named. Cross-reference
  with Ch 3 (waterman chapter set in Chesapeake region).
- **Author personal-life claims (Ch 10:15).** Three claims:
  - "I had spent twenty years helping institutions move value across
    ledgers — hospitals, federal agencies, insurance companies,
    defense contractors" — verify against author bio / AuthorsNote /
    prior chapter framings (Ch 1's NIH + cable-TV-CEO experience).
    Twenty-year span + four-industry list; verify dates + industries
    match elsewhere in the book.
  - "My wife had died once on a hospital bed and I had eventually
    realized that even after she came back the hospital had taken
    something I would not get back either" — verify memoir-accuracy
    against any AuthorsNote / dedication / prior framings. Named-
    subject register check: the wife is anonymized as "my wife"
    (consent-clean per the named-subject discipline since she is
    not named formally). Verify the near-death framing is
    consistent with any prior framings.
  - "I wanted to be close to my parents, who are standing a little
    less straight than they used to" — verify register matches Ch 1's
    references to author's parents (father in particular figures in
    Ch 1).
- **Cross-cut consistency checks:**
  - **McDowell miner (Ch 10:21).** Verify the framing ("a man
    roughly my age... pulling on boots... lungs sound the way his
    father's lungs sounded") matches Ch 2's McDowell content + Ch 8's
    coal-miner framing. Flag any divergence (specific stats; specific
    industry claims; black-lung framing).
  - **Hampton waterman (Ch 10:9, 11, 13, 23).** Verify consistency
    with Ch 3's Fox Hill / Chesapeake content. The chapter's harbor
    scene depicts watermen going out before dawn; Ch 3 establishes
    Biggie (deceased) + Phat (anonymized) + Fox Hill mutual aid 3am
    scene as canonical Chesapeake scenes. Verify Ch 10's framing
    doesn't conflict with Ch 3 (no new named watermen unless
    consent-cleared).
  - **Baotou rare-earth processing (Ch 10:25).** Verify Baotou as
    canonical Chinese rare-earth processing center (Baotou, Inner
    Mongolia; site of Bayan Obo deposit + major REE processing).
    Cross-reference with Ch 9's rare-earth claims for any specific
    Baotou stats.
  - **Niger Delta fisherman (Ch 10:25).** Verify consistency with
    Ch 4's Niger Delta content (Ogoniland; Saro-Wiwa hanged 1995;
    UNEP 2011 cleanup report). Verify Ch 10's framing ("rinsing
    oil off a net") doesn't conflict with Ch 4's framing.
  - **Texas Panhandle aquifer farmer (Ch 10:25).** Verify
    consistency with Ch 9's Ogallala claims. "Pumping what the
    aquifer still has left to pump" — verify framing matches Ch 9's
    aquifer-depletion claims.
- **Mars administrator scene cross-reference (Ch 10:29).** Verify
  Ch 10's framing of the Mars administrator ("the administrator's
  own children would drink nothing, breathe nothing, eat nothing...
  every cubic meter and every gallon enumerated against the finite
  supply") matches Ch 7's Mars thought-experiment scenario. Cross-
  reference Ch 7:25-29 (the habitat scene at the chapter's open).
- **Ch 1 sunrise / Ch 10 sunset bookend.** Ch 1 opens with the
  author on a flight at dawn ("the plane was past the cloud line.
  The sun was up. The day was beginning"). Ch 10 opens at the harbor
  before dawn ("the water is flat, black... the light comes later").
  Verify the bookend coherence: Ch 1 dawn-departure narrative-arc
  with Ch 10 pre-dawn-witness narrative-arc. Severity LOW unless a
  specific bookend cross-reference is misaligned.
- **Framework-synthesis claims (Ch 10:13).** "I have spent nine
  chapters trying to name what happens to men like them. What I
  have called cost severance is a long word for a simple mechanism:
  value leaves the place it comes from, and the costs of its leaving
  stay behind." Verify:
  - "Nine chapters" is accurate (Chs 1-9; Ch 10 is the synthesis).
  - The cost-severance one-sentence summary matches the apparatus
    register decision + the canonical introduction site (typically
    Ch 1 + Ch 8 surfaces; Ch 6 formalizes).
  - The synthesis doesn't overpromise — every claim made about what
    the earlier chapters "named" should be defensibly grounded in
    the actual earlier-chapter content.

== Pass 1: Fact-check ==

For every factual claim in the chapter, verify against canonical
sources. Flag findings by severity:

- **CRITICAL** — claim is factually wrong; publisher pre-publication
  review would flag.
- **HIGH** — claim is misleading or imprecise; could be challenged by
  a knowledgeable reader (Appalachian-or-Chesapeake-or-Niger-Delta-or-
  Baotou-or-Ogallala-literate reader; reader of the rest of the book
  noticing synthesis-vs-actual divergence).
- **MEDIUM** — claim is technically defensible but loose.
- **LOW** — claim is accurate but framing could be sharpened.

For each finding: cite chapter line number + chapter text + canonical
truth + recommended spot-fix.

Pay special attention to: geographic accuracy (Old Point Comfort /
Hampton); author personal-life claims (Ch 10:15 wife / parents /
twenty-year career); cross-cut figure consistency with Chs 2/3/4/7/9;
Mars administrator cross-reference to Ch 7; sunrise/sunset bookend
coherence with Ch 1; framework-synthesis claims (Ch 10:13).

== Web verification — default mode ==

For external-fact claims (geographies, industries, public events):
DEFAULT to WebSearch / WebFetch against authoritative sources BEFORE
flagging "verify against canonical X" for later work. Ch 10 is
literary-synthesis register and most of its fact-check surface is
internal-corpus (cross-chapter consistency), but the external-fact
items below should be web-verified:

- Old Point Comfort geography — verify against Hampton, VA city
  records; Fort Monroe National Monument records (NPS); USGS
  topographic maps; Hampton Roads / Chesapeake Bay regional
  references
- Baotou rare-earth processing — verify against USGS Mineral
  Commodity Summaries (Bayan Obo deposit; Inner Mongolia REE
  processing); industry publications (Mining Magazine; Argus REE)
- Niger Delta oil-cleanup status — verify against UNEP 2011
  Ogoniland report follow-up data; HYPREP (Hydrocarbon Pollution
  Remediation Project) status reports
- Ogallala Aquifer current depletion status — verify against USGS
  Water Resources / Texas Water Development Board / Kansas Geological
  Survey current saturated-thickness data
- Wikipedia ONLY as a starting-point pointer to primary sources
  (verify the underlying citation; do not cite Wikipedia itself)

Fact-check pass DOES the verification, not "flag for later." If
WebSearch returns conflicting authoritative sources, document the
disagreement.

Flag-for-later is reserved for:
- Internal-corpus claims (cross-chapter consistency with Chs 1/2/3/
  4/7/8/9 — these constitute the bulk of Ch 10's fact-check surface
  and require reading the actual chapter files, not WebSearch)
- Author personal-life claims (Ch 10:15 wife / parents / career
  framing) — these are author-internal-verifiable; WebSearch is not
  appropriate; cross-check against AuthorsNote + Ch 1 + dedication
  framings
- Claims requiring manual judgment beyond WebSearch

== Apparatus / consistency / named-subject sub-checks (§5 in output) ==

- **Apparatus residue.** Ch 10 is largely apparatus-light (literary-
  synthesis register). Verify no formal apparatus residue (Greek
  letters, integrals, subscripts) in body prose.
- **Path B contamination.** Verify no verbatim-clone passages from
  Chs 1-9. Some cross-reference paraphrase is expected (Ch 10
  recalls and synthesizes); verify it's paraphrase, not verbatim.
- **Named-subject consent.** Verify the author's wife (Ch 10:15)
  + parents (Ch 10:15) + any other family references are
  consent-clean (anonymized; no specific names; no specific
  consent-required identifying details).
- **Cross-chapter consistency.** McDowell (Ch 2 + Ch 8); Chesapeake
  (Ch 3); Niger Delta (Ch 4); Mars (Ch 7); Ogallala (Ch 9); Ch 1
  bookend.

== Out-of-scope flagging (§6 + §7 in output) ==

- **§6 Pass-2 (voice-polish) future-session input.** Ch 10 voice
  emphases will likely include literary-meditative register
  consistency; harbor-scene cadence (em-dash / declarative-three
  risks); cross-cut figure cadence (rule-of-three risk in 5-figure
  enumeration); Mars-administrator passage cadence (cross-chapter
  cadence-borrowing from Ch 7?).
- **§7 Pass-3 (audience-load) future-session input.** Tier-1
  trade-press reader (does the synthesis land?); Tier-2 memoir
  reader (does the literary-register hold?); Tier-3 cross-tier
  political reader (does the miner/waterman/farmer cross-cut land
  as inclusive or as appropriating?).

== Verdict synthesis (§8 in output) ==

- **§8.1 Findings tally.** Table.
- **§8.2 Aggregate Pass-1 verdict.** READY AS-IS / READY AFTER SPOT-
  FIXES / STRUCTURAL REVISION NEEDED.
- **§8.3 Phase-C disposition recommendation.** Sequenced list.

== Output ==

Single atomic commit on feature branch:
- tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_ch10_common_bonds_stage3_fact_check_v1.0.0.md

== Hard constraints ==

- Do NOT apply spot-fixes to the chapter file.
- Do NOT re-write paragraphs.
- Do NOT score Pass 2 or Pass 3 — flag-forward at §6 / §7.
- Do NOT contact named subjects.
- DO flag any cross-chapter consistency issue with Chs 1, 2, 3, 4, 7,
  8, 9 — Ch 10 is the synthesis chapter; misrepresentation of
  earlier-chapter content is HIGH severity.
- DO flag any named-subject consent issue (author's wife / parents /
  other family — anonymization register must hold).
- DO flag any apparatus regressions or Path B contamination.

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-ch10-pass1-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. Report rigor-pass back to PM session
+ author. Author ratifies which spot-fixes to apply via separate Phase C
session.

== Verify-stale-memory-claims discipline ==

Before asserting any time-sensitive claim:
- Verify chapter file path exists at session start (note: single-
  underscore prefix); verify line count.
- Verify Chs 1 / 2 / 3 / 4 / 7 / 8 / 9 file paths exist on origin/main
  for cross-reference reads.
- Verify AuthorsNote file path exists for personal-life cross-check.
- Verify the framework-synthesis "nine chapters" claim by reading
  the actual chapter count.
- If any cited file does not exist where claimed, stop and ask before
  guessing.
```

---

*End of Ch 10 Pass 1 paste-text. Expect moderate token budget — Ch 10 is literary-synthesis with a smaller raw fact-check surface than Chs 8/9, but the cross-reference verification surface (Chs 1/2/3/4/7/8/9) is broad. The session will spend most of its token budget on cross-chapter consistency reads.*
