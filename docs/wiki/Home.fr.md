---
title: "Accueil"
layout: default
---

# Le cadre K₇

**Une correspondance déclarée entre la topologie G₂ et 33 paramètres sans dimension, énoncée avec son dictionnaire, son résidu et une règle de décision.**

Le cadre K₇ associe 33 paramètres sans dimension du Modèle Standard et de la cosmologie à des formes closes en les invariants d'une variété K₇ de dimension sept, d'holonomie G₂ et de nombres de Betti (b₂, b₃) = (21, 77), avec E₈×E₈. La version 3.6 le présente comme une correspondance et non comme une dérivation : on ne connaît aucune application géométrique qui envoie les invariants sur les observables, et aucune règle ne fixe quelle formule est associée à quelle observable. K₇ est un candidat privilégié, choisi par l'auteur, et le papier le dit.

---

## En bref

| | |
|----------|-------|
| **Ce qui est proposé** | 33 relations sans paramètre continûment ajustable, écrites avec vingt constantes structurelles déclarées |
| **Ce qui est posé, non dérivé** | le registre des résidus R1–R12 : la paire de Betti (21, 77), la normalisation imposée det(g) = 65/32, κ_T⁻¹ = 61, l'unité dans laquelle 197 est lu comme phase CP, les échelles de comparaison, l'attribution des formules |
| **Face aux données actuelles** | 23 à moins de 2σ, 3 en tension, 5 rejetées comme égalités exactes et gardées comme proximités, 1 dans un intervalle du PDG, 1 dont l'octant n'est pas tranché (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022) |
| **Effet look-elsewhere** | non surmonté : quand chaque concurrent cherche ses propres formules, 1 085 paires de Betti sur 4 159 et 1 015 vocabulaires inventés sur 2 000 atteignent autant de cibles que K₇ (P_global = 0,51) |
| **Vérification Lean 4** | l'arithmétique des 33 relations (`relations_v36_certified`), 156 fichiers, 14 axiomes, aucun `sorry` ; elle vérifie l'arithmétique énoncée, pas le contenu physique |
| **Existence de K₇** | ouverte : aucune variété G₂ compacte sans torsion de nombres (21, 77) n'est construite à ce jour |
| **Autres entrées du jeu de données** | 62 extractions conditionnelles et diagnostics, gardés pour la traçabilité et non comptés comme prédictions |

---

## Liens rapides

| | |
|---|---|
| **Nouveau ici ?** | [Pour commencer](Getting-Started.fr.html) : choisissez votre parcours |
| **Lire les articles** | [Article principal](Paper-Main-Framework.html) ([Métrique G₂ explicite](Paper-Explicit-G2-Metric.html)) [Géométrie spectrale](Paper-Spectral-Geometry.html) |
| **Parcourir les relations** | [Référence des observables](Observable-Reference.fr.html) : les 33 relations avec formules, données et statut |
| **Est-ce distinctif ?** | [Éléments statistiques](Statistical-Evidence.fr.html) : le test look-elsewhere |
| **Vérifier les preuves** | [Formalisation Lean](Lean-Formalization.html) |

---

## Les 33 relations en cinq classes

Les classes ne s'additionnent pas en un score unique (article principal, §4.2).

| Classe | Nombre | Relations |
|-------|:-----:|-----------|
| à moins de 2σ | 23 | les autres relations |
| tension (entre 2σ et 3σ) | 3 | m_τ/m_e, m_W/m_Z, Ω_c/Ω_m |
| proximité (au-delà de 3σ, rejetée comme égalité exacte) | 5 | α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t (dans le schéma de masse déclaré) |
| dans l'intervalle du PDG (sans incertitude) | 1 | m_s/m_d |
| profil non gaussien, octant non tranché | 1 | sin²θ₂₃ |

Un échantillon, une ou deux par classe :

| Observable | Formule K₇ | Valeur K₇ | Mesure | Écart normalisé | Statut |
|------------|-------------|-------|------|------|------|
| Q_Koide | dim(G₂)/b₂ = 2/3 | 0,666667 | 0,6666645(51) | +0,4σ | à moins de 2σ |
| α_s(M_Z) | √2/(dim(G₂) − p₂) = √2/12 | 0,117851 | 0,1180(9) | −0,2σ | à moins de 2σ |
| δ_CP | 7·14 + 99 = 197, lu en degrés | 197° | 212 (+26/−36)° | −0,4σ | à moins de 2σ ; assignation d'unité |
| Ω_DE | ln 2 · 98/99 | 0,686146 | 0,6847(73) | +0,2σ | à moins de 2σ |
| m_τ/m_e | 7 + 10·248 + 10·99 | 3477 | 3477,37(18) | −2,1σ | tension |
| m_W/m_Z | 37/42 | 0,880952 | 0,88136(15) | −2,7σ | tension |
| sin²θ_W(M_Z) | 21/91 = 3/13 | 0,230769 | 0,23122(6) | −7,5σ | proximité |
| m_μ/m_τ | 10/168 | 0,059524 | 0,0594612(30) | +20,8σ | proximité |
| m_s/m_d | 4 × 5 = 20 | 20 | 17–22 (intervalle) | s.o. | dans l'intervalle du PDG |
| sin²θ₂₃ (PMNS) | 6/11 | 0,545455 | 0,470 (+17/−14) | +4,4σ* | tension : second octant, dans l'intervalle à 3σ de NuFIT (*le profil n'est pas gaussien, l'écart gaussien la surestime) |

**Ce ne sont pas 33 tests indépendants.** Trois secteurs sont surdéterminés, et dans chacun les relations se contredisent en tant qu'égalités exactes : quatre relations leptoniques pour deux rapports de masses, trois relations CKM pour deux paramètres de Wolfenstein, sept relations de densité pour deux densités indépendantes. Aucune n'est choisie après coup.

## Règle de décision

Les relations sont énoncées comme des égalités exactes. Une relation est rejetée quand sa série de référence (PDG, NuFIT, Planck, CODATA) exclut sa valeur à 3σ ; ni la formule, ni l'unité, ni l'échelle, ni le jeu de données ne sont changés ensuite pour la sauver (article principal, §11).

| # | Relation | Valeur | Rejetée quand | Où |
|---|----------|-------|---------------|-------|
| D1 | δ_CP, la phase 2π·197/360 | 197° | un ajustement global dont l'intervalle à 3σ exclut 197° ; l'assignation d'unité est rejetée avec elle | DUNE, Hyper-Kamiokande |
| D2 | sin²θ₂₃ | 6/11 | un ajustement global dont l'intervalle à 3σ exclut 6/11, dans l'un ou l'autre octant | DUNE, Hyper-Kamiokande |
| D3 | m_τ/m_e et Q_Koide | 1776,74 et 1776,97 MeV pour m_τ | une valeur de m_τ dont l'intervalle à 3σ exclut la valeur, chaque relation séparément | Belle II, BES III |
| D4 | N_gen | 3 | une quatrième génération séquentielle | LHC, FCC |
| D5 | m_s/m_d | 20 | une détermination sur réseau, avec incertitude, dont l'intervalle à 3σ exclut 20 | QCD sur réseau |

Un rejet rejette la relation et l'assignation qui l'a produite, pas le programme à lui seul. Une confirmation montrerait qu'une assignation s'accorde avec le monde, pas que la structure l'impose.

## Ce que la version 3.6 retire

Les versions précédentes de ce site disaient que les relations sont dérivées de la géométrie, que le cadre n'a aucun paramètre libre et ne peut pas être ajusté, qu'il prédit 95 observables avec un faible écart moyen, et qu'une probabilité de coïncidence ou une valeur P mesurait son caractère distinctif. La version 3.6 retire chacune de ces affirmations. La liste complète est dans l'article principal (§12.1) et dans le [journal des changements](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_CHANGELOG.md).

---

## Vulgarisation

Une écriture accessible sur les idées derrière K₇ vit sur le [blog Substack](https://arithmon.substack.com/) (en anglais), en trois pistes : [la série](Blog-Index.fr.html#series) (la physique par les jeux auxquels vous avez déjà joué), [les idées](Blog-Index.fr.html#ideas) (pourquoi les constantes ne sont peut-être pas arbitraires) et [l'histoire](Blog-Index.fr.html#story) (un chercheur indépendant, une IA, et un an de recherche non-orthodoxe). Les traductions FR sont sur ce wiki ; la liste complète est dans l'[index du blog](Blog-Index.fr.html). Dernier paru : *[Peut-on entendre la forme d'un ballon ?](Blog-Can-You-Hear-The-Shape-Of-A-Balloon.fr.html)*, une formule de collège démontée, et la symétrie comme information économisée.

---

## Structure

Ce wiki regroupe la documentation de K₇ à travers trois dépôts :

- **[Arithmon/K7](https://github.com/Arithmon/K7)** : documentation théorique, articles, vulgarisation
- **[Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean)** : preuves Lean 4, paquet Python, blueprint
- **Dépôts Zenodo** : données archivées avec DOI

Parcourez la barre latérale pour la navigation complète, ou consultez le [plan du site](Site-Map.html) pour un index complet.

---

*K₇ Framework v3.6 | [GitHub](https://github.com/Arithmon/K7) | [Core](https://github.com/Arithmon/K7-Lean) | [Blueprint](https://arithmon.github.io/K7-Lean/) | [Zenodo (Article A)](https://doi.org/10.5281/zenodo.19892350) · [Article B](https://doi.org/10.5281/zenodo.19893371) · [Article C](https://doi.org/10.5281/zenodo.19708916) | Licence MIT*
