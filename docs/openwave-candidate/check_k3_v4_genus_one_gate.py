#!/usr/bin/env python3
"""Reproduce the arithmetic part of the K7 H0a V4 lattice gate.

This script does not prove the mathematical input theorems. It records them as
explicit assumptions and checks the character/rank implications used in
K7_P2_neutrino_H0_fiber_lattice_gate.md.

No experimental physics target is embedded or read.
"""

from __future__ import annotations


H2_K3_RANK = 22
V4_ORDER = 4
N_NONTRIVIAL_INVOLUTIONS = 3
FIXED_POINTS_SYMPLECTIC_INVOLUTION = 8
H0_TRACE = 1
H4_TRACE = 1
MEYER_RANK_THRESHOLD = 5


def main() -> None:
    trace_h2 = (
        FIXED_POINTS_SYMPLECTIC_INVOLUTION - H0_TRACE - H4_TRACE
    )
    invariant_rank_numer = (
        H2_K3_RANK + N_NONTRIVIAL_INVOLUTIONS * trace_h2
    )
    assert invariant_rank_numer % V4_ORDER == 0
    invariant_rank = invariant_rank_numer // V4_ORDER
    coinvariant_rank = H2_K3_RANK - invariant_rank

    # For a projective K3 with a symplectic finite group, Omega_G lies in NS(X).
    # The negative-definite coinvariant lattice is independent of one positive
    # ample class, giving this lower bound.
    picard_lower_bound = coinvariant_rank + 1

    assert trace_h2 == 6
    assert invariant_rank == 10
    assert coinvariant_rank == 12
    assert picard_lower_bound == 13
    assert picard_lower_bound >= MEYER_RANK_THRESHOLD

    print("K7 H0a V4 lattice gate")
    print("========================")
    print(f"symplectic involution fixed points : {FIXED_POINTS_SYMPLECTIC_INVOLUTION}")
    print(f"trace on H^2                     : {trace_h2}")
    print(f"rank H^2(K3)^V4                  : {invariant_rank}")
    print(f"rank Omega_V4                    : {coinvariant_rank}")
    print(f"projective Picard-rank lower bound: {picard_lower_bound}")
    print(f"Meyer isotropic-rank threshold   : {MEYER_RANK_THRESHOLD}")
    print()
    print("CONDITIONAL RESULT:")
    print("  If the K7 degree-8 projective K3 genuinely carries the stated")
    print("  symplectic V4 action, rho >= 13; hence NS is indefinite of")
    print("  rank >= 5 and contains a nonzero isotropic class. Standard K3")
    print("  lattice theory then yields a genus-one fibration.")
    print()
    print("NOT ESTABLISHED BY THIS SCRIPT:")
    print("  - a section / primitive U embedding")
    print("  - compatibility with K7 gluing or the full Z2^3 action")
    print("  - applicability of a global M/heterotic duality to K7")
    print("  - any neutrino-mass operator or numerical prediction")


if __name__ == "__main__":
    main()
