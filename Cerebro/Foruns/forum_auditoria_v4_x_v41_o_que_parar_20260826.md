# 🧭 Fórum — Auditoria V4 × V4.1: o que ainda roda de V4 antigo (26/08/2026)

> **Ordem do Miguel (26/08 ~20:00, voz):** "Ué, tá rolando ainda a matéria V4, antiga? Vamos focar no V4.1, ver se tá rolando tecnologia, ciência, inteligência artificial... vê o que de velho tá rolando do V4 para a gente parar e usar só o V4.1. Investiga aí."
> **Executor:** ZCode/Kimi K3 (sessão chat direto). **Natureza:** investigação SOMENTE LEITURA — nada foi parado/alterado. Paradas aguardam o "vai" do Miguel.

## ✅ VEREDITO 1 — V4.1 tec/ciência/IA está SAUDÁVEL e é a única esteira nova de redação

- Vertical **ciência** do V4.1 roda `45 */2` no NYC e produziu hoje: **267808** "Baidu empurra China para chips locais de IA" (publicado 18:09) e **267834** "OpenAI transforma Brasil em base comercial na América Latina" (future 20:29) — tese dinâmica aprovada → gpt-5.5 → FC websearch confirmando claims. Ciclo completo íntegro.
- **Canônico, últimos 7 dias, cats Tecnologia(30)/Ciência(735)/IA(5008): 20 posts** — todos com meta `_v4_versao=4.1` (conferido um a um nos 13 mais recentes). Ritmo 25/08: 8 posts; 26/08: 5+1 agendado.
- Coletor `tec` tem **26 fontes vivas** (MIT Tech Review, Ars, TechCrunch, Verge, Nature, Science, Fapesp, Pandaily/Technode/SCMP, TechCrunch-IA, Ars-IA, VentureBeat-IA, Google AI, OpenAI, Neuroscience News, SciTechDaily, Maglev) — expansão 25/08 (ciência/IA/neuro/medicina) **está implementada**.
- **Ressalva editorial:** o grosso do que sai é tecnologia/IA (chips, China-tech, big techs). Ciência "pura" (Nature/Fapesp/neuro) quase não passa no gate de tese — só 1 dos 20 saiu com cat 735 (267033, Huawei/iFlytek). Não é quebra; é o funil editorial sendo exigente com pauta científica sem gancho de notícia.

## 🔴 VEREDITO 2 — V4 antigo AINDA VIVO em 3 pontos (lista para parar)

1. **Pipeline REGIONAL V4 — `/etc/cron.d/v4_regional`** (escapou da faxina de 24/08, que só comentou o crontab do root!):
   - `7 * * * *` v4_regional_intake.py (1/1h, flagrado rodando 23:07 UTC)
   - `5 10,13,16,19,22,1 * * *` v4_regional_rodar_worker.sh (**6 drafts/dia**, redator antigo sem tese dinâmica/FC)
   - **Hoje criou 5 pendentes:** 267542 (Flávio 34% Quaest RS), 267770 (69% indecisos gov Rio), 267743 (Cleitinho MG), 267724 (candidatos SP nascidos fora), 267589 (desaprovação gov gaúcho 45%).
   - Últimos 5 dias: 16 v4d_regional publicados (a esteira CM/AGY publica os pendentes — ou seja, consome slot e LLM no fluxo velho).
2. **REPETIDOR ESTATAL — cron root `7 */2`:** roda o pipeline CARO completo (LLM + download/upload full-res + caption) e **falha no publish com 400 `cafezinho_imagem_sem_checagem` desde 16/08** — 975 ocorrências no log. Última: hoje 22:08 UTC (media 267819 subiu, post morreu no gate). **~US$1-2/dia queimados para publicar ZERO.** (Incidente já aberto na memória `blocos-saude-esporte-ambiente-v41-religados-20260826`.)
3. **v4_tendencias_intake — `*/30`:** alimenta banco de tendências cujo redator foi desligado 24/08 (`DESLIGADO_V4_20260824`). Coleta sem consumidor.

## 🟢 VEREDITO 3 — V4 que NÃO é velho (MANTER)

- **Coletores+intake das verticais** (geo/pol/eco/cul/amb/esp/sad/tec/dig): são a **matéria-prima do V4.1** — o comentário inline `V4_DESLIGADO_20260824` NÃO desativa cron (gotcha conhecido) e NÃO deve desativar.
- **v4_media_mechanical_promoter + v4_media_expander:** banco de mídia usado pela Ponte Imagens (caçadora reativada 26/08 pelo Qwen).
- **v4_autolimpeza** (`/etc/cron.d/v4_autolimpeza`): arquivamento diário com ordem explícita do Miguel (07/08, "nada se joga fora").
- Temáticos (2/dia/site), YouTube (`0 11,17`), Bot News, comentarista/enxame: produtos separados, fora do escopo "matéria V4".

## 📋 PROPOSTA DE PARADA (aguardando "vai" do Miguel)

| # | Alvo | Ação | Impacto |
|---|------|------|---------|
| 1 | `/etc/cron.d/v4_regional` (worker+intake) | Renomear p/ `.PAUSADO_20260826` (ou comentar c/ tag + backup) | Para 6 drafts/dia V4 velho + LLM. **Decisão editorial pendente:** os 5 Quaest pendentes de hoje são bons p/ mutirão eleições — publicar manual ou migrar regional p/ V4.1 depois |
| 2 | Repetidor estatal (`7 */2` root) | Comentar c/ tag `PAUSADO_20260826_GATE_IMG` + backup crontab | Economiza ~US$1-2/dia; reverter exige ensinar o script o gate §86 (checagem de imagem) |
| 3 | `v4_tendencias_intake` (`*/30`) | Comentar c/ tag | Para coleta sem consumidor |

**Estado da missão:** investigação entregue → **falta** o "vai" do Miguel nos 3 itens (e a decisão sobre os 5 pendentes regionais / futuro do regional) → **preciso de você (Miguel):** aprovar a tabela acima ou dizer o que manter.

Memória técnica: `Memorias/memoria_auditoria_v4_x_v41_o_que_parar_20260826.md`
