# Aeon portal-timing investigation — Sun May 31 2026

**Investigation window:** Sun May 31 2026 ~10:05–10:40 EDT (~14:05–14:40 UTC).
**Trigger:** Empirical observation that `aeon.co/pitch` was NOT open at 10:05 EDT (~14:05 UTC), contradicting the submission-day-package assumption that the portal would open at 00:01 AEST Mon Jun 1 (= 14:01 UTC = 10:01 EDT).
**Spawning PM session:** `pm-portfolio-ratification-and-aeon-submission-260529-b4ac02`.
**Methodology:** Direct site fetches (blocked by Vercel security checkpoint — see §4); web-search triangulation across editor LinkedIn/Wikipedia/X profiles; UK Companies House lookup; second-hand pitch-guidance posts (Instagram, APA Blog, Quora summaries).

---

## §1 Executive recommendation

**SUPERSEDED — see §8 for current recommendation (Update 2, 20:44 EDT).** The recommendation below was the state of the investigation through ~11:00 EDT; both 19:00 EDT (London BST midnight) and 20:00 EDT (UTC midnight) candidate open-moments are now empirically falsified per author observation at 20:44 EDT. Read §1 for the reasoning trail; read §8 for the revised hypothesis ranking + current recommendation.

**Original recommendation (now superseded):** **Do not submit at 10:01 EDT today.** That target was based on a falsified timezone assumption (see §3 + §5). Instead:

**Primary recommendation — submit at portal-open tonight Sun May 31 ~19:00–20:00 EDT** (= 23:00 UTC May 31 or 00:00 UTC Jun 1 = 00:00 BST or 00:00 UTC Mon Jun 1). This is the queue-position-optimal moment within the Jun 1–7 window: portal-open submission lands ahead of overnight Asia/Pacific + UK + EU pitches that will accumulate between portal-open and Mon AM US-time, all of which arrive in Haselby's first Monday-morning review batch.

**Acceptable backup — submit any time Mon Jun 1 EDT** if author has independent reason to prefer Mon AM (rest, focus, calmer headspace). Submitting Mon AM buys nothing editorially over portal-open — both arrive before Haselby logs in for his workday — but it costs queue position relative to overnight global submissions. The cost is small but real; choose Mon AM only on author-convenience grounds, not on editorial reasoning.

**Hard floor:** Author MUST manually verify `aeon.co/pitch` is open via a real browser session BEFORE pasting. Aeon's site is behind a Vercel security checkpoint that blocks automated state checks; the only authoritative open/closed signal is a human-browser visit. Browser cache + CDN propagation can lag — recommend hard-refresh (Cmd-Shift-R) and/or incognito session if the page appears stuck on a stale "closed" state past the candidate open-moments.

**Confidence rating:** **HIGH** that 10:01 EDT today is wrong (empirically falsified — see §4). **MEDIUM-HIGH** that the portal opens tonight 19:00–24:00 EDT (= 23:00 UTC Sun → 04:00 UTC Mon — bracketing London-midnight, UTC-midnight, and the latest plausible NYC-midnight cron). **MEDIUM** on the marginal queue-position benefit of portal-open submission vs Mon AM EDT — small in absolute terms (Haselby reads pitches in batch regardless), but real if there is any FIFO bias.

**Correction note (2026-05-31 corrected ~10:55 EDT):** The initial version of this document recommended "Mon Jun 1 ~07:00–09:00 EDT" as primary. That landed in an inconsistent middle — it argued queue position is weak (so timing doesn't matter), then recommended a sub-optimal time within the week anyway. The corrected position above is internally coherent: if queue position matters at all, submit at portal-open; if it doesn't, submit anytime; the original "Mon AM EDT" recommendation was author-convenience reasoning ("submit during your own daylight hours") miscast as editorial reasoning ("before Haselby logs in"). Both submissions arrive before Haselby logs in; only the earlier submission is ahead of overnight global pitches.

---

## §2 Editor location findings

| Person | Role | Location | Source confidence |
|---|---|---|---|
| **Sam Haselby** | Senior Editor (Philosophy desk; THE pitch target) | **New York, NY, US** | HIGH — LinkedIn ([sam-haselby-8b890495](https://www.linkedin.com/in/sam-haselby-8b890495/)); Aeon staff page; cross-confirmed via prior academic posts at Columbia + Al Jazeera America (NYC); Wikipedia |
| **Sam Dresser** | Deputy Editor | **New York City** | HIGH — Instagram bio + multiple staff-page summaries cross-confirm NYC |
| **Brigid Hains** | Editorial Director / co-founder | Australian by nationality; founded Aeon in London 2012; current physical location **probably Melbourne** but not confirmed by primary source within this investigation window | MEDIUM — Wikipedia + Aeon Media descriptions; Aeon Media run from Melbourne head office per multiple sources |
| **Paul Hains** | Co-founder / Director | Australian; same as Brigid; **probably Melbourne** | MEDIUM |
| **Kirsten Freeman** | Director (operations, leading teams across Melbourne / London / NYC) | Not confirmed; operations role implies distributed coordination | LOW |
| **Nigel Warburton** | Founding-era Philosophy editor | UK-based historically; **current status as active Aeon editor not confirmed by this investigation** | LOW — may have departed or shifted role |

**Critical implication:** The pitch is targeted at Sam Haselby on the Philosophy desk. **Haselby is in NYC.** Sam Dresser (deputy) is also in NYC. The original submission-day-package's "first-in-queue Monday morning Melbourne time" strategic rationale presupposed editorial workflow on Melbourne hours — but the Philosophy desk that will actually read this pitch operates on US Eastern time. **Queue position at "Melbourne morning" is irrelevant to the editor's read order.**

**Aeon Media corporate structure (from Companies House + Wikipedia + secondary):**
- **Legal entity:** AEON MEDIA LIMITED (UK company; registered office "The Fisheries, 1 Mentmore Terrace, London, England, E8 3PN" — UK Companies House #07920160)
- **Founded:** London, September 2012, by Australian couple Paul + Brigid Hains
- **Offices:** London, Melbourne, and New York
- **Editorial distribution:** Director Brigid Hains works closely with commissioning editors across all three cities; operations led by Kirsten Freeman across Melbourne / London / NYC
- **HQ characterization is contested across sources:** some characterize as "Melbourne head office"; the legal entity is UK-registered. The most accurate description is **distributed: legally UK; founded London; founders Australian; operationally trans-Pacific**.

---

## §3 Portal cadence findings

**Cadence rule (confirmed from primary source):**

Sam Haselby on X (multiple tweets): *"Aeon Magazine's pitch portal is open for essay pitches for the first week of each month."*

Cross-confirmed via [Instagram repost (suremedia.agency, Mar 4 2026)](https://www.instagram.com/p/DVeHByxEs9A/) which states verbatim: *"Aeon only accepts pitches from the 1st to the 7th of each month, and the current window closes 7 March 2026."*

So the rule is **calendar days 1–7 of each month**, not "Monday only" and not "Melbourne timezone." The "Mondays Melbourne morning" framing in the original strategy artifact was a heuristic INFERENCE about queue position, not stated Aeon guidance.

**Timezone of the cron switchover (NOT directly stated by Aeon anywhere this investigation surfaced):**

| Timezone hypothesis | Portal opens at (UTC) | EDT equivalent | Plausibility |
|---|---|---|---|
| Melbourne AEST midnight (original assumption) | 14:00 UTC May 31 | **10:00 EDT today** | **FALSIFIED** (portal observed closed at 10:05 EDT) |
| Melbourne business open (09:00 AEST Mon) | 23:00 UTC May 31 | 19:00 EDT today | MEDIUM (cron-on-business-hours is unusual) |
| **London BST midnight (00:00 BST Jun 1)** | **23:00 UTC May 31** | **19:00 EDT today** | **HIGH** — UK-registered company; UK editorial office; server cron most likely tied to legal-entity timezone |
| **UTC midnight (Jun 1)** | **00:00 UTC Jun 1** | **20:00 EDT today** | **HIGH** — generic server-default; many SaaS portals use UTC cron irrespective of business location |
| NYC EDT midnight (00:00 EDT Mon Jun 1) | 04:00 UTC Jun 1 | **00:00 EDT Mon (midnight tonight)** | MEDIUM — editorial team is NYC; cron less commonly tied to editorial-team time |
| Sometime Mon AM London business start | ~08:00 BST Jun 1 = 07:00 UTC Jun 1 | 03:00 EDT Mon | LOW (Aeon would not gate weekly window by business-hours-of-one-office) |

**Best estimate:** Portal opens **tonight US-time**, most likely in the 19:00–20:00 EDT window (= London midnight or UTC midnight), with a possible bracket extending to 00:00 EDT Mon (NYC midnight). All three candidates align with the same general rule: "first calendar day of the month in some Northern-Hemisphere-relevant timezone."

**Why the original "Melbourne AEST midnight" inference fell:**
- It rested on "Melbourne HQ" as the timezone anchor.
- Aeon's legal entity is UK-registered; "Melbourne HQ" is from second-hand sources and is contested.
- Even granting Melbourne HQ, the server-side cron rarely follows the HQ timezone of a globally distributed magazine — typically follows UTC or the legal-entity jurisdiction (London).
- The empirical observation at 14:05 UTC May 31 conclusively rules out 14:00 UTC May 31 as the opening moment.

---

## §4 Current portal state at investigation time

**Direct fetch attempts to `aeon.co/pitch` and `aeon.co/people` returned:**
- HTTP 429 Too Many Requests (WebFetch); OR
- HTTP 429 with body `<title>Vercel Security Checkpoint</title>` (curl with browser User-Agent)

**Implication:** Aeon's site is behind Vercel's bot-protection challenge. The challenge requires browser JavaScript execution; it cannot be solved by command-line HTTP clients, the Claude WebFetch tool, or any standard scrape. **Only a human browser session (or the Chrome MCP extension, if installed) can reliably read the live portal state.**

The Wikipedia/Sam Haselby/Aeon people-page WebFetches via Google's cache (the search-snippet route) succeeded; direct site fetches did not.

**Snapshot of human-observable state at investigation time:**
- Author empirically reports portal CLOSED at 10:05 EDT (= 14:05 UTC) Sun May 31.
- This investigation could NOT independently re-verify the closed state via automated tool, only via inference from secondary sources ("Aeon Magazine is currently closed for pitches" appears in current Google search snippets for `aeon.co/pitch`).

**Author-action required:** Manual browser refresh of `aeon.co/pitch` at the candidate open-moments listed in §3 to confirm transition to open state. Recommended check times:
1. ~19:00 EDT Sun May 31 (London-midnight hypothesis)
2. ~20:00 EDT Sun May 31 (UTC-midnight hypothesis)
3. ~00:00 EDT Mon Jun 1 (NYC-midnight hypothesis)
4. ~07:00 EDT Mon Jun 1 (failsafe — by this time portal will certainly be open if it's opening at all on Jun 1)

---

## §5 Strategy artifact verification

**Source artifact:** `publishing/essays/aeon-mask-of-abundance/_archive/planning/aeon-submission-strategy_2026-05-08.md` §"Phase 1 — Submit (June 1-7, 2026 portal window)"

**Verbatim quote of timing rationale:**

> **Scheduled submission time:** **At or near 00:01 AEST on Mon Jun 1, 2026** (Melbourne HQ timezone; UTC+10 in southern-hemisphere winter).
>
> Equivalent timestamps in other zones:
> - 14:01 UTC, Sun May 31, 2026
> - 10:01 EDT, Sun May 31, 2026
> - 07:01 PDT, Sun May 31, 2026
>
> **Strategic rationale for portal-open submission:** Aeon's pitch volume is high; submitting at portal-open puts the pitch at the top of Monday morning's queue Melbourne time, before the day's pitch volume builds. Earlier discussions (the May 2026 portal closing on schedule rather than extending due to the Philosophy Prize bandwidth pressure) suggest queue position matters.

**Confidence assessment of original rationale:**

| Claim | Evidence cited in artifact | Investigation finding |
|---|---|---|
| "Melbourne HQ timezone" | Asserted without citation | **WEAK** — Aeon Media Limited is UK-registered (London); "Melbourne HQ" is contested across sources |
| "Portal opens 00:01 AEST Mon Jun 1" | Inferred from "Melbourne HQ" assumption | **FALSIFIED** — portal observed closed at the predicted open moment |
| "Queue position matters" | "Earlier discussions" — no specific source quoted | **WEAK** — queue-position-matters logic presupposes editor reads in arrival order; Haselby is NYC-based and almost certainly batch-processes pitches during his US workday |
| "First-in-queue Monday morning Melbourne time" | Compound inference from above two | **WEAK** — even if queue position mattered, Melbourne morning is not when the NYC-based Philosophy editor would be reading |

**Root cause of the falsified prediction:** The strategy artifact (2026-05-08) made three layered assumptions, none of which was empirically anchored:
1. Aeon's HQ is Melbourne (contested; legal entity is London).
2. The portal cron runs on HQ time (a SaaS-engineering assumption that often doesn't hold).
3. Queue-position FIFO matters (an editorial-workflow assumption that is unlikely for a magazine processing high pitch volume across a one-week window via a single Philosophy editor).

The "earlier discussions" reference about May 2026 portal closing on schedule does NOT actually support the AEST-midnight inference — that observation is consistent with any timezone-anchored close-of-window rule.

**The strategy artifact is not wrong about the overall window (Jun 1-7).** It is wrong about the specific opening moment and the urgency of submitting at minute zero of that window.

---

## §6 Revised submission-day-package amendment proposal

**Status:** PROPOSED for author ratification; NOT applied by this investigation per scope discipline.

**File to amend:** `publishing/essays/aeon-mask-of-abundance/submission-day-package_2026-05-31.md`

**Proposed edits:**

### Amendment 1 — Replace top banner

Current:
```
# Aeon submission-day package — Sun May 31 2026 14:01 UTC

**Purpose:** Single file to open at submission time. All copy-paste material in one place; no context-switching across files mid-submission.

**Submission target:** Sun May 31 2026 ~14:01 UTC (= Mon Jun 1 ~00:01 AEST Melbourne; = Sun May 31 ~10:01 EDT; = Sun May 31 ~07:01 PDT)
```

Proposed:
```
# Aeon submission-day package — portal-open Sun May 31 evening EDT

**Purpose:** Single file to open at submission time. All copy-paste material in one place; no context-switching across files mid-submission.

**Submission target (REVISED 2026-05-31 per portal-timing investigation):**
Primary window — Sun May 31 2026 ~19:00–20:00 EDT (= 23:00 UTC May 31 or 00:00 UTC Jun 1 = portal-open moment per London-midnight or UTC-midnight cron hypothesis).
Acceptable backup — any time Mon Jun 1 EDT (author-convenience choice; small queue-position cost vs portal-open).

**Why revised:** Original 14:01 UTC target was based on a "Melbourne AEST midnight" inference that was empirically falsified Sun May 31 at 10:05 EDT (portal closed). The actual portal-open cron almost certainly runs on London BST or UTC, opening ~19:00–20:00 EDT Sun May 31 (= 00:00 BST or 00:00 UTC Mon Jun 1). The Philosophy editor (Sam Haselby) processing this pitch is NYC-based and reads pitches during his US workday — but portal-open submission still lands ahead of overnight Asia/Pacific + UK + EU pitches that will accumulate before his Mon AM EDT review batch. Submit at portal-open for the queue-position-optimal moment. See `rigor/portal-timing-investigation_2026-05-31.md` §1 + §7 for full evidence + the corrected reasoning trail.
```

### Amendment 2 — Replace "Strategic rationale" line

Current:
```
**Strategic rationale for portal-open submission:** First-in-queue Monday morning Melbourne time, before the day's pitch volume builds. Per Aeon submission strategy 2026-05-08 §"Phase 1."
```

Proposed:
```
**Strategic rationale (REVISED 2026-05-31):** Submit at portal-open Sun May 31 evening EDT (~19:00–20:00 EDT = London-midnight or UTC-midnight Mon Jun 1). The "first-in-queue Melbourne morning" rationale in the 2026-05-08 strategy artifact rested on three unsupported assumptions (Melbourne HQ as cron anchor; cron-on-HQ-time SaaS convention; FIFO editorial workflow); the first was empirically falsified Sun May 31. The corrected version of the queue-position logic: the Philosophy editor (Haselby, NYC) reads pitches during his US workday in batch, but portal-open submission still lands ahead of overnight Asia/Pacific + UK + EU pitches that accumulate between portal-open and Mon AM EDT, all of which arrive in Haselby's first weekly review batch. The marginal benefit of portal-open submission is small in absolute terms but coherent — it costs nothing (V-E pitch is already final-ratified) and removes the noise of "submit during my own daylight hours" rationalization.
```

### Amendment 3 — Update §"Submission-day workflow (suggested sequence)" §1

Current ¶1:
```
1. **~13:55 UTC (10 min before):** Open this file. Open `aeon.co/pitch` portal in a separate tab.
2. **~13:58 UTC:** Confirm portal is open + form fields are as expected from Fri May 29 pre-sub check. If form has changed, take a screenshot and adjust paste-order accordingly.
3. **~14:01 UTC:** Begin paste sequence:
```

Proposed:
```
1. **Sun May 31 ~18:30 EDT (30 min before earliest candidate open):** Open this file. Open `aeon.co/pitch` portal in a separate tab (real browser; portal is behind Vercel bot-checkpoint — automated state checks unreliable; recommend hard-refresh + incognito session if state appears stuck).
2. **Sun May 31 ~18:55 EDT onward:** Refresh `aeon.co/pitch` at 5-min intervals starting 18:55 EDT. Candidate open-moments: 19:00 EDT (London BST midnight), 20:00 EDT (UTC midnight), 00:00 EDT Mon (NYC midnight). Cache/CDN propagation may lag — give each candidate moment +5-10 min buffer before moving to next hypothesis.
3. **At first verified-open moment:** Begin paste sequence:
```

### Amendment 4 — Update §"What to do if something unexpected happens at submission" §"Portal isn't open at 14:01 UTC"

Current:
```
**Portal isn't open at 14:01 UTC:** wait 5-10 minutes; refresh. If still not open by 14:30 UTC, document the issue + try again at 15:00 UTC + every 30 min. If Aeon has delayed the June portal open (rare but possible — May 2026 prize cycle caused similar friction per `aeon-submission-strategy_2026-05-08.md` §"Aeon Philosophy Prize concurrent activity"), submit when portal opens.
```

Proposed:
```
**Portal isn't open at planned submission moment:** wait 15-30 minutes; refresh. The June portal cron is most likely tied to London or UTC midnight (= 19:00–20:00 EDT Sun May 31), but if Aeon's cron is on NYC midnight or business-hours start, portal may not open until 00:00 EDT Mon (midnight) or even ~07:00 EDT Mon. Cap escalation: if still closed by 09:00 EDT Mon Jun 1, the portal cron may have a longer delay or Aeon may have paused the June window — at that point document the issue and follow up via `aeon.co/contact` (cmh+pitch@aeon.co or as listed).
```

### Amendment 5 — Update §"Pre-submission verification" item

Current:
```
- [ ] Verify timezone alignment (AEST = UTC+10 in southern-hemisphere winter; Mon Jun 1 ~00:01 AEST = Sun May 31 14:01 UTC)
```

Proposed:
```
- [ ] Verify portal is open via REAL BROWSER (not automated tool — site is behind Vercel bot-checkpoint). Portal cron likely runs on London BST or UTC, opening ~19:00–20:00 EDT Sun May 31 = 00:00 BST/UTC Mon Jun 1. Hard floor for submission: portal must show submission form fields visible + active, not "currently closed" message.
```

---

## §7 Confidence + caveats

**What I am HIGH-confidence about:**
- Sam Haselby is NYC-based (multiple cross-referenced sources)
- Sam Dresser is NYC-based (multiple cross-referenced sources)
- Aeon Media Limited is UK-registered (UK Companies House primary record)
- "First 7 days of each month" is the actual portal window rule (Haselby's own X post + Instagram repost)
- The original 00:01 AEST Mon Jun 1 = 14:01 UTC = 10:01 EDT timing is FALSIFIED (empirical observation by author at 10:05 EDT)

**What I am MEDIUM-confidence about:**
- Portal opens tonight 19:00 EDT (London midnight) or 20:00 EDT (UTC midnight) — high prior probability, but not directly verified
- The "first-in-queue" rationale is weak because Haselby batch-processes — strong reasoning but no insider source confirms his workflow

**What I COULD NOT verify in this investigation:**
- The exact portal-open moment Sun May 31 evening — Aeon's site is behind Vercel bot-checkpoint; automated probes fail; only a human browser can see the live state
- Brigid + Paul Hains' current physical location (assumed Melbourne but not primary-source confirmed)
- Whether Nigel Warburton is still an active Aeon Philosophy editor
- Whether Aeon's pitch portal has separate "submissions intake" staff who operate on a different timezone than the editorial team

**What would CHANGE the recommendation:**
- If author manually visits `aeon.co/pitch` and finds it has reopened earlier than expected (e.g., already open by 18:00 EDT Sun) → submit then
- If author finds Aeon has posted an explicit "next opens at X UTC/EDT" countdown on the closed-page → that supersedes my inference
- If Haselby tweets confirming a specific opening time on his X account this evening → that supersedes my inference
- If author can reach Aeon contact for guidance directly → primary source beats this investigation

**One caveat worth flagging:** This investigation operated under a 30-45 min wall-clock cap and relied heavily on second-hand sources (Instagram, search snippets, LinkedIn) because Aeon's own site was unreachable via automated tools. The recommendation has high confidence in the *direction* (don't submit at 10am EDT; wait for actual open + likely tonight or Mon AM EDT) and medium confidence in the *specific* alternative timing. The hard floor — wait until the author can VERIFY the portal is open via real browser — is what matters most.

---

*Investigation completed Sun May 31 2026 ~10:45 EDT. Findings document committed to feature branch `claude/aeon-portal-timing-investigation-260531-87934e`; auto-merging to main per merge-on-ratification (internal scaffolding) at session close.*

---

## §8 Update 2 — empirical anchor at 20:44 EDT Sun May 31

**Author observation (20:44 EDT Sun May 31 / 00:44 UTC Mon Jun 1):** Portal STILL NOT open. Cache-bust + incognito verified.

**Empirically falsified hypotheses (all candidate open-moments through 20:44 EDT):**

| Hypothesis | Predicted open at (EDT) | Status |
|---|---|---|
| Melbourne AEST midnight (original assumption) | 10:00 EDT Sun | FALSIFIED (10:05 EDT obs) |
| Melbourne business open (09:00 AEST Mon) | 19:00 EDT Sun | FALSIFIED (20:44 EDT obs) |
| London BST midnight (00:00 BST Mon Jun 1) | 19:00 EDT Sun | FALSIFIED (20:44 EDT obs) |
| UTC midnight (00:00 UTC Mon Jun 1) | 20:00 EDT Sun | FALSIFIED (20:44 EDT obs) |

**Revised hypothesis ranking — remaining candidates:**

| Hypothesis | Predicted open at (EDT) | Time until (from 20:44 EDT) | Plausibility |
|---|---|---|---|
| **NYC EDT midnight (00:00 EDT Mon Jun 1)** | **00:00 EDT Mon Jun 1** | **~3h 16m** | **HIGH** — editorial team is NYC; cron tied to editor-local clock is the remaining standard option after UTC + London + Melbourne are all falsified |
| London BST business open (~08:00 BST Mon) | 03:00 EDT Mon | ~6h 16m | MEDIUM — implies human-toggled portal vs cron |
| London BST business open (~09:00 BST Mon) | 04:00 EDT Mon | ~7h 16m | MEDIUM |
| NYC business open (~09:00 EDT Mon) | 09:00 EDT Mon | ~12h 16m | LOWER — gates the whole weekly window by one office's business hours, which is unusual but possible if Haselby personally toggles |
| Portal paused / June window delayed | N/A | N/A | LOW-MEDIUM — no public signal of delay (no Haselby X update; no Aeon social-channel notice surfacing in web search) but cannot be ruled out |

**Current primary recommendation (supersedes §1):**

1. **Continue checking at 00:00 EDT Mon Jun 1** — highest-probability remaining candidate (NYC midnight, ~3.25h from now).
2. **If still closed at 00:30 EDT:** check at 03:00–04:00 EDT Mon (London business-hours-open candidate).
3. **If still closed at 09:00 EDT Mon:** check on the hour through 12:00 EDT (NYC business-hours-open candidate).
4. **If still closed by 12:00 EDT Mon Jun 1:** escalate. Likely interpretations: (a) June window has been delayed/paused (cf. May 2026 Philosophy Prize bandwidth-pressure friction noted in 2026-05-08 strategy artifact); (b) Aeon shifted the portal cadence and Haselby hasn't tweeted the change yet; (c) Vercel/CDN issue specific to today. Escalation actions: check Haselby's X account for any pitch-window update; check `@aeonmag` X account; if both silent, send a single short email via `aeon.co/contact` ("Hi — wanted to confirm the June pitch window is open; aeon.co/pitch still showing closed at [time]. Submitting [working title] this cycle. Thanks.").

**Decision-tree threshold for switching out of "portal-open is queue-optimal" framing:** If portal is still closed by ~09:00 EDT Mon Jun 1, the queue-position rationale evaporates entirely (all global submitters are now blocked equally). At that point, the right move is "submit cleanly when portal opens, no matter the hour"; no need to anchor to a specific candidate window.

**Authority of remaining hypotheses:** All four falsified hypotheses had MEDIUM-or-better prior plausibility before tonight's observation. Their joint falsification is informative: it suggests the Aeon portal cron is NOT tied to any of the standard server-side clocks (UTC, the legal-entity London time, the founder-Melbourne time). The remaining best-fit hypothesis is **editor-local time (NYC EDT)** — which would be a quirky choice for a SaaS cron but coherent if the portal is human-toggled by Haselby or Dresser themselves at the start of their week. The "human-toggled" interpretation has a separate empirical signature: if true, the portal would never open during the editor's sleep hours, which would predict NYC-business-hours-Mon (09:00 EDT) as the actual moment. The NYC-midnight hypothesis is a compromise between cron-based and editor-local logics.

**Confidence on §8 revised ranking:** MEDIUM. The falsifications are HIGH-confidence; the remaining ranking is a best-guess given limited data. Author's continued empirical observations (each "still closed" datapoint at a candidate moment is a falsification; first "open" observation is the answer) will dominate this analysis going forward.

**Update author handling:** Author has indicated they will continue manual portal checks. This investigation cannot improve on real-time observation; the §8 ranking is a prior over candidate moments, not an authoritative answer. Author's manual check IS the authoritative signal. Suggest the author keep a short timestamp log of "checked at HH:MM EDT — state X" — this becomes useful evidence if the portal-open moment falls in a pattern (e.g., a specific top-of-the-hour or top-of-the-minute moment that confirms cron vs human-toggle).

*§8 update added Sun May 31 2026 ~21:00 EDT.*
