#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
k7_v3_6_dataset_labels.py -- passe de libellés de observables.json pour la 3.6 (accord de Brieuc, 2026-11-03).

Le gate `numeric_fields` compare chaque champ numérique au commit PIN_COMMIT, celui du run LEE rév. 1 (f0de1c05…). Seule
exception, depuis le 2026-11-03 : les six rapports recalculés sur les chaînes Planck (k7_v3_6_planck_ratios.py). Ce pin
d'entrée changé justifie le run LEE rév. 2 (CLAUDE.md, « pool ou pas pool ») ; amendement 2 de sa préinscription.

Corrige : titre et version, bloc lean_build (dérivé de K7-Lean au commit de lean_map), DOI des papiers (concepts,
dérivés de dois.json), `lean_theorem` des 33 relations (dérivé de lean_map), B07, libellé « S10 » de C19–C21, C14 (nom, symbole, formule), notes
A04, A08, C17, C18, C20, C21, D22, résumé recalculé avec la formule de observable_dataset.py. Régénère les dérivés.

C18 : le libellé est juste (Vol_e − Vol_μ) mais la référence est ln(m_τ/m_μ), que la relation d'instanton apparie à
Vol_μ − Vol_τ. Sources : legacy/notebooks/run_associative_volumes.py l. 13-14 et 423, K7-Lean
GIFT/Hierarchy/AssociativeVolumes.lean l. 85. C'est une valeur : décision à Brieuc, seule la note est écrite ici.

observable_dataset.py ne tourne plus (ses entrées sont absentes) : ses exporteurs sont repris par extraction ast.

Usage : python3 canonical/scripts/k7_v3_6_dataset_labels.py [--check]
"""
import ast, csv, io, json, math, os, re, subprocess, sys
from types import SimpleNamespace

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
CSV_OUT = os.path.join(ROOT, 'canonical', 'data', 'observables.csv')
LEAN_MAP = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_lean_map.json')
DOIS = os.path.join(ROOT, 'canonical', 'data', 'dois.json')
_COMMON = subprocess.run(['git', '-C', ROOT, 'rev-parse', '--path-format=absolute', '--git-common-dir'],
                         capture_output=True, text=True, check=True).stdout.strip()
LEAN = os.environ.get('LEAN_DIR') or os.path.join(os.path.dirname(os.path.dirname(_COMMON)), 'K7-Lean')
PLANCK = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_planck_ratios.json')
PIN_COMMIT = '1e3bc4828'
DATE = '2026-11-11'
NUMERIC = ('gift_value', 'exp_value', 'exp_error', 'exp_error_asym', 'exp_range', 'deviation_pct', 'type', 'id')
# Titres relus sur l'API Zenodo le 2026-11-03 (dernière version de chaque concept) ; dois.json garde des libellés.
PAPERS = {'A': ('g2_metric_certified_torsion_free', 'A Certified Torsion-Free G₂ Structure on a TCS Neck Model via Computer-Assisted Proof'),
          'B': ('g2_spectral_geometry', 'Spectral Geometry of an Explicit G₂ Metric: Laplacian Spectrum and Harmonic Forms'),
          'C': ('k3_donaldson_embedding', 'Newton–Kantorovich diagnostics on a Donaldson K3 metric: two β estimates, machine-checked inequalities')}
# Le Ω_m de Planck contient les neutrinos (Σm_ν = 0,06 eV) : voir k7_v3_6_planck_ratios.py.
PLANCK_NOTE = {'A25': 'Ω_c h² / Ω_b h²', 'A26': 'Ω_c h² / h² / Ω_Λ', 'A27': 'Ω_Λ / Ω_m, Planck definitions',
               'A29': 'Ω_b h² / Ω_m h², Ω_m includes neutrinos', 'A30': 'Ω_c h² / Ω_m h², Ω_m includes neutrinos',
               'A33': 'Ω_m / Ω_Λ, Planck definitions'}
RECOMPUTED = tuple(PLANCK_NOTE)
COMB = 'Wilson-line ratio × exp(e^K · ΔV)'
MISPAIR = ('[2026-11-03] Value is Vol_e − Vol_μ = 3.271; reference is ln(m_τ/m_μ), which the instanton relation '
           'pairs with Vol_μ − Vol_τ = 5.362, so the 15.9% deviation is not meaningful; ln(m_μ/m_e) = 5.33 is the '
           'matching reference. Recorded as computed; targets from PDG 2025 central values')
INHERIT = '[2026-11-03] Computed with Vol_e − Vol_μ, the mismatched difference of C18'


def git(*a):
    r = subprocess.run(['git', *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f'git {" ".join(a)} : {r.stderr.strip()} (clone de K7-Lean ailleurs ? passer LEAN_DIR)')
    return r.stdout


def lean_counts(commit):
    files = [f for f in git('-C', LEAN, 'ls-tree', '-r', '--name-only', commit).split() if f.endswith('.lean')]
    ax = {}
    for line in git('-C', LEAN, 'grep', '-cE', r'^\s*(private |protected )?axiom ', commit, '--', '*.lean').split():
        _, path, n = line.split(':')
        ax[path] = int(n)
    assert ax.pop('GIFT/Foundations/IntervalCertificates.lean') == 10
    return len(files), sum(ax.values()), 10


def apply(d):
    m = json.load(open(LEAN_MAP, encoding='utf-8'))
    n_files, n_lit, n_cert = lean_counts(m['commit'])
    assert (n_lit, n_cert) == (4, 10), (n_lit, n_cert)
    reg = {e['key']: e for e in json.load(open(DOIS, encoding='utf-8'))['deposits']}
    md = d['metadata']
    md['title'] = 'K₇ Dictionary Observable Dataset (formerly GIFT): Source of Truth'
    md['version'] = '3.6'
    md['generator'] = 'observable_dataset.py (v3.4), then k7_v3_6_exp_refresh.py and k7_v3_6_dataset_labels.py'
    md['lean_build'] = {
        'repo': m['lean_repo'], 'commit': m['commit'], 'merged': m['merged'], 'aggregate': m['aggregate'],
        'n_files': n_files, 'n_sorry': 0, 'n_axioms_main_chain': n_lit, 'n_axioms_interval_certificates': n_cert,
        'note': f'{n_lit + n_cert} axioms beyond Mathlib: {n_lit} literature imports and {n_cert} interval '
                'certificates; the aggregate depends only on ' + ', '.join(m['axioms']),
    }
    md['papers'] = {k: f"Zenodo {reg[v[0]]['concept']} (concept DOI): {v[1]}" for k, v in PAPERS.items()}
    md['label_pass'] = {'date': DATE, 'script': 'canonical/scripts/k7_v3_6_dataset_labels.py', 'values_changed': 'exp_value, exp_error, deviation_pct of ' + ', '.join(RECOMPUTED) + ' (Planck chains) and of A21 (mass-ratio rule, 2026-11-11); gift_value and deviation_pct of B01, B04 (formula value in place of a rounded one, 2026-11-11)',
                        'numeric_fields_compared_with': PIN_COMMIT}
    obs = {o['id']: o for o in d['observables']}
    for r in m['relations']:
        obs[r['id']]['lean_theorem'] = r['lean_declaration'] or ''
    obs['D04']['lean_theorem'] = ''
    planck = json.load(open(PLANCK, encoding='utf-8'))['ratios']
    for i, r in planck.items():
        o = obs[i]
        o['exp_value'], o['exp_error'] = r['mean'], r['sd']
        o['deviation_pct'] = round((o['gift_value'] - r['mean']) / r['mean'] * 100, 6)
        o['notes'] = f"[2026-11-03] exp recomputed on the Planck 2018 chains: {PLANCK_NOTE[i]}"
    obs['C14']['name'] = 'Self-dual Yukawa count'
    obs['C14']['symbol'] = 'n_SD'
    obs['C14']['gift_formula'] = 'Count of positive eigenvalues of the K3 intersection form'
    obs['C14']['notes'] = ('[2026-11-03] The producer key yukawa_rank holds this count; the matrix rank it records is 22; earlier '
                           'label "Mass matrix SVD" withdrawn')
    obs['B07']['gift_formula'] = 'Scale bridge from the unit assignment (R10)'
    for i in ('C19', 'C20', 'C21'):
        obs[i]['gift_formula'] = COMB
    obs['A08']['notes'] = ('[2026-10-22] exp refreshed to PDG 2026: PDG gives the range 17–22, not a measurement '
                           'with an uncertainty; no pull is defined')
    obs['C17']['notes'] = '[2026-11-03] Target ln(3477.0), from a PDG 2025 central value'
    obs['C18']['notes'] = MISPAIR
    obs['C20']['notes'] = 'α = e^K (geometric); [2026-10-22] exp refreshed to PDG 2026; ' + INHERIT
    obs['C21']['notes'] = ('α = e^K (geometric); [2026-10-22] exp refreshed to CODATA 2022; [2026-11-03] Ratio C19/C20, '
                           'so it inherits the mismatched difference of C18')
    obs['A04']['notes'] = ('[2026-10-02] Identity corrected: the compared observable is α⁻¹ at low energy (Thomson limit, '
                           'α(0)), not α⁻¹(M_Z), about 127.93 in MS-bar with five flavours (PDG); the comparison was always '
                           'with 137.036. Formula and value unchanged. Former record: symbol α⁻¹(M_Z), exp_value 137.036, '
                           'exp_error 0.0001 (unsourced), exp_source PDG 2025, deviation_pct −0.001971. Deviation −19.70 ppm: '
                           'a numerical proximity, not experimental compatibility (about 1.3e5 σ at the CODATA uncertainty). '
                           'Public erratum: K7 publications/ERRATUM_v3.5.md §5; [2026-10-22] exp refreshed to CODATA 2022: '
                           'α⁻¹ at q² = 0')
    # 2026-11-11 (Brieuc) : A21 par la règle des rapports de masses (k7_v3_6_exp_refresh.py) ; B01 et B04 portaient une
    # valeur arrondie à la place de la valeur de leur formule.
    obs['A21']['notes'] = ('[2026-11-11] exp computed from the PDG 2026 masses m_W = 80.3625(77) GeV and m_Z = 91.1879(20) GeV, '
                           'as for the other mass ratios (correlations neglected); the ratio line of the PDG summary table, '
                           '0.88136(15), is no longer used')
    for i, g in (('B01', math.sqrt(14 / 3)), ('B04', (14 - math.pi) ** 3)):
        obs[i]['gift_value'] = g
        obs[i]['deviation_pct'] = round((g - obs[i]['exp_value']) / obs[i]['exp_value'] * 100, 6)
    obs['D22']['notes'] = obs['D22']['notes'].replace('GIFT: K7 topology', 'K₇ topology')
    md['timestamp'] = DATE
    md['experimental_sources'] = ['PDG 2026', 'PDG 2025 (entries not refreshed, S3)', 'PDG 2024 (Y_p, S3)',
                                  'NuFIT 6.1 (2025, IC24+SK-atm)', 'Planck 2018 (TT,TE,EE+lowE+lensing)', 'CODATA 2022']
    summary(d)
    return d


def stats(lst):
    devs = [abs(o['deviation_pct']) for o in lst if o['exp_value'] != 0]
    return {'count': len(lst), 'n_with_exp': len(devs),
            'mean_abs_deviation_pct': round(sum(devs) / len(devs), 4) if devs else 0}


def summary(d):
    """Mêmes définitions que observable_dataset.py l. 681-715."""
    o = d['observables']
    s = d['summary']
    for typ in sorted({x['type'] for x in o}):
        lst = [x for x in o if x['type'] == typ]
        s['by_type'][typ] = {**stats(lst), 'n_lean_certified': sum(1 for x in lst if x['lean_theorem'])}
    for sec in sorted({x['sector'] for x in o}):
        s['by_sector'][sec] = stats([x for x in o if x['sector'] == sec])
    devs = [abs(x['deviation_pct']) for x in o if x['exp_value'] != 0 and x['type'] in ('I', 'II', 'III')]
    s.pop('n_exact', None)   # 2026-11-11 : la catégorie « exact » est retirée (S3)
    s.update(n_with_experiment=len(devs), mean_abs_deviation_pct=round(sum(devs) / len(devs), 4),
             n_below_01_pct=sum(1 for v in devs if v < 0.1),
             n_below_1_pct=sum(1 for v in devs if v < 1.0), n_lean_certified=sum(1 for x in o if x['lean_theorem']))


def numeric_fields(d):
    # le LEE ne lit que le Type I : son symbole est figé ; celui de C14 change, il était faux
    # Seule exception permise par ce gate : exp_value, exp_error, deviation_pct des six rapports recalculés sur les chaînes.
    free = ('exp_value', 'exp_error', 'deviation_pct')
    return {o['id']: {k: o.get(k) for k in NUMERIC + (('symbol',) if o['type'] == 'I' else ())
                      if not (o['id'] in RECOMPUTED + ('A21',) and k in free)
                      and not (o['id'] in ('B01', 'B04') and k in ('gift_value', 'deviation_pct'))} for o in d['observables']}


def export_csv():
    src = open(os.path.join(ROOT, 'canonical', 'scripts', 'observable_dataset.py'), encoding='utf-8').read()
    fn = [n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == 'export_csv']
    ns = {'csv': csv, 'List': list, 'GIFTObservable': object}
    exec(compile(ast.Module(fn, []), 'observable_dataset.py', 'exec'), ns)
    return ns['export_csv']


def dump(d):
    return json.dumps(d, ensure_ascii=False, indent=2) + '\n'


def main():
    raw = open(OBS, encoding='utf-8').read()
    d = apply(json.loads(raw))
    pinned = json.loads(git('-C', ROOT, 'show', f'{PIN_COMMIT}:canonical/data/observables.json'))
    a_, b_ = numeric_fields(pinned), numeric_fields(d)
    diff = [i for i in a_ if a_[i] != b_[i]]
    assert not diff and a_.keys() == b_.keys(), f'valeurs changées : {diff}'
    new = dump(d)
    objs = [SimpleNamespace(**{'gift_fraction': '', 'exp_error': None, **o}) for o in d['observables']]
    tmp = CSV_OUT + '.tmp'
    out, sys.stdout = sys.stdout, io.StringIO()
    export_csv()(objs, tmp)
    sys.stdout = out
    c = open(tmp, encoding='utf-8', newline='').read()
    os.remove(tmp)
    if '--check' in sys.argv:
        same = new == raw and c == open(CSV_OUT, encoding='utf-8', newline='').read()
        print('à jour' if same else 'PÉRIMÉ')
        sys.exit(0 if same else 1)
    open(OBS, 'w', encoding='utf-8').write(new)
    open(CSV_OUT, 'w', encoding='utf-8', newline='').write(c)
    print(f'valeurs comparées à {PIN_COMMIT} : {len(a_)} entrées identiques ; CSV régénéré')


if __name__ == '__main__':
    main()
