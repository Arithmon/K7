#!/usr/bin/env python3
"""Exact discriminant-form decomposition for the standard symplectic V4.

Starting from the Piroddi integral V4 model already certified by
check_k3_standard_symplectic_v4.py, this script computes

    M = Lambda_K3^V4,
    Omega = M^perp,

then exposes the full finite quadratic modules A_M and A_Omega and the gluing
anti-isometry induced by the ambient unimodular K3 lattice.

The important point is stronger than matching determinants: the graph of the
anti-isometry is reconstructed explicitly and q_Omega(phi(x)) = -q_M(x) is
checked on all 1024 discriminant classes.

No K7 observable or experimental target enters the calculation.
"""

from __future__ import annotations

import itertools
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

import check_k3_standard_symplectic_v4 as standard


def integer_kernel(matrix: sp.Matrix) -> sp.Matrix:
    """Primitive Z-basis of ker(matrix: Z^n -> Z^m), via Smith decomposition."""
    dm = DomainMatrix.from_Matrix(matrix).convert_to(ZZ)
    smith, _, right = smith_normal_decomp(dm)
    diagonal = smith.to_Matrix()
    transform = right.to_Matrix()
    rank = sum(1 for i in range(min(diagonal.shape)) if diagonal[i, i] != 0)
    return transform[:, rank:]


def mod1(value: sp.Rational) -> sp.Rational:
    value = sp.Rational(value)
    return sp.Rational(int(value.p) % int(value.q), int(value.q))


def mod2(value: sp.Rational) -> sp.Rational:
    value = sp.Rational(value)
    return sp.Rational(int(value.p) % (2 * int(value.q)), int(value.q))


def reduced_q_matrix(matrix: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(*matrix.shape)
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            out[i, j] = mod2(matrix[i, j]) if i == j else mod1(matrix[i, j])
    return out


def discriminant_data(gram: sp.Matrix):
    """SNF coordinates for A_L = L^*/L and its quadratic-form matrix."""
    dm = DomainMatrix.from_Matrix(gram).convert_to(ZZ)
    smith, left, right = smith_normal_decomp(dm)
    diagonal = smith.to_Matrix()
    left = left.to_Matrix()
    right = right.to_Matrix()

    divisors = [abs(int(diagonal[i, i])) for i in range(gram.rows)]
    nontrivial = [i for i, d in enumerate(divisors) if d > 1]

    # For Z^n / G Z^n, left*z gives SNF coordinates.  A generator of the
    # i-th SNF factor is therefore represented by z=left^{-1} e_i, and the
    # corresponding dual vector is G^{-1} z.
    z_generators = left.inv()[:, nontrivial]
    q_matrix = sp.simplify(z_generators.T * gram.inv() * z_generators)

    return divisors, nontrivial, z_generators, reduced_q_matrix(q_matrix), left, right


def build_standard_v4():
    """Reconstruct Piroddi's Lambda_K3 and the standard V4 matrices."""
    A2 = sp.Matrix([[-2, 1], [1, -2]])
    A2_2 = 2 * A2
    U3 = sp.Matrix([[0, 3], [3, 0]])
    final_block = sp.Matrix([[4, 2], [2, 4]])
    gram_W = sp.diag(*([A2] * 8 + [A2_2, U3, final_block]))

    lin = standard.linear_combination
    e = standard.basis_vector

    alpha = lin({
        "a1": -1, "a2": 1, "d1": 1, "d2": -1,
        "e1": -1, "e2": 1, "f1": 1, "f2": -1,
        "g1": -1, "g2": 1, "h1": 1, "h2": -1,
    }, 3)
    beta = lin({
        "b1": -1, "b2": 1, "c1": 1, "c2": -1,
        "e1": -1, "e2": 1, "f1": 1, "f2": -1,
        "g1": 1, "g2": -1, "h1": -1, "h2": 1,
    }, 3)
    gamma = lin({
        "x": 1, "y": -1, "e1": -1, "e2": 1, "f1": -1, "f2": 1,
    }, 3)
    delta = lin({
        "x": 1, "c1": -1, "c2": 1, "d1": -1, "d2": 1,
        "e1": -1, "e2": 1,
    }, 3)
    epsilon = lin({
        "x": 1, "z": -1, "w": 1, "c1": 1, "c2": -1,
        "e1": -1, "e2": 1, "g1": -1, "g2": 1,
        "h1": 1, "h2": -1,
    }, 3)
    zeta = (
        lin({
            "x": 1, "z": 1, "c1": 1, "c2": 1,
            "e1": 1, "e2": 1, "g1": 1, "g2": 1,
            "h1": 1, "h2": 1,
        }) + epsilon
    ) / 2 + e("v2") / 2
    eta = (
        lin({"x": 1, "c1": 1, "c2": 1, "e1": 1, "e2": 1}) + epsilon
    ) / 2 + lin({
        "g1": 1, "g2": -1, "h1": 1, "h2": -1,
    }, 6) + e("v1") / 6 - e("v2") / 3

    scale = 6
    generators = [sp.eye(22)[:, i] * scale for i in range(22)]
    generators += [v * scale for v in (alpha, beta, gamma, delta, epsilon, zeta, eta)]
    generator_matrix = standard.integer_matrix(sp.Matrix.hstack(*generators))
    hnf = hermite_normal_form(generator_matrix)
    basis = hnf / sp.Integer(scale)
    gram = sp.simplify(basis.T * gram_W * basis)

    assert int(gram.det()) == -1
    assert all(int(gram[i, i]) % 2 == 0 for i in range(22))

    change_inverse = basis.inv()
    sigma_A = standard.integer_matrix(
        sp.simplify(change_inverse * standard.action_on_W("sigma_A") * basis)
    )
    sigma_B = standard.integer_matrix(
        sp.simplify(change_inverse * standard.action_on_W("sigma_B") * basis)
    )

    return gram, sigma_A, sigma_B


def discr_coords_from_fraction(
    fraction: sp.Matrix,
    gram: sp.Matrix,
    left: sp.Matrix,
    divisors: list[int],
) -> tuple[int, ...]:
    z = gram * fraction
    assert all(sp.Rational(entry).q == 1 for entry in z)
    z = sp.Matrix([int(entry) for entry in z])
    snf = left * z
    return tuple(
        int(snf[i]) % d
        for i, d in enumerate(divisors)
        if d > 1
    )


def add_coords(a, b, orders):
    return tuple((x + y) % d for x, y, d in zip(a, b, orders))


def linear_combination_coords(coeffs, generators, orders):
    out = (0,) * len(orders)
    for coefficient, generator in zip(coeffs, generators):
        for _ in range(coefficient):
            out = add_coords(out, generator, orders)
    return out


def q_value(coords, q_matrix):
    vector = sp.Matrix(coords)
    return mod2((vector.T * q_matrix * vector)[0])


def main() -> None:
    gram, sigma_A, sigma_B = build_standard_v4()
    identity = sp.eye(22)

    # Integral invariant and coinvariant lattices.
    M_basis = integer_kernel(sp.Matrix.vstack(
        sigma_A - identity,
        sigma_B - identity,
    ))
    M_gram = sp.simplify(M_basis.T * gram * M_basis)

    Omega_basis = integer_kernel(M_basis.T * gram)
    Omega_gram = sp.simplify(Omega_basis.T * gram * Omega_basis)

    assert M_basis.shape == (22, 10)
    assert Omega_basis.shape == (22, 12)
    assert Omega_gram.is_negative_definite
    assert abs(int(M_gram.det())) == 2 ** 10
    assert abs(int(Omega_gram.det())) == 2 ** 10

    M_snf = smith_normal_form(M_gram, domain=ZZ)
    O_snf = smith_normal_form(Omega_gram, domain=ZZ)
    M_divisors_expected = [1, 1, 2, 2, 2, 2, 2, 2, 4, 4]
    O_divisors_expected = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4]
    assert [abs(int(M_snf[i, i])) for i in range(10)] == M_divisors_expected
    assert [abs(int(O_snf[i, i])) for i in range(12)] == O_divisors_expected

    M_divisors, _, _, qM, left_M, _ = discriminant_data(M_gram)
    O_divisors, _, _, qO, left_O, _ = discriminant_data(Omega_gram)
    orders_M = [d for d in M_divisors if d > 1]
    orders_O = [d for d in O_divisors if d > 1]
    assert orders_M == orders_O == [2, 2, 2, 2, 2, 2, 4, 4]
    orders = orders_M

    # M+Omega inside Lambda_K3.  Since both are primitive orthogonal
    # complements in the unimodular lattice, the quotient must be the graph
    # of an anti-isometry between their full discriminant groups.  We extract
    # that graph explicitly from the ambient integral basis.
    direct_basis = sp.Matrix.hstack(M_basis, Omega_basis)
    direct_index = abs(int(direct_basis.det()))
    assert direct_index == 2 ** 10

    smith_P, left_P, _ = smith_normal_decomp(
        DomainMatrix.from_Matrix(direct_basis).convert_to(ZZ)
    )
    diag_P = smith_P.to_Matrix()
    left_P = left_P.to_Matrix()
    quotient_divisors = [abs(int(diag_P[i, i])) for i in range(22)]
    assert [d for d in quotient_divisors if d > 1] == orders

    direct_inverse = direct_basis.inv()
    left_P_inverse = left_P.inv()
    quotient_indices = [i for i, d in enumerate(quotient_divisors) if d > 1]

    graph_generators = []
    for i in quotient_indices:
        ambient_vector = left_P_inverse[:, i]
        assert all(sp.Rational(x).q == 1 for x in ambient_vector)
        coordinates = direct_inverse * ambient_vector
        m_fraction = coordinates[:10, :]
        o_fraction = coordinates[10:, :]

        m_class = discr_coords_from_fraction(
            m_fraction, M_gram, left_M, M_divisors
        )
        o_class = discr_coords_from_fraction(
            o_fraction, Omega_gram, left_O, O_divisors
        )
        graph_generators.append((quotient_divisors[i], m_class, o_class))

    m_generators = [entry[1] for entry in graph_generators]
    o_generators = [entry[2] for entry in graph_generators]

    graph = {}
    image_M = set()
    image_O = set()
    for coefficients in itertools.product(*[range(d) for d in orders]):
        m_class = linear_combination_coords(coefficients, m_generators, orders)
        o_class = linear_combination_coords(coefficients, o_generators, orders)
        image_M.add(m_class)
        image_O.add(o_class)
        graph[m_class] = o_class

    assert len(image_M) == len(image_O) == len(graph) == 2 ** 10

    # Full quadratic-form anti-isometry check, not just bilinear/determinant.
    for m_class, o_class in graph.items():
        assert mod2(q_value(m_class, qM) + q_value(o_class, qO)) == 0

    # Images of the standard SNF generators of A_M under phi.
    phi_standard = []
    for i in range(8):
        generator = [0] * 8
        generator[i] = 1
        phi_standard.append(graph[tuple(generator)])

    print("rho=17 standard-V4 discriminant gluing certificate")
    print("==================================================")
    print("M = Lambda_K3^V4")
    print("  rank                   : 10")
    print("  signature              : (3,7)")
    print("  |disc|                 : 2^10")
    print("  Smith divisors         :", M_divisors_expected)
    print()
    print("Omega = M^perp")
    print("  rank                   : 12")
    print("  signature              : (0,12)")
    print("  |disc|                 : 2^10")
    print("  Smith divisors         :", O_divisors_expected)
    print()
    print("A_M ~= A_Omega           : (Z/2)^6 + (Z/4)^2")
    print("[Lambda:M+Omega]         : 2^10")
    print("gluing graph size        : 1024")
    print("q anti-isometry check    : PASS on all 1024 classes")
    print()
    print("q_M in SNF generator coordinates (diag mod 2, off-diag mod 1):")
    print(qM)
    print()
    print("q_Omega in SNF generator coordinates (diag mod 2, off-diag mod 1):")
    print(qO)
    print()
    print("phi: A_M -> A_Omega, images of standard generators")
    print("orders                  :", orders)
    for i, image in enumerate(phi_standard):
        print(f"  e{i} -> {image}")
    print()
    print("NEXT GATE")
    print("  Search tau_M in O(M) with eigensignatures (1,4)+(2,3), and")
    print("  tau_Omega in C_O(Omega)(V4) with three rational 2+2 splits.")
    print("  Keep only pairs whose induced discriminant actions satisfy")
    print("      phi o bar(tau_M) = bar(tau_Omega) o phi.")
    print("  Only then lift back to Lambda_K3 and test JK a=(7,9,9,9).")


if __name__ == "__main__":
    main()
