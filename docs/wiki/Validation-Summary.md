---
title: "Validation Summary"
layout: default
---

# Validation Summary: the 33 Relations against Current Data

**Framework version**: 3.6. **Source**: main paper [§4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) and supplement [S3](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S3_observables.md); the tables on this page are copied from the paper by a script.

**Data.** PDG 2026 for particle data, NuFIT 6.1 for neutrino mixing (normal ordering, with atmospheric data), Planck 2018 for cosmology (TT,TE,EE+lowE+lensing, one column), CODATA 2022 for α and m_μ/m_e. All uncertainties are brought to 1σ. Correlations are neglected, except in the Planck density ratios, which are computed on the published chains. The pull is (K₇ − measured)/σ with the experimental uncertainty alone: the framework supplies no theoretical uncertainty.

---

## 1. Five classes, not one score

| Class | Count | Relations |
|-------|-------|-----------|
| within 2σ | 23 | the remaining relations |
| tension (2σ < \|pull\| ≤ 3σ) | 2 | m_τ/m_e (−2.1σ), Ω_c/Ω_m (+2.5σ) |
| proximity (\|pull\| > 3σ) | 6 | α⁻¹, sin²θ_W (−7.5σ), m_μ/m_e, m_μ/m_τ (+20.8σ), m_b/m_t (−10.2σ, in the declared mass scheme), m_W/m_Z (−3.8σ) |
| inside the PDG range (no uncertainty) | 1 | m_s/m_d |
| non-Gaussian profile | 1 | sin²θ₂₃ (§4.3) |

Earlier versions summarised the comparison by a mean deviation. That summary is withdrawn: it hid the relations outside 2σ, and a mean deviation measures closeness, which the [look-elsewhere test](Statistical-Evidence.html) shows is not distinctive.

## 2. The table

| ID | Observable | Formula | K₇ value | Measured | Dev. | Pull | Status |
|---|-------|-------------|------|----------|------|-----|--------|
| A01 | sin²θ_W (M_Z) | b₂/(b₃ + dim G₂) = 3/13 | 0.230769 | 0.23122(6) | −0.19% | −7.5σ | integer; **proximity** |
| A02 | α_s(M_Z) | √2/(dim G₂ − p₂) = √2/12 | 0.117851 | 0.1180(9) | −0.13% | −0.2σ | algebraic |
| A03 | λ_H | √(dim G₂ + N_gen)/det_den = √17/32 | 0.128847 | 0.12914(23) | −0.22% | −1.3σ | algebraic; det(g) |
| A04 | α⁻¹(0) | 128 + 9 + det(g)·κ_T | 137.0333 | 137.035999177(21) | −0.0020% | ≫ 10σ | det(g), κ_T; **proximity** |
| A05 | Q_Koide | dim G₂/b₂ = 2/3 | 0.666667 | 0.6666645(51) | +0.0003% | +0.4σ | integer; approximate (R8) |
| A06 | m_τ/m_e | 7 + 10·248 + 10·99 = 3477 | 3477 | 3477.37(18) | −0.011% | −2.1σ | integer; approximate (R8); **tension** |
| A07 | m_μ/m_e | 27^φ | 207.012 | 206.7682827(46) | +0.12% | ≫ 10σ | φ; approximate (R8); **proximity** |
| A08 | m_s/m_d | p₂² × Weyl = 20 | 20 | 17–22 (range) | n/a | n/a | integer; inside the PDG range |
| A09 | m_c/m_s | (dim E₈ − p₂)/b₂ = 246/21 | 11.714 | 11.769(35) | −0.46% | −1.6σ | integer |
| A10 | m_b/m_t | 1/(2b₂) = 1/42 | 0.023810 | 0.024253(43) | −1.83% | −10.2σ | integer; **proximity** (in the scheme declared in R7) |
| A11 | m_u/m_d | (1 + dim E₆)/\|PSL(2,7)\| = 79/168 | 0.470238 | 0.462(12) | +1.78% | +0.7σ | integer |
| A12 | sin²θ₁₂ (PMNS) | (1 + N_gen)/α_sum = 4/13 | 0.307692 | 0.3088(+67/−66) | −0.36% | −0.2σ | integer |
| A13 | sin²θ₂₃ (PMNS) | (D_bulk − Weyl)/D_bulk = 6/11 | 0.545455 | 0.470(+17/−14) | +16.05% | +4.4σ* | integer; **tension** (octant; inside the NuFIT 3σ range, §4.3) |
| A14 | sin²θ₁₃ (PMNS) | D_bulk/dim(E₈×E₈) = 11/496 | 0.022177 | 0.02248(+55/−59) | −1.35% | −0.5σ | integer |
| A15 | δ_CP | dim K₇ · dim G₂ + H* = 197 | 197 → phase 2π·197/360 | 212 (+26/−36)° | −7.08% | −0.4σ | **unit assignment** (R6) |
| A16 | sin θ₁₂ (CKM) | fund(E₇)/dim E₈ = 56/248 | 0.225806 | 0.22517(68) | +0.28% | +0.9σ | integer; approximate (R12) |
| A17 | A (Wolfenstein) | (Weyl + dim E₆)/H* = 83/99 | 0.838384 | 0.826(+17/−15) | +1.50% | +0.7σ | integer; approximate (R12) |
| A18 | sin θ₂₃ (CKM) | dim K₇/\|PSL(2,7)\| = 7/168 | 0.041667 | 0.04189(+81/−69) | −0.53% | −0.3σ | integer; approximate (R12) |
| A19 | m_H/m_t | fund(E₇)/b₃ = 56/77 | 0.727273 | 0.7250(13) | +0.32% | +1.8σ | integer |
| A20 | m_H/m_W | (N_gen + dim E₆)/dim F₄ = 81/52 | 1.557692 | 1.5571(14) | +0.040% | +0.5σ | integer |
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = 37/42 | 0.880952 | 0.881285(87) | −0.038% | −3.8σ | integer; **proximity** |
| A22 | m_μ/m_τ | (b₂ − D_bulk)/\|PSL(2,7)\| = 10/168 | 0.059524 | 0.0594612(30) | +0.11% | +20.8σ | integer; approximate (R8); **proximity** |
| A23 | Ω_DE | ln 2 · (b₂ + b₃)/H* | 0.686146 | 0.6847(73) | +0.21% | +0.2σ | ln 2; approximate (R11) |
| A24 | n_s | ζ(11)/ζ(5) | 0.964864 | 0.9649(42) | −0.0037% | 0.0σ | ζ values |
| A25 | Ω_DM/Ω_b | (1 + 2b₂)/rank E₈ = 43/8 | 5.375 | 5.364(77) | +0.21% | +0.1σ | integer; approximate (R11) |
| A26 | Ω_c/Ω_Λ | det_num/\|PSL(2,7)\| = 65/168 | 0.386905 | 0.387(14) | +0.10% | 0.0σ | integer; det(g); approximate (R11) |
| A27 | Ω_Λ/Ω_m | (dim G₂ + H*)/dim F₄ = 113/52 | 2.173077 | 2.173(74) | −0.017% | 0.0σ | integer; approximate (R11) |
| A28 | h | (\|PSL(2,7)\| − 1)/dim E₈ = 167/248 | 0.673387 | 0.6736(54) | −0.032% | 0.0σ | integer |
| A29 | Ω_b/Ω_m | Weyl/det_den = 5/32 | 0.15625 | 0.1565(19) | −0.13% | −0.1σ | integer; det(g); approximate (R11) |
| A30 | Ω_c/Ω_m | (det_den − Weyl)/det_den = 27/32 | 0.84375 | 0.8390(19) | +0.56% | +2.5σ | integer; det(g); approximate (R11); **tension** |
| A31 | σ₈ | (p₂ + det_den)/(2b₂) = 34/42 | 0.809524 | 0.8111(60) | −0.19% | −0.3σ | integer; det(g) |
| A32 | Y_p | (1 + dim G₂)/κ_T⁻¹ = 15/61 | 0.245902 | 0.245(3) | +0.37% | +0.3σ | integer; κ_T |
| A33 | Ω_m/Ω_Λ | (1 + dim J₃(𝕆))/κ_T⁻¹ = 28/61 | 0.459016 | 0.461(16) | −0.35% | −0.1σ | integer; κ_T; approximate (R11) |

**Status vocabulary.** *integer*: a ratio of structural integers. *algebraic, φ, ln 2, ζ values*: the formula uses the corresponding additional operation. *det(g)*, *κ_T*: the formula uses the imposed normalization det(g) = 65/32 or the combination κ_T⁻¹ = 61. *tension*: between 2σ and 3σ, or a deviation whose reading is itself ambiguous (θ₂₃). *proximity*: beyond 3σ; the relation is excluded as an exact equality and retained as a numerical proximity. *approximate*: one of several mutually incompatible relations in an overdetermined sector, none of which is selected. *unit assignment*: the prediction depends on a unit chosen by the dictionary. The asterisk on sin²θ₂₃ marks a non-Gaussian profile: the Gaussian pull overstates the tension.

## 3. What the table shows

- **Six proximities are already rejected as exact equalities.** α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ and m_W/m_Z compare with quantities measured to between 10⁻¹⁰ and a few 10⁻⁴ (m_W/m_Z = 37/42 lies 3.8σ from the ratio of the published masses); m_b/m_t lies 1.8% from the ratio in the declared mass scheme and is not rescued by reading it in another scheme.
- **The 33 relations are not 33 independent tests.** Three sectors are overdetermined, and in each the relations disagree with one another as exact equalities: four lepton relations bear on two mass ratios; three CKM relations bear on two Wolfenstein parameters (sin θ₂₃ = Aλ², 2.6% apart); seven density relations bear on two independent densities. A complete audit of the dependencies among the 33 has not been done, so no count of independent quantities is given.
- **Most of the 23 are tested only weakly.** For quark mass ratios, mixing parameters and cosmological ratios the experimental uncertainties are at the percent level, and a percent-level agreement is what a rich vocabulary reaches easily.
- **sin²θ₂₃ = 6/11.** NuFIT 6.1 prefers the first octant; the fit keeps a second-octant branch, and its 3σ range (0.435 to 0.584) contains 6/11. The relation is in tension with the preferred octant.
- **δ_CP.** The structure produces the integer 197. Reading it in degrees is a choice of the dictionary, recorded in the residue register and counted in the look-elsewhere test.
- **Ω_c/Ω_m.** Planck's Ω_m includes neutrinos, so that Ω_b/Ω_m + Ω_c/Ω_m = 0.9955, while 5/32 + 27/32 = 1: the two formulas are not compatible with that definition of total matter.

## 4. With and without the imposed normalization

Six relations use det(g) = 65/32 (λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈) and three use κ_T⁻¹ = 61 (α⁻¹, Y_p, Ω_m/Ω_Λ). Without the six det(g) relations, 27 remain, of which 19 lie within 2σ; without the eight relations that use either, 25 remain, of which 17 lie within 2σ. A reader who regards the imposed normalization as an extra parameter should read the framework through the reduced counts.

## 5. The other 62 entries of the dataset

The dataset contains 62 further entries, which version 3.6 does not count as predictions: 19 dimensionful or composite quantities (Type II), several of them numbers read in a chosen unit and eight of them legacy values whose derivation is not documented; 21 outputs of mechanisms that consume declared calibration choices (Type III); and 22 structural diagnostics with no experimental counterpart (Type IV). They are kept in S3 for traceability. The scale-bridge and dimensional predictions shown on earlier versions of this page belong to these entries.

## 6. Decision rule

The relations are stated as exact equalities with no theoretical uncertainty. A relation is rejected when its reference series excludes its value at 3σ; after rejection it may be kept only as a numerical proximity, with no predictive claim. The rule has no repair clause (main paper, §11).

| # | Quantity | K₇ value | Rejection condition | What is rejected |
|---|----------|----------|---------------------|------------------|
| D1 | the phase e^{iδ_CP}, δ_CP = 2π·197/360 | 197° | a global fit of the reference series, including DUNE or Hyper-Kamiokande, whose 3σ interval excludes 197° | the δ_CP relation and the unit assignment that produced it |
| D2 | sin²θ₂₃ (PMNS) | 6/11 = 0.5455 | a global fit whose 3σ interval excludes 6/11, in either octant | the θ₂₃ relation |
| D3 | m_τ/m_e and Q_Koide | 1776.74 MeV and 1776.97 MeV for m_τ | a value of m_τ whose 3σ interval excludes the value | each excluded relation, separately |
| D4 | N_gen | 3 | a fourth sequential generation | the integer identity, as a consistency check |
| D5 | m_s/m_d | 20 | a lattice determination adopted by the reference series, with an uncertainty whose 3σ interval excludes 20 | the m_s/m_d relation |

Two contradicting measurements outside the reference series are reported beside their class: h = 167/248 agrees with Planck (0.0σ) and is excluded by the SH0ES distance ladder at 5.5σ; the density relations agree with Planck and are strained by the baryon acoustic oscillations of DESI (second data release, arXiv:2503.14738): in flat ΛCDM, DESI alone gives Ω_m = 0.2975 ± 0.0086, which puts Ω_Λ/Ω_m = 113/52 at −1.9σ, Ω_m/Ω_Λ = 28/61 at +2.0σ and Ω_DE at −1.9σ; DESI combined with the cosmic microwave background gives Ω_m = 0.3027 ± 0.0036 and H₀ = 68.17 ± 0.28, which puts them at −3.3σ, +3.4σ and −3.1σ, and h at −3.0σ. While methods keep disagreeing, the status is stated both ways, and neither agreement counts as a confirmation.

Under the same rule, the next sharp test is sin²θ₁₂ = 4/13 = 0.3077: JUNO's first measurement is 0.3092 ± 0.0087 (arXiv:2511.14593), and after six years its uncertainty should be about four times smaller than that of today's global fit.

## 7. What is verified, and what is not

The arithmetic of the 33 relations is machine-checked in Lean 4 (K7-Lean, `relations_v36_certified`): given the declared integers, each closed form evaluates to the stated number. This does not establish the existence of K₇, the physical interpretation of any relation, or the choice of assignments. No compact torsion-free G₂ manifold with Betti numbers (21, 77) is currently constructed.

---

*The K₇ Framework v3.6 | generated from the paper sources by `k7_v3_6_surface_pages.py`*
