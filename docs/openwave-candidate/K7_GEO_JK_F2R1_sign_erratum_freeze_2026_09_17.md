# K7-GEO-JK-F2R1 — sign erratum freeze

**Status:** FROZEN CANDIDATE, NOT YET RATIFIED

**Date:** 2026-09-17

**Parent preregistration:** `K7-GEO-JK-F2 @ f9d92ada6e7de7a7dd76f17ca88900ea5b054bd1`

**Refuting audit:** `f69ef8c2ddd329b394ec88ec51b1ad8f094b42a4`,
[`K7_P2_JK_F2_ratification_audit_2026_09_17.md`](K7_P2_JK_F2_ratification_audit_2026_09_17.md).

**Freeze rule:** this new identifier records exactly one geometric correction
to F2, before its own independent audit. `f9d92ad` and `f69ef8c` remain
unaltered in the history. Any further change to the action, fixed loci,
Betti package, or product form requires a later identifier and a fresh
audit. The commit first adding this file is the F2R1 preregistration point;
the next audit must cite its exact SHA.

## Why this is a new artefact

The original F2 audit's Gate 0 **failed**. With conventional positive
hyperkähler Kähler forms, its displayed

```text
phi_+ = e123 + e1∧omega_I + e2∧omega_J + e3∧omega_K
```

induces a split metric of signature `(3,4)`, not a Riemannian `G2`
metric. Therefore the Joyce–Karigiannis existence theorem could not
ratify the original F2 as written. F2R1 is a separately frozen,
target-blind sign erratum, not a retrospective rewrite of F2.

The **only correction** is the product three-form:

```text
phi_F2R1 = phi_JK
          = e123 - e1∧omega_I - e2∧omega_J - e3∧omega_K.
```

This is exactly the positive product convention in
[Joyce–Karigiannis, equation (2.13)](https://arxiv.org/pdf/1707.09325).
It changes no automorphism, affine torus map, K3 fixed locus, quotient
stratum, or preregistered Betti number.

## Frozen inherited data, unchanged from F2

The K3 is the weighted double plane
`X={w²=z0⁶+z1⁶+z2⁶}⊂P(1,1,1,3)`. Its three generators remain

```text
alpha([z0,z1,z2],w) = ([z0,z1,z2],-w)
beta ([z0,z1,z2],w) = ([bar(z0),bar(z1),bar(z2)],bar(w))
s    ([z0,z1,z2],w) = ([-z0,z1,z2],-w).
```

On `T³=R³/Z³` the affine generators remain

```text
alpha_T(x1,x2,x3) = ( x1,     -x2,       -x3)
beta_T (x1,x2,x3) = (-x1,      x2, 1/2 - x3)
s_T    (x1,x2,x3) = ( x1+1/2,  x2,         x3).
```

The seven nontrivial K3 fixed-locus claims remain, in the order
`alpha,beta,alpha beta,s,alpha s,beta s,alpha beta s`:

```text
C10, S², empty, eight points, C2, S², T².
```

The unchanged numerical claims are

```text
(b1,b2,b3)((T³×X)/G) = (0,0,15),
(b0,b1)(singular L)  = (4,20),
(b1,b2,b3)(resolved N) = (0,4,35).
```

These are frozen **claims to recheck**, not declared consequences of
the sign change without audit. The F2R1 audit must independently test
positivity of `phi_JK`, invariance under each generator, the
`I_lambda` and exceptional-class signs, the hypotheses of §6.5, and
the unchanged topology. Ratification and full-holonomy status remain
open until that audit is committed.

F2R1 is a possible **distinct geometry benchmark / positive control**.
It is not `K7-GEO-JK-F1`, does not reproduce the selected `(21,77)`,
and is not a `K7-P2` physical prediction.
