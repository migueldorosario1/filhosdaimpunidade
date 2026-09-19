# 📦 Plano de descarga dos rascunhos (ordem Miguel 24/08: "não podemos produzir mais do que temos capacidade de distribuir")

**Inventário (10 dias, CSV ao lado: `inventario_rascunhos_20260824.csv`): 131 rascunhos+pendentes** — V4.1: 54 (nacional, todos 0-1 dia, **51 sem imagem**) · V4: 77 (geo 46, outras 27, tec 2, eco 1, esporte 1 — quase todos COM imagem).

## Temporalidade (heurística por título, transparente no CSV)
- **TEMPORAL (perecível: pesquisa/debate/jogo/eleição): 27** — 12 do V4.1 hoje, 15 do V4 (4 já com 4+ dias = VENCIDOS)
- **Durável (IA/economia/parcerias/estrutural): 59** — o grosso (geo 14 com 4+d, V4.1 25 frescos)
- **Médio: 45**

## Plano de descarga (capacidade real ~20-30/dia)
1. **Descartar já (4)**: temporais V4 com 4+ dias (perecidos: notícia que passou);
2. **Hoje (21 temporais 0-1d)**: revisão expressa — publicar o que ainda pega (ex.: debate da Band é HOJE), descartar o resto amanhã;
3. **Queima da fila (próximos 3-4 dias)**: duráveis com imagem (35) a ~10-15/dia nos slots; duráveis V4.1 sem imagem (25) a ~5-8/dia (capa aplicada pelo editor, Emenda 6);
4. **Médios (45)**: esteira normal após os duráveis.

## Regra nova proposta (a frase do Miguel como mecanismo): GATE DE ESTOQUE no v41_ciclo
Antes de redigir, contar rascunhos+pendentes; **se > 80, pular a rodada** (status `estoque_cheio_pula` — fail-soft: nunca trava, só não empilha). Produção ≤ capacidade de distribuição, automática. + ritmo */2 já vigente. Código pronto, aguarda um "vai" do Miguel.

— ZCode/GLM-5.3 · 24/08 ~10:10. Fontes: WP ao vivo + heurística no título (sem LLM).
