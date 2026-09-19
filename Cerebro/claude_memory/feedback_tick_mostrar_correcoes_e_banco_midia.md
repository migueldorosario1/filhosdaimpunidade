---
name: feedback-tick-mostrar-correcoes-e-banco-midia
description: "Todo resumo de tick do loop Maestro deve mostrar as correções concretas (de/para) quando houver, e incluir o uso do Banco de Mídia (monitorar de perto 48h a partir de 29/05)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# Resumo do tick: mostrar correções concretas + uso do Banco de Mídia

Miguel 2026-05-29 (~17:00 BRT), durante o loop Maestro.

**A regra:**
1. **Quando houver correções, MOSTRE quais foram** — não basta dizer "3 correções". Trazer no resumo do tick o de/para concreto (título original → corrigido, post_id, motivo). Vale para auditor de títulos GPT e qualquer outro agente corretor.
2. **Incluir o uso do Banco de Mídia em todo resumo de tick** — monitorar de perto nas próximas 48h (a partir de 29/05). Métricas por janela: caminhos resolvidos (og:image/Prioridade 1, Flickr/1.5, banco local/2, Wikimedia, IA), `database is locked`, e — quando agentes adotarem — chamadas a `banco_midia_busca` (entidade) vs busca textual.

**Why:** Miguel quer ver o trabalho concreto do sistema, não só contadores agregados — transparência operacional. E o banco de mídia está em transição (reforma S9 do Kimi entregue, baseline em [[project-baseline-banco-midia-s9]]); ele quer acompanhar a adoção de perto para decidir Fase 2 (Qwen-VL).

**How to apply:**
- No `auditor_titulos_gpt`, distinguir `acao` (efetiva: monitorar/ok/corrigido) de `acao_gpt` (sugestão crua). Mostrar as `corrigido` reais com de/para. **Atenção:** o GPT sugere muito mais `corrigir` (ex. 27 num dia) do que é aplicado (3) — as sugestões barradas frequentemente são alucinação reversa (GPT com conhecimento desatualizado quer "corrigir" fatos corretos). Ver [[feedback-monitorar-auditor-titulos-gpt-cada-tick]].
- Quando flagrar correção suspeita, SEMPRE puxar o título real no WP antes de afirmar dano ([[feedback-verificar-conteudo-real-wp-ao-flagrar]]).
- Fonte das correções: `/root/agent_data/auditor_titulos_gpt/auditor_titulos_gpt_YYYY-MM-DD.jsonl`. Banco de mídia: grep marcadores nos logs `master_*.log` (Prioridade/Wikimedia/IA Visual/database is locked).
