# 🧠 Memória — Moka Reader 6.5: investigação de bugs (13/08/2026)

**Fórum-irmão:** `Foruns/forum_moka_reader_bugs_65_20260813.md`
**Sessão:** ZCode (Kimi K3), workspace ZCodeProject. Relato do Miguel (iPad).

## Fatos técnicos verificados (lendo o código)

- Repo: `Outros/Aplicativos/Moka/Moka-Lab`, branch `main`, remote `git@github.com:migueldorosario1/moka.git`. `git status -sb` = `## main...origin/main`, `rev-list --left-right --count` = `0 0` → **local idêntico ao origin/main**. Produção (curl em `/ajuda` e `/tutorial`) mostra **6.5**.
- Reader.tsx: **2379 linhas**. Importa `translatePageStream, explainPageStream, translateStream, explainStream, translateForSpeech` de `@/lib/ai-client` (linha 18).
- `lib/ai-client.ts` — `resolveProvider()` (linha 52): usa `getEntryForText()`; **sem chave → erro orientando a colocar a própria (BYOK, pivô 04/08)**. Transporte = `createProxyTransport("/api/proxy")`. `toMessage()` (linha 70) converte status HTTP em msg amigável (400/401/403/404/429/5xx, network, timeout).
- `translatePageStream` (linha 233): **NÃO define `maxTokens`**; `temperature: 0.3`. Streaming palavra a palavra.
- Rotas API: `/api/proxy` tem `maxDuration = 60`; `/api/proxy-stream` tem **`maxDuration = 60`** (comentário no código: sem isso o Vercel Hobby corta em 10s). `runtime="nodejs"`, `dynamic="force-dynamic"`. Allowlist anti-SSRF: z.ai, openai, deepseek, moonshot(.cn/.ai), dashscope.aliyuncs, anthropic, generativelanguage, together.
- **Fluxo tradução full-page** (`Reader.tsx` ~1111 `handlePageAction`): chama `translatePageStream(currentPageText, ctx, onChunk)`; erro → `setPageTranslation("⚠️ "+error)`; sucesso → auto-save em notas. **Nenhum log persistido** — o erro morre na tela.
- **Bug página-reset:** `book/[id]/page.tsx:190` — `onOpenSettings={() => router.push("/configuracoes")}` **navega pra outra rota** (desmonta o Reader). `initialChapterIdx` (linha 184) = `session.chapterIdx || localStorage["moka.chap."+titulo] || 0`. `Reader.tsx:338` `useState(initialChapterIdx)`; `Reader.tsx:341` o useEffect de restore só aplica se `initialChapterIdx > 0` — **se vier 0 (race na hidratação), fica na página 1**.
- **Chaves (6.5):** `lib/config.ts` — cofre `igot.aiVault` (AES-GCM). Seleção por função: `getEntryForText()` (linha 484) usa a entry com `useForText`, senão a ativa (fallback). `setUseForText` (linha 514) é **toggle single-select** (`e.useForText = e.id === entryId ? !e.useForText : false`) — um clique acidental pode desmarcar. `SettingsForm.tsx` (~390-420) tem os 3 checkboxes.
- Commits recentes tentando curar cache de página: `7b34238` (init síncrona), `c42f025` (lê direto), `0ad62c8` (por livro), `df829f4` (salva no setChapterIdx síncrono), `2f4f157` (useEffect quando initialChapterIdx muda).

## Cofre (sem expor valores)
- Só existe `GITHUB_TOKEN_AIATOLAH_KIMI` (projeto Aiatolah) — **não usar no repo moka**. Supabase do Moka existe (auth), mas sem service-role/PAT no cofre pra DDL.

## Próximos passos técnicos
1. Implementar `lib/logger.ts` (captura erros IA + globais, contexto: ação/livro/página/provedor/modelo/erro/stack/UA/ts) + botão "📋 Copiar diagnóstico".
2. Rota `/api/log` → grava em Supabase `moka_logs` (SQL pro Miguel colar no dashboard).
3. Consertar página-reset: salvar posição antes de navegar + restore com prioridade.
4. Endurecer tradução full-page: `maxTokens` + tratamento de timeout + retry.
