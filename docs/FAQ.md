---
title: FAQ
---

# Frequently Asked Questions

Common questions about the K₇ framework, as of version 3.6 of the framework paper. Where this page and the [main paper](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) differ, the paper holds.

## The framework

### What is the K₇ framework?

A **declared correspondence**. It assigns 33 dimensionless parameters of the Standard Model and of cosmology to closed forms in the invariants of a compact seven-dimensional manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with an E₈×E₈ gauge structure. For example, sin²θ_W is assigned b₂/(b₃ + dim G₂) = 3/13.

It is stated with three things: its **dictionary** (twenty structural constants and the grammar in which formulas are written), its **residue register** (everything that was set rather than derived) and a **decision rule** written in advance.

### Is it a derivation of the Standard Model's constants?

No. No geometric map is known that sends the invariants of K₇ to the observables, and no rule fixes which formula is assigned to which observable. Earlier versions wrote "derive" where the operation is an assignment; version 3.6 withdraws that wording throughout. K₇ is a privileged candidate chosen by the author, and the paper says so.

### Does it have free parameters?

No relation has a **continuously** adjustable parameter: an integer ratio cannot be nudged. That is not the same as having nothing chosen. The residue register (R1 to R12) lists what was set: the Betti pair (21, 77), the imposed normalization det(g) = 65/32, the combination κ_T⁻¹ = 61, the unit in which the integer 197 is read as a CP phase, the scales and mass schemes of the comparisons, the assignment of formulas to observables, and the absence of a choice among incompatible relations in three sectors. Earlier versions described this as a framework with no free parameter and no fitting; that description of the formula choice is withdrawn.

### Does the manifold K₇ exist?

It is not known. No compact torsion-free G₂ manifold with Betti numbers (21, 77) is currently constructed, and the route proposed in version 3.5 does not realise the pair ([erratum](https://github.com/Arithmon/K7/blob/main/publications/ERRATUM_v3.5.md), §9). The 33 relations do not use the metric of K₇: they rest on the declared topological invariants and on the E₈×E₈ group data. The companion papers certify local or conditional pieces (a seam metric, a neck ansatz), not a compact K₇.

### How is this different from string theory or M-theory?

E₈×E₈ and G₂ holonomy both appear in M-theory, but the framework does not supply a compactification of either kind. Its smooth K₇ does not yield the chiral non-abelian content of the Standard Model, and its relations are not derived from a four-dimensional effective theory. It uses the exceptional structures as a source of integers and says so.

### Is this mainstream physics?

No. It is the work of an independent researcher, developed with AI assistance, and it has not been through journal peer review. The papers, the data and the code are public so that the claims can be checked by anyone. The framework has been cited in the peer-reviewed literature; a citation is not an endorsement.

## The 33 relations

### What does the framework compare with experiment?

Thirty-three dimensionless relations: gauge couplings, lepton and quark mass ratios, PMNS and CKM mixing parameters, boson mass ratios and cosmological parameters. The [Observable Reference](wiki/Observable-Reference.html) gives each formula, its value, the measurement and its status.

The dataset holds 62 further entries (dimensionful quantities read in a chosen unit, outputs of mechanisms with calibration choices, structural diagnostics). Version 3.6 does **not** count them as predictions; earlier versions spoke of 95 predicted observables, which is withdrawn.

### How well do the 33 relations agree with the data?

Against PDG 2026, NuFIT 6.1, Planck 2018 and CODATA 2022, with all uncertainties at 1σ, they fall into five classes that are not added into one score:

| Class | Count | Relations |
|---|:---:|---|
| within 2σ | 23 | the remaining relations |
| tension (between 2σ and 3σ) | 2 | m_τ/m_e, Ω_c/Ω_m |
| proximity (beyond 3σ, rejected as an exact equality) | 6 | α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t, m_W/m_Z |
| inside the PDG range (no uncertainty given) | 1 | m_s/m_d |
| non-Gaussian profile, octant unresolved | 1 | sin²θ₂₃ |

Earlier versions summarised the agreement by a mean deviation. That summary is withdrawn: it hid the relations outside 2σ. Details are in the [Validation Summary](wiki/Validation-Summary.html).

### Are these 33 independent tests?

No. Three sectors are overdetermined: four lepton relations bear on two mass ratios, three CKM relations on two parameters, seven density relations on two independent densities. In each, the relations disagree with one another as exact equalities, so they cannot all hold, and none is selected after the fact. Taken jointly as exact equalities, the 33 are already incompatible; individual relations remain testable.

### Is the agreement statistically significant?

No. In a preregistered look-elsewhere test, every competitor searches for its own formulas in the same grammar and with the same budget. K₇ reaches 31 of the 33 targets; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many, and none reaches more (global p-value 0.51 against a threshold of 0.01). A control with no K₇ constant reaches 30. Closeness to the measured values is therefore not, by itself, evidence for K₇.

The coincidence probabilities, P-values and Bayes factors of earlier versions are withdrawn: they came from tests in which the alternatives were scored with K₇'s own formulas. See [Statistical Evidence](wiki/Statistical-Evidence.html); the code and results of the test are [public](https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/).

### What are the weakest points?

- Six relations are rejected as exact equalities and kept only as numerical proximities, among them α⁻¹ and sin²θ_W.
- sin²θ₂₃ = 6/11 sits in the second octant while the global fit prefers the first.
- The agreement is not distinctive (previous question).
- The Betti pair, the formulas and the normalization are chosen, not derived; five routes to deriving (21, 77) have been closed without success.
- The manifold is not constructed, and no mechanism leads from it to the chiral Standard Model.

### What about δ_CP = 197°?

The structure produces the integer 197 = 7·14 + 99. Reading it as an angle in degrees is a choice of the dictionary, recorded in the residue register and counted in the look-elsewhere test; read in radians or grads, the same integer gives other phases. NuFIT 6.1 gives δ_CP = 212 (+26/−36)°, so the reading in degrees lies inside the 1σ band today. A confirmation would show that this assignment agrees with the world, not that the structure requires it.

### What about dimensionful quantities like masses?

Absolute masses and scales appear only among the 62 entries that are not counted as predictions. Several are structural numbers read in MeV; reading a number in a unit is an assignment of the same kind as reading 197 in degrees, with a far larger space of alternatives.

## Testing

### Can the framework be refuted?

Individual relations can. Each is stated as an exact equality with no theoretical uncertainty, and the rule is written in advance with no repair clause: a relation is rejected when its reference series (PDG, NuFIT, Planck, CODATA) excludes its value at 3σ, and it is not rescued by changing its formula, its unit, its scale or its dataset.

| Relation | Value | Rejected when | Where |
|---|---|---|---|
| δ_CP | 197° | a global fit whose 3σ interval excludes 197°; the unit assignment is rejected with it | DUNE, Hyper-Kamiokande |
| sin²θ₂₃ | 6/11 | a global fit whose 3σ interval excludes 6/11, in either octant | DUNE, Hyper-Kamiokande |
| sin²θ₁₂ | 4/13 | a global fit whose 3σ interval excludes 4/13 | JUNO (first result 0.3092 ± 0.0087; about four times tighter than today's global fit after six years) |
| m_τ/m_e and Q_Koide | 1776.74 and 1776.97 MeV for m_τ | an m_τ value whose 3σ interval excludes the value | Belle II, BES III |
| N_gen | 3 | a fourth sequential generation | LHC, FCC |
| m_s/m_d | 20 | a lattice determination with an uncertainty whose 3σ interval excludes 20 | lattice QCD |

A rejection rejects the relation and the assignment that produced it. It does not by itself reject the programme, whose other relations stand or fall on their own; the paper says so now, so that it cannot be said later as a repair. The wider exploratory programme has, at present, no single criterion of refutation.

### What would count in its favour?

Less than one might hope. Since closeness is not distinctive, further agreements at the percent level add little. What would change the picture is of another kind: a construction of the manifold, a mechanism that selects (21, 77), a rule that assigns formulas to observables, or a relation surviving a measurement precise enough to discriminate among competing vocabularies.

### Are there measurements that already contradict a relation?

Two contradicting results outside the reference series are reported beside their class. h = 167/248 agrees with Planck and is excluded by the SH0ES distance ladder at 5.5σ. The density relations agree with Planck and are strained by the baryon acoustic oscillations of DESI (second data release): DESI alone puts Ω_Λ/Ω_m = 113/52, Ω_m/Ω_Λ = 28/61 and Ω_DE at about 2σ; DESI combined with the cosmic microwave background puts them at −3.3σ, +3.4σ and −3.1σ, and h at −3.0σ. While methods disagree, the status is stated both ways, and neither agreement counts as a confirmation.

## Mathematics and verification

### Why E₈×E₈ and G₂ holonomy?

They are structures whose interest owes nothing to the Standard Model's constants: the octonions, Berger's classification of holonomy groups, the exceptional Lie algebras, and the role of both in M-theory. That answers whether the family deserves to be explored. It does not answer why this member: the requirements do not select (21, 77), the formulas or the normalization.

### What does the Lean 4 formalization prove?

The arithmetic. Given the declared integers, each of the 33 closed forms evaluates to the stated number (collected in `relations_v36_certified`; 156 files, 14 axioms, no `sorry`). It does not establish the existence of K₇, the physical interpretation of any relation, the choice of assignments, or the consistency of the relations taken together. A formula that is machine-checked is not thereby the right formula.

### Why these numbers and not others?

That is the selection question, and it is open. The pair (21, 77) is a construction-level input on the same footing as the G₂-holonomy postulate: fixed before the relations were frozen and used rigidly by all of them, but chosen, not selected. One numerical observation survives, b₂ + b₃ = 98 = dim(K₇) · dim(G₂), held as a target and not as a theorem.

### Does this mean physics is "just mathematics"?

The framework is read as a structural proposal: structure is asked to carry predictive weight, with no further ontological commitment. Readings in which geometry and information are aspects of one thing motivated the work historically; they are neither required nor supported by the relations.

## Practical

### What changed in version 3.6?

It withdraws several things earlier versions said: that the relations are derived from the geometry, that they cannot be fitted, that 95 observables are predicted, that a coincidence probability or a P-value measures the framework's distinctiveness, that 197° is a prediction of pure geometry, that the generation count comes from an index theorem. What remains is smaller and can be checked. The full list is in the [changelog](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_CHANGELOG.md).

### Where do I start reading?

- **No equations**: [K₇ for Everyone](wiki/GIFT-for-Everyone.html).
- **Physicist**: the [main paper](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md), sections 3, 4, 7 and 11.
- **Mathematician**: supplement S1 and the companion papers on the seam metric.
- **The numbers**: [Observable Reference](wiki/Observable-Reference.html), [Validation Summary](wiki/Validation-Summary.html), [Statistical Evidence](wiki/Statistical-Evidence.html).

### How do I cite it?

The framework paper is archived on Zenodo; the concept DOI [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489) always resolves to the latest version. The [Citation Guide](wiki/Citation-Guide.html) gives the formats.

### Can I use this in my research, or contribute?

Yes: the repository is under the MIT License. Corrections, new data comparisons and reports of errors are welcome through [GitHub issues](https://github.com/Arithmon/K7/issues); see `CONTRIBUTING.md`.

---

*The K₇ Framework v3.6*
