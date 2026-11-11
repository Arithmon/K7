---
title: "For Physicists"
layout: default
---

# The K₇ Dictionary: a Technical Overview for Physicists

*As of version 3.6 of the framework paper. Where this page and the [main paper](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) differ, the paper holds.*

## Abstract

The K₇ framework states a **declared correspondence**: the topological and Lie-theoretic invariants of a compact seven-manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with an E₈×E₈ gauge structure, are assigned to 33 dimensionless Standard-Model and cosmological parameters by explicit closed forms. It is presented as a privileged candidate, not as a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable. The paper makes the correspondence auditable, with a dictionary, a residue register and a decision rule.

## 1. The parameter problem and the selection problem

The Standard Model leaves about nineteen parameters to measurement and explains neither its gauge group nor its three generations. Any framework that proposes structure behind these numbers inherits two questions that are easily run together:

1. **Does a family of structures deserve to be explored?** For K₇ the answer is positive: the octonions, G₂ holonomy and E₈ are structures whose interest owes nothing to the Standard Model's constants.
2. **Why this precise structure, and these precise assignments?** This is **not** answered. The pair (21, 77) is not derived, and the formulas are assigned, not forced.

## 2. The inputs

**E₈×E₈.** Used as a source of group-theoretic integers (dimensions, ranks, representation dimensions of E₈ and of its exceptional subgroups). The framework does not embed Standard-Model fermions in E₈, which avoids the Distler–Garibaldi obstruction and also means it makes no claim about how the fermions arise.

**G₂ holonomy.** In seven dimensions G₂ is the exceptional holonomy group of Berger's list; it is the automorphism group of the octonions and the condition for N = 1 supersymmetry in an M-theory compactification on a seven-manifold.

**K₇.** A compact G₂-holonomy manifold with (b₂, b₃) = (21, 77) is *posited*. **No such manifold is currently constructed**; the topological route of version 3.5 does not realise the pair. The companion papers certify local or conditional pieces (a Newton–Kantorovich-certified seam metric, a neck ansatz), not a compact K₇. The relations use only the declared integers and no metric.

**What is not supplied.** A smooth G₂ compactification gives an abelian, non-chiral four-dimensional theory. The chiral non-abelian content of the Standard Model would require a UV bridge (a singular locus, a heterotic bundle, or a duality) that the framework does not provide. The relations are not derived from a four-dimensional effective theory, and they are not stated at a common energy scale: each comparison carries a (scheme, scale, dataset) tag.

## 3. The dictionary

All 33 relations are written in twenty structural constants: seven primitive (among them dim E₈ = 248, rank E₈ = 8, dim G₂ = 14, dim K₇ = 7, b₂ = 21, b₃ = 77) and thirteen derived (for instance H* = b₂ + b₃ + 1 = 99, N_gen = 3, the Weyl factor 5, |PSL(2,7)| = 168). The grammar is ratios and small integer combinations, with four further operations declared when used (√, φ, ln 2, ζ values).

Representative entries:

| Observable | Formula | K₇ value | Measured | Pull | Status |
|---|---|---|---|---|---|
| sin²θ_W (M_Z, MS-bar) | b₂/(b₃ + dim G₂) = 3/13 | 0.230769 | 0.23122(6) | −7.5σ | proximity |
| α_s(M_Z) | √2/(dim G₂ − p₂) = √2/12 | 0.117851 | 0.1180(9) | −0.2σ | within 2σ |
| Q_Koide | dim G₂/b₂ = 2/3 | 0.666667 | 0.6666645(51) | +0.4σ | within 2σ |
| m_τ/m_e | 7 + 10·248 + 10·99 = 3477 | 3477 | 3477.37(18) | −2.1σ | tension |
| sin²θ₂₃ (PMNS) | 6/11 | 0.545455 | 0.470 (+17/−14) | second octant | inside the NuFIT 3σ range |
| δ_CP | 7·14 + 99 = 197, read in degrees | 197° | 212 (+26/−36)° | −0.4σ | unit assignment |
| m_W/m_Z | 37/42 | 0.880952 | 0.881285(87) | −3.8σ | proximity |
| Ω_DE | ln 2 · 98/99 | 0.686146 | 0.6847(73) | +0.2σ | within 2σ |

The complete table is in the [Observable Reference](Observable-Reference.html).

**The residue register.** What was set rather than derived is listed and ranked with the results (R1 to R12): the Betti pair; the imposed normalization det(g) = 65/32; the combination κ_T⁻¹ = 61; the unit in which 197 is read as a phase; the scales and mass schemes of the comparisons; the formula assignments; and, in three overdetermined sectors, the absence of a choice among mutually incompatible relations.

## 4. Where the relations stand

Against PDG 2026, NuFIT 6.1, Planck 2018 and CODATA 2022, with uncertainties at 1σ: 23 relations lie within 2σ; 2 are in tension (m_τ/m_e, Ω_c/Ω_m); 6 are excluded as exact equalities at more than 3σ and retained as proximities (α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t, m_W/m_Z); m_s/m_d lies inside a PDG range that carries no uncertainty; sin²θ₂₃ sits in the second octant, inside the 3σ range of the global fit. The classes are not added into one score.

The 33 are **not independent tests**. Four lepton relations bear on two mass ratios, three CKM relations on two Wolfenstein parameters (sin θ₂₃ = Aλ², 2.6% apart), seven density relations on two independent densities. In each sector the relations are mutually incompatible as exact equalities, and none is selected. Other dependencies exist (sin²θ_W and m_W/m_Z are related through radiative corrections) and the audit is not complete.

Six relations use det(g) = 65/32 and three use κ_T⁻¹ = 61. A reader who regards the imposed normalization as an extra parameter should read the framework through the reduced counts given in the [Validation Summary](Validation-Summary.html).

## 5. Look-elsewhere

In a preregistered test, every competitor searches for its own formulas in the same grammar, at the same budget (five nodes) and with the same windows (2σ). K₇ reaches 31 of the 33 targets; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many, and none reaches more. The global p-value is 0.51 against a threshold of 0.01: the effect is not overcome. A control with no K₇ constant reaches 30. In the public Sieve battery, no K₇ relation clears the null that prices the choice of vocabulary.

Closeness to the measured values is therefore not, by itself, evidence. The coincidence probabilities and P-values of earlier versions are withdrawn. Details and code: [Statistical Evidence](Statistical-Evidence.html).

## 6. What is claimed, and what is not

**Claimed.** Given the declared constants and assignments, the 33 relations hold as arithmetic identities (machine-checked in Lean 4), and they lie at the stated deviations from measurement. The decision rule applies to them.

**Not claimed.** That the relations are derived from the geometry of K₇; that (21, 77), the formulas or det(g) = 65/32 are forced by any requirement; that the relations hold at a common scale; that closeness is evidence; that the manifold has been constructed; that the chiral Standard Model follows from it.

## 7. Decision rule

The relations are exact equalities with no theoretical uncertainty. A relation is rejected when its reference series excludes its value at 3σ, and it is not rescued by changing its formula, unit, scale or dataset.

| Quantity | K₇ value | Rejected by |
|---|---|---|
| δ_CP (phase 2π·197/360) | 197° | a global fit, with DUNE or Hyper-Kamiokande, whose 3σ interval excludes 197°; the unit assignment falls with it |
| sin²θ₂₃ | 6/11 | a global fit whose 3σ interval excludes 6/11, in either octant |
| sin²θ₁₂ | 4/13 | a global fit whose 3σ interval excludes 4/13; JUNO's first result is 0.3092 ± 0.0087, and its six-year precision is about four times that of today's global fit |
| m_τ/m_e, Q_Koide | m_τ = 1776.74 and 1776.97 MeV | an m_τ value whose 3σ interval excludes the value; the two differ by 0.23 MeV |
| N_gen | 3 | a fourth sequential generation |
| m_s/m_d | 20 | a lattice determination with an uncertainty whose 3σ interval excludes 20 |

Outside the reference series, h = 167/248 is excluded by SH0ES at 5.5σ while agreeing with Planck, and the baryon acoustic oscillations of DESI (second data release) combined with the cosmic microwave background put Ω_Λ/Ω_m = 113/52, Ω_m/Ω_Λ = 28/61, Ω_DE and h at −3.3σ, +3.4σ, −3.1σ and −3.0σ (about 2σ for the three density relations with DESI alone); both are reported beside the class. A rejection rejects a relation and its assignment, not the programme by itself; a confirmation would confirm an assignment, not a requirement of the structure.

## 8. Relation to other approaches

**M-theory.** E₈×E₈ and G₂ holonomy both appear in M-theory. The framework does not supply a compactification of either kind and differs from standard G₂ phenomenology, which works with moduli stabilization and singular compactifications.

**Direct E₈ embeddings.** Not attempted (Distler–Garibaldi).

**The string landscape.** The framework does not solve a selection problem; it has one of its own, stated in the residue register.

## 9. Summary

Thirty-three dimensionless parameters are matched by closed forms in the invariants of a G₂-holonomy seven-manifold with (21, 77) and of E₈×E₈. The correspondence is not derived, its closeness to the data is not distinctive, and its manifold is not constructed. What it offers is rigidity (no continuous parameter), a written residue, and a rule fixed in advance under which individual relations can be rejected. The paper does not claim that the framework is correct.

---

*K₇ Framework v3.6*
