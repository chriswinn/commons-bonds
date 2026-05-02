# Pre-submission readiness audit — 7 drafted chapters (2026-05-01)

**Scope:** Ch 2, Ch 4, Ch 5, Ch 7, Ch 8, Ch 9, Ch 10 (all currently-drafted publisher-facing chapter Drafts; excludes Ch 1 because <500 publisher-facing words awaiting drafting; Ch 3 undrafted; Ch 6 HTML deferred to Insight #21 dedicated session).

**Method:** vocabulary-regression sweep against canonical retirement archive (`archive/retirements/index.md`) + register check (Pattern 2 per Insight #9 ratification) + WP#10 scrub-residual check + cross-chapter consistency notes + polish observations.

**Conducted by:** Claude (synchronous in-session audit; not parallel-thread spinup).

---

## Net result

**5 vocabulary-regression auto-fixes applied** across 3 chapters (Ch 5 ×2, Ch 8 ×2, Ch 10 ×1). All others surveyed clean.

**2 over-aggressive fixes initially applied + then REVERTED** after author flagged the question of "is this normal-English usage vs framework-specific retired vocabulary?" Both reverted to original.

**3 items flagged for author judgment** (no auto-fix; surfaced for Chris's call).

**Pattern 2 register check:** PASS across all 7 chapters (already verified during #37 separation pass; this audit confirms still holds).

**WP#10 scrub-residual check:** PASS across all 7 chapters (#37 already scrubbed; this audit confirms no residuals re-emerged).

**Cross-chapter references:** verified across all 7 chapters; no broken references or stale cross-references found.

---

## Auto-fixes applied (verbatim text changes)

### Ch 5

| Line | Before | After | Rationale |
|---|---|---|---|
| 175 | "That **value capture** generates costs" | "That **value extraction** generates costs" | Summarizing the framework's mechanism in lowercase Pattern 2 prose; internal consistency with framework's preferred term per Insight #28 retirement (Value Capture → Value Extraction). |
| 183 | "structures that reward **value capture**" | "structures that reward **value extraction**" | Same as above — naming the framework's structural mechanism; framework's preferred lowercase term applies. |

### Ch 8

| Line | Before | After | Rationale |
|---|---|---|---|
| 99 | "The **dynastic cost** is real" | "The **lineage labor cost** is real" | Section header at line 91 already updated to "Lineage Labor Cost" (current framework term per Insight #56); line 99 was internal-inconsistency back-reference to same cost-component using OLD name. Fix restores internal consistency. |
| 181 | "**dynastic cost** (what cannot be inherited because the parents could not accumulate)" | "**lineage labor cost** (...)" | Used as framework cost-component label in a list of framework cost-components ("foreclosure-of-mobility cost", "[X] cost", "political capture cost"); framework's current term applies. |

### Ch 10

| Line | Before | After | Rationale |
|---|---|---|---|
| 125 | "the foreclosure cost and the externality tail and the community cost and the political capture cost and the **dynastic labor cost** and the acceleration cost" | "... and the **lineage labor cost** and the acceleration cost" | Explicit list of framework cost-components; "Dynastic Labor Cost" was renamed to "Lineage Labor Cost" per Insight #56 ratified 2026-04-30. |

---

## Reverted (initially auto-fixed, then reverted on author flag)

### Ch 5 line 71 — REVERTED

- Original: "Against roughly five to six billion dollars in annual **value capture**, the severed costs accumulate at a rate that dwarfs what the industry has ever paid or provisioned to pay."
- Initial auto-fix: "annual value extraction"
- Reverted to: "annual value capture"
- Reasoning: "value capture" is normal business-English (standard supply-chain / value-chain-analysis literature usage). The framework's retirement of "Value Capture" → "Value Extraction" was about the framework's PROPER-NOUN preferred term, not a ban on the phrase in all contexts. The original passage was describing what an industry does in business-strategy register, not summarizing the framework's structural mechanism. Auto-fix was over-aggressive.

### Ch 8 line 191 — REVERTED

- Original: "the surplus that would otherwise have funded mobility, accumulation, and **dynastic transfer**"
- Initial auto-fix: "lineage transfer"
- Reverted to: "dynastic transfer"
- Reasoning: "dynastic transfer" is a recognized wealth-economics / inheritance-economics term referring to multi-generational wealth transmission. Not specifically the framework's cost-component. The framework's "Dynastic Labor Cost" → "Lineage Labor Cost" rename was about the framework's specific cost-component name; the adjective "dynastic" has independent English usage in inheritance economics. Auto-fix was over-aggressive.

---

## Flagged for author judgment (no auto-fix)

### 1. Ch 2 line 107 — "dynastic dimension"

> *"This is the **dynastic dimension** of cost severance: not just what was taken from the people who stayed, but what was taken from the generations who would have built what came next, if there had been something to build."*

Framework register or descriptive register? "Dynastic dimension" reads as an adjective-noun phrase that could be:
- (a) Descriptive register — adjective use of "dynastic" referring to multi-generational pattern; consistent with "dynastic transfer" wealth-economics usage. Keep as-is.
- (b) Framework-adjacent register — referring to the same dimension the framework now calls "lineage." Update to "lineage dimension" for consistency with the framework's class-connotation cleanup rationale.

Recommendation: author's call. Both defensible; (b) is more internally-consistent with the framework's vocabulary, (a) reads more conventional.

### 2. Ch 10 line 125 — "the community cost" and "the acceleration cost"

> *"... the foreclosure cost and the externality tail and the community cost and the political capture cost and the lineage labor cost and the acceleration cost ..."*

Two cost-component names in the list don't appear in the current Cᵢ illustrative list per `core/terms/terms_index.md` §3:
- **"the community cost"** — framework has "Community Disruption Cost" and "Community Transition Reserve" but not "Community Cost." Possibly author's shorthand for one of those, or a third term not yet canonicalized.
- **"the acceleration cost"** — not in the current Cᵢ illustrative list. Could be a cost-component Chris uses in chapter prose that hasn't been canonicalized in terms_index, or a deprecation-candidate.

Recommendation: author's call. Either (a) update the Cᵢ illustrative list in terms_index to include these names, OR (b) update Ch 10 line 125 to use the canonical Cᵢ names (Community Disruption Cost; an acceleration-cost equivalent or removal).

### 3. Ch 1 GuidanceDoc line 142 — "Knowledge and Culture Cost" (out of audit scope; flagging for hygiene)

> *"...that is **Knowledge and Culture Cost** at the individual scale."*

This is in INTERNAL SCAFFOLDING (GuidanceDoc), not publisher-facing prose, so technically out of this audit's scope. But the current canonical term is **"Knowledge and Cultural Cost"** (per Insight #34 ratified 2026-04-29; "Culture" → "Cultural" rename). Worth a single-keystroke fix during a future GuidanceDoc cleanup pass.

---

## Per-chapter audit results

### Ch 2 — The Miner

- **Vocabulary regression sweep:** 1 flag for author judgment (line 107 "dynastic dimension"; descriptive vs framework-register call).
- **Register (Pattern 2):** PASS. Pure Register 1 throughout; no codified-methodology language.
- **WP#10 scrub residuals:** PASS (clean post-#37 scrub).
- **Cross-chapter references:** Lines 123 (→ Ch 8), 145 (→ Harvey + Mazzucato), 157 (→ Ch 7) — all current and accurate.
- **Polish observations:** none flagged.

### Ch 4 — The Existence Proof

- **Vocabulary regression sweep:** clean.
- **Register (Pattern 2):** PASS.
- **WP#10 scrub residuals:** PASS.
- **Cross-chapter references:** none beyond chapter title.
- **Polish observations:** none flagged.

### Ch 5 — The Accountability Gap (originally FLAGGED for pre-submission review)

- **Vocabulary regression sweep:** 2 fixes applied (lines 175, 183 — framework-mechanism summarizations; "value capture" → "value extraction" for internal consistency with framework's preferred term). 1 fix reverted (line 71 — "annual value capture" stands as normal business-English usage).
- **Register (Pattern 2):** PASS. Chapter is heavily case-driven with cross-domain examples; framework vocabulary lands in lowercase prose register consistent with Pattern 2 discipline.
- **WP#10 scrub residuals:** PASS (#37 separation pass already scrubbed the [Target length] tail block).
- **Cross-chapter references:** Lines 95 (→ Ch 9 Dodd-Frank reference), 127 (→ Ch 4 Norway), 167 (→ Ch 9 cross-national), 189 (→ Ch 6 + Ch 9 + Ch 10), 207 (→ Ch 9), 209 (→ Ch 6 + Ch 7 + Ch 8 + Ch 9 + Ch 10) — extensive cross-references, all current and accurate.
- **Polish observations:** the chapter does substantial work as the structural-pattern synthesis chapter; the cross-references are heavy but appropriate to the synthesis function. Length is ~9,460 publisher-facing words (over original 5K-6K target; not a defect — see project rewrite-plan + author convo 2026-05-01 about chapter-length-imbalance being non-issue at this stage).
- **Net pre-submission-FLAG status:** can be considered SUBSTANTIALLY ADDRESSED post-this-audit. Remaining items: cross-chapter coordination after Ch 4 + Ch 9 lock to final state; polish pass when manuscript-overall is closer to submission-ready. The vocabulary-regression component of the FLAG is closed.

### Ch 7 — On Other Worlds

- **Vocabulary regression sweep:** clean (lines 139, 207 use "universality test" in lowercase; this is the post-demotion form — Universality Test was demoted to descriptive prose use 2026-04-24; lowercase usage is the canonical post-demotion form, not a regression).
- **Register (Pattern 2):** PASS.
- **WP#10 scrub residuals:** PASS.
- **Cross-chapter references:** Lines 21 (→ Ch 5), 107 (→ Ch 5), 109 (→ Ch 5 + later chapters), 133 (→ Ch 9), 197-199 (→ Ch 5 + Ch 9) — all current and accurate.
- **Polish observations:** none flagged.

### Ch 8 — What Things Actually Cost

- **Vocabulary regression sweep:** 2 fixes applied (lines 99, 181 — framework cost-component names "dynastic" → "lineage"). 1 fix reverted (line 191 — "dynastic transfer" stands as wealth-economics English).
- **Register (Pattern 2):** PASS.
- **WP#10 scrub residuals:** PASS.
- **Cross-chapter references:** Lines 19 (→ Ch 2), 33 (→ Ch 6), 77 (→ Ch 2 + Ch 6), 177 (→ Ch 5), 195 (→ Ch 9), 237 (→ Ch 1-7 + Ch 9 + Ch 10) — all current and accurate.
- **Polish observations:** Ch 8 line 105 confirms "Knowledge and Cultural Cost" header uses CURRENT canonical term (per Insight #34 rename). Good.

### Ch 9 — Pricing Honestly

- **Vocabulary regression sweep:** clean.
- **Register (Pattern 2):** PASS.
- **WP#10 scrub residuals:** PASS (#37 separation pass already scrubbed the closing meta-notes block).
- **Cross-chapter references:** Lines 7 (→ Ch 8), 107 (→ Ch 8), 181 (→ Ch 4), 195 (→ Ch 4), 213 (→ Ch 7), 217 (→ Ch 2) — all current and accurate.
- **Polish observations:** none flagged.

### Ch 10 — Common Bonds

- **Vocabulary regression sweep:** 1 fix applied (line 125 — "dynastic labor cost" → "lineage labor cost"; framework cost-component name in explicit list of framework cost-components). 2 cost-component names flagged for author judgment ("the community cost" and "the acceleration cost" not in current Cᵢ illustrative list).
- **Register (Pattern 2):** PASS.
- **WP#10 scrub residuals:** PASS (#37 separation pass already scrubbed the closing author-meta-notes block).
- **Cross-chapter references:** Line 35 (→ Ch 7), Line 37 (→ Ch 7) — all current and accurate.
- **Polish observations:** none flagged.

---

## Cross-chapter consistency observations (no action required)

- Norway material is consistent across Ch 4 (primary case) and Ch 9 (entering-wedges reference).
- McDowell County material is consistent across Ch 2 (primary case), Ch 8 (worked example), Ch 9 (referenced).
- The Mian + Sufi *House of Debt* citation appears in Ch 5 (line 119) and Ch 8 (line 195); both treatments consistent.
- Dodd-Frank discussion in Ch 5 (line 95) cross-references Ch 9 entering-wedges; consistent.
- The Asymmetric Regret Rule (ARR) appears in Ch 10 line 57; uses CURRENT canonical term post-ARP→ARR rename.

---

## Cross-references

- Canonical retirement archive: [archive/retirements/index.md](../../archive/retirements/index.md)
- Current canonical vocabulary: [core/terms/terms_index.md](../../core/terms/terms_index.md)
- Pattern 2 register discipline: Insight #9 (ratified 2026-04-30); WP#10 (ratified 2026-04-30)
- WP#8 publisher-facing scrub: [alignment/commons_bonds_working_principles_v1.0.0.md](../../alignment/commons_bonds_working_principles_v1.0.0.md)
- #37 separation pass that established baseline: commit `3db040a`
- Vocabulary retirement events covered:
  - Insight #28 (Value Capture → Value Extraction); 2026-04-24
  - Insight #56 (Dynastic Labor Cost → Lineage Labor Cost); 2026-04-30
  - Insight #34 (Knowledge and Culture Cost → Knowledge and Cultural Cost); 2026-04-29
  - Insight #21 + #63 (8-tier scheme → Cᵢ via Four Gates); 2026-04-24

## Recommendations for author

1. **Decide on Ch 2 line 107 "dynastic dimension"** — keep descriptive register OR update to "lineage dimension" for framework consistency.
2. **Decide on Ch 10 line 125 "the community cost" and "the acceleration cost"** — either canonicalize these names in terms_index Cᵢ illustrative list, OR update Ch 10 to use canonical Cᵢ names.
3. **Optional: Ch 1 GuidanceDoc line 142** — update "Knowledge and Culture Cost" → "Knowledge and Cultural Cost" during future GuidanceDoc hygiene pass (out of this audit's scope).
4. **Cross-chapter consistency:** no action required from this audit; reference network is healthy.
5. **Length calibration:** per author conversation 2026-05-01, individual-chapter-imbalance is non-issue at current stage; Ch 5 over-length is acceptable; total book length is the relevant metric and is currently short for academic-trade hybrid venue (~55-60K publisher-facing post-#37); fill Ch 1 + Ch 3 to bring total into 70K+ range.

## Audit verdict

Net pre-submission-readiness state of the 7 audited chapters is **GOOD**. Vocabulary regressions resolved (5 mechanical fixes applied); Pattern 2 register holds; WP#10 scrub holds; cross-chapter references current. The pre-submission-readiness FLAG on Ch 5 from v1.48.0 §3 can be considered SUBSTANTIALLY ADDRESSED post-this-audit (remaining items are downstream coordination + final polish at submission time, not present-day corrections).
