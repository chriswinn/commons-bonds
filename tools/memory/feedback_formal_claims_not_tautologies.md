---
name: feedback-formal-claims-not-tautologies
description: "B<RCV and the Hotelling Identity are NOT tautologies; never call them \"theorems\" in chapters/essays — B<RCV is Empirical Observation 10.1b, only the sign-identity is Theorem 10.1a."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5cea42db-f293-463e-9c57-18d23f3c61d6
---

The framework's two load-bearing formal claims survive the "tautology dressed as a
result" charge **only because the TA labels them carefully** — and that labeling
discipline must be preserved in all downstream prose.

- **B < RCV (Cost Severance > 0).** RCV (the foreclosure+externality integral,
  Def 1.6, triangulated 3 ways, computed in §11), Hotelling rent (price − marginal
  extraction cost), and **B (the *observed* posted accountability bond — severance
  taxes, reclamation bonds, etc., Def 1.7)** are all **independently measured**.
  CS ≡ RCV − B is the one defined residual. So B < RCV is **NOT true by construction**
  — B is not a fraction of RCV. The TA proves only the trivial sign-identity
  (`CS>0 ⇔ B<RCV`) as **Theorem 10.1a**, and labels the substantive real-world claim
  **Empirical Observation 10.1b** (explicitly NOT a theorem; has falsifiability +
  domain). There is no "Theorem 10.1b" and no "Theorem P1/P2" in the TA — the
  Coase/Pigou items are **Premises (i)/(ii)** of Emp. Obs. 10.1b.

- **Hotelling Identity (`RCV − Hotelling rent = CS per unit`).** "CS" = **Cost
  Severance, NOT consumer surplus** (consumer surplus appears nowhere as an identity
  in the corpus). It is the difference of two independently-measured quantities, so it
  has empirical content; it's a *bridge*, not an accounting tautology. The robustness
  claim ("CS > 0 across the Nordhaus-to-Stern range") is genuine — RCV is recomputed
  at each discount rate ($526 Stern → $541 Nordhaus).

**Why:** The 2026-06-17 matrix-independent verification flagged this as the deepest
methodologist exposure. Verification (`tools/audits/ta-tautology-verification_2026-06-17.md`)
confirmed the TA already handles it; the "B<RCV is a theorem" over-claim lived ONLY in
the contribution matrix + a few ledgers (zero chapters/essays). Corrected 2026-06-17.
The TA §4.2 now carries an explicit "why this is not a definitional tautology" note.

**How to apply:** Never let a chapter, essay, op-ed, or cover letter call B<RCV or the
Hotelling Identity a "theorem" or "near-theorem." Say "empirical observation" / "the
framework's bridge." "Conservative by construction" (the estimate is biased *down*) is
fine; never slide it into "CS>0 by construction" (the tautology charge). When drafting
from the contribution matrix, trust the canonical TA labels over any stale ledger cell.
A pre-commit guard (`regressed-patterns.yaml`: `regressed-canon-*-theorem*`, HIGH) now
blocks affirmative "theorem" over-claims in staged chapter-Draft/op-ed prose — but
`publishing/essays/<venue>/essay.md` is **not yet in gate scope**, so essays still rely on
this discipline. (2026-06-18: also fixed a parser bug that had silently disabled 6 ratified
convergence-sunset guards; `scope:` must stay at end-of-file in that YAML.)
Related: [[feedback_quantitative_apparatus_peer_review_defense]],
[[feedback_no_invented_factual_claims_in_publisher_facing_prose]].
