#!/usr/bin/env python3
"""Test whether a first-step mod-2 class determines second-step continuations."""
from collections import defaultdict
import argparse, numpy as np, sympy as sp
import hashlib
from sympy.matrices.normalforms import hermite_normal_form
import check_k3_rho17_tauM_matching as matching
import check_k3_rho17_jk_eichler_compositions as comp
import check_k3_rho17_jk_reflection_twists as refl
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def key(E): return bytes((E%2).astype(np.uint8).flat)

def exact_state(tM):
    """Canonical embedded primitive eigensublattices plus inclusion glue."""
    bs=[]
    for sign in (1,-1):
        B=comp.eigbasis(tM,sign)
        # Column-HNF gives a deterministic encoding of the embedded sublattice.
        bs.append(hermite_normal_form(B))
    C=sp.Matrix.hstack(*bs)
    return (tuple(int(x) for B in bs for row in B.tolist() for x in row),
            abs(int(C.det())))

def reduced_state(tM,modulus):
    A=np.array(tM.tolist(),dtype=np.int64)%modulus
    return bytes(A.astype(np.uint8).flat)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--classes',type=int,default=3); ap.add_argument('--lifts',type=int,default=2); ap.add_argument('--bound',type=int,default=1); args=ap.parse_args()
    data,gm,p,pinv,matches=matching.matched_actions(verbose=False)
    match=matches[0]; PM=sp.Matrix(p[:,:10]); tau=np.array(match['tau'],dtype=np.int64)
    tauM=PM.gauss_jordan_solve(sp.Matrix(tau)*PM)[0]
    raw=comp.eichlers(tauM,gm,PM,args.bound,data['gram'])
    groups=defaultdict(list)
    for item in raw: groups[key(item[0])].append(item)
    repeated=[(k,v) for k,v in groups.items() if len(v)>=args.lifts]
    print('First raw twists:',len(raw),'distinct mod2:',len(groups),'repeated classes:',len(repeated),flush=True)
    sigmas=[np.array(s,dtype=np.int64) for s in (sp.eye(22),data['a'],data['b'],data['a']*data['b'])]
    for ci,(k,lifts) in enumerate(repeated[:args.classes]):
        sets=[]
        states=[]; reductions={j:defaultdict(set) for j in range(1,6)}
        for item in lifts[:args.lifts]:
            E=item[0]; t1=E@tau
            t1M=PM.gauss_jordan_solve(sp.Matrix(t1)*PM)[0]
            eig_inv=[]
            eig_bases=[]
            for sign in (1,-1):
                B=comp.eigbasis(t1M,sign)
                eig_bases.append(B)
                G=B.T*gm*B
                S=smith_normal_form(G,domain=ZZ)
                eig_inv.append((tuple(abs(int(S[i,i])) for i in range(S.rows)),int(abs(G.det()))))
            glue_index=abs(int(sp.Matrix.hstack(*eig_bases).det()))
            eig_inv.append(('plus_minus_index',glue_index))
            lift_mod4=hashlib.sha256(bytes((np.array(t1M.tolist(),dtype=np.int64)%4).astype(np.uint8).flat)).hexdigest()[:16]
            lift_mod8=hashlib.sha256(bytes((np.array(t1M.tolist(),dtype=np.int64)%8).astype(np.uint8).flat)).hexdigest()[:16]
            second=comp.eichlers(t1M,gm,PM,args.bound,data['gram'],mod2=False)
            actions={key(x[0]) for x in second}
            sets.append(actions)
            states.append(exact_state(t1M))
            for j in range(1,6):
                mod=2**j
                cont={bytes(((x[0]%mod)@(t1%mod)%mod).astype(np.uint8).flat) for x in second}
                reductions[j][reduced_state(t1M,mod)].add(hashlib.sha256(b''.join(sorted(cont))).hexdigest())
            print('class',ci,'lift',len(sets),'t1M_mod4',lift_mod4,'t1M_mod8',lift_mod8,'eigensublattice invariant',eig_inv,
                  'second raw',len(second),'distinct actions',len(actions),flush=True)
        equal=all(s==sets[0] for s in sets[1:])
        exact_groups=defaultdict(list)
        for state,s in zip(states,sets): exact_groups[state].append(s)
        exact_equal=all(all(s==v[0] for s in v[1:]) for v in exact_groups.values())
        print('CLASS',ci,'continuation-complete:',equal,'set sizes',[len(s) for s in sets],flush=True)
        print('  exact state classes:',len(exact_groups),'same-state continuation equality:',exact_equal,flush=True)
        print('  reduced-state ambiguities k=1..5:',[sum(len(v)>1 for v in reductions[j].values()) for j in range(1,6)],flush=True)
        if not equal:
            print('symmetric differences',[len(sets[0]^s) for s in sets[1:]],flush=True)
    print('No equivalence inferred; equality must be established for every tested lift/class before exhaustive use.')

if __name__=='__main__': main()
