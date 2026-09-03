# K7-P1 — Higgs trilinear self-coupling preregistration

**Freeze date:** 2026-09-03  
**Status:** `FROZEN TREE-LEVEL BENCHMARK — OpenWave genuine-prediction gate unresolved`  
**Historical K7 source snapshot:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`

This record is deliberately narrower than a claim of a complete collider prediction.

## 1. Historical input, not a new prediction

The K7 observable ledger already contains

\[
\lambda_H^{K7}=\frac{\sqrt{17}}{32}=0.1288470508005519\ldots
\]

The value of the Higgs-sector target was known when this relation was developed. Therefore this relation is **historical / calibration-sensitive** for OpenWave accounting. This preregistration does not relabel it as target-blind.

## 2. New frozen consequence

Freeze the minimal renormalizable single-Higgs-doublet potential

\[
V(H)=-\mu^2H^\dagger H+\lambda_H(H^\dagger H)^2.
\]

For \(H=(0,(v+h)/\sqrt2)^T\), the tree-level trilinear vertex coefficient is

\[
g_{hhh}^{tree}=6\lambda_Hv.
\]

The primary dimensionless K7 quantity is therefore

\[
\rho_3^{K7}:=\frac{g_{hhh}^{tree}}{v}
=6\lambda_H^{K7}
=\frac{3\sqrt{17}}{16}
=0.7730823048033113\ldots
\]

This number is the frozen K7-P1 output.

No measured Higgs-pair target enters this arithmetic assembly.

## 3. Operator-basis freeze

K7-P1 adopts the **minimal benchmark**

\[
C_6=0
\]

for an independent dimension-six \((H^\dagger H)^3\) deformation.

This is ledgered as a **discrete physical-identification choice**, not claimed as a theorem derived from the current compact K7 construction.

A later need for non-zero \(C_6\) does not permit K7-P1 to be silently repaired. It falsifies or supersedes this minimal Higgs identification.

## 4. Experimental convention

Collider results are usually reported through

\[
\kappa_\lambda=\frac{g_{hhh}}{g_{hhh}^{SM}},
\qquad
g_{hhh}^{SM}=\frac{3m_H^2}{v}.
\]

K7-P1 does **not** freeze a data-edition-dependent \(m_H\) or \(v\) as part of the model prediction. A publication may convert the immutable \(\rho_3^{K7}\) into its own stated convention:

\[
\kappa_\lambda^{K7}
=\frac{\rho_3^{K7}v^2}{3m_H^2}.
\]

Those anchors are conversion metadata only.

For regression checking, the historical pair \(m_H=125.20\) GeV and \(v=246.22\) GeV gives

\[
\kappa_\lambda^{K7}=0.9966495482\ldots
\]

but that converted value is not the primary frozen quantity.

## 5. Baseline known before this freeze

CMS-PAS-HIG-25-008 was public on 2026-08-06, before K7-P1 was frozen. Its combined Run-2 + Run-3 result constrains

\[
-2.5 < \kappa_\lambda < 9.4
\]

at 95% CL, with coupling modifiers not included in the scan fixed to their SM values.

Therefore **being compatible with that interval earns no prospective credit**. It is baseline information already known at freeze time.

Reference:
`https://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/HIG-25-008/index.html`

## 6. Prospective test rule

A post-freeze direct Higgs-self-coupling result may test K7-P1 only if:

1. the result provides a one-dimensional \(\kappa_\lambda\) likelihood/interval or an equivalent extractable \(g_{hhh}\);
2. the assumed operator/coupling benchmark is stated;
3. the conversion convention for \(m_H\) and \(v\) is recorded;
4. the K7 arithmetic, sign and operator basis are not altered after seeing the result.

### Falsifier

Under a compatible minimal benchmark, exclusion of the K7-P1 value at **95% CL** falsifies the **minimal K7 Higgs identification**.

It does not automatically falsify the K7 topology or every historical K7 arithmetic relation.

## 7. No-revision rule

After this freeze:

- do not change 17, 32, the sign, or the factor 6;
- do not introduce a fitted \(C_6\) to rescue disagreement;
- do not select a different Higgs-potential normalization after seeing the result;
- do not move the comparison scale or scheme post hoc and call the result the same prediction;
- any revised physical map must receive a new identifier (`K7-P1R1`, etc.) while K7-P1 remains in the record.

## 8. OpenWave status

This entry is a serious candidate for OpenWave's “at least one genuine prediction” gate because a previously fixed K7 relation is being committed to a new physical observable before precision data exist.

However, the historical origin of \(\lambda_H\), the minimal-operator choice, and the lack of a derived UV-to-IR matching calculation are material objections. OpenWave reviewers should be invited to decide whether K7-P1 counts as a genuine prediction or only as a prospective consequence of a calibration.

No stronger status is claimed here.

## 9. Reproduction

From the repository root:

```bash
python3 docs/openwave-candidate/reproduce_k7_p1.py
```

Optional conversion only:

```bash
python3 docs/openwave-candidate/reproduce_k7_p1.py --mh 125.20 --v 246.22
```

The default run contains no experimental target values.
