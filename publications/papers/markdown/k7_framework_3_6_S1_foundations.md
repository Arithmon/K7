# Supplement S1: Mathematical Foundations

## E₈ Exceptional Lie Algebra, G₂ Holonomy Manifolds, and K₇ Construction

*Mathematical background for the K₇ framework: the E₈ and G₂ data the dictionary uses, the topological status of K₇, and the algebraic reference form.*

**Lean**: the arithmetic statements of this supplement are formalized in Arithmon/K7-Lean (the library rests on fourteen axioms beyond Mathlib's foundations, four literature imports and ten interval certificates, and uses no `sorry`; the 33 relations themselves depend only on the standard axioms; main §8, S3.7). Formalization establishes the arithmetic, not the physical reading. Lean names are given as they appear in the repository (v3.6 alignment branch, S3.7).

---

## Abstract

This supplement presents the mathematical architecture underlying the K₇ framework. Part I gives the E₈ data the dictionary uses, with the arithmetic rewritings of earlier versions and their status. Part II introduces G₂ holonomy manifolds, including the characterization of the g₂ subalgebra as the kernel of the Lie derivative map. Part III discusses the topology of K₇: the pair (b₂, b₃) = (21, 77) has no known construction. It does not appear among the catalogued compact G₂ manifolds, and the Joyce–Karigiannis ℤ₂³ route proposed in version 3.5 does not currently realize it, because its quotient cohomology is incompatible with the stated group action (§8.4). Part IV describes the algebraic reference form, whose scale is fixed by the imposed normalization det(g) = 65/32 (main R2), and the status of Joyce's perturbation theorem for this setting: its smallness constant depends on geometric bounds that are not established here, and the existence of a compact torsion-free metric is open (main §9). Numerical (PINN) experiments are reported as such. The arithmetic statements are verified in Lean 4; the archived module `JoyceKarigiannisConstruction.lean` verified arithmetic on an erroneous input and is withdrawn as evidence (§8.4).

---

# Part 0: The Octonionic Foundation

## 0. Why This Framework Exists

The K₇ framework is motivated by a single algebraic fact:

**The octonions 𝕆 are the largest normed division algebra.**

The chain of motivations, and where the framework's choices enter, is:

```
𝕆 (octonions, dim 8)
    │
    ▼
Im(𝕆) = ℝ⁷ (imaginary octonions)
    │
    ▼
G₂ = Aut(𝕆) (automorphism group, dim 14)
    │
    ▼
K₇ with G₂ holonomy (posited; seam metric certified in [A]; global existence open)
    │
    ▼
Topological invariants (b₂, b₃) = (21, 77)   ← input (main R1)
    │
    ▼
33 relations assigned to observables   ← dictionary (main §3), not derived
```

**Status**: the relations are assignments, written in the constants that the steps above supply; the dataset (95 entries, of which 33 relations are counted) is described in S3, and the arithmetic of each relation in S2. No geometric map from the invariants to the observables is known.

### 0.1 The Division Algebra Chain

| Algebra | Dim | Physics Role | Stops? |
|---------|-----|--------------|--------|
| ℝ | 1 | Classical mechanics | No |
| ℂ | 2 | Quantum mechanics | No |
| ℍ | 4 | Spin, Lorentz group | No |
| **𝕆** | **8** | **Exceptional structures** | **Yes** |

The pattern terminates at 𝕆. There is no 16-dimensional normed division algebra. The octonions are *the end of the line*.

### 0.2 G₂ as Octonionic Automorphisms

**Definition**: G₂ = {g ∈ GL(𝕆) : g(xy) = g(x)g(y) for all x,y ∈ 𝕆}

| Property | Value | Role |
|----------|-------|-----------|
| dim(G₂) | 14 = C(7,2) − C(7,1) = 21 − 7 | Q_Koide numerator |
| Action | Transitive on S⁶ ⊂ Im(𝕆) | Connects all directions |
| Embedding | G₂ ⊂ SO(7) | Preserves φ₀ |

### 0.3 Why dim(K₇) = 7

The dimension 7 is a consequence of the octonionic structure, not an independent choice:
- Im(𝕆) has dimension 7
- G₂ acts naturally on ℝ⁷
- G₂ occurs as a holonomy group only in dimension 7 (Berger, §6.3)

The choice made by the framework is G₂ holonomy; dimension 7 then follows.

### 0.4 The Fano Plane: Combinatorial Structure of Im(𝕆)

The 7 imaginary octonion units form the **Fano plane** PG(2,2), the smallest projective plane:
- 7 points (imaginary units e₁...e₇)
- 7 lines (multiplication triples eᵢ × eⱼ = ±eₖ)
- 3 points per line

**Combinatorial counts**:
- Point-line incidences: 7 × 3 = 21 = C(7,2) = b₂
- Automorphism group: PSL(2,7) with |PSL(2,7)| = 168

**Arithmetic identity**:
$$(b_3 + \dim(G_2)) + b_3 = 91 + 77 = 168 = |{\rm PSL}(2,7)| = {\rm rank}(E_8) \times b_2$$

It is an identity among the chosen integers of the kind recorded in S2.7; no geometric structure is attached to it.

---

# Part I: E₈ Exceptional Lie Algebra

## 1. Root System and Dynkin Diagram

### 1.1 Basic Data

| Property | Value | Role |
|----------|-------|-----------|
| Dimension | dim(E₈) = 248 | Gauge DOF |
| Rank | rank(E₈) = 8 | Cartan subalgebra |
| Number of roots | \|Φ(E₈)\| = 240 | E₈ kissing number |
| Root length | √2 | α_s numerator |
| Coxeter number | h = 30 | Icosahedron edges |
| Dual Coxeter number | h∨ = 30 | McKay correspondence |

### 1.2 Root System Construction

E₈ root system in ℝ⁸ has 240 roots:

**Type I (112 roots)**: Permutations and sign changes of (±1, ±1, 0, 0, 0, 0, 0, 0)

**Type II (128 roots)**: Half-integer coordinates with even minus signs:
$$\frac{1}{2}(\pm 1, \pm 1, \pm 1, \pm 1, \pm 1, \pm 1, \pm 1, \pm 1)$$

**Verification**: 112 + 128 = 240 roots, all length √2.

**Lean**: the root-system statements are proved:
- `D8_roots_card` = 112, `HalfInt_roots_card` = 128
- `E8_roots_card` = 240, `E8_roots_decomposition`
- `E8_inner_integral`, `E8_norm_sq_even`, `E8_sub_closed`
- `E8_basis_generates`: Every lattice vector is integer combination of simple roots (theorem)

### 1.3 Cartan Matrix

$$A_{E_8} = \begin{pmatrix}
2 & 0 & -1 & 0 & 0 & 0 & 0 & 0 \\
0 & 2 & 0 & -1 & 0 & 0 & 0 & 0 \\
-1 & 0 & 2 & -1 & 0 & 0 & 0 & 0 \\
0 & -1 & -1 & 2 & -1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 & 2 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 & 2 & -1 & 0 \\
0 & 0 & 0 & 0 & 0 & -1 & 2 & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & -1 & 2
\end{pmatrix}$$

**Properties**: det(A) = 1 (unimodular), positive definite.

---

## 2. Weyl Group

### 2.1 Order and Factorization

$$|W(E_8)| = 696,729,600 = 2^{14} \times 3^5 \times 5^2 \times 7$$

### 2.2 Factorization in the Structural Constants

The Weyl group order can be written in the framework's structural constants:

$$|W(E_8)| = p_2^{\dim(G_2)} \times N_{gen}^{Weyl} \times Weyl^{p_2} \times \dim(K_7)$$

| Factor | Exponent | Value | Origin |
|--------|----------|-------|-------------|
| 2¹⁴ | dim(G₂) = 14 | 16384 | p₂^(holonomy dim) |
| 3⁵ | Weyl = 5 | 243 | N_gen^(Weyl factor) |
| 5² | p₂ = 2 | 25 | Weyl^(binary) |
| 7¹ | 1 | 7 | dim(K₇) |

This is an arithmetic rewriting of the prime factorization 2¹⁴ · 3⁵ · 5² · 7, with each prime and exponent matched to a constant; it is the source of the constant Weyl = 5. Lean: `E8_weyl_order_factored`, `E8_weyl_factored` (the prime factorization).

---

### 2.3 Three Expressions for Weyl = 5

$$\frac{\dim(G_2) + 1}{N_{gen}} = \frac{b_2}{N_{gen}} - p_2 = \dim(G_2) - \text{rank}(E_8) - 1 = 5$$

| Expression | Computation | Result |
|------------|-------------|--------|
| (dim(G₂) + 1)/N_gen | (14 + 1)/3 | 5 |
| b₂/N_gen − p₂ | 21/3 − 2 | 5 |
| dim(G₂) − rank(E₈) − 1 | 14 − 8 − 1 | 5 |

Earlier versions called this the "Weyl Triple Identity" and read the convergence as evidence that Weyl = 5 is "structurally constrained". Three expressions in small integers that evaluate to the same small integer are an arithmetic fact about the chosen integers; they fix no further quantity, and the reading is withdrawn (S2.1). Weyl enters det(g) = 65/32 (main R2) and the factorization of §2.2. The "cosmological ratio √Weyl" of earlier versions belonged to the relation Ω_m = Ω_DE/√5, withdrawn in v3.6 (S2.6).

---

## 3. Exceptional Chain

### 3.1 The Pattern

A pattern connects exceptional algebra dimensions to primes:

| Algebra | n | dim(E_n) | Prime | Index |
|---------|---|----------|-------|-------|
| E₆ | 6 | 78 | 13 | prime(6) |
| E₇ | 7 | 133 | 19 | prime(8) = prime(rank(E₈)) |
| E₈ | 8 | 248 | 31 | prime(11) = prime(D_bulk) |

### 3.2 Three Factorizations

For n ∈ {6, 7, 8}:
$$\dim(E_n) = n \times prime(g(n))$$

where g(6) = 6, g(7) = rank(E₈) = 8, g(8) = D_bulk = 11 (= dim(M₄) + dim(K₇) = 4 + 7, the total bulk dimension of M-theory).

**Check** (Lean):
- E₆: 6 × 13 = 78 ✓
- E₇: 7 × 19 = 133 ✓
- E₈: 8 × 31 = 248 ✓

The index function g is chosen case by case (6, rank E₈, D_bulk), so the statement is a description of three factorizations, not a structural theorem. Lean: `all_exceptional_chain_relations_certified`. Earlier versions called this the "Exceptional Chain Theorem"; the name is withdrawn with the reading.

---

## 4. E₈×E₈ Product Structure

### 4.1 Direct Sum

| Property | Value |
|----------|-------|
| Dimension | 496 = 248 × 2 |
| Rank | 16 = 8 × 2 |
| Roots | 480 = 240 × 2 |

### 4.2 τ Numerator Connection

The hierarchy parameter numerator:
$$\tau_{num} = 3472 = 7 \times 496 = \dim(K_7) \times \dim(E_8 \times E_8)$$

Lean: `tau_num_factorization`. τ is used only by Type II entries (S3).

### 4.3 The Binary Ratio p₂ = 2

p₂ is defined as dim(G₂)/dim(K₇) = 14/7 = 2 and is called the binary ratio. It is not a Pontryagin class (v3.5 erratum, §6). Earlier versions listed a "triple geometric origin" of p₂ (also 496/248, and the √2 of the E₈ root length); these are three different occurrences of the number 2, not three derivations of one constant, and the list is withdrawn.

---

## 5. Exceptional Algebras from Octonions

The foundational role of octonions is established in Part 0. This section details the exceptional algebraic structures that emerge from 𝕆.

### 5.1 Exceptional Jordan Algebra J₃(O)

| Property | Value |
|----------|-------|
| dim(J₃(O)) | 27 = 3³ |
| dim(J₃(O)₀) | 26 (traceless) |

**E-series expression**: 27 can be written in E-series dimensions:

$$\dim(J_3(\mathbb{O})) = \frac{\dim(E_8) - \dim(E_6) - \dim(SU_3)}{6} = \frac{248 - 78 - 8}{6} = \frac{162}{6} = 27$$

This is an arithmetic expression for 27 in E-series dimensions; dim J₃(𝕆) = 27 is a Lie datum in its own right (main §3.1).

Lean: `j3o_e_series_certificate`.

### 5.2 F₄ Connection

F₄ is the automorphism group of J₃(O):
$$\dim(F_4) = 52 = p_2^2 \times \alpha_{sum} = 4 \times 13$$

### 5.3 Exceptional Differences

| Difference | Value | Framework expression |
|------------|-------|------|
| dim(E₈) − dim(J₃(O)) | 221 = 13 × 17 | α_sum × (dim G₂ + N_gen) |
| dim(F₄) − dim(J₃(O)) | 25 = 5² | Weyl² |
| dim(E₆) − dim(F₄) | 26 | dim(J₃(O)₀) |

These are arithmetic rewritings (S2.7); they are not formalized as a group.

### 5.4 Structural Derivation of τ

The hierarchy parameter τ is defined as a ratio of framework constants:

$$\tau = \frac{\dim(E_8 \times E_8) \times b_2}{\dim(J_3(\mathbb{O})) \times H^*} = \frac{496 \times 21}{27 \times 99} = \frac{10416}{2673} = \frac{3472}{891}$$

**Prime factorization**:
- Numerator: 3472 = 2⁴ × 7 × 31 = dim(K₇) × dim(E₈×E₈)
- Denominator: 891 = 3⁴ × 11 = N_gen⁴ × D_bulk

**Alternative form**: τ_num = 7 × 496 = dim(K₇) × dim(E₈×E₈) = 3472

τ is used only by Type II entries (S3), which are not counted; earlier versions presented this definition as establishing τ as "a geometric constant rather than a free parameter", which a choice of ratio cannot do, and the sentence is withdrawn.

Lean: `tau_structural_certificate`.

---

# Part II: G₂ Holonomy Manifolds

## 6. Definition and Properties

### 6.1 G₂ as Exceptional Holonomy

| Property | Value | Role |
|----------|-------|-----------|
| dim(G₂) | 14 | Q_Koide numerator |
| rank(G₂) | 2 | Lie rank |
| Definition | Aut(O) | Octonion automorphisms |

**Lean**: the G₂ cross-product statements are proved:
- `epsilon_antisymm`, `epsilon_diag`, `cross_apply` ✓
- `G2_cross_bilinear`, `G2_cross_antisymm`, `cross_self` ✓
- `G2_cross_norm` (Lagrange identity ‖u×v‖² = ‖u‖²‖v‖² − ⟨u,v⟩²) ✓
- `reflect_preserves_lattice` (Weyl reflection) ✓
- `cross_is_octonion_structure` (case check over the 343 index triples) ✓
- `G2_equiv_characterizations` ✓ (by `rfl`: the two predicates are defined to coincide, so this is not a theorem about two characterizations)

### 6.2 G₂ as Kernel of the Lie Derivative

The G₂ subalgebra of so(7) admits a precise characterization as the stabilizer of the associative 3-form phi₀. For any antisymmetric matrix A in so(7), the Lie derivative of phi₀ is:

$$L_A(\varphi_0)_{ijk} = A_{ia}\varphi_{ajk} + A_{ja}\varphi_{iak} + A_{ka}\varphi_{ija}$$

The g₂ subalgebra consists of all A for which L_A(phi₀) = 0:

$$\mathfrak{g}_2 = \ker(L) = \{A \in \mathfrak{so}(7) : L_A(\varphi_0) = 0\}$$

This yields the decomposition so(7) = g₂ + V₇, where dim(g₂) = 14 and dim(V₇) = 7. The complement V₇ carries the standard 7-dimensional representation of G₂.

In practice, the kernel is computed via singular value decomposition (SVD) of the linear map L: so(7) --> Lambda³(R⁷). The 14 singular vectors with eigenvalue zero span g₂; the 7 singular vectors with nonzero eigenvalue span V₇.

**Note**: A heuristic construction based on Fano-plane indices does not produce correct g₂ generators (each such generator is approximately 67% in g₂ and 33% in V₇). The kernel-based construction is the correct definition and must be used in all numerical computations involving g₂/V₇ decomposition.

### 6.3 Holonomy Classification (Berger)

| Dimension | Holonomy | Geometry |
|-----------|----------|----------|
| **7** | **G₂** | **Exceptional** |
| 8 | Spin(7) | Exceptional |

### 6.4 Torsion: Definition and Framework Interpretation

**Mathematical definition**: Torsion measures failure of G₂ structure to be parallel:
$$T = \nabla\phi \neq 0$$

For a G₂ structure φ, the intrinsic torsion decomposes into four irreducible G₂-modules:

$$T \in W_1 \oplus W_7 \oplus W_{14} \oplus W_{27}$$

| Class | Dimension | Characterization |
|-------|-----------|------------------|
| W₁ | 1 | Scalar: dφ = τ₀ ⋆φ |
| W₇ | 7 | Vector: dφ = 3τ₁ ∧ φ |
| W₁₄ | 14 | Co-closed part of d⋆φ |
| W₂₇ | 27 | Traceless symmetric |

**Total dimension**: 1 + 7 + 14 + 27 = 49 = 7² = dim(K₇)²

The torsion-free condition requires all four classes to vanish simultaneously, a highly constrained state with 49 conditions.

**Torsion-free condition**:
$$\nabla\phi = 0 \Leftrightarrow d\phi = 0 \text{ and } d*\phi = 0$$

**What the framework uses.** None of the 33 relations uses a torsion value. The integer κ_T⁻¹ = 61 = b₃ − dim(G₂) − p₂ enters three relations (α⁻¹, Y_p, Ω_m/Ω_Λ); earlier versions called κ_T = 1/61 a "topological capacity for torsion" bounding deviations from the reference form, and said that physical interactions "emerge from the geometry of K₇". No computation connects 61 to torsion, and no mechanism is supplied for the second statement; both readings are withdrawn (main R3).

---

## 7. Topological Invariants

### 7.1 Combinations Used by the Dictionary

| Constant | Formula | Value | Status |
|----------|---------|-------|--------|
| det(g) | p₂ + 1/(b₂ + dim(G₂) − N_gen) | 65/32 | imposed normalization (main R2) |
| κ_T | 1/(b₃ − dim(G₂) − p₂) | 1/61 | integer combination (main R3) |
| sin²θ_W | b₂/(b₃ + dim(G₂)) | 3/13 | relation A01 (S2.2) |

det(g) and κ_T⁻¹ each have a second expression in the constants that agrees with the one above on the line b₂ = 21 and differs elsewhere (main R2, R3; S2.1).

### 7.2 The 61 Decomposition

$$\kappa_T^{-1} = 61 = \dim(F_4) + N_{gen}^2 = 52 + 9$$

Alternative:
$$61 = p_2 \times \text{Weyl} \times (\text{Weyl} + 1) + 1 = 2 \times 5 \times 6 + 1$$

Further expressions for 61 are arithmetic facts of the kind recorded in S2.7; they do not give 61 a physical meaning (main R3). Lean: `kappa_T_from_F4_generations`.

### 7.3 Spectral Geometry

The Laplace-Beltrami operator on K₇ admits a discrete spectrum with eigenvalues 0 = λ₀ < λ₁ ≤ λ₂ ≤ ... Its first non-zero eigenvalue is λ₁ (the spectral gap).

**A ratio of the constants**:

$$\frac{\dim(G_2)}{H^*} = \frac{14}{b_2 + b_3 + 1} = \frac{14}{99} = 0.1414...$$

This is not the spectral gap, and it is not a bound on it; it is listed for comparison.

**Analytical spectral gap**: If K₇ were a twisted connected sum with a building block of b₂(M₁) = 11 (a decomposition that is not available, §8.3), the first eigenvalue of the scalar Laplacian admits a closed-form expression from the 1D Sturm-Liouville reduction on the TCS neck:

$$\boxed{\lambda_1 = \frac{\pi^2}{L^2 \cdot g_{ss}} = \frac{6\pi^2}{25 \cdot (b_2(M_1) + \mathrm{rank}(E_8))} = \frac{6\pi^2}{475} = 0.12467...}$$

where L = 5 is the effective neck domain length (including ACyl tails), g_ss = 19/6 is the seam metric component of [A], written as (b₂(M₁) + rank(E₈))/(3·rank(G₂)), and b₂(M₁) = 11 is the Picard rank assigned to the first building block of the conjectured decomposition. A numerical computation on the seam metric (Richardson extrapolation, N = 800 → 1600) gives λ₁ = 0.12461, 0.05% from the closed form.

This is a closed form for the first eigenvalue of the one-dimensional seam reduction, conditional on the identification above (see the status paragraph below).

**Comparison with topological ratios:**

| Expression | Value | Deviation from λ₁ | Status |
|-----------|-------|-------------------|--------|
| 6π²/475 (closed form) | 0.12467 | 0.00% (definition) | conditional on b₂(M₁) = 11 |
| NK Richardson | 0.12461 | 0.05% | Numerical verification |
| 14/99 (ratio of constants) | 0.14141 | +13.4% | not a bound |
| 13/99 | 0.13131 | +5.3% | ratio of constants |

*Remark:* The exact value λ₁ = 6π²/475 involves π (from the Sturm-Liouville eigenvalue structure), not a rational number. The product λ₁ × H* = 6π² × 99/475 = 12.342 (see the regularity below).

**Lean**: the arithmetic of the closed form is in the module `Spectral.PhysicalSpectralGap`; the analytic statements it relies on enter through the literature axioms of main §8. Earlier versions also described the near-identity dim(G₂)/√2 ≈ π² (0.30%) as "resolved" by this formula, and a Lean module `Spectral.SelbergBridge` as connecting the spectral gap to a Dirichlet polynomial through the Selberg trace formula; neither bears on the framework, and both statements are withdrawn here.

**Status of §7.3.** The closed form assumes a TCS decomposition with b₂(M₁) = 11, whose building blocks are not identified (§8.3), and the numerical value is a spectrum of the approximate seam metric, not of a torsion-free metric on a compact K₇ (main §9). The regularity λ₁ · H* ≈ 12.34 across the catalogued G₂ manifolds is an empirical observation of a scan (`canonical/scripts/construction_classification.py`), not a theorem. No relation of the framework uses λ₁.

### 7.4 Continued Fraction Structure

The ratio dim(G₂)/H* has the continued fraction

$$\frac{14}{99} = [0; 7, 14] = \cfrac{1}{7 + \cfrac{1}{14}}$$

whose partial quotients are 7 = dim(K₇) and 14 = dim(G₂). This is a property of the ratio 14/99, not of the spectral gap. It is an arithmetic fact; no physical consequence is claimed.

### 7.5 Pell Equation Structure

H* and dim(G₂) satisfy a Pell equation:

$$\boxed{H^{*2} - 50 \times \dim(G_2)^2 = 1}$$

Explicitly:
$$99^2 - 50 \times 14^2 = 9801 - 9800 = 1$$

where $50 = \dim(K_7)^2 + 1 = 49 + 1$.

**Fundamental solution**: $(99, 14)$ is the fundamental solution of $x^2 - 50y^2 = 1$. It is the square of $\varepsilon = 7 + \sqrt{50}$, which solves $x^2 - 50y^2 = -1$:

$$\varepsilon^2 = (7 + \sqrt{50})^2 = 99 + 14\sqrt{50}$$

**Continued fraction**: $\sqrt{50} = [7; \overline{14}]$, with period 1, which is why the same two integers appear in §7.4.

**Status**: arithmetic identity, verified in Lean; no physical consequence is claimed. Earlier versions combined it with a "selection principle" κ = π²/14 (a spectral normalization in the Lean module `Spectral.SelectionPrinciple`, unrelated to the selection problem of main §1) into a link with the spectral gap; that reading is withdrawn.

---

# Part III: K₇ Manifold Construction

## 8. Twisted Connected Sum Framework

### 8.1 TCS Construction

The twisted connected sum (TCS) construction provides the primary method for constructing compact G₂ manifolds from asymptotically cylindrical building blocks.

Compact G₂ manifolds can be built by gluing two asymptotically cylindrical (ACyl) G₂ manifolds along their cylindrical ends, with the topology controlled by a twist diffeomorphism φ.

### 8.2 Asymptotically Cylindrical G₂ Manifolds

**Definition**: A complete Riemannian 7-manifold (M, g) with G₂ holonomy is asymptotically cylindrical (ACyl) if there exists a compact subset K ⊂ M such that M \ K is diffeomorphic to (T₀, ∞) × N for some compact 6-manifold N.

### 8.3 Topological Status of (21, 77)

K₇ is posited with (b₂, b₃) = (21, 77) (main R1). **No construction of a compact G₂ manifold with these Betti numbers is currently known.** The Newton–Kantorovich certificate of [A] concerns the neck (seam) metric; it does not certify the Betti numbers, and no global torsion-free G₂ structure has been constructed (main §9).

**Catalogued constructions.** The pair does not appear among the catalogued compact G₂ manifolds (Joyce's orbifold constructions; the twisted connected sums of Corti–Haskins–Nordström–Pacini). Orthogonal TCS is excluded by parity (b₂ + b₃ = 98 is even; CHNP Lemma 6.7). A building-block scan (2026-04-14) shows that b₂ = 21 > 20 = max ρ(K3) forces at least one semi-Fano building block, and all generic K3 lattice embeddings are excluded by the parity theorem. The CHNP 2015 tabulation covered building blocks with ρ ≤ 9 (b₂ ≤ 18); a TCS construction with semi-Fano blocks of high Picard rank has not been carried out. Non-orthogonal TCS and extra-twisted connected sums remain open within TCS.

**Withdrawn: a lattice sketch.** Earlier versions described sublattices N₁, N₂ of the K3 lattice U³ ⊕ E₈(−1)², of ranks 11 and 10, with N₁ ⊕ N₂ ⊕ ⟨2⟩ of full rank, as "consistent with a TCS construction". N₁ ⊕ N₂ ⊕ ⟨2⟩ cannot be an orthogonal decomposition of the unimodular K3 lattice (⟨2⟩ is not unimodular), only a sublattice of finite index; and two building-block lattices N₁ ⊥ N₂ describe an orthogonal gluing, which is the case excluded by parity above. The embedding conditions were never verified and no matching data was constructed. The sketch is withdrawn as support for a TCS realization.

The Joyce–Karigiannis route proposed in version 3.5 as a realization of (21, 77) does not currently realize it (§8.4).

**Global properties assumed, not established**:
- Compact 7-manifold (no boundary)
- Simply connected: π₁(K₇) = {1}, b₁ = 0
- If a torsion-free G₂ structure g* exists on K₇, then Hol(g*) = G₂ [Joyce, Prop. 11.2.3] and Ric(g*) = 0. Its existence is open (main §9; v3.5 erratum, §7.5).
- (Euler characteristic χ(K₇) = 0 is automatic for a closed odd-dimensional manifold; §9.1.)

**Arithmetic.** b₂ = 21 = C(7,2) and b₃ = 77 = C(7,3) + 2b₂ = 35 + 42 are arithmetic facts about the posited integers; they define no geometric decomposition (§9.3).

### 8.4 The Joyce–Karigiannis ℤ₂³ Route: Proposed, Not Currently a Realization

The Joyce–Karigiannis framework [43] resolves orbifolds (T³ × K3)/G, with G ⊂ Aut(T³) × Aut(K3) acting with A₁-type singularities, by gluing families of Eguchi–Hanson spaces, and yields compact torsion-free G₂ manifolds. For a resolution of this type the Betti numbers are

$$b_2(N) = b_2\big((T^3 \times K3)/G\big) + b_0(\text{fixed loci}), \qquad b_3(N) = b_3\big((T^3 \times K3)/G\big) + b_1(\text{fixed loci}).$$

**What version 3.5 claimed.** For G = ℤ₂³ with a mixed-parity action, a four-phase computer-assisted audit (a symplectic V4 screen on a CI(2,2,2) K3, an anti-symplectic obstruction for P⁵-linear maps, abstract existence of the K3 lattice action via Mukai [44], Garbagnati–Sarti [45] and Nikulin [51], and a fixed-locus table with contributions (b₀, b₁) = (21, 55)) was combined with a quotient cohomology (b₂, b₃) = (0, 22) to give b₂ = 0 + 21 = 21 and b₃ = 22 + 55 = 77, on a K3 of Picard rank 1.

**Why the claim does not hold.** An audit of 2026-09-16 (Arithmon/K7, `docs/openwave-candidate/K7_P2_JK_postfreeze_cohomology_audit_2026_09_16.md`, with the standard-library checker `check_k3_jk_quotient_cohomology.py`) shows that the quotient cohomology is incompatible with the stated action:

- G acts diagonally on T³ × K3, so the rational cohomology of the quotient is the G-invariant part of the cohomology of T³ × K3. The stated trace of G on H²(K3) gives character multiplicities (5, 5, 2, 2, 2, 2, 2, 2), so dim H²(K3; ℚ)^G = 5.
- With W = H¹(T³; ℚ) a sum of three characters and H¹(K3) = H³(K3) = 0, the Künneth formula gives b₂((T³ × K3)/G) = 5 + #{i < j : χ_i = χ_j} ≥ 5 and b₃((T³ × K3)/G) ≤ 16. The checker enumerates all 8³ = 512 ordered torus-character triples and confirms both bounds; the product action compatible with the G₂ form gives (b₁, b₂, b₃) = (1, 6, 16).
- The pair (0, 22) is therefore impossible for this action. Keeping the stated fixed-locus contributions (21, 55) and the same resolution formula would give b₂ ≥ 26 and b₃ ≤ 71, not (21, 77).
- The stated involution profile also requires a K3 of Picard rank at least 17 (`check_k3_jk_character_gate.py`; `K7_P2_neutrino_JK_character_obstruction.md`), not the Picard-rank-1 K3 on which version 3.5 placed it.

**Scope.** This invalidates this route as stated. It does not show that every Joyce–Karigiannis construction, or every construction of a compact G₂ manifold with Betti numbers (21, 77), is impossible. The archived Lean module `JoyceKarigiannisConstruction.lean` (master theorem `jk_z23_construction_realizes_gift_betti`) verified the arithmetic of the Betti formula from the erroneous quotient input; it is withdrawn as evidence for the route. Correcting the route would require a fully specified product action, its quotient Betti numbers computed directly, and an independent audit of the singular components and of the resolution formula.

**The neck.** The NK-certified seam metric of [A] and the closed-form neck ansatz of [D] operate at the neck level of a putative compact extension and do not depend on which global construction, if any, completes it. They are evidence about a neck, not about the existence of K₇.

**Compatibility with intermediate-curvature splitting (Chen-Hong 2026).** Recent work of Chen and Hong [48] establishes a sharp dichotomy for noncompact manifolds with nonnegative m-intermediate curvature admitting a smooth proper degree-nonzero map to M^{n−m} × T^{m−1} × ℝ. For 3 ≤ n ≤ 5 with 1 ≤ m ≤ n−1, or for 6 ≤ n ≤ 7 with m ∈ {1, n−2, n−1}, the manifold is forced to split isometrically as the Riemannian product E × T^{m−1} × ℝ. By contrast, for 6 ≤ n ≤ 7 and 2 ≤ m ≤ n−3, they construct explicit metrics on S^{n−m} × T^{m−1} × ℝ with uniformly positive m-intermediate curvature, showing the algebraic gate m² − mn + m + n > 0 is sharp. The framework's coassociative neck has topology K3 × T² × ℝ (n = 7, m = 3, giving m² − mn + m + n = −2 < 0), placing it within the Chen-Hong "non-rigid" window: metrics on this topology with nonnegative 3-intermediate curvature need not split. The k ≥ 1 Chebyshev corrections of the seam metric [A] are therefore not obstructed by a forced splitting; this is a compatibility statement about the neck, not a construction of K₇.

---

## 9. Cohomological Structure (Conditional on Existence)

### 9.1 Betti Spectrum, Poincaré Duality and Euler Characteristic

If a compact, simply connected K₇ with holonomy G₂ and (b₂, b₃) = (21, 77) exists, Poincaré duality fixes its full Betti spectrum:

| k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| b_k(K₇) | 1 | 0 | 21 | 77 | 77 | 21 | 0 | 1 |

with b₁ = 0 from simple connectivity, b₂ and b₃ posited (R1), and b₄ to b₇ by duality. The Euler characteristic of any compact oriented odd-dimensional manifold vanishes: χ(K₇) = 0. Lean: `euler_char_K7_is_zero`, `poincare_duality_K7`. The combination H* = b₂ + b₃ + 1 = 99 is used by the dictionary.

A Mayer–Vietoris computation of (b₂, b₃) would require a decomposition of K₇, for example the two halves of a twisted connected sum; none is available (§8.3).

### 9.2 Numerical Consistency

The spectral analysis of the approximate seam metric ([B]) finds 21 near-zero eigenvalues of the Laplacian on 2-forms and 77 on 3-forms, separated from the rest of the spectrum. This is consistent with the posited Betti numbers; it is not a certificate of them, since the metric is approximate and is not a metric on a compact K₇.

### 9.3 The Integer 42

The number 42 appears in several relations as a combination of framework constants:

| Expression | Value |
|-----------|-------|
| p₂ × N_gen × dim(K₇) | 2 × 3 × 7 = 42 |
| 2 × b₂ | 2 × 21 = 42 |
| b₃ − C(7,3) | 77 − 35 = 42 |

It is not the Euler characteristic (χ(K₇) = 0). Lean: `magic_42_gift_form`; on the v3.6 alignment branch 42 is `two_b2 := 2 * b2`, and the earlier name `chi_K7` is kept only as a deprecated alias (S3.7).

**Withdrawn: a "local ⊕ global" splitting of H³.** Earlier versions wrote H³(K₇) = H³_local ⊕ H³_global with dimensions 35 + 42, the 35 identified with Λ³(ℝ⁷). The 35 is the rank of the bundle Λ³T*K₇, a pointwise dimension; it does not provide a 35-dimensional subspace of the global cohomology H³(K₇). The identity 35 + 42 = 77 is arithmetic and does not justify the decomposition.

---

# Part IV: Metric Structure and Verification

## 10. Structural Metric Invariants

### 10.1 Structural Metric Invariants and Normalizations

Two quantities that the dictionary uses are written as properties of a metric. Neither is computed from a metric: κ_T⁻¹ is an integer combination and det(g) is a normalization imposed on the metric.

| Invariant | Formula | Value | Status |
|-----------|---------|-------|--------|
| κ_T | 1/(b₃ - dim(G₂) - p₂) | 1/61 | integer combination (main R3) |
| det(g) | p₂ + 1/(b₂ + dim(G₂) − N_gen) | 65/32 | imposed normalization (main R2; §10.3) |

### 10.2 The Combination κ_T = 1/61

**Arithmetic**:
$$\kappa_T = \frac{1}{b_3 - \dim(G_2) - p_2} = \frac{1}{77 - 14 - 2} = \frac{1}{61}$$

Earlier versions read 61 as "effective matter degrees of freedom" (77 fermion modes minus 14 gauge constraints minus a binary factor). Nothing in the framework identifies b₃ with fermion modes or dim(G₂) with gauge constraints in this subtraction; the reading is withdrawn.

**Status**: integer combination (main R3)

### 10.3 Metric Determinant det(g) = 65/32

The value 65/32 can be written in several ways in the framework constants; three are:

**Expression 1**:
$$\det(g) = \frac{\text{Weyl} \times (\text{rank}(E_8) + \text{Weyl})}{2^{\text{Weyl}}} = \frac{5 \times 13}{32} = \frac{65}{32}$$

**Expression 2** (the one used, main App. B):
$$\det(g) = p_2 + \frac{1}{b_2 + \dim(G_2) - N_{\text{gen}}} = 2 + \frac{1}{21+14-3} = 2 + \frac{1}{32} = \frac{65}{32}$$

**Expression 3**:
$$\det(g) = \frac{H^* - b_2 - 13}{32} = \frac{99 - 21 - 13}{32} = \frac{65}{32}$$

Expressions 1 and 2 agree on the line b₂ = 21 and differ elsewhere (main R2); expression 3 uses only b₃. Several expressions of one rational number in a few integers are not a derivation from topology. The actual chain is:
the metric optimization was constrained to det(g) = 65/32 (a normalization target
chosen to be compatible with the known structural parameters g_ss = 19/6, g_T² = 7/6),
and the above formulas were identified post-hoc. Any rational number with small
numerator/denominator can be expressed as combinations of a few integers.

**Numerical value**: 65/32 = 2.03125 (exact rational)

**Status**: imposed normalization (main R2), exact by construction and not derived from topology. Six of the 33 relations use det_num or det_den and depend on this choice (main §4.4).

---

## 11. Reference Form, Numerics and Formalization

### 11.1 The Algebraic Reference Form

**Scaling law.** A positive 3-form φ determines its metric g_φ through
$$(\iota_x\varphi)\wedge(\iota_y\varphi)\wedge\varphi = 6\, g_\varphi(x,y)\,\mathrm{vol}_{g_\varphi}.$$
Under φ ↦ cφ (c > 0) the left side scales by c³, and if g ↦ λg the volume form scales by λ^{7/2}; hence c³ = λ^{9/2}, that is
$$g_{c\varphi} = c^{2/3}\, g_\varphi, \qquad \det g_{c\varphi} = c^{14/3}\,\det g_\varphi .$$

**The reference form.** Fix a coframe (e¹, …, e⁷) and let φ₀ be the standard form in it (§12.1); in that coframe the matrix of g_{φ₀} is I₇. To impose det g = D = 65/32 in this fixed coframe,
$$\boxed{\varphi_{\text{ref}} = D^{3/14}\,\varphi_0, \qquad g_{\text{ref}} = D^{1/7}\, g_{\varphi_0}, \qquad \det g_{\text{ref}} = D.}$$

**Correction.** Earlier versions wrote φ_ref = c φ₀ with c = D^{1/14} and g_ref = c² I₇, using the law g_{cφ} = c² g_φ. That law is wrong; with the correct law, D^{1/14} φ₀ induces det g = D^{1/3} ≈ 1.26645, not 65/32. The metric written there, D^{1/7} I₇, is the right metric, but it is induced by D^{3/14} φ₀.

**Which metric the coframe is orthonormal for.** The coframe is orthonormal for g_{φ₀}. For g_ref it is not: the matrix of g_ref in it is D^{1/7} I₇. In a coframe orthonormal for g_ref itself, the matrix of g_ref is I₇ and the form reads φ₀ again; the normalization det g = 65/32 is a statement relative to the fixed coframe, not an invariant of the G₂ structure. "I₇" reflects this frame choice, not global flatness. The NK-certified model of [A] is a conditional statement about a seam region; it does not construct a compact K₇ (main §9).

| Property | Value | Status |
|----------|-------|--------|
| det(g) | 65/32 | exact by imposed normalization, not fitted to experiment (§10.3) |
| φ_ref components | 7 of 35 non-zero | standard form (§12.2) |
| Joyce smallness hypothesis | depends on geometric bounds not established here | not verified (§11.2) |

### 11.2 Joyce Existence Theorem and Global Solutions

**Clarification**: The reference form φ_ref = D^{3/14} φ₀ is the canonical G₂ structure in a local orthonormal coframe, not a globally constant form on K₇. On a compact G₂ manifold, the coframe 1-forms {eⁱ} satisfy deⁱ ≠ 0 in general, so "constant components" does not imply dφ = 0 globally.

**Actual solution structure**: The topology and geometry of K₇ impose a deformation:
$$\varphi = \varphi_{\text{ref}} + \delta\varphi$$

The torsion-free condition (dφ = 0, d*φ = 0) is a **global constraint**. Joyce's perturbation theorem gives a nearby torsion-free G₂ metric when the torsion of a closed G₂ structure is small compared with a constant that depends on the injectivity radius and curvature bounds of that structure (Joyce 2000, Thm. 11.6.1). Earlier versions compared a PINN torsion value (‖T‖_max = 4.46 × 10⁻⁴) with a fixed threshold ε₀ = 0.1 and reported a "224× safety margin". There is no universal threshold: the constant has not been computed for this structure, and the comparison is not an existence argument (main §9).

*(Version 3.5 added here that the bound κ_T = 1/61 places K₇ within Joyce's perturbative regime. No argument connects the number 1/61 to Joyce's smallness hypothesis, and the sentence is withdrawn; v3.5 erratum, §7.6.)*

### 11.3 Independent Numerical Validation (PINN)

A companion numerical program trains physics-informed neural networks (PINNs) towards G₂ metrics on a model of K₇; since no compact K₇ is constructed, the model is an atlas, not a manifold whose existence is established. The three-chart atlas (neck + two Calabi-Yau bulk regions) uses approximately 10⁶ trainable parameters in float64 precision.

**Phase 2**:

| Metric | Value | Significance |
|--------|-------|--------------|
| ‖T‖_max | 4.46 × 10⁻⁴ | small; not compared with a computed Joyce constant |
| ‖T‖_mean | 9.8 × 10⁻⁵ | small |
| det(g) error | < 10⁻⁶ | the training constrains det(g) to 65/32, so this measures the constraint, not a confirmation |

**G₂ holonomy training** (Phase 3, 13 versions, v2-v13):

Over successive training protocol refinements, the holonomy quality has improved:

| Metric | Initial (v5) | Current best (v11) | Improvement |
|--------|-------------|-------------------|-------------|
| g2_self (honest holonomy) | 3.86 | 3.25 | -16% |
| V₇ projection score | 0.51 | 0.014 | -97% |
| det(g) at neck | 4.69 | 2.031 | locked at target |
| phi drift | 13.4% | 0% | controlled |

The g2_score measures the normalized projection of Riemann curvature onto the complement of g₂ in so(7). A score of 0 corresponds to exact G₂ holonomy; the flat metric scores approximately 3.5. The V₇ projection score measures the fraction of curvature outside the g₂ subalgebra (using the correct kernel-based g₂ decomposition, see Section 6.2).

A critical bug in the g₂ basis construction was discovered and corrected between versions 9 and 10: the Fano-plane heuristic does not produce correct g₂ generators. The correct g₂ subalgebra is the kernel of the Lie derivative map (Section 6.2). This correction led to significant improvement in all subsequent versions.

Earlier versions reported that the normalization target det(g) = 65/32 "passes 8/8 independent consistency tests" (permutation, bootstrap, a Bayesian posterior, a joint p-value). A target that the optimization is constrained to cannot be validated by the optimization's output; these tests are withdrawn. det(g) = 65/32 is imposed (main R2, §10.3).

Full details of the PINN architecture, training protocol, and version-by-version results are presented in a companion paper.

### 11.4 Lean 4 Formalization

**Scope of verification**: The Lean formalization (Arithmon/K7-Lean; fourteen axioms, no `sorry`) verifies:
1. Arithmetic identities and algebraic relations between the framework's constants, including the 33 relations (`relations_v36_certified`, standard axioms only; S3.7)
2. Numerical enclosures (the ten interval certificates)
3. G₂ linear algebra on ℝ⁷: exterior algebra, Hodge star, ψ = ⋆φ (`Geometry` module)
4. Spectral modules (§7.3), which no relation uses

**The axioms** (see main §8.1): four prediction-chain axioms import literature results (`cheeger_inequality`, `literature_package`, `spectral_upper_bound`, `neck_dominates`), and ten interval certificates import numerical enclosures (`det_g_at_half`, `K3_eigenvalue_0…3` and their `_bracketed` forms). They carry content that cannot be checked by `decide` alone because it involves real arithmetic. The v3.5 text named four "external data-package" axioms, three of which had already been eliminated (v3.5 erratum, §7.1).

It does **not** formalize:
- Existence of K₇ as a smooth G₂ manifold
- Physical interpretation of topological invariants
- Uniqueness of the TCS construction

```lean
-- GIFT.Foundations.AnalyticalMetric

def phi0_indices : List (Fin 7 × Fin 7 × Fin 7) :=
  [(0,1,2), (0,3,4), (0,5,6), (1,3,5), (1,4,6), (2,3,6), (2,4,5)]

def phi0_signs : List Int := [1, 1, 1, 1, -1, -1, -1]

def scale_factor_power_14 : Rat := 65 / 32

theorem torsion_satisfies_joyce :
  torsion_norm_constant_form < joyce_threshold_num := by native_decide

theorem det_g_equals_target :
  scale_factor_power_14 = det_g_target := rfl
```

Both statements are true as written and say less than their names. `torsion_satisfies_joyce` compares two integers, one of them a fixed threshold (288) that is not Joyce's constant, which has not been computed for this structure (§11.2); it is not an existence argument. `det_g_equals_target` is a definitional equality of the rational 65/32 with the target (§12.5).

### 11.5 The Chain of Choices

The logical structure from algebra to the reference metric, and where the framework's choices enter:

```
Octonions (𝕆)
     │
     ▼
G₂ = Aut(𝕆), dim = 14
     │
     ▼
Standard form φ₀ (Harvey-Lawson 1982)
     │
     ▼
φ_ref = D^{3/14} φ₀, D = 65/32  ← framework constraint (imposed, R2)
     │
     ▼
Metric g_ref = D^{1/7} g_{φ₀}    (law g_{cφ} = c^{2/3} g_φ)
     │
     ▼
det(g) = 65/32               ← exact by imposed normalization, not fitted to experiment (§10.3)
     │
     ▼
sin²θ_W = 3/13, Q = 2/3, ...  ← assigned relations (main §3); not functionals of this metric
```

---

## 12. Analytical G₂ Metric Details

### 12.1 The Standard Form φ₀

The associative 3-form preserved by G₂ ⊂ SO(7), introduced by Harvey and Lawson (1982) in their foundational work on calibrated geometries:

$$\varphi_0 = \sum_{(i,j,k) \in \mathcal{I}} \sigma_{ijk} \, e^{ijk}$$

where:
- 𝓘 = {(0,1,2), (0,3,4), (0,5,6), (1,3,5), (1,4,6), (2,3,6), (2,4,5)}
- σ = (+1, +1, +1, +1, -1, -1, -1)

### 12.2 Linear Index Representation

In the C(7,3) = 35 basis:

| Index | Triple | Sign | Index | Triple | Sign |
|-------|--------|------|-------|--------|------|
| 0 | (0,1,2) | +1 | 23 | (1,4,6) | -1 |
| 9 | (0,3,4) | +1 | 27 | (2,3,6) | -1 |
| 14 | (0,5,6) | +1 | 28 | (2,4,5) | -1 |
| 20 | (1,3,5) | +1 | -- | -- | -- |

All other 28 components are exactly 0.

### 12.3 Metric Derivation

The metric of a positive 3-form is defined intrinsically by the identity of §11.1. Equivalently, with
$$B_\varphi(x,y) = \tfrac{1}{6}\,(\iota_x\varphi)\wedge(\iota_y\varphi)\wedge\varphi \in \Lambda^7,$$
written in the fixed coframe as B_{ij} e^{1…7}, one has g_φ = (det B)^{-1/9} B. For the standard φ₀, B = I₇ and g = I₇, det g = 1; for cφ₀, B = c³ I₇ and g = c^{2/3} I₇, recovering the scaling law.

Earlier versions reconstructed the metric as g_ij = (1/6) Σ_{k,l} φ_ikl φ_jkl. That contraction raises indices with a background Euclidean metric, so it is not a general reconstruction of g_φ: it agrees with g_φ only when φ is already standard for that background metric, and for cφ₀ it gives c² I₇ instead of c^{2/3} I₇. This is the source of the error corrected in §11.1. Setting c^{14/3} = 65/32, i.e. c = (65/32)^{3/14}, yields the framework's reference metric.

### 12.4 Comparison: Fano Plane vs G₂ Form

| Structure | 7 Triples | Role |
|-----------|-----------|------|
| **Fano lines** | (0,1,3), (1,2,4), (2,3,5), (3,4,6), (4,5,0), (5,6,1), (6,0,2) | G₂ cross-product ε_{ijk} |
| **G₂ form** | (0,1,2), (0,3,4), (0,5,6), (1,3,5), (1,4,6), (2,3,6), (2,4,5) | Associative 3-form |

Both have 7 terms but different index patterns. The Fano plane defines the octonion multiplication (cross-product), while the G₂ form is the associative calibration.

### 12.5 Verification Summary

| Method | Result | Reference |
|--------|--------|-----------|
| Algebraic | φ_ref = (65/32)^{3/14} φ₀, g_ref = (65/32)^{1/7} g_{φ₀} | §11.1 |
| Lean 4 | `det_g_equals_target : rfl` (a definitional equality of the rational 65/32 with the target; it does not check the scaling law) | AnalyticalMetric.lean |
| PINN | small torsion, holonomy score improved; not a torsion-free metric | §11.3 |
| Joyce theorem | applies under a smallness hypothesis whose constant is not computed here | [Joyce 2000]; main §9 |

None of these methods establishes a torsion-free metric on a compact K₇ (main §9).

---

## References

1. Adams, J.F. *Lectures on Exceptional Lie Groups*
2. Harvey, R., Lawson, H.B. "Calibrated geometries." *Acta Math.* 148, 47-157 (1982)
3. Bryant, R.L. "Metrics with exceptional holonomy." *Ann. of Math.* 126, 525-576 (1987)
4. Joyce, D. *Compact Manifolds with Special Holonomy*, Oxford U. Press (2000)
5. Corti, Haskins, Nordström, Pacini. *G₂-manifolds and associative submanifolds*
6. Kovalev, A. *Twisted connected sums and special Riemannian holonomy*
7. Conway, J.H., Sloane, N.J.A. *Sphere Packings, Lattices and Groups*
8. **[43]** Joyce, D., Karigiannis, S. "A new construction of compact torsion-free G₂-manifolds by gluing families of Eguchi-Hanson spaces." *J. Differential Geom.* (2021), arXiv:1707.09325 (2017).
9. **[44]** Mukai, S. "Finite groups of automorphisms of K3 surfaces and the Mathieu group." *Invent. Math.* **94**, 183–221 (1988).
10. **[45]** Garbagnati, A., Sarti, A. "Symplectic automorphisms of prime order on K3 surfaces." *J. Algebra* **318**, 323–350 (2007), arXiv:math/0603742.
11. **[48]** Chen, J., Hong, H. "Intermediate curvature and splitting theorem," arXiv:2604.26529 (2026).

---

## Author's Related Works

- **[A]** B. de La Fournière, "An Explicit Approximate G₂ Metric on a Compact 7-Manifold with Certified Torsion-Free Completion," Zenodo [10.5281/zenodo.18643069](https://doi.org/10.5281/zenodo.18643069) (2026).
- **[B]** B. de La Fournière, "Spectral Geometry of the G₂-GIFT Manifold: Betti Numbers, KK Spectrum, and Spectral Invariants," Zenodo [10.5281/zenodo.18920367](https://doi.org/10.5281/zenodo.18920367) (2026).
- **[D]** B. de La Fournière, "An Explicit Closed-Form G₂ Ansatz on a K3-Coassociative Neck with Hyperkähler Rotation and Picard-Lefschetz Wirtinger Certificate," Zenodo [10.5281/zenodo.20039065](https://doi.org/10.5281/zenodo.20039065) (2026).

---

*The K₇ Framework (formerly GIFT): Supplement S1*
*Mathematical Foundations: E₈ + G₂ + K₇*
