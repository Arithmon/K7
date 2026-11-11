---
title: "Home"
layout: default
---

# The K₇ Framework

**A declared correspondence between G₂ topology and 33 dimensionless parameters, stated with its dictionary, its residue and a decision rule.**

The K₇ framework assigns 33 dimensionless Standard-Model and cosmological parameters to closed forms in the invariants of a G₂-holonomy seven-manifold K₇ with Betti numbers (b₂, b₃) = (21, 77), together with E₈×E₈. Version 3.6 presents this as a correspondence, not a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable. K₇ is a privileged candidate chosen by the author, and the paper says so.

---

## At a Glance

| | |
|----------|-------|
| **What is proposed** | 33 relations with no continuously adjustable parameter, written in twenty declared structural constants |
| **What is set, not derived** | the residue register R1–R12: the Betti pair (21, 77), the imposed normalization det(g) = 65/32, κ_T⁻¹ = 61, the unit in which 197 is read as a CP phase, the comparison scales, the formula assignments |
| **Against current data** | 23 within 2σ, 2 in tension, 6 rejected as exact equalities and kept as proximities, 1 inside a PDG range, 1 with an unresolved octant (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022) |
| **Look-elsewhere** | not overcome: when every competitor searches for its own formulas, 1 085 of 4 159 Betti pairs and 1 015 of 2 000 invented vocabularies reach as many targets as K₇ (global p-value 0.51) |
| **Lean 4 verification** | the arithmetic of the 33 relations (`relations_v36_certified`), 156 files, 14 axioms, no `sorry`; it verifies stated arithmetic, not physical content |
| **Existence of K₇** | open: no compact torsion-free G₂ manifold with (21, 77) is currently constructed |
| **Further dataset entries** | 62 conditional extractions and diagnostics, kept for traceability and not counted as predictions |

---

## Quick Links

| | |
|---|---|
| **New here?** | [Getting Started](Getting-Started.html): Pick your path |
| **Read papers** | [Paper Main Framework](Paper-Main-Framework.html) ([Paper Explicit G2 Metric](Paper-Explicit-G2-Metric.html)) [Paper Spectral Geometry](Paper-Spectral-Geometry.html) |
| **Browse the relations** | [Observable Reference](Observable-Reference.html): the 33 relations with formulas, data and status |
| **How distinctive is it?** | [Statistical Evidence](Statistical-Evidence.html): the look-elsewhere test |
| **Check proofs** | [Lean Formalization](Lean-Formalization.html) |

---

## The 33 Relations in Five Classes

The classes are not added into a single score (main paper §4.2).

| Class | Count | Relations |
|-------|:-----:|-----------|
| within 2σ | 23 | the remaining relations |
| tension (between 2σ and 3σ) | 2 | m_τ/m_e, Ω_c/Ω_m |
| proximity (beyond 3σ, rejected as an exact equality) | 6 | α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t (in the declared mass scheme), m_W/m_Z |
| inside the PDG range (no uncertainty given) | 1 | m_s/m_d |
| non-Gaussian profile, octant unresolved | 1 | sin²θ₂₃ |

A sample, one or two per class:

| Observable | K₇ formula | K₇ value | Measured | Pull | Status |
|------------|-------------|-------|------|------|------|
| Q_Koide | dim(G₂)/b₂ = 2/3 | 0.666667 | 0.6666645(51) | +0.4σ | within 2σ |
| α_s(M_Z) | √2/(dim(G₂) − p₂) = √2/12 | 0.117851 | 0.1180(9) | −0.2σ | within 2σ |
| δ_CP | 7·14 + 99 = 197, read in degrees | 197° | 212 (+26/−36)° | −0.4σ | within 2σ; unit assignment |
| Ω_DE | ln 2 · 98/99 | 0.686146 | 0.6847(73) | +0.2σ | within 2σ |
| m_τ/m_e | 7 + 10·248 + 10·99 | 3477 | 3477.37(18) | −2.1σ | tension |
| m_W/m_Z | 37/42 | 0.880952 | 0.881285(87) | −3.8σ | proximity |
| sin²θ_W(M_Z) | 21/91 = 3/13 | 0.230769 | 0.23122(6) | −7.5σ | proximity |
| m_μ/m_τ | 10/168 | 0.059524 | 0.0594612(30) | +20.8σ | proximity |
| m_s/m_d | 4 × 5 = 20 | 20 | 17–22 (range) | n/a | inside the PDG range |
| sin²θ₂₃ (PMNS) | 6/11 | 0.545455 | 0.470 (+17/−14) | +4.4σ* | tension: second octant, inside the NuFIT 3σ range (*the profile is not Gaussian, so the Gaussian pull overstates it) |

**They are not 33 independent tests.** Three sectors are overdetermined, and in each the relations disagree with one another as exact equalities: four lepton relations on two mass ratios, three CKM relations on two Wolfenstein parameters, seven density relations on two independent densities. None is selected after the fact.

## Decision Rule

The relations are stated as exact equalities. A relation is rejected when its reference series (PDG, NuFIT, Planck, CODATA) excludes its value at 3σ; no formula, unit, scale or dataset is changed afterwards to rescue it (main paper §11).

| # | Relation | Value | Rejected when | Where |
|---|----------|-------|---------------|-------|
| D1 | δ_CP, the phase 2π·197/360 | 197° | a global fit whose 3σ interval excludes 197°; the unit assignment is rejected with it | DUNE, Hyper-Kamiokande |
| D2 | sin²θ₂₃ | 6/11 | a global fit whose 3σ interval excludes 6/11, in either octant | DUNE, Hyper-Kamiokande |
| general rule | sin²θ₁₂ | 4/13 | a global fit whose 3σ interval excludes 4/13 | JUNO (first result 0.3092 ± 0.0087; about four times tighter than today's global fit after six years) |
| D3 | m_τ/m_e and Q_Koide | 1776.74 and 1776.97 MeV for m_τ | an m_τ value whose 3σ interval excludes the value, each relation separately | Belle II, BES III |
| D4 | N_gen | 3 | a fourth sequential generation | LHC, FCC |
| D5 | m_s/m_d | 20 | a lattice determination with an uncertainty whose 3σ interval excludes 20 | lattice QCD |

A rejection rejects the relation and the assignment that produced it, not the programme by itself. A confirmation would show that an assignment agrees with the world, not that the structure requires it.

## What Version 3.6 Withdraws

Earlier versions of this site said that the relations are derived from the geometry, that the framework has no free parameter and cannot be fitted, that it predicts 95 observables with a small mean deviation, and that a coincidence probability or a P-value measured its distinctiveness. Version 3.6 withdraws each of these. The full list is in the main paper (§12.1) and in the [changelog](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_CHANGELOG.md).

---

## Outreach

Accessible writing on the ideas behind K₇ lives on the [Substack blog](https://arithmon.substack.com/), in three tracks: [The Series](Blog-Index.html#series) (physics through the games you have already played), [The Ideas](Blog-Index.html#ideas) (why the constants might not be arbitrary), and [The Story](Blog-Index.html#story) (an independent researcher, an AI, and a year of unorthodox research). The full list with French translations is in the [Blog Index](Blog-Index.html). Latest: *[Can you hear the shape of a balloon?](https://arithmon.substack.com/p/can-you-hear-the-shape-of-a-balloon)*, a school formula taken apart, and symmetry as information saved.

---

## Structure

This wiki consolidates K₇ documentation across three repositories:

- **[Arithmon/K7](https://github.com/Arithmon/K7)**: Theoretical documentation, papers, outreach
- **[Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean)**: Lean 4 proofs, Python package, blueprint
- **Zenodo deposits**: Archived data with DOIs

Browse the sidebar for full navigation, or see the [Site Map](Site-Map.html) for a complete index.

---

*The K₇ Framework v3.6 | [GitHub](https://github.com/Arithmon/K7) | [Core](https://github.com/Arithmon/K7-Lean) | [Blueprint](https://arithmon.github.io/K7-Lean/) | [Zenodo (Paper A)](https://doi.org/10.5281/zenodo.19892350) · [Paper B](https://doi.org/10.5281/zenodo.19893371) · [Paper C](https://doi.org/10.5281/zenodo.19708916) | MIT License*
