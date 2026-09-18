"""Directed interval coefficient bounds + scalar min-max, no NK dependency.

For A=-d/ds(a(s)d/ds), Neumann endpoints, the quadratic-form domain is H^1.
The constant zero mode is exact. On its L2 orthogonal complement, Poincare and
the cosine test function give a_min*pi^2/L^2 <= lambda_1 <= a_max*pi^2/L^2.
The frozen determinant is constant, so w cancels from the Rayleigh quotient.
"""
from fractions import Fraction
from mpmath import iv
from common import read, write_result

def exact(x):
    f=Fraction.from_float(x) if isinstance(x,float) else Fraction(x)
    return iv.mpf(f.numerator)/f.denominator

def endpoint(x, side):
    sign, mantissa, exponent, _=x._mpi_[side]
    f=Fraction((-1 if sign else 1)*int(mantissa))
    return f*2**exponent if exponent>=0 else f/Fraction(2**(-exponent))

def bounds(x):
    return [str(endpoint(x,0)), str(endpoint(x,1))]

def interval_gss(left,right):
    data=read("inputs/metric.json")
    c=[[exact(v) for v in row] for row in data["coefficients"]]
    s=iv.mpf([exact(left).a,exact(right).b])
    def poly(x):
        t=[iv.mpf(1),x]
        for k in range(2,len(c)):t.append(2*x*t[-1]-t[-2])
        return [sum(c[k][j]*t[k] for k in range(len(c))) for j in range(28)]
    gamma=exact(data["gamma"])
    if Fraction(right)<=0:
        edge=poly(iv.mpf(-1))
        derivative=[sum(2*((-1)**(k+1))*k*k*c[k][j] for k in range(1,len(c))) for j in range(28)]
        flat=[v+d/gamma*(iv.exp(gamma*s)-1) for v,d in zip(edge,derivative)]
    elif Fraction(left)>=1:
        edge=poly(iv.mpf(1))
        derivative=[sum(2*k*k*c[k][j] for k in range(1,len(c))) for j in range(28)]
        flat=[v-d/gamma*(iv.exp(-gamma*(s-1))-1) for v,d in zip(edge,derivative)]
    else:
        assert Fraction(left)>=0 and Fraction(right)<=1
        flat=poly(2*s-1)
    L=[[iv.mpf(0) for _ in range(7)] for _ in range(7)]
    k=0
    for i in range(7):
        for j in range(i+1):
            L[i][j]=iv.ln(1+iv.exp(flat[k])) if i==j else flat[k]
            k+=1
    # g = scale^2 LL^T; g^{ss}=||L^-1 e_s||^2 / scale^2.
    logdet=sum(iv.ln(L[i][i]) for i in range(7))
    target=exact(Fraction(*data["determinant"]))
    scale2=iv.exp((iv.ln(target)-2*logdet)/7)
    z=[]
    for i in range(7):
        z.append(((1 if i==0 else 0)-sum(L[i][j]*z[j] for j in range(i)))/L[i][i])
    return sum(v**2 for v in z)/scale2

def compute(subdivisions=32):
    iv.dps=40
    cells=[]
    for start,end in [(-2,0),(0,1),(1,3)]:
        for k in range(subdivisions):
            l=Fraction(start)+Fraction((end-start)*k,subdivisions)
            r=Fraction(start)+Fraction((end-start)*(k+1),subdivisions)
            a=interval_gss(l,r)
            cells.append({"domain":[str(l),str(r)],"g_inverse_ss":bounds(a)})
    lo=min(Fraction(c["g_inverse_ss"][0]) for c in cells)
    hi=max(Fraction(c["g_inverse_ss"][1]) for c in cells)
    if lo<=0:raise ValueError("Nonpositive interval coefficient bound")
    pi2=iv.pi**2
    eig_lo=endpoint(exact(lo)*pi2/25,0)
    eig_hi=endpoint(exact(hi)*pi2/25,1)
    unit=10**12
    rounded_lo=Fraction((eig_lo*unit).__floor__(),unit)
    rounded_hi=Fraction((eig_hi*unit).__ceil__(),unit)
    return {"cells":cells,"a_bounds":[str(lo),str(hi)],"pi_squared":bounds(pi2),
            "eigenvalue_interval_rational":[str(rounded_lo),str(rounded_hi)],
            "eigenvalue_interval_decimal":[format(float(rounded_lo),".12f"),format(float(rounded_hi),".12f")],
            "width_rational":str(rounded_hi-rounded_lo),
            "values":{"lambda_lower":str(rounded_lo),"lambda_upper":str(rounded_hi)}}

def run():
    data=compute()
    write_result("lambda1_enclosure.json", dict(data,status="CERTIFIED",
        scope="first positive eigenvalue of the frozen reduced scalar Neumann operator only",
        method="outward interval coefficient evaluation; min-max/Poincare comparison",
        arithmetic="mpmath.iv at 40 decimal digits; exact dyadic coefficient inputs; exact rational endpoints",
        theorem="a_min*pi^2/25 <= lambda_1 <= a_max*pi^2/25",
        full_7D_interval=None,
        trusted_base=["Python integer/Fraction arithmetic","mpmath interval elementary functions","stated scalar variational proof"]))

if __name__ == "__main__": run()
