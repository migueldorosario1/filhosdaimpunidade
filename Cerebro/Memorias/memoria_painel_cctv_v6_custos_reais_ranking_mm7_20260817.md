# Memória — Painel CCTV V6: custos em reais + ranking LLMs + MM7 vs semana anterior (17/08/2026)

**Sessão:** ZCode (Qwen 3.8-Max), conversa ZCodeProject, 17/08 ~00:30→01:20 BRT.
**Ordem do Miguel:** /v6/custos tudo em R$ (cotação no alto, nada em dólar, gráfico escrito
"em reais") + ranking dinâmico preços/qualidade LLMs (o do Moka Reader/Aiatolah) +
/v6/audiencia com MM7 vs MM7 da semana anterior. Pedia também para conferir se o Moka
ainda tem o ranking.

## Arquivo tocado

- **Tencent:** `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (serviço `cctv-v6`, porta 8084,
  usuário ubuntu). Backup: `painel_cctv_v6.py.bak_pre_custos_brl_ranking_20260817`.

## Mudanças no código

1. **`svg_barras_custo(serie, taxa)`** — agora converte para R$ (eixo `R$ {gv:.2f}`, tooltip
   `R$`, legenda "💵 eixo em reais (R$)").
2. **Novos helpers:** `_fmt_brl_val()` (formata valor já em R$), `_fmt_brl_peq()` (precisão
   4 casas p/ valores < R$ 0,10), `RANKING_LLM_URL` (jsDelivr), `RANKING_LLM_FALLBACK`
   (16 modelos, mesmo cânone Moka/Aiatolah), `RANKING_QUALIDADE` (S/A/B → cores) e
   `_ranking_llms(taxa)` (fetch com cache 6h via `_cache_get/_cache_set`, converte p/ R$,
   ordena por custo de resumo, fallback se vazio/erro).
3. **`pagina_custos()`** — ordem FINAL (ranking movido para o fim por ordem do Miguel,
   17/08 ~01:25): (1) banner cotação dourado NO ALTO (R$ grande + fonte + aviso "tudo em
   reais"); (2) telemetria só em R$ (hoje/7d/30d/chamadas/tokens); (3) gráfico diário em
   reais; (4) por modelo/agente; (5) saúde das LLMs; (6) por provedor — todos SÓ com
   coluna R$ (colunas US$ removidas); (7) seção do ranking POR ÚLTIMO (medalhas,
   qualidade, velocidade, entrada/saída R$/1M, "resumir 1 livro" R$, link Moka/Aiatolah,
   "↻ atualizado em"). `_fmt_usd` removida (não usada).
4. **`pagina_audiencia()`** — `mm`/`mm_prev` calculados no escopo da função; card novo
   "MM7 vs semana anterior (valor anterior)" com `_delta_pct(mm[-1], mm[-8])`; título da
   seção do gráfico atualizado.
5. **`svg_linha(serie, titulo_mm, mm7_prev=None)`** — linha tracejada `#c9a227`
   (`stroke-dasharray="7 6"`) com a MM7 defasada 7 dias + legenda
   "┅ MM7 da semana anterior (defasada 7 dias)".
6. **Home:** texto do card Custos atualizado ("Gastos em reais, cotação e ranking de
   preços das LLMs").

## Verificação do ranking Moka/Aiatolah (pedido do Miguel)

- **Moka Reader — ✅ tem e está no ar:** `https://www.mokareader.com/ajuda` (HTTP 200),
  componente `LlmPriceRanking.tsx` renderiza "Mural das IAs" + "Ranking de Preços" com
  GLM-4 Flash/DeepSeek V4 Flash. Repo local:
  `Outros/Aplicativos/Moka/Moka-Lab/apps/web` (`src/lib/llm-prices.ts` +
  `src/components/LlmPriceRanking.tsx`; fetch dinâmico com cache 24h localStorage +
  fallback hardcoded; URL dinâmica jsDelivr `migueldorosario1/cafezinhomediagroup@main/data/ranking_llm.json`).
- **Aiatolah News — ✅ tem e está no ar:** `https://aiatolah.com/rankings` (HTTP 200),
  página `src/pages/rankings.astro` + cânone `src/data/ranking.json` (com campo
  `quality` S/A/B e `speed`).
- **Agente atualizador VIVO:** cron Tencent `0 9 * * * flock -n /tmp/precos_llm.lock
  /root/venv/bin/python3 /root/agentes_cafezinho/atualizador_precos_llm.py`; JSON no
  jsDelivr com `updated_at: 2026-08-16T12:00:02Z` (do dia) e campos `quality`, `speed`,
  `custo_resumo_usd/brl`. Painel usa a própria cotação (`_dolar_brl`) para converter —
  não o `usd_brl` estático do JSON.

## Provas

- `python3 -m py_compile` OK local e no servidor; `systemctl is-active cctv-v6` = active.
- `/v6/custos` e `/v6/audiencia` HTTP 200 via Nginx.
- DOM renderizado no navegador: cotação R$ 5,19 no alto; ranking com dados dinâmicos
  (🥇 GLM-4 Flash R$ 0,36/R$ 0,36, 🥈 Mistral Small, 🥉 DeepSeek V4 Flash 🏆S …);
  telemetria hoje R$ 33,22 / 7d R$ 137,96 / 30d R$ 2.364,07; gráfico com legenda "eixo em
  reais (R$)"; audiência com card "▲ +1% MM7 vs semana anterior (7.931)" e legenda da
  linha tracejada.
- Únicas menções a "US$" na página = cotação de referência (intencional, pedida).

## Lições

- A captura de tela do navegador embutido (IAB) falhou nesta sessão ("screenshot capture
  failed" e depois timeout 30s) — `domSnapshot` serviu como homologação visual textual.
- jsDelivr responde bem a partir do Tencent (mesma via do agente que commita lá).
- Fallback embutido garante que o ranking nunca quebre a página se o agente/jSDelivr cair.

## Catalogação

- Fórum: `Foruns/forum_painel_cctv_v6_custos_reais_ranking_mm7_20260817.md`.
- Nodo: `CEREBRO_NODE_OBSERVABILIDADE.md` §19.
- Monitor: linha da sessão marcada ✅.

— ZCode (Qwen 3.8-Max), 17/08/2026
