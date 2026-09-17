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

An expanded audit over four repeated first-step classes (two exact lifts each)
found the same pattern: class 1 remains the only observed continuation split
(`204` versus `208`), while classes 0, 2, and 3 have equal continuation sets.
One additional class has an ambiguity at `k=2` despite equal continuation
sets; all four classes are separated by `k=3` (modulo 8). This strengthens the
empirical status of mod 8 as a sufficient state descriptor for this bounded
sample, but does not establish it globally.

The exact-state audit now canonically encodes the primitive embedded
`M^+(t),M^-(t)` column lattices (HNF) and their inclusion index in `M`.
Identical exact states have identical continuation sets in the tested sample.
However, two distinct exact states in the same mod-2 class had continuation
sets of sizes `204` and `208`. State reductions had ambiguity counts
`k=1..5: [1,1,0,0,0]`: mod 2 and mod 4 are insufficient, while mod 8, mod
16, and mod 32 separate all tested continuation classes. This makes mod 8 a
strong empirical candidate, not a proved exhaustive reduction.

These results concern the bounded LLL-generated parameter box only. They do
not identify it with the intrinsic set of all Eichler parameters or all of
`O(M)`; those must remain separate scopes.

The first-step collision hunt recorded `11,616` states and `5,664` mod-8
classes over two structured bases. Its original zero-collision line inspected
only the first 20 repeated classes by default, so exhaustion was **not**
established. No second step was computed there; this is a state-collision
audit, not a continuation search. The initial straight SymPy loop was stopped
after three bases because it scaled poorly; the optimized coordinate-level
census is recorded below.

The coordinate-level census was subsequently optimized by forming `t₁|_M`
directly from the Eichler formula. The recorded 24-base run produced `139,392`
raw first-step states and `67,968` distinct mod-8 fingerprints. The checker
at `3f6f01a` inspected only its first 20 repeated-fingerprint classes unless
given a larger `--collision-limit`; its printed zero therefore did **not**
establish injectivity across all classes. The checker now compares exact
involution matrices in every class and asserts the required action gates, but
the 24-base run has not been repeated with that repaired checker. Injectivity
of the full bounded first-step sample is **HOLD** pending that run. No
descendants were generated, and continuation completeness remains open even
if first-step injectivity is confirmed. See the post-freeze cohomology audit
for the independent geometry blocker.

The modular prefilter was then run on two bases and sixteen first twists per
base (`180,048` two-step candidates). It reproduced the same phenomenon: no
`(7,9,9,9)`, while profiles with a `7` retained an `11`. This is still a
scoped mod-2 observation; exact primitive fixed-lattice invariants remain the
acceptance gate for any future hit.
