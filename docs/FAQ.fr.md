---
title: FAQ
---

# Foire aux questions

Les questions courantes sur le cadre K₇, à la version 3.6 de l'article. Là où cette page et l'[article principal](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) diffèrent, c'est l'article qui fait foi.

## Le cadre

### Qu'est-ce que le cadre K₇ ?

Une **correspondance déclarée**. Elle associe 33 paramètres sans dimension du Modèle Standard et de la cosmologie à des formes closes en les invariants d'une variété compacte K₇ de dimension sept, d'holonomie G₂ et de nombres de Betti (b₂, b₃) = (21, 77), avec une structure de jauge E₈×E₈. Par exemple, sin²θ_W reçoit b₂/(b₃ + dim G₂) = 3/13.

Elle est énoncée avec trois choses : son **dictionnaire** (vingt constantes structurelles et la grammaire dans laquelle s'écrivent les formules), son **registre des résidus** (tout ce qui a été posé plutôt que dérivé) et une **règle de décision** écrite à l'avance.

### Est-ce une dérivation des constantes du Modèle Standard ?

Non. On ne connaît aucune application géométrique qui envoie les invariants de K₇ sur les observables, et aucune règle ne fixe quelle formule est associée à quelle observable. Les versions précédentes écrivaient « dériver » là où l'opération est une attribution ; la version 3.6 retire ce mot partout. K₇ est un candidat privilégié, choisi par l'auteur, et l'article le dit.

### Y a-t-il des paramètres libres ?

Aucune relation n'a de paramètre **continûment** ajustable : un rapport d'entiers ne se retouche pas. Cela ne veut pas dire que rien n'a été choisi. Le registre des résidus (R1 à R12) énumère ce qui a été posé : la paire de Betti (21, 77), la normalisation imposée det(g) = 65/32, la combinaison κ_T⁻¹ = 61, l'unité dans laquelle l'entier 197 est lu comme phase CP, les échelles et schémas de masse des comparaisons, l'attribution des formules aux observables, et l'absence de choix entre relations incompatibles dans trois secteurs. Les versions précédentes parlaient d'un cadre sans paramètre libre ni ajustement ; cette description du choix des formules est retirée.

### La variété K₇ existe-t-elle ?

On ne le sait pas. Aucune variété G₂ compacte sans torsion de nombres de Betti (21, 77) n'est construite à ce jour, et la voie proposée dans la version 3.5 ne réalise pas cette paire ([erratum](https://github.com/Arithmon/K7/blob/main/publications/ERRATUM_v3.5.md), §9). Les 33 relations n'utilisent pas la métrique de K₇ : elles reposent sur les invariants topologiques déclarés et sur les données du groupe E₈×E₈. Les articles compagnons certifient des morceaux locaux ou conditionnels (une métrique de couture, un ansatz de col), pas un K₇ compact.

### Quelle différence avec la théorie des cordes ou la M-théorie ?

E₈×E₈ et l'holonomie G₂ apparaissent toutes deux en M-théorie, mais le cadre ne fournit aucune compactification de ce type. Son K₇ lisse ne donne pas le contenu chiral non abélien du Modèle Standard, et ses relations ne sont pas dérivées d'une théorie effective à quatre dimensions. Il utilise les structures exceptionnelles comme source d'entiers, et le dit.

### Est-ce de la physique reconnue ?

Non. C'est le travail d'un chercheur indépendant, mené avec l'aide de l'IA, qui n'est pas passé par l'évaluation d'une revue. Les articles, les données et le code sont publics pour que chacun puisse vérifier ce qui est avancé. Le cadre a été cité dans la littérature à comité de lecture ; une citation n'est pas une approbation.

## Les 33 relations

### Que compare-t-on à l'expérience ?

Trente-trois relations sans dimension : couplages de jauge, rapports de masses des leptons et des quarks, paramètres de mélange PMNS et CKM, rapports de masses des bosons et paramètres cosmologiques. La [référence des observables](wiki/Observable-Reference.fr.html) donne chaque formule, sa valeur, la mesure et son statut.

Le jeu de données contient 62 autres entrées (quantités dimensionnées lues dans une unité choisie, sorties de mécanismes avec choix de calibration, diagnostics structurels). La version 3.6 ne les compte **pas** comme prédictions ; les versions précédentes parlaient de 95 observables prédites, ce qui est retiré.

### Les 33 relations s'accordent-elles avec les données ?

Face à PDG 2026, NuFIT 6.1, Planck 2018 et CODATA 2022, toutes incertitudes à 1σ, elles se répartissent en cinq classes qui ne s'additionnent pas en un score :

| Classe | Nombre | Relations |
|---|:---:|---|
| à moins de 2σ | 23 | les autres relations |
| tension (entre 2σ et 3σ) | 2 | m_τ/m_e, Ω_c/Ω_m |
| proximité (au-delà de 3σ, rejetée comme égalité exacte) | 6 | α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t, m_W/m_Z |
| dans l'intervalle du PDG (sans incertitude) | 1 | m_s/m_d |
| profil non gaussien, octant non tranché | 1 | sin²θ₂₃ |

Les versions précédentes résumaient l'accord par un écart moyen. Ce résumé est retiré : il masquait les relations au-delà de 2σ. Le détail est dans le [bilan de validation](wiki/Validation-Summary.fr.html).

### Sont-ce 33 tests indépendants ?

Non. Trois secteurs sont surdéterminés : quatre relations leptoniques portent sur deux rapports de masses, trois relations CKM sur deux paramètres, sept relations de densité sur deux densités indépendantes. Dans chacun, les relations se contredisent en tant qu'égalités exactes : elles ne peuvent pas toutes tenir, et aucune n'est choisie après coup. Prises ensemble comme égalités exactes, les 33 sont déjà incompatibles ; chaque relation reste testable séparément.

### L'accord est-il statistiquement significatif ?

Non. Dans un test look-elsewhere préenregistré, chaque concurrent cherche ses propres formules, dans la même grammaire et avec le même budget. K₇ atteint 31 des 33 cibles ; 1 085 paires de Betti alternatives sur 4 159 et 1 015 vocabulaires inventés sur 2 000 en atteignent autant, et aucun n'en atteint plus (valeur p globale de 0,51 pour un seuil de 0,01). Un contrôle sans aucune constante de K₇ en atteint 30. La proximité avec les valeurs mesurées n'est donc pas, à elle seule, un indice en faveur de K₇.

Les probabilités de coïncidence, valeurs P et facteurs de Bayes des versions précédentes sont retirés : ils venaient de tests où les alternatives étaient notées avec les formules de K₇. Voir les [éléments statistiques](wiki/Statistical-Evidence.fr.html) ; le code et les résultats du test sont [publics](https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/).

### Quels sont les points faibles ?

- Six relations sont rejetées comme égalités exactes et gardées seulement comme proximités numériques, dont α⁻¹ et sin²θ_W.
- sin²θ₂₃ = 6/11 se trouve dans le second octant alors que l'ajustement global préfère le premier.
- L'accord n'est pas distinctif (question précédente).
- La paire de Betti, les formules et la normalisation sont choisies, non dérivées ; cinq voies pour dériver (21, 77) ont été fermées sans succès.
- La variété n'est pas construite, et aucun mécanisme ne mène d'elle au Modèle Standard chiral.

### Et δ_CP = 197° ?

La structure produit l'entier 197 = 7·14 + 99. Le lire comme un angle en degrés est un choix du dictionnaire, consigné au registre des résidus et compté dans le test look-elsewhere ; lu en radians ou en grades, le même entier donne d'autres phases. NuFIT 6.1 donne δ_CP = 212 (+26/−36)°, de sorte que la lecture en degrés est aujourd'hui dans la bande à 1σ. Une confirmation montrerait que cette assignation s'accorde avec le monde, pas que la structure l'impose.

### Et les quantités dimensionnées, comme les masses ?

Les masses et les échelles absolues ne figurent que parmi les 62 entrées non comptées comme prédictions. Plusieurs sont des nombres structurels lus en MeV ; lire un nombre dans une unité est une assignation du même genre que lire 197 en degrés, avec un espace d'alternatives bien plus vaste.

## Les tests

### Le cadre peut-il être réfuté ?

Les relations, une à une, oui. Chacune est énoncée comme une égalité exacte, sans incertitude théorique, et la règle est écrite à l'avance, sans clause de réparation : une relation est rejetée quand sa série de référence (PDG, NuFIT, Planck, CODATA) exclut sa valeur à 3σ, et elle n'est pas sauvée en changeant sa formule, son unité, son échelle ou son jeu de données.

| Relation | Valeur | Rejetée quand | Où |
|---|---|---|---|
| δ_CP | 197° | un ajustement global dont l'intervalle à 3σ exclut 197° ; l'assignation d'unité est rejetée avec elle | DUNE, Hyper-Kamiokande |
| sin²θ₂₃ | 6/11 | un ajustement global dont l'intervalle à 3σ exclut 6/11, dans l'un ou l'autre octant | DUNE, Hyper-Kamiokande |
| sin²θ₁₂ | 4/13 | un ajustement global dont l'intervalle à 3σ exclut 4/13 | JUNO (première mesure 0,3092 ± 0,0087 ; environ quatre fois plus serré que l'ajustement global actuel après six ans) |
| m_τ/m_e et Q_Koide | 1776,74 et 1776,97 MeV pour m_τ | une valeur de m_τ dont l'intervalle à 3σ exclut la valeur | Belle II, BES III |
| N_gen | 3 | une quatrième génération séquentielle | LHC, FCC |
| m_s/m_d | 20 | une détermination sur réseau, avec incertitude, dont l'intervalle à 3σ exclut 20 | QCD sur réseau |

Un rejet rejette la relation et l'assignation qui l'a produite. Il ne rejette pas à lui seul le programme, dont les autres relations tiennent ou tombent chacune pour son compte ; l'article le dit maintenant, pour que cela ne puisse pas être dit plus tard comme une réparation. Le programme exploratoire au sens large n'a, à ce jour, aucun critère unique de réfutation.

### Qu'est-ce qui compterait en sa faveur ?

Moins qu'on pourrait l'espérer. La proximité n'étant pas distinctive, de nouveaux accords au pour cent ajoutent peu. Ce qui changerait le tableau est d'une autre nature : une construction de la variété, un mécanisme qui sélectionne (21, 77), une règle qui attribue les formules aux observables, ou une relation qui survit à une mesure assez précise pour départager des vocabulaires concurrents.

### Des mesures contredisent-elles déjà une relation ?

Deux résultats contradictoires, hors des séries de référence, sont rapportés à côté de leur classe. h = 167/248 s'accorde avec Planck et est exclu par l'échelle des distances SH0ES à 5,5σ. Les relations de densité s'accordent avec Planck et sont mises sous tension par les oscillations acoustiques de baryons de DESI (deuxième livraison de données) : DESI seul place Ω_Λ/Ω_m = 113/52, Ω_m/Ω_Λ = 28/61 et Ω_DE à environ 2σ ; DESI combiné au fond diffus cosmologique les place à −3,3σ, +3,4σ et −3,1σ, et h à −3,0σ. Tant que les méthodes divergent, le statut est donné des deux façons, et aucun des deux accords ne vaut confirmation.

## Mathématiques et vérification

### Pourquoi E₈×E₈ et l'holonomie G₂ ?

Ce sont des structures dont l'intérêt ne doit rien aux constantes du Modèle Standard : les octonions, la classification des groupes d'holonomie par Berger, les algèbres de Lie exceptionnelles, et leur rôle en M-théorie. Cela répond à la question de savoir si la famille mérite d'être explorée. Cela ne dit pas pourquoi ce membre-ci : ces exigences ne sélectionnent ni (21, 77), ni les formules, ni la normalisation.

### Que prouve la formalisation en Lean 4 ?

L'arithmétique. Étant donné les entiers déclarés, chacune des 33 formes closes s'évalue au nombre annoncé (réunies dans `relations_v36_certified` ; 156 fichiers, 14 axiomes, aucun `sorry`). Elle n'établit ni l'existence de K₇, ni l'interprétation physique d'une relation, ni le choix des attributions, ni la cohérence des relations prises ensemble. Une formule vérifiée par machine n'est pas pour autant la bonne formule.

### Pourquoi ces nombres et pas d'autres ?

C'est la question de la sélection, et elle est ouverte. La paire (21, 77) est une entrée de construction, au même rang que le postulat de l'holonomie G₂ : fixée avant que les relations soient gelées et utilisée de façon rigide par toutes, mais choisie, non sélectionnée. Une observation numérique subsiste, b₂ + b₃ = 98 = dim(K₇) · dim(G₂), tenue pour une cible et non pour un théorème.

### Cela veut-il dire que la physique n'est « que des mathématiques » ?

Le cadre se lit comme une proposition structurelle : on demande à la structure de porter un poids prédictif, sans engagement ontologique supplémentaire. Les lectures où géométrie et information sont deux aspects d'une même chose ont motivé le travail à l'origine ; les relations ne les exigent pas et ne les étayent pas.

## Pratique

### Qu'est-ce qui a changé avec la version 3.6 ?

Elle retire plusieurs affirmations des versions précédentes : que les relations sont dérivées de la géométrie, qu'elles ne peuvent pas être ajustées, que 95 observables sont prédites, qu'une probabilité de coïncidence ou une valeur P mesure le caractère distinctif du cadre, que 197° est une prédiction de pure géométrie, que le nombre de générations vient d'un théorème de l'indice. Ce qui reste est plus modeste et se vérifie. La liste complète est dans le [journal des changements](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_CHANGELOG.md).

### Par où commencer ?

- **Sans équations** : [K₇ pour tout le monde](wiki/GIFT-for-Everyone.fr.html).
- **Physicien** : l'[article principal](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md), sections 3, 4, 7 et 11.
- **Mathématicien** : le supplément S1 et les articles compagnons sur la métrique de couture.
- **Les chiffres** : [référence des observables](wiki/Observable-Reference.fr.html), [bilan de validation](wiki/Validation-Summary.fr.html), [éléments statistiques](wiki/Statistical-Evidence.fr.html).

### Comment citer ?

L'article du cadre est archivé sur Zenodo ; le DOI concept [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489) renvoie toujours à la dernière version. Le [guide de citation](wiki/Citation-Guide.html) (en anglais) donne les formats.

### Puis-je m'en servir dans mes recherches, ou contribuer ?

Oui : le dépôt est sous licence MIT. Les corrections, les nouvelles comparaisons de données et les signalements d'erreurs sont bienvenus par les [tickets GitHub](https://github.com/Arithmon/K7/issues) ; voir `CONTRIBUTING.md`.

---

*K₇ Framework v3.6*
