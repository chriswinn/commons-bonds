# Aeon Essay (Post-Acceptance) — Two-Stage Drafting — Workstream Handoff (2026-05-10)

**Date drafted:** 2026-05-10
**Branch to create at session start:** `claude/aeon-essay-drafting-<harness-id>` (branch from current `origin/main`)
**Status going in:** **CONDITIONAL — fires only after Aeon accepts the pitch.** Pitch (Version C, *The Mask of Abundance*) submission scheduled for Mon Jun 1, 2026. Acceptance window is 4–8 weeks per `aeon-submission-strategy_2026-05-08.md`. **If acceptance lands, this handoff drives essay drafting using the validated two-stage discipline** (assuming Stage 3 of the Noema/Aeon-pitch experiment validates the discipline).

---

## Trigger condition

This handoff is dormant until:

1. **Aeon editorial response is positive** (any of: explicit acceptance; request for full essay; "we're interested, please send") AND
2. **The two-stage drafting discipline has been validated or modified** at Stage 3 of the experiment (per `feedback_audience_aware_drafting_discipline.md` and the Noema/Aeon-pitch comparison artifacts).

If both conditions hold, this handoff drives a fresh-session Stage 2 audience-blind flow draft of the Aeon essay (~3,500–4,500w, per Aeon's published essay range of 2,500–5,000w; aim for the middle).

---

## Workstream scope

Draft the Aeon essay version of *The Mask of Abundance* using the two-stage discipline. Source chapter: Ch 7 *On Other Worlds* (`manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md`) plus Ch 8 *What Things Actually Cost* for the McDowell case-walk and Ch 1 for the personal/commute case.

**Stage 1 (pre-draft audience pass) for the essay would be done in this handoff's prep session** (not the fresh session). It produces a Stage 1 brief similar to the Aeon-pitch Stage 1 brief at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_pre_draft_audience_structure_v1.0.0.md`, but for the full essay rather than the pitch:

- Audience set adapted from Aeon-pitch v1.0.0 (the same 14 characters apply; Aeon Philosophy Prize judges + Berggruen Prize judges remain Tier 2).
- Editorial-brain map: the editor handling the post-acceptance essay will likely be Sam Haselby (philosophy editor) or Sam Dresser (deputy). Voice + register matches the pitch.
- Comp-titles cluster: same as the pitch's, with potentially deeper engagement now that the essay has room.
- Structure: Aeon essays have looser structure than 300-word pitches; the brief should ratify a section structure (likely 5–8 sections).
- Voice register: same as the pitch's (literary-philosophical, thought-experiment-tolerant, abstract-tolerant).
- **Path B preemptive policy:** the same load-bearing constraint — do NOT open Ch 7, Ch 8, Ch 1, or the pitch versions as source texts.
- **Cultural-engagement commitment:** *The Mask of X* construction means the Dunbar/Du Bois/Ellison/Fanon engagement that was paratextual in the pitch becomes textual in the essay. Per `aeon-essay-dunbar-aside-drafts_2026-05-08.md`, Dunbar-aside drafts already exist (light/medium/heavy variants). The Stage 1 brief picks which variant to use and where it lands in the essay structure.

**Stage 2 (audience-blind flow draft) is the fresh session.** Produces `manuscript/essay/aeon/aeon-essay-fresh-session_<DATE>.md`.

**Stage 3 (rigor pass + comparison)** runs after Stage 2. Compares against any Stage-1-conformant baseline (likely just the Stage 1 brief itself; there's no "control" essay since the Aeon essay hasn't been drafted before).

---

## Why this matters

If Aeon accepts the pitch (which by the time this fires has happened), the post-acceptance essay is the high-stakes deliverable. Aeon essays get reviewed widely; an Aeon publication directly feeds the Berggruen Prize track, agent query letters (review-blurb material), and acquisitions-editor positioning. Drafting it well matters more than drafting the pitch well — the pitch was the gate; the essay is the product.

If the two-stage discipline validates at Stage 3 of the Noema/Aeon-pitch experiment, applying it here is the natural next test under load: a real-stakes essay drafted under real deadline pressure with editorial-collaboration overlay (Aeon's post-acceptance process involves back-and-forth with the editor). The discipline either holds or doesn't.

---

## Methodology

1. **Confirm acceptance and review editor's commission terms.** Aeon's post-acceptance process: editor sends commission letter with timeline, length target, any structural preferences. Read these carefully.
2. **Stage 1 prep session.** Build the Stage 1 brief as an Aeon-essay version of the Aeon-pitch Stage 1 brief. Save as `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_aeon_essay_pre_draft_audience_structure_v1.0.0.md`.
3. **Build the fresh-session handoff doc** for Stage 2. Save as `manuscript/essay/aeon/aeon-essay-session-handoff_<DATE>.md`. Mirror the structure of the Aeon-pitch handoff at `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md`.
4. **Trigger fresh session for Stage 2.** Audience-blind flow draft. Stops after drafting.
5. **Stage 3 rigor pass.** Run audience-load rigor against the Stage 1 brief's audience set. Apply fixes.
6. **Editor collaboration phase.** Send to Aeon editor; iterate per editorial direction.
7. **Final polish + AI disclosure.** Submit final essay.

**Path B audit during Stage 3:** essential. Aeon's "we only publish original content" rule applies to the essay too. The Stage 2 draft must pass Path B against Ch 1, Ch 7, Ch 8 — the chapters that source the essay's material.

---

## Current state (as of 2026-05-10, before trigger condition fires)

- **Pitch ratified** for Mon Jun 1 2026 submission.
- **Dunbar aside drafts** at `manuscript/essay/aeon/aeon-essay-dunbar-aside-drafts_2026-05-08.md` (light/medium/heavy variants). These are paratextual prep for the post-acceptance essay; one will be selected per Stage 1 brief.
- **Source chapters** drafted: Ch 1, Ch 7, Ch 8.
- **Two-stage discipline experiment in flight** — Stage 2 fresh sessions for Noema essay and Aeon pitch are pending. Stage 3 verdicts will determine whether the discipline holds.
- **AI disclosure paragraph** ready in `publishing/essay-drafts/templates/ai-disclosure-paragraph.md`.

---

## Deliverables (post-trigger)

1. **`tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_aeon_essay_pre_draft_audience_structure_v1.0.0.md`** — Stage 1 brief.
2. **`manuscript/essay/aeon/aeon-essay-session-handoff_<DATE>.md`** — fresh-session handoff doc for Stage 2.
3. **`manuscript/essay/aeon/aeon-essay-fresh-session_<DATE>.md`** — Stage 2 audience-blind flow draft.
4. **`tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_aeon_essay_audience_load_v1.0.0.md`** — Stage 3 rigor pass + audit findings.
5. **`manuscript/essay/aeon/aeon-essay-final_<DATE>.md`** — final essay after editor-collaboration phase + Stage 3 polish.

---

## First actions for fresh session (post-trigger)

1. Confirm the trigger condition: Aeon accepted the pitch AND two-stage discipline status is known (validated, modified, or falsified per Stage 3 of the Noema/Aeon-pitch experiment).
2. Read this handoff end-to-end.
3. Read the Aeon editor's commission letter (length, deadline, structural preferences).
4. Read the Aeon-pitch Stage 1 brief at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_pre_draft_audience_structure_v1.0.0.md` — this is the template for the essay's Stage 1 brief.
5. Read `feedback_audience_aware_drafting_discipline.md` (memory). If the discipline was modified, read the modification.
6. Build the Stage 1 brief in this prep session.
7. Build the fresh-session handoff doc.
8. Trigger fresh Claude Code session for Stage 2.

---

## What NOT to do

- Do not draft the essay before Aeon acceptance. Pre-drafting is wasted effort if Aeon declines.
- Do not skip the Stage 1 prep session. The whole point of the two-stage discipline is that Stage 1 happens before Stage 2.
- Do not have the Stage 2 fresh session read the chapters as source texts. Same Path B preemptive policy as the pitch.
- Do not skip the Dunbar aside engagement — *The Mask of X* construction obligates explicit cultural engagement in the essay body. The aside drafts already exist; pick one.
- Do not bypass editor collaboration. Aeon's post-acceptance process is part of the artifact; engage with it rather than around it.

---

## Reference files

- `manuscript/essay/aeon/aeon-pitch-commons-bonds-winn_VERSION-C.md` (the pitch that got accepted)
- `manuscript/essay/aeon/aeon-essay-dunbar-aside-drafts_2026-05-08.md` (Dunbar engagement variants)
- `manuscript/essay/aeon/aeon-submission-strategy_2026-05-08.md` (post-acceptance context)
- `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md` (template for the essay's handoff)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_pre_draft_audience_structure_v1.0.0.md` (template for the essay's Stage 1 brief)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-08_aeon_pitch_title_candidates_v1.0.0.md` (title rigor pass)
- `manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md` (primary source — DO NOT read as source text in fresh session)
- `manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md` (McDowell case)
- `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md` (commute case)
- `feedback_audience_aware_drafting_discipline.md` (memory)
- `research/literature/bibliography.md` §21 (Black literary tradition citations)
- `publishing/essay-drafts/templates/ai-disclosure-paragraph.md`

---

*End of handoff.*
