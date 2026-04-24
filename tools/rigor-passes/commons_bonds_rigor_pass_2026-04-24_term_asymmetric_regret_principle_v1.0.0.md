# Commons Bonds — Full Rigor Pass: Asymmetric Regret Principle (ARP)

**Version:** 1.0.0
**Date:** 2026-04-24
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.2.0.md` — full 11-module suite + §22 Path Comparison Mode + §22.4 usefulness-vs-goals alignment + Principle-#2 concept audit + Principle-#3 distinctness check vs Precautionary Principle literature.
**Scope:** resolves meta-pass §13.2.c DEFERRED status for Asymmetric Regret Principle. Tests Ring placement (promote / demote / retire / rename).
**Status:** rigor pass executed 2026-04-24; pending author ratification.
**Author:** Chris Winn

**Applies Working Principles:**
- **Principle #1** (effort-to-repair not rigor argument).
- **Principle #2** (audit concept not phrase) — 53 refs across 16 files audited at concept level; Ch 7 pedagogical use inspected.
- **Principle #3** (distinctness check) — tests ARP against established Precautionary Principle literature.

---

## §1. Executive summary

**RECOMMENDED: Option A — PROMOTE to Ring 2 (internal load-bearing), with a flagged sub-decision on rename.** ARP passes the load-bearing bar (20+ active refs across Ch 7 / Ch 9 / Ch 10 manuscript drafts + heavy pedagogical use in Ch 7 GuidanceDoc). It names a distinct decision-theoretic rule that the framework invokes repeatedly. **Flagged sub-decision:** whether to rename from "Asymmetric Regret Principle" to something that doesn't overclaim "Principle" status (candidates: "Reversibility Default," "Irreversibility Bias," "Asymmetric-Regret Rule").

**The key finding (Principle #2 concept audit):** ARP is actively used as an operational decision rule in Ch 7's Mars-colony-administrator scenario — the rule flips between "extract aggressively" (Comet flyby — access window closes permanently) and "preserve" (Europa — incommensurable externalities). This reversible-application-by-context is distinctive enough that ARP earns named-rule status.

**The distinctness-from-Precautionary-Principle check (Principle #3):**

| Dimension | Precautionary Principle (established literature) | Asymmetric Regret Principle (framework-specific) |
|---|---|---|
| Core claim | Act under uncertainty to prevent harm | Default to reversibility under quantification uncertainty |
| Axis of asymmetry | Risk of harm vs. cost of action | Reversibility vs. irreversibility |
| Application trigger | Environmental/health uncertainty | Cost-quantification uncertainty (specifically for RCV tail) |
| Operational rule | Prevent (default to action) | Preserve (default to inaction when extractive) |
| Can flip direction? | No — always precautionary | **YES** — flips for closing-window cases (Comet flyby: extract now) |
| Memorable aphorism | "Better safe than sorry" | "We can always extract later. We can never un-extract." |

**Distinctness verdict:** ARP is a RELATED BUT DISTINCT decision rule. Specifically: ARP's bidirectional flip-by-context is the distinguishing feature — Precautionary Principle defaults to preventive action; ARP defaults to reversible action (which means extract-aggressively when the reversible choice is extraction-during-access-window, preserve when the reversible choice is non-extraction). This reversibility-centric framing is framework-distinctive.

**Options tested:**

- **A — PROMOTE to Ring 2** (load-bearing, distinct from PP, heavy pedagogical use). **RECOMMENDED.**
- **B — DEMOTE to prose** (use the reasoning but drop the capitalized term). REJECTED — compresses poorly over 20 refs; loses named-rule pedagogical anchor.
- **C — RETIRE entirely and invoke Precautionary Principle instead.** REJECTED — ARP's bidirectional flip isn't PP; retiring loses the Comet-flyby case argument.
- **D — MERGE into existing framework element** (e.g., sub-entry under Substitutability Function). REJECTED — ARP operates on uncertainty about RCV tails, not S per se; poor fit.
- **E — RENAME** (candidates: Reversibility Default · Irreversibility Bias · Asymmetric-Regret Rule). **SUB-DECISION FLAGGED** — defer to author.

---

## §2. The question under test

### §2.1 V2 definition

> *"Asymmetric Regret Principle: When costs cannot be precisely quantified, default to what is reversible. Preserving something you didn't need is cheap; extracting something irreplaceable is not. 'We can always extract later. We can never un-extract.' Applies across all uncertainty ranges for high-CSG resources."*

### §2.2 Ch 7 pedagogical use (concept audit)

From Ch 7 GuidanceDoc (11 refs) + Ch 7 draft (4 refs):

**Comet flyby case:** *"The access window closes permanently. The asymmetric regret flips. The model is not anti-extraction — it says 'extract when RCV is low and preservation isn't an option.'"* — ARP operates here as a DIRECTION-FLIPPING rule; not a default-toward-preservation rule.

**Europa case:** *"The model honestly says 'I can't price this. The asymmetric regret principle applies: wait, study, decide later.'"* — ARP operates as preservation-default under incommensurable uncertainty.

**Summary statement:** *"The asymmetric regret, stated simply: 'We can always extract later. We can never un-extract.'"* — proverb compression.

**Practical instruments list:** *"CSG ranking, insurance cost, asymmetric regret, spatial cost severance."* — ARP listed as one of the book's framework-specific operational tools.

**Finding:** ARP is operationalized in Ch 7's decision-rule exercises. The bidirectional flip (Comet: extract; Europa: preserve) is the distinguishing feature.

### §2.3 Options

- **A — PROMOTE to Ring 2.**
- **B — DEMOTE to prose.**
- **C — RETIRE; invoke Precautionary Principle.**
- **D — MERGE into another framework element.**
- **E — RENAME** (and promote / demote at new name).

### §2.4 Sub-claims

**Option A:**
- SC-A1: 20+ active refs demonstrate load-bearing status.
- SC-A2: ARP is distinct from Precautionary Principle (bidirectional flip by context).
- SC-A3: Named rule serves pedagogical continuity across Ch 7/9/10.
- SC-A4: "Principle" naming is defensible given framework-specific operational rule.

**Option B (demote):**
- SC-B1: "Default to reversibility when uncertain" is prose-expressible without capitalized term.
- SC-B2: Reduces acronym load.

**Option C (retire, invoke PP):**
- SC-C1: PP is established in international law + environmental philosophy.
- SC-C2: Framework benefits from connecting to established literature rather than reinventing.

**Option E (rename):**
- SC-E1: "Principle" overclaims originality.
- SC-E2: "Reversibility Default" is more concrete; "Asymmetric-Regret Rule" softer.

### §2.5 Falsifiers

**Option A is falsified if:**
- ARP collapses into Precautionary Principle under Principle #3 check.
- 20+ refs are actually expressible as simple "prefer reversible" prose without a named rule.
- The bidirectional flip isn't really ARP-distinctive — it's a feature of any rule under context-sensitive application.

**Option C is falsified if:**
- ARP has distinctive content beyond PP that retiring would erase.
- Ch 7's Comet-flyby case (ARP directs extract) can't be expressed through PP (which is unidirectional toward preservation).

---

## §3. Distinctness check vs Precautionary Principle (Principle #3 — decisive module)

### §3.1 Precautionary Principle — the established baseline

**Rio Declaration 1992 Principle 15:** *"Where there are threats of serious or irreversible damage, lack of full scientific certainty shall not be used as a reason for postponing cost-effective measures to prevent environmental degradation."*

**Structural features:**
- Uncertainty trigger: scientific uncertainty about harm.
- Direction: act (toward prevention) despite uncertainty.
- Asymmetry axis: risk of ignoring early warnings.
- Unidirectional: always defaults toward preventive action.

### §3.2 ARP — framework-specific rule

**Per v2 + Ch 7 use:**
- Uncertainty trigger: can't precisely quantify RCV tails.
- Direction: choose the REVERSIBLE option — which can be either extract (Comet access-window closes) or preserve (Europa biosphere).
- Asymmetry axis: irreversibility of the chosen action.
- **Bidirectional: flips by context.**

### §3.3 Where ARP and PP overlap

- Both triggered by uncertainty.
- Both bias toward caution.
- Both have memorable aphoristic form.

### §3.4 Where ARP departs from PP (load-bearing distinctions)

- **PP always defaults to action-to-prevent-harm; ARP defaults to whichever-option-is-reversible.** For some cases these agree (Europa — preserve is both precautionary AND reversible). For other cases they diverge (Comet flyby — reversibility argues extract-now-because-window-closes; PP doesn't have a clean answer).
- **PP operates on harm uncertainty; ARP operates on cost-quantification uncertainty specifically for RCV tails.** Different trigger frame.
- **PP is a principle of ETHICS + LAW (how to act under scientific uncertainty); ARP is a decision-theoretic rule applied inside a pricing framework** (how to handle unpriceable tails in RCV). Different domain of application.

**Verdict on §3:** ARP is distinct from PP. Retiring ARP and substituting PP would lose the bidirectional-flip content. Option C rejected.

### §3.5 Does ARP collapse under closer analysis to something else?

Candidate reductions:
- **Max-min expected utility (Wald 1950):** maximize the minimum outcome. ARP has min-regret flavor but the reversibility axis is distinct.
- **Savage's minimax regret (1951):** minimize maximum regret. Closer to ARP spirit; asymmetric-regret is a specialization where the regret-distribution is bimodal with heavy tail on irreversibility.
- **Robust decision-making under deep uncertainty (Lempert et al.):** choose strategies that perform acceptably across many scenarios. ARP is simpler; prefers reversible actions regardless of scenario.

**Closest reduction:** ARP is essentially *"minimize maximum regret where regret is asymmetric, with irreversibility being the heavy-tail arm."* That's a specific variant of Savage's minimax regret applied to resource extraction.

**Does this reduction retire ARP?** No — because naming the framework-specific application is what gives the rule operational force in the book. Readers don't need to invoke Savage 1951 to use the rule; they just need the named rule.

**Academic-rigor concern:** in Ch 7 / Tech Appendix, the pass recommends a citation footnote linking ARP to Savage's minimax regret + Precautionary Principle. This positions ARP as a framework-specialization rather than a novel ethical principle.

---

## §4. The rename sub-decision (Option E)

### §4.1 Why this matters

"Principle" in "Asymmetric Regret Principle" is a heavy word — suggests foundational status. Given ARP is a framework-specific application of established decision-theoretic ideas, "Principle" may overclaim.

Alternatives:
- **Reversibility Default:** crisp, concrete, describes the operational rule.
- **Irreversibility Bias:** psychology-flavored; describes why we prefer reversible.
- **Asymmetric-Regret Rule:** softer than "Principle"; preserves the aphorism.
- **Keep: Asymmetric Regret Principle** — established in draft prose; renaming has 20-ref sweep cost.

### §4.2 Rename weighing

- **Rename cost:** 20 refs to update (Principle-#1: not a rigor argument; noted as scheduling).
- **Rename benefit:** less overclaim; more concrete name; better academic travel.
- **Rename risk:** breaks existing draft's rhetorical continuity; Ch 7 GuidanceDoc was crafted around "asymmetric regret."

### §4.3 Recommendation on sub-decision

**Defer to author.** This pass recommends keeping ARP as Ring-2 named rule; whether the name is "Asymmetric Regret Principle" vs. "Reversibility Default" vs. other is an author-voice + pedagogical-continuity decision, not a rigor decision.

If author ratifies rename, this pass's rigor analysis applies to whichever name is chosen — the UNDERLYING rule passes.

---

## §5. M1–M11 abbreviated results

- **M1 CORE:** ARP operates on the uncertainty boundary of RCV — applies where quantification fails. Compatible with framework CORE.
- **M2 Case study:** Ch 7 Mars/Comet/Europa + Ch 9 Renewable Imperative + Ch 10 integration — all use ARP actively.
- **M3 Book content:** 20+ refs in active draft prose. Retiring or demoting would require sweep.
- **M4 Craft:** ARP's aphoristic form ("extract later / un-extract never") is strong craft. Register: philosophical.
- **M5 Dinner-table:** "When uncertain, do the thing you can undo" parses immediately. ARP passes.
- **M6 Academic:** Connects to Savage + Precautionary Principle + Lempert; positioned as framework-specialization. Footnotes recommended.
- **M7 Originality:** Specialization of established minimax-regret reasoning; originality at the framework-internal operationalization level, not at the decision-theoretic level.
- **M8 Long-term:** Named rule serves adoption IF the name is strong enough. Rename sub-decision relevant.
- **M9 Risk:** "Principle" overclaim; mitigated by academic footnotes OR by rename.
- **M10 Publishing:** Neutral. Editorial might flag "Principle" as heavy; rename addresses.
- **M11 Critic:** *"Isn't this just Precautionary Principle?"* — Response: related but distinct (bidirectional flip + cost-quantification trigger); academic-audience footnote makes this explicit. Survives.

**§22.4 alignment:** Option A positive. Option C negative (loses bidirectional-flip content).

---

## §6. Verdict

**OPTION A — PROMOTE TO RING 2.** ARP earns framework-internal load-bearing status. 20+ active refs + distinct-from-PP + bidirectional-flip mechanism + memorable aphoristic form.

**Rename sub-decision — DEFERRED to author.** Pass recommends retaining "Asymmetric Regret Principle" unless author prefers "Reversibility Default" or similar. Rename doesn't affect the rigor verdict.

### §6.1 What changes

- **Terms Index:** ARP record `CURRENT` at Ring 2; supersedes earlier "DEFERRED" status from meta-pass §13.2.c.
- **Ring 2 count:** grows to 9 (assuming Abundance Masking promote also ratifies): Accountability Bond · CS=RCV−B · Four Gates · Abundances · Substitutability Function · Externality Tail · IPG · **Abundance Masking** · **Asymmetric Regret Principle**.
- **Glossary v3:** keep the v2 definition with minor edits to reference Savage minimax-regret as academic anchor.
- **Tech Appendix:** add a brief methodological footnote citing Savage 1951 + Precautionary Principle + Lempert et al. to position ARP academically.

### §6.2 What doesn't change

- Framework CORE math — unchanged.
- Ch 7 / Ch 9 / Ch 10 existing prose — unchanged (no rewrite sweep needed unless rename adopted).
- Substitutability Function — unchanged.

### §6.3 Cross-pairing note (post-CSG-retirement)

**Status:** CSG retirement ratified 2026-04-24 (commit `a9acf8e`). ARP's v2 reference *"Applies across all uncertainty ranges for high-CSG resources"* must be rewritten. Post-retirement canonical form: *"Applies across all uncertainty ranges for resources with large industrial-existential substitutability gaps."* This rewrite is a Phase A3 Stream A sweep target (same sweep that handles Ch 7 + Ch 9 "CSG" → "industrial-existential substitutability gap" replacements).

---

## §7. Term Provenance Record

### Asymmetric Regret Principle (ARP)

**Working definition:** Framework-specific operational decision rule — when RCV tails cannot be precisely quantified, default to the reversible option. "We can always extract later. We can never un-extract." Specialization of Savage-style minimax-regret applied to resource-extraction decisions under quantification uncertainty.

**Status:** `CURRENT` at Ring 2 (recommended by this pass; supersedes meta-pass §13.2.c DEFERRED status).

**Term-spec version:** v1.0 (first individual rigor pass on this term).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §13.2.c (commit `af2f18e`) — DEFERRED pending author re-read.
- This individual rigor pass — Option A (PROMOTE to Ring 2) recommended with rename-sub-decision flagged.

**Why Ring 2 (not Ring 1):**
- Framework-internal operational rule, not a public adoption target.
- Pedagogically useful but not the flagship contribution.

**Why NOT retired (despite overlap with Precautionary Principle):**
- Bidirectional flip-by-context is ARP-distinctive; PP is unidirectional.
- Trigger condition (cost-quantification uncertainty for RCV tails) is specific.
- 20+ active chapter refs make retirement expensive without rigor-justified gain.

**Depends on:** RCV (the function over whose tails uncertainty applies) · framework's cost-quantification methodology.

**Pairs with:**
- Substitutability Function (S) — ARP governs decisions about high-gap resources (formerly "high-CSG resources").
- Universality Test concept — ARP is the rule for the boundary-condition regime (where framework self-identifies limits).

**Staleness triggers:**
- Framework develops a formal minimax-regret treatment that subsumes ARP mechanically.
- Academic community adopts "Reversibility Default" or analogous terminology that would make current name outdated.

**Rename candidates (sub-decision deferred):**
- "Reversibility Default"
- "Irreversibility Bias"
- "Asymmetric-Regret Rule"
- (retain) "Asymmetric Regret Principle"

**Notes:**
- Academic positioning: cite Savage 1951 + Rio Declaration 1992 + Lempert et al. RDM in Tech Appendix footnote. Position ARP as framework-specialization of established ideas.
- Pedagogical positioning: Ch 7's Comet/Europa cases exhibit the bidirectional flip — keep these as canonical illustrations.
- "Principle" is a heavy word; consider rename if author prefers less-overclaiming framing.

---

## §8. Author-ratified resolutions

*Pending author ratification:*
1. **Primary verdict:** Option A (PROMOTE to Ring 2) — ratify Y/N.
2. **Rename sub-decision:** retain "Asymmetric Regret Principle" OR rename to one of the candidates OR hold for future pass.

---

## §9. Rerun gate

Rerun if:
- Framework restructures RCV in a way that changes what ARP applies to.
- Academic adoption shows "Reversibility Default" or analogous displacing "Asymmetric Regret Principle."
- Rename is ratified — rerun under new name to verify rigor transfers cleanly.

---

*End of individual rigor pass v1.0.0. Option A (PROMOTE to Ring 2) recommended. Bidirectional-flip mechanism distinguishes ARP from Precautionary Principle. Rename sub-decision deferred to author. Pending author ratification.*
