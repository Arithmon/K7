# Préinscription — K7-V36-LEE : la P-value de K₇ survit-elle quand chaque concurrent cherche ses propres formules ? (2026-10-17, laptop)

**Décision 5 de Brieuc (plan v3.6, 17-10)** : null de look-elsewhere planifié depuis le laptop, préinscription avant le run
(R1). Lecture préinscrite, **deux issues seulement** : une P-value **globale calibrée** (recherche concurrente comprise), ou
le **retrait** de la P-value du texte.

## La question (R1)

PM §8.4 (l. 760, v3.5 publiée) : « Among 192,349 alternative (gauge group, holonomy, Betti) configurations tested by Monte
Carlo, zero outperform the framework […] (P < 5 × 10⁻⁶) ». La question qui peut tuer ou promouvoir cette phrase : **K₇
reste-t-il exceptionnel quand chaque géométrie concurrente cherche ses propres formules, dans la même grammaire, au même
budget, avec la même liberté d'assignation et d'unité ?**

## Qui a tranché (R0) — recherche sérialisée

**Motifs** : `192[,_ ]?349`, `total_configs`, `0.73`, `32.9`, `look-elsewhere`, `look_elsewhere`, `budget[-_ ]uniqueness`,
`budget d'unicité`, `betti scan`, `b2_b3`, `alternative betti`, `fake_frameworks`, `landscape_scan`, `held-out`, `105329`,
`20 structural constants`. **Répertoires** : `private/{canonical,legacy,memory}`, `K7/`, `Program/`, `Sieve/`, `Lean/` (hors
worktrees `.wt/`).

**Trouvé :**

1. **Le producteur de la phrase publiée** : `legacy/statistical_validation/validation_v33.py` →
   `validation_v33_results.json` (2026-02-03, graine 42) ; copie publique `K7/publications/validation/legacy/v3.3/`.
   - 192 349 = 100 000 (Betti) + 8 (jauge) + 4 (holonomie) + 91 896 (combinatoire) + 441 (grille ±10).
   - **Les formules sont figées** : `compute_predictions_v33` (l. 201-342) code en dur les 33 formules de K₇ et les réévalue
     avec les invariants alternatifs. Aucun concurrent ne cherche ses propres formules. C'est le **piège de circularité**
     déjà nommé par le design du landscape scan (DESIGN.md du 17-06, « The circularity trap ») : les formules ayant été
     choisies pour (21, 77), (21, 77) gagne par construction.
   - Défauts constatés au passage, à verser aux corrections v3.6 (§ « À verser au plan ») : plusieurs prédictions ne
     dépendent pas de la configuration (λ_H, m_μ/m_e, n_s, Ω_b/Ω_m, sin²θ₂₃, α⁻¹) ; bogue l. 297
     (`dim_E8_sq = dim_E8*2`) ; 6 tirages sont (21, 77) lui-même ; « P < 5 × 10⁻⁶ » n'est que 1/192 349. **Le 0,73 % n'est
     pas le chiffre de ce run** : le JSON donne 0,8388 % (ancien θ₂₃), le résumé 0,26 %, et la moyenne Type I de
     `observables.json` actuel vaut 0,993 %.
2. **Le précédent qui fait déjà ce test pour (b₂, b₃)** : `canonical/scripts/coincidence_landscape_scan.py` (design gelé le
   17-06, `canonical/papers/landscape_scan/DESIGN.md`, FREEZE-Q1..Q5, seuil « spécial » au 99ᵉ percentile).
   - D4 (b₂ ≤ 40, b₃ ≤ 120, 4 961 paires) : percentile 79,0 en couverture sensible à τ = 10⁻⁴, coût 68,2.
   - D6 (grille KS complète, 242 064 paires) : percentiles 35,6 et 28,3.
   - Verdict publié en interne : « **convenient, not special** ».
   - Limites : 50 feuilles (tout l'alphabet de Lie) avec seulement les deux Betti qui varient, donc **aucune constante
     dérivée de K₇** (H*, κ_T⁻¹, det(g)) ; cibles = les 28 du Sieve, pas les 33 de K₇ ; tolérance relative uniforme.
3. **N2 sur les vraies cibles** (`coincidence_n2_real.py`, `coincidence_n2_trans.py` →
   `papers/counting_coincidences/mapping/`) et scorecard 4.3 : **0/9** battements de l'enveloppe des alphabets inventés ;
   m_H/m_W et n_s, les deux survivants de N0/N1, **échouent N2**.
4. **Contrôles du Sieve** (`Sieve/scripts/coincidence_fake_frameworks.py`) : `fake_alphabet` (20 entiers tirés sans remise
   dans 3..248) est le générateur gelé des alphabets inventés.

**Pas trouvé** : aucun producteur ne fait chercher ses propres formules à un concurrent **avec le vocabulaire de K₇
re-dérivé**, sur les **33 cibles de K₇**, avec la **liberté d'unité de δ_CP**. C'est l'objet de ce lot.

**Évidence antérieure, déclarée avant le run** : D4, D6 et N2 placent tous K₇ loin du seuil. L'issue la plus probable est le
**retrait**. Le lot reste utile pour trois raisons : le referee le demande (décision Sci. Rep. du 16-10, l. 28 : géométries,
vocabulaires, unités, échelles, assignations) ; le vocabulaire de K₇ (constantes dérivées) n'a jamais été testé ainsi ; et la
v3.6 doit pouvoir citer un calcul, pas une opinion. **Route moins chère à signaler à Brieuc** : retirer la P-value sans
calcul, en citant D4/D6/N2. Ce lot coûte quelques heures de laptop ; il ne se justifie que si la v3.6 veut un chiffre.

## Objet (figé)

**Cibles** : les **33 observables de type I** de `canonical/data/observables.json` (sha256 `4704e967…921c`), valeur
`exp_value` et incertitude `exp_error`. Ce sont celles que la v3.5 compte dans sa moyenne et dans la phrase de §8.4.

**Grammaire** (moteur gelé `Sieve/scripts/coincidence_grammars.py`, sha256 `bcb03fe0…251b133`, Sieve `5adaf3d`) :
- feuilles = celles de **G_TRANS** (1 à 9, π, e, φ, γ, ln 2, ζ(3), ζ(5), ζ(7), ζ(9), ζ(11)) **plus** les **19 constantes entières**
  du registre du concurrent (φ n'est pas dupliqué) : **38 feuilles pour tous** (taille d'alphabet constante, garde
  anti-mirage du landscape scan) ;
- opérations de G_TRANS : `+ − × / ^`, `sqrt inv sq log` ; gardes du moteur (exposants entiers dans [−4, 4], imbrication de
  puissances ≤ 2, magnitude dans [10⁻¹², 10¹²], dédoublonnage à 12 chiffres) ;
- **budget : au plus 5 nœuds** (FREEZE-Q4 du landscape, continuité méthodologique) ; complexité κ_MDL du moteur.

**Concordance** : la cible o est **atteinte** par le vocabulaire V si une expression de ≤ 5 nœuds tombe à moins de
**τ_z = 2 écarts-types expérimentaux** (règle gelée du Sieve v1.1, DOI 10.5281/zenodo.21705149).
**Unités de δ_CP** : 207 ± 21 en degrés, ou la même grandeur en radians, en grades ou en tours ; la cible est atteinte si
l'une des quatre l'est. La règle vaut pour tous, K₇ compris.

**Assignations** : la recherche est **aveugle** ; chaque cible prend la meilleure expression du vocabulaire. Toute la
liberté d'assignation formule → observable est donc accordée à tous, **K₇ compris** : K₇ est noté par la même recherche
aveugle sur son propre vocabulaire, et non par ses formules publiées.

**Statistiques** :
- **S_cover(V)** = nombre de cibles atteintes (sur 33). **Primaire.**
- **S_cost(V)** = Σ sur les cibles du κ_MDL minimal d'une expression concordante ; une cible non atteinte coûte le κ_MDL
  maximal atteignable plus un coût d'opération (pénalité du landscape scan). **Duale**, rapportée, hors règle.

**Familles concurrentes** :
- **F-BETTI** (la géométrie et ses constantes dérivées) : b₂ ∈ [1, 40], b₃ ∈ [17, 120] (4 160 paires ; borne basse de b₃
  pour que κ_T⁻¹ ≥ 1). Les constantes qui dépendent de (b₂, b₃) sont re-dérivées par les **définitions publiées de la
  v3.5** (PM, App. B) : H* = b₂ + b₃ + 1 ; κ_T⁻¹ = b₃ − dim(G₂) − p₂ ; det(g) = p₂ + 1/(b₂ + dim(G₂) − N_gen), d'où
  det_den = b₂ + dim(G₂) − N_gen et det_num = p₂·det_den + 1. Les autres constantes restent celles de K₇.
  *Variante de sensibilité, hors règle* : κ_T⁻¹ = b₃ − b₂ + Weyl et det_num = Weyl·α_sum, det_den = 2^Weyl (dérivations
  de la fiche privée, qui coïncident avec les publiées en (21, 77) seulement). Le désaccord des deux dérivations hors de
  (21, 77) est lui-même une liberté de dictionnaire, publiée comme telle.
- **F-VOCAB** (le vocabulaire entier) : 2 000 vocabulaires de 19 entiers tirés par le générateur gelé du Sieve
  (`fake_alphabet` : sans remise dans 3..248), graine 20261017, plus φ.

**K₇** : le registre publié des 20 constantes (19 entiers + φ ; `canonical/scripts/algebraic_montecarlo.py`, l. 51-71), qui
est aussi le point (21, 77) de F-BETTI.

## Gates (dériver, ne pas nommer)

- **G1 (moteur)** : rejouer `G_STRUCT(betti=(21, 77))` à 5 nœuds sur les 28 cibles du Sieve, et retrouver **observable par
  observable** le `best_dev` de la ligne (21, 77) de `landscape_scan.json` (D4), à 10⁻⁹ près en relatif. (La couverture à
  τ = 10⁻² est saturée, 28/28 partout : elle ne distinguerait rien.) Si le moteur ou les cibles changent, G1 rougit.
- **G2 (appartenance)** : pour chaque cible, **calculer** (et non déclarer) si la valeur publiée de K₇ (`gift_value`) est
  dans l'ensemble énuméré de son vocabulaire à ≤ 5 nœuds (à 12 chiffres). Publier la liste. Toute cible dont la valeur
  publiée est dans l'ensemble et à moins de 2σ doit être atteinte par la recherche aveugle de K₇ ; sinon, REFUS-MOTEUR.
- **G3 (diagnostic circulaire, étiqueté)** : le score de K₇ avec ses formules publiées (nombre de valeurs publiées à moins
  de 2σ) est rapporté **comme diagnostic** seulement, jamais comme statistique.

## Verdicts (figés)

- P_F = (1 + #{V ∈ F : S_cover(V) ≥ S_cover(K₇)}) / (1 + |F|), pour F ∈ {F-BETTI, F-VOCAB}. Les égalités comptent contre
  K₇.
- **P_global = max(P_F-BETTI, P_F-VOCAB)** (test intersection-union : K₇ doit battre les deux classes de référence ; calibré
  sans correction de multiplicité).
- **LEE-GLOBALE** si P_global ≤ 0,01 (le seuil du 99ᵉ percentile de FREEZE-Q3) : §8.4 de la v3.6 remplace « P < 5 × 10⁻⁶ »
  par P_global, avec la phrase « chaque concurrent cherche ses propres formules dans la même grammaire, au même budget ».
- **LEE-RETRAIT** sinon : la P-value sort du texte ; §8.4 rapporte les deux percentiles **de façon descriptive** (« convenient,
  not special », vocabulaire du landscape scan), avec D4, D6 et N2.
- **REFUS-MOTEUR** si G1 ou G2 rougit : rien n'est lu.
- Pas de troisième issue ; S_cost et la variante de dérivation ne changent pas le verdict, ils sont publiés.

## Coût et mise en œuvre

- Producteur `canonical/scripts/k7_v3_6_lee_null.py` → `canonical/results/k7_v3_6_lee_null.json` (petit, committable) ;
  `--limit N` écrit `_limited.json`. Environ 6 160 vocabulaires à ~10-30 s chacun : quelques heures sur 12 workers.
- **Laptop, après la fin du run A6-QUAL-CH0** (on ne charge pas la machine pendant un run confiné).
- Pilote `--limit 20` d'abord, pour le temps par vocabulaire et les gates G1 et G2.

## N'atteste pas

- Rien sur l'**existence** de K₇, ni sur la vérité physique d'une relation.
- Rien au-delà de 5 nœuds : les formules plus profondes de K₇ (α⁻¹, m_τ/m_e, etc.) ne sont atteignables par personne à ce
  budget, et ce n'est **pas** une réussite.
- Les familles ne couvrent ni les changements de groupe de jauge ou d'holonomie au-delà des Betti (aucune règle publique de
  dérivation du registre pour un autre couple ; l'ancien Monte-Carlo changeait dim_E8 à la main), ni les **formes**
  d'observable (sin² contre angle) hors δ_CP. Ces libertés restent au registre du résidu de la v3.6.

**Revue** : Codex au jalon `prereg` (plafond 2 : 1 initiale + 1 ciblée) ; au jalon `measure`, **doublon Codex + Grok** (R4 :
le verdict touche une surface publiée).

## À verser au plan v3.6 (erreurs publiques trouvées par R0)

1. **PM §7, « headline outcome »** : « the unique survivor at exact rank 1 budget-unique is m_H/m_W » et « m_H/m_W and […]
   Koide […] are the sieve-distinguished survivors », alors que la scorecard 4.3 publiée
   (`papers/counting_coincidences/scorecard_4_3.md`, l. 8 et 56) marque **m_H/m_W et n_s N2 fail** (22 alphabets inventés
   sur 24 reproduisent m_H/m_W ; « neither clears the N2 envelope »).
2. **PM §8.4** : le 0,73 % ne vient pas du run cité ; formules figées ; prédictions indépendantes de la configuration
   comptées ; bogue `dim_E8*2` ; P plancher = 1/N (voir R0, 1).
3. **Registre** : deux dérivations de κ_T⁻¹ et de det(g) (App. B publiée, et fiche privée) qui ne coïncident qu'en
   (21, 77). La v3.6 doit en déclarer une, et l'autre au résidu.

## Amendement avant gel : pilote `--limit 3` (2026-10-17, avant le commit de cette note)

Un pilote de 9 vocabulaires (3 par famille, `k7_v3_6_lee_null_limited.json`) a tourné **avant** le commit de cette
préinscription, pour valider les gates et le temps (≈ 1 s par vocabulaire). Il a changé **une seule chose** dans la note : G1
compare désormais `best_dev` observable par observable, au lieu de la couverture à τ = 10⁻², qui est saturée.
**La statistique, les familles, les seuils et le verdict ne changent pas.**

Ce que le pilote a montré, déclaré ici pour que la lecture ne puisse pas en être choisie après coup :
- G1 vert (28/28 `best_dev` identiques à D4) ; G2 vert (28 valeurs publiées dans l'ensemble énuméré, toutes atteintes).
- **S_cover est saturé** : K₇ atteint 32 cibles sur 33 (seul α⁻¹ résiste, σ = 2·10⁻⁸), comme chacun des 9 vocabulaires
  pilotes (un F-VOCAB à 31). S_cost : K₇ 395,6 bits, F-BETTI 394,5 à 396,6, F-VOCAB 377,7 à 379,9 (moins cher que K₇).
- **Conséquence pour la lecture** : à 2σ et ≤ 5 nœuds, la grammaire atteint presque toute cible depuis presque tout
  vocabulaire. Un LEE-RETRAIT signifie alors « le null n'a **pas de puissance** pour distinguer K₇ : la proximité de ses
  valeurs aux mesures n'est pas, à elle seule, une évidence ». C'est l'issue « retrait » telle que préinscrite, pas une
  troisième ; la phrase de la v3.6 doit dire cette absence de puissance, sans parler d'évidence contre K₇.
- Changer la statistique après ce pilote serait la régler sur les données : on ne le fait pas. S_cost reste duale, publiée.

## Addendum après revue measure (2026-10-18, hors gel : prose seulement, rien de calculé ne change)

- **Dérivations (Codex M3)** : « qui coïncident avec les publiées en (21, 77) seulement » est faux. κ_pub⁻¹ = κ_fiche⁻¹ et
  det_pub = det_fiche ⟺ b₂ = 21 : les deux dérivations coïncident sur **toute la ligne b₂ = 21** (104 paires de la grille,
  de (21, 17) à (21, 120)) ; H* est identique partout. Le désaccord hors de cette ligne reste une liberté de dictionnaire.
  Même correction pour le point 3 de « À verser au plan v3.6 ».
- **Profondeur (Codex M2)** : « α⁻¹, m_τ/m_e, etc. ne sont atteignables par personne à ce budget » est faux pour m_τ/m_e :
  3477 = (56 + 1) × 61 a un témoin à 5 nœuds (1,61σ). La profondeur d'une écriture publiée n'est pas la complexité
  minimale de sa valeur ; seule la syntaxe publiée au-delà de 5 nœuds n'est pas testée comme telle.

## Amendement 1 (2026-10-22, avant le run rév. 1) — données et fenêtres

Motif : revue externe de la v3.6 (Brieuc, 2026-10-22). Les chiffres publiés du null (32/33, 4 159, 1 635/2 000) ont été
calculés sur l'ancien dataset ; le dataset est rafraîchi (PDG 2026, NuFIT 6.1 IC24+SK-atm, Planck 2018 une colonne,
CODATA 2022) et ses incertitudes sont ramenées à 1σ (entrées PDG à 90 % CL ÷ 1,645). Changements du producteur, seuls :
- fenêtre = [x − τ_z σ₋, x + τ_z σ₊] avec les DEUX côtés des erreurs asymétriques (NuFIT, A de Wolfenstein) ; le
  dataset ne stocke dans `exp_error` que le côté tourné vers K₇ (convention du pull), ce qui aurait biaisé la recherche
  des concurrents ;
- m_s/m_d : le PDG ne donne qu'une plage (17–22) ; la fenêtre est cette plage.
Inchangés : question, familles, graine, budget (5 nœuds), τ_z = 2, unités de δ_CP (degrés, radians, grades, tours),
règle de verdict (P_global ≤ 0,01 ⟹ LEE-GLOBALE, sinon LEE-RETRAIT). Les chiffres du run du 17-10 restent cités
comme résultat historique sur le dataset d'alors (sha `4704e967…`).

## Amendement 2 (2026-11-03, avant le run rév. 2) — fenêtres des rapports cosmologiques, témoin

Motif : revue Gemini `0ff8b67b2` (B3) et réserves de Brieuc du 2026-11-03. Les rapports A25, A26, A27, A29, A30 et A33
étaient propagés en négligeant les corrélations ; ω_c et ω_m sont pourtant corrélés à environ 0,99. Ils sont recalculés
sur les chaînes officielles Planck 2018 (`canonical/scripts/k7_v3_6_planck_ratios.py`, moyenne et écart-type pondérés ;
G1 : les chaînes redonnent `margestats`). Changements, seuls :
- les fenêtres de ces six cibles, via `observables.json` ;
- un témoin sérialisé, sans constantes de K₇ (registre vide : feuilles et opérations universelles de G_TRANS) ; il ne
  concourt pas dans P, il est publié ;
- la localisation du clone du Sieve et le contrôle de la grammaire (sha figé au run rév. 1) : câblage, sans effet numérique.
Inchangés : question, familles, graine, budget (5 nœuds), τ_z = 2, unités de δ_CP, règle de verdict. Les P et coûts du run
rév. 1 (dataset `f0de1c05…`) restent cités comme résultat historique.

### Résultat du run rév. 2 (2026-11-03, 10 076 s, `git_head` 0081490bc, Sieve 601283f, grammaire inchangée)

G1 et G2 passent. K₇ 31/33, S_cost 408,1. F-BETTI 1 085/4 159 (P = 0,261), F-VOCAB 1 015/2 000 (P = 0,508),
P_global = 0,508, **LEE-RETRAIT** (inchangé). Témoin sans constantes : 30/33 (manquent A04, A06, A07) ; son S_cost 404,2 n'est pas comparable à celui de K₇ (alphabet réduit, donc feuilles moins chères) et n'est pas cité dans S4.
Les comptes et les P sont ceux de la rév. 1, car seule A06 départage et sa fenêtre n'a pas bougé ; A30, dont la
valeur publiée sort de sa fenêtre, reste atteinte à l'aveugle par une autre expression, par K₇ comme par tous les
concurrents. Tables : `k7_v3_6_s4_tables.py`.

## Amendement 3 (2026-11-11, avant le run rév. 3) — fenêtre de m_W/m_Z

Motif : revue Gemini du 2026-11-11 (`canonical/notes/gemini_k7_v3_6_fop_referee_review_2026_11_11.md`, M3) et décision de
Brieuc du même jour. Le texte pose que les rapports de masses sont calculés depuis les masses publiées ; A21 (m_W/m_Z)
utilisait seul la ligne de rapport du résumé PDG, 0,88136(15). La règle lui est appliquée : 80,3625(77)/91,1879(20) =
0,881285(87), corrélations négligées (`k7_v3_6_exp_refresh.py`). La valeur publiée 37/42 passe de −2,7σ à −3,8σ.
Changement, seul : la fenêtre de A21, via `observables.json` (centre 0,881285, demi-largeur 2σ = 0,000173 au lieu de
0,00030). Les valeurs de B01 et B04 (type II) changent aussi dans le dataset ; le test ne lit que le type I.
Voie : RERUN PLEIN, justifié par (i) le pin d'entrée `observables.json` a changé.
Inchangés : question, familles, graine, budget (5 nœuds), τ_z = 2, unités de δ_CP, témoin, règle de verdict. Les chiffres du
run rév. 2 (dataset `dc772909…`) restent cités comme résultat historique.
Attendu, écrit avant le run et sans valeur de résultat : A21 était atteinte par les 6 159 vocabulaires dans l'ancienne
fenêtre ; si elle cesse de l'être pour certains, elle devient une seconde cible qui départage, et les P changent.

### Résultat du run rév. 3 (2026-11-11, 10 196 s, `git_head` 274c4a793, Sieve 601283f, grammaire inchangée)

G1 et G2 passent. K₇ 31/33, S_cost 408,1. F-BETTI 1 085/4 159 (P = 0,261), F-VOCAB 1 015/2 000 (P = 0,508),
P_global = 0,508, **LEE-RETRAIT** (inchangé). Témoin sans constantes : 30/33 (manquent A04, A06, A07).
A21 reste atteinte par les 6 159 vocabulaires dans sa fenêtre resserrée : elle ne devient pas une seconde cible qui
départage, et les comptes et les P sont ceux des rév. 1 et 2. Ce qui bouge : les coûts des concurrents, donc les comptes
« coût ≤ K₇ » du closeout (F-BETTI 1 163 → 1 038, F-VOCAB 698 → 628, variante 601 → 548). Tables : `k7_v3_6_s4_tables.py`.
