---
title: "Article S1 fondations"
layout: default
---

# Article : S1, fondations mathématiques

**Supplément S1 : fondations mathématiques, algèbre de Lie exceptionnelle E₈, variétés à holonomie G₂ et construction de K₇**

*Brieuc de La Fournière (2026)*
[Texte intégral (markdown, v3.5)](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_5_S1_foundations.md) | [archive v3.3 sur Zenodo : 10.5281/zenodo.18837071](https://doi.org/10.5281/zenodo.18837071)

> **v3.5.** [PDF](https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_5_S1_foundations.pdf) · [DOI : 10.5281/zenodo.21296168](https://doi.org/10.5281/zenodo.21296168) · markdown canonique [`k7_framework_3_5_S1_foundations.md`](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_5_S1_foundations.md).

---

## Résumé

Développe l'architecture E₈, les variétés à holonomie G₂ via le noyau de la dérivée de Lie, et la topologie de K₇. La paire (b₂, b₃) = (21, 77) est posée : aucune construction d'une variété G₂ compacte avec ces nombres de Betti n'est connue, et la route de Joyce–Karigiannis de la v3.5 ne la réalise pas (erratum v3.5, §9). La forme de référence fixe det(g) = 65/32 par une normalisation imposée (erratum §10 pour sa mise à l'échelle) ; le théorème de perturbation de Joyce ne s'applique que sous une hypothèse de petitesse dont la constante n'est pas calculée ici.

---

## Résultats clés

| Résultat | Valeur | Statut |
|----------|--------|--------|
| Chaîne d'algèbres à division | ℝ(1) → ℂ(2) → ℍ(4) → 𝕆(8) | terminale à 8 |
| Système de racines E₈ | 240 racines = 112 D₈ + 128 demi-entières | vérifié |
| \|W(E₈)\| | 2¹⁴ × 3⁵ × 5² × 7 = 696 729 600 | vérifié en Lean |
| Blocs de construction TCS | M₁(quintique)[b₂=11,b₃=40] + M₂(CI(2,2,2))[b₂=10,b₃=37] | conjecturaux ; non identifiés |
| det(g) | 65/32 | normalisation imposée |
| Spectral gap | λ₁ = 13/99 | algébrique |

---

## Structure des sections

- **Partie 0** : fondation octonionique, pourquoi 𝕆 est terminale, G₂ = Aut(𝕆), plan de Fano
- **Partie I** : algèbre de Lie exceptionnelle E₈, système de racines, groupe de Weyl, chaîne exceptionnelle
- **Partie II** : variétés à holonomie G₂, définition, classification de Berger, classes de torsion W₁ à W₂₇
- **Partie III** : construction de la variété K₇, cadre TCS, blocs ACyl, Mayer-Vietoris
- **Partie IV** : structure métrique et vérification, κ_T = 1/61, det(g) = 65/32 (imposé), statut du théorème de Joyce

---

## L'identité triple de Weyl

```
Weyl = (dim(G₂)+1)/N_gen = b₂/N_gen − p₂ = dim(G₂) − rang(E₈) − 1 = 5
```

---

## Liens connexes

- [Article principal](Paper-Main-Framework.html) : article principal
- [Article S2 dérivations](Paper-S2-Derivations.html) : les 33 dérivations
- [Article métrique G₂ explicite](Paper-Explicit-G2-Metric.html) : métrique numérique
- [Glossaire](Glossary.fr.html) : définitions des termes
