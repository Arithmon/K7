#!/usr/bin/env python3
"""A discriminant-trivial 5+5 involution seed on M = Lambda_K3^V4.

For the standard symplectic V4 on the K3 lattice, the invariant lattice is
isometric to

    M = U + U(2) + U(2) + D4(-2).

This script supplies a particularly simple involution tau_M:

- swap the two basis vectors of U;
- act by -I on both U(2) blocks;
- act by +I on D4(-2).

It checks the required rational 5+5 split, the signatures of the two
eigenspaces, and -- crucially for the next gluing gate -- that tau_M induces
the identity on the full discriminant group A_M.

The latter is basis-independent, so after transporting this seed across any
isometry from the explicit Piroddi invariant lattice to the standard model M,
its discriminant action is still the identity.

No K7 observable or experimental target enters this calculation.
"""

from __future__ import annotations

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def integer_kernel(matrix: sp.Matrix) -> sp.Matrix:
    dm = DomainMatrix.from_Matrix(matrix).convert_to(ZZ)
    smith, _, right = smith_normal_decomp(dm)
    diagonal = smith.to_Matrix()
    transform = right.to_Matrix()
    rank = sum(1 for i in range(min(diagonal.shape)) if diagonal[i, i] != 0)
    return transform[:, rank:]


def inertia_symmetric(matrix: sp.Matrix) -> tuple[int, int, int]:
    """Exact rational congruence reduction, including isotropic 2x2 pivots."""
    matrix = sp.Matrix(matrix)
    assert matrix == matrix.T
    positive = negative = 0
    while matrix.rows:
        pivot = next((i for i in range(matrix.rows) if matrix[i, i]), None)
        if pivot is not None:
            indices = [pivot] + [i for i in range(matrix.rows) if i != pivot]
            matrix = matrix.extract(indices, indices)
            value = matrix[0, 0]
            positive += 1 if value > 0 else 0
            negative += 1 if value < 0 else 0
            matrix = matrix[1:, 1:] - matrix[1:, :1] * matrix[:1, 1:] / value
        else:
            pair = next(((i, j) for i in range(matrix.rows)
                         for j in range(i + 1, matrix.rows) if matrix[i, j]), None)
            if pair is None:
                return positive, negative, matrix.rows
            indices = list(pair) + [i for i in range(matrix.rows) if i not in pair]
            matrix = matrix.extract(indices, indices)
            positive += 1
            negative += 1
            matrix = matrix[2:, 2:] - matrix[2:, :2] * matrix[:2, :2].inv() * matrix[:2, 2:]
    return positive, negative, 0


def main() -> None:
    U = sp.Matrix([[0, 1], [1, 0]])
    U2 = sp.Matrix([[0, 2], [2, 0]])
    D4 = sp.Matrix([
        [2, -1, 0, 0],
        [-1, 2, -1, -1],
        [0, -1, 2, 0],
        [0, -1, 0, 2],
    ])
    D4m2 = -2 * D4

    gram_M = sp.diag(U, U2, U2, D4m2)
    swap_U = sp.Matrix([[0, 1], [1, 0]])
    tau_M = sp.diag(swap_U, -sp.eye(2), -sp.eye(2), sp.eye(4))
    identity = sp.eye(10)

    assert tau_M ** 2 == identity
    assert tau_M.T * gram_M * tau_M == gram_M
    assert int(sp.trace(tau_M)) == 0

    snf = smith_normal_form(gram_M, domain=ZZ)
    divisors = [abs(int(snf[i, i])) for i in range(10)]
    assert divisors == [1, 1, 2, 2, 2, 2, 2, 2, 4, 4]
    assert abs(int(gram_M.det())) == 2 ** 10

    fixed_basis = integer_kernel(tau_M - identity)
    anti_basis = integer_kernel(tau_M + identity)
    fixed_gram = sp.simplify(fixed_basis.T * gram_M * fixed_basis)
    anti_gram = sp.simplify(anti_basis.T * gram_M * anti_basis)

    assert fixed_basis.shape == (10, 5)
    assert anti_basis.shape == (10, 5)
    assert inertia_symmetric(fixed_gram) == (1, 4, 0)
    assert inertia_symmetric(anti_gram) == (2, 3, 0)
    assert abs(int(fixed_gram.det())) == 2 ** 7
    assert abs(int(anti_gram.det())) == 2 ** 5

    # An isometry T acts trivially on A_L=L*/L iff (T-I)G^{-1} is integral:
    # every dual vector G^{-1}z is moved by an element of L.
    discr_difference = sp.simplify((tau_M - identity) * gram_M.inv())
    assert all(sp.Rational(entry).q == 1 for entry in discr_difference)

    print("rho=17 invariant-lattice tau_M seed")
    print("====================================")
    print("M                       : U + U(2)^2 + D4(-2)")
    print("rank/signature          : 10 / (3,7)")
    print("|disc(M)|               : 2^10")
    print("A_M                     : (Z/2)^6 + (Z/4)^2")
    print()
    print("tau_M")
    print("  on U                  : swap")
    print("  on U(2)^2             : -I")
    print("  on D4(-2)             : +I")
    print("  order                 : 2")
    print("  trace                 : 0")
    print("  eigenspace ranks      : 5 + 5")
    print("  fixed signature       : (1,4)")
    print("  anti signature        : (2,3)")
    print("  |disc(fixed)|         : 2^7")
    print("  |disc(anti)|          : 2^5")
    print("  action on A_M         : IDENTITY")
    print()
    print("CONSEQUENCE FOR GLUING")
    print("  For the explicit anti-isometry phi: A_M -> A_Omega already certified,")
    print("  compatibility phi*tau_Mbar = tau_Omegabar*phi reduces to")
    print("      tau_Omegabar = identity on A_Omega.")
    print("  The next gate is therefore an involution tau_Omega in the V4 centralizer")
    print("  with the required 2+2 splits and trivial discriminant action.")


if __name__ == "__main__":
    main()
