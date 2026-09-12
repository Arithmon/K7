# K7-P2 Candidate A — H0 fiber-lattice gate

**Status:** `H0a.1 + H0a.2 CONDITIONAL PASS / H0a.3 HOLD / H0b GLOBAL DUALITY OPEN`  
**Opened:** 2026-09-11  
**Updated:** 2026-09-12  
**Target-value exposure:** none.  
**K7 baseline:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`

This note sharpens the first gate of the provisional heterotic-dual route. It does not produce a neutrino observable.

The question is split into logically distinct parts:

- **H0a.1 — fiber lattice:** does the projective K3 fiber used by K7 have enough Picard lattice to force a genus-one fibration?
- **H0a.2 — Jacobian upgrade:** does its Néron–Severi lattice contain a hyperbolic plane `U`, hence an elliptic fibration with section?
- **H0a.3 — equivariance:** can such a fibration be chosen compatibly with the K7 `V4` / matching / orbifold data?
- **H0b — global compactification:** is the *global K7 construction* in a class for which the fiberwise M-theory/heterotic duality is actually established or independently derived?

Under the current K7 Phase-1 symplectic-`V4` assumption, H0a.1 and H0a.2 pass. H0a.3 does not follow; at the minimal Picard rank it is actually obstructed.

---

## 1. Frozen assumptions used by H0a

H0a uses only the following pre-existing K7 statements.

**A1.** The K3 fiber is a smooth projective degree-8 K3, represented in the analytic program as a `CI(2,2,2) ⊂ P5`.

**A2.** The same K3 carries the Phase-1 symplectic action

`V4 = (Z/2Z)^2 = <s1,s2>`.

The K7 JK audit records 24 raw fixed points across the three nontrivial involutions, i.e. the expected 8 fixed points per symplectic involution.

If A2 is only a screen on a family and not an automorphism action on the final chosen K3, the conclusions below do not transfer automatically. That distinction remains load-bearing.

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

This agrees with the explicit lattice calculation of Garbagnati–Sarti. For `G=(Z/2Z)^2` they give

- `rk(Omega_G)=12`,
- `|disc(Omega_G)|=2^10`,
- `A_Omega ≅ (Z/2Z)^6 ⊕ (Z/4Z)^2`.

Reference: A. Garbagnati, A. Sarti, *Elliptic fibrations and symplectic automorphisms on K3 surfaces*, Commun. Algebra 37 (2009), arXiv:0801.3992.

---

## 3. Picard-rank lower bound

For a projective K3 with a symplectic finite group `G`, the coinvariant lattice `Omega_G` is contained in the Néron–Severi lattice `NS(X)`; equivalently the symplectic action is trivial on the transcendental lattice.

Since `Omega_V4` is negative definite of rank 12 and a projective K3 has an invariant positive ample class independent of it,

`rho(X) = rk NS(X) >= 1 + rk Omega_V4 = 13`.

This is much stronger than the generic degree-8 `CI(2,2,2)` Picard rank.

### Reproducible arithmetic

Run from repository root:

```bash
python3 docs/openwave-candidate/check_k3_v4_genus_one_gate.py
```

The script reproduces the character/rank arithmetic and the numerical inequalities entering the lattice criteria below. The fixed-point, symplectic-action and Nikulin theorems remain cited mathematical inputs.

---

## 4. H0a.1 — genus-one fibration

For a projective K3, `NS(X)` has signature `(1, rho-1)`. With `rho >= 13`, it is an indefinite integral lattice of rank at least 5.

By Meyer's theorem such a lattice represents zero: there is a nonzero integral divisor class `F` with

`F^2 = 0`.

For a K3, after the standard effective/Weyl-chamber reduction one obtains a primitive nef isotropic class; its complete linear system defines a genus-one fibration over `P1`.

Equivalent standard formulation: a K3 admits a genus-one fibration iff `NS(X)` contains a nonzero isotropic class; in particular every projective K3 with `rho >= 5` admits one.

Reference: M. Schütt, T. Shioda, *Elliptic Surfaces*, Adv. Stud. Pure Math. 60 (2010), Proposition 12.8 and Corollary 12.9, arXiv:0907.0298.

### H0a.1 ruling

> **Conditional on A1+A2 referring to the same projective K3 fiber, H0a.1 passes: the K3 must admit a genus-one fibration.**

---

## 5. H0a.2 — a section is also forced at `rho >= 13`

The previous version of this note left a section as an open finite-lattice problem. A stronger general theorem closes it.

Schütt–Shioda, following Nikulin, state:

> Every complex K3 surface of Picard number at least 13 admits an elliptic fibration with section.

The lattice criterion is the following. For an indefinite even integral lattice `L`, if

`rk(L) >= length(A_L) + 3`,

then the hyperbolic plane `U` embeds in `L`.

For a complex K3,

`length(A_NS) <= rk(T_X) = 22 - rho(X)`.

At the minimal rank forced by `V4`, `rho=13`, therefore

- `rk(NS)=13`,
- `rk(T_X)=9`,
- `length(A_NS) <= 9`,
- `13 >= 9 + 3`.

Hence

`U -> NS(X)`

and the K3 admits a Jacobian elliptic fibration, i.e. an elliptic fibration with section.

Reference: Schütt–Shioda, Lemma 12.22, citing Nikulin, Corollary 1.13.5.

### H0a.2 ruling

> **Conditional on A1+A2, H0a.2 passes. The existence of a section does not require choosing among the degree-8 `V4` overlattices.**

### Correction to the finite-lattice bookkeeping

The finite classification remains relevant to the detailed geometry, but not to existence of a section. For `G=V4` and a primitive positive class `L` with `L^2=8`, Garbagnati–Sarti Proposition 6.2 allows, subject to the appropriate discriminant element existing:

1. the direct lattice `Z L ⊕ Omega_V4`;
2. an index-2 overlattice generated by a class of type `(L/2,v/2)`;
3. an index-4 overlattice generated by a class of type `(L/4,v/4)`.

An earlier working summary that reduced the possibilities to only the direct and index-2 cases was incomplete. This correction does not affect H0a.2 because `rho>=13` already forces `U` abstractly.

---

## 6. H0a.3 — `V4`-compatible elliptic fibration is not automatic

The existence theorem above does **not** say that the elliptic fibration can be chosen invariant under the K7 `V4` action.

A necessary condition for a `V4`-preserved genus-one / elliptic fibration is that its fiber class `F` be fixed by `V4`, hence

`0 != F in NS(X)^V4`, with `F^2=0`.

The minimal-Picard case is already obstructed.

A finite symplectic group acts trivially on `T_X`. Therefore, over `Q`,

`H^2(X)^V4 = T_X ⊕ NS(X)^V4`.

We already know

`rk H^2(X)^V4 = 10`.

Since `rk T_X = 22-rho`,

`rk NS(X)^V4 = 10 - (22-rho) = rho - 12`.

At the generic/minimal `V4` Picard number `rho=13`, this gives

`rk NS(X)^V4 = 1`.

An invariant ample class exists by averaging an ample class over the finite group, so this rank-one invariant lattice is positive. It therefore contains no nonzero isotropic vector.

Thus:

> **At `rho=13`, no genus-one or elliptic fibration can be preserved by the full symplectic `V4`.**

This does not contradict H0a.2: the K3 has elliptic fibrations with section, but `V4` permutes them rather than preserving one.

### Necessary specialization

For a `V4`-compatible fibration one needs at least

`rk NS(X)^V4 >= 2`,

hence necessarily

`rho >= 14`.

This is only a **necessary**, not sufficient, condition. The actual invariant lattice must contain a primitive nef isotropic class, and for a section compatible with the desired group action one must additionally control the section / Mordell–Weil action.

### H0a.3 ruling

> **HOLD. Compatibility is impossible on the minimal `rho=13` `V4` family and requires an explicit higher-Picard specialization plus an invariant isotropic class.**

This is now the next fiber-level construction problem.

---

## 7. A useful high-Picard degree-8 benchmark — not yet identified with K7

There is a mathematically close explicit family that shows the required kind of specialization is plausible.

Garbagnati–Sarti study smooth complete intersections of three diagonal quadrics in `P5` on which changing an even number of coordinate signs realizes a symplectic `(Z/2Z)^4` action. The family has dimension 4; for an algebraic K3 with this full symplectic group the minimal Picard number is 16.

Reference: A. Garbagnati, A. Sarti, *Kummer surfaces and K3 surfaces with (Z/2Z)^4 symplectic action*, Rocky Mountain J. Math. 46 (2016), arXiv:1305.3514, especially §§7 and 10.

This is highly relevant because K7 already uses a degree-8 `CI(2,2,2)` and a diagonal symplectic `V4` screen. But the current public K7 artifact does **not** establish that its final quadric net lies in this complete diagonal `(Z/2)^4` family.

Therefore this family is recorded only as a **construction benchmark**:

- it demonstrates explicit degree-8 K3 surfaces with much higher Picard rank and large symplectic 2-group action;
- when restricted to a chosen `V4`, the larger Picard lattice gives room for `NS(X)^V4` to have rank greater than one;
- it does not by itself provide the specific `V4`-invariant isotropic class required by K7;
- it must not be substituted for the actual K7 fiber without an explicit identification of the quadric net / lattice polarization / automorphisms.

The next constructive target is therefore not merely `rho>13`; it is an explicit degree-8 specialization carrying the K7 action **and** a primitive invariant nef isotropic class.

---

## 8. Critical inconsistency exposed: `Picard-rank-1` versus symplectic `V4`

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

- construct a **special degree-8 K3 with `rho>=14` for an equivariant elliptic route** carrying the required `V4` / `Z2^3` lattice action; or
- abandon the claim that the same K3 carries the symplectic `V4` action.

The second option would reopen the Betti / fixed-locus route and therefore cannot be treated as a cosmetic edit.

This contradiction is a **critical K7 structural hold**, independent of OpenWave.

---

## 9. H0b — global duality is still open

The explicit Braun–Schäfer-Nameki M/heterotic construction is established for appropriate **K3-fibered TCS G2 manifolds**, and their tractable explicit class uses elliptically fibered K3 fibers.

Current K7 v3.5 says instead:

- `(b2,b3)=(21,77)` is absent from the catalogued TCS examples;
- orthogonal TCS is excluded by the cited parity condition;
- non-orthogonal / extra-twisted TCS remain open;
- the **leading global candidate is the Joyce–Karigiannis `T3 × K3 / Z2^3` route**, not an established TCS realization.

Therefore one may not infer

`K7 elliptic K3 fiber -> K7 has the Schoen heterotic dual`.

That implication would be another local-to-global jump.

### H0b pass options

At least one of the following would be needed:

1. **TCS option:** construct an actual K7 non-orthogonal / extra-twisted TCS realization with the required compatible elliptic K3 data, then apply the established fiberwise duality.
2. **JK option:** derive an M/heterotic dual dictionary directly for the specific JK `T3 × K3 / Z2^3` resolution used by K7 and show how geometry, bundle data and orbifold action map.
3. **Independent duality option:** provide another controlled compactification dictionary that derives the 4D chiral spectrum without importing the TCS/Schoen result.

Until one closes, the Schoen `X_(19,19)` discussion remains a **conditional benchmark**, not K7 field content.

---

## 10. Updated gate table

| Gate | Statement | Status |
| --- | --- | --- |
| H0a.1 | K7 projective K3 with genuine symplectic `V4` admits genus-one fibration | **CONDITIONAL PASS** |
| H0a.2 | `U -> NS(X)` / elliptic fibration with section | **CONDITIONAL PASS** (`rho>=13`) |
| H0a.3 | elliptic fibration can be chosen `V4`-compatible | **HOLD** — impossible at minimal `rho=13`; requires higher-Picard specialization + invariant isotropic class |
| H0-struct | Picard-rank-1 description compatible with symplectic `V4` | **FAIL — contradiction** |
| H0b | global K7 lies in an established M/heterotic duality class | **OPEN** |
| H1+ | heterotic CY/bundle, chirality, `nu_R`, neutrino operator | **NOT REACHED** |

---

## 11. Immediate next computation

The next useful calculation is still **not** a neutrino mass and not yet a Schoen bundle.

It is now narrower than before:

> construct or identify the actual higher-Picard degree-8 K3 specialization selected by K7, compute `NS(X)^V4`, and exhibit (or rule out) a primitive `V4`-invariant nef isotropic class `F`.

A successful result closes H0a.3 at the fiber level. Failure on the actual K7 lattice kills the equivariant heterotic-dual route before any neutrino target is consulted.
