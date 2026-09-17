# Independent F2 ratification audit

**Date:** 2026-09-17

**Frozen preregistration point:** `K7-GEO-JK-F2 @ f9d92ada6e7de7a7dd76f17ca88900ea5b054bd1`.
The maps `alpha,beta,s`, their affine torus partners, and the stated K3
fixed-locus package are audited exactly as registered. This audit does not
edit the preregistration or reuse its arithmetic checker as proof.

**Decision:** **HOLD ratification of F2 at the frozen point.** The fixed-set,
orbifold, fundamental-group and rational-cohomology calculations pass the
independent gates below. The displayed product three-form in the frozen
preregistration has the wrong sign for a *Riemannian* `G2` structure: it is a
split form of signature `(3,4)`. The same frozen maps preserve the correct
Joyce–Karigiannis minus-form, but substituting that geometric datum would be
an explicit erratum or a new preregistration, not an automatic ratification
of `f9d92ad`. Neither F1 nor K7-P2 is affected.

**Primary references:** [Joyce–Karigiannis, equations (2.7), (2.13),
Remark 4.1 and §§6.5–6.6, 7.3](https://arxiv.org/pdf/1707.09325);
[Armstrong's orbit-space theorem](https://doi.org/10.1017/S0305004100042845).

## Gate 0: the frozen product form

At an oriented orthonormal K3 tangent frame `e4,...,e7`, its conventional
hyperkähler forms can be written

```text
omega_I = e45 + e67
omega_J = e46 - e57
omega_K = e47 + e56.
```

The frozen note writes `phi_+ = e123 + e1 omega_I + e2 omega_J + e3 omega_K`.
For any stable three-form define the symmetric density
`B_phi(u,v)=(i_u phi ∧ i_v phi ∧ phi)/6`. Direct exterior multiplication
gives

```text
B_phi+(e1,e1) = + e1234567,
i_e4 phi+    = -e15 -e26 -e37,
B_phi+(e4,e4) = - e1234567.
```

Indeed the complete diagonal is `(+,+,+,-,-,-,-)` in this frame. A positive
Riemannian `G2` form has `B_phi(u,u)` of one sign for every nonzero `u`.
Thus `phi_+` is a split-`G2` form, not the claimed torsion-free Riemannian
product form. Reversing the seven-dimensional orientation cannot make this
indefinite density definite. Joyce–Karigiannis's positive form for these
same Kähler forms is

```text
phi_JK = e123 - e1 omega_I - e2 omega_J - e3 omega_K.
```

The common metric can be obtained without assuming it from the frozen
note. Start with a Kähler form `kappa0`, average it over the holomorphic
group `<alpha,s>` to get `kappa1`, and set
`kappa=(kappa1-beta^*kappa1)/2`. Since `beta` is antiholomorphic,
`-beta^*kappa1` is Kähler. The resulting class is fixed by `alpha,s`
and negated by `beta`; uniqueness of the Ricci-flat Kähler metric in
that class gives a metric invariant under all three maps. The weighted
residue holomorphic two-form transforms by `alpha^*Omega=-Omega`,
`s^*Omega=Omega` (base and sheet signs cancel), and after phasing
`beta^*Omega=bar(Omega)`. Thus the K3 parallel-form signs are
`alpha:(+,-,-)`, `beta:(-,+,-)`, `s:(+,+,+)`, exactly the differentials
of the three frozen torus maps. The valid `phi_JK` is closed and
coclosed for the resulting flat-product metric.

Every frozen generator preserves **both** displayed algebraic forms:
its torus coframe signs equal its `omega` signs, their products in each
summand are `+1`, and the torus linear determinant is `+1`. This establishes
that the *maps* admit a genuine product `G2` action; it does not make the
frozen `phi_+` positive. The following local `I_lambda` and analytic gates
are therefore stated for `phi_JK` as a **conditional comparison**, while
the topological gates concern the unchanged quotient itself.

## A. Four new K3 fixed loci in weighted-projective coordinates

Use `X={w²=z0⁶+z1⁶+z2⁶} ⊂ P(1,1,1,3)`, so
`(z0,z1,z2,w)~(t z0,t z1,t z2,t³w)`.
Let `alpha:w↦-w`, `beta:(z,w)↦(bar z,bar w)`, and
`s:(z0,z1,z2,w)↦(-z0,z1,z2,-w)`. Equality of a point with its image is
always checked up to this weighted scaling.

* `s`: if `(z1,z2)≠(0,0)`, the scaling factor must be `1`; hence
  `z0=w=0` and `z1⁶+z2⁶=0`, giving six simple points. If `z1=z2=0`,
  the scaling factor is `-1`; the two points `w=±z0³` above `[1:0:0]`
  are both fixed. Thus `Fix_X(s)` consists of exactly eight points.
* `alpha s:(z0,z1,z2,w)↦(-z0,z1,z2,w)`: away from `[1:0:0]` the
  scaling factor is `1`, so `z0=0` and
  `w²=z1⁶+z2⁶` in `P(1,1,3)`. This is the connected double cover of
  `P¹` branched at six distinct points, of genus two by
  Riemann–Hurwitz. At `[1:0:0]` a scaling by `-1` would require `w=0`,
  contradicting `w²=z0⁶`; no further points occur.
* The base of `beta s` and `alpha beta s` has the real form
  `[z0:z1:z2]=[i u0:u1:u2]`, with real nonzero `u` modulo `u~−u`.
  Over this `RP²`, the sheet coordinate is a section of the real line
  bundle `O(3)_R=gamma^{⊗3}`, where `gamma` is the tautological line.
  Because its degree is odd, `(u,v)~(-u,-v)` and transport around the
  nontrivial loop of `RP²` reverses the sheet sign. This is the global
  line-bundle fact that an affine scalar equation alone would miss.
* For `beta s`, the fixed condition is `w=i v` and
  `v²=u0⁶-u1⁶-u2⁶`. The allowed base lies in the chart `u0=1` and is
  the closed superellipse disk `D_+={u1⁶+u2⁶≤1}`. Its two sheets join
  smoothly along the one boundary oval (locally `v²=t`, with `dt≠0`).
  The branched double of this disk is connected, orientable, and `S²`.
* For `alpha beta s`, the fixed condition is `w=v` and
  `v²=u1⁶+u2⁶-u0⁶`. The allowed base
  `D_-=RP²\int(D_+)` is a Möbius band. On its core `u0=0`, write
  `(u1,u2)=(cos theta,sin theta)` with `theta` modulo `pi`.
  Its two nonzero roots satisfy `(theta,v)~(theta+pi,-v)`, so one
  circuit exchanges the sheets: the branched double is connected.
  Its Euler characteristic is
  `2 chi(D_-)-chi(boundary D_-)=2*0-0=0`. It is orientable because the
  nowhere-zero holomorphic K3 two-form `Omega` can be phased so that
  `(beta s)^*Omega=bar(Omega)` and
  `(alpha beta s)^*Omega=-bar(Omega)`. Consequently `Re(Omega)` on
  `Fix(beta s)` and `Im(Omega)` on `Fix(alpha beta s)` are nonzero real
  area forms. A connected orientable closed surface of Euler zero is `T²`.

For completeness, the three original loci are also visible directly:
`Fix(alpha)` is the branch sextic `C10`; `Fix(beta)` is the connected
unit double cover of `RP²` in the odd real line `O(3)_R`, hence `S²`;
`Fix(alpha beta)` is empty because on real base points its condition
would be `-v²=u0⁶+u1⁶+u2⁶>0`. These agree with the source's Example 7.2.

## B. Residual groups, normal matrices and the local-system sign

Write `e_i=∂/∂x_i` and set `C=Fix_X(alpha)`. The three torus fixed-circle
families, their setwise stabilizers `H` for **one raw connected component**,
and pointwise isotropy `K` are:

| Sector | Fixed torus labels; free axis | `H` | `K` | Residual `H/K` |
| --- | --- | --- | --- | --- |
| `alpha` | `x2,x3∈{0,1/2}`; `x1` | `<alpha,s>` | `<alpha>` | `<s>≅Z2` |
| `beta` | `x1∈{0,1/2}`, `x3∈{1/4,3/4}`; `x2` | `<beta>` | `<beta>` | `1` |
| `beta s` | `x1,x3∈{1/4,3/4}`; `x2` | `<beta s>` | `<beta s>` | `1` |

In the `alpha` family, `beta` swaps `x3=0` and `1/2`, whereas `s`
preserves each circle and translates its `x1` by `1/2`. In either other
family, `alpha` swaps the two `x3` levels and `s` swaps the two `x1`
levels. These permutations prove the stated setwise stabilizers; they also
show the three sector families are mutually disjoint. Every other
nonidentity torus map has a half-translation along a `+1` linear axis,
so it has no fixed point. The three sector involutions act by `-1`
on the complete real four-dimensional normal at each fixed point:

```text
N_alpha  = span_R(e2,e3) ⊕ N_{C/X},          Dalpha|N_alpha = -I4;
N_beta   = span_R(e1,e3) ⊕ N_{S²_beta/X},  Dbeta |N_beta  = -I4;
N_betas  = span_R(e1,e3) ⊕ N_{S²_betas/X}, D(beta s)|N_betas = -I4.
```

For `alpha`, use local charts `z1=1` or `z2=1`, which cover all of `C`.
The normal complex coordinate is `eta=w/z_j³`. The map `s` fixes `z_j`
and sends `eta↦-eta`, while `s_T` fixes `e2,e3`. Thus, between the
normal fibres over `(x,p)` and `(x1+1/2,s_Cp)`, its exact real matrix in
the frame `(e2,e3,n,In)` is `diag(1,1,-1,-1)`. At `beta` and `beta s`
fixed surfaces, the K3 involution preserves the hyperkähler `J` and is
`+1` on its `J`-complex fixed tangent plane, hence `-1` on its `J`-complex
normal line. Their raw-circle residual groups are trivial.

For the **positive comparison form** `phi_JK`, Joyce–Karigiannis's complex
structure on a normal fibre is `I_lambda(v)=u×v`, with
`u=lambda^#/|lambda|`. It is not defined as a Riemannian `G2` cross
product by the frozen split form `phi_+`. With `lambda=dx1` on an
`alpha` representative, and `lambda=dx2` on a `beta` or `beta s`
representative, direct contraction with `phi_JK` gives

```text
alpha:   I_lambda(e2)=e3, I_lambda(e3)=-e2;
         I_lambda(n)=-I n on N_{C/X}.
beta,*s: I_lambda(e3)=e1, I_lambda(e1)=-e3;
         I_lambda(n)=-J n on N_{S²/X}.
```

Thus in the complex coordinates on `N_alpha` determined by this
`I_lambda`, the residual `s` is `diag(1,-1)` and induces
`[z_t:z_X]↦[z_t:-z_X]` on the exceptional `CP¹`. This map is
holomorphic of degree `+1`; its action on `H²(CP¹;Z)` is `+1`.
No residual map acts on an individual `beta` or `beta s` circle.
Transport between distinct raw components does not create a loop in the
quotient: choose one representative component in each transitive orbit.
Therefore the exceptional-class monodromy is **ordinary, not
`Z2`-twisted**, for a resolution using the positive comparison form.

The one-forms descend globally: assign `dx1` to one `alpha` raw
component and transport it by `G` to its paired component (where `beta`
reverses its sign); the only residual map `s` preserves it. Assign
`dx2` similarly on each `beta`/`beta s` orbit; `alpha` may reverse its
sign while exchanging different components, but the setwise stabilizer is
trivial. On the quotient strata these forms are parallel, nowhere zero,
closed and coclosed. This verifies the local one-form gate for `phi_JK`.

## C. Lifted affine deck group and Armstrong gate

Let `Y=R³×X`, simply connected because K3 is simply connected. Write
`T_i(x,p)=(x+e_i,p)` and use the explicit lifts

```text
A(x,p) = (( x1,    -x2,       -x3), alpha p)
B(x,p) = ((-x1,     x2,  1/2 - x3), beta p)
S(x,p) = (( x1+1/2, x2,        x3), s p).
```

The full discrete group `D=<T1,T2,T3,A,B,S>` has the relations

```text
[Ti,Tj]=1; A²=B²=1; S²=T1;
A(T1,T2,T3)A^-1=(T1,T2^-1,T3^-1);
B(T1,T2,T3)B^-1=(T1^-1,T2,T3^-1);
S Ti S^-1=Ti; AS=SA; AB=T3^-1 BA; BS=T1^-1 SB.
```

The following six elements of `D` have literal fixed points in `Y`:

| Element | Torus coordinates of a fixed point | K3 fixed locus |
| --- | --- | --- |
| `A` | `x2=x3=0` | `Fix(alpha)≠empty` |
| `T2 A` | `x2=1/2,x3=0` | `Fix(alpha)≠empty` |
| `T3 A` | `x2=0,x3=1/2` | `Fix(alpha)≠empty` |
| `B` | `x1=0,x3=1/4` | `Fix(beta)≠empty` |
| `T1 B` | `x1=1/2,x3=1/4` | `Fix(beta)≠empty` |
| `B S` | `x1=-1/4,x3=1/4` | `Fix(beta s)≠empty` |

For example, the K3 points `[0:1:e^{i*pi/6}],w=0` for `alpha`, the
point `[1:0:0],w=1` for `beta`, and `[i:0:0],w=i` for `beta s`
make nonemptiness explicit. Products of the fixed-point elements give

```text
T2=(T2 A)A; T3=(T3 A)A; T1=(T1 B)B; S=B(B S).
```

They therefore generate **all** of `D`; its normal subgroup generated by
point-fixing elements is `D` itself. The action is properly discontinuous,
with finite stabilizers, and `Y/D=(T³×X)/G`. Armstrong's theorem now gives
`pi1(Y/D)=D/D=1`. Replacing disjoint `A1` cones by the corresponding
simply connected Eguchi–Hanson fibres does not change `pi1`, by van
Kampen along their `RP³` links. This conclusion is independent of the
three-form sign.

## D. Independent character and topology recomputation

The direct fixed-locus proof gives the H² traces via Lefschetz
`tr(g|H²(X))=chi(Fix_X(g))-2`, in bit order `(alpha,beta,s)`:

```text
g              1  alpha beta alpha*beta s alpha*s beta*s alpha*beta*s
trace H²      22  -20     0      -2       6    -4       0       -2
```

First Fourier-invert only the `alpha,beta` subgroup. Its four character
dimensions `(++, +-, -+, --)` are `(0,1,11,10)`. Separately invert the
four traces `(s,alpha s,beta s,alpha beta s)=(6,-4,0,-2)` to obtain the
trace of `s` on those same sectors: `(0,1,3,2)`. Taking half of
`dimension±trace_s` gives the eight full character multiplicities

```text
character mask (alpha,beta,s)  0 1 2 3 4 5 6 7
H² multiplicity                0 7 1 6 0 4 0 4.
```

The torus `H¹` characters are `(2,1,3)` for `(dx1,dx2,dx3)` and are
pairwise distinct, nontrivial, with xor zero. Künneth over `Q` then gives

```text
b1(M') = 0;
b2(M') = m0 + dim(Λ²H¹(T³))^G = 0;
b3(M') = dim(Λ³H¹(T³))^G + m2+m1+m3 = 1+1+7+6 = 15.
```

The remaining invariant dimensions are independently
`b4=1+m3+m1+m2=15`, `b5=m0+0=0`, `b6=0`, `b7=1`. Hence the full rational
orbifold vector is `(1,0,0,15,15,0,0,1)`, satisfying Poincaré duality
and Euler characteristic zero. Burnside supplies a separate Euler check:
the identity fixed set contains a `T³` factor, and every nonempty other
fixed set contains a circle; each has Euler characteristic zero, so
`chi(M')=|G|^-1 sum_g chi(Fix(g))=0`.

For the stratum count, the four raw `alpha` circles form two orbits.
The `s` restriction on `C10` fixes its six points with `z0=0`; the
Riemann–Hurwitz equation
`18=2(2g(C10/s)-2)+6` gives `g(C10/s)=4`.
Each `alpha` quotient stratum is a mapping torus of `s_C`, hence has
`b1=1+dim H¹(C10)^s=1+2*4=9`. Each `beta` and `beta s` four-circle
family is one orbit with no residual quotient, contributing one
`S¹×S²` with `b1=1`. Thus `b0(L)=2+1+1=4` and
`b1(L)=2*9+1+1=20`. These oriented closed threefolds also have
`(b0,b1,b2,b3)(L)=(4,20,20,4)` by Poincaré duality and `chi(L)=0`.

The ordinary exceptional-class sign computed in B yields, for the
associated smooth topological `A1` resolution,

```text
b_k(N_top)=b_k(M')+b_{k-2}(L),
(b0,...,b7)(N_top)=(1,0,4,35,35,4,0,1).
```

Both Poincaré duality and `chi(N_top)=1+4-35+35-4-1=0` check this
vector. The pair `(b2,b3)=(4,35)` is therefore a **topological A1
resolution calculation**. Its promotion to the Betti vector of a
Joyce–Karigiannis torsion-free `G2` manifold requires a positive input
three-form, which the frozen displayed `phi_+` does not supply.

## E. Claim adjudication

| Claim | Gate | Exact evidence |
| --- | --- | --- |
| Product `G2` action of the frozen maps | **PASS** | Their paired torus/K3 characters preserve the positive `phi_JK` with the same `alpha,beta,s` and affine maps. |
| Frozen displayed product form | **FAIL** | The preregistered `phi_+` has signature `(3,4)` and cannot be the asserted Riemannian `G2` form. |
| K3 fixed loci | **PASS** | Weighted scaling and the real `O(3)` line show `8 points`, `C2`, `S²`, `T²` for `s,alpha s,beta s,alpha beta s`. |
| Disjoint `A1` strata | **PASS** | Only `alpha,beta,beta s` have torus fixed circles; their families are disjoint and each point isotropy acts as `-I4`. |
| Local-system sign | **PASS** | The sole residual map on an `alpha` circle is complex-linear `diag(1,-1)` for positive `phi_JK`, giving degree `+1` on exceptional `CP¹`; other residual groups are trivial. The resulting class system is ordinary if JK is applied. |
| Quotient Betti | **PASS** | Independent Fourier/Künneth gives `(b1,b2,b3)=(0,0,15)` and full vector `(1,0,0,15,15,0,0,1)`. |
| Stratum Betti | **PASS** | Two mapping tori with `b1=9` each and two `S¹×S²` with `b1=1` each give `(b0,b1)=(4,20)`. |
| `pi1` | **PASS** | Six displayed fixed-point lifts generate all `T1,T2,T3,A,B,S`; Armstrong gives `pi1(M')=1`, preserved by an `A1` resolution. |
| Joyce–Karigiannis hypotheses for frozen F2 | **FAIL** | §6.5 requires a torsion-free *Riemannian* `G2` orbifold; frozen `phi_+` is split, despite the local `A1` and one-form gates passing for `phi_JK`. |
| Resolved Betti as a JK `G2` output | **HOLD** | Ordinary exceptional-class monodromy yields `(0,4,35)` for a smooth topological `A1` resolution, but the frozen JK existence claim is not established. |
| Full holonomy | **HOLD** | `pi1=1` would imply full `G2` after a valid JK construction; the frozen `phi_+` cannot enter that theorem. |

Because a required analytic gate fails, **F2 at `f9d92ad` is not
ratified** as a geometry benchmark or positive control. The exact maps,
fixed loci, and target-blind Betti arithmetic remain available as
audited data. A sign-corrected product form can be evaluated under an
explicitly separate erratum/freeze decision; this audit makes no such
change and makes no K7-GEO-JK-F1 or K7-P2 identification.
