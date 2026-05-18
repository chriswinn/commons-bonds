---
name: Grammatical-role discipline for chapter → appendix cross-references
description: Cross-references between chapter prose and the Tech Appendix follow a grammatical-role principle rather than a blanket "always include §-number" or "never include §-number" rule. Distinguishes sections-as-nouns from sections-as-citations and treats theorems differently.
type: feedback
originSessionId: appendix-numbering-reconciliation-2026-05-11
---
**Canonical full content:** Apparatus Item 10 + Phase 5 of appendix-numbering-reconciliation workstream (see this file's own footer for commit refs)
**Layer:** scan-friendly summary; this file is the cross-session discipline pointer. Update the canonical artifact when content changes; sync this summary via `tools/memory-updates/` spec for substantive amendments.

# Grammatical-role discipline for chapter → appendix cross-references

**Ratified:** 2026-05-11 (Tech Appendix numbering reconciliation workstream Phase 5; applied to Ch 6 in commit `50ec90b`).

**Rule.** When a chapter references the Tech Appendix, the format depends on the cross-reference's grammatical role in the sentence:

1. **Sections used as noun phrases in body prose** → **named only** (no §-number).
   - Example: *"the Four Gates Admission Apparatus filters cost claims for unit-consistency..."*
   - The named content does both jobs: tells the layman what the concept is, and is findable in the annotated TOC for specialists who flip back.

2. **Sections used as navigation instructions / parentheticals (citations)** → **name + §-number**.
   - Example: *"(§8, Asymmetric Regret Rule)"* or *"see §7 of the Tech Appendix for the formal specification"*.
   - When the cross-reference *is* the act of pointing somewhere, the address belongs in the pointer.

3. **Theorems / Empirical Observations / Corollaries / Definitions** → **always compound identifier (name + number)**.
   - Example: *"Theorem 10.3 (Abundance Masking) formalizes this..."*
   - The number is part of the theorem's canonical identity, not parenthetical decoration. Math/econ writing has worked this way for a century.

4. **For HTML-format chapters** (currently only Ch 6; Ch 6 → markdown conversion is a queued workstream) → **hyperlink named cross-references to appendix anchors**.
   - Example: `<a href="../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-7-four-gates">Four Gates Admission Apparatus section</a>`
   - Zero body-prose cost; nice digital affordance. Print/PDF readers don't see it; digital readers click through.

**Why.** Author asked the fresh-take question during the 2026-05-11 numbering reconciliation session: *"ignore prior ratifications; what's best for the book?"* The reasoning that emerged:

- Adding `(§7)` mid-sentence to every section mention is **apparatus tax** the reader skips. Trade-comp shelf (Mazzucato, Sandel, Raworth, Piketty) all do named-only in body prose; technical addresses live in notes/appendix/citation infrastructure.
- But when the cross-reference IS the act of pointing somewhere (parentheticals, "see X" constructions), the address belongs in the pointer — that's the whole purpose of the pointer.
- Theorems are different from sections: the number is a stable academic-citation convention (math/econ has done "Theorem X.Y" for a century). The name + number compound is natural identifier usage, not apparatus tax.
- The annotated TOC (landed 2026-05-11 commit `8f5c416`) makes named-only-for-sections cheap to navigate; the lookup cost is one TOC scan, not painful.

Cross-comp evidence: this is how Piketty's *Capital in the Twenty-First Century*, Mazzucato's *The Value of Everything*, and academic-econ working papers (AER/QJE/JPE) handle internal cross-references — grammar-driven, not blanket-rule.

**How to apply.**

- When writing or editing chapter prose, check the cross-reference's grammatical role: is the section name the **subject/object** of the sentence (noun → named only) or a **parenthetical pointer / "see X" construction** (citation → name + §)?
- For theorems, lemmas, corollaries, definitions: always pair the number with the name on first use within a passage. Reuse the name alone afterward if context is clear; otherwise re-pair.
- For HTML-format files: add hyperlinks to appendix anchors using relative paths (`../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-N-...`). Verify the anchor exists.
- For markdown files: use markdown link syntax `[text](path#anchor)` if the downstream renderer supports it (Pandoc + HTML/DOCX targets do); otherwise plain text follows the same grammatical-role principle.
- The principle applies book-wide. If a new chapter adds a cross-reference, check the grammatical role and format accordingly. If editing existing chapters and you spot a violation, normalize per this principle.

**Edge cases and tensions:**

- **When the section name and the §-number both feel necessary mid-sentence** (e.g., "the four gates apparatus (§7) extends..."): treat as parenthetical citation — name + §. If the parenthetical feels heavy, reword to noun form ("the Four Gates Admission Apparatus extends...") and trust the reader to navigate.
- **When a theorem is referenced repeatedly within a paragraph**: full compound identifier on first use; name-only or number-only acceptable after. Don't repeat "Theorem 10.3 (Abundance Masking)" four times in one paragraph.
- **When the cross-reference is to a sub-section (e.g., §7.1, §11.5)**: same grammatical-role principle; the §-number's depth doesn't change the discipline.
- **When a cross-reference points to embedded supplement-style numbering** (Scheme 4 from Phase 1 inventory; deferred to separate workstream): treat as ambiguous; rewrite descriptively rather than preserving locally-restarted §-notation in chapter prose.

**Companion principles** (separately ratified, not superseded):
- Apparatus Item 10 (commit `16876a1`) — named-content discipline for chapter cross-references (this grammatical-role principle generalizes Item 10 to cover the citation case + theorem case).
- Dual-audience layman+specialist test (`feedback_dual_audience_test.md`) — every format decision tested against both audiences; this principle passes that test.
- Verify-stale-memory-claims (`feedback_verify_stale_memory_claims.md`) — when applying §-numbers, verify the target section number against the current canonical scheme.

**Implementation status:** Applied to Ch 6 in commit `50ec90b` (Phase 5 of appendix-numbering-reconciliation workstream). Ch 7 line 119 already complies (Theorem 10.3 compound identifier; landed in Phase 4 commit `4b53320`). Other chapters substantively comply via Apparatus Item 10 ratification. If future apparatus passes touch chapter cross-references, apply this principle.
