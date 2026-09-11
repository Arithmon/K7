# K7-P2 Candidate A — H0 fiber-lattice gate

**Status:** `H0a CONDITIONAL PASS / H0b GLOBAL DUALITY OPEN`  
**Date:** 2026-09-11  
**Target-value exposure:** none.  
**K7 baseline:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`

This note sharpens the first gate of the provisional heterotic-dual route. It does not produce a neutrino observable.

The question is split into two logically distinct parts:

- **H0a — fiber geometry:** does the projective K3 fiber used by K7 admit a genus-one / elliptic fibration?
- **H0b — global compactification:** is the *global K7 construction* in a class for which the fiberwise M-theory/heterotic duality used in the TCS literature is actually established or independently derived?

The first question has a strong conditional answer from the existing K7 `V4` screen. The second remains open.

---

## 1. Frozen assumptions used by H0a

H0a uses only the following pre-existing K7 statements.

**A1.** The K3 fiber is a smooth projective degree-8 K3, represented in the analytic program as a `CI(2,2,2) ⊂ P5`.

**A2.** The same K3 carries the Phase-1 symplectic action

`V4 = (Z/2Z)^2 = <s1,s2>`.

The K7 JK audit records 24 raw fixed points across the three nontrivial involutions, i.e. the expected 8 fixed points per symplectic involution.

If A2 is only a screen on a family and not an automorphism action on the final chosen K3, the conclusion below does not transfer automatically. That distinction is now load-bearing.

---

## 2. Invariant / coinvariant rank from Lefschetz

A symplectic involution on a complex K3 has 8 isolated fixed points. The topological Lefschetz formula gives

`8 = tr(H^0) + tr(H^2) + tr(H^4) = 1 + tr(H^2) + 1`,

so every nontrivial involution in `V4` has

`tr(g | H^2) = 6`.

For a finite group, the dimension of the invariant subspace is the average of the character:

`rk H^2(X,Z)^V4 = (1/4) [22 + 6 + 6 + 6] = 10`.

Hence the coinvariant lattice

`Omega_V4 := (H^2(X,Z)^V4)^perp`

has

`rk Omega_V4 = 22 - 10 = 12`.

This agrees with the explicit lattice calculation of Garbagnati–Sarti. They give for `G=(Z/2Z)^2`

- `rk(Omega_G)=12`,
- `|disc(Omega_G)|=2^10`,
- `A_Omega ≅ (Z/2Z)^6 ⊕ (Z/4Z)^2`.

Reference: A. Garbagnati, A. Sarti, *Elliptic fibrations and symplectic automorphisms on K3 surfaces*, Commun. Algebra 37 (2009), arXiv:0801.3992.

---

## 3. Picard-rank lower bound

For a projective K3 with a symplectic finite group `G`, the coinvariant lattice `Omega_G` is contained in the Néron–Severi lattice `NS(X)`.

Since `Omega_V4` is negative definite of rank 12 and a projective K3 also has a positive ample class independent of it,

`rho(X) = rk NS(X) >= 1 + rk Omega_V4 = 13`.

This is much stronger than the generic degree-8 `CI(2,2,2)` Picard rank.

### Reproducible arithmetic

Run from repository root:

```bash
python3 docs/openwave-candidate/check_k3_v4_genus_one_gate.py
```

The script only reproduces the character/rank arithmetic. The fixed-point and lattice theorems remain cited mathematical inputs.

---

## 4. Genus-one fibration follows from the Picard bound

For a projective K3, `NS(X)` has signature `(1, rho-1)`. With `rho >= 13`, it is an indefinite integral lattice of rank at least 5.

By Meyer's theorem, such a lattice represents zero: there is a nonzero integral divisor class `F` with

`F^2 = 0`.

For a K3, after the standard effective/Weyl-chamber reduction one obtains a primitive nef isotropic class; its complete linear system defines a genus-one fibration over `P1`.

Equivalent standard formulation: a K3 admits a genus-one fibration iff `NS(X)` contains a nonzero isotropic class; in particular every projective K3 with `rho >= 5` admits one.

References:

- I. Piatetski-Shapiro, I. Shafarevich, *A Torelli theorem for algebraic surfaces of type K3*, 1971.
- M. Schütt, T. Shioda, *Elliptic Surfaces*, Algebraic Geometry in East Asia (2010), §12.9.
- A. Garbagnati, A. Sarti, arXiv:0801.3992, for the `V4` lattice input.

### H0a ruling

> **Conditional on A1+A2 referring to the same projective K3 fiber, H0a passes: the K3 must admit a genus-one fibration.**

No explicit Weierstrass equation is needed to establish existence.

---

## 5. What H0a does *not* prove

### 5.1 A section is not automatic

A genus-one fibration need not have a section. A **Jacobian elliptic fibration** corresponds lattice-theoretically to a primitive embedding

`U -> NS(X)`

of the hyperbolic plane.

The rank argument above guarantees an isotropic class, not divisibility one and not a section.

Therefore introduce a sub-gate:

> **H0a.2:** determine the actual `NS(X)` lattice / overlattice selected by the K7 degree-8 polarization and test for a primitive `U` embedding.

Garbagnati–Sarti classify the minimal-Picard lattices with a symplectic `V4`. For a primitive positive class `L` with `L^2=8`, `NS(X)` is built from `<L> ⊕ Omega_V4`, with possible finite-index overlattices. This gives a finite lattice problem once K7 fixes which gluing class applies.

### 5.2 Compatibility with the K7 matching / orbifold data is not automatic

The isotropic divisor provided abstractly need not be invariant under every K7 automorphism or compatible with the hyperkähler rotation / global gluing data.

Existence of *some* genus-one fibration is therefore not yet the fiberwise duality datum required by the proposed physical map.

---

## 6. Critical inconsistency exposed: `Picard-rank-1` versus symplectic `V4`

The current K7 v3.5 foundations simultaneously state:

1. Phase 1 uses a symplectic `V4` action on the degree-8 `CI(2,2,2)` K3 fiber; and
2. the deferred explicit polynomial `Z2^3` model is described as living on a **Picard-rank-1, eta^2=8 K3**.

These cannot describe the same projective K3.

From the previous sections,

`symplectic V4  =>  Omega_V4 ⊂ NS(X), rk(Omega_V4)=12  =>  rho(X)>=13`.

Therefore

> **A projective Picard-rank-1 K3 cannot carry the required symplectic `V4` action.**

The degree-8 polarization `eta^2=8` is not itself the problem: a special degree-8 K3 may have high Picard rank. The conflicting adjective is `Picard-rank-1`.

### Required correction before global promotion

The global JK program must choose one consistent statement, for example:

- construct a **special degree-8 K3 with `rho>=13`** carrying the required `V4` / `Z2^3` lattice action; or
- abandon the claim that the same K3 carries the symplectic `V4` action.

The second option would reopen the Betti / fixed-locus route and therefore cannot be treated as a cosmetic edit.

This contradiction is a **critical K7 structural hold**, independent of OpenWave.

---

## 7. H0b — global duality is still open

The explicit Braun–Schäfer-Nameki M/heterotic construction is established for appropriate **K3-fibered TCS G2 manifolds**, and their tractable explicit class uses elliptically fibered K3 fibers.

Current K7 v3.5 says instead:

- `(b2,b3)=(21,77)` is absent from the catalogued TCS examples;
- orthogonal TCS is excluded by the cited parity condition;
- non-orthogonal / extra-twisted TCS remain open;
- the **leading global candidate is the Joyce–Karigiannis `T3 × K3 / Z2^3` route**, not an established TCS realization.

Therefore one may not infer

`K7 K3 fiber is genus-one -> K7 has the Schoen heterotic dual`.

That implication would be another local-to-global jump.

### H0b pass options

At least one of the following would be needed:

1. **TCS option:** construct an actual K7 non-orthogonal / extra-twisted TCS realization with the required compatible elliptic K3 data, then apply the established fiberwise duality.
2. **JK option:** derive an M/heterotic dual dictionary directly for the specific JK `T3 × K3 / Z2^3` resolution used by K7 and show how geometry, bundle data and orbifold action map.
3. **Independent duality option:** provide another controlled compactification dictionary that derives the 4D chiral spectrum without importing the TCS/Schoen result.

Until one closes, the Schoen `X_(19,19)` discussion remains a **conditional benchmark**, not K7 field content.

---

## 8. Updated gate table

| Gate | Statement | Status |
| --- | --- | --- |
| H0a | K7 projective K3 with genuine symplectic `V4` admits genus-one fibration | **CONDITIONAL PASS** |
| H0a.1 | `rho(X)>=13` from `V4` | **PASS under A2** |
| H0a.2 | fibration has section / `U -> NS(X)` | **OPEN** |
| H0a.3 | fibration compatible with K7 automorphisms / matching | **OPEN** |
| H0-struct | Picard-rank-1 description compatible with symplectic `V4` | **FAIL — contradiction** |
| H0b | global K7 lies in an established M/heterotic duality class | **OPEN** |
| H1+ | Schoen bundle / chirality / neutrino operator | **NOT REACHED** |

## 9. Immediate next computation

The next useful calculation is **not** a neutrino mass and not yet a Schoen bundle.

It is:

> determine the actual degree-8 `V4`-polarized Néron–Severi lattice of the K7 K3 fiber, including the allowed overlattice class, then test primitive `U` embeddings and compatibility with the required automorphism/gluing action.

That calculation closes or kills H0a.2 without target leakage.
