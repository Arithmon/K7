"""Fresh deterministic reduced scalar spectrum: conservative P1 mass-lumped FEM."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from common import coefficients, write_result

def solve(n, count=40):
    s = np.linspace(-2,3,n)
    h = s[1]-s[0]
    p,w = coefficients(s)
    p_mid,_ = coefficients((s[1:]+s[:-1])/2)
    edge = p_mid/h
    mass = h*w
    mass[[0,-1]] *= .5
    diagonal = np.zeros(n)
    diagonal[:-1] += edge; diagonal[1:] += edge
    vals, vectors = eigh_tridiagonal(diagonal/mass, -edge/np.sqrt(mass[:-1]*mass[1:]),
                                    select="i", select_range=(0,count-1))
    residual = (diagonal/mass)[:,None]*vectors - vectors*vals
    off = -edge/np.sqrt(mass[:-1]*mass[1:])
    residual[:-1] += off[:,None]*vectors[1:]
    residual[1:] += off[:,None]*vectors[:-1]
    return vals, float(np.max(np.linalg.norm(residual,axis=0)))

def run():
    rows=[]
    for n in [201,401,801,1601]:
        vals,res = solve(n)
        rows.append({"nodes":n,"eigenvalues":vals.tolist(),"max_discrete_residual":res})
    # Second order estimate is a numerical diagnostic, not an enclosure.
    fine=rows[-1]["eigenvalues"][1]; coarse=rows[-2]["eigenvalues"][1]
    write_result("scalar_spectrum.json", {
        "status":"NUMERICAL", "scope":"reduced scalar operator on frozen optimized coordinate metric",
        "operator":"-w^-1 (p u')', p=sqrt(det(g))*g^{ss}, w=sqrt(det(g)) constant",
        "boundary":"Neumann p u'=0 at s=-2,3; first positive eigenvalue",
        "method":"conservative P1 FEM with midpoint stiffness and trapezoidal lumped mass",
        "sweep":rows,"values":{"scalar_gap":fine},
        "richardson_estimate":fine+(fine-coarse)/3,
        "numerical_refinement_error_estimate":abs(fine-coarse)/3,
        "full_seven_dimensional_gap":None
    })

if __name__ == "__main__": run()
