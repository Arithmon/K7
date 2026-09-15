#!/usr/bin/env python3
"""Bounded paired-root twists of the exactly glued structured M family.

Roots have coefficients in [-bound,bound] in primitive, Euclidean-LLL-reduced
eigenlattice bases. Equal-norm pairs preserve both signatures and trace.
One root representative per ambient mod-2 class suffices for the mod-2
profile filter; exact SNF/parity verification is mandatory for every hit.
This is a bounded experiment, not a no-go theorem for the whole centralizer.
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


def rank2(matrix):
    rows = [sum((int(v)&1)<<i for i,v in enumerate(row)) for row in matrix]
    pivots = {}
    for row in rows:
        while row:
            bit = row.bit_length()-1
            if bit in pivots:
                row ^= pivots[bit]
            else:
                pivots[bit] = row
                break
    return len(pivots)


def root_classes(gm,tm,sign,bound):
    basis = discr.integer_kernel(tm-sign*sp.eye(10)).T.lll().T
    assert basis.cols == 5
    gf = omega.ints(basis.T*gm*basis)
    coefficients = np.array(list(itertools.product(range(-bound,bound+1),repeat=5)),dtype=np.int64)
    norms = np.sum((coefficients@gf)*coefficients,axis=1)
    classes = {2:{},-2:{}}
    counts = Counter()
    bn = omega.ints(basis)
    for i in np.flatnonzero(np.abs(norms)==2):
        v = bn@coefficients[i]
        norm = int(norms[i])
        counts[norm] += 1
        key = tuple(int(x)%2 for x in v)
        candidate = tuple(int(x) for x in v)
        previous = classes[norm].get(key)
        if previous is None or (sum(x*x for x in candidate),candidate)<(sum(x*x for x in previous),previous):
            classes[norm][key] = candidate
    return basis,classes,counts


def root_residue_upper_bound(gm,basis):
    """Necessary mod-8 norm conditions for EVERY integral root, no height bound.

    The eigenlattice is even, so z^T G z mod 8 depends only on z mod 4.
    Return M/2M classes which could contain roots of either norm.
    """
    gf = omega.ints(basis.T*gm*basis)
    coefficients = np.array(list(itertools.product(range(4),repeat=5)),dtype=np.int64)
    norms = np.sum((coefficients@gf)*coefficients,axis=1)%8
    bn = omega.ints(basis)
    return {n:{tuple(int(x)%2 for x in bn@v) for v in coefficients[norms==n%8]}
            for n in (2,-2)}


def orthogonal_residue_products(gm,basis,ambient_m,qn):
    """Over-approximate products of orthogonal roots of arbitrary height.

    Pairings on each eigenlattice are even, so pairings mod 4 depend on
    coefficients mod 2. Exact orthogonality implies this necessary test.
    Up to one positive and three negative lines can be exchanged between
    eigenspaces of signatures (1,4) and (2,3).
    """
    gf = omega.ints(basis.T*gm*basis)
    assert np.all(gf%2 == 0)
    upper = root_residue_upper_bound(gm,basis)
    bn = omega.ints(basis)
    reps = {tuple(int(x)%2 for x in bn@np.array(z)):bn@np.array(z,dtype=np.int64)
            for z in itertools.product(range(2),repeat=5)}
    keys = sorted(upper[2]|upper[-2])
    gn = omega.ints(gm)
    reflections = {}
    am = omega.ints(ambient_m)
    for key in keys:
        v = (am@reps[key])%2
        reflections[key] = np.outer(v,v@qn)%2
    result = {}
    for count in range(5):
        for subset in itertools.combinations(keys,count):
            if any(int(reps[u]@gn@reps[v])%4 for u,v in itertools.combinations(subset,2)):
                continue
            update = sum((reflections[k] for k in subset),np.zeros((22,22),dtype=np.int64))%2
            for signs in itertools.product((2,-2),repeat=count):
                positive = signs.count(2)
                negative = count-positive
                if positive>1 or negative>3 or any(k not in upper[n] for k,n in zip(subset,signs)):
                    continue
                result.setdefault((positive,negative),{})[bytes(np.asarray(update,dtype=np.uint8).flat)] = (subset,signs)
    return result


def residue_screen(data,gm,p,matches):
    qn = omega.ints(data['gram'])%2
    sn = [omega.ints(s)%2 for s in (sp.eye(22),data['a'],data['b'],data['a']*data['b'])]
    cache = {}
    counts = Counter()
    hits = Counter()
    examples = {}
    for match in matches:
        ci,tm = match['candidate'],match['tm']
        if ci not in cache:
            bp = discr.integer_kernel(tm-sp.eye(10)).T.lll().T
            bm = discr.integer_kernel(tm+sp.eye(10)).T.lll().T
            pp = orthogonal_residue_products(gm,bp,p[:,:10],qn)
            pm = orthogonal_residue_products(gm,bm,p[:,:10],qn)
            cache[ci] = pp,pm
            print('All-height orthogonal product classes',ci,
                  {k:(len(pp[k]),len(pm.get(k,{}))) for k in pp},flush=True)
        pp,pm = cache[ci]
        tau = omega.ints(match['tau'])%2
        for signature in sorted(set(pp)&set(pm)):
            k = sum(signature)
            for xp,xm in itertools.product(pp[signature],pm[signature]):
                rp = np.frombuffer(xp,dtype=np.uint8).reshape(22,22).astype(np.int64)
                rm = np.frombuffer(xm,dtype=np.uint8).reshape(22,22).astype(np.int64)
                t = ((np.eye(22,dtype=np.int64)+rp+rm)@tau)%2
                profile = tuple(rank2(t@s-np.eye(22,dtype=np.int64)) for s in sn)
                counts[k] += 1
                if sorted(profile) == [7,9,9,9]:
                    hits[k] += 1
                    examples.setdefault(k,(ci,match['triple'],signature,pp[signature][xp],pm[signature][xm]))
    print('All-height necessary residue candidates by number of pairs:',dict(counts),flush=True)
    print('Target residue hits:',dict(hits),flush=True)
    print('First residue witnesses (not integral roots):',examples,flush=True)
    assert counts == {0:96,1:12288,2:69120,3:61440}
    assert not hits
    return counts,hits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bound',type=int,default=2)
    parser.add_argument('--output',help='Write first exact hit as a new JSON file')
    parser.add_argument('--residue-only',action='store_true',help='All-height orthogonal-product necessary screen')
    args = parser.parse_args()
    assert 1 <= args.bound <= 4
    data,gm,p,pinv,matches = matching.matched_actions()
    if args.residue_only:
        residue_screen(data,gm,p,matches)
        return
    ambient_m = p[:,:10]
    qn = omega.ints(data['gram'])
    sn = [omega.ints(s) for s in (sp.eye(22),data['a'],data['b'],data['a']*data['b'])]
    cache = {}
    profiles = Counter()
    total = 0
    for mi,match in enumerate(matches):
        ci,tm = match['candidate'],match['tm']
        if ci not in cache:
            bp,cp,np_ = root_classes(gm,tm,1,args.bound)
            bm,cm,nm = root_classes(gm,tm,-1,args.bound)
            upperp = root_residue_upper_bound(gm,bp)
            upperm = root_residue_upper_bound(gm,bm)
            print('All-height mod-8 upper bounds:',{k:len(v) for k,v in upperp.items()},
                  {k:len(v) for k,v in upperm.items()},flush=True)
            cache[ci] = (cp,cm)
            print('M candidate',ci,'roots +/- eigenspaces:',dict(np_),dict(nm),
                  'classes:',{k:len(v) for k,v in cp.items()},
                  {k:len(v) for k,v in cm.items()},flush=True)
        cp,cm = cache[ci]
        tn = omega.ints(match['tau'])
        for norm in (2,-2):
            for u,v in itertools.product(cp[norm].values(),cm[norm].values()):
                un = omega.ints(ambient_m*sp.Matrix(u)).reshape(22)
                vn = omega.ints(ambient_m*sp.Matrix(v)).reshape(22)
                size = max(int(np.max(np.abs(un))),int(np.max(np.abs(vn))),1)
                assert 22*int(np.max(np.abs(qn)))*size**2 < 2**63
                ru = np.eye(22,dtype=np.int64)-(2//norm)*np.outer(un,un@qn)
                rv = np.eye(22,dtype=np.int64)-(2//norm)*np.outer(vn,vn@qn)
                twist2 = ((ru%2)@(rv%2)@(tn%2))%2
                profile = tuple(rank2(twist2@(s%2)-np.eye(22,dtype=np.int64)) for s in sn)
                profiles[profile] += 1
                total += 1
                if sorted(profile) != [7,9,9,9]:
                    continue
                # Relabel tau by the coset element with a=7.
                selected = sp.Matrix(ru)*sp.Matrix(rv)*sp.Matrix(tn)*sp.Matrix(sn[profile.index(7)])
                reports = matching.verify_lift(data,selected)
                exact = [(r['rank'],r['a'],r['delta']) for r in reports]
                assert exact == [(11,7,1)]+[(11,9,1)]*3
                assert (sp.Matrix(u).T*gm*sp.Matrix(v))[0] == 0
                print('EXACT TARGET HIT:',ci,match['triple'],'norm',norm,'u',u,'v',v,flush=True)
                print('Fixed types:',exact,flush=True)
                if args.output:
                    def rows(mat):
                        return [[int(x) for x in row] for row in mat.tolist()]
                    certificate = dict(schema=1,gram=rows(data['gram']),
                        sigma_A=rows(data['a']),sigma_B=rows(data['b']),tau=rows(selected),
                        source_candidate=ci,source_triple=match['triple'],root_norm=norm,
                        root_u=list(u),root_v=list(v),M_embedding=rows(ambient_m),
                        coset_relabel=profile.index(7),bound=args.bound,
                        fixed=[dict(gram=rows(r['gram']),snf=r['snf'],rank=r['rank'],
                                    a=r['a'],delta=r['delta']) for r in reports])
                    with open(args.output,'x',encoding='utf-8') as stream:
                        json.dump(certificate,stream,sort_keys=True,indent=2)
                        stream.write('\n')
                return
    print('Paired mod-2 root classes tested:',total)
    print('Profiles:',dict(sorted(profiles.items())))
    if args.bound == 2:
        assert total == 8736
    print('NO HIT in this bounded paired-root experiment; no global no-go claimed.')


if __name__ == '__main__':
    main()
