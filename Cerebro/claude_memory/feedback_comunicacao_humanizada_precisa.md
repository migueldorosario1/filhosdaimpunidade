---
name: feedback-comunicacao-humanizada-precisa
description: "Regra Trindade aprovada por Miguel 21/05/2026 12:32 BRT — mensagens copy-paste pra Miguel devem ser humanas/claras MAS tecnicamente precisas, sem ambiguidade. Sempre explicitar responsável/escopo/autorização/limites em mensagens de missão."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2a780f3-ebca-439c-8179-9660775e2727
---

# Comunicação Humanizada com Precisão Técnica

**Regra Codex Maestro 21/05/2026 12:32 BRT (aprovada por Miguel).**

Mensagens que vão pro chat do Miguel pra ele repassar entre agentes — tom humano, claro, fácil de ler, **MAS sem perder precisão técnica nem deixar ambiguidade**.

**Why:** modelo copy-paste-friendly do [[feedback-resumo-humanizado-copy-paste-friendly]] já estava em uso, mas mensagens curtas tipo "Fase 1 pode seguir" causaram confusão (com quem? em qual arquivo? pode publicar? mexer no cron?). Precisão técnica é não-negociável.

**How to apply:** Quando orientar missão, autorizar fase ou pedir ação a outro agente, explicitar SEMPRE:

1. **Quem é o responsável** (Claude / Codex / DS / Kimi Code / AG)
2. **O que deve ser feito** (verbo + objeto claro)
3. **Em qual arquivo, fórum ou sistema** (path completo)
4. **Até onde a pessoa pode ir** (escopo positivo)
5. **O que NÃO está autorizado** (escopo negativo — limites)
6. **Backup/rollback/validação obrigatório** (procedimento de segurança)
7. **Onde isso foi registrado** (fórum, Cérebro, memória)
8. **Se também foi pontuado no canal** (canal_trindade.md)
9. **Assinatura** com nome, papel e horário BRT

**Exemplo ruim (ambíguo):**
> Fase 1 pode seguir.

**Exemplo bom (preciso):**
> Kimi Code pode seguir com a Fase 1A do Rio Carta, apenas em shadow mode, no arquivo `riocarta_smoke_markdown.py`, sem alterar publicação real e sem mexer no cron remoto. Antes do smoke real, precisa salvar laudos também nos caminhos de erro/skip. Codex Maestro vai auditar o resultado antes de qualquer promoção para modo ativo.

**Registros canônicos:**
- `CEREBRO_NODE_COMUNICACAO.md §21`
- `Foruns/forum_nova_trindade_20260521.md §13`
- `Memorias/memoria_codex_maestro_20260521.md`
- `Foruns/canal_trindade.md` (pontuado 21/05 12:32 BRT)

Aplica a mensagens internas Trindade E mensagens que Miguel vai repassar entre agentes. Em ticks de monitoramento (rotina), mantém formato sintético atual — esta regra é pra MISSÕES e AUTORIZAÇÕES.

Relacionado: [[feedback-resumo-humanizado-copy-paste-friendly]] · [[feedback-registrar-tudo-canal-sempre]]
