#!/usr/bin/env python3
"""Target-free exact checks for the explicit JK Example 7.2 extension.

This checks the split torus action, rational character arithmetic and stratum
orbit counts. K3 fixed-locus topology is a mathematical input documented in
K7_P2_JK_F2_explicit_candidate_2026_09_16.md, not certified by this script.
"""

from fractions import Fraction
from itertools import product


ZERO = (0, 0, 0)


def xor(a: int, b: int) -> int:
    return a ^ b


def torus_map(mask: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """(diagonal signs, translations in half-period units), bits a,b,s."""
    a, b, s = ((mask >> i) & 1 for i in range(3))
    return ((-1) ** b, (-1) ** a, (-1) ** (a ^ b)), (s, 0, b)


def apply_torus(mask: int, point: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    signs, shifts = torus_map(mask)
    return tuple((sign * x + Fraction(shift, 2)) % 1 for sign, shift, x in zip(signs, shifts, point))


def fixed_circles(mask: int) -> tuple[int, tuple[tuple[Fraction, ...], ...]]:
    signs, shifts = torus_map(mask)
    if any(sign == 1 and shift for sign, shift in zip(signs, shifts)):
        return -1, ()
    free = [i for i, sign in enumerate(signs) if sign == 1]
    if len(free) != 1:
        return -1, ()
    axis = free[0]
    choices = [
        (Fraction(0),) if sign == 1 else
        (Fraction(shift, 4), Fraction(shift, 4) + Fraction(1, 2))
        for sign, shift in zip(signs, shifts)
    ]
    circles = tuple(tuple(point) for point in product(*choices))
    for point in circles:
        assert apply_torus(mask, point) == point
    return axis, circles


def orbit_count(mask: int) -> int:
    axis, circles = fixed_circles(mask)
    assert len(circles) == 4
    remaining = set(circles)
    count = 0
    while remaining:
        seed = remaining.pop()
        orbit = {
            tuple(Fraction(0) if i == axis else value for i, value in enumerate(apply_torus(g, seed)))
            for g in range(8)
        }
        assert orbit <= set(circles)
        remaining -= orbit
        count += 1
    return count


def h2_multiplicities(traces: dict[int, int]) -> dict[int, int]:
    return {
        character: sum(
            trace * (-1) ** ((character & element).bit_count() % 2)
            for element, trace in traces.items()
        ) // 8
        for character in range(8)
    }


def main() -> None:
    for g, h in product(range(8), repeat=2):
        # Signs commute and half-shifts are unchanged by signs modulo integers.
        for point in product((Fraction(0), Fraction(1, 4), Fraction(1, 2)), repeat=3):
            assert apply_torus(g, apply_torus(h, point)) == apply_torus(xor(g, h), point)

    fixed = {g: fixed_circles(g) for g in range(1, 8)}
    assert {g for g, (_, circles) in fixed.items() if circles} == {1, 2, 6}
    assert {g: orbit_count(g) for g in (1, 2, 6)} == {1: 2, 2: 1, 6: 1}
    assert fixed[1][0] == 0 and fixed[2][0] == fixed[6][0] == 1
    assert {p[2] for p in fixed[1][1]} == {Fraction(0), Fraction(1, 2)}
    assert {p[2] for p in fixed[2][1]} == {Fraction(1, 4), Fraction(3, 4)}
    assert {p[0] for p in fixed[2][1]} == {Fraction(0), Fraction(1, 2)}
    assert {p[0] for p in fixed[6][1]} == {Fraction(1, 4), Fraction(3, 4)}

    # Traces come from χ(Fix_X(g))−2 for the seven K3 involutions.
    # The topology and the treatment of weighted-projective real points are
    # reasoned in the note, independently of this finite arithmetic check.
    fixed_euler = {1: -18, 2: 2, 3: 0, 4: 8, 5: -2, 6: 2, 7: 0}
    traces = {0: 22, **{g: fixed_euler[g] - 2 for g in fixed_euler}}
    multiplicities = h2_multiplicities(traces)
    assert multiplicities == {0: 0, 1: 7, 2: 1, 3: 6, 4: 0, 5: 4, 6: 0, 7: 4}
    assert sum(multiplicities.values()) == 22
    coframe_characters = (2, 1, 3)  # dx1, dx2, dx3
    assert coframe_characters[0] ^ coframe_characters[1] ^ coframe_characters[2] == 0
    b1_quotient = sum(character == 0 for character in coframe_characters)
    b2_quotient = multiplicities[0] + sum(
        coframe_characters[i] == coframe_characters[j]
        for i in range(3) for j in range(i + 1, 3)
    )
    b3_quotient = 1 + sum(multiplicities[c] for c in coframe_characters)
    assert (b1_quotient, b2_quotient, b3_quotient) == (0, 0, 15)

    # Six ramification points on C10 for s|C; Riemann–Hurwitz gives genus 4.
    genus_curve, branch_points = 10, 6
    quotient_genus = ((2 * genus_curve - 2 - branch_points) // 2 + 2) // 2
    assert 2 * genus_curve - 2 == 2 * (2 * quotient_genus - 2) + branch_points
    assert quotient_genus == 4
    b0_singular = orbit_count(1) + orbit_count(2) + orbit_count(6)
    b1_singular = orbit_count(1) * (1 + 2 * quotient_genus) + orbit_count(2) + orbit_count(6)
    assert (b0_singular, b1_singular) == (4, 20)
    assert (b1_quotient, b2_quotient + b0_singular, b3_quotient + b1_singular) == (0, 4, 35)

    print("Torus fixed sectors: alpha=4 circles/2 orbits, beta=4/1, beta*s=4/1")
    print("H2 character multiplicities:", multiplicities)
    print("Quotient Betti (b1,b2,b3):", (b1_quotient, b2_quotient, b3_quotient))
    print("Singular strata (b0,b1):", (b0_singular, b1_singular))
    print("Ordinary A1 resolution Betti (b1,b2,b3):", (0, 4, 35))


if __name__ == "__main__":
    main()
