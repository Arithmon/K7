# K7-P2 Candidate A — `rho=17` equivariant K3-lattice gluing

**Status:** `PASS AT K3-LATTICE LEVEL / GLOBAL TORELLI OPEN`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent:** [`K7_P2_neutrino_rho17_JK_lattice_candidate.md`](K7_P2_neutrino_rho17_JK_lattice_candidate.md)

The explicit rank-17 JK candidate has

`NS = NS_17(C)`, signature `(1,16)`, `A_NS ~= (Z/2)^5`, `delta=1`.

Take

`T = U(2) + U(2) + A1(-1)`,

of signature `(2,3)`, determinant `2^5` and 2-elementary parity `delta=1`.

The public reproducer

```bash
python3 docs/openwave-candidate/check_k3_rho17_k3_gluing.py
```

constructs an explicit anti-isometry

`q_T -> -q_NS`

and checks it on all 32 discriminant classes.

One set of generator images in `C^perp/C` is represented by supports

```text
(0, 1, 3, 6)
(1, 2, 3, 6)
(3, 4, 6, 7)
(0, 1, 2, 3, 5, 6, 7, 10)
(3, 6, 9)
```

for the standard discriminant generators of `U(2)+U(2)+A1(-1)`.

Gluing `NS+T` along the graph of this anti-isometry has index `2^5`. Therefore

`|disc(glued)| = 2^5 * 2^5 / (2^5)^2 = 1`.

The glued lattice is even and has signature

`(1,16)+(2,3)=(3,19)`.

Hence, by uniqueness of the even unimodular lattice of signature `(3,19)`, it is the K3 lattice `Lambda_K3`.

## Equivariance

The `G=(Z/2)^3` action on `NS` is realized by sign changes on the `A1` frame. These induce the identity on the 2-elementary discriminant group `A_NS`.

On `T` we prescribe

- `sigma_A = sigma_B = +I`;
- `tau = -I`.

Because `A_T` is 2-elementary, `-I` also induces the identity on `A_T`. Thus the graph of the explicit discriminant anti-isometry is `G`-stable, and the action extends to `Lambda_K3`.

This removes the discriminant-gluing obstruction that killed the historical rank-15 Torelli package.

## Current boundary

The remaining K3-level problem is geometric rather than lattice-theoretic:

1. choose a compatible period with `V4` symplectic and `tau` anti-symplectic;
2. exhibit a `G`-stable ample chamber so Global Torelli promotes the lattice isometries to actual K3 automorphisms;
3. find a primitive `G`-invariant ample class of square `8` for the genus-5 `CI(2,2,2)` model;
4. promote the rank-5 invariant isotropic lattice statement to a primitive nef invariant elliptic fiber with controlled section.

Only after these steps can the global JK resolution / heterotic-duality gate be revisited.
