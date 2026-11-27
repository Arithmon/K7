# The K₇ Framework: Publications

[![Lean 4 Verified](https://img.shields.io/badge/Lean_4-Verified-blue)](https://github.com/Arithmon/K7-Lean)

The K₇ Framework (formerly GIFT): a declared correspondence between the invariants of a posited G₂-holonomy geometry, together with E₈×E₈, and dimensionless Standard-Model and cosmological parameters.

Version 3.6 is the current version (Zenodo [10.5281/zenodo.24584099](https://doi.org/10.5281/zenodo.24584099), 2026-11-27).

---

## Documentation Structure

```
publications/
├── papers/
│   ├── markdown/                    # Canonical sources
│   │   ├── k7_framework_3_6_main.md                 # Main paper (v3.6)
│   │   ├── k7_framework_3_6_S1_foundations.md       # E₈, G₂, K₇ foundations
│   │   ├── k7_framework_3_6_S2_derivations.md       # The 33 relations
│   │   ├── k7_framework_3_6_S3_observables.md       # Observable dataset
│   │   ├── k7_framework_3_6_S4_sieve_diagnostics.md # Look-elsewhere test
│   │   ├── k7_framework_3_6_CHANGELOG.md            # Changes from v3.5
│   │   ├── g2_certified_neck.md                     # Paper A
│   │   └── g2_spectral.md                           # Paper B
│   ├── pdf/                         # Compiled PDFs
│   │   ├── k7_framework_3_6_*.pdf                   # Framework v3.6 (main, S1 to S4)
│   │   ├── g2_certified_neck.pdf                    # Paper A
│   │   ├── g2_spectral.pdf                          # Paper B
│   │   ├── K3_NK_Certificate.pdf                    # Paper C
│   │   ├── donaldson_analytic.pdf                   # Paper D
│   │   ├── rank_one_branched_adiabatic.pdf          # Paper E
│   │   └── k7_one_page.pdf                          # One-page summary
│   ├── tex/                         # LaTeX sources (v3.6, companions)
│   ├── figures/                     # Publication figures
│   ├── notebooks/                   # Companion Jupyter notebooks (papers A and B)
│   ├── legacy/v3.3/                 # v3.3 framework PDFs + markdown + tex (archived)
│   ├── legacy/v3.4/                 # v3.4 framework PDFs + markdown + tex (archived)
│   └── legacy/v3.5/                 # v3.5 framework PDFs + markdown + tex (archived)
│
├── outreach/                        # Essay sources and the one-page summary
│
├── references/
│   ├── observables.csv              # Machine-readable data
│   ├── GIFT_ATLAS.json
│   ├── OBSERVABLE_REFERENCE.md
│   ├── STATISTICAL_EVIDENCE.md
│   └── Bibliography.md
│
├── validation/
│   ├── v3.6/                        # Look-elsewhere test of v3.6 (code, data, results)
│   ├── v3.6_generators/             # Generators of the tables and of the generated pages
│   └── legacy/v3.3/                 # v3.3 validation pipeline (archived)
│
└── ERRATUM_v3.5.md                  # Erratum to version 3.5
```

---

## Framework v3.6 (published Zenodo [10.5281/zenodo.24584099](https://doi.org/10.5281/zenodo.24584099))

| Document | PDF | Markdown |
|----------|-----|----------|
| Main paper | [k7_framework_3_6_main.pdf](pdf/k7_framework_3_6_main.pdf) (39 pp.) | [k7_framework_3_6_main.md](markdown/k7_framework_3_6_main.md) |
| S1: Mathematical foundations | [k7_framework_3_6_S1_foundations.pdf](pdf/k7_framework_3_6_S1_foundations.pdf) (26 pp.) | [k7_framework_3_6_S1_foundations.md](markdown/k7_framework_3_6_S1_foundations.md) |
| S2: The 33 relations | [k7_framework_3_6_S2_derivations.pdf](pdf/k7_framework_3_6_S2_derivations.pdf) (15 pp.) | [k7_framework_3_6_S2_derivations.md](markdown/k7_framework_3_6_S2_derivations.md) |
| S3: Observable dataset | [k7_framework_3_6_S3_observables.pdf](pdf/k7_framework_3_6_S3_observables.pdf) (17 pp.) | [k7_framework_3_6_S3_observables.md](markdown/k7_framework_3_6_S3_observables.md) |
| S4: Look-elsewhere test | [k7_framework_3_6_S4_sieve_diagnostics.pdf](pdf/k7_framework_3_6_S4_sieve_diagnostics.pdf) (11 pp.) | [k7_framework_3_6_S4_sieve_diagnostics.md](markdown/k7_framework_3_6_S4_sieve_diagnostics.md) |
| Changes from v3.5 | | [k7_framework_3_6_CHANGELOG.md](markdown/k7_framework_3_6_CHANGELOG.md) |

LaTeX sources: [`tex/`](tex/) (`k7_framework_3_6_*.tex`, `gift_3.6_bib.tex`). Concept DOI (always the latest version): [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489).

---

## Framework v3.5 (previous version, Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168))

The v3.5 files are archived unchanged in [`legacy/v3.5/`](legacy/v3.5/), and are read together with the [erratum](../ERRATUM_v3.5.md). Version 3.6 withdraws a number of their statements ([changes from v3.5](markdown/k7_framework_3_6_CHANGELOG.md)).

| Document | PDF | Markdown |
|----------|-----|----------|
| Main Paper (47 pp.) | [k7_framework_3_5_main.pdf](legacy/v3.5/pdf/k7_framework_3_5_main.pdf) | [k7_framework_3_5_main.md](legacy/v3.5/markdown/k7_framework_3_5_main.md) |
| S1: Foundations | [k7_framework_3_5_S1_foundations.pdf](legacy/v3.5/pdf/k7_framework_3_5_S1_foundations.pdf) | [k7_framework_3_5_S1_foundations.md](legacy/v3.5/markdown/k7_framework_3_5_S1_foundations.md) |
| S2: Derivations | [k7_framework_3_5_S2_derivations.pdf](legacy/v3.5/pdf/k7_framework_3_5_S2_derivations.pdf) | [k7_framework_3_5_S2_derivations.md](legacy/v3.5/markdown/k7_framework_3_5_S2_derivations.md) |
| S3: Observables | [k7_framework_3_5_S3_observables.pdf](legacy/v3.5/pdf/k7_framework_3_5_S3_observables.pdf) | [k7_framework_3_5_S3_observables.md](legacy/v3.5/markdown/k7_framework_3_5_S3_observables.md) |
| S4: Sieve Diagnostics | [k7_framework_3_5_S4_sieve_diagnostics.pdf](legacy/v3.5/pdf/k7_framework_3_5_S4_sieve_diagnostics.pdf) | [k7_framework_3_5_S4_sieve_diagnostics.md](legacy/v3.5/markdown/k7_framework_3_5_S4_sieve_diagnostics.md) |

## Companion Papers (Zenodo)

Cited by their concept DOI, as in the paper's reference list.

| Paper | Description | DOI |
|-------|-------------|-----|
| [A: Certified G₂ Structure](pdf/g2_certified_neck.pdf) | Newton–Kantorovich certificate for a torsion-free G₂ structure near an explicit metric on a neck model; a local result, which does not construct a compact K₇ | [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069) |
| [B: Spectral Geometry](pdf/g2_spectral.pdf) | Numerical Laplacian spectrum and harmonic forms of the explicit metric of paper A | [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) |
| [C: K3 Newton-Kantorovich](pdf/K3_NK_Certificate.pdf) | NK diagnostics on Donaldson K3 (CI(2,2,2)) | [10.5281/zenodo.19708915](https://doi.org/10.5281/zenodo.19708915) |
| [D: Donaldson Analytic Note](pdf/donaldson_analytic.pdf) | Closed-form G₂ ansatz on K3-coassociative neck, 5-layer Wirtinger cert | [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065) |
| [E: Rank-1 Branched Adiabatic](pdf/rank_one_branched_adiabatic.pdf) | Conditional analytic framework for rank-one branched adiabatic limits, computed at a datum D₀ that is not realisable as posed (erratum to v3.5); its global hypotheses are open | [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) |

---

## Headline results and statistical validation of version 3.5 (withdrawn in 3.6)

The tables that stood here in version 3.5 gave the relations the status **PROVEN** and reported "0 better alternatives" among 3,000,000+ configurations and a set-level probability of about 10⁻⁶. Version 3.6 withdraws them: the relations are assignments whose arithmetic is verified, not derivations; the alternatives were scored with the framework's own formulas; and in a preregistered test where each competitor searches for its own formulas, a quarter of the alternative Betti pairs and half of the invented vocabularies reach as many targets as K₇ (S4). See the [v3.6 changelog](markdown/k7_framework_3_6_CHANGELOG.md).

---

## Formal Verification

156 Lean 4 files, 14 axioms at K7-Lean main (4 imported from the literature, 10 interval certificates), 0 sorry; the arithmetic of the 33 relations is collected in `relations_v36_certified`.

See [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) for the proofs.

---

## Legacy

- `legacy/v3.3/`: v3.3 framework PDFs, markdown and tex (archived 2026-05-02, Zenodo [10.5281/zenodo.18837071](https://doi.org/10.5281/zenodo.18837071))
- `legacy/v3.4/`: v3.4 framework PDFs, markdown and tex (archived 2026-07-14, Zenodo [10.5281/zenodo.20070101](https://doi.org/10.5281/zenodo.20070101))
- `legacy/v3.5/`: v3.5 framework PDFs, markdown and tex (archived 2026-11-27, Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168))
- `../validation/legacy/v3.3/`: v3.3 validation pipeline + Pareto formula selection

---

**Version**: 3.6 (2026-11-27)
**Repository**: https://github.com/Arithmon/K7
