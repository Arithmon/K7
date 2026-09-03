#!/usr/bin/env python3
"""Minimal K7 arithmetic reproducer for the OpenWave candidate dossier.

Deliberately contains NO experimental target values.

It reproduces a small set of ledger-to-output relations and the arithmetic
part of K7-P1. It does not claim that the physical identifications are thereby
derived.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction


def main() -> None:
    # Declared structural ledger used by this minimal reproducer.
    b2 = 21
    b3 = 77
    dim_g2 = 14
    dim_k7 = 7
    p2 = 2
    h_star = b2 + b3 + 1  # 99

    # Exact / algebraic assembly.
    sin2_theta_w = Fraction(b2, b3 + dim_g2)  # 21 / 91 = 3 / 13
    koide_q = Fraction(dim_g2, b2)             # 14 / 21 = 2 / 3
    kappa_t = Fraction(1, b3 - dim_g2 - p2)    # 1 / 61
    delta_cp_deg = dim_k7 * dim_g2 + h_star    # 197

    lambda_h = math.sqrt(17.0) / 32.0
    rho3_tree = 6.0 * lambda_h

    out = {
        "ledger": {
            "b2": b2,
            "b3": b3,
            "dim_G2": dim_g2,
            "dim_K7": dim_k7,
            "p2": p2,
            "H_star": h_star,
        },
        "relations": {
            "sin2_theta_W": {
                "exact": f"{sin2_theta_w.numerator}/{sin2_theta_w.denominator}",
                "value": float(sin2_theta_w),
            },
            "Koide_Q": {
                "exact": f"{koide_q.numerator}/{koide_q.denominator}",
                "value": float(koide_q),
            },
            "kappa_T": {
                "exact": f"{kappa_t.numerator}/{kappa_t.denominator}",
                "value": float(kappa_t),
            },
            "delta_CP_deg": delta_cp_deg,
            "lambda_H": lambda_h,
        },
        "K7_P1_tree_benchmark": {
            "status": "frozen_tree_level_benchmark",
            "rho3_tree_formula": "3*sqrt(17)/16",
            "rho3_tree": rho3_tree,
            "experimental_targets_embedded": False,
        },
    }

    # Internal arithmetic guards. These are not experimental tests.
    assert sin2_theta_w == Fraction(3, 13)
    assert koide_q == Fraction(2, 3)
    assert kappa_t == Fraction(1, 61)
    assert delta_cp_deg == 197
    assert math.isclose(rho3_tree, 3.0 * math.sqrt(17.0) / 16.0, rel_tol=0.0, abs_tol=1e-15)

    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
