# Commons Bonds — Term Provenance Index

**Version:** 1.0.0 (current-state document; established 2026-04-24 as v0.1.0 skeleton; bumped to v1.0.0 2026-04-30 per refined Working Principle #4 — Insight #59)
**Purpose:** current-state registry of framework vocabulary — rigor support, dependency tracking, staleness triggers, versioning — replacing prior "canonical" claims that masked the testing-dependent nature of every term.

**Retirement-trace discipline (per refined WP#4 + Insight #59 ratified 2026-04-30):** v1.0.0+ carries summary-level retirement traces (skeleton form: status + supersession + 1-sentence why + archive pointer). Full traces — multi-paragraph history, full rigor-provenance, sweep targets, commit trails — live at `archive/retirements/index.md` (canonical retirement-archive) plus the ratifying rigor pass for each retirement event. This bumps terms_index from skeleton-with-full-traces (v0.1.0) to current-state-document-with-summary-traces (v1.0.0).

---

## §0. Why this index exists

The framework's prior vocabulary discipline used words like *canonical*, *locked*, and *final* to mark terms as settled. Those claims hid the fact that every framework term rests on specific testing-suite decisions that can and do change when the suite finds issues with upstream or downstream elements.

Today's three rigor passes demonstrated the stakes:

- **Path F rigor pass (2026-04-24)** reframed the 10 abundances from "canonical taxonomy" to "variables AIT has discovered." A word previously used as a truth-claim ("canonical") became inaccurate.
- **Tier-reframing rigor pass (2026-04-24)** exposed the v10 tier schema as a mis-labeled variable list. The "Canonical v10" label it carried was not reflecting reality — the schema failed under its own weight on a duplication check.
- **Macro-grouping rigor pass (2026-04-24)** would have produced an attractive but harmful "canonical macro-category" layer if the rigor had not caught the abstraction-hides-severance concern.

A system that called any of these "canonical" at the time would have masked the dependencies that later testing exposed. The Term Provenance Index replaces truth-claim language with traceable-reasoning discipline: every term carries the rigor that supports it, the decisions it depends on, and the triggers that would require re-testing.

## §1. How to read a record

Each term has a Provenance Record with the following fields:

### Template

```markdown
### <Term>

**Working definition:** <current definition — no claim of finality>

**Status:** <CURRENT | PENDING-RIGOR | UNDER-REVIEW | SUPERSEDED | RETIRED>

**Term-spec version:** v<N.M>

**Last reviewed:** <YYYY-MM-DD>

**Rigor provenance:**
- <Rigor pass filename / version / §ref / date / commit> — <what that pass established about this term>
- <Additional rigor passes, session handoffs, or ratified decisions>

**Depends on (framework decisions this term rests on):**
- <Decision 1> — <brief description>
- <Decision 2>

**Staleness triggers (what would require re-review):**
- <Upstream change 1>
- <Upstream change 2>

**Commit trail:** <most relevant commit refs>

**Supersedes / superseded by:** <if applicable>

**Notes:** <optional — any caveats, pending questions, or edge cases>
```

### Status indicators

| Status | Meaning |
|---|---|
| `CURRENT` | In active use; has passed applicable rigor; no known staleness. |
| `PENDING-RIGOR` | Introduced but not yet rigor-tested; use at own risk until pass runs. |
| `UNDER-REVIEW` | Rigor pass in progress; term may be revised or retired when pass ratifies. |
| `SUPERSEDED` | Replaced by newer term; preserved for historical reference with pointer to replacement. |
| `RETIRED` | Dropped without replacement (e.g., dissolved concepts). |
| `DEMOTED` | Concept persists in prose but no longer carries proper-noun framework-term status (glossary entry removed; chapter-prose use continues). |

**Critical property:** no status claims truth. `CURRENT` means "this survives our most recent applicable rigor." It does not mean "this is correct." Framework decisions are always downstream of rigor testing, which is always subject to new pressure.

### Retired / superseded / demoted entry template (skeleton form, v1.0.0+)

Per refined Working Principle #4 (Insight #59 ratified 2026-04-30), retired/superseded/demoted entries use a skeleton form rather than full inline trace. Full traces live in `archive/retirements/index.md` + the ratifying rigor pass.

```markdown
### <Term>

**Status:** RETIRED|SUPERSEDED|DEMOTED YYYY-MM-DD (Insight #N). <Replaced by | Demoted from glossary; concept persists as prose | etc.>
**Why:** <one sentence — the rigor-level rationale, not the narrative>.
**Full trace:** `archive/retirements/index.md` §<N> + <ratifying rigor pass path>.
```

Skeleton entries may add a single `**Notes:**` line if structurally load-bearing (e.g., diagnostic originated here; cross-cutting reuse). Multi-paragraph narratives, full rigor-provenance lists, sweep-target catalogs, and commit trails belong in the archive index + rigor pass, not here.

### Staleness detection

Each record lists *dependencies* and *staleness triggers* explicitly. When an upstream framework decision changes (tracked by rigor-pass commit or handoff ratification), records whose dependencies reference the changed decision are flipped to `UNDER-REVIEW` and queued for re-testing. The discipline: every rigor-pass ratification ends with a terms-index impact assessment — which records flip to `UNDER-REVIEW`, which are confirmed still `CURRENT`.

### Versioning

Each term carries its own `term-spec version` independent of document versions. When a term's definition or status changes materially (rigor re-test flips verdict, supersession, retirement), the term-spec bumps (v1.0 → v2.0). When re-confirmed with minor clarification, patch bumps (v1.0 → v1.1). Readers can spot stale terms at a glance: if a term's provenance lists v3.0 as the current spec but a chapter draft reflects v1.0 vocabulary, the staleness is visible.

## §2. Integration with other framework docs

- **Glossary (`core/glossary/commons_bonds_updated_glossary_v4.html`)** carries short gloss entries derived from this index per S1 schema (alphabetical-vocabulary body + trailing Architecture + Commons-categories + Retired/Superseded sections). Glossary is the user-facing lookup; this index is the provenance source-of-truth.
- **Technical Appendix (`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`)** carries formal definitions + theorem framework. v2.0.0 rebuild landed 2026-05-02 via Phase α.2 (batched all Phase 2 + Group 1 ratifications: theorem restructures 10.1a + 10.1b + 10.2 (Empirical Observation, formerly E.2) + 10.3 + 10.4 + 10.5 + Corollary 10.5.1 (numbering canonicalized to single numeric scheme 2026-05-11; prior letter labels were E.X); §15.2 methodological framing footnotes; notation discipline α → ξ + τ → u + C → 𝒞; mathematical apparatus + Q-stock convention + scarcity multiplier motivation + Externality Tail + RCV acronym disambiguation; B₁/B₂ formal definitions in §5; content absorption from `core/dimensions/`; comprehensive WP#8 + WP#10 scaffolding-scrub; §18 Bibliography). Glossary v4 rebuild (Phase α.3) follows.
- **Retirement archive (`archive/retirements/index.md`)** is the canonical retirement-archive established 2026-04-30 by Insight #59. Full traces of every retirement event live there + in the ratifying rigor pass. This index carries summary-level traces only (skeleton form per §1 template).
- **Rigor passes** produce provenance records as their primary deliverable. When a pass ratifies, it updates affected records in this index. Rigor passes themselves remain canonical decision-record (frozen by date in filename).
- **Working principles + vocabulary strategy** (`alignment/commons_bonds_working_principles_v1.0.0.md` + `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md`) carry light retirement traces with cross-reference to the archive index per refined WP#4.
- **Layer classification (per WP#10 ratified 2026-04-30):** terms_index is INTERNAL scaffolding — rich per its layer. Three principles coordinate the internal/external axis: WP#4 (refined) governs retirement-time discipline; WP#8 governs scrubbing-time discipline (publisher-facing artifacts scrubbed of audit-trail content); WP#10 governs origination-time discipline (classify new content as internal or external before generating it). Rendering-field drafts in entries here (Glossary def, Tech Appendix def) are internal scaffolding that FEEDS external rebuilds (Phase α.2 Tech Appendix v2.0.0 + Phase α.3 Glossary v4) per WP#10 §4.3 cross-layer flow.
- **Session handoffs** reference this index's current state rather than repeating "canonical" summaries.
- **README** canonical-state table links to relevant provenance records.

## §3. Current-state snapshot

This section gives readers a one-screen orientation to the framework's current vocabulary state. Full per-term records live in §4. Retirement traces are skeleton-form per §1; full traces live in `archive/retirements/index.md`.

### Ring-1 (7 terms — framework architecture; ratified 2026-04-24)

- **Commons Bonds** (framework name + book title)
- **Cost Severance** (mechanism)
- **Severed Cost** (result + flagship adoption phrase)
- **Value Extraction** (causal event; supersedes Value Capture)
- **Commons Inversion Test (CIT)** (methodology + Gate 1 of Four Gates Admission Apparatus, §7.1; supersedes AIT 2026-04-24)
- **Residual Commons Value (RCV)** (quantification-anchor + equation component)
- **Cost (Cᵢ)** (atomic unit; admitted via Four Gates)

### Ring-2 (mechanism + measurement + sub-instruments)

Mechanism / measurement / equation: Abundance Masking · Substitutability Function (S) · Externality Tail (E) · Intergenerational Pricing Gap (IPG) · CS = RCV − B equation · Cost Severance Damages (CSD) · Hotelling Identity · Three Ways of Counting (formerly Triangulated RCV Estimation; Insight #31 2026-04-28) · Intergenerational Option Value (Tier B promotion 2026-04-30 per Insight #57).

Accountability instruments: Accountability Bond (B) = Restitution Bond (B₁) + Foreclosure Bond (B₂).

Decision rule: Asymmetric Regret Rule (ARR; supersedes ARP).

Cost-component examples (Cᵢ illustrative-list; class is open per Path F): Foreclosure Cost · Lineage Labor Cost (renamed from Dynastic Labor Cost 2026-04-30 per Insight #56) · Community Disruption Cost · Knowledge and Cultural Cost · Political Capture Cost · Lifetime Survival Cost · Actuarial Risk Cost · Mission Failure Reserve · Community Transition Reserve · Ecological Carrying Cost.

### Lowercase prose phrases (subtype descriptors; not capitalized framework terms)

intergenerational cost severance · spatial cost severance.

### Retired / superseded / demoted (full traces in `archive/retirements/index.md`)

Abundance Inversion Test (AIT) · Asymmetric Regret Principle (ARP) · Reversibility Default (RD; same-day flip) · Civilizational Substitutability Gap (CSG; demoted to descriptive prose) · Universality Test (demoted) · Cost Bearing (demoted) · Value Capture · Temporal Cost Severance · Spatial Cost Severance proper-noun (un-retired as lowercase prose phrase; see entry) · Full Generational Cost (FGC) · 8-tier decomposition scheme · "Reparations Bond" working label (renamed to Restitution Bond) · "Resource-Foreclosure Bond" working label (renamed to Foreclosure Bond) · industrial-existential substitutability gap · Knowledge and Culture Cost (renamed to Knowledge and Cultural Cost) · Dynastic Labor Cost (renamed to Lineage Labor Cost).

---

## §4. Established records

*(Records below are populated as rigor passes land. Each record's body summarizes the pass's verdict; full pass documents live at `tools/rigor-passes/`.)*

---

### Commons Bonds

**Working definition:** the framework's identifying name and the book's title. Polysemous compound naming three simultaneously-operating meanings: (1) **accountability bonds** — the formal instrument B in CS = RCV − B (reclamation bonds, performance bonds, community-transition reserves); (2) **relational bonds** — intergenerational duty, community-place attachment, labor solidarity, and other human-and-ecological bonds that cost severance breaks; (3) **structural bonds** — ecosystem interdependencies, atmospheric stability, economic interconnections that cost severance frays. All three meanings operate simultaneously in the book; contexts disambiguate.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, batch ratification with standalone + integrated rigor).

**Glossary definition (~80 words, reader-register):**
> The framework's identifying name and the book's title. The phrase carries three meanings working at once: the formal **accountability bonds** that would close the gap between what extraction costs and what extractors pay; the **relational bonds** between people, generations, and place that extraction without accountability frays; and the **structural bonds** of ecosystems and economies that hold what we share. The book's central question is how to keep all three intact.

**Tech Appendix definition (~300 words, formal + lineage):**
> The framework's identifying name. *Commons Bonds* is a polysemous compound naming three simultaneously-operating meanings, each load-bearing for the framework's argument:
>
> (1) **Accountability bonds** — the formal pricing instrument B in the framework's primitive equation CS = RCV − B. The instrument cluster includes reclamation bonds (Surface Mining Control and Reclamation Act 1977), Environmental Impact Bonds (Balboa 2016), Pigouvian-tax mechanisms (Pigou 1920), sovereign wealth funds operationalizing the Hartwick rule (Hartwick 1977), and decommissioning reserves. Decomposed in Ring 2 as B = B₁ + B₂ where B₁ is the Restitution Bond (backward-looking; reparations-economics lineage per Darity & Mullen 2020) and B₂ is the Foreclosure Bond (forward-looking; option-value + Hartwick-rule lineage).
>
> (2) **Relational bonds** — intergenerational duty (per Parfit 1984 *Reasons and Persons* Part IV impersonal-outcomes evaluation), community-place attachment (per Anderson 2017 *Private Government*; Klinenberg 2018 *Palaces for the People*), labor solidarity, kinship obligations, and other human-and-ecological bonds that cost severance breaks. The framework's RCV calculation prices what these bonds were worth when extraction severed them.
>
> (3) **Structural bonds** — ecosystem interdependencies (commons-governance per Ostrom 1990 *Governing the Commons*; Hess & Ostrom 2007), atmospheric stability (carbon-stability commons priced via DAC three-horizon and Social Cost of Carbon), economic interconnections, and physical commons whose continued availability the framework's foreclosure-cost component prices.
>
> All three meanings operate simultaneously throughout the book; chapter context disambiguates which is foregrounded. Polysemy is load-bearing, not loose: the framework's structural claim is that the three meanings are mechanistically linked — accountability-bond posting B is what would close the gap that severs relational + structural bonds, and the framework's measurement methodology (CIT + Three Ways + Four Gates) operates across all three.

**Term-spec version:** v1.0 (first sanctioned spec after dedicated rigor pass).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Commons Bonds standalone rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_commons_bonds_v1.0.0.md` (2026-04-24) §9 — Option A PASSES extreme rigor unconditionally. Polysemy confirmed as load-bearing (each of 3 meanings does framework work). 7 rename candidates tested; none improves.
- Full Ring-1 integrated rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_ring1_full_integrated_v1.0.0.md` (2026-04-24) §7 — Commons Bonds pairs coherently with every other Ring-1 term (21 pairings verified).
- Open Insight #4 (Commons Bonds name rigor) RESOLVED by these two passes.

**Polysemy per meaning, load-bearing verification:**
- Accountability bonds (Meaning #1): direct link to CS = RCV − B formula where B is the accountability bond.
- Relational bonds (Meaning #2): Ch 1's 120-hour-week thread, Ch 7's Mars habitat bonds, Ch 10's closing reflection.
- Structural bonds (Meaning #3): ecosystem cases (Chesapeake, McDowell watersheds), atmospheric/climate stability, economic-community interdependencies.

**Role:** framework identifier + book title; umbrella under which all Ring-1 terms live.

**Depends on:** every Ring-1 term (title only name-works if the framework it names is coherent): Cost Severance + Severed Cost + Value Extraction + CIT + RCV + Cost (Cᵢ).

**Staleness triggers:**
- Framework scope changes materially (e.g., non-commons extraction becomes primary).
- One of the three meanings becomes obsolete.
- Adoption evidence after publication shows title failing to travel.

**Commit trail:**
- Standalone rigor pass: commit `be6646f` (2026-04-24).
- Full Ring-1 integrated pass: commit `d4c4be4` (2026-04-24).
- Batch ratification: this commit.

**Supersedes / superseded by:** N/A — retention. First-ever rigor pass on the name.

**Notes:**
- Subtitle choice is author's call + publisher convention; rigor-neutral. Examples discussed in standalone pass §9.1.
- Polysemy is asset, not liability. Parallel: "capital" in economics has multiple meanings (financial, human, social, political); context disambiguates; no one calls that imprecision.

---

### Cost Severance

**Working definition:** the structural mechanism by which extraction separates value capture from cost bearing. The process/mechanism noun that names the framework's core phenomenon. Middle position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.* **Specialization (not contradiction) of the familiar employment-severance concept** — inverted to describe the relationship between value-capturers and the commons they draw from (per M12 audit 2026-04-24 + Option C rhetorical-bridge ratification; canonical Ch 1 framing established).

**Status:** `CURRENT` at Ring 1 (Ring-1 synthesis batch ratified 2026-04-24 by Chris Winn; M12 collision audit + Option C ratified 2026-04-24 by Chris Winn).

**Glossary definition (~80 words, reader-register):**
> The mechanism by which extraction separates value capture from cost bearing. When a company extracts value from a commons — a community, an ecosystem, a future generation — and the costs of that extraction stay with the source rather than the extractor, the result is **cost severance**. The framework's term builds on the familiar idea of employment severance, where a company that sheds a worker pays that worker for the cut tie. Cost severance is the same logic applied to commons extraction — except the payment architecture is missing.

**Tech Appendix definition (~310 words, formal + lineage):**
> The structural mechanism by which extraction separates value capture from cost bearing. Cost Severance is the framework's process/mechanism noun naming the central phenomenon the framework measures and prices. Middle position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost* (where Severed Cost is the result/quantity companion noun).
>
> Formal expression in the framework's primitive equation:
>
> **CS(R, t₀) = RCV(R, t₀) − B(R, t₀)**
>
> where CS is per-unit Cost Severance for resource R extracted at time t₀, RCV is the per-unit Residual Commons Value (the full intergenerational cost; integral of substitutability-weighted foreclosure cost plus externality tail across all future time), and B is the per-unit Accountability Bond posting (the actual instrument value capturing rents and committing them to closing the gap). CS &gt; 0 indicates extraction is underpriced under the current accountability regime; CS &asymp; 0 indicates the bond approximates the true intergenerational cost; CS theoretically can be negative under fully-bonded sustainable management.
>
> M12 lineage: specialization (not contradiction) of the familiar employment-severance concept. In employment, severance is the payment a value-capturer (employer) makes when severing the tie with a cost-bearer (worker). The framework inverts the direction: under cost severance, the value-capturer (extractor) sheds costs onto the source (commons) without compensating for the severing. The Ch 1 rhetorical bridge recruits the reader's existing employment-severance schema as on-ramp; subsequent chapters use the term cleanly without defensive disambiguation. Cost Severance is the framework's most-used mechanism term. Aggregate at scale: cumulative cost severance across all Earth-bound extraction since the industrial revolution exceeds, by every available estimate, the cumulative wages paid for the extraction labor by orders of magnitude.

**Term-spec version:** v1.1 (v1.0 was Ring-1 synthesis ratification; v1.1 adds M12 finding + Option C rhetorical-bridge ratification + Ch 1 canonical framing).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-addability rigor pass (2026-04-24) — CORE mechanism preserved under Path F generalization.
- Tier-reframing + macro-grouping passes (2026-04-24) — mechanism preserved under all ratified framework changes.
- CS-vs-SC triage rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_cost_severance_vs_severed_cost_v1.0.0.md` (2026-04-24) §17 — Option A (keep both Cost Severance + Severed Cost with role discipline) PASSES extreme rigor.
- Ring-1 synthesis pass (2026-04-24) — verdict reinforced; CS = RCV − B equation integration verified.
- **M12 collision rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_cost_severance_collision_v1.0.0.md` (2026-04-24)** — tested semantic collision with HR/accounting "severance costs" (IAS 37, US GAAP, Big-4 firms, corporate-law practice). Classification: lexical collision, different concept, HIGH severity for legal/accounting audience. **Option C (rhetorical bridge) ratified 2026-04-24 by Chris Winn** — the collision is converted into a Ch 1 teaching move that recruits reader's existing HR-severance schema as on-ramp ("THIS IS the same move, applied differently"). Option B (rename) tested 6 candidates including Accountability Severance as strongest; all rejected. First application of M12 as primary driver in a rigor pass; established rhetorical-bridge as Level 5 on M12 action ladder.
- **Phase 2 deeper-dive rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md` (2026-04-29)** — full 12-cell multi-audience matrix per vocabulary strategy v1.0.1 §2 + §8 + M6 academic rigor depth audit + M11 critic-survival from 5 critic positions + M12 attribution-honesty depth audit + Ch 1 Option C bridge plan verification at Tier 2d depth. **Verdict: KEEP terms (PASS conditional on three enhancements) — RATIFIED 2026-04-29 by Chris Winn.** No cell FAILS. Tier 2a + Tier 2d + Lived-oppression conditional STRONG-with-enhancement. Rename rejected (6 alternatives tested; none dominates). Three enhancements ratified: (a) lineage citation expansion (this update); (b) Ch 1 Option C bridge prose extension to three registers (labor + severance-tax + colonial; canonical text below); (c) Tech Appendix §L methodological footnote on commodification + decolonial framing (placement: NOW vs Phase 3 Tech Appendix v2.0.0 rebuild — pending author choice on §12.3 of Phase 2 rigor pass).

**Cross-political-tradition lineage (Phase 2 expansion 2026-04-29):**
- *Decolonial / lived-oppression / Tier 2d* — Coulthard 2014 *Red Skin, White Masks* (severance-as-colonial-cutting); Tuck & Yang 2012 "Decolonization is not a metaphor" (severance of land from people); Whyte (indigenous environmental ethics; severance of ancestral kinship); Wolfe 1999 *Settler Colonialism* (logic of elimination); Patel & Moore 2017 *A History of the World in Seven Cheap Things* (capitalist severance of nature/work/care/lives); Federici 2004 *Caliban and the Witch* (primitive accumulation as severance of reproductive labor); Hickel 2020 *Less Is More* + *The Divide* (colonial extraction; Global South cost-severance).
- *Reparations economics / dollar-quantification of historic injustice* — Darity & Mullen 2020 *From Here to Equality* (dollar quantification specifically because demanding atonement without numbers lets establishment dismiss the claim).
- *Black radical tradition / existential-rupture* — DuBois *Souls of Black Folk* (double-consciousness as severance); Robinson *Black Marxism*; Wilderson *Afropessimism* (anti-Black ontological severance).
- *Civic-republican* — Anderson 2017 *Private Government* (severance of civic standing in workplace); Pettit 1997 *Republicanism* (non-domination violations).
- *Marxist / socialist* — Marx *Capital* Vol. 1 (severance of labor from product; structurally analogous, conceptually distinct from framework's severance-of-cost-from-value-capture).
- *Classical-liberal / property-law* — Demsetz 1967 "Toward a Theory of Property Rights"; Coase 1960 "The Problem of Social Cost" (severance-context-specific cite); Hayek 1960 *The Constitution of Liberty*.
- *Legal/policy adoption-travel anchor (Tier 2b)* — US severance-tax law (state statutes: Texas Tax Code Title 2 Subtitle I; Alaska AS 43.55; Wyoming Statutes Title 39 Ch 14; North Dakota Century Code Ch 57-51; Montana Code Annotated Title 15 Ch 36; ~36 states levy severance taxes on natural-resource extraction). Severance-tax precedent is the existing US legal vocabulary that comes closest to what Cost Severance Damages + Restitution Bond + Foreclosure Bond architecture extends.

**Role discipline:** Cost Severance is the *process/mechanism noun*. Use when naming the mechanism, describing how the phenomenon operates, or in theoretical discussion. *"McDowell suffers cost severance."* *"Cost severance operates through..."* Lexical slot: subject of analytical sentences about mechanism operation. Companion term: Severed Cost for result/quantity naming (see separate record).

**Usage audit:** 227 occurrences in 36 files as of 2026-04-24 — framework's most-used mechanism term.

**Depends on:**
- Value Extraction (causal event that triggers the mechanism — Ring 1)
- Severed Cost (result-side companion — Ring 1)
- RCV (quantification that measures the mechanism's output — Ring 1)
- CS = RCV − B equation (Cost Severance appears as "CS" in the equation)
- CIT (methodology for identifying costs within the mechanism's scope)

**Staleness triggers:**
- Framework CORE math redefines the CS = RCV − B relation.
- Academic adoption evidence shows "cost severance" failing to travel.
- Role-discipline slippage where prose blurs CS (mechanism) with SC (result).

**Commit trail:**
- CS-vs-SC rigor pass: commit `0021e24` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A — retained under triage.

**Notes:**
- Pair with Severed Cost is grammatical complementarity (process noun vs result noun), NOT duplication. Standard economics convention (externality vs externality cost; rent-seeking vs rent).
- Style-discipline per CS-vs-SC rigor pass: use Cost Severance when naming the mechanism; use Severed Cost when quantifying specific instances.
- **M12 bridge-commitment discipline (ratified 2026-04-24; extended 2026-04-29 per Phase 2):** Ch 1 opening leans into the multi-register strength of *severance* as rhetorical bridge — labor-severance + severance-tax + colonial-severance — recruiting the reader's existing schema as on-ramp across multiple traditions simultaneously. Post-Ch-1 chapters use "Cost Severance" cleanly without defensive "not to be confused with..." language. Bridge does its work once; chapters trust it. If Ch 1 drafting reveals the bridge is authorially unsustainable, fallback to Option A (explicit disambiguation). Do NOT fallback to Option B (rename) unless both C and A attempts fail.
- **Canonical Ch 1 framing (RATIFIED 2026-04-29 v2 — three-register extended version per Phase 2 §7.4; supersedes the single-register 2026-04-24 v1 below):**
  > *"Corporate America knows the word 'severance.' When a company sheds workers to cut costs, we pay the severed employee — severance — and call it a cost of doing business. The word honors something: when you cut someone loose, you owe them. You sever the tie, and you pay for the severing.*
  >
  > *American tax law knows the word too. In thirty-six states, when oil or gas or minerals or timber is severed from the land — extracted — we pay a* severance tax*. The state honors something: when a public-trust resource is cut loose from its source, the source is owed payment. We sever the resource, and we pay for the severing.*
  >
  > *And before American tax law knew the word, the histories of indigenous peoples on every continent knew it more painfully. Land was severed from peoples; generations were severed from inherited governance; rivers were severed from those who lived alongside them. The severing was real; the payment was almost never made.*
  >
  > *Cost severance is the framework's name for the same structural move — applied to the relationship between value-capturers and the commons they draw from — and to the question that flows from all three of these registers: when something is severed, who pays for the severing? The book's argument is that markets systematically perform the severance and systematically fail to pay for it. The cost-bearer — the community, the ecosystem, the future generation — gets stuck with what was severed onto them. That's the problem this book is about."*

  **Bridge prose status:** v2 DRAFT in Claude's voice (Phase 2 §7.4 ratification 2026-04-29); awaits Chris's voice refinement during the Ch 1 + Ch 2 conversational drafting session (deferred per author direction 2026-04-29 — to follow scaffolding-vs-publisher-facing separation pass + word-count recompute). Verdict at Phase 2 depth on the bridge is "PLAN HOLDS conditionally pending execution + enhancement" — execution = Chris drafting Ch 1 to 5K-6K target with the v2 bridge prose landed at appropriate placement.

- **Canonical Ch 1 framing v1 (2026-04-24 — single labor-register version, SUPERSEDED 2026-04-29 by v2 above; preserved here as historical record per Working Principle #4):**
  > *"Corporate America knows the word 'severance.' When a company sheds workers to cut costs, we pay the severed employee — severance — and call it a cost of doing business. The word honors something: when you cut someone loose, you owe them. You sever the tie, and you pay for the severing. Cost severance works the opposite direction. When a company extracts value from a commons — a community, an ecosystem, a future generation — it sheds the COST of that value onto the source. The tie between value-capturer and cost-bearer gets severed, but the payment architecture of employment severance is absent. The cost-bearer gets stuck with the cost the value-capturer got paid to generate. So: severance we understand in employment. Cost severance is the same move, applied to the relationship between value-capturers and the commons they draw from — except the bill never comes due to the severing party. That's the problem this book is about."*

---

### Severed Cost

**Working definition:** a specific cost that has been severed — value extracted by capturer while the cost remains at the source (community, ecosystem, future generation). The result/quantity noun naming the quantified outcome of the Cost Severance mechanism. **Flagship adoption target** for the framework's success criterion ("severed cost" used by labor lawyer in brief).

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, Ring-1 synthesis batch).

**Glossary definition (~80 words, reader-register):**
> The result of cost severance — a specific cost cut loose from the transaction that created it and transferred to a third party who did not capture the value. The Black Lung Trust Fund's $4.6 billion deficit is a severed cost. The 13-year life expectancy gap in McDowell County is a severed cost. **Severed cost** is the framework's adoption target — the phrase the book hopes a labor lawyer or judge will use in court without needing it explained.

**Tech Appendix definition (~290 words, formal + lineage):**
> A specific instance of cost that has been severed from the transaction that produced it. Severed Cost is the framework's result/quantity noun naming the quantified outcome of the Cost Severance mechanism. Companion to Cost Severance (the process/mechanism noun) per the role-discipline ratified by the CS-vs-SC triage rigor pass (2026-04-24): Cost Severance for mechanism-naming and theoretical discussion; Severed Cost for instance-quantification and legal-register prose.
>
> Formal relationship: each Severed Cost instance is a specific value of CS = RCV − B for a given resource extraction at a given time. The aggregate Cost Severance across all extraction instances in a given accounting scope is the sum of the corresponding Severed Costs.
>
> Lexical role: subject or quantified predicate in accounting sentences. *"McDowell County bears a severed cost of $550/ton."* *"The Black Lung Trust Fund deficit is the severed cost the framework prices."* *"Severed cost shows up in community collapse, life-expectancy gaps, and atmospheric carbon."*
>
> M12 lineage: standard economics convention of distinguishing process-noun from result-noun (externality / externality cost; rent-seeking / rent). Severed Cost extends this convention to the cost-severance mechanism. Pair with Cost Severance is grammatical complementarity, not duplication.
>
> Adoption-target status: Severed Cost is THE framework's target for legal-register adoption per the framework's success criterion. The target case: a labor lawyer or judge uses "severed cost" in a brief or in open court without needing it explained, ten-plus years from publication. The criterion is structural — when the term has reached general legal vocabulary, the framework has succeeded in its adoption goal.

**Term-spec version:** v1.0 (first sanctioned spec after CS-vs-SC triage).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Same implicit rigor as Cost Severance — Severed Cost is the flagship adoption phrase tested across every rigor pass since Path F.
- CS-vs-SC triage rigor pass (2026-04-24) §17 — Option A ratified; Severed Cost retained as flagship adoption target alongside Cost Severance mechanism name.
- Ring-1 synthesis (2026-04-24) — role discipline reinforced.
- **Phase 2 deeper-dive rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md` (2026-04-29)** — bundled with Cost Severance Phase 2 audit. **Verdict: KEEP — RATIFIED 2026-04-29 by Chris Winn.** Severed Cost passes 12-cell matrix as flagship legal-tort-vocabulary adoption target. Cross-political-tradition lineage citations apply symmetrically (see Cost Severance entry above for full lineage list — Coulthard 2014; Tuck & Yang 2012; Darity & Mullen 2020 *From Here to Equality* especially load-bearing for Severed Cost as reparations-economics-parallel; Anderson 2017; Patel & Moore 2017; Federici 2004; Hickel 2020; Marx; Demsetz; Coase; Hayek; Pettit; US severance-tax law).

**Role discipline:** Severed Cost is the *result/quantity noun* + *flagship adoption phrase*. Use when quantifying a specific instance, writing legal/policy-register prose, or using the framework's adoption-target vocabulary. *"McDowell bears a severed cost of $550/ton."* *"The severed cost shows up in community collapse."* Lexical slot: object or quantified predicate in accounting sentences. Companion: Cost Severance for mechanism naming.

**Usage audit:** 37 occurrences in 12 files as of 2026-04-24 — less framework-internal usage than Cost Severance, but higher adoption potential (shorter, quantifiable, legal-register).

**Success criterion:** THE framework's target for adoption. *"If, ten-plus years from now, a labor lawyer uses 'severed cost' in a brief or in open court and the judge does not need it explained — the book has succeeded."*

**Depends on:**
- Cost Severance (mechanism-side companion — Ring 1)
- CS = RCV − B equation (Severed Cost is the quantified CS in specific instances)
- Value Extraction (causal event upstream)
- RCV − B computation (mathematical basis)

**Staleness triggers:**
- Success criterion shifts away from "severed cost" adoption target.
- Legal/policy adoption evidence after publication shows different phrase traveling instead.
- Mechanism-name changes (Cost Severance) would force SC revisit.

**Commit trail:**
- CS-vs-SC rigor pass: commit `0021e24` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A — retained under triage.

**Notes:**
- Flagship adoption phrase. When the book's rhetorical strategy is honest accounting, Severed Cost is the term that travels into legal briefs, policy memos, and journalism. Retirement or replacement would directly sabotage the success criterion.
- Style-discipline per CS-vs-SC rigor pass (and applies symmetrically with Cost Severance).

---

### Cost (Cᵢ)

**Working definition:** the framework's atomic unit of measurement — an indexed cost term admitted to the RCV integrand under the Four Gates discipline. Each Cᵢ has units [$ · resource-unit⁻¹ · time-unit⁻¹], is identified through the Commons Inversion Test (CIT) applied to a specific extraction Context, and contributes additively to RCV via the sum-of-costs form. The class of all costs is open and extensible — CIT applied to new Contexts may surface new costs the current framework does not enumerate.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn as part of Ring-1 synthesis batch; standalone rigor via Variable-vs-Cost pass).

**Glossary definition (~75 words, reader-register):**
> The framework's atomic unit of measurement — a specific cost term that gets summed into the framework's accounting. Each **Cᵢ** is a named cost (Direct Health Cost, Foreclosure Cost, Community Disruption Cost, Lineage Labor Cost, etc.) that the Commons Inversion Test has identified for a specific extraction. The class is open: every extraction surfaces its own Cᵢ set; the methodology is universal, the components are case-specific.

**Tech Appendix definition (~330 words, formal + lineage):**
> The framework's atomic unit of measurement: an indexed cost term Cᵢ admitted to the RCV integrand under the Four Gates discipline. Each Cᵢ has units [$ · resource-unit⁻¹ · time-unit⁻¹], is identified through the Commons Inversion Test (CIT) applied to a specific extraction Context, and contributes additively to RCV via the sum-of-costs form:
>
> **RCV(R, t₀, Context) = ∫ₜ₀^∞ { Σᵢ Cᵢ(R, t, Context) } · D(t, t₀) dt**
>
> The Σᵢ enumerates all Cᵢ that have been admitted via the Four Gates: (1) **CIT** — the cost claim is grounded in consumption of a finite commons (verified via Commons-Absence Inversion + Commons-Consumption Inversion sub-forms); (2) **Units Consistency** — Cᵢ is expressible in the framework's standard units; (3) **Boundedness** — Cᵢ's contribution to the integral converges to a finite value under the framework's discount assumptions; (4) **Independence** — Cᵢ does not double-count what an existing term already captures.
>
> The class of all Cᵢ is open and extensible — CIT applied to new Contexts may surface new cost components the current framework does not enumerate. Specific named costs that have been admitted across cases include Foreclosure Cost (C₁ canonical), Externality Tail (C₂ canonical), Community Disruption Cost, **Lineage Labor Cost** (renamed from Dynastic Labor Cost per Insight #56 RATIFIED 2026-04-30), Knowledge and Cultural Cost, Political Capture Cost, Temporal Displacement Cost. Each is a Cᵢ entry in the framework's accounting; each was admitted by passing the Four Gates against a specific extraction Context.
>
> Style discipline: prefer specific named costs ("Black Lung Cost," "Community Transition Cost") to the class noun "cost" wherever prose allows. Use Cᵢ (indexed by i) in formal/mathematical contexts; "cost term" remains admissible where math-as-term-of-sum is being explicitly invoked.
>
> Replaces prior informal "variable" / "cost variable" usage retired 2026-04-24 per Variable-vs-Cost rigor pass.

**Term-spec version:** v1.0 (first ratified spec; supersedes prior informal "variable" / "cost variable" / "cost term" usage).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-vs-Cost rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_variable_vs_cost_v1.0.0.md` (2026-04-24) §15 — Option B (replace "variable" with "cost") recommended. 5 options tested (A: variable / B: cost / C: hybrid / D: drop class term / E: ledger entry). Option B won on 9 of 11 modules; M1 and M7 indifferent.
- Full Ring-1 integrated rigor pass (2026-04-24) — Cost (Cᵢ) coheres with all other Ring-1 terms.

**Style discipline (inherited from D + E options as addenda):**
- *From Option D:* prefer specific named costs ("Black Lung Cost," "Community Transition Cost") to the class noun "cost" wherever prose allows. The class noun is fallback; specific names are default.
- *From Option E:* preserve bookkeeping metaphor at discourse level — framework voice is accountant's voice. "Cost" as atomic-unit name reinforces without needing more formal "ledger entry" / "accounting item" language.

**Notation:** Cᵢ (indexed by i) in formal/mathematical contexts; "cost" as class noun + specific-name (e.g., "black-lung cost") in prose contexts. "Cost term" remains admissible where math-as-term-of-sum is being explicitly invoked ("each cost term Cᵢ enters the integrand").

**Role:** atomic-unit-of-measurement across the framework's formula, gates, and accounting. Every named specific cost (Community Transition Cost, Lineage Labor Cost, Political Capture Cost, etc.) is a Cᵢ.

**Depends on:**
- Four gates (L.1–L.4 admit Cᵢ to RCV)
- RCV formula (integrand is Σᵢ Cᵢ · D)
- CIT (identifies which Cᵢ admit — Gate 1 of the Four Gates)
- Cost Severance (Cᵢ are what get severed)

**Staleness triggers:**
- Framework's atomic unit changes structurally (e.g., introduction of a higher-abstraction class above Cᵢ).
- Four-gate discipline materially revised.

**Commit trail:**
- Variable-vs-Cost rigor pass: commit `0c7547a` (2026-04-24).
- Ring-1 synthesis batch ratification: commit `af4b6d6` (2026-04-24).
- Integrated Ring-1 pass: commit `d4c4be4` (2026-04-24).

**Supersedes:** prior informal "variable" / "cost variable" / "cost term" usage in Path F rigor pass + Technical Appendix Sections L + M (usage continues as historical record in those docs per live-vs-archive policy).

**Notes:**
- Ambiguity with everyday "cost" in prose is managed by context-disambiguation — the same discipline economists apply to "utility" and "welfare."

---

### Residual Commons Value (RCV)

**Working definition:** the framework's central quantification — the true intergenerational cost of extraction that remains unpriced by conventional accounting (market prices + accountability bonds + existing externality instruments). Computed as the integral of the sum of admitted cost terms (Cᵢ) against a declining discount factor over infinite horizon:

RCV(R, t₀, Context) = ∫ₜ₀^∞ { Σᵢ Cᵢ(R, t, Context) } · D(t, t₀) dt

One side of the flagship equation CS = RCV − B, where CS is cost severance and B is the accountability bond.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, Ring-1 synthesis batch).

**Glossary definition (~75 words, reader-register):**
> The framework's central quantification — the true intergenerational cost of an extraction that remains unpriced by markets, accountability bonds, and standard externality instruments combined. **Residual Commons Value** is what's *left over* when you account for everything ordinary accounting captures and ask: what did this extraction actually cost the future, the community, the ecosystem? It pairs with the accountability bond in the framework's primitive equation: Cost Severance = Residual Commons Value − Bond posting.

**Tech Appendix definition (~310 words, formal + lineage):**
> The framework's central quantification: the true intergenerational cost of extraction that remains unpriced by conventional accounting (market prices + accountability bonds + existing externality instruments combined). RCV pairs with the Accountability Bond (B) in the framework's primitive equation:
>
> **CS(R, t₀) = RCV(R, t₀) − B(R, t₀)**
>
> where CS is per-unit Cost Severance for resource R at time t₀.
>
> RCV's formal expression — the integrand-and-integral form that admits new cost components per the Four Gates discipline:
>
> **RCV(R, t₀, Context) = ∫ₜ₀^∞ { Σᵢ Cᵢ(R, t, Context) } · D(t, t₀) dt**
>
> The integrand sums all admitted cost components Cᵢ (each filtered through the Commons Inversion Test, Units Consistency, Boundedness, and Independence gates), weighted by the social discount factor D(t, t₀). The integral runs from extraction time t₀ to infinite horizon — the framework prices what extraction severs from every future generation, not only present-value-discounted near-term harms.
>
> Triangulated estimation per Three Ways of Counting: each RCV calculation reports three independent methodological estimates (Replacement Cost / Revealed Preference / Scarcity-Adjusted Option Value) with explicit convergence range; no single-method RCV claim has standing in the framework's accounting.
>
> Semantic work per word: *Residual* — what remains unpriced after conventional accounting captures what it can; *Commons* — the shared pools bearing the cost (communities, ecosystems, future generations); *Value* — dollar-denominated quantity. Each word load-bearing per the RCV rigor pass §3.1; removing any creates ambiguity or unmoors the term.
>
> Framework's most-used term (~729 occurrences across framework docs). Most durable citation infrastructure.

**Term-spec version:** v1.0 (first sanctioned spec after rigor-pass verification).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-addability rigor pass (2026-04-24) — RCV confirmed as CORE quantification; variable-addability generalization preserves RCV form.
- Path F rigor pass (2026-04-24) — RCV's role under the four-gate discipline confirmed.
- Tier-reframing + macro-grouping passes (2026-04-24) — RCV unchanged.
- RCV rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_rcv_v1.0.0.md` (2026-04-24) §17 — Option A PASSES unconditionally. 729 total uses (658 acronym + 71 full-form) across 34 files — framework's MOST-used term. Name-quantity match exact per word (Residual / Commons / Value each does load-bearing semantic work).
- Ring-1 synthesis (2026-04-24) — RCV's equation-anchor role reinforced.

**Role:** quantification-anchor + equation-component (CS = RCV − B) + academic-citation target.

**Semantic work per word:**
- *Residual* — what remains unpriced after conventional accounting
- *Commons* — the shared pools bearing the cost (communities, ecosystems, future generations)
- *Value* — dollar-denominated quantity

Removing any word creates ambiguity or unmoors the term.

**Usage audit (2026-04-24):** 729 total uses across 34 files — **framework's most-used term.**

**Depends on:**
- Cost Severance (RCV is one side of CS = RCV − B)
- Severed Cost (SC is the result of CS = RCV − B computation)
- Accountability Bond (B) (RCV pairs with B in the equation)
- CIT (CIT admits Cᵢ that RCV integrates)
- Four gates (filter Cᵢ admissible to RCV)
- Value Extraction (causal event upstream)
- Framework CORE math

**Staleness triggers:**
- CS = RCV − B equation redefined.
- Conventional accounting scope changes in a way that redefines "residual" reference.
- Academic adoption evidence shows RCV failing to travel as citation anchor.

**Commit trail:**
- RCV rigor pass: commit `5dea091` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A.

**Notes:**
- Each word of "Residual Commons Value" is load-bearing per §3.1 of the RCV rigor pass.
- Rename candidates (True Intergenerational Cost, Commons Value, drop acronym, different root) each failed rigor on precision, equation integration, academic citation, or existing-usage continuity.
- The acronym's 658 framework-internal uses represent the framework's most durable citation infrastructure.
- Integration discipline: "RCV" as technical acronym; "Residual Commons Value" in first-use + formal contexts.

---

### Value Extraction

**Working definition:** the act by which value is separated from its source (a community, ecosystem, or future generation) and taken by a value-capturer. The causal event that produces Cost Severance — extraction severs cost from the capturer (who benefits) and leaves it with the source (who bears). First position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.*

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, promoted from Ring 2).

**Glossary definition (~75 words, reader-register):**
> The act by which value is separated from its source — a community, an ecosystem, or a future generation — and taken by someone who did not produce it. Value extraction is the causal event that produces cost severance: the same act that captures the value severs the cost from the capturer and leaves it with the source. The framework's causal chain runs *Value Extraction → Cost Severance → Severed Cost*.

**Tech Appendix definition (~330 words, formal + lineage):**
> The act by which value is separated from its source (a community, ecosystem, or future generation) and taken by a value-capturer. Value Extraction is the causal event that produces Cost Severance — extraction severs cost from the capturer (who benefits) and leaves it with the source (who bears). First position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.*
>
> M12 lineage: the framework builds on two adjacent intellectual traditions.
>
> Mariana Mazzucato (*The Value of Everything: Making and Taking in the Global Economy*, Penguin/PublicAffairs, 2018) is the dominant published usage of "value extraction" in political economy. Mazzucato defines value extraction as *"activities focused on moving around existing resources and outputs, and gaining disproportionately from the ensuing trade"* — focused on rent-seeking in financial capitalism (asset managers, pharmaceutical patent rents, financial-sector extraction). The framework extends Mazzucato's diagnosis from rent-seeking-in-financial-capitalism into the physical-resource domain — adding (a) a pricing mechanism (RCV, Severed Cost, Accountability Bond); (b) a causal chain naming the mechanism at three positions; (c) the Cost Severance specialization for the separation of value-capturers from cost-bearers in resource extraction; (d) an accountability instrument (B) that would internalize the severed costs into the extractor's ledger.
>
> David Harvey (*The New Imperialism*, Oxford University Press, 2003), Chapter 4, develops *accumulation by dispossession* as the contemporary form of the older primitive-accumulation pattern Marx named — capital accumulating not through productive activity but through seizure or enclosure of common resources. Harvey's framing predates Mazzucato and is foundational for both usages. The framework's "value extraction" rendering reframes Harvey's critique in accessible accounting-register language suitable for legal / policy / non-academic audiences.
>
> Canonical positioning: *"this framework extends Mazzucato's value-extraction critique from financial rent-seeking into the physical-resource domain, with a specific accountability instrument."*

**Term-spec version:** v1.1 (Mazzucato citation addendum added 2026-04-24 after literature audit; v1.0 was first sanctioned spec after triage vs Value Capture).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Full rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` (2026-04-24) — Option B PASSES extreme rigor. Wins on decisive causal-chain bridge test + register alignment with book's extraction-economy critique + Harvey lineage + legal-register adoption + Berggruen fit + concept-level audit (extract-derivatives already dominate framework prose 42 refs).
- Cross-pairing synthesis `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_synthesis_ring1_terms_v1.0.0.md` (2026-04-24) — Value Extraction verdict REINFORCED by synthesis: extraction's separation-from-source semantics pairs natively with Cost Severance's severance-from-capturer semantics. The chain flows.
- Vocabulary-footprint meta-pass §13.2.c (2026-04-24) — initial Ring-2 classification; corrected audit + author ratification promoted to Ring 1.

**Decisive test from rigor pass (causal-chain bridge):**
- *Value Extraction → Cost Severance → Severed Cost* reads as tight causal sequence because extraction IS the severance mechanism (the act of separating value from source is the same act that severs cost from the capturer).
- *Value Capture → Cost Severance → Severed Cost* required reader inference (capture is acquisition, not separation). Rejected.

**Literature positioning (added 2026-04-24 after prior-art audit):**

Mariana Mazzucato, *The Value of Everything: Making and Taking in the Global Economy* (Penguin/PublicAffairs, 2018), is the dominant established usage of the term "value extraction" in political economy. Mazzucato defines value extraction as *"activities focused on moving around existing resources and outputs, and gaining disproportionately from the ensuing trade"* — focused on rent-seeking in financial capitalism (asset managers, pharma patents, hedge funds, financial-sector extraction).

**Chris's relationship to Mazzucato's term:** Chris arrived at "value extraction" independently through his sociology-essay work as an accessible-language reframing of David Harvey's *"accumulation by dispossession"* (Harvey 2003). This was independent rediscovery of a parallel framing — not original coinage in the sense of priority in published discourse. Intellectual honesty requires acknowledging Mazzucato's prior published usage.

**The framework's extension of Mazzucato:** Where Mazzucato diagnoses value extraction as rent-seeking in financial capitalism (moving existing value without creating new), this framework operationalizes and specializes the diagnosis for physical-resource extraction — adding (a) a pricing mechanism (RCV, Severed Cost, Accountability Bond), (b) a causal chain (Value Extraction → Cost Severance → Severed Cost), (c) the Cost Severance mechanism specific to the separation of value-capturers from cost-bearers in resource extraction, (d) the Accountability Bond instrument that would price the severed costs into the extractor's ledger. The framework can be positioned as *"extending Mazzucato's value-extraction critique from financial rent-seeking into the physical-resource domain, with a specific accountability instrument."*

**Canonical citation form (recommended for Ch 1, Ch 6, Tech Appendix):**

> *"This framework extends Mariana Mazzucato's diagnosis of value extraction (Mazzucato 2018) — developed there for rent-seeking in financial capitalism — into the physical-resource domain. Where Mazzucato identifies value-extraction as activities that move existing value without creating new, this framework specifies the mechanism by which physical-resource extraction systematically separates value-capturers from cost-bearers (Cost Severance) and proposes a pricing instrument (Accountability Bond) to internalize the resulting Severed Cost. The framing echoes David Harvey's accumulation by dispossession (Harvey 2003), rendered in accessible accounting-register language."*

**Harvey lineage (preserved):** Value Extraction connects to David Harvey's *"accumulation by dispossession"* (Harvey 2003) as philosophical antecedent. Chris's usage reframes Harvey's critique in accessible accounting-register language suitable for policy / legal / non-academic audiences. Harvey's framing predates Mazzucato and is foundational for both usages.

**Depends on:**
- Cost Severance (Ring 1; the mechanism that Value Extraction causes)
- Severed Cost (Ring 1; the result downstream of the chain)
- Abundance framework (the abundances that Value Extraction operates against — producing scarcity-grounded costs that CIT admits)
- Principle #3 (variant-mechanism-match discipline; Value Extraction passes)

**Staleness triggers:**
- Cost Severance concept redefined in a way that changes the causal-chain relationship.
- Published peer review identifies legal-register ambiguity with regulatory-capture or extraction-industry usage.
- Adoption evidence shows "value extraction" failing to travel in legal/policy/Berggruen contexts.

**Commit trail:**
- Full rigor pass: commit `daef46a` (2026-04-24).
- Cross-pairing synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 promotion: this commit.

**Supersedes:** Value Capture (retired as duplicative per author 2026-04-24 admission that the two were interchangeable). Previous interchangeable-usage convention retired.

**Notes:**
- **Style discipline:** capitalized "Value Extraction" when naming the framework term; lowercase "value extraction" in prose when describing the act in context.
- First position in causal chain; Berggruen essay-critical per author direction 2026-04-24 ("that causal chain not landing means I lose the reader, reviewer, editor, et al at the very beginning").
- Phase A3 sweep target: 16 Value Capture proper-noun refs across 9 files → Value Extraction.
- Principle #4 (active-use traceability): chapter drafts using Value Extraction will gain provenance-pointer headers pointing to this Terms Index record during Phase A3 sweep.

---

### Value Capture

**Status:** RETIRED 2026-04-24 (Insight #28). Replaced by **Value Extraction** as the sole causal-event term.

**Why:** duplicative with Value Extraction (author 2026-04-24 admission that the two were interchangeable in meaning); triage selects one to avoid redundant vocabulary footprint competing with Value Extraction's success-criterion single-term adoption bet. Rigor-pass decisive tests (causal-chain bridge, register alignment, Harvey lineage, concept-level audit, critic pressure) all preferred Value Extraction.

**Notes:**
- Different retirement basis from misnaming (Principle #3) or adjective-precision retirements: Value Capture retires as DUPLICATE of a co-existing-preferred term.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md`.

---

### intergenerational cost severance (lowercase prose phrase)

**Working definition:** the intergenerational subtype of Cost Severance — value captured now, costs borne by future generations. Used as a lowercase descriptive phrase composing the framework's existing "intergenerational" adjective and "cost severance" Ring-1 term. Not a capitalized proper-noun compound.

**Status:** `CURRENT` as lowercase prose phrase (ratified 2026-04-24 by Chris Winn). Replaces the retired capitalized "Temporal Cost Severance" term.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Lowercase discipline is LOAD-BEARING:**
- Capitalizing as a proper-noun compound would reintroduce the jargon-inflation problem that sank "Temporal Cost Severance."
- The phrase composes two existing framework concepts (one abstract, one Ring-1); does not warrant proper-noun status.
- Style-guide: use lowercase always; restructure sentences to avoid sentence-start capitalization where possible.

**Academic connections:** Intergenerational equity (Weiss, Brown-Weiss); Intergenerational justice (Rawls, Parfit); Intergenerational ethics (Broome, Stern, Nordhaus); Intergenerational mobility (Chetty, Piketty). The phrase slots cleanly into these discourses.

**Depends on:** Cost Severance (Ring 1 parent); "intergenerational" adjective (framework's heavy usage); Principle-#3 variant-subtype discipline (passed — genuine subtype); lowercase discipline.

**Staleness triggers:** Cost Severance concept redefined; phrase drifts into capitalized usage; published peer review identifies systematic ambiguity.

**Rigor provenance:** Focused rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_intergenerational_cost_severance_v1.0.0.md` (Option A PASSES UNCONDITIONALLY). Companion: Temporal Cost Severance retirement (paired move). Principle-#3 check: PASSED.

**Supersedes:** "Temporal Cost Severance" capitalized term (see retired entry below). Full retirement trace at `archive/retirements/index.md` §1.

**Notes:**
- This phrase is NOT a technical term like Cost Severance, RCV, or CIT. It is a descriptive compound used consistently per style-guide discipline.
- Parallel to *spatial cost severance* (lowercase prose phrase). Together these form the framework's subtype-descriptor pair.

---

### Cost Bearing

**Status:** DEMOTED 2026-04-24 — concept persists in prose ("the cost-bearer," "the community bears," "future generations bear the cost") but no longer a framework-technical term. Glossary v2 entry removed in v3 bump.

**Why:** Cost Bearing describes a ROLE (someone is bearing cost), not a framework-specific mechanism or event. Role-description doesn't need technical vocabulary; chapter-draft usage (46 refs at audit) is already descriptive-register; no sweep required.

**Staleness triggers:** academic or legal discourse adopts "cost-bearer" as a technical-legal term (possible in employment/workers-rights law) — would warrant revisit.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor pass (vocabulary-footprint meta-pass §13.2.c) + author 2026-04-24 guidance.

---

### Temporal Cost Severance

**Status:** RETIRED 2026-04-24 (capitalized proper-noun term). Replaced by lowercase prose phrase **intergenerational cost severance** (see entry above).

**Why:** framework usage strongly preferred "intergenerational" over "temporal" (109× vs 6×); Principle-#3 check PASSED (genuine subtype) but retired on adjective-precision + framework-usage-evidence grounds.

**Reconsider pass (2026-04-24, ratified):** tested whether "temporal cost severance" should be adopted as a lowercase prose phrase parallel to spatial + intergenerational. **Verdict: KEEP RETIRED.** Principle-#3 check FAILED for "temporal" as lowercase form — the qualifier describes a constitutive property of ALL cost severance (all severance has temporal offset between value-capture and cost-bearing), not a distinguishing gap-type. Spatial + intergenerational lowercase pair does NOT extend to a three-member cohort.

**Notes (structurally load-bearing):**
- Different retirement basis from Spatial Cost Severance: Temporal PASSED Principle #3 but retired on usage-evidence; Spatial FAILED then PASSED on re-examination under v2 definition.
- Reconsider verdict diagnostic — "if removing a qualifier's condition doesn't leave other severance forms intact, the qualifier isn't a subtype qualifier" — originated in Spatial CS re-examination; reused here to reject lowercase adoption.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor passes (`commons_bonds_rigor_pass_2026-04-24_term_temporal_cost_severance_v1.0.0.md` + `..._reconsider_v1.0.0.md` + companion intergenerational lowercase adoption pass).

---

### Spatial Cost Severance / spatial cost severance

**Working definition:** the geographic subtype of Cost Severance — value extracted from an area disperses to distant consumers while costs (health, environmental, community) concentrate locally where extraction occurred. Used as **lowercase descriptive phrase** composing "spatial" modifier + Ring-1 "cost severance" term. Not capitalized as proper-noun compound.

**Status:** `CURRENT` as lowercase prose phrase (ratified 2026-04-24 by Chris Winn — un-retirement via re-examination rigor pass). Supersedes earlier `RETIRED` status from 2026-04-24 which was a Principle-#2 failure (audited the wrong phenomenon).

**Term-spec version:** v1.1 (v1.0 was RETIRED; v1.1 is CURRENT lowercase-prose-phrase after re-examination).

**Last reviewed:** 2026-04-24

**Why current:** Principle-#3 variant-subtype check under v2 definition PASSES — counterfactual (remove spatial dispersal of value) collapses value-capturer and cost-bearer into the same community; severance mechanism can't operate across a collapsed geography; spatial dispersal is load-bearing.

**Hybrid status (structurally load-bearing):** the proper-noun "Spatial Cost Severance" was RETIRED 2026-04-24 then UN-RETIRED same day as lowercase prose phrase via re-examination rigor pass. The original retirement was a Principle-#2 failure — the asteroid-teleport articulation audited spatial-abundance mechanics, not the v2 glossary geographic-dispersal definition. This re-examination **originated the "distinguishing gap-type" diagnostic** (later reused in Temporal CS reconsider pass): *"if removing a qualifier's condition doesn't leave other severance forms intact, the qualifier isn't a subtype qualifier."* Diagnostic remains live in framework toolkit.

**Depends on:** Cost Severance (Ring 1 parent); "spatial" adjective; Principle-#3 variant-subtype discipline; Principle #2 (audit concept not phrase — this re-examination is a Principle-#2 recovery template).

**Staleness triggers:** phrase drifts into capitalized usage → lowercase-discipline re-test; Cost Severance parent redefined; academic field adopts established terminology that should displace.

**Parallel to:** intergenerational cost severance (lowercase prose phrase). Together these form the framework's subtype-descriptor pair. Temporal was tested as potential third member via reconsider pass; FAILED Principle #3, kept retired.

**Notes:**
- **Distinct from Spatial abundance** (one of the 10 abundances). Spatial cost severance is a CS-subtype-by-geographic-gap. These are different framework elements; the conflation between them caused the original Principle-#2 failure.
- **Canonical example:** McDowell County 13-year life-expectancy gap.
- **Style discipline (lowercase always):** restructure sentences to avoid sentence-start capitalization where possible.

**Rigor provenance:** Re-examination rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_spatial_cost_severance_re_examination_v1.0.0.md` (Option B ratified). Earlier retirement + un-retirement event recorded in `archive/retirements/index.md` §1.

---

### Universality Test

**Status:** RETIRED / DEMOTED 2026-04-24 as capitalized named term. Concept preserved in prose as scope-claim + boundary-awareness; Tech Appendix §F Mars/Europa illustration retained without the named test.

**Why:** named-test status requires the test to be EXERCISED; 0 chapter refs + no in-book exercise failed that threshold. Pairing with CIT (then AIT) is categorial — both methodologies — but NOT structural (CIT's definition does not depend on UT being named), unlike the structural Abundance-Masking ↔ CIT pairing.

**Staleness triggers:** book cases start exercising a repeated universality-check methodology that benefits from a name-handle; CIT restructured such that its definition becomes dependent on UT being named; framework develops a formal boundary-condition protocol warranting its own named test.

**Notes:** Distinguishing from Abundance Masking (PROMOTED to Ring 2 in parallel re-examination): AM names an in-the-world mechanism active in every extraction case; UT names a validation methodology that isn't exercised anywhere. Different Principle-#3 outcomes despite both having pairing-with-methodology in v2.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_universality_test_re_examination_v1.0.0.md`.

---

### Civilizational Substitutability Gap (CSG)

**Status:** RETIRED 2026-04-24 as capitalized named term. Concept preserved in prose as **existential substitutability gap** (renamed 2026-04-29 from "industrial-existential substitutability gap" per Insight #33). Tech Appendix §G formula retained as sub-entry under Substitutability Function; policy rule retained.

**Why:** parsimony — framework doesn't name derived scalars. CSG is a DIFFERENCE between two S-evaluations (S_max(industrial) − S_max(existential)); analogous unnamed derivations include S(t) − S(t−1), max-S-over-uncertainty, S-for-rival-baselines. ARP-CSG pairing is TOPICAL not STRUCTURAL (ARP's definition doesn't depend on CSG being named) — contrasts with the structural Abundance-Masking ↔ CIT pairing.

**Notes (structurally load-bearing):**
- Close-call retirement: 66 active refs + active pedagogical use in Ch 7/Ch 9 + ARP topical pairing. **This ratification established Working Principle #1 Corollary B** ("usage frequency alone is not a rigor argument for retention") — usage-inertia could not override the derivation-from-primitive verdict.
- Prose form **existential substitutability gap** requires Bostrom 2002 + Bostrom 2014 + MacAskill 2022 + Ord 2020 lineage citations on first chapter introduction (per Insight #33 disambiguation discipline).

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor passes `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_csg_v1.0.0.md` + `..._csg_descriptive_prose_renaming_v1.0.0.md` (Insight #33).

---

### Substitutability Function (S)

**Working definition:** Probability function S(t | t₀) — probability that a functionally adequate substitute for resource R exists at future time t, conditional on baseline technological state at t₀. Appears in foreclosure-cost term C₁ = [1 − S(t|t₀)] · U(R, t, Q(t)). Influenced by extraction-timing feedback: earlier extraction can reduce innovation pressure and lower S(t) for future t. Framework's most novel single mathematical component per meta-pass §10.2.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Glossary definition (~80 words, reader-register):**
> A probability that says, for any future time, whether an adequate substitute for the resource being extracted will exist. **Substitutability Function S** answers the question every foreclosure calculation needs: how likely is it that the people of 2200 will have a non-petroleum way to do what petroleum currently does? When S = 1, foreclosure cost vanishes (a perfect substitute exists). When S = 0, foreclosure cost is the full intergenerational claim. Most cases sit between, and the function tracks where.

**Tech Appendix definition (~280 words, formal + lineage):**
> Probability function S(t | t₀): the probability that a functionally adequate substitute for resource R exists at future time t, conditional on baseline technological state at t₀. Appears in the foreclosure-cost term within RCV's integrand:
>
> **C₁(R, t, Q(t)) = [1 − S(t | t₀)] · U(R, t, Q(t))**
>
> where U is stock-dependent utility. The factor [1 − S(t | t₀)] weights the foreclosure contribution at each future time by the probability that no substitute exists then. Under perfect substitutability (S = 1), the foreclosure contribution vanishes. Under no substitutability (S = 0), the full per-period utility loss enters the integrand.
>
> The framework's most novel single mathematical component per Meta-pass §10.2 — distinguishes from Hicks 1932 elasticity of substitution (single-period; no time-indexed probability) and from Dixit-Pindyck 1994 real options (option-value framing without baseline-conditional probability structure).
>
> Endogenous to extraction timing: earlier extraction can reduce innovation pressure on substitute development, lowering S(t) for future t. The function therefore carries an extraction-timing feedback loop the framework prices but standard externality analysis does not.
>
> M12 lineage: Hicks 1932 *The Theory of Wages* (foundational elasticity-of-substitution lineage); Dixit & Pindyck 1994 *Investment under Uncertainty* (closest established real-options framing). Framework's specialization adds time-indexed probability + baseline-conditional structure + extraction-timing endogeneity.
>
> Mathematical function (not adoption-target vocabulary). Framework-internal load-bearing component; readers encounter S to understand C₁; the named adoption-target vocabulary is RCV / Cost Severance / Severed Cost.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 (commit `46600bc`) — identified as framework's most novel single component; Ring-2 default classification.
- Individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_substitutability_function_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) verified via distinctness check vs Hicks / real options / intertemporal substitution + 98-ref concept audit + Principle-#3 primitive-distinctness check.

**M12 classification:** Independent specialization (not adoption, not original coinage). Framework-specific features (time-indexed probability, baseline-conditional, endogenous to extraction timing) distinguish from Hicks 1932 elasticity of substitution + Dixit-Pindyck 1994 real options + intertemporal substitution macro theory.

**M12 citations (ratified 2026-04-24):**
- Hicks, John R. *The Theory of Wages* (1932) — foundational elasticity-of-substitution lineage.
- Dixit, Avinash K. & Pindyck, Robert S. *Investment under Uncertainty* (Princeton 1994) — real-options theory closest established concept.
Tech Appendix §L methodological footnote positions S as framework-specific extension.

**Why Ring 2 (not Ring 1):** S is a mathematical function; policymakers adopt named quantities (RCV), not named functions. Readers encounter S to understand C₁; non-readers don't adopt. Internal load-bearing is the correct scope.

**Depends on:** C₁ formula structure · definition of "functionally adequate substitute" · baseline t₀ convention.

**Pairs with:** Externality Tail E (sibling canonical cost term) · Foreclosure Cost C₁ (S is a factor in C₁) · Extraction-timing feedback loop.

**Staleness triggers:**
- CORE math restructured to eliminate C₁ as separate term.
- Academic field produces established terminology that should displace.
- Ring-1 vs Ring-2 boundary redrawn such that S becomes a public-adoption target.

**Commit trail:**
- Individual rigor pass: commit `302dffb` (2026-04-24).
- Ratification + Ring-2 record: this commit.

**Notes:**
- S_max derivations (including retired CSG formula) are compositional uses of S, not separate primitives. Primitive/derivation discipline established via CSG retirement pass.
- 98 active refs across 25 files as of 2026-04-24.
- Ch 6 §Substitutability Function is the term's pedagogical home.

---

### Externality Tail (E)

**Working definition:** Time-indexed cost function E(R, t) — damage from extraction of resource R at time t that persists independently of substitute availability. Sibling to foreclosure cost C₁ in the RCV integrand; runs on its own clock (temporally independent of S); structurally specializes Pigouvian externality concept with post-extraction persistence + substitutability-independence. "A substitute for coal doesn't clean up the mine. A substitute for oil doesn't remove carbon from the atmosphere."

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Glossary definition (~80 words, reader-register):**
> The damage that lingers after extraction stops. A substitute for coal doesn't clean up the mine. A substitute for oil doesn't remove carbon from the atmosphere. *Externality Tail* is the framework's name for costs that persist independently of whether substitutes appear — climate damage from past emissions, mine-tailings dispersion, biological extinction. Mathematically: E(R, t) — a time-indexed function that runs on its own clock. Specializes Pigou's externality concept (1920) for post-extraction persistence.

**Tech Appendix definition (~310 words, formal + lineage):**
> **E(R, t)** is a time-indexed cost function — the damage from extraction of resource R at time t that persists independently of substitute availability. The *Externality Tail* captures the class of costs whose persistence is decoupled from substitution dynamics: a substitute for coal doesn't clean up the mine; a substitute for oil doesn't remove carbon from the atmosphere; a substitute for a destroyed species doesn't restore extinction.
>
> Sibling to foreclosure cost C₁ in the RCV integrand. The two functions appear together in the framework's expanded RCV form: RCV(R, t₀) = ∫_{t₀}^∞ {[1 − S(t|t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt — where S is the Substitutability Function (governing C₁ behavior) and E captures externalities that run on their own clock (temporally independent of S).
>
> **Distinguished from generic Pigouvian externalities** (Pigou 1920) on four axes: (a) post-extraction persistence — the cost continues after extraction stops; (b) substitutability-independence — the cost is decoupled from whether substitutes appear; (c) time-indexed function form — E is a function of (resource, time), not a static unit-tax target; (d) "runs on its own clock" rhetorical anchor — separate temporal dynamics from S.
>
> **Why a function name (not a scalar).** Policymakers adopt named quantities (severed cost, accountability bond) rather than named functions. The Externality Tail is internal load-bearing infrastructure — Ring 2, not Ring 1. The phrase *"externality tail"* itself may earn Ring-1 travel potential if policy/legal discourse adopts; monitoring flag only.
>
> **M12 lineage.** Pigou 1920 *The Economics of Welfare* (4th ed. 1932) — foundational externality literature; Nordhaus & Boyer 2000 *Warming the World* (MIT Press) — DICE-model methodological parallel for time-indexed cumulative climate damage; Stern 2007 *The Economics of Climate Change: The Stern Review* (Cambridge) — intergenerational-equity framing. Framework's contribution is the four-axis specialization.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 — Ring-2 internal load-bearing classification.
- Individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_externality_tail_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) verified via distinctness check vs Pigouvian externalities + 46-ref concept audit + Principle-#3 check.

**M12 classification:** Framework-specific specialization of Pigouvian externality concept. Distinct via (a) post-extraction persistence, (b) substitutability-independence, (c) time-indexed function form, (d) "runs on its own clock" rhetorical anchor.

**M12 citations (ratified 2026-04-24):**
- Pigou, Arthur Cecil. *The Economics of Welfare* (1920, 4th ed. 1932) — foundational externality literature.
- Nordhaus, William D. & Boyer, Joseph. *Warming the World* (MIT Press 2000) — DICE model methodological parallel.
- Stern, Nicholas. *The Economics of Climate Change: The Stern Review* (Cambridge 2007) — intergenerational-equity framing.
Tech Appendix §L footnote positions E as temporal-specialization of Pigouvian externality.

**Why Ring 2 (not Ring 1):** E(R, t) is a function name; policymakers adopt named quantities, not named functions. Expanding Ring 1 dilutes adoption-bet focus on Severed Cost flagship.

**Phrase travel-potential flagged:** The PHRASE "externality tail" (not the function) may have Ring-1-travel potential if policy / legal discourse adopts. Monitoring note only; not a Ring-1 promotion recommendation.

**Depends on:** RCV integrand structure · "extraction" concept · "persistence" concept.

**Pairs with:** Substitutability Function (S) sibling · Foreclosure Cost (C₁) sibling · Four Gates (E passes through Gates like any admitted Cᵢ).

**Staleness triggers:**
- CORE math restructured to eliminate E as separate term.
- Academic field produces established terminology that should displace.
- Phrase "externality tail" adoption reaches threshold for Ring-1 promotion consideration.

**Commit trail:**
- Individual rigor pass: commit `bbe8069` (2026-04-24).
- Ratification + Ring-2 record: this commit.

**Notes:**
- "Tail" metaphor does NOT imply diminishing — E can compound (climate cumulative damage). Ch 6 clarification recommended.
- Ch 7 pedagogical role teaches foreclosure-vs-persistence distinction (C₁ vs E). Preserve.

---

### Intergenerational Option Value

**Working definition:** The value of preserving optionality on a resource for future-generation uses that may emerge from future technologies / discoveries / civilizational-application changes. Specialization of real-options option-value concept (Henry 1974; Arrow + Fisher 1974; Dixit + Pindyck 1994) to intergenerational temporal-scope. Distinct from Substitutability Function S (which captures *probability* of substitute existing) — Intergenerational Option Value captures the *value* of preserving the option to discover one.

**Status:** `CURRENT` at Ring 2 — RATIFIED 2026-04-30 by Chris Winn per Insight #57 (Group 1.2 Tier B promotion verdict).

**Glossary definition (~80 words, reader-register):**
> The value of preserving the option that future generations might discover or develop a use for a resource we currently extract. **Intergenerational Option Value** specializes real-options theory (Henry 1974; Arrow + Fisher 1974) to the temporal scope where future generations cannot bid in present markets. When extraction is irreversible and substitute discovery uncertain, preserving optionality has positive value even if no substitute is yet known. Ch 4 *The Existence Proof* uses this concept to establish that future generations have value-claims on present extraction.

**Tech Appendix definition (~280 words, formal + lineage):**
> Specialization of real-options theory's option-value concept (Henry 1974 *AER* "Investment Decisions Under Uncertainty: The Irreversibility Effect"; Arrow + Fisher 1974 *QJE* "Environmental Preservation, Uncertainty, and Irreversibility" quasi-option value; Dixit + Pindyck 1994 *Investment under Uncertainty*) to intergenerational temporal-scope. The framework specializes the temporal scope axis: real-options theory addresses uncertainty + irreversibility within markets where all parties bid; intergenerational option value addresses the same structure across generational boundaries where future parties cannot bid.
>
> Conceptual relationship to existing framework apparatus:
> - **Substitutability Function S(t | t₀)** captures *probability* of substitute existing at time t.
> - **Intergenerational Option Value** captures *value* of preserving the option to discover one.
> - Both contribute to the foreclosure-cost component C₁ within RCV's integrand, but at different conceptual levels (S is a probability factor; option-value is the welfare gain from preserved optionality).
>
> Ch 4 argument-load-bearing role: Ch 4 *The Existence Proof* frames the entire chapter via option-value reasoning. The "existence proof" Ch 4 establishes is that this option-value is non-zero under any reasonable preservation-of-future-utility assumption — therefore future generations have value-claims on present extraction even when no specific substitute has emerged.
>
> M12 lineage: Henry 1974 + Arrow + Fisher 1974 + Dixit-Pindyck 1994 (foundational real-options); Howarth + Norgaard 1990 *Land Economics* (intergenerational extension; "Intergenerational Resource Rights, Efficiency, and Social Optimality"); Howarth + Norgaard 1992 *AER* (sustainable-development valuation). Framework specializes by integrating with RCV integrand + Cᵢ-admissibility via CIT + Four Gates.

**Term-spec version:** v1.0 (first sanctioned spec post Group 1.2 ratification 2026-04-30).

**Last reviewed:** 2026-04-30

**Rigor provenance:**
- Holistic strategy §10 §5.1 (2026-04-29) — flagged Tier B promotion vs defer (commit `0a8510d`); discussion-needed verdict between (α) Tier B promotion and (β) defer.
- Group 1.2 rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-30_group1_2_intergenerational_option_value_v1.0.0.md` (2026-04-30) — full-depth rigor test parallel to Phase 2 #3.# theorem audits. **Verdict (α) Tier B promotion + dedicated terms_index entry RATIFIED 2026-04-30 by Chris Winn.** 12-cell multi-audience matrix: 9 STRONG + 3 ADEQUATE (Tier 2d + Socialist/communitarian + Lived-oppression — option-value reads as detached/abstract for present-suffering positions; mitigable via Tech Appendix §L methodological footnote per Insight #35 + #38 patterns). M11 critic-survival SURVIVES all 5 probes. Tier-ladder: Tier B clean (Henry/Arrow-Fisher/Dixit-Pindyck close-fit + intergenerational specialization decodable via light footnote).

**Decisive criterion for Tier B (vs defer):** Argument-load-bearing distinction. Ch 4 argument-spine depends on Intergenerational Option Value as named concept; threshold-policy that defers single-chapter Cᵢ items (Lifetime Survival Cost; Community Disruption Cost; Political Capture Cost; Temporal Displacement Cost) applies to illustrative mentions, not argument-spines. Per Insight #32 §32.3 corollary: usage-frequency is not the rigor argument; argument-load-bearing-ness is a separate axis.

**M12 lineage citations (ratified 2026-04-30):**
- Henry, C. 1974. "Investment Decisions Under Uncertainty: The Irreversibility Effect." *American Economic Review* 64(6): 1006-1012. — quasi-option-value foundation.
- Arrow, K. J. & Fisher, A. C. 1974. "Environmental Preservation, Uncertainty, and Irreversibility." *Quarterly Journal of Economics* 88(2): 312-319.
- Dixit, A. K. & Pindyck, R. S. 1994. *Investment Under Uncertainty.* Princeton University Press.
- Howarth, R. B. & Norgaard, R. B. 1990. "Intergenerational Resource Rights, Efficiency, and Social Optimality." *Land Economics* 66(1).
- Howarth, R. B. & Norgaard, R. B. 1992. "Environmental Valuation under Sustainable Development." *American Economic Review* 82(2).

**Cross-political-tradition robustness (per vocabulary strategy v1.0.1 §8):** STRONG on classical-liberal + civic-republican; ADEQUATE on socialist/communitarian + lived-oppression (option-value reads as academic-distance vocabulary; some heterodox traditions critique option-value as marketizing-the-future). Mitigation: Tech Appendix §L methodological footnote addressing commodification critique parallel to Insight #35 + #38 patterns (queued for Phase 3 v2.0.0 rebuild).

**Pairs with:** Substitutability Function (S) — distinct conceptual level (S = probability factor; option-value = welfare gain from preserved optionality); Foreclosure Cost (C₁) — option-value is welfare-economic basis for C₁ admissibility per CIT; RCV integrand.

**Pre-publication external review (per Insight #39):** economics PhD with real-options-theory specialization (Dixit-Pindyck tradition) + intergenerational-equity specialization (Brown Weiss + Howarth-Norgaard tradition) verifies framework-specialization is correctly characterized. Downstream gate.

**Implementation pending Phase 3 v2.0.0 rebuild:**
- Tech Appendix §L methodological footnote — address commodification critique + clarify intergenerational temporal-scope specialization.
- Glossary v3 → v4 rebuild Intergenerational Option Value dedicated entry.
- Optional Ch 4 prose tightening — verify framework-specialization + lineage bridge readable.

**Notes:**
- Distinct from Substitutability Function S(t) — S captures probability; Intergenerational Option Value captures the welfare value of preserving optionality. Both contribute to C₁ at different conceptual levels.
- Ch 4 first-introduction is the term's pedagogical home; framework cites Henry/Arrow-Fisher/Dixit-Pindyck/Howarth-Norgaard lineage on first use.
- Tier B classification preserves academic-anchor (real-options theory) while allowing framework-specialization (intergenerational temporal-scope; Cᵢ-admissibility via CIT + Four Gates).

---

### Asymmetric Regret Principle (ARP) — SUPERSEDED 2026-04-24 by Asymmetric Regret Rule (ARR)

**Status:** SUPERSEDED 2026-04-24 by Asymmetric Regret Rule (ARR). Decision-theoretic content + aphorism *"We can always extract later. We can never un-extract."* preserved unchanged; only LAST WORD updated ("Principle" → "Rule").

**Why renamed:** "Principle" overclaimed (operational decision rule, not foundational ethical principle). "Rule" downgrades while preserving the "Asymmetric Regret" M6 direct-name-visibility to Loomes-Sugden 1982 + Savage 1951 regret-theory tradition (no Tech-Appendix-footnote dependency).

**See:** Asymmetric Regret Rule (ARR) entry below for current framework element.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_asymmetric_regret_principle_v1.0.0.md`.

---

### Reversibility Default (RD) — RATIFICATION REVERSED 2026-04-24 (same-day flip)

**Status:** RATIFICATION-REVERSED 2026-04-24 (same-day flip). Preliminary ratification reversed when M6 academic-rigor question surfaced post-ratification: RD required Tech Appendix footnote + Ch 7 prose + Glossary entries to make Savage / Loomes-Sugden lineage visible; ARR has the lineage IN THE NAME (no footnote dependency). Author flipped to ARR.

**Lesson captured (structurally load-bearing for future rename passes):** when M5 + cross-tradition-adoption tradeoffs appear close, foreground M6 direct-name-visibility EXPLICITLY in the executive summary recommendation. The M5/M6 weighing should be visible to author at ratification time, not surfaced post-ratification.

**See:** Asymmetric Regret Rule (ARR) entry below — final ratified element. Same decision-theoretic content; only the name candidate differed.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor pass + ARP rename rigor pass.

---

### Asymmetric Regret Rule (ARR) — FINAL ratification 2026-04-24

**Working definition:** Framework-specific Ring-2 operational decision rule — when RCV tails cannot be precisely quantified, default to the option whose action is reversible: extraction when access window closes (Comet flyby), preservation when irreversible damage is at stake (Europa). Aphorism: *"We can always extract later. We can never un-extract."* Specialization of Savage 1951 minimax-regret with irreversibility-weighted regret tails (Loomes-Sugden 1982 regret-theory tradition). Bidirectional-flip-by-context (per Working Principle #5: context-flipping rules earn named-rule status). Aligned with Lempert-Popper-Bankes 2003 RDM + Rio Declaration 1992 precautionary tradition.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — supersedes Asymmetric Regret Principle; ratification finalized after same-day flip from preliminary Reversibility Default ratification).

**Glossary definition (~85 words, reader-register):**
> The framework's operational decision rule for cases where future costs can't be precisely quantified. *We can always extract later. We can never un-extract.* When in doubt, default to the action that's reversible. The rule flips by context: on a comet flyby (access window closes permanently), extraction is the reversible choice. On Europa-class biosphere risk, preservation is the reversible choice. Same rule, opposite verdicts. Specialization of regret-theory + minimax-regret tradition (Savage 1951; Loomes & Sugden 1982) with irreversibility-weighted regret tails.

**Tech Appendix definition (~310 words, formal + lineage):**
> The *Asymmetric Regret Rule* (ARR) is the framework's operational decision rule for the regime where RCV tails cannot be precisely quantified. Instruction: when uncertain, default to the option whose action is reversible relative to the alternative. The rule produces opposite operational verdicts under different contexts while remaining the same underlying rule (per Working Principle #5: context-flipping rules earn named-rule status). On Comet-flyby cases, extraction is the reversible action — the access window closes permanently and failing to extract is irreversible. On Europa-class cases (incommensurable biosphere externality), preservation is the reversible action — extraction would impose irreversible damage. The bidirectional flip is what justifies named-rule status over generic precautionary prose.
>
> **Aphorism:** *"We can always extract later. We can never un-extract."* The aphorism describes the operational instruction; the named rule names the principled basis (regret asymmetry under irreversibility).
>
> **Distinguished from the Precautionary Principle.** PP is unidirectional (default-to-caution). ARR is bidirectional — the default-to-reversibility direction depends on which action is reversible in the specific context. ARR survives M11 critic-survival probes that PP cannot (e.g., the critic claim "your rule would freeze all extraction" is false: ARR directs *extract* on Comet flyby).
>
> **M12 lineage.** Specialization within counterfactual-reasoning + minimax-regret + precautionary + real-options decision-theoretic lineage. Savage 1951 (*JASA* 46, no. 253: 55-67) — minimax-regret foundation; Loomes & Sugden 1982 (*Economic Journal*) — regret theory; Dixit & Pindyck 1994 — real-options reversibility-as-decision-axis; Lempert, Popper & Bankes 2003 (RAND) — Robust Decision Making; Rio Declaration 1992 Principle 15 — international-law precautionary tradition. Framework's contribution is the bidirectional-flip + irreversibility-weighted regret-tail framing.

**Term-spec version:** v2.0 (rename from Asymmetric Regret Principle v1.0; framework content unchanged; last word "Principle" → "Rule" to downgrade overclaim while preserving regret-theory direct-lineage in name).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- ARP rigor pass (commit `7f35783`, 2026-04-24) — Ring-2 promotion ratified for the underlying decision rule (originally as Asymmetric Regret Principle).
- ARP rename rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_arp_rename_v1.0.0.md` (commit `b8b62e3`, 2026-04-24) — 10 candidates tested; Reversibility Default identified as top M5 finalist; Asymmetric Regret Rule identified as M6 fallback. Pass's executive summary insufficiently surfaced M6 cost of RD's footnote-dependency; author M6 question post-ratification flipped final choice to ARR.
- Preliminary ratification (Reversibility Default) — REVERSED same-day 2026-04-24 after M6 question surfaced.
- Final ratification 2026-04-24 by Chris Winn — this commit. **Asymmetric Regret Rule (ARR) ratified.**

**Why "Asymmetric Regret Rule" (FINAL):**
- **M6 maximum-protective in the name.** Decision theorist + academic reviewer pattern-matches "Asymmetric Regret" to Loomes-Sugden 1982 + Savage 1951 regret-theory tradition immediately. No Tech-Appendix-footnote dependency.
- **"Rule" downgrades "Principle" overclaim** while preserving regret-theory framing — operational decision rule, not foundational ethical principle.
- **Minimal sweep cost** — ARP and ARR differ only in last word; existing chapter prose retains "asymmetric regret" framing largely intact.
- **Authorial-voice continuity** preserved — Ch 7 GuidanceDoc's existing "asymmetric regret" prose largely unchanged.
- **Decision-theoretic lineage in the name** stronger M6 than Reversibility Default's footnote-dependent lineage.
- **Aphorism preserved:** *"We can always extract later. We can never un-extract."* The aphorism describes the operational instruction; "Asymmetric Regret Rule" names the principled basis for that instruction (regret asymmetry under irreversibility).

**M12 classification:** Original specialization within counterfactual-reasoning + minimax-regret + precautionary-principle + real-options decision-theoretic lineage. Adjacent traditions cited; framework's contribution is specialization-with-bidirectional-flip + irreversibility-weighted regret-tail framing.

**M12 citations:**
- Savage, Leonard J. "The Theory of Statistical Decision." *Journal of the American Statistical Association* 46, no. 253 (1951): 55–67. — already in bibliography §16.
- Loomes & Sugden 1982 *Economic Journal* — already in bibliography §16. Asymmetric-regret theory.
- Lempert, Popper & Bankes 2003 *Shaping the Next One Hundred Years* — already in bibliography §16. Robust Decision Making.
- Dixit & Pindyck 1994 — already in bibliography §16. Real-options theory; reversibility-as-decision-axis.
- Rio Declaration 1992 Principle 15 — precautionary-principle tradition (general international-law reference; Tech Appendix footnote).

**Why Ring 2 (not Ring 1):**
- Framework-internal operational decision rule, not public-adoption-target vocabulary.
- Pedagogically useful across Ch 7 / Ch 9 / Ch 10 + Ch 7 GuidanceDoc but not flagship contribution.

**Why NOT retired (despite overlap with Precautionary Principle):**
- Bidirectional flip-by-context is RD-distinctive; PP is unidirectional.
- Trigger condition (cost-quantification uncertainty for RCV tails) is specific.
- 20+ active chapter refs.

**Pairs with:**
- RCV (Ring 1) — the function over whose tails uncertainty applies.
- Substitutability Function S (Ring 2) — RD governs decisions about high-substitutability-gap resources.
- Working Principle #5 (context-flipping rules earn named-rule status) — RD is the originating example.
- CSD + RCV two-instrument architecture — RD applies to uncertainty in either instrument's tails.

**Aphorism preserved:** *"We can always extract later. We can never un-extract."* This aphorism literally describes reversibility-default; renaming the rule to match the aphorism's actual content is consistent.

**Two paradigm cases (Ch 7) preserved:**
- **Comet flyby:** access window closes permanently → extraction is reversible-relative-to-losing-access → RD directs extract.
- **Europa:** incommensurable biosphere externality → preservation is reversible-relative-to-irreversible-damage → RD directs preserve.

**Open Insight #12** (ARP rename sub-decision) — closed-ratified 2026-04-24.

**Staleness triggers:**
- Framework develops formal minimax-regret treatment that subsumes RD mechanically.
- Academic adoption shows alternative naming displacing RD.
- Two paradigm cases (Comet/Europa) restructured in chapter drafting.

**Commit trail:**
- ARP Ring-2 promotion: commit `7f35783`.
- ARP rename rigor pass: commit `b8b62e3`.
- Ratification + Terms Index supersession + RD record: this commit.

**Notes:**
- Decision-theoretic content unchanged; only the name updated (ARP → ARR).
- Same Option C' political-philosophical-accommodation discipline that resolved Restitution Bond + 10-list dissolution applies — ARR is operationally primary + cross-tradition-adoption-broad.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §13.2.c (commit `af2f18e`) — DEFERRED pending author re-read.
- Individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_asymmetric_regret_principle_v1.0.0.md` (2026-04-24) — Option A (PROMOTE to Ring 2) ratified with rename-sub-decision flagged.
- **Principle #5 origination:** ARP's bidirectional-flip behavior originated Working Principle #5 ("Context-flipping rules earn named-rule status") ratified 2026-04-24.

**M12 classification:** Framework-specific operational specialization of established decision-theoretic family. Related to Precautionary Principle (different: ARP bidirectional, PP unidirectional); related to Savage 1951 minimax-regret + Loomes-Sugden 1982 regret theory (framework-specialization with irreversibility-weighted regret tails); related to Lempert Popper Bankes 2003 Robust Decision Making (philosophically aligned).

**M12 citations (ratified 2026-04-24):**
- Savage, Leonard J. "The Theory of Statistical Decision" (JASA 1951).
- Loomes, Graham & Sugden, Robert. "Regret Theory: An Alternative Theory of Rational Choice Under Uncertainty" (Economic Journal 1982).
- Lempert, Popper & Bankes. *Shaping the Next One Hundred Years* (RAND 2003).
Tech Appendix footnote positions ARP as framework-specialization.

**Why Ring 2 (not Ring 1):** Framework-internal operational rule, not public adoption target. Pedagogically useful across Ch 7 / Ch 9 / Ch 10 but not the flagship contribution.

**Why NOT retired (despite overlap with Precautionary Principle):** Bidirectional flip-by-context is ARP-distinctive; PP is unidirectional. Trigger condition (cost-quantification uncertainty for RCV tails) is specific. 20+ active chapter refs.

**Rename sub-decision (OPEN — pending author decision, does not affect rigor verdict):**
Candidates: *Asymmetric Regret Principle (current)* · *Asymmetric Regret Rule* · *Asymmetric Rule* · *Asymmetry Rule* · *Reversibility Default* · *Irreversibility Bias* · *Regret Asymmetry Rule* · *Option-Preservation Rule*. Captured as Open Insight for author deliberation. Rename (if adopted) is Phase A3 Stream A sweep work.

**CSG-ARP cross-pairing:** CSG retired 2026-04-24; ARP's v2 reference "high-CSG resources" rewrites to "resources with large industrial-existential substitutability gaps" in Phase A3 sweep. Applies regardless of rename outcome.

**Depends on:** RCV (the function over whose tails uncertainty applies) · framework's cost-quantification methodology.

**Pairs with:**
- Substitutability Function (S) — ARP governs decisions about high-gap resources.
- Universality Test concept (demoted) — ARP is the rule for boundary-condition regime.

**Staleness triggers:**
- Framework develops a formal minimax-regret treatment that subsumes ARP mechanically.
- Academic community adopts "Reversibility Default" or analogous terminology that would displace current name.
- Rename ratified — rerun under new name to verify rigor transfers cleanly.

**Commit trail:**
- Individual rigor pass: commit `7f35783` (2026-04-24).
- Principle #5 ratified (originating context): commit `cae4936`.
- Ratification + Ring-2 record: this commit.

**Notes:**
- "Principle" in current name may overclaim given ARP is operational decision rule, not foundational principle. Rename sub-decision captures this concern.
- Academic-positioning: Tech Appendix footnote cites Savage 1951 + Rio Declaration 1992 (Precautionary Principle) + Lempert et al. 2003 RDM to position ARP as framework-specialization of established decision theory.

---

### Accountability Bond (B)

**Working definition:** Formal quantity B in the framework's flagship equation CS = RCV − B. Represents the total dollars forced onto extractors via accountability instruments — reclamation bonds, sovereign wealth funds, carbon taxes, insurance requirements, direct liability, severance agreements, any financial mechanism that internalizes extraction costs. Under the framework's ideal B = RCV (honest accounting). Under current regimes B < RCV (accountability gap = Cost Severance = RCV − B). Extends established environmental-bonding / Pigouvian-tax lineage from project-specific or single-externality scope to full Severed Cost spectrum.

**Distinguishing identity — B is the framework's REMEDIATION-side variable** *(author-specified framing 2026-04-24):* where RCV / CIT / Cost Severance / Severed Cost are **diagnostic** (they reveal, identify, name, quantify the problem), Accountability Bond is the **action-side** element. B is the dollars that actually flow onto the extractor's ledger to close (or attempt to close) the cost-severance gap. B doesn't measure severance; it REMEDIATES it. **Structurally the only remediation-side variable in the framework** — every other Ring-1/Ring-2 element works to make the gap visible; B is the element that does something about it. This is why B draws the heaviest scope-creep pressure (Open Insight #13) — action-side questions invite instrument-design depth (how specifically to raise B in case X for category Y?) that belongs to Book 2/3 not Book 1. The "Bond" metaphor reinforces the identity: a bond is POSTED (action), not MEASURED.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Glossary definition (~75 words, reader-register):**
> The framework's action-side variable: the dollars actually forced onto extractors via accountability instruments — reclamation bonds, sovereign wealth funds, carbon taxes, environmental insurance, severance agreements. **Accountability Bond (B)** is what closes (or attempts to close) the cost-severance gap. The primitive equation: Cost Severance = Residual Commons Value − Accountability Bond posted. Under honest accounting, B = RCV; current regimes leave B < RCV by orders of magnitude.

**Tech Appendix definition (~340 words, formal + lineage):**
> The framework's right-side equation variable: the formal scalar B in the primitive equation
>
> **CS(R, t₀) = RCV(R, t₀) − B(R, t₀)**
>
> Represents the total dollars forced onto extractors via accountability instruments — the financial mechanisms that internalize extraction costs onto the extractor's ledger. Instrument cluster includes: reclamation bonds (Surface Mining Control and Reclamation Act 1977 + supporting OSMRE guidance + GAO 2017 financial-assurances analysis); Environmental Impact Bonds (Balboa 2016); Pigouvian taxes (Pigou 1920 *Economics of Welfare*); sovereign wealth funds operationalizing the Hartwick rule (Hartwick 1977); decommissioning bonds; carbon-pricing schemes; environmental-justice damages compensation; toxic-tort + class-action damages; truth-and-reconciliation processes.
>
> The Accountability Bond is the framework's only **action-side** variable — every other Ring-1 / Ring-2 element (RCV / CIT / Cost Severance / Severed Cost / Cᵢ / Substitutability Function / Externality Tail) is **diagnostic** (reveals, identifies, names, or quantifies the problem). B is the dollars that actually flow onto the extractor's ledger to close (or attempt to close) the cost-severance gap. B doesn't measure severance; it remediates it.
>
> Decomposed in Ring 2 as B = B₁ + B₂ where B₁ is the Restitution Bond (backward-looking; closes already-realized harm; reparations-economics lineage per Darity & Mullen 2020) and B₂ is the Foreclosure Bond (forward-looking; closes prospective intergenerational foreclosure; option-value + Hartwick-rule lineage).
>
> Under honest accounting, B = RCV: the bond posted equals the true intergenerational cost. Under current regimes, B < RCV across nearly every extraction case examined; the gap is the cost severance the framework prices.
>
> Norway's Government Pension Fund Global (sovereign wealth fund) is the canonical real-world exemplar of B operating at scale — capturing roughly 70-80% of net petroleum wealth for intergenerational distribution. Norway's solution presupposes governance preconditions and is not universal. The framework's claim is mathematical (B = RCV is honest accounting); which specific instrument-mix best realizes that equality is a live policy-design space.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 (commit `46600bc`) — Ring-2 internal load-bearing classification.
- Literature audit + citation ratification commits `56a226f` + `f643e59` (2026-04-24) — M12 classification as extension of reclamation-bond + EIB + Pigouvian-tax lineage; bibliography citations ratified for Ch 5 + Tech Appendix.
- Individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_accountability_bond_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) + two monitoring flags (phrase-travel + scope-creep).

**M12 classification:** Independent specialization + extension of established environmental-bonding / Pigouvian-tax lineage. Framework novelty is (a) full-Severed-Cost scope vs reclamation-only, (b) equational-closure role in CS = RCV − B. Not original coinage; consciously extends prior art.

**M12 citations (ratified 2026-04-24):**
- Pigou, Arthur Cecil. *The Economics of Welfare* (1920, 4th ed. 1932).
- Balboa, Cristina M. "Accountability of Environmental Impact Bonds" (*Global Environmental Politics* 2016).
- Yang, Peifang & Davis, Graham A. "Why Don't Environmental Bonds Fully Cover Reclamation Costs?" (*Energy Policy* 2021).
- U.S. GAO. *Financial Assurances for Reclamation* (GAO-17-207R, 2017).
- U.S. OSMRE. *Reclamation Bonds* (agency guidance).

Canonical Ch 5 + Tech Appendix first-use citation form drafted in rigor pass §3.5.

**Why Ring 2 (not Ring 1):**
- Scalar-variable role dominant (right-side of CS = RCV − B equation).
- Ring-1 focus discipline preserves adoption-bet focus on 7 current flagships.
- Phrase-travel-flag captures Ring-1-promotion upside without current commitment.

**Two monitoring flags (ratified 2026-04-24):**

**(i) Phrase-travel monitoring flag.** Watch for post-publication adoption evidence that "accountability bond" travels independently of framework uptake (legal briefs, policy papers, academic citation as load-bearing adoption term). Rerun trigger: reconsider Ring-1 promotion if phrase begins traveling in target-audience discourse.

**(ii) Scope-creep monitoring flag (cross-cutting; applies to whole framework, but Accountability Bond is likely-heaviest source of pressure). Governing doc: `tools/commons_bonds_book_scope_v1_0_3.md`.** Boundary is **framework-naming vs applied-advocacy-on-named-beneficiaries**, NOT diagnosis-vs-fix (corrected 2026-04-24 after author pointed to v1.0.3 strategy doc).
- **In-scope for Book 1 (framework-naming; passes v1.0.3 §6.1 rigor test as symmetric + shielded):** naming Accountability Bond; equational-closure role; lineage citation; flagship case illustration (McDowell, Deepwater, Libby, Social Security, etc.); framework-level prescription ("B should equal RCV" as stated ideal); Community Transition Reserve as named policy rec in Ch 9; one-paragraph signposts ($10–15T aggregate subsidy Ch 8 signpost).
- **Out-of-scope for Book 1, belongs in Book 2 (applied-advocacy; FAILS v1.0.3 §6.1 rigor test as asymmetric + unshielded for lone author):** full-economy B-vs-RCV simulation; resource-by-resource transition mechanics; named industries with documented lobbying histories that have kept their specific B below their specific RCV; named beneficiaries of the B < RCV gap; specific regulatory-capture events as case-study material; policy architecture at implementation level for named jurisdictions.
- **Trigger indicators during chapter drafting:** passage names specific industries with lobbying history; passage attempts full-economy simulation; passage does resource-by-resource transition mechanics; footnote becomes mini-essay on named industry.
- **Why B is heaviest scope-creep source:** B is the framework's **remediation-side variable** (only framework element that does something about the gap rather than measure it). Remediation role structurally pulls toward applied-advocacy on named beneficiaries. Book 1 names B + states B = RCV as ideal; Book 2 (requires coauthor/institutional shield) does applied work on specific industries' under-bonding + lobbying histories that sustain it.
- **Mitigation:** Book 1 points to future books ("a fuller treatment of named industries' lobbying histories is beyond this book's framework scope and is the subject of future applied work") rather than absorbing the depth. Preserve detailed notes in `archive/_OneDayMaybe/book-two/` for future.

**Rename candidates tested and rejected (per rigor pass §4):** *Accountability Severance* · *Severance Bond* · *Severed-Cost Bond* · *Commons Liability Bond*. Best fallback if rename ever needed: *Severed-Cost Bond* (pairs with Ring-1 flagship Severed Cost).

**Depends on:** CS = RCV − B equation · RCV definition · "accountability instrument" concept space.

**Pairs with:**
- RCV (left-side equation term; B is compared against RCV).
- Cost Severance (CS = gap between RCV and B).
- Commons Bonds (framework name; B is the instrument subtype of the broader commons-bonds category).

**Staleness triggers:**
- CS = RCV − B equation restructured.
- Phrase adoption in legal/policy discourse triggers Ring-1 reconsideration.
- Chapter drafting triggers scope-creep flag (instrument-design specifics beyond Book 1 scope).
- Established instrument terminology shifts (e.g., EIBs displace reclamation bonds as dominant policy frame).

**Commit trail:**
- Literature audit + citation ratification: commits `56a226f` + `f643e59` (2026-04-24).
- Individual rigor pass: commit `7fa1c1b` (2026-04-24).
- Ratification + Terms Index record: this commit.

**Notes:**
- B pairs structurally with RCV to close CS equation. Same mathematical-function-dominance as S and E but different role (output-side of equation vs integrand-components).
- "Accountability" vs "liability" distinction: accountability is the relational + constructive word (positive framing); liability is the defensive legal-action word. Framework uses "accountability" intentionally.
- "Bond" metaphor: operates both as financial-instrument (legal-register) and relational-bond (framework-title register). Double-entendre load-bearing for book's Commons Bonds positioning.

**Epistemic-humility discipline — author-specified framing 2026-04-24 (load-bearing for Book 1 authorial-voice calibration):**
- B is the framework CATEGORY for every mechanism that forces cost-bearing on extractors — NOT a novel single-instrument prescription. Book 1 should NOT present Accountability Bond as THE solution to cost severance.
- **Norway's Government Pension Fund Global (sovereign wealth fund) is Book 1's canonical existing real-world exemplar** of intergenerational-cost-severance mitigation. Norway is the most impressive existing solution humanity has produced for this problem class — framework-canonical case (Ch 4 anchor).
- **Norway's solution presupposes governance preconditions** (rule of law; institutional architecture preventing plundering current-population accounts or not-yet-born-generation accounts). Not a universal solution; its preconditions are load-bearing. Book 1 honors this — "even the best existing example isn't universal."
- **No claim to having solved it.** The framework's claim is mathematical (B = RCV is honest accounting); which specific instrument-mix best realizes that equality is a LIVE policy design space Book 1 frames but doesn't settle. Book 2 (or authors with institutional cover) are better positioned for applied instrument-design debate.
- **Book 1 CAN ponder.** Framework-appropriate pondering: *"perhaps something like an accountability bond could bridge this, though the Norway example shows what actually works and under what preconditions."* What's OUT of scope: prescribing a specific instrument design (e.g., "The Commons Bonds Framework Accountability Bond Act") as THE fix.

---

### Abundance Masking

**Working definition:** The mechanism by which abundance makes costs invisible to market pricing until scarcity forces them into view. Oxygen feels free because Earth's atmosphere is abundant. Ecological services feel free because ecosystems haven't collapsed yet. **Abundance Masking is the mechanism; Abundance Dimension is the dimension along which it operates** — distinct entries: masking is a process, dimension is a category (per v2 definition). Paired with CIT: masking is the process; CIT is the methodology that detects what masking hides.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — promoted from earlier DEMOTE-to-prose via re-examination).

**Glossary definition (~75 words, reader-register):**
> The mechanism by which abundance makes costs invisible to market pricing until scarcity forces them into view. Oxygen feels free because Earth's atmosphere is abundant. Ecological services feel free because ecosystems haven't collapsed yet. Coal-country lung tissue felt free because the affected population was small and dispersed. *Abundance Masking* names *how* costs hide; the Commons Inversion Test (CIT) is the methodology that *finds* what's being hidden. Mechanism + methodology — paired.

**Tech Appendix definition (~290 words, formal + lineage):**
> *Abundance Masking* is the framework's mechanism-name for the process by which a commons's abundance state suppresses market pricing of costs that draw down that commons. The mechanism operates whenever the commons is sufficiently abundant that scarcity-driven price signals haven't yet emerged: atmospheric oxygen is unpriced because Earth's atmosphere is abundant; ecological services are unpriced because ecosystems haven't yet collapsed; lung-tissue capacity in coal communities was unpriced because the affected population was geographically and politically small. The mechanism does not require *intent* — it operates structurally whenever the abundance condition holds.
>
> **Pairing structure (load-bearing).** Abundance Masking is paired structurally — not topically — with the Commons Inversion Test (CIT, Ring 1, supersedes AIT 2026-04-24). The pairing is: Abundance Masking is the mechanism the framework asks CIT to detect; CIT is the methodology that surfaces what Abundance Masking is hiding. CIT's definition requires Abundance Masking to be a named object — without the mechanism-name, CIT becomes circular ("a test for the unnamed thing"). Retiring Abundance Masking would break CIT's definition. The structural-pairing principle (originated in this term's re-examination) now governs Ring-2 promotion decisions for mechanism-methodology pairs.
>
> **Distinguished from Abundance Dimension.** Mechanism vs category. Abundance Masking is the *process* by which costs become invisible; abundance dimension is the *kind* of abundance along which the mechanism operates (atmospheric, ecological, temporal, etc.).
>
> **M12 lineage.** Framework-specific mechanism-name. Adjacent literature includes ecological-economics work on the rhetoric of abundance masking depletion + artificial-scarcity literature (Desai & Lemley 2022, *Notre Dame Law Review*); no established term captures the specific framework role as CIT-paired mechanism-name. Appears novel as specific framework term.

**Term-spec version:** v1.1 (v1.0 was the meta-pass demote-to-prose recommendation; v1.1 corrects after Principle-#2 re-read under re-examination).

**Last reviewed:** 2026-04-24

**History and re-examination:**

The term was initially scheduled for DEMOTE-to-prose 2026-04-24 (meta-pass §13.2.c, commit `46600bc`) with rationale: *"Abundance Masking names the phenomenon that AIT detects — abundances mask costs by making them invisible to pricing. But the phenomenon is what AIT is FOR. Naming it as a separate term creates a term-per-mechanism bloat."*

**The re-examination (2026-04-24) revealed this was a Principle-#2 failure.** The reasoning got the direction BACKWARDS — it said "AIT detects AM, therefore AM is redundant with AIT." That's analogous to saying "we have 'severance mechanism detection,' so we don't need the term 'severance mechanism' itself." The DETECTOR and the DETECTED are complementary, not redundant.

The v2 definition makes the pairing structure explicit: *"Abundance Masking is the mechanism; Abundance Dimension is the dimension along which it operates. These are distinct entries: masking is a process, dimension is a category."*

**Decisive test — "What does CIT detect?":**
- Without Abundance Masking term: CIT's definition becomes circular or unanchored. Adversarial reader: *"What makes a cost scarcity-grounded vs not?"* The answer requires naming the phenomenon CIT is designed to detect.
- With Abundance Masking term: *"CIT tests whether a candidate cost survives commons-inversion — i.e., whether the cost is genuinely hidden by Abundance Masking or is intrinsic to the activity regardless of scarcity."* Clean + explanatorily complete.

**Parallel to Cost Severance vs Severed Cost pair:** framework benefits from naming both sides of flagship mechanism-pairs:

| Pair type | Left side | Right side |
|---|---|---|
| Mechanism + Result | Cost Severance | Severed Cost |
| **Mechanism + Methodology** | **Abundance Masking** | **CIT** |
| Event + Mechanism | Value Extraction | Cost Severance |

**Rigor provenance:**
- Meta-pass §11.3 + §13.2.c (commit `46600bc`, 2026-04-24) — initial DEMOTE-to-prose recommendation; Principle-#2 failure.
- Re-examination rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_abundance_masking_re_examination_v1.0.0.md` (2026-04-24, commit `cf02160`) — Option A (PROMOTE to Ring 2) recommended; supersedes earlier demote-to-prose.
- Ratification 2026-04-24 by Chris Winn — this commit.
- **Diagnostic originated here (cross-cutting):** "structural vs topical pairing" distinction that later guided Universality Test re-examination + CSG-ARP pairing analysis. Structural pairings (Partner-A's definition requires Partner-B named) justify Ring-2 promotion; topical pairings don't.

**M12 classification:** Framework-specific mechanism-name. The concept of abundance making costs invisible is adjacent to "rhetoric of abundance masks depletion" in ecological-economics literature + artificial-scarcity literature (Desai & Lemley 2022), but no established term captures the specific framework role as CIT-paired mechanism-name. **Appears novel as specific framework term.**

**Why Ring 2 (not Ring 1):**
- Framework-internal mechanism-name paired with CIT (also Ring 1).
- Not a public-adoption target. Readers encounter AM to understand CIT's object; non-readers don't adopt.
- Chapter usage pattern: the MECHANISM is active in every extraction case in the book (costs masked by atmospheric abundance, ecosystem-service abundance, etc. — McDowell, Deepwater, Libby, all exhibit the mechanism). Naming it at Ring 2 formalizes what's already operating.

**Depends on:**
- CIT (paired detection methodology — Ring 1)
- Abundances (the domain over which masking operates)
- Cost Severance (the phenomenon that masking enables by hiding costs)

**Pairs with:**
- **CIT (structural pairing).** CIT's definition requires Abundance Masking named. Retiring AM would break CIT's definition.
- **Abundance Dimension.** Process vs category distinction per v2 definition.

**Staleness triggers:**
- CIT methodology redefined in a way that changes what it detects.
- Framework's abundance vocabulary restructured.

**Commit trail:**
- Meta-pass initial DEMOTE-to-prose analysis: commit `46600bc` (2026-04-24).
- Re-examination rigor pass: commit `cf02160` (2026-04-24).
- Ratification + Ring-2 record: this commit.

**Supersedes / superseded by:** v1.1 (CURRENT Ring 2) supersedes v1.0 (DEMOTE-to-prose) from meta-pass §13.2.c. Earlier demotion preserved in history above as Principle-#2 recovery template.

**Notes:**
- Distinct from Abundance Dimension per v2 explicit distinction (process vs category).
- In-the-world mechanism: active in every extraction case in the book whether or not named in chapter prose. Naming formalizes what's already operating.
- **Diagnostic origination:** this re-examination surfaced the "structural vs topical pairing" distinction that is now part of the rigor protocol's working toolkit for evaluating CIT-pairing arguments (and analogous mechanism-methodology pairings). Formalized as M12 action-ladder input via Principle #6.

---

### CS = RCV − B equation (named relational claim)

**Working definition:** The framework's central relational claim — Cost Severance in a transaction equals specifically Residual Commons Value minus Accountability Bond (arithmetic subtraction). The equation asserts: (i) only RCV and B matter for computing CS; (ii) the accountability-gap is linear in B (each dollar of B reduces CS dollar-for-dollar); (iii) B = RCV defines the framework's ideal state quantitatively (CS = 0 ↔ honest accounting). **Named framework object distinct from its component terms** — CS, RCV, B each have their own Terms Index record + rigor pass; this equation record is the ratified-2026-04-24 classification of the equation itself as a distinct Ring-2 structural element.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — "named relational claim").

**Glossary definition (~85 words, reader-register):**
> The framework's flagship equation. Cost Severance equals Residual Commons Value minus Accountability Bond — *what's truly owed minus what's actually paid*. When B = RCV, severance is zero (honest accounting). When B is below RCV, the difference is what gets passed to communities, ecosystems, or future generations. Norway's sovereign wealth fund is the canonical real-world example of B approaching RCV; the American extraction economy operates with B ≪ RCV. Three words, one operator — the book's central assertion in compressed form.

**Tech Appendix definition (~320 words, formal + lineage):**
> **CS = RCV − B** — the framework's central relational claim. Cost Severance in a transaction equals Residual Commons Value minus Accountability Bond (arithmetic subtraction, dollar-denominated). The equation asserts three things simultaneously: (i) only RCV and B matter for computing CS — no third term, no nonlinearity; (ii) the accountability-gap is linear in B (each dollar of B reduces CS dollar-for-dollar); (iii) B = RCV defines the framework's ideal state quantitatively (CS = 0 ↔ honest accounting). It is a *named relational claim* — the equation itself is a Ring-2 framework object distinct from its component terms (CS / RCV / B each have separate Terms Index records).
>
> **Stability-anchor function.** Naming the equation forces consistency across term definitions. If a later rigor pass weakens one component, the equation surfaces the consequence for the whole framework immediately (rigor-infrastructure load-bearing).
>
> **Scope discipline.** The equation is *framework-level prescription* — it does NOT commit to which specific instrument-mix realizes B. Norway's sovereign wealth fund is the canonical real-world example of B approaching RCV; the equation itself is the framework-level object that makes Norway's success measurable AND that makes the American B ≪ RCV gap visible. Book 1 presents the equation + points to Norway as best-existing-example + ponders Accountability Bond as one candidate direction; the framework does not prescribe a specific instrument design as THE fix (per Insight #14 epistemic-humility discipline).
>
> **M12 lineage.** Independent specialization of established gap/deficit-accounting structure. Gap-form equations are ubiquitous in adjacent literature: Pigou 1920 *The Economics of Welfare* (externality − tax = unpriced amount); Stern 2007 *The Economics of Climate Change: The Stern Review* (present-cost-to-future − current-priced = intergenerational transfer); Nordhaus & Boyer 2000 *Warming the World* (cumulative marginal damage − market carbon price = social cost of carbon gap). Framework novelty is NOT the gap-form (ubiquitous in welfare economics) — it is the specific decomposition: what RCV is, what B is, what CS is as mechanism-result pair with Severed Cost.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 + §12.1 item 7 (commit `46600bc`) — identified as Ring-2 internal load-bearing ("CS = RCV − B equation (as a single conceptual object)").
- Ring-1 full integrated pass (commit `d4c4be4`) — equation structurally tested in unified-system rigor; no reconsideration surfaced.
- Individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_cs_rcv_b_equation_v1.0.0.md` (2026-04-24) — Option A (CONFIRM Ring 2 as named relational claim) ratified 2026-04-24 by Chris Winn. Principle-#3 derivation check PASSES (light non-triviality: equation fixes arithmetic form + only-these-components claim + ideal-state definition beyond what's in components' prose definitions). M12 classification: independent specialization of established gap-accounting structure.

**M12 classification:** Independent specialization of established gap/deficit-accounting structure. Gap-form equations ubiquitous in adjacent literature:
- **Pigouvian gap:** externality − tax = unpriced amount (Pigou 1920).
- **Stern Review intergenerational framing:** present-cost-to-future minus current-priced = intergenerational transfer (Stern 2007).
- **Nordhaus DICE social-cost-of-carbon:** cumulative marginal damage − market carbon price = SCC gap (Nordhaus & Boyer 2000).
- **Accounting identity:** economic-cost − recorded-cost = unrecorded-cost.

Framework novelty is NOT the gap-form (ubiquitous) — it is the specific decomposition (what RCV is, what B is, what CS is as mechanism-result pair with Severed Cost).

**M12 citations (ratified 2026-04-24, already added to bibliography in prior commits):**
- Pigou, Arthur Cecil. *The Economics of Welfare* (1920) — Pigouvian gap lineage.
- Stern, Nicholas. *The Economics of Climate Change: The Stern Review* (Cambridge 2007) — intergenerational-gap parallel.
- Nordhaus, William D. & Boyer, Joseph. *Warming the World* (MIT Press 2000) — DICE social-cost-of-carbon parallel.

Tech Appendix §L methodological footnote positions the equation as extension of this established gap-accounting lineage with framework-specific decomposition.

**Why Ring 2 (not Ring 1):**
- Equations don't travel as adoption vocabulary the way terms do. Ring-1 adoption-targets are CS / SC / RCV / B / CIT / VE / Commons Bonds individually.
- Analogue: *F = ma* travels as vocabulary, but only AFTER Newtonian framework adoption; the framework-level terms (force, mass, acceleration) travel first. Same pattern: framework terms travel first; the equation holds them together internally.
- The equation is the internal structural anchor — Ring 2 (internal load-bearing) appropriate.

**Why NOT demoted to "just math" or merged into Cost Severance record:**
- Carries independent content (arithmetic form; only-B-and-RCV-matter claim; ideal-state definition).
- Citing the equation as a single object is rhetorically and pedagogically more economical than reconstructing the relationship each time.
- **Stability-anchor function** in rigor infrastructure: naming the equation forces consistency across term definitions. If a later rigor pass weakens one term, the equation surfaces the consequence for the whole framework immediately.
- **Scope-creep discipline (Insight #13):** equation-as-object helps chapter drafts stay at framework level ("CS = RCV − B; current regimes produce B < RCV") without sprawling into instrument-specific territory.

**Cross-reference to epistemic-humility discipline (Insight #14):**
The equation's statement "CS = RCV − B" is **framework-level prescription** (in-scope for Book 1 per v1.0.3). The equation does NOT commit to which specific instrument-mix realizes B. **Norway's sovereign wealth fund is the canonical real-world example of B approaching RCV;** the equation itself is the framework-level object that makes Norway's success measurable + that makes the American B << RCV gap visible. Book 1 presents the equation + points to Norway as best-existing-example + PONDERS Accountability Bond as one candidate direction — does NOT prescribe a specific instrument design as THE fix.

**Depends on (all these must hold for equation to hold):**
- CS definition (Ring 1) — mechanism/quantity.
- RCV definition (Ring 1) — integrand form ∫ᵗ₀^∞ {[1 − S(t|t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt.
- B definition (Ring 2) — full-Severed-Cost scope.
- Substitutability Function S (Ring 2) — appears in RCV integrand via C₁.
- Externality Tail E (Ring 2) — appears in RCV integrand.
- Abundance Masking + CIT (Ring 2/1) — govern which costs are admitted to RCV.
- Four Gates (Ring 2, pending) — admission apparatus for Cᵢ.

**Pairs with:**
- All component terms — equation is their combined structural anchor.
- Accountability-gap argument (the interpretive claim that CS > 0 in practice).
- Insight #14 epistemic-humility discipline (B = RCV is the ideal; Norway is canonical existing example; no single-instrument cure prescribed).

**Staleness triggers:**
- Any component definition changes in a way that affects the equation (stability-anchor function surfaces this immediately).
- CORE math restructured to use a different form (ratio, logarithm, multi-term).
- Academic adoption evidence shows gap-accounting form displaced by an alternative.

**Commit trail:**
- Individual rigor pass: this commit.
- Ratification + Terms Index record: this commit.

**Notes:**
- "CS = RCV − B" is the three-word / four-character / one-operator encapsulation of the framework's central claim. Maximum compressibility.
- Pedagogical role: readers who internalize the equation acquire the framework's central assertion in one expression.
- Rigor-infrastructure role: the equation acts as stability anchor — if later rigor weakens one component, the equation immediately surfaces the consequence for the whole.
- Scope-creep discipline: equation-as-object keeps chapter drafts at framework level rather than instrument-specific level (per Open Insight #13 + Insight #14).

---

### Intergenerational Pricing Gap (IPG)

**Working definition:** Ratio IPG = RCV / market_price — the factor by which markets underprice extraction at the point of transaction. "IPG = 33" means the market price covers approximately 3% of the true intergenerational cost captured in RCV. Framework-specific market-pricing-gap diagnostic, DISTINCT from Cost Severance (CS = RCV − B — accountability-pricing-gap diagnostic). Different diagnostic purpose, different denominator.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Glossary definition (~75 words, reader-register):**
> The ratio of true intergenerational cost (RCV) to market price. *IPG = 33* means today's price covers about 3% of the cost being passed forward. A market-pricing-gap diagnostic — distinct from Cost Severance, which measures what accountability instruments fail to cover. IPG > 1 is architectural for extraction; the empirical question is the magnitude. McDowell's IPG ≈ 33 is the book's canonical compression — readers remember a single number.

**Tech Appendix definition (~330 words, formal + lineage):**
> **IPG = RCV(R, t₀) / market_price(R, t₀)** — the dimensionless ratio of the framework's Residual Commons Value (true intergenerational cost) to the empirically observed market price at the transaction. Definitionally: IPG quantifies the factor by which markets underprice extraction at the point of transaction. *IPG = 33* (McDowell coal calibration) means the market price covers approximately 3% of the true intergenerational cost.
>
> **Distinguished from Cost Severance.** CS = RCV − B uses the framework's accountability primitive (B = Restitution Bond + Foreclosure Bond) — measures what accountability instruments fail to cover. IPG uses market price (external empirical reference) — measures what markets fail to price at transaction. The two diagnostics can diverge: Norway has small CS (sovereign-wealth-fund B ≈ RCV) but potentially large IPG (oil market price below true intergenerational cost AT transaction). Complementary, not redundant.
>
> **Architectural status.** IPG > 1 is partly architectural: RCV by construction includes intergenerational costs markets don't price, so IPG > 1 follows from the framework's primitive definitions. Empirical work calibrates the *magnitude* — not the direction. Ch 6 framing presents IPG > 1 as architecture + magnitude calibration, not as open empirical finding (per M12 honesty: overclaiming architectural facts as empirical discoveries would erode rigor integrity).
>
> **External-composite lineage.** IPG is the framework's canonical example of *external-composite* terms earning named status — a framework primitive (RCV) composed with an external empirical reference (market price). Per parsimony discipline ratified 2026-04-24, internal derivations (S_max, S(t)−S(t−1)) are NOT named; external-composites earn named status when load-bearing.
>
> **M12 lineage.** Ramsey 1928 (foundational intergenerational-discount framework, *Economic Journal*); Stern 2007 (*The Economics of Climate Change*); Nordhaus DICE model (multi-decade development, *American Economic Review* and successor venues); declining-discount-rate literature (Weitzman, Gollier, Portney-Weyant) for Tech Appendix depth. Adjacent intergenerational-pricing literature addresses *"markets underprice intergenerational costs"* qualitatively; no established work uses this specific RCV-as-numerator ratio form. IPG is framework-specific independent specialization.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 + §12.1 item 10 (commit `46600bc`) — Ring-2 classification with flag for individual rigor to test demote-to-Ring-3 alternative.
- Individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_ipg_v1.0.0.md` (2026-04-24, commit `256e34d`) — Option A (CONFIRM Ring 2) ratified 2026-04-24. Principle-#3 derivation check PASSES.

**M12 classification:** Independent specialization. Adjacent intergenerational-pricing literature (Ramsey 1928, Stern 2007, Nordhaus DICE, declining-discount work from Weitzman/Gollier/Portney-Weyant) addresses "markets underprice intergenerational costs" qualitatively; no established work uses this specific ratio form with RCV-as-numerator. Framework-specific diagnostic composite.

**M12 citations (for Tech Appendix §L methodological footnote):**
- Ramsey, Frank P. "A Mathematical Theory of Saving" (1928) — foundational intergenerational-discount framework.
- Stern 2007 + Nordhaus DICE — already in bibliography for Externality Tail; cross-reference.
- Declining discount rate literature — optional Tech Appendix depth.

**Distinguishing from CS:**
- **CS uses B** (Accountability Bond — all accountability-instrument dollars; framework primitive). Measures what's not internalized by accountability mechanisms.
- **IPG uses market_price** (transaction price — external empirical reference). Measures what's not priced by markets at transaction time.
- Can diverge: Norway has small CS (sovereign wealth fund captures B ≈ RCV post-transaction) but potentially large IPG (oil market price below true intergenerational cost AT transaction). Complementary diagnostics.

**Parsimony-principle corollary established (ratified 2026-04-24):**
- **Internal derivations** (framework primitives only): NOT named (per CSG retirement — S_max, S(t)−S(t−1), etc.).
- **External-composites** (framework primitive composed with external empirical reference): CAN earn named-object status when load-bearing.
- IPG is canonical example of external-composite earning named status.
- Worth flagging as possible Principle #6 sub-corollary if pattern repeats.

**Epistemic-honesty note (for Ch 6 framing, ratified 2026-04-24):**
- "IPG ≫ 1 universally" is PARTLY by construction — RCV includes intergenerational costs markets don't price, so IPG > 1 is architectural for extraction cases.
- Empirical work quantifies MAGNITUDE (McDowell IPG = 33), not direction.
- Ch 6 convergence-table framing should present as "architecture + magnitude calibration," not "open empirical finding." Overclaiming the architectural-fact as empirical-discovery would be a rigor-integrity risk.

**Why Ring 2 (not Ring 3 demote per meta-pass flag):**
- Distinct diagnostic from CS (different denominator, different diagnostic purpose).
- 15+ active chapter/guidance refs + dedicated WS12 decision doc.
- Convergence-table pedagogy (Ch 6) depends on IPG as compressed scalar ("IPG = 33" is framework's canonical empirical compression).
- "IPG ≫ 1" architectural claim deserves a named handle.

**Depends on:**
- RCV definition (numerator — framework primitive).
- Market-price measurement (denominator — external empirical reference).
- Cost Severance (IPG is complementary diagnostic, not synonym).

**Pairs with:**
- CS = RCV − B (complementary gap diagnostic — different denominator).
- RCV (direct component).
- Accountability-gap narrative (IPG quantifies market-pricing-gap at transaction time; CS quantifies what accountability instruments cover).

**Staleness triggers:**
- RCV definition restructured.
- Framework develops more precise pricing-gap diagnostic that displaces.
- Empirical work reveals "IPG ≫ 1" not universal (would change both architectural claim and IPG's role).

**Commit trail:**
- Individual rigor pass: commit `256e34d` (2026-04-24).
- Ratification + Terms Index record: this commit.

**Notes:**
- Convergence-table pedagogy: 4 approaches converge on IPG ≫ 1. Chapter's numerical center of gravity.
- McDowell IPG = 33 (market covers ~3% of true cost) is framework's canonical empirical compression — readers remember single-number claim.
- WS12 IPG data table (`alignment/decisions/ws12-ipg-data-table-for-reconciliation.md`) is load-bearing for case-study cross-comparison.

---

### Commons Inversion Test (CIT) [supersedes AIT 2026-04-24]

**Working definition:** Framework-specific Ring-1 methodology for admitting candidate costs to RCV. Operates on commons categories: imagine the commons inverted (either absent or unconsumed); if the candidate cost becomes visible as commons-dependent, admit to Cᵢ via Four Gates. Two sub-forms:
- **Commons-Absence Inversion** — imagine commons not existing (paradigm: oxygen in space; McDowell habitability destroyed by coal extraction). Operational question: *what would it take to replace the commons?*
- **Commons-Consumption Inversion** — imagine commons not consumed (paradigm: commute-time returned; forest uncut). Operational question: *what could the commons do if not drawn down?*

Specialized extension of commons-governance methodology (Ostrom lineage) to extraction-contexts where commons are drawn down rather than managed-in-place.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn). Supersedes AIT.

**Glossary definition (~75 words, reader-register):**
> The framework's discovery method for identifying which costs of extraction belong in the accounting. The **Commons Inversion Test** asks of a candidate cost: imagine the commons that grounds it is absent or unconsumed. If the cost becomes visible only against that imagined inversion, it is commons-grounded and admits to the framework's accounting. If the cost would persist regardless, it is intrinsic to the activity, not to the commons-state, and is excluded.

**Tech Appendix definition (~310 words, formal + lineage):**
> A framework-specific methodology for admitting candidate costs to the RCV integrand. The Commons Inversion Test (CIT) is the discrimination gate that filters cost claims for commons-grounding before they reach the measurement apparatus. Two operational sub-forms:
>
> **Commons-Absence Inversion (CAI)** asks whether the cost claim is commons-grounded at all. The operation: imagine the commons does not exist. The cost the test surfaces is replacement cost — what it would take to recreate or compensate for what was destroyed. Paradigm cases: McDowell County's habitability commons demonstrably stripped by coal extraction; atmospheric oxygen that feels free on Earth and must be priced when imagined absent (the asteroid-mining test in Chapter 7).
>
> **Commons-Consumption Inversion (CCI)** asks whether the commons-grounded claim is consumption-of-finite-commons. The operation: imagine the commons not being consumed. The cost the test surfaces is opportunity cost — what the commons would have done if not drawn down. Paradigm cases: lifetime hours that could have gone to language-learning or family-time if not spent commuting; a forest functioning as carbon sink and watershed if not cut.
>
> The two sub-forms run different filters. CAI distinguishes commons-grounded claims from private-property externalities. CCI distinguishes consumption-of-finite-commons claims from coordination-of-mutually-acceptable-use claims. A single-form CIT would have collapsed these into one test and produced ambiguous results in Ostrom-tradition cases where CAI passes but CCI fails. The two-sub-form architecture makes the routing explicit.
>
> M12 lineage: specialized extension of commons-governance methodology (Ostrom 1990 *Governing the Commons*; Hess & Ostrom 2007 *Understanding Knowledge as a Commons*) into extraction-contexts where commons are drawn down rather than managed-in-place. The counterfactual-reasoning operational family (Lewis 1973 + subsequent philosophy-of-action literature) supplies the thought-experiment lineage. CIT supersedes AIT (Abundance Inversion Test) per the CIT rename rigor pass 2026-04-24; AIT's semantic content preserved + refined via the two sub-forms.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Author structural-identity insights 2026-04-24 — commons-as-structural-identity + AIT-as-CIT realizations.
- Commons-as-Structural-Identity rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_commons_as_structural_identity_v1.0.0.md` (commit `c4b09dc`) — broader reframing including CIT rename + 10-as-commons-categories. Option A ratified.
- Dedicated CIT rename rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md` (commit `b294c79`) — Option A (ratify CIT) ratified with full M12 audit + sub-form formalization.
- 10-Commons-List Dissolution rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_10_commons_list_dissolution_v1.0.0.md` (commit `e30087e`) — Option C' ratified (10 as examples-not-canonical; methodology-forward; political-philosophical acknowledgment).

**M12 classification:** Original specialization within counterfactual-reasoning methodological family. No prior-art collision on phrase or concept; acronym collisions in unrelated domains only (spell-out-at-first-use convention mitigates).

**M12 citations (for Tech Appendix methodological footnote):**
- Ostrom 1990 *Governing the Commons* — commons-governance lineage.
- Hess & Ostrom 2007 *Understanding Knowledge as a Commons* — knowledge commons extension; precedent for extending commons to novel domains.
- Counterfactual reasoning family (Lewis 1973 + subsequent philosophy-of-action literature) — operational lineage.

**Supersedes:** AIT (Abundance Inversion Test). AIT's semantic content preserved + refined via two sub-forms; name updated to match operational instruction (commons-inversion, not abstract abundance-inversion).

**Depends on:** commons-governance tradition (Ostrom lineage); commons as structural identity of formerly-named-abundances; Four Gates admission apparatus; "abundance" as state-name of each commons.

**Pairs with:**
- RCV (Ring 1) — CIT admits costs to RCV integrand.
- Four Gates (Ring 2) — CIT is one of four admission gates.
- Abundance Masking (Ring 2) — CIT detects what Abundance Masking hides.
- Cᵢ (Ring 1) — CIT-admitted costs become Cᵢ entries.
- Commons categories (the 10 examples) — CIT operates on each commons.

**Staleness triggers:**
- Commons-as-structural-identity reframing reversed.
- New methodology replaces CIT.
- Academic adoption evidence shows CIT failing to travel.

**Commit trail:**
- Commons-as-Structural-Identity pass: commit `c4b09dc` (2026-04-24).
- Dedicated CIT rename pass: commit `b294c79` (2026-04-24).
- 10-list dissolution pass: commit `e30087e` (2026-04-24).
- Ratification + Terms Index record: this commit.

**Notes:**
- "Commons Inversion Test" at first-use per chapter; "CIT" as acronym after. Framework convention per AIT precedent.
- Two sub-forms formalized as framework methodology contribution beyond rename — see Tech Appendix methodology section + Open Insight #16.
- Commute-story (Personal Stories Candidate #1) is the paradigm Commons-Consumption case; most resource-extraction cases are Commons-Absence; some (mining) exercise both.

---

### Abundance Inversion Test (AIT) — RETIRED

**Status:** RETIRED 2026-04-24. Superseded by **Commons Inversion Test (CIT)** per commons-as-structural-identity reframing. AIT's semantic content preserved + refined in CIT (see CIT entry above).

**Why:** author insight 2026-04-24: *"AiT is really CiT showing that a commons cost exists when you imagine the current abundance of that commons not existing."* The test operates on commons (concrete shared resources), not on abstract abundance-states. CIT's framing makes the operational instruction visualizable; AIT required reader-side abstraction. Plus the two sub-forms (Commons-Absence + Commons-Consumption Inversion) became visible only after the commons-reframing.

**Full trace:** `archive/retirements/index.md` §1 + ratifying rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md` + Commons-as-Structural-Identity + 10-list dissolution rigor passes.

---

### Abundances → Commons Categories (10-element example record) — UPDATED 2026-04-24

**Working definition (v1.2 — supersedes v1.1 from earlier-this-session Abundances pass):** The 10 commons categories the framework has examined across the 18 cases of this book's research: Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy. **These are EXAMPLES, not a canonical or exhaustive enumeration.** Each names a commons whose abundance state CIT can invert to reveal scarcity-grounded costs. "Abundance" is the STATE of each commons (abundant vs scarce), not the commons itself.

**Status:** `CURRENT` as **examples-record reference** at Ring 2 (ratified 2026-04-24 by Chris Winn — Option C' middle path with political-philosophical acknowledgment).

**Glossary definition (~80 words, reader-register):**
> The ten kinds of commons the framework has examined across the 18 cases in this book — Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political, Cohesion, Epistemic, Autonomy. They are *examples*, not a closed list. When McDowell County loses generations of healthy lung tissue, that is the **Habitability commons** being extracted. When a coal town loses its civic life, that is **Cohesion**. Different political traditions disagree about what counts as a commons; the framework's methodology works within any of them.

**Tech Appendix definition (~300 words, formal + lineage):**
> The 10 commons categories surfaced by Commons Inversion Test (CIT) application across the 18 cases of this book's research: Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political, Cohesion, Epistemic, Autonomy. The list is an examples-record reference, not a canonical or exhaustive enumeration. Each category names a class of commons whose abundance state CIT can invert to reveal scarcity-grounded costs admissible to the RCV integrand under the Four Gates discipline.
>
> Architectural status (Option C' ratified 2026-04-24): the 10 are framework EXAMPLES — what CIT has surfaced across the cases examined — not framework SCAFFOLDING (load-bearing architecture). The framework's universality claim is about METHODOLOGY (CIT operates wherever extraction acts on commons-like resources), not about enumeration canonicity. Reader application may surface different or additional commons categories in different contexts; the framework is generative and politically-pluralistic.
>
> Political-philosophical acknowledgment (load-bearing): what counts as a commons is politically-traditionally contested. Classical liberalism (autonomy as individual natural-right); civic republicanism (Pettit / Skinner — autonomy as non-domination requiring shared institutions); socialist/communitarian (autonomy enabled by shared infrastructure); Marxist (material-conditions dependent); lived-oppression perspectives (autonomy as denied/extracted); dominant-class perspectives (autonomy as individual privilege). The framework does not argue a universal ontology of what IS a commons; it argues that when any of these operate AS commons in a given society, extraction severs cost from that commons and CIT measures the severance.
>
> M12 lineage: Ostrom 1990 *Governing the Commons*; Hess & Ostrom 2007 *Understanding Knowledge as a Commons*; Klinenberg 2018 *Palaces for the People*; Anderson 2017 *Private Government* (civic-republican autonomy framing); Polanyi 1944 *The Great Transformation* (commons-disembedding lineage). Per-commons rich profiles preserved in methodology doc v1.4.0.

**Term-spec version:** v1.2 (supersedes v1.1 "scaffolding construct" framing → "examples-record reference" per Option C' refinement).

**Last reviewed:** 2026-04-24

**Key reframing (Option C' specific):**
- The 10 are NOT framework scaffolding (load-bearing architecture).
- The 10 ARE framework EXAMPLES — what CIT has surfaced across the 18 cases examined.
- Framework's UNIVERSALITY claim is about METHODOLOGY (CIT works wherever extraction operates on commons-like resources), NOT about enumeration canonicity.
- Different political traditions have different commitments about what IS a commons; the framework accommodates rather than settles this contestation.
- Reader application may surface different or additional commons categories in their context; framework is generative + politically-pluralistic.

**Rigor provenance:**
- Path F rigor pass — variables-not-dimensions reframing.
- Naming-cohort rigor passes 2026-04-22 (per-element rigor) preserved.
- Commons-as-Structural-Identity rigor pass (commit `c4b09dc`) — abundances → commons categories.
- 10-Commons-List Dissolution rigor pass (commit `e30087e`) — Option C' ratified: examples-not-canonical + political-philosophical acknowledgment.

**Political-philosophical acknowledgment (load-bearing for Ch 1 + Tech Appendix):**

What counts as a commons is politically-traditionally contested:
- **Classical liberalism** — autonomy as individual natural-right; supporting infrastructure enabling but not commons.
- **Civic republicanism** (Pettit/Skinner) — autonomy as non-domination; requires shared institutions; commons-like dependence.
- **Socialist/communitarian** — autonomy as enabled by shared infrastructure; the enabling conditions ARE commons.
- **Marxist** — autonomy material-conditions dependent.
- **Lived-oppression perspective** (slave, colonized, repressed worker) — autonomy as something denied/extracted, not shared commons.
- **Dominant-class perspective** — autonomy as individual privilege.

Framework doesn't argue universal ontology of what IS a commons. Argues: when any of these operate AS commons in a given society, extraction severs cost from that commons; CIT measures the severance. **Universality of method, examples of application, political-traditional-agnosticism on specific commons-ontology.**

Politically-contested commons especially: Autonomy (Anderson 2017 *Private Government* civic-republican framing); Political (rules of voice + representation contested); Kindred (Western nuclear vs collectivist kinship norms contested); Epistemic (knowledge-as-commons vs knowledge-as-property contested).

**Why Ring 2 (not Ring 1):** examples-record reference is framework-internal; not a public-adoption target.

**Recommended authorial-voice positioning** (for Ch 1 / Ch 6):
> *"This framework doesn't argue that autonomy is universally a commons, or that habitability is, or that time is. It argues that when any of these operate AS commons in a given society — shared, depended-on, collectively enabling — extraction can sever cost from that commons, and this methodology measures the severance. Different political traditions have different commitments about what is shared and what is individual. The framework works within any of those commitments. What it doesn't accept is extraction without accountability, regardless of which commons is being extracted from."*

**Depends on:**
- CIT methodology (operates on examples).
- Path F generative framework architecture.
- Per-commons rich profiles (preserved in methodology doc v1.4.0).
- Bibliography commons-governance lineage (Ostrom + Hess + Klinenberg + Anderson + Polanyi).

**Pairs with:**
- CIT (Ring 1) — examples illustrate methodology.
- Abundance Masking (Ring 2) — operates across commons examples.
- Cᵢ (Ring 1) — admitted via CIT operating on commons.

**Staleness triggers:**
- Commons-as-structural-identity reversed.
- New examples surfaced via CIT framework application.
- Political-philosophical positioning challenged in academic reception.

**Commit trail:**
- Commons-as-Structural-Identity pass: commit `c4b09dc`.
- 10-list dissolution pass: commit `e30087e`.
- Ratification + Terms Index update: this commit.

**Notes:**
- Phase A3 Stream A sweep targets: glossary v3 → "Commons categories (examples)" entry; methodology doc rename v1.3.0 → v1.4.0; chapter audit + case-study audit framed as reproducibility record (preserved); Ch 6 restructured methodology-forward.
- Per-commons rich profiles (v1.2.0 naming-cohort work) preserved in methodology doc — NOT chapter prose. Per Open Insight #13 (scope-creep monitoring), per-commons depth = Tech Appendix not chapters.
- Autonomy-as-commons specifically gets explicit political-philosophical acknowledgment in Ch 1 + Ch 6 + Tech Appendix per Open Insight #18.

---

### Cost Severance Damages (CSD)

**Working definition:** Backward-looking framework instrument measuring realized human harm from cost severance — health damages, intergenerational disadvantage, community-level suffering, foreclosed life-trajectories. Distinct from RCV (forward-looking resource permanent-foreclosure measurement). The framework's two-instrument architecture (per Three Ways + RCV Formal-Model rigor pass Block 1, ratified 2026-04-24): CSD measures damages-to-people; RCV measures damages-to-resource. Together they constitute Total Extraction Damages.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Glossary definition (~80 words, reader-register):**
> The framework's measurement instrument for already-realized human harm from cost severance — health damages, intergenerational disadvantage, community-level suffering, foreclosed life-trajectories. **Cost Severance Damages (CSD)** is backward-looking; it counts what extraction has already done to people. Companion to Residual Commons Value, which is forward-looking and counts what extraction forecloses for future generations. Together: CSD prices what's been taken from people; RCV prices what's been taken from the resource.

**Tech Appendix definition (~310 words, formal + lineage):**
> Backward-looking framework instrument measuring realized human harm from cost severance: health damages, intergenerational disadvantage, community-level suffering, foreclosed life-trajectories. CSD is the framework's specific measurement instrument for the human-harm component of Severed Cost.
>
> Two-instrument architecture per Three Ways + RCV Formal-Model rigor pass Block 1 (ratified 2026-04-24): CSD measures damages-to-people (already-realized; person-affecting); RCV measures damages-to-resource (forward-looking; impersonal-outcomes per Parfit 1984). Together they constitute Total Extraction Damages = CSD + uncaptured RCV (Block 3 framework decomposition). The two instruments are orthogonal: full reparations on the human-harm side leave the resource still gone (Block 1 Hole 5).
>
> Pairs with B₁ (Restitution Bond, Ring-2 sub-instrument): the accountability instrument that closes the CSD gap. Where CSD diagnoses the realized harm, B₁ posts the dollars that would discharge it.
>
> M12 lineage: independent specialization with established-methodology lineage. Adopts:
> - **Reparations-economics methodology** (Darity & Mullen 2020 *From Here to Equality*) — wealth-gap-against-comparable-households calculation; the contemporary state of the art for pricing harm structurally embedded in economic systems.
> - **Environmental-justice damages** (Bullard 1990 *Dumping in Dixie*) — distributional analysis of environmental harm across racial / socioeconomic / geographic lines.
> - **Intergenerational-mobility methodology** (Chetty et al.) — quantifying foreclosed life-trajectories through opportunity-mobility data.
> - **VSL / DALY health-economics** — value-of-statistical-life and disability-adjusted-life-year frameworks for pricing health harm at scale.
>
> Framework's contribution is the extraction-community-context specialization + the two-instrument architecture integration. Implicit operation across seven demonstrated cases (McDowell coal; healthcare end-of-life; opioid Appalachia; 2008 financial crisis; Chesapeake watermen; Libby vermiculite; tax-tradeoff US-Sweden welfare-state comparison).

**Term-spec version:** v1.0 (first sanctioned spec; supersedes implicit-operation status across 7+ framework cases).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Three Ways + RCV Formal-Model rigor pass Block 1 (commit `1c8e4dd`, 2026-04-24) — surfaced CSD as hidden Ring-2 element via two-instrument architecture.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`, 2026-04-24) — promotion commissioned by Chris Winn directive.
- CSD individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_csd_v1.0.0.md` (commit `98fc8e6`, 2026-04-24) — Option A (Ring 2) ratified by Chris Winn 2026-04-24 with Principle-#3 distinctness check + M12 audit + 7-case implicit-operation evidence.

**M12 classification:** Independent specialization with established-methodology lineage. Adopts reparations-economics (Darity & Mullen 2020) wealth-gap-against-comparable-households methodology + VSL/DALY health-economics + intergenerational-mobility (Chetty et al.) + extends into extraction-community contexts via two-instrument architecture.

**M12 citations (LOAD-BEARING for Tech Appendix):**
- Darity, William A., Jr., & Mullen, A. Kirsten. *From Here to Equality* (UNC Press 2020) — already in bibliography §18.5.
- Bullard, Robert D. *Dumping in Dixie* (Westview 1990) — already in bibliography §7. Environmental-justice cross-reference.
- Chetty, Raj, et al. — already in bibliography §4. Intergenerational-mobility cross-reference.
- VSL/DALY methodology references — Tech Appendix v0.0.5.

**Why Ring 2 (not Ring 1):**
- Framework-internal architecture; readers learn it; non-readers don't adopt CSD as travel-ready vocabulary.
- Adoption-bet focus on Ring-1 flagships (Commons Bonds + Cost Severance + Severed Cost + Value Extraction + RCV + Cᵢ + CIT) preserved.

**Why Ring 2 (not subsumed under Cost Severance / Severed Cost):**
- Cost Severance = mechanism noun; Severed Cost = quantified result noun; CSD = specific measurement instrument for the human-harm component of result. Three different conceptual layers; instrument-layer warrants separate record.

**Implicit operation in framework cases (7 demonstrated; preserved in CSD rigor pass §2.2):**
- McDowell coal — life-expectancy gap, Black Lung, community-collapse mortality, intergenerational mobility loss
- Healthcare end-of-life — family-caregiver labor-time, patient-suffering, financial depletion
- Opioid Appalachia — overdose deaths, family destruction, multi-generational trauma, foster-care overload
- 2008 financial crisis — 10M foreclosures, retirement-cohort wealth destruction, racial wealth-gap effects
- Chesapeake watermen — multi-generational livelihood-loss, community-cohesion erosion
- Libby vermiculite — multi-decade asbestos health damages
- Tax-tradeoff (US-Sweden) — welfare-state-architecture-driven life-outcome disparities

**Pairs with:**
- RCV (Ring 1) — companion forward-looking instrument; orthogonal measurement (Block 1 Hole 5: full reparations leave the resource still gone).
- B1 (Restitution Bond, Ring-2 sub-instrument; ratified 2026-04-24 per B1 + B2 naming rigor pass commit `8e6a5b2`) — accountability instrument that closes CSD gap.
- Cost Severance (Ring 1) — mechanism CSD measures damages from.
- Severed Cost (Ring 1) — quantified result; CSD is the backward-looking measurement of its human-harm component.
- Total Extraction Damages = CSD + uncaptured RCV (Block 3 framework decomposition).

**Staleness triggers:**
- Two-instrument architecture (Block 1) reversed.
- CSD methodology displaced by superior measurement framework.
- Reparations-economics field develops a different framing that supersedes wealth-gap-against-comparable-households methodology.

**Commit trail:**
- Three Ways + RCV Formal-Model pass: commit `1c8e4dd`.
- Three Ways + RCV Formal-Model ratification + bibliography additions: commit `66becc5`.
- CSD individual rigor pass: commit `98fc8e6`.
- Ratification + Terms Index record: this commit.

**Open Insights:**
- **Open Insight #19** (CSD-RCV correlation hypothesis) — the framework's deepest empirical claim that CSD and uncaptured RCV correlate across extraction cases; remains hypothesis pending Block 4 validation execution.

**Notes:**
- CSD is the framework's most-empirically-validated measurement instrument — reparations-economics + environmental-justice + health-economics traditions have decades of methodology development.
- Norway's welfare-state architecture is approximately B1-for-Norwegian-citizens; framework's CSD measurement of climate-extraction damages on non-Norwegian populations remains uncompensated.
- Phase A3 sweep targets: Ch 5 prose; Tech Appendix v0.0.5 formalism; Glossary v3 entry.

---

### Hotelling Identity (framework's extension of Hotelling 1931)

**Working definition:** The framework's articulation that the gap between commons' true cost of extraction (RCV) and extractor's market-priced scarcity premium (Hotelling rent) IS, by definition, the per-unit Cost Severance: **RCV − Hotelling rent = Cost Severance per unit.** Bridge between framework vocabulary and standard resource-economics math.

**INTELLECTUAL HONESTY — clear attribution of components (per author M12 directive 2026-04-24):**

- **Hotelling's part** (Hotelling 1931): resource rent = market price − extraction cost (p − c); the rent rises over time at rate of interest; this rent represents the EXTRACTOR's scarcity premium accruing as the resource depletes. Standard resource-economics; foundational.
- **Framework's part:** (a) defining RCV as the COMMONS' true cost of extraction (forward-looking; integrand over substitutability + externality + abundance-grounded costs admitted via Four Gates); (b) recognizing that Hotelling rent under honest accounting represents commons' scarcity value being APPROPRIATED by extractor (rather than compensated to the commons); (c) articulating the identity: RCV − Hotelling rent = CS per unit. The identity is framework's articulation; Hotelling didn't write it (didn't have RCV; didn't have Cost Severance as named mechanism).

The framework EXTENDS Hotelling 1931 by adding a commons-side measurement to pair with Hotelling's extractor-side rent + naming the gap as the framework's central concept (Cost Severance).

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn with explicit extension-positioning discipline).

**Glossary definition (~80 words, reader-register):**
> The framework's mathematical bridge to standard resource economics. Hotelling 1931 priced the rent that accrues to a private extractor as a finite resource depletes — the gap between price and extraction cost, rising over time. The framework's **Hotelling Identity** says: that same rent, looked at from the commons' side, is the cost severance per unit. Per-unit Residual Commons Value minus per-unit standard Hotelling rent equals per-unit Cost Severance. Hotelling's math; framework's commons-side reading.

**Tech Appendix definition (~330 words, formal + lineage):**
> A framework-articulated identity bridging the framework's commons-side measurement (RCV) to standard resource economics' extractor-side rent rule (Hotelling 1931):
>
> **RCV − Hotelling rent = Cost Severance per unit**
>
> M12 attribution discipline (per Hotelling Identity rigor pass §3 + author M12 directive 2026-04-24):
>
> *Hotelling's part* (Hotelling 1931 *The Economics of Exhaustible Resources*): resource rent = market price − extraction cost (p − c); the rent rises over time at the rate of interest; this rent represents the **extractor's** scarcity premium accruing as the resource depletes. Standard resource-economics; foundational.
>
> *Framework's part:* (a) defining RCV as the **commons'** true cost of extraction (forward-looking integrand over substitutability + externality + commons-grounded costs admitted via Four Gates); (b) recognizing that Hotelling rent under honest accounting represents commons' scarcity value being **appropriated** by the extractor (rather than compensated to the commons); (c) articulating the identity RCV − Hotelling rent = CS per unit. The identity is the framework's articulation; Hotelling did not write it (he did not have RCV; he did not have Cost Severance as named mechanism).
>
> The framework extends Hotelling 1931 by adding a commons-side measurement to pair with Hotelling's extractor-side rent + naming the gap as the framework's central concept (Cost Severance). Adjacent literature deepening the extension: Solow 1974 (intergenerational equity and exhaustible resources); Hartwick 1977 (invest resource rents in reproducible capital — operationalized in Norway's sovereign-wealth fund); Pearce-Atkinson 1993 (sustainability accounting / capital-theory extension); Daly's stock-flow accounting tradition.
>
> Mathematical bridge, not adoption-target vocabulary. Ring 2 placement honors M6 academic-positioning value: transforms the M11 critic's *"isn't this rebranding externality theory?"* attack into structural identification — the framework names the gap Hotelling's framing identifies but does not price.

**Term-spec version:** v1.0.

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Three Ways + RCV Formal-Model rigor pass Block 3 (commit `1c8e4dd`) — Hotelling Identity surfaced.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`) — promotion commissioned.
- Hotelling Identity individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_hotelling_identity_v1.0.0.md` (commit `5b8ff42`) — Option A (Ring 2 promote) with §3.2 Tech Appendix specification framing for the appropriated-commons-value interpretation.
- Author M12 challenge round 1 (2026-04-24): *"note 'Hotelling Identity' isn't my idea it's Hotelling, correct? we are just citing it and leveraging it within our formula."*
- Author M12 resolution round 2 (2026-04-24): *"ratify = Hotelling Identity Ring 2 promotion... but again, it's not my work so just cite it and then use it and call out how my work extends / adds to his work."*
- Ratification 2026-04-24 by Chris Winn — this commit. Ring 2 promotion ratified WITH extension-positioning discipline.

**M12 classification:** Independent specialization with foundational lineage extension. Hotelling 1931 is the foundation (clearly attributed); framework's identity-articulation + RCV-as-Hotelling-complementary-measurement is the extension (clearly attributed). NOT framework coinage of the underlying resource-rent concept.

**M12 citations (LOAD-BEARING):**
- **Hotelling, Harold. "The Economics of Exhaustible Resources." *Journal of Political Economy* 39, no. 2 (1931): 137–175.** — foundational; in bibliography §18.5.

**Optional Tech Appendix depth additions:**
- Solow 1974 — intergenerational equity and exhaustible resources.
- Hartwick 1977 — invest resource rents in reproducible capital (Norway sovereign-fund operationalization).
- Pearce-Atkinson 1993 — sustainability accounting / capital-theory extension.
- Daly's stock-flow accounting — already in bibliography §3.

**Why Ring 2 (not Ring 1):**
- Mathematical bridge, not adoption-target vocabulary.
- Lawyers + policymakers don't adopt mathematical identities directly; they adopt the framework concepts (Severed Cost; Cost Severance; Commons Bonds) the identity supports.

**Why Ring 2 with extension-positioning discipline:**
- Ring 2 placement honors the identity's M6 academic-positioning value (transforms M11 critic's *"isn't this rebranding externality theory?"* attack into structural identification).
- Extension-positioning honesty (Hotelling's part vs framework's part clearly attributed in this record + Tech Appendix passage) prevents the overclaim that the framework "coined" Hotelling's foundational work.
- Bibliography Hotelling 1931 entry is correct attribution at scholarly level.

**Pairs with:**
- RCV (Ring 1) — numerator in identity; framework's measurement.
- Hotelling rent (resource-economics term; Hotelling 1931) — subtractend; clearly Hotelling's contribution.
- Cost Severance equation CS = RCV − B (Ring 2) — Hotelling Identity is the per-unit specialization for standard-economics framing.
- Cost Severance mechanism (Ring 1) — what the identity ultimately characterizes per-unit.

**Tech Appendix v0.0.5 publication required:**
- Hotelling 1931 lineage citation + clear attribution.
- Per-unit per-period form: RCV(t) − Hotelling-rent(t) = CS(t).
- Integrated form: ∫RCV(t) dt − ∫Hotelling-rent(t) dt = ∫CS(t) dt.
- Hotelling-rent-as-appropriated-commons-value interpretive passage: under honest accounting, Hotelling rent represents commons' scarcity value being appropriated by extractor rather than compensated to commons.
- Framework-extends-Hotelling positioning (Hotelling's part + framework's part clearly attributed).

**Staleness triggers:**
- Hotelling 1931 framework displaced in resource economics (not expected; foundational status).
- Framework restructures CS equation in ways that change identity form.
- Tech Appendix specification reveals identity holds only under restricted assumptions.

**Commit trail:**
- Three Ways + RCV Formal-Model pass: commit `1c8e4dd`.
- Three Ways ratification + Hotelling 1931 added to bibliography: commit `66becc5`.
- Hotelling Identity individual rigor pass: commit `5b8ff42`.
- Ratification + Terms Index record: this commit.

**Notes:**
- The identity transforms M11 critic's "rebranding externality theory" attack into structural identification — framework asserts the algebraic complement to Hotelling 1931.
- M6 academic-positioning value is high; extension-positioning discipline preserves the value while honestly attributing components.
- Captured lesson (per Hotelling Identity rigor pass §8): when ratifying Ring placement for elements that EXTEND established work, Terms Index records must explicitly distinguish (a) foundational component cited and (b) framework's specific contribution. This protects against accidental over-claim while preserving framework's legitimate extension contribution.

---

### Three Ways of Counting (formerly "Triangulated RCV Estimation"; renamed 2026-04-28)

**Working definition:** Three-method estimation methodology for RCV producing a defensible range rather than a single point estimate. Method 1 (Replacement Cost lower bound) + Method 2 (Norway Revealed Preference middle-anchor within triangulation) + Method 3 (Scarcity-Adjusted Option Value upper bound). Convergence reduces uncertainty; divergence reveals where real disagreements live (substitutability vs scarcity-rate vs option-value parameter dominance). The methodology's output is described inline as *"the triangulated three-method range."*

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — methodology unchanged; renamed 2026-04-28 by Chris Winn from "Triangulated RCV Estimation" to "Three Ways of Counting" per `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-28_triangulated_rcv_estimation_naming_review_v1.0.0.md` Option B verdict — drop redundant formal name; promote pedagogical alias to primary methodology name; preserve "the triangulated three-method range" as inline result description; vocabulary footprint reduces by one Ring-2 term per Working Principle #1 parsimony).

**Supersession record:** "Triangulated RCV Estimation" (proper-noun coined 2026-04-24) RETIRED 2026-04-28 as redundant with "Three Ways of Counting" pedagogical name. Methodology, three sub-methods (Replacement Cost / Revealed Preference / Scarcity-Adjusted Option Value), convergence/divergence diagnostic, reporting discipline all preserved unchanged. Tier verdict reaffirmed at Ring 2 / Tier D under "Three Ways of Counting" (chapter title pattern-matches accessible academic-trade convention per Mazzucato / Raworth / Anderson lineage).

**Glossary definition (~80 words, reader-register):**
> The framework's discipline for estimating Residual Commons Value: instead of a single point estimate, run three independent methods and report the convergence range. **Three Ways of Counting** runs Replacement Cost (what would it cost to replace what was lost?), Revealed Preference (what did the most-honest existing example actually capture?), and Scarcity-Adjusted Option Value (what's the option value of leaving it in situ?). Where the three methods converge, the answer is robust. Where they diverge, the parameter pulling them apart names the real argument.

**Tech Appendix definition (~310 words, formal + lineage):**
> Three-method estimation methodology for Residual Commons Value producing a defensible range rather than a single point estimate. Each method has independent epistemological grounding; convergence reduces uncertainty; divergence reveals which parameters are doing the load-bearing work in any particular case.
>
> **Method 1 — Replacement Cost (lower bound):** RCV_min per unit ≥ replacement cost from nearest substitute − market price at extraction. Lineage: Costanza et al. 1997 ecosystem-services valuation + standard regulatory cost-benefit analysis + eminent-domain takings law. Boundary check: low for substitutable resources (e.g., common construction sand); severe for irreplaceable resources (e.g., helium for cryogenic applications). Correct directional differentiation across the substitutability spectrum.
>
> **Method 2 — Revealed Preference (middle-anchor within triangulation):** Norway sovereign-fund-captured value ÷ total barrels extracted = per-barrel captured value; gap between this and true cost = empirical measure of uncaptured RCV. Sidesteps the discount-rate debate (empirical not philosophical). Per Open Insight #14 epistemic-humility ratification: Norway did not fully capture RCV either (climate damages externalized; future-uses option-value uncaptured). Method 2 functions as Norway-anchored middle within the triangulation; not absolute middle of true RCV.
>
> **Method 3 — Scarcity-Adjusted Option Value (upper bound):** Real-options-theory foundation per Dixit & Pindyck 1994. Prices the option value of leaving the resource in situ given uncertainty about future substitutability + future demand + future applications not yet invented. Requires parameter calibration that ranges across two orders of magnitude in plausible values; Method 3's α-dominance finding (Block 4 sensitivity analysis) demonstrates that asymmetric-regret structure is the dominant pattern for Earth-bound civilization-scale extractions.
>
> Reporting discipline: every RCV estimate reports all three methods individually plus the convergence range plus identified divergence sources. No single-method RCV claim has standing in the framework's accounting. The triangulation operationalizes the framework's commitment to expressing uncertainty in a form that supports decisions rather than hiding it behind a headline number.

**Term-spec version:** v1.0.

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Three Ways + RCV Formal-Model rigor pass Block 2 (commit `1c8e4dd`) — methodology surfaced.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`) — promotion commissioned.
- Triangulated RCV Estimation individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_triangulated_rcv_estimation_v1.0.0.md` (commit `4f48c48`) — Option A (Ring 2 promote) verified with three method sub-tests + triangulation-discipline check + integration check.
- Ratification 2026-04-24 by Chris Winn — this commit.

**M12 classification:** Independent specialization within established estimation methodology traditions. Each method adopts standard methodology; triangulation discipline is standard validation. Framework's contribution is the SPECIFIC THREE METHODS chosen + convergence/divergence diagnostic + integration with Two-Instrument Architecture (CSD ↔ B1; RCV ↔ B2).

**M12 citations:**
- Costanza, Robert, et al. *Nature* 1997 — Method 1 replacement-cost methodology lineage. (Optional Tech Appendix addition.)
- Hartwick 1977 + Solow 1974 — Method 2 Hartwick-rule + intergenerational-equity lineage. (Optional Tech Appendix addition.)
- Dixit & Pindyck 1994 — Method 3 real-options-theory foundation. Already in bibliography §16.
- Hotelling 1931 — used in Tech Appendix discussion of how RCV connects to standard resource economics; CITED not promoted as framework element. Already in bibliography §18.5.

**Sub-records (Methods 1, 2, 3) preserved within parent record below:**

#### Method 1 — Replacement Cost (Lower Bound)
- *Methodology:* RCV_min per unit ≥ replacement cost from nearest substitute − market price at extraction.
- *Boundary checks:* sand → low; helium → severe (correct directional differentiation).
- *M12 lineage:* Costanza 1997 ecosystem-services valuation + standard regulatory cost-benefit analysis + eminent-domain takings law.

#### Method 2 — Norway Revealed Preference (Middle-Anchor within Triangulation)
- *Methodology:* Norway fund value ÷ total barrels extracted = per-barrel captured value; for any comparison case, gap = Empirical measure of uncaptured RCV.
- *Sidesteps the discount-rate debate* (empirical not philosophical).
- *Per Open Insight #14 epistemic-humility ratification:* Norway didn't fully capture RCV either (climate damages externalized; future-uses option-value uncaptured). Method 2 functions as Norway-anchored MIDDLE within the triangulation (Method 1 ≤ Method 2 ≤ Method 3 ≤ true RCV); not absolute middle of true RCV.
- *M12 lineage:* Hartwick rule 1977 + Solow 1974 + revealed-preference economics tradition.

#### Method 3 — Scarcity-Adjusted Option Value (Theoretical Upper Bound)
- *Methodology:* Real-options theory (Dixit-Pindyck 1994) specialized for declining substitutability + future-use uncertainty. Parameters σ + α + V_option.
- *Tech Appendix v0.0.5 specification REQUIRED:* mathematical specification, parameter calibration approach, upper-bound rationale.
- *M12 lineage:* Dixit-Pindyck 1994 (already in bibliography); real-options applications in natural-resource extraction (Brennan-Schwartz 1985); option-pricing foundation (Black-Scholes 1973).

**Why Ring 2 (not Ring 1):**
- Mathematical methodology, not adoption-target vocabulary.
- Readers learn methodology; non-readers adopt framework concepts (Severed Cost; CS), not estimation methodologies.

**Pairs with:**
- RCV (Ring 1) — the quantity estimated.
- Four Gates (Ring 2) — admit costs first; estimate value second.
- CSD (Ring 2) — companion two-instrument-architecture estimation (different methodology — reparations economics rather than triangulated).
- Substitutability Function S (Ring 2) — appears in Method 3 formal model.

**Convergence-table pedagogy** (Ch 6 numerical center-of-gravity per IPG rigor pass): 4 approaches converge on IPG ≫ 1 across cases. Tech Appendix v0.0.5 should clarify whether 4-approaches reference is Methods 1+2+3 + Hotelling-citation cross-check OR Methods + CSD-RCV correlation cross-check (Block 1 cross-validation idea).

**Methodology naming decision (ratified 2026-04-24):**
- "Triangulated RCV Estimation" — formal name (Tech Appendix).
- "Three Ways of Counting" — pedagogical name (Ch 6 chapter title; preserves M5 dinner-table accessibility).
- Both forms ratified; different audiences.

**Open Insight #20** (sensitivity-analysis execution σ + α + V_option dominance) opened for Tech Appendix v0.0.5 publication.

**Staleness triggers:**
- Block 4 validation execution reveals methods don't converge on test cases.
- New estimation methodology emerges that displaces one of the three.
- Sensitivity-analysis reveals one parameter dominates such that triangulation provides no value.

**Commit trail:**
- Three Ways + RCV Formal-Model pass: commit `1c8e4dd`.
- Three Ways ratification + bibliography additions: commit `66becc5`.
- Triangulated RCV Estimation individual rigor pass: commit `4f48c48`.
- Ratification + Terms Index record: this commit.

---

### Accountability Bond — UPDATE: B = B1 + B2 decomposition (v1.2 — final sub-instrument names ratified)

**Working definition update (v1.2, supersedes v1.1 working-label sub-instrument names):** Aggregate framework instrument B = B1 + B2 closing the Cost Severance gap (CS = RCV − B at aggregate level; expanding via two-instrument architecture: total CS = (CSD − B1) + (RCV − B2)). Sub-decomposed into **B1 (Restitution Bond, backward-looking, pairs with CSD) and B2 (Foreclosure Bond, forward-looking, pairs with RCV)**. Final sub-instrument names ratified 2026-04-24 via dedicated B1 + B2 naming rigor pass.

**Status:** `CURRENT` at Ring 2 (aggregate ratified 2026-04-24 by Chris Winn; v1.1 update with B = B1 + B2 decomposition ratified 2026-04-24; v1.2 update with final sub-instrument names ratified 2026-04-24).

**Term-spec version:** v1.2 (aggregate v1.0 + B = B1 + B2 decomposition v1.1 + final sub-instrument names v1.2; Ring 2 status preserved).

**Last reviewed:** 2026-04-24.

**Rigor provenance update:**
- Original Accountability Bond rigor pass (commit `7fa1c1b`) — aggregate Ring-2 ratified.
- Three Ways + RCV Formal-Model pass §7.3 (commit `1c8e4dd`) — surfaced B = B1 + B2 decomposition via Block 1 two-instrument architecture.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`) — decomposition rigor pass commissioned.
- B1/B2 decomposition individual rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_b1_b2_decomposition_v1.0.0.md` (commit `ab24a8e`) — Option A (decomposition ratified) verified with equational consistency check + per-sub-instrument M12 audit.
- B1 + B2 naming rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` (commit `8e6a5b2`) — Restitution Bond + Foreclosure Bond ratified over working labels (Reparations Bond + Resource-Foreclosure Bond).
- Aggregate decomposition ratification 2026-04-24 by Chris Winn (commit `56b5fd4`) — B = B1 + B2 + Open Insight #14 refinement.
- Final names ratification 2026-04-24 by Chris Winn — this commit.

**Equational consistency:** CS = RCV − B holds aggregately; decomposed: total CS = (CSD − B1) + (RCV − B2) = TED − B (Total Extraction Damages minus Total Accountability Bond). Boundary-case instruments (spanning both) decomposed by component.

#### B1 — Restitution Bond (Ring-2 sub-instrument)

**Working definition:** Backward-looking accountability-instrument cluster that closes the CSD gap. Mechanisms restoring (in monetary, legal, structural, or rights-based form) what was taken from people via cost severance — restitution payments, reparations programs, welfare-state instruments (universal healthcare, social-safety-net programs, public pensions), environmental-justice damages compensation, toxic-tort litigation, class-action damages, truth-and-reconciliation processes. Pairs with CSD in two-instrument architecture.

**Glossary definition (~75 words, reader-register; v1 DRAFT in Claude's voice — awaits author voice refinement during Phase 4 Glossary v4 rebuild):**
> Backward-looking accountability instrument — restitution payments, reparations programs, welfare-state instruments (universal healthcare, public pensions), environmental-justice damages compensation, toxic-tort litigation, truth-and-reconciliation processes. *Restitution Bond (B₁)* closes the cost-severance damages gap: dollars that flow to people, communities, and ecosystems already harmed by extraction. Pairs with B₂ Foreclosure Bond (forward-looking) in the framework's two-instrument architecture. Underdeveloped territory globally; varies by welfare-state design.

**Tech Appendix definition (~290 words, formal + lineage; v1 DRAFT in Claude's voice — awaits author voice refinement during Phase 3 Tech Appendix v2.0.0 rebuild):**
> **B₁ — Restitution Bond** is the backward-looking sub-instrument in the framework's two-instrument decomposition of Accountability Bond (B = B₁ + B₂). It denotes the cluster of accountability mechanisms that close the Cost Severance Damages (CSD) gap by restoring — in monetary, legal, structural, or rights-based form — what was taken from people via realized cost severance. In the decomposed equation total CS = (CSD − B₁) + (RCV − B₂), B₁ pairs structurally with CSD: B₁ is the dollars that would discharge the realized-harm half of total severance.
>
> **Mechanisms in cluster.** Restitution payments; reparations programs; welfare-state instruments (universal healthcare, social-safety-net programs, public pensions); environmental-justice damages compensation; toxic-tort litigation; class-action damages; truth-and-reconciliation processes.
>
> **Why "Restitution" over "Reparations"** (per B₁+B₂ naming rigor pass 2026-04-24): legal-register-clear; cross-political-tradition adoption potential. "Reparations" carries political-loading that narrows framework adoption to politically-progressive audiences; "Restitution" preserves the same restoration-of-what-was-taken meaning while reaching center-right, libertarian, and politically-cautious institutional audiences who would disengage at "Reparations." Restitution-law scope is broader than damages-law (encompasses monetary + legal + structural + rights-based restoration), fitting CSD's broader scope.
>
> **M12 lineage.** Restitution-law tradition (general legal vocabulary). Darity & Mullen 2020 *From Here to Equality* (UNC Press) — primary reparations-economics methodology source. Bullard 1990 *Dumping in Dixie* (Westview) — environmental-justice damages cross-reference. Toxic-tort + class-action damages tradition. Truth-and-reconciliation processes (South Africa post-apartheid + analogous infrastructures). Esping-Andersen 1990 *The Three Worlds of Welfare Capitalism* (Princeton) — welfare-state design lineage.
>
> **Status of B₁ globally.** UNDERDEVELOPED. Restitution-and-reparations is the active scholarly territory; less politically settled than B₂; varies widely across welfare-state architectures; environmental-justice damages compensation is litigation-driven and incomplete.

**Why "Restitution" over "Reparations" (per B1 + B2 naming rigor pass commit `8e6a5b2`):** legal-register-clear; cross-political-tradition adoption potential. "Reparations" carries political-loading that narrows framework adoption to politically-progressive audiences; "Restitution" preserves the same restoration-of-what-was-taken meaning while reaching center-right + libertarian + politically-cautious institutional audiences who'd disengage at "Reparations." Per Option C' political-philosophical-accommodation discipline (ratified 2026-04-24): framework accommodates political traditions rather than asserts politically-loaded commitments. Restitution-law scope is BROADER than damages-law (encompasses monetary + legal + structural + rights-based restoration); fits CSD's broader scope than narrow damages.

**M12 lineage:**
- Restitution-law tradition (general legal vocabulary; not citation-specific).
- Darity, William A., Jr., & Mullen, A. Kirsten. *From Here to Equality* (UNC Press 2020) — primary reparations economics methodology source. Already in bibliography §18.5.
- Bullard, Robert D. *Dumping in Dixie* (Westview 1990) — environmental-justice damages cross-reference. Already in bibliography §7.
- Toxic-tort + class-action damages tradition (legal-economics lineage).
- Truth and Reconciliation processes (South Africa post-apartheid + analogous infrastructures).
- Esping-Andersen, *The Three Worlds of Welfare Capitalism* (Princeton 1990) — welfare-state design lineage (optional Tech Appendix addition).

**Status of B1 globally:** UNDERDEVELOPED. Restitution-and-reparations is the active scholarly territory; less politically settled than B2; varies widely across welfare-state architectures; environmental-justice damages compensation is litigation-driven and incomplete.

**Pairs with:** CSD (Ring 2); aggregate Accountability Bond; Cost Severance mechanism (Ring 1).

#### B2 — Foreclosure Bond (Ring-2 sub-instrument)

**Working definition:** Forward-looking accountability-instrument cluster that closes the RCV gap. Mechanisms internalizing resource permanent-foreclosure value — Hartwick savings (sovereign wealth funds), reclamation bonds, Environmental Impact Bonds, Pigouvian carbon taxes, cap-and-trade schemes, decommissioning bonds. Pairs with RCV in two-instrument architecture.

**Glossary definition (~75 words, reader-register; v1 DRAFT in Claude's voice — awaits author voice refinement during Phase 4 Glossary v4 rebuild):**
> Forward-looking accountability instrument — sovereign wealth funds operationalizing Hartwick's rule (Norway = canonical existing exemplar), reclamation bonds, Environmental Impact Bonds, Pigouvian carbon taxes, cap-and-trade schemes, decommissioning bonds for oil and gas. *Foreclosure Bond (B₂)* closes the residual-commons-value gap: dollars forced from extractors to internalize the permanent foreclosure of future-generation options. Term-pair coherence with Foreclosure Cost (C₁) — what the bond internalizes. Pairs with B₁ Restitution Bond (backward-looking) in the framework's two-instrument architecture.

**Tech Appendix definition (~290 words, formal + lineage; v1 DRAFT in Claude's voice — awaits author voice refinement during Phase 3 Tech Appendix v2.0.0 rebuild):**
> **B₂ — Foreclosure Bond** is the forward-looking sub-instrument in the framework's two-instrument decomposition of Accountability Bond (B = B₁ + B₂). It denotes the cluster of accountability mechanisms that close the Residual Commons Value (RCV) gap by forcing extractors to internalize the dollar quantification of permanent foreclosure imposed on future generations. In the decomposed equation total CS = (CSD − B₁) + (RCV − B₂), B₂ pairs structurally with RCV: B₂ is the dollars that would discharge the prospective-foreclosure half of total severance.
>
> **Mechanisms in cluster.** Hartwick savings (sovereign wealth funds — Norway's GPFG = canonical existing exemplar); reclamation bonds (SMCRA 1977 surface mining); Environmental Impact Bonds (Balboa 2016); Pigouvian carbon taxes; cap-and-trade schemes; decommissioning bonds for oil and gas (BLM 43 CFR Part 3162; BSEE 30 CFR Part 250 + 254; ~36 state plugging/abandonment bond regimes); CERCLA / RCRA financial-assurance requirements.
>
> **Why "Foreclosure Bond" over "Resource-Foreclosure Bond"** (per B₁+B₂ naming rigor pass 2026-04-24): term-pair coherence with Foreclosure Cost (C₁ in RCV integrand) — *"Foreclosure Cost is what's lost; Foreclosure Bond is what would internalize it."* Shorter; preserves descriptive content via framework context; M5 dinner-table strong via mortgage-foreclosure analogy (in mortgage-foreclosure, ownership permanently severed from borrower; in resource-foreclosure, future-use permanently severed from future generations).
>
> **M12 lineage.** Hotelling 1931 *Journal of Political Economy* — foundational resource-economics; Hotelling rent under honest accounting flows to B₂ instrument. Hartwick rule 1977 — invest resource rents in reproducible capital. Solow 1974 — intergenerational equity and exhaustible resources. OSMRE Reclamation Bonds + GAO-17-207R + Yang & Davis 2021. Balboa 2016 *Accountability of Environmental Impact Bonds*. Pigou 1920 *Economics of Welfare*.
>
> **Norway = canonical existing B₂ exemplar.** Refines Open Insight #14: Norway's GPFG is canonical B₂, NOT canonical aggregate B; Norwegian welfare-state is approximately B₁-for-Norwegian-citizens but does not extend to non-Norwegian populations affected by Norwegian oil's climate externalities. Phase 2 deeper-dive rigor pass 2026-04-29 ratified KEEP term + 6 alternatives rejected at Phase 2 depth (Resource-Foreclosure Bond; Future-Options Bond; Long-Horizon Bond; Intergenerational Resource Bond; Hartwick Bond; Sovereign Reserve Bond; Forward Accountability Bond).

**Why "Foreclosure Bond" over "Resource-Foreclosure Bond" (per B1 + B2 naming rigor pass commit `8e6a5b2`):** **term-pair coherence with Foreclosure Cost (C₁ in RCV integrand)** — *"Foreclosure Cost is what's lost; Foreclosure Bond is what would internalize it."* Shorter; preserves descriptive content via framework context; M5 dinner-table strong via mortgage-foreclosure analogy (in mortgage-foreclosure, ownership permanently severed from borrower; in resource-foreclosure, future-use permanently severed from future generations).

**Norway = canonical existing B2 exemplar** (specifically — operationalizes Hartwick rule 1977 via sovereign-wealth-fund). Refines Open Insight #14: Norway's GPFG is canonical B2, NOT canonical aggregate B; Norwegian welfare-state is approximately B1-for-Norwegian-citizens but doesn't extend to non-Norwegian populations affected by Norwegian oil's climate externalities.

**M12 lineage:**
- Hotelling, Harold. *Journal of Political Economy* 1931 — already in bibliography §18.5. Foundational resource-economics; Hotelling rent under honest accounting flows to B2 instrument.
- Hartwick rule 1977 — invest resource rents in reproducible capital. Norway sovereign-fund operationalizes (optional Tech Appendix addition).
- Solow 1974 — intergenerational equity and exhaustible resources (optional Tech Appendix addition).
- OSMRE Reclamation Bonds + GAO-17-207R + Yang & Davis 2021 — already in bibliography §15. Reclamation bond literature.
- Balboa 2016 *Accountability of Environmental Impact Bonds* — already in bibliography §15.
- Pigou 1920 *Economics of Welfare* — already in bibliography §17. Pigouvian-tax tradition.

**Phase 2 deeper-dive rigor pass `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md` (2026-04-29):** full 12-cell multi-audience matrix per vocabulary strategy v1.0.1 §2 + §8 + M6 academic rigor depth audit + M11 critic-survival from 5 critic positions (housing-crisis-trauma; race-justice; mortgage-finance-vocabulary; resource-economics; marketing-positioning) + M12 attribution-honesty depth audit + affective-valence dimension. **Verdict: KEEP term (PASS conditional on three enhancements) — RATIFIED 2026-04-29 by Chris Winn.** Re-tested 2026-04-24 b1_b2_naming verdict against 12-cell matrix that did not exist at original ratification; verdict held. No cell FAILS. Tier 1 + Tier 2b + Tier 2d/Lived-oppression conditional STRONG-with-enhancement / WEAK-without (heavier failure-mode than Cost Severance Phase 2 due to housing-foreclosure trauma-affect vs HR-severance bureaucratic-affect). Tier 3a + 3b ADEQUATE due to inherent trauma-affect on jacket-marketing register (structural property of the term). Rename rejected (6 alternatives tested at Phase 2 depth: Resource-Foreclosure Bond; Future-Options Bond; Long-Horizon Bond; Intergenerational Resource Bond; Hartwick Bond; Sovereign Reserve Bond; Forward Accountability Bond). Three enhancements ratified: (a) lineage citation expansion (this update); (b) Ch 9 *Pricing Honestly* bridge prose at Foreclosure Bond first-introduction (canonical text below; DRAFT v1 Phase 2 §7.3); (c) Tech Appendix §L methodological footnote on Foreclosure Bond housing-crisis-affect handling (placement: NOW vs Phase 3 Tech Appendix v2.0.0 rebuild — pending author choice on §12.5 of Phase 2 rigor pass; option for unification with Cost Severance Phase 2 §L footnote into single methodological-framing section per §12.4).

**Cross-political-tradition lineage (Phase 2 expansion 2026-04-29):**
- *Race + housing-economics scholarship (Tier 2d + Lived-oppression load-bearing)* — Mian & Sufi 2014 *House of Debt* (already cited at Ch 9:119 housing-crisis discussion; lineage anchor for bridge prose); Rothstein 2017 *The Color of Law* (housing segregation; structural foreclosure of Black wealth); Taylor 2019 *Race for Profit* (racial dimensions of subprime crisis); Coates 2014 "The Case for Reparations" *The Atlantic* (housing/wealth/race nexus); Hyman 2011 *Debtor Nation* (consumer credit + foreclosure history); Sugrue 1996 *The Origins of the Urban Crisis* (urban + race + wealth + foreclosure); Desmond 2016 *Evicted* (eviction + housing-instability lineage).
- *Decolonial / colonial-foreclosure (cross-reference Cost Severance Phase 2 lineage)* — Wolfe 1999 *Settler Colonialism and the Transformation of Anthropology* (logic of elimination; severance of indigenous peoples from territory); Coulthard 2014 *Red Skin, White Masks*; Tuck & Yang 2012 "Decolonization is not a metaphor"; Whyte (indigenous environmental ethics).
- *Reparations economics (positions Foreclosure Bond as forced-extractor-payment analog)* — Darity & Mullen 2020 *From Here to Equality* (already cited in Restitution Bond B1 lineage §2049; symmetric application to Foreclosure Bond as forward-looking analog of backward-looking restitution).
- *US regulatory precedent (Tier 2b adoption-travel anchor)* — BLM 43 CFR Part 3162 (federal oil and gas decommissioning bond requirements); BSEE 30 CFR Part 250 + 30 CFR Part 254 (offshore drilling decommissioning + oil-spill-response bonds); state oil-and-gas commission rules (Texas Railroad Commission Form W-1; Wyoming Oil and Gas Conservation Commission Rule Ch 3 §8; Oklahoma Corporation Commission rules; ~36 states require some form of plugging/abandonment bond); CERCLA / RCRA financial-assurance requirements (hazardous-waste cleanup bonds); SMCRA 1977 reclamation bonds (already cited at §2071); Environmental Impact Bonds (Balboa 2016, already cited at §2072). Foreclosure Bond positions as cluster-name + principled extension of existing US regulatory practice that 36+ states + federal agencies recognize.

**Pairs with:** RCV (Ring 1); Foreclosure Cost C₁ (term-pair coherence — what the bond internalizes); aggregate Accountability Bond; Hotelling 1931 framing; Norway case study; Restitution Bond B1 (forward-looking analog of backward-looking restitution; symmetric bond-as-forced-extractor-payment positioning).

**Ch 9 *Pricing Honestly* bridge prose at Foreclosure Bond first-introduction (RATIFIED 2026-04-29 v1 DRAFT per Phase 2 §7.3; awaits author voice refinement during Ch 9 revision cycle; ~250-350 words):**
> *"The 2008 housing crisis is one of the few recent moments at which the foreclosure problem became visible at civilizational scale. Ten million American families lost homes; eleven trillion dollars in household wealth disappeared; the racial disproportionality was severe — Black homeownership fell from 47.7% in 2004 to roughly 40% by 2014, and Latino subprime targeting was systematic enough to produce a substantial scholarship documenting the predatory lending architecture that produced it (Taylor 2019; Rothstein 2017; Coates 2014). Mian and Sufi (2014) argued that the welfare cost of the chosen federal response — recapitalizing bank balance sheets rather than restructuring underwater mortgages — was substantial and could have been avoided by the alternative architecture. The instrument we did not have was the one that would have forced internalization at the front end: a structure that priced the foreclosure-of-options-for-future-borrowers at the moment loans were originated and held the originating institutions accountable for that cost.*
>
> *The framework names this kind of instrument the* Foreclosure Bond*. It is the forward-looking accountability instrument that closes the residual-commons-value gap — the dollar quantification of the foreclosure of future-generation options-substitution. Mortgage-foreclosure foreclosed homeowners' equity-of-redemption; resource-foreclosure forecloses future generations' options-substitution. The structural form is the same; the asset class differs.*
>
> *Foreclosure Bond is built on a cluster of existing mechanisms — sovereign wealth funds operationalizing Hartwick's rule (Norway = canonical existing exemplar), reclamation bonds (SMCRA 1977 for surface mining), Environmental Impact Bonds (Balboa 2016), Pigouvian carbon taxes, cap-and-trade schemes, decommissioning bonds for oil and gas. What unifies these is the structural commitment: the bond is forced from extractors to internalize the foreclosure-cost they would otherwise impose on future generations. It is not capital-deployment; it is capital-constraint. In the housing-crisis analog: it is the instrument that would have prevented the wave of foreclosures by pricing the foreclosure risk at origination — and we did not have it. We do not have it for resource-foreclosure either. The remainder of this chapter examines what such an instrument architecture looks like in practice, what existing instruments approximate it, and where the framework's specification differs from them."*

**Bridge prose status:** v1 DRAFT in Claude's voice (Phase 2 §7.3 ratification 2026-04-29); awaits Chris's voice refinement during Ch 9 revision cycle (Ch 9 *Pricing Honestly* is currently drafted at ~5,600 words; bridge prose insertion expected during pre-submission editorial review or as part of scaffolding-vs-publisher-facing separation pass per Insight #37). Verdict at Phase 2 depth on the bridge is "PLAN HOLDS conditionally pending execution + enhancement" — execution = bridge prose landed at appropriate Ch 9 placement (specific line-number / section TBD by author).

**Aggregate B notes (v1.1 update):**
- Phrase-travel-monitoring flag (Open Insight #11) preserved at aggregate level.
- Scope-creep-monitoring flag (Open Insight #13) preserved + applies to both sub-instruments.
- Two-readership adoption opportunity surfaced: B2-conversation (resource-economics + sustainability-finance audiences); B1-conversation (justice-economics + political-philosophy audiences).
- Open Insight #14 refined: Norway = canonical existing B2 exemplar; B1 globally underdeveloped.

**Phase A3 sweep targets:**
- Ch 5 (accountability gap) — two-instrument architecture framing.
- Ch 9 (policy economy) — two distinct instrument-design conversations named.
- Tech Appendix v0.0.5 — B = B1 + B2 decomposition section + per-sub-instrument formalism.
- Glossary v3 — B1 + B2 sub-entries.
- Open Insight #14 update — Norway-as-B2-canonical refinement.

---

*End of Term Provenance Index v1.0.0. Skeleton established 2026-04-24 (v0.1.0); populated progressively through Phase 2 + Group 1 ratifications; bumped to v1.0.0 2026-04-30 per refined Working Principle #4 (Insight #59) — current-state document with summary-level retirement traces. Full retirement traces at `archive/retirements/index.md`.*
