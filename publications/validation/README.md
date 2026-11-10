# Statistical validation

| Directory | What it holds | Status |
|---|---|---|
| [`v3.6/`](v3.6/) | The preregistered look-elsewhere test of version 3.6: producer, dataset, preregistration, results, hashes, and the command to rerun it | current |
| [`legacy/v3.3/`](legacy/v3.3/) | The validation pipeline of version 3.3 (fixed-formula configuration search, null models, Bayesian comparison) | archived, not maintained |

## Version 3.6

In the test of version 3.6, each competitor searches for its own formulas in the same grammar, at the same budget, with the same freedom of assignment and of unit. K₇ reaches 31 of the 33 targets; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many, and none reaches more. P_global = 0.51 against a preregistered threshold of 0.01: the look-elsewhere effect is not overcome. See [`v3.6/README.md`](v3.6/README.md), the main paper (§7) and supplement S4.

## Earlier versions

The figures reported by versions 3.3 to 3.5 are withdrawn: the rank among several million configurations, the null-model and coincidence probabilities, the Bayes factors and the mean deviation. They came from searches in which the alternatives were scored with the formulas of K₇ and did not search for their own, so that (21, 77) won by construction. The scripts and reports are kept in `legacy/v3.3/` as a record of what was reported. The statistics refresh of version 3.4 was run in the author's working repository and was never deposited here.

The summary for readers is [Statistical Evidence](../references/STATISTICAL_EVIDENCE.md).
