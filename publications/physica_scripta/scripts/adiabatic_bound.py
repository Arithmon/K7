"""Same-metric diagnostics; separate these from an unproved full operator bound."""
from fractions import Fraction
import numpy as np
from common import metric, write_result

def run():
    g, _ = metric(np.linspace(-2,3,1001))
    reference = g.mean(axis=0)
    blocks = np.zeros((7,7))
    for ids in [[0],[1,6],[2,3,4,5]]:
        blocks[np.ix_(ids,ids)] = reference[np.ix_(ids,ids)]
    d,U = np.linalg.eigh(blocks)
    root_inv = (U/np.sqrt(d))@U.T
    rel = np.linalg.eigvalsh(root_inv @ g @ root_inv - np.eye(7))
    eps = float(abs(rel).max())
    wrong_sum = Fraction(2,1000)+2*Fraction(135,10**9)
    write_result("adiabatic_bound.json", {
        "status":"PENDING", "reference_matrix":blocks.tolist(),
        "sampled_relative_operator_deviation":eps, "sample_count":len(g),
        "epsilon_ad_certified":None,"full_spectral_relative_error":None,
        "historical_triangle_rhs_exact":str(wrong_sum),
        "historical_triangle_le_0_002":wrong_sum <= Fraction(2,1000),
        "scalar_comparison_theorem":{
            "hypothesis":"(1-e) g0 <= g <= (1+e) g0 as quadratic forms everywhere; same scalar form domain",
            "lower":"(1-e)^(d/2)/(1+e)^(d/2+1)",
            "upper":"(1+e)^(d/2)/(1-e)^(d/2+1)",
            "proof":"Bound inverse metrics and volume densities in both scalar Rayleigh quotients, then apply min-max.",
            "scope":"scalar eigenvalues only; no blanket Hodge-form perturbation bound"},
        "blocked_by":["Sampled comparison of coordinate matrices is not a bound on the global K3 metric.",
                      "NK correction to g* is not certified.",
                      "The historical 0.78 percent operator estimate has no form-domain/volume-density proof.",
                      "The historical triangle-inequality rounding rounds an upper bound down."]
    })

if __name__ == "__main__": run()
