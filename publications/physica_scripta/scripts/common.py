"""Shared provenance and metric reconstruction for the isolated paper pipeline."""
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys
import numpy as np
import scipy
import mpmath

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads((ROOT / path).read_text())

def metric_hash():
    # Includes reconstruction semantics, not just the coefficient array.
    payload={"input":sha(ROOT/"inputs/metric.json"),"reconstruction":sha(ROOT/"scripts/common.py")}
    return hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()

def write_result(name, payload, inputs=()):
    paths = ["inputs/metric.json", "SOURCE_FREEZE.json", "THEOREMS.md", "scripts/common.py",
             "scripts/" + Path(sys.argv[0]).name, *inputs]
    paths = sorted(set(paths))
    payload = dict(payload, schema_version=1, metric_sha256=metric_hash(),
                   source_commit=read("SOURCE_FREEZE.json")["source_commit"],
                   provenance={p: sha(ROOT/p) for p in paths},
                   environment={"python": platform.python_version(), "numpy": np.__version__,
                                "scipy": scipy.__version__, "mpmath": mpmath.__version__})
    (ROOT/"results"/name).write_text(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n")
    return payload

def validate_freeze():
    f = read("SOURCE_FREEZE.json")
    for entry in f["files"]:
        if sha(REPO/entry["path"]) != entry["sha256"]:
            raise ValueError("Frozen source changed: "+entry["path"])
        if "source_commit" in f:
            blob=subprocess.check_output(["git","show",f["source_commit"]+":"+entry["path"]],cwd=REPO)
            if hashlib.sha256(blob).hexdigest()!=entry["sha256"]:
                raise ValueError("Source commit does not contain pinned bytes: "+entry["path"])
    return f

def validate_metric_input():
    data=read("inputs/metric.json")
    c=np.asarray(data["coefficients"],dtype="<f8")
    legacy=json.loads((REPO/"publications/papers/notebooks/g2_certified_neck_companion_results.json").read_text())
    actual=hashlib.sha256(c.tobytes()).hexdigest()
    if c.shape!=(6,28) or actual!=data["coefficient_sha256"]:
        raise ValueError("Coefficient shape/hash mismatch")
    if actual!=legacy["coefficient_hashes_sha256"]["OPT_COEFFS"]:
        raise ValueError("Input is not the frozen optimized metric")
    if data["gamma"]!=legacy["parameters"]["acyl_decay_rate"]:
        raise ValueError("Decay rate differs from selected source")
    if data["domain"]!=[-2,3] or data["seam"]!=[0,1] or data["determinant"]!=[65,32]:
        raise ValueError("The current operator contract requires the frozen domain/normalization")

def validate_result(path):
    data = read(path)
    if data["source_commit"] != read("SOURCE_FREEZE.json")["source_commit"]:
        raise ValueError("Source commit mismatch: "+path)
    if data["metric_sha256"] != metric_hash():
        raise ValueError("Metric hash mismatch: "+path)
    for p, digest in data["provenance"].items():
        if sha(ROOT/p) != digest:
            raise ValueError("Stale result dependency: "+p)
    return data

def metric(s):
    """Smooth seam, C1 exponential extensions; numerical evaluation only."""
    data = read("inputs/metric.json")
    c = np.asarray(data["coefficients"])
    s = np.atleast_1d(s).astype(float)
    x = 2*np.clip(s, 0, 1)-1
    flat = np.polynomial.chebyshev.chebval(x, c).T
    dc = np.polynomial.chebyshev.chebder(c, axis=0)*2
    gamma = data["gamma"]
    for edge, mask, sign in [(0, s<0, 1), (1, s>1, -1)]:
        value = np.polynomial.chebyshev.chebval(2*edge-1, c)
        deriv = np.polynomial.chebyshev.chebval(2*edge-1, dc)
        flat[mask] = value + sign*deriv/gamma*(np.exp(sign*gamma*(s[mask,None]-edge))-1)
    L = np.zeros((len(s), 7, 7))
    L[:, np.tril_indices(7)[0], np.tril_indices(7)[1]] = flat
    for k in range(7):
        L[:,k,k] = np.logaddexp(0, L[:,k,k])
    det_target = data["determinant"][0]/data["determinant"][1]
    scale = np.exp((0.5*np.log(det_target)-np.log(np.diagonal(L,axis1=1,axis2=2)).sum(axis=1))/7)
    L *= scale[:,None,None]
    g = L @ L.transpose(0,2,1)
    return g, np.linalg.inv(g)

def coefficients(s):
    g, gi = metric(s)
    data=read("inputs/metric.json")
    w = np.full(len(g), np.sqrt(data["determinant"][0]/data["determinant"][1]))
    return w*gi[:,0,0], w

def chebyshev(n, left=-2., right=3.):
    """Ascending Lobatto nodes and differentiation in the physical coordinate."""
    x = np.cos(np.pi*np.arange(n+1)/n)
    c = np.ones(n+1); c[[0,-1]] = 2; c *= (-1.)**np.arange(n+1)
    dx = x[:,None]-x[None,:]
    D = (c[:,None]/c[None,:])/(dx+np.eye(n+1))
    D -= np.diag(D.sum(axis=1))
    order = np.arange(n,-1,-1)
    return ((left+right)/2+(right-left)/2*x)[order], D[np.ix_(order,order)]*2/(right-left)
