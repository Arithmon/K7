#!/usr/bin/env python3
"""Exhaust the trace-zero involutions in the labelled V4 centralizer of Omega.

All D4 automorphisms are enumerated by images of its simple roots, not a
bounded matrix search. The three sector lattices and their glue are derived
from the live Piroddi backend. Integer numpy arithmetic is used only after
exact denominator clearing (with explicit overflow bounds).
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import itertools
import json

import numpy as np
import sympy as sp

import check_k3_rho17_v4_discriminant_gluing as discr

D4 = sp.Matrix([[2, -1, 0, 0], [-1, 2, -1, -1],
                [0, -1, 2, 0], [0, -1, 0, 2]])
CHANGES = (
    sp.Matrix([[-1,-1,1,1],[-1,0,0,0],[1,2,-1,-1],[-1,-1,0,1]]),
    sp.Matrix([[-1,0,0,0],[1,0,1,1],[-1,1,-1,-1],[-1,0,-1,0]]),
    sp.Matrix([[-1,-1,1,1],[-1,0,0,0],[1,2,-1,-1],[-1,-1,0,1]]),
)


def ints(matrix):
    assert all(sp.Rational(x).q == 1 for x in matrix)
    assert max((abs(int(x)) for x in matrix), default=0) < 10**8
    return np.array(matrix.tolist(), dtype=np.int64)


def d4_automorphisms():
    # Columns e1-e2, e2-e3, e3-e4, e3+e4.
    simple = sp.Matrix([[1,0,0,0],[-1,1,0,0],[0,-1,1,1],[0,0,-1,1]])
    assert simple.T * simple == D4
    roots = []
    for i,j in itertools.combinations(range(4), 2):
        for a,b in itertools.product((-1,1), repeat=2):
            v = sp.zeros(4,1)
            v[i],v[j] = a,b
            roots.append(tuple(int(x) for x in simple.inv()*v))
    roots = np.array(sorted(roots), dtype=np.int64)
    products = roots @ ints(D4) @ roots.T
    result = []
    for center in range(24):
        neighbors = [i for i in range(24) if products[center,i] == -1]
        for a,b,c in itertools.permutations(neighbors, 3):
            if products[a,b] or products[a,c] or products[b,c]:
                continue
            result.append(roots[[a,center,b,c]].T.copy())
    result.sort(key=lambda x: tuple(x.flat))
    assert len(result) == 1152
    assert len({tuple(x.flat) for x in result}) == 1152
    for x in result:
        assert np.array_equal(x.T @ ints(D4) @ x, ints(D4))
    # Independent completeness check: signed coordinate permutations and
    # a Hadamard triality isometry generate the same 1152-element group.
    generators = []
    for i in range(3):
        t = sp.eye(4)
        t.col_swap(i,i+1)
        generators.append(ints(simple.inv()*t*simple))
    generators.append(ints(simple.inv()*sp.diag(-1,1,1,1)*simple))
    hadamard = sp.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
    generators.append(ints(simple.inv()*hadamard*simple))
    seen = {tuple(np.eye(4,dtype=np.int64).flat)}
    queue = [np.eye(4,dtype=np.int64)]
    for x in queue:
        for generator in generators:
            y = x@generator
            key = tuple(y.flat)
            if key not in seen:
                seen.add(key)
                queue.append(y)
    assert seen == {tuple(x.flat) for x in result}
    return result


def setup():
    gram,a,b = discr.build_standard_v4()
    m = discr.integer_kernel(sp.Matrix.vstack(a-sp.eye(22),b-sp.eye(22)))
    o = discr.integer_kernel(m.T*gram)
    sectors = [discr.integer_kernel(sp.Matrix.vstack(a-ea*sp.eye(22),
                b-eb*sp.eye(22)))*c
               for (ea,eb),c in zip(((-1,1),(1,-1),(-1,-1)),CHANGES)]
    for s in sectors:
        assert s.T*gram*s == -2*D4
    left = (o.T*o).inv()*o.T
    p = left*sp.Matrix.hstack(*sectors)
    assert abs(p.det()) == 16
    assert all(sp.Rational(x).q == 1 for x in p)
    return gram,a,b,m,o,p


def enumerate_actions(verbose=True):
    gram,a,b,m,o,p = setup()
    go = o.T*gram*o
    auts = d4_automorphisms()
    invols = [x for x in auts if np.trace(x) == 0 and
              np.array_equal(x@x,np.eye(4,dtype=np.int64))]
    assert len(invols) == 90
    pinv = p.inv()
    contributions = []
    for i in range(3):
        contributions.append(np.stack([ints(2*p[:,4*i:4*i+4]*sp.Matrix(x)*
                                     pinv[4*i:4*i+4,:]) for x in invols]))
    dual4 = ints(4*go.inv())
    assert max(np.max(np.abs(c)) for c in contributions)*3*12*np.max(np.abs(dual4)) < 2**63
    records = {}
    # T G^-1 modulo Z, encoded in the primitive Omega basis; basis-dependent
    # but canonical and injective for discriminant actions in this fixed basis.
    for i in range(90):
        for j in range(90):
            totals = contributions[0][i]+contributions[1][j]+contributions[2]
            for k in np.flatnonzero(np.all(totals % 2 == 0, axis=(1,2))):
                t = totals[k]//2
                key = bytes(np.asarray((t@dual4)%4,dtype=np.uint8).flat)
                records.setdefault(key,[]).append((i,j,int(k)))
    counts = Counter(map(len,records.values()))
    total = sum(len(v) for v in records.values())
    identity_key = bytes(np.asarray(dual4%4,dtype=np.uint8).flat)
    digest = hashlib.sha256(b''.join(sorted(records))).hexdigest()
    if verbose:
        print('D4 automorphisms:',len(auts),flush=True)
        print('Trace-zero involutions per sector:',len(invols))
        print('Triples:',len(invols)**3)
        print('Omega-integral triples:',total)
        print('Discriminant actions:',len(records))
        print('Fibre multiplicities:',dict(sorted(counts.items())))
        print('Identity discriminant action present:',identity_key in records)
        print('Sorted action-table SHA256:',digest,flush=True)
    assert total == 47304
    assert len(records) == 11826 and counts == {4:11826}
    assert identity_key not in records
    return dict(gram=gram,a=a,b=b,m=m,o=o,p=p,invols=invols,
                contributions=contributions,records=records,digest=digest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',help='Optional noncanonical JSON table destination')
    args = parser.parse_args()
    data = enumerate_actions()
    if args.output:
        out = dict(schema=1,encoding='row-major (4*T*G_Omega^-1 mod 4), 12x12 bytes',
                   sha256=data['digest'],
                   omega_gram=[[int(x) for x in row] for row in
                               (data['o'].T*data['gram']*data['o']).tolist()],
                   sector_in_omega=[[int(x) for x in row] for row in data['p'].tolist()],
                   d4_involutions=[x.tolist() for x in data['invols']],
                   actions=[dict(action_hex=k.hex(),triples=v)
                            for k,v in sorted(data['records'].items())])
        # Matrix entries must be native Python integers for portable JSON.
        out['omega_basis'] = [[int(x) for x in row] for row in data['o'].tolist()]
        with open(args.output,'x',encoding='utf-8') as stream:
            json.dump(out,stream,sort_keys=True,separators=(',',':'))
            stream.write('\n')


if __name__ == '__main__':
    main()
