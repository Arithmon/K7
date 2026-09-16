# K7-P2 Candidate A — standard symplectic `V4` on `Lambda_K3`

**Status:** `STANDARD V4 INTEGRAL ACTION PASS / COMMUTING JK tau OPEN`  
**Date:** 2026-09-12  
**Target-value exposure:** none.  
**Parent reset:** [`K7_P2_neutrino_rho17_symplectic_V4_reset.md`](K7_P2_neutrino_rho17_symplectic_V4_reset.md)

The first `rho=17` sign-change realization failed because its purported symplectic involutions negate genuine `(-2)` roots and therefore cannot preserve a K3 ample/effective chamber.

This note replaces that ad hoc integralization by an explicit reconstruction of the **standard integral symplectic `(Z/2)^2` action on the full K3 lattice**.

The backend is Benedetta Piroddi, *K3 surfaces with a symplectic action of `(Z/2Z)^2`*, arXiv:2408.00643, Proposition 1.2.1. Piroddi constructs the universal cohomological action from an elliptic Kummer K3 with Mordell–Weil group `(Z/2)^2`; uniqueness of the symplectic action on `H^2(K3,Z)` then makes the resulting integral conjugacy class independent of that special surface.

Public reproducer:

```bash
python3 docs/openwave-candidate/check_k3_standard_symplectic_v4.py
```

---

## 1. Notation warning

Piroddi denotes her two **symplectic** generators by `tau` and `phi`.

K7 already uses `tau` for the required **anti-symplectic** Joyce–Karigiannis involution.

To avoid repeating the historical notation collision, the reproducer renames Piroddi's generators

```text
Piroddi tau  -> sigma_A
Piroddi phi  -> sigma_B
```

throughout.

---

## 2. Finite-index lattice `W`

The reconstruction starts from

`W = A2^8 + A2(2) + U(3) + [[4,2],[2,4]]`,

with signature `(3,19)`.

The eight `A2` components are labelled

```text
a,b,c,d,e,f,g,h
```

with two generators each. The `A2(2)` block has generators `w,z`, the `U(3)` block `x,y`, and the final positive rank-2 block `v1,v2`.

Piroddi gives seven explicit glue elements

```text
alpha, beta, gamma, delta, epsilon, zeta, eta
```

which generate `H^2(K3,Z)` as an overlattice of `W`.

The reproducer encodes equations (1.2.2) exactly and computes

`[Lambda_K3 : W] = 2916`.

The resulting rank-22 Gram matrix is:

- integral;
- even;
- determinant `-1`;
- signature `(3,19)`.

Hence it is the K3 lattice.

---

## 3. Explicit `V4` action

On `W`, `sigma_A` and `sigma_B` act by the permutations/signs of Piroddi Proposition 1.2.1.

The seven glue classes are then used to transport those rational actions to an integral basis of the full K3 lattice.

The resulting two `22 x 22` integral matrices satisfy exactly

```text
sigma_A^2 = I
sigma_B^2 = I
sigma_A sigma_B = sigma_B sigma_A
sigma_A^T G sigma_A = G
sigma_B^T G sigma_B = G
```

and

```text
tr(sigma_A)                 = 6
tr(sigma_B)                 = 6
tr(sigma_A sigma_B)         = 6.
```

Thus the character agrees with the required symplectic `V4` character, now in the correct integral conjugacy class rather than only rationally.

---

## 4. Individual involution certificate

For each of

```text
sigma_A
sigma_B
sigma_A sigma_B
```

the reproducer computes the primitive integral anti-invariant lattice as the exact integer kernel of `sigma+I`.

In all three cases:

- rank = `8`;
- determinant magnitude = `2^8`;
- the lattice is negative definite;
- after multiplying its form by `-1/2`, one obtains an integral even positive-definite unimodular rank-8 lattice.

Therefore each anti-invariant lattice is

`E8(-2)`.

This is the integral Nikulin-involution check that the old `A1` sign action failed.

In particular there are no anti-invariant `(-2)` roots to force an ample-chamber contradiction.

---

## 5. Full `V4` invariant lattice

The exact simultaneous integer kernel of

```text
sigma_A - I
sigma_B - I
```

has rank `10` and determinant magnitude

`2^10`.

Its Smith elementary divisors are

```text
1, 1, 2, 2, 2, 2, 2, 2, 4, 4
```

so its discriminant group is

`(Z/2)^6 + (Z/4)^2`.

This matches the standard lattice computed by Garbagnati–Sarti:

`Lambda_K3^V4 ~= U(2)^2 + Q_(2,2)`,

with coinvariant

`Omega_V4 ~= Lambda_12(-1)`

of rank `12`, determinant `2^10`, and no `(-2)` vectors.

Reference: A. Garbagnati and A. Sarti, *Elliptic fibrations and symplectic automorphisms on K3 surfaces*, arXiv:0801.3992.

---

## 6. What has actually been repaired

The old route had the correct rational dimensions

`10 + 4 + 4 + 4`

but the wrong integral realization.

We now have both:

```text
rational V4 character       PASS
integral K3 lattice         PASS
integral commuting V4       PASS
three E8(-2) coinvariants   PASS
full invariant lattice      PASS
rootless Omega_V4           PASS
```

Therefore the `rho=17` program can resume without returning to the discarded `A1(-1)^15` sign action.

---

## 7. Next gate: the anti-symplectic JK involution

The remaining problem is now sharply posed on a **fixed integral K3 lattice with a fixed standard `V4` action**.

Find

`tau_JK in O(Lambda_K3)`

such that:

1. `tau_JK^2=1`;
2. `tau_JK` commutes with `sigma_A` and `sigma_B`;
3. its rational action has the already-forced sector splits

```text
V4 invariant rank 10 : +5 / -5
V4 character A rank 4: +2 / -2
V4 character B rank 4: +2 / -2
V4 character C rank 4: +2 / -2;
```

4. integrally,

```text
Lambda_K3^tau_JK                       type (11,7,1)
Lambda_K3^(tau_JK sigma_A)             type (11,9,1)
Lambda_K3^(tau_JK sigma_B)             type (11,9,1)
Lambda_K3^(tau_JK sigma_A sigma_B)     type (11,9,1);
```

5. the eventual period lies in a rank-5 `tau_JK=-1`, `V4=+1` transcendental lattice;
6. the resulting projective rank-17 Néron–Severi lattice admits a common invariant ample class.

This is now a centralizer / integral fixed-lattice search, not a vague Torelli search.

---

## 8. Ruling

> **The standard symplectic `V4` obstruction is closed constructively. A fully integral `V4` action on `Lambda_K3` has been rebuilt from Piroddi's explicit gluing data and independently checked against the canonical fixed/coinvariant lattice invariants. The next live obstruction is the simultaneous integral realization of the anti-symplectic JK involution inside this `V4` centralizer.**

No degree-8 polarization, invariant elliptic fiber, global JK quotient or neutrino observable is claimed at this stage.
