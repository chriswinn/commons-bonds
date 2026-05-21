# Stage 1c Cross-Artifact Coherence Check — Ch 8 Rent-Seeking Paragraph vs Ch 9 Reading C v3

**Date:** 2026-05-21
**Pass:** Stage 1c (cross-artifact coherence check) per pipeline doctrine v1.0.0 §3.1
**Scope:** Ch 8 rent-seeking paragraph (line 122) checked against Ch 9 Reading C v3 framing (lines 134–148)
**Trigger:** Cross-chapter cascade flagged at Ch 9 Pass 2 (Voice-Polish) §11 disposition log (commit `78a26c2`, 2026-05-21)
**Status:** PROPOSED — author ratifies via separate Phase C session
**Branch:** `worktree-agent-a185e66fbbb404582` (feature branch from `aa04a4a`; auto-merges to main per CLAUDE.md rigor-pass merge default)

---

## §0. Source artifacts read (with line counts + commit hashes verified)

| Artifact | Path | Line count | Commit verification |
|---|---|---|---|
| Ch 8 — *What Things Actually Cost* | `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` | 243 lines | Rent-seeking paragraph inserted by `a1e54d9` (2026-05-17), ratified `bc02767` (2026-05-18); current location line 122 (within Political Capture Cost section, lines 112–124) |
| Ch 9 — *Pricing Honestly* | `manuscript/chapters/Chapter__9_PricingHonestly.md` | 294 lines | Reading C v3 substantive rewrite applied at `78a26c2` (2026-05-21); current location lines 134–148 (header line 136; body 138–148) |
| Pass 2 disposition artifact | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_ch9_pricing_honestly_stage3_voice_polish_v1.0.0.md` | 750 lines | §11 disposition log records Reading C v3 emergence + cross-chapter cascade flag at lines 716, 734–736 |
| Pipeline doctrine v1.0.0 | `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` | (verified §3 + §3.1 + §3.3 light re-fire definition) | §3.1 routes "cross-chapter workstream applies content to multiple chapters" through Stage 1c automatically; light re-fire defined at §3.3 |
| Memory: audience-aware drafting | `tools/memory/feedback_audience_aware_drafting_discipline.md` | (verified Stage 1c position + change-cascade routing rules) | v3.0 doctrine framing matches |
| Memory: verify-stale-memory | `tools/memory/feedback_verify_stale_memory_claims.md` | (heeded staleness reminder; verified all date / file / commit / line-number claims at session start) | n/a |

**Filename correction noted:** The prompt referenced `Chapter__8_WhatThingsActuallyCost_Draft.md`; the canonical file on origin/main is `Chapter__8_WhatThingsActuallyCost.md` (no `__Draft` suffix). Ch 8 carries no `__Draft` suffix — only Ch 2 and Ch 3 retain the consent-pending marker per `feedback_chapter_draft_suffix_consent_marker.md` (2026-05-18 author flag). Ch 9 Pass 2 §11 disposition log used the `_Draft` path as a stale relative-link target; the canonical path is corrected here.

**Commit verification (all three referenced hashes confirmed on `origin/main`):**
- `78a26c2` — *Ch 9 Pass 2 Phase C — RATIFIED spot-fixes applied (13 prose + Reading C v3 rewrite)* (2026-05-21)
- `a1e54d9` — *Cross-chapter rent-seeking engagement — PROPOSED content edits (Public Choice complementarity)* (2026-05-17)
- `bc02767` — *Cross-chapter rent-seeking engagement workstream — RATIFIED 2026-05-18* (2026-05-18)

---

## §1. Coherence-check scope

### §1.1 What is being checked

The Ch 8 rent-seeking paragraph at line 122 (single paragraph; located within the *Political Capture Cost* component of the per-ton arithmetic spine). Verbatim current text:

> The architecture that produced McDowell County's specific form of post-extraction collapse was not impersonal. It was shaped, generation after generation, by coal-industry political-economic actors — operators, absentee-mineral-rights holders, industry trade associations — whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record. The cost-bearing-party analysis the framework performs (who absorbed what; over what timeframe; against what counterfactual) operates on top of an architecture that specific identifiable actors shaped. The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) does both kinds of work at once for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) does the architecture-shaping work cleanly for cases where the political-coalition record is on the books. Both readings illuminate McDowell. The framework's apparatus contributes the cost-bearing magnitudes; both adjacent traditions contribute the actor-and-coalition analysis the framework does not attempt.

### §1.2 What it is being checked against

Ch 9 Reading C v3 framing at lines 134–148, the canonical source-of-truth for the framework-vs-Public-Choice relationship as of `78a26c2`. Key Reading C v3 moves (per Pass 2 §11 disposition log + verified against Ch 9 source):

1. **Asymmetric framework-vs-Public-Choice positioning.** Public Choice = the extractor's reasoning under incomplete cost-visibility. Framework = the complete ledger that changes what the extractor is reasoning about. Not symmetric mutual-citation; not "complementary accounting."
2. **"Complete" replaces "honest"** in apparatus-describing prose. *Complete* is a structural claim about missing ledger columns; *honest* would smuggle moral judgment.
3. **"Ledger" / "what gets counted" replaces "consequence"** language. The framework doesn't track *consequences* (judgment-laden); it tracks *what gets counted on the ledger* (impartial).
4. **"Extractor's reasoning" replaces "mechanism"** for Public Choice / rent-seeking. Rent-seeking is rational actors maximizing extraction, not an abstract mechanism.
5. **Framework framed as both measurement AND decision tool** (paragraph 4 of the rewrite). Widened beyond consequence-accounting.
6. **Closing aphorism reframed in framework idiom.** "Someone designed it, and we can identify them" (Public Choice) + "the ledger then shows what they designed has been costing, and to whom" (framework) — two-part construction.

### §1.3 What is explicitly NOT in scope

- Re-litigating any Ch 9 Pass 2 disposition. Reading C v3 is fixed; this audit measures Ch 8 against it.
- Proposing Ch 9 changes. Ch 9 is source-of-truth.
- Any prose modification to Ch 8 — this artifact is PROPOSED-only.
- Apparatus / register audits beyond the rent-seeking paragraph (incidental flags are surfaced in §6 but are not the primary scope).

---

## §2. Verdict summary

**Aggregate verdict: STRUCTURAL DRIFT.**

The Ch 8 rent-seeking paragraph reads from the older "complementary accounting" framing (symmetric mutual-citation between Public Choice and the framework). Reading C v3's six-paragraph rewrite of Ch 9 substantively rejects that symmetric framing in favor of an asymmetric one. The Ch 8 paragraph, written under the older framing assumption, now reads as a contradicted-by-Ch-9 framing if both chapters are read together. The drift is structural (framing-level), not terminological (vocabulary-level) — though terminological drift compounds it.

**Per-question one-line rationales:**

| Q | Topic | Verdict | One-line rationale |
|---|---|---|---|
| 1 | Asymmetric vs symmetric framework-vs-Public-Choice positioning | ⚠⚠ INCOHERENT | Ch 8 reads symmetric ("Both readings illuminate McDowell"; "both adjacent traditions contribute"); Reading C v3 rejects the symmetry. |
| 2 | "Consequence" language | ✓ COHERENT (incidental) | Ch 8 paragraph does not use "consequence" / "consequences" framing; passes this check. |
| 3 | "Mechanism" language for Public Choice / rent-seeking | ✓ COHERENT (incidental) | Ch 8 paragraph does not use "mechanism" framing for Public Choice; passes this check. |
| 4 | "Honest" vs "complete" for the framework's ledger | ✓ COHERENT (incidental) | Ch 8 paragraph does not use "honest" / "complete" in framework-describing position; uses neither. (Ch 8 elsewhere uses "honest" — see §6 incidental flag.) |
| 5 | Framework as narrow consequence-accounting vs broad measurement+decision tool | ⚠ DRIFT | Ch 8 frames framework's contribution narrowly as "cost-bearing magnitudes" — narrower than Reading C v3's "measurement tool + decision tool" widening. |
| 6 | Cross-chapter terminology drift creating reader-confusion | ⚠⚠ INCOHERENT | "Both readings illuminate" + "both adjacent traditions contribute" + the parenthetical-citation symmetry (Coates/Darity/etc. + Buchanan/Tullock at the same grammatical level) all enact the symmetric framing that Reading C v3 abandons. A reader reading Ch 8 → Ch 9 sequentially will experience framing whiplash at Ch 9:144 ("the angles are not symmetric"). |

**Spot-fixes proposed:** 1 substantive paragraph-level rewrite (parallel in scope to Reading C v3's six-paragraph rewrite of Ch 9, scaled to Ch 8's single-paragraph length). Plus 2 incidental flags (§6) routing follow-up work.

---

## §3. Per-question detailed findings

### §3.Q1 — Does Ch 8's framing align with Reading C v3's asymmetric positioning, or does it still reflect the older "complementary accounting" symmetric framing?

**Verdict: ⚠⚠ INCOHERENT.**

**Ch 8 text (line 122):**
> *"The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) does both kinds of work at once for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) does the architecture-shaping work cleanly for cases where the political-coalition record is on the books. Both readings illuminate McDowell. The framework's apparatus contributes the cost-bearing magnitudes; both adjacent traditions contribute the actor-and-coalition analysis the framework does not attempt."*

**Ch 9 Reading C v3 corresponding move (line 144):**
> *"The two traditions describe the same political-economy phenomenon from two angles, but the angles are not symmetric. Public Choice supplied the vocabulary for analyzing the extractor's reasoning; the framework supplies the accounting that changes what the extractor is reasoning about... The framework is both a measurement tool and a decision tool. It counts the costs of past and ongoing extraction; it also makes possible different decisions about future extraction by every party who was previously maximizing under incomplete cost-information — including the extractors themselves."*

**Why this is INCOHERENT, not merely DRIFT:**
- The Ch 8 paragraph's load-bearing summary sentence — *"Both readings illuminate McDowell. The framework's apparatus contributes the cost-bearing magnitudes; both adjacent traditions contribute the actor-and-coalition analysis the framework does not attempt"* — is the canonical statement of the symmetric "complementary accounting" framing. Reading C v3's line 144 sentence *"the angles are not symmetric"* is the canonical statement of the rejection of that framing.
- A reader reading Ch 8 → Ch 9 sequentially will experience the contradiction at Ch 9:144 as an authorial reversal between chapters. This is not the kind of cross-chapter variation that reads as productive complexity; it reads as the author having changed their mind between chapters without updating the earlier one.
- Compounding the symmetry: the parenthetical-citation construction in Ch 8 places reparations-economics (Coates, Darity, Mullen, Hamilton, Conley) and Public Choice (Buchanan, Tullock) at the same grammatical level. Reading C v3 places Public Choice in an asymmetric structural position (the tradition that supplied the extractor's-reasoning vocabulary; the framework supplies the ledger). Ch 8 reads the two as parallel; Ch 9 reads them as asymmetric.

**Proposed spot-fix (PROPOSED form; do NOT apply):**

Rewrite Ch 8:122 to preserve the McDowell-specific actor-identification content but re-frame the framework-vs-Public-Choice (and -vs-reparations-economics) relationship to match Reading C v3. Three options for the author to ratify:

**Option A (light-touch reframe; preserves paragraph structure):**
> The architecture that produced McDowell County's specific form of post-extraction collapse was not impersonal. It was shaped, generation after generation, by coal-industry political-economic actors — operators, absentee-mineral-rights holders, industry trade associations — whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record. The cost-bearing-party analysis the framework performs (who absorbed what; over what timeframe; against what counterfactual) operates on top of an architecture that specific identifiable actors shaped. The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) supplies the actor-and-coalition vocabulary for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning that shaped the political-coalition record on the books. The framework's contribution is different in kind: the ledger that counts what those traditions described has been costing, and to whom — the cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number rather than as an actor-attribution problem. Chapter 9 develops the framework-Public-Choice relationship at greater length.

(Net change: replaces the two symmetric "does X cleanly" sentences with two asymmetric "supplies the vocabulary for" sentences that mirror Reading C v3's "supplied / supplies" construction; replaces the symmetric closing summary with an asymmetric one foregrounding the framework's ledger-contribution; adds the explicit Ch 9 forward-reference; preserves all named subjects + the McDowell-specific load-bearing detail.)

**Option B (medium-touch; introduces Reading C v3's "is a number" anaphora in compressed form):**
> The architecture that produced McDowell County's specific form of post-extraction collapse was not impersonal. It was shaped, generation after generation, by coal-industry political-economic actors — operators, absentee-mineral-rights holders, industry trade associations — whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record. The Public Choice tradition (Buchanan, Tullock) named the extractor's reasoning that shaped that record: rational actors maximizing what they could extract from politically-mediated arrangements under conditions of incomplete cost-visibility. The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) named the parallel actor-and-coalition architecture for the racial wealth gap. The framework's contribution is the ledger that counts what those architectures have been putting on it. McDowell County's thirteen-year life-expectancy gap is a number. The cost-bearing-party analysis (who absorbed what; over what timeframe; against what counterfactual) assigns that number to the column it belongs in. Chapter 9 develops the framework-Public-Choice relationship; this paragraph reads the architecture-and-actor side of the same case.

(Net change: introduces the *"is a number"* construction in single-instance form — under-states Reading C v3's four-fold anaphora to keep paragraph length comparable; foregrounds the asymmetric framework-supplies-the-ledger framing more strongly than Option A; preserves all named subjects.)

**Option C (heavy-touch; close paragraph-scale parallel to Reading C v3):**
A 2–3-paragraph expansion that mirrors more of Reading C v3's structure. Likely overweight for the *Political Capture Cost* component slot — this is one of seven cost-component slots in a per-ton arithmetic spine, and the surrounding component paragraphs (Black Lung at line 116; Social Cost of Carbon at line 118; cost-of-the-fight at line 120) average ~1 paragraph each. A 2–3-paragraph treatment here would distort the component-spine rhythm. **Not recommended** unless the author wants Ch 8 to carry substantial framework-Public-Choice argument in its own right (in which case the right answer is probably to move it out of the cost-component spine and into a new section).

**Recommended:** **Option A** for minimal-disruption framing-correction; **Option B** if the author wants Ch 8 to enact the Reading C v3 idiom (the *"is a number"* construction) rather than merely point forward to Ch 9. Either preserves the named-subject discipline (all five reparations-economics figures + Buchanan/Tullock preserved; coal-industry actor types preserved).

---

### §3.Q2 — Does Ch 8 use "consequence" / "consequences" language in describing what the framework documents?

**Verdict: ✓ COHERENT (incidental).**

**Audit result:** A full-paragraph scan for "consequence" / "consequences" in the Ch 8 rent-seeking paragraph (line 122) returns zero matches. The paragraph uses "cost-bearing-party analysis," "actor-and-coalition analysis," "cost-bearing magnitudes" — all framework-idiomatic accounting vocabulary. No moralism-smuggling vocabulary surfaces.

**Note:** A broader scan of Ch 8 for "consequence" / "consequences" returns: zero. The chapter consistently uses "cost," "component," "burden," "absorbed" — register matches the cost-accounting frame. No proposed change.

---

### §3.Q3 — Does Ch 8 use "mechanism" language for Public Choice / rent-seeking?

**Verdict: ✓ COHERENT (incidental).**

**Audit result:** The Ch 8 rent-seeking paragraph (line 122) describes Public Choice via "the architecture-shaping work" — not "mechanism." This is closer to Reading C v3's idiom than "mechanism" would have been.

**Note:** A broader scan of Ch 8 surfaces one use of "the mechanism" in the *Political Capture Cost* section preface (line 116, *"The mechanism that produced the higher wages was, of course, also the mechanism that produced the disease"*). This is not a Public-Choice-describing use — "mechanism" is used in its normal physical-causation sense (the mechanization of coal extraction). No proposed change.

---

### §3.Q4 — Does Ch 8 use "honest" language for the framework's ledger?

**Verdict: ✓ COHERENT (in the rent-seeking paragraph specifically); see incidental flag in §6.

**Audit result:** The Ch 8 rent-seeking paragraph (line 122) uses neither "honest" nor "complete" in any framework-describing position. Passes this check.

**Incidental flag (out-of-scope for this audit, surfaced per §6):** Ch 8's chapter title is *What Things Actually Cost*, which preserves "actually" rather than moralizing. However, the chapter elsewhere uses "honest" in framework-describing positions (one of which is the chapter's own apparatus, and another is in cross-chapter references to Ch 9). The Reading C v3 deliberation explicitly moved away from "honest" because it smuggles moralism into the impartial-accounting frame. Whether this should propagate book-wide ("honest" → "complete" in apparatus-describing positions) is a question for a separate Stage 1c book-wide coherence sweep, not for this single-paragraph audit. **Routed to §6 incidental flag.**

---

### §3.Q5 — Does Ch 8 frame the framework's contribution narrowly as "consequence-accounting" or broadly as "measurement + decision tool"?

**Verdict: ⚠ DRIFT.**

**Ch 8 text (line 122 closing summary):**
> *"The framework's apparatus contributes the cost-bearing magnitudes; both adjacent traditions contribute the actor-and-coalition analysis the framework does not attempt."*

**Ch 9 Reading C v3 corresponding move (line 144):**
> *"The framework is both a measurement tool and a decision tool. It counts the costs of past and ongoing extraction; it also makes possible different decisions about future extraction by every party who was previously maximizing under incomplete cost-information — including the extractors themselves."*

**Why this is DRIFT (not INCOHERENT):**
- The Ch 8 framing is narrower than Reading C v3's. *"Cost-bearing magnitudes"* names the measurement dimension only; it does not name the decision-tool dimension that Reading C v3 added.
- The Ch 8 framing is not incompatible with Reading C v3; it is incomplete relative to it. A reader who has internalized Reading C v3 reading Ch 8 will not experience contradiction here (as in Q1), but will experience the framework as narrowed.
- The drift is severity-MEDIUM because Ch 8's primary work is the per-ton arithmetic (the measurement dimension); the decision-tool dimension is appropriately foregrounded in Ch 9 (the chapter explicitly titled *Pricing Honestly*, where the decision-implication framing lives). Ch 8 does not need to carry the full measurement+decision framing — but its closing summary sentence should not actively undercut it by naming the framework's contribution as the cost-magnitude side only.

**Proposed spot-fix:** Absorbed into the Q1 proposed rewrite. Options A and B both replace the *"cost-bearing magnitudes only"* closing with framing that does not foreclose the decision-tool dimension. The light-touch version: change *"The framework's apparatus contributes the cost-bearing magnitudes"* → *"The framework's contribution is the ledger that counts what those architectures have been putting on it"* — preserves the measurement work + leaves the decision-tool work to be developed in Ch 9 without contradicting it from Ch 8.

---

### §3.Q6 — Are there terminology drifts between Ch 8 and Ch 9 that would create reader-confusion if both chapters are read together?

**Verdict: ⚠⚠ INCOHERENT (composite of Q1 + Q5; surfaced separately because the reader-experience question is distinct from the per-clause framing question).**

**Specific terminology / framing mismatches:**

| Concept | Ch 8 (line 122) | Ch 9 Reading C v3 (134–148) |
|---|---|---|
| Framework-Public-Choice relationship | *"Both readings illuminate McDowell. ... both adjacent traditions contribute the actor-and-coalition analysis"* (symmetric) | *"The two traditions describe the same political-economy phenomenon from two angles, but the angles are not symmetric"* (asymmetric) |
| Framework's contribution | *"the cost-bearing magnitudes"* (measurement only) | *"both a measurement tool and a decision tool"* (broader) |
| What Public Choice supplies | *"does the architecture-shaping work cleanly"* (act of analysis) | *"supplied the vocabulary for analyzing the extractor's reasoning"* (vocabulary supply; specific subject = extractor's reasoning) |
| What Ch 8 leaves implicit but Ch 9 makes explicit | (nothing said about whose reasoning the framework changes) | *"makes possible different decisions about future extraction by every party who was previously maximizing under incomplete cost-information — including the extractors themselves"* (explicit decision-implication for extractors) |
| Closing-summary form | Single declarative summary (*"Both readings illuminate"*) | Two-part construction (*"Someone designed it..." (Public Choice idiom); "the ledger then shows what they designed has been costing, and to whom" (framework idiom)*) |

**Reader-experience prediction (if Ch 8 → Ch 9 read sequentially):**

A reader who has just read Ch 8:122 carrying the *"Both readings illuminate; both adjacent traditions contribute"* summary will, upon reaching Ch 9:144, encounter *"the angles are not symmetric"* — a direct reversal. The reversal lands at the exact same load-bearing position in each chapter's argument (the framework-vs-Public-Choice summary statement). This is the canonical form of cross-chapter framing whiplash: not productive complexity, but the author appearing to have changed their mind between chapters without updating the earlier one.

The whiplash compounds with reader-type:
- **A Public Choice reader** (Cato / Mercatus / GMU; per Pass 2 §11 Pass-3 readiness §744) will read Ch 8 as the symmetric mutual-citation they expect and feel courted; then read Ch 9 as the asymmetric framework-supplies-the-ledger framing they did not expect. The acceptance verdict shifts from strong-INCLUDE (under Ch 8) to qualified-INCLUDE-or-worse (under Ch 9). The Pass 2 audience-load test predicted qualified-INCLUDE for this audience under Reading C v3; uncorrected Ch 8 drift increases the qualified-INCLUDE-to-EXCLUDE risk because Ch 8's symmetric framing primes the reader to expect symmetric treatment at Ch 9.
- **A cost-accounting-tradition reader** (the framework's home audience) will read Ch 8 → Ch 9 and notice the framing shift; if astute, they will read Ch 9 as the corrected version and Ch 8 as the older version, and ask whether Ch 8 needs updating. (This is the reader who motivated this coherence-check session.)
- **A general reader** will likely not consciously register the asymmetry, but will experience the chapter-to-chapter argument as slightly unsettled rather than building.

**Proposed spot-fix:** Same as Q1 — Option A or Option B of the proposed rewrite. The rewrite eliminates the framing whiplash by aligning Ch 8's framework-Public-Choice summary with Reading C v3's asymmetric framing. No separate spot-fix needed beyond the Q1 paragraph rewrite.

---

## §4. Cross-chapter terminology drift summary

The compact vocabulary-and-framing drift table:

| Reading C v3 idiom (Ch 9:134–148) | Ch 8:122 current form | Drift severity |
|---|---|---|
| *"the angles are not symmetric"* | *"Both readings illuminate McDowell. ... both adjacent traditions contribute"* | INCOHERENT |
| *"supplied the vocabulary for the extractor's reasoning"* | *"does the architecture-shaping work cleanly"* | INCOHERENT (different verb-frame: vocabulary-supply vs work-doing) |
| *"under conditions of incomplete cost-visibility"* | (absent from Ch 8 paragraph) | MISSING (Ch 8 does not invoke the visibility frame at all) |
| *"both a measurement tool and a decision tool"* | *"the cost-bearing magnitudes"* | DRIFT (narrower) |
| *"the ledger then shows what they designed has been costing, and to whom"* | *"the framework's apparatus contributes the cost-bearing magnitudes"* | DRIFT (narrower; absent the costing-and-to-whom direction) |
| *"is a number"* (four-fold anaphora paragraph 3) | (absent from Ch 8 paragraph) | OPTIONAL — Option B of §3.Q1 proposed rewrite introduces a single-instance use; Option A does not |
| Italicized aphorism convention (closing line 148) | (no aphorism at Ch 8:122) | NOT REQUIRED — Ch 8:122 is a single component paragraph, not a section close; no aphorism slot. |

**Net assessment:** the drift is concentrated at the framework-vs-Public-Choice summary clause (the single most load-bearing sentence in the Ch 8 paragraph). Other terminological dimensions are minor or absent-but-acceptable. A single targeted paragraph rewrite (per §3.Q1) resolves the structural drift; no chapter-wide terminology sweep is required by this coherence check.

---

## §5. Aggregate verdict + Phase C recommendation

**Aggregate verdict: STRUCTURAL DRIFT.**

**Phase C recommendation:** Author ratifies one of the §3.Q1 options (A, B, or C) — or instructs Claude on an other-prose direction — in a separate Phase C session per pipeline doctrine §3.7 Amendment C interactive ratification protocol. Recommended: **Option A** (light-touch reframe; preserves paragraph structure; eliminates framing whiplash; preserves named-subject discipline; adds explicit Ch 9 forward-reference).

**Cross-chapter cascade implication for Ch 9:**

The Pass 2 §11 disposition log's Pass-3-readiness note §745 specifies: *"Cross-chapter cascade flag (Ch 8 rent-seeking paragraph coherence) should be resolved before Pass 3 fires to avoid cross-chapter drift in the audience-load read."* This audit confirms that the cascade is non-trivial (STRUCTURAL DRIFT, not CLEAN) and recommends resolving the cascade *before* Ch 9 Pass 3 runs its 40-character full-rigor + adversarial audience-load test on the Reading C v3 Public Choice section. Specifically:

- The Cato / Mercatus / GMU libertarian-Public-Choice acceptance verdict under Reading C v3 was Pass 2's predicted-qualified-INCLUDE landing. With Ch 8 drift uncorrected, the same audience reading Ch 8 → Ch 9 sequentially encounters framing whiplash that risks shifting that verdict toward EXCLUDE.
- Pass 3.4 (adversarial-set thread-pull synthesis) for Ch 9 is most likely to surface this drift as a finding (an adversarial Public Choice reader will read Ch 8:122 as the chapter that promised symmetric treatment and Ch 9:144 as the chapter that withdrew the promise; the thread-pull verdict will flag the cross-chapter inconsistency).
- Recommended sequence: ratify the §3.Q1 spot-fix in a Phase C session → apply to Ch 8 → then fire Ch 9 Pass 3.

**Phase C session sizing:**

The §3.Q1 spot-fix is a single-paragraph rewrite of approximately 12 sentences. Per Amendment C §3.7.6 (interactive ratification + application combined), the Phase C session is roughly a 30-minute walkthrough: author selects A / B / C / other-prose / defer; Claude applies the selected option to Ch 8 source; commit lands. This is well-sized for a single interactive session.

**Cross-thread-todos entry (proposed):**

Add to `tools/cross-thread-todos.md` (or equivalent PM dashboard tracking) a single entry:

> *Ch 8 rent-seeking paragraph (line 122) — Phase C session to ratify §3.Q1 spot-fix per Stage 1c coherence-check artifact `tools/rigor-passes/commons_bonds_stage_1c_coherence_check_2026-05-21_ch8_rent_seeking_v1.0.0.md`. Blocks Ch 9 Pass 3 firing per Pass 2 §11 readiness note §745.*

---

## §6. Hard constraints honored + incidental flags

### §6.1 Hard constraints honored

| Constraint | Status |
|---|---|
| No spot-fixes applied to `Chapter__8_WhatThingsActuallyCost.md` | ✓ HELD — this artifact is PROPOSED-only; chapter file unchanged. |
| No re-litigation of Ch 9 Pass 2 dispositions | ✓ HELD — Reading C v3 is treated throughout as fixed source-of-truth; this audit measures Ch 8 against it, not vice versa. |
| No Ch 9 changes proposed | ✓ HELD — all proposed changes target Ch 8:122 only. |
| Apparatus / register / named-subject discipline drifts flagged incidentally | ✓ See §6.2 below. |
| Cross-thread-todos items flagged | ✓ See §5 above (single proposed entry). |
| Fresh feature branch from current origin/main | ✓ The worktree branch `worktree-agent-a185e66fbbb404582` was already created at `aa04a4a` (current origin/main HEAD); per the worktree-as-feature-branch convention (used at Ch 9 Pass 2 §10), this is the feature branch for this session. No additional branch creation needed. |
| Stage 1c artifact auto-merges to main per CLAUDE.md rigor-pass merge default | ✓ Pending session-close commit + fast-forward. |
| Verify-stale-memory discipline | ✓ All file paths, line counts, commit hashes, current date claims verified at session start (§0 records the verification). |

### §6.2 Incidental flags (out-of-scope of this single-paragraph audit; routed for separate work)

**Incidental flag IF-1 — book-wide "honest" → "complete" question.** Reading C v3's deliberation surfaced that "honest" smuggles moralism into the impartial-accounting frame. Ch 8 uses "honest" in apparatus-describing positions outside the rent-seeking paragraph (lines verified during the §3.Q4 broader scan). Ch 9 title is *Pricing Honestly* — a chapter-title-level use of the word that pre-dates the Reading C v3 deliberation. **Routing:** open question whether the Reading C v3 vocabulary shift propagates book-wide (book title + Ch 9 title + apparatus uses in Ch 8 + apparatus uses in TA + AuthorsNote, etc.). **Recommended routing:** separate Stage 1c book-wide vocabulary-coherence sweep session, scoped at the apparatus-describing-position level. NOT in scope for this single-paragraph audit; flagged for the cross-thread-todos PM tracking.

**Incidental flag IF-2 — Ch 5 + Tech Appendix sibling cross-chapter touches from same workstream.** The cross-chapter rent-seeking-engagement workstream (commits `a1e54d9` → `bc02767`) also inserted parallel content at:
- Ch 5:184 (*"Architecture and rent-seeking: who shaped the system?"* section) per `a1e54d9` commit message.
- Tech Appendix §1.10:608 (*"Scope: complementarity with Public Choice / rent-seeking analysis"* paragraph) per `a1e54d9` commit message.

This audit's scope was specifically Ch 8. The Pass 2 §11 disposition log §736 named Ch 8 as the cascade-flagged chapter. However, the symmetric "complementary accounting" framing the Reading C v3 rewrite supersedes would have informed those Ch 5 + TA touches as well. **Recommended routing:** open second Stage 1c coherence-check sessions for Ch 5 + TA §1.10 against Reading C v3 — either as separate sessions per chapter / artifact, or as a combined cross-chapter-rent-seeking-coherence sweep. NOT in scope for this Ch 8 audit; flagged for PM tracking + cross-thread-todos.

**Incidental flag IF-3 — verb-frame drift "does the work cleanly" vs "supplied the vocabulary for".** The Ch 8 line 122 verb-frame for Public Choice — *"does the architecture-shaping work cleanly"* — differs from Reading C v3's *"supplied the vocabulary for the extractor's reasoning."* The Ch 8 verb-frame implies Public Choice is doing the analytical work itself (within Public Choice's analytical chain). Reading C v3's verb-frame implies Public Choice supplied vocabulary that the framework then uses. The verb-frame drift is captured under §3.Q6 (cross-chapter terminology drift) but flagged separately here because it has implications beyond this paragraph: any book-wide reference to Public Choice as a tradition (rather than a vocabulary-supplier) carries this drift. **Routing:** absorbed into IF-2's sibling-chapter audit recommendation.

**Named-subject discipline — confirmed clean.** All named subjects in the Ch 8:122 paragraph are scholarly citations (Coates, Darity, Mullen, Hamilton, Conley as reparations-economics tradition; Buchanan, Tullock as Public Choice). All are public scholars cited in their public scholarly capacity per `tools/memory/feedback_named_subject_consent.md` public-record exception (their published work is the citation basis). No consent gating required. The McDowell County reference is a place name (safe per memory). No incidental flag.

**Apparatus discipline — clean within paragraph scope.** Citations are parenthetical-list form, consistent with the rest of Ch 8's citation register. Hyphenation of "cost-bearing-party" / "actor-and-coalition" / "architecture-shaping" is consistent with Ch 8's chapter-wide hyphenation discipline. No apparatus drift surfaced.

---

## §7. Session-close protocol

Per pipeline-doctrine + CLAUDE.md rigor-pass merge default:

1. ✓ Stage 1c coherence-check artifact (this document) is the only file modified by this session.
2. Pending: commit on feature branch `worktree-agent-a185e66fbbb404582` with descriptive message.
3. Pending: fast-forward merge to `main`; push `origin main`.
4. Pending: report back to author per the prompt's report-format requirements (under 300 words; aggregate verdict + spot-fix count + most-important drift + filename + commit hash + decisions-needed).

Author decisions needed (post-session):
- **D-1.** Which §3.Q1 spot-fix option to ratify (A / B / C / other-prose / defer). **Recommended:** Option A.
- **D-2.** Whether to open the §6.2 IF-1 book-wide *"honest" → "complete"* sweep as a separate session, or defer.
- **D-3.** Whether to open the §6.2 IF-2 Ch 5 + TA §1.10 sibling-chapter coherence-check sessions, or defer.
- **D-4.** Whether to enforce the §5 "resolve Ch 8 cascade before Ch 9 Pass 3" sequencing, or proceed with Pass 3 first (latter risks adversarial-set finding the cross-chapter drift).

---

*End of Stage 1c coherence-check artifact — Ch 8:122 rent-seeking paragraph vs Ch 9 Reading C v3 (134–148). PROPOSED 2026-05-21. Author ratifies via separate Phase C session.*
