# Technical Appendix — independent review, Phase 1 (2026-11-10)

**Status:** PROPOSED (internal scaffolding). Review report only. **No edits were made to the TA.**
**Target:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (8,367 lines, read in full, §0–§18).
**Kickoff:** `tools/workstream-handoffs/ta-independent-review-kickoff_2026-11-10.md`.
**Baseline at review time:** invariants gate HIGH = 0; calc engines 21/21 and 24/24, 0 mismatches.
**Method:** each kickoff finding checked against the TA text with verbatim quotes; prior audits read first
and cited; one strongest-critic read, run once. No sub-agents.

## Read this first (two minutes)

1. Of the 17 kickoff findings: **13 confirmed, 3 partly (F3, F15, F16), and F17 is a mixed list** (one item already fixed, two partly, four open). None refuted.
2. The review found **12 further internal problems** (N1–N12) and **6 strongest-critic exposures** (C1–C6).
3. The four that matter most before Sandy Darity reads it:
   - **"Method 1" means two different things** (replacement cost in §3, damage audit in §9), and McDowell
     carries three different RCV levels ($504–518, $525–540, $1,000–1,500). The headline CS uses the highest. (N1, N2)
   - **The headline multiples divide 2020-dollar costs by a 1960 nominal price.** The TA itself calls that
     an inflation artifact in §11.6 and §11.11, then prints it in §9.5, §14.7 and §16.4. On a consistent basis
     the integral lens is about 4–13×, not 61–115×. (N3)
   - **The central equation has no term for who bears the cost.** CS = RCV − B gives a positive answer for
     the Mars colony that mines its own ore, which §12 says should be zero. (F10)
   - **Three passages about reparations economics would read badly to a reparations economist**, including
     one sentence that calls Darity and Mullen's method "the framework's." (C6)
4. Calc engines pass because several disputed inputs are typed in as constants, not derived. A clean engine
   run is not evidence the numbers reconcile.
5. The summary table and the **8 decisions** are at the end.

**Verdict vocabulary:** CONFIRMED / PARTLY / REFUTED / ALREADY-FIXED, as the kickoff specifies.
Section numbers refer to the TA. Quotes are verbatim from v2.0.0.

---

## Part 1. Kickoff findings F1–F17

### A. Naming and structure of the counting methods

#### F1. The "Three Ways of Counting" name

1. **Verdict: CONFIRMED.** The exact phrase appears 11 times in the TA and the short form "Three Ways" 7 more
   (18 total; the kickoff said 17). §3 title: "RCV Quantification — Three Ways of Counting." §3.6 then says
   M1 and M3 "are the two independent RCV estimators" and M2 is "not a third RCV estimator." Outside the TA
   the phrase is in 3 chapter files (it is Ch 6's title), 46 files under `publishing/`, 38 under `alignment/`,
   and the generated back matter.
2. **Why it matters:** a reader who sees "three ways" expects three estimates of one quantity and then finds two.
   It is the first thing a methodologist will ask about.
3. **Options:**
   - (a) Rename ("Two Estimators and One Receipt"). Cost: Ch 6 title, glossary, back matter, proposal, 46
     publishing files; a new term to teach.
   - (b) Keep the name and gloss it once: three ways of counting the identity, two that estimate what is owed
     and one that reads what was paid. Cost: one sentence in §3 and the F2 fixes.
   - (c) Keep the name, no gloss. Cost: the inconsistency stays.
4. **Recommendation: (b).** The name is accurate under that gloss: §3.6 already says the three "jointly count
   the framework's central identity." It is the more portable phrase, and "when in doubt, trim" argues against
   a new coinage. Revisit a rename only at the Ch 6 rebuild. Proposed sentence for the top of §3:
   *"Three ways of counting, not three estimates of one number: Methods 1 and 3 estimate what is owed (RCV);
   Method 2 reads what has been paid (B). The gap between them is the result."*
5. **Downstream:** none if (b). If (a): Ch 6 title, glossary, `terms_index.md`, proposal §05, plus a
   deprecated-term gate pattern in the same commit.

#### F2. "Triangulation" and "three methods" language

1. **Verdict: CONFIRMED, and wider than listed.**
   - §4.2: RCV is "triangulated three ways in §3.3–§3.6."
   - §15.1.3 title: "Triangulation (Three Ways) versus single-method"; text: "Each of the three methods has
     standing as a primary methodology in its tradition." The same paragraph lists Hartwick 1977 and Solow 1974
     as the "Revealed Preference" lineage, which they are not.
   - §11 intro (not in the kickoff): "validates the three-model convergence."
   - §3 TOC line: "triangulation logic." §3.6 heading: "Triangulation logic."
2. **Why it matters:** §3.6 and §9.1 say the opposite. §9.1: "The framework does not require the lenses to
   agree, and does not treat agreement as the result."
3. **Options:** (a) fix the four sites; (b) fix them and retitle §3.6 "How the three readings combine";
   (c) leave.
4. **Recommendation: (b).** Replacement text:
   - §4.2: "estimated two ways (Methods 1 and 3) in §3.3–§3.6".
   - §15.1.3 title: "Two estimators and a realized-bond reading versus a single method."
   - §15.1.3 sentence: "Each of the two estimators has standing as a primary methodology in its tradition
     (Replacement Cost; quasi-option value). Method 2 is a reading of the realized bond, not an estimate."
     Drop Hartwick and Solow from the Method 2 lineage.
   - §11 intro: see N8.
5. **Downstream:** proposal §05 chapter summaries; Ch 6 rebuild brief already carries the two-estimator frame.

#### F3. The convergence rule when Method 3 is Open

1. **Verdict: PARTLY.** The reef row is already handled. §3.6: "Method 3 is the admitted-but-Open ceiling
   variable (so no M1 ∩ M3 convergence range is claimed)." What is missing is the general rule, and one
   sentence contradicts the TA's own cases. §3.6: "No single-method CS claim has standing." Yet §9.5 reports
   Deepwater ("CSD − B₁ ≈ $8–12B"), Libby and Baotou ("that floor alone … independently implies CS > 0") on
   the damage lens alone, and the reef on Method 1 alone.
2. **Why it matters:** by the TA's own reporting rule, four of its six computed cases have no standing.
3. **Options:** (a) add the floor rule; (b) drop the "no standing" sentence; (c) compute M3 for every case
   (not possible on documented inputs, per §9.5).
4. **Recommendation: (a).** Replace the sentence with: *"A convergence range is claimed only where both
   estimators compute. Where only one computes (Method 3 Open, or not applicable), the result is reported as
   a floor, a lower bound on RCV or CSD, and labeled as one."*
5. **Downstream:** §5.5 (already consistent), §9.5 table note, §10.2.

### B. Definitions and symbols

#### F4. B₁ and CSD have no formal definition; units disagree

1. **Verdict: CONFIRMED.**
   - CSD has no numbered Definition (Definitions run 1.1–1.10). It is defined in prose in §2.1, §5 and §5.5.
   - Units: Definition 1.7 says "B is the per-unit dollar value." §0 lists "B, B₁, B₂ … $" and "CS, CSD … $."
     The reef B₁ (~$115M) and Deepwater B₁ ($61.6B) are aggregates; McDowell and Norway are per unit.
   - No measurement rule. And Definition 1.7 conflicts with use: B is "mechanisms actually in operation that
     force extractors to bear costs," but §5.1.1 puts "welfare-state instruments (universal healthcare …)" in
     B₁, and the reef B₁ is "100% public, $0 industry."
   - Prior work checked: `symbol-registry_2026-06-07.md` and `notation-alignment-proposal_2026-06-09` cover
     collisions (E vs E[·], B vs "billion") but not this.
2. **Why it matters:** the equation's two backward terms cannot be recomputed by a third party, and "B" means
   "what the extractor pays" in the definition and "what anyone pays" in the cases.
3. **Options:** (a) add two Definitions and fix §0; (b) fix §0 units only; (c) leave to prose.
4. **Recommendation: (a)**, with a payer split. Draft:
   - *Definition 1.11 (Cost Severance Damages). CSD is the realized, gate-admitted cost of extraction that has
     already occurred, for a named extraction history, place and period, valued at analysis time:
     CSD = CSD_floor + Σ (admitted Cᵢ in the Filled state), where CSD_floor is the Method-1 cost to cure.
     Any admitted Cᵢ left Open makes the reported CSD a lower bound. Units: dollars in aggregate; $·res⁻¹ when
     divided by cumulative quantity extracted.*
   - *Definition 1.12 (Restitution Bond, as measured). B₁ is the sum of payments actually made toward repair
     of the damages counted in CSD, over the same history, place and period, reported with the payer split
     B₁ = B₁(extractor) + B₁(public). Both reduce unrepaired harm; only B₁(extractor) discharges the
     extractor's obligation.*
   - §0: B, B₁, B₂, CS, CSD: "$·res⁻¹ per unit; $ in aggregate (stated per case)."
5. **Downstream:** Definition 1.7 wording (see F10); §11.12 (the reef compares James River damage with
   bay-wide spending, see F17); Ch 3 and Ch 5 only if they quote the definitions; glossary entries.

#### F5. The Hotelling Identity uses "CS" for two quantities

1. **Verdict: CONFIRMED.** §4.2: "Hotelling Identity: RCV per unit − Hotelling rent per unit = CS per unit,"
   then: "RCV − Hotelling rent and RCV − B are distinct quantities that share the CS label only in that
   idealized case." Prior work: `tools/audits/ta-tautology-verification_2026-06-17.md` reached the same view
   ("a reused 'CS' symbol that invites the tautology charge") and left the fix author-gated.
   Two further problems:
   - The "not a tautology" note shows both inputs can be measured separately. That does not give the equation
     content; the only empirical claim is the sign (RCV > rent). The equation defines a new quantity.
   - The worked example is backwards: "That difference is the commons-loss Norway is NOT incurring." The
     difference between the fund and full RCV is what Norway has *not* covered. §11.5 puts it at $13–15 trillion.
2. **Why it matters:** a resource economist will read it as subtracting the owner's income from a social cost
   and calling the remainder unpaid. Rent is what the owner receives; it is a bond only if it is collected and
   held for the cost-bearers.
3. **Options:** (a) rename one symbol (CS_H); (b) restate as a true identity; (c) demote §4 to a paragraph in §14.1.
4. **Recommendation: (b).** There is a correct identity available and it says something useful:
   **CS = (RCV − H) + (H − B)**, where H is the Hotelling rent per unit. The first term is the gap that would
   remain even if every dollar of scarcity rent were bonded; the second is rent that was not bonded. Norway is
   the case where the second term is small and the first is not. The name "Hotelling Identity" can stay,
   because this one is an identity. Rewrite the Norway example to match.
5. **Downstream:** §4.3 citation form, §15.1.4, §15.1.9, §14.1; glossary entry; any essay that quotes the
   identity (grep before Phase 2). Pairs naturally with the El Serafy user-cost distinction (F11).

#### F6. Cost variables as estimators, most of them near zero

1. **Verdict: CONFIRMED.** The pieces exist but are never joined. Theorem 10.3 (I): "for any ε > 0 there exists
   A_ε such that c(A) < ε for A > A_ε." §5.5: "Zero: under abundance the cost genuinely is $0 (the CIT toggle;
   Theorem 10.3)." Those two differ: the theorem gives "below any tolerance," not zero. And the theorem's domain
   excludes "Renewable commons," "Information / non-rivalrous commons" and "Network-effect commons," so it
   cannot be the warrant for a Zero state on the Autonomy or Epistemic commons.
2. **Why it matters:** a reader will ask whether "Zero" is a measurement or an approximation.
3. **Options:** (a) one statement at the top of §17, back-referenced from §5.5; (b) at §6.1; (c) leave implicit.
4. **Recommendation: (a).** Draft: *"Every admitted Cᵢ is an estimate of one cost among many. In a given
   setting most are negligible: for depletable commons Theorem 10.3 shows the cost falls below any tolerance ε
   once abundance exceeds A_ε, and the framework records such a term as Zero. Zero therefore means 'below
   tolerance at this abundance,' not 'absent.' The inversion test is what shows which terms leave that state as
   abundance falls. For commons outside the theorem's domain the Zero state is an assumption stated per case."*
   Change §5.5's "genuinely is $0" to "is below tolerance (recorded as $0)."
5. **Downstream:** §5.5 three-states paragraph; §17.7; calc engine labels use "ZERO" (no numeric change).

### C. CIT and the Four Gates

#### F7. Seven inversions: overlap, gap, and two "seven" lists

1. **Verdict: CONFIRMED on all three, with a correction.**
   - Two lists: §6.2 "Seven Worked Inversions" (commons) and §6.7 "Seven Walkthroughs" (cases). The TOC mixes
     them: "seven worked inversions (McDowell coal, the commute trade, Norwegian oil, …)."
   - Overlap: Inversion 4 ends "cost severance operates at maximum scale because B ≈ 0"; Inversion 7 ends
     "accountability bonds collapse toward zero and cost severance operates at maximum scale." Definition 1.10
     gives both the lineage Stigler 1971 and Acemoglu & Robinson 2012, and "regulatory capture" appears in both.
   - Count: Definition 1.8 lists **ten** categories; §6.2 walks seven; §15.1.6 says "ten."
   - Correction to the kickoff: §6.3 maps Institutional, Political and Epistemic to "B term," not to a cost
     term. They are conditions that suppress the bond, not costs in the integrand.
2. **Rigor tests.**
   - *Merger gate (Institutional vs Political).* As written, independence is not shown: shared lineage, shared
     mechanism, shared ending. With sharper definitions it can be: Institutional = capacity to enforce rules
     that exist; Political = whose interests the rules are written for. Candidate cases from the TA's own
     material: capacity failure without political capture (liabilities shed through bankruptcy, "~$865M to
     taxpayers," in a contested democracy); political failure with capacity (a capable state whose affected
     villagers have no say, the Baotou pattern). Both are candidates for the author to accept or reject, not
     established facts.
   - *Primitiveness gate (adding Autonomy).* Fails for now. §5.5 leaves the coercion cost "an Open slot in this
     volume" and says pricing it is "methodologically unresolved." A walkthrough with no priced cost cannot
     show that its costs do not decompose into existing categories.
   - *Two-path test.* §6.3's own mapping fits it: commons that route to U or E carry the allocation asymmetry
     (Path 1); commons that route to B are shields (Path 2).
3. **Why it matters:** two of the seven tell the same story, and a careful reader will count ten, seven and seven.
4. **Options:** (a) keep seven, sharpen 4 and 7, relabel the lists, add no Autonomy walkthrough; (b) merge 4
   and 7 into one "governance" inversion (six); (c) regroup all ten as cost-bearing versus bond-suppressing.
5. **Recommendation: (a), plus one sentence from (c).** Rename §6.7 "Seven case walkthroughs" and fix the TOC.
   Move "regulatory capture" to Political only. Add to the §6.2 note: *"Inversions 4 and 7 differ from the
   rest: they reveal what suppresses the bond B, not a cost in the integrand (§6.3)."* Layer changes are
   organizational, so this does not touch framework integrity.
6. **Downstream:** Definition 1.8 and 1.10 profiles; §6.3 table; Ch 6 and Ch 8 rebuild briefs; glossary.

#### F8. Gate 1 versus the CAI/CCI sequence and the level-of-claim rule

1. **Verdict: CONFIRMED.** §7.1 was read in full. Its formal statement is a single abundance test: the cost
   "reduces to zero" when "the scarcity-condition underlying Cᵢ is removed." It never mentions CAI, CCI or
   level of claim, although §7's own header says "CIT — Commons Inversion Test (CAI + CCI sub-forms)" and §6.5
   says "sub-forms per §6.4; level-of-claim per §6.4.1." Worse, §15.1.8 names the single-form test as the
   *rejected alternative*: "the single-form's 'abundance of the relevant condition' was silently conflating
   two different counterfactuals." So §7.1 formally states what §15.1.8 says was rejected.
   The test is also stated three ways: strip abundance and costs appear (Definition 1.8); would the price
   differ if the claim did not exist / the commons were inexhaustible (§6.4); imagine the commons absent
   and the cost becomes visible (§6.7).
2. **Why it matters:** the framework's central test has no single statement a reviewer can apply.
3. **Options:** (a) restate Gate 1 as a three-step test; (b) drop CAI/CCI and keep the single form; (c) cross-reference only.
4. **Recommendation: (a).** §7.1's abundance test is CCI; keep it and put the other two steps in front.
   Draft: *"Gate 1. State the level of claim (§6.4.1). Then: (i) grounding (CAI): the cost is attached to a
   named shared stock, not to a privately owned asset; (ii) inversion (CCI): under a counterfactual in which
   that stock is inexhaustible or self-restoring at zero marginal cost, the cost falls to zero. A claim that
   passes (i) but fails (ii) is a coordination problem and is routed to §6.6."*
5. **Downstream:** §7.5 Step 1; §7.6 and §17.6 gate checks; the §6.7 "sub-form" table (Absence/Consumption
   there describes how the commons was damaged, which is a different thing from the two test steps and should be
   relabeled); Ch 6 brief.

#### F9. Gates 2 and 3 are form checks; Gate 3 does nothing backward

1. **Verdict: CONFIRMED, and Gate 3 has an error.** The TA already says most of this: "Units Consistency is
   mostly boilerplate"; "the other three are the mathematical hygiene"; Gate 3 backward is "typically satisfied
   trivially." But:
   - §7: "The gates are not hierarchical" sits beside "CIT is the framework's intellectual contribution; the
     other three are the mathematical hygiene." Both cannot be the summary.
   - Gate 3 is nearly empty forward as well. Theorem 10.4 (SC1) proves convergence for any polynomially
     bounded term whenever r_∞ > 0, and §16.1 sets r_min at about 1% (§11.1 uses 2%). See N6: the "rejected
     candidate" in §7.3 would in fact pass.
   - Gate 2 is stated three ways: "[dollars · (resource-unit)⁻¹ · (time-unit)⁻¹]" (§7.2), "dollars ×
     time-domain" (throughout §6.7), "$" (§0).
2. **Why it matters:** four gates presented as equals invite the question of what two of them exclude.
3. **Options:** (a) keep four, state the roles plainly; (b) fold Gates 2 and 3 into a "well-formedness"
   condition and present two gates plus that; (c) leave.
4. **Recommendation: (a).** "Four Gates" is settled vocabulary. Add to §7: *"The gates do different work.
   Gates 1 and 4 are substantive: one decides whether a cost belongs, the other prevents counting it twice.
   Gates 2 and 3 are well-formedness checks. Gate 3 binds only where the long-run discount rate is taken to
   zero; under the declining-rate schedule of §16.1 any bounded cost passes, and backward costs pass by construction."*
5. **Downstream:** §6.5, §6.7 overview, §15.1.5; the Gate 3 example (N6).

#### F10. No gate tests attribution or incidence

1. **Verdict: CONFIRMED. This is the largest structural finding.** Three separate gaps:
   - *Incidence.* CS = RCV − B has no term for who bears the cost. §12 Scenario 5: "The extractor and the
     cost-bearer are the same people … CS → 0. No cost severance possible." By the formula that colony has
     RCV > 0 and B = 0, so CS > 0. §12 Scenario 1: "Cost severance requires distance." The equation does not
     contain distance or allocation. §17.2 puts "who captures value, who bears cost" into "Context," which has
     no formal role.
   - *Attribution.* Nothing tests that this extraction caused the cost. The McDowell RCV is 92% combustion
     carbon ("the carbon pulse carries ≈92% of the level"), assigned to the ton at the mine mouth. The reef
     assigns the whole 1910–1981 acreage loss to extraction.
   - *Self-severance.* §6.6 defines the domain as costs "borne by stakeholders who do not capture extraction
     value." Walkthrough 2 (the commute) admits a case where "value-capturer = cost-bearer."
2. **Rigor tests on a candidate fifth gate ("borne by someone other than the beneficiary").**
   - *Primitiveness:* passes. It does not reduce to scarcity-grounding, units, boundedness or non-overlap.
   - *Merger:* independent of Gate 1 both ways (the Mars colony passes Gate 1 and fails incidence; a pure
     transfer passes incidence and fails Gate 1).
   - *But it is the wrong home.* The gates admit costs into RCV. Incidence does not change what the commons is
     worth; it changes how much of that is already borne by the party who gains. That is the B side.
   - *Two-path test:* the allocation asymmetry (Path 1) is the mechanism and must be in the definition; the
     shield (Path 2) explains why B stays low. Neither is in the equation today.
3. **Why it matters:** a reviewer can produce a counterexample to the central equation from the TA's own §12.
4. **Options:** (a) a fifth gate; (b) amend Definition 1.7 so B includes cost the beneficiary bears itself, and
   add a scope statement to §7 on attribution; (c) scope statement only.
5. **Recommendation: (b). No fifth gate.** Draft for Definition 1.7: *"B counts every dollar of the cost that
   the party capturing the value bears: through instruments that force payment, and directly, where the
   beneficiary and the cost-bearer are the same. Cost severance is what remains: cost that falls on someone
   else."* Draft for §7: *"The gates test whether a cost is commons-grounded and well-formed. They do not test
   causation. Attribution of a cost to a given extraction is case work and is stated with each case: the
   causal claim, its source, and the share assigned."* Then decide the commute: either it is a teaching case
   outside the formal domain, or "past self / future self" is declared a form of distance. I recommend the first.
6. **Downstream:** §12 Scenarios 1 and 5 then follow from the definition; §6.6; Walkthrough 2; §16.3; F4's
   payer split; Ch 1 (the commute appears there) and Ch 7.

### D. Literature and contribution

#### F11. Prior art missing from the TA

1. **Verdict: CONFIRMED.** Zero hits in the v2.0.0 HTML for: Perrings, TEEB, NRDA, "Natural Resource Damage,"
   Martínez-Alier, Mudliar, Polanyi, Fraser, El Serafy, "user cost," "Loss and Damage," Gerard, Pistor,
   Christophers, Gardiner, Broome. ("Kapp" matches only inside other words. "True cost" appears four times as
   ordinary prose, never as True Cost Accounting.) Two more that a resource economist will expect and that no
   prior document lists: **Epstein et al. 2011** and **Muller, Mendelsohn & Nordhaus 2011** (see C1).
2. **Verification done this session (bibliographic existence and abstract-level claim only):**

   | Source | Checked | What the check supports |
   |---|---|---|
   | Costanza & Perrings 1990, *Ecological Economics* 2(1): 57–75 | Verified | Abstract: a bond "equal to the current best estimate of the largest potential future environmental damages," held in escrow. Supports "anticipatory, sized to worst case." |
   | Gerard 2000, *Resources Policy* 26(4): 189–197 | Verified (abstract only) | Reclamation bonds as an enforcement device. |
   | Mudliar & Koontz 2021, *Society & Natural Resources* 34(5): 639–658 | Verified (abstract) | The principles "can conceal and perpetuate power asymmetries … even while improving environmental outcomes." |
   | El Serafy 1989, in Ahmad, El Serafy & Lutz (eds.), World Bank | Verified (secondary) | User cost splits receipts into a capital element and true income: the owner's side. |
   | Epstein et al. 2011, *Annals NYAS* 1219: 73–98 | Verified | Life-cycle external cost of US coal, roughly a third to over half a trillion dollars a year. |
   | Muller, Mendelsohn & Nordhaus 2011, *AER* 101(5): 1649–75 | Verified (abstract) | Coal-fired generation's air-pollution damages are 0.8–5.6 times its value added. |
   | Broome 1992, *Counting the Cost of Global Warming* | Verified | Exists; White Horse Press. |
   | Broome 2012 *Climate Matters*; Broome 1994 "Discounting the Future" | **Unverified this session** | Search returned nothing usable. Check before adding. |
   | Kapp 1950; Martínez-Alier; Polanyi; Fraser; TEEB; NRDA (CERCLA/OPA); Loss and Damage Fund; Pistor; Christophers; Gardiner | **Not re-verified this session** | Rely on `verified-positioning-findings_2026-06-24.md`, which itself notes three threads were closed without a fresh check. |

3. **Why it matters:** the two nearest neighbours to the framework's instrument (Costanza & Perrings) and to
   its flagship number (Epstein; Muller et al.) are absent. A specialist will supply them.
4. **Options:** (a) one new subsection, "§14.8 Closest prior art," five short cite-and-distinguish entries;
   (b) spread entries through §14.1–§14.7; (c) chapters only.
5. **Recommendation: (a), TA-now set of six.** Costanza & Perrings (the figure differs, not the timing);
   NRDA (after the fact); TEEB / True Cost Accounting (aggregate evaluation, no per-event reserve); El Serafy
   user cost (owner's forgone rent versus third-party loss; goes with F5); Epstein and Muller et al. (credit
   them for the coal damage total, see C1); Mudliar & Koontz (goes with F12). Broome goes in §14.3–§14.4 once
   the two unverified titles are checked. Leave Kapp, Martínez-Alier, Polanyi/Fraser, Pistor, Christophers,
   Gardiner and the Loss and Damage Fund to Ch 5 and Ch 6, where the 06-19 handoff already assigns them.
   Entry drafts are a Phase 2 task; each must be written from the source, not from the summary above.
6. **Downstream:** §18 bibliography and `tools/back-matter/sources/bibliography.md`; proposal §02 comps.

#### F12. §14.5 (Ostrom) is on a superseded axis

1. **Verdict: CONFIRMED, and wider than §14.5.** §14.5, read in full: "Ostrom's framework was designed for
   renewable commons … They give us nothing for the permanent farewell to a barrel of oil … necessary but
   insufficient." The TA positions Ostrom three incompatible ways:
   - §14.5: renewable versus non-renewable.
   - §6.6: extraction commons versus coordination commons.
   - Definition 1.10 ("Heterogeneous-stakeholder commons scope"): "Ostrom's eight design principles (Ostrom
     1990) presume substantially-aligned stakeholders … structurally divided stakeholders fall outside that
     scope." This is the claim the 06-24 verification rejected ("Do NOT claim 'heterogeneity breaks Ostrom's
     cooperation'"). It also traces to Darity's May call (item MI-3 in
     `research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md`), so it is call material.
   - §11.12 prices a renewable commons, which §14.5 says is Ostrom's territory.
   - There is no contribution mirror inside the TA: its §0 is the notation table. The "§00 mirror" named in the
     positioning file is most likely the book proposal's §00 overview, which is outside this review.
2. **Why it matters:** the verified formulation is in none of the three places, and one of them carries a rejected claim.
3. **Options:** (a) rewrite §14.5 only; (b) rewrite §14.5 and bring Definition 1.10 and §6.6 onto the same
   axis; (c) also remove the call-derived paragraph until Darity has seen it.
4. **Recommendation: (b) and (c).** One axis everywhere: Ostrom's principles govern bounded, repeatedly
   interacting, heterogeneous appropriators who substantially share the resource's fate; the framework's
   domain is where that shared-fate structure breaks. Cite Ostrom 1990, Mudliar & Koontz 2021 and Harvey, framed
   as "under-theorize," never "power-blind," never "coequal." §6.6's CCI filter stays as the operational test.
5. **Downstream:** §15.1.6, §15.1.8; Ch 6 L323 is already on the corrected axis; essay sessions inherit.

#### F13. No single statement of what is borrowed and what is added

1. **Verdict: CONFIRMED.** Contribution claims sit in §4.2, §8 and §8.3, §15.1.9 and §17. §15.1.9: "None of
   these eight choices is novel as choice-architecture … The framework's contribution is the specific
   configuration." That paragraph names "option-value economics (Dixit & Pindyck 1994)," which §3.5 says "the
   framework does not use."
2. **Why it matters:** Darity asked to see the mathematics. A reviewer should learn in one table what to credit elsewhere.
3. **Options:** (a) a table before §1; (b) a table at §15.1.9; (c) prose only.
4. **Recommendation: (a), mirrored by a pointer at §15.1.9.** Draft rows (Component / Source / Borrowed / Added / Where):

   | Component | Source | Borrowed | Added | Where |
   |---|---|---|---|---|
   | Externality | Pigou 1920 | Unpriced third-party cost | Tracked per unit of extraction, against what was actually paid | §1.7 |
   | Scarcity rent | Hotelling 1931; El Serafy 1989 | Rent rule; owner's user cost | The split CS = (RCV − H) + (H − B) | §4 |
   | Reinvesting rent | Hartwick 1977; Solow 1974 | Invest the rent | Treats the fund as a bond and measures what it leaves uncovered | §5, §11.5 |
   | Discounting | Weitzman 2001 | Declining rate | None | §1.5, §16.1 |
   | Irreversibility | Arrow & Fisher 1974; Henry 1974 | The concept | A simple multiplier of the framework's own design (F16) | §3.5 |
   | Damage totals | EPA 2023; Epstein et al. 2011; Muller et al. 2011 | Social cost of carbon; life-cycle damages | None on the damage total itself | §11.1 |
   | Bonding | Costanza & Perrings 1990; reclamation bonds | Bond posted in advance | Sized to the per-unit severed figure, not worst-case total | §5, §14.8 |
   | Restitution | Darity & Mullen 2020 | The method for pricing realized harm; restitution as redress | None on method; a slot for it beside the forward term | §5.1.1, §5.5 |
   | Commons governance | Ostrom 1990 | Shared-fate governance | A price where shared fate breaks | §6.6, §14.5 |
   | Decision rule | Savage 1951; Loomes & Sugden 1982 | Minimax regret | Applied to irreversible extraction | §8 |
   | Inversion test and gates | (framework) | Counterfactual reasoning | The admission test | §6, §7 |

   The "Added" column must not exceed the verified positioning: the claim is the per-event price with a reserve
   posted against it, and the configuration.
5. **Downstream:** proposal §00 and §02; cover note to Darity.

#### F14. The anticipatory reserve is not illustrated

1. **Verdict: CONFIRMED.** §11 was read in full. No case sizes or posts a reserve ahead of extraction. Every
   case prices RCV or CSD after the fact and reads the bond that was paid. The only forward mention is a
   counterfactual inside §7.6: "under a national community-transition-reserve fund fully bonded to extraction
   at the time of permitting." The word "anticipatory" does not occur in the TA.
2. **Why it matters:** the verified novelty, and the whole distinction from Costanza & Perrings and from NRDA,
   is the reserve posted in advance against a per-event figure. The TA never shows one being sized.
3. **Options:** (a) scope the claim in a sentence; (b) add a short, labeled illustration of sizing from numbers
   already in §11.6; (c) add a new case (needs new facts; not recommended).
4. **Recommendation: (a) and (b).** State plainly that the §11 cases are retrospective. Then one paragraph,
   labeled as arithmetic and not as a case: per-unit reserve = RCV estimate − bonds already in force, using
   the §11.6 figures, with the range shown. No new sources. Which RCV level feeds it depends on Decision 3.
5. **Downstream:** §5.1.2; Ch 5 and Ch 9 (the bond chapters) once rebuilt.

#### F15. The §5.4 B₂-only moral-grounding flag

1. **Verdict: PARTLY (closed in text, never ratified).** §5.4 is titled "… B₂ Foreclosure Bond direction." §5.5
   ends with a paragraph that implements Option (i): "The backward-direction moral grounding is delivered
   operationally through that reparations-economics lineage." The 2026-05-13 proposal is marked "superseded by
   parallel-session work." There is no in-section note left in the TA.
2. **Why it matters:** B₁ gets a definition (F4) but its grounding is one sentence that names five people and no work.
3. **Options:** (i) leave; (ii) expand §5.4 to cover both directions; (iii) new §5.6.
4. **Recommendation: (i), tightened, and ask Darity.** Do not write new philosophy on his ground. Move the
   existing paragraph to the end of §5.4, retitle §5.4 to cover both directions, and ground B₁ in the
   Darity–Mullen structure the TA already cites in §5.1.1 (acknowledgment, redress, closure). Replace the name
   list with cited works only. Put the question "what should ground B₁?" in the cover note. His answer is worth
   more than a drafted §5.6.
5. **Downstream:** Ch 5 (the CSD paragraph promises §5.5); nothing numeric.

### E. Other checks

#### F16. Method 3's functional form: provenance

1. **Verdict: PARTLY.** The anchor's provenance is stated: "a posited 5%/yr calibration (… a calibration
   parameter, not an external datum)." The form's provenance is not. §3.5 calls the construct "the quasi-option
   value of preserving an irreversibly-losable commons (Arrow & Fisher 1974; Henry 1974)" and gives "four
   converging reasons" for the logarithm. Problems a specialist will raise:
   - Quasi-option value is the value of information gained by waiting. RCV_M3 has no learning term. The
     citation supports the concept, not the formula.
   - 1/(1 − α) is glossed "per-event expected loss given irreversibility probability α." An expected loss is
     α × loss. 1/(1 − α) is the sum of a geometric series. Its derivation is not given.
   - "Hotelling_anchor ≈ 5%/yr" is a rate; ln(1 + ς) is a pure number; their product is added to 1. The units
     do not balance unless the anchor is a pure number. The June audit flagged this (D5); it is still there.
   - "The logarithmic form is the conjugate that linearizes this exponential under integration" and the appeal
     to Cobb & Douglas 1928 (a production function) do not derive anything.
2. **Why it matters:** this is where the headline CS comes from (see N2).
3. **Options:** (a) say plainly it is a calibrated construct and trim the lineage paragraph; (b) derive the
   form from a stated model (a research task); (c) leave.
4. **Recommendation: (a).** Draft: *"The functional form is the framework's own parameterization. Arrow–Fisher
   and Henry supply the reason irreversibility carries a premium; they do not supply this formula. The form is
   chosen to be simple, to return the market price when scarcity and irreversibility are absent, and to make
   irreversibility the dominant term. The coefficient 0.05 is a dimensionless calibration constant."* Cut
   reasons 1, 2 and 4; keep 3.
5. **Downstream:** §0 (anchor units), §8.3, §9.3, §11.8, §15.1.3; glossary. No number changes.

#### F17. Open items on the STATE.md TA line

| Item | Verdict | Note |
|---|---|---|
| Apply 06-24 positioning findings | **OPEN** | Zero hits (F11–F13). |
| Three reef §11.12 calls | **PARTLY** | The content is already in v2.0.0 on main (§11.12, the "seven cases" census, the 10.1b note, Wilberg and Woods cited). What is open is the author's ratification. Two of the three have defects: the census (N8) and the reef's use of Theorem 10.3 (N11). One new issue: CSD is James River acreage while B₁ is bay-wide spending. |
| §6.3 "~$1,025–1,065/ton" | **PARTLY** | Derived in §11.6 as M3 centre minus $50–88. The $50 is underived (N5). The figure is in §3.6, §9.5 and §11.6, not §6.3. |
| §6.2 "Seven Abundance Dimensions" | **ALREADY-FIXED** | Zero hits for the phrase. |
| Render check | **OPEN** | Not done here (plan W5). |
| Changelog against the 05-15 copy | **OPEN** | Base: `tools/audits/ta-darity-version-diff_2026-06-07.md`. Will need this review's changes added. |
| List of call material | **OPEN** | "Darity" now appears 24 times (the plan says 18). The clearly call-derived passage is the Definition 1.10 heterogeneous-stakeholder paragraph (F12). Others in C6. |

---

## Part 2. New findings (N-series)

Each block: verdict and quotes; why it matters; options; recommendation; downstream.

#### N1. "Method 1" is two different methods

- **Finding.** §3.3: "Method 1 uses DAC (substitution-side; engineering reversal cost). Social Cost of Carbon
  … is the damage-side number." §9.1: "Method 1 — the damage-function audit (§3.3): bottom-up audit of all
  identifiable costs," and §9.2's total includes "Carbon" priced at the social cost of carbon. For McDowell,
  §3.6 gives M1 as "$290–2,702/ton across DAC horizons"; §9.5 gives M1 as "107–110× ($504–518 component floor ÷ $4.71)."
- **Why it matters:** the same label carries a replacement-cost estimate and a damage estimate that differ by up to five times.
- **Options:** (a) §3 governs; rename the §9 lens "damage-function floor" and stop calling it Method 1;
  (b) §9 governs and DAC becomes a variant; (c) call them 1a and 1b.
- **Recommendation: (a).** §3.3 draws the distinction on purpose and §11.9 repeats it.
- **Downstream:** §9.1, §9.2, §9.5 headers, §10.2, §11.1, §11.2, §11.3; ledger labels ("Damage-Function ~107–110×" is already named that way).

#### N2. Estimators of one quantity, or lenses on different quantities?

- **Finding.** §3.6: M1 and M3 "are the two independent RCV estimators, and their convergence range is the
  well-supported RCV." §11.6: "that overlap is the well-supported RCV." §9.1: "The lenses measure different
  quantities — a documented-damage floor, a price-independent premium multiple, a discounted integral — so
  their magnitudes legitimately differ." Result for McDowell: the integral that *defines* RCV gives
  "$525–540/ton"; the "well-supported RCV" is "~$1,000–1,500/ton"; and the headline CS "≈ $1,025–1,065/ton"
  is "RCV ~$1,115/ton (M3 geometric center)" minus the bond. The chapters use a fourth figure, the $510 total.
- **Why it matters:** the headline severance rests on the one estimator whose form is the framework's own
  (F16), and it is twice the definitional integral. The June correction fixed §9 and left §3.6 and §11.6 on the old frame.
- **Options:** (a) the integral is the definition and the headline; M1 and M3 are cross-checks reported beside
  it; CS headline = $525–540 minus B; (b) M1 ∩ M3 is the headline and the integral is a conservative floor,
  said so; (c) report all three with no headline.
- **Recommendation: (a).** It is the conservative choice, it matches the chapters' order of magnitude, and it
  survives if a reviewer rejects Method 3. It changes the McDowell CS from about $1,025–1,065 to about
  $440–490 per ton (525–540 minus 50–88), so it is the author's call.
- **Downstream:** §3.6 table, §9.5, §11.6, §11.7; ledger; calc engine constants; Ch 6 rebuild; F14.

#### N3. The printed multiples mix 2020 dollars with a 1960 price

- **Finding.** §11.6: "comparing a present-dollar RCV against a 1960-nominal price (an inconsistent basis)
  would inflate the ratio by an order of magnitude — the era-mixing the lens-explicit reporting discipline
  exists to prevent." §11.11: against a 1960-nominal price the ratio "inflates by roughly two orders of
  magnitude." (The two sections disagree on how much.) Yet §9.5 prints "107–110× ($504–518 component floor ÷
  $4.71)" and "61–115×"; §14.7 says "you absorbed at least $525 of cost for every $4.71/ton"; §16.4 repeats 61–115×.
  The low end uses "the contemporary ~$8.66," which has no source anywhere in the repo and contradicts the
  contemporary value used elsewhere: "$40–140/ton" (§7.6, §11.6) and `p=75.0` inside the integral's own code.
  The $190 social cost of carbon is also a recent-emissions figure applied to 1960 tons.
- **Why it matters:** this is the first arithmetic a hostile economist checks. On a consistent basis the
  integral lens is about 4–13× ($525–540 over $40–140), which agrees with Method 3's 8.5–26×. That agreement
  is a better result than the inflated one.
- **Options:** (a) headline the consistent-basis multiple; keep the 1960 comparison only as a labeled
  statement of two prices in two eras; (b) deflate $4.71 to current dollars and use that as the basis
  (needs a BLS series, to be sourced); (c) leave the lens-explicit labels as ratified in June.
- **Recommendation: (a), with (b) as a sourced footnote.** Retire $8.66 unless a source is found.
- **Downstream:** the ledger's IPG row (107–110×, and a stale 67–134×, see N10); a gate pattern for each
  retired figure in the same commit; Ch 8, Atlantic Ideas, the McDowell op-ed and Harper's all set "$4.71"
  beside "$510." Those can keep the two prices side by side if they do not state a multiple.

#### N4. Norway does not reconcile

- **Finding.**
  - Label: §3.4 and §3.6 call $48/BOE "the realized B₂." §11.5 calls it "B₁-for-Norwegians-only; B₂ globally
    underdeveloped." §5.3 says the fund is "canonical existing B₂."
  - Construction: "GPFG ~$2.0T … at ~75% capture rate … implies ~$2.67T total petroleum wealth ÷ ~55 billion
    BOE ≈ $48/BOE." Dividing by the capture rate gives total wealth, including the quarter not captured. The
    fund itself is about $36/BOE, and §11.5's own caveat says rent capture net of investment returns is "~$30–40/BOE."
  - Stale table: §11.5's summary table has M1 "~$300–$650" and M3 "~$70–$1,000 (mid: $280)" against text
    values $161–422 and $96–610. The June audit flagged the M1 cell (A10); it was not applied.
  - CS: §3.6 "~$233/BOE; ~$12.8T cumulative"; §11.5 "~$250/BOE … $13.75T … on the order of $13–$15 trillion."
  - §12 Scenario 5: "the Norwegian government owns its own oil fund … cost severance approaches zero
    automatically." §16.3: Norway is an "SCS = 0" example. §11.5: a residual of $13–15 trillion.
- **Why it matters:** Norway is the comparison case for everything else.
- **Recommendation:** B₂ everywhere; $48 replaced or relabeled as "state take per barrel (fund ÷ capture rate)"
  with the fund-only $36 shown; table cells fixed; one CS figure; §12 and §16.3 reworded to "domestic severance
  approaches zero; the global carbon cost does not."
- **Downstream:** ledger (Norway $48), calc engine line 138, Ch 4, Norway op-ed, proposal.

#### N5. McDowell's realized bond

- **Finding.** §11.6: "Total realized B … ~$53-60 billion … Per-ton coal: $53 billion / 600M tons ≈ $88/ton,"
  then "$50–88/ton societally-paid." $53–60 billion over 600 million tons is $88–100; the $50 has no
  derivation. "Industry-paid component is roughly $5-8 billion … ~$8-15/ton": $5–8 billion over 600 million
  is $8–13. Both were flagged in June (A11) and not applied. The engine passes because both ranges are typed
  in as constants ("TA §11.6 (landed)"). Separately, the numerators are national (Black Lung payouts "~$44
  billion cumulative through 2009"; reclamation shortfalls) and the denominator is "McDowell + adjacent
  counties." That overstates B per ton, which is conservative for CS but wrong as a statement of fact.
  The 1960 price is sourced to "Ch 6 convergence table"; the ledger says EIA Table 7.9.
- **Recommendation:** correct to $88–100 and $8–13, or state the allocation rule that gives $50; say the
  numerators are national and the figure is therefore an upper bound on B; cite EIA for $4.71.
- **Downstream:** CS level (with N2), §3.6, §9.5, engine constants, ledger.

#### N6. Convergence and Gate 3 contradict each other

- **Finding.**
  - §7.3 rejects a constant cost: "Under any Weitzman-type discount factor that decays only to a small nonzero
    asymptotic constant, the integral grows without bound." That confuses the discount *rate* settling at a
    positive floor with the discount *factor* doing so. §16.1 sets "r_min (~1%)"; with a positive long-run
    rate the factor decays exponentially and Theorem 10.4 (SC1) gives convergence. The rejected candidate passes.
  - §6.7 Walkthrough 3: "Stern Review's argument turns on declining-or-zero discount rate which makes the
    integral effectively infinite," then "apply Nordhaus DICE / Stern Review discount-rate convention … (Stern's
    ~1.4% …) the integral converges." Stern cannot be both. (Stern's rate is a low constant; its
    pure-time-preference component is 0.1%.)
  - §3.1: the discount factor "declines toward zero as t → ∞ but does so slowly enough that the integral
    converges." It should be "fast enough."
  - §16.1 has r_min ≈ 1%; the §11.1 calibration uses "r_∞ = 2% with a 50-year half-life."
- **Recommendation:** fix all four. Gate 3's rejected example becomes a term that grows exponentially faster
  than the discount rate, or a constant under a zero long-run rate. Pick one long-run rate and state it once.
- **Downstream:** F9; §7.5 Step 3; engine docstring.

#### N7. The §7.6 worked example

- **Finding.** §7.2 says the community-transition cost is "roughly $5–$15 per ton of coal extracted,
  distributed across the transition period." §7.6 says "$5–$15 per ton of coal per year during the transition
  window, approximately 1990–2050," then "Present-value contribution … approximately $5–$10 per ton." Sixty
  years at $5–15 a year cannot discount to $5–10 from 1960 at these rates; the total reading can. The "empirical
  allocation" has no source. And Gate 1 is run with the wrong counterfactual: "under a national
  community-transition-reserve fund fully bonded … the cost to the commons reduces to zero." That is a
  counterfactual in which a bond pays, not one in which a commons is abundant. Any cost vanishes if someone pays it.
- **Why it matters:** this is the TA's one worked example of admitting a new variable, and it blurs RCV with B.
- **Recommendation:** state the cost as a total per ton spread over the window; label it a framework estimate
  unless a source is supplied; rerun Gate 1 on a real abundance counterfactual (for example, abundant
  alternative employment and tax base), or pick a different third variable.
- **Downstream:** §7.2, §17.7, §17.8 ("adds ~$5–$10/ton").

#### N8. Stale and inconsistent residue (one batch)

All CONFIRMED; all mechanical unless noted.
- §11 intro: "validates the three-model convergence. All four cases show IPG ≫ 1 … all four involve B ≈ 0
  relative to RCV." Baotou's IPG is "not computable"; Deepwater's bond is $61.6 billion against about $70
  billion of cost. The June correction drafted a replacement for this line; it did not land.
- §3.2: "All empirical cases tested (§11) yield IPG ≫ 1." Same problem.
- §10.2 census: "two thought-experiment scenarios (asteroid mining; lunar regolith — see §13)." §13 has no
  lunar regolith; §12 has helium-3. Baotou is discussed but not counted. Thought experiments are counted as "tested cases."
- §5.3: post-mining Appalachia is the example of "high CSD but low forward-looking RCV." §11.7: "McDowell =
  very high CSD + very high uncaptured RCV."
- Asteroid iron: "RCV ≈ 0. Extract freely" (§12, §10.3, Corollary 10.5.1) versus "RCV_M3 approaches market price" (§3.5, §11.8).
- §11.8: the regime map says "Scarce-but-restorable … ς … scarcity_multiplier carries the work." At ς = 100 the
  multiplier is 1.23; at α = 0.1–0.5 the other factor is 1.1–2.0. Scarcity never dominates under this form.
  "Norway: ς + α near-equal" is 1.23 against 2.86. Same section: V_market "≈ $50–$500" beside "$40–140."
- Dixit & Pindyck: "which the framework does not use" (§3.5, §15.1.3); used in the Observation 10.5 argument and
  named as the option-value tradition in §15.1.9 and §15.2.3.
- Definitions appear in the order 1.8, 1.10, 1.9. "Ten categories" (1.8, §15.1.6) beside seven (§6.2).
  §15.1.6: "eighteen cases of this volume's research"; the TA shows far fewer.
- Cross-references: "see §4 below" for the bonds (should be §5), twice in §2.1; "§1.7" for Definition 1.7;
  "Ch 6 line 304 et seq." (a line number in a chapter due for rebuild); "Per bibliography §12"; in §6.7 "(§3),"
  "(§4)," "(§1)," "(§7)" mean walkthrough numbers.
- §14.2: "Hartwick's Rule is the investment policy that makes CS = 0 under the assumption S_max = 1." Not
  shown, and the externality term does not vanish under Hartwick.
- §15.2.3 defines "Intergenerational Option Value," a term absent from §0 and unused elsewhere.

#### N9. Ostrom is positioned three ways (see F12)

Recorded separately because it reaches beyond §14.5 and touches call material. Handled under F12 and Decision 6.

#### N10. Case figures drift from the ledger, and the ledger is stale

- **Finding.**
  - Walkthrough 6: "$461 procedural payment vs. $54 end-of-life conversation payment historically." The ledger
    (added today): $54 is "the standard office-visit rate … NOT 'a fee for a conversation.'" Also "extended his
    cognitive decline 5+ years" against the ledger's "nearly five years."
  - Same walkthrough: "25× growth in medical GoFundMe campaigns 2011-2020. 88% medical-GoFundMe failure rate.
    Racial disparity in crowdfunding success (Ly & Soman 2020)." The ledger's reconciliation note points to an
    AJPH 2022 source (437,596 campaigns). I could not match "Ly & Soman 2020" to anything in the repo. Treat as unverified.
  - Walkthrough 7: "Sackler $11 billion extraction = framework's predicted value extraction … The framework's
    prediction matches what the courts found." The framework postdates the record, as the next clause admits.
    "Strongest empirical validation" overstates it. The Vance paragraph is out of register for an appendix.
  - §14.4 presents "there are no grounds for discounting future well-being on the basis of pure time
    preference" as Rawls's words. The June audit flagged it as a paraphrase in quote marks (D2). A search this
    session could not confirm the wording. It is still in quote marks.
  - The ledger still lists "RCV-model estimate $580–620/ton" and "RCV-integral 67–134×." The TA and the gate
    file retired both on 2026-06-10 in favor of $525–540 and 61–115×.
- **Recommendation:** align Walkthrough 6 to the ledger; replace or remove the crowdfunding line; reword
  Walkthrough 7 to "consistent with the public record"; unquote Rawls or supply the page; amend the ledger.
- **Downstream:** Ch 5 (Butler) already uses the corrected figures; ledger amendment is internal.

#### N11. Theorem 10.3 is asked to do more than it proves

- **Finding.** §11.12: consumption faster than restoration "is exactly the condition under which cost
  severance is positive for a renewable commons (Theorem 10.3)." The theorem says nothing about cost
  severance and "does not cover: Renewable commons." §5.5: the theorem "operates whether the abundance being
  stripped is forward-projected or backward-realized," and is extended to "the abundance of freedom"; its
  domain is "a non-renewable depletable resource." Definition 1.8: "CIT's validity as a discovery methodology
  follows from Theorem 10.3." The theorem's conclusions restate its Assumption (ii) (June audit C2): it shows
  that *if* cost has that shape, masking follows.
- **Recommendation:** cite the theorem only for depletable stocks; for the reef say "by analogy, as the
  substrate goes ρ falls toward the non-renewable case" (the TA's next clause already says this); change
  "validity follows from" to "is motivated by."
- **Downstream:** §5.5, §11.12, Definition 1.8, F6.

#### N12. The commute and the domain definition (see F10)

Walkthrough 2 concludes "Foregone-life-time cost admits to RCV" for a case with no shared stock and no second
party. It conflicts with §6.6 and with §12's "requires distance." Handled under F10 and Decision 2.

---

## Part 3. Strongest-critic read (run once)

Two readers: a hostile, competent resource economist (C1–C5) and a reparations economist (C6).

#### C1. "Your flagship number is the social cost of carbon"

- **Finding.** §11.1: "the carbon pulse carries ≈92% of the level." The integral takes utility "at Definition
  1.3's lower bound r(t)·P," so the foreclosure term, the framework's own piece, supplies a few percent of
  $525–540. The remainder is EPA's $190 times an emission factor, plus $8–22 of other damages.
- **Critic's line:** the damage total is established work (Epstein et al. 2011; Muller, Mendelsohn & Nordhaus
  2011; EPA 2023). What does the framework add to the number?
- **Options:** (a) credit those sources for the total and locate the contribution elsewhere: the comparison
  with what was paid, the per-unit form, the reserve; (b) show the foreclosure term at something above its
  lower bound; (c) leave.
- **Recommendation: (a).** It is true and it disarms the objection. One paragraph in §11.1 and a row in the F13 table.

#### C2. "Method 3 is the market price times a number you chose"

- **Finding.** The scarcity multiplier is 1.2–1.3 across every case, so RCV_M3 ≈ 1.25 × price ÷ (1 − α).
  - α is defined as "probability commons cannot be restored at any finite cost," read "from physical
    registers." For coal the carbon cycle makes α 0.85–0.95. For Norwegian oil, the same atmosphere, α is
    0.50–0.75 because "institutional architecture lowers Norway's effective irreversibility … through GPFG."
    A savings fund does not make a barrel or the atmosphere restorable.
  - That makes Norway's RCV depend on its bond, so B sits on both sides of CS = RCV − B.
  - RCV_M3 ≥ price by construction, so "no computed lens in any case returns IPG ≤ 1" is guaranteed for this lens.
  - Bands spanning a factor of ten ("$340–$3,670"; "$290–$2,702") will overlap whatever the truth is. "Agree
    to within ~30% at center" compares two chosen centres.
- **Recommendation:** fix α to the physical definition (Norway's oil then takes the same carbon-cycle α as
  coal, and its institutional credit appears where it belongs, in B); say plainly that Method 3 cannot return a
  ratio below one and is therefore not evidence of direction; describe the overlap as "not inconsistent," not
  as convergence. This strengthens Decision 3's case for the integral as headline.
- **Downstream:** Norway M3 and CS change materially; ledger; Ch 4; engine.

#### C3. "Nothing could ever lower your estimate"

- **Finding.** §17.5: "Admitting an additional Cₙ₊₁ can only increase RCV … Adding correctly-specified
  variables cannot falsify CS > 0." The gates admit costs only. Benefits that extraction leaves to third
  parties and later generations (capital, infrastructure, knowledge) have no entry, except through Norway's α.
  Definition 1.7 says institutions are "ensuring CS > 0 structurally"; Observation 10.1b calls the same claim
  empirical and falsifiable.
- **Critic's line:** gross cost is being compared with a net payment.
- **Options:** (a) say RCV is gross by design and name what would falsify CS > 0 (a case where B ≥ RCV;
  Deepwater is close on documented costs); (b) admit benefit terms through the same gates; (c) leave.
- **Recommendation: (a)** now, and change "ensuring … structurally" in Definition 1.7 to "so that CS > 0 in
  every case examined (Empirical Observation 10.1b)." (b) is a Book 2 question.

#### C4. Case-level attribution choices that will be pressed

- McDowell's seam is described as "Pocahontas-seam" coal while the integral uses "S_max ≈ 0.85 for electricity
  generation." Public sources describe Pocahontas No. 3 chiefly as low-volatile metallurgical coal (one calls
  it steam coal). If most of it went to coke ovens, the substitutability figure and the story about
  substitutes are for the wrong use. Needs a sourced end-use split.
- All combustion carbon is assigned to the extraction, none to the burner or the buyer.
- The reef's 1910–1981 loss is assigned to extraction; a fisheries reviewer will ask about disease and sediment.
- **Recommendation:** one attribution sentence per case (the F10 scope statement requires it). Nothing here
  needs a new number, but each needs a stated rule and, for the coal end use, a source.

#### C5. Deepwater Horizon cuts the other way

- **Finding.** §11.2 divides one well's total damages by that well's revenue: "~15–16× ($61.6 billion all-in
  cost ÷ ~$4 billion private gain)." The well was chosen because it blew out. The per-barrel expected cost of
  offshore drilling is the comparable figure. And the record shows the operator paid $61.6 billion of roughly
  $70–74 billion: after-the-fact liability recovered most of the documented cost.
- **Critic's line:** this is a case for NRDA and tort, not against them.
- **Recommendation:** present Deepwater as what it is in the TA's own terms, "the largest realized
  industry-paid B₁," and as the contrast case with Mexico's $25.5 million (now in the ledger). Drop the IPG for
  it, or label it as conditional on the accident. Use it in the NRDA entry (F11): liability worked where the
  defendant was solvent, identifiable and under US jurisdiction.

#### C6. A reparations economist's reading of §5

Darity's published work is citable; anything from the May call is not, until he approves it.
- **Ownership of the method.** §5.5: "the methodology is the framework's, applied backward, with Darity and
  Mullen as the primary developers." Their method predates the framework. The 06-19 handoff already ruled the
  relation is a "method-port." **Recommended wording:** *"The method here is Darity and Mullen's. The framework
  adopts it for the Method-1 slot in the backward direction and adds nothing to it."*
- **What counts as restitution.** §5.1.1 lists "welfare-state instruments (universal healthcare, social-safety-net
  programs, public pensions)" in B₁ and says "Norwegian welfare-state is approximately B₁-for-Norwegian-citizens."
  The same section says Darity and Mullen "explicitly declare in favor of restitution," the material sub-type of
  redress. General programs open to everyone are not obviously that, and their published position on universal
  programs should be checked against the book before this goes to him. The F4 payer split would let the TA say
  it precisely: public spending is repair paid by someone else.
- **Why "Restitution" and not "Reparations."** §5.1.1: "'Reparations' carries US-political-specific loading;
  'Restitution' … reaching center-right, libertarian, and politically-cautious institutional audiences who
  would disengage." §5.2 repeats it. To this reader that is a statement that his field's word was avoided for
  palatability. The better reason is already in the next paragraph: in their typology restitution is the
  material component of redress, and the bond is that component. Lead with it; cut the audience argument.
- **Unsourced statements about his work.** "Darity and colleagues' more recent work prices the 6–7 year average
  life-expectancy differential" has no citation. "applies cost-to-cure reasoning … against the racial wealth
  gap accumulated through American policy choices since 1619" is the TA's characterization of their method.
  Each needs a page reference or a place on the approval list.
- **Time value.** §2.1 gives CSD a "low / zero / negative" discount posture in one line and never returns to
  it. The reef CSD is today's rebuilding cost with nothing for a century of lost service. He will ask how past
  harm is brought forward.
- **Recommendation:** fix the first three in Phase 2 (they are wording, not numbers). Put the fourth and fifth
  on the list of questions for him.

---

## Summary table

Size: S = under an hour of session work; M = a few hours; L = a session or more, or cascades outside the TA.

| ID | Finding | Verdict | Recommended action | Size | Author decision |
|---|---|---|---|---|---|
| F1 | "Three Ways" name | CONFIRMED | Keep the name, add a one-line gloss | S | **Y (1)** |
| F2 | Triangulation / three-methods language | CONFIRMED | Fix 4 sites, retitle §3.6 | S | N |
| F3 | Rule when Method 3 is Open | PARTLY | Add the floor rule; drop "no standing" | S | N |
| F4 | CSD and B₁ undefined; units | CONFIRMED | Two Definitions with payer split; fix §0 | M | **Y (2)** |
| F5 | Hotelling Identity, two CS | CONFIRMED | Restate as CS = (RCV − H) + (H − B) | M | **Y (3)** |
| F6 | Estimators near zero | CONFIRMED | One statement at §17; fix "genuinely $0" | S | N |
| F7 | Seven inversions | CONFIRMED | Keep 7, sharpen 4 and 7, relabel lists, no Autonomy | M | **Y (5)** |
| F8 | Gate 1 vs CAI/CCI | CONFIRMED | Three-step Gate 1 | M | **Y (5)** |
| F9 | Gates 2 and 3 | CONFIRMED | Keep four; state roles; fix Gate 3 | S | **Y (5)** |
| F10 | No incidence or attribution | CONFIRMED | Amend Def 1.7; scope statement; no fifth gate | M | **Y (2)** |
| F11 | Prior art missing | CONFIRMED | New §14.8, six entries; two Broome titles unverified | M | **Y (7)** |
| F12 | Ostrom axis | CONFIRMED | One axis in §14.5, §6.6, Def 1.10 | M | **Y (6, 7)** |
| F13 | Borrowed / added | CONFIRMED | Table before §1 | M | **Y (7)** |
| F14 | Reserve not illustrated | CONFIRMED | Scope sentence + labeled sizing paragraph | S | **Y (7)** |
| F15 | §5.4 B₁ grounding | PARTLY | Tighten; ask Darity | S | **Y (6)** |
| F16 | Method 3 provenance | PARTLY | Plain statement; trim lineage; fix units | S | N |
| F17 | STATE open items | mixed | See table in F17 | — | **Y (8)** |
| N1 | Two "Method 1"s | CONFIRMED | §3 governs; rename §9 lens | M | **Y (3)** |
| N2 | Estimators vs lenses; three RCV levels | CONFIRMED | Integral is the headline | L | **Y (3)** |
| N3 | Era-mixed multiples; $8.66 unsourced | CONFIRMED | Headline consistent basis; gate patterns | L | **Y (4)** |
| N4 | Norway does not reconcile | CONFIRMED | Five fixes | M | N (unless $48 changes: then Y with 3) |
| N5 | McDowell realized bond | CONFIRMED | Correct or derive; label national numerators | S | N |
| N6 | Convergence / Gate 3 errors | CONFIRMED | Four fixes | S | N |
| N7 | §7.6 example | CONFIRMED | Restate cost; rerun Gate 1 | S | N |
| N8 | Stale residue | CONFIRMED | Batch | M | N |
| N9 | Ostrom three ways | CONFIRMED | With F12 | — | (6) |
| N10 | Case figures vs ledger; ledger stale | CONFIRMED | Align; amend ledger | S | N |
| N11 | Theorem 10.3 overreach | CONFIRMED | Narrow three citations | S | N |
| N12 | Commute vs domain | CONFIRMED | With F10 | — | (2) |
| C1 | Flagship number is SCC | exposure | Credit sources; relocate the claim | S | (7) |
| C2 | Method 3 and α | exposure | Physical α; no "convergence" | L | **Y (3)** |
| C3 | One-way ratchet | exposure | Say gross by design; name the falsifier | S | N |
| C4 | Attribution choices | exposure | One sentence per case; source coal end use | M | (2) |
| C5 | Deepwater | exposure | Reframe as realized-bond case | S | N |
| C6 | §5 and reparations economics | exposure | Three wording fixes; two questions for Darity | S | **Y (6)** |

Rows marked N will be fixed in Phase 2 as listed unless the author objects.

---

## Decisions for the author (8)

Each has a recommendation. "Yes to all recommendations" is a complete answer.

1. **The name.** Keep "Three Ways of Counting" and add one sentence saying two estimate what is owed and one
   reads what was paid? **Recommend: yes; no rename before the Ch 6 rebuild.** (F1)

2. **Where "who bears it" lives.** Amend Definition 1.7 so the bond counts cost the beneficiary bears itself,
   add formal definitions of CSD and B₁ with a public/extractor split, and state that attribution is case work,
   with **no fifth gate**? And treat the commute as a teaching case outside the formal domain?
   **Recommend: yes to both.** (F4, F10, N12, C4)

3. **The McDowell headline.** Three linked choices:
   (a) "Method 1" means replacement cost only; the §9 damage audit gets its own name. **Recommend: yes.**
   (b) The integral ($525–540/ton) is the headline RCV; Methods 1 and 3 are cross-checks. This lowers the
   headline CS from about $1,025–1,065 to about $440–490 per ton. **Recommend: yes.**
   (c) Restate the Hotelling Identity as CS = (RCV − H) + (H − B). **Recommend: yes.** (N1, N2, C2, F5)

4. **The multiples.** Headline the consistent-basis multiple (about 4–13× on the integral lens; 8.5–26× on
   Method 3) and keep "$4.71 then, $525 now" only as two prices in two eras, with no ratio? This amends the
   ledger and needs gate patterns. **Recommend: yes.** (N3)

5. **Inversions and gates.** Keep seven inversions with Institutional and Political sharpened, add no Autonomy
   walkthrough; keep four gates and say which two are substantive; restate Gate 1 as level-of-claim, then
   grounding, then inversion? **Recommend: yes.** (F7, F8, F9)

6. **Passages Darity will read as his ground.** (a) Change "the methodology is the framework's" to "the method
   is Darity and Mullen's"; (b) lead the Restitution-versus-Reparations rationale with their typology and cut
   the audience argument; (c) take the call-derived Ostrom paragraph out of Definition 1.10 for this send and
   put it on the approval list; (d) ask him, in the cover note, what should ground B₁ and how past harm should
   be carried forward, instead of drafting it. **Recommend: yes to all four.** (C6, F12, F15)

7. **Prior art and the contribution claim.** Add a short "closest prior art" subsection (Costanza & Perrings,
   NRDA, TEEB/True Cost Accounting, El Serafy, Epstein and Muller et al., Mudliar & Koontz), a borrowed/added
   table before §1, and a labeled paragraph showing how a reserve would be sized, leaving the rest of the list
   to the chapters? **Recommend: yes.** Broome waits on two titles I could not verify. (F11, F13, F14, C1)

8. **The reef calls.** The three held items are already in the file. Ratify the two bibliography additions as
   they stand; **do not** ratify the "seven cases" census or the Theorem 10.3 sentence as written (fix under N8
   and N11); and decide whether the reef comparison should use James River spending only or say plainly that
   the damage is one river and the spending is bay-wide. **Recommend: say it plainly.** (F17, N11)

---

## Notes for Phase 2 (not started)

- Version on edit: archive v2.0.0, write v2.0.1. Math stays `.html`.
- Engines: replace typed-in constants for the McDowell bond, Norway bond and the $8.66 basis with derivations,
  so a pass means something.
- Gate patterns in the same commit for every retired figure or term (candidates: `8\.66`, `107–110×`,
  `61–115×` if Decision 4 is yes; `1,025–1,065` if Decision 3b is yes; `lunar regolith`; "three-model convergence").
- Ledger amendments: integral level and band (already superseded in the TA), Norway bond, McDowell bond, IPG row.
- After edits: invariants HIGH = 0, engines clean, render check, then the changelog against the 05-15 copy.
- Sources consulted this session for F11 and C4 are listed below; none has been added to the TA.

### Sources checked (bibliographic verification only)

- Costanza & Perrings 1990: https://econpapers.repec.org/RePEc:eee:ecolec:v:2:y:1990:i:1:p:57-75
- Gerard 2000: https://ideas.repec.org/a/eee/jrpoli/v26y2000i4p189-197.html
- Mudliar & Koontz 2021: https://informahealthcare.com/doi/epub/10.1080/08941920.2020.1864535
- El Serafy 1989 (via World Bank overview): https://documents1.worldbank.org/curated/en/185081493258142730/pdf/Environmental-and-resource-accounting-an-overview.pdf
- Epstein et al. 2011: https://hsph.harvard.edu/climate-health-c-change/news/full-cost-accounting-for-the-life-cycle-of-coal
- Muller, Mendelsohn & Nordhaus 2011: https://econpapers.repec.org/RePEc:aea:aecrev:v:101:y:2011:i:5:p:1649-75
- Broome 1992: https://philarchive.org/rec/BROCTC-12
- Pocahontas No. 3 seam (end use; mixed sources): https://www.wvencyclopedia.org/entries/1821 and https://wvexplorer.com/coal-mining/coal-fields/flat-top-pocahontas-coal-field/
- Stern discounting (0.1% pure time preference): https://www.bu.edu/eci/files/2019/06/SternDebateReport.pdf
