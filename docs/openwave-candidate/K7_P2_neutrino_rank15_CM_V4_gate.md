# K7-P2 Candidate A — rank-15 Clingher–Malmendier fiber gate

**Status:** `H0a.3a V4-FIBER CONDITIONAL PASS / H0a.3b DONALDSON REFLECTION CONDITIONAL PASS / H0a.3c FULL JK-GLOBAL MATCHING OPEN`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent gate:** [`K7_P2_neutrino_H0a3_equivariant_data_contract.md`](K7_P2_neutrino_H0a3_equivariant_data_contract.md)

This note records the recovery of the rank-15 K3 lattice that had previously appeared in the public K7-Lean changelog only as a private cross-check. It closes substantially more of H0a.3, but it does **not** close the global Joyce–Karigiannis / M-theory-to-heterotic dictionary.

The recovered canonical research record is from `gift-framework/private@8a8d4a4c05225b97c0165b73f175f1179d593a99`. Because that workspace is not itself a public dependency of this dossier, the arithmetic used below is reproduced here from scratch and every geometric identification remains explicitly conditional until promoted to a public source artifact.

---

## 1. Recovered rank-15 Néron–Severi lattice

The exact lattice used in the canonical K3 work is

`NS(X) = U ⊕ E7(-1) ⊕ A1(-1)^6`.

It has

- rank `15`;
- determinant `2^7` in absolute value;
- signature `(1,14)`;
- the 2-elementary Nikulin type `(r,a,delta)=(15,7,1)`.

This is the lattice called the rank-15 polarisation lattice in the later Donaldson-monodromy checks.

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

Thus the rank-15 lattice contains, in its actual algebraic `NS(X)` rather than only in ambient `H^2`, both a primitive hyperbolic plane and an explicit degree-8 polarization.

The dependency-free reproducer is

```bash
python3 docs/openwave-candidate/check_k3_rank15_cm_v4_gate.py
```

It verifies the integral Gram matrix, determinant, evenness and the four displayed intersection identities.

---

## 2. The geometric `V4` is not the old phase-D8 proxy

A nomenclature collision in the canonical research history is load-bearing here.

The old phase-D8 lattice exercise used an abstract involution labelled `sigma_A` with a block-sign action on an auxiliary decomposition. Later audit showed that this object is **not** the geometric symplectic involution used by the K3 `V4`: its coinvariant contains roots, whereas a symplectic K3 involution has the standard root-free Nikulin coinvariant.

Therefore the old `phase_d8` sign matrices must not be used to certify H0a.3.

The geometric object retained by the canonical K3 construction is instead the Jacobian elliptic model of Clingher–Malmendier type, with Weierstrass form

`y^2 = x (x-A(t)) (x-B(t))`,

where `A` and `B` have degree 4, and three non-zero 2-torsion sections represented by

`(0,0)`, `(A,0)`, `(B,0)`.

The associated Mordell–Weil torsion is

`MW_tors ≅ (Z/2Z)^2`.

Translations by two independent 2-torsion sections generate the geometric symplectic

`V4 = <T_A,T_B>`.

This is consistent with the general fact that translation by torsion sections preserves an elliptic fibration and gives symplectic automorphisms on a K3 surface. See A. Garbagnati, *Elliptic K3 surfaces with abelian and dihedral groups of symplectic automorphisms*, arXiv:0904.1519, and A. Clingher–A. Malmendier, *On Néron–Severi lattices of Jacobian elliptic K3 surfaces*, arXiv:2109.01929.

### Consequence

The translations act fiberwise over the same base coordinate `t`. Therefore the fiber divisor class is fixed:

`T_A(F)=F`, `T_B(F)=F`.

The zero section itself need not be fixed — torsion translation permutes sections — and H0a.3 never required pointwise fixation of a distinguished section. It requires preservation of the elliptic fibration / fiber class.

### H0a.3a ruling

> **Conditional on adopting the recovered rank-15 Clingher–Malmendier Jacobian model as the K7 K3 fiber, the actual symplectic `V4` preserves an elliptic fibration with section. H0a.3a passes.**

This resolves the earlier minimal-rank obstruction: the relevant specialization has `rho=15`, not `rho=13` and certainly not Picard rank 1.

---

## 3. Donaldson reflection monodromy preserves the same fiber class

The canonical exact NS embedding used for the Donaldson analysis has

`M = U ⊕ D4(-1) ⊕ A1(-1)^5`

as the rank-11 invariant sublattice, with a rank-4 negative-definite orthogonal complement `Mperp` containing the algebraic `(-2)` candidates for the uniform Donaldson vanishing cycle `alpha_1`.

The crucial point for the elliptic fiber is independent of which candidate is eventually selected:

`Mperp` is orthogonal to `M`, and the full `U=<e,f>` lies in `M`.

Hence for every candidate root `alpha in Mperp`,

`F.alpha = e.alpha = 0`.

For a `(-2)` root, the Picard–Lefschetz reflection is

`s_alpha(v) = v + (v.alpha) alpha`.

Therefore

`s_alpha(F)=F`

for **every** current `alpha_1` candidate.

This does not identify the physically correct `alpha_1`; it shows that the unresolved choice cannot spoil the fiber class at lattice level.

### H0a.3b ruling

> **The uniform Donaldson reflection monodromy preserves the rank-15 elliptic fiber class at lattice level, independently of the surviving `alpha_1` candidate. H0a.3b passes conditionally on the recovered NS embedding.**

---

## 4. What is still open

This result does **not** resurrect the historical full `Z2^3` packaging automatically.

Later canonical audits separated the true symplectic Mordell–Weil `V4` from old abstract lattice proxies and found obstructions to one attempted realization of the complete target character table on the rank-15 K3. In particular, one must not infer that a desired anti-symplectic `tau` and all historical fixed-locus data coexist with the recovered `V4` merely because their separate lattice invariants exist.

The remaining fiber/global gate is therefore:

1. give the actual anti-symplectic / JK map used in the selected compact route on the same rank-15 model;
2. prove it is geometrically realized and compatible with the required fixed-locus data;
3. show that the global K7 matching / resolution preserves the elliptic datum needed by the proposed M/heterotic dictionary;
4. only then invoke a controlled heterotic dual compactification and derive bundle / chiral field content.

The existing TCS `3U` matching certificate remains useful but cannot by itself substitute for this global identification.

---

## 5. Picard-rank correction

If the rank-15 Clingher–Malmendier route is retained as the K7 fiber model, the public phrase

`Picard-rank-1, eta^2=8 K3`

cannot describe the same K3 and should be retired or explicitly scoped to a different model/screen.

The consistent rank-15 statement is instead

`NS(X) ≅ U ⊕ E7(-1) ⊕ A1(-1)^6`,

with a degree-8 class `h=4e+f`.

This resolves the previous `Picard-rank-1` versus symplectic-`V4` contradiction at fiber level, but adopting this correction in the framework mainline requires its own source-level reconciliation.

---

## 6. Updated local gate table

| Gate | Claim | Status |
| --- | --- | --- |
| H0a.1 | symplectic `V4` forces enough Picard rank for genus-one fibration | **PASS under V4 assumption** |
| H0a.2 | an elliptic fibration with section exists | **PASS under V4 assumption** |
| H0a.3a | actual symplectic `V4` preserves a selected elliptic fiber | **CONDITIONAL PASS on rank-15 CM model** |
| H0a.3b | uniform Donaldson reflection preserves that fiber class | **CONDITIONAL PASS at lattice level** |
| H0a.3c | full JK `Z2^3` / anti-symplectic / global matching package preserves the required elliptic datum | **OPEN** |
| H0b | global K7 lies in a controlled M/heterotic duality class | **OPEN** |
| H1+ | heterotic bundle, chirality, `nu_R`, neutrino mass operator | **NOT REACHED** |

No neutrino-mass target or preferred ordering entered this calculation.
