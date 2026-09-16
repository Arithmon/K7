#!/usr/bin/env python3
"""Check the frozen JK character against the claimed quotient Betti numbers.

For a finite diagonal action on T^3 x K3, rational cohomology of the quotient
is the invariant part of product cohomology.  Every representation of
(Z/2)^3 on H^1(T^3; Q) splits into three one-dimensional characters.
This checks all 8^3 possible ordered character triples, without assuming a
particular torus action or a K3 realization.
"""

from itertools import product
from pathlib import Path


# Group bits are tau, sigma_A, sigma_B.  Values follow the frozen order in
# K7-GEO-JK-F1, with sigma_A*sigma_B encoded by 0b110.
H2_TRACE = (22, 0, 6, 0, 6, 0, 6, 0)


def character_value(character: int, element: int) -> int:
    return -1 if (character & element).bit_count() % 2 else 1


def multiplicities() -> tuple[int, ...]:
    numerators = [
        sum(trace * character_value(character, element)
            for element, trace in enumerate(H2_TRACE))
        for character in range(8)
    ]
    assert all(value % 8 == 0 for value in numerators)
    return tuple(value // 8 for value in numerators)


def quotient_betti(torus_characters: tuple[int, int, int], h2: tuple[int, ...]) -> tuple[int, int]:
    c0, c1, c2 = torus_characters
    # H^2 = Lambda^2 H^1(T^3) + H^2(K3).
    b2 = h2[0] + int(c0 == c1) + int(c0 == c2) + int(c1 == c2)
    # H^3 = Lambda^3 H^1(T^3) + H^1(T^3) tensor H^2(K3).
    b3 = int(c0 ^ c1 ^ c2 == 0) + h2[c0] + h2[c1] + h2[c2]
    return b2, b3


def main() -> None:
    freeze = Path(__file__).with_name("K7_P2_JK_geometry_freeze.md").read_text(encoding="utf-8")
    character_section = freeze.split("the frozen H² character is", 1)[1].split("## DERIVED CONSEQUENCES", 1)[0]
    assert "(22, 0, 6, 6, 0, 0, 6, 0)" in character_section, "frozen character changed"
    h2 = multiplicities()
    assert h2 == (5, 5, 2, 2, 2, 2, 2, 2)
    assert sum(h2) == 22
    pairs = {quotient_betti(chars, h2) for chars in product(range(8), repeat=3)}
    assert min(b2 for b2, _ in pairs) == 5
    assert max(b3 for _, b3 in pairs) == 16
    assert (0, 22) not in pairs
    # A common hyperkaehler triple is fixed by symplectic V4 and changed by
    # tau as (+,-,-).  G2 invariance forces the dual torus characters below.
    product_torus_characters = (0, 1, 1)
    assert quotient_betti(product_torus_characters, h2) == (6, 16)
    b1 = sum(character == 0 for character in product_torus_characters)
    assert b1 == 1
    print("H^2(K3) character multiplicities:", h2)
    print("All 512 torus-character triples: quotient b2 >=", min(b2 for b2, _ in pairs))
    print("All 512 torus-character triples: quotient b3 <=", max(b3 for _, b3 in pairs))
    print("Product G2 torus characters (1,tau,tau): quotient (b1,b2,b3) =", (b1, 6, 16))
    print("Claimed quotient Betti pair (0,22): IMPOSSIBLE for this diagonal action")


if __name__ == "__main__":
    main()
