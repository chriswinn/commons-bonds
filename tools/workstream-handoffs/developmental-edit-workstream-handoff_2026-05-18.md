# Workstream Handoff — Developmental-Editing Workstream Class

**Date:** 2026-05-18
**Workstream class:** Developmental-Editing (per-chapter; whole-chapter
scale; restoration-of-richness lens)
**Status:** OPEN — Ch 1 first session landed PROPOSED 2026-05-18; Ch 2
through Ch 10 + AuthorsNote pending per-chapter sessions
**Triggering observation (author, 2026-05-18):** "Ch 1's prose
(post Stage 3 four passes + Phase C ratified-and-applied) still feels
flat / unemotional / over-compressed."
**Workstream rationale:** Pass 3.2 voice-polish operates at per-paragraph
LLM-tic scale + caught what it was designed to catch; this workstream
operates at whole-chapter scale + catches what Pass 3.2 doesn't —
emotional arc, voice flow, scene-anchor density, sensory detail
restoration, reader engagement across the chapter.

---

## §1. Workstream definition

### §1.1 Scope

Per-chapter developmental-editing review at whole-chapter scale. Each
chapter fires as its own session per branch discipline (one chapter per
session per the per-chapter retrofit pattern). Each session produces a
PROPOSED developmental-edit review artifact at
`tools/rigor-passes/ch<N>_developmental_edit_review_<date>.md` with:

- Per-finding format (F-DE-Ch<N>-K) — severity (HIGH / MEDIUM / LOW);
  location (line + verbatim current text); diagnosis (what reads as
  flat / compressed / lost-richness); proposed rewrite(s) (specific
  prose; same canonical-facts + same consent gates + same named-subject
  discipline); cross-pass flag (whether the rewrite affects any prior
  Pass 1 / Pass 2 / Pass 3 finding's disposition).
- Whole-chapter synthesis §: cumulative diagnosis (what produced the
  flatness?); cumulative recommendation (apply N rewrites; restore K
  paragraphs of cut richness; structural pacing adjustment); token-
  economy note per Amendment A; cross-chapter cascade flag.

### §1.2 What this workstream catches that the existing four-pass
Stage 3 architecture does not

| Pass | Scale | Catches | Misses |
|---|---|---|---|
| 3.1 fact-check | Per-fact | Factual drift; source-citation accuracy | Whole-chapter narrative arc |
| 3.2 voice-polish | Per-paragraph | LLM tics (named-inventory matches) | Cumulative effect of multiple tic-fixes; clipped-after-cutting feel |
| 3.3 acceptance | Per-character (per-audience) | Whether target audiences INCLUDE | Whether the chapter HOLDS reader attention through analytically-loaded passages |
| 3.4 robustness | Per-adversarial-character | Hostile-read thread-pull synthesis | Same as 3.3 — character-set tests rather than experience-of-reading |
| **Developmental-edit (proposed Pass 3.5 or equivalent)** | **Whole-chapter** | **Emotional-arc continuity; scene-anchor density; sensory-detail restoration; voice-flow continuity; cumulative-LLM-cadence residue; reader-engagement at analytical pivots** | **Cross-chapter narrative arc (handled by separate cross-chapter developmental-coherence workstream)** |

### §1.3 Per-chapter sequencing plan

Per the session brief, after Ch 1 lands:

| Order | Chapter | Status (as of 2026-05-18) |
|---|---|---|
| 1 | Ch 1 — The Quiet Math | **PROPOSED 2026-05-18** (this workstream's first session) |
| 2 | Ch 2 — The Miner | Pending |
| 3 | Ch 3 — The Waterman | Pending |
| 4 | Ch 4 — The Existence Proof | Pending |
| 5 | Ch 5 — The Accountability Gap | Pending |
| 6 | Ch 6 — Three Ways of Counting | Pending |
| 7 | Ch 7 — On Other Worlds | Pending |
| 8 | Ch 8 — What Things Actually Cost | Pending |
| 9 | Ch 9 — Pricing Honestly | Pending |
| 10 | Ch 10 — Common Bonds | Pending |
| 11 | AuthorsNote — On Wind Tunnels and AI | Pending |
| — | Dedication | **SKIPPED** (too short to warrant developmental-edit review) |

**Each chapter fires as its own session per branch discipline.**
PM-session-handoff queues the next chapter after the prior chapter's
session closes (and after the Phase C application of any ratified
spot-fixes, if the author chooses to apply between sessions vs. batch
at the end).

**Cross-chapter developmental-coherence workstream** (separate):
fires after all per-chapter developmental edits land + Phase C
applications complete. Tests cross-chapter narrative arc; recurring
patterns surfaced across the per-chapter sessions; consistency-of-
treatment across analytical pivots (e.g., the both/and reveal
pattern flagged at Ch 1 §5.4); cross-artifact coherence with
AuthorsNote + Tech Appendix + bibliography commitments.

### §1.4 Cascade per pipeline doctrine Amendment A

This workstream is an EXPLICIT-GATE pass per Amendment A §3.2. Fires:

- **Per-chapter, after Stage 3 four passes + Phase C ratify-and-apply
  complete.** Ch 1 retrofit closes the four-pass cycle; developmental
  edit fires now. Same gating for Ch 2 through Ch 10 + AuthorsNote —
  developmental edit fires after the chapter's four-pass cycle closes.
- **Before pre-publication.** The developmental edit is gate-relevant
  to publication readiness. Pre-publication gating may automatically
  queue this pass alongside Stage 4 (render-integrity audit) + Stage 5
  (sign-off + pre-pub review queue) + Pass 3.3 + Pass 3.4 as a
  pre-pub-readiness batch.
- **Not on every prose edit.** Heavy work; only valuable at
  chapter-level distribution-readiness gates.
- **Light re-fire pattern (post-Phase-C)**: after the author ratifies
  + applies developmental-edit spot-fixes, a light re-fire of Pass
  3.3 (acceptance, light) recommended to confirm cumulative
  acceptance verdicts hold. Pass 3.4 re-fire NOT warranted (the
  restorations strengthen rather than weaken adversarial robustness;
  thread-pull surface unchanged).

### §1.5 Token-economy positioning

Approximate Claude-token cost per chapter session:

- **Per-chapter developmental-edit pass:** ~50K–80K tokens (whole-
  chapter context + 3-4 rigor-pass artifacts + AuthorsNote + several
  raw-substrate dumps in context; reasoning + finding-extraction;
  per-finding restoration drafts; whole-chapter synthesis).

Per Amendment A's token-economy table at §3.4: this pass sits at the
**explicit-gate cascade** end of the spectrum (heavy; comparable in
token-weight to Pass 3.3 acceptance + Pass 3.4 robustness + Stage 4
render-integrity audit), NOT at the automatic-on-edit cascade end.

**Total workstream-class cost** (10 chapters + AuthorsNote × ~65K
tokens average per session) ≈ 650K–800K Claude tokens distributed
across 11 sessions over multiple days/weeks per per-prompt serial
cadence.

---

## §2. Doctrine-amendment — RATIFIED 2026-05-18 (Option (a) Pass 3.5 within Stage 3)

**Status update 2026-05-18:** the doctrine-amendment candidate flagged in this section was RATIFIED by author 2026-05-18 — Option (a) "Pass 3.5 within Stage 3" — codified as **pipeline doctrine v1.0.0 Amendment B**. See `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` §3.6 for the formal codification + `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` (v3.1) for the updated five-pass Stage 3 template. Stage 3 is now a five-pass rigor audit: 3.1 → 3.2 → 3.3 → 3.4 → 3.5. Memory entry bumps to v3.1.0 (memory-update spec at `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md` revised to capture the v3.1.0 framing).

Empirical-grounding-recommendation in §2.3 below was OVERRIDDEN — author ratified on Ch 1 single-chapter empirical basis + methodological-clarity argument (Pass 3.2 cuts; Pass 3.5 restores; opposite polarities; folding would lose discipline). Cross-chapter empirical grounding continues via this workstream's per-chapter sessions; if cross-chapter data surfaces material refinements, those land as future amendments (Amendment C, etc.) without disturbing Pass 3.5's codification.

The original session brief framing is preserved below as audit trail:

### §2.1 Candidate statement

The developmental-editing lens operates at a scale + catches findings
that the existing four-pass Stage 3 architecture
(3.1 fact-check / 3.2 voice-polish / 3.3 acceptance / 3.4 robustness)
does not. Empirically grounded by the Ch 1 PROPOSED review at
[`tools/rigor-passes/ch1_developmental_edit_review_2026-05-18.md`](../rigor-passes/ch1_developmental_edit_review_2026-05-18.md):
the 3 HIGH findings (§4 analytical-overlay; grandfather lineage-load;
§3 compression + both/and reveal breath) are not findings any of the
four existing passes was designed to surface, yet they are
gate-relevant to publication readiness.

### §2.2 Codification options

The doctrine-amendment session would choose among:

- **Option (a) Pass 3.5 within Stage 3.** Extends the existing 3.1 →
  3.2 → 3.3 → 3.4 cadence into 3.1 → 3.2 → 3.3 → 3.4 → 3.5.
  Advantages: continuity with existing pass-numbering; same per-prompt
  serial cadence applies; same Phase C ratify-and-apply pattern.
  Trade-offs: extends Stage 3's already-multi-pass scope; may dilute
  Stage 3's per-paragraph rigor-pass identity.

- **Option (b) New explicit-gate cascade item.** Alongside Stage 4
  (render-integrity audit) and Stage 5 (sign-off + pre-pub review
  queue) per the Amendment-A explicit-gate cascade table.
  Advantages: cleanly positioned as gate-relevant heavy-pass;
  token-economy-positioning matches Stage 4 + Stage 5; explicit-gate-
  cascade structure already exists to absorb the new item.
  Trade-offs: less natural numbering (the cascade table is
  stage-numbered); operates on prose-content rather than render-
  artifact (which is what Stage 4 + Stage 5 operate on).

- **Option (c) Stage 3.5 between Stage 3 and Stage 4.** Treats
  developmental-editing as a distinct stage rather than a pass within
  Stage 3. Advantages: clean separation of per-paragraph (Stage 3) vs
  whole-chapter (Stage 3.5) vs render-side (Stage 4) work; honors
  the scale-distinction the workstream class makes salient.
  Trade-offs: introduces a new stage-numbering item (cumulatively
  more stages); may overweight the workstream's structural
  importance relative to existing stages.

Each option has trade-offs in: where in the cadence; what triggers it;
how the cross-chapter developmental-coherence workstream fits;
whether per-prompt serial cadence applies; how the cascade routing
protocol (§3 of pipeline doctrine) treats developmental-edit findings.
Out-of-scope for both this workstream-handoff and the per-chapter
sessions; deferred to a separate doctrine-amendment session.

### §2.3 Empirical-grounding requirement before codification

Per the workstream class's per-chapter sequencing plan, this Ch 1
session + the planned Ch 2 → Ch 10 + AuthorsNote sessions will
provide empirical grounding for the doctrine-amendment session:

- **10 chapters × per-chapter findings.** Aggregate the finding-counts
  + severity-distributions across chapters to see whether the
  developmental-edit lens consistently produces gate-relevant findings
  (justifying codification) or whether the Ch 1 finding-density is
  anomalous (suggesting the doctrine-amendment is premature).

- **Cross-chapter recurring-pattern observations.** Do the same
  classes of findings recur across chapters (e.g., the analytical-
  overlay pattern at chapter-load-bearing sections; the
  compression-without-breath pattern at substrate-dense sections;
  the under-built lineage-load pattern at character sections)? If
  so, this strengthens the codification case + may surface
  refinements to the doctrine-amendment proposal.

- **Cumulative token-economy data.** Actual token-costs per session
  + total workstream-class cost will refine the §1.5 estimates +
  inform the doctrine-amendment's explicit-gate-cascade positioning.

Recommended sequencing: complete all 11 per-chapter sessions + Phase
C applications + light Pass 3.3 re-fires; then run the
doctrine-amendment session with the empirical grounding in hand. Do
NOT codify the amendment prematurely on Ch 1's single-chapter
evidence alone.

---

## §3. PROPOSED → ratified → applied workflow

Per CLAUDE.md rigor-pass artifact discipline + the merge-to-main
default for rigor-pass artifacts:

### §3.1 Per-chapter session (this workflow applies to each of the
11 per-chapter sessions) — UPDATED 2026-05-19 per pipeline-doctrine
v1.0.0 Amendment C (interactive ratification protocol)

**Two-session workflow per chapter (replaces the three-step pre-
Amendment-C pattern):**

**Session 1 — Discovery:**

1. Branch from current origin/main as
   `claude/ch<N>-developmental-edit-<harness-id>`. Read the chapter
   end-to-end at whole-chapter scale + the prior Pass 1 / Pass 2 /
   Pass 3.3 / Pass 3.4 artifacts + AuthorsNote + relevant raw-substrate
   dumps in `research/story-drafts/`.

2. Surface findings per Amendment C §3.7.2 per-finding format
   (Finding ID + Severity + Location + Diagnosis + **Options** +
   **Recommendation** + **Reasoning** + initial Author disposition: TBD).

3. Produce PROPOSED artifact at
   `tools/rigor-passes/ch<N>_developmental_edit_review_<date>.md`.

4. PROPOSED artifact autonomously fast-forward merges to main per
   CLAUDE.md rigor-pass merge default (chapter source untouched
   in this session).

**Session 2 — Interactive ratification + application (combined per
Amendment C §3.7.6):**

5. Branch from current origin/main as
   `claude/ch<N>-developmental-edit-ratify-apply-<harness-id>`. Read
   the PROPOSED artifact from session 1 + the chapter source.

6. Walk author through each finding per Amendment C §3.7.4 format:
   present Options + Recommendation + Reasoning → author selects
   A/B/C/hold/other/defer → capture disposition + author rationale.

7. **Apply ratified spot-fixes to chapter source in the same
   session.** Each APPLY disposition produces a chapter-source
   change; commit with the disposition log update.

8. Append §"Disposition log (YYYY-MM-DD interactive ratification +
   application session)" to the PROPOSED artifact with the
   Amendment C §3.7.5 table format (Finding / Severity / Selected
   option / Disposition / Author rationale / Commit short-sha).

9. Both updates auto-merge to main per CLAUDE.md author-ratified
   content-change merge default.

10. **Light Pass 3.3 re-fire recommended.** After application,
    light Pass 3.3 (acceptance) re-fire to confirm cumulative
    acceptance verdicts hold across the affected character-set.
    Pass 3.4 (robustness) re-fire NOT routinely warranted; can be
    added on author trigger.

11. **PM-session-handoff queues next chapter.** Next chapter's
    developmental-edit session enters the queue per the §1.3
    sequencing plan.

**Pre-Amendment-C ratifications stay valid.** Ch 1 dev-edit
ratification at commit `1f5c6ad` 2026-05-18 ("as recommended and
proposed") remains valid — those dispositions are author-ratified
per the prior workflow. **However, per Amendment C §3.7.7
retroactive scope rule: Ch 1's Phase C application (not yet fired)
follows Amendment C interactive protocol** — author sees each
restoration applied in context as it lands.

### §3.2 Cross-chapter developmental-coherence session (fires once;
after all 11 per-chapter sessions complete)

After all 11 per-chapter sessions land + Phase C applications complete
+ light Pass 3.3 re-fires clear:

1. **Cross-chapter developmental-coherence session.** Reads all 10
   chapters + AuthorsNote end-to-end. Tests:
   - Cross-chapter narrative arc continuity.
   - Recurring-pattern consistency (e.g., do all chapter-load-bearing
     pivots get breath; do all character-sections have appropriate
     lineage-load).
   - Cross-artifact coherence with AuthorsNote + Tech Appendix +
     bibliography commitments.
2. **Produces** `tools/rigor-passes/cross_chapter_developmental_coherence_<date>.md`.
3. **Closes the workstream-class** after Phase C cross-chapter
   spot-fix application + light Pass 3.3 batch re-fire across all
   touched chapters.

---

## §4. Open questions for PM-session

1. **Per-chapter session pacing.** All 11 per-chapter sessions
   back-to-back (full workstream-class throughput; ~5-10 days at
   one-session-per-day cadence), or distributed across the
   pre-publication runway? Author's call.

2. **Phase C application timing.** Apply Phase C spot-fixes after
   each per-chapter session (more cadence-discipline; light Pass
   3.3 re-fire after each), or batch all 11 PROPOSED artifacts +
   author ratifies all in one batch + one Phase C application
   session per chapter (faster workstream-class throughput; light
   Pass 3.3 batch re-fire across all chapters at the end)? Author's
   call.

3. **Doctrine-amendment session timing.** Run after all 11 per-
   chapter sessions land (full empirical grounding), or earlier if
   the Ch 1 findings already suggest the doctrine-amendment is
   warranted? Recommended: wait for full empirical grounding.

4. **AuthorsNote treatment.** The AuthorsNote is structurally
   different from chapter prose — paratextual; shorter; explicit
   meta-commentary about AI collaboration. Does the developmental-
   edit lens apply unchanged, or does the AuthorsNote need a
   modified protocol? Open question for the AuthorsNote session.

5. **Cross-chapter cascade flag interaction with cross-chapter
   developmental-coherence session.** Per Ch 1 §5.4, two cross-
   chapter cascade flags emerged (faithfulness-of-the-model
   register-coherence with AuthorsNote; both/and reveal pattern
   consistency across chapters). Should these batch into the
   cross-chapter session, or trigger lighter cross-artifact light
   re-fires sooner? Recommended: batch into the cross-chapter
   session unless any individual flag becomes blocking.

---

## §5. References

- **This workstream's first session artifact:**
  [`tools/rigor-passes/ch1_developmental_edit_review_2026-05-18.md`](../rigor-passes/ch1_developmental_edit_review_2026-05-18.md)
- **Pipeline doctrine:**
  [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)
  (Amendment A — selective stage-firing — establishes the
  explicit-gate-cascade framework this workstream operates within).
- **Stage-3 rigor-pass template:**
  [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md)
  (template for the existing four passes; developmental-edit pass
  format mirrors Pass 3.2 voice-polish artifact structure per
  session brief).
- **Memory entry (cross-session discipline reference):**
  `tools/memory/feedback_audience_aware_drafting_discipline.md` (v3.0
  Amendment B carry-forward; the four-pass Stage 3 architecture this
  workstream proposes to extend).

---

*End of Developmental-Editing Workstream Handoff — Ch 1 first session
landed PROPOSED 2026-05-18. Ch 2 through Ch 10 + AuthorsNote queued.
Cross-chapter developmental-coherence session queued for after all
per-chapter sessions complete. Doctrine-amendment session queued for
after full empirical grounding lands.*
