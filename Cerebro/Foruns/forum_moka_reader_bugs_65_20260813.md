# 🐛 Fórum — Moka Reader 6.5: investigação de bugs (13/08/2026)

**Sprint:** investigar por que o Moka Reader "não está funcionando direito" (relato do Miguel, usando no iPad). Sessão: ZCode (Kimi K3, workspace ZCodeProject).
**Memória-irmã (log técnico):** `Memorias/memoria_moka_reader_bugs_65_20260813.md`

## Contexto / onde está o código

- **Repo canônico:** `Outros/Aplicativos/Moka/Moka-Lab`, branch `main`, remote `git@github.com:migueldorosario1/moka.git`.
- **Local 100% sincronizado com o ar** (`git status` = `main...origin/main`, diff 0/0). Site em produção = **versão 6.5** (confirmado em `/ajuda` e `/tutorial`).
- Arquitetura da IA: **100% BYOK no navegador** — a chave fica criptografada no `localStorage` (`lib/config.ts`, cofre `igot.aiVault`), e as chamadas passam por proxy serverless na Vercel (`/api/proxy` e `/api/proxy-stream`) pra furar CORS. **Não existe mais IA da casa/pontos** (pivô 04/08).
- Últimos commits do main: feature **6.5 "mix de IAs"** (checkboxes `useForText/Voice/Video`, commit `2fe7019`) + vários fixes de "cache de página" (`7b34238`, `c42f025`, `0ad62c8`, `df829f4`) — sinal de que o bug de posição já vem sendo atacado.

## Relatos do Miguel (sintomas)

1. Tradução de **página inteira** dá erro e **demora um tempão**.
2. **Cache** instável — às vezes funciona, às vezes não.
3. Tá na **página 50**, entra em Configurações, ao sair **volta pra página 1** (perde a posição). "Qualquer coisa que faço não volta pra página que eu estava."
4. **Chaves** instáveis.
5. "Tem **crédito no DeepSeek** em vários reais" mas a tradução falha (ou seja: não é saldo).

## Diagnóstico (hipóteses fortes no código — a confirmar com LOG)

- **(1) Tradução full-page lenta/erro:** `translatePageStream` (`lib/ai-client.ts`) usa streaming via **`/api/proxy-stream`**, que tem **`maxDuration = 60`s**. Página grande + modelo lento → a Vercel mata a função em 60s → "Failed to fetch" no cliente. Agravante: `translatePageStream` **não define `maxTokens`** → página grande pode gerar saída enorme/demorada. "Tem crédito mas falha" ⇒ problema de **timeout/transporte**, não de saldo. ⚠️ Precisa do log pra confirmar o status HTTP exato.
- **(3) Página reseta pra 1:** o botão Configurações faz **`router.push("/configuracoes")`** (`book/[id]/page.tsx:190`) — **navega pra outra rota e desmonta o Reader**. Ao voltar, remonta e relê `initialChapterIdx = session.chapterIdx || localStorage`. O `useEffect` de restore (`Reader.tsx:341`) só aplica se `initialChapterIdx > 0`; se a leitura do cache falha/ainda não hidratou naquele instante (race), cai pra `0` = página 1. **Cura:** salvar a posição ANTES de navegar + restaurar com prioridade.
- **(4) Chaves:** o 6.5 introduziu seleção por função. `getEntryForText()` usa a entry marcada `useForText`, senão a ativa (fallback). Se a entry marcada tá corrompida ou a marcação mudou sem querer (toggle single-select), a tradução usa a chave errada → falha mesmo com outra chave boa.
- **(2) Cache intermitente:** mesmo mecanismo do (3) — race na leitura do `localStorage` na hidratação.

## Plano — sistema de LOGS (pedido explícito do Miguel)

Objetivo: capturar erros no navegador/iPad (tradução, navegação, erros globais) com contexto (ação, livro, página, provedor, modelo, erro, stack, userAgent, timestamp) pra eu analisar.

- **(a) Botão "📋 Copiar diagnóstico"** — funciona JÁ, zero backend. Ao dar erro, monta relatório e o usuário copia/cola pra mim.
- **(b) Envio automático pro Supabase** — tabela `moka_logs` + rota `/api/log`. Eu leio via SQL. **Precisa o Miguel colar 1 SQL no dashboard** (precedente: BUG-20260722). GitHub puro descartado (geraria spam de issues/commits e não há token confiável pro repo moka — só existe `GITHUB_TOKEN_AIATOLAH_KIMI`, de outro projeto).

## Estado / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** investigação mapeada; código localizado (Moka-Lab 6.5 = o que tá no ar); hipóteses fortes pros 4 bugs.
- **Falta:** (1) implementar o log (a+b) pra capturar o erro real do iPad; (2) consertar página-reset (causa clara); (3) endurecer tradução full-page (timeout/maxTokens); (4) revisar lógica de chaves.
- **Preciso de você:** confirmar se implemento os logs agora (Supabase pede 1 SQL seu no dashboard) e qual bug atacar primeiro.

---

## ✅ IMPLEMENTADO — Moka 6.5.1 (13/08 ~09:35, commit `31c86d8`, NO AR)

**Ordem Miguel:** *"ok montar o a"*. Sistema de diagnóstico de erros entregue e deployado (Vercel confirmou — `/configuracoes` já mostra o botão).

**O que foi pro ar:**
- **Botão "📋 Copiar diagnóstico"** junto do erro de tradução de página (aparece **só quando falha**). Clica → copia relatório completo → "✅ Copiado! Cole pra mim".
- **Atalho "📋 Copiar diagnóstico"** nas Configurações (sempre visível — copia o último erro mesmo depois de sumir).
- **Captura automática** de todos os erros de IA (provider/modelo/status HTTP) + erros globais (window.onerror/rejection). Guarda últimos 20 no dispositivo.
- **Segurança:** o relatório NUNCA inclui a chave de API — só provedor/modelo. Fallback de clipboard pro iPad/Safari.

**Arquivos:** `lib/diagnostics.ts` (novo) · `lib/ai-client.ts` · `Reader.tsx` · `SettingsForm.tsx` · `I18nProvider.tsx` · `globals.css`. Build+tsc limpos.

**Como o Miguel usa:** quando a tradução falhar no iPad, toca em "📋 Copiar diagnóstico" e cola pra mim → eu vejo o status HTTP exato e aponto a causa real.

**Falta (próximos sprints):** (b) envio automático pro Supabase `moka_logs` (precisa SQL do Miguel) · conserto página-reset · endurecer tradução full-page (maxTokens/timeout/retry) · revisar chaves.

---

## ✅ Adendo — rodada de consertos (13/08, Kimi)

- **6.7** (`ab84e9d`): e-mail automático de diagnóstico via nodemailer+SMTP GoDaddy (rota `/api/report-error`) + resposta "em até 24h" c/ especialista localizado. **PROVA IMAP:** e-mail de teste chegou no info@ (18→19). Miguel colou as 4 env vars `SMTP_MOKA_*` na Vercel.
- **6.7.1** (`91cd361`): **timeout tradução 60s→300s** (proxy + proxy-stream; DeepSeek V4 thinking estourava 60s — causa raiz q o Miguel identificou) + diagnóstico robusto (2ª camada de captura no Reader) + marcador guarda pageLabel+preview (primeiras 50 palavras).
- **6.8** (`27b9233`): marcador **navega** ao clicar (reset página local+scroll topo) + **indicador 🔖** na chave de zoom + **confirmações** (12 idiomas) + **lixeira** nos marcadores e anotações.
- **Diagnóstico do info@ (IMAP):** o 1º diagnóstico do Miguel veio "nenhum erro capturado" → por isso a 2ª camada de captura. **Importante:** o `APP_VERSION` ficou "6.6" (não bumpado em 6.6.1/6.7/6.8) — corrigir na próxima.

---

## 🔑 CAUSA RAIZ do marcador descoberta (13/08 ~12:35, Kimi) — PRÓXIMA CORREÇÃO

**Sintoma do Miguel (preciso):** *"marquei a página 3, fui pra página 5, clico no marcador 'página 3' e VOLTA pra página 1. E o 🔖 tem que aparecer SÓ na página marcada, posso marcar quantas páginas quiser."*

**Causa raiz (CONFIRMADA pela lógica):** o bookmark guarda **só `chapterIdx`**, mas em livros com **paginação interna** (EPUB por capítulo, ou PDF com `chapterPages`), o usuário navega por **`pageIdx` (página local dentro do capítulo)** — e o `chapterIdx` é o CAPÍTULO. Ao marcar, salva `chapterIdx` (perde o `pageIdx`); ao clicar, `setChapterIdx(bm.chapterIdx) + setPageIdx(0)` → cai na **página 1 do capítulo**. Por isso volta pra "página 1". O `pageLabel` mostra certo (capturado no clique), mas a navegação ignora a página local.

**Solução (próxima rodada):**
1. Bookmark guarda **`globalPageIdx`** (índice global = `pageOffsets.offsets[chapterIdx] + pageIdx`, ou `chapterIdx` puro pra PDF) — além de chapterIdx/pageLabel/preview.
2. Ao **marcar**: capturar `globalPageIdx` atual (var `globalPageIdx` já existe no Reader, linha ~1014).
3. Ao **clicar no marcador**: `goToGlobalPage(bm.globalPageIdx)` (existe, linha ~1093 — converte global→chapterIdx+pageIdx). NÃO usar setPageIdx(0).
4. **`isBookmarked`**: comparar `globalPageIdx` atual com os `globalPageIdx` dos marcadores (não só chapterIdx) → aí o 🔖 aparece **só na página marcada exata**, e dá pra marcar várias.
5. Tipo do bookmark: adicionar `globalPageIdx?: number` (opcional, em `db.ts` Session.bookmarks + Reader props).

**Arquivos a tocar:** `Reader.tsx` (toggleBookmark captura globalPageIdx; onClick usa goToGlobalPage; isBookmarked por globalPageIdx), `db.ts` (tipo), `book/[id]/page.tsx` (onToggleBookmark passa globalPageIdx). Editar `onToggleBookmark` pra `(chapterIdx, meta?)` onde meta tem globalPageIdx.

⚠️ **Crédito Kimi K3 + Qwen esgotaram aqui (12:35).** Continuar no GLM-5.2 (fallback) ou retomar quando Kimi voltar. Estado checkpointado.

---

## ✅ CORREÇÃO DA CAUSA RAIZ — Moka 6.8.1 (13/08 ~12:50, GLM-5.2, commit `a93ec3a`, NO AR)

Miguel conectou os pontos: *"talvez fosse isso a razão do cache... sempre que reiniciava voltava pro começo do capítulo e não pra página. O cache tem que guardar a PÁGINA, não o capítulo."* → **CONFIRMADO, mesma raiz.**

**Implementado (GLM-5.2):**
- **Marcador guarda `pageIdx` (página local):** `isBookmarked` agora compara `chapterIdx E pageIdx` → 🔖 aparece **só na página marcada exata** e dá pra marcar várias páginas. Clique navega via `pendingPage` (volta na página exata, não no começo do capítulo). Tipo `pageIdx?` em `db.ts`/Reader props; `book/[id]` salva.
- **CACHE de posição exata:** agora salva/restaura o **`globalPageIdx`** (índice absoluto) no localStorage (`moka.pos.<titulo>`), não só o `chapterIdx`. Reinicia na **página exata** em que parou. useEffect de restaurar (1x, depois que a paginação do EPUB carrega) + useEffect de salvar (a cada mudança).
- `APP_VERSION` 6.6 → 6.8.
- Build+tsc limpos (exit 0). Push origin/main, HEAD==origin ✅.
- **Aguarda Miguel re-testar:** (1) marcar uma página → ir pra outra → clicar no marcador → volta na exata? (2) 🔖 só na página marcada? (3) reiniciar (F5/fechar e abrir) → volta na página exata (não no começo do capítulo)? Se ainda falhar, diagnóstico robusto vai pegar.

---

## ✅ Mural das IAs + aviso de paciência (Moka 6.8.3, 13/08 ~21:00, commit `a96417b`, NO AR)

- **Aviso durante a tradução da página:** no estado "traduzindo..." aparece *"Tenha paciência — algumas IAs são mais lentas que outras. Veja em nosso **Mural das IAs** quais são as mais rápidas, melhores e econômicas."* (pt-BR/en/es/fr) com **link** `/ajuda#mural-das-ias`.
- **"Mural das IAs":** a seção do ranking (`LlmPriceRanking`) ganhou o título **"🏆 Mural das IAs"** e o `id="mural-das-ias"` (o link rola até ela).
- **Coluna de tempo:** o ranking agora tem **"⏱️ /página"** — segundos estimados pra traduzir 1 página de livro (≈ benchmark honesto: 3s Groq/LPU até 60s Kimi K3/DeepSeek V4 Pro com thinking). Campo `velSeg` em `llm-prices.ts` (mesclado no fetch dinâmico via presetId/modelo).
- Build+tsc limpos. Push origin/main, HEAD==origin ✅. CSS `page-ai-tip`/`lpr-mural` confirmado no ar.
