#!/usr/bin/env python3
"""
verifica_estilo.py v2 — Auditor do MANUAL_DE_ESTILO_UNIFICADO (v1.1.0) para toda a casa.
Uso: python3 verifica_estilo.py <arquivo.md|.txt>

Herda do verifica_estilo.py do Kimi (#3/#7/#9/#13/#14/#16/#17) e acrescenta as
EMENDAS 14/15/16 (EMU-3/4/5, ordem do Miguel 01/09/2026):
  [E14] abertura abstrata — 1ª frase sem fato/cena/data (heurística: "X é uma palavra...", meta-conceito)
  [E15] metalinguagem/anúncio do efeito — "a metáfora é reveladora", "note a lógica", "a pergunta deste capítulo", "aí mora a ironia", "resta o retrato"...
  [E15b] spoiler da emoção — "assusta", "choca", "impressiona", "o pior ainda vem" na voz do narrador
  [E16] frase vazia — frases-curta-que-nada-entregam (lista de padrões anúncio/guia)
  [PV] ponto e vírgula · [TD] travessão · [DP] dois-pontos (fora de URL/hora/markdown) ·
  [P2] parágrafo com mais de 2 frases (aviso — livro pode respirar, portal não)
"""
import re, sys, unicodedata

STOP = {"de","da","do","das","dos","e","em","um","uma","o","a","os","as","que","se","com","por",
        "para","no","na","nos","nas","ao","aos","à","às","ou","como","mais","foi","são","é",
        "ser","ter","seu","sua","seus","suas","ele","ela","eles","elas","isso","esse","essa",
        "este","esta","estes","estas","the","of","and","to","in","an"}

META_PATTERNS = [
    r"[aà] met[áa]fora [ée] reveladora", r"note (a|o) ", r"a pergunta (deste? (cap[íi]tulo|texto)|central) [ée]",
    r"a[íi] mora (a|uma) ", r"resta o retrato", r"o golpe de g[êe]nio est[áa] em", r"vamos ao que interessa",
    r"como veremos", r"veremos adiante", r"sem mais delongas", r"vale destacar que", r"cabe destacar que",
    r"[ée] preciso dizer que", r"n[ãa]o por acaso", r"o que isso significa\??", r"e o que [ée] pior",
    r"a seguir", r"no pr[óo]ximo cap[íi]tulo", r"este cap[íi]tulo (vai|pretende|se prop[õo]e)",
]
SPOILER = [r"\bassusta\b", r"\bchoca\b", r"\bimpressiona\b", r"\bdeixa estarrecido\b", r"o pior ainda vem", r"\bespantoso\b"]

def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    return "".join(c for c in w if unicodedata.category(c) != "Mn")

def main(path):
    text = open(path, encoding="utf-8").read()
    # ignora cabeçalhos markdown, citações (>) e bloco de notas finais
    body = re.sub(r"^(#|>).*$", "", text, flags=re.M)
    body = body.split("*(As notas")[0]
    issues = []

    # parágrafos com mais de 2 frases
    for par in [p.strip() for p in body.split("\n") if len(p.strip()) > 40]:
        n = len([x for x in re.split(r"(?<=[.!?…])\s+", par) if len(x.strip()) > 2])
        if n > 2:
            issues.append(f"[P2] Parágrafo com {n} frases (máx 2): «{par[:60]}…»")

    sents = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", body.replace("\n", " ")) if len(s.strip()) > 2]

    # E14: primeira frase abstrata (meta-conceito em vez de fato/cena/data)
    if sents:
        f1 = sents[0]
        if re.match(r"^(O|A) [a-zà-ú]+ [ée] (uma|a|o) (palavra|conceito|ideia|pergunta|tese)", f1, re.I):
            issues.append(f"[E14] 1ª frase abstrata, não entra no fato/cena: «{f1[:70]}…»")

    for i, s in enumerate(sents):
        low = norm(s)
        first = norm(s.split()[0]) if s.split() else ""
        if first == "e":
            issues.append(f"[#3] Frase começa com 'E,': «{s[:70]}…»")
        if first == "porem":
            issues.append(f"[#13] 'Porém' abrindo frase: «{s[:70]}…»")
        if "—" in s:
            issues.append(f"[#9] Travessão: «{s[:70]}…»")
        if ";" in s:
            issues.append(f"[PV] Ponto e vírgula: «{s[:70]}…»")
        if re.search(r":", s) and not re.search(r"https?://|\d{1,2}:\d{2}", s):
            issues.append(f"[#14] Dois-pontos (avaliar): «{s[:70]}…»")
        for pat in META_PATTERNS:
            if re.search(pat, low):
                issues.append(f"[E15] Metalinguagem/anúncio ({pat[:24]}…): «{s[:60]}…»")
                break
        for pat in SPOILER:
            if re.search(pat, low):
                issues.append(f"[E15b] Spoiler da emoção: «{s[:60]}…»")
                break
        # repetição de palavra significativa na frase anterior
        if i > 0:
            prev_words = {norm(w) for w in re.findall(r"\b\w{4,}\b", sents[i-1])} - {norm(x) for x in STOP}
            cur_words = {norm(w) for w in re.findall(r"\b\w{4,}\b", s)} - {norm(x) for x in STOP}
            rep = {w for w in (prev_words & cur_words) if len(w) > 4}
            if rep:
                issues.append(f"[#7] Repete «{', '.join(sorted(rep))}» em frases vizinhas: «{s[:60]}…»")
        rhymes = re.findall(r"\b\w+(ece|esse|isse|ice)\b", low)
        if len(set(rhymes)) > 1:
            issues.append(f"[#17] Possível rima deselegante: «{s[:70]}…»")

    sizes = [len(s.split()) for s in sents]
    for i in range(len(sizes) - 2):
        a, b, c = sizes[i], sizes[i+1], sizes[i+2]
        if a >= 8 and max(a, b, c) - min(a, b, c) <= 3:
            issues.append(f"[#16] Metrônomo? 3 frases de {a},{b},{c} palavras: «{sents[i][:50]}…»")

    print(f"== AUDITORIA DE ESTILO v2 (manual v1.1.0) — {path.split('/')[-1]} ==")
    print(f"frases analisadas: {len(sents)}")
    if not issues:
        print("✅ Nenhuma infração encontrada.")
    else:
        seen = set()
        for it in issues:
            key = it[:80]
            if key in seen: continue
            seen.add(key)
            print(" •", it)
        print(f"\n{len(seen)} alertas.")
    return 0 if not issues else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
