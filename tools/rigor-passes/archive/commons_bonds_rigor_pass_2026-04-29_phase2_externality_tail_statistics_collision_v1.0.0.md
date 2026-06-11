# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: Externality Tail — Statistics-Distribution-Tail Collision Audit

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — academic-rigor depth audit per author direction 2026-04-29: pass/fail gate on academic-rigor for vocabulary including suffix-collision concerns. Tests applied: premise enumeration (definitional clarity); collision check against statistics distribution-tail conventions; Tier 2a + 2e multi-audience misread risk; semantic-disambiguation discipline; falsifiability (does collision produce wrong-framework reading?); domain of applicability; counterexample resistance + alternative-naming feasibility analysis; suffix-coherence (one-off "-Tail" acceptability per Phase 1 §9.4 prior closed disposition).

**Scope:** Phase 2 academic-rigor depth audit on the **Externality Tail (E(R, t))** Ring-2 term — does the "tail" suffix collide with statistics-distribution-tail conventions in finance / actuarial / extreme-value theory / risk literature? Phase 1 §6.11 + §10 #3 flagged: *"Externality Tail — statistics-distribution-tail collision + suffix coherence (already deferred per Item 4.2 partly). Statistics-distribution-tail collision (Tier 2a econ readers may import distribution-tail framing; framework's E is a time-indexed function, not distribution tail). Verdict: PASS screening BUT FLAG for Phase 2 deeper dive on statistics-tail collision + suffix-convention coherence."*

**Status:** **RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify both enhancements.** Tech Appendix HTML edit timing pending author choice on §15 Q6 (same open question as Insights #35 + #38 + #40 + #47 + #48). Insight #49 closed-ratified entry added to `alignment/commons_bonds_open_insights_v1.0.0.md`.

**Author:** Chris Winn

**Recommended verdict (preview):** **PASS conditional on two concrete disambiguation enhancements.** The framework's "Externality Tail" terminology is **intentionally metaphorical** — the "tail" refers to **temporal persistence** of damage post-extraction (the tail of the damage curve in time), not to the **statistical-distribution sense** of tail (extreme-value behavior of probability distributions). The metaphor is rooted in the same geometric intuition (tail = part far from the central mass) but the framework's domain is **time** (post-extraction persistence) while statistics-distribution-tail's domain is **probability** (extreme outcomes far from the mean).

The collision risk is real for Tier 2a (academic-economist) + Tier 2e (working-quant) readers who pattern-match "-Tail" to Mandelbrot heavy-tail / Taleb Black Swan / actuarial ruin-theory tail / extreme-value-theory tail. A reader from any of these literatures sees "Externality Tail" and may infer "extreme-value externality cost" (Black-Swan-style externality risk), which is structurally different from the framework's intended meaning.

Two enhancements: (1) explicit disambiguation note at terms_index Externality Tail entry + Tech Appendix §B Definition A.4 first appearance + glossary v3 — distinguishing the framework's temporal-persistence sense from statistics-distribution-tail conventions; (2) bibliography expansion citing the relevant divergent lineages (Mandelbrot 1963 fat-tail; Taleb 2007 Black Swan; extreme-value theory) so the disambiguation is academically anchored.

**Rename considered + rejected.** Alternative naming (Persistent Externality / Externality Persistence / Post-Extraction Externality / Lingering Externality / Externality Aftermath) tested via §12 alternative-naming feasibility analysis. **Rejected** because: (a) "Externality Tail" already has 29+ publisher-facing line-counts of established usage (terms_index, glossary v3, Tech Appendix, Ch 4 GuidanceDoc, Ch 7 prose, multiple case studies including Norway / Niger Delta / Indigenous-dispossession / 2008-financial-crisis / Vienna / Chattanooga / Alaska); (b) the rhetorical anchor "runs on its own clock" depends on the temporal-tail metaphor; (c) the metaphor itself is correct and useful — the temporal tail of damage IS structurally analogous to the geometric tail of a distribution; (d) disambiguation note resolves the collision at lower cost than full rename.

**Suffix-coherence question (Phase 1 §10 #3 bundling) closed-confirmed.** Phase 1 §9.4 ratified "-Tail" as acceptable one-off suffix; this audit confirms no additional suffix-coherence concern. The two-issue bundling (statistics-tail collision + suffix coherence) collapses to a single-issue concern (statistics-tail collision) at the Phase 2 depth.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

The Externality Tail (E(R, t)) Ring-2 term currently appears in:
- **Tech Appendix §B Definition A.4** — primary definition: *"E(R, t) represents the externality flow at time t resulting from extraction of resource R at time t₀. This includes ongoing environmental damage, health costs, community disruption, and ecological degradation that persist beyond the extraction event. E(R, t) ≥ 0 for all t, and typically exhibits a long tail: E(R, t) > 0 for many generations after extraction ceases."*
- **terms_index Externality Tail entry** — comprehensive Tier-D treatment with M11/M12 lineage (Pigou 1920 + Nordhaus-Boyer 2000 + Stern 2007); 4-axis distinctness from generic Pigovian externality.
- **Glossary v3 entry** (~80 words reader-register).
- **Chapter prose** — Ch 4 GuidanceDoc; Ch 7 prose; multiple case studies (Norway, Niger Delta, Indigenous-dispossession, 2008-financial-crisis, Vienna, Chattanooga, Alaska, opioid-extraction-Appalachia).
- **RCV integrand** — E(R, t) as second component (sibling to foreclosure cost C₁) per RCV(R, t₀) = ∫_{t₀}^∞ {[1 − S(t|t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt.

The audit tests:
1. **Premise enumeration** — is "Externality Tail" defined precisely with explicit semantic anchor?
2. **Collision check** — does "-Tail" suffix pattern-match with statistics-distribution-tail conventions in finance / actuarial / extreme-value theory / risk literature? Concrete misread risk for which audiences?
3. **Multi-audience misread risk** — Tier 2a (academic-economist) + Tier 2e (working-quant) + Tier 3 (cross-disciplinary) collision exposure?
4. **Semantic-disambiguation discipline** — does any current text explicitly distinguish "Externality Tail" from statistics-distribution-tail readings?
5. **Falsifiability** — does the collision produce a framework-divergent claim that would be falsified empirically?
6. **Domain of applicability** — where does "Externality Tail" apply consistently as temporal-persistence-of-damage?
7. **Counterexample resistance + alternative-naming feasibility** — can a reader misread "Externality Tail" as statistics-distribution-tail and produce framework-divergent results? are alternative naming options feasible at acceptable cost?
8. **Suffix-coherence (Phase 1 §9.4 bundling)** — is "-Tail" one-off suffix acceptable per established Phase 1 disposition?

### §1.2 Phase 2 outcomes

| Test | Verdict | Note |
|---|---|---|
| Premise enumeration | **STRONG** | terms_index + glossary + Tech Appendix Definition A.4 each define E(R, t) as time-indexed cost function with 4-axis distinctness from Pigouvian externality |
| Collision check | **WEAK** | "-Tail" pattern-matches with Mandelbrot 1963 fat-tail; Taleb 2007 Black Swan; ruin-theory tail; extreme-value-theory tail; long-tail Anderson 2006. Reader from any of these literatures imports wrong-domain framing on first encounter |
| Multi-audience misread risk | **MEDIUM-WEAK** | Tier 2a (academic-economist) + Tier 2e (working-quant from finance / actuarial / risk) at significant misread risk. Tier 1 (lay) + Tier 2c (policy-practitioner) low risk. Tier 2b (academic-philosopher) low risk |
| Semantic-disambiguation discipline | **WEAK** | No current text explicitly distinguishes "Externality Tail" from statistics-distribution-tail conventions. The 4-axis distinctness from Pigouvian externality does not address the statistics-tail collision |
| Falsifiability | N/A | Naming choice is convention; the underlying concept (post-extraction persistence) is falsifiable separately |
| Domain of applicability | **STRONG** | Externality Tail used consistently as temporal-persistence-of-damage across all 29+ framework appearances; no instances where it shifts to mean distribution-tail |
| Counterexample resistance | **STRONG** | Internal definition (∂E/∂t — temporal flow at time t after extraction; runs-on-its-own-clock rhetorical anchor) forces temporal-persistence reading. A reader who tries to apply distribution-tail interpretation produces incoherence |
| Alternative-naming feasibility | **WEAK (rejected)** | Alternatives (Persistent Externality / Externality Persistence / Post-Extraction Externality / Lingering Externality / Externality Aftermath) tested; all are functional but rename cost (29+ publisher-facing instances) outweighs collision-mitigation benefit; metaphor itself is correct and useful |
| Suffix-coherence | **CONFIRMED ACCEPTABLE** | Per Phase 1 §9.4 prior disposition — "-Tail" one-off suffix; no additional concerns surfaced at Phase 2 depth |

**Aggregate verdict: PASS conditional on two concrete disambiguation enhancements.**

The framework's "Externality Tail" terminology is metaphorically sound and definitionally rigorous, but the disambiguation against statistics-distribution-tail conventions is currently absent. A Tier 2a + 2e reader will pattern-match "-Tail" to extreme-value / heavy-tail / Black Swan literature on first encounter unless explicitly directed otherwise. The repair work is disambiguation-discipline + citation, not rename or re-derivation.

### §1.3 Two concrete disambiguation enhancements

**ENHANCEMENT 1: Explicit disambiguation note at three load-bearing locations**

(a) **terms_index Externality Tail entry** — add a new "Notational disambiguation" subsection (~80 words):

> **Notational disambiguation.** The framework's "Externality Tail" refers to **temporal persistence of damage post-extraction** (the tail of the damage curve in time, per the rhetorical anchor "runs on its own clock"), not to the **statistical-distribution sense** of "tail" used in finance / actuarial / extreme-value-theory / risk literature (e.g., Mandelbrot 1963 fat-tailed price distributions; Taleb 2007 Black Swans; ruin-theory tail risk; long-tail in business per Anderson 2006). The two senses share the underlying geometric intuition (tail = part far from the central mass) but the framework's domain is **time** (when does damage occur?) while statistics-distribution-tail's domain is **probability** (how extreme are the values?). E(R, t) is a deterministic time-indexed cost function, not a probability distribution.

(b) **Tech Appendix §B Definition A.4 first formula appearance** — add one parenthetical at the *"and typically exhibits a long tail: E(R, t) > 0 for many generations after extraction ceases"* sentence:

> *Replace:* "E(R, t) ≥ 0 for all t, and typically exhibits a long tail: E(R, t) > 0 for many generations after extraction ceases."
>
> *With:* "E(R, t) ≥ 0 for all t, and typically exhibits a long tail in time: E(R, t) > 0 for many generations after extraction ceases. (The 'tail' here is temporal — the persistence of damage after extraction ends — not the statistical-distribution sense of tail used in extreme-value theory or heavy-tail finance literature.)"

(c) **Glossary v3 entry** — add one disambiguating sentence to the existing 80-word entry:

> *Append:* "(Note: 'tail' here is temporal — the lingering damage after extraction — not the statistical sense used in extreme-value theory or finance.)"

**ENHANCEMENT 2: Bibliography expansion citing divergent lineages**

Add to bibliography:
- **Mandelbrot, Benoit. 1963.** "The Variation of Certain Speculative Prices." *Journal of Business* 36(4): 394-419. — fat-tailed price distributions; foundational heavy-tail finance literature.
- **Taleb, Nassim Nicholas. 2007.** *The Black Swan: The Impact of the Highly Improbable*. Random House. — extreme-value / Black Swan tail risk popularization.
- **Embrechts, Paul, Claudia Klüppelberg, and Thomas Mikosch. 1997.** *Modelling Extremal Events for Insurance and Finance*. Springer. — extreme-value-theory canonical text.
- **Anderson, Chris. 2006.** *The Long Tail: Why the Future of Business Is Selling Less of More*. Hyperion. — long-tail business / market-dynamics popularization.

(Pigou 1920 + Nordhaus-Boyer 2000 + Stern 2007 already in bibliography per Externality Tail terms_index M12 lineage.)

These citations support the disambiguation note's claim that the framework's "tail" is divergent from these established statistics-distribution-tail conventions; they are NOT load-bearing on the framework's substantive claims.

### §1.4 Why this verdict pattern (not rename Externality Tail → alternative)

Considered alternatives (per §12 feasibility analysis):
- **(A) Persistent Externality** — drops "tail"; gains explicit "persistent" descriptor; loses the metaphor.
- **(B) Externality Persistence** — preserves Pigouvian root; adds noun "persistence"; functional but flat.
- **(C) Post-Extraction Externality** — explicit temporal anchor; verbose.
- **(D) Lingering Externality** — colloquial; loses formal register.
- **(E) Externality Aftermath** — strong rhetorical; loses Pigouvian anchor.
- **(F) Temporal Externality** — abstract; potentially confusing (could read as time-of-damage, not post-extraction-persistence).

**All rejected** because:

1. **High rename cost.** "Externality Tail" appears in 29+ publisher-facing locations (terms_index Tier-D entry; glossary v3; Tech Appendix Definition A.4 + RCV integrand + multiple worked examples; Ch 4 GuidanceDoc; Ch 7 prose multiple instances; Norway / Niger Delta / Indigenous-dispossession / 2008-financial-crisis / Vienna / Chattanooga / Alaska case studies; opioid-extraction-Appalachia case study). Rename sweep is comparable to existential substitutability gap (CSG → existential substitutability gap rename at Insight #33) but with broader case-study reach.

2. **Metaphor is correct + useful.** The temporal tail of damage IS structurally analogous to the geometric tail of a distribution. Both concepts describe "what's far from the central mass" — geometric mass for distributions, temporal mass for the framework's damage curves. The metaphor's similarity to statistics-distribution-tail is precisely why the disambiguation note is needed; it's not a reason to abandon the metaphor.

3. **Rhetorical anchor "runs on its own clock"** depends on the temporal-tail metaphor. Without "tail," the anchor's pedagogical force diminishes. *"E runs on its own clock"* presupposes E has a temporal extent (a tail); replacing with *"Persistent Externality runs on its own clock"* reads less naturally.

4. **Disambiguation note resolves collision at lower cost.** Two enhancements (~120 words at terms_index + ~30 words at Tech Appendix + ~25 words at glossary + 4 bibliography entries = ~175 words + 4 references) close the misread-risk gap without rename. Comparable to P2#7 [scarcity-multiplier] + P2#8 [Q(t)] disambiguation patterns.

5. **Pigouvian externality lineage preserved.** "Externality Tail" keeps "Externality" prefix → directly anchored to Pigou 1920 lineage per Tech Appendix §L footnote. Alternatives B (Externality Persistence) preserve this; alternatives A/D/E (Persistent / Lingering / Aftermath) reorder the modifier-noun structure and weaken the Pigouvian anchor.

If author preference is to invest in rename (option A or B from §12), §14.4 keeps that on the table as alternative ratification choice.

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 1 §6.11 + §9.4 + §9.5 + §10 #3 + §12.2](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"§6.11 Externality Tail (E) [⚠ Phase 2 candidate]. Possible concerns surfaced: -Tail suffix one-off (already deferred per Item 4.2 suffix-convention coherence); Statistics-distribution-tail collision (Tier 2a econ readers may import distribution-tail framing; framework's E is a time-indexed function, not distribution tail). M11 probes: collision with statistics distribution-tail vocabulary (Phase 2 verification recommended). Verdict: PASS screening BUT FLAG for Phase 2 deeper dive on statistics-tail collision + suffix-convention coherence."*
>
> *"§9.4 Suffix-convention coherence. One-off suffixes already deferred per Item 4.2: -Identity (Hotelling Identity), -Tail (Externality Tail). The -Estimation suffix removed via Three Ways of Counting rename. No additional suffix concerns surfaced in Phase 1."*
>
> *"§10 #3. Externality Tail — statistics-distribution-tail collision + suffix coherence (already deferred per Item 4.2 partly)."*
>
> *"§12.2 Phase 2 proposal item 5: Externality Tail statistics-tail collision — minor; can bundle with Item 4.2 suffix-convention coherence."*

Phase 2 (this rigor pass) executes the screening-recommended audit at academic-rigor depth. The bundling between statistics-tail collision (load-bearing) and suffix-coherence (closed per Phase 1 §9.4) collapses to a single-issue audit on the collision, with suffix-coherence confirmed as already-resolved.

### §2.2 What this audit produces

For pass/fail academic-rigor gate at top-tier journals (AER, QJE, JPE, JEEM, JPubE, *Resource and Energy Economics*, *J Environ Econ Manage*, *J Risk and Uncertainty*) and academic-trade hybrid presses, the "Externality Tail" terminology must meet the following standards:

- Definitional clarity at every formula appearance.
- Explicit semantic-anchor distinguishing temporal-persistence sense from statistics-distribution-tail conventions.
- Reader from finance / actuarial / extreme-value-theory / risk literature can immediately disambiguate the framework's usage.
- Bibliography acknowledges the divergent lineages.

This audit produces:
1. Per-test verdict (premise enumeration; collision check; etc.).
2. Concrete disambiguation enhancement recommendations.
3. Recommended disambiguation language for terms_index + Tech Appendix + glossary.
4. Cross-references to established statistics-distribution-tail literature.
5. Alternative-naming feasibility analysis (rename considered + rejected justification).

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic rigor for vocabulary including suffix-collision concerns. This audit applies the same standard to "Externality Tail" that prior audits applied to other Ring-1 / Ring-2 collision concerns (Foreclosure Bond housing-crisis collision per Insight #38; Cost Severance + Severed Cost Tier 2d concern per Insight #35; Q(t) notation collision per Phase 2 #8).

### §2.4 What this pass does NOT cover

- **Re-litigation of Externality Tail Ring-2 ratification** — already RATIFIED 2026-04-24 per `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_externality_tail_v1.0.0.md`; this audit verifies collision-resilience, not the term's substantive content.
- **Pigouvian externality lineage audit** — Externality Tail's Pigovian distinctness on 4 axes (post-extraction persistence + substitutability-independence + time-indexed function form + "runs on its own clock") was confirmed in the 2026-04-24 individual rigor pass; not re-litigated here.
- **E(R, t) functional-form derivation** — Phase 2 candidate for separate audit if needed (not currently flagged).
- **Bibliography accuracy** — completeness audit per Insight #39 territory; this pass identifies citation gaps but does not execute full bibliography expansion.
- **Cross-coordination with theorem session** — Externality Tail appears in Theorem E.4 (RATIFIED Insight #40 with E in restructured premises A2 polynomial growth on E) and may appear in E.1/E.3/E.5 sibling theorem audits. The disambiguation enhancement is non-disruptive to theorem proofs (it adds a definitional note; doesn't change E's mathematical role).

---

## §3. Methodology

### §3.1 Academic-rigor depth audit framework

For each test below, the audit (a) reads every appearance of "Externality Tail" / E(R, t) across Tech Appendix + chapters + terms_index + glossary + case studies + prior rigor passes; (b) tests against academic-peer-review collision-resilience standards as practiced at top-tier journals; (c) produces verdict (STRONG / ADEQUATE / WEAK / FAIL); (d) flags concrete repair work where verdict < STRONG.

### §3.2 Tests applied

1. **Premise enumeration** — definitional clarity at every appearance.
2. **Collision check** — pattern-matching against statistics distribution-tail conventions.
3. **Multi-audience misread risk** — collision exposure per audience tier.
4. **Semantic-disambiguation discipline** — explicit distinction in current text.
5. **Falsifiability** — does collision produce framework-divergent claim?
6. **Domain of applicability** — consistent usage across framework surfaces.
7. **Counterexample resistance + alternative-naming feasibility** — internal coherence of intended reading + viability of rename.
8. **Suffix-coherence (Phase 1 §9.4 bundling)** — confirm "-Tail" one-off acceptability.

### §3.3 What the audit does NOT do

- Does NOT re-derive E(R, t) or its components.
- Does NOT verify the empirical claim that Externality Tail E ≥ 0 / persists post-extraction.
- Does NOT replace pre-publication external review by credentialed third party.
- Does NOT extend to other one-off suffix concerns (e.g., -Identity for Hotelling Identity — separate audit if needed).

---

## §4. Current state — close reading

### §4.1 Canonical definition (Tech Appendix §B Definition A.4)

[Tech Appendix v1.0.0 line 452-455](manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html):

> **Definition A.4 (Externality Tail)**
>
> E(R, t) represents the externality flow at time t resulting from extraction of resource R at time t₀. This includes ongoing environmental damage, health costs, community disruption, and ecological degradation that persist beyond the extraction event. E(R, t) ≥ 0 for all t, and typically exhibits a long tail: E(R, t) > 0 for many generations after extraction ceases.

### §4.2 terms_index Externality Tail entry (lines 1011-1059)

Comprehensive Tier-D treatment. Defines E(R, t) as time-indexed cost function with 4-axis distinctness from Pigouvian externality (post-extraction persistence + substitutability-independence + time-indexed + "runs on its own clock"). M11/M12 lineage cites Pigou 1920 + Nordhaus-Boyer 2000 + Stern 2007. Phrase travel-potential flagged for Ring-1 promotion if policy/legal discourse adopts.

### §4.3 Glossary v3 entry (~80 words reader-register)

> The damage that lingers after extraction stops. A substitute for coal doesn't clean up the mine. A substitute for oil doesn't remove carbon from the atmosphere. *Externality Tail* is the framework's name for costs that persist independently of whether substitutes appear — climate damage from past emissions, mine-tailings dispersion, biological extinction. Mathematically: E(R, t) — a time-indexed function that runs on its own clock. Specializes Pigou's externality concept (1920) for post-extraction persistence.

### §4.4 Chapter prose + case studies (~25+ instances)

Across publisher-facing surfaces:
- **Ch 4 GuidanceDoc:** "Environmental externality tail of North Sea drilling persists" — temporal-persistence usage.
- **Ch 7 prose:** Multiple instances; consistently temporal-persistence ("Decrease the externality tail" / "the externality tail is long").
- **Norway case study:** "the externality tail persists" / "does not close the externality tail" — temporal-persistence.
- **Niger Delta case study:** "borne the externality tail" — temporal-persistence.
- **Indigenous-dispossession case study:** "§3.3 The temporal structure of the externality tail" — explicit temporal anchor; "externality tail is measured in centuries."
- **Opioid-extraction case study:** "The externality tail was biological / behavioral / fiscal" — temporal-persistence with breadth qualifier.
- **2008-financial-crisis case study:** "B was vastly insufficient to cover the externality tail" — temporal-persistence.
- **Alaska / Chattanooga / Vienna case studies:** "Does not price permanent foreclosure or externality tail" — temporal-persistence.

**Pattern:** All 25+ instances use Externality Tail as **temporal-persistence-of-damage**. Zero instances where it shifts to mean distribution-tail or extreme-value tail.

### §4.5 Initial reading observations

- **The framework's domain is consistently temporal.** Every appearance describes damage that continues over time after extraction ends. "Long tail in time" / "tail measured in centuries" / "lingers after extraction stops" / "runs on its own clock" — all temporal-persistence framing.

- **Statistics-distribution-tail collision is real but not internally disruptive.** A reader who imports distribution-tail framing on first encounter would expect E(R, t) to be a probability distribution with extreme-value behavior in some random variable. The framework's E(R, t) is a deterministic function of (resource, time); not a probability distribution; doesn't have extreme-value behavior in the statistics sense. Reader who pauses to read Definition A.4 disambiguates immediately.

- **The metaphor is genuine.** "Tail" in both senses (statistics-distribution and the framework's temporal-persistence) refers to "the part far from the central mass." For statistics, central mass is the mean; the tail is far from the mean in probability-density. For the framework, central mass is the extraction event at t₀; the tail is far from t₀ in time. The geometric intuition is shared; the domain (probability vs time) differs.

- **The "long tail" phrasing in Definition A.4** ("typically exhibits a long tail: E(R, t) > 0 for many generations") explicitly invokes the temporal sense via the qualifier "for many generations." But the phrase "long tail" alone (without the qualifier) is identical to Anderson 2006 *Long Tail* business-economics phrase, which is yet another statistics-adjacent collision.

- **Tier 2a (academic-economist) has the strongest collision exposure.** Resource economics readers from Pindyck / Hartwick / Solow lineage may not pattern-match strongly to statistics-tail. But economics readers from finance / risk-management / actuarial sub-fields routinely use "tail" in the distribution sense; "Externality Tail" reads as "extreme-value externality cost" on first encounter. The framework's intended reader landscape (per vocabulary strategy v1.0.1 §2 multi-audience matrix) explicitly includes Tier 2a quant-trained readers — collision risk is in scope.

- **Tier 2e (working-quant) has equally strong collision exposure.** Risk-management / quant-finance / actuarial readers carry "tail" as distribution-tail vocabulary as native idiom. Their first inference at "Externality Tail" is "extreme-value externality" → wrong-framework reading.

---

## §5. Test 1 — Premise enumeration (definitional clarity)

### §5.1 Current state

- Tech Appendix §B Definition A.4: defines E(R, t) operationally as externality flow at time t persisting beyond extraction event.
- terms_index entry: 4-axis distinctness from Pigouvian externality.
- Glossary v3 entry: ~80-word reader-register definition.
- Chapter prose: contextually disambiguates per case-study walkthroughs.

The term is well-defined locally. Each definition stands on its own.

### §5.2 Verdict

**STRONG.** Premise enumeration is rigorous: time-indexed function form; non-negativity; persistence-condition; 4-axis Pigouvian distinctness. No definitional gaps.

### §5.3 Repair recommendation

None at premise-enumeration level. (Disambiguation discipline per Test 4 is the actual repair territory.)

---

## §6. Test 2 — Collision check against statistics distribution-tail conventions

### §6.1 Statistics distribution-tail lineage

| Reference | Tail concept |
|---|---|
| Mandelbrot 1963 *J Business* "The Variation of Certain Speculative Prices" | Fat-tailed (Lévy stable) distributions for asset returns |
| Mandelbrot 1982 *The Fractal Geometry of Nature* | Power-law tails as natural-systems pattern |
| Embrechts, Klüppelberg & Mikosch 1997 *Modelling Extremal Events* | Extreme-value-theory canonical text; tail-index estimation |
| Taleb 2007 *The Black Swan* | Black Swan extreme-value tail risk popularization |
| McNeil, Frey & Embrechts 2005 *Quantitative Risk Management* | Tail-VaR (Value at Risk); expected shortfall; conditional tail expectation |
| Reiss & Thomas 2007 *Statistical Analysis of Extreme Values* | Extreme-value-theory applications in insurance / finance / hydrology |
| Anderson 2006 *The Long Tail* | Long-tail in business / market dynamics (low-volume high-variety) |

**Convention pattern:** "Tail" in statistics / finance / actuarial / risk-management literature is **probability-distribution behavior far from the central tendency**. Heavy-tail / fat-tail / long-tail / power-law-tail / Pareto-tail / Cauchy-tail / Lévy-tail are all variants of the same probabilistic concept.

### §6.2 Framework's "tail" usage

The framework's "Externality Tail" refers to **temporal persistence of damage**:
- Domain: time (when does damage occur?).
- Function form: E(R, t) deterministic function of resource × time.
- "Long tail" qualifier means "extends far in time from extraction event."
- Rhetorical anchor: "runs on its own clock" (temporal extent).

**Domain divergence:** statistics-tail = probability domain; framework-tail = time domain.

### §6.3 Reader's first-encounter inference

A reader encountering "Externality Tail" or *"E(R, t) typically exhibits a long tail"* without prior context:
- **Tier 2a (academic-economist) trained in resource economics:** pauses; reads "long tail" as Anderson 2006 long-tail or as temporal-persistence (depending on sub-field background); resolves on reading Definition A.4. **Medium misread risk; resolved by definition.**
- **Tier 2a (academic-economist) trained in finance / IO:** pattern-matches "tail" to Mandelbrot fat-tail or Tirole IO long-tail; reads "Externality Tail" as "extreme-value externality." **High misread risk; only resolved by careful Definition A.4 reading.**
- **Tier 2e (working-quant from finance / actuarial):** pattern-matches to McNeil-Frey-Embrechts tail-VaR / extreme-value theory; reads E(R, t) as a probability distribution; misreads framework's deterministic function as stochastic. **High misread risk; resolved only after Definition A.4 study.**
- **Tier 2e (working-quant from physics / engineering):** pattern-matches to power-law / heavy-tail in physical-systems literature; medium misread risk.
- **Tier 1 (lay):** "tail" reads colloquially as "the end part" or "what trails behind"; no strong technical pattern-match. **Low misread risk.**
- **Tier 2c (policy-practitioner):** "tail" reads colloquially as "long-term consequences"; matches framework intended reading. **Low misread risk.**
- **Tier 2b (academic-philosopher):** "tail" not a load-bearing technical vocabulary item; reads contextually. **Low misread risk.**

### §6.4 Verdict

**WEAK.** Tier 2a (subset trained in finance / IO) + Tier 2e (working-quant with risk-management background) face high misread risk on first encounter. Without explicit disambiguation, these readers will infer "extreme-value externality" or "stochastic-tail externality" — both framework-divergent readings. The misread is corrected by careful reading of Definition A.4 + 4-axis distinctness, but academic-publication discipline expects disambiguation at first encounter, not after careful reading.

### §6.5 Repair recommendation

Disambiguation note per Enhancement 1 §13.1 — explicit at terms_index + Tech Appendix Definition A.4 + glossary v3, with bibliography expansion citing the divergent lineages.

---

## §7. Test 3 — Multi-audience misread risk

### §7.1 Tier-by-tier risk assessment

Per Vocabulary Strategy v1.0.1 §2 + §8 multi-audience matrix:

| Audience tier | Misread risk | Driver |
|---|---|---|
| Tier 1 (lay general reader) | **LOW** | "tail" reads colloquially; no technical pattern-match |
| Tier 2a-resource-econ (Pindyck / Hartwick / Solow lineage) | **MEDIUM** | "tail" in resource-econ is not a strong technical term; collision is real but mild |
| Tier 2a-finance/IO (Mandelbrot / Tirole lineage) | **HIGH** | "tail" is native fat-tail / heavy-tail vocabulary; "Externality Tail" reads as "extreme-value externality" |
| Tier 2b (academic-philosopher) | **LOW** | "tail" not technical vocabulary |
| Tier 2c (policy-practitioner) | **LOW** | "tail" reads as "long-term consequences"; matches framework |
| Tier 2d (cross-political-tradition) | **LOW** | not a technical-vocabulary register |
| Tier 2e (working-quant; finance / actuarial / risk-management) | **HIGH** | "tail" is native distribution-tail vocabulary; E(R, t) misread as probability distribution |
| Tier 3 (cross-disciplinary; physics / engineering / climate-science) | **MEDIUM** | "tail" carries power-law / heavy-tail framing in physical-systems literature |

### §7.2 Aggregate risk

- **HIGH risk:** ~30-40% of intended Tier 2 academic audience (Tier 2a-finance/IO + Tier 2e). These are readers the framework actively wants — academic-trade hybrid press strategy per Mazzucato/Raworth/Anderson positioning.
- **MEDIUM risk:** Tier 3 cross-disciplinary readers.
- **LOW risk:** Tier 1 + Tier 2c + Tier 2b + Tier 2d (majority of book audience but not the ones with collision exposure).

### §7.3 Verdict

**MEDIUM-WEAK.** Significant subset of intended Tier 2 academic audience faces high misread risk. The framework's vocabulary-strategy v1.0.1 multi-audience matrix discipline expects collision exposure to be addressed at first encounter for Tier 2 audiences specifically.

### §7.4 Repair recommendation

Per Enhancement 1 §13.1 — disambiguation note targets exactly the Tier 2a-finance/IO + Tier 2e readers who face the highest misread risk; the divergent-lineage citations (Mandelbrot 1963; Taleb 2007; Embrechts et al. 1997; Anderson 2006) are the references those readers will recognize, making the disambiguation immediately effective.

---

## §8. Test 4 — Semantic-disambiguation discipline (current state)

### §8.1 Current state

No current text in terms_index, Tech Appendix Definition A.4, or glossary v3 explicitly distinguishes "Externality Tail" from statistics-distribution-tail conventions.

The current discipline relies on:
- Definition A.4 operational definition (E is "externality flow at time t" — implies temporal but does not say "not statistics-tail").
- 4-axis distinctness from Pigouvian externality (addresses Pigouvian collision; does not address statistics-tail collision).
- Chapter prose context (every chapter usage clarifies temporally — but only after reader has encountered the term).

### §8.2 Verdict

**WEAK.** Current text relies on context to disambiguate; academic-publication discipline expects explicit notational disambiguation at canonical-definition location.

### §8.3 Repair recommendation

Enhancement 1 §13.1 places the disambiguation note at three locations (terms_index + Tech Appendix Definition A.4 + glossary v3) so a reader encountering the term at any entry-point gets the disambiguation without depending on chapter-context.

---

## §9. Test 5 — Falsifiability

### §9.1 Current state

The naming-collision concern is not a falsifiable claim per se; it is a discipline question (does the naming produce wrong-framework readings?). The underlying concept (post-extraction persistence per Definition A.4) is falsifiable separately (empirical: do externality damages persist post-extraction?), but that's a Definition A.4 audit, not a naming-collision audit.

### §9.2 Verdict

**N/A.**

### §9.3 Repair recommendation

None at falsifiability level.

---

## §10. Test 6 — Domain of applicability

### §10.1 Current state

"Externality Tail" / E(R, t) appears 29+ times across publisher-facing surfaces. Every appearance reads as **temporal persistence of damage post-extraction**. No instance found where it shifts to mean distribution-tail or extreme-value tail.

### §10.2 Verdict

**STRONG.** Domain of applicability is consistent across all framework surfaces; the temporal-persistence reading holds without exception.

### §10.3 Repair recommendation

None at domain level. (Disambiguation per Enhancement 1 closes the academic-publication first-encounter misread risk; consistency of internal usage is already strong.)

---

## §11. Test 7 — Counterexample resistance + alternative-naming feasibility

### §11.1 Counterexample resistance (internal coherence)

**Approach:** try to construct a reading of "Externality Tail" other than temporal-persistence under which the framework's E(R, t) equations still produce the framework's claims.

**Attempt 1 (Externality Tail = probability distribution-tail):** read E(R, t) as a probability density evaluated at extreme outcomes. Then E(R, t) > 0 means "extreme-outcome probability is positive at time t." Definition A.4 says "E(R, t) ≥ 0 for all t" — coherent with probability-density. But Definition A.4 also says "E represents the externality flow at time t resulting from extraction of resource R at time t₀" — flow is deterministic, not probabilistic. **Inconsistency surfaces immediately at "flow" terminology.** Probability-distribution-tail reading FAILS at the canonical definition.

**Attempt 2 (Externality Tail = extreme-value externality cost):** read E(R, t) as the extreme-value (worst-case) externality. Then E(R, t) is a max over random scenarios. Definition A.4 doesn't support max-formulation; E is a deterministic function. **FAILS.**

**Attempt 3 (Externality Tail = long-tail per Anderson 2006):** read "long tail" as "low-frequency-high-variety business pattern." Doesn't apply to externality-cost-over-time; concept mismatch. **FAILS.**

**Attempt 4 (Externality Tail = power-law tail per Mandelbrot 1982):** read E(R, t) as exhibiting power-law decay. Possibly coherent (E(R, t) ~ t^{-α} for large t is empirically plausible for some externality types — atmospheric carbon decay ~ exponential; toxin half-life ~ exponential; species-loss ~ irreversible → no decay). But the framework's claim is not "E follows power-law" — it's "E persists beyond extraction event." **PARTIALLY COHERENT but FRAMEWORK-DIVERGENT** — would require framework to commit to specific functional form, which it does not.

**Verdict:** Internal coherence FORCES temporal-persistence reading. A reader who tries probability-distribution-tail or extreme-value reading produces inconsistency at canonical-definition level.

### §11.2 Alternative-naming feasibility

**Six alternatives tested:**

**(A) Persistent Externality.**
- Pros: explicit "persistent" descriptor; drops "tail" suffix entirely; no statistics collision.
- Cons: loses temporal-tail metaphor; loses rhetorical anchor "runs on its own clock"; rename cost ~29+ instances.
- Verdict: functional but flat; rejected.

**(B) Externality Persistence.**
- Pros: preserves Pigouvian "Externality" prefix; adds "Persistence" noun; clean register.
- Cons: weaker rhetorical anchor; rename cost ~29+ instances; "Persistence" reads as abstract property rather than temporal phenomenon.
- Verdict: functional; second-best alternative; still rejected on rename-cost / metaphor-loss grounds.

**(C) Post-Extraction Externality.**
- Pros: explicit temporal anchor ("post-extraction"); unambiguous.
- Cons: verbose; loses metaphor; rename cost; "post-extraction" too narrow (some Externality Tails — e.g., atmospheric carbon — were generated DURING extraction, just persist after).
- Verdict: functional but narrow; rejected.

**(D) Lingering Externality.**
- Pros: colloquial accessibility; clear temporal sense.
- Cons: too colloquial for formal register; loses Pigouvian anchor; rename cost.
- Verdict: rejected on register grounds.

**(E) Externality Aftermath.**
- Pros: strong rhetorical force; clear temporal sense.
- Cons: loses Pigouvian formal anchor; "aftermath" reads as event-following rather than function-extending; rename cost.
- Verdict: rejected on lineage-anchor grounds.

**(F) Temporal Externality.**
- Pros: clean academic register; explicit temporal anchor.
- Cons: ambiguous (could read as "externality occurring at this time" rather than "externality persisting over time"); abstract; rename cost.
- Verdict: rejected on ambiguity grounds.

**Aggregate alternative-naming verdict:** All six alternatives are functional but each carries trade-offs (metaphor loss, anchor weakening, rename cost, ambiguity, register mismatch). None is sufficiently superior to "Externality Tail" to justify the rename cost (29+ publisher-facing instances + 4 prior rigor passes + chapter prose retraining + case-study sweep). Disambiguation note per Enhancement 1 achieves comparable collision-mitigation at lower cost.

### §11.3 Verdict

- **Counterexample resistance: STRONG.** Internal definition forces temporal-persistence reading; alternative readings produce canonical-definition inconsistency.
- **Alternative-naming feasibility: WEAK.** Rename cost > collision-mitigation benefit; metaphor loss; rhetorical anchor loss. Recommended: keep "Externality Tail" with disambiguation note.

### §11.4 Repair recommendation

Reject rename; apply Enhancement 1 disambiguation per §13.1.

---

## §12. Test 8 — Suffix-coherence (Phase 1 §9.4 bundling)

### §12.1 Current state

[Phase 1 §9.4](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"§9.4 Suffix-convention coherence. One-off suffixes already deferred per Item 4.2: -Identity (Hotelling Identity), -Tail (Externality Tail). The -Estimation suffix removed via Three Ways of Counting rename. No additional suffix concerns surfaced in Phase 1."*

Phase 1 closed the suffix-coherence question with disposition: "-Tail" is acceptable as a one-off suffix because:
- "-Identity" and "-Tail" both have domain-specific lineage (Identity from accounting / mathematics; Tail from statistics / temporal-flow).
- Forcing a uniform suffix convention would impose a vocabulary-discipline cost without semantic benefit.
- Each suffix carries its own lineage and reads naturally in context.

### §12.2 Verdict

**CONFIRMED ACCEPTABLE per Phase 1 §9.4 prior disposition.** No additional concern at Phase 2 depth. The collision-check (Test 2 + 6 + 7) is the load-bearing concern; suffix-coherence is closed.

### §12.3 Repair recommendation

None. Phase 2 audit confirms the Phase 1 §9.4 disposition.

---

## §13. Recommended formal restatement

### §13.1 Enhancement 1 — Explicit disambiguation note at three locations

**(a) terms_index Externality Tail entry — add new "Notational disambiguation" subsection:**

Insert into `tools/back-matter/sources/terms_index.md` Externality Tail entry (between current "M12 lineage" subsection and "Term-spec version" line) the following ~120-word block:

> **Notational disambiguation.** The framework's "Externality Tail" refers to **temporal persistence of damage post-extraction** (the tail of the damage curve in time, per the rhetorical anchor "runs on its own clock"), not to the **statistical-distribution sense** of "tail" used in finance / actuarial / extreme-value-theory / risk-management literature (e.g., Mandelbrot 1963 fat-tailed price distributions; Taleb 2007 Black Swans; ruin-theory tail risk per Embrechts, Klüppelberg & Mikosch 1997; long-tail in business per Anderson 2006). The two senses share the underlying geometric intuition — tail = part far from the central mass — but the framework's domain is **time** (when does damage occur?) while statistics-distribution-tail's domain is **probability** (how extreme are the values?). E(R, t) is a deterministic time-indexed cost function, not a probability distribution; it does not exhibit extreme-value behavior in the statistics sense.

**(b) Tech Appendix §B Definition A.4 — extend with disambiguating parenthetical:**

Replace at Tech Appendix v1.0.0 line 455:

> *Replace:* "E(R, t) ≥ 0 for all t, and typically exhibits a long tail: E(R, t) > 0 for many generations after extraction ceases."
>
> *With:* "E(R, t) ≥ 0 for all t, and typically exhibits a **long tail in time**: E(R, t) > 0 for many generations after extraction ceases. The 'tail' here is temporal — the persistence of damage after extraction ends — not the statistical-distribution sense of tail used in extreme-value theory, heavy-tail finance literature, or actuarial ruin theory."

**(c) Glossary v3 entry — append disambiguating sentence:**

Append to existing entry:

> *Append at end of definition:* " (Note: 'tail' here is temporal — the lingering damage after extraction — not the statistical sense of tail used in extreme-value theory or finance.)"

### §13.2 Enhancement 2 — Bibliography expansion citing divergent lineages

Add to bibliography:

- **Mandelbrot, Benoit. 1963.** "The Variation of Certain Speculative Prices." *Journal of Business* 36(4): 394-419.
- **Taleb, Nassim Nicholas. 2007.** *The Black Swan: The Impact of the Highly Improbable*. New York: Random House.
- **Embrechts, Paul, Claudia Klüppelberg, and Thomas Mikosch. 1997.** *Modelling Extremal Events for Insurance and Finance*. Berlin: Springer.
- **Anderson, Chris. 2006.** *The Long Tail: Why the Future of Business Is Selling Less of More*. New York: Hyperion.

(Pigou 1920 + Nordhaus & Boyer 2000 + Stern 2007 already in bibliography per Externality Tail M12 lineage from 2026-04-24 individual rigor pass.)

These four citations are NOT load-bearing on the framework's substantive claims; they are anchor-references for the Enhancement 1 disambiguation note, supporting reader recognition of the divergent lineages.

---

## §14. Verdict + ratification choices

### §14.1 Recommended verdict

**KEEP "Externality Tail" terminology with two concrete disambiguation enhancements per §13.** The substance is sound; the term is metaphorically correct + rhetorically anchored ("runs on its own clock"); domain of applicability is consistent across 29+ framework appearances; internal definition forces temporal-persistence reading. The repair work is disambiguation-discipline + citation, not rename or re-derivation.

Two concrete enhancements:

1. **Enhancement 1: Disambiguation note at three locations (per §13.1)** — terms_index Externality Tail entry; Tech Appendix §B Definition A.4 first appearance; glossary v3 entry. Closes Tier 2a-finance/IO + Tier 2e collision-exposure gap.

2. **Enhancement 2: Bibliography expansion (per §13.2)** — Mandelbrot 1963; Taleb 2007; Embrechts et al. 1997; Anderson 2006. Anchors the disambiguation note for academic-recognition.

### §14.2 Pass-fail verdict on as-currently-written Externality Tail terminology

**ADEQUATE-WEAK.** Survives sympathetic-referee review at top-tier journals on internal-coherence grounds (math forces temporal-persistence reading) but flagged on first-encounter misread risk for finance / IO / quant readers. Currently no explicit disambiguation against statistics-distribution-tail conventions.

### §14.3 Pass-fail verdict on enhanced Externality Tail per §13

**STRONG.** With disambiguation note + bibliography expansion applied, terminology meets academic-peer-review standards. Multi-audience misread risk closed for highest-exposure tiers (Tier 2a-finance/IO + Tier 2e). Citation discipline anchors the disambiguation against established literatures.

### §14.4 Author ratification choices

**(a) Full ratify §13 enhancements** — both enhancements applied; terms_index + Tech Appendix + glossary edited; bibliography expanded. **Recommended.**

**(b) Rename to alternative** — six alternatives tested in §11.2; all rejected on rename-cost / metaphor-loss / anchor-weakening grounds. Author override possible — alternative B (Externality Persistence) is least-bad if rename is preferred.

**(c) Partial ratify** — adopt subset:
- (c.i) terms_index disambiguation note only (highest-leverage location).
- (c.ii) terms_index + Tech Appendix Definition A.4; defer glossary v3 + bibliography.
- (c.iii) All disambiguation notes, defer bibliography expansion.

**(d) Modify verdict** — author specifies different recommendation (e.g., shorter disambiguation note; different citation set; different placement).

**(e) Defer Phase 2 ratification** — additional questions before locking; possibly bundle with sibling Phase 2 audits for combined ratification.

**(f) Reject** — author rejects audit findings (would require justifying why current Externality Tail usage survives academic peer review without disambiguation; possible justification: Tier 2a-finance/IO + Tier 2e are not the framework's primary academic audience per vocabulary-strategy multi-audience matrix prioritization).

**Recommendation: (a) Full ratify.** Two enhancements are mutually-reinforcing; partial ratification leaves disambiguation gaps at one or more entry-points. Total text added: ~175 words across three locations + 4 bibliography entries. Substantial gain in Tier 2a-finance/IO + Tier 2e collision-resilience; modest implementation cost.

### §14.5 Implementation pending after ratification

If (a) full ratify:
1. `tools/back-matter/sources/terms_index.md` Externality Tail entry — insert §13.1 (a) disambiguation note ~120 words.
2. Tech Appendix v1.0.0 HTML §B Definition A.4 line 455 — replace with §13.1 (b) extended text.
3. Glossary v3 entry — append §13.1 (c) disambiguating sentence.
4. Bibliography expansion per §13.2 (Mandelbrot 1963; Taleb 2007; Embrechts et al. 1997; Anderson 2006).
5. terms_index — append Phase 2 verdict entry; cross-reference to this rigor pass.
6. Open Insights — new Insight # closed-ratified entry capturing Phase 2 #5 verdict (number TBD).

**Same open question as Insights #35 + #38 + #40 + Phase 2 #8 + Phase 2 #7 + Phase 2 #6 Tech Appendix HTML edit timing:** apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Possible unification:** all Phase 2 Tech Appendix changes batched into Phase 3 v2.0.0 rebuild as single coordinated update.

### §14.6 Pre-publication external review (Insight #39)

This rigor pass produces Claude's assessment of Externality Tail collision-resilience. Per Insight #39, eventual external review by economics PhD + finance/risk-management practitioner or actuary is warranted before publication. Specifically for Externality Tail:
- A finance/risk-management reviewer should verify the disambiguation note adequately separates "Externality Tail" from extreme-value-theory / heavy-tail / Black Swan vocabulary.
- A welfare-economics reviewer should verify the Pigouvian distinctness (4-axis) is preserved in the enhanced terminology.
- The bibliography expansion (Mandelbrot 1963; Taleb 2007; etc.) should be verified for citation appropriateness vs. alternative anchor references.

This rigor pass does NOT replace external review; it produces the substrate that external review would test.

---

## §15. Open questions for author discussion

1. **Disambiguation note length.** Enhancement 1 (a) terms_index note is ~120 words. Author preference: tighter (~80 words; drop one or two of the cited literatures) vs current (comprehensive across four divergent lineages)?

2. **Bibliography citation set.** Enhancement 2 adds 4 references. Are all needed, or can the citation set be reduced to 2-3 (e.g., Mandelbrot 1963 + Taleb 2007 only — covering the highest-leverage divergent lineages)?

3. **Tech Appendix Definition A.4 wording.** Enhancement 1 (b) currently uses "long tail in time" as the temporal-anchor phrasing. Alternative options: "long temporal tail" / "long-running tail" / "extended temporal persistence." Author preference?

4. **Glossary v3 disambiguation length.** Enhancement 1 (c) appends ~25 words. Could be expanded to ~40-50 words for fuller disambiguation, or kept terse. Trade-off: glossary discipline favors brevity; collision-mitigation favors fullness.

5. **Cross-coordination with Phase 2 #6 [TWoC-adoption] + Phase 2 #7 + Phase 2 #8.** Combined Tech Appendix edits across Phase 2 audits are accumulating. If §14.4 (a) ratified, this Phase 2 #5 adds ~120 words at terms_index + ~30 words at Tech Appendix Definition A.4 + ~25 words at glossary v3 + 4 bibliography entries. Combined Phase 2 #5-#8 Tech Appendix edits would be ~500 words + multiple new sub-sections + ~14 new bibliography entries. **Recommend batched application during Phase 3 Tech Appendix v2.0.0 rebuild rather than incremental v1.0.0 edits.**

6. **Tech Appendix HTML edit timing.** Same open question as Insights #35 + #38 + #40 + Phase 2 #8 + Phase 2 #7 + Phase 2 #6: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild?

7. **Phase 2 #4 [RCV-acronym] interaction.** RCV acronym collision audit is the next + final Phase 2 audit in this session's reverse-priority sweep. Both audits sit in vocabulary-collision-discipline territory. Note for sequential reading; no direct file-level interaction.

---

## §16. Cross-references

### §16.1 Upstream rigor passes

- [Phase 1 full framework audit §6.11 + §9.4 + §9.5 + §10 #3 + §12.2](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md) — flagged Externality Tail statistics-tail collision for Phase 2 deeper-dive; suffix-coherence closed at §9.4.
- [Externality Tail individual rigor pass 2026-04-24](tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_term_externality_tail_v1.0.0.md) — RATIFIED 2026-04-24; Ring-2 promotion under current naming; 4-axis distinctness from Pigouvian externality preserved; this pass extends with collision-disambiguation.
- [Phase 2 Theorem E.4 Integral Convergence](tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #40); Theorem E.4 restructured premises A2 includes E polynomial-growth bound; Externality Tail disambiguation here is non-disruptive to E.4 proof structure.
- [P2#8 RCV integrand Q(t) notation-clarity](commons_bonds_rigor_pass_2026-04-29_phase2_rcv_integrand_q_notation_clarity_v1.0.0.md) — [PROPOSED] 2026-04-29; sibling Phase 2 audit; methodology-precedent.
- [P2#7 Scarcity multiplier formula academic-defensibility](commons_bonds_rigor_pass_2026-04-29_phase2_scarcity_multiplier_academic_defensibility_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #47); methodology-precedent.
- [P2#6 Three Ways of Counting post-rename adoption-fit](commons_bonds_rigor_pass_2026-04-29_phase2_three_ways_of_counting_adoption_fit_v1.0.0.md) — [PROPOSED] 2026-04-29; sibling Phase 2 audit.
- [Phase 2 Foreclosure Bond housing-crisis collision](tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #38); methodology template — collision-disambiguation pattern.
- [Phase 2 Cost Severance + Severed Cost Tier 2d](tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #35); methodology template.
- [Vocabulary strategy v1.0.1 §2 + §8 multi-audience matrix](alignment/commons_bonds_vocabulary_strategy_v1.0.1.md) — Tier 2a-finance/IO + Tier 2e collision-exposure discipline applied here.

### §16.2 Sibling Phase 2 candidates (concurrent + remaining)

- **Phase 2 #3 Theorems E.1, E.3, E.5, Renewable Imperative academic-rigor proof-structure audit** — sibling session in progress 2026-04-29. E(R, t) appears in restructured premises A2 (RATIFIED Insight #40 Theorem E.4) and may appear in E.1/E.3/E.5 sibling theorem audits. The disambiguation enhancement here is non-disruptive to theorem proofs.
- **P2#8 [Q(t)] RCV integrand Q(t) notation-clarity** — [PROPOSED] 2026-04-29.
- **P2#7 [scarcity-multiplier] Scarcity multiplier formula academic-defensibility** — RATIFIED 2026-04-29 (Insight #47).
- **P2#6 [TWoC-adoption] Three Ways of Counting post-rename adoption-fit** — [PROPOSED] 2026-04-29.
- **P2#4 [RCV-acronym] RCV acronym collision audit** — pending (next + final in this session's reverse-priority sweep).

### §16.3 Downstream artifacts (this pass would update on ratification)

- `tools/back-matter/sources/terms_index.md` Externality Tail entry — insert §13.1 (a) Notational disambiguation subsection.
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` §B Definition A.4 line 455 — replace with §13.1 (b) extended text.
- `tools/back-matter/sources/glossary/archive/commons_bonds_updated_glossary_v3.html` Externality Tail entry — append §13.1 (c) disambiguating sentence.
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` bibliography section — Mandelbrot 1963; Taleb 2007; Embrechts et al. 1997; Anderson 2006 additions.
- `tools/back-matter/sources/terms_index.md` — append Phase 2 verdict entry; cross-reference to this rigor pass.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight # closed-ratified capturing Phase 2 #5 verdict (number TBD).

### §16.4 Pre-publication external review (Insight #39)

This rigor pass + 4 sibling Phase 2 deeper-dive passes (#8, #7, #6, #4) + 4 sibling theorem rigor passes (E.1, E.2, E.3, E.5) produce Claude's pre-external-review assessment substrate. Per Insight #39, eventual external review by economics PhD + finance/risk-management practitioner is warranted. For Externality Tail specifically, a multi-disciplinary review (welfare economist + finance/risk practitioner or actuary) would verify the disambiguation against statistics-distribution-tail conventions adequately addresses cross-literature collision exposure.

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED — pending author ratification].**
