# The K₇ Framework: Conditional Topological Relations for Standard-Model Parameters from G₂ Holonomy and E₈×E₈ Structure

**Brieuc de La Fourniere**

*Independent researcher, Beaune, France*

---

## Abstract

The Standard Model leaves about nineteen parameters to measurement, and no theory explains its gauge group, its three generations or the values it measures. This paper states a **declared correspondence**. The topological and Lie-theoretic invariants of a compact seven-manifold K₇ with G₂ holonomy and Betti numbers (b₂, b₃) = (21, 77), together with an E₈×E₈ gauge structure, are assigned to dimensionless Standard-Model and cosmological parameters by explicit closed forms. The paper presents the correspondence as a privileged candidate, not as a derivation: no geometric map is known that sends the invariants to the observables, and no rule fixes which formula is assigned to which observable. What the paper does instead is make the correspondence auditable. It gives the full **dictionary** (twenty structural constants and the grammar in which formulas are written). It keeps a **residue register**, ranked with the results, of everything that was set rather than derived: the pair (21, 77), the imposed normalization det(g) = 65/32, the unit in which an integer is read as a CP phase, the scale at which each comparison is made, and the absence of an assignment rule. And it writes a **decision rule** with no repair clause. The core is 33 relations with no continuously adjustable parameter; because two sectors are overdetermined with relations that disagree as exact equalities (four on two lepton mass ratios, seven on two cosmological densities), they bear on 26 independent quantities. Against the most recent data (PDG 2026, NuFIT 6.1, Planck 2018), 25 of these lie within two standard deviations of measurement. Six are proximities, excluded as exact equalities at current precision (α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_τ/m_e, m_W/m_Z); one, m_b/m_t, depends on the mass scheme in which it is compared; and sin²θ₂₃ sits in the second octant while the global fit prefers the first, inside its 3σ range. The remaining 62 entries of the dataset are conditional extractions and diagnostics, and are not counted as predictions. A look-elsewhere test in which every competing Betti pair and invented vocabulary searches for its own formulas reaches 32 of 33 targets as often as K₇ does, so closeness to the measured values is not, by itself, evidence for K₇; the coincidence-probability figures of earlier versions are withdrawn. The sharpest test is the leptonic CP phase: the structure produces the integer 197, the dictionary reads it as the phase 2π·197/360, and a measurement outside [182°, 212°] at 3σ rejects that prediction together with the assignment that produced it. Existence of a compact torsion-free G₂ metric with these Betti numbers is open (§9).

**Keywords**: G₂ holonomy, exceptional Lie algebras, Standard Model parameters, selection problem, falsifiability, look-elsewhere effect, formal verification

---

**Framework status at a glance (version 3.6).**

*Formerly presented as the Geometric Information Field Theory (GIFT), versions 1.0–3.4 of this record.*

- **What is proposed.** A correspondence between invariants of (K₇, E₈×E₈) and 33 dimensionless parameters, written in a declared dictionary (§3). It is a privileged candidate, chosen by the author, not a selection that the requirements force (§3.5).
- **What is set rather than derived.** The residue register of §3.3: the Betti pair, det(g) = 65/32, κ_T⁻¹ = 61, the unit of δ_CP, the comparison scales, the formula assignments.
- **What is established.** The algebraic identities among the declared integers, machine-checked in Lean 4 (§8); a Newton–Kantorovich-certified seam metric [A]; a topological route to (21, 77) [43]. These certify internal consistency, not physical content.
- **What is open.** A compact torsion-free G₂ manifold realising K₇ (§9); a physical mechanism from the smooth K₇ to the chiral non-abelian Standard Model (§2.3); the selection of (21, 77) (§10); a rule that assigns formulas to observables (§3.2).
- **What would refute it.** The decision rule of §11.

---

## 1. Introduction

### 1.1 The parameter problem and the selection problem

The Standard Model describes the known interactions with great precision, yet leaves about nineteen parameters to experiment [1]: gauge couplings, Yukawa couplings spanning five orders of magnitude, mixing angles and phases, and the Higgs sector. It does not explain its gauge group or the number of generations, and it leaves open the hierarchy problem [2] and the flavour puzzle [5]; cosmology adds a persistent tension between early- and late-universe determinations of H₀ [3, 4]. General relativity does not derive the dimension of spacetime, and string theory has of the order of 10⁵⁰⁰ vacua with no internal criterion for electing one. The question *why this structure rather than another?* is the shape that explanatory regress takes in fundamental physics, and every framework that proposes structure inherits it.

Two questions are easily run together, and this paper keeps them apart.

1. **Does a family of structures deserve to be explored?** A good answer points to requirements, motivated independently of one another and of the Standard Model's values, that the family might satisfy together.
2. **Why this precise structure, and these precise assignments, rather than their competitors?** A good answer shows that the requirements eliminate the competitors, or make their differences physically indiscernible.

For K₇ the first question has a positive answer, given in §2: the octonions, G₂ holonomy and E₈ are structures whose interest owes nothing to the Standard Model's constants. The second question is **not** answered here. The pair (21, 77) is not derived (§10), and the formulas are assigned rather than forced (§3.2). Earlier versions of this record blurred the two questions, in particular by writing "derive" where the operation is an assignment. Version 3.6 separates them throughout.

### 1.2 What the paper is

The paper states a correspondence, gives the means to audit it, and says what would reject it. It has three parts.

- **The correspondence and its dictionary (§2–§4).** The mathematical inputs; the twenty structural constants and the grammar of formulas; the 33 Type I relations, each with its measured deviation and its status.
- **The audit (§5–§10).** Consistency checks on the gauge and lepton sectors; the look-elsewhere test; the formal verification; the existence status of K₇; the selection audit of (21, 77).
- **The rule (§11).** A decision rule written in advance, with no repair clause.

Throughout, the residue register of §3.3 is given the same rank as the results. A relation is only as rigid as the pair (structure, dictionary) that produces it: when the structure is rigid but the dictionary is free (which integer, which operation, which unit, which scale), the freedom driven out of continuous parameters returns through the discrete assignments. The register is where those assignments are written down.

### 1.3 Paper organization

- **§2** Mathematical inputs: octonions, E₈×E₈, the topological type of K₇, and what the Betti numbers constrain.
- **§3** The correspondence and its dictionary: structural constants, grammar, residue register, claims, and the status of a privileged candidate.
- **§4** The 33 Type I relations, and the conditional status of Types II–IV.
- **§5** Gauge sector: consistency checks on an assumed Standard-Model content.
- **§6** Lepton masses: four incompatible relations, none selected, and the conditional mechanisms.
- **§7** Look-elsewhere: the Sieve reading and the null in which competitors search for their own formulas.
- **§8** Formal verification (method).
- **§9** Existence status of the compact K₇.
- **§10** Selection audit of (21, 77).
- **§11** Decision rule and refutation.
- **§12** Discussion and conclusion: what K₇ does not fix.

Four supplements give technical details: S1 (mathematical foundations), S2 (the arithmetic of the 33 relations and the dictionary choices each makes), S3 (the 95-entry dataset, with a status column), S4 (Sieve and look-elsewhere diagnostics).

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

Octonionic approaches to Standard-Model structure form an independent line of research [7, 8, 10, 37]. A G₂-holonomy seven-manifold is the geometric setting in which this algebra acts on tangent spaces, which is the reason for exploring it here; it is a motivation, not a derivation.

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
- *Topology.* Among the catalogued compact G₂ examples (Joyce's orbifold constructions [20] and the twisted connected sums of Corti–Haskins–Nordström–Pacini [21, 22]), the pair (21, 77) does not appear (see [12, 14, 15] for the construction literature and census), and orthogonal twisted connected sums are excluded by parity (b₂ + b₃ = 98 is even; [22], Lemma 6.7). A Joyce–Karigiannis ℤ₂³ orbifold route [43] produces (21, 77) at the topological and lattice level, through a four-phase computer-assisted audit (a symplectic screen on CI(2,2,2), an anti-symplectic obstruction, the existence of the K3 lattice via [44, 45, 51], and the Betti formula b₂ = 0 + 21, b₃ = 22 + 55). This is a topological count, not a metric.
- *A local metric.* An explicit approximate G₂ metric on a seam region, g = g_seam(s) ⊕ g_{T²} ⊕ g_{K3}(y), with 169 Chebyshev–Cholesky parameters, carries a Newton–Kantorovich certificate (h = 8.95 × 10⁻⁹) for a nearby torsion-free metric within a ball δg/g ≤ 4.86 × 10⁻⁶ [A]. Its spectral analysis is consistent with (b₂, b₃) = (21, 77) [B]. The certificate is local: it does not construct a compact K₇ (§9).
- *A neck ansatz and a conditional analytic scheme.* An explicit closed-form positive G₂ ansatz on a K3-coassociative neck is certified in [D]. The conditional analytic scheme of [E] for a K₇ → S³ construction with 77 branch components is computed at a datum 𝒟₀ that is not realisable as posed (§9).
- *The K3 fibre.* No certified bound on a Ricci-flat metric of the K3 fibre is claimed; the closed-form bound stated in version 3.5 concerns an auxiliary quantity (v3.5 erratum, §1). An explicit K3 surface has a publicly certified holomorphic atlas, with no metric claim [K3A].

**Metric normalization.** The framework imposes det(g) = 65/32 on the metric. This value is a target, not a consequence of the topology: it has suggestive expressions in the structural constants (§3.3), none of which is a derivation. Six of the 33 relations depend on it.

**The physical gap.** In the standard M-theory dictionary, a compactification on a *smooth* G₂ manifold yields b₂ abelian vector multiplets and no chiral fermions; non-abelian gauge symmetry and chirality require codimension-four and codimension-seven singularities [25, 11]. The framework does not supply such singularities, a heterotic gauge bundle, or a duality that would turn its dictionary into a physical mechanism. Its gauge-sector statements (§5) are therefore consistency checks on an assumed Standard-Model content, not a derivation of it.

### 2.4 What the Betti numbers constrain

**Capacities.** In M-theory on a smooth G₂ manifold, b₂ counts abelian vector multiplets and b₃ counts neutral chiral multiplets [11]. The framework reads b₂ = 21 and b₃ = 77 as capacities of the gauge and matter sectors. The non-abelian Standard-Model gauge group does not come from these multiplets.

**An integer identity.** The integers satisfy
$$(\mathrm{rank}(E_8) + N) \cdot b_2 = N \cdot b_3 \quad\Longleftrightarrow\quad (8 + N) \cdot 21 = 77\,N \quad\Longleftrightarrow\quad N = 3.$$
Earlier versions called this a derivation of the number of generations and attributed it to index theory. It is neither. It is an identity among integers, and no index theorem has been exhibited that produces it; N_gen = 3 is a measured input that the identity reproduces. Equivalently, N_gen = b₂ / dim(K₇) = 21/7. The identity is a consistency check of the declared integers against a known fact, and it is counted as such, not as a prediction.

---

## 3. The Correspondence and Its Dictionary

A relation of the framework has the form *observable ≈ closed form in the structural constants*. Whether such a relation is evidence depends on three things that the formula alone does not show: where the constants come from, how much freedom there was in writing the formula, and how the formula was matched to the observable. This section states all three.

### 3.1 The structural constants

All 33 relations are written in twenty structural constants. Seven are primitive; thirteen are derived from them, and the derivation is part of the dictionary.

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
| 20 | det_num | 65 | Weyl × α_sum | combination; enters det(g) |

Two further quantities appear in the relations: κ_T⁻¹ = b₃ − dim(G₂) − p₂ = 61, an integer combination with no established physical meaning (version 3.5 presented it as a torsion scale; that reading is withdrawn), and the golden ratio φ = (1 + √5)/2, which enters one relation through the McKay correspondence E₈ ↔ 2I (S2.1, R9).

The *status* column distinguishes constants that come from the mathematics independently of this framework (Lie data, topological dimension), inputs posited by the framework (b₂, b₃), and *combinations*: integers built from the others by the framework's own choices. A combination is not an independent datum: choosing to name 32 or 61 is part of the dictionary.

### 3.2 The grammar, and the absence of an assignment rule

**The grammar.** Formulas are rational expressions in the structural constants, with a small set of additional operations: square roots, integer powers, the exponent φ, the logarithm ln 2 and ratios of zeta values. This grammar was frozen with the observable list in a public release [S-frozen] on 12 June 2026, *after* the formulas of the framework had been found. Freezing after discovery does not remove the look-elsewhere effect; it only prevents it from growing. §7 measures it.

**No assignment rule.** There is no rule, internal to the framework, that says which formula is assigned to which observable. Each of the 33 relations was found by searching for a closed form in the structural constants close to a measured value, and was then retained. Version 3.4 said so; version 3.5 replaced this admission with statements that the assignments follow from "metric uniqueness" and that the observables are "functionals of the metric". Those statements are withdrawn: the metric enters none of the formulas, and no map from the geometry to the observables is known. The formula assignments are therefore **assignments**, declared in the residue register, and the question of why (21, 77) (§10) is distinct from the question of why these formulas.

Structural redundancy does not repair this. That sin²θ_W = 3/13 can be written in fourteen ways, and Q = 2/3 in twenty, in the structural constants (S2.7) measures the *size of the vocabulary*, not the absence of choice: a richer vocabulary reaches a given value by more routes. Earlier versions cited these counts as evidence against cherry-picking; they are evidence of the freedom §7 prices.

### 3.3 The residue register

The residue is the part of the framework not fixed by its requirements: what was set rather than derived. It is written here with the same prominence as the results, because it indicates where a further requirement would have to bite, or where the framework rests on a choice.

| Item | What is set | Where it acts | Status |
|------|-------------|---------------|--------|
| R1 | (b₂, b₃) = (21, 77) | every relation | input; five derivation routes audited and closed, one open identity (§10) |
| R2 | det(g) = 65/32 | λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈ | **imposed** normalization; not derived from the topology. Results are given with and without these six relations (§4.4) |
| R3 | κ_T⁻¹ = 61 = b₃ − dim(G₂) − p₂ | α⁻¹, Y_p, Ω_m/Ω_Λ | integer combination without a physical name; it also has a second expression in the structural constants that agrees with the first on the whole line b₂ = 21 and differs elsewhere, and the one used is declared here |
| R4 | the formula assigned to each observable | all 33 | no assignment rule (§3.2) |
| R5 | the grammar and vocabulary | all 33 | frozen after discovery; priced in §7 |
| R6 | the unit in which 197 is read | δ_CP | **unit assignment**: the structure gives the integer 197; reading it in degrees makes the prediction the phase 2π·197/360, and the 360 does not come from the structure (§4.3) |
| R7 | the comparison scale and mass scheme | sin²θ_W, α_s (at M_Z); α⁻¹ (at q² = 0); m_b/m_t | declared; the relations are not claimed to hold at a common scale (§5). m_b/m_t compares m_b in MS-bar at m_b with the directly measured m_t: a ratio of masses in two schemes, with no scheme-independent meaning (0.0243 in this reading, about 0.026 with both masses in MS-bar), so its agreement depends on the choice (§4.2) |
| R8 | the choice among the lepton relations | m_μ/m_e, m_τ/m_e, Q_Koide, m_μ/m_τ | four relations on two ratios, mutually incompatible; the framework selects none, and none is declared primary: a selection made after the values are known would be a dictionary choice, not a result (§6.1) |
| R9 | the exponent φ | m_μ/m_e | enters through the McKay correspondence, an additional step not shared by the integer relations |
| R10 | the unit of Type II entries | absolute masses (MeV) | dimensionful numbers read in a chosen unit; not claimed (§4.5) |
| R11 | the choice among the cosmological density relations | Ω_DE, Ω_DM/Ω_b, Ω_c/Ω_Λ, Ω_Λ/Ω_m, Ω_b/Ω_m, Ω_c/Ω_m, Ω_m/Ω_Λ | seven relations on two independent densities (flat ΛCDM), mutually incompatible as exact equalities; Ω_Λ/Ω_m and Ω_m/Ω_Λ are the same quantity with two formulas; none is selected (§4.2) |

### 3.4 What is claimed, and what is not

**Claimed.** Given the declared constants and the declared assignments, the 33 relations hold as algebraic identities (machine-checked, §8), and they lie at the deviations from measurement listed in §4, with the statuses listed there. The decision rule of §11 applies to them.

**Not claimed.**
- That the relations are derived from the geometry of K₇. No map from the geometry to the observables is known.
- That (21, 77), the formulas, or det(g) = 65/32 are forced by any requirement.
- That the relations hold at a common energy scale.
- That closeness to the measured values is, by itself, evidence for K₇. The look-elsewhere test of §7 shows that it is not.
- That a compact torsion-free G₂ manifold with these Betti numbers has been constructed (§9).
- That the Standard Model's chiral non-abelian content follows from the smooth K₇ (§2.3).

### 3.5 Why state a correspondence that is not derived

A correspondence that is not derived can still be worth stating, provided its status is stated with it. Three states are open to a programme that asks why a structure is the one realised:

1. **Demonstrated uniqueness.** The requirements leave one object, or one class whose members are physically equivalent.
2. **Residual family.** The requirements leave several physically distinct candidates, and the programme says what would tell them apart.
3. **Privileged candidate.** The requirements leave a family, and the author designates a member for reasons that are the author's own and are declared as such.

All three are legitimate. What is not legitimate is to present the third as the first. K₇ is in the third state. The requirements that motivate it (G₂ holonomy, compactness, the E₈ data) are justified independently of the Standard Model's values, which answers the first question of §1.1. They do not select (21, 77), the formulas, or the normalization: these are where the author's choice enters, and the register of §3.3 records them.

Two points follow, and they set the posture of the paper.

**Independence must hold where the selection happens.** A requirement such as "G₂ holonomy" has independent warrant: Berger's classification, the octonions and M-theory give reasons to study it that owe nothing to particle physics. But a requirement of the form "G₂ holonomy *together with* this realisation and these assignments" inherits the warrant of G₂ holonomy without that warrant reaching the realisation. Whatever selects (21, 77) and the formulas would need a justification of its own that does not run through the values it produces. None is available yet, and the paper does not pretend otherwise.

**Rigidity exposes a framework; it does not certify it.** The 33 relations have no continuous parameter: an integer ratio cannot be nudged. That makes each relation refutable by a single measurement, provided its dictionary is fixed in advance, which is what §11 does. It does not make the framework true, and it does not show that the structure was earned rather than picked: an exceptional structure is rigid whether it was derived or chosen for the values it gives. Rigidity is used here as a criterion of exposure, not as a guide to truth.

**Posture.** The framework is read as a structural proposal, in the moderate structural-realist sense of Worrall [40] and Ladyman and Ross [41]: structure is asked to carry predictive weight, with no further ontological commitment. Readings in which geometry and information are aspects of one configuration, in the spirit of Wheeler's "it from bit" [39], historically motivated the work; they are neither required nor supported by the relations. A short essay discusses this posture for a general audience [essay].

---

## 4. The 33 Relations

**Dataset.** Experimental values and uncertainties are those of the framework's observable dataset (S3): PDG 2026 for particle data, NuFIT 6.1 for neutrino mixing (normal ordering, with the tabulated Super-Kamiokande and IceCube atmospheric data), Planck 2018 for cosmology (TT,TE,EE+lowE+lensing, one column for all entries), CODATA 2022 for α and m_μ/m_e. Ratios are computed from the published masses or densities, with independent error propagation, an upper bound since the summary tables do not publish covariances; for asymmetric uncertainties the pull uses the side facing the K₇ value. Quark masses and their ratios are MS-bar values at the PDG reference scales; sin²θ_W and α_s are at M_Z in MS-bar; α⁻¹ is the Thomson-limit value at q² = 0. Each comparison therefore carries a (scheme, scale, dataset) tag [1, 3, 27, 50]. The column *pull* is (K₇ − measured)/σ_exp with the experimental uncertainty alone: the framework supplies no theoretical uncertainty.

### 4.1 Table

| ID | Observable | Formula | K₇ value | Measured | Dev. | Pull | Status |
|----|-----------|---------|----------|----------|------|------|--------|
| A01 | sin²θ_W (M_Z) | b₂/(b₃ + dim G₂) = 3/13 | 0.230769 | 0.23122(6) | −0.19% | −7.5σ | integer; **proximity** |
| A02 | α_s(M_Z) | √2/(dim G₂ − p₂) = √2/12 | 0.117851 | 0.1180(9) | −0.13% | −0.2σ | algebraic |
| A03 | λ_H | √(dim G₂ + N_gen)/det_den = √17/32 | 0.128847 | 0.12914(23) | −0.22% | −1.3σ | algebraic; det(g) |
| A04 | α⁻¹(0) | 128 + 9 + det(g)·κ_T | 137.0333 | 137.035999177(21) | −0.0020% | ≫ 10σ | det(g), κ_T; **proximity** |
| A05 | Q_Koide | dim G₂/b₂ = 2/3 | 0.666667 | 0.6666645(51) | +0.0003% | +0.4σ | integer; approximate (R8) |
| A06 | m_τ/m_e | 7 + 10·248 + 10·99 = 3477 | 3477 | 3477.37(18) | −0.011% | −2.1σ | integer; approximate (R8); **proximity** |
| A07 | m_μ/m_e | 27^φ | 207.012 | 206.7682827(46) | +0.12% | ≫ 10σ | φ; approximate (R8); **proximity** |
| A08 | m_s/m_d | p₂² × Weyl = 20 | 20 | 19.5(25) | +2.56% | +0.2σ | integer |
| A09 | m_c/m_s | (dim E₈ − p₂)/b₂ = 246/21 | 11.714 | 11.769(35) | −0.46% | −1.6σ | integer |
| A10 | m_b/m_t | 1/(2b₂) = 1/42 | 0.023810 | 0.024253(51) | −1.83% | −8.6σ | integer; **scheme assignment** (R7) |
| A11 | m_u/m_d | (1 + dim E₆)/\|PSL(2,7)\| = 79/168 | 0.470238 | 0.462(20) | +1.78% | +0.4σ | integer |
| A12 | sin²θ₁₂ (PMNS) | (1 + N_gen)/α_sum = 4/13 | 0.307692 | 0.3088(+67/−66) | −0.36% | −0.2σ | integer |
| A13 | sin²θ₂₃ (PMNS) | (D_bulk − Weyl)/D_bulk = 6/11 | 0.545455 | 0.470(+17/−14) | +16.05% | +4.4σ* | integer; **tension** (octant; inside the NuFIT 3σ range, §4.3) |
| A14 | sin²θ₁₃ (PMNS) | D_bulk/dim(E₈×E₈) = 11/496 | 0.022177 | 0.02248(+55/−59) | −1.35% | −0.5σ | integer |
| A15 | δ_CP | dim K₇ · dim G₂ + H* = 197 | 197 → phase 2π·197/360 | 212 (+26/−36)° | −7.08% | −0.4σ | **unit assignment** (R6) |
| A16 | sin θ₁₂ (CKM) | fund(E₇)/dim E₈ = 56/248 | 0.225806 | 0.22517(68) | +0.28% | +0.9σ | integer |
| A17 | A (Wolfenstein) | (Weyl + dim E₆)/H* = 83/99 | 0.838384 | 0.826(+17/−15) | +1.50% | +0.7σ | integer |
| A18 | sin θ₂₃ (CKM) | dim K₇/\|PSL(2,7)\| = 7/168 | 0.041667 | 0.04189(+81/−69) | −0.53% | −0.3σ | integer |
| A19 | m_H/m_t | fund(E₇)/b₃ = 56/77 | 0.727273 | 0.7250(13) | +0.32% | +1.8σ | integer |
| A20 | m_H/m_W | (N_gen + dim E₆)/dim F₄ = 81/52 | 1.557692 | 1.5571(14) | +0.040% | +0.5σ | integer |
| A21 | m_W/m_Z | (2b₂ − Weyl)/(2b₂) = 37/42 | 0.880952 | 0.88136(15) | −0.046% | −2.7σ | integer; **proximity** |
| A22 | m_μ/m_τ | (b₂ − D_bulk)/\|PSL(2,7)\| = 10/168 | 0.059524 | 0.0594612(30) | +0.11% | +20.8σ | integer; approximate (R8); **proximity** |
| A23 | Ω_DE | ln 2 · (b₂ + b₃)/H* | 0.686146 | 0.6847(73) | +0.21% | +0.2σ | ln 2; approximate (R11) |
| A24 | n_s | ζ(11)/ζ(5) | 0.964864 | 0.9649(42) | −0.0037% | 0.0σ | ζ values |
| A25 | Ω_DM/Ω_b | (1 + 2b₂)/rank E₈ = 43/8 | 5.375 | 5.364(65) | +0.20% | +0.2σ | integer; approximate (R11) |
| A26 | Ω_c/Ω_Λ | det_num/\|PSL(2,7)\| = 65/168 | 0.386905 | 0.3863(84) | +0.17% | +0.1σ | integer; det(g); approximate (R11) |
| A27 | Ω_Λ/Ω_m | (dim G₂ + H*)/dim F₄ = 113/52 | 2.173077 | 2.172(73) | +0.069% | 0.0σ | integer; approximate (R11) |
| A28 | h | (\|PSL(2,7)\| − 1)/dim E₈ = 167/248 | 0.673387 | 0.6736(54) | −0.032% | 0.0σ | integer |
| A29 | Ω_b/Ω_m | Weyl/det_den = 5/32 | 0.15625 | 0.1564(16) | −0.12% | −0.1σ | integer; det(g); approximate (R11) |
| A30 | Ω_c/Ω_m | (det_den − Weyl)/det_den = 27/32 | 0.84375 | 0.839(11) | +0.55% | +0.4σ | integer; det(g); approximate (R11) |
| A31 | σ₈ | (p₂ + det_den)/(2b₂) = 34/42 | 0.809524 | 0.8111(60) | −0.19% | −0.3σ | integer; det(g) |
| A32 | Y_p | (1 + dim G₂)/κ_T⁻¹ = 15/61 | 0.245902 | 0.245(3) | +0.37% | +0.3σ | integer; κ_T |
| A33 | Ω_m/Ω_Λ | (1 + dim J₃(𝕆))/κ_T⁻¹ = 28/61 | 0.459016 | 0.460(16) | −0.32% | −0.1σ | integer; κ_T; approximate (R11) |

*Status vocabulary.* **integer**: a ratio of structural integers. **algebraic / φ / ln 2 / ζ values**: the formula uses the corresponding additional operation. **det(g)**, **κ_T**: the formula uses the imposed normalization (R2) or the unnamed combination (R3). **proximity**: the relation lies outside 2σ of a precise measurement, so it is excluded as an exact equality at current precision and retained as a numerical proximity. **tension**: outside 2σ of a measurement whose interpretation is itself ambiguous (§4.3). **approximate**: one of several mutually incompatible relations in an overdetermined sector, none of which is selected (leptons, R8, §6.1; cosmological densities, R11, §4.2). **unit assignment**: the prediction depends on a unit chosen by the dictionary. **scheme assignment**: the comparison depends on the mass scheme in which the measured value is taken (R7). \* the Δχ² profile is not Gaussian (§4.3), so the Gaussian pull overstates the tension.

The arithmetic of each relation and the dictionary choices it makes are in S2; the reference data are in S3.

### 4.2 What the table shows

- **25 of the 33 relations lie within 2σ** of measurement. The median absolute deviation is 0.21%; the mean is 1.13%, dominated by sin²θ₂₃ (16%) and δ_CP (7.1%).
- **Eight relations are outside 2σ.** Six are proximities. Four of them (α⁻¹, m_μ/m_e, m_μ/m_τ, sin²θ_W) compare with quantities measured to between 10⁻¹⁰ and a few 10⁻⁴, and their deviations (0.002%, 0.12%, 0.11%, 0.19%) are many times the experimental uncertainty; m_τ/m_e (−2.1σ) and m_W/m_Z (−2.7σ) are closer. As exact equalities all six are excluded; they are retained as proximities, and the paper does not claim more for them. m_b/m_t (−8.6σ) is a scheme assignment (R7). sin²θ₂₃ is discussed in §4.3.
- **The 33 relations bear on 26 independent quantities.** Two sectors are overdetermined. The four lepton relations bear on two mass ratios (§6.1, R8). The seven density relations bear on two independent densities, since in flat ΛCDM Ω_b + Ω_c + Ω_Λ = 1 (R11), and they disagree with one another as exact equalities: Ω_Λ/Ω_m is 113/52 = 2.1731 by A27, 61/28 = 2.1786 by the inverse of A33 (the same quantity, written with another formula), and 2.1862 from Ω_DE with flatness; Ω_c/Ω_b is 43/8 = 5.375 by A25 and 27/5 = 5.400 from A30/A29; Ω_c/Ω_Λ is 65/168 = 0.3869 by A26 and 0.3873 from A30 × A33. The disagreements lie below the Planck uncertainties, which is why every one of the seven passes at 2σ, but at most two of the seven can be exact. None is selected, for the reason given for the leptons. (sin²θ_W in MS-bar and m_W/m_Z are also related in the Standard Model, through radiative corrections; the dependence is noted, not counted.)
- **Most of the 25 are tested only weakly.** For quark mass ratios, mixing parameters and cosmological ratios, the experimental uncertainties are at the percent level, and a percent-level agreement is what a rich vocabulary reaches easily (§7).

Earlier versions summarised this table as "33 predictions with mean deviation 0.73%". That summary is withdrawn: the mean was computed against an earlier dataset, it hid the relations outside 2σ, and a mean deviation measures closeness, which §7 shows is not distinctive.

### 4.3 The neutrino sector: θ₂₃ and the CP phase

**sin²θ₂₃ = 6/11 = 0.545.** NuFIT 6.1 (normal ordering, with atmospheric data) prefers the first octant, sin²θ₂₃ = 0.470 (+0.017/−0.014); a Gaussian reading of these errors would put 6/11 about 4σ away. The Δχ² profile is not Gaussian, however: the fit keeps a second-octant branch, and its 3σ range, 41.27° < θ₂₃ < 49.86° (0.435 < sin²θ₂₃ < 0.582), contains 6/11. The relation is therefore in tension with the preferred octant, and the tension depends on an ambiguity the experiments have not resolved. This is stated here as it stands; it is also the largest source of uncertainty in the Jarlskog invariant below.

**The CP phase.** The structure produces an integer:
$$\dim(K_7) \cdot \dim(G_2) + H^* = 7 \cdot 14 + 99 = 197.$$
To compare an integer with a phase, the dictionary must say in which unit it is read. Versions up to 3.5 read 197 as degrees without saying that this was a choice. Read in degrees, the prediction is the phase
$$e^{i\delta_{CP}}, \qquad \delta_{CP} = 2\pi \cdot \frac{197}{360},$$
and the number 360 enters the prediction without coming from the structure. Read in radians, turns or grads, the same integer gives different phases. Version 3.6 therefore states the prediction as the phase above, records the unit as a dictionary assignment in the residue register (R6), and counts the choice of unit in the look-elsewhere test (§7). A confirmation would show that this assignment agrees with the world, not that the structure requires it.

**The Jarlskog invariant as a derived observable.** The three PMNS relations are ratios with no convention in them: sin²θ₁₂ = 4/13, sin²θ₂₃ = 6/11, sin²θ₁₃ = 11/496. They give
$$J_{\max} = s_{12}c_{12}s_{23}c_{23}s_{13}c_{13}^2 = 0.0335,$$
against 0.0338 at the NuFIT 6.1 central values (0.3088, 0.470, 0.02248). The invariant J = J_max · sin δ_CP inherits the unit assignment through sin δ: with δ read in degrees, sin δ = −0.292 and J = −0.0098; in radians, J = +0.0266; in grads, J = +0.0016. J does not remove the assignment; it hides it. It is reported as a derived observable, with its angular part free of convention and its phase part conditional on R6.

**Experimental status.** NuFIT 6.1 (normal ordering, with atmospheric data) gives δ_CP = 212 (+26/−36)°, with a 3σ range of 125° to 365°; the reading-in-degrees prediction lies inside the 1σ band. NuFIT 6.0 gave 177 ± 20°, and NuFIT 5.2 about 197°. The central value has moved by tens of degrees between releases, driven mainly by the joint T2K–NOvA analysis [26], and the experimental uncertainty (several tens of degrees) remains large. The decision rule is in §11.

### 4.4 Results with and without the imposed normalization

Six relations use det(g) = 65/32 (R2): λ_H, α⁻¹, Ω_c/Ω_Λ, Ω_b/Ω_m, Ω_c/Ω_m, σ₈. Three use κ_T⁻¹ = 61 (R3): α⁻¹, Y_p, Ω_m/Ω_Λ. Without the six det(g) relations, 27 remain, of which 20 lie within 2σ; without the eight relations that use R2 or R3, 25 remain, of which 18 lie within 2σ. Of the eight relations outside 2σ, only α⁻¹ uses R2 or R3. A reader who regards the imposed normalization as an extra parameter should read the framework through the reduced counts.

### 4.5 Types II, III and IV: conditional extractions, not predictions

The dataset of S3 contains 62 further entries. Version 3.6 does not count them as predictions.

- **Type II (19 entries)** are dimensionful or composite quantities: absolute quark masses, the electroweak scale and boson masses, CKM magnitudes, and cascades of Type I ratios. Several are numbers read in a chosen unit (for example m_u = √(dim G₂/3) = 2.16 read in MeV, or m_t = 415² read in MeV); reading a structural number in MeV is a unit assignment of the same kind as reading 197 in degrees, with a far larger space of alternatives (R10). Others are Type I ratios multiplied by a measured anchor, and add no information beyond the ratio. Earlier versions described all nineteen as "a Type I ratio times an experimental anchor"; that description does not match the dataset and is withdrawn.
- **Type III (21 entries)** are outputs of mechanisms (Wilson-line eigenvalue splitting, associative-cycle volumes, spectral counts, gauge-bundle conditioning) that consume declared calibration choices (§6.2). They are conditional reconstructions. The four entries of the two-loop supersymmetric running from a grand-unification boundary condition are withdrawn with that reading (§5).
- **Type IV (22 entries)** are structural diagnostics of the construction (Betti numbers, certificates, conditioning numbers) with no experimental counterpart. They are not observables. Three of them are taken from the black-hole-remnant analysis of [42]; one of these depends on the scale identification τ₀ = v_EW.

The count "95 observables" of earlier versions is therefore replaced by: **33 relations**, of which 25 within 2σ, six proximities, one scheme assignment and one octant tension; bearing on 26 independent quantities; and 62 conditional or diagnostic entries, kept in S3 for traceability.

---

## 5. Gauge Sector: Consistency Checks on an Assumed Standard-Model Content

This section does not derive the Standard Model's gauge sector. As §2.3 states, the smooth K₇ supplies no mechanism for non-abelian gauge symmetry or chirality. What the section does is check that the declared integers are compatible with the Standard-Model content when that content is assumed.

### 5.1 Branching chain and generations

The adjoint of E₈ decomposes under E₆ × SU(3) as
$$248 = (78, 1) + (1, 8) + (27, 3) + (\overline{27}, \overline{3}),$$
with 78 + 8 + 81 + 81 = 248. The (27, 3) term carries three copies of the E₆ representation 27, which contains one Standard-Model generation. The factor 3 is the dimension of the fundamental of the SU(3) commutant; matching it to the three observed generations is a consistency check, as is the integer identity of §2.4. Neither is a derivation of N_gen.

The framework posits π₁(K₇) = {1} (b₁ = 0 constrains only the abelianisation). Wilson-line breaking through π₁ is therefore unavailable, and no other breaking mechanism is specified at the level of this paper (§6.2 records a ℤ₃ lattice action on the K3 fibre used by the lepton mechanisms).

### 5.2 Anomalies

The six gauge anomalies of one Standard-Model generation vanish (SU(3)³, SU(2)³, U(1)³, mixed gravitational–U(1), SU(3)²–U(1), SU(2)²–U(1)). This is a property of the Standard-Model representations, which the framework assumes; it is reproduced in Lean (`TCSGaugeBreaking.lean`) as a check, not claimed as a prediction. The Euler characteristic χ(K₇) = 0 holds for any compact odd-dimensional manifold.

### 5.3 Scales

The three gauge-sector relations are read at the scales of their comparison data, declared in R7:

- sin²θ_W = 3/13 and α_s = √2/12 are compared with MS-bar values **at M_Z**;
- α⁻¹ = 137.033 is compared with the Thomson-limit value **at q² = 0**.

The framework does not claim a triplet of couplings at a common scale. Version 3.5 also read sin²θ_W = 3/13 as a grand-unification boundary condition and ran it to M_Z with two-loop supersymmetric renormalization-group equations; the same value was thus labelled at M_Z in the relation and at M_GUT in its proof. That reading is withdrawn in version 3.6, together with the running chain, its threshold treatment and the supersymmetric spectrum computed from it (including the argument that a pure-Bino lightest neutralino escapes the LEP chargino bound [46]).

### 5.4 An algebraic identity among the framework's couplings

The two relations sin²θ_W = 3/13 and α_s = √2/12, combined with the one-loop beta-function coefficients of the minimal supersymmetric Standard Model, (b₁, b₂, b₃) = (33/5, 1, −3), satisfy the following identity. With the GUT normalization factor 5/3 for hypercharge, sin²θ_W = 3/13 gives α₁⁻¹ = 2α₂⁻¹. The ratio
$$B = \frac{\alpha_1^{-1} - \alpha_2^{-1}}{\alpha_2^{-1} - \alpha_3^{-1}}$$
equals the MSSM value (b₁ − b₂)/(b₂ − b₃) = 7/5 if and only if
$$\alpha_{\rm em}^{-1} = (b_3 + \dim G_2)\sqrt{2} = 91\sqrt{2} = 128.69,$$
and the three inverse couplings are then 42√2, 21√2 and 6√2, in the ratio dim(G₂) : dim(K₇) : p₂ = 14 : 7 : 2.

This is an algebraic identity among the framework's own values. It is **not** a statement about the measured couplings at any scale: the value 128.69 is neither the measured α⁻¹(M_Z) ≈ 127.9 nor the low-energy 137.036, and version 3.5's description of it as holding "at M_Z" or at an "exact scale" is withdrawn. Whether the identity has physical content would require the running that §5.3 removes.

### 5.5 Gauge-kinetic diagnostics

Numerical diagnostics of the certified seam metric (eigenvalues of the gauge-kinetic matrix on the 22 harmonic 2-forms of the K3 fibre, conditioning of Gram matrices) are Type III and IV entries of the dataset (S3). They describe the approximate metric; they are not observables.

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

**No primary relation (R8).** Version 3.6 declares none of the four primary. Nothing in the framework's requirements selects one, and selecting one after the values are known would be a choice of dictionary, of the kind §3.3 registers, not a result. The four are therefore stated as approximate relations, each with its deviation above. Three of them are proximities in the same sense as α⁻¹ and sin²θ_W (§4.2): m_μ/m_e is measured to about 10⁻⁸ and 27^φ lies 0.12% away; 10/168 lies 21σ from m_μ/m_τ; 3477 lies 2.1σ from m_τ/m_e. 27^φ is also the most expensive of the four, since φ enters only through the McKay correspondence (R9), an additional step that the integer relations do not need.

The lepton sector therefore supplies no relation specific to K₇ that agrees with measurement at its precision. The relation closest to measurement, Q_Koide = 2/3, predates the framework [6], and its value is reached by every invented vocabulary (§7). This changes the reading of the Sieve analysis: Koide's Q = 2/3 was presented there as a "survivor"; in version 3.6 it is an approximate relation, isolated in the fixed vocabulary but with a value (2/3) that every invented vocabulary reaches.

**The τ mass as a discriminator.** The relations predict different τ masses from the measured m_e and m_μ: m_τ = 3477 m_e = 1776.74 MeV, and Koide's relation gives 1776.97 MeV. The world average m_τ = 1776.93 ± 0.09 MeV [1] lies 2.1σ from the first; Belle II's measurement, 1777.09 ± 0.08 ± 0.11 MeV [52], lies further. Future τ-mass measurements discriminate between m_τ/m_e = 3477 and Q_Koide = 2/3 under rule D3 (§11). No τ-mass measurement bears on 27^φ, whose test is the measurement of m_μ/m_e already in hand.

### 6.2 Mechanisms (Type III, conditional)

Two mechanisms on the approximate seam metric reproduce the hierarchy at the percent level: an eigenvalue splitting of a non-adiabatic Wilson-line operator on the K3 fibre, and the exponential of differences of associative 3-cycle volumes [23]. Both consume declared calibration choices: a coupling c = 0.452 and three positions for the first, and an assignment of the three generations to three of 57 associative cycles, selected by minimising the combined deviation, for the second. Their combination, normalised by α = e^K computed from the Kähler potential of the approximate metric, gives m_τ/m_e = 3485, m_τ/m_μ = 16.69, m_μ/m_e = 208.8, within 1% of measurement.

Because the calibration choices are selected against the measured ratios, these are conditional reconstructions, not predictions; they are Type III entries (§4.5), with their search spaces and selection protocol documented in S3. The SVD of the fibre Wilson-line operator has numerical rank 2; the count of three generations does not come from it.

---

## 7. Look-Elsewhere

A framework that matches 33 measured values with closed forms in a vocabulary of twenty constants must answer a prior question: how often would the same grammar, with a different vocabulary, have matched them just as well? This section reports two answers. Neither supports the claim, made in earlier versions, that the agreements are statistically exceptional.

### 7.1 The Sieve reading

The Sieve [M] is a public battery of four nulls with a frozen observable list and grammar [S-frozen]: N1 asks whether a relation is isolated in the fixed vocabulary; N2 prices the freedom to have chosen the vocabulary, by comparing with budget-matched invented vocabularies; N3 and N4 shuffle coefficients and targets. Its published scorecard for the K₇ relations [M, §4.3] reads:

- Two relations, n_s and m_H/m_W, survive N1 on all three of its axes.
- **Neither clears N2**: once the freedom to choose the vocabulary is priced, a budget-matched invented vocabulary matches them as well (for m_H/m_W, 22 of 24 invented vocabularies do).
- Q_Koide is isolated in the fixed vocabulary, but its value 2/3 is reached by every vocabulary; it is a tie, not a survivor.
- Across the nine shallow relations tested by N2, the invented-vocabulary envelope is beaten 0 times out of 9.

Version 3.5 described m_H/m_W as "the unique survivor" and m_H/m_W and Koide as "sieve-distinguished survivors". Those descriptions omitted the N2 result of the same scorecard and are withdrawn. What N2 cannot price, and what remains load-bearing, is that the K₇ vocabulary (E₈ dimensions and ranks, the Betti numbers) is geometrically pre-specified rather than invented.

### 7.2 A null in which every competitor searches for its own formulas

Version 3.5 reported that, among 192 349 alternative configurations, none outperformed the framework (P < 5 × 10⁻⁶). That figure came from a Monte Carlo in which the alternatives were scored with K₇'s own formulas; it did not let them search. It is withdrawn, together with the coincidence-probability exponents of version 3.4 (10⁻³⁴⁶, 10⁻¹³³), which no longer appear in the main text.

In its place, version 3.6 reports a preregistered look-elsewhere test (S4) in which each competitor searches for its own formulas in the same grammar, with the same budget (at most five nodes per expression) and the same windows (2σ). Two families of competitors were used: 4 159 alternative Betti pairs, with the structural constants re-derived for each; and 2 000 invented vocabularies from the Sieve.

- K₇ reaches 32 of the 33 targets (α⁻¹ is reached by nobody at this budget).
- **All 4 159 alternative Betti pairs reach as many**; 1 635 of the 2 000 invented vocabularies reach as many.
- K₇ is not cheaper either: its description cost (395.6 bits) lies inside the range of the competitors.

With the same grammar, a five-node budget and 2σ windows, the saturated score therefore does not distinguish K₇ within these reference classes. These counts are descriptive. They are an observed absence of discrimination in these families and windows, not a measurement of statistical power, and they are not a physical refutation of K₇. They say that closeness to the measured values is not, by itself, evidence. Not tested: changes of gauge group or holonomy beyond the Betti numbers, other forms of the δ_CP observable, and budgets beyond five nodes; these freedoms belong to the residue register (R4, R5, R6).

### 7.3 What remains

Three things survive the look-elsewhere tests, and the paper rests on them rather than on closeness:

1. **Pre-specification.** The vocabulary comes from E₈, G₂ and the Betti numbers, not from a search over vocabularies. This is a fact about where the constants come from, which no null of the kind above can price; it is also exactly what §10 has not yet justified at the selecting step.
2. **Rigidity under a fixed dictionary.** Each relation has no continuous parameter. With the dictionary fixed in advance, a single measurement can reject it (§11).
3. **The declared residue.** What was set is written down (§3.3), so that a reader can see where the framework's choices enter.

The descriptive diagnostics of earlier versions (a random-forest regression of deviation on formula complexity, the singular values of the constant-usage matrix, the "overdetermination ratio" of 2.13, correlation networks) are kept in S4. They describe the formula set; they are not evidence against cherry-picking, and are no longer presented as such.

---

## 8. Formal Verification

The arithmetic of the framework is formalized in Lean 4 [28] with Mathlib [29] (code: Arithmon/K7-Lean). The formalization certifies the algebraic identities among the declared integers (for example b₂ · 13 = 3 · (b₃ + dim G₂) for sin²θ_W = 3/13), the G₂ three-form and dim 𝔤₂ = 14, the E₈ root system, and the arithmetic of several numerical certificates. It rests on fourteen axioms in addition to the standard Mathlib foundations: four that import results from the literature (`cheeger_inequality`, `literature_package`, `spectral_upper_bound`, `neck_dominates`) and ten interval certificates that import numerical enclosures (v3.5 erratum, §7.1); no `sorry` is used.

What the formalization establishes is internal consistency: given the declared integers and assignments, the stated relations hold. It does not establish the existence of K₇, the physical interpretation of any relation, or the choice of assignments; a formula that is machine-checked is not thereby the right formula. Per-module counts are in S3.

---

## 9. Existence status (two-layer boundary)

This section gathers in one place every claim about *existence of the compact $K_7$ manifold* (in the 3.4 version this language was distributed across §2.3, §5.5, §8.5, §9.3 and §9.4).

### 9.1 The two layers

- **Datum-level analytic layer.** A *normalised datum* $\mathcal D_0$ is fixed: a base $S^3$, a coassociative fibration $\pi: K_7 \to S^3$ with $N = 77$ round-unlink branch components, a rank-one Picard–Lefschetz monodromy along each meridian, and a collar-affine period section $h$. On $\mathcal D_0$, the companion paper [E] proves a *conditional branched lifting scheme* (a special case of [Donaldson 2017, Conjecture 1]) via seven theorem-grade results. Source-side discharge constants ($C_{\rm src} = 27/16$, $C_{\rm nl} = 2/3$, $C_{\rm link} \le 1$, $\gamma = 2$) carry structural provenance; the tail-contraction threshold $R_0(\mathcal D_0) \le 4.9 \cdot 10^3$ is enclosed by outward-rounded interval arithmetic. **But $\mathcal D_0$ is not realisable as posed**: a Stokes-type obstruction (2026-08-19) shows that the single-root global datum admits no period section (v3.5 erratum, §2). This layer is therefore *conditional on a datum that is not currently instantiated*; it is not discharged.
- **Global-analytic layer.** Passing to a smooth compact $K_7$ carrying a genuine torsion-free $G_2$-structure requires, first, a **realisable datum** replacing $\mathcal D_0$, and then closing, for that datum, two external structural slots (jointly the pack $\mathsf H_{\rm global}$ of [E]) and one standalone hypothesis:
  1. **(L4) Hyperkähler K3-fibration with prescribed periods.** A hyperkähler K3-fibration on the topological $K_7$ with rank-one Picard–Lefschetz monodromy along the 77-unlink and a period section $h$ consistent with the datum $(A_2^{\rm collar})$–$(A_5)$. The closest current template is Kovalev's Hopf-link coassociative K3 fibration [13].
  2. **(C.1) Smooth-topology classification.** Standard Voisin–Kovalev classification data [21] (Dehn–Seidel twist + K3-family gluing) producing the smooth 7-manifold on which (L4) can live.
  3. **(J) Anisotropic three-scale perturbation.** An anisotropic refinement of Joyce's perturbation theorem in the three-scale collapsing geometry (base $\sim 1$, fibre $\sim \varepsilon$, EH core $\sim \varepsilon^2$) that deforms each closed positive $3$-form of $G_2$-type to a torsion-free $G_2$-structure. Companion long chantier of [E].

### 9.2 Chain-of-locks and certified constants (headline synthesis from [E])

To make this section standalone (a reader interested only in the framework's headlines should not have to open [E] to gauge the status of the analytic layer), we transport here the four-lock status ledger and the source-side certified constants. Preambles, proofs, and the interval-arithmetic verification scripts remain in [E].

**Datum $\mathcal D_0$.** Base $S^3$; coassociative fibration $\pi: K_7 \to S^3$; branch locus $= N = 77$ round unlink components; rank-one Picard–Lefschetz monodromy along each meridian; collar-affine period section $h$ satisfying gates $(A_2^{\rm collar})$–$(A_5)$; source-side envelopes $K_{F_1} = K_{g_1} = K_v = 2.31$, $D_{\rm max} = 7/5$.

**Chain-of-locks.** At the posed datum, the scheme rests on the following locks:

| Lock | Content | Status | Source-side certificate |
|------|---------|--------|-------------------------|
| **L1.6** | $K_{\rm Sch} \le 16/3$ (Schauder recollement) | CLOSED (theorem-grade) | $q_{\rm coeff} \le 0.168$ headline / $0.110$ sharp, slack 33–56% of $1/4$; independent checker gates O0–O5 all pass |
| **L2 assembly** | Product-Banach reconstruction on $X_{\rm AR} = X_\omega \times X_\lambda \times X_\mu \times X_\Theta$ | CLOSED (theorem-grade) | $q_{\rm total} = q_{\rm AR} + q_{\rm comm} + q_{\rm proj} + q_{\rm hodge} + q_{\rm gauge} \le 8.20 \cdot 10^{-3} < 1/2$, contraction margin $60.9\times$; gates A0–A5 pass |
| **(L4)** | Hyperkähler K3-fibration with prescribed periods, rank-1 PL monodromy along the 77-unlink | **OBSTRUCTED for $\mathcal D_0$** (no period section; v3.5 erratum, §2 and §7.4); open for a future realisable datum | Closest template: Kovalev's Hopf-link coassociative K3 fibration [13] |
| **(C.1)** | Smooth-topology classification (7-manifold on which L4 lives) | OPEN | Voisin–Kovalev classification inputs [21] |
| **(J)** | Anisotropic three-scale perturbation theorem (base $\sim 1$, fibre $\sim \varepsilon$, EH core $\sim \varepsilon^2$) | OPEN | Companion long-term project of [E] |

The two CLOSED locks are theorem-grade computations at the posed datum $\mathcal D_0$, which is now known not to be realisable. The residual analytic content of the global-existence problem is therefore larger than the three slots: it starts with a realisable datum, for which (L4), (C.1) and (J) must then be discharged.

**Source-side certified constants (all with structural provenance).**

| Constant | Value | Provenance |
|----------|-------|------------|
| $C_{\rm src}$ | $27/16$ | Cubique + parity on Donaldson canonical gauge |
| $C_{\rm nl}$ | $2/3$ | Simons identity + collinéarité; strictly below power-counting envelope $\sim 1$ |
| $\gamma$ | $2$ | Proved (spectral order of the rank-1 branched Jacobi) |
| $C_{\rm link}$ | $\le 1$ | Impedance match ($\Lambda_{\rm in}^{\rm model} = -\Lambda_{\rm out}^{\rm model}$) $+$ parity $\vert c_0\vert^2$ $+$ type-IV sectional $\vert K_{\rm sec}\vert \le 1$ |
| $C_{\rm FS}$ | $\approx 0.29$ | Fredholm–Schauder outer coercivity |
| $\kappa_E$ | $\le 1.02$ | KA1 rigidity ($Df_0 = 0$, $\Vert g'\Vert_\infty = 2$, compensation $(1/2) \cdot 2$) |
| $\Vert\mathfrak M^{-1}\Vert$ | $\le 1.246$ | Schur + sector exhaustion at the gate $\Pi_{\rm obs}^{\rm PDE} = \Pi_{\mathbb R^{2N}}$ |
| $K_{\rm Sch}$ | $\le 16/3$ | L1.6 recollement, $(4/3) \cdot 3 \cdot (4/3)$ |
| $q_{\rm total}$ | $\le 8.20 \cdot 10^{-3}$ | L2 assembly (Banach product-max on $X_{\rm AR}$) |
| $R_0(\mathcal D_0)$ | $\le 4.9 \cdot 10^3$ | Newton–Kantorovich tail-contraction threshold; outward-rounded interval arithmetic |

**Operational meaning of $R_0(\mathcal D_0) \le 4.9 \cdot 10^3$.** In the branched adiabatic scheme, $R_0$ is the smallest scale beyond which the Newton–Kantorovich iteration converges uniformly at $\mathcal D_0$. The certified bound $R_0 \le 4.9 \cdot 10^3$ is enclosed by outward-rounded interval arithmetic (mpmath, 60 decimal digits, 4 verification scripts distributed with [E]) and sits $\sim 9\%$ below the power-counting threshold and $\sim 34\%$ below the Codex Stage B recomputation; this headroom is a property of the computation at the posed datum, not of an instantiated one.

*What this section does not claim.* All quantities above are proved conditional on $\mathcal D_0$ being an admissible datum, and $\mathcal D_0$ is not: they are computations, not an instantiated layer. Passing to a smooth compact $K_7$ requires a realisable datum and, for it, (L4), (C.1) and (J) (see §9.3). No proof is reproduced here; [E] is the citable source.

### 9.3 What version 3.6 claims and what it does not

The framework's claims (the 33 relations, the look-elsewhere tests, the Lean 4 ledger) **do not use the existence layers at all**: they do not consume $\mathcal D_0$, $\mathsf H_{\rm global}$ or $(\mathrm J)$. They rest on the declared topological invariants of a manifold with $(b_2, b_3) = (21, 77)$, on the E₈×E₈ group data, and on the assignments declared in §3. Whether such a compact torsion-free $G_2$ manifold exists is open, and none of the relations depends on its metric.

The framework does not claim to have constructed a smooth compact $K_7$ carrying a globally torsion-free $G_2$-structure. That claim would require a realisable datum and, for it, (L4), (C.1) and (J) discharged as theorems. For the posed datum $\mathcal D_0$, (L4) is obstructed; (C.1) and (J) are open.

### 9.4 Relation to earlier drafts and independent constructions

The Chebyshev–Cholesky NK-certified metric of [A] is a *seam-level* result: it certifies the seam that would appear in a TCS-style gluing, subject to that gluing being available. The [D] paper strengthens the neck-level ansatz with an explicit closed-form + five-layer Wirtinger certificate. The [E] paper replaces the TCS-style rectangular hypothesis with a rank-one branched Kovalev–Lefschetz hypothesis; the Crowley–Goette–Nordström invariant statement for a rectangular twisted connected sum [16] (S1) is retained as an independent structural constraint. Since the datum of [E] is not realisable as posed, no existence argument for the compact $K_7$ is currently load-bearing. The (b₂, b₃) = (21, 77) outlier position in the catalogued literature is a documentary observation, not an obstruction.

---

## 10. Selection Audit of (21, 77)

This section concerns one item of the residue register (R1): why the Betti pair is (21, 77). It is distinct from the question of why these formulas are assigned to these observables (R4), which has no answer at present (§3.2) and which a derivation of (21, 77) would not supply.

### 10.1 Five investigated routes

- **Landscape density.** In the census of Picard-lattice-realisable hyperkähler K3 pairs, (21, 77) is sub-median: convenient, not special. It is not a distinguished point of a natural density.
- **Chamber structure.** The associated chamber analysis yields one chamber with three gauge orbits off 77; the "77 side" is not a distinguished wall.
- **S₅ propagation.** The propagation S₅ → 77 closes negatively by mechanism: the induced flow on the moduli side does not favour 77 over its neighbours.
- **Higher-hyperkähler distinguishedness.** Across several classifications, 21 has distinguishing invariants and 77 does not, under any of the mechanisms specified so far; the single exception is an isolated context (Camere, Lemma 5.8).
- **An independent construction.** The Zhou series produces (b₂, b₃) = 7 · (3, 11) as a reparametrisation rather than an alternative construction; a screening constraint b₂ ≥ 9 used there is refuted by the census.

Each route is closed as an investigation. The selection question itself is not closed.

### 10.2 The open identity

One structural observation survives:
$$b_2 + b_3 = 98 = 7 \cdot 14 = \dim(K_7) \cdot \dim(G_2).$$
It is held as a target, not a theorem. Until a mechanism is exhibited that forces b₂ + b₃ to equal dim(K₇) · dim(G₂) on structural grounds, the identity is a numerical observation, and it is flagged as such.

### 10.3 Status of (21, 77)

Pending such a mechanism, (21, 77) is a **construction-level input**, on the same footing as the G₂-holonomy postulate. It is a discrete pair, fixed before the relations were frozen and consumed rigidly by all of them, but it is chosen, not selected. Version 3.5 wrote that the deeper question "why G₂ holonomy?" has the same status as "why Lorentz invariance?", and that G₂ is "the unique compact exceptional holonomy admitting the stabilizer chain G₂ ⊃ SU(3) ⊃ SU(2) ⊃ U(1)". Both statements are withdrawn. Lorentz invariance is an empirically established symmetry; G₂ holonomy is a hypothesis about an unobserved manifold. And Spin(7) contains the same chain, so G₂ is not unique in that sense.

---

## 11. Decision Rule and Refutation

A prediction is a receipt only if three things are fixed in advance: the quantity, the interval, and what happens when the measurement falls outside it. Versions up to 3.5 fixed the first two for δ_CP and wrote that a measurement outside the interval "would create serious tension". Serious tension is not a refutation. Version 3.6 writes the rule in full.

### 11.1 The rule

The rules below are fixed in version 3.6 and apply to the relations as stated in §4, with the dictionary of §3. They have no repair clause: a relation that fails is not rescued by changing its formula, its unit, its scale, or the dataset against which it is compared.

| # | Quantity | K₇ value | Rejection condition | What is rejected |
|---|----------|----------|---------------------|------------------|
| D1 | the phase e^{iδ_CP}, δ_CP = 2π·197/360 | 197° | a measurement placing δ_CP outside [182°, 212°] at 3σ (DUNE, Hyper-Kamiokande, or a global fit including them) | the δ_CP relation **and** the unit assignment R6 that produced it |
| D2 | sin²θ₂₃ (PMNS) | 6/11 = 0.545 | the octant resolved in favour of the first octant, with sin²θ₂₃ excluded from 6/11 at 3σ | the θ₂₃ relation |
| D3 | m_τ/m_e (approximate) against Q_Koide (approximate) | 1776.74 MeV vs 1776.97 MeV | an m_τ measurement excluding one value at 3σ while including the other | the excluded relation |
| D4 | sin²θ_W (M_Z), α_s (M_Z) | 3/13, √2/12 | these are already proximities or within 1σ; no rule beyond §4 is claimed | none |
| D5 | N_gen | 3 | a fourth sequential generation | the integer identity of §2.4 as a consistency check |
| D6 | m_s/m_d | 20 | lattice QCD excluding 20 at 3σ | the m_s/m_d relation |

**What a rejection does not do.** A rejection under D1 rejects the stated prediction together with the dictionary assignment that produced it; it does not by itself reject the programme, whose other relations stand or fall on their own. The paper says so now, so that it cannot be said later as a repair.

**What a confirmation would show.** A measurement of δ_CP inside the interval would show that the assignment "read 197 in degrees" agrees with the world. It would not show that the structure requires that reading, which is why R6 stays in the residue register in either case.

### 11.2 Timeline

| Experiment | Quantity | Timeline |
|------------|----------|----------|
| DUNE Phase I | δ_CP | after first beam (targeted 2031 [47]); resolution depends on exposure and true parameters [30, 31] |
| DUNE Phase II, Hyper-Kamiokande | δ_CP, octant of θ₂₃ | late 2030s–2040s |
| Belle II, BES III | m_τ | ongoing [52] |
| Lattice QCD | m_s/m_d | current 20.0 ± 2.0 in the dataset; target precision ±0.5 |
| FCC-ee | sin²θ_W, m_W/m_Z | 2040s |

---

## 12. Discussion and Conclusion: What K₇ Does Not Fix

### 12.1 What the framework is, and what it is not

The framework is a correspondence between invariants of (K₇, E₈×E₈) and 33 dimensionless parameters, stated with its dictionary, its residue and a decision rule. It is a privileged candidate in the sense of §3.5: its requirements are motivated independently of the Standard Model's values, but they do not select the Betti pair, the formulas or the normalization, and the author's choices are where those enter.

Version 3.6 withdraws several things earlier versions said: that the relations are derived from the geometry; that they cannot be fitted; that 95 observables are predicted; that m_H/m_W and Koide survive the Sieve; that a coincidence probability of 10⁻³⁴⁶ or a P-value of 5 × 10⁻⁶ measures the framework's distinctiveness; that 197° is a "pure geometry" prediction; that the generation count comes from an index theorem. Each of these was stronger than what the work supports. What remains is smaller and can be checked.

### 12.2 Where the choices enter

Every framework rests somewhere on choices it does not derive, and saying where is part of stating it. For K₇ there are three places.

- **At the requirements.** G₂ holonomy, compactness and the E₈ data are posited, not derived. They are well motivated, and they answer the question of whether the family deserves exploration; they do not answer why this member.
- **At the residue.** The Betti pair (21, 77), the normalization det(g) = 65/32 and the combination κ_T⁻¹ = 61 are set, not forced, and in the two overdetermined sectors (four lepton relations, seven density relations) none of the incompatible relations is selected (§3.3). §10 closes five routes to deriving (21, 77) and leaves one identity open.
- **At the dictionary.** No rule assigns formulas to observables, and two assignments carry units or scales that the structure does not supply: the degrees in which 197 is read, and the scales at which the couplings are compared. A confirmation of a relation would confirm the assignment, not a requirement of the structure.

### 12.3 Relation to M-theory and to other proposals

E₈×E₈ and G₂ holonomy both appear in M-theory: E₈×E₈ on the boundaries of heterotic M-theory [32], G₂ holonomy as the condition for N = 1 supersymmetry in a compactification on a seven-manifold [24, 34]. The framework does not supply a compactification of either kind. It differs from standard M-theory phenomenology [35], which works with moduli stabilization and specific singular compactifications. Its smooth K₇ does not yield the chiral non-abelian content of the Standard Model (§2.3), and its relations are not derived from a four-dimensional effective theory. The relation to the G₂-MSSM phenomenology of [33] that version 3.5 drew through a supersymmetric spectrum is withdrawn with that spectrum (§5.3).

Lisi's E₈ proposal attempted to place all Standard-Model fermions, chirality included, in a single E₈ representation, and Distler and Garibaldi showed that no such embedding exists [36]. The framework does not attempt that embedding: it uses E₈ as a source of group-theoretic integers. This avoids the obstruction; it also means that the framework makes no claim about how the fermions arise.

### 12.4 Limitations and open questions

| Issue | Status | Section |
|-------|--------|---------|
| Existence of a compact torsion-free G₂ manifold with (21, 77) | open; requires a realisable datum, then (L4), (C.1), (J) | §9 |
| Chiral non-abelian gauge sector from K₇ | not supplied; requires a UV bridge (singular locus, heterotic bundle or duality) | §2.3 |
| Selection of (21, 77) | five routes closed; one identity open | §10 |
| Formula assignment rule | absent | §3.2 |
| det(g) = 65/32 | imposed | §3.3 |
| Unit of δ_CP | assigned | §4.3 |
| Eight relations outside 2σ | retained as proximities, a scheme assignment, or in tension | §4.2 |
| Overdetermined sectors (leptons, cosmological densities) | relations mutually incompatible as exact equalities; none selected | §4.2, §6.1 |
| Look-elsewhere | closeness not distinctive in the tested reference classes | §7 |
| Quantum-gravity completion | not addressed | n/a |

### 12.5 Conclusion

This paper has stated a correspondence and the terms on which it can fail. Thirty-three dimensionless parameters are matched by closed forms in the invariants of a G₂-holonomy seven-manifold with Betti numbers (21, 77) and of E₈×E₈. Twenty-five lie within two standard deviations of the most recent measurements and eight do not. The correspondence is not derived: the Betti pair, the formulas, a metric normalization and a unit are set, and are written down as such. A test in which competing vocabularies search for their own formulas shows that closeness to the measured values does not distinguish the framework. What can distinguish it is a measurement against a rule fixed in advance; the sharpest is the leptonic CP phase, which DUNE will measure.

**We do not claim that the framework is correct.** It may be a genuine structural insight, an approximation to one, or an elaborate coincidence. The paper's aim is that whichever it is can be found out, and that the reader can see, at every step, what was derived, what was assumed, and what would bring it down.

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
[3] Planck Collaboration, A&A 641, A6 (2020)
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

[49] M. Tristram et al., "Cosmological parameters derived from the final Planck data release (PR4)," A&A 682, A37 (2024). (Frozen cosmology dataset; cited in Supplement S3.)

[50] E. Tiesinga, P.J. Mohr, D.B. Newell, B.N. Taylor, "CODATA recommended values of the fundamental physical constants: 2022," Rev. Mod. Phys. 97, 025002 (2025). (Cited in Supplement S3.)

[51] V. V. Nikulin, "Integer symmetric bilinear forms and some of their geometric applications," Izv. Akad. Nauk SSSR Ser. Mat. 43 (1979); English transl. Math. USSR Izv. 14 (1980).

[52] Belle II Collaboration, "Measurement of the τ-lepton mass with the Belle II experiment," Phys. Rev. D 108, 032006 (2023), doi:10.1103/PhysRevD.108.032006, arXiv:2305.19116.

---

## Author's Related Works

*Code and Lean proofs:* [github.com/Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) (formerly `gift-framework/core`).

- **[A]** B. de La Fournière, "An Explicit Approximate G₂ Metric on a Compact 7-Manifold with Certified Torsion-Free Completion," Zenodo [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069) (2026).
- **[B]** B. de La Fournière, "Spectral Geometry of the G₂-GIFT Manifold: Betti Numbers, KK Spectrum, and Spectral Invariants," Zenodo [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) (2026).
- **[C]** B. de La Fournière, "Newton-Kantorovich Certificate for the K3 Donaldson Embedding in the G₂-GIFT Metric," Zenodo [10.5281/zenodo.19708915](https://doi.org/10.5281/zenodo.19708915) (2026).
- **[D]** B. de La Fournière, "An Explicit Closed-Form G₂ Ansatz on a K3-Coassociative Neck with Hyperkähler Rotation and Picard-Lefschetz Wirtinger Certificate," Zenodo [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065) (2026).
- **[E]** B. de La Fournière, "A conditional analytic framework for rank-one branched Kovalev–Lefschetz adiabatic limits," Zenodo DOI [10.5281/zenodo.21215956](https://doi.org/10.5281/zenodo.21215956) (2026), main paper 68 pp + supplement 25 pp; dataset and four `mpmath.iv` verification scripts at Zenodo [10.5281/zenodo.21209412](https://doi.org/10.5281/zenodo.21209412) (CC BY 4.0). Conditional theorems for a $K_7 \to S^3$ construction with $N = 77$ round-unlink branch components; the single-root datum $\mathcal D_0$ at which its constants are computed is not realisable as posed (§9).
- **[M]** B. de La Fournière, "A reproducible standard for arithmetic coincidence claims in fundamental physics," Zenodo [10.5281/zenodo.20728964](https://doi.org/10.5281/zenodo.20728964) (2026). The Sieve methodology and its four-null scorecard for the K₇ relations.
- **[S-frozen]** B. de La Fournière, "Counting Coincidences: frozen inputs" (observable list and expression grammars), Zenodo dataset [10.5281/zenodo.20666878](https://doi.org/10.5281/zenodo.20666878), v1.0 of 12 June 2026.
- **[K3A]** B. de La Fournière, "Certified Analytic Geometry on an Explicit K3 Surface," Zenodo [10.5281/zenodo.22047469](https://doi.org/10.5281/zenodo.22047469) (2026). A certified holomorphic atlas of an explicit K3 surface; no metric claim.
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
| S4: Sieve and look-elsewhere diagnostics | The four-null scorecard, the look-elsewhere test of §7.2, archived diagnostics of earlier versions |

---

*The K₇ Framework (formerly GIFT)*
