# Ch 1 + Ch 3 — redline-prep readiness report (2026-06-19)

**Session:** dedicated REDLINE-PREP for Chapter 1 + Chapter 3 only.
**Branch:** `claude/ch1-ch3-redline-prep-260619-2e62ec` (isolated worktree, branched from newest `origin/main` @ `ddc2e36b`).
**Purpose:** stage both chapters clean for the author's single final human redline. PREP only — no creative redline performed; all prose left exactly as on main. Recommendations below are *recommend-not-impose* per author-redline-is-final discipline.
**Scope guard honored:** touched only the two chapter files (read-only) + this report. No other chapter, no TA, no essays/op-eds/proposal. No matrix insertions or rebuilds (those are owned by `claude/book-drafting-plan-260618-88009b`).

---

## Chapter 1 — *The Quiet Math* — READY-TO-SHIP, CONFIRMED CLEAN

**Verdict: redline-ready.** No rewriting needed. The chapter is the author-redlined, READY-TO-SHIP text (per STATE.md, 2026-06-11) and reads as such.

- **Corpus-invariant gate:** CLEAN. `check-corpus-invariants.sh --scope …Chapter__1… --severity ALL` → "CLEAN BASELINE — no matches across 116 patterns × 1 file", exit 0. (HIGH+MEDIUM also empty.)
- **Em-dash render gate:** 0 em-dash characters. ✓
- **ADDED beats:** none (correct — no matrix finding touches Ch 1).
- **Prose snags:** none surfaced. The prose is clean and in the author's voice; contractions intact; no grammar/flow stumbles flagged. (Per discipline, I did not manufacture snags in author-redlined prose.)

**One staged pre-submission dependency (not a prose issue):**
- **L120 citation-pin** — the inline HTML comment at the top-1–2% household-income sentence is a deliberate *endnote-time* citation pin (Census CPS ASEC / CBO household-income percentile thresholds for the 2017–2018 peak years), kept as a hedged percentile range, not a dollar figure, per the 2026-06-11 author register call. It renders invisibly and does not trip the gate. **Action owner: endnote assembly (pre-submission), not this redline.** Flagging only so it is not forgotten when Ch 1 goes into the Wave-1 sample package.

---

## Chapter 3 — *The Waterman* — STAGED FOR REDLINE; per-beat flow verdicts below

**Verdict: redline-ready.** Full promoted assembly intact (Option B, NOT the compressed redo2-A). Priced Restitution-Bond reef section (GATE 2) present and intact. All four matrix-v2 ADDED beats read in-flow; one carries a minor optional smoothing the author may want to consider. The `<!-- ADDED 2026-06-17 … -->` markers are LEFT IN PLACE so the author can see the new beats during the redline — strip them only after the author ratifies the flow.

- **Corpus-invariant gate:** CLEAN. Same command, Ch 3 path → "CLEAN BASELINE — no matches across 116 patterns × 1 file", exit 0 (15 frontmatter/comment lines correctly skipped). HIGH+MEDIUM empty.
- **Em-dash render gate:** 0 em-dash characters. ✓
- **Do-not-regress flags — all verified:**
  - Tangier erosion = **Option A** (plain sourced): "nearly two feet a year on the long-term average" + "a bit over a square mile" (L177). The banned press "15 ft/yr" shock figure is **absent**. ✓
  - Full promoted assembly preserved (compressed redo2-A NOT promoted). ✓
  - Priced reef section / GATE 2 intact: Restitution Bond named (L228), $20–37M floor (L236), $211M robust center subordinated (L238), $92M MD / $115M Bay-wide public itemization (L252). ✓
  - Harvey **magnitude relation NOT duplicated** here — only the concept-name *accumulation by dispossession* appears (L247, exactly once); the magnitude relation correctly stays in Ch 9. ✓

### Per-beat flow verdicts (the four ADDED matrix-v2 beats)

**Beat 1 — Ostrom at the renewable boundary (L55–57).** Verdict: **reads in-flow.**
Lands right after the coal-seam-vs-living-reef contrast and the "rate of taking exceeds the rate of making" paragraph; picks up "renewal" and the verbatim phrase "written off as a cost of doing business" from L53, and the following "Nobody marks the day this happens" (L59) still has a clean antecedent (the boundary being crossed). Well-bridged both directions.
- *Optional smoothing (author's call):* the appositive "the fisheries and forests and irrigation systems communities governed themselves" reads slightly compressed — a reader can stumble on the missing relative pronoun. The author may prefer "…the fisheries and forests and irrigation systems that communities governed for themselves." Minor.
- *Optional:* "written off as a cost of doing business" repeats L53 verbatim two paragraphs up. It functions as a deliberate callback, but if it reads as an echo-too-soon the author may vary one instance.

**Beat 3 — Hardin contradiction at the moratorium (L90–92).** Verdict: **reads in-flow; no smoothing needed.**
Best-placed of the four. Lands after the "moratorium worked / fishery restored by 1995" paragraph and before "That recovery is part of why what is happening now is hard." The beat closes on "the recovered fishery is the proof," which dovetails directly into the next paragraph's opening "That recovery." The argumentative-aside register ("It is worth naming what the moratorium disproves") is consistent with the chapter's established voice ("This chapter is about what those books are not allowed to record"; "Structurally, this is an interesting case"). Hardin summary is accurate; this is the only place he is named, and the moratorium is the chapter's clearest self-governance success — apt anchor.

**Beat 4 — Mazzucato/Harvey "gives it a number" (L246–248).** Verdict: **reads mostly in-flow; carries the chapter's one real seam-risk — recommend the author look here first.**
Strongly anchored ("what this reef shows…", "the column above") to the immediately preceding three-numbers payoff. Mazzucato (create vs capture value) and Harvey (accumulation by dispossession) are the right lineage to attach to the priced column. Harvey magnitude relation correctly NOT duplicated.
- *Optional smoothing #1 (the seam):* the beat restates the pattern as "value created in the water, value captured at distant tables, and a cost left in the mud that no one captured at all" — a three-part move that closely echoes the *immediately preceding* paragraph's "Value goes up and out. Cost stays and settles down." Two consecutive paragraphs landing the same three-part restatement is the one spot a reader may feel a redundancy. The author may want to vary or tighten the Mazzucato restatement so it adds the *names/lineage* without re-walking the three numbers.
- *Optional smoothing #2:* the compound "gave the taking-by-foreclosure-rather-than-by-making its name, accumulation by dispossession" is dense to read. With em-dashes off (render gate), a colon reads cleaner, e.g.: "David Harvey gave it a name, accumulation by dispossession: taking by foreclosure rather than by making." Author's call.

**Beat 2 — reparations-economics lineage (L258–260).** Verdict: **reads in-flow; coercion-distance discipline correctly observed.**
Well-bridged: L256 ends on "asks the parties who drew it down… to fund the rebuilding" (naming who owes), and the beat opens "naming who owes the bill is not one I invented" — clean lexical hand-off; then L262 returns to the floor figure. Credits the field (Darity, Mullen, Coates) and **prices no coercion**, explicitly "keeping the distance between a reef and what they price exactly as wide as it is" — consistent with the first-person coercion-abstention discipline and with Ch 1's "a commute and a stolen life do not belong on the same line." Substantively safe.
- *Author-judgment flag (not a fix):* the beat calls the subject of reparations "a different and a graver commons." Framing enslavement / the reparations subject as "a commons" is a deliberate, slightly bold extension of the book's key term. The next clause keeps the distance, so it is defensible, but whether "commons" is the right word there (vs. "a graver injury/injustice") is a register call only the author should make. Worth a deliberate look during the redline.

### Ch 3 — strip-after-ratification reminder
Once the author ratifies the flow of each beat, strip its `<!-- ADDED 2026-06-17 BEGIN … -->` / `<!-- ADDED 2026-06-17 END … -->` marker pair (and update the line-1 STATUS comment's "matrix v2 fills added … as ADDED marked beats" note to reflect that the markers are cleared). Until then they stay in so the author can see the new beats.

---

## State / merge

- **No STATE.md transition made.** Neither chapter changes status value: Ch 1 remains READY-TO-SHIP; Ch 3 remains PROMOTED / awaiting author redline. "Redline-prep staged" is captured by this report, not a new status marker. The dense aggregate Chapters row in STATE.md is owned by the PM / book-drafting sessions; this prep session does not mutate it (live-session ownership boundary, MAP.md §Live-session ownership).
- **No prose merged.** Both chapter files are byte-identical to `origin/main`; nothing of the author's to merge. This report (internal scaffolding) is committed to the feature branch and left there for the author's redline pass per the "PREP + stage, do not finalize" instruction.
- **After the author's final redline + ratification:** the ratified chapter commit merges to `origin/main` via the pre-push reconciliation pattern (`git fetch origin main` + rebase, then push). Never force-push main; never skip hooks.

## Commands run (reproducible)
```
bash tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/Chapter__1_TheQuietMath.md --severity HIGH+MEDIUM --no-fail   # clean, exit 0
bash tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/Chapter__3_TheWaterman.md --severity HIGH+MEDIUM --no-fail    # clean, exit 0
grep -c $'—' …Chapter__1….md   # 0
grep -c $'—' …Chapter__3….md   # 0
# Tangier Option A present / 15ft absent; reef GATE-2 markers present; ADDED beats 4-paired; Harvey concept-name x1, no magnitude dup — all verified
```
