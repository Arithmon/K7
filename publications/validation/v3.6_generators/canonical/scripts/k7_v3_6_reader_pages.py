#!/usr/bin/env python3
"""k7_v3_6_reader_pages.py -- pages « pour géomètres » et « formalisation Lean » de K7 au cadrage 3.6.

Motif (revues indépendantes du 2026-11-26, note canonical/notes/k7_v3_6_pre_merge_audit_2026_11_26.md) :
ces pages dataient des versions 3.3 à 3.5 (table TCS 11 + 10 -> (21, 77), « well below Joyce's threshold »,
« 290+ relations », « zero domain-specific axioms », `all_75_relations_certified`) et contredisaient S1 §8
et main §8. Elles sont remplacées par des pages courtes écrites depuis le papier.

Dériver, ne pas nommer : le nombre de fichiers Lean, les noms des axiomes et le commit sont LUS dans le
clone K7-Lean et dans S1 ; les phrases reprises du papier sont contrôlées par assertion contre
physics_main.md (si le papier change, ce script refuse d'écrire).

Usage : k7_v3_6_reader_pages.py [--k7 DIR] [--check]
"""
import argparse
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PAPERS = os.path.join(ROOT, "canonical", "papers", "framework")
K7_DEFAULT = os.path.join(os.path.dirname(ROOT), "K7")
MD = "https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_%s.md"


def read(name):
    return open(os.path.join(PAPERS, name), encoding="utf-8").read()


def facts(k7):
    lean = os.path.join(os.path.dirname(k7), "K7-Lean")
    files, axioms = 0, []
    for r, ds, fs in os.walk(lean):
        ds[:] = [d for d in ds if d not in (".lake", ".git", "build")]
        for x in fs:
            if x.endswith(".lean"):
                files += 1
                for ln in open(os.path.join(r, x), encoding="utf-8"):
                    m = re.match(r"axiom\s+([A-Za-z0-9_.']+)", ln)
                    if m:
                        axioms.append((m.group(1), os.path.relpath(os.path.join(r, x), lean)))
    assert files > 100, "clone K7-Lean introuvable à côté de K7"
    main, s1 = read("physics_main.md"), read("supplement_foundations.md")
    lit = ["cheeger_inequality", "literature_package", "spectral_upper_bound", "neck_dominates"]
    names = [a for a, _ in axioms]
    assert len(axioms) == 14 and all(a in names for a in lit), names
    for claim in ("It rests on fourteen axioms", "every ordinary twisted connected sum is excluded by parity",
                  "does not realise (21, 77)", "h = 8.95 × 10⁻⁹", "δg/g ≤ 4.86 × 10⁻⁶",
                  "is not realisable as posed", "depends only on the standard axioms",
                  "exact equality for 27", "No such construction is currently known"):
        assert claim in main, "le main a changé : " + claim
    commit = re.search(r"commit `([0-9a-f]{7})`", s1).group(1)
    return dict(files=files, axioms=axioms, lit=lit, commit=commit)


def lean_page(f):
    cert = [(a, p) for a, p in f["axioms"] if a not in f["lit"]]
    rows = "\n".join("| `%s` | `%s` | literature import |" % (a, p) for a, p in f["axioms"] if a in f["lit"])
    rows += "\n" + "\n".join("| `%s` | `%s` | interval certificate |" % (a, p) for a, p in cert)
    return """# Lean Formalization

The arithmetic of the K₇ framework is formalized in Lean 4 with Mathlib, in the repository
[Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean). This page says what the formalization
establishes and what it does not. It follows §8 of the [main paper](%s) and section S3.7 of
[supplement S3](%s), version 3.6.

## What is formalized

| Item | Value |
|---|---|
| Lean 4 files | %d |
| Axioms beyond the Mathlib foundations | 14 (4 literature imports, 10 interval certificates) |
| `sorry` | none |
| The 33 relations | collected in `relations_v36_certified` (commit `%s`), which depends only on the standard axioms `propext`, `Classical.choice`, `Quot.sound` |

The formalization certifies algebraic identities among the declared integers (for example
b₂ · 13 = 3 · (b₃ + dim G₂) for sin²θ_W = 3/13), the G₂ three-form and dim 𝔤₂ = 14, the E₈ root
system, and the arithmetic of several numerical certificates.

## The form of the 33 statements

Each relation has a statement that ties its closed form, written in the structural constants, to its
value. The forms differ, and S3.7 gives the declaration and the line for each:

- an exact equality for 27 relations, between rationals for 25 of them and between natural numbers
  for m_τ/m_e and m_s/m_d;
- a closed form in ℝ, with no numerical bound, for α_s, λ_H, Ω_DE and n_s;
- the base 27 and the bounds 206 < 27^φ < 209 for m_μ/m_e, an interval wider than the deviation it is
  compared with;
- the integer 197 for δ_CP, whose reading in degrees is an assignment of the dictionary.

## The fourteen axioms

`relations_v36_certified` uses none of them. They are used elsewhere in the library.

| Axiom | File | Kind |
|---|---|---|
%s

The four literature imports state results taken from published work; the ten interval certificates
import numerical enclosures computed outside Lean.

## What the formalization does not establish

- **Not the physics.** A machine-checked formula is a formula whose arithmetic is right. Which formula
  is assigned to which observable is a choice of the author, recorded in the paper's dictionary.
- **Not the consistency of the relations taken together.** Formulas that are each computed correctly
  disagree with one another, as exact equalities, in the three overdetermined sectors (main §4.2).
- **Not the existence of K₇.** No compact G₂ manifold with Betti numbers (21, 77) is known (main §9).

## Checking it yourself

```bash
git clone https://github.com/Arithmon/K7-Lean
cd K7-Lean
lake build
```

The statement to inspect is `GIFT.Certificate.RelationsV36.relations_v36_certified`;
`#print axioms` on it lists the axioms it depends on.

Counts and statements of earlier versions of this page (numbers of relations, "zero domain-specific
axioms", earlier certificate names) described earlier states of the library and are withdrawn.
""" % (MD % "main", MD % "S3_observables", f["files"], f["commit"], rows)


def geometers_page():
    return """# For Geometers

What is known, and what is not, about the geometry the K₇ framework posits. This page follows §2.3
and §9 of the [main paper](%s) and §8 of [supplement S1](%s), version 3.6. It replaces an earlier
page that described a twisted-connected-sum construction of K₇; that construction is withdrawn.

## What the framework posits

A compact, simply connected seven-manifold K₇ with holonomy G₂ and Betti numbers (b₂, b₃) = (21, 77).
The 33 relations of the paper use only these integers and Lie-theoretic data, never a metric.

**No compact G₂ manifold with these Betti numbers is known.** Whether one exists is open.

## What is excluded

- **Catalogued examples.** The pair (21, 77) does not appear among Joyce's orbifold constructions or
  among the twisted connected sums of Corti, Haskins, Nordström and Pacini.
- **Ordinary twisted connected sums, all of them.** For every ordinary twisted connected sum
  b₂ + b₃ is odd (Nordström, *Extra-twisted connected sum G₂-manifolds*, Introduction, property (i));
  here b₂ + b₃ = 98. Within this family only the extra-twisted connected sums, which carry no
  parity constraint, remain open.
- **The building-block decomposition 11 + 10.** The table that stood on this page (two blocks with
  b₂ = 11 and b₂ = 10 glued into (21, 77)) is withdrawn: such sublattices of the K3 lattice do not
  support a twisted-connected-sum realisation (S1 §8.3).
- **A Joyce–Karigiannis ℤ₂³ orbifold route.** It does not realise (21, 77): the group action forces
  b₂ ≥ 5 and b₃ ≤ 16 on the quotient for every compatible torus action (S1 §8.4).

## What is established, locally

- **A certified local metric** (companion paper A, [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069)).
  An explicit approximate G₂ metric on a gluing region, with 169 Chebyshev–Cholesky parameters, carries
  a Newton–Kantorovich certificate (h = 8.95 × 10⁻⁹) for a nearby torsion-free metric within a ball
  δg/g ≤ 4.86 × 10⁻⁶. The certificate is local: it does not construct a compact K₇, and the
  smallness constant of Joyce's perturbation theorem depends on geometric bounds that are not
  established here (S1).
- **Its numerical spectrum** (companion paper B, [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367)).
  It gives no independent evidence for (21, 77): the multiplicities it reports are built from
  decompositions that S1 withdraws.
- **A closed-form neck ansatz** (companion paper D, [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065)):
  a positive G₂ three-form on a neck region with K3 coassociative fibres, with its own certificate.
- **A conditional analytic scheme** (companion paper E, [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956))
  for a fibration K₇ → S³ with 77 branch components. It is computed at a datum that is not realisable
  as posed, so no existence argument for the compact K₇ currently holds.
- **The K3 fibre.** No certified bound on a Ricci-flat metric of the K3 fibre is available. An explicit
  K3 surface has a publicly certified holomorphic atlas, with no metric claim
  ([10.5281/zenodo.22047469](https://doi.org/10.5281/zenodo.22047469)).

## What an existence proof would need

Main §9.1 lists it: a realisable datum, and then the global analytic steps that are open problems.
Until then the framework's geometric input is a posited topology, recorded as item R1 of its residue
register.

## Code

The project's Python package is in [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean)
(`contrib/python`); the numerical artefacts of the certificates are in the Zenodo deposits of the
companion papers. Statements made by earlier versions of this page about Joyce's threshold,
about Betti numbers read from spectra, and about typical bounds on b₂ are withdrawn.
""" % (MD % "main", MD % "S1_foundations")


def front(title):
    return '---\ntitle: "%s"\nlayout: default\n---\n\n' % title


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k7", default=K7_DEFAULT)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    f = facts(a.k7)
    lean, geo = lean_page(f), geometers_page()
    assert "—" not in lean + geo
    out = {"docs/LEAN_FOR_PHYSICS.md": lean,
           "docs/wiki/Lean-Formalization.md": front("Lean Formalization") + lean,
           "docs/wiki/For-Formalization-Experts.md": front("For Formalization Experts") + lean,
           "docs/GIFTPY_FOR_GEOMETERS.md": geo,
           "docs/wiki/For-Geometers.md": front("For Geometers") + geo}
    bad = 0
    for rel, txt in out.items():
        p = os.path.join(a.k7, rel)
        cur = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if cur == txt:
            print("identique ", rel)
        elif a.check:
            print("DIFFÈRE   ", rel); bad += 1
        else:
            open(p, "w", encoding="utf-8").write(txt); print("écrit     ", rel)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
