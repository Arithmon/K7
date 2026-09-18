"""Chebyshev Dirichlet profiles; no identification with global harmonic forms."""
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve
from common import chebyshev, coefficients, write_result

def run():
    rows=[]; profiles=[]
    invp=lambda x: 1/coefficients([x])[0][0]
    def integral(x):
        edges=sorted(set([-2., *[e for e in [0.,1.] if e<x], float(x)]))
        return sum(quad(invp,a,b,epsabs=1e-12,epsrel=1e-12)[0] for a,b in zip(edges,edges[1:]))
    total=integral(3.)
    for n in [24,48,96,192]:
        s,D=chebyshev(n)
        p,w=coefficients(s)
        A=-(D*p[None,:])@D
        b=np.zeros(n+1);b[-1]=1
        A[0]=0;A[0,0]=1;A[-1]=0;A[-1,-1]=1
        f=np.zeros(n+1);f[-1]=1
        f[1:-1]=solve(A[1:-1,1:-1],-A[1:-1,-1])
        exact=np.array([integral(x)/total if x>-2 else 0. for x in s])
        flux=p*(D@f)
        rows.append({"degree":n,"max_collocation_residual":float(abs(A@f-b).max()),
                     "max_error_vs_quadrature":float(abs(f-exact).max()),
                     "relative_flux_variation":float(np.ptp(flux)/abs(flux.mean())),
                     "boundary_error":float(max(abs(f[0]),abs(f[-1]-1)))})
        profiles.append({"degree":n,"s":s.tolist(),"left":(1-f).tolist(),"right":f.tolist()})
    write_result("hodge_profiles.json", {
        "status":"NUMERICAL","operator":"-(p f')'=0, p=sqrt(det(g))*g^{ss}",
        "boundary":"right profile f(-2)=0, f(3)=1; left=1-right",
        "scope":"scalar Dirichlet interpolation profiles only; no global Hodge multiplicity",
        "method":"Chebyshev-Lobatto collocation, independent piecewise adaptive quadrature comparison",
        "exact_identity":"f_right(s)=integral[-2,s](1/p)/integral[-2,3](1/p)",
        "sweep":rows,"profiles":profiles,
        "values":{"profile_error":rows[-1]["max_error_vs_quadrature"]}
    })

if __name__ == "__main__": run()
