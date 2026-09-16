# Prospective prediction registry

## Rule for the `K7-Pn` namespace

A `K7-Pn` entry exists only when all load-bearing choices are frozen before the future comparison is used:

- source commit;
- structural inputs;
- physical observable map;
- operator basis;
- normalization;
- scheme and scale where applicable;
- branch / sign conventions;
- dimensional anchors, if any;
- executable assembly;
- numerical value;
- experiment / data release that will test it;
- falsification rule;
- no-revision rule.

If any load-bearing item is chosen after seeing the target, the entry is downgraded from **prospective prediction** to **post-fit / revised**.

A later freeze can make a future comparison prospective. It cannot retroactively make the historical discovery target-blind.

## Historical provenance audit

The dedicated October-2025 → September-2026 audit found **zero pre-existing K7 physical observables** that satisfy the OpenWave genuine-prediction gate under the hostile criteria used here.

See [`historical_prediction_audit_2025_10_to_2026_09.md`](historical_prediction_audit_2025_10_to_2026_09.md).

That result closes the historical archaeology unless new dated evidence is identified. The registry will not manufacture a pass from retrodictions.

---

# K7-P1 — Higgs trilinear self-coupling

**Status:** `FROZEN FAILED SELF-SCREEN — NOT A GENUINE PREDICTION UNDER OPENWAVE §1.1`

Full frozen preregistration:
[`K7-P1_higgs_trilinear_preregistration.md`](K7-P1_higgs_trilinear_preregistration.md)

The preregistration is retained unchanged as part of the provenance record.

Historical K7 input:

`lambda_H = sqrt(17)/32`

The frozen minimal one-doublet map used

`rho3_K7 := g_hhh(tree)/v = 6 lambda_H`

with `C6=0`.

## OpenWave ruling

OpenWave maintainer review classified K7-P1 as a **prospective consequence of a calibration, degenerate with the null**, not a genuine prediction.

In the frozen minimal one-doublet potential,

`m_h^2 = 2 lambda_H v^2`

and therefore

`g_hhh = 6 lambda_H v = 3 m_h^2 / v`,

so `kappa_lambda = 1` identically when the same frozen potential is used consistently.

The dossier's previously quoted `kappa_lambda ~ 0.9966` came from combining the K7 quartic with an independently measured `m_h`; it is therefore a restatement of the existing K7-quartic / Higgs-mass residual, not a new independent trilinear observable.

**Admission consequence:** K7-P1 earns no OpenWave §1.1 prediction credit and is not used to open a model PR.

Reproducer retained for provenance:

```bash
python3 docs/openwave-candidate/reproduce_k7_p1.py
```

---

# Candidate K7-P2 — not yet instantiated

There is currently **no `K7-P2` prediction** and no numerical value reserved under that name.

The clean-room workbench is:
[`K7_P2_candidate_generation.md`](K7_P2_candidate_generation.md)

The first operator-level Candidate A audit is:
[`K7_P2_neutrino_operator_inventory.md`](K7_P2_neutrino_operator_inventory.md)

Candidate priority:

1. absolute neutrino mass / `m_beta` — **blocked at N0/N1** pending a physical chiral-spectrum map, neutrino-capable field content and charges;
2. low-`Q^2` weak mixing angle — hold until an independent repair of the current RGE mismatch;
3. a flavor selection rule — hold until the generation-to-cycle map is derived rather than calibrated.

The surviving neutrino hypothesis seed is an exact-rank route: only if K7 derives a physical neutrino mass operator inheriting a target-blind rank-2 constraint, and independently fixes the eigenstate / ordering map, may measured oscillation quantities be ledgered as non-target anchors to compute a definite `m_beta`.

The identifier `K7-P2` is promoted only after a target-blind derivation, executable freeze, named experiment, discriminating prediction, falsifier and no-revision rule are committed.
