"""Re-evaluate every covering interval and check the rational min-max inequalities."""
from fractions import Fraction as Q
from mpmath import iv
from common import validate_result, write_result
from lambda1_enclosure import interval_gss, endpoint

def check(data):
    iv.dps=50
    cells=data["cells"]
    if Q(cells[0]["domain"][0]) != -2 or Q(cells[-1]["domain"][1]) != 3:
        raise ValueError("Incomplete domain coverage")
    previous=Q(-2); low=[];high=[]
    for cell in cells:
        l,r=map(Q,cell["domain"])
        if l!=previous or l>=r:raise ValueError("Gap or invalid interval")
        previous=r
        computed=interval_gss(l,r)
        a,b=map(Q,cell["g_inverse_ss"])
        if not (0<a<=endpoint(computed,0)<=endpoint(computed,1)<=b):
            raise ValueError("Coefficient bound does not contain fresh interval evaluation")
        low.append(a);high.append(b)
    if list(map(Q,data["a_bounds"])) != [min(low),max(high)]:
        raise ValueError("Incorrect aggregate coefficient bounds")
    p,q=map(Q,data["pi_squared"])
    if not(p<=endpoint(iv.pi**2,0)<=endpoint(iv.pi**2,1)<=q):
        raise ValueError("Incorrect pi enclosure")
    l,u=map(Q,data["eigenvalue_interval_rational"])
    if not (0<l<=min(low)*p/25 and u>=max(high)*q/25 and l<u):
        raise ValueError("Incorrect eigenvalue endpoints")
    if u-l != Q(data["width_rational"]):raise ValueError("Incorrect width")
    if data["values"]!={"lambda_lower":str(l),"lambda_upper":str(u)}:
        raise ValueError("Published endpoints mismatch certificate")
    return True

if __name__=="__main__":
    data=validate_result("results/lambda1_enclosure.json")
    check(data)
    write_result("lambda1_check.json",{"status":"CERTIFIED","passed":True,
        "scope":data["scope"],"check_precision_decimal_digits":50},
        ["results/lambda1_enclosure.json","scripts/lambda1_enclosure.py"])
