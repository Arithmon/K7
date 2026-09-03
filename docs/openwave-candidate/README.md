# K7 → OpenWave candidate dossier

**Status:** internal pre-onboarding dossier; not an OpenWave submission and not an earned OpenWave column.

**K7 source snapshot:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`  
**OpenWave protocol snapshot:** `openwave-labs/openwave@3416b53921a144f0d8d4827f377b030b984f0ba7`

## Purpose

This directory is a hostile-read bridge between the K7 framework and the OpenWave model-onboarding protocol. It is intentionally narrower and more conservative than the public framework presentation.

The goal is not to maximize checkmarks. The goal is to expose, before any application:

1. which K7 claims are structural inputs, historical retrodictions, sieve-distinguished relations, or genuinely prospective outputs;
2. which OpenWave criteria K7 can plausibly address today;
3. which claims are reproducible from a clean, minimal script;
4. which falsifiers are sharp enough to be recorded in advance;
5. which physical identifications are still chosen rather than forced.

## Scope carried into this dossier

K7 is treated here as a **static / spectral / structural framework first**. It is not presented as a completed field simulator.

The compact torsion-free `K_7` existence theorem remains open. The repository's own scope audit forbids promoting local, box-local, neck-level, or conditional artifacts into a compact-global metric theorem. See:

- [`../../audit/claim_scope.md`](../../audit/claim_scope.md)
- [`../../docs/analytic_status.md`](../../docs/analytic_status.md)
- [`../../publications/ERRATUM_v3.5.md`](../../publications/ERRATUM_v3.5.md)

This dossier therefore makes no claim of an exact compact metric on `K_7`.

## Terminology used here

We deliberately do **not** use “zero free parameters” as an unqualified OpenWave claim.

The working wording is:

> **No continuously adjustable parameter is tuned inside the frozen Type-I algebraic layer; discrete structural inputs, normalizations, model-selection choices, formula/observable identifications, and any dimensional anchors are ledgered separately.**

Likewise, the 33 Type-I relations are not called “33 prospective predictions” here. The v3.5 statistical layer already distinguishes conditional algebraic identities, sieve-distinguished survivors, and exploratory identities; this dossier additionally separates those from prospective predictions.

## Files

- [`honest_ledger.md`](honest_ledger.md) — inputs, choices, calibrations/retrodictions, survivors, prospective outputs.
- [`openwave_mapping.md`](openwave_mapping.md) — all 31 OpenWave criteria, with a deliberately conservative K7 disposition.
- [`falsifiers.md`](falsifiers.md) — what would refute which layer of K7.
- [`prospective_predictions.md`](prospective_predictions.md) — prospective freeze rules and registry.
- [`K7-P1_higgs_trilinear_preregistration.md`](K7-P1_higgs_trilinear_preregistration.md) — frozen K7-P1 record.
- [`reproduce_minimal.py`](reproduce_minimal.py) — target-free minimal arithmetic reproducer.
- [`reproduce_k7_p1.py`](reproduce_k7_p1.py) — dedicated target-free K7-P1 reproducer.
- [`new_model_discussion_draft.md`](new_model_discussion_draft.md) — draft only; do not post until the hostile review is closed.

## Minimal reproduction

From the repository root:

```bash
python3 docs/openwave-candidate/reproduce_minimal.py
python3 docs/openwave-candidate/reproduce_k7_p1.py
```

The scripts print quantities assembled from the declared K7 ledger and contain no experimental target in their default execution. Comparison data belong in a separate, source-cited validation layer.

## Gate before an OpenWave application

Do not post the draft application until all of the following are true:

- [ ] an independent parameter-counter pass has challenged every “forced” step;
- [x] the candidate public reproducer paths are explicit from repository root;
- [x] historical target leakage is explicitly recorded;
- [x] K7-P1 has a frozen tree-level observable map and a no-revision rule;
- [ ] OpenWave reviewers / a second hostile read decide whether K7-P1 is a genuine prediction or only a prospective consequence of a historical calibration;
- [ ] no status icon in `openwave_mapping.md` is represented as earned in-platform;
- [ ] a second independent hostile read has tried to refute the dossier.

A low initial score is acceptable. Inflating a partial map into a validated mechanism is not.
