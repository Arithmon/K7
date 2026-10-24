# Supplement S3: Observable Dataset

## S3.1 Introduction

This supplement documents the framework's observable dataset (`canonical/data/observables.json`, 95 entries) and the comparison data behind the main text. The dataset is a ledger, not a list of predictions. Version 3.6 counts **33 relations** (Type I) as the framework's claims, compared with measurement in main §4. The other **62 entries** (Types II–IV) are conditional extractions, outputs of mechanisms that consume calibration choices, or diagnostics of the approximate seam metric; they are kept here for traceability and are not counted (main §4.5).

Earlier versions described the dataset as "95 observables derived from a single G₂ metric, zero freely adjustable parameters". That description is withdrawn. The 33 relations are closed forms in twenty declared constants, assigned to observables by the author (main §3); no geometric map sends the invariants to the observables, and the metric does not produce them. The entries below carry a status that says which of these they are.

---

## S3.2 Type classification

| Type | Count | What it is | Counted in main §4 |
|------|-------|-----------|--------------------|
| I | 33 | Dimensionless closed forms in the structural constants, assigned to measured parameters | yes |
| II | 19 | Dimensionful numbers read in a chosen unit (R10), scale bridges, and cascades of Type I relations | no |
| III | 21 | Outputs of mechanisms on the approximate seam metric (Wilson-line splitting, associative volumes, spectral counts, bundle conditioning), with calibration choices; and the withdrawn supersymmetric running | no |
| IV | 22 | Structural quantities and numerical diagnostics, with no experimental counterpart | no |

**Type I.** Each relation is a ratio of structural integers or uses one further operation (√, φ, ln 2, ζ values), declared in its status. The status vocabulary is that of main §4.1: *integer*, *algebraic / φ / ln 2 / ζ values*, *det(g)* (R2), *κ_T* (R3), *proximity*, *tension*, *approximate* (R8, R11, R12), *inside the PDG range*, *unit assignment* (R6); m_b/m_t is compared in the mass scheme declared in R7.

**Type II.** Several entries are numbers read in MeV or GeV, for example m_u = √(dim G₂/3) = 2.16, m_d = ln 107 = 4.673, m_c = (dim G₂ − π)³ = 1280, m_t = 415². Reading a structural number in a unit is an assignment of the same kind as reading 197 in degrees, with a far larger space of alternatives (R10). The CKM magnitudes and the mass cascades (m_c/m_d, m_b/m_d, m_t/m_c) are products of Type I relations and add no information beyond them. Earlier versions described all nineteen as "a Type I ratio times an experimental anchor"; that description did not match the dataset and is withdrawn.

**Type III.** The Wilson-line and associative-volume entries reproduce lepton mass ratios at the percent level with declared calibration choices (a coupling c = 0.452, an exponent α = e^K = 0.002763, a cycle assignment) selected against the measured ratios; they are conditional reconstructions (main §6.2). The four entries of the two-loop supersymmetric running from a grand-unification boundary (C04–C07) are withdrawn with that reading (main §5). The remaining entries are diagnostics, some compared with a mathematical expectation (the Weyl exponent with d/2, the gauge-kinetic conditioning with 1), none with a measurement.

**Type IV.** Topological inputs (b₂, b₃: R1), integer combinations (H*, N_gen), the imposed normalization det(g) = 65/32 (R2), numerical diagnostics of the certified seam metric (Newton–Kantorovich quantities, Gram conditioning, spectral counts, metric block eigenvalues), and three entries taken from the black-hole-remnant analysis of main ref. [42], one of which depends on the scale identification τ₀ = v_EW.

---

## S3.3 Experimental data and conventions

The comparison data were refreshed on 2026-10-22 to the most recent releases (`canonical/scripts/k7_v3_6_exp_refresh.py`, log `canonical/results/k7_v3_6_exp_refresh.json`):

| Source | Used for | Convention |
|--------|----------|-----------|
| PDG 2026 [1] | particle masses, sin²θ_W and α_s at M_Z, CKM parameters, quark mass ratios | MS-bar at the PDG reference scales; m_t from direct measurements |
| NuFIT 6.1 [27] | neutrino mixing | normal ordering, with the tabulated Super-Kamiokande and IceCube atmospheric data; one variant for all four entries |
| Planck 2018 [3] | cosmology | base ΛCDM, TT,TE,EE+lowE+lensing; one column for all entries |
| CODATA 2022 [50] | α at q² = 0, m_μ/m_e | n/a |

**Derived reference values.** Mass ratios are computed from the published masses, density ratios from the published densities, with error propagation that neglects correlations. This is an approximation, not a bound: the summary tables do not publish the covariances, and for a ratio R = x/y the term −2 Cov(x, y)/(xy) in Var(R)/R² can have either sign. Ω_Λ/Ω_m and Ω_m/Ω_Λ use flatness (Ω_Λ = 1 − Ω_m), neglecting the neutrino density (Ω_ν h² ≈ 0.0006 in the Planck base model; Planck's Ω_m includes it). λ_H is the tree-level m_H²/(2v²) with v = (√2 G_F)^(−1/2), a definition that is itself a scheme choice. m_s/m_d is given by the PDG as the range 17–22, without an uncertainty; it is stored as a range, and no pull is defined (the relation's value 20 lies inside it).

**Confidence levels.** All uncertainties are brought to 1σ. The PDG summary tables quote the light-quark masses, m_c, m_b and m_u/m_d at 90% confidence; these are divided by 1.645. The lattice average of m_c/m_s (PDG quark-mass review, statistical and systematic errors in quadrature) is already a 1σ value.

**Asymmetric uncertainties.** NuFIT and the CKM parameter A have asymmetric errors; both sides are kept in the dataset, and the pull uses the side facing the framework's value. The sin²θ₂₃ profile is not Gaussian: its 3σ range (0.435–0.582) contains 6/11 although the Gaussian pull exceeds 4σ (main §4.3).

**Corrections made in the refresh.** The previous dataset gave m_μ/m_τ and m_τ/m_e with uncertainties larger than the PDG errors propagate (by factors 13 and 1.3); computed Q_Koide from the PDG 2022 τ mass while m_τ/m_e used the later one; gave m_b/m_t an uncertainty with no source; quoted an h that matched no Planck column; mixed NuFIT variants with and without atmospheric data; gave m_μ/m_e an uncertainty of 0.02 where CODATA 2022 gives 4.6 × 10⁻⁶; and labelled the CKM entries A16 and A18 sin²θ although their values are sin θ₁₂ = λ and sin θ₂₃ = Aλ². With the corrected data and one convention for all uncertainties, the 33 relations fall into the five classes of main §4.2: 24 within 2σ, 2 in tension, 5 proximities beyond 3σ (m_b/m_t in the scheme of R7 among them), 1 inside the PDG range, 1 with a non-Gaussian profile. (The earlier count, 28 within 2σ, rested on the uncertainties listed above.)

**Not refreshed.** Y_p (0.245 ± 0.003) is the PDG's recommended observational helium abundance from HII regions (BBN review of the 2024 Review of Particle Physics, eq. 24.3; earlier versions of the dataset labelled it Planck 2018, which it is not), and was not re-checked against the 2026 edition; the Type II CKM magnitudes and mass cascades keep their earlier reference values, since they are not compared in the main text.

---

## S3.4 Structural constants

The twenty constants, their origin and their status are given in main §3.1. Two corrections to earlier versions of this supplement: N_gen = 3 is an integer identity (b₂/dim K₇), not the output of an index theorem (main §2.4); and b₂, b₃ are inputs posited by the framework (R1), not quantities confirmed by the spectral analysis of [B], which concerns an approximate metric.

---

## S3.5 The 33 relations: reference data

Formulas, framework values and deviations are in main §4.1. This table gives, for each relation, the reference value, its source and the convention under which it is compared. It is generated from the dataset (`canonical/scripts/k7_v3_6_s3_tables.py`); the status column is read from main §4.1.

<!-- BEGIN S3-TYPE-I -->
| ID | Observable | Measured | Source | Pull | Convention / note | Status |
|----|-----------|----------|--------|------|-------------------|--------|
| A01 | sin²θ_W (M_Z) | 0.23122(6) | PDG 2026 | −7.5σ | MS-bar at M_Z (PDG Table 1.1) | integer; **proximity** |
| A02 | α_s(M_Z) | 0.1180(9) | PDG 2026 | −0.2σ | n/a | algebraic |
| A03 | λ_H | 0.12914(23) | PDG 2026 | −1.3σ | tree level m_H²/(2v²), v = (√2 G_F)^(−1/2) = 246.220 GeV | algebraic; det(g) |
| A04 | α⁻¹(0) | 137.035999177(21) | CODATA 2022 | ≫ 10σ | α⁻¹ at q² = 0 | det(g), κ_T; **proximity** |
| A05 | Q_Koide | 0.6666645(51) | PDG 2026 | +0.4σ | computed from the PDG 2026 masses | integer; approximate (R8) |
| A06 | m_τ/m_e | 3477.37(18) | PDG 2026 | −2.1σ | from the PDG 2026 masses | integer; approximate (R8); **tension** |
| A07 | m_μ/m_e | 206.7682827(46) | CODATA 2022 | ≫ 10σ | n/a | φ; approximate (R8); **proximity** |
| A08 | m_s/m_d | 17–22 (range) | PDG 2026 | n/a | PDG gives the range 17–22, not a measurement with an uncertainty | integer; inside the PDG range |
| A09 | m_c/m_s | 11.769(35) | PDG 2026 | −1.6σ | lattice average (N_f = 2+1+1), PDG quark-mass review | integer |
| A10 | m_b/m_t | 0.024253(43) | PDG 2026 | −10.2σ | m_b at 90% CL converted to 1σ | integer; **proximity** (in the scheme declared in R7) |
| A11 | m_u/m_d | 0.462(12) | PDG 2026 | +0.7σ | MS-bar at 2 GeV | integer |
| A12 | sin²θ₁₂ (PMNS) | 0.3088(+67/−66) | NuFIT 6.1 (IC24+SK-atm, NO) | −0.2σ | n/a | integer |
| A13 | sin²θ₂₃ (PMNS) | 0.470(+17/−14) | NuFIT 6.1 (IC24+SK-atm, NO) | +4.4σ* | 3σ range 41.27°–49.86°, i.e. sin² 0.435–0.582, contains 6/11 | integer; **tension** (octant; inside the NuFIT 3σ range, §4.3) |
| A14 | sin²θ₁₃ (PMNS) | 0.02248(+55/−59) | NuFIT 6.1 (IC24+SK-atm, NO) | −0.5σ | n/a | integer |
| A15 | δ_CP | 212 (+26/−36)° | NuFIT 6.1 (IC24+SK-atm, NO) | −0.4σ | degrees | **unit assignment** (R6) |
| A16 | sin θ₁₂ (CKM) | 0.22517(68) | PDG 2026 | +0.9σ | PDG CKM review: sin θ₁₂ = λ (not squared) | integer; approximate (R12) |
| A17 | A (Wolfenstein) | 0.826(+17/−15) | PDG 2026 | +0.7σ | PDG CKM review, Wolfenstein fit | integer; approximate (R12) |
| A18 | sin θ₂₃ (CKM) | 0.04189(+81/−69) | PDG 2026 | −0.3σ | PDG CKM review: sin θ₂₃ = Aλ² (not squared) | integer; approximate (R12) |
| A19 | m_H/m_t | 0.7250(13) | PDG 2026 | +1.8σ | m_t from direct measurements | integer |
| A20 | m_H/m_W | 1.5571(14) | PDG 2026 | +0.5σ | n/a | integer |
| A21 | m_W/m_Z | 0.88136(15) | PDG 2026 | −2.7σ | W/Z mass ratio of the PDG summary table | integer; **tension** |
| A22 | m_μ/m_τ | 0.0594612(30) | PDG 2026 | +20.8σ | from the PDG 2026 masses | integer; approximate (R8); **proximity** |
| A23 | Ω_DE | 0.6847(73) | Planck 2018 (TT,TE,EE+lowE+lensing) | +0.2σ | Ω_Λ | ln 2; approximate (R11) |
| A24 | n_s | 0.9649(42) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | n/a | ζ values |
| A25 | Ω_DM/Ω_b | 5.364(65) | Planck 2018 (TT,TE,EE+lowE+lensing) | +0.2σ | Ω_c h² / Ω_b h² | integer; approximate (R11) |
| A26 | Ω_c/Ω_Λ | 0.3863(84) | Planck 2018 (TT,TE,EE+lowE+lensing) | +0.1σ | Ω_c = Ω_c h² / h² | integer; det(g); approximate (R11) |
| A27 | Ω_Λ/Ω_m | 2.172(73) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | flatness: Ω_Λ = 1 − Ω_m, neutrinos neglected | integer; approximate (R11) |
| A28 | h | 0.6736(54) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | n/a | integer |
| A29 | Ω_b/Ω_m | 0.1564(16) | Planck 2018 (TT,TE,EE+lowE+lensing) | −0.1σ | Ω_b h² / Ω_m h² | integer; det(g); approximate (R11) |
| A30 | Ω_c/Ω_m | 0.839(11) | Planck 2018 (TT,TE,EE+lowE+lensing) | +0.4σ | Ω_c h² / Ω_m h² | integer; det(g); approximate (R11) |
| A31 | σ₈ | 0.8111(60) | Planck 2018 (TT,TE,EE+lowE+lensing) | −0.3σ | n/a | integer; det(g) |
| A32 | Y_p | 0.245(3) | PDG 2024 (BBN review, eq. 24.3) | +0.3σ | n/a | integer; κ_T |
| A33 | Ω_m/Ω_Λ | 0.460(16) | Planck 2018 (TT,TE,EE+lowE+lensing) | −0.1σ | flatness: Ω_Λ = 1 − Ω_m, neutrinos neglected | integer; κ_T; approximate (R11) |
<!-- END S3-TYPE-I -->

\* Non-Gaussian profile (S3.3).

---

## S3.6 The 62 conditional and diagnostic entries

Generated from the dataset. "Reference value" is the measured value where one exists, otherwise the mathematical expectation the entry is compared with, otherwise a dash. None of these entries is counted as a prediction.

<!-- BEGIN S3-TYPE-II-IV -->
| ID | Type | Quantity | Formula or mechanism | Framework value | Reference value | Status |
|----|------|----------|----------------------|-----------------|-----------------|--------|
| B01 | II | m_u | sqrt(dim(G₂)/3) | 2.16 | 2.16 | unit assignment (R10) |
| B02 | II | m_d | ln(107) | 4.673 | 4.7 | unit assignment (R10) |
| B03 | II | m_s | τ×24 | 93.52 | 92.9 | unit assignment (R10) |
| B04 | II | m_c | (dim(G₂)-π)³ | 1280 | 1272.9 | unit assignment (R10) |
| B05 | II | m_b | 2b₂×H* | 4158 | 4186 | unit assignment (R10) |
| B06 | II | m_t | 415² | 172225 | 172600 | unit assignment (R10) |
| B07 | II | v_EW | Λ_GIFT scale bridge | 246.87 | 246.22 | scale bridge; unit assignment (R10) |
| B08 | II | M_W | (g₂/2)×v_EW | 80.4 | 80.3625 | scale bridge; unit assignment (R10) |
| B09 | II | M_Z | M_W/cos(θ_W) | 91.2 | 91.1879 | scale bridge; unit assignment (R10) |
| B10 | II | \|V_us\| | Cabibbo from b₂ | 0.2245 | 0.2243 | cascade of Type I relations; no independent content |
| B11 | II | \|V_cb\| | 2nd gen mixing | 0.04214 | 0.0422 | cascade of Type I relations; no independent content |
| B12 | II | \|V_ub\| | 3rd gen coupling | 0.003947 | 0.00394 | cascade of Type I relations; no independent content |
| B13 | II | \|V_td\| | down-type mixing | 0.008657 | 0.00867 | cascade of Type I relations; no independent content |
| B14 | II | \|V_ts\| | strange-top coupling | 0.04154 | 0.0415 | cascade of Type I relations; no independent content |
| B15 | II | \|V_tb\| | unitarity | 0.999106 | 0.999105 | cascade of Type I relations; no independent content |
| B16 | II | m_c/m_s (ext) | τ×3.49 | 13.6 | 13.6 | mixed scales (m_c at m_c, m_s at 2 GeV); not comparable |
| B17 | II | m_c/m_d | m_c/m_s (ext, B16) × m_s/m_d (A08) = τ×3.49×20 | 271.99 | 272 | cascade of B16 (Type II, not comparable) and A08; no independent content |
| B18 | II | m_b/m_d | cascade | 891.97 | 893 | cascade of Type I relations; no independent content |
| B19 | II | m_t/m_c | cascade | 135.49 | 136 | cascade of Type I relations; no independent content |
| C01 | III | m_τ/m_e (dyn) | Wilson line 3-gen optimization | 3403.1 | 3477.37 | conditional reconstruction (calibration choices, main §6.2) |
| C02 | III | m_τ/m_μ (dyn) | Wilson line 3-gen optimization | 16.5441 | 16.8177 | conditional reconstruction (calibration choices, main §6.2) |
| C03 | III | c* | Non-adiabatic threshold | 0.177828 | n/a | diagnostic of the approximate seam metric |
| C04 | III | sin²θ_W (RGE) | 2-loop MSSM RGE | 0.237655 | 0.23122 | withdrawn (supersymmetric running from a GUT boundary, main §5) |
| C05 | III | α_s (RGE) | 2-loop MSSM RGE | 0.103769 | 0.118 | withdrawn (supersymmetric running from a GUT boundary, main §5) |
| C06 | III | M_GUT | Gauge unification | 2e+16 | 2e+16 | withdrawn (supersymmetric running from a GUT boundary, main §5) |
| C07 | III | α_GUT⁻¹ | Gauge unification | 25.3 | 25.3 | withdrawn (supersymmetric running from a GUT boundary, main §5) |
| C08 | III | λ₁ | Neumann FD + Richardson | 0.124607 | n/a | diagnostic of the approximate seam metric |
| C09 | III | α_Weyl | N(λ) ~ C λ^(d/2) | 3.46002 | 3.5 | diagnostic of the approximate seam metric (compared with d/2, not a measurement) |
| C10 | III | N_KK | Unified KK tower enumeration | 22671 | n/a | diagnostic of the approximate seam metric |
| C11 | III | N_fiber | Adiabatic + explicit fiber modes | 57578 | n/a | diagnostic of the approximate seam metric |
| C12 | III | spacing | Level spacing statistics | 1.35838 | n/a | diagnostic of the approximate seam metric |
| C13 | III | κ_gauge | f_IJ eigenvalue spread | 1.0471 | 1 | diagnostic of the approximate seam metric (compared with 1, not a measurement) |
| C14 | III | rank(Y) | Mass matrix SVD | 3 | 3 | diagnostic of the approximate seam metric (compared with N_gen) |
| C15 | III | N_assoc | Homology 3-cycles with φ-calibration | 57 | n/a | diagnostic of the approximate seam metric |
| C16 | III | \|\|T\|\|_C⁰ | G₂ torsion norm | 2.98e-05 | n/a | diagnostic of the approximate seam metric |
| C17 | III | ΔV(e-τ) | Associative volume differences | 8.6331 | 8.15393 | conditional reconstruction (calibration choices, main §6.2) |
| C18 | III | ΔV(e-μ) | Associative volume differences | 3.27125 | 2.82257 | conditional reconstruction (calibration choices, main §6.2) |
| C19 | III | m_τ/m_e (comb) | S10 × exp(e^K · ΔV) | 3485.3 | 3477.37 | conditional reconstruction (calibration choices, main §6.2) |
| C20 | III | m_τ/m_μ (comb) | S10 × exp(e^K · ΔV) | 16.69 | 16.8177 | conditional reconstruction (calibration choices, main §6.2) |
| C21 | III | m_μ/m_e (comb) | S10 × exp(e^K · ΔV) | 208.8 | 206.768 | conditional reconstruction (calibration choices, main §6.2) |
| D01 | IV | b₂ | TCS K₇ | 21 | n/a | input (R1) |
| D02 | IV | b₃ | TCS K₇ | 77 | n/a | input (R1) |
| D03 | IV | H* | b₂+b₃+1 | 99 | n/a | integer combination of R1 |
| D04 | IV | N_gen | b₂/dim(K₇) | 3 | n/a | integer identity (main §2.4) |
| D05 | IV | det(g) | det(g₅) | 2.03125 | n/a | imposed normalization (R2) |
| D06 | IV | h_NK | β×η×γ | 8.95e-09 | n/a | diagnostic of the approximate seam metric |
| D07 | IV | dist(g,g*) | NK contraction ball | 4.86e-06 | n/a | diagnostic of the approximate seam metric |
| D08 | IV | \|\|T\|\|_C⁰ (cert) | Chebyshev coefficient bound | 2.95e-05 | n/a | diagnostic of the approximate seam metric |
| D09 | IV | κ(G_K3) | L² Gram matrix K3 2-forms | 1.05232 | n/a | diagnostic of the approximate seam metric |
| D10 | IV | N_levels | Unified spectrum enumeration | 22671 | n/a | diagnostic of the approximate seam metric |
| D11 | IV | N_states_total | Including degeneracies | 210060 | n/a | diagnostic of the approximate seam metric |
| D12 | IV | V_eff | Effective 7D volume from Weyl fit | 5.38e+05 | n/a | diagnostic of the approximate seam metric |
| D13 | IV | n_homology | b₃ = 77 | 77 | n/a | diagnostic of the approximate seam metric |
| D14 | IV | N_assoc | φ-calibrated cycles | 57 | n/a | diagnostic of the approximate seam metric |
| D15 | IV | \|\|Y\|\| | Total Yukawa coupling norm | 8.96902 | n/a | diagnostic of the approximate seam metric |
| D16 | IV | ΔV_range | max(V) - min(V) | 8.91952 | n/a | diagnostic of the approximate seam metric |
| D17 | IV | g_ss | g_ss = 19/6 (S¹ sector) | 3.16667 | n/a | diagnostic of the approximate seam metric |
| D18 | IV | g_T2 | g_T2 = 7/6 (T² sector) | 1.16667 | n/a | diagnostic of the approximate seam metric |
| D19 | IV | g_K3 | g_K3 ~ 64/77 (K3 sector mean) | 0.831169 | n/a | diagnostic of the approximate seam metric |
| D20 | IV | N_QNM | b2 + b3 = H* - 1 | 98 | n/a | from [42]; topological count |
| D21 | IV | b3/b3_S3S4 | b3(K7) = 77 vs b3(S3xS4) = 1 | 77 | n/a | from [42]; topological count |
| D22 | IV | M_res | tau_0 = v_EW, M_res = v_EW^2 / M_Pl | 4969.2 | n/a | from [42]; conditional on the scale identification τ₀ = v_EW |
<!-- END S3-TYPE-II-IV -->

**Withdrawn readings attached to these entries.** Earlier versions of this supplement listed "exact matches" (deviation below 0.01%) and ranked sectors by mean deviation. Both are withdrawn: an exact match between a Type II number and a PDG mass rounded to two or three figures (m_u = 2.16, m_c = 1.27 GeV) measures the rounding, not the framework; M_GUT, α_GUT⁻¹ and rank(Y) were compared with values the same computation had set; and a mean deviation measures closeness, which main §7 shows is not distinctive. The description of Q_Koide as "the most precise agreement in the framework, with no fitting involved" is withdrawn with the primary-relation reading (main §6.1): Q = 2/3 predates the framework and every invented vocabulary reaches it. An earlier table of neutrino angles in this supplement used formulas (θ₂₃ = arcsin(75/99), θ₁₂ from an auxiliary parameter) that are not the dataset's; the dataset's relations are those of main §4.1.

---

## S3.7 Lean cross-references

The Lean formalization (Arithmon/K7-Lean, main §8) verifies arithmetic identities. A verified identity says that a closed form evaluates to a number; it says nothing about the physical identification, the choice of formula, or the consistency of relations taken together. The table gives, for each of the 33 relations, the Lean declaration that ties the closed form to its value, and the scope of that proof. It is generated from `canonical/results/k7_v3_6_lean_map.json`; the library builds at the commit named, and the axioms are those reported by `#print axioms`.

<!-- BEGIN S3-LEAN -->
Arithmon/K7-Lean, branch `v3.6-alignment`, commit `34ce857`; aggregate `Certificate.RelationsV36.relations_v36_certified`, which depends only on the axioms `propext`, `Classical.choice`, `Quot.sound`.

| ID | Observable | Lean declaration (under `GIFT.`) | Location | Scope |
|----|-----------|-----------------------------------|----------|-------|
| A01 | sin²θ_W | `Certificate.RelationsV36.A01_sin2_theta_W` | Certificate/RelationsV36.lean:50 | exact rational equality of the closed form |
| A02 | α_s(M_Z) | `Certificate.RelationsV36.A02_alpha_s` | Certificate/RelationsV36.lean:55 | closed form in ℝ equal to the stated real value (no numerical bound) |
| A03 | λ_H | `Certificate.RelationsV36.A03_lambda_H` | Certificate/RelationsV36.lean:59 | closed form in ℝ equal to the stated real value (no numerical bound) |
| A04 | α⁻¹(0) | `Certificate.RelationsV36.A04_alpha_inv` | Certificate/RelationsV36.lean:65 | exact rational equality of the closed form |
| A05 | Q_Koide | `Certificate.RelationsV36.A05_Q_Koide` | Certificate/RelationsV36.lean:73 | exact rational equality of the closed form |
| A06 | m_τ/m_e | `Certificate.RelationsV36.A06_m_tau_m_e` | Certificate/RelationsV36.lean:77 | exact rational equality of the closed form |
| A07 | m_μ/m_e | `Certificate.RelationsV36.A07_m_mu_m_e` | Certificate/RelationsV36.lean:81 | base 27 and interval bounds on 27^φ |
| A08 | m_s/m_d | `Certificate.RelationsV36.A08_m_s_m_d` | Certificate/RelationsV36.lean:91 | exact rational equality of the closed form |
| A09 | m_c/m_s | `Certificate.RelationsV36.A09_m_c_m_s` | Certificate/RelationsV36.lean:95 | exact rational equality of the closed form |
| A10 | m_b/m_t | `Certificate.RelationsV36.A10_m_b_m_t` | Certificate/RelationsV36.lean:100 | exact rational equality of the closed form |
| A11 | m_u/m_d | `Certificate.RelationsV36.A11_m_u_m_d` | Certificate/RelationsV36.lean:104 | exact rational equality of the closed form |
| A12 | sin²θ₁₂ᴾᴹᴺˢ | `Certificate.RelationsV36.A12_sin2_theta12_PMNS` | Certificate/RelationsV36.lean:109 | exact rational equality of the closed form |
| A13 | sin²θ₂₃ᴾᴹᴺˢ | `Certificate.RelationsV36.A13_sin2_theta23_PMNS` | Certificate/RelationsV36.lean:113 | exact rational equality of the closed form |
| A14 | sin²θ₁₃ᴾᴹᴺˢ | `Certificate.RelationsV36.A14_sin2_theta13_PMNS` | Certificate/RelationsV36.lean:117 | exact rational equality of the closed form |
| A15 | δ_CP | `Certificate.RelationsV36.A15_delta_CP` | Certificate/RelationsV36.lean:122 | the integer 197 (the unit is not in Lean) |
| A16 | sin θ₁₂ᶜᴷᴹ | `Certificate.RelationsV36.A16_sin_theta12_CKM` | Certificate/RelationsV36.lean:126 | exact rational equality of the closed form |
| A17 | A_Wolf | `Certificate.RelationsV36.A17_A_Wolf` | Certificate/RelationsV36.lean:131 | exact rational equality of the closed form |
| A18 | sin θ₂₃ᶜᴷᴹ | `Certificate.RelationsV36.A18_sin_theta23_CKM` | Certificate/RelationsV36.lean:135 | exact rational equality of the closed form |
| A19 | m_H/m_t | `Certificate.RelationsV36.A19_m_H_m_t` | Certificate/RelationsV36.lean:140 | exact rational equality of the closed form |
| A20 | m_H/m_W | `Certificate.RelationsV36.A20_m_H_m_W` | Certificate/RelationsV36.lean:145 | exact rational equality of the closed form |
| A21 | m_W/m_Z | `Certificate.RelationsV36.A21_m_W_m_Z` | Certificate/RelationsV36.lean:150 | exact rational equality of the closed form |
| A22 | m_μ/m_τ | `Certificate.RelationsV36.A22_m_mu_m_tau` | Certificate/RelationsV36.lean:155 | exact rational equality of the closed form |
| A23 | Ω_DE | `Certificate.RelationsV36.A23_Omega_DE` | Certificate/RelationsV36.lean:159 | closed form in ℝ equal to the stated real value (no numerical bound) |
| A24 | n_s | `Certificate.RelationsV36.A24_n_s` | Certificate/RelationsV36.lean:165 | indices (11, 5) and ζ(D_bulk)/ζ(Weyl) = ζ(11)/ζ(5) (no numerical bound) |
| A25 | Ω_DM/Ω_b | `Certificate.RelationsV36.A25_Omega_DM_b` | Certificate/RelationsV36.lean:173 | exact rational equality of the closed form |
| A26 | Ω_c/Ω_Λ | `Certificate.RelationsV36.A26_Omega_c_Lambda` | Certificate/RelationsV36.lean:177 | exact rational equality of the closed form |
| A27 | Ω_Λ/Ω_m | `Certificate.RelationsV36.A27_Omega_Lambda_m` | Certificate/RelationsV36.lean:182 | exact rational equality of the closed form |
| A28 | h | `Certificate.RelationsV36.A28_hubble_h` | Certificate/RelationsV36.lean:187 | exact rational equality of the closed form |
| A29 | Ω_b/Ω_m | `Certificate.RelationsV36.A29_Omega_b_m` | Certificate/RelationsV36.lean:191 | exact rational equality of the closed form |
| A30 | Ω_c/Ω_m | `Certificate.RelationsV36.A30_Omega_c_m` | Certificate/RelationsV36.lean:196 | exact rational equality of the closed form |
| A31 | σ_8 | `Certificate.RelationsV36.A31_sigma_8` | Certificate/RelationsV36.lean:200 | exact rational equality of the closed form |
| A32 | Y_p | `Certificate.RelationsV36.A32_Y_p` | Certificate/RelationsV36.lean:204 | exact rational equality of the closed form |
| A33 | Ω_m/Ω_Λ | `Certificate.RelationsV36.A33_Omega_m_Lambda` | Certificate/RelationsV36.lean:208 | exact rational equality of the closed form |
<!-- END S3-LEAN -->

**Scope.** Every relation has a statement that ties its closed form, written in the structural constants, to its value: an exact rational equality for 27; a closed form in ℝ equal to the stated real value for α_s, λ_H and Ω_DE, with no numerical bound; the indices and the ζ-quotient for n_s, with no numerical bound; the base 27 and the bounds 206 < 27^φ < 209 for m_μ/m_e, an interval wider than the deviation it is compared with; and the integer 197 for δ_CP, whose unit is a dictionary assignment outside Lean. The 33 statements are collected in `relations_v36_certified`.

**What earlier versions cited.** Earlier versions cited the single theorem `observables_certified` (`Certificate/Predictions.lean`) as certifying the relations. That theorem is a conjunction of statements of the form `X = v` where `X` is defined as the literal `v`; each holds by definition. Before the alignment of 2026-10-22 (commit `70dc589`), 24 relations had an exact statement elsewhere in the library, 5 had only their components, 1 had bounds and 3 (m_μ/m_τ, Ω_c/Ω_m, Ω_m/Ω_Λ) had none.

**Names and withdrawn content.** The alignment renamed declarations whose names misdescribed them, keeping the old names as deprecated aliases: the CKM entries are now `sin_theta12_CKM` and `sin_theta23_CKM` (the quantities compared are sin θ, S2.4); 42 is `two_b2 := 2 * b2`, not `chi_K7` (χ(K₇) = 0, S1 §9.3); identities giving other values for the paper's observables (4/7 and 8/14 for θ₂₃, 7/23 for θ₁₂, 85/99) carry neutral arithmetic names and are documented as instances of the vocabulary freedom of S2.7. The δ_CP correction 197 × 62/69 = 12214/69 (S2.8) was removed from the aggregated certificate; its module is kept, marked withdrawn. A statement proves that the Koide parameter built from the framework's own m_μ/m_e = 27^φ and m_τ/m_e = 3477 lies strictly below 2/3 (`Relations/KoideAssembly.lean`), the incompatibility of main §6.1.

**Axioms.** The formalization rests on fourteen axioms beyond Mathlib: four that import results from the literature (`cheeger_inequality`, `literature_package`, `spectral_upper_bound`, `neck_dominates`) and ten interval certificates that import numerical enclosures (v3.5 erratum, §7.1); no `sorry` is used.

---

## S3.8 Data availability

The dataset is `canonical/data/observables.json` (95 entries; for each: formula, framework value, reference value and uncertainty, source, deviation, Lean theorem, provenance, and dated notes of every change). The refresh script and its log, and the generators of the main §4.1 table and of the S3 tables, are listed in S3.3 and S3.5. The dataset and scripts are available from the author on request pending public deposit; the spectral companion artifacts of [B] are archived on Zenodo (DOI: [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367)).

---

## References

[1] Particle Data Group, F. Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026)
[3] Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," A&A 641, A6 (2020)
[27] I. Esteban et al., "NuFit-6.0: updated global analysis of three-flavor neutrino oscillations," JHEP 12 (2024) 216, arXiv:2410.05380; NuFIT 6.1: three-neutrino fit based on data available in November 2025, www.nu-fit.org
[42] R. Pinčák, A. Pigazzini, M. Pudlák, E. Bartoš, "Geometric origin of a stable black hole remnant from torsion in G₂-manifold geometry," Gen. Rel. Grav. **58**, 29 (2026), doi:10.1007/s10714-026-03528-z
[50] CODATA 2022, Rev. Mod. Phys. 97, 025002 (2025), physics.nist.gov/cuu/Constants

**Author's related works**

- **[B]** B. de La Fournière, "Spectral Geometry of the G₂-GIFT Manifold: Betti Numbers, KK Spectrum, and Spectral Invariants," Zenodo [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) (2026).

---

*The K₇ Framework (formerly GIFT): Supplement S3: Observable Dataset*
*33 relations compared with measurement; 62 conditional and diagnostic entries*
