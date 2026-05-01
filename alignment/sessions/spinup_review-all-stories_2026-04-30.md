# Full session spinup — Review ALL captured stories (disposition + integration plan)

**Created:** 2026-04-30 by Insight #37 follow-on (Thread β.1).
**Use case:** spin up a comprehensive session to walk through every captured story, evaluate per-story disposition (include / anonymize / edit / defer / reject), and produce an integration plan for Ch 1 + Ch 3.
**Layer:** internal-scaffolding per WP#10. Outputs are scaffolding decisions + chapter-integration plans; chapter-prose drafting itself is the next session (Insight #36 β.2).
**Prerequisite:** at least 3-5 stories captured at `research/story-drafts/` per the mini-spinup `spinup_capture-one-story_2026-04-30.md`. Project memory `project_personal_stories_drafting.md` gates per-story testing on 3-5 drafts existing.

---

## Copy-paste this block into a new Claude session

```
SESSION CONTEXT — Commons Bonds — Review ALL captured stories (disposition + integration plan)

Project: /Users/c17n/commons-bonds. Worktree-isolation git workflow per Working Principle #9.

GOAL: Walk through every story at research/story-drafts/. For each: evaluate per the test suite below, decide disposition, propose anonymization / length-edit changes if needed, and produce an integration plan that names which stories land in Ch 1 (publisher-facing prose) vs Ch 3 vs Book 2 seed vs archive. Output: per-story disposition matrix + Ch 1 + Ch 3 integration plans + updated candidates catalog + commit.

READ TO ORIENT (in order):

1. alignment/commons_bonds_personal_stories_candidates_v1.0.0.md (strategic catalog; current candidates + statuses + format spec)

2. research/story-drafts/ (every file in this directory; each is a captured raw story awaiting evaluation)

3. manuscript/chapters/Chapter__1___GuidanceDoc.md
   - Lines 70-93: structural-asks (the book needs living people / villain who isn't a villain / origin story)
   - Lines 138-143: story-types-worth-drafting menu
   - Lines 220-227: pre-drafting gates (CEO-era NDA / subordinate anonymization / wife's medical privacy / parents' privacy / Hampton observations)
   - Lines 365-426: operational guidance section (Pattern 2 anchor framing for commute-trade; Cᵢ cost-category mapping; conversational session structure)

4. manuscript/chapters/Chapter__3___GuidanceDoc.md
   - Operational guidance section (lines 132-230): Pattern 2 anchor framing for waterman; structural-asks; story-types menu; Cᵢ cost-category mapping; migrated §9.1 fieldwork specification; tone/consent notes

5. tools/commons_bonds_rigor_protocol_v2.2.0.md §M3 + §M4 + §M5 + §M9 + §M11 (per-story rigor test suite — see below for which modules apply)

6. alignment/commons_bonds_working_principles_v1.0.0.md
   - WP#10 (Two-layer content origination — internal scaffolding vs external publisher-facing)
   - WP#8 (publisher-facing scrubbed of scaffolding)

7. alignment/commons_bonds_open_insights_v1.0.0.md
   - Insight #9 (Pattern 2 / threaded verdict ratified 2026-04-30 — decision-time anchors at Ch 1 commute-trade + Ch 3 waterman)
   - Insight #13 (Book-scope creep monitoring — Book 1 framework / Book 2 applied advocacy)
   - Insight #36 (Ch 1 + Ch 3 conversational drafting session — gated on this review)
   - Insight #14 (Norway treatment + epistemic-humility discipline — Pattern 2 register family)
   - Insight #25 (academic-trade hybrid audience choice — Pattern 2 fits this audience natively)

OUT OF SCOPE FOR THIS SESSION:
- Tech Appendix · terms_index · Glossary · framework theorems · other chapters' drafts
- Capturing NEW stories (use spinup_capture-one-story_2026-04-30.md for that)
- Drafting Ch 1 or Ch 3 chapter prose itself (that's the next session, Insight #36 β.2; this session produces the integration plan that drives β.2)

PER-STORY EVALUATION: 5-MODULE TEST SUITE

For EACH story at research/story-drafts/, score against these five rigor-protocol modules:

- M3 (Case rigor): does the story demonstrate the framework's mechanism cleanly at individual / lived scale? Does it illuminate one or more Cᵢ cost categories without naming them? Cross-reference: Ch 1 GuidanceDoc operational §"Cost-category demonstration mapping" or Ch 3 GuidanceDoc same.
- M4 (Craft): does the prose hold pure Register 1? Voice-led, no data, no framework vocabulary? If author voice is uneven, what light edits would tighten it without breaking author voice?
- M5 (Dinner-table accessibility): does the story land for a non-economist reader at first read? Or does it require background to understand?
- M9 (Publishing path / book-scope): does the story fit Book 1's framework-establishment register vs Book 2's applied-advocacy register (per Insight #13 + #24)? Does it preempt Ch 2 / Ch 4 / Ch 5 / Ch 6 etc. content?
- M11 (Critic-survival): how does the story land under hostile readings? Free-market critic ("voluntary trade-off")? Lived-oppression critic ("you had elite resources; this is a privilege story")? Class-anxiety critic ("this is just a knowledge-worker complaining")? Materialist critic ("the structural argument requires more")? Pick 2-3 critic positions and stress-test the story's defense.

PER-STORY DISPOSITION (one of):

A. INCLUDE — chapter-ready or near-ready. Story passes M3+M4+M5+M9+M11 cleanly. Light edits OK; no major restructure.

B. ANONYMIZE — story is good but personal-detail risk hits one or more pre-drafting gates (CEO-era NDA / subordinate / wife's medical / parents / Hampton operators / waterman names). Propose specific anonymized phrasing. Author confirms.

C. EDIT FOR LENGTH — story is good but too long / dense for chapter integration. Propose specific cuts that preserve the structural demonstration. Note approximate target length.

D. EDIT FOR REGISTER — story is good but breaks Register 1 in places (uses framework vocabulary; reads as analytical rather than scene-based; codifies decision-time methodology in violation of WP#10 / Pattern 2). Propose specific reframings.

E. DEFER (Book 2 seed) — story is good but not a Book 1 fit. Per WP#10 internal-scaffolding bridges to Book 2: capture rationale, leave story at research/story-drafts/, flag candidate file as "Book 2 seed."

F. DEFER (later Ch 1 / Ch 3 cycle) — story is good but doesn't fit the immediate β.2 drafting cycle (e.g., requires interview that hasn't happened, or surfaces a question that needs author deliberation first). Flag with what's needed.

G. REJECT — story does not serve any chapter; archive and move on.

ANONYMIZATION GUIDANCE:

For Ch 1 stories — apply pre-drafting gates from Chapter__1___GuidanceDoc.md lines 220-227:
- CEO-era client names (NASA, Johns Hopkins, NIH, defense contractors, insurance companies, MDLogix-era specifics) → "a federal research client" / "a healthcare-IT firm" / generic-but-truthful framing; flag for legal counsel review per gate 1.
- Subordinates / direct-report references → scrub or seek consent.
- Wife's medical privacy → fact-of-near-death + recovery + caregiving-displacement OK; diagnosis / surgical specifics / ongoing condition NOT OK.
- Parents' privacy → "parents standing a little less straight" register OK; specific health/family-structure details NOT OK.
- Hampton operators → generic observational register ("a man moving on deck, a line cast, a cough"); specific names with consent only.

For Ch 3 stories — apply pre-drafting gates from Chapter__3___GuidanceDoc.md:
- Waterman names → ask consent at start of capture; default anonymity ("a waterman I know" / "the waterman with thirty years on the water") if consent uncertain.
- Specific boat / slip / family identifications → consent-gated.
- CBF / VIMS institutional handling → clarify view = institutional or individual.

LENGTH-EDIT GUIDANCE:

- Ch 1 target: 5,000-6,000 words total chapter; current publisher-facing wc 414 (gap to fill ~4,600-5,600).
- Ch 3 target: 5,000-6,000 words total chapter; currently undrafted (gap to fill = full).
- Recommend per-story length contribution: short anchor stories 300-600 words; medium scene stories 600-1,200 words; long demonstration stories 1,200-2,000 words. Aim for chapter to land 3-5 stories integrated, not 10+ at survey depth.

OUTPUT (write at session end):

1. Per-story disposition matrix → write to alignment/sessions/story-disposition_2026-MM-DD.md with format:

   | # | Story file | Chapter | Disposition | M3 | M4 | M5 | M9 | M11 | Notes / proposed edits |
   |---|---|---|---|---|---|---|---|---|---|

   Plus per-story sections expanding on critic-survival (M11) results, anonymization specifics, and length-edit recommendations.

2. Ch 1 integration plan → as a new section at the end of manuscript/chapters/Chapter__1___GuidanceDoc.md OR as a separate file alignment/sessions/ch1-integration-plan_2026-MM-DD.md (recommend the latter — keeps GuidanceDoc clean per WP#10).

   Format:
   - Selected stories (with raw-draft file paths)
   - Sequence in chapter (which story opens; which closes; bridging order)
   - Per-story integration notes (anonymization to apply; length-edit to apply; register-edit to apply)
   - Approximate word-count budget per story (sum to 5K-6K target)
   - Ch 1 §AUTHOR-ZONE-N mapping (which story lands in which AUTHOR-ZONE per the GuidanceDoc structural skeleton at lines ~280-320)

3. Ch 3 integration plan → analogous file alignment/sessions/ch3-integration-plan_2026-MM-DD.md.

4. Update alignment/commons_bonds_personal_stories_candidates_v1.0.0.md:
   - Per-story status flips: drafted → integrated (for INCLUDE) / drafted → deferred (for DEFER) / drafted → rejected (for REJECT) / drafted (with anonymization note for ANONYMIZE) / drafted (with length-edit note for EDIT)
   - §3 Drafted stories table populated
   - §4 Integrated stories — populated when β.2 drafting actually integrates; this session sets the plan, β.2 executes it
   - §5 Rejected candidates — populated for REJECT dispositions

5. If any of the dispositions surface a NEW insight (e.g., a story type the GuidanceDocs don't anticipate, a register-discipline issue not yet captured, a Book-scope edge case), raise it to alignment/commons_bonds_open_insights_v1.0.0.md as Insight #N (next free; check HEAD before claiming).

6. Commit + FF push per WP#9. Suggested commit message:
   "Story review session — disposition matrix + Ch 1 + Ch 3 integration plans + candidates catalog update"

DISCIPLINE:

- Apply ALL FIVE modules to every story; don't skip M11 even when stories feel obviously good (the critic-survival test is most valuable on stories that feel obvious).
- For ANONYMIZE / EDIT dispositions: propose SPECIFIC reframings inline so the author can accept / reject / amend the proposal directly. Don't return the story as "needs work" without showing what the work looks like.
- For DEFER (Book 2): be honest about Book-scope. Insight #13 names this — rich material that's not Book 1-appropriate accumulates internally as Book 2 / Book 3 seed; don't force-fit.
- Do NOT integrate stories into Chapter Drafts during this session — produce the integration PLAN; β.2 executes it. Per WP#10, internal review feeds external; the promotion is a separate step gated by the plan.
- If a captured story file lacks frontmatter or has incomplete metadata, flag it but evaluate the prose anyway. Note metadata gaps in the disposition matrix.

CONFLICT-ZONE NOTES:

- Thread α may concurrently be doing Phase α.2 Tech Appendix v2.0.0 rebuild; manuscript/chapters/* is β-thread-owned. No conflict unless Phase α touches a chapter Draft (it shouldn't).
- Thread γ may concurrently update README.md or archive/. No conflict.
- The candidates catalog file alignment/commons_bonds_personal_stories_candidates_v1.0.0.md is shared — coordinate via git pull before write.

INSIGHT NUMBERING: next free is #64 (or higher if α / β / γ / δ have claimed). Check alignment/commons_bonds_open_insights_v1.0.0.md HEAD before claiming.

START BY:
1. Listing every file at research/story-drafts/ with brief one-line summary per file.
2. Confirming with author: any stories Chris wants to defer / reject upfront before the formal evaluation? Any stories he wants to flag as load-bearing / chapter-anchor candidates?
3. Then walking the formal per-story evaluation in order.
```

---

## What success looks like for this session

- A disposition matrix at `alignment/sessions/story-disposition_2026-MM-DD.md` covering every captured story with M3+M4+M5+M9+M11 scoring + disposition + specific edits proposed.
- Two integration-plan files (`ch1-integration-plan_*.md` + `ch3-integration-plan_*.md`) that drive the next session (Insight #36 β.2 chapter drafting).
- Updated `alignment/commons_bonds_personal_stories_candidates_v1.0.0.md` with current per-story statuses + §3 / §4 / §5 populated.
- Optional: 1-2 new insights at the open-insights file if novel issues surfaced.
- Single batched commit + FF push.

## What this session does NOT do

- Does not draft chapter prose (that's Insight #36 β.2 — gated by the integration plans this session produces).
- Does not capture new stories (use the mini-spinup for that).
- Does not run pre-drafting gates as final-go (legal counsel for NDA, consent for waterman names) — proposes anonymization where applicable; author runs the actual gates.
- Does not commit to specific publisher / agent placement (that's downstream of manuscript completion).

## How to use this spinup

1. Confirm at least 3-5 stories exist at `research/story-drafts/` (per project memory's per-story testing gate). If fewer, run additional capture sessions first.
2. Open a new Claude session in the worktree of your choice.
3. Paste the SESSION CONTEXT block above (from `SESSION CONTEXT —` through `START BY:`) as the first message.
4. Walk the conversation: confirm upfront defer/reject calls, then per-story evaluation, then integration plans.
5. Approve outputs; let Claude commit + push.

Total session length expectation: 2-4 hours depending on story count. If story count > 8, consider splitting into two sessions (Ch 1 stories first; Ch 3 stories second).

## Cross-references

- Mini-session spinup that produces the inputs for this session: `spinup_capture-one-story_2026-04-30.md`.
- Strategic catalog: `alignment/commons_bonds_personal_stories_candidates_v1.0.0.md`.
- Chapter operational guidance: `manuscript/chapters/Chapter__1___GuidanceDoc.md` + `manuscript/chapters/Chapter__3___GuidanceDoc.md`.
- Working principles: WP#10 (two-layer content origination); WP#8 (publisher-facing scrubbed); WP#9 (worktree git workflow).
- Insights: #9 (Pattern 2 verdict); #13 (Book-scope creep); #14 (Norway epistemic-humility); #25 (academic-trade hybrid audience); #36 (Ch 1 + Ch 3 drafting — UNBLOCKED by this review); #37 (separation pass — closed-ratified 2026-04-30; this is post-#37 follow-on).
- Rigor protocol: `tools/commons_bonds_rigor_protocol_v2.2.0.md` §M3 / §M4 / §M5 / §M9 / §M11.
