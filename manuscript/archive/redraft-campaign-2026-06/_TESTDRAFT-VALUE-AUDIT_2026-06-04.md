# Test-Draft Value-Retention Audit (2026-06-04)
**Adversarial audit answering: did the lens-driven sleeper drafts lose value?** 8 agents compared each ORIGINAL chapter against its test-draft. **Verdict: "lost NONE of the value" is FALSE for every chapter — but no chapter needs a re-draft.** Losses are small, identifiable, restorable (sentences-to-paragraphs), and concentrated in three patterns. All 7 rated `yes-with-restorations`. Per-chapter cut/add/lost-value detail in `_testdraft-value-audit-detail_2026-06-04.json`.

**The three systematic patterns (see synthesis §4):**
1. **"Relocate" became "delete"** — the dominant risk. ~3,600w (Ch9) + ~1,200w (Ch5) marked `[RELOCATE TO ChX]` and excised, but the moves are PROPOSALS, never executed. Until the destination carries it, the value is GONE from the corpus. **This is exactly what the coordinated reconciliation pass must close.**
2. **Over-cut last-instances mistaken for redundancy** — the 13-year life-expectancy gap, the Dunbar couplet's "this debt we pay," the CIT two sub-forms, the bond-forward-posting link, Lewis/UMW. Memo said "cut to one"; draft cut to zero. Restorable in sentences.
3. **Polanyi/Fraser adds are the bright spot but** (a) re-inflate and (b) carry author-characterization risk → need a Pass 3.1 fact-check (D1).

**Plus Severity A (blocking): scaffolding brackets (`[CITATION GAP]`, `[RELOCATE TO]`) leaked into the running prose of all 6 shrunk drafts — must strip before any render. Ch2 is worst (dirtier than its original AND didn't shrink).**

---

# Value-Retention Audit — Synthesis Across 7 Chapters

## (1) VERDICT TABLE

| Chapter | Words-delta | safe_as_redraft_base | Lost-value items | Notable |
|---|---|---|---|---|
| **Ch5** | Down (overshot target: 8,822w, kept MORE than the aggressive option) | yes-with-restorations | **5** | 1 hard drop (Niger Delta) + 1 dangling promise (Sandel) + 2 unverified relocations |
| **Ch6** | Down hard (13,431 → 9,103, −32%) | yes-with-restorations | **5** | 2 genuinely load-bearing over-cuts beyond memo authorization |
| **Ch9** | Down hard (~3,600w relocated) | yes-with-restorations | **6** | Largest relocation risk; 4 blocks excised-but-not-landed |
| **Ch2** | Essentially FLAT (5,434 → 5,373, −1.1%) | yes-with-restorations | **4** | Failed to tighten; dirtier than original (scaffolding leaks) |
| **Ch4** | Down (modest) | yes-with-restorations | **3** | Cleanest of the set; nets RICHER in argument |
| **Ch7** | Down | yes-with-restorations | **4** | Near net-gain; 1 clean loss + 3 conditional |
| **Ch8** | Down | yes-with-restorations | **6** | 4 quiet over-cuts beyond memo + 1 unverified new figure |

**Headline for the skeptic:** Your instinct is partially right. Across all three chapters you flagged (Ch5/Ch6/Ch9), the drafts did lose genuinely load-bearing content beyond what the deep-pass memos authorized. None is fatal; all are restorable in sentences-to-paragraphs, not restarts. But "lost NONE of the value" is false for every chapter in the set. The honest verdict is "lost a small, identifiable, restorable amount — and relocated a larger amount that is not yet confirmed to have landed."

---

## (2) THE LOST-VALUE LIST — consolidated and prioritized

### SEVERITY A — BLOCKING. Must fix before ANY draft renders or merges (mechanical, affects all 6 shrunk chapters)

**A1. Inline scaffolding markers leaked into prose (Ch2, Ch4, Ch5, Ch6, Ch7, Ch8, Ch9).**
Every shrunk draft carries `[CITATION GAP: ...]` and `[RELOCATE TO ...]` brackets embedded in the running prose. These are HIGH-severity hits under the Stage-1a scaffolding-invariant scan (`tools/quality-gates/scaffolding-patterns.yaml`) and CANNOT ship. Worst case is **Ch2**, where the brackets make the draft *dirtier than the original it came from* (the original stated those figures cleanly). Strip or resolve every bracket before any move toward render.

### SEVERITY B — TRUE LOST VALUE. Excised content, no confirmed home. Restore before using the draft.

**B1. Niger Delta exemplar — Ch5.** 3 uses → 0, with NO relocation home. The chapter's *only* sustained non-US extraction-community example for the Restitution Bond, and half of the structural-independence illustration ("McDowell after coal, the Niger Delta after sixty years"). Its loss narrows demonstrated portability to US-only and undercuts the "methodology is portable, calibration differs" claim. **Restore at minimum the orig-228 structural-independence pairing.**

**B2. Commons Inversion Test two sub-forms (Commons-Absence / Commons-Consumption) — Ch6.** Dropped entirely; with Ten-Categories and Four-Gates also compressed, they have NO home left in-chapter. These are the operational heart of the discovery method the chapter claims as its #3 contribution — Commons-Consumption Inversion is what admits the personal-scale time/autonomy cases and distinguishes extraction-commons from Ostrom coordination-commons. **Restore the named distinction in 1–2 sentences.**

**B3. Bond-forward-posting architecture link — Ch6.** The orig-¶121 closing sentence ("naming the tail is what makes the bond's forward-posting architecture necessary... a bond against a tail must carry forward indefinitely") is the causal link from term-choice to instrument design. Not lexicography. **Restore as one sentence.**

**B4. Lewis/UMW history paragraph — Ch8.** Memo said cut to ONE sentence; draft cut to ZERO, unflagged. The chapter's only narrated demonstration that political capture ran through *labor's own institutions against labor* ("the rank and file paid the difference"). Originality-bearing + values beat. **Restore one compressed sentence.**

**B5. 13-year life-expectancy gap as a hard number — Ch8.** Two separate cuts conspired to erase it; the number is now stated NOWHERE. Recurring, citable book figure and the human-scale anchor of the McDowell case. **Restore the number in at least one location.**

**B6. Dunbar couplet truncation — Ch8.** Dropped line "this debt we pay to human guile" is the verbal hinge making the mask quotation do *cost-accounting* (debt/pay) work rather than just evoke concealment. **Restore the full couplet.**

**B7. Delivery-cost grounding has zero residue — Ch7.** Memo wanted one sentence; draft deleted the whole closing note. Chapter still leans on asteroid-iron / Mars-water parameter ranges with no anchor against "these numbers are fantasy." **Restore a 1–3 sentence note/footnote.**

**B8. $70–80-cents B-is-large figure softened to "the large majority" — Ch4.** The chapter's single load-bearing quantification of the accountability bond, downgraded to a qualitative phrase. **Restore the concrete figure once the ~78% marginal-tax source is confirmed.**

### SEVERITY C — RELOCATED-BUT-NOT-LANDED. Value is in limbo; cannot certify "no loss" until destination chapters are verified to carry it.

**C1. Ch9 — ~3,600 words relocated, none confirmed landed.** This is the single biggest risk in the whole set:
- 2008-TARP-vs-Sweden-1932 case (~1,400w, Mian & Sufi, $11T/10M/$700B, Saltsjöbaden) → marked `[RELOCATE TO Ch5]`, NOT in Ch5.
- "What the eleven-cent difference buys" healthcare section (~1,300w, tax-wedge, medical-crowdfunding, "you already pay Swedish taxes") → intended Ch4, NO bracket left, NOT confirmed.
- Chattanooga/Mondragon/Vienna trio (~900w) → `[RELOCATE TO macro chapter]` with destination **undefined** and no one-clause stub left behind. These are the chapter's strongest "it works" demonstrations and its only human/values register.
- Christophers coda → `[RELOCATE TO Ch5]`, not landed.

**C2. Ch5 — 2008 four-objection rebuttal (~1,200w)** asserted to "live in the Technical Appendix," but that is a memo PROPOSAL, not a confirmed state. If the TA doesn't carry it, the adversarial depth is LOST, not moved. Verify the TA.

**C3. Ch7 / Ch8 — hard dependencies on Ch9 delivery.** Ch7's Pistor/immune-response answer and existential-substitutability payoff, plus Ch8's YIMBY steelman-rebuttal and the Public-Choice/Buchanan-disarming move + reparations roster, are all relocated to Ch9. Acceptable inside a book ONLY if Ch9 actually carries them. The YIMBY apparatus must travel with any Ch8-derived standalone essay.

**C4. Ch6 — reverse-direction Restitution roster** (Holocaust / 1988 Civil Liberties Act / Black Lung Trust Fund / South African TRC) compressed to "Darity and Mullen." Verify Ch5 carries the roster.

### SEVERITY D — VERIFICATION / FACT-CHECK gating (added value can itself introduce risk)

**D1. New Polanyi/Fraser/Harvey/Pistor/Darity characterizations across Ch5, Ch6, Ch7, Ch8, Ch9** must pass a Pass 3.1 fact-check. These are real authors with real positions; the no-invented-factual-claims rule applies to how their views are summarized, not just to invented biography.

**D2. Ch5 Sandel "the book engages it directly elsewhere" — DANGLING PROMISE.** Sandel/commodification appears in NO manuscript chapter (verified by grep). This is an unsupported claim about the book's own contents. Either confirm/create the owning chapter or soften the clause to "the framework's response here is..." Keep the paragraph; fix the promise.

**D3. Ch8 new "~50x triangulated central estimate"** is a keystone-adjacent figure NOT confirmed in the deep-pass §8 ledger audit. Verify against the Canonical Figure Ledger before ship.

**D4. Ch6 / Ch9 figure-fix dependencies.** Both reconcile to canonical $496 carbon / $510 total, which depends on Ch8 actually carrying those figures (memo §10 flag). Verify Ch8.

### SEVERITY E — DEFENSIBLE / AUTHOR-RATIFY-CONSCIOUSLY (memo-sanctioned trades, flagged so they aren't absorbed silently)

- Ch9 + Ch8 Public-Choice center-right think-tank courtship (AEI/Cato/Mercatus/GMU address-list) + FMLA worked example cut — a deliberate adversarial-audience positioning asset. Ratify consciously.
- Ch9 Nordic demographic-homogeneity steelman (3 specific pressure-test rebuttals) compressed to assertion — the original's self-described "strongest claim." For adversarial Tier-1 readers this is the most substantive argumentative thinning in Ch9.
- Ch6 Sen capability-valuation "how" function dropped (Parfit "whether" survives); Ch4 named-government-succession roster; Ch7 commute-lease arithmetic genericized; Ch8 "recognizably capitalist" closing beat.

---

## (3) CLEAN BASES vs RESTORATION vs RE-DRAFT

**No chapter needs a re-draft.** All seven are rated `yes-with-restorations`, and the adversarial reads agree: the spines survived, the case studies kept full empirical weight, and the additions are overwhelmingly memo-sanctioned and value-adding. Re-drafting would discard genuine net gains.

- **Cleanest base — Ch4.** Executed all cuts faithfully AND landed every high-value add (Hartwick/Hotelling/Daly naming, public-choice badging, Coase, falsifiability, the F-1 term-gloss). Nets richer than the original. Only 3 lost-value items, all narrow (one figure restoration + one relocation decision + sourcing). Closest to a clean base.

- **Strong bases needing targeted restoration — Ch7, Ch5, Ch6.** Ch7 is near net-gain (closes ~10 named-theorist gaps + repairs 2 objection seams); needs B7 + citation cleanup + Ch9 verification. Ch5 and Ch6 are high-quality compressions but each carries 2 genuine over-cuts (B1/D2 for Ch5; B2/B3 for Ch6) plus relocation verification.

- **Strong base but with the most over-cuts — Ch8.** Excellent adds, correct figure-fixes, but FOUR quiet over-cuts (B4/B5/B6 + 2008-beat) plus one unverified new figure (D3). Restore-heavy.

- **Highest relocation exposure — Ch9.** Excellent base for argument, but ~3,600w is excised-but-not-landed (C1). Cannot be certified until all four relocations land in live destinations. This is the chapter where the skeptic's worry is most justified: as a corpus, that value is currently in limbo.

- **The outlier — Ch2.** The ONE draft that arguably should be re-worked rather than lightly restored, but for the opposite reason: it FAILED to shrink (−1.1% vs ~−13% target). It took the two heaviest SAFE cuts but barely touched the prescribed §Numbers and pride-restatement consolidations, then added ~270w back. Net: it did not achieve its tightening objective AND it leaked the most scaffolding. Pure prose-value loss is low; the problem is it's dirtier and no shorter. Re-run the tightening pass, don't restart.

---

## (4) PATTERN — did the one-shot approach systematically drop a KIND of thing?

Yes. Three clear systematic patterns, in descending order of importance:

**PATTERN 1 (dominant): "Relocate" became "delete," because destinations were never executed.**
The single biggest systematic failure mode. Across Ch5, Ch6, Ch7, Ch8, Ch9, the one-shot confidently marked large blocks `[RELOCATE TO ChX]` and excised them — but the relocations are PROPOSALS, not executed moves. The drafts treat "I flagged it for Ch9" as equivalent to "the value is retained." It is not: until ChX is confirmed to carry it, the content is gone from the corpus. Ch9 (~3,600w) and Ch5 (~1,200w TA) are the acute cases. The model systematically under-weighted the difference between "excised here" and "landed there." **This is the pattern most likely to fool a skeptic doing a single-chapter read — the bracket reads like a safety net but isn't one until the cascade executes.**

**PATTERN 2: Over-cutting "redundant"-looking restatements that were actually load-bearing or were named differently by the memo.**
The one-shot repeatedly cut to ZERO what the memo said cut to ONE sentence: Ch8 Lewis/UMW (memo: one sentence → draft: zero), Ch7 delivery-cost note (memo: keep one sentence → draft: deleted whole), Ch5/Ch6 operational machinery (CIT sub-forms, bond-forward-posting link). The shared signature: the model treated *restatements and apparatus* as fungible redundancy and removed the last instance along with the redundant ones — erasing figures and concepts that appeared nowhere else (the 13-year gap; the "debt we pay" hinge; the forward-posting rationale). It optimized for "no repeated content" rather than "every load-bearing claim stated at least once."

**PATTERN 3: New theory-positioning adds are excellent but (a) re-inflate the chapters and (b) carry unverified author-characterization risk.**
The Polanyi/Fraser/Harvey/Pistor/Coase/Hotelling/Pigou/Daly/Weitzman/Sandel adds are the consistent BRIGHT SPOT — nearly every one closes a memo-flagged exposed flank at the exact point of contact. But they systematically (a) offset the cuts (Ch2 stayed flat partly because ~270w of adds replaced the cuts; Ch6/Ch9 grew their analytical-positioning load even while shrinking overall), and (b) introduce a NEW risk class — substantive characterizations of real scholars that must pass fact-check (D1). The one-shot is better at *adding* lit-positioning than at *tightening*, and it doesn't track that adds can themselves be liabilities under the no-invented-claims rule.

**What was NOT systematically dropped (reassuring for the skeptic):** scene-anchors, case-study empirical weight, the four spine moves, the killer lines, and emotional/values beats largely survived. The losses are concentrated in (1) relocated-but-unlanded blocks, (2) last-instance figures/concepts mistaken for redundancy, and (3) named non-US/historical exemplars (Niger Delta, Bismarck, the reverse-restitution roster) — i.e., the breadth-of-portability evidence, not the core argument.

**Bottom line for the author:** Your skepticism about Ch5/Ch6/Ch9 is justified but mis-aimed. The shrunk drafts did NOT gut the argument — they kept the spines and got richer in positioning. What they lost is (1) one or two load-bearing last-instances per chapter (restorable in sentences), and (2) a large amount of *relocated* value that is currently homeless because the destination cascades were never run. Don't re-draft. Do three things before using any of them: strip all scaffolding brackets (A1), restore the Severity-B last-instances, and EXECUTE-or-verify every relocation (C1–C4) — because "I'll move it to Ch9" is the load-bearing lie in this whole exercise.
