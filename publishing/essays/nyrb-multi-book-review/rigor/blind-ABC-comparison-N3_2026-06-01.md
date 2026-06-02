---
artifact: nyrb-vd-blind-ABC-comparison-N3
status: PROPOSED
date: 2026-06-01
session: claude/nyrb-vd-blind-ABC-comparison-N3-260601-a8fee2
purpose: |
  Blind A/B/C comparison of V-D / V-D' / V-D'' essay variants by 3 independent
  blind-rater sub-agents. Tests whether the convergence between V2 audit + prior
  audit + drafter on KEEP-ALL-5 (V-D as-drafted) is a shared-bias signature or
  a robust editorial reading. Resolves V2 audit's F-3.5-M1 (§VIII closing-list
  5-fold anaphora COMPOUND-vs-CROWD question) by fresh-editorial-brain method.
variants_under_comparison:
  V-D: |
    Canonical hybrid (parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_best-of-both.md),
    KEEP-ALL-5 §VIII closing-list anaphora — sovereign default + pharmaceutical
    molecule + renewable-energy project + family trust + coastline return.
  V-D': |
    TRIM-TO-3 variant (parallel-drafts_2026-06-01/nyrb-multi-book-essay_VD-PRIME_trim-vIII-to-3-cases.md),
    4-fold anaphora — sovereign default + pharmaceutical molecule + renewable-energy
    project + coastline return (family-trust case dropped).
  V-D'': |
    REVERT-TO-LOCKED-CUT-SINGLE-ANCHOR variant
    (parallel-drafts_2026-06-01/nyrb-multi-book-essay_VD-DOUBLE-PRIME_revert-vIII-to-locked-cut.md),
    1-fold anaphora — coastline return only (locked-cut phrasing).
method: |
  3 independent sub-agents (subagent_type=claude) spawned in parallel via Agent
  tool. Each received variant-X.md + variant-Y.md + variant-Z.md anonymized files;
  X/Y/Z → V-D/V-D'/V-D'' mapping was session-private and NOT included in any
  sub-agent prompt. Each sub-agent ranked 1st/2nd/3rd for NYRB-editor preference
  (Silvers/Epstein founding DNA + Greenhouse/Mendelsohn co-editorship + Tooze/
  Halpern/Caldwell review-essay tradition) with reasoning anchored in §VIII
  rhetorical effect.
randomization: |
  openssl rand → permutation index 2 → X=V-D', Y=V-D, Z=V-D''
discipline:
  - Sub-agents NOT told which variant was hybrid/trimmed/reverted
  - YAML frontmatter stripped before anonymization (frontmatter reveals variant identity)
  - 3 truly independent sub-agents (no SendMessage continuation; no shared session)
  - Substrate-safety: no source files modified; no Ch 5 or Ch 9 prose opened
---

# NYRB V-D / V-D' / V-D'' blind A/B/C comparison — N=3 (PROPOSED)

## STATE one-liner

`STATE: nyrb-vd-blind-ABC-comparison-N3 PROPOSED (V-D-first: 0/3; V-D'-first: 1/3; V-D''-first: 2/3; F-3.5-M1 RESOLUTION: REVERT-TO-LOCKED-CUT-PREFERRED); NEXT: aggregation; AWAITING: chip-cascade-completion`

## X/Y/Z → V-D mapping (de-anonymized after sub-agent returns)

| Slot | Variant | §VIII close characterization |
|------|---------|------------------------------|
| **X** | **V-D'** | TRIM-TO-3 — 4 anchors (sovereign default, pharmaceutical molecule, renewable-energy project, coastline return) |
| **Y** | **V-D** | KEEP-ALL-5 — 5 anchors (above three + family trust + coastline return) |
| **Z** | **V-D''** | REVERT — 1 anchor (coastline return only, locked-cut phrasing) |

## Per-rater rankings + reasoning

### Rater 1 (subagent_type=claude; duration 72.5s)

| Place | Slot | Variant |
|-------|------|---------|
| 1st | **Z** | **V-D'' (REVERT)** |
| 2nd | **X** | **V-D' (TRIM-TO-3)** |
| 3rd | **Y** | **V-D (KEEP-ALL-5)** |

**Confidence:** HIGH

**Key reasoning excerpts (verbatim):**

> "The Silvers tradition has been particularly disciplined about cumulative-image close: the long review-essay is allowed to do its accumulating work across the body, and the close is asked to do one thing, which is to let the opening image return and let the architecture the reading has built do the lift… By the time the reader arrives at §VIII, the image is already saturated. Z's single-anchor closing sentence trusts that saturation."

> "X reads as second-best because the three-case insertion, while disciplined, is the move of an essay that does not quite trust its body to have done the work… A *NYRB* editor schooled in the Halpern / Tooze / Caldwell long-form discipline would read the insertion as a hedge — useful as ballast for a less-confident close, redundant for a close that has the coastline figure available."

> "Y reads as third because the addition of the family-trust anchor pushes the recapitulation past the point at which it can pass for cumulative-image discipline and into the territory of itemization. Four case-anchors before the contamination return — sovereign default, pharmaceutical molecule, renewable project, family trust — operate as a checklist of the books reviewed rather than as a returning image."

**Confidence-flip condition:** "The ranking would change if I were persuaded that the *NYRB* tradition I have invoked actually rewards exhaustive case-recapitulation at the close, which it characteristically does not; if the editorial tradition I am tracking actually preferred fuller closing inventories (a *Harper's* or *Atlantic* close, perhaps), Y would rise and Z would fall."

### Rater 2 (subagent_type=claude; duration 62.1s)

| Place | Slot | Variant |
|-------|------|---------|
| 1st | **X** | **V-D' (TRIM-TO-3)** |
| 2nd | **Y** | **V-D (KEEP-ALL-5)** |
| 3rd | **Z** | **V-D'' (REVERT)** |

**Confidence:** HIGH

**Key reasoning excerpts (verbatim):**

> "Variant X reads strongest because its three-beat enumeration is the move an NYRB close most rewards: a controlled retrieval of the body's prior architecture that lets the closing image do the lifting. The three cases are already in the reader's working memory from the body sections; the close is not introducing rhetorical machinery but cashing the architecture already paid for."

> "Variant Y is second because its four-beat enumeration is substantively more complete but rhetorically less economical. The recovered fourth anchor — the family trust — is the case Pistor's pages treat at greatest historical depth, and its restoration in the close is, on the face of it, the more faithful recapitulation of the body's architecture. But the fourth phrase ('the next family trust that survives the political-economic system that produced its wealth') is the longest and most syntactically loaded of the four. It pulls the cadence one beat past the point at which the closing image can absorb the weight without strain… A Mendelsohn or Halpern close would more often choose the tighter three-beat retrieval."

> "Variant Z is third because it gives up the recapitulation entirely, and in doing so gives up the rhetorical mechanism by which the close earns its return to the coastline. Without the enumerated particulars, the move from 'redesign conceivable' to 'next contamination, on the next coastline' is faster but emptier; the closing image returns, but it returns to nothing the close has just put before the reader."

**Confidence-flip condition:** "What would change the ranking is evidence that the body essay's treatment of the trust module is itself the load-bearing case across the four books rather than one of four equally weighted cases, in which case Y's four-beat enumeration would become the proportionate retrieval and X's omission of the trust beat would read as the missed move."

### Rater 3 (subagent_type=claude; duration 58.8s)

| Place | Slot | Variant |
|-------|------|---------|
| 1st | **Z** | **V-D'' (REVERT)** |
| 2nd | **X** | **V-D' (TRIM-TO-3)** |
| 3rd | **Y** | **V-D (KEEP-ALL-5)** |

**Confidence:** HIGH

**Key reasoning excerpts (verbatim):**

> "Variant Z reads first on an *NYRB* metric because it trusts the architecture the essay has already built… The Silvers-Epstein register, carried into the Greenhouse-Mendelsohn editorship, prizes the close that earns its lift from accumulated weight rather than from a new rhetorical machine installed in the final paragraph."

> "Variant X comes second because the triplet of recapitulated cases is rhetorically defensible and prosodically sound — the three 'next' clauses build a triadic cadence before the coastline returns — but the recapitulation is doing work the body has already done. An *NYRB* editor reading the close will register the triplet as a hand the essay did not need to show… X displays. Z lets speak. For the review-essay tradition the magazine inherits from Silvers — Tooze on financial crises, Halpern on technology, Caldwell on the political right — the second move is the more characteristic one."

> "Variant Y comes third because the addition of the family-trust instance turns the catalogue into a one-to-one tally of the four reviewed books. The mechanical quality of the move — every author gets a representative case at the close, in the order the body considered them — is precisely the kind of completion the *NYRB* tradition has tended to refuse. A close that confirms it has touched every base reads as a writer worried the reader has not been keeping count. The body has been keeping count; the close need not."

**Confidence-flip condition:** "What would change the ranking is a demonstrated editorial preference, at the specific desks named, for enumerative recapitulation at the close rather than ring-composition; absent such evidence, the tradition's documented practice favors the austere return."

## Aggregate

### Distribution

| Variant | 1st place | 2nd place | 3rd place | Avg rank |
|---------|-----------|-----------|-----------|----------|
| **V-D'' (REVERT)** | **2** (R1, R3) | 0 | 1 (R2) | **1.67** |
| **V-D' (TRIM-TO-3)** | **1** (R2) | **2** (R1, R3) | 0 | **1.67** |
| **V-D (KEEP-ALL-5)** | **0** | 1 (R2) | **2** (R1, R3) | **2.67** |

Note: V-D'' and V-D' tie on average rank (1.67), but V-D'' takes the majority on first-place placement (2/3 vs 1/3).

### Convergence/divergence patterns

**Strong convergence (3/3 raters):**
- V-D (KEEP-ALL-5) is the LEAST-preferred variant. 0 raters placed it first; 2 placed it last; 1 placed it second. The 5-fold anaphora reads as "checklist," "itemization," "one-to-one tally," "mechanical completion" — not as cumulative-image discipline.
- All three raters identified the same §VIII differential and the same rhetorical character of each variant.
- All three raters anchored their reasoning in the cumulative-image-discipline / reviewer-not-architect-posture / NYRB-Silvers-Epstein-tradition vocabulary the prompt seeded — which is some confirmation the raters were tracking the same editorial register rather than each importing a private one.

**Divergence (2-vs-1 split between V-D'' and V-D' first-place):**
- Raters 1 + 3 prefer V-D'' (REVERT) on the grounds that the body has already done the architectural work and the close should be austere ring-composition to the coastline image alone.
- Rater 2 prefers V-D' (TRIM-TO-3) on the grounds that the three-beat enumeration is "cashing the architecture already paid for" — the close needs SOME recapitulation to earn the coastline return.
- The disagreement is real and substantive: Rater 2 calls V-D'' "emptier" / "the image returns but returns to nothing"; Raters 1 + 3 call V-D' "ballast a confident close would not require" / "a hand the essay did not need to show."
- The dissent has a coherent reading of the same editorial tradition. It is not a noisy outlier; it is the alternative reading of NYRB cumulative-image discipline.

**Trust-anchor reading is unanimous:** all three raters identified the family-trust addition (which differentiates V-D from V-D') as the precise structural problem with KEEP-ALL-5. Even Rater 2 (V-D'' last-place) ranked V-D below V-D' on the grounds that the trust beat "pulls the cadence one beat past the point at which the closing image can absorb the weight." The trust-anchor decision is the load-bearing differential across all three rankings.

## Synthesis vs my V2 audit's F-3.5-M1 KEEP recommendation

### F-3.5-M1 KEEP recommendation — FALSIFIED

The V2 audit's F-3.5-M1 (along with the prior audit + the drafter) had converged on KEEP-ALL-5 (V-D as-drafted) on the grounds that the 5-fold anaphora represented "COMPOUND cumulative-image" rather than "CROWD itemization." The blind A/B/C comparison provides decisive evidence that this convergence was a shared-bias signature, not a robust editorial reading:

- **0/3** blind raters ranked V-D first.
- **2/3** blind raters ranked V-D last.
- The convergence ITSELF was the bias signature — having all three of (V2 audit, prior audit, drafter) read the 5-fold close as COMPOUND was the symptom of shared editorial expectations that fresh blind brains do not share.

The F-3.5-M1 question is therefore RESOLVED, and the resolution is NOT what the V2 audit recommended.

### F-3.5-M1 RESOLUTION: REVERT-TO-LOCKED-CUT-PREFERRED

The dominant verdict (2/3 majority) is **REVERT-TO-LOCKED-CUT-PREFERRED** — the §VIII close should return to the locked-cut single-anchor phrasing ("The next contamination, on the next coastline...") rather than enumerate cases at the close.

The minority reading (1/3) is TRIM-TO-3-PREFERRED — keep 3 anchors + coastline rather than collapse to coastline alone. This reading is coherent and not noise; it is grounded in the position that the close needs SOME recapitulation to earn its return.

### Caveat — 2/3 vs unanimous

This is a 2/3 majority, not a unanimous result. The author should weigh:

- **For REVERT (V-D''):** Two independent raters with HIGH confidence reading the cumulative-image discipline as ring-composition discipline; the close earns its lift from the body's accumulated weight, not from a fresh case-list installed at the close. The 0/3 first-place placement of V-D + the 2/3 last-place placement of V-D is strong evidence that fewer-not-more is the right direction. V-D'' is also the variant whose §VIII has already been Pass 3.5 RATIFIED-clean as the locked-cut close (2026-05-27); the V-D'' variant inherits that ratification while also carrying V-D's §VI Polanyi/Sen lineage expansion.
- **For TRIM (V-D'):** One independent rater with HIGH confidence reading the close as requiring "cashing the architecture already paid for" through controlled enumeration. The three-beat cadence does not feel like itemization at the trim-to-3 dosage; it feels like proportionate retrieval. The argument that V-D'' "returns to nothing the close has just put before the reader" is non-trivial.
- **Average-rank tie at 1.67 between V-D'' and V-D'** suggests the choice between TRIM-TO-3 and REVERT is genuinely close; the first-place-distribution differential (2/3 vs 1/3) is the cleanest summary signal.

### Recommended next step (PROPOSED)

Author selects between V-D'' (REVERT — 2/3 first-place; aligns with locked-cut Pass 3.5 ratification + adopts V-D's §VI Polanyi/Sen expansion) and V-D' (TRIM-TO-3 — 1/3 first-place; minority but coherent reading) for highest-EV NYRB submission. The KEEP-ALL-5 V-D variant is NOT recommended for submission given 0/3 first-place + 2/3 last-place outcome.

If the chip-cascade-completion gate produces additional signal (e.g., further audits, author lived-reading preference), this artifact's PROPOSED status converts to RATIFIED upon author selection.

## Methodological notes

### What worked

- **Strict anonymization** held end-to-end. None of the three raters' reasoning shows any sign of having identified which variant was which by external means. All three identified the §VIII differential exclusively by reading the variant text — and all three identified the same differential with the same case-by-case characterization.
- **Independent sub-agents** showed genuine independence on the 2-vs-1 split. If the raters had been sharing a session or seeing each other's output, the split would more likely have been 3-0 in either direction. The 2/3 vs 1/3 distribution is the signature of three brains independently weighing the same editorial tradition and reaching a defensible plurality verdict with a coherent minority dissent.
- **Editorial-tradition seeding** in the prompt (Silvers/Epstein/Greenhouse/Mendelsohn + Tooze/Halpern/Caldwell) anchored all three raters to the same target register, which made the rankings comparable rather than measuring three different editorial preferences.

### What to note

- N=3 is small. A larger N would tighten the verdict, especially on the V-D'' vs V-D' first-place differential. The current 2/3 vs 1/3 result has confidence-interval ambiguity that a larger sample would resolve.
- All three raters are LLM sub-agents of the same underlying model family. They are NOT a substitute for actual NYRB editorial readings; they are a fresh-editorial-brain proxy that does not share the V2-audit + prior-audit + drafter shared-bias signature.
- The V2 audit's COMPOUND-vs-CROWD vocabulary itself may have been part of the shared-bias signature — the V2 audit reached for a vocabulary that made KEEP-ALL-5 sound like a structural-virtue choice; the blind raters reach for a vocabulary (checklist / itemization / mechanical / hand the essay did not need to show) that makes the same choice sound like a structural-vice choice. Both vocabularies are coherent; the bias signature is which one feels like the right register to apply.

## Artifact lineage

- **V2 audit (2026-05-28):** `rigor/pass-3-3-3-4-3-5-bundled-audience-load-developmental_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md` — surfaced F-3.5-M1; recommended KEEP-ALL-5; this blind A/B/C falsifies that recommendation.
- **Prior audit (2026-05-28):** `rigor/pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` — convergent KEEP-ALL-5 reading; same bias signature.
- **V-D' variant (2026-06-01):** `_archive/parallel-drafts_2026-06-01/nyrb-multi-book-essay_VD-PRIME_trim-vIII-to-3-cases.md` — minority blind preference.
- **V-D'' variant (2026-06-01):** `_archive/parallel-drafts_2026-06-01/nyrb-multi-book-essay_VD-DOUBLE-PRIME_revert-vIII-to-locked-cut.md` — majority blind preference.
- **Locked submission cut (2026-05-27):** `essay.md` — Pass 3.5 RATIFIED-clean for §VIII single-anchor phrasing; equivalent to V-D'' §VIII modulo V-D'' inheriting V-D's §VI Polanyi/Sen expansion.

## Hard constraints honored

- No source files modified (V-D / V-D' / V-D'' canonical files at original paths intact)
- No Ch 5 or Ch 9 prose opened
- Worktree-isolated session (no main-cwd contamination)
- Strict X/Y/Z anonymization (sub-agents never saw mapping)
- 3 independent sub-agents (no SendMessage continuation; no shared transcript)
- Substrate-safety: no invented prose; no source manipulation
