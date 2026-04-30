# Commons Bonds — Working Principle #4 Refinement: Tiered Retirement-Trace Policy + Retirement-Archive Index

**Version:** 1.0.0
**Date:** 2026-04-30
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — focused rigor pass on Working Principle #4 retirement-trace discipline; tests 5 alternatives against framework's evolving needs (publisher-prep phase; Phase 3 Tech Appendix v2.0.0 + Phase 4 Glossary v4 rebuilds; pre-publication external review).

**Author direction triggering this pass (2026-04-30 by Chris Winn):** *"Should I change the framework's discipline of keeping retirement traces in scaffolding documents?"* → upon recommendation: *"ratify as recommended."*

**Scope:** Refine WP#4 retirement-trace discipline as the framework matures from work-in-progress phase to publisher-prep phase. Tests 5 alternative disciplines; recommends Tiered B + Archive C combined approach.

**Status:** **RATIFIED 2026-04-30 by Chris Winn — verdict: Tiered retirement-trace policy + dedicated retirement-archive index (Options B + C combined).**

**Author:** Chris Winn

**Recommended verdict (preview):** **Refine WP#4 to a tiered discipline + create dedicated retirement-archive index.** Preserves provenance + reversibility + M12 honesty (the discipline's purpose) while reducing scaffolding-doc bloat + improving navigability for publisher-prep + Phase 3+4 rebuild derivation work.

---

## §1. Executive summary

### §1.1 Why this refinement now

Working Principle #4 was ratified in the framework's rapid-development phase (Apr 22-29 ratifications cycle). The discipline solved real problems:
- Provenance tracking when decisions were rapidly evolving
- Reversibility (CSG renaming case; ARP→ARR same-day flip; Reparations Bond → Restitution Bond)
- M12 attribution-honesty for academic lineage
- Context-collapse prevention

The framework is now mature enough that **the discipline's costs are starting to outweigh its benefits in some places:**
1. terms_index approaching v1.0.0 with substantial retirement-trace metadata; Phase 3 Tech Appendix v2.0.0 rebuild + Phase 4 Glossary v4 rebuild derive from it; rebuild inherits the noise.
2. Pre-publication external review (Insight #39) — reviewer wants current state; heavy traces are friction.
3. Scaffolding doc navigability declining as retirement annotations accumulate.
4. Routine 1 retired-vocabulary patterns growing (8 patterns: FGC; AIT; Reparations Bond; ARP; CSG; Spatial Cost Severance; Eight-tier; Dynastic Labor Cost).

### §1.2 The tiered policy ratified

| Document type | Retirement-trace policy |
|---|---|
| **Open insights / pending rigor passes** | Full traces (active discipline; status quo) |
| **Ratified rigor passes (frozen)** | Full traces preserved as historical record (status quo; self-archiving by date in filename) |
| **Working principles** | Light traces in body; cross-reference retirement archive index |
| **Vocabulary strategy v1.0.1** | Light traces in §6 + §7 + §13 ledger; cross-reference retirement archive index |
| **terms_index v1.0.0+** | SUMMARY-level traces (1-line "renamed YYYY-MM-DD per Insight #N"); full traces in retirement archive index |
| **Publisher-facing (Tier 1 per WP#8)** | NO traces (status quo) |
| **Tier 2 archived/superseded files** | Header-note only (status quo) |

PLUS: dedicated **`archive/retirements/index.md`** as canonical retirement-archive index.

### §1.3 What this preserves

- **Provenance** — preserved via retirement archive index + ratified rigor passes
- **Reversibility** — preserved (rigor passes that ratified retirements remain canonical)
- **M12 attribution-honesty** — preserved (academic lineage stays in rigor passes + vocabulary strategy)
- **Academic peer review** — *improved* (current-state visible; full audit trail still accessible)
- **Routine 1 sentinel** — preserved (still catches retired-vocabulary regression)

### §1.4 What this changes

- **terms_index v1.0.0** reads as current-state document, not retirement-trace catalog
- **Working principles** + **vocabulary strategy** less cluttered
- **Phase 3 + Phase 4 rebuilds** derive from cleaner sources
- **Pre-publication external reviewer** sees current state cleanly; full audit trail accessible via retirement archive

---

## §2. Question + scope

### §2.1 Triggering articulation

Per author direction 2026-04-30: *"Should I change the framework's discipline of keeping retirement traces in scaffolding documents?"*

The question surfaced after Group 1 ratification batch + Insight #55 cleanup work, where retirement-trace volume across scaffolding docs became visible.

### §2.2 What this rigor pass tests

For each of 5 alternative disciplines:
1. **Provenance preservation** — does it preserve the discipline's primary purpose?
2. **Reversibility** — can decisions still be revisited cleanly?
3. **M12 attribution-honesty** — academic lineage preserved?
4. **Navigability** — can current-state info be found efficiently?
5. **Phase 3 + Phase 4 rebuild compatibility** — does rebuild derivation work cleanly?
6. **Pre-publication external review compatibility** — reviewer sees what they need?
7. **Routine 1 + 2 sentinel compatibility** — automated retirement detection still works?

### §2.3 Pass/fail gate framing

This is a Working Principle revision — load-bearing for the framework. Effort-to-repair (sweeping scaffolding to apply tiered policy) is **excluded as verdict input** per Working Principle #1.

---

## §3. Methodology

5 alternatives tested per dimension. Comparative scoring. Recommended verdict driven by:
- Provenance + reversibility + M12 preservation
- Navigability improvement
- Compatibility with Phase 3 + Phase 4 + pre-publication external review work
- Implementation feasibility

---

## §4. Alternatives tested

### §4.1 Option (A) — Status quo

Keep WP#4 unchanged. Full retirement traces preserved in all scaffolding documents.

| Dimension | Verdict |
|---|---|
| Provenance preservation | STRONG |
| Reversibility | STRONG |
| M12 attribution-honesty | STRONG |
| Navigability | **WEAK** (and getting worse) |
| Phase 3+4 rebuild compatibility | ADEQUATE |
| Pre-publication external review compatibility | ADEQUATE |
| Routine 1+2 compatibility | STRONG |

**Verdict:** REJECTED. Status quo solves provenance but at increasing cost to navigability + publisher-prep.

### §4.2 Option (B) — Tiered retirement-trace policy

Distinguish trace-density by document type:
- Active scaffolding (open insights; pending rigor passes): full traces
- Ratified rigor passes (frozen): full traces (self-archiving)
- Working principles + vocabulary strategy: light traces
- terms_index v1.0.0+: summary-level traces
- Publisher-facing: no traces (status quo per WP#8)

| Dimension | Verdict |
|---|---|
| Provenance preservation | STRONG (preserved in active + frozen rigor passes) |
| Reversibility | STRONG (rigor passes remain canonical record) |
| M12 attribution-honesty | STRONG (academic lineage stays in rigor passes) |
| Navigability | **STRONG** (current-state docs less cluttered) |
| Phase 3+4 rebuild compatibility | STRONG (cleaner derivation source) |
| Pre-publication external review compatibility | STRONG |
| Routine 1+2 compatibility | STRONG (sentinels still catch regressions) |

**Verdict:** STRONG. Addresses the navigability cost without losing provenance.

### §4.3 Option (C) — Retirement-archive index (standalone)

Move all retirement traces from scaffolding into a dedicated `archive/retirements/index.md`. Other scaffolding docs cite the archive but don't carry traces inline.

| Dimension | Verdict |
|---|---|
| Provenance preservation | STRONG (centralized in archive) |
| Reversibility | STRONG |
| M12 attribution-honesty | ADEQUATE (lineage citations in rigor passes; archive consolidates retirements) |
| Navigability | STRONG |
| Phase 3+4 rebuild compatibility | STRONG |
| Pre-publication external review compatibility | STRONG (one canonical archive to consult) |
| Routine 1+2 compatibility | ADEQUATE (sentinel patterns reference archive) |

**Verdict:** STRONG, but standalone is incomplete — needs to be paired with active-scaffolding policy (Option B). Together they're stronger than either alone.

### §4.4 Option (D) — Sunset clause on retirement traces

Preserve retirement traces for N months (e.g., 6 months) after retirement-date; then archive.

| Dimension | Verdict |
|---|---|
| Provenance preservation | ADEQUATE (depends on archive after sunset) |
| Reversibility | ADEQUATE (within sunset window; weaker after) |
| M12 attribution-honesty | ADEQUATE |
| Navigability | ADEQUATE (improves over time) |
| Phase 3+4 rebuild compatibility | ADEQUATE (depends on rebuild timing relative to sunset windows) |
| Pre-publication external review compatibility | ADEQUATE |
| Routine 1+2 compatibility | ADEQUATE |

**Verdict:** ADEQUATE. Time-based discipline introduces calendar-management overhead; doesn't cleanly distinguish active-vs-settled scaffolding.

### §4.5 Option (E) — Two-tier scaffolding

Distinguish "active scaffolding" (working principles; vocabulary strategy; current insights) from "decision-record scaffolding" (rigor passes; archived insights). Active gets light traces; decision-record gets full traces.

| Dimension | Verdict |
|---|---|
| Provenance preservation | STRONG |
| Reversibility | STRONG |
| M12 attribution-honesty | STRONG |
| Navigability | STRONG (active scaffolding cleaner) |
| Phase 3+4 rebuild compatibility | STRONG |
| Pre-publication external review compatibility | STRONG |
| Routine 1+2 compatibility | STRONG |

**Verdict:** STRONG. Functionally equivalent to Option B but with binary tiering rather than per-document-type granularity. Option B's per-document-type granularity is slightly cleaner for terms_index specifically.

### §4.6 Comparative scoring summary

| Option | Aggregate score | Key strength | Key weakness |
|---|---|---|---|
| (A) Status quo | 6 STRONG + 1 WEAK | Provenance | Navigability declining |
| **(B) Tiered policy** | **7 STRONG** | **Cleanest improvement on navigability** | Implementation work to apply across docs |
| (C) Archive-only | 5 STRONG + 2 ADEQUATE | Centralization | Incomplete without active-scaffolding policy |
| (D) Sunset clause | 0 STRONG + 7 ADEQUATE | Time-based simplicity | Calendar-management overhead |
| (E) Two-tier | 7 STRONG | Equivalent to B | Less granular than B |

**Top candidates:** (B) and (E) both score 7 STRONG. (B) preferred for per-document-type granularity. **(C) standalone is incomplete but valuable as supplement to (B).**

---

## §5. Recommended verdict

### §5.1 Verdict — Option (B) Tiered policy + Option (C) Retirement-archive index combined

**Refine Working Principle #4 to a tiered retirement-trace policy + create dedicated retirement-archive index.**

The combination preserves the discipline's purpose (provenance + reversibility + M12 honesty) while addressing the navigability cost as the framework matures.

### §5.2 Tiered policy specification

| Document type | Retirement-trace policy | Rationale |
|---|---|---|
| **Open insights** (`alignment/commons_bonds_open_insights_v1.0.0.md` insights with OPEN status) | Full traces | Active decisions; full context needed |
| **Pending rigor passes** ([PROPOSED] status) | Full traces | Active audit trails |
| **Ratified rigor passes** (frozen; in tools/rigor-passes/) | Full traces | Self-archiving via dated filenames; historical record |
| **Working principles** (alignment/commons_bonds_working_principles_v1.0.0.md) | Light traces in body; cross-reference retirement archive | Standing discipline document; current-state focus |
| **Vocabulary strategy v1.0.1** | Light traces in §6 + §7 + §13 ledger; cross-reference retirement archive | Standing discipline reference |
| **terms_index v1.0.0+** | Summary-level traces (1-line "renamed YYYY-MM-DD per Insight #N"); full traces in retirement archive | Phase 3+4 rebuild derivation source; current-state focus |
| **Publisher-facing artifacts** (chapter drafts; glossary; Tech Appendix) | No traces (status quo per WP#8) | Reader-facing; audit-trail content excluded |
| **Tier 2 archived/superseded files** | Header-note only (status quo) | Frozen historical record |

### §5.3 Retirement-archive index specification

Create new file: `archive/retirements/index.md`.

**Structure:**
```
# Commons Bonds — Retirement Archive Index

[Preamble explaining discipline]

## §1. Vocabulary retirements

| Date | Original term | Replacement / disposition | Insight # | Rigor pass | Reason |

## §2. Methodology retirements

[Same table format]

## §3. File / artifact retirements

[Same table format]

## §4. Cross-references

[Links to ratified rigor passes preserving full retirement traces]
```

**Initial population:** all known retirements from current scaffolding (FGC; AIT; Reparations Bond; ARP→ARR; CSG; Spatial Cost Severance; Eight-tier scheme; Dynastic Labor Cost → Lineage Labor Cost; etc.).

**Maintenance:** every new retirement adds a one-line entry. Routine 1 patterns reference the archive for remediation hints.

### §5.4 What this preserves vs changes

**Preserves:**
- Working Principle #4's purpose (provenance + reversibility + M12 honesty)
- Active scaffolding discipline (full traces during decisions)
- Ratified rigor passes as canonical decision-record (frozen + dated)
- Routine 1 retired-vocabulary regression sentinel
- Working Principle #8 publisher-facing scrub

**Changes:**
- terms_index v1.0.0+ reads as current-state document, not retirement-trace catalog
- Working principles + vocabulary strategy less cluttered with retirement annotations
- One canonical retirement-archive index (instead of distributed retirement traces)
- Phase 3 + Phase 4 rebuilds derive from cleaner sources

---

## §6. Implementation plan

### §6.1 Immediate (this commit)

1. **Update Working Principle #4** — revise discipline statement in `alignment/commons_bonds_working_principles_v1.0.0.md` to reflect tiered policy + cite retirement-archive index.

2. **Create `archive/retirements/index.md`** — initial structure + populated entries for known retirements (FGC; AIT; Reparations Bond; ARP→ARR; CSG; Spatial Cost Severance; Eight-tier; Dynastic Labor Cost; etc.).

3. **Insight #59 closed-ratified record** — capture WP#4 refinement verdict.

### §6.2 Subsequent (queued for Phase 3 + Phase 4 rebuilds + scaffolding cleanup)

1. **terms_index v1.0.0 version bump** — apply summary-level retirement traces; full traces moved to retirement archive index.

2. **Working principles body cleanup** — replace inline retirement traces with archive cross-references.

3. **Vocabulary strategy v1.0.1 §6 + §7 + §13 cleanup** — light retirement traces; cross-reference archive.

4. **Insight #37 (scaffolding-vs-publisher-facing separation)** — incorporates this refined WP#4 discipline as part of separation pass scope.

5. **Phase 3 Tech Appendix v2.0.0 rebuild** — derives from cleaner terms_index v1.0.0+.

6. **Phase 4 Glossary v4 rebuild** — derives from cleaner terms_index v1.0.0+.

7. **Routine 1 + 2 patterns** — already function correctly; cross-reference retirement archive for remediation hints (cosmetic update).

### §6.3 What does NOT need to be swept

Per Working Principle #4 retirement-trace discipline (refined):
- Existing ratified rigor passes preserve full traces (no sweep)
- Existing open insights preserve full traces (no sweep — they're active)
- Pre-submission readiness audit dated snapshots preserve historical state (no sweep)

Cleanup is targeted at:
- terms_index (Phase 3 prep)
- Working principles + vocabulary strategy (active standing-discipline docs)

---

## §7. Open questions

1. **Retirement archive index population timing** — populate in this commit (full historical sweep — substantial work) OR populate incrementally as part of subsequent scaffolding cleanup (queued)? Recommendation: populate framework + ~5-10 most-significant entries this commit; remainder populated as discovered during Phase 3+4 rebuilds.

2. **terms_index summary-level trace format** — define standard format. Recommendation: 1-line entry in retirement-trace section of each entry: `[RETIRED YYYY-MM-DD → New Term per Insight #N; full trace at archive/retirements/index.md]`.

3. **Working principles + vocabulary strategy retirement-trace cleanup scope** — full sweep this commit OR queued? Recommendation: queued (substantial scope; not blocking Phase 3 immediately; could absorb into Insight #37 scaffolding-separation work).

4. **Cross-reference format from retirement archive to ratified rigor passes** — single citation per retirement OR full-detail link. Recommendation: single citation; rigor pass file is canonical detail.

5. **Routine 1 + 2 update timing** — when to update sentinel patterns to cite archive index. Recommendation: queued; not blocking.

---

## §8. Cross-references

### §8.1 Upstream

- **Working Principle #4** — current discipline being refined.
- **Working Principle #8** — publisher-facing scrub; complementary; unchanged.
- **Working Principle #1** — effort-to-repair-not-rigor; supports refinement.
- **Working Principle #9** — git workflow; orthogonal.
- Insight #28 (retirement-traces / scaffolding-vs-publisher-facing tier-3 trichotomy) — origin of WP#4's tier discipline; refined here.
- Insight #37 (OPEN scaffolding-vs-publisher-facing separation) — natural integration point.
- Insight #39 (pre-publication external review) — refinement improves reviewer experience.

### §8.2 Downstream artifacts

- `alignment/commons_bonds_working_principles_v1.0.0.md` — Principle #4 update.
- `archive/retirements/index.md` — new file (initial structure + populated).
- `alignment/commons_bonds_open_insights_v1.0.0.md` — Insight #59 closed-ratified record.

### §8.3 Sibling working principles

- WP#1 (effort-to-repair-not-rigor): orthogonal; unchanged.
- WP#2 (audit concept not phrase): orthogonal; unchanged.
- WP#3 (misnaming is rigor failure): orthogonal; unchanged.
- WP#4 (retirement traces): **refined** per this rigor pass.
- WP#5 (context-flipping rules earn named-rule status): orthogonal; unchanged.
- WP#6 (intellectual-honesty prior-art audit): orthogonal; unchanged.
- WP#7 (pre-publication-state discipline): orthogonal; unchanged.
- WP#8 (publisher-facing scrub): complementary; unchanged.
- WP#9 (worktree-isolation git workflow): orthogonal; unchanged.

---

**End of Working Principle #4 refinement rigor pass v1.0.0 [RATIFIED 2026-04-30 by Chris Winn — verdict: Tiered policy + retirement-archive index combined].**
