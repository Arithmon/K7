# Validation record

Code/data commit tested: `1bf615062d20ea751a589fcb6d1238708fdcf3d5`.
Date: 2026-09-18. Python: 3.14.4. Package versions: requirements.txt.

- `make paper-data test` passed in a new detached worktree of that commit.
- All 16 tests passed, including source-byte mutation, stale producer,
  invalid interval coverage/coefficient/endpoints, hand-entered paper
  number, unknown claim and pending-claim rejection.
- After full regeneration in that clean checkout, `git diff --exit-code`
  passed and `git status --short` was empty: all tracked outputs were
  reproduced byte for byte.
- `make manuscript` produced the five-page working PDF. The final LaTeX
  log had no undefined citations, errors or overfull boxes.
- `make submission-check` failed as intended on the six open scientific
  gates after the integrity checks and all tests passed.
- No submission tag was created. No historical notebook, original paper,
  OpenWave or other programme file was modified.

The checker reruns interval evaluation at higher precision; it is not an
independent formalization of the analytic min-max proof or of mpmath.
The numerical scalar solver is separately tested on an analytic
constant-coefficient problem. Profile values are compared with an
independent quadrature solution.

## Other certificates inspected for scope

The existing [sigma-min / Neumann-Kronecker artifact](../../certificates/axis2/results/axis2_certificate_sigma_min_NK_2026_06_30.json)
concerns the rank-one J_phys datum D0, not the Chebyshev torsion Jacobian.
The existing [adiabatic M-epsilon artifact](../../certificates/axis2/results/axis2_M_epsilon_adiabatic_2026_07_01.json)
verifies formal perturbative matching for a Donaldson-system ansatz.
Neither supplies a bridge to the frozen companion metric or closes its
NK and full spectral-transfer gates. They were read, not executed or
imported into the new numerical pipeline.
