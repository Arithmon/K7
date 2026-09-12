# K7-P2 Candidate A — rank-15 Clingher–Malmendier fiber gate

**Status:** `H0a.3a V4-FIBER CONDITIONAL PASS / H0a.3b DONALDSON REFLECTION CONDITIONAL PASS / FULL JK AT rho=15 FAIL`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent gate:** [`K7_P2_neutrino_H0a3_equivariant_data_contract.md`](K7_P2_neutrino_H0a3_equivariant_data_contract.md)  
**Character obstruction:** [`K7_P2_neutrino_JK_character_obstruction.md`](K7_P2_neutrino_JK_character_obstruction.md)

This note records the recovery of the rank-15 K3 lattice that had previously appeared in the public K7-Lean changelog only as a private cross-check. It closes the `V4`-preserved elliptic-fiber problem for the recovered Clingher–Malmendier model, but a subsequent full-group character audit now proves that the **frozen JK `(Z/2)^3` fixed-locus package cannot coexist at Picard rank 15**.

The recovered canonical research record is from `gift-framework/private`. Because that workspace is not itself a public dependency of this dossier, the arithmetic used below is reproduced here from scratch and every historical geometric identification is treated conservatively.

---

## 1. Recovered rank-15 Néron–Severi lattice

The exact lattice used in the canonical K3 work is

`NS(X) = U ⊕ E7(-1) ⊕ A1(-1)^6`.

It has

- rank `15`;
- determinant `2^7` in absolute value;
- signature `(1,14)`;
- the 2-elementary Nikulin type `(r,a,delta)=(15,7,1)`.

Let `(e,f)` denote the standard basis of the `U` summand,

`e^2=f^2=0`, `e.f=1`.

Then the following classes are exact:

`F := e`,

`S := f-e`,

`h := 4e+f`.

They satisfy

`F^2=0`,

`S^2=-2`,

`F.S=1`,

`h^2=8`.

Thus the rank-15 lattice contains, in its algebraic `NS(X)` rather than only in ambient `H^2`, both a primitive hyperbolic plane and an explicit degree-8 polarization.

The dependency-free reproducer is

```bash
python3 docs/openwave-candidate/check_k3_rank15_cm_v4_gate.py
```

It verifies the integral Gram matrix, determinant, evenness and the four displayed intersection identities.

---

## 2. The geometric `V4` is not the old phase-D8 proxy

A nomenclature collision in the canonical research history is load-bearing here.

The old phase-D8 lattice exercise used an abstract involution labelled `sigma_A` with a block-sign action on an auxiliary decomposition. Later audit showed that this object is **not** the geometric symplectic `V4` generator and must not be used for H0a.3.

The geometric object retained by the canonical K3 construction is instead the Jacobian elliptic model of Clingher–Malmendier type, with Weierstrass form

`y^2 = x (x-A(t)) (x-B(t))`,

where `A` and `B` have degree 4, and three non-zero 2-torsion sections represented by

`(0,0)`, `(A,0)`, `(B,0)`.

The associated Mordell–Weil torsion is

`MW_tors ≅ (Z/2Z)^2`.

Translations by two independent 2-torsion sections generate the geometric symplectic

`V4 = <T_A,T_B>`.

Such translations act fiberwise over the same base coordinate `t`. Therefore the fiber divisor class is fixed:

`T_A(F)=F`, `T_B(F)=F`.

The zero section itself need not be fixed — torsion translation permutes sections — and H0a.3 requires preservation of the elliptic fibration / fiber class, not pointwise fixation of the zero section.

### H0a.3a ruling

> **Conditional on the recovered rank-15 Clingher–Malmendier Jacobian model, the actual symplectic `V4` preserves an elliptic fibration with section. H0a.3a passes.**

This resolves the earlier minimal-`V4` obstruction for the `V4` subgroup alone: the specialization has `rho=15`, not `rho=13`.

---

## 3. Donaldson reflection monodromy preserves the same fiber class

The canonical exact NS embedding used for the Donaldson analysis has

`M = U ⊕ D4(-1) ⊕ A1(-1)^5`

as a rank-11 sublattice, with a rank-4 negative-definite orthogonal complement `Mperp` containing the algebraic `(-2)` candidates for the uniform Donaldson vanishing cycle `alpha_1`.

Since the full `U=<e,f>` lies in `M`, every such candidate obeys

`F.alpha_1 = 0`.

For a `(-2)` root,

`s_alpha(v) = v + (v.alpha) alpha`,

hence

`s_alpha(F)=F`.

This is independent of which surviving `alpha_1` is ultimately selected.

### H0a.3b ruling

> **The uniform Donaldson reflection preserves the rank-15 elliptic fiber class at lattice level, independently of the surviving `alpha_1` candidate. H0a.3b passes conditionally on the recovered embedding.**

---

## 4. Full JK package at rank 15 — FAIL

The previous version of this note left the anti-symplectic / JK extension merely `OPEN`. The exact character audit now sharpens that status to a no-go at Picard rank 15.

The frozen JK target asks for

- three non-trivial symplectic `V4` involutions, each with eight fixed points;
- `tau` of type `(11,7,1)`, hence fixed locus `(g,k)=(2,2)`;
- the three `tau sigma` elements of type `(11,9,1)`, hence `(g,k)=(1,1)`.

Consequently the character on `H^2(K3)` is

`(22,0,6,6,0,0,6,0)`.

At `rho=15`, `T_X` has rank 7. The symplectic `V4` acts trivially on `T_X`, while `tau` and its three cosets act as `-I`. Subtracting the transcendental character gives

`chi_NS = (15,7,-1,-1,7,7,-1,7)`.

Fourier inversion over `(Z/2)^3` gives multiplicity

`m_tau = -2`

for the character that changes sign only under `tau`. Negative representation multiplicity is impossible.

Therefore:

> **The frozen full JK `(Z/2)^3` package cannot exist on a Picard-rank-15 K3.**

The exact public reproducer is

```bash
python3 docs/openwave-candidate/check_k3_jk_character_gate.py
```

and the full derivation is in [`K7_P2_neutrino_JK_character_obstruction.md`](K7_P2_neutrino_JK_character_obstruction.md).

The same calculation yields the sharp necessary condition

`rho >= 17`.

So the rank-15 CM model remains useful evidence for the `V4`-fiber and Donaldson sub-gates, but it is **not** a candidate for the frozen full JK compactification package.

---

## 5. Historical anti-symplectic searches — why they do not evade the obstruction

Three historical branches were checked.

### Direct CM-Weierstrass `tau`

The obvious commuting anti-symplectic involution on the CM family preserves the fibration, but acts as `+I` on all of `NS`, giving fixed rank 15 rather than the target `(11,7,1)`. Its `V4` coset and the natural Möbius base-involution variants were exhausted without recovering the target abelian package.

### Abstract 15×15 / Torelli package

The old abstract action was assigned the desired fixed-lattice types but later failed the transcendental character test. The new public calculation shows that this was not an accident of one matrix basis: the rank-15 target character itself is impossible.

### T5-prime / `T5''`

The later explicit CI(2,2,2) construction repairs the symplectic projective geometry, but records all three `tau sigma` involutions as **free**, giving Enriques quotients. That cannot realize `(11,9,1)`, which requires one elliptic curve plus one rational curve in the fixed locus.

Thus none of the three encoded rank-15 routes realizes the frozen JK package.

---

## 6. What survives and what changes

The useful rank-15 facts do survive:

- `NS=U+E7(-1)+A1(-1)^6` is an explicit high-Picard lattice;
- the CM Mordell–Weil `V4` preserves an elliptic fiber;
- the recovered Donaldson reflections fix that same fiber.

But they can no longer be promoted to a full JK realization.

The next construction target is **not** “find the missing `tau` on this rank-15 CM K3.” It is:

> **construct or identify a degree-8 K3 with `rho>=17` carrying the complete frozen JK `(Z/2)^3` action.**

For the frozen target character, the full invariant cohomology has rank 5. Because the anti-symplectic generator removes the holomorphic two-form directions, this invariant lattice is algebraic and has one positive direction. At lattice level it is therefore an indefinite rank-5 lattice, so Meyer forces a non-zero invariant isotropic class.

Thus the higher-Picard pivot is not arbitrary: if the correct full group exists, a common invariant genus-one fiber class is structurally expected. Nef/effective and section checks still have to be performed on the actual model.

---

## 7. Updated local gate table

| Gate | Claim | Status |
| --- | --- | --- |
| H0a.1 | symplectic `V4` forces enough Picard rank for genus-one fibration | **PASS under V4 assumption** |
| H0a.2 | an elliptic fibration with section exists abstractly | **PASS under V4 assumption** |
| H0a.3a | rank-15 CM symplectic `V4` preserves a selected elliptic fiber | **CONDITIONAL PASS** |
| H0a.3b | recovered Donaldson reflection preserves that fiber class | **CONDITIONAL PASS** |
| H0a.3c-15 | frozen full JK package exists at `rho=15` | **FAIL — character obstruction** |
| H0a.3c-T5 | historical `T5''` realizes target anti-symplectic cosets | **FAIL — free versus required `(g,k)=(1,1)`** |
| H0a.3d | full JK package on a higher-Picard degree-8 K3 | **OPEN — `rho>=17` necessary** |
| H0b | global K7 lies in a controlled M/heterotic duality class | **OPEN** |
| H1+ | heterotic bundle, chirality, `nu_R`, neutrino mass operator | **NOT REACHED** |

No neutrino-mass target or preferred ordering entered this calculation.