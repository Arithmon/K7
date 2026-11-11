---
title: "Éléments statistiques"
layout: default
---

# Éléments statistiques : le test look-elsewhere

**Version du cadre** : 3.6. **Source** : article principal [§7](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) et supplément [S4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md) ; les tables de cette page sont copiées de S4 par un script, sans retouche à la main.

Un cadre qui retrouve 33 valeurs mesurées par des formes closes, avec un vocabulaire de vingt constantes, doit d'abord répondre à une question : combien de fois la même grammaire, avec un autre vocabulaire, les aurait-elle retrouvées aussi bien ? La version 3.6 a posé cette question par un test préenregistré. La réponse est que **la proximité avec les valeurs mesurées ne distingue pas K₇** dans les classes de référence testées. Les affirmations statistiques des versions précédentes de cette page sont retirées ; la section 6 les énumère.

---

## 1. Résumé

| | |
|---|---|
| **Question** | K₇ reste-t-il exceptionnel quand chaque concurrent cherche ses propres formules, dans la même grammaire, avec le même budget et la même liberté d'attribution et d'unité ? |
| **Préenregistré** | le 2026-10-17, avant tout passage, avec deux issues seulement : une valeur P globale calibrée, ou le retrait de la valeur P du texte |
| **K₇** | atteint 31 des 33 cibles |
| **Paires de Betti alternatives** | 1 085 sur 4 159 en atteignent autant (P = 0,26) ; aucune n'en atteint plus |
| **Vocabulaires inventés** | 1 015 sur 2 000 en atteignent autant (P = 0,51) ; aucun n'en atteint plus |
| **Contrôle sans constante de K₇** | atteint 30 des 33 avec les seules feuilles universelles de la grammaire |
| **Verdict** | valeur p globale de 0,51 pour un seuil de 0,01 : l'effet look-elsewhere n'est pas surmonté, et la valeur P est retirée du texte |

La valeur 0,51 n'est pas la probabilité que K₇ soit juste ou faux, et ces comptes ne sont pas une réfutation physique. Ils disent que le meilleur score discrimine peu dans ce protocole : 30 cibles sont atteintes par tous, deux par personne, et une seule sépare les concurrents.

## 2. Le test

- **Cibles.** Les 33 relations du jeu de données ([S3](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S3_observables.md)), avec leurs valeurs mesurées et leurs incertitudes.
- **Grammaire.** Le moteur gelé du Sieve : ses feuilles universelles (1 à 9, π, e, φ, γ, ln 2, ζ(3) à ζ(11)) plus les 19 constantes entières du concurrent, les opérations + − × / ^, racine carrée, inverse, carré et logarithme, et **cinq nœuds au plus** par expression.
- **Concordance.** Une cible est atteinte si une expression du vocabulaire tombe à moins de 2σ de la valeur mesurée, de part et d'autre, les incertitudes asymétriques restant asymétriques. Pour m_s/m_d, que le PDG donne comme un intervalle, la fenêtre est cet intervalle. Pour δ_CP, la phase peut être lue en degrés, radians, grades ou tours.
- **Attribution.** La recherche est aveugle : chaque cible reçoit l'expression concordante la moins coûteuse. La liberté d'attribuer les formules aux observables est donnée à tous, K₇ compris, qui est noté par la même recherche sur son propre vocabulaire et non par ses formules publiées.
- **Concurrents.** Toute paire de Betti avec b₂ dans [1, 40] et b₃ dans [17, 120] autre que (21, 77), avec H*, κ_T⁻¹ et det(g) re-dérivés et les autres constantes gardées aux valeurs de K₇ ; et 2 000 vocabulaires de 19 entiers tirés par le générateur gelé du Sieve.
- **Règle de verdict.** Pour une famille de taille N où n concurrents atteignent au moins autant de cibles que K₇, P = (1 + n)/(1 + N), les égalités comptant contre K₇. La valeur p globale est la plus grande des deux valeurs, et l'effet n'est surmonté que si elle vaut au plus 0,01.

L'alphabet testé pour K₇ est celui des dix-neuf entiers du registre Monte Carlo de la version 3.5, et non littéralement les vingt constantes de l'article principal (§3.1) : dim E₇ = 133 et α_sum = 13 en sont absents, κ_T⁻¹ = 61 y figure. Un test sur le registre littéral serait un autre calcul.

## 3. Résultat

| Famille | N | atteignent ≥ 31/33 (autant que K₇) | P = (1 + n)/(1 + N) | meilleure couverture | coût de description, étendue (bits) | coût ≤ K₇ |
|---|---:|---:|---:|---:|---:|---:|
| K₇ (21, 77), recherche aveugle sur son propre vocabulaire | 1 | 31/33 | s.o. | 31 | 408,1 | s.o. |
| paires de Betti alternatives (dérivations publiées) | 4 159 | 1 085 | 0,261 | 31 | 389,2 à 418,7 | 1 038 |
| vocabulaires inventés (générateur de [M]) | 2 000 | 1 015 | 0,508 | 31 | 385,0 à 430,4 | 628 |
| paires de Betti alternatives, dérivations variantes (hors règle) | 4 160 | 723 | 0,174 | 31 | 391,3 à 417,6 | 548 |

La valeur p globale, la plus grande des deux premières lignes, vaut **0,508** ; seuil 0,01. La ligne de la variante n'entre pas dans le verdict. K₇ n'est pas moins coûteux non plus : son coût de description se situe dans l'étendue des deux familles.

Par cible :

| ID | Observable | K₇ atteint (aveugle) | valeur publiée dans l'ensemble ≤ 5 nœuds de K₇ | valeur publiée dans la fenêtre | paires de Betti qui atteignent (sur 4 159) | vocabulaires qui atteignent (sur 2 000) |
|---|---|---|---|---|---:|---:|
| A01 | sin²θ_W | oui | oui | non | 4 159 | 2 000 |
| A02 | α_s(M_Z) | oui | oui | oui | 4 159 | 2 000 |
| A03 | λ_H | oui | non | oui | 4 159 | 2 000 |
| A04 | α⁻¹(0) | non | non | non | 0 | 0 |
| A05 | Q_Koide | oui | oui | oui | 4 159 | 2 000 |
| A06 | m_τ/m_e | oui | oui | non | 1 085 | 1 015 |
| A07 | m_μ/m_e | non | non | non | 0 | 0 |
| A08 | m_s/m_d | oui | oui | oui | 4 159 | 2 000 |
| A09 | m_c/m_s | oui | oui | oui | 4 159 | 2 000 |
| A10 | m_b/m_t | oui | oui | non | 4 159 | 2 000 |
| A11 | m_u/m_d | oui | oui | oui | 4 159 | 2 000 |
| A12 | sin²θ₁₂ᴾᴹᴺˢ | oui | oui | oui | 4 159 | 2 000 |
| A13 | sin²θ₂₃ᴾᴹᴺˢ | oui | oui | non | 4 159 | 2 000 |
| A14 | sin²θ₁₃ᴾᴹᴺˢ | oui | oui | oui | 4 159 | 2 000 |
| A15 | δ_CP | oui | oui | oui | 4 159 | 2 000 |
| A16 | sin θ₁₂ᶜᴷᴹ | oui | oui | oui | 4 159 | 2 000 |
| A17 | A_Wolf | oui | oui | oui | 4 159 | 2 000 |
| A18 | sin θ₂₃ᶜᴷᴹ | oui | oui | oui | 4 159 | 2 000 |
| A19 | m_H/m_t | oui | oui | oui | 4 159 | 2 000 |
| A20 | m_H/m_W | oui | oui | oui | 4 159 | 2 000 |
| A21 | m_W/m_Z | oui | non | non | 4 159 | 2 000 |
| A22 | m_μ/m_τ | oui | oui | non | 4 159 | 2 000 |
| A23 | Ω_DE | oui | oui | oui | 4 159 | 2 000 |
| A24 | n_s | oui | non | oui | 4 159 | 2 000 |
| A25 | Ω_DM/Ω_b | oui | oui | oui | 4 159 | 2 000 |
| A26 | Ω_c/Ω_Λ | oui | oui | oui | 4 159 | 2 000 |
| A27 | Ω_Λ/Ω_m | oui | oui | oui | 4 159 | 2 000 |
| A28 | h | oui | oui | oui | 4 159 | 2 000 |
| A29 | Ω_b/Ω_m | oui | oui | oui | 4 159 | 2 000 |
| A30 | Ω_c/Ω_m | oui | oui | non | 4 159 | 2 000 |
| A31 | σ_8 | oui | oui | oui | 4 159 | 2 000 |
| A32 | Y_p | oui | oui | oui | 4 159 | 2 000 |
| A33 | Ω_m/Ω_Λ | oui | oui | oui | 4 159 | 2 000 |

La plupart des cibles sont atteintes par tous les concurrents : à cinq nœuds et 2σ, la grammaire les couvre quel que soit le vocabulaire. Les cibles qui discriminent sont les rares dont l'incertitude relative est très petite. α⁻¹ et m_μ/m_e ne sont atteintes par personne, K₇ compris. m_τ/m_e est atteinte par K₇ et par un tiers environ des concurrents, et les comptes de la table des familles sont exactement ceux de cette seule cible. Trois scores sont à distinguer : les formules publiées (24 des 33 tombent dans leur fenêtre), la recherche libre avec l'alphabet de K₇ (31), et le contrôle sans constante de K₇ (30).

## 4. Le tableau du Sieve

Le Sieve est une batterie publique de quatre tests nuls, avec une liste d'observables et une grammaire gelées. Le premier demande si une relation est isolée dans le vocabulaire fixé ; le deuxième chiffre la liberté d'avoir choisi le vocabulaire ; le troisième et le quatrième permutent coefficients et cibles. Son tableau publié pour les relations de K₇ donne :

- n_s et m_H/m_W passent le test d'isolement sur ses trois axes.
- Aucune des deux ne passe le test de liberté du vocabulaire : un vocabulaire inventé de même budget les retrouve aussi bien (pour m_H/m_W, 22 vocabulaires inventés sur 24).
- Q_Koide est isolée dans le vocabulaire fixé, mais sa valeur 2/3 est atteinte par tous les vocabulaires : une égalité, pas une survivante.
- Sur les neuf relations peu profondes soumises au test de liberté du vocabulaire, l'enveloppe des vocabulaires inventés est battue 0 fois sur 9.

Ce que ce test ne peut pas chiffrer, c'est d'où vient le vocabulaire : les constantes de K₇ sont des dimensions et des rangs de E₈ et les nombres de Betti, pas une liste inventée. C'est un fait sur l'origine des constantes, pas l'indice qu'elles ont été choisies avant de connaître les données.

## 5. Ce que le test ne couvre pas, et son histoire

Le test ne fait varier ni le groupe de jauge ni l'holonomie au-delà des nombres de Betti, ne considère pas d'autres formes d'une observable (un angle plutôt que le carré de son sinus) hormis l'unité de δ_CP, et ne va pas au-delà de cinq nœuds, où se trouvent plusieurs formules de K₇. Ces libertés restent au registre des résidus de l'article principal (attribution des formules, grammaire, unité).

Le préenregistrement a été amendé trois fois, chaque fois après une revue externe et sans changer la question, les familles, la grammaire, le budget, la graine ni la règle de verdict : données rafraîchies et fenêtres des deux côtés (2026-10-22), puis fenêtres des six rapports de densité de Planck recalculées sur les chaînes publiées et ajout du contrôle (2026-11-03), enfin fenêtre de m_W/m_Z calculée depuis les masses publiées, comme pour les autres rapports de masses (2026-11-11).

| Quantité | premier passage (2026-10-17, données de la v3.5, fenêtres d'un seul côté) | révision 1 (2026-10-24, données rafraîchies, fenêtres des deux côtés) | révision 2 (2026-11-03, rapports de densité sur les chaînes de Planck) | révision 3 (2026-11-11, données courantes : m_W/m_Z depuis les masses publiées) |
|---|---|---|---|---|
| couverture de K₇ | 32/33 | 31/33 | 31/33 | 31/33 |
| coût de description de K₇ (bits) | 395,6 | 409,2 | 408,1 | 408,1 |
| paires de Betti alternatives (dérivations publiées) : atteignent autant que K₇ | 4 159 sur 4 159 (P = 1,000) | 1 085 sur 4 159 (P = 0,261) | 1 085 sur 4 159 (P = 0,261) | 1 085 sur 4 159 (P = 0,261) |
| vocabulaires inventés (générateur de [M]) : atteignent autant que K₇ | 1 635 sur 2 000 (P = 0,818) | 1 015 sur 2 000 (P = 0,508) | 1 015 sur 2 000 (P = 0,508) | 1 015 sur 2 000 (P = 0,508) |
| paires de Betti alternatives, dérivations variantes (hors règle) : atteignent autant que K₇ | 4 160 sur 4 160 (P = 1,000) | 723 sur 4 160 (P = 0,174) | 723 sur 4 160 (P = 0,174) | 723 sur 4 160 (P = 0,174) |
| valeur p globale, issue | 1,000, effet look-elsewhere non surmonté | 0,508, effet look-elsewhere non surmonté | 0,508, effet look-elsewhere non surmonté | 0,508, effet look-elsewhere non surmonté |
| cibles atteintes par personne | α⁻¹(0) | α⁻¹(0), m_μ/m_e | α⁻¹(0), m_μ/m_e | α⁻¹(0), m_μ/m_e |

## 6. Ce que disaient les versions précédentes de cette page

Les versions précédentes de cette page présentaient les éléments suivants comme des preuves statistiques. Chacun est retiré.

- **« N° 1 parmi 3 070 396 configurations », « 0 meilleure alternative », valeur p du modèle nul < 2 × 10⁻⁵.** Ils venaient d'une recherche où les alternatives étaient notées avec les formules de K₇ et ne cherchaient pas les leurs. Les formules ayant été choisies pour (21, 77), (21, 77) gagnait par construction. Un balayage aveugle antérieur de 242 064 paires de Betti avait déjà trouvé (21, 77) sous la médiane ([Program, principe de sélection, Q-B](https://github.com/arithmon/program/blob/main/problems/selection-principle.md)).
- **« P < 5 × 10⁻⁶ parmi 192 349 configurations » (version 3.5).** Même protocole ; 1/192 349 était le plancher de l'estimateur. Retiré.
- **Probabilités de coïncidence 10⁻³⁴⁶, 10⁻¹³⁸ et 10⁻¹³³ (versions 3.3 et 3.4).** Le modèle nul uniforme traite les prédictions comme des nombres aléatoires, ce qu'aucune recherche de formules ne produit ; le modèle nul algébrique compare des formules choisies à des formules aléatoires et ne chiffre donc pas le choix. Retirées.
- **Écart moyen (0,21 %, 0,24 %, 0,39 %, 0,73 %, 0,99 % selon les versions).** Un écart moyen mesure la proximité, dont le test ci-dessus montre qu'elle n'est pas distinctive, et il masquait les relations au-delà de 2σ. Retiré ; le [bilan de validation](Validation-Summary.fr.html) donne les cinq classes à la place.
- **Facteurs de Bayes, Westfall–Young et tests hors échantillon du rapport 3.3.** Calculés sur les données de la 3.3 avec le même protocole à formules fixées, ils n'ont pas été recalculés. Retirés comme preuves.
- **« Rapport de surdétermination 2,13 » et diagnostics voisins (version 3.5).** Ils décrivent l'usage que les formules font des constantes ; ils ne distinguent pas une formule ajustée d'une formule qui ne l'est pas. Gardés en S4.3 comme description archivée.

Les scripts et rapports derrière les chiffres retirés sont conservés, sans maintenance, dans l'[archive de la version 3.3](https://github.com/Arithmon/K7/blob/main/publications/validation/legacy/v3.3/), comme trace de ce qui a été publié.

## 7. Ce qui reste

Deux choses survivent aux tests look-elsewhere, et l'article s'appuie sur elles plutôt que sur la proximité : **la rigidité sous un dictionnaire fixé** (aucune relation n'a de paramètre continu, une seule mesure peut donc la rejeter selon la règle de décision de l'article principal, §11) et **le résidu déclaré** (ce qui a été posé plutôt que dérivé est écrit, §3.3).

## 8. Reproductibilité

Le producteur, le jeu de données lu par le passage, le préenregistrement et ses trois amendements, le résultat et ceux des trois passages antérieurs sont dans [`publications/validation/v3.6/`](https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/), avec leurs empreintes et la commande pour relancer le test. Le supplément [S4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md), section S4.5, donne les entrées épinglées (commit du moteur du Sieve, empreinte de la grammaire, graine).

---

*K₇ Framework v3.6 | page générée depuis les sources de l'article par `k7_v3_6_surface_pages.py`*
