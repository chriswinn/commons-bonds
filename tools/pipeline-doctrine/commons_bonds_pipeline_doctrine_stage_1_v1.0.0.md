# Pipeline Doctrine — Stage 1 (v1.0.0)

**Date drafted:** 2026-05-17
**Status:** PROPOSED — pending author ratification at session close.
**Parent doctrine:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](commons_bonds_pipeline_doctrine_v1.0.0.md) §1
**Relates to existing template:** [`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`](../drafting-templates/stage-1-audience-aware-structure-pass.md) (Stage 1b internal-substantive template; this doctrine adds 1a + 1c wrapper sub-steps).

---

## §0. Purpose

Stage 1 is the **ready-to-draft gate**: everything Stage 2 needs to draft without re-opening source-prose paragraphs. Per the pipeline doctrine §1, Stage 1 has three sub-steps:

| Sub-step | Purpose | Output |
|---|---|---|
| **1a** | Corpus-hygiene invariant gate (scaffolding + regressed-pattern scan) | Clean-baseline verification artifact + any HIGH-severity blockers resolved |
| **1b** | Canonical fact-ground + audience-aware structure + render-safe convention | Stage 1 brief (the load-bearing pre-draft artifact; per existing template) |
| **1c** | Cross-artifact coherence check | Cross-artifact coherence verification artifact (bibliography + AuthorsNote + sibling-chapter + rigor-pass coherence) |

All three substeps complete before Stage 2 fires. Bookend sign-offs at Stage-1-complete: academic-rigor + prose-quality (per pipeline doctrine §6.1).

**Change-cascade routing target.** Per pipeline doctrine §3 change-cascade routing table, Stage 1 is the routing target for: new fact discoveries (→ 1b canonical-facts inventory update); new audience characters (→ 1b pressure-test set update); bibliography commitments landing (→ 1c coherence-check update); spot-fix applications (→ 1c light coherence re-check); cross-chapter workstream touches (→ 1c for each affected chapter); source-file changes (→ 1a invariant scans, automatic via pre-commit hook). Each cascade event runs the affected sub-step(s) + then re-fires the downstream passes per the routing rules.

---

## §1. Stage 1a — Corpus-hygiene invariant gate

### §1.1 What this catches

Process-scaffolding vocabulary + drafting placeholders + LLM-tic-class patterns + regressed patterns from prior rigor passes. Run automatically via `tools/scripts/check-corpus-invariants.sh` against the source artifact (if Stage 1 is for new content) or the chapter under audit (if Stage 1 is for a retrofit / partial cycle).

Two scans (per pipeline doctrine §2):

- **Scaffolding scan** — `tools/quality-gates/scaffolding-patterns.yaml`
- **Regressed-pattern scan** — `tools/quality-gates/regressed-patterns.yaml`

### §1.2 What Stage 1a is NOT

- Stage 1a is **not** a full voice-polish pass. Pass 3.2 voice-polish fires at Stage 3 against the Stage 2 draft. Stage 1a is the pre-flight invariant check that catches scaffolding leakage + already-known regressed patterns.
- Stage 1a is **not** a fact-check. Pass 3.1 fact-check fires at Stage 3 against the Stage 2 draft. Stage 1a verifies the source content is free of scaffolding tokens, not the truth-content of claims.

### §1.3 Procedure

1. Identify scope (the source artifact for new content; the chapter for retrofit).
2. Run `tools/scripts/check-corpus-invariants.sh --scope <path>`.
3. Resolve any HIGH-severity findings (block proceeding until resolved).
4. Review MEDIUM findings; address or add to allowlist with rationale.
5. Record clean-baseline verification artifact at `tools/quality-gates/clean-baselines/<scope-slug>_stage1a_<date>.md`.
6. Allowlist updates land in YAML registries; commit before proceeding to 1b.

### §1.4 Output artifact format

```
# Stage 1a Invariant-Gate Clean Baseline — [SCOPE]

**Date:** [YYYY-MM-DD]
**Scope:** [path/to/artifact-or-chapter]
**Scaffolding-scan registry version:** [git commit short-sha of YAML]
**Regressed-pattern-scan registry version:** [git commit short-sha of YAML]

## Scan results

- HIGH-severity matches: [count] — see §HIGH for details
- MEDIUM-severity matches: [count] — see §MEDIUM
- LOW / informational matches: [count] — see §LOW

## §HIGH

[Per-match: pattern + line + verbatim text + resolution (fixed / allowlisted with rationale)]

## §MEDIUM

[Per-match: pattern + line + verbatim text + disposition (addressed / allowlisted / held with rationale)]

## §LOW

[Per-match: pattern + line + verbatim text — informational only]

## Allowlist updates committed

[List of allowlist entries added to the YAML registries with rationale]

## Verdict

CLEAN BASELINE — Stage 1a complete; ready for Stage 1b.
```

---

## §2. Stage 1b — Canonical fact-ground + audience-aware structure + render-safe convention

### §2.0 Artifact-class classification (Amendment D, ratified 2026-05-31)

**Before** building the audience-pressure-test character set, classify the artifact class per the worked-examples table at [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) §"Reception-chain audience weighting (Amendment D)". The classification identifies direct readers (HIGHEST weight), consultants (HIGH), and projected-downstream readers (LOWER). Assign per-character weight-tags to the §1 character set; the brief records the artifact-class label + per-character weight-tags + reception-chain roles. Weight-tags propagate forward to Stage 3 Pass 3.3 / 3.4 / 3.5 audit aggregation. Empirical anchor: Aeon Option E.2 γ.1 opener-contingency Pass 3.3 + 3.4 + 3.5 audit addendum 2026-05-31 (commit `73c5764`).

### §2.1 What this is

Stage 1b is the existing audience-aware structure pass per [`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`](../drafting-templates/stage-1-audience-aware-structure-pass.md), with the following content-type-aware sub-protocols (per pipeline doctrine §4):

| Content type | Sub-protocol |
|---|---|
| Prose | Canonical-facts inventory (per existing template §6) + audience pressure-test character set (per existing template §1; see `audience-pressure-test-construction.md`) + voice register specification (per existing template §5) + locked-elements inventory (per existing template §7) |
| Math | Canonical-formula inventory + numerical-constants inventory + **baseline render test** (verify formulas render correctly through the publishing pipeline before drafting; see Stage 4 doctrine for render-safety conventions) |
| Tables | Canonical-data inventory + baseline render test (cell alignment + truncation check) |
| Figures | Source verification + caption verification + alt-text specification |

For math-heavy artifacts (Tech Appendix; Ch 6 + Ch 9 math-section), the baseline render test is **load-bearing** — minus-into-box rendering artifacts, Greek-letter font-fallback failures, and inline-vs-display drift are the categorical failure modes Stage 4 catches; Stage 1b establishes the render-safe convention so that Stage 2 drafting + Stage 4 audit have a known-good baseline.

### §2.2 Procedure

0. **Classify artifact class** per §2.0; record the classification label.
1. Use the existing Stage 1 template (`tools/drafting-templates/stage-1-audience-aware-structure-pass.md`) verbatim.
2. For each content type in scope, run the relevant sub-protocol. **Assign per-character weight-tags (HIGH / MEDIUM / LOW)** to the audience-pressure-test character set per the artifact-class classification.
3. Produce the Stage 1 brief artifact per the template's output spec; the §1 character set records the artifact-class label + per-character weight-tags + reception-chain roles.

### §2.3 Output

Single atomic commit: `tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_pre_draft_audience_structure_v1.0.0.md`.

---

## §3. Stage 1c — Cross-artifact coherence check

### §3.1 What this catches

The friction surfaced by Ch 1 Pass 3 REAUDIT v3: bibliography commitments + AuthorsNote framings + sibling-chapter cross-references + existing rigor-pass artifacts surfacing mid-Pass-3 rather than pre-Pass-3.

Specifically:

- **Bibliography commitments.** Every cited work in the bibliography that touches the artifact's scope. Especially load-bearing for chapter-relevance commitments (e.g., bibliography §21 marking a citation as load-bearing for a specific chapter). Each commitment surfaced + verified the artifact realizes it (or scoped out explicitly).
- **AuthorsNote framing.** The AuthorsNote is paratextual but sets reader expectations for the manuscript. Stage 1c verifies the artifact's framing is coherent with AuthorsNote claims.
- **Sibling-chapter cross-references.** For chapter artifacts: cross-references to other chapters (named in the prose; alluded to in scene-anchor terms; signaled via shared terminology). Each cross-reference verified for canonical consistency.
- **Existing rigor-pass artifacts.** Prior rigor-pass artifacts touching the same scope (e.g., for Ch 1 Pass 2 re-fire: the Ch 1 Pass 1 fact-check artifact's surfaced findings; the Ch 1 Pass 2 prior version's findings). Each prior finding's disposition surfaced + verified honored.
- **Cross-chapter consistency inventory.** The terminology + symbol + flagship-equation canonical-name commitments tracked in `tools/audits/` (cross-chapter consistency audit artifacts). Each commitment verified the artifact respects.

### §3.2 Procedure

1. Identify scope (the artifact under Stage 1; for new content: the artifact's planned scope + adjacent chapters).
2. Inventory:
   - All bibliography entries that touch the scope (search bibliography for chapter-tag commitments + named-subject overlaps + topic overlaps).
   - The AuthorsNote section that touches the scope (if any).
   - Sibling-chapter cross-references (search adjacent chapters for prose mentioning this chapter / topic / named subject).
   - Prior rigor-pass artifacts for this artifact (search `tools/rigor-passes/` for filename matches + scope matches).
   - Cross-chapter consistency-inventory entries (search `tools/audits/` for entries touching this scope).
3. For each item: verify the artifact's Stage 1b brief realizes the commitment / honors the framing / honors the prior finding's disposition.
4. If any item is not realized: add to the Stage 1b brief (canonical-facts inventory + structural decisions + locked elements + hard constraints as appropriate) **before** Stage 2 fires.
5. Record cross-artifact coherence verification artifact at `tools/quality-gates/coherence-checks/<scope-slug>_stage1c_<date>.md`.

### §3.3 Output artifact format

```
# Stage 1c Cross-Artifact Coherence Check — [SCOPE]

**Date:** [YYYY-MM-DD]
**Scope:** [path/to/artifact-or-chapter + planned-scope]
**Stage 1b brief artifact:** [path]

## Inventory

### Bibliography commitments touching scope
[List entries; each with bibliography line + commitment summary + disposition (realized in Stage 1b brief §X / added as new §Y / scoped out with rationale)]

### AuthorsNote framings touching scope
[Same structure]

### Sibling-chapter cross-references touching scope
[Same structure]

### Prior rigor-pass artifacts touching scope
[Same structure]

### Cross-chapter consistency-inventory items touching scope
[Same structure]

## Stage 1b brief updates

[List of edits made to the Stage 1b brief artifact to realize coherence items. Each edit cites the brief section + commitment source.]

## Verdict

COHERENCE VERIFIED — Stage 1c complete; ready for Stage 1 sign-off.
```

### §3.4 Worked example — the Ch 1 Pass 3 REAUDIT v3 friction

Friction (per pipeline-revision handoff §0): Bibliography §21 LOAD-BEARING Ch-1 chapter-relevance commitment was discovered mid-Pass-3 via a patent-verification search, not via a structured cross-artifact-coherence check.

How Stage 1c resolves this:

1. Stage 1c inventories bibliography entries touching Ch 1's scope.
2. Bibliography §21's LOAD-BEARING Ch-1 commitment for Dunbar / Du Bois surfaces during the inventory.
3. Stage 1b brief's structural-decisions section (§4) adds the Dunbar / Du Bois bibliography commitment as a locked element + adds the Black-Studies-resonance audience character to §1 pressure-test set.
4. Stage 2 drafts with the commitment + audience character in hand.
5. Pass 3.3 audience-load tests against the (now-included) Black-Studies-resonance character. Verdict at item (iv) is "default-apply per existing bibliography commitment" rather than a 45-minute mid-pass deliberation.

---

## §4. Stage 1 sign-off (bookend gate)

Per pipeline doctrine §6.1, two sign-offs gate Stage 2 firing after 1a + 1b + 1c complete:

### §4.1 Academic-rigor sign-off

Verify:
- Canonical-facts inventory (1b §6) complete + each fact verified against source.
- Canonical-formula inventory (if math content) complete + verified against Tech Appendix.
- Cross-artifact coherence verified (1c verdict CLEAN).
- Bibliography commitments touching scope all inventoried + dispositioned in Stage 1b brief.
- Stage 1a invariant scan returned CLEAN BASELINE.
- Named-subject consent gating (if any living named subject) verified + documented.

### §4.2 Prose-quality sign-off

Verify:
- **Artifact-class classification (§2.0) recorded + per-character weight-tags assigned to audience-pressure-test character set (Amendment D).**
- Audience pressure-test character set (1b §1) complete + tier-coverage appropriate to venue.
- Voice register specification (1b §5) complete + venue-appropriate.
- LLM-tic avoidance list (1b §5) complete.
- Locked elements (1b §7) verified + reproduced verbatim where applicable.
- Hard constraints (1b §8) complete.

### §4.3 Sign-off artifact

Brief markdown at `tools/quality-gates/sign-offs/<scope-slug>_stage1_signoff_<date>.md`:

```
# Stage 1 Sign-Off — [SCOPE]

**Date:** [YYYY-MM-DD]
**Stage 1b brief:** [path]
**Stage 1a clean-baseline:** [path]
**Stage 1c coherence-check:** [path]

## Academic-rigor sign-off
[Per §4.1 checklist; each item PASS / HOLD with rationale]
Verdict: PASS / HOLD

## Prose-quality sign-off
[Per §4.2 checklist; each item PASS / HOLD with rationale]
Verdict: PASS / HOLD

## Overall
- PASS — Stage 2 cleared to fire.
- HOLD — items listed for resolution before Stage 2.
```

Author ratifies sign-off artifact before Stage 2 fires.

---

## §5. Retrofit-mode notes

For chapters already through prior pipeline cycles (per retrofit policy decision #9):

- **Stage 1a always fires.** Likely produces CLEAN BASELINE (per 2026-05-17 leak-check survey expectation) but verification is per-chapter.
- **Stage 1b is partial.** Existing Stage 1 brief artifacts may not exist for chapters drafted before v2.0 discipline. For retrofit, treat the existing chapter prose AS the canonical reference for §6-equivalent facts (per the existing Stage 3 template's "Audit-existing-prose mode"). Build only the Stage 1c coherence-check and update the audience pressure-test set for the Pass 3.4 robustness test.
- **Stage 1c always fires.** This is the new-to-pipeline element; surfaces small gaps similar to today's bibliography §21 / Ch-1 / Dunbar-Du-Bois mid-Pass-3 discovery.

Retrofit Stage 1 sign-off is lighter than first-cycle sign-off (academic-rigor verifies coherence only; prose-quality may be deferred to Pass 3.2 voice-polish at retrofit).

---

## §6. Hard constraints

- Stage 1c **must** check bibliography commitments. The Ch 1 REAUDIT v3 friction's central lesson is that the bibliography itself is a load-bearing commitment registry.
- Stage 1a HIGH-severity findings block proceeding to 1b until resolved.
- Stage 1 sign-off **must** be author-ratified before Stage 2 fires.
- Stage 1b brief is the load-bearing artifact; Stage 2 drafts against it without re-opening source prose.
- Living named subjects require explicit author confirmation in Stage 1b before naming in publisher-facing prose.

---

*End of Stage 1 doctrine.*
