# Back-matter / reference-apparatus reorg — QUEUED (BLOCKED)

**Date queued:** 2026-06-09
**Status:** 🚧 **BLOCKED — DO NOT SPAWN YET.** Routed to the PM session by the TA-provenance-resume session for scheduling. Spawn the dedicated session(s) only AFTER the blockers in §Blockers land + merge; starting now would collide with the live TA sessions + the redraft campaign.
**Routed by:** `claude/ta-provenance-resume-260609-509a46` (cross-session message → PM session `pm-portfolio-ratification-and-aeon-submission-260529-b4ac02`)
**Branch when spawned:** fresh `claude/back-matter-reorg-<harness>` off current `origin/main` (after blockers land).

---

## §Why this exists — findings (current on-disk state, 2026-06-09)

### Two bibliographies that diverge

- **`research/literature/bibliography.md`** — standalone WORKING master (~24 sections, ~170 entries incl. agency sources §23/§24; heavy scaffolding: Status / Rigor-provenance / candidate-flags / character-notes / commit-refs). This is the SUPERSET.
- **TA §18 Bibliography** — embedded INSIDE `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (`<section id="sec-18-bibliography">`, ~180 lines, alphabetical-by-author, "academic citations only," ~3 agency mentions). Does NOT reference the standalone bib. Hand-maintained separately → drift. This is a SUBSET.

**Proof of drift (load-bearing):** the Darity longevity paper carries DIFFERENT author strings in each. The TA-provenance-resume session fixed the standalone bib to the correct **Himmelstein-lead** authorship, but **TA §18 still has the garbled "Bassett-Bell, Naa Oyo A. / David R. Williams / Darity" string.** Same error, two copies. See §Pre-reorg-divergence-flag below.

### Symbol / glossary / terms = scattered 3-file set

- `core/terms/terms_index.md` (~1,915 lines) — internal term-provenance SOURCE.
- `core/glossary/commons_bonds_updated_glossary_v{2,3,4}.html` — THREE reader-facing glossary versions (dedup to one).
- `manuscript/technical-appendix/symbol-registry_2026-06-07.md` — internal symbol/notation SOURCE (PROPOSED); states "the reader-facing Notation section is to be curated FROM this" — that reader-facing Notation section does NOT yet exist in the TA.

---

## §Target architecture (two-layer: internal source → reader-facing back-matter)

The repo already implies this pattern. Reader-facing back-matter cluster, curated FROM internal sources:

| Order | Reader-facing output | Curated FROM (internal source) |
|---|---|---|
| A | Technical Appendix | (the artifact itself) |
| B | Notation / Symbols | `manuscript/technical-appendix/symbol-registry_2026-06-07.md` |
| C | Glossary | `core/terms/terms_index.md` |
| D | References / Bibliography | `research/literature/bibliography.md` (the SUPERSET — NOT the TA §18 subset) |

- Keep `bibliography.md` as internal source-of-truth (scaffolding stays); generate a CLEAN reader-facing `references.md` from it.
- Retire TA §18 into a generated view/pointer, NOT a hand-copy.
- Co-locate the 4 reader-facing outputs as book back matter (e.g. `core/back-matter/`, order A→D); co-locate/tag the 3 internal sources as working files.

---

## §Dedicated session scope (when spawned)

1. Reconcile standalone bib ↔ TA §18 → one canonical source; fix duplicated errors (Himmelstein + whatever the diff surfaces); retire TA §18 to a generated subset.
2. Curate a clean reader-facing `references.md` from the master.
3. Dedup 3 glossary versions → one; curate reader-facing Notation section from `symbol-registry.md`.
4. Lay out back-matter appendix set + ordering + cross-references.

---

## §Blockers — spawn ONLY after these land + merge

1. **Live TA sessions editing the TA + §23.1 bib** (all active as top-level worktrees confirmed 2026-06-09):
   - "TA: Method-3 Path-B rework" (Session D)
   - "TA: internal-correctness fix sweep" (Session C; owns IPG apparatus + coal $4.71) — worktree `ta-internal-fixes-260607-208b7b`
   - "TA: Deepwater reconciliation + closeout" (Session E; owns Deepwater §11.2 + Solow-orphan + §23.1/§24 merge-eyeball)
2. **Held branches (MERGE-HOLD; author reviews before merge):**
   - `ta-rigor-audit-260606` + sub-branch `claude/ta-provenance-260607-ad2dfc`
   - `claude/ta-provenance-resume-260609-509a46` (5 commits, MERGE-HOLD — TA §11.6 $44B relabel + Eco/Cohesion estimate-labels + bib §24 consolidation + §23.3 Himmelstein fix)
3. **The redraft campaign** — rewriting chapters that cite the bib (live; per `tools/workstream-handoffs/`-tracked whole-cloth redraft campaign, resume handoff 2026-06-06).

**Reason to wait:** a bib/TA reorg while 3+ sessions edit the TA + bib = merge chaos; chapters citing the bib are mid-redraft. Spawn the reorg only once the TA is quiescent (no active TA worktrees), the held branches have merged to main (or been dispositioned), and the chapter redraft campaign has stabilized the citing prose.

**Spawn-readiness check (run before spawning):**
```bash
git -C /Users/c17n/commons-bonds worktree list | grep -iE "ta-internal|ta-provenance|ta-rigor|ta-method|ta-deepwater"
# Expect NO matches. If matches remain, blockers are still active — do not spawn.
```

---

## §Pre-reorg-divergence-flag (Himmelstein author string) — minor, optional fast-follow

The TA §18 bibliography Himmelstein/longevity-paper author string is **divergent** from the corrected standalone bib (standalone = Himmelstein-lead; TA §18 = garbled "Bassett-Bell, Naa Oyo A. / David R. Williams / Darity"). The reorg unifies this regardless. **Optional fast-follow** (per the routing session's suggestion): an already-active TA session (Session E, which already has the TA checked out) could fix the TA §18 string to match the corrected standalone now, so the two copies don't ship divergent in the interim. Routing this to a NEW chip is NOT recommended — it would touch the TA mid-edit and collide. Author may hand the one-line fix to an active TA session if convenient; otherwise the reorg catches it.

---

*Internal scaffolding; auto-merges to main per CLAUDE.md merge-on-ratification rule. This is a QUEUED kickoff scaffold — the workstream itself is BLOCKED and unspawned.*
