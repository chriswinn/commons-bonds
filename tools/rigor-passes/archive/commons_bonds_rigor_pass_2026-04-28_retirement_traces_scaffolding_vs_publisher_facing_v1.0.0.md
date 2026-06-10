# Commons Bonds — Focused Rigor Pass: Retirement Traces — Scaffolding vs Publisher-Facing

**Version:** 1.0.0
**Date:** 2026-04-28
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — focused subset (M3 book/artifact scope, M6 academic, M8 test-of-time, M10 publishing, M11 critic survival, M12 intellectual honesty). Full 12-module suite not required — this is a refinement/extension of an already-ratified principle (Principle #4) rather than a new claim.

**Scope:** Refines Working Principle #4 (*Retirements preserve their history in-document*, ratified 2026-04-24) by surfacing a missing third tier — **scaffolding / decision-record documents** — that the existing Tier 1 / Tier 2 dichotomy elides. Provides per-folder classification across the repo. Triggered by the Value Capture sweep scope question (2026-04-27 → 2026-04-28).

**Status:** **RATIFIED 2026-04-28 by Chris Winn** — verdict (a) full ratify A2 + L2 + S1 (Tier 3 trichotomy with explicit per-folder classification + per-instance lowercase judgment + Tier-aware sentinel exclusion).

**Author:** Chris Winn (originating articulation 2026-04-28 while drifting off: *"perhaps this is the sort of thing that's perfect to keep living in scaffolding along with reasons that we regressed the use of that term/word/etc. and that means the publisher facing documents will be scrubbed clean"*).

**Ratified verdict:** **Option A — Tier 3 trichotomy with explicit per-folder classification.** Preserves audit trail discipline while clarifying which documents get scrubbed at retirement. Triggers Phase 1 (Working Principle #4 update — add Tier 3 row), Phase 2 (Value Capture → Value Extraction publisher-facing sweep per §4 plan), Phase 3 (routine 1 Tier-aware exclusion update + add `\bValue Capture\b` regression pattern).

---

## §1. Executive summary

**RECOMMENDED:** Adopt **Option A** — extend Working Principle #4's Tier 1 / Tier 2 dichotomy with a third tier:

- **Tier 1 — Reader-facing (publisher-facing) live documents** → SWEEP retired terms (replace with current term where applicable; remove + rewrite where no replacement exists). Same as existing Principle #4 Tier 1.
- **Tier 2 — Reader-facing archived / superseded versions** → header-note retirement annotation; body intact. Same as existing Principle #4 Tier 2.
- **Tier 3 — Scaffolding / decision-record / author-facing documents** (NEW) → preserve all retirement traces in full. These documents *are* the audit trail. Sweeping them destroys the reasoning chain. New work uses current vocabulary; retired-term historical references stay.

**Why this is a refinement, not a new principle:** Principle #4's table already implicitly recognizes Tier 3 in one row — *"For documents that are PRIMARILY about vocabulary (Terms Index itself, glossary, rigor passes, provenance records) — no header note needed; they're already the reasoning-chain docs."* This rigor pass makes that "PRIMARILY about vocabulary" carve-out explicit, generalizes it beyond vocabulary-authoritative documents to all decision-record / scaffolding artifacts, and provides a per-folder classification.

**Decisive findings:**

1. **Principle #4's table has a coverage gap.** The existing principle classifies "active chapter drafts" + "active glossary" + "active Technical Appendix" + "active audit docs" as Tier 1 (sweep). It classifies "archived sessions" + "archived rigor passes" + "archived audits" as Tier 2 (header note only). But CURRENT scaffolding artifacts — `core/terms/terms_index.md`, `tools/rigor-passes/*.md` (still being authored), `alignment/commons_bonds_open_insights_v1.0.0.md`, `alignment/commons_bonds_working_principles_v1.0.0.md`, `alignment/sessions/*.md` (current handoffs) — fall through. They're CURRENT (so not Tier 2), but sweeping them destroys the audit trail.

2. **The architecture rigor pass (2026-04-27, A2 + S1 + B1 + M1 ratified) already established the upstream-source-of-truth dichotomy.** terms_index = internal source-of-truth. Glossary + Tech Appendix = publication artifacts derived downstream. This rigor pass extends that dichotomy to *all* repo content: **internal/scaffolding** (preserve traces) vs **publication/reader-facing** (scrubbed clean).

3. **Value Capture sweep concrete instance.** As of 2026-04-28, Value Capture (RETIRED 2026-04-24) appears in 14 active files with 37+ instances. A naive Phase A3 sweep would touch all of them — including Insight #7 in Open Insights (the decision record), Principle #4's worked example in Working Principles, and the rigor pass that ratified the retirement. The trichotomy resolves the scope: sweep Tier 1 only; preserve Tier 3 in full.

4. **Lowercase / non-framework-sense uses warrant per-instance judgment.** Several "value capture" / "value captured" instances in research/case-studies are descriptive English, not framework-Value-Capture references (e.g., `norway-swf.md:56` — *"the total financial value captured on behalf of the national community"* meaning state-internalized rents, not the framework's causal-event term). Sweeping these to "value extraction" would change meaning, not just vocabulary. The rigor pass formalizes per-instance judgment for lowercase prose uses.

5. **Routine 1 (terminology-regression sentinel) needs Tier-aware pattern logic.** Currently routine 1 excludes specific paths (terms_index SUPERSEDED+RETIRED records, rigor-passes, sessions/archive/, etc.) but the exclusion list is ad-hoc. Reframing to "exclude all Tier 3 scaffolding paths" gives routine 1 a principled exclusion rule that scales to future retirements without per-term routine updates.

**Net verdict:** Adopt the Tier 3 extension. Strengthens M3 (publisher-facing artifacts properly scrubbed) + M6 (academic audit trail intact) + M8 (durable retirement-handling discipline) + M11 (critic encountering retired term in chapter sees it swept; encountering retired term in rigor pass sees the decision record) + M12 (intellectual honesty preserved at the audit-trail level).

---

## §2. The question under test

### §2.1 Triggering context (2026-04-27 → 2026-04-28)

Author asked (2026-04-27): *"Go ahead and completely remove Value Capture and we have switched to using Value Extraction."*

Surfaced scope ambiguity: 37+ instances across 14 active files, including (a) live chapter prose, (b) the decision record itself (Insight #7), (c) Working Principle #4's worked example, (d) the rigor pass that ratified the retirement, (e) lowercase descriptive English uses that aren't framework references.

Author response (2026-04-28, drifting off): *"hmm, actually let me not make this call half awake as I'm drifting off. Perhaps this is the sort of thing that's perfect to keep living in scaffolding along with reasons that we regressed the use of that term/word/etc. and that means the publisher facing documents will be scrubbed clean."*

That articulation surfaced a missing structural distinction in Principle #4 that this rigor pass tests + formalizes.

### §2.2 The question

**Q1 (architecture):** Does Working Principle #4's Tier 1 / Tier 2 dichotomy fully cover the project's retirement-handling needs, or is a third tier required?

**Q2 (classification):** If Tier 3 is added, how do we classify each folder/document type unambiguously?

**Q3 (Value Capture):** Given the Tier classification, which of the 37+ Value Capture instances get swept? Which preserved? Which need per-instance judgment?

**Q4 (sentinel):** How does routine 1's exclusion logic update to be Tier-aware so it scales to future retirements?

### §2.3 Options under test

**Architecture (Axis A):**
- **A1:** Status quo — keep Principle #4's Tier 1 / Tier 2 dichotomy unchanged. Treat scaffolding case-by-case at retirement time.
- **A2 (RECOMMENDED):** Extend with explicit Tier 3 (scaffolding / decision-record / author-facing) — preserve all traces.
- **A3:** Collapse to dichotomy at a different cleavage line — "publisher-facing live = sweep; everything else = preserve" (drops the archived-vs-scaffolding distinction).

**Lowercase-prose handling (Axis L):**
- **L1:** Sweep all instances regardless of case (machine-only).
- **L2 (RECOMMENDED):** Per-instance judgment for lowercase; sweep proper-noun forms uniformly. Lowercase "value capture" / "value captured" is reviewed for framework-vs-descriptive-English sense.
- **L3:** Sweep proper-noun only; leave all lowercase as-is.

**Sentinel update (Axis S):**
- **S1 (RECOMMENDED):** Routine 1 exclusion list reframed to "Tier 3 scaffolding paths" (principled rule that scales).
- **S2:** Add Value Capture-specific exclusion entries to routine 1 (term-by-term ad-hoc).

---

## §3. Per-folder Tier classification

Based on the Tier 3 extension, here is the proposed classification for the Commons Bonds repo:

### Tier 1 — Reader-facing (publisher-facing) live documents — SWEEP

| Path | Notes |
|---|---|
| `manuscript/chapters/*Draft.{md,html}` | The book itself. Reader-facing. Sweep retired terms. |
| `core/glossary/archive/commons_bonds_updated_glossary_v3.html` | Current glossary. Reader-facing reference. Sweep. |
| `core/technical-appendix/TechnicalAppendix_v1.0.0.html` | Current Tech Appendix. Reader-facing. Sweep. (Note: scheduled for v2.0.0 rebuild that will derive from terms_index, which is itself the cleanest sweep mechanism.) |
| `research/case-studies/*.md` | Currently feeds chapter prose. Treat as Tier 1 because content flows to publisher-facing chapters. **Per-instance judgment required (Axis L2)** for lowercase descriptive uses. |
| `tools/audits/commons_bonds_case_study_audit_v1.0.6.md` | Active audit doc. **Per Principle #4 table = Tier 1.** Re-examined here: this is an author-facing scaffolding tool, but it's the document the author USES to audit case studies for current vocabulary. Decision: **stays Tier 1** because it should reflect current vocabulary — a future audit pass shouldn't see retired terms as "currently active." Historical references to retired terms (e.g., "previously called Value Capture") may be left if they preserve a reasoning chain; but pattern-match references should sweep. |

### Tier 2 — Reader-facing archived / superseded versions — header-note annotation only

| Path | Notes |
|---|---|
| `core/glossary/archive/commons_bonds_updated_glossary_v2.html` | Superseded prior glossary version. Header note pointing to v3 + terms_index. |
| `core/technical-appendix/archive/*.html` | Superseded Tech Appendix versions. Header note. |
| `alignment/sessions/archive/*` | Archived session handoffs. Header note. |
| `tools/archive/*` | Archived rigor protocol versions, etc. Header note. |
| `core/decomposition/eight-tier-v10.html` | Pre-retirement scaffolding. Header note (already partially annotated). |

### Tier 3 — Scaffolding / decision-record / author-facing — PRESERVE FULL TRACES (NEW)

**Note (added 2026-04-28 per Working Principle #8 ratification):** the Tier 1 / Tier 3 split established here for retirement-trace handling generalizes to ALL scaffolding/audit-trail content per Working Principle #8 (`alignment/commons_bonds_working_principles_v1.0.0.md`). Publisher-facing artifacts are scrubbed not only of retired-term references but of all audit-trail content (rigor-pass commit references, M11 probes, decision-record narratives, status indicators in prose, author-meta-notes, version-progression archaeology). Reasoning chains for ALL framework decisions live in Tier 3 scaffolding documents.

| Path | Notes |
|---|---|
| `core/terms/terms_index.md` | The vocabulary source-of-truth. RETIRED records are scaffolding-by-design. Preserve in full. (Already Principle #4 Tier 1 in the existing table, but the existing rule says "full RETIRED record with rigor-pass link" — i.e., trace preserved within the entry. This rigor pass affirms that pattern under Tier 3.) |
| `tools/rigor-passes/*.md` (current + past) | Each rigor pass is a decision record. They reference retired terms by name as part of the decision context. Preserve in full. The `term_value_capture_vs_extraction` rigor pass IS the Value Capture retirement document. |
| `tools/commons_bonds_rigor_protocol_v*.md` (current) | The rigor protocol itself. Author-facing methodological scaffolding. May reference retired terms in worked examples. Preserve. |
| `alignment/commons_bonds_working_principles_v*.md` | Principle examples reference retired terms by design (Principle #4 uses Value Capture as worked example). Preserve. |
| `alignment/commons_bonds_open_insights_v*.md` | Insight records (e.g., Insight #7 = Value Capture decision) ARE the decision record. Preserve. |
| `alignment/sessions/*.md` (current handoffs) | Session handoffs document in-flight project state. Reference retired terms when work was done on them. Preserve. |
| `alignment/patches/*.md` | Patch decision records. Preserve. |
| `tools/routines/proposed_routines_v*.md` | Routine drafts. Reference retired-term patterns by design. Preserve. |
| `core/scaffolding/*` (if/when created per architecture rigor pass) | Internal-only docs split off from Tech Appendix. Scaffolding by design. Preserve. |

### Edge cases / tier-judgment notes

- **`tools/audits/commons_bonds_case_study_audit_v1.0.6.md`** — placed in Tier 1 above with per-instance reasoning. Author's call.
- **`research/case-studies/*.md`** — placed in Tier 1; per-instance judgment for lowercase. Author's call.
- **Mixed-content alignment files** — when a current alignment file (Tier 3) gets bumped to a new version, the old version moves to Tier 2 (archived). Standard versioning lifecycle.

---

## §4. Value Capture concrete sweep plan (under Option A2 + L2 + S1)

Given the Tier classification and Axis-L2 lowercase discipline, here's the sweep plan for Value Capture:

### Tier 1 sweeps (per file)

| File | Instances | Plan |
|---|---|---|
| `manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md` | 1 | Sweep proper-noun → Value Extraction. |
| `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` | 4 | Sweep proper-noun → Value Extraction; lowercase per-instance review. |
| `core/glossary/archive/commons_bonds_updated_glossary_v3.html` | 2 | One is Cost-Severance entry prose ("separates value capture from cost bearing") — sweep to "value extraction." Other is the standalone "Value Capture" term entry at line 337 — **remove or rewrite as RETIRED-pointer to Value Extraction**. (Glossary v4 rebuild will derive from terms_index cleanly; until then v3 patches.) |
| `tools/audits/commons_bonds_case_study_audit_v1.0.6.md` | 4 | Sweep proper-noun; lowercase per-instance review. |
| `research/case-studies/indigenous-land-dispossession.md` | 1 | Per-instance review. |
| `research/case-studies/ancient-egypt-pyramids.md` | 1 | Per-instance review. |
| `research/case-studies/mondragon-cooperative.md` | 1 | Per-instance review. |
| `research/case-studies/norway-swf.md` | 3 | Per-instance review. **Confirmed:** at least 2 of 3 are descriptive English ("financial value captured" / "value capture paired with the transfer of costs") — leave or rewrite to lowercase non-framework prose. |
| `research/case-studies/deepwater-horizon.md` | 1 | Per-instance review. |

### Tier 3 preserves (no sweep — verify trace integrity)

| File | Instances | Plan |
|---|---|---|
| `core/terms/terms_index.md` | RETIRED record (lines 611-650) | Preserve. Already authoritative retirement record. |
| `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` | All instances | Preserve. This IS the retirement decision document. |
| `tools/rigor-passes/*.md` (other 5+ rigor passes referencing Value Capture) | All instances | Preserve. Decision records. |
| `tools/commons_bonds_rigor_protocol_v2.2.0.md` | 1 | Preserve. |
| `alignment/commons_bonds_working_principles_v1.0.0.md` | 5 | Preserve. Principle #4 worked example. |
| `alignment/commons_bonds_open_insights_v1.0.0.md` | 10 | Preserve. Insight #7 = Value Capture decision. |
| `alignment/patches/principle_7_retroactive_scan_2026-04-26.md` | 1 | Preserve. |
| `alignment/patches/pending-framework-review/c3_mechanism_shield_patch.md` | 2 | Preserve. |
| `alignment/sessions/*.md` (current handoffs) | (multiple) | Preserve. |

### Tier 2 (archived) — verify header notes

| File | Status |
|---|---|
| `core/glossary/archive/commons_bonds_updated_glossary_v2.html` | Has standalone "Value Capture" entry. Per Tier 2: keep entry intact + add header note to v2 file referencing v3 + terms_index. |
| `alignment/sessions/archive/*` | Per Tier 2: header notes for retirement batch (already partially in place per Principle #4 ratification). |

### Estimated effort

- Tier 1 publisher-facing sweep: ~2 hours (chapter edits + glossary v3 patches + per-instance research case-study review)
- Tier 2 verification: ~30 min (check header notes are present)
- Tier 3 verification: 0 min (preserve)
- Routine 1 update (Axis S1): ~15 min
- **Total: ~2.5-3 hours**

---

## §5. Routine 1 update (Axis S1)

Reframe routine 1's exclusion list from ad-hoc per-path entries to a principled "Tier 3 scaffolding" exclusion rule:

**Current exclusions in routine 1 prompt:**
> *Exclusions (do NOT flag): terms_index.md SUPERSEDED+RETIRED records · tools/rigor-passes/* historical-record files · core/scaffolding/* · alignment/sessions/archive/* · core/decomposition/eight-tier-v10.html · glossary entries flagged with RETIRED status.*

**Proposed reframed exclusions (Tier-aware):**
> *Exclusions (do NOT flag): all Tier 3 scaffolding paths per `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-28_retirement_traces_scaffolding_vs_publisher_facing_v1.0.0.md` §3 — specifically: `core/terms/terms_index.md` · `tools/rigor-passes/*.md` · `tools/commons_bonds_rigor_protocol_v*.md` · `alignment/commons_bonds_working_principles_v*.md` · `alignment/commons_bonds_open_insights_v*.md` · `alignment/sessions/*.md` · `alignment/patches/*.md` · `tools/routines/*.md` · `core/scaffolding/*`. Tier 2 archived paths excluded: `alignment/sessions/archive/*` · `core/glossary/*v2*.html` · `core/technical-appendix/archive/*` · `tools/archive/*` · `core/decomposition/eight-tier-v10.html`. Sweep ONLY Tier 1 publisher-facing live docs: `manuscript/chapters/*Draft.{md,html}` · `core/glossary/archive/commons_bonds_updated_glossary_v3.html` · `core/technical-appendix/TechnicalAppendix_v1.0.0.html` · `research/case-studies/*.md` · `core/case-studies/*current*.md`.*

**Pattern additions:**
Add `\bValue Capture\b` to retired-vocabulary patterns (proper-noun only — lowercase requires judgment per Axis L2; routine 1 should not flag lowercase "value capture" / "value captured").

---

## §6. M11 critic-survival probe

**Critic prompt:** *"You're proposing a third tier of retirement-handling that wasn't in the original ratified principle. How do we know this isn't post-hoc rationalization to dodge the work of sweeping rigor passes + working principles + open insights?"*

**Response:**
1. **Already implicit in Principle #4 itself.** Principle #4 already says: *"For documents that are PRIMARILY about vocabulary (Terms Index itself, glossary, rigor passes, provenance records) — no header note needed; they're already the reasoning-chain docs."* That's the Tier 3 carve-out, framed only for active-use traceability. The current rigor pass generalizes it to retirement-trace handling.

2. **Architecture rigor pass A2 ratified the same dichotomy.** terms_index = internal source-of-truth + scaffolding fields. Glossary + Tech Appendix = publication artifacts. The architecture rigor pass split internal-only fields (rigor_provenance, decision_history) from rendering fields (glossary_definition, tech_appendix_definition). That same split applies to retirement-trace handling.

3. **The rigor passes themselves are the audit trail.** Sweeping retired terms out of rigor passes destroys the reasoning chain a future reader (academic reviewer, publisher, future self) follows. *"This term was retired in 2026-04-24 because..."* — if the supporting rigor pass no longer mentions the term, the audit chain breaks. M6 + M11 + M12 all argue for preservation.

4. **Tier 3 is more conservative, not less.** It does *more* work, not less — it requires per-folder classification and an explicit discipline. Naive sweep would be the lazy path. This rigor pass takes the discipline-heavier route.

**Critic counter-prompt:** *"Why not just version-bump current scaffolding files (working principles, open insights) and treat the new version as Tier 1, sweeping retired terms while preserving the old version as Tier 2?"*

**Response:** That works for *retired-term scrubbing in current scaffolding* but at the cost of constant version bumps that don't track meaningful conceptual change. Working Principles v1.0.0 evolved through ratification; bumping to v1.0.1 just to scrub Value Capture from one example sentence doesn't reflect a substantive evolution. The Tier 3 discipline preserves the document at its current version with the trace intact — readers see Principle #4's worked example *as the trace itself*. That's stronger pedagogy.

---

## §7. Decision matrix

| Axis | Option | Verdict | Strength |
|---|---|---|---|
| A (architecture) | A2 — Tier 3 trichotomy | RECOMMENDED | High (refines existing principle; matches architecture rigor pass) |
| A (architecture) | A1 — status quo dichotomy | NOT RECOMMENDED | Coverage gap surfaced |
| A (architecture) | A3 — alternate cleavage | NOT RECOMMENDED | Loses archived-vs-scaffolding distinction |
| L (lowercase) | L2 — per-instance judgment | RECOMMENDED | Avoids meaning-change errors |
| L (lowercase) | L1 — uniform sweep | NOT RECOMMENDED | Will rewrite descriptive English incorrectly |
| L (lowercase) | L3 — proper-noun only | NOT RECOMMENDED | Misses lowercase framework references |
| S (sentinel) | S1 — Tier-aware exclusion | RECOMMENDED | Scales to future retirements |
| S (sentinel) | S2 — term-by-term ad-hoc | NOT RECOMMENDED | Linear maintenance cost |

---

## §8. Implementation plan (post-ratification)

### Phase 1 — Update Working Principle #4 (10 min)

In `alignment/commons_bonds_working_principles_v1.0.0.md`:
- Add Tier 3 row to the Per-document-type format table (between current Tier 1 + Tier 2 rows).
- Add cross-reference pointer to this rigor pass.

### Phase 2 — Tier 1 Value Capture sweep (~2 hours)

Per §4 plan above. Per-instance judgment for lowercase prose uses.

### Phase 3 — Routine 1 update (15 min)

Update routine 1's prompt body via `RemoteTrigger` action `update` with the reframed Tier-aware exclusion list per §5. Add `\bValue Capture\b` to pattern list.

### Phase 4 — Future retirements adopt Tier 3 discipline by default

Going forward, every retirement rigor pass invokes this Tier 3 framework. The retirement-handling becomes routine: classify per Tier; sweep Tier 1; verify Tier 2 header notes; preserve Tier 3 in full; update routine 1's pattern list (proper-noun only).

---

## §9. Verdict candidates summary (for ratification)

**Author choice required:**

- **(a) Full ratify A2 + L2 + S1** — adopt Tier 3 trichotomy, per-instance lowercase judgment, Tier-aware sentinel. Full implementation per §8. *(RECOMMENDED.)*
- **(b) Ratify A2 only; L1 (uniform sweep)** — adopt Tier 3 but sweep all lowercase regardless of sense. Faster, but will introduce meaning-shift errors in research/case-studies prose that need cleanup.
- **(c) Ratify A1 status quo; case-by-case** — keep dichotomy, handle each retirement case-by-case. Compatible with current Principle #4; doesn't formalize Tier 3.
- **(d) Modify recommendation** — author specifies different cleavage line or per-folder reclassification.

---

## §10. Open questions for ratification

1. **`research/case-studies/*.md` Tier classification.** §3 places these in Tier 1 (reader-facing-adjacent because content flows to chapters). Alternative: Tier 3 if treated as raw research that gets quoted/paraphrased into chapters with author judgment per quote. Author's call.

2. **`tools/audits/commons_bonds_case_study_audit_v1.0.6.md` Tier classification.** §3 places in Tier 1 per existing Principle #4 table. Alternative: Tier 3 if treated as author-facing scaffolding for the case-study writing process. Author's call.

3. **Should the Tier classification go in working_principles_v1.0.0 itself, or stay in this rigor pass?** §8 Phase 1 proposes adding a Tier 3 row to Principle #4's table; an alternative is to add the per-folder classification table inline to working_principles. Trade-off: inline = single-source; rigor-pass-only = principle stays compact + classification stays separately versionable. RECOMMENDED: inline the Tier-3 ROW to Principle #4 table; keep the per-folder classification in this rigor pass (which gets cross-referenced).

---

**End of rigor pass v1.0.0 (PROPOSED).**
