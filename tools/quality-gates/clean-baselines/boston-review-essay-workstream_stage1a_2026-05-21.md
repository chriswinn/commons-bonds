# Stage 1a Invariant-Gate Clean Baseline — Boston Review Essay Workstream

**Date:** 2026-05-21
**Scope:** `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` (source chapter for Stage 2 audience-blind drafting; the doctrinally-correct Stage 1a target)
**Base sha:** current `origin/main` at session run (worktree branch `claude/boston-review-essay-clever-sinoussi-440b42`)
**Scaffolding-scan registry version:** `c41ae4a` (`tools/quality-gates/scaffolding-patterns.yaml`)
**Regressed-pattern-scan registry version:** `85878d1` (`tools/quality-gates/regressed-patterns.yaml`)
**Command:** `bash tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/Chapter__5_TheAccountabilityGap.md`
**Pipeline doctrine reference:** [`tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](../../commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) §1
**Stage 1b brief:** [`publishing/essays/boston-review-accountability-gap/rigor/stage-1-brief.md`](../../../publishing/essays/boston-review-accountability-gap/rigor/stage-1-brief.md) (v1.0.1)
**Audit finding driving this artifact:** Audit Finding H1 in Stage 1b brief walkthrough 2026-05-21.

---

## Scan results

| Severity | Count |
|---|---|
| HIGH | 0 |
| MEDIUM | 1 |
| LOW | 0 |
| **Total** | **1** |

Patterns scanned: 78 (scaffolding + regressed combined).
Files scanned: 1.

## §HIGH

None.

## §MEDIUM

[MEDIUM] [scaffolding/scaffold-ratified] `manuscript/chapters/Chapter__5_TheAccountabilityGap.md:50` —

> "BP's sixty billion dollars in penalties against one hundred and fifty billion dollars in total costs yields a cost recovery ratio of forty percent. The company captured the full value of the oil it extracted. It paid less than half the cost of its extraction. The framework's accountability target is one hundred percent — extractors paying the full residual cost. Deepwater paid forty. The forty-percent ratio is the documented, court-validated, settlement-ratified empirical magnitude of the accountability gap for one of the largest environmental disasters in American history."

**Disposition:** SAME finding as flagged in `ch5_stage1a_2026-05-18.md`. The `scaffold-ratified` pattern matches the compound "settlement-ratified" — a legitimate Pass-3-ratified usage describing the empirical magnitude of the Deepwater accountability gap as established through judicial settlement, not a process-scaffolding token. The 2026-05-18 baseline documented this and predicted future tightening of the `ratified` regex would warrant codified allowlist entry. The 2026-05-18 baseline's overall verdict ("CLEAN BASELINE") stands; this MEDIUM is the documented false positive carry-forward. No allowlist amendment made in this session (registry SHAs unchanged; same disposition applies).

## §LOW

None.

## Brief-itself Stage 1a scan (informational; not the doctrinal target)

A supplemental scan of the Stage 1b brief (`publishing/essays/boston-review-accountability-gap/rigor/stage-1-brief.md` v1.0.0) returned 15 HIGH + 61 MEDIUM + 24 LOW findings. **These are expected false positives by design.** The brief is a rigor-pass artifact that discusses process-scaffolding vocabulary as something to AVOID in the essay; it does not USE the vocabulary as scaffolding leakage. Stage 1a's scaffolding-pattern registry is designed to catch process-vocabulary leakage INTO chapter prose (the Stage 2 output), not to scan rigor-pass artifacts themselves.

Per Stage 1 doctrine §1.1: "Run automatically via `tools/scripts/check-corpus-invariants.sh` against the source artifact (if Stage 1 is for new content) or the chapter under audit (if Stage 1 is for a retrofit / partial cycle)." For the BR essay workstream, the source artifact is Ch 5 — which this baseline records. The brief itself is the Stage 1b output, not the Stage 1a target.

**No allowlist amendment made for rigor-pass-artifact-class false positives.** Future doctrine refinement may add a global allowlist for `tools/rigor-passes/**/*.md` to suppress the noise, but the current Stage 1a discipline correctly targets chapter prose; the rigor-pass artifact's process-vocabulary content is by-design and out-of-scope.

## Allowlist updates committed

None.

## Verdict

**CLEAN BASELINE — Stage 1a complete for BR essay workstream; ready for Stage 1c.**

Ch 5 source remains effectively clean. The single MEDIUM is documented carry-forward from the 2026-05-18 baseline. Registry SHAs unchanged since 2026-05-18 (scaffolding `c41ae4a`; regressed `85878d1`).

**Next:** Stage 1c cross-artifact coherence check fires as separate session (per Audit Finding H2). Stage 1 bookend sign-off fires post-Stage 1c + fuller Stage 0 (per Audit Finding H3 + Decision #15).
