---
title: "Paper S1 Foundations"
layout: default
---

# Paper: S1, Mathematical Foundations

**Supplement S1: Mathematical Foundations. E₈ Exceptional Lie Algebra, G₂ Holonomy Manifolds, and K₇ Construction** (The K₇ Framework, v3.6)

*Brieuc de La Fournière (2026)*

[**PDF (25 pp.)**](https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_S1_foundations.pdf) | concept DOI [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489) (version 3.6 not yet deposited) | [Markdown](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S1_foundations.md)

---

## What the supplement contains

The mathematical background of the dictionary: the E₈ data it uses, G₂ holonomy manifolds, the topological status of K₇ and the algebraic reference form.

Three points of status, stated in the supplement itself:

- **The pair (b₂, b₃) = (21, 77) is posited.** It has no known construction: it does not appear among the catalogued compact G₂ manifolds, and the Joyce–Karigiannis route proposed in version 3.5 does not realise it (S1 §8.4; v3.5 erratum, §9).
- **det(g) = 65/32 is an imposed normalization** of the reference form (residue R2), not a result.
- **Joyce's perturbation theorem is not applied to a compact K₇ here**: its smallness constant depends on geometric quantities that are not controlled for this setting (S1 §11).

---

## The twenty structural constants

From main §3.1; the *status* column separates Lie data, posited inputs and combinations built by the framework's own choices.

| # | Constant | Value | Origin | Status |
|---|----------|-------|--------|--------|
| 1 | dim(E₈) | 248 | Lie algebra | Lie datum |
| 2 | rank(E₈) | 8 | Cartan subalgebra | Lie datum |
| 3 | dim(G₂) | 14 | Aut(𝕆) | Lie datum |
| 4 | dim(K₇) | 7 | Im(𝕆) | topological |
| 5 | b₂(K₇) | 21 | posited (§10) | input |
| 6 | b₃(K₇) | 77 | posited (§10) | input |
| 7 | dim(J₃(𝕆)) | 27 | exceptional Jordan algebra | Lie datum |
| 8 | N_gen | 3 | b₂/dim(K₇); the integer identity of §2.4 | measured, reproduced |
| 9 | p₂ | 2 | dim(G₂)/dim(K₇) ("binary ratio"; not a Pontryagin class) | combination |
| 10 | Weyl | 5 | factor of \|W(E₈)\| | combination |
| 11 | H* | 99 | b₂ + b₃ + 1 | combination |
| 12 | dim(E₆) | 78 | Lie algebra | Lie datum |
| 13 | dim(E₇) | 133 | Lie algebra | Lie datum |
| 14 | dim(F₄) | 52 | Aut(J₃(𝕆)) | Lie datum |
| 15 | fund(E₇) | 56 | fundamental representation | Lie datum |
| 16 | \|PSL(2,7)\| | 168 | automorphisms of the Fano plane | Lie datum |
| 17 | D_bulk | 11 | 4 + 7 | combination |
| 18 | α_sum | 13 | rank(E₈) + Weyl | combination |
| 19 | det_den | 32 | b₂ + dim(G₂) − N_gen | combination; enters det(g) |
| 20 | det_num | 65 | p₂ · det_den + 1 (also Weyl × α_sum) | combination; enters det(g) |

---

## Sections

- 0. Why This Framework Exists
- 1. Root System and Dynkin Diagram
- 2. Weyl Group
- 3. Exceptional Chain
- 4. E₈×E₈ Product Structure
- 5. Exceptional Algebras from Octonions
- 6. Definition and Properties
- 7. Topological Invariants
- 8. Twisted Connected Sum Framework
- 9. Cohomological Structure (Conditional on Existence)
- 10. Structural Metric Invariants
- 11. Reference Form and Formalization
- 12. Analytical G₂ Metric Details
- 13. Changes since Version 3.5

---

## Related

- [Paper Main](Paper-Main-Framework.html)
- [Paper S2 Derivations](Paper-S2-Derivations.html)
- [Paper Explicit G2 Metric](Paper-Explicit-G2-Metric.html)
- [Glossary](Glossary.html)
