---
title: "K₇ : Résumé"
---

# K₇ : une correspondance, et les conditions de son échec

*Un résumé technique pour les lecteurs curieux de physique, à la version 3.6*

---

## Le problème, dit simplement

Le Modèle Standard de la physique des particules atteint une précision qu'aucune autre théorie scientifique n'a égalée. Il décrit toutes les interactions fondamentales connues hormis la gravité, avec un accord expérimental qui va parfois jusqu'à douze décimales.

Il contient pourtant une vingtaine de paramètres libres, des nombres que la théorie ne calcule pas et qu'il faut mesurer avant de pouvoir s'en servir : les masses des leptons chargés et des six quarks, les paramètres de la matrice CKM, les trois constantes de couplage, la masse du Higgs et sa valeur moyenne dans le vide. Les masses et le mélange des neutrinos en ajoutent d'autres.

S'y ajoutent des énigmes anciennes. Pourquoi exactement trois générations de matière ? Pourquoi les masses des leptons chargés suivent-elles de si près la relation de Koide *Q* = 2/3, remarquée en 1981 et jamais expliquée ? Pourquoi le rapport entre matière noire et matière baryonique est-il proche d'un rationnel simple ?

K₇ (*anciennement Geometric Information Field Theory*) est une tentative de regarder ces nombres autrement. Il demande : et s'ils pouvaient s'écrire comme des formes closes en les invariants d'une seule structure géométrique ? Et, puisque écrire de telles formes se révèle facile, il pose une seconde question avec le même sérieux : que faudrait-il pour qu'une telle correspondance signifie quelque chose ?

## La proposition

En une phrase : 33 paramètres sans dimension du Modèle Standard et de la cosmologie sont associés à des combinaisons algébriques des invariants topologiques d'une variété compacte de dimension sept à holonomie exceptionnelle, avec une structure de jauge E₈ × E₈.

Une **variété de dimension sept** est un espace courbe à sept dimensions. L'**holonomie** mesure la façon dont un vecteur change quand on le transporte le long d'une boucle fermée de cet espace. Pour la plupart des variétés, ce changement peut être n'importe quelle rotation. Certaines ont une holonomie restreinte à un sous-groupe, et en dimension sept il en existe un exceptionnel, **G₂**, de dimension 14, le groupe des automorphismes des octonions. Les variétés à holonomie G₂ sont rares et difficiles à construire.

Les **invariants topologiques** d'une telle variété sont des entiers qui caractérisent sa forme indépendamment de sa métrique. Les plus importants sont les **nombres de Betti** *b₂* et *b₃*, qui comptent les 2-formes et les 3-formes harmoniques que l'espace peut porter. Ce sont des nombres entiers : ils ne varient pas continûment.

Le cadre pose une variété *K₇* avec (*b₂*, *b₃*) = (21, 77), accompagnée de E₈ × E₈, de dimension 496. À partir de ces entiers et de quelques autres qui leur sont liés (vingt constantes structurelles en tout), il écrit des formules comme

- sin²θ_W = *b₂* / (*b₃* + dim G₂) = 3/13,
- *Q*_Koide = dim G₂ / *b₂* = 2/3,
- *m*_τ / *m*_e = 7 + 10 × 248 + 10 × 99 = 3477.

**E₈** est le plus grand groupe de Lie exceptionnel. Le cadre ne cherche pas à plonger les particules du Modèle Standard dans E₈, approche dont Distler et Garibaldi ont montré l'impossibilité en 2010. Il utilise E₈ × E₈ comme source d'entiers issus de la théorie des groupes, ce qui évite cette obstruction et signifie aussi qu'il ne dit rien de l'origine des fermions.

## Une correspondance, pas une dérivation

C'est le point sur lequel la version 3.6 s'écarte le plus de ce qui précédait, et il vaut d'être dit sans détour.

**On ne connaît aucune application géométrique qui envoie les invariants de K₇ sur les observables.** Les formules sont *attribuées* : rien dans la géométrie ne dit que sin²θ_W doit valoir *b₂* / (*b₃* + dim G₂) plutôt qu'un autre rapport. Les versions précédentes écrivaient « dériver » pour cette opération. La version 3.6 retire le mot.

**Aucune règle ne fixe quelle formule va avec quelle observable.** La grammaire et la liste des observables ont été gelées après que les formules avaient été trouvées.

**La variété n'est pas construite.** Aucune variété G₂ compacte sans torsion de nombres de Betti (21, 77) n'est connue à ce jour, et la voie proposée dans la version 3.5 n'en produit pas. Les relations n'utilisent que les entiers déclarés, pas une métrique.

Ce que fait l'article, c'est rendre la correspondance vérifiable. Il donne le **dictionnaire** complet. Il tient un **registre des résidus**, où figure tout ce qui a été posé plutôt que dérivé : la paire (21, 77), une normalisation imposée det(g) = 65/32, une combinaison κ_T⁻¹ = 61, l'unité dans laquelle un entier est lu comme phase CP, les échelles des comparaisons, les attributions elles-mêmes. Et il écrit une **règle de décision** sans clause de réparation.

K₇ est, dans les termes de l'article, un *candidat privilégié* : le membre d'une famille bien motivée, désigné par l'auteur pour des raisons qui sont les siennes et qui sont déclarées comme telles. Présenter un candidat privilégié comme une unicité démontrée, c'est ce que faisaient les versions précédentes, et ce que celle-ci cesse de faire.

## Comment le cadre s'est construit

La première version, en 2025, comportait quatre paramètres géométriques ajustables, réglés pour reproduire environ 22 observables. Une deuxième les a ramenés à trois quantités, chacune un rapport d'entiers topologiques. La structure actuelle n'a aucun paramètre continûment ajustable : les relations sont des rapports d'entiers, ou utilisent une opération supplémentaire déclarée.

Les versions précédentes de ce résumé lisaient cette trajectoire (quatre, trois, zéro paramètres, avec davantage d'observables couvertes à chaque fois) comme le signe d'une compression et non d'un ajustement. Cette lecture ne tient pas. Supprimer les paramètres continus tout en choisissant les formules dans une grammaire riche déplace la liberté ; cela ne la supprime pas. La liberté se trouve désormais dans le choix des formules, du vocabulaire et de la paire de Betti, c'est-à-dire exactement ce que le registre des résidus consigne et que le test look-elsewhere ci-dessous chiffre.

Ce que donne l'absence de paramètres continus, c'est la **rigidité** : un rapport d'entiers ne se retouche pas, une seule mesure précise peut donc rejeter une relation. La rigidité expose un cadre à la réfutation. Elle ne le certifie pas : une structure exceptionnelle est rigide, qu'elle ait été dérivée ou choisie pour les valeurs qu'elle donne.

## Où en sont les 33 relations

Face aux données les plus récentes (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022), avec une seule convention pour toutes les incertitudes, les relations se répartissent en cinq classes, qui ne s'additionnent pas en un score :

- **23 sont à moins de deux écarts-types** de la mesure. Parmi elles *Q*_Koide = 2/3, α_s = √2/12, la phase CP lue comme 197°, et la plupart des rapports de quarks, de mélange et de cosmologie.
- **2 sont en tension**, entre 2σ et 3σ : *m*_τ/*m*_e = 3477 et Ω_c/Ω_m = 27/32.
- **6 sont rejetées comme égalités exactes** à plus de 3σ et gardées seulement comme proximités numériques : α⁻¹, sin²θ_W = 3/13, *m*_μ/*m*_e, *m*_μ/*m*_τ, *m*_b/*m*_t et *m*_W/*m*_Z = 37/42. Ces quantités sont mesurées si précisément qu'une formule à 0,2 % se trouve à de nombreux écarts-types.
- **1 tombe dans un intervalle** que le PDG donne sans incertitude : *m*_s/*m*_d = 20.
- **1 se trouve dans l'autre octant** : sin²θ₂₃ = 6/11, alors que l'ajustement global préfère le premier octant ; la valeur est dans son intervalle à 3σ.

Ce ne sont pas non plus **33 tests indépendants**. Dans trois secteurs il y a plus de relations que de quantités : quatre relations leptoniques pour deux rapports de masses, trois relations CKM pour deux paramètres, sept relations de densité pour deux densités. Dans chaque secteur, les relations se contredisent en tant qu'égalités exactes. Chaque formule est calculée correctement, et elles ne peuvent pas toutes être vraies ensemble.

La plupart des 23 ne sont testées que faiblement : là où les incertitudes expérimentales sont de l'ordre du pour cent, un accord au pour cent est ce qu'un vocabulaire riche atteint facilement.

## Pourquoi l'hypothèse de la coïncidence ne peut pas être écartée

Devant des formules aussi proches des données, la question est inévitable : est-ce le produit d'une pêche au hasard dans un océan de combinaisons algébriques ?

Les versions précédentes de ce résumé répondaient non, et citaient des tests statistiques : un rang parmi trois millions de configurations, une valeur P, des facteurs de Bayes, des validations par omission. Tous sont retirés. Ils avaient un défaut commun. Les alternatives étaient notées avec les formules de K₇, qui avaient été choisies pour (21, 77) ; aucune n'avait le droit de chercher les siennes. Avec un tel protocole, (21, 77) gagne par construction.

La version 3.6 les remplace par un test préenregistré où **chaque concurrent cherche ses propres formules**, dans la même grammaire, avec le même budget et la même liberté d'attribution. Le résultat :

- K₇ atteint 31 des 33 cibles.
- 1 085 paires de Betti alternatives sur 4 159 en atteignent autant, et 1 015 vocabulaires inventés sur 2 000 aussi. Aucun n'en atteint plus.
- Un témoin sans aucune constante de K₇, qui n'utilise que les symboles universels de la grammaire, en atteint 30.

Le verdict préenregistré : l'effet look-elsewhere n'est pas surmonté, et la valeur P est retirée du texte. **La proximité avec les valeurs mesurées n'est pas, à elle seule, un indice en faveur de K₇.** Ce n'est pas non plus une réfutation : le test dit que le score ne discrimine pas, pas que le cadre est faux.

Ce qui survit au test est modeste et réel : la rigidité sous un dictionnaire fixé à l'avance, et la trace écrite de ce qui a été choisi.

## Comment une relation peut échouer

Les relations sont énoncées comme des égalités exactes, sans incertitude théorique. Une relation est rejetée quand sa série de données de référence exclut sa valeur à 3σ. Ni la formule, ni l'unité, ni l'échelle, ni le jeu de données ne sont changés ensuite pour la sauver.

**La phase CP.** La structure produit l'entier 197. Le lire en degrés est un choix, déclaré comme tel. DUNE et Hyper-Kamiokande mesureront δ_CP ; un ajustement global dont l'intervalle à 3σ exclut 197° rejette la relation, et le choix d'unité avec elle. Aujourd'hui l'ajustement donne 212 (+26/−36)°.

**L'octant de θ₂₃.** Un ajustement dont l'intervalle à 3σ exclut 6/11 rejette cette relation.

**L'angle solaire.** La première mesure de JUNO donne sin²θ₁₂ = 0,3092 ± 0,0087, pour 4/13 = 0,3077. Après six ans, son incertitude devrait être environ quatre fois plus petite que celle de l'ajustement global actuel, et une exclusion de 4/13 à 3σ rejette la relation.

**La masse du tau.** Deux relations donnent 1776,74 et 1776,97 MeV ; une mesure assez précise doit en rejeter au moins une.

**Une quatrième génération** rejetterait l'identité entière *N*_gen = 3.

Un rejet rejette une relation et l'assignation qui la porte. Il ne rejette pas à lui seul le programme, et l'article le dit à l'avance pour que cela ne puisse pas être dit plus tard comme une réparation. À l'inverse, une confirmation montrerait qu'une assignation s'accorde avec le monde, pas que la structure l'impose. Deux résultats hors des séries de référence contredisent déjà une relation (la constante de Hubble de SH0ES, et les oscillations acoustiques de baryons de DESI pour les rapports de densité) et sont rapportés à côté d'elle.

## Ce que K₇ n'est pas

K₇ n'est pas une théorie du tout. Il ne traite ni la gravité quantique ni le problème de la mesure.

K₇ n'est pas une dérivation du Modèle Standard. Sa variété lisse ne donne pas le contenu chiral non abélien du Modèle Standard, et ses relations ne viennent pas d'une théorie effective à quatre dimensions.

K₇ n'est pas une cosmogonie. Il ne propose aucun mécanisme de sélection de la variété. Cinq voies pour dériver (21, 77) ont été examinées et fermées sans succès ; il reste une observation numérique, *b₂* + *b₃* = 98 = 7 × 14, tenue pour une cible et non pour un théorème.

K₇ ne dépend d'aucune lecture du mot *information*. Les relations tiennent ou tombent indépendamment de ce qu'est, au fond, l'« information ». La lignée qui a motivé le travail (le « it from bit » de Wheeler, la borne de Bekenstein, la dérivation thermodynamique des équations d'Einstein par Jacobson, le programme holographique) rend l'idée d'un lien entre géométrie et information moins exotique qu'il n'y paraît ; les relations ne l'exigent pas et ne l'étayent pas. Un essai à part en discute ([*Gift from Bit*](https://arithmon.substack.com/p/gift-from-bit)).

## Les questions ouvertes

- **Existence.** Aucune variété G₂ compacte sans torsion de nombres (21, 77) n'est construite.
- **Physique.** Aucun mécanisme ne mène d'un K₇ lisse au Modèle Standard chiral.
- **Sélection.** Rien ne sélectionne (21, 77) ; la paire est choisie.
- **Attribution.** Aucune règle n'attribue les formules aux observables.
- **Dépendances.** L'audit des dépendances entre les 33 relations n'est pas terminé : aucun compte de tests indépendants n'est donné.

## Ce qui reste à voir

L'article ne prétend pas que le cadre est juste. Ce peut être une véritable intuition structurelle, l'approximation d'une telle intuition, ou une coïncidence élaborée. Le but de la version 3.6 est que l'on puisse savoir laquelle, et que le lecteur voie, à chaque étape, ce qui a été dérivé, ce qui a été supposé, et ce qui le ferait tomber.

C'est une affirmation plus modeste que celle que cette page portait. Elle se vérifie.

---

*Pour l'énoncé complet, voir l'[article principal](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) et ses suppléments ; le code et les résultats du test look-elsewhere sont [publics](https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/). La dernière version déposée est toujours au DOI concept Zenodo [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489).*
