#!/usr/bin/env python3
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
"""
k7_v3_6_lee_null_closeout.py -- consommateur de closeout de K7-V36-LEE (sans pool, sans énumération) : paie la dette M1
de la revue Codex du jalon measure (`codex_k7-v3-6-lee-null_review_2026_10_17.md`, commit c595fddf4).

Le producteur compare `S_cost <= k7cost` en flottants ; or chaque coût est L·log₂(38) + O·log₂(9) avec (L, O) entiers,
et des égalités mathématiques se trouvent coupées par l'ordre des additions (écarts ≤ 1,2·10⁻¹³). Ce que le corpus
dit : le Sieve tolère déjà ces comparaisons MDL (`rank_at`). Ce que j'écris : égalité si |ΔS_cost| ≤ 1e-9 bit, très
en dessous de l'écart minimal entre deux coûts distincts. S_cover, P_global et le verdict ne bougent pas (entiers).

Usage : python3 canonical/scripts/k7_v3_6_lee_null_closeout.py → canonical/results/k7_v3_6_lee_null_closeout.json
"""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'canonical/results/k7_v3_6_lee_null.json'
OUT = ROOT / 'canonical/results/k7_v3_6_lee_null_closeout.json'
TOL = 1e-9
L38, L9 = math.log2(38), math.log2(9)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def couple(c):
    """(L, O) entiers tels que c = L·log₂38 + O·log₂9, dans les bornes du budget, ou None."""
    for L in range(1, 100):
        O = round((c - L * L38) / L9)
        if 0 <= O <= 132 and abs(c - L * L38 - O * L9) < 1e-8:
            return L, O
    return None


def main():
    o = json.loads(SRC.read_text(encoding='utf-8'))
    k = o['K7']['S_cost']
    fam = {}
    for F in ('F-BETTI', 'F-VOCAB', 'F-BETTI-FICHE'):
        c = [r['S_cost'] for r in o['lignes'] if r['famille'] == F]
        st = sum(x < k - TOL for x in c); eq = sum(abs(x - k) <= TOL for x in c)
        fam[F] = {'n': len(c), 'strictement_moins_cher': st, 'egalites': eq,
                  'P_cost_dual_corrige': (1 + st + eq) / (1 + len(c)),
                  'P_cost_dual_artefact': o['familles'][F]['P_cost_dual'],
                  'couples_des_egalites': sorted({couple(x) for x in c if abs(x - k) <= TOL})}
    sans_couple = sum(couple(r['S_cost']) is None for r in o['lignes'])
    out = {'lot': 'K7-V36-LEE-CLOSEOUT', 'source': str(SRC.relative_to(ROOT)), 'source_sha256': sha(SRC),
           'self_sha256': sha(__file__), 'tolerance_bits': TOL, 'K7_S_cost': k, 'K7_couple': couple(k),
           'lignes_sans_couple_entier': sans_couple, 'familles': fam,
           'inchange': {'P_global': o['P_global'], 'verdict': o['verdict']}}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    for F, v in fam.items():
        print(F, v['strictement_moins_cher'], v['egalites'], round(v['P_cost_dual_corrige'], 6), v['couples_des_egalites'])
    print('K7', couple(k), 'sans couple', sans_couple, '→', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
