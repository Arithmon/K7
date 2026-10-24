# Changelog: K₇ framework paper, version 3.6 (draft)

*Draft branch `v3.6-draft`. Version 3.5 (Zenodo 21296168) remains the published version; the files `k7_framework_3_5_*` are unchanged. Supplement S4 (look-elsewhere null and descriptive diagnostics) is included from batch 5. LaTeX and PDF are not yet regenerated.*


**Batch 6 (2026-10-24): second outside review of the draft.**
- Look-elsewhere test: the alphabet actually tested is declared (§7.2,
  S4.2.1): the nineteen integers of the 3.5 Monte Carlo register, without
  dim E₇ = 133 and α_sum = 13 and with κ_T⁻¹ = 61, not literally the
  register of §3.1; F-BETTI re-derives only H*, κ_T⁻¹ and det(g) and holds
  N_gen = 3 (author's decision: declared, not rerun). The 30 / 2 / 1
  structure of the targets stated in §7.2; P_global = 0.51 is not a
  probability about K₇.
- "At most as many relations can be exact as the sector has parameters"
  withdrawn (§4.2, S2.6): A23, A29 and A30 hold together; the largest
  compatible density subsets have three relations (A29, A30 and one of
  A23, A26, A27, A33), computed.
- m_b/m_t rejected as an exact equality in the scheme declared in R7
  (author's decision): five proximities, no "scheme assignment" class;
  the classes are 24 / 2 / 5 / 1 / 1. §4.2 aligned with rule G of §11
  ("none of these statements is a rejection" withdrawn).
- "Geometric pre-specification" no longer listed among what survives the
  look-elsewhere tests (§7.1, §7.3, S4.1; author's decision): the origin of
  the vocabulary is stated as a fact, not as evidence of a selection made
  before the data, since the grammar was frozen after the formulas.
- S1: the Chen–Hong compatibility conclusion withdrawn (the theorem does not
  apply to K3 × T² × ℝ, and that shows nothing about the neck); the PINN
  holonomy-score description withdrawn (it cannot be 0 for G₂ holonomy and
  3.5 for a flat metric; Hol ⊆ G₂ is not Hol = G₂); the "b₂ = 21 > 20 =
  max ρ" building-block argument withdrawn (TCS b₂ = rk K₊ + rk K₋ +
  rk(N₊ ∩ N₋)); the coframe of §11.2 stated as that of §11.1.
- Dataset (author's request): B17 formula made explicit (B16 × A08; A09 ×
  A08 would give 234.29); Y_p labelled PDG 2024 BBN review, eq. 24.3 (was
  "Planck 2018"); S3 notes the m_μ/m_e uncertainty corrected in the
  refresh (0.02 → 4.6 × 10⁻⁶). §11.2: m_s/m_d given as the PDG range, not
  20 ± 2. S2, A03: cross-reference to S2.7.

**Batch 5 (2026-10-24): look-elsewhere null rerun, S4 rewritten, S2 status column, S1 pass.**
- The preregistered look-elsewhere null rerun on the refreshed dataset with
  two-sided windows (amendment 1): K₇ reaches 31/33 by blind search on its
  own vocabulary; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000
  invented vocabularies reach as many, none more; P_global = 0.51,
  LEE-RETRAIT (unchanged). α⁻¹ and m_μ/m_e are reached by nobody; the only
  target that separates competitors is m_τ/m_e. Abstract and §7.2 report
  this run; the first run (3.5 dataset) is kept as a comparison.
- S4 rewritten: the Sieve scorecard with its N2 result (the 3.5 "unique
  survivor" reading withdrawn there too); the design, gates and results of
  the null, with tables generated from the result files
  (`k7_v3_6_s4_tables.py`, which also checks the figures of main §7.2); the
  3.5 diagnostics (random forest, SVD, effective rank, shared constants)
  archived as descriptive, the "overdetermination ratio" reading withdrawn;
  the 3.4 coincidence probabilities archived as withdrawn, with the reason.
- S2: each table carries the status and pull of every relation, generated
  from the table of main §4.1 (`k7_v3_6_s2_status.py`); cross-reference to
  S2.7 fixed; m_u/m_d uncertainty stated at 1σ (90% CL ÷ 1.645); the
  look-elsewhere result cited in S2.7.
- det(g) declared like κ_T⁻¹ (R2, §3.1, S2.1): its two expressions in the
  constants, p₂ + 1/(b₂ + dim G₂ − N_gen) (used, App. B) and
  Weyl · α_sum/2^Weyl, agree on the line b₂ = 21 and differ elsewhere;
  §3.1 had defined det_num by the second and det_den by the first. No value
  changes at (21, 77).
- S1 pass. Lean references checked against Arithmon/K7-Lean: seven cited
  declaration names did not exist (now the actual names, or the claim of
  formalization removed); the two G₂ items listed as "remaining" are proved
  (one by `rfl`, so not a theorem about two characterizations); the file
  count dropped; `torsion_satisfies_joyce` described as what it is (a
  comparison with a fixed threshold, not Joyce's constant); the Selberg-bridge
  and "selection principle" readings withdrawn. "Exceptional Chain Theorem",
  "VERIFIED"/"STRUCTURAL" statuses, the circle–U(1) analogy and the
  "topological bound" 14/99 withdrawn; λ₁ match corrected to 0.05% (was
  0.08%) and λ₁·H* to 12.342 (was 12.3364); Pell solution stated correctly
  (99 + 14√50 = (7 + √50)², the latter of norm −1); undefined α_B notations
  replaced. §8.3: the lattice sketch N₁ ⊕ N₂ ⊕ ⟨2⟩ withdrawn (not an
  orthogonal decomposition of a unimodular lattice; N₁ ⊥ N₂ is the
  orthogonal gluing excluded by parity). §10: det(g) listed by the
  expression used (App. B) with the second one declared. PINN described as
  training on a model, not on K₇.

**Batch 4 (2026-10-22): outside review of the v3.6 draft, geometry.**
- The Joyce–Karigiannis ℤ₂³ route does not currently realize (21, 77): its
  quotient cohomology (0, 22) is incompatible with the stated action (the
  H²(K3) character forces b₂ ≥ 5 and b₃ ≤ 16 for all 512 torus-character
  triples; the product action gives (1, 6, 16)), and the stated involution
  profile requires Picard rank ≥ 17, not 1 (audit of 2026-09-16 and its
  checkers, rerun). S1 §8.3–§8.4 rewritten, main §1.2, §2.3, §9.1 corrected;
  no construction of a compact G₂ manifold with (21, 77) is claimed.
- G₂ normalization corrected (S1 §11.1, §11.5, §12.3, §12.5): g_{cφ} =
  c^{2/3} g_φ, so φ_ref = D^{3/14} φ₀ and g_ref = D^{1/7} g_{φ₀} for
  D = 65/32 (the earlier c = D^{1/14} induced det g = D^{1/3}); the
  index-contraction reconstruction of g from φ, which uses a background
  metric, replaced by the intrinsic formula; the coframe is orthonormal for
  g_{φ₀}, not for g_ref.
- S1 §9 restructured: Betti spectrum conditional on existence; the
  "H³ = local ⊕ global, 35 + 42" splitting withdrawn (35 is a fibre rank, not
  a subspace of H³); 42 is not an Euler characteristic.

- Comparisons harmonized: all uncertainties at 1σ (PDG summary entries quoted
  at 90% CL divided by 1.645: m_u/m_d, m_b and the Type II quark masses);
  m_s/m_d kept as the PDG range 17–22 with no pull; error propagation
  described as neglecting correlations (an approximation, not a bound);
  neutrino density stated as neglected in the flatness closure.
- One vocabulary: pull (descriptive), tension (2σ–3σ), proximity (beyond
  3σ, excluded as an exact equality), rejection only under the rules of
  §11. The single score "25 of 33 within 2σ" replaced by a six-class
  breakdown generated from the dataset: 24 within 2σ, 2 tensions (m_τ/m_e,
  m_W/m_Z), 4 proximities, 1 inside the PDG range, 1 non-Gaussian (θ₂₃),
  1 scheme assignment (m_b/m_t).
- CKM overdetermination declared (R12): sin θ₂₃ = Aλ², and 7/31, 83/99,
  1/24 are 2.6% apart as exact equalities. The count "26 independent
  quantities" withdrawn: three overdetermined sectors are identified, and
  a complete dependency audit has not been done.

- Decision rule (§11) rewritten for point values (author's decision): a
  relation stated as exact is rejected when a measurement's 3σ interval
  excludes its value (general rule G); D1 tests 197° itself, not the band
  [182°, 212°] (a point value and a band are different hypotheses); D2
  applies in either octant; D3 rejects each lepton relation separately.
- §8: the formalization "verifies the arithmetic identities it states"; it
  does not establish internal consistency of the relations taken together.

**Batch 3 (2026-10-22): leptons, no primary relation.**
- R8 and §6.1: none of the four lepton relations is declared primary; a
  selection made after the values are known is a dictionary choice, not a
  result. m_μ/m_e = 27^φ is a proximity like α⁻¹ and sin²θ_W; the lepton sector
  supplies no relation specific to K₇ that agrees with measurement at its
  precision (Koide's 2/3 predates the framework and is reached by every invented
  vocabulary). τ-mass measurements test 3477 against Koide (D3), not 27^φ.
- Dataset refreshed to the most recent measurements (author's decision,
  2026-10-22): PDG 2026, NuFIT 6.1 (normal ordering, IC24 with SK atmospheric
  data, one variant for all four entries), Planck 2018 (one column,
  TT,TE,EE+lowE+lensing), CODATA 2022; ratios computed from the published
  masses with propagated errors (`canonical/scripts/k7_v3_6_exp_refresh.py`).
  Corrections found on the way: m_μ/m_τ and m_τ/m_e had overstated errors
  (×13 and ×1.3), Q_Koide used the PDG 2022 τ mass, m_b/m_t had an error with
  no source, h matched no Planck column, A16/A18 are sin θ (λ and Aλ²), not
  sin²θ.
- §4 table regenerated from the JSON (`k7_v3_6_table_sec4.py`): 25 of 33
  within 2σ (was 28). Outside: six proximities (α⁻¹, sin²θ_W at −7.5σ with
  PDG 2026, m_μ/m_e, m_μ/m_τ at +21σ, m_τ/m_e at −2.1σ, m_W/m_Z), m_b/m_t as
  a scheme assignment (R7 extended to the mass scheme), sin²θ₂₃ in octant
  tension but inside the NuFIT 3σ range (the "≈ 4σ" was a Gaussian reading of
  a non-Gaussian profile). δ_CP: 212 (+26/−36)°. Counts without det(g) / κ_T,
  abstract, §6.1 and conclusion updated. §7 (look-elsewhere) pending the rerun
  of the null on the refreshed windows.
- Cosmological overdetermination declared (R11, §4.2): seven density relations
  on two independent densities, mutually incompatible as exact equalities
  (Ω_Λ/Ω_m = 113/52 by A27, 61/28 by the inverse of A33, 2.186 from Ω_DE;
  Ω_c/Ω_b = 43/8 vs 27/5); none selected. The 33 relations bear on 26
  independent quantities; stated in the abstract, §4.2, §4.5, §12.
- S3 rewritten: the dataset as a ledger (33 counted relations; 62 conditional
  or diagnostic entries with a status each), sources and conventions of the
  refresh, corrections declared; tables generated from the JSON. Withdrawn:
  "exact matches", sector rankings, Koide "with no fitting", the old table of
  neutrino angles (θ₂₃ = arcsin(75/99), not the dataset's relation).
- S2 rewritten ("The 33 relations: arithmetic, dictionary choices and
  status"): the arithmetic of each relation and the residue entries it uses;
  N_gen as an integer identity (no index theorem); expression counts reported
  as vocabulary freedom, with the second formulas the corpus gives for the
  same observables (λ_H, Ω_DE, m_c/m_s, Ω_Λ/Ω_m, the three angles, δ_CP);
  withdrawn: statistical uniqueness (192 349 alternatives), the 3477
  "cross-confirmation" (circular: the target was ln of the measured ratio),
  Ω_m = Ω_DE/√5, the Fibonacci–Lucas "embedding" as evidence, and the
  Appendix F contingency plan for 62/69, a repair clause excluded by D1.
- S1, targeted pass: erratum banner removed (integrated in batch 1); the
  motivation chain ends in assigned relations, not "95 observables"; Weyl's
  "triple identity", the "exceptional chain theorem", the "triple origin" of
  p₂, τ as "a geometric constant" and the readings of κ_T (torsion capacity,
  matter degrees of freedom) withdrawn or restated as arithmetic; b₂, b₃ no
  longer "NK-certified" in the Betti table (contradicted §8.3); the "Joyce
  threshold ε₀ = 0.1, 224× margin" withdrawn (Joyce's constant depends on
  bounds not computed here); PINN det(g) "confirmation" and the "8/8
  validation" of the normalization target withdrawn (the training is
  constrained to it); λ₁ = 6π²/475 conditional on b₂(M₁) = 11, and the
  λ₁·H* regularity reported as an empirical scan result.

**Batch 2 (2026-10-20): reframing of the main paper (physics_main.md).**
Decisions of the author (2026-10-17 and 2026-10-20): full reframing; δ_CP as a
phase with the unit declared; the 33 Type I relations in front, Types II–IV as
conditional extractions; the selection-principle discussion rewritten into the
text.
- New §3 "The correspondence and its dictionary": the twenty constants with a
  status column; the grammar (frozen after discovery); the absence of an
  assignment rule declared (the "metric uniqueness" / "functionals of the
  metric" statements withdrawn); the residue register R1–R10; claims and
  non-claims; the privileged-candidate status.
- §4: one table of the 33 relations from observables.json (PDG 2025, NuFIT
  6.1, Planck 2018, CODATA 2022) with deviation, pull and status; 28 within 2σ,
  five outside (α⁻¹, sin²θ_W, m_μ/m_e, m_W/m_Z as proximities; sin²θ₂₃ ≈ 4σ,
  octant). Counts with and without det(g) and κ_T. "95 observables" and
  "mean deviation 0.73%" withdrawn; Types II–IV not counted as predictions
  (Type II read in MeV is a unit assignment; its earlier description as
  "ratio × anchor" did not match the dataset).
- δ_CP: prediction stated as the phase 2π·197/360; the unit is a dictionary
  assignment (R6); J reported as a derived observable.
- Leptons: the four relations declared mutually incompatible; Belle II cited
  for m_τ. (Batch 2 declared m_μ/m_e = 27^φ primary; withdrawn in batch 3.)
- §5: consistency checks on an assumed SM content; comparisons at M_Z (and
  α at q² = 0), no common-scale triplet; the GUT boundary reading, the two-loop
  SUSY running and the SUSY spectrum withdrawn; the B-test as an algebraic
  identity among the framework's values (no "exact scale").
- §2: branching chain, not a breaking mechanism; heterotic 10D vs M-theory 11D
  separated; N_gen = 3 an integer identity, not an index theorem.
- §7: Sieve scorecard reported with its N2 result (m_H/m_W and n_s do not clear
  N2; Koide a tie); "unique survivor" withdrawn; P < 5·10⁻⁶ withdrawn and
  replaced by the preregistered look-elsewhere null (LEE-RETRAIT, 32/33
  reached by all 4 159 Betti alternatives and 1 635/2 000 invented
  vocabularies); 10⁻³⁴⁶ / 10⁻¹³³ out of the main text; the "14 derivations"
  argument reversed; SVD / random forest / 2.13× moved to S4 as descriptive.
- §8: formal verification reduced to one method paragraph.
- §10: the "why Lorentz invariance?" analogy and the "unique holonomy with
  the stabilizer chain" claim withdrawn (Spin(7) contains it).
- New §11: decision rule with no repair clause (D1–D6).
- §12: what K₇ does not fix; list of withdrawn claims.
- Not yet: supplements S1–S4 (status per relation in S2, status column in S3,
  the new null in S4), .tex regeneration, title, release audit.

**Batch 1 (2026-10-17): errata integrated into the sources.**
- §1 (K3 closed-form bound concerns an auxiliary quantity): main §2.3 and §8.5,
  S1 §8.3 rewritten; no certified Ricci-flat K3 bound is claimed; the certified
  K3 atlas [K3A] (concept 22047469, no metric claim) cited.
- §2 and §7.4 (datum 𝒟₀ of [E] not realisable; (L4) obstructed for it): §9
  rewritten (layer conditional on a datum not instantiated; global existence
  needs a realisable datum first), §1.3, §2.3, §8.5, status lines, [E] entry.
- §3: [B] cited by its concept DOI 18920367 (md and .tex); [A], [C], [D] also
  moved to their concept DOIs (18643069, 19708915, 20039065).
- §5 (α⁻¹(0)): already in S2 since 2026-10-02.
- §7.1–7.3: 14 axioms (4 prediction-chain + 10 interval certificates)
  everywhere; the KK_YM_EFT sentence replaced; methodology paper is the
  preprint 20728964 (dataset 20666878 kept for the frozen inputs).
- §7.5–7.6: S1 global properties stated as assumed; Betti numbers no longer
  "certified by NK"; the κ_T / Joyce-regime sentence withdrawn.
- Lean code link → Arithmon/K7-Lean; [E] dataset DOI 21209412 cited separately.
- Not yet: abstract and summaries (part of the reframing), .tex regeneration
  (build_3.6), decisions 2–4 (leptons, M_Z, δ_CP), Pontryagin in the .tex.
