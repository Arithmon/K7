#!/usr/bin/env python3
"""Bounded two-step Eichler compositions (post-freeze experiment).

This deliberately samples a small number of compatible bases and first twists;
after each step the eigenspaces are recomputed.  It is not an exhaustion.
"""
from __future__ import annotations
import argparse, itertools
from collections import Counter
import numpy as np
import sympy as sp
import check_k3_rho17_tauM_matching as matching
import check_k3_rho17_tauOmega_discriminant_actions as omega
import check_k3_rho17_jk_reflection_twists as reflections
import check_k3_rho17_v4_discriminant_gluing as discr

def eigbasis(t, sign):
    return discr.integer_kernel(t-sign*sp.eye(t.rows)).T.lll().T

def eichlers(t, gram, ambient, bound, ambient_gram, mod2=False):
    t = sp.Matrix(t)
    ambient = sp.Matrix(ambient)
    q = omega.ints(ambient_gram); out=[]
    for sign in (1,-1):
        be, ba = eigbasis(t,sign), eigbasis(t,-sign)
        cs = list(itertools.product(range(-bound,bound+1), repeat=5))
        es = []
        for z in cs:
            e = be*sp.Matrix(z)
            if any(e) and int((e.T*gram*e)[0]) == 0:
                es.append(e)
        # deterministic, nonzero isotropic representatives only
        es = {tuple(int(x) for x in e):e for e in es}
        for key in sorted(es, key=lambda z:(sum(x*x for x in z),z)):
            e = es[key]
            ee = omega.ints(ambient*e).reshape(22)
            for z in cs:
                a = ba*sp.Matrix(z)
                if not any(a): continue
                aa = omega.ints(ambient*a).reshape(22)
                an = int(aa@q@aa)
                if int(ee@q@ee) or int(ee@q@aa): continue
                E = np.eye(22,dtype=np.int64)+np.outer(aa,ee@q)-np.outer(ee,aa@q)-(an//2)*np.outer(ee,ee@q)
                if np.array_equal(E.T@q@E,q) and np.array_equal(E@E,np.eye(22,dtype=np.int64)):
                    # E itself is not expected involutive; this check is only a guard.
                    pass
                out.append(((E%2).astype(np.int64) if mod2 else E,e,a,sign))
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--matches',type=int,default=2); ap.add_argument('--first-limit',type=int,default=32); ap.add_argument('--bound',type=int,default=1); ap.add_argument('--mod2-only',action='store_true',help='skip exact integer gates after the mod-2 profile filter'); args=ap.parse_args()
    data,gm,p,pinv,matches=matching.matched_actions(verbose=False)
    q=omega.ints(data['gram']); sigmas=[omega.ints(s) for s in (sp.eye(22),data['a'],data['b'],data['a']*data['b'])]
    tested=0; profiles=Counter(); transitions=Counter(); first_profiles=Counter()
    for match in matches[:args.matches]:
        PM=sp.Matrix(p[:,:10])
        tau=omega.ints(match['tau'])
        tauM=PM.gauss_jordan_solve(sp.Matrix(tau)*PM)[0]
        first_raw=eichlers(tauM,gm,PM,args.bound,data['gram'])
        first_seen={}
        for item in first_raw:
            first_seen.setdefault(bytes((item[0]%2).astype(np.uint8).flat),item)
        first=list(first_seen.values())[:args.first_limit]
        if len(first_raw)!=len(first_seen):
            print('First twists raw/distinct mod2:',len(first_raw),len(first_seen),flush=True)
        for E1,_,_,_ in first:
            t1=E1@tau
            if not np.array_equal(t1@t1,np.eye(22,dtype=np.int64)): continue
            p1=tuple(reflections.rank2((t1@s)%2-np.eye(22,dtype=np.int64)) for s in sigmas)
            first_profiles[p1]+=1
            # Recompute eigenspaces of the new involution, then generate step two.
            t1M=PM.gauss_jordan_solve(sp.Matrix(t1)*PM)[0]
            second_raw=eichlers(t1M,gm,PM,args.bound,data['gram'],mod2=args.mod2_only)
            second_seen={}
            for item in second_raw:
                second_seen.setdefault(bytes((item[0]%2).astype(np.uint8).flat),item)
            second=list(second_seen.values())
            if len(second_raw)!=len(second_seen):
                print('Second twists raw/distinct mod2:',len(second_raw),len(second_seen),flush=True)
            for E2,_,_,_ in second:
                t2mod=(E2 if args.mod2_only else E2%2)@(t1%2)%2
                prof=tuple(reflections.rank2(t2mod@(s%2)-np.eye(22,dtype=np.int64)) for s in sigmas)
                profiles[prof]+=1; transitions[(p1,prof)]+=1; tested+=1
                if args.mod2_only:
                    continue
                t2=E2@t1
                if not np.array_equal(t2@t2,np.eye(22,dtype=np.int64)): continue
                if not np.array_equal(t2.T@q@t2,q) or np.trace(t2)!=0: continue
                if any(not np.array_equal(t2@s,s@t2) or np.trace(t2@s)!=0 for s in sigmas[1:]): continue
                if sorted(prof)==[7,9,9,9]:
                    selected=sp.Matrix(t2)*sp.Matrix(sigmas[prof.index(7)])
                    exact=[(r['rank'],r['a'],r['delta']) for r in matching.verify_lift(data,selected)]
                    print('EXACT TARGET HIT',match['candidate'],prof,exact); return
    print('Two-step candidates tested:',tested)
    print('First-step profiles:',dict(sorted(first_profiles.items())))
    print('Final profiles:',dict(sorted(profiles.items())))
    print('Distinct profile transitions:',len(transitions))
    for (p1,p2),n in sorted(transitions.items(),key=lambda kv:(-kv[1],kv[0]))[:20]:
        print('  ',p1,'->',p2,':',n)
    print('NO HIT in this bounded recomputed-eigenspace experiment; no global no-go claimed.')

if __name__=='__main__': main()
