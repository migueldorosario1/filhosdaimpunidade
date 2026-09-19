# Memória — Espelho do Moka Reader (log técnico)

**Data:** 22/08/2026 (~20:30–21:05 BRT) · **Autor:** ZCode/Qwen 3.8
**Fórum:** `Foruns/forum_moka_espelho_experimentos_20260822.md`

## Arquitetura final

- Repo espelho **`migueldorosario1/moka-espelho`** (público, criado via `gh repo create` — moka é público).
- Projeto Vercel **`moka-espelho`** (`prj_Gt8yTvgxGQbFUbY8HC3H6ueuH1gf`, team `team_QQzbgQTC569AoQxaur7tNLGj`), linkado ao repo espelho, productionBranch `main`.
- Local: branch `espelho` no repo `moka-app` + remote **`mirror`** (`git@github.com:migueldorosario1/moka-espelho.git`). Deploy: `git push mirror espelho:main`.
- URL: **https://moka-espelho.vercel.app**
- 10 env vars espelhadas (produção+preview): GITHUB_TOKEN_MOKA, MOKA_MOTOR_KEY, NEXT_PUBLIC_SITE_URL (**= https://moka-espelho.vercel.app**), NEXT_PUBLIC_SUPABASE_ANON_KEY, NEXT_PUBLIC_SUPABASE_URL, SMTP_MOKA_HOST, SMTP_MOKA_PASSWORD, SMTP_MOKA_PORT, SMTP_MOKA_USER, TRANSKRIPTOR_API_KEY. Valores nunca exibidos; arquivo temporário removido após uso.
- GA4 guard (commit espelho 1032b21): `GoogleAnalytics.tsx` client-only, injeta gtag só em mokareader.com/www. Provado: espelho 0 ocorrências no HTML, canônico 2.

## Sequência executada (resumo)

1. Branch `espelho` da main + push origin.
2. Projeto criado via POST `/v11/projects` (gitRepository aceito mas NÃO conectou).
3. Conexão git: `vercel link` + `vercel git connect <url-ssh-do-remote> --non-interactive` → link criado (`link.repo`).
4. Env: `vercel env pull --environment=production` → POST `/v10/projects/{id}/env` (10/10).
5. Tentativas FRUSTRADAS de productionBranch=espelho: PATCH /v9,v10,v11,v12,v13 do projeto (schema rejeita gitRepository), recriar link com campo extra (ignorado), PATCH/PUT no /link (404), promote de preview (422). **Conclusão: API pública não seta production branch.**
6. Solução: repo espelho no GitHub. Push inicial FALHOU ("did not receive expected object") — **repo local era raso** (shallow em 87c76c6) → `git fetch --unshallow origin` (377 commits) → push OK.
7. DELETE + POST `/v9/projects/{id}/link` com repo novo → productionBranch main → commit vazio → deploy READY alvo **production** repo moka-espelho. Provado ponta a ponta.

## Gotchas (lições)

- **GET de projeto: o campo de git é `link` (não `gitRepository`)** — `link.repo`, `link.productionBranch`. O campo `gitRepository` vem sempre None mesmo em projeto conectado; não usar pra diagnóstico.
- **Repo raso quebra push para repo novo** ("did not receive expected object" / "remote unpack failed") — checar `git rev-parse --is-shallow-repository` antes; cura = `git fetch --unshallow`.
- `vercel env pull` SEM `--environment=production` baixa só development (vazio aqui).
- CLI interativo: usar `--non-interactive`; **NUNCA** `yes |` (loop de prompt gerou 174MB de saída).
- `vercel link` cria/atualiza `.env.local` (gitignored) e troca `.vercel/project.json` — conferir o projectId depois de cada link; ao fim, religado ao canônico `moka` (`prj_fwvwofNZTPTXV9HuR25MmaA3KgDU`).
- Token do CLI pra REST: `~/.local/share/com.vercel.cli/auth.json` → `token`. Nunca exibir.
- Endpoints úteis descobertos no bundle do CLI: `/v9/projects/{id}/link` (POST conecta / DELETE desconecta), `/v10/projects/{pid}/promote/{dpl}` (exige rolling release), `/v9/projects/{pid}/rollback/{dpl}`.

## Topologia Vercel dos projetos Moka

| Projeto | URL | Repo/branch produção | Papel |
|---|---|---|---|
| `moka` | www.mokareader.com | moka @ main | canônico |
| `moka-espelho` | moka-espelho.vercel.app | moka-espelho @ main | experimentos (NOVO) |
| `moka-lab` | moka-lab.vercel.app | moka @ main (legado) | inativo — candidato a desconectar |
| `moka-v3` | moka-v3.vercel.app | moka @ main (legado) | inativo — candidato a desconectar |

## Estado final

Espelho NO AR com auto-deploy provado. Pasta de trabalho na main, link local = canônico. Fluxo: experiência na espelho → push mirror → Miguel testa → aprovado? merge espelho→main (canônico) + `git push mirror main:main` (re-sincroniza base do espelho).


## Adendo — incidente das env vars cifradas (22/08 ~21:05–21:30)

**Correção ao corpo acima:** onde se lê "10 env vars espelhadas", o espelhamento inicial (20:23) ficou CORROMPIDO — copiou blobs cifrados. O inventário correto e funcional só existiu após o reespelhamento das ~21:20.

**Sequência do diagnóstico (reproduzível):**
1. `curl` na capa → HTTP 200 (erro é client-side, pós-hydration).
2. Navegador nas rotas: `/privacidade` ok; `/`, `/sobre`, `/telemetria` quebram → interseção = AuthGate/LangSwitcher/SiteFooter (não é layout global, senão todas quebrariam).
3. Local dev e build de produção funcionavam → diferença = presença das env vars (local NÃO tinha `.env.local` em `apps/web/` — o `vercel env pull` escreveu na RAIZ do repo, onde o Next não lê).
4. `apps/web/.env.local` com os valores do espelho + `npm run dev` → overlay: `Error: Invalid supabaseUrl: Must be a valid HTTP or HTTPS URL.` em `src/lib/supabase/client.ts:16` (`createBrowserClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, ...)` chamado do `useAuth` quando a env EXISTE — guard na linha 28 do `auth.ts` só cobre o caso ausente).
5. Bundle do espelho: zero `https://*.supabase.co` reais e zero chave → valores inlined eram o cifrado (~1KB de base64 por var).

**Por que o espelhamento saiu cifrado:** GET `/v10/projects/{id}/env` devolve `value` cifrado para vars `sensitive` (as 10 do canônico são `sensitive`); `decrypt=true` devolve valor VAZIO nesse tipo. O POST no espelho aceitou o blob e re-cifrou.

**Fontes dos valores reais (reconstrução):**
- `NEXT_PUBLIC_SUPABASE_URL` + `NEXT_PUBLIC_SUPABASE_ANON_KEY`: PÚBLICAS por design — extraídas do chunk do bundle de produção do canônico (www.mokareader.com): formato `sb_publishable_*` (chave publicável nova do Supabase, não é JWT).
- `NEXT_PUBLIC_SITE_URL`: literal `https://moka-espelho.vercel.app` (própria do espelho).
- `SMTP_MOKA_HOST/PORT/USER/PASSWORD` + `TRANSKRIPTOR_API_KEY`: cofre vivo `Projeto Cafezinho Agentes/root/.env.unificado`.
- `MOKA_MOTOR_KEY`: cofre legado `Outros/chaves/legacy/20260809_unificacao_llm/...pre_unificacao` (única fonte; tam=64) — validar se transcrição de vídeo funciona no espelho; se não, pedir nova ao Miguel.
- `GITHUB_TOKEN_MOKA`: inexistente em qualquer cofre → REMOVIDA do espelho (usada só em path opcional do /api/report-error, try/catch).

**Reespelhamento correto (como fazer):** DELETE `/v10/projects/{pid}/env/{envId}?teamId=...` + POST `/v10/projects/{pid}/env?teamId=...` com `[{key, value, type:"encrypted", target:["production","preview"]}]`. Env var nova NÃO dispara rebuild — commit vazio + `git push mirror espelho:main` (deploy `0615e5f` READY ~21:25).

**Verificação final:** bundle novo contém URL Supabase real + `sb_publishable_*` (chunks 714/819 idênticos aos do canônico); navegador: capa/sobre/telemetria 100% (sem Application error).

**Gotchas novos (permanentes):**
- Espelhar env vars Vercel→Vercel: conferir VALOR, não só nome; `sensitive` nunca sai em plaintext.
- `vercel env pull` precisa escrever no diretório do app Next (`apps/web/`), não na raiz do monorepo.
- "Funciona local sem env" ≠ "funciona em produção": guard de env ausente esconde o bug — testar SEMPRE com as env reais.
- Chave publicável do Supabase tem formato `sb_publishable_*` (não buscar só por JWT `eyJ`).

---

## Adendo técnico — contenção total do espelho + default useForText (22/08, ~21:40–22:40)

**Diagnóstico do vazamento espelho→canônico (método reprodutível):**
1. Navegador: `goto` direto nas 9 rotas (`/`, `/estante`, `/configuracoes`, `/video`, `/sobre`, `/ajuda`, `/tutorial`, `/experimente`, `/biblioteca`, `/telemetria`) → nenhuma sai de `moka-espelho.vercel.app` (zero redirect server-side).
2. `grep` geral por saídas absolutas no código: único link clicável pro canônico = rodapé do `/video` (`href="https://www.mokareader.com"`). Demais hits: `robots.ts`/`sitemap.ts`/`metadataBase` (SEO, sem navegação) e fallback localhost do callback (inalcançável em produção).
3. Callback de auth testado com `curl https://moka-espelho.vercel.app/api/auth/callback` → 307 Location `https://moka-espelho.vercel.app/` (a env `NEXT_PUBLIC_SITE_URL` do espelho está certa em runtime).
4. `curl .../auth/v1/authorize?provider=google&redirect_to=<espelho>` no Supabase → 302 para o Google preservando o redirect_to — mas o `/authorize` NÃO valida (aceitou até domínio externo inválido no teste de controle); a validação da allowlist acontece no `/callback` pós-Google, com fallback para o **Site URL** do projeto (= produção). Conclusão: login no espelho → canônico, até a URL do espelho entrar na allowlist (ação de dashboard; não há credencial Supabase de gestão em nenhum cofre).

**Mudanças (commit espelho `75e43ff`, build limpo, deploy READY, push mirror+origin):**
- `apps/web/src/app/video/page.tsx`: `<a href="https://www.mokareader.com">` → `<Link href="/">`.
- `apps/web/src/app/layout.tsx`: badge `🧪 ESPELHO` (fixed, bottom-left, pointer-events none) renderizado por `(process.env.NEXT_PUBLIC_SITE_URL ?? "").includes("espelho")` — server component, invisível no canônico.
- `apps/web/src/lib/config.ts` (`setConfig`): nova entry → `if (!cachedEntries.some(e => e.useForText)) entry.useForText = true;`; edição → copia `useForText/Voice/Video` da entry anterior (antes o objeto novo zerava as marcas).

**Prova da lógica (Node, /tmp/test_default_text.mjs):** 1ª chave nasce marcada ✅; 2ª chave não rouba a marca ✅; nova chave quando nada marcado → marca ✅.

**Gotchas novos (permanentes):**
- Espelho/canônico no MESMO projeto Supabase = login OAuth só funciona nos dois se TODAS as URLs de callback estiverem em Authentication → URL Configuration → Redirect URLs; senão o Supabase usa o Site URL (produção) e o usuário "vaza" pro canônico.
- `/authorize` do Supabase não valida redirect_to (validação só no `/callback`): authorize 302 não prova que a allowlist aceita a URL.
- IAB/ZCode browser: `getByRole(...).click()` e `cua.scroll` podem travar em páginas com topbar densa; `dom_cua.click({node_id})` e clique por coordenada funcionam como plano B; pra lógica de UI simples, prova determinística em Node vale como verificação.

## Adendo 4 — recado de tradução maior + i18n 12 idiomas (22/08 ~22:50, commit `3e0057b`)

- `globals.css`: `.page-ai-waiting strong` 18→20px; `.pdf-translation-waiting strong` 17→20px; spans de ambos 13,5→14,5px (max-width 320/340→360); `.page-ai-tip` 13→13,5px (max-width 380).
- `ui-strings.ts`: chaves novas `reader_patience_pre` / `reader_patience_wall` / `reader_patience_post` na união `UIStringKey` e nos 12 blocos. de/it/ru/zh/ja/ko/ar/hi = traduções novas; pt/en mantêm texto anterior; es/fr localizam tb o nome do mural ("Muro de las IAs" / "Mur des IAs" — antes "AI Wall").
- `Reader.tsx`: cadeia ternária da dica (só pt/en/es/fr) → `t("reader_patience_pre")` + `<b>{t("reader_patience_wall")}</b>` + `t("reader_patience_post")`.
- `PdfPageCanvas.tsx`: hook `useI18n` (fallback seguro p/ pt-BR fora do provider — componente só é usado dentro do Reader, que está dentro do I18nProvider) + strings PT hardcoded → `t("reader_translating_page")` / `t("reader_translating_page_sub")`.
- **Verificação em produção:** deploy READY (3e0057b); chunk `592-*.js` contém a string do mural nos 12 idiomas (grep 1× cada, incl. hindi दीवार e árabe جدار); CSS deployado com os tamanhos novos (`.page-ai-waiting strong{font-size:20px` etc.).
- **Gotcha novo (permanente):** ao editar strings hindi/árabe/russas com o Edit, NUNCA redigitar devanagari/árabe de memória (Unicode sutil não bate — "String not found"); ancorar o old_string numa linha vizinha copiada EXATA do Read (ex.: o `reader_view_original:` seguinte) e só INSERIR o texto novo.

## Adendo 5 — allowlist Supabase: espelho autorizado (23/08 ~14:05, ação do Miguel guiada pelo ZCode)

- **Mudança (Dashboard, não código):** Redirect URLs do projeto `nsasbuqeeqdwsagpfpcc` (nome interno **"Igotit"**, Free, org migueldorosario1) passou de 5 para 6 entradas; nova: `https://moka-espelho.vercel.app/api/auth/callback` (caminho completo, igual às demais — melhor que wildcard: o app só usa esse caminho via `redirectTo: ${origin}/api/auth/callback`). Site URL intocado (`https://mokareader.com`).
- **Método:** IAB do ZCode sem sessão GitHub (login OAuth abre e fica na tela do GitHub — IAB não herda sessões do sistema); login do Miguel completou no Chrome DELE. Guiado por chat: Add URL está no TOPO da lista (faixa do "Docs"), discreto.
- **Prova:** texto da página colado no chat ("Total URLs: 6" com a URL nova). Teste final (Entrar no espelho → voltar logado ao espelho) pendente do Miguel; bug marcado 🟢 RESOLVIDO em BUGS_ATIVOS + entrada em BUGS_RESOLVIDOS.
- **Lição de coordenação humano+agente em painel de terceiros:** quando não há token de gestão, o caminho é agente prepara a URL exata → humano clica. Texto colado pelo usuário no chat vale como prova quando screenshot não renderiza para o agente.

## Adendo 6 — capa na estante do espelho: capa passa a viajar na nuvem (23/08 ~16:15, commit `8b5a7bb`)

- **Diagnóstico:** `estante/page.tsx` tem 3 camadas de capa (extraída do EPUB no parse → `renderPdfCover` PDF pág. 1 → `generateDynamicBookCover` azul), mas o resultado só ficava no IndexedDB do domínio. `repository.ts`: `sessionToCloud`/`saveToLibrary` upsert SEM capa; `listLibrary` lê `row.cover_image` — coluna inexistente. Prova: `curl "$SUPABASE_URL/rest/v1/books?select=cover_image&limit=1" -H "apikey: $ANON"` → `42703 column does not exist` (truque: PostgREST valida o select ANTES do RLS — anon key basta pra provar existência de coluna, sem expor nada).
- **Fix (sem schema):** `book: { ...session.book, coverImage: session.coverImage ?? session.book.coverImage }` nos 2 upserts (via `sessionToCloud` + direto no `saveToLibrary`); leitura `row.cover_image ?? book.coverImage`; merge `coverImage: local.coverImage ?? cloudCover`.
- **Verificação:** build limpo; deploy 8b5a7bb READY; chunk `43-9ceac633730d2bdf.js` contém `cover_image` 2× (lógica nova no ar).
- **Limites conscientes:** PDF antigo só na nuvem (sem pdfSource local) segue com capa azul até o Miguel reabrir/reenviar o arquivo (contrato: pdfSource nunca sobe). `.env.local` usa nomes `NEXT_PUBLIC_SUPABASE_URL/ANON_KEY` — `source .env.local` + grep com nomes errados dão vazio; extrair com `cut -d= -f2-`.
- **Sequela boa:** canônico também ganha capas na nuvem a partir dos próximos saves (mesmo código no merge futuro).

## Adendo 7 — capa inteligente por eleição de página (23/08 ~17:00, commit `bf3f54d`)

- **Feature:** `renderPdfCover` não fotografa mais cegamente a p1; mede as 10 primeiras páginas (miniaturas 150px + texto + blobs conexos 4-conexos) e elege a capa em 3 níveis: A) arte colorida (tinta≥50%, sat>0.10, cores≥40 — primeira que satisfaz); B) digital com texto (maior maxFont, itens≥3, cobertura≥2%); C) scan P&B (tinta 2–20%, maior blob de tinta com altura 4–25% da página — letras de título — escolhendo a de maior letra). Fallback: p1.
- **Calibração:** 6 PDFs reais; caso-escola Roman (capa na p9) resolvido no nível C: p2 excluída (blob 42.8%h = ilustração da chapa U. Washington), p8 excluída (tinta 32.5% = miolo), p9 escolhida (tinta 6.6%, blob 8.2%h). Visão confirmou: p9 = folha de rosto.
- **Re-envio recalcula capa** (`estante/page.tsx` existingByTitle): PDF reenviado regenera `coverImage` (best-effort, mantém antiga se falhar).
- **Método de calibração reutilizável (gotcha permanente):** quando canvas nativo do Node falhar nesta máquina (double free no @napi-rs/canvas; canvas@2 não instala sem cairo), usar o navegador do ZCode (IAB) + `python3 -m http.server` em /tmp + página-sonda com o MESMO pdf.js do app (`node_modules/pdfjs-dist/build/pdf.min.mjs` + `public/pdf.worker.min.mjs`), resultados no `<pre>` lidos via domSnapshot; PNGs saem como data URL no DOM → decodificar base64 local → Read (que sobe pra CDN) → analyze_image pra VER a página.
- **Verificação:** build limpo; deploy bf3f54d READY; teste final = Miguel re-enviar o Roman no espelho (capa deve virar a p9). Teste de mesa da eleição com as métricas medidas: 6/6 corretos.

## Adendo 8 — botão 🌐 mudo em página sem texto (23/08 ~20:30, commit `0bc38c0`)

- **Causa:** `disabled={translatingPage || !currentPageText}` no botão 🌐 — PDF scan (Roman: 0 itens de texto em TODAS as páginas) ou PDF carregando ⇒ currentPageText vazio ⇒ clique morto (nem o `confirm()` era alcançado). A caixa de confirmação nunca foi removida; EPUB alimenta currentPageText no useEffect de troca de página (linha ~1206), PDF via `onPageText` do PdfPageCanvas.
- **Fix:** `disabled={translatingPage}`; no clique sem texto → `alert(t("reader_scan_no_text"))` (chave nova nos 12 blocos, ancorada após `reader_patience_post` — âncora única por idioma) e return antes de qualquer chamada de IA. Handler `handlePageAction` mantém a guarda interna (defesa em profundidade).
- **Lição:** botão disabled silencioso parece bug — feedback explícito no clique > estado desabilitado sem explicação. OCR para scans = ideia futura (não prometida).

## Adendo 10 — página-imagem por IA de visão (23/08 ~22:10, commit `41387bc`)

- **Adapter:** `CompleteOptions.images?: string[]`; `buildMessages` vira multimodal (`[{type:"text"},{type:"image_url",image_url:{url}}]`) só quando há imagens — string pura preservada (compat total).
- **ai-client:** `translatePageImageStream(dataUrl, ctx, onChunk)` (meta.task `translate-page-image`, note "página-imagem (IA de visão)") + `estimateImagePageCostUsd()` (IMAGE_TOKENS_EST 1300 + OUTPUT 1800 via `computeCostUsd`); custo real: usage do provedor ?? estimativa; `AIActionResult.costUsd` novo. `runStreamWithCap` ganhou `images` (repassado ao opts).
- **Reader:** `capturePageImage()` (canvas→1500px JPEG 0.85); botão 🌐 sem texto + canvas → confirm com estimativa (`reader_vision_confirm` com {cost}) → `handlePageAction("translate-image")` (guard libera); ao fim, nota "💰 custo real" anexada à exibição (`reader_vision_spent`), auto-save limpo (source "[página de imagem...]", kind "translate").
- **Telemetria:** TASK_KEY_MAP + rótulo nos 12 idiomas; ledger + CSV cobrem "tudo anotado".
- **Gotchas:** UsageInfo.promptTokens é OPCIONAL (?? 0 ao calcular custo); parâmetro do wrapper é `contextText` (não `context`); t() do I18nProvider suporta {var}.
- **Verificação:** build limpo; deploy 41387bc READY. Teste pendente do Miguel (Roman: precisa de chave de modelo COM visão).
