#!/usr/bin/env python3
"""Check every first-step mod-8 class for distinct exact involutions."""
from collections import Counter
import argparse, numpy as np, sympy as sp
import check_k3_rho17_tauM_matching as matching
import check_k3_rho17_jk_eichler_compositions as comp

def rkey(t,m): return bytes((t%m).astype(np.uint8).flat)

def record(groups, counts, genuine, t):
    """Stream a state; distinct involutions have distinct embedded eigenspaces."""
    mod8 = rkey(t,8)
    exact = t.tobytes()
    previous = groups.setdefault(mod8, exact)
    counts[mod8] += 1
    if exact != previous:
        genuine.add(mod8)

def self_test():
    """A duplicate is harmless; a distinct exact involution mod 8 must fail."""
    a=np.array([[1,0],[0,-1]],dtype=np.int64)
    b=np.array([[1,8],[0,-1]],dtype=np.int64)
    assert np.array_equal(a@a,np.eye(2,dtype=np.int64))
    assert np.array_equal(b@b,np.eye(2,dtype=np.int64))
    groups={}; counts=Counter(); genuine=set()
    record(groups,counts,genuine,a)
    record(groups,counts,genuine,a)
    assert not genuine and list(counts.values())==[2]
    record(groups,counts,genuine,b)
    assert len(genuine)==1 and list(counts.values())==[3]
    print('positive/negative mod8 collision gate: PASS')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--matches',type=int,default=4); ap.add_argument('--bound',type=int,default=1); ap.add_argument('--collision-limit',type=int,default=20,help='maximum diagnostic fingerprints printed; all classes are checked'); ap.add_argument('--self-test',action='store_true',help='run a tiny positive/negative collision control'); args=ap.parse_args()
    if args.self_test:
        self_test(); return
    assert args.matches > 0 and args.bound > 0 and args.collision_limit >= 0
    data,gm,p,pinv,matches=matching.matched_actions(verbose=False); PM=sp.Matrix(p[:,:10])
    gm_np=np.array(gm.tolist(),dtype=np.int64)
    groups={}; counts=Counter(); genuine=set(); total=0
    # one representative per structured M candidate; this avoids counting the
    # four Omega lifts as distinct first-step geometry states.
    seen_candidates=set()
    for match in matches:
        if match['candidate'] in seen_candidates: continue
        if len(seen_candidates)==args.matches: break
        seen_candidates.add(match['candidate'])
        tau=sp.Matrix(match['tau']); tauM=PM.gauss_jordan_solve(tau*PM)[0]
        raw=comp.eichlers(tauM,gm,PM,args.bound,data['gram'])
        print('candidate',match['candidate'],'raw first twists',len(raw),flush=True)
        for E,e,a,_ in raw:
            an=int((a.T*gm*a)[0])
            EM=sp.eye(10)+a*(e.T*gm)-e*(a.T*gm)-(an//2)*e*(e.T*gm)
            t1M=EM*tauM
            assert all(x.q==1 for x in t1M), 'nonintegral first-step action'
            t=np.array(t1M.tolist(),dtype=np.int64)
            max_t=int(np.max(np.abs(t))); max_g=int(np.max(np.abs(gm_np)))
            assert 100*max_t*max_t*max_g < 2**63, 'int64 matrix products could overflow'
            assert np.trace(t)==0 and np.array_equal(t@t,np.eye(10,dtype=np.int64)), 'not a trace-zero involution'
            assert np.array_equal(t.T@gm_np@t,gm_np), 'not an M isometry'
            record(groups,counts,genuine,t); total+=1
    assert len(seen_candidates)==args.matches, 'fewer matched bases than requested'
    repeated=sum(n>1 for n in counts.values())
    print('First states total:',total,'distinct mod8:',len(groups),'repeated mod8 classes checked:',repeated,flush=True)
    for k in sorted(genuine)[:args.collision_limit]:
        print('genuine collision fingerprint',k.hex(),'multiplicity',counts[k],flush=True)
    print('mod8 collision classes with >1 exact embedded state:',len(genuine))
    assert not genuine, 'mod8 fingerprint is not injective on this bounded sample'
    print('No continuation sets computed: this is the first-step collision hunt only.')

if __name__=='__main__': main()
