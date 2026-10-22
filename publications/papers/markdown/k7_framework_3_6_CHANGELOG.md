# Changelog: K₇ framework paper, version 3.6 (draft)

*Draft branch `v3.6-draft`. Version 3.5 (Zenodo 21296168) remains the published version; the files `k7_framework_3_5_*` are unchanged. Supplement S4 (look-elsewhere null and descriptive diagnostics) is not yet included: it awaits a rerun of the null on the refreshed data. LaTeX and PDF are not yet regenerated.*


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
