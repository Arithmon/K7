# Look-elsewhere test of version 3.6 (K7-V36-LEE)

This directory holds the code, the inputs and the results of the preregistered look-elsewhere test reported in the main paper (§7.2) and in supplement S4 (§S4.2) of the K₇ framework paper, version 3.6.

**Question.** Does K₇ remain exceptional when each competitor searches for its own formulas, in the same grammar, at the same budget, with the same freedom of assignment and of unit?

**Result.** K₇ reaches 31 of the 33 targets. 1 085 of 4 159 alternative Betti pairs reach as many (P = 0.261), and 1 015 of 2 000 invented vocabularies reach as many (P = 0.508); none reaches more. P_global = 0.508 against a preregistered threshold of 0.01: the look-elsewhere effect is not overcome, and the P-value of version 3.5 is withdrawn (verdict `LEE-RETRAIT`). A witness with no K₇ constant reaches 30 of the 33.

## Layout

The files are verbatim copies from the author's working repository and keep its relative paths (`canonical/...`), so that the scripts run unmodified and the hashes recorded in the results can be checked. Comments, the preregistration and some field names are in French.

| File | Bytes | sha256 |
|---|---:|---|
| `canonical/data/observables.json` | 62 405 | `dc77290984a729d278893f244683c1f8189df9f5f4d16490162693bfb9df0439` |
| `canonical/notes/k7_v3_6_lee_null_prereg_2026_10_17.md` | 17 657 | `a5b4071ae629f6d5f319a49ff48ece962c0980ef74e70b05274766cb51702607` |
| `canonical/papers/landscape_scan/mapping/landscape_scan.json` | 2 908 | `03074e5a83d6ff7efd51c3ef5d7a3be7863baa1e045926858a8762a9f1c50991` |
| `canonical/results/k7_v3_6_lee_null.json` | 4 872 057 | `844eeac4a8d250e763de352d0bd88fce9f9ec7f8b3537a4e77c4761a5b3e69a4` |
| `canonical/results/k7_v3_6_lee_null_closeout.json` | 1 181 | `0fc98b5883cb345547caa4399c89a8aea14a386b99b9e53ba39fdd4cc8910057` |
| `canonical/results/history/k7_v3_6_lee_null_first_run_2026_10_17.json` | 5 063 364 | `308900c9f1936d90613603765eee2c4632e16953ac9fe0f7a912fb8c86a12355` |
| `canonical/results/history/k7_v3_6_lee_null_rev1_2026_10_24.json` | 4 871 595 | `072e351a2d4ed269cb1803ce6a95df34d47c6a4b4501da3ea2051cb98c974a05` |
| `canonical/scripts/k7_v3_6_lee_null.py` | 15 828 | `75044f3dd2ad16ced8f63fcdc0d01f87ea59d928f0df5fed6023d5ace04418fb` |
| `canonical/scripts/k7_v3_6_lee_null_closeout.py` | 3 023 | `a470e13e0bcab6f16e5e740dbb09283fb0cbdd4241df67e06772cd5af6b39296` |
| `canonical/scripts/k7_v3_6_s4_tables.py` | 11 323 | `e857f5c9675be198ea2c89d053a99b38d5fe58ed8bfb4f0be00a597705c633c5` |

- `canonical/scripts/k7_v3_6_lee_null.py`: the producer. Its sha256 is the `self_sha256` field of the result.
- `canonical/results/k7_v3_6_lee_null.json`: the result of the current run (revision 2, 2026-11-03; 10 319 vocabularies, 2 h 48 on three processes). It records the hashes of the producer, of the dataset and of the Sieve grammar, and the Sieve commit.
- `canonical/scripts/k7_v3_6_lee_null_closeout.py` and its result: exact ties of the dual description cost.
- `canonical/data/observables.json`: the dataset of version 3.6 (95 entries), as read by the run. Its sha256 is the `observables_sha256` field of the result.
- `canonical/notes/k7_v3_6_lee_null_prereg_2026_10_17.md`: the preregistration, written before the first run, with its two amendments (2026-10-22 and 2026-11-03).
- `canonical/results/history/`: the results of the first run (2026-10-17) and of revision 1 (2026-10-24), from which the comparison table of S4.2.3 is built.
- `canonical/papers/landscape_scan/mapping/landscape_scan.json`: a reduced copy of the earlier landscape scan, with only the (21, 77) row. Gate G1 of the producer reads that row and no other; the file states the hash and the row count of the full scan.
- `canonical/scripts/k7_v3_6_s4_tables.py`: the generator of the tables of S4.2 and of the figures of main §7.2. It is given for inspection: it writes into the paper sources and reads the two earlier results from the history of the working repository, so it does not run from this directory.

## Running it

The producer needs Python 3 (standard library only) and a clone of the Sieve at the commit recorded in the result (`sieve_head`, [Arithmon/Sieve](https://github.com/Arithmon/Sieve) `601283f`).

```
git clone https://github.com/Arithmon/Sieve && git -C Sieve checkout 601283f
cd K7/publications/validation/v3.6
SIEVE_DIR=/path/to/Sieve/scripts python3 canonical/scripts/k7_v3_6_lee_null.py --limit 2 --workers 3
```

`--limit N` runs the first N vocabularies of each family and writes `canonical/results/k7_v3_6_lee_null_limited.json`; it takes about twenty seconds for N = 2 and already replays the gates and the blind search of K₇ (31/33, 408.1 bits). Without `--limit` the full run rewrites `canonical/results/k7_v3_6_lee_null.json` (about three hours on three processes). The producer records the commit of the enclosing git repository in `git_head`, so a rerun differs from the deposited result in that field and in `seconds`.

```
python3 canonical/scripts/k7_v3_6_lee_null_closeout.py
```

rewrites the closeout result from the deposited run; it reproduces the deposited file bit for bit.

## What the test does not show

P_global = 0.51 is not a probability that K₇ is right or wrong, and the counts are not a physical refutation. With 30 targets reached by every competitor, two by none and one that separates them, the score has little discriminating power in this protocol. The scope and the limits of the test are stated in S4.2.4.
