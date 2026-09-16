# K7-P2 Candidate A — Joyce–Karigiannis character obstruction

**Status:** `RANK-15 FULL JK PACKAGE FAIL / rho >= 17 NECESSARY / HIGHER-PICARD CONSTRUCTION OPEN`  
**Date:** 2026-09-12  
**Target-value exposure:** none. No neutrino mass, ordering, or experimental number enters this calculation.  
**Parent gate:** [`K7_P2_neutrino_H0a3_equivariant_data_contract.md`](K7_P2_neutrino_H0a3_equivariant_data_contract.md)

This note audits the remaining anti-symplectic / Joyce–Karigiannis part of H0a.3 after recovery of the rank-15 K3 lattice. The outcome is sharper than the previous `OPEN` status:

> **The currently stated JK fixed-locus package cannot be realized on a Picard-rank-15 K3 carrying the required symplectic `V4`. Picard rank at least 17 is necessary.**

The obstruction is representation-theoretic and does not depend on the historical 15×15 matrices.

---

## 1. Frozen JK fixed-locus package

Let

`G = (Z/2Z)^3 = <tau, sigma_A, sigma_B>`,

with

`V4 = <sigma_A, sigma_B>`

symplectic.

The K7 JK target package assigns:

- `tau`: non-symplectic involution of 2-elementary type `(r,a,delta)=(11,7,1)`;
- `tau sigma_A`, `tau sigma_B`, `tau sigma_A sigma_B`: type `(11,9,1)`;
- each of the three non-trivial `V4` elements: a symplectic K3 involution with eight isolated fixed points.

For a non-exceptional 2-elementary non-symplectic involution,

`g = (22-r-a)/2`,

`k = (r-a)/2`,

where the fixed locus is one genus-`g` curve together with `k` rational curves.

Therefore

- `(11,7,1) -> (g,k)=(2,2)`;
- `(11,9,1) -> (g,k)=(1,1)`.

In both cases the fixed-locus Euler characteristic is `2`.

Thus the topological Lefschetz trace on `H^2(K3)` is

`tr(g | H^2) = chi(Fix(g)) - 2 = 0`

for all four anti-symplectic elements.

For a non-trivial symplectic involution the fixed locus is eight points, hence

`tr(g | H^2)=8-2=6`.

In the element order

`(1, tau, sigma_A, sigma_B, tau sigma_A, tau sigma_B, sigma_A sigma_B, tau sigma_A sigma_B)`, 

the target character on `H^2` is therefore

`chi_H2 = (22, 0, 6, 6, 0, 0, 6, 0)`.

Its character decomposition is perfectly valid:

`(5,5,2,2,2,2,2,2)`

in the eight one-dimensional characters of `(Z/2)^3`. The obstruction appears only after imposing projectivity and Picard rank.

---

## 2. Action on the transcendental lattice

Let `rho=rk NS(X)` and `rk T_X=22-rho`.

Two standard K3 facts are load-bearing:

1. a finite symplectic automorphism acts trivially on the transcendental lattice `T_X`;
2. for a non-symplectic involution, the invariant lattice lies in `NS(X)`, so `tau` acts as `-I` on `T_X`.

Since the generators commute, every non-trivial `V4` element acts by `+I` on `T_X`, while every element of the `tau V4` coset acts by `-I`.

Writing `t=22-rho`,

`chi_T = (t,-t,t,t,-t,-t,t,-t)`.

Hence

`chi_NS = chi_H2 - chi_T`.

At `rho=15`, `t=7`, so

`chi_NS = (15,7,-1,-1,7,7,-1,7)`.

---

## 3. Exact character obstruction at rho=15

For the character `chi_tau` which is `-1` on the `tau V4` coset and `+1` on `V4`, Fourier inversion gives its multiplicity in `NS(X)`:

`m_tau = (1/8) sum_g chi_NS(g) chi_tau(g)`.

At `rho=15`,

`m_tau = (15 - 7 - 1 - 1 - 7 - 7 - 1 - 7)/8 = -2`.

A representation cannot contain an irreducible character with negative multiplicity.

Therefore:

> **No Picard-rank-15 projective K3 can simultaneously realize the stated symplectic `V4` and the frozen JK anti-symplectic fixed-locus package.**

This is stronger than saying that one historical matrix ansatz failed. It excludes the entire rank-15 realization under the stated fixed-locus assumptions.

The public exact reproducer is

```bash
python3 docs/openwave-candidate/check_k3_jk_character_gate.py
```

It performs the full Walsh/Fourier character inversion over `(Z/2)^3` using integer arithmetic.

---

## 4. The obstruction gives a sharp lower bound: rho >= 17

For arbitrary Picard rank `rho`, the same computation yields

`m_tau = rho - 17`.

Therefore non-negativity of character multiplicities requires

`rho >= 17`.

The first representation-theoretically admissible rank is exactly

`rho=17`,

where

`rk T_X=5`

and the `tau`-only character occurs with multiplicity zero in `NS`.

This is a **necessary**, not sufficient, condition. It does not construct the required K3.

### Full-group invariant rank

The target `H^2` character also gives

`rk H^2(X)^G = (22 + 6 + 6 + 6)/8 = 5`.

Because `tau` is non-symplectic, the full `G`-invariant subspace contains no holomorphic two-form direction and is algebraic. Thus a successful realization has

`rk NS(X)^G = 5`.

Its real signature is expected to be `(1,4)`: an averaged ample class supplies the positive direction, while the two positive transcendental directions are anti-invariant under `tau`.

Consequently the full invariant lattice is an indefinite rank-5 integral lattice. By Meyer's theorem it represents zero. Thus, **if a genuine higher-Picard realization of the frozen JK package exists, a full-`G` invariant isotropic class is forced at lattice level.**

This is encouraging for the elliptic/genus-one route: the obstruction moves the required K3 to higher Picard rank, but the corrected group package itself then supplies enough invariant lattice to force an isotropic class.

Nef/effective reduction and a section for that particular class remain separate gates.

---

## 5. Historical realization audit

The private canonical construction history contains three relevant attempts. They must not be conflated.

### A. Rank-15 Clingher–Malmendier Jacobian model

The Jacobian model

`y^2 = x(x-A(t))(x-B(t))`

has the correct geometric symplectic Mordell–Weil `V4`, and that `V4` preserves its elliptic fiber.

However the obvious commuting anti-symplectic involution acts as `+I` on all of `NS`, so its fixed lattice has rank 15 rather than the required `(11,7,1)` type. The historical search through its `V4` coset and natural base Möbius involutions was exhausted without producing the target `tau`; one branch with the desired singular-fiber pattern instead generated a dihedral group rather than abelian `(Z/2)^3`.

**Ruling:** the direct rank-15 CM-Weierstrass route does not realize the frozen full JK package.

### B. Historical abstract 15×15 / Torelli package

The old lattice package was engineered to have the desired fixed-lattice ranks, but the later transcendental-character audit found an impossible negative multiplicity. The calculation above recovers the obstruction without depending on those historical matrices.

**Ruling:** not a geometric escape from the rank-15 no-go.

### C. Explicit T5-prime / `T5''` CI(2,2,2)

The later `T5''` construction successfully repaired the symplectic side at projective-model level: it gives a smooth numerical CI(2,2,2) witness with a Mukai-type symplectic `V4` and an anti-symplectic `tau` at coordinate/type level.

But its three `tau sigma` elements were explicitly recorded as **free** involutions, producing Enriques quotients. That is incompatible with the frozen `(11,9,1)` target, which requires `(g,k)=(1,1)`, i.e. an elliptic curve plus one rational curve in each fixed locus.

The same construction also retained the full integral NS Gram identification as pending at the relevant closure stage.

**Ruling:** `T5''` is useful geometry, but it does not realize the stated JK fixed-locus package.

---

## 6. Revised H0a.3 boundary

The rank-15 result must now be split cleanly:

| Sub-gate | Statement | Status |
| --- | --- | --- |
| H0a.3a | rank-15 CM geometric `V4` preserves its elliptic fiber | **CONDITIONAL PASS** |
| H0a.3b | recovered Donaldson root reflections preserve that fiber class | **CONDITIONAL PASS** |
| H0a.3c-15 | full frozen JK `Z2^3` package exists at `rho=15` | **FAIL — character obstruction** |
| H0a.3c-T5 | historical `T5''` realizes the frozen JK fixed loci | **FAIL — `tau sigma` free versus required `(g,k)=(1,1)`** |
| H0a.3d | higher-Picard degree-8 K3 realizes the full frozen JK package | **OPEN; `rho>=17` necessary** |
| H0a.3e | full-group invariant isotropic class exists once such a package is realized | **LATTICE-LEVEL CONSEQUENCE** — rank-5 invariant lattice, Meyer |
| H0b | resulting global K7 admits a controlled M/heterotic duality | **OPEN** |

So the scientifically correct statement is no longer

> “find the missing tau on the rank-15 K3.”

It is

> **“rank 15 is excluded for the frozen JK target; construct or identify a degree-8 K3 with `rho>=17` carrying the correct full `(Z/2)^3` action.”**

---

## 7. Next constructive target

The next clean-room construction problem is now finite and substantially sharper.

Find a projective degree-8 K3 `X` with:

1. `rho(X)>=17`;
2. a commuting `G=(Z/2)^3=<tau,sigma_A,sigma_B>` action;
3. `V4=<sigma_A,sigma_B>` symplectic, hence eight fixed points for each non-trivial element;
4. `tau` fixed-lattice type `(11,7,1)`;
5. all three `tau V4 \ {tau}` elements of type `(11,9,1)`;
6. an explicit degree-8 polarization preserved by `G`;
7. an explicit primitive invariant isotropic class, then nef/effective and section checks.

The representation obstruction is a preregistered falsifier: any proposed `rho<17` realization is rejected before geometric tuning.

A Picard-rank-17 K3 is therefore the new minimal search target. Kummer-type or other high-Picard degree-8 constructions may be useful search backends, but none is promoted merely from its rank.

No neutrino observable should be computed until this gate and H0b are closed.
