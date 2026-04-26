# Candidate prose additions tracker — 2026-04-26 forward

**Purpose:** Persistent index of candidate-prose-addition rigor passes — one entry per candidate that has been formally rigor-tested. Each candidate gets its own rigor pass (in `tools/rigor-passes/`) that answers two questions: (Q1) does the addition belong in the book at all? (Q2) if yes, which chapter is the best home? The tracker doc here points to those rigor passes so they don't get lost between sessions.

**Discipline:** Per author direction 2026-04-26 (correcting an earlier blunter "always expand" rule): when a candidate prose addition surfaces during register-review or rigor work and is rejected for its originally-proposed location, the candidate gets a **full rigor test** before any chapter-placement is recommended. The rigor test answers Q1 (belongs in the book at all?) and Q2 (best chapter home?) explicitly. Pre-judging chapter placement without rigor is the error this discipline corrects.

**Companion to other discipline docs:**
- `feedback_always_expand_rule.md` (memory) — expansion-discipline rule (structural framing default-yes; argumentative additions rigor-tested per candidate)
- `commons_bonds_rigor_protocol_v2.4.0.md` §3.5 — pre-publication-state discipline for M6/M11/M12 (Working Principle #7)
- `alignment/commons_bonds_open_insights_v1.0.0.md` — framework-decision tracker (decisions, not additions; companion not duplicate)

---

## §1. Active candidates (rigor-tested)

### Candidate #1 — 2008 housing-bubble-scale-vs-rescue-scope argument

**Surfaced:** 2026-04-26 during Ch 5 passage 1 register-review. Originally tested as A.3 4th sub-steelman option for Ch 5; rejected from Ch 5 per immediate rigor (scale mismatch with cost-severance mechanism focus). Author 2026-04-26 noted the framework response "seems like a hell-of-a thing to mention" and directed full rigor test on whether/where it belongs.

**Rigor pass executed:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-26_candidate_2008_scope_argument_v1.0.0.md`

**Q1 verdict (does it belong in the book?):** YES — passes M1 + M3 + M5 + M6 + M9 + M11 + §22.4 alignment. Argument extends framework's mechanism claim by isolating scope-choice as design variable distinct from crisis-scale.

**Q2 verdict (best chapter home?):** **Ch 9 primary placement (recommended)**; Ch 8 defensible secondary; Ch 10 echo-only at one-line reflective. Ch 5 + Ch 6 rejected.

**Status:** **closed-ratified 2026-04-26 (Chris Winn) — pending integration commits.** Author ratified Q1=yes + Q2=D (Ch 9 primary) + C (Ch 8 secondary) + E (Ch 10 tertiary). Full three-placement integration approved. Integration scope:
- **Ch 9 primary:** ~500-600 words at "political economy of resistance" or "entering wedges" section (pending integration during Ch 9 register-review this session)
- **Ch 8 secondary:** ~150-200 word cross-reference paragraph (pending integration during Ch 8 register-review this session)
- **Ch 10 tertiary:** one-line reflective echo (pending integration during Ch 10 register-review this session)
- **Bibliography:** Mian & Sufi 2014 *House of Debt* + Reinhart & Rogoff 2009 *This Time Is Different* promoted to §6 (Financial crisis and financial commons) — DONE in this commit cluster.

**Cross-references:** Ch 5 register-review session 2026-04-26 (originating context); the rigor pass; Ch 9 draft (recommended integration target); Ch 8 draft (secondary); bibliography §19 candidate list (Mian-Sufi + Reinhart-Rogoff promotions pending).

---

## §2. Discipline notes

### §2.1 When to add a candidate to this tracker

During register-review or rigor work, when an argumentative-addition candidate surfaces and is rejected for its originally-proposed location AND the framework response would arguably be load-bearing somewhere else in the book:

1. Run a full rigor test on the candidate (separate file in `tools/rigor-passes/`)
2. Rigor test answers Q1 (belongs in book?) and Q2 (best chapter?)
3. Add the candidate to this tracker with pointer to the rigor pass

Candidates that the immediate register-review rejects AND that have no plausible alternative home don't go in this tracker — the immediate rejection stands.

### §2.2 When to remove a candidate

When the candidate has been integrated into chapter prose at its rigor-pass-ratified best location and that integration has landed (committed). Mark closed-integrated with commit reference.

### §2.3 Periodic review

During Phase B chapter-revision passes, walk this tracker per chapter being revised; integrate the candidates whose rigor-pass-ratified best-chapter is the chapter being worked.

### §2.4 Distinction from open insights

Open insights track *framework decisions* (term ratifications; structural reframings; methodology choices). This tracker tracks *prose additions* (specific arguments / passages / cross-references that need integration). Different docs; different disciplines; cross-reference each other where relevant.

---

*End of candidate prose additions tracker. Active 2026-04-26 forward.*
