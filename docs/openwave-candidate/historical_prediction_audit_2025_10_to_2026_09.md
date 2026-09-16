# Historical prediction audit — October 2025 to September 2026

**Audit date:** 2026-09-07  
**K7 source snapshot:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`  
**Purpose:** determine whether any physical observable already present in the K7 history satisfies the OpenWave genuine-prediction gate without retroactive relabeling.

## Result

> **PASS COUNT: 0 pre-existing physical observables found to satisfy the OpenWave genuine-prediction gate in the audited window.**

This is a provenance result, not a claim that K7 has no falsifiable consequences. It means that, after hostile review, no physical observable found in the October-2025 → September-2026 repository history simultaneously satisfies all of the following:

1. the relevant target value was not known / used when the formula and physical map were fixed;
2. the physical observable map is sufficiently closed to identify what an experiment measures;
3. the result has enough experimental discriminating power to be tested rather than merely remaining compatible with a broad range;
4. the result is reproducible without post-result changes of sign, branch, operator basis, dimensional anchor, scale or scheme.

`K7-P1` is **not** counted as a pass in this historical audit. It is a later, explicitly preregistered consequence in the OpenWave dossier and remains separately classified as `genuine-prediction gate unresolved`.

---

## Audited families

| Family | Historical state | Gate failure | Disposition |
| --- | --- | --- | --- |
| Type-I SM relations: electroweak, charged leptons, PMNS, CKM, boson ratios, cosmology | formulas developed with corresponding experimental values already available | target known before formula freeze | **FAIL — retrodiction / calibration-sensitive** |
| `delta_CP = 197 deg`, `theta_23`, PMNS | sharp and falsifiable for future data, but historical targets were already known | prospective future comparison does not make discovery target-blind | **FAIL — locked retrodiction** |
| Dark-matter masses `90.5 GeV`, `352.7 GeV` (2025-11-14, e.g. commit `3420fff606ee63e7cd1c3f9d1a34319cdaaeac3a`) | numerical masses were announced prospectively | no derived interaction strength / production or scattering map sufficient to define an experiment-level signal; hidden-sector identification remains underderived | **FAIL — physical map incomplete** |
| Spectral / KK mass gap | internal spectral quantity; later cleaned up in Papers A/B | commit `81a3aacf247e42acf2b6054bf4108a854a2674ee` explicitly reframed `lambda_1 = 6 pi^2 / 475` as derived a posteriori, not a topological prediction; no collision-scale identification | **FAIL — internal + a posteriori** |
| Wilson-line / instanton lepton hierarchy | geometric mechanism study | current v3.5 record consumes calibrated `c = 0.452`, optimized positions, and generation-to-cycle assignment selected among 57 cycles by minimizing deviation | **FAIL — conditional calibration** |
| SUSY spectrum (`m_3/2 ~ 166 GeV`, moduli ~3.2 TeV) | model-dependent phenomenological consequence | uses explicit `M_GUT`, `alpha_GUT`, condensation / spectrum assumptions and allows compressed or suppressed-coupling realizations | **FAIL — anchors + underdetermined signal** |
| Proton lifetime `~4.06e38 y` | model-dependent consequence | uses `M_X = M_GUT`, `alpha_GUT` and a lattice-QCD hadronic matrix element; target is far beyond near-term reach | **FAIL — anchored + non-discriminating near term** |
| Riemann / Yang-Mills blind and holdout challenges (Jan–Feb 2026) | genuinely preregistered mathematical tests with holdouts, null models and frozen conductors | not a subatomic physical observable for OpenWave's model-comparison gate | **OUT OF SCOPE — methodologically positive** |

## Methodological positive result

K7 has already demonstrated the **process** needed for a genuine prediction in the 2026 mathematical blind challenges:

- preregistration before the holdout calculation;
- frozen candidate sets;
- explicit controls / null grammars;
- willingness to record failures rather than rewrite the target.

The prediction problem is therefore not primarily procedural. It is now a **physics-output problem**: produce a new experiment-facing observable from K7 before its target is known or used.

## Stop rule for historical archaeology

The October-2025 → September-2026 archaeology is considered **closed** for onboarding purposes.

Re-open it only if one of the following occurs:

- a reviewer identifies a specific historical K7 statement whose dated provenance may satisfy the gate;
- a forgotten timestamped artifact is found that fixes both a physical observable and its numerical value before the corresponding target was available;
- the OpenWave definition of genuine prediction materially changes.

Do not continue scanning old formulas merely to manufacture a pass.

## Consequence for the OpenWave dossier

The dossier should state plainly:

> **Historical provenance audit, Oct 2025–Sep 2026: no pre-existing K7 physical observable was found to satisfy OpenWave §1.1 as a genuine prediction.**

The route forward is new prospective work, not retrospective relabeling. See [`K7_P2_candidate_generation.md`](K7_P2_candidate_generation.md).
