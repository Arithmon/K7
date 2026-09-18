# Physica Scripta submission — skeleton

**Working title (pick one, all avoid "Standard Model", "constants", "GIFT/K7 framework"):**

1. *Certified spectral geometry of an explicit torsion-free G₂ structure on a K3 × T² neck*
2. *Laplacian spectrum and harmonic forms of a computer-certified G₂ neck metric*
3. *A Newton–Kantorovich-certified G₂ neck model and its Kaluza–Klein spectrum*

**Article type:** Paper (regular research article), Mathematical physics section.
**Target length:** 18–22 journal pages, 5 figures, 6 tables, 2 appendices.
**Sources merged:** Zenodo A (`g2_certified_neck.pdf`, 20 pp.) condensed to ~35 %, Zenodo B (`g2_spectral.pdf`, 11 pp.) kept at ~90 %, plus one new result (§7 below).

Principle: one self-contained paper. Everything the spectral sections use from A is restated in the paper; nothing is "see companion paper [A]" for a load-bearing quantity.

---

## 0. Abstract (draft, ~220 words — PS has no hard limit, keep ≤ 250)

We construct an explicit G₂ structure on the twisted-connected-sum-type neck model K3 × T² × [0, 1], parametrised by 168 Chebyshev–Cholesky coefficients and an asymptotically cylindrical decay rate, and certify by Newton–Kantorovich interval arithmetic the existence and uniqueness of a nearby torsion-free G₂ structure (contraction parameter h ≤ 1.43 × 10⁻⁹, metric correction |δg|/g ≤ 1.35 × 10⁻⁷). The certified metric is adiabatically of product type to an error of 2 × 10⁻³, which reduces the seven-dimensional Hodge Laplacians to families of one-dimensional Sturm–Liouville problems. We compute the scalar spectral gap λ₁ = 0.12461 ± 0.00016 [→ replace by rigorous enclosure, §7], the Weyl exponent of the full Kaluza–Klein tower (α = 3.46 ± 0.04 against 7/2), 22 671 levels below λ = 20 with Poisson level-spacing statistics, and the near-harmonic 2- and 3-forms, whose multiplicities (21, 77) and whose 2-form intersection signature (3, 18) are the ones expected of a compact extension with Betti numbers (b₂, b₃) = (21, 77). We prove that product-type Ricci-flat G₂ metrics satisfy spectral democracy (equal Weitzenböck spectra on the three form sectors) and verify it numerically to 10⁻⁵. All results are properties of the explicit neck metric; their interpretation on a closed compact G₂ manifold is conditional on the existence of such an extension, which we do not claim. Certificates, code and data are public.

**Keywords:** G₂ holonomy · special holonomy metrics · spectral geometry · Hodge Laplacian · Kaluza–Klein spectrum · Newton–Kantorovich theorem · computer-assisted proof · interval arithmetic

---

## 1. Introduction (≈ 1.5 pages)

PS requires the broad context up front for specialist submissions. Three paragraphs, in this order:

- **1.1 Broad context (for the generalist reader).** Explicit metrics with special holonomy are almost never known in closed form; existence theorems (Joyce, Kovalev, CHNP) are non-constructive. Spectral data on such spaces matter beyond geometry: the Laplacian spectrum fixes the Kaluza–Klein mass tower and the harmonic forms fix the low-energy field content in eleven-dimensional supergravity on G₂ manifolds (cite Acharya–Gukov, and one modern KK-reduction review). Numerical special-holonomy metrics have become an active field (Donaldson algebraic approximations, machine-learned CY/G₂ metrics, Laplacian-flow numerics) — cite 4–6 recent papers so the referee sees the field, not just you.
- **1.2 What is new here.** (i) A neck-model G₂ structure whose torsion-free deformation is *certified* rather than numerically converged; (ii) the first spectral computation (gap, Weyl law, KK tower, harmonic forms, intersection form) on a certified G₂ neck; (iii) a democracy theorem for product-type Ricci-flat G₂ metrics with numerical verification; (iv) [new, §7] a rigorous enclosure of λ₁.
- **1.3 Scope statement, one paragraph, no hedging beyond this.** The model is a neck, not a compact manifold. The seam geometry is adapted to a conjectural compact extension with (b₂, b₃) = (21, 77); that pair is realised at the topological/lattice level by a Joyce–Karigiannis ℤ₂³ construction (cite) but no compact metric is constructed here. Every statement in the paper is about the explicit neck metric g*.
- **1.4 Outline.** One sentence per section.

*Cut from A:* §1.4 "Relation to existing work" as a separate section — fold into 1.1. *Cut from B:* the "Note on related work" on Zhou & Zhou — move to Discussion or drop; a referee who doesn't know that reference gains nothing.

## 2. Geometric setting (≈ 1.5 pages) — from A §2, condensed

- 2.1 G₂ structures, torsion, torsion-free ⇔ Ricci-flat with holonomy ⊆ G₂ (three sentences + one reference; no octonion preamble).
- 2.2 The TCS neck model K3 × T² × [0, 1]: coordinates (s, θ, χ, y), the ACyl ends, what "seam sector" means.
- 2.3 The topological target (21, 77): where it sits relative to the CHNP database (nearest neighbour at distance 7.6, parity exclusion of orthogonal TCS), and the ℤ₂³ lattice realisation. **Keep this to half a page.** It is context, not a result of this paper.
- 2.4 Assumptions, listed and numbered (A1–A4): fixed K3 fibre input, adiabatic product ansatz, boundary conditions at s = −2 and s = 3, normalisation det g = 65/32 *imposed*. Number them so the referee and you can point at them later.

## 3. The explicit metric and its certificate (≈ 3.5 pages) — from A §3–5, heavily condensed

- 3.1 Parametrisation: Chebyshev–Cholesky, 168 + 1 parameters, ACyl extension.
- 3.2 Torsion norms and the G₂ representation-theoretic split (W₁ ⊕ W₇ ⊕ W₁₄ ⊕ W₂₇); torsion at the final iterate (table).
- 3.3 **Theorem 3.1 (NK certificate).** Statement with all three ingredients (invertibility bound β, residual η, Lipschitz ω), the two values of h (analytical β = 0.321 → h ≤ 8.95 × 10⁻⁹; numerical β = 0.02961 → h ≤ 1.43 × 10⁻⁹), and the 1D → 7D promotion via the Fréchet bound on the K3 fibre (‖T(g*)‖_{C⁰} ≤ 1.59 × 10⁻³). State explicitly: *relative to the fixed K3 fibre input*.
- 3.4 The adiabatic decomposition of g*: the three effective sectors (g_ss = 19/6, g_T² = 7/6, g_K3 ≈ 64/77), and **Proposition 3.2** (adiabatic error ε_ad = 2 × 10⁻³ ⇒ |δλ|/λ ≤ 0.78 %). This proposition is the hinge of the whole paper; give it a full proof or a full reference to the certificate file, not a sketch.
- 3.5 What is exact, what is certified, what is numerical: a three-column table (quantity / status / where checked). Reuse the "epistemic status" device from the FoP paper; PS readers will like it.

*Cut from A entirely:* §3.7 reconstruction algorithm (→ Appendix B or repository), §3.8 "complete metric decomposition" (→ one table), the five-constant "approximate structure" narrative (19/6, 7/6, 64/77, 65/32, 2π√(6/7)). Keep the rational values as fitted effective parameters with their deviations; **do not present them as identities**. That paragraph is where a referee smells numerology, and the spectral paper's own Remark says the spectral results do not depend on it.

## 4. Scalar Laplacian spectrum (≈ 3 pages) — from B §3, kept

- 4.1 Sturm–Liouville reduction, eq. (2) of B, discretisation (Chebyshev collocation, N = 200–1600, Neumann and Dirichlet).
- 4.2 Spectral gap: Table 1 of B, Richardson extrapolation (appendix), the analytical expression λ₁ = π²/(L² g_ss) = 6π²/475 **labelled as a consistency check on the certified parameters, not a prediction** (B already says this; keep the sentence verbatim).
- 4.3 Weyl law: seam channel α = 1.998 (trivial, say so), full tower α₇D = 3.460 ± 0.040 vs 7/2 (the non-trivial check). Figure 1(a).
- 4.4 KK tower: 22 671 levels below λ = 20, sector hierarchy (Table 2 of B), Poisson vs GOE level spacing with χ² values. Figure 1(b). Add one sentence on why Poisson is *expected* for an adiabatically separable system (so it reads as a consistency check, not a discovery).

## 5. Harmonic forms and intersection structure (≈ 3 pages) — from B §4, **rewritten in one place**

This is the section a good referee will attack. Rewrite the framing before touching the numbers:

- 5.1 Construction of the near-harmonic 2-forms by lifting K3 (1,1)-classes with radial profiles f_I(s); the profile solver (currently a 3-layer MLP variational ansatz). **Add a deterministic cross-check**: solve the same radial ODE by Chebyshev collocation and report agreement; a neural ansatz alone for a harmonic-form profile will draw a "why not just solve the ODE?" from any mathematical-physics referee.
- 5.2 **Why 21 and not 22 (or 23).** The plain product K3 × T² has 22 + 1 harmonic 2-forms. The paper must state, as a lemma with proof, which classes fail the boundary/TCS matching at the ends and why (the class that shows up as λ₂₂ ≈ first non-zero eigenvalue, and the T² volume form). If the argument is "invariant part under the ℤ₂³ action", make the action explicit on H²(K3). Without this, "spectral confirmation of b₂ = 21" reads as constructed-to-order.
- 5.3 Same for the 3-forms: H³(K3 × T²) = H²(K3) ⊗ H¹(T²) has rank 44 on the bare product; the 77 near-harmonic 3-forms need the same explicit accounting (22 + 55 in the ℤ₂³ Betti formula). Give the decomposition of the 77 by origin (fibre class ⊗ circle, seam-supported, etc.).
- 5.4 Intersection form on the 21 forms: signature (3, 18), SD/ASD split, gap 2 210. State that this is the restriction of the K3 lattice (3, 19), and give the actual 21 × 21 matrix (or its Gram determinant and diagonal blocks) in Appendix A.
- 5.5 Gap ratios (14 635 for Δ₂) and robustness under the 0.78 % perturbation budget (B §6.3 argument, moved here).

*Cut or quarantine:* the conjectural scaling V_min ≈ √(Vol/11) for associative cycle volumes (B §4/§6.1 item 6). It has "no derivation" by the paper's own words; in PS it is one more unexplained numerical coincidence. Either drop it or put one sentence in "Open questions".

## 6. Spectral democracy (≈ 1.5 pages) — from A §6 (theorem) + B §5 (numerics)

- 6.1 Weitzenböck identity on product metrics; **Theorem 6.1** with full proof (A §6.2). This is the paper's one clean analytical result; give it room.
- 6.2 Numerical verification to 10⁻⁵ on g*: table of the three sector spectra.

## 7. New result for this submission (≈ 1.5 pages) — to be produced

PS will accept a paper whose content exists as a Zenodo preprint, but "enough new results" is their stated bar and the two preprints are a year old by submission. One addition, chosen to fix the paper's own stated limitation ("the error bar ±0.0001 is a numerical estimate, not a rigorous bound"):

- **7.1 Rigorous enclosure of λ₁.** Interval Sturm–Liouville eigenvalue enclosure on the (0,0,0) seam channel (e.g. a Rayleigh–Ritz upper bound + a Temple/Lehmann–Goerisch or Kato lower bound, evaluated in interval arithmetic on the certified coefficient enclosures). Output: λ₁ ∈ [ℓ, u] with u − ℓ ≲ 10⁻⁵, machine-checked (Lean `native_decide` on the final rational inequality, same pattern as the K3 NK note). Then the abstract sentence becomes "λ₁ is rigorously enclosed in [ℓ, u]".
- **7.2 (optional, if cheap)** The same enclosure for the first non-zero eigenvalue of Δ₂, which turns the "gap ratio 14 635" into a certified statement.

If 7.1 turns out too expensive: fall back to publishing the Richardson error analysis honestly *and* a convergence study against grid refinement of the 7D operator without the adiabatic split at low N, which would independently test Proposition 3.2. But a certified λ₁ is the headline PS referees will remember.

## 8. Discussion (≈ 1.5 pages)

- 8.1 Summary of certified vs numerical results (restate the three-column table in words).
- 8.2 Relevance for KK reductions on G₂ spaces: lightest KK mass, 4D field content, coupling structure from the intersection form. **Three sentences, general, no particle-physics numbers.**
- 8.3 Limitations, in this order: neck ≠ compact manifold; K3 input fixed (certificate is relative); adiabatic ansatz; det g imposed; harmonic-form counts depend on the boundary-matching lemma of §5.2.
- 8.4 Open questions (B §6.4, keep three).

## Appendices

- A. Convergence tables (B Appendix A) + the intersection matrix.
- B. Reconstruction algorithm and file map: which certificate JSON / Lean declaration backs which number in the text.

## Figures and tables (target)

| # | Content | Source |
|---|---|---|
| Fig 1 | Torsion decay across NK iterations, per W_i component | A |
| Fig 2 | Metric components g_ss(s), g_T²(s), K3 mean eigenvalue vs s | A |
| Fig 3 | Weyl exponent convergence + level-spacing histogram | B Fig 1 |
| Fig 4 | Δ₂ and Δ₃ low-lying spectra, gap visible on log scale | B |
| Fig 5 | Enclosure of λ₁: Rayleigh–Ritz upper vs lower bound vs N | new |
| Tab 1 | NK certificate ingredients (β, η, ω, h) two ways | A |
| Tab 2 | Status table: exact / certified / numerical | new |
| Tab 3 | Seam-channel eigenvalues + Richardson | B Tab 1 |
| Tab 4 | KK sector hierarchy | B Tab 2 |
| Tab 5 | Harmonic form counts by origin (21 = …, 77 = 22 + 55 = …) | new |
| Tab 6 | Democracy check on three sectors | B |

## Referee-risk list (write the paper against these)

1. "Why 21 and 77 on a product neck?" → §5.2–5.3 lemma. **Highest risk.**
2. "The NK certificate is relative to a neural-network K3 input; what is certified about the K3 fibre itself?" → say it plainly in Theorem 3.1 and Limitations; point to the box-local Calabi–Yau residual bound only if the K3 companion paper is public by then, otherwise don't lean on it.
3. "det g = 65/32, 19/6, 7/6, 64/77: are these fits or claims?" → fitted effective values with deviations, §3.4; no "identity" language anywhere.
4. "Neural ansatz for harmonic profiles" → deterministic ODE cross-check, §5.1.
5. "What is new relative to the Zenodo preprints?" → §7 + the merged, self-contained presentation; say so in the cover letter and cite both DOIs.
6. "Is this the same author's E₈/Standard-Model programme?" → the paper should not mention it. One neutral sentence in 2.3 that the Betti pair is of interest for M-theory compactifications with three chiral generations is the maximum; anything more invites a referee from the wrong side.

## PS-specific checklist

- **OA route:** decline gold; green route, 0 €. Zenodo preprints are allowed (not prior publication); the accepted manuscript can go on Zenodo/arXiv after the IOP embargo. Check the current embargo length on the journal page before submitting.
- **Anonymity:** author's choice. Double-anonymous is attractive for an unaffiliated author, but it requires anonymising self-citations — the Zenodo DOIs and the repository URLs identify you. Either (a) single-anonymous and cite A/B openly, or (b) double-anonymous with "certificates available in an anonymised bundle" (the MATH-AI repository already shows you know how to do this). Decide before writing the reference list.
- **Cover letter, one page:** what is certified, what is numerical, what is new vs the preprints, why Physica Scripta (mathematical-physics scope, computer-assisted methods, broad readership), and a sentence that the paper makes no claim about a compact manifold.
- **Suggested referees:** 3–4 names from numerical special holonomy / computer-assisted proofs in geometry. Not people you have emailed about the programme.
- **Data availability statement:** Zenodo DOIs for certificates and code, Lean repository tag frozen at submission.
- **AI-use declaration:** IOP requires disclosure of generative-AI tools in the manuscript (not as authors); reuse the wording from the FoP paper.
- **Style:** IOP LaTeX class `iopart`, numbered references (Vancouver-style in IOP), figures as separate files, no colour-only encoding.

## Work plan

1. Freeze a `physica-scripta` branch in `Arithmon/K7` with the two source PDFs and this skeleton.
2. Write §5.2–5.3 lemma first (it decides whether the harmonic-form section survives as is).
3. Run the λ₁ enclosure (§7.1); if it works, it is the abstract's first sentence.
4. Merge A and B into `iopart` following the section map above; target 20 pages.
5. Two review passes with the referee-risk list as the rubric, then the FoP-style status table.
6. Cover letter, referee suggestions, submit via ScholarOne.
