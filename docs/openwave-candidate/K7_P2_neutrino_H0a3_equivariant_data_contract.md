# K7-P2 Candidate A — H0a.3 equivariant elliptic data contract

**Status:** `H0a.3 HOLD — exact NS/action data required`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent gate:** [`K7_P2_neutrino_H0_fiber_lattice_gate.md`](K7_P2_neutrino_H0_fiber_lattice_gate.md)

This note specifies the exact mathematical data needed to close the remaining fiber-level gate of the provisional heterotic-dual route.

H0a.1 and H0a.2 are already conditionally closed under the K7 symplectic-`V4` assumption:

`V4 symplectic -> rho(X)>=13 -> U embeds in NS(X) -> elliptic fibration with section exists`.

The remaining question is stronger:

> Can an elliptic fibration be chosen compatibly with the actual K7 `V4` / monodromy / global gluing data?

At minimal `rho=13` the answer is no. A higher-Picard specialization and an explicit invariant isotropic class are required.

---

## 1. Existing K7 lattice certificates do not yet close H0a.3

`Arithmon/K7-Lean:GIFT/Foundations/G2TCSLatticeCertificate.lean` contains an explicit copy of the `3U` block of the ambient K3 lattice

`Lambda_K3 = 3U + 2 E8(-1)`

and the degree-8 vectors

- `vPlus = 4 e1 + f1`,
- `vMinus = 4 e2 + f2`,
- `w = 4 e3 + f3`,

with squares 8, pairwise orthogonality in the relevant slots, primitive embedding checks, and a cyclic hyperkähler matching isometry.

This is valuable matching data, but it is **ambient cohomology data**. It does not establish that a chosen copy of `U` is contained in the Néron–Severi lattice of the actual K7 fiber.

The distinction is load-bearing:

`U subset H^2(K3,Z)`

does not imply

`U subset NS(X)`.

The latter is a Hodge / algebraic condition and is what an elliptic fibration with section requires.

Likewise, the `Z2^3` sign table in the same Lean module is encoded on a six-dimensional representation used for the determinant parity test. It is not an explicit pair of integral action matrices on `NS(X)`.

Therefore the existing Lean `3U` certificate must **not** be cited as closure of H0a.3.

---

## 2. A possible lead that is not yet public evidence

`G2DonaldsonLinkCohomology.lean` and the K7-Lean changelog mention a private exact cross-check on a **rank-15 polarisation lattice**.

That rank is interesting because `rho>=14` is necessary for a `V4`-invariant isotropic class to become possible. However, the public artifact currently exposes neither

- the Gram matrix of that rank-15 lattice,
- its identification with `NS(X)` for the K7 degree-8 fiber,
- nor the `V4` action on it.

It is therefore recorded only as a retrieval lead. It earns no H0a.3 credit until those data are explicit and independently checkable.

---

## 3. Minimal exact input package

To close H0a.3, freeze one concrete K3 fiber `X` and publish the following.

### D1 — Néron–Severi lattice

An integral basis of `NS(X)` and its Gram matrix

`Q in Mat_r(Z)`, `r = rho(X)`.

Required checks:

- `Q` even;
- signature `(1,r-1)`;
- degree-8 polarization `h` is represented explicitly with `h^T Q h = 8`;
- the declared lattice embeds primitively in the K3 lattice or is otherwise identified by a theorem-grade construction.

### D2 — actual `V4` action on `NS(X)`

Integral matrices `S1,S2 in GL(r,Z)` representing the two generators, with

- `S1^2 = I`, `S2^2 = I`;
- `S1 S2 = S2 S1`;
- `Si^T Q Si = Q`;
- the action agrees with the geometric automorphisms used in the JK fixed-locus screen, rather than merely an abstract isometric copy.

### D3 — monodromy / matching action

Give the action on the same lattice basis of every extra map that the elliptic fiber must survive, in particular the relevant Picard–Lefschetz reflection / hyperkähler matching map used by the selected global route.

### D4 — effective / nef chamber data

Enough `(-2)`-root / ample-cone information to decide whether a primitive isotropic class can be moved to, or already lies in, the nef cone without destroying the required equivariance.

---

## 4. Exact H0a.3 computation

Once `Q,S1,S2` are frozen, the gate is finite and target-free.

### Step E1 — compute the invariant lattice over `Z`

Compute

`K = NS(X)^V4 = ker_Z(S1-I) intersect ker_Z(S2-I)`.

This must be an **integral** kernel computation, e.g. via Smith/Hermite normal form, not merely a floating-point eigenspace.

Record a basis matrix `B` for `K` and the restricted Gram matrix

`Q_K = B^T Q B`.

Sanity check against the character result:

`rk K = rho(X) - 12`

for the symplectic `V4` action used in the current gate.

### Step E2 — search for a primitive invariant isotropic class

Solve exactly

`x^T Q_K x = 0`

for a nonzero primitive integer vector `x`.

Lift

`F = B x in NS(X)`.

Required checks:

- `F != 0`;
- `gcd(F_i)=1` in the chosen primitive basis;
- `F^2=0` exactly;
- `S1 F = F`, `S2 F = F`.

If no such `F` exists, the `V4`-equivariant elliptic route fails for this K3 specialization.

### Step E3 — nef/effective representative

Show that the isotropic class defines a fibration. Either

- prove `F` is nef directly against the effective `(-2)` roots; or
- give an explicit Weyl reflection sequence to a primitive nef isotropic representative and verify that the required group/matching compatibility survives.

### Step E4 — section for the selected fiber class

H0a.2 proves that *some* Jacobian elliptic fibration exists on `X`; it does not automatically say that the particular invariant `F` found in E2 has a section.

For this `F`, exhibit a class `S` such that, after choosing the effective representative,

- `F . S = 1`;
- a section representative exists (for a K3 section one expects `S^2=-2`).

Equivalently, exhibit the corresponding primitive `U` associated with this specific fibration.

The section itself need not be pointwise fixed by `V4`; a controlled orbit or torsion-translation action is acceptable if it is compatible with the intended quotient/duality construction. The **fiber class** must be invariant for the fibration to be preserved.

### Step E5 — global matching check

Verify that the selected matching / monodromy data preserve the fiber structure required by the proposed fiberwise duality. This is the bridge from H0a.3 to H0b; it must not be inferred from the existence of `F` alone.

---

## 5. Sharp falsifiers

H0a.3 fails for the selected K3 realization if any of the following occurs:

1. the published `NS(X)` has `rho=13`; then `rk NS(X)^V4=1` and no invariant isotropic class can exist;
2. `rho>=14` but the exact invariant lattice `Q_K` represents no nonzero primitive zero;
3. an invariant isotropic class exists but every such class is incompatible with the required nef chamber / effective geometry;
4. a suitable elliptic fibration exists but the selected JK / Picard–Lefschetz / matching action does not preserve the required fiber structure;
5. the `V4` matrices used in the lattice calculation cannot be identified with the geometric `V4` used in the K7 fixed-locus count.

A failure is recorded; the lattice or action may not be changed after inspection simply to recover a desired heterotic dictionary under the same candidate identifier.

---

## 6. High-Picard construction benchmark

Garbagnati–Sarti give an explicit family of smooth complete intersections of three diagonal quadrics in `P5` with a symplectic `(Z/2Z)^4` action generated by even sign changes. For algebraic members the minimal Picard number for the full group is 16.

This is a useful existence benchmark for degree-8 high-symmetry K3 surfaces, and it is geometrically close to the K7 `CI(2,2,2)` setup. It is **not** yet identified with the K7 fiber.

A valid use of this benchmark would be:

1. show the actual K7 quadric net lies in, or is explicitly specialized to, the relevant family;
2. identify the K7 `V4` subgroup inside the full sign-change group;
3. compute `NS(X)^V4` and an invariant isotropic fiber class there;
4. check compatibility with the rest of the K7 gluing data.

Skipping step 1 would merely replace one unproved physical identification by another.

Reference: A. Garbagnati, A. Sarti, *Kummer surfaces and K3 surfaces with (Z/2Z)^4 symplectic action*, arXiv:1305.3514.

---

## 7. Promotion rule

H0a.3 becomes `PASS` only when the repository contains, from a clean checkout:

- the exact `NS(X)` Gram matrix;
- exact `V4` action matrices;
- an exact primitive invariant nef isotropic class `F`;
- a section / `U` certificate for that particular fibration;
- the relevant matching/monodromy compatibility checks;
- a reproducer that uses no neutrino-mass target data.

Until then the scientifically correct status is

> **elliptic-with-section exists abstractly; K7-equivariant elliptic structure remains unproved.**
