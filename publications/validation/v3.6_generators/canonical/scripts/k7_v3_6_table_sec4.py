#!/usr/bin/env python3
"""K₇ v3.6 — régénère les colonnes Measured / Dev. / Pull de la table §4.1 de physics_main.md
DEPUIS canonical/data/observables.json (R6 : les tables d'une note se régénèrent depuis le JSON).

Les colonnes ID / Observable / Formula / K₇ value viennent du texte et ne sont pas réécrites, sauf
l'étiquette de A16/A18 (sin θ, pas sin²θ : le symbole du JSON fait foi). La colonne Status est
réécrite pour les entrées listées dans STATUS (décisions de Brieuc du 2026-10-22), sinon gardée.

Usage : python3 canonical/scripts/k7_v3_6_table_sec4.py [--check | --counts]
        --check : n'écrit rien, sort 1 si la table diffère de ce que le JSON produit.
"""
import io
import json
import math
import os
import sys

if (sys.stdout.encoding or '').lower() != 'utf-8':   # pas de double enveloppe à l'import
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
PM = os.path.join(ROOT, 'canonical', 'papers', 'framework', 'physics_main.md')

LABEL = {'A16': 'sin θ₁₂ (CKM)', 'A18': 'sin θ₂₃ (CKM)'}
STATUS = {
    'A06': 'integer; approximate (R8); **tension**',
    'A10': 'integer; **proximity** (in the scheme declared in R7)',   # décision de Brieuc du 2026-10-24 : règle G
    'A08': 'integer; inside the PDG range',
    'A21': 'integer; **proximity**',
    'A16': 'integer; approximate (R12)',
    'A17': 'integer; approximate (R12)',
    'A18': 'integer; approximate (R12)',
    'A13': 'integer; **non-Gaussian profile** (octant; inside the NuFIT 3σ range, §4.3)',
    'A22': 'integer; approximate (R8); **proximity**',
    # surdétermination cosmologique (R11, décision de Brieuc du 2026-10-22)
    'A23': 'ln 2; approximate (R11)',
    'A25': 'integer; approximate (R11)',
    'A26': 'integer; det(g); approximate (R11)',
    'A27': 'integer; approximate (R11)',
    'A29': 'integer; det(g); approximate (R11)',
    'A30': 'integer; det(g); approximate (R11); **tension**',
    'A33': 'integer; κ_T; approximate (R11)',
}
GAUSS_NOTE = {'A13'}   # profil non gaussien : le pull est marqué *


def classify(obs):
    """Classes du décompte (vocabulaire du main §4.1, revue externe du 2026-10-22) :
    within_2sigma (|pull| ≤ 2), tension (2 < |pull| ≤ 3), excluded_3sigma (|pull| > 3, proximité),
    in_range (plage PDG, pas de pull), non_gaussian (profil non gaussien). m_b/m_t est comparé dans le
    schéma déclaré par R7 et classé par son pull (décision du 2026-10-24 : plus de classe « scheme »)."""
    out = {k: [] for k in ('within_2sigma', 'tension', 'excluded_3sigma', 'in_range', 'non_gaussian')}
    for i, o in sorted(obs.items()):
        if o['type'] != 'I':
            continue
        if o.get('exp_error') is None:
            out['in_range'].append(i); continue
        if i in GAUSS_NOTE:
            out['non_gaussian'].append(i); continue
        p = abs((o['gift_value'] - o['exp_value']) / o['exp_error'])
        out['within_2sigma' if p <= 2 else 'tension' if p <= 3 else 'excluded_3sigma'].append(i)
    return out


def sig_digits(err, val=None):
    """Décimales : 2 chiffres significatifs sur l'erreur, puis une de moins si la valeur ET
    l'erreur finissent par 0 à cette précision (0.231220(60) → 0.23122(6) ; 0.462(20) reste)."""
    e = int(math.floor(math.log10(err)))
    nd = max(0, 1 - e)
    if val is not None and nd > 0:
        u = 10 ** nd
        if round(err * u) % 10 == 0 and round(abs(val) * u) % 10 == 0:
            nd -= 1
    return nd


def fmt_measured(o):
    v, asym = o['exp_value'], o.get('exp_error_asym')
    if o.get('exp_range'):
        lo, hi = o['exp_range']
        return f'{lo}–{hi} (range)'
    if o['id'] == 'A15':
        lo, hi = asym
        return f"{v:.0f} (+{hi:.0f}/−{lo:.0f})°"
    if asym:
        lo, hi = asym
        nd = sig_digits(min(lo, hi), v)
        u = 10 ** nd
        return f"{v:.{nd}f}(+{round(hi * u)}/−{round(lo * u)})"
    e = o['exp_error']
    if o['id'] in ('A04', 'A07'):          # erreur à 10⁻⁸ : on montre assez de chiffres
        nd = sig_digits(e, v)
        return f"{v:.{nd}f}({round(e * 10 ** nd)})"
    nd = sig_digits(e, v)
    return f"{v:.{nd}f}({round(e * 10 ** nd)})"


def fmt_dev(o):
    if o.get('exp_range'):
        return 'n/a'
    d = (o['gift_value'] - o['exp_value']) / o['exp_value'] * 100
    s = '+' if d > 0 else '−' if d < 0 else ''
    a = abs(d)
    if a < 0.01:
        return f"{s}{a:.4f}%"
    return f"{s}{a:.3f}%" if a < 0.1 else f"{s}{a:.2f}%"


def fmt_pull(o):
    if o.get('exp_error') is None:
        return 'n/a'
    p = (o['gift_value'] - o['exp_value']) / o['exp_error']
    if abs(p) > 100:
        return '≫ 10σ'
    s = '+' if p > 0.05 else '−' if p < -0.05 else ''
    t = f"{s}{abs(p):.1f}σ"
    return t + '*' if o['id'] in GAUSS_NOTE else t


def main():
    obs = {o['id']: o for o in json.load(open(OBS, encoding='utf-8'))['observables']}
    text = open(PM, encoding='utf-8').read()
    lines = text.split('\n')
    out = []
    n = 0
    for ln in lines:
        if ln.startswith('| A') and ln[3:5].isdigit() and ln[5] == ' ':
            cells = ln.split(' | ')
            i = cells[0][2:]
            o = obs[i]
            # cellules : 0 "| ID", 1 observable, 2 formule, 3 valeur K₇, 4 mesure, 5 dev, 6 pull, 7 statut |
            cells[4] = fmt_measured(o)
            cells[1] = LABEL.get(i, cells[1])
            cells[5] = fmt_dev(o)
            cells[6] = fmt_pull(o)
            if i in STATUS:
                cells[7] = STATUS[i] + ' |'
            ln = ' | '.join(cells)
            n += 1
        out.append(ln)
    assert n == 33, n
    new = '\n'.join(out)
    if '--counts' in sys.argv:
        for k, v in classify(obs).items():
            print(f'{k}: {len(v)} {v}')
        return
    if '--check' in sys.argv:
        sys.exit(0 if new == text else 1)
    open(PM, 'w', encoding='utf-8').write(new)
    print(f'{n} lignes régénérées')


if __name__ == '__main__':
    main()
