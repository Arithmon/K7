# Supplement S2: The 33 Relations: Arithmetic, Dictionary Choices and Status

## S2.0 What this supplement establishes

No geometric map is known that sends the invariants of (K₇, E₈×E₈) to the Standard-Model parameters, and no rule assigns a formula to an observable (main §3.2). For each of the 33 relations (Type I in the dataset, S3), this supplement establishes three things:

1. **The arithmetic.** Given the declared constants, the closed form evaluates to the stated number. The arithmetic below is exact. Each relation has a Lean statement tying its closed form to its value (`relations_v36_certified`, Arithmon/K7-Lean); the form of each statement (exact rational equality, real closed form, bounds, integer) is given in S3.7.
2. **The dictionary choices.** Which constants the formula uses, which operations beyond integer ratios, and which items of the residue register it depends on (main §3.3, where the items R1 to R12 list what is set rather than derived).
3. **The status.** The status of each relation against the most recent data (main §4.1, generated from the dataset) is shown in the last column of each table, with its pull. The column is generated from the table of main §4.1 and is not edited here, so that the status has one source; the status vocabulary is defined in main §4.1.

The arithmetic of a relation says nothing about whether the formula is the right one for the observable (main §3.2, §7). Section S2.7 records the alternative formulas found in the project's record for the same observables; their number measures the vocabulary's freedom. Section S2.8 lists what changed since version 3.5.

---

## S2.1 Notation

The twenty structural constants and their status (Lie datum, topological, input, combination) are listed in main §3.1. The relations also use the following, each a combination chosen by the framework:

| Symbol | Value | Definition | Register |
|--------|-------|-----------|----------|
| det(g) | 65/32 | p₂ + 1/(b₂ + dim G₂ − N_gen) = det_num/det_den (main App. B) | **imposed** normalization (register item R2); a second expression, Weyl · α_sum/2^Weyl, agrees with it on the line b₂ = 21 and differs elsewhere |
| κ_T⁻¹ | 61 | b₃ − dim(G₂) − p₂ | integer combination without a physical name (register item R3); a second expression, b₃ − b₂ + Weyl, agrees with it on the line b₂ = 21 and differs elsewhere |
| φ | (1 + √5)/2 | through the McKay correspondence E₈ ↔ 2I | additional step (register item R9) |
| 1 | 1 | the integer 1 | used freely as an additive constant |
| 2b₂ | 42 | also p₂ × N_gen × dim(K₇) | combination |
| τ | 3472/891 | dim(E₈×E₈) · b₂/(dim J₃(𝕆) · H*) | used only in the dimensionful entries of the dataset (Type II, S3) |

**Weyl = 5.** Three expressions give 5: (dim G₂ + 1)/N_gen, b₂/N_gen − p₂, dim G₂ − rank E₈ − 1. This is an arithmetic coincidence among the declared integers; it fixes no further quantity.

**N_gen = 3.** The integer identity (rank E₈ + N_gen) · b₂ = N_gen · b₃, i.e. 11 · 21 = 3 · 77, is satisfied by N_gen = 3. It is a consistency check on (21, 77): no index theorem is known that produces it, and the expression (77 − 8/3 · 21)/7 = 3 is the same arithmetic, with no operator whose index it would be (main §2.4).

---

## S2.2 Gauge sector and Higgs

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A01 | sin²θ_W (M_Z, MS-bar) | b₂/(b₃ + dim G₂) = 21/91 = **3/13** = 0.230769 | scale and scheme (R7) | integer; **proximity**; pull −7.5σ |
| A02 | α_s(M_Z) | √2/(dim G₂ − p₂) = **√2/12** = 0.117851 | operation √; scale (R7) | algebraic; pull −0.2σ |
| A03 | λ_H | √(dim G₂ + N_gen)/det_den = **√17/32** = 0.128847 | operation √; det(g) (R2); compared with the tree-level m_H²/(2v²) | algebraic; det(g); pull −1.3σ |
| A04 | α⁻¹(0) | (dim E₈ + rank E₈)/2 + H*/D_bulk + det(g) · κ_T = 128 + 9 + 65/1952 = **267489/1952** = 137.03330 | det(g) (R2); κ_T (R3); scale q² = 0 (R7) | det(g), κ_T; **proximity**; pull ≫ 10σ |

**On α⁻¹.** The three terms carry no physical name: the first two are integer combinations, and the third is the product of the imposed normalization and the unnamed combination κ_T. The relation lies 19.7 ppm below α⁻¹(0), whose relative uncertainty is 1.5 × 10⁻¹⁰: a proximity (main §4.2).

**On λ_H.** The comparison is with the tree-level m_H²/(2v²), a scheme choice declared in the register (R7, main §3.3). A second formula for λ_H is on record (S2.7).

---

## S2.3 Leptons (an overdetermined sector, register item R8)

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A05 | Q_Koide | dim G₂/b₂ = 14/21 = **2/3** | R8 | integer; approximate (R8); pull +0.4σ |
| A06 | m_τ/m_e | dim K₇ + 10 · dim E₈ + 10 · H* = 7 + 2480 + 990 = **3477** | R8; the coefficient 10 is not among the twenty constants | integer; approximate (R8); **tension**; pull −2.1σ |
| A07 | m_μ/m_e | dim(J₃(𝕆))^φ = **27^φ** = 207.0119 | R8; φ (R9) | φ; approximate (R8); **proximity**; pull ≫ 10σ |
| A22 | m_μ/m_τ | (b₂ − D_bulk)/\|PSL(2,7)\| = 10/168 = **5/84** = 0.059524 | R8 | integer; approximate (R8); **proximity**; pull +20.8σ |

Four relations bear on two independent mass ratios, and they are mutually incompatible: with 27^φ and 3477, the Koide parameter is 0.666546, not 2/3. None is selected (main §6.1). The factorization 3477 = 3 × 19 × 61 involves 19, which is not a structural constant. The associative 3-cycle volumes of S3 (the volume-difference entries of Type III) take ln(m_τ/m_e) = 8.154, the logarithm of the measured ratio, as their target, so their agreement with 3477 is the target returning and carries no independent information.

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
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = **37/42** = 0.880952 | n/a | integer; **proximity**; pull −3.8σ |

**The CKM sector is overdetermined (register item R12).** The three relations bear on two Wolfenstein parameters, since sin θ₂₃ = Aλ². With λ = 7/31 and A = 83/99, Aλ² = 4067/95139 = 0.042748, while the sin θ₂₃ relation gives 1/24 = 0.041667: the three relations are 2.6% apart as exact equalities, and at most two can hold. None is selected (main §4.2).

**Sines, not squared sines.** The two CKM relations 7/31 and 1/24 are compared with λ = sin θ₁₂ and Aλ² = sin θ₂₃ (S3.3).

**On the constant 42.** The integer 42 = 2b₂ appears in both m_b/m_t = 1/42 and Ω_DM/Ω_b = (1 + 42)/8. Two formulas that share an integer share a choice of vocabulary; no connection between the quantities is implied.

**m_W/m_Z from the published masses.** Like the other mass ratios, m_W/m_Z is computed from the PDG masses, 80.3625(77)/91.1879(20) = 0.88128(9), correlations neglected (S3.3).

**Dependence noted, not counted.** sin²θ_W in MS-bar and m_W/m_Z are related in the Standard Model through radiative corrections; the two relations are not independent tests in the strict sense.

---

## S2.5 Neutrino mixing

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A12 | sin²θ₁₂ (PMNS) | (1 + N_gen)/α_sum = **4/13** = 0.307692 | additive 1 | integer; pull −0.2σ |
| A13 | sin²θ₂₃ (PMNS) | (D_bulk − Weyl)/D_bulk = **6/11** = 0.545455 | octant (main §4.3) | integer; **tension** (octant; inside the NuFIT 3σ range, main §4.3); pull +4.4σ, not Gaussian (main §4.3) |
| A14 | sin²θ₁₃ (PMNS) | D_bulk/dim(E₈×E₈) = **11/496** = 0.022177 | n/a | integer; pull −0.5σ |
| A15 | δ_CP | dim K₇ · dim G₂ + H* = 98 + 99 = **197**, read as the phase 2π · 197/360 | **unit** (R6) | **unit assignment** (R6); pull −0.4σ |

**The δ_CP rule.** The prediction is the phase 2π · 197/360, a point value; the unit is a dictionary assignment (register item R6), and the decision rule of main §11.1 for δ_CP applies: a measurement whose 3σ interval excludes 197° rejects the relation and the unit assignment together, with no repair clause and no theoretical tolerance added afterwards.

---

## S2.6 Cosmology (an overdetermined sector, register item R11)

| ID | Relation | Arithmetic | Choices declared | Status (main §4.1) |
|----|----------|-----------|------------------|---|
| A23 | Ω_DE = Ω_Λ | ln 2 · (b₂ + b₃)/H* = ln 2 · 98/99 = **0.686146** | operation ln 2; R11 | ln 2; approximate (R11); pull +0.2σ |
| A24 | n_s | ζ(D_bulk)/ζ(Weyl) = **ζ(11)/ζ(5)** = 0.964864 | operation ζ | ζ values; pull 0.0σ |
| A25 | Ω_DM/Ω_b | (1 + 2b₂)/rank E₈ = **43/8** = 5.375 | additive 1; R11 | integer; approximate (R11); pull +0.1σ |
| A26 | Ω_c/Ω_Λ | det_num/\|PSL(2,7)\| = **65/168** = 0.386905 | R2; R11 | integer; det(g); approximate (R11); pull 0.0σ |
| A27 | Ω_Λ/Ω_m | (dim G₂ + H*)/dim F₄ = **113/52** = 2.173077 | R11 | integer; approximate (R11); pull 0.0σ |
| A28 | h | (\|PSL(2,7)\| − 1)/dim E₈ = **167/248** = 0.673387 | additive 1 | integer; pull 0.0σ |
| A29 | Ω_b/Ω_m | Weyl/det_den = **5/32** = 0.15625 | R2; R11 | integer; det(g); approximate (R11); pull −0.1σ |
| A30 | Ω_c/Ω_m | (det_den − Weyl)/det_den = **27/32** = 0.84375 | R2; R11 | integer; det(g); approximate (R11); **tension**; pull +2.5σ |
| A31 | σ₈ | (p₂ + det_den)/(2b₂) = 34/42 = **17/21** = 0.809524 | R2 | integer; det(g); pull −0.3σ |
| A32 | Y_p | (1 + dim G₂)/κ_T⁻¹ = **15/61** = 0.245902 | additive 1; R3 | integer; κ_T; pull +0.3σ |
| A33 | Ω_m/Ω_Λ | (1 + dim J₃(𝕆))/κ_T⁻¹ = **28/61** = 0.459016 | additive 1; R3; R11 | integer; κ_T; approximate (R11); pull −0.1σ |

**The seven density relations bear on two independent densities** (flat ΛCDM: Ω_b + Ω_c + Ω_Λ = 1) and are mutually incompatible as exact equalities (main §4.2):

| Quantity | Values implied by the relations |
|----------|--------------------------------|
| Ω_Λ/Ω_m | 113/52 = 2.1731 (the Ω_Λ/Ω_m relation); 61/28 = 2.1786 (inverse of the Ω_m/Ω_Λ relation); 2.1862 (Ω_DE with flatness) |
| Ω_c/Ω_b | 43/8 = 5.375 (the Ω_DM/Ω_b relation); 27/5 = 5.400 (Ω_c/Ω_m over Ω_b/Ω_m) |
| Ω_c/Ω_Λ | 65/168 = 0.3869 (the Ω_c/Ω_Λ relation); 0.3873 (Ω_c/Ω_m times Ω_m/Ω_Λ); 0.3883 (Ω_c/Ω_m over Ω_Λ/Ω_m) |

Ω_Λ/Ω_m and Ω_m/Ω_Λ are the same quantity, written with two formulas. The disagreements are below the Planck uncertainties of these ratios, which is why six of the seven pass at 2σ; Ω_c/Ω_m, whose uncertainty is much smaller (0.0019), is in tension at +2.5σ. The seven cannot hold together; none is selected (R11). Some are redundant and some subsets are compatible: the Ω_b/Ω_m and Ω_c/Ω_m relations are equivalent when neutrinos are neglected (Ω_m = Ω_b + Ω_c, so that 5/32 + 27/32 = 1), with or without flatness, and the largest compatible subsets have three relations, these two with one of Ω_DE, Ω_c/Ω_Λ, Ω_Λ/Ω_m or Ω_m/Ω_Λ (checked by solving each subset for (Ω_b, Ω_c)).

**Not among the 33.** Ω_m = Ω_DE/√Weyl = 0.3068 (2.7% from Planck) would be an eighth density relation, incompatible with the others; it is not part of the dataset. The factor ln 2 in Ω_DE is an operation of the grammar, with no computation behind it. Against the Planck 2018 chains, Ω_DM/Ω_b is 5.364 ± 0.077.

---

## S2.7 Vocabulary freedom: alternative formulas on record

For each relation one can count the distinct expressions in the constants that reduce to the same value (for example 14 for sin²θ_W = 3/13, 20 for Q_Koide = 2/3, 21 for m_b/m_t = 1/42). A value reached by many paths through twenty constants is a value the vocabulary reaches easily: the count measures the vocabulary's freedom (register items R4, the formula assignments, and R5, the grammar and vocabulary). It is not what the look-elsewhere test of main §7 prices: the published values 3/13 and 1/42 lie outside their 2σ windows, and the 30 targets that every competitor reaches are already reached by the universal constants of the grammar, with no constant of K₇ at all (S4.2.2). The counts are:

| Relation | Distinct expressions recorded | Examples |
|----------|-------------------------------|----------|
| sin²θ_W = 3/13 | 14 | N_gen/α_sum; b₂/(b₃ + dim G₂); dim J₃(𝕆)/(dim F₄ + det_num); (1 + dim G₂)/det_num |
| Q_Koide = 2/3 | 20 | p₂/N_gen; dim G₂/b₂; dim F₄/dim E₆; rank E₈/(Weyl + dim K₇) |
| m_b/m_t = 1/42 | 21 | 1/(2b₂); (1 + N_gen)/\|PSL(2,7)\|; p₂/(dim K₇ + b₃); N_gen/(dim J₃(𝕆) + H*) |
| sin²θ₁₂ (PMNS) = 4/13 | 28 | n/a |
| m_H/m_t = 8/11 | 19 | n/a |
| m_u/m_d = 79/168, m_H/m_W = 81/52 | 1 each | n/a |

**Second formulas for the same observable.** The project's record also contains formulas that give a *different* value for the same observable, chosen at different times:

| Observable | Dataset formula | Other formula on record |
|------------|-----------------|-----------------------------|
| λ_H | √17/32 = 0.12885 | b₂(M₁)/(b₃ + b₂(M₂)) = 11/87 = 0.12644 (TCS building blocks) |
| Ω_DE | ln 2 · 98/99 = 0.68615 | 1 − χ(K3)/b₃ = 53/77 = 0.68831 |
| m_c/m_s | 246/21 = 11.714 | b₂(M₁) + dim K₇/b₂(M₂) = 117/10 = 11.700 |
| Ω_Λ/Ω_m | 113/52 = 2.1731 | (det_den − dim K₇)/D_bulk = 25/11 = 2.2727; 61/28 (the Ω_m/Ω_Λ relation inverted) |
| θ₁₃ | sin²θ₁₃ = 11/496 | θ₁₃ = π/b₂ = 8.571°; θ₁₃ = 94/11 = 8.545° read in degrees |
| θ₂₃ | sin²θ₂₃ = 6/11 (θ = 47.6°) | θ₂₃ = arcsin(75/99) = 49.25° (sin²θ₂₃ = 0.574) |
| θ₁₂ | sin²θ₁₂ = 4/13 | θ₁₂ = arctan √((2π/25)/(511/884)) = 33.40° |
| δ_CP | 197 | 197 × 62/69 = 177.01 (S2.8) |

The formulas labelled "TCS building blocks" (twisted connected sum) use b₂(M₁) = 11 and b₂(M₂) = 10, Betti numbers of building blocks whose identification is open (main §9). Several alternatives were introduced after a release of the data had moved: the Ω_DE alternative was preferred against one Planck release and not the other, and the θ₁₃ alternative "in degrees" is a second unit assignment of the kind register item R6 records. None of these is part of the 33; they are listed because they show, on the framework's own record, how many formulas the vocabulary offers for one observable and how the choice among them was made.

**Patterns.** The Fibonacci and Lucas numbers among the constants (2, 3, 5, 8, 13, 21; 7, 11) and the identities among the integers (dim G₂ = p₂ · dim K₇, b₂ = N_gen · dim K₇, \|PSL(2,7)\| = rank E₈ · b₂, b₃ + dim G₂ = dim K₇ · α_sum) are arithmetic facts about the chosen integers. Small integers satisfy many such identities; no physical consequence follows from these.

---

## S2.8 Changes since version 3.5

The sections above state the present position. This section lists, once, what versions up to 3.5 of this supplement said that version 3.6 no longer says.

| Earlier statement | Present position |
|-------------------|--------------------|
| the supplement titled "Complete Derivations", each relation presented as a theorem with a proof | arithmetic, dictionary choices and status (S2.0) |
| "proof", "VERIFIED", "TOPOLOGICAL" as statuses of the relations | the arithmetic is exact; the assignment is not derived (S2.0) |
| N_gen = 3 by the Atiyah–Singer index theorem | no operator is specified; the expression is the integer identity of S2.1 |
| "All 33 predictions use only topological invariants; no fitting" | eight use the imposed normalization or κ_T (R2, R3); the formulas were chosen with the values known (R4) |
| Mean deviation 0.73%, "11 exact matches", deviation histograms | computed against an earlier dataset; a mean deviation measures closeness, which is not distinctive (main §4.2, §7) |
| Statistical uniqueness: 192 349 alternatives, none better, P < 5 × 10⁻⁶, gauge-group and holonomy rankings | the alternatives were scored with the framework's own formulas, not allowed to search; replaced by the preregistered test of main §7 and S4 |
| "Literature uniqueness" of (21, 77) | absence from a catalogue is not selection; the selection audit is main §10 |
| Results "from analysis of the Newton–Kantorovich-certified metric": V_min formula, U(1)² symmetry, origin of the SM gauge group from triality | properties of an approximate local metric (main §2.3, §9); not used by any relation; the gauge group is assumed (main §2.3) |
| κ_T = 1/61 as a "topological torsion capacity"; 61 = dim F₄ + N_gen² | an integer combination without a physical name (R3); a second expression for 61 is another instance of S2.7 |
| det(g) = 65/32 "consistent with the topological formula" via three algebraic paths | imposed normalization (R2); the metric optimization was constrained to this target |
| 3477 "factorizes into framework constants"; a "period-integral cross-confirmation" of 3477 from associative volumes | 19 is not a structural constant; the volumes take the measured ratio as their target (S2.3) |
| Ω_m = Ω_DE/√5 as a "derived" relation; Ω_DM/Ω_b = 43/8 "exact" (from a dataset value 5.375 ± 0.1 that matched no Planck column); ln 2 as a "binary information factor" of the moduli space | not among the 33; 5.364 ± 0.077 on the Planck chains; an operation of the grammar (S2.6) |
| the three terms of α⁻¹ named "algebraic", "bulk impedance" and "torsional correction" | no physical name (S2.2) |
| Weyl = 5 as a "triple identity"; the additive constant 1 written b₀ | an arithmetic coincidence; the integer 1 (S2.1) |
| the two CKM relations labelled sin²θ₁₂ and sin²θ₂₃ | sines (S2.4, S3.3) |
| 42 in m_b/m_t and Ω_DM/Ω_b as "connecting quark physics to large-scale structure" | a shared choice of vocabulary (S2.4) |
| counts of equivalent expressions as "structural robustness"; an "algebraic web" and a "Fibonacci–Lucas embedding" reflecting icosahedral geometry | measures of the vocabulary's freedom; arithmetic facts (S2.7) |
| "at most two of the seven density relations can be exact" (earlier drafts of 3.6) | the largest compatible subsets have three (S2.6) |

**The factor 62/69 (Appendix F of earlier versions).** A search after the NuFIT 6.0 release found 197 × 62/69 = 177.01, matching that release's central value, and earlier versions kept it as a "contingency plan": if DUNE measured δ_CP near 177°, the framework would adopt 177.01 and read 197 as a "bare" value. That is a repair clause, and the decision rule has none (main §11.1): if a measurement excludes 197° at 3σ, the relation δ_CP = 197 and its unit assignment are rejected, and no factor found afterwards replaces them. The factor 62/69 = 248/276 is recorded in S2.7 as one more formula the vocabulary offers.

---

## References

The sources named in this supplement (PDG, NuFIT, Planck, Koide) are those of the main paper's bibliography, which is shared across the main paper and Supplements S1-S4.

---

*The K₇ Framework (formerly GIFT): Supplement S2*
*The 33 relations: arithmetic, dictionary choices and status*
