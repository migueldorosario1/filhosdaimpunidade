---
name: feedback-gatilho-retomar-ritual-despertar
description: "Quando Miguel disser \"retomar\", ler boletins news + instruções gerais de despertar antes de qualquer outra ação. É gatilho ritual, não conversa."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c864c422-014f-4122-8468-216a5d32e450
---

🔁 **Quando Miguel disser apenas "retomar" (ou começar mensagem com isso), executar ritual de despertar ANTES de responder qualquer outra coisa.**

**Why:** Miguel 2026-06-11 ~18:05 BRT, ao desligar laptop: "quero voltar depois com 'retomar'. ai voce leia boletins news e instrucoes gerais do despertar." Padrão consciente pra economizar tokens e garantir handoff limpo entre sessões — sem precisar repetir o estado todo manualmente.

**How to apply ao receber "retomar":**
1. Ler último handoff em `MEMORY.md` (`estado_fim_sessao_*` mais recente).
2. Ler Boletim News do Cafezinho: `Projeto Cafezinho Agentes/Foruns/boletim_news_*.md` (mais recente) — atualizações do dia/semana.
3. Ler `Foruns/inbox_trindade/claude.md` desde último timestamp.
4. Ler `Foruns/canal_trindade.md` (últimas 48h).
5. Fazer varredura retroativa de posts publicados desde o último tick §53 (Tencent autônomo continuou).
6. Trazer um resumo curto: estado, flags detectadas, pendências, próxima ação sugerida.

**O que NÃO fazer:** responder "retomar" como uma palavra qualquer; pular o ritual; iniciar tarefa nova sem o contexto reconstruído.

Relacionado: [[estado_fim_sessao_20260611_tarde]] (handoff atual), [[feedback_fim_sessao_boletim_news_nao_tarefasdeagora]] (ritual irmão de fechamento).
