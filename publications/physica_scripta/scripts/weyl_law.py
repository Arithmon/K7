"""alpha ALWAYS denotes log N(lambda) / log lambda slope in this projection."""
import numpy as np
from common import read, write_result

def fit(lam, first, last):
    n = np.arange(first,last+1)
    x=np.log(lam[n]); y=np.log(n)
    A=np.column_stack([x,np.ones(len(x))])
    slope,intercept=np.linalg.lstsq(A,y,rcond=None)[0]
    r=y-A@np.array([slope,intercept])
    se=np.sqrt(float(r@r)/(len(x)-2)/float(np.sum((x-x.mean())**2)))
    return {"first_positive_index":first,"last_positive_index":last,
            "lambda":lam[n].tolist(),"counting_function":n.tolist(),
            "alpha":float(slope),"intercept":float(intercept),"OLS_standard_error":float(se)}

def run():
    spectrum=read("results/scalar_spectrum.json")
    lam=np.array(spectrum["sweep"][-1]["eigenvalues"])
    fits=[fit(lam,4,19),fit(lam,8,30),fit(lam,12,38)]
    write_result("weyl_law.json",{
        "status":"NUMERICAL", "scope":"finite-window diagnostic for reduced one-dimensional operator",
        "definition":"N(lambda) ~ C lambda^alpha; alpha=d/2",
        "inverse_index_growth_symbol":"nu, lambda_n ~ C n^nu, nu=1/alpha only asymptotically",
        "fits":fits,"values":{"weyl_alpha":fits[0]["alpha"],"weyl_one_dimensional":"1/2","weyl_seven_dimensional":"7/2"},
        "window_sensitivity":max(f["alpha"] for f in fits)-min(f["alpha"] for f in fits),
        "uncertainty_scope":"OLS standard error measures fit residuals only; window spread is separate; neither proves an asymptotic law.",
        "full_tower_fit":None},["results/scalar_spectrum.json"])

if __name__ == "__main__": run()
