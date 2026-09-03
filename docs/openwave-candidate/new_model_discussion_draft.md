# DRAFT — OpenWave New Model discussion

**Do not post until the candidate dossier passes an independent hostile review.**

## Proposed title

`[New Model] K7 — G2 compactification / spectral-arithmetic structural framework`

## Model identity

- **Name:** K7 framework
- **Author:** Brieuc de La Fournière
- **Repository:** `Arithmon/K7`
- **Program:** Arithmon
- **Proposed initial regime:** static / spectral / structural; dynamics incomplete
- **Requested outcome:** an honest OpenWave column, allowed to begin mostly untested

## Lineage

K7 is a top-down compactification framework motivated by 11D / M-theory, `E8 × E8`, `G2` geometry and a K3/TCS construction program. Its historical arithmetic layer explores whether dimensionless observables can be expressed as invariants/counts of a fixed compact geometry.

## Why we are applying

We first used OpenWave's STEP 1 protocol against K7 privately. It exposed useful problems before any application:

- historical relations must be separated from prospective predictions;
- “zero free parameters” is too broad under OpenWave because discrete structural and identification choices must be counted;
- the public reproducer must be separated from private canonical machinery;
- statistical survivors are not the same thing as target-blind predictions;
- a new prospective namespace needs immutable observable maps.

Those findings are now recorded rather than hidden.

## Substrate

Top-down compactification / spectral geometry on a proposed compact seven-dimensional `G2` geometry `K7`, with declared topology ledger including `b2=21`, `b3=77`.

The compact torsion-free existence theorem is an active analytic target, not claimed complete.

## Native dynamics

Not complete.

There is 4D effective-theory / RGE work in the project, but we are not presenting K7 initially as a native field-evolution simulator. We propose a Tier-3-like static/spectral entry first.

## Particle map

Partial only.

The cleanest current overlaps with OpenWave are:

- PMNS / three-generation static data;
- charged-lepton mass ratios;
- potentially running coupling after a clean public RGE reproducer is frozen.

We do not claim electron soliton dynamics, baryon bound states, nuclear structure, Maxwell emergence, or atomic quantization.

## Free-choice ledger

Working statement:

> No continuously adjustable parameter is tuned inside the frozen Type-I algebraic layer; discrete structural inputs, normalizations, model-selection choices, physical identifications and dimensional anchors are ledgered separately.

We do not ask OpenWave to accept the historical phrase “zero free parameters” without that qualification.

## Prediction / calibration ledger

Historical Type-I relations are treated conservatively as retrodictions unless target-blind provenance is demonstrated.

The Sieve supplies an ex-post frozen grammar/null audit and identifies survivors, but it does not retroactively preregister relations discovered earlier.

### Prospective candidate K7-P1

We have now frozen a new consequence of the historical Higgs relation:

`lambda_H = sqrt(17)/32`

under the minimal renormalizable one-doublet potential:

`rho3 = g_hhh(tree)/v = 3 sqrt(17)/16 = 0.7730823048033113...`

The full record is in `K7-P1_higgs_trilinear_preregistration.md`, with a dedicated target-free reproducer and a no-revision rule.

We are **not** claiming that `lambda_H` itself was target-blind. It was historically compared with a known Higgs target.

We are also **not** hiding the remaining choices: `C6=0` is a discrete minimal-operator benchmark, and K7 does not yet provide a derived UV-to-IR Higgs matching calculation.

The question we would like OpenWave reviewers to attack is therefore precise:

> Does committing a previously fixed, calibration-sensitive relation to a genuinely new physical observable before precision data exist satisfy the OpenWave “genuine prediction” gate, or should K7-P1 be classified only as a prospective consequence of a calibration?

Either answer is useful. We prefer a conservative classification over inflating the score.

## Reproducibility

From a clean clone:

```bash
python3 docs/openwave-candidate/reproduce_minimal.py
python3 docs/openwave-candidate/reproduce_k7_p1.py
```

The default K7-P1 run contains no experimental targets.

## Falsifiers

See `docs/openwave-candidate/falsifiers.md`.

Notably, we distinguish:

- falsification of the compact analytic construction;
- falsification of a physical identification (e.g. PMNS or minimal Higgs map);
- failure of reproducibility;
- failure of the underlying topology hypothesis.

## Formal artifacts

K7 has a companion Lean repository (`Arithmon/K7-Lean`) and machine-checked algebraic/certificate layers. We do not use formal verification of arithmetic identities as a substitute for physical derivation.

## Provisional OpenWave coverage

See `docs/openwave-candidate/openwave_mapping.md`.

The initial self-map has only two serious partial candidates (PMNS and charged-lepton spectrum), one deferred candidate (running coupling), and otherwise intentionally leaves rows unclaimed.

## Help wanted

We would especially value hostile review on:

1. the parameter count;
2. whether any claimed step is chosen rather than forced;
3. the minimum evidence needed for the static half of PMNS / lepton-spectrum rows;
4. whether K7-P1 qualifies as a genuine prediction under section 1.1;
5. whether the proposed initial static/spectral scope matches OpenWave's intended model class.
