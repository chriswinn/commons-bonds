# TA Tautology Verification — B vs RCV + the Hotelling Identity

**Status: VERIFICATION COMPLETE (findings RATIFIED-as-fact); WORDING FIXES PROPOSED (author-gated).**
**Date: 2026-06-17**
**Trigger:** `tools/audits/matrix-independent-verification_2026-06-17.md` §3 #1 / §4 #3 — the
single finding the matrix-independent synthesis "could not verify either way," flagged as the
deepest exposure to a quantitative methodologist. Settled here against the canonical TA
(`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`, 8,361 lines) by direct read +
grep of §1, §3, §4, §10, §14, §15.1.4, plus a full-corpus sweep of chapters, essays, op-eds,
proposal, and ledgers.

---

## TL;DR

**Neither claim is a fatal tautology. Both carry genuine empirical content at the TA level.**
The TA already handles the exposure with strong discipline — it does *not* call B < RCV a
theorem. The only live exposures are:

1. A **terminological looseness** in the §4 "Hotelling Identity" naming (the word "Identity"
   + a reused "CS" symbol) that *invites* the tautology charge even though the underlying
   content is sound. → optional author-gated TA hardening.
2. A **"theorem" over-claim that lives ONLY in internal scaffolding** — the contribution
   matrix + two older ledgers — and in **zero** publisher-facing prose. Because the matrix is
   a drafting source for essays, this should be corrected preventively. → internal fix.

The audit/task framing also carried **two factual inaccuracies** (corrected below): the
identity equals **Cost Severance**, not "consumer surplus"; and at the TA level B < RCV is an
**Empirical Observation**, not a theorem.

---

## 1. The central question: are RCV, Hotelling rent, and B independent — or definitional?

| Quantity | How defined | Independent? | Where |
|---|---|---|---|
| **RCV** (Residual Commons Value) | Integral of foreclosure cost + externality tail, discounted: `RCV = ∫{[1−S]·U + E}·D dt`. Estimated three independent ways (Method 1 replacement cost; Method 2 revealed preference; Method 3 scarcity-adjusted option value) and triangulated; computed per-case in §11. | **YES — independently estimated.** Not a residual. | Def 1.6 (L506–544); §3.3–§3.6; §11 |
| **Hotelling rent** | Standard resource-economics quantity: price − marginal extraction cost, rising at rate *r* (Hotelling 1931). | **YES — standard, observable.** | §4.1 (L1273–1283); §14.1 (L6845) |
| **B** (Accountability Bond) | Per-unit dollar value of accountability mechanisms *actually in operation* — severance taxes + reclamation/decommissioning bonds + carbon taxes + SWF Hartwick coverage. "B measures what is *posted*, not what is owed." | **YES — independently observed.** **NOT defined as a fraction/share of RCV.** | Def 1.7 (L546–556); Emp. Obs. 10.1b Assumption (iv) (L3474) |
| **CS** (Cost Severance) | The one **defined residual**: `CS ≡ RCV − B`. | Definitional — *and labeled as such*. | Def 1.7 (L552); Theorem 10.1a |

**This directly defeats the Concern-1 premise.** The concern was: "if B is defined as a ≤1
share of RCV, then B < RCV is true by construction." **B is not a share of RCV.** It is the
independently-observed sum of posted accountability mechanisms (≈ 0 relative to RCV in the
McDowell coal case; Norway's realized fund in the oil case — §11). So `B < RCV` (i.e. `CS > 0`)
requires the **independently-estimated RCV to exceed the independently-observed B** — an
empirical claim, not a definitional one.

---

## 2. The TA already separates the tautology from the result (exemplary discipline)

§10 bifurcates the claim exactly the way a hostile economist would demand:

- **Theorem 10.1a (Cost Severance Identity)** — the *only* "theorem" here — proves **only the
  trivial sign-identity**: `CS > 0 ⇔ B < RCV`. Proof in full (L3451): *"By Assumption (i),
  CS = RCV − B. Therefore CS > 0 ⇔ RCV − B > 0 ⇔ B < RCV. ∎"* This **is** a tautology, and the
  TA **honestly labels it an *identity*** and claims nothing more from it. ✔ No over-claim.

- **Empirical Observation 10.1b (Structural Cost Severance under Current Institutions)** — the
  substantive claim that B *is actually* < RCV in the real world — is **explicitly NOT a
  theorem.** It carries premises (Coase intergenerational-incompleteness; Pigou partial
  pricing; empirical instrument-inadequacy), a **falsifiability clause** (L3531: a single
  case with B ≥ RCV refutes it), and a **domain of applicability**. The TA states *why* it is
  not a theorem (L3537): *"presented as an empirical observation rather than a theorem because
  its operative content is empirical … the load-bearing premise (Premise (iii)) is an
  empirical regularity established by the §11 cases, not derivable from primitive premises."*

Verified labeling: the TA uses **"Empirical Observation 10.1b"** at every occurrence; the
string **"Theorem 10.1b" does not exist** in the TA. Genuine theorems (10.3 Abundance Masking;
10.4 Integral Convergence) are derivable limit results with real proofs — correctly labeled.

**Conclusion (Concern 1):** at the TA level the tautology charge does not land. The
definitional part is labeled an identity; the empirical part is labeled an empirical
observation with falsifiability. This already reflects the **2026-06-06 "claim less" audit
lesson** ("the audit caught proofs that restate premises").

---

## 3. The Hotelling Identity — empirical content, loose label

The §4 identity is **`RCV per unit − Hotelling rent per unit = CS per unit`** (L1290) — note:
**Cost Severance, not "consumer surplus."**

**It is not a definitional rearrangement of one quantity into a sum of others.** It is the
**difference of two independently-defined quantities** — the RCV integral (Def 1.6) and the
standard Hotelling private rent (Hotelling 1931). §14.1 (L6842–6845) is explicit: *"RCV adds
to Hotelling … The Hotelling price path is P(t)=P(0)·e^{rt}. The RCV augments this with the
foreclosure cost ∫[1−S]U·D dt."* The number `RCV − Hotelling rent` is therefore a real
computed magnitude, not a definitional zero. **Empirical content: present.**

**The genuine, reviewer-catchable exposure is naming, not substance:**

- **(a) "Identity" over-signals definitional truth.** In econ usage an "identity" is true by
  construction (an accounting identity). The §4 relation is really a *conditional bridge* — it
  holds when the extractor posts exactly the private Hotelling rent (B = Hotelling rent), which
  §4.2 does state ("when extraction prices the standard Hotelling rent…", L1300) and §15.1.4
  qualifies ("when 'value' is defined as RCV", L7047). But the bare label "Identity" hands a
  methodologist the tautology framing on a plate.
- **(b) The "CS" symbol is overloaded.** `CS = RCV − B` (Def 1.7, B = posted bond) and
  `CS = RCV − Hotelling rent` (§4) **coincide only when B = Hotelling rent.** Same symbol, two
  differents. A careful reviewer flags this immediately.

Neither is fatal; both are exposition fixes (see §6, FIX 2).

---

## 4. The robustness claim is genuine robustness (not its opposite)

Concern 2 feared: "if RCV is *defined* as the sum of the other terms, then CS > 0 is true by
definition and is the OPPOSITE of robustness." **RCV is not defined that way** (it is the
integral), so this does not apply. The actual claim — *"CS > 0 holds across the entire
plausible discount rate range; only the magnitude varies"* (§14.3 L6869; §11.8 L7806) — is a
real sensitivity result:

- RCV is **re-computed at each discount rate**: $526/ton (Stern, r₀=1.4%) → $537 → **$541/ton
  (Nordhaus, r₀=5.5%)** (L4043). The conclusion (RCV ≫ B; IPG ≥ 5×) **survives the most
  adversarial, RCV-minimizing discount choice.** That is what robustness means.
- §11.8 (L7806): "CS > 0 across all parameter combinations tested" — varying discount rate,
  S_max, SCC, and externality-tail length, all **inputs** to the integral. Independent inputs,
  not a tautology.

---

## 5. Two factual corrections to the audit/task framing

1. **The identity equals Cost Severance (CS), not "consumer surplus."** "Consumer surplus"
   appears **nowhere** in the TA and is **not any identity** in the corpus (the one corpus hit
   is an unrelated cost-benefit objection in a Harper's rigor doc). The task's "consumer
   surplus" wording is a mis-expansion of the abbreviation "CS." *(The audit's own §3 #1
   correctly wrote "CS per unit"; the expansion drifted downstream.)*
2. **At the TA level, B < RCV is an Empirical Observation, not a theorem.** The only theorem
   is the trivial definitional sign-identity (10.1a). The audit's strong form — "these are
   tautologies dressed as results; retire the word *theorem*" — **does not survive TA
   verification**, because the TA already did the retiring.

---

## 6. Where the exposure actually lives + recommended fixes

### Corpus state (full sweep)
- **Chapters:** clean. Ch6 (L331) calls it **"the framework's bridge"** — not a theorem. Ch7
  (L121) correctly cites the genuine **Theorem 10.3 (Abundance Masking)**. No chapter calls
  B < RCV or the Hotelling Identity a theorem.
- **Essays / cover-letters / op-eds:** **zero** "theorem" usages for these claims. The essays
  carry "conservative by construction" as an *epistemic-posture* phrase (the estimate is a
  floor, biased down) — distinct from, and not to be slid into, "CS > 0 by construction." Deep
  passes repeatedly note the essays *under-deploy* even this.
- **Proposal:** the pre-publication review queue (`pre-publication-review-queue_2026-06-11.md`
  L20/28/36) is **model-correct** — it distinguishes "the appendix's theorems and empirical
  observations," names "the Hotelling Identity derivation" as un-refereed, and recommends a
  welfare-economics theorist as a priority external reviewer.
- **The over-claim lives in exactly 3 internal-scaffolding files** (and nowhere else):
  - `manuscript/ledgers/_contribution-matrix-lens_v2_2026-06-15.md:98` — "aggregate B <
    aggregate RCV is a theorem" (current matrix; the live drafting source — highest priority)
  - `manuscript/ledgers/_contribution-matrix-lens_2026-06-04.md:116` — "as a theorem … honest
    by construction" (superseded matrix)
  - `manuscript/ledgers/_contribution-matrix-reads_2026-06-04.json:129` — "establishing
    aggregate B < aggregate RCV as a theorem, hence CS > 0" (built against an older 8,044-line
    TA; also mislabels the Coase/Pigou premises "Theorem P1/P2" and the result "Theorem 10.1b"
    — none of which strings exist in the current TA)

### FIX 1 — Matrix/ledger correction *(internal scaffolding; PROPOSED, author-gated per task)*
In matrix meta-claim 3, replace "aggregate B < aggregate RCV is a theorem" with:

> "aggregate B < aggregate RCV is an **empirical observation** (TA Empirical Observation
> 10.1b) — it holds because the *independently-estimated* RCV exceeds the *independently-
> observed* posted bond B, not by definition. The only theorem in the neighborhood is the
> trivial sign-identity CS > 0 ⇔ B < RCV (TA Theorem 10.1a). The Coase/Pigou items are
> *premises* of the empirical observation, not standalone theorems."

Also retire the "Theorem P1/P2" and "Theorem 10.1b" labels in the matrix rows to match the TA.
**Why preventive:** the matrix feeds essay drafting; left as "theorem," a future session could
promote the over-claim into publisher-facing prose.

### FIX 2 — TA §4 hardening *(publisher-facing; PROPOSED, author-gated; optional belt-and-suspenders — the current TA is already defensible)*
Add after the §4.2 identity statement:

> "Both quantities on the left are measured independently: RCV from the foreclosure-plus-
> externality integral (Definition 1.6; triangulated three ways in §3.3–§3.6 and computed
> per-case in §11), and Hotelling rent from the standard price-minus-marginal-extraction-cost
> rule (Hotelling 1931). The relation is therefore not a definitional rearrangement; it is the
> empirical claim that the independently-estimated commons value exceeds the standard private
> rent, the excess being the severed commons cost. Where an extractor posts a bond B equal to
> the Hotelling rent, this CS coincides with CS = RCV − B of Definition 1.7; in general B ≤
> Hotelling rent and the two differences are distinct."

Optional larger move (author decision — ripples to Ch6 + matrix + essays): rename "Hotelling
**Identity**" → "Hotelling **Bridge**" / "Hotelling **Decomposition**" to drop the
definitional-truth connotation.

### FIX 3 — Standing constraint *(already satisfied; codify)*
"No chapter or essay asserts 'theorem' for B < RCV or the Hotelling Identity." Currently true.
Recommend adding it as a `tools/quality-gates/regressed-patterns.yaml` guard so a future
drafting session pulling from the matrix can't reintroduce it.

---

## Verification provenance
Direct read of TA §1 (Defs 1.6/1.7), §4, §10 (Theorems 10.1a/10.3/10.4; Empirical
Observations 10.1b/10.2/10.5), §14.1, §15.1.4; grep-verified labels ("Empirical Observation
10.1b" everywhere, zero "Theorem 10.1b"; zero "Theorem P1/P2"; zero "consumer surplus" in TA).
Full-corpus sweep of `manuscript/chapters/`, `publishing/essays/`, `publishing/op-eds/`,
`publishing/book-proposal/`, `manuscript/ledgers/` on 2026-06-17.
