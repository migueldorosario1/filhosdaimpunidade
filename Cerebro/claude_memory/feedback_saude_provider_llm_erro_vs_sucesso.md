---
name: feedback-saude-provider-llm-erro-vs-sucesso
description: "Ao reportar saúde/crédito de provider LLM, comparar timestamp do último ERRO vs último SUCESSO — nunca usar contagem acumulada do dia (gera alarme falso). E quota_exhausted/429 ≠ saldo zerado."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# Saúde de provider LLM: último-erro vs último-sucesso (nunca contagem acumulada)

Miguel me corrigiu 2026-05-29 ~22:50 BRT (3 mensagens seguidas: "deepseek está com crédito", "zhipu também tem crédito", "qwen está funcionando?") durante o loop Maestro. Eu havia reportado nos Ticks 131/135 que ~5 providers estavam "sem crédito / precisa recarga urgente". **Estava errado em toda a linha.**

**A regra:**
1. **Saúde de um modelo = comparar timestamp do ÚLTIMO ERRO vs ÚLTIMO SUCESSO.** Se há sucesso *depois* do último erro → está OK agora. Ex: deepseek-v4-pro tinha 221× 402 no dia, mas último erro 16:48 e sucesso 22:30 → funcional. Idem qwen-max (sucesso 22:30, zero erro).
2. **NUNCA usar contagem acumulada do dia** (ex. "402 × 221") como estado atual — ela mistura picos de madrugada/manhã já superados e gera alarme falso.
3. **Distinguir tipo de falha:**
   - `402 Insufficient Balance` / `余额不足` = saldo zerado de verdade (mas verificar recência — pode já ter sido recarregado).
   - `429` / `quota_exhausted` / cooldown de circuit breaker = limite de *uso/rate* do tier, **NÃO** falta de dinheiro. Prova diagnóstica: se outro modelo da *mesma conta* funciona (ex. qwen-max OK enquanto qwen3-max em cooldown — ambos Alibaba), então a conta tem crédito; é só cota do modelo premium.
4. **Modelo no fundo da cascata raramente é acionado** → ausência de sucesso recente ≠ sem crédito (pode só não ter sido chamado). Ex: glm-4-plus fica em posição 6-8, quase nunca testado.

**Why:** Miguel controla o billing e sabe o saldo real — alarme falso de "recarga urgente" o faz perder tempo checando contas que estão OK, e mina a confiança nos meus reportes. Foi a 2ª vez (Tick 133 foi a 1ª, com o mesmo deepseek-v4-pro 402).

**How to apply:**
- Comando-padrão por modelo: `erro_ult = grep "MODELO.*(402|401|429|Insufficient|余额不足|quota_exhausted)" | TS | tail -1` vs `sucesso_ult = grep "(maestria|entregue).*MODELO" | TS | tail -1`. (Cuidado: na linha de sucesso o nome do modelo vem DEPOIS de "entregue/maestria" — padrão `entregue.*MODELO`, não `MODELO.*entregue`.)
- Só sinalizar "sem crédito" se: último sinal for erro 402/余额不足 E recente E sem sucesso posterior E o modelo está sendo realmente acionado.
- Lembrar do princípio geral [[feedback-verificar-conteudo-real-wp-ao-flagrar]]: verificar empiricamente o estado atual antes de afirmar dano/problema.
