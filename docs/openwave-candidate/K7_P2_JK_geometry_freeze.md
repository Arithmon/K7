# K7-GEO-JK-F1 — Joyce–Karigiannis geometry target freeze

**STATUS: FROZEN GEOMETRY TARGET — NO-REVISION RULE**

**Freeze identifier:** `K7-GEO-JK-F1`  
**Freeze date:** 2026-09-16  
**Repository:** `Arithmon/K7`  
**Starting branch:** `main`  
**Starting SHA:** `cc03b63c182ae4820ac7d5d3c4acc0057842368e`  
**Purpose:** freeze the selected Joyce–Karigiannis geometry package before
any further rho17 search.

This document is a provenance boundary. It records the geometry target as it
stood before the next search. A later success, failure, or change of method
cannot silently redefine this target.

## Source of the historical fixed-locus package

The source of record is:

```text
publications/papers/markdown/k7_framework_3_5_S1_foundations.md
§8.4 Joyce-Karigiannis Z₂³ Construction, realizes (b₂, b₃) = (21, 77)
Arithmon/K7 @ cc03b63c182ae4820ac7d5d3c4acc0057842368e
```

The source states the JK resolution formula

```text
b₂(N) = b₂(T³ × K3 / G) + b₀(fixed loci)
b₃(N) = b₃(T³ × K3 / G) + b₁(fixed loci)
```

and transcribes the following fixed-locus accounting table:

| Component | Count | b₀ | b₁ | Source role |
| --- | ---: | ---: | ---: | --- |
| `T³` | 12 | 12 | 36 | V4-fixed K3 points (Phase 1) |
| `S¹×Σ₂` | 1 | 1 | 5 | `τ`, `(g,k)=(2,2)` |
| `S¹×CP¹` | 2 | 2 | 2 | `τ`, the two rational curves |
| `S¹×T²` | 3 | 3 | 9 | `s₁τ`, `s₂τ`, `s₁s₂τ`, `(g,k)=(1,1)` |
| `S¹×CP¹` | 3 | 3 | 3 | `s₁τ`, `s₂τ`, `s₁s₂τ`, the rational curves |
| **Total** | **21** | **21** | **55** | |

The source further gives quotient cohomology
`b₂(T³×K3/G)=0`, `b₃(T³×K3/G)=22`. Independently summing the table:

```text
b₀(fixed loci) = 12 + 1 + 2 + 3 + 3 = 21
b₁(fixed loci) = 36 + 5 + 2 + 9 + 3 = 55
b₂(N) = 0 + 21 = 21
b₃(N) = 22 + 55 = 77
```

This verifies the selected pair `(b₂,b₃)=(21,77)` from the source's own
decomposition. The table does not supply a canonical naming of the three
symplectic generators beyond `s₁,s₂,s₁s₂`; identifying those labels with
`sigma_A,sigma_B,sigma_A sigma_B` is only a harmless generator relabelling.
No finer assignment may be invented from this source.

## FROZEN CHOICES

### Selected topology

```text
b₂(K₇) = 21
b₃(K₇) = 77
```

These are selected structural inputs / selected topology in the current K7
program. This freeze does not claim that they were independently predicted by
the current construction. Changing either number creates a new geometry
package, rather than continuing `K7-GEO-JK-F1`.

### Group and roles

```text
G = <tau, sigma_A, sigma_B> ~= (Z/2)^3
```

The three nonidentity elements of the symplectic subgroup

```text
sigma_A, sigma_B, sigma_A*sigma_B
```

are symplectic. The anti-symplectic coset is

```text
tau, tau*sigma_A, tau*sigma_B, tau*sigma_A*sigma_B.
```

Exchanging `sigma_A` and `sigma_B` is a harmless generator relabelling. The
symplectic versus anti-symplectic coset, and the multiplicities of the fixed
locus types below, are frozen.

### Nikulin package

```text
tau                    : (r,a,delta) = (11,7,1)
tau*sigma_A            : (r,a,delta) = (11,9,1)
tau*sigma_B            : (r,a,delta) = (11,9,1)
tau*sigma_A*sigma_B    : (r,a,delta) = (11,9,1)
```

The standard non-exceptional formulas give

```text
(11,7,1) -> (g,k) = ((22-11-7)/2, (11-7)/2) = (2,2)
(11,9,1) -> (g,k) = ((22-11-9)/2, (11-9)/2) = (1,1)
```

Thus every one of the four anti-symplectic fixed loci has Euler characteristic

```text
χ = (2-2g) + 2k = 2.
```

This is a verification of the frozen types, not a route for changing them.

### H² character

In the fixed order

```text
(1, tau, sigma_A, sigma_B,
 tau*sigma_A, tau*sigma_B, sigma_A*sigma_B, tau*sigma_A*sigma_B)
```

the frozen H² character is

```text
(22, 0, 6, 6, 0, 0, 6, 0).
```

The symplectic entries are `6` because an order-two symplectic K3
automorphism has eight isolated fixed points and Lefschetz trace `8-2=6`.
The four anti-symplectic entries are `χ(fixed locus)-2=0`. This character is a
mathematical consequence of the frozen fixed-locus package, not an additional
tunable target.

## DERIVED CONSEQUENCES

### Picard rank bound and first search rank

Fourier inversion of the above H² character, with `V4` acting trivially on the
transcendental lattice and `tau` acting by `-1`, gives for the tau-only NS
character

```text
m_tau = rho - 17.
```

Therefore the frozen package requires `rho >= 17`. The value `rho=17` is the
minimal admissible rank and the first search target; it is not independently
predicted. Values `rho=18,19,...` remain within this freeze when the complete
package above is unchanged.

At `rho=17`, `rank(T_X)=22-17=5`, and the NS character multiplicities in the
same eight-character order are

```text
(5,0,2,2,2,2,2,2).
```

The rank checks are explicit:

```text
rank(NS^tau) = 5 + 2 + 2 + 2 = 11
rank(H²^V4) = (22 + 6 + 6 + 6)/4 = 10
rank(each nontrivial V4 sector) = (22 - 6 - 6 + 6)/4 = 4
```

The rank-five transcendental lattice lies entirely in the tau-only rational
character. These are consequences of the frozen character, not choices.

### Standard symplectic V4 lattice

The existing integral backend derives, rather than freezes, the following:

```text
M = Lambda_K3^V4       rank 10, signature (3,7)
Omega = M^perp         rank 12, signature (0,12)
```

The three nontrivial rational `V4` sectors have dimensions `4+4+4`. Their
integral sector lattices are each `D4(-2)` and

```text
D4(-2)^3 ⊂ Omega
[Omega : D4(-2)^3] = 16
Omega / D4(-2)^3 ~= (Z/2)^4.
```

The standard backend also supplies the explicit discriminant anti-isometry
`phi : A_M -> A_Omega`. A basis, glue coordinate system, or Smith normal form
is a representation choice, not frozen physical input. The general matching
condition is

```text
phi o tau_Mbar = tau_Omegabar o phi.
```

## SEARCH DEGREES OF FREEDOM

The following moves preserve `K7-GEO-JK-F1`:

- change of lattice basis, normal form, or explicit embedding in `Lambda_K3`;
- independent implementations and improved exact arithmetic;
- additional discriminant-action fibres and classification of `O(M)->O(q_M)`;
- root reflections, Eichler transvections, products and compositions;
- non-orthogonal constructions and recomputation of eigenspaces after twists;
- searches outside the current block-diagonal `M` family;
- increasing `rho` above 17 while retaining the exact frozen package;
- a different explicit K3 construction carrying the same frozen action;
- a proof that the frozen package is impossible.

These are search or representation freedoms. They cannot change the target
roles, types, multiplicities, or selected topology.

## OPEN GEOMETRIC GATES

The freeze does not assert any of the following:

- an exact integral `tau` with fixed types `(11,7,1)+(11,9,1)^3`;
- Hodge realization at Picard rank exactly 17;
- a `G`-stable ample/Kähler chamber or Global Torelli automorphisms;
- a primitive ample invariant class of square 8;
- a primitive nef invariant isotropic class and section;
- an explicit projective degree-8 K3 carrying the full action;
- global Joyce–Karigiannis/K7 gluing or a closed runnable `G₂` object;
- a heterotic dictionary, neutrino operator, or K7-P2 observable.

The current semantic outcome is `HOLD`: searched families may fail while the
full mathematical search space remains open. `HOLD` must not be promoted to
`NO-GO` without a theorem or genuinely exhaustive classification.

## REVISION TRIGGERS

Any of the following requires a new geometry identifier, for example
`K7-GEO-JK-F2`, rather than continuation under `F1`:

1. changing `b₂=21` or `b₃=77`;
2. replacing the historical fixed-locus decomposition after seeing a result;
3. replacing `(11,7,1)` or any of the three `(11,9,1)` types;
4. introducing a free involution into an anti-symplectic slot frozen as
   non-free;
5. changing the `1+3` multiplicity of the two anti-symplectic types;
6. changing which group-element class is symplectic versus anti-symplectic;
7. modifying the group away from the frozen `(Z/2)^3` package to rescue it;
8. retroactively changing the interpretation of historical source material;
9. selecting a new topology or fixed-locus assignment because `F1` has no
   realization.

A revision may be scientifically legitimate. It simply cannot inherit the
provenance of `K7-GEO-JK-F1`.

## OUTCOME SEMANTICS

- **PASS:** an exact integral action realizes the frozen package. This unlocks
  Hodge, ample-cone, polarization and elliptic gates; it does not yet prove
  geometric K3 automorphisms or K7.
- **NO-GO:** a theorem or genuinely exhaustive classification excludes the
  frozen package in the stated scope. Preserve the failure; do not alter F1.
- **HOLD:** searched families fail but the complete mathematical space is not
  closed. This is the current status.

## Provenance rule for subsequent work

Every post-freeze rho17 or higher-rank search note must cite the freeze commit
SHA and retain the exact roles and types above. The first post-freeze scientific
result must be committed separately from this document. No neutrino target or
experimental central value is part of this geometry freeze.
