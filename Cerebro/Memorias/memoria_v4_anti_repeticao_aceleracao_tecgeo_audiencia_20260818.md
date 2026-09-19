# Memória — Desenho: anti-repetição V4 + aceleração Tec/Geo + audiência (18/08)

**Sessão:** ZCode/DeepSeek. **Horário:** 18/08/2026 ~17:20→17:50 BRT.
**Ordem Miguel (voz):** análise de audiência + cerco anti-repetição NA COLETA + acelerar drasticamente Tec/Geo e desacelerar Nacional + por que o agente YouTube parou. **DESENHO — nada aplicado além dos gates da manhã (fórum `forum_v4_gate_tema_geopolitica_tecnologia_20260818.md`).**

## Dados coletados (provas)

- **GA4 (query direta via `/root/keys/ga4.json` no Tencent, sudo):** sessões 16/08 7.933 (google 2.323, direto 5.174) · 17/08 6.871 (1.831/4.521) · 18/08 até 17:20 2.749 (437/2.132). Views 3.130. Queda real desde domingo, google −68% — fim do impulso Discover/News de ~14/08; sem problema técnico. Observar 3-5 dias.
- **Repetições confirmadas (WP):** Vila Euclides 266116 (16/08) × 266323 (18/08) — mesmo evento, 2 dias; pesquisa 47×44 266262 (18/08) repete 266274 Nexus (17/08). Dedup atual = `duplicate_recent_topic()` por TÍTULO em 24h (Bug #23) — repetição semântica passa.
- **YouTube:** pipeline rodou 11:00 e 17:00 (`youtube_v2_pipeline.log`) com "Coletor warning (continuando)" e ZERO drafts novos; banco: 1 `novo`, 30 `falha_transcricao`, 2 `pronto` (rotas EN→gsn_fila). Coletor é o suspeito (rate-limit/filtro de canais) — investigar (YT-PATRULHA).
- **Crontab NYC:** geo `0,30` · ciencia `10,40` · nacional `20,50`; worker limita 1 draft/h por vertical (linha 2 do `v4_vertical_draft_worker.py`).

## Desenho (detalhes no fórum `forum_v4_anti_repeticao_aceleracao_tecgeo_audiencia_20260818.md`)

1. **RAR — Registro Anti-Repetição** (`agent_data/anti_repeticao/registro.sqlite`): tabela `cobertos(topic_key, entidades, tema, titulo, post_id, vertical, data_cobertura, janela_dias)`; topic_key = entidades|tema. Alimentação: worker pós-draft + sync diário do WP (14 dias, LLM leve em batch) + YouTube.
2. **Cerco em 4 estágios:** coleta (Jaccard títulos + sobreposição de entidades, zero LLM) → intake (mesma checagem + item_key) → worker (consulta RAR; SKIP se coberto na janela; prompt anti-ângulo-repetido se só entidades batem) → Loop (recibo RAR na revisão). Janelas: política 3d · geo/tec 5d · economia 4d · resto 7d. Fato novo concreto = exceção, com ângulo no título.
3. **Variedade:** rodízio de fontes (worker prefere fonte fora das últimas 3; coletor limita fonte a 50% do estoque) + penalização de entidades saturadas (top-5 dos últimos 3 dias) + contador semanal de bloqueios por estágio.
4. **Rebalanceamento:** geo 4×/h (0,15,30,45) máx 2 drafts/h; ciencia 4×/h (10,25,40,55) máx 2/h; nacional 1×/2h máx 1. → ~48+48+12 drafts/dia; Loop publica até 60 (Sprint V4). Worker: `max_drafts_per_hour` por vertical no CONFIG (kill switch por vertical). Custo extra estimado US$ 8-12/dia.
5. **Diretrizes imediatas anti-repetição** (valem hoje, sem código): pesquisa só com dado novo; evento ≤3/5 dias só com fato novo no título; entidade repetida ok se tema novo explícito.

## Estado / o que precisa do Miguel

Aprovar o desenho (ou ajustar janelas/cadências) e confirmar a aceleração Tec/Geo (2/h cada). Nada aplicado sem ordem.
