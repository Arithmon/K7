#!/usr/bin/env python3
"""Exact character check for the K7 K3 Joyce--Karigiannis target package.

This reproducer contains no neutrino-mass target and no experimental input.
It checks only finite-group character arithmetic implied by the currently
stated K3 fixed-locus package:

- G = (Z/2)^3 = <tau, sigma_A, sigma_B>;
- the three nontrivial V4 elements are symplectic involutions, hence have
  eight isolated fixed points and trace 6 on H^2(K3);
- tau has Nikulin type (r,a,delta)=(11,7,1), giving fixed locus C_2 + 2 P^1;
- each tau*sigma coset has type (11,9,1), giving C_1 + P^1;
- a finite symplectic K3 automorphism acts trivially on T_X;
- a non-symplectic involution acts as -1 on T_X because its invariant lattice
  is algebraic.

Under those assumptions the rank-15 package is impossible: the induced
character on NS(X) has a negative irreducible-character multiplicity.  The
same arithmetic shows rho(X) >= 17 is necessary for this exact JK profile.
"""

from __future__ import annotations

from dataclasses import dataclass


# Group elements are bits (tau, sigma_A, sigma_B), in this fixed order.
GROUP = (
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
)
NAMES = (
    "id",
    "tau",
    "sigma_A",
    "sigma_B",
    "tau_sigma_A",
    "tau_sigma_B",
    "sigma_A_sigma_B",
    "tau_sigma_A_sigma_B",
)


def chi(character: tuple[int, int, int], element: tuple[int, int, int]) -> int:
    exponent = sum(c * g for c, g in zip(character, element)) % 2
    return -1 if exponent else 1


def fourier_multiplicities(traces: tuple[int, ...]) -> dict[tuple[int, int, int], int]:
    assert len(traces) == 8
    out: dict[tuple[int, int, int], int] = {}
    for character in GROUP:
        numerator = sum(t * chi(character, g) for t, g in zip(traces, GROUP))
        assert numerator % 8 == 0
        out[character] = numerator // 8
    return out


def nikulin_fixed_locus(r: int, a: int) -> tuple[int, int]:
    """Return (g,k) for the non-exceptional 2-elementary fixed-locus formula."""
    assert (22 - r - a) % 2 == 0
    assert (r - a) % 2 == 0
    return ((22 - r - a) // 2, (r - a) // 2)


def fixed_euler(g: int, k: int) -> int:
    # One genus-g curve plus k rational curves.
    return (2 - 2 * g) + 2 * k


def target_h2_traces() -> tuple[int, ...]:
    # Symplectic involution: 8 fixed points -> tr(H^2)=8-2=6.
    symplectic_trace = 6

    tau_gk = nikulin_fixed_locus(11, 7)
    coset_gk = nikulin_fixed_locus(11, 9)
    assert tau_gk == (2, 2)
    assert coset_gk == (1, 1)

    # Both fixed loci have Euler characteristic 2, hence tr(H^2)=0.
    tau_trace = fixed_euler(*tau_gk) - 2
    coset_trace = fixed_euler(*coset_gk) - 2
    assert tau_trace == 0
    assert coset_trace == 0

    return (
        22,
        tau_trace,
        symplectic_trace,
        symplectic_trace,
        coset_trace,
        coset_trace,
        symplectic_trace,
        coset_trace,
    )


def transcendental_traces(rho: int) -> tuple[int, ...]:
    t_rank = 22 - rho
    assert t_rank >= 2
    # V4 symplectic -> +I on T_X; tau-coset -> -I on T_X.
    return (
        t_rank,
        -t_rank,
        t_rank,
        t_rank,
        -t_rank,
        -t_rank,
        t_rank,
        -t_rank,
    )


def ns_traces(rho: int) -> tuple[int, ...]:
    h2 = target_h2_traces()
    tx = transcendental_traces(rho)
    return tuple(a - b for a, b in zip(h2, tx))


@dataclass(frozen=True)
class GateResult:
    rho: int
    t_rank: int
    traces_ns: tuple[int, ...]
    multiplicities_ns: dict[tuple[int, int, int], int]

    @property
    def representation_possible(self) -> bool:
        return all(m >= 0 for m in self.multiplicities_ns.values())


def evaluate(rho: int) -> GateResult:
    traces = ns_traces(rho)
    mult = fourier_multiplicities(traces)
    return GateResult(rho, 22 - rho, traces, mult)


def main() -> None:
    h2 = target_h2_traces()
    h2_mult = fourier_multiplicities(h2)
    assert all(m >= 0 for m in h2_mult.values())

    # The character (1,0,0) is the one that changes sign only with tau.
    tau_character = (1, 0, 0)

    r15 = evaluate(15)
    assert r15.traces_ns == (15, 7, -1, -1, 7, 7, -1, 7)
    assert r15.multiplicities_ns[tau_character] == -2
    assert not r15.representation_possible

    scan = [evaluate(rho) for rho in range(13, 21)]
    feasible = [r.rho for r in scan if r.representation_possible]
    assert feasible
    rho_min = min(feasible)
    assert rho_min == 17

    # Closed form check: multiplicity of the tau-only character is rho-17.
    for result in scan:
        assert result.multiplicities_ns[tau_character] == result.rho - 17

    # The full G-invariant rank is the trivial-character multiplicity.
    # It is 5 for every rho compatible with this fixed H^2 character.
    for result in scan:
        assert result.multiplicities_ns[(0, 0, 0)] == 5

    print("K7 JK character gate")
    print("====================")
    print("target Nikulin loci:")
    print("  tau       (11,7,1) -> (g,k) =", nikulin_fixed_locus(11, 7))
    print("  tau*sigma (11,9,1) -> (g,k) =", nikulin_fixed_locus(11, 9))
    print("  therefore tau*sigma is NOT free")
    print()
    print("traces on H^2 in order")
    print(" ", NAMES)
    print(" ", h2)
    print()
    print("rho=15:")
    print("  rank(T_X)             :", r15.t_rank)
    print("  traces on NS          :", r15.traces_ns)
    print("  NS multiplicities     :", r15.multiplicities_ns)
    print("  tau-only multiplicity :", r15.multiplicities_ns[tau_character])
    print("  verdict               : IMPOSSIBLE")
    print()
    print("rho scan:")
    for result in scan:
        m_tau = result.multiplicities_ns[tau_character]
        print(
            f"  rho={result.rho:2d}  rank(T)={result.t_rank:2d}  "
            f"m_tau={m_tau:2d}  representation_possible={result.representation_possible}"
        )
    print()
    print("NECESSARY CONDITION FOR THE STATED JK PROFILE:")
    print("  m_tau = rho - 17 >= 0  ->  rho >= 17")
    print("  rank H^2(K3)^G = rank NS(X)^G = 5")
    print()
    print("SCOPE:")
    print("  This kills the rank-15 full JK package, not every possible higher-Picard route.")
    print("  It does not construct a rho>=17 model, prove nefness, produce a section for")
    print("  the common invariant isotropic class, or establish a heterotic dual.")


if __name__ == "__main__":
    main()
