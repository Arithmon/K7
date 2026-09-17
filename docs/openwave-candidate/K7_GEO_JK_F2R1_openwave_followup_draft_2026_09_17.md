# Draft follow-up to OpenWave after the F2R1 audit

**Status:** internal draft for Brieuc to edit and send in his own voice. No
external message or OpenWave application has been made from this file.

## Proposed message

Following your recommendation to freeze before auditing, our selected
K7-GEO-JK-F1 geometry proposal failed its post-freeze cohomology and stabilizer
checks. We kept that failure in the record. We then preregistered a
distinct, target-blind Joyce–Karigiannis product-action candidate, F2, at
[`f9d92ad`](https://github.com/Arithmon/K7/commit/f9d92ada6e7de7a7dd76f17ca88900ea5b054bd1).
Its adversarial audit at
[`f69ef8c`](https://github.com/Arithmon/K7/commit/f69ef8c2ddd329b394ec88ec51b1ad8f094b42a4)
refuted the displayed product \(G_2\) form at Gate 0: the plus sign gave a
split metric.

We froze the sign correction under a new identifier, K7-GEO-JK-F2R1, at
[`bfc1db0`](https://github.com/Arithmon/K7/commit/bfc1db056f4ed63311dca059d7f708bc70e2299c),
without changing the involutions, affine torus action, K3 fixed loci or
Betti data. A fresh independent audit at
[`2ce2193`](https://github.com/Arithmon/K7/blob/2ce2193b8a47ec8f7cb1bf241e35571952762d42/docs/openwave-candidate/K7_GEO_JK_F2R1_ratification_audit_2026_09_17.md)
passes the positivity, invariance, normal-complex-structure, local-system
and Joyce–Karigiannis resolution gates. The resulting theorem-backed
compact simply connected full-holonomy \(G_2\) example has
\((b_2,b_3)=(4,35)\). Its finite group and cohomology calculations have
an executable checker; the torsion-free metric is supplied by the
Joyce–Karigiannis existence theorem, not a numerical metric solver.

F2R1 is a geometry benchmark and positive control. It is not our
selected F1 geometry, a K7-P2 physical prediction, a closed spectral
problem producing an observable, or an earned OpenWave criterion cell.
Does this audited benchmark change your assessment of K7's route toward
a closed Tier-3 static/spectral system, or is an observable-producing
spectral problem still the prerequisite you would want to see?

## Evidence and scope for the author

- The complete chain is retained: F1 failure; F2 preregistration
  `f9d92ad`; F2 Gate 0 refutation `f69ef8c`; F2R1 sign-only freeze
  `bfc1db0`; independent ratification `2ce2193`. None is squashed into
  another.
- The F2R1 [freeze](K7_GEO_JK_F2R1_sign_erratum_freeze_2026_09_17.md)
  and [ratification](K7_GEO_JK_F2R1_ratification_audit_2026_09_17.md)
  give the full mathematical evidence and claim-level verdicts.
- OpenWave's [onboarding guide](https://github.com/openwave-labs/openwave/blob/main/ONBOARDING_MODELS.md)
  describes Tier 3 as a spectral/eigenvalue problem yielding static
  observables; its model-fit scorecard also asks for a genuine physical
  prediction. The [AI hygiene guide](https://github.com/openwave-labs/openwave/blob/main/AI_HYGIENE.md)
  asks the author to own outbound scientific prose and for substantive
  claims to receive adversarial review.
