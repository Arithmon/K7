#!/usr/bin/env python3
"""k7_v3_6_surface_prose.py -- prose des pages bilingues de K7 (FAQ), v3.6.

Importé par k7_v3_6_surface_pages.py. Une seule source par langue pour les
deux copies de la FAQ (docs/FAQ*.md et docs/wiki/FAQ*.md) : seul le préfixe
des liens vers le wiki change ({w} = "" dans le wiki, "wiki/" dans docs/).
Les chiffres sont ceux de physics_main.md (§3.3, §4.2, §7.2, §8, §11) ;
k7_v3_6_surfaces_lint.py contrôle les classes contre observables.json.
"""
import io
import sys

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

GH = "https://github.com/Arithmon/K7/blob/main/"
MAIN = GH + "publications/papers/markdown/k7_framework_3_6_main.md"
CHLOG = GH + "publications/papers/markdown/k7_framework_3_6_CHANGELOG.md"
ERR = GH + "publications/ERRATUM_v3.5.md"
LEE = GH + "publications/validation/v3.6/"
CONCEPT = "https://doi.org/10.5281/zenodo.16891489"

FAQ_EN = """# Frequently Asked Questions

Common questions about the K₇ framework, as of version 3.6 of the framework paper. Where this page and the [main paper]({main}) differ, the paper holds.

## The framework

### What is the K₇ framework?

A **declared correspondence**. It assigns 33 dimensionless parameters of the Standard Model and of cosmology to closed forms in the invariants of a compact seven-dimensional manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with an E₈×E₈ gauge structure. For example, sin²θ_W is assigned b₂/(b₃ + dim G₂) = 3/13.

It is stated with three things: its **dictionary** (twenty structural constants and the grammar in which formulas are written), its **residue register** (everything that was set rather than derived) and a **decision rule** written in advance.

### Is it a derivation of the Standard Model's constants?

No. No geometric map is known that sends the invariants of K₇ to the observables, and no rule fixes which formula is assigned to which observable. Earlier versions wrote "derive" where the operation is an assignment; version 3.6 withdraws that wording throughout. K₇ is a privileged candidate chosen by the author, and the paper says so.

### Does it have free parameters?

No relation has a **continuously** adjustable parameter: an integer ratio cannot be nudged. That is not the same as having nothing chosen. The residue register (R1 to R12) lists what was set: the Betti pair (21, 77), the imposed normalization det(g) = 65/32, the combination κ_T⁻¹ = 61, the unit in which the integer 197 is read as a CP phase, the scales and mass schemes of the comparisons, the assignment of formulas to observables, and the absence of a choice among incompatible relations in three sectors. Earlier versions described this as a framework with no free parameter and no fitting; that description of the formula choice is withdrawn.

### Does the manifold K₇ exist?

It is not known. No compact torsion-free G₂ manifold with Betti numbers (21, 77) is currently constructed, and the route proposed in version 3.5 does not realise the pair ([erratum]({err}), §9). The 33 relations do not use the metric of K₇: they rest on the declared topological invariants and on the E₈×E₈ group data. The companion papers certify local or conditional pieces (a seam metric, a neck ansatz), not a compact K₇.

### How is this different from string theory or M-theory?

E₈×E₈ and G₂ holonomy both appear in M-theory, but the framework does not supply a compactification of either kind. Its smooth K₇ does not yield the chiral non-abelian content of the Standard Model, and its relations are not derived from a four-dimensional effective theory. It uses the exceptional structures as a source of integers and says so.

### Is this mainstream physics?

No. It is the work of an independent researcher, developed with AI assistance, and it has not been through journal peer review. The papers, the data and the code are public so that the claims can be checked by anyone. The framework has been cited in the peer-reviewed literature; a citation is not an endorsement.

## The 33 relations

### What does the framework compare with experiment?

Thirty-three dimensionless relations: gauge couplings, lepton and quark mass ratios, PMNS and CKM mixing parameters, boson mass ratios and cosmological parameters. The [Observable Reference]({w}Observable-Reference.html) gives each formula, its value, the measurement and its status.

The dataset holds 62 further entries (dimensionful quantities read in a chosen unit, outputs of mechanisms with calibration choices, structural diagnostics). Version 3.6 does **not** count them as predictions; earlier versions spoke of 95 predicted observables, which is withdrawn.

### How well do the 33 relations agree with the data?

Against PDG 2026, NuFIT 6.1, Planck 2018 and CODATA 2022, with all uncertainties at 1σ, they fall into five classes that are not added into one score:

| Class | Count | Relations |
|---|:---:|---|
| within 2σ | 23 | the remaining relations |
| tension (between 2σ and 3σ) | 2 | m_τ/m_e, Ω_c/Ω_m |
| proximity (beyond 3σ, rejected as an exact equality) | 6 | α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t, m_W/m_Z |
| inside the PDG range (no uncertainty given) | 1 | m_s/m_d |
| non-Gaussian profile, octant unresolved | 1 | sin²θ₂₃ |

Earlier versions summarised the agreement by a mean deviation. That summary is withdrawn: it hid the relations outside 2σ. Details are in the [Validation Summary]({w}Validation-Summary.html).

### Are these 33 independent tests?

No. Three sectors are overdetermined: four lepton relations bear on two mass ratios, three CKM relations on two parameters, seven density relations on two independent densities. In each, the relations disagree with one another as exact equalities, so they cannot all hold, and none is selected after the fact. Taken jointly as exact equalities, the 33 are already incompatible; individual relations remain testable.

### Is the agreement statistically significant?

No. In a preregistered look-elsewhere test, every competitor searches for its own formulas in the same grammar and with the same budget. K₇ reaches 31 of the 33 targets; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many, and none reaches more (the preregistered threshold is not met, so no p-value is reported). A control with no K₇ constant reaches 30. Closeness to the measured values is therefore not, by itself, evidence for K₇.

The coincidence probabilities, P-values and Bayes factors of earlier versions are withdrawn: they came from tests in which the alternatives were scored with K₇'s own formulas. See [Statistical Evidence]({w}Statistical-Evidence.html); the code and results of the test are [public]({lee}).

### What are the weakest points?

- Six relations are rejected as exact equalities and kept only as numerical proximities, among them α⁻¹ and sin²θ_W.
- sin²θ₂₃ = 6/11 sits in the second octant while the global fit prefers the first.
- The agreement is not distinctive (previous question).
- The Betti pair, the formulas and the normalization are chosen, not derived; five routes to deriving (21, 77) have been closed without success.
- The manifold is not constructed, and no mechanism leads from it to the chiral Standard Model.

### What about δ_CP = 197°?

The structure produces the integer 197 = 7·14 + 99. Reading it as an angle in degrees is a choice of the dictionary, recorded in the residue register and counted in the look-elsewhere test; read in radians or grads, the same integer gives other phases. NuFIT 6.1 gives δ_CP = 212 (+26/−36)°, so the reading in degrees lies inside the 1σ band today. A confirmation would show that this assignment agrees with the world, not that the structure requires it.

### What about dimensionful quantities like masses?

Absolute masses and scales appear only among the 62 entries that are not counted as predictions. Several are structural numbers read in MeV; reading a number in a unit is an assignment of the same kind as reading 197 in degrees, with a far larger space of alternatives.

## Testing

### Can the framework be refuted?

Individual relations can. Each is stated as an exact equality with no theoretical uncertainty, and the rule is written in advance with no repair clause: a relation is rejected when its reference series (PDG, NuFIT, Planck, CODATA) excludes its value at 3σ, and it is not rescued by changing its formula, its unit, its scale or its dataset.

| Relation | Value | Rejected when | Where |
|---|---|---|---|
| δ_CP | 197° | a global fit whose 3σ interval excludes 197°; the unit assignment is rejected with it | DUNE, Hyper-Kamiokande |
| sin²θ₂₃ | 6/11 | a global fit whose 3σ interval excludes 6/11, in either octant | DUNE, Hyper-Kamiokande |
| sin²θ₁₂ | 4/13 | a global fit whose 3σ interval excludes 4/13 | JUNO (first result 0.3092 ± 0.0087; about four times tighter than today's global fit after six years) |
| m_τ/m_e and Q_Koide | 1776.74 and 1776.97 MeV for m_τ | an m_τ value whose 3σ interval excludes the value | Belle II, BES III |
| N_gen | 3 | a fourth sequential generation | LHC, FCC |
| m_s/m_d | 20 | a lattice determination with an uncertainty whose 3σ interval excludes 20 | lattice QCD |

A rejection rejects the relation and the assignment that produced it. It does not by itself reject the programme, whose other relations stand or fall on their own; the paper says so now, so that it cannot be said later as a repair. The wider exploratory programme has, at present, no single criterion of refutation.

### What would count in its favour?

Less than one might hope. Since closeness is not distinctive, further agreements at the percent level add little. What would change the picture is of another kind: a construction of the manifold, a mechanism that selects (21, 77), a rule that assigns formulas to observables, or a relation surviving a measurement precise enough to discriminate among competing vocabularies.

### Are there measurements that already contradict a relation?

Two contradicting results outside the reference series are reported beside their class. h = 167/248 agrees with Planck and is excluded by the SH0ES distance ladder at 5.5σ. The density relations agree with Planck and are strained by the baryon acoustic oscillations of DESI (second data release): DESI alone puts Ω_Λ/Ω_m = 113/52, Ω_m/Ω_Λ = 28/61 and Ω_DE at about 2σ; DESI combined with the cosmic microwave background puts them at −3.3σ, +3.4σ and −3.1σ, and h at −3.0σ. While methods disagree, the status is stated both ways, and neither agreement counts as a confirmation.

## Mathematics and verification

### Why E₈×E₈ and G₂ holonomy?

They are structures whose interest owes nothing to the Standard Model's constants: the octonions, Berger's classification of holonomy groups, the exceptional Lie algebras, and the role of both in M-theory. That answers whether the family deserves to be explored. It does not answer why this member: the requirements do not select (21, 77), the formulas or the normalization.

### What does the Lean 4 formalization prove?

The arithmetic. Given the declared integers, each of the 33 closed forms evaluates to the stated number (collected in `relations_v36_certified`; 156 files, 14 axioms, no `sorry`). It does not establish the existence of K₇, the physical interpretation of any relation, the choice of assignments, or the consistency of the relations taken together. A formula that is machine-checked is not thereby the right formula.

### Why these numbers and not others?

That is the selection question, and it is open. The pair (21, 77) is a construction-level input on the same footing as the G₂-holonomy postulate: fixed before the relations were frozen and used rigidly by all of them, but chosen, not selected. One numerical observation survives, b₂ + b₃ = 98 = dim(K₇) · dim(G₂), held as a target and not as a theorem.

### Does this mean physics is "just mathematics"?

The framework is read as a structural proposal: structure is asked to carry predictive weight, with no further ontological commitment. Readings in which geometry and information are aspects of one thing motivated the work historically; they are neither required nor supported by the relations.

## Practical

### What changed in version 3.6?

It withdraws several things earlier versions said: that the relations are derived from the geometry, that they cannot be fitted, that 95 observables are predicted, that a coincidence probability or a P-value measures the framework's distinctiveness, that 197° is a prediction of pure geometry, that the generation count comes from an index theorem. What remains is smaller and can be checked. The full list is in the [changelog]({chlog}).

### Where do I start reading?

- **No equations**: [K₇ for Everyone]({w}GIFT-for-Everyone.html).
- **Physicist**: the [main paper]({main}), sections 3, 4, 7 and 11.
- **Mathematician**: supplement S1 and the companion papers on the seam metric.
- **The numbers**: [Observable Reference]({w}Observable-Reference.html), [Validation Summary]({w}Validation-Summary.html), [Statistical Evidence]({w}Statistical-Evidence.html).

### How do I cite it?

The framework paper is archived on Zenodo; the concept DOI [10.5281/zenodo.16891489]({concept}) always resolves to the latest version. The [Citation Guide]({w}Citation-Guide.html) gives the formats.

### Can I use this in my research, or contribute?

Yes: the repository is under the MIT License. Corrections, new data comparisons and reports of errors are welcome through [GitHub issues](https://github.com/Arithmon/K7/issues); see `CONTRIBUTING.md`.

---

*The K₇ Framework v3.6*
"""

FAQ_FR = """# Foire aux questions

Les questions courantes sur le cadre K₇, à la version 3.6 de l'article. Là où cette page et l'[article principal]({main}) diffèrent, c'est l'article qui fait foi.

## Le cadre

### Qu'est-ce que le cadre K₇ ?

Une **correspondance déclarée**. Elle associe 33 paramètres sans dimension du Modèle Standard et de la cosmologie à des formes closes en les invariants d'une variété compacte K₇ de dimension sept, d'holonomie G₂ et de nombres de Betti (b₂, b₃) = (21, 77), avec une structure de jauge E₈×E₈. Par exemple, sin²θ_W reçoit b₂/(b₃ + dim G₂) = 3/13.

Elle est énoncée avec trois choses : son **dictionnaire** (vingt constantes structurelles et la grammaire dans laquelle s'écrivent les formules), son **registre des résidus** (tout ce qui a été posé plutôt que dérivé) et une **règle de décision** écrite à l'avance.

### Est-ce une dérivation des constantes du Modèle Standard ?

Non. On ne connaît aucune application géométrique qui envoie les invariants de K₇ sur les observables, et aucune règle ne fixe quelle formule est associée à quelle observable. Les versions précédentes écrivaient « dériver » là où l'opération est une attribution ; la version 3.6 retire ce mot partout. K₇ est un candidat privilégié, choisi par l'auteur, et l'article le dit.

### Y a-t-il des paramètres libres ?

Aucune relation n'a de paramètre **continûment** ajustable : un rapport d'entiers ne se retouche pas. Cela ne veut pas dire que rien n'a été choisi. Le registre des résidus (R1 à R12) énumère ce qui a été posé : la paire de Betti (21, 77), la normalisation imposée det(g) = 65/32, la combinaison κ_T⁻¹ = 61, l'unité dans laquelle l'entier 197 est lu comme phase CP, les échelles et schémas de masse des comparaisons, l'attribution des formules aux observables, et l'absence de choix entre relations incompatibles dans trois secteurs. Les versions précédentes parlaient d'un cadre sans paramètre libre ni ajustement ; cette description du choix des formules est retirée.

### La variété K₇ existe-t-elle ?

On ne le sait pas. Aucune variété G₂ compacte sans torsion de nombres de Betti (21, 77) n'est construite à ce jour, et la voie proposée dans la version 3.5 ne réalise pas cette paire ([erratum]({err}), §9). Les 33 relations n'utilisent pas la métrique de K₇ : elles reposent sur les invariants topologiques déclarés et sur les données du groupe E₈×E₈. Les articles compagnons certifient des morceaux locaux ou conditionnels (une métrique de couture, un ansatz de col), pas un K₇ compact.

### Quelle différence avec la théorie des cordes ou la M-théorie ?

E₈×E₈ et l'holonomie G₂ apparaissent toutes deux en M-théorie, mais le cadre ne fournit aucune compactification de ce type. Son K₇ lisse ne donne pas le contenu chiral non abélien du Modèle Standard, et ses relations ne sont pas dérivées d'une théorie effective à quatre dimensions. Il utilise les structures exceptionnelles comme source d'entiers, et le dit.

### Est-ce de la physique reconnue ?

Non. C'est le travail d'un chercheur indépendant, mené avec l'aide de l'IA, qui n'est pas passé par l'évaluation d'une revue. Les articles, les données et le code sont publics pour que chacun puisse vérifier ce qui est avancé. Le cadre a été cité dans la littérature à comité de lecture ; une citation n'est pas une approbation.

## Les 33 relations

### Que compare-t-on à l'expérience ?

Trente-trois relations sans dimension : couplages de jauge, rapports de masses des leptons et des quarks, paramètres de mélange PMNS et CKM, rapports de masses des bosons et paramètres cosmologiques. La [référence des observables]({w}Observable-Reference.fr.html) donne chaque formule, sa valeur, la mesure et son statut.

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

Les versions précédentes résumaient l'accord par un écart moyen. Ce résumé est retiré : il masquait les relations au-delà de 2σ. Le détail est dans le [bilan de validation]({w}Validation-Summary.fr.html).

### Sont-ce 33 tests indépendants ?

Non. Trois secteurs sont surdéterminés : quatre relations leptoniques portent sur deux rapports de masses, trois relations CKM sur deux paramètres, sept relations de densité sur deux densités indépendantes. Dans chacun, les relations se contredisent en tant qu'égalités exactes : elles ne peuvent pas toutes tenir, et aucune n'est choisie après coup. Prises ensemble comme égalités exactes, les 33 sont déjà incompatibles ; chaque relation reste testable séparément.

### L'accord est-il statistiquement significatif ?

Non. Dans un test look-elsewhere préenregistré, chaque concurrent cherche ses propres formules, dans la même grammaire et avec le même budget. K₇ atteint 31 des 33 cibles ; 1 085 paires de Betti alternatives sur 4 159 et 1 015 vocabulaires inventés sur 2 000 en atteignent autant, et aucun n'en atteint plus (le seuil préenregistré n'est pas atteint, donc aucune valeur p n'est rapportée). Un contrôle sans aucune constante de K₇ en atteint 30. La proximité avec les valeurs mesurées n'est donc pas, à elle seule, un indice en faveur de K₇.

Les probabilités de coïncidence, valeurs P et facteurs de Bayes des versions précédentes sont retirés : ils venaient de tests où les alternatives étaient notées avec les formules de K₇. Voir les [éléments statistiques]({w}Statistical-Evidence.fr.html) ; le code et les résultats du test sont [publics]({lee}).

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

Elle retire plusieurs affirmations des versions précédentes : que les relations sont dérivées de la géométrie, qu'elles ne peuvent pas être ajustées, que 95 observables sont prédites, qu'une probabilité de coïncidence ou une valeur P mesure le caractère distinctif du cadre, que 197° est une prédiction de pure géométrie, que le nombre de générations vient d'un théorème de l'indice. Ce qui reste est plus modeste et se vérifie. La liste complète est dans le [journal des changements]({chlog}).

### Par où commencer ?

- **Sans équations** : [K₇ pour tout le monde]({w}GIFT-for-Everyone.fr.html).
- **Physicien** : l'[article principal]({main}), sections 3, 4, 7 et 11.
- **Mathématicien** : le supplément S1 et les articles compagnons sur la métrique de couture.
- **Les chiffres** : [référence des observables]({w}Observable-Reference.fr.html), [bilan de validation]({w}Validation-Summary.fr.html), [éléments statistiques]({w}Statistical-Evidence.fr.html).

### Comment citer ?

L'article du cadre est archivé sur Zenodo ; le DOI concept [10.5281/zenodo.16891489]({concept}) renvoie toujours à la dernière version. Le [guide de citation]({w}Citation-Guide.html) (en anglais) donne les formats.

### Puis-je m'en servir dans mes recherches, ou contribuer ?

Oui : le dépôt est sous licence MIT. Les corrections, les nouvelles comparaisons de données et les signalements d'erreurs sont bienvenus par les [tickets GitHub](https://github.com/Arithmon/K7/issues) ; voir `CONTRIBUTING.md`.

---

*K₇ Framework v3.6*
"""


def faq(lang, w):
    src = FAQ_EN if lang == "en" else FAQ_FR
    return src.format(w=w, main=MAIN, chlog=CHLOG, err=ERR, lee=LEE, concept=CONCEPT)


# ---------------------------------------------------------------- Executive summary
EXEC_EN = """---
title: "K₇: Executive Summary"
---

# K₇: a correspondence, and the terms on which it can fail

*A technical summary for curious physics readers, as of version 3.6*

---

## The problem, stated plainly

The Standard Model of particle physics operates with a precision no other scientific theory has ever matched. It describes every known fundamental interaction apart from gravity, with experimental agreement sometimes reaching twelve decimal places.

Yet it contains about nineteen free parameters, numbers the theory does not compute and which must be measured before the theory can be used: the masses of the charged leptons and of the six quarks, the parameters of the CKM matrix, the three coupling constants, the Higgs mass and its vacuum expectation value. Neutrino masses and mixing add more.

To this are added long-standing puzzles. Why exactly three generations of matter? Why do the charged lepton masses obey the Koide relation *Q* = 2/3 so closely, a relation noticed in 1981 and never explained? Why does the ratio of dark matter to baryonic matter sit close to a simple rational?

K₇ (*formerly Geometric Information Field Theory*) is one attempt to look at these numbers differently. It asks: what if they could be written as closed forms in the invariants of a single geometric structure? And, since writing such forms turns out to be easy, it asks a second question with the same seriousness: what would it take for such a correspondence to mean anything?

## The proposal

In one sentence: 33 dimensionless parameters of the Standard Model and of cosmology are assigned to algebraic combinations of the topological invariants of a compact seven-dimensional manifold with exceptional holonomy, together with an E₈ × E₈ gauge structure.

A **seven-dimensional manifold** is a curved space with seven dimensions. **Holonomy** measures how a vector changes when carried around a closed loop in that space. For most manifolds this change can be any rotation. Certain manifolds have holonomy restricted to a subgroup, and in seven dimensions there is an exceptional one, **G₂**, of dimension 14, the automorphism group of the octonions. Manifolds with G₂ holonomy are rare and difficult to construct.

The **topological invariants** of such a manifold are integers that characterize its shape independently of its metric. The most important are the **Betti numbers** *b₂* and *b₃*, which count the harmonic 2-forms and 3-forms the space can carry. They are whole numbers and cannot vary continuously.

The framework posits a manifold *K₇* with (*b₂*, *b₃*) = (21, 77), together with E₈ × E₈, of dimension 496. From these and a few related integers (twenty structural constants in all), it writes formulas such as

- sin²θ_W = *b₂* / (*b₃* + dim G₂) = 3/13,
- *Q*_Koide = dim G₂ / *b₂* = 2/3,
- *m*_τ / *m*_e = 7 + 10 × 248 + 10 × 99 = 3477.

**E₈** is the largest exceptional Lie group. The framework does not try to embed the Standard Model's particles in E₈, an approach shown to be impossible by Distler and Garibaldi in 2010. It uses E₈ × E₈ as a source of group-theoretic integers, which avoids that obstruction and also means that it makes no claim about how the fermions arise.

## A correspondence, not a derivation

This is the point on which version 3.6 differs most from what came before, and it is worth stating bluntly.

**No geometric map is known that sends the invariants of K₇ to the observables.** The formulas are *assigned*: nothing in the geometry says that sin²θ_W must be *b₂* / (*b₃* + dim G₂) and not some other ratio. Earlier versions wrote "derive" for this operation. Version 3.6 withdraws the word.

**No rule fixes which formula goes with which observable.** The grammar and the list of observables were frozen after the formulas had been found.

**The manifold is not constructed.** No compact torsion-free G₂ manifold with Betti numbers (21, 77) is currently known, and the route proposed in version 3.5 does not produce one. The relations use only the declared integers, not a metric.

What the paper does instead is make the correspondence auditable. It gives the full **dictionary**. It keeps a **residue register** of everything that was set rather than derived: the pair (21, 77), an imposed normalization det(g) = 65/32, a combination κ_T⁻¹ = 61, the unit in which an integer is read as a CP phase, the scales of the comparisons, the assignments themselves. And it writes a **decision rule** with no repair clause.

K₇ is, in the paper's own terms, a *privileged candidate*: a member of a well-motivated family, designated by the author for reasons that are the author's own and are declared as such. Presenting a privileged candidate as a demonstrated uniqueness is what the earlier versions did, and what this one stops doing.

## How the framework was built

The first version, in 2025, carried four adjustable geometric parameters tuned to reproduce about 22 observables. A second version reduced them to three quantities, each a ratio of topological integers. The current structure has no continuously adjustable parameter: the relations are ratios of integers, or use one further declared operation.

Earlier versions of this summary read that trajectory (four, three, zero parameters, with more observables covered each time) as a sign that what was happening was compression and not fitting. That reading does not survive. Removing continuous parameters while choosing formulas from a rich grammar moves the freedom; it does not remove it. The freedom now sits in the choice of formulas, of the vocabulary and of the Betti pair, which is exactly what the residue register records and what the look-elsewhere test below prices.

What the absence of continuous parameters does give is **rigidity**: an integer ratio cannot be nudged, so a single precise measurement can reject a relation. Rigidity exposes a framework to refutation. It does not certify it: an exceptional structure is rigid whether it was derived or chosen for the values it gives.

## Where the 33 relations stand

Against the most recent data (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022), with one convention for all uncertainties, the relations fall into five classes, which are not added into a single score:

- **23 lie within two standard deviations** of the measurement. Among them *Q*_Koide = 2/3, α_s = √2/12, the CP phase read as 197°, and most quark, mixing and cosmological ratios.
- **2 are in tension**, between 2σ and 3σ: *m*_τ/*m*_e = 3477 and Ω_c/Ω_m = 27/32.
- **6 are rejected as exact equalities** at more than 3σ and kept only as numerical proximities: α⁻¹, sin²θ_W = 3/13, *m*_μ/*m*_e, *m*_μ/*m*_τ, *m*_b/*m*_t and *m*_W/*m*_Z = 37/42. The quantities are measured so precisely that a formula 0.2%% away is many standard deviations off.
- **1 lies inside a range** the PDG gives without uncertainty: *m*_s/*m*_d = 20.
- **1 sits in the other octant**: sin²θ₂₃ = 6/11, while the global fit prefers the first octant; the value lies inside the fit's 3σ range.

They are also **not 33 independent tests**. In three sectors there are more relations than quantities: four lepton relations for two mass ratios, three CKM relations for two parameters, seven density relations for two densities. In each sector the relations disagree with one another as exact equalities. Each formula is computed correctly, and the formulas cannot all be true together.

Most of the 23 are tested only weakly: where experimental uncertainties are at the percent level, a percent-level agreement is what a rich vocabulary reaches easily.

## Why the coincidence hypothesis cannot be ruled out

Faced with formulas this close to the data, the question is unavoidable: is this the result of a fishing expedition in an ocean of algebraic combinations?

Earlier versions of this summary answered no, and cited statistical tests: a rank among three million configurations, a P-value, Bayes factors, leave-one-out validations. All of them are withdrawn. They shared one flaw. The alternatives were scored with K₇'s own formulas, which had been chosen for (21, 77); no alternative was allowed to search for its own. Under that design, (21, 77) wins by construction.

Version 3.6 replaces them with a preregistered test in which **every competitor searches for its own formulas**, in the same grammar, with the same budget and the same freedom of assignment. The result:

- K₇ reaches 31 of the 33 targets.
- 1 085 of 4 159 alternative Betti pairs reach as many, and 1 015 of 2 000 invented vocabularies reach as many. None reaches more.
- A witness with no K₇ constant at all, using only the universal symbols of the grammar, reaches 30.

The preregistered verdict: the look-elsewhere effect is not overcome, and the P-value is withdrawn from the text. **Closeness to the measured values is not, by itself, evidence for K₇.** This is not a refutation either: the test says that the score does not discriminate, not that the framework is wrong.

What survives the test is modest and real: rigidity under a dictionary fixed in advance, and a written record of what was chosen.

## How a relation can fail

The relations are stated as exact equalities with no theoretical uncertainty. A relation is rejected when its reference data series excludes its value at 3σ. No formula, unit, scale or dataset is changed afterwards to rescue it.

**The CP phase.** The structure produces the integer 197. Reading it in degrees is a choice, declared as such. DUNE and Hyper-Kamiokande will measure δ_CP; a global fit whose 3σ interval excludes 197° rejects the relation together with the choice of unit. Today the fit gives 212 (+26/−36)°.

**The octant of θ₂₃.** A fit whose 3σ interval excludes 6/11 rejects that relation.

**The solar angle.** JUNO's first measurement gives sin²θ₁₂ = 0.3092 ± 0.0087, against 4/13 = 0.3077. After six years its uncertainty should be about four times smaller than that of today's global fit, and a 3σ exclusion of 4/13 rejects the relation.

**The tau mass.** Two relations give 1776.74 and 1776.97 MeV; a precise enough measurement must reject at least one.

**A fourth generation** would reject the integer identity *N*_gen = 3.

A rejection rejects a relation and the assignment behind it. It does not by itself reject the programme, and the paper says so in advance so that it cannot be said later as a repair. Conversely, a confirmation would show that an assignment agrees with the world, not that the structure requires it. Two results outside the reference series already contradict a relation (the SH0ES value of the Hubble constant, and the DESI baryon acoustic oscillations for the density ratios) and are reported beside it.

## What K₇ is not

K₇ is not a theory of everything. It does not address quantum gravity or the measurement problem.

K₇ is not a derivation of the Standard Model. Its smooth manifold does not yield the chiral non-abelian content of the Standard Model, and its relations do not come from a four-dimensional effective theory.

K₇ is not a cosmogony. It proposes no mechanism for the selection of the manifold. Five routes to deriving (21, 77) have been investigated and closed without success; one numerical observation remains, *b₂* + *b₃* = 98 = 7 × 14, held as a target and not as a theorem.

K₇ does not depend on any reading of the word *information*. The relations stand or fall independently of what "information" ultimately is. The lineage that motivated the work (Wheeler's "it from bit", Bekenstein's bound, Jacobson's thermodynamic derivation of Einstein's equations, the holographic programme) makes the idea that geometry and information are related less exotic than it sounds; it is neither required nor supported by the relations. A separate essay discusses it ([*Gift from Bit*](https://arithmon.substack.com/p/gift-from-bit)).

## The open questions

- **Existence.** A compact torsion-free G₂ manifold with (21, 77) is not constructed.
- **Physics.** No mechanism leads from a smooth K₇ to the chiral Standard Model.
- **Selection.** Nothing selects (21, 77); it is chosen.
- **Assignment.** No rule assigns formulas to observables.
- **Dependencies.** The audit of the dependencies among the 33 relations is not complete, so no count of independent tests is given.

## What remains to be seen

The paper does not claim that the framework is correct. It may be a genuine structural insight, an approximation to one, or an elaborate coincidence. The aim of version 3.6 is that whichever it is can be found out, and that a reader can see, at every step, what was derived, what was assumed, and what would bring it down.

That is a smaller claim than the one this page used to make. It can be checked.

---

*For the full statement, see the [main paper](%(main)s) and its supplements; the code and results of the look-elsewhere test are [public](%(lee)s). The latest deposited version is always at the Zenodo concept DOI [10.5281/zenodo.16891489](%(concept)s).*
"""

EXEC_FR = """---
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
- **6 sont rejetées comme égalités exactes** à plus de 3σ et gardées seulement comme proximités numériques : α⁻¹, sin²θ_W = 3/13, *m*_μ/*m*_e, *m*_μ/*m*_τ, *m*_b/*m*_t et *m*_W/*m*_Z = 37/42. Ces quantités sont mesurées si précisément qu'une formule à 0,2 %% se trouve à de nombreux écarts-types.
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

*Pour l'énoncé complet, voir l'[article principal](%(main)s) et ses suppléments ; le code et les résultats du test look-elsewhere sont [publics](%(lee)s). La dernière version déposée est toujours au DOI concept Zenodo [10.5281/zenodo.16891489](%(concept)s).*
"""


def exec_summary(lang):
    src = EXEC_EN if lang == "en" else EXEC_FR
    return src % dict(main=MAIN, lee=LEE, concept=CONCEPT)


# ---------------------------------------------------------------- For physicists
PHYS_EN = """# The K₇ Dictionary: a Technical Overview for Physicists

*As of version 3.6 of the framework paper. Where this page and the [main paper](%(main)s) differ, the paper holds.*

## Abstract

The K₇ framework states a **declared correspondence**: the topological and Lie-theoretic invariants of a compact seven-manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with an E₈×E₈ gauge structure, are assigned to 33 dimensionless Standard-Model and cosmological parameters by explicit closed forms. It is presented as a privileged candidate, not as a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable. The paper makes the correspondence auditable, with a dictionary, a residue register and a decision rule.

## 1. The parameter problem and the selection problem

The Standard Model leaves about nineteen parameters to measurement and explains neither its gauge group nor its three generations. Any framework that proposes structure behind these numbers inherits two questions that are easily run together:

1. **Does a family of structures deserve to be explored?** For K₇ the answer is positive: the octonions, G₂ holonomy and E₈ are structures whose interest owes nothing to the Standard Model's constants.
2. **Why this precise structure, and these precise assignments?** This is **not** answered. The pair (21, 77) is not derived, and the formulas are assigned, not forced.

## 2. The inputs

**E₈×E₈.** Used as a source of group-theoretic integers (dimensions, ranks, representation dimensions of E₈ and of its exceptional subgroups). The framework does not embed Standard-Model fermions in E₈, which avoids the Distler–Garibaldi obstruction and also means it makes no claim about how the fermions arise.

**G₂ holonomy.** In seven dimensions G₂ is the exceptional holonomy group of Berger's list; it is the automorphism group of the octonions and the condition for N = 1 supersymmetry in an M-theory compactification on a seven-manifold.

**K₇.** A compact G₂-holonomy manifold with (b₂, b₃) = (21, 77) is *posited*. **No such manifold is currently constructed**; the topological route of version 3.5 does not realise the pair. The companion papers certify local or conditional pieces (a Newton–Kantorovich-certified seam metric, a neck ansatz), not a compact K₇. The relations use only the declared integers and no metric.

**What is not supplied.** A smooth G₂ compactification gives an abelian, non-chiral four-dimensional theory. The chiral non-abelian content of the Standard Model would require a UV bridge (a singular locus, a heterotic bundle, or a duality) that the framework does not provide. The relations are not derived from a four-dimensional effective theory, and they are not stated at a common energy scale: each comparison carries a (scheme, scale, dataset) tag.

## 3. The dictionary

All 33 relations are written in twenty structural constants: seven primitive (among them dim E₈ = 248, rank E₈ = 8, dim G₂ = 14, dim K₇ = 7, b₂ = 21, b₃ = 77) and thirteen derived (for instance H* = b₂ + b₃ + 1 = 99, N_gen = 3, the Weyl factor 5, |PSL(2,7)| = 168). The grammar is ratios and small integer combinations, with four further operations declared when used (√, φ, ln 2, ζ values).

Representative entries:

| Observable | Formula | K₇ value | Measured | Pull | Status |
|---|---|---|---|---|---|
| sin²θ_W (M_Z, MS-bar) | b₂/(b₃ + dim G₂) = 3/13 | 0.230769 | 0.23122(6) | −7.5σ | proximity |
| α_s(M_Z) | √2/(dim G₂ − p₂) = √2/12 | 0.117851 | 0.1180(9) | −0.2σ | within 2σ |
| Q_Koide | dim G₂/b₂ = 2/3 | 0.666667 | 0.6666645(51) | +0.4σ | within 2σ |
| m_τ/m_e | 7 + 10·248 + 10·99 = 3477 | 3477 | 3477.37(18) | −2.1σ | tension |
| sin²θ₂₃ (PMNS) | 6/11 | 0.545455 | 0.470 (+17/−14) | second octant | inside the NuFIT 3σ range |
| δ_CP | 7·14 + 99 = 197, read in degrees | 197° | 212 (+26/−36)° | −0.4σ | unit assignment |
| m_W/m_Z | 37/42 | 0.880952 | 0.881285(87) | −3.8σ | proximity |
| Ω_DE | ln 2 · 98/99 | 0.686146 | 0.6847(73) | +0.2σ | within 2σ |

The complete table is in the [Observable Reference](Observable-Reference.html).

**The residue register.** What was set rather than derived is listed and ranked with the results (R1 to R12): the Betti pair; the imposed normalization det(g) = 65/32; the combination κ_T⁻¹ = 61; the unit in which 197 is read as a phase; the scales and mass schemes of the comparisons; the formula assignments; and, in three overdetermined sectors, the absence of a choice among mutually incompatible relations.

## 4. Where the relations stand

Against PDG 2026, NuFIT 6.1, Planck 2018 and CODATA 2022, with uncertainties at 1σ: 23 relations lie within 2σ; 2 are in tension (m_τ/m_e, Ω_c/Ω_m); 6 are excluded as exact equalities at more than 3σ and retained as proximities (α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t, m_W/m_Z); m_s/m_d lies inside a PDG range that carries no uncertainty; sin²θ₂₃ sits in the second octant, inside the 3σ range of the global fit. The classes are not added into one score.

The 33 are **not independent tests**. Four lepton relations bear on two mass ratios, three CKM relations on two Wolfenstein parameters (sin θ₂₃ = Aλ², 2.6%% apart), seven density relations on two independent densities. In each sector the relations are mutually incompatible as exact equalities, and none is selected. Other dependencies exist (sin²θ_W and m_W/m_Z are related through radiative corrections) and the audit is not complete.

Six relations use det(g) = 65/32 and three use κ_T⁻¹ = 61. A reader who regards the imposed normalization as an extra parameter should read the framework through the reduced counts given in the [Validation Summary](Validation-Summary.html).

## 5. Look-elsewhere

In a preregistered test, every competitor searches for its own formulas in the same grammar, at the same budget (five nodes) and with the same windows (2σ). K₇ reaches 31 of the 33 targets; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many, and none reaches more. The preregistered threshold is not met: the effect is not overcome, and no p-value is reported. A control with no K₇ constant reaches 30. In the public Sieve battery, no K₇ relation clears the null that prices the choice of vocabulary.

Closeness to the measured values is therefore not, by itself, evidence. The coincidence probabilities and P-values of earlier versions are withdrawn. Details and code: [Statistical Evidence](Statistical-Evidence.html).

## 6. What is claimed, and what is not

**Claimed.** Given the declared constants and assignments, the 33 relations hold as arithmetic identities (machine-checked in Lean 4), and they lie at the stated deviations from measurement. The decision rule applies to them.

**Not claimed.** That the relations are derived from the geometry of K₇; that (21, 77), the formulas or det(g) = 65/32 are forced by any requirement; that the relations hold at a common scale; that closeness is evidence; that the manifold has been constructed; that the chiral Standard Model follows from it.

## 7. Decision rule

The relations are exact equalities with no theoretical uncertainty. A relation is rejected when its reference series excludes its value at 3σ, and it is not rescued by changing its formula, unit, scale or dataset.

| Quantity | K₇ value | Rejected by |
|---|---|---|
| δ_CP (phase 2π·197/360) | 197° | a global fit, with DUNE or Hyper-Kamiokande, whose 3σ interval excludes 197°; the unit assignment falls with it |
| sin²θ₂₃ | 6/11 | a global fit whose 3σ interval excludes 6/11, in either octant |
| sin²θ₁₂ | 4/13 | a global fit whose 3σ interval excludes 4/13; JUNO's first result is 0.3092 ± 0.0087, and its six-year precision is about four times that of today's global fit |
| m_τ/m_e, Q_Koide | m_τ = 1776.74 and 1776.97 MeV | an m_τ value whose 3σ interval excludes the value; the two differ by 0.23 MeV |
| N_gen | 3 | a fourth sequential generation |
| m_s/m_d | 20 | a lattice determination with an uncertainty whose 3σ interval excludes 20 |

Outside the reference series, h = 167/248 is excluded by SH0ES at 5.5σ while agreeing with Planck, and the baryon acoustic oscillations of DESI (second data release) combined with the cosmic microwave background put Ω_Λ/Ω_m = 113/52, Ω_m/Ω_Λ = 28/61, Ω_DE and h at −3.3σ, +3.4σ, −3.1σ and −3.0σ (about 2σ for the three density relations with DESI alone); both are reported beside the class. A rejection rejects a relation and its assignment, not the programme by itself; a confirmation would confirm an assignment, not a requirement of the structure.

## 8. Relation to other approaches

**M-theory.** E₈×E₈ and G₂ holonomy both appear in M-theory. The framework does not supply a compactification of either kind and differs from standard G₂ phenomenology, which works with moduli stabilization and singular compactifications.

**Direct E₈ embeddings.** Not attempted (Distler–Garibaldi).

**The string landscape.** The framework does not solve a selection problem; it has one of its own, stated in the residue register.

## 9. Summary

Thirty-three dimensionless parameters are matched by closed forms in the invariants of a G₂-holonomy seven-manifold with (21, 77) and of E₈×E₈. The correspondence is not derived, its closeness to the data is not distinctive, and its manifold is not constructed. What it offers is rigidity (no continuous parameter), a written residue, and a rule fixed in advance under which individual relations can be rejected. The paper does not claim that the framework is correct.

---

*K₇ Framework v3.6*
"""


def for_physicists():
    return PHYS_EN % dict(main=MAIN)
