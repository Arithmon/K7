# Source reconciliation and next work

Baseline: the full SHA is in SOURCE_FREEZE.json. The original skeleton,
unchanged, is in sources/original_skeleton.md. Sources A and B remain
untouched, and their notebooks/results are designated **legacy snapshots
March 2026** in the freeze and LEGACY_SNAPSHOTS.md.

## Blocking findings

1. **NK inverse and codomain.** A finite-dimensional derivative cannot be
   an isomorphism onto the stated C0 codomain. No finite square residual,
   gauge fixing, norm or certified inverse is supplied. Remedy: specify
   the actual residual and a posteriori theorem before computing beta.
2. **False polynomial closure.** Softplus and determinant normalization
   occur in both executable reconstructions. A finite DCT of sampled
   torsion is not a bound on the continuous nonlinear function without
   remainder and rounding bounds. Remedy: validated nonlinear evaluation
   or a proved analytic tail estimate.
3. **Different input metrics.** B's embedded COEFFS equals A's BASE_COEFFS,
   not OPT_COEFFS. The projection freezes A's embedded optimized tensor.
   Its canonical input includes gamma, normalization and domain as well
   as coefficients. The new scalar result must not be described as a
   numerical reproduction on the same metric as B.
4. **21 and 77 are selected inputs.** B forces a true check for 21, and
   supplies 14635 as a fallback; it computes 77 by adding prescribed
   dimensions. Remedy: explicit end maps, bases, ranks, kernel and
   completeness proof. Product cohomology alone gives different ranks.
5. **Adiabatic proof absent.** The historical triangle estimate rounds
   an upper bound down; a metric condition number alone does not prove
   the asserted Hodge-operator perturbation estimate. Remedy: global
   form comparisons and a certified relation to g*.
6. **KK geometry mismatch.** The six-integer fibre model treats K3 as
   a flat periodic four-dimensional factor. Archived counts also differ
   from the manuscript count. Remedy: an actual K3 spectral input and
   certified omitted-mode lower bounds.
7. **Intersection signature mismatch.** The archived numerical recipe
   has exact rational inertia (6,15), not (3,18), because the blocks
   duplicate positive directions. Remedy: a matching-selected basis
   with its lattice embedding and exact Gram matrix.

## Recomputed, bounded work

The executable suite reconstructs the selected metric, computes a
deterministic scalar N-sweep with correct Neumann endpoint masses,
fits N(lambda) rather than the inverse index law, solves radial profiles
by Chebyshev collocation, checks the restricted one-form sector,
reconstructs the old matrix in exact arithmetic, and encloses the first
positive reduced scalar eigenvalue by interval/min-max comparison.
Live values and hashes are in CLAIMS_MANIFEST.json and ARTIFACT_MAP.md.

These are projections of the frozen coordinate model. In particular,
neither the new enclosure nor small profile residuals closes NK or the
global Hodge matching problem.

## NEXT, in the requested order

1. Source freeze: implemented; changes require a deliberate new freeze.
2. NK: obtain/define the square residual, gauge, norm and K3 input; prove
   the inverse bridge and continuous residual bounds. PENDING.
3. Matching: supply both restriction maps and the global complex. PENDING.
4. Adiabatic transfer: prove the full metric quadratic-form comparison. PENDING.
5. Scalar/Weyl: fresh reduced numerical data implemented.
6. KK: obtain K3 spectral data and all omitted-index lower bounds. PENDING.
7. Profiles: deterministic scalar interpolation implemented; global lifts PENDING.
8. Democracy: selected product one-form theorem; projected numerical check.
9. Lambda-one: reduced interval enclosure implemented and independently
   checked at higher precision; transfer to g* PENDING.
10. Manuscript: cautious draft generated from manifest; final abstract,
    conclusion and submission tag remain blocked by submission-check.

There is no dummy certificate, fabricated matching map or synthetic K3
tower used to make an unresolved gate green.
