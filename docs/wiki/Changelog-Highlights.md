---
title: "Changelog Highlights"
layout: default
---

# Changelog Highlights

Abridged version history. The full record is in [`CHANGELOG.md`](https://github.com/Arithmon/K7/blob/main/CHANGELOG.md), and the changes of version 3.6, section by section, in the [paper changelog](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_CHANGELOG.md). Statements withdrawn by version 3.6 are not repeated below.

---

## v3.6, in preparation

**The K₇ Dictionary: a declared correspondence, with its residue and a decision rule**

- **New title**: "The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology". The series keeps the name "The K₇ Framework".
- **Reframing**: the relations are presented as a correspondence chosen by the author, a privileged candidate, not as a derivation. No geometric map from the invariants to the observables is known, and no rule assigns formulas to observables.
- **Dictionary, residue, decision rule**: twenty structural constants and a grammar; a residue register R1 to R12 of everything set by choice; a rule that rejects a relation with no repair clause.
- **The 33 relations against the most recent data** (PDG 2026, NuFIT 6.1, Planck 2018): 23 within 2σ of measurement, 3 in tension, 5 excluded as exact equalities at more than 3σ and kept as proximities, 1 inside a PDG range, 1 with a non-Gaussian profile. A single score over the 33 is no longer reported.
- **Not 33 independent tests**: three sectors are overdetermined, with relations that disagree as exact equalities.
- **The other 62 entries** of the dataset are conditional extractions and diagnostics, and are not counted as predictions.
- **Look-elsewhere**: a preregistered test in which every competitor searches for its own formulas. K₇ reaches 31 of the 33 targets and is not distinctive on closeness. Code and results are public in `publications/validation/v3.6/`.
- **Withdrawn**: the coincidence probabilities and uniqueness statements of versions 3.3 to 3.5, the reading of the relations as derived from the geometry, a primary lepton relation, and the Joyce–Karigiannis route to (21, 77).
- **Formal verification**: 156 Lean 4 files, 14 axioms (4 literature imports, 10 interval certificates), no sorry; the arithmetic of the 33 relations is collected in `relations_v36_certified` (commit 34ce857).

## v3.5, 2026-07-10

- Renamed "The K₇ Framework" (GIFT remains the name of the founding phase).
- Supplement S4 added; conditional framing throughout.
- **Erratum** (2026-08 to 2026-10, sections 1 to 11): [`ERRATUM_v3.5.md`](https://github.com/Arithmon/K7/blob/main/publications/ERRATUM_v3.5.md). Version 3.6 integrates it.

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

*For complete details, see the [full changelog](https://github.com/Arithmon/K7/blob/main/CHANGELOG.md).*
