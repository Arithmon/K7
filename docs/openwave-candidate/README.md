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

## Historical provenance result

The October-2025 → September-2026 hostile audit is now closed with **zero pre-existing K7 physical observables found to satisfy the OpenWave genuine-prediction gate**. That result is recorded rather than repaired by relabeling old formulas.

See [`historical_prediction_audit_2025_10_to_2026_09.md`](historical_prediction_audit_2025_10_to_2026_09.md).

OpenWave maintainer review also ruled K7-P1 **not** to be a genuine prediction under §1.1. The frozen preregistration is retained as a failed self-screen / provenance record rather than rewritten after the fact.

The forward route is a clean-room candidate-generation workbench. No `K7-P2` prediction exists yet.

See [`K7_P2_candidate_generation.md`](K7_P2_candidate_generation.md).

## Files

- [`honest_ledger.md`](honest_ledger.md) — inputs, choices, calibrations/retrodictions, survivors, prospective outputs.
- [`historical_prediction_audit_2025_10_to_2026_09.md`](historical_prediction_audit_2025_10_to_2026_09.md) — dated hostile provenance audit; historical pass count = 0.
- [`K7_P2_candidate_generation.md`](K7_P2_candidate_generation.md) — clean-room workbench for the next genuine prediction; no K7-P2 number yet.
- [`K7_P2_neutrino_operator_inventory.md`](K7_P2_neutrino_operator_inventory.md) — D1 neutrino operator / field-content inventory; Candidate A currently blocked at N0/N1.
- [`openwave_mapping.md`](openwave_mapping.md) — all 31 OpenWave criteria, with a deliberately conservative K7 disposition.
- [`falsifiers.md`](falsifiers.md) — what would refute which layer of K7.
- [`prospective_predictions.md`](prospective_predictions.md) — prospective freeze rules and registry, including the post-freeze K7-P1 ruling.
- [`K7-P1_higgs_trilinear_preregistration.md`](K7-P1_higgs_trilinear_preregistration.md) — frozen K7-P1 record; retained unchanged.
- [`reproduce_minimal.py`](reproduce_minimal.py) — target-free minimal arithmetic reproducer.
- [`reproduce_k7_p1.py`](reproduce_k7_p1.py) — dedicated K7-P1 reproducer retained for provenance.
- [`new_model_discussion_draft.md`](new_model_discussion_draft.md) — historical discussion draft; no model PR is opened from K7-P1.

## Minimal reproduction

From the repository root:

```bash
python3 docs/openwave-candidate/reproduce_minimal.py
python3 docs/openwave-candidate/reproduce_k7_p1.py
```

The scripts print quantities assembled from the declared K7 ledger and contain no experimental target in their default execution. Comparison data belong in a separate, source-cited validation layer.

## Gate before an OpenWave application

Do not open a model PR until all of the following are true:

- [ ] an independent parameter-counter pass has challenged every “forced” step;
- [x] the candidate public reproducer paths are explicit from repository root;
- [x] historical target leakage is explicitly recorded;
- [x] the Oct-2025 → Sep-2026 provenance audit is closed; historical pass count = 0;
- [x] the next-prediction clean-room workbench is opened with target-use restrictions;
- [x] K7-P1 has a frozen record and no-revision provenance;
- [x] OpenWave maintainer review classified K7-P1 as **not** a genuine §1.1 prediction;
- [x] Candidate A has an operator-level inventory separating representation seeds from derived physical field content;
- [ ] at least one `K7-Pn` entry is accepted as satisfying the genuine-prediction gate; currently none is counted as such by this dossier;
- [ ] the relevant K7 physical map is derived without target leakage;
- [ ] no status icon in `openwave_mapping.md` is represented as earned in-platform;
- [ ] a second independent hostile read has tried to refute the eventual promoted candidate.

A low initial score is acceptable. Inflating a partial map into a validated mechanism is not.
