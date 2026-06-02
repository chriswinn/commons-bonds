---
artifact: Pipeline doctrine two-level reorganization — PROPOSED
date: 2026-06-02
session_of_origin: claude/pipeline-prose-revision-corpus-audit-260602-6b5eda
status: RATIFIED 2026-06-02 — framework ratified by author ("I think this is good. go ahead and write the changes"); codified as Amendment E to commons_bonds_pipeline_doctrine_v1.0.0.md §14 + brief-template update + standalone X.4 memory entry. This artifact is the canonical DETAILED SPEC; §14 is the summary + pointer. The §7 items marked DEFERRED below remain open downstream-work decisions (not framework gaps).
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

**Differentiation has TWO axes, not one** (sibling-session addition,
2026-06-02). "Differentiation" was being treated as a single concept. It is
actually two distinct axes, each needing its own criteria, and a piece must
clear *both*:

- **Internal-corpus differentiation** — what does this artifact carry that no
  other Winn essay or book chapter carries? Answered by the cross-corpus
  duplication matrix above. Lives in the Portfolio layer.
- **External-field differentiation** — what does this artifact say that the
  broader discourse / field does not already say? The unique contribution
  against everything else that exists on the topic in the world. NOT answered
  by the internal matrix; an essay can be internally-unique-vs-siblings while
  being externally-redundant-with-the-field ("Winn restates Christophers in
  his own voice"). Needs a per-essay positioning artifact at
  `publishing/essays/<essay>/research/differential-positioning.md`.

**Reasoning + dependency.** The external axis is not a free-standing research
effort — it *consumes the Gather phase's adjacent-works harvest* (§2.2). The
citation/adjacent-works sweep is already happening and is already
fabrication-gated (§5); the positioning artifact repurposes that validated
material to articulate "here is what the field already says; here is what this
piece adds." Wiring the external axis to the Gather harvest makes it cheap and
keeps both axes honest: the matrix stops same-voice duplication *inside* the
corpus; the positioning artifact stops same-claim duplication *against* the
field.

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

**gather → [material-readiness gate] → allocate → plan → generate → cut → cascade → calibrate**

- **Gather (abundance).** Two intelligence sweeps before any drafting:
  - *Publisher + audience intelligence* — who receives this, what their
    editorial brain wants (deepens existing Stage 1b + Amendment D
    reception-chain weighting into its own deliberate phase).
  - *Citation / adjacent-works harvest* — operates in three layers:
    - **(1) Collect what exists, broadly.** Public-domain quotes, adjacent
      scholarship, on-record interviews, and other material citable under fair
      use *available* to this piece. Abundance-first — do NOT pre-filter to
      "only what this piece needs," which would narrow the harvest and defeat
      the abundance principle. Collecting what exists is valuable in its own
      right: during information-gathering it **maps what has already been said
      on the subject**, and that map is what reveals **what has not been said
      yet** — i.e., it is the direct input to the external-field
      differentiation axis (§2.1, `differential-positioning.md`). You cannot
      credibly claim the unsaid without first surveying the said.
    - **(2) Goal-directed overlay.** As material is collected, keep an ear open
      for — and tag — the subset that specifically *accomplishes what this
      piece needs to land* (supplies the analytical anchor, the counterargument
      source, the human face, etc.).
    - **(3) Outstanding-needs note.** Record which landing-requirements existing
      fair-use material already satisfies, and which remain **outstanding /
      still needed.** This note is what the material-readiness gate consumes.

    New to the doctrine. Anchored in the author's McDowell/Chesapeake insight:
    the book unblocked not by funding travel to extraction sites for original
    quotes, but by *recognizing* that an overabundance of public works +
    on-record interviews was already citable under fair use — "more citable
    work than we could ever fit." The gap was **research/recognition, not
    fieldwork.** **Abundance is the precondition for good prose, not a
    nice-to-have.** Harvested material runs through the two-state fabrication
    gate (§5).
- **Material-readiness gate (between Gather and Allocate).** Before allocating,
  an explicit verdict on whether there is enough material to brief this piece
  (sibling-session addition, 2026-06-02). Three verdicts:
  - `READY-TO-ALLOCATE` — **the common, default outcome.** Most
    essays/chapters/op-eds land cleanly with no fieldwork. Reached by any of
    three routes:
    - **(i) No external citations needed at all** *(distinct callout)*. The
      piece's argument stands on its own reasoning / the author's framework and
      requires no external sourcing to land. Fieldwork question never arises.
    - **(ii) Sufficient fair-use material already exists** — the harvest pool
      and the outstanding-needs note (Gather layer 3) show every landing-
      requirement is met by existing citable material.
    - **(iii) Explicit thought-experiment / theoretical register** — the
      subject is future, counterfactual, or theoretical, so no real
      interviewable subject exists or *can* exist (the asteroid-miner in Aeon
      *Mask of Abundance* + book Ch 7; the $100-barrel sections). The "missing
      face" is not a fillable gap; the theoretical analysis **is** the
      contribution (it is where the CIT + the framework were established —
      arguably among the author's biggest contributions). **Guardrail:** this
      route is legitimate ONLY under the no-invented-claims hard rule's narrow
      exception — the theoretical register must be **explicitly signaled in the
      prose** (the Ch 7 *On Other Worlds* model), and a fictional subject must
      **never** be rendered with invented biographical detail presented as
      real. The absence of a real subject is honored openly, not invented away.
  - `NOT-READY-NEEDS-X` (X enumerated) — gaps remain; specify what closes them.
    **X requires a two-branch diagnosis before this verdict stands:**
    - **(a) Mis-diagnosed gap.** What looks like a material shortage is
      actually unrecognized abundance — fair-use public works, on-record
      interviews, adjacent scholarship already exist and were simply not yet
      recognized. Resolution: recognition, not acquisition. The true verdict
      is `READY-TO-ALLOCATE`.
    - **(b) Genuine gap.** There really are zero (or too few) citable published
      works/interviews; the material can only be acquired by real-world work —
      fieldwork, original interviews, site visits, travel. The gap is real and
      cannot be recognized away. Closing it triggers a **cost-justification
      decision** (see below) before any commitment.
    Do not proceed to Allocate until X closes (branch b) or is recognized as
    already-met (branch a).
  - `RECONSIDER` — the piece may be the wrong piece: different shape, different
    venue, deferred, or dropped from the queue. **This verdict IS the X.5
    substrate-question ("is this the right essay?") relocated to the
    front-end** (see §3 X.5) — the same judgment, now with a concrete verdict
    and a home rather than bolted onto the late cascade. **It is also where a
    genuine-gap (branch b) piece lands when the fieldwork is not worth it
    right now** (see cost-justification below).

  **Branch (b) first classifies the gap as blocking vs non-blocking:**
  - **Blocking gap** — the piece cannot land at all without the missing
    element. → run the cost-justification (below); close it via fieldwork or
    `RECONSIDER`.
  - **Non-blocking gap** — the piece lands as-is but *weaker* (worked example:
    it lands, but has no human *face* / personal story to carry it). → choose
    among the **four paths** below.

  **Cost-justification / EV decision.** When closing the gap requires
  real-world acquisition, the gate forces an explicit, portfolio-level
  **expected-value** decision: *does the value of closing the gap (materially
  better landing odds, a human face, a decisive source) justify the fieldwork
  cost + time, given everything else in the queue?* The binding cost is
  **real-world — author time, travel money, clock time — NOT tokens**
  (consistent with the ratified token-cost-not-a-constraint memory; the
  constraints that bind are attention + clock + real expense).

  **Four paths for a non-blocking gap:**
  1. **Ship as-is now.** The piece lands without the element; accept it is
     somewhat weaker. Verdict effectively `READY-TO-ALLOCATE`.
  2. **Postpone for fieldwork while prioritizing other work.** EV of the
     fieldwork is high enough to wait; verdict stays `NOT-READY-NEEDS-X` with a
     justified acquisition plan, but lower-priority than work whose material is
     in hand.
  3. **Ship now, upgrade in a later printing/version.** Ship without the
     element now; add it once fieldwork happens. Mirrors the ratified
     named-subject **upgrade-window** discipline (anonymize/omit now, restore
     later) — see `tools/memory/feedback_named_subject_consent.md`.
  4. **Reframe in explicit thought-experiment register.** When the gap is
     *structurally unfillable* because the subject is theoretical/future/
     counterfactual (no real subject exists or can exist — the asteroid-miner
     case), the "missing face" is a category error, not a gap. Reframe the
     piece to operate openly in theoretical register; the theoretical analysis
     is the contribution. **Same guardrail as `READY-TO-ALLOCATE` route (iii):
     explicit register signaling + no fabricated-as-real subject.**

  For a **blocking** gap the EV decision collapses to two outcomes: **worth
  it → commit the fieldwork** (verdict stays `NOT-READY-NEEDS-X` with a
  justified plan); **not worth it now → `RECONSIDER` / postpone** for
  higher-priority work. Not a verdict that the piece is bad — it may re-enter
  the queue when priorities or resources shift.

  *Empirical anchors (corrected 2026-06-02).* Branch (a): the McDowell County /
  Chesapeake Bay moment — the book *appeared* blocked in `NOT-READY-NEEDS-X`
  where X was mistaken for "funding to travel to extraction sites and get
  usable quotes." Stepping back revealed an overabundance of public works +
  on-record interviews already citable under fair use; the actual gap was
  **research/recognition, not fieldwork or funding**, and the true verdict was
  already `READY-TO-ALLOCATE`. The gate's highest-value function is forcing the
  question "is X genuinely missing, or do we simply not yet recognize the
  abundance that already exists?" Branch (b): a piece for which no published or
  on-record material exists — the gate must NOT hand-wave the gap away; it must
  classify blocking vs non-blocking and run the EV decision. Thought-experiment
  route (READY route iii / non-blocking path 4): the asteroid-miner in Aeon
  *Mask of Abundance* + book Ch 7 + the $100-barrel sections — no asteroid
  miners exist, so no interview is possible *or needed*; the theoretical
  analysis is where the CIT + framework were established. The gate must
  recognize this as `READY`, not chase an impossible interview — under the
  explicit-register + no-fabrication guardrail. The current pipeline handles
  readiness implicitly (the brief just doesn't get written until someone feels
  ready); the explicit gate makes the state, the branch-(a)-vs-(b) diagnosis of
  X, the blocking/non-blocking classification, and the EV/cost-justification
  all visible + auditable.

  *Location (refinement):* defaults to a **preface section of the
  drafting-plan artifact** (§4, under "Allocation & scope"). Promote to a
  standalone `material-readiness.md` only when a piece's readiness has real
  deliberation history worth tracking separately (the McDowell case would have
  earned its own file; most pieces will not).

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
| **X.6** Bidirectional brief↔essay update flow | New brief-amendment trigger | Per-artifact pipeline + Portfolio layer | **Adopted, widened — has its own sub-cascade (see §3.1).** Pass 3.1 fact-corrections already propagate forward to brief §7. Extend the same to §5 voice register and §4 structural decisions. AND: essay-level structural lessons propagate *up* to the portfolio layer (a case discovered load-bearing here updates the allocation matrix). AND: essay-side → book-side propagation (a sharper essay formulation amending the chapter) is a six-step sub-cascade gated by a hard threshold — §3.1. |

**Reasoning.** The re-sort is not cosmetic. It reveals that X.1 and X.5 were
both *symptoms* of the missing portfolio layer + the max-length root cause —
once those are fixed, X.1 demotes and X.5 relocates to the front-end. X.2 and
X.3 are the prose-craft discipline made structural. X.4 is genuinely
orthogonal (a session-discipline memory) and stays standalone. X.6 is the
update-flow glue that keeps both levels from going stale.

### §3.1 X.6 essay→book sub-cascade (sibling-session addition, 2026-06-02)

The X.6 widening understated the operational complexity of *essay-side →
book-side* propagation (a sharper essay formulation amending the chapter it
derived from). It is a workflow of its own:

1. **Identification.** A pass flags "this essay-side formulation is sharper
   than the book's." *Trigger location: the Cut phase* (§2.2 fine post-draft
   cut) — earlier and more general than Pass 3.5, which is late and
   restoration-polarity. *Worked example:* the Atlantic Ideas fresh draft
   surfaced a cost-of-mis-classification asymmetry paragraph (§Classify)
   sharper than Ch 9's current treatment of the same logic.
2. **Candidate capture.** Write to a living `book-amendment-candidates.md`
   that **batches** candidates. The full cascade fires when a batch is worked,
   NOT per-candidate.
3. **Book-side amendment cycle.** Apply the sharpening via a Phase C amendment.
4. **Cross-chapter coherence check.** Does the sharpening affect adjacent
   chapters? (Ch 9's asymmetry might also touch Ch 6 or Ch 8.)
5. **Brief refresh.** If the sharpening changes any §7 canonical fact-anchor,
   update the relevant essay brief(s).
6. **Sibling-essay cascade.** If other essays cite the book's older
   formulation, align them.

**The threshold is THE gate, not a footnote.** Propagate to the book only if
**(a)** the formulation makes a load-bearing claim more rigorous OR more
clearly expressed, AND **(b)** the book's current treatment does not already
convey what the sharpening adds, AND **(c)** propagation does not break
cross-chapter coherence. Without this gate, every sharp essay-side phrasing
triggers a book-amendment cycle and the sub-cascade fires constantly.

**Class-boundary flag (load-bearing).** Step 3 touches
`manuscript/chapters/` — that is **end-user-facing prose**, governed by
**merge-on-*ratification***, NOT the auto-merge that governs this
internal-scaffolding artifact. The sub-cascade *crosses a content-class
boundary at step 3*; the doctrine must say so explicitly, or a session will
auto-merge a chapter change that requires author ratification.

**Reasoning.** The six steps are real, but this is the item most at risk of
becoming heavyweight process. Batching (step 2) + the hard threshold + the
Cut-phase trigger keep it disciplined; the class-boundary flag keeps it safe.

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
  what it consciously leaves to siblings (consults the portfolio map). Opens
  with the **material-readiness verdict** (§2.2 gate: `READY-TO-ALLOCATE` /
  `NOT-READY-NEEDS-X` / `RECONSIDER`) as a preface, before allocation
  decisions.
- **§ Differential positioning (pointer)** — links to
  `publishing/essays/<essay>/research/differential-positioning.md` (the
  external-field axis, §2.1) so the drafting plan reflects both
  differentiation axes.
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

### §6.1 Per-venue submission-norms artifact (sibling-session addition, 2026-06-02)

Min-only generation removes venue length constraints from the *drafter*, but
venue submission norms still exist and still need to inform the Cut phase
(§2.2) and Stage 5 sign-off ("does this fit the venue's submission norms?").
Once relocated out of the per-essay brief (§10), those norms need a home.

**Location:** a per-venue artifact at
`publishing/venues/<venue>/submission-norms.md`.

**CONTAMINATION FIREWALL (author correction 2026-06-02 — load-bearing).** A
venue's stated norms include a **maximum** (e.g., Atlantic Ideas 3,000–6,000w —
the 6,000 is a ceiling). The entire point of min-only generation is that the
drafter NEVER sees a maximum. Therefore the venue artifact MUST be internally
partitioned, and the generation-prompt assembly must draw ONLY from the
drafter-safe partition:

- **Drafter-safe block** (may be surfaced to the drafter):
  - Editorial-brain map — the current brief §2, **moved up to venue level**
    since it is venue-property, not essay-property.
  - Format requirements that carry no length ceiling (markdown / Word / PDF;
    em-dash vs ASCII; etc.).
  - The venue-anchored **minimum** floor only.
- **Editorial-only block** (consulted ONLY by the Cut phase + Stage 5, AFTER
  generation; NEVER injected into the generation prompt):
  - The stated **maximum** / ceiling and any section-fit upper bounds.
  - The §6 descriptive **calibration band** ("a fully-developed piece for this
    venue historically runs N words").

The maximum is a real submission constraint — Cut + Stage 5 must respect it —
but it lives behind the firewall. **The brief's pointer to the venue artifact
(§7-3 brief-template change) resolves to the drafter-safe block for generation,
and to the full artifact only for the post-generation editorial phases.** If a
pointer ever lets the maximum reach the drafter, the contamination that
manufactured compression in the first place (§1) is reintroduced.

**Reasoning.** Venue norms are properties of the venue, not of any specific
piece. Embedding them in per-essay briefs duplicates the same information
across every essay targeting that venue (Atlantic Ideas norms would appear in
the Pricing-Honestly brief AND any future Atlantic Ideas essay brief). A
per-venue artifact is one source of truth. Consequence for the brief template:
brief §2 (editorial brain) and the §10 *minimum* stop duplicating and instead
*point to the drafter-safe block* of the venue artifact — a concrete
brief-template change that feeds open decision §7-3. The §10 *maximum* does NOT
move into the generation-facing brief at all; it lives only in the
editorial-only block, consulted by the Cut phase + Stage 5 after generation.
The drafter never receives the venue artifact's editorial-only block, and
therefore never sees a maximum.

---

## §7. Open decisions still needing author ratification

Status as of 2026-06-02: decisions **1, 2, 3, 4 SETTLED**; decision **5
DEFERRED** (Atlantic cut/focus timing — fires after the test-run verification).

**§7-test-gate (author direction 2026-06-02).** Before any cross-corpus audit
execution or multi-essay generation rollout, VERIFY the core hypothesis on
Atlantic Ideas: did removing the maximum-length parameter + applying the §5
prose-craft discipline produce **smoother prose without contamination** (full
length AND low em-dash-crutch density AND no fabrication/drift)? The 2026-06-01
fresh draft is NOT a fair test — it predates the §5 discipline and ran 8.3
em-dashes/1k-words (vs Locked's 2.1). The test run uses the new-pipeline prompt.
Differentiation-criteria *execution* (matrix + profiles) and the rollout are
gated behind a passing verification.

1. **Codification container — SETTLED 2026-06-02.** Split-by-natural-home: the
   two-level architecture is **Amendment E** to doctrine v1.0.0 (codified at
   §14 as summary + pointer; THIS artifact is the canonical detailed spec,
   mirroring the Amendment D pattern). X.4 → standalone memory entry
   (`tools/memory/feedback_cost_constraint_removal_default_reset.md`). §5 voice
   register + venue-pointer → brief-template update
   (`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`).
2. **Differentiation criteria + cut threshold — RATIFIED 2026-06-02.** Two
   axes (§2.1); a case/claim must clear BOTH.
   - **Axis A — internal-corpus.** Three tests per case per location: (1)
     *load-bearing* (does the argument collapse/weaken if removed?); (2)
     *functional-role/register* (what work does it do here — establish-concept
     / illustrate / thought-experiment-stress-test / policy-mechanism / hook —
     and in what register?); (3) *redundancy* (does it do the SAME work, same
     register, as another location?). **Cut dial (author-set 2026-06-02):**
     cut a case from a location ONLY when it does the **same work, in the same
     register, and is non-load-bearing there.** Different work / load-bearing /
     distinct register → KEEP. **Recognizable authorial voice is a FEATURE, not
     a cut criterion** — you want the corpus recognizably the author's; the
     asteroid-miner (Ch 7 thought-experiment-establishing-CIT vs Aeon
     mask-of-abundance illustration vs Atlantic policy-mechanism) earns all
     three homes precisely because it does different work in each. Book is the
     provisional canonical home (deferred from audit per §7-4); essays must
     differentiate or carry as load-bearing.
   - **Axis B — external-field.** (1) *novel-move* (name what this piece
     asserts/reframes that the field comps don't carry); (2) *restatement guard*
     (strip the author's voice — is the substantive claim already made, with no
     new analytical move? → externally redundant). Contribution must be ≥1 of:
     (a) new framework/concept, (b) novel cross-tradition synthesis, (c) new
     case/data, (d) novel application. (e) fresh-voiced-restatement alone does
     NOT earn a venue.
   - **Output:** per-artifact unique-contribution profile + per-case
     earned-presence decision (Portfolio layer). The cross-corpus *execution*
     of these criteria (the matrix + profiles) is downstream work, gated behind
     verifying the pipeline produces better prose (see §7-test-gate).
3. **Brief §5 voice-register + brief-template pointer changes — SETTLED +
   APPLIED 2026-06-02.** The prose-craft discipline is now written into the
   brief template §5 ("write long with detail, then cut what doesn't directly
   support"; "fewer ideas written fully over more ideas compressed densely";
   "separate writing-energy from editorial-judgment"). The brief-template
   changes are applied: the `Length:` field now carries a MINIMUM FLOOR only
   (the HARD CEILING removed — it was the literal contamination vector); §2 +
   the §10 minimum point to the **drafter-safe block** of
   `publishing/venues/<venue>/submission-norms.md`; the maximum stays behind
   the firewall (§6.1). (Full front-end restructure of the template to the
   gather→gate→allocate→plan→generate shape remains a larger follow-on.)
4. **Corpus-wide audit scope — SETTLED 2026-06-02.** Generation scope = essays
   + op-eds (the book is content-complete; not re-drafted now). Near-term audit
   scope = essays + op-eds (so they don't duplicate *each other*). Book
   chapters + tech appendix are **DEFERRED — TBD on essay/op-ed results**: if
   the new pipeline produces better prose, chapters may be re-drafted through it
   and brought into the audit then. Caveat: without the book in the audit, a
   case's "canonical home" is *provisional* (flag "also in Ch X" without
   resolving cross-book allocation).
5. **Atlantic Ideas editorial cut/focus timing — DEFERRED (downstream work).**
   Suggested: AFTER the differentiation framework is settled, since Atlantic
   Ideas cut decisions depend on knowing what is in the other essays. Author
   confirmation needed when that session is scheduled.

---

## §8. Consolidated change table (change → reasoning)

| # | Change | Reasoning |
|---|---|---|
| 1 | Reframe compression as a generation-time (max-length) failure, not a rigor failure | Relocates the corrective upstream; motivates min-only generation and demotes the fresh-draft diagnostic from permanent step to legacy fallback |
| 2 | Add a standing **Portfolio layer** (duplication matrix + unique-contribution profiles + allocation decisions) above the per-artifact pipeline | Cross-artifact decisions can't be made correctly inside a single artifact's pipeline; a compressed *map* gives coherence without holding all text in one context; generalizes the existing `_BookLevelGuidance.md` migration instinct corpus-wide |
| 3 | Rebuild the per-artifact front-end as **gather → [material-readiness gate] → allocate → plan → generate → cut → cascade → calibrate**. Gather's harvest is **three-layer**: (1) collect-what-exists broadly (abundance + field-map of what's already said), (2) goal-directed overlay (tag what accomplishes landing), (3) outstanding-needs note (what the gate consumes) | Encodes the author's discuss-then-draft discipline; abundance precedes drafting; broad collection maps the said → reveals the unsaid (feeds external differentiation, row 9); two cuts at two grains (coarse pre-draft scope; fine post-draft fat) |
| 4 | **Min-only generation, no maximum** | Max-length manufactured compression; venue-anchored floor + abundance lets the drafter write each element fully |
| 5 | Re-sort X.1–X.6 into the two homes (X.1 demoted to legacy fallback; X.2/X.3 prose-craft made structural; X.4 standalone memory; X.5 relocated to front-end; X.6 widened to bidirectional incl. portfolio) | Once the two levels exist, four of the six amendments are consequences; the re-sort reveals X.1/X.5 were symptoms of the missing layer + max-length root cause |
| 6 | Replace per-chapter GuidanceDocs with a **disposable, sectioned drafting-plan artifact** that points up to the portfolio map | Fixes the four observed GuidanceDoc failure modes (mixing, accretion, no available-vs-decided split, no upward pointer); makes discuss-then-draft portable |
| 7 | **Two-state citation model** (tentative w/ provenance → confirmed on landing) + fabrication gate built into the gather phase | Harvest is where fabrication enters; catching it at harvest is far cheaper than at Pass 3.1; provenance-at-tentative enforces the hard no-invented-claims rule |
| 8 | **Length calibration discipline** — running actual-vs-minimum tally used descriptively, never as a target | Cutting fat beats adding substance; but lowering minimums to match observed overage would re-smuggle length-targeting; tally guides *our* floor choice, not the drafter's optimization |
| 9 | **Two differentiation axes** (§2.1) — internal-corpus (matrix) + external-field (`differential-positioning.md`, fed by Gather harvest layer 1's field-map of what's already been said) | A piece can be internally-unique-vs-siblings yet externally-redundant-with-the-field ("restates Christophers in his own voice"); both axes must clear the bar; external axis reuses the already-harvested, fabrication-gated adjacent works — you cannot claim the unsaid without first surveying the said |
| 10 | **Material-readiness gate** (§2.2) — `READY-TO-ALLOCATE` (common, default) / `NOT-READY-NEEDS-X` / `RECONSIDER`; READY has 3 routes incl. a distinct no-citations callout + a thought-experiment route; `NOT-READY-NEEDS-X` = two-branch diagnosis + blocking/non-blocking + EV decision | Makes readiness visible + auditable. **Most pieces are simply `READY`** — no citations needed (i), or fair-use abundance exists (ii), or explicit thought-experiment register where no real subject exists/can-exist and the theory IS the contribution (iii; asteroid-miner/$100-barrel/Ch7/Aeon; guardrail: explicit register + no fabricated-as-real subject). `NOT-READY-NEEDS-X` diagnoses **(a) mis-diagnosed** (unrecognized fair-use abundance → really READY; McDowell catch) vs **(b) genuine gap**; (b) classifies blocking vs non-blocking and runs an EV decision (value of closing the gap vs real-world cost — time/travel/clock, NOT tokens). Non-blocking → 4 paths: ship-as-is / postpone-for-fieldwork / ship-now-upgrade-later (consent upgrade-window) / reframe-as-thought-experiment. Defaults to a drafting-plan preface |
| 11 | **X.6 essay→book sub-cascade** (§3.1) — 6 steps, batched via `book-amendment-candidates.md`, hard (a)+(b)+(c) threshold, Cut-phase trigger, class-boundary flag at step 3 | Essay→book propagation is a workflow, not a line item; threshold + batching prevent constant firing; step 3 crosses into end-user-facing prose (merge-on-ratification), which the doctrine must flag or a session auto-merges a chapter change |
| 12 | **Per-venue submission-norms artifact** (§6.1) at `publishing/venues/<venue>/submission-norms.md`, **partitioned by a contamination firewall** — drafter-safe block (editorial brain, format, minimum) vs editorial-only block (maximum, calibration band) | Venue norms are venue-property not essay-property (one source of truth, no per-essay duplication); BUT the artifact contains a maximum, and pointing the drafter at it would re-contaminate generation with a ceiling (§1) — so generation draws only from the drafter-safe block; Cut + Stage 5 consult the editorial-only block after generation |

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
- Sibling session (source of the four 2026-06-02 additions §2.1 two-axis, §2.2 readiness gate, §3.1 essay→book sub-cascade, §6.1 per-venue norms): branch `claude/atlantic-ideas-package-ratification-260601-e8593b`
- Atlantic Ideas tree (empirical anchor for the additions; fresh draft surfaced the §3.1 cost-of-mis-classification worked example): `publishing/essays/atlantic-ideas-pricing-honestly/` + `_archive/fresh-stage-2-experiment_2026-06-01.md`

---

*End of pipeline doctrine two-level reorganization, RATIFIED 2026-06-02.
Internal scaffolding. This is the canonical detailed spec for Amendment E to
`commons_bonds_pipeline_doctrine_v1.0.0.md` (§14 = summary + pointer). §7
decisions 2/4/5 remain deferred downstream-work items (not framework gaps);
decision 1 (codification) + decision 3 (brief-template changes) are settled +
applied. Merge-on-ratification per CLAUDE.md.*
