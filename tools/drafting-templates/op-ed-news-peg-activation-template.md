# Op-Ed News-Peg Activation Template

**Date drafted:** 2026-05-24
**Purpose.** Both op-eds (Norway sovereign-wealth + McDowell true-cost) are pipeline-ready: Stage 1 + Stage 2 + Stage 3 done; lede slot marked HTML-comment for swap; body ~1,000w needs ~125–175w trim down to 750–900w for primary venues. When a news-peg surfaces, the turnaround target is **1–2 days from news → submission.**

Each activation prompt below is a self-contained paste-text for a fresh Claude session. Drop the news-event detail into the bracketed slot at the top; the session executes the rest.

**Discipline alignment.** v3.1 pipeline doctrine. The op-eds are short-form publisher-facing prose with a strong iterated draft already in hand, so the activation is a Stage-3-light cycle plus lede-swap plus cover-letter draft — NOT a full Stage 1 + Stage 2 + Stage 3 fire (that work has been banked).

---

## Op-ed A — Norway sovereign-wealth ("What Norway Proves About Resource Wealth")

**Source draft:** `publishing/op-eds/norway-sovereign-wealth/op-ed.md`
**Body word count:** 1,016 → target ~750–900 (Project Syndicate / Bloomberg primary) or hold ~900–1,000 (NYT / WaPo / Guardian stretch). Trim candidates pre-identified in source draft.
**Source chapter:** Ch 4 — *The Existence Proof* (Norway as institutional design vs. petrostate default)

### News-peg trigger types (any one fires)

| Trigger | Example forms | Best venue match |
|---|---|---|
| **Sovereign-wealth-fund news** | GPFG annual report; Alaska Permanent Fund draw-down debate; Alberta Heritage Fund news; any major fund's governance change | FT / Bloomberg / Project Syndicate |
| **Critical-minerals licensing** | DRC cobalt, Greenland rare earths, Chilean lithium, Indonesian nickel licensing decisions | FT / Bloomberg / Guardian |
| **Deep-sea-mining licensing** | International Seabed Authority decisions; Pacific island nation seabed announcements | FT / Guardian / NYT |
| **Petrostate transition event** | Saudi Aramco moves; Norway oil-production milestones; Guyana ExxonMobil license news | FT / Bloomberg |
| **UN / IMF / OECD resource-governance announcement** | Any institutional pronouncement on resource curse / extractive accountability | Project Syndicate / FT |
| **Equinor or GPFG portfolio decision** | Divestment announcements; ESG policy changes; major new investments | FT / Bloomberg |
| **Greenland / Arctic resource news** | Self-rule debates; resource-licensing news; geopolitical attention spikes | NYT / Guardian / FT |

### Paste-text for fresh session

```
You are a fresh session activating the Norway sovereign-wealth op-ed
for submission, triggered by this news event:

[PASTE 2–4 SENTENCES SUMMARIZING THE NEWS EVENT — what happened,
when, who's involved, what's the lede angle. Include a primary
source link if available.]

Target venue (primary):
[PICK ONE: Project Syndicate / Bloomberg Opinion / FT Opinion /
NYT Opinion / WaPo Opinion / Guardian Long Read]
Target word band:
[PICK ONE: 750–900 (PS/Bloomberg) | 900–1,100 (NYT/WaPo/Guardian)]

Your task in this session, in order:

1. READ:
   - publishing/op-eds/norway-sovereign-wealth/op-ed.md
     (canonical draft; ~1,016 words body)
   - publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md
     (canonical facts inventory — DO NOT DRIFT)
   - tools/memory/feedback_audience_aware_drafting_discipline.md
     (v3.1 discipline; this is a short-form pipeline-ready activation,
     not a full Stage 1+2+3 fire)
   - tools/memory/feedback_named_subject_consent.md
     (no living named subjects in this op-ed; verify)

2. SWAP THE LEDE (~80–100 words):
   - Replace the placeholder lede (marked HTML-comment "LEDE:
     news-peggable; current placeholder is generic") with a
     news-pegged opener that names the event.
   - Lede tone: matter-of-fact news observation that pivots into
     the universalizable question. Do not editorialize the event.
   - KEEP the nut graf intact — it states the argument and must
     survive any lede swap.

3. TRIM TO TARGET BAND (if primary band 750–900):
   - Pre-identified trim candidates: Alberta/Alaska comparator
     graf; second half of the existence-proof graf. Neither is
     load-bearing for the central argument.
   - Verify final word count.
   - PRESERVE: nut graf · the architecture-not-complicated
     paragraph · the discipline-required-to-maintain paragraph ·
     the vulnerability-targeting paragraph · the call graf.

4. STAGE 3 LIGHT RE-FIRE (single pass):
   - Fact-check: GPFG founded 1990, renamed 2006 (not 1990 rename);
     2001 fiscal rule (Stoltenberg I); successor administrations
     enumerated WITHOUT temporal-order error. Verify all numbers
     against canonical-facts inventory.
   - Voice-polish: read for em-dash overuse (per
     feedback_em_dash_overuse.md); check for LLM-cadence tics
     (rule-of-three, meta-commentary, hedge-stack openings).
   - Audience-load: pass against the op-ed audience set for the
     chosen venue (see tools/drafting-templates/audience-pressure-
     test-construction.md venue table).
   - Apparatus check: ZERO named framework terms (RCV, CIT, Cᵢ,
     Pattern 2, IPG, etc.). Concept must come through plainly.
   - Path B audit: ZERO verbatim sentences from Ch 4. Verify by
     grep against manuscript/chapters/Chapter__4_*.md.

5. DRAFT COVER LETTER / PITCH EMAIL:
   - Format per chosen venue's submission conventions.
   - 3–5 short paragraphs:
     (a) news-peg hook + the op-ed's central claim in one sentence
     (b) why this argument right now (timeliness)
     (c) author bio short-form (one sentence per author-bio doctrine)
     (d) AI-collaboration disclosure (per Aeon-precedent; venue-
         appropriate)
     (e) practical close (word count, exclusivity offered, response
         window comfort)

6. OUTPUT:
   - Updated op-ed body (with swapped lede + trimmed prose)
   - Cover letter / pitch email
   - 3-line submission checklist (portal URL, expected response
     window, diarized follow-up date)
   - Recommended commit message + git branch name
     (claude/op-ed-norway-activation-<harness-id>)

DO NOT submit. Author submits via portal.
DO NOT modify the canonical 2026-05-10 source draft. Save the
activated version as a sibling file with date suffix:
publishing/op-eds/norway-sovereign-wealth/news-peg-variant_<YYYY-MM-DD>_
activated_<news-peg-shortname>.md

Per CLAUDE.md merge-to-main default: this is a propose-only
activation (author ratifies + submits). Branch stops at feature
branch; do not auto-merge to main.
```

---

## Op-ed B — McDowell County true-cost ("What a Ton of Coal Actually Cost")

**Source draft:** `publishing/op-eds/mcdowell-county-true-cost/op-ed.md`
**Body word count:** 1,024 → target ~750–900 (PS/Bloomberg) or hold ~900–1,000 (NYT/WaPo/Guardian)
**Source chapter:** Ch 8 — *What Things Actually Cost* (full-cost accounting; coal-McDowell case)

### News-peg trigger types (any one fires)

| Trigger | Example forms | Best venue match |
|---|---|---|
| **EPA Social Cost of Carbon revision** | Any administration's revision (the article references the $190/ton 2023 figure as anchor) | NYT / WaPo / Project Syndicate |
| **Coal-company bankruptcy** | Liabilities transferring to public ledger; specifically black-lung-liability assumption | FT / Bloomberg / Project Syndicate |
| **Appalachian community cleanup announcement** | EPA / state actions on abandoned mine reclamation | WaPo (regional) / Guardian |
| **Mountaintop-removal regulatory ruling** | Court decisions; permit revocations or grants | NYT / WaPo / Guardian |
| **Major mine closure or coal-plant retirement** | Job-loss announcements; transition funding decisions | WaPo / FT / Bloomberg |
| **SCOTUS environmental-regulation decision** | West Virginia v. EPA-style major-questions doctrine cases | NYT / WaPo / Guardian / Project Syndicate |
| **Inflation Reduction Act / Justice40 implementation** | Funds reaching (or not reaching) Appalachian transition communities | WaPo / Bloomberg / Guardian |
| **Black Lung Disability Trust Fund news** | Funding crisis; legislative action; debt-projection updates | Bloomberg / WaPo |
| **Climate-damages litigation milestone** | Loss-and-damage proceedings; states-vs-fossil-fuels cases | NYT / Guardian / Project Syndicate |
| **Just-transition policy news** | Federal or state programs for coal-region transition | WaPo / Project Syndicate |

### Paste-text for fresh session

```
You are a fresh session activating the McDowell County true-cost
op-ed for submission, triggered by this news event:

[PASTE 2–4 SENTENCES SUMMARIZING THE NEWS EVENT — what happened,
when, who's involved, what's the lede angle. Include a primary
source link if available.]

Target venue (primary):
[PICK ONE: Project Syndicate / Bloomberg Opinion / FT Opinion /
NYT Opinion / WaPo Opinion / Guardian Long Read]
Target word band:
[PICK ONE: 750–900 (PS/Bloomberg) | 900–1,100 (NYT/WaPo/Guardian)]

Your task in this session, in order:

1. READ:
   - publishing/op-eds/mcdowell-county-true-cost/op-ed.md
     (canonical draft; ~1,024 words body)
   - publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md
     (canonical facts inventory — DO NOT DRIFT; this op-ed's
     numbers MUST match this inventory)
   - manuscript/chapters/Chapter__8_*.md (for Path B verification)
   - tools/memory/feedback_audience_aware_drafting_discipline.md
   - tools/memory/feedback_named_subject_consent.md (place name
     McDowell County is safe; no living named subjects in this
     op-ed — verify)

2. SWAP THE LEDE (~80–100 words):
   - Replace the placeholder lede (marked HTML-comment "LEDE:
     news-peggable; current placeholder is generic") with a
     news-pegged opener that names the event.
   - Lede tone: matter-of-fact news observation that pivots into
     the question of who paid the rest of the bill. Do not
     editorialize the event.
   - KEEP the nut graf intact — the $4.50-vs-$558 framing must
     survive any lede swap.

3. TRIM TO TARGET BAND (if primary band 750–900):
   - Pre-identified trim candidates: three-responses graf
     (cheap-energy-lifted-billions / markets-aren't-fake /
     not-pulling-the-ladder concessions can compress); McDowell-
     numbers paragraph (Walmart + 16th-poorest data lines can
     compress).
   - Verify final word count.
   - PRESERVE: nut graf · the Black Lung Trust Fund paragraph ·
     the reclamation paragraph · the carbon-arithmetic paragraph
     · the call graf.

4. STAGE 3 LIGHT RE-FIRE (single pass):
   - Fact-check: Black Lung Trust Fund cumulative >$44B; $4.5B
     debt 2021; projected >$15B by 2050; 633,000 acres awaiting
     reclamation; $3.8B bonds vs $7.5–9.8B documented need; 2.86
     tons CO₂ per ton coal; $190/ton SCC anchored to 2022 Nature
     meta-analysis + 2023 EPA update; ~$544 implied damage per
     ton coal; McDowell 1950 peak 100K; 2020 <20K; 1990 U.S.
     Steel mine closure cut personal income by two-thirds; 2016
     last Walmart left; 2022 16th-poorest US county; median
     household income ~$28K vs $67K national; poverty rate ~38%;
     2015 drug-induced death rate 141/100K. ALL must match
     canonical-facts inventory.
   - Voice-polish: em-dash audit; LLM-tic check (rule-of-three,
     meta-commentary); hedge-stack openings.
   - Audience-load: pass against the op-ed audience set for the
     chosen venue. Tier 1 dispositive audience: a Bloomberg/FT
     reader who shares the "markets aren't fake" intuition. The
     three-responses paragraph is built to address exactly this
     reader — verify it still does after trim.
   - Apparatus check: ZERO named framework terms. Concept comes
     through plainly via "accounting that priced one side of the
     ledger / a parallel transaction running alongside the
     priced one."
   - Path B audit: ZERO verbatim sentences from Ch 8.

5. DRAFT COVER LETTER / PITCH EMAIL:
   - Format per chosen venue's submission conventions.
   - 3–5 short paragraphs:
     (a) news-peg hook + the op-ed's central claim
     (b) why this argument right now (timeliness; full-cost
         accounting connection to the event)
     (c) author bio short-form (one sentence)
     (d) AI-collaboration disclosure
     (e) practical close (word count, exclusivity, response
         window comfort)

6. OUTPUT:
   - Updated op-ed body (swapped lede + trimmed prose)
   - Cover letter / pitch email
   - 3-line submission checklist
   - Recommended commit message + git branch name
     (claude/op-ed-mcdowell-activation-<harness-id>)

DO NOT submit. Author submits via portal.
DO NOT modify the canonical 2026-05-10 source draft. Save the
activated version as a sibling file with date suffix:
publishing/op-eds/mcdowell-county-true-cost/news-peg-variant_<YYYY-MM-DD>_
activated_<news-peg-shortname>.md

Per CLAUDE.md merge-to-main default: this is a propose-only
activation (author ratifies + submits). Branch stops at feature
branch; do not auto-merge to main.
```

---

## Standing news-peg watch (recommended setup)

To minimize the time from news → submission, set up news alerts now:

| Alert source | What to watch for |
|---|---|
| Google Alerts: "Government Pension Fund Global" + "GPFG" | Norway-fund news (Op-ed A) |
| Google Alerts: "Alaska Permanent Fund" + "Alberta Heritage Fund" | Sovereign-fund comparator news (Op-ed A) |
| Google Alerts: "International Seabed Authority" + "deep-sea mining" | Critical-minerals frontier (Op-ed A) |
| Google Alerts: "social cost of carbon" + "EPA SCC" | SCC revision news (Op-ed B) |
| Google Alerts: "Black Lung Disability Trust Fund" | Black-lung funding news (Op-ed B) |
| Google Alerts: "McDowell County" | Direct regional news (Op-ed B; high priority) |
| Google Alerts: "mountaintop removal" + "abandoned mine reclamation" | Coal-region regulatory news (Op-ed B) |
| Twitter/X list: energy/climate policy reporters | Real-time signal for both op-eds |
| Daily scan: Bloomberg Green section + FT Energy section | Editor-relevant news flow |

Setup time: ~15 minutes. Once alerts are running, the news → activation → submission window collapses to ~24 hours.

---

## Submission portals (pre-staged URLs)

| Venue | Portal | Notes |
|---|---|---|
| Project Syndicate | <https://www.project-syndicate.org/about/submissions> | Pitch-first; 4–6 wk response |
| Bloomberg Opinion | Editor-direct via published editor emails (no portal) | Pitch via email |
| FT Opinion | <https://aboutus.ft.com/community/opinion-pieces> | Pitch via email |
| NYT Opinion | <https://www.nytimes.com/section/opinion/submission-guidelines> | Highly selective; news-peg essential |
| WaPo Opinion | <https://www.washingtonpost.com/opinions/2018/03/05/submission-guidelines/> | Regional connection helpful for McDowell |
| Guardian Long Read | <https://www.theguardian.com/info/2015/may/06/the-guardian-long-read> | International scope helps Norway op-ed |

---

## Update log

- **2026-05-24.** Initial template. Sourced from existing op-ed drafts (2026-05-10, commit `5167edd`) + canonical-facts inventory + v3.1 pipeline doctrine + PM dashboard 2026-05-24 §6 op-ed activation framing.

---

*End of op-ed news-peg activation template.*
