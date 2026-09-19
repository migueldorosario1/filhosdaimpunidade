# 🧠 MEMÓRIA TÉCNICA — OBRA MOKA: CHEFIA ZM + PRINTS 30/30 (30/08/2026)

> Irmã do fórum `Foruns/forum_obra_moka_chefia_zm_20260830.md` (Regra do Tema Duplo). Log técnico completo.

## Ambiente provado

- Chrome headless no Dell: `/usr/bin/google-chrome --headless=new --disable-gpu --no-sandbox --hide-scrollbars --user-data-dir=<tmp> --window-size=W,H --virtual-time-budget=15000 --screenshot=<png> URL` → PNG ok (warnings libva/vaapi inofensivos).
- Rotas 200 (30/08 13:5x): mokareader.com `/`, `/biblioteca`, `/estante`, `/video`, `/ajuda`; mokawriter.vercel.app `/`.
- PIL disponível no Dell (validação anti-branco: ≥12KB e ≥40 cores únicas em amostra ¼).
- Sync `scripts/sync_cerebro_to_github.py`: SOURCE=Downloads/AG → TARGET=~/cerebro-miguel; **ignora** `ponte_laura_completa` (+backups/.git/etc, linha ~120, bug ZL-027); não deleta — pasta `cerebro/Insumos/moka_prints` só no repo sobrevive aos ciclos :07/:37.
- Monitor vivo: FONTE ≡ `~/cerebro-miguel/cerebro/MONITORAMENTO_DE_TRABALHO.md` (raiz do repo = legado).

## Artefatos criados

1. `~/cerebro-miguel/scripts/moka_prints_ronda.sh` — ronda completa: flock anti-sobreposição; 4 alvos × 3 tamanhos; valida anti-branco (PIL); `LOG_RONDAS.md` 1 linha/ronda; commit SELETIVO `cerebro/Insumos/moka_prints`; append de 1 linha na ponte `de_dell.md`; commit ponte; pull --rebase + push origin (+nyc best-effort). Saída: `RONDA_OK|RONDA_DEGRADED|RONDA_FALHA`.
2. Automação ZCode `automation-25e54785` — cron `10,40 * * * *` (interval 30min) rodando o script; alerta na ponte se RONDA_FALHA.
3. Ponte: ZM-20260830-008 (aceite) + linha da 1ª ronda.
4. Prints da 1ª ronda: `cerebro/Insumos/moka_prints/20260830_1359_*` (12 arquivos).

## Lições git da sessão (30/08 14:0x)

- `git rebase --quit` num rebase já aplicado deixa **detached HEAD** — branch `main` local ficou atrás e push dava "non-fast-forward" sem motivo aparente. Cura: `git checkout main && git reset --hard origin/main` (nada perdido; o sync das :07 já tinha publicado meu HEAD).
- Ponte em ritmo quente (DS-Laura/DS-N/DSC/sync): push pode exigir fetch+rebase várias vezes; o sync das :07/:37 publica o que estiver no working tree — commits locais sobem "carona" nele.
- Nunca filtrar demais a saída de erro do git (perdi 3 rodadas por grep; mensagem completa revelou o detached HEAD).

## Estado ao fechar deste registro

- Obra Etapa 1 (MEMÓRIA v1) INICIANDO: ler DSC-021a (INDEX.md), índice MOKA, repo do app (moka-app / laboratório Vercel `moka`), specs DSC-014/017/018/019.
- Despertador rodando; rondas autônomas.

— ZM · ZCode/GLM-5.3 · 20260830 14:10 BRT

## Adendo técnico — Etapa 1 + ckpt 2 (30/08 15:15)

- Repo: `~/ZCodeProject/moka-app` branch `obra/memoria` (base 420aad3). Commits: `2721c15` (ckpt1, +2216 linhas) → `b4f642d` (ckpt2). Push `mirror` (espelho deploya sozinho); canônico `origin` main intocado.
- Novos arquivos: `src/lib/memoria/{types,markdown,store,orcamento}.ts` + `src/app/memoria/page.tsx`; editados: `SectionSwitcher.tsx` (🧠, active "memoria"), `ui-strings.ts` (45 chaves ×12, bloco no TOPO de cada idioma), `globals.css` (seção .memoria-*), `book-translate.ts` (merge devolve `book`), `TranslateBookModal.tsx` (armed/receipt/auto-memória).
- Recibo real = listener do `USAGE_EVENT` ("moka:usage") filtrando `task.startsWith("livro")`; acumula totalTokens/costUsd.
- Fix de reimport: `splitImportFile` DESCARTA o bloco antes do 1º `%%%MOKA-OBJ%%%` (o Índice não vira objeto).
- Build: verde 2× (next build; /memoria 5,4kB First Load pós-tree-shaking).
- Pegadinha: import duplicado de ParsedBook no modal (build acusa "Duplicate identifier") — corrigido.
- Git da ponte: NUNCA fazer append → reset --hard (apaga o append não commitado — perdi o ZM-009 uma vez); ordem certa: fetch/rebase → append → add → commit → push. Push da ponte em ritmo quente: loop fetch+rebase+push.

— ZM · ZCode/GLM-5.3 · 20260830 15:15 BRT

---

## 🔧 ADENDO 6 — 31/08 10:12→10:35: CONCERTOS DO 1º TESTE (commit ee8df8b)

**Log técnico completo:**

- **Repo:** `~/ZCodeProject/moka-app` branch `obra/memoria`; commit `ee8df8b` (17 arquivos, +1110/−155); push `ousadia-mirror obra/memoria:main` → https://moka-ousadia.vercel.app (deploy Vercel automático).
- **Visual:** `TopNav.tsx` ganhou `TopNavActions({back, gearUnset})` (voltar+AuthGate+LangSwitcher+gear+TelemetryIconButton). Páginas padronizadas: estante, memoria, harness, writer, biblioteca, ajuda, video, video/[id] (todas `<TopNav active=... right={<TopNavActions .../>}/>`). Vídeo: wrapper `igot-topbar` com logo duplo REMOVIDO (era o TopNav aninhado dentro do header antigo). CSS: `.bib`/`.help` de `#fff6ee` → `var(--bg)`/`var(--text)`; `.bib-topbar`/`.help-topbar` mortos.
- **Progresso de upload:** `lib/pdf-cover.ts` — `isImagePdf(data, onProgress?)` e `renderPdfCover(data, onProgress?)` (total = PROBE_PAGES+1, o +1 é o render final). `app/estante/page.tsx` — estado `ingest {pct,label}`; etapas: 8% abrir / 10-40% verificar / 45-90% capa (coverProgress callback: `t("ingest_cover",{n:d,total:n})`) / 96% salvar; finally zera. UI `.ingest-progress` (barra 16px + % + label) na estante cheia E no `Uploader` (prop `progress`, condição `books.length===0` sem `!addingBook`). Cuidado TS: bloco de nuvem tinha que ficar APÓS `importText` e `ativa` (block-scoped use-before-declare — 2 iterações de build).
- **Nuvem BYO-bucket:** `lib/cloud.ts` (CloudConfig{provider:host/accessKeyId/secretAccessKey/bucket}; localStorage `moka.cloud.v1` CRIPTOGRAFADO com encrypt/decrypt AES-GCM do `lib/crypto.ts`; endpointOf: r2=`https://<id>.r2.cloudflarestorage.com`, b2=`https://s3.<região>.backblazeb2.com`, s3=host direto; regionOf: auto/região/us-east-1). `lib/cloud-s3.ts` (SigV4 completo com Web Crypto: sha256Hex+hmac; s3Fetch path-style `/{bucket}{path}` com headers host+x-amz-content-sha256+x-amz-date; testCloud GET `?list-type=2&max-keys=1` → ok{objects}|credencial(401/403)|bucket(400/404)|rede(catch=quase sempre CORS); cloudPut PUT text/markdown; cloudGet). `components/CloudSettings.tsx` (provedor em chips + campos por provedor + testar/salvar/esquecer + mensagens de diagnóstico). Página memoria: `cloudSave` (exportMemoriaMarkdown → PUT latest+datado) e `cloudRestore` (GET latest → reusa `importText`); link "Configurar nuvem →" quando não há config.
- **i18n:** 33 chaves (`ingest_*` 4 + `cloud_*` 29) ×12 idiomas. ⚠️ O arquivo tem union TYPE MANUAL `UIStringKey` (além dos 12 blocos) — esquecer dele = `Type error: Argument of type '"cloud_title"' is not assignable` (errou 1× nesta sessão). Blocos: pt-BR com aspas `"pt-BR": {`, demais sem (`en: {`).
- **Build:** `npx next build` OK na 3ª tentativa (2 erros de tipo corrigidos). Lint não roda no build.
- **Monitoramento:** linha aberta 10:12, fechada ✅ em seguida.
- **Ponte:** linha ZM da ronda seguinte consolidará.
- **Pendências carregadas:** CORS do bucket R2 cortesia `moka-memoria-cortesia` (painel Cloudflare → R2 → Settings → CORS: permitir origem moka-ousadia.vercel.app + GET/PUT/HEAD + header authorization) SE quisermos oferecer o cortesia; B2 app key `moka-cortesia` ainda SEM escopo (Miguel recriar Read&Write); G-Drive = parecer negativo por enquanto (OAuth verificação + refresh token 7 dias).


---

## 🔧 ADENDO 7 — 31/08 10:40→10:48 (errata de carimbo: 1ª versão estimada era 11:0x→11:2x): REFORMA DO LEITOR (commit 1131cfe)

- `components/Reader.tsx`: estado novo `bigMenu: "page"|"mark"|"more"|null`. Row-scroll: removidos os 14 icon-btns individuais (📓🏷📸🔊🎤📝🌐🌍) — handlers PRESERVADOS e movidos pros itens do submenu (TTS com estados preparar/pausar/continuar; tradução de página com fluxo visão/scan intacto; foto com confirm; bookmark toggle). Logo+➕+📚+⏹ ficam. Grupo `reader-big-group` centrado com 3 `reader-big-btn`. Row-right: LangSwitcher + AuthGate + wrap ☰ (`reader-more-menu` alinhado à direita) com Link/telemetria/mural + onOpenSettings (usa `tt(lang, ...)` das telemetry-strings p/ telemetria/mural).
- CSS: `.reader-big-btn` 46px/`--surface`, `.reader-big-menu` dropdown absoluto c/ `big-menu-backdrop` fixed z-40 (fecha ao clicar fora), mobile 52px e labels escondidos <640px.
- `app/configuracoes/page.tsx`: right virou `<TopNavActions />`; `cfg-topbar-label`/`cfg-close-btn`/brand duplicado mortos.
- i18n: +5 chaves (`reader_big_page/mark/ask`, `reader_menu_more`, `reader_menu_translate_page`) ×12 + union `UIStringKey`.
- Build OK 1ª tentativa; commit `1131cfe` → push ousadia-mirror; curl: 5 rotas 200, config sem label duplicado, cloud-settings intacto.
- Prompt AGY: `Foruns/PROMPT_AGY_CHECAGEM_MOKA_20260831.md` (9 itens, ✅/❌ c/ print, ANALISA sem editar; sem credenciais — alvo público).

---

## 🔧 ADENDO 8 — 31/08 31/08/2026 10:52: aviso de PDF grande (commit 1d18ebe)

- `app/estante/page.tsx`: `ingestIntro(fileName, fileSize)` — PDF ≥10MB → `t("ingest_big_pdf_intro", {mb, time})`; time = `ingest_time_mid` (10-80MB) | `ingest_time_slow` (>80MB); senão `ingest_open`. pct inicial 6. Deps do useCallback ingestBook +ingestIntro.
- `ui-strings.ts`: `ingest_cover` REESCRITO ×12 ("Renderizando pra achar a capa — página {n} de {total}…" e equivalentes); +`ingest_big_pdf_intro`/`ingest_time_mid`/`ingest_time_slow` ×12 + union. Build 1ª tentativa; push `1d18ebe`; estante 200.


---

## 🔧 ADENDO 9 — 31/08 11:1x→11:37: capa limpa + submenus destravados (commit d2c89c3)

- **Lição técnica 🔴 (arquivar): dropdown `position:absolute` DENTRO de ancestral com `overflow-x:auto` é CORTADO também na vertical (o browser computa overflow-y=auto) — parece "menu não abre". Os 3 botões grandes do leitor saíram da `reader-row-scroll`; header = grid-template-areas `left big right`; ≤760px = 2 linhas (`"left right" / "big big"`).**
- `Reader.tsx`: bloco reader-big-group recortado do interior do scroll (python por âncoras; indent normalizado 12→8). `globals.css`: `.reader-row-main` 3 colunas; `.reader-row-scroll{grid-area:left}`, big=big, right=right; `.zoom-rail{top:132px}` no mobile (era 64 e o header 2-linhas cobria, z-100 > z-90).
- `Capa.tsx`: TopNav inteiro removido + imports limpos (TopNav/ZeMocaAvatar/Telemetry/Mural/AuthGate/LangSwitcher/useRouter). Botões: `<span class="capa-launch-ico">📖</span><b>nome</b><span>desc</span>` — sem classe `settings` especial (tamanho único); CSS: grid 3 colunas (mobile 2), radius 20, sombra 0 3px 12px, hover translateY(-3px)+sombra maior, ícone 34px.
- Provas curl pós-deploy: topnav=0 na capa; 6 ocorrências de capa-launch-ico; 0 classe settings dupla.
- Prompt AGY (`PROMPT_AGY_CHECAGEM_MOKA_20260831.md`) revisado: capa = exceção limpa no item 1, item 4 pede teste no celular + zoom-rail visível, item 8 redesenhado.


---

## 🔧 ADENDO 10 — 31/08 11:45→12:15: chip LLM + ajuda/tutorial (328bce3, fd9d8b2)

- `components/LlmChip.tsx` (novo): loadConfigCache→getEntryForText→PRESETS.find(providerId).name; chip `.llm-chip` (accent-soft) / `.none` (vermelho); router.push("/configuracoes"). Inserido no harness-hero e no writer hero.
- `app/memoria/page.tsx`: Link harness-link removido (import Link ficou órfão mas inofensivo — sem noUnusedLocals).
- `app/ajuda/page.tsx`: FAQ_PT/FAQ_EN +3 entradas cada (menu leitor/nuvem/pdf lento).
- `app/tutorial/page.tsx`: steps +{n:"6", extra:[tut_s6_d2]}; render já suportava extra/link/providers.
- i18n: +7 chaves (llm_on/llm_none/llm_change/reader_home_title/tut_s6_t/tut_s6_d/tut_s6_d2) ×12 + union. Reader brand title agora t().
- 🔴 LIÇÃO Vercel: deploy pode não propagar (chunk antigo na CDN mesmo com commit no GitHub); query string NÃO burla cache de rota estática; prova correta = baixar o chunk JS da página e grep; cura = commit vazio pra redisparar build.


---

## 🔧 ADENDO 12 — 31/08 12:4x→13:0x: memória → estante (4eb7882)

- `app/memoria/page.tsx`: `livroParaEstante(obj)` — split `^## ` → chapters `{id, title, blocks:[{id,type:"paragraph",text}]}`; ParsedBook EXIGE `metadata` (errou 1× no build); `sourceFormat: "txt"` (union epub|pdf|txt); capa `generateDynamicBookCover`; `saveToLibrary(session)` sem userId (local); botão no `.memoria-card-actions` só quando `obj.type === "livro"`; estado shelfBusy por id.
- i18n: +3 chaves (mem_to_shelf/_ok/_shelf_empty) ×12; `cloud_provider_s3` reescrito ×12 ("Outro — S3 compatível").
- Prova: chunk JS app/memoria/page-a5a0f7d8a8c7c7ab.js contém mem_to_shelf; rota 200.


---

## 🎯 ADENDO 13 — 31/08 12:5x→13:2x: estante só com original (983ec62)

- 🔴 REGRA DE OURO (arquivar): estante = ARQUIVO ORIGINAL (pdf/epub); memória = texto. O botão "📖 Pra estente" do adendo 12 foi REMOVIDO (era texto reconstruído) — decisão do produto do Miguel.
- `lib/db.ts`: `epubSource?: Uint8Array | null`. `estante/page.tsx` ingestBook: guarda `epubSource` no novo livro e no re-upload.
- `lib/cloud-s3.ts`: body `string | Uint8Array` (cast `as BodyInit` — TS novo reclama de Uint8Array genérico); content-type octet-stream p/ bytes; `cloudPutBytes/cloudGetBytes/cloudList(prefix)` (regex `<Contents>`, key+size).
- Estante page: `shelfCloudSave` (getBook pega originais; PUT .bin + .json; conta sem-original/falhas) / `shelfCloudRestore` (cloudList → GET json+bin → `parseBook(bin.slice().buffer)` → Session id novo se já existe → saveToLibrary(auth.userId) → recarrega). Botões .cloud-btn no shelf-actions; `.shelf-cloud-msg` role=status.
- i18n: 7 chaves shelf_cloud_* ×12. FAQ PT/EN reescrita. Provas: chunk estante page-271b753d contém shelfCloudSave+moka-estante; chunk memória sem livroParaEstante.


---

## 🔐 ADENDO 15 — 31/08 13:25→13:50: teste da credencial R2 do Miguel (7fdb3b4)

- Cofre: R2_MIGUEL_* nos 3 cofres + backups; sha8 AK 486accc5 / SK 0aad5c03 / cfat ddc61e37. Account ID CORRETO: termina d4c0 (1ª leitura da visão invertera p/ f4dc — 🔴 lição: transcrever IDs caractere a caractere ou pedir confirmação; TLS handshake failure em subdomínio inexistente é a assinatura disso).
- Provas: rclone ListObjects bookstore-moka 200 / moka-estante 403 (escopo do token); preflight CORS moka-estante 204 c/ Allow-Origin correto.
- Fixes: estante vazia ganhou ⬇️ Restaurar (.shelf-cloud-empty, fragmento <> no ternário — swc "Unexpected token main" = filhos múltiplos em branch sem container); ☁️ Salvar clica-e-avisa (shelf_empty_for_cloud ×12); CloudSettings input name="moka-cloud-host-off" anti-autofill.
- Conta R2 usada = a da casa (bookstore/cafezinho no mesmo lsd) — anotado.


---

## 🔧 ADENDO 18 — 31/08 13:55→14:1x: 403-que-parece-rede + cola mágica (07568ca)

- 🔴 LIÇÃO R2: resposta 403 AccessDenied vem SEM Access-Control-Allow-* → fetch do browser lança TypeError → indistinguível de CORS/rede. Diagnóstico real = testar fora do browser (rclone) OU checar escopo do token.
- Roll (rotacionar) troca secret mas MANTÉM buckets do escopo — só Create novo com All buckets resolve.
- Cola mágica em CloudSettings: regex `https://<32hex>.r2.cloudflarestorage.com` (provider+host), `<64hex>` (SK), `<32hex> != accountId` (AK). textarea .cloud-magic dashed accent. Cuidado: account id e access key são AMBOS 32 hex — distinguir por exclusão.
- cloud_test_net reescrito ×12 (3 causas). Commit 07568ca no ar (chunk confere cloud_magic).
