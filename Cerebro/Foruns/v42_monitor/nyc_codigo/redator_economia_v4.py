#!/usr/bin/env python3
"""
redator_economia_v4.py - MÓDULO D: Motor de Teses & Redator Autônomo V4.2
==========================================================================
Transforma estatísticas primárias (banco_estatistico.sqlite3) em teses
jornalísticas d'O Cafezinho, seguindo o contrato editorial "Texto Música":

  REGRA INVIOLÁVEL — TODOS os parágrafos contêm ESTRITAMENTE DUAS FRASES.

Gera versão PT (O Cafezinho) e EN (Global South News) no mesmo ciclo.

Garantias anti-alucinação:
  - O LLM recebe um PACOTE FACIONAL fechado (série, último valor, variações)
    e é instruído a usar SOMENTE esses números.
  - Validação mecânica do contrato (2 frases/parágrafo, título limpo) com
    reintento em cascata (até 3 provedores) e reparo determinístico final.

Cascata de provedores (OpenAI-compatible, sem SDK): DeepSeek → OpenAI → Gemini.
"""

import os
import re
import sys
import json
import sqlite3
import logging
import urllib.request
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from env_loader import carregar_env
from banco_estatistico import BancoEstatistico

carregar_env()

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] [REDATOR-V42] %(message)s')

MAX_TENTATIVAS_LLM = 6  # REFORMA 03/09: validador factual mais rígido + gemini
                         # geo-bloqueado no NYC → 2 ciclos da cascata para não
                         # esgotar quando o modelo escorrega no contrato
TITULO_MAX = 80
FRASES_POR_PARAGRAFO = 2

# ---------------------------------------------------------------------------
# Frases: separador robusto com proteção de abreviações
# ---------------------------------------------------------------------------
_ABREV = [
    "US$", "R$", "sr.", "sra.", "srta.", "dr.", "dra.", "ex.", "p.", "pp.",
    "vs.", "num.", "no.", "nos.", "na.", "nas.", "art.", "inc.",
    "e.g.", "i.e.", "u.s.",
]


def separar_frases(texto: str) -> List[str]:
    """Divide parágrafo em frases protegendo abreviações comuns."""
    protegido = texto.strip()
    tokens: Dict[str, str] = {}
    for i, ab in enumerate(_ABREV):
        marcador = f"§ABR{i}§"
        padrao = re.escape(ab)
        if ab.endswith("."):
            padrao = re.escape(ab[:-1]) + r"\."
        protegido = re.sub(padrao, marcador, protegido, flags=re.IGNORECASE)
        tokens[marcador] = ab
    partes = re.split(r'(?<=[.!?…])\s+(?=[A-ZÀ-Ú0-9"“\(])', protegido)
    frases = []
    for p in partes:
        for marcador, ab in tokens.items():
            p = p.replace(marcador, ab)
        p = p.strip()
        if p:
            frases.append(p)
    return frases


def validar_texto_musica(paragrafos: List[str]) -> List[str]:
    """Retorna lista de violações do contrato Texto Música."""
    violacoes: List[str] = []
    if not paragrafos:
        return ["nenhum parágrafo"]
    for i, par in enumerate(paragrafos, 1):
        frases = separar_frases(par)
        if len(frases) != FRASES_POR_PARAGRAFO:
            violacoes.append(f"parágrafo {i} tem {len(frases)} frase(s); obrigatório {FRASES_POR_PARAGRAFO}")
    return violacoes


def validar_titulo(titulo: str) -> List[str]:
    violacoes = []
    t = titulo.strip()
    if len(t) < 10:
        violacoes.append("título curto demais")
    if len(t) > TITULO_MAX:
        violacoes.append(f"título com {len(t)} chars (máx {TITULO_MAX})")
    if re.search(r"[:—–…]", t):
        violacoes.append("título com dois-pontos/travessão/reticências")
    if len(t.split()) < 4:
        violacoes.append("título com menos de 4 palavras")
    return violacoes


def reparar_titulo(titulo: str) -> str:
    t = re.sub(r"[:—–…]", ",", titulo.strip())
    t = re.sub(r"\s+([,;])", r"\1", t)
    t = re.sub(r"\s+", " ", t)
    if len(t) > TITULO_MAX:
        cortado = t[:TITULO_MAX]
        if " " in cortado:
            cortado = cortado.rsplit(" ", 1)[0]
        t = cortado.rstrip(",; ")
    return t


def reparar_texto_musica(paragrafos: List[str]) -> List[str]:
    """Reparo determinístico de último recurso: achata as frases e reagrupa 2 a 2."""
    todas: List[str] = []
    for par in paragrafos:
        todas.extend(separar_frases(par))
    if len(todas) % 2 == 1:
        logging.warning("Reparo Texto Música: nº ímpar de frases — descartando a última.")
        todas = todas[:-1]
    return [" ".join(todas[i:i + 2]) for i in range(0, len(todas), 2)]


# ---------------------------------------------------------------------------
# REFORMA 03/09/2026 — validador factual mecânico (anti-alucinação)
# ---------------------------------------------------------------------------
_NUM_TXT = re.compile(
    r"(\d{1,3}(?:[.,]\d{1,3})?)\s*(bilh\w*|milh\w*|bi\b|mi\b|%)", re.IGNORECASE
)


def _para_float(txt_num: str) -> float:
    """'10,67' → 10.67 | '10.673' → 10673 (pt-BR: vírgula decimal, ponto milhar)."""
    txt_num = txt_num.strip()
    if "," in txt_num:
        return float(txt_num.replace(".", "").replace(",", "."))
    if "." in txt_num and len(txt_num.split(".")[-1]) == 3:
        return float(txt_num.replace(".", ""))  # 10.673 = milhar
    return float(txt_num)


def _candidatos_pacote(pacote: List[Dict[str, Any]]) -> Dict[str, List[float]]:
    """Valores citáveis por moeda: último_valor (normalizado em BI), variações %,
    e somas/diferências simples entre valores de MESMA moeda (p/ 'superávit de 4,26')."""
    base: Dict[str, List[float]] = {"USD": [], "EUR": [], "": [], "pct": []}
    pares: Dict[str, List[float]] = {"USD": [], "EUR": [], "": []}
    for f in pacote:
        moeda = f.get("moeda", "") or ""
        if moeda not in base:
            base[moeda] = []
            pares[moeda] = []
        try:
            v = float(f.get("ultimo_valor") or 0)
        except (TypeError, ValueError):
            continue
        # normaliza para BILHÕES quando a unidade é milhões
        un = str(f.get("unidade", "")).lower()
        v_bi = v / 1000.0 if "milh" in un else v
        base[moeda].append(v_bi)
        base[moeda].append(v)  # tolera o LLM escrever em milhões também
        # prosa cita magnitude de déficit/superávit ("déficit de 4,92") —
        # o sinal negativo do banco não pode bloquear o texto legítimo
        if v_bi < 0:
            base[moeda].append(abs(v_bi))
        for campo in ("variacao_periodo_anterior_pct", "variacao_12m_pct"):
            if f.get(campo) is not None:
                base["pct"].append(float(abs(f[campo])))
        pares[moeda].append(v_bi)
    for moeda, vals in pares.items():
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                base[moeda].append(abs(vals[i] - vals[j]))
    return base


def validar_afirmacoes_numericas(
    paragrafos: List[str], pacote: List[Dict[str, Any]], titulo: str = ""
) -> List[str]:
    """Todo número do texto (título incluso) precisa nascer do pacote: valor,
    variação %, ou soma/diferença de valores da mesma moeda. Pega também moeda
    trocada (US$ colado em valor de série em euros)."""
    violacoes: List[str] = []
    base = _candidatos_pacote(pacote)
    moedas_por_valor: Dict[float, set] = {}
    for moeda, vals in base.items():
        if moeda == "pct":
            continue
        for v in vals:
            moedas_por_valor.setdefault(round(v, 2), set()).add(moeda)

    texto = " ".join([titulo] + list(paragrafos))
    vistos: set = set()
    for m in _NUM_TXT.finditer(texto):
        bruto, escala = m.group(1), m.group(2).lower()
        try:
            n = _para_float(bruto)
        except ValueError:
            continue
        if n > 100000:  # valores brutos em milhões escritos por extenso raramente
            n_bi = n / 1000.0
        else:
            n_bi = n
        chave = (round(n_bi, 2), escala[:3])
        if chave in vistos:
            continue
        vistos.add(chave)

        eh_pct = escala.startswith("%") or escala == "%"
        janela = texto[max(0, m.start() - 12):m.start()]
        escrito_usd = bool(re.search(r"US\$|d[oó]lar", janela, re.IGNORECASE))
        escrito_eur = bool(re.search(r"euro", janela, re.IGNORECASE))

        if eh_pct:
            ok = any(abs(n - p) <= max(0.06, p * 0.02) for p in base["pct"])
            if not ok:
                # níveis de taxa cuja unidade JÁ é % (Selic 14% a.a., Fed 3,63%)
                niveis = [v for v in base.get("", []) if 0 < v < 100]
                ok = any(abs(n - v) <= max(0.02, v * 0.02) for v in niveis)
            if not ok:
                violacoes.append(f"percentual sem origem no pacote: {bruto}%")
            continue

        tol = max(0.02, n_bi * 0.012)
        moedas_aceitas = set()
        for moeda in ("USD", "EUR", ""):
            vals = base.get(moeda, [])
            if any(abs(n_bi - v) <= tol for v in vals):
                moedas_aceitas.add(moeda)
        if not moedas_aceitas:
            violacoes.append(f"número sem origem no pacote: {bruto} {escala}")
            continue
        if escrito_usd and moedas_aceitas == {"EUR"}:
            violacoes.append(f"US$ escrito sobre valor de série em euros: {bruto}")
        if escrito_eur and moedas_aceitas == {"USD"}:
            violacoes.append(f"'euros' escrito sobre valor de série em dólares: {bruto}")
    return violacoes[:8]


def jaccard_palavras(a: str, b: str) -> float:
    pa = {w.strip(".,:;!?\"'()").lower() for w in a.split() if len(w) > 2}
    pb = {w.strip(".,:;!?\"'()").lower() for w in b.split() if len(w) > 2}
    if not pa or not pb:
        return 0.0
    return len(pa & pb) / len(pa | pb)


# ---------------------------------------------------------------------------
# Pacote factual (autoridade mecânica: só números do banco)
# ---------------------------------------------------------------------------
class ConstrutorFactual:
    def __init__(self, db: Optional[BancoEstatistico] = None):
        self.db = db or BancoEstatistico()

    def resumo_serie(self, fonte: str, serie_id: str, limite: int = 24) -> Optional[Dict[str, Any]]:
        # BUGFIX 26/08/2026 (ordem Miguel): obter_serie_historica ordena ASC com LIMIT,
        # então séries com mais de `limite` observações devolviam a janela mais ANTIGA
        # e o "último valor" saía defasado (caso real: dez/2025 no lugar de jul/2026).
        # Busca a série completa e fatia os `limite` meses MAIS RECENTES.
        serie = self.db.obter_serie_historica(fonte, serie_id, limite=1000)
        serie = [s for s in serie if s["data_referencia"] <= datetime.now(timezone.utc).strftime("%Y-%m-%d")]
        if not serie:
            return None
        serie.sort(key=lambda s: s["data_referencia"])
        serie = serie[-limite:]
        ultimo = serie[-1]
        resumo: Dict[str, Any] = {
            "fonte": fonte,
            "serie_id": serie_id,
            "serie_nome": ultimo["serie_nome"],
            "unidade": ultimo["unidade"],
            "ultima_data": ultimo["data_referencia"],
            "ultimo_valor": ultimo["valor"],
            "observacoes": len(serie),
            "observacao_hash": ultimo["hash_id"],
        }
        # REFORMA 03/09/2026 (auditoria DSC): idade e defasagem explícitas no pacote —
        # série parada (>90 dias) NUNCA pode ser tratada como dado corrente.
        try:
            d_ult = datetime.strptime(str(ultimo["data_referencia"])[:10], "%Y-%m-%d").date()
            hoje = datetime.now(timezone.utc).date()
            resumo["idade_dias"] = (hoje - d_ult).days
        except Exception:
            resumo["idade_dias"] = None
        resumo["defasada"] = bool(resumo.get("idade_dias") is not None and resumo["idade_dias"] > 90)
        moeda = str(ultimo.get("unidade", "")).upper()
        if "EUR" in moeda:
            resumo["moeda"] = "EUR"
        elif "US$" in moeda or "USD" in moeda:
            resumo["moeda"] = "USD"
        else:
            resumo["moeda"] = ""
        if len(serie) >= 2:
            anterior = serie[-2]
            if anterior["valor"]:
                resumo["variacao_periodo_anterior_pct"] = round(
                    (ultimo["valor"] - anterior["valor"]) / abs(anterior["valor"]) * 100, 2
                )
        if len(serie) >= 13:
            ano_atras = serie[-13]
            if ano_atras["valor"]:
                resumo["variacao_12m_pct"] = round(
                    (ultimo["valor"] - ano_atras["valor"]) / abs(ano_atras["valor"]) * 100, 2
                )
        return resumo

    def montar_pacote(self, refs: List[Tuple[str, str]]) -> List[Dict[str, Any]]:
        pacote = []
        for fonte, serie_id in refs:
            r = self.resumo_serie(fonte, serie_id)
            if r:
                pacote.append(r)
        return pacote


# ---------------------------------------------------------------------------
# Motor de Teses
# ---------------------------------------------------------------------------
TESES: Dict[str, Dict[str, Any]] = {
    "comercio_sul_sul": {
        "titulo_tese": "Comércio Sul-Sul e a Centralidade da China",
        "angulo": (
            "O crescimento do comércio Brasil-China e a força do eixo Sul-Sul, "
            "com a China mantendo superávits comerciais recordes com o mundo e a "
            "balança brasileira sustentada por commodities e manufaturados para a Ásia."
        ),
        "series": [
            ("COMEXSTAT", "COMEX_EXPORT_CHINA"),
            ("COMEXSTAT", "COMEX_IMPORT_CHINA"),
            ("COMEXSTAT", "COMEX_EXPORT_TOTAL"),
            ("COMEXSTAT", "COMEX_IMPORT_TOTAL"),
            ("GACC", "GACC_CHINA_BALANCE"),
            ("EUROSTAT", "EUROSTAT_BALANCA_EXTRAUE"),
            ("FRED", "USTRADE"),
        ],
        "graficos": [
            {"fonte": "COMEXSTAT", "serie_id": "COMEX_EXPORT_CHINA", "tipo": "line",
             "legenda": "Exportações brasileiras para a China, mês a mês"},
            {"fonte": "GACC", "serie_id": "GACC_CHINA_BALANCE", "tipo": "bar",
             "legenda": "Balança comercial da China com o mundo (dados GACC)"},
            {"fonte": "FRED", "serie_id": "USTRADE", "tipo": "line",
             "legenda": "Saldo comercial dos Estados Unidos (bens e serviços)"},
        ],
    },
    "politica_monetaria_comparada": {
        "titulo_tese": "O Custo de Carregar os Juros Mais Altos do Mundo",
        "angulo": (
            "A taxa básica de juros do Brasil (Selic) roda quase quatro vezes a dos Estados "
            "Unidos. Essa diferença segura o câmbio na linha, mas cobra um preço altíssimo do "
            "país: juros caríssimos na dívida pública, crédito caro para empresa e família e "
            "renda garantida ao rentismo. A linha do jornal: reduzir os juros é tarefa "
            "histórica do Brasil; enaltecer o juro alto é PROIBIDO."
        ),
        "series": [
            ("BCB", "BCB_432"),
            ("FRED", "FEDFUNDS"),
            ("BCB", "BCB_1"),
        ],
        "graficos": [
            # Selic é diária: 260 pontos ≈ 12 meses — janela que conta a história do ano
            # (24 pontos ≈ 1 mês era achatado e sem informação; lição 27/08).
            {"fonte": "BCB", "serie_id": "BCB_432", "tipo": "line", "limit": 260,
             "legenda": "Taxa básica de juros do Brasil (Selic), últimos 12 meses"},
            {"fonte": "FRED", "serie_id": "FEDFUNDS", "tipo": "line",
             "legenda": "Taxa básica de juros dos Estados Unidos (Fed)"},
        ],
    },
    "inflacao_primaria": {
        "titulo_tese": "Inflação Primária e Poder de Compra",
        "angulo": (
            "O comportamento do IPCA frente ao câmbio: pressão importada ou doméstica."
        ),
        "series": [
            ("BCB", "BCB_433"),
            ("IBGE", "IBGE_IPCA_GERAL"),
            ("BCB", "BCB_1"),
        ],
        "graficos": [
            {"fonte": "BCB", "serie_id": "BCB_433", "tipo": "bar",
             "legenda": "IPCA variação mensal"},
        ],
    },
}


def escolher_tese(
    pacote_factual: List[Dict[str, Any]],
    tema: str = "auto",
    dias_desde_ultima: Optional[Dict[str, int]] = None,
) -> str:
    """REFORMA 03/09/2026 (auditoria DSC): a versão antiga retornava SEMPRE
    comercio_sul_sul (primeira série sempre presente no pacote amplo) — daí 6
    matérias seguidas com os mesmos números e título repetido (posts 400168 a
    400265 do espelho). Agora: só entram teses com dado FRESCO (idade ≤
    TeseSel.LIMITE_FRESCO dias); entre as elegíveis, ganha a que está há mais
    tempo sem publicar (rodízio); empate → dado mais novo. Sem elegível, cai a
    mais fresca (o gate de publicação decide se vira post)."""
    if tema != "auto" and tema in TESES:
        return tema
    dias_desde_ultima = dias_desde_ultima or {}

    def _idade_minima(tese_id: str) -> Optional[int]:
        refs = {(f["fonte"], f["serie_id"]) for f in pacote_factual}
        idades = [
            f["idade_dias"] for f in pacote_factual
            if f.get("idade_dias") is not None
            and (f["fonte"], f["serie_id"]) in set(TESES[tese_id]["series"]) & refs
        ]
        return min(idades) if idades else None

    cand: List[tuple] = []
    for tese_id in TESES:
        idade = _idade_minima(tese_id)
        if idade is None:
            continue
        cand.append((tese_id, idade))
    if not cand:
        return "politica_monetaria_comparada"

    LIMITE_FRESCO = 45  # dias — dado mais velho que isso não é pauta do dia
    elegiveis = [(t, i) for t, i in cand if i <= LIMITE_FRESCO]
    pool = elegiveis or cand
    pool.sort(key=lambda ti: (-dias_desde_ultima.get(ti[0], 9999), ti[1]))
    tese_escolhida = pool[0][0]
    logging.info(
        f"escolher_tese (reforma): eleitas={[(t, i) for t, i in pool]} → {tese_escolhida} "
        f"(rodízio={dias_desde_ultima.get(tese_escolhida, '?')}d sem publicar; "
        f"elegíveis_frescas={[t for t, i in elegiveis]})"
    )
    return tese_escolhida


# ---------------------------------------------------------------------------
# Cascata LLM (OpenAI-compatible via urllib, sem SDK)
# ---------------------------------------------------------------------------
PROVEDORES = [
    {
        "nome": "deepseek",
        "base_url": "https://api.deepseek.com/v1/chat/completions",
        "modelo": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
    },
    {
        "nome": "openai",
        "base_url": "https://api.openai.com/v1/chat/completions",
        "modelo": "gpt-4o-mini",
        "env_key": "OPENAI_API_KEY",
    },
    {
        "nome": "gemini",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
        "modelo": "gemini-2.5-flash",
        "env_key": "GEMINI_API_KEY",
    },
]

SYSTEM_PROMPT = """Você é o redator econômico sênior do jornal brasileiro O Cafezinho, \
um veículo progressista, soberanista e comprometido com a análise séria de dados primários.
Você recebe um PACOTE FACIONAL com números reais de fontes oficiais (BCB, IBGE, ComexStat, \
FRED, Eurostat, GACC). Use SOMENTE os números fornecidos. NUNCA invente, extrapole ou cite \
números fora do pacote. Você pode contextualizar com conhecimento geral de economia \
(história, mecanismos, geopolítica), mas todo dado quantitativo deve vir do pacote.

CONTRATO EDITORIAL "TEXTO MÚSICA" (INVIOLÁVEL):
1. TODOS os parágrafos devem conter ESTRITAMENTE DUAS FRASES. Nem uma, nem três. Exatamente duas.
2. Escreva entre 6 e 9 parágrafos (portanto 12 a 18 frases no total).
3. Ritmo jornalístico: alterne frases curtas e médias; cada parágrafo avança o argumento.
4. Título: máximo 80 caracteres, sem dois-pontos, sem travessão, sem reticências, mínimo 4 palavras.
5. Tom: analítico, firme, com perspectiva do Sul Global; sem sensacionalismo.
6. A versão em INGLÊS é um relatório executivo jornalístico para o portal Global South News, \
com o MESMO contrato de duas frases por parágrafo.
7. SEMPRE cite o período completo com o ANO (ex.: "em julho de 2026", "no acumulado de janeiro a julho de 2026"). \
NUNCA escreva um mês solto sem o ano ("em dezembro" é PROIBIDO).

DIRETRIZ HISTORIAL O CAFEZINHO (INVIOLÁVEL — ordem do editor, 27/08/2026):
8. A linha do jornal é CONTRA a taxa de juros alta. O Brasil carrega juros entre os mais altos \
do mundo e isso é um entrave histórico ao desenvolvimento, não uma virtude. NUNCA elogie, \
endeuse ou trate juros altos como âncora boa, mérito ou conquista ("o juro alto segura o real \
e isso é bom" é PROIBIDO como enquadramento positivo).
9. Sempre que os dados mostrarem efeito "benéfico" do juro alto (câmbio estável, entrada de \
capital), apresente o CUSTO do outro lado no MESMO parágrafo ou no seguinte: rolagem caríssima \
da dívida pública, crédito caro para empresa e família, freio no investimento e no emprego, \
renda garantida ao rentismo. Cortes de juros = avanço; altas de juros = agravamento do custo.
10. SIGLAS: leitor popular. Na PRIMEIRA menção, sempre por extenso — "Banco Central dos Estados \
Unidos (Fed)", "taxa oficial do dólar (PTAX)", "inflação oficial (IPCA)", "taxa básica de juros \
(Selic)". Depois pode repetir a sigla. NUNCA abra parágrafo com sigla crua não explicada.
11. Linguagem jornalística, não acadêmica: nada de jargão de mercado ("apetite de risco", \
"fluxo de capitais", "prêmio de risco") sem tradução em português simples. Escreva para o \
leitor comum que paga a conta dos juros.

REGRAS ANTI-ALUCINAÇÃO (REFORMA 03/09/2026 — cada uma nasceu de um defeito real publicado):
12. MOEDA: cada série do pacote diz a moeda certa (US$ milhões, EUR milhões). Valor em EUR é \
"bilhões de euros"/"milhões de euros" — JAMAIS "US$" em cima de número de série em euros \
(defeito real: déficit da UE publicado como US$ num post e como euros no outro).
13. JANELA: todo valor do pacote é MENSAL (ou diário, se a data muda todo dia no pacote). \
Escreva "em julho de 2026", NUNCA "no acumulado de doze meses" para um valor mensal \
(defeito real: US$ 34,12 bi mensais publicados como "acumulado de 12 meses"). Só use \
"acumulado"/"em 12 meses" com os campos variacao_12m_pct/variacao_periodo_anterior_pct.
14. DADO DEFASADO: série com "defasada": true ou idade_dias alto (>90) só pode ser citada \
com a data explícita no corpo ("dados até fevereiro de 2026") e JAMAIS como recorde ou \
situação corrente ("mantém superávit recorde" para dado de fevereiro num texto de julho \
é PROIBIDO).
15. SEM ECO: não repita o mesmo número ou o mesmo fato em frases consecutivas nem no \
título+1ª frase+2ª frase (defeito real: matéria abria com US$ 10,67 bilhões três vezes \
seguidas). Cada parágrafo traz INFORMAÇÃO NOVA.
16. TÍTULO INÉDITO: se o prompt listar "títulos a evitar", seu título deve ser claramente \
diferente deles em palavras e estrutura (defeito real: dois posts com título idêntico \
em dias diferentes).
17. TÍTULO EM FRASE: caixa normal de frase (sentence case) — PROIBIDO capitalizar cada \
palavra ("Análise Do IPCA E A Influência..."). Frase declarativa com o fato central, \
nunca rótulo genérico ("Análise de...", "Panorama de...", "O comportamento de...").
18. ABERTURA É FATO: a primeira frase do primeiro parágrafo afirma o fato central com \
número e período. PROIBIDA frase-moldura vazia antes do dado ("o comportamento de X \
revela Y", "o dado reflete a pressão...") — é enchimento.
19. TAXA QUE MUDOU: quando uma taxa cai de A para B, escreva "de A para B" (ou "recuou \
para B"); NUNCA "queda de X% na variação" (percentual do percentual confunde o leitor).

Responda APENAS com um objeto JSON válido (sem markdown, sem comentários), exatamente assim:
{
  "titulo_pt": "...",
  "resumo_pt": "resumo de 1 frase para o excerpt",
  "paragrafos_pt": ["Frase um. Frase dois.", "..."],
  "titulo_en": "...",
  "resumo_en": "one-sentence excerpt",
  "paragrafos_en": ["Sentence one. Sentence two.", "..."]
}"""


def _extrair_json(texto: str) -> Optional[Dict[str, Any]]:
    texto = texto.strip()
    texto = re.sub(r"^```(?:json)?\s*", "", texto)
    texto = re.sub(r"\s*```$", "", texto)
    inicio = texto.find("{")
    if inicio < 0:
        return None
    profundidade = 0
    for i in range(inicio, len(texto)):
        if texto[i] == "{":
            profundidade += 1
        elif texto[i] == "}":
            profundidade -= 1
            if profundidade == 0:
                try:
                    obj = json.loads(texto[inicio:i + 1])
                    return obj if isinstance(obj, dict) else None
                except json.JSONDecodeError:
                    return None
    return None


def chamar_llm(provedor: Dict[str, str], system: str, user: str) -> Tuple[Optional[str], str]:
    chave = os.environ.get(provedor["env_key"], "")
    if not chave:
        return None, "chave ausente"
    payload = {
        "model": provedor["modelo"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.7,
        "max_tokens": 4000,
    }
    req = urllib.request.Request(
        provedor["base_url"],
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {chave}",
            "User-Agent": "OCafezinho-V42-Redator/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            dados = json.loads(resp.read().decode("utf-8"))
            conteudo = dados.get("choices", [{}])[0].get("message", {}).get("content", "")
            return conteudo, ""
    except urllib.error.HTTPError as e:
        corpo = ""
        try:
            corpo = e.read().decode("utf-8")[:200]
        except Exception:
            pass
        return None, f"HTTP {e.code}: {corpo}"
    except Exception as e:
        return None, str(e)


def _validar_estrutura(obj: Dict[str, Any]) -> List[str]:
    erros = []
    for campo in ("titulo_pt", "resumo_pt", "paragrafos_pt", "titulo_en", "resumo_en", "paragrafos_en"):
        if campo not in obj:
            erros.append(f"campo ausente: {campo}")
    for campo_par in ("paragrafos_pt", "paragrafos_en"):
        pars = obj.get(campo_par)
        if not isinstance(pars, list) or not pars or not all(isinstance(p, str) and p.strip() for p in pars):
            erros.append(f"{campo_par} deve ser lista de strings não vazias")
    return erros


class RedatorTextoMusica:
    def __init__(self):
        self.factual = ConstrutorFactual()

    def redigir(
        self,
        tema: str = "auto",
        titulos_evitar: Optional[List[str]] = None,
        dias_desde_ultima: Optional[Dict[str, int]] = None,
    ) -> Dict[str, Any]:
        """Ciclo completo: tese → pacote factual → redação validada PT+EN.

        REFORMA 03/09/2026: `titulos_evitar` carrega os títulos das últimas
        matérias publicadas (regra 16 + gate do ciclo) e `dias_desde_ultima`
        alimenta o rodízio de teses do escolher_tese."""
        # 1. Pacote factual amplo (todas as séries candidatas das teses)
        refs_unicas: List[Tuple[str, str]] = []
        for tese in TESES.values():
            for ref in tese["series"]:
                if ref not in refs_unicas:
                    refs_unicas.append(ref)
        pacote_completo = self.factual.montar_pacote(refs_unicas)
        if not pacote_completo:
            raise RuntimeError("Nenhuma série disponível no banco estatístico")

        # 2. Escolha da tese e filtro do pacote
        tese_id = escolher_tese(pacote_completo, tema, dias_desde_ultima)
        tese = TESES[tese_id]
        refs_tese = set(tese["series"])
        pacote = [f for f in pacote_completo if (f["fonte"], f["serie_id"]) in refs_tese]
        if not pacote:
            pacote = pacote_completo[:3]

        # 3. Prompt do usuário com o pacote factual
        bloco_evitar = ""
        if titulos_evitar:
            lista = "\n".join(f"  - {t}" for t in titulos_evitar[:8])
            bloco_evitar = (
                "\n\nTÍTULOS A EVITAR (já publicados; o seu título deve ser "
                f"inequívoca e estruturalmente diferente):\n{lista}\n"
            )
        user_prompt = (
            f"TESE EDITORIAL: {tese['titulo_tese']}\n"
            f"ÂNGULO: {tese['angulo']}\n\n"
            f"PACOTE FACIONAL (use SOMENTE estes números):\n"
            f"{json.dumps(pacote, ensure_ascii=False, indent=2)}\n"
            f"{bloco_evitar}\n"
            "Escreva agora a matéria completa em PT e a versão executiva em EN, "
            "respeitando RIGOROSAMENTE o contrato Texto Música (2 frases por parágrafo). "
            "Responda somente com o JSON especificado."
        )

        # 4. Cascata de provedores com reintento e feedback de violações
        feedback = ""
        resultado: Optional[Dict[str, Any]] = None
        provedor_usado, modelo_usado = "", ""
        for tentativa in range(1, MAX_TENTATIVAS_LLM + 1):
            provedor = PROVEDORES[(tentativa - 1) % len(PROVEDORES)]
            system = SYSTEM_PROMPT + (f"\n\nATENÇÃO — TENTATIVA DE CORREÇÃO: a versão anterior "
                                      f"violou o contrato:\n{feedback}\nCorrija mantendo o conteúdo."
                                      if feedback else "")
            logging.info(f"Tentativa {tentativa}: provedor={provedor['nome']} modelo={provedor['modelo']}")
            conteudo, erro = chamar_llm(provedor, system, user_prompt)
            if erro:
                logging.warning(f"Falha no provedor {provedor['nome']}: {erro}")
                continue
            obj = _extrair_json(conteudo or "")
            if obj is None:
                feedback = "A resposta não era um JSON válido. Responda APENAS com o objeto JSON."
                provedor_usado, modelo_usado = provedor["nome"], provedor["modelo"]
                continue

            erros = _validar_estrutura(obj)
            if not erros:
                viol_pt = validar_texto_musica(obj["paragrafos_pt"])
                viol_en = validar_texto_musica(obj["paragrafos_en"])
                viol_tit = validar_titulo(obj["titulo_pt"]) + validar_titulo(obj["titulo_en"])
                # REFORMA 03/09: validador factual mecânico (anti-alucinação) no PT
                viol_num = validar_afirmacoes_numericas(
                    obj["paragrafos_pt"], pacote, obj["titulo_pt"])
                if not viol_pt and not viol_en and not viol_tit and not viol_num:
                    resultado = obj
                    provedor_usado, modelo_usado = provedor["nome"], provedor["modelo"]
                    logging.info(f"✅ Contrato Texto Música cumprido na tentativa {tentativa}.")
                    break
                feedback = ("; ".join(viol_pt + viol_en + viol_tit + viol_num))[:1500]
                logging.warning(f"Violações na tentativa {tentativa}: {feedback[:300]}")
                provedor_usado, modelo_usado = provedor["nome"], provedor["modelo"]
            else:
                feedback = "; ".join(erros)[:1500]
                provedor_usado, modelo_usado = provedor["nome"], provedor["modelo"]

        if resultado is None:
            raise RuntimeError("Redator esgotou as tentativas sem JSON estruturalmente válido")

        # 5. Reparo mecânico final (último recurso, garante o contrato)
        reparos = []
        if validar_titulo(resultado["titulo_pt"]):
            resultado["titulo_pt"] = reparar_titulo(resultado["titulo_pt"])
            reparos.append("titulo_pt")
        if validar_titulo(resultado["titulo_en"]):
            resultado["titulo_en"] = reparar_titulo(resultado["titulo_en"])
            reparos.append("titulo_en")
        if validar_texto_musica(resultado["paragrafos_pt"]):
            resultado["paragrafos_pt"] = reparar_texto_musica(resultado["paragrafos_pt"])
            reparos.append("paragrafos_pt")
        if validar_texto_musica(resultado["paragrafos_en"]):
            resultado["paragrafos_en"] = reparar_texto_musica(resultado["paragrafos_en"])
            reparos.append("paragrafos_en")
        if reparos:
            logging.warning(f"Reparo mecânico aplicado em: {reparos}")

        # Garantia final fail-closed
        assert not validar_texto_musica(resultado["paragrafos_pt"]), "contrato PT violado pós-reparo"
        assert not validar_texto_musica(resultado["paragrafos_en"]), "contrato EN violado pós-reparo"

        return {
            "tese_id": tese_id,
            "tese_titulo": tese["titulo_tese"],
            "pacote_factual": pacote,
            "graficos_planejados": tese["graficos"],
            "provedor": provedor_usado,
            "modelo": modelo_usado,
            "reparos_mecanicos": reparos,
            **resultado,
        }


if __name__ == "__main__":
    redator = RedatorTextoMusica()
    saida = redator.redigir(tema="auto")
    print(json.dumps({k: v for k, v in saida.items() if k != "pacote_factual"},
                     ensure_ascii=False, indent=2))
