#!/usr/bin/env python3
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
"""
k7_v3_6_lee_null.py -- K7-V36-LEE : la P-value de K₇ (PM §8.4, « P < 5 × 10⁻⁶ ») survit-elle quand chaque concurrent
cherche ses PROPRES formules, dans la même grammaire, au même budget, avec la même liberté d'assignation et d'unité ?

Préinscription : canonical/notes/k7_v3_6_lee_null_prereg_2026_10_17.md (figée avant tout run).

Ce que le corpus a déjà tranché (R0, cité) : le Monte-Carlo publié (legacy/statistical_validation/validation_v33.py)
FIGE les formules de K₇ (piège de circularité, landscape_scan/DESIGN.md) ; le landscape scan
(coincidence_landscape_scan.py, D4/D6) fait la recherche aveugle pour (b₂, b₃) sur l'alphabet de Lie du Sieve et
les 28 cibles du Sieve. Ce lot reprend son moteur et sa garde anti-mirage (taille d'alphabet constante), mais avec
le vocabulaire de K₇ RE-DÉRIVÉ (H*, κ_T⁻¹, det(g) ; PM App. B), les 33 cibles de type I de K₇, la concordance
τ_z = 2σ du Sieve v1.1, et la liberté d'unité de δ_CP. Ce que j'écris de différent et pourquoi : la tolérance
relative uniforme du landscape devient 2σ expérimentaux, parce que la phrase publiée porte sur les écarts aux
mesures de K₇ et que τ_z = 2 est la règle gelée du Sieve.

Familles : K₇ (registre publié, = point (21, 77) de F-BETTI) ; F-BETTI (b₂ ∈ [1, 40], b₃ ∈ [17, 120], dérivations
publiées ; variante « fiche », hors règle) ; F-VOCAB (2 000 vocabulaires `fake_alphabet` du Sieve, 19 entiers, graine
20261017). Verdict : P_global = max(P_F-BETTI, P_F-VOCAB) sur S_cover ; LEE-GLOBALE si ≤ 0,01, sinon LEE-RETRAIT ;
REFUS-MOTEUR si G1 ou G2 rougit.

Rév. 1 (2026-10-22, revue externe de la v3.6) — voie : RERUN PLEIN, justifié par (i) le pin d'entrée
`observables.json` a changé (données PDG 2026 / NuFIT 6.1 / Planck 2018 une colonne, incertitudes ramenées à 1σ)
et (ii) le chemin numérique des fenêtres change : une fenêtre est désormais l'intervalle [x − τ_z σ₋, x + τ_z σ₊]
(erreurs asymétriques des deux côtés, au lieu du seul côté tourné vers K₇, qui biaisait la recherche des
concurrents vers la valeur de K₇), et une référence donnée par le PDG comme simple PLAGE (m_s/m_d, 17–22) a pour
fenêtre la plage elle-même. Amendement : `canonical/notes/k7_v3_6_lee_null_prereg_2026_10_17.md`, § Amendement 1.

Rév. 3 (2026-11-11) — voie : RERUN PLEIN, justifié par (i) le pin d'entrée `observables.json` a changé (fenêtre de A21,
m_W/m_Z, calculée depuis les masses publiées comme les autres rapports de masses). Aucun changement de code numérique.
Amendement 3 de la préinscription.

Usage : python3 canonical/scripts/k7_v3_6_lee_null.py [--limit N] [--workers W] [--no-variante]
        (--limit N : N premiers vocabulaires de chaque famille → k7_v3_6_lee_null_limited.json)
        SIEVE_DIR=<clone du Sieve>/scripts si le clone n'est pas à côté de private/.
"""
import argparse
import bisect
import hashlib
import json
import math
import multiprocessing as mp
import os
import random
import subprocess
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SIEVE = os.environ.get('SIEVE_DIR')
if not SIEVE:
    for _c in ('Sieve', 'sieve', 'arithmon-sieve'):
        # rév. 2 : racine des clones lue via git, valable aussi depuis un worktree (.wt/<agent>)
        _common = subprocess.run(['git', '-C', ROOT, 'rev-parse', '--path-format=absolute', '--git-common-dir'],
                                 capture_output=True, text=True).stdout.strip()
        _p = os.path.join(os.path.dirname(os.path.dirname(_common)), _c, 'scripts')
        if os.path.isdir(_p):
            SIEVE = os.path.abspath(_p)
            break
if not SIEVE or not os.path.isfile(os.path.join(SIEVE, 'coincidence_grammars.py')):
    sys.exit(f'clone du Sieve introuvable ({SIEVE}) : passer SIEVE_DIR=<clone>/scripts')
GRAMMAIRE_SHA = 'bcb03fe0c0b991f067d9ddcfea42adc0ed9404cf7d0ef516fdd4ab017251b133'   # figée au run rév. 1
with open(os.path.join(SIEVE, 'coincidence_grammars.py'), 'rb') as _f:
    if hashlib.sha256(_f.read()).hexdigest() != GRAMMAIRE_SHA:
        sys.exit('grammaire du Sieve différente de celle du run rév. 1 : vérifier le commit du clone')
sys.path.insert(0, SIEVE)
from coincidence_grammars import G_TRANS, G_STRUCT, Grammar, enumerate_lean, canon  # noqa: E402
from coincidence_fake_frameworks import fake_alphabet  # noqa: E402

PREREG = 'canonical/notes/k7_v3_6_lee_null_prereg_2026_10_17.md'
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
LANDSCAPE = os.path.join(ROOT, 'canonical', 'papers', 'landscape_scan', 'mapping', 'landscape_scan.json')
SIEVE_FREEZE = os.path.join(SIEVE, '..', 'freeze', 'observables_freeze_draft.json')
DEPTH = 5; TAU_Z = 2.0; SEED = 20261017; N_VOCAB = 2000; ALPHA = 0.01
B2 = (1, 40); B3 = (17, 120)
DCP_ID = 'A15'
# registre publié des 20 constantes (algebraic_montecarlo.py l. 51-71) : 19 entiers + φ (φ est déjà une feuille de G_TRANS)
K7 = {'b2': 21, 'b3': 77, 'dim_K7': 7, 'det_num': 65, 'det_den': 32, 'dim_G2': 14, 'p2': 2, 'dim_E8': 248,
      'rank_E8': 8, 'fund_E7': 56, 'dim_E6': 78, 'dim_F4': 52, 'dim_J3O': 27, 'N_gen': 3, 'Weyl': 5, 'D_bulk': 11,
      'H_star': 99, 'PSL27': 168, 'kappa_T_inv': 61}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def betti_vocab(b2, b3, variant='publiee'):
    v = dict(K7); v['b2'] = b2; v['b3'] = b3; v['H_star'] = b2 + b3 + 1
    if variant == 'publiee':                     # PM App. B (v3.5)
        v['kappa_T_inv'] = b3 - v['dim_G2'] - v['p2']
        v['det_den'] = b2 + v['dim_G2'] - v['N_gen']; v['det_num'] = v['p2'] * v['det_den'] + 1
    else:                                        # fiche privée (gift_cheatsheet) : hors règle
        v['kappa_T_inv'] = b3 - b2 + v['Weyl']
        alpha_sum = v['N_gen'] + v['rank_E8'] + v['p2']
        v['det_num'] = v['Weyl'] * alpha_sum; v['det_den'] = 2 ** v['Weyl']
    return v


def grammar_of(vocab):
    g = G_TRANS()
    leaves = dict(g.leaves)
    leaves.update({f'reg_{k}': float(x) for k, x in vocab.items()})
    return Grammar('G_LEE', leaves, unary=g.unary, binary=g.binary)


def load_targets():
    d = json.load(open(OBS, encoding='utf-8'))
    T = []
    for o in d['observables']:
        if o['type'] != 'I':
            continue
        if o.get('exp_range'):                    # rév. 1 : plage PDG sans incertitude → la plage elle-même
            lo, hi = map(float, o['exp_range'])
        else:                                     # rév. 1 : [x − τ σ₋, x + τ σ₊], erreurs asymétriques
            x = float(o['exp_value'])
            sm, sp = o.get('exp_error_asym') or (o['exp_error'], o['exp_error'])
            lo, hi = x - TAU_Z * float(sm), x + TAU_Z * float(sp)
        # une fenêtre (centre, demi-largeur / τ) : le test x − τs ≤ v ≤ x + τs redonne [lo, hi]
        win = [((lo + hi) / 2, (hi - lo) / (2 * TAU_Z))]
        if o['id'] == DCP_ID:                    # unités de δ_CP : degrés, radians, grades, tours
            c, s = win[0]
            win = [(c, s), (c * math.pi / 180, s * math.pi / 180), (c * 400 / 360, s * 400 / 360), (c / 360, s / 360)]
        T.append({'id': o['id'], 'symbol': o['symbol'], 'gift_value': float(o['gift_value']), 'windows': win})
    return T


def score(vocab, targets, penalty):
    snaps = enumerate_lean(grammar_of(vocab), DEPTH, checkpoints={DEPTH}, log=lambda s: None)
    vals, mdls = snaps[DEPTH]
    cover, cost, hit = 0, 0.0, {}
    for t in targets:
        best = None
        for x, s in t['windows']:
            i = bisect.bisect_left(vals, x - TAU_Z * s); j = bisect.bisect_right(vals, x + TAU_Z * s)
            if j > i:
                m = min(mdls[i:j])
                best = m if best is None else min(best, m)
        hit[t['id']] = best
        if best is not None:
            cover += 1; cost += best
        else:
            cost += penalty
    return cover, cost, hit, vals, mdls


_CTX = None


def _init(targets, penalty):
    global _CTX
    _CTX = (targets, penalty)


def _work(item):
    fam, key, vocab = item
    cover, cost, hit, _, _ = score(vocab, *_CTX)
    return {'famille': fam, 'cle': key, 'S_cover': cover, 'S_cost': cost,
            'atteintes': sorted(k for k, v in hit.items() if v is not None)}


def gate_g1():
    """moteur : rejouer la ligne (21, 77) de D4 (best_dev par observable, 28 cibles du Sieve). Recopie de
    `coincidence_landscape_scan.load_observables` / `scan_pair` (fenêtre la plus large τ = 10⁻²) : l'importer ré-enveloppe
    stdout et ferme le flux partagé."""
    d = json.load(open(SIEVE_FREEZE, encoding='utf-8')); entries = d['entries'] if isinstance(d, dict) else d
    obs = [(e['name'], float(e['value'])) for e in entries if float(e['value']) > 0]
    vals, _ = enumerate_lean(G_STRUCT(betti=(21, 77)), DEPTH, checkpoints={DEPTH}, log=lambda s: None)[DEPTH]
    bd = {}
    for name, x in obs:
        i = bisect.bisect_left(vals, x * (1 - 1e-2)); j = bisect.bisect_right(vals, x * (1 + 1e-2))
        bd[name] = min(abs(vals[k] - x) / x for k in range(i, j)) if j > i else None
    row = next(r for r in json.load(open(LANDSCAPE, encoding='utf-8'))['rows'] if r['b2'] == 21 and r['b3'] == 77)
    bad = [k for k, v in row['best_dev'].items()
           if (v is None) != (bd.get(k) is None) or (v is not None and abs(bd[k] - v) > 1e-9 * max(abs(v), 1e-300))]
    return {'n': len(row['best_dev']), 'desaccords': bad, 'ok': not bad and len(bd) == len(row['best_dev'])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--workers', type=int, default=max(1, (os.cpu_count() or 2) - 2))
    ap.add_argument('--no-variante', action='store_true')
    a = ap.parse_args()
    t0 = time.time()
    out_path = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_lee_null' + ('_limited' if a.limit else '') + '.json')
    out = {'lot': 'K7-V36-LEE', 'prereg': PREREG, 'mode': 'limited' if a.limit else 'full', 'limit': a.limit,
           'self_sha256': sha(os.path.abspath(__file__)), 'observables_sha256': sha(OBS),
           'grammaire_sha256': sha(os.path.join(SIEVE, 'coincidence_grammars.py')),
           'git_head': subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(),
           'sieve_head': subprocess.run(['git', '-C', SIEVE, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(),
           'depth': DEPTH, 'tau_z': TAU_Z, 'graine': SEED}
    targets = load_targets()
    out['n_cibles'] = len(targets)
    # ---- G1
    out['G1'] = gate_g1(); print(f"G1 moteur : {out['G1']}", flush=True)
    # ---- K₇ : recherche aveugle sur son registre ; pénalité ; G2 ; G3
    g0 = grammar_of(K7)
    snap0 = enumerate_lean(g0, DEPTH, checkpoints={DEPTH}, log=lambda s: None)
    penalty = max(snap0[DEPTH][1]) + g0.op_cost()
    c7, k7cost, hit7, vals7, _ = score(K7, targets, penalty)
    vset = set(vals7)
    g2 = []
    for t in targets:
        x, s = t['windows'][0]
        inset = canon(t['gift_value']) in vset; close = abs(t['gift_value'] - x) <= TAU_Z * s
        g2.append({'id': t['id'], 'valeur_publiee_dans_l_ensemble': inset, 'a_2_sigma': close,
                   'atteinte_aveugle': hit7[t['id']] is not None, 'ok': (not (inset and close)) or hit7[t['id']] is not None})
    out['G2'] = {'lignes': g2, 'ok': all(r['ok'] for r in g2),
                 'publiees_dans_l_ensemble': sum(r['valeur_publiee_dans_l_ensemble'] for r in g2)}
    out['G3_diagnostic_circulaire'] = {'formules_publiees_a_2_sigma': sum(r['a_2_sigma'] for r in g2),
                                       'note': 'formules choisies pour (21, 77) : diagnostic, jamais statistique'}
    out['K7'] = {'S_cover': c7, 'S_cost': k7cost, 'atteintes': sorted(k for k, v in hit7.items() if v is not None),
                 'penalite_mdl': penalty, 'n_valeurs': len(vals7)}
    # rév. 2 (amendement 2) : témoin sans constantes de K₇. Registre vide : seules restent les feuilles et opérations
    # universelles de G_TRANS. Distinct des formules publiées (G3) et de la recherche libre avec l'alphabet K₇ (S_cover).
    c0, cost0, hit0, vals0, _ = score({}, targets, penalty)
    out['temoin_sans_constantes'] = {'S_cover': c0, 'S_cost': cost0, 'n_valeurs': len(vals0),
                                     'atteintes': sorted(k for k, v in hit0.items() if v is not None),
                                     'manquantes': sorted(k for k, v in hit0.items() if v is None)}
    print(f"témoin sans constantes : S_cover {c0}/{len(targets)}, manquantes {out['temoin_sans_constantes']['manquantes']}", flush=True)
    print(f"K₇ : S_cover {c7}/{len(targets)}, S_cost {k7cost:.1f} ; G2 ok {out['G2']['ok']} ({time.time() - t0:.0f} s)", flush=True)
    if not (out['G1']['ok'] and out['G2']['ok']):
        out['verdict'] = 'REFUS-MOTEUR'
        json.dump(out, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); print(out['verdict']); return
    # ---- familles
    items = [('F-BETTI', [b2, b3], betti_vocab(b2, b3)) for b2 in range(B2[0], B2[1] + 1) for b3 in range(B3[0], B3[1] + 1)
             if (b2, b3) != (21, 77)]
    rng = random.Random(SEED); vv = []
    for _ in range(N_VOCAB):
        g = fake_alphabet(rng, n=19)
        vv.append(sorted(int(x) for k, x in g.leaves.items() if not k.isdigit()))
    items_v = [('F-VOCAB', n, dict(zip(K7.keys(), v))) for n, v in enumerate(vv)]
    items_f = [] if a.no_variante else [('F-BETTI-FICHE', [b2, b3], betti_vocab(b2, b3, 'fiche'))
                                        for b2 in range(B2[0], B2[1] + 1) for b3 in range(B3[0], B3[1] + 1)]
    if a.limit:
        items, items_v, items_f = items[:a.limit], items_v[:a.limit], items_f[:a.limit]
    todo = items + items_v + items_f
    print(f"{len(todo)} vocabulaires ({len(items)} F-BETTI, {len(items_v)} F-VOCAB, {len(items_f)} variante) ; {a.workers} workers", flush=True)
    rows = []
    with mp.Pool(a.workers, initializer=_init, initargs=(targets, penalty)) as pool:
        for n, r in enumerate(pool.imap_unordered(_work, todo, chunksize=4)):
            rows.append(r)
            if (n + 1) % 200 == 0:
                print(f"  {n + 1}/{len(todo)} ({time.time() - t0:.0f} s)", flush=True)
    rows.sort(key=lambda r: (r['famille'], json.dumps(r['cle'])))
    fam = {}
    for F in ('F-BETTI', 'F-VOCAB', 'F-BETTI-FICHE'):
        R = [r for r in rows if r['famille'] == F]
        if not R:
            continue
        ge = sum(r['S_cover'] >= c7 for r in R); le_cost = sum(r['S_cost'] <= k7cost for r in R)
        hist = {}
        for r in R:
            hist[r['S_cover']] = hist.get(r['S_cover'], 0) + 1
        fam[F] = {'n': len(R), 'n_ge_K7': ge, 'P': (1 + ge) / (1 + len(R)), 'percentile_K7': 100.0 * sum(r['S_cover'] < c7 for r in R) / len(R),
                  'P_cost_dual': (1 + le_cost) / (1 + len(R)), 'hist_S_cover': dict(sorted(hist.items())),
                  'max_S_cover': max(r['S_cover'] for r in R)}
    out['familles'] = fam
    out['frequence_atteinte_par_cible'] = {t['id']: sum(t['id'] in r['atteintes'] for r in rows if r['famille'] != 'F-BETTI-FICHE')
                                          for t in targets}
    pg = max(fam['F-BETTI']['P'], fam['F-VOCAB']['P'])
    out['P_global'] = pg
    out['verdict'] = 'LEE-GLOBALE' if pg <= ALPHA else 'LEE-RETRAIT'
    if a.limit:
        out['verdict'] += ' (limited : non lisible)'
    out['lignes'] = rows
    out['seconds'] = time.time() - t0
    json.dump(out, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"familles : { {k: {kk: v[kk] for kk in ('n', 'P', 'percentile_K7', 'max_S_cover')} for k, v in fam.items()} }")
    print(f"P_global {pg:.4g} ⟹ {out['verdict']} ({out['seconds']:.0f} s) → {out_path}")


if __name__ == '__main__':
    main()
