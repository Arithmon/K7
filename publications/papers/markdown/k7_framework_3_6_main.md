# The K₇ Dictionary: Testing G₂ Topology against Particle Physics and Cosmology

**Brieuc de La Fournière**

*Independent researcher, Beaune, France*

---

## Abstract

The Standard Model leaves about nineteen parameters to measurement. This paper states a **declared correspondence**: the topological and Lie-theoretic invariants of a compact seven-manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with an E₈×E₈ gauge structure, are assigned to dimensionless Standard-Model and cosmological parameters by explicit closed forms. The correspondence is a privileged candidate, not a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable. The paper makes it auditable instead. It gives the **dictionary** (twenty structural constants and a grammar), a **residue register** of everything that is set rather than derived, and a **decision rule** with no repair clause. The core is 33 relations with no continuously adjustable parameter; they are not 33 independent tests, since three sectors are overdetermined. Against current data (PDG 2026, NuFIT 6.1, Planck 2018), 23 lie within two standard deviations of measurement, two are in tension between 2σ and 3σ, six are excluded as exact equalities at more than 3σ and kept as numerical proximities, m_s/m_d lies inside a PDG range that carries no uncertainty, and sin²θ₂₃ sits in the octant the global fit disfavours, inside its 3σ range. A preregistered look-elsewhere test, in which every competing Betti pair and invented vocabulary searches for its own formulas, finds that K₇ reaches 31 of the 33 targets and that a quarter of the alternative Betti pairs and half of the invented vocabularies reach as many (§7.2): closeness to today's values does not single out K₇. Measurements to come can. The register is frozen, and each relation is exposed to data that did not exist when it was written: JUNO will determine sin²θ₁₂ about four times more tightly than the present global fit, against 4/13; DUNE and Hyper-Kamiokande will measure the leptonic CP phase, against 2π·197/360; τ-mass and cosmological measurements bear on others (§11). Existence of a compact torsion-free G₂ metric with these Betti numbers is open (§9).

**Keywords**: G₂ holonomy, exceptional Lie algebras, Standard Model parameters, selection problem, falsifiability, look-elsewhere effect, formal verification

---

**Framework status at a glance (version 3.6).**

*Formerly presented as the Geometric Information Field Theory (GIFT), versions 1.0–3.4 of this record.*

- **What is proposed.** A correspondence between invariants of (K₇, E₈×E₈) and 33 dimensionless parameters, written in a declared dictionary (§3). It is a privileged candidate, chosen by the author, not a selection that the requirements force (§3.5).
- **What is set rather than derived.** The residue register of §3.3: the Betti pair, det(g) = 65/32, κ_T⁻¹ = 61, the unit of δ_CP, the comparison scales, the formula assignments.
- **What is established.** The arithmetic identities stated for the relations, machine-checked in Lean 4 (§8, S3.7); a Newton–Kantorovich-certified local metric [A]. These verify the stated arithmetic and a local metric, not physical content; the relations, each correctly computed, are mutually incompatible in the overdetermined sectors (§4.2). No construction of a compact G₂ manifold with (21, 77) is currently known (§2.3).
- **What is open.** A compact torsion-free G₂ manifold realising K₇ (§9); a physical mechanism from the smooth K₇ to the chiral non-abelian Standard Model (§2.3); the selection of (21, 77) (§10); a rule that assigns formulas to observables (§3.2).
- **What would refute it.** The 33 equalities taken jointly are already incompatible, so that exact system cannot be true (§4.2). Individual relations remain testable, each under the decision rule of §11, and several meet tighter data within the decade (§11.2). The wider exploratory programme has, at present, no single criterion of refutation.
- **What changed since version 3.5.** Appendix D, once; the body states the present position.

---

## 1. Introduction

### 1.1 The parameter problem and the selection problem

The Standard Model describes the known interactions with great precision, yet leaves about nineteen parameters to experiment [1]: gauge couplings, Yukawa couplings spanning five orders of magnitude, mixing angles and phases, and the Higgs sector. It does not explain its gauge group or the number of generations, and it leaves open the hierarchy problem [2] and the flavour puzzle [5]; cosmology adds a persistent tension between early- and late-universe determinations of H₀ [3, 4]. General relativity does not derive the dimension of spacetime, and string theory has of the order of 10⁵⁰⁰ vacua with no internal criterion for electing one. The question *why this structure rather than another?* is the shape that explanatory regress takes in fundamental physics, and every framework that proposes structure inherits it.

Two questions are easily run together, and this paper keeps them apart.

1. **Does a family of structures deserve to be explored?** A good answer points to requirements, motivated independently of one another and of the Standard Model's values, that the family might satisfy together.
2. **Why this precise structure, and these precise assignments, rather than their competitors?** A good answer shows that the requirements eliminate the competitors, or make their differences physically indiscernible.

For K₇ the first question has a positive answer, given in §2: the octonions, G₂ holonomy and E₈ are structures whose interest owes nothing to the Standard Model's constants. The second question is **not** answered here. The pair (21, 77) is not derived (§10), and the formulas are assigned rather than forced (§3.2).

### 1.2 What the paper is

The paper states a correspondence, gives the means to audit it, and says what would reject it. It has three parts.

- **The correspondence and its dictionary (§2–§4).** The mathematical inputs; the twenty structural constants and the grammar of formulas; the 33 relations, each with its measured deviation and its status.
- **The audit (§5–§10).** Consistency checks on the gauge and lepton sectors; the look-elsewhere test; the formal verification; the existence status of K₇; the selection audit of (21, 77).
- **The rule and the tests to come (§11).** A decision rule written in advance, with no repair clause, and the measurements that will apply it.

Throughout, the residue register of §3.3 is given the same rank as the results. A relation is only as rigid as the pair (structure, dictionary) that produces it: when the structure is rigid but the dictionary is free (which integer, which operation, which unit, which scale), the freedom driven out of continuous parameters returns through the discrete assignments. The register is where those assignments are written down.

### 1.3 Paper organization

- **§2** Mathematical inputs: octonions, E₈×E₈, the topological type of K₇, and what the Betti numbers constrain.
- **§3** The correspondence and its dictionary: structural constants, grammar, residue register, claims, and the status of a privileged candidate.
- **§4** The 33 relations, and the conditional status of the other dataset entries.
- **§5** Gauge sector: consistency checks on an assumed Standard-Model content.
- **§6** Lepton masses: four incompatible relations, none selected, and the conditional mechanisms.
- **§7** Look-elsewhere: four published null tests, and a null in which competitors search for their own formulas.
- **§8** Formal verification (method).
- **§9** Existence status of the compact K₇.
- **§10** Selection audit of (21, 77).
- **§11** Decision rule, out-of-sample tests and timeline.
- **§12** Discussion and conclusion: where the necessity of K₇ ends.

Four supplements give technical details: S1 (mathematical foundations), S2 (the arithmetic of the 33 relations and the dictionary choices each makes), S3 (the 95-entry dataset, with a status column), S4 (Sieve and look-elsewhere diagnostics). Appendix D lists what changed since version 3.5.

---

## 2. Mathematical Inputs

### 2.1 The octonionic foundation

The real normed division algebras are ℝ, ℂ, ℍ and 𝕆, of dimensions 1, 2, 4 and 8 (Hurwitz). The octonions are the last of the four and the only non-associative one. Their automorphism group G₂ = Aut(𝕆) has dimension 14 and acts on Im(𝕆) ≅ ℝ⁷. The exceptional Lie algebras are tied to the octonions through a chain established in the literature [17]:

| Algebra | Dimension | Connection to 𝕆 |
|---------|-----------|-----------------|
| G₂ | 14 | Aut(𝕆) |
| F₄ | 52 | Aut(J₃(𝕆)) |
| E₆ | 78 | Collineations of 𝕆P² |
| E₈ | 248 | Contains the lower exceptional algebras |

Octonionic approaches to Standard-Model structure form an independent line of research [7, 8, 10, 37]. A G₂-holonomy seven-manifold is the geometric setting in which this algebra acts on tangent spaces, which is the reason for exploring it here.

The G₂ structure is encoded in the standard 3-form on ℝ⁷ (Bryant–Joyce convention):
$$\varphi_0 = e_{012} + e_{034} + e_{056} + e_{135} - e_{146} - e_{236} - e_{245}.$$
G₂ is the stabilizer of φ₀ in GL(7, ℝ), and its Lie algebra is the kernel of $X \mapsto \mathcal{L}_X \varphi_0$ on 𝔤𝔩(7), of dimension 49 − 35 = 14. This is formalized in Lean (`G2ThreeForm.lean`).

### 2.2 E₈×E₈ structure

E₈ is the largest exceptional simple Lie algebra, of dimension 248 and rank 8 [18]. The product E₈×E₈, of total dimension 496, is one of the two gauge groups of ten-dimensional heterotic string theory [19]; in heterotic M-theory it appears on the two boundaries of an eleven-dimensional spacetime [32]. The framework uses E₈×E₈ as a source of group-theoretic data. It does not specify a compactification of either string theory or M-theory that realises it.

The Standard-Model gauge algebra sits inside one E₈ through a chain of subgroup branchings,
$$E_8 \supset E_6 \times SU(3) \supset SO(10) \times U(1) \supset SU(5) \times U(1) \supset SU(3)_c \times SU(2)_L \times U(1)_Y,$$
compatible with the Standard-Model representations. This is a chain of embeddings, not a breaking mechanism: an actual breaking would specify the mechanism (Wilson lines, a gauge bundle, a singular locus) responsible for each step, and none is specified here. The intermediate SU(5) × U(1) step is of Georgi–Glashow type, not Pati–Salam. The second E₈ is a hidden sector whose physical role is not committed to. That E₈ can accommodate three generations with grand-unified structure has been argued independently [9].

### 2.3 The K₇ manifold

The framework posits a compact, simply connected seven-manifold K₇ with holonomy G₂ and Betti numbers (b₂, b₃) = (21, 77). A compact Riemannian seven-manifold with holonomy G₂ is Ricci-flat, and its compactification of M-theory preserves N = 1 supersymmetry in four dimensions [11]. Whether a compact manifold of this kind exists with these Betti numbers is open (§9); the relations of §4 use only the integers, never the metric.

**What is known about the geometry.**
- *Topology.* Among the catalogued compact G₂ examples (Joyce's orbifold constructions [20] and the twisted connected sums of Corti–Haskins–Nordström–Pacini [21, 22]), the pair (21, 77) does not appear (see [12, 14, 15] for the construction literature and census), and orthogonal twisted connected sums are excluded by parity (b₂ + b₃ = 98 is even; [22], Lemma 6.7). **A Joyce–Karigiannis ℤ₂³ orbifold route [43] does not realise (21, 77)**: the character of the group action on H²(K3) forces b₂ ≥ 5 and b₃ ≤ 16 on the quotient for every compatible torus action, and the involution profile requires a K3 of Picard rank at least 17 (S1 §8.4; the lattice inputs come from [44, 45, 51]). This closes that route, not every possible construction of a compact G₂ manifold with Betti numbers (21, 77). No such construction is currently known.
- *A local metric.* An explicit approximate G₂ metric on a gluing region, g = g_seam(s) ⊕ g_{T²} ⊕ g_{K3}(y), with 169 Chebyshev–Cholesky parameters, carries a Newton–Kantorovich certificate (h = 8.95 × 10⁻⁹) for a nearby torsion-free metric within a ball δg/g ≤ 4.86 × 10⁻⁶ [A]. Its spectral analysis [B] gives no independent evidence for (b₂, b₃) = (21, 77): the multiplicities it reports are built from decompositions withdrawn in S1 §8.3 and §9.3. The certificate is local: it does not construct a compact K₇ (§9).
- *A neck ansatz and a conditional analytic scheme.* An explicit closed-form positive G₂ 3-form on a neck region with K3 coassociative fibres is certified in [D]. The conditional analytic scheme of [E] for a K₇ → S³ construction with 77 branch components is computed at a datum 𝒟₀ that is not realisable as posed (§9).
- *The K3 fibre.* No certified bound on a Ricci-flat metric of the K3 fibre is available [ERR, §1]. An explicit K3 surface has a publicly certified holomorphic atlas, with no metric claim [K3A].

**Metric normalization.** The framework imposes det(g) = 65/32 on the metric. This value is a target, not a consequence of the topology (R2, §3.3). Six of the 33 relations depend on it.

**The physical gap.** In the standard M-theory dictionary, a compactification on a *smooth* G₂ manifold yields b₂ abelian vector multiplets and no chiral fermions; non-abelian gauge symmetry and chirality require codimension-four and codimension-seven singularities [25, 11]. The framework does not supply such singularities, a heterotic gauge bundle, or a duality that would turn its dictionary into a physical mechanism. Its gauge-sector statements (§5) are therefore consistency checks on an assumed Standard-Model content, not a derivation of it.

### 2.4 What the Betti numbers constrain

**Capacities.** In M-theory on a smooth G₂ manifold, b₂ counts abelian vector multiplets and b₃ counts neutral chiral multiplets [11]. The framework reads b₂ = 21 and b₃ = 77 as capacities of the gauge and matter sectors. The non-abelian Standard-Model gauge group does not come from these multiplets.

**An integer identity.** The integers satisfy
$$(\mathrm{rank}(E_8) + N) \cdot b_2 = N \cdot b_3 \quad\Longleftrightarrow\quad (8 + N) \cdot 21 = 77\,N \quad\Longleftrightarrow\quad N = 3.$$
Equivalently, N_gen = b₂ / dim(K₇) = 21/7. The identity reproduces the measured N_gen = 3; it is counted as a consistency check, since no index theorem is known that produces it.

---

## 3. The Correspondence and Its Dictionary

A relation of the framework has the form *observable ≈ closed form in the structural constants*. Whether such a relation is evidence depends on three things that the formula alone does not show: where the constants come from, how much freedom there was in writing the formula, and how the formula was matched to the observable. This section states all three.

### 3.1 The structural constants

All 33 relations are written in twenty structural constants. Seven are primitive; thirteen are derived from them, and the derivation is part of the dictionary. Small integer coefficients also occur, and they are choices of formula: the integer 1 (S2) and the coefficient 10 of m_τ/m_e. At K₇, 10 equals p₂ · Weyl; that rewriting is not a derivation of the coefficient, and the formula is not stated that way.

| # | Constant | Value | Origin | Status |
|---|----------|-------|--------|--------|
| 1 | dim(E₈) | 248 | Lie algebra | Lie datum |
| 2 | rank(E₈) | 8 | Cartan subalgebra | Lie datum |
| 3 | dim(G₂) | 14 | Aut(𝕆) | Lie datum |
| 4 | dim(K₇) | 7 | Im(𝕆) | topological |
| 5 | b₂(K₇) | 21 | posited (§10) | input |
| 6 | b₃(K₇) | 77 | posited (§10) | input |
| 7 | dim(J₃(𝕆)) | 27 | exceptional Jordan algebra | Lie datum |
| 8 | N_gen | 3 | b₂/dim(K₇); the integer identity of §2.4 | measured, reproduced |
| 9 | p₂ | 2 | dim(G₂)/dim(K₇) ("binary ratio"; not a Pontryagin class) | combination |
| 10 | Weyl | 5 | factor of \|W(E₈)\| | combination |
| 11 | H* | 99 | b₂ + b₃ + 1 | combination |
| 12 | dim(E₆) | 78 | Lie algebra | Lie datum |
| 13 | dim(E₇) | 133 | Lie algebra | Lie datum |
| 14 | dim(F₄) | 52 | Aut(J₃(𝕆)) | Lie datum |
| 15 | fund(E₇) | 56 | fundamental representation | Lie datum |
| 16 | \|PSL(2,7)\| | 168 | automorphisms of the Fano plane | Lie datum |
| 17 | D_bulk | 11 | 4 + 7 | combination |
| 18 | α_sum | 13 | rank(E₈) + Weyl | combination |
| 19 | det_den | 32 | b₂ + dim(G₂) − N_gen | combination; enters det(g) |
| 20 | det_num | 65 | p₂ · det_den + 1 (also Weyl × α_sum) | combination; enters det(g) |

Two further quantities appear in the relations: κ_T⁻¹ = b₃ − dim(G₂) − p₂ = 61, an integer combination with no established physical meaning, and the golden ratio φ = (1 + √5)/2, which enters one relation through the McKay correspondence E₈ ↔ 2I (S2.1, R9).

The *status* column distinguishes constants that come from the mathematics independently of this framework (Lie data, topological dimension), inputs posited by the framework (b₂, b₃), and *combinations*: integers built from the others by the framework's own choices. A combination is not an independent datum: choosing to name 32 or 61 is part of the dictionary.

### 3.2 The grammar, and the absence of an assignment rule

**The grammar.** Formulas are rational expressions in the structural constants, with a small set of additional operations: square roots, integer powers, the exponent φ, the logarithm ln 2 and ratios of zeta values. This grammar was frozen with the observable list in a public release [S-frozen] on 12 June 2026, *after* the formulas of the framework had been found. Freezing after discovery does not remove the look-elsewhere effect; it only prevents it from growing. §7 measures it.

**No assignment rule.** There is no rule, internal to the framework, that says which formula is assigned to which observable. Each of the 33 relations was found by searching for a closed form in the structural constants close to a measured value, and was then retained. The metric enters none of the formulas, and no map from the geometry to the observables is known. The formula assignments are therefore **assignments**, declared in the residue register, and the question of why (21, 77) (§10) is distinct from the question of why these formulas.

Structural redundancy does not repair this. That sin²θ_W = 3/13 can be written in fourteen ways, and Q = 2/3 in twenty, in the structural constants (S2.7) measures the *size of the vocabulary*, not the absence of choice: a richer vocabulary reaches a given value by more routes. These counts measure the freedom that §7 prices.

### 3.3 The residue register

The residue is the part of the framework not fixed by its requirements: what was set rather than derived. It is written here with the same prominence as the results, because it indicates where a further requirement would have to bite, or where the framework's necessity ends.

| Item | What is set | Where it acts | Status |
|------|-------------|---------------|--------|
| R1 | (b₂, b₃) = (21, 77) | every relation | input; five derivation routes audited and closed, one open identity (§10) |
| R2 | det(g) = 65/32 | λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈ | **imposed** normalization; not derived from the topology. Results are given with and without these six relations (§4.4). Like κ_T⁻¹, it has a second expression, Weyl · α_sum/2^Weyl, that agrees with p₂ + 1/(b₂ + dim G₂ − N_gen) on the line b₂ = 21 and differs elsewhere; the one used is the latter (App. B) |
| R3 | κ_T⁻¹ = 61 = b₃ − dim(G₂) − p₂ | α⁻¹, Y_p, Ω_m/Ω_Λ | integer combination without a physical name; it also has a second expression in the structural constants that agrees with the first on the whole line b₂ = 21 and differs elsewhere, and the one used is declared here |
| R4 | the formula assigned to each observable | all 33 | no assignment rule (§3.2) |
| R5 | the grammar and vocabulary | all 33 | frozen after discovery; priced in §7 |
| R6 | the unit in which 197 is read | δ_CP | **unit assignment**: the structure gives the integer 197; reading it in degrees makes the prediction the phase 2π·197/360, and the 360 does not come from the structure (§4.3) |
| R7 | the comparison scale and mass scheme | sin²θ_W, α_s (at M_Z); α⁻¹ (at q² = 0); λ_H; m_b/m_t | declared; the relations are not claimed to hold at a common scale (§5). λ_H is compared with the tree-level m_H²/(2v²) = 0.12914, a definition that is itself a scheme choice (S3); the MS-bar quartic coupling at the top-mass scale is lower, about 0.126 [60], and would exclude √17/32. m_b/m_t compares m_b in MS-bar at m_b with the directly measured m_t: a ratio of masses in two schemes, with no scheme-independent meaning (0.0243 in this reading, about 0.026 with both masses in MS-bar). The scheme is fixed here, and the relation is tested in it: at −10σ it is rejected as an exact equality (§11); reading it in another scheme afterwards would be a repair, which §11 excludes |
| R8 | the choice among the lepton relations | m_μ/m_e, m_τ/m_e, Q_Koide, m_μ/m_τ | four relations on two ratios, mutually incompatible; the framework selects none, and none is declared primary: a selection made after the values are known would be a dictionary choice, not a result (§6.1) |
| R9 | the exponent φ | m_μ/m_e | enters through the McKay correspondence, an additional step not shared by the integer relations |
| R10 | the unit of Type II entries | absolute masses (MeV) | dimensionful numbers read in a chosen unit; not claimed (§4.5) |
| R11 | the choice among the cosmological density relations | Ω_DE, Ω_DM/Ω_b, Ω_c/Ω_Λ, Ω_Λ/Ω_m, Ω_b/Ω_m, Ω_c/Ω_m, Ω_m/Ω_Λ | seven relations on two independent densities (neutrino density neglected; flat ΛCDM for those that involve Ω_Λ), mutually incompatible as exact equalities; Ω_Λ/Ω_m and Ω_m/Ω_Λ are the same quantity with two formulas; none is selected (§4.2) |
| R12 | the choice among the CKM relations | sin θ₁₂, A, sin θ₂₃ (CKM) | three relations on two Wolfenstein parameters (sin θ₂₃ = Aλ²), mutually incompatible as exact equalities (2.6% apart); none is selected (§4.2) |

### 3.4 What is claimed

Given the declared constants and the declared assignments, the 33 relations hold as algebraic identities (machine-checked, §8), and they lie at the deviations from measurement listed in §4, with the statuses listed there. The decision rule of §11 applies to them. Nothing beyond this is claimed. Each limit is stated where it acts: what is set, in the register above; the geometric and physical gaps, in §2.3 and §9; the look-elsewhere result, in §7.

### 3.5 Why state a correspondence that is not derived

A correspondence that is not derived can still be worth stating, provided its status is stated with it. Three states are open to a programme that asks why a structure is the one realised:

1. **Demonstrated uniqueness.** The requirements leave one object, or one class whose members are physically equivalent.
2. **Residual family.** The requirements leave several physically distinct candidates, and the programme says what would tell them apart.
3. **Privileged candidate.** The requirements leave a family, and the author designates a member for reasons that are the author's own and are declared as such.

All three are legitimate. What is not legitimate is to present the third as the first. The three states, and the condition of independence stated below, are developed in a companion paper in the philosophy of science [WNE], which also audits version 3.5 of this framework against them. K₇ is in the third state. The requirements that motivate it (G₂ holonomy, compactness, the E₈ data) are justified independently of the Standard Model's values, which answers the first question of §1.1. They do not select (21, 77), the formulas, or the normalization: these are where the author's choice enters, and the register of §3.3 records them.

Two points follow, and they set the posture of the paper.

**Independence must hold where the selection happens.** A requirement such as "G₂ holonomy" has independent warrant: Berger's classification, the octonions and M-theory give reasons to study it that owe nothing to particle physics. But a requirement of the form "G₂ holonomy *together with* this realisation and these assignments" inherits the warrant of G₂ holonomy without that warrant reaching the realisation. Whatever selects (21, 77) and the formulas would need a justification of its own that does not run through the values it produces. None is available yet.

**Rigidity exposes a framework; it does not certify it.** The 33 relations have no continuous parameter: an integer ratio cannot be nudged. That makes each relation refutable by a single measurement, provided its dictionary is fixed in advance, which is what §11 does. It does not make the framework true, and it does not show that the structure was earned rather than picked: an exceptional structure is rigid whether it was derived or chosen for the values it gives. Rigidity is used here as a criterion of exposure, not as a guide to truth.

**Posture.** The framework is read as a structural proposal, in the moderate structural-realist sense of Worrall [40] and Ladyman and Ross [41]: structure is asked to carry predictive weight, with no further ontological commitment. Readings in which geometry and information are aspects of one configuration, in the spirit of Wheeler's "it from bit" [39], historically motivated the work; they are neither required nor supported by the relations. A short essay discusses this posture for a general audience [essay].

---

## 4. The 33 Relations

**Dataset.** Experimental values and uncertainties are those of the framework's observable dataset (S3): PDG 2026 for particle data, NuFIT 6.1 for neutrino mixing (normal ordering, with the tabulated Super-Kamiokande and IceCube atmospheric data), Planck 2018 for cosmology (TT,TE,EE+lowE+lensing, one column for all entries; Y_p is the PDG's observational helium abundance), CODATA 2022 for α and m_μ/m_e. Mass ratios are computed from the published masses, with error propagation that neglects correlations (an approximation, not a bound: the summary tables do not publish the covariances, and their sign matters). The Planck density ratios are computed sample by sample on the published chains [3], which keeps their correlations (S3). All uncertainties are brought to 1σ: entries the PDG quotes at 90% confidence (the quark masses and m_u/m_d of its summary tables) are divided by 1.645. For asymmetric uncertainties the pull uses the side facing the K₇ value. m_s/m_d is given by the PDG as a range (17–22), without an uncertainty; no pull is computed for it. Quark masses and their ratios are MS-bar values at the PDG reference scales; sin²θ_W and α_s are at M_Z in MS-bar; α⁻¹ is the Thomson-limit value at q² = 0. Each comparison therefore carries a (scheme, scale, dataset) tag [1, 3, 27, 50]. The column *pull* is (K₇ − measured)/σ_exp with the experimental uncertainty alone: the framework supplies no theoretical uncertainty.

### 4.1 Table

| ID | Observable | Formula | K₇ value | Measured | Dev. | Pull | Status |
|---|-------|-------------|------|----------|------|-----|--------|
| A01 | sin²θ_W (M_Z) | b₂/(b₃ + dim G₂) = 3/13 | 0.230769 | 0.23122(6) | −0.19% | −7.5σ | integer; **proximity** |
| A02 | α_s(M_Z) | √2/(dim G₂ − p₂) = √2/12 | 0.117851 | 0.1180(9) | −0.13% | −0.2σ | algebraic |
| A03 | λ_H | √(dim G₂ + N_gen)/det_den = √17/32 | 0.128847 | 0.12914(23) | −0.22% | −1.3σ | algebraic; det(g) |
| A04 | α⁻¹(0) | 128 + 9 + det(g)·κ_T | 137.0333 | 137.035999177(21) | −0.0020% | ≫ 10σ | det(g), κ_T; **proximity** |
| A05 | Q_Koide | dim G₂/b₂ = 2/3 | 0.666667 | 0.6666645(51) | +0.0003% | +0.4σ | integer; approximate (R8) |
| A06 | m_τ/m_e | 7 + 10·248 + 10·99 = 3477 | 3477 | 3477.37(18) | −0.011% | −2.1σ | integer; approximate (R8); **tension** |
| A07 | m_μ/m_e | 27^φ | 207.012 | 206.7682827(46) | +0.12% | ≫ 10σ | φ; approximate (R8); **proximity** |
| A08 | m_s/m_d | p₂² × Weyl = 20 | 20 | 17–22 (range) | n/a | n/a | integer; inside the PDG range |
| A09 | m_c/m_s | (dim E₈ − p₂)/b₂ = 246/21 | 11.714 | 11.769(35) | −0.46% | −1.6σ | integer |
| A10 | m_b/m_t | 1/(2b₂) = 1/42 | 0.023810 | 0.024253(43) | −1.83% | −10.2σ | integer; **proximity** (in the scheme declared in R7) |
| A11 | m_u/m_d | (1 + dim E₆)/\|PSL(2,7)\| = 79/168 | 0.470238 | 0.462(12) | +1.78% | +0.7σ | integer |
| A12 | sin²θ₁₂ (PMNS) | (1 + N_gen)/α_sum = 4/13 | 0.307692 | 0.3088(+67/−66) | −0.36% | −0.2σ | integer |
| A13 | sin²θ₂₃ (PMNS) | (D_bulk − Weyl)/D_bulk = 6/11 | 0.545455 | 0.470(+17/−14) | +16.05% | +4.4σ* | integer; **tension** (octant; inside the NuFIT 3σ range, §4.3) |
| A14 | sin²θ₁₃ (PMNS) | D_bulk/dim(E₈×E₈) = 11/496 | 0.022177 | 0.02248(+55/−59) | −1.35% | −0.5σ | integer |
| A15 | δ_CP | dim K₇ · dim G₂ + H* = 197 | 197 → phase 2π·197/360 | 212 (+26/−36)° | −7.08% | −0.4σ | **unit assignment** (R6) |
| A16 | sin θ₁₂ (CKM) | fund(E₇)/dim E₈ = 56/248 | 0.225806 | 0.22517(68) | +0.28% | +0.9σ | integer; approximate (R12) |
| A17 | A (Wolfenstein) | (Weyl + dim E₆)/H* = 83/99 | 0.838384 | 0.826(+17/−15) | +1.50% | +0.7σ | integer; approximate (R12) |
| A18 | sin θ₂₃ (CKM) | dim K₇/\|PSL(2,7)\| = 7/168 | 0.041667 | 0.04189(+81/−69) | −0.53% | −0.3σ | integer; approximate (R12) |
| A19 | m_H/m_t | fund(E₇)/b₃ = 56/77 | 0.727273 | 0.7250(13) | +0.32% | +1.8σ | integer |
| A20 | m_H/m_W | (N_gen + dim E₆)/dim F₄ = 81/52 | 1.557692 | 1.5571(14) | +0.040% | +0.5σ | integer |
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = 37/42 | 0.880952 | 0.881285(87) | −0.038% | −3.8σ | integer; **proximity** |
| A22 | m_μ/m_τ | (b₂ − D_bulk)/\|PSL(2,7)\| = 10/168 | 0.059524 | 0.0594612(30) | +0.11% | +20.8σ | integer; approximate (R8); **proximity** |
| A23 | Ω_DE | ln 2 · (b₂ + b₃)/H* | 0.686146 | 0.6847(73) | +0.21% | +0.2σ | ln 2; approximate (R11) |
| A24 | n_s | ζ(11)/ζ(5) | 0.964864 | 0.9649(42) | −0.0037% | 0.0σ | ζ values |
| A25 | Ω_DM/Ω_b | (1 + 2b₂)/rank E₈ = 43/8 | 5.375 | 5.364(77) | +0.21% | +0.1σ | integer; approximate (R11) |
| A26 | Ω_c/Ω_Λ | det_num/\|PSL(2,7)\| = 65/168 | 0.386905 | 0.387(14) | +0.10% | 0.0σ | integer; det(g); approximate (R11) |
| A27 | Ω_Λ/Ω_m | (dim G₂ + H*)/dim F₄ = 113/52 | 2.173077 | 2.173(74) | −0.017% | 0.0σ | integer; approximate (R11) |
| A28 | h | (\|PSL(2,7)\| − 1)/dim E₈ = 167/248 | 0.673387 | 0.6736(54) | −0.032% | 0.0σ | integer |
| A29 | Ω_b/Ω_m | Weyl/det_den = 5/32 | 0.15625 | 0.1565(19) | −0.13% | −0.1σ | integer; det(g); approximate (R11) |
| A30 | Ω_c/Ω_m | (det_den − Weyl)/det_den = 27/32 | 0.84375 | 0.8390(19) | +0.56% | +2.5σ | integer; det(g); approximate (R11); **tension** |
| A31 | σ₈ | (p₂ + det_den)/(2b₂) = 34/42 | 0.809524 | 0.8111(60) | −0.19% | −0.3σ | integer; det(g) |
| A32 | Y_p | (1 + dim G₂)/κ_T⁻¹ = 15/61 | 0.245902 | 0.245(3) | +0.37% | +0.3σ | integer; κ_T |
| A33 | Ω_m/Ω_Λ | (1 + dim J₃(𝕆))/κ_T⁻¹ = 28/61 | 0.459016 | 0.461(16) | −0.35% | −0.1σ | integer; κ_T; approximate (R11) |

*Status vocabulary.* **integer**: a ratio of structural integers. **algebraic / φ / ln 2 / ζ values**: the formula uses the corresponding additional operation. **det(g)**, **κ_T**: the formula uses the imposed normalization (R2) or the unnamed combination (R3). **pull**: a descriptive deviation, (K₇ − measured)/σ. **tension**: 2 < |pull| ≤ 3, or a deviation whose reading is itself ambiguous (θ₂₃, §4.3). **proximity**: |pull| > 3; the relation is excluded as an exact equality at 3σ and retained as a numerical proximity. Rejection of a relation is decided by the rule of §11, which uses 3σ. **inside the PDG range**: the reference is a range without an uncertainty; no pull is defined. **approximate**: one of several mutually incompatible relations in an overdetermined sector, none of which is selected (leptons, R8, §6.1; CKM, R12, and cosmological densities, R11, §4.2). **unit assignment**: the prediction depends on a unit chosen by the dictionary. For m_b/m_t the comparison is made in the mass scheme declared in R7. \* the Δχ² profile is not Gaussian (§4.3), so the Gaussian pull overstates the tension.

The arithmetic of each relation and the dictionary choices it makes are in S2; the reference data are in S3.

### 4.2 What the table shows

**The breakdown of the 33.** With one convention for all uncertainties (1σ; correlations neglected, except in the Planck density ratios; §4 dataset note), the 33 relations fall into five classes, which are not added into a single score:

| Class | Count | Relations |
|-------|-------|-----------|
| within 2σ | 23 | the remaining relations |
| tension (2σ < \|pull\| ≤ 3σ) | 2 | m_τ/m_e (−2.1σ), Ω_c/Ω_m (+2.5σ) |
| proximity (\|pull\| > 3σ) | 6 | α⁻¹, sin²θ_W (−7.5σ), m_μ/m_e, m_μ/m_τ (+20.8σ), m_b/m_t (−10.2σ, in the declared mass scheme), m_W/m_Z (−3.8σ) |
| inside the PDG range (no uncertainty) | 1 | m_s/m_d |
| non-Gaussian profile | 1 | sin²θ₂₃ (§4.3) |

The counts are generated from the dataset (`k7_v3_6_table_sec4.py --counts`).

- **Proximities and tensions.** Five proximities compare with quantities measured to between 10⁻¹⁰ and a few 10⁻⁴, and their deviations (0.002% for α⁻¹, 0.19% for sin²θ_W, 0.12% for m_μ/m_e, 0.11% for m_μ/m_τ, 0.04% for m_W/m_Z) are several times the experimental uncertainty or more; the sixth, m_b/m_t, lies 1.8% (−10σ) from the ratio in the declared mass scheme (§3.3). Under the general rule of §11, all six are rejected as exact equalities and kept only as numerical proximities, and m_b/m_t is not rescued by reading it in another scheme. For m_W/m_Z the reference is the ratio of the published masses, as for every mass ratio; the W mass measured by CDF II [57] lies further still (−10.6σ). m_τ/m_e and Ω_c/Ω_m lie between 2σ and 3σ: they are in tension, not rejected. sin²θ₂₃ is discussed in §4.3.
- **The 33 relations are not 33 independent tests.** Three sectors are overdetermined, and in each the relations disagree with one another as exact equalities. The four lepton relations bear on two mass ratios (§6.1, R8). The three CKM relations bear on two Wolfenstein parameters, since sin θ₂₃ = Aλ²: with λ = 7/31 and A = 83/99, Aλ² = 4067/95139 = 0.042748, while the relation for sin θ₂₃ gives 1/24 = 0.041667, 2.6% apart (R12). The seven density relations bear on two independent densities, since in flat ΛCDM Ω_b + Ω_c + Ω_Λ = 1 when the neutrino density (Ω_ν h² ≈ 0.0006 in the Planck base model) is neglected (R11); Ω_Λ/Ω_m is 113/52 = 2.1731 by its own relation, 61/28 = 2.1786 by the inverse of the relation for Ω_m/Ω_Λ (the same quantity, written with another formula), and 2.1862 from Ω_DE with flatness; Ω_c/Ω_b is 43/8 = 5.375 by its own relation and 27/5 = 5.400 from the ratio of Ω_c/Ω_m to Ω_b/Ω_m; Ω_c/Ω_Λ is 65/168 = 0.3869 by its own relation and 0.3873 from the product of Ω_c/Ω_m and Ω_m/Ω_Λ. In the CKM and density sectors the disagreements lie mostly below the experimental uncertainties, which is why most of those relations pass individually. The relations of a sector cannot all hold together; some are redundant and some subsets are compatible (for the densities, the relations for Ω_b/Ω_m and Ω_c/Ω_m are equivalent when neutrinos are neglected, with or without flatness, and the largest compatible subsets have three relations: these two and one of those for Ω_DE, Ω_c/Ω_Λ, Ω_Λ/Ω_m, Ω_m/Ω_Λ). None is selected, for the reason given for the leptons. Other dependencies are possible (sin²θ_W in MS-bar and m_W/m_Z are related in the Standard Model through radiative corrections) and a complete audit of the dependencies among the 33 has not been done, so no count of independent quantities is given.
- **Ω_c/Ω_m and the definition of Ω_m.** Planck's Ω_m includes neutrinos (Ω_ν/Ω_m = 0.0045 at Σm_ν = 0.06 eV), so that Ω_b/Ω_m + Ω_c/Ω_m = 0.9955, while 5/32 + 27/32 = 1. The two formulas are therefore not compatible with that definition of total matter, whatever the measurement. With Ω_b + Ω_c in the denominator the pull of Ω_c/Ω_m = 27/32 would be +0.5σ; that is a different quantity, given for information. The class above uses the quantity as Planck defines it.
- **Most of the 23 are tested only weakly.** For quark mass ratios, mixing parameters and cosmological ratios, the experimental uncertainties are at the percent level, and a percent-level agreement is what a rich vocabulary reaches easily (§7).

No mean deviation is quoted for the table: a mean hides the relations outside 2σ, and it measures closeness, which §7 shows is not distinctive.

### 4.3 The neutrino sector: θ₂₃ and the CP phase

**sin²θ₂₃ = 6/11 = 0.545.** NuFIT 6.1 (normal ordering, with atmospheric data) prefers the first octant, sin²θ₂₃ = 0.470 (+0.017/−0.014); a Gaussian reading of these errors would put 6/11 about 4σ away. The Δχ² profile is not Gaussian, however: the fit keeps a second-octant branch, and its 3σ range, 41.27° < θ₂₃ < 49.86° (0.435 < sin²θ₂₃ < 0.584), contains 6/11. The relation is therefore in tension with the preferred octant, and the tension depends on an ambiguity the experiments have not resolved. This is stated here as it stands; it is also the largest source of uncertainty in the Jarlskog invariant below.

**The CP phase.** The structure produces an integer:
$$\dim(K_7) \cdot \dim(G_2) + H^* = 7 \cdot 14 + 99 = 197.$$
To compare an integer with a phase, the dictionary must say in which unit it is read. Read in degrees, the prediction is the phase
$$e^{i\delta_{CP}}, \qquad \delta_{CP} = 2\pi \cdot \frac{197}{360},$$
and the number 360 enters the prediction without coming from the structure. Read in radians, turns or grads, the same integer gives different phases. The prediction is therefore stated as the phase above; the paper records the unit as a dictionary assignment in the residue register (R6), and counts the choice of unit in the look-elsewhere test (§7). A confirmation would show that this assignment agrees with the world, not that the structure requires it.

**The Jarlskog invariant as a derived observable.** The three PMNS relations are ratios with no convention in them: sin²θ₁₂ = 4/13, sin²θ₂₃ = 6/11, sin²θ₁₃ = 11/496. They give
$$J_{\max} = s_{12}c_{12}s_{23}c_{23}s_{13}c_{13}^2 = 0.0335,$$
against 0.0338 at the NuFIT 6.1 central values (0.3088, 0.470, 0.02248). The invariant J = J_max · sin δ_CP inherits the unit assignment through sin δ: with δ read in degrees, sin δ = −0.292 and J = −0.0098; in radians, J = +0.0266; in grads, J = +0.0016. J does not remove the assignment; it hides it. It is reported as a derived observable, with its angular part free of convention and its phase part conditional on R6.

**Experimental status.** NuFIT 6.1 (normal ordering, with atmospheric data) gives δ_CP = 212 (+26/−36)°, with a 3σ range of 125° to 365°; the reading-in-degrees prediction lies inside the 1σ band. NuFIT 6.0 gave 177 ± 20°, and NuFIT 5.2 about 197°. The central value has moved by tens of degrees between releases, driven mainly by the joint T2K–NOvA analysis [26], and the experimental uncertainty (several tens of degrees) remains large. The decision rule is in §11.

### 4.4 Results with and without the imposed normalization

Six relations use det(g) = 65/32 (R2): λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈. Three use κ_T⁻¹ = 61 (R3): α⁻¹, Y_p, Ω_m/Ω_Λ. Without the six det(g) relations, 27 remain, of which 19 lie within 2σ; without the eight relations that use R2 or R3, 25 remain, of which 17 lie within 2σ. Of the relations outside the within-2σ class, only α⁻¹ and Ω_c/Ω_m use R2 or R3. A reader who regards the imposed normalization as an extra parameter should read the framework through the reduced counts.

### 4.5 The other 62 dataset entries: conditional extractions

The dataset of S3 contains 62 further entries, in three types. They are not counted as predictions.

- **Type II (19 entries)** are dimensionful or composite quantities: absolute quark masses, the electroweak scale and boson masses, CKM magnitudes, and further quark-mass ratios. Several are numbers read in a chosen unit (for example m_u = √(dim G₂/3) = 2.16 read in MeV, or m_t = 415² read in MeV); reading a structural number in MeV is a unit assignment of the same kind as reading 197 in degrees, with a far larger space of alternatives (R10). Others are legacy values whose derivation is not documented in the current dataset (B10–B15, B18, B19); they are retained for traceability.
- **Type III (21 entries)** are outputs of mechanisms (Wilson-line eigenvalue splitting, associative-cycle volumes, spectral counts, gauge-bundle conditioning) that consume declared calibration choices (§6.2). They are conditional reconstructions. The four entries of a two-loop supersymmetric running from a grand-unification boundary condition are retired (App. D).
- **Type IV (22 entries)** are structural diagnostics of the construction (Betti numbers, certificates, conditioning numbers) with no experimental counterpart. They are not observables. Three of them are taken from the black-hole-remnant analysis of [42]; one of these depends on the scale identification τ₀ = v_EW.

The 95 entries of the dataset are therefore **33 relations** in the five classes of §4.2, not all independent, and 62 conditional or diagnostic entries, kept in S3 for traceability.

---

## 5. Gauge Sector: Consistency Checks on an Assumed Standard-Model Content

The smooth K₇ supplies no mechanism for non-abelian gauge symmetry or chirality (§2.3). This section checks that the declared integers are compatible with the Standard-Model content when that content is assumed.

### 5.1 Branching chain and generations

The adjoint of E₈ decomposes under E₆ × SU(3) as
$$248 = (78, 1) + (1, 8) + (27, 3) + (\overline{27}, \overline{3}),$$
with 78 + 8 + 81 + 81 = 248. The (27, 3) term carries three copies of the E₆ representation 27, which contains one Standard-Model generation. The factor 3 is the dimension of the fundamental of the SU(3) commutant; matching it to the three observed generations is a consistency check, as is the integer identity of §2.4.

The framework posits π₁(K₇) = {1} (b₁ = 0 constrains only the abelianisation). Wilson-line breaking through π₁ is therefore unavailable, and no other breaking mechanism is specified at the level of this paper (§6.2 records a ℤ₃ lattice action on the K3 fibre used by the lepton mechanisms).

### 5.2 Anomalies

The six gauge anomalies of one Standard-Model generation vanish (SU(3)³, SU(2)³, U(1)³, mixed gravitational–U(1), SU(3)²–U(1), SU(2)²–U(1)). This is a property of the Standard-Model representations, which the framework assumes; it is reproduced in Lean (`TCSGaugeBreaking.lean`) as a check. The Euler characteristic χ(K₇) = 0 holds for any compact odd-dimensional manifold.

### 5.3 Scales

The three gauge-sector relations are read at the scales of their comparison data, declared in the register (R7):

- sin²θ_W = 3/13 and α_s = √2/12 are compared with MS-bar values **at M_Z**;
- α⁻¹ = 137.033 is compared with the Thomson-limit value **at q² = 0**.

The three couplings are not a triplet at a common scale, and the framework uses no renormalization-group running between scales.

### 5.4 An algebraic identity among the framework's couplings

The two relations sin²θ_W = 3/13 and α_s = √2/12, combined with the one-loop beta-function coefficients of the minimal supersymmetric Standard Model, (b₁, b₂, b₃) = (33/5, 1, −3), satisfy the following identity. With the GUT normalization factor 5/3 for hypercharge, sin²θ_W = 3/13 gives α₁⁻¹ = 2α₂⁻¹. The ratio
$$B = \frac{\alpha_1^{-1} - \alpha_2^{-1}}{\alpha_2^{-1} - \alpha_3^{-1}}$$
equals the MSSM value (b₁ − b₂)/(b₂ − b₃) = 7/5 if and only if
$$\alpha_{\rm em}^{-1} = (b_3 + \dim G_2)\sqrt{2} = 91\sqrt{2} = 128.69,$$
and the three inverse couplings are then 42√2, 21√2 and 6√2, in the ratio dim(G₂) : dim(K₇) : p₂ = 14 : 7 : 2.

This is an algebraic identity among the framework's own values. It says nothing about the measured couplings at any scale: the value 128.69 is neither the measured α⁻¹(M_Z) ≈ 127.9 nor the low-energy 137.036. Whether the identity has physical content would require a running between scales, which the framework does not supply (§5.3).

### 5.5 Gauge-kinetic diagnostics

Numerical diagnostics of the certified local metric (eigenvalues of the gauge-kinetic matrix on the 22 harmonic 2-forms of the K3 fibre, conditioning of Gram matrices) are Type III and IV entries of the dataset (S3). They describe the approximate metric; they are not observables.

---

## 6. Lepton Masses

### 6.1 Four relations on two ratios

The charged-lepton sector has two independent mass ratios. The framework assigns four relations to them:

| Relation | K₇ value | Measured | Deviation |
|----------|----------|----------|-----------|
| m_μ/m_e = 27^φ | 207.012 | 206.7682827(46) | +0.118% (≫ 10σ) |
| m_τ/m_e = 3477 | 3477 | 3477.37(18) | −0.011% (−2.1σ) |
| Q_Koide = 2/3 | 0.666667 | 0.6666645(51) | +0.0003% (+0.4σ) |
| m_μ/m_τ = 10/168 | 0.059524 | 0.0594612(30) | +0.11% (+20.8σ) |

Any two of them fix the third and the fourth, and the four are mutually incompatible (the Koide relation itself dates from 1982 [6]): with m_μ/m_e = 27^φ and m_τ/m_e = 3477, the Koide parameter is Q = 0.666546, not 2/3; with 27^φ and Q = 2/3, m_τ/m_e is not 3477. An overdetermined sector whose relations disagree cannot have all of them as exact equalities.

**No primary relation (R8).** None of the four is declared primary. Nothing in the framework's requirements selects one, and selecting one after the values are known would be a choice of dictionary, of the kind §3.3 registers, not a result. The four are therefore stated as approximate relations, each with its deviation above. Two of them are proximities in the sense of §4.2: m_μ/m_e is measured to about 10⁻⁸ and 27^φ lies 0.12% away; 10/168 lies 21σ from m_μ/m_τ. 3477 lies 2.1σ from m_τ/m_e, a tension. 27^φ is also the most expensive of the four, since φ enters only through the McKay correspondence (R9), an additional step that the integer relations do not need.

The lepton sector therefore supplies no relation specific to K₇ that agrees with measurement at its precision. The relation closest to measurement, Q_Koide = 2/3, predates the framework [6], and its value is reached by every invented vocabulary (§7).

**The τ mass as a discriminator.** The relations predict different τ masses from the measured m_e and m_μ: m_τ = 3477 m_e = 1776.74 MeV, and Koide's relation gives 1776.97 MeV. The world average m_τ = 1776.93 ± 0.09 MeV [1] lies 2.1σ from the first; Belle II's measurement, 1777.09 ± 0.08 ± 0.11 MeV [52], lies further. Future τ-mass measurements discriminate between m_τ/m_e = 3477 and Q_Koide = 2/3 under the decision rule (§11). No τ-mass measurement bears on 27^φ, whose test is the measurement of m_μ/m_e already in hand.

### 6.2 Mechanisms (conditional)

Two mechanisms on the approximate local metric reproduce the hierarchy at the percent level: an eigenvalue splitting of a non-adiabatic Wilson-line operator on the K3 fibre, and the exponential of differences of associative 3-cycle volumes [23]. Both consume declared calibration choices: a coupling c = 0.452 and three positions for the first, and an assignment of the three generations to three of the six self-dual cycles among the 57 associative cycles, selected by minimising the deviation from the measured ratios, for the second. Their combination, normalised by α = e^K computed from the Kähler potential of the approximate metric, gives m_τ/m_e = 3485, m_τ/m_μ = 16.69, m_μ/m_e = 208.8, within 1% of measurement.

Because the calibration choices are selected against the measured ratios, these are conditional reconstructions; they are Type III entries of the dataset (§4.5), with their calibration choices listed in S3. The SVD of the fibre Wilson-line operator has numerical rank 2; the count of three generations does not come from it.

---

## 7. Look-Elsewhere

A framework that matches 33 measured values with closed forms in a vocabulary of twenty constants must answer a prior question: how often would the same grammar, with a different vocabulary, have matched them just as well? This section reports two answers. Neither finds the agreements statistically exceptional. What neither can price, survival against data that did not exist when the formulas were written, is taken up in §11.2.

### 7.1 Four null tests on a fixed list

A public protocol for coincidence claims [M] (the "Sieve") applies four null tests to a frozen observable list and grammar [S-frozen]. The first asks whether a relation is isolated in the fixed vocabulary. The second prices the freedom to have chosen the vocabulary, by comparing with invented vocabularies of the same size and budget. The third and fourth shuffle coefficients and targets. The published scorecard for the K₇ relations [M, §4.3] reads:

- Two relations, n_s and m_H/m_W, pass the isolation test on all three of its axes.
- **Neither passes the vocabulary-freedom test**: an invented vocabulary of the same budget matches them as well (for m_H/m_W, 22 of 24 invented vocabularies do).
- Q_Koide is isolated in the fixed vocabulary, but its value 2/3 is reached by every vocabulary; it is a tie, not a survivor.
- Across the nine shallow relations submitted to the vocabulary-freedom test, the invented-vocabulary envelope is beaten 0 times out of 9.

### 7.2 A null in which every competitor searches for its own formulas

A null in which the alternatives are scored with K₇'s own formulas does not let them search. In the preregistered look-elsewhere test reported here (S4), each competitor searches for its own formulas in the same grammar, with the same budget (at most five nodes per expression) and the same windows (2σ on each side of the measured value, asymmetric uncertainties kept asymmetric; for m_s/m_d, the range the PDG gives, which carries no uncertainty). Two families of competitors were used: 4 159 alternative Betti pairs, with H*, κ_T⁻¹ and det(g) re-derived for each and the other constants held at K₇'s values (N_gen = 3 included, although §3.1 writes N_gen = b₂/dim K₇); and 2 000 invented vocabularies drawn by the generator of [M]. The alphabet tested is not literally the register of §3.1: it is the nineteen integers of the version 3.5 Monte Carlo register, in which dim E₇ = 133 and α_sum = 13 are absent and κ_T⁻¹ = 61 is present (S4.2.1). At a fixed budget this matters, since 13 then costs two leaves (8 + 5). A test on the literal register of §3.1 would be a separate computation.

On the current dataset (§4, S3):

- K₇ reaches 31 of the 33 targets. The two targets reached by no vocabulary at this budget are α⁻¹ and m_μ/m_e, both retained as proximities in §4. Of the 31 targets K₇ reaches, 30 are reached by every competitor; the 31st, m_τ/m_e, alone separates the vocabularies. A control with no constant of K₇ reaches 30 of the 33 with the universal leaves of the grammar alone, all but α⁻¹, m_τ/m_e and m_μ/m_e: the score has little discriminating power in this protocol, and it must be kept apart from the published formulas, of which 24 lie inside their windows (the 23 within 2σ of §4, and m_s/m_d inside its PDG range). Seven targets are counted as reached although K₇'s published value lies outside the window (sin²θ_W, m_τ/m_e, m_b/m_t, sin²θ₂₃, m_W/m_Z, m_μ/m_τ, Ω_c/Ω_m): another expression of K₇'s alphabet falls inside it. m_τ/m_e, the one target that separates the vocabularies, is among them: the published 3477 lies at −2.1σ, so the 31st target is reached by the alphabet, not by the published formula.
- **1 085 of the 4 159 alternative Betti pairs reach as many** (P = 0.26, with P = (1 + n)/(1 + N)); **1 015 of the 2 000 invented vocabularies reach as many** (P = 0.51). No competitor reaches more than 31.
- K₇ is not cheaper either: its description cost (408.1 bits) lies inside the range of the competitors (389.2 to 418.7 bits for the Betti pairs, 385.0 to 430.4 for the vocabularies); 1 038 of the Betti pairs and 628 of the vocabularies cost at most as much.

The preregistered verdict takes the larger of the two family p-values, 0.51, against a threshold of 0.01: the look-elsewhere effect is not overcome. With the same grammar, a five-node budget and 2σ windows, the top score therefore does not distinguish K₇ within these reference classes. These counts are descriptive: an observed absence of discrimination in these families and windows. The value 0.51 is not a probability that K₇ is right or wrong; it says that closeness to the measured values is not, by itself, evidence. Not tested: changes of gauge group or holonomy beyond the Betti numbers, observables built from the CP phase other than δ_CP itself (such as J; the test does include the four units in which the integer 197 can be read: degrees, radians, grads, turns), and budgets beyond five nodes; these freedoms belong to the residue register (formula assignment, grammar, unit).

### 7.3 What remains

Three things are left standing by the look-elsewhere tests, and the paper rests on them rather than on closeness:

1. **Rigidity under a fixed dictionary.** Each relation has no continuous parameter. With the dictionary fixed in advance, a single measurement can reject it (§11).
2. **The declared residue.** What was set is written down (§3.3), so that a reader can see where the framework's necessity ends.
3. **Out-of-sample exposure.** The tests above price a search made against today's windows. They cannot price what happens when a window narrows after the register is frozen, which is what §11.2 sets out.

The origin of the vocabulary (E₈, G₂ and the Betti numbers rather than an invented list) is a fact about the constants that no null of this kind can price. It does not show a selection made before the data were known: the grammar was frozen after the formulas had been found (§3.2), and §10 has not justified the Betti pair at the selecting step.

Descriptive diagnostics of the formula set (a random-forest regression of deviation on formula complexity, the singular values of the constant-usage matrix, an "overdetermination ratio", correlation networks) are in S4. They describe the formula set and carry no evidential weight.

---

## 8. Formal Verification

The arithmetic of the framework is formalized in Lean 4 [28] with Mathlib [29] (code: Arithmon/K7-Lean). The formalization certifies the algebraic identities among the declared integers (for example b₂ · 13 = 3 · (b₃ + dim G₂) for sin²θ_W = 3/13), the G₂ three-form and dim 𝔤₂ = 14, the E₈ root system, and the arithmetic of several numerical certificates. It rests on fourteen axioms in addition to the standard Mathlib foundations: four that import results from the literature (`cheeger_inequality`, `literature_package`, `spectral_upper_bound`, `neck_dominates`) and ten interval certificates that import numerical enclosures [ERR, §7.1]; no `sorry` is used.

The formalization verifies the arithmetic identities it states: given the declared integers, a stated closed form evaluates to the stated number. It does not establish internal consistency of the relations taken together (formulas each computed correctly are mutually incompatible in the overdetermined sectors of §4.2), the existence of K₇, the physical interpretation of any relation, or the choice of assignments; a formula that is machine-checked is not thereby the right formula. The 33 statements are collected in `relations_v36_certified`, which depends only on the standard axioms (`propext`, `Classical.choice`, `Quot.sound`); S3.7 gives, for each relation, the declaration, the commit and the form of the statement (exact rational equality for 27; closed forms in ℝ without numerical bounds for α_s, λ_H, Ω_DE and n_s; bounds for 27^φ; the integer 197 for δ_CP).

---

## 9. Existence Status of the Compact K₇

This section gathers in one place every statement about *existence of the compact $K_7$ manifold*.

### 9.1 What an existence proof would need

- **Topological layer (prior to both).** No compact G₂ manifold with Betti numbers (21, 77) is currently constructed; the Joyce–Karigiannis route does not realise the pair (§2.3; S1 §8.4). Both layers below presuppose a manifold with this topology.
- **Datum-level analytic layer.** A *normalised datum* $\mathcal D_0$ is fixed: a base $S^3$, a coassociative fibration $\pi: K_7 \to S^3$ with $N = 77$ round-unlink branch components, a rank-one Picard–Lefschetz monodromy along each meridian, and a collar-affine period section $h$. On $\mathcal D_0$, the companion paper [E] proves a *conditional branched lifting scheme* (a special case of [53, Conjecture 1]) in seven theorems, with constants computed at $\mathcal D_0$ in interval arithmetic. **But $\mathcal D_0$ is not realisable as posed**: a Stokes-type obstruction shows that the single-root global datum admits no period section [ERR, §2]. This layer is therefore conditional on a datum that does not currently exist.
- **Global-analytic layer.** Passing to a smooth compact $K_7$ carrying a genuine torsion-free $G_2$-structure requires, first, a **realisable datum** replacing $\mathcal D_0$, and then, for that datum, three steps that are open problems (the first two are the global hypotheses of [E], the third a separate theorem):
  1. **A hyperkähler K3 fibration with prescribed periods.** A hyperkähler K3-fibration on the topological $K_7$ with rank-one Picard–Lefschetz monodromy along the 77-unlink and a period section $h$ consistent with the datum $(A_2^{\rm collar})$–$(A_5)$. The closest current template is Kovalev's Hopf-link coassociative K3 fibration [13].
  2. **A smooth-topology classification.** Standard Voisin–Kovalev classification data [21] (Dehn–Seidel twist + K3-family gluing) producing the smooth 7-manifold on which the fibration can live.
  3. **An anisotropic three-scale perturbation theorem.** An anisotropic refinement of Joyce's perturbation theorem in the three-scale collapsing geometry (base $\sim 1$, fibre $\sim \varepsilon$, EH core $\sim \varepsilon^2$) that deforms each closed positive $3$-form of $G_2$-type to a torsion-free $G_2$-structure.

### 9.2 What depends on existence

The framework's claims (the 33 relations, the look-elsewhere tests, the Lean 4 ledger) **do not use the existence layers at all**. They rest on the declared topological invariants of a manifold with $(b_2, b_3) = (21, 77)$, on the E₈×E₈ group data, and on the assignments declared in §3. Whether such a compact torsion-free $G_2$ manifold exists is open, and none of the relations depends on its metric.

A smooth compact $K_7$ carrying a globally torsion-free $G_2$-structure would require a realisable datum and, for it, the three steps of §9.1 proved. For the posed datum $\mathcal D_0$, the first is obstructed; the other two are open.

### 9.3 Relation to the companion papers and independent constructions

The Newton–Kantorovich-certified metric of [A] is a local result: it certifies the gluing region that would appear in a twisted-connected-sum construction, subject to that gluing being available. The paper [D] gives the neck ansatz in closed form, with its own certificate. The paper [E] replaces the rectangular twisted-connected-sum hypothesis with a rank-one branched Kovalev–Lefschetz hypothesis; the Crowley–Goette–Nordström invariant statement for a rectangular twisted connected sum [16] is retained as an independent structural constraint. Since the datum of [E] is not realisable as posed, no existence argument for the compact $K_7$ currently holds. The (b₂, b₃) = (21, 77) outlier position in the catalogued literature is a documentary observation, not an obstruction.

---

## 10. Selection Audit of (21, 77)

This section concerns one item of the residue register (R1): why the Betti pair is (21, 77). It is distinct from the question of why these formulas are assigned to these observables (R4), which has no answer at present (§3.2) and which a derivation of (21, 77) would not supply.

### 10.1 Five investigated routes

- **Landscape density.** In the inverse-problem scan over candidate Betti pairs (b₂, b₃), (21, 77) is sub-median: convenient, not special. It is not a distinguished point of a natural density.
- **Chamber structure.** The associated chamber analysis yields one chamber with three gauge orbits off 77; the "77 side" is not a distinguished wall.
- **S₅ propagation.** The propagation S₅ → 77 closes negatively by mechanism: the induced flow on the moduli side does not favour 77 over its neighbours.
- **Higher-hyperkähler distinguishedness.** Across several classifications, the fibre lattice (15, 7, 1) behind b₂ = 21 has distinguishing invariants, including its place as the single named exception of a mirror lemma ([54], Lemma 5.8); 77 has none, under any of the mechanisms specified so far.
- **An independent construction.** The Zhou series [55] produces (b₂, b₃) = 7 · (3, 11) as a reparametrisation rather than an alternative construction; a screening constraint b₂ ≥ 9 used there is refuted by the census.

Each route is closed as an investigation. The selection question itself is not closed.

### 10.2 The open identity

One structural observation survives:
$$b_2 + b_3 = 98 = 7 \cdot 14 = \dim(K_7) \cdot \dim(G_2).$$
It is held as a target, not a theorem. Until a mechanism is exhibited that forces b₂ + b₃ to equal dim(K₇) · dim(G₂) on structural grounds, the identity is a numerical observation, and it is flagged as such.

### 10.3 Status of (21, 77)

Pending such a mechanism, (21, 77) is a **construction-level input**, on the same footing as the G₂-holonomy postulate. It is a discrete pair, fixed before the relations were frozen and consumed rigidly by all of them, but it is chosen, not selected. G₂ holonomy itself is a hypothesis about an unobserved manifold, and the stabilizer chain G₂ ⊃ SU(3) ⊃ SU(2) ⊃ U(1) does not single it out, since Spin(7) contains the same chain.

---

## 11. Decision Rule and Tests to Come

A prediction is a receipt only if three things are fixed in advance: the quantity, the test, and what happens when the measurement fails it. Each relation is a point value, with no band around it, and the rule is written in full.

### 11.1 The rule

The relations are stated as exact equalities with no theoretical uncertainty, and the rule treats them so. It is fixed in version 3.6, applies to the relations as stated in §4 with the dictionary of §3, and has no repair clause: a relation that fails is not rescued by changing its formula, its unit, its scale, or the dataset against which it is compared, and no theoretical tolerance is added afterwards.

**Reference series.** The classes of §4.2 are computed uniformly with the reference series of S3 (PDG, NuFIT, Planck, CODATA) and their conventions. A new edition of a series, or a new analysis from the same collaboration on the same data class, replaces the current one when it is published, and all relations of that series are then recomputed at once. Replacing a series by another source must be declared, and applied to every relation that uses it.

**General rule.** A relation is rejected as an exact equality when its reference series excludes its value at 3σ, using that series' own confidence interval (for a non-Gaussian likelihood, its published 3σ interval). After rejection it may be kept only as a numerical proximity, with no predictive claim. The six proximities of §4.2 are already rejected in this sense.

| # | Quantity | K₇ value | Rejection condition | What is rejected |
|---|----------|----------|---------------------|------------------|
| D1 | the phase e^{iδ_CP}, δ_CP = 2π·197/360 | 197° | a global fit of the reference series, including DUNE or Hyper-Kamiokande, whose 3σ interval excludes 197° | the δ_CP relation **and** the unit assignment R6 that produced it |
| D2 | sin²θ₂₃ (PMNS) | 6/11 = 0.5455 | a global fit of the reference series whose 3σ interval excludes 6/11, in either octant | the θ₂₃ relation |
| D3 | m_τ/m_e and Q_Koide (approximate, R8) | 1776.74 MeV and 1776.97 MeV for m_τ | a value of m_τ in the reference series whose 3σ interval excludes the value | each excluded relation, separately |
| D4 | N_gen | 3 | a fourth sequential generation | the integer identity of §2.4 as a consistency check |
| D5 | m_s/m_d | 20 | a lattice determination adopted by the reference series, with an uncertainty whose 3σ interval excludes 20 (the current PDG range carries none) | the m_s/m_d relation |

**Measurements outside the reference series.** A contradicting result outside the series does not change a class, and it is never left out: it is reported beside the class. Two stand today. h = 167/248 agrees with the Planck reference (0.0σ) and is excluded by the SH0ES distance ladder [4] at 5.5σ. The density relations agree with the Planck reference and are strained by the baryon acoustic oscillations of DESI [61]: in flat ΛCDM, DESI alone gives Ω_m = 0.2975 ± 0.0086, which puts Ω_Λ/Ω_m = 113/52 at −1.9σ, Ω_m/Ω_Λ = 28/61 at +2.0σ and Ω_DE at −1.9σ; DESI combined with the cosmic microwave background gives Ω_m = 0.3027 ± 0.0036 and H₀ = 68.17 ± 0.28 km s⁻¹ Mpc⁻¹, which puts the same three relations at −3.3σ, +3.4σ and −3.1σ, and h at −3.0σ (neutrino density neglected in the ratios). If the reference series moves to such a result, the relation is rejected. While methods keep disagreeing, the status is stated both ways, and neither agreement counts as a confirmation.

**When this wording was fixed.** The reference-series wording was fixed in version 3.6 with today's results already known (under "a measurement, or a global fit", SH0ES alone would reject h). It is therefore not a choice of arbiter made before seeing the results; it is frozen prospectively from version 3.6.

**What survival does not do.** Rejecting incompatible relations separately is legitimate. A relation that survives in an overdetermined sector (leptons, CKM, densities) is not thereby a prediction selected by the geometry, nor a global confirmation: the selection that left it standing has to be counted. For the τ mass, for instance, the Koide relation and m_τ/m_e = 3477 differ by 0.23 MeV, so a measurement with σ below 0.04 MeV must reject at least one of them.

**What a rejection does not do.** A rejection of the δ_CP relation rejects the stated prediction together with the dictionary assignment that produced it; it does not by itself reject the programme, whose other relations stand or fall on their own. This is fixed now, so that it cannot be introduced later as a repair.

**What a confirmation would show.** A measurement of δ_CP whose 3σ interval contains 197° would show that the assignment "read 197 in degrees" agrees with the world at that precision. It would not show that the structure requires that reading, which is why R6 stays in the residue register in either case.

### 11.2 Out-of-sample tests and timeline

Each of the 33 formulas was written down with the measured value already known, and §7 shows that reaching today's windows is cheap. What a search cannot buy is agreement with a measurement made afterwards. The register is frozen with this version: a formula that was retained because it fell in a window of half-width w, and that carries no information about the true value, falls in a later window of half-width w/k with probability about 1/k (for a new window that lies inside the old one). Each narrowing is therefore a test with a stated chance cost, which the look-elsewhere test of §7 could not supply, and several arrive within the decade.

**sin²θ₁₂ at JUNO.** The relation is 4/13 = 0.3077. The present global fit gives 0.3088 (+0.0067/−0.0066). JUNO's first measurement, from 59.1 days of data, is 0.3092 ± 0.0087 [58], at −0.2σ from 4/13; its projected precision after six years is about 0.5%, or ±0.0016 [59]. That is about four times tighter than the present window: a formula that sat in today's window by chance has roughly one chance in four of remaining within 2σ. This test comes before DUNE, and under the general rule a 3σ exclusion of 4/13 rejects the relation.

| Experiment | Quantity | K₇ value | Timeline |
|------------|---------------------|----------|----------|
| JUNO | sin²θ₁₂ | 4/13 | first result published [58]; about 0.5% after six years of data [59] |
| DUNE Phase I | δ_CP | 2π·197/360 | after first beam (targeted 2031 [47]); resolution depends on exposure and true parameters [30, 31] |
| DUNE Phase II, Hyper-Kamiokande | δ_CP, octant of θ₂₃ | 197°; 6/11 | late 2030s–2040s |
| Belle II, BES III | m_τ | 1776.97 MeV (Koide); 1776.74 MeV (3477 m_e) | ongoing [52] |
| Lattice QCD | m_s/m_d | 20 | the PDG gives the range 17–22, with no uncertainty (§4.1); the rule needs a determination with one |
| DESI, Euclid, Simons Observatory | the density ratios, σ₈, n_s, h | §4.1 | DESI's second data release already strains the density relations (§11.1); further releases through the decade. They enter the classes when the reference series adopts them |

The seven cosmological density relations are the most exposed: they bear on two independent densities (§4.2), so tighter densities must reject some of them, and the rule rejects them separately (§11.1).

---

## 12. Discussion and Conclusion: Where the Necessity of K₇ Ends

### 12.1 What the framework is

The framework is a correspondence between invariants of (K₇, E₈×E₈) and 33 dimensionless parameters, stated with its dictionary, its residue and a decision rule. It is a privileged candidate in the sense of §3.5: its requirements are motivated independently of the Standard Model's values, but they do not select the Betti pair, the formulas or the normalization, and the author's choices are where those enter.

### 12.2 Where its necessity ends

Necessity ends somewhere in every framework, and saying where is part of stating it [WNE]. For K₇ it ends in three places.

- **At the requirements.** G₂ holonomy, compactness and the E₈ data are posited, not derived. They are well motivated, and they answer the question of whether the family deserves exploration; they do not answer why this member.
- **At the residue.** The Betti pair (21, 77), the normalization det(g) = 65/32 and the combination κ_T⁻¹ = 61 are set, not forced, and in the three overdetermined sectors (four lepton relations, three CKM relations, seven density relations) none of the incompatible relations is selected (§3.3). §10 closes five routes to deriving (21, 77) and leaves one identity open.
- **At the dictionary.** No rule assigns formulas to observables, and two assignments carry units or scales that the structure does not supply: the degrees in which 197 is read, and the scales at which the couplings are compared. A confirmation of a relation would confirm the assignment, not a requirement of the structure.

### 12.3 Relation to M-theory and to other proposals

E₈×E₈ and G₂ holonomy both appear in M-theory: E₈×E₈ on the boundaries of heterotic M-theory [32], G₂ holonomy as the condition for N = 1 supersymmetry in a compactification on a seven-manifold [24, 34]. The framework does not supply a compactification of either kind. It differs from standard M-theory phenomenology [33, 35], which works with moduli stabilization and specific singular compactifications. Its smooth K₇ does not yield the chiral non-abelian content of the Standard Model (§2.3), and its relations are not derived from a four-dimensional effective theory.

Lisi's E₈ proposal attempted to place all Standard-Model fermions, chirality included, in a single E₈ representation, and Distler and Garibaldi showed that no such embedding exists [36]. The framework does not attempt that embedding: it uses E₈ as a source of group-theoretic integers. This avoids the obstruction, and leaves open how the fermions arise.

### 12.4 Limitations and open questions

| Issue | Status | Section |
|-------|--------|---------|
| Existence of a compact torsion-free G₂ manifold with (21, 77) | open; requires a realisable datum, then the three steps of §9.1 | §9 |
| Chiral non-abelian gauge sector from K₇ | not supplied; requires a UV bridge (singular locus, heterotic bundle or duality) | §2.3 |
| Selection of (21, 77) | five routes closed; one identity open | §10 |
| Formula assignment rule | absent | §3.2 |
| det(g) = 65/32 | imposed | §3.3 |
| Unit of δ_CP | assigned | §4.3 |
| Relations outside the within-2σ class | proximities (rejected as exact equalities), tensions, a range, an octant | §4.2 |
| Overdetermined sectors (leptons, CKM, cosmological densities) | relations mutually incompatible as exact equalities; none selected; dependency audit not complete | §4.2, §6.1 |
| Look-elsewhere | closeness not distinctive in the tested reference classes | §7 |
| Quantum-gravity completion | not addressed | n/a |

### 12.5 Conclusion

This paper states a correspondence and the terms on which it can fail. Thirty-three dimensionless parameters are matched by closed forms in the invariants of a G₂-holonomy seven-manifold with Betti numbers (21, 77) and of E₈×E₈. Twenty-three lie within two standard deviations of current measurements; six are excluded as exact equalities and kept as proximities; the others are in tension or depend on a range or an unresolved octant. The Betti pair, the formulas, a metric normalization and a unit are set, and are written down as such. A test in which competing vocabularies search for their own formulas shows that closeness to today's values does not distinguish the framework.

The register is now frozen, and what follows is measurement. JUNO narrows sin²θ₁₂ fourfold against 4/13; DUNE and Hyper-Kamiokande measure the leptonic CP phase against 2π·197/360 and resolve the octant against 6/11; the τ mass separates 3477 from Koide's 2/3; tighter cosmological densities must reject some of seven relations that cannot all hold. Each of these can reject a relation together with its assignment, under a rule with no repair clause, and none of them was available to the search that found the formulas. The framework may be a structural insight, an approximation to one, or a coincidence; the measurements of the coming decade are how one finds out.

---

## Author's note

This framework was developed through sustained collaboration between the author and several AI systems, primarily Claude (Anthropic), with substantial contributions from GPT and Codex (OpenAI), whose independent audit passes, certificate engineering, and adversarial review rounds shaped this version and the companion paper [E], and with contributions from Gemini (Google), Grok (xAI), Kimi (Moonshot AI), DeepSeek, and GLM (Zhipu AI) for specific mathematical insights and review passes. The formal verification in Lean 4, architectural decisions, and many key derivations emerged from iterative dialogue sessions over several months; AI-derived mathematical content is either machine-verified (Lean 4, interval arithmetic) or cross-checked against primary sources. This collaboration follows a transparent crediting approach for AI-assisted research, consistent with publisher AI policies [38]. Mathematical constants underlying these relationships represent timeless logical structures that preceded human discovery. The value of any theoretical proposal depends on mathematical coherence and empirical accuracy, not origin. Mathematics is evaluated on results, not résumés.

---

## Competing Interests

The author declares no competing interests.

---

## References

*The bibliography is shared across the main paper and Supplements S1-S4; entries cited only in a supplement are marked accordingly.*

[1] Particle Data Group, F. Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026)
[2] S. Weinberg, Phys. Rev. D 13, 974 (1976)
[3] Planck Collaboration, A&A 641, A6 (2020); chains: Planck Legacy Archive, COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00
[4] A.G. Riess et al., ApJL 934, L7 (2022)
[5] C.D. Froggatt, H.B. Nielsen, Nucl. Phys. B 147, 277 (1979)
[6] Y. Koide, Lett. Nuovo Cim. 34, 201 (1982)
[7] C. Furey, *Standard Model Physics from an Algebra?*, PhD thesis, U. Waterloo (2015)
[8] C. Furey, M.J. Hughes, Phys. Lett. B 831, 137186 (2022)
[9] R. Wilson, arXiv:2404.18938 (2024)
[10] T.P. Singh et al., arXiv:2206.06911v3 (2024)
[11] B.S. Acharya, S. Gukov, Phys. Rep. 392, 121 (2004)
[12] L. Foscolo et al., Duke Math. J. 170, 3 (2021)
[13] A. Kovalev, "Coassociative K3 fibrations of compact G₂-manifolds," arXiv:math/0511150 (2005)
[14] M. Haskins, J. Nordstrom, arXiv:1809.09083 (2022)
[15] G. Bera, "Associative submanifolds in twisted connected sum G₂-manifolds," arXiv:2209.00156 (2022)
[16] D. Crowley, S. Goette, J. Nordstrom, Invent. Math. (2025)
[17] T. Dray, C.A. Manogue, *The Geometry of the Octonions*, World Scientific (2015)
[18] J.F. Adams, *Lectures on Exceptional Lie Groups*, U. Chicago Press (1996)
[19] D.J. Gross et al., Nucl. Phys. B 256, 253 (1985)
[20] D.D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford U. Press (2000)
[21] A. Kovalev, J. Reine Angew. Math. 565, 125 (2003)
[22] A. Corti et al., Duke Math. J. 164, 1971 (2015)
[23] R. Harvey, H.B. Lawson, Acta Math. 148, 47 (1982)
[24] B.S. Acharya, Class. Quant. Grav. 19, 5619 (2002)
[25] B.S. Acharya, E. Witten, arXiv:hep-th/0109152 (2001)
[26] The NOvA Collaboration, The T2K Collaboration, "Joint neutrino oscillation analysis from the T2K and NOvA experiments," Nature 646, 818-824 (2025), doi:10.1038/s41586-025-09599-3, arXiv:2510.19888
[27] I. Esteban, M.C. Gonzalez-Garcia, M. Maltoni, I. Martinez-Soler, J.P. Pinheiro, T. Schwetz, "NuFit-6.0: updated global analysis of three-flavor neutrino oscillations," JHEP 12 (2024) 216, arXiv:2410.05380; NuFIT 6.1: three-neutrino fit based on data available in November 2025, www.nu-fit.org
[28] L. de Moura, S. Ullrich, CADE 28, 625 (2021)
[29] mathlib Community, github.com/leanprover-community/mathlib4
[30] DUNE Collaboration, FERMILAB-TM-2696 (2020)
[31] DUNE Collaboration, arXiv:2103.04797 (2021)
[32] E. Witten, "Strong coupling expansion of Calabi-Yau compactification," Nucl. Phys. B 471, 135 (1996)
[33] B.S. Acharya et al., Phys. Rev. D 76, 126010 (2007)
[34] M. Atiyah, E. Witten, Adv. Theor. Math. Phys. 6, 1 (2002)
[35] G. Kane, *String Theory and the Real World* (2017)
[36] J. Distler, S. Garibaldi, Commun. Math. Phys. 298, 419 (2010)
[37] J.C. Baez, "Octonions and the Standard Model," math.ucr.edu/home/baez/standard/ (2020-2025)
[38] Springer Nature, "Artificial intelligence (AI) policy," www.springernature.com/gp/policies (2024)

[39] J.A. Wheeler, "Information, physics, quantum: the search for links," in *Complexity, Entropy, and the Physics of Information* (W.H. Zurek, ed.), Addison-Wesley (1990), pp. 3–28.

[40] J. Worrall, "Structural realism: the best of both worlds?," *Dialectica* **43**, 99–124 (1989).

[41] J. Ladyman, D. Ross, *Every Thing Must Go: Metaphysics Naturalized*, Oxford University Press (2007).

[42] R. Pinčák, A. Pigazzini, M. Pudlák, E. Bartoš, "Geometric origin of a stable black hole remnant from torsion in G₂-manifold geometry," Gen. Rel. Grav. **58**, 29 (2026), doi:10.1007/s10714-026-03528-z

[43] D. Joyce, S. Karigiannis, "A new construction of compact torsion-free G₂-manifolds by gluing families of Eguchi-Hanson spaces," *J. Differential Geom.* (2021), arXiv:1707.09325 (2017).

[44] S. Mukai, "Finite groups of automorphisms of K3 surfaces and the Mathieu group," *Invent. Math.* **94**, 183–221 (1988).

[45] A. Garbagnati, A. Sarti, "Symplectic automorphisms of prime order on K3 surfaces," *J. Algebra* **318**, 323–350 (2007), arXiv:math/0603742.

[46] LEP2 SUSY Working Group (ALEPH, DELPHI, L3, OPAL), "Combined LEP chargino results, up to 208 GeV for large m0," note LEPSUSYWG/01-03.1 (2001), lepsusy.web.cern.ch.

[47] Fermilab News, "Fermilab marks major milestone for world-leading DUNE experiment," 7 May 2026, news.fnal.gov.

[48] J. Chen, H. Hong, "Intermediate curvature and splitting theorem," arXiv:2604.26529 (2026). (Cited in Supplement S1, §8.4.)

[49] M. Tristram et al., "Cosmological parameters derived from the final Planck data release (PR4)," A&A 682, A37 (2024). (Cited in Supplement S3; not used in the dataset.)

[50] E. Tiesinga, P.J. Mohr, D.B. Newell, B.N. Taylor, "CODATA recommended values of the fundamental physical constants: 2022," Rev. Mod. Phys. 97, 025002 (2025). (Cited in Supplement S3.)

[51] V. V. Nikulin, "Integer symmetric bilinear forms and some of their geometric applications," Izv. Akad. Nauk SSSR Ser. Mat. 43 (1979); English transl. Math. USSR Izv. 14 (1980).

[52] Belle II Collaboration, "Measurement of the τ-lepton mass with the Belle II experiment," Phys. Rev. D 108, 032006 (2023), doi:10.1103/PhysRevD.108.032006, arXiv:2305.19116.

[53] S. K. Donaldson, "Adiabatic limits of co-associative Kovalev–Lefschetz fibrations," in Algebra, Geometry, and Physics in the 21st Century, Progr. Math. 324, Birkhäuser (2017), pp. 1–29, arXiv:1603.08391.

[54] C. Camere, "Lattice polarized irreducible holomorphic symplectic manifolds," Ann. Inst. Fourier 66 (2016), 687–709, arXiv:1312.3224.

[55] C. Zhou, Z. Zhou, "Algebraic Stability and Cosmological Structure E: The Arithmetic Necessity of Three Generations of Fermions," Zenodo, doi:10.5281/zenodo.18626667 (2026).

[56] Particle Data Group, S. Navas et al., "Review of Particle Physics," Phys. Rev. D 110, 030001 (2024), doi:10.1103/PhysRevD.110.030001 (cited in S3 only)

[57] CDF Collaboration, T. Aaltonen et al., "High-precision measurement of the W boson mass with the CDF II detector," Science 376, 170 (2022), doi:10.1126/science.abk1781

[58] JUNO Collaboration, "First measurement of reactor neutrino oscillations at JUNO," arXiv:2511.14593 (2025).

[59] JUNO Collaboration, "Sub-percent precision measurement of neutrino oscillation parameters with JUNO," Chin. Phys. C 46, 123001 (2022), arXiv:2204.13249.

[60] D. Buttazzo, G. Degrassi, P.P. Giardino, G.F. Giudice, F. Sala, A. Salvio, A. Strumia, "Investigating the near-criticality of the Higgs boson," JHEP 12 (2013) 089, arXiv:1307.3536.

[61] DESI Collaboration, M. Abdul Karim et al., "DESI DR2 results. II. Measurements of baryon acoustic oscillations and cosmological constraints," Phys. Rev. D 112, 083515 (2025), arXiv:2503.14738.

---

## Author's Related Works

*Code and Lean proofs:* [github.com/Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) (formerly `gift-framework/core`).

- **[A]** B. de La Fournière, "A Certified Torsion-Free G₂ Structure on a TCS Neck Model via Computer-Assisted Proof," Zenodo [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069) (2026).
- **[B]** B. de La Fournière, "Spectral Geometry of an Explicit G₂ Metric: Laplacian Spectrum and Harmonic Forms," Zenodo [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) (2026).
- **[C]** B. de La Fournière, "Newton–Kantorovich diagnostics on a Donaldson K3 metric: two β estimates, machine-checked inequalities," Zenodo [10.5281/zenodo.19708915](https://doi.org/10.5281/zenodo.19708915) (2026).
- **[D]** B. de La Fournière, "An Explicit Closed-Form G₂ Ansatz on a K3-Coassociative Neck with Hyperkähler Rotation and Picard-Lefschetz Wirtinger Certificate," Zenodo [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065) (2026).
- **[E]** B. de La Fournière, "A conditional analytic framework for rank-one branched Kovalev–Lefschetz adiabatic limits," Zenodo DOI [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) (2026), main paper 68 pp + supplement 25 pp; dataset and four `mpmath.iv` verification scripts at Zenodo [10.5281/zenodo.21209412](https://doi.org/10.5281/zenodo.21209412) (CC BY 4.0). Conditional theorems for a $K_7 \to S^3$ construction with $N = 77$ round-unlink branch components; the single-root datum $\mathcal D_0$ at which its constants are computed is not realisable as posed (§9).
- **[M]** B. de La Fournière, "A reproducible standard for arithmetic coincidence claims in fundamental physics," Zenodo [10.5281/zenodo.20728964](https://doi.org/10.5281/zenodo.20728964) (2026). The Sieve protocol and the scorecard of its four null tests for the K₇ relations.
- **[ERR]** B. de La Fournière, "Erratum: GIFT / K₇ framework v3.5" (2026), repository Arithmon/K7, `publications/ERRATUM_v3.5.md`, commit aed460315eecc17a20402b1f4d20ac310dd4f6c2, [github.com/Arithmon/K7/blob/aed4603/publications/ERRATUM_v3.5.md](https://github.com/Arithmon/K7/blob/aed460315eecc17a20402b1f4d20ac310dd4f6c2/publications/ERRATUM_v3.5.md).
- **[S-frozen]** B. de La Fournière, "Counting Coincidences: frozen inputs" (observable list and expression grammars), Zenodo dataset [10.5281/zenodo.20666878](https://doi.org/10.5281/zenodo.20666878), v1.0 of 12 June 2026.
- **[K3A]** B. de La Fournière, "Certified Analytic Geometry on an Explicit K3 Surface," Zenodo [10.5281/zenodo.22047469](https://doi.org/10.5281/zenodo.22047469) (2026). A certified holomorphic atlas of an explicit K3 surface; no metric claim.
- **[WNE]** B. de La Fournière, "Where Necessity Ends: Selection by Joint Compatibility," preprint, PhilArchive (2026), [philpapers.org/rec/DELWNE](https://philpapers.org/rec/DELWNE). Selection by the joint compatibility of independently motivated requirements, the obligations it carries (independence, a fixed dictionary, a declared residue, refutation with no repair clause), and the three states of §3.5; its §13 audits version 3.5 of this framework.
- **[essay]** B. de La Fournière, *Orientation, not ontology* (companion essay), <https://arithmon.substack.com/p/orientation-not-ontology> (2026).

*This is the founding-framework paper of the [Arithmon program](https://arithmon.com); the methodology of §7 is [M].*

## Appendix A: Primitive Constants

| Symbol | Definition | Value |
|--------|------------|-------|
| dim(E₈) | Lie algebra dimension | 248 |
| rank(E₈) | Cartan subalgebra dimension | 8 |
| dim(K₇) | Manifold dimension | 7 |
| b₂(K₇) | Second Betti number (posited) | 21 |
| b₃(K₇) | Third Betti number (posited) | 77 |
| dim(G₂) | Holonomy group dimension | 14 |
| dim(J₃(𝕆)) | Exceptional Jordan algebra dimension | 27 |

The complete set of twenty structural constants, with their status, is in §3.1.

## Appendix B: Combinations and Imposed Values

| Symbol | Formula | Value | Status |
|--------|---------|-------|--------|
| p₂ | dim(G₂)/dim(K₇) (binary ratio; not a Pontryagin class) | 2 | combination |
| Weyl | factor of \|W(E₈)\| | 5 | combination |
| N_gen | b₂/dim(K₇); integer identity of §2.4 | 3 | measured, reproduced |
| H* | b₂ + b₃ + 1 | 99 | combination |
| τ | (496 × 21)/(27 × 99) | 3472/891 | combination (used by Type II entries only) |
| κ_T⁻¹ | b₃ − dim(G₂) − p₂ | 61 | combination without physical name (R3) |
| det(g) | p₂ + 1/(b₂ + dim(G₂) − N_gen) | 65/32 | **imposed** normalization (R2); the formula is an expression, not a derivation |

## Appendix C: Supplement Reference

| Supplement | Content |
|------------|---------|
| S1: Foundations | E₈, G₂, K₇ construction details |
| S2: The 33 relations | Arithmetic, dictionary choices, alternative formulas, withdrawn readings |
| S3: Observable Dataset | The 95-entry dataset, type classification and status column |
| S4: Sieve and look-elsewhere diagnostics | The scorecard of the four null tests, the look-elsewhere test of §7.2, archived diagnostics of earlier versions |

## Appendix D: Changes since version 3.5

The body of the paper states the present position. This appendix lists, once, what versions up to 3.5 said that version 3.6 no longer says. The corrections of record are in the erratum [ERR] and in the changelog of the repository.

| Earlier statement | Present position | Where |
|-------------------|------------------|-------|
| the relations are "derived" from the geometry; the assignments follow from "metric uniqueness"; the observables are "functionals of the metric" | assignments, with no map from the geometry | §3.2 |
| N_gen = 3 derived, by index theory | integer identity, counted as a consistency check | §2.4 |
| a Joyce–Karigiannis ℤ₂³ route [43] realises (21, 77) topologically | the route does not realise the pair | §2.3, S1 §8.4 |
| κ_T is a torsion scale; p₂ is a Pontryagin class | integer combinations without a physical name | §3.1, R3 |
| a closed-form bound on the K3 fibre metric | the bound concerned an auxiliary quantity | [ERR, §1] |
| "95 observables"; "33 predictions with mean deviation 0.73%"; Type II entries as "a Type I ratio times an experimental anchor" | 33 relations in five classes; 62 entries not counted | §4.2, §4.5 |
| sin²θ_W = 3/13 as a grand-unification boundary condition, run to M_Z at two loops; the supersymmetric spectrum computed from it, including a pure-Bino argument against the LEP chargino bound [46] and the link to G₂-MSSM phenomenology [33]; the identity of §5.4 as holding "at M_Z" | relations read at the scales of their data; no running | §5.3, §5.4 |
| m_H/m_W "the unique survivor" of the Sieve [M], Koide a "survivor" | neither passes the vocabulary-freedom test | §7.1 |
| P < 5 × 10⁻⁶ among 192 349 alternatives (scored with K₇'s own formulas); coincidence exponents 10⁻³⁴⁶, 10⁻¹³³ | preregistered test in which competitors search; global p-value 0.51. On the version 3.5 dataset with one-sided windows the same test had found K₇ at 32 of 33 and every alternative Betti pair at as many (S4.2.3) | §7.2 |
| redundancy counts and descriptive diagnostics as evidence against cherry-picking | measures of the vocabulary's freedom; no evidential weight | §3.2, §7.3 |
| δ_CP = 197° read in degrees without declaring the unit, with a band [182°, 212°] and "serious tension" outside it; a "pure geometry" prediction | point value, unit assignment R6, rule D1 | §4.3, §11 |
| "why G₂ holonomy?" has the status of "why Lorentz invariance?"; G₂ is the unique exceptional holonomy with the chain G₂ ⊃ SU(3) ⊃ SU(2) ⊃ U(1) | Lorentz invariance is empirically established, G₂ holonomy is a hypothesis; Spin(7) contains the same chain | §10.3 |
| rejection by "a measurement, or a global fit" | rejection by the reference series | §11.1 |

---

*The K₇ Framework (formerly GIFT)*
