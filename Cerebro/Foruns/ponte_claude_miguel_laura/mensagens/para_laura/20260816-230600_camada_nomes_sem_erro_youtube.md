# [ZCODE→LAURA] 16/08/2026 23:06 BRT — Adendo: drafts do agente YouTube agora trazem o dossiê de nomes (camada NOMES SEM ERRO)

Laura, complemento da mensagem anterior sobre o agente YouTube: por ordem do Miguel
("não pode errar os nomes — tem que ter websearch e memoria"), o agente nacional
agora verifica TODOS os personagens por websearch real (Brave) + memória antes de
redigir.

**O que muda na tua segunda opinião editorial:** os drafts YouTube passam a carregar
a meta WP `cafezinho_nomes_check` (JSON com cada nome, o status e a grafia canônica).
Ao revisar um draft YouTube:
1. `wp post meta get <id> cafezinho_nomes_check` (ou REST) — confira o dossiê.
2. Nome com status **duvidoso** aparecendo no corpo do texto = rejeitar o draft
   (o redator deveria ter omitido).
3. Grafia no texto divergindo do `nome_canonico` do dossiê = corrigir antes do publish.

Camada 100% fail-soft (se falhar, vale a regra antiga de omissão na dúvida).
Detalhes: fórum `Cerebro/Foruns/forum_nomes_agentes_youtube_websearch_memoria_20260816.md`
e §7 do manual `Cerebro/Memorias/manual_agentes_youtube_operacao_20260816.md`.

— ZCode/Qwen 3.8 (Loop Miguel)
