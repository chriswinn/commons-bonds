# Commons Bonds — Session Handoff v1.49.0 — Parallel Execution Plan

**Date:** 2026-04-30
**Branch:** `claude/serene-franklin-1d85a7` (worktree); ratified-chunk fast-forwards to `origin/main` per Working Principle #9
**Purpose:** Organize the post-v1.48.0 OPEN work queue into parallel threads so multiple Claude sessions can run concurrently without colliding. v1.48.0 remains the canonical state-snapshot; this handoff is the **execution plan** layered on top.

**Read this file PLUS:**
- `alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md` — full state-snapshot (what landed; current insights)
- The thread-specific block (§3.α, §3.β, §3.γ, or §3.δ) for the work that session will pick up

---

## §1. Self-orienting copy-paste blocks (per-thread variants)

Each thread starts with a different copy-paste block to load Claude with thread-scoped context. **Use the block matching the thread you're starting.**

### §1.α Thread α — Architecture / terms_index → Phase 3 → Phase 4

```
SESSION CONTEXT — Commons Bonds (Book 1) — THREAD α (architecture/scaffolding)

Project: /Users/c17n/commons-bonds. Worktree-isolation git workflow per Working Principle #9 (commit on feature branch; push HEAD:main on ratified chunks).

Read these to orient:
1. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md (full project state)
2. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md §3.α (this thread's scope)
3. alignment/commons_bonds_working_principles_v1.0.0.md (WP#4 REFINEMENT 2026-04-30 + WP#9 NEW)
4. archive/retirements/index.md (canonical retirement-archive per Insight #59)

THREAD α SCOPE: Bucket A (refined WP#4 implementation: terms_index v1.0.0 + vocab strategy light-trace + working principles cleanup) + Bucket F (AIT → CIT cleanup in terms_index) + Bucket G (4 nuanced Ring-2 entries) → batched as ONE terms_index v1.0.0 commit. THEN Phase 3 Tech Appendix v2.0.0 rebuild (~20-30 hrs; batches all Phase 2 + Group 1 ratifications). THEN Phase 4 Glossary v4 rebuild (~3-5 hrs).

DO NOT TOUCH (Thread β scope): manuscript/chapters/Chapter*.md prose · publisher-facing chapter HTML drafts · Ch 1 + Ch 3 drafting work.

DO NOT TOUCH (Thread γ scope): README.md (any section beyond what Phase 3 implies) · archive/ folder structure (consolidation decision is γ's call).

INSIGHT NUMBERING: next free is #64. If you need to raise a new insight, take #64; coordinate with author before #65 if multiple threads claim simultaneously.

START BY: confirming thread α scope; surfacing the first batched commit plan (terms_index v1.0.0 changes) for author confirmation before edits.
```

### §1.β Thread β — Drafting / #37 → #36 → Ch 6 → Ch 5

```
SESSION CONTEXT — Commons Bonds (Book 1) — THREAD β (drafting/manuscript)

Project: /Users/c17n/commons-bonds. Worktree-isolation git workflow per Working Principle #9.

Read these to orient:
1. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md (full project state)
2. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md §3.β (this thread's scope)
3. alignment/commons_bonds_open_insights_v1.0.0.md (Insights #21 + #36 + #37 — full content)
4. tools/commons_bonds_book_scope_v1_0_3.md (Book 1 scope; Insight #24 — no Book 2 references)

THREAD β SCOPE: Insight #37 scaffolding-vs-publisher-facing separation pass first (~3-5 hrs; produces accurate publisher-facing word-count gaps). THEN Insight #36 Ch 1 + Ch 3 conversational drafting session (gated by #37 completion). THEN Ch 6 structural placement (Insight #21; ~13 placements; ~5,000 words). Ch 5 pre-submission review (FLAGGED) is a side-quest.

DO NOT TOUCH (Thread α scope): core/terms/terms_index.md · core/glossary/* · core/technical-appendix/* (Tech Appendix v2.0.0 rebuild is α's batched scope; mid-stream chapter edits that cite Tech Appendix should reference current v1.0.0 not in-progress v2.0.0).

DO NOT TOUCH (Thread γ scope): README.md · archive/ folder structure.

CONFLICT-ZONE WARNING: If Phase 3 (Thread α) is running concurrently with Ch 6 structural placement (Thread β Insight #21), Ch 6 work depends on Tech Appendix §6.5–§6.10 companion passages — likely safer to defer Ch 6 structural placement until α's Phase 3 lands, OR confirm with author that Ch 6's source supplementary §6.5–§6.10 references are stable before β starts.

INSIGHT NUMBERING: next free is #64 (or higher if α claimed). Coordinate with author.

START BY: confirming thread β scope + reading Insight #37 + #36 + #21 in detail; recommending whether to start with #37 separation pass OR Ch 5 pre-submission review (Ch 5 is independent and lower-conflict).
```

### §1.γ Thread γ — Hygiene / README + archive consolidation

```
SESSION CONTEXT — Commons Bonds (Book 1) — THREAD γ (hygiene)

Project: /Users/c17n/commons-bonds. Worktree-isolation git workflow per Working Principle #9.

Read these to orient:
1. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md (full project state)
2. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md §3.γ (this thread's scope)
3. alignment/commons_bonds_open_insights_v1.0.0.md (Insight #61 README + Insight #62 archive consolidation — full content)
4. README.md current state

THREAD γ SCOPE: Two items — (i) Insight #61 README.md comprehensive update (full sweep beyond obvious-stale entries fixed in #60 follow-on; ~1-2 hrs); (ii) Insight #62 archive folder consolidation DECISION (decide strategy, optionally execute). Both can land in one session.

DO NOT TOUCH (Thread α scope): core/terms/terms_index.md · core/glossary/* · core/technical-appendix/* · alignment/commons_bonds_working_principles_v1.0.0.md (Phase 3 + Phase 4 work) · alignment/commons_bonds_vocabulary_strategy_v1.0.1.md.

DO NOT TOUCH (Thread β scope): manuscript/chapters/* prose (drafting work).

LOW-CONFLICT NOTE: this thread is best run between α/β phases or as solo work — README is mostly orthogonal to active edits, but archive consolidation execution touches paths that Phase 3 may reference, so hold #62 EXECUTION until Phase 3 (α) completes; #62 DECISION is safe anytime.

INSIGHT NUMBERING: next free is #64.

START BY: surface README #61 work plan to author; if approved, execute README sweep first; #62 decision second (lighter cognitive load to land both in one session).
```

### §1.δ Thread δ — Discussion-surfacing (lightweight)

```
SESSION CONTEXT — Commons Bonds (Book 1) — THREAD δ (discussion-surfacing)

Project: /Users/c17n/commons-bonds.

Read:
1. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md (full project state)
2. alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md §3.δ (this thread's scope)
3. alignment/commons_bonds_open_insights_v1.0.0.md (Insights #9 + #13 + #14 — full content)

THREAD δ SCOPE: Surface three OPEN insights to author for decision/discussion:
- Insight #9 — Framework as decision-time severance-detection tool (raised; no decision yet)
- Insight #14 — Norway's sovereign wealth fund canonical exemplar (load-bearing for Book 1 voice; Ch 4 + Accountability Bond integration)
- Insight #13 — Book-scope creep monitoring (ongoing discipline; not per-term decision; periodic check-in)

NO FILE EDITS WITHOUT AUTHOR DECISION. This is conversation/discussion thread; outputs are decisions logged into open insights file once ratified.

INSIGHT NUMBERING: next free is #64.

START BY: surface Insight #9 first (oldest unresolved); summarize current state + decision options + recommended verdict; await author response.
```

---

## §2. Coordinated state (one paragraph)

Post-v1.48.0: All 8 Phase 2 flagged items resolved. All 3 Group 1 items resolved. Insight #55 framework-wide notation collision audit ratified (3 HIGH renames queued for Phase 3 batch). WP#4 refined (tiered retirement-trace policy + canonical retirement-archive at `archive/retirements/index.md`). WP#9 added (worktree-isolation git workflow). 10 OPEN insights remain (#9, #13, #14, #21, #36, #37, #39, #61, #62, #63). **No remaining blockers for Phase 3 Tech Appendix v2.0.0 rebuild** (~20-30 hrs; the largest single batched effort in the queue). Phase 4 Glossary v4 rebuild (~3-5 hrs) follows Phase 3. Insight #63 (Tier word-level conceptual collision) captured as OPEN with quick-fix (B) applied; focused rigor pass (D) queued for pre-publication external review window (Insight #39).

---

## §3. Threads — parallel execution plan

### §3.α Thread α — Architecture (terms_index → Phase 3 → Phase 4)

**Lead files (this thread owns):**
- `core/terms/terms_index.md`
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` → rebuild as `v2.0.0.html`
- `core/glossary/commons_bonds_updated_glossary_v3.html` → rebuild as `v4`
- `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` (§6 + §7 + §13 light-trace migration)
- `alignment/commons_bonds_working_principles_v1.0.0.md` (body cleanup)
- `archive/retirements/index.md` (additions as full traces migrate from terms_index)

**Prereqs:** none — α is the upstream architectural work; can start immediately.

**Scope (sequential within thread):**

**Phase α.1 — Bucket A + F + G batched (terms_index v1.0.0 version bump; ~2-3 hrs):**
- terms_index v0.1.0 → v1.0.0 version bump applies summary-level retirement traces (full traces migrate to `archive/retirements/index.md`)
- Vocab strategy v1.0.1 §6 + §7 + §13 light-trace migration to cross-reference archive
- Working principles body cleanup (small; some inline traces could cross-reference archive)
- AIT → CIT regression cleanup in terms_index (line 1395 + Abundance Masking entry historical/current judgment) — Bucket F
- 4 nuanced Ring-2 entries: intergenerational cost severance lowercase; Temporal CS hybrid; Spatial CS hybrid; Accountability Bond UPDATE sub-instruments (B₁ + B₂ rendering fields) — Bucket G

**Phase α.2 — Phase 3 Tech Appendix v2.0.0 rebuild (~20-30 hrs):**
- Theorem restructures: E.1 split into E.1a + E.1b + premises P1–P3 + citations (Insight #41); E.2 categorization (Insight #51); E.3 restructure + parallel-session integration (Insight #42); E.4 premises A1–A4 + restructured proof (Insight #40); E.5 Renewable Imperative → Substitution Dominance + Corollary E.5.1 (Insight #53)
- Notation discipline (Insight #55): α → ξ for E.3 cost-function curvature; τ → u for line 6720 integration variable; C → 𝒞 (script C) for line 398 commons-territory set
- §L methodological footnotes: Cost Severance + Severed Cost (Insight #35); Foreclosure Bond (Insight #38); Intergenerational Option Value (Insight #57)
- Mathematical apparatus: RCV integrand Definition A.3 expansion (Insight #52); scarcity multiplier formula bibliography expansion (Insight #47); Externality Tail enhancements (Insight #49); Three Ways of Counting adoption-fit (Insight #48); RCV acronym disambiguation (Insight #50)
- Content absorption: `core/dimensions/` content into §C.2 (then archive directory)
- Bibliography expansion (full citation list in v1.48.0 §5.2)

**Phase α.3 — Phase 4 Glossary v4 rebuild (~3-5 hrs):**
- Derives from terms_index v1.0.0 per S1 schema; absorbs Phase 2 + Group 1 ratifications

**Files NOT to touch (Thread β + γ scope):**
- `manuscript/chapters/*` (Thread β)
- `README.md` (Thread γ)
- `archive/` folder structure beyond `archive/retirements/index.md` additions (Thread γ owns consolidation)

**Success criteria:**
- terms_index v1.0.0 committed (closes refined WP#4 implementation pending list)
- Phase 3 commit lands `core/technical-appendix/TechnicalAppendix_v2.0.0.html` with all theorem restructures + notation discipline + §L footnotes + math apparatus integrated
- Phase 4 commit lands `core/glossary/commons_bonds_updated_glossary_v4.html` with terms_index-derived structure
- WP#4 implementation pending list per v1.48.0 §5.2 closes

**Closes insights:** none directly (the implementation-pending items are sub-tasks of #59 which is already closed); but this work UNBLOCKS #39 + #63 + pre-publication citations audit.

**Estimated total effort:** ~25-38 hrs across multiple sessions.

---

### §3.β Thread β — Drafting (#37 → #36 → Ch 6 → Ch 5)

**Lead files (this thread owns):**
- `manuscript/chapters/Chapter*.md` (chapter drafts)
- `manuscript/chapters/Chapter*GuidanceDoc.md` (chapter guidance docs)
- `manuscript/chapters/archive/Chapter__6___SupplementaryDrafts_2026-04-24.md` (read-only source for Ch 6 placement)

**Prereqs:** Thread β can start without Thread α completing — but Ch 6 structural placement (Insight #21 sub-item) benefits from Phase 3 (α) being stable for Tech Appendix companion-passage references. Recommendation: start with Insight #37 OR Ch 5 review (both safe regardless of α state).

**Scope (sequential within thread):**

**Phase β.1 — Insight #37 scaffolding-vs-publisher-facing separation pass (~3-5 hrs):**
- Decide scope: now vs at chapter pre-submission editing (per Insight #37 OPEN status)
- If proceeding now: separate scaffolding annotations (audit-trail content per WP#8) from publisher-facing chapter prose
- Recompute publisher-facing word counts → produces accurate gaps for Ch 1 + Ch 3 drafting

**Phase β.2 — Insight #36 Ch 1 + Ch 3 conversational drafting session (gated by β.1; dedicated session):**
- Ch 1 personal stories drafting cycle (Path F)
- Ch 3 (waterman) draft — currently 0 words; 5K-6K target

**Phase β.3 — Insight #21 Ch 6 HTML structural placement (~13 placements; ~5,000 words):**
- Integrate Ch 6 supplementary §6.5–§6.10 passages into proper chapter body structure
- Source: `manuscript/chapters/archive/Chapter__6___SupplementaryDrafts_2026-04-24.md`
- Target: `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`
- ⚠ Coordinate with α before starting if Phase 3 Tech Appendix rebuild is mid-flight (Tech Appendix companion passages may shift)

**Phase β.4 (side-quest) — Ch 5 pre-submission review (FLAGGED):**
- Independent of α state; can run anytime
- Ch 2 interviews (3 INTERVIEW NEEDED placeholders) — author-only

**Files NOT to touch (Thread α + γ scope):**
- `core/terms/terms_index.md` · `core/glossary/*` · `core/technical-appendix/*` (Thread α)
- `alignment/commons_bonds_working_principles_v1.0.0.md` · `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` (Thread α)
- `README.md` · `archive/` folder structure (Thread γ)

**Success criteria:**
- #37 closes (separation pass applied OR explicit decision to defer to pre-submission editing)
- #36 closes (Ch 1 + Ch 3 land at target word counts)
- #21 closes (Ch 6 supplementary passages integrated; Ch 6 reaches target word count)

**Closes insights:** #37, #36, #21 (potentially Ch 5 review FLAG). Manuscript meaningfully closer to submission-ready state, which UNBLOCKS #39 → #63 + pre-publication citations audit.

**Estimated total effort:** ~15-25 hrs across multiple sessions (Ch 3 drafting is the largest sub-item).

---

### §3.γ Thread γ — Hygiene (README #61 + archive consolidation #62)

**Lead files (this thread owns):**
- `README.md`
- `archive/` folder structure (consolidation decision/execution)
- `tools/README.md` (if archive consolidation affects tools/archive/)

**Prereqs:** none for #61 README sweep; #62 EXECUTION should hold until Phase 3 (α) completes (path stability), but #62 DECISION is safe anytime.

**Scope:**

**Phase γ.1 — Insight #61 README.md comprehensive update (~1-2 hrs):**
- Beyond obvious-stale entries fixed in #60 follow-on (commit `47408e1`)
- Cross-section consistency check
- Regenerate from current canonical state
- Integrate WP#9 + refined WP#4 + Insight #63 disambiguation + retirement-archive references
- Verify Repository structure section reflects actual directory state
- Verify Current canonical state table reflects all Phase 2 + Group 1 ratifications

**Phase γ.2 — Insight #62 archive folder consolidation DECISION (~30 min for decision; ~1-2 hrs for execution):**
- Three options per Insight #62: (a) Consolidate now to `archive/{technical-appendix,manuscript-chapters,tools}/`; (b) Leave per-domain archives; (c) Hybrid — top-level `archive/` for cross-domain + per-domain archives
- Trade-offs already enumerated in Insight #62 body
- DECISION first; execution gated by Phase 3 (α) completion

**Files NOT to touch (Thread α + β scope):**
- `core/terms/terms_index.md` · `core/glossary/*` · `core/technical-appendix/*` (Thread α)
- `alignment/commons_bonds_working_principles_v1.0.0.md` · `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` (Thread α)
- `manuscript/chapters/*` (Thread β)

**Success criteria:**
- #61 closes (README full sweep applied)
- #62 decision recorded; execution either applied OR explicitly deferred-pending-Phase-3

**Closes insights:** #61, #62 (decision-only or full).

**Estimated total effort:** ~2-4 hrs single session.

---

### §3.δ Thread δ — Discussion-surfacing (lightweight, async)

**Lead files (this thread owns):** `alignment/commons_bonds_open_insights_v1.0.0.md` (status updates only; no new insights without author confirmation).

**Prereqs:** none — fully independent.

**Scope:**

- **Insight #9** — Framework as decision-time severance-detection tool: surface to author with current state + decision options + recommended verdict
- **Insight #14** — Norway's sovereign wealth fund canonical exemplar: surface for Book 1 voice calibration discussion (Ch 4 + Accountability Bond integration)
- **Insight #13** — Book-scope creep monitoring: periodic check-in (ongoing discipline; not per-term decision)

**Output:** decisions logged into open insights file once ratified by author. No file edits beyond status updates without author confirmation.

**Files NOT to touch:** anything beyond open insights status updates.

**Success criteria:**
- #9 → closed-ratified or explicit defer-with-rationale
- #14 → closed-ratified with Ch 4 + Accountability Bond integration plan
- #13 → confirmed ongoing; no action needed

**Estimated total effort:** ~1-2 hrs single session (likely runs as conversation rather than execution).

---

## §3.5 Cross-thread discipline addendum (2026-04-30) — Working Principle #10 layer-classification

**RATIFIED 2026-04-30 during Thread δ Insight #9 surfacing.** Working Principle #10 (Two-layer content origination discipline) applies to **all four threads**:

> All new framework content is classified at origination as **internal-scaffolding** or **external-publisher-facing**. Internal scaffolding is rich; external is disciplined per WP#8 + Pattern 2 demonstration (threaded through cases rather than codified in dedicated how-to / methodology sections — the *Doughnut Economics* / *Mission Economy* / *Mine!* model).

**Per-thread application:**
- **Thread α (architecture):** Phase 3 Tech Appendix v2.0.0 + Phase 4 Glossary v4 are external-layer rebuilds — apply WP#8 scrubbing + Pattern 2 demonstration (Tech Appendix demonstrates the framework's apparatus through theorems + cases; doesn't codify a decision-time methodology). Internal scaffolding (terms_index v1.0.0; vocab strategy; working principles) stays rich per its layer.
- **Thread β (drafting):** Ch 1 + Ch 3 conversational drafting (Insight #36) absorbs Pattern 2 threading at external layer — personal stories carry decision-time anchors WITHOUT codifying a methodology. Ch 6 supplementary integration applies same discipline. Ch 5 review applies WP#8 scrubbing.
- **Thread γ (hygiene):** README.md is publisher-facing landing page — apply WP#8 + Pattern 2; archive consolidation operates on internal-scaffolding structure (no external-layer impact except path references).
- **Thread δ (discussion):** Insight #14 (Norway) already operates on Pattern 2 discipline ("demonstrate the affordance; don't codify it"); Insight #13 (book-scope creep) is reinforced by WP#10 (rich internal preserves Book 2 seed material without scope-creep into Book 1).

**Default behavior when uncertain:** classify new content as internal scaffolding. It's easier to promote internal material to external (when it earns the slot via Pattern 2 demonstration) than to scrub publisher-facing artifacts of accumulated scaffolding.

**Cross-references:**
- Working Principle #10 — `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #10
- Internal scaffolding canonical artifact — `core/methodology/decision_time_application_internal_v1.0.0.md`
- Insight #9 closed-ratified 2026-04-30 (verdict source for WP#10 generalization)

---

## §4. Parallel-session coordination discipline

### §4.1 File-level conflict map

| Domain | Owner thread | Other threads |
|---|---|---|
| `core/terms/terms_index.md` | **α** | β/γ/δ: read-only |
| `core/glossary/*` | **α** | β/γ/δ: read-only |
| `core/technical-appendix/*` | **α** | β: read-only (chapter cross-references); γ/δ: read-only |
| `alignment/commons_bonds_working_principles_v1.0.0.md` | **α** | others: read-only |
| `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` | **α** | others: read-only |
| `archive/retirements/index.md` | **α** (additions) | γ: read-only |
| `manuscript/chapters/*` (drafts + GuidanceDocs + HTML) | **β** | α/γ/δ: read-only |
| `manuscript/chapters/archive/*` | **β** (read source) | α: read-only |
| `README.md` | **γ** | others: read-only |
| `archive/` structure (folder-level) | **γ** (consolidation) | α: read-only beyond `archive/retirements/index.md` |
| `alignment/commons_bonds_open_insights_v1.0.0.md` | **shared** (any thread can add insights or update statuses for own insights) | strict insight-numbering coordination |
| `alignment/sessions/*` | **shared** (handoff updates) | usually only one thread writing per cycle |
| `tools/rigor-passes/*` | **scoped per insight** | author-direction-gated |

### §4.2 Insight numbering discipline

**Next free insight number: #64.**

Parallel sessions MUST coordinate to avoid the Insight #54 collision pattern (subject-collision with canonical #42 from this session — required retirement of #54 + renumbering #41–#47 → #47–#53).

**Discipline:**
- First thread to need a new insight number takes #64
- Subsequent threads check `alignment/commons_bonds_open_insights_v1.0.0.md` HEAD before claiming (a quick `git pull` + grep)
- If two threads claim the same number simultaneously, author-arbitrated retirement + renumber (per #54 precedent)
- For Phase 3 work (Thread α), insights ratified during the rebuild can pre-claim a numeric range (e.g., #64–#70 reserved for Phase 3 if needed) — coordinate with author

### §4.3 Sync points (where threads must coordinate)

1. **terms_index v1.0.0 commit (Thread α Phase α.1)** — once landed, all threads can reference summary-level retirement traces; full traces in archive. Threads should `git pull` before continuing if they're reading terms_index.

2. **Phase 3 Tech Appendix v2.0.0 commit (Thread α Phase α.2)** — Tech Appendix companion passages stabilize. Thread β Insight #21 (Ch 6 structural placement) should defer until this lands OR confirm with author that Ch 6 source supplementary §6.5–§6.10 references are stable independently.

3. **Phase 4 Glossary v4 commit (Thread α Phase α.3)** — Glossary references stabilize.

4. **Insight #62 archive consolidation execution (Thread γ Phase γ.2)** — must wait for Thread α Phase α.2 + α.3 to complete (path stability). Decision can land before; execution after.

### §4.4 Commit + push discipline (WP#9 reminder)

- Commit on the worktree's feature branch
- After each closed-ratified insight or atomic patch: `git push origin <branch>:main` (FF)
- Other threads `git pull origin main` to receive ratified work
- If ratified-chunk push fails non-FF, the other thread already pushed — `git pull --rebase origin main` and retry

### §4.5 Handoff update discipline

When a thread closes meaningful work, append a stub to v1.49.0 §5 (cross-thread log) noting:
- Date
- Thread (α/β/γ/δ)
- Closed insights / committed work
- Next thread can read the cross-thread log for state-of-the-pack before starting

---

## §5. Cross-thread execution log

*Threads append entries here as work lands. Use this to see what other threads have closed without reading every commit.*

| Date | Thread | What landed | Insights closed |
|---|---|---|---|
| 2026-04-30 | δ | Insight #9 RATIFIED (verdict (b) threaded Pattern 2 + rich internal scaffolding) + Insight #14 CLOSED-RATIFIED + Working Principle #10 NEW (Two-layer content origination discipline) + new internal-scaffolding artifact `core/methodology/decision_time_application_internal_v1.0.0.md` + §3.5 cross-thread WP#10 addendum to this handoff. Commits `35d202e` + `61817a9`. | #9, #14 |
| 2026-04-30 | α | Phase α.1 batched commit — terms_index v0.1.0 → v1.0.0 (Buckets A + F + G): summary-level retirement-trace migration per refined WP#4; AIT → CIT regression cleanup; intergenerational/Temporal/Spatial CS hybrid entries condensed; B₁/B₂ Restitution Bond + Foreclosure Bond rendering fields added (Glossary def + Tech Appendix def in Claude's voice — flagged for author voice refinement during Phase α.2/α.3); vocab strategy v1.0.1 §6 + §13 light-trace migration; working principles v1.0.0 P#4 annotation marking 2026-04-30 refinement supersedes 2026-04-24 body | none directly (closes refined-WP#4 implementation pending list per v1.48.0 §5.2; UNBLOCKS Phase α.2 Tech Appendix v2.0.0 + Phase α.3 Glossary v4) |
| 2026-04-30 | γ (hygiene) | (i) `README.md` rescoped as slim publisher-facing landing page per WP#10 verdict (R2); (ii) `AGENTS.md` NEW — canonical internal-scaffolding orientation document (canonical-state table, repository structure, archive convention, working discipline, WP#10 layer classification, queued work, session workflow, operating rules, internal vocabulary); (iii) `archive/retirements/index.md` §0 archive convention added (v1.0 → v1.1) per Insight #62 verdict (c) hybrid as canonical pattern. WP#10 mid-thread-γ reframe applied: original Insight #61 hybrid sweep was scrubbed and split per WP#10 origination discipline rather than executing-then-scrubbing per Insight #37. | #61 (README rescope per (R2) + WP#10); #62 (archive hybrid (c) ratified) |
| 2026-04-30 | δ wrap | Working principles WP#5 light-trace cleanup (ARP → ARR + AIT → CIT current-term sweep with archive cross-references per refined WP#4 / Insight #59). Chapter word counts refreshed in v1.48.0 §3 (RAW counts via `wc -w` sweep; notable shifts vs v1.47.0 estimates flagged as scaffolding-accumulation candidates for Insight #37 separation pass). Auto-memory updates capturing WP#10 + Pattern 2 register for future-session inheritance (`feedback_two_layer_content_discipline.md` + `reference_pattern_2_register.md` added to user memory; MEMORY.md index updated). Insight #13 status line updated with REINFORCED-by-WP#10 note (remains OPEN as ongoing discipline). | none (cleanup only) |
| 2026-04-30 | β | **Insight #37 RATIFIED** — full scope (option a) separation pass executed across all 9 chapter Drafts + 9 chapter GuidanceDocs (incl. Ch 3 pre-draft GuidanceDoc). Mechanism revised mid-flight per author direction: scaffolding consolidated INTO existing `Chapter__N___GuidanceDoc.md` (not separate `Scaffolding.md` sidecars; reuses existing filename so 65 cross-references unchanged). Each GuidanceDoc carries WP#10 frontmatter + global staleness disclaimer (per-section staleness audit deferred to future pass). Pattern 2 register check across all Drafts: PASS. **Publisher-facing word counts (post-#37):** Ch 1: 414 (was 1,446 raw; -71% — vast Insight #36 β.2 gap to fill); Ch 2: 5,026 (-250); Ch 4: 4,039 (no change; ~1K below target); Ch 5: 9,460 (-46; **β.4 pre-submission review side-quest still open — ~58% over original 5K-6K target**); Ch 6 HTML: 10,941 (no scrub; deferred to Insight #21 dedicated session); Ch 7: 7,532 (no change); Ch 8: 6,027 (no change); Ch 9: 10,007 (-320); Ch 10: 7,420 (-262). UNBLOCKS Insight #36 (Ch 1 + Ch 3 conversational drafting; accurate word-count gaps now available). | #37 |
| 2026-05-01 | α | **Phase α.2.1 batched commit** — Tech Appendix v1.0.0 §15.2 *Methodological framing footnotes* added (3 subsections: §15.2.1 Cost Severance + Severed Cost cross-political-tradition; §15.2.2 Foreclosure Bond housing-crisis affect handling; §15.2.3 Intergenerational Option Value framework specialization). v1 DRAFT in Claude's voice — awaits author voice refinement during full Phase α.2 rebuild. Publisher-facing-clean per WP#8 + WP#10 (no Ring/Tier/Insight/Working-Principle/rigor-pass-path scaffolding refs). Insertion: +364 lines after §15.1.9, before §16. **Note:** existing §15.1 retains some scaffolding-style refs (M12, Working Principle #6, rigor-pass commit `d4c4be4`) that should land in the comprehensive WP#8 + WP#10 scaffolding-scrub batch (queued as α.2.7). Phase α.2 first batch (proof-of-concept); E.4 restructure (α.2.2) follows. | none directly (advances Phase α.2 rebuild; UNBLOCKS subsequent theorem restructures) |
| 2026-05-01 | α | **Phase α.2.2 batched commit** — Tech Appendix v1.0.0 Theorem E.4 (RCV Integral Convergence under Weitzman Declining Discount) restructured per Insight #40 ratified verdict (a). Replaces 9-line single-paragraph theorem-statement-and-proof with: explicit Premises A1–A4 (utility growth, externality growth, substitutability monotonicity, Weitzman declining-rate framework); restructured theorem statement with two sufficient conditions (SC1: positive long-run discount; SC2: sufficient substitutability convergence); knife-edge divergence corollary promoted from prose-footnote to explicit corollary; multi-case proof with explicit Lebesgue dominated convergence theorem invocation per case (Royden 1988 §4.4 + Folland 1999 §2.4 cited); interpretation note separated from proof body. Net diff +119 / -3 lines at HTML lines 3278–3404. Publisher-facing-clean per WP#8 + WP#10. Cross-reference at line 707 ("see Theorem E.4") preserved. | none directly (advances Phase α.2 rebuild; restructured E.4 now meets academic-peer-review standards per ratified rigor pass §13) |
| 2026-05-02 | α | **Phase α.2.3 batched commit** — Tech Appendix v1.0.0 Theorem E.1 split into E.1a + E.1b per Insight #41 ratified verdict (a). Replaces ~10-line single-paragraph E.1 (Structural Cost Severance with wrong "B ≤ P" assumption) with: **E.1a (Cost Severance Identity)** — trivially true by algebra; sign-determination of CS via comparison of RCV vs B; Assumption A1 (Cost Severance Definition); usable as building-block for downstream theorem proofs (E.5 Renewable Imperative invokes it). **E.1b (Structural Cost Severance under Current Institutions)** — explicit Assumptions A2–A4 (RCV non-negativity; B non-negativity; aggregate scope) + load-bearing Premises P1–P3 (P1 intergenerational market incompleteness as Coase 1960 extension; P2 partial externality pricing as Pigou 1920 + Stern Review 2007 extension; P3 current accountability bond inadequacy as empirical claim cross-referencing §H validation cases); structural-empirical theorem stating B < RCV under current institutions; explicit falsifiability conditions; explicit domain of applicability (non-renewable extraction under contemporary institutions; renewable extraction + comprehensive-coverage hypothetical jurisdictions outside scope). Plus stale-cross-reference fix at line 2866 (was "Theorem E.1 in Section E on RCV integral convergence" — that was actually E.4's content; corrected to "Theorem E.4"). Net diff +114 / -5 lines at HTML lines 3248–3380. Publisher-facing-clean per WP#8 + WP#10. Cross-reference at line 720 ("Theorem E.1 (Structural Cost Severance)") preserved as resolving to E.1b's name. | none directly (advances Phase α.2 rebuild; restructured E.1a + E.1b now meets academic-peer-review standards per ratified rigor pass §13; framework's central theorem now has academic-rigor-grade proof structure) |
| 2026-05-02 | α | **Phase α.2.4 batched commit** — Tech Appendix v1.0.0 Theorem E.3 (Abundance Masking under Stock-Flow Framework) restructured per Insight #42 ratified verdict (a) Full ratify with 4 enhancements (3 original + 1 post-ratification per parallel-session integration). Replaces ~7-line E.3 (circular-reasoning proof citing CIT-as-source-of-phenomenon) with: explicit Assumptions A1–A4 (stock-flow framework; cost-function structure with explicit functional form c(A) = c₀ · (τ/(A−τ))^ξ for ξ ≥ 1; standard supply-elasticity behavior; domain restrictions excluding renewable / non-rivalrous / network-effect / multi-threshold commons); abstract premise framing (P1–P4) complementary to A1–A4 per parallel-session integration; notation note disambiguating τ (scarcity threshold) from S(t) (substitutability function) and S_max (existential substitutability gap); restructured theorem statement with parts (i) cost-masked-when-abundance-large + (ii) cost-diverges-as-abundance-approaches-threshold; multi-case proof (proof of (i) + proof of (ii)) with TWO complementary lineages cited (commodity-economics + supply-elasticity: Marshall 1890; Hotelling 1931; Hamilton 2009; Kilian 2009; Pindyck 2008 — price-discovery framing; resource-economics + tipping-point: Pindyck 1978; Dasgupta-Heal 1979; Barnosky 2012; Lenton 2008 — biophysical/structural framing); empirical illustration separated from proof; operational-corollary backward-pointer to CIT establishing E.3-as-analytic-theorem / CIT-as-operational-protocol relationship (eliminates circularity at structural level). Plus Definition A.8 (CIT) update at line 496+: forward-pointer establishing CIT-as-operational-corollary relationship to E.3 + scarcity-threshold notation update Sj → τj. **Notation discipline applied:** ξ used (not α) for cost-function curvature parameter per Insight #55 reserved-letter ledger (α reserved for §M scarcity multiplier irreversibility parameter). Net diff +133 / -4 lines at HTML lines 496–504 + 3379–3500 (within §6 CIT Definition + §10 Theorems and Proofs). Publisher-facing-clean per WP#8 + WP#10. | none directly (advances Phase α.2 rebuild; restructured E.3 now meets academic-peer-review standards per ratified rigor pass §13 + §17 integrated content; circular-reasoning structural defect eliminated at both proof-content level and logical-organization level) |
| 2026-05-02 | α | **Phase α.2.5 batched commit** — Tech Appendix v1.0.0 Theorem E.2 + Theorem E.5 restructured per Insights #51 + #53 ratified verdicts. **E.2 (Insight #51 Option A):** "Theorem E.2 (Convergence of Independent Models)" → "Empirical Observation E.2 (Cross-Model Convergence)"; replaces single-paragraph theorem-and-proof-sketch with: explicit empirical claim (4 empirical + 2 thought-experiment cases producing IPG estimates within one order of magnitude); supporting argument citing data-source independence + Hong & Page 2004 PNAS + Mosteller & Tukey 1977; failure modes (3 categories); domain of applicability (tested calibration case landscape); categorization note explaining why E.2 is empirical observation rather than theorem (claim-form difference from E.1/E.3/E.4/E.5). Plus cross-reference cleanup at line 3239 ("consistent with Theorem E.2 (Convergence of Independent Models)" → "consistent with E.2 (Cross-Model Convergence)"). **E.5 (Insight #53 Option α + β COMBINED):** "Theorem E.5 (Renewable Imperative)" → "Theorem E.5 (Substitution Dominance)"; replaces single-paragraph theorem with appended-corollary with: explicit Premises P1–P4 (cost-severance condition citing Theorem E.1a; substitutability-improvement structural premise; future-generation positive weight; investment-cost opportunity-cost framing); restructured Path A / Path B social welfare comparison proof; lineage paragraph (Hartwick 1977 AER; Weitzman 2001 AER; Dixit-Pindyck 1994; Solow 1974 Rev Econ Stud; Stiglitz 2000; Stern 2007); failure modes (4 categories — discount-rate / substitutability-investment / ethical-framework / investment-cost); **Corollary E.5.1 (Optimal Extraction Sequencing) promoted from prose-appendage to formal corollary** with own proof + asteroid-mining + renewable-energy prioritization examples; interpretation note ("framework is a navigation system, not a prohibition") separated from formal apparatus. Cross-reference to Theorem E.1a explicit per Insight #41 cross-reference guidance (E.5 invokes E.1a's algebraic identity in proof). Note: line 328 historical "Renewable Imperative" reference in version-archaeology preamble preserved as-is (broader version-archaeology scrub queued for α.2.7 per WP#8). Net diff +181 / -7 lines at HTML lines 3239 + 3375–3470 (E.2) + 3663–3820 (E.5). Publisher-facing-clean per WP#8 + WP#10. | none directly (advances Phase α.2 rebuild; all 5 theorems now restructured to academic-peer-review standards: E.1a + E.1b + E.2 (now Empirical Observation) + E.3 + E.4 + E.5 + Corollary E.5.1) |
| 2026-05-02 | α | **Phase α.2.6 batched commit** — Tech Appendix v1.0.0 mathematical apparatus + remaining notation discipline + acronym/term disambiguation enhancements per Insights #47 + #48 + #49 + #50 + #52 + #55 (remaining items). **#48 TWoC adoption-fit:** TOC line 225 + section header line 683 "RCV Quantification — Triangulated Estimation (Three Ways of Counting)" → "RCV Quantification — Three Ways of Counting" (Option A clean drop). **#55 remaining notation discipline:** C → 𝒞 (script C) at line 398 commons-territory set with typographic-disambiguation note (distinguishes from C cost variable Cᵢ); τ → u for line 7612 integration variable in K.1 RCV with Variable Discount Rates (disambiguates from E.3 scarcity threshold τ). **#52 RCV integrand Definition A.3 expansion:** explicit Q-as-stock notational convention with type-disambiguation citing convention-divergence anchors (Hotelling 1931 q-as-flow; Pindyck 1978 X-as-stock; Dasgupta-Heal 1979 S-as-stock collision; Mussa-Rosen 1978 Q-as-quality); adjacent literature (Slade-Thille 2009; Spence 1976; Tirole 1988). **#47 scarcity multiplier formula:** functional-form motivation note inserted after RCV_M3 formula at line 887; four converging reasons (Hotelling rent-path conjugate; welfare-economics log-utility lineage Atkinson 1970 + Cobb-Douglas 1928; bounded-concavity + numerical-tractability with discipline-claim correction (slow-growing logarithmically; structurally unbounded as σ → ∞; alternative asymptotic-bounded forms admissible); intergenerational-equity lineage Solow 1956 + Bergson 1938). **#49 Externality Tail temporal-tail vs statistics-tail disambiguation:** Definition A.4 extended with notational disambiguation paragraph clarifying "long tail in time" vs statistics-distribution-tail conventions (Mandelbrot 1963; Taleb 2007; Embrechts et al. 1997; Anderson 2006). **#50 RCV acronym disambiguation:** Definition A.6 extended with three real-world acronym-collision notes (Ranked-Choice Voting first per §15 Q5 ratification — Reilly 2001; Replacement Cost Value — Insurance Information Institute / Casualty Actuarial Society; Risk Capital Value — Basel III); first-introduction discipline codified ("introduce as 'Residual Commons Value (RCV)' on first appearance per chapter or major section"). Net diff +75 / -6 lines across 6 surgical edits. Publisher-facing-clean per WP#8 + WP#10. | none directly (advances Phase α.2 rebuild; mathematical apparatus + notation discipline complete; all framework primitive definitions A.3/A.4/A.6 + scarcity multiplier + integration variable + commons-territory set now meet academic-peer-review standards) |
| 2026-05-02 | α | **Phase α.2.7a batched commit** — Tech Appendix v1.0.0 §5 (Accountability Bond Decomposition) restructured: B₁/B₂ Tech Appendix formal definitions integrated from terms_index Phase α.1 drafts as new §5.1.1 (B₁ Restitution Bond) + §5.1.2 (B₂ Foreclosure Bond) sub-sub-sections under §5.1 "Sub-instrument formal definitions"; each sub-instrument carries definition + mechanisms-in-cluster + naming-rationale + lineage paragraphs (B₁ adds status-of-globally-underdeveloped note; B₂ ends at lineage). Plus expanded §5 introduction making the two-instrument decomposition explicit at the equation level (total CS = (CSD − B₁) + (RCV − B₂)) with structural-pairing explanation. Plus section-numbering cleanup: §4.1/§4.2/§4.3 (mislabeled artifacts from prior numbering schemes inside §5) → §5.1/§5.2/§5.3 (consistent). Plus WP#8 scrub of audit-trail content from §5: "Sources: ... Backed by B₁/B₂ decomposition rigor pass (commit ab24a8e) + B₁ + B₂ naming rigor pass (commit 8e6a5b2)" preamble + "See core/terms/terms_index.md Accountability Bond v1.2 record" reference + "Source rigor passes: B = B₁ + B₂ decomposition (commit ab24a8e); B₁ + B₂ naming — Restitution + Foreclosure (commit 8e6a5b2)" all removed. Net diff +67 / -40 lines (+27 net). Publisher-facing-clean per WP#8 + WP#10. | none directly (advances Phase α.2.7 final batch; B₁/B₂ formal definitions now in publisher-facing layer per WP#10 cross-layer flow — internal terms_index drafts feed external Tech Appendix; §5 section-numbering consistent with §10 + §15 + §16 naming pattern) |
| 2026-05-02 | α | **Phase α.2.7b batched commit** — Tech Appendix v1.0.0 comprehensive WP#8 scaffolding-scrub of audit-trail / version-archaeology / cross-reference-to-internal-scaffolding content. Net diff **+32 / -576 lines (-544 effective)**. Removed: status-block "CURRENT at v1.0.0 (Scope 2 of 7)" + Scope-progress checklist + "Note on naming" terms_index-§0 cross-reference; entire #preamble section (duplicate header + version-archaeology "What changed from previous version" + "v0.0.5 additions" + stale "Sections: A. ... M." letter-anchor list with broken anchors); §2/§3/§6/§11/§16 "Sources:" preamble blocks (rigor-pass commit hashes + partial-integration provenance); §5.4 Parfit Source/Cross-reference scaffolding + Ch 6 supplementary-drafts file-path refs; §6.1.1 + §6.1.2 M11 Character probe scaffolding (Char 12 graduate-student + Char 17 Ostrom-successor) + tools/rigor-passes/ paths; §7 Four Gates + Asymmetric Regret "Backed by ... rigor pass" + "Source rigor pass" lines; §7.3 "Same-day-flip lesson (from rename rigor pass)" + Reading-discipline note (entire end-of-Phase-B partial-integration block); §12 Boundary-Awareness "Note on reframing" rigor-pass-commit ref; §13 Substitutability Function "Sources" with CSG-retirement commit ref; §15.1.1 + §15.1.9 M12/Working-Principle-#6/Ring-1-rigor-pass-commit-d4c4be4 references; all eight §15.1.x "Rigor-pass record:" blocks (CIT rename + Commons-as-Structural-Identity + Three-Ways-RCV-Formal-Model + CSD individual + B₁/B₂ decomposition + Hotelling Identity individual + Three-Ways individual + Four-Gates cluster + Term-Consistency-Gate-Rename + Path-F-Variable-Addability + 10-Commons-List-Dissolution + ARP rename + academic-rigor-full-test). Plus inline parenthetical scrubs: "(per the commons-as-structural-identity rigor pass, commit c4b09dc)"; "(per Open Insight #14)" ×3; "(per Working Principle #5: context-flipping rules earn named-rule status)"; "(per Insight #2 closed-ratified 2026-04-26 Term Consistency Gate Rename rigor pass)"; "(Open Insight #19)" sub-section-heading parenthetical. Plus §C.2 abundance-list reframing: "Habitability abundance / Spatial abundance / etc." → "Habitability commons (abundant state) / Spatial commons (abundant state) / etc." per Path F reframing discipline; FGC reference removed (RETIRED term); §C.2 epilogue paragraph added documenting Path F discipline + v1.3.0 ten-cohort note + Phase B integration of three additional dimensions. Plus HTML-entity error fix: "&amp;amp;" → "&amp;" in §19 title (TOC + section header) per author flag. Residual scaffolding: 17 refs remain (most in §18 "Working Principles + Open Insights Cross-Reference" meta-section + §19 Provenance & Cross-References — handled in α.2.7d bibliography sweep). | none directly (advances Phase α.2.7 final batch; Tech Appendix now meets WP#8 publisher-facing-scrub discipline in body sections; meta-sections §18-§19 + bibliography pass remain for α.2.7d) |
| 2026-05-02 | α | **Phase α.2.7c batched commit** — Content absorption from `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` → Tech Appendix §C.2 + new §C.2.1 (per-category profiles). Net diff +81 / -3 lines in Tech Appendix HTML; plus file move (`core/dimensions/` → `archive/dimensions/`) + directory removal + Tier-2 header-note per WP#4 + retirement-archive index update §3 row marking absorption complete (was QUEUED). **§C.2 list extended from 7 → 10 commons categories** (added Cohesion + Epistemic + Autonomy with abundant-state↔scarcity-grounded-cost readings). **New §C.2.1 Per-category profiles section:** academic-summary depth profile per commons category — Habitability (life-support substrate; Daly + Costanza + Rockström + Stern lineage); Spatial (geographic/place-access; Tuan + Jacobs + Bullard); Temporal (multi-generational availability; Hartwick + Brundtland + Brown Weiss); Institutional (governance + accountability; North + Acemoglu-Robinson + Stigler + Mann + Tilly); Kindred (identity-deep specific bonds; Weston + Coulthard + Tuck-Yang + intergenerational-trauma scholarship); Ecosystem (biospheric services; Daily + Costanza + planetary boundaries); Political (democratic-process infrastructure; Stigler + Olson + Acemoglu-Robinson); Cohesion (civic-trust / non-kin coordination; Putnam + Coleman + Ostrom + Tönnies + Klinenberg); Epistemic (evidence/knowledge access; Akerlof + Fricker + Hess-Ostrom + Habermas + AI-ethics literature; Kantian-pair with Autonomy); Autonomy (non-coerced choice; Kant + Mill + Sen + Nussbaum + Anderson; Kantian-pair with Epistemic). **Discipline note added:** the 10 categories are illustrative organizational scaffolding (Path F + Option C' commons-as-structural-identity discipline), not closed ontological taxonomy — the framework's job is methodology (CIT + Four Gates); a political-philosophical tradition supplies the candidate commons. Publisher-facing-clean per WP#8 + WP#10. | none directly (advances Phase α.2.7 final batch; `core/dimensions/` directory absorbed + archived; retirement-archive index §3 entry updated from QUEUED to complete) |

---

## §6. Parallelism reality check

**True-parallel cases (independent author attention):**
- Thread α (architectural work, derive-from-terms_index pipelines) ⊥ Thread β (drafting work, conversational mode)
- Thread γ (hygiene) ⊥ everything (mostly read-only-with-targeted-writes)
- Thread δ (discussion) ⊥ everything (low-edit, conversation-mode)

**Sequential within thread:**
- α: α.1 → α.2 → α.3 (each derives from prior)
- β: β.1 → β.2 (β.1 produces word-count gaps for β.2); β.3 has α-dependency note; β.4 independent
- γ: γ.1 ⊥ γ.2 within thread; γ.2 execution gated by α.2 + α.3

**Realistic-throughput cases:** running α + β + γ simultaneously across separate sessions is feasible. δ runs as conversation between sessions. The hard constraint is author attention — each thread requires author engagement at insight-ratification points.

---

## §7. Cross-references

- **Full state-snapshot:** [`alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md)
- **Working principles:** [`alignment/commons_bonds_working_principles_v1.0.0.md`](alignment/commons_bonds_working_principles_v1.0.0.md) (WP#9 NEW + WP#4 REFINEMENT 2026-04-30)
- **Open insights log:** [`alignment/commons_bonds_open_insights_v1.0.0.md`](alignment/commons_bonds_open_insights_v1.0.0.md)
- **Retirement archive:** [`archive/retirements/index.md`](archive/retirements/index.md)
- **Vocabulary strategy:** [`alignment/commons_bonds_vocabulary_strategy_v1.0.1.md`](alignment/commons_bonds_vocabulary_strategy_v1.0.1.md) (§3.1 Tier disambiguation note 2026-04-30)

---

**End of session handoff v1.49.0 — Parallel Execution Plan.**

**Next session start (any thread): read v1.48.0 + v1.49.0 §3.<thread>; surface thread-scoped first-action for author confirmation before edits.**
