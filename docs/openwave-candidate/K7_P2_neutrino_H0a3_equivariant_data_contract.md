# K7-P2 Candidate A — H0a.3 equivariant elliptic data contract

**Status:** `PARTIAL PASS — rank-15 CM V4 + Donaldson fiber preservation closed conditionally; full JK/global matching open`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent gate:** [`K7_P2_neutrino_H0_fiber_lattice_gate.md`](K7_P2_neutrino_H0_fiber_lattice_gate.md)  
**Rank-15 resolution:** [`K7_P2_neutrino_rank15_CM_V4_gate.md`](K7_P2_neutrino_rank15_CM_V4_gate.md)

This file began as the exact data contract for H0a.3. The previously private rank-15 lattice record has now been recovered and distilled into a public target-free reproducer. The contract is therefore no longer wholly open: D1 and the fiber-preservation parts of D2/D3 are conditionally closed.

The remaining question is global:

> Does the same rank-15 elliptic K3, with its actual geometric symplectic `V4`, extend through the selected anti-symplectic / Joyce–Karigiannis / matching data in a way that supports a controlled M-theory/heterotic dictionary?

No neutrino mass, ordering, or preferred experimental value is used here.

---

## 1. Recovered exact lattice package

The canonical K3 work uses

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

### D1 ruling — Néron–Severi lattice

**CONDITIONAL PASS.** The rank-15 Gram is now explicit and target-free reproducible. What remains conditional is the framework-level decision that this recovered rank-15 model is the K3 fiber adopted by the final global K7 construction.

---

## 2. D2 — use the geometric `V4`, not the old sign-matrix proxy

The historical private workspace used the name `sigma_A` for two distinct objects. Later reconciliation showed that the phase-D8 block-sign involution is **not** the genuine symplectic `V4` generator and must not be used for H0a.3.

The retained geometric model is instead a Jacobian elliptic K3 of Clingher–Malmendier type with Weierstrass form

`y^2 = x (x-A(t)) (x-B(t))`

and Mordell–Weil 2-torsion

`MW_tors ≅ (Z/2Z)^2`.

Translations by two independent 2-torsion sections generate the actual symplectic `V4`. Such translations act fiberwise over the same base and therefore preserve the fiber class `F`.

The section is allowed to move in its Mordell–Weil orbit; H0a.3 requires the **fibration/fiber class** to be preserved, not pointwise fixation of the zero section.

### D2 ruling — actual `V4`

**CONDITIONAL PASS for fiber preservation.** The geometric mechanism fixes `F` by construction. Full integral matrices on the chosen NS basis would still be useful for a stand-alone machine certificate, but they are no longer logically required to establish that Mordell–Weil translations preserve the fibration.

The old phase-D8 sign matrices are explicitly excluded from this ruling.

References for the general geometry:

- A. Garbagnati, *Elliptic K3 surfaces with abelian and dihedral groups of symplectic automorphisms*, arXiv:0904.1519.
- A. Clingher, A. Malmendier, *On Néron–Severi lattices of Jacobian elliptic K3 surfaces*, arXiv:2109.01929.

---

## 3. D3 — Donaldson Picard–Lefschetz monodromy

The recovered NS embedding contains

`M = U ⊕ D4(-1) ⊕ A1(-1)^5`

and a rank-4 negative-definite orthogonal complement `Mperp`. The surviving algebraic `alpha_1` candidates all lie in `Mperp`.

Since the full `U=<e,f>` lies in `M`, every such candidate obeys

`F.alpha_1 = 0`.

For a `(-2)` root,

`s_alpha(v)=v+(v.alpha)alpha`,

hence

`s_alpha(F)=F`.

This is independent of which surviving `alpha_1` is ultimately selected.

### D3 ruling — uniform reflection

**CONDITIONAL PASS at lattice level.** The unresolved root selection cannot destroy the elliptic fiber class.

This does **not** by itself prove the global hyperkähler / JK matching needed by the proposed duality.

---

## 4. D4 — nef/effective and section data

For the abstract contract, D4 asked for a primitive nef isotropic class plus a section. In the rank-15 Jacobian model these data are supplied geometrically by the selected elliptic fibration:

- `F` is the fiber divisor class;
- `S` is a section class with `F.S=1` and `S^2=-2`;
- the public arithmetic reproducer verifies the lattice identities.

### D4 ruling

**CONDITIONAL PASS inside the recovered Jacobian model.** A separate root-by-root nef-cone search is unnecessary once the fibration itself is part of the geometric construction.

If the final K7 fiber is changed away from this model, D4 reopens.

---

## 5. What remains open — H0a.3c

The following is **not** closed by the rank-15 recovery:

1. an actual anti-symplectic / JK involution on the **same** rank-15 K3, with the fixed-locus data needed by the selected global compact route;
2. compatibility of that map with the geometric Mordell–Weil `V4`;
3. compatibility of the full global gluing / resolution with the preserved elliptic fiber;
4. a theorem-grade bridge from that compact K7 construction to a controlled heterotic dual compactification.

Later canonical audits already showed that one attempted historical `Z2^3` character packaging cannot simply be imported onto the smooth rank-15 model. Therefore the existence of the separate `V4` and anti-symplectic lattice ingredients is not counted as proof that the full package coexists geometrically.

This is now the sharp boundary:

> **Fiber-level equivariance has a viable rank-15 realization; full JK/global equivariance remains unproved.**

---

## 6. Superseded requirements from the original contract

The original H0a.3 contract demanded:

- D1: exact `NS(X)` Gram;
- D2: actual `V4` action;
- D3: monodromy/matching action;
- D4: nef/effective section data.

After the rank-15 recovery:

| Item | Status | Evidence |
| --- | --- | --- |
| D1 exact `NS` | **conditional pass** | `U+E7(-1)+A1(-1)^6`, determinant `2^7`, public reproducer |
| D2 symplectic `V4` preserves fiber | **conditional pass** | geometric translations by independent 2-torsion sections |
| D3 Donaldson reflection preserves `F` | **conditional pass** | `alpha_1 in Mperp`, `U subset M`, hence `F.alpha_1=0` |
| D4 selected fiber has section | **conditional pass** | Jacobian fibration + exact `F,S` intersection data |
| Full anti-symplectic / JK / global matching | **OPEN** | must be constructed on the same model |

---

## 7. Sharp falsifiers from here

The rank-15 route fails if any of the following is established:

1. the final K7 K3 fiber is not the recovered `(15,7,1)` Jacobian model or an explicitly equivalent specialization;
2. the geometric `V4` used in the K7 fixed-locus/global construction is not the Mordell–Weil translation group preserving this fibration;
3. no compatible anti-symplectic / JK involution exists on the same K3 with the required fixed-locus data;
4. the required global matching sends the elliptic fiber out of the structure needed for the proposed duality;
5. the only way to recover the global package is to change the lattice/action after inspecting a desired neutrino result.

A failure is recorded and the candidate is not repaired by target-driven model switching.

---

## 8. Next gate

Do **not** compute a neutrino mass yet.

The next constructive task is now:

> build or recover the anti-symplectic / JK action on the same rank-15 Jacobian K3, reconcile it with the true Mordell–Weil `V4`, and test whether the global K7 matching preserves the elliptic fiber.

Only after that can H0b and the heterotic bundle / chiral spectrum gates be addressed.
