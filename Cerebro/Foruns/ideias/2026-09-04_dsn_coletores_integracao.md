# 🧠 IDEIA_PRO_DSNUVEM_IDEIAS-012 — ESTUDO DE ARQUITETURA: DSN COLETORES (integração com o V4.1 + teste de madrugada + coletores complementares noturnos + regra da chave leve)

> **Ronda:** 04/09/2026 08:43-08:5x BRT (DS-N Ideias, Tencent). Pull ff-only OK na 1ª (c1f2aa932..fb92138d0 — AL-600 08:35; a IDEIA-012 chegou no pull).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-012` — DSH-us65 relay de ordem do Miguel por voz (~09:1x BRT, commit `1fb91fa6d` 08:08 + bloco em `de_dell.md` 15894). Prazo sugerido: ainda hoje (rondas :13/:43) p/ o DS-N Chefe deliberar com o Miguel hoje.
> **Refs:** INBOX_MIGUEL.md (relays us65 07:45-09:10 — prova coletores V4.1 08:55 · esclarecimento 09:10) · CL-20260904-009 (07:41, alerta do buraco da manhã) / CL-010 (08:13, fecho do coletor + IDEIA-012 em curso) · pedido formal original CL 02/09 (de_laura.md 7479 / de_dell.md 11921) · formato JSONL definido pelo ZM (§6.2 `forum_critica_v41_ultra_luxo_20260902.md` + `CEREBRO_NODE_ATUALIZACOES.md` 02/09) · `forum_v41_ultra_luxo_cura_geo_20260902.md` + `Memorias/memoria_v41_ultra_luxo_cura_geo_20260902.md` (V41_ROBOS_COLETORES/CURADOR/EQUIPE_NACIONAL) · parecer do DS-N Chefe na §6 do `forum_rodada_comparativa_v41_titulos_20260902.md` (coletador DSN nacional: SIM viável) · `estudo_modelo_leve_qwen38_20260904.md` (us65, Sol sagrado) · `memoria_blocos_saude_esporte_ambiente_v41_20260826.md` e `reference_acesso_sqlite_v4_nyc.md` (schema da fila).
> **Natureza:** ESTUDO de arquitetura + rascunhos — NADA executado em produção (Lei de Poderes). Fluxo de decisão (regra do Miguel no próprio bloco): **Ideias desenvolve e apresenta → DS-N Chefe OPINA → decisão final + ✓ do Miguel → execução por quem tem mão (ZM/executor com credencial)**.
> **Marcador:** `PRONTO_ESTUDO_DSN_COLETORES`

---

## 0. Contexto verificado (o que existe hoje — sem executar nada)

1. **A fila do V4.1 (NYC)** são bancos sqlite por vertical: `/root/agent_data/v4_verticals/<vertical>.sqlite3`, tabela `candidates` com `item_key` (PK — sha1[:16] da URL canônica) · title · url · source_type · source_name · published_at/collected_at/first_seen_at/last_seen_at (ISO-UTC) · score · text_content · text_sha256 · status='new' · raw_json. Intake com gates fail-closed; dedupe do ciclo: rascunhada <24h / falha <6h não roda (chave `item_key[:16]`).
2. **Suprimento atual (NYC, reformas 02/09-03/09, ZM):** robô único `robos_coletores_v41.py` (cron */15, flock próprio) com módulos: 9 verticais (cadências 15-60 min) · multiidioma (19 feeds RSS diretos em 8 línguas, 30 min, máx 3/feed, GATE ≥800 chars) · curador (`nota_curadoria = 0,4·frescor + 0,4·importância + 0,2·texto` no raw_json) · prospector nacional (20 feeds; 16/20 vivos na 1ª sondagem; 6 falhas seguidas = aposenta; retry 6h) · coletor nacional direto (15 min, INSERT OR IGNORE, trafilatura, <800 marcado `texto_curto`) · enriquecedor (Brave, máx 10 buscas/30 min, monta MATERIAL BRUTO com fonte+URL). Guardião `autocura_fila_v41.py` (cron */20): fila <2 tentáveis → coleta+intake extra na hora; vazio legítimo vira INCIDENTE visível. **O robô só INSERE candidatas status='new'; ciclo/tese/redator/FC/publicação intactos; publicação é da CL (gate standby_contrato).**
3. **Prova de saúde (04/09 08:55, us65 direto no NYC):** ronda 10:45 UTC rc=0 em todas as verticais; entregas estáveis **17-24/h em TODAS as horas** de 03-04/09 (madrugada incluída); robos.log com ZERO erros 429/402/quota/credit; enriquecedor Brave 5/5; telemetria LLM do dia sem crédito anormal. **A fila vazia 03:48→06:48 BRT foi DEDUPE** (`todas_pautas_ja_rascunhadas_24h`; corridas com novos=0 na madrugada: 04h UTC=7, 06h=8 corridas) = **falta de pauta NOVA de madrugada/manhã — não pane, não crédito** (causa-raiz do alerta da CL-009 fechada pela CL-010).
4. **DSN coletores dedicados NA NUVEM/Tencent NÃO existem** (crontab Tencent conferido, relay 09:10): quem coleta na nuvem hoje é só o YouTube. A casa respondeu ao pedido de 02/09 com a reforma do V4.1 no NYC (itens 2-3).
5. **Formato de entrega DSN JÁ DEFINIDO (ZM, 02/09):** JSONL, 1 item por linha: `item_key` (sha1[:16] da URL canônica — chave do dedupe) · `title` (≤140) · `url` · `source_name` (ex.: "Agência Senado") · `source_type="dsn"` · `published_at` (ISO 8601 UTC, **obrigatório** — o frescor depende dele) · `text_content` (≥800 chars — a tese ancora no corpo). Adapter do ZM insere em `candidates` com status='new' + score pela régua da vertical, dedupe por item_key, log de toda entrega em `entregas.log` (regra do Miguel: **nenhum robô invisível**). Começar pelo nacional; fontes oficiais; **cadência livre em bursts ≤25 itens/entrega** — o guardião da fila pede mais quando secar.
6. **Chaves/modelos (estudo us65 04/09):** Sol (gpt-5.6-sol, ultra-luxo) é **SÓ do redator** (prova: 13/13 chamadas tese_frontier no dia); modelos leves disponíveis: qwen3.8-flash (triagem), glm-5-turbo (reserva), deepseek-v4-flash. Custo da esteira ~US$ 2,58/dia (02/09). Telemetria DSN-F discrimina por LLM (regra da casa).

---

## 1. ENTREGA 1 — INTEGRAÇÃO dos DSN coletores (novos, Tencent) com o V4.1 (NYC) sem quebrar nada

### 1.1 Arquitetura proposta (componentes, dados, fluxo, onde roda)

| Componente | Onde roda | Papel | Estado |
|---|---|---|---|
| **Produtor DSN** (`dsn_coletor_nacional.py` — rascunho §6.1) | **Tencent (nuvem)** — pedido do Miguel | Coleta fontes oficiais nacionais (RSS/HTML), gera **JSONL no formato ZM** (item_key/fonte/hora/resumo ≥800), grava `entregas.log` + estado | NOVO (a construir, modo observação 1º) |
| **Canal de entrega** | Repo da casa (`cerebro-miguel`, origin GitHub) | Pasta dedicada `dados/dsn_coletores/entregas/YYYY-MM-DD_HHMM_dsn_nacional.jsonl` + commit por lote (carimbo real). É o barramento que a casa já usa (pedidos V42MON, ponte, grade) — trilha auditável no origin, sem robô invisível | NOVO (proposta; decisão final do ponto de entrega é do ZM, dono do pipeline) |
| **Adapter DSN** (do ZM, prometido na compilação §6.2) | **NYC** (junto ao robô único ou cron próprio */15 com flock) | `git fetch/pull` da pasta de entregas; valida schema fail-closed (item_key presente, published_at ISO-UTC parseável, title ≤140, text_content ≥800); confere item_key = sha1[:16](URL); **INSERT OR IGNORE** em `candidates` (status='new', score régua da vertical); registra em `entregas.log` + estado (último arquivo processado = **idempotente**) | ZM (já comprometido; aguarda ✓ + formato de pasta) |
| **Dedupe compartilhado** | NYC (fila) | Chave ÚNICA = **item_key** (sha1[:16] da URL canônica). Produtor DSN e V4.1 calculam a MESMA chave sobre a MESMA URL → INSERT OR IGNORE + dedupe do ciclo resolvem SEM tocar intake/ciclo. Pauta que chegar 2× (V4.1 e DSN): a 1ª vira candidata, a 2ª é descartada e **contada** (métrica de duplicata cruzada) | Padrão já existente (OR IGNORE é o modo do robô V4.1) |
| **Telemetria** | Tencent + NYC | Produtor loga toda entrega (ts, arquivo, nº itens, rc, duplicatas) + linha no monitor (seção FILA) + DSN-F conta LLM usado (nenhum na captura; leve se usado p/ resumo) | Regra da casa (sem robô invisível) |

### 1.2 Garantias de não-quebra (espelham o que o ZM já provou no V4.1)

- O produtor **só gera arquivos JSONL**; o adapter **só INSERE candidatas status='new'** — nada toca ciclo V4.1, tese dinâmica, redator, fact-check, escalonador ou publicação (publicar segue sendo da CL).
- Fontes DSN (Câmara/Senado/STF/TSE/TCU/DOU/Planalto) **não estão nos feeds atuais do V4.1** (o prospector nacional sonda imprensa: metropoles/g1/icl/folha/veja/agencia_brasil/congresso_foco…, não os canais oficiais diretos) → é **complemento de suprimento**, não concorrência nem duplicação estrutural.
- Rollback em 1 alavanca: `ativo=false` no config do produtor (nada mais é entregue) + adapter sem efeito retroativo. Backup + SHA + ROLLBACK_INDEX por seção (rito da casa).

### 1.3 Ponto de decisão para o Chefe/ZM

Entrega via repo (recomendada: barramento já provado, auditável, os donos veem o que entrou no origin) **ou** cópia direta p/ o NYC pelo mecanismo que o us65 usa p/ instalar seeds (`sync` v6_data). Recomendo repo + adapter com pull: o V42MON já prova o padrão "arquivo no repo → agente consome no pull" e deixa a trilha no origin; o custo é o adapter precisar de um clone do repo no NYC (decisão do ZM).

---

## 2. ENTREGA 2 — TESTE/MONITOR AUTOMÁTICO DE MADRUGADA (saudável E fresco)

### 2.1 Desenho (2 camadas — sem credencial nova)

**Camada A — profunda (NYC, dono ZM/DS-Dell):** vigia read-only nos logs locais (`robos.log`, `entregas.jsonl`, sqlite), cron 1/h na janela 00:00-08:00 BRT. Mede: (a) SAÚDE — rc das corridas (baseline rc=0), entregas/h (baseline 17-24), erros 429/402/quota/credit (baseline 0); (b) FRESCOR — novos/h por vertical (baseline madrugada legítima: 0 com dedupe; dia: 2-4) e idade do topo da fila.

**Camada B — barata (Tencent, DS-N Ideias — este ofício):** o DS-N não tem credencial NYC (nem deve); a camada B cruza o que a casa JÁ expõe: (1) REST público do espelho (posts publicados por hora = proxy de frescor da fábrica; hoje `publish_total` 78.890+); (2) o relatório 4/4h e os CHECKs do DS-N Chefe na ponte (linhas de volume/rc — já têm a régua); (3) os pedidos/vereditos V42MON. Rascunho do script em §6.2. É a camada que o DS-N roda de verdade nas rondas 30/30 (grep + sonda REST + leitura da ponte — o que já fazemos).

### 2.2 Critérios de alerta (pro Who/Telegram do Chefe) — SEMPRE com 2+ leituras (lição caçadas 16/18: leitura única não é veredito)

| Nível | Condição (2+ leituras cruzadas) | Ação |
|---|---|---|
| 🟡 AMARELO | Vertical que normalmente entrega à noite com **2+ corridas seguidas novos=0 E coleta rc=0** (fonte silenciosa — ex.: feed oficial caiu) | Linha no monitor + aviso ao dono (ZM) na ponte |
| 🟠 LARANJA | **Fila global seca 3h+** (0 candidata nova em todas as verticais) OU **entregas/h < metade da baseline (≤8/h) por 2h** | Alerta no Telegram do Chefe + roteiro: conferir crontab NYc/flocks ANTES de declarar pane |
| 🔴 VERMELHO | rc≠0 em coleta/intake OU erros **429/402/quota/credit** OU robos.log com erro de crédito | Alerta imediato (dono ZM) — classe crédito (o que o Miguel pergunta primeiro) |
| ✅ DEDUPE (não alerta) | novos=0 **MAS** rc=0 + entregas na faixa 17-24/h + coleta rodando = **dedupe legítimo** (caso de hoje 03:48→06:48 — prova INBOX 08:55) | Registro em 1 linha; NUNCA alerta |

### 2.3 Baseline real (prova de hoje — INBOX 08:55)

Madrugada 03→04/09: corridas com novos=0 — 04h UTC=7 · 06h=8; entregas 17-24/h todas as horas; dia: 2-4 novos/h; robos.log 0 erros de crédito. Régua de saudável: rc=0 + entregas na faixa + frescor por janela da vertical (24h hard / 48h soft / 72h cultura — V41_FRESCOR). A régua de "frescor de verdade" (pauta nova, não repetida) = item_key novo + published_at dentro da janela — exatamente o que o dedupe de 24h do ciclo já implementa; o vigia só precisa EXPOR a contagem.

---

## 3. ENTREGA 3 — COLETORES COMPLEMENTARES/NOTURNOS (começar PEQUENO: 1 coletor, 1 vertical)

### 3.1 Proposta da fase 1 — UM coletor DSN, vertical NACIONAL, fontes oficiais

- **Por quê nacional/oficial:** é o buraco exato que a CL-009 apontou (manhã 05:25/07:25 = `todas_pautas_ja_rascunhadas_24h` numa manhã cheia) e o pedido formal original de 02/09. As fontes oficiais (Câmara, Senado, STF, TSE, TCU, DOU, Planalto) **publicam de manhã cedo** — o antídoto do dedupe da madrugada, e são primárias (fonte da fonte, sem paywall/botwall).
- **Fontes fase 1 (RSS oficial público, sem chave):** Agência Câmara (RSS), Agência Senado (RSS), STF notícias (RSS), TSE, TCU, Planalto, DOU (seção 1). Agência Brasil entra na fase 2 (deu 404 na sondagem 02/09 — precisa de prospector de saúde antes). Total ~6-7 feeds.
- **Cadência:** 3-4 corridas/dia concentradas no buraco/manhã: **06:15 · 07:15 · 08:15 BRT** (cobrem o pós-buraco 03:48-06:48 e alimentam a manhã cheia antes dos ciclos humanos) + **1 sonda 23:45** (fuso invertido fica p/ fase 2). Burst ≤25 itens/entrega. NÃO é 15 em 15 min: o buraco é pontual e o guardião da fila já pede mais quando seca — o robô DSN é complemento fino, não redundância ruidosa.
- **Chave:** **NENHUMA na captura** (RSS + trafilatura no HTML final = texto oficial ≥800 direto). **Nenhum LLM na fase 1** — a tese do V4.1 ancora no corpo da notícia oficial; resumo/nota com qwen3.8-flash/glm-5-turbo (reserva) fica como opção do ZM para itens que precisarem de complemento. **Sol: PROIBIDO** (regra de ouro, item 4).
- **Onde roda:** Tencent (nuvem — o pedido explícito do Miguel), cron leve com flock próprio, estado/log/telemetria próprios; entrega pelo repo (item 1).

### 3.2 Fase 2 (futuro — só após o degrau 1 provado)

- **Critério de avanço:** 2 semanas de entregas da fase 1 com dedupe zero-conflito, frescor provado (item_key novo + published_at na janela) e 0 alerta vermelho.
- Candidatos: fuso invertido (Ásia/Oceania — jornais que amanhecem na nossa madrugada: Japão/Austrália/Coreia) e demais verticais famintas (economia: TCU/BCB comunicados). Avaliar UMA de cada vez — nunca multiplicar sem o degrau anterior com prova.

---

## 4. ENTREGA 4 — REGRA DE OURO + FLUXO DE DECISÃO (resumo do que o bloco manda)

1. **Chave LEVE sempre** no coletor DSN (nenhuma na captura; qwen3.8-flash/glm-5-turbo no máximo p/ resumo de inédita, se o ZM quiser). **O Sol é sagrado e SÓ do redator** — prova de hoje: 13/13 chamadas `tese_frontier` (estudo us65 + INBOX 09:10). Custo estimado fase 1: ~US$ 0/dia (sem LLM).
2. **Fluxo:** esta proposta (Ideias) → **DS-N Chefe OPINA** → decisão final + **✓ do Miguel** → execução por quem tem mão (ZM: adapter no NYC; executor com credencial na Tencent: cron do produtor). Nada executado pelo Ideias (Lei de Poderes).
3. **Nenhum robô invisível:** toda entrega logada (`entregas.log` + commit no repo + linha no monitor + telemetria por LLM).
4. **Telemetria é pré-requisito** (regra da casa 02/09) — o coletor só entra em produção com contagem visível.

---

## 5. PLANO DE EXECUÇÃO (passos numerados — protocolo da casa: backup → prova → registro → rollback escrito)

- **P0 — Decisão:** parecer do DS-N Chefe + ✓ do Miguel (hoje, prazo do bloco). Sem isso, nada abaixo acontece.
- **P1 — Adapter (ZM, NYC):** módulo leitor do JSONL DSN no robô único (ou cron próprio */15 com flock). Backup nomeado → py_compile → INSERT OR IGNORE com validação fail-closed → `entregas.log` + estado de último arquivo → ROLLBACK_INDEX seção `V41_ADAPTER_DSN_20260904`. Prova: injeção de 1 JSONL de teste (3-5 itens fictícios de fonte oficial) → fila nacional mostra os itens → conferência no ciclo.
- **P2 — Produtor (executor Tencent, modo observação 1º):** implementar o rascunho §6.1; rodar 1 corrida manual com `--dry-run` (gera JSONL em pasta de staging, NÃO entrega) e conferir: item_key correto, published_at ISO-UTC, ≥800 chars, ≤25 itens, sem segredo em lugar nenhum.
- **P3 — Prova E2E:** 1 entrega real de 1-5 itens de fonte oficial (Câmara/Senado) via repo → adapter → fila nacional (`SELECT` read-only ou seção FILA do monitor) → dedupe: re-entregar o MESMO arquivo = 0 itens novos (idempotência).
- **P4 — Registro:** `entregas.log` + estado + linha no monitor + telemetria DSN-F (0 LLM na fase 1) + este arquivo como registro da arquitetura.
- **P5 — Rollback escrito:** seção no ROLLBACK_INDEX: `ativo=false` no config do produtor (para) · remoção da linha de cron com backup do crontab · adapter sem efeito retroativo (só insere). Reversível em <5 min, sem tocar em nada do V4.1.

### Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Duplicação com o V4.1 (mesma pauta nas 2 fontes) | item_key compartilhado (OR IGNORE) + métrica de duplicatas cruzadas; fontes oficiais não estão nos feeds atuais |
| Nota curta oficial (<800 chars) | trafilatura no corpo completo da página; se ainda <800: descarta + conta (régua do multiidioma) |
| published_at ausente/mal formatado (agências variam) | gate fail-closed no adapter (obrigatório ISO-UTC) — frescor depende dele; rejeição logada |
| Fonte cai/404 (ex.: Agência Brasil) | prospector de saúde de feed (padrão V4.1: 6 falhas = aposenta, retry 6h) + alerta de fonte silenciosa (vigia camada A) |
| Escopo vazar (multiplicar coletor antes da prova) | fase 1 travada em 1 coletor/1 vertical; avanço só com o critério da §3.2 |
| Segredo/vazamento | nenhuma chave no coletor (captura sem LLM); valores de chave JAMAIS no repo/ponte (§82) |

---

## 6. RASCUNHOS (dentro do arquivo — NUNCA em produção; Lei de Poderes)

### 6.1 `dsn_coletor_nacional.py` (esqueleto — produtor fase 1, Tencent)

```python
#!/usr/bin/env python3
# RASCUNHO — DSN coletor nacional fase 1 (fontes oficiais). Nada disto roda em produção sem P0-P5 + ✓ Miguel.
# Uso: dsn_coletor_nacional.py [--dry-run]   (--dry-run gera em staging, não entrega)
import hashlib, json, sys, time, urllib.request
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

FEEDS_OFICIAIS = [  # RSS oficiais públicos — fase 1 (Câmara/Senado/STF/TSE/TCU/DOU/Planalto)
    # {"nome": "ag_camara",      "rss": "https://www.camara.leg.br/noticias/rss/"},
    # {"nome": "ag_senado",      "rss": "https://www12.senado.leg.br/noticias/rss"},
    # {"nome": "stf_noticias",   "rss": "http://www.stf.jus.br/portal/rss/noticiaRss.asp"},
    # {"nome": "tse",            "rss": "https://www.tse.jus.br/comunicacao/noticias/rss"},
    # {"nome": "tcu",            "rss": "https://portal.tcu.gov.br/noticias-rss/"},
    # {"nome": "planalto",       "rss": "https://www.gov.br/planalto/pt-br/ultimas-noticias/rss"},
    # {"nome": "dou_secao1",     "rss": "https://www.in.gov.br/consulta/rss"},
]
UA = {"User-Agent": "Mozilla/5.0 (DSN-coletor-casa/0.1; contato interno)"}
MAX_ITENS = 25          # burst máximo por entrega (regra ZM)
TEXTO_MIN  = 800        # corpo mínimo p/ a tese ancorar (regra ZM)

def item_key(url):      # sha1[:16] da URL canônica = chave do dedupe (regra ZM)
    return hashlib.sha1(url.encode()).hexdigest()[:16]

def iso_utc(dt):        # published_at SEMPRE ISO 8601 UTC (regra ZM)
    return dt.astimezone(timezone.utc).isoformat()

def baixar(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "replace")

def parse_feed(rss_url):
    """Extrai (title, url, published_at) do RSS. Corpo >= 800 vem da página final (trafilatura/leitura simples)."""
    out = []
    root = ET.fromstring(baixar(rss_url))
    for it in root.iter("item"):
        t = (it.findtext("title") or "").strip()
        u = (it.findtext("link") or "").strip()
        p = (it.findtext("pubDate") or "").strip()
        if t and u:
            out.append({"title": t[:140], "url": u, "published_at_raw": p})
    return out

def montar_entrega(dry_run=False):
    linhas, log = [], []
    for feed in FEEDS_OFICIAIS:
        try:
            for it in parse_feed(feed["rss"])[:5]:        # máx 5/feed (régua do nacional direto)
                corpo = baixar(it["url"])                 # simplificação de rascunho: leitura do HTML
                texto = corpo  # aqui entraria a extração de texto (trafilatura) p/ >= 800
                if len(texto) < TEXTO_MIN:
                    log.append({"fonte": feed["nome"], "url": it["url"], "motivo": "texto_curto"})
                    continue
                published_at = datetime.now(timezone.utc)  # rascunho: do RSS/pubDate parseado
                linhas.append({
                    "item_key": item_key(it["url"]),
                    "title": it["title"],
                    "url": it["url"],
                    "source_name": feed["nome"],
                    "source_type": "dsn",
                    "published_at": iso_utc(published_at),
                    "text_content": texto,
                })
        except Exception as e:
            log.append({"fonte": feed["nome"], "erro": str(e)})  # fail-open por fonte
    if dry_run or not linhas:
        print(json.dumps({"dry_run": dry_run, "itens": len(linhas), "log": log}, ensure_ascii=False))
        return
    nome = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M_") + "dsn_nacional.jsonl"
    with open(nome, "w", encoding="utf-8") as f:          # staging → repo → adapter (P3)
        for l in linhas[:MAX_ITENS]:
            f.write(json.dumps(l, ensure_ascii=False) + "\n")
    print(json.dumps({"entrega": nome, "itens": min(len(linhas), MAX_ITENS), "log": log}, ensure_ascii=False))

if __name__ == "__main__":
    montar_entrega(dry_run="--dry-run" in sys.argv)
```

> Nota de rascunho: a extração de corpo real (trafilatura) e o parse correto de pubDate ficam na implementação P2; o esqueleto acima fixa o CONTRATO (formato JSONL ZM + item_key + burst ≤25 + fail-open por fonte).

### 6.2 `dsn_vigia_madrugada.py` (esqueleto — camada B Tencent, read-only, 1/h na janela 00:00-08:00 BRT)

```python
#!/usr/bin/env python3
# RASCUNHO — vigia de madrugada camada B (Tencent, DS-N Ideias). Read-only: REST público do espelho + ponte.
# Alerta só com 2+ leituras cruzadas (lição caçadas 16/18). Quem alerta no Telegram: relatório 4/4h do Chefe.
import json, sys, time, urllib.request
from datetime import datetime, timezone

ESPELHO = "https://cafezinho.news/wp-json/wp/v2/posts"   # REST público (já usado nas sondas V42MON)
JANELA   = (0, 8)     # 00:00-08:00 BRT (o buraco)
PISO_ENTREGAS = 8     # metade da baseline 17-24/h → abaixo disso por 2h = 🟠

def posts_por_hora(horas=6):
    """Proxy de frescor: quantos posts o espelho publicou por hora (baseline dia 2-4/h; madrugada dedupe ~0)."""
    url = f"{ESPELHO}?per_page=100&_fields=id,date&orderby=date&order=desc"
    with urllib.request.urlopen(url, timeout=15) as r:
        posts = json.load(r)
    por_hora = {}
    for p in posts:
        h = p["date"][:13]  # "2026-09-04T05"
        por_hora[h] = por_hora.get(h, 0) + 1
    return por_hora

def main():
    agora = datetime.now(timezone.utc)
    h_brt = (agora.hour - 3) % 24
    if not (JANELA[0] <= h_brt < JANELA[1]):
        print("fora_da_janela"); return
    ph = posts_por_hora()
    # 2 leituras: REST agora + relatório 4/4h do Chefe na ponte (volume/rc) — a camada A (NYC) faz a leitura profunda.
    leituras = {"rest_h": len(ph)}
    # 🟠 se a última hora útil (06:00-08:00 BRT) publicou 0 e o dia começou com a régua do Chefe
    # (leitura única NUNCA alerta — imprime estado p/ o monitor e deixa a decisão p/ 2ª leitura)
    print(json.dumps({"h_brt": h_brt, "leituras": leituras,
                      "regra": "2_leituras_obrigatorias; alerta via relatorio_4h_do_Chefe"}, ensure_ascii=False))

if __name__ == "__main__":
    main()
```

> Nota de rascunho: camada A (NYC, dono ZM) é quem enxerga rc/robos.log/entregas — o script acima é a parte que o DS-N consegue rodar sem credencial (REST público + ponte), honesta com a Lei de Poderes.

---

## 7. O QUE ESTE ESTUDO NÃO FAZ (limites)

- NÃO cria/instala cron nenhum, NÃO toca NYC, NÃO insere nada em fila, NÃO publica. Execução = P0 (✓ Miguel) + P1-P5 (ZM/executor com credencial).
- NÃO decide o ponto físico de entrega (repo vs sync) — recomenda repo; a decisão final é do ZM (dono do pipeline) sob o parecer do Chefe.
- NÃO inclui segredo/valor de chave em lugar nenhum (captura sem LLM; nenhuma chave no arquivo).

**Síntese para o Chefe (fluxo do bloco):** proposta apresentada — aguardo teu parecer p/ levar ao ✓ do Miguel ainda hoje. Nada em produção (Lei de Poderes).

— DS Nuvem Ideias (DS-N Ideias) · 20260904 08:48:54 BRT
