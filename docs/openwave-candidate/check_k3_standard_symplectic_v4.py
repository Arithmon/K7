#!/usr/bin/env python3
"""Exact reconstruction of the standard symplectic V4 action on Lambda_K3.

This implements Piroddi, arXiv:2408.00643, Proposition 1.2.1.  To avoid a
notation collision with the K7 anti-symplectic tau, Piroddi's symplectic
involutions tau and phi are called sigma_A and sigma_B here.

The construction starts from the finite-index lattice

    W = A2^8 + A2(2) + U(3) + [[4,2],[2,4]]

and adjoins Piroddi's seven explicit glue classes alpha,...,eta.  The script
then verifies that the resulting rank-22 lattice is even unimodular, that the
two involutions extend integrally and commute, and that the integral fixed /
anti-invariant lattices have the canonical symplectic-V4 invariants.

No K7 target observable or neutrino input is used.
"""

from __future__ import annotations

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


NAMES = (
    "a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2",
    "e1", "e2", "f1", "f2", "g1", "g2", "h1", "h2",
    "w", "z", "x", "y", "v1", "v2",
)
IDX = {name: i for i, name in enumerate(NAMES)}


def basis_vector(name: str) -> sp.Matrix:
    out = sp.zeros(22, 1)
    out[IDX[name], 0] = 1
    return out


def linear_combination(terms: dict[str, int], denominator: int = 1) -> sp.Matrix:
    out = sp.zeros(22, 1)
    for name, coefficient in terms.items():
        out[IDX[name], 0] = sp.Rational(coefficient, denominator)
    return out


def integer_matrix(matrix: sp.Matrix) -> sp.Matrix:
    assert all(entry.q == 1 for entry in matrix)
    return sp.Matrix([[int(entry) for entry in row] for row in matrix.tolist()])


def integer_kernel(matrix: sp.Matrix) -> sp.Matrix:
    """Primitive Z-basis of ker(matrix: Z^n -> Z^m), via Smith decomposition."""
    dm = DomainMatrix.from_Matrix(matrix).convert_to(ZZ)
    smith, _, right = smith_normal_decomp(dm)
    diagonal = smith.to_Matrix()
    transform = right.to_Matrix()
    rank = sum(
        1 for i in range(min(diagonal.shape))
        if diagonal[i, i] != 0
    )
    return transform[:, rank:]


def action_on_W(which: str) -> sp.Matrix:
    """Piroddi's two symplectic generators on the chosen W basis."""
    out = sp.zeros(22)
    mapping = {name: (name, 1) for name in NAMES}

    if which == "sigma_A":
        # Piroddi's tau: a<->b, c<->d, g<->h; -id on A2(2).
        swaps = (
            ("a1", "b1"), ("a2", "b2"),
            ("c1", "d1"), ("c2", "d2"),
            ("g1", "h1"), ("g2", "h2"),
        )
        for left, right in swaps:
            mapping[left] = (right, 1)
            mapping[right] = (left, 1)
        mapping["w"] = ("w", -1)
        mapping["z"] = ("z", -1)
    elif which == "sigma_B":
        # Piroddi's phi: a<->d, b<->c, e<->f, g<->h; +id on A2(2).
        swaps = (
            ("a1", "d1"), ("a2", "d2"),
            ("b1", "c1"), ("b2", "c2"),
            ("e1", "f1"), ("e2", "f2"),
            ("g1", "h1"), ("g2", "h2"),
        )
        for left, right in swaps:
            mapping[left] = (right, 1)
            mapping[right] = (left, 1)
    else:
        raise ValueError(which)

    for column, name in enumerate(NAMES):
        destination, sign = mapping[name]
        out[IDX[destination], column] = sign
    return out


def main() -> None:
    # W, using the negative-definite convention for the eight A2 root blocks.
    A2 = sp.Matrix([[-2, 1], [1, -2]])
    A2_2 = 2 * A2
    U3 = sp.Matrix([[0, 3], [3, 0]])
    transcendental = sp.Matrix([[4, 2], [2, 4]])
    gram_W = sp.diag(*([A2] * 8 + [A2_2, U3, transcendental]))

    # Piroddi (1.2.2), in the basis
    # a1,a2,...,h1,h2,w,z,x,y,v1,v2.
    alpha = linear_combination({
        "a1": -1, "a2": 1, "d1": 1, "d2": -1,
        "e1": -1, "e2": 1, "f1": 1, "f2": -1,
        "g1": -1, "g2": 1, "h1": 1, "h2": -1,
    }, 3)
    beta = linear_combination({
        "b1": -1, "b2": 1, "c1": 1, "c2": -1,
        "e1": -1, "e2": 1, "f1": 1, "f2": -1,
        "g1": 1, "g2": -1, "h1": -1, "h2": 1,
    }, 3)
    gamma = linear_combination({
        "x": 1, "y": -1, "e1": -1, "e2": 1, "f1": -1, "f2": 1,
    }, 3)
    delta = linear_combination({
        "x": 1, "c1": -1, "c2": 1, "d1": -1, "d2": 1,
        "e1": -1, "e2": 1,
    }, 3)
    epsilon = linear_combination({
        "x": 1, "z": -1, "w": 1, "c1": 1, "c2": -1,
        "e1": -1, "e2": 1, "g1": -1, "g2": 1,
        "h1": 1, "h2": -1,
    }, 3)
    zeta = (
        linear_combination({
            "x": 1, "z": 1, "c1": 1, "c2": 1,
            "e1": 1, "e2": 1, "g1": 1, "g2": 1,
            "h1": 1, "h2": 1,
        }) + epsilon
    ) / 2 + basis_vector("v2") / 2
    eta = (
        linear_combination({
            "x": 1, "c1": 1, "c2": 1, "e1": 1, "e2": 1,
        }) + epsilon
    ) / 2 + linear_combination({
        "g1": 1, "g2": -1, "h1": 1, "h2": -1,
    }, 6) + basis_vector("v1") / 6 - basis_vector("v2") / 3

    glue = (alpha, beta, gamma, delta, epsilon, zeta, eta)

    # All denominators divide six.  Work in coordinates of 6*Lambda_K3,
    # compute a column HNF, then divide the resulting basis by six.
    scale = 6
    generators = [sp.eye(22)[:, i] * scale for i in range(22)]
    generators += [vector * scale for vector in glue]
    generator_matrix = integer_matrix(sp.Matrix.hstack(*generators))
    hnf = hermite_normal_form(generator_matrix)

    index_Lambda_over_W = scale ** 22 // abs(int(hnf.det()))
    assert index_Lambda_over_W == 2916

    basis_Lambda_in_W = hnf / sp.Integer(scale)
    gram_K3 = sp.simplify(basis_Lambda_in_W.T * gram_W * basis_Lambda_in_W)

    assert all(entry.q == 1 for entry in gram_K3)
    assert all(int(gram_K3[i, i]) % 2 == 0 for i in range(22))
    assert int(gram_K3.det()) == -1
    # The signature is inherited from W: 8*A2 + A2(2) contributes 18
    # negative directions, U(3) contributes (1,1), and the final rank-2
    # block is positive definite.  Hence signature (3,19).

    sigma_A_W = action_on_W("sigma_A")
    sigma_B_W = action_on_W("sigma_B")
    assert sigma_A_W.T * gram_W * sigma_A_W == gram_W
    assert sigma_B_W.T * gram_W * sigma_B_W == gram_W

    change_inverse = basis_Lambda_in_W.inv()
    sigma_A = integer_matrix(sp.simplify(change_inverse * sigma_A_W * basis_Lambda_in_W))
    sigma_B = integer_matrix(sp.simplify(change_inverse * sigma_B_W * basis_Lambda_in_W))

    identity = sp.eye(22)
    assert sigma_A ** 2 == identity
    assert sigma_B ** 2 == identity
    assert sigma_A * sigma_B == sigma_B * sigma_A
    assert sigma_A.T * gram_K3 * sigma_A == gram_K3
    assert sigma_B.T * gram_K3 * sigma_B == gram_K3
    assert [int(sp.trace(g)) for g in (sigma_A, sigma_B, sigma_A * sigma_B)] == [6, 6, 6]

    # Full V4 invariant lattice.
    fixed_basis = integer_kernel(sp.Matrix.vstack(
        sigma_A - identity,
        sigma_B - identity,
    ))
    fixed_gram = fixed_basis.T * gram_K3 * fixed_basis
    assert fixed_basis.shape == (22, 10)
    assert abs(int(fixed_gram.det())) == 2 ** 10

    fixed_snf = smith_normal_form(fixed_gram, domain=ZZ)
    fixed_elementary_divisors = [
        abs(int(fixed_snf[i, i])) for i in range(10)
    ]
    assert fixed_elementary_divisors == [1, 1, 2, 2, 2, 2, 2, 2, 4, 4]

    # Each individual symplectic involution has anti-invariant E8(-2).
    involution_reports = []
    for label, involution in (
        ("sigma_A", sigma_A),
        ("sigma_B", sigma_B),
        ("sigma_A*sigma_B", sigma_A * sigma_B),
    ):
        anti_basis = integer_kernel(involution + identity)
        anti_gram = anti_basis.T * gram_K3 * anti_basis
        assert anti_basis.shape == (22, 8)
        assert abs(int(anti_gram.det())) == 2 ** 8
        assert anti_gram.is_negative_definite

        # If anti_gram = E8(-2), then -anti_gram/2 is the positive E8 lattice:
        # integral, even, positive definite and unimodular of rank 8.
        e8_gram = -anti_gram / 2
        assert all(entry.q == 1 for entry in e8_gram)
        assert int(e8_gram.det()) == 1
        assert all(int(e8_gram[i, i]) % 2 == 0 for i in range(8))
        assert e8_gram.is_positive_definite
        involution_reports.append((label, abs(int(anti_gram.det()))))

    print("standard symplectic V4 K3-lattice certificate")
    print("=============================================")
    print("source                 : Piroddi arXiv:2408.00643, Prop. 1.2.1")
    print("W -> Lambda_K3 index   :", index_Lambda_over_W)
    print("Lambda_K3 determinant  :", int(gram_K3.det()))
    print("Lambda_K3 even         : yes")
    print("Lambda_K3 signature    : (3,19)")
    print()
    print("V4 generators")
    print("  integral on Lambda_K3: yes")
    print("  commute/order two    : yes")
    print("  traces               : 6, 6, 6")
    print()
    print("full V4 invariant lattice")
    print("  rank                  :", fixed_basis.shape[1])
    print("  |det|                 :", abs(int(fixed_gram.det())))
    print("  Smith divisors        :", fixed_elementary_divisors)
    print("  discriminant group    : (Z/2)^6 + (Z/4)^2")
    print()
    print("individual anti-invariants")
    for label, determinant in involution_reports:
        print(f"  {label:19s}: rank 8, |det|={determinant}, E8(-2) check PASS")
    print()
    print("VERDICT")
    print("  STANDARD SYMPLECTIC V4 INTEGRAL ACTION: PASS")
    print("  This is the correct replacement backend for the failed A1 sign action.")
    print("  The next gate is a commuting anti-symplectic JK tau in this centralizer.")


if __name__ == "__main__":
    main()
