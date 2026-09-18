# Physica Scripta: audited paper projection

This isolated directory starts from the pinned K7 source commit in
[SOURCE_FREEZE.json](SOURCE_FREEZE.json). It does not modify OpenWave,
K3-CAP, Phase 3/4, the historical papers or their notebooks.

**This is a working branch, not a submission-ready paper.** The fresh
reduced scalar eigenvalue enclosure is certified for the frozen coordinate
input. NK torsion-free existence, the matching multiplicities, the full
adiabatic transfer, KK completeness and the geometric intersection form
remain open. See [AUDIT.md](AUDIT.md) and [THEOREMS.md](THEOREMS.md).

## Run

From this directory:

```sh
make paper-data
make test
make manuscript
make submission-check
```

Or from the repository root:
`make -C publications/physica_scripta paper-data`.

Python with the already available NumPy, SciPy, SymPy, mpmath and Matplotlib
is needed. No notebook execution, GPU training, K3 pool, network access or
installation is part of the build. Exact versions used are recorded in
each result. Tests use the standard-library unittest runner.

The last command **must fail while submission gates remain open**.
A passing data-integrity/test command is not publication approval.
The reduced interval checker can be rerun with
`python3 scripts/check_lambda1_enclosure.py`.

## Authority and terminology

- **exact**: algebraic or rational equality under explicitly stated inputs.
- **proved**: a mathematical statement with its hypotheses and proof in THEOREMS.md.
- **certified**: validated interval/rational computation and a replayable checker,
  within the stated model and trusted arithmetic base.
- **numerical**: floating-point computation, with convergence/residual diagnostics.
- **conditional**: statement requiring named unproved hypotheses.
- **pending**: evidence needed for the claim is absent or invalid.

The machine field claim_status is CERTIFIED / NUMERICAL / CONDITIONAL /
PENDING; evidence_kind distinguishes exact, proved, certified and numerical.
A model definition can be exact without making the metric torsion-free.

The generated [CLAIMS_MANIFEST.json](CLAIMS_MANIFEST.json) records value,
status, source script, JSON selector, scope, theorem, source commit, metric
hash and section. [ARTIFACT_MAP.md](ARTIFACT_MAP.md) links them.
Only accepted claims get numeric LaTeX macros. Pending claims produce
limitations; they do not unlock strong wording.

## Inputs and history

The input metric is A's embedded optimized coefficient array, interpreted
as exact dyadic values. Gamma, coordinate order, determinant normalization,
domain and reconstruction are explicit. A's base tensor and B's tensor
coincide; B therefore uses a different metric from this projection.

Historical PDFs and notebooks are retained at their original paths,
identified by immutable commit and SHA256 in the freeze. The skeleton
found in the local downloads was copied unchanged into sources/.
[LEGACY_SNAPSHOTS.md](LEGACY_SNAPSHOTS.md) marks their role without changing
the archival bytes.

## Manuscript and release

manuscript/physica_scripta.tex is a data-driven working draft, currently in
the standard article class (iopart.cls is not installed; nothing was installed).
Its generated tables, macros and limitations
are checked byte-for-byte against the manifest and results.
The historical certification title and abstract are not carried forward.
The final abstract, conclusion, journal formatting, bibliography expansion,
external review and release tag require the scientific gates to close.
No submission tag is created by this build.

To freeze a submission later, pass submission-check, review the full
manuscript and commit, then deliberately create the submission tag.
Every source dependency must remain pinned; no output points to moving main.
