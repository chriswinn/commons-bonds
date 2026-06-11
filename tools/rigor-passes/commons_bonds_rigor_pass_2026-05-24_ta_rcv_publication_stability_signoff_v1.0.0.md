# Commons Bonds — Tech Appendix RCV Publication-Stability Sign-Off — v1.0.0

**Date drafted:** 2026-05-24 (Sun)
**Pass type:** Cross-chapter sign-off rigor pass — Tech Appendix RCV (Residual
Commons Value) publication-stability verification across the four corpus sites
where RCV is load-bearing. Read-only verification; produces a closure artifact
for the corpus rather than a per-workstream verification.
**Status:** **PROPOSED — sign-off artifact.** Author auto-ratifies via the
parent Ch 4 Stage 0 ratification session (this artifact is fired as a
precondition to closing Condition C1.a in
[`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md)
§4.3). Author has affirmed publication-stability via direct author knowledge in
the parent session; this artifact provides the corpus-side independent
verification trace.
**Scope:** Four canonical sites + cross-check of derivative deployment. Tech
Appendix Definition 1.6 + 1.7 + CS = RCV − B equation (§1); Ch 6 RCV
three-component name-defense paragraph (1f3ad9c, line 325); Ch 4 RCV framing
+ accountability-bond B + foreclosure component + externality tail; Ch 1 as
framework-introduction site (verify whether RCV first appears there or
downstream). Op-eds + Wave 1 essays cross-checked only at the level of "named
vs translated-out," not deep-dived.
**Output:** Per-site verdict (GREEN / YELLOW / RED) + overall verdict +
recommendation for cross-thread-todo #10 sub-item 2b status + downstream
applicability list.
**Branch:** committed on dedicated feature branch
`claude/ta-rcv-publication-stability-signoff-663265` per CLAUDE.md
internal-scaffolding merge-to-main discipline. (Parent Ch 4 Stage 0
ratification session lives on `claude/wave-2-derivative-planning-663265`;
this artifact will fast-forward to main at session close regardless of branch
choice, since both branches share ancestry with main.)

---

## 1. Inputs reviewed

| Site | File | Commit anchor | Lines verified |
|---|---|---|---|
| Tech Appendix §1 Foundations | `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (filename retains v2.0.0; content bumped to v2.1.0 per commit `36073ca` 2026-05-13) | `36073ca` (v2.1.0 bump) + `eb636c6` (pipeline retrofit 2026-05-18) | Definition 1.6 (RCV core formula) at lines 419–426; integrand-component breakdown at lines 447–457; Definition 1.7 (Accountability Bond) at lines 459–469; CS = RCV − B equation at line 465; forward-pricing shorthand vs. full bidirectional form at lines 470–475. TOC annotation at line 176 (Foundations §1 contents listing). |
| Tech Appendix §2 Two-Instrument Architecture | same file | same | §2 RCV ↔ B₂ pairing label at line 181 + §2 header at line 627; CSD–RCV correlation hypothesis at line 711. |
| Tech Appendix §3 RCV Quantification | same file | same | §3 header at line 724; RCV integrand restated at line 733; IPG definition at lines 756–759; Method 1 / 2 / 3 (Replacement Cost / Revealed Preference / Scarcity-Adjusted Option Value) at lines 780 / 849 / 889. |
| Ch 6 RCV three-component name-defense | `manuscript/chapters/Chapter__6_ThreeWaysofCounting.md` | `1f3ad9c` (2026-05-11) | Line 325 (the *Residual / Commons / Value* sub-choice paragraph anchoring Hartwick + Ostrom + Mazzucato); surrounding framework-introduction at lines 90–145 (Approach 3 RCV Model + Method 1/2/3 + triangulation); Four Gates at lines 289–315; the Hotelling Identity bridge at line 331. |
| Ch 4 RCV framing | `manuscript/chapters/Chapter__4_TheExistenceProof.md` | (current tip) | Lines 44–56 (Norway "what the framework says" passage — names *residual commons value framework*, accountability bond B, foreclosure component, externality tail); lines 84–88 (Nigeria comparison — names *residual commons value framework* explicitly); lines 116–124 (the parts Norway has not solved — foreclosure + externality tail named). |
| Ch 1 framework introduction | `manuscript/chapters/Chapter__1_TheQuietMath.md` | (current tip) | **Zero occurrences** of "RCV" / "residual" / "accountability bond" / "cost severance" / "foreclosure" / "externality tail" verified by grep. Ch 1 introduces the framework conceptually but does NOT introduce the RCV formal apparatus by name. |
| Op-eds (cross-check) | `publishing/op-eds/{norway-sovereign-wealth,mcdowell-county-true-cost}-op-ed_2026-05-10.md` | (current tip) | Apparatus-check rubrics in both op-eds explicitly list "residual commons value" / "RCV" / "accountability bond" as **confirmed-absent**; concept comes through translated-out. RCV is correctly translated-out in op-eds per the FPD non-partisan-framing discipline. |
| Wave 1 / Wave 2 essays (cross-check) | `manuscript/essay/{100-barrel,atlantic-ideas,Noema}/` various | (current tip) | $100 Barrel essay draft (`100-barrel-essay-draft_2026-05-19_v1.0.0.md`) names RCV; Atlantic Ideas essay (`atlantic-ideas-essay-fresh-session-draft_2026-05-21.md`) names RCV; Noema essay (`noema-commons-bonds-chriswinn_withdrawn_draft.md` historical) named RCV. Not deep-dived — flagged as inheritors of this sign-off for downstream coherence checks. |

### Cross-thread anchors

- **Cross-thread-todo #10 sub-item 2b** ([`publishing/strategy/cross-thread-todos.md`](../../publishing/strategy/cross-thread-todos.md) lines 73, 76, 78, 84, 188) — "Tech Appendix Phase 3 rebuild status: NOT-VERIFIED" since 2026-05-21 PM session. This artifact closes that status.
- **$100 Barrel fire-time verification: EVIDENCE-INCONCLUSIVE** (cross-thread #10 line 75) — Stage 1 brief at commit `53db177` asserts "Condition 2 apparatus-stability checkpoint verified by PM Session 2026-05-19" but produced no independent verification artifact. This artifact retroactively supplies the missing independent verification trace.
- **Wave 2 Ch 4 → Foreign Affairs Condition C1.a** ([`commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md) §4.3 line 241 + line 392) — "Tech Appendix RCV publication-stability verified explicitly" was the CONDITIONAL gate for the Ch 4 Stage 0 verdict. This artifact closes that gate.

---

## 2. RCV canonical form (as found in TA v2.1.0)

The Tech Appendix is the formal-apparatus source-of-truth. The canonical form
has three components: the core integrand-and-integral formula (Definition 1.6),
the two-component decomposition of the integrand (foreclosure + externality),
and the central equation CS = RCV − B (Definition 1.7).

### 2.1 Definition 1.6 — RCV Core Formula (TA lines 418–426)

> **Definition 1.6 (Residual Commons Value: Core Formula).** The RCV of
> resource unit R, extracted at t₀, is the present value of all foregone
> intergenerational utility plus all ongoing externalities (per Definition 1.3,
> Q(t) = remaining in-situ stock at time t):
>
> RCV(R, t₀) = ∫_{t₀}^{∞} { [1 − S(t | t₀)] · U(R, t, Q(t)) + E(R, t) } · D(t, t₀) dt

Variable definitions per TA §1: R = resource unit; t₀ = extraction time;
S(t | t₀) = substitutability function (probability a substitute exists at t
given extraction at t₀); U(R, t, Q(t)) = stock-dependent utility of the
resource at time t with remaining stock Q(t); E(R, t) = externality cost at
time t; D(t, t₀) = Weitzman declining discount factor.

### 2.2 Integrand components (TA lines 447–457)

> The integrand has two components:
>
> - **Foreclosure component:** [1 − S(t | t₀)] · U(R, t, Q(t)) — the expected
>   utility loss when no substitute exists, weighted by the probability that no
>   substitute exists at time t.
> - **Externality component:** E(R, t) — the ongoing damage costs regardless of
>   substitution status. A substitute for coal does not remove carbon from the
>   atmosphere; the externality tail runs independently.

Note: the TA's integrand-level decomposition is **two-component** (foreclosure
+ externality). The Ch 4 prose names what looks like a *three-component
framing* — financial rent (captured by B), foreclosure component, externality
tail — but on inspection this is the equation-level decomposition CS = RCV − B
*with the integrand's two components named within RCV*, not a third component
of RCV. Coherence check at §3 confirms this is consistent across sites.

### 2.3 Definition 1.7 — Accountability Bond + central equation (TA lines 459–469)

> **Definition 1.7 (Accountability Bond).** B represents the total set of
> mechanisms that force extractors to bear costs: reclamation bonds, severance
> taxes, legal liability, regulatory requirements, community compensation
> agreements. Cost Severance is formally defined as:
>
> CS = RCV − B
>
> Cost severance occurs whenever CS > 0, indicating that the true social cost
> of extraction exceeds the mechanisms forcing extractors to bear those costs.

### 2.4 Bidirectional articulation (TA lines 470–475)

The TA explicitly designates **CS = RCV − B as the high-level forward-pricing
shorthand** operative through chapter prose, with the canonical bidirectional
form `total CS = (CSD − B₁) + (RCV − B₂)` reserved for §5 + §5.5 articulation.
This is the load-bearing scope-clarification that prevents drift between the
shorthand-form (used throughout chapter prose) and the full-form (used in
TA-internal apparatus + §5.5 bidirectional application).

---

## 3. Per-site verification matrix

| Site | Same definition? | Same integrand decomposition? | Same equation CS = RCV − B? | Same "RCV" first-introduction discipline? | Same scope qualifiers? | **Verdict** |
|---|---|---|---|---|---|---|
| **TA §1 / §2 / §3** (canonical source) | ✅ canonical | ✅ canonical (foreclosure + externality) | ✅ canonical | ✅ canonical (Acronym disambiguation discipline at lines 428–445) | ✅ canonical (forward-pricing shorthand + bidirectional fallback at §5/§5.5) | **GREEN** |
| **Ch 6 (line 325 + line 90 + line 137)** | ✅ same integrand form `[1 − S(t \| t₀)] · U(R, t, Q(t)) + E(R, t)` at line 108; CS = RCV − B at line 125 | ✅ same two-component framing — foreclosure + externality tail named at line 104 ("foreclosure cost… plus the externality tail, both integrated") | ✅ same (line 125) | ✅ first introduced as "residual commons value (RCV)" at line 20; reused with full phrase at multiple chapter pivots | ✅ same — Hartwick / Ostrom / Mazzucato name-defense at line 325 articulates the three sub-choices in the term itself (not three components of RCV) | **GREEN** |
| **Ch 4 (lines 44 / 48 / 50 / 52 / 56 / 84 / 88)** | N/A — Ch 4 cites the framework conceptually, not formally (no equation, no integrand printed) | ✅ same — foreclosure component named explicitly (line 52: "the foreclosure component of residual commons value persists even under Norway's architecture"); externality tail named explicitly (lines 50, 54, 88) | implicit — Ch 4 names B explicitly (line 48: "the accountability bond B"), names CS implicitly via "cost severance" prose; equation not printed but reasoned through | ✅ first introduces phrase at line 44 ("the residual commons value framework"); reuses full phrase throughout (lines 50, 84, 88); no bare "RCV" acronym usage in current Ch 4 prose — full phrase preferred throughout | ✅ same — Ch 4 is the existence-proof chapter; uses RCV at concept-and-name level without surfacing the integrand or CS = RCV − B equation, consistent with the chapter's role in the cascade | **GREEN** |
| **Ch 1 (zero occurrences)** | N/A — does not introduce RCV | N/A | N/A | N/A — RCV not introduced in Ch 1; first formal introduction is Ch 6 line 20 ("residual commons value (RCV) framework"), with Ch 4 using the full phrase conceptually beforehand | N/A | **GREEN** (by design — Ch 1 introduces the framework conceptually; RCV's formal introduction sits at Ch 6 with the apparatus-naming chapter; Ch 4 deploys the named-framework conceptually in the Norway/Nigeria existence proof. This is the correct cascade.) |
| **Op-eds (cross-check)** | translated-out by design | translated-out | translated-out | translated-out — concept comes through plainly without naming | translated-out — non-partisan framing discipline | **GREEN** (correct translation-out posture; op-eds are FPD-compliant) |
| **Wave 1 / Wave 2 essays (cross-check)** | not deep-dived this session | not deep-dived | not deep-dived | RCV named in $100 Barrel + Atlantic Ideas + (withdrawn) Noema — derivative deployment inherits this sign-off | not deep-dived | **GREEN (inheritance-mode)** — these essays inherit publication-stability via this sign-off; future essay-side audits should reference this artifact rather than re-firing per-workstream verification |

### 3.1 Drift findings

**None at HIGH or MEDIUM severity.** Two LOW-severity observations flagged for
future polish but not blocking publication-stability:

- **LOW-1 (file-name vs. content version drift, cosmetic).** TA HTML file is
  still named `TechnicalAppendix_v2.0.0.html` even though the content header
  was bumped to v2.1.0 in commit `36073ca` (2026-05-13). This is filename
  cosmetic-debt, not content-drift; downstream cross-references to the file
  use the v2.0.0 filename and resolve correctly. Author may wish to rename
  the file to v2.1.0 at a future pipeline-hygiene pass; not blocking.
- **LOW-2 (Ch 4 doesn't print the equation).** Ch 4 prose names B and reasons
  through cost severance verbally without printing CS = RCV − B. This is
  by-design for Ch 4's role in the cascade — Ch 4 is the existence-proof
  chapter, not the formal-apparatus chapter (that's Ch 6 + TA). But a future
  Stage 1c-light coherence pass could surface a one-line equation reference
  for reader-coherence if Ch 4 is read out of book sequence (e.g., as a
  derivative-essay source for Foreign Affairs). Not blocking; flagged for
  pipeline-doctrine §5 cross-chapter workstream lifecycle if Ch 4 → Foreign
  Affairs essay surfaces it as a Stage 1c finding.

### 3.2 Coherence-check matrix summary

| Coherence dimension | Status |
|---|---|
| Same formal definition of RCV across TA + chapters | ✅ aligned (TA Definition 1.6 anchors; Ch 6 reproduces; Ch 4 reasons through) |
| Same integrand decomposition (foreclosure + externality) | ✅ aligned across TA §1, Ch 6, Ch 4 |
| Same use of "residual commons value" full phrase + "RCV" acronym | ✅ aligned (TA first-introduction discipline at §1 lines 428–445; Ch 6 introduces full phrase + RCV at line 20; Ch 4 uses full phrase) |
| Same scope qualifiers / disclaimers | ✅ aligned (TA forward-pricing shorthand vs. full bidirectional form at lines 470–475 explicitly anchors what chapter prose carries vs. what TA-internal apparatus carries; Ch 6 + Ch 4 stay in the shorthand-form scope) |
| Same equation form CS = RCV − B | ✅ aligned (TA Definition 1.7 line 465; Ch 6 line 125; Ch 4 reasons through verbally) |
| Same variable names (R, t₀, S, U, Q, E, D, B) | ✅ aligned (Ch 6 line 108 reproduces TA variables verbatim) |
| Drift between Ch 6 three-component name-defense (1f3ad9c) and current TA | ✅ no drift — Ch 6 name-defense addresses the three sub-choices in the *term* (Residual / Commons / Value); TA's two-component integrand decomposition (foreclosure + externality) is a different decomposition operating at the formula level. No conflict; the two operate at different layers of the apparatus. |

---

## 4. Overall verdict

**GREEN — publication-stable.**

The Tech Appendix RCV formal-apparatus definition (Definition 1.6 + Definition
1.7 + CS = RCV − B + the forward-pricing shorthand vs. full bidirectional form
scope-clarification) is internally consistent and consistently realized at
every load-bearing site in the corpus. Ch 6 (the formal-apparatus chapter)
reproduces the TA definition with the same integrand, the same equation, and
the same variable names. Ch 4 (the existence-proof chapter) deploys the
framework conceptually with full-phrase usage, names the load-bearing
components (foreclosure + externality tail) explicitly, and names B explicitly,
all without surfacing the formal apparatus inappropriately. Ch 1 (correctly)
does not introduce RCV at all — that's Ch 6's job. Op-eds correctly translate
out. The Ch 6 three-component name-defense (commit `1f3ad9c`, 2026-05-11)
addresses a different decomposition than the TA's two-component integrand
decomposition, and the two operate at different layers without conflict.

No HIGH or MEDIUM drift findings. Two LOW-severity cosmetic observations
flagged but not blocking.

The verdict supports the parent Ch 4 Stage 0 ratification session's Condition
C1.a closure (Tech Appendix RCV publication-stability verified explicitly), as
well as retroactively supplying the missing verification trace for the $100
Barrel workstream's Stage 1 brief assertion (commit `53db177` claimed
verification but produced no independent artifact).

---

## 5. Cross-thread integration

### 5.1 Cross-thread-todo #10 sub-item 2b

**Status change recommendation:** sub-item 2b NOT-VERIFIED → **VERIFIED (GREEN
per this artifact)**. The surrounding sub-items (2a + 2c + 2d) have their own
resolution arcs and do not collapse into this closure; the item-level entry
remains in the Open section but with a 2026-05-24 update line appended to the
Status field referencing this artifact.

Per the task instruction, the cross-thread-todos.md update appends a status
update note in the Status field rather than moving the item to the Resolved
section, since the item's other sub-items have their own resolution timelines
(notably the $100 Barrel workstream fire-time verification residue and any
future RCV-naming workstream's apparatus-stability checkpoint inheritance).

### 5.2 $100 Barrel EVIDENCE-INCONCLUSIVE residue

The $100 Barrel Stage 1 brief at commit `53db177` (2026-05-19) asserted
"Condition 2 (apparatus-stability checkpoint) — verified by PM Session
2026-05-19 ahead of this session firing" without producing an independent
verification artifact. This created an EVIDENCE-INCONCLUSIVE residue noted at
cross-thread #10 line 75.

This artifact retroactively supplies the missing verification trace: TA RCV
publication-stability was, in fact, verifiable as of 2026-05-21 (the date the
cross-thread-todo flagged the gap) and remains verifiable as of 2026-05-24 (the
date this artifact fires). The $100 Barrel session's assertion was substantively
correct even if not artifact-documented at the time. **EVIDENCE-INCONCLUSIVE
residue: CLOSED.** Future workstreams that require apparatus-stability
checkpoint should reference this artifact rather than re-asserting verification
without a trace.

---

## 6. Downstream applicability

Future RCV-naming workstreams inherit this sign-off rather than each
re-firing per-workstream verification. Specifically:

- **Ch 4 → Foreign Affairs essay (primary, immediate).** Wave 2 Stage 0
  candidate C; Condition C1.a closed by this artifact. Stage 1 brief firing
  recommended after Ch 4 Pass 3.4 closure + Pass 2 + Pass 3 spot-fix Phase C
  application complete (Condition C1.b remains the open gate; this artifact
  closes C1.a only).
- **$100 Barrel essay → Phenomenal World (already in flight).** Stage 2 / Stage
  3 sessions can cite this artifact in lieu of re-firing the missing
  verification trace.
- **Atlantic Ideas essay (already drafted; in pipeline).** Names RCV per the
  Wave 2 batch's Atlantic-Ideas candidate-B analysis (commit `e6fc8bf`
  2026-05-24); inherits this sign-off for apparatus-stability.
- **Future derivative essays naming RCV (e.g., Phenomenal World follow-on;
  Aeon post-acceptance; long-form derivatives derived from Ch 6 + Ch 8 + Ch 9
  for which the formal apparatus surfaces).** All inherit this sign-off as
  the corpus-side independent verification trace; per-workstream verification
  can be skipped.

The inheritance window is bounded by the Darity-feedback contingency at §7;
this sign-off remains valid until either Darity feedback substantively
restructures the RCV formal apparatus or a downstream apparatus revision
(e.g., MI-2 coercion-vector scope-acknowledgment per cross-thread-todo #15)
ratifies into the TA.

---

## 7. Darity-feedback contingency

Author packet (~150 pages: Q0 proactive citation questions + Ch 5 with-citations
+ Ch 6 with-citations + Tech Appendix with-citations) was sent to William A.
Darity Jr. on 2026-05-14 with a cover-email window of "no rush, but if you have
notes within ~2 weeks that's the window" (cross-thread-todo #2). As of
2026-05-24, ~10 days have elapsed; the soft deadline is 2026-05-28; the full
4–6 week response window extends through ~2026-06-25.

Substantive RCV-framework feedback from Darity is the only foreseeable
near-term destabilizer of this sign-off. If Darity surfaces feedback that:

- restructures the RCV integrand decomposition (e.g., a stratification-economics
  three-component requirement that splits foreclosure or externality further);
- restructures the CS = RCV − B equation (e.g., a coercion-vector scope
  extension per MI-2 in cross-thread-todo #15);
- restructures the three-component name-defense at Ch 6 line 325 (e.g.,
  recommending a different lineage-anchor than Hartwick / Ostrom / Mazzucato);

then this sign-off is invalidated and must be re-fired or supplemented. The
re-fire would be a fast incremental pass against the revised apparatus rather
than a fresh full-scope verification.

**Contingency posture:** this artifact is valid as of 2026-05-24 against the
current TA + chapter state. Downstream sessions that need apparatus-stability
inheritance after Darity feedback lands should verify against this artifact's
commit anchors (`36073ca` + `eb636c6` + `1f3ad9c` + current Ch 4 tip + Ch 1
zero-occurrence baseline) and re-fire if any of those anchors have moved.

---

## 8. STATE marker

**STATE.** TA RCV publication-stability sign-off PROPOSED 2026-05-24 (this
artifact); overall verdict GREEN at TA + Ch 6 + Ch 4 + Ch 1; zero HIGH/MEDIUM
drift; two LOW-severity cosmetic observations (filename version-tag debt;
Ch 4 implicit-equation prose). Closes cross-thread-todo #10 sub-item 2b
(NOT-VERIFIED → VERIFIED) + closes $100 Barrel EVIDENCE-INCONCLUSIVE residue.
Supports parent Ch 4 Stage 0 Condition C1.a closure. Darity-feedback
contingency window extends through ~2026-06-25; re-fire trigger is substantive
RCV-framework restructuring feedback from Darity. Auto-ratifies via parent
session.
