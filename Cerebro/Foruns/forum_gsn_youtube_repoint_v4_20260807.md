# Fórum — GSN YouTube FUNCIONANDO no globalsouth.news (repoint V4 + canais completos)

> **Data:** 2026-08-07 ~14:30 UTC (11:30 BRT) · **Autor:** Kimi K3 / ZCode · **Ordem do Miguel (voz, ~11:20 BRT):** "vamos dar uma força pro Global South News, botar os vídeos, botar o agente YouTube do Global South News pra funcionar, com aqueles canais que já te passei"
> **Memória técnica:** `Memorias/memoria_gsn_youtube_repoint_v4_20260807.md`

## Decisões/resultados (resumo)

1. **Causa-raiz encontrada:** o agente YouTube do GSN estava VIVO (coletor+publicador no droplet), mas publicava no **repo legado** `global-south-news.git` — que NÃO serve o site. O site globalsouth.news é servido pelo `globalsouth-v4.git`. Os vídeos viravam posts no beco sem saída.
2. **Fix aplicado e provado AO VIVO:** publicador repontado pro clone V4 no droplet (`/root/gsn_v4/globalsouth-v4`), frontmatter no schema V4 (com `hero_legenda`/`hero_credit`/`source_name`/`source_url` — regra da legenda obrigatória), **commit-guard** (prova = HEAD==origin), logs explícitos de falha de LLM (o post "Gary" de 06/08 tinha morrido em silêncio no redator + expiração de 6h da fila).
3. **1º post real publicado hoje:** *"Ambassador Chas W. Freeman: 'It's basically a declaration of independence from American tutelage'"* (Dialogue Works / Nima Alkhorshid) — HTTP 200, hero real `youtube-1mco7F7ZzA4.jpg` (245KB), iframe do vídeo, legenda visível, na home. HEAD==origin `8453943c`.
4. **Lista de canais completa (6/6):** Judging Freedom, Glenn Diesen, Dialogue Works, Daniel Davis / Deep Dive (já ativos) + **Neutrality Studies** (`UCHdLVKdAeG6zAeZMGZh91bg`) e **MFA Russia** (`UCIULQ7Y_Y5UiH2Rqqw8Tl7w`) — os 2 placeholders resolvidos via scrape do feed RSS oficial.
5. **Incidente de bancada (corrigido na hora):** 1º teste vazou commit de teste pro origin real (falha minha no setup: `&&` não executou o `set-url` → push foi pro GitHub). Removido com force-push em minutos (janela limpa), HEAD==origin verificado, repo intacto. Lição registrada na memória: bancada = set-url pro bare ANTES de qualquer operação, nunca depender de `&&`.

## Pendências sinalizadas (decisão do Miguel, não urgente)

- **Bot legado "Publish GSN hourly batch (0)"** (NYC `gsn_remote`) segue rodando vazio e inflando o repo legado + log de 143MB. Sugiro desligar — entra na faxina/plano de limpeza.
- **ZHIPU/GLM sem saldo** (429 余额不足) no roteador GSN — a cascata DEEPSEEK segura, mas o editor fica sem a 1ª opção. Recarregar ou remover da cascata.
- Transcrições expiram em 6h (`YOUTUBE_INBOX_MAX_IDADE_HORAS`) — com cron 6/14/22 UTC, 1 falha de LLM pode expirar o item. Avaliar subir p/ 12h.
