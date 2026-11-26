# Lean Formalization

The arithmetic of the K₇ framework is formalized in Lean 4 with Mathlib, in the repository
[Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean). This page says what the formalization
establishes and what it does not. It follows §8 of the [main paper](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) and section S3.7 of
[supplement S3](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S3_observables.md), version 3.6.

## What is formalized

| Item | Value |
|---|---|
| Lean 4 files | 156 |
| Axioms beyond the Mathlib foundations | 14 (4 literature imports, 10 interval certificates) |
| `sorry` | none |
| The 33 relations | collected in `relations_v36_certified` (commit `34ce857`), which depends only on the standard axioms `propext`, `Classical.choice`, `Quot.sound` |

The formalization certifies algebraic identities among the declared integers (for example
b₂ · 13 = 3 · (b₃ + dim G₂) for sin²θ_W = 3/13), the G₂ three-form and dim 𝔤₂ = 14, the E₈ root
system, and the arithmetic of several numerical certificates.

## The form of the 33 statements

Each relation has a statement that ties its closed form, written in the structural constants, to its
value. The forms differ, and S3.7 gives the declaration and the line for each:

- an exact equality for 27 relations, between rationals for 25 of them and between natural numbers
  for m_τ/m_e and m_s/m_d;
- a closed form in ℝ, with no numerical bound, for α_s, λ_H, Ω_DE and n_s;
- the base 27 and the bounds 206 < 27^φ < 209 for m_μ/m_e, an interval wider than the deviation it is
  compared with;
- the integer 197 for δ_CP, whose reading in degrees is an assignment of the dictionary.

## The fourteen axioms

`relations_v36_certified` uses none of them. They are used elsewhere in the library.

| Axiom | File | Kind |
|---|---|---|
| `spectral_upper_bound` | `GIFT/Spectral/TCSBounds.lean` | literature import |
| `neck_dominates` | `GIFT/Spectral/TCSBounds.lean` | literature import |
| `cheeger_inequality` | `GIFT/Spectral/CheegerInequality.lean` | literature import |
| `literature_package` | `GIFT/Spectral/LiteratureAxioms.lean` | literature import |
| `det_g_at_half` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_0` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_1` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_2` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_3` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `det_g_at_half_bracketed` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_0_bracketed` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_1_bracketed` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_2_bracketed` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |
| `K3_eigenvalue_3_bracketed` | `GIFT/Foundations/IntervalCertificates.lean` | interval certificate |

The four literature imports state results taken from published work; the ten interval certificates
import numerical enclosures computed outside Lean.

## What the formalization does not establish

- **Not the physics.** A machine-checked formula is a formula whose arithmetic is right. Which formula
  is assigned to which observable is a choice of the author, recorded in the paper's dictionary.
- **Not the consistency of the relations taken together.** Formulas that are each computed correctly
  disagree with one another, as exact equalities, in the three overdetermined sectors (main §4.2).
- **Not the existence of K₇.** No compact G₂ manifold with Betti numbers (21, 77) is known (main §9).

## Checking it yourself

```bash
git clone https://github.com/Arithmon/K7-Lean
cd K7-Lean
lake build
```

The statement to inspect is `GIFT.Certificate.RelationsV36.relations_v36_certified`;
`#print axioms` on it lists the axioms it depends on.

Counts and statements of earlier versions of this page (numbers of relations, "zero domain-specific
axioms", earlier certificate names) described earlier states of the library and are withdrawn.
