#!/usr/bin/env python3
"""K₇ v3.6 — remplit la colonne « Status (main §4.1) » des tables de S2 (supplement_derivations.md) DEPUIS la table
§4.1 de physics_main.md (R6 : une seule source, lue, jamais recopiée à la main).

Chaque ligne `| Axx | … |` d'une table de S2 dont l'en-tête se termine par « Status (main §4.1) » reçoit en
dernière cellule le statut du §4.1 et le pull ; le reste de la ligne n'est pas touché. --check rougit si une
cellule diffère, si une relation manque à S2 ou y figure deux fois.

Usage : python3 canonical/scripts/k7_v3_6_s2_status.py [--check]
"""
import io
import os
import re
import sys

if (sys.stdout.encoding or '').lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k7_v3_6_s3_tables import PM  # noqa: E402  (même table source que S3)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
S2 = os.path.join(ROOT, 'canonical', 'papers', 'framework', 'supplement_derivations.md')
HEAD = 'Status (main §4.1)'


def main_rows():
    """ID → (pull, statut) lus dans la table §4.1 du main."""
    out = {}
    for ln in open(PM, encoding='utf-8'):
        m = re.match(r'\| (A\d\d) \| ', ln)
        if m:
            cells = [c.strip() for c in ln.strip().strip('|').split(' | ')]
            out[m.group(1)] = (cells[6], cells[7].replace('§', 'main §'))
    assert len(out) == 33, len(out)
    return out


def cell(pull, status):
    if pull in ('n/a', ''):
        return status
    if pull.endswith('*'):                      # le § 4.1 marque d'un astérisque un profil Δχ² non gaussien
        return f'{status}; pull {pull[:-1]}, not Gaussian (main §4.3)'
    return f'{status}; pull {pull}'


def main():
    rows = main_rows()
    src = open(S2, encoding='utf-8').read().split('\n')
    out, seen, in_table = [], [], False
    for ln in src:
        if ln.startswith('|') and ln.rstrip().rstrip('|').strip().endswith(HEAD):
            in_table = True
        elif not ln.startswith('|'):
            in_table = False
        m = re.match(r'\| (A\d\d) \| ', ln)
        if in_table and m:
            i = m.group(1); seen.append(i)
            cells = ln.strip().strip('|').split(' | ')
            cells[-1] = cell(*rows[i])
            ln = '| ' + ' | '.join(c.strip() for c in cells) + ' |'
        out.append(ln)
    missing = sorted(set(rows) - set(seen)); dup = sorted({i for i in seen if seen.count(i) > 1})
    t = '\n'.join(out)
    stale = t != '\n'.join(src)
    if '--check' in sys.argv:
        print('S2 :', 'PÉRIMÉ' if stale else 'à jour', '; absentes :', missing or 0, '; doublons :', dup or 0)
        sys.exit(1 if stale or missing or dup else 0)
    assert not missing and not dup, (missing, dup)
    open(S2, 'w', encoding='utf-8').write(t)
    print(f'S2 écrit ({len(seen)} relations)')


if __name__ == '__main__':
    main()
