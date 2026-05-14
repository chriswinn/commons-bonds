# Rigor Pass — Ch 3 "The Waterman" Stage-3 Pass 1 (Fact-Check)

**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A — Ch 3
**Date:** 2026-05-12 (audit + ratification); artifact filed retroactively 2026-05-13.
**Scope:** Pass 1 of the v2.0 three-pass discipline (fact-check only). Pass 2 (voice-polish) and Pass 3 (audience-load) deferred to subsequent fires per author's per-prompt scoping.
**Mode:** Audit-existing-prose (no Stage 1 brief; per Stage-3 template §"Audit-existing-prose mode", the existing prose is treated as canonical for memoir-register first-person claims; Pass 1 verifies externally-verifiable claims + cross-chapter / cross-artifact consistency).
**Status:** **RATIFIED 2026-05-12.** F-1 (Norway fund age) + F-3 (Colden public-record exception — naming swap + memory refinement) applied (Phase A + Phase C, same-session via author "ratify" trigger; commit `2f76e37` on `main`). F-2 (crab "sixth consecutive year" tightening) declined as defensible per author. Memory `feedback_named_subject_consent.md` updated with public-record exception (ratified 2026-05-12, landed in same commit). Two pre-staged downstream artifacts produced 2026-05-13 as carries from this audit: Colden pre-publication citation-verification packet (commit `15c6b0f`) + Biggie family courtesy-notification process guide (commit `164b9e2`).

---

## Source artifacts read

1. `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` (9,577 words / 228 lines pre-audit; 8 lines net delta post-ratification per commit `2f76e37`)
2. `manuscript/chapters/Chapter__3___GuidanceDoc.md` (internal scaffolding — not load-bearing for this Pass 1)
3. `research/literature/bibliography.md` §19.5 "Chesapeake fieldwork — interview-prospect public record"
4. `research/case-studies/chesapeake-fisheries.md` (boundary-test case placeholder; oyster collapse numbers ground-truth)
5. `research/case-studies/norway-swf.md` (Norway fund architecture — fund-age ground-truth)
6. `research/outreach/subjects/colden/background-brief_2026-05-08.md` (FPD-9 third instance; substitution-hypothesis CONFIRMED per commit `0e83dc5`; 26-quote register)
7. `research/outreach/subjects/moore/background-brief_2026-05-08.md` (FPD-9 fourth instance; substitution-hypothesis CONFIRMED per commit `c352d9a`)
8. `research/outreach/subjects/phat/consent-process-guide_2026-05-10.md` (Phat consent-status verification)
9. `research/outreach/subjects/phat/phat-mentions-inventory_2026-05-10.md` (Phat consent-state edit recipe)
10. `research/story-drafts/ch3_fox-hill-watermen-biggie-phats_2026-05-09.md` (author primary-source recollection — Biggie, Phat, Fox Hill, chop physics, mutual-aid 3am scene)
11. `tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` (workstream brief; Ch 3 emphases)
12. Commit log: `b5692f1` (Ch 3 Fox Hill / Biggie / Phat integration + VMRC date correction); `0e83dc5` (Colden FPD-9 substitution-hypothesis CONFIRMED); `c352d9a` (Moore FPD-9)
13. Memory: `feedback_named_subject_consent.md` (named-subject consent discipline — three paths)
14. Memory: `feedback_verify_stale_memory_claims.md` (staleness discipline applied to time-sensitive claims)
15. Memory: `project_book1_state_2026-05-10.md` (Book 1 work threads + status)

---

## §1. Externally-verifiable claims (audit-existing-prose Pass 1 scope)

For each claim below: chapter line + chapter text + canonical truth + severity + recommended spot-fix.

### §1.1 Findings — HIGH severity

*None.*

### §1.2 Findings — MEDIUM severity

#### F-1 — Norway fund "kept intact for fifty years" overstates fund age

**Line 210 (chapter, pre-fix):**
> "They have, against more pressure than is usually acknowledged, kept the fund intact for fifty years."

**Line 214 (chapter, pre-fix):**
> "The alternative is possible. They have done it. They have been doing it for half a century."

**Canonical truth.** Per `research/case-studies/norway-swf.md`: the Government Pension Fund Global (formerly the Government Petroleum Fund) was established in **1990** — 36 years to 2026, not 50. The chapter's "fifty years" framing conflates the 1970s-rules-architecture period (the White Paper, the early decision not to spend the money) with the fund's own institutional age. The two surrounding sentences in the chapter make "the fund" the explicit noun ("They set up a fund. They imposed limits... They have... kept the fund intact for fifty years.") — so the count is bound to the fund itself, not the broader institutional architecture.

**Severity:** MEDIUM. Numeric claim off by ~14 years. A trade-press fact-checker pencil would flag immediately. Not a structural risk to the chapter's argument (the Norway-as-existence-proof framing survives at 36 years just as well as at 50), but the kind of round-number drift that erodes trust if uncaught.

**Recommended spot-fix (ratified 2026-05-12, applied same-session via commit `2f76e37`):**
- Line 210: "kept the fund intact for fifty years" → **"kept the fund intact for more than thirty years"**
- Line 214: "They have been doing it for half a century" → **"They have been doing it for more than three decades"**

Anchor to fund (not architecture) preserves the noun across both sentences; "more than thirty years" / "more than three decades" varied phrasing preserves the rhetorical doubling of the original; both are conservative against the fund's actual age (36 years).

#### F-3 — Colden anonymization mis-applied the named-subject-consent discipline

**Lines 75, 93, 109, 172, 174, 178 (chapter, pre-fix):** Colden is rendered anonymously throughout — "*a scientist with the Chesapeake Bay Foundation*" (first use); "*the same Bay Foundation scientist*" / "*the same scientist*" (subsequent uses). Two HTML comments flag the anonymization as v1-from-public-record-pending-Colden-interview (lines 57 + 74).

**Canonical truth surfaced during audit.** All twelve verbatim Colden quotes in Ch 3 verified against `research/outreach/subjects/colden/background-brief_2026-05-08.md` §9. All quotes are from **public-record on-record speech**:
- CBF press releases issued under Colden's name
- Bay Journal / WMRA / Maryland Matters / Southern Maryland Chronicle / Outdoor News on-the-record interviews
- One MD DNR press release
- Cross-confirmed via the brief's 26-quote register; substitution-hypothesis (Ch 3 draftable from public record alone) CONFIRMED per commit `0e83dc5` §10.

The named-subject-consent discipline as ratified 2026-05-09 (`feedback_named_subject_consent.md`) was developed in the context of **private-narrative subjects** (Biggie, Phat, the watermen the author knows socially). The default for that category — consent-first, anonymize until signed — is correct for private subjects characterized in detail by an author who knows them socially. **It was not designed to apply to public officials quoted from on-record speech**, where standard journalistic practice is to name. The Ch 3 anonymization treatment over-applied the private-narrative default to a category the discipline did not address.

**Severity:** MEDIUM. Not a factual-drift finding — the quotes are verbatim and the attributions are accurate. A discipline-application finding surfaced by Pass 1 work. The over-cautious anonymization reads evasive in publisher-facing prose, denies Colden professional credit for positions she has publicly staked, and denies readers the ability to verify the quotes against the public record.

**Recommended spot-fix (ratified 2026-05-12, applied same-session via commit `2f76e37`):**

Two parts — chapter and memory.

**Chapter (5 attribution swaps + 2 HTML stale-comment removals):**
- Line 57: remove HTML comment `<!-- v1 from public record; revisit post-Colden-interview -->`
- Line 74: remove HTML comment `<!-- v1 from public record; revisit post-Colden-interview -->`
- Line 75: "A scientist with the Chesapeake Bay Foundation" → "Allison Colden, the Chesapeake Bay Foundation's Maryland executive director"
- Line 93: "the same Bay Foundation scientist has said" → "Colden has said"
- Line 109: "the same Bay Foundation scientist has said" → "she has said"
- Line 172: "the Bay Foundation scientist has said" → "Colden has said"; "the same scientist has said elsewhere" → "she has said elsewhere"
- Line 174: "the same scientist said" → "Colden said"
- Line 178: "the same scientist has said" → "Colden has said"

Subsequent uses mix "Colden" and "she" rather than mechanical repetition.

**Memory refinement (added 2026-05-12 to `feedback_named_subject_consent.md`):**

A new bullet was added under the three existing discipline paths:

> **Public-record exception → public officials / institutional spokespersons quoted from on-record speech are attributable by default.** Press releases issued under their name, signed Congressional or legislative testimony, on-the-record interviews granted to journalists, named op-eds — all of these are public utterances made in institutional capacity and do not require consent for attribution. Standard journalism names them. Anonymizing such quotes reads evasive and denies the subject professional credit for positions they have publicly staked. **Courtesy notification before publication** (a heads-up to the subject or their communications coordinator listing the verbatim quotes attributed to them, asking only for citation-accuracy verification) is the right discipline — not consent. This exception does NOT extend to *characterizations* of the subject's personal views, motivations, or beliefs beyond what the on-record quotes themselves say; for that, the living-subject consent default applies.

The discipline now distinguishes three paths instead of two: private-alive (consent-seeking) / private-deceased (courtesy-notify) / public-on-record (courtesy-notify-not-consent). `MEMORY.md` index hook updated to match.

**Downstream disposition.** The discipline refinement triggered a downstream pre-staging task — the Colden pre-publication citation-verification packet — operationalized 2026-05-13 (commit `15c6b0f`, [`research/outreach/subjects/colden/pre-publication-citation-verification-packet_2026-05-13.md`](../research/outreach/subjects/colden/pre-publication-citation-verification-packet_2026-05-13.md)). Packet fires at the manuscript-to-publisher milestone independent of whether the Colden interview happens.

---

### §1.3 Findings — LOW severity / sharpening opportunities

#### F-2 — Blue crab "sixth consecutive year of below-average numbers" reads tighter than Colden's "more than five years" source quote

**Line 93 (chapter):**
> "It was the sixth consecutive year of below-average numbers."

**Canonical truth.** The chapter's quoted Colden material in the immediately following sentence uses the looser phrasing: *"with more than five years of below average crab numbers, it is clear that changing conditions in the Bay are undermining the current management of this important species."* (Source: CBF "Chesapeake Bay Blue Crab Population Drops to Distressing Low," May 2025; cross-confirmed Maryland Matters 2025-05-23.) The chapter's narrator-voice "sixth consecutive year" is more specific than Colden's "more than five." Both are consistent with the MD DNR winter dredge survey 2020–2025 sequence (six consecutive below-average years through 2025), so the chapter's count is defensible against the underlying data — but tighter than the proximate quoted source.

**Severity:** LOW. Defensible against the underlying survey data. Could be softened to mirror Colden's phrasing for source-mirror discipline; could be left as-is for narrator-voice specificity. A trade-press fact-checker would not flag.

**Disposition (author's call, declined 2026-05-12).** Left as-is. The chapter's "sixth consecutive year" reads as the narrator's own count against the survey record, not as a paraphrase of Colden — and the narrator's count is accurate. The looser quoted phrasing in the immediately following sentence belongs to Colden's institutional voice (which was uttered in May 2025, before the full 2025 winter dredge data closed out). No conflict.

**If a downstream fact-checker pushes back:** the response is "MD DNR winter dredge survey 2020–2025 — six consecutive below-average years through 2025."

---

### §1.4 Externally-verifiable claims — confirmed accurate (no fix needed)

#### §1.4.1 Twelve Colden quotes — all verbatim against `research/outreach/subjects/colden/background-brief_2026-05-08.md` §9

| Ch 3 line | Quote (short form) | Brief Q# / confidence | Verdict |
|---|---|---|---|
| ~75 | "Maryland's striped bass surveys have made it clear; we're facing a looming disaster…" | Q1 [H] | ✓ verbatim (chapter uses `;` connector where source uses `—`; substance identical) |
| ~75 | "there are very few levers left to pull" | Q2 [M] | ✓ verbatim |
| ~75 | "Many people in Maryland rely on striped bass for their food, their businesses, and their futures. Without action, that will all be at risk." | Q4 [H] | ✓ verbatim |
| ~75 | "pummeling" | Q5 [M] | ✓ verbatim (single-word inset; chapter incorporates correctly) |
| ~93 | "The red flags are flying for blue crabs." | Q17 [H] | ✓ verbatim |
| ~93 | "with more than five years of below average crab numbers, it is clear that changing conditions in the Bay are undermining the current management of this important species." | Q18 [H] | ✓ verbatim (chapter lowercases "With" → "with" to fit sentence flow; word-substance identical) |
| ~109 | "Just as we were confident in increasing the total allowable catch when the science says we should, we need to be as willing to take reductions when the science indicates that that's warranted." | Q15 [H] | ✓ verbatim |
| ~172 | "Large-scale oyster restoration is working." | Q6 [H] | ✓ verbatim |
| ~172 | "Our effort to bring oysters back from the brink in Chesapeake Bay is working ... but continued recovery is not guaranteed." | Q8 [H] | ✓ verbatim (chapter elides comma → `...`; word-substance identical) |
| ~174 | "Despite a growing oyster population, Maryland's watermen are feeling the pinch of extreme weather and market competition." | Q13 [H] | ✓ verbatim |
| ~178 | "One of the most important ways people connect with the Chesapeake Bay is through eating seafood and fishing." | Q14 [H] | ✓ verbatim |
| ~178 | "there's certainly a lot fewer eyes on the water and a lot fewer people caring passionately about the Bay." | Q14 [H] | ✓ verbatim |

#### §1.4.2 Fishery numbers and dates

| Claim | Canonical source | Verdict |
|---|---|---|
| Oysters: ~15M bushels (late 1880s) → <200k (1990s) → 99% decline | `research/case-studies/chesapeake-fisheries.md` | ✓ |
| MSX in late 1950s / Dermo "in the years that followed" | Standard fisheries history; defensible at memoir register (MSX detected 1957 Delaware Bay → Chesapeake 1959; Dermo present from ~1949 but became epizootic in 1980s) | ✓ defensible |
| MD striped bass moratorium "five years … beginning in 1985" | 1985–1989 established record | ✓ |
| Atlantic striped bass "declared restored" by 1995 | ASMFC declaration 1995 | ✓ |
| MD 2024 YOY index 2.0 vs long-term avg 11.0 | Colden brief §3a / Q3 | ✓ |
| "sixth such season in a row" (stripers YOY 2024) | Colden brief Q3 — "sixth consecutive below-average year" | ✓ |
| 2025 winter dredge: ~238M crabs, 2nd-lowest since 1990 | Colden brief 2025-05-23 entry | ✓ |
| ASMFC menhaden Bay cap 51,000 MT (November 2017) | Colden brief §3c — "Colden's original motion" | ✓ |
| MD oyster population "roughly tripled since 2005" | Colden brief Q6 source phrasing | ✓ (narrator "roughly" softens precise number; no semantic change) |
| Chesapeake watershed 64,000 sq mi, 6 states + DC | Standard CBP figure | ✓ |
| Chesapeake Bay Program "established in 1983" | 1983 Chesapeake Bay Agreement | ✓ |
| Virginia commercial shad fishery closed "in January 1994" | VMRC; verified per commit `b5692f1` (author originally recalled 1990; correction landed) | ✓ — **VMRC date correction confirmed landed** |
| English up the James "in 1607" | Jamestown founded May 1607 | ✓ |
| Norway oil "late 1960s and early 1970s" | Ekofisk strike December 1969 | ✓ |
| Tangier Island "continuously inhabited since the 1770s" | Crockett-family settlement traditionally dated 1778 | ✓ |
| Tangier "two square miles" | ~1.2 sq mi land / ~2 sq mi total | ✓ |
| Tangier "losing about fifteen feet of shoreline a year" | USACE-cited 8–25 ft/yr range | ✓ |
| Smith Island "twelve miles to the north" of Tangier | Straight-line ~12 mi MD-VA Bay distance | ✓ |
| Reedville VA menhaden industrial reduction plant | Omega Protein operations | ✓ |
| Fox Hill = Hampton VA neighborhood, former island fishing community | Local geography | ✓ |
| Author's grandfather at NASA Langley, "twelve miles or so" from Fox Hill | Per story-draft 2026-05-09 author confirmation | ✓ |
| Bay wavelength "three or four seconds" (vs. ~20s ocean swell) | Per story-draft 2026-05-09 chop-physics dump; standard Bay-vs-ocean wave physics | ✓ |

---

## §2. Author-internal memoir claims (audit-existing-prose mode: prose IS canonical reference)

Per Stage-3 template §"Audit-existing-prose mode": skip canonical-facts cross-check for memoir-register first-person claims (no Stage 1 brief; prose is canonical). These claims are flagged here for author-internal verification only.

| Ch 3 lines | Claim | Author-internal verification needed |
|---|---|---|
| 18, 28 | "My grandfather worked at NASA Langley... My family is one generation removed from the working life. We are zero generations removed from the community." | Personal genealogy |
| 47–53 | Biggie portrait — oak-tree build, generational oysterman, one-oar-between-the-beds, 6-pack of Coca-Cola, lunch-in-the-water, oyster-shucking minimal-wrist-motion, eating-while-working | Author's father's recollection (the relationship-holder); courtesy-notify-surviving-family workstream will probe the family for any corrections (see [`research/outreach/subjects/biggie/courtesy-notification-process-guide_2026-05-13.md`](../research/outreach/subjects/biggie/courtesy-notification-process-guide_2026-05-13.md)) |
| 51 | "Biggie has been dead for more than thirty years" / "He died before Virginia stopped its commercial shad fishery in 1994" | Family-of-Biggie may have exact year; if surfaced via courtesy-notify, chapter can be tightened from "more than thirty years" to specific year |
| 132–140 | Phat portrait — 2-3am crab pots, mid-morning return, mechanic shop on the Peninsula with name on the sign, crab pots stacked behind locked fence, customer cars in the back lot, shop close 5-6 pm | Phat's own recollection — to be confirmed during the Phat consent conversation per `research/outreach/subjects/phat/consent-process-guide_2026-05-10.md`. Phat may ask for corrections; chapter is currently in named-pending-consent state. |
| 125 | "I have watched the green of the water change, in the years I have been on it from the deck of a sailboat in summer, in a way that does not feel like life." | First-person observation; author canonical source |
| 68 | "The watermen I knew as a boy at the marinas where my family kept boats were talking, as the moratorium years came on, about something they had not had to talk about before." | First-person childhood memory of 1985-moratorium-era marina talk; author canonical source |
| 150 | "I have watched the marina I keep my own boat at, in the years I have kept her there, slowly tip from a place where the working operators had most of the slips toward a place where the recreational owners do." | First-person observation; author canonical source |

**Recommendation:** Author runs a single internal pass against personal records (any family-history notes; conversations with father; Phat consent conversation when it lands; Biggie family notification when it lands) before publisher submission. The Biggie family notification (if substantive corrections surface) and the Phat consent conversation (if Phat asks for corrections) are the two most likely sources of author-side §2 sharpening between now and publisher handoff.

---

## §3. Named-subject consent — Pass 1 verification

Per workstream-handoff Ch 3 emphasis: "Biggie courtesy-notify-family before publication; Phat's consent status; substitution-hypothesis CONFIRMED" + post-audit refinement: "public-record exception for Colden."

### §3.1 Biggie (deceased, private subject)

Chapter posture (pre-audit and post-audit): named throughout; HTML comment at line 46 `<!-- courtesy-notify surviving family if reachable -->` carries the discipline flag.

**Verdict:** ✓ Discipline-correct per `feedback_named_subject_consent.md` "deceased = named with courtesy-notify-surviving-family-if-reachable." Pre-publication action operationalized 2026-05-13: [`research/outreach/subjects/biggie/courtesy-notification-process-guide_2026-05-13.md`](../research/outreach/subjects/biggie/courtesy-notification-process-guide_2026-05-13.md) (commit `164b9e2`) — covers locating reachable family, packet contents, cover-letter draft, delivery options, response scenarios, good-faith-effort threshold, documentation.

### §3.2 Phat (alive, private subject)

Chapter posture (pre-audit and post-audit): named throughout the portrait (lines 132–140); HTML comment at line 131 `<!-- consent-pending; anonymize at publication if declined -->` carries the discipline flag; in-prose disclaimer at line 132 ("a man I will call Phat, which is the short form of his given name, and I have not yet asked him whether he wants to be called something else in a book") signals the named-pending-consent state to the reader.

**Verdict:** ✓ Discipline-correct per `feedback_named_subject_consent.md` "living = named-pending-consent." Pre-publication action operationalized previously: `research/outreach/subjects/phat/consent-process-guide_2026-05-10.md`. Fallback recipe (anonymize lines 132 + 140 + remove HTML flag) documented in `research/outreach/subjects/phat/phat-mentions-inventory_2026-05-10.md`.

**Process note (workstream-handoff hygiene — see §4):** the original Ch 3 audit-emphasis row described Phat as "anonymized as 'a crabber and a fisherman' pending consent." This describes the **fallback state** if consent declines (per the inventory's "If consent declined" recipe), not the current chapter state, which is named-pending-consent. No chapter finding flows from this; the workstream handoff's framing is what needs reconciling.

### §3.3 Allison Colden (alive, public official)

Chapter posture (pre-audit): anonymized as "a scientist with the Chesapeake Bay Foundation" / "the same Bay Foundation scientist" with HTML flags `<!-- v1 from public record; revisit post-Colden-interview -->` at lines 57 + 74.

Chapter posture (post-F-3, ratified 2026-05-12): **named** ("Allison Colden, the Chesapeake Bay Foundation's Maryland executive director" on first use; "Colden" / "she" thereafter); HTML flags removed.

**Verdict:** ✓ Discipline-correct per `feedback_named_subject_consent.md` **public-record exception** (added 2026-05-12 as part of F-3 ratification). All twelve quotes verified verbatim against the public-record substrate; standard journalistic attribution applies; courtesy notification (not consent) is the appropriate downstream discipline.

**Pre-publication action operationalized 2026-05-13:** [`research/outreach/subjects/colden/pre-publication-citation-verification-packet_2026-05-13.md`](../research/outreach/subjects/colden/pre-publication-citation-verification-packet_2026-05-13.md) (commit `15c6b0f`) — quote-and-citation table for Val DiMarzio (CBF MD Communications, gatekeeper since 2026-05-05) covering all twelve verbatim quotes; fires at the manuscript-to-publisher milestone independent of whether the Colden interview happens.

### §3.4 Other potentially-named subjects

- **Powhatan** (line 32, historical reference) — no living-person concern. ✓
- **English (re Jamestown 1607)** — no living-person concern. ✓
- **Author's father / grandfather / family** — not named in Ch 3 ("my father", "my grandfather"); consistent with Ch 1 / Ch 10 / AuthorsNote registration of the same family. ✓
- **The "retired waterman who worked the Bay through the 1985 moratorium" (line 81)** — composite / anonymous; no consent issue. ✓
- **"A waterman in his fifties on the Lower Bay" (line 160) and "the men on the dock" (line 158)** — composite / anonymous archetypes. ✓
- **Chris Moore (CBF VA executive director)** — NOT quoted by name or pronoun in Ch 3 (the chapter quotes only Colden, female `she` pronouns throughout). The Moore FPD-9 brief (`c352d9a`) exists as parallel-track substrate but the chapter does not currently call on it. Cross-chapter consistency observation only (see §6).

**Verdict on consent pass:** ✓ No regressions; F-3 produced a net discipline refinement (public-record exception added) that strengthens the project's posture going forward.

---

## §4. Workstream-handoff Ch 3 row — item dispositions

The workstream-handoff Ch 3 audit-emphasis row carried four items. Verification + disposition:

1. **"Biggie courtesy-notify-family before publication"** — confirmed; discipline applied at line 46 HTML comment; downstream process guide pre-staged 2026-05-13 (commit `164b9e2`). ✓
2. **"Phat's consent status"** — confirmed; chapter posture is named-pending-consent; pre-existing process guide covers execution. ✓
3. **"substitution-hypothesis CONFIRMED (commits `0e83dc5` + `c352d9a`)"** — confirmed via the Colden + Moore FPD-9 briefs. The Colden brief's §10 verdict — "Ch 3 is draftable from public record alone. The chapter can ship without the Colden interview having taken place" — is operative; all twelve Colden quotes in Ch 3 verified against the brief's quote register. ✓
4. **"VMRC date correction landed (`b5692f1`)"** — confirmed; chapter lines 51 + 85 carry the corrected 1994 date (author's original recollection per story-draft 2026-05-09 was 1990; correction to verified VMRC 1994 date landed in commit `b5692f1` per the commit message). ✓

### §4.1 Workstream-handoff hygiene (process observations, not chapter findings)

Two minor descriptions in the audit-emphasis row that do not affect the chapter but are worth flagging for downstream session hygiene:

- **"Karen Moore (CBF VA)"** in the named-subjects column — CBF Virginia's executive director is **Chris Moore** (male), per commit `c352d9a` and `research/outreach/subjects/moore/background-brief_2026-05-08.md`. No "Karen Moore" surfaced in the project's CBF-side research. Likely a transcription artifact in the handoff table. No chapter finding flows from this (Moore is not quoted in Ch 3); the workstream-handoff Ch 3 row could be tightened on the next PM dashboard sync.
- **"Phat's (anonymized as 'a crabber and a fisherman' pending consent)"** — describes the fallback state (per the inventory's "If consent declined" recipe) rather than the current named-pending-consent state. Same disposition as above: no chapter finding; workstream-handoff framing could be tightened on the next sync.

---

## §5. Bonus — claims that improvise beyond canonical anchor list

Per Stage-3 template Pass-1 bonus: surface claims the draft makes that aren't in the canonical-facts inventory. In audit-existing-prose mode the §6 inventory is absent, so this bonus runs against the Colden background brief + case-study briefs + bibliography §19.5 (the nearest canonical-anchor surrogates).

- **Author's first-person Bay observations** (lines 125, 68, 150 — sailboat-summer green-water, 1985-moratorium-era marina memory, marina recreational-tip observation) — first-person memoir; author canonical. Not in any external anchor list; per audit-existing-prose mode, prose IS canonical. ✓
- **Fox Hill mutual-aid 3am scene** (lines 24, 26) — author primary-source per story-draft 2026-05-09 §"Raw dump"; not in any external anchor list. Author canonical for this material. ✓
- **Chop-physics aside** (line 20) — author primary-source per story-draft 2026-05-09 §"Raw dump" (Bay 3-4 second wavelength vs. ocean 20+ second wavelength); cross-checked against standard wave physics — defensible. ✓
- **Biggie portrait specifics** (lines 47–53) — father's recollection per story-draft 2026-05-09; courtesy-notify-family will probe for any corrections. Per audit-existing-prose mode, prose IS canonical pending family corrections. ✓
- **Phat portrait specifics** (lines 132–140) — author's observation; Phat's own recollection will be probed during consent conversation. Per audit-existing-prose mode, prose IS canonical pending Phat's corrections. ✓
- **"Tangier Island losing about fifteen feet of shoreline a year"** (line 146) — within USACE-cited 8–25 ft/yr range; defensible. ✓
- **"a hollowing"** quoted as a phrase "by people who like the phrase" (line 107) — explicitly attributed to unnamed observers; no specific source claim. Not load-bearing; reads as generalized observation. ✓

---

## §6. Cross-chapter consistency observations (flagged for Phase B whole-book audit)

These are NOT Ch 3-only fact-check findings; flagged here for the Phase B whole-book audit:

- **McDowell County callbacks** (Ch 3 lines 154, 190, 194, 202) — Ch 3 calls back to Ch 2 territory four times. Cross-chapter consistency between Ch 3's references to McDowell and Ch 2's actual McDowell material should be verified in Phase B. Specifically: Ch 3 line 154 "The chapter on McDowell County described this same pattern from the inside of the hollow"; line 194 "The miner who developed black lung was not compensated for the lung. He was paid for the coal." Phase B should confirm both claims land cleanly against Ch 2's content.
- **Norway-bridge framing** (Ch 3 lines 208–220) — Ch 3 closes with a Norway introduction that bridges to Ch 4 (`The Existence Proof`). Phase B should verify the framing aligns with Ch 4's opening + the Norway case-study brief (`research/case-studies/norway-swf.md`). The fund-age fix (F-1) brought Ch 3 into alignment with the Norway case-study brief; cross-check that Ch 4's parallel framing is internally consistent (Ch 4 is downstream territory).
- **Chris Moore (CBF VA) as latent Ch 3 voice** — the workstream-handoff Ch 3 row implicitly suggests Moore could be a Ch 3 voice; the Moore FPD-9 brief (`c352d9a`) exists as parallel-track substrate; but Ch 3 currently only quotes Colden. Phase B should decide whether Ch 3 stays Colden-only or admits Moore as a second voice (the symmetry argument for adding Moore: MD-side voice + VA-side voice = full Bay representation; the cost: chapter weight + voice-management complexity). Out of scope for Ch 3 Pass 1.

---

## §7. Pass-1 verdict

**Total findings by severity:**

- CRITICAL: 0
- HIGH: 0
- MEDIUM: 2 (F-1 Norway fund age; F-3 Colden public-record exception)
- LOW: 1 (F-2 crab "sixth consecutive year" — declined as defensible)

**Pass-1 verdict:** **READY AS-IS, post-ratification.** F-1 (Norway fund age) was a numeric correction; F-3 (Colden) was a discipline-application correction that produced 5+ chapter spot-fixes plus a memory refinement; both applied 2026-05-12 in commit `2f76e37`. F-2 was author-declined as defensible against survey data.

**No Ch 3 prose blocks submission on fact-check grounds.** The chapter is fact-check-stable for trade-press fact-checker review.

**Author-internal verification gap:** §2's author-internal memoir claims (Biggie portrait, Phat portrait, first-person Bay observations) need the two pre-staged downstream processes to land before submission:
- Biggie family courtesy-notify (commit `164b9e2`, no hard deadline)
- Phat consent conversation (per existing 2026-05-10 process guide; tied to *Noema* submission window)

Plus the manuscript-to-publisher-stage Colden citation-verification packet fire (commit `15c6b0f`).

---

## §8. What this pass did NOT do

Per the user's per-prompt scoping, this artifact covers Pass 1 (fact-check) only. The following are deferred to subsequent fires:

- **Pass 2 (voice-polish).** LLM tics + em-dash crutches + rule-of-three + cadence repetition + apparatus residue + memoir-register sentence-length-variance discipline. Per workstream handoff, Ch 3's specific Pass-2 emphasis (per the memoir-register category Ch 1, Ch 3, Ch 10) is "sentence-length variance discipline; first-person consistency."
- **Pass 3 (audience-load).** 20-character book-audience pressure-test set per `tools/drafting-templates/audience-pressure-test-construction.md`. Per workstream handoff, Tier-1 gating audiences + cumulative comp-cluster reader + Ch 3-specific cultural-resonance emphasis (Fox Hill).

Author should fire Pass 2 + Pass 3 sessions to complete the three-pass discipline before Ch 3 is considered Phase-A-complete.

---

## §9. Hard constraints honored

- ✓ Applied spot-fixes to `Chapter__1_TheQuietMath__Draft.md`? **N/A — this is the Ch 3 pass.** Applied spot-fixes to `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` per the author's "ratify" trigger same-session (Phase A audit + Phase C application combined), consistent with Ch 1's same-session pattern per commit log dates.
- ✓ Did NOT re-write sections — only surgical attribution swaps + 2 HTML stale-comment removals + 2 numeric-phrase substitutions (F-1).
- ✓ Did NOT propose meta-conclusions about the v2.0 discipline — but did surface a discipline-refinement (public-record exception) ratified separately to `feedback_named_subject_consent.md` + MEMORY.md index.
- ✓ Did NOT contact named subjects — pre-staged the two downstream processes (Biggie family notification, Colden citation-verification packet) as artifacts to be fired by the author when their respective triggers arrive.
- ✓ Flagged the workstream-handoff hygiene items (§4.1 Karen→Chris Moore; Phat current-vs-fallback state framing) as process observations, not chapter findings.

---

*End of Ch 3 Stage-3 Pass 1 (Fact-Check) rigor pass — RATIFIED 2026-05-12 (audit + spot-fixes + memory refinement; commits `2f76e37`). Two downstream pre-staged artifacts (Colden citation-verification packet commit `15c6b0f`; Biggie family courtesy-notification process guide commit `164b9e2`) produced 2026-05-13 as carries from this audit. Artifact filed retroactively 2026-05-13 for archival symmetry with the Ch 1 Pass-1 artifact (commons_bonds_rigor_pass_2026-05-11_ch1_the_quiet_math_stage3_fact_check_v1.0.0.md). Ready for Ch 3 Pass 2 (voice-polish).*
