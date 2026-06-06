# CSD Computation Method — Specification (PROPOSED, 2026-06-06)

**Status:** PROPOSED design spec for author + parallel-session review. Not yet drafted into the TA.
Branch `claude/ta-rigor-audit-260606-f537b4` (held from main). Sequenced **behind** the TA HARD-fix
pass — the reef calibration must be built on a TA whose forward figures are already corrected.

**What this is.** The worked **Cost Severance Damages (CSD)** computation method — the backward
(restitution) counterpart to the forward RCV method. The TA already *articulates* the bidirectional
form `total CS = (CSD − B₁) + (RCV − B₂)` (§5.5) but declares the backward side "outside this
volume's empirical scope." This spec fills that gap: a worked CSD method + the Chesapeake oyster-reef
calibration (Ch3's Restitution Bond case).

**Provenance.** Ratified through the 2026-06-06 design discussion (author). Supersedes the earlier
"cost-to-cure only / demote Method 3" sketch, which the author corrected.

---

## 0. The decision history this encodes (so nothing is re-litigated)

1. CSD is a **bounded range**, not a single number. (Author correction to my "cost-to-cure only.")
2. **No `S_max → 0 ⇒ unpriceable` theorem.** Rejected for three reasons (below).
3. **No "standing" anywhere in the apparatus** — not even "open to anyone." Math is value-free.
4. The author's reason for declining coercion lives in a **first-person authorial note**, in the
   chapters *and* in the TA (visibly distinct from the apparatus).
5. The structural work is done by the **Ostrom-path generative posture** already ratified 2026-05-02,
   not by any new mechanism.

---

## 1. Core principle — CSD is a structured range, floor + moving ceiling

> **CSD is generated as a range. The lower bound is what you can prove; the upper bound moves with
> which cost variables you admit and what values you enter. The framework's contribution is making the
> range — and exactly what drives its ceiling — explicit and gate-disciplined, NOT forcing consensus on
> one complete computation.**

This is the right output because the restitution conversation never converges on a single number or
method. A method that delivers (a) a floor everyone must accept and (b) a transparent, structured menu
of what moves the ceiling is more useful than one that demands agreement — and it lets the author
contribute to that conversation **without entering it**.

- **Lower bound (provable):** Method 1 (cost-to-cure / remediation) + Method 2 (revealed restitution).
- **Upper bound (contested, moving):** floor + Σ additional gate-admitted cost variables Cᵢ, each
  toggled $0 → $X by the Commons Inversion Test (abundance-masking, Theorem 10.3). Method 3
  (scarcity-adjusted option value) is **one** such admittable ceiling variable.

Forward triangulation converges three estimators to a point (the framework's robustness claim).
**Backward triangulation does NOT transfer that convergence** — once uncertainty is resolved, the
methods answer subtly different questions and the honest output is a range. Say this plainly; do not
import the forward convergence epistemology unmodified.

---

## 2. The three methods in reverse

| | Forward | Backward (CSD) | Role |
|---|---|---|---|
| **Method 1** | cost to engineer a substitute commons function | **remediation / cost-to-cure**: foreclosed commons extent × realized restoration unit-cost + flow of commons-services lost over the degraded interval | **Estimates the CSD floor.** Translates with no methodological violence; the interval term is bounded (Gate 3 trivially satisfied). |
| **Method 2** | revealed restraint (Norway GPFG) | **revealed restitution**: what society has *actually paid* to restore comparable harm (NRDA settlements; public restoration programs) | **Comparator, not a third estimator.** Does double duty: (a) corroborates the Method-1 unit-cost, and (b) reveals the **realized B₁** (and who paid it). Per audit finding E12, M2 is the realized-B side of CS = RCV − B, not an RCV estimator. |
| **Method 3** | expected option value under uncertainty (Dixit-Pindyck irreversibility premium; scarcity multiplier) | **option value with uncertainty resolved** | **One admittable ceiling variable, NOT the bond basis.** Backward it forks: ex-post realized value vs. ex-ante correct-value-at-t₀. The framework **exposes** the choice (strict-liability → ex-post; negligence → ex-ante) rather than settling it. Ch5 (line 234) already commits to M3-backward as "the option value extinguished at the time of past extraction, evaluable from what we know now." |

---

## 3. The lower bound (provable floor)

`CSD_floor = Method-1 cure-cost = (foreclosed extent) × (realized remediation unit-cost) [+ bounded interval-services term]`

Corroborated by Method-2 revealed restitution (the per-unit price society has actually paid). This is
the number a hostile reviewer cannot knock over because every input is documented and realized. A
chapter may choose to **publish only the floor** (Ch3 does); that is a presentation choice, not a claim
that the ceiling doesn't exist.

---

## 4. The moving upper bound (already-existing apparatus)

The ceiling is generated by machinery the TA **already contains**:

- **Four Gates (§7)** — the admission discipline for which Cᵢ may enter (CIT scarcity-grounding,
  units consistency, boundedness, independence/non-overlap). Each gate is a structural test on the
  *variable*, computable by anyone, indifferent to who runs it.
- **Commons Inversion Test / Theorem 10.3** — the $0 → $X toggle. Each admittable Cᵢ is a cost the
  relevant commons's abundance masked (was $0) and that scarcity makes legible. (Earth-air-vs-space-air.)
- **§17 sum-of-costs generalization** — `CS = Σ Cᵢ`; "adding correctly-specified Cᵢ widens the gap;
  neither direction's admission can falsify a CS > 0 finding" (line 7623). This **is** the moving-ceiling
  machinery; the CSD range is §17 run backward.

`CSD_ceiling = CSD_floor + Σ (gate-admitted Cᵢ, incl. Method-3 option value, ecosystem-service heads, …)`

The ceiling **moves** with admission choices and input values, and the framework never claims it is
final (see §8).

---

## 5. CSD vs the Restitution Bond B₁

- **CSD** (true backward severance) = the range above.
- **B₁** (the *enforceable* Restitution Bond actually posted) = anchored at the provable floor — you
  bond what you can prove. The polity/affected parties choose where in the CSD range to set B₁.
- `(CSD − B₁) > 0` always; the range tells you how much unrestituted severance plausibly sits above
  the bonded floor.
- **The mis-assignment punch:** currently the public pays B₁ (reef: ~$110M) while the *extractor's*
  B₁ ≈ $0. The bond does not invent a new bill; it **reassigns** B₁ from the public back onto the value.
  "Value disperses up and out; cost stays local and falls to the public" — in the algebra.

---

## 6. Three states of a variable — never collapsed

- **Zero** — under abundance the cost genuinely *is* $0 (CIT toggle).
- **Filled** — someone with standing + data enters a value (the reef floor).
- **Open** — a real, gate-admitted slot deliberately left empty.

**Open ≠ Zero ≠ Unpriceable.** An unfilled admitted Cᵢ means the computed CSD is a **lower bound**
(pure arithmetic — a sum missing a non-negative term). That is the only thing the math says about an
empty slot; it says nothing about *why* it is empty or who should fill it.

---

## 7. What the apparatus must NOT do

**No `S_max → 0 ⇒ unpriceable` theorem.** Rejected because it would:
1. **Overreach morally** — make the framework declare a cost unfillable *by anyone*, which is not the
   author's (or the framework's) to assert.
2. **Gut the framework's usefulness** exactly where it matters most — a user with standing trying to
   price an irreplaceable harm would get a divide-by-zero "give up" instead of a usable high-magnitude slot.
3. **Contradict the framework's own math** — Theorem 10.5 (Substitution Dominance), §13, and §14.6
   already *price* low-substitutability resources, and price them *high*. Divergence as S_max → 0 means
   **"this cost dominates,"** not "this cannot be priced."

**No "standing" in the apparatus** — not even the permissive "open to anyone who has it." The math
defines slots, gates (structural), units, and the sum; it never speaks about who may fill what.
Substitutability may be cited backward only as a **structural characterization** of a slot
(low-S ⇒ would-be-dominant), never as a valuation.

---

## 8. The Ostrom path does the structural work

Ratified 2026-05-02 (`reference_ostrom_illustrative_register.md`; Option C'): **lists are illustrative,
not exhaustive; universality is a property of the *method*, not a closed ontology.** Formally present
in §17.7 ("The Generative Property"). This single posture:

- prevents any absent variable from reading as "zero" or "the ledger is complete" — for *every*
  variable at once, so coercion is never singled out by a special convention;
- carries the forward-looking generative claim: *as reality unfolds, new scenarios and contexts will
  naturally surface variables that can, will, and should be introduced.* The framework's confidence is
  in the method's generativity, not in any finished list. **Strengthen §17.7/§5.5 to state this
  explicitly** (currently only implicit). Value-free, standing-free.

So coercion left unentered is not the framework falling short — it is one not-yet-entered variable
among the many the method anticipates.

---

## 9. The authorial note (coercion) — first-person, outside the apparatus

The only thing specific to coercion is the **author's personal reason for leaving it out of this book.**
It makes no framework claim, no standing claim, no unpriceability claim.

- **Lives in the chapters** (already): Ch1:56 ("a commute and a stolen life do not belong on the same
  line… naming the rhyme is not the same as making them equal"); Ch5:240 (scope boundary); Atlantic:80
  ("what the framework offers is the ledger; what belongs on it, looking backward, is theirs to enter").
- **Also lives in the TA** (ratified placement): a brief, first-person author's-scope-note at §5.5/§1.10,
  **visibly distinct from the apparatus** (not a definition or theorem), so a reader who comes to the
  formal appendix cold meets the restraint where coercion's absence would otherwise be noticed.

**"You're pricing slaves like oyster reefs" answers itself:** the framework prices *some* things
illustratively, claims no complete list, and asserts more variables will come; the author personally
declines to enter coercion in this book and says why — the same way he declines to price fertile soil
to an off-world colony 200,000 years hence, and for the same reason. No special move, no flattening.

---

## 10. Worked example — the Chesapeake oyster reef (Ch3 Restitution Bond)

The case the author **has standing to compute** (his commons; ecological, not human-coercion;
restorable; documented). Numbers from `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md`
(sourced there; do not re-derive new figures here).

- **Method 1 (floor):** foreclosed reef area **2,738 ac** (James River high-quality oyster-rock lost
  1910→1981; Schulte 2017) × realized restoration **$7,300–13,500/ac** (Great Wicomico realized /
  forward-engineering, natural-recruitment lower-Bay basis) = **$20–37M floor**. Bay-wide-average
  step-up (~$77K/ac) → ~$200M.
- **Method 2 (corroboration + realized B₁):** public restoration spend ~**$57K/ac** realized (sits
  between floor and average → corroborates M1 unit-cost); **$92M (MD) / ~$110M (Bay-wide)** already
  posted — *all public*, *zero from the extractive industry*. This is the realized B₁, mis-assigned to
  the public.
- **Method 3 (declined for the bond; available as ceiling):** the foregone fishery / "all the oysters
  that bar would have grown" — Ch3 explicitly declines to price it ("invites an argument I do not need
  to have"). In TA terms: a gate-admittable ceiling variable the chapter chooses not to enter; the bond
  is anchored at the cure-cost floor.
- **Renewable-with-extracted-renewal-structure:** the reef exercises the S_max / Theorem 10.3 machinery
  via destruction of the *regeneration function* (the reef the next set sets on), not drawdown of a
  fixed stock — a different formal object than the forward non-renewable §11 cases, and a feature.

---

## 11. Substantive TA changes this entails

1. **§14.6 Daly fix** (also audit item 23): Daly's claim is **S_max < 1 for critical natural capital →
   maintain the physical stock**, NOT "S_max must equal 1." Fix as a clean structural statement, no
   moral freight. (Load-bearing for the substitutability characterization here.)
2. **§5.5 rewrite:** flip "backward is outside this volume's empirical scope" → "backward is computed
   for the ecological restitution case (reef) via cost-to-cure; Method-3-backward is an admittable
   ceiling variable; the human-coercion case is left to those with standing (authorial note)." Correct
   the symmetric-triangulation sentence to the range framing.
3. **§17.7 strengthen** the generative property into an explicit forward-looking claim (§8 above).
4. **New §11.x** — Chesapeake oyster-reef restitution calibration (worked, §10 above), parallel to the
   forward §11 cases, cross-referenced to Ch3 (figure-cascade coherence).
5. **§5.4/§5.6** — resolve the TA's own flagged open question (line 1447) on B₁-direction moral grounding,
   delivered via the reparations-economics lineage + the authorial note, not a new theorem.
6. **§11.6 M2-is-comparator** clarity (audit E12): backward M2 reveals realized B₁; it is not a third
   RCV/CSD estimator.

---

## 12. Sequencing + coherence

- **Behind the audit fixes.** The reef calibration cross-references forward convergence logic; build it
  on a corrected TA.
- **Figure-cascade coherence.** The reef numbers ($20–37M / ~$200M / $92M / ~$110M) join the cascade
  discipline; reconcile against Ch3 and add them to the canonical figure ledger
  (`manuscript/_CANONICAL_FIGURE_LEDGER.md`) so TA ↔ Ch3 ↔ any reef-touching essay stay aligned.
- **Final confirmation burst** should re-audit the new §11.x reef arithmetic + the §5.5/§14.6/§17.7 edits.

---

## Cross-references
- TA §5.5 (bidirectional), §7 (Four Gates), §10.3 (abundance masking), §10.5 (substitution dominance),
  §11.6 (M2 logic), §14.6 (Daly), §17.7 (generative property).
- `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md` (reef numbers + sources).
- `manuscript/chapters/Chapter__3_TheWaterman.md` (the shipped reef case).
- Chapters Ch1:56 / Ch5:234,240 / Atlantic:80 (the moral/standing beats — unchanged).
- `reference_ostrom_illustrative_register.md` (the generative posture).
- `core/technical-appendix/TA-rigor-audit-ledger_2026-06-06.md` (the forward-fix pass this sits behind).
