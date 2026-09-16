#!/usr/bin/env python3
"""Non-conjugate integral Eichler twists with transparent involutivity.

Choose an isotropic e in one tau_M eigenspace and a in the opposite one.
Then E(e,a) tau is an involution, since tau E(e,a) tau = E(e,-a).
It is rationally conjugate via E(e,a/2), preserving rational character and
signatures, but that half-transvection need not be integral. E(e,a) acts
trivially on the discriminant group. This is multiplication, not an integral
conjugacy-orbit search.
"""
from __future__ import annotations

import argparse
from collections import Counter
import itertools
import json
import numpy as np
import sympy as sp

import check_k3_rho17_tauM_matching as matching
import check_k3_rho17_tauOmega_discriminant_actions as omega
import check_k3_rho17_v4_discriminant_gluing as discr
from check_k3_rho17_jk_reflection_twists import rank2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bound',type=int,default=2)
    parser.add_argument('--output',help='New JSON certificate destination for first exact hit')
    args = parser.parse_args()
    assert 1<=args.bound<=4
    data,gm,p,pinv,matches = matching.matched_actions()
    qn = omega.ints(data['gram'])
    sn = [omega.ints(s) for s in (sp.eye(22),data['a'],data['b'],data['a']*data['b'])]
    cache = {}
    profiles = Counter()
    for match in matches:
        ci,tm = match['candidate'],match['tm']
        if ci not in cache:
            cache[ci] = []
            for sign in (1,-1):
                be = discr.integer_kernel(tm-sign*sp.eye(10)).T.lll().T
                ba = discr.integer_kernel(tm+sign*sp.eye(10)).T.lll().T
                coeff = np.array(list(itertools.product(range(-args.bound,args.bound+1),repeat=5)),dtype=np.int64)
                norms = np.sum((coeff@omega.ints(be.T*gm*be))*coeff,axis=1)
                en = omega.ints(be)
                ereps = {}
                for v in coeff[norms==0]:
                    e = en@v
                    key = tuple(int(x)%2 for x in e)
                    if not any(key):
                        continue
                    candidate = tuple(int(x) for x in e)
                    old = ereps.get(key)
                    if old is None or (sum(x*x for x in candidate),candidate)<(sum(x*x for x in old),old):
                        ereps[key] = candidate
                residues = np.array(list(itertools.product(range(4),repeat=5)),dtype=np.int64)
                residue_norms = np.sum((residues@omega.ints(be.T*gm*be))*residues,axis=1)%8
                upper = {tuple(int(x)%2 for x in en@v) for v in residues[residue_norms==0]}
                upper.discard((0,)*10)
                assert set(ereps) == upper
                print('Eichler M candidate',ci,'eigenvalue',sign,'isotropic classes',len(ereps),flush=True)
                for ev,av in itertools.product(sorted(ereps.values()),itertools.product(range(2),repeat=5)):
                    e = sp.Matrix(ev)
                    a = ba*sp.Matrix(av)
                    ea = omega.ints(p[:,:10]*e).reshape(22)
                    aa = omega.ints(p[:,:10]*a).reshape(22)
                    assert int(ea@qn@ea)==0 and int(ea@qn@aa)==0
                    anorm = int(aa@qn@aa)
                    assert anorm%2==0
                    # Bound every subsequent int64 product before performing it.
                    vector_max = max(int(np.max(np.abs(ea))),int(np.max(np.abs(aa))),1)
                    qmax = int(np.max(np.abs(qn)))
                    emax = 1+(2+abs(anorm)//2)*22*qmax*vector_max**2
                    assert 22*emax*max(abs(int(x)) for x in match['tau']) < 2**63
                    E = np.eye(22,dtype=np.int64)+np.outer(aa,ea@qn)-np.outer(ea,aa@qn)-(anorm//2)*np.outer(ea,ea@qn)
                    actual_emax = max(1,int(np.max(np.abs(E))))
                    assert 22**2*qmax*actual_emax**2 < 2**63
                    assert np.array_equal(E.T@qn@E,qn)
                    twisted = E@omega.ints(match['tau'])
                    tmax = max(1,int(np.max(np.abs(twisted))))
                    assert 22**2*qmax*tmax**2 < 2**63
                    assert np.array_equal(twisted@twisted,np.eye(22,dtype=np.int64))
                    assert np.array_equal(twisted.T@qn@twisted,qn)
                    assert np.trace(twisted)==0
                    for sigma in sn[1:]:
                        assert np.array_equal(twisted@sigma,sigma@twisted)
                        assert np.trace(twisted@sigma)==0
                    cache[ci].append((E,e,a,sign))
        tn = omega.ints(match['tau'])
        for E,e,a,sign in cache[ci]:
            t2 = ((E%2)@(tn%2))%2
            profile = tuple(rank2(t2@(s%2)-np.eye(22,dtype=np.int64)) for s in sn)
            profiles[profile] += 1
            if sorted(profile) != [7,9,9,9]:
                continue
            selected = sp.Matrix(E)*sp.Matrix(tn)*sp.Matrix(sn[profile.index(7)])
            reports = matching.verify_lift(data,selected)
            exact = [(r['rank'],r['a'],r['delta']) for r in reports]
            assert exact == [(11,7,1)]+[(11,9,1)]*3
            assert sp.Matrix(E).T*data['gram']*sp.Matrix(E)==data['gram']
            print('EXACT EICHLER TARGET HIT:',ci,match['triple'],'e',list(e),'a',list(a),flush=True)
            print('Exact fixed types:',exact,flush=True)
            if args.output:
                def rows(mat):
                    return [[int(x) for x in row] for row in mat.tolist()]
                certificate = dict(schema=1,gram=rows(data['gram']),sigma_A=rows(data['a']),
                    sigma_B=rows(data['b']),tau=rows(selected),source_candidate=ci,
                    source_triple=match['triple'],isotropic_e=[int(x) for x in e],
                    parameter_a=[int(x) for x in a],isotropic_eigenvalue=sign,
                    M_embedding=rows(p[:,:10]),coset_relabel=profile.index(7),bound=args.bound,
                    fixed=[dict(gram=rows(r['gram']),snf=r['snf'],rank=r['rank'],a=r['a'],delta=r['delta'])
                           for r in reports])
                with open(args.output,'x',encoding='utf-8') as stream:
                    json.dump(certificate,stream,sort_keys=True,indent=2)
                    stream.write('\n')
            return
    print('Eichler profiles:',dict(sorted(profiles.items())),flush=True)
    assert sum(profiles.values()) == 43008
    assert not any(sorted(p)==[7,9,9,9] for p in profiles)
    print('NO HIT for a single opposite-eigenspace Eichler twist of any height on these bases.')
    print('All nonzero isotropic residue classes attained the mod-8 upper bound;')
    print('no no-go for compositions or other discriminant fibres is claimed.')


if __name__ == '__main__':
    main()
