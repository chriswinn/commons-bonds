# Mini-session spinup — Capture ONE story (Ch 1 or Ch 3)

**Created:** 2026-04-30 by Insight #37 follow-on (Thread β.1).
**Use case:** spin up a focused conversational session to capture ONE personal or waterman story into a raw draft. NOT a chapter-drafting session — this captures raw material for later evaluation.
**Layer:** internal-scaffolding per WP#10. Output is research-layer raw material; chapter-prose promotion is decided in the review session (see `spinup_review-all-stories_2026-04-30.md`).

---

## Copy-paste this block into a new Claude session

```
SESSION CONTEXT — Commons Bonds — capture ONE story (mini-session)

Project: /Users/c17n/commons-bonds. Worktree-isolation git workflow per Working Principle #9.

GOAL: Capture ONE story from Chris into a raw draft at research/story-drafts/. Single story per session. Conversational mode — Chris narrates / types; you ask targeted follow-ups; you write the captured prose to disk at session end.

SCOPE:
- Either a Ch 1 story (Chris's own personal narrative) OR a Ch 3 story (waterman story Chris is recounting from interview / observation).
- Chris picks at session start which chapter + which story type.

READ TO ORIENT (in order; minimal):
1. alignment/commons_bonds_personal_stories_candidates_v1.0.0.md (existing candidates + format spec; the captured story will land here as a tracking entry + as a separate raw-draft file)
2. For Ch 1: manuscript/chapters/Chapter__1___GuidanceDoc.md §"Story types worth drafting" (lines 138-143) + §"Pre-drafting gates" (lines 220-227) + §"Operational guidance" (lines 365-426)
3. For Ch 3: manuscript/chapters/Chapter__3___GuidanceDoc.md §"Story types worth gathering" + §"Migrated fieldwork specification" (§9.1 core questions) + §"Tone / consent notes"

DO NOT READ (out of scope for this session):
- Tech Appendix · terms_index · open insights · framework theorems · other chapter Drafts. The story capture does NOT need framework vocabulary; pure Register 1.

REGISTER DISCIPLINE (load-bearing):
- Pure Register 1: voice-led, scene-and-observation-based. NO data, NO formulas, NO framework vocabulary (CIT, RCV, Cost Severance, Accountability Bond, Cᵢ categories, etc.).
- The captured story should read as Chris's voice (or, for Ch 3, as Chris recounting a waterman's voice with appropriate texture).
- Do not codify a methodology in the story prose (Pattern 2 per Insight #9). Demonstrate; don't prescribe.

OUTPUT FORMAT (write at session end):

1. Raw story draft → research/story-drafts/<chapter>_<slug>_2026-MM-DD.md
   Example filenames:
   - research/story-drafts/ch1_120-hour-week_2026-04-30.md
   - research/story-drafts/ch1_commute-trade_2026-04-30.md
   - research/story-drafts/ch3_generational-handoff_2026-04-30.md
   - research/story-drafts/ch3_year-water-changed_2026-04-30.md
   File contents:
     ---
     # <Story title>
     **Captured:** YYYY-MM-DD by Chris Winn (story-capture session)
     **Chapter target:** Ch <1|3> — <chapter title>
     **Status:** drafted (awaiting review per spinup_review-all-stories_2026-04-30.md)
     **Story type:** <one of the menu types from the relevant GuidanceDoc>
     **Pre-drafting-gate flags:** <list any gates touched: NDA review needed, subordinate anonymization, wife's medical privacy, parents' privacy, Hampton-community observations, waterman-consent — match the chapter's gate list>
     **Length:** <wc -w>
     ---
     <raw story prose; pure Register 1>

2. Update alignment/commons_bonds_personal_stories_candidates_v1.0.0.md:
   - If story is a NEW candidate not yet in §2: add a Candidate #N entry per §1 format with status "drafted" + cross-reference to the raw-draft file.
   - If story extends an EXISTING candidate (e.g., Candidate #1 commute-trade): flip status candidate → drafted; add cross-reference to the raw-draft file.

3. Commit the new file + candidates-doc update in a single batched commit:
   "Story-capture session — <chapter> <slug> raw draft + candidates catalog update"
   FF push to main per WP#9.

CONVERSATIONAL APPROACH:

Step 1 — At session start, ask Chris:
  (a) Ch 1 (Chris's own story) or Ch 3 (waterman story)?
  (b) Which story type from the relevant GuidanceDoc menu?
  (c) Any specific framing notes Chris wants to start with (a remembered line, a place, a moment)?

Step 2 — Chris narrates / types the story in his own voice. You take it down verbatim where possible. Where he pauses or jumps, you ask ONE follow-up at a time per the relevant question architecture:
  - For Ch 1 stories: lean on the four-story-types prompts at GuidanceDoc lines 138-143 (logistics, what was displaced, knowledge handoff, business-vs-family calendar) — but only what Chris hasn't already given.
  - For Ch 3 waterman stories: lean on the §9.1 core questions (generational handoff, specific year, last-year-caught, what-tell-children, when-the-sense-changed, what-was-asked-vs-paid-back). Only after rapport.

Step 3 — When Chris signals he's done OR when the natural arc has landed, read back the draft to him. Ask: anything to add, cut, or reframe? Anonymize?

Step 4 — Pre-drafting-gate check (do NOT run the gates; FLAG them):
  - Ch 1 stories: CEO-era NDA / subordinate anonymization / wife's medical privacy / parents' privacy / Hampton observations.
  - Ch 3 stories: waterman consent / Hampton-specificity / CBF/VIMS institutional handling / dignity discipline.
  Note in the Pre-drafting-gate-flags frontmatter which gates are touched. Author resolves them later.

Step 5 — Write to disk per OUTPUT FORMAT above. Update candidates catalog. Commit + push.

DISCIPLINE:
- ONE story per session. If a second story surfaces, capture it as a candidate-level note in the catalog file (not as a draft) and recommend a follow-on session.
- Do not edit Chris's voice. Light grammatical / continuity polish OK; no register-shifting, no analytical reframing.
- Do not name framework concepts in the prose even if Chris does. If Chris uses framework vocabulary while narrating, ask if he wants the prose to keep it (default: no — Pattern 2 / Register 1).
- If a pre-drafting gate is hit (specific named individuals, NDA-territory clients, medical specifics), flag in frontmatter and propose anonymized phrasing inline; let Chris choose.

INSIGHT NUMBERING: do not raise new insights this session unless something genuinely surprising surfaces. Story capture is mechanical; the review session (spinup_review-all-stories_2026-04-30.md) is where insights surface.

START BY: asking Chris which chapter + which story type + any opening anchor he wants to start with.
```

---

## What success looks like for this session

- One new file at `research/story-drafts/<chapter>_<slug>_2026-MM-DD.md` with raw Register-1 story prose + frontmatter metadata.
- One updated entry in `alignment/commons_bonds_personal_stories_candidates_v1.0.0.md` (status flipped to "drafted" with cross-reference to the raw file).
- One batched commit + FF push.
- No chapter-prose changes. No GuidanceDoc changes. No framework vocabulary in the captured story.

## What this session does NOT do

- Does not integrate the story into any Chapter Draft (that's β.2 chapter-drafting work, gated by the review session).
- Does not run pre-drafting gates (NDA, anonymization, etc.) — only flags them.
- Does not evaluate the story for inclusion / fit / register quality (that's the review session).
- Does not name framework concepts in the prose.
- Does not handle multiple stories — one per session, full stop.

## How to use this spinup

1. Open a new Claude session in the worktree of your choice.
2. Paste the SESSION CONTEXT block above (from `SESSION CONTEXT —` through `START BY:`) as the first message.
3. Answer Claude's opening question (chapter / story type / opening anchor).
4. Narrate the story; respond to follow-ups.
5. Approve the read-back; let Claude write to disk + commit.

Total session length expectation: 30-90 minutes per story depending on depth.
