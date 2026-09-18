"""Reconstruct the archived matrix exactly, without supplying a missing basis."""
import ast
import json
from fractions import Fraction
import sympy as sp
from common import REPO, write_result

def run():
    nb=json.loads((REPO/"publications/papers/notebooks/g2_spectral_companion.ipynb").read_text())
    literals={}
    for node in ast.parse("".join(nb["cells"][13]["source"])).body:
        if isinstance(node,ast.Assign) and isinstance(node.targets[0],ast.Name):
            try:literals[node.targets[0].id]=ast.literal_eval(node.value)
            except (ValueError,TypeError):pass
    archived=json.loads((REPO/"publications/papers/notebooks/g2_spectral_companion_results.json").read_text())
    overlaps=archived["results"]["k7_2forms"]
    # Exact rational interpretation of the stored decimal literals, NOT an exact geometric pairing.
    q=[sp.Rational(str(v)) for v in literals["sd_vals"]+literals["asd_vals"]]
    r11,r22,r12=[sp.Rational(str(overlaps[k])) for k in ["R11","R22","R12"]]
    matrix=sp.zeros(21)
    for i in range(11):matrix[i,i]=r11*q[i]
    for i in range(10):
        matrix[11+i,11+i]=r22*q[i]
        matrix[i,11+i]=matrix[11+i,i]=r12*q[i]
    _,D=matrix.LDLdecomposition(hermitian=False)
    inertia=[sum(bool(D[i,i]>0) for i in range(21)),sum(bool(D[i,i]<0) for i in range(21))]
    write_result("intersection_form.json",{
        "status":"PENDING","scope":"exact arithmetic reconstruction of historical numerical recipe",
        "matrix_exact_rationals":[[str(matrix[i,j]) for j in range(21)] for i in range(21)],
        "LDL_pivots":[str(D[i,i]) for i in range(21)],
        "historical_recipe_signature":inertia,"target_signature":[3,18],
        "target_signature_passed":inertia==[3,18],
        "basis_provenance":None,"geometric_matrix":None,
        "blocked_by":["The two blocks reuse the same positive directions; the archived recipe has signature (6,15).",
                      "Stored eigenvalues and radial overlaps do not identify an integral basis in H^2(K3).",
                      "No matching-selected rank-21 sublattice embedding is supplied."]
    })

if __name__ == "__main__": run()
