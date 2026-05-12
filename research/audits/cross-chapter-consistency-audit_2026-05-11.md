# Cross-Chapter Consistency — Drift-Findings Audit — 2026-05-11

**Status:** ✅ **COMPLETE — all 10 findings ratified 2026-05-11; all 5 batches landed on `main`.** Companion to the canonical-terms inventory at `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`. Parent handoff: `tools/workstream-handoffs/cross-chapter-consistency-handoff_2026-05-10.md`.

**Final state:**
- Batch 1 (high-severity stale cross-references: X-1, X-2, X-3) — commit `b645806`
- Batch 2 (numerical drift: N-1, N-2) — commit `9695b67`
- Batch 3 (formatting: X-4, F-1) — commit `93dd2c4`
- Batch 4 (Glossary terminology + citation: T-1, T-2, C-2) — commit `c3b0cc9`
- Batch 5 (citation verification: C-1) — VERIFIED CLEAN; no edit needed (both Pistor in Ch 5 line 200 and Christophers in Ch 9 line 149 are substantively engaged at depth, >200 words each)
- Inventory + audit artifact commit (Phases 1+2) — commit `46b175b`

**Methodology applied:** Per-pair grep scans across canonical framework terms, retired terms, named cases, recurring statistics, cross-reference patterns, citation patterns, italicization patterns, voice. Surfaced findings clustered by audit dimension; per finding: current state, proposed canonical choice, severity, scope of edit needed.

**Operates downstream of:** apparatus register decisions (#9, ratified 2026-05-11) + Path B audit canonical-home assignments (#8, ratified 2026-05-11). This audit does NOT re-litigate either.

---

## Headline finding

**The manuscript is in unusually strong consistency shape going into this audit.** Two of eight audit dimensions returned ZERO drift:

- **Retired-term scan:** 0 hits across all 18 retired terms × 10 chapter drafts. The apparatus register sweep + Glossary v4 retirement work has held.
- **Apparatus encoding scan:** 0 stale `tₔ` subscripts; 0 stale `⟯` operators (these were the encoding issues caught + fixed during the 2026-05-11 apparatus sweep).

Three of eight dimensions returned **mild** drift (formatting, citation date, single-instance capitalization). Two dimensions returned **moderate** drift (one Norway SWF figure inconsistency; one Ch 5 BLTF-debt rounding looseness). **One dimension returned high-severity drift: three stale cross-references** in Ch 6 + Ch 8 pointing at Ch 2 content that does not exist in Ch 2.

The high-severity finding is the only one that materially affects reader trust. Everything else is polish-tier.

---

## Severity legend

- 🔴 **High** — pointer-to-nowhere or self-contradictory numeric claim; reader would notice + lose trust.
- 🟡 **Medium** — different presentations of the same fact across chapters; readable but invites copyeditor flag.
- 🟢 **Low** — single-instance formatting drift; trade-press copyedit would catch.
- ⚪ **No-op** — flagged for completeness but not actually drift (intentional voice / scope difference).

---

## DIMENSION 1 — Cross-reference integrity (HIGH-SEVERITY FINDINGS)

### 🔴 X-1: Ch 6 line 748 attributes Deepwater $65–70B to "Chapter 2's enumeration" — but Ch 2 has zero Deepwater content

**Current state (Ch 6 line 748):**
> "Deepwater Horizon. Under pure Pigouvian accounting, the per-barrel external cost is the documented cleanup plus restoration plus lost-ecosystem services — the $65 to $70 billion of Chapter 2's enumeration."

**Problem:** Ch 2 has no Deepwater content (zero hits on grep). Deepwater is Ch 5's canonical case (line 36–52). The cited $65 billion figure appears at [Ch 5 line 44](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:44): "*The total documented cost to BP approached sixty-five billion dollars*". The "$70 billion" upper bound does not appear anywhere in the chapter drafts — it may be a slight number-widening drift.

**Proposed fix:**
- Change "Chapter 2's enumeration" → "Chapter 5's enumeration".
- Change "$65 to $70 billion" → "$65 billion" (matching Ch 5 line 44 canonical phrasing), OR keep the range as a Ch 6 convergence-table summary form and confirm with author whether $70B has a documented source.

**Scope:** 1 sentence edit at Ch 6 line 748.

---

### 🔴 X-2: Ch 6 line 745 attributes "$5 to $15 per ton" community-cost to "Chapter 2 enumerated" — but Ch 2 does not enumerate $5–15 per ton

**Current state (Ch 6 line 745):**
> "McDowell County coal. Under standard Pigouvian accounting... lands around $550 per ton of coal. RCV adds the foreclosure term... and lets the Commons Inversion Test probe the community-disruption costs — the $5 to $15 per ton Chapter 2 enumerated — that Pigouvian accounting treats as separate policy questions..."

**Problem:** Ch 2 lines 89, 121 describe community cost categories qualitatively (schools, roads, hospitals, tax base, transition cost) but do not enumerate a $5–$15 per-ton figure. The $5–$15 per-ton figure appears in [Ch 6 itself, line 154](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html:154) ("*A conservative community-cost estimate comes in between $5 and $15 per ton*"). The Ch 6 line 745 sentence attributes Ch 6's own number to Ch 2.

**Proposed fix:**
- Change "Chapter 2 enumerated" → "this chapter's Approach 1 enumerated" or "this chapter's bottom-up walkthrough enumerated".
- Alternatively: change to "the community-disruption costs Chapter 2 named qualitatively and this chapter's bottom-up walkthrough priced at $5–$15 per ton".

**Scope:** 1 sentence edit at Ch 6 line 745.

---

### 🔴 X-3: Ch 8 line 71 references "the $100 barrel passage" in Ch 2 — but Ch 2 has no $100 barrel passage

**Current state (Ch 8 line 71):**
> "This is the cost component Chapter 2 named through the $100 barrel passage and Chapter 6 formalized through the residual commons value integral."

**Problem:** Ch 2 contains no "$100 barrel" passage (zero grep hits across `100 barrel`, `hundred dollar barrel`, `$100`, `oil`, `barrel of oil`). Ch 2 is a coal-only case; barrels-of-oil reasoning lives in Ch 5 (Deepwater) and Ch 8 itself. This appears to be a stale reference — possibly to a passage that was earlier in Ch 2 and removed during the Path B BLTF compression, OR a misremembered cross-reference.

**Proposed fix (requires author judgment):**
- Option A: Remove the "$100 barrel passage" phrase entirely, leaving "*the cost component this chapter has been pricing and Chapter 6 formalized through the residual commons value integral*".
- Option B: Replace with a different valid Ch 2 reference — e.g., "*the cost component Chapter 2 named through its actuarial-cost-dwarfs-what-the-coal-sold-for passage (line 121)*".
- Option C: Replace "Chapter 2" with "Chapter 5" if the intended reference is Macondo's per-barrel arithmetic — but Ch 5 doesn't use "$100/barrel" specifically either; Ch 5 cites Macondo barrels at 2010 prices ($3–4 billion for 40–60M barrels ≈ $66/barrel).

**Recommended:** Option A is the safest fix. Authoring intent unclear without author input.

**Scope:** 1 sentence edit at Ch 8 line 71.

---

### 🟢 X-4: Ch 5 line 92 lowercase "chapter 9" against 51 capitalized instances

**Current state:** [Ch 5 line 92](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:92): "*chapter 9 will name it as one of the entering wedges*".

**Standard:** Title-case "Chapter N" — 51 instances across the manuscript use Title-case.

**Proposed fix:** Change "chapter 9" → "Chapter 9".

**Scope:** 1 word capitalization edit.

---

### ⚪ X-5: All other "Chapter N" cross-references — verified valid

Spot-checked the following:
- Ch 2 line 123 → Ch 8 (per-ton walkthrough) ✓
- Ch 2 line 157 → Ch 7 (arrangements that hide cost) ✓
- Ch 5 line 96 → Ch 9 (Sweden comparison at depth) ✓ (Path B audit confirmed)
- Ch 5 line 124 → Ch 4 (Norway/SS contrast) ✓
- Ch 5 line 186 → Ch 6, Ch 9 (methodology + policy economy) ✓
- Ch 6 line 148 → Ch 2 (BLTF fund mechanics) ✓
- Ch 6 line 588 → Tech Appendix (out of audit scope per handoff)
- Ch 7 line 215 → Ch 5 (conditions named) ✓
- Ch 8 line 35 → Ch 2 (BLTF walkthrough) ✓
- Ch 8 line 173 → Ch 5 (case after case) ✓ (Path B "architecture-by-design")
- Ch 8 line 191 → Ch 9 (alternative architecture) ✓
- Ch 9 line 147 → Ch 5 (Pistor engagement at depth) — see C-1 below
- Ch 9 line 183 → Ch 4 (retirement-security comparison) ✓
- Ch 9 line 215 → Ch 7 (Europa-ocean treatment) ✓
- Ch 9 line 219 → Ch 2 (reclamation bond gap documentation) ✓
- Ch 10 line 29, 31 → Ch 7 (Mars + cost-severance arrangements) ✓

---

## DIMENSION 2 — Numerical / statistical consistency

### 🟡 N-1: Norway SWF AUM stated differently in Ch 4 vs Ch 6

**Current state:**
- [Ch 4 line 23](manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md:23): "*The fund now holds more than one and nine-tenths trillion dollars in assets.*" (≈ $1.9T)
- [Ch 6 line 537](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html:537): "*The Norwegian sovereign wealth fund — formally, the Government Pension Fund Global — holds roughly $1.8 trillion against the country's cumulative oil revenues*"

**Problem:** $1.9T vs $1.8T. Both are plausible point estimates for different time-points (the fund has been moving through that range over 2024–2026). Reader sees inconsistency.

**Proposed fix (requires author judgment):**
- Option A — Single canonical figure: Pick one number and standardize. Recommend Ch 4 line 23's "more than $1.9 trillion" (Ch 4 is canonical home; prose-form aligns with chapter voice). Update Ch 6 line 537 to match.
- Option B — Update both to current 2026 figure: If author wants to refresh to current state (Norwegian Government Pension Fund Global was approaching $2 trillion in early 2026 per author memory), update both to a refreshed canonical value.
- Option C — Keep distinct figures if author intent is "Ch 4 narrates 2025 state; Ch 6 cites 2024 published figure": no fix, document the scope difference in inventory.

**Recommended:** Option A — Ch 4 is canonical home. Make Ch 6 conform.

**Scope:** 1 sentence edit at Ch 6 line 537 (if Option A); 2 edits if Option B.

---

### 🟡 N-2: BLTF debt — Ch 5 rounds "4.6 billion" down to "over four billion"

**Current state:**
- [Ch 2 line 67](manuscript/chapters/Chapter__2_TheMiner__Draft.md:67) (canonical site per Path B Fix 2): "*the fund is $4.6 billion in debt*"
- [Ch 5 line 206](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:206): "*currently over four billion dollars in debt*"

**Problem:** Ch 5's "over four billion" is technically true (4.6 is over 4) but rounds away the specificity Ch 2 establishes as canonical. Mild inconsistency.

**Proposed fix:** Change Ch 5 line 206 "over four billion dollars in debt" → "currently $4.6 billion in debt" OR "approaching five billion dollars in debt" (the latter aligns with Ch 2's "by 2050 reaches $15 billion" trajectory and Ch 5's apparatus-introduction voice).

**Recommended:** Match Ch 2 exactly — "$4.6 billion in debt" — but acknowledge author may prefer Ch 5's prose-form rounding for voice reasons. Author judgment.

**Scope:** 1 phrase edit at Ch 5 line 206.

---

### ⚪ N-3: Libby IPG figures (40–80× per-case vs 55–82× convergence table)

**Current state:**
- Ch 6 line 170: "55 to 82 times" (convergence-table form)
- Ch 6 line 486: explicitly reconciles — "*Libby's table figures are 55–82× and 40–80×, and reduce in the per-case work to a simpler 40× cost-to-revenue ratio*"
- Ch 8 line 173: "between forty and eighty" (per-case-walk form)

**Verdict:** Not drift. Ch 6 line 486 explicitly reconciles the two ranges and explains why both are valid. The framework's "Three Ways of Counting" discipline is on display.

**No fix.**

---

### ⚪ N-4: McDowell IPG range (33–122×, floor 33) — consistent

Verified consistent across Ch 2 line 123, Ch 6 line 486, Ch 6 line 625. **No fix.**

---

### ⚪ N-5: BLTF $44B + $15B by 2050 + per-ton ~$0.80 — consistent across chapters

Verified consistent across Ch 2, Ch 5, Ch 6, Ch 8 per Path B Fix 2's canonicalization. **No fix.**

---

### ⚪ N-6: 2008 figures ($11T household wealth + 10M foreclosures + $700B TARP) — consistent across Ch 5/Ch 8/Ch 9

Verified consistent. Ch 5's additional "$16 trillion Fed peak" figure is Ch 5-scope and does not appear elsewhere. **No fix.**

---

## DIMENSION 3 — Terminology / framework-definition drift

### 🟡 T-1: "Value Extraction" — Glossary capitalizes; chapters use lowercase

**Current state:**
- Glossary v4 entry: "Value Extraction" (Title-case framework term)
- Glossary definition body: "*value extraction is the causal event*" (lowercase within the entry's own definition)
- [Ch 2 line 137](manuscript/chapters/Chapter__2_TheMiner__Draft.md:137): "*The paired mechanism is **value extraction***" (lowercase bold)
- [Ch 10 line 85](manuscript/chapters/Chapter_10_CommonBonds__Draft.md:85): "*value extraction and cost bearing are separated*" (lowercase prose)

**Question:** Is "value extraction" a Title-case framework term (paralleling "Cost Severance") or a lowercase prose phrase (paralleling "intergenerational cost severance")?

**Author judgment required.** Options:
- Option A — Treat as Title-case framework term, capitalize at first introduction (Ch 2 line 137 → `**Value Extraction**`), keep lowercase prose use elsewhere as voice-driven. Update Glossary to reflect "Value Extraction is a Title-case framework term; chapter prose deploys lowercase form per author voice."
- Option B — Treat as lowercase prose phrase throughout, retire the Glossary capitalization. Add Glossary note: "(lowercase prose phrase)" matching the discipline applied to "intergenerational cost severance" and "spatial cost severance".

**Recommended:** Option B (lowercase prose throughout). Consistent with the Mazzucato-discipline / "name the mechanism in plain language" intent. Matches existing chapter behavior. Glossary already inconsistent with itself (entry header capitalized, body lowercase).

**Scope:** Glossary edit only if Option B; potentially 1 chapter edit if Option A.

---

### 🟡 T-2: "Severed Cost" — Glossary capitalizes; chapters use lowercase

**Same pattern as T-1.** Glossary entry header is "Severed Cost"; chapter introductions use `**severed cost**` lowercase bold; Glossary's own definition body says the term is "*the framework's adoption target — the phrase the book hopes a labor lawyer or judge will use in court without needing it explained*".

**Recommended:** Option B (lowercase prose throughout). Adoption-target intent is itself a lowercase-prose intent. Glossary should note "(lowercase prose phrase)" like intergenerational/spatial cost severance.

**Scope:** Glossary edit only.

---

### ⚪ T-3: Cost Severance / cost-severance hyphenation

**Verdict:** Consistent with English hyphenation conventions (unhyphenated noun-phrase, hyphenated compound-adjective). Author voice handles this naturally; no rule needed beyond what English conventions provide.

**No fix.**

---

### ⚪ T-4: Spatial / intergenerational / existential lowercase prose phrases

**Verdict:** All three are correctly lowercase throughout. Consistent with Glossary discipline.

**No fix.**

---

## DIMENSION 4 — Case-description consistency

### ⚪ C-1: McDowell, Norway, Chesapeake, Libby, Mondragon, Vienna, Macondo, Sweden — verified consistent

Per canonical-home table in inventory Section 2. Each case's primary description lives in one canonical chapter (Ch 2 McDowell; Ch 3 Chesapeake; Ch 4 Norway; Ch 5 Libby + Macondo + Social Security + 2008; Ch 9 Mondragon + Vienna + Sweden Saltsjöbaden). Cross-chapter references compress to summary/cross-reference form.

Path B audit (#8) already canonicalized the architecturally-clean preview-then-full patterns (Ch 2 → Ch 3 Chesapeake; Ch 5 → Ch 9 Sweden) and resolved the contaminations (Ch 5 ↔ Ch 6 Restitution Lineage; Ch 2 ↔ Ch 6 ↔ Ch 8 BLTF).

**No additional case-description drift surfaced by this audit.**

---

## DIMENSION 5 — Citation consistency

### 🟡 C-1: Pistor engagement-depth claim — verify Ch 5 actually engages Pistor "at depth"

**Current state:**
- [Ch 9 line 147](manuscript/chapters/Chapter__9_PricingHonestly__Draft.md:147): "*Pistor's The Code of Capital (engaged at depth in Chapter 5) names the legal-architectural reason*"
- [Ch 5 line 182](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:182): "*Brett Christophers' The Price is Wrong (2024), engaged at depth in Chapter 9*"

**Cross-claim pattern:** Each chapter claims the other engages a source "at depth". Verify both engagements are actually at-depth.

**Status:** Not yet verified by reading Ch 5's full Pistor treatment + Ch 9's full Christophers treatment. **Spot-verification needed** before this audit can confirm or flag. Likely OK per user memory ("*Ch 5 + Ch 9 Pistor/Christophers/Susskind engagement landed*" — commit d78872e, per the handoff doc).

**Proposed action:** Verify both engagement depths in a 5-minute read of Ch 5 + Ch 9 Pistor/Christophers passages. If both are at-depth (>1 paragraph of substantive engagement each), no fix. If either is a passing mention, soften the "engaged at depth in" phrasing in the other chapter.

**Scope:** 0 edits if verified clean; 1 phrase edit per chapter if not.

---

### 🟢 C-2: Stern Review date — "2006" vs "2007"

**Current state:**
- [Ch 7 line 71](manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md:71): "*The 2006 Stern Review argued for a near-zero pure rate of time preference*"
- Glossary v4 entry (Externality Tail): "*Stern Review 2007*"

**Problem:** The Stern Review was published in October 2006 and formally released as the Cabinet Office document in 2007. Both dates are defensible.

**Proposed fix:** Standardize to one. Recommend "2006 Stern Review" (date of publication / common shorthand). Update Glossary to match.

**Scope:** Glossary edit only.

---

### ⚪ C-3: Coates, Darity & Mullen, Pistor, Parfit, Hartwick, Hotelling, Mazzucato, Harvey, Mian & Sufi, Christophers — citation forms consistent

Spot-checked all major recurring sources. Citation forms (italic titles, author names, years) consistent across chapters. **No fix.**

---

## DIMENSION 6 — Italicization / formatting consistency

### 🟢 F-1: Chapter-end marker drift — Ch 10 missing em-dash format

**Current state:**
- Ch 2, 3, 4, 5, 7, 9: "— End of Chapter N —" (em-dash flanked)
- [Ch 10 line 149](manuscript/chapters/Chapter_10_CommonBonds__Draft.md:149): "End of Chapter 10" (no em-dashes)
- Ch 1, 6, 8: not yet verified — spot-check needed

**Proposed fix:** Standardize Ch 10 to "— End of Chapter 10 —" matching other chapters. Spot-verify Ch 1, Ch 6, Ch 8 endings.

**Scope:** 1 line edit at Ch 10 line 149; spot-verify 3 other chapters.

---

### 🟢 F-2: Em-dash format across .md vs .html chapters

**Current state:**
- .md chapters: literal `—` (U+2014)
- Ch 6 .html: `&mdash;` HTML entity

**Verdict:** Both render identically. This is HTML-vs-Markdown encoding, not content drift. No fix needed.

**No fix.**

---

### ⚪ F-3: Bold + italic conventions for framework-term introductions

Verified consistent. `**Cost severance**` / `**severed cost**` / `**value extraction**` / `**Restitution Bond**` / `**Foreclosure Bond**` all use bold at first introduction.

**No fix.**

---

## DIMENSION 7 — Author voice / tense consistency

### ⚪ V-1: First-person voice register — voice-discipline holds

Memoir chapters (Ch 1, Ch 3, Ch 10) carry first-person; analytical chapters (Ch 2, 4, 5, 6, 7, 8, 9) are expository. The voice register is consistent with the chapter's argumentative role. No drift surfaced.

**No fix.**

---

### ⚪ V-2: Tense consistency within scenes

Spot-checked Ch 1 (grandfather scenes — past tense throughout); Ch 3 (waterman scenes — mixed past/present per chapter intent); Ch 10 (harbor scenes — present-tense framing with past-tense memory). Tense usage is voice-driven and consistent within scenes.

**No fix.**

---

## Summary punch list (proposed edits, total)

### 🔴 High-severity (3 edits)
- **X-1** Ch 6 line 748 — "Chapter 2's enumeration" → "Chapter 5's enumeration"; verify $65 vs $65–70 range
- **X-2** Ch 6 line 745 — "Chapter 2 enumerated" → "this chapter's bottom-up walkthrough enumerated"
- **X-3** Ch 8 line 71 — remove "$100 barrel passage" reference (Option A); or replace with valid Ch 2 anchor (Option B)

### 🟡 Medium-severity (3 edits)
- **N-1** Ch 6 line 537 — Norway SWF AUM "$1.8 trillion" → match Ch 4 canonical ($1.9 trillion) or refreshed 2026 figure
- **N-2** Ch 5 line 206 — "over four billion" → "$4.6 billion" (or author-preferred prose form)
- **C-1** Verify Ch 5 Pistor engagement + Ch 9 Christophers engagement are both "at depth" (likely no edit; verification pass)

### 🟢 Low-severity (2 edits + glossary)
- **X-4** Ch 5 line 92 — "chapter 9" → "Chapter 9"
- **F-1** Ch 10 line 149 — "End of Chapter 10" → "— End of Chapter 10 —"; spot-verify Ch 1, Ch 6, Ch 8
- **T-1, T-2** Glossary v4 — add "(lowercase prose phrase)" annotation to Value Extraction + Severed Cost entries (if Option B ratified)
- **C-2** Glossary v4 — Stern Review date alignment ("2006" vs "2007")

### Optional (author-judgment)
- **T-1, T-2** chapter prose treatment (Option A vs Option B) — purely conventional choice

---

## Ratification record (closed 2026-05-11)

All 10 findings ratified 2026-05-11. Resolution per item:

1. ✅ **X-1 (Ch 6 line 748):** Ratified — Ch 5 attribution + $65 billion (dropped $70 upper bound). Applied in Batch 1 (commit `b645806`).
2. ✅ **X-2 (Ch 6 line 745):** Ratified — "those Chapter 2 named qualitatively and this chapter's bottom-up walkthrough priced at $5 to $15 per ton". Applied in Batch 1.
3. ✅ **X-3 (Ch 8 line 71):** Ratified — REPLACE phrasing (not remove). Author-ratified specific text: "cost-walkthrough that lands multiple orders of magnitude above the price coal actually sold for". Regression context: 2026-04-27 Ch 8 restructure rigor pass had flagged "$100 barrel passage" as retired vocabulary at this exact line; cleanup did not propagate. Batch 1 completes the 14-days-late propagation. The original oil → coal pivot was deliberate (oil $100/barrel walkthrough survives in the withdrawn Noema essay `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md` Section III — recoverable as derivative-essay material; PM session has stood up workstream #16 to explore venue alignment per commit `d84b54b`).
4. ✅ **X-4 (Ch 5 line 92):** Ratified — capitalize "chapter 9" → "Chapter 9". Applied in Batch 3 (commit `93dd2c4`).
5. ✅ **N-1 (Ch 6 line 537):** Ratified — Option A ($1.9T standardization to Ch 4 canonical). Applied in Batch 2 (commit `9695b67`).
6. ✅ **N-2 (Ch 5 line 210):** Ratified — "four and a half billion dollars in debt" (prose-form preserving Ch 5's voice; restores specificity to match Ch 2's $4.6B canonical). Applied in Batch 2.
7. ✅ **T-1 + T-2 (Value Extraction + Severed Cost):** Ratified — Option B (lowercase prose phrases). Glossary v4 headers downcased + "(lowercase prose phrase)" annotation added, paralleling existing entries for `intergenerational cost severance` and `spatial cost severance`. No chapter prose changes. Applied in Batch 4 (commit `c3b0cc9`).
8. ✅ **C-1 (Pistor/Christophers):** Verified clean — both engagements are substantively at depth (>200 words each). Ch 5 line 200 has full Pistor *The Code of Capital* engagement with legal-modules thesis + Libby case application. Ch 9 line 149 has full Christophers *The Price is Wrong* engagement with profit-not-price thesis + framework's structural-response synthesis. Both mutual "engaged at depth in Chapter X" cross-claims are accurate. NO EDIT NEEDED.
9. ✅ **C-2 (Stern Review date):** Ratified — standardize to 2006. Glossary v4 two instances (lines 169, 206 in lineage notes for Externality Tail + Residual Commons Value entries) updated to "Stern Review 2006". Applied in Batch 4.
10. ✅ **F-1 (Ch 10 ending + spot-check):** Ratified — Ch 10 line 149 "End of Chapter 10" → "— End of Chapter 10 —". Applied in Batch 3. Spot-verify finding: Ch 1, Ch 6, Ch 8 have NO chapter-end marker at all (they end on narrative/argumentative beat) — likely intentional minority pattern; flagged in Batch 3 commit message for author awareness, not modified.

## Flagged for separate workstream

**Ch 2 GuidanceDoc staleness — `$100 barrel passage` references.** [Chapter__2___GuidanceDoc.md:31,122,214](manuscript/chapters/Chapter__2___GuidanceDoc.md:31) still references "$100 barrel passage" as if Ch 2 currently has it. Surfaced during X-3 regression sweep. PM session has picked this up as cross-thread #9 per commit `d84b54b`.

**$100 barrel derivative-essay potential.** PM session has stood up workstream #16 (commit `d84b54b`) to evaluate venue alignment for an oil-framed standalone essay. Source material at `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md` Section III "The $100 Barrel". Current gas-price spike is the news peg.

**Ch 1/6/8 no-chapter-end-marker pattern.** Spot-verify revealed three chapters lack the em-dashed end-marker that six other chapters use. Likely intentional (narrative-beat closing for Ch 1's plane scene; methodology closing for Ch 6; forward-pivot to Ch 9/10 for Ch 8). Author awareness item; not modified.

---

## Phase 4 application record (closed 2026-05-11)

Per the handoff + WP#9: committed per ratified chunk; merged per ratified chunk via `git push origin HEAD:main`. Final batch landings:

- ✅ **Batch 1 (high-severity cross-references):** X-1 + X-2 + X-3 — commit `b645806` on main
- ✅ **Batch 2 (numerical drift):** N-1 + N-2 — commit `9695b67` on main
- ✅ **Batch 3 (formatting):** X-4 + F-1 — commit `93dd2c4` on main
- ✅ **Batch 4 (glossary + citation):** T-1 + T-2 + C-2 — commit `c3b0cc9` on main
- ✅ **Batch 5 (citation verification):** C-1 — VERIFIED CLEAN; no edit needed

Total: 5 chapter-prose edits (Ch 5 ×2, Ch 6 ×3, Ch 8 ×1, Ch 10 ×1 = 7 across 4 chapters) + 4 Glossary edits + 0 verification edits = **9 edits across 5 files**.

Workstream complete. Standing references on main:
- `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` — canonical-terms inventory
- `research/audits/cross-chapter-consistency-audit_2026-05-11.md` — this document

---

*End of audit. Workstream closed 2026-05-11.*
