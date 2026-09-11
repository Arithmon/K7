# K7-P2 Candidate A — N0-H heterotic-dual route

**Status:** `PROVISIONAL PREFERRED ROUTE — NOT YET ADMISSIBLE`  
**Date:** 2026-09-11  
**Target-value exposure:** none added by this route analysis.

This note selects the first UV dictionary to test for Candidate A. It does **not** assert that the duality applies to the present K7 construction, and it does not instantiate K7-P2.

The route is preferred because it preserves both pieces already present in the framework:

1. K7 is studied as a K3-fibered / G2 compactification candidate;
2. the gauge architecture is written in E8×E8 language with the algebraic branching `E8 -> E6 × SU(3)`.

A fiberwise M-theory / heterotic duality is known for appropriate K3-fibered G2 manifolds. The explicit TCS subclass in the literature maps M-theory on an elliptically K3-fibered G2 manifold to E8×E8 heterotic string theory on a Calabi-Yau threefold, with the heterotic bundle data encoded by the G2/TCS geometry.

Primary background:

- A. Braun, S. Schäfer-Nameki, *Compact, Singular G2-Holonomy Manifolds and M/Heterotic/F-Theory Duality*, arXiv:1708.07215.
- S. Gukov, S.-T. Yau, E. Zaslow, *Duality and Fibrations on G2 Manifolds*, arXiv:hep-th/0203217.

---

## 1. Why this route is preferred over adding a singular-G2 matter sector by hand

A direct M-theory-on-singular-G2 route is physically legitimate in principle, but current K7 does not specify the ADE singular locus, localized chiral spectrum, representations or interaction data. Introducing those now would add a large new model-selection layer.

The heterotic-dual route instead gives a concrete interpretation of structures K7 already invokes:

- `E8 × E8` is native on the heterotic side;
- an `SU(3)` bundle structure group has commutant `E6` in `E8`;
- chiral multiplicities become an index / bundle-cohomology calculation;
- `E6 -> SO(10)` supplies a standard representation-theory route to neutrino-capable matter;
- Yukawa matrices can in principle be computed from bundle cohomology / overlap data rather than guessed from arithmetic matches.

This is an **epistemic preference**, not evidence that the required dual geometry already exists for K7.

---

## 2. Gate H0 — prove that the K7 fibration lies in a usable duality class

The explicit duality construction of Braun–Schäfer-Nameki requires the relevant K3 fibers to carry additional elliptic-fibration structure so that M-theory / heterotic duality can be applied fiberwise.

The current K7 baseline does contain a K3 fibration in the Donaldson / rank-one 77-unlink program. However, targeted repository searches found no explicit K3 Weierstrass model, no `dP9` building-block description and no theorem that the K3 fibers used by K7 are elliptically fibered in a way compatible with the monodromy / matching data.

Therefore the first gate is:

> **H0: construct or identify an elliptic fibration on the K7 K3 fibers and prove compatibility with the K7 monodromy / gluing data.**

### H0 falsifier

If no compatible elliptic K3 structure exists for the frozen K7 fibration data, **abandon N0-H**. Do not import a heterotic dual Calabi-Yau by analogy.

---

## 3. Conditional consequence of passing H0 — the Schoen dual benchmark

For the explicit elliptically K3-fibered TCS subclass treated in the duality literature, the heterotic Calabi-Yau is the Schoen / split-bicubic threefold

`X_het = X_(19,19)`

with

`h^(1,1) = h^(2,1) = 19`, hence `chi(X_het)=0`.

Different TCS G2 geometries in this class correspond to different choices of heterotic vector-bundle data on the same Schoen threefold.

This gives a sharp accounting rule:

> K7 may use the Schoen benchmark only after H0 establishes that its actual building-block / fibration data belong to this duality class.

No claim is made yet that `(b2,b3)=(21,77)` uniquely selects the Schoen dual or a unique bundle.

---

## 4. Gate H1 — the current “standard embedding” shortcut cannot give three net generations on Schoen

For a heterotic compactification with `c1(V)=0`, the net chiral generation index is

`N_chiral = (1/2) ∫_X c3(V)`

up to the conventional sign used to label generations versus anti-generations.

For the **standard embedding** `V = TX`, one has

`∫ c3(TX) = chi(X)`.

Therefore on the Schoen threefold,

`chi(X_(19,19)) = 0`

implies

`N_chiral = 0`

for the standard embedding.

### Consequence

If N0-H is the K7 route, the phrase “standard embedding” cannot simultaneously be used to justify the `E6` branch and three chiral generations on the Schoen dual.

Three net families require a **non-standard stable SU(3) bundle** `V` satisfying

`(1/2) ∫_X c3(V) = ±3`.

This is a major improvement over `N_gen = dim(3)`: the generation question becomes a topological bundle condition that can be computed and falsified.

Background on the heterotic index:

- G. Curio, *Chiral matter and transitions in heterotic string models*, arXiv:hep-th/9803224.
- V. Braun, P. Candelas, R. Davies, R. Donagi, *The MSSM Spectrum from (0,2)-Deformations of the Heterotic Standard Embedding*, arXiv:1112.1097.

---

## 5. Gate H2 — derive the bundle from K7 rather than choose one to obtain `c3=±6`

Finding **some** SU(3) bundle on Schoen with `c3(V)=±6` would not be a K7 prediction. Candidate A needs the K7 geometry to select or constrain the bundle before the desired generation index is imposed.

Required data include:

1. a bundle `V1` in the visible `E8` with structure group `SU(3)` (or a precisely stated alternative);
2. the hidden-sector bundle `V2` / five-brane class where required;
3. anomaly / Bianchi consistency, schematically

   `c2(TX) - c2(V1) - c2(V2) = [W]`

   with `[W]` an allowed effective five-brane class when nonzero;
4. `c3(V1)` computed from the selected bundle, **not fixed by demanding three generations**;
5. the relevant bundle moduli and any discrete flux / spectral-cover choices counted in the free-choice ledger.

### H2 pass condition

The K7-to-bundle map is specified independently of the desired `N_chiral`, and its computed index happens to give a definite value.

If that value is not `±3`, record the failure. Do not choose a different bundle after reading the result and call the replacement the same prediction route.

---

## 6. Gate H3 — compute the actual chiral spectrum

Even `N_chiral=3` is only a **net index**. It does not prove “exactly three families and no vector-like pairs.”

The next layer must compute the appropriate bundle cohomologies, schematically

`H^1(X,V)` and `H^1(X,V*)`

(or the correct representations for the selected bundle construction), together with any quotient / Wilson-line action.

Pass condition:

- actual massless `E6` matter multiplicities are computed;
- vector-like exotics are identified rather than hidden in the net index;
- the subsequent `E6 -> SO(10) -> ...` breaking data are explicit.

---

## 7. Gate H4 — neutrino-capable field content

Only after H3 may Candidate A ask whether the surviving matter contains:

- the lepton doublets `L_i`;
- Higgs doublet(s) `H`;
- right-handed neutrino fields `N_Ri` or other neutral singlets;
- residual `U(1)` / discrete charges controlling lepton-number violation.

Standard E6/SO(10) representation theory makes such a spectrum plausible, but K7 must derive which components survive the compactification / quotient.

No `N_R` may be introduced merely because a generic `27` can contain neutral singlets.

---

## 8. Gate H5 — operator and rank

The neutrino mass mechanism is then selected by the derived spectrum and symmetries:

- Dirac if `L H N_R` is allowed and Majorana terms are forbidden;
- seesaw if both `L H N_R` and a derived `N_R N_R` scale exist;
- Weinberg / another Majorana operator if a controlled `Delta L=2` mechanism generates it.

The strongest surviving K7-specific hypothesis remains the rank route:

> Does the rank-2 K7 fiber / adiabatic operator map, under the now-explicit duality, to an exact rank constraint on the neutrino Yukawa or effective mass matrix?

The duality map must be shown. Numerical similarity of ranks earns no credit.

If an exact physical `3×3` light-neutrino matrix is forced to rank 2, then one mass eigenvalue is zero at the frozen level. If K7 independently fixes which eigenstate is zero, a definite beta-decay `m_beta` can subsequently be computed using separately ledgered oscillation anchors.

No numerical `m_beta` is computed at N0-H.

---

## 9. Route scorecard

| Gate | Question | Current state |
| --- | --- | --- |
| H0 | Are K7's K3 fibers elliptically fibered compatibly with gluing / monodromy? | **OPEN / not established** |
| H1 | Does the dual CY / embedding support nonzero chirality? | **standard embedding fails on Schoen (`chi=0`)** |
| H2 | Does K7 derive a non-standard SU(3) bundle and its Chern classes? | **ABSENT** |
| H3 | Are the physical chiral cohomologies / multiplicities computed? | **ABSENT** |
| H4 | Does `N_R` survive with fixed charges? | **ABSENT** |
| H5 | Is the neutrino operator / exact rank derived? | **ABSENT** |

### Current route ruling

`N0-H` is the **preferred route to test first**, because it is the least discontinuous with K7's existing K3-fibered `G2` and `E8×E8 -> E6×SU(3)` architecture.

It is not yet an accepted K7 physical dictionary.

The immediate scientific task is H0, not a neutrino mass calculation.
