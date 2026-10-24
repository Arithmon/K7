# The K₇ Framework

> ### This repository has moved
>
> **`gift-framework/GIFT` → [`Arithmon/K7`](https://github.com/Arithmon/K7)**
>
> The framework is now presented as the **K₇ framework**; *GIFT* remains the name of its
> founding phase. The move consolidates it under the [Arithmon](https://github.com/Arithmon)
> organisation alongside Atlas, Program, Lean and Sieve (moved 2026-07-14).
>
> **Nothing you cite will break.** GitHub redirects the old URLs (web *and* `git clone` /
> `fetch` / `push`), and the published papers cite `github.com/gift-framework/*`: those
> redirects are load-bearing infrastructure, so the old paths will never be reused.
>
> One thing does *not* redirect: the documentation site moves from
> `gift-framework.github.io/GIFT/` to `arithmon.github.io/K7/`.
>
> Companion repository: `gift-framework/core` → [`Arithmon/K7-Lean`](https://github.com/Arithmon/K7-Lean) (moved 2026-07-14).

---


[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Lean 4](https://img.shields.io/badge/Lean_4-arithmetic_verified-blue)](https://github.com/Arithmon/K7-Lean)

Part of the **[Arithmon program](https://github.com/arithmon)**.

> **Branch `v3.6-draft`.** This README describes version 3.6 of the framework paper, in preparation. The published version is 3.5 (Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168)), read together with its [erratum](publications/ERRATUM_v3.5.md).

**A declared correspondence, stated with its dictionary, its residue and a decision rule.**

The K₇ framework assigns 33 dimensionless Standard-Model and cosmological parameters to closed forms in the invariants of a G₂-holonomy seven-manifold K₇ with Betti numbers (b₂, b₃) = (21, 77), together with E₈×E₈. Version 3.6 presents this as a correspondence, not a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable. What the paper does is make the correspondence auditable.

| | |
|---|---|
| **What is proposed** | 33 relations with no continuously adjustable parameter, written in twenty declared structural constants (main §3) |
| **What is set, not derived** | the residue register R1–R12: the Betti pair, the imposed normalization det(g) = 65/32, κ_T⁻¹ = 61, the unit in which 197 is read as a CP phase, comparison scales and mass schemes, the formula assignments, and the choice among incompatible relations in three overdetermined sectors (main §3.3) |
| **What is established** | the arithmetic identities stated for the relations, machine-checked in Lean 4 (exact for 24 of the 33; see S3.7); a Newton–Kantorovich-certified seam metric ([A]) |
| **What is open** | a compact torsion-free G₂ manifold with (21, 77): **no construction is currently known**, and the Joyce–Karigiannis route of v3.5 does not realize the pair ([erratum](publications/ERRATUM_v3.5.md) §9); a physical mechanism to the chiral Standard Model; the selection of (21, 77); an assignment rule |
| **What would refute it** | the decision rule of main §11, written in advance with no repair clause |

---

## The 33 relations against current data

Data: PDG 2026, NuFIT 6.1 (normal ordering, with atmospheric data), Planck 2018 (one column), CODATA 2022; all uncertainties at 1σ, correlations neglected. The relations fall into six classes, which are not added into one score (main §4.2):

| Class | Count | Relations |
|-------|:-----:|-----------|
| within 2σ | 24 | |
| tension (between 2σ and 3σ) | 2 | m_τ/m_e, m_W/m_Z |
| proximity (beyond 3σ, excluded as an exact equality) | 4 | α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ |
| inside the PDG range (no uncertainty given) | 1 | m_s/m_d |
| non-Gaussian profile, octant unresolved | 1 | sin²θ₂₃ = 6/11 |
| depends on the mass scheme | 1 | m_b/m_t |

**They are not 33 independent tests.** Three sectors are overdetermined, and in each the relations disagree with one another as exact equalities: four lepton relations on two mass ratios, three CKM relations on two Wolfenstein parameters (sin θ₂₃ = Aλ², 2.6% apart), seven density relations on two independent densities. None is selected after the fact.

**Closeness is not distinctive.** In a preregistered look-elsewhere test, each competitor searches for its own formulas in the same grammar and budget. K₇ reaches 31 of the 33 targets; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many, and none reaches more (P_global = 0.51, S4). The coincidence probabilities of earlier versions (10⁻³⁴⁶, 10⁻¹³³, P < 5 × 10⁻⁶) are withdrawn.

---

## Decision rule (main §11)

The relations are stated as exact equalities; a relation is rejected when a measurement's 3σ interval excludes its value. No theoretical tolerance is added afterwards.

| # | Relation | Value | Rejected when |
|---|----------|-------|---------------|
| D1 | δ_CP, the phase 2π · 197/360 | 197° | a 3σ interval (DUNE, Hyper-Kamiokande, or a global fit) excludes 197°; the unit assignment is rejected with it |
| D2 | sin²θ₂₃ | 6/11 | a 3σ interval excludes 6/11, in either octant |
| D3 | m_τ/m_e and Q_Koide | 1776.74 and 1776.97 MeV for m_τ | an m_τ measurement excludes the value at 3σ, for each relation separately |
| D4 | N_gen | 3 | a fourth sequential generation |
| D5 | m_s/m_d | 20 | a lattice determination with an uncertainty excludes 20 at 3σ |

A rejection rejects the relation and the dictionary assignment that produced it; it does not by itself reject the programme. A confirmation would show that an assignment agrees with the world, not that the structure requires it.

---

## What version 3.6 withdraws

That the relations are derived from the geometry; "no free parameters, no fitting" as a description of the formula choice; "95 observables" (now 33 relations and 62 conditional or diagnostic entries); a primary lepton relation; the survival of m_H/m_W and Koide in the Sieve; the coincidence probabilities and the P-value of earlier versions; δ_CP as a "pure geometry" prediction read in degrees without saying so; the index-theorem reading of N_gen = 3; the Joyce–Karigiannis realization of (21, 77); the "Joyce threshold, 224× margin"; and the δ_CP compactification factor 62/69 kept as a contingency plan.

---

## Papers

### Framework v3.6 (draft, this branch)

| Document | Markdown |
|----------|----------|
| Main paper | [k7_framework_3_6_main.md](publications/papers/markdown/k7_framework_3_6_main.md) |
| S1: Mathematical foundations | [k7_framework_3_6_S1_foundations.md](publications/papers/markdown/k7_framework_3_6_S1_foundations.md) |
| S2: The 33 relations (arithmetic, dictionary choices, status) | [k7_framework_3_6_S2_derivations.md](publications/papers/markdown/k7_framework_3_6_S2_derivations.md) |
| S3: Observable dataset | [k7_framework_3_6_S3_observables.md](publications/papers/markdown/k7_framework_3_6_S3_observables.md) |
| S4: Look-elsewhere test and descriptive diagnostics | [k7_framework_3_6_S4_sieve_diagnostics.md](publications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md) |
| Changes from v3.5 | [k7_framework_3_6_CHANGELOG.md](publications/papers/markdown/k7_framework_3_6_CHANGELOG.md) |

PDF and LaTeX will be generated at release.

### Framework v3.5 (published: PDF, TeX and markdown, Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168))

Read with the [erratum](publications/ERRATUM_v3.5.md) (sections 1–11).

| Document | PDF | Markdown |
|----------|-----|----------|
| Main Paper (47 pp.) | [PDF](publications/papers/pdf/k7_framework_3_5_main.pdf) | [Markdown](publications/papers/markdown/k7_framework_3_5_main.md) |
| S1: Foundations | [PDF](publications/papers/pdf/k7_framework_3_5_S1_foundations.pdf) | [Markdown](publications/papers/markdown/k7_framework_3_5_S1_foundations.md) |
| S2: Derivations | [PDF](publications/papers/pdf/k7_framework_3_5_S2_derivations.pdf) | [Markdown](publications/papers/markdown/k7_framework_3_5_S2_derivations.md) |
| S3: Observables | [PDF](publications/papers/pdf/k7_framework_3_5_S3_observables.pdf) | [Markdown](publications/papers/markdown/k7_framework_3_5_S3_observables.md) |
| S4: Sieve Diagnostics | [PDF](publications/papers/pdf/k7_framework_3_5_S4_sieve_diagnostics.pdf) | [Markdown](publications/papers/markdown/k7_framework_3_5_S4_sieve_diagnostics.md) |

> LaTeX sources: [`publications/papers/tex/`](publications/papers/tex/). Archives: [`legacy/v3.4/`](publications/papers/legacy/v3.4/), [`legacy/v3.3/`](publications/papers/legacy/v3.3/).

### Companion papers (published on Zenodo)

| Paper | Description | DOI |
|-------|-------------|-----|
| [A: Certified G₂ Structure (PDF)](publications/papers/pdf/g2_certified_neck.pdf) | Newton–Kantorovich certificate for a nearby torsion-free metric on a seam region; it does not construct a compact K₇ | [10.5281/zenodo.19892350](https://doi.org/10.5281/zenodo.19892350) |
| [B: Spectral Geometry (PDF)](publications/papers/pdf/g2_spectral.pdf) | Laplacian spectrum and harmonic forms of the approximate seam metric | [10.5281/zenodo.19893371](https://doi.org/10.5281/zenodo.19893371) |
| [C: Newton-Kantorovich on K3 (PDF)](publications/papers/pdf/K3_NK_Certificate.pdf) | NK diagnostics on a Donaldson K3 metric (CI(2,2,2)) | [10.5281/zenodo.19708916](https://doi.org/10.5281/zenodo.19708916) |
| [D: Donaldson Analytic Note (PDF)](publications/papers/pdf/donaldson_analytic.pdf) | Explicit closed-form G₂ ansatz on a K3-coassociative neck with 5-layer Wirtinger certificate | [10.5281/zenodo.20039066](https://doi.org/10.5281/zenodo.20039066) |
| [E: Rank-1 Branched Adiabatic (PDF)](publications/papers/pdf/rank_one_branched_adiabatic.pdf) | Conditional analytic framework for the neck; the datum-level instantiation at D₀ is not realisable as posed ([erratum](publications/ERRATUM_v3.5.md), section 2) | [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) |

---

## Current analytic scope

The compact K₇ torsion-free existence theorem is not a result of this repository. Status is tracked in [docs/analytic_status.md](docs/analytic_status.md). No compact G₂ manifold with (b₂, b₃) = (21, 77) is currently constructed; the existence layers of main §9 presuppose one.

---

## Start here

| | |
|:---:|:---:|
| [**Watch** (8 min)](https://www.youtube.com/watch?v=6DVck30Q6XM) | [**Read the blog**](https://arithmon.substack.com/) |
| [**K₇ for Everyone**](docs/GIFT_FOR_EVERYONE.md) | [**FAQ**](docs/FAQ.md) |

The guides under `docs/` were written for earlier versions and will be revised for v3.6; where they differ from the paper, the paper and the erratum hold.

---

## Related Repositories

| Repository | Description |
|------------|-------------|
| [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) | Formal verification (Lean 4), K₇ metric pipeline, giftpy (formerly `gift-framework/core`) |

---

## Cited By

- Heyes, Hirst, Sá Earp & Silva, *Neural and numerical methods for G₂-structures on
  contact Calabi-Yau 7-manifolds*, *Physics Letters B* **878** (2026) 140566
  (Imperial College London / UNICAMP). Mapped in the
  [atlas](https://github.com/arithmon/atlas/blob/main/entries/heyes-plb-g2-numerics.md).
- Zhou & Zhou, *Algebraic Stability and Cosmological Structure* (2026): derives
  (b₂, b₃) = (21, 77) from self-referential dynamics, citing this work as empirical
  motivation. Mapped, with the standing caveats, in the
  [atlas](https://github.com/arithmon/atlas/blob/main/entries/zhou-algebraic-stability.md).
- Mamun, *The Void Paradox: Towards a Universal Coordinate System for Information
  Reality* (2026), University of Oxford. Not yet mapped in the atlas.
- Cabannas & Silva, *The Modal Discipline of Objectivity* (2026), UFBA / UFMA.
  Not yet mapped in the atlas.

A citation is not an endorsement, and an atlas entry is not one either: the atlas
records what a neighbouring work claims and where it differs, in both directions.

---

## Connect

| Platform | |
|----------|---|
| Substack | [arithmon.substack.com](https://arithmon.substack.com/) |
| YouTube | [@arithmon](https://youtube.com/@arithmon) |
| X | [@ArithmonProgram](https://x.com/ArithmonProgram) |

| Archive | |
|---------|---|
| Zenodo (framework v3.5, current) | [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168) |
| Zenodo (framework concept DOI, always latest) | [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489) |
| Zenodo (framework v3.4 archive) | [10.5281/zenodo.20070101](https://doi.org/10.5281/zenodo.20070101) |
| Zenodo (framework v3.3 archive) | [10.5281/zenodo.18837071](https://doi.org/10.5281/zenodo.18837071) |
| Zenodo (Paper E, rank-1 branched adiabatic) | [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) |
| Zenodo (Paper A, certified G₂) | [10.5281/zenodo.19892350](https://doi.org/10.5281/zenodo.19892350) |
| Zenodo (Paper B, spectral) | [10.5281/zenodo.19893371](https://doi.org/10.5281/zenodo.19893371) |
| Zenodo (Paper C, K3 NK) | [10.5281/zenodo.19708916](https://doi.org/10.5281/zenodo.19708916) |
| Zenodo (Paper D, Donaldson analytic) | [10.5281/zenodo.20039066](https://doi.org/10.5281/zenodo.20039066) |
| ResearchGate | [Author page](https://www.researchgate.net/profile/Brieuc-De-La-Fourniere) |

---

## Citation

```bibtex
@software{k7_framework,
  title   = {The K₇ Framework (formerly GIFT)},
  author  = {de La Fournière, Brieuc},
  year    = {2026},
  url     = {https://github.com/Arithmon/K7},
  doi     = {10.5281/zenodo.16891489},
  version = {3.5}
}
```

Cite the published version (3.5) until 3.6 is deposited.

See [CITATION.md](CITATION.md) for additional formats.

---

## License

MIT License, see [LICENSE](LICENSE)

---

>
> *Gift from bit*

---

**K₇ (formerly GIFT) is the founding framework of the [Arithmon program](https://github.com/arithmon).**
