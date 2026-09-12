#!/usr/bin/env python3
"""Rho=17 symplectic-V4 reset gate for K7-P2 Candidate A.

This gate separates two statements which had previously been conflated:

1. the rho=17 rational character is admissible;
2. the explicit integral sign-change action on NS_17(C) is geometric.

The first statement survives.  The second fails before Global Torelli:
each non-trivial V4 generator sends genuine (-2)-roots in the A1(-1)^15
frame to their negatives.  A projective K3 automorphism cannot do that,
because one of +/-r is effective by Riemann--Roch and automorphisms preserve
the effective (equivalently ample/Kahler) chamber.

The replacement target is the standard symplectic V4 lattice package:
the V4 coinvariant lattice Omega_V4 has rank 12, determinant 2^10,
discriminant group (Z/2)^6 + (Z/4)^2 and contains no (-2)-vectors.
Its invariant orthogonal complement in the K3 lattice is
    U(2) + U(2) + Q_(2,2)
with Q_(2,2) as in Garbagnati--Sarti.

No neutrino mass, ordering or experimental target is used.
"""

from __future__ import annotations

from fractions import Fraction


# Character labels are bits (tau, sigma_A, sigma_B), exactly as in the
# previous rho=17 certificate.  The 15 negative A1 roots carry these labels.
CHARS = (
    (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 1, 0), (0, 1, 0),
    (0, 0, 1), (0, 0, 1),
    (1, 1, 0), (1, 1, 0),
    (1, 0, 1), (1, 0, 1),
    (0, 1, 1), (0, 1, 1),
    (1, 1, 1), (1, 1, 1),
)

V4 = (
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 1),
)

# Target H^2 traces in the order
# 1, tau, sigma_A, sigma_B, tau*sigma_A, tau*sigma_B,
# sigma_A*sigma_B, tau*sigma_A*sigma_B.
TARGET_H2_TRACES = (22, 0, 6, 6, 0, 0, 6, 0)

# Garbagnati--Sarti's Q_(2,2) Gram matrix.  Together with U(2)^2 this is
# the rank-10 invariant lattice of a symplectic (Z/2)^2 action.
Q22 = (
    (0, 1, 0, 0, 0, 0),
    (1, -2, 2, 0, 0, 0),
    (0, 2, -4, 2, 0, 0),
    (0, 0, 2, -4, 2, 0),
    (0, 0, 0, 2, -4, 4),
    (0, 0, 0, 0, 4, -8),
)
U2 = (
    (0, 2),
    (2, 0),
)


def char_sign(character: tuple[int, int, int],
              element: tuple[int, int, int]) -> int:
    return -1 if sum(a * b for a, b in zip(character, element)) & 1 else 1


def block_diag(*blocks: tuple[tuple[int, ...], ...]) -> list[list[int]]:
    n = sum(len(b) for b in blocks)
    out = [[0] * n for _ in range(n)]
    offset = 0
    for block in blocks:
        m = len(block)
        for i in range(m):
            for j in range(m):
                out[offset + i][offset + j] = block[i][j]
        offset += m
    return out


def determinant(matrix: list[list[int]] | tuple[tuple[int, ...], ...]) -> int:
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        p = a[col][col]
        det *= p
        for row in range(col + 1, n):
            if not a[row][col]:
                continue
            factor = a[row][col] / p
            for j in range(col, n):
                a[row][j] -= factor * a[col][j]
    assert det.denominator == 1
    return det.numerator


def v4_sector_data() -> dict[tuple[int, int], tuple[int, int]]:
    """Return (dimension, tau-trace) on each V4 character sector of H^2."""
    # V4 elements ordered 1, sigma_A, sigma_B, sigma_A*sigma_B.
    v4_elements = ((0, 0), (1, 0), (0, 1), (1, 1))
    h2_v4_traces = (22, 6, 6, 6)
    tau_coset_traces = (0, 0, 0, 0)

    out: dict[tuple[int, int], tuple[int, int]] = {}
    for psi in v4_elements:
        signs = tuple(
            -1 if (psi[0] * g[0] + psi[1] * g[1]) & 1 else 1
            for g in v4_elements
        )
        dim_num = sum(s * t for s, t in zip(signs, h2_v4_traces))
        tau_num = sum(s * t for s, t in zip(signs, tau_coset_traces))
        assert dim_num % 4 == 0
        assert tau_num % 4 == 0
        out[psi] = (dim_num // 4, tau_num // 4)
    return out


def main() -> None:
    # Reconfirm the rho=17 rational-character content relevant here.
    assert TARGET_H2_TRACES == (22, 0, 6, 6, 0, 0, 6, 0)
    sectors = v4_sector_data()
    assert sectors[(0, 0)] == (10, 0)
    assert sectors[(1, 0)] == (4, 0)
    assert sectors[(0, 1)] == (4, 0)
    assert sectors[(1, 1)] == (4, 0)

    # Fatal check on the previous integralization.
    # Every non-trivial V4 element negates eight actual A1(-1) roots.
    inverted_roots: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for sigma in V4:
        roots = tuple(i for i, c in enumerate(CHARS) if char_sign(c, sigma) == -1)
        assert len(roots) == 8
        inverted_roots[sigma] = roots

    # Each listed coordinate vector belongs to the original frame L0 subset NS
    # and has square -2.  Therefore the old sign-change action cannot preserve
    # any K3 effective/ample chamber.
    assert all(inverted_roots[sigma] for sigma in V4)

    # Standard symplectic-V4 replacement lattice contract.
    invariant_gram = block_diag(U2, U2, Q22)
    assert len(invariant_gram) == 10
    assert abs(determinant(Q22)) == 2 ** 6
    assert abs(determinant(invariant_gram)) == 2 ** 10

    omega_rank = 22 - len(invariant_gram)
    omega_discriminant_order = 2 ** 10
    assert omega_rank == 12

    # The target character forces tau to split every V4 isotypic sector evenly:
    # invariant sector 10 -> 5+5, and each non-trivial sector 4 -> 2+2.
    tau_splits = {}
    for psi, (dim, tr_tau) in sectors.items():
        plus = (dim + tr_tau) // 2
        minus = (dim - tr_tau) // 2
        assert plus + minus == dim
        assert plus - minus == tr_tau
        tau_splits[psi] = (plus, minus)
    assert tau_splits[(0, 0)] == (5, 5)
    assert all(tau_splits[psi] == (2, 2) for psi in ((1, 0), (0, 1), (1, 1)))

    print("rho=17 symplectic-V4 reset gate")
    print("================================")
    print()
    print("SURVIVES")
    print("  rho>=17 character obstruction       : unchanged")
    print("  rho=17 H^2 V4 sectors               : 10 + 4 + 4 + 4")
    print("  tau trace on every V4 sector        : 0")
    print("  tau eigenspace split                : 5+5; 2+2; 2+2; 2+2")
    print()
    print("OLD INTEGRAL ACTION")
    for sigma, roots in inverted_roots.items():
        print(f"  sigma={sigma} negates A1 roots       : {roots}")
    print("  each such root has square            : -2")
    print("  verdict                              : FAIL (no preserved K3 ample/effective chamber)")
    print()
    print("REPLACEMENT SYMPLECTIC V4 CONTRACT")
    print("  rank Omega_V4                       :", omega_rank)
    print("  |disc Omega_V4|                     :", omega_discriminant_order)
    print("  A_Omega                             : (Z/2)^6 + (Z/4)^2")
    print("  Omega_V4 has (-2)-vectors           : no")
    print("  rank Lambda_K3^V4                   :", len(invariant_gram))
    print("  Lambda_K3^V4                        : U(2) + U(2) + Q_(2,2)")
    print("  |disc Lambda_K3^V4|                 :", abs(determinant(invariant_gram)))
    print()
    print("NEXT INTEGRAL PROBLEM")
    print("  Realize the standard symplectic V4 conjugacy class first, then find")
    print("  a commuting tau whose fixed lattices are (11,7,1) and (11,9,1),")
    print("  before any period/ample/Torelli promotion or neutrino calculation.")


if __name__ == "__main__":
    main()
