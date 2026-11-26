#!/usr/bin/env python3
"""Génère gift_3.6_bib.tex depuis la section References de physics_main.md (source unique).
La bibliographie 3.5 était maintenue à la main et avait divergé du md (entrée [1] encore PDG 2024)."""
import sys, io, re, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
md = open('../physics_main.md', encoding='utf-8').read()
sec = md[md.index('## References'):]
sec = sec[:sec.index('\n---')]
ents = re.findall(r'^\[(\d+)\] (.+)$', sec, re.M)
nums = [int(n) for n, _ in ents]
assert nums == list(range(1, len(nums) + 1)), 'numérotation non contiguë'
out = ['% GÉNÉRÉ par gen_bib_3_6.py depuis physics_main.md : ne pas éditer.', '', '\\begin{thebibliography}{99}', '']
for n, t in ents:
    tex = subprocess.run(['pandoc', '-f', 'markdown', '-t', 'latex', '--wrap=none'], input=t, capture_output=True, text=True, check=True).stdout.strip()
    out += [f'\\bibitem{{{n}}} {tex}', '']
out.append('\\end{thebibliography}')
open('gift_3.6_bib.tex', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'{len(ents)} entrées')
