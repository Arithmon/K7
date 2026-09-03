#!/usr/bin/env python3
"""Reproduce K7-P1 without embedding any experimental target.

Primary K7 outputs:
    lambda3_K7 = sqrt(17)/32
    rho3_K7    = g_hhh/v = 6*lambda3_K7 = 3*sqrt(17)/16

Optional --mh/--v arguments only convert the frozen K7 coefficient into the
experimental kappa_lambda convention. They do not change the K7 prediction.
"""

from __future__ import annotations

import argparse
import json
import math


def k7_p1() -> dict[str, float | str]:
    lambda3 = math.sqrt(17.0) / 32.0
    rho3 = 6.0 * lambda3
    return {
        "lambda3_formula": "sqrt(17)/32",
        "lambda3_K7": lambda3,
        "rho3_formula": "3*sqrt(17)/16",
        "rho3_K7": rho3,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mh", type=float, help="Higgs-mass anchor in GeV for kappa_lambda conversion")
    parser.add_argument("--v", type=float, help="electroweak VEV anchor in GeV for conversion")
    args = parser.parse_args()

    if (args.mh is None) != (args.v is None):
        parser.error("--mh and --v must be supplied together")

    out: dict[str, object] = {
        "id": "K7-P1",
        "status": "frozen_tree_level_benchmark",
        "prediction": k7_p1(),
        "experimental_targets_embedded": False,
    }

    if args.mh is not None and args.v is not None:
        pred = out["prediction"]
        assert isinstance(pred, dict)
        rho3 = float(pred["rho3_K7"])
        g_hhh_k7 = rho3 * args.v
        g_hhh_sm = 3.0 * args.mh * args.mh / args.v
        out["conversion_only"] = {
            "mh_anchor_GeV": args.mh,
            "v_anchor_GeV": args.v,
            "g_hhh_K7_GeV": g_hhh_k7,
            "g_hhh_SM_reference_GeV": g_hhh_sm,
            "kappa_lambda_K7": g_hhh_k7 / g_hhh_sm,
            "note": "Anchors convert the frozen K7 coefficient; they are not K7 inputs.",
        }

    assert math.isclose(float(out["prediction"]["lambda3_K7"]), math.sqrt(17.0) / 32.0, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(float(out["prediction"]["rho3_K7"]), 3.0 * math.sqrt(17.0) / 16.0, rel_tol=0.0, abs_tol=1e-15)

    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
