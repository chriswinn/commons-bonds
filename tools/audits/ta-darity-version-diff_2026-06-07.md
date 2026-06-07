# TA — Darity-version vs current diff (READ-ONLY analysis)

**Date:** 2026-06-07
**Session:** Session B (Darity version diff) of the TA rigor-audit resume plan.
**Branch:** `claude/ta-darity-diff-260607-a91c8f` (worktree off the held branch
`claude/ta-rigor-audit-260606-f537b4`). **No TA edits made — report only.**
**Status:** COMPLETE.

## Scope + method

Compare the version of the Technical Appendix sent to William Darity Jr. on
2026-05-14 against the current TA, and for each confirmed audit error
(`core/technical-appendix/TA-rigor-audit-ledger_2026-06-06.md`) determine
whether it was **present in Darity's version** or **introduced later**.

**Three text states extracted and compared:**

1. **Darity's actual deliverable** — `Technical_Appendix_Commons_Bonds_2026-05-14.docx`,
   extracted to plain text via `pandoc` (ground truth of what Darity received;
   the `.pdf` and `_with-citations_` variants carry the same body text).
2. **`cf24f57`** (2026-05-15) — the TA source just after the Darity send, used
   for provenance archaeology.
3. **`origin/main`** — canonical current repo state. *(The held branch's
   proposed audit fixes `cefe5e4..4521e28` are NOT on main and are NOT what
   Darity's copy should be compared against; they are the corrections under
   review. Comparisons below are Darity-DOCX vs `origin/main`.)*

### Provenance finding (DOCX archaeology) — resolved

The handoff warned the DOCX might be rendered from a pre-rename source. It is
not. **The Darity DOCX body text matches the `cf24f57`-era TA source exactly**
on every load-bearing marker checked: carbon term ($544), total-with-carbon
($552–566), 2.32 CO₂-intensity basis, the expanded "OSIRIS-REx → Bennu" row,
the Keck/Planetary-Resources/DSI commercial-mining table, and the full §11.10
space-economics block. The only DOCX-vs-`cf24f57` differences are cosmetic
table line-wrapping introduced by the DOCX renderer. **The DOCX is a faithful
ground-truth witness; treat `cf24f57` ≈ Darity's TA for content purposes.**

---

## (a) What materially changed between Darity's version and current

There are exactly **6 commits** touching the TA between `cf24f57` and
`origin/main`. Of these, **only one changed any number.** The complete
material change-set:

| Commit | Date | Class | What it did to the TA |
|---|---|---|---|
| `a1e54d9` | 2026-05-17 | prose | Added a "Scope: complementarity with Public Choice / rent-seeking analysis" paragraph (§1.x). No numbers. |
| `dd825f2` | 2026-05-21 | structural | Added an HTML anchor `id="sec-11-11-ipg-reconciliation"` to the §11.11 header. No content change. (The §11.11 reconciliation section itself was already in Darity's copy.) |
| **`914addc`** | **2026-05-23** | **NUMERIC** | **The Coal-CO₂ methodology cascade — the only numeric change, and the source of every introduced error. See below.** |
| `8aa7dfb` | 2026-05-25 | citation | Removed an interview "(Darity 2026)" parenthetical. No numbers. |
| `06eb1ea` | 2026-05-25 | citation | Removed an interview "(Darity 2026)" parenthetical. No numbers. |
| `389b773` | 2026-06-04 | citation | Deleted all interview citations: removed the "Darity (2026) did not view the framework's calculations … as underestimating" sentence from the Darity-Mullen para; removed the bibliography entry "Darity … Interview by Christopher Winn. May 13, 2026. Recording on file with author." |

### The one numeric change: `914addc` (Coal-CO₂ cascade, 2026-05-23)

This commit re-based the McDowell carbon accounting from the
**national-bituminous-average basis (2.32 mt CO₂/short ton)** to a
**McDowell-specific Pocahontas-seam basis (2.61 mt CO₂/short ton, ~28 mmBtu/short
ton)**. It cascaded through §11.1 and §11.6:

| Quantity | Darity's version | Current (`origin/main`) |
|---|---|---|
| CO₂ intensity | ~2.32 mt/short ton | ~2.61 mt/short ton |
| §11.1 carbon term | **~$544/ton** | **~$510/ton** |
| §11.1 total with carbon | **$552–566/ton** | **$518–532/ton** |
| §14.7 "absorbed $___ for every $4.50" | $552 | at least $518 |
| Cumulative CO₂ from McDowell | 1.4B (1.39B) tons | 1.6B (1.57B) mt |
| §11.6 atmospheric replacement cost (conservative) | $836B–$1.39T | $942B–$1.57T |
| §11.6 Habitability-only per-ton (conservative DAC) | **$1,392–$2,320/ton** | **$1,566–$2,610/ton** |
| §11.6 Habitability-only (at-scale / optimistic) | $696–1,392 / $232–696 | $783–1,566 / $261–783 |
| Ch 6 framework-introduction figure (referenced) | $550–570/ton | $449–464/ton |

Everything else in the TA is byte-for-byte identical between Darity's copy and
`origin/main` except the prose/citation edits in the table above.

---

## (b) Per-error provenance: present in Darity vs introduced later

**Headline: of the ~45 distinct confirmed audit findings, only the carbon
cascade cluster was introduced after the Darity send. Every other confirmed
error was already present in the copy Darity received.**

### INTRODUCED LATER (by `914addc`, 2026-05-23 — NOT in Darity's copy)

| Ledger | Error (as audited, current state) | Darity's copy instead had | Verdict |
|---|---|---|---|
| **A1** | §11.1 carbon "$510" (should be $496 = 2.61×190) | **$544** (a *different* wrong number) | The specific "$510" error is post-send. ⚠ |
| **A1 cascade** | total $518–532; "$510/ton carbon term"; §14.7 "$518" | $552–566; "$544/ton"; $552 | post-send |
| **A4** | §11.6 combined Method-1 anchor ($1,421–2,412) **< its own Habitability-only component** ($1,566–2,610) | combined $1,421–2,412 **≥** component $1,392–2,320 (consistent: $1,392+12+17 = $1,421; $2,320+50+42 = $2,412, exactly) | **INTRODUCED.** `914addc` bumped the component but left the combined anchor untouched, breaking a relationship that was internally consistent in Darity's copy. |

**A4 is the cleanest illustration of the author's "out-of-context sessions
introduce errors" concern.** The 2026-05-23 cascade session updated the
Habitability-only DAC derivation (2.32 → 2.61 basis) but did not propagate the
change into the combined Method-1 anchor 18 lines below, manufacturing an
arithmetic contradiction (a combined floor lower than one of its addends) that
did not exist in the version Darity reviewed.

### PRESENT in Darity's copy (pre-existing; unchanged through to current)

All of the following are byte-identical in Darity's DOCX and `origin/main`:

| Ledger | Error | Confirmed in Darity DOCX |
|---|---|---|
| A2 | §11.1 IPG "33–122× (without carbon)" label backwards | yes — identical line |
| A3 | §11.5 Norway CS-reduction "~84%" (should be ~16%) | yes — "Norway's CS-reduction is ~84% (1 − $48/$300)" |
| A5 | §11.2 Deepwater IPG 15–17× + component-sum > stated total (n21) | yes — rev ~$1.1B, costs $20–30B (components sum $30.7–34.7B), IPG 15–17×. *(NB the audit's "→18–27×" was later ruled a false positive; keep 15–17×.)* |
| A6 | §11.8 scarcity_multiplier "≈6–7 via log(1+200..500)" (should be 1.27–1.31) | yes — and already inconsistent in Darity with its own worked examples that use 1.27 |
| A7 | §11.9 intro DAC bands $600–1,200 / $150–500 / $100–200 | yes — identical |
| A8 | §11.10 Falcon 9 ~$2,700/kg (should be ~$2,939) | yes — "~$2,700/kg … $67M/22.8t" |
| A9 | §3.4/§3.6 Norway vintage 50B BOE / $50/BOE vs §11.5's 55B / $48 | yes — both vintages present, same split |
| A10 | §11.5 M1 table cell $300–650 vs derived $161–422 | yes — Norway-oil M1 cell $300–650 |
| A11 | §11.6 M2 industry-paid $8–15, societally-paid $50–88 | yes — identical |
| A12 | §3.6 McDowell M1 band $310–1,800 vs §11.6 derived band | yes — "Appalachian $310–$1,800/ton" |
| A13 | §11.8 V_option $500–2,000 vs §11.6 canonical $50–500 | yes — §11.8 "$500–$2,000/ton"; §11.6 "$50–500/ton" (same internal split) |
| A14 | §11.10 commercial cost $1–100/gram + "5–7 orders" unit/scale | yes — identical framing |
| (Keck) | §11.10 Keck "7-ton asteroid … ~$370,000/kg" (diameter-vs-mass mis-transcription per `ta-11.10-space-economics-sourcing_2026-06-07.md`) | yes — "~$2.6B for retrieval of a 7-ton asteroid … (~$370,000/kg retrieved)" |
| (PR) | §11.10 Planetary Resources "$50–500/kg" (unverifiable) | yes — identical |
| B1/B2 | Theorem 10.1b proof restates premise / "any jurisdiction" scope | yes — Theorem 10.1b + proof present |
| B4 | §16.1 declining-rate form r₀·e^−δt + r_min (gives r(0)=r₀+r_min) | yes — "r(t) = r₀ · e−δt + r_min" |
| D3 | §14.6 Daly inversion (S_max = 1 attributed to Daly) | yes — §14.6 present |
| D4 | §3.5 "Solow 1956 QJE" misattribution (should be 1974 RES) | yes — "Solow 1956 Quarterly" present |
| E13 | §11.1 reclamation shortfall $3.7B vs §11.6 $4B | yes — "$3.7–$6B reclamation shortfall" |
| E15 | §11.1 population endpoint 18,000 vs ~19,000 elsewhere | yes — both "18,000" and "19,000" present in Darity (same internal inconsistency) |

The remaining ledger items (B3, B5–B7, C1–C8, D1–D2, D5, E1–E12, E14) are all
structural / notational / citation issues in long-standing apparatus untouched
by any of the 6 post-send commits; spot-checks (B4, D3, D4, E13, E15, A12)
confirm the pattern, and the complete `cf24f57..origin/main` TA diff shows no
edits to those sections. **They are present in Darity's copy.**

---

## (c) Errors unique to one version

**Unique to Darity's copy (corrected or removed since):**

1. **§11.1 carbon "$544/ton" does not reproduce from its own stated basis.**
   Darity's copy states intensity 2.32 mt/short ton and SCC $190, but
   2.32 × 190 = **$440.8**, not $544 (the $544 implies ~2.86 mt/short ton — a
   stale higher-intensity legacy value). So Darity's §11.1 carbon term was
   *internally inconsistent* with both its own stated intensity and its own
   §11.6 derivation (which correctly used 2.32 → $1,392–2,320). `914addc`
   replaced this with the 2.61-basis $510 — which *also* fails to reproduce
   ($2.61 × 190 = $496, audit error A1), so the term has been arithmetically
   wrong in both versions, but the wrong number differs ($544 → $510).
   Corollary totals $552–566 are likewise unique to Darity.

2. **Interview citations present in Darity's copy, removed since:** the
   "(Darity 2026)" parentheticals (coercion-vector boundary, stratification-
   economics, Parfit/Sen, coercion-vector list item), the "Darity (2026) did
   not view the framework's calculations … as underestimating" sentence, and
   the bibliography entry "Darity … Interview by Christopher Winn. May 13,
   2026." These are *content* differences, not errors.

**Unique to current (introduced since the send):** the carbon-cascade cluster
in (b) above (A1's $510 / $518–532 / 2.61 basis / 1.57B mt / $1,566–2,610
component, and the A4 combined-anchor contradiction) — plus the additive
Public Choice paragraph (`a1e54d9`).

---

## Bottom line + implications for a Darity correction

1. **The version Darity holds is, on the carbon question, *less broken in one
   way and equally broken in another* than the current main.** His §11.1
   carbon was internally inconsistent ($544 vs its 2.32 basis) but his §11.6
   Method-1 chain was *self-consistent* (component ≤ combined). The post-send
   cascade fixed the basis-consistency at §11.1 while (a) carrying a fresh
   arithmetic slip ($510 ≠ $496) and (b) breaking the §11.6 combined anchor
   (A4). This is a concrete instance of the failure class — a partial cascade
   by an out-of-context session — that the prompt flags.

2. **For the corrections-to-Darity decision:** essentially the *entire*
   confirmed-error ledger (A2, A3, A5-domain, A6–A14, Keck, PR, B/C/D/E series)
   was already in the copy Darity received. Whatever correction note is sent to
   him should therefore be scoped to **the full ratified fix set**, not just
   the carbon cluster. The carbon-specific wrinkle to disclose accurately:
   *his* copy shows $544 / $552–566 / 2.32-basis; the corrected target is
   $496 / $504–518 on the McDowell-specific 2.61 basis (per held-branch fix
   `cefe5e4`), with the §11.6 combined anchor repaired to $1,595–2,702 (fix
   `23ec2e7`).

3. **Do not describe the carbon error to Darity as "we wrote $510 instead of
   $496."** Darity never saw $510. His copy said $544. The honest framing is:
   "the carbon term and the McDowell Method-1 chain were both re-based and
   corrected after we sent your copy; the figures you have are superseded."

4. **Session F (CSD reverse model) addition stands unaffected** — Darity's copy
   had no reverse model; that is an addition to offer, independent of this diff.

### Verification artifacts
- Darity DOCX text: extracted via `pandoc -f docx -t plain` (provenance matched to `cf24f57`).
- Complete change-set: `git diff cf24f57 origin/main -- core/technical-appendix/TechnicalAppendix_v2.0.0.html` (63 content lines; 1 numeric commit).
- Per-commit TA stats: `a1e54d9` +6 (prose), `dd825f2` ±1 (anchor), `914addc` ±42 (carbon), `8aa7dfb`/`06eb1ea` ±2 each (citations), `389b773` −13/+? (citation deletion).
