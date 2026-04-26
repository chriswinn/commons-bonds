---

# Commons Bonds

By Chris Winn

---

Chapter 7 (The Colony Administrator)

========

========

Objections

========

========

---

Chapter 7 (The Colony Administrator): The "Mars is a false analogy" objection belongs here, right after the universality claim. Address it within the chapter as a natural complication. One to two pages.

---

CHAPTER 7: THE COLONY ADMINISTRATOR

From our conversations, what lives here:

The Mars thought experiment:

- Colony of 10,000 people, three water ice deposits, 50-year supply at current consumption
- Walk through the RCV framework applied to Mars water: S ≈ 0, U is life-or-death, Q is small and fixed, D is near zero
- The model produces the obviously correct answer: strategic reserves, progressive pricing, aggressive investment in recycling

The pivot paragraph: "Earth is also a bounded system..."

The universality test — all cross-scenario results:

Asteroid iron mining: RCV near zero, extract freely. The model says "this is the cheapest extraction possible."

Lunar helium-3: conditionally high CSG, preserve (insurance is free). The model says "wait — the downside of unnecessary preservation is zero."

Lunar regolith: RCV near zero, extract freely. Same body, different resource, different answer. The model differentiates correctly within a single location.

> **2026-04-24 Phase A3 sweep header:** This guidance doc preserves "asymmetric regret" framing throughout (the underlying concept). Per ARP rename rigor pass commit `b8b62e3` ratified 2026-04-24, the formal name is now **Asymmetric Regret Rule (ARR)** — last-word "Principle" → "Rule" downgrades overclaim while preserving regret-theory direct lineage. References to "asymmetric regret principle" below should mentally substitute "Asymmetric Regret Rule" or the lowercase phrase "asymmetric regret" depending on context. AIT references in this doc renamed to CIT (Commons Inversion Test) per commit `b294c79`. Both renames preserve underlying decision-theoretic + admission-test content unchanged.

Comet flyby: extract aggressively. The access window closes permanently. The asymmetric regret flips. The model is not anti-extraction — it says "extract when RCV is low and preservation isn't an option."

Mars colony rare earths: cost severance goes to zero because the extractor and the affected community are the same people. The deepest insight: cost severance requires distance.

Europa ice: the model hits its boundary. The externality of potentially destroying an independent biosphere is incommensurable. The model honestly says "I can't price this. The asymmetric regret principle applies: wait, study, decide later."

Exoplanet rare earths (the extreme test): genuine tension between low S (you need the resource) and high E (ecosystem disruption). The model resolves it: "extract if necessary, but with extreme accountability and minimized footprint."

The "cost severance as a function of distance" insight: Mars compresses the distance between beneficiary and cost-bearer to zero, which eliminates cost severance automatically. On Earth, distance — geographic, temporal, social — enables the ignorance that enables severance. The model prices what distance hides.

The CSG ranking system:

- CSG ≈ 0: coal, sand, iron ore, common stone
- Low CSG: conventional oil, copper, zinc
- Moderate CSG: uranium, lithium, cobalt
- High CSG: rare earths, platinum group metals
- Conditionally high CSG: helium-3

The insurance cost argument: In-situ preservation (leave it in the ground) is nearly free. The insurance cost for most critical minerals is single-digit percentages of total extraction revenue.

The appreciating reserve: Value increases as non-reserved stocks deplete, peaks during the maximum-scarcity period, depreciates only when substitution succeeds and the danger passes. A hedge that costs nothing to hold and pays off exactly when needed.

The asymmetric regret, stated simply: "We can always extract later. We can never un-extract."

Counterarguments woven in:

"Mars is a false analogy." Address it. The complexity objection — Mars is simple, Earth is complex. Response: the structure is the same, the parameters differ, and using a limiting case to illuminate the general case is standard scientific method. One to two pages.

"On an uninhabited asteroid, your model reduces to market pricing." Accept it and reframe as a strength: the model shouldreduce to market pricing when externalities are zero and stocks are abundant, because in those conditions market pricing is correct. The model adds value where market pricing fails and correctly reduces to market pricing where it doesn't. That's not a weakness. That's a well-calibrated instrument.

How to handle this: Register 1 (the Mars thought experiment is a story) transitioning to Register 2 (the cross-scenario results presented as a structured analysis with a summary table). The CSG ranking is a Register 2 concept presented with a Register 1 entry: "Not all resources matter equally for the far future. Some — coal, sand — can be extracted freely with proper externality pricing. Others — the rare earths in your phone, the platinum in a catalytic converter — might be the materials our grandchildren need to leave the planet."

========

========

I think you possibly already have from what you wrote. But just to be sure. Tell me what happens when you apply this model to miners mining rare earth to common things on a comet, on a planet, on a moon, on Mars, etc. I want to make sure it stands up to rigorous cross testing.

========

========

Architected systematic testing across multiple extraterrestrial mining scenarios

Architected systematic testing across multiple extraterrestrial mining scenarios

Let me run this systematically across every scenario I can construct, varying the body type, the resource type, the presence or absence of life and community, and the extraction purpose. I'll track what happens to each term in the model and flag anywhere the model breaks or produces a counterintuitive result.

The formula under test:

RCV = ∫ { [1 - S(t)] · U(R, t, Q(t)) + E(R, t) } · D(t) dt

CS = RCV - B

And the practical instruments: CSG ranking, insurance cost, asymmetric regret, spatial cost severance.

---

SCENARIO 1: Mining Common Iron from an Uninhabited Asteroid

Body: Near-Earth asteroid, ~500 meters diameter

Resource: Iron-nickel, abundant in this class of asteroid

Life: None

Community: None

Purpose: Industrial feedstock for orbital construction

Term-by-term analysis:

S(t): High. Iron is substitutable for most applications. Other asteroids contain iron. Earth contains abundant iron. S\_max ≈ 1 for virtually all applications.

U(R, t, Q(t)): Moderate and not strongly stock-dependent. Iron is abundant across many asteroids. Extracting from this particular asteroid doesn't meaningfully reduce the total accessible stock because thousands of similar bodies exist.

E(R, t): Near zero. No atmosphere to pollute. No water table to contaminate. No ecosystem to disrupt. No community to displace. No workers breathing dust (assuming robotic mining). The only externalities are debris generation (orbital mechanics concern) and energy consumption of the mining operation itself.

D(t): Standard — no special reason to weight near-term or far-future generations differently for this extraction.

RCV result: Very low. Approaching the market price of the extracted material. The IPG is near 1. This is the lowest-RCV extraction possible in the model.

CS result: Near zero if any reasonable accountability bond is posted (cleanup of debris, energy accounting).

CSG: Zero. Iron from asteroids has no existential substitutability gap.

Does the model produce the right answer? Yes. Asteroid mining of abundant materials from lifeless bodies should be the cheapest form of extraction in a properly priced economy. The model confirms this. It says: "extract here first." That's correct.

What if we change the resource to something rare? If this particular asteroid contains an unusually concentrated deposit of platinum group metals found nowhere else in the accessible solar system, Q(t) shrinks dramatically, U increases, and S(t) for that specific composition drops. RCV rises. The model correctly differentiates between abundant asteroid iron (low RCV) and unique asteroid platinum (higher RCV). The model holds.

---

SCENARIO 2: Mining Water Ice on Mars (Uninhabited, Pre-Colony)

Body: Mars, before any human settlement

Resource: Subsurface water ice deposit

Life: None confirmed (but possible subsurface microbial life)

Community: None

Purpose: Prospecting and caching for future human use

Term-by-term analysis:

S(t): Very low on Mars. Water cannot be synthesized economically. There is no substitute for water in life support. S\_max is well below 1 for biological applications. Some substitutability exists for industrial applications (certain chemical processes can use other solvents), but for drinking, agriculture, and oxygen generation, S ≈ 0.

U(R, t, Q(t)): Extremely high and sharply stock-dependent. If there are only three accessible ice deposits on Mars, each unit from any deposit is enormously valuable. U spikes as Q decreases because you're approaching the hard floor below which the future colony cannot survive.

E(R, t): This is where it gets interesting. If Mars has no life, environmental externalities in the terrestrial sense are zero — no ecosystem to damage. But there are habitability externalities: extraction that contaminates the remaining ice with drilling chemicals, or that destabilizes the geological formation, or that releases subsurface volatiles. These are potentially severe because they reduce the usability of the remaining stock.

And there's a deeper externality question: what if Mars has subsurface microbial life? If extraction destroys the only other example of life in the known universe, E(R, t) becomes almost impossible to price — the scientific and philosophical value of confirming extraterrestrial life is incalculable.

D(t): Should be very low (near-zero discount rate). The colony's survival depends entirely on long-term resource availability. Discounting the future heavily on Mars is suicidal.

RCV result: Extremely high. The combination of near-zero substitutability, high stock-dependent utility, potential habitability externalities, and low discounting produces an RCV per unit that is orders of magnitude above extraction cost.

CS result: Under any accountability regime that doesn't incorporate the full intergenerational life-support value of the water, CS is enormous.

CSG: Maximum. Water on Mars is the highest-CSG resource conceivable — zero substitutability for the most essential application (staying alive).

Does the model produce the right answer? Yes. Any rational Mars planning authority would treat water ice deposits as the single most valuable asset on the planet, subject to the most stringent conservation, rationing, and strategic reserve protocols imaginable. The model produces exactly this recommendation.

Interesting finding: The model reveals that the first resource decision on Mars — how to manage water — is the purest possible test case for the framework. Every parameter is at its extreme value. S ≈ 0, U is life-or-death, Q is small and fixed, E includes potential destruction of extraterrestrial life. If the model works here (and it does, producing the obviously correct answer), it works everywhere.

---

SCENARIO 3: Mining Rare Earths on Mars (Inhabited Colony, 10,000 People)

Body: Mars, established colony

Resource: Rare earth deposit discovered near colony

Life: Human colony, possibly native microbial life

Community: 10,000 colonists

Purpose: Manufacturing electronics and equipment locally rather than importing from Earth

Term-by-term analysis:

S(t): Low for local manufacturing (no alternative local source), but moderate if you include Earth imports as a substitute. The question is whether you treat Earth supply as a substitute or not. If the colony can import rare earths from Earth, S(t) is moderate. If supply lines are disrupted (war, economic collapse, orbital mechanics limiting launch windows), S(t) drops to near-zero.

This reveals something important: substitutability is supply-chain dependent. On Earth, S(t) for any given mine's output is high because you can import from other mines. On Mars, S(t) for the local deposit depends on the reliability of interplanetary supply chains. The model correctly captures this — S(t) is a function of accessible alternatives, not just theoretical alternatives.

U(R, t, Q(t)): High. Local rare earths mean local manufacturing capability, which means reduced dependence on Earth supply. The strategic value exceeds the market value.

E(R, t): Here we get spatial cost severance on Mars. If the mine is near the colony, dust generation threatens habitat air filtration. Chemical processing creates waste that must be managed in a closed system (you can't dump tailings "somewhere else" on Mars the way you can in Mongolia — there's only one settlement). Worker health in a pressurized environment with limited medical resources is a severe concern.

The colony experiences every externality directly and immediately. There is no "somewhere else" to sever costs to. This is the key insight: spatial cost severance is impossible on Mars because the extraction community and the consuming community are the same people.

D(t): Low. The colony's planning horizon is intergenerational by necessity.

RCV result: High, driven primarily by supply-chain-dependent substitutability and the impossibility of spatial cost severance.

CS result: If the colony's governance prices the extraction honestly (which they must, because they bear all costs directly), CS should be near zero — not because the costs are low, but because B (the accountability bond) naturally equals RCV when the extractor and the affected community are the same entity. You can't sever costs onto yourself.

Does the model produce the right answer? Yes, and it reveals something profound. Cost severance requires distance — spatial, temporal, or social distance between the entity capturing value and the entity bearing costs. On Mars, that distance is compressed to zero. Everyone breathes the same recycled air. Everyone drinks the same recycled water. The CEO of the mining operation and the family living downwind are probably neighbors. Cost severance cannot operate in this environment.

This means: The model predicts that a Mars colony would automatically develop full-cost pricing — not because they read Commons Bonds, but because the physics of their situation makes cost severance impossible. The costs can't be hidden because there's nowhere to hide them.

And this tells us something about Earth: cost severance is a function of distance. The reason McDowell County bore the costs of national coal consumption is that the consumers were thousands of miles away and never visited. The reason Baotou villagers bear the costs of global smartphone production is that the consumers never see the toxic lake. Cost severance requires ignorance, and ignorance requires distance.

The model doesn't just price resources. It prices distance — the distance between those who benefit and those who pay.

---

SCENARIO 4: Mining Helium-3 on the Moon

Body: Lunar surface

Resource: Helium-3, embedded in regolith by solar wind over billions of years

Life: None

Community: None (or small research outpost)

Purpose: Fuel for hypothetical fusion reactors

Term-by-term analysis:

S(t): Complex and time-dependent. Currently, helium-3 fusion doesn't work — no reactor has achieved net energy from He-3 fusion. So the resource has near-zero current utility. But if deuterium-helium-3 fusion is achieved, He-3 becomes potentially the most valuable energy source in the solar system — clean fusion with minimal neutron radiation, ideal for spacecraft propulsion.

This creates a fascinating S(t) profile: for the current application (none), S = 1 (you don't need a substitute for something you're not using). For the potential future application (fusion fuel), S is near zero (no substitute for He-3 in He-3 fusion by definition). The substitutability depends on which application you're pricing.

U(R, t, Q(t)): Near zero today. Potentially enormous in the future. The utility function has a phase transition — it jumps from near-zero to very high at the moment fusion becomes viable. Q is large (the Moon's regolith contains an estimated 1 million tons of He-3), but extraction is energy-intensive (you must heat regolith to 600°C+ to release the He-3).

E(R, t): Low but not zero. Large-scale regolith processing disturbs the lunar surface, creates dust hazards for equipment and potential future settlements, and permanently alters the lunar landscape. For a research outpost, the externalities are manageable. For industrial-scale processing of thousands of square kilometers of regolith, the externalities become significant.

There's also a cultural and scientific externality: the Moon has scientific value as an undisturbed geological record of 4.5 billion years of solar system history. Large-scale mining destroys that record.

RCV result: This depends entirely on the probability of He-3 fusion becoming viable. If P(fusion) is near zero, RCV is near zero — you're pricing a resource with no current use and no foreseeable use. If P(fusion) is significant (say, 10-30% within the next century), RCV jumps to very high levels because you're pricing the potential fuel source for interstellar travel.

Does the model handle this correctly? Yes, but it reveals a limitation: for resources whose value is entirely contingent on a future technological breakthrough, the model's output is only as good as the probability estimate for that breakthrough. The model correctly says "the answer depends on P(fusion)" — it doesn't pretend to know what P(fusion) is.

CSG result: High but uncertain. He-3 has maximum existential relevance if fusion works. Zero relevance if it doesn't. The CSG ranking should reflect this uncertainty: "conditionally high CSG, contingent on fusion viability."

Practical recommendation from the model: The insurance cost of preserving lunar He-3 is nearly zero — it costs nothing to not mine the Moon. The asymmetric regret applies perfectly: if we preserve He-3 deposits and fusion never works, we've lost nothing (the Moon is still there, unchanged). If we mine it all for some other purpose and fusion later becomes viable, we've lost a potentially irreplaceable fuel source. The preservation decision is trivially easy under asymmetric regret, regardless of P(fusion).

---

SCENARIO 5: Mining Common Regolith on the Moon for Construction

Body: Lunar surface

Resource: Regolith (common lunar soil), used for building material (sintered into bricks, 3D-printed structures)

Life: None

Community: Small but growing lunar base

Purpose: Construction of lunar habitat expansion

Term-by-term analysis:

S(t): Very high. Regolith is the most abundant material on the lunar surface. You literally cannot run out of it — the Moon is made of it. Alternative construction materials (imported from Earth, mined from asteroids) exist but are more expensive. S\_max ≈ 1.

U(R, t, Q(t)): Low per unit because Q is effectively unlimited. The entire lunar surface is regolith. Stock-dependent utility doesn't activate because the stock doesn't meaningfully deplete.

E(R, t): Low. Dust management is a concern for equipment and habitats (lunar dust is abrasive and electrostatically clingy), but the externality is localized and manageable. No ecosystem damage. No community displacement (if the base plans around the mining area).

RCV result: Very low. Near zero. The model says: extract freely, manage dust, proceed.

Does the model produce the right answer? Yes. Lunar regolith for construction is the mostappropriate resource to extract aggressively — abundant, low externality, high substitutability, no stock depletion concern. The model correctly identifies this as a near-zero-RCV extraction.

Interesting contrast: On the same celestial body, the model produces radically different recommendations for two different resources. He-3: preserve (conditionally high CSG, zero insurance cost, asymmetric regret favors preservation). Regolith: extract freely (zero CSG, unlimited stock, minimal externalities). The model differentiates correctly within the same location based on resource characteristics. This is a strong validation — a model that said "preserve everything on the Moon" or "extract everything on the Moon" would be wrong. The model says "it depends on the resource," which is correct.

---

SCENARIO 6: Mining Subsurface Ice on Europa

Body: Europa (moon of Jupiter)

Resource: Subsurface liquid water ocean

Life: Possible — Europa's ocean is one of the most likely locations for extraterrestrial life in the solar system

Community: None (robotic mission or distant-future crewed outpost)

Purpose: Fuel (electrolysis → hydrogen/oxygen), life support for future outpost, scientific study

Term-by-term analysis:

S(t): For fuel and life support at Jupiter, very low. No other accessible water source in the Jovian system offers Europa's volume (estimated 2-3x Earth's total water). Ganymede and Callisto have ice but less accessible. S is low for Jupiter-system operations.

U(R, t, Q(t)): Moderate per unit (the ocean is vast — estimated 3 × 10^18 cubic meters, roughly 2-3 times Earth's ocean volume). Stock depletion is not a concern for any foreseeable extraction rate.

E(R, t): This is where the model encounters its most interesting edge case. If Europa's ocean harbors life — even microbial life — the externalities of extraction are unlike anything in the model's terrestrial or Martian applications.

What is the externality of potentially destroying the only other biosphere in the known universe? This isn't a health cost or an environmental remediation cost or a community displacement cost. It's a knowledge and existence externality — the permanent loss of scientific understanding and the moral weight of extinguishing an independent origin of life.

The model's E(R,t) term can technically accommodate this — you assign a value to the destruction and integrate it over time. But the value is genuinely unestimable. It's not V\_civ (which was unfalsifiable because it was too large). It's something different — it's the value of knowing whether we're alone in the universe, which is a question that, once answered negatively by destroying the evidence, can never be asked again.

Does the model handle this? Partially. The model correctly identifies that E(R,t) is potentially enormous and that extraction should be delayed until the scientific question is resolved. It produces the right recommendation: study first, extract later (if at all). The asymmetric regret is overwhelming — the regret of extracting and destroying Europan life (if it exists) is irreversible and incalculable, while the regret of waiting to extract is merely the time cost of delayed resource access.

But the model can't price the Europan life externality in the same way it prices black lung disease or acid mine drainage. Some externalities are genuinely incommensurable with market values.

What this reveals: The model has a boundary. It works excellently for resources whose externalities are expressible in health costs, environmental remediation, community disruption, and climate damage. It works well for existence-value externalities (preserving a natural wonder, maintaining biodiversity) using contingent valuation methods. But it encounters a genuine limit when the externality involves potentially unique phenomena — an independent origin of life, a one-of-a-kind geological formation, an irreproducible scientific record.

The model's honest response at this boundary: "The RCV of this extraction includes an externality term that I cannot price, but whose irreversibility and potential magnitude are sufficient to recommend extreme caution. The asymmetric regret framework applies: wait, study, decide later."

This is actually the correct response. A model that claimed to price everything, including the value of extraterrestrial life, would be dishonest. A model that says "I can price most things, and for the things I can't price, the irreversibility principle applies" is honest and useful.

---

SCENARIO 7: Mining Comet Material During a Flyby

Body: Long-period comet making a single pass through the inner solar system

Resource: Volatile ices (water, CO₂, ammonia, methane), organic compounds, mineral dust

Life: Extremely unlikely

Community: None

Purpose: Resource capture for space-based industry

Term-by-term analysis:

S(t): Moderate. Other comets exist, but long-period comets are individually unique and may not return for thousands or millions of years. Short-period comets are more accessible but less resource-rich. Substitutability depends on whether the specific comet's composition is unique or typical.

U(R, t, Q(t)): Here's the interesting part. A comet flyby is a time-limited extraction opportunity. The resource is accessible only during the flyby window (weeks to months). After that, the comet is gone for millennia. This creates a temporal version of the stock-depletion problem — not "the stock is getting smaller" but "the access window is closing."

The model handles this naturally. U(R, t, Q(t)) is very high during the flyby window and drops to zero afterward (the resource becomes physically inaccessible). This means the RCV calculation collapses to a finite integral over the flyby period — the foreclosure cost is the value of what you didn't extract during the window, multiplied by the probability you'll never have access again.

E(R, t): Near zero. No life, no community, no atmosphere, no ecosystem. The only externality is potential alteration of the comet's orbit through mass removal (negligible for any practical extraction volume relative to comet mass).

RCV result: Moderate, but with a time-urgency component that the model captures through the temporal utility function. The model says: extract as much as economically feasible during the flyby, because the access window closes permanently.

Does the model produce the right answer? Yes, and it reveals an interesting inversion. For every other scenario, the model recommends caution and preservation. For a comet flyby, it recommends aggressive extraction — because the "preserve for later" option doesn't exist. The resource is going away regardless of what you do. The asymmetric regret flips: the regret of not extracting (losing access permanently) exceeds the regret of extracting (minimal externalities).

What this reveals about the model's structure: The model is not inherently conservative. It doesn't always say "preserve." It says "extract when RCV is low relative to the value extracted, preserve when RCV is high relative to the value extracted." For a comet flyby with near-zero externalities and a closing access window, aggressive extraction is the model's recommended strategy.

This is important for the book because it demonstrates that Commons Bonds is not an anti-extraction framework. It's a proper-pricing framework. Sometimes proper pricing says "don't extract" (McDowell County coal). Sometimes it says "extract aggressively" (comet flyby, asteroid iron). The model differentiates correctly based on the parameters.

---

SCENARIO 8: Mining Rare Earth Elements on an Inhabited Exoplanet (Far Future)

Body: Terrestrial exoplanet with indigenous non-technological life (complex ecosystem, no sentient species)

Resource: Rare earth deposit

Life: Complex non-sentient ecosystem (equivalent to Earth's Carboniferous period)

Community: Human colony, 50,000 people

Purpose: Manufacturing for interstellar communication and propulsion systems

This is the most extreme test case. Every term is active. Let me trace through:

S(t): Low for the specific application (interstellar propulsion). No substitute exists for certain rare earth magnetic properties at the energy densities required.

U(R, t, Q(t)): Very high. The resource enables interstellar capability, which is an existential function for a species that has already left its home system.

E(R, t): Substantial. Mining disrupts a complex alien ecosystem. This raises the Europa question again — what is the externality of disrupting an independent biosphere? — but in a more nuanced form, because the ecosystem isn't being destroyed entirely, just disrupted locally.

Spatial cost severance: the colony and the extraction site are on the same planet. The cost-distance is compressed but not zero (the colony might be far from the mine).

RCV result: High, driven by a large E(R,t) term (ecosystem disruption) partially offset by low S(t) (the resource is genuinely needed for an existential application).

The model produces a genuine tension: the foreclosure component says "extract, because S is low and U is high — you need this resource for survival." The externality component says "caution, because E is large — you're damaging a unique ecosystem." These pull in opposite directions.

How does the model resolve this? Through the net RCV and comparison with B. If the colony can extract with sufficient environmental mitigation (high B — accountability bonds that fund ecosystem restoration, minimal-footprint mining techniques, biodiversity offsets), CS can be reduced toward zero even though RCV is high. The model doesn't say "never extract from living worlds." It says "the accountability bond must be very large — proportional to the ecosystem damage — and the extraction method must minimize E(R,t)."

Does the model produce the right answer? I think so. It produces the nuanced answer: "extract if necessary, but with extreme accountability, minimized footprint, and only after exhausting alternatives." This is how a responsible civilization should approach resource extraction from living worlds. The model captures the tension rather than collapsing it into a simple yes or no.

---

CROSS-SCENARIO SYNTHESIS

Let me compile the results:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Scenario | RCV | CS | CSG | Model Says | Correct? |
| Asteroid iron | Very low | ~0 | 0 | Extract freely | Yes |
| Mars water (pre-colony) | Extreme | Extreme | Maximum | Preserve absolutely | Yes |
| Mars rare earths (colony) | High | ~0 (self-bearing) | High | Extract carefully, costs borne locally | Yes |
| Lunar He-3 | Uncertain | Uncertain | Conditionally high | Preserve (insurance is free) | Yes |
| Lunar regolith | Near zero | ~0 | 0 | Extract freely | Yes |
| Europa ice | Unestimable E | N/A | N/A | Wait, study, decide later | Yes |
| Comet flyby | Moderate | Low | Low | Extract aggressively | Yes |
| Exoplanet rare earths | High (tension) | Reducible with high B | High | Extract with extreme accountability | Yes |

The model produces the correct answer in every scenario. More importantly, it produces different answers for different scenarios, which is what a useful model must do. It differentiates by:

Resource abundance (asteroid iron vs. Mars water)

Presence of life (Europa vs. asteroid)

Community presence (Mars colony vs. uninhabited asteroid)

Substitutability (water on Mars vs. regolith on Moon)

Access window (comet flyby vs. permanent deposit)

Existential relevance (He-3 for fusion vs. iron for construction)

Properties the model demonstrates across all scenarios:

Universality. The same formula, the same terms, the same logic applies on every body. No modifications needed. The parameters change; the structure doesn't.

Differentiation. The model never produces one-size-fits-all recommendations. It produces a spectrum from "extract aggressively" to "preserve absolutely," driven by the parameters.

Boundary honesty. When the model encounters something it can't price (Europan life), it says so and defaults to the asymmetric regret principle rather than pretending to compute a number. This is a strength, not a weakness.

Cost severance as a function of distance. The Mars colony scenario reveals that cost severance requires distance between beneficiary and cost-bearer. When that distance is zero (colony mining for itself), cost severance naturally goes to zero. This is a deep structural insight about why cost severance happens on Earth — not because people are evil, but because distance enables ignorance.

The model is not anti-extraction. It's pro-honest-pricing. Sometimes honest pricing says extract (asteroid iron, comet flyby). Sometimes it says preserve (Mars water, lunar He-3). Sometimes it says "extract but pay full costs" (exoplanet ecosystem). The model is a navigation system, not a prohibition.

---

WHAT THIS MEANS FOR THE BOOK

The cross-scenario testing confirms that the model is genuinely universal. It works on every body type, every resource type, every community configuration, and every extraction purpose I can construct. The single modification needed from the original framework is the recognition that some externalities are incommensurable (Europa life) and the model honestly defaults to asymmetric regret rather than pretending to price them.

For the book, this testing produces a powerful passage — probably a section within the Colony Administrator chapter — where you walk through three or four of these scenarios briefly, showing the model producing different answers for different conditions, and then make the point: the model that tells a Mars colony to preserve its water ice and a comet miner to extract aggressively is the same model that tells us coal in Appalachia has been mispriced by a factor of 30-100x. The math is the same. The parameters are different. The model doesn't have an agenda. It has a formula. And the formula works everywhere.

That's the universality claim, validated. It's what gives you the right to say that Commons Bonds isn't a critique of capitalism or a political argument. It's an instrument — like a thermometer or a scale. It measures what things actually cost. What we do with the measurement is up to us.

========

========

Counterargument

========

========

---

COUNTERARGUMENT 7: "Your interplanetary test proves less than you think. Comparing Earth to Mars is a false analogy."

Who makes this argument: Pragmatists, people skeptical of big theoretical claims.

The strongest version: "A Mars colony of 10,000 people with three water deposits is nothing like Earth with eight billion people and enormous resource stocks. On Mars, scarcity is immediate and lethal. On Earth, scarcity is distant and gradual. The colony administrator prices water correctly because the feedback loop is immediate — misprice it and people die this year. On Earth, the feedback loop is generational — misprice it and people in McDowell County die slowly over decades while the rest of the country doesn't notice.

"Your model produces the 'obviously correct' answer on Mars precisely because Mars is a simple system with clear boundaries. Earth is a complex system with unclear boundaries, massive stocks, continuous discovery of new deposits, ongoing technological innovation, and political and economic feedback loops that Mars doesn't have. Saying 'the math is the same' ignores that the systems are qualitatively different.

"And your asteroid mining scenario — where you say the model recommends aggressive extraction because externalities are near zero — reveals a problem. On an uninhabited asteroid, your model reduces to market pricing because all the novel terms (S, E, spatial cost severance) go to zero. The model only diverges from market pricing when there are communities and ecosystems to protect. So it's not really a universal resource-pricing model. It's an environmental protection model with extra steps."

Why this is dangerous: Because the complexity objection is legitimate, and the "reduces to market pricing for asteroids" observation is analytically sharp.

How the book should respond:

On the complexity objection: the model doesn't claim Earth is as simple as Mars. It claims that the structure of the pricing problem is the same — finite resources, irreversible extraction, intergenerational consequences. The parameters are vastly different (Earth's stocks are larger, the timeline is longer, the feedback loops are slower), and those parameter differences produce different quantitative outputs. The model produces "extract freely" for asteroid iron and "severe underpricing" for Appalachian coal not because it ignores complexity but because it correctly incorporates the parameters that differ.

The key response to the "Mars is simple" objection: the fact that Mars makes the model's logic undeniable is precisely the point. Mars is the limiting case where the parameters are extreme enough to make the correct answer obvious. Earth is the case where the same logic applies but the parameters are moderate enough to obscure the correct answer. Using the limiting case to illuminate the general case is standard scientific practice — physicists use frictionless planes and perfect vacuums to derive laws that hold imperfectly but usefully in the real world.

On the "reduces to market pricing for asteroids" observation: this is not a weakness. It's a strength. A good model should reduce to existing models as special cases. When externalities are zero, community impact is zero, and stocks are abundant, the RCV model should reduce to market pricing — because in those conditions, market pricing is correct. The model adds value precisely and only where market pricing fails — where externalities are significant, communities are affected, and stocks are finite. That's not "environmental protection with extra steps." That's a pricing model that correctly accounts for costs that market pricing structurally cannot see, and that correctly reduces to market pricing when those costs are absent.

The model's universality claim is not "it always disagrees with the market." It's "it always produces the correct price, which sometimes agrees with the market (asteroid iron) and sometimes dramatically disagrees (McDowell County coal)." A model that always disagreed with the market would be as useless as one that always agreed. A model that correctly identifies when and by how much the market errs is genuinely useful.

---

8. THE BOOK NEEDS COMPARATIVE CASES WITHIN CHAPTERS, NOT JUST ACROSS CHAPTERS

Right now, each chapter focuses on a single case or theme. This is clean structurally but misses opportunities for comparison that would strengthen the argument.

Within Chapter 7 (The Colony Administrator), the cross-scenario testing already serves this comparative function. Keep it.

These within-chapter comparisons strengthen the argument because they show the model isn't a blunt instrument that says "extraction bad." It's a sensitive instrument that says "extraction under these conditions produces this much cost severance, and extraction under different conditions produces a different amount." That sensitivity is what makes it credible.

---

## Multi-perspective application example — asteroid mining contract scenario (added 2026-04-23 per PCR v1.0.0 Cross-cutting Finding 3)

**Source + rationale:** Path Comparison Report v1.0.0 (Path Comparison Mode applied to framework-scope decision) surfaced the asteroid-miner-considering-off-world-contract example as decisive evidence for the framework's individual-scale usability (Goal-2 — individual readers apply the framework to their own decisions). The example is currently absent from the manuscript and from this guidance doc.

**Test-suite assessment (M1.5 + M2 + M3 + M5 + M7 + M8 + M11) on whether to expand to multi-perspective + Earth equivalent:** EXPAND. Strengthens on 7 modules (M1.5 universality, M2 chapter fit, M3.4 counterargument coverage, M7 originality, M8 long-term, M11 C9 + C10 + C13 + C24); weakens recoverably on 2 (M3.1 trying-to-do-too-much, M5 dinner-table). Earth-equivalent perspective is the highest-leverage addition because it connects the speculative asteroid scenarios to current-day extraction contexts where readers actually live.

**Recommended placement within Ch 7:** extend the existing cross-scenario universality-test material (currently scenarios 1–8) with a multi-perspective "applied" demonstration that walks the framework through a single asteroid-mining contract scenario from four stakeholder perspectives + one Earth-based equivalent. Treat as the chapter's pivot from "the model produces correct answers across scenario types" to "the model produces actionable answers across stakeholder positions within a single scenario" — which sets up Ch 8 (one extraction worked through all tiers) and Ch 9 (policy response).

**The four perspectives:**

1. **The asteroid miner considering the off-world contract (individual scale, off-Earth).**
   - Activates: Habitability (bodily safety, biological adaptation, life-support dependency), Kindred (family separation, communication delay across distance + time, dependents the miner is responsible for), Temporal (return-trip uncertainty, post-contract Earth-economy reintegration delay), Autonomy (constrained consent — what alternatives exist back on Earth?), Institutional (contract enforceability across jurisdictions; legal recourse if the company fails on its obligations).
   - Tier signature: Tier 1 (direct survival risk) + Tier 3 (dynastic — family back on Earth bears the cost of separation) + Tier 4 (foreclosure of return options if contract terms degrade).
   - Application: applies CIT (Commons Inversion Test; renamed from AIT 2026-04-24) to the contract terms — what scarcity does this contract operate on? Identifies which tiers the offered compensation covers and which it leaves uncovered. Computes residual cost severance. Uses the result in negotiation: "the offered B doesn't cover Tier 3 dynastic costs; I need either a higher base + family-support stipend, or a shorter contract term, or both."

2. **The asteroid mining company (corporate scale, off-Earth).**
   - Activates: Institutional (regulatory exposure across jurisdictions; reserve-bond requirements; insurance), Political (geopolitical positioning between Earth-based regulators and any off-Earth governance), Temporal (extraction-rate optionality — extract now vs. preserve for future demand), Epistemic (worker-safety information disclosure standards), Ecosystem (any biological hazards the operation exposes the workforce to).
   - Tier signature: Tier 7 (political capture cost the company has the resources to attempt) + Tier 8 (temporal displacement — extraction-pace decisions affect future colony viability) + bonding-side calculations on Tiers 1, 4, 5.
   - Application: applies CIT (Commons Inversion Test; renamed from AIT 2026-04-24) to its own extraction model — what costs is the company currently externalizing? Computes the bond required to make contracts socially acceptable. Decides between (a) raising compensation to internalize, (b) restructuring extraction pace to reduce externality tail, (c) accepting that some operations are not viable under honest accounting.

3. **The asteroid colony administrator (community-government scale, off-Earth).**
   - Activates: Spatial (the asteroid is the commons; extraction reduces the commons), Temporal (intergenerational reserve preservation; what does the next generation inherit?), Cohesion (social impact of extraction-rate decisions on colony fabric), Political (distributional fairness across colony residents — who captures the value, who bears the cost), Institutional (governance instruments available to set extraction policy).
   - Tier signature: Tier 4 (foreclosure of resource for colony's long-term viability) + Tier 5 (community-transition reserve — what happens when this asteroid is depleted?) + Tier 7 (political capture pressure from extraction firms) + Tier 8 (temporal displacement — pace of extraction relative to colony's capacity to absorb).
   - Application: applies CIT (Commons Inversion Test; renamed from AIT 2026-04-24) to extraction-policy decisions — what are the cumulative cost-severance effects of permitted extraction across all operating contracts? Sets bond requirements that the framework computes are necessary to make the operations colony-net-positive. Negotiates with extraction firms from a framework-grounded position rather than a purely-political position.

4. **Earth-based equivalent — McDowell County coal miner considering an extraction job (individual scale, Earth) — connects to Ch 2 anchor case.**
   - Activates: same dimension set as the asteroid miner but with different parameter values. Habitability (black lung; not asphyxiation but the same dimensional cost). Kindred (family in the hollows; different geography but same dynastic-cost shape). Temporal (post-extraction-economy reintegration; the cost of staying when the mine closes). Autonomy (constrained consent under company-town conditions historically; under landlord-class housing capture currently). Institutional (bond requirements under SMCRA; regulatory enforcement gaps).
   - Tier signature: same as the asteroid miner — Tier 1 + Tier 3 + Tier 4 — with different parameter values.
   - Application: the McDowell coal miner historically did not apply this framework because it didn't exist. The framework's contribution is to make this analytical apparatus available to any worker considering any extraction job. The Earth-equivalent demonstrates that the same multi-perspective analysis the asteroid miner performs is performable today by current workers — the framework operates at present-day Earth-extraction scale, not just at speculative-future-off-Earth scale.

**Why all four perspectives matter together:**

The single-perspective version (just the miner) demonstrates Goal-2 (individual readers apply the framework). The multi-perspective version demonstrates that the framework operates as a *negotiation instrument* across the full stakeholder set in any extraction context. The Earth equivalent grounds the speculative scenarios in present-day applicability — readers can apply this Tuesday morning, not in a hypothetical future. Together the four perspectives demonstrate the framework's full operational range in a single scenario architecture.

**Register notes:**

- Each perspective: 2-4 paragraphs maximum. Total addition to Ch 7: ~1,000-1,500 words.
- Compress aggressively — this is a worked example serving the universality argument, not a deep case study. Use the 8 cross-scenarios above as the model for compression (each scenario gets ~150-300 words of analysis).
- Earth-equivalent paragraph should explicitly cross-reference Ch 2 (McDowell coal anchor case) so the connection is visible, not implied.
- Asteroid scenario specifics (asteroid composition, contract length, colony size, etc.) — use the same setup as the existing Mars-water-ice colony for continuity, or reference a new asteroid scenario that complements it.

**Cross-chapter coordination:**

- **Ch 1 guidance** — note the framework-as-tool framing in Ch 1 should reference forward to Ch 7's worked example as "the kind of application this book teaches you to do."
- **Ch 10 guidance** — note Ch 10 closing can briefly reference the asteroid-miner example as the demonstration of "tool readers apply in their own contexts."
- **Ch 8 guidance** — Ch 8's tier-by-tier worked McDowell coal example pairs with Ch 7's multi-perspective application. Ch 7 = how the framework applies across stakeholders within a scenario; Ch 8 = how the framework prices an extraction tier-by-tier within a single perspective. Don't duplicate; complement.

**Path-dependency note:**

[*UPDATED 2026-04-24 Phase A3 sweep:*] Path F (variables-not-dimensions reframing) was ratified 2026-04-24 + further developed via commons-as-structural-identity reframing — each perspective discovers its **commons categories** (formerly "variables" / "10 abundance dimensions") via **CIT (Commons Inversion Test, formerly AIT)** rather than being structured around the canonical 10. The 10 commons are EXAMPLES (per Option C' political-philosophical-accommodation discipline); not exhaustive. 8-tier decomposition retired (per tier-dissolution rigor pass); costs are Cᵢ admitted through Four Gates. The example survives the path-F + commons-reframing changes; only framing updates.

