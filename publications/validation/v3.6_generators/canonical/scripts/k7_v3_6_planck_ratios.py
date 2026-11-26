#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
k7_v3_6_planck_ratios.py -- rapports cosmologiques de K₇ v3.6 calculés sur le posterior Planck 2018 lui-même.

Source : chaînes officielles base_plikHM_TTTEEE_lowl_lowE_lensing, burn-in retiré (burn_removed=T), archive PLA
COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip (miroir IRSA). L'archive n'est pas committée (65 Mo) : son sha
et son URL sont sérialisés, l'artefact JSON l'est.

Moyenne et écart-type pondérés de chaque rapport, sur tous les échantillons : ni propagation au premier ordre, ni matrice
de proposition. Motif : `k7_v3_6_exp_refresh.py` propageait ces rapports en négligeant les corrélations (revue Gemini B3,
réserves de Brieuc du 2026-11-03).

Gates : G1 chaîne ↔ margestats publié (écart < 1 % de σ sur la moyenne, sur σ < 1 %) ; G2 identité Ω_b/Ω_m + Ω_c/Ω_m +
Ω_ν/Ω_m = 1 sur chaque échantillon : le Ω_m de Planck contient les neutrinos, ce que 5/32 + 27/32 = 1 ne permet pas.
Publié aussi : dispersion entre les 4 chaînes, quantiles à 2σ, et la propagation négligeant les corrélations, pour comparaison.

Usage : python3 canonical/scripts/k7_v3_6_planck_ratios.py <répertoire contenant l'archive décompressée et le zip>
"""
import glob, hashlib, io, json, math, os, sys
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_planck_ratios.json')
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
URL = ('https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/'
       'COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip')
B = 'base_plikHM_TTTEEE_lowl_lowE_lensing'
RATIOS = {
    'A25': ('Ω_c h²/Ω_b h²', lambda p: p['omegach2'] / p['omegabh2']),
    'A26': ('Ω_c/Ω_Λ', lambda p: p['omegach2'] / (p['H0'] / 100) ** 2 / p['omegal']),
    'A27': ('Ω_Λ/Ω_m', lambda p: p['omegal'] / p['omegam']),
    'A29': ('Ω_b h²/Ω_m h²', lambda p: p['omegabh2'] / p['omegamh2']),
    'A30': ('Ω_c h²/Ω_m h²', lambda p: p['omegach2'] / p['omegamh2']),
    'A33': ('Ω_m/Ω_Λ', lambda p: p['omegam'] / p['omegal']),
}
NAMES = ('omegabh2', 'omegach2', 'H0', 'omegal', 'omegam', 'omegamh2', 'omeganuh2')


def wstat(x, w):
    m = np.average(x, weights=w)
    return float(m), float(math.sqrt(np.average((x - m) ** 2, weights=w)))


def wquant(x, w, qs):
    i = np.argsort(x)
    c = np.cumsum(w[i]) / w.sum()
    return [float(x[i][np.searchsorted(c, q)]) for q in qs]


def main():
    base = sys.argv[1]
    D = os.path.join(base, 'x', 'base', 'plikHM_TTTEEE_lowl_lowE_lensing')
    names = [l.split()[0].rstrip('*') for l in open(os.path.join(D, B + '.paramnames'), encoding='utf-8')]
    idx = {n: names.index(n) + 2 for n in NAMES}
    files = sorted(glob.glob(os.path.join(D, B + '_[0-9].txt')))
    assert len(files) == 4, files
    chains = [np.loadtxt(f) for f in files]
    A = np.vstack(chains)
    w = A[:, 0]
    P = {n: A[:, i] for n, i in idx.items()}
    pub = {l.split()[0].rstrip('*'): (float(l.split()[1]), float(l.split()[2]))
           for l in open(os.path.join(D, 'dist', B + '.margestats'), encoding='utf-8')
           if l.split() and l.split()[0].rstrip('*') in NAMES}
    g1 = {}
    for n in NAMES:
        if n not in pub:          # Ω_ν h² est fixé (Σm_ν = 0,06 eV) : absent de margestats
            continue
        m, s = wstat(P[n], w)
        g1[n] = {'chain': [m, s], 'margestats': pub[n], 'ok': abs(m - pub[n][0]) < 0.01 * s and abs(s / pub[n][1] - 1) < 0.01}
    assert all(v['ok'] for v in g1.values()), g1
    resid = np.abs((P['omegabh2'] + P['omegach2'] + P['omeganuh2']) / P['omegamh2'] - 1).max()
    assert resid < 1e-4, resid
    obs = {o['id']: o for o in json.load(open(OBS, encoding='utf-8'))['observables']}
    res = {}
    for i, (lab, f) in RATIOS.items():
        x = f(P)
        m, s = wstat(x, w)
        per = [wstat(f({n: c[:, idx[n]] for n in NAMES}), c[:, 0])[0] for c in chains]
        q = wquant(x, w, [0.02275, 0.5, 0.97725])
        g = float(obs[i]['gift_value'])
        res[i] = {'quantity': lab, 'mean': m, 'sd': s, 'q2sigma_low': q[0], 'median': q[1], 'q2sigma_high': q[2],
                  'chain_means_spread_over_sd': (max(per) - min(per)) / s,
                  'gift_value': g, 'pull': (g - m) / s, 'gift_inside_2sigma_quantiles': q[0] <= g <= q[2],
                  'previous': {'exp_value': obs[i]['exp_value'], 'exp_error': obs[i]['exp_error'],
                               'pull': (g - obs[i]['exp_value']) / obs[i]['exp_error']}}
    nu = P['omeganuh2'] / P['omegamh2']
    # Informatif, jamais la référence : le dénominateur Ω_b + Ω_c est une AUTRE quantité que le Ω_m de Planck (réserve de
    # Brieuc, 2026-11-03). Il mesure ce que la définition pèse dans le pull de A29 et A30, dont les formules somment à 1.
    gap = {}
    for i, num in (('A29', 'omegabh2'), ('A30', 'omegach2')):
        x = P[num] / (P['omegabh2'] + P['omegach2'])
        m, s = wstat(x, w)
        gap[i] = {'mean': m, 'sd': s, 'pull': (res[i]['gift_value'] - m) / s}
    z = open(glob.glob(os.path.join(base, '*.zip'))[0], 'rb').read()
    out = {'lot': 'K7-V36-PLANCK-RATIOS', 'source_url': URL, 'source_zip_sha256': hashlib.sha256(z).hexdigest(),
           'chains': B, 'n_rows': int(A.shape[0]), 'sum_weights': float(w.sum()),
           'self_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
           'G1_chain_vs_margestats': g1, 'G2_max_relative_residual_matter_budget': float(resid),
           'omega_nu_over_omega_m': dict(zip(('mean', 'sd'), wstat(nu, w))),
           'A29_plus_A30_mean': res['A29']['mean'] + res['A30']['mean'], 'ratios': res,
           'sans_neutrinos_informatif_pas_la_reference': gap}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for i, r in res.items():
        print(f"{i} {r['quantity']:<15} {r['mean']:.6f} ± {r['sd']:.6f}  K₇ {r['gift_value']:.6f} pull {r['pull']:+.2f}σ "
              f"(avant {r['previous']['exp_value']:.5f} ± {r['previous']['exp_error']:.5f}, {r['previous']['pull']:+.2f}σ) "
              f"2σ-quantiles {'dedans' if r['gift_inside_2sigma_quantiles'] else 'DEHORS'} ; dispersion/σ {r['chain_means_spread_over_sd']:.2f}")
    print('sans neutrinos (informatif)', gap)
    print('Ω_ν/Ω_m', out['omega_nu_over_omega_m'], 'somme A29+A30', out['A29_plus_A30_mean'], 'résidu G2', resid, 'n', A.shape[0])


if __name__ == '__main__':
    main()
