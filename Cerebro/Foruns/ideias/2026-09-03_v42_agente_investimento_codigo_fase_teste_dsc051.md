# 💻 RASCUNHO DE CÓDIGO — V4.2 "CAFEZINHO INVESTIMENTO" FASE DE TESTE (DSC-20260902-051 · ordem Miguel → DS-N Ideias)

> **Encomenda:** DSC-20260902-051 (02/09 20:2x BRT, postada em `de_dell.md`; commit 005c29941 03/09 00:05) — **ORDEM DO MIGUEL (~20:1x-20:2x, chat):** *"Vamos terminar, vamos implementar esse V4.2 de investimento com agentes baratos pra gente testar. Manda o Ideias refazer com essa crítica [varredura, DSC-050] e CODAR — fazer um agente e colocar em produção em período de TESTE com modelo baratinho: Qwen Flash (pode ser GLM Flash também, baratinho) e Qwen-VL pra visão também. Manda começar a rodar teste. Deixa ele bem SIMPLES e ELEGANTE."*
> **Despacho da ordem (divisão de ofícios):** (1) **DS-N IDEIAS** — (a) incorporar a VARREDURA (DSC-050) no desenho [FEITO 23:46 — v1.1 do design] + (b) **ENTREGAR O CÓDIGO** do agente (simples e elegante, pipeline único varredura → pauta → escuta dirigida → tese → redação → meta `_v42_*`, pilha barata: **qwen3.8-flash motor principal · glm flash/turbo reserva · qwen3-vl p/ visão; frontier PROIBIDO nesta fase**, nem na tese) + (c) cron de teste proposto + checklist de deploy + (d) critérios de sucesso do teste · (2) **DSC + ZM** — instalação/deploy no tencent (espelho), MODO TESTE = só RASCUNHOS, nada publicado; publicação segue o caminho único v3 e só com ✓ do Miguel · (3) **Chefe** — vigiar o teste (custo ~zero esperado — Token Plan) · (4) **Disciplina "simples e elegante":** 1 script, sem dependência nova, sem mexer na esteira V4.1, rollback = desligar o cron. Primeira versão NÃO precisa de tudo do desenho — mínima que prove o ciclo.
> **Natureza:** RASCUNHO DE CÓDIGO dentro do arquivo da ideia (regra da casa) — **NADA em produção**. Execução/deploy = DSC + ZM (item 2 do despacho), só após ✓ do Miguel. Eu não instalo, não rodo, não publico (Lei de Poderes).
> **Arquivos irmãos:** design V4.2 v1.1 → `2026-09-02_v42_agente_analise_investimento.md` (C0a VARREDURA incorporada 23:46) · banco de fontes ★ → `2026-09-02_banco_fontes_investimento_geopolitica_estrelas.md` · minuta da constituição ideológica → `2026-09-02_minuta_constituicao_ideologica_cafezinho.md`.

---

## 0. SÍNTESE (o que este arquivo entrega)

1. **Um único script** (`v42_analise_teste.py`, rascunho abaixo) que prova o ciclo mínimo do V4.2: **C0a varredura (4 feixes) → C0 pauta → C1 escuta dirigida leve (feeds do banco ★) → C3 tese → C4 redação → grava rascunho no WP com meta `_v42_*`** — MODO TESTE: post_status `draft`, NUNCA `publish`.
2. **Pilha 100% barata nesta fase (regra DSC-051):** qwen3.8-flash (Token Plan, custo marginal ~0) como motor principal; glm flash/turbo como reserva; qwen3-vl só quando precisar de visão (capa/gráfico). **Frontier PROIBIDO — nem na tese** (o design v1.1 previa frontier na C3; a DSC-051 reduz para a fase de teste: a tese também sai no barato; se a qualidade não fechar, o teste MEDE isso e o relatório sobe ao Miguel).
3. **Cron de teste proposto:** 1 ciclo/dia ~14:00 (varredura+pipeline → rascunho pronto ~15:00) — fica FORA da esteira V4.1, não disputa janela de publicação.
4. **Critérios de sucesso objetivos** (§4): o que o teste mede e a régua de "passou".
5. **Nada executa sozinho:** o script exige env de credenciais WP do executor (DSC/ZM) e chaves de modelo no cofre da casa — nenhum segredo neste arquivo (§82).

---

## 1. ARQUITETURA DO CÓDIGO (1 script, sem dependência nova)

| # | Função no script | O que faz | Modelo (fase TESTE) | Saída |
|---|---|---|---|---|
| 1 | `varredura_4feixes()` | C0a: busca agenda dura (calendário), mercado (cotações via fonte pública/API gratuita), manchetes (feeds do banco ★), casa (anel de audiência/esteira) | qwen3.8-flash (leitura/ranking) | JSON feixes |
| 2 | `ranking_top3()` | pondera tração × relevância pro bolso BR × dado duro do dia × âncora geopolítica; devolve top-3 com nota + justificativa | qwen3.8-flash | JSON top3 |
| 3 | `escolhe_pauta()` | C0: vencedor pela régua (dado duro > geo com preço > pauta da casa); se nada passa → `dia_morno: true` + fallback tese-âncora | regra (sem LLM) | JSON pauta |
| 4 | `escuta_dirigida()` | C1: puxa 3-8 fontes do banco ★ (seed local `banco_fontes_v42.json`) sobre a pauta; extrai blocos (título/link/posição) | requests + parsing | lista fontes |
| 5 | `engenharia_tese()` | C3: dados do dia + quadro de fontes → tese JSON (verbo/conflito/direção/ângulo leitor BR + validação MatrizEditorial) | qwen3.8-flash (barato NESTA fase; design v1.1 prevê frontier na Fase 2) | JSON tese |
| 6 | `redacao_4camadas()` | C4: título-primeiro → lead factual → contexto → impacto BR → fechos; self-review leve (verifica_estilo) | qwen3.8-flash | texto + título |
| 7 | `grava_rascunho_wp()` | grava post `draft` com meta `_v42_modo=teste` + `_v42_varredura` + `_v42_tese` + `_v42_dados_dia` — **NUNCA publish** | REST do executor (DSC/ZM) | post_id draft |

**Regras de ouro do script (disciplina DSC-051):**
- **1 arquivo, stdlib + `requests` apenas** (sem framework, sem banco novo, sem dependência nova).
- **Fail-closed:** qualquer etapa sem dado com fonte → aborta o ciclo com log (não inventa número; regra da casa: número sem fonte não entra).
- **MODO TESTE travado no código:** `POST_STATUS = "draft"` constante; `--publish` só existiria numa fase futura e exigiria flag explícita + gate — nesta versão NEM a flag existe.
- **Rollback = desligar o cron** (1 linha) ou apagar o arquivo; não toca em nada do V4.1.
- **Segredo:** chaves/credenciais só via env (cofre da casa, fora do repo); este arquivo não contém nenhum valor de chave.

---

## 2. RASCUNHO DO CÓDIGO — `v42_analise_teste.py` (para discussão/validação do ZM; NUNCA rodar sem deploy autorizado)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.2 "Cafezinho Investimento" — FASE DE TESTE (DSC-20260902-051)
RASCUNHO do DS Nuvem Ideias (DS-N Ideias) — dentro do arquivo da ideia, NUNCA em produção.
Execução/deploy: DSC + ZM (item 2 do despacho), só após ✓ do Miguel.

Ciclo mínimo: C0a varredura(4 feixes) -> C0 pauta -> C1 escuta dirigida -> C3 tese -> C4 redação
              -> grava RASCUNHO (draft) com meta _v42_*. NUNCA publica.

Pilha (fase TESTE, frontier PROIBIDO):
  motor principal : qwen3.8-flash (Token Plan — custo marginal ~0)
  reserva         : glm flash/turbo (se qwen indisponível)
  visão           : qwen3-vl (só quando precisar de capa/gráfico; fase posterior)
Dependências: stdlib + requests. Sem framework, sem banco novo.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# ----------------------------------------------------------------------------
# 0. CONSTANTES — MODO TESTE TRAVADO (disciplina DSC-051)
# ----------------------------------------------------------------------------
POST_STATUS = "draft"          # NUNCA "publish" nesta fase. Nem flag --publish existe.
V42_MODO = "teste"
DATA = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")

# Cofre da casa — chaves via ENV (nunca no arquivo). O executor (DSC/ZM) injeta.
QWEN_MODEL = os.environ.get("V42_QWEN_MODEL", "qwen3.8-flash")
QWEN_BASE = os.environ.get("V42_QWEN_BASE", "")        # ex.: endpoint DashScope compatível OpenAI
QWEN_KEY = os.environ.get("V42_QWEN_KEY", "")          # do cofre (token plan)
GLM_MODEL = os.environ.get("V42_GLM_MODEL", "glm-flash")  # reserva
GLM_BASE = os.environ.get("V42_GLM_BASE", "")
GLM_KEY = os.environ.get("V42_GLM_KEY", "")
WP_REST = os.environ.get("V42_WP_REST", "")            # ex.: https://espelho.../wp-json/wp/v2 (executor)
WP_USER = os.environ.get("V42_WP_USER", "")
WP_APP_PASS = os.environ.get("V42_WP_APP_PASS", "")

BANCO_FONTES = Path(os.environ.get("V42_BANCO_FONTES", "banco_fontes_v42.json"))

# ----------------------------------------------------------------------------
# 1. LLM — chamada barata com reserva (sem segredo em log)
# ----------------------------------------------------------------------------
def chamar_llm(system: str, user: str, modelo: str | None = None,
               json_mode: bool = False) -> str:
    """Chama o modelo barato (qwen3.8-flash) com fallback p/ glm flash.
    Fase TESTE: frontier PROIBIDO — não existe caminho p/ modelo caro aqui."""
    tentativas = []
    if QWEN_KEY:
        tentativas.append((QWEN_MODEL, QWEN_BASE, QWEN_KEY))
    if GLM_KEY and GLM_MODEL != QWEN_MODEL:
        tentativas.append((GLM_MODEL, GLM_BASE, GLM_KEY))
    if not tentativas:
        raise RuntimeError("V42: sem chave de modelo barato no env (cofre) — aborta (fail-closed)")

    ultimo_erro = None
    for nome, base, chave in tentativas:
        try:
            payload = {
                "model": nome,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": 0.3,
            }
            if json_mode:
                payload["response_format"] = {"type": "json_object"}
            req = urllib.request.Request(
                base.rstrip("/") + "/chat/completions",
                data=json.dumps(payload).encode(),
                headers={"Content-Type": "application/json",
                         "Authorization": "Bearer " + chave},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=120) as r:
                corpo = json.loads(r.read().decode())
            return corpo["choices"][0]["message"]["content"]
        except Exception as e:  # noqa: BLE001 — loga e tenta a reserva
            ultimo_erro = f"{nome}: {e}"
            continue
    raise RuntimeError(f"V42: todas as pernas baratas falharam — {ultimo_erro}")

def llm_json(system: str, user: str) -> dict:
    """Chama com response_format json e devolve dict validado."""
    texto = chamar_llm(system, user, json_mode=True)
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        # fail-closed: não tenta adivinhar JSON quebrado
        raise RuntimeError("V42: LLM devolveu JSON inválido — aborta (fail-closed)")

# ----------------------------------------------------------------------------
# 2. C0a — VARREDURA do dia (4 feixes; varredura MAPEIA, não aprofunda)
# ----------------------------------------------------------------------------
def varredura_4feixes() -> dict:
    """Monta os 4 feixes da varredura (emenda DSC-050). Cada número com fonte+hora.
    Em fase TESTE os alimentadores podem ser manuais/seed (lista abaixo) — a automação
    de calendário/cotações entra como melhoria medida pelo teste (critério §4)."""
    # --- feixe 1: agenda dura (o que TEM HORA hoje) — alimentador manual/seed no teste
    agenda = _agenda_dura_do_dia()
    # --- feixe 2: mercado (o que MEXEU vs média) — seed manual/API gratuita no teste
    mercado = _mercado_do_dia()
    # --- feixe 3: manchetes (clusters de fontes DISTINTAS no banco ★)
    manchetes = _manchetes_clusters()
    # --- feixe 4: casa (anel de audiência + pautas quentes da esteira)
    casa = _anel_casa()

    system = (
        "Você é o editor de varredura do O Cafezinho (Cafezinho Investimento). "
        "Varredura MAPEIA, não aprofunda (aprofundar é a C1). Devolva APENAS JSON."
    )
    user = json.dumps(
        {"hoje": DATA, "agenda_dura": agenda, "mercado": mercado,
         "manchetes": manchetes, "casa": casa},
        ensure_ascii=False,
    ) + (
        "\nProduza o ranking top-3 em JSON: "
        '{"top3": [{"candidato": "...", "nota": 0-10, "justificativa": "..."}], '
        '"dia_morno": false} pela régua: tração (nº de fontes DISTINTAS × destaque) × '
        "relevância pro bolso do leitor BR não-Faria Lima × tem dado duro do dia pra ancorar? × "
        "âncora geopolítica da linha. Desempate: dado duro > fato geopolítico com efeito em preço "
        "> desdobramento de pauta da casa. Se NADA passar do limiar (nota < 6): "
        '{"dia_morno": true, "fallback": "tese-âncora do banco com o dado mais recente"} — '
        "NUNCA fique sem pauta, NUNCA invente urgência. Cada fato citado com fonte."
    )
    return llm_json(system, user)

# --- alimentadores (fase TESTE: seed manual / TODO automação pós-teste) ---
def _agenda_dura_do_dia() -> list[dict]:
    """TODO(ZM): ligar ao calendário econômico (B3/BC/IBGE/USDA/Fed/leilões).
    No teste: arquivo `v42_seed_agenda.json` editado pelo executor antes do ciclo."""
    seed = Path("v42_seed_agenda.json")
    if seed.exists():
        return json.loads(seed.read_text())
    return []  # fail-closed: sem agenda não inventa

def _mercado_do_dia() -> list[dict]:
    """TODO(ZM): cotações do dia (dólar/juros/Ibov/minério/petróleo/ouro) com fonte+hora."""
    seed = Path("v42_seed_mercado.json")
    if seed.exists():
        return json.loads(seed.read_text())
    return []

def _manchetes_clusters() -> list[dict]:
    """Conta clusters: nº de fontes DISTINTAS do banco ★ cobrindo cada fato."""
    if not BANCO_FONTES.exists():
        return []
    banco = json.loads(BANCO_FONTES.read_text())
    # TODO(ZM): puxar feeds das fontes do banco e agrupar por fato (título normalizado)
    return [{"fato": "seed-teste", "fontes_distintas": 0}]  # placeholder honesto

def _anel_casa() -> list[dict]:
    """Pautas quentes da esteira/audiência (anel INFORMA, não decide)."""
    return [{"fonte": "esteira-casa", "nota": "ver canal de_ideias/de_dell"}]

# ----------------------------------------------------------------------------
# 3. C0 — escolha da pauta (regra determinística sobre o ranking)
# ----------------------------------------------------------------------------
def escolhe_pauta(varredura: dict) -> dict:
    top3 = varredura.get("top3", [])
    if varredura.get("dia_morno") or not top3:
        return {"pauta": varredura.get("fallback", "tese-anclora"),
                "dia_morno": True, "por_que": "nada passou do limiar"}
    vencedor = top3[0]  # o ranking já vem ordenado pela régua
    return {"pauta": vencedor["candidato"], "dia_morno": False,
            "por_que": vencedor["justificativa"], "top3": top3}

# ----------------------------------------------------------------------------
# 4. C1 — escuta dirigida (3-8 fontes do banco ★ sobre a pauta)
# ----------------------------------------------------------------------------
def escuta_dirigida(pauta: str) -> list[dict]:
    """Puxa do banco ★ as fontes BR+intl relevantes à pauta; devolve quadro bruto."""
    if not BANCO_FONTES.exists():
        raise RuntimeError("V42: banco_fontes_v42.json ausente — aborta (fail-closed)")
    banco = json.loads(BANCO_FONTES.read_text())
    # TODO(ZM): busca dirigida nas fontes (RSS/URLs) — no teste aceita seed manual
    # `v42_seed_coleta.json` com [{veiculo, titulo, url, data, alinhamento_estrelas}]
    seed = Path("v42_seed_coleta.json")
    if seed.exists():
        coletado = json.loads(seed.read_text())
        return [f for f in coletado if pauta.lower() in f.get("titulo", "").lower()][:8] or coletado[:8]
    return []

# ----------------------------------------------------------------------------
# 5. C3 — engenharia da tese (BARATA nesta fase — DSC-051)
# ----------------------------------------------------------------------------
def engenharia_tese(dados_dia: list[dict], quadro: list[dict]) -> dict:
    system = (
        "Você é o editor de análise do O Cafezinho (Cafezinho Investimento). "
        "Produza UMA tese em JSON. A tese vale para quem investe no Brasil e NÃO é da Faria "
        "Lima. Pauta afirmativa (BRICS/SCO/Sul Global) NÃO precisa de vilão. "
        "Análise crítica cita fonte. Devolva APENAS JSON."
    )
    user = json.dumps(
        {"hoje": DATA, "pauta_escolhida": "...", "dados_dia": dados_dia,
         "quadro_fontes": quadro},
        ensure_ascii=False,
    ) + (
        '\nJSON: {"verbo": "...", "conflito": "...", "direcao": "...", '
        '"angulo_para_leitor_br": "...", "pauta_afirmativa_sem_vilao": bool, '
        '"dado_central": {"numero": "...", "fonte": "...", "hora": "..."}, '
        '"valida_matriz_editorial": {"verbo_ok": bool, "conflito_ok": bool, '
        '"direcao_ok": bool, "dado_ok": bool}}'
    )
    return llm_json(system, user)

# ----------------------------------------------------------------------------
# 6. C4 — redação (4 camadas; título-primeiro; manual v2.1.0)
# ----------------------------------------------------------------------------
def redacao_4camadas(tese: dict, dados_dia: list[dict], quadro: list[dict]) -> dict:
    system = (
        "Você é o redator do O Cafezinho (Cafezinho Investimento). Manual de escrita v2.1.0: "
        "título-primeiro (1 ideia, ≤80c, sem ':'/'—', máx. 1 nome próprio), corpo em 4 camadas "
        "(Lead factual -> Contexto -> Impacto pro leitor BR -> Cenários/fecho). No corpo, 3 "
        "respostas EXPLÍCITAS: o que as fontes CONCORDAM; onde DISCORDAM (nunca apague em "
        "silêncio); o que mudou HOJE pro leitor. Número sem fonte não entra. Zero recomendação "
        "de compra/venda (explica o mecanismo). Zero xingamento de país. 'Ditadura' só com "
        "critério + fonte. Fecho = a pergunta que importa. Máx. 2 frases/parágrafo. "
        "Devolva APENAS JSON."
    )
    user = json.dumps(
        {"hoje": DATA, "tese": tese, "dados_dia": dados_dia, "quadro_fontes": quadro},
        ensure_ascii=False,
    ) + (
        '\nJSON: {"titulo": "...", "camada_1_lead": "...", "camada_2_contexto": "...", '
        '"camada_3_impacto_br": "...", "camada_4_fechos": "..."}'
    )
    return llm_json(system, user)

# ----------------------------------------------------------------------------
# 7. grava RASCUNHO no WP (MODO TESTE — draft, NUNCA publish)
# ----------------------------------------------------------------------------
def grava_rascunho_wp(titulo: str, conteudo: str, metas: dict) -> int:
    if not (WP_REST and WP_USER and WP_APP_PASS):
        # Em teste sem WP configurado: grava local p/ inspeção (nunca publica nada)
        Path(f"v42_rascunho_{DATA}.md").write_text(
            f"# {titulo}\n\n{conteudo}\n\n<!-- metas: {json.dumps(metas, ensure_ascii=False)} -->"
        )
        return 0
    import requests  # única dependência externa; carregada só no caminho WP
    auth = (WP_USER, WP_APP_PASS)
    payload = {
        "title": titulo,
        "content": conteudo,
        "status": POST_STATUS,          # "draft" — travado
        "meta": metas,                  # _v42_* (ver design v1.1 §2.2)
    }
    r = requests.post(WP_REST.rstrip("/") + "/posts", json=payload, auth=auth, timeout=60)
    r.raise_for_status()
    return r.json()["id"]

# ----------------------------------------------------------------------------
# MAIN — ciclo do dia (fase teste)
# ----------------------------------------------------------------------------
def main() -> int:
    print(f"[V4.2 TESTE] {DATA} — início do ciclo (modo {V42_MODO}, status={POST_STATUS})")
    try:
        # C0a
        varredura = varredura_4feixes()
        # C0
        pauta = escolhe_pauta(varredura)
        # C1
        quadro = escuta_dirigida(pauta["pauta"])
        dados_dia = _mercado_do_dia()
        # C3 (barato nesta fase)
        tese = engenharia_tese(dados_dia, quadro)
        if not all(tese.get("valida_matriz_editorial", {}).get(k)
                   for k in ("verbo_ok", "conflito_ok", "direcao_ok", "dado_ok")):
            raise RuntimeError("V42: tese reprovou na MatrizEditorial — aborta (fail-closed)")
        # C4
        redacao = redacao_4camadas(tese, dados_dia, quadro)
        conteudo = "\n\n".join(
            redacao[k] for k in
            ("camada_1_lead", "camada_2_contexto", "camada_3_impacto_br", "camada_4_fechos")
        )
        metas = {
            "_v42_modo": "teste",
            "_v42_pauta": pauta["pauta"],
            "_v42_varredura": json.dumps(varredura, ensure_ascii=False),
            "_v42_tese": json.dumps(tese, ensure_ascii=False),
            "_v42_dados_dia": json.dumps(dados_dia, ensure_ascii=False),
        }
        post_id = grava_rascunho_wp(redacao["titulo"], conteudo, metas)
        # prova no log (nunca segredo)
        print(f"[V4.2 TESTE] OK — rascunho {'local' if post_id == 0 else 'WP#' + str(post_id)}")
        print(f"[V4.2 TESTE] titulo: {redacao['titulo']}")
        return 0
    except Exception as e:  # noqa: BLE001
        print(f"[V4.2 TESTE] FALHA (fail-closed, nada publicado): {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

> **Notas de validação (para o ZM na hora do deploy):** (1) o nome/endpoint exato do qwen3.8-flash e do glm-flash via Token Plan precisa ser conferido com o cofre/llm_env da casa (o R1 usa escada GLM5.3+web → qwen3.8-max → brave+deepseek; aqui a DSC-051 manda flash/turbo — validar disponibilidade real antes de fixar); (2) `requests` é a única dependência — se o ambiente já tiver, zero instalação; (3) os `v42_seed_*.json` são o "andaime" do teste (o Miguel pediu simples e elegante: começa com seed manual e automatiza o que o teste provar); (4) NENHUM valor de chave neste arquivo — tudo via env no momento de rodar.

---

## 3. CRON DE TESTE PROPOSTO + CHECKLIST DE DEPLOY (execução = DSC + ZM, item 2 do despacho)

### 3.1 Cron (proposta — 1 ciclo/dia, FORA da esteira V4.1)
```cron
# V4.2 Cafezinho Investimento — FASE TESTE (rascunho ~15:00; nada publica)
# rollback = comentar/remover esta linha (1 passo)
0 14 * * 1-5  cd /caminho/do/deploy/v42 && . /caminho/do/cofre/env && python3 v42_analise_teste.py >> v42_teste.log 2>&1
```
- **SLA de teste:** ciclo 14:00 → rascunho pronto ~15:00 (pipeline barato ≈ minutos; folga p/ revisão humana).
- **Dias:** 2ª-6ª (dias de mercado; o design prevê "todo dia da semana" na Fase 2 — o teste começa em dias úteis).
- **Rollback:** `crontab -e` remove a linha (1 passo); nada mais a desfazer (rascunhos ficam drafts).

### 3.2 Checklist de deploy (rito da casa: backup → prova → registro → rollback escrito)
| # | Passo | Quem | Prova |
|---|---|---|---|
| D1 | Backup do estado atual (crontab + diretório de deploy se existir) | ZM | `.bak_AAAA-MM-DD` + diff |
| D2 | Copiar `v42_analise_teste.py` p/ o tencent (ex.: `~/v42_analise/v42_analise_teste.py`) + `banco_fontes_v42.json` seed | ZM | `sha256sum` no stdout |
| D3 | Preparar `v42_seed_agenda.json` + `v42_seed_mercado.json` + `v42_seed_coleta.json` do dia (andaime do teste) | ZM/DS-N Ideias ajuda no formato | arquivos no deploy |
| D4 | **Prova de modelo (antes do cron):** 1 chamada qwen3.8-flash + 1 glm-flash de smoke (a casa já aprendeu: testar cada perna antes de fixar — escada R1) | DSC/ZM | stdout da chamada |
| D5 | Teste manual 1 ciclo (sem cron): rodar o script 1× e conferir o rascunho (draft) + metas `_v42_*` no WP espelho | ZM/AGY (visão) | post_id + REST do rascunho |
| D6 | Registrar no canal/ponte (regra de ouro: ponte + grade no mesmo commit — V4.2 entra como TESTE na grade, sem mudar cadência de produção) | DSC/ZM/Chefe | commit + linha na grade |
| D7 | Ligar o cron 14:00 | ZM | `crontab -l` |
| D8 | Vigiar 3 primeiros ciclos (custo ~zero esperado — Token Plan; qualquer gasto fora → alerta Chefe) | Chefe | relatório de ronda + DSN-F |
| D9 | **Rollback escrito** (guardar no deploy): se algo falhar, `crontab -e` remove a linha; rascunhos não publicados não precisam limpeza | ZM | registro |

**Nada disto é executado por mim** — é o checklist para DSC + ZM (item 2 do despacho DSC-051). Eu entrego o código + o desenho; execução exige ✓ do Miguel (Lei de Poderes).

---

## 4. CRITÉRIOS DE SUCESSO DO TESTE (o que medir — DSC-051 item 1d)

| # | Critério | Como mede | Régua de "passou" (proposta p/ o Miguel validar) |
|---|---|---|---|
| 1 | **Pauta bem escolhida** | `_v42_varredura` (top3 + nota + justificativa) vs o dia real (reconferência do Chefe/R1) | em ≥4 de 5 dias úteis o vencedor do top-3 é defensável como o fato mais relevante do dia pro leitor BR |
| 2 | **Tese com verbo/conflito/direção** | `_v42_tese` + validação MatrizEditorial no log | 100% das teses passam na Matriz (verbo/conflito/direção/dado) |
| 3 | **Dado do dia correto e checado** | R1 confere os números do rascunho (fonte + hora no `_v42_dados_dia`) | 100% dos números com fonte real; 0 número sem fonte no rascunho |
| 4 | **Estilo manual v2.1.0** | revisão R2/CL do título e do texto (rascunho) | 0 erro de clareza de título; texto dentro do manual (lead→contexto→impacto→fechos) |
| 5 | **Custo ~zero** | DSN-F (router/telemetry) | gasto da fase teste ≈ 0 (Token Plan qwen flash); qualquer gasto fora → alerta |
| 6 | **Não atrapalha a esteira** | grade/volume do V4.1 | 0 interferência: volume e pontualidade do hard news intactos durante o teste |
| 7 | **Qualidade da tese no barato** | comparação qualitativa (Chefe/CL/Miguel) | o barato segura a tese? Se não: o teste REGISTRA e o relatório sobe — aí a Fase 2 (frontier só na C3) volta ao desenho v1.1 |

**Duração sugerida:** 5 dias úteis (1 semana) de rascunhos — depois o relatório de teste (o que passou/fallhou, com os rascunhos como prova) vai ao Miguel para a decisão de Fase 2 (canário 1/dia ~19h com gate CL/CM — design v1.1 §4).

---

## 5. RISCOS E REVERSIBILIDADE (protocolo da casa)

| Risco | Prob. | Impacto | Mitigação / reversão |
|---|---|---|---|
| R1 — qwen3.8-flash/glm-flash indisponível ou com nome/endpoint diferente no cofre | média | ciclo não roda | D4 (smoke antes do cron); ajuste de env em 1 linha; rollback = cron off |
| R2 — qualidade da tese no barato abaixo do padrão Cafezinho | média | rascunho fraco (não publicado) | critério 7 mede e REGISTRA; nada publicado → zero dano; Fase 2 volta frontier-só-C3 |
| R3 — número errado no seed (andaime manual) | média | rascunho com número errado | fail-closed "sem fonte não entra" + R1 confere (critério 3); rascunho não publica |
| R4 — cron disputar recurso com a esteira | baixa | lentidão | 1 ciclo/dia ~14:00 (fora dos slots de publish); rollback 1 linha |
| R5 — segredo vazar no log | baixa | §82 | script nunca loga chave; env injetado no momento de rodar; revisão do ZM no D2 |

**Reversibilidade total:** desligar o cron = fim do teste; rascunhos `draft` não publicados não têm efeito público; nada do V4.1 é tocado (arquivo separado, cron separado, sem mudança em scripts da esteira).

---

## 6. O QUE PRECISO (para o teste sair do papel)

1. **✓ do Miguel** para DSC+ZM instalarem a fase TESTE no espelho (item 2 do despacho DSC-051) — meu papel (código + desenho) está entregue aqui e no design v1.1.
2. **Validação do ZM** do rascunho de código (nomes/endpoints dos modelos baratos no cofre, formato dos seeds, caminho de deploy) — D2-D5 do checklist.
3. **Ciência do Chefe** para a vigia de custo (critério 5) e da entrada "V4.2 TESTE" na grade (regra de ouro: ponte + grade no mesmo commit — execução DSC/ZM).
4. **Decisão do Miguel na régua do critério 7:** se a tese no barato não fechar qualidade, o teste registra e a Fase 2 volta ao desenho v1.1 (frontier só na C3) — ou ele prefere já autorizar frontier na C3 mesmo no teste.

**Refs:** DSC-20260902-051 (de_dell.md, commit 005c29941) · DSC-050 (varredura, incorporada no design v1.1) · design `2026-09-02_v42_agente_analise_investimento.md` v1.1 · `2026-09-02_banco_fontes_investimento_geopolitica_estrelas.md` · `2026-09-02_minuta_constituicao_ideologica_cafezinho.md` · escada R1 (memória dsn_revisor1 — lição "testar cada perna antes de fixar") · regra do Cofre §82 (segredo nunca em arquivo de ideia) · ZM-058 (texto limpo no Telegram; este é repo md).

---

## 7. REVISÃO v1.3 — OS 4 GATES DA LIÇÃO DO ESTATÍSTICO (V42MON-OFICIO 03/09, item 4)

> **Origem:** bloco `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (Vigia V4.2 / DSC us65, 03/09 ~01:45) — a lição do V4.2 Estatística (retro 26/08-02/09: números 100% reais mas 9 defeitos editoriais — título duplicado, tese repetida, mensal chamado de acumulado, euros chamados de US$, dado de fevereiro como "recorde") virou 4 gates na reforma do NYC. **"Modelo barato sem gate vira 'inteligência barata'; COM gate, o barato passa."** Adoto os mesmos 4 gates neste rascunho (`v42_analise_teste.py`) — **antes do 1º ciclo-alvo de HOJE 14h (DSC-063: ✓✓✓ do Miguel, destino espelho)**.
> **Natureza:** rascunho (regra da casa) — nada em produção. O executor (DSC/ZM) dobra estas funções no deploy D2-D5; não muda env/cron/checklist D1-D9; rollback continua = desligar o cron.

### 7.1 Onde entram no `main()` (delta sobre o rascunho da seção 2)

```python
# ----------------------------------------------------------------------------
# 7.1a GATE A — VALIDADOR FACTUAL MECÂNICO (número do texto nasce do banco)
#      Física: mesma do validador do NYC/vigia — número fora de dados_dia/banco = aborta.
#      Roda ANTES de gravar o rascunho (fail-closed: nada com número órfão sai).
# ----------------------------------------------------------------------------
import re as _re

def valida_numeros_mecanico(texto: str, dados_dia: list[dict]) -> list[str]:
    """Devolve lista de números do texto sem origem em dados_dia (vazio = passa)."""
    def para_float(t: str) -> float:
        t = t.strip()
        if "," in t:
            return float(t.replace(".", "").replace(",", "."))
        if "." in t and len(t.split(".")[-1]) == 3:
            return float(t.replace(".", ""))
        return float(t)
    # candidatos: valores + conversões p/ bilhões + somas/diferenças de saldo
    cand = set()
    for d in dados_dia:
        try:
            v = para_float(str(d.get("valor", "")))
        except ValueError:
            continue
        un = str(d.get("unidade", "")).lower()
        cand.add(round(v / 1000.0 if "milh" in un else v, 2))
    numeros = []
    for m in _re.finditer(r"(\d{1,3}(?:[.,]\d{1,3})?)\s*(bilh\w*|milh\w*|bi\b|mi\b)", texto, _re.IGNORECASE):
        try:
            n = para_float(m.group(1))
        except ValueError:
            continue
        esc = m.group(2).lower()
        n_bi = n if esc.startswith("bilh") or esc == "bi" else n / 1000.0
        numeros.append((m.group(0), round(n_bi, 2)))
    # % fica fora do validador mecânico (o rodapé Var: é do NYC; aqui seed carrega var)
    orfaos = [f"{txt} ({n_bi} bi)" for txt, n_bi in numeros
              if not any(abs(n_bi - c) <= max(0.02, n_bi * 0.012) for c in cand)]
    return orfaos[:5]

# ----------------------------------------------------------------------------
# 7.1b GATE B — RODÍZIO DE TESES POR FRESCOR (anti "mesma tese todo dia")
#      Estado persistente mínimo: v42_teste_estado.json (nunca segredo).
# ----------------------------------------------------------------------------
ESTADO = Path("v42_teste_estado.json")

def _ler_estado() -> dict:
    if ESTADO.exists():
        try:
            return json.loads(ESTADO.read_text())
        except json.JSONDecodeError:
            return {}
    return {}

def _gravar_estado(est: dict) -> None:
    ESTADO.write_text(json.dumps(est, ensure_ascii=False, indent=1))

def escolhe_pauta_antieco(varredura: dict) -> dict:
    """top-3 vencedor; se repetir a última pauta, pula pro próximo (registra o porquê)."""
    top3 = varredura.get("top3", [])
    if varredura.get("dia_morno") or not top3:
        return {"pauta": varredura.get("fallback", "tese-anclora"),
                "dia_morno": True, "por_que": "nada passou do limiar"}
    est = _ler_estado()
    ultima = est.get("ultima_pauta")
    for cand in top3:  # top3 já vem ordenado pela régua
        if cand["candidato"] != ultima:
            return {"pauta": cand["candidato"], "dia_morno": False,
                    "por_que": cand["justificativa"]
                               + (f" | rodizio: ultima pauta era '{ultima}'" if ultima else ""),
                    "top3": top3}
    return {"pauta": top3[0]["candidato"], "dia_morno": False,
            "por_que": top3[0]["justificativa"] + " | todas repetem a ultima; vencedor mantido",
            "top3": top3}

# ----------------------------------------------------------------------------
# 7.1c GATE C — GATE DE FRESCOR DE DADO (só publica com dado novo)
#      mensal ≤60d · semanal ≤21d · anual ≤400d; sem dado novo → dia_morno honesto.
# ----------------------------------------------------------------------------
def _idade_dias(data_iso: str) -> int:
    from datetime import date as _date
    return (_date.today() - _date.fromisoformat(data_iso)).days

def gate_frescor_dado(pauta: dict, dados_dia: list[dict], frequencia: str = "mensal") -> dict:
    limiar = {"mensal": 60, "semanal": 21, "anual": 400}.get(frequencia, 60)
    if pauta.get("dia_morno"):
        return pauta  # fallback já é o dado mais recente — não inventa urgência
    for d in dados_dia:
        if d.get("data") and _idade_dias(str(d["data"])) <= limiar and d.get("valor") is not None:
            return pauta  # tem dado fresco ancorando a pauta
    # fail-closed honesto: pauta sem dado novo NÃO sobe como se fosse do dia
    return {"pauta": pauta.get("pauta"), "dia_morno": True,
            "por_que": f"gate de frescor: sem dado <= {limiar}d p/ ancorar — vira dia morno",
            "top3": pauta.get("top3", [])}

# ----------------------------------------------------------------------------
# 7.1d GATE D — GATE ANTI-ECO DE TÍTULO (Jaccard ≥0,85 → 1 retry, senão aborta)
# ----------------------------------------------------------------------------
def _jaccard_titulos(a: str, b: str) -> float:
    pa = {w.strip(".,:;!?\"'()").lower() for w in a.split() if len(w) > 2}
    pb = {w.strip(".,:;!?\"'()").lower() for w in b.split() if len(w) > 2}
    if not pa or not pb:
        return 0.0
    return len(pa & pb) / len(pa | pb)

def gate_antieco_titulo(titulo: str, estado: dict, limiar: float = 0.85) -> str | None:
    """Devolve o título com problema se ecoar os últimos títulos; None = passa."""
    for t in estado.get("ultimos_titulos", [])[-10:]:
        if _jaccard_titulos(titulo, t) >= limiar:
            return f"título em eco com anterior (Jaccard {_jaccard_titulos(titulo, t):.2f}): {titulo!r}"
    return None
```

### 7.2 Delta no `main()` (substitui os trechos marcados)

```python
    # C0 (com GATE B — rodízio por frescor)
    pauta = escolhe_pauta_antieco(varredura)
    # ... C1 ... dados_dia = _mercado_do_dia() ...
    # GATE C — só segue com dado fresco ancorando (senão dia morno honesto)
    pauta = gate_frescor_dado(pauta, dados_dia)
    # ... C3 tese ...
    # ... C4 redacao ...
    conteudo = "\n\n".join(...)  # (como já está)
    # GATE A — validador factual mecânico ANTES de gravar (número órfão = aborta)
    orfaos = valida_numeros_mecanico(conteudo, dados_dia)
    if orfaos:
        raise RuntimeError(f"V42: GATE A (factual mecânico) reprovou — números sem origem: {orfaos}")
    # GATE D — anti-eco de título (1 retry, senão aborta o ciclo)
    est = _ler_estado()
    eco = gate_antieco_titulo(redacao["titulo"], est)
    if eco:
        raise RuntimeError(f"V42: GATE D (anti-eco de título) reprovou — {eco}")
    # grava + atualiza o estado do rodízio (B) e os últimos títulos (D)
    post_id = grava_rascunho_wp(redacao["titulo"], conteudo, metas)
    est["ultima_pauta"] = pauta.get("pauta")
    est["ultimos_titulos"] = est.get("ultimos_titulos", [])[-9:] + [redacao["titulo"]]
    _gravar_estado(est)
```

### 7.3 Notas de validação (para o ZM no deploy de HOJE 14h)

1. **Ordem dos gates no ciclo:** C0 com rodízio (B) → C1 → gate de frescor (C) → C3 tese → C4 redação → gate factual mecânico (A) → gate anti-eco (D) → grava rascunho. Nenhum gate muda o que já estava fail-closed (MatrizEditorial, sem-fonte-não-entra); todos são **rascunho → nunca publicam**.
2. **`v42_teste_estado.json`** é o único estado novo (mesmo diretório do deploy; sem segredo). Rollback = apagar o arquivo + desligar o cron (nada muda).
3. **Seeds:** `v42_seed_*` passam a aceitar `data` (ISO) e `valor`/`unidade` por item — o formato dos seeds no checklist D3 ganha esses 2 campos (ex.: `{"veiculo": "...", "titulo": "...", "data": "2026-09-03", "valor": 5.2, "unidade": "US$ bilhões"}`).
4. **Regra de ouro da lição:** gate é para o modelo BARATO; o teste mede quantos ciclos os gates barram (meta `_v42_gates`: `{"factual": n_orfãos, "frescor": bool, "eco": bool, "rodizio": bool}`) — isso entra no relatório do critério 7 (§4) e na minha síntese semanal do V4.2.

**Refs:** V42MON-OFICIO (item 4) · `forum_v42_reforma_monitoramento_20260903.md` (gates do Estatístico) · DSC-063 (espelho aprovado, 1º ciclo HOJE 14h) · §82 (sem segredo) · ZM-058 (texto limpo; este é repo md).

— DS Nuvem Ideias (DS-N Ideias) · 20260903 03:16:49 BRT
