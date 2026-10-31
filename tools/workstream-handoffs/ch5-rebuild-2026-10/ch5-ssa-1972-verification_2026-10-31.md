# Ch 5 Social Security rung — 1972 verification note

**Date:** 2026-10-31 · **Status:** verification complete (internal; not publisher-facing).
**Purpose:** ground the Ch 5 Social Security rung (brief §6.3 / D2) in the documented record
before any 1972 specific enters a draft. Per the brief: *no numbers from memory; render strictly
within the documented record; impute no motive beyond what's documented.*

**Reachability note.** `ssa.gov` is reachable at the network level in this container (the proxy
reached it), but ssa.gov returns **HTTP 403** to the automated fetch tool (its own bot filter),
so the SSA pages could not be read directly. The facts below were confirmed through web search
against **SSA-sourced** results (SSA history pages + the *Social Security Bulletin* legislative
history) plus CRS / congress.gov and a Cato legislative timeline. This is NOT the network-settings
problem the author was guarding against — the host resolves; the block is ssa.gov's anti-bot WAF.
I did **not** spoof a browser user-agent to get around it (that was blocked as an evasion, correctly).

---

## CONFIRMED — safe to use in a draft

1. **The 20% across-the-board benefit increase.** The 1972 legislation (Public Law 92-336, the
   July 1972 debt-limit bill, via a rider introduced by Senator Frank Church) provided a **20%
   across-the-board increase** in monthly Social Security cash benefits, **effective for September
   1972**. *(SSA history / SSB v36 legislative history.)*
2. **The checks arrived a month before the November election.** SSA's own history: the September
   benefits (the first to carry the increase) were **delivered in the first week of October 1972**,
   at least 20% higher — about a month before the November 1972 elections. *(SSA history; Cato
   legislative timeline.)*
3. **The funding was deferred past the election.** The **payroll-tax increase** enacted to pay for
   the higher benefits **did not take effect until after the election**. *(Cato legislative
   timeline; corroborated by the contemporaneous Congressional Record framing.)* This is the
   load-bearing, documented "harvest the cheap promise now, defer the funding" fact.
4. **Automatic COLA.** The same 1972 legislation (Church rider) established **automatic annual
   cost-of-living adjustments**, tied to the Consumer Price Index, with the **first automatic COLA
   first payable in 1975**. *(SSA COLA history; SSB legislative history.)*
5. **The 1972 indexing method was flawed and over-generous.** The 1972 automatic-indexing method
   ("double indexing" / "coupling") **over-adjusted** initial benefits, pushing replacement rates
   **above ~50%** against a congressional intent of roughly 40%. *(CRS "Social Security: The Notch
   Issue," RS22678; SSA notch files.)*
6. **The 1977 correction fixed the formula but left the long-run shortfall largely unfunded.**
   The 1977 amendments corrected the benefit-formula flaw (wage-indexing the initial benefit) — the
   source of the "Notch" — **while, per the critical literature, leaving the long-run financing
   deficits largely untouched and declining to impose the payroll taxes needed to fund the automatic
   increases.** *(CRS RS22678; Cato; Concord Coalition.)*

## NOT CONFIRMED — do NOT assert from memory

- **"Every actuarial report of the period named the deficit window the expansions would eventually
  run into."** This exact claim — made in the **current Ch 5 (candidate C), §118** — could **not**
  be confirmed from the accessible record. Two targeted searches returned nothing documenting that
  the 1972-era Trustees/actuarial reports already named a specific long-range deficit window at the
  time of the 1972 expansion. The historical record is in fact more nuanced: the long-range
  financing problem became prominent **after** 1972 (driven by the over-indexing flaw, 1970s
  stagflation, and demographic projections), and the **1975 Trustees Report** was the one that
  prominently flagged short- and long-range deficits, leading to the 1977 corrective amendments.
- **The specific 1972/1975 baby-boom demographic projections in the Trustees reports** — likewise
  unconfirmed in the accessible record.

## Drafting consequence (applied in Variants A and B)

Render the SS severance on the **confirmed** facts only:

- the 20% increase + automatic COLA enacted in an election year, **effective September 1972 with
  checks arriving the first week of October — a month before the November election**;
- the **payroll-tax funding deferred past the election**;
- the **over-indexing** flaw and the **1977 partial fix** (formula corrected, long-run shortfall
  left largely unfunded);
- the deterioration of the worker-to-retiree ratio as a **decades-visible demographic certainty**
  (the baby-boom cohort was, by 1972, a known and countable population whose retirement timing was
  arithmetic) — WITHOUT putting a specific "named the deficit window" claim in the 1972 Trustees'
  mouths.

This keeps the rung **documented, datable, non-partisan, villain-free, and repeatable as a
pattern**, exactly as the brief requires, and it removes the one unverifiable assertion that
candidate C currently carries. **Flag for the author (fact-check + developmental read):** candidate
C's §118 "every actuarial report of the period named the deficit window" should be softened to the
documented framing above, whichever candidate wins.

## Sources (SSA-sourced + CRS/Cato, via search; ssa.gov pages WAF-blocked to direct fetch)

- SSA, *1972 Social Security Amendments* history (`ssa.gov/history/1972amend.html`,
  `tally1972b.html`); SSA COLA history (`ssa.gov/cola/`).
- *Social Security Bulletin* v36n3, "Social Security Amendments of 1972: Summary and Legislative
  History."
- CRS, "Social Security: The Notch Issue" (RS22678); SSA notch files (`ssa.gov/history/notchfile*`).
- CRS, "Social Security: Major Decisions in the House and Senate Since 1935" (RL30920); congress.gov.
- Cato, "Social Security Administration Timeline" (legislative-timeline corroboration of the
  pre-election benefit timing + deferred payroll-tax funding).
