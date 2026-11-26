#!/usr/bin/env python3
"""k7_v3_6_surfaces_lint.py -- les surfaces publiques de K7 contre la v3.6.

Étape 4 de la v3.6 (décision de Brieuc, 2026-11-10 : « tout réécrire »).
Le papier 3.6 retire des affirmations que le wiki, le site docs/ et les
références du dépôt public K7 affichent encore. Ce lint dit, fichier par
fichier, ce qui reste.

Deux contrôles, tous deux DÉRIVÉS (rule_derive_dont_name) :

  1. AFFIRMATIONS RETIRÉES. Une liste de motifs que la 3.6 retire (main
     §4.2, §7.2, §12.1). Une occurrence est tolérée si son paragraphe dit
     lui-même qu'elle est retirée (« withdrawn », « earlier versions »,
     « retiré », ...) : le README 3.6 cite 10⁻³⁴⁶ pour le retirer.
  2. CHIFFRES COURANTS. Les classes des 33 relations sont lues de
     observables.json par k7_v3_6_table_sec4.classify (la même fonction que
     la table du §4.1) ; les chiffres du look-elsewhere de l'artefact du
     closeout. Une page qui écrit une classe ou un compte périmé rougit ;
     si la source changeait, ce contrôle rougirait aussi.

CE QUE « 0 DÉFAUT » VEUT DIRE : aucune des formules retirées CONNUES de ce
lint. Ce n est pas une relecture. Une page n entre dans DONE qu après avoir
été lue en entier contre le papier (leçon du 2026-11-26 : une page DONE à
0 défaut portait la formule de Koide inversée).

Sorties : table par fichier ; code 1 si un fichier de --strict (ou de la
liste DONE ci-dessous) porte encore un défaut. Les pages pas encore revues
sont listées, sans faire échouer.

Usage :
  k7_v3_6_surfaces_lint.py [--k7 DIR] [--strict F ...] [--show F] [--all]
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
K7_DEFAULT = os.path.join(os.path.dirname(ROOT), "K7")

# Pages hors périmètre : archives datées, sources des papiers, billets de blog
# (textes d'auteur datés), rapports d'audit et de chantier analytique.
EXCLUDE = re.compile(
    r"^(legacy/|audit/|paper/|certificates/|scripts/|"
    r"publications/papers/(markdown|tex|legacy|pdf|notebooks)/|"
    r"publications/validation/legacy/|publications/validation/v3\.6/canonical/|publications/validation/v3\.6_generators/canonical/|"
    r"publications/outreach/(?!k7_one_page)|"
    r"publications/ERRATUM_|"
    r"docs/wiki/Blog-|docs/openwave-candidate|docs/stage[DE]_|"
    r"docs/stale_artifact|docs/mission_progress|docs/analytic_status|"
    r"docs/figures/archive/|docs/notebooks/|"
    r"CHANGELOG\.md$|CODE_OF_CONDUCT|CONTRIBUTING|SECURITY|"
    r".*lint_report\.json$|cross_repo_report\.json$)"
)
EXT = (".md", ".html", ".json", ".csv", ".cff", ".yml")

# Pages déclarées revues pour la 3.6 : un défaut y fait échouer le lint.
DONE = [
    "README.md",
    "docs/wiki/Home.md", "docs/wiki/Home.fr.md",
    "docs/index.html", "docs/index.fr.html",
    # générées par k7_v3_6_surface_pages.py
    "docs/wiki/Statistical-Evidence.md", "docs/wiki/Statistical-Evidence.fr.md",
    "publications/references/STATISTICAL_EVIDENCE.md",
    "docs/wiki/Validation-Summary.md", "docs/wiki/Validation-Summary.fr.md",
    "docs/wiki/Observable-Reference.md", "docs/wiki/Observable-Reference.fr.md",
    "publications/references/OBSERVABLE_REFERENCE.md", "publications/references/observables.csv",
    "publications/validation/README.md", "publications/validation/v3.6/README.md",
    "docs/FAQ.md", "docs/FAQ.fr.md", "docs/wiki/FAQ.md", "docs/wiki/FAQ.fr.md",
    "docs/GIFT_EXEC_SUMMARY.md", "docs/GIFT_EXEC_SUMMARY.fr.md",
    "docs/GIFT_FOR_EVERYONE.md", "docs/GIFT_FOR_EVERYONE.fr.md",
    "docs/wiki/GIFT-for-Everyone.md", "docs/wiki/GIFT-for-Everyone.fr.md",
    "docs/wiki/For-Physicists.md", "docs/INFO_GEO_FOR_PHYSICISTS.md",
    "publications/references/Bibliography.md", "publications/papers/README.md",
    "docs/wiki/Glossary.md", "docs/wiki/External-Resources.md", "docs/figures/k7_blueprint.html", "docs/README.md",
    "docs/wiki/Getting-Started.md", "docs/wiki/Getting-Started.fr.md",
    "docs/wiki/Site-Map.md", "docs/wiki/Site-Map.fr.md",
    # générées par k7_v3_6_deposit_pages.py (lot du dépôt)
    "CITATION.md", "docs/wiki/Citation-Guide.md", "CITATION.cff",
    "STRUCTURE.md", "docs/wiki/Repository-Structure.md",
    "docs/wiki/Paper-Main-Framework.md", "docs/wiki/Paper-S1-Foundations.md", "docs/wiki/Paper-S2-Derivations.md",
    "docs/wiki/Changelog-Highlights.md",
    "publications/references/README.md", "publications/references/GIFT_ATLAS.json",
    # générées par k7_v3_6_reader_pages.py (2026-11-26)
    "docs/LEAN_FOR_PHYSICS.md", "docs/wiki/Lean-Formalization.md", "docs/wiki/For-Formalization-Experts.md",
    "docs/GIFTPY_FOR_GEOMETERS.md", "docs/wiki/For-Geometers.md",
    # réécrites le 2026-11-26 (revues indépendantes)
    "CLAUDE.md", "publications/outreach/k7_one_page.md", "docs/GLOSSARY.md",
    "publications/validation/v3.6_generators/README.md",
]

# Pages dont les tables sont COPIÉES du jeu de données ou du papier : la source
# d'une entrée (« PDG 2024 (BBN review) » pour Y_p, « PDG 2025 » pour les valeurs
# héritées B10–B19) y est celle que le jeu de données déclare. Le motif old-data,
# écrit pour la prose, ne s'y applique pas.
DATA_PAGES = {
    "docs/wiki/Observable-Reference.md", "docs/wiki/Observable-Reference.fr.md",
    "publications/references/OBSERVABLE_REFERENCE.md", "publications/references/observables.csv",
    "publications/references/GIFT_ATLAS.json",
}

# Un paragraphe qui porte l'un de ces mots PARLE d'un retrait : toléré.
RETRACT = re.compile(
    r"withdraw|withdrawn|earlier version|previous version|versions? up to|"
    r"version 3\.[0-5] (described|reported|wrote|read)|v3\.[0-5] (described|reported|wrote)|"
    r"no longer|superseded|historical|retir[ée]|versions? antérieure|versions? précédente|"
    r"n'est plus|ne sont plus|historique|jusqu'à la 3\.5|archive",
    re.I,
)

# (clé, motif, ce que la 3.6 dit)
WITHDRAWN = [
    ("zero-param", r"zero[- ](free[- ])?(adjustable[- ])?param|zéro paramètre|no free param|sans paramètre libre|aucun paramètre libre|free parameters\*?\*? *\| *0",
     "§3.3 : pas de paramètre CONTINU, mais un registre de résidus R1–R12 (choix posés)"),
    ("derive", r"\bderiv(es|ing|ed) (the |all |every )?(standard[- ]model|sm |physical |fundamental )?(constants|parameters)|dérive (les |des )?(constantes|paramètres)|from pure geometry|de la (pure|seule) géométrie",
     "§3.4 : correspondance déclarée, pas une dérivation"),
    ("95-obs", r"95 (observables|predictions|prédictions)|95-observable",
     "§4.5 : 33 relations + 62 entrées conditionnelles ou diagnostiques"),
    ("mean-dev", r"mean dev(iation|\.)?|déviation moyenne|écart moyen",
     "§4.2 : la moyenne des écarts est retirée ; cinq classes, pas un score"),
    ("p-value", r"10⁻¹³⁸|10⁻³⁴⁶|10⁻¹³³|10\^\{?-1[34]\d|2 ?× ?10⁻⁵|5 ?× ?10⁻⁶|σ ?> ?4\.2|bayes factor|facteur de bayes|westfall|3,?070,?396|192[ ,]?349|3M\+|unique among|better than K₇",
     "§7.2 : probabilités de coïncidence et P retirés ; issue préenregistrée : aucune valeur p dans le texte"),
    # motifs ajoutés le 2026-11-26 : trouvés par deux revues indépendantes sur des pages que ce lint
    # donnait à 0 défaut (il ne voit que les formules qu on lui a apprises)
    ("p-reported", r"\bP ?= ?0[.,]\d|P_global ?= ?0[.,]\d|global p-value (of |is )?\*{0,2}0[.,]\d|valeur p globale (de |vaut )\*{0,2}0[.,]\d",
     "préinscription : sous LEE-RETRAIT la valeur p sort du texte ; comptes et proportions seulement"),
    ("before-any-run", r"before any run|avant tout passage,|before the first run",
     "un pilote de 9 vocabulaires, déclaré, a tourné avant le commit de la préinscription : « before any full run »"),
    ("koide-inverted", r"\(√m_e ?\+ ?√m_μ ?\+ ?√m_τ\)² ?/ ?\(m_e",
     "Q = (m_e + m_μ + m_τ)/(√m_e + √m_μ + √m_τ)² = 2/3, pas l inverse"),
    ("27-phi", r"27\^φ ?≈ ?206[.,]7",
     "27^φ = 207,01 ; 206,77 est la valeur mesurée"),
    ("existence", r"guarantees? (that )?K₇ can exist|garantit que K₇|explains Koide|explique Koide|theorem gives N_gen|"
                  r"well below Joyce|Betti numbers confirmed spectrally",
     "§9 : aucune variété compacte (21, 77) connue ; N_gen = 3 reproduit, pas prédit"),
    ("old-lean", r"290\+ (exact )?relations|zero domain-specific axioms|all_75_relations_certified|All 7 axioms|"
                 r"127 relations|213[- ]conjunct",
     "§8 : 14 axiomes (4 + 10), relations_v36_certified ; compter depuis K7-Lean"),
    ("tcs-open", r"non-orthogonal TCS|[Oo]rthogonal (TCS|twisted connected sums?) (is|are) excluded|yield b₂ ≤ 9",
     "§2.3, S1 §8.3 : toute TCS ordinaire est exclue par parité ; seules les extra-twisted restent ouvertes"),
    ("cp-band", r"182° ?(to|,|–|-) ?212°|\[182°?, ?212°?\]",
     "§4.3, §11 : valeur ponctuelle 197°, règle D1 ; plus de bande"),
    ("survivor", r"unique survivor|sieve-distinguished|seul survivant|survivant unique",
     "§7.1 : aucun ne passe N2"),
    ("pure-geom-cp", r"197° ?\(?pure|pure(ly)? geometr\w+ prediction|prédiction purement géométrique",
     "§4.3 : 197 est lu en degrés par une assignation d'unité (R6)"),
    ("index-thm", r"index theorem (gives|yields|fixes|forces)|théorème de l'indice (donne|fixe|impose)",
     "§12.1 : lecture de N_gen = 3 par un théorème de l'indice retirée"),
    ("jk-realise", r"joyce[–-]karigiannis (construction|route) (realis|realiz|gives|yields)|224 ?×",
     "erratum §9 : la route JK ne réalise pas (21, 77)"),
    ("lean-146", r"14[36] (\.lean )?(files|fichiers)",
     "S3.7 : 156 fichiers, 14 axiomes (K7-Lean 34ce857)"),
    ("lean-conj", r"(213|140)[- ](certified )?(conjunct|conjonction)|certificat à 213",
     "compte de conjonctions non publié par K7-Lean (README, 34ce857) : citer relations_v36_certified"),
    ("old-data", r"PDG 202[0-5]|NuFIT [0-5]\.\d|NuFIT 6\.0",
     "§4 : PDG 2026, NuFIT 6.1, Planck 2018, CODATA 2022"),
    ("cp-band", r"182 ?°|\[182|182&deg;|outside \[0\.2295|\[19, 21\]",
     "§11 : valeur ponctuelle et règle à 3σ de la série de référence ; les bandes sont retirées"),
    ("old-title", r"Conditional Topological Relations",
     "titre 3.6 : The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology"),
]
WITHDRAWN = [(k, re.compile(p, re.I), w) for k, p, w in WITHDRAWN]


def current_facts():
    """Chiffres courants, lus des sources (jamais recopiés ici)."""
    sys.path.insert(0, HERE)
    out = subprocess.run(
        [sys.executable, os.path.join(HERE, "k7_v3_6_table_sec4.py"), "--counts"],
        capture_output=True, text=True, check=True).stdout
    counts = {}
    for line in out.splitlines():
        m = re.match(r"(\w+): (\d+)", line)
        if m:
            counts[m.group(1)] = int(m.group(2))
    return counts


def stale_number_patterns(c):
    """Motifs de chiffres PÉRIMÉS, construits depuis les chiffres courants.

    « of which 19 lie within 2σ » / « dont 19 à moins de 2σ » sont les comptes
    réduits du §4.4 (sans det(g), sans κ_T) : non contrôlés ici."""
    w2, ten = c["within_2sigma"], c["tension"]
    pats = []
    # « N within 2σ » / « N lie within two standard deviations » avec N ≠ courant
    pats.append(("class-2σ", re.compile(
        r"(?<!of which )(?<!dont )\b(\d{2}) (of the 33 )?(relations? )?(lie |are |sont )?(within|inside|à moins de|dans) (2 ?σ|two standard|deux écarts)", re.I),
        lambda m: int(m.group(1)) != w2,
        "%d à moins de 2σ (dérivé de observables.json)" % w2))
    pats.append(("class-row", re.compile(r"\|\s*(within 2σ|à moins de 2σ)\s*\|\s*(\d+)\s*\|", re.I),
                 lambda m: int(m.group(2)) != w2, "%d à moins de 2σ" % w2))
    pats.append(("tension-row", re.compile(r"\|\s*tension[^|]*\|\s*(\d+)\s*\|", re.I),
                 lambda m: int(m.group(1)) != ten, "%d en tension" % ten))
    # 2026-11-11 : la ligne et les phrases des proximités, et la valeur de m_W/m_Z, n'étaient pas contrôlées
    # (le passage de A21 en proximité n'a rougi que sur la ligne des tensions).
    exc = c["excluded_3sigma"]
    pats.append(("proximity-row", re.compile(r"\|\s*proximit[^|]*\|\s*(\d+)\s*\|", re.I),
                 lambda m: int(m.group(1)) != exc, "%d proximités" % exc))
    pats.append(("tension-count", re.compile(r"\b(\d+) (are |sont )?(in|en) tension\b", re.I),
                 lambda m: int(m.group(1)) != ten, "%d en tension" % ten))
    pats.append(("proximity-count", re.compile(
        r"\b(\d+) (are |sont )?(rejected|excluded|rejetées|exclues) (as exact|comme égalités)", re.I),
        lambda m: int(m.group(1)) != exc, "%d rejetées comme égalités exactes" % exc))
    pats.append(("mW/mZ-stale", re.compile(r"0[.,]88136\(15\)"), lambda m: True,
                 "m_W/m_Z se compare au rapport des masses publiées, 0.881285(87)"))
    return pats


def paragraphs(text):
    """(numéro de première ligne, texte) par paragraphe ; une ligne de table = un paragraphe."""
    out, buf, start = [], [], 1
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("|"):
            if buf:
                out.append((start, "\n".join(buf)))
                buf = []
            if line.lstrip().startswith("|"):
                out.append((i, line))
            start = i + 1
        else:
            if not buf:
                start = i
            buf.append(line)
    if buf:
        out.append((start, "\n".join(buf)))
    return out


def lint_file(path, stale, skip=()):
    try:
        text = open(path, encoding="utf-8").read()
    except (UnicodeDecodeError, OSError):
        return []
    hits = []
    for ln, para in paragraphs(text):
        tolerated = bool(RETRACT.search(para))
        for key, rx, why in WITHDRAWN:
            if key in skip:
                continue
            m = rx.search(para)
            if m and not tolerated:
                hits.append((ln, key, m.group(0), why))
        for key, rx, bad, why in stale:
            for m in rx.finditer(para):
                if bad(m) and not tolerated:
                    hits.append((ln, key, m.group(0), why))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k7", default=os.environ.get("K7_DIR", K7_DEFAULT))
    ap.add_argument("--strict", nargs="*", default=[])
    ap.add_argument("--show", default="", help="détail des défauts d'un fichier")
    ap.add_argument("--all", action="store_true", help="lister aussi les fichiers propres")
    args = ap.parse_args()

    k7 = os.path.abspath(args.k7)
    files = subprocess.run(["git", "-C", k7, "ls-files"], capture_output=True,
                           text=True, check=True).stdout.split("\n")
    files = [f for f in files if f.endswith(EXT) and not EXCLUDE.match(f)]
    branch = subprocess.run(["git", "-C", k7, "branch", "--show-current"],
                            capture_output=True, text=True).stdout.strip()
    counts = current_facts()
    stale = stale_number_patterns(counts)
    strict = set(DONE) | set(args.strict)

    print("K7 : %s (branche %s) — %d surfaces dans le périmètre" % (k7, branch, len(files)))
    print("classes courantes (observables.json) : %s" % counts)
    missing = sorted(strict - set(files))
    if missing:
        print("STRICT introuvables : %s" % missing)

    total, dirty, fail = 0, 0, []
    rows = []
    for f in files:
        hits = lint_file(os.path.join(k7, f), stale, skip=("old-data",) if f in DATA_PAGES else ())
        if args.show and f == args.show:
            for ln, key, txt, why in hits:
                print("  %s:%d [%s] « %s » — %s" % (f, ln, key, txt, why))
        total += len(hits)
        if hits:
            dirty += 1
            keys = {}
            for _, key, _, _ in hits:
                keys[key] = keys.get(key, 0) + 1
            rows.append((len(hits), f, keys))
            if f in strict:
                fail.append(f)
        elif args.all:
            rows.append((0, f, {}))
    for n, f, keys in sorted(rows, reverse=True):
        tag = "REVUE" if f in strict else "     "
        print("%4d %s %-52s %s" % (n, tag, f, " ".join("%s:%d" % kv for kv in sorted(keys.items()))))
    print("\n%d défauts dans %d fichiers sur %d ; %d pages déclarées revues, %d en défaut"
          % (total, dirty, len(files), len(strict), len(fail)))
    if fail or missing:
        print("ÉCHEC : %s" % (fail + missing))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
