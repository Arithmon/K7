# K7-P2 Candidate A — H0a.3 equivariant elliptic data contract

**Status:** `RANK-15 V4 SUBGATES PARTIAL PASS / FULL JK AT rho=15 FAIL / HIGHER-PICARD rho>=17 OPEN`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent gate:** [`K7_P2_neutrino_H0_fiber_lattice_gate.md`](K7_P2_neutrino_H0_fiber_lattice_gate.md)  
**Rank-15 fiber result:** [`K7_P2_neutrino_rank15_CM_V4_gate.md`](K7_P2_neutrino_rank15_CM_V4_gate.md)  
**Full-group obstruction:** [`K7_P2_neutrino_JK_character_obstruction.md`](K7_P2_neutrino_JK_character_obstruction.md)

This file began as the exact data contract for H0a.3. Recovery of the rank-15 K3 package conditionally closed the `V4`-preserved fiber and Donaldson-reflection parts. A subsequent exact character calculation now closes a different question negatively:

> **The frozen Joyce–Karigiannis `(Z/2)^3` fixed-locus package is impossible at Picard rank 15. Any realization of that exact package must have `rho>=17`.**

No neutrino mass, ordering, or preferred experimental value is used here.

---

## 1. Rank-15 lattice package — useful but no longer a full-JK candidate

The recovered K3 work uses

`NS(X) = U ⊕ E7(-1) ⊕ A1(-1)^6`,

of Nikulin type `(15,7,1)`, with absolute determinant `2^7` and signature `(1,14)`.

In the `U` basis `(e,f)`, define

- `F=e`,
- `S=f-e`,
- `h=4e+f`.

Then exactly

- `F^2=0`,
- `S^2=-2`,
- `F.S=1`,
- `h^2=8`.

The public dependency-free check is

```bash
python3 docs/openwave-candidate/check_k3_rank15_cm_v4_gate.py
```

### D1 ruling

**PASS as exact rank-15 lattice arithmetic; conditional as K7 geometry.** The Gram and the `F,S,h` witnesses are explicit. However this lattice can no longer be the carrier of the **full frozen JK package**, because that package has a separate rank obstruction described below.

---

## 2. D2 — geometric `V4` fiber preservation

The retained geometric rank-15 model is a Jacobian elliptic K3 of Clingher–Malmendier type with

`y^2 = x (x-A(t)) (x-B(t))`

and Mordell–Weil 2-torsion

`MW_tors ≅ (Z/2Z)^2`.

Translations by two independent 2-torsion sections generate a genuine symplectic `V4` and preserve the elliptic fiber class `F`.

The historical phase-D8 block-sign matrices are excluded from this ruling: later audit showed that they are not the geometric Mukai `V4` action.

### D2 ruling

**CONDITIONAL PASS for the rank-15 CM `V4` subgroup.** This remains a valid local/fiber result, but it no longer promotes to a full JK realization at `rho=15`.

---

## 3. D3 — Donaldson Picard–Lefschetz monodromy

The recovered NS embedding contains

`M = U ⊕ D4(-1) ⊕ A1(-1)^5`

and a rank-4 negative-definite orthogonal complement `Mperp`. The surviving algebraic `alpha_1` candidates all lie in `Mperp`.

Since `U=<e,f> subset M`, every candidate obeys

`F.alpha_1=0`.

For a `(-2)` root,

`s_alpha(v)=v+(v.alpha)alpha`,

hence

`s_alpha(F)=F`.

### D3 ruling

**CONDITIONAL PASS at rank-15 lattice level.** The unresolved Donaldson root selection cannot destroy this CM fiber. This result is orthogonal to the new full-group obstruction.

---

## 4. D4 — selected rank-15 fiber and section

Inside the recovered Jacobian model,

- `F` is a fiber divisor;
- `S` is a section with `F.S=1` and `S^2=-2`.

### D4 ruling

**CONDITIONAL PASS inside the rank-15 CM model.** If the final construction moves to the now-required `rho>=17` K3, the particular `F,S` pair must be reconstructed there.

---

## 5. New load-bearing result — full JK package excludes rho=15

The frozen JK target requires

- three symplectic `V4` involutions with eight isolated fixed points each;
- `tau` of type `(11,7,1)`, hence fixed locus `(g,k)=(2,2)`;
- the three `tau sigma` elements of type `(11,9,1)`, hence `(g,k)=(1,1)`.

Topological Lefschetz therefore fixes the character on `H^2(K3)` to

`(22,0,6,6,0,0,6,0)`

in the element order

`(1,tau,sigma_A,sigma_B,tau sigma_A,tau sigma_B,sigma_A sigma_B,tau sigma_A sigma_B)`.

For `rho=15`, `T_X` has rank 7. Finite symplectic automorphisms act trivially on `T_X`; the non-symplectic `tau` acts by `-I` there. Thus

`chi_NS = (15,7,-1,-1,7,7,-1,7)`.

Fourier inversion over `(Z/2)^3` gives multiplicity `-2` for the character that changes sign only under `tau`. This is impossible for a genuine representation.

More generally the offending multiplicity is

`m_tau = rho - 17`.

Hence

`rho >= 17`

is necessary for the exact frozen JK profile.

The public reproducer is

```bash
python3 docs/openwave-candidate/check_k3_jk_character_gate.py
```

### Full-JK rank-15 ruling

**FAIL.** This is a structural obstruction, not a missing matrix or a failed numerical search.

---

## 6. Historical realization audit

The no-go clarifies three previously overlapping construction attempts.

### A. Direct Clingher–Malmendier route

The obvious commuting anti-symplectic involution preserves the CM fibration but acts trivially on all of `NS`, so its invariant lattice has rank 15 rather than target rank 11. Historical coset and base-involution searches did not recover the target package.

**Status:** **FAIL for full frozen JK at rank 15.**

### B. Historical abstract 15×15 / Torelli route

The abstract matrices were assigned the target fixed-lattice ranks, but the later transcendental-character audit produced a negative multiplicity. The new public character check shows why: the problem is intrinsic to `rho=15` under the frozen target traces.

**Status:** **FAIL.**

### C. `T5''` explicit CI(2,2,2)

The later projective construction successfully realizes a smooth numerical CI(2,2,2) with a Mukai-type symplectic `V4` and an anti-symplectic coordinate involution. But it records the three `tau sigma` involutions as **free**, yielding Enriques quotients.

The frozen target `(11,9,1)` instead gives `(g,k)=(1,1)`: an elliptic curve plus one rational curve. Therefore the `T5''` cosets do not realize the target fixed loci.

**Status:** **FAIL for the frozen JK profile.**

---

## 7. What the higher-Picard pivot buys us

The target `H^2` character has full-group invariant rank

`rk H^2(K3)^G = 5`.

For a successful anti-symplectic `G` action these invariant directions are algebraic; an averaged ample class gives the positive direction. Thus the invariant lattice is expected to have signature `(1,4)`.

An integral indefinite lattice of rank 5 represents zero by Meyer's theorem. Consequently, once a genuine `rho>=17` realization of the frozen JK package exists, a **full-`G` invariant isotropic class is forced at lattice level**.

This is the positive surprise hidden inside the no-go:

> the rank-15 model cannot host the desired group, but the corrected full-group target naturally supplies enough invariant algebraic lattice to recover a common genus-one fiber class.

What is not automatic:

- nef/effective chamber control for that isotropic class;
- a section for that particular fibration;
- a degree-8 polarization on the same realization;
- the global JK resolution/matching and heterotic dual dictionary.

---

## 8. Revised exact input package

The next admissible K3 realization must publish:

### D1'
An exact `NS(X)` with

`rho>=17`,

including an explicit degree-8 polarization.

### D2'
Exact or theorem-grade geometric realization of

`G=(Z/2)^3=<tau,sigma_A,sigma_B>`

with

- `V4=<sigma_A,sigma_B>` symplectic;
- `tau` type `(11,7,1)`;
- all three `tau sigma` elements type `(11,9,1)`.

### D3'
The same Donaldson / matching data expressed on this new lattice, not inherited silently from the rank-15 model.

### D4'
An explicit primitive full-`G` invariant isotropic class `F`, followed by nef/effective and section checks.

The character reproducer is a hard preregistered falsifier: any proposed realization with `rho<17` fails before further tuning.

---

## 9. Current H0a.3 table

| Item | Status |
| --- | --- |
| rank-15 exact NS / `F,S,h` arithmetic | **PASS** |
| rank-15 CM geometric `V4` preserves its fiber | **CONDITIONAL PASS** |
| rank-15 Donaldson reflection preserves that fiber | **CONDITIONAL PASS** |
| full frozen JK package at `rho=15` | **FAIL — character obstruction** |
| historical `T5''` anti-symplectic cosets match target | **FAIL — free vs `(g,k)=(1,1)`** |
| higher-Picard full-JK realization | **OPEN — `rho>=17` necessary** |
| invariant isotropic at lattice level once full target group exists | **FORCED by rank-5 invariant lattice + Meyer** |
| nef representative + section on actual higher-Picard model | **OPEN** |
| global K7 / heterotic duality | **OPEN** |

---

## 10. Next gate

Do **not** compute a neutrino mass yet.

The next construction task is now:

> **find a degree-8 K3 with `rho>=17` realizing the exact frozen JK fixed-locus package, then extract the forced full-group invariant isotropic class and test nefness/section data.**

Only after that can H0b and the heterotic bundle / chiral spectrum gates be addressed.