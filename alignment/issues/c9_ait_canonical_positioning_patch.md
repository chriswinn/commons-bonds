# C9 Patch — AIT Canonical Positioning (scaffolding-vs-load-bearing)

**Date:** 2026-04-21
**Version:** 1.0.0
**Patch ID:** C9
**Protocol applied:** `commons_bonds_rigor_protocol_1_1_0.md`
**Status:** Produced pending manual GitHub apply

---

## 1. Purpose

Establish the AIT (Abundance Inversion Test) as the framework's epistemic core independent of the specific layer taxonomy. The distinction is load-bearing in its own right: AIT validity does not depend on the layer set being complete or optimally named. Layers provide systematic coverage, vocabulary portability, pedagogical shape, and next-gen scholarship seed points — but they are scaffolding, not load-bearing.

**Motivation.** Surfaced during session v1.21.0 layer-set review when the user asked whether the framework needs specific layers or whether AIT stands on its own. AIT operates on any proposed cost by naming its underlying scarcity and testing whether the cost evaporates under abundance. The test's validity is a property of the cost-scarcity relationship itself, not a property of any containing taxonomy. Ratifying this explicitly takes pressure off layer-set perfection and gives the framework an accurate account of where its epistemic load actually sits.

**Corollary:** Future layer-set changes (additions, mergers, renames) are organizational revisions, not framework integrity events. This is worth stating because the project has iterated on layer names three times already; the current statement absorbs that iteration rather than presenting it as instability.

---

## 2. Target files

| File | Format | Insert location(s) |
|---|---|---|
| `CommonsBondsTechnicalAppendixv0_0_2.html` | .html (math) | §A.8 intro (primary); Appendix intro (secondary if present) |
| `commons_bonds_updated_glossary_v2.html` | .html (glossary) | "Abundance Inversion Test" entry (expand); "Abundance Layer" entry (append clarification) |

Confirm section identifier on apply — prior handoff notes list A.8 as AIT methodology and C.2 as layer definitions; if structure has drifted, locate AIT methodology section by content and use that location.

---

## 3. Canonical statement

The following paragraph is canonical. Insert verbatim (preserving HTML tag wrapping per target file) at the locations specified in §4 and §5.

> **The Abundance Inversion Test (AIT) is a universal falsifiability gate for proposed cost categories.** A proposed cost survives AIT if and only if naming its underlying scarcity and imagining that scarcity inverted causes the cost to evaporate. AIT applies to any cost proposal independently of whether a pre-existing layer taxonomy accommodates it — the test operates on the cost-scarcity relationship itself. The abundance layers in the Commons Bonds taxonomy provide systematic coverage, vocabulary portability, pedagogical shape, and scholarship seed points, but they are scaffolding, not load-bearing. A framework with an imperfect or incomplete layer set still has valid AIT application to individual cost proposals. **AIT is the framework's epistemic core; layers are its organizational surface.**

---

## 4. Insert into Technical Appendix

### 4.1 Primary location: §A.8 (AIT section) introduction

Find the opening of section A.8 (the AIT methodology section). Insert the canonical statement as the first paragraph of §A.8, before any existing methodology content.

**HTML form to insert:**

```html
<p><strong>The Abundance Inversion Test (AIT) is a universal falsifiability gate for proposed cost categories.</strong> A proposed cost survives AIT if and only if naming its underlying scarcity and imagining that scarcity inverted causes the cost to evaporate. AIT applies to any cost proposal independently of whether a pre-existing layer taxonomy accommodates it — the test operates on the cost-scarcity relationship itself. The abundance layers in the Commons Bonds taxonomy provide systematic coverage, vocabulary portability, pedagogical shape, and scholarship seed points, but they are scaffolding, not load-bearing. A framework with an imperfect or incomplete layer set still has valid AIT application to individual cost proposals. <strong>AIT is the framework's epistemic core; layers are its organizational surface.</strong></p>
```

### 4.2 Secondary location: Appendix introduction (if present)

If the Appendix has a top-level introduction before §A.1, add a one-sentence cross-reference:

```html
<p>Section A.8 establishes AIT as the framework's epistemic core, independent of the specific layer taxonomy presented in §C.</p>
```

If no top-level introduction exists, skip. The §A.8 insert is sufficient on its own.

---

## 5. Insert into Glossary

### 5.1 Expand existing "Abundance Inversion Test" entry

Locate the existing AIT glossary entry. Replace its definition block with the expanded form below. If the existing entry is a one-line definition, append the canonical statement after it rather than replacing.

**HTML form:**

```html
<dt>Abundance Inversion Test (AIT)</dt>
<dd>A universal falsifiability gate for proposed cost categories. A proposed cost survives AIT if and only if naming its underlying scarcity and imagining that scarcity inverted causes the cost to evaporate. AIT applies to any cost proposal independently of whether a pre-existing layer taxonomy accommodates it — the test operates on the cost-scarcity relationship itself. AIT is the framework's epistemic core; the abundance layers are its organizational surface. See Technical Appendix §A.8.</dd>
```

### 5.2 Append clarification to existing "Abundance Layer" entry

Locate the existing "Abundance Layer" entry. Append the clarification paragraph inside or immediately after the `<dd>` block:

```html
<p>The abundance layers provide systematic coverage, vocabulary portability, pedagogical shape, and scholarship seed points. They are the framework's organizational scaffolding, not its epistemic load-bearing. Valid AIT application to an individual cost proposal does not require that the cost fit an existing layer; layers support systematic taxonomy-building and vocabulary, not validity. Layer-set revisions (additions, mergers, renames) are organizational, not framework-integrity events. See <em>Abundance Inversion Test</em> and Technical Appendix §A.8.</p>
```

---

## 6. Project-wide audit task list

Files that may contain AIT scope language reading as over-committing to a specific layer taxonomy. Audit post-apply and soften or align any phrases suggesting AIT validity *requires* the seven-layer set (or any specific layer count).

| File | Audit target | Action |
|---|---|---|
| `eight-tier-v10.html` | AIT methodology sections | Verify no language implying AIT requires specific layer taxonomy; align if present |
| `error-out-v10.html` | Duplicate of above | Same audit |
| `eight-tier-decomposition-v10.md` | AIT introductory paragraphs | Same audit |
| `Chapter__6_ThreeWaysofCounting.html` / `.md` | AIT explanation for general audience | Add scaffolding/load-bearing framing if missing; Ch6 is the highest-public-exposure AIT explanation |
| `commons_bonds_integrated_framework.html` | AIT positioning post-C6 patch | Align with canonical statement |
| `commons_bonds_rigor_protocol_1_1_0.md` | §4 (Test 1 — AIT) | Add cross-reference to C9 patch; consider §4.5 explicit note on scaffolding-vs-load-bearing |
| WS02 (abundance layers workstream) when drafted | Layer introduction | Must align with scaffolding framing from the start |
| WS08 (technical appendix stub) | AIT references | Align |

---

## 7. Completion criteria

This patch is complete when:

1. Technical Appendix §A.8 contains the canonical statement as opening paragraph.
2. Glossary "Abundance Inversion Test" entry contains the canonical statement.
3. Glossary "Abundance Layer" entry has the scaffolding clarification appended.
4. Project-wide audit from §6 complete; any conflicting language softened or aligned.
5. Rigor protocol §4 cross-references this patch.

---

## 8. Verification

For each applied location:

- [ ] Canonical statement text matches §3 verbatim (modulo HTML tag wrapping).
- [ ] Insert location is correct (§A.8 intro in Tech Appendix; correct glossary entries).
- [ ] No duplicate or contradictory AIT definitions remain elsewhere in the same file.
- [ ] Layer-set references no longer imply AIT validity depends on having "the right" layer set.
- [ ] `grep -i "epistemic core"` returns at least one match in Tech Appendix and Glossary post-apply.
- [ ] `grep -i "scaffolding, not load-bearing"` returns matches in both Tech Appendix and Glossary.
- [ ] Rigor protocol §4 has a cross-reference line pointing to C9.

---

## 9. Dependencies and queue position

- **Independent of C7 and C8.** AIT positioning does not depend on layer-naming review outcomes. Apply before, during, or after C7/C8 ratification.
- **Precedes future layer-set additions.** If Cohesion, Informational, Agency, or other layers are ratified in this or future sessions, the canonical statement in this patch anchors them correctly without further revision.
- **Queue position:** Apply after C6. Recommended order: C1 → C2 → C3 → C4 → C5 → C6 → **C9** → (C7/C8 on ratification) → (any subsequent Cx from layer-set work).

---

## 10. Change log

**v1.0.0 (2026-04-21):** Initial patch. Canonical statement drafted in session v1.21.0 when user asked whether AIT stands on its own without specific layers. Ratified same session. Insert locations: Tech Appendix §A.8, Glossary AIT entry and Abundance Layer entry. Audit list for project-wide alignment.

---

*End of C9 AIT Canonical Positioning Patch v1.0.0.*
