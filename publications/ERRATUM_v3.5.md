# Erratum — GIFT / K₇ framework v3.5

**Issued** 2026-08-22. **Applies to** the v3.5 release
(Zenodo concept `10.5281/zenodo.16891489`, version record `21296168`,
deposited 2026-07-10) and to the copies of those sources distributed in this
repository under `publications/papers/`.

**This erratum does not trigger a new deposit.** The v3.5 record stands as
published; the corrections below are recorded here and will be integrated
into **v3.6**. Nothing in `publications/papers/` has been regenerated — the
sources are left as deposited, so that this erratum can be read against them,
with two exceptions, both limited to links and identifiers: the live Lean links
repointed to `Arithmon/K7-Lean` on 2026-07-17 (one line each in the main text
and supplements S1, S2, markdown only), and the three [E] citations corrected
on 2026-10-01 (section 4).

---

## 1. The closed-form Calabi–Yau residual bound does not bound what it says

**Where.** `publications/papers/markdown/k7_framework_3_5_main.md` lines 131
and 760; `…/k7_framework_3_5_S1_foundations.md` line 528; and the
corresponding passages in `publications/papers/tex/k7_framework_3_5_main.tex`
and `…_S1.tex`.

**What is written.** That the Ricci-flat Kähler (Calabi–Yau) metric on the
Z₂³-equivariant K3 fibre admits an explicit closed-form approximation whose
order-3 residual (667 parameters) satisfies an *interval-rigorous,
assumption-free, machine-checked* bound

    Var(log R) ≤ ε₃ = 1309/10⁷ ≈ 1.309 × 10⁻⁴ < 10⁻³

on a frozen 4000-point Krawczyk-certified witness, formalised in Lean 4
(`K3ClosedFormWitness`).

**What is wrong.** The 667-parameter witness was fitted **and evaluated**
with the contraction `V† H V`, which is not the holomorphic pullback of the
ambient (1,1) form to the K3; the correct pullback is `Vᵀ H V̄`. That metric
convention was retracted on **2026-07-13**, and the defect was measured
**directly on this witness** on **2026-07-19**, over the same 4000 points:

| quantity | value |
|---|---:|
| `Var(log R)` over all 4000 points, code convention — *what ε₃ bounds* | 1.309 × 10⁻⁴ |
| `Var(log R)` on the 3478 points positive-definite in **both** conventions, code | 1.445 × 10⁻⁴ |
| `Var(log R)` on those same points, **correct pullback** | **5.315 × 10⁻¹** |
| ratio true / code | **3677** |
| `log det_code − log det_true` | mean 0.534, std 0.730 |
| positive-definite census | 4000 (code) vs **3478** (correct pullback) |

So ε₃ bounds an **auxiliary quantity**, not the Calabi–Yau residual of a
Kähler metric on the K3. And in the correct convention the ansatz is **not**
close to Ricci-flat: 5.3 × 10⁻¹ is not a small residual, and 522 of the 4000
points do not even carry a positive-definite form.

**What still stands.** The arithmetic and the surface-level certification are
untouched:

* the Lean theorems are `native_decide` statements about integers and about
  the aggregate of the 4000 serialised rational endpoints — they remain valid;
* the Krawczyk–Rump certification that each box contains an **exact** common
  zero of the defining equations is a statement about the **surface**,
  independent of any metric convention;
* the *method* — the frame-invariant determinant identity, the rank-one
  caching, forward interval arithmetic, and the Lean re-computation of the
  variance envelope from rational endpoints — transfers unchanged.

The public Lean modules carry the matching correction
(`GIFT/Foundations/K3ClosedFormWitness.lean` and
`…/K3ClosedFormBoxEnclosures.lean` in the `K7-Lean` repository, 2026-08-22).

**What v3.6 must do.** Restate the passage as a bound on the auxiliary
quantity, or re-establish the certificate on the current metric datum (the
degree-3 witness v2, `holomorphic_pullback_VT`, gauge det M = 1, frozen
2026-07-16). The honest target for a re-run on the current datum is of order
10⁻³ – 10⁻², not 1.3 × 10⁻⁴.

---

## 2. The datum-level instantiation of [E] is no longer realisable as posed

**Where.** The passages of `k7_framework_3_5_main.md` (§ around line 131 and
the two-layer claim boundary of §9) that discharge the datum-level analytic
existence scheme at the normalised datum 𝒟₀ of the companion paper [E],
with `R₀(𝒟₀) ≤ 4.9 × 10³`.

**What is wrong.** On **2026-08-19** a Stokes-type obstruction (internally
`P3-R1`, ratified) established that the **global single-root** datum 𝒟₀ of
[E] is not realisable as posed.

**What still stands.** The **conditional theorems** of [E] are unaffected —
they are conditional on the two-slot external structure pack, and that
conditionality is exactly what the obstruction touches at the level of
*instantiation*, not of proof. Corollary B remains valid **as a computation**;
what fails is that its datum is no longer available in the single-root global
form. A multi-root salvage is in progress.

**What v3.6 must do.** Present the datum-level layer as conditional on a
datum that is *not currently instantiated*, rather than as discharged at 𝒟₀.

---

## 3. Citation hygiene noted for v3.6 (not an error of substance)

The v3.5 sources cite the **version** DOI `10.5281/zenodo.19893371` of the
companion spectral-geometry paper [B] 31 times, and never its **concept** DOI
`10.5281/zenodo.18920367`. The concept DOI is the one that should be cited:
it resolves to the latest version. To be corrected in v3.6.

---

## 4. Paper [E] is cited by the DOI of its dataset, not of the preprint (added 2026-10-02)

**Where.** Three places in the v3.5 main text: the "Established at the
datum" item of the claim boundary, the "Companion analytic paper [E]"
paragraph, and the bibliography entry **[E]**, in
`k7_framework_3_5_main.md` and in `k7_framework_3_5_main.tex`, and therefore
in the deposited PDF.

**What is written.** "concept DOI 10.5281/zenodo.21209413" for the paper [E].

**What is wrong.** The two Zenodo records of [E] were swapped in our
citations. According to the Zenodo API (`resource_type`, files):

| record | concept DOI | version DOI | type | content |
|---|---|---|---|---|
| **[E], the preprint** | **10.5281/zenodo.21215956** | 10.5281/zenodo.21215957 | Preprint | main paper (68 pp) + supplement (25 pp), PDF |
| [E], its dataset | 10.5281/zenodo.21209412 | 10.5281/zenodo.21209413 | Dataset | data + verification scripts, tar.gz |

So the number printed in v3.5 resolves to the **dataset**, and it is a
*version* DOI, not a concept DOI. The paper should be cited as
**10.5281/zenodo.21215956**. The swap was found on 2026-10-01 by
cross-checking our DOI registry against the author's ORCID record.

**Already corrected.** On 2026-10-01 (commit `366f69e`), the repository
surfaces (README, CITATION, STRUCTURE, wiki, `publications/papers/README.md`)
and the three passages of the distributed copies
`publications/papers/markdown/k7_framework_3_5_main.md` and
`publications/papers/tex/k7_framework_3_5_main.tex` were changed to cite
21215956. Apart from the Lean links of 2026-07-17 (see the header), these
are the only changes to the copies since the deposit. The deposited PDF and
the Zenodo record of v3.5 are immutable and keep 21209413.

**What v3.6 must do.** Cite [E] by its preprint concept DOI 21215956. Where
the dataset is meant, cite it explicitly as such (concept DOI 21209412).

---

## 5. The fine-structure relation is labelled at the wrong scale (added 2026-10-02)

**Where.** Supplement S2, §20b (relation #18), whose formula is written
α⁻¹(M_Z) = (248 + 8)/2 + 99/11 + (65/32)(1/61), in
`k7_framework_3_5_S2_derivations.md` and `k7_framework_3_5_S2.tex`, and the
row α⁻¹(M_Z) of the observable reference (wiki, corrected on 2026-10-02).

**What is wrong.** The value is compared with 137.036, which is the inverse
fine-structure constant **at low energy**, in the Thomson limit, α⁻¹(0). The
running coupling at M_Z is a different quantity (about 127.93 in the
five-flavour MS-bar scheme, PDG). The main text is already consistent with
the low-energy reading: §5.4 calls 137.033 "the topological low-energy value
α_em⁻¹" and keeps it distinct from the M_Z values of the RGE chain. The label
in S2 contradicts it.

**What still stands.** The relation itself, 267489/1952 = 137.033299…, and
its classification (STRUCTURAL: it uses the imposed normalization
det(g) = 65/32).

**How to read the agreement.** Against α⁻¹(0) = 137.035999177(21) (CODATA
2022), the deviation is −19.7 ppm (0.002%). That is a numerical proximity,
not an agreement within experimental uncertainty: the measurement is about
10⁵ times more precise than the gap. The internal observable record also
carried an unsourced uncertainty of ±0.0001. It now cites CODATA 2022.

**What v3.6 must do.** Write the relation as α⁻¹(0), and state the
comparison as above.

---

## 6. p₂ = 2 is not a Pontryagin class (added 2026-10-16)

**Where.** `publications/papers/markdown/k7_framework_3_5_main.md` line 458
("the Pontryagin ratio p₂ = dim(G₂)/dim(K₇)"); `…/k7_framework_3_5_S2_derivations.md`
line 655 ("Pontryagin class contribution (spin structure correction)"), the
physical-interpretation paragraph of θ₂₃ that follows (line 659), and line
1353 (Fibonacci table); the corresponding passages of the `.tex` sources.

**What is wrong.** The constant p₂ = dim(G₂)/dim(K₇) = 14/7 = 2 is called a
Pontryagin class, ratio or number. For a 7-manifold, the second Pontryagin
class p₂(TK₇) lies in H⁸(K₇; ℤ), which vanishes for dimensional reasons, and
there is no second Pontryagin number to integrate. The ratio 14/7 is neither.
The reading of (b₃ − p₂)/H* in θ₂₃ as "spin-corrected 3-cycles", with "the
Pontryagin correction accounting for the spin structure", has no basis and is
withdrawn. The error was pointed out by a referee.

**What still stands.** The value p₂ = 2 and every formula that uses it. The
symbol is kept for continuity; its definition is the ratio dim(G₂)/dim(K₇),
which other passages of the paper already call the binary duality factor.

**What v3.6 must do.** Call p₂ the binary ratio dim(G₂)/dim(K₇) wherever it is
named, with no topological-class reading.

---

## 7. Further statements found wrong in a full audit (added 2026-10-17)

A line-by-line audit of the v3.5 sources against the formal core, the DOI
registry and the sections above found six more statements that are wrong as
written. None changes a predicted value.

**7.1 Axiom accounting.** `k7_framework_3_5_main.md` lines 13, 25, 72, 703
and 718 (and supplements S1, S2 and S3, which repeat them) say that the Lean
core has 15 classified axioms, "of which 4 external data packages":
`K7_analysis_data`, `K7_spectral_data`, `literature_package` and `KK_YM_EFT`.
The total of 15 was correct at deposit, but the list was not: three of the four
named axioms had been eliminated on 2026-04-13 (K7-Lean `7b28895`,
`3312228`). The 15 axioms at deposit were:
- the four prediction-chain axioms: `cheeger_inequality`, `literature_package`,
  `spectral_upper_bound` and `neck_dominates`;
- ten interval certificates: `det_g_at_half` and `K3_eigenvalue_0…3`, each
  with its `_bracketed` form;
- `PSLQ_null_in_TCS_basis`.

The last was discharged on 2026-09-08 (K7-Lean #163). The current core has
**14 axioms** and 0 sorry.

**7.2 The KK spectral bridge.** Line 720 says that the 4D mass gap is
"formally conditional on KK_YM_EFT alone". `KK_YM_EFT` is no longer an axiom:
it is a theorem whose type is arithmetic (`KKSpectralBridge.lean`), and the
physical content of the bridge is not in that type. The sentence is withdrawn.

**7.3 The methodology paper.** Lines 596 and 1054 of the main text, and line 9
of S4, cite Zenodo `10.5281/zenodo.20666879` as the methodology paper on
counting coincidences. That DOI is version 1.0 of the **dataset** "Counting
Coincidences — frozen inputs" (concept `10.5281/zenodo.20666878`). The paper
itself is the preprint "A reproducible standard for arithmetic coincidence
claims in fundamental physics", concept `10.5281/zenodo.20728964`. Line 604
cites the dataset as the frozen-inputs record, which is correct.

**7.4 Hypothesis (L4).** Lines 825 and 831 list (L4) among the hypotheses
that are "currently OPEN". For the single-root datum 𝒟₀ of [E], (L4) is
obstructed, not open: this follows from §2 above. A global statement needs
(C.1), (J) **and** a realisable datum with its own (L4).

**7.5 Global properties of K₇ stated as facts.**
- Lines 520–521 of S1 list "G₂ holonomy: Hol(g*) = G₂" and "Ricci-flat:
  Ric(g) = 0" as properties of the manifold. No global torsion-free G₂
  structure has been constructed (main text, §9).
- Lines 506 and 528 of S1 say that (b₂, b₃) = (21, 77) is "certified by the
  NK metric". The Newton–Kantorovich certificate [A] concerns the neck metric.
  The Betti numbers come from the topological route (Joyce–Karigiannis); the
  spectral count of [B] is consistent with them, and does not certify them.

**7.6 κ_T and Joyce's regime.** Line 732 of S1 says that the bound κ_T = 1/61
"constrains ‖δφ‖, placing the manifold within Joyce's perturbative regime
where a torsion-free solution exists". No argument connects the number 1/61
to Joyce's smallness hypothesis. The sentence is withdrawn.

**What v3.6 must do.**
- State 14 axioms, with the list above.
- Drop the `KK_YM_EFT` sentence.
- Cite `10.5281/zenodo.20728964` for the methodology.
- Write (L4) as obstructed for 𝒟₀.
- State the global properties of K₇ as open.
- Remove the κ_T paragraph.

---

## 8. Two internal inconsistencies, and how v3.6 resolves them (added 2026-10-17)

**8.1 The charged-lepton relations are mutually inconsistent.** The paper
states four relations for two independent mass ratios: m_μ/m_e = 27^φ
(= 207.0119), m_τ/m_e = 3477, Koide's Q = 2/3, and m_μ/m_τ = 10/168. They
cannot all hold at the precision quoted. With m_e = 0.51099895 MeV:
- Q(1, 27^φ, 3477) = 0.666546, so Q − 2/3 = −1.2 × 10⁻⁴;
- m_τ = 3477 m_e = 1776.743 MeV, which lies 2.1σ below the measured value,
  1776.93 ± 0.09 MeV;
- Q = 2/3 taken together with 27^φ would force m_τ = 1778.88 MeV.

**v3.6 takes m_μ/m_e = 27^φ as the primary relation**, and presents the other
three as approximate, with their deviations stated.

**8.2 The gauge couplings sit at no common scale.**
- §4.1 (line 243) compares sin²θ_W = 3/13 directly with its measured value at
  M_Z, but §5.3 takes 3/13 as a boundary condition at M_GUT and runs it down
  with two-loop MSSM RGEs.
- The B-test theorem (line 440) labels α_em⁻¹ = 91√2 at M_Z, while line 446
  speaks of the "B = 7/5 exact scale".
- Since §5 of this erratum, α⁻¹ is read at q² = 0.

**v3.6 reads sin²θ_W and α_s at M_Z.** It withdraws the reading of 3/13 as a
GUT boundary condition, together with the RGE chain built on it. It keeps
α⁻¹ = 137.033… as a low-energy (q² = 0) relation, and it makes no claim that
the three couplings form a triplet at a common scale.

---

## 9. The Joyce–Karigiannis route does not realize (b₂, b₃) = (21, 77) (added 2026-10-22)

**Where.** `publications/papers/markdown/k7_framework_3_5_main.md` line 11
(abstract: "a Joyce–Karigiannis route realizing (b₂, b₃) = (21, 77)") and line
131 (§2.3, "a Joyce-Karigiannis (JK) Z₂³ orbifold construction [43] *does*
produce (b₂, b₃) = (21, 77)"); `…/k7_framework_3_5_S1_foundations.md` line 15
(abstract) and §8.4 (lines 530–575, in particular line 555, "quotient
cohomology b₂(T³ × K3 / Z₂³) = 0 and b₃(T³ × K3 / Z₂³) = 22", and line 566, a
Picard-rank-1 K3); `…/k7_framework_3_5_S2_derivations.md` lines 42 and 69; the
corresponding passages of the `.tex` sources.

**What is wrong.** The Betti count adds the fixed-locus contributions
(b₀, b₁) = (21, 55) to a quotient cohomology (b₂, b₃) = (0, 22) of
(T³ × K3)/ℤ₂³. That quotient cohomology is incompatible with the group action
the paper states. The action is diagonal, so the rational cohomology of the
quotient is the invariant part of H*(T³ × K3); the stated character of ℤ₂³ on
H²(K3) has multiplicities (5, 5, 2, 2, 2, 2, 2, 2), so dim H²(K3; ℚ)^G = 5, and
the Künneth formula then gives b₂ ≥ 5 and b₃ ≤ 16 for every compatible torus
action (the product action gives (b₁, b₂, b₃) = (1, 6, 16)). With the same
fixed-locus contributions and resolution formula, the resolved manifold would
have b₂ ≥ 26 and b₃ ≤ 71, not (21, 77). The stated involution profile also
requires a K3 of Picard rank at least 17, not 1. The Lean module
`JoyceKarigiannisConstruction.lean` verified the arithmetic of the Betti
formula from the erroneous quotient input and does not bear on this.

**How it was checked.** The audit
`docs/openwave-candidate/K7_P2_JK_postfreeze_cohomology_audit_2026_09_16.md`
in this repository, with the standard-library checkers
`check_k3_jk_quotient_cohomology.py` (all 8³ = 512 torus-character triples)
and `check_k3_jk_character_gate.py` (Picard rank ≥ 17), rerun on 2026-10-22.
The audit dates from 2026-09-16 and was not carried into the paper until an
outside review of the v3.6 draft pointed to it; the delay is ours.

**What still stands.** Nothing in the 33 relations uses this route: they use
the integers (21, 77) as posited inputs. The route is invalidated as stated;
this does not show that every Joyce–Karigiannis construction, or every
construction of a compact G₂ manifold with Betti numbers (21, 77), is
impossible.

**What v3.6 does.** It states that no construction of a compact G₂ manifold
with (b₂, b₃) = (21, 77) is currently known, and that the proposed route does
not realize the pair.

---

## 10. The scaling of the reference G₂ form is wrong (added 2026-10-22)

**Where.** `publications/papers/markdown/k7_framework_3_5_S1_foundations.md`
§11.1 (line 712), §11.5 (line 815), §12.3 (lines 855–863) and §12.5 (line 878).

**What is wrong.** The text scales the standard form, φ ↦ cφ, with the law
g ↦ c²g, and takes c = (65/32)^{1/14} so that det g = 65/32. The metric of a
positive 3-form scales as g_{cφ} = c^{2/3} g_φ (the defining identity
(ι_xφ) ∧ (ι_yφ) ∧ φ = 6 g(x, y) vol_g scales by c³ on the left and by λ^{9/2}
on the right when g ↦ λg). With the correct law, (65/32)^{1/14} φ₀ induces
det g = (65/32)^{1/3} ≈ 1.2664, not 65/32. The reconstruction
g_ij = (1/6) Σ φ_ikl φ_jkl of §12.3 contracts indices with a background
Euclidean metric; it is not a general formula for g_φ, and it is the source
of the wrong law.

**What still stands.** The metric written in the text, (65/32)^{1/7} I₇ in
the fixed coframe, is the metric with determinant 65/32; it is induced by
φ_ref = (65/32)^{3/14} φ₀, not by (65/32)^{1/14} φ₀. The normalization
det g = 65/32 remains imposed, not derived (§7.6 of this erratum, and v3.6).

**What v3.6 does.** It states the scaling law, gives φ_ref = D^{3/14} φ₀ and
g_ref = D^{1/7} g_{φ₀} for D = 65/32, uses the intrinsic reconstruction of the
metric from φ, and says for which metric the coframe is orthonormal.

---

## 11. Update to §8.1: v3.6 declares no primary lepton relation (added 2026-10-22)

Section 8.1 announced that v3.6 would take m_μ/m_e = 27^φ as the primary lepton
relation. That choice was made after the values were known and has been
withdrawn: **v3.6 declares none of the four lepton relations primary.** All
four are stated as approximate, with their deviations; m_μ/m_e = 27^φ is
excluded as an exact equality at current precision and kept as a numerical
proximity. Section 8.2 is unchanged.

---

## Provenance

Sections 1–3 were surfaced by an internal audit of the corpus on
2026-08-22 and verified against the primary measurements before being written
here. The measurement underlying §1 is dated 2026-07-19 and predates this
erratum by five weeks; the delay is a process failure of ours, recorded as
such, and it is what prompted the audit.

Sections 7 and 8 come from a second audit, on 2026-10-17, after a referee
report on the framework paper. Each item was
checked against its primary source:
- the axiom list, by `grep` on K7-Lean main and its history;
- the DOIs, against the Zenodo API;
- the lepton numbers, recomputed independently.

Sections 9–11 come from an outside review of the public v3.6 draft
(branch `v3.6-draft`, 2026-10-22). Section 9 was checked by rerunning the two
checkers named there; section 10 by the scaling identity it states, and by
evaluating (65/32)^{1/3}.
