---
title: "K₇: Executive Summary"
---

# K₇: a correspondence, and the terms on which it can fail

*A technical summary for curious physics readers, as of version 3.6*

---

## The problem, stated plainly

The Standard Model of particle physics operates with a precision no other scientific theory has ever matched. It describes every known fundamental interaction apart from gravity, with experimental agreement sometimes reaching twelve decimal places.

Yet it contains about nineteen free parameters, numbers the theory does not compute and which must be measured before the theory can be used: the masses of the charged leptons and of the six quarks, the parameters of the CKM matrix, the three coupling constants, the Higgs mass and its vacuum expectation value. Neutrino masses and mixing add more.

To this are added long-standing puzzles. Why exactly three generations of matter? Why do the charged lepton masses obey the Koide relation *Q* = 2/3 so closely, a relation noticed in 1981 and never explained? Why does the ratio of dark matter to baryonic matter sit close to a simple rational?

K₇ (*formerly Geometric Information Field Theory*) is one attempt to look at these numbers differently. It asks: what if they could be written as closed forms in the invariants of a single geometric structure? And, since writing such forms turns out to be easy, it asks a second question with the same seriousness: what would it take for such a correspondence to mean anything?

## The proposal

In one sentence: 33 dimensionless parameters of the Standard Model and of cosmology are assigned to algebraic combinations of the topological invariants of a compact seven-dimensional manifold with exceptional holonomy, together with an E₈ × E₈ gauge structure.

A **seven-dimensional manifold** is a curved space with seven dimensions. **Holonomy** measures how a vector changes when carried around a closed loop in that space. For most manifolds this change can be any rotation. Certain manifolds have holonomy restricted to a subgroup, and in seven dimensions there is an exceptional one, **G₂**, of dimension 14, the automorphism group of the octonions. Manifolds with G₂ holonomy are rare and difficult to construct.

The **topological invariants** of such a manifold are integers that characterize its shape independently of its metric. The most important are the **Betti numbers** *b₂* and *b₃*, which count the harmonic 2-forms and 3-forms the space can carry. They are whole numbers and cannot vary continuously.

The framework posits a manifold *K₇* with (*b₂*, *b₃*) = (21, 77), together with E₈ × E₈, of dimension 496. From these and a few related integers (twenty structural constants in all), it writes formulas such as

- sin²θ_W = *b₂* / (*b₃* + dim G₂) = 3/13,
- *Q*_Koide = dim G₂ / *b₂* = 2/3,
- *m*_τ / *m*_e = 7 + 10 × 248 + 10 × 99 = 3477.

**E₈** is the largest exceptional Lie group. The framework does not try to embed the Standard Model's particles in E₈, an approach shown to be impossible by Distler and Garibaldi in 2010. It uses E₈ × E₈ as a source of group-theoretic integers, which avoids that obstruction and also means that it makes no claim about how the fermions arise.

## A correspondence, not a derivation

This is the point on which version 3.6 differs most from what came before, and it is worth stating bluntly.

**No geometric map is known that sends the invariants of K₇ to the observables.** The formulas are *assigned*: nothing in the geometry says that sin²θ_W must be *b₂* / (*b₃* + dim G₂) and not some other ratio. Earlier versions wrote "derive" for this operation. Version 3.6 withdraws the word.

**No rule fixes which formula goes with which observable.** The grammar and the list of observables were frozen after the formulas had been found.

**The manifold is not constructed.** No compact torsion-free G₂ manifold with Betti numbers (21, 77) is currently known, and the route proposed in version 3.5 does not produce one. The relations use only the declared integers, not a metric.

What the paper does instead is make the correspondence auditable. It gives the full **dictionary**. It keeps a **residue register** of everything that was set rather than derived: the pair (21, 77), an imposed normalization det(g) = 65/32, a combination κ_T⁻¹ = 61, the unit in which an integer is read as a CP phase, the scales of the comparisons, the assignments themselves. And it writes a **decision rule** with no repair clause.

K₇ is, in the paper's own terms, a *privileged candidate*: a member of a well-motivated family, designated by the author for reasons that are the author's own and are declared as such. Presenting a privileged candidate as a demonstrated uniqueness is what the earlier versions did, and what this one stops doing.

## How the framework was built

The first version, in 2025, carried four adjustable geometric parameters tuned to reproduce about 22 observables. A second version reduced them to three quantities, each a ratio of topological integers. The current structure has no continuously adjustable parameter: the relations are ratios of integers, or use one further declared operation.

Earlier versions of this summary read that trajectory (four, three, zero parameters, with more observables covered each time) as a sign that what was happening was compression and not fitting. That reading does not survive. Removing continuous parameters while choosing formulas from a rich grammar moves the freedom; it does not remove it. The freedom now sits in the choice of formulas, of the vocabulary and of the Betti pair, which is exactly what the residue register records and what the look-elsewhere test below prices.

What the absence of continuous parameters does give is **rigidity**: an integer ratio cannot be nudged, so a single precise measurement can reject a relation. Rigidity exposes a framework to refutation. It does not certify it: an exceptional structure is rigid whether it was derived or chosen for the values it gives.

## Where the 33 relations stand

Against the most recent data (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022), with one convention for all uncertainties, the relations fall into five classes, which are not added into a single score:

- **23 lie within two standard deviations** of the measurement. Among them *Q*_Koide = 2/3, α_s = √2/12, the CP phase read as 197°, and most quark, mixing and cosmological ratios.
- **3 are in tension**, between 2σ and 3σ: *m*_τ/*m*_e = 3477, *m*_W/*m*_Z = 37/42 and Ω_c/Ω_m = 27/32.
- **5 are rejected as exact equalities** at more than 3σ and kept only as numerical proximities: α⁻¹, sin²θ_W = 3/13, *m*_μ/*m*_e, *m*_μ/*m*_τ and *m*_b/*m*_t. The quantities are measured so precisely that a formula 0.2{'main': 'https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md', 'lee': 'https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/', 'concept': 'https://doi.org/10.5281/zenodo.16891489'}way is many standard deviations off.
- **1 lies inside a range** the PDG gives without uncertainty: *m*_s/*m*_d = 20.
- **1 sits in the other octant**: sin²θ₂₃ = 6/11, while the global fit prefers the first octant; the value lies inside the fit's 3σ range.

They are also **not 33 independent tests**. In three sectors there are more relations than quantities: four lepton relations for two mass ratios, three CKM relations for two parameters, seven density relations for two densities. In each sector the relations disagree with one another as exact equalities. Each formula is computed correctly, and the formulas cannot all be true together.

Most of the 23 are tested only weakly: where experimental uncertainties are at the percent level, a percent-level agreement is what a rich vocabulary reaches easily.

## Why the coincidence hypothesis cannot be ruled out

Faced with formulas this close to the data, the question is unavoidable: is this the result of a fishing expedition in an ocean of algebraic combinations?

Earlier versions of this summary answered no, and cited statistical tests: a rank among three million configurations, a P-value, Bayes factors, leave-one-out validations. All of them are withdrawn. They shared one flaw. The alternatives were scored with K₇'s own formulas, which had been chosen for (21, 77); no alternative was allowed to search for its own. Under that design, (21, 77) wins by construction.

Version 3.6 replaces them with a preregistered test in which **every competitor searches for its own formulas**, in the same grammar, with the same budget and the same freedom of assignment. The result:

- K₇ reaches 31 of the 33 targets.
- 1 085 of 4 159 alternative Betti pairs reach as many, and 1 015 of 2 000 invented vocabularies reach as many. None reaches more.
- A witness with no K₇ constant at all, using only the universal symbols of the grammar, reaches 30.

The preregistered verdict: the look-elsewhere effect is not overcome, and the P-value is withdrawn from the text. **Closeness to the measured values is not, by itself, evidence for K₇.** This is not a refutation either: the test says that the score does not discriminate, not that the framework is wrong.

What survives the test is modest and real: rigidity under a dictionary fixed in advance, and a written record of what was chosen.

## How a relation can fail

The relations are stated as exact equalities with no theoretical uncertainty. A relation is rejected when its reference data series excludes its value at 3σ. No formula, unit, scale or dataset is changed afterwards to rescue it.

**The CP phase.** The structure produces the integer 197. Reading it in degrees is a choice, declared as such. DUNE and Hyper-Kamiokande will measure δ_CP; a global fit whose 3σ interval excludes 197° rejects the relation together with the choice of unit. Today the fit gives 212 (+26/−36)°.

**The octant of θ₂₃.** A fit whose 3σ interval excludes 6/11 rejects that relation.

**The tau mass.** Two relations give 1776.74 and 1776.97 MeV; a precise enough measurement must reject at least one.

**A fourth generation** would reject the integer identity *N*_gen = 3.

A rejection rejects a relation and the assignment behind it. It does not by itself reject the programme, and the paper says so in advance so that it cannot be said later as a repair. Conversely, a confirmation would show that an assignment agrees with the world, not that the structure requires it. Two results outside the reference series already contradict a relation (the SH0ES value of the Hubble constant, the CDF II W mass) and are reported beside it.

## What K₇ is not

K₇ is not a theory of everything. It does not address quantum gravity or the measurement problem.

K₇ is not a derivation of the Standard Model. Its smooth manifold does not yield the chiral non-abelian content of the Standard Model, and its relations do not come from a four-dimensional effective theory.

K₇ is not a cosmogony. It proposes no mechanism for the selection of the manifold. Five routes to deriving (21, 77) have been investigated and closed without success; one numerical observation remains, *b₂* + *b₃* = 98 = 7 × 14, held as a target and not as a theorem.

K₇ does not depend on any reading of the word *information*. The relations stand or fall independently of what "information" ultimately is. The lineage that motivated the work (Wheeler's "it from bit", Bekenstein's bound, Jacobson's thermodynamic derivation of Einstein's equations, the holographic programme) makes the idea that geometry and information are related less exotic than it sounds; it is neither required nor supported by the relations. A separate essay discusses it ([*Gift from Bit*](https://arithmon.substack.com/p/gift-from-bit)).

## The open questions

- **Existence.** A compact torsion-free G₂ manifold with (21, 77) is not constructed.
- **Physics.** No mechanism leads from a smooth K₇ to the chiral Standard Model.
- **Selection.** Nothing selects (21, 77); it is chosen.
- **Assignment.** No rule assigns formulas to observables.
- **Dependencies.** The audit of the dependencies among the 33 relations is not complete, so no count of independent tests is given.

## What remains to be seen

The paper does not claim that the framework is correct. It may be a genuine structural insight, an approximation to one, or an elaborate coincidence. The aim of version 3.6 is that whichever it is can be found out, and that a reader can see, at every step, what was derived, what was assumed, and what would bring it down.

That is a smaller claim than the one this page used to make. It can be checked.

---

*For the full statement, see the [main paper](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) and its supplements; the code and results of the look-elsewhere test are [public](https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/). The latest deposited version is always at the Zenodo concept DOI [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489).*
