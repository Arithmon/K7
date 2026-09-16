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
