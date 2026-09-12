#!/usr/bin/env python3
"""Finite block-monomial centralizer screen for the rho=17 JK tau.

Scope: exhaustive only inside the natural automorphisms that preserve Piroddi's
finite-index block decomposition
    W=A2^8+A2(2)+U(3)+[[4,2],[2,4]]
and commute with the standard symplectic V4.  This is deliberately a finite
negative control, not a no-go theorem for the full integral centralizer.

Among candidates with tau^2=1 and the required four anti-coset traces zero,
the script keeps only those extending integrally to Piroddi's Lambda_K3
overlattice.  It then computes rank_F2(g-I).  For involutions of a unimodular
lattice this equals the 2-elementary discriminant length a of the primitive
fixed lattice.  The JK target is (a_tau,a_tau*sigma*)=(7,9,9,9).
"""

from __future__ import annotations

import itertools
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


NAMES = (
    "a1","a2","b1","b2","c1","c2","d1","d2",
    "e1","e2","f1","f2","g1","g2","h1","h2",
    "w","z","x","y","v1","v2",
)
IDX = {n:i for i,n in enumerate(NAMES)}


def e(name: str) -> sp.Matrix:
    out=sp.zeros(22,1)
    out[IDX[name],0]=1
    return out


def lin(terms: dict[str,int], denominator: int=1) -> sp.Matrix:
    out=sp.zeros(22,1)
    for name,c in terms.items():
        out[IDX[name],0]=sp.Rational(c,denominator)
    return out


def integral_matrix(M: sp.Matrix) -> sp.Matrix:
    assert all(x.q==1 for x in M)
    return sp.Matrix([[int(x) for x in row] for row in M.tolist()])


def build_hnf_basis() -> sp.Matrix:
    alpha=lin({"a1":-1,"a2":1,"d1":1,"d2":-1,"e1":-1,"e2":1,"f1":1,"f2":-1,"g1":-1,"g2":1,"h1":1,"h2":-1},3)
    beta=lin({"b1":-1,"b2":1,"c1":1,"c2":-1,"e1":-1,"e2":1,"f1":1,"f2":-1,"g1":1,"g2":-1,"h1":-1,"h2":1},3)
    gamma=lin({"x":1,"y":-1,"e1":-1,"e2":1,"f1":-1,"f2":1},3)
    delta=lin({"x":1,"c1":-1,"c2":1,"d1":-1,"d2":1,"e1":-1,"e2":1},3)
    epsilon=lin({"x":1,"z":-1,"w":1,"c1":1,"c2":-1,"e1":-1,"e2":1,"g1":-1,"g2":1,"h1":1,"h2":-1},3)
    zeta=(lin({"x":1,"z":1,"c1":1,"c2":1,"e1":1,"e2":1,"g1":1,"g2":1,"h1":1,"h2":1})+epsilon)/2+e("v2")/2
    eta=(lin({"x":1,"c1":1,"c2":1,"e1":1,"e2":1})+epsilon)/2+lin({"g1":1,"g2":-1,"h1":1,"h2":-1},6)+e("v1")/6-e("v2")/3
    scale=6
    gens=[sp.eye(22)[:,i]*scale for i in range(22)] + [v*scale for v in (alpha,beta,gamma,delta,epsilon,zeta,eta)]
    A=integral_matrix(sp.Matrix.hstack(*gens))
    return hermite_normal_form(A)


def involutive_auts_2x2(G: np.ndarray) -> list[np.ndarray]:
    out=[]
    I=np.eye(2,dtype=np.int64)
    for vals in itertools.product(range(-2,3),repeat=4):
        M=np.array(vals,dtype=np.int64).reshape(2,2)
        det=round(np.linalg.det(M))
        if abs(det)!=1:
            continue
        if np.array_equal(M.T@G@M,G) and np.array_equal(M@M,I):
            if not any(np.array_equal(M,N) for N in out):
                out.append(M)
    return out


def compose(p: np.ndarray,q: np.ndarray) -> np.ndarray:
    return p[q]


def block_action(p: np.ndarray, Ms: tuple[np.ndarray,np.ndarray,np.ndarray]) -> np.ndarray:
    C=np.zeros((22,22),dtype=np.int64)
    for src in range(8):
        oi=0 if src<4 else (1 if src<6 else 2)
        dest=int(p[src])
        C[2*dest:2*dest+2,2*src:2*src+2]=Ms[oi]
    return C


def rank_mod2(matrix: np.ndarray) -> int:
    A=np.array(matrix,dtype=np.int64)%2
    m,n=A.shape
    rank=0
    for col in range(n):
        pivot=next((r for r in range(rank,m) if A[r,col]),None)
        if pivot is None:
            continue
        A[[rank,pivot]]=A[[pivot,rank]]
        for r in range(m):
            if r!=rank and A[r,col]:
                A[r]^=A[rank]
        rank+=1
    return rank


def main() -> None:
    # Standard V4 on the eight A2 blocks.
    pA=np.array([1,0,3,2,4,5,7,6],dtype=np.int64)
    pB=np.array([3,2,1,0,5,4,7,6],dtype=np.int64)
    identity8=np.arange(8,dtype=np.int64)

    centralizer_perms=[]
    for perm in itertools.permutations(range(8)):
        p=np.array(perm,dtype=np.int64)
        if (np.array_equal(compose(p,pA),compose(pA,p))
                and np.array_equal(compose(p,pB),compose(pB,p))
                and np.array_equal(compose(p,p),identity8)):
            centralizer_perms.append(p)
    assert len(centralizer_perms)==16

    A2=np.array([[-2,1],[1,-2]],dtype=np.int64)
    A22=2*A2
    U3=np.array([[0,3],[3,0]],dtype=np.int64)
    T2=np.array([[4,2],[2,4]],dtype=np.int64)
    autA=involutive_auts_2x2(A2)
    autZ=involutive_auts_2x2(A22)
    autU=involutive_auts_2x2(U3)
    autT=involutive_auts_2x2(T2)
    assert (len(autA),len(autZ),len(autU),len(autT))==(8,8,4,8)

    IA=block_action(pA,(np.eye(2,dtype=np.int64),)*3)
    IB=block_action(pB,(np.eye(2,dtype=np.int64),)*3)
    IA[16:18,16:18]=-np.eye(2,dtype=np.int64)
    IB[16:18,16:18]= np.eye(2,dtype=np.int64)
    IA[18:22,18:22]=np.eye(4,dtype=np.int64)
    IB[18:22,18:22]=np.eye(4,dtype=np.int64)

    # Exact integrality test for the Piroddi overlattice.
    H=build_hnf_basis()
    Hinv=H.inv()
    denominator=sp.ilcm(*[sp.Rational(x).q for x in Hinv])
    assert denominator==6
    J=np.array([[int(sp.Rational(x)*denominator) for x in row] for row in Hinv.tolist()],dtype=np.int64)
    Hn=np.array(H.tolist(),dtype=np.int64)

    # Standard V4 matrices in the integral Lambda_K3 basis.
    sigmaA_q=Hinv*sp.Matrix(IA.tolist())*H
    sigmaB_q=Hinv*sp.Matrix(IB.tolist())*H
    sigmaA=np.array(integral_matrix(sigmaA_q).tolist(),dtype=np.int64)
    sigmaB=np.array(integral_matrix(sigmaB_q).tolist(),dtype=np.int64)
    identity22=np.eye(22,dtype=np.int64)

    # Precompute the A2^8 block centralizer and its four traces.
    block_records=[]
    IA16=IA[:16,:16]
    IB16=IB[:16,:16]
    for p in centralizer_perms:
        for M0 in autA:
            for M1 in autA:
                for M2 in autA:
                    base=block_action(p,(M0,M1,M2))[:16,:16]
                    traces=(
                        int(np.trace(base)),
                        int(np.trace(base@IA16)),
                        int(np.trace(base@IB16)),
                        int(np.trace(base@IA16@IB16)),
                    )
                    block_records.append((base,traces))
    assert len(block_records)==8192

    trace_admissible=0
    integral_count=0
    profiles={}

    for base,traces in block_records:
        for Mz in autZ:
            tz=int(np.trace(Mz))
            zcon=(tz,-tz,tz,-tz)
            for Mu in autU:
                tu=int(np.trace(Mu))
                for Mt in autT:
                    common=tu+int(np.trace(Mt))
                    if (traces[0]+zcon[0]+common != 0
                            or traces[1]+zcon[1]+common != 0
                            or traces[2]+zcon[2]+common != 0
                            or traces[3]+zcon[3]+common != 0):
                        continue
                    trace_admissible+=1

                    C=np.zeros((22,22),dtype=np.int64)
                    C[:16,:16]=base
                    C[16:18,16:18]=Mz
                    C[18:20,18:20]=Mu
                    C[20:22,20:22]=Mt

                    N=J@C@Hn
                    if not np.all(N % int(denominator)==0):
                        continue
                    integral_count+=1
                    tau=N//int(denominator)
                    profile=(
                        rank_mod2(tau-identity22),
                        rank_mod2(tau@sigmaA-identity22),
                        rank_mod2(tau@sigmaB-identity22),
                        rank_mod2(tau@sigmaA@sigmaB-identity22),
                    )
                    profiles[profile]=profiles.get(profile,0)+1

    assert trace_admissible==290496
    assert integral_count==1296
    assert profiles=={(11,11,11,11):1296}
    assert (7,9,9,9) not in profiles

    print("rho=17 JK tau finite centralizer screen")
    print("========================================")
    print("scope                    : Piroddi-W block-monomial centralizer only")
    print("centralizer permutations :",len(centralizer_perms))
    print("trace-admissible          :",trace_admissible)
    print("integral on Lambda_K3     :",integral_count)
    print("fixed-lattice a profiles :",profiles)
    print("JK target a profile       : (7, 9, 9, 9)")
    print("verdict                   : NO HIT IN THIS FINITE FAMILY")
    print()
    print("SCOPE WARNING")
    print("  This is not a no-go theorem for the full centralizer O(Lambda_K3)^V4.")
    print("  It rules out the obvious block-monomial lifts and forces the next search")
    print("  to use genuine overlattice/discriminant mixing outside that family.")


if __name__=="__main__":
    main()
