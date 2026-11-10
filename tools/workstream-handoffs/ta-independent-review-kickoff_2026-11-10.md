# TA independent review + revision — session kickoff (2026-11-10)

**Status:** PROPOSED (internal scaffolding). **Target:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`.
**Why now:** the TA is the centerpiece of the Darity package (corrected TA + Ch 1 + Ch 5). A prior
session produced 17 candidate findings from a read-through. They are **hypotheses, not facts** — the
new session must verify each one independently against the TA text, then propose a solution with
reasoning. It must also look for problems the prior session missed.

---

## 0. Paste this to start the new session

```
Read CLAUDE.md (CURRENT OPERATING MODE banner), MAP.md, STATE.md, tools/commons_bonds_guiding_constraints_v1_0_0.md, and tools/workstream-handoffs/ta-independent-review-kickoff_2026-11-10.md. Then run the TA independent review it describes. One session, one branch. Phase 1 is a review report only: no edits to the TA. Stop after Phase 1 and hand me a short decision list.
```

---

## 1. Ground rules (from the standing instructions; do not skip)

- **One active session, one branch.** No sub-agents, no parallel sessions, no workflow fleets.
- **Lean pipeline.** Fact-check against `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`; one strongest-critic read, run once; the author's hand redline; mechanical polish last. No acceptance panels, no repeat runs. Every ratified figure change gets a gate pattern in the same commit (so does a retired term; see F1).
- **Math stays `.html`.** Never convert the TA to `.md`. Version on edit: archive v2.0.0, write v2.0.1, and increment the rightmost digit per update.
- **No invented facts, quotes or sources.** Every citation you add must be one you can verify from a retrievable source. If you cannot verify it, flag it "unverified"; do not add it. Anything attributed to Sandy Darity's May 2026 call stays out until he reviews it.
- **Do not trust this document.** Each finding below came from a read-through that skimmed some sections. Open the TA, quote the exact lines, and say CONFIRMED / PARTLY / REFUTED / ALREADY-FIXED before proposing anything.
- **Check for prior work first.** These files may already cover or contradict a finding: `manuscript/technical-appendix/TA-rigor-audit-ledger_2026-06-06.md`, `symbol-registry_2026-06-07.md`, `notation-alignment-proposal_2026-06-09_PROPOSED.md`, `convergence-scope-correction_2026-06-11_PROPOSED.md`, `CSD-computation-method-spec_2026-06-06.md`, `tools/workstream-handoffs/ta-closeout-summary_2026-06-09.md`, and `verified-positioning-findings_2026-06-24.md`. Cite them rather than redoing them.
- **Rigor tests for architectural claims** (apply to F7 and F10 before ratifying anything): the two-path test (allocation symmetry AND shield absence), the merger gate (bilateral independence, with cases in both directions), and the primitiveness gate (a new layer's costs must not decompose into existing ones).
- **Privacy.** No personal financial details in anything written to the repo.
- **Do not touch** `/Noema/` or `/Berggruen Institute - Essay/` on Drive. Never write to Drive.

---

## 2. Method for Phase 1 (per finding)

For each finding F1–F17, write one block in this exact shape:

1. **Verdict:** CONFIRMED / PARTLY / REFUTED / ALREADY-FIXED, with the TA section and verbatim quote(s).
2. **Why it matters:** one or two sentences on the reader or reviewer consequence.
3. **Options:** two or three, with costs.
4. **Recommendation + reasoning:** the one you would ship and why. Include exact replacement text when the fix is short.
5. **Downstream impact:** other TA sections, chapters (Ch 5, Ch 6, Ch 1), glossary, gate patterns.

Then add **N-series findings**: anything you find that is not on this list. Look especially for (a) internal contradictions between sections, (b) symbols or units that change meaning, (c) claims stronger than their support, (d) places where the prose promises something a section does not deliver, (e) numbers that do not reconcile across §3.6, §9.5 and §11.

Then one strongest-critic read of the whole TA, run once: what would the most hostile competent resource economist or reparations economist press on? Report it as extra findings, in the same block shape.

**Deliverable:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-11-10_technical_appendix_independent_review_v1.0.0.md` (status PROPOSED).

**Finish Phase 1 with:** a table (finding / verdict / recommended action / size S-M-L / needs-author-decision Y-N), then a decision list of **no more than 8 items** the author must decide. Keep every ask short; the author has 1–2 hours a week.

**Phase 2 (only after the author ratifies):** apply the ratified fixes to v2.0.1, run `tools/scripts/check-corpus-invariants.sh` (HIGH must stay 0), re-run the calc engines if any number or symbol changes, add gate patterns, update the STATE.md line, and commit and push per CLAUDE.md. Publisher-facing prose merges to main on ratification.

---

## 3. Findings to verify (F1–F17)

### A. Naming and structure of the counting methods

**F1. The "Three Ways of Counting" name no longer matches the structure.**
- §3 says M1 (Replacement Cost) and M3 (Scarcity-Adjusted Option Value) are the two independent RCV estimators. M2 (Revealed Preference) reads the realized Bond B and is only a strict lower bound (RCV ≥ B̂_M2): "not a third independent estimator" (§3.4, §3.6, §9.1).
- The name still appears 17 times in the TA (§3 title and TOC; §4.2; §11.5/§11.6 subheads; §15.1.3). It is also Ch 6's title.
- Candidate renames: "Two Estimators and One Receipt" or "Two Estimators and a Paid Bill". "Bill" can read as the amount owed, which is what RCV is, so "receipt" may fit better. The alternative is to keep "Three Ways of Counting" as an umbrella and fix only the triangulation language (F2).
- Check: how many other files carry the old name (alignment/, Ch 6 drafts, outreach prep, glossary). Many are historical and need no change.
- If renamed: add a deprecated-term pattern to `tools/quality-gates/regressed-patterns.yaml` in the same commit.
- **Author decision.**

**F2. §15.1.3 and §4.2 still say "triangulation" and "three methods."**
- §15.1.3 is titled "Triangulation (Three Ways) versus single-method" and says each of the three methods "has standing as a primary methodology."
- §4.2 says RCV is "triangulated three ways in §3.3–§3.6."
- §15.1.9 and §3.6 already use the two-plus-one language, so the TA is inconsistent with itself.
- Fix regardless of the F1 outcome.

**F3. The convergence rule when Method 3 is Open (backward).**
- §3.6 states the M1 ∩ M3 convergence rule, but §5.5 and §11.12 allow an Open M3 ceiling backward. In that case the CSD claim is floor-only (a lower bound).
- Say this once at §3.6 so the reef row does not read as a gap.
- Confirm that no TA text implies a three-estimator convergence requirement.

### B. Definitions and symbols

**F4. B₁ and CSD are defined in words but not formally.**
- §5.1.1 defines B₁ as "restitution dollars actually posted," with a mechanism list and the discharge condition B₁ = CSD. Definition 1.7 and §0 mention it.
- Open questions:
  - CSD has no numbered Definition (only §2.1 prose and one §0 row).
  - Unit inconsistency: Definition 1.7 types B per unit; §0 lists B, B₁, B₂ in $ and B̂_M2 in $·res⁻¹.
  - No stated measurement rule: which instruments count, how they are summed, and per-unit versus aggregate.
- Check against `symbol-registry_2026-06-07.md` and `notation-alignment-proposal_2026-06-09_PROPOSED.md` before proposing.
- Suggested direction: add formal Definitions for CSD and B₁ (CSD = realized, gate-admitted Cᵢ with the floor + Σ form from §5.5; B₁ = posted restitution instruments, units explicit) and fix the §0 unit rows.

**F5. The Hotelling Identity uses two meanings of "CS."**
- §4.2: RCV − Hotelling rent = CS per unit. The same section admits this coincides with CS = RCV − B (Definition 1.7) only when the posted B equals the Hotelling rent; in general B ≤ rent, so the two quantities are different but share the label.
- Evaluate: rename one (for example "CS_H" for the Hotelling form), restate the identity, or demote it. Also test whether the "not a tautology" argument (the independent-measurement note) holds.

**F6. The cost-variables-as-estimators principle is implicit, not stated.**
- The author's framing: each Cᵢ is an estimator among many; in a given environment most are so small as to be essentially zero under familiar abundance; the CIT is what shows which ones switch on.
- Support already in the TA: Theorem 10.3 (A_ε: the abundance level beyond which c(A) < ε), the §5.5 Zero/Filled/Open states, and §17.
- Gap: it is never stated once for both directions. Also distinguish "ε-zero" (Theorem 10.3) from the §5.5 "Zero" state (genuinely $0 under abundance), which a reader will conflate.
- Suggested placement: the top of §17 or §6.1, with a back-reference from §5.5. Verify Theorem 10.3's wording supports this reading before relying on it.

### C. CIT and the Four Gates

**F7. The seven inversions (§6.2) have an overlap and a gap, and there are two different "seven" lists.**
- §6.2 lists seven inversions: Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political. §6.7 lists seven walkthroughs: McDowell coal, the commute trade, Norwegian oil, the 2008 crisis, the asteroid miner, the pacemaker case, Opioid Appalachia. Label them unambiguously.
- Institutional (4) and Political (7) both strip legal and political infrastructure and both end in "B ≈ 0 in failed or captured states." Apply the merger gate: independence cases in both directions, or merge.
- Autonomy appears in §5.5 and Definition 1.10 as the coercion commons but is not among the seven. Apply the primitiveness gate before adding anything.

**F8. Does Gate 1 (§7.1) match the CAI/CCI sequence (§6.4) and the level-of-claim rule (§6.4.1)?**
- §6.4: CAI ("would the extraction price differently if the commons claim did not exist?") then CCI ("...if the commons were inexhaustible or self-restoring at zero marginal cost?"); only claims passing both are Cost Severance. §6.4.1 requires stating aggregation, temporal and substitutability scope first.
- §7.1 states a single abundance-counterfactual test. The prior read covered only its opening. Read it all and confirm whether the two formulations agree and whether §7.1 requires the level-of-claim specification.

**F9. Gates 2 and 3 are form checks, and Gate 3 is forward-only.**
- Gate 2 (Units) admits any cost once converted to dollars transparently. Gate 3 (Boundedness) is "typically satisfied trivially" backward (§5.5) and overlaps Theorem 10.4 for Weitzman discounting.
- Decide whether to keep all four and say so explicitly (Gates 1 and 4 substantive; Gates 2 and 3 form checks; Gate 3 does nothing backward) or restructure. Check §7's own claim that "the other three are the mathematical hygiene" for consistency.

**F10. No gate tests causal attribution or incidence.**
- CIT tests that a cost is scarcity-grounded, not that this extraction caused it, or that someone other than the beneficiary bears it.
- Decide whether attribution lives in B and the case work (then add an explicit scope statement in §7) or needs a fifth gate. Apply the primitiveness gate and the merger gate to any candidate fifth gate before recommending it.

### D. Literature and contribution

**F11. Prior art missing from the TA text.** A text search of the v2.0.0 HTML found zero hits for each of:
- Costanza & Perrings (1990): closest prior art; anticipatory, escrowed bond sized to worst-case total damage, not a per-event severed figure.
- TEEB / True Cost Accounting: closest by configuration; aggregate evaluation framework.
- NRDA (CERCLA / OPA): strictly ex post.
- Kapp (1950), Martínez-Alier, Mudliar & Koontz (2021), Polanyi / Fraser.
- Hotelling user cost (El Serafy): owner's forgone rent versus third-party severed commons value.
- Loss & Damage Fund; reclamation / financial-assurance bonds (Gerard 2000).
- Also zero hits: Pistor, Christophers, Gardiner, Broome (Broome is ranked MUST-NOW for Ch 6 in `matrix-findings-chapter-TA-update-handoff_2026-06-19.md`).

For each:
- Re-verify the claim from a primary source. `verified-positioning-findings_2026-06-24.md` is the input, but it is a negative-existence finding bounded by its search, and three residual threads were closed by the parent session without a fresh three-vote check.
- Decide whether it belongs in the TA or in the chapters; the 06-19 findings mark some items BOOK-2/3 and deferrable.
- Draft a cite-and-distinguish entry.

**F12. §14.5 (Ostrom) sits on a superseded axis.**
- Current text argues renewable versus non-renewable ("necessary but insufficient").
- The verified formulation: Ostrom's principles govern bounded, repeatedly-interacting, heterogeneous appropriators who substantially share the resource's fate; the framework's domain is where that shared-fate structure breaks. Never "coequal"; use Mudliar & Koontz (2021) and Harvey for the power critique, framed as "under-theorize," not "power-blind."
- Read the whole of §14.5 (the prior read saw only the first part) and the §0 contribution mirror, then rewrite per the findings.

**F13. There is no single statement of what the TA adds and what it borrows.**
- Contribution claims are scattered across §4.2, §8.3, §15.1.9 and §17. §15.1.9 concedes none of the eight design choices is novel; the claim is the configuration.
- Draft one short table near the top (Component / Source / What is borrowed / What is added / Where in the TA) and keep it consistent with the verified positioning. No overclaiming.

**F14. The anticipatory reserve may not be illustrated.**
- The verified novelty is a per-extraction-event price with a reserve posted in advance against that figure. The calibration cases price RCV and CS and read the realized bond.
- Read §11 in full: does any case size and post a reserve ahead of extraction? If not, say so, and propose whether to add a short worked example or to scope the claim.

**F15. The §5.4 B₂-only / B₁-companion flag is still open.**
- Since 2026-05-13 (`tools/rigor-passes/ta_section_5_5_bidirectionality_proposal_2026-05-13.md`), an in-section note logs Option (i) (no action). Options (ii) (expand §5.4) and (iii) (new §5.6) were never ratified.
- With B₁ now to be formally defined (F4), re-evaluate whether the moral grounding for B₁ needs its own text.

### E. Other checks

**F16. Method 3's functional form: is its provenance stated?**
- RCV_M3 = V_market × [1 + ln(1+ς) × Hotelling_anchor] × 1/(1−α), with the Hotelling anchor ≈ 5%/yr.
- Unverified suspicion: the log scarcity form and the anchor may be the framework's own calibrated parameterization, not derived from Arrow–Fisher or Henry. Read §3.5 and `method3_sensitivity_analysis_2026-04-25.md`. If it is a calibrated construct, the TA should say so plainly.

**F17. Existing open items from STATE.md (the TA line).**
- Apply the 06-24 positioning findings (F11, F12, F13 cover this); the three reef §11.12 calls; the §6.3 and §6.2 loose ends; a render check; a changelog against Sandy's 05-15 copy; a list of his call-material for his approval.
- Confirm each is still open and fold the live ones into the decision list.

---

## 4. Prior session's summary of the TA (for orientation only; verify)

- 18 sections. §1 definitions (1.1–1.10; central equation CS = RCV − B). §2 two-instrument architecture (CSD ↔ B₁ backward; RCV ↔ B₂ forward). §3 RCV integral, IPG, three methods. §4 Hotelling Identity. §5 B = B₁ + B₂, Parfit/Sen grounding, bidirectionality (§5.5). §6 CIT (CAI/CCI, seven inversions, four-gate walkthroughs). §7 Four Gates. §8 Asymmetric Regret Rule. §9 cross-check architecture. §10 theorems (10.1a, 10.3, 10.4; Empirical Observations 10.1b, 10.2, 10.5). §11 validation cases (McDowell, Deepwater Horizon, Libby, Baotou; Norway, Appalachia, CSD–RCV test, sensitivity, DAC, space anchors, IPG reconciliation, Chesapeake reef). §12 boundary scope. §13 substitutability. §14 literature. §15 limitations and design defense. §16 extensions. §17 sum-of-costs generalization. §18 bibliography.
- Calc engines re-ran clean 2026-10-25 (21/21, 24/24). Invariants HIGH = 0 at that time. Re-check both after any edit.

---

## 5. End-of-session close (required)

End with exactly three lines: **what got done · what is waiting on the author · the exact paste line for the next session.**
