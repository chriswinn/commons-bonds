# Standard-notation reserve + alignment — PROPOSAL (2026-06-09)

**Status: PROPOSED. Apply nothing.** Publisher-facing math: propose → author ratifies → apply
(per the Interactive Ratification Protocol, Amendment C). This is the WS3 deliverable of the
back-matter-consolidation session. It re-runs the symbol collision sweep against the **merged**
TA (`origin/main` fd12275 + this session) and proposes (a) a refreshed reserve pool and (b)
alignment options for the residual standard-notation risks. Companion to the synced
`symbol-registry_2026-06-07.md` (Parts 4–6).

## Headline finding

**The merged TA's residual standard-notation risk is LOW.** The closeout already resolved the
dismissal-grade items (σ→ς, δ→κ, E-region→Ω, §16.2 α,β→ζ,ω, log→ln, τ overload, §10 A/P→roman).
A fresh grep of the merged TA shows the remaining "risks" the registry flagged are now minor or
near-moot. Each below carries Options + Recommendation + Reasoning. **No item is dismissal-grade;
none blocks publication. These are polish-tier refinements for the author to accept or decline.**

---

## Item 1 — Externality function E(R,t) vs expectation operator E[·]

**Merged-TA fact:** `E[` (expectation operator) appears **0 times** in the TA. The collision is
therefore purely *reader-expectation* (a finance/stats-literate referee reads `E` and primes for
`E[·]`), not an internal ambiguity.

- **Option A — rename** E(R,t) → ℰ (script E) or Ξ everywhere (§1.4, §16.1, §17 + the glossary
  term "Externality Tail (E)"). High blast radius; breaks the E-for-Externality mnemonic.
- **Option B (RECOMMENDED) — keep E, add one disambiguation line** in the reader Notation section:
  "E(R,t) denotes the deterministic externality-tail flow, not a statistical expectation E[·]."
  The glossary already distinguishes the temporal "tail" from the statistical tail; this extends
  that discipline one step.
- **Option C — do nothing.**

**Recommendation: B.** **Reasoning:** E(R,t) is a named framework primitive with a glossary entry;
renaming it is costly and mnemonic-breaking, and there is no *internal* E[·] to collide with. A
one-line note is proportionate to a reader-expectation-only risk.

## Item 2 — Accountability Bond B vs "billion" magnitude suffix

**Merged-TA fact:** the bare-`NNNB` billion-suffix pattern now appears **once** (`21,268B`, the
GPFG NOK figure). The registry's old "~50 occurrences" estimate (I-5, deferred) is **stale** — the
closeout's worked-number cleanups largely spell out "billion" or use "$Xbn" already.

- **Option A (RECOMMENDED) — normalize the lone survivor:** `NOK 21,268B` → `NOK 21,268 billion`
  (or `21,268 bn`). One-character-class edit; removes the last bare-B-billion adjacency.
- **Option B — leave it** (context + the `21,268` magnitude make "billion" unambiguous).

**Recommendation: A** (trivial) **or B** (acceptable). **Reasoning:** B-the-bond is a core,
un-renameable framework variable; the incidental magnitude suffix is the thing to adjust, and
there is now only one. This effectively closes registry item I-5 (no longer a ~50-site coordination
problem).

## Item 3 — Proof bound M vs "million" suffix

**Merged-TA fact:** `M` as the §10.3 proof divergence-bound is local to one proof; "million"
suffixes (`$1M`, `600M`, `3M`, …) live in §11 worked numbers — **different sections**, no adjacency.

- **Option A — normalize "million" suffixes to "mn"/"million"** in §11 for consistency with Item 2.
- **Option B (RECOMMENDED) — no action.** The proof-M and the million-M never co-occur.

**Recommendation: B.** **Reasoning:** section separation already disambiguates; the risk is lower
than Item 2's. Bundle into A only if the author wants global magnitude-suffix consistency.

## Item 4 — Theorem 10.3: (i)–(iv) used for BOTH conclusion clauses and assumptions

**Merged-TA fact:** the §10 relabel resolved the A/P collision by moving Assumptions/Premises to
roman `(i)–(iv)` and cost-function properties to `(a)–(d)`. But within Theorem 10.3, `(i)–(iv)`
now labels both the *assumptions* ("Assumption (ii)") and the *conclusion clauses* ("Proof of (i)").
Currently prefix-disambiguated; a referee skimming still sees "(i)" mean two things.

- **Option A (RECOMMENDED) — split by case:** conclusion clauses → **uppercase roman (I)–(IV)**;
  assumptions stay **lowercase roman (i)–(iv)**. One-glance distinction; no collision with the
  `(a)–(d)` cost-function properties.
- **Option B — keep prefix-disambiguation** ("Assumption (i)" vs "Proof of (i)"); it is already
  unambiguous on a close read.
- **Option C — conclusion clauses → (a)–(d)**: REJECTED (collides with cost-function properties).

**Recommendation: A.** **Reasoning:** publisher-facing math benefits from one-glance disambiguation;
upper/lower roman is a standard convention. Scope is local to Theorem 10.3 (low blast radius).
Caveat: `(i)–(iv)` is also used pervasively as a generic enumeration device elsewhere — Option A
applies *only* to Theorem 10.3's conclusion clauses, not a global change.

---

## Reserve pool — refreshed against the merged TA (for future quantities)

Confirms/updates registry Part 6. **Governing principle (unchanged):** "unused in this corpus" ≠
"free of reader-brought meaning" — vet any new symbol against BOTH the used-symbol inventory
(internal collision) AND standard-notation baggage (reader-expectation collision). Default for a
new quantity: a descriptive/subscripted name, not a bare letter.

**TAKEN (live in the merged TA — do NOT reuse):** s, R, P, A, Q, S, U, E, D, B, C, M, K, T, V;
Greek ς α ρ λ τ ξ η ε δ κ ζ ω Σ; plus the standard proof set (ε, δ, M, K as local proof variables).

**GENUINELY FREE, low reader-baggage (recommended draw order):**
- Greek: **ι** (iota — cleanest), **ψ** (psi — minor wavefunction/digamma baggage).
- Capitals: **F, G, J, N** (verify each at point of use; G carries gravitational/Gibbs baggage in
  physics-literate registers; N reads as "count/natural numbers" — acceptable).
- Lowercase: **a, b, w, v, y, z** (b is cleanest; v/w/y/z low-baggage).

**AVOID despite being internally free:** **H** (Hamiltonian / enthalpy / entropy — heaviest standard
baggage of any free capital); θ, π, μ, φ (option-Greek / constant / drift / normal-density baggage,
per Part 6).

---

## Apply path (when ratified)

Each item is independent. On author ratification, apply via a dedicated notation session that owns
the TA (same pre-push reconciliation discipline). Items 1–3 are ~1–2 edits each; Item 4 is local to
Theorem 10.3. After apply: re-sync `symbol-registry_2026-06-07.md`, regenerate
`manuscript/back-matter/symbol-registry.html`, and re-run the invariants gate. **Nothing is applied
by this proposal.**
