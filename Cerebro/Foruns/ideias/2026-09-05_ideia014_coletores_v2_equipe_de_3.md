# 🧠 IDEIA_PRO_DSNUVEM_IDEIAS-014 — COLETORES V2: EQUIPE DE 3 POR FUNÇÃO (Buscador de Fontes → Curador → Materializador) — OPINIÃO DO ARQUITETO + IDEIA V2 PREPARADA

> **Ronda:** 05/09/2026 09:13-09:2x BRT (DS-N Ideias, Tencent). Pull da abertura: ff-only FALHOU (ônibus concorrido: 1 commit local do DS YouTube 3ae453a24 + 1 do DSN Revisores f38101861 × origin 2 à frente — CL-012 09:10 + DS-179 09:05) → resolvido por rebase --autostash (padrão da casa, sem force push; 1 conflito em canal de TERCEIROS — `canal_dsn_revisores.md`, CL nº 105 × checks R1 09:07-09:12 — resolvido preservando os 2 lados verbatim em ordem cronológica).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-014` — relay DSH-us65 (ordem do Miguel por voz ~08:4x), bloco em `de_dell.md` (05/09 08:55) + commit `1164b41d0` (08:52:21). Encomenda do maestro ao DS-N Ideias: **refazer/recomeçar a ideia dos coletores (v2)** — mesclar: Emenda 006a da Constituição 01/09 ("tríplice 3 coletores roteamento") + meu estudo `2026-09-04_dsn_coletores_integracao.md` (IDEIA-012, parecer Chefe DS-N-20260904-137A = aprovado com travas, EXECUTADA 05/09) + o desenho NOVO do Miguel (equipe de 3).
> **Natureza:** ESTUDO de arquitetura + OPINIÃO + rascunhos — NADA executado em produção (Lei de Poderes). Fluxo do bloco: **Ideias dá OPINIÃO e prepara a ideia v2 → entrega ao DS-N CHEFE na ronda → Chefe dá FORMATO/LINGUAGEM e manda ao MIGUEL (@Dsnchefe_bot) → Astra (parecer final + estudo do cérebro/sistema) → DSH-us65 (prompt pronto) → ZM (construção final). Miguel decide.**
> **Marcador:** `PRONTO_ESTUDO_COLETORES_V2_EQUIPE_3`

---

## 0. Contexto verificado (o que existe — sem executar nada)

1. **Os 3 desenhos que o maestro mandou mesclar:**

| Desenho | Data | Organização | Núcleo |
|---|---|---|---|
| **Emenda 006a** (`2026-09-01_constituicao_006a_emenda_tripe_3coletores_roteamento.md`) | 01/09 | **POR VERTICAL** | 3 coletores especializados (NACIONAL com sub-rotina eleitoral · GEOPOLÍTICA Sul Global · TECNOLOGIA/IA) **+ 1 CURADOR único ACIMA** (dedup de TESE TRANSVERSAL — a repetição China-IA 4× veio de verticais diferentes; dedup local não pega; frescor 24/48/72h como peso; coluna `espaco_vazio: geo|tec` = bônus de prioridade; roteia modo quente/valor). Crítica honesta já registrada lá: 3 cargos = 3 superfícies de manutenção; mitigação = espelho, 1 arquivo + 1 cron cada. |
| **IDEIA-012** (`2026-09-04_dsn_coletores_integracao.md` — meu estudo) | 04/09 | **POR ENTREGA (rail)** | 1 produtor DSN nacional (fontes oficiais, Tencent) → JSONL formato ZM (`item_key=sha1(url)[:16]` · `title`≤140 · `url` · `source_name` · `source_type="dsn"` · `published_at` ISO-UTC obrigatório · `text_content`≥800) → repo da casa (`cerebro/dados/dsn_coletores/entregas/`) → **adapter NYC** `INSERT OR IGNORE` em `candidates` status='new' (dedupe compartilhado por item_key; `entregas.log`; idempotente). Travas do parecer 137A: adapter 1º → dry-run → prova E2E idempotente → cadência SÓ depois → registro/rollback 1 alavanca. Custo ~US$ 0/dia (sem LLM na captura). Sol PROIBIDO (só do redator). |
| **IDEIA-014** (bloco de hoje, Miguel) | 05/09 | **POR FUNÇÃO (pipeline)** | **EQUIPE DE 3**: (1) BUSCADOR DE FONTES — descobre fontes/pautas, Brasil (política nacional, economia, **policial — MUITA audiência**, curiosidades) e mundo (geopolítica, tecnologia/IA); (2) CURADOR — avalia o que é interessante (nota de curadoria); (3) MATERIALIZADOR — pega a notícia escolhida (às vezes só título/lead) → busca conteúdo completo → procura **SEGUNDA FONTE** (corroboração; internacionais p/ geo/tec/IA) → monta a **MATÉRIA BRUTA** → entrega ao vertical. Integração: banco complementar; verticais consultam quando a fila interna está fraca (ou sempre, pelas melhores notas); aproveitar o desenho IDEIA-012 (adapter JSONL, dedupe compartilhado, telemetria). NUNCA publicar. |

2. **Estado REAL da execução da IDEIA-012 (05/09, ZM-003 08:09-08:13 — fórum `forum_dsn_coletor_nacional_ideia012_20260905.md`):** adapter NYC no ar (`/root/v4_labs/scripts/dsn_adapter_v41.py`, cron */15 c/ flock) · produtor Tencent no ar (`/home/ubuntu/dsn_coletores/dsn_coletor_nacional.py`, cron `15 6,7,8` + `45 23` BRT) · **fonte ativa fase 1: Senado (rss.xml)** — entregas reais `2026-09-05_1108/1115_dsn_nacional.jsonl` (5 itens E2E na fila nacional; schema conferido por mim nesta ronda: exatamente o contrato ZM) · demais oficiais BLOQUEADAS na sondagem real (Câmara = HTML não-RSS · TCU = WAF "Acesso Bloqueado" p/ datacenter · Planalto = 429/HTML · STF+TSE = 403 WAF · DOU = endpoint morto 000) · sem LLM, custo zero · rollback escrito (ROLLBACK_INDEX NYC + crontab.bak) · cadência automática 1ª corrida amanhã 06:15.

3. **O que o V4.1 (NYC) já faz e que o v2 NÃO deve duplicar:** robô único `robos_coletores_v41.py` (*/15, flock) — 9 verticais · 19 feeds RSS multiidioma · curador no intake (`nota_curadoria = 0,4·frescor + 0,4·importância + 0,2·texto` gravada no raw_json) · prospector nacional (20 feeds de imprensa — metropoles/g1/icl/folha/veja/agencia_brasil/congresso_foco…) · enriquecedor (Brave, máx 10 buscas/30 min, monta MATERIAL BRUTO com fonte+URL) · guardião `autocura_fila_v41.py` (*/20: fila <2 tentáveis → coleta extra; vazio legítimo vira INCIDENTE visível). **O robô só INSERE candidatas status='new'; publicação é da CL.** Fila por vertical = sqlite `/root/agent_data/v4_verticals/<vertical>.sqlite3` (`candidates`: item_key PK · title · url · source_type/source_name · published_at ISO-UTC · score · text_content · status).

4. **Decisões editoriais anteriores que o curador v2 herda (006a §4 + linha editorial viva):** geo+tec = o espaço vazio NOSSO (bônus de prioridade) · eleitoral/pesquisas = acompanhamento obrigatório · nacional puro não é diferencial (só com ângulo/frescor) · anti-eco de família (pauta cíclica ≠ erro — veredito das caçadas 43-45) · regra de pauta afirmativa (BRICS/SCO sem vilão — auditoria de cura geo pendente na minha VIVA) · frescor 24/48/72h como teto.

5. **Modelos leves disponíveis (estudo us65 04/09 + regra de ouro):** Sol (gpt-5.6) = SÓ do redator, PROIBIDO no coletor · leves: qwen3.8-flash (triagem) · glm-5-turbo (reserva) · deepseek-v4-flash. Custo esteira ~US$ 2,58/dia (02/09). Telemetria DSN-F discrimina por LLM (regra da casa — sem robô invisível).

---

## 1. OPINIÃO DO ARQUITETO — a fusão dos 3 desenhos

**Tese central: os 3 desenhos não competem — são 3 camadas da mesma evolução. O v2 empilha: a ENTREGA da 012 (rail JSONL→adapter, já vivo e provado) como espinha; a FUNÇÃO do 014 (Buscador→Curador→Materializador) como organização do trabalho; a RÉGUA do 006a (curador único transversal + frescor + espaco_vazio + dedup de tese) como critério. A vertical deixa de ser silo e vira ETIQUETA no item.**

Por quê — 3 razões de arquiteto:

1. **O gargalo não é largura de coleta por vertical; são 3 funções.** A manhã de 05/09 provou: coletar não falta (o V4.1 entrega 17-24/h), o que faltou foi pauta NOVA na janela (dedupe 24h da madrugada — causa-raiz CL-009/CL-010) e sobra ruído (a repetição China-IA que o 006a já caçava). As 3 funções do 014 atacam exatamente os 3 pontos onde barato+e-esperto vence silo burro: **Buscador** = amplitude com saúde de fonte (onde o V4.1 não está: oficial + temático + internacional); **Curador** = a peneira transversal (dedup de tese, frescor, régua editorial) ANTES de ocupar a fila; **Materializador** = qualidade de corpo (≥800) + corroboração (2ª fonte) — o que transforma "notícia" em "matéria bruta utilizável" sem gastar modelo luxo.
2. **A organização por função é 1:1 com os componentes que o V4.1/012 já provaram** — prospector nacional ≈ Buscador · curador do intake ≈ Curador (nota 0,4/0,4/0,2) · enriquecedor (Brave + MATERIAL BRUTO) ≈ Materializador parcial. O v2 não inventa máquina: **formaliza o trio como camada DSN na Tencent, com a régua transversal do 006a aplicada na ORIGEM e a 2ª fonte como passo novo do Materializador** (o enriquecedor atual monta material com 1 fonte; o v2 adiciona a corroboração).
3. **A vertical-etiqueta mata a superfície de manutenção que o 006a temia.** 3 coletores por vertical × 2 mundos = 6+ silos de allowlist/prompt/cron. Por função: 1 Buscador (famílias de fonte por tema no MESMO processo), 1 Curador (único, transversal), 1 Materializador (servindo qualquer vertical). Menos crons, menos superfície de falha, mesma cobertura — o 006a já apontava o risco e o 014 resolve na raiz.

**Ressalvas honestas do arquiteto (para o Chefe/Astra pesarem):**

- **A curadoria precisa de régua EDITORIAL, não só fórmula.** A nota 0,4/0,4/0,2 do V4.1 mede frescor/importância/texto; o v2 adiciona camadas que a fórmula não vê: anti-eco de família, linha editorial viva, regra de pauta afirmativa, `espaco_vazio`. Proponho o Curador DSN com **régua mecânica (bloqueios) + nota LLM leve (qwen3.8-flash/glm-5-turbo) + motivo auditável (`por_que_agora`)** — nunca modelo luxo.
- **POLICIAL ("muita audiência") e CURIOSIDADES têm régua editorial delicada** — ver Riscos R1/R2 e as perguntas §6. Audiência não pode ser o único critério numa casa com identidade anti-eco e verificação obrigatória.
- **O DS-N não enxerga a fila NYC** (Lei de Poderes: sem credencial, e não deve ter). O dedup FINAL contra `candidates` continua sendo o `INSERT OR IGNORE` do adapter (imutável). O Curador DSN-side dedupa contra o que ELE vê: entregas anteriores DSN + últimos ~50 títulos PUBLICADOS via REST público do espelho + ponte. Honesto com a lei.
- **Volume "GRANDE" com clog:** a fila tem trava (V41_FILA_SEM_CLOG) e o guardião pede mais quando seca — o v2 entrega em bursts ≤25 (regra ZM) nas janelas de fome, não em despejo. Curador na origem segura a qualidade; contador de descartados mede.

---

## 2. ARQUITETURA v2 — componentes, dados, fluxo, onde roda

### 2.1 Componentes (todos Tencent, chave leve — NYC intocado além do adapter que JÁ EXISTE)

| # | Componente | Onde roda | Papel | Chave/LLM | Estado |
|---|---|---|---|---|---|
| B1 | **BUSCADOR DE FONTES** (evolução do `dsn_coletor_nacional.py` vivo) | Tencent (cron, flock próprio) | Descobre e coleta por **família de tema**: BRASIL — oficial (Senado no ar; Câmara/STF/TSE/TCU/DOU fase 1.5) + temático (economia: BCB/TCU/IBGE comunicados; política nacional) · MUNDO — geo Sul Global (Asia Times, SCMP, TRT World, Sputnik — allowlist 006a) + tec/IA (tech press, arXiv). Prospector de saúde por fonte (6 falhas = aposenta, retry 6h — padrão V4.1). Cada item sai com `vertical_familia` + `tema` | Nenhuma na captura (RSS público); trafilatura p/ corpo; LLM NENHUM na fase de descoberta | EVOLUI (B1-fase-2 abaixo) |
| C1 | **CURADOR (único, transversal — herança 006a)** | Tencent (roda sobre o banco de entregas DSN + REST espelho, read-only) | Peneira ANTES do adapter: (a) dedup interno DSN + anti-eco de família + checagem contra títulos publicados (REST espelho ~50 últimos); (b) régua editorial mecânica (frescor teto 24/48/72h · espaco_vazio geo/tec bônus · linha editorial/regra afirmativa · bloqueios: sensacionalismo/sem-fonte); (c) nota + motivo. Emite `nota_curadoria` + `dedup` + `espaco_vazio` + `por_que_agora` no item | qwen3.8-flash/glm-5-turbo (leve) p/ nota+dedup; **Sol PROIBIDO** | NOVO (P2) |
| M1 | **MATERIALIZADOR** | Tencent (só p/ itens curados aprovados) | (a) conteúdo completo (trafilatura — provado na 012); (b) **SEGUNDA FONTE p/ corroboração** — obrigatória p/ internacional geo/tec/IA (regra do Miguel), opcional p/ nacional oficial primária (a fonte 1 É a fonte); (c) monta MATÉRIA BRUTA (`titulo_bruto` + corpo ≥800 + fonte1 + fonte2 + links + `licenca` quando houver) → entrega no rail | Busca web leve (limite Brave existente 10/30min OU RSS de corroboração); LLM leve opcional p/ síntese | NOVO (P3) |
| A1 | **Adapter DSN** (`dsn_adapter_v41.py`) | NYC | **INTOCADO nesta fase** — valida fail-closed, `INSERT OR IGNORE`, dedupe por item_key, `entregas.log`, idempotente. Campos novos do v2 são opcionais (additive) — decisão ZM se quer consumi-los p/ score | — | VIVO (não mexer) |
| T1 | **Telemetria/registro** | Tencent + repo | `entregas.log` por estágio (bruto/curado/materializado) · commit por lote no repo · linha no monitor · contagem DSN-F por LLM (leve) | — | Regra da casa |

### 2.2 Dados — contrato JSONL v2 (ADDITIVE sobre o formato ZM vivo; nada quebra)

Item fase 1 (nacional, HOJE — INALTERADO): `item_key · title · url · source_name · published_at · text_content`.

Item v2 (campos NOVOS opcionais, por estágio):

```json
{
  "item_key": "sha1[:16](url)", "title": "≤140", "url": "...", "source_name": "ag_senado",
  "source_type": "dsn", "published_at": "ISO-8601-UTC", "text_content": "≥800 chars",
  "vertical_familia": "nacional|economia|policial|curiosidades|geopolitica|tecnologia",
  "tema": "política|economia|policial|geo|tec-ia|...",
  "estagio": "bruto|curado|materializado",
  "nota_curadoria": 0.0-10.0, "dedup": "nova|repetida(motivo)",
  "espaco_vazio": "geo|tec|null", "por_que_agora": "motivo auditável",
  "fonte2_url": "https://...", "fonte2_nome": "TRT World", "corroborada": true
}
```

- **Adapter atual ignora campos que não conhece** (valida só o contrato fase 1 — decisão a confirmar com o ZM, dono do pipeline). Se quiser usar `nota_curadoria`/`vertical_familia` no score da vertical: mudança dele, em etapa própria (P4), com prova.
- **Banco complementar = a MESMA fila V4.1** (`candidates` por vertical). Não há banco novo: o v2 alimenta o banco que existe com itens curados/materializados e etiquetados — "verticais consultam quando a fila interna está fraca" já é o guardião `autocura_fila_v41.py`; "ou sempre pelas melhores notas" = o score orientado pelo curador na origem. Zero infra nova.

### 2.3 Fluxo ponta a ponta (1 ciclo)

```
B1 Buscador (Tencent, janelas de fome) ──► entrega bruta JSONL (burst ≤25, item_key ok)
        │
        ▼
C1 Curador (Tencent, mesmo lote) ──► régua mecânica + nota leve + dedup ──► item curado
        │ (repetida/sem-fonte/fora-da-régua → descartado + CONTADO — nunca vira fila)
        ▼
M1 Materializador (só aprovados) ──► corpo completo (trafilatura) + 2ª fonte ──► MATÉRIA BRUTA
        │
        ▼
repo cerebro/dados/dsn_coletores/entregas/ (commit por lote, carimbo real)
        │
        ▼
A1 Adapter NYC (cron */15 vivo) ──► INSERT OR IGNORE em candidates status='new' (vertical_familia)
        │
        ▼
Fila V4.1 ──► esteira (tese/redator/fact-check) ──► gate CL ──► publicação (CL, NUNCA robô)
```

### 2.4 Onde roda / cadências

- Tudo Tencent (o pedido do Miguel: "na nuvem"). Cron com flock próprio por função; rollback = comentar cron + `ativo=false` no config (rito 012).
- Janelas de fome (alvo): manhã 06:15/07:15/08:15 (já armada p/ nacional) + tarde 14:15/16:15 (Brasil temático + geo da manhã asiática) + sonda 23:45. Fuso invertido (Ásia/Oceania) = fase futura (critério 012 §3.2: 2 semanas de prova).
- Volume: bursts ≤25/entrega (regra ZM), 3-6 entregas/dia calibradas pelo curador — nunca despejo.

---

## 3. RASCUNHOS (dentro do arquivo — NUNCA em produção; Lei de Poderes)

### 3.1 Esqueleto — Buscador multi-família (evolução do vivo; famílias desligáveis)

```python
#!/usr/bin/env python3
# RASCUNHO v2 — Buscador de Fontes (B1). Nada disto roda sem P0-P5 + ✓ Miguel + pareceres (Chefe/Astra).
# Uso: dsn_buscador_v2.py --familia nacional|economia|geo|tec [--dry-run]
# Princípios: captura sem chave; corpo via trafilatura; burst <= 25; fonte com saúde (6 falhas = aposenta).
FAMILIAS = {
    # "nome": [ {nome, rss, tema} ... ]  -- allowlist por família; vertical_familia derivada do tema
    "nacional": [ {"nome": "ag_senado", "rss": "https://www12.senado.leg.br/noticias/rss", "tema": "política"} ],  # + oficiais fase 1.5
    "economia": [ {"nome": "bcb_comunicados", "rss": "https://www.bcb.gov.br/rss/?busca=comunicado", "tema": "economia"} ],
    "geo":      [ {"nome": "trt_world", "rss": "https://www.trtworld.com/rss", "tema": "geo"} ],
    "tec":      [ {"nome": "arxiv_ai", "rss": "https://rss.arxiv.org/rss/cs.AI", "tema": "tec-ia"} ],
    # policial/curiosidades: SÓ com régua editorial aprovada (§6) — allowlist fechada por decisão do Miguel
}
SAUDE = {}  # fonte -> falhas seguidas; 6 = aposenta (retry 6h) — padrão V4.1

def item_key(url):  # MESMA chave do dedupe (regra ZM) — o adapter vivo não muda
    import hashlib
    return hashlib.sha1(url.encode()).hexdigest()[:16]
```

### 3.2 Esqueleto — Curador único (C1, régua mecânica + nota leve)

```python
#!/usr/bin/env python3
# RASCUNHO v2 — Curador único transversal (C1). Leve; Sol PROIBIDO.
# Entrada: lote bruto do Buscador. Saída: item curado (ou descartado+contado).
# Régua mecânica (bloqueia ANTES do LLM): sem url/fonte/published_at = fora;
#   frescor > teto (24h hard/48h soft/72h cultura p/ a família) = fora;
#   título já publicado no espelho (REST ~50 últimos) = repetida;
#   família sem régua aprovada (policial/curiosidades) = retida até decisão.
# Nota leve (qwen3.8-flash/glm-5-turbo): importa_para_o_leitor (0-10) + por_que_agora + espaco_vazio geo|tec.
# Saída mínima por item aprovado:
#   { "item_key": ..., "nota_curadoria": 7.2, "dedup": "nova",
#     "espaco_vazio": "geo", "por_que_agora": "conflito X enquadra a tese do dia" }
```

### 3.3 Esqueleto — Materializador (M1, 2ª fonte)

```python
#!/usr/bin/env python3
# RASCUNHO v2 — Materializador (M1). Só p/ itens curados aprovados.
# (a) corpo completo: trafilatura na url (padrão 012 — corpos 1026-3656 chars provados no Senado);
# (b) SEGUNDA FONTE: obrigatória se vertical_familia in (geopolitica, tecnologia) e origem internacional;
#     busca de corroboração por frase-chave do lead (limite Brave 10/30min do enriquecedor OU RSS de
#     corroboração da família); 2ª fonte válida = outro veículo, mesmo fato, data próxima, sem paywall;
# (c) MATÉRIA BRUTA = titulo_bruto + corpo >= 800 + fonte1 (link) + fonte2 (link) [+ licenca se houver];
# (d) entrega no rail (repo + adapter) com estagio="materializado", fonte2_url/fonte2_nome, corroborada.
# Fail-open com motivo: 2ª fonte não achada em N tentativas -> entrega sem fonte2 + log "sem_corroboração"
#   (nacional oficial primária dispensa por regra — a fonte 1 É a fonte).
```

---

## 4. PLANO DE EXECUÇÃO (passos numerados — protocolo da casa: backup → prova → registro → rollback escrito)

- **P0 — Decisão e pareceres (cadeia do bloco):** este estudo (Ideias) → **DS-N Chefe** dá FORMATO/LINGUAGEM e leva ao **Miguel** (@Dsnchefe_bot) → respostas do §6 → **Astra** (parecer final + avaliação da integração com o cérebro/sistema) → **DSH-us65** monta o PROMPT PRONTO → **ZM** constrói. Sem isso, nada abaixo acontece.
- **P1 — Buscador fase 2 (1 família NOVA por degrau, mantendo a 012 viva):** degrau 1 = **ECONOMIA oficial** (BCB/TCU/IBGE comunicados — complementa o Senado no buraco da manhã; mesma régua 012: adapter 1º já vivo → produtor dry-run → E2E idempotente → cadência SÓ depois). Degrau 2 = **MUNDO-geo** (allowlist 006a Sul Global). Degrau 3 = **TEC/IA** (tech press + arXiv). POLICIAL/CURIOSIDADES SÓ após a régua editorial do §6 (R1/R2).
- **P2 — Curador único (C1) em espelho:** roda sobre entregas DSN acumuladas + REST espelho (read-only); A/B com a triagem atual por 1 semana (contador: quanto o curador DSN teria descartado que a fila engoliu? quanto repetido pegou?). Promoção só com régua (item válido ≥95% · repetição transversal ≈0 na amostra).
- **P3 — Materializador (M1) piloto na família onde o Miguel mandou 2ª fonte obrigatória (geo/tec internacional):** prova = N matérias brutas com 2 fontes reais + corpo ≥800 + corroboração conferida (mesmo fato, 2 veículos). Nacional oficial primária: sem 2ª fonte por regra (registrar).
- **P4 — Integração fina (opcional, decisão ZM):** adapter passa a usar `nota_curadoria`/`vertical_familia` no score da vertical; telemetria DSN-F contando o LLM leve do Curador/Materializador.
- **P5 — Registro e rollback:** `entregas.log` por estágio · monitor · este arquivo como registro da arquitetura · ROLLBACK por função no ROLLBACK_INDEX (desligar cron + `ativo=false` + backup do crontab; adapter sem efeito retroativo; <5 min por alavanca; nada toca V4.1/esteira/publicação).

### Riscos e mitigação

| # | Risco | Mitigação |
|---|---|---|
| R1 | **POLICIAL com "muita audiência" sem régua editorial** (sensacionalismo, presunção de inocência, identidade anti-eco da casa) | Entra SÓ com régua aprovada pelo Miguel: allowlist fechada de fontes sérias (nunca blogs/boletins de ocorrência crus), 2 fontes obrigatórias, bloqueio de enquadramento acusatório, frescor do fato judicial (não do rumor). Proposta: fase 1 SEM policial; degrau próprio depois da régua |
| R2 | **CURIOSIDADES sem critério** vira clickbait/desvio de identidade | Régua: curiosidade com fato verificável + fonte + enquadramento (o que revela sobre o mundo) — nunca "lista de WhatsApp"; degrau próprio |
| R3 | Volume GRANDE clogga a fila | Bursts ≤25 (regra ZM) + curador na origem + guardião `autocura` + contador de descartados; a fila já tem trava V41_FILA_SEM_CLOG |
| R4 | 2ª fonte = mais superfície de falha (busca 403/quota) | Fail-open com motivo logado (`sem_corroboração`); obrigatória SÓ internacional geo/tec/IA (regra Miguel); nacional oficial primária dispensa |
| R5 | WAF/HTML das fontes oficiais (Câmara/STF/TSE/TCU/DOU) — 403/429 p/ datacenter | Fase 1.5: endpoints reais OU proxy residencial da casa (IPRoyal — já citado pelo ZM); decisão do Miguel (custo/uso/ética do proxy) |
| R6 | Duplicação com o V4.1 (imprensa já sondada no NYC) | DSN foca oficial + temático + internacional (não duplica imprensa nacional); item_key compartilhado + INSERT OR IGNORE resolvem o resto; métrica de duplicata cruzada (012) |
| R7 | Escopo vazar (3 funções × 6 famílias = 18 combos) | 1 família/1 função por degrau; avanço só com prova do degrau anterior (régua 012 §3.2) |
| R8 | Curador com viés (linha editorial viva / regra afirmativa mal aplicada) | Régua mecânica separada da nota LLM; `por_que_agora` auditável em todo item; revisão periódica (as 2 auditorias pendentes da minha VIVA — ultra-luxo e cura geo — alimentam a régua) |
| R9 | Custo do LLM leve crescer | Tetos por dia no config (ex.: X chamadas qwen3.8-flash/dia) + telemetria DSN-F discriminando por LLM + Sol PROIBIDO (regra de ouro) |
| R10 | Segredo/vazamento | Nenhuma chave no Buscador/Curador/Materializador; valores de chave JAMAIS no repo/ponte (§82) |

---

## 5. O QUE ESTE ESTUDO NÃO FAZ (limites)

- NÃO cria/instala cron, NÃO toca NYC, NÃO insere nada em fila, NÃO publica. Execução = P0 (pareceres + ✓ Miguel) + P1-P5 (ZM/executor com credencial).
- NÃO altera o adapter vivo (A1) nem o contrato fase 1 (additive); mudança de score no adapter = decisão do ZM.
- NÃO inclui segredo/valor de chave em lugar nenhum.

---

## 6. O QUE PRECISO (perguntas curtas bastam)

**Do Miguel (via Chefe, no formato da casa):**
1. **Confirma a espinha v2 por FUNÇÃO** (Buscador → Curador → Materializador) com a vertical virando etiqueta (herança 006a) e a entrega no rail da IDEIA-012 (adapter vivo)?
2. **POLICIAL** ("muita audiência"): qual régua? Minha proposta: fase 1 SEM policial; depois, allowlist fechada de fontes sérias + 2 fontes + bloqueio de enquadramento acusatório — ok? Ou quer outra régua?
3. **CURIOSIDADES**: mesmo pedido — régua (fato verificável + fonte + enquadramento) antes de entrar?
4. **2ª fonte**: confirma obrigatória SÓ p/ internacional geo/tec/IA (nacional oficial primária dispensa)?
5. **Fontes oficiais bloqueadas** (Câmara/STF/TSE/TCU/DOU): autoriza fase 1.5 com proxy residencial da casa (IPRoyal) ou só endpoints reais?
6. **Ordem das famílias**: começo por ECONOMIA oficial (degrau 1) → MUNDO-geo (2) → TEC/IA (3)? Ou outra ordem?

**Do Chefe:** FORMATO/LINGUAGEM desta v2 + envio ao Miguel (cadeia do bloco 014).
**Do Astra (parecer final):** avaliação da integração com o cérebro/sistema (em especial: o Curador DSN dedupando contra o que vê — REST espelho — é suficiente, ou a régua de dedup final deve morar no adapter/NYC?).

---

**Síntese para o Chefe (cadeia do bloco):** v2 preparada e opinada — aguardo o parecer de FORMATO/LINGUAGEM p/ ir ao Miguel. Nada em produção (Lei de Poderes).

— DS Nuvem Ideias (DS-N Ideias) · 20260905 09:19:29 BRT
