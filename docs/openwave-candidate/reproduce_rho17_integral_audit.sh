#!/usr/bin/env bash
set -euo pipefail

export PYTHONDONTWRITEBYTECODE=1
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
export PYTHONPATH="${PYTHONPATH:-}:$ROOT/../.pylibs-k3-mp130:$ROOT/../.pylibs-k3:$SCRIPT_DIR"

python3 "$SCRIPT_DIR/check_k3_rho17_tauOmega_discriminant_actions.py"
python3 "$SCRIPT_DIR/check_k3_rho17_tauM_matching.py"
python3 "$SCRIPT_DIR/check_k3_rho17_jk_reflection_twists.py" --bound 2
python3 "$SCRIPT_DIR/check_k3_rho17_jk_eichler_twists.py" --bound 2
