---
title: "Blog : Le jumeau étoilé"
layout: default
---

> Version originale en anglais sur [arithmon.substack.com](https://arithmon.substack.com/p/the-star-twin)

# Le jumeau étoilé
## Deux polyèdres que l'arithmétique ne sait pas distinguer, et la seule question qui les sépare

---

En septembre, j'ai ajouté un petit programme de vérification à un projet de recherche voisin du mien, et son résultat le plus intéressant a été une limite.

Le programme vérifiait, en arithmétique exacte, une vieille correspondance mathématique entre les symétries de l'icosaèdre, le polyèdre à vingt faces mieux connu comme le d20 des jeux de rôle sur table, et E₈, la structure exceptionnelle qui revient sans cesse dans mon travail. La correspondance tenait. Toutes les cases étaient cochées. Et puis, tout en bas du rapport, il y avait une ligne que je n'attendais pas : *cette construction ne choisit pas le nombre d'or.*

Elle hésite entre deux nombres. Le nombre d'or, φ = 1,618…, et un autre qui lui ressemble comme un frère. Suivez cette hésitation jusqu'au bout et vous arrivez à deux objets que les géomètres connaissent depuis plus de deux siècles, et à une question d'une simplicité presque enfantine.

Combien de fois faut-il faire le tour ?

## Deux programmes, un dé à vingt faces

Le projet voisin s'appelle *Observer Patch Holography*, OPH pour les intimes. Il est mené par Bernhard Mueller, qui a passé vingt ans à casser des systèmes informatiques pour gagner sa vie avant de se demander si l'on pouvait faire la même chose à la réalité : de la rétro-ingénierie, appliquée à l'univers.

Son point de départ est l'inverse du mien. Là où Arithmon part d'une forme géométrique et demande quels nombres elle produit, OPH part des observateurs. Des observateurs finis, qui ne voient chacun qu'un morceau du monde, et qui doivent se mettre d'accord sur ce qui est vrai. Dans OPH, aucun observateur ne voit l'univers entier ; un fait ne devient public qu'une fois qu'il a survécu à la comparaison entre voisins.

Et voici le détail qui m'a fait dresser l'oreille : chaque observateur d'OPH a douze « ports » par lesquels il échange avec les autres. Douze ports câblés comme les sommets d'un icosaèdre.

Un icosaèdre, c'est vingt triangles, douze sommets, trente arêtes, cinq triangles autour de chaque sommet. Le dé à vingt faces de vos soirées de jeu de rôle. Et si vous écrivez les coordonnées de ses sommets, vous y trouvez le nombre d'or, bien rangé à l'intérieur.

Deux programmes partis des deux bouts opposés du problème, et qui tombent sur le même dé. J'ai rejoint OPH début septembre.

## Le nombre d'or et son ombre

Le nombre d'or est la solution d'une équation très simple :

x² = x + 1

Sauf que cette équation a deux solutions. La première, φ = 1,618…, est celle que tout le monde connaît, celle des coquillages, des façades et des livres de développement personnel. La seconde vaut −0,618…, exactement 1 − φ. Je l'appellerai son ombre.

Ces deux nombres partagent une propriété troublante : si vous n'avez que des fractions, vous ne pouvez pas les distinguer. Toute équation à coefficients entiers que φ vérifie, son ombre la vérifie aussi. Ils ne diffèrent que par le signe placé devant une racine carrée de cinq, et les fractions sont aveugles à ce signe. Vue uniquement à travers les fractions, une théorie ne sait pas quel jumeau elle regarde.

Les mathématiciens appellent cela une symétrie de Galois. On peut aussi dire, plus simplement, que φ a un jumeau parfait, et que l'arithmétique ordinaire est incapable de les départager.

C'est ce que mon programme avait trouvé : la correspondance entre l'icosaèdre et E₈ marche aussi bien avec l'un qu'avec l'autre. Elle ne sait pas lequel des deux jumeaux elle tient.

Alors j'ai fait ce qu'on fait avec des jumeaux : je les ai mis côte à côte.

## Deux polyèdres, un squelette

Prenez les coordonnées de l'icosaèdre. Partout où φ apparaît, remplacez-le par son ombre. Ne touchez à rien d'autre : chaque sommet garde son numéro, chaque arête relie toujours les deux mêmes numéros, chaque face reste le même triangle.

Vous obtenez un autre polyèdre.

Il a douze sommets et, à un changement d'échelle près, ils forment exactement le même nuage de points qu'un icosaèdre ordinaire. Il a trente arêtes, toutes de même longueur. Il a vingt faces triangulaires, toutes identiques. Il a exactement les mêmes symétries. Si vous écriviez la liste de qui touche qui, les deux listes coïncideraient mot pour mot.

Et pourtant ce n'est plus une boule bien sage. C'est une étoile. Ses triangles se traversent et s'enroulent sur eux-mêmes, et au lieu de relier chaque sommet à ses plus proches voisins, chaque arête va chercher les suivants.

Ce polyèdre a un nom : le **grand icosaèdre**. Louis Poinsot l'a découvert en 1809, près de deux siècles après que Kepler eut reconnu, vers 1619, que certaines étoiles pouvaient être aussi régulières que les solides de Platon. Les artistes, il se trouve, y étaient arrivés les premiers : sur le sol de la basilique Saint-Marc à Venise, une marqueterie de marbre du XVᵉ siècle, parfois attribuée à Paolo Uccello, montre déjà un cousin étoilé du dodécaèdre. Qui fréquente les galeries connaît ce frisson : une seule et même structure, deux présences radicalement différentes.

Mais ce que ni Kepler ni Poinsot ne pouvaient savoir, puisque Galois n'avait pas encore écrit une ligne, c'est que ces deux objets sont des jumeaux au sens exact du mot. Le grand icosaèdre, c'est l'icosaèdre vu à travers l'ombre du nombre d'or.

## L'expérience de la lampe

Comment distinguer deux objets que toutes les équations en fractions confondent ?

Le problème ressemble un peu à un plan de métro. Le plan vous dit quelles stations se suivent et où l'on peut changer de ligne ; il ne vous dit pas comment les voies serpentent réellement sous la ville. Nos deux jumeaux ont exactement le même plan de métro. Pour voir la différence, il faut rendre son espace au plan.

Imaginez donc une expérience. Posez une petite lampe exactement au centre du polyèdre, et entourez le tout d'une grande sphère de verre dépoli. Chaque face triangulaire projette son ombre sur la sphère.

Avec l'icosaèdre, les vingt ombres se posent côte à côte sans se chevaucher et couvrent la sphère exactement une fois. À part les points qui tombent pile sur une arête, chaque point du verre est dans l'ombre d'une face, et d'une seule.

Avec le grand icosaèdre, les vingt ombres s'empilent. Presque chaque point du verre se retrouve sous **sept** couches d'ombre. L'étoile fait sept fois le tour de la sphère.

Un et sept. Aucune fraction ne voit la différence, mais un enfant qui compte les couches la voit tout de suite.

Les géomètres appellent ce nombre le *degré*, et c'est un invariant topologique : vous pouvez déformer, étirer, tordre, tant que rien ne se déchire et que rien ne passe par la lampe, un tour reste un tour et sept tours restent sept. Il appartient à la même famille d'idées que la ficelle enroulée autour de l'axe du [diabolo](Blog-Gods-Diabolo.fr.html) : vous pouvez tirer aussi fort que vous voulez, il faut dérouler pour défaire.

Et c'est là que les choses deviennent belles. Car le critère de la lampe n'est pas seul. Il y a au moins trois autres façons de poser la même question, et entre nos deux candidats, elles désignent toutes le même jumeau.

**Les arêtes les plus courtes.** Dans l'icosaèdre, chaque arête relie un sommet à ses plus proches voisins. Dans le jumeau étoilé, aux suivants.

**La rotation.** Autour d'un sommet de l'icosaèdre, les cinq voisins forment un pentagone. Passer d'un voisin au suivant, c'est tourner d'un cinquième de tour, 72 degrés, et le nombre d'or apparaît dans la mesure de cette rotation. Dans le jumeau étoilé, le même pas vers « le voisin suivant » en saute un et trace un pentagramme : c'est un tour de 144 degrés, et c'est l'ombre qui apparaît.

**La note la plus grave.** Celle-ci me ravit tout particulièrement, parce qu'elle me ramène au [verre qui chante](Blog-The-Singing-Glass.fr.html). Imaginez douze personnes debout aux sommets, chacune reliée à ses cinq voisins par des élastiques, et demandez à chacune de pointer vers son propre sommet. Dans l'icosaèdre, deux voisins reliés par un élastique pointent dans des directions proches : le motif varie doucement, les élastiques sont à peine tendus. Dans le jumeau étoilé, les mêmes élastiques relient des gens qui pointent à travers la figure : le motif zigzague, tout est tendu. Si ce réseau vibrait, le premier motif serait sa note la plus grave, le second sa plus aiguë. Autrement dit, l'icosaèdre est la façon la plus douce de faire vivre trois directions sur ce réseau ; son jumeau est la plus nerveuse.

Ce critère-là, je ne l'ai pas découvert : OPH l'avait déjà établi formellement. Dans OPH, les observateurs passent leur temps à comparer leurs notes avec leurs voisins et à réparer leurs désaccords, et cet été Bernhard a démontré, avec une vérification par ordinateur, que la géométrie ordinaire des ports est celle dont la réparation coûte le moins, et son jumeau celle qui coûte le plus, pour peu qu'on prenne cette règle de réparation comme la bonne mesure du désaccord. Vocabulaire différent, même idée : le squelette ne choisit pas le jumeau, mais la règle qui pénalise le désaccord le peut.

**Le graphe sait qui parle à qui ;**

**la géométrie sait comment ça s'enroule ;**

**la dynamique sait ce que ça coûte.**

Un seul tour. Les arêtes les plus courtes. Le nombre d'or dans la rotation. La note la plus grave. Quatre façons de dire la même chose : c'est l'icosaèdre, pas son jumeau.

Là où l'arithmétique ne peut pas trancher, il suffit de compter les tours.

## Pourquoi OPH a besoin de savoir

Revenons à nos observateurs à douze ports.

Le premier axiome d'OPH décrit leurs ports de façon combinatoire : qui est relié à qui, combien de faces, combien d'arêtes, dans quel ordre. Et il y insiste : le texte précise que l'icosaèdre n'y est « régulier » qu'au sens du plan de métro, sans coordonnées, sans longueurs, sans placement dans l'espace. Or un plan de métro, c'est exactement ce que les deux jumeaux ont en commun. À l'échelle d'un seul observateur, l'axiome ne sait pas s'il décrit un icosaèdre ou un grand icosaèdre.

Ce n'est pas un défaut caché que je viendrais dénoncer : les papiers d'OPH le disent eux-mêmes, noir sur blanc. À plusieurs endroits, ils précisent qu'ils ne prétendent pas sélectionner le nombre d'or. C'est l'une des choses que j'apprécie dans ce projet, et l'une des raisons pour lesquelles je l'ai rejoint : ses limites y sont écrites aussi visiblement que ses résultats.

Je suis donc parti chercher dans OPH une condition supplémentaire qui pourrait choisir entre les deux jumeaux. Et c'est en relisant l'axiome jusqu'au bout que je suis tombé sur une phrase troublante. Les observateurs ne flottent pas dans le vide : leur réseau doit se raccorder à un écran sphérique, et ce raccord doit être de degré un. En langage moins technique : quand on compte les tours en tenant compte de leur sens, le réseau doit faire le tour de l'écran exactement une fois, au total.

Un tour. C'est exactement le nombre que ma lampe trouve pour l'icosaèdre. Le grand icosaèdre, lui, fait sept tours.

Ce n'est pas encore une preuve. Les deux « un » vivent pour l'instant à deux étages différents de la construction : l'un concerne le réseau de tous les observateurs et leur écran commun, l'autre les vingt faces d'un seul observateur et leur ombre. Il reste à montrer que c'est le même tour, ou à découvrir que ce n'en est pas un.

Je ne connais pas encore la réponse. Mais je sais maintenant exactement ce qu'il faut démontrer.

## Et Arithmon, dans tout ça ?

Je vous dois un aveu, parce que ce texte me concerne aussi.

Parmi les trente-trois relations exactes du framework K₇, une seule fait intervenir un ingrédient qui n'est pas un nombre entier : le rapport des masses du muon et de l'électron, écrit 27^φ. Le nombre d'or y entre précisément par la correspondance entre E₈ et l'icosaèdre. C'est la relation la plus fragile du framework, et les papiers la tiennent délibérément à part, pour qu'elle n'emprunte pas la solidité des trente-deux autres.

Choisir φ plutôt que son ombre ne la sauve pas. Cela lève une ambiguïté, pas deux. Même avec le bon jumeau en main, il faudrait encore expliquer pourquoi ce nombre devrait se retrouver en exposant, et personne ne l'a fait. Je préfère le dire ici plutôt que de laisser croire qu'un joli polyèdre étoilé a réglé la question.

## Ce que je sais et ce que je ne sais pas

Je sais que les mathématiques de ce texte ne sont pas nouvelles. Le lien entre l'icosaèdre et le grand icosaèdre par la symétrie de Galois est classique, et le mathématicien John Baez l'a très joliment exposé en mai dernier. Ce qui m'intéresse ici, c'est l'endroit où on l'applique : aux ports d'un observateur, dans une théorie qui a besoin de savoir lequel des deux jumeaux elle abrite.

Je sais qu'entre ces deux candidats, les quatre critères désignent le même jumeau : je l'ai vérifié en arithmétique exacte, sans une seule approximation, et le programme sera public avec la contribution à OPH. L'un des quatre, celui de la réparation des désaccords, avait déjà été démontré dans OPH avant moi.

Je ne sais pas si le tour global qu'OPH impose force le tour local de chaque observateur. Je ne sais pas si ce choix a des conséquences mesurables. Rien dans ce texte n'est une prédiction, et rien n'y est une découverte physique. C'est une question mieux posée qu'avant, ce qui est modeste, et c'est souvent là que tout commence.

Il y a quelque chose de réconfortant dans cette histoire. Deux programmes de recherche, partis des deux bouts, l'un de la géométrie, l'autre des observateurs, tombent sur le même dé à vingt faces et sur la même hésitation. Et la réponse ne demande ni plus de nombres, ni plus de précision, ni plus de puissance de calcul.

Elle demande d'allumer une lampe au centre, et de compter les couches d'ombre.

Une, et c'est l'icosaèdre. Sept, et c'est son jumeau étoilé.

L'univers, s'il est bâti sur l'un des deux, sait lequel.

---

*Si vous découvrez ce blog, le point de départ est [ici](Blog-Brieucs-Gift.fr.html). Le dépôt d'OPH est ouvert sur [GitHub](https://github.com/FloatingPragma/observer-patch-holography), et l'exposé de John Baez sur le grand icosaèdre est [ici](https://johncarlosbaez.wordpress.com/2026/05/27/the-great-icosahedron/). Les papiers techniques d'Arithmon sont sur [Zenodo](https://zenodo.org/communities/arithmon/records?q=&l=list&p=1&s=10&sort=newest). Et si vous avez un d20 à portée de main, vous tenez déjà l'un des deux jumeaux.*
