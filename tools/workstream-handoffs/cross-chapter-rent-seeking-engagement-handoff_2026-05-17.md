# Cross-chapter rent-seeking engagement — workstream handoff

**Date drafted:** 2026-05-17
**Workstream:** Cross-chapter rent-seeking engagement (Public Choice tradition compatibility)
**Status:** **RATIFIED 2026-05-18** by PM session. §5 draft content already applied to main via commit `a1e54d9` (2026-05-17, author direct push). Workstream-spinup ratification flips PROPOSED → RATIFIED. Cross-chapter touches landed at: Ch 5 line 184 (Architecture and rent-seeking section), Ch 9 line 133 (Public Choice complementary accounting section), Tech Appendix §1.10 line 608 (Scope: complementarity paragraph), Ch 8 line 123 (Political Capture Cost touch). **Residual follow-on items deferred to separate sessions** (see §9 Ratification log below).
**Origin context:** Ch 1 Pass 3 REAUDIT v3 (40-character full-rigor audit with adversarial coverage). Surfaced as the most intellectually-serious adversarial thread in the audit's §5.3 thread-pull synthesis.
**Recommended branch prefix:** `claude/rent-seeking-engagement-`
**Recommended sequencing:** spin up after Ch 5 + Ch 9 each complete their three-pass rigor cycles (per workstream #20 Phase A); this workstream applies a focused cross-chapter touch rather than a from-scratch chapter draft.
**Origin commit:** `76ca8a6` (Ch 1 Pass 3 REAUDIT v3 PROPOSED) — see [`tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`](../rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) §4 character #33 + §5.3 thread-pull synthesis.

---

## §0. Background — how this surfaced

Ch 1 Pass 3 REAUDIT v3 (2026-05-17) ran the full-rigor audience-load pass against a 40-character set including 10 adversarial / detractor characters explicitly designed to test chapter robustness (the v3 expansion ran per author directive: *"include detractors, even oil / coal paid economists looking to poke holes in the book or pull a thread to unwind it"*). The audit's §5.3 thread-pull synthesis surfaced one specifically-actionable adversarial thread:

**Character #33 (Public-choice theorist; Buchanan / Tullock / Virginia-school tradition) returned ⚠ EXCLUDE with an intellectually-serious critique** of the chapter's line-81 no-villain framing:

> *"The system did exactly what the system was designed to do" — by whom? Systems don't design themselves. FMLA (1993) was designed via a specific legislative process; business lobbies fought paid leave hard during the design phase. That's rent-seeking. Your no-villain framing either masks the rent-seekers who shaped the architecture or denies they exist. Both are analytically incomplete. Your framework claims to be cost-accounting; cost-accounting has to include who benefits from the cost-shift, not just who bears it."*

Author response 2026-05-17:

> *"I'd say your rent-seeking argument bears real weight and absolutely needs to be addressed. But I'd also argue that some of the books existing use cases show that not every group of extractors are heterogeneous with the cost bearers. But I will concede without preamble that the vast majority seem to be and in an effort to try to apply as broadly as possible I ended up with this miss that you correctly flagged."*

The author's concession + nuance about heterogeneity is the key framing input. The framework needs to engage rent-seeking analysis explicitly in the analytical chapters + Technical Appendix without claiming uniform applicability across all cases.

---

## §1. The Public Choice / rent-seeking critique (what the framework needs to engage)

**Public Choice theory** (Buchanan & Tullock, *The Calculus of Consent*, 1962; Tullock, "The Welfare Costs of Tariffs, Monopolies, and Theft," 1967): apply economic analysis to political and bureaucratic actors. Assume politicians, bureaucrats, voters, lobbyists, and regulators are rational self-interested agents, not neutral public servants.

**Rent-seeking** is the school's signature concept: actors expending resources to obtain privileges, subsidies, or favorable regulations from government — redistributive activity that creates no new wealth but transfers existing wealth. The classic example: a domestic industry spending millions lobbying for tariffs that protect it from competition; the lobbying expenditure IS the rent-seeking cost — economically wasteful but rational from the industry's perspective.

**Adjacent concepts:** rational ignorance (voters under-invest in being informed); regulatory capture (industries dominate the agencies regulating them); logrolling (legislators trade votes); iron triangles.

**The critique applied to the book's framework:**

The framework's central work is COST-ACCOUNTING — identifying who bears the cost when commons are extracted. Public Choice argues that the answer to who bears the cost is structurally INCOMPLETE without the complementary question: who shaped the institutional architecture that distributed the cost the way it did? Institutions do not emerge as neutral architectures; they emerge through political processes where rent-seekers compete to shape them. The framework's "no-villain" framing either:
- (a) **Masks** the rent-seekers who shaped the architecture (would be analytically dishonest if they exist), or
- (b) **Denies** they exist (would be empirically wrong; we have documentation of FMLA lobbying records + financial-deregulation lobbying records + many others).

The critique is intellectually serious because:
1. The no-villain framing IS a deliberate analytical move that brackets the agency question.
2. Public Choice argues you CAN'T bracket the agency question — institutions are *products of* rent-seeking, and the framework's job has to include accounting for who shaped the system.
3. If the framework doesn't engage rent-seeking, the framework can be attacked as "structural mystification" — making institutions seem like impersonal forces when in fact they were shaped by specific actors with specific interests.

---

## §2. Why this is load-bearing for the framework

Three reasons the framework needs to engage rent-seeking explicitly:

**1. Strengthens the framework rather than weakening it.** Acknowledging Public Choice as the complementary analytical tradition the framework operates alongside positions the framework as cost-bearing-party-identification that COMPLEMENTS rent-seeking-actor-identification. The framework supplies: who bore the cost? Public Choice supplies: who shaped the system that made them bear it? Both questions matter; the framework focuses on the first to give the second something concrete to apply to.

**2. Unlocks Public Choice readers as potential allies rather than detractors.** Public Choice has institutional weight (GMU economics; Cato; AEI; Mercatus Center; significant fraction of policy-think-tank readership). A properly-engaged complementary positioning brings these readers in. A silent framework that doesn't acknowledge the tradition reads as either ignorance-of-it or hostility-to-it — both costly.

**3. Preempts the "structural mystification" attack.** The strongest version of the Public Choice critique is that structural-architecture-analysis without rent-seeking-actor-identification *mystifies* — makes institutions seem like impersonal forces when they were shaped by specific people with specific interests. By explicitly naming Public Choice as the complementary analytical tradition the framework operates alongside, the framework neutralizes the mystification charge: it's not pretending architecture is impersonal; it's scoping its accounting work to one tractable question while pointing readers at where the other tractable question gets handled.

---

## §3. Heterogeneity nuance (where rent-seeking applies + where it blurs)

Per author concession 2026-05-17, the framework needs to be **honest about heterogeneity** rather than claiming uniform Public Choice applicability across all the book's cases. Specifically:

**Cases where extractors ≠ cost-bearers (rent-seeking analysis highly applicable):**
- **Libby asbestos (Ch 5):** W.R. Grace = extractor; Libby residents + downstream-asbestos-exposed populations = cost-bearers. Distinct populations; documented Grace lobbying history.
- **Deepwater Horizon (Ch 5):** BP + offshore oil industry = extractors; Gulf-coast fishing communities + ecological-cost-absorbers = cost-bearers. Documented MMS-as-captured-regulator history.
- **2008 financial crisis (Ch 5):** Financial-industry actors + executive-comp recipients = extractors; mortgage-distressed households + taxpayers absorbing TARP losses = cost-bearers. Most clearly-rent-seeking-shaped architecture in the book (Gramm-Leach-Bliley 1999; Commodity Futures Modernization Act 2000; documented Wall-Street lobbying records).
- **McDowell County coalfield (Ch 2 + Ch 8):** Coal-industry operators + absentee-mineral-rights holders = extractors; coalfield-community residents + miners with pneumoconiosis = cost-bearers. Distinct populations; documented industry-funded political-economy history.
- **Healthcare cost severance (Ch 5):** Pharma + insurance-industry lobbyists = extractors; patients + employer-health-plan-paying workers = cost-bearers. Distinct populations; documented industry-lobbying records.

**Cases where extractors ≈ cost-bearers (rent-seeking analysis blurs):**
- **Baotou rare-earth (Ch 5):** Global electronics consumers = both extractors (consume rare-earth-mineral-containing products) AND cost-bearers (eventually absorb climate + supply-chain externalities). The line between extractor and cost-bearer is genuinely diffuse here — the lobbying-actor-identification framework doesn't apply cleanly because the actors-who-benefit are not concentrated in a way Public Choice can isolate.
- **Social Security 75-year actuarial gap (Ch 5):** Current beneficiaries + politicians-within-re-election-window = extractors (benefit from kicking the can); future workers = cost-bearers. The extractors are partially-identifiable (politicians); but current beneficiaries are ALSO former workers who paid in (so they're partially cost-bearers in the historical frame). Temporal-heterogeneity rather than actor-heterogeneity.
- **Intergenerational climate cost (touched in framework introductions):** Current emitters = extractors; future generations = cost-bearers. Actors are diffuse; rent-seeking-actor-identification is intractable across temporal scales the way it's tractable within a single political-economic moment.

**Framing implication.** The framework's engagement with Public Choice should:
- Acknowledge that in the vast majority of the book's cases, extractors are heterogeneous from cost-bearers, and rent-seeking analysis is highly applicable + valuable
- Honestly note the cases where extractors and cost-bearers blur, and where the framework's cost-accounting is doing useful work that rent-seeking analysis can't easily replicate
- Position the framework + Public Choice as **complementary analytical tools with different scope conditions** rather than as alternatives or competitors

---

## §4. Cross-chapter scope — where engagement needs to happen

Per Ch 1 Pass 3 REAUDIT v3 §5.3 recommendation: hold Ch 1 as-applied (the no-villain framing is doing major load-bearing work for several Tier-1 / Tier-2 acceptance audiences; weakening it to placate Public Choice would damage acceptance verdicts). The rent-seeking engagement belongs in the analytical chapters where the framework operates at the political-economy register.

**Locations requiring engagement (in priority order):**

1. **Ch 9 (Pricing Honestly — policy economy chapter):** Primary engagement home. Add a dedicated section explicitly engaging Public Choice tradition + naming Buchanan and Tullock + positioning the framework as complementary.

2. **Ch 5 (The Accountability Gap — six case studies):** Add a dedicated cross-case section on architecture-and-rent-seeking after the case-study set + before the Restitution-and-Foreclosure apparatus section, addressing the rent-seeking dimension across the case-studies that have it.

3. **Technical Appendix scope-of-applicability section (§1.10 area or new subsection):** Add a brief boundary statement scoping the framework's complementarity with Public Choice as an explicit methodological-scope decision.

4. **Ch 8 (What Things Actually Cost — McDowell coalfield at depth):** Brief touch incorporating coal-industry rent-seeking actor history where it's already part of the McDowell-County political-economy narrative.

5. **Ch 6 (Three Ways of Counting — methodology):** Probably no engagement needed; the chapter is about cost-counting methodology, which is conceptually orthogonal to rent-seeking actor identification. Verify during workstream execution.

6. **AuthorsNote / paratextual:** No engagement needed; the AuthorsNote is biographical-archive register, not analytical-tradition-engagement register.

---

## §5. Per-location draft content

### §5.1 Ch 9 draft section — "Public Choice and the framework: complementary accounting"

Draft section to insert somewhere mid-chapter in Ch 9 (specific placement to be determined during workstream execution; suggested anchor: after the chapter's introduction of the framework's political-economy positioning + before the chapter's policy-recommendations section). Approximately 600-800 words.

> **Public Choice and the framework: complementary accounting**
>
> The framework's central question is who bears the cost. A complementary question — equally serious, equally tractable — is who shaped the architecture that distributed the cost the way it did. The Public Choice tradition, founded by James M. Buchanan and Gordon Tullock at Virginia and developed over six decades by their successors, has built rigorous tools for that second question. The framework operates alongside it, not against it.
>
> Public Choice begins from a methodological move that resists the temptation to treat institutions as neutral architectures. Institutions do not emerge by themselves. They are designed through political processes in which actors with concentrated interests compete against actors with diffuse interests. The Family and Medical Leave Act of 1993 — to take one example near the chapters that opened this book — was not authored by a deliberative committee balancing employer and employee interests in some impartial weighing. It was authored through a legislative fight in which business lobbies actively opposed paid leave and successfully pushed the final architecture toward twelve weeks of unpaid leave. That outcome is the residue of rent-seeking: lobbying expenditure deployed by actors with concentrated stakes to shape an institutional architecture that distributes cost asymmetrically. The architecture is not impersonal. Someone shaped it, and the shaping is on the public record.
>
> The framework this book develops focuses on the side of the architecture that absorbs the cost. Public Choice focuses on the side that shaped the architecture. Each is incomplete without the other. The framework's claim that "the system did exactly what the system was designed to do" is true; Public Choice adds the necessary follow-on — *and someone designed it, and we can identify them*. The framework's commons-pricing apparatus identifies the magnitudes; rent-seeking analysis identifies the actors. Read together, the two traditions describe the same architecture from two angles. Read apart, each is partial.
>
> Some cases the framework treats are sharper for rent-seeking analysis than others. Where extractors and cost-bearers are distinct populations — a corporate operator and a downstream community; a financial-services industry and a mortgage-distressed household; an industry trade association and a worker — the rent-seeking analytical chain runs cleanly. The framework's cost-bearing-party identification gives Public Choice's actor-identification something concrete to apply to. Where extractors and cost-bearers overlap — as with global electronics consumers who are both demand-side beneficiaries of rare-earth mining and eventual absorbers of the supply-chain externalities — the rent-seeking framing blurs and the framework's structural-accounting framing carries the analytic weight that rent-seeking cannot easily isolate. The book is honest about both kinds of case, and treats neither as the default.
>
> The framework is therefore not a Public Choice book, and does not aim to be. It is also not a structural-mystification book that treats institutions as impersonal forces no one shaped. It is a cost-accounting book that names what is absorbed and by whom, and that points to where the architecture-shaping analysis lives when readers want to ask the next question. Buchanan and Tullock built the apparatus for that next question; this book recommends reading them alongside it.
>
> The practical implication for readers in the policy-economy traditions Public Choice has shaped — readers at AEI, Cato, the Mercatus Center, George Mason economics, and the broader policy-think-tank cluster influenced by Virginia-school analysis — is that the framework here is a foundation their apparatus can use, not a competitor for the analytical space they already occupy. The framework supplies the magnitudes; their apparatus supplies the actor accountability. Both are needed; neither is sufficient alone.

### §5.2 Ch 5 draft section — "Architecture and rent-seeking: who shaped the system?"

Draft section to insert into Ch 5 after the six case-studies + before the Restitution-and-Foreclosure apparatus section (suggested anchor: around current line ~180 of Ch 5 where the cross-case synthesis begins). Approximately 500-700 words.

> **Architecture and rent-seeking: who shaped the system?**
>
> The cases this chapter has documented share a structural pattern: a commons is consumed; the costs are absorbed by parties downstream or downwind or downstream-in-time of the consumption; the accountability architecture as it currently stands does not require the absorbed costs to be priced. The framework that the rest of this book develops is the response apparatus — the matched-comparison methodology, the cost-severance-damages instrument, the Restitution and Foreclosure Bonds. That work focuses on the side of the architecture that absorbs the cost: who bore it, how much, and what an honest accounting would require.
>
> A complementary question — necessary, but distinct — is who shaped the architecture that distributed the cost the way it did. The Public Choice tradition (Buchanan, Tullock, and their successors) has built rigorous tools for this question. Where extractors and cost-bearers are distinct populations, the rent-seeking analytical chain runs cleanly: identify the concentrated-interest actors who shaped the relevant institutional architecture; identify the lobbying expenditures and political coalitions that produced the current design; identify whose interests the architecture serves and whose it costs.
>
> Several of the cases this chapter has documented have well-documented rent-seeking architectures:
>
> - **Libby asbestos:** W.R. Grace's documented lobbying record at EPA, including the multi-year delay in asbestos regulatory action that the company's own internal documents (released during litigation) reveal as deliberately sought. The architecture that allowed Grace to operate the Libby vermiculite mine for decades after the asbestos contamination was known to the company was shaped by Grace's own rent-seeking.
> - **Deepwater Horizon:** The Minerals Management Service was a textbook captured regulator; the offshore oil industry's funding of MMS personnel travel, gifts, and revolving-door employment was so well-documented that post-disaster restructuring split MMS into three successor agencies. The architecture that produced the Macondo blowout was shaped by industry rent-seeking that the Department of Interior Inspector General reports had been describing for years.
> - **2008 financial crisis:** The deregulatory architecture that produced the crisis — Gramm-Leach-Bliley 1999, the Commodity Futures Modernization Act 2000, the various Office of the Comptroller of the Currency preemption rules through the 2000s — was shaped by financial-industry lobbying expenditure that the Center for Responsive Politics and successive Congressional hearings documented in detail.
> - **Healthcare cost severance:** Pharmaceutical-industry lobbying expenditure consistently leads U.S. industry-lobbying totals; the Patient Protection and Affordable Care Act's prohibition on Medicare drug-price negotiation (since modified) is a textbook rent-seeking outcome.
> - **McDowell County (developed at depth in Chapter 8):** The coal industry's political-economic dominance in West Virginia legislative and regulatory architecture is a multi-generational rent-seeking history.
>
> Other cases this chapter has documented blur the extractor / cost-bearer line in ways that make rent-seeking actor identification less tractable. Baotou's rare-earth supply chain is shaped by global electronics-consumer demand as much as by specific industry-lobbying; the Social Security actuarial gap is shaped by an intertemporal political-economic dynamic in which current beneficiaries and politicians-within-re-election-window benefit from kicking the gap forward, but current beneficiaries are also former workers who paid in. The framework's structural-accounting work carries the analytic weight in those blurred cases; rent-seeking analysis is most powerful where the actor populations are sharpest.
>
> The framework's accounting of who bore the cost is therefore compatible with — and depends on — the Public Choice tradition's analysis of who shaped the architecture. Read together, the two questions describe the same systems from complementary angles. Read apart, each is partial. The remainder of this chapter develops the framework's response apparatus; readers who want the architecture-shaping analysis the framework's apparatus does not perform should read Buchanan and Tullock and their successors in parallel.

### §5.3 Technical Appendix draft — scope-of-applicability boundary statement

Draft to add as a new subsection in the Tech Appendix scope-of-applicability section (suggested anchor: existing §1.10 if present, or a new §1.11). Approximately 200-250 words.

> **§1.11 (or appropriate §) — Scope: complementarity with Public Choice / rent-seeking analysis**
>
> The framework's cost-severance accounting operates at the architecture level — identifying which parties absorb which costs given an institutional architecture's distributive properties. A complementary analytical question — who shaped the institutional architecture, by what political-economic process, with what rent-seeking expenditure — is the domain of Public Choice analysis (Buchanan, Tullock, and successors).
>
> The framework is compatible with Public Choice analysis layered on top of it, and depends on it for cases where the architecture's origins are part of the substantive analytical work. The framework does not attempt to replicate Public Choice's actor-identification methodology; the framework's apparatus is calibrated for cost-bearing-party identification + magnitude, not for political-coalition-of-architecture-shapers analysis.
>
> Applicability conditions:
> - **Sharpest application of Public Choice complementarity:** cases where extractor populations and cost-bearer populations are heterogeneous (corporate operator vs downstream community; industry lobbying vs unaffiliated household; financial-services concentration vs diffuse depositor base).
> - **Blurred application:** cases where extractor and cost-bearer populations overlap (consumer-good supply chains where consumers occupy both roles; intergenerational dynamics where temporal-distance creates an actor-identification challenge that present-tense Public Choice analysis is not optimized for).
> - **Out of scope of this Technical Appendix:** rent-seeking-actor-identification methodology; the Appendix does not develop this apparatus and refers readers to the Public Choice literature for it.
>
> Readers in the Public Choice tradition should read the framework's cost-bearing-party identification as a foundation their apparatus can apply to, not as an alternative to their apparatus.

### §5.4 Ch 8 draft — brief touch on coal-industry rent-seeking

Draft language to incorporate (brief; 100-200 words) into Ch 8's McDowell-County coalfield depth-treatment, at a natural anchor-point where coal-industry political-economic history is already part of the narrative.

> *[Suggested incorporation, register-matched to Ch 8's voice:]*
>
> The architecture that produced McDowell County's specific form of post-extraction collapse was not impersonal. It was shaped, generation after generation, by coal-industry political-economic actors — operators, absentee-mineral-rights holders, industry trade associations — whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record. The cost-bearing-party analysis the framework performs (who absorbed what; over what timeframe; against what counterfactual) operates on top of an architecture that specific identifiable actors shaped. The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) does both kinds of work at once for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) does the architecture-shaping work cleanly for cases where the political-coalition record is on the books. Both readings illuminate McDowell. The framework's apparatus contributes the cost-bearing magnitudes; both adjacent traditions contribute the actor-and-coalition analysis the framework does not attempt.

### §5.5 Ch 6 (Three Ways of Counting) — verify during execution

Probably no insertion needed; Ch 6 develops cost-counting methodology, which is orthogonal to rent-seeking actor identification. Verify during workstream execution by reading Ch 6 for any architecture-shaping claims that would benefit from a Public-Choice complementarity flag.

---

## §6. Sequencing + dependencies

**Suggested sequencing:**

1. **Wait for Ch 5 + Ch 9 three-pass rigor cycles to complete** (workstream #20 Phase A). The drafts in §5 above are based on the current state of these chapters; if either chapter undergoes substantive revision via its three-pass cycle, the drafts may need to be refit to the post-rigor-pass state.

2. **PM session ratifies the workstream + reviews draft content.** Author can adjust draft content + voice + register before any chapter touches.

3. **Workstream session applies the four touches** (Ch 5 + Ch 9 + Tech Appendix + Ch 8) in a single feature branch.

4. **Each touched chapter gets a focused mini-rigor-pass** (similar to a Pass-1 / Pass-2 follow-up rather than a full three-pass rerun) verifying the insertion lands cleanly + doesn't trip the chapter's existing audience-load verdicts.

5. **PM session adds a cross-thread flag** in `publishing/essays/_pipeline/cross-thread-todos.md` if any chapter-specific audience-load discounts surface from the inserted content (parallel to the Ch 1 Pass-3 center-right discount disposition).

**Dependencies:**
- Ch 9 must exist in a near-final state. (Verify: per workstream #20 Phase A schedule, Ch 9 fact-check Pass 1 PROPOSED landed 2026-05-15 commit `9720da0`; voice-polish Pass 2 + audience-load Pass 3 pending.)
- Ch 5 three-pass cycle CLOSED (commits `da26bdc` / `d68d92e` / `7cbb9c1` / `d2ee178` + Pass 3 RATIFIED 2026-05-14). Ready for cross-chapter touch.
- Ch 8 three-pass cycle status: Pass 1 PROPOSED landed 2026-05-16 commit `210b02c`; Pass 2 + Pass 3 pending.
- Tech Appendix Pass 3 disposition: per PM-session-handoff 2026-05-13 status. Verify state before touching.

**Branch:** `claude/rent-seeking-engagement-<harness-id>` from current `origin/main`.

---

## §7. Open questions for PM session

1. **Whether to wait for all dependency chapters to close their three-pass cycles** before spinning up, or to apply touches incrementally as each chapter completes its cycle. Recommendation: wait. Reasoning: the rent-seeking engagement is a cross-chapter coherence move; doing it all at once preserves consistency in how the framework engages the tradition across locations.

2. **Whether Ch 9 needs the longer draft (§5.1) or a tighter version.** The proposed Ch 9 section is ~700 words; some Ch 9 readers will want more depth, others will want less. Author judgment + Ch 9 three-pass cycle's audience-load read should inform.

3. **Whether to add Buchanan + Tullock to the bibliography.** Likely yes, given the explicit engagement in Ch 9 + Tech Appendix. Suggested entries:
   - Buchanan, J. M., & Tullock, G. (1962). *The Calculus of Consent: Logical Foundations of Constitutional Democracy.* University of Michigan Press.
   - Tullock, G. (1967). "The Welfare Costs of Tariffs, Monopolies, and Theft." *Western Economic Journal*, 5(3), 224-232.
   - Possibly: a modern successor work (e.g., Mueller, D. C. (2003). *Public Choice III.* Cambridge University Press) for current-state reference.
   - These would join bibliography as a new §22 (or appropriate section) "Public Choice / political-economy tradition."

4. **Whether the Ch 8 touch is necessary or whether the cross-tradition acknowledgment lives sufficiently at Ch 5 + Ch 9.** Lean toward including it (Ch 8 is the McDowell-coalfield depth chapter; coal-industry rent-seeking history is well-documented + germane) but author can rule otherwise.

5. **Whether to flag this engagement in the Ch 1 Pass 3 REAUDIT v3 doc's §5.3 "Open questions" section** so future audits know the engagement is in flight. Recommendation: yes; cross-thread coherence.

---

## §8. PM session spinup metadata

**Workstream name:** Cross-chapter rent-seeking engagement (Public Choice complementarity)
**Trigger to spin up:** PM session ratification + dependency chapters (Ch 5 + Ch 9) at three-pass-cycle-closed state.
**Estimated session length:** moderate (single session). Four touches to apply + brief verification reads per chapter; no from-scratch drafting required given the §5 drafts.
**Branch:** `claude/rent-seeking-engagement-<harness-id>`.
**Merge-to-main default:** per CLAUDE.md, post-author-ratification spot-fix application sessions autonomously fast-forward merge to main; this workstream qualifies once author ratifies the §5 draft content.
**Cross-thread items:** add entry in `publishing/essays/_pipeline/cross-thread-todos.md` (PM-session task).

**Cross-thread coherence flags:**
- Touches multiple chapters; verify post-application that each chapter's three-pass rigor cycle remains CLOSED (no new audience-load discounts).
- The bibliography update (per §7 open question 3) is a parallel-track item that should land in the same workstream or in an immediately-following bibliography-update session.
- The Ch 1 Pass 3 REAUDIT v3 doc should be updated post-completion of this workstream to record that the cross-thread thread-pull from §5.3 is resolved.

---

---

## §9. Ratification log

**Ratified 2026-05-18** by PM session (handoff `pm-session-handoff_2026-05-18.md` §5.1 IN FLIGHT row + §8 Decisions pending closure).

**State of work at ratification:**

- ✅ **Four cross-chapter touches APPLIED** via commit `a1e54d9` (2026-05-17, author direct push, stopped at feature-branch-equivalent then merged to main):
  - Ch 5 line 184 — "Architecture and rent-seeking: who shaped the system?" section
  - Ch 9 line 133 — "Public Choice and the framework: complementary accounting" section
  - Tech Appendix §1.10 line 608 — "Scope: complementarity with Public Choice / rent-seeking analysis" paragraph
  - Ch 8 line 123 — brief touch within Political Capture Cost section
- ✅ All four touches verified present on origin/main 2026-05-18 (PM session spot-check).

**Residual follow-on items (flagged for separate sessions; not gating this workstream's ratification):**

1. **Per-chapter mini-rigor-pass verification** (per §6 step 4) — each touched chapter (Ch 5, Ch 8, Ch 9, TA) gets a focused verification read confirming the insertion lands cleanly + doesn't trip the chapter's audience-load verdicts. Ch 5 + TA already at three-pass-cycle-CLOSED state pre-touch; mini-pass is light. Ch 8 + Ch 9 have Pass 1 PROPOSED only; their forthcoming Pass 2/3 cycles will absorb the rent-seeking-section verification as standard pass scope. **Disposition: route into Ch 8 + Ch 9 Pass 2/3 cycles when those fire; no standalone session needed.**

2. **Bibliography additions** (per §7 open question 3) — Buchanan & Tullock 1962, Tullock 1967, Mueller 2003 likely belong in bibliography as a new "Public Choice / political-economy tradition" section. **Disposition: route into bibliography Phase A workstream (§7 Apparatus); fold alongside the Darity C-2 Du Bois addition.**

3. **Ch 1 Pass 3 REAUDIT v3 doc update** (per §7 open question 5 + §8 cross-thread coherence) — the REAUDIT doc's §5.3 thread-pull synthesis should be updated to record that the rent-seeking engagement thread is RESOLVED. **Disposition: minor doc-state update; can land as a small standalone commit or fold into the next Ch 1 dashboard touch.**

4. **Cross-thread-todos entry** (per §6 step 5 + §8) — add an entry to `publishing/essays/_pipeline/cross-thread-todos.md` flagging the engagement landed + pointing at this ratification log. **Disposition: small PM-session task; can land in the next dashboard refresh.**

**Standing reference:** this workstream's §5 draft content + §6 sequencing logic + §7 open questions remain as the canonical reference if any of the four touches needs to be revisited or re-engaged (e.g., if Sandy or another reviewer surfaces a follow-up critique of the engagement).

---

*End of cross-chapter rent-seeking engagement workstream handoff — RATIFIED 2026-05-18.*
