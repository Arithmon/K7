---
title: "Référence des observables"
layout: default
---

# Référence des observables

**Version du cadre** : 3.6. **Source** : article principal [§3–§4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) et supplément [S3](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S3_observables.md) ; toutes les tables de cette page sont copiées de l'article par un script. Données lisibles par machine : [`observables.csv`](https://github.com/Arithmon/K7/blob/main/publications/references/observables.csv) (95 entrées).

Le jeu de données a 95 entrées. **33 sont des relations** comparées à la mesure et comptées dans l'article principal ; **62 sont des extractions conditionnelles et des diagnostics**, gardés pour la traçabilité et non comptés comme prédictions. Les versions précédentes de cette page comptaient les 95 comme observables prédites par le cadre et les résumaient par un écart moyen ; les deux sont retirés.

Les tables des sections 1, 2, 4 et 5 et la table des données de référence sont reprises telles quelles de l'article, en anglais.

---

## 1. Types

| Type | Count | What it is | Counted in main §4 |
|------|-------|-----------|--------------------|
| I | 33 | Dimensionless closed forms in the structural constants, assigned to measured parameters | yes |
| II | 19 | Dimensionful numbers read in a chosen unit (register item R10, the unit of dimensionful entries), scale bridges, one ratio of masses taken at different scales and its product with m_s/m_d, and legacy values without a documented derivation | no |
| III | 21 | Outputs of mechanisms on the approximate seam metric (Wilson-line splitting, associative volumes, spectral counts, bundle conditioning), with calibration choices; and four retired entries of a supersymmetric running | no |
| IV | 22 | Structural quantities and numerical diagnostics, with no experimental counterpart | no |

## 2. Les constantes structurelles

Les 33 relations sont toutes écrites avec vingt constantes structurelles. Sept sont primitives ; treize en sont dérivées, et cette dérivation fait partie du dictionnaire.

| # | Constant | Value | Origin | Status |
|---|----------|-------|--------|--------|
| 1 | dim(E₈) | 248 | Lie algebra | Lie datum |
| 2 | rank(E₈) | 8 | Cartan subalgebra | Lie datum |
| 3 | dim(G₂) | 14 | Aut(𝕆) | Lie datum |
| 4 | dim(K₇) | 7 | Im(𝕆) | topological |
| 5 | b₂(K₇) | 21 | posited (§10) | input |
| 6 | b₃(K₇) | 77 | posited (§10) | input |
| 7 | dim(J₃(𝕆)) | 27 | exceptional Jordan algebra | Lie datum |
| 8 | N_gen | 3 | b₂/dim(K₇); the integer identity of §2.4 | measured, reproduced |
| 9 | p₂ | 2 | dim(G₂)/dim(K₇) ("binary ratio"; not a Pontryagin class) | combination |
| 10 | Weyl | 5 | factor of \|W(E₈)\| | combination |
| 11 | H* | 99 | b₂ + b₃ + 1 | combination |
| 12 | dim(E₆) | 78 | Lie algebra | Lie datum |
| 13 | dim(E₇) | 133 | Lie algebra | Lie datum |
| 14 | dim(F₄) | 52 | Aut(J₃(𝕆)) | Lie datum |
| 15 | fund(E₇) | 56 | fundamental representation | Lie datum |
| 16 | \|PSL(2,7)\| | 168 | automorphisms of the Fano plane | Lie datum |
| 17 | D_bulk | 11 | 4 + 7 | combination |
| 18 | α_sum | 13 | rank(E₈) + Weyl | combination |
| 19 | det_den | 32 | b₂ + dim(G₂) − N_gen | combination; enters det(g) |
| 20 | det_num | 65 | p₂ · det_den + 1 (also Weyl × α_sum) | combination; enters det(g) |

N_gen = 3 est une identité entière (b₂/dim K₇), pas le résultat d'un théorème de l'indice. b₂ et b₃ sont des entrées posées par le cadre, pas des quantités confirmées par un calcul : aucune variété G₂ compacte de nombres (21, 77) n'est construite à ce jour.

## 3. Les 33 relations

Formules, valeurs et statut. Données : PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022 ; incertitudes à 1σ. L'écart normalisé est (K₇ − mesure)/σ avec la seule incertitude expérimentale.

| ID | Observable | Formule | Valeur K₇ | Mesure | Écart | Écart normalisé | Statut |
|---|-------|-------------|------|----------|------|-----|--------|
| A01 | sin²θ_W (M_Z) | b₂/(b₃ + dim G₂) = 3/13 | 0,230769 | 0,23122(6) | −0,19% | −7,5σ | entier ; **proximité** |
| A02 | α_s(M_Z) | √2/(dim G₂ − p₂) = √2/12 | 0,117851 | 0,1180(9) | −0,13% | −0,2σ | algébrique |
| A03 | λ_H | √(dim G₂ + N_gen)/det_den = √17/32 | 0,128847 | 0,12914(23) | −0,22% | −1,3σ | algébrique ; det(g) |
| A04 | α⁻¹(0) | 128 + 9 + det(g)·κ_T | 137,0333 | 137,035999177(21) | −0,0020% | ≫ 10σ | det(g), κ_T ; **proximité** |
| A05 | Q_Koide | dim G₂/b₂ = 2/3 | 0,666667 | 0,6666645(51) | +0,0003% | +0,4σ | entier ; approchée (R8) |
| A06 | m_τ/m_e | 7 + 10·248 + 10·99 = 3477 | 3477 | 3477,37(18) | −0,011% | −2,1σ | entier ; approchée (R8) ; **tension** |
| A07 | m_μ/m_e | 27^φ | 207,012 | 206,7682827(46) | +0,12% | ≫ 10σ | φ ; approchée (R8) ; **proximité** |
| A08 | m_s/m_d | p₂² × Weyl = 20 | 20 | 17–22 (intervalle) | s.o. | s.o. | entier ; dans l'intervalle du PDG |
| A09 | m_c/m_s | (dim E₈ − p₂)/b₂ = 246/21 | 11,714 | 11,769(35) | −0,46% | −1,6σ | entier |
| A10 | m_b/m_t | 1/(2b₂) = 1/42 | 0,023810 | 0,024253(43) | −1,83% | −10,2σ | entier ; **proximité** (dans le schéma déclaré en R7) |
| A11 | m_u/m_d | (1 + dim E₆)/\|PSL(2,7)\| = 79/168 | 0,470238 | 0,462(12) | +1,78% | +0,7σ | entier |
| A12 | sin²θ₁₂ (PMNS) | (1 + N_gen)/α_sum = 4/13 | 0,307692 | 0,3088(+67/−66) | −0,36% | −0,2σ | entier |
| A13 | sin²θ₂₃ (PMNS) | (D_bulk − Weyl)/D_bulk = 6/11 | 0,545455 | 0,470(+17/−14) | +16,05% | +4,4σ* | entier ; **tension** (octant ; dans l'intervalle à 3σ de NuFIT, §4.3) |
| A14 | sin²θ₁₃ (PMNS) | D_bulk/dim(E₈×E₈) = 11/496 | 0,022177 | 0,02248(+55/−59) | −1,35% | −0,5σ | entier |
| A15 | δ_CP | dim K₇ · dim G₂ + H* = 197 | 197 → phase 2π·197/360 | 212 (+26/−36)° | −7,08% | −0,4σ | **assignation d'unité** (R6) |
| A16 | sin θ₁₂ (CKM) | fund(E₇)/dim E₈ = 56/248 | 0,225806 | 0,22517(68) | +0,28% | +0,9σ | entier ; approchée (R12) |
| A17 | A (Wolfenstein) | (Weyl + dim E₆)/H* = 83/99 | 0,838384 | 0,826(+17/−15) | +1,50% | +0,7σ | entier ; approchée (R12) |
| A18 | sin θ₂₃ (CKM) | dim K₇/\|PSL(2,7)\| = 7/168 | 0,041667 | 0,04189(+81/−69) | −0,53% | −0,3σ | entier ; approchée (R12) |
| A19 | m_H/m_t | fund(E₇)/b₃ = 56/77 | 0,727273 | 0,7250(13) | +0,32% | +1,8σ | entier |
| A20 | m_H/m_W | (N_gen + dim E₆)/dim F₄ = 81/52 | 1,557692 | 1,5571(14) | +0,040% | +0,5σ | entier |
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = 37/42 | 0,880952 | 0,881285(87) | −0,038% | −3,8σ | entier ; **proximité** |
| A22 | m_μ/m_τ | (b₂ − D_bulk)/\|PSL(2,7)\| = 10/168 | 0,059524 | 0,0594612(30) | +0,11% | +20,8σ | entier ; approchée (R8) ; **proximité** |
| A23 | Ω_DE | ln 2 · (b₂ + b₃)/H* | 0,686146 | 0,6847(73) | +0,21% | +0,2σ | ln 2 ; approchée (R11) |
| A24 | n_s | ζ(11)/ζ(5) | 0,964864 | 0,9649(42) | −0,0037% | 0,0σ | valeurs de ζ |
| A25 | Ω_DM/Ω_b | (1 + 2b₂)/rank E₈ = 43/8 | 5,375 | 5,364(77) | +0,21% | +0,1σ | entier ; approchée (R11) |
| A26 | Ω_c/Ω_Λ | det_num/\|PSL(2,7)\| = 65/168 | 0,386905 | 0,387(14) | +0,10% | 0,0σ | entier ; det(g) ; approchée (R11) |
| A27 | Ω_Λ/Ω_m | (dim G₂ + H*)/dim F₄ = 113/52 | 2,173077 | 2,173(74) | −0,017% | 0,0σ | entier ; approchée (R11) |
| A28 | h | (\|PSL(2,7)\| − 1)/dim E₈ = 167/248 | 0,673387 | 0,6736(54) | −0,032% | 0,0σ | entier |
| A29 | Ω_b/Ω_m | Weyl/det_den = 5/32 | 0,15625 | 0,1565(19) | −0,13% | −0,1σ | entier ; det(g) ; approchée (R11) |
| A30 | Ω_c/Ω_m | (det_den − Weyl)/det_den = 27/32 | 0,84375 | 0,8390(19) | +0,56% | +2,5σ | entier ; det(g) ; approchée (R11) ; **tension** |
| A31 | σ₈ | (p₂ + det_den)/(2b₂) = 34/42 | 0,809524 | 0,8111(60) | −0,19% | −0,3σ | entier ; det(g) |
| A32 | Y_p | (1 + dim G₂)/κ_T⁻¹ = 15/61 | 0,245902 | 0,245(3) | +0,37% | +0,3σ | entier ; κ_T |
| A33 | Ω_m/Ω_Λ | (1 + dim J₃(𝕆))/κ_T⁻¹ = 28/61 | 0,459016 | 0,461(16) | −0,35% | −0,1σ | entier ; κ_T ; approchée (R11) |

Les classes, les secteurs surdéterminés et la règle de décision sont dans le [bilan de validation](Validation-Summary.fr.html). L'accord est-il distinctif : [éléments statistiques](Statistical-Evidence.fr.html).

### Données de référence et conventions

| ID | Observable | Measured | Source | Pull | Convention / note | Status |
|---|--------|------------|-------|----|---------------------|---------------|
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
| A13 | sin²θ₂₃ (PMNS) | 0.470(+17/−14) | NuFIT 6.1 (IC24+SK-atm, NO) | +4.4σ* | 3σ range 41.27°–49.86°, i.e. sin² 0.435–0.584, contains 6/11 | integer; **tension** (octant; inside the NuFIT 3σ range, main §4.3) |
| A14 | sin²θ₁₃ (PMNS) | 0.02248(+55/−59) | NuFIT 6.1 (IC24+SK-atm, NO) | −0.5σ | n/a | integer |
| A15 | δ_CP | 212 (+26/−36)° | NuFIT 6.1 (IC24+SK-atm, NO) | −0.4σ | degrees | **unit assignment** (R6) |
| A16 | sin θ₁₂ (CKM) | 0.22517(68) | PDG 2026 | +0.9σ | PDG CKM review: sin θ₁₂ = λ (not squared) | integer; approximate (R12) |
| A17 | A (Wolfenstein) | 0.826(+17/−15) | PDG 2026 | +0.7σ | PDG CKM review, Wolfenstein fit | integer; approximate (R12) |
| A18 | sin θ₂₃ (CKM) | 0.04189(+81/−69) | PDG 2026 | −0.3σ | PDG CKM review: sin θ₂₃ = Aλ² (not squared) | integer; approximate (R12) |
| A19 | m_H/m_t | 0.7250(13) | PDG 2026 | +1.8σ | m_t from direct measurements | integer |
| A20 | m_H/m_W | 1.5571(14) | PDG 2026 | +0.5σ | n/a | integer |
| A21 | m_W/m_Z | 0.881285(87) | PDG 2026 | −3.8σ | from the PDG 2026 masses | integer; **proximity** |
| A22 | m_μ/m_τ | 0.0594612(30) | PDG 2026 | +20.8σ | from the PDG 2026 masses | integer; approximate (R8); **proximity** |
| A23 | Ω_DE | 0.6847(73) | Planck 2018 (TT,TE,EE+lowE+lensing) | +0.2σ | Ω_Λ | ln 2; approximate (R11) |
| A24 | n_s | 0.9649(42) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | n/a | ζ values |
| A25 | Ω_DM/Ω_b | 5.364(77) | Planck 2018 (TT,TE,EE+lowE+lensing) | +0.1σ | Ω_c h² / Ω_b h² | integer; approximate (R11) |
| A26 | Ω_c/Ω_Λ | 0.387(14) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | Ω_c h² / h² / Ω_Λ | integer; det(g); approximate (R11) |
| A27 | Ω_Λ/Ω_m | 2.173(74) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | Ω_Λ / Ω_m, Planck definitions | integer; approximate (R11) |
| A28 | h | 0.6736(54) | Planck 2018 (TT,TE,EE+lowE+lensing) | 0.0σ | n/a | integer |
| A29 | Ω_b/Ω_m | 0.1565(19) | Planck 2018 (TT,TE,EE+lowE+lensing) | −0.1σ | Ω_b h² / Ω_m h², Ω_m includes neutrinos | integer; det(g); approximate (R11) |
| A30 | Ω_c/Ω_m | 0.8390(19) | Planck 2018 (TT,TE,EE+lowE+lensing) | +2.5σ | Ω_c h² / Ω_m h², Ω_m includes neutrinos | integer; det(g); approximate (R11); **tension** |
| A31 | σ₈ | 0.8111(60) | Planck 2018 (TT,TE,EE+lowE+lensing) | −0.3σ | n/a | integer; det(g) |
| A32 | Y_p | 0.245(3) | PDG 2024 (BBN review, eq. 24.3) | +0.3σ | n/a | integer; κ_T |
| A33 | Ω_m/Ω_Λ | 0.461(16) | Planck 2018 (TT,TE,EE+lowE+lensing) | −0.1σ | Ω_m / Ω_Λ, Planck definitions | integer; κ_T; approximate (R11) |

## 4. Les 62 entrées conditionnelles et diagnostiques

« Reference value » est la valeur mesurée quand il y en a une, sinon l'attendu mathématique auquel l'entrée est comparée, sinon n/a. Aucune de ces entrées n'est comptée comme prédiction.

| ID | Type | Quantity | Formula or mechanism | Framework value | Reference value | Status |
|---|---|-------|-------------|------|------|----------------------|
| B01 | II | m_u | sqrt(dim(G₂)/3) | 2.16025 | 2.16 | unit assignment (R10) |
| B02 | II | m_d | ln(107) | 4.673 | 4.7 | unit assignment (R10) |
| B03 | II | m_s | τ×24 | 93.52 | 92.9 | unit assignment (R10) |
| B04 | II | m_c | (dim(G₂)-π)³ | 1280.26 | 1272.9 | unit assignment (R10) |
| B05 | II | m_b | 2b₂×H* | 4158 | 4186 | unit assignment (R10) |
| B06 | II | m_t | 415² | 172225 | 172600 | unit assignment (R10) |
| B07 | II | v_EW | Scale bridge from the unit assignment (R10) | 246.87 | 246.22 | scale bridge; unit assignment (R10) |
| B08 | II | M_W | (g₂/2)×v_EW | 80.4 | 80.3625 | scale bridge; unit assignment (R10) |
| B09 | II | M_Z | M_W/cos(θ_W) | 91.2 | 91.1879 | scale bridge; unit assignment (R10) |
| B10 | II | \|V_us\| | not documented (legacy label: Cabibbo from b₂) | 0.2245 | 0.2243 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B11 | II | \|V_cb\| | not documented (legacy label: 2nd gen mixing) | 0.04214 | 0.0422 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B12 | II | \|V_ub\| | not documented (legacy label: 3rd gen coupling) | 0.003947 | 0.00394 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B13 | II | \|V_td\| | not documented (legacy label: down-type mixing) | 0.008657 | 0.00867 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B14 | II | \|V_ts\| | not documented (legacy label: strange-top coupling) | 0.04154 | 0.0415 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B15 | II | \|V_tb\| | not documented (legacy label: unitarity) | 0.999106 | 0.999105 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B16 | II | m_c/m_s (ext) | τ×3.49 | 13.6 | 13.6 | mixed scales (m_c at m_c, m_s at 2 GeV); not comparable |
| B17 | II | m_c/m_d | m_c/m_s (ext, B16) × m_s/m_d (A08) = τ×3.49×20 | 271.99 | 272 | cascade of B16 (Type II, not comparable) and A08; no independent content |
| B18 | II | m_b/m_d | not documented (legacy label: cascade) | 891.97 | 893 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| B19 | II | m_t/m_c | not documented (legacy label: cascade) | 135.49 | 136 | Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction |
| C01 | III | m_τ/m_e (dyn) | Wilson line 3-gen optimization | 3403.1 | 3477.37 | conditional reconstruction (calibration choices, main §6.2) |
| C02 | III | m_τ/m_μ (dyn) | Wilson line 3-gen optimization | 16.5441 | 16.8177 | conditional reconstruction (calibration choices, main §6.2) |
| C03 | III | c* | Non-adiabatic threshold | 0.177828 | n/a | diagnostic of the approximate local metric |
| C04 | III | sin²θ_W (RGE) | 2-loop MSSM RGE | 0.237655 | 0.23122 | retired (supersymmetric running from a GUT boundary; main App. D) |
| C05 | III | α_s (RGE) | 2-loop MSSM RGE | 0.103769 | 0.118 | retired (supersymmetric running from a GUT boundary; main App. D) |
| C06 | III | M_GUT | Gauge unification | 2e+16 | 2e+16 | retired (supersymmetric running from a GUT boundary; main App. D) |
| C07 | III | α_GUT⁻¹ | Gauge unification | 25.3 | 25.3 | retired (supersymmetric running from a GUT boundary; main App. D) |
| C08 | III | λ₁ | Neumann FD + Richardson | 0.124607 | n/a | diagnostic of the approximate local metric |
| C09 | III | α_Weyl | N(λ) ~ C λ^(d/2) | 3.46002 | 3.5 | diagnostic of the approximate local metric (compared with d/2, not a measurement) |
| C10 | III | N_KK | Unified KK tower enumeration | 22671 | n/a | diagnostic of the approximate local metric |
| C11 | III | N_fiber | Adiabatic + explicit fiber modes | 57578 | n/a | diagnostic of the approximate local metric |
| C12 | III | spacing | Level spacing statistics | 1.35838 | n/a | diagnostic of the approximate local metric |
| C13 | III | κ_gauge | f_IJ eigenvalue spread | 1.0471 | 1 | diagnostic of the approximate local metric (compared with 1, not a measurement) |
| C14 | III | n_SD | Count of positive eigenvalues of the K3 intersection form | 3 | 3 | diagnostic of the approximate local metric (compared with N_gen) |
| C15 | III | N_assoc | Homology 3-cycles with φ-calibration | 57 | n/a | diagnostic of the approximate local metric |
| C16 | III | \|\|T\|\|_C⁰ | G₂ torsion norm | 2.98e-05 | n/a | diagnostic of the approximate local metric |
| C17 | III | ΔV(e-τ) | Associative volume differences | 8.6331 | 8.15393 | conditional reconstruction (calibration choices, main §6.2) |
| C18 | III | ΔV(e-μ) | Associative volume differences | 3.27125 | 2.82257 | conditional reconstruction (calibration choices, main §6.2); mismatched reference (see Type III above) |
| C19 | III | m_τ/m_e (comb) | Wilson-line ratio × exp(e^K · ΔV) | 3485.3 | 3477.37 | conditional reconstruction (calibration choices, main §6.2) |
| C20 | III | m_τ/m_μ (comb) | Wilson-line ratio × exp(e^K · ΔV) | 16.69 | 16.8177 | conditional reconstruction (calibration choices, main §6.2); inherits the C18 pairing |
| C21 | III | m_μ/m_e (comb) | Wilson-line ratio × exp(e^K · ΔV) | 208.8 | 206.768 | conditional reconstruction (calibration choices, main §6.2); ratio C19/C20, inherits the C18 pairing |
| D01 | IV | b₂ | TCS K₇ | 21 | n/a | input (R1) |
| D02 | IV | b₃ | TCS K₇ | 77 | n/a | input (R1) |
| D03 | IV | H* | b₂+b₃+1 | 99 | n/a | integer combination of R1 |
| D04 | IV | N_gen | b₂/dim(K₇) | 3 | n/a | integer identity (main §2.4) |
| D05 | IV | det(g) | det(g₅) | 2.03125 | n/a | imposed normalization (R2) |
| D06 | IV | h_NK | β×η×γ | 8.95e-09 | n/a | diagnostic of the approximate local metric |
| D07 | IV | dist(g,g*) | NK contraction ball | 4.86e-06 | n/a | diagnostic of the approximate local metric |
| D08 | IV | \|\|T\|\|_C⁰ (cert) | Chebyshev coefficient bound | 2.95e-05 | n/a | diagnostic of the approximate local metric |
| D09 | IV | κ(G_K3) | L² Gram matrix K3 2-forms | 1.05232 | n/a | diagnostic of the approximate local metric |
| D10 | IV | N_levels | Unified spectrum enumeration | 22671 | n/a | diagnostic of the approximate local metric |
| D11 | IV | `N_states_total` | Including degeneracies | 210060 | n/a | diagnostic of the approximate local metric |
| D12 | IV | V_eff | Effective 7D volume from Weyl fit | 5.38e+05 | n/a | diagnostic of the approximate local metric |
| D13 | IV | n_homology | b₃ = 77 | 77 | n/a | diagnostic of the approximate local metric |
| D14 | IV | N_assoc | φ-calibrated cycles | 57 | n/a | diagnostic of the approximate local metric |
| D15 | IV | \|\|Y\|\| | Total Yukawa coupling norm | 8.96902 | n/a | diagnostic of the approximate local metric |
| D16 | IV | ΔV_range | max(V) - min(V) | 8.91952 | n/a | diagnostic of the approximate local metric |
| D17 | IV | g_ss | g_ss = 19/6 (S¹ sector) | 3.16667 | n/a | diagnostic of the approximate local metric |
| D18 | IV | g_T2 | g_T2 = 7/6 (T² sector) | 1.16667 | n/a | diagnostic of the approximate local metric |
| D19 | IV | g_K3 | g_K3 ~ 64/77 (K3 sector mean) | 0.831169 | n/a | diagnostic of the approximate local metric |
| D20 | IV | N_QNM | b2 + b3 = H* - 1 | 98 | n/a | from [42]; topological count |
| D21 | IV | `b3/b3_S3S4` | b3(K7) = 77 vs b3(S3xS4) = 1 | 77 | n/a | from [42]; topological count |
| D22 | IV | M_res | tau_0 = v_EW, M_res = v_EW^2 / M_Pl | 4969.2 | n/a | from [42]; conditional on the scale identification τ₀ = v_EW |

## 5. Renvois Lean

L'arithmétique de chacune des 33 relations est vérifiée par machine en Lean 4 (Arithmon/K7-Lean, agrégat `relations_v36_certified`). La formalisation vérifie que chaque forme close s'évalue au nombre annoncé ; elle n'établit ni le contenu physique d'une relation ni le choix des attributions.

| ID | Observable | Lean declaration (under `GIFT.`) | Location | Scope |
|---|------|---------------------|-------------|-------------|
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

---

*K₇ Framework v3.6 | page générée depuis les sources de l'article par `k7_v3_6_surface_pages.py`*
