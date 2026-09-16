#!/usr/bin/env python3
"""Enumerate the split affine T^3 actions compatible with frozen JK roles.

The standard product G2 three-form pairs the torus coframe with a common K3
hyperkaehler triple.  Symplectic V4 has linear torus action I; anti-symplectic
tau has D=diag(1,-1,-1).  The two V4 generators may translate by half periods.
After torus conjugation, tau has translation (epsilon/2,0,0), epsilon in F2.
This script counts fixed torus sectors using the frozen K3 fixed-point counts;
it does not construct a K3 group action or the full quotient strata.
"""

from collections import Counter
from itertools import product


ZERO = (0, 0, 0)
SHIFTS = tuple(product((0, 1), repeat=3))


def xor(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(x ^ y for x, y in zip(a, b))


def counts(a: tuple[int, int, int], b: tuple[int, int, int], epsilon: int) -> tuple[int, int, int]:
    shifts = (ZERO, a, b, xor(a, b))
    # Each surviving nonidentity V4 element has 8 isolated K3 fixed points,
    # hence four V4 orbits when the other generator acts freely on them.
    symplectic_orbits = 4 * sum(shift == ZERO for shift in shifts[1:])
    # For split D, an anti element has four fixed torus circles precisely when
    # its axial half-translation vanishes.
    anti_elements = sum((epsilon ^ shift[0]) == 0 for shift in shifts)
    anti_circles = 4 * anti_elements
    return symplectic_orbits, anti_elements, anti_circles


def main() -> None:
    census = Counter(counts(a, b, epsilon) for a in SHIFTS for b in SHIFTS for epsilon in (0, 1))
    assert sum(census.values()) == 128
    assert {row[0] for row in census} == {0, 4, 12}
    assert {row[1] for row in census} == {0, 2, 4}
    target_cases = [
        (a, b, epsilon) for a in SHIFTS for b in SHIFTS for epsilon in (0, 1)
        if counts(a, b, epsilon)[:2] == (12, 4)
    ]
    assert target_cases == [(ZERO, ZERO, 0)]
    assert counts(ZERO, ZERO, 0) == (12, 4, 16)
    print("Split affine actions enumerated:", sum(census.values()))
    print("Possible V4-orbit T3 sector counts:", sorted({row[0] for row in census}))
    print("Possible anti elements with torus fixed circles:", sorted({row[1] for row in census}))
    print("Cases retaining all 12 V4 orbits and all four anti sectors:", len(target_cases))
    print("Unique case: V4 translations zero, tau axial shift zero; four circles per anti element")
    print("K3 component orbits and multi-isotropy are NOT certified by this torus census")


if __name__ == "__main__":
    main()
