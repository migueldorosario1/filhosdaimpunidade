#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v42_checagens.py — checagens mecânicas anti-alucinação do Vigia V4.2 (us65).

Lê um post JÁ PÚBLICO do espelho (categoria Estatística 100005) e confere:
  1. números do texto × rodapé "Fontes primárias" (valor/variação/soma-diferença);
  2. moeda trocada (US$ × série em euros);
  3. eco de título com posts anteriores (Jaccard ≥ 0,6 — defeito real: posts
     400178 e 400265 com título idêntico);
  4. série defasada (>90 dias) tratada como corrente ("recorde"/"mantém" perto
     de valor velho — defeito real: GACC de fevereiro chamado de recorde em
     texto de julho).

Mesmo motor lógico do validador implantado no NYC (redator_economia_v4.py,
REFORMA 03/09/2026) — aqui de forma autônoma, fazendo parse do rodapé do post.
O código vive no repo de propósito: DSN Ideias revisa e propõe melhorias.
"""
import re
from datetime import date
from html import unescape

HOJE = date.today()

_NUM_TXT = re.compile(
    r"(\d{1,3}(?:[.,]\d{1,3})?)\s*(bilh\w*|milh\w*|bi\b|mi\b|%)", re.IGNORECASE)
_LINHA_FONTE = re.compile(
    r"(?P<nome>.*?)\((?P<fonte>[A-Z]{2,10})/(?P<serie>[A-Z0-9_]+)\)\s*[—-]\s*"
    r"último:\s*(?P<valor>-?[\d.,]+)\s+(?P<unidade>.+?)\s+em\s+(?P<data>\d{4}-\d{2}-\d{2})",
    re.IGNORECASE)
# formato antigo (posts até 28/08): "BCB/BCB_432: último 14.0 % a.a. em 2026-08-27"
_LINHA_FONTE_ANTIGA = re.compile(
    r"(?P<fonte>[A-Z]{2,10})/(?P<serie>[A-Z0-9_]+):\s+último\s+"
    r"(?P<valor>-?[\d.,]+)\s+(?P<unidade>.+?)\s+em\s+(?P<data>\d{4}-\d{2}-\d{2})",
    re.IGNORECASE)


def extrair_texto(html: str) -> str:
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html or "", flags=re.S)
    txt = re.sub(r"<[^>]+>", " ", html)
    return unescape(re.sub(r"\s+", " ", txt)).strip()


def _para_float(txt_num: str) -> float:
    txt_num = txt_num.strip()
    if "," in txt_num:
        return float(txt_num.replace(".", "").replace(",", "."))
    if "." in txt_num and len(txt_num.split(".")[-1]) == 3:
        return float(txt_num.replace(".", ""))
    return float(txt_num)


def parse_fontes(texto: str) -> list:
    """Extrai do rodapé 'Fontes primárias' as séries citáveis."""
    achados = []
    bloco = texto[texto.find("Fontes primárias"):] if "Fontes primárias" in texto else texto
    matches = list(_LINHA_FONTE.finditer(bloco))
    if not matches:  # rodapé antigo
        matches = list(_LINHA_FONTE_ANTIGA.finditer(bloco))
    for m in matches:
        try:
            valor = _para_float(m.group("valor"))
        except ValueError:
            continue
        unidade = m.group("unidade").strip()
        serie = f'{m.group("fonte")}/{m.group("serie")}'
        achados.append({
            "serie": serie,
            "nome": m.groupdict().get("nome", serie) or serie,
            "valor": valor,
            "unidade": unidade,
            "data": m.group("data"),
            "moeda": "EUR" if "EUR" in unidade.upper() else
                     ("USD" if ("US$" in unidade or "USD" in unidade.upper()) else ""),
            "idade_dias": (HOJE - date.fromisoformat(m.group("data"))).days,
            "defasada": (HOJE - date.fromisoformat(m.group("data"))).days > 90,
            "pct": "%" in unidade,
        })
    return achados


def candidatos_do_rodape(fontes: list) -> dict:
    """Valores citáveis por moeda (em BI e cru) + percentuais + somas/diferenças."""
    base = {"USD": [], "EUR": [], "": [], "pct": []}
    pares = {"USD": [], "EUR": [], "": []}
    for f in fontes:
        moeda = f["moeda"] if f["moeda"] in base else ""
        v = f["valor"]
        un = f["unidade"].lower()
        v_bi = v / 1000.0 if "milh" in un else v
        if f["pct"]:
            base["pct"].append(abs(v))
        else:
            base[moeda].extend([v_bi, v] + ([abs(v_bi)] if v_bi < 0 else []))
            pares[moeda].append(abs(v_bi))
    for moeda, vals in pares.items():
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                base[moeda].append(abs(vals[i] - vals[j]))
    return base


def checar_numeros(texto: str, cand: dict) -> list:
    """Número fora do rodapé = problema. US$ em valor de série em euros = problema."""
    problemas = []
    vistos = set()
    for m in _NUM_TXT.finditer(texto):
        bruto, escala = m.group(1), m.group(2).lower()
        try:
            n = _para_float(bruto)
        except ValueError:
            continue
        # escala manda na conversão p/ bilhões (não o tamanho do número)
        if escala.startswith("bilh") or escala == "bi":
            n_bi = n
        elif escala.startswith("milh") or escala == "mi":
            n_bi = n / 1000.0
        else:  # "%"
            n_bi = n
        chave = (round(n_bi, 2), escala[:3])
        if chave in vistos:
            continue
        vistos.add(chave)
        if escala.startswith("%"):
            # variação % da série NÃO vem no rodapé (só o último valor) —
            # inviável validar mecanicamente aqui; o NYC valida na geração com
            # o pacote completo. Vigia só marca o absurdo (>1000% ou negativo
            # escrito como alta). O veredito LLM julga o resto contextualmente.
            if n > 1000:
                problemas.append(f"percentual implausível no texto: {bruto}%")
            continue
        tol = max(0.02, n_bi * 0.012)
        janela = texto[max(0, m.start() - 12):m.start()]
        usd = bool(re.search(r"US\$|d[oó]lar", janela, re.IGNORECASE))
        eur = bool(re.search(r"euro", janela, re.IGNORECASE))
        moedas = set()
        for moeda in ("USD", "EUR", ""):
            if any(abs(n_bi - v) <= tol for v in cand.get(moeda, [])):
                moedas.add(moeda)
        if not moedas:
            problemas.append(f"número sem origem no rodapé: {bruto} {escala}")
        elif usd and moedas == {"EUR"}:
            problemas.append(f"US$ sobre valor de série em euros: {bruto}")
        elif eur and moedas == {"USD"}:
            problemas.append(f"'euros' sobre valor de série em dólares: {bruto}")
    return problemas[:8]


def _palavras(t: str) -> set:
    return {w.strip(".,:;!?\"'()").lower() for w in t.split() if len(w) > 2}


def checar_titulo_eco(titulo: str, anteriores: list, limiar: float = 0.6) -> str:
    """`anteriores`: [(id, titulo, texto)]. Retorna string de problema ou ''."""
    pt = _palavras(titulo)
    if not pt:
        return ""
    pior_j, pior_id = 0.0, None
    for pid, t, _ in anteriores:
        pt_other = _palavras(t)
        pj = len(pt & pt_other) / len(pt | pt_other) if pt_other else 0.0
        if pj > pior_j:
            pior_j, pior_id = pj, pid
    if pior_j >= limiar:
        return f"título em eco com post {pior_id} (Jaccard {pior_j:.2f})"
    return ""


def checar_defasados(texto: str, fontes: list) -> list:
    """Série >90 dias citada como corrente/recorde sem aviso de defasagem."""
    problemas = []
    trecho = re.sub(r"\s+", " ", texto)
    for f in fontes:
        if not f["defasada"]:
            continue
        padrao_valor = re.escape(f"{abs(f['valor']):.2f}".rstrip("0").rstrip("."))
        if not padrao_valor:
            continue
        for m in re.finditer(padrao_valor, trecho):
            volta = trecho[max(0, m.start() - 160):m.end() + 160]
            aviso = re.search(r"dados até|até (janeiro|fevereiro|março|abril|maio|junho|"
                              r"julho|agosto|setembro|outubro|novembro|dezembro)", volta, re.IGNORECASE)
            if not aviso and re.search(r"recorde|mantém|segue com|acumula", volta, re.IGNORECASE):
                problemas.append(
                    f"série defasada {f['serie']} (dados de {f['data']}) tratada como corrente/recorde")
                break
    return problemas[:4]
