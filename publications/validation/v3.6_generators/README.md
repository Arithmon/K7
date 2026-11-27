# Generators of version 3.6

This directory holds the scripts that produce the tables of the K₇ framework paper, version 3.6, its LaTeX sources and the generated pages of this repository, with the result files they write. Supplement S3 (§S3.8) refers to it. The look-elsewhere test has its own directory, [`../v3.6/`](../v3.6/).

## Layout

The files are verbatim copies from the author's working repository and keep its relative paths (`canonical/...`). Comments and messages are in French.

| File | Bytes | sha256 | Role |
|---|---:|---|---|
| `canonical/scripts/k7_v3_6_exp_refresh.py` | 13 416 | `fdbe3e47f896c290d7438dabb459c86bd29aac639f9b48e1e40d4d8f81bff5f1` | refreshes the reference values of the dataset to the most recent measurements and logs every change |
| `canonical/results/k7_v3_6_exp_refresh.json` | 26 051 | `a76906f2561ddeda23fc58713d94410f5cd215b87312d11ae3bbdbfb0dc3a02e` | its log |
| `canonical/scripts/k7_v3_6_planck_ratios.py` | 6 612 | `7acc74714ed6034f93933d6640c61178dc37d3fb9e1e40b54e873f3c21e4354d` | computes the density ratios and their uncertainties on the public Planck 2018 chains (the archive is not included; its URL and sha256 are in the result) |
| `canonical/results/k7_v3_6_planck_ratios.json` | 4 979 | `096034a44bdaa1c1796aa39d2f3d0567330ad7a95a543b2a2e4ea5ca56818d06` | its result |
| `canonical/scripts/k7_v3_6_dataset_labels.py` | 13 048 | `7fb9a8bc350c726a365c63fe4961a2af1a939d67a4f5de1857d3279f7185b12a` | label pass of the dataset (titles, Lean pointers, notes) and its derived exports |
| `canonical/results/k7_v3_6_lean_map.json` | 13 901 | `cb7d8f9e9b165fa1ae1ae362c243a91c4656f97855990fe63bc7b28117c5d44f` | the map from each relation to its Lean declaration |
| `canonical/scripts/k7_v3_6_table_sec4.py` | 6 130 | `a4c87966d27ec3aa4a674c9ee166f42690505cfd295c152d2195248c9e703a6b` | generates the table of main §4.1 and the five classes from the dataset |
| `canonical/scripts/k7_v3_6_s2_status.py` | 2 956 | `aea4a8ec33bf1af34fe999cde7c48c06e506bb07087721d636add516ac9174a2` | status column of the tables of S2 |
| `canonical/scripts/k7_v3_6_s3_tables.py` | 7 944 | `df5b10330d117732ad21e3c97b34b610d102ac6863095185b4f5c2f08af6064d` | tables of S3 |
| `canonical/scripts/k7_v3_6_s4_tables.py` | 12 529 | `c62c4fde39dffc3a6569f60c0323073e2d9b72a87e13ae8e538cf8b7e66e421d` | tables of S4.2 and the figures of main §7.2, from the look-elsewhere results |
| `canonical/papers/framework/latex/gen_bib_3_6.py` | 1 087 | `160929ca588d9c5a92decab5ab91c16ed993b20e8ffd2702da4abe651a0c574a` | bibliography of the LaTeX sources, from the reference list of the main paper |
| `canonical/papers/framework/latex/build_3.6.sh` | 16 779 | `3a1c71a4f85e47c10fd61e957a990b7e0d58f1848210fe7cdeee3f9018c94126` | Markdown to LaTeX to PDF build of the five documents |
| `canonical/scripts/k7_v3_6_surface_pages.py` | 53 659 | `a9bc6852fdb5740f6b8dae484704c5df372cac7309a5870ada08a17ccef73700` | generated pages of this repository: statistical evidence, validation summary, observable reference |
| `canonical/scripts/k7_v3_6_surface_prose.py` | 66 298 | `2a452f278d8d82f6c3b378725864513758a8efef302373a9258789e3de1315d0` | FAQ, executive summary and physicists' overview |
| `canonical/scripts/k7_v3_6_reader_pages.py` | 11 351 | `82310d1565a7418aaba5bc926e33f3b389a84e37b3fed53cf8aec643c75a79cb` | Lean formalization and geometers' pages |
| `canonical/scripts/k7_v3_6_landing_pages.py` | 22 852 | `73387b913bcb7a6928ed539baf44518eabf0675e162e9f362d39e8b58a1c7818` | results, papers and falsification sections of the landing pages |
| `canonical/scripts/k7_v3_6_deposit_pages.py` | 58 050 | `3143996763bcf134ae46b6f52865171d8187c644f6a9fe80e94161726b796ed4` | citation files, structure pages, paper pages, changelog highlights, atlas; copies the papers |
| `canonical/scripts/k7_v3_6_surfaces_lint.py` | 16 805 | `2027475eea0a93dc8e8c3feba89282205b75c023932bd920da3a20481e6b48ad` | checks the public pages for statements that version 3.6 withdraws |
| `canonical/scripts/k7_v3_6_for_everyone_patch.py` | 17 444 | `f88c446aaa2c328124da270f20afc9a288d86901494d5f9eba2291b173dae185` | one-off targeted edits of the plain-language guide (2026-11-10) |
| `canonical/scripts/k7_v3_6_publish_generators.py` | 6 942 | `67f773e6473a2587e3e03433c11f04e6d778fb3a3ce586d165a4b9aedb893992` | this deposit |

## What runs from here, and what does not

These scripts read and write the author's working tree: the dataset `canonical/data/observables.json`, the Markdown sources of the papers under `canonical/papers/framework/`, and a clone of this repository and of [Arithmon/K7-Lean](https://github.com/Arithmon/K7-Lean) beside it. They are published so that every generated number and every generated page can be traced to the code that wrote it; they are not packaged as a standalone tool.

To rerun one of them, recreate the layout: the dataset is in [`../v3.6/canonical/data/observables.json`](../v3.6/canonical/data/observables.json) (the copy read by the look-elsewhere run), and the Markdown sources of the papers are in [`../../papers/markdown/`](../../papers/markdown/) under their public names (`k7_framework_3_6_main.md` is `physics_main.md`; `S1_foundations`, `S2_derivations`, `S3_observables` and `S4_sieve_diagnostics` are `supplement_foundations.md`, `supplement_derivations.md`, `supplement_observables.md` and `supplement_sieve_diagnostics.md`). The table generators have a `--check` mode that writes nothing and reports whether the tables of the papers are those the dataset produces.

`k7_v3_6_planck_ratios.py` takes as argument a directory holding the public Planck 2018 chain archive, whose URL and sha256 are recorded in its result. `k7_v3_6_exp_refresh.py` reads an earlier state of the dataset from the history of the working repository, which is not public: its log is given so that each changed value can be checked against its source.
