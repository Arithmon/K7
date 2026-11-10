---
title: "Bilan de validation"
layout: default
---

# Bilan de validation : les 33 relations face aux données actuelles

**Version du cadre** : 3.6. **Source** : article principal [§4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) et supplément [S3](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S3_observables.md) ; les tables de cette page sont copiées de l'article par un script.

**Données.** PDG 2026 pour les particules, NuFIT 6.1 pour le mélange des neutrinos (ordre normal, avec les données atmosphériques), Planck 2018 pour la cosmologie (TT,TE,EE+lowE+lensing, une seule colonne), CODATA 2022 pour α et m_μ/m_e. Toutes les incertitudes sont ramenées à 1σ. Les corrélations sont négligées, sauf dans les rapports de densité de Planck, calculés sur les chaînes publiées. L'écart normalisé est (K₇ − mesure)/σ avec la seule incertitude expérimentale : le cadre ne fournit pas d'incertitude théorique.

---

## 1. Cinq classes, pas un score

| Classe | Nombre | Relations |
|-------|-------|-----------|
| à moins de 2σ | 23 | les autres relations |
| tension (2σ < \|écart\| ≤ 3σ) | 3 | m_τ/m_e (−2,1σ), m_W/m_Z (−2,7σ), Ω_c/Ω_m (+2,5σ) |
| proximité (\|écart\| > 3σ) | 5 | α⁻¹, sin²θ_W (−7,5σ), m_μ/m_e, m_μ/m_τ (+20,8σ), m_b/m_t (−10,2σ, schéma de R7) |
| dans l'intervalle du PDG (sans incertitude) | 1 | m_s/m_d |
| profil non gaussien | 1 | sin²θ₂₃ (§4.3) |

Les versions précédentes résumaient la comparaison par un écart moyen. Ce résumé est retiré : il masquait les relations au-delà de 2σ, et un écart moyen mesure la proximité, dont le [test look-elsewhere](Statistical-Evidence.fr.html) montre qu'elle n'est pas distinctive.

## 2. La table

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
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = 37/42 | 0,880952 | 0,88136(15) | −0,046% | −2,7σ | entier ; **tension** |
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

**Vocabulaire des statuts.** *entier* : un rapport d'entiers structurels. *algébrique, φ, ln 2, valeurs de ζ* : la formule utilise l'opération correspondante. *det(g)*, *κ_T* : la formule utilise la normalisation imposée det(g) = 65/32 ou la combinaison κ_T⁻¹ = 61. *tension* : entre 2σ et 3σ, ou un écart dont la lecture est elle-même ambiguë (θ₂₃). *proximité* : au-delà de 3σ ; la relation est exclue comme égalité exacte et gardée comme proximité numérique. *approchée* : l'une de plusieurs relations mutuellement incompatibles dans un secteur surdéterminé, dont aucune n'est choisie. *assignation d'unité* : la prédiction dépend d'une unité choisie par le dictionnaire. L'astérisque de sin²θ₂₃ signale un profil non gaussien : l'écart gaussien surestime la tension.

## 3. Ce que montre la table

- **Cinq proximités sont déjà rejetées comme égalités exactes.** α⁻¹, sin²θ_W, m_μ/m_e et m_μ/m_τ se comparent à des quantités mesurées entre 10⁻¹⁰ et quelques 10⁻⁴ ; m_b/m_t est à 1,8 % du rapport dans le schéma de masse déclaré, et n'est pas sauvée par une lecture dans un autre schéma.
- **Les 33 relations ne sont pas 33 tests indépendants.** Trois secteurs sont surdéterminés, et dans chacun les relations se contredisent en tant qu'égalités exactes : quatre relations leptoniques portent sur deux rapports de masses ; trois relations CKM sur deux paramètres de Wolfenstein (sin θ₂₃ = Aλ², 2,6 % d'écart) ; sept relations de densité sur deux densités indépendantes. L'audit complet des dépendances entre les 33 n'a pas été fait : aucun compte de quantités indépendantes n'est donné.
- **La plupart des 23 ne sont testées que faiblement.** Pour les rapports de masses des quarks, les paramètres de mélange et les rapports cosmologiques, les incertitudes expérimentales sont de l'ordre du pour cent, et un accord au pour cent est ce qu'un vocabulaire riche atteint facilement.
- **sin²θ₂₃ = 6/11.** NuFIT 6.1 préfère le premier octant ; l'ajustement garde une branche dans le second, et son intervalle à 3σ (0,435 à 0,584) contient 6/11. La relation est en tension avec l'octant préféré.
- **δ_CP.** La structure produit l'entier 197. Le lire en degrés est un choix du dictionnaire, consigné au registre des résidus (R6) et compté dans le test look-elsewhere.
- **Ω_c/Ω_m.** Le Ω_m de Planck inclut les neutrinos, de sorte que Ω_b/Ω_m + Ω_c/Ω_m = 0,9955, alors que 5/32 + 27/32 = 1 : les deux formules ne sont pas compatibles avec cette définition de la matière totale.

## 4. Avec et sans la normalisation imposée

Six relations utilisent det(g) = 65/32 (λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈) et trois utilisent κ_T⁻¹ = 61 (α⁻¹, Y_p, Ω_m/Ω_Λ). Sans les six relations à det(g), il en reste 27, dont 19 à moins de 2σ ; sans les huit qui utilisent l'une ou l'autre, il en reste 25, dont 17 à moins de 2σ. Un lecteur qui tient la normalisation imposée pour un paramètre supplémentaire doit lire le cadre avec ces comptes réduits.

## 5. Les 62 autres entrées du jeu de données

Le jeu de données contient 62 autres entrées, que la version 3.6 ne compte pas comme prédictions : 19 quantités dimensionnées ou composites (type II), dont plusieurs sont des nombres lus dans une unité choisie et huit des valeurs héritées dont la dérivation n'est pas documentée ; 21 sorties de mécanismes qui consomment des choix de calibration déclarés (type III) ; et 22 diagnostics structurels sans contrepartie expérimentale (type IV). Elles sont gardées dans S3 pour la traçabilité. Le pont d'échelle et les prédictions dimensionnées des versions précédentes de cette page relèvent de ces entrées.

## 6. Règle de décision

Les relations sont énoncées comme des égalités exactes, sans incertitude théorique. Une relation est rejetée quand sa série de référence exclut sa valeur à 3σ ; après rejet, elle ne peut être gardée que comme proximité numérique, sans prétention prédictive. La règle n'a pas de clause de réparation (article principal, §11).

| # | Quantité | Valeur K₇ | Condition de rejet | Ce qui est rejeté |
|---|----------|----------|---------------------|------------------|
| D1 | la phase e^{iδ_CP}, δ_CP = 2π·197/360 | 197° | un ajustement global de la série de référence, incluant DUNE ou Hyper-Kamiokande, dont l'intervalle à 3σ exclut 197° | la relation δ_CP et l'assignation d'unité qui l'a produite |
| D2 | sin²θ₂₃ (PMNS) | 6/11 = 0,5455 | un ajustement global dont l'intervalle à 3σ exclut 6/11, dans l'un ou l'autre octant | la relation θ₂₃ |
| D3 | m_τ/m_e et Q_Koide | 1776,74 MeV et 1776,97 MeV pour m_τ | une valeur de m_τ dont l'intervalle à 3σ exclut la valeur | chaque relation exclue, séparément |
| D4 | N_gen | 3 | une quatrième génération séquentielle | l'identité entière, comme contrôle de cohérence |
| D5 | m_s/m_d | 20 | une détermination sur réseau adoptée par la série de référence, avec une incertitude dont l'intervalle à 3σ exclut 20 | la relation m_s/m_d |

Deux mesures contradictoires, hors des séries de référence, sont rapportées à côté de leur classe : h = 167/248 s'accorde avec Planck (0,0σ) et est exclu par l'échelle des distances SH0ES à 5,5σ ; m_W/m_Z = 37/42 est à −2,7σ du PDG et à −10,6σ de la masse du W de CDF II. Tant que les méthodes divergent, le statut est donné des deux façons, et aucun des deux accords ne vaut confirmation.

## 7. Ce qui est vérifié, et ce qui ne l'est pas

L'arithmétique des 33 relations est vérifiée par machine en Lean 4 (K7-Lean, `relations_v36_certified`) : étant donné les entiers déclarés, chaque forme close s'évalue au nombre annoncé. Cela n'établit ni l'existence de K₇, ni l'interprétation physique d'une relation, ni le choix des attributions. Aucune variété G₂ compacte sans torsion de nombres de Betti (21, 77) n'est construite à ce jour.

---

*K₇ Framework v3.6 | page générée depuis les sources de l'article par `k7_v3_6_surface_pages.py`*
