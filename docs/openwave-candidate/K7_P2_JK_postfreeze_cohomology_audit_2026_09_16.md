# Post-freeze JK quotient-cohomology audit

**Date:** 2026-09-16

**Target:** `codex/k7-geometry-freeze-rho17 @ 3f6f01ae326178761222ddfc9d066830abc35c84`

**Frozen target:** `K7-GEO-JK-F1 @ 629e87ef968f2b126b7ca4a1fa89a81ccedf2fa4`

**Corpus:** the frozen character and fixed-locus table; §8.4 of
`publications/papers/markdown/k7_framework_3_5_S1_foundations.md` at
`cc03b63c182ae4820ac7d5d3c4acc0057842368e`; and the live post-freeze
composition audit and its reproducer. This note does not revise F1.

## Claim verdicts

| Claim | Verdict | Reason |
| --- | --- | --- |
| F1's selected `(b2,b3)=(21,77)` and fixed-locus types remain recorded without revision | GO as provenance | This audit does not change the frozen choices. |
| The stated diagonal `T³×K3/G` has quotient Betti pair `(0,22)` | **REQUEST CHANGES — BLOCKER** | Its frozen K3 `H²` character forces quotient `b2>=5` and `b3<=16`, for every three-character torus action. |
| The fixed-locus table plus the quoted resolution formula establishes `(21,77)` | **HOLD — BLOCKER** | If the table contributes `(21,55)` as stated, the same formula instead gives `b2>=26` and `b3<=71`. |
| The 24-base mod-8 census establishes injectivity on all `67,968` fingerprints | **HOLD — HIGH** | The checker at the target commit inspected only the first 20 repeated fingerprints by default; the repaired checker has not run on 24 bases. |
| A rho17 integral action or K7-P2 physical observable has been obtained | HOLD | Neither follows from this audit or the bounded lattice searches. |

## BLOCKER: quotient cohomology contradicts the frozen character

Section 8.4 explicitly places `G` inside `Aut(T³) × Aut(K3)`, so its action on
the product is diagonal. For a finite group, ordinary rational cohomology of
the quotient is the invariant part of the cover's cohomology, even when the
action has fixed points. One way to see this is to use the Borel construction:
the map to the orbit space has fibres `BG_x`, which are rationally acyclic for
finite stabilizers, while averaging makes the invariants functor exact over
`Q`. The claim concerns ordinary quotient cohomology, before resolution.

Encode `G=(Z/2)^3` by bits `(tau,sigma_A,sigma_B)`. Fourier inversion of F1's
frozen `H²(K3)` trace `(22,0,6,6,0,0,6,0)` gives multiplicities

```text
character  (trivial, tau-only, remaining six)
m          (5,       5,        2 each)
```

In particular, `dim H²(K3;Q)^G=5`, independently corroborated by the existing
JK character gate. Let `W=H¹(T³;Q)=chi_x ⊕ chi_y ⊕ chi_z`. Every rational
representation of this exponent-two group splits into such characters. As
`H¹(K3)=H³(K3)=0`, Künneth gives

```text
H²(T³×K3) = Λ²W ⊕ H²(K3)
H³(T³×K3) = Λ³W ⊕ (W ⊗ H²(K3)).

b2(T³×K3/G) = 5 + #{i<j : chi_i=chi_j}                  >= 5
b3(T³×K3/G) = 1_{x xor y xor z = 0} + m_x + m_y + m_z <= 16.
```

Thus `(0,22)` is impossible for **every** diagonal torus action compatible
with the frozen K3 character. This is an internal contradiction, before the
open integral-action, Hodge, Torelli, or analytic gates. The independent
stdlib-only checker
`python3 docs/openwave-candidate/check_k3_jk_quotient_cohomology.py`
enumerates all `8³=512` ordered torus-character triples and asserts both
bounds. It contains no neutrino or measured-physics target.

The source and F1 give fixed-locus contributions `(b0,b1)=(21,55)`. If their
resolution formula and that component accounting are retained, the resolved
Betti numbers obey `b2>=5+21=26` and `b3<=16+55=71`, so they cannot be
`(21,77)`. The exact corrected Betti pair needs the actual torus action and a
checked singular-orbit/component calculation. This audit does **not** prove
that all JK constructions, or the selected pair by another route, are
impossible.

**Remedy:** compute the torus representation and ordinary quotient Betti
numbers directly from one fully specified product action, then independently
audit the singular components and the resolution formula. Preserve F1 as a
historical target. Any alteration of its topology or fixed-locus package
requires a new freeze identifier under F1's no-revision rule. Do not promote
the current arithmetic closure as a realized K7 geometry.

## HIGH: the latest mod-8 census gate is narrower than its conclusion

At target commit `3f6f01a`, `check_k3_rho17_eichler_mod8_collisions.py` defaults to
`--matches 4 --collision-limit 20` and slices the repeated-fingerprint list
to `[:args.collision_limit]`. The `139,392` raw states and `67,968` mod-8
fingerprints recorded for 24 bases do not establish that **every** repeated
fingerprint has one exact embedded state. The zero printed by that default
run covers only its first 20 repeated fingerprints. No full-coverage
command, checked-class count, or asserted gate accompanies the claim.
The earlier two-base zero-collision sentence had the same coverage gap.

Two exact involutions on `M` with the same embedded primitive `+1` and `-1`
eigensublattices have the same rational eigenspace decomposition and hence the
same matrix. A complete collision gate can therefore stream the exact
`t1|M` matrix key for **every** mod-8 fingerprint, count all fingerprints
with more than one exact key, and assert that each generated `t1|M` is an
integral trace-zero isometric involution. HNF can be kept for a diagnostic
collision, without limiting the exhaustiveness of the gate. The checker was
repaired in this post-audit branch: `--collision-limit` now limits diagnostic
printing only, all repeated classes are checked, and generated actions must
pass integral trace-zero involution and isometry assertions. A synthetic
positive/negative collision check is reproducible with
`python3 docs/openwave-candidate/check_k3_rho17_eichler_mod8_collisions.py --self-test`
when the project's NumPy/SymPy libraries are on `PYTHONPATH`; it prints
`positive/negative mod8 collision gate: PASS`. The full 24-base run has **not**
been repeated, so the injectivity claim remains HOLD. Even a passing full run
would say nothing about continuation completeness or intrinsic Eichler
parameters.

## Concrete NEXT

1. Put the quotient-cohomology check before further attempts to certify the
   F1 Betti pair or to present the rho17 action as a K7-P2 geometry route.
2. Audit one actual `G` action on `T³×K3`, including torus characters,
   stabilizer orbits, component topology, and the exact resolution formula.
3. Run the repaired mod-8 collision gate with `--matches 24 --bound 1` before
   citing its 24-base injectivity claim. Retain the current `HOLD` on integral
   action and on mod-8 continuation completeness.

**Follow-up:** `K7_P2_JK_torus_action_and_strata_audit_2026_09_16.md`
specifies the forced product-form torus representation and checks the
full-group singular-stratum bookkeeping. Its ordinary quotient Betti triple
is exactly `(1,6,16)` under those product-action hypotheses.
