#!/usr/bin/env python3
"""Integral V4-character decomposition of Omega for the standard symplectic V4.

The rational coinvariant space Omega_Q splits into the three non-trivial
characters of V4, each of dimension four.  This script determines the
integral lattices in those three character spaces inside the Piroddi K3
lattice.

Result:

    L_10 ~= D4(-2),
    L_01 ~= D4(-2),
    L_11 ~= D4(-2),

and their orthogonal direct sum has index 16 in Omega.  Thus Omega is a
2^4-overlattice of D4(-2)^3.  Each pair of sectors has index 4 in the
E8(-2) anti-invariant lattice of the corresponding symplectic involution.

This is the integral reduction needed for the JK tau_Omega search: instead
of an opaque rank-12 lattice, one may work with three D4(-2) blocks plus a
four-bit glue code, while still enforcing the full Omega overlattice.

No K7 observable or experimental target enters the calculation.
"""

from __future__ import annotations

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form

import check_k3_rho17_v4_discriminant_gluing as discr


def integer_matrix(matrix: sp.Matrix) -> sp.Matrix:
    assert all(sp.Rational(entry).q == 1 for entry in matrix)
    return sp.Matrix([[int(entry) for entry in row] for row in matrix.tolist()])


def main() -> None:
    gram, sigma_A, sigma_B = discr.build_standard_v4()
    identity = sp.eye(22)

    M_basis = discr.integer_kernel(sp.Matrix.vstack(
        sigma_A - identity,
        sigma_B - identity,
    ))
    Omega_basis = discr.integer_kernel(M_basis.T * gram)
    Omega_gram = sp.simplify(Omega_basis.T * gram * Omega_basis)
    assert Omega_basis.shape == (22, 12)
    assert abs(int(Omega_gram.det())) == 2 ** 10

    # Non-trivial characters, written as eigenvalues under (sigma_A,sigma_B).
    characters = ((-1, +1), (+1, -1), (-1, -1))
    sector_bases = []
    sector_grams = []

    for eps_A, eps_B in characters:
        basis = discr.integer_kernel(sp.Matrix.vstack(
            sigma_A - eps_A * identity,
            sigma_B - eps_B * identity,
        ))
        gram_sector = sp.simplify(basis.T * gram * basis)
        assert basis.shape == (22, 4)
        assert gram_sector.is_negative_definite
        assert int(gram_sector.det()) == 2 ** 6

        snf = smith_normal_form(gram_sector, domain=ZZ)
        assert [abs(int(snf[i, i])) for i in range(4)] == [2, 2, 4, 4]

        # Explicit D4(-2) certificate.  Dividing by -2 gives a positive even
        # determinant-4 lattice.  The matrices below give a unimodular change
        # of basis to the standard D4 Cartan Gram matrix.
        sector_bases.append(basis)
        sector_grams.append(gram_sector)

    D4 = sp.Matrix([
        [2, -1, 0, 0],
        [-1, 2, -1, -1],
        [0, -1, 2, 0],
        [0, -1, 0, 2],
    ])
    changes = (
        sp.Matrix([
            [-1, -1,  1,  1],
            [-1,  0,  0,  0],
            [ 1,  2, -1, -1],
            [-1, -1,  0,  1],
        ]),
        sp.Matrix([
            [-1,  0,  0,  0],
            [ 1,  0,  1,  1],
            [-1,  1, -1, -1],
            [-1,  0, -1,  0],
        ]),
        sp.Matrix([
            [-1, -1,  1,  1],
            [-1,  0,  0,  0],
            [ 1,  2, -1, -1],
            [-1, -1,  0,  1],
        ]),
    )
    for gram_sector, change in zip(sector_grams, changes):
        assert abs(int(change.det())) == 1
        assert change.T * (-gram_sector / 2) * change == D4

    # The three character spaces are pairwise orthogonal.
    for i in range(3):
        for j in range(i + 1, 3):
            assert sector_bases[i].T * gram * sector_bases[j] == sp.zeros(4)

    sector_sum = sp.Matrix.hstack(*sector_bases)
    sector_sum_gram = sp.simplify(sector_sum.T * gram * sector_sum)
    assert abs(int(sector_sum_gram.det())) == 2 ** 18

    # Express the sector sum in the primitive Omega basis.  Exact Euclidean
    # left inversion is legitimate because Omega_basis has full column rank
    # and the sector vectors are known to lie in its rational span.
    left_inverse_Omega = sp.simplify(
        (Omega_basis.T * Omega_basis).inv() * Omega_basis.T
    )
    sector_in_Omega = integer_matrix(sp.simplify(left_inverse_Omega * sector_sum))
    index_sector_sum = abs(int(sector_in_Omega.det()))
    assert index_sector_sum == 16

    quotient_snf = smith_normal_form(sector_in_Omega, domain=ZZ)
    quotient_divisors = [abs(int(quotient_snf[i, i])) for i in range(12)]
    assert quotient_divisors == [1] * 8 + [2] * 4

    # Pairwise consistency: the two sectors on which an individual symplectic
    # involution is -1 generate an index-4 sublattice of its E8(-2)
    # anti-invariant lattice.
    pair_reports = []
    for label, involution, pair in (
        ("sigma_A", sigma_A, (0, 2)),
        ("sigma_B", sigma_B, (1, 2)),
        ("sigma_A*sigma_B", sigma_A * sigma_B, (0, 1)),
    ):
        anti_basis = discr.integer_kernel(involution + identity)
        pair_basis = sp.Matrix.hstack(
            sector_bases[pair[0]], sector_bases[pair[1]]
        )
        left_inverse_anti = sp.simplify(
            (anti_basis.T * anti_basis).inv() * anti_basis.T
        )
        pair_in_anti = integer_matrix(sp.simplify(left_inverse_anti * pair_basis))
        pair_index = abs(int(pair_in_anti.det()))
        assert pair_index == 4

        pair_snf = smith_normal_form(pair_in_anti, domain=ZZ)
        pair_divisors = [abs(int(pair_snf[i, i])) for i in range(8)]
        assert pair_divisors == [1] * 6 + [2] * 2
        pair_reports.append((label, pair_index))

    print("rho=17 Omega V4-character sector certificate")
    print("=============================================")
    for character in characters:
        print(f"sector {character}: rank 4, D4(-2), |disc|=2^6")
    print()
    print("orthogonal sector sum   : D4(-2)^3")
    print("|disc(sector sum)|      : 2^18")
    print("|disc(Omega)|           : 2^10")
    print("[Omega:D4(-2)^3]        :", index_sector_sum)
    print("Omega / sector sum      : (Z/2)^4")
    print()
    print("pairwise E8(-2) checks")
    for label, pair_index in pair_reports:
        print(f"  {label:19s}: sector-pair index {pair_index} in E8(-2)")
    print()
    print("CONSEQUENCE")
    print("  The tau_Omega search reduces to trace-zero involutions on three")
    print("  D4(-2) character blocks, subject to preservation of the 2^4 glue")
    print("  defining Omega.")
    print("  A matched tau_M is accepted only when")
    print("      phi o tau_Mbar = tau_Omegabar o phi.")
    print("  Trivial action on A_Omega is only the exploratory seed's special case.")


if __name__ == "__main__":
    main()
