# 🏗️ V4 — Arquitetura anti-repetição + aceleração Tec/Geo + análise de audiência (18/08)

**Ordem do Miguel (18/08 ~17:20, voz):** (1) entender por que a audiência está baixa hoje; (2) diretrizes anti-repetição — "cerco já na coleta", arquivo anti-repetição, coisas variáveis; (3) acelerar drasticamente a produção de Tecnologia e Geopolítica, desacelerar o Nacional (folga pro publicador humano); (4) por que o agente YouTube está parado. **Este fórum é o DESENHO — nada foi aplicado em produção além do que já estava (gates de tema desta manhã).**

---

## 1. 📉 Audiência hoje — o que os dados dizem (GA4 real, consultado às 17:20)

| Dia | Sessões | Google orgânico | Direto | Views (painel) |
|---|---|---|---|---|
| 16/08 (sáb) | 7.933 | 2.323 | 5.174 | 9.773 |
| 17/08 (dom) | 6.871 | 1.831 | 4.521 | 8.225 |
| 18/08 (seg, até 17:20) | 2.749 | 437 | 2.132 | 3.130 |

**Leitura honesta:** a queda é REAL e começou domingo, não hoje. Projeção de hoje: ~3.700 sessões (−46% vs domingo; −53% vs sábado), com o Google orgânico caindo mais forte (−68% vs domingo). Não há indício de problema técnico (site e painel saudáveis). Hipóteses, em ordem de probabilidade: (a) fim do impulso do Discover/Google News que vinha desde ~14/08 (o grosso do tráfego google veio de uma onda de destaque); (b) ciclo de notícias eleitoral esfriando no fim de semana; (c) o aumento de volume de posts ainda NÃO gerou audiência — post novo leva 1-3 dias para indexar e distribuir; o efeito do volume só aparece no meio da semana. **Recomendação: observar 3-5 dias no painel antes de qualquer decisão de conteúdo; nenhum alarme.** O ponto do Miguel está certo: "tem que esperar alguns dias para ver se é tendência".

---

## 2. 🔁 Anti-repetição — o problema e o desenho

**Casos confirmados (hoje):**
- 266116 (16/08) "Na Vila Euclides, Lula liga a campanha ao trabalho e à soberania" × 266323 (18/08) "Lula abre campanha na Vila Euclides com foco em mobilização e direitos" — mesmo evento, 2 dias depois.
- 266262 (18/08) "Lula e Flávio mantêm empate técnico no segundo turno com 47% e 44%" — pesquisa repetida de ontem/anteontem (266274 Nexus 17/08 + cobertura de pesquisa 16/08).

**Por que o dedup atual falha:** o worker tem `duplicate_recent_topic()` (Bug #23, 24/07) — mas é comparação de TÍTULO em janela de 24h. Repetição semântica (mesmo evento, título novo, 2 dias depois) passa.

### Arquitetura proposta: RAR — Registro Anti-Repetição (na coleta e no pipeline)

**Componente novo (NYC):** `agent_data/anti_repeticao/registro.sqlite` — 1 tabela:

```
cobertos(topic_key PK, entidades, tema, titulo, post_id, vertical, data_cobertura, janela_dias)
```

- **topic_key** = `entidades_normalizadas|tema` (ex.: `lula;vila-euclides|abertura-campanha`). Entidades = pessoas/órgãos/lugares; tema = slug do assunto (LLM na entrada, heurística nas comparações).
- **Alimentado por 3 fontes:** (1) worker, ao CONFIRMAR draft, grava a pauta coberta; (2) sync diário (00:10) do WP: últimos 14 dias publicados → extração de entidades/tema via LLM em batch barato (modelo leve da cascata, 1×/dia); (3) agente YouTube ao criar draft.
- **Janelas por vertical:** política 3 dias · geopolítica 5 · tecnologia 5 · economia 4 · demais 7. Exceção: **fato novo concreto** (desdobramento novo do mesmo evento) passa — a regra exige que o ângulo novo esteja explícito no título.

### O cerco em 4 estágios (defesa em profundidade)

| Estágio | Onde | Custo | Ação |
|---|---|---|---|
| 1. **Coleta** (o cerco pedido) | `coletor.py` | ZERO LLM | Item coletado passa por: (a) título Jaccard/shingle vs `cobertos.titulo`; (b) sobreposição de entidades (heurística, nomes próprios) vs `cobertos.entidades`; (c) URL já coletada. Bateu → descarta ANTES de entrar no estoque, com log `coleta_repetida`. |
| 2. **Intake** | `v4_vertical_intake.py` | ZERO LLM | Mesma checagem (RAR em disco já atualizado) + item_key (já existe). Rejeição vira linha em `rejections` (motivo `tema_ja_coberto`). |
| 3. **Worker (pré-redação)** | `v4_vertical_draft_worker.py` | 1 chamada LLM por candidata borderline | Estende o `duplicate_recent_topic` existente: consulta o RAR pela pauta; se tema+entidade cobertos dentro da janela → SKIP (grava `skip_repeticao`). Se só entidades batem (tema novo) → passa, mas o prompt do redator recebe "não repetir o ângulo de: [últimos títulos cobertos]" (novidade obrigatória no ângulo). |
| 4. **Publicação (Loop Miguel)** | Claude, no /loop | humano | O bloco de revisão de cada post ganha o "recibo RAR": lista dos posts recentes do mesmo tema (o Claude decide publicar/rejeitar). |

### Variedade ("coisas variáveis")

- **Rodízio de fontes:** o worker prefere candidata cuja fonte NÃO esteja entre as últimas 3 usadas no vertical (score bonus), e o coletor nunca deixa uma fonte dominar >50% do estoque.
- **Diversidade de entidades:** o coletor marca as 5 entidades mais vistas nos últimos 3 dias no RAR e derruba o score de pautas que só repetem essas entidades sem tema novo.
- **Métrica:** fórum de monitoramento ganha um contador semanal "repetições bloqueadas por estágio" — se o estágio 1 zerar e o 4 estiver alto, o cerco da coleta está frouxo.

### Diretrizes imediatas (valem HOJE, sem depender do código)

1. **Pesquisa eleitoral: só publica se for dado novo** (novo instituto, nova data de campo, ou virada de tendência). "Mesma pesquisa, outro ângulo" = proibido.
2. **Evento coberto ≤3 dias (política) / ≤5 dias (geo/tec) só volta com fato novo concreto**, e o título DEVE carregar o fato novo.
3. Se a pauta repetir entidade mas tiver tema novo (ex.: Lula mas sobre energia), ok — destacar o tema novo no título.
4. Ao revisar, conferir o painel: aba Publicações mostra os títulos recentes lado a lado.

---

## 3. 🚀 Rebalanceamento de produção (desenho para aplicar quando o Miguel autorizar)

**Estado atual (crontab NYC):** geopolitica `0,30` · ciencia `10,40` (comentário) · nacional `20,50` — todos 2×/hora, mas o worker limita **1 draft/hora por vertical** → teto real de 24 drafts/dia por vertical, ~72/dia no total.

**Desenho proposto:**

| Vertical | Coleta+intake | Worker (novo limite por vertical) | Drafts/dia |
|---|---|---|---|
| Geopolítica | `0,15,30,45` (4×/h) | máx **2/h** | ~48 |
| Tecnologia/Ciência | `10,25,40,55` (4×/h) | máx **2/h** | ~48 |
| Nacional | `20` e `50` → `0 */2` (1×/2h) | máx **1/2h** | ~12 |

- Tec+Geo somam ~96 drafts/dia disponíveis; o Loop Miguel (publicador, teto 60/dia autorizado no Sprint V4) escolhe os melhores — oferta farta, sem repetição (RAR) e sem sobrecarregar o Nacional.
- Worker: trocar o limite global de 1/hora por `max_drafts_per_hour` por vertical no CONFIG (geo 2, ciencia 2, nacional 1). Mesmo padrão dos cron jobs atuais (flock por vertical), sem risco de corrida.
- Custo LLM estimado: +~US$ 8-12/dia na cascata (a calibragem exata fica na aplicação, com kill switch por vertical no CONFIG).

---

## 4. 📺 Agente YouTube — status

**Não está morto, mas está improdutivo hoje:** o pipeline rodou às 11:00 e às 17:00 (log `youtube_v2_pipeline.log`), porém com "Coletor warning (continuando)" e **zero drafts novos hoje**. Estado do banco: só 1 vídeo `novo`, 30 em `falha_transcricao`, 2 `pronto` aguardando (rotas recentes foram para `gsn_fila` — EN). Causa provável do "nada hoje": coletor achando pouco/nada (rate-limit de YouTube ou filtro de canais) + os vídeos prontos serem EN (vão pro GSN, não pro Cafezinho). **Ação proposta:** investigar o "Coletor warning" na próxima janela (item YT-PATRULHA) — provavelmente chave/rotação de API ou o filtro de canais estreito demais.

---

## 5. Estado e próximos passos

- **Aplicado hoje (antes desta conversa):** gates de tema Tec×Geo + 266468 recategorizado (`forum_v4_gate_tema_geopolitica_tecnologia_20260818.md`).
- **Este fórum é desenho — aguarda avaliação/ordem do Miguel** para: (a) implementar RAR (coletor → intake → worker → recibo pro Loop); (b) rebalancear crons/limites; (c) investigar coletor do YouTube.
- **O que preciso do Miguel:** aprovar o desenho (ou ajustar janelas/cadências) + confirmar se acelero Tec/Geo como proposto (2/h cada) ou com outro número.
