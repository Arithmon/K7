# Independent ratification of K7-GEO-JK-F2R1

**Date:** 2026-09-17

**Frozen object audited:** `K7-GEO-JK-F2R1 @ bfc1db056f4ed63311dca059d7f708bc70e2299c`.

**Provenance chain:** original target-blind F2 preregistration
`f9d92ada6e7de7a7dd76f17ca88900ea5b054bd1` → adversarial Gate 0
refutation `f69ef8c2ddd329b394ec88ec51b1ad8f094b42a4` → separate,
sign-only F2R1 freeze `bfc1db056f4ed63311dca059d7f708bc70e2299c`
→ this new audit. Neither earlier artefact is rewritten.

**Verdict:** **PASS for F2R1 as a distinct geometry benchmark / positive
control.** This is an explicit compact simply connected full-holonomy
`G2` existence construction with `(b2,b3)=(4,35)`, subject to the
published Joyce–Karigiannis theorem. It is not the selected
`K7-GEO-JK-F1` `(21,77)`, not a K7-P2 physical prediction, and not an
OpenWave-admitted model or criterion result.

**Method:** two independent hostile reads checked the positive-form / JK
gate and the unchanged topology separately after `bfc1db0`. The
calculations below use direct exterior algebra, weighted-projective
geometry, group relations, Lefschetz/Fourier inversion and
Riemann–Hurwitz. The earlier
`check_k3_jk_f2_explicit_action.py` was not used as proof for this audit.
Primary source: [Joyce–Karigiannis, equations (2.13), (6.16), §§4.1,
6.5–6.6, 7.3](https://arxiv.org/pdf/1707.09325). Fundamental-group
input: [Armstrong's orbit-space theorem](https://doi.org/10.1017/S0305004100042845).

## 1. Freeze integrity and the positive product form

The F2R1 freeze commit adds one new document. The original F2 file at
`f9d92ad` is byte-for-byte unchanged. F2R1 repeats exactly the same
`alpha,beta,s`, torus affine maps, seven K3 fixed-locus claims, and three
Betti data; its sole revised geometric datum is

```text
phi_JK = e123 - e1∧omega_I - e2∧omega_J - e3∧omega_K.
```

For an oriented orthonormal K3 frame `(e4,e5,e6,e7)` choose
`omega_I=e45+e67`, `omega_J=e46-e57`, `omega_K=e47+e56`.
Then

```text
phi_JK = e123-e145-e167-e246+e257-e347-e356.
```

An independent wedge calculation of
`B_phi(u,v)=(i_u phi∧i_v phi∧phi)/6` gives its **full** matrix
`B_phi_JK(e_i,e_j)=delta_ij e1234567`. It is positive and induces
exactly the product Riemannian metric. It agrees with Joyce–Karigiannis
equation (2.13). The frozen F2 plus-form had diagonal
`(+,+,+,-,-,-,-)` and remains refuted; no result here retroactively
changes its Gate 0.

For completeness, a common invariant metric exists on `X`. Average a
Kähler form over the holomorphic `<alpha,s>` to obtain `kappa1`, then
take `kappa=(kappa1-beta^*kappa1)/2`. Because `beta` is
antiholomorphic, `-beta^*kappa1` is Kähler. Yau uniqueness in this
class makes the Ricci-flat K3 metric invariant under all three maps.
The holomorphic two-form satisfies
`alpha^*Omega=-Omega`, `s^*Omega=Omega`, and after phase choice
`beta^*Omega=bar(Omega)`. Thus the three K3 parallel-form signs are

| Generator | `(omega_I,omega_J,omega_K)` | `(dx1,dx2,dx3)` |
| --- | --- | --- |
| `alpha` | `(+,-,-)` | `(+,-,-)` |
| `beta` | `(-,+,-)` | `(-,+,-)` |
| `s` | `(+,+,+)` | `(+,+,+)` |

Each generator has torus determinant `+1`, so every term of `phi_JK`
is invariant. Half-translations do not affect differentials. The K3
forms and torus coframe are parallel; therefore `phi_JK` and its Hodge
dual are parallel, hence closed and coclosed. The quotient inherits a
torsion-free Riemannian `G2` orbifold structure.

## 2. Normal complex structures and JK local data

Exactly three nonidentity elements have product fixed points:
`alpha`, `beta`, `beta s`. Their torus fixed-circle families are
pairwise disjoint. On each raw fixed threefold the pointwise
involution acts as `-I4` on its full real normal, so the local model is
`R³×(R⁴/{±1})`. The setwise stabilizer modulo pointwise isotropy is
`<s>≅Z2` for each `alpha` raw component and trivial for each `beta` or
`beta s` raw component.

With `I_lambda(v)=u×v`, `u=lambda^#/|lambda|`, contraction with the
**corrected minus-form** gives

```text
alpha, lambda=dx1: I_lambda(e2)=e3, I_lambda(e3)=-e2,
                   I_lambda|N_{C/X}=-I;
beta or beta s, lambda=dx2:
                   I_lambda(e3)=e1, I_lambda(e1)=-e3,
                   I_lambda|N_{S²/X}=-J.
```

In the `z1=1` and `z2=1` weighted charts covering `C`, the K3 normal
coordinate is `eta=w/z_j³`. The residual `s` sends `eta↦-eta` and is
the identity on the torus normal plane `(e2,e3)`. Its real normal
matrix is `diag(1,1,-1,-1)`, complex `diag(1,-1)` for the displayed
`I_lambda`. It acts on the exceptional `CP¹` by
`[z_t:z_X]↦[z_t:-z_X]`, a holomorphic map of degree `+1`.
Consequently it acts by `+1` on `H²(CP¹)`. The other two sectors have
no residual stabilizer of a raw circle. The exceptional-class local
system is **ordinary** on all four quotient strata, not `Z2`-twisted.

On an `alpha` representative choose `lambda=dx1`, and on each
`beta`/`beta s` representative choose `lambda=dx2`. Each setwise
stabilizer preserves its chosen form. Transport the form to other raw
components by the group action: `beta` reverses `dx1` while exchanging
the two raw components in each `alpha` pair, and `alpha` reverses `dx2`
while exchanging raw components in each sphere family. This transport
is consistent because those
maps do not stabilize an individual raw component. The descended
forms are parallel, nowhere zero, closed and coclosed.

The quotient is compact; its singular locus is the disjoint union of
these smooth compact associative threefolds; its local normal model
and the ordinary harmonic one-form meet precisely the orbifold
hypotheses stated in Joyce–Karigiannis §6.5. Their §6.6 twisted
variant is unnecessary. The published resolution theorem therefore
provides a compact smooth torsion-free `G2` manifold `N`.

## 3. Independent unchanged-topology check

The K3 fixed loci are still `C10,S²,empty,8 points,C2,S²,T²`
for `(alpha,beta,alpha beta,s,alpha s,beta s,alpha beta s)`.
Their Euler characteristics give the H² traces
`(22,-20,0,-2,6,-4,0,-2)` in identity-first order. Direct
Fourier inversion for character masks `(alpha,beta,s)=0,...,7`
gives multiplicities `(0,7,1,6,0,4,0,4)`. Since the torus `H¹`
characters are `(2,1,3)`, Künneth gives the rational quotient
Betti vector

```text
(b0,...,b7)(M') = (1,0,0,15,15,0,0,1).
```

There are two `alpha` quotient strata. The six fixed points of
`s|C10` give `g(C10/s)=4` by `18=2(2g-2)+6`; each mapping torus
has `b1=1+2g=9`. The `beta` and `beta s` families each form one
`S¹×S²` stratum with `b1=1`. Hence

```text
(b0,b1,b2,b3)(L) = (4,20,20,4).
```

For `pi1`, lift to `R³×X` and use the notation `T_i,A,B,S` of the
previous audit. The six elements `A,T2A,T3A,B,T1B,BS` have fixed
points. Their products give `T2,T3,T1,S` respectively, while `A,B`
are already in the list. They generate the full lifted deck group;
Armstrong yields `pi1(M')=1`. The `A1` replacement preserves `pi1`.

The ordinary resolution formula now applies **as a JK theorem**, not
only as a topological counterfactual:

```text
b_k(N)=b_k(M')+b_{k-2}(L),
(b0,...,b7)(N)=(1,0,4,35,35,4,0,1).
```

Both vectors obey Poincaré duality and have Euler characteristic zero.
Because `pi1(N)=1`, the torsion-free metric has holonomy exactly
`G2` by the full-holonomy criterion used in Joyce–Karigiannis.

## Claim table and scope

| Claim | Verdict | Decisive evidence |
| --- | --- | --- |
| F2R1 freeze integrity | **PASS** | Sign-only document at `bfc1db0`; original F2 and its failed audit remain unchanged. |
| Positive product `G2` form | **PASS** | `B_phi_JK=I7·vol7` in an orthonormal frame; JK equation (2.13). |
| Generator invariance and torsion-free orbifold | **PASS** | Paired sign table, torus determinant `+1`, common Ricci-flat metric and parallel forms. |
| `I_lambda` / ordinary local system | **PASS** | Residual `s` acts complex `diag(1,-1)` and degree `+1` on exceptional `CP¹`; other residuals trivial. |
| JK §6.5 hypotheses | **PASS** | Compact torsion-free positive orbifold, disjoint `A1` three-strata, descended parallel nowhere-zero one-forms. |
| Quotient character and Betti | **PASS** | Direct Lefschetz/Fourier and Künneth give `(0,0,15)`. |
| Stratum topology | **PASS** | Two mapping tori of `b1=9` and two `S¹×S²` of `b1=1`, giving `(b0,b1)=(4,20)`. |
| Fundamental group | **PASS** | Six fixed-point lifts generate the deck group; Armstrong gives `pi1=1`. |
| Resolved Betti and full holonomy | **PASS** | JK ordinary resolution gives `(b1,b2,b3)=(0,4,35)` and preserves `pi1=1`. |

**Ratification boundary:** F2R1 is a positive control for this explicit
Joyce–Karigiannis geometric construction. The finite checker can
reproduce character and orbit arithmetic; it does not numerically
construct the torsion-free metric, whose existence follows from the
published analytic theorem. No degree-eight/rho17 F1 package,
selected `(21,77)` topology, K7 neutrino operator, physical observable,
or OpenWave criterion is inferred.
