#!/usr/bin/env bash
# Build "The K7 Dictionary" v3.6 LaTeX from markdown sources (formerly GIFT).
# Copy of build_3.5.sh; mirrors the v3.4 template (preamble, headers, biblio numeric \cite{N}).
#
# Pipeline per doc:
#   1. pandoc md -> body.tex (no header, no biblio)
#   2. sed post-process:  [N] -> \cite{N};  [N, M] -> \cite{N,M};
#                         [N, "extra"] -> \cite[extra]{N}
#   3. wrap with 3.6 title/author/date + \input{gift_3.6_bib} + \end{document}
#   4. pdflatex x 2 for TOC/refs
#
# Requires: pandoc, pdflatex, python3.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$(cd "$HERE/.." && pwd)"
cd "$HERE"

VERSION="3.6"
python3 "$HERE/gen_bib_3_6.py"
DATE_LABEL="November 2026"
DOI_CONCEPT="10.5281/zenodo.16891489"   # concept DOI of the series, printed in the title block of the five PDFs (checked below)

# -------- helper: md -> body.tex via pandoc, then cite conversion --------
convert_body() {
    local md="$1"    # absolute path
    local out="$2"   # absolute output tex path
    local mode="${3:-supp}"   # "main" inserts \tableofcontents after Keywords
    local tmp
    tmp="$(mktemp -t gift36body.XXXXXX.tex)"

    # Preprocess: strip the redundant front-matter that pandoc would emit
    # as \section (which then duplicates the LaTeX \maketitle title/author):
    #   1. First `#` heading (the doc title -- already in \title{})
    #   2. `**Brieuc de La Fourniere**` and `*Independent researcher…*` lines
    #      (already in \author{} / \noindent block)
    #   3. Leading horizontal rules (---)
    #   4. Shield-badge lines
    # We consume until we hit the first `## ` (real body section) or the
    # first paragraph of prose. Uses a tiny python filter for precision.
    local pre
    pre="$(mktemp -t gift36pre.XXXXXX.md)"
    python3 - "$md" "$pre" <<'PYPRE'
import sys, re
src, dst = sys.argv[1], sys.argv[2]
with open(src) as f: lines = f.readlines()

# Consume leading front-matter until we hit either a `## ` heading OR a body
# line that clearly starts real content (a bold-italic abstract paragraph,
# a `**Status**:` line, etc. -- anything that isn't the redundant title block).
front_patterns = [
    re.compile(r'^#\s'),                              # h1 title
    re.compile(r'^\*\*Brieuc'),                       # author bold
    re.compile(r'^\*Independent researcher'),         # affiliation italic
    re.compile(r'^---\s*$'),                          # horizontal rule
    re.compile(r'^\[!\[.*shields\.io.*\)\]\(.*\)\s*$'),  # shield badges
    re.compile(r'^\s*$'),                             # blank
]
def is_front(line):
    return any(p.match(line) for p in front_patterns)

i = 0
while i < len(lines) and is_front(lines[i]):
    i += 1
# A supplement's unnumbered `## ` subtitle right under its title is already in
# \title{} (SUPP_SUB): left in the body it printed twice on page 1 of S1.
if i < len(lines) and re.match(r'^##\s+(?!S?\d)', lines[i]) and not re.match(r'^##\s+(Abstract|Preface)', lines[i]):
    i += 1
    while i < len(lines) and is_front(lines[i]):
        i += 1
body = lines[i:]

# Strip the numbered "References" section: the shared bibliography is
# injected as \input{gift_3.6_bib}; leaving the md list in the body
# renders a duplicate reference list whose [N] entries get converted
# to \cite{N}. Keep everything after the section (e.g. Author's
# Related Works, footer).
out, skipping = [], False
for line in body:
    if re.match(r'^#{1,3}\s+References\s*$', line):
        skipping = True
        continue
    if skipping and re.match(r'^#{1,3}\s+\S', line):
        skipping = False
    if not skipping:
        # De-link internal md anchors ([text](#anchor)): the heading shift
        # breaks their hyperref targets, leaving dead links in the PDF TOC.
        out.append(re.sub(r'\[([^\]]+)\]\(#[^)]+\)', r'\1', line))

with open(dst, 'w') as f:
    f.writelines(out)
PYPRE

    pandoc -f markdown+lists_without_preceding_blankline -t latex \
        --wrap=none \
        --no-highlight \
        --top-level-division=section \
        --shift-heading-level-by=-1 \
        "$pre" -o "$tmp"
    rm -f "$pre"

    # Cite pipeline: apply python for robustness (multi-digit, spaces, qualified)
    python3 - "$tmp" "$out" "$mode" <<'PY'
import re, sys
inp, outp = sys.argv[1], sys.argv[2]
mode = sys.argv[3] if len(sys.argv) > 3 else "supp"
with open(inp) as f: txt = f.read()

# SMP (>U+FFFF) glyphs that pdftex+inputenc utf8 can't map via
# \DeclareUnicodeCharacter -- substitute inline. Inside verbatim
# environments LaTeX macros print LITERALLY (the raw
# "\ensuremath{\mathbb{O}}" leak in the S1 derivation diagrams,
# caught by the 2026-07-09 review): use ASCII fallbacks there.
SMP = {
    '\U0001D4D8': r'\ensuremath{\mathcal{I}}',   # 𝓘
    '\U0001D524': r'\ensuremath{\mathfrak{g}}',  # 𝔤
    '\U0001D546': r'\ensuremath{\mathbb{O}}',    # 𝕆
    '\U0001D49F': r'\ensuremath{\mathcal{D}}',  # 𝒟
    '\U0001D529': r'\ensuremath{\mathfrak{l}}',  # 𝔩
}
SMP_ASCII = {
    '\U0001D4D8': 'I',
    '\U0001D524': 'g',
    '\U0001D546': 'O',
    '\U0001D49F': 'D',
    '\U0001D529': 'l',
}
_parts = re.split(r'(\\begin\{verbatim\}.*?\\end\{verbatim\})', txt, flags=re.S)
for _i, _p in enumerate(_parts):
    _table = SMP_ASCII if _p.startswith(r'\begin{verbatim}') else SMP
    for k, v in _table.items():
        _p = _p.replace(k, v)
    _parts[_i] = _p
txt = ''.join(_parts)

# Handle bracketed citation patterns produced by pandoc from md `[N]`, `[N, M]`, `[N-M]`.
# Pandoc keeps them as literal `{[}N{]}` for the outer brackets when the input was inside
# markdown. Handle both raw `[N]` and pandoc-escaped `{[}N{]}` forms.

BIB_MAX = max(int(k) for k in re.findall(r'\\bibitem\{(\d+)\}', open('gift_3.6_bib.tex', encoding='utf-8').read()))  # derived from the bib — numbers above this are
              # intervals/data (e.g. the [182, 212] deg falsification window),
              # NOT citations; converting them produced "[?, ?]" in the PDF.

def cite_repl(m):
    inner = m.group(1)
    parts = [p.strip() for p in inner.split(',')]
    # Reject if any part is not numeric (avoid rewriting things like [Voisin 2002])
    if not all(p.isdigit() for p in parts):
        return m.group(0)
    if any(int(p) < 1 or int(p) > BIB_MAX for p in parts):
        return m.group(0)
    # A bracketed pair after a membership or comparison sign is an interval, even when
    # both ends are valid keys: b2 in [1, 40] must not become \\cite{1,40}.
    if len(parts) > 1 and re.search(r'(∈|\\in|=|≤|≥|\bin|\brange)\s*\$?\s*$', m.string[max(0, m.start() - 12):m.start()]):
        return m.group(0)
    return r'\cite{' + ','.join(parts) + '}'

# Order matters: escaped-form first, then raw.
txt = re.sub(r'\{\[\}([0-9][0-9,\s]*)\{\]\}', cite_repl, txt)
txt = re.sub(r'\[([0-9][0-9,\s]*)\]', cite_repl, txt)

# Qualified citations: [53, Conjecture 1] -> \\cite[Conjecture 1]{53}.
def qual_repl(m):
    return r'\cite[' + m.group(2).strip() + ']{' + m.group(1) + '}' if 1 <= int(m.group(1)) <= BIB_MAX else m.group(0)
txt = re.sub(r'\{\[\}([0-9]+),\s*([A-Z][^{}\[\]]*?)\{\]\}', qual_repl, txt)

# Captions: markdown alt-texts start with "**Figure N.**"; LaTeX prepends its
# own "Figure N:" label, producing "Figure 1: Figure 1. ...". Strip the prefix.
txt = re.sub(r'(\\caption\{)\\textbf\{Figure \d+\.\}\s*', r'\1', txt)

# Horizontal rules: pandoc renders md `---` as a half-width centered rule;
# render full-width (cold-read request 2026-07-09).
txt = txt.replace(r'\rule{0.5\linewidth}', r'\rule{\linewidth}')

# Overfull fixes (cold-read 2026-07-09): long unbreakable tokens overflow the
# margin. (a) allow line breaks after _ . / - inside inline code (\texttt);
# (b) allow breaks after escaped underscores in plain text (identifiers like
# max_constant_value). \allowbreak only takes effect when the line is full.
def breakable_tt(m):
    inner = m.group(1)
    inner = re.sub(r'(?<=[a-z])(?=[A-Z])', r'\\allowbreak{}', inner)  # CamelCase
    inner = inner.replace(r'\_', r'\_\allowbreak{}')
    inner = re.sub(r'([./-])', r'\1\\allowbreak{}', inner)
    return r'\texttt{' + inner + '}'
txt = re.sub(r'\\texttt\{([^{}]*)\}', breakable_tt, txt)

# Subscripts and superscripts of the plain-text notation (m_W, Ω_Λ, N_gen^2): pandoc
# escapes them as literal characters. Identifiers, code, links and labels stay literal.
PROTECT = re.compile(r'(\\(?:texttt|href|url|label|hypertarget|includegraphics|cite)(?:\[[^\]]*\])?'
                     r'\{(?:[^{}]|\{[^{}]*\})*\}|\\begin\{verbatim\}.*?\\end\{verbatim\})', re.S)
GREEK = 'αβγδεζηθικλμνξπρστφχψωΓΔΘΛΞΠΣΦΨΩ'
SUB_BODY = rf'[A-Za-z0-9{GREEK}]+(?:-[A-Z]+)?'
SUB = re.compile(rf'((?:(?<![A-Za-z0-9\\])(?:[A-Za-z]|det|tau|Vol)|[{GREEK}³]|\\textbar|‖))\\_'
                 rf'(?:\\\{{([^{{}}$]*?)\\\}}|({SUB_BODY}))(?![A-Za-z0-9]|\\_)')
SUP = re.compile(rf'\\\^\{{\}}(?:\\\{{([^{{}}$]*?)\\\}}|\(([^(){{}}$]*)\)|(-?[A-Za-z0-9{GREEK}]+))')
def notation(chunk):
    chunk = SUP.sub(lambda m: r'\textsuperscript{' + (m.group(1) or m.group(2) or m.group(3)) + '}', chunk)
    return SUB.sub(lambda m: m.group(1) + r'\textsubscript{' + (m.group(2) or m.group(3)) + '}', chunk)
txt = ''.join(c if i % 2 else notation(c) for i, c in enumerate(PROTECT.split(txt)))

# Wide tables (five columns or more): smaller type and tighter columns; break long table tokens.
txt = re.sub(r'\\begin\{longtable\}\[\]\{@\{\}\n(?=[^\n]*\(\\linewidth - (?:[89]|\d\d)\\tabcolsep\))',
             lambda m: '{\\footnotesize\\setlength{\\tabcolsep}{3pt}\n' + m.group(0), txt)
parts = re.split(r'(\{\\footnotesize\\setlength\{\\tabcolsep\}\{3pt\}\n.*?\\end\{longtable\})', txt, flags=re.S)
txt = ''.join(p + '}' if i % 2 else p for i, p in enumerate(parts))
txt = txt.replace('(TT,TE,EE+lowE+lensing)', r'(TT,TE,EE +\allowbreak{}lowE +\allowbreak{}lensing)')
txt = txt.replace('Certificate/RelationsV36', r'Certificate/\allowbreak{}RelationsV36')
txt = re.sub(r'\\_(?!\\allowbreak)', r'\\_\\allowbreak{}', txt)

# Main only: page break after the abstract, then ToC, then page break
# (cold-read request 2026-07-09). Anchor = the Keywords paragraph line.
if mode == "main":
    txt = re.sub(
        r'(\\textbf\{Keywords\}[^\n]*\n)',
        r'\1\n\\newpage\n\\setcounter{tocdepth}{1}\n\\tableofcontents\n\\newpage\n',
        txt, count=1)

with open(outp, 'w') as f: f.write(txt)
PY
    rm -f "$tmp"
}

# -------- helper: emit header/footer wrapper --------
# args: outfile, fancyhead_left, pdftitle, title_body, author_block, date_block, is_main(1/0)
wrap_doc() {
    local out="$1" fancy="$2" pdftitle="$3" titlebody="$4" authblock="$5" dateblock="$6" is_main="$7" body="$8"

    {
        cat <<EOF
\documentclass[11pt,a4paper]{article}
\input{gift_preamble}
% Glyphs new in 3.6, kept here rather than in the preamble shared with 3.4 and 3.5.
\DeclareUnicodeCharacter{02E2}{\ensuremath{^{\mathrm{S}}}}
\DeclareUnicodeCharacter{1D37}{\ensuremath{^{\mathrm{K}}}}
\DeclareUnicodeCharacter{1D39}{\ensuremath{^{\mathrm{M}}}}
\DeclareUnicodeCharacter{1D3A}{\ensuremath{^{\mathrm{N}}}}
\DeclareUnicodeCharacter{1D3E}{\ensuremath{^{\mathrm{P}}}}
\DeclareUnicodeCharacter{1D9C}{\ensuremath{^{\mathrm{C}}}}
\DeclareUnicodeCharacter{211A}{\ensuremath{\mathbb{Q}}}
\DeclareUnicodeCharacter{226B}{\ensuremath{\gg}}
\DeclareUnicodeCharacter{22A5}{\ensuremath{\perp}}
% pandoc >= 3.2.1 emits \pandocbounded around images; provide a fallback.
% Also clamp all images to \linewidth (natural-size figures overflowed the
% right margin -- the "truncated figures" flagged by the round-2 reviews).
% Kept here rather than in gift_preamble.tex, shared with the 3.4 build.
\providecommand{\pandocbounded}[1]{#1}
\makeatletter
\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
\makeatother
\setkeys{Gin}{width=\maxwidth,keepaspectratio}
% md headings carry their own literal numbering ("3.2 What ..."); suppress
% the LaTeX section counters to avoid "0.2 1. Introduction" double numbering.
\setcounter{secnumdepth}{0}
% Loosen justification slightly: long technical identifiers (made breakable
% at build time via \allowbreak) still need extra stretch to avoid overfulls.
\emergencystretch=3em
\fancyhead[L]{${fancy}}
\hypersetup{pdftitle={${pdftitle}},pdfauthor={Brieuc de La Fournière}}

\graphicspath{{../../../figures/}}

\title{%
${titlebody}%
}
${authblock}
${dateblock}

\begin{document}

\maketitle
\noindent\rule{\textwidth}{0.2pt}
EOF

        if [ "$is_main" = "1" ]; then
            cat <<'MAINHDR'

\noindent\textbf{Author}: Brieuc de La Fourni\`ere

\noindent Independent researcher, Beaune, France

\noindent Contact: \href{mailto:brieuc@arithmon.com}{\texttt{brieuc@arithmon.com}} \quad | \quad \href{https://arithmon.com}{arithmon.com}

\noindent\textbf{Date}: November 2026 \quad v3.6 \quad | \quad DOI (all versions): \href{https://doi.org/10.5281/zenodo.16891489}{10.5281/zenodo.16891489}

% Title page: allow one extra line so the (shortened) abstract + keywords
% end exactly on page 1 (ToC follows on its own page).
\enlargethispage{2\baselineskip}
MAINHDR
        else
            # Same explicit block as the main paper: with \author and \date the
            # preamble's \maketitle ran subtitle, author and date into one paragraph.
            cat <<'SUPPHDR'

\noindent\textbf{Author}: Brieuc de La Fourni\`ere \quad | \quad Independent researcher, Beaune, France

\noindent\textbf{Date}: November 2026 \quad v3.6 \quad | \quad DOI (all versions): \href{https://doi.org/10.5281/zenodo.16891489}{10.5281/zenodo.16891489}

\thispagestyle{fancy}
SUPPHDR
        fi

        echo ""
        cat "$body"
        echo ""
        cat <<'FOOT'

\bigskip
\input{gift_3.6_bib}

\end{document}
FOOT
    } > "$out"
}

# ============================================
# MAIN PAPER
# ============================================
echo "==> physics_main.md -> k7_framework_3_6_main.tex"
BODY_MAIN="$(mktemp -t gift36main.XXXXXX.tex)"
convert_body "$SRC/physics_main.md" "$BODY_MAIN" "main"

wrap_doc \
    "k7_framework_3_6_main.tex" \
    'The $K_7$ Dictionary v3.6' \
    "The K7 Dictionary: Testing G2 Topology against Particle Physics and Cosmology" \
    '\LARGE\textbf{The $K_7$ Dictionary}\\[0.3em]
\large Testing $\mathrm{G}_2$ Topology against Particle Physics and Cosmology' \
    '\author{}' \
    '\date{}' \
    "1" \
    "$BODY_MAIN"
rm -f "$BODY_MAIN"

# ============================================
# SUPPLEMENTS
# ============================================
declare -A SUPP_TITLE=(
    [S1]='Mathematical Foundations'
    [S2]='The 33 Relations'
    [S3]='Observable Dataset'
    [S4]='Sieve and Look-Elsewhere Diagnostics'
)
declare -A SUPP_SUB=(
    [S1]='$E_8$ Exceptional Lie Algebra, $G_2$ Holonomy Manifolds, and the Topological Status of $K_7$'
    [S2]='Arithmetic, Dictionary Choices and Status'
    [S3]='33 Relations Compared with Measurement; 62 Conditional and Diagnostic Entries'
    [S4]='The Look-Elsewhere Null and Descriptive Diagnostics'
)
declare -A SUPP_SRC=(
    [S1]='supplement_foundations.md'
    [S2]='supplement_derivations.md'
    [S3]='supplement_observables.md'
    [S4]='supplement_sieve_diagnostics.md'
)

for S in S1 S2 S3 S4; do
    echo "==> ${SUPP_SRC[$S]} -> k7_framework_3_6_${S}.tex"
    BODY="$(mktemp -t gift36${S}.XXXXXX.tex)"
    convert_body "$SRC/${SUPP_SRC[$S]}" "$BODY"

    wrap_doc \
        "k7_framework_3_6_${S}.tex" \
        "The \$K_7\$ Dictionary v3.6: Supplement ${S}" \
        "The K7 Dictionary v3.6 Supplement ${S}: ${SUPP_TITLE[$S]}" \
        "\\LARGE\\textbf{Supplement ${S}: ${SUPP_TITLE[$S]}}\\\\[0.3em]
\\large ${SUPP_SUB[$S]}" \
        '\author{}' \
        '\date{}' \
        "0" \
        "$BODY"
    rm -f "$BODY"
done

# ============================================
# BUILD PDFs
# ============================================
echo ""
echo "==> pdflatex passes"
for f in k7_framework_3_6_main k7_framework_3_6_S1 k7_framework_3_6_S2 k7_framework_3_6_S3 k7_framework_3_6_S4; do
    echo "--- building ${f}.pdf ---"
    pdflatex -interaction=nonstopmode -halt-on-error "${f}.tex" > "${f}.build.log" 2>&1 || {
        echo "PASS 1 FAILED for ${f} -- see ${f}.build.log"; tail -60 "${f}.build.log"; exit 1;
    }
    pdflatex -interaction=nonstopmode -halt-on-error "${f}.tex" > "${f}.build.log" 2>&1 || {
        echo "PASS 2 FAILED for ${f} -- see ${f}.build.log"; tail -60 "${f}.build.log"; exit 1;
    }
    echo "    OK: $(du -h ${f}.pdf | cut -f1) $(grep -c '^' ${f}.tex) lines src"
done

echo ""
for f in k7_framework_3_6_main k7_framework_3_6_S1 k7_framework_3_6_S2 k7_framework_3_6_S3 k7_framework_3_6_S4; do
    grep -q "$DOI_CONCEPT" "${f}.tex" || { echo "concept DOI missing from ${f}.tex"; exit 1; }
done
echo "=== 3.6 build DONE ==="
ls -la k7_framework_3_6_*.pdf
