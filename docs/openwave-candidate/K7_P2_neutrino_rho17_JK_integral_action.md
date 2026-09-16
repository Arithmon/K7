# rho17 JK integral-action audit: finite reconstruction and scoped exclusions

Date: 2026-09-15. Decision target: `OpenWave-K7-rho17-v4-reset`
at `1c7c1b6238e49969d2a1bcc955f24968143d42ab`.

**Full JK integral action: HOLD.** No action with four types
`(11,7,1), (11,9,1), (11,9,1), (11,9,1)` has been constructed here.
There is no general rho17 impossibility theorem here either.

This audit independently reconstructs the uncommitted finite searches in the
handoff, corrects their reported profiles, and excludes several precisely
defined classes of extensions. No physical observable is calculated.
The historical OpenWave pass count remains zero; K7-P1 remains rejected;
there is still no K7-P2 prediction.

## Decision corpus and baseline reproduction

Read: the dossier README, honest ledger, historical prediction audit,
falsifiers and OpenWave mapping; all rho17/V4 Python certificates; the
character gate, standard-V4 note and the supplied 2026-09-15 handoff.
The integral backend remains [Piroddi, Proposition 1.2.1](https://arxiv.org/html/2408.00643v1#S1.SS2),
reconstructed by the existing public scripts. The search derives its input
matrices from those live scripts, not from the handoff's numerical summaries.

All eleven pre-existing `check_k3_*.py` scripts in this dossier were rerun.
Ten ran successfully at the starting SHA. The tau_M seed failed with
`sympy.core.evalf.PrecisionExhausted` in its floating eigenvalue calculation.
That helper also counted distinct eigenvalues without their multiplicities.
Replacing it by exact rational congruence reduction makes the seed pass:
fixed signature `(1,4)`, anti signature `(2,3)`, determinant magnitudes
`2^7` and `2^5`, and trivial discriminant action. Repeated, isotropic and
singular signature cases were separately checked. This repair is commit
`e835ba7`.

The successful historical A1 scripts certify their abstract code lattices
only. Their geometric V4 action remains superseded and invalid, as the reset
gate itself confirms. No old printed optimistic status is promoted here.

## Findings and adjudication

| Claim | Verdict | Evidence / remedy |
| --- | --- | --- |
| rho15 full frozen JK package | NO-GO retained | Exact character inversion; `rho >= 17` is necessary. |
| Standard symplectic V4 backend | GO | Even unimodular `(3,19)` lattice; three actual `E8(-2)` anti-lattices. |
| Omega counts `90^3`, `47304`, `11826`, four lifts each | GO | Exhaustive labelled-centralizer enumeration, two constructions of `O(D4)`. |
| Discriminant-trivial tau_M | NO-GO | No trace-zero-sector Omega involution has trivial discriminant action. |
| Structured M counts `1557 -> 24 -> 96` | GO for the specified embedding below | Explicit model isometry, full quadratic gluing map, integral lifts. |
| Claimed base multiset `{11,9,9,9}` | REQUEST CHANGES | Reconstructed base family has `{7,9,9,11}`; exact fixed lattices checked twice. |
| Orthogonal paired-root products from these bases | NO-GO within this class, all heights | Mod-8 necessary residue screen, including multiple pairs. |
| One opposite-eigenspace Eichler twist from these bases | NO-GO within this class, all heights | Isotropic residue upper bound attained, all parameter residues tested. |
| All centralizing integral tau at rho17 | HOLD | Other discriminant fibres and non-orthogonal/composed twists remain open. |
| Hodge/ample/Torelli, degree 8, elliptic data, global JK, operator | HOLD | No full JK lattice PASS to promote. |

HIGH: the session-local corrected profile is not reproduced. Do not treat
`{11,9,9,9}` as the base-family certificate. The historical local matrices
and the isometry aligning its abstract M model were not supplied. Thus the
numerical count agreement alone does not establish that two unspecified
embeddings define the same finite subset. This audit supplies the missing
embedding explicitly and makes the scope reproducible.

MEDIUM: the seed's numerical signature gate was not reproducible in the
shared environment. Remedy: the exact helper now committed.

MEDIUM: the Omega-sector script's old final sentence still demands trivial
discriminant action. That is a negative-control specialization, not the
general gluing condition. Use `phi * tau_Mbar = tau_Omegabar * phi` instead.

## 1. Exhaustive Omega enumeration

Reproducer: [check_k3_rho17_tauOmega_discriminant_actions.py](check_k3_rho17_tauOmega_discriminant_actions.py).

Each labelled rational V4 character sector has primitive lattice `D4(-2)`.
An isometry commuting with both labelled generators preserves every sector.
All automorphisms of D4 are enumerated by the possible images of a simple
root basis among its 24 roots. Independently, signed coordinate permutations
and a Hadamard triality matrix generate exactly the same 1152 matrices.
Of these, exactly 90 square to the identity and have trace zero.

The live primitive Omega basis determines the index-16 sector-sum embedding
`P`. Every candidate is `P diag(t1,t2,t3) P^-1`. Clearing the actual
denominator 2 gives an exact integrality test for all 729000 triples.
There are 47304 integral triples, inducing 11826 different actions on
`A_Omega`, with fibre multiplicity four for every action.

The action key is the row-major byte matrix
`4*T*G_Omega^-1 mod 4`, in the derived primitive Omega basis. Equality of
keys is exactly equality of the induced action on the discriminant group:
the columns of `G_Omega^-1` generate the dual lattice. These are fixed-basis
representatives, not conjugacy-class labels. Sorted keys concatenate to SHA256

```text
baaff7f758a110742a621835e29b00c9be92a11c486619a73509550b6ce60473
```

The optional JSON table includes every key, its four deterministic triples,
the ordered D4 matrices, and the sector/Omega bases needed to decode them.

The identity key is absent. Consequently **every** tau_M acting trivially
on `A_M` is excluded for the required character, regardless of its height,
its chosen expression in generators, or its eigensignatures. This uses the
full labelled Omega centralizer with the three necessary 2+2 splits, not a
bounded subfamily of that negative-definite group.

## 2. The specified structured M family and exact profiles

Reproducer: [check_k3_rho17_tauM_matching.py](check_k3_rho17_tauM_matching.py).

An explicit unimodular change of basis from the live invariant lattice to
`U + U(2)^2 + D4(-2)` is derived and checked. It is also printed/exported.
The finite family consists of block-diagonal products of:

1. all four automorphisms of U;
2. all 20 involutive signed coordinate permutations preserving the displayed
   `U(2)^2` (not the infinite full orthogonal group of that lattice);
3. all 140 involutions of D4, including the identity.

Trace zero and fixed positive index one retain 1557 candidates. The ambient
K3 lattice rederives the graph `phi` in these specific M/Omega coordinates;
its quadratic anti-isometry is checked on all 1024 classes. Exactly 24 M
candidates match the Omega table. Their four Omega lifts each give 96
integral full actions.

For every lift and every anti-symplectic coset element, the script checks
order two, isometry, commutation with both sigma generators and trace zero.
It computes fixed lattices by **two independent integral constructions**:

- primitive integer kernel from Smith decomposition;
- HNF of `(I+g)L`, then saturation by all integral half-sums.

The second construction is sufficient because `2 L^g` lies in `(I+g)L`.
The two primitive lattices have identical HNF bases. Exact Gram matrices,
Smith divisors and the parity of dual squares establish `(r,a,delta)`;
all 384 fixed lattices have rank 11 and signature `(1,10)`.
Their independently recomputed mod-2 ranks also agree with all 384 Smith
discriminant lengths. Both JSON exports passed a read-back/hash check.

In the order `(tau, tau*sigma_A, tau*sigma_B, tau*sigma_A*sigma_B)`:

| a-profile | Number | delta-profile |
| --- | ---: | --- |
| `(9,11,9,7)` | 24 | `(1,1,1,1)` |
| `(9,7,9,11)` | 24 | `(1,1,1,1)` |
| `(11,9,7,9)` | 24 | `(1,1,1,1)` |
| `(7,9,11,9)` | 24 | `(1,1,1,1)` |

The deterministic JSON records of matrices, fixed Grams, Smith divisors
and types have SHA256

```text
0790cc2b1ae90b8e64a75e59824abfbb5c14de97e2074b75c495a2203dea2490
```

Neither the target nor `{11,9,9,9}` occurs in this base family. Some subsequent
root/Eichler twists do produce `{11,9,9,9}`. That observation does not establish
why the historical session reported it as its base profile.

## 3. Orthogonal paired-root obstruction, without a height cutoff

Reproducer: [check_k3_rho17_jk_reflection_twists.py](check_k3_rho17_jk_reflection_twists.py),
especially `--residue-only`.

The coefficient-box experiment `[-2,2]^5` tests 8736 pairs of mod-2 root
classes, retaining exact representatives. It finds no target. The stronger
test then removes this coefficient bound entirely.

Let `B_+`, `B_-` be primitive bases of the M eigenspaces. The code checks
that each eigenlattice Gram matrix is even entry by entry. For a root
`B z` of square `+2` or `-2`, its norm modulo 8 depends only on `z modulo 4`.
Enumerating all `4^5` residues therefore gives a necessary upper set of
root classes modulo 2, including classes not attained in the small box.
There are eight possible classes for each norm and each eigenspace.

Because the eigenlattice pairings are even, pairings modulo 4 depend only
on coefficients modulo 2. Exact orthogonality requires pairing zero modulo
4. Distinct orthogonal roots cannot have the same residue: their pairing
would instead equal the root square modulo 4. Thus subsets of this finite
upper set cover all orthogonal root configurations at arbitrary height.

The signatures `(1,4)` and `(2,3)` permit matching at most one positive and
three negative root directions on each side. All subsets through size four
are enumerated; none of size four passes the necessary pairing conditions.
For each surviving subset, its product of reflections modulo 2 is determined
by the root residues. Orthogonality removes the cross terms. The resulting
upper sets of **paired products**, over all 96 bases, have sizes:

| Number of reflection pairs | Residue candidates | Target hits |
| ---: | ---: | ---: |
| 0 | 96 | 0 |
| 1 | 12288 | 0 |
| 2 | 69120 | 0 |
| 3 | 61440 | 0 |
| 4 | 0 | 0 |

This excludes the target for every product in this orthogonal paired-root
class from these bases, without assuming that every residue lifts to a root.
It does **not** exclude successive products chosen in new eigenspaces, or
non-orthogonal products whose involutivity is obtained by other relations.

Why a mod-2 exclusion is legitimate here: for an involution `g` of an even
unimodular lattice, `ker(g-I mod 2) = (L^g + L^-g)/2L`. Primitive orthogonal
gluing identifies `[L:L^g+L^-g] = |A_(L^g)| = 2^a`, so `rank_F2(g-I)=a`.
This is used only as a necessary exclusion filter. The positive fixed-lattice
claims in Section 2 use actual primitive Gram matrices, SNF and parity.

## 4. A single opposite-eigenspace Eichler twist

Reproducer: [check_k3_rho17_jk_eichler_twists.py](check_k3_rho17_jk_eichler_twists.py).

For integral isotropic `e in M` and integral `a in M` perpendicular to `e`, use

```text
E(e,a)(x) = x + (x,e)a - (x,a)e - (a,a)/2 * (x,e)e.
```

If `e` belongs to one tau eigenspace and `a` to the other, then
`tau E(e,a) tau = E(e,-a) = E(e,a)^-1`.
Thus `E(e,a) tau` is an integral involution with unchanged discriminant
action. Rational conjugation by `E(e,a/2)` shows that it retains the exact
character and signatures. The half-transvection need not be integral;
this does not merely enumerate integral conjugates.

For each of the 24 matched M actions, each eigenspace has seven nonzero
isotropic residue classes, all realized in the box of bound two. This set
equals the necessary mod-8 upper bound from all coefficient residues modulo
four. Every opposite-eigenspace parameter residue modulo two is tested.
The evenness of M makes `(a,a)/2 mod 2` depend only on `a mod 2`, so the
transvection modulo two is fully determined by these residues. Even `e`
acts trivially modulo two and returns the already excluded base profile.

Across the 96 full lifts this gives 43008 parameter tests, with no target.
The residue completeness therefore excludes **one** such eigen-compatible
Eichler twist at arbitrary height from these bases. Compositions and other
initial involutions are not covered.

## Reproduction and environment

The verified shared environment was Python 3.14.4, SymPy 1.14.0,
NumPy 2.5.1 and mpmath 1.3.0. No packages or toolchains were installed.
No K3 pools or Lean builds were run. On this workspace:

```bash
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=/home/galerie/gift-framework/.pylibs-k3-mp130:/home/galerie/gift-framework/.pylibs-k3
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
python3 docs/openwave-candidate/check_k3_rho17_tauOmega_discriminant_actions.py
python3 docs/openwave-candidate/check_k3_rho17_tauM_matching.py
python3 docs/openwave-candidate/check_k3_rho17_jk_reflection_twists.py --bound 2
python3 docs/openwave-candidate/check_k3_rho17_jk_reflection_twists.py --residue-only
python3 docs/openwave-candidate/check_k3_rho17_jk_eichler_twists.py --bound 2
```

Outside this workspace, ordinary NumPy/SymPy imports suffice; the absolute
shared-library paths are not embedded in the scripts. The Omega and matching
scripts accept `--output NEW_FILE.json` for deterministic machine-readable
tables. Export uses exclusive creation and never overwrites a certificate.
Run with assertions enabled. HNF/SNF basis-dependent hashes above are pinned
to the stated versions, not asserted invariant across library versions.

## Concrete NEXT

1. Classify the remaining discriminant-action fibres of `O(M) -> O(q_M)`
   against the complete 11826-action Omega table. The 1557-element M family
   is explicitly not exhaustive in the indefinite orthogonal group.
2. Alternatively use successive non-conjugate twists with eigenspaces
   recomputed after each step; the all-height exclusions above apply to
   the original 24 M bases, not every subsequently reached involution.
3. Preserve order two and trace zero as exact gates before expensive fixed
   lattices. Reject target-free mod-2 hits whose rational character changes.
4. An eventual hit must still pass a standalone full-action check from a
   clean checkout, then the Hodge/ample/Torelli and remaining geometric gates.

No README status is upgraded. No external OpenWave post or PR is made.
