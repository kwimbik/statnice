"""Vygeneruje 07-shrnuti.tex: pouze oddily "Shrnuti ke zkousce" ze vsech tri okruhu.

Spousteni z korene repozitare:  python zkouseni/gen-07-shrnuti.py
Pote 2x pdflatex 07-shrnuti.tex.
"""
import io
import re

SOURCES = [
    ("01-multiagentni-systemy.tex", "Multiagentní systémy"),
    ("02-prirodou-inspirovane-pocitani.tex", "Přírodou inspirované počítání"),
    ("03-dobyvani-znalosti.tex", "Dobývání znalostí"),
]
OUT = "07-shrnuti.tex"

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[czech]{babel}
\usepackage[margin=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{parskip}
\usepackage{enumitem}
\setlist{nosep,leftmargin=1.4em}
\usepackage{booktabs}
\usepackage{array}
\usepackage{xcolor}
\definecolor{linkblue}{RGB}{20,60,150}
\definecolor{defbg}{RGB}{240,244,252}
\definecolor{defframe}{RGB}{100,130,190}
\definecolor{markcol}{RGB}{176,84,0}
\definecolor{markbg}{RGB}{253,246,236}
\usepackage[most]{tcolorbox}
\newtcolorbox{defbox}[1][]{breakable,colback=defbg,colframe=defframe,boxrule=0.6pt,arc=1.5mm,left=2mm,right=2mm,top=1mm,bottom=1mm,title={#1},fonttitle=\bfseries}
\newtcolorbox{poznbox}[1][]{breakable,colback=markbg,colframe=markcol,boxrule=0.6pt,arc=1.5mm,left=2mm,right=2mm,top=1mm,bottom=1mm,title={#1},fonttitle=\bfseries}
\newtheorem{veta}{Věta}[section]
\theoremstyle{definition}
\newtheorem{definice}{Definice}[section]
\usepackage[colorlinks=true,linkcolor=linkblue,urlcolor=linkblue]{hyperref}
\usepackage{algorithm}
\usepackage{algpseudocode}
\renewcommand{\algorithmicrequire}{\textbf{Vstup:}}
\renewcommand{\algorithmicensure}{\textbf{Výstup:}}
\usepackage{graphicx}
\graphicspath{{obrazky/mas/}}
\newcommand{\mimo}{\textcolor{markcol}{\textsf{\footnotesize[$\blacklozenge$~nad rámec slidů]}}}
\newcommand{\mimoq}[1]{\textcolor{markcol}{\textsf{\footnotesize[$\blacklozenge$~nad rámec slidů: #1]}}}

\title{\textbf{Shrnutí ke zkoušce}\\[0.3em]\large Opakovací výtah ze všech tří okruhů}
\author{SZZ Umělá inteligence, MFF UK}
\date{září 2026}

\begin{document}
\maketitle
\vspace{-1.5em}
\begin{center}
\begin{minipage}{0.93\textwidth}
\small
Generovaný dokument: pouze oddíly \uv{Shrnutí ke zkoušce} z~učebních textů
\texttt{01-multiagentni-systemy}, \texttt{02-prirodou-inspirovane-pocitani}
a~\texttt{03-dobyvani-znalosti}, beze změny obsahu. Číslování kapitol odpovídá zdrojovým
textům (= položkám okruhu). Odkazy na oddíly zdrojových textů jsou vypuštěny.
Znovu vygenerovat: \texttt{python zkouseni/gen-07-shrnuti.py} a~2$\times$ \texttt{pdflatex}.
\end{minipage}
\end{center}
\tableofcontents
\newpage
"""


def read(path):
    raw = io.open(path, encoding="utf-8", newline="").read()
    return raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def balanced_title(lines, i):
    """Vrati (titulek, index posledniho radku) pro \\section{...}/\\part{...}, i pres vice radku."""
    buf = lines[i]
    j = i
    while buf.count("{") > buf.count("}") and j + 1 < len(lines):
        j += 1
        buf += " " + lines[j].strip()
    m = re.match(r"\\(?:part|section)\{(.*)\}\s*$", buf.strip())
    title = m.group(1) if m else buf
    title = re.sub(r"\\label\{[^}]*\}", "", title).strip()
    return title, j


REF_PATTERNS = [
    # (odd.~\ref{x}), (kap.~\ref{x}, \ref{y}), (odst.~\ref{x}) ... i s "viz"
    r"\s*\((?:viz\s+)?(?:odd|odst|kap|sec|Sect|Section|část|čás)\.?~?\\ref\{[^}]*\}(?:\s*(?:,|a)~?\s*\\ref\{[^}]*\})*\)",
    # "viz odd.~\ref{x}" / "odd.~\ref{x}" bez zavorek
    r"\s*(?:viz\s+)?(?:odd|odst|kap|sec|Sect|Section)\.?~?\\ref\{[^}]*\}(?:\s*(?:,|a)~?\s*\\ref\{[^}]*\})*",
    r"\s*(?:kapitol[aěuy]|oddíl[uy]?|část[i]?)~\\ref\{[^}]*\}",
    r"\\ref\{[^}]*\}",
]


def clean(body):
    text = "\n".join(body)
    text = re.sub(r"\\label\{[^}]*\}", "", text)
    for pat in REF_PATTERNS:
        text = re.sub(pat, "", text)
    text = re.sub(r"\(\s*\)", "", text)          # prazdne zavorky
    text = re.sub(r"[ \t]+([,;.])", r"\1", text)  # mezera pred interpunkci
    text = re.sub(r"~([,;.])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n") + "\n"


def extract(path):
    lines = read(path)
    out = []
    section_title = None
    pending_part = None
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if s.startswith("\\part{"):
            pending_part, i = balanced_title(lines, i)
            i += 1
            continue
        if s.startswith("\\section{"):
            section_title, i = balanced_title(lines, i)
            i += 1
            continue
        if re.match(r"\\subsection\{Shrnutí ke~?zkoušce\}", s):
            j = i + 1
            body = []
            while j < n:
                t = lines[j].strip()
                if (t.startswith("\\section") or t.startswith("\\subsection")
                        or t.startswith("\\part") or t.startswith("\\end{document}")
                        or t.startswith("%=====")):
                    break
                body.append(lines[j])
                j += 1
            if pending_part is not None:
                out.append("\\section*{" + pending_part + "}\n"
                           "\\addcontentsline{toc}{section}{" + pending_part + "}\n")
                pending_part = None
            out.append("\\section{" + section_title + "}\n" + clean(body))
            i = j
            continue
        i += 1
    return out


doc = [PREAMBLE]
for path, name in SOURCES:
    parts = extract(path)
    doc.append("\\part{" + name + "}\n\\setcounter{section}{0}\n")
    doc.extend(parts)
    print(path, "->", len(parts), "shrnutí")
doc.append("\\end{document}\n")

text = "\n".join(doc)
left = re.findall(r"\\ref\{[^}]*\}", text)
if left:
    print("POZOR, zbyle \\ref:", left)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(text)
print("zapsano", OUT)
