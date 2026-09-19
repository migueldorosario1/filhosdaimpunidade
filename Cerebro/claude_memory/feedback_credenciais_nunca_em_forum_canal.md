---
name: feedback-credenciais-nunca-em-forum-canal
description: "Reformulada Miguel 21/05/2026 17:15 BRT — pragmatismo: credenciais em fórum/canal NÃO viram alarme crítico. Ambiente Trindade é fechado, Miguel usa cartões pré-pagos limitando dano, troca chaves periodicamente. Reportar achados sem paranoia. Aguardar 'grande monitoramento de segurança' futuro que Miguel vai conduzir."
metadata:
  node_type: memory
  type: feedback
  originSessionId: a2a780f3-ebca-439c-8179-9660775e2727
---

# Credenciais em fórum/canal — pragmatismo sobre paranoia

**Versão original (Codex Maestro 17:02 BRT):** regra dura "credenciais NUNCA em fórum/canal/Cérebro, só em cofre".

**Reformulação Miguel 21/05/2026 17:15 BRT** após eu fazer report alarmista de "vazamento crítico" sobre 4 arquivos com chaves:

> "Essas chaves que eu boto aqui só tá entre a gente, ninguém vai ver. Tenho sistema de segurança em cada sistema. Meu próprio cartão é pré-pago, não tem muito dinheiro lá. Eu fico monitorando. Em algum momento prepara aí pra a gente fazer um grande monitoramento de segurança pra melhorar tudo, mas por enquanto não fica com muita paranoia. Vai em frente, vamos trabalhar. Eu preciso às vezes expor a chave aqui pra adiantar o trabalho. Depois eu troco essas chaves todas, não se preocupa."

**Como aplicar:**

- **Boa prática que mantém:** ao escrever em fórum/canal, prefira mascarar (fingerprint `sk-d0d8...e9e5`). Não é proibido, mas é o caminho default elegante.
- **Não bloquear trabalho por isso:** se Miguel ou outro agente colar chave por pragmatismo (acelerar troubleshooting, alinhar Trindade), trate como decisão consciente — não escale como "crítico" no chat dele.
- **Não fazer report alarmista:** detectar vazamento em fórum antigo (tipo `forum_algoritmos_todas_llms.md` de 15/05) não é incidente — é estado normal do ambiente Trindade. Pode mencionar em tick como "FYI achei N chaves em N fóruns" sem dramatização. Miguel gerencia o risco no nível dele (cartão pré-pago, rotação periódica).
- **Quando ESCALAR de verdade:** só se chave vazar **PARA FORA do ambiente Trindade** (commit em git público, paste em pastebin, log em CDN, screenshot em rede social, e-mail externo). Aí sim é incidente.
- **Caso fundador IPRoyal:** Codex fez mascaramento porque era prática de Antigravity (que precisa ser ajustado) + a chave do parceiro IPRoyal tem valor sensível prolongado externo. Padrão exceção, não regra do dia-a-dia.

**Sobre o "grande monitoramento de segurança" futuro:**
Miguel sinalizou que VAI montar um sprint dedicado pra revisar segurança de tudo. Quando vier, contribuir:
- Inventário completo de chaves ativas × histórico de exposição
- Rotação coordenada batch
- Política de mascaramento default em logs/fóruns
- Cofre de chaves separado do Cérebro indexado
- Possivelmente o sprint `vigia_chaves_llm.py` da TaskList #25 vira parte dessa frente

**Erro que cometi 17:08 BRT (lição):** report técnico OK, mas tom "🚨 CRÍTICO / precisa rotacionar agora / vetor do mesmo incidente IPRoyal" virou ruído. Miguel não pediu paranoia — pediu monitor competente. Direto, sem dramatização.

**Relacionado:** [[feedback-comunicacao-humanizada-precisa]] · [[feedback-triplice-chat-forum-canal]] · [[feedback-audit-antigravity-tudo]]
