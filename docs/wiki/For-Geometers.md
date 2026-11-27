---
title: "For Geometers"
layout: default
---

# For Geometers

What is known, and what is not, about the geometry the K₇ framework posits. This page follows §2.3
and §9 of the [main paper](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) and §8 of [supplement S1](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S1_foundations.md), version 3.6. It replaces an earlier
page that described a twisted-connected-sum construction of K₇; that construction is withdrawn.

## What the framework posits

A compact, simply connected seven-manifold K₇ with holonomy G₂ and Betti numbers (b₂, b₃) = (21, 77).
The 33 relations of the paper use only these integers and Lie-theoretic data, never a metric.

**No compact G₂ manifold with these Betti numbers is known.** Whether one exists is open.

## What is excluded

- **Catalogued examples.** The pair (21, 77) does not appear among Joyce's orbifold constructions or
  among the twisted connected sums of Corti, Haskins, Nordström and Pacini.
- **Ordinary twisted connected sums, all of them.** For every ordinary twisted connected sum
  b₂ + b₃ is odd (Nordström, *Extra-twisted connected sum G₂-manifolds*, Introduction, property (i));
  here b₂ + b₃ = 98. Within this family only the extra-twisted connected sums, which carry no
  parity constraint, remain open.
- **The building-block decomposition 11 + 10.** The table that stood on this page (two blocks with
  b₂ = 11 and b₂ = 10 glued into (21, 77)) is withdrawn: such sublattices of the K3 lattice do not
  support a twisted-connected-sum realisation (S1 §8.3).
- **A Joyce–Karigiannis ℤ₂³ orbifold route.** It does not realise (21, 77): the group action forces
  b₂ ≥ 5 and b₃ ≤ 16 on the quotient for every compatible torus action (S1 §8.4).

## What is established, locally

- **A certified local metric** (companion paper A, [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069)).
  An explicit approximate G₂ metric on a neck region, with 169 Chebyshev–Cholesky parameters, carries
  a Newton–Kantorovich certificate (h = 8.95 × 10⁻⁹ by the analytical bound, 1.43 × 10⁻⁹ by the sharper
  numerical one) for a nearby torsion-free metric within a ball δg/g ≤ 1.35 × 10⁻⁷. The certificate is local: it does not construct a compact K₇, and the
  smallness constant of Joyce's perturbation theorem depends on geometric bounds that are not
  established here (S1).
- **Its numerical spectrum** (companion paper B, [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367)).
  It gives no independent evidence for (21, 77): the multiplicities it reports are built from
  decompositions that S1 withdraws.
- **A closed-form neck ansatz** (companion paper D, [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065)):
  a positive G₂ three-form on a neck region with K3 coassociative fibres, with its own certificate.
- **A conditional analytic scheme** (companion paper E, [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956))
  for a fibration K₇ → S³ with 77 branch components. It is computed at a datum that is not realisable
  as posed, so no existence argument for the compact K₇ currently holds.
- **The K3 fibre.** No certified bound on a Ricci-flat metric of the K3 fibre is available. An explicit
  K3 surface has a publicly certified holomorphic atlas, with no metric claim
  ([10.5281/zenodo.22047469](https://doi.org/10.5281/zenodo.22047469)).

## What an existence proof would need

Main §9.1 lists it: a realisable datum, and then the global analytic steps that are open problems.
Until then the framework's geometric input is a posited topology, recorded as item R1 of its residue
register.

## Code

The project's Python package is in [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean)
(`contrib/python`); the numerical artefacts of the certificates are in the Zenodo deposits of the
companion papers. Statements made by earlier versions of this page about Joyce's threshold,
about Betti numbers read from spectra, and about typical bounds on b₂ are withdrawn.
