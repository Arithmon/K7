# Supplement S2: The 33 Relations: Arithmetic, Dictionary Choices and Status

## S2.0 What this supplement establishes

Earlier versions of this supplement were titled "Complete Derivations" and presented each relation as a theorem with a proof. Version 3.6 withdraws that framing. No geometric map is known that sends the invariants of (K₇, E₈×E₈) to the Standard-Model parameters, and no rule assigns a formula to an observable (main §3.2). What can be established for each relation is narrower, and this supplement establishes it:

1. **The arithmetic.** Given the declared constants, the closed form evaluates to the stated number. The arithmetic below is exact. Each relation has a Lean statement tying its closed form to its value (`relations_v36_certified`, Arithmon/K7-Lean); the form of each statement (exact rational equality, real closed form, bounds, integer) is given in S3.7.
2. **The dictionary choices.** Which constants the formula uses, which operations beyond integer ratios, and which entries of the residue register it depends on (main §3.3: R1–R12).
3. **The status.** The status of each relation against the most recent data (main §4.1, generated from the dataset) is shown in the last column of each table, with its pull. The column is generated from main §4.1 (`k7_v3_6_s2_status.py`) and is never edited here, so that the status keeps one source; the status vocabulary is defined in main §4.1.

What a relation's arithmetic does not establish: that the formula is the right one for the observable, that the structure requires it, or that the agreement with measurement is evidence for the framework (main §7). Section S2.7 records the alternative formulas found in the corpus for the same observables; their number is a measure of the vocabulary's freedom, not of robustness.

---

## S2.1 Notation

The twenty structural constants and their status (Lie datum, topological, input, combination) are listed in main §3.1. The relations also use the following, each a combination chosen by the framework:

| Symbol | Value | Definition | Register |
|--------|-------|-----------|----------|
| det(g) | 65/32 | p₂ + 1/(b₂ + dim G₂ − N_gen) = det_num/det_den (main App. B) | **imposed** normalization (R2); a second expression, Weyl · α_sum/2^Weyl, agrees with it on the line b₂ = 21 and differs elsewhere |
| κ_T⁻¹ | 61 | b₃ − dim(G₂) − p₂ | integer combination without a physical name (R3); a second expression, b₃ − b₂ + Weyl, agrees with it on the line b₂ = 21 and differs elsewhere |
| φ | (1 + √5)/2 | through the McKay correspondence E₈ ↔ 2I | additional step (R9) |
| 1 | 1 | written b₀ in earlier versions | used freely as an additive constant |
| 2b₂ | 42 | also p₂ × N_gen × dim(K₇) | combination |
| τ | 3472/891 | dim(E₈×E₈) · b₂/(dim J₃(𝕆) · H*) | used only in Type II entries (S3) |

**Weyl = 5.** Three expressions give 5: (dim G₂ + 1)/N_gen, b₂/N_gen − p₂, dim G₂ − rank E₈ − 1. Earlier versions called this a "triple identity". It is an arithmetic coincidence among the declared integers; it fixes no further quantity.

**N_gen = 3.** The integer identity (rank E₈ + N_gen) · b₂ = N_gen · b₃, i.e. 11 · 21 = 3 · 77, is satisfied by N_gen = 3. It is a consistency check on (21, 77), not the output of an index theorem: the "Atiyah–Singer" expression of earlier versions, (77 − 8/3 · 21)/7 = 3, is the same arithmetic written as an index without an operator whose index it is (main §2.4).

---

## S2.2 Gauge sector and Higgs

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A01 | sin²θ_W (M_Z, MS-bar) | b₂/(b₃ + dim G₂) = 21/91 = **3/13** = 0.230769 | scale and scheme (R7) | integer; **proximity**; pull −7.5σ |
| A02 | α_s(M_Z) | √2/(dim G₂ − p₂) = **√2/12** = 0.117851 | operation √; scale (R7) | algebraic; pull −0.2σ |
| A03 | λ_H | √(dim G₂ + N_gen)/det_den = **√17/32** = 0.128847 | operation √; det(g) (R2); compared with the tree-level m_H²/(2v²) | algebraic; det(g); pull −1.3σ |
| A04 | α⁻¹(0) | (dim E₈ + rank E₈)/2 + H*/D_bulk + det(g) · κ_T = 128 + 9 + 65/1952 = **267489/1952** = 137.03330 | det(g) (R2); κ_T (R3); scale q² = 0 (R7) | det(g), κ_T; **proximity**; pull ≫ 10σ |

**On A04.** The three terms were written as "algebraic", "bulk impedance" and "torsional correction" in earlier versions. None of the three names corresponds to a computation; the correction term is the product of the imposed normalization and the unnamed combination. The relation lies 19.7 ppm below α⁻¹(0), whose uncertainty is 1.5 × 10⁻¹⁰ relative: a proximity (main §4.2).

**On A03.** A second formula for λ_H is recorded in the corpus (S2.7).

---

## S2.3 Leptons (overdetermined: R8)

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A05 | Q_Koide | dim G₂/b₂ = 14/21 = **2/3** | R8 | integer; approximate (R8); pull +0.4σ |
| A06 | m_τ/m_e | dim K₇ + 10 · dim E₈ + 10 · H* = 7 + 2480 + 990 = **3477** | R8; the coefficient 10 is not among the twenty constants | integer; approximate (R8); **tension**; pull −2.1σ |
| A07 | m_μ/m_e | dim(J₃(𝕆))^φ = **27^φ** = 207.0119 | R8; φ (R9) | φ; approximate (R8); **proximity**; pull ≫ 10σ |
| A22 | m_μ/m_τ | (b₂ − D_bulk)/\|PSL(2,7)\| = 10/168 = **5/84** = 0.059524 | R8 | integer; approximate (R8); **proximity**; pull +20.8σ |

Four relations bear on two independent mass ratios, and they are mutually incompatible: with 27^φ and 3477, the Koide parameter is 0.666546, not 2/3. None is selected (main §6.1). Earlier versions added that 3477 = 3 × 19 × 61 "factorizes into framework constants"; 19 is not a framework constant, and a factorization is not a derivation. They also cited a "period-integral cross-confirmation" of 3477 from associative 3-cycle volumes, ln(m_τ/m_e) = 8.154; that number is the logarithm of the measured ratio, used as the target of the volume assignment (S3, entries C17–C19), so the agreement is the target returning, not an independent confirmation. Both statements are withdrawn.

---

## S2.4 Quarks, CKM and boson masses

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A08 | m_s/m_d | p₂² × Weyl = 4 × 5 = **20** | the PDG gives a range (17–22), not a measurement | integer; inside the PDG range |
| A09 | m_c/m_s | (dim E₈ − p₂)/b₂ = 246/21 = **82/7** = 11.7143 | n/a | integer; pull −1.6σ |
| A10 | m_b/m_t | 1/(2b₂) = **1/42** = 0.023810 | **mass scheme** (R7): m_b in MS-bar at m_b over the directly measured m_t | integer; **proximity** (in the scheme declared in R7); pull −10.2σ |
| A11 | m_u/m_d | (1 + dim E₆)/\|PSL(2,7)\| = **79/168** = 0.470238 | additive 1; the PDG quotes the uncertainty at 90% CL, divided by 1.645 to 1σ (S3) | integer; pull +0.7σ |
| A16 | sin θ₁₂ (CKM) = λ | fund(E₇)/dim E₈ = 56/248 = **7/31** = 0.225806 | compared with sin θ₁₂, not sin²θ₁₂; R12 | integer; approximate (R12); pull +0.9σ |
| A17 | A (Wolfenstein) | (Weyl + dim E₆)/H* = **83/99** = 0.838384 | R12 | integer; approximate (R12); pull +0.7σ |
| A18 | sin θ₂₃ (CKM) = Aλ² | dim K₇/\|PSL(2,7)\| = 7/168 = **1/24** = 0.041667 | compared with sin θ₂₃, not sin²θ₂₃; R12 | integer; approximate (R12); pull −0.3σ |
| A19 | m_H/m_t | fund(E₇)/b₃ = 56/77 = **8/11** = 0.727273 | m_t from direct measurements | integer; pull +1.8σ |
| A20 | m_H/m_W | (N_gen + dim E₆)/dim F₄ = **81/52** = 1.557692 | n/a | integer; pull +0.5σ |
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = **37/42** = 0.880952 | n/a | integer; **tension**; pull −2.7σ |

**The CKM sector is overdetermined (R12).** The three relations bear on two Wolfenstein parameters, since sin θ₂₃ = Aλ². With λ = 7/31 and A = 83/99, Aλ² = 4067/95139 = 0.042748, while A18 gives 1/24 = 0.041667: the three relations are 2.6% apart as exact equalities, and at most two can hold. None is selected (main §4.2).

**Labels corrected.** Earlier versions labelled A16 and A18 "sin²θ₁₂(CKM)" and "sin²θ₂₃(CKM)" while comparing them with λ = sin θ₁₂ and Aλ² = sin θ₂₃. The values are sines; the labels are corrected (S3.3).

**On the constant 42.** Earlier versions presented the appearance of 42 = 2b₂ in both m_b/m_t = 1/42 and Ω_DM/Ω_b = (1 + 42)/8 as "connecting quark physics to large-scale structure". Two formulas that share an integer share a choice of vocabulary; no connection between the quantities is implied, and the sentence is withdrawn.

**Dependence noted, not counted.** sin²θ_W in MS-bar (A01) and m_W/m_Z (A21) are related in the Standard Model through radiative corrections; the two relations are not independent tests in the strict sense.

---

## S2.5 Neutrino mixing

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A12 | sin²θ₁₂ (PMNS) | (1 + N_gen)/α_sum = **4/13** = 0.307692 | additive 1 | integer; pull −0.2σ |
| A13 | sin²θ₂₃ (PMNS) | (D_bulk − Weyl)/D_bulk = **6/11** = 0.545455 | octant (main §4.3) | integer; **tension** (octant; inside the NuFIT 3σ range, §4.3); pull +4.4σ, not Gaussian (main §4.3) |
| A14 | sin²θ₁₃ (PMNS) | D_bulk/dim(E₈×E₈) = **11/496** = 0.022177 | n/a | integer; pull −0.5σ |
| A15 | δ_CP | dim K₇ · dim G₂ + H* = 98 + 99 = **197**, read as the phase 2π · 197/360 | **unit** (R6) | **unit assignment** (R6); pull −0.4σ |

**The δ_CP rule.** The prediction is the phase 2π · 197/360, a point value; the unit is a dictionary assignment (R6), and rule D1 of main §11 applies: a measurement whose 3σ interval excludes 197° rejects the relation and the unit assignment together, with no repair clause and no theoretical tolerance added afterwards. The compactification factor 62/69 of earlier versions is addressed in S2.8.

---

## S2.6 Cosmology (overdetermined: R11)

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A23 | Ω_DE = Ω_Λ | ln 2 · (b₂ + b₃)/H* = ln 2 · 98/99 = **0.686146** | operation ln 2; R11 | ln 2; approximate (R11); pull +0.2σ |
| A24 | n_s | ζ(D_bulk)/ζ(Weyl) = **ζ(11)/ζ(5)** = 0.964864 | operation ζ | ζ values; pull 0.0σ |
| A25 | Ω_DM/Ω_b | (1 + 2b₂)/rank E₈ = **43/8** = 5.375 | additive 1; R11 | integer; approximate (R11); pull +0.2σ |
| A26 | Ω_c/Ω_Λ | det_num/\|PSL(2,7)\| = **65/168** = 0.386905 | R2; R11 | integer; det(g); approximate (R11); pull +0.1σ |
| A27 | Ω_Λ/Ω_m | (dim G₂ + H*)/dim F₄ = **113/52** = 2.173077 | R11 | integer; approximate (R11); pull 0.0σ |
| A28 | h | (\|PSL(2,7)\| − 1)/dim E₈ = **167/248** = 0.673387 | additive 1 | integer; pull 0.0σ |
| A29 | Ω_b/Ω_m | Weyl/det_den = **5/32** = 0.15625 | R2; R11 | integer; det(g); approximate (R11); pull −0.1σ |
| A30 | Ω_c/Ω_m | (det_den − Weyl)/det_den = **27/32** = 0.84375 | R2; R11 | integer; det(g); approximate (R11); pull +0.4σ |
| A31 | σ₈ | (p₂ + det_den)/(2b₂) = 34/42 = **17/21** = 0.809524 | R2 | integer; det(g); pull −0.3σ |
| A32 | Y_p | (1 + dim G₂)/κ_T⁻¹ = **15/61** = 0.245902 | additive 1; R3 | integer; κ_T; pull +0.3σ |
| A33 | Ω_m/Ω_Λ | (1 + dim J₃(𝕆))/κ_T⁻¹ = **28/61** = 0.459016 | additive 1; R3; R11 | integer; κ_T; approximate (R11); pull −0.1σ |

**The seven density relations bear on two independent densities** (flat ΛCDM: Ω_b + Ω_c + Ω_Λ = 1) and are mutually incompatible as exact equalities (main §4.2):

| Quantity | Values implied by the relations |
|----------|--------------------------------|
| Ω_Λ/Ω_m | 113/52 = 2.1731 (A27); 61/28 = 2.1786 (inverse of A33); 2.1862 (A23 with flatness) |
| Ω_c/Ω_b | 43/8 = 5.375 (A25); 27/5 = 5.400 (A30/A29) |
| Ω_c/Ω_Λ | 65/168 = 0.3869 (A26); 0.3873 (A30 × A33); 0.3883 (A30/A27) |

A27 and A33 are the same quantity, written with two formulas. The disagreements are below the Planck uncertainties, which is why each relation passes at 2σ. The seven cannot hold together; none is selected (R11). Some are redundant and some subsets are compatible: A29 and A30 are equivalent under flatness without neutrinos (5/32 + 27/32 = 1), and the largest compatible subsets have three relations, A29 and A30 with one of A23, A26, A27 or A33 (checked by solving each subset for (Ω_b, Ω_c)). Earlier drafts of this version said that at most two of the seven can be exact; A23, A29 and A30 hold together, and the statement is withdrawn.

**Withdrawn.** Earlier versions also gave Ω_m = Ω_DE/√Weyl = 0.3068 (2.7% from Planck) as a "derived" relation, and described ln 2 as a "binary information factor" of the moduli space. The first is an eighth density relation, incompatible with the others; the second names an operation without a computation behind it. Both are withdrawn. The statement that Ω_DM/Ω_b = 43/8 is "exact" (from a dataset value 5.375 ± 0.1 that matched no Planck column) is withdrawn; against Planck 2018 it is 5.364 ± 0.065.

---

## S2.7 Vocabulary freedom: alternative formulas in the corpus

Earlier versions counted, for each relation, the number of distinct expressions in the constants that reduce to the same value (for example 14 for sin²θ_W = 3/13, 20 for Q_Koide = 2/3, 21 for m_b/m_t = 1/42), and read a large count as "structural robustness": a value reached by many paths was said to be less likely a coincidence. Version 3.6 reverses that reading (main §7). A value reached by many paths through twenty constants is a value the vocabulary reaches easily; the count measures the vocabulary's freedom (R4, R5), and the look-elsewhere test of main §7 prices it: there, every one of the 6 159 competing vocabularies reaches sin²θ_W, Q_Koide and m_b/m_t within 2σ at five nodes (S4.2.2). The counts are kept as such a measure:

| Relation | Distinct expressions recorded | Examples |
|----------|-------------------------------|----------|
| sin²θ_W = 3/13 | 14 | N_gen/α_sum; b₂/(b₃ + dim G₂); dim J₃(𝕆)/(dim F₄ + det_num); (1 + dim G₂)/det_num |
| Q_Koide = 2/3 | 20 | p₂/N_gen; dim G₂/b₂; dim F₄/dim E₆; rank E₈/(Weyl + dim K₇) |
| m_b/m_t = 1/42 | 21 | 1/(2b₂); (1 + N_gen)/\|PSL(2,7)\|; p₂/(dim K₇ + b₃); N_gen/(dim J₃(𝕆) + H*) |
| sin²θ₁₂ (PMNS) = 4/13 | 28 | n/a |
| m_H/m_t = 8/11 | 19 | n/a |
| m_u/m_d = 79/168, m_H/m_W = 81/52 | 1 each | n/a |

**Second formulas for the same observable.** The corpus also contains formulas that give a *different* value for the same observable, chosen at different times:

| Observable | Dataset formula | Other formula in the corpus |
|------------|-----------------|-----------------------------|
| λ_H | √17/32 = 0.12885 | b₂(M₁)/(b₃ + b₂(M₂)) = 11/87 = 0.12644 (TCS building blocks) |
| Ω_DE | ln 2 · 98/99 = 0.68615 | 1 − χ(K3)/b₃ = 53/77 = 0.68831 |
| m_c/m_s | 246/21 = 11.714 | b₂(M₁) + dim K₇/b₂(M₂) = 117/10 = 11.700 |
| Ω_Λ/Ω_m | 113/52 = 2.1731 | (det_den − dim K₇)/D_bulk = 25/11 = 2.2727; 61/28 (A33 inverted) |
| θ₁₃ | sin²θ₁₃ = 11/496 | θ₁₃ = π/b₂ = 8.571°; θ₁₃ = 94/11 = 8.545° read in degrees |
| θ₂₃ | sin²θ₂₃ = 6/11 (θ = 47.6°) | θ₂₃ = arcsin(75/99) = 49.25° (sin²θ₂₃ = 0.574) |
| θ₁₂ | sin²θ₁₂ = 4/13 | θ₁₂ = arctan √((2π/25)/(511/884)) = 33.40° |
| δ_CP | 197 | 197 × 62/69 = 177.01 (S2.8) |

The "TCS building-block" formulas use b₂(M₁) = 11 and b₂(M₂) = 10, Betti numbers of building blocks whose identification is open (main §9). Several alternatives were introduced after a release of the data had moved: the Ω_DE alternative was preferred against one Planck release and not the other, and the θ₁₃ alternative "in degrees" is a second unit assignment of the kind R6 registers. None of these is part of the 33; they are listed because they show, on the framework's own record, how many formulas the vocabulary offers for one observable and how the choice among them was made.

**Patterns.** The Fibonacci and Lucas numbers among the constants (2, 3, 5, 8, 13, 21; 7, 11, 47) and the identities among the integers (dim G₂ = p₂ · dim K₇, b₂ = N_gen · dim K₇, \|PSL(2,7)\| = rank E₈ · b₂, b₃ + dim G₂ = dim K₇ · α_sum) are arithmetic facts about the chosen integers. Earlier versions called them an "algebraic web" and a "Fibonacci–Lucas embedding" reflecting icosahedral geometry. Small integers satisfy many such identities; no physical consequence follows from these, and they are not evidence.

---

## S2.8 Withdrawn readings

| Earlier statement | Why it is withdrawn |
|-------------------|--------------------|
| "Complete derivations", "proof", "VERIFIED", "TOPOLOGICAL" as statuses of the relations | the arithmetic is exact; the assignment is not derived (S2.0) |
| N_gen = 3 by the Atiyah–Singer index theorem | no operator is specified; the expression is the integer identity of S2.1 |
| "All 33 predictions use only topological invariants; no fitting" | eight use the imposed normalization or κ_T (R2, R3); the formulas were chosen with the values known (R4) |
| Mean deviation 0.73%, "11 exact matches", deviation histograms | computed against an earlier dataset; a mean deviation measures closeness, which is not distinctive (main §4.2, §7) |
| Statistical uniqueness: 192 349 alternatives, none better, P < 5 × 10⁻⁶, gauge-group and holonomy rankings | the alternatives were scored with the framework's own formulas, not allowed to search; replaced by the preregistered null of main §7 and S4 |
| "Literature uniqueness" of (21, 77) | absence from a catalogue is not selection; the selection audit is main §10 |
| Results "from analysis of the NK-certified metric": V_min formula, U(1)² symmetry, origin of the SM gauge group from triality | properties of an approximate seam metric (main §9); not used by any relation, and the gauge-group statement is not a derivation (main §2) |
| κ_T = 1/61 as a "topological torsion capacity"; 61 = dim F₄ + N_gen² | an integer combination without a physical name (R3); a second expression for 61 is another instance of S2.7 |
| det(g) = 65/32 "consistent with the topological formula" via three algebraic paths | imposed normalization (R2); the metric optimization was constrained to this target |
| 3477 "factorizes into framework constants"; associative-volume "cross-confirmation" | S2.3 |
| Ω_m = Ω_DE/√5, Ω_DM/Ω_b "exact", ln 2 as an information factor | S2.6 |

**Appendix F of earlier versions: the compactification factor 62/69.** A residual search after the NuFIT 6.0 release found 197 × 62/69 = 177.01, matching that release's central value, and earlier versions kept it as a "contingency plan": if DUNE measured δ_CP near 177°, the framework would adopt 177.01 as its prediction and read 197 as a "bare" value. That plan is a repair clause, and version 3.6 has none (main §11, rule D1). It is withdrawn without condition: if a measurement excludes 197° at 3σ, the relation δ_CP = 197 and its unit assignment are rejected, and no factor found afterwards replaces them. The factor 62/69 = 248/276 is recorded in S2.7 as one more formula the vocabulary offers.

---

## References

1. Particle Data Group, F. Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026).
2. I. Esteban et al., "NuFit-6.0: updated global analysis of three-flavor neutrino oscillations," JHEP 12 (2024) 216, arXiv:2410.05380; NuFIT 6.1: three-neutrino fit based on data available in November 2025, www.nu-fit.org.
3. Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," A&A 641, A6 (2020).
4. Y. Koide, Lett. Nuovo Cim. 34, 201 (1982).

---

## Author's Related Works

- **[A]** B. de La Fournière, "An Explicit Approximate G₂ Metric on a Compact 7-Manifold with Certified Torsion-Free Completion," Zenodo [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069) (2026).
- **[B]** B. de La Fournière, "Spectral Geometry of the G₂-GIFT Manifold: Betti Numbers, KK Spectrum, and Spectral Invariants," Zenodo [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) (2026).

---

*The K₇ Framework (formerly GIFT): Supplement S2*
*The 33 relations: arithmetic, dictionary choices and status*
