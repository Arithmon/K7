---
title: "Statistical Evidence"
layout: default
---

# Statistical Evidence: the Look-Elsewhere Test

**Framework version**: 3.6. **Source**: main paper [§7](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_main.md) and supplement [S4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md); the tables on this page are copied from S4 by a script, not edited by hand.

A framework that matches 33 measured values with closed forms in a vocabulary of twenty constants must answer a prior question: how often would the same grammar, with a different vocabulary, have matched them just as well? Version 3.6 asked that question with a preregistered test. The answer is that **closeness to the measured values does not distinguish K₇** in the reference classes tested. The statistical claims of earlier versions of this page are withdrawn; section 6 lists them.

---

## 1. Summary

| | |
|---|---|
| **Question** | Does K₇ remain exceptional when each competitor searches for its own formulas, in the same grammar, at the same budget, with the same freedom of assignment and of unit? |
| **Preregistered** | 2026-10-17, before any run, with two outcomes only: a calibrated global P-value, or withdrawal of the P-value from the text |
| **K₇** | reaches 31 of the 33 targets |
| **Alternative Betti pairs** | 1 085 of 4 159 reach as many (P = 0.26); none reaches more |
| **Invented vocabularies** | 1 015 of 2 000 reach as many (P = 0.51); none reaches more |
| **Witness with no K₇ constant** | reaches 30 of the 33 with the universal leaves of the grammar alone |
| **Verdict** | P_global = 0.51 against a threshold of 0.01: the look-elsewhere effect is not overcome, and the P-value is withdrawn from the text |

P_global = 0.51 is not a probability that K₇ is right or wrong, and the counts are not a physical refutation. They say that the top score has little discriminating power in this protocol: 30 targets are reached by everyone, two by no one, and one separates the competitors.

## 2. The test

- **Targets.** The 33 relations of the dataset ([S3](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S3_observables.md)), with their measured values and uncertainties.
- **Grammar.** The frozen engine of the Sieve: its universal leaves (1 to 9, π, e, φ, γ, ln 2, ζ(3) to ζ(11)) plus the 19 integer constants of the competitor, the operations + − × / ^, square root, inverse, square and logarithm, and **at most five nodes** per expression.
- **Concordance.** A target is reached if one expression of the vocabulary falls within 2σ of the measured value on either side, asymmetric uncertainties being kept asymmetric. For m_s/m_d, which the PDG gives as a range, the window is that range. For δ_CP, the phase may be read in degrees, radians, grads or turns.
- **Assignment.** The search is blind: each target takes the cheapest concordant expression. The freedom to assign formulas to observables is granted to everyone, K₇ included, which is scored by the same search on its own vocabulary and not by its published formulas.
- **Competitors.** Every Betti pair with b₂ in [1, 40] and b₃ in [17, 120] other than (21, 77), with H*, κ_T⁻¹ and det(g) re-derived and the other constants held at K₇'s values; and 2 000 vocabularies of 19 integers drawn by the Sieve's frozen generator.
- **Verdict rule.** For a family of size N in which n competitors reach at least as many targets as K₇, P = (1 + n)/(1 + N), ties counting against K₇. P_global is the larger of the two family values, and the effect is overcome only if P_global ≤ 0.01.

The alphabet tested for K₇ is the nineteen integers of the version 3.5 Monte Carlo register, not literally the twenty constants of the main paper (§3.1): dim E₇ = 133 and α_sum = 13 are absent and κ_T⁻¹ = 61 is present. A test on the literal register would be a separate computation.

## 3. Result

| Family | N | reach ≥ 31/33 (as many as K₇) | P = (1 + n)/(1 + N) | max S_cover | S_cost range (bits) | cost ≤ K₇ |
|---|---:|---:|---:|---:|---:|---:|
| K₇ (21, 77), blind search on its own vocabulary | 1 | 31/33 | n/a | 31 | 408.1 | n/a |
| F-BETTI: alternative Betti pairs (published derivations) | 4 159 | 1 085 | 0.261 | 31 | 389.2 to 418.7 | 1 163 |
| F-VOCAB: invented vocabularies (Sieve generator) | 2 000 | 1 015 | 0.508 | 31 | 385.0 to 430.4 | 698 |
| F-BETTI-FICHE: alternative Betti pairs, variant derivations (outside the rule) | 4 160 | 723 | 0.174 | 31 | 391.3 to 417.6 | 601 |

P_global = max(P_F-BETTI, P_F-VOCAB) = **0.508**; threshold 0.01. The variant row does not enter the verdict. K₇ is not cheaper either: its description cost lies inside the range of both families.

Per target:

| ID | Observable | K₇ reaches (blind) | published value in K₇'s ≤ 5-node set | published value within window | Betti pairs reaching (of 4 159) | vocabularies reaching (of 2 000) |
|---|---|---|---|---|---:|---:|
| A01 | sin²θ_W | yes | yes | no | 4 159 | 2 000 |
| A02 | α_s(M_Z) | yes | yes | yes | 4 159 | 2 000 |
| A03 | λ_H | yes | no | yes | 4 159 | 2 000 |
| A04 | α⁻¹(0) | no | no | no | 0 | 0 |
| A05 | Q_Koide | yes | yes | yes | 4 159 | 2 000 |
| A06 | m_τ/m_e | yes | yes | no | 1 085 | 1 015 |
| A07 | m_μ/m_e | no | no | no | 0 | 0 |
| A08 | m_s/m_d | yes | yes | yes | 4 159 | 2 000 |
| A09 | m_c/m_s | yes | yes | yes | 4 159 | 2 000 |
| A10 | m_b/m_t | yes | yes | no | 4 159 | 2 000 |
| A11 | m_u/m_d | yes | yes | yes | 4 159 | 2 000 |
| A12 | sin²θ₁₂ᴾᴹᴺˢ | yes | yes | yes | 4 159 | 2 000 |
| A13 | sin²θ₂₃ᴾᴹᴺˢ | yes | yes | no | 4 159 | 2 000 |
| A14 | sin²θ₁₃ᴾᴹᴺˢ | yes | yes | yes | 4 159 | 2 000 |
| A15 | δ_CP | yes | yes | yes | 4 159 | 2 000 |
| A16 | sin θ₁₂ᶜᴷᴹ | yes | yes | yes | 4 159 | 2 000 |
| A17 | A_Wolf | yes | yes | yes | 4 159 | 2 000 |
| A18 | sin θ₂₃ᶜᴷᴹ | yes | yes | yes | 4 159 | 2 000 |
| A19 | m_H/m_t | yes | yes | yes | 4 159 | 2 000 |
| A20 | m_H/m_W | yes | yes | yes | 4 159 | 2 000 |
| A21 | m_W/m_Z | yes | no | no | 4 159 | 2 000 |
| A22 | m_μ/m_τ | yes | yes | no | 4 159 | 2 000 |
| A23 | Ω_DE | yes | yes | yes | 4 159 | 2 000 |
| A24 | n_s | yes | no | yes | 4 159 | 2 000 |
| A25 | Ω_DM/Ω_b | yes | yes | yes | 4 159 | 2 000 |
| A26 | Ω_c/Ω_Λ | yes | yes | yes | 4 159 | 2 000 |
| A27 | Ω_Λ/Ω_m | yes | yes | yes | 4 159 | 2 000 |
| A28 | h | yes | yes | yes | 4 159 | 2 000 |
| A29 | Ω_b/Ω_m | yes | yes | yes | 4 159 | 2 000 |
| A30 | Ω_c/Ω_m | yes | yes | no | 4 159 | 2 000 |
| A31 | σ_8 | yes | yes | yes | 4 159 | 2 000 |
| A32 | Y_p | yes | yes | yes | 4 159 | 2 000 |
| A33 | Ω_m/Ω_Λ | yes | yes | yes | 4 159 | 2 000 |

Most targets are reached by every competitor: at five nodes and 2σ, the grammar covers them whatever the vocabulary. The targets that discriminate are the few with very small relative uncertainties. α⁻¹ and m_μ/m_e are reached by nobody, K₇ included. m_τ/m_e is reached by K₇ and by about a third of the competitors, and the counts of the family table are exactly the counts on that one target. Three scores must be kept apart: the published formulas (24 of the 33 lie inside their windows), the free search with K₇'s alphabet (31), and the witness with no K₇ constant (30).

## 4. The Sieve scorecard

The Sieve is a public battery of four nulls with a frozen observable list and grammar. N1 asks whether a relation is isolated in the fixed vocabulary; N2 prices the freedom to have chosen the vocabulary; N3 and N4 shuffle coefficients and targets. Its published scorecard for the K₇ relations reads:

- n_s and m_H/m_W survive N1 on all three of its axes.
- Neither clears N2: a budget-matched invented vocabulary matches them as well (for m_H/m_W, 22 of 24 invented vocabularies do).
- Q_Koide is isolated in the fixed vocabulary, but its value 2/3 is reached by every vocabulary: a tie, not a survivor.
- Across the nine shallow relations tested by N2, the invented-vocabulary envelope is beaten 0 times out of 9.

What N2 cannot price is where the vocabulary comes from: the K₇ constants are E₈ dimensions and ranks and the Betti numbers, not an invented list. That is a fact about the origin of the constants, not evidence that they were selected before the data were known.

## 5. What the test does not cover, and its history

The test does not vary the gauge group or the holonomy beyond the Betti numbers, does not consider other forms of an observable (an angle against its sine squared) except for the unit of δ_CP, and does not look beyond five nodes, where several of K₇'s formulas lie. These freedoms stay in the residue register of the main paper (R4, R5, R6).

The preregistration was amended twice, each time after an external review and without changing the question, families, grammar, budget, seed or verdict rule: the dataset was refreshed and the windows made two-sided (2026-10-22), then the windows of the six Planck density ratios were recomputed on the published chains and the witness was added (2026-11-03).

| Quantity | first run (2026-10-17, dataset of v3.5, one-sided windows) | revision 1 (2026-10-24, refreshed dataset, two-sided windows; historical) | revision 2 (2026-11-03, current dataset) |
|---|---|---|---|
| K₇ S_cover | 32/33 | 31/33 | 31/33 |
| K₇ S_cost (bits) | 395.6 | 409.2 | 408.1 |
| F-BETTI: reach as many as K₇ | 4 159 of 4 159 (P = 1.000) | 1 085 of 4 159 (P = 0.261) | 1 085 of 4 159 (P = 0.261) |
| F-VOCAB: reach as many as K₇ | 1 635 of 2 000 (P = 0.818) | 1 015 of 2 000 (P = 0.508) | 1 015 of 2 000 (P = 0.508) |
| F-BETTI-FICHE: reach as many as K₇ | 4 160 of 4 160 (P = 1.000) | 723 of 4 160 (P = 0.174) | 723 of 4 160 (P = 0.174) |
| P_global, verdict | 1.000, LEE-RETRAIT | 0.508, LEE-RETRAIT | 0.508, LEE-RETRAIT |
| targets reached by nobody | A04 | A04, A07 | A04, A07 |

## 6. What earlier versions of this page reported

Earlier versions of this page presented the following as statistical evidence. Each is withdrawn.

- **"#1 among 3,070,396 configurations", "0 better alternatives", null-model p < 2 × 10⁻⁵.** These came from a search in which the alternatives were scored with K₇'s own formulas and did not search for theirs. Since the formulas had been chosen for (21, 77), (21, 77) won by construction. An earlier blind sweep over 242,064 Betti pairs had already found (21, 77) below the median ([Program, selection principle, Q-B](https://github.com/arithmon/program/blob/main/problems/selection-principle.md)).
- **"P < 5 × 10⁻⁶ among 192 349 configurations" (version 3.5).** Same design; 1/192 349 was the floor of the estimator. Withdrawn.
- **Coincidence probabilities 10⁻³⁴⁶, 10⁻¹³⁸ and 10⁻¹³³ (versions 3.3 and 3.4).** The uniform null treats predictions as random numbers, which no formula search produces; the algebraic null compares selected formulas with random ones and so does not price the selection. Withdrawn.
- **Mean deviation (0.21%, 0.24%, 0.39%, 0.73%, 0.99% across versions).** A mean deviation measures closeness, which the test above shows is not distinctive, and it hid the relations outside 2σ. Withdrawn; the [Validation Summary](Validation-Summary.html) gives the five classes instead.
- **Bayes factors, Westfall–Young and held-out tests of the 3.3 report.** They were computed on the 3.3 dataset under the same fixed-formula design and have not been recomputed. Withdrawn as evidence.
- **"Overdetermination ratio 2.13" and related diagnostics (version 3.5).** They describe how the formulas use the constants; they cannot tell a fitted formula from an unfitted one. Kept in S4.3 as archived description.

The scripts and reports behind the withdrawn figures are kept, unmaintained, in the [version 3.3 archive](https://github.com/Arithmon/K7/blob/main/publications/validation/legacy/v3.3/) as a record of what was reported.

## 7. What remains

Two things survive the look-elsewhere tests, and the paper rests on them rather than on closeness: **rigidity under a fixed dictionary** (no relation has a continuous parameter, so a single measurement can reject it under the decision rule of the main paper, §11) and **the declared residue** (what was set rather than derived is written down, §3.3).

## 8. Reproducibility

The producer, the dataset as read by the run, the preregistration with its two amendments, the result and the results of the two earlier runs are in [`publications/validation/v3.6/`](https://github.com/Arithmon/K7/blob/main/publications/validation/v3.6/), with their hashes and the command to rerun the test. Supplement [S4](https://github.com/Arithmon/K7/blob/main/publications/papers/markdown/k7_framework_3_6_S4_sieve_diagnostics.md), section S4.5, gives the pinned inputs (Sieve engine commit, grammar hash, seed).

---

*The K₇ Framework v3.6 | generated from the paper sources by `k7_v3_6_surface_pages.py`*
