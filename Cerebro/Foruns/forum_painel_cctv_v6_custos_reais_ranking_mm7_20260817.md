# Fórum — Painel CCTV V6: custos em reais + ranking de LLMs + MM7 vs semana anterior (17/08/2026)

**Ordem do Miguel (17/08 ~00:30, chat ZCode):** na página `/v6/custos`, TUDO em reais —
com a cotação do dólar em destaque NO ALTO, nada em dólar; incluir o ranking dinâmico de
preços+qualidade das LLMs criado para o Moka Reader (e que também existe no Aiatolah News);
no gráfico de custo diário, tudo em reais e **escrito** que é real. Na página `/v6/audiencia`,
adicionar a MM7 versus a MM7 da semana anterior.

## O que foi decidido/feito

1. **Custos 100% em R$.** Removidas todas as colunas/cards em US$ (por modelo, por agente,
   por provedor, stats de hoje/7d/30d). Todos os valores convertidos pela cotação da página.
   A única menção a "US$" que sobrou é a própria cotação de referência (US$ 1,00 = R$ X) —
   que o Miguel pediu em destaque.
2. **Cotação no alto.** Novo card-banner dourado no topo da página com `R$ 5,19` em fonte
   grande + fonte (open.er-api.com, cache 24h) + aviso "tudo nesta página está em reais".
3. **Gráfico de custo diário em reais.** Eixo rotulado `R$`, tooltips `R$`, legenda
   "💵 eixo em reais (R$)" e título "Custo diário (em reais)".
4. **Ranking dinâmico de LLMs na página — NO FINAL (ajuste 17/08 ~01:25, ordem Miguel).**
   Nova seção "🏆 Ranking dinâmico de preços + qualidade das LLMs (Mural das IAs)" com o
   MESMO cânone do Moka Reader/Aiatolah: medalhas 🥇🥈🥉, bandeira+empresa, qualidade
   (🏆S/A/B com cores), velocidade, entrada/saída **R$/1M tokens** e "resumir 1 livro"
   (15k in + 1k out) em reais. Dados do agente `atualizador_precos_llm.py` (Tencent,
   cron diário 09:00 UTC) via jsDelivr, cache 6h no servidor, fallback embutido de 16
   modelos p/ nunca quebrar. **Ordem final da página: cotação no alto → telemetria →
   gráfico → por modelo/agente → saúde das LLMs → por provedor → ranking (última seção).**
5. **Audiência: MM7 × MM7 semana anterior.** Card novo "MM7 vs semana anterior" (delta % +
   valor da semana anterior) e linha tracejada dourada no gráfico da MM7 = MM7 defasada
   7 dias, com legenda.
6. **Verificação pedida ("confere se o Moka está mesmo o ranking"):** ✅ ESTÁ. O ranking
   existe e está no ar nos dois sites — Moka Reader (`mokareader.com/ajuda`, seção "Mural
   das IAs") e Aiatolah News (`aiatolah.com/rankings`, com campo `quality`). A fonte
   dinâmica (jsDelivr) estava atualizada em 16/08 (agente vivo, cron ativo no Tencent).

## Estado

- **NO AR E VERIFICADO** (17/08 ~01:15): páginas `/v6/custos` e `/v6/audiencia` HTTP 200;
  conteúdo conferido via HTML e DOM renderizado no navegador (cotação no alto, ranking com
  modelos dinâmicos reais, telemetria em R$, card MM7 vs semana anterior com valores).
- Backup no servidor: `painel_cctv_v6.py.bak_pre_custos_brl_ranking_20260817` (rollback =
  restaurar + `systemctl restart cctv-v6`).

## O que falta / o que preciso de você (Miguel)

- Nada obrigatório. Opcional: dar uma olhada visual nas duas páginas e dizer se quer
  algum ajuste (ex.: ordem das seções de custos, coluna de "velocidade" no ranking).
- Obs.: a cotação vem de open.er-api.com (cache 24h); se quiser fonte oficial BCB posso
  trocar.

— ZCode (Qwen 3.8-Max), 17/08/2026
