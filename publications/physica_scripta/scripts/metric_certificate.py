"""Audit the historical NK contract. Does not manufacture an inverse certificate."""
import ast
import json
import math
import numpy as np
from common import ROOT, REPO, read, metric, validate_freeze, write_result

def run():
    validate_freeze()
    source = REPO/"publications/papers/notebooks/g2_certified_neck_companion.ipynb"
    cells = json.loads(source.read_text())["cells"]
    code = "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "code")
    literals = {}
    for node in ast.parse(code).body:
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            try: literals[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError): pass
    old = json.loads((REPO/"publications/papers/notebooks/g2_certified_neck_companion_results.json").read_text())["results"]
    beta = 1/literals["LAMBDA1_PERP"]
    omega = literals["OMEGA_CERTIFIED"]
    # This calculation diagnoses the old arithmetic; eta is explicitly archived.
    historical_h = beta*old["NK_eta"]*omega
    g, _ = metric(np.linspace(-2,3,1001))
    reasons = [
        "DF: R^168 -> C^0(I, Lambda^4 + Lambda^5) cannot have a two-sided inverse onto the stated infinite-dimensional codomain.",
        "No square projected residual, gauge fixing, boundary constraints or validated right inverse with compatibility proof is supplied.",
        "Only raw Cholesky coordinates lie in P_5; softplus and determinant normalization make the reconstructed metric and torsion non-polynomial in general.",
        "The relative nonlinear metric displacement is not a specified fixed norm on coefficient space.",
        "A finite DCT bounds an interpolant; a bound for the interpolation remainder and rounding is missing.",
        "beta is derived from an embedded spectral-gap literal; omega is an embedded finite-difference safety-factor literal.",
        "With raw residual eta and raw derivative Lipschitz omega, the classical sufficient majorant uses h = beta^2 eta omega. The beta eta omega convention requires a preconditioned quantity.",
        "A scalar Sturm-Liouville inverse estimate does not establish invertibility of the torsion Jacobian.",
        "No globally defined fixed K3 metric, atlas or certified fibre bridge is included in the embedded coefficient input."
    ]
    write_result("nk_certificate.json", {
        "status":"PENDING", "certifies_torsion_free_metric":False,
        "parameter_space":"R^168, gamma fixed", "raw_polynomial_space":"P_5(I; R^28)",
        "reconstruction":"c -> raw polynomial -> softplus Cholesky -> determinant-normalized metric -> continuous torsion; not a polynomial torsion map",
        "codomain":"C^0(I; Lambda^4 + Lambda^5), local coordinate model",
        "norm":None, "neighborhood":None, "inverse_object":None,
        "beta":None, "eta":None, "omega":None, "h":None,
        "blocked_by":reasons,
        "historical_diagnostic":{"beta_from_literal":beta,"eta_archived":old["NK_eta"],
            "omega_literal":omega,"h_recomputed_not_certified":historical_h,
            "h_with_raw_lipschitz_convention":beta*historical_h},
        "metric_diagnostic":{"min_sampled_eigenvalue":float(np.linalg.eigvalsh(g).min()),
                            "max_sampled_determinant_error":float(abs(np.linalg.det(g)-65/32).max())},
        "values":{"parameter_count":168,"determinant":"65/32", "zero":0,
                  "one":1,"two":2,"dimension":7,"left_endpoint":-2,"right_endpoint":3},
        "proof":"Positive diagonal softplus gives invertible L; scaling gives det(g)=65/32 exactly in real arithmetic. This proves SPD of this coordinate ansatz, not global K3 geometry."
    })

if __name__ == "__main__": run()
