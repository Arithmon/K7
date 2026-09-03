# Prospective prediction registry

## Rule for the `K7-Pn` namespace

A `K7-Pn` entry exists only when all of the following are frozen before the future comparison is used:

- source commit;
- structural inputs;
- physical observable map;
- operator basis;
- normalization;
- scheme and scale;
- branch / sign conventions;
- dimensional anchor, if any;
- executable assembly;
- numerical value;
- experiment / data release that will test it;
- falsification rule;
- no-revision rule.

If any load-bearing item is chosen after seeing the target, the entry is downgraded from **prospective prediction** to **post-fit / revised**.

---

# K7-P1 — Higgs trilinear self-coupling candidate

**Status:** `CANDIDATE — arithmetic layer frozen; physical experimental map not yet fully frozen`

This entry intentionally stops one step short of calling itself an OpenWave-ready physical prediction.

## Frozen source relation

Historical K7 relation:

`lambda_H = sqrt(17)/32`

Numerically:

`lambda_H = 0.1288470508005519...`

The relation itself is historical and is **not** relabeled as a prospective discovery.

## New out-of-sample consequence

Under the minimal renormalizable single-Higgs-doublet potential

`V(H) = -mu^2 H†H + lambda_H (H†H)^2`

the tree-level cubic coefficient is forced:

`g_hhh(tree) = 6 lambda_H v`

so the dimensionless ratio is

`rho3_tree := g_hhh(tree)/v`

`rho3_tree = 3 sqrt(17)/16`

`rho3_tree = 0.7730823048033113...`

Using `v = 246.22 GeV` only as a declared dimensional anchor gives the tree-level benchmark

`g_hhh(tree) = 190.3483250887 GeV`.

## Why this is potentially prospective

No new K7 integer or arithmetic expression is selected to match a measured Higgs-pair target. The consequence follows from the already-frozen `lambda_H` **if** the minimal Higgs operator basis is adopted.

## Remaining gate before calling it a physical prediction

A collider extraction is not a direct measurement of a bare tree-level coefficient. Before preregistration we must freeze:

1. the renormalization scheme;
2. the reference scale;
3. loop matching / running from the K7 `lambda_H` convention;
4. the precise `kappa_lambda` or other pseudo-observable to be compared;
5. whether any dimension-six `(H†H)^3` operator is allowed.

Until these are fixed **without using the future target**, `K7-P1` is a prospective **tree-level benchmark**, not yet a complete experimental prediction.

## No-revision rule

After the physical map is frozen:

- do not change 17, 32, the sign, or the operator basis to improve agreement;
- do not add a dimension-six Higgs coefficient after seeing the result;
- any necessary post-data change creates `K7-P1R1` and the original verdict remains in the record.

## Desired final artifact

A final preregistration should contain:

```text
K7-P1
source_sha = <immutable K7 commit>
observable = <exact collider pseudo-observable>
scheme = <frozen>
scale = <frozen>
operator_basis = <frozen>
prediction = <number>
falsifier = <interval / likelihood rule>
```
