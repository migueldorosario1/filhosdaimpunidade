# 📡 CEREBRO_NODE — TELEMETRIA GERAL DO SISTEMA

> [!CAUTION]
> **OVERRIDE DE INFRAESTRUTURA 11/08/2026:** a seção “4 máquinas” registra a topologia de 22/07 e não é mais a lista completa dos ambientes vivos. Consultar `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md` para hosts e papéis atuais; este nodo continua canônico para o pipeline de métricas e custos.

> Mapa canônico da telemetria de IA (tokens, custos, modelos, agentes, saúde) de **todo** o ecossistema Cafezinho.
> Criado: **2026-07-22** por ZCode (Kimi), a pedido do Miguel: "mapeamento geral, investigação geral e profunda, de toda a inteligência que a gente usa, todos os gastos, todos os tokens, nome da empresa, modelo — acompanhando tudo online".
> Painel público: **`http://43.156.151.165/v6/custos`** (+ `/v6/tematicos`, `/v6/agentes`).

---

## 🗺️ 1. As 4 máquinas e seus papéis (verificado 2026-07-22)

| Máquina | Papel hoje | Crons-chave vivos |
|---|---|---|
| **NYC DigitalOcean** `198.199.121.136` (root) | 🏭 **FAZENDA DE PRODUÇÃO** — V4 verticals, comentarista, repetidor, SEO, indexer, GSN, **governança financeira** | ~35 jobs: V4 geo/tec/nacional (2h), `agente_comentarista_v4` (1min!), `agente_repetidor_estatal` (2h), `auditor_titulos_gpt` (10min), `coletar_custos_internos.py --write` + `gerar_relatorio_financeiro.py` (**hora :07**), `push_metricas_llm_completo.py` (hora), `augusto_fiscal_tokens` (8h), `validador_modelos` (3h), autocura V4 (15h), GSN coleta (3h) + hourly, SEO pruning (3:07), daemon_indexador (30min) |
| **Tencent Singapura** `43.156.151.165` (ubuntu/root) | 📺 **Painéis + ESP-DE-PRODUÇÃO (standby quente, NÃO "parada")** — nginx 80, CCTV v5 (legacy), **CCTV V6** (8084, systemd), editorial (8083), mídia ouro (8091), watchdog_v3 (dashboard/audiência), push métricas 5min. **Mirror do enxarme** — assume master via failover (manual ou automático). Chairman planeja reativar ambos espelhos em paralelo. Ver `Foruns/forum_dualidade_nyc_tencent_20260726.md` | ubuntu: push_metrics (5min), gerar_pulse (10min); root: watchdog_v3 loop; V6 sob `cctv-v6.service` |
| **Alibaba Beijing** `39.106.184.215` (root) | ⚫ **LEGACY — aposentada por Miguel em 2026-07-29** (SSH timeout; Prometheus central ficava aqui — endpoint precisa migração ou pushers devem ser desligados) | `agente_relatorio_vigias` (25min), push_metrics (5min); Kimi-Beijing DESATIVADO (2026-05-24) |
| **Local (máquina do Miguel)** | 🧠 **Cérebro + ponte de sync** — cerebro-miguel, backups, syncs | cerebro→GitHub (30min), backup Cérebro→B2/Drive/Alibaba (3:40), fóruns→Tencent V6 (30min), **custos NYC→Tencent V6 (1h :12)**, sync fóruns maestro B2 (30min), watchdog painel local |

---

## 💰 2. Onde os dados de custo NASCEM (a espinha dorsal — JÁ EXISTE)

| Camada | Arquivo/Serviço | Conteúdo |
|---|---|---|
| **Evento bruto** | NYC `/root/agent_data/banco_custos_2026-07.jsonl` (~33 MB/mês) | 1 linha por chamada LLM: agente, modelo, tarefa, tokens in/out, custo US$ |
| **Consolidado diário** | NYC `/root/agent_data/custos_consolidados/AAAA-MM-DD.json` (cron 1h :07) | totais, por_dia, **por_agente**, **por_provider**, **por_modelo**, por_tarefa, anomalias |
| **Relatório humano** | NYC `/root/agent_data/relatorios_financeiros/*.md` | resumo diário em prosa |
| **Séries temporais** | `push_metricas_llm_completo.py` → **Pushgateway Aliyun** | `cafezinho_llm_call_total`, `cafezinho_llm_cost_usd_total`, `cafezinho_llm_tokens_prompt/completion_total` com labels {agent, model, tarefa, origem} |
| **Saúde LLM** | node_exporter cada servidor → `cafezinho_api_key_test_latency_ms{key_id, provider}` | latência por chave/provedor (alimenta dashboard + V6) |
| **Audiência** | GA4 — conta `Ocafezinho` (374552425) + conta `Sites_tematicos` (**7 properties**, ver §4) | pageviews diários, top posts |

**Pipeline V6 (montado 2026-07-22):** NYC consolida (1h) → `~/bin/sync_custos_v6.sh` (cron local `12 * * * *`) → Tencent `/home/ubuntu/cafezinho/v6_data/custos/` → página `/v6/custos` lê e renderiza (24h/7d/30d, por modelo+empresa, por agente, US$+R$, gráfico de barras 30d).

> **OVERRIDE 02/09/2026 — DSN FINANCEIRO (DSN-F):** o `sync_custos_v6.sh` da máquina local MORREU
> em 31/07 (cron extinto) — os consolidados diários pararam de chegar na Tencent. O pipeline de custos
> agora tem DONO: o robô **DSN Financeiro** (Tencent `~/dsn_financeiro/dsn_financeiro.py`, cron */15
> com flock; custo zero — não usa LLM). Ele mesmo puxa por ssh: consolidados diários NYC (1×/h) e
> **self-heal a cada ronda dos `banco_custos_YYYY-MM.jsonl` do mês ATUAL e ANTERIOR** (o rsync */15
> do NYC só mandava o mês corrente — a janela 7d perdia a virada do mês; antes do DSN-F o 7d dava
> US$ 9 com o real em US$ 46). Saídas em `v6_data/custos/financeiro_{7d,llms,cobertura}.json`
> (7d por cartão do painel; discriminação por LLM × categoria ULTRA/SUPER LUXO, LUXO, ECONÔMICO,
> IMAGEM com "em uso agora"; **ledger de cobertura com lacunas anotadas**). **Âncora de verdade:**
> saldo real da chave DeepSeek da Tencent (`/user/balance` 1×/ronda) — a queda entre rondas é o gasto
> real dos robôs DSN (que não logam custo por evento — lacuna nº 1, instrumentação na fase 2).
> Painel: custo 7d REAL por cartão em `/v6/agentes` (USD+BRL) e seção LLMs por categoria em
> `/v6/agentes` (USD) e `/v6/custos` (BRL). Detalhes: `Foruns/forum_dsn_financeiro_rastreador_custos_20260902.md`.

---

## 🤖 3. Inventário de inteligência (quem gasta o quê — fotografia 22/07)

**Modelos vistos na telemetria de hoje** (fonte: consolidado 2026-07-22):

| Modelo | Empresa | Uso típico |
|---|---|---|
| deepseek-v4-flash | DeepSeek 🇨🇳 | comentarista V4 (volume) |
| deepseek-v4-pro | DeepSeek 🇨🇳 | redação/raciocínio pesado |
| deepseek-chat | DeepSeek 🇨🇳 | v4_prompt_visual |
| fal-ai | Fal.ai 🇺🇸 | geração de imagem editorial |
| ideogram | Ideogram 🇨🇦 | imagem |
| wan2.6-t2i | Alibaba 🇨🇳 | imagem (texto→imagem) |

**Mapa completo de empresas na regra do painel** (`_empresa_modelo`): DeepSeek, Anthropic, OpenAI, Google, Alibaba, Moonshot, Zhipu (GLM), Mistral, Fal.ai, Ideogram, Perplexity, Brave.

**Agentes que mais gastam hoje:** `agente_comentarista_v4` (1min cron — maior volume), `Repetidor_Estatal`, `gerador_imagem_editorial`, `v4_prompt_visual`.

**Fotografia do dia 22/07 (~13h):** US$ 1,62/dia · 357 chamadas · 840k tokens in · 169k out. Mês (30d): **US$ 572** (ver `/v6/custos`).

---

## 🌐 4. GA4 dos temáticos — CONECTADO (2026-07-22)

Conta GA4 `Sites_tematicos` — a SA `root/ga4.json` (Tencent) **já tem acesso** a tudo:

| Portal | GA4 property | Tráfego 30d (22/07) |
|---|---|---|
| O Cafezinho | 374552425 | ~54k views/7d (vivo) |
| Mundo Trilhos | 546667776 | 7 (inicial) |
| Discover Brazil | 546669474 | inicial |
| Rio Carta | 546673810 | 12 (inicial) |
| **Ceará Digital** | **546675232** | 0 (pré-lançamento) |
| AIatolah | 546675625 | 0 |
| Global South News | 546677232 | 4 (inicial) |
| Rail Post | 546679970 | inicial |

Páginas `/v6/tematicos/<slug>` mostram views 30d/7d/MM7 automaticamente; gráfico acende com 8+ dias de dados. Measurement IDs (gtag) confirmados instalados nos 6 sites no ar.

---

## 📊 5. Prometheus: serve para o que queremos?

**Veredito: SIM para infra + séries LLM, com complemento.**
- ✅ Já recebe: latência por chave LLM (probes), métricas de máquina (node_exporter ×3), métricas LLM completas (push_metricas_llm_completo)
- ✅ Aliyun Managed Prometheus = central, sem manutenção
- ⚠️ Para o **painel**, ler os **consolidados JSON** (via rsync) é mais simples e robusto que PromQL remoto autenticado — decisão adotada
- 🔜 Prometheus ideal para **alertas** (ex.: custo diário > cap) e para as futuras **barras de crédito** (gauges por provider)

---

## 🛣️ 6. Roadmap da telemetria (próximos blocos)

1. **Split por portal** — hoje o consolidado é global por agente/modelo; adicionar label `portal` no banco_custos (Cafezinho × temáticos)
2. **Barras de crédito por provider** (pedido do Miguel): sem API pública de saldo na maioria; caminho = budget mensal configurado por provider − gasto acumulado (telemetria) → barra de previsibilidade + alerta Prometheus
3. **Health check de agentes** no painel: último heartbeat por cron (ler mtime dos logs em `agent_data` e mostrar verde/amarelo/vermelho por agente)
4. **Alertas ativos**: custo diário > cap → Telegram (Augusto já tem canal)
5. **Cobertura de instrumentação**: garantir que TODOS os agentes V4 escrevem no banco_custos (auditar os ~35 crons de NYC)

---

## 🗓️ Atualização 2026-07-29 — Auditoria geral de custos (ZCode, a pedido do Miguel)

- **Auditoria completa executada:** Fórum `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md` + Memória `Memorias/memoria_auditoria_custos_telemetria_recuperacao_crons_20260729.md`.
- **Números reais julho:** total 1–29 = **US$ 443,47**; pós-cortes de 19/07 o burn rate caiu ~92% (US$ 23,65/dia → **US$ 1,95/dia**; projeção 30d ≈ US$ 59). Maior gasto do mês: `motor_coletor:curadoria` legado US$ 380 (pausado). Top modelo: gpt-4o-mini US$ 174,49.
- **Nova lacuna confirmada:** agentes LOCAIS (`agentes_tematicos/v4/orquestrador.py`, ~68 gerações + ~48 julgamentos visuais/dia) **não gravam `usage`/custo** — `nucleo_llm.py` descarta o campo. Fix proposto aguarda aprovação (fecha a pendência 5 abaixo para a perna local).
- **Kimi paygo reativada** 29/07 (crédito Miguel; teste ao vivo OK) — curadoria LLM do Cafezinho restabelecida.

## 🗓️ Atualização 2026-08-01 — Vigia de custos + fiscal corrigido + escalada de imagens (ZCode)

- **Vigia 30min ATIVO:** `~/bin/vigia_custos_baleia.sh` (cron `*/30`, tag `VIGIA_CUSTOS_BALEIA_20260730`) — cap US$ 5/dia · anomalia 1,5× média 7d · fiscal vivo · edição Baleia existe · envio do dia saiu · **saldo DeepSeek < US$ 2** (1×/dia). Alertas Telegram Augusto, anti-spam 1×/dia, log `~/log/vigia_custos.log`.
- **Fiscal NYC 7d/30d CORRIGIDO** (patch `_soma_consolidados()`; backup `augusto_fiscal_tokens.py.bak_pre_fix_7d30d_20260730`) — relatório 08h de 01/08: ontem US$ 6,40 · 7d US$ 26,58 · 30d US$ 455,50.
- **ESCALADA de imagens (28/07→01/08):** US$ 2,41 → 4,09 → **9,22** → 6,40 → 01/08 ~7–9 (cap estourado). Driver: `gerador_imagem_editorial` 48→397 imgs/dia (onda V4 Regional/heroes). Critério Codex aceito: **se 02/08 > 60 imgs ou > US$ 5 → cap reversível 60 imgs/dia**. Ritmo caiu p/ ~6/h ao fim de 01/08 (onda arrefecendo).
- **Juiz visual Kimi:** 401 por chave velha no NYC → sincronizada `sk-kimi-xQ…` (01/08 11:45); zero 401s pós-fix; fallback pago Qwen-VL extinto.
- **Curador Cafezinho:** cascata `deepseek-v4-flash → kimi-k3 paygo → heurística` (decisão Miguel).
- **⚠️ Saldo DeepSeek US$ 1,15 — recarga de Miguel não visível** (ver nodo CHAVES_E_LLMS, atualização 01/08).
- **Baleia Azul:** sem edições 28/07→01/08 (editor-chefe Claude não gerou); cartinhas ao Claude pendentes (Baleia + Cofre Único).
- **03/08 (faxina+links):** crons `--so-youtube` desativados; `biblioteca-editorial-pilot` off; **NAV do V6 ganhou link Mídia Ouro** (`/midia-ouro/` em todas as páginas, verificado); painel `/v6/` e `/v6/custos` 200. **DeepSeek: rotação por consumidor deployada (4 chaves — ver Cofre)** + vigia §5c anti-divergência ativo; mistério do consumo invisível resolvido = estúdio/navegador local (Adendos 5–6 do fórum da auditoria).

## 🔗 Documentos ligados

- **💰 CUSTOS REAIS MENSAL (destaque Chairman 29/07):** `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md` — consolidado de todos os gastos com nível de confiança por linha
- **Auditoria 29/07:** `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md` · `Memorias/memoria_auditoria_custos_telemetria_recuperacao_crons_20260729.md`
- Fórum da reforma: `projeto_cafezinho_agentes/foruns/forum_reforma_cctv_v6_20260721.md`
- Fórum da dualidade NYC↔Tencent (failover automático+manual, modelo espelhado): `Foruns/forum_dualidade_nyc_tencent_20260726.md`
- Scripts: `~/bin/sync_custos_v6.sh` (sync custos) · `~/bin/backup_cerebro_diario.sh` (backup Cérebro)
- App do painel: Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (systemd `cctv-v6.service`)

## Astra — proposta de Controle de Despesas Transparente (05/09/2026)

[Proposta print→ledger→DSN-F→/v6](Foruns/PROPOSTA_ASTRA_CONTROLE_DESPESAS_TRANSPARENTE_20260905.md) e [análise/memória](Memorias/MEMORIA_ASTRA_FASE0_20260905.md). Prioridade: integridade e reconciliação do contador existente; evidência separada de consumo/recarga/saldo/assinatura; idempotência, moeda/período/frescor e documentos privados. GET05/09 01:02:21 indicou cobertura_pool_pct13,3; descontinuidades locais Tencent levadas ao tutor DSN-Chefe sem atribuição de causa. Proposta não implementada, sem mudanças de painel/robôs. Quórum e vai humano para dinheiro preservados.

Adendo05/09 ~01:30: canal Astra registra telemetria privada em ponte_astra/state/usage.jsonl (tokens/cache/saída, duração, modelo/status, tool_events, billing_mode=chatgpt_subscription; custo=null, não inventado). Ainda sem integração ao hub. Modelo só sob mensagem recebida, voz local offline; não há chamada ociosa de modelo nem API key/fallback pago.
