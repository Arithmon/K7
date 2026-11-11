# Changelog: K₇ framework paper (formerly GIFT)

## v3.6 (November 2026)

**Batch 14 (2026-11-11): m_W/m_Z by the mass-ratio rule; supplements in the present tense; plain vocabulary.**
- **A number changes.** m_W/m_Z is computed from the published masses, as every other mass ratio: 80.3625(77)/91.1879(20) = 0.881285(87), correlations neglected, in place of the ratio line of the PDG summary, 0.88136(15). The published value 37/42 moves from −2.7σ to −3.8σ and from "tension" to "proximity". The classes are now 23 within 2σ, 2 tensions (m_τ/m_e, Ω_c/Ω_m), 6 proximities, 1 in range, 1 non-Gaussian. Main §4, S2, S3 and the public pages are regenerated.
- **Dataset.** `observables.json` carries version 3.6; the field `n_exact` is removed; two conditional entries are set to the value of their formula (B01 = 2.160247, B04 = (14 − π)³ = 1280.26).
- **Look-elsewhere test, revision 3.** The preregistration receives a third amendment before the run (window of m_W/m_Z alone). Result: nothing in the verdict changes. K₇ reaches 31 of 33; 1 085 of 4 159 alternative Betti pairs and 1 015 of 2 000 invented vocabularies reach as many; global p-value 0.51. m_W/m_Z is still reached by every competitor. The number of competitors that cost at most as much as K₇ moves (1 163 to 1 038 and 698 to 628). The revision-2 result joins the history of the public deposit.
- **§9.2 (the chain of locks) is removed**; §9 is renumbered (9.1 what an existence proof would need, 9.2 what depends on existence, 9.3 relation to the companion papers).
- **DESI.** §11.1 reports the DESI DR2 results beside the classes [61]: DESI alone, Ω_m = 0.2975 ± 0.0086 (1.9σ to 2.0σ from the three density relations); DESI with the CMB, Ω_m = 0.3027 ± 0.0036 and H₀ = 68.17 ± 0.28 (3.1σ to 3.4σ on the density relations, 3.0σ on h). The FCC-ee row leaves the timeline, the relation it would have tested being already rejected.
- **Vocabulary.** Dataset identifiers, rule labels and internal names of tests and verdicts leave the prose of the main paper and of S1 to S4; they remain as row labels in tables and as field names where a file is cited. Section titles say what the section contains.
- **Supplements.** S1 to S4 are written in the present tense; each gathers what changed in one section, "Changes since version 3.5".
- PDFs rebuilt (main 39 pp., S1 28, S2 15, S3 17, S4 11).

**Batch 13 (2026-11-11): the main paper states the present position; out-of-sample tests.**
- The body is written in the present tense. What versions up to 3.5 said and version 3.6 no longer says is listed once, in the new Appendix D, with pointers to the erratum; the corresponding passages leave §1.1, §2.3, §2.4, §3.1, §3.2, §4.2, §4.3, §4.5, §5.3, §5.4, §6.1, §7.1, §7.2, §9, §10.3, §11 and §12.1. No number, class or verdict changes.
- Abstract shortened (507 to 333 words). §3.4 reduced to what is claimed, each limit being stated where it acts.
- §11.2 becomes "Out-of-sample tests and timeline": a formula retained in a window of half-width w falls by chance in a later window of half-width w/k about once in k. JUNO's first measurement of sin²θ₁₂ (0.3092 ± 0.0087) and its projected six-year precision (about 0.5%) are added against 4/13, with cosmological surveys in the timeline; references [58], [59].
- §7.2: seven targets are counted as reached although K₇'s published value lies outside the window; m_τ/m_e, the one separating target, is among them, and this is now said.
- R7: the comparison of λ_H with the tree-level m_H²/(2v²) is declared as a scheme choice, with the MS-bar value; reference [60].
- §7.3 gains out-of-sample exposure as a third item; conclusion rewritten accordingly. PDFs rebuilt (main 41 pp., S4 11 pp. with the three new references).

**Batch 12 (2026-11-11): release preparation.**
- The "(draft)" stamp is removed from the title pages; `.tex` and PDF rebuilt. No statement or number changes.
- The LaTeX sources and PDFs of version 3.6 enter the public repository (`publications/papers/tex/`, `pdf/`), with the current preamble.
- Repository surfaces that depend on the deposit (citation files, structure, paper pages, changelog highlights, reference data) are regenerated for 3.6.

**Batch 11 (2026-11-10): look-elsewhere test deposited.**
- The producer of the look-elsewhere test, its closeout, the dataset as read by the run, the preregistration with its two amendments, the result and the results of the two earlier runs are deposited in the public repository, `publications/validation/v3.6/`, with their hashes. S4.5 and S3.8 say where; S3.8 no longer says "available on request pending public deposit" for the dataset. No figure changes.

**Batch 10 (2026-11-06): [WNE] located.**
- [WNE] is now on PhilArchive; its bibliography entry gives the record, philpapers.org/rec/DELWNE. No other change.

**Batch 9 (2026-11-03): external review of the release draft.**
- Density ratios A25, A26, A27, A29, A30, A33 computed on the published Planck chains, with their correlations. Ω_c/Ω_m moves from 0.839(11), +0.4σ, to 0.8390(19), +2.5σ: the classes become 23 within 2σ and 3 in tension. No other class changes.
- Planck's Ω_m includes neutrinos, while 5/32 + 27/32 = 1: declared as a defect of compatibility, the denominator not being replaced.
- Two withdrawn figures removed from §9.2: ‖𝔐⁻¹‖ ≤ 1.246 (now ≤ 2.76, ≤ 1.076 normalised, as in [E]) and "~34% below an earlier recomputation".
- §2.3 and S1 §9.2: the spectral analysis of [B] is no longer called consistent with (21, 77); its multiplicities rest on decompositions withdrawn in S1.
- §11: the rule is anchored on the reference series, with an update procedure; contradicting measurements (SH0ES on h, CDF II on m_W) are reported beside the class. This is a clarification made after the problem was identified, frozen prospectively. Survivors of overdetermined sectors are not selected predictions. The abstract and §12.5 no longer call δ_CP the sharpest test.
- Status box: joint system, individual relations and wider programme are kept apart. The coefficient 10 of A06 is declared a choice of formula.
- Look-elsewhere test rerun on the corrected windows (amendment 2), with a witness that has no K₇ constant: it reaches 30 of the 33 targets. K₇ stays at 31/33, the counts of competitors and P_global = 0.51 are those of revision 1 (the six windows changed do not discriminate), LEE-RETRAIT; K₇'s cost moves from 409.2 to 408.1 bits, and the costs of the competitors with it. S2.7 corrected accordingly.
- §10.1 and S1 §12.4: transcription and Fano-plane statements corrected; imported q_AR declared in §9.2.

**Batch 8 (2026-11-03): NuFIT 6.1 checked against the official table.**
- The four entries A12–A15 were compared with the NuFIT 6.1 parameter table (archived copy of www.nu-fit.org, snapshot of 2026-09-12; the live site was unreachable on 2026-10-22 and 2026-11-03). Central values, 1σ errors and the δ_CP 3σ range all agree.
- One correction: the upper 3σ bound of sin²θ₂₃ was given as 0.582; the table gives 0.584, consistent with θ₂₃ < 49.86°. 6/11 stays inside the range; no pull or status changes.
- Release audit, first fixes: "six classes" corrected to five (§4.5, against §4.2); the overdetermined sectors in §12.2 corrected from two to three (CKM added); three sources named without a bibliography entry now cited: Donaldson [53], Camere [54], the Zhou series [55].
- [B10–B15, B18, B19] reclassified: "cascade of Type I relations; no independent content" withdrawn. These eight entries are legacy values whose derivation is not documented in the dataset, retained for traceability and not counted as predictions (dataset, S3 §1 and table, main §4.5). The 33 relations and their breakdown are unchanged.
- Release audit, minor fixes: S1, S2 and S4 reference sections made consistent with the shared bibliography; dead cross-references removed; residual French and internal jargon removed from the main text.
- The v3.5 erratum is now a bibliography entry, [ERR], at a fixed commit; its nine citations read [ERR, §N].
- Dataset labels and metadata corrected, no value changed: title and version, Lean build block (commit 34ce857: 156 files, 14 axioms), concept DOIs, `lean_theorem` of the 33 relations (the theorem of each relation, replacing `observables_certified`), B07 and C19–C21 formula labels, A08 note; summary statistics recomputed (they predated the refresh); CSV and LaTeX exports regenerated.
- C18 disclosed in S3: its comparison is mismatched (Vol_e − Vol_μ against ln(m_τ/m_μ), which the instanton relation pairs with Vol_μ − Vol_τ); C20 and C21 use the same difference. Entries kept as computed.
- LaTeX regenerated: subscripts and superscripts typeset, table widths set from the generator.
- C14 renamed n_SD: its value 3 is the count of positive eigenvalues of the K3 intersection form, not the rank of a mass matrix (that rank is 22).
- Second release audit: search space corrected in §6.2 (three of the six self-dual cycles among the 57); α = e^K no longer listed in S3 among the choices selected against the data; titles of [A], [B], [C] aligned with their Zenodo records; PDF pipeline repaired (S3 related works and S1 background kept, starred symbols, lists, PMNS and CKM superscripts). The unused `observables_latex.tex` export, which did not compile, is removed.
- Release audit, notes closed: "main §" on copied cross-references; author accent; 47 removed from the constants it is not among; unreferenced companion paper removed; earlier Lean module located at its commit; notation J₃(𝕆), Aut(𝕆), φ₀, Λ³(ℝ⁷); realis- throughout; PDG 2024 cited for Y_p, [56].

**Batch 7 (2026-10-31): title, and the companion philosophy paper cited.**
- Title: "The K₇ Dictionary: Testing G₂ Topology against Particle Physics and
  Cosmology" (author's decision), replacing "The K₇ Framework: Conditional
  Topological Relations for Standard-Model Parameters from G₂ Holonomy and
  E₈×E₈ Structure". The series keeps the name "The K₇ Framework".
- The companion philosophy paper [WNE] ("Where Necessity Ends: Selection by
  Joint Compatibility") is cited: §3.5 (the three states and the condition of
  independence come from it; its §13 audits version 3.5) and §12.2. It was
  left uncited during its anonymous review, which has ended.
- The wording neutralised for that review is restored: §12 "Where the
  Necessity of K₇ Ends", §12.2 "Where its necessity ends", §3.3 and §7.3
  ("where the framework's necessity ends").
- Not yet: .tex regeneration, release audit.

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

- Lean (S3.7): a K7-Lean alignment (commit 34ce857, merged
  into `main`, PR #167) adds `relations_v36_certified`, one statement per
  relation tying its closed form to its value (27 exact rational, 3 real
  closed forms, n_s by indices and ζ-quotient, 27^φ by bounds, δ_CP as the
  integer 197), standard axioms only; renames `sin2_…_CKM` → `sin_…_CKM` and
  `chi_K7` → `two_b2` with deprecated aliases; removes 12214/69 from the
  aggregated certificate. `observables_certified` is not cited.

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
conditional extractions; the selection-principle thesis rewritten into the text
without citing the companion philosophy paper (under anonymous review).
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
  replaced by the preregistered look-elsewhere null (LEE-RETRAIT; on the
  refreshed data with two-sided windows, K₇ reaches 31/33, as do 1 085 of
  4 159 Betti alternatives and 1 015 of 2 000 invented vocabularies,
  P_global = 0.51; the first run, on the 3.5 dataset, had 32/33 reached by
  all Betti alternatives); 10⁻³⁴⁶ / 10⁻¹³³ out of the main text; the "14 derivations"
  argument reversed; SVD / random forest / 2.13× moved to S4 as descriptive.
- §8: formal verification reduced to one method paragraph.
- §10: the "why Lorentz invariance?" analogy and the "unique holonomy with
  the stabilizer chain" claim withdrawn (Spin(7) contains it).
- New §11: decision rule with no repair clause (D1–D6).
- §12: where the necessity of K₇ ends; list of withdrawn claims.
- Not yet: .tex regeneration, title, release audit (S1–S4 done).

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

## Erratum (2026-10-16, Scientific Reports referee, point 2)

- **p₂ is not a Pontryagin class.** The constant p₂ = dim(G₂)/dim(K₇) = 2 was
  labelled "Pontryagin class / Pontryagin ratio" (main §gauge "holonomy
  sequence", S2 θ₂₃ components and Fibonacci table). For a 7-manifold,
  p₂(TK₇) ∈ H⁸(K₇; ℤ) = 0, and 14/7 is neither a Pontryagin class nor a
  Pontryagin number. Relabelled "binary ratio" (the name S1/S2 already use
  elsewhere: "binary duality factor"); the unfounded "spin structure
  correction" reading of θ₂₃ is withdrawn. Values and formulas unchanged.

## v3.5 (2026-07, cold-read + external AI-review fixes, 2026-07-09)

**Content corrections (claude-chat review):**

- Ref [32] title corrected: NPB 471, 135 (1996) is Witten, "Strong coupling
  expansion of Calabi-Yau compactification" (heterotic M-theory), not "Bound
  states of strings and p-branes" (= NPB 460, 335). Same error class as the
  FHN/Bera catches.
- Conjunct ventilation reconciled against core v3.4.29 (commit 667c8b9) by
  direct count of the master-certificate refine tuples: Foundations 38->39,
  Predictions 55->56, Spectral 41->45. The headline **213 stands verified**
  (sum 39+56+45+15+10+6+10+11+14+7); the old ventilation summed to 207.
  Counting convention stated: top-level conjunctions.
- Build jobs 8378 -> **8394** (core README at v3.4.29); .lean file count
  134 (=128+6; 12 test) -> **146 under GIFT/ (140 core + 6 generated)**;
  the old ventilation matched no release.
- Figure 1 annotation: 3 generations now credited to Z_3 lattice action +
  (27,3) branching (S6.1), Wilson-line rank-2 SVD demoted to auxiliary data;
  broken parentheses in S8.1 anchors list fixed; [49] Tristram now cited
  numerically at the S3.1 conventions paragraph; essay URL moved to
  arithmon.substack.com; tau/e and mu/e deviations harmonized to 0.23%/0.98%;
  V_min vs S6.3 volumes normalization clarified; 65-catalogued vs 66-known
  clarified (65 + K_7); private master note citation made explicit.
- Parenthetical spaced double-hyphens purged from prose (they render as
  en-dashes in the PDF, same effect as the banned em-dash); paper_lint
  gains a DASH-PROSE check.

**Supplements pass (claude-chat review round 2, same day):**

- S1 LaTeX leak fixed: the build's SMP glyph substitution is now
  verbatim-aware (ASCII fallbacks inside verbatim; the derivation diagrams
  printed a literal "ensuremath" macro).
- Attribution corrected (FHN/Bera class): the (r,a,delta) classification of
  order-two non-symplectic involutions with fixed-locus shapes (g,k) is
  **Nikulin's** (new shared-bib entry [51], Izv. 43 (1979); AST survey
  arXiv:0903.3481 inline), not "Garbagnati-Sarti 2009". [45] stays for the
  symplectic side.
- `JoyceKarigiannisConstruction.lean` is NOT in core v3.4.29 (migrated to
  the authors' archive at a repo audit): all three citation sites now say
  so explicitly.
- S3 exact-match m_c/m_d row fixed (272.0 via the extended Type II chain,
  not 234.3/234.0); sector buckets reassigned to their declared thresholds;
  PMNS composition fixed (sin2theta13 0.81%, mean 0.29% now exact);
  Instanton split from Bundle (kappa_gauge) per main S5.5; quark sector
  mean 0.24%.
- S2 S22 deviation table recomputed over the full 33 Type I at the frozen
  dataset (git snapshot a34c5c05, mean 0.7319); S23 headline ratios aligned
  on the tables (~12x next-best gauge, ~6x vs SU(3)) in both S2 and main
  S8.4 (the "13x/13x" and "10x/5x" variants were stale); S24.2 distribution
  recounted (3/2/2/10/1, delta_CP reclassified DERIVED); duplicate section
  number 21 -> 20b.
- S3.8 Data Availability rewritten to verifiable claims only: DOI
  10.5281/zenodo.19893371 is the [B] spectral record (checked live) and
  does NOT hold the observable dataset; dataset now "available on request
  pending public deposit". Private working-supplement names (S6-S25, S9,
  Paper I, STATISTICAL_EVIDENCE.md path) purged from public text.
- Omega_DE 53/77 claim qualified against the declared PR4 freeze; S4.5
  reconciles 0.99% (post-audit sources) vs 0.73% (frozen); Spectral.lean
  coverage label Types III-IV; supplement page headers use ":" (no em-dash);
  Appendix C page counts fixed (S2 38, S3 15, S4 6); PDG source date fixed;
  shared-bibliography note added at the head of References.

**Layout (cold-read Brieuc):** abstract shortened ~40% (honest-scope
qualifiers preserved; "conditionally" reinstated per release-auditor),
abstract+keywords fit page 1, ToC added page 2, full-width rules, long
code tokens made breakable (main overfull sites cleared, S2 44->35).

## v3.5 (2026-07, rename: The K₇ Framework, 2026-07-08)

The framework is renamed **The K₇ Framework** (formerly the Geometric
Information Field Theory, GIFT). Motivation: the framework takes the name
of its central object, following the K3 precedent (Weil); "Geometric
Information Field Theory" collided with Ensslin's established Information
Field Theory; the GIFT brand had reached saturation. Versions 1.0-3.4 of
this record remain the same line of work; nothing is retracted.

- New title: *The K₇ Framework: Conditional Topological Relations for
  Standard-Model Parameters from G₂ Holonomy and E₈×E₈ Structure*.
- Continuity line added to the first-page status box and the §1.2
  definition site; footers now read "The K₇ Framework (formerly GIFT)".
- Observable-table columns "GIFT" / "GIFT prediction" → "Prediction";
  comparison-table labels (main §11, S3 Koide, S4 vs random algebraic)
  → "K₇ framework".
- **Unchanged (frozen identifiers)**: published titles of [B] and [C]
  ("G₂-GIFT Manifold/Metric"), the ledger symbol γ_GIFT (flagged
  "historical symbol name" at first occurrence), axiom class E
  "GIFT-claims" (synced with core v3.4.29), Lean identifiers
  `GIFT.Core.*`, pre-registration pointers (Sieve v1.0 `247e165`, core
  v3.4.29 `667c8b9`), repository URLs, and this changelog's history.
- Zenodo: v3.5 stacks as a new version on the existing concept DOI
  10.5281/zenodo.18837071 (GIFT 1.0-3.4 chain); "GIFT" kept in keywords
  for discoverability.

## v3.5 (2026-07, §4 catalogue deflation, 2026-07-07)

The deferred structural move from restructure pass 1, plus the length
concern raised by the round-1 reviews (DeepSeek: "45-50 pages"; GPT:
reader fatigue).

- Main §4 restructured from 12 subsections to 6: §4.1 Type I summary
  (representative table + Koide and Weinberg highlights + a dedicated
  **golden-ratio caveat** subsection for m_mu/m_e = 27^phi, per the
  review request that phi's weaker McKay-dependent status not borrow
  from the integer-ratio relations), §4.2 delta_CP (falsifiability
  flagship, kept whole), §4.3-4.5 Type II/III/IV, §4.6 summary stats.
- The eight per-sector relation tables (gauge, lepton, quark, neutrino
  mixing, Higgs, boson, CKM, cosmology) with their derivational prose
  moved to **S3 §3.4 "Per-Sector Relation Tables"**, ahead of the
  existing sector-performance narrative; conventions header points back
  to main §4.
- All cross-references renumbered (main §3.2, conventions note, §4.4/4.5
  internal, §11.4 table; S2 and S3 pointers to old §4.4.1 → §4.2).
- Main paper 1136 → 1040 lines; duplicate Type I summary table removed
  (was §4.8.1).

## v3.5 (2026-07, supplements sync, 2026-07-07)

The four supplements had not been touched since ~v3.4.13/14 (except S4,
new at 3.5); an audit pass reconciled them with the 3.5 main paper.

- **Axiom count** reconciled at all six stale sites (S1 x4, S2 x1, S3 x1):
  "4 axioms" → "15 classified axioms (A-F taxonomy), of which 4 external
  data packages", pointing to main §8.1. S1 §11.4's incorrect location
  claim (Foundation/Bounds) replaced by the four named data-package axioms.
- **NuFIT 6.1** propagated: S2 §13 table + drift paragraph, S2 Appendix F
  (new "NuFIT 6.1 update" note), S2 summary-table footnote, S3 sources +
  outliers + exact-matches note; NuFIT 6.0 kept where it is the *frozen
  dataset* of the deviation statistics, now labelled as such. Refs updated
  to the JHEP 12 (2024) 216 + 6.1 web-release pair.
- **Mechanical**: broken `|, |` cells repaired in S2 Appendix F table and
  S4 KS-test row; S4's 6 em-dashes removed; S4.3 survivor bullets repaired
  (the "Lean rebate" → "formal-identity flag" rename had mangled
  "rebate ≈ 0" semantics; now matches main §7 wording).
- **S2 "92-observable dataset" → 95** (stale count). Stale v3.4.13 tags
  dropped; Lean-module provenance tags (v3.4.14) retained.
- **S1 §11.3**: "det(g) = 65/32 prediction" → normalization target, per
  main §2.3.
- Stale main-numbering cross-refs in S2/S3 (Pinčák "[46]" → main [42]).
- Main-paper conventions note fixed: cosmology source is Planck PR4
  (Tristram et al. 2024), per S3 §3.2, not Planck 2018.
- DUNE "2028-2040" language in S2/S3 updated to first-beam-2031.

## v3.5 (2026-07, IA-review round 1 discharge, 2026-07-07)

Five independent AI reviews (GLM, Kimi, DeepSeek, GPT, Claude chat) of the
post-restructure draft; every mechanical claim verified against the file
and against primary sources before applying. Main paper only (supplements
in a following pass).

**Mechanical repairs:**
- Six table cells mutilated by the anti-em-dash script repaired to `n/a`
  (§5.5 G_35 row, §6.3 V_e row, §6.4 m_mu/m_e row, §11.3 two rows,
  §11.4 quantum-gravity row). Git archaeology confirmed all six were
  em-dash placeholders, no values lost.
- The 33 remaining em-dashes purged (colons/parens/commas), restoring the
  zero-em-dash rule.
- §2.3 metric-decomposition paragraph: four-sentence run-on parenthesis
  restructured.
- Dagger footnote in §4.12 anchored (11.3%†); Appendix C now lists S4.

**References (all verified against primary sources):**
- [26] T2K/NOvA joint analysis corrected to Nature 646, 818-824 (2025),
  doi:10.1038/s41586-025-09599-3 (was: invented volume/pages Nature 638).
- [27] now cites the NuFit-6.0 JHEP paper (JHEP 12 (2024) 216,
  arXiv:2410.05380) plus the NuFIT 6.1 web release, per the site's own
  citation instruction.
- [45] Garbagnati-Sarti corrected to J. Algebra 318 (2007), 323-350,
  arXiv:math/0603742 (was: 2008 + wrong arXiv ID); in-text
  "Garbagnati-Sarti 2009" fixed.
- [34] Atiyah-Witten no longer miscited for the LEP chargino bound; new
  [46] LEPSUSYWG/01-03.1 (103.5 GeV) carries it.
- New [47] Fermilab DUNE first-beam-2031 milestone news (2026-05-07).
- [13] (orphaned duplicate of [16] CGN) recycled as Kovalev 2005
  coassociative K3 fibrations (arXiv:math/0511150), now cited as the L4
  closest template in §9.1.
- Chen-Hong entry dropped (never cited, no natural home). All remaining
  orphans wired where cited by name (octonionic SM literature §2.1,
  construction catalogue §2.3, Harvey-Lawson §6.3, heterotic M-theory
  §11.2, Mukai §2.3, DUNE TDR §3.3, T2K/NOvA §4.4.1, Springer AI policy
  in the author's note). Bibliography now 1-47, zero orphans, zero
  dangling numbers.
- Stale "[30, 45]" on the §5 intro (K3-fiber 0.07% certification)
  corrected to [C].

**Consistency fixes:**
- §11.4 "Singularity structure: Not required" row replaced: it contradicted
  the UV-bridge caveat added in the GPT review pass. Now reads "Not yet
  supplied ... requires an explicit UV bridge; load-bearing open question."
- "CLOSED program" language harmonized with the §10 rename at all three
  remaining sites (§1.3, §3.4, §11.4 x2): audit closed, selection question
  open.
- §11.4 delta_CP row updated to NuFIT 6.1 (4.8%, inside 1-sigma), stale
  §9.1 pointer fixed; §3.5 stale "§9.4" pointer fixed to §10.
- DUNE timeline table: "2028-2030" replaced by "after first beam (targeted
  2031); exposure-dependent".
- M_GUT 2e16 (§5.1) vs 2.7e16 (§5.4) harmonized with an explicit note.
- Version-history self-references ("The 3.5 update...") softened in body
  text (§3.2, §7, §9, §10, §11.4); the delta lives in this CHANGELOG.

**Substantive additions (review decisions):**
- §6 opens with a "Status: conditional calibration (Type III)" disclosure:
  c = 0.452, optimized positions, and cycle assignment are declared
  mechanism/calibration choices; results are conditional reconstructions,
  not independent predictions. §4.10 points to it.
- §7 statistical claim layered explicitly (33 conditional ledger identities
  vs sieve-distinguished survivors m_H/m_W + Koide) + a pre-registration
  traceability paragraph with frozen artifacts: Sieve v1.0 (commit 247e165,
  2026-06-12, Zenodo 10.5281/zenodo.20666879) and Lean core v3.4.29
  (commit 667c8b9).
- §4 opens with a measurement-conventions paragraph (scheme / scale /
  dataset / freeze-date defaults; NuFIT 6.0 frozen for tables, 6.1 tracked
  in §4.4.1 prose).
- §10.2 adds the operational status of (21,77): a construction-level input,
  discrete and pre-registered, not chosen from a continuum; the Sieve tests
  the relations given the input.
- Author's note updated: GPT/Codex (OpenAI) credited for audit passes,
  certificate engineering, and adversarial reviews; Kimi, DeepSeek, GLM
  added for review rounds; publisher-AI-policy citation [38] wired.

## v3.5 (2026-07, restructure, GPT review pass 2026-07-06)

**GPT review pass (2026-07-06).** Fifteen targeted corrections after a
first restructure pass. The paper is now defensible on the specific
correctness gates GPT flagged:

- Koide formula corrected (numerator not squared).
- Wilson-line rank statement corrected (numerical rank 2, not 3; the
  three-generation count comes from the Z₃ lattice action + (27, 3)
  branching, not from a rank-3 SVD).
- Coquille $137.033 = 4\pi/\alpha_{\rm em}$ fixed to $\alpha_{\rm em}^{-1} = 137.033$.
- $b_1 = 0$ vs $\pi_1(K_7) = 1$ fixed: $b_1$ constrains only the
  abelianisation; simple connectivity is postulated as a construction
  input (established in [E, Suppl. App. C] via Van Kampen). Metric
  corrections are not "responsible for $b_1 = 0$" (Betti topological).
- E₈ breaking chain rewritten as a representation-branching chain
  (subgroup branchings compatible with SM reps) rather than a physical
  breaking mechanism; the intermediate $SU(3)$ factor is now explicitly
  hidden-sector; SU(5) × U(1) is *not* Pati–Salam (which is
  $SU(4) \times SU(2)_L \times SU(2)_R$): mislabel fixed.
- "Exact U(1)² symmetry to $2 \times 10^{-5}$" replaced by "numerically
  compatible with U(1)² to tolerance". "Exact" and finite tolerance
  cannot coexist.
- **UV bridge caveat added** (§2.3, §5.1, §9, §11.5): the smooth
  NK-certified metric does not by itself produce non-abelian chiral
  gauge physics in the standard M-theory dictionary (Acharya–Witten
  [hep-th/0109152]); a heterotic-bundle / duality / singular-$G_2$-locus
  bridge is a load-bearing open question, on par with $\mathsf H_{\rm global}$
  and $(\mathrm J)$.
- "Zero free parameters" tightened: 33 Type I relations use no
  continuously tuned parameter after ledger freeze; Types II/III/IV
  are conditional extractions (experimental anchors / dynamical
  assumptions / diagnostics), *not* independent new predictions.
- **"Lean rebate" → "formal-identity flag"** everywhere (main paper,
  Supplement 4, CHANGELOG). The flag certifies the conditional
  identity Lean has been given; it does not raise the physical prior.
- §10 renamed from "Selection principle: CLOSED program" to
  **"Selection audit: five investigated routes and one open residual"**.
  The audit is closed; the selection question is not.
- **NuFIT 6.1 update.** $\delta_{\rm CP} = 207^{+23}_{-20}$° (NO w/o
  SK-atm), so the prediction 197° now sits inside the 1σ band
  (deviation 4.8% from central); replaces the NuFIT 6.0 framing.
- **DUNE calendar update.** First beam targeted by 2031 per Fermilab's
  2026-05 milestone communication; the "2028–2040" window is dropped.
- **Title updated** to "Geometric Information Field Theory: Conditional
  Topological Relations for Standard-Model Parameters from a G₂ / E₈
  Framework".
- **Four-line status box on first page** ("Formally established /
  Established at the datum / Open / Phenomenology"), replacing the
  "at a glance" 5-row table.
- §9 datum-conditional language propagated to Abstract, §2.3, §8.5,
  §11.5 (existing NK "existence and uniqueness" phrasing everywhere
  qualified with "seam / datum level, not global compact").

## v3.5 (2026-07, restructure)

This is a restructure of the 3.4 framework paper (published 2026-05-07 on
Zenodo, DOI [10.5281/zenodo.18837071](https://doi.org/10.5281/zenodo.18837071),
44 pp). The scientific content is stable; the delta is (i) a companion
paper cited upfront, (ii) a methodology swap, (iii) a section re-layout,
(iv) a series of language tightenings and reconciliations.

### Companion paper cited upfront ([E])

Introduces a load-bearing external reference:

> **[E]** B. de La Fournière, "A conditional analytic framework for
> rank-one branched Kovalev–Lefschetz adiabatic limits," Zenodo concept
> DOI [10.5281/zenodo.21209413](https://doi.org/10.5281/zenodo.21209413)
> (2026), main paper 68 pp + supplement 25 pp, dataset and four
> `mpmath.iv` verification scripts (CC BY 4.0).

[E] discharges the analytic side of the existence question at a
normalised datum $\mathcal D_0$ (a $K_7 \to S^3$ construction with
$N = 77$ round-unlink branch components):

- structural: seven theorem-grade results assembled into a conditional
  branched lifting scheme in the sense of a special case of
  [Donaldson 2017, Conjecture 1];
- quantitative: source-side discharge constants certified with
  structural provenance ($C_{\rm src} = 27/16$, $C_{\rm nl} = 2/3$,
  $C_{\rm link} \le 1$, $\gamma = 2$); tail-contraction threshold
  $R_0(\mathcal D_0) \le 4.9 \cdot 10^3$ enclosed by outward-rounded
  interval arithmetic;
- residual: two structural hypotheses (an anisotropic three-scale
  perturbation theorem, and a hyperkähler-with-periods geometric upgrade)
  remain OPEN and are cited as such.

Everywhere the 3.4 paper wrote "full smooth compact construction remains
open" or "NK ball only," the 3.5 paper writes "the datum-level
analytic scheme is discharged conditionally on the two external slots of
[E]" and cites the concept DOI. Load-bearing locations updated:
Abstract, §2.3 K₇ Manifold, §5.5 Bundle universality, §8.5 G₂ metric,
§9.3 comparison table, §9.4 open questions.

### Methodology swap: statistical stress test → Sieve reading

The 3.4 sensitivity headline was a coincidence-probability calculation
under a uniform and an algebraic null model, giving $\sim 10^{-346}$ /
$\sim 10^{-133}$. These exponents are retained here only as an appendix
diagnostic; the headline is replaced by the **Sieve reading** consistent
with the Arithmon methodology paper (Zenodo DOI 10.5281/zenodo.20666879):

- public 4-null battery (uniform / algebraic / factorised / permuted);
- certified survivors with per-survivor budget-uniqueness rank;
- Lean 4 formal-identity flag for survivors that carry a Lean R2 pre-registered
  identity (so that the sieve-passage becomes a certified statement
  rather than a coincidence-probability tail).

Under the Sieve reading, the m_H/m_W route (Route A) is the unique
survivor at exact rank 1 budget-unique after Type I calibration;
Koide's Q remains a survivor but with formal-identity flag ≈ 0 (§7 revised).

### Section re-layout

- **New §9 "Existence status"**: absorbs the six 3.4 loci that
  independently wrote "remains open" language; centralises the [E]
  citation and states the two remaining external slots explicitly.
- **New §10 "Selection principle"**: extracted from the 3.4 §9.4 mixed
  "limitations and open questions" block. States the CLOSED selection
  program (convenient-not-special under KS-full ; distinguishedness
  across multiple higher-HK classifications with a single exception at
  Camere Lemma 5.8 ; sub-Q1/Q2 mechanisms of 77 invisibility ; sub-Q3
  distinguishedness-yes-77-no) and preserves the honest residual
  $b_2 + b_3 = 98 = \dim K_7 \cdot \dim G_2$ (pre-registration flagged
  as required for that identity to graduate from numerology).
- **§4 deflation**: the previous §4 "Observables: 95 Relations"
  (228 lines) is compressed to a "Results at a glance" table; the
  sector-by-sector detail moves to Supplement 3 (Observables).
- **§7 + §8.4 fusion**: statistical uniqueness content is unified
  under the Sieve reading in a single section; the 3.4 §7.5
  coincidence tables move to a new **Supplement 4 (Sieve diagnostics)**.

### Reconciliations and language

- **Axiom count clarified.** The 3.4 paper wrote "4 axioms" for the
  Lean layer (referring to the four data packages
  `K7_analysis_data`, `K7_spectral_data`, `literature_package`,
  `KK_YM_EFT`). The Lean core headline released as v3.4.29
  (2026-06-24, `#print axioms` count over the ledger) is **15
  classified axioms** (A-F taxonomy: A definitional, B standard,
  C geometric, D literature, E GIFT-claims, F numerical). 3.5 states
  both counts explicitly: "4 external data-package axioms; 15 total
  ledger axioms across the A-F classification."
- **Selection principle language** ("full formula-selection rule
  remains open") replaced by pointers to §10 and to the master note
  `axis2_selection_principle_master_2026_07_04` (private).
- **Arithmon hat.** Footer "GIFT is the founding framework of the
  Arithmon program"; three contact entries maximum
  (`brieuc@arithmon.com`, `contact@arithmon.com`, arithmon.com).
- **Related work.** Adds bridge note on Zhou (rank-1 K3-fibration
  series ; retrograded 2026-05) ; Cabannas-Silva short entry ;
  no change to Flyxion pointer.
- **Observables reconciliation.** 0.99% Type I after the audit
  documented in `frozen_inputs_divergence_audit_2026_06_16` ;
  m_c/m_s erratum inlined.

### Referee-pass items (from 3.4 → 3.5)

- $\det(g) = 65/32$ is a **normalisation target** (scale module of a
  Ricci-flat metric), **not** a prediction ; the dimensionless
  spectrum is invariant under the $65/32 \to 2$ rescaling ;
- $\kappa_T^{-1} = 61$ is a **topological anchor**
  $b_3 - \dim(G_2) - p_2$ (not a torsion mass) ; the closure
  $Y_p + \Omega_m/\Omega_\Lambda$ fixes 61 independently of
  $m_\tau/m_e$, defusing the circularity concern.

### Files updated

- `physics_main.md`: restructured.
- `supplement_derivations.md`: unchanged (referenced from §4 table).
- `supplement_foundations.md`: unchanged.
- `supplement_observables.md`: absorbs the 3.4 §4 sector-by-sector detail.
- `supplement_sieve_diagnostics.md` (**new**): 3.4 §7.5 coincidence
  tables + Sieve reading formal-identity flag details.
- `latex/gift_3.5_main.tex` (**new**): hand-maintained LaTeX build.
  `gift_3.4_main.tex` preserved as archive.

## v3.4 (2026-05-07)

Published on Zenodo, DOI 10.5281/zenodo.18837071. 44 pp.
95 observables; four types (I direct-algebraic, II one-step-physical,
III multi-step-dynamical, IV structural-diagnostic). Lean 4 layer
with 213 conjuncts, 4 axioms, 0 sorry. DUNE δ_CP = 197° prediction.
No prior CHANGELOG.
