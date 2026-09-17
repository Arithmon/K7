# K7 / F2R1 — physics pivot handoff

**Date:** 2026-09-17  
**Branch:** `codex/f2r1-physics-pivot`  
**Purpose:** stop spending the critical path on geometry/search tooling and use the ratified F2R1 geometry as a controlled laboratory for a closed physics calculation.

## 0. Decision

The OpenWave ruling is now stable:

- F2R1 is a valid **geometry benchmark / positive control**.
- It is **not** `K7-GEO-JK-F1`, not `(b2,b3)=(21,77)`, not `K7-P2`, and not an observable-producing closed system.
- OpenWave gate stays unchanged until there is either a genuine frozen K7-Pn or a runnable closed system with a testable output.

Therefore the program changes direction here:

> **Primary route:** F2R1 geometry → 4D effective content → analytic geometric quantity → deformation law / spectral response.
>
> **Deprioritized route:** further rho17/Eichler/mod-8 search engineering unless a later scientific argument requires it.

The rho17/Joyce–Karigiannis F1 lattice program remains **HOLD**, not abandoned and not globally refuted. Do not resume it merely because there is available compute time.

## 1. Canonical F2R1 state

Use the following provenance chain as immutable context:

1. F2 preregistration: `f9d92ada6e7de7a7dd76f17ca88900ea5b054bd1`.
2. Adversarial Gate-0 refutation: `f69ef8c2ddd329b394ec88ec51b1ad8f094b42a4`.
3. Sign-only successor freeze: `bfc1db056f4ed63311dca059d7f708bc70e2299c`.
4. Independent F2R1 ratification audit: `2ce2193b8a47ec8f7cb1bf241e35571952762d42`.
5. Canonical merge on `main`: PR #287 / merge `ca7fd24f6f0e28c8422f95958c06e8cf8395bcf8`.

The ratified geometry gives a compact simply connected full-holonomy `G2` existence construction, under the published Joyce–Karigiannis theorem, with

```text
(b1,b2,b3) = (0,4,35).
```

The singular quotient before resolution has

```text
(b1,b2,b3) = (0,0,15),
```

and four disjoint `A1` three-strata:

- two `alpha` mapping-torus strata with `b1=9` each;
- one `beta` stratum `S1 x S2`, `b1=1`;
- one `beta*s` stratum `S1 x S2`, `b1=1`.

Thus the stratum contribution is

```text
(b0,b1)(L) = (4,20),
```

and the ordinary JK resolution adds `4` to `b2` and `20` to `b3`.

Primary source inside this repository:

`docs/openwave-candidate/K7_GEO_JK_F2R1_ratification_audit_2026_09_17.md`

### Non-blocking provenance debt

OpenWave noted that the F2 refutation, F2R1 freeze and ratification audit were produced within a short time window. If F2R1 is later cited as evidence rather than only as a pipeline control, add a short audit-provenance paragraph stating:

- which agent/model/runtime performed the ratification;
- what repository state it could see;
- whether the previous F2 failure/audit was visible;
- whether the audit was independent in method only or also blind in information.

Do **not** delay the physics work for this editorial clarification.

## 2. New scientific objective

We are no longer asking first:

> Can another search family realize the selected F1 lattice package?

We are asking:

> Given one ratified explicit `G2` construction, what physically interpretable quantity can be derived from it without importing experimental targets, and can that quantity be promoted into a closed reproducible calculation?

The first three work packages are deliberately narrow.

---

# Work package A — close the 4D massless-content dictionary

## A1. Question

Determine the 4D massless field content associated with:

1. the singular `A1` orbifold phase of F2R1;
2. the smooth resolved F2R1 phase;
3. the relation between the two.

The working expectation, to be **verified from the M-theory / singular-G2 literature before promotion**, is:

- each disjoint `A1` associative stratum supports an `SU(2)` gauge sector before resolution;
- reduction on a three-stratum `L` produces adjoint chiral multiplets controlled by `b1(L)`;
- the resolved smooth phase has `b2=4` abelian vector multiplets and `b3=35` neutral chiral multiplets.

If the standard dictionary applies without extra monodromy/twisting, the candidate bookkeeping is

```text
singular phase:
  SU(2)^4
  adjoint chiral multiplicities (9,9,1,1)
  15 neutral bulk chiral multiplets

smooth phase:
  U(1)^4
  35 neutral chiral multiplets
```

with `20 = 9+9+1+1` matching the increase `35-15` under resolution.

## A2. Required output

Create a short theory note, not a new software subsystem, e.g.

`docs/openwave-candidate/K7_F2R1_4d_massless_content.md`

It must separate:

- theorem / standard effective-field-theory input from the literature;
- F2R1-specific geometric input already ratified;
- deductions;
- unresolved monodromy or representation questions.

## A3. Acceptance criteria

`PASS` only if the `SU(2)^4 -> U(1)^4` and `(9,9,1,1)` interpretation follows from an explicit published dictionary with the F2R1 local-system/stabilizer data inserted correctly.

`HOLD` if extra monodromy, singularity enhancement or local data are needed.

No Standard Model identification, no neutrino claim, no phenomenological naming of the four sectors.

---

# Work package B — audit the candidate exact period / gauge-coupling ratio

## B1. Status before work

The following is **not ratified**. It is a candidate analytic benchmark derived after F2R1 was already known.

The `beta` and `beta*s` strata are both `S1 x S2` and use the same torus circle direction in the F2R1 construction. Their relative three-volume therefore reduces, subject to checking the quotient and calibration conventions, to the relative area of the two real K3 fixed spheres.

For the Fermat sextic double cover, in a common affine/residue normalization, the candidate periods are

```text
P_beta   ~ int_R2 dx dy / sqrt(1 + x^6 + y^6),
P_betas  ~ int_{x^6+y^6<=1} dx dy / sqrt(1 - x^6 - y^6).
```

A Dirichlet-integral reduction gives the candidate expressions

```text
P_beta  ~ (1/9) Gamma(1/6)^3 / Gamma(1/2),
P_betas ~ (1/9) Gamma(1/6)^2 Gamma(1/2) / Gamma(5/6),
```

hence formally

```text
P_beta / P_betas
 = Gamma(1/6) Gamma(5/6) / Gamma(1/2)^2
 = 2.
```

If the localized gauge kinetic term is proportional to the associative volume with the same normalization for both sectors, this would imply the dimensionless candidate benchmark

```text
R(0) := g_beta^{-2} / g_betas^{-2} = 2.
```

Again: **this is a derivation to attack, not a frozen result.**

## B2. Adversarial audit order

Before writing any numerical code, try to kill `R(0)=2` analytically.

Check, in this order:

1. Derive the holomorphic two-form by residue on the weighted-projective sextic double cover used in F2R1.
2. Identify the two real fixed loci in compatible affine charts.
3. Verify that the relevant real surfaces are calibrated by the same phase / normalization of `Omega`.
4. Verify connectedness, orientation and multiplicity factors.
5. Track the quotient by the finite group: no hidden factor of `2` from orbit length, stabilizer order or mapping from raw to quotient strata.
6. Track the common torus-circle length and confirm it cancels in the ratio.
7. Only then evaluate the two Dirichlet integrals and the Gamma reflection identity.
8. Separately verify the gauge-kinetic normalization needed to turn the volume ratio into `g^{-2}` ratio.

## B3. Required output

Create one compact analytic note, e.g.

`docs/openwave-candidate/K7_F2R1_beta_betas_period_ratio.md`

Outcome language:

- `PASS`: the exact ratio `2` survives every geometric and physical normalization check;
- `FAIL`: identify the exact missing/wrong factor and publish the corrected expression;
- `HOLD`: if a metric-dependent quantity remains that cannot be eliminated by calibration/topology.

Do not create a generalized period engine for this task. A tiny symbolic checker is allowed **only after** the analytic derivation is complete, and only as a cross-check.

---

# Work package C — use the existing sextic-double-cover Picard–Fuchs route

Proceed only after Work Package B has a clean geometric definition of the two periods/cycles.

## C1. Existing private-repo asset

The private working repository already contains a historical Picard–Fuchs calculation for

```text
y^2 + x0^6 + x1^6 + x2^6 - 6 t x0^2 x1^2 x2^2 = 0
```

under the identifier `dwork_k3_sextic_double_cover`.

Relevant historical artifact:

`gift-framework/private/legacy/cleanup_2026_06_06_fop_alignment/notebooks/pf_phase3a_20260424T062004Z.json`

It records:

```text
minimal PF order = 3
integer-form coefficients = [1, 26 t, 36 t^2, 8 t^3 - 1]
manual symmetric-square test = true
```

At `t=0`, after the harmless `y = i w` convention change, this is the Fermat sextic double cover used by F2R1.

Do not assume the old notebook is authoritative merely because it exists. Re-derive the family, involution compatibility and PF equation needed for the present question.

## C2. Scientific target

After B, define the deformation observable

```text
R(t) := P_beta(t) / P_betas(t)
```

or the correctly normalized gauge-coupling ratio if B establishes that interpretation.

Before computing any derivative, freeze:

- the one-parameter family;
- the continuation of the two cycles;
- the base point `t=0`;
- the branch conventions;
- the observable definition;
- the first quantity to compute, preferably `R'(0)`.

This future derivative can be prospective relative to the frozen definition. Do not inspect a numerical value first and then choose a derivative/order because it looks interesting.

## C3. Stop conditions

Stop with `HOLD` if:

- the Dwork deformation fails to preserve the required F2R1 symmetry structure;
- either cycle cannot be continued canonically;
- the two periods mix under monodromy in a way not fixed by the frozen data;
- the observable requires a Ricci-flat metric quantity not determined by periods/calibration.

Do not patch the family after seeing the output under the same frozen identifier.

---

# 3. What to reuse from recent K3 work

The private K3-CAP program contains useful **mathematical patterns**, but its governance stack is not to be imported into F2R1.

## Reuse these ideas if a numerical spectral stage becomes necessary

### Generalized mass-matrix problem

`gift-framework/private @ 4c9f0d04` (`MASS-MATRIX-CLOSES`) established a useful numerical pattern:

- treat the mass/inner-product object as a matrix, not a scalar error bar;
- solve the generalized spectral problem in the correct metric;
- whiten by Cholesky;
- cross-check spectral counts by an independent Sylvester/inertia route;
- certify only the subspace actually consumed downstream.

### Directional rather than global certification

Recent Green-function work found that full operator norms can be grossly more pessimistic than the one direction actually consumed by the theorem. The lesson for F2R1 is:

> choose the physical observable first, then certify the operator/subspace it consumes; do not build a global spectral certificate merely because it is available.

### Correct Kähler primitives only

If an explicit K3 metric/spectral calculation later becomes unavoidable:

- do **not** reuse the historical metric-dependent path in `Arithmon/K3/src/k3_atlas/spectral_basis.py`; it is explicitly retained for audit and marked retracted;
- start from the coherent holomorphic-convention primitives in `Arithmon/K3/src/k3_atlas/kahler_metric.py`;
- note that the current public `Arithmon/K3` surface is a different K3 (three diagonal quadrics in `P5`), so its atlas is not directly the F2R1 sextic atlas.

No metric adaptation is authorized by this handoff. First exhaust the analytic period route.

---

# 4. Explicit anti-tooling rule

For this branch:

> **No new infrastructure unless a named scientific question cannot be answered without it.**

In particular, do not start with:

- a generic `G2` Laplacian engine;
- a new result manifest;
- a new review launcher;
- a BFS/state graph;
- a generalized period framework;
- a full port of K3-CAP;
- extra provenance gates beyond what is necessary to make one scientific result reproducible.

Preferred order:

```text
paper derivation
→ small note
→ tiny calculation if needed
→ only then a reusable tool if the same operation is required again.
```

One negative result is acceptable. A clean `FAIL` or `HOLD` is preferable to inventing a new framework to keep the route alive.

---

# 5. Claim discipline

Keep these distinctions explicit in every note/commit:

- **Ratified:** F2R1 geometry benchmark and `(b2,b3)=(4,35)`.
- **To verify from established M-theory literature:** detailed 4D singular gauge/matter dictionary.
- **Candidate analytic benchmark:** `R(0)=2`.
- **Historical private asset, not yet re-ratified for F2R1:** Dwork sextic-double-cover Picard–Fuchs equation.
- **Future prospective object:** a frozen deformation observable such as `R'(0)` computed only after its definition/cycles/family are fixed.
- **Not claimed:** Standard Model identification, neutrino masses, phenomenological coupling unification, recovery of F1 `(21,77)`, or satisfaction of the OpenWave gate.

Do not call a retrospective derivation a prediction.

---

# 6. Immediate Codex order

Do the following, in this order:

1. **Work Package A only:** literature + F2R1 local-data check; write the massless-content note. No new numerical code.
2. **Work Package B:** independently derive the residue form and both real-period integrals; aggressively search for quotient/calibration factors that could kill `R(0)=2`.
3. If B is `PASS`, commit the analytic result separately.
4. Only then inspect/rederive the old Dwork PF asset and prepare a **pre-computation freeze** for `R(t)` / `R'(0)`.
5. Do not begin a full F2R1 spectral solver unless A–C demonstrate that periods are insufficient.

The desired scientific progression is

```text
F2R1 geometry
    ↓
4D field-content dictionary
    ↓
exact analytic period / coupling ratio
    ↓
one-parameter period response
    ↓
runnable closed observable calculation
```

not

```text
F2R1 geometry
    ↓
more tooling
    ↓
more tooling to audit the tooling.
```

## Current program status

```text
F1 rho17 / Eichler / mod-8 search: HOLD, archived from critical path
F2R1 geometry: PASS as positive control
F2R1 4D physics dictionary: OPEN
R(0)=2: UNRATIFIED CANDIDATE
Dwork R(t): NOT STARTED / MUST BE FROZEN BEFORE NUMERICAL OUTPUT
OpenWave: NO REPLY / GATE B UNCHANGED
```
