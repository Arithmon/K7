#!/usr/bin/env python3
"""k7_v3_6_landing_pages.py -- sections RESULTS / PAPERS / FALSIFICATION de
K7/docs/index.html et index.fr.html au cadrage 3.6 (étape 4, 2026-11-10).

Une seule structure pour les deux langues, pour que EN et FR ne divergent pas.
Les chiffres sont ceux de physics_main.md §4.1, §4.2, §7.2, §11 ; le lint
k7_v3_6_surfaces_lint.py contrôle les classes contre observables.json.
Idempotent sur les sections (remplacées entre marqueurs) ; le pied de page
et le lien v3.5 ne se posent qu une fois (assert).

Usage : k7_v3_6_landing_pages.py <K7>/docs
"""
import io
import re
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
D = sys.argv[1]
H3 = '<h3 style="font-family: var(--font-heading); font-size: 1.15rem; margin: 2rem 0 1rem; color: var(--accent);">'
def table(head, rows):
    o = ['    <table class="results-table">', '      <thead>', '        <tr>']
    o += ['          <th>%s</th>' % h for h in head] + ['        </tr>', '      </thead>', '      <tbody>']
    for r in rows:
        o.append('        <tr>')
        for i, c in enumerate(r):
            cls = ' class="value"' if (i == 1 and len(r) > 2) or (len(r) == 2 and i == 1) else ''
            o.append('          <td%s>%s</td>' % (cls, c))
        o.append('        </tr>')
    o += ['      </tbody>', '    </table>']
    return '\n'.join(o)
def sec(id_, title, body):
    return ('<section id="%s">\n  <div class="container">\n    <h2 class="section-title">%s</h2>\n'
            '    <div class="sep"></div>\n%s\n  </div>\n</section>\n\n') % (id_, title, body)
def p(t, cls='section-intro'):
    return '    <p class="%s">\n      %s\n    </p>' % (cls, t)
def card(title, text, links):
    l = '\n'.join('          <a href="%s">%s &rarr;</a>' % (u, n) for n, u in links)
    return ('      <div class="card">\n        <h3>%s</h3>\n        <p>%s</p>\n'
            '        <div class="card-meta">\n%s\n        </div>\n      </div>') % (title, text, l)

W = 'sin&#178;&#952;<sub>W</sub>'; T23 = 'sin&#178;&#952;<sub>23</sub>'; DCP = '&#948;<sub>CP</sub>'
MD = 'https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_%s.md'
RAW = 'https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/%s.pdf'
CONCEPT = 'https://doi.org/10.5281/zenodo.16891489'
ERR = 'https://github.com/Arithmon/K7/blob/main/publications/ERRATUM_v3.5.md'

L = {}
L['en'] = dict(
 dec=lambda s: s,
 meta='A declared correspondence between the topology of a G2-holonomy manifold K7 with E8 x E8 and 33 dimensionless parameters of the Standard Model and cosmology, stated with its dictionary, its residue and a decision rule. Arithmetic verified in Lean 4.',
 tagline=['K₇ assigns 33 dimensionless parameters of the Standard Model and of cosmology',
          'to closed forms in the invariants of a single 7-dimensional shape.',
          'It is a declared correspondence, not a derivation: what was set is written down,',
          'and so is the rule under which each relation can fail.'],
 res_title='Where It Stands',
 res_intro='Thirty-three relations with no continuously adjustable parameter, compared with the most recent data (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022). The formulas are assigned, not derived, and the classes below are not added into a single score.',
 h_classes='The 33 relations in five classes',
 classes_head=['Class', 'Count', 'Relations'],
 classes=[('within 2&sigma;', '23', 'the remaining relations'),
          ('tension (between 2&sigma; and 3&sigma;)', '2', 'm<sub>&tau;</sub>/m<sub>e</sub>, &Omega;<sub>c</sub>/&Omega;<sub>m</sub>'),
          ('proximity (beyond 3&sigma;, rejected as an exact equality)', '6', '&alpha;<sup>&minus;1</sup>, '+W+', m<sub>&mu;</sub>/m<sub>e</sub>, m<sub>&mu;</sub>/m<sub>&tau;</sub>, m<sub>b</sub>/m<sub>t</sub>, m<sub>W</sub>/m<sub>Z</sub>'),
          ('inside the PDG range (no uncertainty given)', '1', 'm<sub>s</sub>/m<sub>d</sub>'),
          ('non-Gaussian profile, octant unresolved', '1', T23)],
 h_sample='A sample of the relations',
 sample_head=['Relation', 'K₇ value', 'Formula', 'Measured', 'Pull'],
 sample=[('Q<sub>Koide</sub>', '2/3', 'dim G&#8322; / b&#8322;', '0.6666645(51)', '+0.4&sigma;'),
         ('&alpha;<sub>s</sub>(M<sub>Z</sub>)', '&radic;2/12', '&radic;2 / (dim G&#8322; &minus; p&#8322;)', '0.1180(9)', '&minus;0.2&sigma;'),
         (DCP, '197&deg;', '7 &times; dim G&#8322; + H*, read in degrees', '212 (+26/&minus;36)&deg;', '&minus;0.4&sigma;'),
         ('n<sub>s</sub>', '0.964864', '&#950;(11)/&#950;(5)', '0.9649(42)', '0.0&sigma;'),
         ('m<sub>W</sub>/m<sub>Z</sub>', '37/42', '(2b&#8322; &minus; 5) / 2b&#8322;', '0.881285(87)', '&minus;3.8&sigma;'),
         (W, '3/13', 'b&#8322; / (b&#8323; + dim G&#8322;)', '0.23122(6)', '&minus;7.5&sigma;'),
         (T23, '6/11', '(11 &minus; 5) / 11', '0.470 (+17/&minus;14)', 'second octant')],
 sample_note='Three sectors are overdetermined: four lepton relations bear on two mass ratios, three CKM relations on two parameters, seven density relations on two densities. In each, the relations disagree with one another as exact equalities, and none is selected after the fact. The 33 are not 33 independent tests.',
 h_lee='Is the agreement distinctive?',
 lee_intro='No. In a preregistered look-elsewhere test, every competitor searches for its own formulas, in the same grammar and with the same budget.',
 lee_head=['Test', 'Result'],
 lee=[('Targets reached by K₇', '31 of 33'),
      ('Alternative Betti pairs that reach as many', '1 085 of 4 159 (26%)'),
      ('Invented vocabularies that reach as many', '1 015 of 2 000 (51%)'),
      ('A control with no K₇ constant', '30 of 33'),
      ('Preregistered verdict', 'look-elsewhere effect not overcome')],
 lee_note='Closeness to the measured values is therefore not, by itself, evidence for K₇. The coincidence probabilities and the P-values shown on earlier versions of this page are withdrawn. What remains is rigidity (an integer ratio cannot be nudged, so one measurement can reject a relation) and a written list of everything that was set rather than derived.',
 papers_title='Papers &amp; Proofs',
 papers_note='Version 3.6 of the framework paper. The latest deposited version is always at the <a href="%s">Zenodo concept DOI</a>; version 3.5 is read together with its <a href="%s">erratum</a>.' % (CONCEPT, ERR),
 cards=[('Main Paper (v3.6)', '<em>The K₇ Dictionary: Testing G&#8322; Topology against Particle Physics and Cosmology.</em> The correspondence, its dictionary, its residue register, the 33 relations, the look-elsewhere test and the decision rule.', [('Markdown', MD % 'main'), ('Zenodo', CONCEPT)]),
        ('S1: Foundations (v3.6)', 'E&#8328;, G&#8322; and the topology assumed for K&#8327;. No compact manifold with (21, 77) is currently constructed.', [('Markdown', MD % 'S1_foundations')]),
        ('S2: The 33 Relations (v3.6)', 'The arithmetic of each relation, the dictionary choices it makes and its status.', [('Markdown', MD % 'S2_derivations')]),
        ('S3: Observable Dataset (v3.6)', 'Reference data for the 33 relations, and 62 conditional or diagnostic entries that are not counted as predictions.', [('Markdown', MD % 'S3_observables')]),
        ('S4: Look-Elsewhere (v3.6)', 'The preregistered test in which every competitor searches for its own formulas, and descriptive diagnostics.', [('Markdown', MD % 'S4_sieve_diagnostics')]),
        ('Paper A &mdash; Certified G&#8322; Structure', 'Newton&ndash;Kantorovich certificate for a nearby torsion-free metric on a seam region. It does not construct a compact K&#8327;. Zenodo 19892350.', [('PDF', RAW % 'g2_certified_neck'), ('DOI', 'https://doi.org/10.5281/zenodo.19892350')]),
        ('Paper B &mdash; Spectral Geometry', 'Laplacian spectrum and harmonic forms of the approximate seam metric. Zenodo 19893371.', [('PDF', RAW % 'g2_spectral'), ('DOI', 'https://doi.org/10.5281/zenodo.19893371')]),
        ('Paper C &mdash; K3 Newton-Kantorovich', 'NK diagnostics on a Donaldson K3 metric (CI(2,2,2)). Zenodo 19708916.', [('PDF', RAW % 'K3_NK_Certificate'), ('DOI', 'https://doi.org/10.5281/zenodo.19708916')]),
        ('Paper D &mdash; Donaldson Analytic Note', 'Explicit closed-form G&#8322; ansatz on a K3-coassociative neck with 5-layer Wirtinger certificate. Zenodo 20039066.', [('PDF', RAW % 'donaldson_analytic'), ('DOI', 'https://doi.org/10.5281/zenodo.20039066')]),
        ('Paper E &mdash; Rank-1 Branched Adiabatic', 'Conditional analytic framework for the neck. Its datum is not realisable as posed (erratum, section 2). Zenodo 21215956.', [('PDF', RAW % 'rank_one_branched_adiabatic'), ('DOI', 'https://doi.org/10.5281/zenodo.21215956')]),
        ('Lean 4 Proofs', '156 files, 14 axioms (4 from the literature, 10 interval certificates), no sorry. The formalization verifies the arithmetic of the 33 relations; it does not establish their physical content or the existence of K&#8327;.', [('Repository', 'https://github.com/Arithmon/K7-Lean')])],
 dec_title='Decision Rule',
 dec_intro='The relations are stated as exact equalities. A relation is rejected when its reference series (PDG, NuFIT, Planck, CODATA) excludes its value at 3&sigma;. The rule has no repair clause: a relation that fails is not rescued by changing its formula, its unit, its scale or its dataset.',
 dec_head=['Relation', 'Value', 'Rejected when', 'Where'],
 decs=[(DCP+', the phase 2&pi;&middot;197/360', '197&deg;', 'a global fit whose 3&sigma; interval excludes 197&deg;; the unit assignment is rejected with it', 'DUNE, Hyper-Kamiokande'),
       (T23, '6/11', 'a global fit whose 3&sigma; interval excludes 6/11, in either octant', 'DUNE, Hyper-Kamiokande'),
       ('sin<sup>2</sup>&theta;<sub>12</sub>', '4/13', 'a global fit whose 3&sigma; interval excludes 4/13', 'JUNO (first result 0.3092 &plusmn; 0.0087; about four times tighter than today&rsquo;s global fit after six years)'),
       ('m<sub>&tau;</sub>/m<sub>e</sub> and Q<sub>Koide</sub>', '1776.74 and 1776.97 MeV for m<sub>&tau;</sub>', 'an m<sub>&tau;</sub> value whose 3&sigma; interval excludes the value, each relation separately', 'Belle II, BES III'),
       ('N<sub>gen</sub>', '3', 'a fourth sequential generation', 'LHC, FCC'),
       ('m<sub>s</sub>/m<sub>d</sub>', '20', 'a lattice determination with an uncertainty whose 3&sigma; interval excludes 20', 'Lattice QCD')],
 verdicts='<strong>Standing verdicts.</strong> Six relations are already rejected as exact equalities and kept only as numerical proximities: &alpha;<sup>&minus;1</sup>, '+W+', m<sub>&mu;</sub>/m<sub>e</sub>, m<sub>&mu;</sub>/m<sub>&tau;</sub>, m<sub>b</sub>/m<sub>t</sub> and m<sub>W</sub>/m<sub>Z</sub>. '+T23+' is <strong>in tension</strong>: the NuFIT 6.1 best fit sits in the lower octant, and 6/11 lies inside its 3&sigma; range. Two contradicting measurements outside the reference series are reported beside their class: h = 167/248 agrees with Planck and is excluded by the SH0ES distance ladder at 5.5&sigma;; the density relations agree with Planck and are strained by the baryon acoustic oscillations of DESI (second data release): about 2&sigma; with DESI alone, and &minus;3.3&sigma;, +3.4&sigma; and &minus;3.1&sigma; for &Omega;<sub>&Lambda;</sub>/&Omega;<sub>m</sub>, &Omega;<sub>m</sub>/&Omega;<sub>&Lambda;</sub> and &Omega;<sub>DE</sub> with DESI and the cosmic microwave background combined (&minus;3.0&sigma; for h). A rejection rejects a relation and the assignment that produced it, not the programme by itself. Every verdict is recorded, favourable or not, in the <a href="https://github.com/arithmon/program/blob/main/CONFRONTATIONS.md">program scoreboard</a>.',
 v35='Zenodo (framework v3.5)', footer=('K₇ Framework v3.5', 'K₇ Framework v3.6'),
)
fr = dict(L['en'])
fr.update(
 dec=lambda s: s,
 meta="Une correspondance déclarée entre la topologie d'une variété K7 à holonomie G2, avec E8 × E8, et 33 paramètres sans dimension du Modèle Standard et de la cosmologie, énoncée avec son dictionnaire, son résidu et une règle de décision. Arithmétique vérifiée en Lean 4.",
 tagline=['K₇ associe 33 paramètres sans dimension du Modèle Standard et de la cosmologie',
          "à des formes closes en les invariants d'une seule forme de dimension 7.",
          "C'est une correspondance déclarée, pas une dérivation : ce qui a été posé est écrit,",
          'et la règle selon laquelle chaque relation peut échouer aussi.'],
 res_title='Où en est le cadre',
 res_intro="Trente-trois relations sans paramètre continûment ajustable, comparées aux données les plus récentes (PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022). Les formules sont attribuées, non dérivées, et les classes ci-dessous ne s'additionnent pas en un score unique.",
 h_classes='Les 33 relations en cinq classes',
 classes_head=['Classe', 'Nombre', 'Relations'],
 classes=[('à moins de 2&sigma;', '23', 'les autres relations'),
          ('tension (entre 2&sigma; et 3&sigma;)', '2', L['en']['classes'][1][2]),
          ('proximité (au-delà de 3&sigma;, rejetée comme égalité exacte)', '6', L['en']['classes'][2][2]),
          ("dans l'intervalle du PDG (sans incertitude)", '1', 'm<sub>s</sub>/m<sub>d</sub>'),
          ('profil non gaussien, octant non tranché', '1', T23)],
 h_sample='Un échantillon des relations',
 sample_head=['Relation', 'Valeur K₇', 'Formule', 'Mesure', 'Écart normalisé'],
 sample=[(a, b.replace('0.964864', '0,964864'), c.replace('read in degrees', 'lu en degrés'), d.replace('0.', '0,'), e.replace('.', ',').replace('second octant', 'second octant'))
         for a, b, c, d, e in L['en']['sample']],
 sample_note="Trois secteurs sont surdéterminés : quatre relations leptoniques portent sur deux rapports de masses, trois relations CKM sur deux paramètres, sept relations de densité sur deux densités. Dans chacun, les relations se contredisent en tant qu'égalités exactes, et aucune n'est choisie après coup. Les 33 ne sont pas 33 tests indépendants.",
 h_lee="L'accord est-il distinctif ?",
 lee_intro='Non. Dans un test look-elsewhere préenregistré, chaque concurrent cherche ses propres formules, dans la même grammaire et avec le même budget.',
 lee_head=['Test', 'Résultat'],
 lee=[('Cibles atteintes par K₇', '31 sur 33'),
      ('Paires de Betti alternatives qui en atteignent autant', '1 085 sur 4 159 (26 %)'),
      ('Vocabulaires inventés qui en atteignent autant', '1 015 sur 2 000 (51 %)'),
      ('Un contrôle sans aucune constante de K₇', '30 sur 33'),
      ('Verdict préenregistré', 'effet look-elsewhere non surmonté')],
 lee_note="La proximité avec les valeurs mesurées n'est donc pas, à elle seule, un indice en faveur de K₇. Les probabilités de coïncidence et les valeurs P affichées par les versions précédentes de cette page sont retirées. Ce qui reste : la rigidité (un rapport d'entiers ne se retouche pas, une seule mesure peut donc rejeter une relation) et une liste écrite de tout ce qui a été posé plutôt que dérivé.",
 papers_title='Articles &amp; preuves',
 papers_note='Version 3.6 de l\'article du cadre. La dernière version déposée est toujours au <a href="%s">DOI concept Zenodo</a> ; la version 3.5 se lit avec son <a href="%s">erratum</a>.' % (CONCEPT, ERR),
 cards=[('Article principal (v3.6)', "<em>The K₇ Dictionary: Testing G&#8322; Topology against Particle Physics and Cosmology.</em> La correspondance, son dictionnaire, son registre des résidus, les 33 relations, le test look-elsewhere et la règle de décision.", [('Markdown', MD % 'main'), ('Zenodo', CONCEPT)]),
        ('S1 : Fondations (v3.6)', "E&#8328;, G&#8322; et la topologie supposée pour K&#8327;. Aucune variété compacte de nombres (21, 77) n'est construite à ce jour.", [('Markdown', MD % 'S1_foundations')]),
        ('S2 : Les 33 relations (v3.6)', "L'arithmétique de chaque relation, les choix de dictionnaire qu'elle fait et son statut.", [('Markdown', MD % 'S2_derivations')]),
        ('S3 : Jeu de données (v3.6)', 'Données de référence des 33 relations, et 62 entrées conditionnelles ou diagnostiques qui ne sont pas comptées comme prédictions.', [('Markdown', MD % 'S3_observables')]),
        ('S4 : Look-elsewhere (v3.6)', 'Le test préenregistré où chaque concurrent cherche ses propres formules, et des diagnostics descriptifs.', [('Markdown', MD % 'S4_sieve_diagnostics')]),
        ('Article A &mdash; Structure G&#8322; certifiée', "Certificat de Newton&ndash;Kantorovich pour une métrique sans torsion voisine, sur une région de couture. Il ne construit pas un K&#8327; compact. Zenodo 19892350.", L['en']['cards'][5][2]),
        ('Article B &mdash; Géométrie spectrale', 'Spectre du laplacien et formes harmoniques de la métrique de couture approchée. Zenodo 19893371.', L['en']['cards'][6][2]),
        ('Article C &mdash; Newton-Kantorovich sur K3', 'Diagnostics NK sur une métrique K3 de Donaldson (CI(2,2,2)). Zenodo 19708916.', L['en']['cards'][7][2]),
        ('Article D &mdash; Note analytique de Donaldson', 'Ansatz G&#8322; explicite en forme close sur un col K3-coassociatif, avec certificat de Wirtinger à 5 couches. Zenodo 20039066.', L['en']['cards'][8][2]),
        ('Article E &mdash; Adiabatique ramifié de rang 1', "Cadre analytique conditionnel pour le col. Sa donnée n'est pas réalisable telle que posée (erratum, section 2). Zenodo 21215956.", L['en']['cards'][9][2]),
        ('Preuves Lean 4', "156 fichiers, 14 axiomes (4 issus de la littérature, 10 certificats d'intervalles), aucun sorry. La formalisation vérifie l'arithmétique des 33 relations ; elle n'établit ni leur contenu physique ni l'existence de K&#8327;.", [('Dépôt', 'https://github.com/Arithmon/K7-Lean')])],
 dec_title='Règle de décision',
 dec_intro="Les relations sont énoncées comme des égalités exactes. Une relation est rejetée quand sa série de référence (PDG, NuFIT, Planck, CODATA) exclut sa valeur à 3&sigma;. La règle n'a pas de clause de réparation : une relation qui échoue n'est pas sauvée en changeant sa formule, son unité, son échelle ou son jeu de données.",
 dec_head=['Relation', 'Valeur', 'Rejetée quand', 'Où'],
 decs=[(DCP+', la phase 2&pi;&middot;197/360', '197&deg;', "un ajustement global dont l'intervalle à 3&sigma; exclut 197&deg; ; l'assignation d'unité est rejetée avec elle", 'DUNE, Hyper-Kamiokande'),
       (T23, '6/11', "un ajustement global dont l'intervalle à 3&sigma; exclut 6/11, dans l'un ou l'autre octant", 'DUNE, Hyper-Kamiokande'),
       ('sin<sup>2</sup>&theta;<sub>12</sub>', '4/13', "un ajustement global dont l'intervalle à 3&sigma; exclut 4/13", "JUNO (première mesure 0,3092 &plusmn; 0,0087 ; environ quatre fois plus serré que l'ajustement global actuel après six ans)"),
       ('m<sub>&tau;</sub>/m<sub>e</sub> et Q<sub>Koide</sub>', '1776,74 et 1776,97 MeV pour m<sub>&tau;</sub>', "une valeur de m<sub>&tau;</sub> dont l'intervalle à 3&sigma; exclut la valeur, chaque relation séparément", 'Belle II, BES III'),
       ('N<sub>gen</sub>', '3', 'une quatrième génération séquentielle', 'LHC, FCC'),
       ('m<sub>s</sub>/m<sub>d</sub>', '20', "une détermination sur réseau, avec incertitude, dont l'intervalle à 3&sigma; exclut 20", 'QCD sur réseau')],
 verdicts="<strong>Verdicts en cours.</strong> Six relations sont déjà rejetées comme égalités exactes et gardées seulement comme proximités numériques : &alpha;<sup>&minus;1</sup>, "+W+", m<sub>&mu;</sub>/m<sub>e</sub>, m<sub>&mu;</sub>/m<sub>&tau;</sub>, m<sub>b</sub>/m<sub>t</sub> et m<sub>W</sub>/m<sub>Z</sub>. "+T23+" est <strong>en tension</strong> : le meilleur ajustement de NuFIT 6.1 est dans l'octant inférieur, et 6/11 se trouve dans son intervalle à 3&sigma;. Deux mesures contradictoires, hors des séries de référence, sont rapportées à côté de leur classe : h = 167/248 s'accorde avec Planck et est exclu par l'échelle des distances SH0ES à 5,5&sigma; ; les relations de densité s'accordent avec Planck et sont mises sous tension par les oscillations acoustiques de baryons de DESI (deuxième livraison de données) : environ 2&sigma; avec DESI seul, et &minus;3,3&sigma;, +3,4&sigma; et &minus;3,1&sigma; pour &Omega;<sub>&Lambda;</sub>/&Omega;<sub>m</sub>, &Omega;<sub>m</sub>/&Omega;<sub>&Lambda;</sub> et &Omega;<sub>DE</sub> avec DESI et le fond diffus cosmologique combinés (&minus;3,0&sigma; pour h). Un rejet rejette une relation et l'assignation qui l'a produite, pas le programme à lui seul. Chaque verdict est consigné, favorable ou non, dans le <a href=\"https://github.com/arithmon/program/blob/main/CONFRONTATIONS.md\">tableau des confrontations du programme</a>.",
 v35='Zenodo (cadre v3.5)',
)
L['fr'] = fr

def build(lang, path):
    c = L[lang]; t = open(path, encoding='utf-8').read()
    def between(a, b, new):
        nonlocal t
        i = t.index('<!-- ========== %s ========== -->' % a); j = t.index('<!-- ========== %s ========== -->' % b)
        t = t[:i] + '<!-- ========== %s ========== -->\n' % a + new + t[j:]
    t = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % c['meta'], t, count=1)
    t, n = re.subn(r'<p class="tagline">.*?</p>', '<p class="tagline">\n      ' + '\n      '.join(c['tagline']) + '\n    </p>', t, count=1, flags=re.S)
    assert n == 1
    res = '\n\n'.join([p(c['res_intro']),
        '    ' + H3 + '\n      ' + c['h_classes'] + '\n    </h3>', table(c['classes_head'], c['classes']),
        '    ' + H3 + '\n      ' + c['h_sample'] + '\n    </h3>', table(c['sample_head'], c['sample']), p(c['sample_note']),
        '    ' + H3 + '\n      ' + c['h_lee'] + '\n    </h3>', p(c['lee_intro']), table(c['lee_head'], c['lee']), p(c['lee_note'])])
    between('RESULTS', 'PAPERS', sec('results', c['res_title'], res))
    between('PAPERS', 'WORKSHOPS', sec('papers', c['papers_title'], p(c['papers_note']) + '\n\n    <div class="cards">\n' + '\n'.join(card(*k) for k in c['cards']) + '\n    </div>'))
    between('FALSIFICATION', 'FOOTER', sec('falsification', c['dec_title'], '\n\n'.join([p(c['dec_intro']), table(c['dec_head'], c['decs']), p(c['verdicts'])])))
    a = '<li><a href="https://doi.org/10.5281/zenodo.20070101">'
    assert t.count(a) == 1
    if 'zenodo.21296168">%s</a>' % c['v35'] not in t:   # posé une seule fois ; relance sans effet
        t = t.replace(a, '<li><a href="https://doi.org/10.5281/zenodo.21296168">%s</a></li>\n          ' % c['v35'] + a)
    assert t.count('K₇ Framework v3.5</span>') + t.count('K₇ Framework v3.6</span>') == 1
    t = t.replace('K₇ Framework v3.5</span>', 'K₇ Framework v3.6</span>')
    open(path, 'w', encoding='utf-8').write(t)
build('en', D + '/index.html'); build('fr', D + '/index.fr.html')
