# ☕ Fórum Moka Reader — 2026-07-20 — Sprint "Páginas + Perguntas" (V 1.1)

> Tema: retomada do projeto Moka Reader no ZCode (Kimi) com o Miguel.
> Nodo de índice (Camada 2): `CEREBRO_INDEX_MOKA_LOG.md`.
> Governança: este é o Fórum (decisões resumidas). Detalhes técnicos no nodo e nos arquivos citados.

## Contexto
Projeto mora em `~/Downloads/Antigravity Google/Outros/Aplicativos/Moka/` (Lab / Producao / Backup).
Autenticação verificada no início da sessão: **GitHub CLI** e **Vercel CLI** ativas como `migueldorosario1` — nenhuma credencial precisou ser recuperada, apenas confirmada (localizações indexadas no nodo, sem valores).

## Pedidos do Miguel (voz→texto, sessão anterior + esta)
1. EPUB vindo "corrido", sem quebra de páginas → tem que paginar.
2. Novo ícone **microfone+caneta**: "perguntar qualquer coisa" sobre o livro, por voz ou escrita, abrindo uma janelinha com introdução convidativa e link de pesquisa.
3. **Confirmação** nos botões de ação (foto, ouvir, microfone, traduzir/explicar página) — e tradução sempre da **página na tela**, nunca do livro inteiro.
4. Ícone de **resumo**: da página ou do livro inteiro, com aviso de gasto de tokens.
5. **Backup antes de deploy**: sobretudo do **modelo deployado funcional**, pra garantir rollback. Zips datados em `Moka-Backup/`.
6. **Versionamento**: modelo no ar = **Moka V 1.0**; versão nova = **Moka V 1.1**.
7. **Indexar tudo no Cérebro**: diretórios, credenciais (localização, não valores), fóruns, log de trabalho.

## Decisões e entregas (V 1.1 — build ✓, rotas 200 ✓)
- **Paginação EPUB**: `paginateBlocks()` no `Reader.tsx` (~2200 chars/página, cortes em fim de frase; heading e page-break abrem página nova). Navegação, slider, contador e progresso passaram a ser por **página global**.
- **AskModal**: janela "❓ Pergunte qualquer coisa" (voz via SpeechRecognition + texto; streaming; chips de sugestão; link web; auto-save em notas). Ícone SVG microfone+caneta. Funciona em fullscreen.
- **SummaryModal**: resumo da página ou do livro (compilação ~12k chars) com aviso de tokens; auto-save tipo `summary`.
- **Confirmações**: 📸 com confirmação; 🌐/🧠 habilitados pra EPUB (sempre só a página visível).
- **i18n**: 18 chaves × 12 idiomas.
- **Backups**: `moka_V1.0_producao_DEPLOYADO_2026-07-20_1017.zip` (rollback) + `moka_V1.1_lab_2026-07-20_1013.zip` + `MANIFESTO_ROLLBACK.md` (como rodar `vercel promote`).

## Pendências
- Patch de redesign do Claude (11 arquivos) não aplicado — decisão do Miguel.
- Deploy da V 1.1 (só após OK do Miguel; backup V1.0 já garantido).
- Persistir página local do EPUB na sessão.
- Git dedicado pro Moka (hoje vive no monorepo do Downloads).
- Fase 2 (RAG) segue aberta no ROADMAP.

## Update 2026-07-20 (tarde) — Deploy homologação + hotfix GPT-5
- **V 1.1 deployada em homologação:** https://moka-lab.vercel.app (projeto Vercel `moka-lab`). Decisão Miguel: testar lá ANTES de promover ao mokareader.com. Mapa de projetos indexado no `CEREBRO_INDEX_MOKA_LOG.md` §3.
- **Caso de teste real (Cape Fear):** EPUB de 2 HTMLs gigantes (133k+160k chars) que a V 1.0 mostrava como "4 páginas" corridas → V 1.1 pagina em **149 páginas** (simulação via `/tmp/simula-paginacao.js`).
- **Hotfix GPT-5 (erro reportado pelo Miguel):** `400 Unsupported parameter: 'max_tokens'` ao configurar OpenAI GPT-5. Causa: família nova da OpenAI exige `max_completion_tokens` e rejeita `temperature` customizada. Correção em `packages/ai-providers/src/providers/openaiCompatible.ts`: nova detecção `isNewOpenAiModel()` (gpt-5*, o1, o3, o4*) — manda `max_completion_tokens` e omite `temperature` nesses modelos, em `complete()` e `stream()`. Outros provedores (Z.ai, DeepSeek) seguem no contrato antigo. Build ✓, redeploy em moka-lab.vercel.app ✓.

## Update 2026-07-20 (11:30) — V 1.1 EM PRODUÇÃO + gpt-5.5 validado
- **Miguel autorizou testar direto em produção** (app em fase de teste), desde que o backup do modelo no ar seja feito ANTES de cada deploy. Política registrada no `MANIFESTO_ROLLBACK.md`.
- V 1.1 deployada em **www.mokareader.com** (projeto `moka`; pasta `Moka-Producao` re-linkada de `igot` → `moka`). Health check: 3× HTTP 200 (~0,3-0,6s), /ajuda e /premium 200, /api/proxy viva.
- **Erro gpt-5.5 persistia** porque o Miguel testava em `moka-phi.vercel.app` — verificado que é ALIAS do mesmo deployment do mokareader.com (build idêntico); o erro era de antes do deploy da correção.
- **Chave OpenAI do Miguel testada direto na API** (a pedido dele): `gpt-5.5` (= `gpt-5.5-2026-04-23`) funciona com `max_completion_tokens`; com `max_tokens` reproduz o 400. ⚠️ A chave foi colada no chat — Miguel vai ROTACIONAR depois. Chave NÃO registrada em arquivo/Cérebro.
- Ajuste fino: `testConnection` subiu de 16→100 maxTokens (gpt-5.5 gasta reasoning_tokens e devolvia resposta vazia). Teste final direto na API: responde "OK" ✓.
- Novo backup `moka_V1.1_producao_DEPLOYADO_2026-07-20_1130.zip` + rollback points atualizados no manifesto (`moka-igbzp86vb` = V1.1 anterior, `moka-l3s8fehyh` = V1.0).

## Update 2026-07-20 (11:50) — V 1.2: TTS com barra de preparação + traduz-antes-de-falar
Pedidos do Miguel (recursos que ele já tinha configurado e se perderam):
1. **Barra de preparação do áudio em destaque** — não só o ⏳ no ícone. Implementado `.tts-prep-bar`: pílula flutuante no topo do reader com ícone 🔊, label de etapa ("Traduzindo o trecho pra falar…" / "Preparando áudio…"), barra animada indeterminada, cronômetro em segundos e botão ✕ cancelar (com generation-ref pra abortar de verdade).
2. **Traduzir ANTES de falar** — se o idioma da fala (⚙️ áudio) difere do idioma do texto, a IA traduz primeiro na nuvem e fala a tradução (ex.: livro em inglês → fala em português). "Original" fala no idioma do texto. Nova função `translateForSpeech(text, lang, ctx)` no ai-client (traduz pra idioma EXPLÍCITO, não o targetLang). Aplicado no `readPageAloud` (página) e no `fireSpeak` (trecho selecionado); respeita o texto da tradução visível na tela quando é o que está sendo lido.
- Nova chave i18n `reader_tts_translating` × 12 idiomas. Build ✓. Backup pré-deploy: `moka_V1.1.1_producao_DEPLOYADO_2026-07-20_1148.zip`. Deploy: `moka-dfhlegkiw-…` → www.mokareader.com (3× HTTP 200 ✓).
- Fluxo acordado: pedidos do Miguel são executados e deployados na hora; deploy importante = backup datado antes.

## Update 2026-07-20 (12:45) — V 1.3: REPO GITHUB vira fonte canônica + merge das features
**Causa raiz das "regressões" que o Miguel viu (menu de seleção atrás do nativo, menu superior, fonte):** o repo GitHub `migueldorosario1/moka` tinha ~40 commits de fixes de 19/07 (menu seleção no rodapé em touch, Highlight API, redesign Claude mergeado, balão de áudio, dicas iniciais, AIPanel expansível) que a pasta Moka-Lab NÃO tinha — a pasta era snapshot antigo. Ao deployar da pasta (V1.2), cobrimos o código mais novo do repo.

**Solução aplicada (merge no repo, branch `feat/v1.3-paginacao-perguntas` → main, commit `48b1b3a`):**
- Portadas as features da sessão pra CIMA do código do repo: paginação EPUB, AskModal, SummaryModal, confirmação foto, 🌐/🧠 pra EPUB (página visível), fix GPT-5, translateForSpeech (idioma EXPLÍCITO da fala — o repo traduzia pro targetLang errado), balão TTS com 2 etapas + cronômetro + cancelar.
- **Novo:** controle de tamanho da fonte A−/A+ (o "chavezinho" que o Miguel pediu — persiste no aparelho).
- i18n: 21 chaves × 12 idiomas. Build ✓. Push → auto-deploy `moka-6kf11jgmu` → www.mokareader.com (3× 200 ✓).
- **Moka-Lab agora é CLONE GIT do repo** (fim do problema "pastas sem git / código divergente"). Backup pré-deploy: `moka_V1.2_producao_DEPLOYADO_2026-07-20_1237.zip`. Manifesto atualizado: rollback = `vercel promote moka-dfhlegkiw` ou `git revert`.

**Lição registrada:** NUNCA mais deployar de pasta solta — sempre do repo git (fonte única da verdade).

## Update 2026-07-20 (13:00) — Sistema de manifestos + diretório central de backups
A pedido do Miguel ("manifesto central + diários/temáticos", "nenhum arquivo pode se perder", "backups fora das pastas de produção"):
- **`Moka/manifestos/MANIFESTO_INDEX.md`** — índice central do app: mapa de diretórios, fluxo canônico, linha do tempo de versões (V1.0→V1.3), links.
- **`Moka/manifestos/diarios/2026-07-20.md`** — primeiro diário (toda a sessão).
- **`Moka/manifestos/tematicos/PROTOCOLO_SEGURANCA_BACKUP.md`** — protocolos P1–P6: backup pré-deploy, rollback anotado, repo git como fonte única, rastro em manifestos, nada se apaga, health check pós-deploy.
- **`Moka/backups/`** — diretório central criado; zips + MANIFESTO_ROLLBACK.md movidos de `Moka-Backup/` (que vira legado preservado).
- Nodo `CEREBRO_INDEX_MOKA_LOG.md` atualizado com a nova estrutura.

## Update 2026-07-20 (13:30) — Moka 1.3 (fix bandeja) + backup oficial + estudo app mobile
- **Miguel batizou a versão estável: "Moka 1.2 OFICIAL"** (= commit `48b1b3a`). Backup: `backups/moka_1.2_OFICIAL_2026-07-20_1255.zip`. Mapeamento de versões registrado no MANIFESTO_INDEX.
- **Moka 1.3** (commit `6f9dcab`): fix da bandeja de navegação cobrindo o texto — padding inferior do scroll 70px → 110px + safe-area. Lê a página até o fim. ⚠️ Auto-deploy via webhook falhou pro commit (investigar); deploy via fallback CLI (`moka-jj01eey8e`). 3× 200 ✓.
- **Estudo de conversão pra app** (pedido do Miguel: Android, iPhone, Xiaomi, todos os iPads): `Moka/manifestos/tematicos/CONVERSAO_APP_MOBILE.md`. Resumo: Capacitor, modalidade "shell vivo" primeiro; Xiaomi = Android (mesmo APK); iOS = 1 app universal iPhone+iPad mas precisa macOS/CI + Apple Developer US$99/ano; keystore Android = risco #1 (backup no cofre). Decisões pendentes do Miguel no §7 do estudo.
