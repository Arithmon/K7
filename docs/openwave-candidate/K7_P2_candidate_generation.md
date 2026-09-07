# K7-P2 candidate generation workbench

**Status:** `WORKBENCH — K7-P2 NOT YET INSTANTIATED`  
**Opened:** 2026-09-07  
**K7 source baseline:** `Arithmon/K7@0c904242d4131f49cb0d5a476e65f0f54cfc1ba5`  
**OpenWave dossier branch baseline:** `OpenWave-K7@cff68c7b7f7409740e0ba1fca966c5d987de763a`

This file is not a preregistration and contains no K7-P2 numerical prediction. The identifier `K7-P2` remains unavailable for claims until one candidate passes the promotion gate below.

## 1. Clean-room rule

> **No experimental central value, preferred interval, best fit or exclusion curve for the candidate target may be used during derivation.**

The workbench separates four phases:

### Phase D0 — experiment-design information

Allowed before derivation:

- definition of the observable measured by the experiment;
- units, scheme and kinematic point;
- projected sensitivity / resolution;
- whether the experiment can actually discriminate a K7 result from an appropriate null.

Not allowed:

- target central value or preferred range;
- current fit value when it is the quantity being predicted;
- scanning the target literature to choose arithmetic that lands in an allowed region.

### Phase D1 — target-blind derivation

Use only:

- the frozen K7 source baseline;
- standard mathematical / field-theory identities required to map K7 structure to the observable;
- explicitly declared non-target physical anchors whose values were known independently of the target.

Every discretionary sign, branch, operator, representation, scale and normalization choice must be ledgered before the output is evaluated.

### Phase D2 — freeze

Before opening target-result literature, commit:

1. source commit;
2. complete dependency graph;
3. physical operator / observable map;
4. all discrete and continuous choices;
5. executable reproducer;
6. one numerical output or sharply delimited distribution fixed by the model;
7. named experiment and kinematics;
8. null / comparison model;
9. falsification threshold;
10. no-revision rule.

Only then may the candidate become `K7-P2`.

### Phase D3 — eligibility / confrontation

After the freeze, inspect existing bounds and future releases.

If the frozen output is already excluded, record the failure. **Do not revise the formula and reuse the `K7-P2` identifier.** Any changed derivation becomes `K7-P2R1` or a new candidate, depending on scope.

---

## 2. Candidate order

### Candidate A — absolute neutrino mass

**Priority:** 1  
**Current state:** `OPEN — mechanism absent`

Target observables worth deriving:

- the lightest mass eigenvalue `m_lightest`;
- the ordering, if K7 genuinely fixes it;
- the beta-decay effective mass

`m_beta^2 = sum_i |U_ei|^2 m_i^2`.

**Experiment-design information allowed at D0:** Project 8 states that its final Phase IV program is designed to reach approximately **40 meV** neutrino-mass sensitivity; as of the 2026-09-07 workbench opening, its official status page says effort is focused on Phase III.

Official design source: https://www.project8.org/about

#### Repository status at workbench opening

Targeted searches of `main@0c904...` on 2026-09-07 found no implementation / discussion under the terms:

- `Majorana`;
- `seesaw`;
- `right-handed neutrino`.

A search for `Weinberg operator` returned the electroweak Weinberg-angle relation rather than a dimension-five neutrino-mass operator.

Therefore K7 does **not** currently possess a documented absolute-neutrino-mass mechanism suitable for preregistration.

#### Hypothesis seed — not a prediction

The current K7 framework contains a numerical fiber-level Wilson-line operator of rank 2, with the third singular value at machine zero. This is **not** presently a neutrino mass matrix and must not be described as one.

It is worth asking one target-blind structural question:

> Does a correctly derived neutrino mass operator inherit a rank constraint from the same K7 fiber / resolution decomposition?

If the answer is no, discard the route. If yes, derive the operator first; do not choose an ordering or mass scale because it happens to sit near Project 8 sensitivity.

#### Promotion requirements

Candidate A cannot become K7-P2 until K7 fixes a dimensionful neutrino mass scale or a dimensionless relation that, together with separately ledgered non-target anchors, yields `m_beta` without fitting to direct neutrino-mass data.

---

### Candidate B — low-Q^2 weak mixing angle

**Priority:** 2  
**Current state:** `HOLD — current K7 running fails the precondition`

Potential target:

`sin^2 theta_W(Q^2)` at the low momentum transfers probed by P2 and MOLLER.

**Experiment-design information allowed at D0:** 

- P2 targets approximately **0.14% relative uncertainty** on `sin^2 theta_W` at `Q^2 = 4.5e-3 GeV^2`.
- MOLLER's design quotes `Q^2 ~ 0.0056 GeV^2` and a weak-angle uncertainty of order **0.1%**.

Official sources:

- P2 / Mainz: https://agberger.kph.uni-mainz.de/p2/
- P2 precision document: https://openscience.ub.uni-mainz.de/items/27a738a9-1d38-42f8-9c46-9f5e4b800ea9
- MOLLER: https://moller.jlab.org/

#### Blocking precondition

The current K7 Type-III RGE implementation gives `sin^2 theta_W(M_Z) = 0.2377`, recorded as about **2.78%** from its comparison value. A low-Q^2 preregistration is not defensible while the same running prescription already misses the measured Z-scale quantity at a much larger level than the future P2/MOLLER precision.

Therefore:

> **Do not derive or freeze a P2/MOLLER number until the scheme / threshold / matching problem is resolved without using P2 or MOLLER target values.**

A repair tuned to low-Q^2 data is not eligible.

---

### Candidate C — flavor selection rule

**Priority:** 3  
**Current state:** `HOLD — generation/cycle map currently calibrated`

Potential output class:

- an exact forbidden transition;
- a forced branching-ratio zero;
- a parameter-free ratio of two flavor-changing channels.

K7 contains a potentially useful structural statement: non-trivial Yukawa structure is tied to the resolution sector rather than the J-invariant torus sector. But the current Type-III phenomenology also uses optimized positions and a generation-to-cycle assignment selected among 57 associative cycles by minimizing deviation.

That calibrated map cannot be reused as the basis of a genuine prospective flavor prediction.

An admissible route must first derive the generation / cycle / operator identification independently of flavor-target data.

**Pre-freeze baseline only:** Belle II's 2026 `tau -> mu gamma` search reports no significant excess and an upper limit `B < 9.5e-8` at 90% CL from 428 fb^-1. This known bound earns no prospective credit and must not be used to tune a K7 branching ratio.

Official source: https://docs.belle2.org/pub_data/publications/4644/

---

## 3. Candidate scorecard

| Candidate | Target-blind opportunity | K7 mechanism maturity | Experimental discrimination | Current decision |
| --- | --- | --- | --- | --- |
| A. Absolute neutrino mass | **high** | low | medium/high if scale lands in reach | **WORK FIRST** |
| B. low-Q^2 `sin^2 theta_W` | medium | medium but inconsistent at M_Z | very high | **HOLD until RGE repaired independently** |
| C. flavor selection rule | high | medium structural / low predictive | potentially very high | **HOLD until map is forced** |

The ranking is based on epistemic cleanliness first, not on likelihood of a spectacular number.

## 4. Promotion gate to `K7-P2`

A candidate is promoted only if all boxes are true:

- [ ] target value was not used in derivation;
- [ ] observable is experimentally named and scheme / kinematics are fixed;
- [ ] K7 physical map is derived rather than merely identified by numerical resemblance;
- [ ] all anchors and choices are ledgered;
- [ ] one executable reproducer emits the frozen result without experimental target data;
- [ ] predicted result is sufficiently discriminating relative to the null at the named experiment's projected resolution;
- [ ] explicit falsifier and no-revision rule are committed;
- [ ] historical provenance check confirms the target was not already used to construct the same relation.

Until then, **there is no K7-P2 prediction**.

## 5. Next scientific action

Begin Candidate A by constructing an operator-level neutrino-mass inventory from the K7 gauge / representation / Wilson-line / instanton sectors **without consulting direct neutrino-mass target values**.

The first deliverable is not a number. It is a decision tree answering:

1. Dirac, Majorana, or neither from the current K7 field content?
2. Is there a geometric source for a lepton-number-violating operator?
3. Does K7 force matrix rank, texture zeros, or ordering?
4. Where, if anywhere, does the dimensionful mass scale come from?
5. Which steps are topology, which are field-theory identifications, and which remain free choices?

Only after those questions close should any numerical `m_beta` be computed.
