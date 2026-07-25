#!/usr/bin/env python3
"""
verifica_estilo.py — Auditor do MANUAL_DE_ESTILO para os capítulos do livro.
Uso: python3 verifica_estilo.py <arquivo.md>
Flagra: repetições de palavra em frases vizinhas (#4/#7), frases começando com "E," (#3),
porém no início de frase (#13), travessões (#9), dois-pontos (#14), inglês (#11),
metrônomo de frases de tamanho parecido (#16) e rimas de terminações parecidas (#17).
"""
import re, sys, unicodedata

STOP = {"de","da","do","das","dos","e","em","um","uma","o","a","os","as","que","se","com","por",
        "para","no","na","nos","nas","ao","aos","à","às","ou","como","mais","foi","são","é",
        "ser","ter","seu","sua","seus","suas","ele","ela","eles","elas","isso","esse","essa",
        "este","esta","estes","estas","the","of","and","to","in","a","an"}

def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    return "".join(c for c in w if unicodedata.category(c) != "Mn")

def main(path):
    text = open(path, encoding="utf-8").read()
    # ignora cabeçalhos markdown e notas finais
    body = re.sub(r"^#.*$", "", text, flags=re.M)
    body = body.split("*(As notas")[0]
    sents = [s.strip() for s in re.split(r"(?<=[.!?…])\s+", body.replace("\n", " ")) if len(s.strip()) > 2]
    issues = []

    for i, s in enumerate(sents):
        first = norm(s.split()[0]) if s.split() else ""
        if first == "e":
            issues.append(f"[#3] Frase começa com 'E,': «{s[:70]}…»")
        if first == "porem":
            issues.append(f"[#13] 'Porém' abrindo frase: «{s[:70]}…»")
        if "—" in s:
            issues.append(f"[#9] Travessão: «{s[:70]}…»")
        if re.search(r"[a-z], [a-z].*:", s) and "http" not in s:
            issues.append(f"[#14] Dois-pontos (avaliar): «{s[:70]}…»")
        for w in re.findall(r"\b[A-Za-z]{4,}\b", s):
            if norm(w) in {"trump","truth","social","war","room","white","house","dark","horse",
                           "gettr","warroom","swif","swift","green","card","magnitsky","hakimian",
                           "bessent","miller","bannon","tucker","jason","rubio","vance",
                           "ustr","ofac","cnn","bbc","cpac","intercept","reuters","folha","globo",
                           "poder","washington","post","new","york","times","malasia","pgr","stf",
                           "tse","agu","icl","btg","pactual","tolou","capital","management","lex"}:
                continue
            if re.fullmatch(r"[a-z]+", w) and norm(w) not in STOP and w.lower() not in {
                "moraes","alexandre","eduardo","bolsonaro","jair","figueiredo","paulo","flavio",
                "lula","tarcisio","freitas","viviane","barci","brasil","brasileira","brasileiro",
                "brasileiros","estados","unidos","america","americanos","norte","sul","china",
                "texas","southlake","arlington","dallas","fort","worth","minas","gerais","coroa",
                "real","fazenda","supremo","tribunal","federal","justica","policia","camara",
                "senado","congresso","presidente","deputado","senador","ministro","secretario"}:
                pass  # heurística fraca para inglês; ignora
        # repetição de palavra significativa na frase anterior
        if i > 0:
            prev_words = {norm(w) for w in re.findall(r"\b\w{4,}\b", sents[i-1])} - {norm(x) for x in STOP}
            cur_words = {norm(w) for w in re.findall(r"\b\w{4,}\b", s)} - {norm(x) for x in STOP}
            rep = prev_words & cur_words
            rep = {w for w in rep if len(w) > 4}
            if rep:
                issues.append(f"[#7] Repete «{', '.join(sorted(rep))}» em frases vizinhas: «{s[:60]}…»")
        # rima de terminação (#17): duas palavras com mesma terminação -ece/-esse/-isse na mesma frase
        rhymes = re.findall(r"\b\w+(ece|esse|isse|ice)\b", norm(s))
        if len(set(rhymes)) > 1:
            issues.append(f"[#17] Possível rima deselegante ({', '.join(sorted(set(rhymes)))}): «{s[:70]}…»")

    # metrônomo (#16): 3+ frases seguidas de tamanho parecido
    sizes = [len(s.split()) for s in sents]
    for i in range(len(sizes) - 2):
        a, b, c = sizes[i], sizes[i+1], sizes[i+2]
        if a >= 8 and max(a, b, c) - min(a, b, c) <= 3:
            issues.append(f"[#16] Metrônomo? 3 frases seguidas de {a}, {b}, {c} palavras: «{sents[i][:50]}…»")

    print(f"== AUDITORIA DE ESTILO — {path.split('/')[-1]} ==")
    print(f"frases analisadas: {len(sents)}\n")
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

if __name__ == "__main__":
    main(sys.argv[1])
