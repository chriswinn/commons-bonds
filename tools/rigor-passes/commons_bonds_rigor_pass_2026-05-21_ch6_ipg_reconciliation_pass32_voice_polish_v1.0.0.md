# Stage-3 Pass 3.2 Voice-Polish — Ch 6 IPG Reconciliation Paragraph (Cascade Follow-on)

**Date:** 2026-05-21
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — automatic-on-edit cascade follow-on to the Ch 6 IPG methodology-reconciliation Phase C (commit `dd825f2`, 2026-05-21).
**Chapter file:** [manuscript/chapters/Chapter__6_ThreeWaysofCounting.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) — 343 lines post-Phase-C.
**Mode:** Spot Pass 3.2 (cascade automatic-on-edit per v3.1 Amendment A) on the ~150 words newly added at lines 175 + 177. Scope is voice-polish only on the new prose; not a full Ch 6 Pass 3.2. Pass 3.1 fact-check + Stage 1c-light coherence skipped as completed-by-source-construction during the parent reconciliation artifact (source: Tech Appendix §11.11 prose, already audited).
**Hard constraint observed:** No chapter file modified in this session. Phase C application of ratified spot-fixes pending author ratification at §6.

---

## §1. Scope + canonical sources

### §1.1. Scope

The Ch 6 IPG methodology-reconciliation Phase C (commit `dd825f2`) added a new reconciliation paragraph at line 177 + restructured line 175. Per v3.1 Amendment A, prose-edit events automatically fire **Pass 3.1 fact-check + Pass 3.2 voice-polish + Stage 1c-light coherence**. The parent reconciliation artifact ([tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch6_ipg_methodology_reconciliation_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch6_ipg_methodology_reconciliation_v1.0.0.md)) documents that the new prose's substantive claims are sourced verbatim from Tech Appendix §11.11; Pass 3.1 and Stage 1c are completed-by-source-construction. **This artifact runs Pass 3.2 voice-polish only.**

### §1.2. Canonical sources

1. [manuscript/chapters/Chapter__6_ThreeWaysofCounting.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) lines 175 + 177 — new prose under audit.
2. [~/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_em_dash_overuse.md](~/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_em_dash_overuse.md) (mirrored: [tools/memory/feedback_em_dash_overuse.md](tools/memory/feedback_em_dash_overuse.md)) — **em-dash overuse discipline ratified 2026-05-21** during Ch 3 Pass 3.2 F-V3 ratification. *"Treat em-dash use as a flag requiring active justification, not a default punctuation choice. Default to commas/periods/restructure for smoother prose."*
3. [tools/memory/feedback_voice_polish_pipeline.md](tools/memory/feedback_voice_polish_pipeline.md) — Pass 3.2 voice-polish discipline.
4. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-20_ch3_thewaterman_stage3_pass3.2_voice_polish_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-20_ch3_thewaterman_stage3_pass3.2_voice_polish_v1.0.0.md) — Ch 3 Pass 3.2 format reference; the session that ratified the em-dash memory entry.
5. [tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch6_ipg_methodology_reconciliation_v1.0.0.md](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch6_ipg_methodology_reconciliation_v1.0.0.md) — parent reconciliation artifact + Phase C application record.

---

## §2. Findings

### §2.1. Whole-prose audit summary

The new prose comprises ~150 words across two paragraphs (Ch 6 lines 175 + 177). Audit dimensions checked:

| Dimension | Finding | Severity |
|---|---|---|
| Em-dash overuse | **Two bracketed em-dash pairs (4 em-dashes total) are default-punctuation choices** per the 2026-05-21 discipline | **MEDIUM (F-V1)** |
| Rule-of-three / LLM cadence | None detected | OK |
| Meta-commentary | "A reader carrying Chapter 2's framing forward will notice a different number" is meta-narration; load-bearing for pedagogical setup of the reconciliation | OK (load-bearing) |
| Italicized emphasis | One use ("*which time horizon*"); load-bearing emphasis on the methodological pivot | OK |
| Hyphenated number phrases | "thirty-three-to-one-twenty-two-times" + "fifty-to-five-hundred-fifty-five-times" — consistent with chapter voice (cf. existing "three-hundred-ten to eighteen-hundred-dollar-per-ton-of-coal" at line 129) | OK |
| Source-attribution convention | Chapter's existing convention for source-attribution is parentheses (cf. lines 16, 102, 129); the new line 175's em-dash bracketed source attribution diverges from chapter convention | Folded into F-V1 |
| "Not X; Y" rhetorical structure | "The framework is not committed to a single number; it is committed to a method that makes the time-horizon attribution explicit" — load-bearing for the methodology-over-number pedagogical claim | OK |

**Net audit verdict:** one MEDIUM finding (F-V1, em-dash overuse). All other voice-polish dimensions check clean.

### §2.2. Chapter-context em-dash baseline

For calibration context (not finding): the full Ch 6 file contains 83 em-dashes across 343 lines (~0.24 em-dashes per line). Chapter voice has historically used em-dashes heavily; the new prose's em-dash density (5 across 2 lines including link-title em-dash; 4 in running prose) is **consistent with chapter voice baseline but is the precise pattern the new discipline flags**. A future Ch 6 Pass 3.2 (full-chapter scope) would likely surface em-dash drift across the entire chapter; this spot Pass 3.2 only addresses the newly-added prose.

---

### §2.3. Finding F-V1 (MEDIUM) — Em-dash overuse in the new reconciliation prose

**Sites:**

- **Ch 6 line 175** — bracketed em-dash pair around source attribution:
  > McDowell coal's per-case implied IPG of approximately fifty times **—** anchored at the Technical Appendix's three-method implied cost-severance summary in §3.6 Block 4 **—** falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate.

- **Ch 6 line 177** — bracketed em-dash pair around Method-1 descriptor apposition:
  > The thirty-three-to-one-twenty-two-times canonical reflects Method 1 **—** Replacement Cost **—** alone, anchored to engineering-time-scale substitutability.

**Drift analysis per the em-dash discipline:**

Both em-dash pairs are bracketed parenthetical em-dashes (the precise pattern the 2026-05-21 discipline ratifies as default-punctuation-without-active-justification). Per the discipline: *"Default to commas/periods/restructure for smoother prose."*

**Convention check against chapter's existing source-attribution + descriptor-apposition patterns:**

- **Source-attribution convention (line 175 case):** Ch 6's existing convention for source-attribution at parenthetical insertions is **parentheses**, not em-dashes:
  - Line 16: `(formal articulation in [Technical Appendix §3 — RCV Quantification — Three Ways of Counting]...)`
  - Line 102: `(formal articulation in [Technical Appendix §3 — RCV Quantification — Three Ways of Counting]...)`
  - Line 129: `(Formal specification in [Technical Appendix §3.3 — Method 1: Replacement Cost]...)`
  - The new line 175 bracketed em-dash source attribution **diverges** from chapter convention.

- **Descriptor-apposition convention (line 177 case):** Ch 6's existing pattern for "Method N — Descriptor" in running prose is the *unbracketed* em-dash where the descriptor flows directly into the next clause (line 135: "Method 1 — Replacement Cost specializes to..."), not the bracketed parenthetical em-dash my new prose uses ("Method 1 — Replacement Cost — alone"). The new line 177 bracketed em-dash apposition is a **new pattern** not present in chapter convention.

The em-dash overuse is therefore both (a) flagged by the 2026-05-21 discipline as default-punctuation, AND (b) inconsistent with the chapter's existing convention for these specific prose contexts. Two compounding reasons to spot-fix.

**Severity: MEDIUM.** Not chapter-wide; one short reconciliation paragraph; readers will not be load-bearingly misled by the em-dashes. But the discipline is fresh + the pattern is exactly what the discipline flags, and a fix is cheap. Calibrating MEDIUM rather than HIGH because the substantive claim is correct and reader-coherence holds even with the em-dashes; the fix is voice-polish, not fact-check or coherence-repair.

**Options:**

**Option A — Replace both em-dash pairs with commas + accept minor comma-density:**

Line 175: "McDowell coal's per-case implied IPG of approximately fifty times, anchored at the Technical Appendix's three-method implied cost-severance summary in §3.6 Block 4, falls..."

Line 177: "The thirty-three-to-one-twenty-two-times canonical reflects Method 1, Replacement Cost, alone, anchored to engineering-time-scale substitutability."

Issues: Line 175 reads cleanly. **Line 177 reads choppy** — four commas in close proximity ("Method 1, Replacement Cost, alone, anchored") interrupt the prose flow at exactly the moment the sentence is doing pedagogical work.

**Option B — Replace both em-dash pairs with parentheses (recommended):**

Line 175: "McDowell coal's per-case implied IPG of approximately fifty times (anchored at the Technical Appendix's three-method implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate."

Line 177: "The thirty-three-to-one-twenty-two-times canonical reflects Method 1 (Replacement Cost) alone, anchored to engineering-time-scale substitutability."

Advantages: Line 175's source-attribution-in-parens is **directly consistent with chapter's existing convention** (lines 16, 102, 129). Line 177's "Method 1 (Replacement Cost) alone" reads smoothly without comma-density. Both pairs eliminate em-dashes without restructuring prose architecture.

**Option C — Restructure to remove the parenthetical inserts entirely:**

Line 175: "Per the Technical Appendix's three-method implied cost-severance summary (§3.6 Block 4), McDowell coal's per-case implied IPG of approximately fifty times falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate."

Line 177: "The thirty-three-to-one-twenty-two-times canonical reflects Method 1 alone (Replacement Cost), anchored to engineering-time-scale substitutability."

Issues: Line 175's restructure leads with the source attribution, which inverts the prose's information hierarchy (the McDowell IPG should be the subject, not the appendix). Line 177's "Method 1 alone (Replacement Cost)" is awkward because the parenthetical descriptor is now disconnected from the method-name. Restructure overshoots a fix that mechanical punctuation swap (Option B) solves cleanly.

**Option D — Keep em-dashes; argue active justification:**

Argument: The em-dashes do work that commas/parens would not — they signal the parenthetical's significance (source attribution; method descriptor). Counter: the em-dash discipline explicitly says **the burden of justification is on the em-dash**, not on the alternatives. The em-dashes here do not carry meaning the parens cannot carry; the discipline default applies.

**Recommendation: Option B.** Both punctuation swaps respect the 2026-05-21 em-dash discipline AND align the new prose with chapter convention (source-attribution-in-parens at lines 16, 102, 129; descriptor-apposition in clean form). Mechanical fix, no restructure, no semantic loss.

**Reasoning:**

- Option A is mechanically correct but produces a comma-density problem at line 177 that the parentheses option avoids.
- Option B is the cleanest mechanical fix: preserves the apposition semantics, swaps the punctuation, no restructure required, matches chapter convention for source-attribution.
- Option C overshoots — restructure where punctuation-swap suffices; introduces awkward "Method 1 alone (Replacement Cost)" word order.
- Option D fights the discipline. The em-dashes here are default-punctuation; the discipline says default-away.

**Proposed Option B verbatim replacement prose:**

**Line 175 (full paragraph replacement):**

> McDowell coal's per-case implied IPG of approximately fifty times (anchored at the Technical Appendix's three-method implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate.

**Line 177 (only the affected sentence; rest of paragraph unchanged):**

Replace:

> The thirty-three-to-one-twenty-two-times canonical reflects Method 1 — Replacement Cost — alone, anchored to engineering-time-scale substitutability.

With:

> The thirty-three-to-one-twenty-two-times canonical reflects Method 1 (Replacement Cost) alone, anchored to engineering-time-scale substitutability.

**Net Ch 6 prose change:** four em-dashes removed; two parentheses pairs added; ~6 character net change; no semantic change; no restructure; no line-count shift (file remains 343 lines).

---

## §3. Ratification summary

| Finding | Severity | Site | Recommended option | Phase C touch |
|---|---|---|---|---|
| **F-V1** — Em-dash overuse in new reconciliation prose | **MEDIUM** | Ch 6 lines 175 + 177 | **Option B** (replace both em-dash pairs with parentheses) | Ch 6 lines 175 + 177; ~6 character net change; no line-count shift |

---

## §4. Cross-chapter consequences

**None.** F-V1's Option B is a mechanical punctuation swap on the new prose only. No Ch 2 / Ch 8 / Tech Appendix touches required. Cross-chapter inventory line 89 line citations (175 + 251) remain valid (no line-count shift).

---

## §5. Phase C application sequencing

Single Ch 6 spot-fix (lines 175 + 177); two atomic edits in one Phase C commit.

**Phase C session scope:** trivially small. One file. One finding. Per-prompt serial cadence does not apply.

---

## §6. Ratification record

**Author ratification:** **RATIFIED 2026-05-21** by author direct ratification ("as recommended"). Phase C application authorized in the same session per CLAUDE.md author-ratified-content-change merge-to-main default.

**Disposition (F-V1 — Em-dash overuse):**

- Option A (commas — line 177 reads choppy): [ ]
- Option B (parentheses; chapter-convention-aligned) — **recommended**: [x] **RATIFIED**
- Option C (restructure): [ ]
- Option D (keep em-dashes): [ ]
- Other / custom (specify): [ ]

**Cross-chapter consequence list ratified as written (§4 — none):** [x] **Yes — no cross-chapter touches required.**

**Phase C bundling decision:**

- Apply F-V1 Option B as standalone single-atomic Phase C commit — **recommended**: [x] **RATIFIED standalone**
- Defer until a future full Ch 6 Pass 3.2 session (would catch this + likely other chapter-wide em-dash drift): [ ]
- Other (specify): [ ]

**Phase C application record (2026-05-21, same session as ratification):**

- Ch 6 line 175 em-dash pair (source attribution) → parentheses, per §2.3 Option B verbatim proposed prose.
- Ch 6 line 177 em-dash pair (Method 1 descriptor apposition) → parentheses, per §2.3 Option B verbatim proposed prose.
- Net Ch 6 change: 4 em-dashes removed; 2 parens pairs added; ~6 character net change; no line-count shift (file remains 343 lines).
- Both edits applied in a single atomic Phase C commit; per CLAUDE.md author-ratified-content-change default the session fast-forwards to `origin/main` at session close.

**Notes:**

The full Ch 6 chapter contains 83 em-dashes across 343 lines; a future full Ch 6 Pass 3.2 (chapter-wide scope) will likely surface broader em-dash drift beyond this spot finding. This Pass 3.2 cascade follow-on addresses only the newly-added prose per the v3.1 Amendment A automatic-on-edit cascade scope; the chapter-wide em-dash drift remains for a future full Ch 6 Pass 3.2 session.

---

*End of Ch 6 IPG reconciliation paragraph Pass 3.2 voice-polish cascade artifact. Phase C application sequencing in §5 awaits author ratification at §6. The chapter file is unchanged in this session.*
