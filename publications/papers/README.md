# The K₇ Framework: Publications (v3.5 published, v3.6 in preparation)

[![Lean 4 Verified](https://img.shields.io/badge/Lean_4-Verified-blue)](https://github.com/Arithmon/K7-Lean/tree/main/Lean)

The K₇ Framework (formerly GIFT): Standard Model parameters from G₂ holonomy geometry coupled to E₈×E₈.

---

## Documentation Structure

```
publications/
├── papers/
│   ├── markdown/                    # Canonical sources (v3.5)
│   │   ├── k7_framework_3_5_main.md             # Main paper
│   │   ├── k7_framework_3_5_S1_foundations.md   # E₈, G₂, K₇ foundations
│   │   ├── k7_framework_3_5_S2_derivations.md   # Type I derivations
│   │   ├── k7_framework_3_5_S3_observables.md   # Observable catalog
│   │   ├── k7_framework_3_5_S4_sieve_diagnostics.md # Sieve diagnostics
│   │   ├── g2_certified_neck.md         # Paper A — certified G₂
│   │   └── g2_spectral.md               # Paper B — spectral
│   ├── pdf/                         # Compiled PDFs (all published)
│   │   ├── k7_framework_3_5_main.pdf              # Framework main (Zenodo 21296168)
│   │   ├── k7_framework_3_5_S1_foundations.pdf    # Framework S1  (Zenodo 21296168)
│   │   ├── k7_framework_3_5_S2_derivations.pdf    # Framework S2  (Zenodo 21296168)
│   │   ├── k7_framework_3_5_S3_observables.pdf    # Framework S3  (Zenodo 21296168)
│   │   ├── k7_framework_3_5_S4_sieve_diagnostics.pdf # Framework S4 (Zenodo 21296168)
│   │   ├── g2_certified_neck.pdf        # Paper A (Zenodo 19892350)
│   │   ├── g2_spectral.pdf              # Paper B (Zenodo 19893371)
│   │   ├── K3_NK_Certificate.pdf        # Paper C (Zenodo 19708916)
│   │   ├── donaldson_analytic.pdf       # Paper D (Zenodo 20039066)
│   │   └── rank_one_branched_adiabatic.pdf # Paper E (Zenodo 21215956)
│   ├── tex/                         # LaTeX sources (v3.5)
│   ├── figures/                     # Publication figures
│   ├── notebooks/                   # Companion Jupyter notebooks
│   ├── legacy/v3.3/                 # v3.3 framework PDFs + markdown + tex (archived)
│   └── legacy/v3.4/                 # v3.4 framework PDFs + markdown + tex (archived)
│
├── outreach/                        # Substack mirror (essays archive)
│
├── references/
│   ├── observables.csv              # Machine-readable data
│   ├── OBSERVABLE_REFERENCE.md
│   ├── STATISTICAL_EVIDENCE.md
│   └── Bibliography.md
│
└── validation/
    ├── README.md                    # v3.4 headline + pointer to legacy v3.3
    └── legacy/v3.3/                 # v3.3 validation pipeline (archived)
```

---

## Framework v3.6 (draft, branch `v3.6-draft`)

| Document | Markdown |
|----------|----------|
| Main paper | [k7_framework_3_6_main.md](markdown/k7_framework_3_6_main.md) |
| S1: Mathematical foundations | [k7_framework_3_6_S1_foundations.md](markdown/k7_framework_3_6_S1_foundations.md) |
| S2: The 33 relations | [k7_framework_3_6_S2_derivations.md](markdown/k7_framework_3_6_S2_derivations.md) |
| S3: Observable dataset | [k7_framework_3_6_S3_observables.md](markdown/k7_framework_3_6_S3_observables.md) |
| S4: Look-elsewhere test | [k7_framework_3_6_S4_sieve_diagnostics.md](markdown/k7_framework_3_6_S4_sieve_diagnostics.md) |
| Changes from v3.5 | [k7_framework_3_6_CHANGELOG.md](markdown/k7_framework_3_6_CHANGELOG.md) |

The v3.5 files below are unchanged, and are read together with the [erratum](../ERRATUM_v3.5.md).

---

## Framework v3.5 (PDF + TeX + markdown, published Zenodo [10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168))

| Document | PDF | Markdown |
|----------|-----|----------|
| Main Paper (47 pp.) | [k7_framework_3_5_main.pdf](pdf/k7_framework_3_5_main.pdf) | [k7_framework_3_5_main.md](markdown/k7_framework_3_5_main.md) |
| S1: Foundations | [k7_framework_3_5_S1_foundations.pdf](pdf/k7_framework_3_5_S1_foundations.pdf) | [k7_framework_3_5_S1_foundations.md](markdown/k7_framework_3_5_S1_foundations.md) |
| S2: Derivations | [k7_framework_3_5_S2_derivations.pdf](pdf/k7_framework_3_5_S2_derivations.pdf) | [k7_framework_3_5_S2_derivations.md](markdown/k7_framework_3_5_S2_derivations.md) |
| S3: Observables | [k7_framework_3_5_S3_observables.pdf](pdf/k7_framework_3_5_S3_observables.pdf) | [k7_framework_3_5_S3_observables.md](markdown/k7_framework_3_5_S3_observables.md) |
| S4: Sieve Diagnostics | [k7_framework_3_5_S4_sieve_diagnostics.pdf](pdf/k7_framework_3_5_S4_sieve_diagnostics.pdf) | [k7_framework_3_5_S4_sieve_diagnostics.md](markdown/k7_framework_3_5_S4_sieve_diagnostics.md) |

> LaTeX sources: [`tex/`](tex/). Concept DOI (always latest version): [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489).

## Companion Papers (peer-reviewable, Zenodo)

| Paper | Description | DOI |
|-------|-------------|-----|
| [A — Certified G₂ Structure](pdf/g2_certified_neck.pdf) | First computer-assisted existence proof for a metric with special holonomy | [10.5281/zenodo.19892350](https://doi.org/10.5281/zenodo.19892350) |
| [B — Spectral Geometry](pdf/g2_spectral.pdf) | Laplacian spectrum, harmonic forms, λ₁ ≈ 6π²/475 | [10.5281/zenodo.19893371](https://doi.org/10.5281/zenodo.19893371) |
| [C — K3 Newton-Kantorovich](pdf/K3_NK_Certificate.pdf) | NK diagnostics on Donaldson K3 (CI(2,2,2)) | [10.5281/zenodo.19708916](https://doi.org/10.5281/zenodo.19708916) |
| [D — Donaldson Analytic Note](pdf/donaldson_analytic.pdf) | Closed-form G₂ ansatz on K3-coassociative neck, 5-layer Wirtinger cert | [10.5281/zenodo.20039066](https://doi.org/10.5281/zenodo.20039066) |
| [E — Rank-1 Branched Adiabatic](pdf/rank_one_branched_adiabatic.pdf) | Neck-level analytic machinery closed at D₀ (open: (J) + H_global) | [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) |

---

## Headline results and statistical validation of version 3.5 (withdrawn in 3.6)

The tables that stood here in version 3.5 gave the relations the status **PROVEN** and reported "0 better alternatives" among 3,000,000+ configurations and a set-level probability of about 10⁻⁶. Version 3.6 withdraws them: the relations are assignments whose arithmetic is verified, not derivations; the alternatives were scored with the framework's own formulas; and in a preregistered test where each competitor searches for its own formulas, a quarter of the alternative Betti pairs and half of the invented vocabularies reach as many targets as K₇ (S4). See the [v3.6 changelog](markdown/k7_framework_3_6_CHANGELOG.md).

---

## Formal Verification

146 Lean 4 files, 213 conjuncts certified, 14 axioms at K7-Lean main (4 prediction-chain + 10 K3 interval certificates), 0 sorry, 8394 build jobs.

See [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) for proofs (v3.5).

---

## Legacy

- `legacy/v3.3/` — v3.3 framework PDFs, markdown and tex (archived 2026-05-02)
- `legacy/v3.4/` — v3.4 framework PDFs, markdown and tex (archived 2026-07-14, Zenodo [10.5281/zenodo.20070101](https://doi.org/10.5281/zenodo.20070101))
- `../validation/legacy/v3.3/` — v3.3 validation pipeline + Pareto formula selection

---

**Version**: 3.5 (2026-07-10)
**Repository**: https://github.com/Arithmon/K7
