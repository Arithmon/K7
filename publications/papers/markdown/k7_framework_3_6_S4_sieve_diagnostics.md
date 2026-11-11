# Supplement S4: Sieve and Look-Elsewhere Diagnostics

*Companion to the K₇ framework paper v3.6. This supplement gives the details of the two look-elsewhere readings of main §7: the published scorecard of the coincidence-testing protocol of [M], the Sieve (S4.1), and the preregistered null test in which every competitor searches for its own formulas (S4.2). It then archives, with their status, the descriptive diagnostics of version 3.5 (S4.3) and the coincidence probabilities of versions 3.4 and 3.5 (S4.4). Neither archive is evidence for the framework. The tables of S4.2 are generated from the result files of the test and are not edited by hand.*

## S4.1 The Sieve scorecard

The Sieve [M] is a public protocol of four null tests with a frozen observable list and grammar [S-frozen]. The isolation test (N1) asks whether a relation is isolated in the fixed vocabulary; the vocabulary-freedom test (N2) prices the freedom to have chosen the vocabulary, by comparing with invented vocabularies of the same size; the coefficient and target shuffles (N3, N4) permute coefficients and targets. Its published scorecard for the K₇ relations [M, §4.3] reads:

- n_s and m_H/m_W pass the isolation test on all three of its axes.
- Neither passes the vocabulary-freedom test: an invented vocabulary of the same size matches them as well (for m_H/m_W, 22 of 24 invented vocabularies do).
- Q_Koide is isolated in the fixed vocabulary, but its value 2/3 is reached by every vocabulary: it is a tie, not a survivor.
- Across the nine shallow relations submitted to the vocabulary-freedom test, the invented-vocabulary envelope is beaten 0 times out of 9.

What the vocabulary-freedom test cannot price is where the vocabulary comes from: the K₇ constants are E₈ dimensions and ranks and the Betti numbers, not an invented list. That is a fact about the origin of the constants, not evidence that they were selected before the data were known: the grammar and the observable list were frozen after the formulas had been found (main §3.2), and main §10 has not justified the Betti pair at the selecting step.

## S4.2 A null in which every competitor searches for its own formulas

### S4.2.1 Question and design

The test asks: **does K₇ remain exceptional when each competitor searches for its own formulas, in the same grammar, at the same budget, with the same freedom of assignment and of unit?** A null in which the alternatives are scored with K₇'s own formulas cannot answer it, since those formulas were chosen for (21, 77) (S4.4). The test was preregistered on 2026-10-17, before any run, with two outcomes only: a calibrated global p-value, or no p-value in the text.

- **Targets.** The 33 relations of the dataset (S3), with their measured values and uncertainties.
- **Grammar.** The frozen Sieve engine [M]: the leaves of its transcendental grammar (1 to 9, π, e, φ, γ, ln 2, ζ(3), ζ(5), ζ(7), ζ(9), ζ(11)) plus the 19 integer constants of the competitor's register, so that every competitor has 38 leaves (a constant alphabet size, which keeps a larger vocabulary from winning by size alone); the operations + − × / ^, square root, inverse, square and logarithm, with the engine's guards; **at most five nodes** per expression.
- **Concordance.** A target is reached by a vocabulary if one of its expressions falls in the target's window. The window is [x − 2σ₋, x + 2σ₊] around the measured value x, with asymmetric uncertainties kept asymmetric (the Sieve's frozen rule τ_z = 2); for m_s/m_d, which the PDG gives as a range with no uncertainty, the window is that range. For δ_CP, the target is reached if the phase is reached in any of four units: degrees, radians, grads or turns.
- **Assignment.** The search is blind: each target takes the cheapest concordant expression of the vocabulary. The full freedom to assign formulas to observables is therefore granted to everyone, **K₇ included**: K₇ is scored by the same blind search on its own vocabulary, not by its published formulas.
- **Scores.** The coverage score (`S_cover` in the tables), the number of targets reached, is the primary score. The description cost (`S_cost`) is the sum over targets of the description length of the cheapest concordant expression, an unreached target costing the largest attainable description length plus one operation; it is reported and does not enter the decision.
- **K₇'s register as tested.** The nineteen integers 2, 3, 5, 7, 8, 11, 14, 21, 27, 32, 52, 56, 61, 65, 77, 78, 99, 168, 248, plus φ: the register of the version 3.5 Monte Carlo (`algebraic_montecarlo.py`), not literally the twenty constants of main §3.1. Relative to §3.1, dim E₇ = 133 and α_sum = 13 are absent, and κ_T⁻¹ = 61 is present. At a fixed budget the difference matters (13 costs two leaves, 8 + 5); a test on the literal register of §3.1 is a separate computation, not done here.
- **Competitors.** The Betti-pair family (`F-BETTI`): every pair b₂ ∈ [1, 40], b₃ ∈ [17, 120] other than (21, 77), 4 159 pairs. Only H\*, κ_T⁻¹, det_den and det_num are re-derived, by the published definitions (main App. B): H\* = b₂ + b₃ + 1, κ_T⁻¹ = b₃ − dim(G₂) − p₂, det(g) = p₂ + 1/(b₂ + dim(G₂) − N_gen). Every other constant is held at K₇'s value, N_gen = 3 included, although main §3.1 writes N_gen = b₂/dim K₇: the family is conditional on that choice. The invented-vocabulary family (`F-VOCAB`): 2 000 vocabularies of 19 integers drawn by the Sieve's frozen generator (without replacement in 3 to 248, seed 20261017), plus φ.
- **Decision rule.** For each family F of size N, P_F = (1 + n)/(1 + N), where n is the number of competitors whose coverage score is at least that of K₇ (ties count against K₇). The global p-value (`P_global`) is the larger of the two family values: K₇ must beat both reference classes. The look-elsewhere effect is overcome if the global p-value is at most 0.01; otherwise the preregistered outcome is that the look-elsewhere effect is not overcome and no p-value is reported (`LEE-RETRAIT` in the tables). Neither the description cost nor the variant below can change the outcome.
- **Checks.** The first check (G1) replays the engine on the (21, 77) row of an earlier scan of Betti pairs, target by target, to 10⁻⁹. The second (G2) computes for each target whether K₇'s published value is in the set of its own expressions of at most five nodes, and requires that every such value within its window be reached by the blind search. If either fails, no result is read.
- **Variant, outside the decision rule.** κ_T⁻¹ and det(g) have two expressions: the published one above, and a second one (κ_T⁻¹ = b₃ − b₂ + Weyl, det(g) = Weyl·(N_gen + rank(E₈) + p₂)/2^Weyl) that agrees with it on the line b₂ = 21 and differs elsewhere. Which one is used off that line is itself a freedom of the dictionary (main §3.3, R2 and R3); the variant family (`F-BETTI-FICHE`; 4 160 pairs, (21, 77) included) reports its effect.

The preregistration has three amendments, each written before the run it governs. The first (2026-10-22) follows an external review: the dataset is refreshed (S3) with all uncertainties brought to 1σ, the windows are two-sided (the first run used only the side of each measurement that faces K₇'s value, which biased the search of the competitors towards that value), and the PDG range is the window of m_s/m_d. The second (2026-11-03), after a further external review, takes the windows of the six Planck ratios from the official chains (S3; the window of Ω_c/Ω_m narrows by a factor of six), and adds the control with no K₇ constant. The third (2026-11-11) takes the window of m_W/m_Z from the published masses, as for every other mass ratio (S3.3). None of them changes the question, the families, the grammar, the budget, the seed, τ_z or the decision rule.

### S4.2.2 Result

Both checks pass: the first reproduces the 28 rows of the earlier scan with no disagreement, and the second check finds 28 of K₇'s 33 published values among its own expressions of at most five nodes, every one of them within its window being reached. A further diagnostic (24 of the 33 published formulas lie within their windows: the 23 within 2σ of main §4, and m_s/m_d inside its PDG range) is not a statistic, since these formulas were chosen for (21, 77).

<!-- BEGIN S4-LEE-FAMILIES -->
| Family | N | reach ≥ 31/33 (as many as K₇) | P = (1 + n)/(1 + N) | best coverage | description cost, range (bits) | cost ≤ K₇ |
|---|---:|---:|---:|---:|---:|---:|
| K₇ (21, 77), blind search on its own vocabulary | 1 | 31/33 | n/a | 31 | 408.1 | n/a |
| alternative Betti pairs (published derivations) | 4 159 | 1 085 | 0.261 | 31 | 389.2 to 418.7 | 1 038 |
| invented vocabularies (generator of [M]) | 2 000 | 1 015 | 0.508 | 31 | 385.0 to 430.4 | 628 |
| alternative Betti pairs, variant derivations (outside the rule) | 4 160 | 723 | 0.174 | 31 | 391.3 to 417.6 | 548 |

Global p-value (the larger of the first two rows): **0.508**; threshold 0.01; preregistered outcome: **look-elsewhere effect not overcome**. The variant row does not enter the verdict. "Cost ≤ K₇" counts floating-point ties as ties (|ΔS_cost| ≤ 1e-09 bit; every tie is at the same (length, operations) pair as K₇).
<!-- END S4-LEE-FAMILIES -->

Per target, the blind search of K₇ and the frequency with which each family reaches the target:

<!-- BEGIN S4-LEE-TARGETS -->
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
<!-- END S4-LEE-TARGETS -->

Most targets are reached by every competitor: at five nodes and 2σ, the grammar covers them whatever the vocabulary. A control with no constant of K₇ makes this explicit. With an empty register, only the universal leaves and operations of the grammar remain (1 to 9, π, e, φ, γ, ln 2, the ζ values), and they reach 30 of the 33 targets, all but α⁻¹, m_τ/m_e and m_μ/m_e. Three scores must therefore be kept apart: the published formulas, the free search with K₇'s alphabet, and this control. The targets that discriminate are the few with very small relative uncertainties. α⁻¹ and m_μ/m_e are reached by nobody, K₇ included. Every competitor reaches the other 30 targets that K₇ reaches except m_τ/m_e, which K₇ and about a third of the competitors reach; the counts of the family table are exactly the counts on that one target. Ω_c/Ω_m shows the difference between the scores: its published value 27/32 lies outside the window of the chains (+2.46σ, main §4), yet the target is reached by K₇ with another expression, as by every competitor and by the control. A published value outside K₇'s five-node set (α⁻¹, m_μ/m_e and three others) is not available to the blind search, which may still reach the target with another expression.

### S4.2.3 Comparison with the earlier runs

<!-- BEGIN S4-LEE-HISTORY -->
| Quantity | first run (2026-10-17, dataset of v3.5, one-sided windows) | revision 1 (2026-10-24, refreshed dataset, two-sided windows) | revision 2 (2026-11-03, density ratios on the Planck chains) | revision 3 (2026-11-11, current dataset: m_W/m_Z from the published masses) |
|---|---|---|---|---|
| K₇ coverage | 32/33 | 31/33 | 31/33 | 31/33 |
| K₇ description cost (bits) | 395.6 | 409.2 | 408.1 | 408.1 |
| alternative Betti pairs (published derivations): reach as many as K₇ | 4 159 of 4 159 (P = 1.000) | 1 085 of 4 159 (P = 0.261) | 1 085 of 4 159 (P = 0.261) | 1 085 of 4 159 (P = 0.261) |
| invented vocabularies (generator of [M]): reach as many as K₇ | 1 635 of 2 000 (P = 0.818) | 1 015 of 2 000 (P = 0.508) | 1 015 of 2 000 (P = 0.508) | 1 015 of 2 000 (P = 0.508) |
| alternative Betti pairs, variant derivations (outside the rule): reach as many as K₇ | 4 160 of 4 160 (P = 1.000) | 723 of 4 160 (P = 0.174) | 723 of 4 160 (P = 0.174) | 723 of 4 160 (P = 0.174) |
| global p-value, outcome | 1.000, look-elsewhere effect not overcome | 0.508, look-elsewhere effect not overcome | 0.508, look-elsewhere effect not overcome | 0.508, look-elsewhere effect not overcome |
| targets reached by nobody | α⁻¹(0) | α⁻¹(0), m_μ/m_e | α⁻¹(0), m_μ/m_e | α⁻¹(0), m_μ/m_e |
<!-- END S4-LEE-HISTORY -->

The first run, on the dataset of version 3.5 with one-sided windows, had every alternative Betti pair at K₇'s score. Two targets change. m_μ/m_e, whose uncertainty in the 3.5 dataset (0.02) was some four thousand times the CODATA value (4.6 × 10⁻⁶), is now reached by nobody, K₇ included, which lowers K₇'s score by one and every competitor's alike. m_τ/m_e, reached by every alternative Betti pair and most invented vocabularies in the first run, is now reached by K₇ and by about a third of the competitors, its uncertainty having shrunk from 0.23 to 0.18. It is the only target that separates competitors: those that reach as many targets as K₇ are exactly those that reach m_τ/m_e (S4.2.2). Revision 2 changes the windows of six ratios that are not discriminating: the counts of competitors reaching as many as K₇ are therefore those of revision 1, while the costs move (K₇, 409.2 to 408.1 bits). Revision 3 changes the window of m_W/m_Z alone: every competitor still reaches it, so the counts are again unchanged, and the number of competitors that cost at most as much as K₇ moves (alternative Betti pairs, 1 163 to 1 038; invented vocabularies, 698 to 628). The figures of revisions 1 and 2 are historical. The verdict does not change.

### S4.2.4 What the test does not cover

The counts are descriptive. They record an absence of discrimination in these families and windows, not a measurement of statistical power. The global p-value of 0.51 is not a probability that K₇ is right or wrong: with 30 targets reached by everyone, two by no one and one that separates, the coverage score has little discriminating power in this protocol. The test does not vary the gauge group or the holonomy beyond the Betti numbers (there is no public rule for re-deriving the register in that case), does not consider other forms of an observable (an angle against its sine squared) except for the unit of δ_CP, and does not look beyond five nodes, where several of K₇'s formulas lie. These freedoms remain in the residue register of main §3.3 (the formula assignments, R4; the grammar and vocabulary, R5; the unit of δ_CP, R6). Nor does the test use the literal register of main §3.1 (S4.2.1).

## S4.3 Descriptive diagnostics of version 3.5 (archived)

Version 3.5 reported the following analyses of its formula set as evidence against cherry-picking. They were computed on the formula set and dataset of version 3.5 and have not been recomputed. They describe how the formulas use the constants; they do not price the choice of formulas, which is what S4.2 does, and they are no longer read as evidence.

- **Complexity against deviation.** A random-forest regression of |deviation| on formula features (number of constants, largest constant, number of operations, sector), with leave-one-out cross-validation, gave R² = −0.518: formula complexity did not predict the size of the deviation.
- **Sensitivity.** Perturbing each of the 20 constants by ±1 gave a 20 × 33 sensitivity matrix with 19 non-zero singular values (3.50, 2.54, 2.39, 2.14, 2.11, …) and a correlation of −0.083 between sensitivity and deviation.
- **Effective rank.** The 20 × 33 binary constant-usage matrix had an effective rank of 15.53; 12 singular values carried 90 % of the variance and 17 carried 99 %. Version 3.5 divided 33 by 15.53 and called the ratio, 2.13, an "overdetermination ratio" characteristic of a system that is not fitted. The ratio counts the 33 relations as independent, which they are not (main §4), and a usage matrix cannot tell a fitted formula from an unfitted one; the reading is withdrawn.
- **Shared constants.** Of the 528 pairs of observables, 155 share at least one structural constant, and the 33 form one connected component; 51 pairs of deviations have |ρ| ≥ 0.5.
- **Reading of the Sieve scorecard.** Version 3.5 of this supplement (§S4.4 there) described m_H/m_W as the "unique survivor at exact rank 1", and Koide and n_s as passing the battery. That reading left out the vocabulary-freedom result of the same scorecard (S4.1).

## S4.4 Coincidence probabilities of versions 3.4 and 3.5 (archived)

Version 3.5 stated that among 192 349 alternative configurations, none outperformed the framework (P < 5 × 10⁻⁶). The Monte Carlo behind that figure kept the 33 formulas of K₇ fixed and re-evaluated them with the invariants of each alternative; no alternative searched for its own formulas. Since the formulas had been chosen for (21, 77), (21, 77) won by construction. Several of the 33 predictions did not depend on the configuration at all, and 1/192 349 was simply the floor of the estimator. The figure is withdrawn; S4.2 is the test that lets the alternatives search.

Version 3.4 reported joint coincidence probabilities of 10⁻³⁴⁶ (uniform null) and 10⁻¹³³ (algebraic null) for the 33 relations. Both are withdrawn. The uniform null treats the predictions as random numbers in [0, 50 %] of deviation, which no formula search produces. The algebraic null compares K₇'s *selected* formulas with *random* formulas built from the same constants, so it does not price the selection: a competitor allowed to select its own formulas, as in S4.2, does as well. The tables are kept as a record of what was reported.

| Uniform null, deviations in [0, 50 %] | Statistic | df | p-value |
|---|---|---|---|
| χ² | 1063 | 33 | 5.0 × 10⁻²⁰² |
| Fisher combined | 1100.5 | 66 | 2.2 × 10⁻¹⁸⁷ |
| KS (pull normality) | 0.189 | n/a | 0.165 |
| Combined | n/a | n/a | 10⁻³⁴⁶ |

| Algebraic null (4 188 086 formula values from the 20 constants) | K₇ (3.4 dataset) | Random formulas (median) |
|---|---|---|
| Mean deviation | 0.73 % | 4.1 × 10⁹ % |
| Matches within 0.01 % | 5 | 0 |
| Matches within 1 % | 28 | 0 |

The pull distribution of version 3.4 had mean −0.774 and standard deviation 5.62 (reduced χ² = 32.2, driven by δ_CP and α_s); these figures refer to the 3.4 dataset and are superseded by the comparisons of main §4.

## S4.5 Reproducibility

- **Scorecard (S4.1).** [M, §4.3], with the frozen inputs [S-frozen].
- **Look-elsewhere null (S4.2).** Test script `canonical/scripts/k7_v3_6_lee_null.py` (Sieve engine at commit `601283f`, grammar verified by its SHA-256 hash, depth 5, τ_z = 2, seed 20261017); result `canonical/results/k7_v3_6_lee_null.json` (10 319 vocabularies, 2 h 50 on three processes); ties of the description cost are counted by a post-processing script, `canonical/scripts/k7_v3_6_lee_null_closeout.py`. The tables of S4.2 and the figures of main §7.2 are generated and checked by `canonical/scripts/k7_v3_6_s4_tables.py`. The earlier runs are the same script before each amendment, each at its own commit, read from git by the generator. The test script, the post-processing script, the dataset as read by the run, the preregistration with its amendments, the result and the results of the earlier runs are deposited with their hashes in the public repository (Arithmon/K7, `publications/validation/v3.6/`, which keeps the `canonical/` paths); the test runs from there against a clone of the Sieve.
- **Archives (S4.3, S4.4).** The scripts of the 3.4 and 3.5 releases; they are not maintained.

## Author's Related Works

- **[M]** B. de La Fournière, "A reproducible standard for arithmetic coincidence claims in fundamental physics," Zenodo [10.5281/zenodo.20728964](https://doi.org/10.5281/zenodo.20728964) (2026). The Sieve methodology and its four-null scorecard for the K₇ relations.
- **[S-frozen]** B. de La Fournière, "Counting Coincidences: frozen inputs" (observable list and expression grammars), Zenodo dataset [10.5281/zenodo.20666878](https://doi.org/10.5281/zenodo.20666878), v1.0 of 12 June 2026.

---

*The K₇ Framework: Supplement S4: Sieve and Look-Elsewhere Diagnostics*
