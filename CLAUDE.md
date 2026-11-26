# CLAUDE.md - Development Guide for the K₇ Documentation Repository

Conventions for editing this repository. It describes the state of version 3.6 of the framework paper.

## Repository Purpose

This repository holds the **papers, datasets and public pages** of the K₇ framework (formerly GIFT). The Lean 4 formalization and the Python package are in [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean). The layout is described in [`STRUCTURE.md`](STRUCTURE.md), which is generated.

## What version 3.6 says, and what it withdrew

Every page must agree with the main paper, `publications/papers/markdown/k7_framework_3_6_main.md`.

- The framework is a **declared correspondence**: 33 closed-form relations assigned by the author to dimensionless parameters. It is a candidate, not a derivation. No geometric map from the invariants to the observables is known, and no rule assigns a formula to an observable.
- **No compact G₂ manifold with Betti numbers (21, 77) is known.** Existence is open; the pair is posited.
- The 33 relations are compared with data in five classes (within 2σ, tension, excluded as exact equalities at more than 3σ and kept as proximities, inside a PDG range, non-Gaussian profile). The counts come from the dataset, never from memory.
- The other 62 entries of the dataset are conditional extractions and diagnostics, and are not counted as predictions.
- The preregistered look-elsewhere test finds that closeness to the measured values does not single out K₇. As preregistered, **no p-value is reported**; counts and proportions are.
- The Lean formalization verifies arithmetic, not physics.

**Withdrawn wordings, do not write**: "zero parameters", "no free parameters", "derives", "predicts" or "explains" for a relation; "proven" for a physical statement; "K₇ exists" or "a theorem guarantees K₇"; any coincidence probability, p-value, Bayes factor or "unique among N alternatives"; "95 observables" as a count of predictions; a tolerance band around δ_CP.

**Write instead**: "the relation assigns", "the closed form evaluates to", "reproduced" (for N_gen = 3), "posited" (for the Betti pair), "within 2σ of measurement", "excluded as an exact equality, kept as a proximity".

## Generated files: do not edit by hand

These files are written by generators from the paper sources and the dataset. A hand edit is overwritten at the next run, and the generators' `--check` mode reports it.

| Files | Generator |
|---|---|
| `publications/papers/markdown/k7_framework_3_6_*.md`, `tex/`, `pdf/` | copied from the author's sources by `k7_v3_6_deposit_pages.py` |
| `CITATION.md`, `CITATION.cff`, `STRUCTURE.md`, `docs/wiki/Citation-Guide.md`, `Repository-Structure.md`, `Paper-Main-Framework.md`, `Paper-S1-Foundations.md`, `Paper-S2-Derivations.md`, `Changelog-Highlights.md`, `publications/references/README.md`, `GIFT_ATLAS.json` | `k7_v3_6_deposit_pages.py` |
| `docs/wiki/Statistical-Evidence*.md`, `Validation-Summary*.md`, `Observable-Reference*.md`, `publications/references/STATISTICAL_EVIDENCE.md`, `OBSERVABLE_REFERENCE.md`, `observables.csv` | `k7_v3_6_surface_pages.py` |
| `docs/FAQ*.md`, `docs/wiki/FAQ*.md`, `docs/GIFT_EXEC_SUMMARY*.md`, `docs/INFO_GEO_FOR_PHYSICISTS.md`, `docs/wiki/For-Physicists.md` | `k7_v3_6_surface_prose.py` |
| `docs/LEAN_FOR_PHYSICS.md`, `docs/GIFTPY_FOR_GEOMETERS.md`, `docs/wiki/Lean-Formalization.md`, `For-Formalization-Experts.md`, `For-Geometers.md` | `k7_v3_6_reader_pages.py` |
| the results, papers and falsification sections of `docs/index.html` and `docs/index.fr.html` | `k7_v3_6_landing_pages.py` |

The generators are published in `publications/validation/v3.6_generators/`.

## Frozen files: never edit

- `publications/validation/v3.6/canonical/`: the deposit of the look-elsewhere test. Its files are listed with their sha256 and are kept byte for byte.
- `publications/papers/legacy/` and the 3.4 and 3.5 files: published versions. Version 3.5 is read with `publications/ERRATUM_v3.5.md`.
- Blog pages (`docs/wiki/Blog-*.md`) are dated texts: they say what was held at their date and are not rewritten.

## Languages

French pages exist only for the landing page, Home, Getting-Started, Site-Map, Observable-Reference, Validation-Summary, Statistical-Evidence, the FAQ, K₇ for Everyone, the executive summary and the blog. Do not create other `.fr` pages.

## Writing Guidelines

- **State the present position.** No evolutionary narrative in the body of a page ("in v3.1 we improved"); what changed goes in a changelog.
- **Standard academic terms**, no internal identifiers of tests, rules or batches in prose.
- **No em dash** in Markdown: the documentation linter refuses it.
- **A count is derived**, from `publications/references/observables.csv` or from the Lean repository, never recalled.

## Checks before committing

```bash
python .github/scripts/docs_linter.py
python .github/scripts/fix_em_dashes.py --check
python .github/scripts/observable_calculator.py
python .github/scripts/cross_repo_check.py --core-path ../K7-Lean
```

## Links

| Resource | URL |
|----------|-----|
| Lean repository | https://github.com/Arithmon/K7-Lean |
| Program | https://github.com/Arithmon/Program |
| Site | https://arithmon.github.io/K7/ |

---

## GPU Computing Tips (CuPy/CUDA)

When writing notebooks for GPU execution (Colab A100), be aware of CuPy limitations:

### CuPy Sparse Matrix Gotchas

| SciPy | CuPy | Workaround |
|-------|------|------------|
| `M.tolil()` | ❌ Not implemented | Build COO/CSR directly |
| `eigsh(..., which='SM')` | ❌ Only 'LM', 'LA', 'SA' | Use `which='SA'` for smallest eigenvalues |
| `M[i,j] = x` on CSR | ❌ Inefficient/broken | Build from COO format |

### Correct Pattern for Periodic BC Sparse Matrix

```python
# ❌ Wrong (CuPy incompatible)
D2 = cp_diags([...], format='csr')
D2 = D2.tolil()           # NotImplementedError!
D2[0, N-1] = 1/h²
D2 = D2.tocsr()

# ✓ Correct (build COO directly)
row, col, data = [], [], []
for i in range(N):
    row.append(i); col.append(i); data.append(-2/h²)
    row.append(i); col.append((i+1) % N); data.append(1/h²)  # periodic
    row.append(i); col.append((i-1) % N); data.append(1/h²)  # periodic
D2 = cp_csr((cp.array(data), (cp.array(row), cp.array(col))), shape=(N, N))
```

### Eigenvalue Computation

```python
# ❌ Wrong for CuPy
eigs = cp_eigsh(L, k=10, which='SM')  # ValueError!

# ✓ Correct for CuPy (positive semi-definite matrices)
eigs = cp_eigsh(L, k=10, which='SA')  # Smallest Algebraic
```

### Memory Management

```python
# Clear GPU memory between large computations
cp.get_default_memory_pool().free_all_blocks()
```

### JSON Serialization with NumPy Types

NumPy types (`numpy.bool_`, `numpy.int64`, `numpy.float64`) are not JSON-serializable:

```python
# ❌ Wrong (TypeError: Object of type bool_ is not JSON serializable)
results = {'passed': deviation < 5}  # numpy.bool_
json.dump(results, f)

# ✓ Correct (explicit conversion to Python types)
results = {'passed': bool(deviation < 5)}
json.dump(results, f)
```

Common conversions:
| NumPy Type | Python Conversion |
|------------|-------------------|
| `numpy.bool_` | `bool(x)` |
| `numpy.int64` | `int(x)` |
| `numpy.float64` | `float(x)` |
| `numpy.ndarray` | `x.tolist()` |

---

*GIFT Documentation Repository*
