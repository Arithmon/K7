---
title: "Glossary"
layout: default
---

# Glossary of Technical Terms

Comprehensive definitions of technical terms, mathematical notation, and acronyms used in the K₇ framework.

## Framework-Specific Terms

### K₇ framework
**The K₇ framework** (formerly Geometric Information Field Theory). A declared correspondence (a dictionary) that assigns closed forms in the topological and Lie-theoretic invariants of a G₂-holonomy seven-manifold K₇, together with E₈×E₈ group data, to 33 dimensionless parameters of particle physics and cosmology. The relations are assignments, not derivations: no geometric map from the invariants to the observables is known.

### K₇
A posited compact 7-dimensional Riemannian manifold with G₂ holonomy. The subscript 7 indicates dimension. Its Betti numbers b₂(K₇) = 21, b₃(K₇) = 77 are inputs. No compact G₂ manifold with these Betti numbers is known; its existence is open.

### Status Classifications
Version 3.6 sorts the 33 relations into five classes against current data (they are not added into a single score):
- **within 2σ** (23 relations)
- **tension** (2): between 2σ and 3σ from the measured value
- **proximity** (6): excluded as an exact equality at more than 3σ and kept only as a numerical proximity (α⁻¹, sin²θ_W, m_μ/m_e, m_μ/m_τ, m_b/m_t, m_W/m_Z)
- **inside the PDG range** (1): m_s/m_d, whose reference is a range without an uncertainty
- **non-Gaussian profile** (1): sin²θ₂₃, in the octant the global fit disfavours, inside its 3σ range

The Lean 4 formalization verifies the arithmetic of the relations, not their physical content. The earlier labels (VERIFIED, TOPOLOGICAL, DERIVED, THEORETICAL, PHENOMENOLOGICAL, EXPLORATORY) are withdrawn.

## Lie Algebras and Groups

### E₈
The largest exceptional simple Lie algebra. Properties:
- Dimension: 248
- Rank: 8
- Root system: 240 roots, all length √2
- Simply-laced (all roots equal length)
- Cartan matrix determinant: 1

### E₈×E₈
Product of two independent copies of E₈. Total dimension 496 = 2×248.

### G₂
The automorphism group of the octonions. A 14-dimensional exceptional Lie group. Smallest exceptional group, important for 7-dimensional geometry.

### SU(N)
**Special Unitary Group**. Group of N×N unitary matrices with determinant 1.
- SU(3): Strong force (quantum chromodynamics)
- SU(2): Weak force component
- U(1): Electromagnetic force component

### Exceptional Lie Algebras
Five Lie algebras that don't fit standard infinite families:
- G₂ (dimension 14, rank 2)
- F₄ (dimension 52, rank 4)
- E₆ (dimension 78, rank 6)
- E₇ (dimension 133, rank 7)
- E₈ (dimension 248, rank 8)

### Weyl Group
Symmetry group of root system. For E₈, the Weyl group has order 696,729,600.

### Root System
Set of vectors in Euclidean space satisfying reflection symmetry. For E₈: 240 roots arranged in highly symmetric configuration.

### Rank
Dimension of maximal torus (maximal abelian subgroup). For E₈: rank 8.

## Geometry and Topology

### Holonomy
Geometric property describing how vectors change when parallel-transported around closed loops. G₂ holonomy implies special geometric structure.

### Cohomology
Mathematical tool measuring topological features. For K₇:
- H²(K₇) = ℝ²¹: read as the capacity of the gauge sector (in M-theory on a smooth G₂ manifold, b₂ counts abelian vector multiplets; the Standard-Model gauge group does not come from them)
- H³(K₇) = ℝ⁷⁷: read as the capacity of the matter sector (b₃ counts neutral chiral multiplets; a smooth G₂ manifold yields no chiral fermions)

### Betti Numbers
Topological invariants counting independent homology classes.
- b₂: Second Betti number (2-dimensional holes)
- b₃: Third Betti number (3-dimensional holes)
For K₇: b₂ = 21, b₃ = 77 (posited inputs, not derived)

### AdS₄
**Anti-de Sitter space in 4 dimensions**. Maximally symmetric spacetime with negative cosmological constant. Used in holographic models. Not used by the K₇ relations.

### Compact Manifold
Topological space that is closed (contains all limit points) and bounded. K₇ is posited to be compact.

### Ricci-Flat
Manifold with Ricci curvature tensor equal to zero. G₂ holonomy manifolds are automatically Ricci-flat, suitable for compactification.

### Harmonic Forms
Differential forms satisfying Laplace equation. Zero modes in dimensional reduction corresponding to 4D fields.

### Kaluza-Klein Reduction
Process of compactifying extra dimensions to derive lower-dimensional effective theory. Fields decompose into tower of modes.

## Particle Physics

### Standard Model
Current theory of particle physics describing electromagnetic, weak, and strong forces. Contains 19 free parameters in conventional formulation.

### Generation
Family of fermions. Standard Model has three generations:
- First: (u, d, e, νₑ)
- Second: (c, s, μ, νμ)
- Third: (t, b, τ, ντ)

### Gauge Coupling
Strength of force interaction. Three in Standard Model:
- α: Electromagnetic (fine structure constant)
- g₂: Weak force
- g₃ (or α_s): Strong force

### Fine Structure Constant (α)
Dimensionless coupling for electromagnetic interaction. α ≈ 1/137.036.

### Weak Mixing Angle (θ_W)
Parameter relating electromagnetic and weak forces. sin²θ_W ≈ 0.231.

### Strong Coupling (α_s)
Coupling constant for quantum chromodynamics. α_s(M_Z) ≈ 0.118.

### CKM Matrix
**Cabibbo-Kobayashi-Maskawa matrix**. 3×3 unitary matrix describing quark mixing between generations. Contains 4 independent parameters (3 angles, 1 phase).

### PMNS Matrix
**Pontecorvo-Maki-Nakagawa-Sakata matrix**. Analogous to CKM for neutrino sector. Contains 3 mixing angles (θ₁₂, θ₁₃, θ₂₃) and CP violation phase (δ_CP).

### CP Violation
Breaking of combined charge conjugation (C) and parity (P) symmetry. Observed in quark and neutrino sectors.

### Yukawa Coupling
Interaction strength between fermions and Higgs field, determining fermion masses.

### Higgs Mechanism
Process by which gauge bosons acquire mass through spontaneous symmetry breaking.

### VEV
**Vacuum Expectation Value**. Non-zero value of Higgs field in vacuum, v ≈ 246 GeV.

## Specific Observables

### N_gen
Number of fermion generations. Experimentally: 3. K₇ reproduces it through the integer identity (rank(E₈) + N)·b₂ = N·b₃, equivalently N = b₂/dim(K₇) = 21/7 = 3. This is a consistency check, not a prediction: no index theorem is known that produces it.

### δ_CP
CP-violating phase in neutrino mixing. The structure gives the integer dim(K₇)×dim(G₂) + H* = 7×14 + 99 = 197; reading it in degrees (the phase 2π·197/360) is a declared unit assignment. Current global fit (NuFIT 6.1): 212 (+26/−36)°.

### θ₁₂, θ₁₃, θ₂₃
Three neutrino mixing angles in PMNS matrix.
- θ₁₂ (solar mixing): measured sin²θ₁₂ = 0.3088; K₇ relation 4/13
- θ₁₃ (reactor mixing): measured sin²θ₁₃ = 0.02248; K₇ relation 11/496
- θ₂₃ (atmospheric mixing): octant unresolved. The K₇ relation is sin²θ₂₃ = 6/11 = 0.545 (θ₂₃ = 47.6°), in the upper octant; the current global fit prefers the lower octant (0.470), and 6/11 lies inside its 3σ range

### Q_Koide
Parameter in Koide formula relating charged lepton masses:
```
Q = (mₑ + mμ + mτ) / (√mₑ + √mμ + √mτ)²
```
Experimental: Q = 0.6666645(51). K₇ relation: Q = dim(G₂)/b₂ = 14/21 = 2/3 (+0.4σ). The relation dates from Koide (1982); it is one of four mutually incompatible lepton relations, none of which is selected.

### Ω_DE
Dark energy density as fraction of critical density. Experimental (Planck 2018): Ω_DE = 0.6847(73). K₇ relation: Ω_DE = ln 2 · (b₂ + b₃)/H* = ln 2 · 98/99 = 0.686146 (+0.2σ).

### H₀
**Hubble constant**. Current expansion rate of universe. Local measurements: ~73 km/s/Mpc. CMB measurements: ~67 km/s/Mpc. "Hubble tension" refers to discrepancy.

## Mathematical Constants

### π
Pi, ratio of circle circumference to diameter. π ≈ 3.14159...

### e
Euler's number, base of natural logarithm. e ≈ 2.71828...

### φ
**Golden ratio**. φ = (1 + √5)/2 ≈ 1.61803...
Appears in E₈ via McKay correspondence.

### ζ(3)
**Riemann zeta function at 3**. ζ(3) = 1 + 1/8 + 1/27 + ... ≈ 1.202.
Not used by the 33 relations. The zeta values that appear are ζ(11) and ζ(5), in n_s = ζ(11)/ζ(5).

### ln(2)
Natural logarithm of 2 ≈ 0.693. Enters the Ω_DE relation as one of the operations of the formula grammar.

## Physics Experiments

### PDG
**Particle Data Group**. International collaboration compiling experimental particle physics data. Standard reference for measured parameters.

### LHC
**Large Hadron Collider**. Particle accelerator at CERN. Discovered Higgs boson in 2012.

### Belle II
Particle physics experiment in Japan studying B mesons and precision measurements.

### DUNE
**Deep Underground Neutrino Experiment**. Future neutrino experiment in USA for precision measurements.

### T2K
**Tokai to Kamioka**. Long-baseline neutrino experiment in Japan.

### NOvA
**NuMI Off-Axis νₑ Appearance**. Neutrino experiment in USA.

## Mathematical Notation

### dim(G)
Dimension of Lie group or algebra G. Example: dim(E₈) = 248.

### rank(G)
Rank of Lie algebra G. Example: rank(E₈) = 8.

### Hⁿ(M)
n-th cohomology group of manifold M. Example: H²(K₇) = ℝ²¹.

### bₙ
n-th Betti number, dimension of Hⁿ. Example: b₃(K₇) = 77.

### |·|
Absolute value or cardinality (size of set).

### ⊕
Direct sum of vector spaces or algebras.

### ⊗
Tensor product.

### ∈
"Element of" (set membership).

### ∀
"For all" (universal quantifier).

### ∃
"There exists" (existential quantifier).

### ≈
Approximately equal.

### ≡
Identically equal or defined as.

### ∼
Of the same order of magnitude, or equivalent to.

## Greek Letters in K₇

### α (alpha)
Fine structure constant, α ≈ 1/137.


### γ (gamma)
Euler-Mascheroni constant.

### δ (delta)
CP violation phase (δ_CP) or small deviation.


### ζ (zeta)
Riemann zeta function; ζ(11)/ζ(5) appears in n_s.

### θ (theta)
Mixing angles (θ₁₂, θ₁₃, θ₂₃, θ_W).


### Ω (Omega)
Density parameters (Ω_DE for dark energy).

### φ (phi)
Golden ratio or angle.

## Acronyms

### GIFT
Geometric Information Field Theory, the former name of the K₇ framework (versions 1.0 to 3.4)

### SM
Standard Model (of particle physics)

### GUT
Grand Unified Theory

### QCD
Quantum Chromodynamics (strong force)

### QED
Quantum Electrodynamics (electromagnetic force)

### EW
Electroweak (unified electromagnetic and weak theory)

### SUSY
Supersymmetry

### CMB
Cosmic Microwave Background

### VEV
Vacuum Expectation Value

### RG
Renormalization Group

### UV
Ultraviolet (high energy)

### IR
Infrared (low energy)

### LO/NLO/NNLO
Leading Order / Next-to-Leading Order / Next-to-Next-to-Leading Order (perturbative expansion)

## Unit Conventions

### Natural Units
System where ℏ = c = 1. Energies, masses, and momenta have same dimensions.

### GeV
Giga-electron-volt, 10⁹ eV. Common energy/mass unit in particle physics.
- Proton mass: ~1 GeV
- Higgs boson mass: ~125 GeV
- Top quark mass: ~173 GeV

### MeV
Mega-electron-volt, 10⁶ eV.
- Electron mass: ~0.511 MeV
- Quark masses: few MeV to few GeV

## Formal Verification

### Lean 4
Theorem prover used to verify the arithmetic of the K₇ relations. The [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) repository (156 Lean files, 14 axioms: 4 imported from the literature and 10 interval certificates; 0 sorry) collects the 33 relations in `relations_v36_certified` and also covers E₈ root system, G₂ cross product properties, spectral theory, TCS bounds, Yukawa mass ratios, and the K3 Newton-Kantorovich certificate. It verifies arithmetic, not physics.

## Cross-References

For more detailed explanations:
- **Mathematical foundations**: See [S1: Foundations](Paper-S1-Foundations.html)
- **Particle physics background**: See [Main Paper](Paper-Main-Framework.html) Section 1
- **Experimental values**: See [Observable Reference](Observable-Reference.html)
- **Common questions**: See [FAQ](FAQ.html)

## Contributing

This glossary is continuously updated. To suggest additions or corrections:
1. Open issue at https://github.com/Arithmon/K7/issues
2. Tag as "documentation"
3. Specify term and proposed definition

---

Last updated: v3.6
