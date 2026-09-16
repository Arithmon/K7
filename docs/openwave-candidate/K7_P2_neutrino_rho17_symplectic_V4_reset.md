# K7-P2 Candidate A — `rho=17` symplectic-`V4` reset

**Status:** `OLD rho17 SIGN ACTION FAIL / rho>=17 CHARACTER SURVIVES / STANDARD V4 INTEGRALIZATION OPEN`  
**Date:** 2026-09-12  
**Target-value exposure:** none. No neutrino mass, ordering or experimental number enters this gate.  
**Parent:** [`K7_P2_neutrino_rho17_K3_gluing.md`](K7_P2_neutrino_rho17_K3_gluing.md)

The previous `rho=17` package closed an abstract lattice problem correctly: the frozen JK character is representation-theoretically admissible at `rho=17`, the lattice `NS_17(C)` is even of type `(17,5,1)`, and its discriminant form admits an equivariant abstract gluing to the K3 lattice.

It did **not** yet prove that the particular integral sign-change action used on `NS_17(C)` belongs to the geometric conjugacy class of a symplectic `V4=(Z/2)^2` action on a K3 surface.

That missing check fails.

The correction is narrow but decisive:

> **The lower bound `rho>=17` survives. The old integral sign-change realization of the `V4` does not. Before Global Torelli, the `V4` must be rebuilt in the standard symplectic integral conjugacy class.**

Public reproducer:

```bash
python3 docs/openwave-candidate/check_k3_rho17_symplectic_v4_gate.py
```

---

## 1. What remains valid

Nothing in this note changes the exact character obstruction

`m_tau = rho - 17`.

So the full frozen JK package still requires

`rho >= 17`,

and `rho=17` remains the first rationally admissible Picard rank.

Likewise the target character on `H^2(K3)` remains

`(22, 0, 6, 6, 0, 0, 6, 0)`

in the order

`(1, tau, sigma_A, sigma_B, tau*sigma_A, tau*sigma_B, sigma_A*sigma_B, tau*sigma_A*sigma_B)`.

Restricting that character to

`V4=<sigma_A,sigma_B>`

gives the four `V4` isotypic dimensions

`10 + 4 + 4 + 4`.

Thus a genuine symplectic `V4` at `rho=17` must still have

- `rank H^2(K3)^V4 = 10`;
- `rank NS(X)^V4 = 5`, because `rank T_X=5` and the symplectic group fixes `T_X` pointwise;
- a rank-12 coinvariant lattice inside `NS(X)`.

The rational bookkeeping was therefore not the mistake.

---

## 2. Fatal check on the previous integral action

The old construction starts from the frame

`L0 = U + A1(-1)^15`

and realizes `G` by sign changes on the fifteen `A1(-1)` coordinate roots.

For every non-trivial element of the proposed symplectic `V4`, the reproducer finds eight coordinate roots `r` such that

`r^2 = -2`

and

`sigma(r) = -r`.

This cannot be the action of a projective K3 automorphism.

By Riemann–Roch, for a `(-2)` class `r` on a K3, at least one of `r` and `-r` is effective. An automorphism preserves the effective cone. If it sends `r` to `-r`, it sends whichever of the two is effective to its negative, which is impossible; equivalently no ample/Kähler chamber can be preserved by this sign action.

So the obstruction appears **before** the period or Global Torelli step.

This also explains why the previous check

`rank H^2(X)^sigma = 14`

was insufficient. The rank is a necessary character check, not an integral conjugacy-class check.

### Ruling

The statements

- `rho=17 character PASS`;
- `abstract NS lattice PASS`;
- `abstract discriminant gluing PASS`;

remain useful.

The statement

- `the explicit sign-change V4 is a geometric symplectic V4`

is **FAIL**.

---

## 3. Correct integral target for a symplectic `V4`

Nikulin's uniqueness theorem says that for a fixed finite abelian symplectic group, the induced action on the K3 lattice is unique up to lattice isometry. Garbagnati–Sarti compute this action explicitly for the allowed groups, including

`V4=(Z/2)^2`.

References:

- A. Garbagnati and A. Sarti, *Elliptic fibrations and symplectic automorphisms on K3 surfaces*, arXiv:0801.3992.
- B. Piroddi, *K3 surfaces with a symplectic action of (Z/2Z)^2*, arXiv:2408.00643.

For the standard symplectic `V4`, let

`Omega_V4 = (H^2(K3,Z)^V4)^perp`.

The required integral package is:

- `rank Omega_V4 = 12`;
- `|disc Omega_V4| = 2^10`;
- `A_Omega ~= (Z/2)^6 + (Z/4)^2`;
- `Omega_V4` contains no vectors of square `-2`;
- the invariant lattice has rank 10 and is

`H^2(K3,Z)^V4 ~= U(2) + U(2) + Q_(2,2)`,

where

```text
Q_(2,2) =
[ 0  1  0  0  0  0 ]
[ 1 -2  2  0  0  0 ]
[ 0  2 -4  2  0  0 ]
[ 0  0  2 -4  2  0 ]
[ 0  0  0  2 -4  4 ]
[ 0  0  0  0  4 -8 ]
```

and the reproducer verifies

`|det(U(2)^2 + Q_(2,2))| = 2^10`.

This is the integral object that must replace the old `A1` sign representation.

---

## 4. The JK character already constrains the commuting `tau`

The reset does not return us to an unconstrained search.

Let the four rational `V4` sectors of `H^2` be

- the invariant sector, dimension `10`;
- the three non-trivial character sectors, dimension `4` each.

The traces of all four elements in the coset `tau V4` are zero in the frozen JK package.

Fourier inversion over `V4` therefore gives

`tr(tau | H_psi) = 0`

on **every** `V4` character sector.

Hence the target eigenspace splits of `tau` are forced:

```text
V4-invariant sector, dim 10 :  +5 / -5
nontrivial sector A, dim 4  :  +2 / -2
nontrivial sector B, dim 4  :  +2 / -2
nontrivial sector AB, dim 4 :  +2 / -2
```

At `rho=17`, the five `tau=-1` directions in the invariant sector are precisely the intended transcendental directions, while the five `tau=+1` directions are algebraic.

Thus the next search is not

> choose an arbitrary new rank-17 lattice.

It is

> **inside the centralizer of the standard symplectic `V4` action on `Lambda_K3`, find an involution `tau` with the forced `5+5 / 2+2 / 2+2 / 2+2` rational split and the required integral fixed-lattice types.**

---

## 5. Integral fixed-lattice gates for `tau`

The rational split is only a first filter.

A successful `tau` must still satisfy all of the following integrally:

1. `tau` commutes with the standard symplectic `V4` action;
2. `tau` acts anti-symplectically on the eventual period;
3. `Lambda_K3^tau` has 2-elementary type `(11,7,1)`;
4. each of
   - `tau*sigma_A`,
   - `tau*sigma_B`,
   - `tau*sigma_A*sigma_B`
   has fixed lattice type `(11,9,1)`;
5. the projective Néron–Severi lattice has rank `17` rather than an accidental larger rank;
6. there exists a common invariant positive class and hence a `G`-stable Kähler chamber.

Only after these are closed does Global Torelli become the correct next theorem.

---

## 6. Preferred construction backends

### Backend A — standard cohomological action

Piroddi gives an explicit description of the standard symplectic `(Z/2)^2` action on `H^2(X,Z)` and studies its projective moduli. This is the cleanest backend for a centralizer calculation because it starts in the correct integral conjugacy class rather than trying to repair the old sign frame after the fact.

### Backend B — elliptic/Kummer realization

Garbagnati–Sarti obtain the standard lattices from explicit elliptic K3 surfaces with torsion sections. This route is attractive later because Candidate A also wants an invariant elliptic datum.

The backend is acceptable only if it realizes the standard marked `V4` action first. Sharing the correct rank or trace is not enough.

---

## 7. Revised order of work

The previous handoff proposed

```text
period
-> ample chamber
-> Global Torelli
-> h^2=8
-> invariant elliptic fiber
```

for the old `NS_17(C)` action.

That order is now superseded by

```text
rho>=17 character theorem                    CLOSED
old A1 sign integralization                  FAIL
standard symplectic V4 lattice/action        NEXT
commuting tau in its integral centralizer    NEXT
four Nikulin fixed-lattice types             NEXT
G-stable positive/ample chamber              THEN
period + Global Torelli                      THEN
primitive invariant h^2=8                    THEN
primitive nef invariant fiber + section      THEN
global JK                                    LATER
M/heterotic + neutrino operator              NOT REACHED
```

No neutrino observable should be calculated during this reset.

---

## 8. Current ruling

> **`rho=17` remains the first admissible rank for the frozen JK character, but the first explicit `NS_17(C)` sign action is not the integral symplectic `V4` conjugacy class and cannot preserve a K3 ample chamber. The constructive problem is now to place the same forced rational character inside the standard rootless rank-12 symplectic `V4` coinvariant lattice, then solve for the commuting anti-symplectic `tau`.**

This is a correction of the integral action, not a reopening of the rank-15 route and not a failure of the `rho>=17` theorem.
