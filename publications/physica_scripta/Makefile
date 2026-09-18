PYTHON ?= python3
export OPENBLAS_NUM_THREADS = 1
export OMP_NUM_THREADS = 1
export PYTHONDONTWRITEBYTECODE = 1
export MPLBACKEND = Agg
export MPLCONFIGDIR = /tmp/k7-physica-matplotlib

.PHONY: paper-data calculations render check test submission-check manuscript
calculations:
	$(PYTHON) scripts/metric_certificate.py
	$(PYTHON) scripts/hodge2_matching.py
	$(PYTHON) scripts/hodge3_matching.py
	$(PYTHON) scripts/adiabatic_bound.py
	$(PYTHON) scripts/scalar_spectrum.py
	$(PYTHON) scripts/weyl_law.py
	$(PYTHON) scripts/kk_tower.py
	$(PYTHON) scripts/hodge_profiles.py
	$(PYTHON) scripts/intersection_form.py
	$(PYTHON) scripts/democracy_check.py
	$(PYTHON) scripts/lambda1_enclosure.py
	$(PYTHON) scripts/check_lambda1_enclosure.py

paper-data: calculations
	$(PYTHON) scripts/paper_data.py
	$(PYTHON) scripts/check_claims.py

render:
	$(PYTHON) scripts/paper_data.py
	$(PYTHON) scripts/check_claims.py

check:
	$(PYTHON) scripts/check_claims.py

test:
	$(PYTHON) -m unittest discover -s tests -v

submission-check: check test
	$(PYTHON) scripts/check_claims.py --submission

manuscript: check
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error physica_scripta.tex
	cd manuscript && bibtex physica_scripta
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error physica_scripta.tex
	cd manuscript && pdflatex -interaction=nonstopmode -halt-on-error physica_scripta.tex
