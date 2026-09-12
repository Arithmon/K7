#!/usr/bin/env python3
"""Exact arithmetic check for the K7 rank-15 Clingher–Malmendier fiber gate.

This script reproduces only the lattice arithmetic that is public in the
companion note. It does not prove the geometric identification of the K7 fiber,
the Mordell–Weil translation action, the anti-symplectic JK involution, or a
global M/heterotic duality.

No experimental target is embedded or read.
"""

from __future__ import annotations

from math import gcd


def block_diag(*blocks: list[list[int]]) -> list[list[int]]:
    n = sum(len(b) for b in blocks)
    out = [[0 for _ in range(n)] for _ in range(n)]
    off = 0
    for b in blocks:
        m = len(b)
        for i in range(m):
            for j in range(m):
                out[off + i][off + j] = b[i][j]
        off += m
    return out


def det_bareiss(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant for an integer square matrix."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def pairing(q: list[list[int]], v: list[int], w: list[int]) -> int:
    return sum(v[i] * q[i][j] * w[j] for i in range(len(v)) for j in range(len(w)))


def primitive(v: list[int]) -> bool:
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    return g == 1


def unit(i: int, n: int) -> list[int]:
    return [1 if j == i else 0 for j in range(n)]


def add(a: list[int], b: list[int], ca: int = 1, cb: int = 1) -> list[int]:
    return [ca * x + cb * y for x, y in zip(a, b)]


def main() -> None:
    # Exact lattice used by the recovered canonical rank-15 work:
    # NS = U + E7(-1) + A1(-1)^6.
    U = [[0, 1], [1, 0]]
    E7 = [
        [2, -1, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0],
        [0, 0, -1, 2, -1, 0, -1],
        [0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, -1, 2, 0],
        [0, 0, 0, -1, 0, 0, 2],
    ]
    minus_E7 = [[-x for x in row] for row in E7]
    A1m = [[-2]]
    Q = block_diag(U, minus_E7, *([A1m] * 6))

    assert len(Q) == 15
    assert all(len(row) == 15 for row in Q)
    assert all(Q[i][j] == Q[j][i] for i in range(15) for j in range(15))
    assert all(Q[i][i] % 2 == 0 for i in range(15))

    det_q = det_bareiss(Q)
    assert det_q == 128

    # E7 Cartan is positive definite by Sylvester: all leading principal
    # minors are positive. Therefore -E7 is negative definite. Together with
    # U of signature (1,1) and six A1(-1), Q has signature (1,14).
    leading_minors = [det_bareiss([row[:k] for row in E7[:k]]) for k in range(1, 8)]
    assert leading_minors == [2, 3, 4, 5, 6, 7, 2]

    e = unit(0, 15)
    f = unit(1, 15)
    F = e
    S = add(f, e, 1, -1)  # f-e
    h = add(e, f, 4, 1)   # 4e+f

    assert primitive(F)
    assert primitive(S)
    assert primitive(h)
    assert pairing(Q, F, F) == 0
    assert pairing(Q, S, S) == -2
    assert pairing(Q, F, S) == 1
    assert pairing(Q, h, h) == 8

    # Any vector supported entirely in the negative E7+A1 block is orthogonal
    # to the U summand. The recovered Donaldson alpha_1 candidates lie in the
    # rank-4 M-perp contained in this negative block, so every such candidate
    # is orthogonal to F. A (-2)-reflection therefore fixes F.
    for i in range(2, 15):
        v = unit(i, 15)
        assert pairing(Q, F, v) == 0

    print("K7 rank-15 CM V4 fiber gate")
    print("============================")
    print("NS(X) = U + E7(-1) + A1(-1)^6")
    print(f"rank                         : {len(Q)}")
    print(f"det(NS)                      : {det_q} = 2^7")
    print(f"E7 leading principal minors  : {leading_minors}")
    print("signature                    : (1,14) by block decomposition")
    print("even lattice                 : yes")
    print()
    print(f"F^2                           : {pairing(Q, F, F)}")
    print(f"S^2                           : {pairing(Q, S, S)}")
    print(f"F.S                           : {pairing(Q, F, S)}")
    print(f"h^2 for h=4e+f               : {pairing(Q, h, h)}")
    print()
    print("CONDITIONAL INTERPRETATION:")
    print("  - F=e and S=f-e exhibit a Jacobian U inside the actual rank-15 NS lattice.")
    print("  - In the recovered Clingher-Malmendier model, the geometric V4 is generated")
    print("    by translations by independent 2-torsion sections, hence it preserves")
    print("    the elliptic fibration and its fiber class F.")
    print("  - The current Donaldson alpha_1 candidates live in M-perp, orthogonal to U;")
    print("    therefore every candidate Picard-Lefschetz reflection fixes F.")
    print()
    print("NOT ESTABLISHED BY THIS SCRIPT:")
    print("  - that the recovered rank-15 CM model is the final global K7 fiber")
    print("  - the full anti-symplectic / JK Z2^3 action on that same model")
    print("  - global matching needed for a controlled M/heterotic duality")
    print("  - any chiral spectrum, neutrino operator, or neutrino mass")


if __name__ == "__main__":
    main()
