#!/usr/bin/env python3
"""K₇ v3.6 — rafraîchissement des valeurs expérimentales de observables.json (2026-10-22).

Autorisé par Brieuc le 2026-10-22 (« autant se baser sur les mesures les plus récentes »).

Ce que le script fait : pour les 33 entrées de type I, et pour les entrées de types II/III qui
comparent à une masse ou à un rapport de leptons, il remplace exp_value / exp_error / exp_source
par des valeurs DÉRIVÉES ici des sources primaires ci-dessous (rapports calculés depuis les masses,
erreurs propagées), recalcule deviation_pct, et date chaque changement dans `notes`.
Il n'écrit JAMAIS gift_value ni gift_fraction (les prédictions ne bougent pas).

Sources (lues le 2026-10-22) :
- PDG 2026 : F. Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026). Tables résumées
  (leptons, bosons, quarks), Table 1.1 (constantes), revue 12 (CKM, éq. 12.26-12.28),
  revue 60 (masses des quarks, moyenne réseau de m_c/m_s).
- CODATA 2022 (via PDG 2026 Table 1.1) : α, m_e ; m_μ/m_e = 206.7682827(46).
- NuFIT 6.1 (données de novembre 2025), ordre normal, variante IC24 + SK-atm (« TByes »). Le site
  nu-fit.org refusait la connexion le 22-10 ; valeurs prises dans deux articles indépendants qui
  citent la publication officielle : arXiv:2608.19691 (éq. 49-52, avec erreurs) et
  arXiv:2608.18812 (table 1, valeurs centrales identiques). Recoupé le 2026-11-03 sur la table officielle (Wayback, capture 20260912055217).
- Planck 2018 VI (arXiv:1807.06209), table 2, colonne de référence TT,TE,EE+lowE+lensing.
  UNE seule colonne pour toutes les entrées cosmologiques (R7) ; l'ancien h = 0.6764 ne
  correspondait à aucune colonne.

Conventions :
- Erreur asymétrique : exp_error = l'erreur du côté de la valeur K₇ (convention du pull) ;
  les deux côtés sont gardés dans exp_error_asym = [moins, plus].
- Rapports : propagation des erreurs EN NÉGLIGEANT LES CORRÉLATIONS (approximation, pas un
  majorant : le signe de la covariance compte ; les tables résumées ne la publient pas), sauf
  Ω_Λ/Ω_m et Ω_m/Ω_Λ (platitude Ω_Λ = 1 − Ω_m, neutrinos négligés).
- Niveau de confiance (rév. 1, revue externe du 2026-10-22) : les entrées du résumé PDG des quarks
  sont étiquetées « CL = 90 % » ; elles sont ramenées à 1σ par σ = e/1,645 (CL90). La moyenne
  réseau de m_c/m_s (revue 60) est déjà à 1σ (stat ⊕ syst).
- m_s/m_d : le PDG ne donne qu'une PLAGE (17–22) ; elle est stockée telle quelle (exp_range),
  sans erreur ni pull (exp_error = None).
"""
import io
import json
import math
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
OUT = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_exp_refresh.json')
DATE = '2026-10-22'
# état « avant » : le dataset tel qu'il était avant le premier rafraîchissement (commit b147fa7d3),
# lu dans git, pour que le journal reste juste quand le script est relancé (idempotence).
BASE = 'b147fa7d3^'

PDG = 'PDG 2026'
NUFIT = 'NuFIT 6.1 (IC24+SK-atm, NO)'
PLANCK = 'Planck 2018 (TT,TE,EE+lowE+lensing)'

CL90 = 1.6448536269514722   # demi-largeur d'un intervalle gaussien à 90 % en unités de σ

# --- entrées primaires ---------------------------------------------------------------
me, s_me = 0.51099895069, 0.00000000016          # MeV
mmu, s_mmu = 105.6583755, 0.0000023              # MeV
mtau, s_mtau = 1776.93, 0.09                     # MeV
mu_e_codata, s_mu_e_codata = 206.7682827, 0.0000046
mW, s_mW = 80.3625, 0.0077                       # GeV
mZ, s_mZ = 91.1879, 0.0020
mH, s_mH = 125.13, 0.11
mt, s_mt = 172.60, 0.27                          # direct
mb, s_mb = 4.186, 0.006 / CL90                   # MSbar m_b(m_b), CL 90 % → 1σ
GF = 1.1663785e-5                                # GeV^-2
WZ_ratio, s_WZ = 0.88136, 0.00015                # PDG résumé
obh2, s_obh2 = 0.02237, 0.00015
och2, s_och2 = 0.1200, 0.0012
omh2, s_omh2 = 0.1430, 0.0011
H0, s_H0 = 67.36, 0.54
OL, s_OL = 0.6847, 0.0073
Om = 0.3153


def ratio(a, sa, b, sb):
    r = a / b
    return r, abs(r) * math.hypot(sa / a, sb / b)


def koide(t):
    return (me + mmu + t) / (math.sqrt(me) + math.sqrt(mmu) + math.sqrt(t)) ** 2


h = H0 / 100
s_h = s_H0 / 100
v = (math.sqrt(2) * GF) ** -0.5
Q = koide(mtau)
s_Q = math.hypot(abs(koide(mtau + s_mtau) - Q),
                 abs((me + mmu + s_mmu + mtau) / (math.sqrt(me) + math.sqrt(mmu + s_mmu)
                                                   + math.sqrt(mtau)) ** 2 - Q))
oc = och2 / h ** 2
s_oc = oc * math.hypot(s_och2 / och2, 2 * s_h / h)

# id -> (valeur, erreur ou (moins, plus), source, note, nouveau symbole éventuel)
NEW = {
    'A01': (0.23122, 0.00006, PDG, 'MS-bar at M_Z (PDG Table 1.1)'),
    'A02': (0.1180, 0.0009, PDG, ''),
    'A03': (mH ** 2 / (2 * v ** 2), 2 * mH ** 2 / (2 * v ** 2) * s_mH / mH, PDG,
            f'tree level m_H²/(2v²), v = (√2 G_F)^(−1/2) = {v:.3f} GeV; error from m_H only; '
            'the definition is a scheme choice'),
    'A04': (137.035999177, 0.000000021, 'CODATA 2022', 'α⁻¹ at q² = 0'),
    'A05': (Q, s_Q, PDG, 'computed from the PDG 2026 masses; error dominated by m_τ'),
    'A06': ratio(mtau, s_mtau, me, s_me) + (PDG, 'from the PDG 2026 masses'),
    'A07': (mu_e_codata, s_mu_e_codata, 'CODATA 2022', ''),
    'A08': (19.5, None, PDG, 'PDG gives the range 17–22, not a measurement with an uncertainty; '
            'no pull is defined'),
    'A09': (11.769, 0.035, PDG, 'lattice average (N_f = 2+1+1), PDG quark-mass review; scale independent'),
    'A10': ratio(mb, s_mb, mt, s_mt) + (PDG, 'm_b at 90% CL converted to 1σ; mixed schemes: m_b in MS-bar at m_b over the directly measured m_t; '
                                          'the ratio has no scheme-independent meaning'),
    'A11': (0.462, 0.020 / CL90, PDG, 'MS-bar at 2 GeV; PDG ±0.020 at 90% CL, converted to 1σ'),
    'A12': (0.3088, (0.0066, 0.0067), NUFIT, ''),
    'A13': (0.470, (0.014, 0.017), NUFIT, '3σ range 41.27°–49.86°, i.e. sin² 0.435–0.584, contains 6/11; '
            'non-Gaussian profile (second-octant branch): the Gaussian pull overstates the tension'),
    'A14': (0.02248, (0.00059, 0.00055), NUFIT, ''),
    'A15': (212.0, (36.0, 26.0), NUFIT, 'degrees; 3σ range 125°–365°'),
    'A16': (0.22517, 0.00068, PDG, 'PDG CKM review: sin θ₁₂ = λ (not squared)',
            'sin θ₁₂ᶜᴷᴹ'),
    'A17': (0.826, (0.015, 0.017), PDG, 'PDG CKM review, Wolfenstein fit'),
    'A18': (0.04189, (0.00069, 0.00081), PDG, 'PDG CKM review: sin θ₂₃ = Aλ² (not squared)',
            'sin θ₂₃ᶜᴷᴹ'),
    'A19': ratio(mH, s_mH, mt, s_mt) + (PDG, 'm_t from direct measurements'),
    'A20': ratio(mH, s_mH, mW, s_mW) + (PDG, ''),
    # 2026-11-11 (Brieuc) : la règle des rapports de masses s'applique aussi à A21 ; la ligne de rapport du résumé PDG
    # (WZ_ratio, 0,88136(15)) n'est plus utilisée.
    'A21': ratio(mW, s_mW, mZ, s_mZ) + (PDG, 'from the PDG 2026 masses'),
    'A22': ratio(mmu, s_mmu, mtau, s_mtau) + (PDG, 'from the PDG 2026 masses'),
    'A23': (OL, s_OL, PLANCK, 'Ω_Λ'),
    'A24': (0.9649, 0.0042, PLANCK, ''),
    # A25, A26, A27, A29, A30, A33 : remplacés depuis le 2026-11-03 par les chaînes (k7_v3_6_planck_ratios.py, appliqué
    # par k7_v3_6_dataset_labels.py) : la propagation ci-dessous néglige les corrélations.
    'A25': ratio(och2, s_och2, obh2, s_obh2) + (PLANCK, 'Ω_c h² / Ω_b h²'),
    'A26': ratio(oc, s_oc, OL, s_OL) + (PLANCK, 'Ω_c = Ω_c h² / h²'),
    'A27': (OL / Om, s_OL / Om ** 2, PLANCK, 'flatness: Ω_Λ = 1 − Ω_m, neutrinos neglected'),
    'A28': (h, s_h, PLANCK, ''),
    'A29': ratio(obh2, s_obh2, omh2, s_omh2) + (PLANCK, 'Ω_b h² / Ω_m h²'),
    'A30': ratio(och2, s_och2, omh2, s_omh2) + (PLANCK, 'Ω_c h² / Ω_m h²'),
    'A31': (0.8111, 0.0060, PLANCK, ''),
    'A33': (Om / OL, s_OL / OL ** 2, PLANCK, 'flatness: Ω_Λ = 1 − Ω_m, neutrinos neglected'),
    # type II : masses directes du résumé PDG 2026 (MeV / GeV comme le dataset)
    'B01': (2.16, 0.07 / CL90, PDG, 'MeV, MS-bar 2 GeV; 90% CL converted to 1σ'),
    'B02': (4.70, 0.07 / CL90, PDG, 'MeV, MS-bar 2 GeV; 90% CL converted to 1σ'),
    'B03': (92.9, 0.7 / CL90, PDG, 'MeV, MS-bar 2 GeV; 90% CL converted to 1σ'),
    'B04': (1272.9, 4.5 / CL90, PDG, 'MeV, MS-bar m_c(m_c); 90% CL converted to 1σ'),
    'B05': (4186.0, 6.0 / CL90, PDG, 'MeV, MS-bar m_b(m_b); 90% CL converted to 1σ'),
    'B06': (172600.0, 270.0, PDG, 'MeV, direct'),
    'B07': (v, 0.0, PDG, 'GeV, from G_F'),
    'B08': (mW, s_mW, PDG, 'GeV'),
    'B09': (mZ, s_mZ, PDG, 'GeV'),
    # type III : seulement les références leptoniques (même source que A05-A07, A22)
    'C01': ratio(mtau, s_mtau, me, s_me) + (PDG, ''),
    'C02': ratio(mtau, s_mtau, mmu, s_mmu) + (PDG, ''),
    'C04': (0.23122, 0.00006, PDG, ''),
    'C19': ratio(mtau, s_mtau, me, s_me) + (PDG, ''),
    'C20': ratio(mtau, s_mtau, mmu, s_mmu) + (PDG, ''),
    'C21': (mu_e_codata, s_mu_e_codata, 'CODATA 2022', ''),
}

# Hors périmètre, déclaré : A32 (Y_p, 0.245(3), observationnel, non revérifié), B10-B19
# (|V_ij| et rapports à échelles mélangées du type II), C05-C18 sans référence leptonique.
NOT_REFRESHED = ['A32', 'B10-B19', 'C05', 'C06', 'C07', 'C09', 'C13', 'C14', 'C17', 'C18']

FORMULA_FIX = {'A14': 'D_bulk/dim(E₈×E₈)'}   # la valeur était déjà 11/496


def main():
    d = json.load(open(OBS, encoding='utf-8'))
    base = {o['id']: o for o in json.loads(subprocess.run(
        ['git', 'show', f'{BASE}:canonical/data/observables.json'], cwd=ROOT, capture_output=True,
        check=True, text=True).stdout)['observables']}
    log = []
    for o in d['observables']:
        if o['id'] not in NEW:
            continue
        spec = NEW[o['id']]
        val, err, src, note = spec[:4]
        before = {k: base[o['id']].get(k) for k in ('symbol', 'exp_value', 'exp_error', 'exp_source', 'deviation_pct')}
        g = o['gift_value']
        if o['id'] == 'A08':
            o['exp_range'] = [17, 22]
        if isinstance(err, tuple):
            lo, hi = err
            o['exp_error_asym'] = [lo, hi]
            err = hi if g > val else lo
        else:
            o.pop('exp_error_asym', None)
        o['exp_value'] = val
        o['exp_error'] = err
        o['exp_source'] = src
        o['deviation_pct'] = round((g - val) / val * 100, 6)
        if len(spec) > 4:
            o['symbol'] = spec[4]
        if o['id'] in FORMULA_FIX:
            o['gift_formula'] = FORMULA_FIX[o['id']]
        stamp = f'[{DATE}] exp refreshed to {src}' + (f': {note}' if note else '')
        old = o.get('notes', '') or ''
        old = '; '.join(p for p in old.split('; ') if not p.startswith(f'[{DATE}] exp refreshed'))
        o['notes'] = (old + '; ' if old else '') + stamp
        pull = (g - val) / err if err else None
        log.append({'id': o['id'], 'type': o['type'], 'before': before,
                    'after': {'symbol': o['symbol'], 'exp_value': val, 'exp_error': err,
                              'exp_error_asym': o.get('exp_error_asym'), 'exp_source': src,
                              'deviation_pct': o['deviation_pct']},
                    'pull_after': pull})

    t1 = [o for o in d['observables'] if o['type'] == 'I']
    d['summary']['by_type']['I']['mean_abs_deviation_pct'] = round(
        sum(abs(o['deviation_pct']) for o in t1) / len(t1), 4)
    d['metadata']['experimental_sources'] = ['PDG 2026', 'NuFIT 6.1 (2025, IC24+SK-atm)',
                                             'Planck 2018 (TT,TE,EE+lowE+lensing)', 'CODATA 2022']
    d['metadata']['exp_refresh'] = {'date': DATE, 'script': 'canonical/scripts/k7_v3_6_exp_refresh.py',
                                    'log': 'canonical/results/k7_v3_6_exp_refresh.json'}
    with open(OBS, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)   # sans saut final, comme l'original

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from k7_v3_6_table_sec4 import classify   # une seule définition des classes (statuts du §4.1)
    classes = classify({o['id']: o for o in t1})
    out = {'date': DATE, 'self': 'canonical/scripts/k7_v3_6_exp_refresh.py',
           'sources': __doc__.split('Sources (lues le 2026-10-22) :')[1].split('Conventions')[0].strip(),
           'not_refreshed': NOT_REFRESHED,
           'type_I_classes': classes,
           'type_I_mean_abs_deviation_pct': d['summary']['by_type']['I']['mean_abs_deviation_pct'],
           'entries': log}
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write('\n')
    for r in log:
        if r['type'] == 'I':
            b = r['before']
            e = r['after']['exp_error']
            pl = r['pull_after']
            print(f"{r['id']:4} {r['after']['symbol']:14} exp {b['exp_value']}±{b['exp_error']} -> "
                  f"{r['after']['exp_value']:.6g}±{e if e is None else f'{e:.2g}'}  "
                  f"pull {'n/a' if pl is None else f'{pl:+.2f}'}")
    for k, v in classes.items():
        print(f'{k}: {len(v)} {v}')
    print('mean |dev| %:', out['type_I_mean_abs_deviation_pct'])


if __name__ == '__main__':
    main()
