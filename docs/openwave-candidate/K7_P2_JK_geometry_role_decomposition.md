# K7-P2 JK geometry: role decomposition after freeze

**Freeze:** `K7-GEO-JK-F1` @ `629e87ef968f2b126b7ca4a1fa89a81ccedf2fa4`  
**Status:** audit map; this note does not revise the frozen target.

This note separates selected inputs, consequences, certified computations,
search conveniences, and open gates.  A search result cannot be used to move a
row marked **FROZEN CHOICE** or **SELECTED INPUT**; such a change requires a new
geometry identifier.

| Stage | Content | Role |
|---|---|---|
| Topology | `(b2,b3)=(21,77)` | **SELECTED INPUT / FROZEN CHOICE**; selected structural target, not an independent prediction |
| Historical source | The component table and accounting in `publications/papers/markdown/k7_framework_3_5_S1_foundations.md`, §8.4, at source commit `cc03b63c182ae4820ac7d5d3c4acc0057842368e` | **SOURCE RECORD**; labels `s1,s2` are only identified with `sigma_A,sigma_B` up to exchange |
| Fixed-locus package | `tau:(11,7,1)` and `tau*sigma:(11,9,1)` for the three anti-symplectic coset elements | **FROZEN CHOICE** |
| Nikulin consequences | `(11,7,1)->(g,k)=(2,2)`, `(11,9,1)->(g,k)=(1,1)`; each Euler characteristic is `2` | **MATHEMATICAL CONSEQUENCE** |
| H2 character | In order `(1,tau,sigma_A,sigma_B,tau*sigma_A,tau*sigma_B,sigma_A*sigma_B,tau*sigma_A*sigma_B)`: `(22,0,6,6,0,0,6,0)` | **MATHEMATICAL CONSEQUENCE** |
| Picard rank | `m_tau=rho-17`, hence `rho>=17`; `rho=17` is the minimal admissible/current first target | **MATHEMATICAL CONSEQUENCE / SEARCH CONVENIENCE**; not an independent prediction |
| rho17 split | `NS` character multiplicities `(5,0,2,2,2,2,2,2)` and `rank(T_X)=5`, with `T_X` in the tau-only sector | **MATHEMATICAL CONSEQUENCE** |
| Standard symplectic backend | `M=Lambda^V4`, rank/signature `(10;(3,7))`; `Omega=M^perp`, rank/signature `(12;(0,12))`; nontrivial sectors `4+4+4` | **CERTIFIED COMPUTATION** |
| Integral Omega structure | `D4(-2)^3` has index `16` in `Omega`; quotient `(Z/2)^4` | **CERTIFIED COMPUTATION** |
| Discriminant gluing | Explicit anti-isometry `phi:A_M->A_Omega`; compatibility is `phi tau_Mbar=tau_Omegabar phi` | **CERTIFIED COMPUTATION / OPEN INTERFACE** |
| Current finite searches | Omega table: `90^3=729000`, `47304` integral triples, `11826` actions, fibres of `4`; structured M family: `1557` candidates, `24` compatible, `96` glued actions, profiles permutations of `(7,9,9,11)` | **CERTIFIED SCOPED RESULTS**; not an exhaustion of `O(M)` |
| Remaining integral problem | Other discriminant fibres, full indefinite `O(M)`, and successive/non-orthogonal stable-kernel twists | **OPEN GATE** |
| Geometric realization | Hodge period, exact Picard rank, invariant ample chamber, degree-8 polarization, primitive nef elliptic data, Torelli, and global JK/K7 realization | **OPEN GATES** |
| Physical route | Field-content/operator dictionary and target-blind prospective observable | **OPEN GATES**; no K7-P2 prediction exists |

The arithmetic checks at rho17 are immediate from the frozen character:

```text
rank(NS^tau) = 5 + 2 + 2 + 2 = 11
rank(H^2^V4) = (22+6+6+6)/4 = 10
rank(each nontrivial V4 sector) = 4
```

The current verdict remains **HOLD**: the tested finite M family misses the
frozen `(7,9,9,9)` profile, while the full centralizing integral search is
open.  A PASS would unlock Hodge and ample-chamber gates; a scoped theorem of
impossibility would be a NO-GO.  Neither outcome permits rewriting F1.
