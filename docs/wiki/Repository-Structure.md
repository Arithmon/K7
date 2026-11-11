---
title: "Repository Structure"
layout: default
---

# Repository Structure

This repository holds the papers, the dataset and the documentation of the K₇ framework, version 3.6 (formerly GIFT).

## Directory layout

```
K7/
├── publications/
│   ├── papers/
│   │   ├── markdown/                  # Canonical sources
│   │   │   ├── k7_framework_3_6_main.md                 # Main paper (v3.6)
│   │   │   ├── k7_framework_3_6_S1_foundations.md       # S1: E₈, G₂, K₇ background
│   │   │   ├── k7_framework_3_6_S2_derivations.md       # S2: the 33 relations
│   │   │   ├── k7_framework_3_6_S3_observables.md       # S3: the dataset
│   │   │   ├── k7_framework_3_6_S4_sieve_diagnostics.md # S4: look-elsewhere
│   │   │   ├── k7_framework_3_6_CHANGELOG.md            # Changes from v3.5
│   │   │   ├── k7_framework_3_5_*.md                    # v3.5 (read with the erratum)
│   │   │   ├── g2_certified_neck.md                     # Paper A
│   │   │   └── g2_spectral.md                           # Paper B
│   │   ├── tex/                       # LaTeX sources (v3.6, v3.5, A, B)
│   │   ├── pdf/                       # PDFs (v3.6, v3.5, companion papers A to E)
│   │   ├── legacy/                    # v3.3 and v3.4 (archived)
│   │   ├── figures/
│   │   └── notebooks/                 # Companion notebooks (A, B)
│   ├── ERRATUM_v3.5.md                # Erratum to the published v3.5
│   ├── outreach/                      # Blog posts
│   ├── references/                    # Dataset and reference pages
│   │   ├── observables.csv            # The 95-entry dataset
│   │   ├── GIFT_ATLAS.json            # Constants and the 33 relations (generated)
│   │   ├── OBSERVABLE_REFERENCE.md
│   │   ├── STATISTICAL_EVIDENCE.md
│   │   └── Bibliography.md
│   └── validation/
│       ├── v3.6/                      # Look-elsewhere test of v3.6 (code, data, results)
│       └── legacy/                    # Earlier validation scripts (archived)
│
├── docs/                              # Guides and the Jekyll site
│   ├── index.html                     # Landing page (arithmon.github.io/K7)
│   ├── GIFT_FOR_EVERYONE.md           # Plain-language guide
│   ├── FAQ.md
│   ├── GLOSSARY.md
│   ├── INFO_GEO_FOR_PHYSICISTS.md
│   ├── GIFTPY_FOR_GEOMETERS.md
│   ├── LEAN_FOR_PHYSICS.md
│   └── wiki/                          # Wiki pages
│
├── README.md
├── CHANGELOG.md
├── CITATION.md / CITATION.cff
├── STRUCTURE.md                       # This file
└── LICENSE                            # MIT
```

## Quick navigation

| Looking for | Go to |
|-------------|-------|
| Framework overview | `README.md` |
| Plain-language guide | `docs/GIFT_FOR_EVERYONE.md` |
| Main paper (v3.6) | `publications/papers/markdown/k7_framework_3_6_main.md` |
| The 33 relations, one by one | `publications/papers/markdown/k7_framework_3_6_S2_derivations.md` |
| Dataset description | `publications/papers/markdown/k7_framework_3_6_S3_observables.md` |
| Dataset (machine-readable) | `publications/references/observables.csv` |
| Look-elsewhere test (code, preregistration, results) | `publications/validation/v3.6/` |
| Changes from v3.5 | `publications/papers/markdown/k7_framework_3_6_CHANGELOG.md` |
| Erratum to v3.5 | `publications/ERRATUM_v3.5.md` |
| Paper A (certified seam metric) | `publications/papers/pdf/g2_certified_neck.pdf` |
| Paper B (spectral geometry) | `publications/papers/pdf/g2_spectral.pdf` |
| Companion notebooks | `publications/papers/notebooks/` |
| Blog posts and outreach | `publications/outreach/` |
| Earlier versions | `publications/papers/legacy/` |
| Technical definitions | `docs/GLOSSARY.md` |
| How to cite | `CITATION.md` |
| Lean 4 identities | [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) |

## Core documents (v3.6)

| File (`publications/papers/markdown/`) | Title | Pages (PDF) |
|----------------------------------------|-------|-------------|
| `k7_framework_3_6_main.md` | The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology | 41 |
| `k7_framework_3_6_S1_foundations.md` | Supplement S1: Mathematical Foundations | 26 |
| `k7_framework_3_6_S2_derivations.md` | Supplement S2: The 33 Relations | 14 |
| `k7_framework_3_6_S3_observables.md` | Supplement S3: Observable Dataset | 15 |
| `k7_framework_3_6_S4_sieve_diagnostics.md` | Supplement S4: Sieve and Look-Elsewhere Diagnostics | 11 |

## Related repositories

| Repository | Content |
|------------|---------|
| [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) | Lean 4 identities, metric pipeline, giftpy (formerly `gift-framework/core`) |
| [Arithmon/Sieve](https://github.com/Arithmon/Sieve) | The look-elsewhere methodology used in main §7 |

## Version

**Current**: v3.6 (in preparation)

**Relations**: 33, compared with measurement in five classes: 23 within 2σ of measurement, 3 in tension, 5 excluded as exact equalities at more than 3σ and kept as proximities, 1 inside a PDG range, 1 with a non-Gaussian profile (main §4.1; PDG 2026, NuFIT 6.1, Planck 2018). The other 62 entries of the dataset are conditional or diagnostic and are not counted.

**Formal verification**: 156 Lean 4 files, 14 axioms (4 literature imports, 10 interval certificates), no sorry; the arithmetic of the 33 relations is collected in `relations_v36_certified` (commit 34ce857). It establishes the stated arithmetic, not the physical reading.

**Papers**: Framework v3.6 (not yet deposited; concept DOI 10.5281/zenodo.16891489). Published version: v3.5 (Zenodo 10.5281/zenodo.21296168); companion papers A (10.5281/zenodo.18643069), B (10.5281/zenodo.18920367), C (10.5281/zenodo.19708915), D (10.5281/zenodo.20039065), E (10.5281/zenodo.21215956).
