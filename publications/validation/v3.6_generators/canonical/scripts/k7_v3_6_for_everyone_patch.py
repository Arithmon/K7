#!/usr/bin/env python3
"""k7_v3_6_for_everyone_patch.py -- « K₇ for Everyone » au cadrage 3.6.

Le guide (1 180 lignes d'analogies) n'est pas réécrit : seuls les passages qui
contredisent la 3.6 sont remplacés, à l'identique dans docs/ et docs/wiki/, en
anglais et en français. Chaque remplacement doit se trouver exactement une
fois par fichier (assert) ; le script est donc à usage unique par fichier
(un second passage échoue sur le premier motif, sans rien écrire).

Usage : k7_v3_6_for_everyone_patch.py <K7>/docs
"""
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

EN = [
("""**The core idea in one sentence**: The universe has 7 hidden dimensions curled up in a specific shape called K₇, and the properties of this shape mathematically determine everything we measure.""",
 """**The core idea in one sentence**: Suppose the universe has 7 hidden dimensions curled up in a specific shape called K₇. Then 33 of the numbers we measure can be written as simple formulas in the properties of that shape.

**What kind of claim this is (version 3.6).** It is a *dictionary*, not a derivation. Nobody knows a mechanism that goes from the shape to the numbers: the formulas were matched to the measurements, and the framework says so. The shape itself has not been constructed. This guide explains the ideas; whenever it says "in K₇", read "in the dictionary that K₇ proposes"."""),
("""K₇ proposes answers: **zero free parameters**. Everything comes from geometry.""",
 """K₇ proposes a dictionary in which no formula has a dial to turn: the numbers are ratios of whole numbers. What it does not have is a reason why *these* formulas go with *these* measurements. That gap is written down, not hidden."""),
("""**In K₇**: Everything flows from K₇. It's THE shape of the hidden universe.""",
 """**In K₇**: Every formula of the dictionary is written with the numbers of this shape. Whether such a shape exists with exactly 21 and 77 holes is an open mathematical question: nobody has built it yet."""),
("""and CP phase (δ = 197°) are derived from topology.""",
 """and CP phase (δ = 197°) are written as ratios of the shape's numbers. For the phase, the shape gives the whole number 197; reading it in degrees is a choice."""),
("""**In K₇**: Quark mass ratios like m_s/m_d = 20 are derived from topology.""",
 """**In K₇**: Quark mass ratios like m_s/m_d = 20 are written as products of the shape's numbers."""),
("""**K₇'s claim**: it's not magic. `α⁻¹ = 137.033` emerges from the topology of K₇, as `128 + 9 + correction`, where `128 = 2⁷` (the 7 hidden dimensions of K₇) and `9 = 99/11` (a ratio of topological invariants). Feynman's "great damn mystery" becomes a **consequence of shape**.""",
 """**K₇'s formula**: `α⁻¹ = 137.033`, written as `128 + 9 + correction`, where `128 = 2⁷` and `9 = 99/11` (a ratio of the shape's numbers). It is close, and it is not right: α is measured to ten decimal places, and 137.033 is not 137.036. The framework keeps this formula as a *proximity*, a near miss, and no longer claims it as an exact result. Feynman's mystery stands."""),
("""**In K₇**: The cocktail recipe isn't arbitrary, it's dictated by the shape of the cosmic shaker (K₇).""",
 """**In K₇**: The recipe 3/13 = 0.2308 comes close to the measured 0.2312. But this number is measured so precisely that the small gap is seven times the uncertainty: as an exact equality the formula is rejected, and the framework keeps it only as a near miss."""),
("""**In K₇**: This troubling coincidence becomes a logical consequence.""",
 """**In K₇**: The dictionary writes 2/3 as a ratio of two numbers of the shape, and the measurement agrees. Honesty requires a footnote: 2/3 is such a simple fraction that almost any list of numbers can produce it, so this agreement is not evidence that the shape is right."""),
("""It's like asking "Why does a cube have 6 faces?" The answer isn't "just because," it's "because it's a cube." The shape imposes the number.

**In K₇**: The number of families isn't an accident, it's a geometric consequence.""",
 """**In K₇**: The number 3 comes out as a division of two whole numbers of the dictionary. It is an arithmetic identity, a consistency check; it is not a proof that nature must have three families."""),
("""### Zero Free Parameters

**The fancy word**: Theory without adjustable constants.

**The kitchen table version**: IKEA vs Custom-made.

- **The Standard Model** = Custom furniture. The carpenter takes 19 measurements at your place and builds furniture that fits perfectly. But he can't explain *why* your living room has those dimensions.

- **K₇** = Universal IKEA furniture. The instructions say: "Take a 7-dimensional diabolo with G₂ holonomy." There's only one way to assemble it. The dimensions come out automatically.

**In K₇**: 19 mysterious numbers → 0 mysterious numbers. Everything comes from the shape.""",
 """### Zero Free Parameters

**The fancy word**: No continuously adjustable constant; and a register of everything that was chosen.

**The kitchen table version**: Lego vs modelling clay.

- **Modelling clay** can be squeezed to fit any mould. A theory with adjustable dials is like that: turn the dial, match the measurement.

- **Lego bricks** cannot be squeezed. A formula like 3/13 is a Lego brick: you cannot nudge it by 1%. If the measurement moves away, the formula is simply wrong.

K₇'s formulas are Lego bricks. But somebody still chose *which bricks to use and where to put them*. With a big enough box of bricks, you can build something close to almost any shape. So "no dials" is not the same as "nothing was chosen".

**In K₇**: No dials, and a written list (the *residue register*) of every choice that was made: the two numbers 21 and 77, the formulas themselves, a normalization, and the unit in which 197 is read."""),
("""- If DUNE finds 197° ± 5° → K₇ survives
- If DUNE finds 250° → K₇ is dead. Done. We move on.

**That's science**: predictions that can die.

**In K₇**: K₇ plays the game honestly. It makes testable predictions.""",
 """- If the measurements end up excluding 197° (at the level physicists call 3 sigma) → this formula is dead, and so is the choice of reading 197 in degrees. No rescue, no adjusted version.
- If they include 197° → the formula survives. That would show the choice agrees with nature; it would not prove the shape is right.

**That's science**: statements that can die, with the rules written before the result is known.

**In K₇**: The rules are written in advance, formula by formula. Six of the 33 formulas have already failed as exact equalities, and the framework says which. One failed formula does not sink the others, and the framework says that in advance too."""),
("""**In K₇**: Zero adjustable parameters = maximum naturalness.""",
 """**In K₇**: The formulas have no dial to tune. Whether that makes the framework "natural" or just rigid is exactly what the experiments are for."""),
("""If Lean accepts your proof, it's **mathematically certain**.

**In K₇**: 290+ relations verified in Lean 4 with 0 "sorry" (holes). Zero domain-specific axioms.""",
 """If Lean accepts your proof, it's **mathematically certain**.

**In K₇**: The arithmetic of the 33 formulas is checked in Lean 4, with no "sorry" (holes). What that proves is that the sums are right: that 21/91 really is 3/13. It does not prove that 3/13 is the right formula for nature, nor that the shape exists."""),
("""**In K₇**: The LHC measured W, Z, Higgs masses that K₇ predicts.""",
 """**In K₇**: The LHC measured the W, Z and Higgs masses; the dictionary has formulas for their ratios."""),
("""**K₇ prediction**: δ_CP = 197° ± 5° (measurable 2034-2039)

**In K₇**: If DUNE finds δ_CP very different from 197°, K₇ is falsified. This is the key test.""",
 """**K₇ value**: δ_CP = 197°, exactly (today's measurements say 212°, give or take about 30°).

**In K₇**: If the measurements end up excluding 197°, that formula is rejected, together with the choice of reading 197 in degrees. It is one clear test among several; it would not decide the whole framework by itself, in either direction."""),
("""**In K₇**: Planck measured Ω_DE, n_s, etc. that K₇ predicts.""",
 """**In K₇**: Planck measured Ω_DE, n_s and other quantities for which the dictionary has formulas."""),
("""*K₇ Framework v3.3: For Everyone*""", """*K₇ Framework v3.6: For Everyone*"""),
]

FR = [
("""K₇ propose des réponses : **zéro paramètre libre**. Tout vient de la géométrie.""",
 """K₇ propose un dictionnaire où aucune formule n'a de molette à tourner : les nombres sont des rapports de nombres entiers. Ce qu'il n'a pas, c'est la raison pour laquelle *ces* formules vont avec *ces* mesures. Ce manque est écrit noir sur blanc, pas caché.

**Quel genre d'affirmation est-ce (version 3.6) ?** C'est un *dictionnaire*, pas une dérivation. Personne ne connaît de mécanisme qui mène de la forme aux nombres : les formules ont été appariées aux mesures, et le cadre le dit. La forme elle-même n'a pas été construite. Ce guide explique les idées ; quand il dit « dans K₇ », lisez « dans le dictionnaire que propose K₇ »."""),
("""**Et dans K₇** : tout découle de K₇. C'est LA forme de l'univers caché.""",
 """**Et dans K₇** : toutes les formules du dictionnaire s'écrivent avec les nombres de cette forme. Savoir si une telle forme existe avec exactement 21 et 77 trous est une question mathématique ouverte : personne ne l'a encore construite."""),
("""et la phase CP (δ = 197°) sont dérivés de la topologie.""",
 """et la phase CP (δ = 197°) s'écrivent comme des rapports des nombres de la forme. Pour la phase, la forme donne le nombre entier 197 ; le lire en degrés est un choix."""),
("""**Et dans K₇** : des rapports comme m_s/m_d = 20 sont dérivés de la topologie.""",
 """**Et dans K₇** : des rapports comme m_s/m_d = 20 s'écrivent comme des produits des nombres de la forme."""),
("""**La proposition de K₇** : ce n'est pas magique. `α⁻¹ = 137,033` émerge de la topologie de K₇, sous la forme `128 + 9 + correction`, où `128 = 2⁷` (les 7 dimensions cachées de K₇) et `9 = 99/11` (un rapport d'invariants topologiques). Le « grand sacré mystère » de Feynman devient une **conséquence de la forme**.""",
 """**La formule de K₇** : `α⁻¹ = 137,033`, écrit `128 + 9 + correction`, où `128 = 2⁷` et `9 = 99/11` (un rapport des nombres de la forme). C'est proche, et ce n'est pas juste : α est mesuré à dix décimales, et 137,033 n'est pas 137,036. Le cadre garde cette formule comme une *proximité*, un tir à côté de peu, et ne la présente plus comme un résultat exact. Le mystère de Feynman reste entier."""),
("""**Et dans K₇** : la recette du cocktail n'est pas arbitraire, elle est dictée par la forme du shaker cosmique (K₇).""",
 """**Et dans K₇** : la recette 3/13 = 0,2308 approche la valeur mesurée, 0,2312. Mais ce nombre est mesuré si précisément que ce petit écart vaut sept fois l'incertitude : comme égalité exacte, la formule est rejetée, et le cadre ne la garde que comme un tir à côté de peu."""),
("""**Et dans K₇** : cette coïncidence troublante devient une conséquence logique.""",
 """**Et dans K₇** : le dictionnaire écrit 2/3 comme le rapport de deux nombres de la forme, et la mesure est d'accord. L'honnêteté demande une note : 2/3 est une fraction si simple que presque n'importe quelle liste de nombres peut la produire, donc cet accord n'est pas un indice que la forme est la bonne."""),
("""C'est comme demander « pourquoi un cube a 6 faces ? ». La réponse n'est pas « comme ça », c'est « parce que c'est un cube ». La forme impose le nombre.

**Et dans K₇** : le nombre de familles n'est pas un accident, c'est une conséquence géométrique.""",
 """**Et dans K₇** : le nombre 3 sort d'une division de deux entiers du dictionnaire. C'est une identité arithmétique, un contrôle de cohérence ; ce n'est pas la preuve que la nature doit avoir trois familles."""),
("""### Zéro paramètre libre

**En jargon** : Théorie sans constantes ajustables.

**Version comptoir** : IKEA contre meuble sur mesure.

- **Le Modèle Standard** = un meuble sur mesure. Le menuisier prend 19 mesures chez vous et construit un meuble qui s'adapte parfaitement. Mais il ne peut pas expliquer *pourquoi* votre salon a ces dimensions-là.

- **K₇** = un meuble IKEA universel. La notice dit : « Prenez un diabolo de 7 dimensions à holonomie G₂. » Il n'y a qu'une seule façon de l'assembler. Les dimensions tombent automatiquement.

**Et dans K₇** : 19 nombres mystérieux → 0 nombre mystérieux. Tout vient de la forme.""",
 """### Zéro paramètre libre

**En jargon** : Aucune constante continûment ajustable ; et un registre de tout ce qui a été choisi.

**Version comptoir** : Lego contre pâte à modeler.

- **La pâte à modeler** se presse pour épouser n'importe quel moule. Une théorie à molettes, c'est ça : on tourne la molette, on retrouve la mesure.

- **Les briques de Lego** ne se pressent pas. Une formule comme 3/13 est une brique de Lego : on ne peut pas la pousser de 1 %. Si la mesure s'éloigne, la formule est fausse, c'est tout.

Les formules de K₇ sont des briques de Lego. Mais quelqu'un a quand même choisi *quelles briques prendre et où les poser*. Avec une boîte assez grande, on construit quelque chose de proche d'à peu près n'importe quelle forme. « Pas de molette » ne veut donc pas dire « rien n'a été choisi ».

**Et dans K₇** : pas de molette, et une liste écrite (le *registre des résidus*) de tous les choix faits : les deux nombres 21 et 77, les formules elles-mêmes, une normalisation, et l'unité dans laquelle on lit 197."""),
("""- Si DUNE trouve 197° ± 5° → K₇ survit
- Si DUNE trouve 250° → K₇ est mort. Terminé. On passe à autre chose.

**Ça, c'est de la science** : des prédictions qui peuvent mourir.

**Et dans K₇** : K₇ joue le jeu honnêtement. Il fait des prédictions testables.""",
 """- Si les mesures finissent par exclure 197° (au niveau que les physiciens appellent 3 sigma) → cette formule est morte, et le choix de lire 197 en degrés avec elle. Pas de sauvetage, pas de version retouchée.
- Si elles incluent 197° → la formule survit. Cela montrerait que le choix s'accorde avec la nature ; cela ne prouverait pas que la forme est la bonne.

**Ça, c'est de la science** : des énoncés qui peuvent mourir, avec des règles écrites avant de connaître le résultat.

**Et dans K₇** : les règles sont écrites à l'avance, formule par formule. Six des 33 formules ont déjà échoué comme égalités exactes, et le cadre dit lesquelles. Une formule qui tombe n'entraîne pas les autres, et le cadre le dit à l'avance aussi."""),
("""**Et dans K₇** : zéro paramètre ajustable = naturalité maximale.""",
 """**Et dans K₇** : les formules n'ont pas de molette à régler. Savoir si cela rend le cadre « naturel » ou seulement rigide, c'est justement ce que les expériences diront."""),
("""Si Lean accepte votre preuve, c'est **mathématiquement certain**.

**Et dans K₇** : 290+ relations vérifiées en Lean 4 avec 0 « sorry » (trous). Zéro axiome spécifique au domaine.""",
 """Si Lean accepte votre preuve, c'est **mathématiquement certain**.

**Et dans K₇** : l'arithmétique des 33 formules est vérifiée en Lean 4, sans « sorry » (trous). Ce que cela prouve, c'est que les calculs sont justes : que 21/91 vaut bien 3/13. Cela ne prouve pas que 3/13 est la bonne formule pour la nature, ni que la forme existe."""),
("""**Et dans K₇** : le LHC a mesuré les masses des W, Z et Higgs que K₇ prédit.""",
 """**Et dans K₇** : le LHC a mesuré les masses des W, Z et Higgs ; le dictionnaire a des formules pour leurs rapports."""),
("""**Prédiction K₇** : δ_CP = 197° ± 5° (mesurable entre 2034 et 2039)

**Et dans K₇** : si DUNE trouve δ_CP très différent de 197°, K₇ est falsifié. C'est le test crucial.""",
 """**Valeur K₇** : δ_CP = 197°, exactement (les mesures d'aujourd'hui donnent 212°, à une trentaine de degrés près).

**Et dans K₇** : si les mesures finissent par exclure 197°, cette formule est rejetée, avec le choix de lire 197 en degrés. C'est un test net parmi plusieurs ; à lui seul il ne déciderait pas du cadre entier, ni dans un sens ni dans l'autre."""),
("""**Et dans K₇** : Planck a mesuré Ω_DE, n_s, etc., des valeurs que K₇ prédit.""",
 """**Et dans K₇** : Planck a mesuré Ω_DE, n_s et d'autres quantités pour lesquelles le dictionnaire a des formules."""),
]


def patch(path, pairs):
    t = open(path, encoding="utf-8").read()
    for a, b in pairs:
        if t.count(a) != 1:
            raise SystemExit("%s : motif présent %d fois : %r" % (path, t.count(a), a[:70]))
        t = t.replace(a, b)
    open(path, "w", encoding="utf-8").write(t)
    print("ok  %s (%d remplacements)" % (path, len(pairs)))


if __name__ == "__main__":
    d = sys.argv[1]
    for f in ("GIFT_FOR_EVERYONE.md", "wiki/GIFT-for-Everyone.md"):
        patch("%s/%s" % (d, f), EN)
    for f in ("GIFT_FOR_EVERYONE.fr.md", "wiki/GIFT-for-Everyone.fr.md"):
        patch("%s/%s" % (d, f), FR)
