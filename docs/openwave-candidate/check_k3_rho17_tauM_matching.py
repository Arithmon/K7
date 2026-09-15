#!/usr/bin/env python3
"""Structured M involutions and explicit gluing with the finite Omega search."""
from __future__ import annotations

from collections import Counter
import argparse
import hashlib
import itertools
import json
import numpy as np
import sympy as sp

import check_k3_rho17_tauOmega_discriminant_actions as omega
import check_k3_rho17_v4_discriminant_gluing as discr
from check_k3_rho17_tauM_discriminant_seed import inertia_symmetric
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def small_isotropic(gram):
    n = gram.rows
    candidates = np.array(list(itertools.product((-1,0,1),repeat=n)),dtype=np.int64)
    norms = np.sum((candidates@omega.ints(gram))*candidates,axis=1)
    candidates = [tuple(int(a) for a in v) for v in candidates[norms==0] if any(v)]
    candidates.sort(key=lambda v:(sum(a*a for a in v),v))
    return candidates


def split_plane(gram,scale):
    candidates = small_isotropic(gram)
    vectors = np.array(candidates,dtype=np.int64)
    gn = omega.ints(gram)
    for e in candidates:
        row = np.array(e,dtype=np.int64)@gn
        if np.any(row%scale):
            continue
        for j in np.flatnonzero(vectors@row == scale):
            f = candidates[j]
            if np.any((np.array(f,dtype=np.int64)@gn)%scale):
                continue
            plane = sp.Matrix.hstack(sp.Matrix(e),sp.Matrix(f))
            comp = discr.integer_kernel(plane.T*gram)
            # Euclidean LLL changes only the primitive kernel basis.
            comp = comp.T.lll().T
            change = sp.Matrix.hstack(plane,comp)
            if abs(change.det()) != 1:
                continue
            gc = comp.T*gram*comp
            if scale == 1 and (any(x%2 for x in gc) or any(gc[i,i]%4 for i in range(gc.rows))):
                continue
            return change,gc
    raise AssertionError('No split plane in the stated coefficient box')


def model_M(data,verbose=True):
    gm = data['m'].T*data['gram']*data['m']
    change = sp.eye(10)
    remaining = gm
    for offset,scale in ((0,1),(2,2),(4,2)):
        step,remaining = split_plane(remaining,scale)
        change = change*sp.diag(sp.eye(offset),step)
    # Enumerate all norm-2 roots of the positive rank-four complement.
    gd = -remaining/2
    assert gd.is_positive_definite and gd.det() == 4
    bounds = [int(sp.floor(sp.sqrt(2*gd.inv()[i,i]))) for i in range(4)]
    roots = [sp.Matrix(v) for v in itertools.product(*[range(-b,b+1) for b in bounds])
             if (sp.Matrix(v).T*gd*sp.Matrix(v))[0] == 2]
    assert len(roots) == 24
    for center in roots:
        neighbors = [v for v in roots if (center.T*gd*v)[0] == -1]
        for a,b,c in itertools.permutations(neighbors,3):
            if any((x.T*gd*y)[0] for x,y in ((a,b),(a,c),(b,c))):
                continue
            d = sp.Matrix.hstack(a,center,b,c)
            if abs(d.det()) == 1:
                change = change*sp.diag(sp.eye(6),d)
                target = sp.diag(sp.Matrix([[0,1],[1,0]]),
                                 sp.Matrix([[0,2],[2,0]]),sp.Matrix([[0,2],[2,0]]),-2*omega.D4)
                assert abs(change.det()) == 1 and change.T*gm*change == target
                if verbose:
                    print('M explicit unimodular model change:',change.tolist(),flush=True)
                return change,target
    raise AssertionError('No D4 simple-root basis')


def structured_candidates():
    u = np.array([[0,1],[1,0]],dtype=np.int64)
    guu = np.zeros((4,4),dtype=np.int64)
    guu[:2,:2] = guu[2:,2:] = u
    uauts = [np.eye(2,dtype=np.int64),-np.eye(2,dtype=np.int64),u,-u]
    # All signed coordinate permutations preserving the displayed U(2)^2.
    pairauts = []
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((-1,1),repeat=4):
            t = np.zeros((4,4),dtype=np.int64)
            for j in range(4):
                t[perm[j],j] = signs[j]
            if np.array_equal(t.T@guu@t,guu) and np.array_equal(t@t,np.eye(4,dtype=np.int64)):
                pairauts.append(t)
    dauts = [x for x in omega.d4_automorphisms() if np.array_equal(x@x,np.eye(4,dtype=np.int64))]
    answer = []
    for t1,t2,t3 in itertools.product(uauts,pairauts,dauts):
        if np.trace(t1)+np.trace(t2)+np.trace(t3):
            continue
        t = sp.diag(sp.Matrix(t1),sp.Matrix(t2),sp.Matrix(t3))
        gu = sp.diag(sp.Matrix(u),2*sp.Matrix(guu))
        plus = discr.integer_kernel(t[:6,:6]-sp.eye(6))
        if inertia_symmetric(plus.T*gu*plus)[0] != 1:
            continue
        answer.append(t)
    print('Structured factors / candidates:',len(uauts),len(pairauts),len(dauts),len(answer),flush=True)
    return answer


def glue_matcher(data,change,gm):
    """Extract and check phi from the live ambient lattice in the new M basis."""
    o,gram = data['o'],data['gram']
    go = o.T*gram*o
    p = sp.Matrix.hstack(data['m']*change,o)
    pinv = p.inv()
    dm = discr.discriminant_data(gm)
    do = discr.discriminant_data(go)
    orders = [d for d in dm[0] if d>1]
    assert orders == [d for d in do[0] if d>1] == [2]*6+[4]*2
    snf,left,_ = smith_normal_decomp(DomainMatrix.from_Matrix(p).convert_to(ZZ))
    snf,left = snf.to_Matrix(),left.to_Matrix()
    gens = []
    for i in range(22):
        d = abs(int(snf[i,i]))
        if d == 1:
            continue
        coords = pinv*left.inv()[:,i]
        cm = discr.discr_coords_from_fraction(coords[:10,:],gm,dm[4],dm[0])
        co = discr.discr_coords_from_fraction(coords[10:,:],go,do[4],do[0])
        gens.append((d,cm,co))
    graph = {}
    for coefficients in itertools.product(*[range(d) for d,_,_ in gens]):
        cm = discr.linear_combination_coords(coefficients,[x[1] for x in gens],orders)
        co = discr.linear_combination_coords(coefficients,[x[2] for x in gens],orders)
        graph[cm] = co
    inverse = {v:k for k,v in graph.items()}
    assert len(graph) == len(inverse) == 1024
    for cm,co in graph.items():
        assert discr.mod2(discr.q_value(cm,dm[3])+discr.q_value(co,do[3])) == 0
    # Preimages under phi of the 12 dual-coordinate generators of Omega.
    co_duals = np.array([[int(do[4][i,j])%d for j in range(12)]
                         for i,d in zip(do[1],orders)],dtype=np.int64)
    preimages = np.array([inverse[tuple(col)] for col in co_duals.T],dtype=np.int64).T
    ml = dm[4]*gm
    mleft = np.array([[int(ml[i,j])%(4*d) for j in range(10)]
                      for i,d in zip(dm[1],orders)],dtype=np.int64)
    mdual4 = omega.ints((4*gm.inv()*dm[2]).applyfunc(lambda x:x%4))
    odual4 = omega.ints((4*go.inv()*do[2]).applyfunc(lambda x:x%4))
    def wanted_key(t):
        numerator = mleft@omega.ints(t)@mdual4
        assert np.all(numerator%4 == 0)
        bar = (numerator//4)%np.array(orders)[:,None]
        images_m = (bar@preimages)%np.array(orders)[:,None]
        images_o = np.array([graph[tuple(col)] for col in images_m.T],dtype=np.int64).T
        return bytes(np.asarray((odual4@images_o)%4,dtype=np.uint8).flat)
    return p,pinv,wanted_key


def fixed_invariants(gram,t):
    basis = discr.integer_kernel(t-sp.eye(t.rows))
    gf = basis.T*gram*basis
    sf = smith_normal_form(gf,domain=ZZ)
    divisors = [abs(int(sf[i,i])) for i in range(gf.rows)]
    assert all(d in (1,2) for d in divisors)
    inv = gf.inv()
    delta = 0 if all(inv[i,i].q == 1 for i in range(gf.rows)) else 1
    return dict(rank=gf.rows,a=divisors.count(2),delta=delta,
                signature=inertia_symmetric(gf),basis=basis,gram=gf,snf=divisors)


def primitive_fixed_hnf(t):
    """Independent fixed-lattice construction: saturate (I+t)L at 2.

    Since 2*L^t is contained in (I+t)L, adjoining every integral half-sum
    suffices. No rational nullspace or Smith right transform is used.
    """
    basis = hermite_normal_form(sp.Matrix(omega.ints(sp.eye(t.rows)+t).tolist()))
    a = [[int(x)%2 for x in row] for row in basis.tolist()]
    pivots = []
    row = 0
    for col in range(basis.cols):
        pivot = next((i for i in range(row,basis.rows) if a[i][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot] = a[pivot],a[row]
        for i in range(basis.rows):
            if i!=row and a[i][col]:
                a[i] = [x^y for x,y in zip(a[i],a[row])]
        pivots.append(col)
        row += 1
    extras = []
    for free in sorted(set(range(basis.cols))-set(pivots)):
        v = sp.zeros(basis.cols,1)
        v[free] = 1
        for i,pivot in enumerate(pivots):
            v[pivot] = a[i][free]
        extra = basis*v/2
        omega.ints(extra)
        extras.append(sp.Matrix(omega.ints(extra).tolist()))
    saturated = hermite_normal_form(sp.Matrix.hstack(basis,*extras))
    assert (t-sp.eye(t.rows))*saturated == sp.zeros(t.rows,saturated.cols)
    # Primitivity cross-check independent of the projector argument.
    sf = smith_normal_form(saturated,domain=ZZ)
    assert all(abs(sf[i,i])==1 for i in range(saturated.cols))
    return saturated


def verify_lift(data,t):
    gram,a,b = data['gram'],data['a'],data['b']
    omega.ints(t)
    assert t*t == sp.eye(22) and t.T*gram*t == gram
    assert t*a == a*t and t*b == b*t
    reports = []
    for s in (sp.eye(22),a,b,a*b):
        g = t*s
        assert g*g == sp.eye(22) and g.T*gram*g == gram
        assert g*a == a*g and g*b == b*g and sp.trace(g) == 0
        info = fixed_invariants(gram,g)
        assert hermite_normal_form(info['basis']) == primitive_fixed_hnf(g)
        assert info['rank'] == 11 and info['signature'] == (1,10,0)
        reports.append(info)
    return reports


def matched_actions(data=None,verbose=True):
    if data is None:
        data = omega.enumerate_actions(verbose)
    change,gm = model_M(data,verbose)
    p,pinv,wanted_key = glue_matcher(data,change,gm)
    candidates = structured_candidates()
    matches = []
    for ci,t in enumerate(candidates):
        key = wanted_key(t)
        if key not in data['records']:
            continue
        assert t*t == sp.eye(10) and t.T*gm*t == gm and sp.trace(t)==0
        assert inertia_symmetric(discr.integer_kernel(t-sp.eye(10)).T*gm*
                                 discr.integer_kernel(t-sp.eye(10))) == (1,4,0)
        for triple in data['records'][key]:
            to = sum((data['contributions'][j][k] for j,k in enumerate(triple)))//2
            lift = p*sp.diag(t,sp.Matrix(to))*pinv
            omega.ints(lift)
            matches.append(dict(candidate=ci,triple=triple,tm=t,to=sp.Matrix(to),tau=lift))
    print('Matched M candidates:',len({x['candidate'] for x in matches}),flush=True)
    print('Full glued actions:',len(matches),flush=True)
    assert len(candidates)==1557
    assert len({x['candidate'] for x in matches})==24 and len(matches)==96
    return data,gm,p,pinv,matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',help='Write a new JSON certificate of all 96 lifts')
    args = parser.parse_args()
    data,gm,p,pinv,matches = matched_actions()
    profiles = Counter()
    rows = lambda mat: [[int(x) for x in row] for row in mat.tolist()]
    records = []
    for i,match in enumerate(matches):
        reports = verify_lift(data,match['tau'])
        profile = tuple((r['rank'],r['a'],r['delta']) for r in reports)
        profiles[profile] += 1
        records.append(dict(candidate=match['candidate'],triple=match['triple'],
                            tau=rows(match['tau']),types=profile,
                            fixed_grams=[rows(r['gram']) for r in reports],
                            smith_divisors=[r['snf'] for r in reports]))
        if (i+1)%16 == 0:
            print('Exact fixed-lattice checks:',i+1,'/',len(matches),flush=True)
    print('Exact profiles:',dict(profiles),flush=True)
    expected = {(9,11,9,7),(9,7,9,11),(11,9,7,9),(7,9,11,9)}
    assert set(profiles) == {tuple((11,a,1) for a in v) for v in expected}
    assert set(profiles.values()) == {24}
    encoded = json.dumps(records,sort_keys=True,separators=(',',':')).encode()
    digest = hashlib.sha256(encoded).hexdigest()
    print('Exact action/fixed-lattice record SHA256:',digest,flush=True)
    if args.output:
        with open(args.output,'x',encoding='utf-8') as stream:
            json.dump(dict(schema=1,gram=rows(data['gram']),sigma_A=rows(data['a']),
                           sigma_B=rows(data['b']),M_embedding=rows(p[:,:10]),
                           records_sha256=digest,records=records),stream,
                      sort_keys=True,separators=(',',':'))
            stream.write('\n')


if __name__ == '__main__':
    main()
