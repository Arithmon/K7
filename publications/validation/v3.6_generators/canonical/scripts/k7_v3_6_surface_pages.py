#!/usr/bin/env python3
"""k7_v3_6_surface_pages.py -- pages statistiques de K7 régénérées sur la 3.6.

Étape 4 de la v3.6 (2026-11-10). Écrit, dans le clone public K7 :

  docs/wiki/Statistical-Evidence.md / .fr.md
  publications/references/STATISTICAL_EVIDENCE.md
  docs/wiki/Validation-Summary.md / .fr.md
  docs/wiki/Observable-Reference.md / .fr.md
  publications/references/OBSERVABLE_REFERENCE.md
  publications/references/observables.csv   (copie de canonical/data/observables.csv)
  docs/FAQ.md / .fr.md et docs/wiki/FAQ.md / .fr.md   (prose : k7_v3_6_surface_prose.py)

Les TABLES ne sont pas recopiées à la main : elles sont lues des sources du
papier (blocs BEGIN/END de supplement_sieve_diagnostics.md, eux-mêmes générés
par k7_v3_6_s4_tables.py ; table du §4.1 et table des classes du §4.2 de
physics_main.md, générées par k7_v3_6_table_sec4.py). Si le papier change,
relancer ce script change les pages. La prose (EN et FR) est écrite ici, une
seule fois pour les trois copies de la page statistique.

Usage : k7_v3_6_surface_pages.py [--k7 DIR] [--check]
  --check : n'écrit rien, code 1 si une page diffère de ce qui serait généré.
"""
import argparse
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from k7_v3_6_surface_prose import faq, exec_summary, for_physicists  # noqa: E402
ROOT = os.path.dirname(os.path.dirname(HERE))
PAPERS = os.path.join(ROOT, "canonical", "papers", "framework")
K7_DEFAULT = os.path.join(os.path.dirname(ROOT), "K7")
GH = "https://github.com/Arithmon/K7/blob/main/"
MAIN = GH + "publications/papers/markdown/k7_framework_3_6_main.md"
S4 = GH + "publications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md"
S3 = GH + "publications/papers/markdown/k7_framework_3_6_S3_observables.md"
LEGACY = GH + "publications/validation/legacy/v3.3/"
LEE = GH + "publications/validation/v3.6/"
QB = "https://github.com/arithmon/program/blob/main/problems/selection-principle.md"


def read(name):
    return open(os.path.join(PAPERS, name), encoding="utf-8").read()


def block(text, tag):
    m = re.search(r"<!-- BEGIN %s -->\n(.*?)\n<!-- END %s -->" % (tag, tag), text, re.S)
    if not m:
        raise SystemExit("bloc %s introuvable" % tag)
    return m.group(1)


def table_after(text, heading):
    """Première table markdown après un titre donné."""
    i = text.index(heading)
    lines = text[i:].split("\n")
    out, on = [], False
    for ln in lines[1:]:
        if ln.startswith("|"):
            on = True
            out.append(ln)
        elif on:
            break
    if not out:
        raise SystemExit("pas de table après %r" % heading)
    return "\n".join(out)


def only_table(md):
    return "\n".join(l for l in md.split("\n") if l.startswith("|"))


# ---- traduction des tables (termes fermés ; les nombres prennent la virgule) ----
FR_TERMS = [
    ("blind search on its own vocabulary", "recherche aveugle sur son propre vocabulaire"),
    ("alternative Betti pairs, variant derivations (outside the rule)", "paires de Betti alternatives, dérivations variantes (hors règle)"),
    ("alternative Betti pairs (published derivations)", "paires de Betti alternatives (dérivations publiées)"),
    ("invented vocabularies (Sieve generator)", "vocabulaires inventés (générateur du Sieve)"),
    ("invented vocabularies (generator of [M])", "vocabulaires inventés (générateur de [M])"),
    ("reach ≥ 31/33 (as many as K₇)", "atteignent ≥ 31/33 (autant que K₇)"),
    ("reach ≥ ", "atteignent ≥ "), ("(as many as K₇)", "(autant que K₇)"),
    ("best coverage", "meilleure couverture"), ("description cost, range (bits)", "coût de description, étendue (bits)"),
    ("K₇ description cost (bits)", "coût de description de K₇ (bits)"), ("K₇ coverage", "couverture de K₇"),
    ("S_cost range (bits)", "étendue de S_cost (bits)"), ("cost ≤ K₇", "coût ≤ K₇"),
    ("Family", "Famille"), (" to ", " à "),
    ("K₇ reaches (blind)", "K₇ atteint (aveugle)"),
    ("published value in K₇'s ≤ 5-node set", "valeur publiée dans l'ensemble ≤ 5 nœuds de K₇"),
    ("published value within window", "valeur publiée dans la fenêtre"),
    ("Betti pairs reaching (of 4 159)", "paires de Betti qui atteignent (sur 4 159)"),
    ("vocabularies reaching (of 2 000)", "vocabulaires qui atteignent (sur 2 000)"),
    ("| yes ", "| oui "), ("| no ", "| non "),
    ("first run (2026-10-17, dataset of v3.5, one-sided windows)", "premier passage (2026-10-17, données de la v3.5, fenêtres d'un seul côté)"),
    ("revision 1 (2026-10-24, refreshed dataset, two-sided windows; historical)", "révision 1 (2026-10-24, données rafraîchies, fenêtres des deux côtés ; historique)"),
    ("revision 2 (2026-11-03, current dataset)", "révision 2 (2026-11-03, données courantes)"),
    ("revision 1 (2026-10-24, refreshed dataset, two-sided windows)", "révision 1 (2026-10-24, données rafraîchies, fenêtres des deux côtés)"),
    ("revision 2 (2026-11-03, density ratios on the Planck chains)", "révision 2 (2026-11-03, rapports de densité sur les chaînes de Planck)"),
    ("revision 3 (2026-11-11, current dataset: m_W/m_Z from the published masses)", "révision 3 (2026-11-11, données courantes : m_W/m_Z depuis les masses publiées)"),
    (": reach as many as K₇", " : atteignent autant que K₇"),
    ("reach as many as K₇", "atteignent autant que K₇"), ("P_global, verdict", "P_global, verdict"),
    ("preregistered outcome", "issue préenregistrée"), ("| share |", "| part |"),
    ("look-elsewhere effect not overcome", "effet look-elsewhere non surmonté"), ("look-elsewhere effect overcome", "effet look-elsewhere surmonté"),
    ("targets reached by nobody", "cibles atteintes par personne"), ("Quantity", "Quantité"),
    ("scheme of R7", "schéma de R7"), ("\\|pull\\|", "\\|écart\\|"),
    ("F-BETTI-FICHE:", "F-BETTI-FICHE :"), ("F-BETTI:", "F-BETTI :"), ("F-VOCAB:", "F-VOCAB :"),
    (" of ", " sur "),
    # table du §4.1 et des classes
    ("| Observable |", "| Observable |"), ("| Formula |", "| Formule |"), ("| K₇ value |", "| Valeur K₇ |"),
    ("| Measured |", "| Mesure |"), ("| Dev. |", "| Écart |"), ("| Pull |", "| Écart normalisé |"), ("| Status |", "| Statut |"),
    ("| Class |", "| Classe |"), ("| Count |", "| Nombre |"),
    ("inside the NuFIT 3σ range", "dans l'intervalle à 3σ de NuFIT"),
    ("in the scheme declared in R7", "dans le schéma déclaré en R7"),
    ("in the declared mass scheme", "dans le schéma de masse déclaré"),
    ("scheme of R7", "schéma de R7"),
    ("inside the PDG range (no uncertainty)", "dans l'intervalle du PDG (sans incertitude)"),
    ("inside the PDG range", "dans l'intervalle du PDG"),
    ("non-Gaussian profile", "profil non gaussien"),
    ("the remaining relations", "les autres relations"),
    ("within 2σ", "à moins de 2σ"),
    ("unit assignment", "assignation d'unité"), ("approximate", "approchée"),
    ("**proximity**", "**proximité**"), ("proximity (", "proximité ("), ("**tension**", "**tension**"),
    ("algebraic", "algébrique"), ("integer", "entier"), ("ζ values", "valeurs de ζ"),
    ("(range)", "(intervalle)"), ("phase 2π", "phase 2π"), ("octant;", "octant ;"), ("n/a", "s.o."),
]


def fr_table(md):
    out = []
    for line in md.split("\n"):
        for a, b in FR_TERMS:
            line = line.replace(a, b)
        line = re.sub(r"(?<![§Sv\d.])(\d+)\.(\d)", r"\1,\2", line)   # 0.26 -> 0,26 ; pas §4.3, S4.2, v3.5
        line = re.sub(r"(\S); ", r"\1 ; ", line)
        out.append(line)
    return "\n".join(out)


# ---------------------------------------------------------------- prose EN
def stat_en(t):
    return """# Statistical Evidence: the Look-Elsewhere Test

**Framework version**: 3.6. **Source**: main paper [§7]({main}) and supplement [S4]({s4}); the tables on this page are copied from S4 by a script, not edited by hand.

A framework that matches 33 measured values with closed forms in a vocabulary of twenty constants must answer a prior question: how often would the same grammar, with a different vocabulary, have matched them just as well? Version 3.6 asked that question with a preregistered test. The answer is that **closeness to the measured values does not distinguish K₇** in the reference classes tested. The statistical claims of earlier versions of this page are withdrawn; section 6 lists them.

---

## 1. Summary

| | |
|---|---|
| **Question** | Does K₇ remain exceptional when each competitor searches for its own formulas, in the same grammar, at the same budget, with the same freedom of assignment and of unit? |
| **Preregistered** | 2026-10-17, before any full run (a pilot of nine vocabularies, declared in the preregistration, had run first), with two outcomes only: a calibrated global p-value, or no p-value in the text |
| **K₇** | reaches 31 of the 33 targets |
| **Alternative Betti pairs** | 1 085 of 4 159 reach as many (26%); none reaches more |
| **Invented vocabularies** | 1 015 of 2 000 reach as many (51%); none reaches more |
| **Control with no K₇ constant** | reaches 30 of the 33 with the universal leaves of the grammar alone |
| **Outcome** | the preregistered threshold is not met: the look-elsewhere effect is not overcome, and no p-value is reported; the proportions above are descriptive |

The proportions are not a probability that K₇ is right or wrong, and the counts are not a physical refutation. They say that the top score has little discriminating power in this protocol: 30 targets are reached by everyone, two by no one, and one separates the competitors.

## 2. The test

- **Targets.** The 33 relations of the dataset ([S3]({s3})), with their measured values and uncertainties.
- **Grammar.** The frozen engine of the Sieve: its universal leaves (1 to 9, π, e, φ, γ, ln 2, ζ(3) to ζ(11)) plus the 19 integer constants of the competitor, the operations + − × / ^, square root, inverse, square and logarithm, and **at most five nodes** per expression.
- **Concordance.** A target is reached if one expression of the vocabulary falls within 2σ of the measured value on either side, asymmetric uncertainties being kept asymmetric. For m_s/m_d, which the PDG gives as a range, the window is that range. For δ_CP, the phase may be read in degrees, radians, grads or turns.
- **Assignment.** The search is blind: each target takes the cheapest concordant expression. The freedom to assign formulas to observables is granted to everyone, K₇ included, which is scored by the same search on its own vocabulary and not by its published formulas.
- **Competitors.** Every Betti pair with b₂ in [1, 40] and b₃ in [17, 120] other than (21, 77), with H*, κ_T⁻¹ and det(g) re-derived and the other constants held at K₇'s values; and 2 000 vocabularies of 19 integers drawn by the Sieve's frozen generator.
- **Verdict rule.** For a family of size N in which n competitors reach at least as many targets as K₇, the decision statistic is (1 + n)/(1 + N), ties counting against K₇. The larger of the two family values is compared with 0.01: at or below it, a calibrated global p-value is reported; above it, none is, and the proportions are given as descriptions. The values of the statistic are in the deposited result file.

The alphabet tested for K₇ is the nineteen integers of the version 3.5 Monte Carlo register, not literally the twenty constants of the main paper (§3.1): dim E₇ = 133 and α_sum = 13 are absent and κ_T⁻¹ = 61 is present. A test on the literal register would be a separate computation.

## 3. Result

{families}

The threshold is not met in either of the first two rows. The variant row does not enter the verdict. K₇ is not cheaper either: its description cost lies inside the range of both families.

Per target:

{targets}

Most targets are reached by every competitor: at five nodes and 2σ, the grammar covers them whatever the vocabulary. The targets that discriminate are the few with very small relative uncertainties. α⁻¹ and m_μ/m_e are reached by nobody, K₇ included. m_τ/m_e is reached by K₇ and by about a third of the competitors, and the counts of the family table are exactly the counts on that one target. Three scores must be kept apart: the published formulas (24 of the 33 lie inside their windows), the free search with K₇'s alphabet (31), and the control with no K₇ constant (30).

## 4. The Sieve scorecard

The Sieve is a public battery of four null tests with a frozen observable list and grammar. The first asks whether a relation is isolated in the fixed vocabulary; the second prices the freedom to have chosen the vocabulary; the third and fourth shuffle coefficients and targets. Its published scorecard for the K₇ relations reads:

- n_s and m_H/m_W pass the isolation test on all three of its axes.
- Neither passes the vocabulary-freedom test: a budget-matched invented vocabulary matches them as well (for m_H/m_W, 22 of 24 invented vocabularies do).
- Q_Koide is isolated in the fixed vocabulary, but its value 2/3 is reached by every vocabulary: a tie, not a survivor.
- Across the nine shallow relations submitted to the vocabulary-freedom test, the invented-vocabulary envelope is beaten 0 times out of 9.

What that test cannot price is where the vocabulary comes from: the K₇ constants are E₈ dimensions and ranks and the Betti numbers, not an invented list. That is a fact about the origin of the constants, not evidence that they were selected before the data were known.

## 5. What the test does not cover, and its history

The test does not vary the gauge group or the holonomy beyond the Betti numbers, does not consider other forms of an observable (an angle against its sine squared) except for the unit of δ_CP, and does not look beyond five nodes, where several of K₇'s formulas lie. These freedoms stay in the residue register of the main paper (formula assignment, grammar, unit).

The preregistration was amended three times, each time after an external review and without changing the question, families, grammar, budget, seed or verdict rule: the dataset was refreshed and the windows made two-sided (2026-10-22), then the windows of the six Planck density ratios were recomputed on the published chains and the control was added (2026-11-03), and finally the window of m_W/m_Z was computed from the published masses, as for the other mass ratios (2026-11-11).

{history}

## 6. What earlier versions of this page reported

Earlier versions of this page presented the following as statistical evidence. Each is withdrawn.

- **"#1 among 3,070,396 configurations", "0 better alternatives", null-model p < 2 × 10⁻⁵.** These came from a search in which the alternatives were scored with K₇'s own formulas and did not search for theirs. Since the formulas had been chosen for (21, 77), (21, 77) won by construction. An earlier blind sweep over 242,064 Betti pairs had already found (21, 77) below the median ([Program, selection principle, Q-B]({qb})).
- **"P < 5 × 10⁻⁶ among 192 349 configurations" (version 3.5).** Same design; 1/192 349 was the floor of the estimator. Withdrawn.
- **Coincidence probabilities 10⁻³⁴⁶, 10⁻¹³⁸ and 10⁻¹³³ (versions 3.3 and 3.4).** The uniform null treats predictions as random numbers, which no formula search produces; the algebraic null compares selected formulas with random ones and so does not price the selection. Withdrawn.
- **Mean deviation (0.21%, 0.24%, 0.39%, 0.73%, 0.99% across versions).** A mean deviation measures closeness, which the test above shows is not distinctive, and it hid the relations outside 2σ. Withdrawn; the [Validation Summary](Validation-Summary.html) gives the five classes instead.
- **Bayes factors, Westfall–Young and held-out tests of the 3.3 report.** They were computed on the 3.3 dataset under the same fixed-formula design and have not been recomputed. Withdrawn as evidence.
- **"Overdetermination ratio 2.13" and related diagnostics (version 3.5).** They describe how the formulas use the constants; they cannot tell a fitted formula from an unfitted one. Kept in S4.3 as archived description.

The scripts and reports behind the withdrawn figures are kept, unmaintained, in the [version 3.3 archive]({legacy}) as a record of what was reported.

## 7. What remains

Two things survive the look-elsewhere tests, and the paper rests on them rather than on closeness: **rigidity under a fixed dictionary** (no relation has a continuous parameter, so a single measurement can reject it under the decision rule of the main paper, §11) and **the declared residue** (what was set rather than derived is written down, §3.3).

## 8. Reproducibility

The producer, the dataset as read by the run, the preregistration with its three amendments, the result and the results of the three earlier runs are in [`publications/validation/v3.6/`]({lee}), with their hashes and the command to rerun the test. Supplement [S4]({s4}), section S4.5, gives the pinned inputs (Sieve engine commit, grammar hash, seed).
""".format(main=MAIN, s4=S4, s3=S3, qb=QB, legacy=LEGACY, lee=LEE, **t)


def stat_fr(t):
    return """# Éléments statistiques : le test look-elsewhere

**Version du cadre** : 3.6. **Source** : article principal [§7]({main}) et supplément [S4]({s4}) ; les tables de cette page sont copiées de S4 par un script, sans retouche à la main.

Un cadre qui retrouve 33 valeurs mesurées par des formes closes, avec un vocabulaire de vingt constantes, doit d'abord répondre à une question : combien de fois la même grammaire, avec un autre vocabulaire, les aurait-elle retrouvées aussi bien ? La version 3.6 a posé cette question par un test préenregistré. La réponse est que **la proximité avec les valeurs mesurées ne distingue pas K₇** dans les classes de référence testées. Les affirmations statistiques des versions précédentes de cette page sont retirées ; la section 6 les énumère.

---

## 1. Résumé

| | |
|---|---|
| **Question** | K₇ reste-t-il exceptionnel quand chaque concurrent cherche ses propres formules, dans la même grammaire, avec le même budget et la même liberté d'attribution et d'unité ? |
| **Préenregistré** | le 2026-10-17, avant tout passage complet (un pilote de neuf vocabulaires, déclaré dans la préinscription, avait tourné d'abord), avec deux issues seulement : une valeur p globale calibrée, ou aucune valeur p dans le texte |
| **K₇** | atteint 31 des 33 cibles |
| **Paires de Betti alternatives** | 1 085 sur 4 159 en atteignent autant (26 %) ; aucune n'en atteint plus |
| **Vocabulaires inventés** | 1 015 sur 2 000 en atteignent autant (51 %) ; aucun n'en atteint plus |
| **Contrôle sans constante de K₇** | atteint 30 des 33 avec les seules feuilles universelles de la grammaire |
| **Issue** | le seuil préenregistré n'est pas atteint : l'effet look-elsewhere n'est pas surmonté, et aucune valeur p n'est rapportée ; les proportions ci-dessus sont descriptives |

Ces proportions ne sont pas la probabilité que K₇ soit juste ou faux, et ces comptes ne sont pas une réfutation physique. Ils disent que le meilleur score discrimine peu dans ce protocole : 30 cibles sont atteintes par tous, deux par personne, et une seule sépare les concurrents.

## 2. Le test

- **Cibles.** Les 33 relations du jeu de données ([S3]({s3})), avec leurs valeurs mesurées et leurs incertitudes.
- **Grammaire.** Le moteur gelé du Sieve : ses feuilles universelles (1 à 9, π, e, φ, γ, ln 2, ζ(3) à ζ(11)) plus les 19 constantes entières du concurrent, les opérations + − × / ^, racine carrée, inverse, carré et logarithme, et **cinq nœuds au plus** par expression.
- **Concordance.** Une cible est atteinte si une expression du vocabulaire tombe à moins de 2σ de la valeur mesurée, de part et d'autre, les incertitudes asymétriques restant asymétriques. Pour m_s/m_d, que le PDG donne comme un intervalle, la fenêtre est cet intervalle. Pour δ_CP, la phase peut être lue en degrés, radians, grades ou tours.
- **Attribution.** La recherche est aveugle : chaque cible reçoit l'expression concordante la moins coûteuse. La liberté d'attribuer les formules aux observables est donnée à tous, K₇ compris, qui est noté par la même recherche sur son propre vocabulaire et non par ses formules publiées.
- **Concurrents.** Toute paire de Betti avec b₂ dans [1, 40] et b₃ dans [17, 120] autre que (21, 77), avec H*, κ_T⁻¹ et det(g) re-dérivés et les autres constantes gardées aux valeurs de K₇ ; et 2 000 vocabulaires de 19 entiers tirés par le générateur gelé du Sieve.
- **Règle de verdict.** Pour une famille de taille N où n concurrents atteignent au moins autant de cibles que K₇, la statistique de décision est (1 + n)/(1 + N), les égalités comptant contre K₇. La plus grande des deux valeurs est comparée à 0,01 : à ce seuil ou en dessous, une valeur p globale calibrée est rapportée ; au-dessus, aucune ne l'est, et les proportions sont données à titre descriptif. Les valeurs de la statistique sont dans le fichier de résultat déposé.

L'alphabet testé pour K₇ est celui des dix-neuf entiers du registre Monte Carlo de la version 3.5, et non littéralement les vingt constantes de l'article principal (§3.1) : dim E₇ = 133 et α_sum = 13 en sont absents, κ_T⁻¹ = 61 y figure. Un test sur le registre littéral serait un autre calcul.

## 3. Résultat

{families}

Le seuil n'est atteint dans aucune des deux premières lignes. La ligne de la variante n'entre pas dans le verdict. K₇ n'est pas moins coûteux non plus : son coût de description se situe dans l'étendue des deux familles.

Par cible :

{targets}

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

{history}

## 6. Ce que disaient les versions précédentes de cette page

Les versions précédentes de cette page présentaient les éléments suivants comme des preuves statistiques. Chacun est retiré.

- **« N° 1 parmi 3 070 396 configurations », « 0 meilleure alternative », valeur p du modèle nul < 2 × 10⁻⁵.** Ils venaient d'une recherche où les alternatives étaient notées avec les formules de K₇ et ne cherchaient pas les leurs. Les formules ayant été choisies pour (21, 77), (21, 77) gagnait par construction. Un balayage aveugle antérieur de 242 064 paires de Betti avait déjà trouvé (21, 77) sous la médiane ([Program, principe de sélection, Q-B]({qb})).
- **« P < 5 × 10⁻⁶ parmi 192 349 configurations » (version 3.5).** Même protocole ; 1/192 349 était le plancher de l'estimateur. Retiré.
- **Probabilités de coïncidence 10⁻³⁴⁶, 10⁻¹³⁸ et 10⁻¹³³ (versions 3.3 et 3.4).** Le modèle nul uniforme traite les prédictions comme des nombres aléatoires, ce qu'aucune recherche de formules ne produit ; le modèle nul algébrique compare des formules choisies à des formules aléatoires et ne chiffre donc pas le choix. Retirées.
- **Écart moyen (0,21 %, 0,24 %, 0,39 %, 0,73 %, 0,99 % selon les versions).** Un écart moyen mesure la proximité, dont le test ci-dessus montre qu'elle n'est pas distinctive, et il masquait les relations au-delà de 2σ. Retiré ; le [bilan de validation](Validation-Summary.fr.html) donne les cinq classes à la place.
- **Facteurs de Bayes, Westfall–Young et tests hors échantillon du rapport 3.3.** Calculés sur les données de la 3.3 avec le même protocole à formules fixées, ils n'ont pas été recalculés. Retirés comme preuves.
- **« Rapport de surdétermination 2,13 » et diagnostics voisins (version 3.5).** Ils décrivent l'usage que les formules font des constantes ; ils ne distinguent pas une formule ajustée d'une formule qui ne l'est pas. Gardés en S4.3 comme description archivée.

Les scripts et rapports derrière les chiffres retirés sont conservés, sans maintenance, dans l'[archive de la version 3.3]({legacy}), comme trace de ce qui a été publié.

## 7. Ce qui reste

Deux choses survivent aux tests look-elsewhere, et l'article s'appuie sur elles plutôt que sur la proximité : **la rigidité sous un dictionnaire fixé** (aucune relation n'a de paramètre continu, une seule mesure peut donc la rejeter selon la règle de décision de l'article principal, §11) et **le résidu déclaré** (ce qui a été posé plutôt que dérivé est écrit, §3.3).

## 8. Reproductibilité

Le producteur, le jeu de données lu par le passage, le préenregistrement et ses trois amendements, le résultat et ceux des trois passages antérieurs sont dans [`publications/validation/v3.6/`]({lee}), avec leurs empreintes et la commande pour relancer le test. Le supplément [S4]({s4}), section S4.5, donne les entrées épinglées (commit du moteur du Sieve, empreinte de la grammaire, graine).
""".format(main=MAIN, s4=S4, s3=S3, qb=QB, legacy=LEGACY, lee=LEE, **t)


def valid_en(t):
    return """# Validation Summary: the 33 Relations against Current Data

**Framework version**: 3.6. **Source**: main paper [§4]({main}) and supplement [S3]({s3}); the tables on this page are copied from the paper by a script.

**Data.** PDG 2026 for particle data, NuFIT 6.1 for neutrino mixing (normal ordering, with atmospheric data), Planck 2018 for cosmology (TT,TE,EE+lowE+lensing, one column), CODATA 2022 for α and m_μ/m_e. All uncertainties are brought to 1σ. Correlations are neglected, except in the Planck density ratios, which are computed on the published chains. The pull is (K₇ − measured)/σ with the experimental uncertainty alone: the framework supplies no theoretical uncertainty.

---

## 1. Five classes, not one score

{classes}

Earlier versions summarised the comparison by a mean deviation. That summary is withdrawn: it hid the relations outside 2σ, and a mean deviation measures closeness, which the [look-elsewhere test](Statistical-Evidence.html) shows is not distinctive.

## 2. The table

{table}

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
| D1 | the phase e^{{iδ_CP}}, δ_CP = 2π·197/360 | 197° | a global fit of the reference series, including DUNE or Hyper-Kamiokande, whose 3σ interval excludes 197° | the δ_CP relation and the unit assignment that produced it |
| D2 | sin²θ₂₃ (PMNS) | 6/11 = 0.5455 | a global fit whose 3σ interval excludes 6/11, in either octant | the θ₂₃ relation |
| D3 | m_τ/m_e and Q_Koide | 1776.74 MeV and 1776.97 MeV for m_τ | a value of m_τ whose 3σ interval excludes the value | each excluded relation, separately |
| D4 | N_gen | 3 | a fourth sequential generation | the integer identity, as a consistency check |
| D5 | m_s/m_d | 20 | a lattice determination adopted by the reference series, with an uncertainty whose 3σ interval excludes 20 | the m_s/m_d relation |

Two contradicting measurements outside the reference series are reported beside their class: h = 167/248 agrees with Planck (0.0σ) and is excluded by the SH0ES distance ladder at 5.5σ; the density relations agree with Planck and are strained by the baryon acoustic oscillations of DESI (second data release, arXiv:2503.14738): in flat ΛCDM, DESI alone gives Ω_m = 0.2975 ± 0.0086, which puts Ω_Λ/Ω_m = 113/52 at −1.9σ, Ω_m/Ω_Λ = 28/61 at +2.0σ and Ω_DE at −1.9σ; DESI combined with the cosmic microwave background gives Ω_m = 0.3027 ± 0.0036 and H₀ = 68.17 ± 0.28, which puts them at −3.3σ, +3.4σ and −3.1σ, and h at −3.0σ. While methods keep disagreeing, the status is stated both ways, and neither agreement counts as a confirmation.

Under the same rule, the next sharp test is sin²θ₁₂ = 4/13 = 0.3077: JUNO's first measurement is 0.3092 ± 0.0087 (arXiv:2511.14593), and after six years its uncertainty should be about four times smaller than that of today's global fit.

## 7. What is verified, and what is not

The arithmetic of the 33 relations is machine-checked in Lean 4 (K7-Lean, `relations_v36_certified`): given the declared integers, each closed form evaluates to the stated number. This does not establish the existence of K₇, the physical interpretation of any relation, or the choice of assignments. No compact torsion-free G₂ manifold with Betti numbers (21, 77) is currently constructed.
""".format(main=MAIN, s3=S3, **t)


def valid_fr(t):
    return """# Bilan de validation : les 33 relations face aux données actuelles

**Version du cadre** : 3.6. **Source** : article principal [§4]({main}) et supplément [S3]({s3}) ; les tables de cette page sont copiées de l'article par un script.

**Données.** PDG 2026 pour les particules, NuFIT 6.1 pour le mélange des neutrinos (ordre normal, avec les données atmosphériques), Planck 2018 pour la cosmologie (TT,TE,EE+lowE+lensing, une seule colonne), CODATA 2022 pour α et m_μ/m_e. Toutes les incertitudes sont ramenées à 1σ. Les corrélations sont négligées, sauf dans les rapports de densité de Planck, calculés sur les chaînes publiées. L'écart normalisé est (K₇ − mesure)/σ avec la seule incertitude expérimentale : le cadre ne fournit pas d'incertitude théorique.

---

## 1. Cinq classes, pas un score

{classes}

Les versions précédentes résumaient la comparaison par un écart moyen. Ce résumé est retiré : il masquait les relations au-delà de 2σ, et un écart moyen mesure la proximité, dont le [test look-elsewhere](Statistical-Evidence.fr.html) montre qu'elle n'est pas distinctive.

## 2. La table

{table}

**Vocabulaire des statuts.** *entier* : un rapport d'entiers structurels. *algébrique, φ, ln 2, valeurs de ζ* : la formule utilise l'opération correspondante. *det(g)*, *κ_T* : la formule utilise la normalisation imposée det(g) = 65/32 ou la combinaison κ_T⁻¹ = 61. *tension* : entre 2σ et 3σ, ou un écart dont la lecture est elle-même ambiguë (θ₂₃). *proximité* : au-delà de 3σ ; la relation est exclue comme égalité exacte et gardée comme proximité numérique. *approchée* : l'une de plusieurs relations mutuellement incompatibles dans un secteur surdéterminé, dont aucune n'est choisie. *assignation d'unité* : la prédiction dépend d'une unité choisie par le dictionnaire. L'astérisque de sin²θ₂₃ signale un profil non gaussien : l'écart gaussien surestime la tension.

## 3. Ce que montre la table

- **Six proximités sont déjà rejetées comme égalités exactes.** α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ et m_W/m_Z se comparent à des quantités mesurées entre 10⁻¹⁰ et quelques 10⁻⁴ (m_W/m_Z = 37/42 est à 3,8σ du rapport des masses publiées) ; m_b/m_t est à 1,8 % du rapport dans le schéma de masse déclaré, et n'est pas sauvée par une lecture dans un autre schéma.
- **Les 33 relations ne sont pas 33 tests indépendants.** Trois secteurs sont surdéterminés, et dans chacun les relations se contredisent en tant qu'égalités exactes : quatre relations leptoniques portent sur deux rapports de masses ; trois relations CKM sur deux paramètres de Wolfenstein (sin θ₂₃ = Aλ², 2,6 % d'écart) ; sept relations de densité sur deux densités indépendantes. L'audit complet des dépendances entre les 33 n'a pas été fait : aucun compte de quantités indépendantes n'est donné.
- **La plupart des 23 ne sont testées que faiblement.** Pour les rapports de masses des quarks, les paramètres de mélange et les rapports cosmologiques, les incertitudes expérimentales sont de l'ordre du pour cent, et un accord au pour cent est ce qu'un vocabulaire riche atteint facilement.
- **sin²θ₂₃ = 6/11.** NuFIT 6.1 préfère le premier octant ; l'ajustement garde une branche dans le second, et son intervalle à 3σ (0,435 à 0,584) contient 6/11. La relation est en tension avec l'octant préféré.
- **δ_CP.** La structure produit l'entier 197. Le lire en degrés est un choix du dictionnaire, consigné au registre des résidus et compté dans le test look-elsewhere.
- **Ω_c/Ω_m.** Le Ω_m de Planck inclut les neutrinos, de sorte que Ω_b/Ω_m + Ω_c/Ω_m = 0,9955, alors que 5/32 + 27/32 = 1 : les deux formules ne sont pas compatibles avec cette définition de la matière totale.

## 4. Avec et sans la normalisation imposée

Six relations utilisent det(g) = 65/32 (λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈) et trois utilisent κ_T⁻¹ = 61 (α⁻¹, Y_p, Ω_m/Ω_Λ). Sans les six relations à det(g), il en reste 27, dont 19 à moins de 2σ ; sans les huit qui utilisent l'une ou l'autre, il en reste 25, dont 17 à moins de 2σ. Un lecteur qui tient la normalisation imposée pour un paramètre supplémentaire doit lire le cadre avec ces comptes réduits.

## 5. Les 62 autres entrées du jeu de données

Le jeu de données contient 62 autres entrées, que la version 3.6 ne compte pas comme prédictions : 19 quantités dimensionnées ou composites (type II), dont plusieurs sont des nombres lus dans une unité choisie et huit des valeurs héritées dont la dérivation n'est pas documentée ; 21 sorties de mécanismes qui consomment des choix de calibration déclarés (type III) ; et 22 diagnostics structurels sans contrepartie expérimentale (type IV). Elles sont gardées dans S3 pour la traçabilité. Le pont d'échelle et les prédictions dimensionnées des versions précédentes de cette page relèvent de ces entrées.

## 6. Règle de décision

Les relations sont énoncées comme des égalités exactes, sans incertitude théorique. Une relation est rejetée quand sa série de référence exclut sa valeur à 3σ ; après rejet, elle ne peut être gardée que comme proximité numérique, sans prétention prédictive. La règle n'a pas de clause de réparation (article principal, §11).

| # | Quantité | Valeur K₇ | Condition de rejet | Ce qui est rejeté |
|---|----------|----------|---------------------|------------------|
| D1 | la phase e^{{iδ_CP}}, δ_CP = 2π·197/360 | 197° | un ajustement global de la série de référence, incluant DUNE ou Hyper-Kamiokande, dont l'intervalle à 3σ exclut 197° | la relation δ_CP et l'assignation d'unité qui l'a produite |
| D2 | sin²θ₂₃ (PMNS) | 6/11 = 0,5455 | un ajustement global dont l'intervalle à 3σ exclut 6/11, dans l'un ou l'autre octant | la relation θ₂₃ |
| D3 | m_τ/m_e et Q_Koide | 1776,74 MeV et 1776,97 MeV pour m_τ | une valeur de m_τ dont l'intervalle à 3σ exclut la valeur | chaque relation exclue, séparément |
| D4 | N_gen | 3 | une quatrième génération séquentielle | l'identité entière, comme contrôle de cohérence |
| D5 | m_s/m_d | 20 | une détermination sur réseau adoptée par la série de référence, avec une incertitude dont l'intervalle à 3σ exclut 20 | la relation m_s/m_d |

Deux mesures contradictoires, hors des séries de référence, sont rapportées à côté de leur classe : h = 167/248 s'accorde avec Planck (0,0σ) et est exclu par l'échelle des distances SH0ES à 5,5σ ; les relations de densité s'accordent avec Planck et sont mises sous tension par les oscillations acoustiques de baryons de DESI (deuxième livraison de données, arXiv:2503.14738) : en ΛCDM plat, DESI seul donne Ω_m = 0,2975 ± 0,0086, ce qui place Ω_Λ/Ω_m = 113/52 à −1,9σ, Ω_m/Ω_Λ = 28/61 à +2,0σ et Ω_DE à −1,9σ ; DESI combiné au fond diffus cosmologique donne Ω_m = 0,3027 ± 0,0036 et H₀ = 68,17 ± 0,28, ce qui les place à −3,3σ, +3,4σ et −3,1σ, et h à −3,0σ. Tant que les méthodes divergent, le statut est donné des deux façons, et aucun des deux accords ne vaut confirmation.

Sous la même règle, le prochain test serré est sin²θ₁₂ = 4/13 = 0,3077 : la première mesure de JUNO donne 0,3092 ± 0,0087 (arXiv:2511.14593), et après six ans son incertitude devrait être environ quatre fois plus petite que celle de l'ajustement global actuel.

## 7. Ce qui est vérifié, et ce qui ne l'est pas

L'arithmétique des 33 relations est vérifiée par machine en Lean 4 (K7-Lean, `relations_v36_certified`) : étant donné les entiers déclarés, chaque forme close s'évalue au nombre annoncé. Cela n'établit ni l'existence de K₇, ni l'interprétation physique d'une relation, ni le choix des attributions. Aucune variété G₂ compacte sans torsion de nombres de Betti (21, 77) n'est construite à ce jour.
""".format(main=MAIN, s3=S3, **t)


def obs_en(t):
    return """# Observable Reference

**Framework version**: 3.6. **Source**: main paper [§3–§4]({main}) and supplement [S3]({s3}); every table on this page is copied from the paper by a script. Machine-readable data: [`observables.csv`]({csv}) (95 entries).

The dataset has 95 entries. **33 are relations** compared with measurement and counted in the main paper; **62 are conditional extractions and diagnostics**, kept for traceability and not counted as predictions. Earlier versions of this page counted all 95 as observables predicted by the framework and summarised them by a mean deviation; both are withdrawn.

---

## 1. Types

{types}

## 2. The structural constants

All 33 relations are written in twenty structural constants. Seven are primitive; thirteen are derived from them, and the derivation is part of the dictionary.

{constants}

N_gen = 3 is an integer identity (b₂/dim K₇), not the output of an index theorem. b₂ and b₃ are inputs posited by the framework, not quantities confirmed by a computation: no compact G₂ manifold with (21, 77) is currently constructed.

## 3. The 33 relations

Formulas, values and status. Data: PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022; uncertainties at 1σ. The pull is (K₇ − measured)/σ with the experimental uncertainty alone.

{table}

The classes, the overdetermined sectors and the decision rule are on the [Validation Summary](Validation-Summary.html). How distinctive the agreement is: [Statistical Evidence](Statistical-Evidence.html).

### Reference data and conventions

{type1}

## 4. The 62 conditional and diagnostic entries

"Reference value" is the measured value where one exists, otherwise the mathematical expectation the entry is compared with, otherwise n/a. None of these entries is counted as a prediction.

{type24}

{inherited}

## 5. Lean cross-references

The arithmetic of each of the 33 relations is machine-checked in Lean 4 (Arithmon/K7-Lean, aggregate `relations_v36_certified`). The formalization verifies that each closed form evaluates to the stated number; it does not establish the physical content of a relation or the choice of assignments.

{lean}
""".format(main=MAIN, s3=S3, csv=GH + "publications/references/observables.csv", **t)


def obs_fr(t):
    return """# Référence des observables

**Version du cadre** : 3.6. **Source** : article principal [§3–§4]({main}) et supplément [S3]({s3}) ; toutes les tables de cette page sont copiées de l'article par un script. Données lisibles par machine : [`observables.csv`]({csv}) (95 entrées).

Le jeu de données a 95 entrées. **33 sont des relations** comparées à la mesure et comptées dans l'article principal ; **62 sont des extractions conditionnelles et des diagnostics**, gardés pour la traçabilité et non comptés comme prédictions. Les versions précédentes de cette page comptaient les 95 comme observables prédites par le cadre et les résumaient par un écart moyen ; les deux sont retirés.

Les tables des sections 1, 2, 4 et 5 et la table des données de référence sont reprises telles quelles de l'article, en anglais.

---

## 1. Types

{types}

## 2. Les constantes structurelles

Les 33 relations sont toutes écrites avec vingt constantes structurelles. Sept sont primitives ; treize en sont dérivées, et cette dérivation fait partie du dictionnaire.

{constants}

N_gen = 3 est une identité entière (b₂/dim K₇), pas le résultat d'un théorème de l'indice. b₂ et b₃ sont des entrées posées par le cadre, pas des quantités confirmées par un calcul : aucune variété G₂ compacte de nombres (21, 77) n'est construite à ce jour.

## 3. Les 33 relations

Formules, valeurs et statut. Données : PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022 ; incertitudes à 1σ. L'écart normalisé est (K₇ − mesure)/σ avec la seule incertitude expérimentale.

{table_fr}

Les classes, les secteurs surdéterminés et la règle de décision sont dans le [bilan de validation](Validation-Summary.fr.html). L'accord est-il distinctif : [éléments statistiques](Statistical-Evidence.fr.html).

### Données de référence et conventions

{type1}

## 4. Les 62 entrées conditionnelles et diagnostiques

« Reference value » est la valeur mesurée quand il y en a une, sinon l'attendu mathématique auquel l'entrée est comparée, sinon n/a. Aucune de ces entrées n'est comptée comme prédiction.

{type24}

{inherited_fr}

## 5. Renvois Lean

L'arithmétique de chacune des 33 relations est vérifiée par machine en Lean 4 (Arithmon/K7-Lean, agrégat `relations_v36_certified`). La formalisation vérifie que chaque forme close s'évalue au nombre annoncé ; elle n'établit ni le contenu physique d'une relation ni le choix des attributions.

{lean}
""".format(main=MAIN, s3=S3, csv=GH + "publications/references/observables.csv", **t)


def front(title):
    return '---\ntitle: "%s"\nlayout: default\n---\n\n' % title


FOOT_EN = "\n---\n\n*The K₇ Framework v3.6 | generated from the paper sources by `k7_v3_6_surface_pages.py`*\n"
FOOT_FR = "\n---\n\n*K₇ Framework v3.6 | page générée depuis les sources de l'article par `k7_v3_6_surface_pages.py`*\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k7", default=os.environ.get("K7_DIR", K7_DEFAULT))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    s4 = read("supplement_sieve_diagnostics.md")
    main_md = read("physics_main.md")
    en = dict(families=only_table(block(s4, "S4-LEE-FAMILIES")),
              targets=block(s4, "S4-LEE-TARGETS"),
              history=block(s4, "S4-LEE-HISTORY"),
              table=table_after(main_md, "### 4.1 Table"),
              classes=table_after(main_md, "**The breakdown of the 33.**"))
    fr = {k: fr_table(v) for k, v in en.items()}
    s3 = read("supplement_observables.md")
    obs = dict(types=table_after(s3, "## S3.2 Type classification"),
               constants=table_after(main_md, "### 3.1 The structural constants"),
               table=en["table"], table_fr=fr["table"],
               type1=only_table(block(s3, "S3-TYPE-I")),
               type24=only_table(block(s3, "S3-TYPE-II-IV")),
               lean=only_table(block(s3, "S3-LEAN")))
    # la note de S3.6 sur les quatre libellés hérités (D01, D02, D06, D07) : lue dans S3, jamais recopiée
    inh = [l for l in s3.splitlines() if l.startswith("Four labels of the dataset are inherited")]
    assert len(inh) == 1 and "TCS K₇" in inh[0] and "1.35 × 10⁻⁷" in inh[0] and "1.43 × 10⁻⁹" in inh[0], "S3.6 : note des libellés hérités absente"
    obs["inherited"] = inh[0].replace("main ref. [A]", "companion paper A")
    obs["inherited_fr"] = (
        "Quatre libellés du jeu de données sont hérités des versions antérieures, et sont gardés pour que le jeu de "
        "données reste identique, octet pour octet, au fichier lu par le test look-elsewhere (S4). D01 et D02 portent "
        "le libellé de formule « TCS K₇ » : la version 3.6 pose (21, 77) et ne suppose aucune construction en somme "
        "connexe tordue, et toute somme connexe tordue ordinaire est exclue (main §2.3). D06 écrit le paramètre de "
        "contraction β×η×γ ; le certificat publié l'écrit h = βηω, et 8.95 × 10⁻⁹ en est la valeur analytique. D07 est "
        "la boule de contraction d'un calcul de certification antérieur (`g9_certification_results.json`) ; le "
        "certificat publié donne δg/g ≤ 1.35 × 10⁻⁷, avec la valeur numérique h = 1.43 × 10⁻⁹ (papier compagnon A, "
        "proposition 1.1 et §5.6).")

    pages = {
        "docs/wiki/Statistical-Evidence.md": front("Statistical Evidence") + stat_en(en) + FOOT_EN,
        "docs/wiki/Statistical-Evidence.fr.md": front("Éléments statistiques") + stat_fr(fr) + FOOT_FR,
        "publications/references/STATISTICAL_EVIDENCE.md":
            (stat_en(en) + FOOT_EN).replace("](Validation-Summary.html)", "](../../docs/wiki/Validation-Summary.md)"),
        "docs/wiki/Validation-Summary.md": front("Validation Summary") + valid_en(en) + FOOT_EN,
        "docs/wiki/Validation-Summary.fr.md": front("Bilan de validation") + valid_fr(fr) + FOOT_FR,
        "docs/wiki/Observable-Reference.md": front("Observable Reference") + obs_en(obs) + FOOT_EN,
        "docs/wiki/Observable-Reference.fr.md": front("Référence des observables") + obs_fr(obs) + FOOT_FR,
        "publications/references/OBSERVABLE_REFERENCE.md":
            (obs_en(obs) + FOOT_EN).replace("](Validation-Summary.html)", "](../../docs/wiki/Validation-Summary.md)")
            .replace("](Statistical-Evidence.html)", "](STATISTICAL_EVIDENCE.md)"),
    }
    # FAQ : une source par langue, deux copies (docs/ et docs/wiki/)
    pages["docs/FAQ.md"] = "---\ntitle: FAQ\n---\n\n" + faq("en", "wiki/")
    pages["docs/FAQ.fr.md"] = "---\ntitle: FAQ\n---\n\n" + faq("fr", "wiki/")
    pages["docs/wiki/FAQ.md"] = front("FAQ") + faq("en", "")
    pages["docs/wiki/FAQ.fr.md"] = front("FAQ") + faq("fr", "")
    pages["docs/GIFT_EXEC_SUMMARY.md"] = exec_summary("en")
    pages["docs/GIFT_EXEC_SUMMARY.fr.md"] = exec_summary("fr")
    pages["docs/wiki/For-Physicists.md"] = front("For Physicists") + for_physicists()
    pages["docs/INFO_GEO_FOR_PHYSICISTS.md"] = ("---\ntitle: K₇ for Physicists\n---\n\n" + for_physicists()
        ).replace("](Observable-Reference.html)", "](wiki/Observable-Reference.html)"
        ).replace("](Validation-Summary.html)", "](wiki/Validation-Summary.html)"
        ).replace("](Statistical-Evidence.html)", "](wiki/Statistical-Evidence.html)")
    # le CSV du jeu de données : copie conforme de canonical/data/observables.csv
    pages["publications/references/observables.csv"] = open(
        os.path.join(ROOT, "canonical", "data", "observables.csv"), encoding="utf-8").read()
    bad = 0
    for rel, text in pages.items():
        path = os.path.join(args.k7, rel)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if old == text:
            print("identique  %s" % rel)
        elif args.check:
            print("DIFFÈRE    %s" % rel)
            bad += 1
        else:
            open(path, "w", encoding="utf-8").write(text)
            print("écrit      %s (%d lignes)" % (rel, text.count("\n")))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
