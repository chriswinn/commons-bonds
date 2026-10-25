# Rigor pipeline — value review

**Date drafted:** 2026-10-25 · **Date modified:** 2026-10-25 (v1.0.1: author correction. The chapter loop of full redraft → hand redline → grammar polish is the proven core and is kept whole; §2G and §3 rewritten) · **Status:** RATIFIED 2026-10-25 (author approval in session)
**Suggested repo home:** `tools/pipeline-doctrine/` (if ratified, the amendment cascades to all three doctrine homes per the three-home rule)
**Question:** Is the v3.1 pipeline worth its cost going forward, given 1–2 hours a week of author time? That pipeline is Stages 0–5: fact-check, voice polish, simulated audience panels, adversarial readers, developmental edit, render and sign-off, plus multi-variant blind redrafts with judges.

---

## 1. What it cost

Word counts of the artifacts on disk stand in for effort, because this clone's git history is shallow (50 commits) and doesn't allow a time-based measure.

| Measure | Value |
|---|---|
| Essay prose, 9 packages | ~51,000 words |
| Rigor artifacts inside those essay packages | ~1,190,000 words (**~23 words of review per word of essay**) |
| Further rigor artifacts in `tools/rigor-passes/` | ~1,240,000 words |
| All of `tools/` (doctrine, handoffs, audits, rigor) | ~2,020,000 words |
| Book chapters | ~92,000 words |
| Rigor files per essay | 14 to 32 (Harper's: 27 files, 230k words, for a 7,200-word essay) |

**Outcome so far:** 3 submissions. Two were declined with no feedback (Boston Review, Phenomenal World), and the American Prospect is presumed passed. Both declined essays had cleared every pass, including the simulated reader panels. Eight pieces are signed off but unsent, and several of them are each waiting on a redraft verdict for you to ratify.

**The constraint was never quality. It was getting things out the door.** The process created more decisions for you than you had time to make.

---

## 2. Layer-by-layer verdict

### A. Automated gates — invariant scan, prose-clarity check, link check, render check
- **Cost:** near zero. Runs on commit, with no author time.
- **Evidence of value:** catches scaffolding leaks, retired terms, em-dash density and render glyphs. The June TA sweep added 21 patterns, and HIGH has stayed at 0 since.
- **Gap found today:** the 1960 coal price was amended from $4.50 to **$4.71** (EIA Total Energy Table 7.9; author-ratified 2026-06-04). **No gate pattern was added**, so the old figure survives in live prose:
  - the *Pricing Honestly* essay (lines 14, 106);
  - Ch 9 (line 12);
  - Ch 6 (lines 44, 80, 173).

  An expensive manual sweep ran but missed these. A one-line pattern would have caught them on every commit.
- **Noise:** the scan flags the ordinary English word "ratified" in the Foreign Affairs essay ("Norwegian voters... ratified the choice") as scaffolding. That's a false positive.
- **Verdict: KEEP and strengthen.** This is the highest-value, lowest-cost layer.

### B. Fact-check (Pass 3.1) and the canonical figure ledger
- **Evidence of value:** this pass caught real errors that would have damaged your reputation:
  - an **invented biography for a real miner** (Bailey; Harper's F-3.1-H1);
  - a Norway fiscal-rule date error that showed up in **three separate essays**;
  - a living scholar's profession misstated (Mullen);
  - a Tangier erosion figure taken from the press rather than the paper;
  - the false "neither addressed" positioning claim in Ch 6, plus the B<RCV overclaim.
- **The catch behind the catch:** many of these errors were **introduced by AI drafting**. Each blind redraft re-derives facts and drifts. So part of what this pass catches is damage the redraft process itself creates.
- **Verdict: KEEP. It's mandatory for anything publisher-facing.** Make it cheaper by checking every draft against the ledger, and by encoding every ledger amendment as a gate pattern in the same commit.

### C. External positioning verification (the Ostrom, Polanyi/Fraser and novelty runs)
- **Evidence of value:** real sources, real prior art, and a real verdict: novelty holds, with 3 narrowings and a list of works to cite and distinguish. That protects the book from the most damaging review an agent or academic could write.
- **Verdict: KEEP** for book-level claims. It's a one-time cost per claim.

### D. Voice polish (Pass 3.2)
- **Evidence:** useful early on. It took meta-commentary tics from 7 to 0 and halved em-dash density. Most of its mechanical findings are now gate patterns, and the rest overlaps with your redline.
- **Verdict: MERGE.** The mechanical part goes to the gate; voice judgment is your redline, which the doctrine already says is the final stage.

### E. Simulated reader panels: acceptance (Pass 3.3) and adversarial (Pass 3.4)
- **Evidence for:** the adversarial readers surfaced a few real threads: the Public Choice rent-seeking objection in Ch 1, and the case for an explicit non-partisan framing move ($100 Barrel).
- **Evidence against:**
  - **They don't predict editors.** Both declined essays passed broadly (e.g. 16/16 INCLUDE patterns).
  - **The panel's overall verdict was wrong** in the Aeon case until Amendment D reweighted it. The method needed a fix to correct its own conclusion.
  - **The Aeon pitch test:** careful iteration beat the full discipline.
  - **Correlated blind spots.** The simulated readers are generated by the same model that drafted the text. An imagined reader is a guess about a reader, not a reader.
  - **Cost multipliers:** repeated re-audits, convergence runs (N=2 and N=3) and bundled re-fires.
- **Verdict:**
  - **DROP the acceptance panels (3.3).**
  - **Keep one adversarial pass (3.4) as a single "strongest critic" read:** 3–4 sharp critics (domain expert, ideological opponent, skeptical editor), run **once per chapter or essay**, never on spot-fixes, and never as convergence runs.
  - **Get real readers where you can:** agents' and editors' responses, and one or two trusted human readers for the samples.

### F. Developmental edit (Pass 3.5)
- **Evidence:** it found real structural gaps, such as missing scenes and abrupt pivots. But in Harper's, 4 of the 6 restorations needed material only you have, so they stalled.
- **Verdict: OPTIONAL, for book chapters only.** Run it once before your redline, and phrase its output as questions to you rather than drafted fixes.

### G. Full chapter redraft → author line-by-line redline → Claude grammar and punctuation polish
- **Author evidence (2026-10-25):** this loop was tested specifically to clear stale figures (e.g. $4.71), fold in new material, and fix clunky grammar. **It overwhelmingly produced the best work.** Ch 1 is the finished example: whole-cloth redraft, then your redline, then a mechanical pass. It is ready to ship, and later fresh variants judged against it did not beat it (bake-off verdict KEEP-CANONICAL).
- **Why it works:** the redraft does the heavy structural and figure work. Your hand redline supplies the voice and judgment no simulated reader can. The polish is purely mechanical. Each step does one job.
- **What actually caused churn was the material around this loop, not the loop itself:**
  - simulated panels and repeat runs stacked on top of it;
  - **redrafts that were never followed by your redline**, so they sat waiting on ratification;
  - re-redrafting essays after they were signed off;
  - redrafts not checked against the figure ledger, which brought back old errors.
- **Verdict: KEEP. This is the core of the chapter pipeline.** Every chapter goes through the full loop once. Chapter 1 is done. Chapters 2, 3, 4 and 10 are redrafted and waiting on your redline. Chapters 5–9 still need the redraft. Run 2 variants plus the current version as a third candidate, so a redraft can't make a strong chapter weaker. Every redraft gets the fact-check against the ledger before it reaches you. For essays, the same loop applies once; don't start a second round without a trigger (a rejection with feedback, a retired figure, or a venue change).

### H. Stage 4 render, Stage 5 sign-off, pre-publication review queue
- **Verdict: KEEP render** (automated). **Keep the pre-pub review queue for the book proposal**: it's an honest, distinctive signal to agents. For essays, reduce Stage 5 to a 10-line checklist.

---

## 3. Proposed lean pipeline (replaces v3.1 for new work)

| Step | When | Author time |
|---|---|---|
| 1. **Full redraft from an updated brief** (chapters: 2 variants plus the current version, judged) | Once per chapter; for essays, at first draft or on a real trigger | ~1 hr to pick the winner |
| 2. **Automated gates** (with every ledger amendment encoded as a pattern in the same commit) | Every commit | 0 |
| 3. **Fact-check against the ledger and sources**, plus the no-invented-facts rule | Every redraft, before it reaches you | Decisions on HIGH findings only |
| 4. **One strongest-critic read** (3–4 adversarial readers, one run) | Once, before your redline | ~15 min to read the summary |
| 5. *(Chapters, optional)* **Developmental read** framed as questions | Once, before your redline | ~15 min |
| 6. **Your line-by-line redline by hand** (final voice) | Once | the real work |
| 7. **Claude grammar and punctuation polish**: mechanical only, no rewording; every change listed for you | Right after your redline | ~10 min to skim the change list |
| 8. **Render and checklist** | At submission | ~10 min |

**Retired:** acceptance panels, convergence and repeat runs, re-firing passes after spot-fixes, and redrafting signed-off essays without a trigger.

**Expected effect:** roughly a 70–80% cut in review overhead per piece. Your time goes to decisions and redlines, which only you can do. The two layers that caught the errors that mattered (fact-check and positioning verification) stay intact.

---

## 4. Immediate actions if ratified

1. **Add `$4.50`, "four dollars and fifty cents" and "about $4.5" as HIGH regressed patterns** (allowlisted in archive files). Then fix *Pricing Honestly* lines 14 and 106 to $4.71 / "just under five dollars". **The number is already ratified; only the propagation was missing.** Ch 6 and Ch 9 get the figure in their rebuilds.
2. **Audit the ledger** for any other amendment that never got a gate pattern. One session, with no author time needed.
3. **Fix the "ratified" false positive** by excluding plain English uses in essay prose.
4. **Run Ch 5 through the proven loop:** 2 redraft variants plus the current version → judge → fact-check → one strongest-critic read → developmental read as questions → **your hand redline** → grammar and punctuation polish.
5. **Cascade the amendment** to the three doctrine homes, in one session.

## 5. Limits of this review

- Effort is measured by artifact size, not hours or tokens.
- Three submissions is a small sample. "The panels didn't predict editors" is suggestive, not proof, since editors decline good work for many reasons.
- The review was written by the same kind of model that ran the panels. Weigh the critique of simulated readers accordingly; the remedy it proposes is real readers.
