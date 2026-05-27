# Stage 1a Invariant-Gate Clean Baseline — Ch 2 → Harper's Magazine derivative essay

**Date:** 2026-05-27
**Scope:** Ch 2 → Harper's Magazine derivative essay (Wave 2 Candidate A) — Stage 1b brief artifact + Stage 2 audience-blind draft artifact + per-essay README sibling
**Files in scope:**
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-26_ch2_harpers_essay_pre_draft_audience_structure_v1.0.0.md` (Stage 1b brief; 610 lines; PROPOSED at commit `3d1810b` 2026-05-26)
- `publishing/essays/harpers-the-miner/essay.md` (Stage 2 draft; 7,216w body; PROPOSED at commit `55842a3` 2026-05-27)
- `publishing/essays/harpers-the-miner/README.md` (per-essay submission package; PROPOSED at commit `55842a3` 2026-05-27)
**Worktree branch:** `worktree-agent-a3390c00c9b9a4df0` (autonomous-mode agent worktree)
**Scaffolding-scan registry version:** `tools/quality-gates/scaffolding-patterns.yaml` (current HEAD)
**Regressed-pattern-scan registry version:** `tools/quality-gates/regressed-patterns.yaml` (current HEAD)
**Command executed:** `tools/scripts/check-corpus-invariants.sh` (full-corpus scan; per-scope verdict extracted below)
**Pipeline doctrine reference:** [`tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](../../commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) §1

---

## Execution note

The brief's §18.2 #1 🔴 DEFERRED-TO-RATIFICATION item (autonomous-mode sandbox blocked bash execution) is resolved in the Phase C ratification session (2026-05-27): the script executed cleanly from the unsandboxed Phase C ratification session against the agent worktree HEAD. Whole-corpus scan completed; per-scope verdict for Ch 2 → Harper's artifacts extracted below.

---

## Scan results — full corpus

| Severity | Count (full corpus) | Touching Ch 2 → Harper's scope |
|---|---|---|
| HIGH | 0 | 0 |
| MEDIUM | 15 | 0 |
| LOW | 14 | 0 |
| **Total** | **29** | **0** |

Patterns scanned: 80 (scaffolding + regressed combined; registry-driven).
Files scanned: 8 (corpus-wide).
Files matched (touching Ch 2 → Harper's scope): **0**.

---

## §HIGH

**None corpus-wide.**

The Stage 1a invariant gate clears for the whole corpus. Per gate doctrine, HIGH = block; zero HIGH findings means no blocking patterns.

## §MEDIUM (15 — all out-of-scope for Ch 2 → Harper's; informational only)

All 15 MEDIUM findings touch the pre-existing op-ed pipeline files (Norway + McDowell op-eds drafted 2026-05-10 onward; canonical-facts inventory). Distribution:
- `publishing/op-eds/norway-sovereign-wealth/op-ed.md` × 1 (`scaffolding/scaffold-stage-numbering` matching the line 14 Path B audit metadata phrasing referencing Stage 3 work)
- `publishing/op-eds/mcdowell-county-true-cost/op-ed.md` × 2 (`scaffolding/scaffold-stage-numbering` matching the line 14 Path B audit metadata phrasing referencing Stage 3 work; `regressed/regressed-consistency-44b-trust-fund-framing` matching line 29 op-ed body $44B Trust Fund framing — pre-existing registered pattern in the op-ed canonical context)
- `publishing/op-eds/norway-sovereign-wealth/README.md` × 3 (`scaffolding/scaffold-canonical-facts-inventory` matching expected canonical-facts cross-reference language in the package README)
- `publishing/op-eds/README.md` × 2 (same canonical-facts-inventory pattern in the README itself)
- `publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md` × 2 (canonical-facts file header + body lines matching the canonical-facts-inventory pattern + the regressed-44B framing pattern)
- `publishing/op-eds/mcdowell-county-true-cost/README.md` × 3 (canonical-facts cross-reference language + section header)

**None of the 15 MEDIUMs touch any Ch 2 → Harper's artifact.** The patterns flagged are doctrine-friendly expected matches in the op-ed metadata layer (canonical-facts cross-reference vocabulary is the intended idiom for op-ed README files); they're MEDIUM-severity informational flags, not regressions introduced by this Stage 2 draft. They were present at brief-PROPOSED time and remain present at Stage 2-PROPOSED time.

## §LOW (14 — all out-of-scope for Ch 2 → Harper's; informational only)

All 14 LOW findings match the `regressed/regressed-render-approx-tilde` pattern (use of `~` for "approximately" in metadata-layer paragraphs that the registry flags as a render-tilde-vs-approx-symbol pattern). Distribution:
- `publishing/op-eds/norway-sovereign-wealth/op-ed.md` × 3 (metadata block phrasings: word-count band, Path B audit phrasing, LEDE placeholder comment)
- `publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md` × 8 (canonical-facts inventory body lines using ~ shorthand for approximate figures)
- `publishing/op-eds/mcdowell-county-true-cost/op-ed.md` × 3 (metadata block phrasings: word-count band, Path B audit phrasing, LEDE placeholder comment)

**None of the 14 LOWs touch any Ch 2 → Harper's artifact.** The `~` shorthand in op-ed metadata is doctrine-acceptable for shorthand approximation in internal-scaffolding contexts (op-ed README + canonical-facts metadata are internal-scaffolding per CLAUDE.md classification). They were present at brief-PROPOSED time and remain present at Stage 2-PROPOSED time.

## Per-scope verdict — Ch 2 → Harper's artifacts

Zero HIGH + zero MEDIUM + zero LOW touching:
- Stage 1b brief artifact (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-26_ch2_harpers_essay_pre_draft_audience_structure_v1.0.0.md`)
- Stage 2 essay draft (`publishing/essays/harpers-the-miner/essay.md`)
- Per-essay README sibling (`publishing/essays/harpers-the-miner/README.md`)

**Per-scope verdict: CLEAN BASELINE.**

## Forward-routing (carry-forward to subsequent stages / sessions)

- **The 15 MEDIUM + 14 LOW corpus-wide findings are op-ed pipeline pre-existing artifacts**, not Harper's Stage 2 regressions. They warrant a corpus-hygiene cleanup pass at op-ed pipeline scope (separate workstream, not Ch 2 → Harper's scope); flag carried forward to the next PM session for triage.
- **No Stage 1c coherence finding routes out of Stage 1a for this scope** — coherence dispositions are already realized in the brief §9 cross-artifact coherence check (no unrealized bibliography commitment; AuthorsNote + sibling-chapter cross-references all dispositioned at brief level).
- **No Pass 3.1 fact-check spot-fix-language proposal is queued from Stage 1a** for this scope (Stage 1a is scaffolding/pattern-leak territory; fact accuracy is Pass 3.1 territory).

## Allowlist updates committed

None — the per-scope clean verdict requires no allowlist amendments. The corpus-wide MEDIUM + LOW findings are pre-existing op-ed pipeline patterns that the registry intentionally flags; allowlist amendments for those (if desired) are properly scoped to the op-ed pipeline cleanup workstream, not this artifact.

## Verdict

**CLEAN BASELINE — Stage 1a complete for Ch 2 → Harper's Magazine derivative essay scope; Stage 1b brief artifact + Stage 2 draft + per-essay README all clear; ready for Stage 3 cascade.**

The brief artifact's substantive content (16-character audience set + 8-section structure + voice register + canonical-facts inventory + apparatus exclusion list + length budget + render-safe convention + named-subject status + Stage 1c coherence verification + Stage 2/3/4/5 forward-pointers + §18 decisions-surfaced summary) carries no scaffolding-vocabulary leakage and no regressed-pattern registry matches. The Stage 2 draft artifact (7,216w literary-essay body + author bio + dek) carries no scaffolding leakage and no regressed-pattern registry matches. The per-essay README sibling carries no scaffolding leakage and no regressed-pattern registry matches.

Brief §18.2 #1 🔴 AUTHOR DECISION REQUIRED item resolved per Phase C ratification 2026-05-27.
