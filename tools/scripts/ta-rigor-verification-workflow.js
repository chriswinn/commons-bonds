export const meta = {
  name: 'ta-rigor-verification',
  description: 'Technical Appendix math rigor: diverse-lens discovery, adversarial confirm, loop-until-dry, completeness critic → confirmed-findings ledger',
  whenToUse: 'Make the Commons Bonds Technical Appendix mathematically rock-solid before author review.',
  phases: [
    { title: 'Discover', detail: 'parallel diverse-lens finders re-derive numbers, check proofs, validate sources' },
    { title: 'Confirm', detail: 'adversarial refuters re-derive/re-check each candidate at source' },
    { title: 'Synthesize', detail: 'consolidate confirmed-only ledger with fixes + cascade locations' },
  ],
}

// ---- Inputs ----------------------------------------------------------------
const TA = args && args.taPath
  ? args.taPath
  : '/Users/c17n/commons-bonds-ta-rigor-audit-260606-f537b4/core/technical-appendix/TechnicalAppendix_v2.0.0.html'

// Section → line map (from header scan) to give finders precise targeting.
const SECTION_MAP = `
Section→line map (TechnicalAppendix_v2.0.0.html):
- §3.1 Core Formula 729; §3.2 IPG 752; §3.3 Method1 Replacement 767; §3.4 Method2 Revealed-Preference (Norway) 836; §3.5 Method3 Scarcity-Adjusted Option Value 875; §3.6 Triangulation 1035
- §4 Hotelling Identity 1127 (4.1 1148, 4.2 1162, 4.3 citation discipline 1190)
- §5 sub-instruments 1215; §5.4 Parfit/Sen grounding 1324
- §6.2 Seven Abundance Dimensions 1461; §6.7 Seven Walkthroughs 1814 (Walkthrough 1 McDowell Black-Lung 1868)
- §7 Four Gates 2519 (7.3 Boundedness/Integral Convergence 2713)
- §8 Asymmetric Regret Rule 2981
- §9 Three-Model 3042 (9.5 Convergence Table 3105, 9.6 Backtesting 3252)
- §10 Theorems & Proofs 3260: Thm10.1a CostSeverance 3265 (Proof 3301); Thm10.1b 3306 (Proof 3366); EmpObs10.2 Cross-Model Convergence 3392; Thm10.3 Abundance Masking 3422 (Proof(i) 3512, Proof(ii) 3518); Thm10.4 RCV Integral Convergence/Weitzman + knife-edge Corollary 3555 (Proof 3616, Corollary ~3671); Thm10.5 Substitution Dominance 3680 (Proof 3721, Hartwick extension ~3801); Corollary10.5.1 Optimal Extraction Sequencing 3811
- §11.1 McDowell Coal 3853; §11.2 Deepwater Horizon 3900; §11.3 Libby 3935; §11.4 Baotou 3967; §11.5 Norway calibration 4002; §11.6 McDowell calibration 4443; §11.7 CSD-RCV correlation 4910; §11.8 Method-3 sensitivity/α-dominance 5062; §11.9 DAC three-horizon 5407; §11.10 Space-economics anchors 5760; §11.11 IPG-table reconciliation 6199
- §12 Boundary-Awareness (Mars/Europa) 6260; §13 Resource Classification 6376
- §14 Literature Engagement 6523: 14.1 Hotelling 6533, 14.2 Hartwick 6547, 14.3 Weitzman 6561, 14.4 Rawls 6575, 14.5 Ostrom 6589, 14.6 Daly/strong-sustainability 6603, 14.7 Harvey 6614
- §15 Methodology Defense 6624; §16 Extensions (16.1 Weitzman var-discount 7334, 16.2 Stock-Dependent Substitutability 7346, 16.3 Spatial 7358, 16.4 Sensitivity Summary 7373)
- §17 Formula Generalization (Sum-of-Costs) 7525 (17.2 Formal Statement 7535, 17.3 Convergence Preservation 7568, 17.6 Worked Derivation 7625)
`

// ---- Seed findings (confirmed by two prior audits; confirmers RE-VALIDATE) --
const SEEDS = [
  { dedup_key: '11.8/scarcity_multiplier', section: '§11.8', claim: 'scarcity_multiplier stated ~6–7 contradicts the formula 1+log(1+σ)×0.05 (~1.3) and worked values 1.23/1.29.' },
  { dedup_key: '11.5/cs-reduction-label', section: '§11.5', claim: 'Norway "CS-reduction ~84%" mislabels the RESIDUAL (1−48/300); actual reduction ~16% (consistent with §11.7 "captured ~17%").' },
  { dedup_key: '11.1/carbon-510', section: '§11.1', claim: '2.61 × $190 = $496, stated $510; cascades to total $518–532 → $504–518 and §14.7 "$518".' },
  { dedup_key: '11.6/method1-combined-anchor', section: '§11.6', claim: 'Method-1 combined anchor $1,421–2,412 is LESS than its Habitability-only component $1,566–2,610 (forgot Ecosystem+Cohesion); correct sums $1,595–2,702 / $812–1,658 / $290–875; cascades lines 4827/4869/4871.' },
  { dedup_key: '11.1/ipg-without-carbon-label', section: '§11.1', claim: 'IPG "33–122× (without carbon)" label is backwards — that range requires carbon.' },
  { dedup_key: '11.9/dac-bands-intro', section: '§11.9', claim: 'Intro DAC bands ($600–1,200 / $150–500 / $100–200) mismatch canonical $600–1,000 / $300–600 / $100–300.' },
  { dedup_key: '11.9/falcon9-per-kg', section: '§11.9 / §11.10', claim: 'Falcon 9 $67M/22.8t = $2,939/kg, stated ~$2,700/kg.' },
  { dedup_key: 'global/log-natural', section: 'global', claim: '"log" never defined as natural log; every worked value requires ln.' },
  { dedup_key: '14.6/daly-inversion', section: '§14.6', claim: 'Inverts Daly\'s strong-sustainability logic (attributes S_max=1 to Daly).' },
  { dedup_key: '3.x/norway-vintage', section: '§3.4/§3.6 vs §11.5', claim: 'Norway vintage mismatch: §3.4/§3.6 use 50B BOE/$50/$12.5T vs §11.5\'s 55B/$48/$13.75T.' },
  { dedup_key: '11.2/deepwater-ipg-15-17', section: '§11.2', claim: 'Deepwater IPG 15–17× does not reproduce from $20–30B/$1.1B (~18–27×).' },
  { dedup_key: '3.6/mcdowell-m1-band', section: '§3.6 vs §11.6', claim: '§3.6 McDowell Method-1 $310–1,800 vs §11.6\'s derived band.' },
]

const KNOWN_FALSE_POSITIVE = 'Deepwater convergence "1.5× should be 1.75×" did NOT reproduce at source (the §11.2 ranges shown support 1.5×). Do NOT report it. The real Deepwater issue is the IPG-15-17× derivation.'

// ---- Schemas ---------------------------------------------------------------
const FINDINGS_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['findings'],
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['dedup_key', 'section', 'location', 'severity', 'claim', 'evidence', 'suggested_fix', 'cascade_locations'],
        properties: {
          dedup_key: { type: 'string', description: 'stable key like "11.8/scarcity_multiplier" — section/short-slug' },
          section: { type: 'string' },
          location: { type: 'string', description: 'line number(s) or anchor in the TA file' },
          severity: { type: 'string', enum: ['HARD', 'SOFT'], description: 'HARD = numerically/logically wrong; SOFT = imprecise/ambiguous/labeling' },
          claim: { type: 'string', description: 'what the TA currently asserts' },
          evidence: { type: 'string', description: 'the re-derivation / source check that shows the problem, with explicit arithmetic' },
          suggested_fix: { type: 'string' },
          cascade_locations: { type: 'string', description: 'other lines/sections that repeat the figure and must change too; "none" if isolated' },
        },
      },
    },
  },
}

const VERDICT_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['dedup_key', 'verdict', 'severity', 'reasoning', 'precise_fix', 'cascade_locations'],
  properties: {
    dedup_key: { type: 'string' },
    verdict: { type: 'string', enum: ['CONFIRMED', 'REFUTED', 'UNCERTAIN'] },
    severity: { type: 'string', enum: ['HARD', 'SOFT'] },
    reasoning: { type: 'string', description: 'the independent re-derivation at source (or re-fetch of external source) and whether it reproduces the problem' },
    precise_fix: { type: 'string', description: 'exact old→new for CONFIRMED; empty otherwise' },
    cascade_locations: { type: 'string' },
  },
}

// ---- Lens prompts ----------------------------------------------------------
const PREAMBLE = `You are auditing the Commons Bonds Technical Appendix for mathematical rigor — internal consistency AND external source-grounding. The file is the formal backbone of a book; correctness is the only goal. Read the file directly: ${TA}
${SECTION_MAP}
RULES:
- Re-derive EVERY figure from scratch; show your arithmetic in the "evidence" field. Do not trust the stated result.
- Report a finding ONLY when you can demonstrate the error. Distinguish HARD (numerically/logically wrong) from SOFT (ambiguous label/units/notation).
- Use a stable dedup_key "section/short-slug".
- KNOWN FALSE POSITIVE (do NOT report): ${KNOWN_FALSE_POSITIVE}
- If you find nothing in your lens, return an empty findings array. Do not invent problems.`

function lensPrompt(body, roundNote) {
  return `${PREAMBLE}\n\n${roundNote || ''}\n\nYOUR LENS:\n${body}`
}

const LENSES = [
  { key: 'rederive-mcdowell', body: `Internal number re-derivation — McDowell County coal. Re-derive EVERY figure in §11.1 (line 3853), §11.6 (4443), §11.7 (4910), and the §6.7 Walkthrough 1 (1868). Carbon: 2.61 t/ton? × SCC $190 → ?; per-ton total; the IPG multiples (33–122×, "with/without carbon"); Method-1 component sums (Habitability + Ecosystem + Cohesion) and the combined anchor band; Black-Lung healthcare cost. Flag every figure that does not reproduce, and every internal sum that is less than one of its own components.` },
  { key: 'rederive-norway', body: `Internal number re-derivation — Norway petroleum. Re-derive §11.5 (4002), §11.7 (4910), and cross-check §3.4 (836) and §3.6 (1035). Cumulative BOE, GPFG value, $/BOE, the "CS-reduction" / "captured %" figures (is the stated % the reduction or the residual 1−captured?), the $12.5T vs $13.75T totals, emission factors per BOE. Flag every vintage mismatch between §3.x and §11.5 and every reduction-vs-residual mislabel.` },
  { key: 'rederive-cases', body: `Internal number re-derivation — other case calibrations. Re-derive §11.2 Deepwater Horizon (3900): IPG from cleanup/settlement $20–30B vs annual pricing $1.1B → what multiple? does 15–17× reproduce? §11.3 Libby (3935) and §11.4 Baotou (3967): every settlement/damage figure and derived multiple. §9.5 Three-Model Convergence Table (3105) and §9.6 Backtesting (3252): does each convergence figure reproduce from its inputs?` },
  { key: 'rederive-space-dac', body: `Internal number re-derivation — space economics + DAC. §11.9 DAC three-horizon (5407): the intro bands vs the canonical/worked bands ($/ton CO₂ across near/mid/long horizons) — do they match? §11.10 space-economics anchors (5760): launch $/kg (Falcon 9 $67M / 22.8 t = ? ; any other vehicle), asteroid-miner calibration, any mass/cost/energy arithmetic. Flag every $/kg or band that does not reproduce.` },
  { key: 'proofs-theorems', body: `Proof / theorem rigor. For §10 (3260): Thm 10.1a, 10.1b, Empirical Observation 10.2, Thm 10.3 (+ proofs i/ii), Thm 10.4 (RCV integral convergence under Weitzman declining discount + knife-edge Corollary), Thm 10.5 (Substitution Dominance) + Corollary 10.5.1; and §17 generalization (7525). For EACH: does the proof actually ESTABLISH the stated claim, or does it (a) restate the premises, (b) assert a step without justification, (c) cite a theorem whose hypotheses are not verified (e.g. invoking dominated convergence where a domination/integrability bound is what's actually needed; monotone convergence misapplied; interchanging limit/integral without justification), or (d) prove something weaker than the headline? Flag over-claimed "theorems" (posited functional forms presented as derived), assumption-dependent dominance stated unconditionally, and any convergence claim whose integrability test is missing.` },
  { key: 'cross-section', body: `Cross-section consistency. Extract EVERY quantity that appears in more than one place (summary tables vs worked derivations; §11.11 IPG reconciliation 6199 vs §3.2/§11.1; §9.5 table vs §11 cases; figure cascade $4.70–4.85 mine-mouth / $496 carbon / $510 total / $504–518 floor / $518). List each quantity, its values at each location with line numbers, and flag every disagreement (including vintage mismatches and rounding that changes a downstream sum).` },
  { key: 'notation-units', body: `Notation + units + labels. Check: every symbol defined before first use (σ, τ, ξ, S, S_max, B, RCV, IPG, P, R, t₀, α, etc.); "log" specified as natural vs base-10 everywhere it appears (do the worked values require ln?); dimensional consistency of every formula (units on both sides); label accuracy ("with/without carbon", "reduction" vs "residual", "captured" vs "internalized", "gross" vs "net"). Flag each undefined-on-first-use symbol, each ambiguous log, each dimensional mismatch, each inaccurate label.` },
  { key: 'hostile-reviewer', body: `Hostile referee. You are a skeptical peer reviewer looking for the weakest points first. Attack: claims labeled "Theorem" that are really definitions or posited forms; functional forms (e.g. scarcity multiplier 1+log(1+σ)×0.05, substitutability S) dressed as derivations when they are assumptions; "dominance" results that secretly depend on parameter ranges; "convergence" across three models that may be selection/calibration artifacts rather than independent agreement; any place where the cited external authority (Hotelling, Hartwick, Weitzman, Dixit-Pindyck, Daly, Ostrom, Rawls, Parfit, Sen) is stretched beyond what it supports. Report the specific over-claims with the exact location.` },
  { key: 'external-validation', body: `External source validation. Use WebSearch / WebFetch (load via ToolSearch query "select:WebSearch,WebFetch" if not already available) to verify the empirical INPUTS against live authoritative sources, and report any TA figure that disagrees with the current authoritative value:
  - EPA social cost of carbon (TA uses $190/t CO₂ — is that the EPA 2023 central value?).
  - EPA AP-42 coal combustion CO₂ factor + Pocahontas-seam (bituminous) heat content (~28 mmBtu/short ton?) → does 2.61 t CO₂/ton reproduce?
  - GPFG (Norway Government Pension Fund Global) value (~$2.0T?) and cumulative Norwegian petroleum production (~55B BOE?) and oil/gas emission factors (0.43 / 0.31 t per BOE?).
  - Deepwater Horizon total settlement (~$20–30B? BP ~$65B all-in?), Libby/W.R. Grace settlement, Baotou figures.
  - DAC cost bands (Climeworks, Carbon Engineering, IEA, IPCC AR6) vs the TA near/mid/long bands.
  - Space-launch $/kg (Falcon 9, and any others cited).
  - Academic citations: confirm Hotelling 1931, Hartwick 1977, Weitzman 2001, Dixit-Pindyck 1994, Daly, Ostrom 1990, Rawls 1971, Parfit 1984, Sen — actually say what the TA cites them for (esp. §4 Hotelling Identity, §14.6 Daly strong-sustainability, §10.5 Hartwick extension).
  Report each input whose live authoritative value differs from the TA, with the source URL in "evidence".` },
]

function criticPrompt(seenKeys) {
  return `${PREAMBLE}

COMPLETENESS CRITIC. The audit has already surfaced findings with these dedup_keys: ${seenKeys.join(', ') || '(none yet)'}.
Your job: identify what CATEGORY of check has NOT been run, or what region of the file has been under-examined, and run it now. Consider: §12 Mars/Europa boundary claims; §13 resource classification; §15 methodology-defense numbers; §16 extensions (variable discount, stock-dependent substitutability, spatial, sensitivity summary); §5 sub-instrument definitions; §6.2 seven abundance dimensions arithmetic; §7.3 integral-convergence gate; any figure in a footnote or table not yet re-derived; any units/notation class not yet swept; any external input not yet validated. Re-derive/re-check whatever you target and report genuinely NEW findings only (different dedup_key from the list above).`
}

// ---- Run -------------------------------------------------------------------
const seen = new Map()
const confirmed = []
const refuted = []
const uncertain = []
let round = 0
const MAX_ROUNDS = 4

while (round < MAX_ROUNDS) {
  round++
  const seenKeys = [...seen.keys()]
  const roundNote = round === 1
    ? `ROUND 1 — full discovery sweep.`
    : `ROUND ${round} — these keys are already in the ledger, do NOT re-report them; look BEYOND them: ${seenKeys.join(', ')}.`

  phase('Discover')
  log(`Round ${round}: discovery burst (${LENSES.length} diverse lenses + completeness critic)`)

  const lensResults = await parallel(
    LENSES.map(L => () =>
      agent(lensPrompt(L.body, roundNote), { schema: FINDINGS_SCHEMA, phase: 'Discover', label: `r${round}:${L.key}` })
    )
  )
  const criticResult = await agent(criticPrompt(seenKeys), { schema: FINDINGS_SCHEMA, phase: 'Discover', label: `r${round}:critic` })

  const allFound = [
    ...lensResults.filter(Boolean).flatMap(r => r.findings || []),
    ...((criticResult && criticResult.findings) || []),
  ]
  // dedup vs cumulative ledger
  const fresh = []
  for (const f of allFound) {
    if (!f || !f.dedup_key) continue
    if (seen.has(f.dedup_key)) continue
    if (fresh.find(x => x.dedup_key === f.dedup_key)) continue // intra-round dup
    fresh.push(f)
  }

  // Round 1 also confirms the SEED findings (re-validated independently).
  const toConfirm = round === 1
    ? [...SEEDS.map(s => ({ ...s, location: 'see seed claim', severity: 'HARD', evidence: 'prior-audit seed — re-derive independently', suggested_fix: '', cascade_locations: '' })), ...fresh]
    : fresh

  for (const f of toConfirm) seen.set(f.dedup_key, f)
  log(`Round ${round}: ${fresh.length} fresh candidate(s)${round === 1 ? ` + ${SEEDS.length} seeds` : ''} → adversarial confirm`)

  if (toConfirm.length > 0) {
    phase('Confirm')
    const verdicts = await parallel(
      toConfirm.map(f => () =>
        agent(
          `${PREAMBLE}\n\nADVERSARIAL CONFIRMATION. A candidate finding is below. Your DEFAULT posture is to REFUTE it: independently re-derive the relevant numbers AT THE SOURCE in the file (or re-fetch the external source via WebSearch/WebFetch), and decide whether the problem is real. Verdict CONFIRMED only if your independent work reproduces the error; REFUTED if the TA is actually correct or the finding misreads it; UNCERTAIN only if genuinely undecidable after real work. For CONFIRMED, give the exact old→new precise_fix and ALL cascade locations (other lines repeating the figure).\n\nCANDIDATE:\n- dedup_key: ${f.dedup_key}\n- section: ${f.section}\n- location: ${f.location || 'n/a'}\n- claim: ${f.claim}\n- evidence offered: ${f.evidence || 'n/a'}\n- suggested_fix: ${f.suggested_fix || 'n/a'}`,
          { schema: VERDICT_SCHEMA, phase: 'Confirm', label: `r${round}:confirm:${f.dedup_key}` }
        )
      )
    )
    for (const v of verdicts.filter(Boolean)) {
      if (v.verdict === 'CONFIRMED') confirmed.push(v)
      else if (v.verdict === 'REFUTED') refuted.push(v)
      else uncertain.push(v)
    }
  }

  // Loop-until-dry: after round 1, a full burst + critic with zero fresh = done.
  if (round > 1 && fresh.length === 0) {
    log(`Round ${round}: dry (full burst + completeness critic surfaced nothing new). Stopping.`)
    break
  }
}

// ---- Synthesize ------------------------------------------------------------
phase('Synthesize')
return {
  rounds: round,
  confirmed_count: confirmed.length,
  refuted_count: refuted.length,
  uncertain_count: uncertain.length,
  confirmed,
  refuted,
  uncertain,
}
