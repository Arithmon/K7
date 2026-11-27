#!/usr/bin/env python3
"""k7_v3_6_deposit_pages.py -- le « lot du dépôt » des surfaces de K7, v3.6.

Dernier lot de l'étape 4 (décision de Brieuc, 2026-11-10 : « tout réécrire »).
Écrit dans le clone public K7 les pages qui dépendent du dépôt de la 3.6 :

  CITATION.md, docs/wiki/Citation-Guide.md, CITATION.cff
  STRUCTURE.md, docs/wiki/Repository-Structure.md
  docs/wiki/Paper-Main-Framework.md, Paper-S1-Foundations.md, Paper-S2-Derivations.md
  docs/wiki/Changelog-Highlights.md
  publications/references/README.md, publications/references/GIFT_ATLAS.json
  README.md (les six régions marquées `<!-- v36:nom -->` seulement), publications/papers/README.md
  publications/papers/pdf/k7_framework_3_6_*.pdf, tex/k7_framework_3_6_*.tex,
  tex/gift_3.6_bib.tex, tex/gift_preamble.tex, markdown/k7_framework_3_6_*.md
                                           (copies conformes de canonical/papers/framework/)

DEUX ÉTATS, un seul texte. Sans --version-doi : la 3.6 n'est pas déposée, les
pages citent le DOI concept et disent que la version publiée est la 3.5. Avec
--version-doi 10.5281/zenodo.N : la 3.6 est la version courante. Le DOI de
version ne s'écrit nulle part avant d'exister (registre dois.json : « au
dépôt, jamais après coup »).

DÉRIVÉ, jamais recopié (rule_derive_dont_name) : les DOI de dois.json ; les
nombres de pages des PDF (pdfinfo) ; les cinq classes de observables.json
(k7_v3_6_table_sec4.classify) ; les plans de sections et la table des vingt
constantes, lus des sources markdown ; le nombre de fichiers Lean, compté dans
le clone K7-Lean ; les quatorze axiomes et « 31 of the 33 », contrôlés
présents dans les sources. Les chemins nommés par STRUCTURE.md sont contrôlés
existants dans K7.

Usage :
  k7_v3_6_deposit_pages.py [--k7 DIR] [--check] [--version-doi DOI] [--date AAAA-MM-JJ]
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from k7_v3_6_surface_pages import read, table_after, front, K7_DEFAULT  # noqa: E402
from k7_v3_6_table_sec4 import classify  # noqa: E402

# Les modules importés enveloppent déjà sys.stdout en UTF-8 ; ne pas l'envelopper deux fois
# (le premier enveloppeur, ramassé, fermerait le tampon).
if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

LATEX = os.path.join(ROOT, "canonical", "papers", "framework", "latex")
GH = "https://github.com/Arithmon/K7/blob/main/"
RAW = "https://github.com/Arithmon/K7/raw/main/"
TITLE = "The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology"
DOCS = [  # (clé, nom de fichier K7 sans extension, titre, source md)
    ("main", "k7_framework_3_6_main", TITLE, "physics_main.md"),
    ("S1", "k7_framework_3_6_S1_foundations",
     "Supplement S1: Mathematical Foundations. E₈ Exceptional Lie Algebra, G₂ Holonomy Manifolds, and the Topological Status of K₇",
     "supplement_foundations.md"),
    ("S2", "k7_framework_3_6_S2_derivations",
     "Supplement S2: The 33 Relations. Arithmetic, Dictionary Choices and Status", "supplement_derivations.md"),
    ("S3", "k7_framework_3_6_S3_observables",
     "Supplement S3: Observable Dataset. 33 Relations Compared with Measurement; 62 Conditional and Diagnostic Entries",
     "supplement_observables.md"),
    ("S4", "k7_framework_3_6_S4_sieve_diagnostics",
     "Supplement S4: Sieve and Look-Elsewhere Diagnostics", "supplement_sieve_diagnostics.md"),
]
COMPANIONS = [  # (lettre, clé dois.json, clé bibtex, titre, note)
    ("A", "g2_metric_certified_torsion_free", "k7_paper_a_certified_neck",
     "A Certified Torsion-Free G₂ Structure on a TCS Neck Model via Computer-Assisted Proof",
     "Newton--Kantorovich certificate for a nearby torsion-free metric on a seam region; it does not construct a compact K₇"),
    ("B", "g2_spectral_geometry", "k7_paper_b_spectral",
     "Spectral Geometry of an Explicit G₂ Metric: Laplacian Spectrum and Harmonic Forms",
     "Laplacian spectrum and harmonic forms of the approximate seam metric"),
    ("C", "k3_donaldson_embedding", "k7_paper_c_k3_nk",
     "Newton--Kantorovich diagnostics on a Donaldson K3 metric: two β estimates, machine-checked inequalities",
     "NK diagnostics on a Donaldson-balanced metric on the K3 surface CI(2,2,2)"),
    ("D", "adiabatic_neck_hyperkahler", "k7_paper_d_donaldson",
     "An Explicit Closed-Form G₂ Ansatz on a K3-Coassociative Neck with Hyperkähler Rotation and Picard-Lefschetz Wirtinger Certificate",
     "Neck-level certificate; not a compact K₇ torsion-free theorem"),
    ("E", "rank_one_branched_adiabatic", "k7_paper_e_rank_one_branched",
     "A conditional analytic framework for rank-one branched Kovalev--Lefschetz adiabatic limits",
     "Conditional analytic framework; the datum-level instantiation at D₀ is not realisable as posed (v3.5 erratum, sections 2 and 7.4)"),
    ("M", "counting_coincidences_preprint", "sieve_methodology",
     "A reproducible standard for arithmetic coincidence claims in fundamental physics",
     "The Sieve methodology and its four-null scorecard for the K₇ relations"),
]


# ---------------------------------------------------------------- faits dérivés
def facts(k7):
    f = {}
    reg = json.load(open(os.path.join(ROOT, "canonical", "data", "dois.json"), encoding="utf-8"))
    dep = {e["key"]: e for e in reg["deposits"]}
    f["concept"] = dep["k7_framework"]["concept"]
    ver = {v["version"]: v["doi"] for v in dep["k7_framework"]["versions"]}
    f["doi35"], f["doi34"], f["doi33"] = ver["v3.5"], ver["main"], ver["3.3"]
    f["comp"] = {letter: dep[key]["concept"] for letter, key, *_ in COMPANIONS}
    for key, name, _t, _s in DOCS:
        pdf = os.path.join(LATEX, "k7_framework_3_6_%s.pdf" % key)
        out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
        f["pp_" + key] = int(re.search(r"Pages:\s+(\d+)", out).group(1))
    d = json.load(open(os.path.join(ROOT, "canonical", "data", "observables.json"), encoding="utf-8"))
    obs = {o["id"]: o for o in d["observables"]}
    f["obs"] = obs
    f["cls"] = classify(obs)
    n = {k: len(v) for k, v in f["cls"].items()}
    f.update(n33=sum(n.values()), n_total=len(obs), **{"n_" + k: v for k, v in n.items()})
    f["n_other"] = f["n_total"] - f["n33"]
    f["sym"] = lambda ids: ", ".join(obs[i]["symbol"] for i in ids)
    lean = os.path.join(os.path.dirname(k7), "K7-Lean")
    f["n_lean"] = sum(1 for r, ds, fs in os.walk(lean) if ".lake" not in r for x in fs if x.endswith(".lean"))
    s1, main = read("supplement_foundations.md"), read("physics_main.md")
    assert "fourteen axioms" in s1 and "four literature imports and ten interval certificates" in s1, "axiomes : S1 a changé"
    m = re.search(r"commit `([0-9a-f]{7})`", s1)
    f["lean_commit"] = m.group(1)
    assert "31 of the 33" in main, "LEE : main a changé"
    assert f["n_lean"] > 100, "clone K7-Lean introuvable à côté de K7"
    f["constants"] = table_after(main, "### 3.1 The structural constants")
    f["classes"] = table_after(main, "**The breakdown of the 33.**")
    f["sections"] = {key: [re.sub(r"^## ", "", l) for l in read(src).splitlines()
                           if re.match(r"## (\d+\.|S\d\.\d)", l)] for key, _n, _t, src in DOCS}
    return f


def lean_note(f):
    return ("%d Lean 4 files, 14 axioms (4 literature imports, 10 interval certificates), no sorry; "
            "the arithmetic of the 33 relations is collected in relations_v36_certified (commit %s)"
            % (f["n_lean"], f["lean_commit"]))


def classes_line(f):
    return ("%d within 2σ of measurement, %d in tension, %d excluded as exact equalities at more than 3σ "
            "and kept as proximities, %d inside a PDG range, %d with a non-Gaussian profile"
            % (f["n_within_2sigma"], f["n_tension"], f["n_excluded_3sigma"], f["n_in_range"], f["n_non_gaussian"]))


def doi_link(doi):
    return "[%s](https://doi.org/%s)" % (doi, doi)


# ---------------------------------------------------------------- CITATION
def citation(f, vdoi, date, wiki):
    dep = bool(vdoi)
    paper_doi = vdoi or f["concept"]
    month = "November"
    if dep:
        status = ("Version 3.6 is the current version (Zenodo %s). The concept DOI %s always resolves to the "
                  "latest version." % (doi_link(vdoi), doi_link(f["concept"])))
    else:
        status = ("**Version 3.6 is not deposited yet.** Until it is, the published version is 3.5 (Zenodo %s), "
                  "read together with its [erratum](%spublications/ERRATUM_v3.5.md). The entries below cite the "
                  "concept DOI %s, which always resolves to the latest deposited version; the version DOI of 3.6 "
                  "will be added at the deposit." % (doi_link(f["doi35"]), GH, doi_link(f["concept"])))
    out = ["# Citation Guide", "", "Citation formats for the K₇ framework, version 3.6 (formerly GIFT).", "",
           status, "", "## Framework (recommended)", "", "### BibTeX", "", "```bibtex",
           "@software{k7_framework,",
           "  title   = {The K₇ Framework (formerly GIFT)},",
           "  author  = {de La Fournière, Brieuc},",
           "  year    = {2026},",
           "  url     = {https://github.com/Arithmon/K7},",
           "  doi     = {%s}," % f["concept"],
           "  version = {3.6},",
           "  license = {MIT},",
           "  note    = {A declared correspondence between invariants of a G₂-holonomy seven-manifold and %d "
           "dimensionless parameters: %s (PDG 2026, NuFIT 6.1, Planck 2018). %s.}"
           % (f["n33"], classes_line(f), lean_note(f).replace("_", r"\_")),
           "}", "```", "", "### APA", "", "```",
           "de La Fournière, B. (2026). The K₇ Framework (formerly GIFT) (Version 3.6) [Software]. Zenodo. "
           "https://doi.org/%s" % f["concept"], "```", "", "### Chicago", "", "```",
           "de La Fournière, Brieuc. \"The K₇ Framework (formerly GIFT).\" Version 3.6. Zenodo, 2026. "
           "https://doi.org/%s." % f["concept"], "```", "", "---", "",
           "## Framework v3.6 papers", ""]
    for key, name, title, _src in DOCS:
        label = "Main paper" if key == "main" else key
        how = ("The K₇ Framework v3.6, %d pp." % f["pp_main"] if key == "main"
               else "The K₇ Framework v3.6, Supplement %s, %d pp." % (key, f["pp_" + key]))
        out += ["### %s" % label, "", "```bibtex",
                "@misc{k7_%s_v36," % key.lower(),
                "  title        = {%s}," % title,
                "  author       = {de La Fournière, Brieuc},",
                "  year         = {2026},",
                "  month        = {%s}," % month,
                "  howpublished = {%s}," % how,
                "  doi          = {%s}," % paper_doi,
                "  url          = {%spublications/papers/pdf/%s.pdf}" % (RAW, name),
                "}", "```", ""]
    pre = "" if not wiki else "https://github.com/Arithmon/K7/tree/main/"
    out += ["> Earlier versions: v3.5 (Zenodo %s, with its [erratum](%spublications/ERRATUM_v3.5.md)); "
            "v3.4 (Zenodo %s, files in [`publications/papers/legacy/v3.4/`](%spublications/papers/legacy/v3.4/)); "
            "v3.3 (Zenodo %s, files in [`publications/papers/legacy/v3.3/`](%spublications/papers/legacy/v3.3/)). "
            "Version 3.6 withdraws a number of statements of these versions; see the "
            "[changes from v3.5](%spublications/papers/markdown/k7_framework_3_6_CHANGELOG.md)."
            % (doi_link(f["doi35"]), GH, doi_link(f["doi34"]), pre, doi_link(f["doi33"]), pre, GH),
            "", "---", "", "## Companion papers (Zenodo)", "",
            "Cited by their concept DOI, as in the paper's reference list.", ""]
    for letter, _k, bib, title, note in COMPANIONS:
        d = f["comp"][letter]
        out += ["### [%s]" % letter, "", "```bibtex", "@misc{%s," % bib,
                "  title  = {%s}," % title, "  author = {de La Fournière, Brieuc},", "  year   = {2026},",
                "  doi    = {%s}," % d, "  url    = {https://doi.org/%s}," % d, "  note   = {%s}" % note,
                "}", "```", ""]
    out += ["---", "", "## Formal verification (K7-Lean)", "", "```bibtex", "@software{k7_lean,",
            "  title  = {K7-Lean (formerly GIFT Core): Formal Verification in Lean 4},",
            "  author = {de La Fournière, Brieuc},", "  year   = {2026},",
            "  url    = {https://github.com/Arithmon/K7-Lean},",
            "  note   = {%s. Formalization establishes the stated arithmetic, not the physical reading.}"
            % lean_note(f).replace("_", r"\_"),
            "}", "```", "", "---", "", "## DOI", "", "| Record | DOI |", "|--------|-----|"]
    if dep:
        out.append("| Framework v3.6 (current) | %s |" % doi_link(vdoi))
    out += ["| Framework, concept DOI (always the latest version) | %s |" % doi_link(f["concept"]),
            "| Framework v3.5%s | %s |" % ("" if dep else " (published version)", doi_link(f["doi35"])),
            "| Framework v3.4 | %s |" % doi_link(f["doi34"]),
            "| Framework v3.3 | %s |" % doi_link(f["doi33"])]
    for letter, _k, _b, title, _n in COMPANIONS:
        out.append("| [%s] %s | %s |" % (letter, title.split(":")[0].replace("--", "–"), doi_link(f["comp"][letter])))
    out += ["", "---", "", "## Version history", "",
            "Statements withdrawn by version 3.6 are not repeated in this table; the full record is in the "
            "[changelog](%sCHANGELOG.md)." % GH, "",
            "| Version | Date | What changed |", "|---------|------|--------------|",
            "| 3.6 | %s | New title; the framework is stated as a declared correspondence with its dictionary, "
            "residue register and decision rule; 33 relations compared with the most recent data in five classes; "
            "preregistered look-elsewhere test; several statistical and derivational claims of earlier versions "
            "withdrawn |" % (date or "2026-11"),
            "| 3.5 | 2026-07-10 | Renamed \"The K₇ Framework\"; S4 supplement added; erratum of 2026-08 to 2026-10 |",
            "| 3.4 | 2026-05-07 | Companion papers A to D published; Lean axiom reduction; K3 certificates |",
            "| 3.3 | 2026-01-12 to 2026-03-02 | 33 relations; neutrino formulas revised; Lean 4 as sole proof system |",
            "| 3.0 to 3.1 | 2025-12 | First Lean-certified relations; first explicit approximate G₂ metric |",
            "| 2.x | 2025-10 to 2025-11 | Framework reorganization |",
            "", "---", "", "## Usage in publications", "",
            "1. Cite the framework by the software entry above (concept DOI).",
            "2. Cite a specific statement by the paper or supplement that makes it, with the version number.",
            "3. Quote a relation with its status in the paper's table (main §4.1), not as a prediction of a "
            "derivation: the paper states a correspondence and a decision rule (main §11).", "",
            "### Example", "",
            "> \"The K₇ dictionary [1] assigns the leptonic CP phase the value 2π · 197/360, that is 197°, by a "
            "declared unit assignment; its decision rule rejects the relation if a global fit of the reference "
            "series excludes 197° at 3σ.\"", ">",
            "> [1] B. de La Fournière, \"%s,\" The K₇ Framework v3.6 (2026), https://doi.org/%s" % (TITLE, paper_doi),
            "", "---", "", "## License", "", "MIT License: see [LICENSE](%sLICENSE)" % ("" if not wiki else GH),
            "", "---", "", "**Version**: 3.6%s" % (" (%s)" % date if date else " (not yet deposited)"), ""]
    return "\n".join(out)


def cff(f, vdoi):
    ids = ["  - type: doi", "    value: %s" % f["concept"], "    description: >-",
           "      Concept DOI. Resolves to the latest version. USE THIS ONE."]
    if vdoi:
        ids += ["  - type: doi", "    value: %s" % vdoi, "    description: >-",
                "      Version DOI for \"The K7 Dictionary\", version 3.6 of the framework (2026)."]
    ids += ["  - type: doi", "    value: %s" % f["doi35"], "    description: >-",
            "      Version DOI for \"The K7 Framework\" v3.5 (2026)%s."
            % ("" if vdoi else ", the published version until 3.6 is deposited")]
    return "\n".join([
        "cff-version: 1.2.0", "title: \"The K7 Framework (formerly GIFT)\"", "message: >-",
        "  If you use this framework, please cite it using the concept DOI below.",
        "  The concept DOI always resolves to the most recent version; do not pin a",
        "  version DOI unless you specifically mean that version.", "type: software", "authors:",
        "  - family-names: \"de La Fournière\"", "    given-names: \"Brieuc\"",
        "repository-code: \"https://github.com/Arithmon/K7\"", "url: \"https://arithmon.github.io/K7/\"",
        "abstract: >-",
        "  A declared correspondence between the topological and Lie-theoretic",
        "  invariants of a G2-holonomy seven-manifold K7 with Betti numbers",
        "  (b2, b3) = (21, 77), together with E8xE8, and %d dimensionless" % f["n33"],
        "  Standard-Model and cosmological parameters, stated with its dictionary,",
        "  its residue register and a decision rule. It is presented as a candidate,",
        "  not as a derivation. Formerly published as GIFT (Geometric Information",
        "  Field Theory). Companion repository of Lean 4 arithmetic identities:",
        "  https://github.com/Arithmon/K7-Lean (formerly gift-framework/core).",
        "identifiers:"] + ids + [
        "keywords:", "  - G2 holonomy", "  - E8xE8", "  - Standard Model", "  - look-elsewhere effect",
        "  - Lean 4", "  - formal verification", "license: MIT", ""])


# ---------------------------------------------------------------- STRUCTURE
NAV = [  # (ce qu'on cherche, chemin relatif dans K7) ; chaque chemin est contrôlé existant
    ("Framework overview", "README.md"),
    ("Plain-language guide", "docs/GIFT_FOR_EVERYONE.md"),
    ("Main paper (v3.6)", "publications/papers/markdown/k7_framework_3_6_main.md"),
    ("The 33 relations, one by one", "publications/papers/markdown/k7_framework_3_6_S2_derivations.md"),
    ("Dataset description", "publications/papers/markdown/k7_framework_3_6_S3_observables.md"),
    ("Dataset (machine-readable)", "publications/references/observables.csv"),
    ("Look-elsewhere test (code, preregistration, results)", "publications/validation/v3.6/"),
    ("Generators of the tables and of the generated pages", "publications/validation/v3.6_generators/"),
    ("Changes from v3.5", "publications/papers/markdown/k7_framework_3_6_CHANGELOG.md"),
    ("Erratum to v3.5", "publications/ERRATUM_v3.5.md"),
    ("Paper A (certified seam metric)", "publications/papers/pdf/g2_certified_neck.pdf"),
    ("Paper B (spectral geometry)", "publications/papers/pdf/g2_spectral.pdf"),
    ("Companion notebooks", "publications/papers/notebooks/"),
    ("Blog posts and outreach", "publications/outreach/"),
    ("Earlier versions", "publications/papers/legacy/"),
    ("Technical definitions", "docs/GLOSSARY.md"),
    ("How to cite", "CITATION.md"),
]
TREE = """K7/
├── publications/
│   ├── papers/
│   │   ├── markdown/                  # Canonical sources
│   │   │   ├── k7_framework_3_6_main.md                 # Main paper (v3.6)
│   │   │   ├── k7_framework_3_6_S1_foundations.md       # S1: E₈, G₂, K₇ background
│   │   │   ├── k7_framework_3_6_S2_derivations.md       # S2: the 33 relations
│   │   │   ├── k7_framework_3_6_S3_observables.md       # S3: the dataset
│   │   │   ├── k7_framework_3_6_S4_sieve_diagnostics.md # S4: look-elsewhere
│   │   │   ├── k7_framework_3_6_CHANGELOG.md            # Changes from v3.5
│   │   │   ├── k7_framework_3_5_*.md                    # v3.5 (read with the erratum)
│   │   │   ├── g2_certified_neck.md                     # Paper A
│   │   │   └── g2_spectral.md                           # Paper B
│   │   ├── tex/                       # LaTeX sources (v3.6, v3.5, A, B)
│   │   ├── pdf/                       # PDFs (v3.6, v3.5, companion papers A to E)
│   │   ├── legacy/                    # v3.3 and v3.4 (archived)
│   │   ├── figures/
│   │   └── notebooks/                 # Companion notebooks (A, B)
│   ├── ERRATUM_v3.5.md                # Erratum to the published v3.5
│   ├── outreach/                      # Blog posts
│   ├── references/                    # Dataset and reference pages
│   │   ├── observables.csv            # The 95-entry dataset
│   │   ├── GIFT_ATLAS.json            # Constants and the 33 relations (generated)
│   │   ├── OBSERVABLE_REFERENCE.md
│   │   ├── STATISTICAL_EVIDENCE.md
│   │   └── Bibliography.md
│   └── validation/
│       ├── v3.6/                      # Look-elsewhere test of v3.6 (code, data, results)
│       ├── v3.6_generators/           # Generators of the tables and of the generated pages
│       └── legacy/                    # Earlier validation scripts (archived)
│
├── docs/                              # Guides and the Jekyll site
│   ├── index.html                     # Landing page (arithmon.github.io/K7)
│   ├── GIFT_FOR_EVERYONE.md           # Plain-language guide
│   ├── FAQ.md
│   ├── GLOSSARY.md
│   ├── INFO_GEO_FOR_PHYSICISTS.md
│   ├── GIFTPY_FOR_GEOMETERS.md
│   ├── LEAN_FOR_PHYSICS.md
│   └── wiki/                          # Wiki pages
│
├── README.md
├── CHANGELOG.md
├── CITATION.md / CITATION.cff
├── STRUCTURE.md                       # This file
└── LICENSE                            # MIT
"""
TREE_PATHS = ["publications/papers/tex", "publications/papers/pdf", "publications/papers/legacy/v3.3",
              "publications/papers/legacy/v3.4", "publications/papers/figures", "publications/papers/notebooks",
              "publications/papers/markdown/g2_certified_neck.md", "publications/papers/markdown/g2_spectral.md",
              "publications/references/Bibliography.md", "publications/references/OBSERVABLE_REFERENCE.md",
              "publications/references/STATISTICAL_EVIDENCE.md", "publications/validation/legacy",
              "docs/index.html", "docs/FAQ.md", "docs/INFO_GEO_FOR_PHYSICISTS.md", "docs/GIFTPY_FOR_GEOMETERS.md",
              "docs/LEAN_FOR_PHYSICS.md", "docs/wiki", "CHANGELOG.md", "CITATION.cff", "LICENSE"]


def structure(f, vdoi, date, k7):
    for p in [p for _w, p in NAV] + TREE_PATHS:
        assert os.path.exists(os.path.join(k7, p)), "STRUCTURE nomme un chemin absent de K7 : " + p
    nav = "\n".join("| %s | `%s` |" % (w, p) for w, p in NAV)
    core = "\n".join("| `%s.md` | %s | %d |" % (name, title.split(". ")[0] if key != "main" else title, f["pp_" + key])
                     for key, name, title, _s in DOCS)
    papers = ("Framework v3.6 (Zenodo %s; concept %s)" % (vdoi, f["concept"]) if vdoi else
              "Framework v3.6 (not yet deposited; concept DOI %s). Published version: v3.5 (Zenodo %s)"
              % (f["concept"], f["doi35"]))
    return """# Repository Structure

This repository holds the papers, the dataset and the documentation of the K₇ framework, version 3.6 (formerly GIFT).

## Directory layout

```
%s```

## Quick navigation

| Looking for | Go to |
|-------------|-------|
%s
| Lean 4 identities | [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) |

## Core documents (v3.6)

| File (`publications/papers/markdown/`) | Title | Pages (PDF) |
|----------------------------------------|-------|-------------|
%s

## Related repositories

| Repository | Content |
|------------|---------|
| [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) | Lean 4 identities, metric pipeline, giftpy (formerly `gift-framework/core`) |
| [Arithmon/Sieve](https://github.com/Arithmon/Sieve) | The look-elsewhere methodology used in main §7 |

## Version

**Current**: v3.6%s

**Relations**: %d, compared with measurement in five classes: %s (main §4.1; PDG 2026, NuFIT 6.1, Planck 2018). The other %d entries of the dataset are conditional or diagnostic and are not counted.

**Formal verification**: %s. It establishes the stated arithmetic, not the physical reading.

**Papers**: %s; companion papers A (%s), B (%s), C (%s), D (%s), E (%s).
""" % (TREE, nav, core, " (%s)" % date if date else " (in preparation)", f["n33"], classes_line(f), f["n_other"],
       lean_note(f).replace("relations_v36_certified", "`relations_v36_certified`"), papers,
       *[f["comp"][x] for x in "ABCDE"])


# ---------------------------------------------------------------- pages des papiers
def paper_links(f, vdoi, key, name):
    doi = (" | [**DOI: %s**](https://doi.org/%s)" % (vdoi, vdoi) if vdoi else
           " | concept DOI %s (version 3.6 not yet deposited)" % doi_link(f["concept"]))
    return ("[**PDF (%d pp.)**](%spublications/papers/pdf/%s.pdf)%s | [Markdown](%spublications/papers/markdown/%s.md)"
            % (f["pp_" + key], RAW, name, doi, GH, name))


def sections(f, key):
    return "\n".join("- %s" % s for s in f["sections"][key])


def paper_main(f, vdoi):
    return """# Paper: Main

**%s** (The K₇ Framework, v3.6)

*Brieuc de La Fournière (2026)*

%s

Supplements: [S1](Paper-S1-Foundations.html) (foundations, %d pp.) · [S2](Paper-S2-Derivations.html) (the 33 relations, %d pp.) · [S3](%spublications/papers/markdown/k7_framework_3_6_S3_observables.md) (dataset, %d pp.) · [S4](%spublications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md) (look-elsewhere, %d pp.) · [changes from v3.5](%spublications/papers/markdown/k7_framework_3_6_CHANGELOG.md)

---

## What the paper states

A **declared correspondence**. The topological and Lie-theoretic invariants of a compact seven-manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with E₈×E₈, are assigned to %d dimensionless Standard-Model and cosmological parameters by explicit closed forms. The paper presents the correspondence as a privileged candidate, not as a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable.

What the paper does is make the correspondence auditable. It gives the full **dictionary** (twenty structural constants and a grammar), a **residue register** of everything that was set by choice (R1 to R12), and a **decision rule** with no repair clause.

---

## The 33 relations against the most recent data

Generated from the dataset (main §4.1; PDG 2026, NuFIT 6.1, Planck 2018; 1σ uncertainties).

%s

The 33 are not 33 independent tests: three sectors are overdetermined, with relations that disagree as exact equalities (main §4.2). The other %d entries of the dataset are conditional extractions and diagnostics and are not counted. The full table is on the [Observable Reference](Observable-Reference.html) page.

---

## Look-elsewhere

In a preregistered test, every competing Betti pair and every invented vocabulary searches for its own formulas in the same grammar and budget. K₇ reaches 31 of the 33 targets, and a sizeable share of the competitors do as well or better: closeness to the data is not distinctive (main §7.2, S4.2). Code, preregistration and results are in [`publications/validation/v3.6/`](%spublications/validation/v3.6/); the numbers are on the [Statistical Evidence](Statistical-Evidence.html) page.

---

## Sections

%s

---

## Related

- [Paper S1 Foundations](Paper-S1-Foundations.html)
- [Paper S2 Derivations](Paper-S2-Derivations.html)
- [Observable Reference](Observable-Reference.html)
- [Statistical Evidence](Statistical-Evidence.html)
- [Validation Summary](Validation-Summary.html)
- [Citation Guide](Citation-Guide.html)
""" % (TITLE, paper_links(f, vdoi, "main", DOCS[0][1]), f["pp_S1"], f["pp_S2"], GH, f["pp_S3"], GH, f["pp_S4"], GH,
       f["n33"], f["classes"], f["n_other"], GH, sections(f, "main"))


def paper_s1(f, vdoi):
    return """# Paper: S1, Mathematical Foundations

**Supplement S1: Mathematical Foundations. E₈ Exceptional Lie Algebra, G₂ Holonomy Manifolds, and the Topological Status of K₇** (The K₇ Framework, v3.6)

*Brieuc de La Fournière (2026)*

%s

---

## What the supplement contains

The mathematical background of the dictionary: the E₈ data it uses, G₂ holonomy manifolds, the topological status of K₇ and the algebraic reference form.

Three points of status, stated in the supplement itself:

- **The pair (b₂, b₃) = (21, 77) is posited.** It has no known construction: it does not appear among the catalogued compact G₂ manifolds, and the Joyce–Karigiannis route proposed in version 3.5 does not realise it (S1 §8.4; v3.5 erratum, §9).
- **det(g) = 65/32 is an imposed normalization** of the reference form (residue R2), not a result.
- **Joyce's perturbation theorem is not applied to a compact K₇ here**: its smallness constant depends on geometric quantities that are not controlled for this setting (S1 §11).

---

## The twenty structural constants

From main §3.1; the *status* column separates Lie data, posited inputs and combinations built by the framework's own choices.

%s

---

## Sections

%s

---

## Related

- [Paper Main](Paper-Main-Framework.html)
- [Paper S2 Derivations](Paper-S2-Derivations.html)
- [Paper Explicit G2 Metric](Paper-Explicit-G2-Metric.html)
- [Glossary](Glossary.html)
""" % (paper_links(f, vdoi, "S1", DOCS[1][1]), f["constants"], sections(f, "S1"))


def paper_s2(f, vdoi):
    return """# Paper: S2, The 33 Relations

**Supplement S2: The 33 Relations. Arithmetic, Dictionary Choices and Status** (The K₇ Framework, v3.6)

*Brieuc de La Fournière (2026)*

%s

---

## What the supplement establishes

Earlier versions of this supplement were titled "Complete Derivations" and presented each relation as a theorem with a proof. Version 3.6 withdraws that framing. For each of the %d relations the supplement establishes three things, and no more:

1. **The arithmetic.** Given the declared constants, the closed form evaluates to the stated number. Each relation has a Lean statement tying its closed form to its value (`relations_v36_certified`, [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean)).
2. **The dictionary choices.** Which constants the formula uses, which operations beyond integer ratios, and which entries of the residue register (R1 to R12) it depends on.
3. **The status** against the most recent data, generated from the dataset: %s.

What the arithmetic does not establish: that the formula is the right one for the observable, that the structure requires it, or that agreement with measurement is evidence for the framework (main §7). Section S2.7 records the alternative formulas found for the same observables; their number measures the freedom of the vocabulary, not robustness.

---

## Sections

%s

---

## Related

- [Paper Main](Paper-Main-Framework.html)
- [Paper S1 Foundations](Paper-S1-Foundations.html)
- [Observable Reference](Observable-Reference.html)
- [Lean Formalization](Lean-Formalization.html)
""" % (paper_links(f, vdoi, "S2", DOCS[2][1]), f["n33"], classes_line(f), sections(f, "S2"))


# ---------------------------------------------------------------- Changelog-Highlights
def changelog(f, vdoi, date):
    return """# Changelog Highlights

Abridged version history. The full record is in [`CHANGELOG.md`](%sCHANGELOG.md), and the changes of version 3.6, section by section, in the [paper changelog](%spublications/papers/markdown/k7_framework_3_6_CHANGELOG.md). Statements withdrawn by version 3.6 are not repeated below.

---

## v3.6, %s

**The K₇ Dictionary: a declared correspondence, with its residue and a decision rule**

- **New title**: "%s". The series keeps the name "The K₇ Framework".
- **Reframing**: the relations are presented as a correspondence chosen by the author, a privileged candidate, not as a derivation. No geometric map from the invariants to the observables is known, and no rule assigns formulas to observables.
- **Dictionary, residue, decision rule**: twenty structural constants and a grammar; a residue register R1 to R12 of everything set by choice; a rule that rejects a relation with no repair clause.
- **The 33 relations against the most recent data** (PDG 2026, NuFIT 6.1, Planck 2018): %s. A single score over the 33 is no longer reported.
- **Not 33 independent tests**: three sectors are overdetermined, with relations that disagree as exact equalities.
- **The other %d entries** of the dataset are conditional extractions and diagnostics, and are not counted as predictions.
- **Look-elsewhere**: a preregistered test in which every competitor searches for its own formulas. K₇ reaches 31 of the 33 targets and is not distinctive on closeness. Code and results are public in `publications/validation/v3.6/`.
- **Withdrawn**: the coincidence probabilities and uniqueness statements of versions 3.3 to 3.5, the reading of the relations as derived from the geometry, a primary lepton relation, and the Joyce–Karigiannis route to (21, 77).
- **Formal verification**: %s.%s

## v3.5, 2026-07-10

- Renamed "The K₇ Framework" (GIFT remains the name of the founding phase).
- Supplement S4 added; conditional framing throughout.
- **Erratum** (2026-08 to 2026-10, sections 1 to 11): [`ERRATUM_v3.5.md`](%spublications/ERRATUM_v3.5.md). Version 3.6 integrates it.

## v3.4, 2026-04 to 2026-06

- Companion papers A, B, C published on Zenodo (2026-04-29), D on 2026-05-05.
- Computer-assisted Newton–Kantorovich certificate for a torsion-free G₂ structure on a seam (neck) model; it does not construct a compact K₇.
- K3 Newton–Kantorovich certificates (Fermat quartic, CI(2,2,2)), formalized in Lean.
- Lean axiom reduction; several fitted closed forms for metric coefficients dropped as artifacts.

## v3.3, 2026-01 to 2026-03

- The list of 33 dimensionless relations fixed.
- Neutrino mixing formulas revised (θ₂₃ corrected in 3.3.17, θ₁₂ and θ₂₃ in 3.3.24).
- Lean 4 as the sole proof system (Coq archived).
- S1 construction claims made conditional.

## v3.0 to v3.1, 2025-12

- First Lean-certified arithmetic relations.
- First explicit approximate G₂ metric with a Newton–Kantorovich check.

## v2.x, 2025-10 to 2025-11

- Framework reorganization; first Lean verification.

---

*For complete details, see the [full changelog](%sCHANGELOG.md).*
""" % (GH, GH, date or "in preparation", TITLE, classes_line(f), f["n_other"], lean_note(f).replace(
        "relations_v36_certified", "`relations_v36_certified`"),
       "\n- **Zenodo**: %s." % doi_link(vdoi) if vdoi else "", GH, GH)


# ---------------------------------------------------------------- références
def references_readme(f):
    return """# Reference Documents

Reference data and pages of the K₇ framework, version 3.6.

---

## Contents

| File | Description | Source |
|------|-------------|--------|
| [observables.csv](observables.csv) | The dataset: %d entries, of which %d relations (Type I) are compared with measurement and %d are conditional or diagnostic | copy of the paper's dataset |
| [GIFT_ATLAS.json](GIFT_ATLAS.json) | The twenty structural constants and the %d relations with their closed form, measured value, pull and class | generated from the dataset and main §3.1 |
| [OBSERVABLE_REFERENCE.md](OBSERVABLE_REFERENCE.md) | The tables of the main paper and of S3, in one page | generated from the paper sources |
| [STATISTICAL_EVIDENCE.md](STATISTICAL_EVIDENCE.md) | The classification of the %d relations and the look-elsewhere test | generated from the paper sources |
| [Bibliography.md](Bibliography.md) | References and works that cite K₇ | |

Every number on these pages is generated from the paper's sources. Where a page and the paper differ, the paper holds.

---

## Papers

The framework papers are in [`../papers/markdown/`](../papers/markdown/):

- [Main paper](../papers/markdown/k7_framework_3_6_main.md)
- [S1: Mathematical foundations](../papers/markdown/k7_framework_3_6_S1_foundations.md)
- [S2: The 33 relations](../papers/markdown/k7_framework_3_6_S2_derivations.md)
- [S3: Observable dataset](../papers/markdown/k7_framework_3_6_S3_observables.md)
- [S4: Sieve and look-elsewhere diagnostics](../papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md)

The look-elsewhere test (code, preregistration, results) is in [`../validation/v3.6/`](../validation/v3.6/); the generators of the tables and of the generated pages are in [`../validation/v3.6_generators/`](../validation/v3.6_generators/).

---

*The K₇ Framework v3.6 | generated by `k7_v3_6_deposit_pages.py`*
""" % (f["n_total"], f["n33"], f["n_other"], f["n33"], f["n33"])


def atlas(f):
    obs, cls = f["obs"], {i: k for k, ids in f["cls"].items() for i in ids}
    consts = []
    for row in f["constants"].splitlines()[2:]:
        c = [x.strip().replace("\\|", "|") for x in re.split(r"(?<!\\)\|", row)[1:-1]]
        consts.append({"n": int(c[0]), "symbol": c[1], "value": int(c[2]), "origin": c[3], "status": c[4]})
    assert len(consts) == 20, "main §3.1 : %d constantes lues" % len(consts)
    rels = []
    for i in sorted(o for o in obs if obs[o]["type"] == "I"):
        o = obs[i]
        err = o.get("exp_error")
        rels.append({
            "id": i, "symbol": o["symbol"], "name": o["name"], "sector": o["sector"],
            "formula": o["gift_formula"], "fraction": o.get("gift_fraction"), "value": o["gift_value"],
            "measured": o["exp_value"], "uncertainty_1sigma": err, "source": o["exp_source"],
            "pull": round((o["gift_value"] - o["exp_value"]) / err, 2) if err else None,
            "class": cls[i], "lean_theorem": o.get("lean_theorem"),
        })
    assert len(rels) == f["n33"]
    doc = {
        "_metadata": {
            "title": "K₇ Framework: structural constants and the 33 relations",
            "version": "3.6",
            "generator": "k7_v3_6_deposit_pages.py, from the paper's dataset (observables.csv) and main §3.1",
            "description": "A declared correspondence, not a derivation. The class of each relation is the one "
                           "of main §4.1. The 33 relations are not independent tests (main §4.2).",
            "class_definitions": {
                "within_2sigma": "|pull| ≤ 2", "tension": "2 < |pull| ≤ 3",
                "excluded_3sigma": "|pull| > 3 as an exact equality; kept as a proximity",
                "in_range": "inside a range given without uncertainty; no pull",
                "non_gaussian": "non-Gaussian profile; the pull is indicative only"},
            "class_counts": {k: len(v) for k, v in f["cls"].items()},
            "entries_not_listed": "%d conditional or diagnostic entries (Types II to IV), in observables.csv; "
                                  "not counted as predictions" % f["n_other"],
        },
        "structural_constants": consts,
        "relations": rels,
    }
    return json.dumps(doc, ensure_ascii=False, indent=2) + "\n"


# ---------------------------------------------------------------- main
# ---------------------------------------------------------------- README racine (régions marquées)
COMP_ROWS = [  # (lettre, libellé de la table Archive)
    ("E", "Paper E, rank-1 branched adiabatic"), ("A", "Paper A, certified G₂"), ("B", "Paper B, spectral"),
    ("C", "Paper C, K3 NK"), ("D", "Paper D, Donaldson analytic"),
]


def readme_regions(f, vdoi, date):
    """Les six régions `<!-- v36:nom -->` du README racine, dans l'état déposé ou non."""
    dep = bool(vdoi)
    erratum = "[erratum](publications/ERRATUM_v3.5.md)"
    tex = "LaTeX sources: [`publications/papers/tex/`](publications/papers/tex/)."
    rows = ["| Archive | |", "|---------|---|"]
    if dep:
        rows.append("| Zenodo (framework v3.6, current) | %s |" % doi_link(vdoi))
    else:
        rows.append("| Zenodo (framework v3.5, current) | %s |" % doi_link(f["doi35"]))
    rows.append("| Zenodo (framework concept DOI, always latest) | %s |" % doi_link(f["concept"]))
    if dep:
        rows.append("| Zenodo (framework v3.5 archive) | %s |" % doi_link(f["doi35"]))
    rows += ["| Zenodo (framework v3.4 archive) | %s |" % doi_link(f["doi34"]),
             "| Zenodo (framework v3.3 archive) | %s |" % doi_link(f["doi33"])]
    rows += ["| Zenodo (%s) | %s |" % (label, doi_link(f["comp"][x])) for x, label in COMP_ROWS]
    rows += ["| ResearchGate | [Author page](https://www.researchgate.net/profile/Brieuc-De-La-Fourniere) |",
             "| PhilPeople | [Author page](https://philpeople.org/profiles/brieuc-de-la-fourniere) |", ""]
    cite = ["```bibtex", "@software{k7_framework,", "  title   = {The K₇ Framework (formerly GIFT)},",
            "  author  = {de La Fournière, Brieuc},", "  year    = {2026},",
            "  url     = {https://github.com/Arithmon/K7},", "  doi     = {%s}," % f["concept"],
            "  version = {%s}" % ("3.6" if dep else "3.5"), "}", "```", "",
            ("The concept DOI always resolves to the latest version; version 3.6 itself is %s." % doi_link(vdoi)
             if dep else "Cite the published version (3.5) until 3.6 is deposited.")]
    return {
        "banner": (
            "> **Version 3.6** (Zenodo %s, %s). This README describes version 3.6 of the framework paper. "
            "It replaces version 3.5 (Zenodo %s) and its %s." % (doi_link(vdoi), date, doi_link(f["doi35"]), erratum)
            if dep else
            "> **Version 3.6.** This README describes version 3.6 of the framework paper, whose files are in this "
            "repository; its Zenodo deposit is pending. Until the deposit, the published version is 3.5 (Zenodo %s), "
            "read together with its %s." % (doi_link(f["doi35"]), erratum)),
        "head36": ("### Framework v3.6 (published: PDF, TeX and markdown, Zenodo %s)" % doi_link(vdoi) if dep
                   else "### Framework v3.6 (Zenodo deposit pending)"),
        "tex36": (tex if dep else tex + " These are the files prepared for the Zenodo deposit of version 3.6; "
                  "until the deposit, the published version is 3.5."),
        "head35": ("### Framework v3.5 (%s: PDF, TeX and markdown, Zenodo %s)"
                   % ("previous version" if dep else "published", doi_link(f["doi35"]))),
        "archive": "\n".join(rows),
        "cite": "\n".join(cite),
    }


def readme(f, vdoi, date, k7):
    """README racine : seules les régions marquées sont réécrites ; le reste du fichier est laissé tel quel."""
    text = open(os.path.join(k7, "README.md"), encoding="utf-8").read()
    for name, body in readme_regions(f, vdoi, date).items():
        pat = re.compile(r"(<!-- v36:%s -->\n).*?(\n<!-- /v36:%s -->)" % (name, name), re.S)
        assert len(pat.findall(text)) == 1, "README : région v36:%s absente ou en double" % name
        text = pat.sub(lambda m: m.group(1) + body + m.group(2), text)
    return text


# ---------------------------------------------------------------- publications/papers/README.md
COMP_PDF = {"A": ("Certified G₂ Structure", "g2_certified_neck.pdf"), "B": ("Spectral Geometry", "g2_spectral.pdf"),
            "C": ("K3 Newton-Kantorovich", "K3_NK_Certificate.pdf"),
            "D": ("Donaldson Analytic Note", "donaldson_analytic.pdf"),
            "E": ("Rank-1 Branched Adiabatic", "rank_one_branched_adiabatic.pdf")}
COMP_DESC = {
    "A": "Newton–Kantorovich certificate for a torsion-free G₂ structure near an explicit metric on a neck model; "
         "a local result, which does not construct a compact K₇",
    "B": "Numerical Laplacian spectrum and harmonic forms of the explicit metric of paper A",
    "C": "NK diagnostics on Donaldson K3 (CI(2,2,2))",
    "D": "Closed-form G₂ ansatz on K3-coassociative neck, 5-layer Wirtinger cert",
    "E": "Conditional analytic framework for rank-one branched adiabatic limits, computed at a datum D₀ that is "
         "not realisable as posed (erratum to v3.5); its global hypotheses are open",
}
S_SHORT = {"main": "Main paper", "S1": "S1: Mathematical foundations", "S2": "S2: The 33 relations",
           "S3": "S3: Observable dataset", "S4": "S4: Look-elsewhere test"}
OLD35 = [("Main Paper (47 pp.)", "main"), ("S1: Foundations", "S1_foundations"), ("S2: Derivations", "S2_derivations"),
         ("S3: Observables", "S3_observables"), ("S4: Sieve Diagnostics", "S4_sieve_diagnostics")]


def papers_readme(f, vdoi, date, k7):
    dep = bool(vdoi)
    base = os.path.join(k7, "publications", "papers")
    names = [n for _k, n, _t, _s in DOCS]
    tree_paths = (["markdown/%s.md" % n for n in names] + ["pdf/%s.pdf" % n for n in names]
                  + ["markdown/k7_framework_3_6_CHANGELOG.md", "markdown/g2_certified_neck.md",
                     "markdown/g2_spectral.md", "tex/gift_3.6_bib.tex", "tex/gift_preamble.tex", "figures",
                     "notebooks", "legacy/v3.3", "legacy/v3.4", "pdf/k7_one_page.pdf", "tex/k7_one_page.tex",
                     "../outreach", "../references/observables.csv", "../references/OBSERVABLE_REFERENCE.md",
                     "../references/STATISTICAL_EVIDENCE.md", "../references/Bibliography.md",
                     "../references/GIFT_ATLAS.json", "../validation/v3.6", "../validation/v3.6_generators",
                     "../validation/legacy/v3.3", "../ERRATUM_v3.5.md"]
                  + ["pdf/" + pdf for _t, pdf in COMP_PDF.values()]
                  + ["markdown/k7_framework_3_5_%s.md" % n for _l, n in OLD35]
                  + ["pdf/k7_framework_3_5_%s.pdf" % n for _l, n in OLD35])
    for p in tree_paths:
        assert os.path.exists(os.path.join(base, p)), "papers/README nomme un chemin absent de K7 : " + p
    status = ("Version 3.6 is the current version (Zenodo %s, %s)." % (doi_link(vdoi), date) if dep else
              "Version 3.6 is in this repository and its Zenodo deposit is pending; until the deposit, the "
              "published version is 3.5 (Zenodo %s)." % doi_link(f["doi35"]))
    out = ["# The K₇ Framework: Publications", "",
           "[![Lean 4 Verified](https://img.shields.io/badge/Lean_4-Verified-blue)](https://github.com/Arithmon/K7-Lean)",
           "",
           "The K₇ Framework (formerly GIFT): a declared correspondence between the invariants of a posited "
           "G₂-holonomy geometry, together with E₈×E₈, and dimensionless Standard-Model and cosmological parameters.",
           "", status, "", "---", "", "## Documentation Structure", "", "```", "publications/",
           "├── papers/",
           "│   ├── markdown/                    # Canonical sources",
           "│   │   ├── k7_framework_3_6_main.md                 # Main paper (v3.6)",
           "│   │   ├── k7_framework_3_6_S1_foundations.md       # E₈, G₂, K₇ foundations",
           "│   │   ├── k7_framework_3_6_S2_derivations.md       # The 33 relations",
           "│   │   ├── k7_framework_3_6_S3_observables.md       # Observable dataset",
           "│   │   ├── k7_framework_3_6_S4_sieve_diagnostics.md # Look-elsewhere test",
           "│   │   ├── k7_framework_3_6_CHANGELOG.md            # Changes from v3.5",
           "│   │   ├── k7_framework_3_5_*.md                    # v3.5, unchanged",
           "│   │   ├── g2_certified_neck.md                     # Paper A",
           "│   │   └── g2_spectral.md                           # Paper B",
           "│   ├── pdf/                         # Compiled PDFs",
           "│   │   ├── k7_framework_3_6_*.pdf                   # Framework v3.6 (main, S1 to S4)",
           "│   │   ├── k7_framework_3_5_*.pdf                   # Framework v3.5 (main, S1 to S4)",
           "│   │   ├── g2_certified_neck.pdf                    # Paper A",
           "│   │   ├── g2_spectral.pdf                          # Paper B",
           "│   │   ├── K3_NK_Certificate.pdf                    # Paper C",
           "│   │   ├── donaldson_analytic.pdf                   # Paper D",
           "│   │   ├── rank_one_branched_adiabatic.pdf          # Paper E",
           "│   │   └── k7_one_page.pdf                          # One-page summary",
           "│   ├── tex/                         # LaTeX sources (v3.6, v3.5, companions)",
           "│   ├── figures/                     # Publication figures",
           "│   ├── notebooks/                   # Companion Jupyter notebooks (papers A and B)",
           "│   ├── legacy/v3.3/                 # v3.3 framework PDFs + markdown + tex (archived)",
           "│   └── legacy/v3.4/                 # v3.4 framework PDFs + markdown + tex (archived)",
           "│", "├── outreach/                        # Essay sources and the one-page summary",
           "│", "├── references/",
           "│   ├── observables.csv              # Machine-readable data",
           "│   ├── GIFT_ATLAS.json",
           "│   ├── OBSERVABLE_REFERENCE.md",
           "│   ├── STATISTICAL_EVIDENCE.md",
           "│   └── Bibliography.md",
           "│", "├── validation/",
           "│   ├── v3.6/                        # Look-elsewhere test of v3.6 (code, data, results)",
           "│   ├── v3.6_generators/             # Generators of the tables and of the generated pages",
           "│   └── legacy/v3.3/                 # v3.3 validation pipeline (archived)",
           "│", "└── ERRATUM_v3.5.md                  # Erratum to version 3.5", "```", "", "---", "",
           ("## Framework v3.6 (published Zenodo %s)" % doi_link(vdoi) if dep
            else "## Framework v3.6 (Zenodo deposit pending)"), "",
           "| Document | PDF | Markdown |", "|----------|-----|----------|"]
    for key, name, _t, _s in DOCS:
        out.append("| %s | [%s.pdf](pdf/%s.pdf) (%d pp.) | [%s.md](markdown/%s.md) |"
                   % (S_SHORT[key], name, name, f["pp_" + key], name, name))
    out += ["| Changes from v3.5 | | [k7_framework_3_6_CHANGELOG.md](markdown/k7_framework_3_6_CHANGELOG.md) |", "",
            "LaTeX sources: [`tex/`](tex/) (`k7_framework_3_6_*.tex`, `gift_3.6_bib.tex`)."
            + ("" if dep else " These are the files prepared for the Zenodo deposit; until the deposit, the "
               "published version is 3.5.")
            + " Concept DOI (always the latest version): %s." % doi_link(f["concept"]), "",
            "---", "",
            "## Framework v3.5 (%s, Zenodo %s)" % ("previous version" if dep else "published", doi_link(f["doi35"])),
            "",
            "The v3.5 files are unchanged, and are read together with the [erratum](../ERRATUM_v3.5.md). "
            "Version 3.6 withdraws a number of their statements "
            "([changes from v3.5](markdown/k7_framework_3_6_CHANGELOG.md)).", "",
            "| Document | PDF | Markdown |", "|----------|-----|----------|"]
    for label, n in OLD35:
        out.append("| %s | [k7_framework_3_5_%s.pdf](pdf/k7_framework_3_5_%s.pdf) | "
                   "[k7_framework_3_5_%s.md](markdown/k7_framework_3_5_%s.md) |" % (label, n, n, n, n))
    out += ["", "## Companion Papers (Zenodo)", "", "Cited by their concept DOI, as in the paper's reference list.",
            "", "| Paper | Description | DOI |", "|-------|-------------|-----|"]
    for x in "ABCDE":
        t, pdf = COMP_PDF[x]
        out.append("| [%s: %s](pdf/%s) | %s | %s |" % (x, t, pdf, COMP_DESC[x], doi_link(f["comp"][x])))
    out += ["", "---", "", "## Headline results and statistical validation of version 3.5 (withdrawn in 3.6)", "",
            "The tables that stood here in version 3.5 gave the relations the status **PROVEN** and reported "
            "\"0 better alternatives\" among 3,000,000+ configurations and a set-level probability of about 10⁻⁶. "
            "Version 3.6 withdraws them: the relations are assignments whose arithmetic is verified, not "
            "derivations; the alternatives were scored with the framework's own formulas; and in a preregistered "
            "test where each competitor searches for its own formulas, a quarter of the alternative Betti pairs and "
            "half of the invented vocabularies reach as many targets as K₇ (S4). See the "
            "[v3.6 changelog](markdown/k7_framework_3_6_CHANGELOG.md).", "", "---", "",
            "## Formal Verification", "",
            "%d Lean 4 files, 14 axioms at K7-Lean main (4 imported from the literature, 10 interval certificates), "
            "0 sorry; the arithmetic of the 33 relations is collected in `relations_v36_certified`." % f["n_lean"], "",
            "See [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) for the proofs.", "", "---", "",
            "## Legacy", "",
            "- `legacy/v3.3/`: v3.3 framework PDFs, markdown and tex (archived 2026-05-02, Zenodo %s)"
            % doi_link(f["doi33"]),
            "- `legacy/v3.4/`: v3.4 framework PDFs, markdown and tex (archived 2026-07-14, Zenodo %s)"
            % doi_link(f["doi34"]),
            "- `../validation/legacy/v3.3/`: v3.3 validation pipeline + Pareto formula selection", "", "---", "",
            "**Version**: 3.6%s" % (" (%s)" % date if dep else " (not yet deposited; published version 3.5, 2026-07-10)"),
            "**Repository**: https://github.com/Arithmon/K7", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k7", default=os.environ.get("K7_DIR", K7_DEFAULT))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--version-doi", default=None, help="DOI de version Zenodo de la 3.6, une fois déposée")
    ap.add_argument("--date", default=None, help="date du dépôt, AAAA-MM-JJ")
    a = ap.parse_args()
    if a.version_doi:
        assert re.fullmatch(r"10\.5281/zenodo\.\d+", a.version_doi), "DOI de version mal formé"
        assert a.date and re.fullmatch(r"\d{4}-\d\d-\d\d", a.date), "--date AAAA-MM-JJ requis avec --version-doi"
    f = facts(a.k7)
    assert not a.version_doi or a.version_doi not in (f["concept"], f["doi35"], f["doi34"], f["doi33"]), \
        "ce DOI est déjà celui du concept ou d'une version antérieure"
    v, d = a.version_doi, a.date
    pages = {
        "CITATION.md": citation(f, v, d, wiki=False),
        "docs/wiki/Citation-Guide.md": front("Citation Guide") + citation(f, v, d, wiki=True),
        "CITATION.cff": cff(f, v),
        "STRUCTURE.md": structure(f, v, d, a.k7),
        "docs/wiki/Repository-Structure.md": front("Repository Structure") + structure(f, v, d, a.k7),
        "docs/wiki/Paper-Main-Framework.md": front("Paper Main Framework") + paper_main(f, v),
        "docs/wiki/Paper-S1-Foundations.md": front("Paper S1 Foundations") + paper_s1(f, v),
        "docs/wiki/Paper-S2-Derivations.md": front("Paper S2 Derivations") + paper_s2(f, v),
        "docs/wiki/Changelog-Highlights.md": front("Changelog Highlights") + changelog(f, v, d),
        "publications/references/README.md": references_readme(f),
        "README.md": readme(f, v, d, a.k7),
        "publications/papers/README.md": papers_readme(f, v, d, a.k7),
        "publications/references/GIFT_ATLAS.json": atlas(f),
    }
    binaries = {}
    for key, name, _t, _s in DOCS:
        binaries["publications/papers/pdf/%s.pdf" % name] = os.path.join(LATEX, "k7_framework_3_6_%s.pdf" % key)
        binaries["publications/papers/tex/k7_framework_3_6_%s.tex" % key] = os.path.join(
            LATEX, "k7_framework_3_6_%s.tex" % key)
    binaries["publications/papers/tex/gift_3.6_bib.tex"] = os.path.join(LATEX, "gift_3.6_bib.tex")
    # le préambule que les .tex 3.6 incluent (celui de K7 était resté à la v3.4 : audit du 2026-11-11)
    binaries["publications/papers/tex/gift_preamble.tex"] = os.path.join(LATEX, "gift_preamble.tex")
    # les sources markdown et le changelog du papier : copies conformes
    for key, name, _t, src in DOCS:
        binaries["publications/papers/markdown/%s.md" % name] = os.path.join(os.path.dirname(LATEX), src)
    binaries["publications/papers/markdown/k7_framework_3_6_CHANGELOG.md"] = os.path.join(
        os.path.dirname(LATEX), "CHANGELOG.md")
    bad = 0
    for rel, text in pages.items():
        path = os.path.join(a.k7, rel)
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        if old == text:
            print("identique  %s" % rel)
        elif a.check:
            print("DIFFÈRE    %s" % rel); bad += 1
        else:
            open(path, "w", encoding="utf-8").write(text)
            print("écrit      %s (%d lignes)" % (rel, text.count("\n")))
    for rel, src in binaries.items():
        path = os.path.join(a.k7, rel)
        new = open(src, "rb").read()
        old = open(path, "rb").read() if os.path.exists(path) else b""
        if old == new:
            print("identique  %s" % rel)
        elif a.check:
            print("DIFFÈRE    %s" % rel); bad += 1
        else:
            open(path, "wb").write(new)
            print("copié      %s (%d octets)" % (rel, len(new)))
    print("état : %s" % ("3.6 déposée, DOI de version %s" % v if v else "3.6 non déposée (DOI concept seul)"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
