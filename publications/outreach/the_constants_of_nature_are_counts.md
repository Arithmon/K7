# The Constants of Nature Are Counts

### A testable geometric hypothesis for the Standard Model: what is derived, what is assumed, and what would refute it

Brieuc de La Fournière · Arithmon program · [arithmon.com](https://arithmon.com)

> **Written for skeptical physicists.** If after fifteen minutes you conclude this is wrong, it should be clear *where* it is wrong. That is the standard this document is trying to meet.

---

## Why read this

Some numbers that physics once had to measure were later derived. The Balmer constant is one. Whether the Standard Model parameters belong to that class is an open question, and this framework treats it as one. The Standard Model itself is among the most successful theories ever built, predicting thousands of measurements to extraordinary precision. And it leaves one question almost entirely unanswered: why do the fundamental constants have the values they do?

Why these particle masses. Why these mixing angles. Why exactly three generations. Today those nineteen numbers (twenty-six, once neutrino masses and mixings are counted) are measured and inserted by hand.

The K₇ framework explores a single possibility: that none of them are free, and that they are instead arithmetic consequences of one compact seven-dimensional geometry. A hypothesis of that shape has only two available fates. It is spectacularly wrong, or it leaves measurable traces everywhere. There is no comfortable middle in which it is vaguely suggestive.

What follows is the claim, the assumptions it rests on, the evidence, and the specific ways it can fail. If correct, the framework changes the status of the Standard Model parameters from empirical inputs to geometric outputs.

---

## At a glance

| | |
|---|---|
| Core hypothesis | Standard Model constants are invariants of one compact G₂ geometry |
| Continuously adjustable parameters | **0**, after the input ledger is frozen |
| Parameter-free algebraic relations (Type I) | **33** |
| Total derived observables, all types | **95** (66 experimentally comparable) |
| Agreement | **11** exact to better than 0.01%, **53** within 1% |
| Formal verification | **213**-conjunct certificate in Lean 4, **15** classified axioms, **0** unproven steps |
| Pre-registration | ledger, grammar and target list deposited before any search ([DOI](https://doi.org/10.5281/zenodo.20666879)) |
| **Falsification** | **δ_CP measured outside [182°, 212°] at 3σ and the framework is wrong. DUNE beam targeted 2031.** |

That last line is the one that matters most, and section 8 returns to it. A framework with no continuously adjustable parameter cannot absorb a bad measurement. That is a cost, not a feature to be apologised for, and it is what makes the rest of the table worth checking.

---

## 1. The claim

The dimensionless constants of the Standard Model are arithmetic and topological invariants of a compact seven-dimensional manifold with G₂ holonomy, not free parameters to be fitted.

That is the whole hypothesis. The specific realisation is a geometry with Betti numbers (b₂, b₃) = (21, 77) and an E₈×E₈ motivated exceptional architecture. From it, thirty-three exact algebraic relations among Standard Model and cosmological observables follow with no continuously adjustable quantity remaining once the geometric input is declared.

---

## 2. Why this deserves skepticism

If someone claims to derive Nature's constants, your first reaction should be skepticism. Mine would be too. Any sufficiently large pool of small integers and transcendentals produces impressive coincidences, and the history of this genre is not encouraging.

There are three obvious failure modes. The framework's response to each is a commitment made in advance rather than an argument made afterwards.

| Objection | Commitment made before any result was obtained |
|---|---|
| This is numerology | Ledger, formula grammar and target list frozen and publicly deposited before the search; four independent null models |
| The relations were cherry-picked | The formula grammar was declared in advance, so the search space is auditable |
| There are hidden fitted parameters | The ledger is explicit and finite; no continuous adjustment is available after freeze |

None of this proves the framework correct. It makes the standard objections testable instead of rhetorical, which is a lower bar and the only one that can be cleared in advance.

The methodology behind the null models is deliberately not bespoke. It is calibrated against historical verdicts, so that Eddington's fine-structure argument fails it and the quantum Hall relation passes it. A test that only its author's framework can pass is not a test.

---

## 3. What is assumed

The inputs are a declared ledger of twenty structural constants, all algebraic functions of six primitive topological integers: b₂, b₃, dim(G₂), dim(E₈), rank(E₈) and dim(K₇). Standard transcendentals enter as well (π, √2, ln 2, ζ values, and the golden ratio φ, whose appearance is traced to the McKay correspondence E₈ ↔ 2I and carries its own caveat).

Some repository summaries compress the input further, and the two compressions should not be merged. Supplement S1 shows the 169 Chebyshev parameters of the certified metric collapsing to one topological integer, b₂(M₁), plus two Lie ranks: rank(E₈) = 8 and rank(G₂) = 2. That is a statement about the metric construction. The ledger's own compression, to the six primitive integers above, is a statement about the observables. Naming the two groups fixes dim(E₈), dim(G₂) and dim(K₇). What no compression supplies is (b₂, b₃), and that selection is the open question of section 8.

The ledger, the grammar and the target list were frozen and deposited **before** any relation was searched for. This matters more than any individual result below. Pre-registration is what separates a prediction from a retrofit, and here it rests on a timestamp rather than on the author's assurance.

One assumption should be handed to a critical reader rather than left to be discovered. The metric normalisation det(g) = 65/32 is imposed as a target, not derived. Six observables depend on it. Its expression in terms of topological integers is suggestive but not derivational. If there is a soft joint in the construction, it is this one.

---

## 4. What is derived

A recurring problem with ambitious frameworks is that everything eventually gets called a prediction. K₇ separates four epistemic categories and keeps them separate in every table it publishes.

| Type | Count | Nature | Mean deviation |
|---|---|---|---|
| I | 33 | Direct algebraic identities in the frozen ledger | 0.73% (frozen dataset) |
| II | 19 | One-step extractions using a named experimental anchor | 0.17% |
| III | 21 | Multi-step dynamical chains, conditional on the mechanism invoked | 3.4% |
| IV | 22 | Structural diagnostics, no direct experimental comparison | n/a |

One bookkeeping point, disclosed rather than discovered: two Type I deviation figures circulate and both are real. The 0.73% above is the mean against the dataset frozen at pre-registration (PDG 2024 + NuFIT 6.0), which is the figure this document quotes because it is the one the pre-registration protects. After a post-freeze audit reconciled six experimental values to primary sources, the same mean reads 0.99%, and that is the figure the repository summaries carry. Supplement S4 documents both.

Only the thirty-three Type I relations are parameter-free consequences of the frozen ledger. The nineteen Type II relations are conditional reconstructions: each multiplies a Type I ratio by a measured anchor, so that m_u is obtained as (m_u/m_d) × m_d measured. They are nineteen traceable extractions of physical scale, not nineteen independent predictions, and counting them as the latter would be the easiest available way to oversell this work. The twenty-one Type III chains are conditional on the mechanism each invokes, enumerated case by case. Type IV are diagnostics.

One Type I relation is worth stating in full, because it shows in one line what "the constants are counts" is supposed to mean. The number of chiral generations follows from the topological constraint (rank(E₈) + N_gen) × b₂ = N_gen × b₃, that is (8 + N_gen) × 21 = N_gen × 77, whose only integer solution is **N_gen = 3**. It is derived, not declared, and a representation-theoretic route through the (27, 3) of E₆ × SU(3) reaches the same answer independently. Nothing in the ledger was chosen to make it come out that way.

Of the sixty-six experimentally comparable observables, eleven agree to better than 0.01% and fifty-three fall within 1%.

---

## 5. Why the numbers are not the main result

Numerical precision is reported here as a secondary figure. That is a deliberate inversion of the usual presentation, and it is not modesty.

A framework of this kind can always be made to look impressive by leading with sub-percent agreement across dozens of quantities. But precision is cheap to manufacture and expensive to interpret: it is exactly what a well-tuned fit also produces. The claim being made is structural, namely that these relations are algebraic consequences of a geometric input fixed in advance. Precision is evidence about that claim. It is not the claim.

An earlier version of this work led with joint coincidence probabilities of order 10⁻³⁴⁶ against a uniform null and 10⁻¹³³ against an algebraic null over 4.2 million random formulas. Those figures are real, they are retained in the supplements as internal-consistency diagnostics, and they have been deliberately removed from the headline. They measure something, but not what a skeptical reader needs to know, and presenting them as primary evidence was a methodological error this version corrects.

---

## 6. Formal verification, and its limits

The framework carries a Lean 4 formal layer. At current head, the master certificate spans ten files with a top-level conjunct count of **213**, resting on **15 classified axioms** in an A to F taxonomy, with **zero** unproven steps. Four of the fifteen axioms are external data packages, named in the source: `K7_analysis_data`, `K7_spectral_data`, `literature_package`, `KK_YM_EFT`. Fifty-five of the ninety-five observables fall inside the verified perimeter.

What this establishes: the algebraic relations hold as stated, and the internal consistency of the ledger is not a matter of arithmetic trust.

What it does not establish, stated plainly because formal verification is routinely oversold: Lean certifies no physical interpretation, and it does not certify the existence of the complete compact construction. A machine-checked identity between topological integers is exactly that. The certificate drives the probability of a bookkeeping error to zero and leaves every substantive question open.

---

## 7. Why this is not numerology, as a testable proposition

Applied to the thirty-three Type I relations, the pre-registered procedure runs a four-null battery (uniform, algebraic, factorised, permuted) through the same declared twenty-constant ledger, then ranks survivors by budget uniqueness.

The outcome is modest and is reported as such. The unique survivor at exact rank-one budget uniqueness is m_H/m_W. Koide's Q = 2/3 survives with a narrow margin. That is the honest statistical claim: two relations distinguish themselves under a null battery fixed in advance. The thirty-three as a set are conditional algebraic identities of the frozen ledger, machine-checked, but not individually distinguished by the sieve.

Two further checks target the most likely failure mode, which is unconscious selection rather than deliberate fraud.

**Does formula complexity buy precision?** A random-forest regression predicting absolute deviation from formula features achieves R² = −0.518 under leave-one-out cross-validation, which is worse than a mean predictor. Complex formulas do not outperform simple ones.

**Are the good agreements simply the insensitive ones?** Perturbing each of the twenty structural constants by ±1 gives a 20 × 33 sensitivity matrix. The correlation between sensitivity and deviation is ρ = −0.083.

Neither result proves the framework correct. Both would look very different had the relations been selected by fitting.

---

## 8. The three questions that matter most

These are load-bearing and unresolved. They appear here at full prominence, because a reader who finds them on page sixty of the full paper is entitled to feel handled.

**Does the geometry exist?** The framework needs a global compact torsion-free G₂ structure on a smooth K₇. The datum-level analytic layer is discharged conditionally in a companion paper. The global-analytic layer remains conditional on a two-slot hypothesis pack. The framework does not claim the construction exists; it claims what follows if it does, and it labels which layer each result sits above.

**Where does the gauge sector come from?** The branching chain E₈ ⊃ E₆ × SU(3) ⊃ ⋯ ⊃ SU(3) × SU(2) × U(1) is compatible with Standard Model matter content, but it is a chain of subgroup branchings, not a physical breaking mechanism. The bridge to a non-abelian chiral gauge sector is open. This is the largest gap in the work.

**Why (21, 77)?** The selection question was audited, not answered. Five candidate routes to deriving the Betti numbers were investigated and closed. One explicit residual remains: b₂ + b₃ = 98 = dim(K₇) · dim(G₂). No uniqueness is claimed, either of the geometry or of the assignment of formulas to observables.

---

## 9. How this framework could fail

| Prediction | Value | Experiment | Timeline | Refuted if |
|---|---|---|---|---|
| δ_CP | 197° = dim(K₇)·dim(G₂) + H* = 7 × 14 + 99 | DUNE Phase I (3σ) | beam targeted 2031 | measured outside [182°, 212°] |
| δ_CP | as above | DUNE Phase II (5σ) | late 2030s to 2040s | definitive |
| N_gen | 3 | any | ongoing | a fourth generation |
| m_s/m_d | 20 | Lattice QCD | 2028 to 2030 | target ±0.5; current 20.0 ± 1.0 |
| sin²θ_W | 3/13 | FCC-ee | 2040s | precision ~10⁻⁵ |

Every integer in the δ_CP decomposition is a named invariant, because in this framework it has to be: 7 × 14 = dim(K₇) · dim(G₂) = 98, the same product that reappears as b₂ + b₃ = 98 in the residual of section 8, and 99 = H\*, the effective cohomological dimension 1 + b₂ + b₃.

Worth stating before a reader finds it: since 99 = 1 + 98, the prediction reduces to δ_CP = 2(b₂ + b₃) + 1. The framework's most exposed prediction therefore rests on a single input, the Betti sum, which is precisely the quantity section 8 declares underived. That is the actual shape of the exposure, and it is better read here than reconstructed by a skeptic.

No reinterpretation is available. If DUNE returns δ_CP = 250°, this framework is wrong, nothing in it can be tuned to survive, and the correct response will be to say so in public.

Two further consequences are recorded as complementary rather than critical, being model-dependent: a proton lifetime of 4.06 × 10³⁸ years, beyond near-term Hyper-Kamiokande reach, and a SUSY spectrum with m_gravitino = 166 GeV and m_moduli = 3.2 TeV, viable only in compressed or suppressed-coupling realisations.

---

## 10. Check it yourself

The framework's central methodological commitment is that its claims should be verifiable without trusting the author, so here is the shortest path to testing one of them.

The Lean sources are public. The conjunct count in section 6 is the number of top-level ∧ operands across the master certificate files. Clone the repository, strip comments, count operands at parenthesis depth zero, and compare. If the number is not 213, that discrepancy is a fact about this work and should be reported as one.

The same holds for pre-registration. The deposit predates the search, the timestamp is on the DOI, and the grammar is in the repository. None of it requires taking anyone's word.

---

## 11. Where to go from here

- **The full framework paper**, with four supplements: derivations, complete observable tables, axiom accounting, selection audit.
- **The methodology paper**: the four-null battery, the historical calibration, and a scorecard reusable on any framework, including this one.
- **The formal core**: Lean 4 sources, certificates, build instructions.
- **The confrontations scoreboard**: named predictions against scheduled data, dated, with outcomes recorded as they arrive.
- **The program charter**: hard core, heuristics, fair-play rules, open problems.

At [arithmon.com](https://arithmon.com) and [github.com/Arithmon](https://github.com/Arithmon).

---

## The question

Most proposals that attempt to explain the constants of Nature eventually fail. Perhaps this one will too.

But the question does not go away with them. If the constants are not fundamental, they come from somewhere. K₇ is one attempt to answer that while making every assumption explicit, every calculation reproducible, every prediction public, and every route to refutation available in advance.

Whether the hypothesis survives is now a matter for mathematics and experiment, not for authority.

---

<sub>The underlying numerical work on G₂ metrics is cited as reference 25 in *Physics Letters B* **878** (2026) 140566 (Heyes, Hirst, Sá Earp and Silva). The author participated remotely in the DANGER workshop at the Banff International Research Station, April 2026, and has no formal training in physics or mathematics: every claim above is built to be checkable without reference to its author.</sub>
