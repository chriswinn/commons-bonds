# Pipeline Doctrine — Stage 5 (v1.0.0)

**Date drafted:** 2026-05-17
**Status:** PROPOSED — pending author ratification at session close.
**Parent doctrine:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](commons_bonds_pipeline_doctrine_v1.0.0.md) §1 + §7
**Related directory:** [`tools/pre-submission-reviews/`](../pre-submission-reviews/) (existing pre-submission review artifacts; pre-publication review queue artifacts will live here too).

---

## §0. Purpose

Stage 5 is the **bookend pre-publication sign-off**: academic-rigor + prose-quality sign-offs on rendered output + the mandatory pre-publication review queue artifact for the manuscript-submission package.

Stage 5 bookends Stage 1's ready-to-draft sign-off (per pipeline doctrine §6). Stage 1 verified the brief met both rigor + voice standards before drafting fired; Stage 5 verifies no drift through the pipeline before the artifact ships to publisher / agent / editor.

The pre-publication review queue is the mandatory hand-off artifact that surfaces what external reviewers should engage post-acceptance — transparent quality-control disclosure rather than overclaiming-verification posture.

---

## §1. When Stage 5 fires

**Per v1.0.0 Amendment A (selective stage-firing, ratified 2026-05-18): Stage 5 is an EXPLICIT-GATE pass — fires only at pre-external-review send + pre-publication, NOT on automatic cascade after every prose edit.**

Stage 5 fires at:
- **Pre-external-review send** — before shipping to a peer reviewer / publisher / agent.
- **Pre-publication** — before final-venue publication; the mandatory pre-publication review queue artifact is generated here.
- **External-reviewer finding lands post-publication** — change-cascade routing routes the finding back through prior stages; Stage 5 re-fires once upstream changes settle.

Stage 5 does NOT auto-fire on prose edits, spot-fix applications, or routine retrofit work. The pre-publication review queue artifact (mandatory per pipeline doctrine §7) is the deliverable that gates Stage 5's firing — it only has meaningful content when an artifact is approaching distribution-readiness.

After Stage 4 (render + character-integrity audit) closes with verdict CLEAN or MEDIUM HOLD. (HIGH BLOCK at Stage 4 blocks Stage 5.)

---

## §2. Procedure

### §2.1 Academic-rigor sign-off

Per pipeline doctrine §6.2 academic-rigor sign-off:

Verify against the artifact's rendered output:

1. **No drift through pipeline.** Rendered text matches Stage 1b canonical-facts inventory + canonical-formula inventory + canonical-data inventory.
2. **Cross-artifact coherence maintained.** Bibliography commitments realized in final prose (verified against Stage 1c artifact); AuthorsNote framings honored; sibling-chapter cross-references resolve correctly.
3. **All Pass 3.1 fact-check findings resolved.** Either applied as spot-fix (rendered output reflects the fix) or held with rationale captured in pre-pub review queue.
4. **All Pass 3.4 adversarial thread-pull diagnoses dispositioned.** Either chapter held its ground (rationale captured in pre-pub review queue) or cross-chapter workstream spun up (handoff artifact referenced).
5. **Stage 4 render-integrity verdict** is CLEAN or MEDIUM HOLD with all MEDIUM dispositioned.

### §2.2 Prose-quality sign-off

Per pipeline doctrine §6.2 prose-quality sign-off:

Verify against the artifact's rendered output:

1. **No regressed-pattern matches.** Regressed-pattern scan against the rendered output returns CLEAN (or MEDIUM HOLD with each allowlisted with rationale).
2. **All Pass 3.2 voice-polish findings dispositioned.** Either applied (rendered output reflects the fix) or held with rationale.
3. **Voice register maintained.** The artifact's specified voice register (per Stage 1b §5) is consistent through the rendered output.
4. **No scaffolding leakage.** Scaffolding scan returns CLEAN (per §2.4 corpus-wide).
5. **Pass 3.3 acceptance verdict** holds in the rendered output (sampled spot-check — does the rendered version still trigger the same acceptance reads as the source?).

### §2.3 Sign-off output artifact

Brief markdown at `tools/quality-gates/sign-offs/<scope-slug>_stage5_signoff_<date>.md`:

```
# Stage 5 Sign-Off — [SCOPE]

**Date:** [YYYY-MM-DD]
**Stage 4 audit artifact:** [path]
**Rendered outputs audited:** [list of .docx + .html + .pdf paths]

## Academic-rigor sign-off
[Per §2.1 checklist; each item PASS / HOLD with rationale]
Verdict: PASS / HOLD

## Prose-quality sign-off
[Per §2.2 checklist; each item PASS / HOLD with rationale]
Verdict: PASS / HOLD

## Pre-publication review queue artifact
Path: [tools/pre-submission-reviews/<scope-slug>_pre_pub_review_queue_v1.0.0.md]
Verdict: GENERATED / DEFERRED-WITH-RATIONALE

## Overall
- PASS — artifact cleared for publisher / agent / editor.
- HOLD — items listed for resolution before shipping.
```

### §2.4 Pre-publication review queue artifact

**Mandatory** — generated as part of Stage 5. No exception. See §3 for full template.

---

## §3. Pre-publication review queue template

```
# Pre-Publication Review Queue — [ARTIFACT NAME]

**Date generated:** [YYYY-MM-DD]
**Artifact:** [title + chapter # / essay name / etc.]
**Stage 5 sign-off commit:** [short-sha]
**Rendered outputs:** [list of paths]
**Manuscript-submission package context:** [for-publisher / for-agent / for-editor]

---

## §1. What has been internally verified

### §1.1 Factual verification

Per the artifact's Stage 1b canonical-facts inventory (artifact path: [Stage 1b brief path]):

- **Named people:** verified by [author / session log + sources cited per Stage 1b §6]. Living named subjects have consent status documented (per the named-subject-consent discipline).
- **Named places:** verified by [author / session log + sources].
- **Dates:** verified against [Stage 1b §6 canonical-dates inventory].
- **Statistics / numbers:** verified against [sources cited per Stage 1b §6].
- **Quotes:** verbatim where claimed; verified against [original source].
- **Scene-anchor sequences:** verified by [author memory + family conversation / interview transcript / etc., per Stage 1b §6].
- **Fact-relationships:** verified.
- **Lineage / intellectual-history claims:** verified against [bibliography entries; secondary sources].

Pass 3.1 fact-check pass artifact: [path]. Total findings: [N] — disposition: [X applied; Y held with rationale below].

### §1.2 Math / framework verification (if applicable)

- **Canonical-formula inventory** matches Tech Appendix formal exposition (cross-verified per Stage 1c coherence check).
- **Numerical-constants inventory** matches sources.
- **Derivation-chain integrity** verified by [author + Pass 3.1 + Stage 4 formula-integrity audit].

### §1.3 Cross-artifact coherence

- Bibliography commitments touching scope: all realized in final prose (per Stage 1c verdict).
- AuthorsNote framings: honored.
- Sibling-chapter cross-references: resolve correctly.
- Cross-chapter consistency-inventory commitments: respected.

### §1.4 Audience-load verification

- Pass 3.3 audience-load acceptance verdict: [verdict] across [N] characters. Per-tier breakdown: [Tier 1 / 2 / 3 INCLUDE counts].
- Pass 3.4 audience-load robustness verdict: [verdict] across [N] adversarial characters. Thread-pull synthesis: [summary; load-bearing-chapter-claim threads vs procedural-flag threads].

### §1.5 Render integrity

- Stage 4 render-integrity audit verdict: [verdict]. MEDIUM HOLD items (if any): [list with rationale].

---

## §2. What has NOT been externally verified

### §2.1 Factual claims that would benefit from external corroboration

[Per claim type:]

- **Archival material with limited public-record traces:** [list specific claims; e.g., "Father's NACA → NASA Langley tenure spanning [date range] — verified via family memory + author's interview; not cross-verified against NASA Langley HR archive (access not pursued for this scope)."]
- **Lineage / intellectual-history claims:** [list claims that rely on author's reading of secondary literature where adjacent-tradition reading might surface different lineage frames]
- **Numerical / statistical claims:** [if any reliance on sources where update-frequency or source-authority might warrant external re-verification]

### §2.2 Math / framework claims that would benefit from external technical review

[Per claim type:]

- **Derivation-chain claims:** [list specific derivations; recommend technical reviewer with quantitative-economics / applied-mathematics background]
- **Framework-methodology claims:** [list specific framework-methodology claims; recommend economist in an adjacent tradition (heterodox-econ / institutional-econ / resource-econ / Stern-tradition / Hartwick-tradition)]
- **Render-integrity post-typesetter:** [for Tech Appendix specifically + any other math-heavy artifact: flag formula-integrity for re-verification post-publisher's typesetter pass]

### §2.3 Audience-coverage gaps (per Pass 3.4 thread-pull synthesis)

- **Adversarial threads NOT fully disarmed:** [per Pass 3.4 verdict, threads where the chapter held its ground but where external review at the affected audience might surface additional remediation. E.g., for Ch 1 REAUDIT v3 #33 Public Choice thread: cross-chapter rent-seeking-engagement workstream addresses but at Ch 5 / Ch 9 / Tech Appendix; Ch 1 itself does not engage Public Choice rent-seeking analysis directly.]

---

## §3. Recommended external reviewer types

### §3.1 Math reviewer

**Profile:** Technical reviewer with quantitative-economics / applied-mathematics background.

**Scope of review:** [for Tech Appendix specifically: every formula + derivation. For Ch 6 + Ch 9: every display math span + framework-application math.]

**What to look for:**
- Derivation-chain correctness.
- Notation conventions consistency.
- Inline-vs-display rendering integrity.
- Formula-integrity post-typesetter.

### §3.2 Framework-methodology reviewer

**Profile:** Economist in an adjacent tradition (heterodox-econ / institutional-econ / resource-econ / Stern-tradition / Hartwick-tradition / [tradition-specific to artifact]).

**Scope of review:** [framework-methodology claims throughout the artifact + lineage-handling]

**What to look for:**
- Methodological soundness vs adjacent traditions.
- Lineage attribution clarity.
- Framework-claim defensibility (specifically against Pass 3.4 adversarial threads documented in §2.3).

### §3.3 Domain expert(s)

[List per artifact; e.g., for Ch 3: Chesapeake-watermen-history reader; for Ch 2: coal-mining-history reader; for Ch 1: NIH / NASA Langley historical-record reader.]

**Profile:** [domain-specific]

**Scope of review:** [factual claims in domain + scene-anchor accuracy]

**What to look for:** [domain-specific]

---

## §4. Highest-priority sections for external review if publisher budget is limited

Per author preference, rank-ordered:

1. **[Section / chapter / span]** — rationale: [why this is highest-priority; e.g., "Tech Appendix §X carries the framework's load-bearing derivation; external math reviewer's verdict is most consequential here."]
2. **[Section / chapter / span]** — rationale
3. **[Section / chapter / span]** — rationale
…

---

## §5. Cross-references

- Stage 1b brief: [path]
- Stage 1c coherence-check: [path]
- Pass 3.1 fact-check: [path]
- Pass 3.2 voice-polish: [path]
- Pass 3.3 audience-load acceptance: [path]
- Pass 3.4 audience-load robustness: [path]
- Stage 4 render-integrity audit: [path]
- Stage 5 sign-off: [path]
- Cross-chapter workstreams touching scope (if any): [list]

---

*End of pre-publication review queue artifact.*
```

---

## §4. Severity-tier rules for Stage 5 verdict

Stage 5 verdict is **PASS** or **HOLD**.

**PASS** requires:
- Academic-rigor sign-off: PASS (all checklist items PASS, or HOLD items disposed via the pre-pub review queue).
- Prose-quality sign-off: PASS (same).
- Pre-publication review queue artifact: GENERATED (or DEFERRED-WITH-RATIONALE with author ratification).

**HOLD** results from:
- Any unresolved HIGH-severity finding from any prior stage that surfaces at Stage 5.
- Cross-artifact coherence verification fails (Stage 1c claims no longer hold after rendered output).
- Pre-publication review queue artifact not generated.

HOLD findings route through change-cascade per pipeline doctrine §3; the artifact does not ship to publisher until HOLD resolves.

---

## §5. Author sign-off + manuscript-submission package

Per ratified decision #10 (2026-05-17 brainstorm): the author self-signs Stage 5 + the pre-publication review queue is the structural artifact that surfaces what publisher should engage post-acceptance.

The manuscript-submission package (whether for publisher / agent / editor) **includes**:

- The artifact itself (rendered output).
- The pre-publication review queue artifact (§3 above).
- (Optional, per author preference) Stage 5 sign-off artifact (transparency about internal verification).

The pre-publication review queue is the doctrine-mandated piece. It is not optional. Submitting without it is a violation of the discipline.

---

## §6. Retrofit-mode notes

For chapters already through prior pipeline cycles (per retrofit policy decision #9):

- Stage 5 fires at the end of retrofit (after Stage 1a + Stage 1c + Pass 3.4 + Stage 4 complete).
- Pre-publication review queue artifact generated at retrofit Stage 5; serves the same hand-off role as first-cycle Stage 5.
- For math-heavy chapters (Ch 6 + Ch 9 + Tech Appendix): the pre-pub review queue specifically flags external math reviewer + formula-integrity post-typesetter as recommended engagements.

---

## §7. Hard constraints

- Stage 5 sign-off **must** be author-ratified before manuscript-submission package ships.
- Pre-publication review queue artifact **mandatory** at Stage 5. No exception.
- HIGH-severity findings surface at Stage 5 block shipping; route back through cascade.
- External-reviewer findings post-publication trigger Stage 5 re-fire after upstream cascade settles.
- The pre-publication review queue is a **transparent quality-control disclosure**, not a confession-of-weakness artifact; the framing is structural-identification of where external expertise adds value relative to internal verification capability.

---

*End of Stage 5 doctrine.*
