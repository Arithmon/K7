# Post-freeze composition audit

**Freeze:** `K7-GEO-JK-F1` @ `629e87ef968f2b126b7ca4a1fa89a81ccedf2fa4`  
**Experiment:** two compatible bases, eight first twists per base, coefficient
box `[-1,1]`; second twists generated from the recomputed eigenspaces.

The run tested `75,504` integral candidates surviving the involution,
commutation, trace, and isometry filters. The first-step mod-2 profiles were
only

```text
(9,9,9,11), (9,9,11,9), (9,11,9,9), (11,9,9,9).
```

The final profiles included `(11,9,9,9)` and profiles with a `7`, but no
`(7,9,9,9)`. In this sample every profile containing `7` also retained an
`11`; conversely the simultaneous three `9`s retained the special `11` slot.
This is a structural lead, not a theorem: the experiment covers neither all
24 compatible bases nor all compositions or all of `O(M)`.

The useful conjecture to test next is therefore:

> For the presently generated successive-Eichler class, at least one
> anti-symplectic slot has `a=11`; a `7` can appear only together with that
> `11`.

The next implementation should test this invariant with a larger, modular
prefiltered sample before attempting exact fixed-lattice SNF. A failure would
be more informative than simply increasing depth: it would identify the first
construction class escaping the observed constraint.

After deduplication, one base yielded `5808` raw first twists but only `230`
distinct actions modulo 2. Second-step generation produced `204--233`
distinct modulo-2 actions from `3388--4840` raw parameter choices. A width
sample over four bases, two first-step classes per base (`1632` candidates),
again produced no `(7,9,9,9)` and retained the same one-`11` pattern. This
supports quotienting by modular actions before any wider search, without being
an exhaustion or a no-go theorem.

The continuation-completeness test found a counterexample to naive mod-2
quotienting: two exact lifts of one first-step mod-2 class produced second-step
sets of sizes `204` and `208`, with symmetric difference `152`. Their fixed
eigensublattices had identical Gram SNF, determinant, and plus/minus index;
their `t_1|_M` matrices agreed modulo `4` but differed modulo `8` (hashes
`bf55099b5bc5e2e0` and `617126b26893fb0a`). Thus mod 2, and even the tested
coarse integral invariants, are not continuation-complete. The minimal
invariant is not identified yet; the mod-8 action/eigensublattice embedding is
the next candidate to test.

The modular prefilter was then run on two bases and sixteen first twists per
base (`180,048` two-step candidates). It reproduced the same phenomenon: no
`(7,9,9,9)`, while profiles with a `7` retained an `11`. This is still a
scoped mod-2 observation; exact primitive fixed-lattice invariants remain the
acceptance gate for any future hit.
