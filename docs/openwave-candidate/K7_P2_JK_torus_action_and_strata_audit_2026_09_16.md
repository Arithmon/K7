# K7-GEO-JK-F1: product torus action and singular-stratum audit

**Date:** 2026-09-16

**Target:** `codex/k7-geometry-freeze-rho17 @ 6289fa13d9849727cc4e1d8156c6e5cb7e6b27f4`

**Freeze:** `K7-GEO-JK-F1 @ 629e87ef968f2b126b7ca4a1fa89a81ccedf2fa4`

**Decision corpus:** the frozen K3 character and fixed-locus types, §8.4 of
`publications/papers/markdown/k7_framework_3_5_S1_foundations.md`, the
post-freeze quotient-cohomology audit, and Joyce–Karigiannis,
[*A new construction of compact torsion-free G2-manifolds by gluing families
of Eguchi–Hanson spaces*](https://arxiv.org/pdf/1707.09325), §§6.6, 7.3.
No K3 automorphism realizing F1 is assumed to have been constructed.

## Verdict by claim

| Claim | Verdict |
| --- | --- |
| The frozen K3 roles admit a product-form torus linear representation | **GO, conditional:** it is forced to have characters `(1,chi_tau,chi_tau)`. |
| The ordinary quotient has the claimed Betti pair `(b2,b3)=(0,22)` | **REQUEST CHANGES — BLOCKER:** the forced triple is `(b1,b2,b3)=(1,6,16)`, independent of affine shifts. |
| The 12 `T³` and nine anti-symplectic curve rows form the claimed disjoint `A1` singular set | **REQUEST CHANGES — BLOCKER:** the full-group orbit count, torus fixed-circle multiplicity, and unavoidable order-four stabilizers contradict that accounting. |
| The displayed additive resolution formula establishes `(21,77)` and full `G2` holonomy for this F1 product route | **NO-GO for the stated simple-`A1` route:** its prerequisites and inputs fail. Other resolutions or a different frozen geometry remain open. |

## 1. Specify the torus representation before any Betti arithmetic

For a common invariant hyperkähler triple on K3, write the product form as

```text
phi = dx1 ∧ dx2 ∧ dx3 + dx1 ∧ omega_I + dx2 ∧ omega_J + dx3 ∧ omega_K.
```

A symplectic K3 element of the frozen `V4` fixes the holomorphic two-form
`omega_J+i omega_K` and, as an isometry, the invariant Kähler form `omega_I`.
An anti-symplectic `tau` fixes `omega_I` and negates `omega_J,omega_K`. To
preserve `phi`, the torus coframe must transform by the same signs:

```text
sigma_A, sigma_B: I_3
tau:              D = diag(+1,-1,-1)
H¹(T³;Q):         1 ⊕ chi_tau ⊕ chi_tau.
```

This is the linear representation; affine translations do not change its
action on cohomology. It is the product-form consequence of the frozen K3
roles, not a constructed K3 action or a choice made after examining a target.

The frozen K3 `H²` character has multiplicities `m_1=5`, `m_chi_tau=5`, and
`m_chi=2` for each other character. Künneth and finite-group averaging give

```text
b1((T³×K3)/G) = dim H¹(T³)^G                         = 1
b2((T³×K3)/G) = dim (Λ² H¹(T³))^G + m_1          = 1 + 5 = 6
b3((T³×K3)/G) = dim (Λ³ H¹(T³))^G + m_1+2m_tau = 1 + 5+10 = 16.
```

`python3 docs/openwave-candidate/check_k3_jk_quotient_cohomology.py`
recomputes this triple as well as the previous representation-independent
bounds. Retaining the *unverified* fixed-locus increments `(21,55)` only as a
counterfactual would give `(b2,b3)=(27,71)`, not `(21,77)`. Under the simple
`A1` resolution theorem, `b1` is unchanged; the resulting `b1=1` would also
preclude full `G2` holonomy. The actual F1 singularities fail the simple
`A1` prerequisite below, so this last statement is conditional on such a
resolution, rather than an asserted theorem about an unknown resolution.

## 2. Affine action on a split torus: the table-compatible case is unique

Take the explicit split torus `T³=R³/Z³` and the above `D`. Every order-two
symplectic generator is a translation by a half-period `u_A,u_B` in
`(Z/2)^3`. After conjugating by a torus translation, the anti-symplectic
generator has the form

```text
sigma_v(x) = x + u_v/2,                 u_v = v_A u_A xor v_B u_B
tau(x)     = D x + (epsilon/2,0,0),    epsilon in {0,1}.
```

There are `8×8×2=128` labelled-generator parameter cases; these are not
claimed inequivalent under torus automorphisms. The stdlib-only
`check_k3_jk_torus_affine_gate.py` enumerates them independently:

```text
V4-orbit T³ sectors from symplectic fixed points: 0, 4, or 12
anti-symplectic elements with torus fixed circles: 0, 2, or 4.
```

All 12 proposed `V4` orbits require `u_A=u_B=0`. To give all four anti
elements fixed circles then requires `epsilon=0`. This is the **only** case
within the split family satisfying both prerequisites of the source table.
It gives four torus fixed circles per anti element. The unique explicit
torus half of that conditional action is therefore

```text
sigma_A(x)=x,  sigma_B(x)=x,  tau(x1,x2,x3)=(x1,-x2,-x3).
```

The K3 half is still unconstructed. For a non-split integral torus lattice,
Joyce–Karigiannis §7.3 allows **two or four** fixed circles for an anti
element; none of the contradictions below needs the split count four.

## 3. The 12 `T³` row does not survive the full-group quotient

The 24 symplectic K3 fixed points form 12 `V4` orbits, as the historical
phase-1 screen states. The source then treats these as 12 `T³` components of
the full `G` quotient without applying `tau`. Suppose `p` pairs of these
orbits are exchanged by `tau` and `s` are preserved. Then `2p+s=12`.

For a paired orbit, the full quotient contributes one `T³` with `b1=3`.
For a preserved orbit, the torus quotient has rational `b1=1`, because
`tau` acts by `D`. Thus, even before accounting for intersections,

```text
b0(symplectic row after full G quotient) = p+s   = 12-p
b1(symplectic row after full G quotient) = 3p+s = 12+p <= 18.
```

The source row `(b0,b1)=(12,36)` is impossible. If the loci intersect other
strata, they cannot be inserted as disjoint `A1` components either.

## 4. The anti-symplectic curves meet symplectic fixed points

Let `C` be the unique genus-two component of `Fix_K3(tau)`. It is preserved
by `V4`, because the other two `tau`-fixed curves are rational. Each
nonidentity symplectic involution restricts nontrivially to `C`: it cannot
fix a K3 curve pointwise, since its K3 fixed locus consists of eight isolated
points. Riemann–Hurwitz makes its number of fixed points on `C` either `2`
or `6`. The three symplectic K3 fixed sets are pairwise disjoint: at a common
fixed point two distinct symplectic involutions would both have derivative
`-I` on the K3 tangent, making their nonidentity product have identity
derivative at a fixed point and hence be the identity isometry. Therefore
the `V4` stabilizer of any point on `C` has order at most two. Applying
Riemann–Hurwitz to the full `V4` action gives

```text
2 = 4(2g(C/V4)-2) + sum_{sigma in V4\{1}} #Fix_C(sigma).
```

Each summand is at least two, so `g(C/V4)=0` and the sum is ten; the three
fixed-point counts are `(6,2,2)` up to relabelling. In particular, there are
K3 points fixed jointly by `tau` and a symplectic generator. In the
table-compatible torus action, the symplectic generators act identically on
`T³`, and `tau` has fixed circles. Their products therefore have points with
stabilizer `(Z/2)^2` in `T³×K3`. The singular set cannot consist solely of
disjoint local `R³×(R⁴/{±1})` strata.

The same calculation gives `C/V4` genus zero. For each torus circle fixed
by `tau`, its genus-two-derived quotient piece is thus based on a rational
curve, not the listed `S¹×Σ₂`. Different fixed torus circles are not
permuted by `V4` when its translations vanish. Their possible intersections
with other strata require an explicit higher-isotropy resolution; counting
them as the one source-table component is invalid.

Joyce–Karigiannis §7.3 explicitly prescribes the orbifold stratum
`Fix(gamma)/Delta`, with `Delta` the residual centralizer quotient. Their
Betti formula applies to an `A1` resolution after the singular strata and
any twisting have been established; §6.6 treats twisted local coefficients.
Neither step is supplied by the K7 fixed-point orbit count.

## Concrete NEXT

1. Record the F1 product simple-`A1` arithmetic closure and full-holonomy
   route as failed. Preserve the frozen F1 target and the scoped rho17
   lattice-search data as provenance, without promoting them to K7 geometry.
2. If a new quotient route is pursued, preregister its K3 action, full affine
   torus matrices and translations, every stabilizer orbit, and the intended
   local resolution before computing Betti numbers. A changed fixed-locus
   package or topology needs a new freeze identifier under F1's rule.
3. Recompute ordinary quotient cohomology from characters and singular
   contributions from the actual quotient strata, including any local-system
   twists and order-four intersections. Only then revisit `(21,77)`, full
   holonomy, or downstream physical claims.
