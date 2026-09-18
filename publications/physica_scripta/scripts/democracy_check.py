"""Restrict the theorem to parallel fibre one-forms on an exact product."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from common import metric, coefficients, read, write_result

def run():
    n=1601;s=np.linspace(-2,3,n);h=s[1]-s[0]
    mid=(s[1:]+s[:-1])/2
    g,_=metric(s);gm,_=metric(mid)
    p,w=coefficients(s);pm,_=coefficients(mid)
    rows=[]
    ref=read("results/scalar_spectrum.json")["sweep"][-1]["eigenvalues"][1:6]
    for k in [1,6]:
        # Explicit block-diagonal projected model and transverse circle sector.
        mass=w/g[:,k,k]*h;mass[[0,-1]]*=.5
        edge=pm/gm[:,k,k]/h
        diag=np.zeros(n);diag[:-1]+=edge;diag[1:]+=edge
        vals=eigh_tridiagonal(diag/mass,-edge/np.sqrt(mass[:-1]*mass[1:]),
                             select="i",select_range=(0,5),eigvals_only=True)
        rows.append({"coordinate":k,"eigenvalues":vals[1:].tolist(),
                     "relative_gap_difference":float(abs(vals[1]-ref[0])/ref[0])})
    write_result("democracy_check.json",{
        "status":"NUMERICAL",
        "theorem":"For a parallel circle one-form theta on an exact product, Delta_1(f theta)=(Delta_0 f)theta, with corresponding radial boundary conditions.",
        "proof":"Use the tensor-product Laplacian; Delta_circle(theta)=0 and all mixed derivatives vanish. Restrict to f depending on the base only.",
        "scope":"isomorphism of the selected scalar/radial one-form sectors, not equality of entire spectra or multiplicities",
        "numerical_model":"block-diagonal coordinate projection with varying circle radii; not the full Hodge operator",
        "checks":rows,"delta_two_comparison":None,
        "values":{"democracy_deviation":max(r["relative_gap_difference"] for r in rows)},
        "three_sector_theorem":False
    },["results/scalar_spectrum.json"])

if __name__ == "__main__": run()
