# RCV Block 1 — Two-Instrument Distinction and the Reparations Model Analysis — April 19, 2026

**Status:** Pending review

**Source:** April 19, 2026 session, File 2 (`archive/Consider Including/commons_bonds_new_material_april_19_2026 - Placeholder to consider for inclusion 2.html`), Block 1. Captured 2026-04-23 as a per-section pending-review item in `alignment/decisions/`.

**Integration target (if accepted):** Ch. 6 (Three Ways of Counting) + Technical Appendix RCV formal-model section. Connects to tier-structure decision (Tier 4 Dynastic Labor Cost + Tier 8 Knowledge-and-Culture Cost + any Autonomy-gap treatment).

**Priority:** High — this is the RCV formal-model session's core conceptual contribution.

---

## Two Proposed Starting Approaches

**Approach 1: Company Value Mapping (extractor-side).** The intuition: if the value was captured, it went somewhere, and you should be able to trace it. Map where the extracting company was, where it is now, and the delta represents captured value.

**Problems identified:** Corporate succession makes attribution nearly impossible at scale. The coal company that stripped an Appalachian hollow in 1940 may have been acquired in 1960, merged in 1980, gone bankrupt in 2000, and had its assets purchased by a private equity firm in 2010. The value didn't disappear — it was laundered through corporate structure until no single entity "holds" it in a traceable way. This is itself an instance of cost severance — the legal architecture exists specifically to sever accountability from the value chain. Even where you can trace a company (ExxonMobil back through Standard Oil), the attribution problem is severe: how much of current market cap traces to specific community extraction vs. refining innovation, global logistics, financial engineering, brand value?

**Assessment:** Useful as an illustration (a single coal company, a single community, well-documented extraction period), not as a generalizable pricing formula.

**Approach 2: The Reparations Model (community-side).** Instead of pricing the barrel forward into infinite future generations (the intractable problem), price the damage backward from the present. Calculate what it would actually cost to make whole every descendant of every person who bore the severed costs — shelter, food, clothing, education, healthcare — the full cost of human flourishing that the extraction economy failed to provide.

**What's clever about this:** It inverts the time-horizon problem. The forward-looking RCV calculation requires discounting across infinite future generations, and the choice of discount rate changes the answer by an order of magnitude (the Stern-Nordhaus debate: Stern used ~1.4%, Nordhaus used ~5%, answers differed by a factor of ten). The reparations model dodges this by looking at realized harm. The people already exist. The costs already happened. You're not projecting — you're measuring.

## Five Holes in the Reparations Model

**Hole 1: The Counterfactual Problem.** To calculate a reparation, you need a baseline: compared to what? If a coal miner's grandchild in McDowell County has worse outcomes than… who? The national average? The state average? Someone in a non-extraction community with otherwise similar demographics? Each choice produces a radically different number. Solvable — the reparations literature (Darity and Mullen's work is the landmark) uses wealth gap calculations against comparable households. A matched-comparison approach (extraction communities vs. demographically similar non-extraction communities, measured across generations) is methodologically defensible.

**Hole 2: Attribution.** These communities weren't shaped only by extraction. War, migration, technological change, federal policy (the interstate highway system, Medicare, the War on Poverty, the opioid crisis) all intervened. Isolating extraction's causal contribution from everything else over 150 years is econometrically brutal. Solvable via instrumental variables or natural experiments (communities on either side of a county line where one had coal and the other didn't), but requires real econometric skill.

**Hole 3: The Demographic Branching Problem.** Tracking descendants creates an exponentially growing, intermingling population. A coal miner's granddaughter marries a farmer's grandson — is their child in or out? Within 3–4 generations, the affected population is so diffuse that the boundary becomes meaningless. A place-based model (what happened to McDowell County as a whole) avoids this but loses the moral force of the individual reparation claim.

**Hole 4: The Unlived-Lives Infinity.** Many people died before having children, or their children died before reproducing. Those unlived lives represent permanently foreclosed human potential — structurally identical to the permanently foreclosed resource. You can't price an unborn lineage any more easily than an unextracted barrel across infinite time. The reparations model encounters the exact same infinity problem it was trying to avoid — just in human generations rather than resource generations.

**Hole 5 — The Critical Distinction:** The reparations model measures *cost severance damages*. It does NOT measure *residual commons value*. These are two distinct concepts, and the model only captures one. You could fully compensate every descendant of every Appalachian coal miner — make them whole on health, education, housing, income — and the coal is still gone. The resource is still permanently foreclosed. The reparations model prices what was done to *people*. Residual commons value is about what was done to the *resource itself* and its permanent unavailability to all future uses and users. A community could receive perfect reparations and the residual commons value could still be entirely unpriced. They're orthogonal quantities.

## The Two-Instrument Conclusion

The framework actually needs two separate instruments:

**Instrument 1: Cost Severance Damages** — the reparations model, backward-looking, measuring realized human harm. Draws on existing reparations economics, health economics (Value of Statistical Life, Disability-Adjusted Life Years), and intergenerational mobility research. Methodologically hard but not unprecedented.

**Instrument 2: Residual Commons Value** — the forward-looking permanent foreclosure price. The harder, more original problem. This is where the triangulated estimation framework (see `april-19-rcv-triangulated-estimation.md`) applies.

**Cross-validation idea:** If CSD and uncaptured RCV are *correlated* across cases — if communities bearing higher severed costs also sit on top of higher permanently foreclosed resource value — that would be a genuinely important empirical finding. It would mean the two problems aren't just conceptually related; they're structurally linked. That correlation, if it holds, is the formal model's deepest claim: cost severance and residual commons value are two measurements of the same underlying extraction event, taken from different directions.
