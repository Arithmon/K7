---
title: "Citation Guide"
layout: default
---

# Citation Guide

Citation formats for the K₇ framework, version 3.6 (formerly GIFT).

**Version 3.6 is not deposited yet.** Until it is, the published version is 3.5 (Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168)), read together with its [erratum](https://github.com/Arithmon/K7/blob/main/publications/ERRATUM_v3.5.md). The entries below cite the concept DOI [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489), which always resolves to the latest deposited version; the version DOI of 3.6 will be added at the deposit.

## Framework (recommended)

### BibTeX

```bibtex
@software{k7_framework,
  title   = {The K₇ Framework (formerly GIFT)},
  author  = {de La Fournière, Brieuc},
  year    = {2026},
  url     = {https://github.com/Arithmon/K7},
  doi     = {10.5281/zenodo.16891489},
  version = {3.6},
  license = {MIT},
  note    = {A declared correspondence between invariants of a G₂-holonomy seven-manifold and 33 dimensionless parameters: 23 within 2σ of measurement, 2 in tension, 6 excluded as exact equalities at more than 3σ and kept as proximities, 1 inside a PDG range, 1 with a non-Gaussian profile (PDG 2026, NuFIT 6.1, Planck 2018). 156 Lean 4 files, 14 axioms (4 literature imports, 10 interval certificates), no sorry; the arithmetic of the 33 relations is collected in relations\_v36\_certified (commit 34ce857).}
}
```

### APA

```
de La Fournière, B. (2026). The K₇ Framework (formerly GIFT) (Version 3.6) [Software]. Zenodo. https://doi.org/10.5281/zenodo.16891489
```

### Chicago

```
de La Fournière, Brieuc. "The K₇ Framework (formerly GIFT)." Version 3.6. Zenodo, 2026. https://doi.org/10.5281/zenodo.16891489.
```

---

## Framework v3.6 papers

### Main paper

```bibtex
@misc{k7_main_v36,
  title        = {The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology},
  author       = {de La Fournière, Brieuc},
  year         = {2026},
  month        = {November},
  howpublished = {The K₇ Framework v3.6, 39 pp.},
  doi          = {10.5281/zenodo.16891489},
  url          = {https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_main.pdf}
}
```

### S1

```bibtex
@misc{k7_s1_v36,
  title        = {Supplement S1: Mathematical Foundations. E₈ Exceptional Lie Algebra, G₂ Holonomy Manifolds, and K₇ Construction},
  author       = {de La Fournière, Brieuc},
  year         = {2026},
  month        = {November},
  howpublished = {The K₇ Framework v3.6, Supplement S1, 25 pp.},
  doi          = {10.5281/zenodo.16891489},
  url          = {https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_S1_foundations.pdf}
}
```

### S2

```bibtex
@misc{k7_s2_v36,
  title        = {Supplement S2: The 33 Relations. Arithmetic, Dictionary Choices and Status},
  author       = {de La Fournière, Brieuc},
  year         = {2026},
  month        = {November},
  howpublished = {The K₇ Framework v3.6, Supplement S2, 15 pp.},
  doi          = {10.5281/zenodo.16891489},
  url          = {https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_S2_derivations.pdf}
}
```

### S3

```bibtex
@misc{k7_s3_v36,
  title        = {Supplement S3: Observable Dataset. 33 Relations Compared with Measurement; 62 Conditional and Diagnostic Entries},
  author       = {de La Fournière, Brieuc},
  year         = {2026},
  month        = {November},
  howpublished = {The K₇ Framework v3.6, Supplement S3, 17 pp.},
  doi          = {10.5281/zenodo.16891489},
  url          = {https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_S3_observables.pdf}
}
```

### S4

```bibtex
@misc{k7_s4_v36,
  title        = {Supplement S4: Sieve and Look-Elsewhere Diagnostics},
  author       = {de La Fournière, Brieuc},
  year         = {2026},
  month        = {November},
  howpublished = {The K₇ Framework v3.6, Supplement S4, 11 pp.},
  doi          = {10.5281/zenodo.16891489},
  url          = {https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_S4_sieve_diagnostics.pdf}
}
```

> Earlier versions: v3.5 (Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168), with its [erratum](https://github.com/Arithmon/K7/blob/main/publications/ERRATUM_v3.5.md)); v3.4 (Zenodo [10.5281/zenodo.20070101](https://doi.org/10.5281/zenodo.20070101), files in [`publications/papers/legacy/v3.4/`](https://github.com/Arithmon/K7/tree/main/publications/papers/legacy/v3.4/)); v3.3 (Zenodo [10.5281/zenodo.18837071](https://doi.org/10.5281/zenodo.18837071), files in [`publications/papers/legacy/v3.3/`](https://github.com/Arithmon/K7/tree/main/publications/papers/legacy/v3.3/)). Version 3.6 withdraws a number of statements of these versions; see the [changes from v3.5](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_CHANGELOG.md).

---

## Companion papers (Zenodo)

Cited by their concept DOI, as in the paper's reference list.

### [A]

```bibtex
@misc{k7_paper_a_certified_neck,
  title  = {A Certified Torsion-Free G₂ Structure on a TCS Neck Model via Computer-Assisted Proof},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  doi    = {10.5281/zenodo.18643069},
  url    = {https://doi.org/10.5281/zenodo.18643069},
  note   = {Newton--Kantorovich certificate for a nearby torsion-free metric on a seam region; it does not construct a compact K₇}
}
```

### [B]

```bibtex
@misc{k7_paper_b_spectral,
  title  = {Spectral Geometry of an Explicit G₂ Metric: Laplacian Spectrum and Harmonic Forms},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  doi    = {10.5281/zenodo.18920367},
  url    = {https://doi.org/10.5281/zenodo.18920367},
  note   = {Laplacian spectrum and harmonic forms of the approximate seam metric}
}
```

### [C]

```bibtex
@misc{k7_paper_c_k3_nk,
  title  = {Newton--Kantorovich diagnostics on a Donaldson K3 metric: two β estimates, machine-checked inequalities},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  doi    = {10.5281/zenodo.19708915},
  url    = {https://doi.org/10.5281/zenodo.19708915},
  note   = {NK diagnostics on a Donaldson-balanced metric on the K3 surface CI(2,2,2)}
}
```

### [D]

```bibtex
@misc{k7_paper_d_donaldson,
  title  = {An Explicit Closed-Form G₂ Ansatz on a K3-Coassociative Neck with Hyperkähler Rotation and Picard-Lefschetz Wirtinger Certificate},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  doi    = {10.5281/zenodo.20039065},
  url    = {https://doi.org/10.5281/zenodo.20039065},
  note   = {Neck-level certificate; not a compact K₇ torsion-free theorem}
}
```

### [E]

```bibtex
@misc{k7_paper_e_rank_one_branched,
  title  = {A conditional analytic framework for rank-one branched Kovalev--Lefschetz adiabatic limits},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  doi    = {10.5281/zenodo.21215956},
  url    = {https://doi.org/10.5281/zenodo.21215956},
  note   = {Conditional analytic framework; the datum-level instantiation at D₀ is not realisable as posed (v3.5 erratum, sections 2 and 7.4)}
}
```

### [M]

```bibtex
@misc{sieve_methodology,
  title  = {A reproducible standard for arithmetic coincidence claims in fundamental physics},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  doi    = {10.5281/zenodo.20728964},
  url    = {https://doi.org/10.5281/zenodo.20728964},
  note   = {The Sieve methodology and its four-null scorecard for the K₇ relations}
}
```

---

## Formal verification (K7-Lean)

```bibtex
@software{k7_lean,
  title  = {K7-Lean (formerly GIFT Core): Formal Verification in Lean 4},
  author = {de La Fournière, Brieuc},
  year   = {2026},
  url    = {https://github.com/Arithmon/K7-Lean},
  note   = {156 Lean 4 files, 14 axioms (4 literature imports, 10 interval certificates), no sorry; the arithmetic of the 33 relations is collected in relations\_v36\_certified (commit 34ce857). Formalization establishes the stated arithmetic, not the physical reading.}
}
```

---

## DOI

| Record | DOI |
|--------|-----|
| Framework, concept DOI (always the latest version) | [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489) |
| Framework v3.5 (published version) | [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168) |
| Framework v3.4 | [10.5281/zenodo.20070101](https://doi.org/10.5281/zenodo.20070101) |
| Framework v3.3 | [10.5281/zenodo.18837071](https://doi.org/10.5281/zenodo.18837071) |
| [A] A Certified Torsion-Free G₂ Structure on a TCS Neck Model via Computer-Assisted Proof | [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069) |
| [B] Spectral Geometry of an Explicit G₂ Metric | [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) |
| [C] Newton–Kantorovich diagnostics on a Donaldson K3 metric | [10.5281/zenodo.19708915](https://doi.org/10.5281/zenodo.19708915) |
| [D] An Explicit Closed-Form G₂ Ansatz on a K3-Coassociative Neck with Hyperkähler Rotation and Picard-Lefschetz Wirtinger Certificate | [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065) |
| [E] A conditional analytic framework for rank-one branched Kovalev–Lefschetz adiabatic limits | [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) |
| [M] A reproducible standard for arithmetic coincidence claims in fundamental physics | [10.5281/zenodo.20728964](https://doi.org/10.5281/zenodo.20728964) |

---

## Version history

Statements withdrawn by version 3.6 are not repeated in this table; the full record is in the [changelog](https://github.com/Arithmon/K7/blob/main/CHANGELOG.md).

| Version | Date | What changed |
|---------|------|--------------|
| 3.6 | 2026-11 | New title; the framework is stated as a declared correspondence with its dictionary, residue register and decision rule; 33 relations compared with the most recent data in five classes; preregistered look-elsewhere test; several statistical and derivational claims of earlier versions withdrawn |
| 3.5 | 2026-07-10 | Renamed "The K₇ Framework"; S4 supplement added; erratum of 2026-08 to 2026-10 |
| 3.4 | 2026-05-07 | Companion papers A to D published; Lean axiom reduction; K3 certificates |
| 3.3 | 2026-01-12 to 2026-03-02 | 33 relations; neutrino formulas revised; Lean 4 as sole proof system |
| 3.0 to 3.1 | 2025-12 | First Lean-certified relations; first explicit approximate G₂ metric |
| 2.x | 2025-10 to 2025-11 | Framework reorganization |

---

## Usage in publications

1. Cite the framework by the software entry above (concept DOI).
2. Cite a specific statement by the paper or supplement that makes it, with the version number.
3. Quote a relation with its status in the paper's table (main §4.1), not as a prediction of a derivation: the paper states a correspondence and a decision rule (main §11).

### Example

> "The K₇ dictionary [1] assigns the leptonic CP phase the value 2π · 197/360, that is 197°, by a declared unit assignment; its decision rule rejects the relation if a global fit of the reference series excludes 197° at 3σ."
>
> [1] B. de La Fournière, "The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology," The K₇ Framework v3.6 (2026), https://doi.org/10.5281/zenodo.16891489

---

## License

MIT License: see [LICENSE](https://github.com/Arithmon/K7/blob/main/LICENSE)

---

**Version**: 3.6 (not yet deposited)
