# Commons Bonds — C5 Content Patch
## Rigor Test Two-Path Structure — Canonical Form
### All Rigor-Testing Materials

**Status:** Canonical structure — adopt universally going forward  
**Produced:** 2026-04-20 · v1.13.0 session  
**Applies to:** All rigor-testing materials, including `commons-bonds-rigor-test.docx` (D3),
`commons-bonds-rigor-testing-roles.html` (B2), and any rigor-test sections in WS files.  
**Rationale:** Prior rigor tests evaluated claims on a single path. The architectural distinction
between *mechanism* (structural allocation) and *shield* (distance) requires a two-path structure.
A claim that passes on one path but fails on the other is not rigorous. All future rigor tests
default to the two-path structure.

---

## The Two Paths — Definitions

### Path 1: Allocation Symmetry

**What it tests:** Whether the mechanism correctly identifies and accounts for the
value-capture/cost-bearing asymmetry.

**The question:** *Who captures value, and who bears cost?*

A claim passes Path 1 if:
- The extractor (value-capture side) is correctly identified
- The cost-bearer (displaced-cost side) is correctly identified
- The asymmetry between them is structurally explained — i.e., it arises from the organization
  of the transaction, not from bad actors or contingent circumstances
- The RCV formula (CS = RCV − B) correctly places the uncaptured cost in the appropriate tier

A claim fails Path 1 if:
- The cost-bearer is misidentified or underspecified
- The asymmetry is attributed to individual moral failure rather than structural arrangement
- The tier assignment is wrong (cost placed in wrong category)
- The claim implies the asymmetry could be corrected by individual behavior change alone

---

### Path 2: Shield Absence

**What it tests:** Whether the mechanism correctly identifies and addresses the shield condition
— the structural arrangement that prevents the allocation asymmetry from being recognized,
measured, or corrected.

**The question:** *What prevents honest accounting?*

A claim passes Path 2 if:
- The shield condition (distance) is named and explained
- Distance is characterized correctly: the gap between where value is captured and where cost
  is borne, operating across space, time, institutional boundary, or epistemic category
- The shield is shown to be structural (not merely accidental, corrupt, or correctable by
  transparency alone)
- The claim explains why the shield persists even when actors know it exists

A claim fails Path 2 if:
- The shield is omitted (claim addresses asymmetry but not the prevention of correction)
- Distance is treated as ignorance rather than structure
- The claim implies the shield can be dissolved by information disclosure alone
- Political Capture (Tier 8) is treated as a separate phenomenon rather than the institutional
  expression of the shield mechanism

---

## Canonical Two-Path Evaluation Form

Use this template for every rigor test evaluation. A claim must pass BOTH paths to be
considered rigorous. Partial passes are noted but do not constitute a pass.

```markdown
## Rigor Test: [Claim or argument being tested]

**Claim:** [State the specific claim in one sentence]

---

### Path 1 — Allocation Symmetry

**Who captures value?**  
[Identify the extractor / value-capture side]

**Who bears cost?**  
[Identify the displaced cost-bearer]

**Is the asymmetry structural?**  
[Yes / No / Partial — explain]

**Correct tier assignment?**  
[Tier # — Name — confirm or correct]

**Path 1 verdict:** PASS / FAIL / PARTIAL  
[One-sentence explanation]

---

### Path 2 — Shield Absence

**What is the shield condition?**  
[Name the distance mechanism preventing recognition or correction]

**Type of distance:**  
[ ] Spatial (geographic separation of extraction site and cost site)  
[ ] Temporal (cost deferred across time; future bears what present captures)  
[ ] Institutional (cost borne by entity outside extractor's accountability boundary)  
[ ] Epistemic (cost is formally unmeasured, unpriced, or categorically excluded)  
[ ] Political (Tier 8 active — accounting rules captured by extractor)  
[ ] Combination: [specify]

**Is the shield structural?**  
[Yes / No / Partial — explain why it persists even with knowledge of it]

**Path 2 verdict:** PASS / FAIL / PARTIAL  
[One-sentence explanation]

---

### Overall Verdict

**PASS** — Both paths clear. Claim is rigorous.  
**CONDITIONAL PASS** — One path partial; note condition for full pass.  
**FAIL** — One or both paths fail. Claim requires revision. See notes below.

**Revision notes:**  
[Specify what must change for the claim to pass both paths]
```

---

## Application Notes

### When to use the full two-path form

Use the full template for:
- Evaluating a new chapter argument or claim before incorporating it
- Stress-testing tier assignments
- Reviewing external critiques of the Commons Bonds model
- Evaluating proposed policy applications of the framework
- Any rigor test that appears in `commons-bonds-rigor-test.docx` (D3)

### When to use abbreviated form

For ongoing WS-level notes (in-line within a workstream file), an abbreviated form is
acceptable:

```markdown
> **Rigor check:** [Claim]. Path 1 (allocation): [extractor] → [cost-bearer], structural.
> Path 2 (shield): [distance type], structural. Verdict: PASS.
```

### How the two paths relate to Tier 8

Tier 8 (Political Capture) is the institutional mechanism by which the shield is legislated
rather than merely structural. When Tier 8 is active:
- Path 2 evaluation must name political capture specifically
- The distance is not merely epistemic or spatial — it is formally encoded in accounting rules,
  regulatory exemptions, or treaty provisions
- A claim about Tier 8 costs must itself pass both paths:
  - Path 1: Who captures value from the suppression of B? (Extraction industry)
  - Path 2: What prevents correction? (The capture itself — recursive shield)

The recursive nature of Tier 8 is not a paradox; it is the structural explanation for why
externalization persists despite being known.

---

## Materials Requiring Update

The following materials should be updated to reflect the two-path structure:

| File | Action |
|---|---|
| `commons-bonds-rigor-test.docx` (D3 → .md conversion pending) | Before converting, review whether existing rigor tests use single-path or two-path structure. Add two-path template as header section. |
| `commons-bonds-rigor-testing-roles.html` (B2 → .md pending) | After converting, add canonical two-path template. Confirm "roles" document assigns Path 1 and Path 2 responsibility explicitly. |
| WS06 (`06_counterargument_framework.md`) | Each counterargument rebuttal should include abbreviated two-path notation. |
| WS14 (`14_counterargument_integration.md`) | Same as WS06. |
| Any chapter guidance doc referencing "rigor" | Replace single-path language with two-path structure per canonical template above. |

---

## Completion Criteria

C5 is complete when:
- [ ] Canonical two-path template is the active form in `commons-bonds-rigor-test.docx` (or its .md conversion)
- [ ] `commons-bonds-rigor-testing-roles.html` (B2) references two-path structure
- [ ] WS06 and WS14 use abbreviated two-path notation for counterargument rebuttals
- [ ] No rigor test in any WS file uses single-path evaluation without annotation

---

## One-Paragraph Summary for Inline Reference

> The Commons Bonds rigor test operates on two paths. **Path 1 (allocation symmetry)** tests
> whether the claim correctly identifies who captures value and who bears cost, and whether that
> asymmetry is structural. **Path 2 (shield absence)** tests whether the claim correctly identifies
> the distance condition that prevents the asymmetry from being recognized or corrected. A claim
> that passes Path 1 but not Path 2 identifies a real harm but cannot explain why it persists.
> A claim that passes Path 2 but not Path 1 names a structural condition but cannot locate the
> cost. Rigor requires both paths.

---

*End of C5 patch. The two-path structure is the default for all future rigor testing. The
one-paragraph summary above can be quoted verbatim in WS files or chapter guidance docs.*
