---
name: feedback-comparacao-legado-reforma-janela-2h
description: "Miguel 14/06 ~23:55 BRT — comparação de vazão/desempenho 🟦 [LEGADO] vs 🟪 [REFORMA] DEVE usar janela das últimas 2 horas, NÃO o dia inteiro. Dia inteiro mascara: legado começou rodando no início do dia com cadência regular; reforma só ligou depois de N AUTHs e está em modo freio. Comparar 24h injustamente faz o legado parecer sempre 50× melhor — não é comparação técnica útil."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Comparação 🟦 LEGADO vs 🟪 REFORMA — janela das últimas 2h

Miguel 14/06 ~23:55 BRT (após eu reportar "49 publishes hoje 🟦 vs 1 draft hoje 🟪"):

> "ao avaliar legado, não adianta pegar no dia inteiro. tem que pegar nas ultimas 2 horas."

## A regra

Qualquer comparação de **vazão/desempenho** entre 🟦 [LEGADO] e 🟪 [REFORMA] (drafts entregues, publishes, taxa Trib Visual, latência por ciclo, etc) DEVE ser feita na **janela das últimas 2 horas**.

Janelas mais longas (dia inteiro, 24h, semana) são **enganosas** porque:
- 🟦 LEGADO ligou no início do dia com cadência regular (`*/10` cron, ~6 publishes/h)
- 🟪 REFORMA só "começou de verdade" depois de cada AUTH (001, 002, 003, 006...) — cada uma destrava um pedaço
- Boa parte das primeiras horas do dia REFORMA estava parada/em diagnóstico
- 24h dá narrativa "LEGADO 50× melhor" que é **artefato da história**, não medida atual

Janela 2h dá número limpo:
- Estado atual de ambos sistemas (último ciclo recente)
- Efeito real da última AUTH aplicada
- Comparação técnica útil pra decisão (escalar Reforma? voltar atrás? esperar mais 2 ciclos?)

## Why
Caso fundador 14/06 23:50 BRT — reportei "49 publishes hoje 🟦 vs 1 draft hoje 🟪" como prova de bloqueio da REFORMA. Número correto, narrativa errada. O LEGADO publicou 49 ao longo de 24h normais; a REFORMA esteve parada/em diagnóstico até ~22:30 BRT quando AUTH-006 entrou. Comparação justa = últimas 2 horas, que mostra estado atual real.

## How to apply

1. **Em todo dado comparativo Legado vs Reforma** (ticks §53, relatórios, cartinhas, fórum freio, fórum mídia reprovada, K command):
   - Buscar publishes/drafts com `?after=<NOW-2h>` no parâmetro WP API
   - Reportar como "🟦 [LEGADO] últimas 2h: N | 🟪 [REFORMA] últimas 2h: M"
   - Se quiser dado de 24h pra contexto, prefixar como "histórico do dia (não comparável):" e deixar separado

2. **Métricas onde aplica:**
   - Vazão de publishes/drafts
   - Taxa Trib Visual (REPROVADA vs APROVADA)
   - Latência por ciclo
   - Curas §51 aplicadas
   - Erros fact-check

3. **Métricas onde NÃO aplica** (24h ainda faz sentido):
   - Auditoria editorial profunda Cláudia Beatriz
   - Cobertura §93 Google Indexing
   - Inventário cumulativo (total publishes no dia)

4. **Quando "últimas 2h" não tem dado suficiente** (ex: REFORMA acabou de ligar):
   - Usar janela disponível (ex: "desde AUTH-006 entrar 23:00 BRT")
   - Deixar claro que janela é assimétrica e por quê

Relacionados: [[feedback_monitoramento_dual_legado_reforma]] (monitoramento dual + Padrão K + 9 métricas), [[feedback_marcacao_obrigatoria_legado_reforma_todo_comentario]] (marcação obrigatória em comentário).
