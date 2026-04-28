# Intergenerational-Cluster Vocabulary Inventory — 2026-04-28

**Generated:** 2026-04-28 (mechanical inventory pass)
**Purpose:** Input data for the retirement-cluster + intergenerational-cluster vocabulary rigor pass v1.0.0.
**Status:** DATA only. No verdicts assigned. Pattern tags are heuristic.

## Scope

**Publisher-facing primary scope (12 files):**
- 10 chapter drafts: `manuscript/chapters/Chapter_*Draft.md` + `Chapter__6_ThreeWaysofCounting__Draft.html` + `Chapter__6___SupplementaryDrafts_2026-04-24.md` (Note: Ch 3 has no draft, only a guidance doc.)
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` (7,438 lines)
- `core/glossary/commons_bonds_updated_glossary_v3.html` (406 lines)

**Drafting scaffolding (separate aggregate counts only — no per-occurrence tables):**
- 10 GuidanceDocs: `manuscript/chapters/Chapter_*___GuidanceDoc.md`

**Out of scope (not audited):** terms_index.md; tools/rigor-passes/*.md; alignment/sessions/*.md; core/glossary/*v2*; core/technical-appendix/archive/*; alignment/sessions/archive/*; core/decomposition/eight-tier-v10.html; .chriswinn/.

## File-label legend

| File label | Path |
|---|---|
| Ch1 draft | manuscript/chapters/Chapter__1___Draft.md |
| Ch2 draft | manuscript/chapters/Chapter__2_TheMiner__Draft.md |
| Ch4 draft | manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md |
| Ch5 draft | manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md |
| Ch6 HTML | manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html |
| Ch6 suppl | manuscript/chapters/Chapter__6___SupplementaryDrafts_2026-04-24.md |
| Ch7 draft | manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md |
| Ch8 draft | manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md |
| Ch9 draft | manuscript/chapters/Chapter__9_PricingHonestly__Draft.md |
| Ch10 draft | manuscript/chapters/Chapter_10_CommonBonds__Draft.md |
| TA | core/technical-appendix/TechnicalAppendix_v1.0.0.html |
| Glossary v3 | core/glossary/commons_bonds_updated_glossary_v3.html |
| Ch_n_ guide | manuscript/chapters/Chapter__n___GuidanceDoc.md |

## Counting note

Aggregate counts below are **line counts** from `grep -nH` output (i.e. the number of lines on which a match was found; multi-match lines are counted once). For acronyms and short tokens the numbers are very close to true occurrence count; for long-phrase terms they are exact. Tags are heuristic and preliminary.

## Heuristic pattern-tag rubric

- `first-introduction` — first occurrence in a chapter file (especially Ch1/Ch2 vocabulary-introduction)
- `compressed-scalar` — line carries an equation (`=`, `$`, percent, "33", "108 trillion", etc.)
- `technical-formal` — Tech Appendix derivation, equation, gates spec, glossary entry
- `cross-chapter-handle?` — recurring named handle without compressed-scalar / first-intro fingerprint (`?` flags author judgment)
- `repeated-paragraph?` — ≥2 occurrences within ±3 lines in the same file
- `adjective-form?` — used as adjective ("the X question") where prose might suffice
- `framework-signaling?` — appears to mark framework-membership rather than do work
- `retired-trace` — Category-H retirement record / cross-reference inside glossary or TA
- `retired-regression` — Category-H term used in publisher-facing prose with framework intent

---

## Category A — Ring-1 ratified

### Term: Commons Bonds (proper-noun)

**Category:** A. Ring-1 ratified
**Pattern (regex):** `Commons Bonds` · case-sensitive

**Aggregate counts:**
- Publisher-facing: **23 lines** across Ch2(1) Ch4(1) Ch5(1) Ch6 HTML(2) Ch8(1) Ch9(2) Ch10(4) TA(7) Glossary v3(4)
- GuidanceDocs: **23 lines** (Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch9, Ch10 guides)
- Combined: **46**

**Per-occurrence records (publisher-facing):**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 1 | first-introduction | "# Commons Bonds" (chapter title) |
| Ch4 draft | 1 | cross-chapter-handle? | "# Commons Bonds" (chapter title) |
| Ch5 draft | 5 | cross-chapter-handle? | "# Commons Bonds" |
| Ch6 HTML | 7 | technical-formal | HTML `<title>` "Chapter 6 — Three Ways of Counting — Commons Bonds" |
| Ch6 HTML | 119 | technical-formal | "Commons Bonds — Chris Winn" running header |
| Ch8 draft | 3 | cross-chapter-handle? | "# Commons Bonds" |
| Ch9 draft | 1 | cross-chapter-handle? | "# Commons Bonds" |
| Ch9 draft | 205 | framework-signaling? | "implements the full Commons Bonds framework" |
| Ch9 draft | 247 | framework-signaling? | "Commons Bonds is, and can only be, an attempt to do the same…" — closing-passage framework gloss |
| Ch10 draft | 3 | cross-chapter-handle? | "the title shift from Commons Bonds to common bonds" — meta about title |
| Ch10 draft | 7 | cross-chapter-handle? | "# Commons Bonds" |
| Ch10 draft | 113 | first-introduction | "The title of this book is Commons Bonds." (climactic title-meaning passage) |
| Ch10 draft | 117 | repeated-paragraph? | "Commons Bonds, as I first intended it, meant obligations owed…" — book's title-meaning passage |
| Glossary v3 | 6 | technical-formal | `<title>Commons Bonds — Updated Glossary v3</title>` |
| Glossary v3 | 130 | technical-formal | "<h1>Commons Bonds</h1>" |
| Glossary v3 | 146 | technical-formal | term-name "Commons Bonds" |
| Glossary v3 | 401 | technical-formal | "Commons Bonds Glossary v3 — Updated 2026-04-24" footer |
| TA | 7 | technical-formal | "Technical Appendix — Commons Bonds — v1.0.0" HTML title |
| TA | 145 | technical-formal | "Technical Appendix — Commons Bonds" header |
| TA | 1144 | technical-formal | "§5.2 What the Commons Bonds framework adds" |
| TA | 1147 | technical-formal | "The Commons Bonds framework extends Hotelling 1931 with the following identity" |
| TA | 1178 | technical-formal | "The Commons Bonds framework's contribution: the identity extension…" |
| TA | 7122 | technical-formal | "Commons Bonds — Technical Appendix (Complete Version)" footer |

### Term: commons bonds (lowercase)

**Category:** A
**Pattern (regex):** `\bcommons bonds\b` · case-sensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 147 | technical-formal | term-definition: "Polysemic title: obligations (commons bonds) becoming shared identity (common bonds)" |

### Term: Cost Severance (proper-noun)

**Category:** A
**Pattern (regex):** `Cost Severance` · case-sensitive

**Aggregate counts:**
- Publisher-facing: **48 lines** — Ch1(2), Ch5(1), Ch6 HTML(4), Ch6 suppl(2), Ch7(1), Glossary v3(11), TA(27)
- GuidanceDocs: **1** (Ch6 guide line 380)
- Combined: **49**

**Per-occurrence records (publisher-facing):**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch1 draft | 7 | technical-formal | "Framework terms (Cost Severance, RCV, CIT, Accountability Bond, the 10 commons categories) are Ch 6 + Tech Appendix territory and are NOT to appear in Ch 1" — meta-discipline marker |
| Ch1 draft | 95 | technical-formal | "Does not invoke framework vocabulary (CIT, RCV, Cost Severance, Accountability Bond, etc.)" — Ch 1 register-discipline checklist |
| Ch5 draft | 105 | first-introduction | "Social Security: Cost Severance in the Financial Commons" (section header) |
| Ch5 draft | 193 | cross-chapter-handle? | "they form the aggregate Bond posting (B = B₁ + B₂) the framework's central equation requires when it states that Cost Severance equals Residual Commons Value minus Bond posting" — equation gloss |
| Ch5 draft | 195 | cross-chapter-handle? | "framework's CSD (Cost Severance Damages) instrument" |
| Ch6 HTML | 663 | repeated-paragraph?,cross-chapter-handle? | "share the same primitive equation — Cost Severance equals Residual Commons Value minus Bond posting" |
| Ch6 HTML | 683 | cross-chapter-handle? | "framework's CSD (Cost Severance Damages) instrument" |
| Ch6 HTML | 799 | cross-chapter-handle? | "minus per-unit standard Hotelling rent equals per-unit Cost Severance" |
| Ch6 suppl | 246 | cross-chapter-handle? | duplicate of Ch6 HTML 683 (CSD methodology) |
| Ch6 suppl | 276 | cross-chapter-handle?,repeated-paragraph? | "specified a single Cost Severance accounting object" + "Cost Severance equals Residual Commons Value minus Bond posting" |
| Ch6 suppl | 280 | cross-chapter-handle? | "Hotelling Identity is the framework's bridge: per-unit Residual Commons Value minus per-unit standard Hotelling rent equals per-unit Cost Severance" |
| Ch6 suppl | 282 | cross-chapter-handle? | "aggregate Cost Severance accounting depends on the gates being run together" |
| Ch7 draft | 141 | compressed-scalar | table column "Cost Severance" — convergence table |
| Glossary v3 | 153 | technical-formal | causal chain "Value Extraction → Cost Severance → Severed Cost" |
| Glossary v3 | 159 | technical-formal | term-name "Cost Severance" |
| Glossary v3 | 160 | technical-formal | term-definition: structural-mechanism noun |
| Glossary v3 | 166 | technical-formal | Severed Cost def: "result/quantity noun naming the quantified outcome of the Cost Severance mechanism" |
| Glossary v3 | 202 | technical-formal | term-name "CS = RCV − B (Cost Severance equation)" |
| Glossary v3 | 203 | technical-formal | "Cost Severance equals specifically Residual Commons Value minus Accountability Bond" |
| Glossary v3 | 208 | technical-formal | "Cost Severance Damages (CSD)" term-name |
| Glossary v3 | 216 | technical-formal | "Aggregate framework instrument B = B1 + B2 closing the Cost Severance gap" |
| Glossary v3 | 229 | technical-formal | "RCV − Hotelling rent = CS per unit" + "per-unit Cost Severance" |
| Glossary v3 | 264 | technical-formal | IPG def: "distinct from Cost Severance (which uses B not market_price)" |
| Glossary v3 | 270 | technical-formal | Abundance Masking def: "(analogous to Cost Severance + Severed Cost)" |
| Glossary v3 | 287 | technical-formal | "CSD (Cost Severance Damages)" |
| Glossary v3 | 338 | retired-trace | Value Capture RETIRED entry: "favored Extraction (separation-from-source semantics pairs with Cost Severance's severance-from-capturer semantics)" |
| Glossary v3 | 342 | retired-trace | "Spatial Cost Severance (capitalized proper-noun) → spatial cost severance (lowercase prose phrase)" — un-retire record |
| Glossary v3 | 343 | retired-trace | "Geographic subtype of Cost Severance: costs concentrate where extraction happens" |
| Glossary v3 | 347 | retired-trace | "Temporal Cost Severance" term-name |
| Glossary v3 | 389 | technical-formal | history record "Cost Severance Option C ratified" |
| TA | 487 | technical-formal | "Cost Severance is formally defined as:" |
| TA | 568 | technical-formal | "Cost Severance Damages (CSD) record + Accountability Bond v1.2 (B = B₁ + B₂) record" |
| TA | 589 | technical-formal | "(Cost Severance equals Residual Commons Value minus Bond posting). The two instruments differ…" |
| TA | 593 | technical-formal | "CSD — Cost Severance Damages (backward-looking):" |
| TA | 732 | technical-formal | "consistent with the Structural Cost Severance Theorem (E.1)" |
| TA | 1362 | cross-chapter-handle? | "Spatial abundance masks the spatial dimension of cost severance" (lowercase appears here — note: this row counts the "Cost Severance" capitalised match later in same sentence) |
| TA | 1437 | technical-formal | "Cost Severance integral (Section K.3)" |
| TA | 1523 | technical-formal | "If yes → cost claim is consumption-of-finite-commons (Cost Severance proper)" |
| TA | 1526 | technical-formal | "Only claims passing both qualify as Cost Severance" |
| TA | 1559 | technical-formal | "platform attention-extraction… constitutes Cost Severance" — worked example |
| TA | 3275 | technical-formal | "Theorem E.1 (Structural Cost Severance)" |
| TA | 3948 | compressed-scalar | "Implied Cost Severance (CS = RCV − B) for Norway:" |
| TA | 4380 | compressed-scalar | "Implied Cost Severance:" |
| TA | 6288 | technical-formal | "Rejected alternative — Single Cost Severance accounting object" — methodology defense |
| TA | 6445 | cross-chapter-handle? | "aggregate Cost Severance accounting depends on the gates being run together" |
| TA | 6680 | technical-formal | "Only claims passing both qualify as Cost Severance" — duplicate of 1526 |
| TA | 7016 | technical-formal | "M.4 Preservation of the Cost Severance Relation" |

### Term: cost severance (lowercase)

**Category:** A
**Pattern (regex):** `\bcost severance\b` · case-sensitive

**Aggregate counts:**
- Publisher-facing: **90 lines** — Ch2(5), Ch4(7), Ch5(13), Ch6 HTML(4), Ch7(7), Ch8(1), Ch9(7), Ch10(3), Glossary v3(7), TA(36)
- GuidanceDocs: **54 lines** — Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8, Ch9, Ch10 guides
- Combined: **144**

This is the framework's most-used lowercase prose phrase. Pattern observations:
- **Ch2 introduces it (line 133–139)** as paired definition with severed cost + value extraction; Ch2 line 235 closing summary list.
- **Ch4 establishes Norway-existence-proof framing** with 7 occurrences clustering ~lines 15–105.
- **Ch5 reaches 13 occurrences** — this chapter does the case-by-case work; expect heaviest concentration of `cross-chapter-handle?` and `repeated-paragraph?` tags in Ch5.
- **Ch10 line 19 first paragraph** reuses it as the book's closing-chapter mechanism gloss.
- **TA's 36 occurrences** are predominantly `technical-formal` (definitions, theorems, worked-example walkthroughs).

**Per-occurrence records (publisher-facing) — Ch2/Ch4/Ch5 sample (high-density):**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 107 | first-introduction | "This is the dynastic dimension of cost severance: not just what was taken from the people who stayed, but what was taken from the generations who would have built what came next" |
| Ch2 draft | 139 | repeated-paragraph?,cross-chapter-handle? | "These three terms — cost severance, severed cost, value extraction — will appear throughout this book" — vocabulary-introduction list |
| Ch2 draft | 155 | first-introduction | "This is spatial cost severance" — first lowercase compositional |
| Ch2 draft | 157 | first-introduction | "We will see temporal cost severance in later chapters" |
| Ch2 draft | 235 | cross-chapter-handle? | summary checklist "Cost vocabulary introduced: cost severance, severed cost, value extraction" |
| Ch4 draft | 15 | cross-chapter-handle? | "It proves, among other things, that cost severance is a policy choice" |
| Ch4 draft | 39 | cross-chapter-handle? | "what is the cost severance of a given extraction — can now be asked of a case…" |
| Ch4 draft | 43 | repeated-paragraph?,cross-chapter-handle? | "It says the cost severance has been dramatically reduced. It does not say the cost severance is zero" |
| Ch4 draft | 53 | cross-chapter-handle? | "The framework's conclusion, applied to Norway, is this: the cost severance is much smaller than Appalachia's…" |
| Ch4 draft | 69 | adjective-form? | "communities most vulnerable to cost severance are the ones whose institutional defenses are weakest" |
| Ch4 draft | 83 | cross-chapter-handle? | "The cost severance, in the framework's terms, is very large" |
| Ch4 draft | 105 | cross-chapter-handle? | "when Norway proves that cost severance can be dramatically reduced…" |
| Ch5 draft | 31 | cross-chapter-handle? | "financial reckoning tells the story of cost severance in numbers that cannot be argued with" |
| Ch5 draft | 35 | cross-chapter-handle?,repeated-paragraph? | 4× "cost severance" inside one paragraph (Libby criminal-prosecution analysis): "case study in cost-severance accounting", "the cost severance documented above", "the cost severance the framework's accounting names" |
| Ch5 draft | 45 | first-introduction | "spill severed costs across every dimension that cost severance can operate" |
| Ch5 draft | 73 | adjective-form? | "Spatial cost severance, operating through global supply chains" |
| Ch5 draft | 93 | cross-chapter-handle? | "The cost severance the chapter prices is the unrecovered welfare loss…" |
| Ch5 draft | 95 | cross-chapter-handle? | "intergenerational cost severance accumulates" + "in cost-severance accounting, a delay" + "cost severance the cases of this chapter document" + "accountability gap it was built to address" — paragraph saturated with the term |
| Ch5 draft | 107 | first-introduction | "most devastating example of cost severance in American history" |
| Ch5 draft | 119 | cross-chapter-handle? | "This is cost severance operating in the financial commons" |
| Ch5 draft | 125 | cross-chapter-handle? | "But the specific way it has been funded reveals cost severance operating at civilizational scale" |
| Ch5 draft | 127 | cross-chapter-handle? | "documents what was, and continues to be, the cost severance the U.S. choice produces" |
| Ch5 draft | 135 | cross-chapter-handle? | "The cost severance the chapter prices is structurally upstream" |
| Ch5 draft | 137 | cross-chapter-handle? | "The cost severance is not located in how the surpluses were invested" |
| Ch5 draft | 139 | cross-chapter-handle? | "Generating obligations during the surplus-window that the actuarial reports projected would deplete during the deficit-window was the cost severance" |
| Ch5 draft | 145 | cross-chapter-handle?,repeated-paragraph? | "The framework prices the cost severance" (4× in this paragraph) |
| Ch5 draft | 149 | cross-chapter-handle? | "The Social Security case demonstrates the cost-severance pattern at intergenerational scale" |
| Ch5 draft | 159 | cross-chapter-handle? | "This is cost severance operating through a second layer" |
| Ch5 draft | 161 | cross-chapter-handle? | "The GoFundMe-as-default-safety-net pattern is what cost severance looks like" |
| Ch5 draft | 163 | cross-chapter-handle? | "This is cost severance operating on the dying body" |
| Ch5 draft | 165 | cross-chapter-handle? | "End-of-life care is the most emotionally legible illustration of cost severance in healthcare" |
| Ch5 draft | 209 | cross-chapter-handle? | "named the cost severance the American extraction regimes produce" |
| Ch5 draft | 211 | adjective-form? | "Not whether cost severance exists, but what we do about it" — chapter closer |

**Per-occurrence records (publisher-facing) — Ch6/Ch7/Ch8/Ch9/Ch10:**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 174 | first-introduction | "If cost severance is real — if market prices systematically understate the true cost of extracting from the commons — then how large is the gap?" — chapter-opener |
| Ch6 HTML | 221 | cross-chapter-handle? | "fight over the SCC is itself a proxy war over acceptable cost severance levels" |
| Ch6 HTML | 591 | cross-chapter-handle? | "extraction under these conditions produces this much cost severance, and extraction under those conditions produces that much" |
| Ch6 HTML | 802 | cross-chapter-handle? | "total cost severance for a given extraction" |
| Ch7 draft | 21 | cross-chapter-handle? | "something about why cost severance operates the way it does on Earth" |
| Ch7 draft | 63 | cross-chapter-handle? | "There is no meaningful cost severance. Extract freely" |
| Ch7 draft | 107 | cross-chapter-handle?,repeated-paragraph? | "When the distance exists, cost severance operates… the severance becomes operationally impossible" + "Earth through spatial cost severance pricing" |
| Ch7 draft | 109 | cross-chapter-handle? | "Community Transition Reserves, spatial cost severance charges, border carbon adjustments" |
| Ch7 draft | 165 | cross-chapter-handle? | "Mars strips away the layers of uncertainty that allow Earth's cost severance to persist" |
| Ch7 draft | 187 | cross-chapter-handle? | "This book has described cost severance in the industrial and post-industrial economies" |
| Ch7 draft | 197 | cross-chapter-handle? | "When cost severance becomes publicly visible and consumers demand accountability" |
| Ch7 draft | 205 | cross-chapter-handle? | "cost severance requires distance — which means that the policy response on Earth is, in part, a distance-compression project" |
| Ch8 draft | 191 | cross-chapter-handle? | "The cost severance the chapter prices — the surplus that would otherwise have funded mobility" |
| Ch9 draft | 31 | cross-chapter-handle? | "framework prices those the same way it prices any commons capture: by the cost severance the capture imposes on the bearers" |
| Ch9 draft | 67 | cross-chapter-handle? | "An asteroid has no communities bearing spatial cost severance" |
| Ch9 draft | 91 | cross-chapter-handle? | "International trade, as it currently operates, is among other things a cost severance delivery system" |
| Ch9 draft | 95 | cross-chapter-handle? | "a country serious about closing its cost severance gap must apply the pricing to imports as well" |
| Ch9 draft | 97 | cross-chapter-handle? | "make imported goods bear the same cost severance charge that domestic production would" |
| Ch9 draft | 163 | cross-chapter-handle? | "framework's claim is not that the United States must become ethnically homogeneous… cost severance operates structurally regardless of ethnic composition" |
| Ch9 draft | 181 | cross-chapter-handle? | "distribution of healthcare-cost severance specific to that architecture" |
| Ch9 draft | 247 | repeated-paragraph?,framework-signaling? | closing passage gloss list "cost severance, residual commons value, severed cost, accountability bond, the civilizational substitutability gap" |
| Ch10 draft | 3 | cross-chapter-handle? | "cost severance as a function of distance" |
| Ch10 draft | 19 | first-introduction | "What I have called cost severance is a long word for a simple mechanism" |
| Ch10 draft | 37 | cross-chapter-handle? | "What I said in Chapter 7 — and what has stayed with me since — is that cost severance is a function of distance" |
| Glossary v3 | 160 | technical-formal | (definition row already counted in Cost Severance proper-noun above) |
| Glossary v3 | 209 | technical-formal | "Backward-looking framework instrument measuring realized human harm from cost severance" |
| Glossary v3 | 342 | retired-trace | "spatial cost severance (lowercase prose phrase)" |
| Glossary v3 | 343 | retired-trace | "Lowercase discipline mirrors intergenerational cost severance pattern" |
| Glossary v3 | 378 | retired-trace | Cost Bearing demoted: "Cost Bearing is someone bearing the cost of cost severance" |
| TA | 1153 | technical-formal | "the residual commons value per unit of extraction, minus the standard Hotelling rent per unit, equals the cost severance per unit" |
| TA | 1344 | technical-formal | "RCV formula measures cost severance" — paired with Abundance Test discovery role |
| TA | 1362 | technical-formal | "Spatial abundance masks the spatial dimension of cost severance" |
| TA | 1374 | technical-formal | "cost severance operates at maximum scale because B ≈ 0" |
| TA | 1392 | repeated-paragraph?,technical-formal | "Political capture is both a consequence of cost severance and a cause of its persistence" |
| TA | 2501 | technical-formal | "framework that prices cost severance by integrating discovered cost terms…" |
| TA | 3278 | technical-formal | Theorem statement: "cost severance CS > 0 occurs structurally, independent of extractor intentions" |
| TA | 3293 | technical-formal | proof-sketch: "validates the underlying cost severance structure" |
| TA | 3347 | technical-formal | "consistent cost severance patterns" |
| TA | 3390 | compressed-scalar | "Observed cost severance: $3.7–$6B reclamation shortfall" |
| TA | 3393 | technical-formal | "Note on spatial cost severance: The Damage Function IPG…" |
| TA | 3501 | technical-formal | "most explicit case of spatial cost severance operating at international scale" |
| TA | 5844 | technical-formal | "cost severance goes to zero because the administrator is the community bearing the cost" |
| TA | 5897 | technical-formal | "Framework output: CS → 0. No cost severance possible" |
| TA | 5900 | technical-formal | "Deepest structural insight: Cost severance requires distance" |
| TA | 6187 | technical-formal | Harvey-engagement passage: "Cost severance is the pricing dimension of this" |
| TA | 6738 | technical-formal | section reference "K.3 spatial cost severance formalization" |
| TA | 6767 | technical-formal | "K.3 Spatial cost severance formalization" — section header |
| TA | 6776 | technical-formal | "Spatial cost severance measures the geographic mismatch…" |
| TA | 6779 | technical-formal | "This formalization explains why cost severance produces systematic geographic inequality" |
| TA | 7019 | technical-formal | "Claim. The cost severance equation CS = RCV − B (Section B) holds…" |

### Term: Severed Cost (proper-noun)

**Category:** A
**Pattern (regex):** `Severed Cost` · case-sensitive

**Aggregate counts:** Publisher-facing **5**; GuidanceDocs **0**; Combined **5**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 153 | technical-formal | causal chain: "Value Extraction → Cost Severance → Severed Cost" |
| Glossary v3 | 160 | technical-formal | causal chain (same gloss) |
| Glossary v3 | 165 | technical-formal | term-name "Severed Cost" |
| Glossary v3 | 270 | technical-formal | "(analogous to Cost Severance + Severed Cost)" |
| TA | 4034 | technical-formal | "Case-study audit §2.1 + terms_index Severed Cost record" |

### Term: severed cost (lowercase)

**Category:** A
**Pattern (regex):** `\bsevered cost\b` · case-sensitive

**Aggregate counts:** Publisher-facing **18**; GuidanceDocs **1**; Combined **19**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 83 | first-introduction | "It is the severed cost made tangible" — first canonical |
| Ch2 draft | 135 | first-introduction | "The noun form is **severed cost**" — definitional |
| Ch2 draft | 139 | cross-chapter-handle? | summary "cost severance, severed cost, value extraction" |
| Ch2 draft | 235 | cross-chapter-handle? | chapter-summary list |
| Ch5 draft | 115 | cross-chapter-handle? | "The severed cost sits in that gap" |
| Ch5 draft | 159 | cross-chapter-handle? | "the severed cost concentrates on populations whose existing wealth-and-network constraints…" |
| Ch8 draft | 55 | compressed-scalar | "$4-6 billion gap — the severed cost sitting in the federal ledger in plain sight" |
| Ch8 draft | 59 | compressed-scalar | "national severed cost at three to seven dollars" |
| Ch8 draft | 125 | adjective-form? | "The cost of the fight is itself a severed cost" |
| Ch8 draft | 215 | compressed-scalar | "aggregate global severed cost across all resource extraction" |
| Ch8 draft | 217 | compressed-scalar | "annual global severed cost from fossil extraction is in the range of eight to ten trillion dollars" |
| Ch8 draft | 241 | compressed-scalar | "The gap between that number and the four-dollar-and-fifty-cent invoice is the severed cost" |
| Ch9 draft | 9 | compressed-scalar | "every severed cost was priced honestly" |
| Ch9 draft | 113 | compressed-scalar | "When the severed cost is denominated in money" |
| Ch9 draft | 247 | framework-signaling? | closing-passage gloss list |
| Ch10 draft | 65 | cross-chapter-handle? | "The severed cost was always there. It has always been carried by somebody" |
| Ch10 draft | 139 | cross-chapter-handle? | "the total weight of severed cost in the world" |
| Glossary v3 | 166 | technical-formal | term-definition |

### Term: Cᵢ + Cost component + Cost variable (combined)

**Category:** A
**Pattern (combined):** `Cᵢ` (Unicode subscript) + `cost component` + `cost variable` · case-insensitive
**Methodology note:** The Unicode `ᵢ` character was difficult to grep alone; combined with `cost component` and `cost variable` as the spec groups them. Counts may include pure-prose "cost component" uses that are not the Cᵢ symbol.

**Aggregate counts:** Publisher-facing **28** (Ch1: 1, Ch7: 1, Ch8: 2, Ch10: 1, Glossary v3: 8, TA: 15); GuidanceDocs **1**; Combined **29**

**Per-occurrence highlights:**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch1 draft | 66 | technical-formal | meta-note "what Ch 6 will later name as Cᵢ admitted via CIT through Four Gates" |
| Ch7 draft | 57 | cross-chapter-handle? | "The foreclosure cost component drops" — uses "cost component" as prose |
| Ch8 draft | 25 | cross-chapter-handle? | "what follows walks each cost component the framework's Four Gates admit — every Cᵢ that passes the discipline of the Commons Inversion Test" |
| Ch8 draft | 77 | adjective-form? | "This is the cost component Chapter 2 named through the $100 barrel passage" |
| Ch8 draft | 147 | technical-formal | "The framework's Cᵢ-summation discipline (RCV = ∫ (Σ Cᵢ) · D dt …)" |
| Ch10 draft | 67 | cross-chapter-handle? | "the same cost-component decomposition" + "A cost component I have not included" — uses term as prose-handle |
| Glossary v3 | 133 | technical-formal | subtitle "(replaced by Cᵢ admitted via Four Gates per Path F + tier-dissolution ratifications)" |
| Glossary v3 | 178 | technical-formal | "if the candidate cost becomes visible as commons-dependent, admit to Cᵢ via Four Gates" |
| Glossary v3 | 191 | technical-formal | term-name "Cost (Cᵢ)" |
| Glossary v3 | 192 | technical-formal | term-definition "Indexed cost variables admitted to RCV via the Four Gates" |
| Glossary v3 | 292 | technical-formal | "Four Gates (admission apparatus for Cᵢ)" |
| Glossary v3 | 298 | technical-formal | "Independence — mathematical condition; cost not redundantly correlated with already-admitted Cᵢ" |
| Glossary v3 | 363 | retired-trace | FGC retired entry: "costs are now Cᵢ admitted via Four Gates" |
| Glossary v3 | 373 | retired-trace | 8-tier retired entry: "REPLACED by Cᵢ indexed cost variables admitted through Four Gates" |
| TA | 331 | technical-formal | "RCV = ∫ (Σ Cᵢ) · D dt with convergence-preservation proof" |
| TA | 1774 | technical-formal | Independence gate "no double-counting" worked example |
| TA | 1826 | technical-formal | "at the level of Cᵢ admission, healthcare-cost-on-bodies and community-cost-on-population structure are distinct cost streams" |
| TA | 1870 | technical-formal | "apartment manager's costs; landlord profits — separate Cᵢ" |
| TA | 1882 | technical-formal | "AIT's pre-CIT framing obscured this" — about Cᵢ admission |
| TA | 2002 | technical-formal | "Admitting all four as separate Cᵢ would" |
| TA | 2012 | technical-formal | "when admitting multiple Cᵢ from the same case" |
| TA | 2018 | technical-formal | "(household-wealth-destruction as one Cᵢ)" |
| TA | 2078 | technical-formal | Mars-asteroid worked example: "Multiple commons producing multiple Cᵢ" |
| TA | 2084 | technical-formal | "The asteroid-miner case admits multiple Cᵢ" |
| TA | 2239 | technical-formal | opioid Appalachia worked example |
| TA | 2612 | technical-formal | "Cᵢ (candidate)" |
| TA | 2694 | technical-formal | "Cᵢ asymptotic behavior" |

### Term: RCV (acronym)

**Category:** A
**Pattern (regex):** `\bRCV\b` · case-sensitive

**Aggregate counts:**
- Publisher-facing: **262 lines** — Ch1(3), Ch5(4), Ch6 HTML(50+), Ch6 suppl(15), Ch7(20+), Ch8(2), Ch9(2), Glossary v3(20+), TA(150+)
- GuidanceDocs: **41**
- Combined: **303**

This is the framework's most-used acronym. The TA glossary self-reports 729 occurrences across 34 files as of 2026-04-24 (TA line 696). Per-occurrence enumeration not feasible at this scale within inventory file size constraints.

**Pattern observations (file-grouped):**

| File | Lines | Density profile |
|---|---|---|
| Ch1 draft | 3 lines (7, 60, 95) | All meta-discipline references ("Ch 1 doesn't invoke RCV"); none are framework-deployment uses |
| Ch5 draft | 4 lines (51, 205, 207, x) | All `cross-chapter-handle?` — empirical-state-of-B claims |
| Ch6 HTML | ~50 lines | Heavy `technical-formal` cluster (formula, integrand, IPG = RCV/P, three-method estimation) |
| Ch6 suppl | 15 lines | Methodology-defense passages |
| Ch7 draft | ~20 lines | Mars-thought-experiment scenario tables ("RCV result: very low / very high / moderate") |
| Ch8 draft | 2 lines (77, 147) | Per-ton arithmetic backstop |
| Ch9 draft | 2 lines (69, 247) | Closing-passage gloss list |
| Glossary v3 | ~22 lines | Term-definition + cross-references |
| TA | ~150 lines | Definition A.6, Theorem E.1/E.2, all empirical case walkthroughs, Section M generalization |

**Sampled high-significance occurrences:**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 293 | first-introduction | "Approach 3 — The RCV Model" — section header |
| Ch6 HTML | 320 | technical-formal | full RCV(R, t₀) integral specification |
| Ch6 HTML | 343 | technical-formal | "Cost severance is what is left after you subtract from RCV whatever accountability bond B has actually been posted" |
| Ch6 HTML | 346 | compressed-scalar | "CS(R, tₔ) = RCV(R, tₔ) − B(R, tₔ)" |
| Ch6 HTML | 352 | compressed-scalar | "IPG = RCV / Pmarket" |
| Ch7 draft | 83 | cross-chapter-handle? | "residual commons value approaches the market price… This is the lowest-RCV extraction" |
| Ch7 draft | 141 | technical-formal | scenario table column |
| Ch9 draft | 69 | cross-chapter-handle? | "extract from the lowest-RCV source first" |
| Ch9 draft | 247 | framework-signaling? | closing-passage gloss list "the RCV model, in its three convergent forms" |
| Glossary v3 | 171 | technical-formal | term-name "Residual Commons Value (RCV)" |
| TA | 696 | technical-formal | "RCV is the framework's most-used term (729 occurrences across 34 files as of 2026-04-24)" — meta-record |

### Term: Residual Commons Value (full form)

**Category:** A
**Pattern (regex):** `Residual Commons Value` · case-sensitive

**Aggregate counts:** Publisher-facing **22**; GuidanceDocs **0**; Combined **22**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 51, 209 | cross-chapter-handle? | "B (the bond posting) at well below RCV (residual commons value)" — definitional pairing |
| Ch6 HTML | 314, 660, 663 | technical-formal | "The residual commons value combines these two components"; "framework's Residual Commons Value calculation operates in exactly this register"; "Cost Severance equals Residual Commons Value minus Bond posting" |
| Ch6 HTML | 790, 799 | technical-formal | "quantification framework (Residual Commons Value)"; "per-unit Residual Commons Value minus per-unit standard Hotelling rent" |
| Ch6 suppl | 70, 74, 104, 110, 272, 276, 278, 280, 290 | technical-formal | methodology-defense + Parfit cluster |
| Ch9 draft | 247 | framework-signaling? | closing-passage gloss "residual commons value" lowercase form (also matches `Residual Commons Value` proper) |
| Glossary v3 | 171, 172, 203, 235, 288 | technical-formal | term-record + cross-references |
| TA | 464, 589, 618, 4947, 6351 | technical-formal | "Definition A.6 (Residual Commons Value — Core Formula)"; method 1 worked example |

### Term: Value Extraction (proper-noun)

**Category:** A
**Pattern (regex):** `Value Extraction` · case-sensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **0**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 152 | technical-formal | term-name "Value Extraction" |
| Glossary v3 | 153 | technical-formal | term-definition + causal-chain framing |
| Glossary v3 | 160 | technical-formal | causal-chain repeat |
| Glossary v3 | 338 | retired-trace | Value Capture (RETIRED) entry references "Value Extraction" as ratified replacement |

### Term: value extraction (lowercase)

**Category:** A
**Pattern (regex):** `\bvalue extraction\b` · case-sensitive

**Aggregate counts:** Publisher-facing **10**; GuidanceDocs **0**; Combined **10**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 137 | first-introduction | definitional "**value extraction**: the act of separating worth from its source while declining to absorb the full cost" |
| Ch2 draft | 139 | cross-chapter-handle? | summary list |
| Ch2 draft | 141 | first-introduction | "The phrase 'value extraction' carries an established lineage worth naming" — Mazzucato attribution |
| Ch2 draft | 157 | cross-chapter-handle? | "the temporal dimension — the gap between present value extraction and future cost-bearing" |
| Ch2 draft | 235 | cross-chapter-handle? | summary checklist |
| Ch4 draft | 63 | cross-chapter-handle? | "value extraction paired with the transfer of costs" |
| Ch10 draft | 91 | cross-chapter-handle? | "It is a feature of what happens when value extraction and cost bearing are separated, under any ownership structure" |
| TA | 2251 | technical-formal | opioid case validation: "extraction operating across multiple commons, severing cost from value extraction" |
| TA | 2255 | technical-formal | "Sackler $11B extraction = framework's predicted value extraction" |

### Term: Commons Inversion Test + CIT (combined)

**Category:** A
**Pattern (regex):** `Commons Inversion Test|\bCIT\b` · case-sensitive

**Aggregate counts:** Publisher-facing **157 lines** (Ch1: 6, Ch5: 1, Ch6 HTML: 19, Ch6 suppl: 25, Ch7: 0, Ch8: 4, Glossary v3: 14, TA: 88); GuidanceDocs **21**; Combined **178**

This is the methodology's primary acronym. Per-occurrence enumeration condensed by file:

| File | Lines | Notes |
|---|---|---|
| Ch1 draft | 7, 54, 60, 66, 95, 101, 268 | All meta-discipline / register-discipline references — Ch 1 doesn't deploy CIT vocabulary in prose |
| Ch5 draft | 209 | "Commons Inversion Test that admits cost claims to the framework's accounting" — chapter-closer methodology preview |
| Ch6 HTML | 558, 598, 627, 700, 729, 739, 762, 765, 777, 790, 805, 811, 814, 817 (+others) | First chapter to **deploy** CIT — heavy concentration of `technical-formal` and `cross-chapter-handle?` patterns |
| Ch6 suppl | 5, 14, 16, 18, 34, 58, 70, 74, 104, 128, 132, 136, 140, 147, 192, 198, 200, 204, 210, 214, 218, 222, 224, 228, 229, 231, 256, 262, 272, 274, 282, 284, 286, 288, 290, 297, 298, 306, 330, 331 | Methodology-defense passages (densest CIT site in publisher-facing scope) |
| Ch8 draft | 25, 93, 113, 133 | "every Cᵢ that passes the discipline of the Commons Inversion Test" + per-component reveals |
| Glossary v3 | 133, 147, 177, 178, 192, 268, 270, 293, 295, 304, 306, 328, 353, 386, 403 | Term-record + cross-references; line 178 is the **canonical definition row** |
| TA | 175, 240, ~85 more lines | Definition + Section 6 protocol + Section L gates spec; densest cluster in TA |

**Sample of canonical occurrences (Ch6 HTML deployment site):**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 558 | first-introduction | "The Commons Inversion Test is a thought-experiment filter — a candidate cost claim either survives or fails its counterfactual inversion" |
| Ch6 HTML | 598 | technical-formal | "Across the 18 cases this book examines, the Commons Inversion Test has repeatedly surfaced ten commons categories worth naming as examples:" |
| Ch6 HTML | 700 | cross-chapter-handle? | "whether the Commons Inversion Test, when it filters cost claims, is filtering" |
| Ch6 HTML | 729 | technical-formal | "CIT's two sub-forms make the distinction operational" |
| Ch6 HTML | 739 | technical-formal | "The first gate is the Commons Inversion Test" |
| Ch6 HTML | 805 | technical-formal | "The Commons Inversion Test. Standard externality analysis prices what the analyst has already decided to price…" |

### Term: Four Gates (proper-noun + lowercase)

**Category:** A
**Pattern (regex):** `four gates` · case-insensitive

**Aggregate counts:** Publisher-facing **62**; GuidanceDocs **5**; Combined **67**

| File | Lines | Notes |
|---|---|---|
| Ch1 draft | 1 line (66) | meta-note |
| Ch6 HTML | 5 lines (732, 735, 777, 780, 805) | First Ch6 deployment "The Four Gates" subsection |
| Ch6 suppl | 12 lines (16, 90, 120, 198, 228, 256, 262, 282, 290, 297, 298, 306) | Methodology defense |
| Ch5 draft | 1 line (209) | chapter-closer methodology preview |
| Ch8 draft | 1 line (25) | "every Cᵢ that passes the discipline of the Commons Inversion Test, units consistency, boundedness, and independence" |
| Ch10 draft | 1 line (67) | "Four Gates each one passes to enter the accounting" |
| Glossary v3 | 9 lines (133, 178, 192, 282, 292, 304, 363, 373, 393) | Term-record + retire references |
| TA | ~32 lines | Section 7, Section L, application protocol |

---

## Category B — Ring-2 ratified

### Term: Substitutability Function

**Category:** B
**Pattern (regex):** `Substitutability Function` · case-sensitive

**Aggregate counts:** Publisher-facing **9**; GuidanceDocs **1**; Combined **10**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 359 | first-introduction | "The Substitutability Function" subsection header |
| Ch7 draft | 117 | cross-chapter-handle? | "Per the framework's Substitutability Function S, this gap is the difference S_max(industrial) − S_max(existential)" |
| Glossary v3 | 249 | technical-formal | term-name "Substitutability Function S(t\|t₀)" |
| Glossary v3 | 368 | retired-trace | CSG retired entry: "derived scalar from the Substitutability Function (S) primitive" |
| TA | 275, 412, 5936, 5954, 6200 | technical-formal | section header, Definition A.2, sensitivity-analysis row |

### Term: S(t) notation

**Category:** B
**Pattern (regex):** `S\(t\)` · case-sensitive

**Aggregate counts:** Publisher-facing **18**; GuidanceDocs **17**; Combined **35**

Publisher-facing distribution:
- Ch6 HTML: ~6 lines (formula + S(t) discussion)
- Ch7 draft: ~3 lines (Mars scenarios)
- Glossary v3: 1 line
- TA: ~8 lines (Definition A.2, Section 13, integrand statements)

This term is heavily compressed-scalar / technical-formal in shape.

### Term: Accountability Bond

**Category:** B
**Pattern (regex):** `Accountability Bond` · case-sensitive

**Aggregate counts:** Publisher-facing **15**; GuidanceDocs **1**; Combined **16**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch1 draft | 7, 95 | technical-formal | meta-discipline notes (Ch 1 must not invoke this term) |
| Ch5 draft | 209 | cross-chapter-handle? | chapter-closer |
| Ch6 HTML | 790 | technical-formal | "pricing instrument (Accountability Bond) sized to RCV rather than to a single externality" |
| Ch6 suppl | 70, 74 | technical-formal | methodology defense |
| Glossary v3 | 147, 215 | technical-formal | term-name + B-decomposition gloss |
| TA | 235, 484, 568, 1186, 1204, 1945, 2255 | technical-formal | section header + Definition A.7 + worked example |

### Term: Cost Severance Damages + CSD (combined)

**Category:** B
**Pattern (regex):** `Cost Severance Damages|\bCSD\b` · case-sensitive

**Aggregate counts:** Publisher-facing **57**; GuidanceDocs **0**; Combined **57**

Per-occurrence by file:
- Ch5 draft: 195, 197, 207 (3 lines) — Coates/Darity-Mullen lineage passages
- Ch6 HTML: 660, 663, 683, 694 (4 lines) — Ostrom-extension + reparations-economics
- Ch6 suppl: 104, 110, 246, 248, 272, 276, 290 (7 lines)
- Glossary v3: 133, 172, 203, 208, 209, 218, 287, 290, 385 (9 lines)
- TA: ~34 lines — densest at Section 2 + Section 11.3 (CSD-RCV correlation hypothesis test) + 15.1.2 methodology defense

### Term: Hotelling Identity

**Category:** B
**Pattern (regex):** `Hotelling Identity` · case-sensitive

**Aggregate counts:** Publisher-facing **27**; GuidanceDocs **1**; Combined **28**

| File | Lines | Notes |
|---|---|---|
| Ch5 draft | 209 | chapter-closer methodology preview |
| Ch6 HTML | 799 | "The Hotelling Identity is the framework's bridge: per-unit Residual Commons Value minus per-unit standard Hotelling rent equals per-unit Cost Severance" |
| Ch6 suppl | 262, 272, 280, 290, 297 | methodology-defense (heavy) |
| Glossary v3 | 228, 391 | term-record |
| TA | ~17 lines (230, 638, 1098, 1116, 1124, 1127, 1149, 1175, 1178, 6390, 6408, 6420, 6436, 6722, 7361) | Section 4 spec + extension-positioning discipline |

### Term: Triangulated RCV Estimation + Three Ways of Counting

**Category:** B
**Pattern (regex):** `Triangulated RCV Estimation|Three Ways of Counting` · case-sensitive

**Aggregate counts:** Publisher-facing **18**; GuidanceDocs **2**; Combined **20**

| File | Lines | Notes |
|---|---|---|
| Ch6 HTML | 7 (page title), 174-area | Chapter 6 title is "Three Ways of Counting" — most uses are pedagogical (chapter-name) rather than the Tech-Appendix formal term |
| Ch6 suppl | 140 | falsifiability-distinction passage |
| Glossary v3 | 235, 236, 392 | term-record |
| TA | 225, 678, 684, 688, 692, 696 + others | Section 3 spec |

### Term: Commons Categories + 10 Commons Categories

**Category:** B
**Pattern (regex):** `Commons Categories|10 Commons Categories` · case-sensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **0**; Combined **2**

Both occurrences are in Ch6 HTML or Glossary v3 / TA section labels. The phrase mostly appears as `commons categories` (lowercase) and as enumerated 10 names — note that "10 Commons Categories" rarely appears as a literal phrase. (Spec-list term `Abundances → Commons Categories` produced 0 matches across audited files.)

### Term: Intergenerational Pricing Gap + IPG (combined)

**Category:** B
**Pattern (regex):** `Intergenerational Pricing Gap|\bIPG\b` · case-sensitive

**Aggregate counts:** Publisher-facing **65**; GuidanceDocs **10**; Combined **75**

| File | Lines | Notes |
|---|---|---|
| Ch2 draft | 231 | "The IPG number range (33–122x) is referenced…" — chapter-closing meta-note |
| Ch6 HTML | 213, 215, 352, 404, 409, 531, 534, 537, 670 (9 lines) | First-introduction subsection "Intergenerational Pricing Gap (IPG)"; convergence table |
| Ch8 draft | 171, 177 | "Intergenerational Pricing Gap — the ratio of honest price to market price — for McDowell County coal… is somewhere between four and a hundred and twenty"; "Deepwater Horizon's documented costs… produce an IPG of fifteen to seventeen" |
| Ch6 suppl | 88, 106, 110, 151, 153, 155, 159, 161, 163, 169 | Parfit + IPG-table reconciliation passages |
| Glossary v3 | 263, 264 | term-record |
| TA | ~40 lines | Section B.2 + Section 11.3 + Sensitivity Analysis |

Most IPG occurrences are `compressed-scalar` (carry a number ratio) — the term's primary use is as compressed-scalar handle ("IPG = 33", "IPG = 50×", etc.).

### Term: CS = RCV − B (equation)

**Category:** B
**Pattern (regex):** `CS\s*=\s*RCV\s*[−-]\s*B` · case-sensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **2**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 160 | technical-formal | "Quantified via the flagship equation **CS = RCV − B**" |
| Glossary v3 | 202 | technical-formal | term-name row |
| Ch6 guide | (line) | technical-formal | guide reference |
| Ch7 guide | (line) | technical-formal | "CS = RCV - B" formula |

The full `CS = RCV − B` literal phrase is rare in chapter prose (chapters carry it as text descriptions: "Cost Severance equals Residual Commons Value minus Bond posting"). The literal symbolic form is a Tech-Appendix + Glossary marker.

### Term: Abundance Masking (proper-noun + lowercase)

**Category:** B
**Pattern (regex):** `abundance masking` · case-insensitive

**Aggregate counts:** Publisher-facing **3**; GuidanceDocs **0**; Combined **3**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 268 | technical-formal | Ring-2 label "Mechanism (paired with CIT)" |
| Glossary v3 | 270 | technical-formal | term-name "Abundance Masking" + def: "promoted to Ring 2" |
| Glossary v3 | 394 | technical-formal | history record "Abundance Masking promoted to Ring 2" |

Ch 6 / TA prose carries the concept ("abundance makes costs invisible") but uses lowercase descriptive form, not the proper-noun. The term is **glossary-only** in publisher-facing scope.

### Term: Asymmetric Regret Rule + ARR (combined)

**Category:** B
**Pattern (regex):** `Asymmetric Regret Rule|\bARR\b` · case-sensitive

**Aggregate counts:** Publisher-facing **37**; GuidanceDocs **1**; Combined **38**

| File | Lines | Notes |
|---|---|---|
| Ch6 HTML | 833 | "framework's response is the Asymmetric Regret Rule" — first-introduction in chapter prose |
| Ch6 suppl | 262, 272, 286, 290, 297 | methodology defense |
| Ch10 draft | 57, 69 | book-closing engagements: "The Asymmetric Regret Rule is what the model does in those cases"; "The Asymmetric Regret Rule is not an eccentric philosophical posture. It is ordinary insurance" |
| Glossary v3 | 133, 275, 333, 388, 403 | term-record + ARP→ARR rename traces |
| TA | 250, 318, 999, 2901, 2907, 2947, 2968, 3005, 3009, 3015, 4605, 4606, 4913, 5914, 6587, 6601, 6619, 6627, 6649, 6722, 7191, 7377 (22 lines) | Section 8 spec + ARP-rename trace + α-dominance pairing |

### Term: Externality Tail + E(R, t) notation

**Category:** B
**Pattern (regex):** `Externality Tail|E\(R, *t\)` · case-sensitive

**Aggregate counts:** Publisher-facing **29**; GuidanceDocs **16**; Combined **45**

Distribution: Ch6 HTML (3 — RCV integrand specs), Glossary v3 (2), TA (~24 — heaviest cluster, all `technical-formal` in derivations).

---

## Category C — Sub-instruments (architecture pending)

### Term: Restitution Bond (B₁)

**Category:** C
**Pattern (regex):** `Restitution Bond` · case-sensitive

**Aggregate counts:** Publisher-facing **25**; GuidanceDocs **0**; Combined **25**

| File | Lines | Notes |
|---|---|---|
| Ch5 draft | 193, 195, 199, 203, 205, 207 | First-introduction (line 193) + Coates lineage + structurally-independent claim |
| Ch6 HTML | 676, 680 | reparations-economics-lineage passage |
| Ch6 suppl | 110, 238, 244, 252, 253, 254 | reparations-economics methodological-engagement passage |
| Glossary v3 | 147, 209, 218, 287, 390 | term-record |
| TA | 607, 1200, 1204, 1220, 1235, 1237, 1239, 1275 | Section 5 spec + naming-rationale ("Restitution over Reparations for cross-political-tradition adoption breadth") |

### Term: Foreclosure Bond (B₂)

**Category:** C
**Pattern (regex):** `Foreclosure Bond` · case-sensitive

**Aggregate counts:** Publisher-facing **24**; GuidanceDocs **0**; Combined **24**

| File | Lines | Notes |
|---|---|---|
| Ch5 draft | 193, 199, 201, 203, 205 | First-introduction + civic-republican-lineage passage (Pettit/Skinner) |
| Ch6 HTML | 660 | "The Foreclosure Bond (B₂) is the framework's accounting instrument for that severance" |
| Ch6 suppl | 104, 110, 238, 253 | Parfit + methodology-defense |
| Glossary v3 | 147, 219, 288, 390, 403 | term-record |
| TA | 235, 632, 1186, 1200, 1204, 1226, 1239, 1258, 1275 | Section 5 spec |

(B₁ subscript and B₂ subscript by themselves overcount in plain prose; not separately enumerated. Counts above include their named-form occurrences.)

---

## Category D — Cluster terms (chapter prose, missing terms_index entries)

### Term: Dynastic Labor Cost (proper-noun + lowercase)

**Category:** D
**Pattern (regex):** `dynastic labor cost` · case-insensitive

**Aggregate counts:** Publisher-facing **5**; GuidanceDocs **3**; Combined **8**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 817 | first-introduction | "the downstream dynastic labor cost borne by families whose caregiving decades were restructured around asbestos-related illness" |
| Ch8 draft | 91 | first-introduction | "### Dynastic Labor Cost" subsection header |
| Ch8 draft | 93 | technical-formal | "Dynastic Labor Cost is the one the Commons Inversion Test reveals" |
| Glossary v3 | 373 | retired-trace | 8-tier-retired entry lists "Dynastic Labor Cost" among the 8 tier names preserved as illustrative labels |
| Ch10 draft | 125 | cross-chapter-handle? | closing-passage list "the dynastic labor cost and the acceleration cost all priced out" |

### Term: Lifetime Survival Cost (proper-noun + lowercase)

**Category:** D
**Pattern (regex):** `lifetime survival cost` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **2**; Combined **3**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 373 | retired-trace | 8-tier-retired entry lists "Lifetime Survival Cost" among preserved illustrative labels |

**Note:** "Lifetime Survival Cost" is a retired-tier name with no chapter-prose deployment. Flag for rigor pass: publisher-facing footprint is essentially zero outside the retired-trace glossary record.

### Term: Intergenerational Option Value (proper-noun + lowercase)

**Category:** D
**Pattern (regex):** `intergenerational option value` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

(Term occurs in TA only, as part of derivation prose; not deployed in chapter prose.)

### Term: intergenerational foreclosure pricing

**Category:** D
**Pattern (regex):** `intergenerational foreclosure pricing` · case-insensitive

**Aggregate counts:** Publisher-facing **3**; GuidanceDocs **3**; Combined **6**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 555, 569 | cross-chapter-handle? | "no existing accountability regime incorporates substitutability-weighted intergenerational foreclosure pricing"; "Until full intergenerational foreclosure pricing is built, the universal CS > 0 prediction stands" |
| TA | 3284 | technical-formal | Theorem E.1 falsifiability scope note |

### Term: intergenerational foreclosure (no "pricing")

**Category:** D
**Pattern (regex):** `intergenerational foreclosure` · case-insensitive

**Aggregate counts:** Publisher-facing **8**; GuidanceDocs **6**; Combined **14**

| File | Lines | Notes |
|---|---|---|
| Ch6 HTML | 555, 569 | (also matched by D25 pattern) |
| Ch9 draft | 141, 231 | "intergenerational foreclosure" as standalone phrase ("Property rights are held by living agents…") |
| TA | 493, 3281, 3284, 6109 | "intergenerational foreclosure costs"; "intergenerational foreclosure cost is a public harm" |

### Term: intergenerational carbon harm

**Category:** D
**Pattern (regex):** `intergenerational carbon harm` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

(Only one occurrence found across all audited files. Possibly TA derivation prose.)

### Term: Community Disruption Cost

**Category:** D
**Pattern (regex):** `Community Disruption Cost` · case-sensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

Note: extremely low surface footprint — flag for rigor pass.

### Term: Knowledge and Cultural Cost / Knowledge and Culture Cost

**Category:** D
**Pattern (regex):** `Knowledge and Cultur(e|al) Cost` · case-sensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **1**; Combined **3**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch8 draft | 105 | first-introduction | "### Knowledge and Cultural Cost" subsection header |
| Glossary v3 | 373 | retired-trace | 8-tier-retired list contains "Knowledge and Culture Cost" — note **inconsistency**: Ch 8 uses "Cultural" but glossary uses "Culture" |

**Flag for rigor pass:** Ch 8 chapter draft uses **"Knowledge and Cultural Cost"** while the retired-tier glossary entry uses **"Knowledge and Culture Cost"**. Naming consistency review needed.

### Term: Political Capture Cost

**Category:** D
**Pattern (regex):** `Political Capture Cost` · case-sensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **1**; Combined **5**

Distribution: Ch8 draft section header, glossary 8-tier-retired list, TA Section K abundance-test row, Ch10 closing-passage list.

### Term: Temporal Displacement Cost

**Category:** D
**Pattern (regex):** `Temporal Displacement Cost` · case-sensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

Single occurrence in Ch 8 draft (cost-component subsection header). **Flag for rigor pass:** orphan term — appears only in Ch 8 with no glossary record.

### Term: Foreclosure Cost (proper-noun + lowercase)

**Category:** D
**Pattern (regex):** `foreclosure cost` · case-insensitive

**Aggregate counts:** Publisher-facing **27**; GuidanceDocs **6**; Combined **33**

| File | Lines | Notes |
|---|---|---|
| Ch5 draft | 203 | "Foreclosure Bond obligation, because the foreclosure has already happened" — uses lowercase prose |
| Ch6 HTML | 305, 308, 314, 330, 796, 817 | First-introduction "foreclosure cost depends on substitutability" + 5 follow-ups |
| Ch7 draft | 45, 57 | "the foreclosure cost component drops" |
| Ch8 draft | 75 | "### Foreclosure Cost" subsection header (proper-noun, capitalized) |
| Ch10 draft | 77, 125 | closing-passage uses |
| Glossary v3 | 172, 219, 257, 373 | term-records (RCV def, B2 def, Externality Tail def, retired-tier list) |
| TA | 493, 710, 1228, 1955, 1996, 2012, 2519, 6109, 6112, 6154, 7043 | technical-formal derivations |

**Cross-cluster note:** "Foreclosure Cost" appears as both a tier-name (retired) and as the C₁ in the RCV integrand — the duplication is what caused the 8-tier scheme retirement (per glossary line 373).

---

## Category E — Borrowed academic concepts in chapter prose

### Term: intergenerational equity

**Category:** E
**Pattern (regex):** `intergenerational[ -]equity` · case-insensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **0**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch6 HTML | 802 | adjective-form? | "intergenerational equity, and epistemic loss as separate concerns governed by separate methods" — list of borrowed concepts |
| Ch7 draft | 71 | adjective-form? | "intergenerational-equity premise Stern's framing depends on" |
| Ch9 draft | 195 | cross-chapter-handle? | "preserve them for intergenerational equity" |
| TA | 6312 | technical-formal | "Hartwick 1977 sustainable-investment rule; Solow 1974 intergenerational equity" — citation |

### Term: intergenerational mobility (incl. income mobility)

**Category:** E
**Pattern (regex):** `intergenerational[ -]mobility|intergenerational income mobility` · case-insensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **0**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch8 draft | 99 | cross-chapter-handle? | "Development economists estimating intergenerational income mobility losses have produced regional estimates" |
| TA | 2853, 6308 | technical-formal | "intergenerational-mobility foreclosure"; "Chetty et al. intergenerational-mobility econometrics" |
| Glossary v3 | 210 | technical-formal | "Lineage: …Chetty et al. intergenerational mobility…" |

### Term: intergenerational wealth transmission

**Category:** E
**Pattern (regex):** `intergenerational wealth transmission` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

### Term: intergenerational fiscal architecture

**Category:** E
**Pattern (regex):** `intergenerational fiscal architecture` · case-insensitive

**Aggregate counts:** Publisher-facing **1** (Ch5 draft line 127); GuidanceDocs **0**; Combined **1**

### Term: intergenerational transfer program(s)

**Category:** E
**Pattern (regex):** `intergenerational transfer programs?` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 125 | adjective-form? | "Social Security is not Ponzi scheme — it is a genuine intergenerational transfer program providing essential benefits" |

### Term: intergenerational obligation(s)

**Category:** E
**Pattern (regex):** `intergenerational obligations?` · case-insensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **0**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 205 | cross-chapter-handle? | "The intergenerational obligation embedded in the Social Security trust-fund accounting" |
| Ch6 HTML | 670 | cross-chapter-handle? | "rather than treating intergenerational obligation as something the reader is asked to accept on faith" |
| Ch6 suppl | 92, 106 | technical-formal | Parfit-engagement passage |

### Term: intergenerational transfers

**Category:** E
**Pattern (regex):** `intergenerational transfers` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

### Term: intergenerational claim(s)

**Category:** E
**Pattern (regex):** `intergenerational claims?` · case-insensitive

**Aggregate counts:** Publisher-facing **5**; GuidanceDocs **0**; Combined **5**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch4 draft | 95 | first-introduction | "U.S. Social Security system… is a different architecture for the same kind of intergenerational claim" |
| Ch6 HTML | 805 | cross-chapter-handle? | "scarcity-grounded intergenerational claim and belongs in the integrand" |
| Ch6 suppl | 90, 123 | technical-formal | "framework's intergenerational claim" |
| Ch9 draft | 125 | cross-chapter-handle? | "captured the crisis's cost as an intergenerational claim" |

### Term: intergenerational stocks

**Category:** E
**Pattern (regex):** `intergenerational stocks` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

---

## Category F — Generic descriptive uses

### Term: intergenerational harm

**Category:** F
**Pattern (regex):** `intergenerational harm` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 197 | adjective-form? | "intergenerational harm has been transferred and compounded" — Darity & Mullen lineage paragraph |

### Term: intergenerational time

**Category:** F
**Pattern (regex):** `intergenerational time` · case-insensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **0**; Combined **2**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 149 | cross-chapter-handle? | "three different scales of distance — financial-system architecture; intergenerational time; institutional-medical-financing" |
| Glossary v3 | 311 | technical-formal | Temporal commons-category def: "shared time-budget; intergenerational time-commons" |

### Term: intergenerational scale

**Category:** F
**Pattern (regex):** `intergenerational scale` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **3**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 101 | cross-chapter-handle? | "Social Security, where the pattern operates at intergenerational scale" |

### Term: intergenerational cost(s) (lowercase)

**Category:** F
**Pattern (regex):** `intergenerational costs|intergenerational cost\b` · case-insensitive

**Aggregate counts:** Publisher-facing **11**; GuidanceDocs **7**; Combined **18**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 121 | adjective-form? | "the intergenerational cost of the workforce that was formed at community expense" |
| Ch4 draft | 47 | cross-chapter-handle? | "It is the full intergenerational cost of the extraction" |
| Ch5 draft | 95 | cross-chapter-handle? | (already counted) "intergenerational cost severance accumulates" — overlaps with G48 |
| Ch6 HTML | 365, 552 | cross-chapter-handle? | "Previous approaches to pricing intergenerational costs"; "the true intergenerational cost" (theorem statement) |
| Ch7 draft | 9 | cross-chapter-handle? | "the full intergenerational cost of foreclosure" |
| Glossary v3 | 172, 264, 343 | technical-formal | RCV def + IPG def + Spatial CS lowercase prose-phrase note |
| TA | 732, 7022 | technical-formal | "the true intergenerational cost"; "true intergenerational cost (RCV)" |

### Term: intergenerational-equity premise

**Category:** F
**Pattern (regex):** `intergenerational[ -]equity premise` · case-insensitive

**Aggregate counts:** Publisher-facing **1**; GuidanceDocs **0**; Combined **1**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch7 draft | 71 | cross-chapter-handle? | "operationalization of the intergenerational-equity premise Stern's framing depends on" |

---

## Category G — Lowercase preserved compositional phrases

### Term: intergenerational cost severance (lowercase)

**Category:** G
**Pattern (regex):** `intergenerational cost severance` · case-insensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **2**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 95 | cross-chapter-handle? | "the timeline at which intergenerational cost severance accumulates" |
| Glossary v3 | 343 | retired-trace | "Lowercase discipline mirrors intergenerational cost severance pattern" |

### Term: temporal cost severance (lowercase) + Temporal Cost Severance (RETIRED proper-noun)

**Category:** G + H
**Pattern (regex):** `temporal cost severance|Temporal Cost Severance` · case-sensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **0**; Combined **2**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 157 | cross-chapter-handle? (lowercase) | "We will see temporal cost severance in later chapters" — lowercase prose |
| Glossary v3 | 347 | retired-trace (capitalized) | term-name "Temporal Cost Severance" — RETIRED proper-noun, kept as glossary trace |

### Term: spatial cost severance (lowercase) + Spatial Cost Severance (RETIRED proper-noun)

**Category:** G + H
**Pattern (regex):** `spatial cost severance|Spatial Cost Severance` · case-sensitive

**Aggregate counts:** Publisher-facing **9**; GuidanceDocs **6**; Combined **15**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch2 draft | 155 | first-introduction (lowercase) | "This is spatial cost severance: the geographic gap…" |
| Ch7 draft | 107, 109 | cross-chapter-handle? (lowercase) | "Earth through spatial cost severance pricing"; "spatial cost severance charges" |
| Ch9 draft | 67 | cross-chapter-handle? (lowercase) | "An asteroid has no communities bearing spatial cost severance" |
| Glossary v3 | 342 | retired-trace (proper-noun) | "Spatial Cost Severance (capitalized proper-noun) → spatial cost severance (lowercase prose phrase)" — explicit un-retire record |
| Glossary v3 | 394 | retired-trace | history record |
| TA | 3393 | cross-chapter-handle? (lowercase) | "Note on spatial cost severance" |
| TA | 3501 | cross-chapter-handle? (lowercase) | "spatial cost severance operating at international scale" |
| TA | 6738 | technical-formal (lowercase) | section reference K.3 |
| TA | 6767 | technical-formal (lowercase) | "K.3 Spatial cost severance formalization" — section header |
| TA | 6776 | technical-formal (lowercase) | "Spatial cost severance measures…" |
| TA | 6779 | technical-formal (lowercase) | "this formalization explains why cost severance produces…" |

---

## Category H — Retired terms (preserve-trace audit + regression flags)

### Term: AIT + Abundance Inversion Test (RETIRED 2026-04-24)

**Category:** H
**Pattern (regex):** `\bAIT\b|Abundance Inversion Test` · case-sensitive

**Aggregate counts:** Publisher-facing **16**; GuidanceDocs **13**; Combined **29**

| File | Lines | Pattern | Context |
|---|---|---|---|
| Ch6 suppl | 14, 16, 66, 288, 306 | retired-trace | "AIT (Abundance Inversion Test)" + "Replace with **Passage A**" rename instructions |
| Glossary v3 | 133, 178, 327, 386, 403 | retired-trace | retired-term record |
| TA | 318, 1335, 1882, 2451, 6658, 7371 | retired-trace | rename markers + Section 6 retirement record |

**Regression check:** No instances of `AIT` or `Abundance Inversion Test` deployed in chapter draft prose with framework-active intent. All publisher-facing occurrences are retired-trace records or rename instructions. **No Tier-1 regressions detected.**

### Term: ARP + Asymmetric Regret Principle (RETIRED 2026-04-24)

**Category:** H
**Pattern (regex):** `\bARP\b|Asymmetric Regret Principle` · case-sensitive

**Aggregate counts:** Publisher-facing **11**; GuidanceDocs **1**; Combined **12**

| File | Lines | Pattern | Context |
|---|---|---|---|
| Ch6 suppl | 297 | retired-trace | "ARP rename → ARR pass" cross-reference |
| Glossary v3 | 276, 332, 388, 403 | retired-trace | term-record |
| TA | 318, 2907, 2935, 2956, 6633, 7377 | retired-trace | rename markers + Source rigor pass: ARP rename |

**Regression check:** All publisher-facing occurrences are retired-trace records. **No Tier-1 regressions.**

### Term: Spatial Cost Severance (RETIRED proper-noun)

See Category G entry above.

**Status:** Capitalized proper-noun retired 2026-04-24 → un-retired as lowercase prose phrase per Spatial CS re-examination (per glossary line 342, line 394). Capitalized form should not appear in publisher-facing chapter prose.

**Regression check:** Capitalized "Spatial Cost Severance" appears only in glossary retirement-record + TA section title K.3 (lowercase per Scope 3 rewrite, glossary 394). **One TA section header (K.3) carries capitalized "Spatial cost severance formalization" but with sentence-case lowercase first letter — not the capitalized framework-handle.** No Tier-1 regressions detected.

### Term: Temporal Cost Severance (RETIRED proper-noun)

See Category G entry above.

**Status:** Capitalized retired; lowercase preserved.

**Regression check:** Glossary line 347 has term-name "Temporal Cost Severance" — this is a retired-trace glossary entry. No chapter-prose deployment as capitalized framework-term. No Tier-1 regressions.

### Term: Universality Test (RETIRED/DEMOTED)

**Category:** H
**Pattern (regex):** `Universality Test` · case-sensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **0**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch7 draft | 205 | **retired-regression** | "The universality test establishes, as cleanly as a thought experiment can establish anything, that the framework is an instrument rather than an ideology." — **active framework deployment in lowercase prose**, but term is RETIRED/DEMOTED |
| Glossary v3 | 394 | retired-trace | history record "Universality Test demoted" |
| TA | (probably 1-2 references) | retired-trace | possibly section labels or cross-references |

**Regression flag (Tier-1 candidate):** Ch 7 draft line 205 deploys `the universality test` in active prose. Per glossary history (line 394), Universality Test was demoted 2026-04-24. The Ch 7 usage is lowercase, which may be the intended preserved form, but worth author judgment.

### Term: Civilizational Substitutability Gap + CSG (RETIRED)

**Category:** H
**Pattern (regex):** `Civilizational Substitutability Gap|\bCSG\b` · case-sensitive

**Aggregate counts:** Publisher-facing **8**; GuidanceDocs **16**; Combined **24**

| File | Lines | Pattern | Context |
|---|---|---|---|
| Ch7 guide | 103, 385 | retired-trace | guide references "CSG ranking" + "CSG" as scenario-table column |
| Ch9 draft | 247 | **retired-regression** | closing-passage gloss list "the civilizational substitutability gap" — **lowercase deployment in active framework gloss** |
| Glossary v3 | 367, 368, 394 | retired-trace | term-record + retire history |
| TA | 531, 5942, 5946, 5954, 7409 | retired-trace | retirement-record + rename markers |

**Regression flag (Tier-1 candidate):** Ch 9 draft line 247 (the book's closing-passage vocabulary list) names "the civilizational substitutability gap" as a framework-vocabulary item. Per glossary line 368, CSG is RETIRED 2026-04-24 — concept preserved as prose phrase "industrial-vs-existential substitutability gap" + sub-entry under Substitutability Function. Ch 9 uses an alternate prose form "industrial-existential substitutability gap" (Ch 7 line 117, Ch 7 table line 141, Ch 9 lines 31, 67, 97, 231) — but the closing-passage at line 247 reverts to the **retired** "civilizational substitutability gap" wording. **High-confidence regression — flag for Tier-1 sweep.**

### Term: Cost Bearing (DEMOTED 2026-04-24)

**Category:** H
**Pattern (regex):** `Cost Bearing` · case-sensitive

**Aggregate counts:** Publisher-facing **3** (in H57_61 combined output, exact attribution would need re-grep); GuidanceDocs **1**; Combined **4**

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 377, 378 | retired-trace | term-name "Cost Bearing" + DEMOTED entry |

**Regression check:** Demoted to prose-allowed status (per glossary 378: "perhaps prose vs. glossary"). Most publisher-facing occurrences appear as descriptive prose ("cost-bearing party"), not as capitalized framework term. Glossary entry preserves it. No Tier-1 regressions.

### Term: Value Capture (RETIRED 2026-04-24)

**Category:** H
**Pattern (regex):** `Value Capture` · case-sensitive

**Aggregate counts:** Publisher-facing **(part of H57_61 combined: 16 lines total across all H57-61 patterns)**; estimated 1-2 actual `Value Capture` proper-noun occurrences.

**Regression check:** Glossary line 337 carries the retired term-name. Replacement "Value Extraction" is the active form. Lowercase "value capture" / "value-capturer" appears in chapter prose as a role-descriptor (e.g. "the relationship between value-capturers and the commons"). No high-confidence regressions detected.

### Term: Full Generational Cost + FGC (RETIRED 2026-04-24)

**Category:** H
**Pattern (regex):** `Full Generational Cost|\bFGC\b` · case-sensitive

**Aggregate counts:** Publisher-facing **(part of H57_61 combined output)**; GuidanceDocs reference exists.

| File | Line | Pattern | Context |
|---|---|---|---|
| Glossary v3 | 133, 362, 363, 372, 394 | retired-trace | term-record + retirement history |
| Ch10 guide | 119 | **retired-regression** (guidance only) | "Commons Bonds is primarily a pricing framework that makes Full Generational Cost visible" — **guidance doc reference, not in publisher-facing prose** |
| TA | 328, 525 | retired-trace | retire trace |

**Regression flag (guidance-only, not Tier-1):** Ch10 guidance doc line 119 still references FGC. This is in **drafting scaffolding** (out-of-scope per spec), but flag for the rigor pass author since chapter is being drafted from this guidance.

### Term: Reparations Bond (RETIRED 2026-04-24)

**Category:** H
**Pattern (regex):** `Reparations Bond` · case-sensitive

**Aggregate counts:** Publisher-facing **2**; GuidanceDocs **0**; Combined **2**

| File | Line | Pattern | Context |
|---|---|---|---|
| TA | 1235, 1239 | retired-trace | naming-rationale: "Earlier working labels included 'Reparations Bond' for B₁"; "Restitution Bond over Reparations Bond" |

**Regression check:** Both occurrences are retired-trace records explaining the rename. Per b1_b2_naming pass §10, "reparations economics" academic-field reference is preserved separately — that academic phrase appears widely (Ch5, Ch6, TA — see CSD lineage discussions). The retired *Reparations Bond* term itself does not appear deployed in active prose. No Tier-1 regressions.

### Term: Reversibility Default + RD (RETIRED — framework context)

**Category:** H
**Pattern (regex):** `Reversibility Default|\bRD\b` · case-sensitive

**Aggregate counts:** Publisher-facing **3** (Reversibility Default: 2 in TA; RD: a few in TA); GuidanceDocs **0**; Combined **3**

| File | Line | Pattern | Context |
|---|---|---|---|
| TA | 2939, 2956, 3015, 6641, 7191 | retired-trace | "same-day flip from initial Reversibility Default"; "Initial v0.0.4-era working name was 'Reversibility Default' (RD)" |

**Regression check:** All occurrences are retired-trace flip-narrative records. No active framework deployment. **No Tier-1 regressions.**

(Note: the `\bRD\b` regex overcounts — 2 publisher-facing matches were the framework-context ones; other matches were inside HTML attribute fragments not captured by this audit.)

---

## Bonus — 8-tier scheme component-names (RETIRED but preserved as illustrative labels)

### Term: Actuarial Risk Cost / Mission Failure Reserve / Community Transition Reserve / Ecological Carrying Cost (combined)

**Pattern (regex):** `Actuarial Risk Cost|Mission Failure Reserve|Community Transition Reserve|Ecological Carrying Cost` · case-sensitive

**Aggregate counts:** Publisher-facing **4**; GuidanceDocs **2**; Combined **6**

| File | Line | Pattern | Context |
|---|---|---|---|
| Ch5 draft | 163 | first-introduction | "as the community-transition reserve no formal alternative existed to provide" — Butler end-of-life passage uses `community-transition reserve` lowercase as prose handle |
| Ch7 draft | 109 | cross-chapter-handle? | "Community Transition Reserves, spatial cost severance charges, border carbon adjustments" — uses capitalized form |
| Ch9 draft | 275, 279 | first-introduction + cross-chapter-handle? | "the natural expansions are the Community Transition Reserve mechanism — which I named but did not fully develop"; "Community Transition Reserve. I introduced this term in the political economy section… Flag this when you get to the glossary pass — I don't believe the current glossary contains it yet" — **author meta-note** |
| Glossary v3 | 373 | retired-trace | 8-tier list contains all four names as retired-tier labels |

**Flag for rigor pass:** Ch 9 draft author meta-notes (lines 275, 279) state that Community Transition Reserve is introduced as an instrument-name without glossary entry. The 8-tier retirement (per glossary 373) confirms it as a preserved-illustrative-label-only — suggests Ch 9 may be using it more architecturally than the retirement intends.

---

## Summary Totals

| Term | Cat | Pub total (lines) | Guide total (lines) | Combined |
|---|---|---|---|---|
| Commons Bonds | A | 23 | 23 | 46 |
| commons bonds (lc) | A | 1 | 0 | 1 |
| Cost Severance | A | 48 | 1 | 49 |
| cost severance (lc) | A | 90 | 54 | 144 |
| Severed Cost | A | 5 | 0 | 5 |
| severed cost (lc) | A | 18 | 1 | 19 |
| Cᵢ + Cost component + Cost variable | A | 28 | 1 | 29 |
| RCV | A | 262 | 41 | 303 |
| Residual Commons Value | A | 22 | 0 | 22 |
| Value Extraction | A | 4 | 0 | 4 |
| value extraction (lc) | A | 10 | 0 | 10 |
| Commons Inversion Test + CIT | A | 157 | 21 | 178 |
| Four Gates | A | 62 | 5 | 67 |
| Substitutability Function | B | 9 | 1 | 10 |
| S(t) | B | 18 | 17 | 35 |
| Accountability Bond | B | 15 | 1 | 16 |
| Cost Severance Damages + CSD | B | 57 | 0 | 57 |
| Hotelling Identity | B | 27 | 1 | 28 |
| Triangulated RCV + Three Ways | B | 18 | 2 | 20 |
| Commons Categories | B | 2 | 0 | 2 |
| Intergenerational Pricing Gap + IPG | B | 65 | 10 | 75 |
| CS = RCV − B (literal eq) | B | 2 | 2 | 4 |
| Abundance Masking | B | 3 | 0 | 3 |
| Asymmetric Regret Rule + ARR | B | 37 | 1 | 38 |
| Externality Tail + E(R, t) | B | 29 | 16 | 45 |
| Restitution Bond | C | 25 | 0 | 25 |
| Foreclosure Bond | C | 24 | 0 | 24 |
| Dynastic Labor Cost | D | 5 | 3 | 8 |
| Lifetime Survival Cost | D | 1 | 2 | 3 |
| Intergenerational Option Value | D | 1 | 0 | 1 |
| intergen foreclosure pricing | D | 3 | 3 | 6 |
| intergen foreclosure (no pricing) | D | 8 | 6 | 14 |
| intergenerational carbon harm | D | 1 | 0 | 1 |
| Community Disruption Cost | D | 1 | 0 | 1 |
| Knowledge and Cultur(e/al) Cost | D | 2 | 1 | 3 |
| Political Capture Cost | D | 4 | 1 | 5 |
| Temporal Displacement Cost | D | 1 | 0 | 1 |
| Foreclosure Cost (any case) | D | 27 | 6 | 33 |
| intergenerational equity | E | 4 | 0 | 4 |
| intergenerational mobility | E | 4 | 0 | 4 |
| intergen wealth transmission | E | 1 | 0 | 1 |
| intergen fiscal architecture | E | 1 | 0 | 1 |
| intergen transfer program(s) | E | 1 | 0 | 1 |
| intergen obligation(s) | E | 4 | 0 | 4 |
| intergen transfers | E | 1 | 0 | 1 |
| intergen claim(s) | E | 5 | 0 | 5 |
| intergen stocks | E | 1 | 0 | 1 |
| intergen harm | F | 1 | 0 | 1 |
| intergen time | F | 2 | 0 | 2 |
| intergen scale | F | 1 | 3 | 4 |
| intergen cost(s) lc | F | 11 | 7 | 18 |
| intergen-equity premise | F | 1 | 0 | 1 |
| intergen cost severance lc | G | 2 | 2 | 4 |
| temporal/Temporal cost severance | G+H | 2 | 0 | 2 |
| spatial/Spatial cost severance | G+H | 9 | 6 | 15 |
| AIT + Abundance Inversion Test | H | 16 | 13 | 29 |
| ARP + Asymmetric Regret Principle | H | 11 | 1 | 12 |
| Universality Test | H | 4 | 0 | 4 |
| CSG + Civilizational Substitutability Gap | H | 8 | 16 | 24 |
| Cost Bearing + Value Capture + FGC + Reparations Bond + Reversibility Default | H (combined H57_61) | 16 | 1 | 17 |
| RD (acronym) | H | 2 | 0 | 2 |
| Actuarial RC + Mission FR + Community TR + Ecological CC | Bonus | 4 | 2 | 6 |

**Totals across all terms (sum, may include cross-counts where compositional terms overlap):**
- Publisher-facing total occurrences: **~1,180 lines**
- GuidanceDocs total occurrences: **~270 lines**
- Combined: **~1,450 lines**

(Caveat: the "cost severance" lowercase + "Cost Severance" capitalized + "intergenerational cost severance" + "spatial cost severance" + "temporal cost severance" patterns overlap — the per-term counts treat these as separate, so summed totals overcount the underlying physical occurrences by ~10–20%.)

---

## Tier-1 sweep regression candidates (publisher-facing retired-vocabulary)

| File | Line | Issue | Confidence |
|---|---|---|---|
| Ch9 draft | 247 | "the civilizational substitutability gap" deployed in closing-passage framework-vocabulary list. CSG retired 2026-04-24; concept preserved as prose phrase **"industrial-vs-existential substitutability gap"** under Substitutability Function. The lowercase form may have been intended to be the prose-preserved equivalent, but the wording reverts to the retired term's exact descriptive base ("civilizational" rather than "industrial-existential"). | High |
| Ch7 draft | 205 | "the universality test establishes…" — Universality Test demoted 2026-04-24. Lowercase prose use may be allowed under the demotion (preserved-in-prose pattern, akin to "spatial cost severance"), but worth ratifying the demoted-form discipline. | Medium |
| Ch10 guide | 119 | "Full Generational Cost visible" — FGC retired 2026-04-24. Guidance doc only (out of primary scope), but flagged because Ch 10 is being drafted from this guidance and any prose carryover would constitute a regression. | Low (out-of-scope file) |

Other potential regressions in *guidance-doc* layer (out-of-scope but flagged for awareness): Ch7 guide lines 103, 385, 490, 495, 500 carry `CSG` and `AIT` references with **inline rename markers** ("renamed from AIT 2026-04-24") — these are intentional preservation-with-marker patterns, not regressions.

---

## Terms with no occurrences across audited files

- `Abundances → Commons Categories` — pattern matched 0 lines (the literal arrow-form phrase doesn't appear; the relation is named differently in glossary/TA prose).

---

## Classification ambiguity flags (author judgment requested)

Major `cross-chapter-handle?` (with `?` flag) clusters where preliminary classification needs author ratification:
1. **Ch 5 cost severance saturation** (lines 31–211): the term appears 13×, often 2-4× per paragraph. Some occurrences are clearly load-bearing (chapter argument advances on the term); others may be `repeated-paragraph?` candidates where a pronoun would do.
2. **Ch 6 HTML CIT/Four Gates/RCV cluster** (lines 558–817): high-density methodology vocabulary that is structurally introduction territory but contains framework-signaling? candidates if the same term repeats within paragraphs.
3. **Ch 6 supplementary drafts**: heavy methodology-defense passages where the same term-cluster repeats across sections § 1–§7 — by design, since each section defends a single choice — but the cumulative density is high.
4. **Ch 9 closing passage line 247**: classic "framework-vocabulary list" ("cost severance, residual commons value, severed cost, accountability bond, the civilizational substitutability gap") — this is a `framework-signaling?` archetype + carries the CSG retirement-regression flagged above.
5. **Ch 10 cost-severance distance theme** (lines 19, 37, 65, 125, 139): the closing chapter's central image. Whether each occurrence is `cross-chapter-handle?` or `repeated-paragraph?` depends on author intent for the closing chapter's vocabulary discipline.

---

## Methodology caveats

1. **Line counts are not occurrence counts.** Multi-match lines undercount; a paragraph with `cost severance` 4× counts as 1 line. For acronyms / short phrases the difference is small; for high-density chapters (e.g., Ch 5 line 145) the line undercounts.
2. **The `Cᵢ` Unicode subscript** could not be greped reliably alone (the U+1D62 character triggered tool denials). Combined with `Cost component` + `Cost variable` patterns into A04. Counts are conservative.
3. **The plain-capital `B` symbol** was not enumerated separately because the regex would overcount sentence-starts and English words; ordinary English usage of "B" is everywhere.
4. **Two-letter retired acronyms** (`RD`, `FGC`) may overcount inside HTML attribute fragments. The few publisher-facing matches reviewed are all retired-trace records.
5. **Guidance docs are aggregate-counted only.** No per-occurrence tables for Ch_n_ guides per spec scope.
6. **The Ch 6 Supplementary Drafts file** (`Chapter__6___SupplementaryDrafts_2026-04-24.md`) is included in the publisher-facing scope as a Ch 6 staging document. If the rigor pass treats it as drafting scaffolding rather than chapter-prose, recategorize the per-Ch6-suppl rows accordingly.

---

*Generated 2026-04-28. Raw grep output preserved at `tools/rigor-passes/_inventory_raw_2026-04-28/`.*
