# Flagship-Equation Terminology Defense Sweep (Narrow) — Workstream Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch to create at session start:** `claude/flagship-terms-defense-sweep-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Status going in:** Bond-defense work for Ch 5 landed 2026-05-11 (commits `f5f905e` → `1c83753`). That work surfaced a generalizable gap pattern — foundational framework choices asserted across the book + carried by the title but never argued in body prose. The author has requested a **narrow** sweep over the rest of the flagship equation **CS = RCV − B** (plus the B = B₁ + B₂ decomposition) to verify the same gap isn't open elsewhere. Narrow first; widen only if the narrow sweep finds evidence the discipline isn't holding generally.

---

## Workstream scope

For each flagship-equation term whose name is currently asserted-but-never-defended in publisher-facing body prose, produce:

(a) a **gap-audit verdict** (is the term currently defended in body prose? where? sufficient against the 20-character book-audience pressure-test set?);
(b) where a gap exists, a **draft body-prose justification paragraph** (Stage 2 audience-blind, ~200–300 words, substance-driven); and
(c) an **include-vs-exclude audience-load rigor pass** against the 20-character book-audience set (Tier 1 + Tier 2 + Tier 3 per the 2026-05-11 rigor-pass).

Mirror the methodology + artifact pattern the bond-defense established. No new framework concepts; defend only existing terminology choices.

---

## Scope — four terms, in narrow order

### 1. Cost Severance (CS)

The term the whole book is naming. Currently anchored only to an employment-severance metaphor in the glossary. Body prose demonstrates the mechanism through cases (extensively) but has never argued the **name choice** at the term-justification level. Sweep verdict: does any chapter defend "why *severance* vs. *externality* / *displacement* / *transfer* / *appropriation*"?

### 2. Residual Commons Value (RCV)

Three loaded sub-choices each doing different lineage work:
- *residual* — Hartwick's rule for sustainable extraction (1977) and the residual-claim tradition in resource economics.
- *commons* — Ostrom's commons-governance lineage; the framework's structural-identity definition.
- *value* — Mazzucato's *Value of Everything* (2018); value-as-extracted-vs-value-as-created distinction.

The term-as-a-whole has not been argued in body prose. Sweep verdict: defended anywhere?

### 3. Restitution Bond (B₁)

Likely partial coverage via Ch 5 lines 192–194 (Coates → Darity-Mullen → Hamilton → Conley → Pistor legal-architecture lineage). Sweep verdict: is existing coverage sufficient as a name-level defense, or does "why *Restitution* specifically" need its own paragraph (i.e., why *Restitution* and not *Reparations* / *Restoration* / *Indemnification* / *Damages*)?

### 4. Foreclosure Bond (B₂)

Likely partial coverage via Ch 5 lines 198–200 (Hartwick + reclamation bonds + Norway-SWF + Pettit-Skinner civic-republican lineage). But the term carries an unwanted primary association with 2008 mortgage foreclosure that an unprepared reader hits first. Sweep verdict: should the name-defense engage that association directly? Or does existing lineage prose route around it sufficiently?

---

## Per-term deliverables

For each of the four terms, produce one of:

**(a) Gap-audit verdict — NO GAP.** A short justification of why existing body-prose treatment is sufficient. Cite the chapter + line ranges that do the work. Single paragraph; no further artifacts.

**(b) Gap-audit verdict — GAP CONFIRMED.** Produce:

- Stage 2 audience-blind draft (~200–300 words, substance-driven, single body paragraph) per the v2.0 audience-aware drafting discipline. Save under `tools/drafts/<term-slug>-defense-paragraph_2026-05-11_v1.0.0.md` (mirror the bond-defense filename convention).
- Stage 3 three-pass audit (fact-check + voice-polish + audience-load) per the v2.0 Stage 3 discipline. The audience-load pass uses the 20-character book-audience pressure-test set (Tier 1 + Tier 2 + Tier 3 per `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md`). Save under `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_<term-slug>_defense_paragraph_include_vs_exclude_audience_load_v1.0.0.md`.
- Placement recommendation (which chapter + which line range).
- Author ratification required before any chapter edits land.

---

## Methodology — mirror the discipline the bond defense established

Apply rigorously:

- **Two-stage v2.0 audience-aware drafting** per `/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md` (RATIFIED 2026-05-10).
- **Two-layer content origination (WP#10)** per `feedback_two_layer_content_discipline.md` — these paragraphs ARE external-publisher-facing prose; classify accordingly.
- **Voice + polish pipeline** per `feedback_voice_polish_pipeline.md` — actively polish.
- **Substance drives length** per `feedback_substance_drives_length.md` — no padding to hit a target; no cutting to fit.
- **20-character book-audience pressure-test set** (Tier 1 + Tier 2 + Tier 3) — pulled from the 2026-05-11 rigor-pass model artifact.
- **No new framework concepts.** Defend only existing terminology choices.
- **No symbols, no Greek letters, no subscripts in body prose.** Named instruments OK (Restitution Bond / Foreclosure Bond as words, not as B₁ / B₂).
- **Path B preemptive policy** — generate fresh prose; do not paraphrase Ch 1 / Ch 5 existing body text into the new defense paragraphs.

---

## Model artifacts to study + mirror

Read before drafting:

1. **Drafting artifact:** `tools/drafts/why-bonds-paragraph_2026-05-11_v1.0.0.md`
2. **Audience-load rigor pass:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md`
3. **Ratified Ch 5 insertion:** commit `1c83753` — see the paragraph as integrated between current line 190 and line 192 of `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md`.

For terms #3 (Restitution Bond) and #4 (Foreclosure Bond), also read the existing Ch 5 lineage prose at lines ~190–214 (the Restitution / Coates / Darity-Mullen / Hamilton / Conley / Pistor lineage paragraphs + the Foreclosure / Hartwick / reclamation-bonds / Pettit-Skinner lineage paragraphs). The gap-audit needs to determine whether those existing paragraphs already do the name-defense work, or whether they only do the *mechanism* / *lineage* work without addressing the *name choice*.

---

## Hard constraints — what NOT to do

- Do NOT edit any chapter file without author ratification of draft + placement.
- Do NOT introduce new framework concepts. Defend only existing terminology choices.
- Do NOT produce multi-paragraph essays per term. One body paragraph each, like the bond defense.
- Do NOT deploy apparatus (B, B₁, B₂, RCV, ∫, Σ, Cᵢ, Greek letters) in any draft. Named instruments only.
- Do NOT paraphrase Ch 1 prose (Path B preemptive policy).
- Do NOT propose meta-conclusions about the discipline framework. Stay scoped to the four terms.

---

## Widening trigger

After the narrow sweep produces verdicts for all four terms:

- **0–1 gaps confirmed:** the bond case was near-a-one-off. Recommend NO broader pass. Single-line PM-session note suffices.
- **2+ gaps confirmed** (terms where a body-prose defense is missing AND the audience-load rigor pass returns INCLUDE): the terminology-defense discipline isn't holding generally. **Recommend widening** to the broader candidate set:
  - CIT (Commons Inversion Test)
  - ARR (Asymmetric Regret Rule)
  - Hotelling Identity
  - Externality Tail
  - Abundance Masking
  - The Cᵢ component set
  - Three-method-convergence-for-RCV

Report the widening recommendation in the PM-session deliverable below.

---

## Branch discipline (per `tools/workstream-handoffs/README.md`)

- Fresh feature branch from `origin/main` after `git fetch`.
- Author ratification required before any chapter edits land.
- Per WP#9: merge per ratified chunk via `git push origin HEAD:main`.

---

## PM-session deliverable at completion

The session reports back to the PM session with:

1. **Per-term gap-audit summary** (4 terms × audit verdict).
2. **Per-gap artifacts** (draft + rigor pass) committed to the feature branch, ready for author ratification.
3. **Widening recommendation** — narrow-was-enough OR broaden-to-set-X.

The PM session auto-verifies per §10.5 of the PM session handoff and updates the dashboard accordingly.

---

## Cross-references

- **Bond defense model artifacts** (2026-05-11):
  - `tools/drafts/why-bonds-paragraph_2026-05-11_v1.0.0.md`
  - `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md`
  - Ch 5 insertion commit `1c83753`
- **v2.0 discipline memory:** `/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md`
- **Apparatus register sweep workstream** (#9) — concurrent in-flight workstream covering apparatus-as-jargon decisions; this terminology-defense sweep is the complementary "we keep these names but justify them" pass.
- **PM session handoff:** `tools/workstream-handoffs/archive/pm-session-handoff_2026-05-10.md` §3 dashboard row #13 (this workstream).

---

*End of workstream handoff. Update in place if scope evolves; mark complete via PM session auto-verify discipline.*
