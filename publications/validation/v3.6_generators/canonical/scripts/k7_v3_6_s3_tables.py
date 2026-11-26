#!/usr/bin/env python3
"""K₇ v3.6 — génère les tables de S3 (supplement_observables.md) DEPUIS observables.json (R6).

Deux blocs, remplacés entre leurs marqueurs :
  <!-- BEGIN S3-TYPE-I --> … <!-- END S3-TYPE-I -->      les 33 relations : mesure, source, convention
  <!-- BEGIN S3-TYPE-II-IV --> … <!-- END S3-TYPE-II-IV -->  les 62 entrées non comptées, avec statut

Une seule source par champ : valeurs et sources ← JSON ; statut du type I ← table §4.1 de
physics_main.md (lue, jamais recopiée à la main) ; statut des types II–IV ← STATUS ci-dessous
(décisions v3.6 : main §4.5 et §5).

Usage : python3 canonical/scripts/k7_v3_6_s3_tables.py [--check]
"""
import io
import json
import os
import re
import sys

if (sys.stdout.encoding or '').lower() != 'utf-8':   # pas de double enveloppe à l'import
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k7_v3_6_table_sec4 import fmt_measured, fmt_pull  # noqa: E402  (même format que le §4)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OBS = os.path.join(ROOT, 'canonical', 'data', 'observables.json')
PM = os.path.join(ROOT, 'canonical', 'papers', 'framework', 'physics_main.md')
S3 = os.path.join(ROOT, 'canonical', 'papers', 'framework', 'supplement_observables.md')

UNIT = 'unit assignment (R10)'
LEGACY = 'Legacy value; derivation not documented in the current dataset; retained for traceability, not counted as a prediction'
COND = 'conditional reconstruction (calibration choices, main §6.2)'
WITHDRAWN = 'retired (supersymmetric running from a GUT boundary; main App. D)'
DIAG = 'diagnostic of the approximate local metric'
STATUS = {
    **{f'B0{i}': UNIT for i in range(1, 7)},
    'B07': 'scale bridge; ' + UNIT, 'B08': 'scale bridge; ' + UNIT, 'B09': 'scale bridge; ' + UNIT,
    **{f'B{i}': LEGACY for i in range(10, 16)},
    'B16': 'mixed scales (m_c at m_c, m_s at 2 GeV); not comparable',
    'B17': 'cascade of B16 (Type II, not comparable) and A08; no independent content', 'B18': LEGACY,
    'B19': LEGACY,
    'C01': COND, 'C02': COND, 'C03': DIAG,
    'C04': WITHDRAWN, 'C05': WITHDRAWN, 'C06': WITHDRAWN, 'C07': WITHDRAWN,
    'C08': DIAG, 'C09': DIAG + ' (compared with d/2, not a measurement)', 'C10': DIAG, 'C11': DIAG,
    'C12': DIAG, 'C13': DIAG + ' (compared with 1, not a measurement)',
    'C14': DIAG + ' (compared with N_gen)', 'C15': DIAG, 'C16': DIAG,
    'C17': COND, 'C18': COND + '; mismatched reference (see Type III above)', 'C19': COND,
    'C20': COND + '; inherits the C18 pairing', 'C21': COND + '; ratio C19/C20, inherits the C18 pairing',
    'D01': 'input (R1)', 'D02': 'input (R1)', 'D03': 'integer combination of R1',
    'D04': 'integer identity (main §2.4)', 'D05': 'imposed normalization (R2)',
    **{f'D{i:02d}': DIAG for i in range(6, 20)},
    'D20': 'from [42]; topological count', 'D21': 'from [42]; topological count',
    'D22': 'from [42]; conditional on the scale identification τ₀ = v_EW',
}


def main_status():
    """ID → (observable, formula, status) lus dans la table §4.1 du main."""
    out = {}
    for ln in open(PM, encoding='utf-8'):
        m = re.match(r'\| (A\d\d) \| ', ln)
        if m:
            cells = [c.strip() for c in ln.strip().strip('|').split(' | ')]
            out[m.group(1)] = (cells[1], cells[2], cells[7].replace('§', 'main §'))
    assert len(out) == 33, len(out)
    return out


def refresh_note(o):
    if (o.get('notes') or '').startswith('[2026-11-11] exp computed from the PDG 2026 masses'):
        return 'from the PDG 2026 masses'
    for part in (o.get('notes') or '').split('; '):
        if part.startswith(('[2026-10-22] exp refreshed to', '[2026-11-03] exp recomputed', '[2026-11-11] exp computed')):
            n = part.split(': ', 1)
            return n[1] if len(n) > 1 else ''
    return ''


def num(v):
    if isinstance(v, int) or (isinstance(v, float) and v.is_integer() and abs(v) < 1e6):
        return str(int(v))
    if isinstance(v, float) and (abs(v) >= 1e5 or abs(v) < 1e-3):
        return f'{v:.3g}'
    return f'{v:.6g}'


def table_I(obs, st):
    rows = ['| ID | Observable | Measured | Source | Pull | Convention / note | Status |',
            '|---|--------|------------|-------|----|---------------------|---------------|']
    for i in sorted(st):
        o = obs[i]
        rows.append(f"| {i} | {st[i][0]} | {fmt_measured(o)} | {o['exp_source']} | {fmt_pull(o)} | "
                    f"{refresh_note(o) or 'n/a'} | {st[i][2]} |")
    return '\n'.join(rows)


def table_II_IV(obs):
    rows = ['| ID | Type | Quantity | Formula or mechanism | Framework value | Reference value | Status |',
            '|---|---|-------|-------------|------|------|----------------------|']
    for i, o in sorted(obs.items()):
        if o['type'] == 'I':
            continue
        ref = num(o['exp_value']) if o.get('exp_value') not in (None, 0, 0.0, '') else 'n/a'
        f = o['gift_formula'].replace('|', '\\|')
        q = o['symbol'].replace('|', '\\|')
        q = f'`{q}`' if i in ('D11', 'D21') else q   # noms de producteur, pas une notation
        rows.append(f"| {i} | {o['type']} | {q} | {f} | {num(o['gift_value'])} | {ref} | {STATUS[i]} |")
    return '\n'.join(rows)


LEAN = os.path.join(ROOT, 'canonical', 'results', 'k7_v3_6_lean_map.json')
SCOPE = {'exact': 'exact rational equality of the closed form', 'components': 'components only',
         'bounds': 'base 27 and interval bounds on 27^φ', 'absent': 'no statement',
         'real': 'closed form in ℝ equal to the stated real value (no numerical bound)',
         'integer': 'the integer 197 (the unit is not in Lean)',
         'indices': 'indices (11, 5) and ζ(D_bulk)/ζ(Weyl) = ζ(11)/ζ(5) (no numerical bound)'}


def table_lean():
    """S3.7 : relation → énoncé Lean → commit → portée, depuis k7_v3_6_lean_map.json (relevé du 22-10)."""
    m = json.load(open(LEAN, encoding='utf-8'))
    rows = [f"Arithmon/K7-Lean, commit `{m['commit']}` ({m['merged']}); aggregate "
            f"`{m.get('aggregate', '').removeprefix('GIFT.')}`, which depends only on the axioms "
            f"{', '.join('`' + x + '`' for x in m.get('axioms', []))}.", '',
            '| ID | Observable | Lean declaration (under `GIFT.`) | Location | Scope |',
            '|---|------|---------------------|-------------|-------------|']
    for r in m['relations']:
        decl = (r['lean_declaration'] or 'n/a').removeprefix('GIFT.')
        loc = (r['location'] or 'n/a').removeprefix('GIFT/')
        # A06 et A08 sont des identités dans ℕ (RelationsV36.lean : A06_m_tau_m_e, A08_m_s_m_d), les 25 autres dans ℚ
        sc = ('exact equality of the closed form, between natural numbers' if r['scope'] == 'exact' and r['id'] in ('A06', 'A08')
              else SCOPE[r['scope']]) + ('; Lean name differs (see text)' if r.get('naming_note') else '')
        rows.append(f"| {r['id']} | {r['symbol']} | `{decl}` | {loc} | {sc} |"
                    .replace('`n/a`', 'n/a'))
    return '\n'.join(rows)


def splice(text, tag, body):
    a, b = f'<!-- BEGIN {tag} -->', f'<!-- END {tag} -->'
    i, j = text.index(a) + len(a), text.index(b)
    return text[:i] + '\n' + body + '\n' + text[j:]


def main():
    obs = {o['id']: o for o in json.load(open(OBS, encoding='utf-8'))['observables']}
    missing = [i for i, o in obs.items() if o['type'] != 'I' and i not in STATUS]
    assert not missing, missing
    text = open(S3, encoding='utf-8').read()
    new = splice(text, 'S3-TYPE-I', table_I(obs, main_status()))
    new = splice(new, 'S3-TYPE-II-IV', table_II_IV(obs))
    new = splice(new, 'S3-LEAN', table_lean())
    if '--check' in sys.argv:
        sys.exit(0 if new == text else 1)
    open(S3, 'w', encoding='utf-8').write(new)
    print('S3 : tables régénérées')


if __name__ == '__main__':
    main()
