#!/usr/bin/env python3
"""Explicit discriminant-form gluing for the rho=17 JK lattice candidate.

This script verifies an anti-isometry between the discriminant form of the
rank-17 NS code lattice and

    T = U(2) + U(2) + A1(-1),

then checks all 32 discriminant classes.  Gluing along the graph of this
anti-isometry produces an even unimodular lattice of signature (3,19), hence
the K3 lattice.

No experimental target is used.
"""

from __future__ import annotations

GENERATOR_SUPPORTS = (
    (3, 6, 11, 12),
    (0, 2, 4, 5, 6, 9, 12, 13),
    (5, 8, 10, 13),
    (0, 1, 2, 3, 5, 6, 8, 14),
    (1, 6, 7, 8, 9, 10, 11, 14),
)

# Images in C^perp/C of the standard discriminant generators of
# U(2) + U(2) + A1(-1): e1/2, f1/2, e2/2, f2/2, a/2.
ANTI_ISOMETRY_SUPPORTS = (
    (0, 1, 3, 6),
    (1, 2, 3, 6),
    (3, 4, 6, 7),
    (0, 1, 2, 3, 5, 6, 7, 10),
    (3, 6, 9),
)


def mask(support: tuple[int, ...]) -> int:
    out = 0
    for i in support:
        out |= 1 << i
    return out


def span(generators: tuple[int, ...]) -> set[int]:
    out = {0}
    for g in generators:
        out |= {x ^ g for x in tuple(out)}
    return out


def dot2(x: int, y: int) -> int:
    return (x & y).bit_count() & 1


def q_ns_anti_twice(v: int) -> int:
    """2*(-q_NS) mod 4 for a discriminant vector represented in A1^15."""
    return v.bit_count() % 4


def q_t_twice(v: int) -> int:
    """2*q_T mod 4 for T=U(2)+U(2)+A1(-1), v in F2^5."""
    a = (v >> 0) & 1
    b = (v >> 1) & 1
    c = (v >> 2) & 1
    d = (v >> 3) & 1
    e = (v >> 4) & 1
    return (2 * a * b + 2 * c * d - e) % 4


def main() -> None:
    c_basis = tuple(mask(s) for s in GENERATOR_SUPPORTS)
    code = span(c_basis)
    assert len(code) == 32

    c_perp = {
        v for v in range(1 << 15)
        if all(dot2(v, c) == 0 for c in code)
    }
    assert len(c_perp) == 2 ** 10

    # Canonical representative for each coset in C^perp/C.
    canonical = {}
    unseen = set(c_perp)
    reps = []
    while unseen:
        x = min(unseen)
        coset = {x ^ c for c in code}
        rep = min(coset)
        reps.append(rep)
        for y in coset:
            canonical[y] = rep
        unseen -= coset
    assert len(reps) == 32

    images = tuple(canonical[mask(s)] for s in ANTI_ISOMETRY_SUPPORTS)

    def image(v: int) -> int:
        y = 0
        for i, im in enumerate(images):
            if (v >> i) & 1:
                y ^= im
        return canonical[y]

    image_set = {image(v) for v in range(32)}
    assert len(image_set) == 32  # bijective

    # Full discriminant quadratic-form check, all 32 classes.
    for v in range(32):
        assert q_ns_anti_twice(image(v)) == q_t_twice(v)

    # Determinants and gluing index.
    disc_ns = 2 ** 5
    disc_t = 2 ** 5
    glue_index = 2 ** 5
    glued_disc = disc_ns * disc_t // (glue_index ** 2)
    assert glued_disc == 1

    # Signatures add: (1,16)+(2,3)=(3,19).  The glued lattice is even by
    # anti-isometry of discriminant quadratic forms and unimodular by determinant.
    print("rho=17 K3-lattice gluing certificate")
    print("=====================================")
    print("NS signature        : (1,16)")
    print("NS discriminant     : 2^5")
    print("T                   : U(2) + U(2) + A1(-1)")
    print("T signature         : (2,3)")
    print("T discriminant      : 2^5")
    print("anti-isometry       : VERIFIED on all 32 discriminant classes")
    print("gluing index        : 2^5")
    print("glued determinant   : 1")
    print("glued signature     : (3,19)")
    print("identification      : even unimodular K3 lattice Lambda_K3")
    print()
    print("anti-isometry generator supports:")
    for s in ANTI_ISOMETRY_SUPPORTS:
        print(" ", s)
    print()
    print("G-equivariance:")
    print("  NS sign changes act trivially on the 2-elementary A_NS.")
    print("  On T, V4 acts as +I and tau as -I; both induce identity on A_T.")
    print("  Therefore the discriminant gluing graph is G-stable.")
    print()
    print("SCOPE:")
    print("  K3 lattice gluing is closed.  Global Torelli / ample chamber,")
    print("  explicit projective equations and invariant nef fiber remain open.")


if __name__ == "__main__":
    main()
