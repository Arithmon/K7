# The Constants of Nature Are Counts

### A declared correspondence for the Standard Model parameters, and the measurements that can reject it

Brieuc de La Fournière · Arithmon program · [arithmon.com](https://arithmon.com)

---

The hypothesis: the dimensionless constants of physics are counts, the invariants of a geometry, not settings. The K₇ framework is one dated answer to it. It assigns 33 closed forms, written in the invariants of a posited seven-dimensional geometry and of E₈×E₈, to 33 dimensionless parameters of particle physics and cosmology.

It is a candidate, not a derivation. No geometric map is known that sends the invariants to the observables, and no rule fixes which formula goes with which observable: the assignments are the author's, and they are written down as such.

What the framework offers instead of a derivation is a way to be wrong. An integer ratio cannot be nudged. Each relation is stated as an exact equality, and it is rejected when the reference data exclude its value at 3σ. Nothing is added afterwards.

---

## What is stated

| | |
|---|---|
| The geometry | a compact G₂-holonomy seven-manifold with Betti numbers (b₂, b₃) = (21, 77), **posited**: no such manifold is known |
| The dictionary | twenty structural constants and a grammar of formulas |
| The residue register | twelve items, R1 to R12: everything that was set by choice rather than obtained |
| The relations | **33**, none with a continuously adjustable parameter |
| Formal verification | the arithmetic of the 33 relations is machine-checked in Lean 4, with no unproven step; this certifies the arithmetic, not the physics |

## Where the 33 stand

Against the most recent data (PDG 2026, NuFIT 6.1, Planck 2018):

| Class | Count |
|---|---|
| within 2σ of measurement | 23 |
| in tension, between 2σ and 3σ | 2 |
| excluded as exact equalities at more than 3σ, kept as numerical proximities | 6 |
| inside a PDG range that carries no uncertainty | 1 |
| non-Gaussian profile (sin²θ₂₃, in the octant the global fit disfavours) | 1 |

These are not 33 independent tests. Three sectors are overdetermined, and their relations disagree with one another as exact equalities. The other 62 entries of the dataset are conditional extractions and diagnostics, and are not counted.

## Is the agreement distinctive? No

In a preregistered test, every competitor searches for its own formulas in the same grammar and at the same budget. K₇ reaches 31 of the 33 targets. So do 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies, and a control with no K₇ constant reaches 30. As preregistered, no p-value is reported: closeness to today's values is not, by itself, evidence. The coincidence probabilities published with earlier versions are withdrawn.

## What can reject it

| Relation | Value | What rejects it |
|---|---|---|
| δ_CP, the phase 2π · 197/360 | 197° | a global fit, including DUNE or Hyper-Kamiokande, whose 3σ interval excludes 197° |
| sin²θ₁₂ | 4/13 | JUNO, whose six-year precision is about four times tighter than the present global fit |
| sin²θ₂₃ | 6/11 | a global fit whose 3σ interval excludes 6/11, in either octant |
| m_τ/m_e | 3477 | a τ-mass measurement that excludes 1776.74 MeV |

Reading the integer 197 as an angle in degrees is itself an assignment of the dictionary. If the δ_CP relation is rejected, that assignment goes with it.

## What is open

Does the geometry exist? No compact G₂ manifold with these Betti numbers is known; every ordinary twisted connected sum is excluded, and one orbifold route is closed. Where does the gauge sector come from? The Standard-Model algebra sits inside E₈ through a chain of embeddings, which is not a breaking mechanism; none is specified. Why (21, 77)? The pair is an input: five routes to deriving it were audited and closed, and one identity, b₂ + b₃ = 98 = dim(K₇) · dim(G₂), remains as an observation.

---

## The question

Most proposals that attempt to explain the constants of Nature eventually fail. Perhaps this one will too. The question does not go away with them: if the constants are not fundamental, they come from somewhere. This is one attempt, with its assumptions listed, its calculations reproducible, and its routes to rejection stated in advance.

---

<sub>Version 3.6 of the framework paper, "The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology", with its supplements, data and code: [github.com/Arithmon/K7](https://github.com/Arithmon/K7), [doi.org/10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489). A numerical G₂ dataset from this work is cited as reference 25 in *Physics Letters B* **878** (2026) 140566.</sub>
