#!/usr/bin/env python3
"""Collect first-step states and locate genuine mod-8 collisions."""
from collections import defaultdict
import argparse, hashlib, numpy as np, sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
import check_k3_rho17_tauM_matching as matching
import check_k3_rho17_jk_eichler_compositions as comp

def exact_state(t):
    bs=[hermite_normal_form(comp.eigbasis(t,s)) for s in (1,-1)]
    C=sp.Matrix.hstack(*bs)
    payload=tuple(int(x) for B in bs for row in B.tolist() for x in row)
    return payload,abs(int(C.det()))

def rkey(t,m): return bytes((np.array(t.tolist(),dtype=np.int64)%m).astype(np.uint8).flat)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--matches',type=int,default=4); ap.add_argument('--bound',type=int,default=1); ap.add_argument('--collision-limit',type=int,default=20); args=ap.parse_args()
    data,gm,p,pinv,matches=matching.matched_actions(verbose=False); PM=sp.Matrix(p[:,:10])
    groups=defaultdict(list)
    # one representative per structured M candidate; this avoids counting the
    # four Omega lifts as distinct first-step geometry states.
    seen_candidates=set()
    for match in matches:
        if match['candidate'] in seen_candidates: continue
        seen_candidates.add(match['candidate'])
        if len(seen_candidates)>args.matches: break
        tau=sp.Matrix(match['tau']); tauM=PM.gauss_jordan_solve(tau*PM)[0]
        raw=comp.eichlers(tauM,gm,PM,args.bound,data['gram'])
        print('candidate',match['candidate'],'raw first twists',len(raw),flush=True)
        for E,_,_,_ in raw:
            t1=sp.Matrix(E)*tau
            t1M=PM.gauss_jordan_solve(t1*PM)[0]
            groups[rkey(t1M,8)].append((t1M,match['candidate']))
    collisions={k:v for k,v in groups.items() if len(v)>1}
    print('First states total:',sum(map(len,groups.values())),'distinct mod8:',len(groups),'collision classes:',len(collisions),flush=True)
    genuine=0
    for i,(k,items) in enumerate(list(collisions.items())[:args.collision_limit]):
        states={exact_state(t)[0] for t,_ in items}
        if len(states)>1:
            genuine+=1
            print('genuine collision',i,'multiplicity',len(items),'exact states',len(states),flush=True)
    print('mod8 collision classes with >1 exact embedded state:',genuine)
    print('No continuation sets computed: this is the first-step collision hunt only.')

if __name__=='__main__': main()
