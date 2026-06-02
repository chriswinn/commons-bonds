---
artifact: Pipeline doctrine two-level reorganization — PROPOSED
date: 2026-06-02
session_of_origin: claude/pipeline-prose-revision-corpus-audit-260602-6b5eda
status: PROPOSED — captures the collaborative framework settled in the 2026-06-02 interactive session; awaits author ratification before becoming doctrine v-next
supersedes: nothing yet (proposal layer); on ratification it amends commons_bonds_pipeline_doctrine_v1.0.0.md
extends: the six amendments (X.1–X.6) proposed in tools/workstream-handoffs/pipeline-prose-revision-and-corpus-wide-audit-handoff_2026-06-01.md §2
scope: items 1 + 2 + the framework for item 4 of the expanded workstream (pipeline doctrine reorg + prose-craft integration + differentiation-framework structure); item 3 mechanical scan + item 4 per-essay profiles fire in subsequent work
empirical_anchor: Atlantic Ideas Pricing-Honestly iteration (2026-05-28 → 2026-06-01) + the archived per-chapter GuidanceDocs (manuscript/chapters/archive/) read 2026-06-02
---

# Pipeline doctrine — two-level reorganization (PROPOSED 2026-06-02)

## §0. What this is and how to read it

The 2026-06-01 handoff surfaced seven lessons, six proposed amendments
(X.1–X.6), and a cross-corpus duplication observation. The 2026-06-02
interactive session worked those collaboratively and reached a more
structural conclusion than a flat list of six amendments: **the current
pipeline is missing an entire level.**

This artifact captures that conclusion as a PROPOSED reorganization. It is
not yet doctrine. Per the session's "decide per-amendment as we go"
direction (author, 2026-06-02), the codification *container* — whether this
becomes "Amendment E" or a structurally distinct revision — is itself one of
the open decisions in §7, deliberately left for ratification rather than
pre-committed.

Read this against:
- The handoff: `tools/workstream-handoffs/pipeline-prose-revision-and-corpus-wide-audit-handoff_2026-06-01.md`
- Current doctrine: `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`
- The proto-artifact this reorg supersedes in spirit: the archived per-chapter
  GuidanceDocs at `manuscript/chapters/archive/Chapter__*___GuidanceDoc.md`
  and the embryonic portfolio file `manuscript/chapters/_BookLevelGuidance.md`.

Every change below carries an explicit **Reasoning** line, per author
direction. §8 consolidates the changes into a single table.

---

## §1. Root-cause reframe — max-length manufactured compression at generation time

**The finding.** The compressed, clunky prose the Atlantic Ideas iteration
fought was not a rigor-pass failure. It was a **generation-time** failure.
Setting maximum lengths *manufactured* compression at the moment of drafting.
Everything downstream — Pass 3.2's cuts, Pass 3.5's restorations, the
handoff's proposed X.1 fresh-draft diagnostic — is machinery for repairing
damage built in at generation. The fresh-draft experiment worked not because
"fresh" is magic but because it dropped the maximum **and** drew from
abundance.

**Reasoning.** Locating the root cause at generation-time relocates the whole
corrective upstream. Rather than adding more repair machinery (a permanent
every-essay fresh-draft diagnostic), the highest-leverage fix is: never
impose a maximum; generate from abundance; calibrate the minimum descriptively.
This reframe is what demotes X.1 from "standard step" to "legacy fallback"
(see §3) and motivates the front-end gather/plan phases (see §2.2).

---

## §2. The two-level architecture

The core proposal. The current doctrine (Stage 0 → Stage 5) is a
**per-artifact assembly line** — it operates on one essay/chapter/op-ed at a
time. But the decisions this workstream is about — what earns its place,
abundance-allocation, differentiation against siblings + the book — are
inherently **cross-artifact**. They cannot be made correctly inside any single
artifact's pipeline without re-creating the duplication problem. Therefore the
doctrine needs a second, higher level.

### §2.1 The Portfolio layer (NEW — standing, incremental)

A standing, lightweight layer that sits *above* the per-artifact pipeline and
feeds into it. Its deliverables:

- **Cross-corpus duplication matrix** — cases/citations/anchors on rows;
  artifacts (book chapters + essays + op-eds) on columns; each cell annotated
  by register (`canonical` / `load-bearing` / `illustrative` / `passing
  reference` / `thought-experiment`).
- **Per-artifact unique-contribution profile** — one paragraph per artifact:
  what this piece carries that no other piece carries; which target
  publisher's editorial brain it fits in a way no sibling does.
- **Allocation decisions** — per duplicated case, an explicit "earns its place
  in locations {A, B} because {register difference / load-bearing role /
  differentiation reason}; cut from {C} as non-load-bearing duplication."

**Critical property — it is a compressed map, not a megadocument.** The
portfolio layer is a few thousand tokens (matrix + profiles + decisions). It
does NOT require holding the full text of every artifact in one context.
Each per-artifact drafting session reads the *map*, not the siblings' prose.
Cross-artifact coherence is achieved through the shared map; drafting stays
per-artifact and parallelizes cleanly across chips (each chip = one artifact +
the small shared map).

**Reasoning.** (1) This resolves the context-limit objection that caused the
author to shelve the portfolio idea months ago: drafting-everything-at-once is
infeasible even at 1M tokens, but a *map* is cheap. The two ideas were
conflated; separating them unblocks the shelved one. (2) The author already
built the embryo: the 2026-05-08 migration of book-level guidance ("the book
needs living people," "within-chapter comparisons") *out* of per-chapter
GuidanceDocs *into* the single canonical `_BookLevelGuidance.md` is exactly
this instinct — some decisions don't belong to any single chapter. The
portfolio layer generalizes that move from the book to the whole corpus.
(3) It is the natural and only correct home for the differentiation framework
(handoff §3.3) and the cross-corpus inventory (handoff Phase 3).

**Lifecycle.** Built once now as a baseline (item 3 mechanical scan + item 4
editorial interpretation); updated *incrementally* whenever a new artifact
enters or a case is reallocated. It is the *durable* layer.

### §2.2 The Per-artifact pipeline (front-end rebuilt)

The existing per-artifact pipeline, with its front-end rebuilt around the
author's discuss-then-draft discipline. The sequence:

**gather → allocate → plan → generate → cut → cascade → calibrate**

- **Gather (abundance).** Two intelligence sweeps before any drafting:
  - *Publisher + audience intelligence* — who receives this, what their
    editorial brain wants (deepens existing Stage 1b + Amendment D
    reception-chain weighting into its own deliberate phase).
  - *Citation / adjacent-works harvest* — collect the public-domain quotes,
    adjacent scholarship, and citable material *available* to this piece. New
    to the doctrine. Anchored in the author's McDowell/Chesapeake insight: the
    book unblocked when fieldwork turned scarcity into surplus — "more citable
    work than we could ever fit." **Abundance is the precondition for good
    prose, not a nice-to-have.** Harvested material runs through the two-state
    fabrication gate (§5).
- **Allocate (coarse, pre-draft cut).** With the portfolio map in hand, decide
  which *cases/topics* belong to this piece at all — and which it consciously
  leaves to siblings. This is the *coarse* cut: scope, not sentences.
- **Plan (discuss-then-draft).** Interactive author+Claude conversation:
  what's the right piece for this venue, what's available, what it would take
  to land. Output is a durable **drafting-plan artifact** (§4), not just a
  conversation.
- **Generate.** Prose drafting with a **minimum target anchored to the venue's
  natural length and NO maximum mentioned.** The drafter writes each allocated
  element *fully*.
- **Cut (fine, post-draft).** Within the generated prose, cut what doesn't
  earn its place — the author's canonical write-long-then-cut discipline,
  operating at sentence/paragraph grain. (This is the existing Stage 2.5
  editorial-cut idea, X.3.)
- **Cascade.** Existing Stage 3 (five-pass rigor) → Stage 4 (render +
  character-integrity) → Stage 5 (sign-off + pre-pub queue), unchanged.
- **Calibrate.** After generation, record actual length vs. the stated
  minimum; feed the running tally back into future minimum *suggestions*
  (descriptive, not prescriptive — §6).

**Reasoning — two cuts at two grains.** The author's write-long-then-cut
discipline is canonical and the fresh-draft experiment confirmed it holds for
Claude too. The reorg adds a *second, coarser* cut *before* drafting (allocate)
that the post-draft cut cannot do: deciding which cases even belong here.
Without it, every essay re-decides scope in isolation and the duplication
problem returns. With it, the drafter never has to compress to fit, because
*which ideas* is settled before prose starts — the post-draft cut then trims
fat *within* the right scope, never amputating substance to hit a number.

---

## §3. Re-sorting X.1–X.6 into the two homes

Once the two levels exist, the six handoff amendments stop being a flat list
and fall out as consequences. The re-sort:

| Amendment | Original framing | New home | Disposition |
|---|---|---|---|
| **X.1** Fresh-start Stage 2 alternate | "Standard pre-Stage-5 step for any cascade-worked essay" | Per-artifact pipeline | **Demoted to legacy fallback.** With min-only generation from abundance as the default (§1, §2.2), the fresh-draft diagnostic is no longer an every-essay step. It runs *once* on essays drafted under the old max-length regime, as a bounded diagnostic with a stopping rule (feeds a finite spot-fix list, then the gate closes — not "iterate until no new structural moves appear"). |
| **X.2** Brief §5 voice register update | Corpus-wide brief template change | Per-artifact pipeline (Plan phase) + brief template | **Adopted.** The author's prose-craft discipline becomes brief §5 template language (exact text is open decision §7-3). Also embodied in the Generate phase's min-only/no-max rule. |
| **X.3** Stage 2.5 editorial-cut step | New stage between Stage 2 and Stage 3 | Per-artifact pipeline (Cut phase) | **Adopted, renamed.** This is the "fine, post-draft cut" in §2.2. Confirmed as the author's canonical write-long-then-cut discipline at sentence/paragraph grain. |
| **X.4** Cost-constraint-removal default reset | Standalone session-discipline memory | Memory layer (`tools/memory/`) | **Adopted as a standalone memory entry**, independent of the two-level reorg. Addresses handoff Lesson 1 (resource-conservation reverting to minimum-discipline defaults under cost-removed framing). Relocate the baseline entirely; don't expand marginally. |
| **X.5** Cascade substrate-question gate | New gate at Pass 3.5 or Stage 5 | Per-artifact pipeline + Portfolio layer | **Adopted, reframed.** "Is this the right essay?" is now answered up front by the Allocate + Plan phases (consulting the portfolio map), not bolted onto the cascade. The legacy X.1 fresh-draft fallback operationalizes it for old-regime essays. |
| **X.6** Bidirectional brief↔essay update flow | New brief-amendment trigger | Per-artifact pipeline + Portfolio layer | **Adopted, widened.** Pass 3.1 fact-corrections already propagate forward to brief §7. Extend the same to §5 voice register and §4 structural decisions. AND: essay-level structural lessons propagate *up* to the portfolio layer (e.g., a case discovered to be load-bearing here updates the allocation matrix). |

**Reasoning.** The re-sort is not cosmetic. It reveals that X.1 and X.5 were
both *symptoms* of the missing portfolio layer + the max-length root cause —
once those are fixed, X.1 demotes and X.5 relocates to the front-end. X.2 and
X.3 are the prose-craft discipline made structural. X.4 is genuinely
orthogonal (a session-discipline memory) and stays standalone. X.6 is the
update-flow glue that keeps both levels from going stale.

---

## §4. The drafting-plan artifact (successor to the GuidanceDoc)

The per-chapter GuidanceDocs (`manuscript/chapters/archive/Chapter__*___GuidanceDoc.md`)
were the right *instinct* — they carried scope, "what lives here" source
material, key analytical points, citations, counterargument inventory, and
register/handling notes. Reading Ch 4's GuidanceDoc on 2026-06-02 shows
exactly why they decayed, and the fixes are specific:

**Four failure modes observed, four fixes:**

1. **Mixed five distinct things in one file** (abundance, scope decision,
   citations, counterarguments, register notes, all interleaved). → **Fix:**
   clearly-sectioned parts.
2. **Accreted forever with no expiry** (giant 2026-05-08 staleness-audit
   tables; retired vocabulary; "[MIGRATED]" / "[DUPLICATE]" scar tissue). →
   **Fix:** regenerated fresh per drafting cycle and cleanly superseded — the
   plan is *disposable scaffolding* for one drafting pass; the portfolio map
   is the durable layer.
3. **No separation between "available" and "decided"** ("what lives here" raw
   material sat next to "the key analytical point" decisions). → **Fix:** the
   two-state source pool (§5) separates the tentative pool from confirmed
   commitments.
4. **No upward pointer** (each chapter re-decided in isolation; the
   `_BookLevelGuidance.md` migration was a manual after-the-fact fix). →
   **Fix:** the Allocation & scope section consults and points up to the
   portfolio map.

**Proposed structure of the drafting-plan artifact (per artifact, per cycle):**

- **§ Source pool** — tentative→confirmed citations with provenance (§5).
- **§ Allocation & scope** — what this piece is about; which cases it carries;
  what it consciously leaves to siblings (consults the portfolio map).
- **§ What-lands plan** — audience/publisher fit + the "what it would take to
  land" editorial output from the Plan-phase discussion, made durable.
- **§ Counterarguments to pre-empt** — the Ch 4 objection-inventory move,
  which was demonstrably valuable.
- **§ Register / handling notes** — voice register, content-type sub-protocol
  notes.

**Reasoning.** The GuidanceDoc concept was sound; it failed on lifecycle and
on the available-vs-decided conflation. Making the plan disposable (regenerated
per cycle) and pushing durable cross-artifact decisions up to the portfolio
layer fixes the staleness rot at its source. This artifact is also what makes
the discuss-then-draft conversation portable (handoff Lesson 6/7): the
generation chip drafts *from* it, and the next session can *see* it.

---

## §5. Two-state citation model + fabrication gate

Harvested abundance is exactly where invented material would enter
publisher-facing prose (fabricated quotes, misattributed sources, wrong
dates). The empirical scars are real: the Noema Pou/Pooh etymology drift, the
GPFG founding-date drift, the Ch 2 → Harper's near-miss. The hard
no-invented-claims rule
(`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`)
governs.

**The two-state model (author-specified 2026-06-02):**

- **TENTATIVE inclusion** — harvested material is *researched + source-validated
  + saved with provenance attached*. The tentative pool is allowed to overflow
  on purpose (abundance). Nothing enters the pool without a real, traceable
  source.
- **CONFIRMED inclusion** — promoted from tentative *only when it actually
  lands in the final version.* Confirmation is the act of earning a place.

**Reasoning.** Catching fabrication at harvest is far cheaper than catching it
at Pass 3.1 after it is load-bearing in prose. Attaching provenance at the
tentative stage means nothing can graduate to confirmed without a real source
behind it — the fabrication gate is *built into* the gather phase, not a later
rigor pass. This also operationalizes the abundance discipline cleanly: the
overflow lives in the tentative pool; the cut decisions (allocate + post-draft)
determine what gets confirmed.

---

## §6. Length calibration discipline (descriptive, not prescriptive)

**The discipline (author-specified 2026-06-02):** discuss a minimum target
anchored to the venue's natural length → pick it → keep a running tally of
*actual generated length vs. the stated minimum* → let the tally inform future
minimum *suggestions*. (Empirical observation to verify: generation has been
running ~50–70% over the stated minimum.)

**Reasoning.** It is easier to cut fat than to add real substance after
drafting — the rationale for write-long-then-cut. The trap to avoid: observing
the overage and then *lowering minimums to compensate* smuggles length-targeting
back in through the side door. So the tally is used **descriptively** — as an
after-the-fact sanity band ("a fully-developed piece for this venue
historically runs N words; this one is way under, is it actually complete?") —
and to guide *our* choice of a realistic floor. The number handed to the
drafter stays venue-anchored; the tally is descriptive input to that choice,
never a target the drafter optimizes toward.

**Next step (mechanical, deferred):** measure actual word counts of existing
essays/op-eds against their brief minimums to test whether the ~50–70%-over
pattern is real and consistent or varies by length-band. This produces the
first calibration data points.

---

## §7. Open decisions still needing author ratification

These are deliberately NOT decided in this PROPOSED artifact. They were the
five §8 inputs from the handoff; input 1 was answered "decide per-amendment as
we go" (2026-06-02). The rest remain open:

1. **Codification container.** Is this two-level reorg "Amendment E" to
   doctrine v1.0.0, or a structurally distinct revision? Recommendation
   pending the substance settling, per "decide as we go." The Amendment D
   pattern (one canonical location + cross-references in sister files) is the
   reference.
2. **Differentiation criteria + cut threshold.** What makes an essay earn its
   place vs. duplicate the book + siblings? What is the cut threshold for
   cross-essay duplications? (handoff §3.3 — feeds the portfolio layer.)
3. **Brief §5 voice-register exact text.** The discipline is articulated
   ("write long with detail, then cut what doesn't directly support"; "fewer
   ideas written fully over more ideas compressed densely"; "separate
   writing-energy from editorial-judgment"). The exact template text is open.
4. **Corpus-wide audit scope.** All essays + op-eds + book + tech appendix? Or
   essays + op-eds only? Or essays only? (Affects the item-3 mechanical scan;
   cost is author-attention, not tokens.)
5. **Atlantic Ideas editorial cut/focus timing.** Suggested: AFTER the
   differentiation framework is settled, since Atlantic Ideas cut decisions
   depend on knowing what is in the other essays. Author confirmation needed.

---

## §8. Consolidated change table (change → reasoning)

| # | Change | Reasoning |
|---|---|---|
| 1 | Reframe compression as a generation-time (max-length) failure, not a rigor failure | Relocates the corrective upstream; motivates min-only generation and demotes the fresh-draft diagnostic from permanent step to legacy fallback |
| 2 | Add a standing **Portfolio layer** (duplication matrix + unique-contribution profiles + allocation decisions) above the per-artifact pipeline | Cross-artifact decisions can't be made correctly inside a single artifact's pipeline; a compressed *map* gives coherence without holding all text in one context; generalizes the existing `_BookLevelGuidance.md` migration instinct corpus-wide |
| 3 | Rebuild the per-artifact front-end as **gather → allocate → plan → generate → cut → cascade → calibrate** | Encodes the author's discuss-then-draft discipline; abundance precedes drafting; two cuts at two grains (coarse pre-draft scope; fine post-draft fat) |
| 4 | **Min-only generation, no maximum** | Max-length manufactured compression; venue-anchored floor + abundance lets the drafter write each element fully |
| 5 | Re-sort X.1–X.6 into the two homes (X.1 demoted to legacy fallback; X.2/X.3 prose-craft made structural; X.4 standalone memory; X.5 relocated to front-end; X.6 widened to bidirectional incl. portfolio) | Once the two levels exist, four of the six amendments are consequences; the re-sort reveals X.1/X.5 were symptoms of the missing layer + max-length root cause |
| 6 | Replace per-chapter GuidanceDocs with a **disposable, sectioned drafting-plan artifact** that points up to the portfolio map | Fixes the four observed GuidanceDoc failure modes (mixing, accretion, no available-vs-decided split, no upward pointer); makes discuss-then-draft portable |
| 7 | **Two-state citation model** (tentative w/ provenance → confirmed on landing) + fabrication gate built into the gather phase | Harvest is where fabrication enters; catching it at harvest is far cheaper than at Pass 3.1; provenance-at-tentative enforces the hard no-invented-claims rule |
| 8 | **Length calibration discipline** — running actual-vs-minimum tally used descriptively, never as a target | Cutting fat beats adding substance; but lowering minimums to match observed overage would re-smuggle length-targeting; tally guides *our* floor choice, not the drafter's optimization |

---

## §9. Cross-references

- Handoff (orientation): `tools/workstream-handoffs/pipeline-prose-revision-and-corpus-wide-audit-handoff_2026-06-01.md`
- Current doctrine: `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`
- Amendment D codification reference pattern: `tools/drafting-templates/audience-pressure-test-construction.md`
- GuidanceDoc proto-artifacts: `manuscript/chapters/archive/Chapter__*___GuidanceDoc.md`
- Portfolio-layer embryo: `manuscript/chapters/_BookLevelGuidance.md`
- No-invented-claims hard rule: `tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`
- Token-cost-not-a-constraint (cost is author-attention): `tools/memory/feedback_token_cost_not_a_constraint.md`
- Brief template (corpus-wide): `tools/drafting-templates/stage-1-audience-aware-structure-pass.md`

---

*End of pipeline doctrine two-level reorganization, PROPOSED 2026-06-02.
Internal scaffolding. Awaits author ratification of the §7 open decisions
before becoming doctrine v-next. Merge-on-ratification per CLAUDE.md (this
PROPOSED artifact merges to origin/main at author direction per the session
2026-06-02; ratification of the §7 decisions is a separate gate).*
