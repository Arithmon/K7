#!/usr/bin/env python3
"""k7_v3_6_publish_generators.py -- dépôt public des générateurs de la v3.6 dans K7.

Décision de Brieuc (2026-11-26) : les scripts que S3.8 disait « available on request » passent en
public, dans un dossier dédié, `publications/validation/v3.6_generators/`. Copies octet pour octet,
chemins `canonical/...` conservés ; le README porte la taille et le sha256 de chaque fichier, CALCULÉS
ici (dériver, ne pas nommer : si un script change, --check rougit tant que le dépôt n'est pas refait).

Usage : k7_v3_6_publish_generators.py [--k7 DIR] [--check]
"""
import argparse
import hashlib
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
K7_DEFAULT = os.path.join(os.path.dirname(ROOT), "K7")
DEST = "publications/validation/v3.6_generators"

FILES = [  # (chemin sous le dépôt de travail, rôle)
    ("canonical/scripts/k7_v3_6_exp_refresh.py", "refreshes the reference values of the dataset to the most recent measurements and logs every change"),
    ("canonical/results/k7_v3_6_exp_refresh.json", "its log"),
    ("canonical/scripts/k7_v3_6_planck_ratios.py", "computes the density ratios and their uncertainties on the public Planck 2018 chains (the archive is not included; its URL and sha256 are in the result)"),
    ("canonical/results/k7_v3_6_planck_ratios.json", "its result"),
    ("canonical/scripts/k7_v3_6_dataset_labels.py", "label pass of the dataset (titles, Lean pointers, notes) and its derived exports"),
    ("canonical/results/k7_v3_6_lean_map.json", "the map from each relation to its Lean declaration"),
    ("canonical/scripts/k7_v3_6_table_sec4.py", "generates the table of main §4.1 and the five classes from the dataset"),
    ("canonical/scripts/k7_v3_6_s2_status.py", "status column of the tables of S2"),
    ("canonical/scripts/k7_v3_6_s3_tables.py", "tables of S3"),
    ("canonical/scripts/k7_v3_6_s4_tables.py", "tables of S4.2 and the figures of main §7.2, from the look-elsewhere results"),
    ("canonical/papers/framework/latex/gen_bib_3_6.py", "bibliography of the LaTeX sources, from the reference list of the main paper"),
    ("canonical/papers/framework/latex/build_3.6.sh", "Markdown to LaTeX to PDF build of the five documents"),
    ("canonical/scripts/k7_v3_6_surface_pages.py", "generated pages of this repository: statistical evidence, validation summary, observable reference"),
    ("canonical/scripts/k7_v3_6_surface_prose.py", "FAQ, executive summary and physicists' overview"),
    ("canonical/scripts/k7_v3_6_reader_pages.py", "Lean formalization and geometers' pages"),
    ("canonical/scripts/k7_v3_6_landing_pages.py", "results, papers and falsification sections of the landing pages"),
    ("canonical/scripts/k7_v3_6_deposit_pages.py", "citation files, structure pages, paper pages, changelog highlights, atlas; copies the papers"),
    ("canonical/scripts/k7_v3_6_surfaces_lint.py", "checks the public pages for statements that version 3.6 withdraws"),
    ("canonical/scripts/k7_v3_6_for_everyone_patch.py", "one-off targeted edits of the plain-language guide (2026-11-10)"),
    ("canonical/scripts/k7_v3_6_publish_generators.py", "this deposit"),
]


def readme(rows):
    table = "\n".join("| `%s` | %s | `%s` | %s |" % (p, f"{n:,}".replace(",", " "), h, role) for p, n, h, role in rows)
    return """# Generators of version 3.6

This directory holds the scripts that produce the tables of the K₇ framework paper, version 3.6, its LaTeX sources and the generated pages of this repository, with the result files they write. Supplement S3 (§S3.8) refers to it. The look-elsewhere test has its own directory, [`../v3.6/`](../v3.6/).

## Layout

The files are verbatim copies from the author's working repository and keep its relative paths (`canonical/...`). Comments and messages are in French.

| File | Bytes | sha256 | Role |
|---|---:|---|---|
%s

## What runs from here, and what does not

These scripts read and write the author's working tree: the dataset `canonical/data/observables.json`, the Markdown sources of the papers under `canonical/papers/framework/`, and a clone of this repository and of [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) beside it. They are published so that every generated number and every generated page can be traced to the code that wrote it; they are not packaged as a standalone tool.

To rerun one of them, recreate the layout: the dataset is in [`../v3.6/canonical/data/observables.json`](../v3.6/canonical/data/observables.json) (the copy read by the look-elsewhere run), and the Markdown sources of the papers are in [`../../papers/markdown/`](../../papers/markdown/) under their public names (`k7_framework_3_6_main.md` is `physics_main.md`; `S1_foundations`, `S2_derivations`, `S3_observables` and `S4_sieve_diagnostics` are `supplement_foundations.md`, `supplement_derivations.md`, `supplement_observables.md` and `supplement_sieve_diagnostics.md`). The table generators have a `--check` mode that writes nothing and reports whether the tables of the papers are those the dataset produces.

`k7_v3_6_planck_ratios.py` takes as argument a directory holding the public Planck 2018 chain archive, whose URL and sha256 are recorded in its result. `k7_v3_6_exp_refresh.py` reads an earlier state of the dataset from the history of the working repository, which is not public: its log is given so that each changed value can be checked against its source.
""" % table


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k7", default=K7_DEFAULT)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    rows, out = [], {}
    for rel, role in FILES:
        b = open(os.path.join(ROOT, rel), "rb").read()
        rows.append((rel, len(b), hashlib.sha256(b).hexdigest(), role))
        out[os.path.join(DEST, rel)] = b
    txt = readme(rows)
    assert "—" not in txt
    out[os.path.join(DEST, "README.md")] = txt.encode("utf-8")
    bad = 0
    for rel, b in out.items():
        p = os.path.join(a.k7, rel)
        cur = open(p, "rb").read() if os.path.exists(p) else None
        if cur == b:
            continue
        if a.check:
            print("DIFFÈRE   ", rel); bad += 1
        else:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "wb").write(b); print("écrit     ", rel)
    extra = []
    base = os.path.join(a.k7, DEST)
    for r, ds, fs in os.walk(base):
        for x in fs:
            rel = os.path.relpath(os.path.join(r, x), a.k7)
            if rel not in out:
                extra.append(rel)
    for rel in extra:
        print("EN TROP   ", rel); bad += 1
    print("dépôt des générateurs :", "à jour" if not bad else "%d écart(s)" % bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
