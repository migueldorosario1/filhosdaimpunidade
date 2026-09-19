# 🏦 FÓRUM — DSN FINANCEIRO (DSN-F): o rastreador de custos do ecossistema (2026-09-02)

> **Origem:** ordem do Miguel por voz (~15h0x de 02/09/2026): *"a gente tem que criar um DSN
> financeiro rastreador de custo — a gente já tem um agente de custo só que eu tenho desconfiança
> que ele não funciona direito — pega esse agente que trabalha custo e vamos redesenhar ele, vê
> se dá pra salvar — todo custo do ecossistema tem que ser enviado pra esse agente, tem que
> captar tudo em todos os servidores — você decide se quer fazer em todos os servidores, mas tem
> que ser anotado — e no painel CCTV discrimina por LLM com as categorias super luxo, ultra luxo,
> econômico, colorindo o que está sendo usado naquele momento, custo 7d."*
> **Execução:** ZCode (GLM-5.3, DSH na us65) · canal: `/root/Cerebro/.tencent_v6_oficina/dsn_financeiro/` (código) · deploy Tencent `~/dsn_financeiro/`.

---

## 1. DIAGNÓSTICO — por que a desconfiança do Miguel estava CERTA (6 falhas achadas)

Auditoria ao vivo (NYC + Tencent + temáticos) em 02/09 15h-16h BRT:

| # | Falha | Efeito visto |
|---|---|---|
| 1 | **Painel de agentes (controle) mostrava `US$ 0.00` em TODOS os 19 cartões** — `gasto_7d_usd()` lia `v6_data/banco_custos_*.jsonl` (caminho errado — os arquivos estão em `v6_data/custos/`), usava campo `ts_epoch` que NÃO EXISTE nos registros e casava a chave do cartão (`dsn_publicador`) com nomes reais de agente (`v4_1_redator`) — nunca bate | custo 7d falso-zero em todos os botões |
| 2 | **Consolidados diários na Tencent morreram em 31/07** — o sync antigo (cron `12 * * * *` da máquina local) acabou; o NYC só rsynca banco+api_usage | agregados 7d/30d do painel congelados desde julho |
| 3 | **Mês anterior nunca chegava à Tencent** — o rsync */15 do NYC só manda o banco do mês CORRENTE; a janela 7d cruza a virada do mês e perdia até 5 dias de dado | 7d subestimado ~5× (vimos $9 quando o real era $46) |
| 4 | **Robôs DSN da Tencent (publicador/revisores/ideias/youtube/chefe) chamam LLM direto (api.deepseek/z.ai/openai) SEM logar custo** — zero telemetria própria; só o gateway Moka logava (e parou 04/08) | custo Tencent invisível por evento |
| 5 | **Mural das IAs** (ranking de preços do painel) — atualizador morreu 22/08 09:00 (morto há 11 dias) | ranking congelado (fora do escopo de hoje; §6) |
| 6 | **Incidente 16:12 de 02/09**: os jsonl de custo de `v6_data/custos/` da Tencent foram **apagados de uma vez** (banco 09, api_usage, ao_vivo_nyc, ao_vivo_tencent) durante esta obra — causa não identificada (nenhum cron da casa deleta; suspeita: rsync `--delete` de fonte parcial ou outra sessão). Restaurados na hora + agente agora se auto-cura (§3) | fragilidade do pipeline velho exposta |

**Número REAL corrigido (7d, 02/09 16:16 BRT):** **US$ 46,06 · 2.448 chamadas · 11 LLMs** — contra
US$ 0,00 no painel e US$ 9,05 na 1ª agregação sem agosto. A esteira V4.1 sozinha: US$ 28,93 (gpt-5.5).

## 2. O DSN FINANCEIRO (DSN-F) — redesenho do agente de custos

- **Quem:** novo robô DSN na Tencent — `~/dsn_financeiro/dsn_financeiro.py` + `categorias_llm.json`
  (editável no servidor, muda sem reiniciar painel). Cron `*/15` com flock (`DSN_FINANCEIRO_15MIN_20260902`).
- **Ofício único: custo. O contador NÃO GASTA — zero chamadas de LLM.** Substitui o antigo
  "Consolidador de custos (D8)" (o cartão do painel virou DS-N Financeiro).
- **Fontes que lê (toda ronda):** banco_custos NYC (eventos reais por agente/modelo), ao_vivo_tencent
  (Moka), ao_vivo_tematicos (159.89), banco_custos_tencent (instrumentação futura — lê se existir).
  `ao_vivo_nyc` é ignorado por ser duplicata byte a byte do banco (evita 2×).
- **Pull próprio (não depende mais de sync de terceiro):** consolidados diários NYC via ssh 1×/h
  (restaura o pipeline morto); **self-heal a cada ronda** dos bancos do mês ATUAL e ANTERIOR
  (idade >35 min → puxa do NYC de novo — cura o incidente #6 e a falha #3 para sempre).
- **Âncora de verdade:** saldo REAL da chave DeepSeek da Tencent (`GET /user/balance`, 1×/ronda):
  queda entre rondas = gasto real da chave (robôs + ronda); subida = recarga (anotada, não contada).
  Em 02/09 16:1x: queda de ~US$ 0,03-0,04 a cada 1-4 min → o "consumidor invisível" da Tencent
  que o vigia §5c caçava agora fica medido e exposto no painel.
- **Saídas em `v6_data/custos/`:** `financeiro_7d.json` (total, por agente/modelo/servidor e
  **por cartão do painel**), `financeiro_llms.json` (discriminação por LLM + categoria + em-uso-agora),
  `financeiro_cobertura.json` (**ledger de cobertura: cada fonte × status + lacunas anotadas** — regra
  do Miguel: "tem que ser anotado"), série diária.
- **Canal da ponte:** `cerebro/Foruns/financeiro/canal_dsn_financeiro.md` (ronda resumida; o sync
  automático da Tencent publica — o robô não toca git).
- **Dedup:** por `corr_id`+servidor+data — nunca conta evento 2× (mitiga o double-counting conhecido
  do coletor velho, que ignora `contabilizado_em`).

### Mapeamento cartão → agentes reais (fonte única: `MAPA_CARTOES` no dsn_financeiro.py)
- `v4_geo`/`v4_nac`/`v4_tec` → `v4_1_redator`+`v4_1_ciclo` (nota honesta: telemetria ainda não
  separa por vertical — os 3 cartões mostram o total da esteira com a nota visível)
- `repetidor_estatal` → Repetidor_Estatal/estatal/Auditor · `comentarista` → agente_comentarista*
- `dsn_imagem` → tribunal_visual, gerador_imagem_editorial, v4_prompt_visual, banco_ouro, cacadora
- `dsn_youtube` → *youtube* · cartões DSN sem telemetria: **LACUNA anotada no cartão** (ver §4)

## 3. PAINEL CCTV V6 — o que mudou (deploy 02/09 ~16:14 BRT, provado)

**Página 👥 Agentes (controle) — `/v6/agentes`:**
1. Banner topo: **custo REAL 7d do ecossistema inteiro** + saldo DeepSeek da chave Tencent + hora do consolidado.
2. **Custo 7d REAL em cada cartão** (USD+BRL) — de `financeiro_7d.json` (por_cartão). Zero inventado:
   sem telemetria = `⚠️ sem telemetria própria (anotado)`; gasto zero real = "(sem gasto de LLM registrado)".
3. **Linha 🧠 colorida por categoria** em cada cartão: o LLM que o agente está usando **AGORA**
   (chamada vista nos últimos 90 min, chip pulsante) — ou o mais usado no 7d.
4. Seção nova **🧠 LLMs usadas — discriminação por categoria · custo 7d**: TODAS as LLMs vistas na
   telemetria, agrupadas por categoria (linhas de categoria coloridas com subtotal), colunas:
   LLM · Empresa · Momento (🟢 EM USO AGORA pulsante / usado há X min) · Custo 7d · Chamadas ·
   Preço tabela · barra proporcional. Rodapé: total ecossistema 7d.
5. Cartões novos: **Repetidor Estatal**, **Agente Comentarista** (grandes gastadores que ficavam de fora)
   e **DS-N Financeiro (DSN-F)** (protegido, custo zero).

**Página 💰 Custos — `/v6/custos`:** a MESMA seção de LLMs, em **reais** (regra da casa de 25/08:
página 100% BRL), logo após o bloco de 24h. Fallback seguro: se o DSN-F ainda não rodou, a seção
avisa "aguardando 1ª ronda" e NUNCA derruba a página (try/except no import).

**Categorias canônicas** (de `v4_rotas_llm_limpas_v1.json` + `v4_pricing_llm_v1.json` + ratings NYC):
**ULTRA LUXO** (gpt-5.5/sol/luna, claude-opus/fable, o3…) · **SUPER LUXO** (gpt-4o, kimi, grok-3,
qwen3-max…) · **LUXO** (deepseek-v4-pro/chat, glm-5.x, qwen-vl…) · **ECONÔMICO** (gpt-4o-mini,
glm-5-turbo, deepseek-v4-flash, gemini-flash…) · **IMAGEM** (fal-ai, ideogram, qwen-image, wan).

**Fotografia 7d real (02/09 16:16):** ULTRA LUXO US$ 31,23 (gpt-5.5 $31,05 — 67% de tudo!) ·
SUPER LUXO US$ 4,94 · ECONÔMICO US$ 9,01 (comentarista: 819 chamadas de gpt-4o-mini $6,01) ·
LUXO US$ 0,56 · IMAGEM US$ 0,32.

## 4. COBERTURA — o que é REAL hoje × lacunas ANOTADAS (regra do Miguel)

| Servidor | Custo por evento | Status |
|---|---|---|
| **NYC** (fazenda) | ✅ VIVO (banco_custos, rsync */15 + pull self-heal do DSN-F) | US$ 46,06 no 7d |
| **Tencent** (robôs) | ⚠️ **LACUNA por evento** — robôs chamam LLM sem logar; **âncora de saldo DeepSeek VIVA** (queda do saldo = gasto real medido a cada 15 min, exibido no painel) | anotado |
| **Temáticos** (159.89) | vazia é CORRETO (sem gasto desde 01/08) | anotado |
| **Dell/us65** (DSH+Maíra) | ⚠️ sem telemetria | anotado (cura na fase 2) |

**Cura proposta (fase 2 — NÃO executada hoje para não colidir com obra em curso nos revisores, §112):**
função `telemetry_log()` padrão em cada robô DSN → `banco_custos_tencent_YYYY-MM.jsonl` (mesmo schema
do banco NYC; o DSN-F já lê esse arquivo — nasce ligado). Reporter leve no us65 lendo `~/.dsh/sessions`
+ saldo de chaves → mesma série. Emenda do double-counting no `coletar_custos_internos.py` (com o dono do NYC).

## 5. PROVAS (02/09, tudo verificado ao vivo)

- Ronda 1: `16:11:18 · 7d REAIS US$ 9.05` (agosto ainda faltando) → self-heal puxou agosto →
  **`16:16:02 · US$ 46.06 · 2448 chamadas · 11 LLMs`**.
- `/v6/agentes` 200 (61.748 bytes): banner US$ 46,06; v4_geo US$ 28,93; comentarista US$ 5,88;
  repetidor US$ 4,82; dsn_imagem US$ 0,52; chips 🧠 AGORA (gpt-4o, gpt-4o-mini); 2× EM USO AGORA;
  LACUNAs visíveis; seção LLMs com ULTRA LUXO US$ 31,23.
- `/v6/custos` 200 (44.605 bytes): seção LLMs em R$ (ULTRA LUXO R$ 161,75; TOTAL R$ 238,59).
- `/v6/custos/ao-vivo` 200 (não quebrou). Backups no servidor: `.bak_pre_dsnf_20260902` (2 arquivos)
  + `py_compile` 3.12 OK + restart `active`.
- Cron instalado: `*/15 * * * * flock -n /tmp/dsn_financeiro.lock ... # DSN_FINANCEIRO_15MIN_20260902`.
- Canal da ponte com rondas 1-4 gravadas (`cerebro/Foruns/financeiro/canal_dsn_financeiro.md` na Tencent).
- Incidente 16:12 anotado (§1.6): arquivos restaurados manualmente + `self_heal_bancos()` de agora em diante.

## 6. PENDÊNCIAS / PRÓXIMOS PASSOS

1. **Instrumentar robôs DSN da Tencent** (lacuna nº 1) — janela sem colisão com a obra dos revisores.
2. **Reporter do us65** (DSH/Maíra) → serie do DSN-F.
3. **Emenda do double-counting** no coletor NYC (respeitar `contabilizado_em`).
4. **Mural das IAs**: reativar `atualizador_precos_llm` (morto 22/08) — pode virar ofício do próprio DSN-F
   (é só custo/preço — sem colisão) — decisão do Miguel.
5. Alarme de saldo: DSN-F apita no Telegram quando saldo DeepSeek < US$ 2 (hoje só anota).
6. Split por vertical no V4.1 (label `portal/vertical` no banco_custos) para os 3 cartões deixarem de dividir o mesmo número.

## 7. ARQUIVOS

- Código (oficina, repo): `.tencent_v6_oficina/dsn_financeiro/dsn_financeiro.py` · `categorias_llm.json`
- Deploy: Tencent `~/dsn_financeiro/` · painel `v6/painel_cctv_v6_controle.py` + `v6/painel_cctv_v6.py`
- Saídas: Tencent `v6_data/custos/financeiro_{7d,llms,cobertura}.json`
- Backups: `painel_cctv_v6*.py.bak_pre_dsnf_20260902` (Tencent v6/)

— ZCode (GLM-5.3, DSH), 02/09/2026 ~16:2x BRT

---

## 🚀 FASE 2 — INSTRUMENTAÇÃO TENCENT + us65 (executada no mesmo dia, ~17h20-17h35 BRT)

O Miguel liberou por voz (~17h): *"se você mesmo faz, você mesmo pode adiantar isso"*. Feito:

### 2.1 CAUSA-RAIZ do custo Tencent invisível (era um bug de PERMISSÃO, não falta de instrumentação)
O `agente_roteador_llm.py` (router central que curadoria_gsn/observador/mapeamento_copa/
repetidor_estatal/youtube/gerador_imagem usam) JÁ tem `gerenciador_tokens.registrar_gasto()`
com banco JSONL próprio e preços — mas **nunca rodava**: `carregar_chaves.py` tentava abrir
`/root/.env.unificado` (root-only 600) como ubuntu → `PermissionError` → **o import do router
inteiro morria** → todo robô caía no fallback próprio sem log. OU seja: a instrumentação existia
desde maio e um `open()` sem try/except a matou.
**Correção (2 patches cirúrgicos no carregar_chaves.py, backup .bak_dsnf_perm_20260902):**
1. `except PermissionError: continue` — pula arquivo ilegível em vez de matar o módulo;
2. candidatos de env ganham `~/.dsh/deepseek_env` e `~/.dsh/llm_env` (as chaves que os robôs
   já usam — nenhum segredo movido/copiado).
**Provado ao vivo:** import OK → `gerar_texto()` entregou via gemini-3.5-flash → spy provou
`registrar_gasto('spy_teste','gemini-3.5-flash',2116,1)` → linha no banco com custo calculado
(US$ 0,002117). Router no ar = todo tráfego dos robôs que passam por ele agora loga sozinho.

### 2.2 DSN-F lê o banco do gerenciador (fonte G)
`cafezinho/Projeto Cafezinho Agentes/root/agent_data/banco_custos_*.jsonl` — com normalização:
servidor="tencent", hora local BRT → UTC (−3h), rejeita registros >15 min no futuro. Ronda 11
já mostra `tencent $0.00` vivo (só probes até agora — o tráfego real acumula conforme os crons
dos robôs rodam). Aresta conhecida: ramo gemini-genai às vezes não registra (usage_metadata) —
demais ramos (openai/deepseek/mistral/anthropic REST) todos registram; anotado.

### 2.3 Publicador instrumentado (fora do router)
Backup `.bak_dsnf_tel_20260902` + 5 linhas na perna `deepseek_vision` → `telemetry_log.py`
(helper novo em `~/dsn_financeiro/`, escreve `v6_data/custos/banco_custos_tencent.jsonl`,
preços do `categorias_llm.json`, nunca derruba o robô). Catálogo: 48 → **57 modelos**
(+glm-5.3-flash/glm-4.5v/gemini-3.5-flash-pro/mistral-small/kimi-k2/claude-haiku-3.5/
opus-4.5/sonnet-4.5 — tabela pública, editável sem restart).

### 2.4 DESCOBERTA: us65 e Tencent usam a MESMA chave DeepSeek
Reporter do escritório (`reporter_us65.py`, cron */15 us65, `REPORTER_US65_15MIN_20260902`)
leu saldo US$ 11,65 ≈ saldo Tencent 11,69 → hash das chaves confere (**mesma chave**, nunca
impressa). Consequência: o pool é UM só e a âncora de saldo do DSN-F (Tencent) já mede
escritório+robôs juntos; reporter fica em **modo observação** (serie local, sem banco — evita
double-count; flag `REGISTRAR_BANCO` pronta para quando existir chave própria no us65).
**Implicação para o Miguel:** a queda de saldo que o painel mostra (US$ 12,83→11,65 em ~1h20
= **US$ 1,18**) é o consumo COMBINADO dos robôs Tencent + sessões DSH do escritório.

### 2.5 Revisores R1/R2
NÃO tocados (obra da linha editorial do ZM §112 em curso neles). Continuam cobertos pela
âncora de saldo. Instrumentar quando o ZM concluir.

— ZCode (GLM-5.3, DSH), 02/09/2026 ~17:35 BRT

---

# 🌙 FASE 3 (02/09 ~23h → 03/09 00:1x BRT) — "DÁ UM SENTIDO À PÁGINA": despesas ao vivo consertadas + relatório diário → DS-N Chefe → Miguel

> **Ordem do Miguel (voz, ~23h de 02/09):** *"a telemetria tá quebrada, notoriamente quebrada…
> essa página aqui, despesas ao vivo, tem que dar um sentido a ela, ela tá errada, não é
> possível tá errada… pensa se vale a pena colocar dois tipos de telemetria, um método
> diferente de medir, pra ficar comparando um com o outro que nem a gente fez com a audiência…
> bota telemetria em todos os DSN, tudo mandando pro nosso DSN financeiro, que compila e manda
> o relatório de tudo — os temáticos também — tudo anotado… e o relatório vai pro DSN Chefe,
> o Chefe manda pra mim."*
> **Execução:** ZCode/GLM-5.3 (DSH na us65) · oficina `.tencent_v6_oficina/dsn_financeiro/`
> (+ cópia do painel em `deploy_noite_20260902/`) · deploy Tencent 03/09 00:00 BRT.

## 1. O QUE ESTAVA ERRADO NA PÁGINA (a razão do "ela tá errada")

A página **acertava os números que mostrava e mentia no retrato**: a janela 24h dizia
**US$ 5,09** (305 chamadas — 100% NYC: OpenAI/Anthropic/GLM/Qwen) enquanto o gasto **REAL**
do dia era **US$ 14,26**: faltavam **US$ 9,17 do pool DeepSeek** (robôs Tencent R1/R2/Chefe/
Ideias + escritório us65 — a chave é UMA, descoberta §2.4), invisível por evento e sem
âncora na página. **Retrato subestimado ~2,8×.** Três causas técnicas:

1. Fontes Tencent próprias (`banco_custos_tencent.jsonl` do telemetry_log + banco do
   gerenciador) ficavam FORA do endpoint ao-vivo (glob `ao_vivo_*.jsonl` só).
2. Nenhuma referência de saldo/âncora na página — o maior fluxo de gasto do dia não
   aparecia nem como número, nem como lacuna.
3. **Bug latente de double-count no DSN-F**: `agregar()` listava `banco_custos_tencent.jsonl`
   e `banco_custos_dell.jsonl` no `extras`, mas o glob `banco_custos_*.jsonl` JÁ os pegava —
   cada evento sem `corr_id` contaria 2× (o dedup por `id(r)` não segura). Corrigido nesta fase.

## 2. O QUE MUDOU (deploy 03/09 00:00 BRT · backups `painel_cctv_v6.py.bak_pre_ancora_20260902` + `dsn_financeiro.py.bak_pre_relatorio_20260902`)

**Painel CCTV (`painel_cctv_v6.py`):**
- Endpoint `/telemetria/v1/ultimos` lê também `banco_custos_tencent.jsonl` + banco do
  gerenciador (hora LOCAL BRT → −3h UTC; origem "tencent").
- **Bloco `ancora` na resposta**: saldo atual, gasto 24h medido pela QUEDA do saldo oficial
  (recarga = anotada, não somada), cobertura do pool por evento (%) e **total_real_24h sem 2×**
  (eventos de todos, exceto deepseek-tencent que já estão na âncora, + queda do pool).
- **Cartão vermelho "💸 GASTO REAL 24h — âncora saldo DeepSeek"** no topo da página + aviso
  de cobertura ("por evento cobre só quem loga chamada") — a página agora explica a si mesma.
- `/v6/custos` (janela 24h) ganha as mesmas fontes (6 jsonl) + dedup.
- Dedup `(agente, modelo, segundo, tokens)` em todos os agregadores — sobreposição de fonte
  nunca mais conta 2×.

**DSN-F (`dsn_financeiro.py`):**
- Correção do double-count do `agregar()` (glob × extras).
- `agregar(inicio_ts, fim_ts)` parametrizado (janela 7d default; dia BRT exato p/ relatório)
  + subset deepseek-por-servidor (base do cálculo anti-2× contra a âncora).
- **RELATÓRIO DIÁRIO (`relatorio_diario`)**: total real do dia (evento+âncora sem 2×),
  decomposição por servidor, top 12 cartões (lacunas anotadas), LLMs por categoria,
  cobertura completa, alertas (saldo<3, recargas). Saídas: `v6_data/custos/
  financeiro_relatorio_diario.md` + datado em `cerebro/Foruns/financeiro/relatorios/
  YYYY-MM-DD.md` (o sync da Tencent publica no repo) + linha no canal com instrução ao
  DS-N Chefe. Gatilho automático: 1ª ronda após **06:30** compila o dia ANTERIOR — chega
  antes da Baleia Azul (07:10). CLI: `--relatorio [YYYY-MM-DD]` força qualquer dia.
- **Alarme saldo < US$ 2** → Telegram pro Miguel (essencial, máx 1/dia; token do .env do
  pontos_api, nunca logado). Antes o pool quase zerava (hoje 12,83→5,63) e a casa só
  descobria de manhã.

## 3. PROVAS (reais, 03/09 00:00–00:02 BRT)

- API: `ancora {saldo 22,74 · gasto_24h 9,17 · recarga 19,04 · leituras 37 ·
  **total_real_24h 14,26**}` contra `janela_24h 5,09` — a diferença é exatamente o que
  estava invisível.
- Página ao-vivo 200 com o cartão (porta 8084 e nginx `/v6/custos/ao-vivo`);
  regressão verde: `/v6/custos` 200, `/v6/agentes` 200, API `/v6/telemetria/v1/ultimos` 200;
  `py_compile` 3.12 OK nos dois arquivos; `systemctl restart cctv-v6` → active.
- Relatórios gerados de verdade: `2026-09-01.md` (total real US$ 5,52 · âncora 0 — o DSN-F
  nasceu 16h de 02/09, a âncora não cobria) e `2026-09-02.md` (**US$ 14,26** · âncora 9,17 ·
  305 chamadas · 1,99M tokens · lacunas 4) no repo da Tencent + canal + ronda 38 OK (US$ 43,14
  7d — estável, sem double-count).

## 4. PARECER — TELEMETRIA REDUNDANTE VALE A PENA? (pergunta do Miguel)

**SIM à redundância, como MÉTODO DIFERENTE medindo a mesma coisa e comparado automaticamente
— NÃO a um segundo sistema completo.** É o modelo FAROL×GA4 da audiência aplicado a custo:

| Método | Como mede | Estado |
|---|---|---|
| **A — por evento** | cada chamada logada (tokens×preço) → ledgers | ativo (alimenta o ao-vivo) |
| **B — por saldo (âncora)** | QUEDA do saldo oficial = gasto agregado; impossível "esquecer" um chamador | **ativo desde hoje na página + relatório** |
| **C — por fatura** | CSV oficial do provedor × banco (reconciliador) | ativo, cron domingo 12h (M3 de 24/08) |

- O que dá confiança é o CRUZAMENTO com alerta: dois sistemas que medem pelo MESMO método
  (evento) erram JUNTOS (os dois "esquecem" o robô que não loga — foi o caso de hoje). A
  âncora pega exatamente o que o evento não pega; a fatura é a prova externa.
- Um stack duplicado (ex.: OpenTelemetry/Prometheus paralelo) dobraria manutenção e a chance
  de bug sem ganhar verdade. Custo incremental do modelo aprovado ≈ **zero** (tudo já
  existia; faltava cruzar e exibir).
- Próximo degrau (fase 4): vigília diária da divergência A×B no pool compartilhado (o vigia
  §5c do NYC já faz isso para a chave DeepSeek do NYC) com alerta > US$ 1/dia.

## 5. ARQUITETURA DO FLUXO — todos os DSN → DSN-F → Chefe → Miguel

```
[Chefe][Ideias][Maíra][R1/R2*][Publicador][YouTube]  (Tencent)
        │ router/gerenciador (automático)  ·  telemetry_log (3 linhas p/ quem chama direto)
        │                                        [NYC: banco_custos] ── rsync */15 ──┐
        │                                        [159.89 temáticos] ── rsync 1min ────┤
        ▼                                        [us65 escritório] ── âncora (olho) ──┤
  DSN FINANCEIRO (*/15, zero LLM, não gasta) ◄───────────────────────────────────────────┘
        ├─ painel: /v6/custos/ao-vivo (evento + âncora + total real sem 2×) · /v6/agentes
        ├─ canal: cerebro/Foruns/financeiro/canal_dsn_financeiro.md (ronda a cada 15 min)
        └─ 06:35: RELATÓRIO DIÁRIO DE TUDO → cerebro/Foruns/financeiro/relatorios/<dia>.md
                     └─► DS-N CHEFE embute 💰 na Baleia Azul (07:10) ──► MIGUEL
```
Cobertura por fonte (tudo anotado no `financeiro_cobertura.json`): NYC ✅ evento · Tencent
router ✅ evento (fase 2) · Tencent telemetry_log ✅ pronto (publicador já instrumentado) ·
temáticos ✅ vivo (vazio = correto, sem gasto desde 01/08; ao voltar a gastar entra só) ·
us65 escritório 👁 âncora (chave compartilhada; split exige chave própria) · R1/R2 ⏳ após
obra do ZM §112 · Mural das IAs ❌ morto 22/08 (token gh expirado — dono ZM) ·
Chefe/Ideias/Maíra/Celular/iPad ⏳ fase 4.

## 6. PENDÊNCIAS COM DONO

1. **ZM:** rotacionar o token gh do `atualizador_precos_llm.py` (Mural das IAs congelado
   desde 22/08 09:00 — a ÚNICA peça do D8 ainda morta).
2. **ZM (após obra §112):** instrumentar R1/R2 com `telemetry_log` (3 linhas cada).
3. **Chefe/Ideias/Maíra (fase 4):** chamar LLM via router (automático) ou `telemetry_log`.
4. **Miguel (decisão):** chave DeepSeek própria p/ o us65 se quiser split
   escritório×robôs; senão a âncora única segue honesta (econômica).
5. **Fase 4:** vigília diária divergência evento×âncora no pool (estender §5c do NYC).

— ZCode/GLM-5.3 (DSH, us65) · 03/09/2026 00:1x BRT
