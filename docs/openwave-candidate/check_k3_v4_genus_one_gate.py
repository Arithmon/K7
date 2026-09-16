#!/usr/bin/env python3
"""Reproduce the arithmetic part of the K7 H0a V4 lattice gates.

This script does not prove the mathematical input theorems. It records them as
explicit assumptions and checks the character/rank inequalities used in
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
NIKULIN_RANK_MARGIN = 3


def main() -> None:
    # Topological Lefschetz for a symplectic involution on a K3.
    trace_h2 = FIXED_POINTS_SYMPLECTIC_INVOLUTION - H0_TRACE - H4_TRACE
    invariant_rank_numer = H2_K3_RANK + N_NONTRIVIAL_INVOLUTIONS * trace_h2
    assert invariant_rank_numer % V4_ORDER == 0
    invariant_h2_rank = invariant_rank_numer // V4_ORDER
    coinvariant_rank = H2_K3_RANK - invariant_h2_rank

    # For a projective K3 with symplectic finite group G, Omega_G is contained
    # in NS(X). Add one independent invariant positive ample class.
    rho_min = coinvariant_rank + 1

    # Nikulin criterion as used by Schuett-Shioda Lemma 12.22:
    #   rk(L) >= length(A_L) + 3  =>  U embeds in L.
    # For a K3, length(A_NS) <= rk(T_X) = 22-rho.
    t_rank_at_rho_min = H2_K3_RANK - rho_min
    discr_length_upper_bound = t_rank_at_rho_min
    nikulin_u_criterion = rho_min >= discr_length_upper_bound + NIKULIN_RANK_MARGIN

    # A symplectic action is trivial on T_X. Therefore
    # rk NS(X)^V4 = rk H^2(X)^V4 - rk T_X = rho - 12.
    ns_v4_invariant_rank_at_rho_min = invariant_h2_rank - t_rank_at_rho_min

    assert trace_h2 == 6
    assert invariant_h2_rank == 10
    assert coinvariant_rank == 12
    assert rho_min == 13
    assert rho_min >= MEYER_RANK_THRESHOLD
    assert t_rank_at_rho_min == 9
    assert discr_length_upper_bound == 9
    assert nikulin_u_criterion
    assert ns_v4_invariant_rank_at_rho_min == 1

    print("K7 H0a V4 lattice gates")
    print("========================")
    print(f"symplectic involution fixed points  : {FIXED_POINTS_SYMPLECTIC_INVOLUTION}")
    print(f"trace on H^2                       : {trace_h2}")
    print(f"rank H^2(K3)^V4                    : {invariant_h2_rank}")
    print(f"rank Omega_V4                      : {coinvariant_rank}")
    print(f"projective Picard-rank lower bound : {rho_min}")
    print(f"rank T_X at rho={rho_min}               : {t_rank_at_rho_min}")
    print(f"upper bound length(A_NS)           : {discr_length_upper_bound}")
    print(
        "Nikulin U-embedding inequality      : "
        f"{rho_min} >= {discr_length_upper_bound}+{NIKULIN_RANK_MARGIN} -> "
        f"{nikulin_u_criterion}"
    )
    print(f"rank NS(X)^V4 at rho={rho_min}           : {ns_v4_invariant_rank_at_rho_min}")
    print()
    print("CONDITIONAL RESULTS:")
    print("  H0a.1: symplectic V4 => rho >= 13 => genus-one fibration exists.")
    print("  H0a.2: rho >= 13 satisfies Nikulin's lattice criterion, so U embeds")
    print("          in NS(X); over C this yields an elliptic fibration with section.")
    print("  H0a.3: at the minimal rho=13, NS(X)^V4 has rank 1. Because an")
    print("          invariant ample class gives its positive direction, it has no")
    print("          nonzero isotropic vector. Hence no fibration can be preserved")
    print("          by the full V4 at minimal Picard rank.")
    print()
    print("H0a.3 NECESSARY SPECIALIZATION:")
    print("  rho >= 14 is necessary for rank NS(X)^V4 >= 2, but is not sufficient.")
    print("  The actual invariant lattice must contain a primitive nef isotropic class.")
    print()
    print("NOT ESTABLISHED BY THIS SCRIPT:")
    print("  - the actual higher-Picard specialization selected by K7")
    print("  - a primitive V4-invariant nef isotropic class on that specialization")
    print("  - compatibility with the full Z2^3 / JK gluing data")
    print("  - applicability of a global M/heterotic duality to K7")
    print("  - any neutrino-mass operator or numerical prediction")


if __name__ == "__main__":
    main()
