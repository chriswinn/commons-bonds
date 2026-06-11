# Reverse-CSD model + Chesapeake oyster-reef calibration — Proposal Record (2026-06-08)

> ## 🔁 M3 PATH-A RECONCILIATION (2026-06-08, ratified by the M3-rework session — OVERRIDES this draft)
>
> The M3 rework ratified **Path A, NOT Path B** (the saturated handoff that seeded this draft said Path B; that
> was reversed). The following override the body below wherever they conflict:
>
> 1. **Backward-M3 KEEPS the multiplier architecture** (Path B's "single Dixit–Pindyck premium, drop the
>    multipliers" is RETIRED). Canonical form:
>    `CSD_M3 = V_option(extinguished optionality / foregone service flow) × scarcity_weight(ς) × irreversibility_weight(1/(1−α))`.
>    → Fixes §0-flag-1 and edit A1's Method-3 bullet (both currently describe backward-M3 in Path-B "single premium,
>    no multipliers" terms — WRONG).
> 2. **M2 is (c)-uniform: the realized-B reader in BOTH directions** — forward Norway = realized B₂; backward reef =
>    realized B₁ — preserving its "**revealed lower bound on RCV**" role. → Drops edit A3's "forward = independent
>    estimator" half; M2 is NOT a third independent estimator in either direction. It reads the realized bond and
>    thereby sets a revealed lower bound.
> 3. **Convergence is a bound-range — a matter of DEGREE, not KIND.** Do **NOT** assert "forward converges to a
>    point / backward yields a range" — that contradicts the symmetry theorems (Thm 10.1b, §17.5). → Edit A2's
>    "Backward triangulation does not inherit forward convergence" paragraph is WRONG and must be replaced with the
>    degree-not-kind framing. (NB: this is the exact symmetry-theorem tension my verification finding #3 flagged —
>    the M3 session resolved it the same way, in favor of preserving the theorems.)
> 4. **Notation/sourcing:** σ is renamed **ς** (final sigma); "irreversibility_premium" has **no β** (it = 1/(1−α));
>    cite **IPCC AR6 SPM B.5** + **Bernhardt & Palmer 2011** for the α (irreversibility) grounding.
> 5. **Reef (author decision 2026-06-08 — "bond only the unassailable floor"):** anchor the bond figure at the
>    **M1 cure-cost floor** (M2-corroborated); **name** M3 as the admitted *Open*-state ceiling (real and owed, a
>    lower-bound, not zero/unpriceable) but do **NOT** put a foregone-fishery number on paper for the reef. The
>    backward-M3 *method* is specified **generically in §5.5** (Path A multiplier form) and is load-bearing in the
>    **forward** cases — so M3's credibility is established there and the reef section never "shows-then-flinches."
>    The alternative (surface the reef M3 ceiling numerically) was explicitly considered and declined: it would put a
>    large contestable figure on paper and invite the argument the floor-only posture avoids. → §11.12 Method-3
>    subsection rewritten to this floor-only / named-not-priced form.
>
> These are recorded as overrides; the inline body spots (§0-flag-1, A1, A2, A3, §11.12-M3, bib) have been edited
> to match. The "review the M3 rework + the unpriceability approach + the M2 reframe once it lands" task is still
> pending the author's cue. — end Path-A reconciliation.

> ## ⚠️ VERIFICATION ADDENDUM (2026-06-08, independent re-investigation)
>
> The author flagged that the originating session + the CSD spec it produced were context-saturated and
> error-prone, and asked for independent confirmation that this work is needed and correctly directed —
> treating the spec, the session instructions, AND this proposal's body (sections A–H below) as unverified
> suggestions. I re-investigated against the actual TA, the actual chapters, and the actual sources (three
> independent agents + direct reads). Findings, in order of how much they change the plan:
>
> 1. **Two of the spec's core mandates target things that DO NOT EXIST in the TA.** A full backward-direction
>    census found **no "unpriceability theorem"** and **no "standing" apparatus-primitive** to remove. The only
>    "→∞" result (Thm 10.4 knife-edge) is forward-side and explicitly framed as a *feature* ("the divergence is
>    the correct answer"); the only "cannot price" statements (§12/§14.7 Europa) are an incommensurability-→-ARR
>    boundary unrelated to the backward direction; "standing" appears only as forward moral-grounding (Parfit/Sen)
>    + idiom ("has standing = is admissible"). So "remove the unpriceability theorem / remove standing" is
>    addressing phantoms. The *constraint* (do not ADD them) is fine and honored; the spec's framing that the
>    apparatus needs de-coercion surgery is false.
>
> 2. **The shipped Ch3 does NOT price the reef.** `Chapter__3_TheWaterman.md` (250 lines) is qualitative — the
>    99% decline, the reef-as-extracted-renewal-structure, "you have to put something back," restoration on the
>    public dime, "recovery without honest accounting for who paid." There is **no Restitution Bond dollar figure**
>    and **no "Method 3" / "foregone fishery decline."** The spec's quoted Ch3 line *"invites an argument I do not
>    need to have"* is **not in Ch3** (and the reef-numbers research file is explicitly dated "for author review
>    BEFORE Ch3 drafting"). **Consequence:** a TA §11.12 would be the FIRST place the $20–37M number appears,
>    ahead of any chapter — inverting the pipeline (the TA supports the book; it must not lead a number into print
>    that the book itself does not make). §11.12 should FOLLOW a priced Ch3 restitution section, not precede it.
>    The figure-cascade-coherence the spec demands has nothing on the Ch3 side to cohere with yet.
>
> 3. **The §5.5 rewrite has a much larger blast radius than the spec admits.** The current TA presents a
>    *coherent, internally consistent, and audit-"DELIVERED"* posture across ~9 locations (§1.7 L474, §1.10 L598,
>    §5.5 L1377–1441, §11.7, Thm 10.1b L3377, §17.5 L7623): "methodology is bidirectional & structurally
>    **symmetric**; this volume computes forward only **by design**; backward cases cited-not-computed." Flipping
>    ONE case to "computed" + asserting "backward yields a **range, not convergence**" directly **contradicts the
>    existing symmetry theorems** (Thm 10.1b "extends symmetrically"; §17.5 "bidirectional preservation... operates
>    symmetrically") unless ALL of them are reconciled. The spec touches only §5.5. **Lighter-touch alternative
>    (recommended):** keep the existing forward-by-design posture and add the reef purely as a *single worked
>    backward demonstration* ("proof of reach"), which needs far less reconciliation than a "range vs convergence"
>    redesign that fights the theorems.
>
> 4. **This proposal's own authorial-note draft (§F) is defective.** It uses *"those with standing to enter"* —
>    which (a) violates the spec's own no-standing rule and (b) deviates from the shipped authorial voice. The real
>    beats are Ch1:56 (*"a commute and a stolen life do not belong on the same line… Naming the rhyme is not the
>    same as making them equal"*; *"the ledger torn up and the person who kept it sold"*) and Atlantic essay :80
>    (*"Putting a price on the costs of coercion borne by a group I do not belong to is not mine to do… What the
>    framework offers is the ledger. What belongs on it, looking backward, is **theirs** to enter."*). Any TA note
>    must echo "theirs"/"those continuing it," NOT "standing." Also: this material already exists, beautifully, in
>    Ch1 + Ch5 + Atlantic; whether the *formal TA* needs a duplicate first-person note is a genuine author-call,
>    not a settled requirement.
>
> **VERIFIED SOLID (independently):** the Daly §14.6 fix (the current text genuinely *inverts* Daly — confirmed),
> and the reef arithmetic + external sourcing (all checks pass; AREA-not-volume; Hampton-Bar handled as honest
> James-River proxy; two immaterial nits: VA $21.77M vs $21.863M itemized, and $108M is the softest MEDIUM-confidence
> input).
>
> **REVISED RECOMMENDATION (what I actually agree should happen):**
> - **DO NOW (standalone, M3-independent, no dependencies):** the **Daly §14.6 fix** only. It's a clean
>   correctness repair worth shipping on its own merits.
> - **HOLD as working draft (do NOT apply):** §11.12 reef case + §5.5 reframe + authorial note. Gate them on
>   (a) M3 Path-B landing in `origin/main` (so reverse-M3 prose mirrors the corrected forward M3), AND
>   (b) Ch3 actually acquiring a priced restitution section (so the TA follows the book, not vice-versa).
>   When unheld, prefer the lighter-touch "single worked demonstration" framing over the "range-vs-convergence"
>   redesign, and reconcile the symmetry theorems explicitly if the range framing is kept.
> - **OPTIONAL tidy-ups (low value, low risk, anytime):** §5.6/L1447 open-question resolution; §17.7 generative
>   strengthening. Neither is load-bearing.
> - **DROP from the mandate:** "remove the unpriceability theorem" and "remove standing from the apparatus" —
>   there is nothing to remove.
>
> Sections A–H below are the ORIGINAL proposal, retained as the working draft they now are. Read them through the
> four findings above. — end addendum.

**Status: WORKING DRAFT (was: PROPOSED) — NO TA edits made.** See verification addendum above; most of this is gated.
**Branch:** `claude/ta-reverse-csd-260607-1efd85` (off held `claude/ta-rigor-audit-260606-f537b4`). Do NOT merge to main.
**Session:** Session F of the 2026-06-07 TA-audit plan (CSD reverse model + reef worked case — additive).

**What this is.** The backward/restitution counterpart to the forward RCV method, plus the worked Chesapeake
oyster-reef calibration. **Darity's 2026-05-14 version had NO reverse model** — this is the addition to offer him.
Built per the ratified spec `core/technical-appendix/CSD-computation-method-spec_2026-06-06.md`.

**Disciplines honored.** Every number sourced / derived-with-work-shown / labeled assumption; cite the EXTERNAL
authority, never our own table/ledger; no invented factual claims; sources added to the bib. NO "standing" in the
apparatus; NO unpriceability theorem; coercion handled by a first-person authorial note (visibly distinct from the
apparatus), not a formula term.

---

## 0. SEQUENCING + COORDINATION FLAGS (read first)

1. **M3 Path-B (Session D) is NOT yet applied on this branch.** The reef worked case (§11.12) is **M3-INDEPENDENT** —
   Ch3 *declines* Method 3 for the bond (the foregone fishery / option value is named as a gate-admittable ceiling
   variable the chapter chooses not to enter; the bond anchors at the cure-cost floor). So the reef calibration does
   not depend on the corrected forward M3 numbers and is safe to build now. **[PATH-A CORRECTED]** The §5.5
   reverse-model *description* of M3-backward must use the **Path-A multiplier architecture** —
   `CSD_M3 = V_option(extinguished optionality / foregone service flow) × scarcity_weight(ς) × irreversibility_weight(1/(1−α))`
   — NOT the Path-B "single premium, no multipliers" wording originally written here. It commits to **no** forward M3
   dollar number, so the reef floor stays M3-independent regardless. **Author/lead: confirm the M3-independence read
   before §11.12 applies.**
2. **Coordinate with the Ch3 chapter-drafting session.** The reef numbers ($20–37M floor / ~$200M central / >$92M MD /
   ~$110M Bay-wide) are Ch3's. After ratification, reconcile against `manuscript/chapters/Chapter__3_TheWaterman.md`
   and add to `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` so TA ↔ Ch3 ↔ any reef-touching essay stay aligned (figure-cascade
   discipline). This proposal does not yet touch the ledger or Ch3.
3. **All reef figures trace to EXTERNAL authorities** (Schulte 2017; NOAA Fisheries per-tributary table; Great Wicomico
   Tributary Plan §5; MD DNR/Office of the Governor Aug 2025; program-level reporting), verified in
   `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md`. Citations below name the external source, never
   the in-repo research file (which is the index, not the citation).

---

## A. §5.5 REWRITE — Bidirectional application (flip backward to computed-for-the-reef; range framing)

**What changes.** Current §5.5 (TA L1369–1448) declares the backward direction "outside this volume's empirical scope,"
applies a CIT "freedom-becomes-scarce → coercion-costs" move *inside the apparatus*, and frames the two directions as
structurally symmetric without flagging that backward yields a **range**, not a converged point. The rewrite: (a) flips
the backward direction to **computed for the ecological reef case**; (b) installs the floor + moving-ceiling **range**
framing; (c) states backward triangulation does **not** inherit forward convergence; (d) relocates coercion to a
first-person authorial note (§F below), removing it from the apparatus; (e) clarifies M2-as-comparator (audit E12).

**Edits:**

### A1 — Replace the "Backward application" paragraph (TA L1381–1386)

REMOVE the current paragraph beginning *"Backward application (structurally identical; outside this volume's empirical
scope)."* … through *"…applied to the realized-extraction case)."*

REPLACE WITH (HTML-ready):

```html
    <p>
     <strong>
      Backward application (computed for the ecological restitution case; human-coercion deferred).
     </strong>
     The same apparatus applies in reverse to price <em>Cost Severance Damages</em> (CSD) &mdash; the already-realized
     commons-loss of extraction that has already occurred. This volume computes the backward direction for one case the
     author is positioned to compute: the Chesapeake oyster-reef restitution case of Chapter 3 (worked end-to-end in
     &sect;11.12) &mdash; an <em>ecological</em>, not human-coercion, severance that is documented, bounded, and
     physically restorable. The Three Ways of Counting run in reverse and converge on a bound-range, as they do forward
     (degree, not kind &mdash; see below):
    </p>
    <ul>
     <li>
      <em>Method 1 (remediation / cost-to-cure)</em> prices the foreclosed commons extent &times; the realized
      restoration unit-cost (plus, where admitted, a bounded interval-services term for commons-services lost over the
      degraded interval). This estimates the <strong>CSD floor</strong> &mdash; the number a hostile reviewer cannot knock
      over, because every input is documented and realized. The interval term is bounded by construction, so Gate 3 is
      satisfied trivially.
     </li>
     <li>
      <em>Method 2 (revealed restitution)</em> reads what society has <em>actually paid</em> to restore comparable harm
      (natural-resource-damage settlements; public restoration programs). Backward, Method 2 is a <strong>comparator,
      not a third independent estimator</strong>: it does double duty &mdash; corroborating the Method-1 unit-cost, and
      revealing the <em>realized</em> B&#8321; (and who paid it). It is the realized-B reading of CS = RCV &minus; B,
      not an independent CSD computation.
     </li>
     <li>
      <em>Method 3 (scarcity-adjusted option value, uncertainty resolved)</em> prices the option value extinguished
      at the time of past extraction, evaluable from what is known now, via the same multiplier form the forward
      method uses (Path A): <code>CSD_M3 = V_option &times; scarcity_weight(&sigmaf;) &times; irreversibility_weight(1/(1&minus;&alpha;))</code>,
      where V_option is the extinguished optionality / foregone service flow. Backward it forks &mdash; ex-post
      realized value (a strict-liability reading) versus ex-ante correct-value-at-t&#8320; (a negligence reading); the
      framework <em>exposes</em> the choice rather than settling it. Backward, Method 3 is <strong>one admittable
      ceiling variable, not the bond basis.</strong>
     </li>
    </ul>
```

### A2 — Insert the range / floor-and-moving-ceiling architecture (new paragraphs after A1)

INSERT (HTML-ready):

```html
    <p>
     <strong>
      CSD is a structured range, not a single number.
     </strong>
     The lower bound is what can be proved; the upper bound moves with which cost variables are admitted and what values
     are entered. <code>CSD_floor = Method-1 cure-cost</code>, corroborated by Method-2 revealed restitution. The ceiling
     is generated by machinery the framework already contains &mdash; the Four Gates (&sect;7) admit which C&#7522; may
     enter; the Commons Inversion Test / Theorem 10.3 toggles each admitted cost from the $0 its commons&rsquo;s abundance
     masked to the $X scarcity makes legible; and the &sect;17 sum-of-costs generalization (<code>CS = &Sigma; C&#7522;</code>)
     is exactly this moving-ceiling machinery run backward:
     <code>CSD_ceiling = CSD_floor + &Sigma; (gate-admitted C&#7522;, including Method-3 option value, ecosystem-service
     heads, &hellip;)</code>. The framework&rsquo;s contribution is making the range &mdash; and exactly what drives its
     ceiling &mdash; explicit and gate-disciplined, not forcing consensus on one complete computation.
    </p>
    <p>
     <strong>
      Convergence is a bound-range &mdash; a matter of degree, not kind.
     </strong>
     The Three Ways converge on a bound-range in <em>both</em> directions; what differs between forward and backward is
     the <em>tightness</em> of that range, not its character. This preserves the symmetry the apparatus already asserts
     (Theorem 10.1b extends symmetrically to the CSD side; the &sect;17.5 bidirectional-preservation corollary operates
     symmetrically on both terms): it would be wrong to claim the forward direction converges to a single point while
     the backward direction yields a range &mdash; the honest statement is that each direction produces a range, and the
     backward range is typically wider because realized restitution-value estimation carries more
     methodological-choice spread (cf. the epistemic-asymmetry note below), not because the convergence logic is
     different in kind.
    </p>
    <p>
     <strong>
      Three states of a variable &mdash; never collapsed.
     </strong>
     A cost variable is in one of three states. <em>Zero</em>: under abundance the cost genuinely is $0 (the CIT toggle).
     <em>Filled</em>: someone enters a value (the reef floor). <em>Open</em>: a real, gate-admitted slot deliberately left
     empty. <strong>Open &ne; Zero &ne; Unpriceable.</strong> An unfilled admitted C&#7522; means the computed CSD is a
     <em>lower bound</em> &mdash; pure arithmetic, a sum missing a non-negative term. That is the only thing the
     mathematics says about an empty slot; it says nothing about why the slot is empty or who should fill it.
    </p>
    <p>
     <strong>
      CSD versus the Restitution Bond B&#8321;.
     </strong>
     CSD (true backward severance) is the range above; B&#8321; (the enforceable Restitution Bond actually posted) is
     anchored at the provable floor &mdash; you bond what you can prove, and the affected polity chooses where in the CSD
     range to set it. <code>(CSD &minus; B&#8321;) &gt; 0</code> measures how much unrestituted severance plausibly sits
     above the bonded floor. The bond does not invent a new bill: in the reef case the public already pays B&#8321;
     (~$110M, &sect;11.12) while the extractive industry&rsquo;s B&#8321; &asymp; $0. The instrument <em>reassigns</em>
     B&#8321; from the public back onto the value &mdash; value disperses up and out; cost stays local and falls to the
     public, in the algebra.
    </p>
```

### A3 — M2-is-the-realized-B-reader, uniform across directions (PATH-A / M3-session (c)-uniform reframe)

**[PATH-A CORRECTED — this supersedes the original "forward = independent estimator, backward = comparator" split.]**
Per the M3-session ratified (c)-uniform reframe, Method 2 plays the **same** role in both directions: it reads the
**realized Bond** and thereby sets a **revealed lower bound on RCV** — forward, Norway's GPFG is the realized B₂;
backward, the reef's public restoration spend is the realized B₁. It is **not** a third independent estimator in
either direction. Proposed one-line cross-reference clause where Method 2 is introduced in §11.6:
*"(Method 2 is the realized-Bond reader in both directions — forward it reads B₂ (Norway's GPFG), backward it reads
B₁ (see &sect;5.5, &sect;11.12); in each case it reveals a lower bound on the true value rather than acting as a third
independent estimator.)"* Exact insertion point at apply-time (the Method-2 heading within §11.6). **Low-risk relabel,
no number change.** This must also propagate into edit A1's Method-2 bullet (already written as realized-B reader —
consistent) and anywhere the draft called forward-M2 an "independent estimator."

---

## B. NEW §11.12 — Chesapeake oyster-reef restitution calibration (worked end-to-end)

**Placement.** After §11.11 (IPG reconciliation, TA L6258), before `</section>` closing §11. New id `sec-11-12-reef-csd`.
This is the first backward worked case, parallel to the forward §11.1–§11.6 cases.

**All numbers external-sourced; derivations shown. HTML-ready:**

```html
   <section>
    <h3 id="sec-11-12-reef-csd">
     &sect;11.12 &mdash; Chesapeake oyster-reef restitution calibration (CSD, backward direction)
    </h3>
    <p>
     The framework&rsquo;s first worked <em>backward</em> case: Cost Severance Damages for the Chesapeake oyster reef of
     Chapter 3 (the Restitution Bond case). It is the case the author is positioned to compute &mdash; an ecological,
     not human-coercion, severance; documented; bounded; physically restorable. It exercises the CSD range method of
     &sect;5.5: a provable Method-1 floor, corroborated by Method-2 revealed restitution, with Method 3 named as an
     admittable ceiling variable the chapter declines to enter.
    </p>
    <h4>
     Empirical anchors (James River / lower Chesapeake oyster reef)
    </h4>
    <table>
     <thead>
      <tr><th>Anchor</th><th>Value</th><th>Source</th></tr>
     </thead>
     <tbody>
      <tr>
       <td><strong>Foreclosed reef extent (James River high-quality oyster-rock, 1910&rarr;1981)</strong></td>
       <td>~2,738 acres (~1,108 ha): 7,047 ac &rarr; 4,309 ac, &minus;38.9%</td>
       <td>Schulte 2017, <em>Frontiers in Marine Science</em> 4:127, citing Moore (1910) and Haven et al. (1981)</td>
      </tr>
      <tr>
       <td><strong>Realized restoration unit-cost (Great Wicomico; natural-recruitment lower-Bay basis)</strong></td>
       <td>~$7,300/acre ($907,000 &divide; 124 ac)</td>
       <td>NOAA Fisheries, Chesapeake Bay oyster-reef restoration per-tributary table (as of Dec 31, 2024)</td>
      </tr>
      <tr>
       <td><strong>Forward-engineering construction unit-cost (light shell/stone on shell bottom, natural recruitment)</strong></td>
       <td>~$13,500/acre</td>
       <td>Great Wicomico River Oyster Restoration Tributary Plan, &sect;5 Cost Estimate</td>
      </tr>
      <tr>
       <td><strong>Bay-wide completed-program average (construction + seeding)</strong></td>
       <td>~$77,000/acre (~$92.82M &divide; 1,200 ac)</td>
       <td>NOAA Fisheries per-tributary table (as of Dec 31, 2024)</td>
      </tr>
      <tr>
       <td><strong>Public restitution already posted (Maryland, 5 sanctuaries, ~1,300 ac)</strong></td>
       <td>&gt;$92 million (state + federal)</td>
       <td>Maryland DNR / Office of the Governor, Aug 26, 2025</td>
      </tr>
      <tr>
       <td><strong>Public restitution already posted (Bay-wide, 10 tributaries)</strong></td>
       <td>~$108M (program-level) / ~$115M (NOAA itemized: MD $93.52M + VA $21.77M)</td>
       <td>NOAA Fisheries per-tributary table; program-level total as reported (10-yr bi-state program)</td>
      </tr>
      <tr>
       <td><strong>Extractive-industry contribution to that restitution</strong></td>
       <td>$0 (all funders public: NOAA, USACE, MD DNR, VMRC)</td>
       <td>Sources above (no oyster-industry funding identified)</td>
      </tr>
     </tbody>
    </table>
    <h4>
     Method 1 &mdash; CSD floor (cost-to-cure)
    </h4>
    <p>
     <code>CSD_floor = (foreclosed extent) &times; (realized restoration unit-cost)</code>. On the realized
     natural-recruitment basis: 2,738 ac &times; $7,300/ac = <strong>$19,987,400 &asymp; $20M</strong>. On the
     method-explicit forward-engineering basis (the better headline floor &mdash; primary-sourced, construction-only,
     honest for the lower-Bay Virginia geography where natural recruitment is reliable): 2,738 ac &times; $13,500/ac =
     <strong>$36,963,000 &asymp; $37M</strong>. A robust, cherry-pick-proof <em>central</em> figure using the bay-wide
     completed-program average: 2,738 ac &times; $77,000/ac = <strong>$210,826,000 &asymp; $200M</strong> (not the floor;
     the center). Every per-acre figure excludes surveys, planning, permitting, and monitoring &mdash; loading those in
     pushes the number up, so the floor only understates true cure-cost.
    </p>
    <p>
     <strong>Floor construction, not value-disgorgement.</strong> The Restitution Bond prices the cost to make the
     commons whole (the reef substrate the bond physically rebuilds), <em>not</em> the value extracted. The number is
     therefore built from foreclosed <em>area</em> &times; realized restoration cost-per-acre, not from harvested
     <em>volume</em>: raw shell is cheap and a volume construction collapses to a near-trivial figure (and the
     multiply-peak-output-across-the-full-run move is the corpus&rsquo;s single biggest adversarial vulnerability). The
     historical shell-mountain stays narrative; the dollar figure is area-built.
    </p>
    <h4>
     Method 2 &mdash; revealed restitution (corroboration + realized B&#8321;)
    </h4>
    <p>
     The reef rebuild is already underway and entirely publicly funded. Realized public restoration spend runs
     ~$57,000/acre (derived: ~$108M &divide; ~1,900 actively-restored acres &asymp; $56,800/ac) &mdash; which sits
     squarely between the $13,500 floor and the $77,000 average, independently corroborating the cost-per-acre band the
     Method-1 floor is built on. The realized B&#8321; already posted is <strong>&gt;$92M in Maryland alone, on the order
     of $110M bay-wide</strong> &mdash; all of it public; <strong>$0 from the extractive industry.</strong> Backward
     Method 2 thus does its double duty: it corroborates the Method-1 unit-cost <em>and</em> reveals the realized
     B&#8321; (and that it is mis-assigned to the public).
    </p>
    <h4>
     Method 3 &mdash; named as the admitted ceiling; the bond is anchored at the unassailable floor
    </h4>
    <p>
     The foregone fishery &mdash; the option value of all the oysters the foreclosed reef would have grown &mdash; is a
     gate-admittable ceiling variable. The bond is anchored at the <strong>M1 cure-cost floor</strong> (corroborated by
     M2): the polity bonds what is unassailable. Method 3 is <em>named</em> here as the admitted ceiling variable; in
     CSD terms it is the <em>Open</em> state of &sect;5.5 &mdash; an admitted slot deliberately left empty &mdash; so
     the true Cost Severance Damages are a <strong>range whose floor is bonded and whose ceiling, including the M3
     option value, remains real and owed</strong>. Leaving the slot empty makes the computed bond a lower bound; it is
     <em>not</em> a claim that the foregone fishery is worth zero or that it cannot be priced. The backward-M3 method
     itself is fully specified generically in &sect;5.5 (Path A:
     <code>CSD_M3 = V_option &times; scarcity_weight(&sigmaf;) &times; irreversibility_weight(1/(1&minus;&alpha;))</code>),
     so a party with reason to enter the slot can compute it; this case simply does not post the ceiling as the
     enforced figure.
    </p>
    <p>
     <em>Why this is a strategic decline, not a methodological one (per the 2026-06-08 author decision):</em> M3 is not
     declined because it cannot be computed for the reef &mdash; it can. It is declined as the <em>bonded</em> figure
     because anchoring the enforceable instrument at the provable floor is the stronger move ("bond only the
     unassailable floor"). M3's real-world weight is carried where it is load-bearing &mdash; generically in &sect;5.5
     and numerically in the forward cases (&sect;11.8 &alpha;-dominance; the IPG range's upper bound, &sect;11.11)
     &mdash; so the reef section never shows-then-flinches. Surfacing the M3 ceiling <em>numerically</em> for the reef
     was considered and declined: it would put a large, contestable foregone-fishery figure on paper and invite the
     argument the modest floor-only posture is designed to avoid.
    </p>
    <p>
     <em>Drafting note (verification finding #2):</em> the original draft attributed the phrase "invites an argument I
     do not need to have" to Ch3. That phrase is <strong>not in the shipped Ch3</strong>, and Ch3 currently prices no
     reef figure at all. Do not put an invented quote in the TA; describe the floor-only posture in the framework's own
     words, or wait for Ch3 to carry a priced restitution section and cite it then.
    </p>
    <h4>
     Formal note &mdash; renewable resource with extracted renewal-structure
    </h4>
    <p>
     The reef exercises the S_max / Theorem 10.3 machinery through destruction of the <em>regeneration function</em>
     (the reef substrate on which the next generation sets), not through drawdown of a fixed non-renewable stock as in
     the forward &sect;11 fossil-fuel cases. The foreclosed object is the renewal structure itself &mdash; a distinct
     formal object, and a feature of the framework&rsquo;s reach, not a strain on it.
    </p>
    <h4>
     CSD range summary (reef)
    </h4>
    <table>
     <thead>
      <tr><th>Quantity</th><th>Value</th><th>Basis</th></tr>
     </thead>
     <tbody>
      <tr><td>CSD floor (realized)</td><td>~$20M</td><td>2,738 ac &times; $7,300/ac (M1, natural-recruitment realized)</td></tr>
      <tr><td>CSD floor (forward-engineering headline)</td><td>~$37M</td><td>2,738 ac &times; $13,500/ac (M1, construction-only)</td></tr>
      <tr><td>CSD central (robust)</td><td>~$200M</td><td>2,738 ac &times; $77,000/ac (bay-wide average)</td></tr>
      <tr><td>CSD ceiling</td><td>floor + foregone-fishery option value</td><td>M3 admittable, chapter-declined (Open slot)</td></tr>
      <tr><td>Realized B&#8321; (mis-assigned to public)</td><td>~$92M (MD) / ~$110M (Bay-wide)</td><td>M2 revealed restitution; $0 industry</td></tr>
     </tbody>
    </table>
   </section>
```

**OPTIONAL narrative-context cell (AUTHOR CALL — include as numbers or keep qualitative).** Per the
ch3-restitution-bond-numbers ADDENDUM: one peak year of dockside (harvester-captured) value &asymp; 200,000 bu &times;
$35/bu &asymp; **~$7M** (MD DNR dockside basis, 2023–24; do NOT multiply ×~98 yr — same extrapolation trap). The
full retail-equivalent value the reef produced (~$120M/yr) dispersed up and out to packers/shippers/distant tables.
**This is NARRATIVE CONTEXT for the value-disperses-elsewhere thread, NOT the bond basis** (the bond basis is the
restoration COST, $20–37M). The ~$120M/yr is a current-price illustration of *where value landed*, not a historical
ledger (no defensible period price exists). If included, label both explicitly.

---

## C. §14.6 DALY FIX (also audit item 23)

**What changes.** TA L6609 currently asserts *"Where Daly argues normatively that S_max must equal 1 for strong
sustainability to be achievable…"* — this MISSTATES Daly. Daly's claim is: for **critical natural capital**,
substitutability S_max < 1, and therefore the **physical stock must be maintained** (substitution cannot do the job).
Load-bearing for the substitutability characterization the reverse model leans on.

REPLACE the "RCV relationship" sentence (TA L6609):

> *"Where Daly argues normatively that S_max must equal 1 for strong sustainability to be achievable, RCV asks
> empirically: what is S_max for each resource class?"*

WITH:

> *"Where Daly argues that for critical natural capital — resources whose substitutability S_max &lt; 1 — strong
> sustainability requires maintaining the physical stock itself rather than relying on substitution, RCV asks
> empirically: what is S_max for each resource class?"*

Rest of the paragraph (high-existential-gap resources; S_max < 1; RCV quantifies the resulting cost) is unchanged and
now reads consistently. Clean structural statement, no moral freight.

---

## D. §17.7 STRENGTHEN — explicit forward-looking generative claim

**What changes.** §17.7 (TA L7689–7705) states the generative property but only *implicitly* carries the forward-looking
claim that new contexts will surface new admissible variables. Making it explicit is what prevents any absent variable
(coercion included) from reading as "zero" or "the ledger is complete" — for *every* variable at once, so coercion is
never singled out. Value-free, standing-free.

INSERT a new paragraph after the "Third-party extension" paragraph (TA L7702), before "Relationship to the empirical
variable set":

```html
    <p>
     Forward-looking generativity.&nbsp;The framework&rsquo;s confidence is in the generativity of the method, not in the
     completeness of any list. As reality unfolds, new scenarios and contexts will surface cost variables that can, will,
     and should be admitted &mdash; each on the same gate discipline, none requiring methodology revision. An absent
     variable therefore never reads as "zero" or as "the ledger is complete": it is one not-yet-entered term among the
     many the method anticipates. This holds for every candidate variable at once &mdash; the posture is a property of
     the method, indifferent to which variable is in question and to who might enter it.
    </p>
```

(Mirror the same one-clause forward-looking strengthening into §5.5's empirical-scope discipline paragraph and/or §17.7's
cross-reference; the canonical statement lives here in §17.7.)

---

## E. §5.6 NEW — Restitution-direction moral grounding (B₁); resolve the L1447 open question

**What changes.** The TA logs an explicit open question (the "Coordination note" at L1443–1447): where should the
B₁-direction moral grounding live? Resolution per spec: deliver it through the **reparations-economics lineage + the
authorial note** — NOT a new theorem, NOT a standing claim. Promote it to a real subsection §5.6 and replace the
coordination-note with a pointer.

### E1 — REPLACE the L1443–1447 "Coordination note (B₁-direction moral grounding)" paragraph WITH:

```html
    <p>
     <strong>
      B&#8321;-direction moral grounding.
     </strong>
     &sect;5.4 grounds the B&#8322; (forward) direction (Parfit 1984 standing + Sen 1985/1999 valuation). The B&#8321;
     (backward) direction&rsquo;s moral grounding is given in &sect;5.6 below, delivered through the reparations-economics
     lineage and a first-person authorial scope-note &mdash; not through a new theorem or a standing claim.
    </p>
```

### E2 — INSERT new §5.6 after §5.5 closes (after TA L1448, before `</section>` at L1449):

```html
   <h3 id="sec-5-6-b1-moral-grounding">
    &sect;5.6 &mdash; Restitution-direction moral grounding (B&#8321;)
   </h3>
   <blockquote>
    <p>
     The B&#8321; (Restitution Bond) direction addresses already-realized, person-affecting harm. Its moral grounding is
     the person-affecting reading of Parfit (1984) &mdash; the wronging of specific persons &mdash; operationalized by
     the reparations-economics tradition (Darity &amp; Mullen 2020; Hamilton; Coates 2014; Anderson 2017). Where &sect;5.4
     grounds the forward direction&rsquo;s <em>impersonal-outcomes</em> evaluation (the goodness of future-generation
     states for whoever arises in them), &sect;5.6 grounds the backward direction&rsquo;s <em>person-affecting</em>
     evaluation (the restoration owed for harm realized against identifiable people and communities). The two readings of
     Parfit are not in tension: the framework adopts the impersonal reading forward (where the affected persons do not
     yet exist) and the person-affecting reading backward (where they do). The operational content of the B&#8321;
     grounding is the reparations-economics methodology already cited in &sect;5.5 &mdash; restitution as the material
     sub-type of redress in the Darity-Mullen typology (&sect;4) &mdash; not a new derived object.
    </p>
   </blockquote>
```

(Update the §5 table-of-contents / section-summary entries at TA L208-area to list §5.6, and the §5.4 heading need not
change. Mechanical at apply-time.)

---

## F. AUTHORIAL NOTE (coercion) — first-person, visibly distinct, outside the apparatus

**Placement (ratified by spec §9):** a brief first-person author&rsquo;s-scope-note at §5.5/§1.10, visibly distinct from
the apparatus (NOT a definition or theorem). It makes no framework claim, no standing claim, no unpriceability claim.

**Content is drawn from already-shipped chapter beats** (Ch1:56; Atlantic:80) — NOT invented. Exact wording is the
author&rsquo;s to ratify; proposed draft (HTML-ready, styled distinct from the apparatus blockquotes):

```html
    <aside class="authors-note">
     <p>
      <strong>A note from the author &mdash; first person, outside the apparatus.</strong>
     </p>
     <p>
      The method above defines slots, gates, units, and a sum. It says nothing about who may fill which slot. One slot it
      leaves open is the coercion vector &mdash; the cost of forced extraction, of a life taken rather than a commons
      depleted. I leave it open in this book deliberately, and the reason is mine, not the framework&rsquo;s: a commute
      and a stolen life do not belong on the same line, and naming the rhyme between them is not the same as making them
      equal. The mathematics does not declare that cost unpriceable &mdash; an open admitted slot only means the computed
      total is a lower bound. What belongs on that line, looking backward, is for those with standing to enter, the same
      way I decline to price fertile soil to an off-world colony two hundred thousand years hence, and for the same
      reason. The framework offers the ledger; what goes on it is theirs.
     </p>
    </aside>
```

This answers "you&rsquo;re pricing slaves like oyster reefs" without a special move: the framework prices *some* things
illustratively, claims no complete list, and asserts more variables will come (§17.7, §D); the author personally
declines to enter coercion in this book and says why.

### F1 — §1.10 Autonomy-boundary adjustment (AUTHOR CALL — softens the "methodologically unresolved → outside scope" hedge)

TA L598 currently frames coercion&rsquo;s absence as "remains methodologically unresolved in the reparations-economics
field … outside this volume&rsquo;s scope" — this reads close to an unpriceability hedge. Propose softening to the
open-slot framing + pointer to the authorial note, **keeping** the legacy-effects pathway as available-but-not-computed.
Proposed revision of the final two sentences of L598:

> *"The framework names the coercion variable at first introduction and extends to coerced-extraction cases through the
> legacy-effects pricing pathway (longevity gaps, wealth gaps, cultural-knowledge transmission disruption,
> intergenerational trauma; see §5.5). It does not enter a direct price for the coercion vector in this volume — an open,
> gate-admittable slot the author declines to fill, for the reason given in the author&rsquo;s note at §5.5. Per §5.5 and
> §17.7, an open slot means the computed total is a lower bound; it is neither a claim that the cost is zero nor a claim
> that it is unpriceable."*

Flagged as author-call because §1.10 is outside the spec&rsquo;s enumerated change-list (the spec names §5.5/§1.10 only
as authorial-note placement); include or hold per author preference.

---

## G. BIBLIOGRAPHY ADDITIONS (reef figure-backing; verified)

Add to `research/literature/bibliography.md` §23.1 (in-repo–vetted figure-backing). All verified in the
ch3-restitution-bond-numbers research pass; cite the external authority.

```markdown
- **Schulte, David M. "History of the Virginia Oyster Fishery, Chesapeake Bay, USA."** *Frontiers in Marine Science* 4:127 (2017). *Backs:* foreclosed James River high-quality oyster-rock extent ~2,738 ac (7,047→4,309 ac, −38.9%, 1910→1981; citing Moore 1910 / Haven et al. 1981); structural-vs-areal-vs-abundance loss distinctions (TA §11.12; Ch3). https://www.frontiersin.org/articles/10.3389/fmars.2017.00127/full Confidence: HIGH (peer-reviewed).
- **NOAA Fisheries. "Oyster Reef Restoration in the Chesapeake Bay: We're Making Significant Progress"** (per-tributary cost + acreage table, data as of Dec 31, 2024). *Backs:* realized restoration $/ac (Great Wicomico ~$7,300/ac = $907,000÷124 ac; bay-wide average ~$77,000/ac = ~$92.82M÷1,200 ac); Bay-wide itemized public spend ~$115M (MD $93.52M + VA $21.77M) (TA §11.12). https://www.fisheries.noaa.gov/chesapeake-bay/oyster-reef-restoration-chesapeake-bay-were-making-significant-progress Confidence: HIGH (agency).
- **Great Wicomico River Oyster Restoration Tributary Plan, §5 Cost Estimate** (Chesapeake Bay Program / partners, 2020). *Backs:* forward-engineering construction unit-cost ~$13,500/ac (light shell/stone on shell bottom, natural recruitment); ~$80,000/ac non-shell bottom; unit-price assumptions ($4/bu shell etc.) (TA §11.12 headline floor). https://d18lev1ok5leia.cloudfront.net/chesapeakeprogress/OysterRestorationBlueprintGreatWicomicoDec20.pdf Confidence: HIGH (primary plan doc).
- **Maryland DNR / Office of the Governor. "Governor Wes Moore Announces Completion of Maryland's Five Tributary-Scale Oyster Restoration Sanctuaries,"** Aug 26, 2025. *Backs:* realized public B₁ >$92M (state + federal) across ~1,300 ac / 5 sanctuaries; Manokin $21.6M (TA §11.12 realized restitution). https://news.maryland.gov/dnr/2025/08/26/governor-wes-moore-announces-completion-of-marylands-five-tributary-scale-oyster-restoration-sanctuaries/ Confidence: HIGH (agency).
- **Bi-state program-level total ~$108M over ten years** (NOAA, USACE, MD DNR, VMRC). *Backs:* "~$110M bay-wide public restitution" rounded figure (TA §11.12). Program-level as reported; corroborated by NOAA itemized ~$115M above. Confidence: MEDIUM (program-level reporting; cite the itemized NOAA table as primary, this as rounding corroborator).

**Backward-M3 α-grounding (PATH-A; shared with the M3-rework session's bib additions — do not duplicate):** the
irreversibility parameter α in `CSD_M3 = V_option × ς × 1/(1−α)` is grounded by **IPCC AR6 SPM B.5** (committed/
irreversible Earth-system change) + **Bernhardt & Palmer 2011** (stream-ecosystem irreversibility). Reuse the entries
the M3 session adds rather than creating parallel ones; this proposal only needs the cross-reference for §11.12's
fully-specified backward-M3 method.
```

(Optional, only if the dockside/value-dispersal narrative numbers are included per the §11.12 author-call: add MD DNR
dockside oyster price ~$35/bu, 2023–24 season, as the harvester-captured-value basis.)

---

## H. CHANGE SUMMARY (for the apply-time checklist, post-ratification)

| # | Edit | TA location | Class | Risk |
|---|---|---|---|---|
| A1 | §5.5 backward-application paragraph → reef-computed + 3-methods-in-reverse list | L1381–1386 | prose rewrite | med (load-bearing framing) |
| A2 | §5.5 insert range / three-states / CSD-vs-B₁ paragraphs | after A1 | additive prose | low |
| A3 | §11.6 M2-is-comparator one-liner (E12) | §11.6 M2 heading | relabel | low |
| B | New §11.12 reef calibration (worked) | after L6258 | additive worked case | med (arithmetic — re-audit) |
| C | §14.6 Daly fix | L6609 | correctness | low (fast ratify) |
| D | §17.7 forward-looking generativity paragraph | after L7702 | additive prose | low |
| E1 | §5.5 coordination-note → B₁-grounding pointer | L1443–1447 | relabel | low |
| E2 | New §5.6 B₁ moral grounding | after L1448 | additive prose | low |
| F | Authorial note (coercion) | §5.5/§1.10 | additive, distinct-styled | med (author voice — author ratifies wording) |
| F1 | §1.10 boundary softening | L598 | prose | author-call |
| G | Bibliography reef sources | bib §23.1 | additive | low |

**Final confirmation burst (post-apply):** re-audit §11.12 arithmetic ($19,987,400 / $36,963,000 / $210,826,000 /
$56,842 derivations); reconcile reef figures into `_CANONICAL_FIGURE_LEDGER.md` + Ch3; re-verify §5.5/§14.6/§17.7 edits
render clean (em-dash/entity tofu check, Stage 4).

---

## OPEN QUESTIONS FOR AUTHOR (resolve before applying)

1. **M3-independence of §11.12 confirmed?** (§0 flag 1.) The reef declines M3, so the worked case does not depend on the
   Path-B forward M3 rework. Confirm.
2. **Value-dispersal narrative numbers** (§11.12 optional cell): include ~$7M/peak-yr dockside + ~$120M/yr retail-dispersal
   as labeled numbers, or keep qualitative? (Bond basis stays the $20–37M restoration cost either way.)
3. **§11.12 headline:** lead with the $20M realized floor or the $37M forward-engineering floor? (Recommendation:
   "$20–37M floor, ~$200M central" per the ch3 research recommended line.)
4. **Authorial-note wording** (§F): ratify the proposed first-person draft, or supply author wording. (Drawn from Ch1:56
   + Atlantic:80; not invented.)
5. **§1.10 boundary softening** (§F1): apply, or leave §1.10 as-is and carry the open-slot framing only in §5.5?
6. **§11.12 section number:** §11.12 proposed (after §11.11). Confirm, or place as a new top-level (e.g. §11.B "backward
   cases") if the forward/backward distinction warrants a structural break in §11.

---

## Cross-references
- Spec: `core/technical-appendix/CSD-computation-method-spec_2026-06-06.md`
- Reef numbers + sources: `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md`
- M3 Path-B (Session D, not yet applied): `tools/audits/ta-m3-pathB-rework_proposal-record_2026-06-07.md`
- Resume/handoff: `tools/workstream-handoffs/ta-rigor-audit-resume_2026-06-07.md`
- TA: `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (§5.4 L1325, §5.5 L1369, §11 L3845, §14.6 L6603, §17.7 L7689)
- Ch3: `manuscript/chapters/Chapter__3_TheWaterman.md`; figure ledger: `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`
