# K7-P2 Candidate A — neutrino operator inventory

**Status:** `D1 / N0–N1 AUDIT — BLOCKED BEFORE MASS MATRIX`  
**Date:** 2026-09-11  
**K7 source baseline:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`  
**K7-Lean reference inspected:** `Arithmon/K7-Lean@0a1252cda1f63cb1054918d19471e86031843449`  
**Target-value exposure:** none added by this audit.

This document is a target-blind operator inventory for Candidate A of the K7-P2 workbench. It is **not** a neutrino-mass prediction and contains no fitted absolute-neutrino-mass number.

The purpose is to answer a prior question: does the current K7 framework already determine enough four-dimensional field content and operator structure to define a Dirac, Majorana or seesaw neutrino mass matrix?

**Current answer: no.** The most promising surviving route is an exact rank constraint, but the present rank-2 Wilson-line diagnostic is not yet a neutrino mass operator.

---

## 1. Clean-room operator basis

Before using K7-specific structure, the possible low-energy mass maps are separated explicitly.

### 1.1 Dirac route

A Dirac mass requires a right-handed neutrino field `N_R` and an allowed Yukawa operator

`L_D ⊃ - \bar L Y_nu \tilde H N_R + h.c.`

which gives

`m_D = Y_nu v / sqrt(2)`.

For K7 to predict an absolute mass through this route it must derive, rather than merely allow:

1. the existence and multiplicity of `N_R`;
2. its gauge / residual-U(1) charges;
3. the allowed Yukawa texture `Y_nu`;
4. the normalization of the relevant zero modes / overlap integrals;
5. any dimensionless coefficient entering `Y_nu`.

The electroweak VEV may be ledgered as a non-target experimental anchor, but using it does not derive `Y_nu`.

### 1.2 Majorana / Weinberg route

A low-energy Majorana mass may arise from the dimension-five Weinberg operator

`O5 = (L \tilde H)(L \tilde H) / Lambda`

with a symmetric flavor coefficient matrix. This violates lepton number by two units. K7 must therefore supply a physical mechanism that permits the operator and fixes its coefficient / scale.

A bare algebraic relation among K7 integers is not enough to identify `Lambda`.

### 1.3 Right-handed Majorana / type-I seesaw route

If `N_R` exists, a Majorana term

`L_M ⊃ -(1/2) N_R^T C M_R N_R + h.c.`

combined with the Dirac matrix gives, in the ordinary seesaw limit,

`m_nu = - m_D M_R^{-1} m_D^T`.

This route therefore requires **more** K7 structure, not less: both the Dirac operator and the lepton-number-violating heavy scale must be derived.

No `M_R`, `B-L` breaking scale or equivalent coefficient is currently present in the K7 neutrino layer inspected here.

---

## 2. What K7 currently contains

| Layer | Present in current K7? | What is actually established | Neutrino-mass status |
| --- | --- | --- | --- |
| `E8 -> E6 × SU(3)` branching | yes | algebraic representation-branching identity; Lean checks `248 = 78 + 8 + 2×27×3` | useful seed only |
| `E6 -> SO(10) × U(1)` step | yes | current Lean module checks the adjoint **dimension identity** `78 = 45 + 1 + 16 + 16` | does not by itself define matter fields or charges |
| three chiral families | claimed | current Lean route identifies `N_gen = 3` with the dimension of the `SU(3)` fundamental / `(27,3)` factor | **physical derivation not closed** |
| chiral non-abelian 4D sector | explicitly open | main K7 paper states the UV bridge to the chiral non-abelian sector is load-bearing open | blocker N0 |
| right-handed neutrino `N_R` | no K7-specific construction found | generic `E6/SO(10)` representation theory can accommodate neutral singlets / `nu_R` | not yet K7-derived field content |
| `B-L` or lepton-number charge ledger | no | the chain contains residual `U(1)` labels but current K7 does not derive their physical charge assignment as `B-L` | blocker N1/N2 |
| neutrino Dirac Yukawa matrix | no | current neutrino module contains mixing-angle arithmetic, not a mass operator | absent |
| `Delta L = 2` operator | no | no K7 Weinberg operator / Majorana term found | absent |
| fiber Wilson-line operator | yes | SVD `[5.71, 0.62, 2.4e-15]`, numerical rank 2 | **not a neutrino mass matrix** |
| adiabatic Yukawa rank | yes | numerical rank `<= 2` diagnostic | possible structural seed only |
| non-adiabatic rank-3 lift | yes | requires calibrated `c*=0.452` in the present phenomenology | forbidden as a K7-P2 target-blind ingredient |
| absolute mass scale | no clean neutrino scale | existing dimensional sectors use external / model-dependent anchors | blocker N4 |

---

## 3. Blocker N0 — field-content dictionary is not closed

The current framework correctly distinguishes an algebraic subgroup chain from a physical symmetry-breaking mechanism. This distinction becomes load-bearing for neutrinos.

### 3.1 M-theory / singular-`G2` reading

For four-dimensional non-abelian gauge symmetry and chiral fermions in an M-theory compactification on a `G2` space, the relevant singular structure must be specified. The current smooth / neck-level K7 construction does not yet provide the singular locus and localized chiral spectrum needed for a neutrino operator.

Reference background:

- B. Acharya and E. Witten, *Chiral Fermions from Manifolds of G2 Holonomy*, arXiv:hep-th/0109152.
- E. Witten, *Anomaly Cancellation On Manifolds Of G2 Holonomy*, arXiv:hep-th/0108165.

### 3.2 Heterotic / bundle reading

If the `(27,3)` branching is interpreted through a heterotic standard-embedding / bundle dictionary, the factor `3` in the `SU(3)` representation is **not by itself the net number of chiral generations**. Physical multiplicities are obtained from the compactification bundle, cohomology / index data and any quotient action.

A concrete standard-embedding example with three net chiral generations computes the spectrum from bundle geometry and cohomology rather than from `dim(3)` alone:

- V. Braun, P. Candelas, R. Davies, R. Donagi, *The MSSM Spectrum from (0,2)-Deformations of the Heterotic Standard Embedding*, arXiv:1112.1097.

### 3.3 Accounting consequence

The Lean theorem currently named `N_gen_from_SU3` certifies an arithmetic / dimension statement, not a theorem that K7 has produced three four-dimensional chiral families.

This does **not** invalidate the algebraic branching

`248 = (78,1) + (1,8) + (27,3) + (27bar,3bar)`.

It does mean that the route

`dim(fundamental SU(3)) = 3  =>  three chiral families`

must not be used as a physical premise for K7-P2 until an index / cohomology / localized-mode construction supplies the missing map.

Other K7 uses of the discrete input `N_gen = 3` remain separate ledger items; they are not promoted by this branching argument.

---

## 4. Blocker N1 — `N_R` is allowed in neighboring representation theory, not yet derived by K7

The `E6 -> SO(10) × U(1)` route is interesting because standard `E6/SO(10)` representation theory can contain neutral singlets and a right-handed neutrino. For example, `E6` models commonly use the fundamental `27`, whose `SO(10)` content includes matter capable of housing `nu_R` plus additional neutral states.

This makes a Dirac or seesaw construction **plausible as a route**, but plausibility is not a K7 field-content theorem.

Useful background examples:

- J. L. Rosner, *Three sterile neutrinos in E6*, arXiv:1404.5198.
- E. Ma, *Naturally Light Dirac Neutrinos from SO(10) × U(1)_psi*, arXiv:2103.15013.

Before K7 uses `N_R`, it must specify the actual matter representation surviving the compactification and its charges under every residual gauge / discrete symmetry relevant to the mass operator.

---

## 5. Blocker N2 — no lepton-number selection rule yet

The repository search found no K7-specific `B-L` / lepton-number construction that decides whether a Majorana term is allowed.

Therefore none of the following may currently be assumed:

- an `N_R N_R` Majorana mass;
- a dimension-five `(LH)(LH)` operator;
- a seesaw scale;
- exact Diracness of the light neutrinos.

A future non-perturbative route (for example an instanton-generated superpotential term) is admissible only if K7 computes the relevant charged zero modes / selection rule and coefficient. Generic facts about membrane or string instantons do not determine a K7 neutrino operator.

---

## 6. The rank-2 route — the strongest surviving hypothesis seed

The current K7 spectral / Wilson-line layer contains a robust-looking numerical fact:

`singular values = [5.71, 0.62, 2.4e-15]`

so the inspected fiber-level operator is numerically rank 2. The current v3.5 text correctly calls this rank 2; older prose that called the same spectrum rank 3 is not used here.

The associated adiabatic Yukawa diagnostic is also rank `<= 2`, while the present non-adiabatic rank-3 completion uses the calibrated coefficient `c*=0.452` and charged-lepton targets. That calibrated lift is ineligible for K7-P2.

### 6.1 Exact question to prove or kill

The admissible question is **not**

> “Can we interpret the machine-zero singular value as a massless neutrino?”

It is:

> **Can a neutrino mass operator be derived from K7 whose flavor map is functorially / geometrically inherited from an exact rank-2 operator, with no target-dependent sector assignment or fitted lifting coefficient?**

Until that map exists, the rank-2 observation earns zero prospective-prediction credit.

### 6.2 What would follow if an exact map were proved

If a physically derived `3×3` Dirac or Majorana light-neutrino mass matrix had exact rank 2, then exactly one light-neutrino mass would vanish at the frozen level.

That would be a strong prospective structure because it removes the otherwise free absolute mass scale. It would still **not** fix which eigenstate is massless unless K7 independently fixes the ordering / eigenvector identification.

Only after both rank and ordering are fixed could already-measured oscillation quantities be ledgered as non-target calibration anchors to obtain a definite beta-decay effective mass:

`m_beta^2 = sum_i |U_ei|^2 m_i^2`.

No numerical oscillation values are inserted in this D1 note.

---

## 7. Decision tree

### N0 — choose and close one UV / compactification dictionary

**Required:** a single physical route that produces chiral four-dimensional matter. Do not silently alternate between a smooth-`G2` M-theory dictionary and a heterotic bundle dictionary when convenient.

Pass condition: explicit field-spectrum map with a reproducible generation index / multiplicity calculation.

### N1 — derive the neutrino-capable field content

Pass condition:

- identify `L` and `H` in the compactified spectrum;
- either derive `N_R` with its multiplicity and charges or explicitly prove that it is absent;
- ledger every residual `U(1)` / discrete charge relevant to neutrino operators.

### N2 — derive the allowed operator class

Pass condition: K7 selects one or more of

- Dirac Yukawa;
- right-handed Majorana;
- Weinberg dimension-five;
- another explicit operator,

with a derived symmetry / zero-mode reason for what is allowed and forbidden.

### N3 — derive texture, rank and eigenstate map

Pass condition: the mass-matrix texture is fixed before any absolute-mass target is inspected. A rank-2 theorem must be exact or have a controlled nonzero bound; “machine zero” alone is insufficient.

### N4 — derive or ledger the dimensionful scale

Pass condition: every dimensionful input is either

- predicted by the same frozen K7 construction, or
- declared in advance as an independent non-target calibration anchor.

No direct neutrino absolute-mass datum may enter this layer.

### N5 — only then instantiate K7-P2

After N0–N4 close:

1. write an executable target-free reproducer;
2. freeze the mass spectrum and `m_beta`;
3. name the experimental comparison and null;
4. commit the falsifier and no-revision rule;
5. only then open existing direct absolute-mass results.

---

## 8. Immediate scientific tasks

1. **Correct the epistemic label of `N_gen_from_SU3`.** Preserve the branching arithmetic, but do not call `dim(3)=3` a derivation of three physical chiral generations.
2. **Select one UV dictionary for Candidate A.** The choice itself is a model choice and must be ledgered.
3. **Build the actual matter-representation decomposition**, including charges and multiplicities, not only adjoint dimensions.
4. **Determine whether `N_R` survives** and whether lepton number / `B-L` is exact, broken, gauged or absent.
5. **Derive the neutrino operator before its spectrum.** No mass fractions or K7-number search is allowed beforehand.
6. **Test the exact rank-2 inheritance hypothesis.** If the map fails, discard it; do not search for a different rank-2-looking operator.

---

## 9. Current ruling

Candidate A remains the highest-priority K7-P2 route because its target has not been used to construct a K7 mass formula.

But its state is now more precise:

> **`BLOCKED AT N0/N1 — chiral field-content map not yet derived; rank-2 route retained as a falsifiable structural hypothesis.`**

There is no K7-P2 neutrino mass prediction at this stage.
