# TA whole-document internal-scaffolding re-scan — findings (2026-06-09)

**Session:** `claude/ta-m3-resume-260609-151562` (M3/integrity successor).
**Scope:** the publisher-facing Technical Appendix
`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (8,007 lines).
**Trigger:** Session-D closeout flagged a SCAFFOLDING-CHECKER GAP — the corpus-invariant
checker (`check-corpus-invariants.sh`) catches only the Option-letter / TODO / glyph
families; it MISSES the class that leaks internal-audience / rigor-test / pipeline /
chapter-author-instruction / cross-draft-reconciliation / revision-history language into
reader-facing prose. Author direction 2026-06-09: "ensure we aren't talking about our
internal audience, or rigor tests as that doesn't really mean anything to anyone else."
**Method:** manual whole-file scan (parent session) + three sub-agents reading thirds
(1–2700 / 2700–5400 / 5400–8007). All findings independently spot-verified in context.
**Status of edits: ALL TIERS RATIFIED + APPLIED 2026-06-09.** Tier-1 (4 items) commit
`8dc1389`; Tier HIGH/MED/LOW (32 targeted + 1 global) applied as a single assertion-guarded
batch (the scaffolding-sweep commit). 0 residual scaffolding-class phrases remain in the TA.
Substance preserved throughout; only internal framing stripped. All MERGE-HOLD.

---

## Headline results

- **M3 sections (§3.5 / §11.5 / §11.6 / §11.8 / §11.11) are CLEAN** of this class. Session D's
  §11.11 cleanup held. The item the handoff assigned to this session ("clean M3-section
  scaffolding") returns empty.
- The leaks cluster in **non-M3 sections**: §5.2 (naming), §6.4–6.7 (CIT walkthrough),
  §11.5/§11.6/§11.8/§11.9/§11.10 (case framing asides), §14 (cross-framework engagement),
  §15.1–§15.2 (Limitations + term-justification apparatus).
- Two recurring patterns dominate: (1) the **"Option C'"** internal design-option label used as
  if it were a named framework component (≥6 occurrences); (2) **"alternative-tested" /
  "dinner-table" / "multi-audience-register"** rigor-test + accessibility-test vocabulary inside
  the §15 naming footnotes.

---

## Tier-1 — APPLIED (commit `8dc1389`, MERGE-HOLD, ratified 2026-06-09)

| Loc | Was | Now |
|---|---|---|
| §5.4 L1448 | "Coordination note (B₁-direction moral grounding) … subsequent-revision question … logged here without prescribing the resolution" | "Backward-direction moral grounding." + substantive close (Parfit person-affecting → backward harm via reparations-economics lineage kept) |
| §15.2.1 L6959 | "(c) Ch 1 Option C bridge plan converts the HR collision into a teaching on-ramp" | clause dropped (criteria list now (a)/(b)) |
| §15.2.3 L7292 | "when Ch 4 frames future-generation foreclosure … without forcing every reader to pattern-match" | "Naming the specialization makes the intergenerational application explicit rather than leaving it to be inferred from the general option-value literature." |
| §10 Thm 10.5 L3771 | "requires RCV > P (per the revised P1)" | "(per P1)" |

---

## Tier HIGH — PROPOSED (unambiguous internal scaffolding; recommend remove/reframe)

| Loc | Verbatim (short) | Class | Recommended fix |
|---|---|---|---|
| §6.4.1? L1970 | "AIT's pre-CIT framing obscured this." | retired internal name + revision-history | delete; the point stands without it (AIT = superseded name for CIT, explained at §15.1.8) |
| §6.7 L2182 | "Strong M5 dinner-table case." | internal pass-code (M5) + accessibility-test shorthand | delete (prior sentences already make the universality point) |
| §6.7 L2254 | "Also a key adoption case for medical professionals + healthcare policy reformers (the framework's vocabulary travels into medical-ethics discourse)." | adoption/marketing meta | delete sentence |
| §14 L6494 | "This section, entirely absent from the prior Technical Appendix, is the most important addition for academic credibility." | revision-history + editorial self-rationale | delete first sentence; keep "Reviewers and economists will ask how RCV relates to existing frameworks. This section answers that…" |
| §15.1.6 L6760/6770/6830/6834/6928 | "Option C'" (×5) as a framework-component name | Option-letter pipeline label | drop "Option C'" tag throughout; refer by substance ("the examples-not-canonical posture") |
| §15.2.1 L6959 | "Six rename candidates were alternative-tested at multi-audience-register depth … (a) dinner-table accessibility" | rigor-test + accessibility-test vocabulary | "Six rename candidates were considered … (a) lay accessibility" |
| §15.2.2 L7092 | "Seven rename candidates were alternative-tested … (b) dinner-table accessibility via mortgage-foreclosure analogy" | same family (Foreclosure-Bond footnote) | "were considered" / "lay accessibility" |

## Tier MED — PROPOSED (reframe; legitimate substance underneath, internal framing on top)

| Loc | Verbatim (short) | Class | Recommended fix |
|---|---|---|---|
| §5.2 L1240 | "narrows framework adoption to politically-progressive audiences … reaching center-right, libertarian … who would disengage at 'Reparations.'" | adoption framing | substance-first: "'Reparations' carries US-political-specific loading; 'Restitution' preserves the restoration-of-what-was-taken meaning with broader cross-tradition scope (legal, civil-law, international-law)." |
| §5.2 L1279/L1309 | "dinner-table-strong via mortgage-foreclosure analogy" | accessibility-test shorthand | "intuitively accessible via the mortgage-foreclosure analogy" |
| §6.x L1758 | "(Option C' political-philosophical-accommodation: …)" | Option-letter label | drop the "Option C'" tag, keep the parenthetical's substance |
| §11.5 L4200 | "…a remaining commons-loss per case file: 'the barrel is still gone'" | internal-doc pointer | delete "per case file"; keep the claim |
| §11.5 L4260 | "Per the case file: 'Norwegian-welfare-state is approximately B₁-for-Norwegian-citizens …'" | internal-doc pointer | delete "Per the case file:"; restate in published register |
| §11.5 L4244 | "(down marginally from prior $50/BOE anchor … updated production denominator drives a small directional shift)" | cross-draft reconciliation | delete the parenthetical (reader needs the current figure, not the delta) |
| §11.6 L4516 | "§7.4 Gate 4's worked example uses … for framework-introduction" / "McDowell-specific worked-example register" | editorial-register rationale | state the two bases + that both derive from EPA AP-42 §1.1; drop "register"/"framework-introduction" framing |
| §11.8 L5350–5397 (+5055/5081) | "framework debate-narrowing", "optimal contested-surface positioning", "Framework-positioning implication" | strategy/positioning meta | keep the substantive point (for Earth-bound cases the dispositive question is irreversibility); strip "contested-surface/debate-narrowing/positioning"; retitle subhead → "Which parameter the RCV debate turns on" |
| §11.9 L5567 | "The framework's Method 1 anchor should report all three ranges …" | instruction-to-self | "The Method 1 anchor reports all three ranges …" |
| §11.9/11.10 L5704/L5770 | "academic-credibility positioning" (×2) | reception/adoption meta | "useful as a steelman upper bound" / "strengthen the empirical grounding" |
| §15.1 L6618 | "Each … was alternative-tested" + "reader-facing depth (~2,000 words) … academic-reviewer depth" | process vocabulary + register/word-count meta | "the rejected alternative is specified, and the lineage the choice extends is cited"; drop word-count/register-depth labels |
| §15.2 L6950 | "Each was alternative-tested alongside lineage citations … The footnotes below preserve that structure" | process vocabulary | "Each carries a rejected alternative, lineage citations, and cross-political-tradition handling, set out below" |
| §15.2.2 L7107 | "the trauma-affect on jacket-marketing register is honored via Ch 9 bridge prose" | book-production/marketing vocabulary | "the term's affective charge is honored via Ch 9 bridge prose at first introduction" |
| §15.2.3 L7230 | "Ch 4's argument relies on reader-side translation … which the chapter's audience does not uniformly carry" | reader-cognition aside | "Naming this specialization makes the intergenerational application explicit rather than leaving it to be inferred from the general option-value literature." (matches the already-fixed L7292 sibling) |

## Tier LOW — PROPOSED (mechanical / low-risk; flagged for completeness)

| Loc | Verbatim (short) | Class | Recommended fix |
|---|---|---|---|
| §5.x L1412 | "(Ch 6 line 304 et seq.)" | manuscript line-number cross-ref (won't survive typesetting) | "(Ch 6)" |
| §6.7 L1924 | "(Personal Stories Candidate #1)" | internal content-pipeline label | delete parenthetical |
| §6.x L2100 | "Tech Appendix §L formal specification requires:" | stale lettered-section reference | point to the actual numbered section (e.g. "The Independence gate (§7.4) …") |
| §5.x L532 | "pre-drafting items are research-supporting material" | process vocabulary | reframe or drop "pre-drafting items" |
| §15.2.3 L7218 | "The decisive criterion was argument-load-bearing" | internal-rationale phrasing | optional light reframe ("The decisive consideration was that Ch 4 builds its central argument on option-value reasoning") |

## Considered-but-KEPT (weighed, judged legitimate — do NOT clean)

- §7.7 L2934 "applied to commons categories in the framework's earlier development" — genuine
  "Relationship to Prior Methodology" intellectual-history exposition.
- §10 L3724–3771 "Path A: Extract R / Path B: Invest in substitute" — a math/theorem construct
  (weak-dominance proof), NOT a rework label.
- §7.x / §17 "Future analysts can apply CIT + the four gates…", "organizational scaffolding over
  variables", "A book-internal convention: … n = 2 restriction in a footnote" — legitimate
  methodological-extensibility + notation-convention exposition.
- §11.7 "Initial hypothesis … NOT SUPPORTED / Reframed hypothesis" — genuine empirical
  hypothesis-testing exposition, not draft-rework process.
- §15.1 term-justification structure (rejected-alternative + lineage citations) — standard
  academic apparatus; only the pipeline-specific phrases riding inside it are flagged above.
- Posited-vs-sourced self-labels ("a calibration parameter, not an external datum"; "a framework
  estimate, not a sourced figure") — the peer-review-defensibility discipline operating correctly.

---

## Related investigations this session (separate verdicts; recorded here for the closeout)

1. **§10 numbering integrity — NO DEFECT.** The author's "no §10.1–10.5, then jumps to 10.5.1"
   read is refuted: §10 is a flat list of numbered theorems (10.1a, 10.1b, Empirical Obs 10.2,
   10.3, 10.4, 10.5) with no §10.x sub-headings; "Corollary 10.5.1" (L3810) is a correctly-numbered
   corollary OF Theorem 10.5. All 12 cross-references resolve. The perceptual trap is the flat §10
   sitting above the sub-sectioned §11. Optional cosmetic only: promote theorem labels `<p>`→`<h3>`
   (presentation-only; no identifier change → no cross-ref ripple). One terse spot: L3418 writes
   "Theorems 10.1" for 10.1a+10.1b (correct, slightly terse).
2. **§15.1.8 (CIT two sub-forms vs single-form) — HOLDS BUT UNDER-EXPLAINED.** The CAI/CCI split is
   sound and motivated: CAI inverts the commons' *existence* (separates private-property
   externalities → Pigou); CCI inverts its *exhaustibility* (separates coordination commons →
   Ostrom). Genuine divergence cell CAI-pass/CCI-fail = coordination commons (§6.4.1 TikTok-Level-A
   worked instance). A single-form silently conflates "the relevant condition" and loses the
   three-way routing. BUT §15.1.8 argues it poorly: buries the orthogonality, leans on an
   unexplained "commons-as-structural-identity framing" phrase, and the §6.7 case table labels ONE
   sub-form per case (superficially contradicting "must pass both"). Recommended: a 3-edit
   prose-clarity pass (state the orthogonality; lead with the divergence cell; one-line reconcile
   with the §6.7 table) — NOT collapse to single-form.
3. **McDowell "33–122×" IPG — RETIRE recommended.** See the dedicated decision record (in flight).
   Bare "33–122×" at §9.5 L3147, §11.1 L3888, §11.6 L4500, §14.3 L6536, §16 table. The "33" floor
   reproduces from no consistent input (it is §3.2's definitional 1/3% = 33.3, inherited as
   "case-file canonical"); "122" = full RCV stack ÷ 1960-nominal price (~113–122×). Four mutually
   incompatible origin stories (discount-rate §14.3/§16; lens/price-basis §11.11; cost-category+SCC
   Ch8; M1-alone Ch6). Nothing load-bearing depends on it (CS>0 / IPG>1 hold under every lens).
   Replacement = the §11.11 lens-explicit framing (M3 8.5–26× price-independent; carbon lens
   price-basis-flagged; RCV-integral 67–134×).

---

## Note for the quality-gate owner (checker-gap closure)

To make `check-corpus-invariants.sh` catch this class going forward, add MEDIUM/HIGH patterns for:
`alternative-tested`, `dinner-table`, `multi-audience-register`, `\bM[0-9]+ (dinner-table|case)\b`,
`Option [A-Z]'`, `case file`, `per the case file`, `pre-CIT|AIT\b`, `academic-credibility positioning`,
`contested-surface`, `debate-narrowing`, `jacket-marketing`, `adoption case for`, `Candidate #[0-9]`,
`absent from the prior`, `reader-side translation`, `should report|should be made explicit`,
`§[A-Z]\b` (stale lettered-section refs), `Ch [0-9]+ line [0-9]+` (manuscript line cross-refs).
Exclude the math "Path A/Path B" theorem construct (§10) and substantive "cluster"/"scaffolding" uses.
