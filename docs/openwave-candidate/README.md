# K7 → OpenWave candidate dossier

**Status:** internal pre-onboarding dossier; not an OpenWave submission and not an earned OpenWave column.

**K7 source snapshot:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`  
**OpenWave protocol snapshot:** `openwave-labs/openwave@3416b53921a144f0d8d4827f377b030b984f0ba7`

**Current rho17 status:** `rho17 full JK integral action: HOLD`.  The
standard integral symplectic `V4` backend passes, but the finite matched
families audited so far do not realize the required anti-symplectic fixed
lattice types `(11,7,1)` and `(11,9,1)^3`.  This is a scoped search result,
not a general rho17 no-go theorem.  See
[`K7_P2_neutrino_rho17_JK_integral_action.md`](K7_P2_neutrino_rho17_JK_integral_action.md).

**Frozen geometry target:** `K7-GEO-JK-F1` at commit
`629e87ef968f2b126b7ca4a1fa89a81ccedf2fa4`; see
[`K7_P2_JK_geometry_freeze.md`](K7_P2_JK_geometry_freeze.md). Subsequent
search notes must cite this freeze and may not revise its target under the same
identifier.

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
- [`K7_P2_neutrino_operator_inventory.md`](K7_P2_neutrino_operator_inventory.md) — D1 neutrino operator / field-content inventory; Candidate A currently blocked before a mass operator.
- [`K7_P2_neutrino_H0_fiber_lattice_gate.md`](K7_P2_neutrino_H0_fiber_lattice_gate.md) — generic `V4` lattice gate and Picard-rank consistency audit.
- [`K7_P2_neutrino_H0a3_equivariant_data_contract.md`](K7_P2_neutrino_H0a3_equivariant_data_contract.md) — exact data contract, now sharpened by the full-group character no-go.
- [`K7_P2_neutrino_rank15_CM_V4_gate.md`](K7_P2_neutrino_rank15_CM_V4_gate.md) — recovered rank-15 `NS=U+E7(-1)+A1(-1)^6`; the geometric CM `V4` and Donaldson reflection preserve an elliptic fiber, but the frozen full JK package is impossible at `rho=15`.
- [`K7_P2_neutrino_JK_character_obstruction.md`](K7_P2_neutrino_JK_character_obstruction.md) — exact representation-theoretic obstruction: the frozen JK package requires `rho>=17`; historical `T5''` also fails the target anti-symplectic fixed loci.
- [`K7_P2_neutrino_N0_heterotic_dual_route.md`](K7_P2_neutrino_N0_heterotic_dual_route.md) — provisional heterotic-dual route; no global K7 duality claimed yet.
- [`openwave_mapping.md`](openwave_mapping.md) — OpenWave criterion mapping, with a deliberately conservative K7 disposition.
- [`falsifiers.md`](falsifiers.md) — what would refute which layer of K7.
- [`prospective_predictions.md`](prospective_predictions.md) — prospective freeze rules and registry, including the post-freeze K7-P1 ruling.
- [`K7-P1_higgs_trilinear_preregistration.md`](K7-P1_higgs_trilinear_preregistration.md) — frozen K7-P1 record; retained unchanged.
- [`reproduce_minimal.py`](reproduce_minimal.py) — target-free minimal arithmetic reproducer.
- [`reproduce_k7_p1.py`](reproduce_k7_p1.py) — dedicated K7-P1 reproducer retained for provenance.
- [`check_k3_v4_genus_one_gate.py`](check_k3_v4_genus_one_gate.py) — target-free generic symplectic-`V4` Picard-rank / elliptic-existence arithmetic.
- [`check_k3_rank15_cm_v4_gate.py`](check_k3_rank15_cm_v4_gate.py) — exact rank-15 NS / fiber / section / degree-8 arithmetic.
- [`check_k3_jk_character_gate.py`](check_k3_jk_character_gate.py) — exact `(Z/2)^3` character inversion proving the rank-15 full-JK no-go and `rho>=17` necessary bound.
- [`check_k3_rho17_tauOmega_discriminant_actions.py`](check_k3_rho17_tauOmega_discriminant_actions.py) — exhaustive trace-zero `D4(-2)^3` Omega action table and discriminant-action hash.
- [`check_k3_rho17_tauM_matching.py`](check_k3_rho17_tauM_matching.py) — explicit finite `M` matching and exact fixed-lattice profiles.
- [`check_k3_rho17_jk_reflection_twists.py`](check_k3_rho17_jk_reflection_twists.py) — paired-root twists, including the all-height residue screen.
- [`check_k3_rho17_jk_eichler_twists.py`](check_k3_rho17_jk_eichler_twists.py) — single opposite-eigenspace Eichler twists and scoped no-hit certificate.
- [`reproduce_rho17_integral_audit.sh`](reproduce_rho17_integral_audit.sh) — ordered target-free audit runner.
- [`K7_P2_JK_geometry_freeze.md`](K7_P2_JK_geometry_freeze.md) — no-revision freeze of the selected JK topology and fixed-locus package.
- [`K7_P2_JK_geometry_role_decomposition.md`](K7_P2_JK_geometry_role_decomposition.md) — selected/derived/certified/open chain.
- [`check_k3_rho17_jk_eichler_compositions.py`](check_k3_rho17_jk_eichler_compositions.py) — bounded two-step Eichler compositions with eigenspace recomputation.
- [`K7_P2_JK_eichler_composition_audit.md`](K7_P2_JK_eichler_composition_audit.md) — scoped structural lead from the recomposed profiles.
- [`check_k3_rho17_eichler_mod2_continuation.py`](check_k3_rho17_eichler_mod2_continuation.py) — continuation-completeness test for repeated exact lifts.
- [`new_model_discussion_draft.md`](new_model_discussion_draft.md) — historical discussion draft; no model PR is opened from K7-P1.

## Minimal reproduction

From the repository root:

```bash
python3 docs/openwave-candidate/reproduce_minimal.py
python3 docs/openwave-candidate/reproduce_k7_p1.py
python3 docs/openwave-candidate/check_k3_v4_genus_one_gate.py
python3 docs/openwave-candidate/check_k3_rank15_cm_v4_gate.py
python3 docs/openwave-candidate/check_k3_jk_character_gate.py
```

The rho17 integral-action audit is reproduced separately, in this order:

```bash
bash docs/openwave-candidate/reproduce_rho17_integral_audit.sh
```

The scripts contain no neutrino-mass target in their default execution. Experimental comparison data belong in a separate, source-cited validation layer.

## Current Candidate-A boundary

The rank-15 recovery closed an important **subgroup/fiber-level** question:

- `NS=U+E7(-1)+A1(-1)^6` contains an explicit Jacobian `U` and degree-8 polarization;
- the recovered Clingher–Malmendier Mordell–Weil `V4` preserves the fiber class;
- every current Donaldson `alpha_1` candidate lies orthogonal to that `U`, so its Picard–Lefschetz reflection also fixes the fiber class.

But the full frozen Joyce–Karigiannis package is now known **not** to fit at Picard rank 15. The exact group-character check gives an impossible multiplicity `-2` in `NS` and the general necessary condition

`rho >= 17`.

The later historical `T5''` CI(2,2,2) does not evade this result: its three `tau sigma` involutions were recorded as free, while the frozen `(11,9,1)` target requires `(g,k)=(1,1)` fixed loci.

The next K3 construction target is therefore a **degree-8, `rho>=17` realization of the complete frozen `(Z/2)^3` action**. If such a realization exists, its full-group invariant cohomology has rank 5; at lattice level this is enough to force an invariant isotropic class by Meyer. Nefness, a section, global matching and the heterotic dictionary remain open.

This is still not a neutrino mechanism.

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
- [x] the rank-15 K3 lattice arithmetic and full-JK rank obstruction are public and reproducible;
- [ ] a `rho>=17` degree-8 K3 realizing the complete frozen JK group action is constructed;
- [ ] the full global compactification / duality map needed by Candidate A is closed;
- [ ] at least one `K7-Pn` entry is accepted as satisfying the genuine-prediction gate; currently none is counted as such by this dossier;
- [ ] the relevant K7 physical map is derived without target leakage;
- [ ] no status icon in `openwave_mapping.md` is represented as earned in-platform;
- [ ] a second independent hostile read has tried to refute the eventual promoted candidate.

A low initial score is acceptable. Inflating a partial map into a validated mechanism is not.
