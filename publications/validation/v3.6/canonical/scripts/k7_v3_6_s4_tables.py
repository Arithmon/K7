#!/usr/bin/env python3
"""K₇ v3.6 — génère les tables du null de look-elsewhere dans S4 (supplement_sieve_diagnostics.md) DEPUIS les
artefacts du lot K7-V36-LEE (R6), et vérifie que les chiffres du §7.2 et du résumé de physics_main.md sont ceux des
artefacts (dériver, ne pas nommer : si le run changeait, --check rougirait).

Trois blocs, remplacés entre leurs marqueurs :
  <!-- BEGIN S4-LEE-FAMILIES --> … <!-- END S4-LEE-FAMILIES -->  une ligne par famille : couverture, P, coût
  <!-- BEGIN S4-LEE-TARGETS -->  … <!-- END S4-LEE-TARGETS -->   une ligne par cible : K₇, G2, fréquence d'atteinte
  <!-- BEGIN S4-LEE-HISTORY -->  … <!-- END S4-LEE-HISTORY -->   premier run (dataset v3.5), rév. 1, rév. 2

Sources : run rév. 2 `canonical/results/k7_v3_6_lee_null.json` ; closeout (égalités de coût, dette M1)
`canonical/results/k7_v3_6_lee_null_closeout.json` ; premier run et rév. 1 lus dans git aux commits FIRST_RUN et REV1 (jamais recopiés).

Usage : python3 canonical/scripts/k7_v3_6_s4_tables.py [--check]
"""
import io
import json
import os
import re
import subprocess
import sys

if (sys.stdout.encoding or '').lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RES = 'canonical/results/k7_v3_6_lee_null.json'
CLOSE = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_lee_null_closeout.json')
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
PM = os.path.join(ROOT, 'canonical', 'papers', 'framework', 'physics_main.md')
S4 = os.path.join(ROOT, 'canonical', 'papers', 'framework', 'supplement_sieve_diagnostics.md')
FIRST_RUN = 'aed0b9dd6'   # K7-V36-LEE, run du 2026-10-17 (dataset v3.5, fenêtres d'un seul côté)
REV1 = '065d9b2d4'        # K7-V36-LEE rév. 1, run du 2026-10-24 (dataset f0de1c05…, avant les chaînes Planck)
REV2 = '274c4a793'        # K7-V36-LEE rév. 2, run du 2026-11-03 (dataset dc772909…, avant la fenêtre de m_W/m_Z par les masses)
OUTCOME = {'LEE-RETRAIT': 'look-elsewhere effect not overcome', 'LEE-GLOBALE': 'look-elsewhere effect overcome'}
FAMS = [('F-BETTI', 'alternative Betti pairs (published derivations)'),
        ('F-VOCAB', 'invented vocabularies (generator of [M])'),
        ('F-BETTI-FICHE', 'alternative Betti pairs, variant derivations (outside the rule)')]


def n(x):
    """entier à séparateur de milliers espace (convention du main)."""
    return f'{x:,}'.replace(',', ' ')


def load():
    new = json.load(open(os.path.join(ROOT, RES), encoding='utf-8'))
    old = json.loads(subprocess.run(['git', 'show', f'{FIRST_RUN}:{RES}'], cwd=ROOT, capture_output=True,
                                    check=True).stdout)
    rev1 = json.loads(subprocess.run(['git', 'show', f'{REV1}:{RES}'], cwd=ROOT, capture_output=True,
                                     check=True).stdout)
    rev2 = json.loads(subprocess.run(['git', 'show', f'{REV2}:{RES}'], cwd=ROOT, capture_output=True,
                                     check=True).stdout)
    assert rev2['observables_sha256'].startswith('dc772909') and rev2['mode'] == 'full'
    close = json.load(open(CLOSE, encoding='utf-8'))
    assert new['mode'] == 'full' and old['mode'] == 'full' and rev1['mode'] == 'full'
    assert close['source_sha256'] == __import__('hashlib').sha256(open(os.path.join(ROOT, RES), 'rb').read()).hexdigest(), \
        'closeout périmé : rejouer k7_v3_6_lee_null_closeout.py'
    return new, old, rev1, rev2, close


def cost_range(res, fam):
    c = [r['S_cost'] for r in res['lignes'] if r['famille'] == fam]
    return min(c), max(c)


def at_most_cost(close, fam):
    f = close['familles'][fam]
    return f['strictement_moins_cher'] + f['egalites']


def families(new, close):
    k = new['K7']
    out = ['| Family | N | reach ≥ ' + f"{k['S_cover']}/33" + ' (as many as K₇) | P = (1 + n)/(1 + N) | best coverage | '
           'description cost, range (bits) | cost ≤ K₇ |',
           '|---|---:|---:|---:|---:|---:|---:|',
           f"| K₇ (21, 77), blind search on its own vocabulary | 1 | {k['S_cover']}/33 | n/a | {k['S_cover']} | {k['S_cost']:.1f} | n/a |"]
    for fam, label in FAMS:
        f = new['familles'][fam]; lo, hi = cost_range(new, fam)
        out.append(f"| {label} | {n(f['n'])} | {n(f['n_ge_K7'])} | {f['P']:.3f} | {f['max_S_cover']} | "
                   f"{lo:.1f} to {hi:.1f} | {n(at_most_cost(close, fam))} |")
    out.append('')
    out.append(f"Global p-value (the larger of the first two rows): **{new['P_global']:.3f}**; threshold 0.01; "
               f"preregistered outcome: **{OUTCOME[new['verdict']]}**. The variant row does not enter the verdict. \"Cost ≤ K₇\" counts "
               f"floating-point ties as ties (|ΔS_cost| ≤ {close['tolerance_bits']:g} bit; every tie is at the "
               f"same (length, operations) pair as K₇).")
    return '\n'.join(out)


def targets(new):
    ob = {o['id']: o for o in json.load(open(OBS, encoding='utf-8'))['observables'] if o.get('type') == 'I'}
    g2 = {x['id']: x for x in new['G2']['lignes']}
    reach = {fam: {} for fam, _ in FAMS[:2]}
    for r in new['lignes']:
        if r['famille'] in reach:
            for a in r['atteintes']:
                reach[r['famille']][a] = reach[r['famille']].get(a, 0) + 1
    nb, nv = new['familles']['F-BETTI']['n'], new['familles']['F-VOCAB']['n']
    yes = lambda b: 'yes' if b else 'no'  # noqa: E731
    out = ['| ID | Observable | K₇ reaches (blind) | published value in K₇\'s ≤ 5-node set | published value within window '
           f'| Betti pairs reaching (of {n(nb)}) | vocabularies reaching (of {n(nv)}) |',
           '|---|---|---|---|---|---:|---:|']
    for i in sorted(ob):
        out.append(f"| {i} | {ob[i]['symbol']} | {yes(i in new['K7']['atteintes'])} | "
                   f"{yes(g2[i]['valeur_publiee_dans_l_ensemble'])} | {yes(g2[i]['a_2_sigma'])} | "
                   f"{n(reach['F-BETTI'].get(i, 0))} | {n(reach['F-VOCAB'].get(i, 0))} |")
    return '\n'.join(out)


def history(new, rev2, rev1, old):
    runs = (old, rev1, rev2, new)
    sym = {o['id']: o['symbol'] for o in json.load(open(OBS, encoding='utf-8'))['observables']}
    rows = [('K₇ coverage', [f"{r['K7']['S_cover']}/33" for r in runs]),
            ('K₇ description cost (bits)', [f"{r['K7']['S_cost']:.1f}" for r in runs])]
    for fam, _ in FAMS:
        rows.append((f'{_}: reach as many as K₇',
                     [f"{n(r['familles'][fam]['n_ge_K7'])} of {n(r['familles'][fam]['n'])} (P = {r['familles'][fam]['P']:.3f})"
                      for r in runs]))
    rows.append(('global p-value, outcome', [f"{r['P_global']:.3f}, {OUTCOME[r['verdict']]}" for r in runs]))
    unr = lambda r: ', '.join(sym[k] for k in sorted(k for k, v in r['frequence_atteinte_par_cible'].items() if v == 0))  # noqa: E731
    rows.append(('targets reached by nobody', [unr(r) for r in runs]))
    out = ['| Quantity | first run (2026-10-17, dataset of v3.5, one-sided windows) | revision 1 (2026-10-24, refreshed dataset, '
           'two-sided windows) | revision 2 (2026-11-03, density ratios on the Planck chains) | revision 3 (2026-11-11, current dataset: '
           'm_W/m_Z from the published masses) |', '|---|---|---|---|---|']
    out += [f'| {a} | {c[0]} | {c[1]} | {c[2]} | {c[3]} |' for a, c in rows]
    return '\n'.join(out)


def s4_claims(new):
    """phrases de S4 hors des blocs générés qui portent un chiffre du lot."""
    t = new['temoin_sans_constantes']; ob = {o['id']: o['symbol'] for o in json.load(open(OBS, encoding='utf-8'))['observables']}
    assert t['manquantes'] == ['A04', 'A06', 'A07'] and [ob[i] for i in t['manquantes']] == ['α⁻¹(0)', 'm_τ/m_e', 'm_μ/m_e']
    g2 = new['G2']['lignes']; pub = sum(x['valeur_publiee_dans_l_ensemble'] for x in g2)
    h = round(new['seconds'] / 60)
    assert all(x['atteinte_aveugle'] for x in g2 if x['valeur_publiee_dans_l_ensemble'] and x['a_2_sigma'])
    return [f"they reach {t['S_cover']} of the 33 targets, all but α⁻¹, m_τ/m_e and m_μ/m_e",
            f"the second check finds {pub} of K₇'s 33 published values",
            f"{new['G3_diagnostic_circulaire']['formules_publiees_a_2_sigma']} of the 33 published formulas lie within their windows",
            f"Sieve engine at commit `{new['sieve_head'][:7]}`",
            f"{h // 60} h {h % 60:02d} on three processes"]


def main_claims(new, old, close):
    """phrases du main qui portent un chiffre du lot : chacune doit s'y trouver telle quelle."""
    fb, fv = new['familles']['F-BETTI'], new['familles']['F-VOCAB']
    blo, bhi = cost_range(new, 'F-BETTI'); vlo, vhi = cost_range(new, 'F-VOCAB')
    ob = {o['id']: o['symbol'] for o in json.load(open(OBS, encoding='utf-8'))['observables']}
    nobody = sorted(k for k, v in new['frequence_atteinte_par_cible'].items() if v == 0)
    assert [ob[i] for i in nobody] == ['α⁻¹(0)', 'm_μ/m_e'], nobody   # la prose les nomme « α⁻¹ and m_μ/m_e »
    freq = new['frequence_atteinte_par_cible']          # F-BETTI + F-VOCAB (6 159), variante exclue
    allr = [i for i in new['K7']['atteintes'] if freq[i] == fb['n'] + fv['n']]
    sep = [i for i in new['K7']['atteintes'] if i not in allr]
    assert len(sep) == 1, sep                            # la prose parle d'UNE cible qui départage
    assert old["familles"]["F-BETTI"]["n_ge_K7"] == old["familles"]["F-BETTI"]["n"]   # « every alternative Betti pair »
    return [f"K₇ reaches {new['K7']['S_cover']} of the 33 targets",
            f"**{n(fb['n_ge_K7'])} of the {n(fb['n'])} alternative Betti pairs reach as many** (P = {fb['P']:.2f},",
            f"**{n(fv['n_ge_K7'])} of the {n(fv['n'])} invented vocabularies reach as many** (P = {fv['P']:.2f})",
            f"No competitor reaches more than {max(fb['max_S_cover'], fv['max_S_cover'])}.",
            f"its description cost ({new['K7']['S_cost']:.1f} bits)",
            f"({blo:.1f} to {bhi:.1f} bits for the Betti pairs, {vlo:.1f} to {vhi:.1f} for the vocabularies)",
            f"{n(at_most_cost(close, 'F-BETTI'))} of the Betti pairs and {n(at_most_cost(close, 'F-VOCAB'))} of the "
            f"vocabularies cost at most as much",
            f"the larger of the two family p-values, {new['P_global']:.2f}, against a threshold of 0.01",
            f"had found K₇ at {old['K7']['S_cover']} of 33 and every alternative Betti pair at as many",
            f"A control with no constant of K₇ reaches {new['temoin_sans_constantes']['S_cover']} of the 33",
            "two targets reached by no vocabulary at this budget are α⁻¹ and m_μ/m_e",
            f"Of the {new['K7']['S_cover']} targets K₇ reaches, {len(allr)} are reached by every competitor; the "
            f"{new['K7']['S_cover']}st, {ob[sep[0]]}, alone separates the vocabularies"]


def main():
    check = '--check' in sys.argv
    new, old, rev1, rev2, close = load()
    blocks = {'S4-LEE-FAMILIES': families(new, close), 'S4-LEE-TARGETS': targets(new),
              'S4-LEE-HISTORY': history(new, rev2, rev1, old)}
    s = open(S4, encoding='utf-8').read(); t = s
    for k, body in blocks.items():
        pat = re.compile(rf'(<!-- BEGIN {k} -->\n).*?(<!-- END {k} -->)', re.S)
        assert pat.search(t), f'marqueur {k} absent de S4'
        t = pat.sub(lambda m: m.group(1) + body + '\n' + m.group(2), t)
    pm = open(PM, encoding='utf-8').read()
    missing = [c for c in main_claims(new, old, close) if c not in pm]
    for c in missing:
        print('MAIN ≠ ARTEFACT :', c)
    missing4 = [c for c in s4_claims(new) if c not in t]
    for c in missing4:
        print('S4 ≠ ARTEFACT :', c)
    missing += missing4
    if check:
        stale = t != s
        print('S4 :', 'PÉRIMÉ' if stale else 'à jour', '; main :', f'{len(missing)} phrase(s) absente(s)' if missing else 'conforme')
        sys.exit(1 if stale or missing else 0)
    open(S4, 'w', encoding='utf-8').write(t)
    print('S4 écrit ;', 'main conforme' if not missing else f'main : {len(missing)} phrase(s) absente(s)')
    sys.exit(1 if missing else 0)


if __name__ == '__main__':
    main()
