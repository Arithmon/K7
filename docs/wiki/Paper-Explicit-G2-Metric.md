---
title: "Paper Explicit G2 Metric"
layout: default
---

# Paper A: A Certified G₂ Structure on a Neck Model

**A Certified Torsion-Free G₂ Structure on a TCS Neck Model via Computer-Assisted Proof**

*Brieuc de La Fournière (2026)*

[PDF](https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/g2_certified_neck.pdf) | [Markdown](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/g2_certified_neck.md) | [DOI: 10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069)

> **Scope.** The result is local. The paper certifies a torsion-free G₂ structure on a neck model, K3 × T² × [0,1]; it does not construct a compact seven-manifold. No compact G₂ manifold with Betti numbers (b₂, b₃) = (21, 77) is known, and every ordinary twisted connected sum is excluded by parity (framework paper, S1 §8.3). The paper's own abstract states the compact case as conditional on the existence of such a manifold.

---

## What the paper does

It writes an explicit G₂ structure on the neck model, with a metric of product type, g = g_seam(s) ⊕ g_{T²} ⊕ g_{K3}(y), and 169 parameters (168 Chebyshev–Cholesky coefficients and one decay rate). It then certifies, by a Newton–Kantorovich argument in interval arithmetic, that a unique torsion-free G₂ structure exists near it. The certificate is relative to a fixed K3 input, which is a neural-network metric.

## Certified figures

| Quantity | Value |
|----------|-------|
| Newton–Kantorovich contraction parameter, analytical certificate | h ≤ 8.95 × 10⁻⁹ (β = 0.321, from a Sturm–Liouville bound) |
| The same with the numerical β = 0.02961 | h ≤ 1.43 × 10⁻⁹ |
| Threshold | 1/2 |
| Seam-sector torsion at the Newton–Kantorovich iterate | η ≤ 2.949 × 10⁻⁵ |
| Torsion of the full seven-dimensional product metric | ‖T(g*)‖_{C⁰} ≤ 1.59 × 10⁻³ |
| Empirical seven-dimensional maximum over 220,000 K3 fiber points | 3.154 × 10⁻⁵ |
| Solution space | finite-dimensional, ℝ¹⁶⁸ |

## Other statements of the paper

- The optimized parameters are close, with sub-percent deviations, to five constants: g_ss ≈ 19/6, g_{T²} ≈ 7/6, g_{K3} ≈ 64/77, det(g) = 65/32 and γ = 2π√(6/7). In the framework paper, det(g) = 65/32 is an imposed normalization (residue register, main §3.3), not a prediction.
- The torsion-free condition reduces the anisotropy of the K3 fiber from 10:1 to 1.012:1.
- Product-type Ricci-flat G₂ metrics satisfy what the paper calls spectral democracy (its Theorem 1.3, proved analytically).

## Sections

1. Introduction
2. The Manifold and its Topological Context
3. The Metric
4. Torsion Analysis
5. Newton–Kantorovich Certification
6. Spectral Democracy
7. Discussion

Appendices: A (metric data), B (Newton–Kantorovich proof chain), C (K3 fiber clarification). A companion notebook is in [`publications/papers/notebooks/`](https://github.com/Arithmon/K7/tree/main/publications/papers/notebooks).

## How the framework paper uses it

Version 3.6 of the framework paper cites this result as "a Newton–Kantorovich-certified local metric" (main §2.3 and §9.3): it certifies the gluing region that would appear in a twisted-connected-sum construction, subject to that gluing being available. The numerical diagnostics computed on this metric are conditional or diagnostic entries of the dataset; they describe the approximate metric and are not observables (main §5.5).

---

## Related

- [Paper Spectral Geometry](Paper-Spectral-Geometry.html): the spectrum of this metric
- [Paper S1 Foundations](Paper-S1-Foundations.html): what is and is not constructed
- [For Geometers](For-Geometers.html)
