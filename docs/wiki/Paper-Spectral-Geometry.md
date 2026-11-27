---
title: "Paper Spectral Geometry"
layout: default
---

# Paper B: Spectral Geometry of the Neck-Model Metric

**Spectral Geometry of an Explicit G₂ Metric: Laplacian Spectrum and Harmonic Forms**

*Brieuc de La Fournière (2026)*

[PDF](https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/g2_spectral.pdf) | [Markdown](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/g2_spectral.md) | [DOI: 10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367)

> **Scope.** Every spectral result of this paper is a property of the explicit neck-model metric of [paper A](Paper-Explicit-G2-Metric.html), on K3 × T² × [0,1]. The paper states that their reading on a closed manifold is conditional on a compact G₂ manifold with (b₂, b₃) = (21, 77), and none is known. Version 3.6 of the framework paper adds that the multiplicities 21 and 77 found here are built from decompositions that supplement S1 withdraws (§8.3, §9.3): they give no independent evidence for the pair (main §2.3).

---

## What the paper does

It computes the spectrum of the scalar Laplacian and of the Hodge Laplacians on the metric of paper A, and the harmonic forms that go with it.

## Reported figures

| Quantity | Value |
|----------|-------|
| Scalar spectral gap | λ₁ = 0.12461 ± 0.00016 (Richardson extrapolation across six grids) |
| Analytical formula, written after the fact from the certified seam parameters | λ₁ = π²/(L² g_ss) = 6π²/475 ≈ 0.12467, within 0.05% |
| Weyl exponent | α = 1.998 (adiabatic value: 2) |
| Near-zero eigenvalues of Δ₂ | 21, with a gap ratio of 14,635 |
| Near-zero eigenvalues of Δ₃ | 77 |
| Intersection form of the 21 two-forms on the K3 fiber | signature (3, 18), a rank-21 restriction of the K3 lattice (3, 19) |
| Self-dual to anti-self-dual eigenvalue gap | 2,210 |
| Spectral democracy of paper A | checked numerically to 10⁻⁵ |
| Kaluza–Klein tower | 22,671 levels, Poisson level-spacing statistics |

The counts 21 and 77 are multiplicities of the model, chosen to match the pair the framework posits; they are not a computation of the Betti numbers of a compact manifold.

## Sections

1. Introduction
2. The Certified Metric (Summary)
3. Laplacian Spectrum
4. Harmonic Forms and Intersection Theory
5. Spectral Democracy (Numerical Verification)
6. Discussion

Appendix A: convergence analysis. A companion notebook is in [`publications/papers/notebooks/`](https://github.com/Arithmon/K7/tree/main/publications/papers/notebooks).

## How the framework paper uses it

The framework paper cites this analysis with the statement that it gives no independent evidence for (b₂, b₃) = (21, 77) (main §2.3). No mass ratio read from this spectrum is one of the 33 relations.

---

## Related

- [Paper Explicit G2 Metric](Paper-Explicit-G2-Metric.html): the metric this paper analyzes
- [Paper S1 Foundations](Paper-S1-Foundations.html): what is and is not constructed
- [For Geometers](For-Geometers.html)
