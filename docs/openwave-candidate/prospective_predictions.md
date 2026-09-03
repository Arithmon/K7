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

---

# K7-P1 — Higgs trilinear self-coupling

**Status:** `FROZEN TREE-LEVEL BENCHMARK — OpenWave genuine-prediction gate unresolved`

Full preregistration:
[`K7-P1_higgs_trilinear_preregistration.md`](K7-P1_higgs_trilinear_preregistration.md)

Historical K7 input:

`lambda_H = sqrt(17)/32`

This historical relation is not relabeled as a new prediction.

Frozen new consequence under the minimal renormalizable one-doublet Higgs potential:

`rho3_K7 := g_hhh(tree)/v = 6 lambda_H`

therefore

`rho3_K7 = 3 sqrt(17)/16 = 0.7730823048033113...`

The benchmark also freezes `C6 = 0` for an independent `(H†H)^3` deformation. This is explicitly counted as a discrete physical-identification choice, not claimed as a K7 theorem.

## Why the primary number is `rho3`, not `kappa_lambda`

`kappa_lambda` depends on the external reporting anchors used for the SM reference:

`kappa_lambda = rho3 * v^2 / (3 m_H^2)`.

The immutable K7 output is therefore `rho3`. Any future experimental release must state the `m_H`, `v`, scheme and benchmark convention used for conversion.

## Known-before-freeze baseline

CMS-PAS-HIG-25-008 (2026-08-06) already gave a broad direct interval

`-2.5 < kappa_lambda < 9.4` at 95% CL

for the combined result. Compatibility with this pre-freeze interval is **not** prospective evidence.

## Falsifier

A future post-freeze direct extraction that excludes the frozen K7-P1 value at 95% CL under a compatible minimal benchmark falsifies the **minimal K7 Higgs identification**.

It does not automatically falsify the K7 topology.

## OpenWave caveat

Whether this satisfies OpenWave's “genuine prediction” gate is intentionally left open to hostile review. The strongest objection is that `lambda_H` itself was historically compared with a known Higgs target; K7-P1 is a new consequence of that fixed relation, not a target-blind origin for the relation itself.

Reproducer:

```bash
python3 docs/openwave-candidate/reproduce_k7_p1.py
```
