# Commons Bonds — Full Rigor Pass: Externality Tail (E)

**Version:** 1.0.0
**Date:** 2026-04-24
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.2.0.md` — full 11-module suite + §22 Path Comparison Mode + §22.4 usefulness-vs-goals alignment + Principle-#2 concept audit + Principle-#3 distinctness vs established externality theory.
**Scope:** Ring-2 individual rigor pass on Externality Tail E(R, t) — sibling cost term to C₁ (foreclosure) in the RCV integrand.
**Status:** rigor pass executed 2026-04-24; pending author ratification.
**Author:** Chris Winn

---

## §1. Executive summary

**RECOMMENDED: Option A — CONFIRM Ring 2 (internal load-bearing). Hold at Ring 2, not Ring 1.** The Externality Tail E(R, t) is load-bearing for the RCV integrand (second canonical cost term alongside C₁), actively used across 46 refs in 18 files, conceptually distinct from Pigouvian externalities via its temporal-persistence framing, and memorably carried by the "runs on its own clock" rhetorical handle.

**However, flag for author:** the PHRASE "externality tail" has Ring-1-travel potential that the FUNCTION E(R, t) does not. If policy / legal discourse adopts "externality tail" as a concept-handle (e.g., "coal's externality tail includes centuries of climate damage"), the phrase travels even if the mathematical function stays framework-internal. Ring-2 classification reflects the framework-vocabulary role; travel potential is noted for adoption monitoring.

**Key conceptual finding — the "own clock" structure:** E's defining feature is **temporal independence from substitutability** — E runs regardless of whether S climbs to 1 or stays at 0. *"A substitute for coal doesn't clean up the mine. A substitute for oil doesn't remove carbon from the atmosphere."* This structural independence is what distinguishes E from a Pigouvian externality and what makes E a sibling-not-subsidiary of S in the RCV integrand.

**Principle-#3 distinctness check (vs Pigovian externalities):**

| Dimension | Pigovian externality | Externality Tail E(R, t) |
|---|---|---|
| Core claim | Cost imposed on third party by transaction | Damage that persists after resource is gone |
| Time structure | Co-temporal with transaction | Post-extraction; runs on own clock |
| Relationship to substitutability | No inherent relation | **Explicitly independent** of S; damage persists regardless of substitute availability |
| Accounting role | Add to transaction cost (Pigouvian tax) | Add to RCV integrand as C₂-equivalent |

**Distinctness verdict:** E is a temporally-specialized externality concept. Retains Pigouvian externality's core intuition (cost-imposed-on-third-party) but adds (a) post-extraction persistence, (b) substitutability-independence, (c) mathematical form as time-indexed function E(R, t). Framework-specific residue is real; passes Principle #3.

**Options tested:**

- **A — CONFIRM Ring 2.** **RECOMMENDED.**
- **B — PROMOTE to Ring 1.** REJECTED — function name isn't a public-adoption target; adding to Ring 1 dilutes adoption-bet focus on Severed Cost / Cost Severance flagship.
- **C — DEMOTE to prose.** REJECTED — load-bearing for RCV integrand; would lose C₂-sibling status.
- **D — RENAME.** REJECTED — "Externality Tail" is evocative ("runs on its own clock") + connects to established externality literature.
- **E — SPLIT** E(R, t) function from "externality tail" phrase. REJECTED — same object; splitting creates needless vocabulary entries.

---

## §2. The question under test

### §2.1 V2 definition

> *"Externality Tail: Damage from extraction that persists after the resource is gone. A substitute for coal doesn't clean up the mine. A substitute for oil doesn't remove carbon from the atmosphere. The externality tail runs on its own clock, independent of substitution status."*

### §2.2 CORE-math role

E appears as the second canonical cost term in the RCV integrand (per Tech Appendix §L formal specification). The RCV integrand is structured as:

- **Cost terms:** Σᵢ Cᵢ — where i indexes cost terms admitted through Four Gates.
- **Canonical terms at current framework state:**
  - C₁ = [1 − S(t|t₀)] · U(R, t, Q(t)) — foreclosure cost
  - C₂ = E(R, t) — externality tail (this term)
  - Additional Cᵢ as admitted via Four Gates

Structural role: E is the cost term that captures damage-persistence post-extraction. Removing E leaves the RCV integrand unable to account for climate debt, mine-tailings, or other persistent extraction damages.

### §2.3 Options

As in §1.

### §2.4 Sub-claims per option

**Option A (confirm Ring 2):**
- SC-A1: E is load-bearing for RCV integrand as C₂-sibling to C₁.
- SC-A2: Distinct from Pigouvian externalities (temporal independence + persistence structure).
- SC-A3: 46 active refs across 18 files — operational use.
- SC-A4: Framework-internal; not a travel-ready public-adoption target as function name.

**Option B (promote Ring 1):**
- SC-B1: "Externality tail" as phrase might travel to policy discourse.
- SC-B2: "Runs on its own clock" is memorable enough for adoption.

**Option C (demote prose):**
- SC-C1: Mathematical role could live in Tech Appendix only.
- SC-C2: Concept carries in prose without named term.

### §2.5 Falsifiers

**Option A is falsified if:**
- E collapses into Pigouvian externality under closer analysis (no framework-specific residue).
- E's role in RCV integrand is shown to be redundant with another cost term.

**Option B is falsified if:**
- Public adoption of function names is shown to be impossible/unlikely.
- "Externality tail" phrase doesn't travel beyond framework-internal usage.

---

## §3. Principle #3 distinctness check

### §3.1 Established externality theory

- **Pigou 1920:** cost imposed on third party by a transaction; remedy via Pigouvian tax.
- **Coase 1960:** externalities resolved by assignment of property rights + negotiation.
- **Environmental economics:** pollution, climate damage, etc. — generally co-temporal with emission.

### §3.2 E's framework-specific features

1. **Post-extraction persistence:** E continues running AFTER the resource is gone. Standard externalities are associated with ongoing transactions; E's distinguishing feature is that extraction ends but damage continues.
2. **Substitutability-independence:** E is explicitly NOT a function of S. A substitute for coal doesn't retroactively clean up the mine. This makes E structurally independent from the foreclosure-cost branch of RCV.
3. **Time-indexed function form:** E(R, t) not just a scalar externality.
4. **Rhetorical anchor:** "runs on its own clock" captures the temporal-independence in memorable form.

### §3.3 Could E collapse into "climate damage" or "persistent pollution"?

Specialized terms in environmental economics cover similar ground:
- Climate debt / cumulative emissions
- Legacy pollution
- Persistent externality

Each covers a subset of E. None has E's full temporal-independence framing combined with the RCV-integrand mathematical role.

**Verdict:** E has framework-specific residue. Passes Principle #3.

---

## §4. 46-ref concept audit (Principle #2)

### §4.1 Usage distribution

- Ch 7 GuidanceDoc: 10 refs (pedagogical — cases use E to distinguish extraction-window decisions from damage-persistence concerns).
- Ch 6 Draft: 1 ref (mathematical introduction).
- Tech Appendix §L: 1 ref (formal specification).
- Rigor passes (path-F, meta, tier-reframing, etc.): ~24 refs (framework-internal reasoning).
- Glossary: 3 refs.

### §4.2 Ch 7 pedagogical role

E appears in Ch 7's asteroid-miner / Mars-colony thought experiments as the term that doesn't go to zero when the resource is exhausted. The pedagogical pattern: readers learn that substitutes handle foreclosure (C₁) but don't handle damage (E). This pattern is load-bearing for the book's argument that framework handles BOTH cost structures.

Removing E would break this pedagogical pattern.

---

## §5. M1–M11 abbreviated results

- **M1 CORE:** E is structurally load-bearing for RCV integrand. Confirmed.
- **M2 Case study:** Coal mines (tailings persist), oil (carbon persists), Deepwater (biosphere damage persists), asbestos (health damage persists) — all require E. Zero friction.
- **M3 Book content:** 46 refs in active use. Demotion would require significant rewrites.
- **M4 Craft:** "Runs on its own clock" is strong craft. Accounting register preserved.
- **M5 Dinner-table:** "The mess after the resource is gone" — non-expert parses immediately.
- **M6 Academic:** Connects to environmental econ + cumulative-damage literature. Tech Appendix citation recommended (Nordhaus DICE, Stern Review).
- **M7 Originality:** Temporal-independence framing + substitutability-independence structure = framework contribution.
- **M8 Long-term:** Ring-2 durability tied to framework adoption.
- **M9 Risk:** Minor — "tail" metaphor may suggest "small / diminishing" when E can actually GROW (compound damage). Mitigable via Ch 6 clarification.
- **M10 Publishing:** Neutral.
- **M11 Critic:** *"Isn't this just Pigouvian externality?"* — Response: no, E is temporally-independent from substitution + explicitly post-extraction. Survives.

**§22.4 alignment:** Option A positive. Option B also positive but dilutes Ring-1 focus.

---

## §6. Verdict

**OPTION A — CONFIRM Ring 2.** E is load-bearing for RCV integrand as C₂-sibling to C₁; distinct from Pigouvian externalities via temporal-independence framing; memorably anchored by "runs on its own clock" rhetoric; 46 active refs.

### §6.1 What changes

- **Terms Index:** E record populated as `CURRENT` at Ring 2 (first individual rigor pass).
- **Glossary v3:** keep v2 definition; add one-sentence Principle-#3 note clarifying distinctness from Pigouvian externalities.
- **Tech Appendix §L:** add methodological footnote citing Nordhaus DICE + Stern Review + legacy-pollution literature for academic positioning.
- **Ch 6 clarification note:** "tail" metaphor doesn't imply diminishing — E can compound over time (climate cumulative damage).

### §6.2 What doesn't change

- CORE math — unchanged.
- RCV integrand structure — unchanged.
- All 46 existing refs — unchanged.

### §6.3 Flag for author — phrase travel potential

While the FUNCTION E(R, t) is framework-internal (Ring 2), the PHRASE "externality tail" may have adoption-target potential. If policy / legal discourse adopts the phrase ("coal's externality tail," "the externality tail of factory farming"), this travel happens regardless of Ring-1 vs Ring-2 classification. Author may choose to elevate phrase to Ring-1-aspirational status; this rigor pass does not recommend that change (framework's Ring-1 adoption bet stays focused on Severed Cost + Cost Severance + RCV + AIT + Cost + Value Extraction + Commons Bonds).

---

## §7. Term Provenance Record

### Externality Tail (E)

**Working definition:** Time-indexed cost function E(R, t) — damage from extraction of resource R at time t that persists independently of substitute availability. Sibling to foreclosure cost C₁ in the RCV integrand; runs on its own clock (temporally independent of S); structurally specializes Pigouvian externality concept with post-extraction persistence + substitutability-independence.

**Status:** `CURRENT` at Ring 2 (recommended by this pass).

**Term-spec version:** v1.0 (first individual rigor pass on this term).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 — identified as Ring-2 internal load-bearing.
- This individual rigor pass — Option A (confirm Ring 2) verified with concept audit + distinctness check.

**Why Ring 2 (not Ring 1):**
- E(R, t) is a function name; policymakers adopt named quantities (RCV), not named functions.
- Ring 1's adoption bet is concentrated on Severed Cost + flagship terms; expanding dilutes.

**Why NOT demoted:**
- Load-bearing for RCV integrand as C₂-sibling to C₁.
- Ch 7 pedagogical role teaches the foreclosure-vs-persistence distinction.
- 46 active refs.

**Depends on:** RCV integrand structure · "extraction" concept · "persistence" concept.

**Pairs with:**
- Substitutability Function (S) — sibling cost-term contributors to RCV integrand.
- Foreclosure Cost (C₁) — sibling in the canonical cost terms.
- Four Gates — E passes through Gates like any admitted Cᵢ.

**Staleness triggers:**
- CORE math restructured to eliminate E as separate term.
- Academic field produces an established term that should displace "Externality Tail."
- Policy discourse adoption of "externality tail" phrase reaches threshold for Ring-1 promotion consideration.

**Notes:**
- "Tail" metaphor does NOT imply diminishing; E can compound (climate cumulative damage). Ch 6 clarification recommended.
- Framework-specific residue vs Pigouvian externality: (1) post-extraction persistence, (2) substitutability-independence, (3) time-indexed function form, (4) "own clock" rhetorical anchor.
- Phrase "externality tail" has Ring-1-travel potential flagged for monitoring.

---

## §8. Author-ratified resolutions

*Pending author ratification. Recommended Option A (confirm Ring 2).*

---

## §9. Rerun gate

Rerun if:
- CORE math restructures to eliminate E as separate RCV integrand term.
- "Externality tail" phrase adoption reaches threshold for Ring-1 promotion.
- Academic field produces established terminology that should displace.

---

*End of individual rigor pass v1.0.0. Option A (confirm Ring 2) recommended. E is structurally distinct from Pigouvian externalities via temporal-independence + substitutability-independence; load-bearing for RCV integrand as C₂-sibling to C₁. Pending author ratification.*
