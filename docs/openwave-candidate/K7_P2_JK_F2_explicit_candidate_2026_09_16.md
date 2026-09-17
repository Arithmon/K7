# K7-GEO-JK-F2 candidate: explicit eight-element product action

**Date:** 2026-09-16

**Base:** `codex/k7-geometry-freeze-rho17 @ de20f3813456e6b1b1fababaa115f7b91f92bea4`

**Status:** target-blind **candidate geometry / review calculation**, not a
ratified K7 topology, not `K7-P2`, and not a continuation of frozen
`K7-GEO-JK-F1`. The F1 choice `(b2,b3)=(21,77)` and its rho17 package are
left intact as provenance. This candidate's distinct output is `(4,35)`.

**Primary source:** [Joyce–Karigiannis, Example 7.2 and §§6.5–6.6,
7.3](https://arxiv.org/pdf/1707.09325). Their example supplies the K3 double
plane, `alpha,beta`, torus action, and orbifold resolution theorem. The
third involution `s` and all eight-element calculations below are a new
proposed extension, not a result attributed to that paper.

## Verdict by claim

| Claim | Current verdict |
| --- | --- |
| An explicit faithful `(Z/2)^3` product action preserves a torsion-free product `G2` structure | **GO**, by the maps and invariant hyperkähler metric below. |
| The orbifold has only disjoint associative `A1` strata | **GO**, from the affine torus fixed sets and residual action below. |
| Ordinary quotient Betti triple | **GO:** `(b1,b2,b3)=(0,0,15)`. |
| Stratum Betti pair, without local-system twist | **GO:** `(b0,b1)=(4,20)`; exceptional `S2` orientation is preserved. |
| Applying Joyce–Karigiannis orbifold resolution gives a compact full-holonomy `G2` example | **Conditional GO:** the stated construction meets the §6.5 local and one-form hypotheses, and the quotient fundamental group calculation below is trivial. This is a mathematical candidate for independent referee review, not an earned K7 geometry claim. |
| Reproducing frozen F1 or deriving a physical observable | **NO:** the K3 characters, fixed loci, Betti numbers, and program role differ. |

## 1. Exact action, fixed before Betti arithmetic

Let `X` be the smooth K3 double cover of `CP2` branched over the Fermat
sextic, written in `P(1,1,1,3)` as

```text
w² = z0⁶ + z1⁶ + z2⁶.
```

The source's deck and real involutions, together with the proposed new map,
are

```text
alpha([z0,z1,z2],w) = ([z0,z1,z2],-w)
beta ([z0,z1,z2],w) = ([bar(z0),bar(z1),bar(z2)],bar(w))
s    ([z0,z1,z2],w) = ([-z0,z1,z2],-w).
```

Weighted-projective scaling makes these well-defined. They are commuting
involutions and generate `G=<alpha,beta,s>=(Z/2)^3`. The map `s` preserves
the holomorphic K3 two-form: its base determinant and its `w` sign are both
`-1`. Thus `alpha` is nonsymplectic holomorphic, `s` is symplectic
holomorphic, and `beta` is antiholomorphic for the displayed complex
structure `I`.

On `T3=R3/Z3`, retain the source's first two affine maps and add a free
half-translation:

```text
alpha_T(x1,x2,x3) = ( x1,     -x2,       -x3)
beta_T (x1,x2,x3) = (-x1,      x2, 1/2 - x3)
s_T    (x1,x2,x3) = ( x1+1/2,  x2,         x3).
```

All commute modulo `Z3` and square to the identity there. Choose any
Kähler form `kappa0` on `X`, average over the holomorphic group `<alpha,s>`
to obtain `kappa1`, and take `kappa=(kappa1-beta^*kappa1)/2`. Because `beta`
is antiholomorphic, `-beta^*kappa1` is Kähler; `kappa` is fixed by
`alpha,s` and negated by `beta`. Uniqueness of the Ricci-flat Kähler metric
in this class gives a common invariant hyperkähler metric. After choosing
the phase of its holomorphic two-form, the actions on its three parallel
forms and on the torus coframe agree:

```text
          omega_I,omega_J,omega_K       dx1,dx2,dx3
alpha          (+,-,-)                    (+,-,-)
beta           (-,+,-)                    (-,+,-)
s              (+,+,+)                    (+,+,+).
```

Hence they preserve the standard product form
`phi=dx1∧dx2∧dx3 + dx1∧omega_I + dx2∧omega_J + dx3∧omega_K`.

## 2. K3 fixed sets and rational character

The source gives `Fix_X(alpha)=C10`, `Fix_X(beta)=S2`, and
`Fix_X(alpha beta)=empty`. The new maps can be checked directly:

| Element | K3 fixed set | Euler characteristic | `tr(H²(X))=chi-2` |
| --- | --- | ---: | ---: |
| `1` | `X` | 24 | 22 |
| `alpha` | sextic curve `C10` | -18 | -20 |
| `beta` | `S2` | 2 | 0 |
| `alpha beta` | empty | 0 | -2 |
| `s` | 6 points at `z0=w=0`, 2 above `[1:0:0]` | 8 | 6 |
| `alpha s` | double cover of `z0=0` branched at 6 points: `C2` | -2 | -4 |
| `beta s` | `S2` | 2 | 0 |
| `alpha beta s` | `T2` | 0 | -2 |

For the last two real loci, write a real base point as `[i u0,u1,u2]`.
On `Fix(beta s)`, `w=i v` and `v²=u0⁶-u1⁶-u2⁶`; the allowed base is a disk
and its branched double is `S2`. On `Fix(alpha beta s)`, `w=v` and
`v²=u1⁶+u2⁶-u0⁶`; the allowed base is the complementary Möbius band.
The real `O(3)` sheet monodromy around its core makes the branched double
connected. Its fixed locus is orientable because a constant phase of the
nowhere-zero holomorphic K3 two-form restricts to a real volume form there;
with `chi=0`, the connected surface is a torus. The nontrivial monodromy
is essential: treating `w` as a globally signed scalar on `RP2` gives the
wrong real topology.

Use character masks with bits `(alpha,beta,s)`. Fourier inversion of the
eight traces gives

```text
character mask       0  1  2  3  4  5  6  7
H² multiplicity      0  7  1  6  0  4  0  4.
```

The torus coframe characters are `(2,1,3)`. Künneth and averaging give

```text
b1(orbifold) = 0
b2(orbifold) = m0 + dim(Λ² H¹(T3))^G = 0
b3(orbifold) = dim(Λ³ H¹(T3))^G + m2+m1+m3
              = 1 + 1 + 7 + 6 = 15.
```

These are ordinary rational cohomology numbers of the singular quotient;
the half-translation does not alter the cohomology representation.

## 3. Actual singular strata and exceptional-class monodromy

The affine fixed-circle sets are

```text
alpha:  x2,x3 in {0,1/2};       x1 free                 (4 circles)
beta:   x1 in {0,1/2}, x3 in {1/4,3/4}; x2 free         (4 circles)
beta s: x1,x3 in {1/4,3/4};    x2 free                 (4 circles).
```

Every other nonidentity group element acts freely on `T3` because it has a
half-translation along a coordinate whose linear sign is `+1`. These three
fixed-circle families are pairwise disjoint, so every product stabilizer
has order at most two. The local quotient is exactly
`R3 × (R4/{+/-1})` along a smooth associative threefold.

The residual centralizer quotient matters. `beta` pairs the four `alpha`
circles into two orbits; `s` preserves each circle but translates `x1` by
`1/2` and acts as `s_C` on `C10`. Each of the two resulting strata is the
mapping torus `(S1 × C10)/<(x1,p) -> (x1+1/2,s_C(p))>`.
The restriction `s_C` has exactly six fixed points (`z0=0` on the Fermat
sextic), and Riemann–Hurwitz gives `g(C10/s_C)=4`. Therefore each mapping
torus has `b1=1+2*4=9`. For `beta` and `beta s`, the residual `<alpha,s>`
acts freely and transitively on each four-circle family. Each contributes
one `S1 × S2`, with `b1=1`. Thus

```text
stratum type                      count   b0   b1
mapping torus of (C10,s_C)         2      2   18
S1 × S2 (beta and beta s)          2      2    2
total                              4      4   20.
```

There is no sign twist on the exceptional `S2` cohomology: the only
nontrivial residual stabilizer of an `alpha` circle is `s`, which is
holomorphic on the K3 normal complex line. It also preserves `phi` and
`lambda=dx1`, hence Joyce–Karigiannis's induced complex structure
`I_lambda` on the full real four-dimensional normal space. Its monodromy
is holomorphic on the exceptional `CP1` and acts by `+1` on `H²(CP1)`;
the Betti increment is therefore untwisted even if the sphere bundle is
not globally a product.

The residual stabilizer of an individual `beta` or `beta s` circle is
trivial. On the two mapping tori `dx1` descends; on the two sphere strata
`dx2` descends. These forms are parallel, nonzero, closed and coclosed in
the induced product metric. The ordinary `A1` resolution formula in
Joyce–Karigiannis §6.5 therefore gives

```text
(b1,b2,b3)(N) = (0, 0+4, 15+20) = (0,4,35).
```

For the fundamental group, lift the action to simply connected `R3 × X`.
Let `t1,t2,t3` be unit deck translations. The lifts of `alpha` and `beta`
have fixed points. For every integer `n`, so do `t2^n alpha`, `t3^n alpha`
and `t1^n beta`: their signed torus coordinates can be set to `n/2`, and
the respective K3 fixed sets are nonempty. The lift `beta s` fixes, for
example, torus coordinates `x1=-1/4, x3=1/4` together with a point of
`Fix_X(beta s)`. Thus `s` lies in the normal subgroup generated by fixed-point
elements after killing `beta` and `t1`. These elements generate the full
deck group. [Armstrong's orbit-space theorem](https://doi.org/10.1017/S0305004100042845)
then gives `pi1((T3×X)/G)=1`; the `A1` resolution preserves `pi1`, as in
Joyce–Karigiannis Proposition 6.1. Under the §6.5 orbifold extension,
the resulting torsion-free metric has full `G2` holonomy.

## Independent gate and program boundary

Run from the repository root:

```bash
python3 docs/openwave-candidate/check_k3_jk_f2_explicit_action.py
```

The stdlib checker composes all 64 torus pairs on an exact rational grid,
derives fixed-circle sets and their group orbits, Fourier-inverts the K3
Euler inputs, and recomputes quotient and resolution Betti numbers. It does
not prove the real-locus topology, invariant metric, local-system sign, or
the analytic gluing theorem; those are the geometric arguments and cited
theorem above. A reviewer should specifically challenge the real `O(3)`
monodromy and the mapping-torus exceptional class before promotion.

This example has a degree-two double-plane polarization and a different
K3 character from F1. No primitive degree-eight polarization, rho17 action,
heterotic map, neutrino mass operator, or genuine physical prediction has
been derived from it. The concrete next program decision is whether to
adopt this as a **new** geometry benchmark under a separately ratified
identifier, or continue seeking the selected `(21,77)` through another
construction. The mathematical calculation itself does not make that
selection.
