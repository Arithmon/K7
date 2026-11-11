---
title: "Paper S2 Derivations"
layout: default
---

# Paper: S2, The 33 Relations

**Supplement S2: The 33 Relations. Arithmetic, Dictionary Choices and Status** (The K₇ Framework, v3.6)

*Brieuc de La Fournière (2026)*

[**PDF (14 pp.)**](https://github.com/Arithmon/K7/raw/main/publications/papers/pdf/k7_framework_3_6_S2_derivations.pdf) | concept DOI [10.5281/zenodo.16891489](https://doi.org/10.5281/zenodo.16891489) (version 3.6 not yet deposited) | [Markdown](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S2_derivations.md)

---

## What the supplement establishes

Earlier versions of this supplement were titled "Complete Derivations" and presented each relation as a theorem with a proof. Version 3.6 withdraws that framing. For each of the 33 relations the supplement establishes three things, and no more:

1. **The arithmetic.** Given the declared constants, the closed form evaluates to the stated number. Each relation has a Lean statement tying its closed form to its value (`relations_v36_certified`, [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean)).
2. **The dictionary choices.** Which constants the formula uses, which operations beyond integer ratios, and which entries of the residue register (R1 to R12) it depends on.
3. **The status** against the most recent data, generated from the dataset: 23 within 2σ of measurement, 3 in tension, 5 excluded as exact equalities at more than 3σ and kept as proximities, 1 inside a PDG range, 1 with a non-Gaussian profile.

What the arithmetic does not establish: that the formula is the right one for the observable, that the structure requires it, or that agreement with measurement is evidence for the framework (main §7). Section S2.7 records the alternative formulas found for the same observables; their number measures the freedom of the vocabulary, not robustness.

---

## Sections

- S2.0 What this supplement establishes
- S2.1 Notation
- S2.2 Gauge sector and Higgs
- S2.3 Leptons (overdetermined: R8)
- S2.4 Quarks, CKM and boson masses
- S2.5 Neutrino mixing
- S2.6 Cosmology (overdetermined: R11)
- S2.7 Vocabulary freedom: alternative formulas in the corpus
- S2.8 Withdrawn readings

---

## Related

- [Paper Main](Paper-Main-Framework.html)
- [Paper S1 Foundations](Paper-S1-Foundations.html)
- [Observable Reference](Observable-Reference.html)
- [Lean Formalization](Lean-Formalization.html)
