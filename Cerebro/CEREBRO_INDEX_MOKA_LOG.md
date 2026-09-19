# 🧠 Cerebro: Índice Mestre — Moka Reader (igot)

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.

Índice principal do **Moka Reader** (nome de pacote: `igot`) — leitor de e-books com IA integrada (tradução + explicação contextualizadas). Criado em 2026-07-20 a pedido do Miguel para indexar diretórios, credenciais (localização, nunca valores), fóruns e o log de trabalho.

---

## 0. Ficha Viva Obrigatória — Arquitetura Real do Moka

Consultar antes de qualquer diagnóstico, deploy ou nova sprint do Moka.

> ⚠️ **ATUALIZAÇÃO 31/08/2026 (ZM):** a OBRA ATIVA do Moka hoje é o repo `~/ZCodeProject/moka-app` (branch `obra/memoria`; laboratório moka-ousadia.vercel.app; rito Ousadia→Espelho→Canônico). A tabela de diretórios abaixo descreve a estrutura LEGADA de julho — ver `CEREBRO_INDEX_MOKA_MASTER.md` e `Foruns/forum_obra_moka_chefia_zm_20260830.md` (adendos 6-23) para o estado atual.

### Resumo Curto
Moka é um **leitor de EPUB/PDF com IA** (BYOK — a chave da IA fica no dispositivo do usuário, AES-GCM/localStorage). Stack: **Next.js (App Router) + TypeScript, monorepo npm workspaces, Supabase (sync opcional) + IndexedDB (local-first)**. Publicação canônica: **GitHub → Vercel**.

### Diretórios (máquina local `novo`)
Base: `/home/migueldorosario/Downloads/Antigravity Google/Outros/Aplicativos/Moka/`

| Pasta | Papel | Vercel link |
|---|---|---|
| `Moka-Lab/` | **Clone git canônico** do repo `migueldorosario1/moka` (main) — é aqui que se coda | projeto `moka-lab` (homologação) |
| `Moka-Producao/` | Espelho de deploy manual do repo (tem `vercel.json`) | projeto `moka` → **www.mokareader.com** |
| `backups/` | 🛡️ **Backups datados + MANIFESTO_ROLLBACK.md** (diretório central, fora das pastas de produção) | — |
| `manifestos/` | 📜 MANIFESTO_INDEX + diários + temáticos (protocolos de segurança) | — |
| `Moka-Backup/` | 📦 LEGADO (snapshot jul/18) — preservado, não usar pra código novo | projeto antigo `prj_tQvKNdIcLQlZJOh2knQbEzVJ5uGm` |

OrgId Vercel (time): `team_QQzbgQTC569AoQxaur7tNLGj`.

⚠️ ~~Pendência estrutural~~ **RESOLVIDO 2026-07-20 12:45:** a pasta `Moka-Lab` agora é **clone git** do repo `migueldorosario1/moka` (branch `main`) — a fonte canônica do código. Deploys fluem por `git push` → auto-deploy Vercel (projeto `moka`). **Regra: nunca mais deployar de pasta solta sem git.**

### Estrutura do monorepo
- `apps/web/` — app Next.js (UI: Reader, AIPanel, AskModal, SummaryModal, Uploader, Settings)
- `packages/parser/` — parsers EPUB (JSZip + DOMParser) e PDF (pdfjs)
- `packages/ai-providers/` — camada multi-provedor plugável (Z.ai/GLM padrão, OpenAI, Anthropic, Gemini…)
- `apps/web/src/lib/` — ai-client (prompts/streaming), config, crypto, db (IndexedDB), repository (sync Supabase), ui-strings (i18n, **12 idiomas**)

### Credenciais e autenticação (ONDE estão — NUNCA valores aqui)
**Regra:** este índice aponta localizações. Segredos não são copiados para o Cérebro (repo `cerebro-miguel` é "sem credenciais"). Cofre canônico de chaves: `CEREBRO_NODE_COFRE_CHAVES.md`.

- **GitHub CLI (`gh`):** logado como `migueldorosario1`, token no **keyring do SO**, protocolo SSH, escopos `repo`/`workflow`. Verificar: `gh auth status`.
- **Vercel CLI:** logado como `migueldorosario1`, auth em `~/.local/share/com.vercel.cli/auth.json`. Verificar: `vercel whoami`.
- **Chaves de IA dos usuários do app:** ficam no navegador do próprio usuário (localStorage encriptado) — não passam pelo servidor.
- **Repos GitHub do projeto:** `migueldorosario1/moka` e `migueldorosario1/igot`.

---

## 1. Fluxo de trabalho canônico

1. Codar em `Moka-Lab` → `npx tsc --noEmit` + `npx next build` verdes.
2. **Backup ANTES de deploy** (ver §3) — regra permanente do Miguel (2026-07-20).
3. Deploy: Vercel (projeto `igot`) a partir de `Moka-Producao` ou `vercel` CLI no Lab.
4. Registrar o trabalho no fórum do dia (`Foruns/forum_moka_reader_*.md`) e atualizar este nodo.

## 2. Roadmap (fonte: `Moka-Lab/ROADMAP.md`)
- **Fase 0/1 ✅** — scaffolding, MVP leitor+IA (EPUB/PDF, traduzir/explicar trecho e página, TTS, sync híbrida).
- **Fase 2 ⚙️ em andamento** — RAG: ingestão de livros inteiros (chunks→embeddings→vetorial), chat Q&A por livro, resumos por capítulo, mapas de personagens.
- **Fase 3/4** — leitura bilíngue interlinear, flashcards; empacotamento Capacitor (lojas).
- **💡 Ideia aprovada (2026-07-21, backlog)** — **Tradução Integral em Volumes**: ícone "traduzir livro inteiro" → volumes de ~50 páginas, EPUB/PDF por volume, integrador de volumes no app. Fórum: `Foruns/forum_moka_traducao_livro_volumes_20260721.md`. Memória técnica: `Memorias/memoria_moka_traducao_volumes_20260721.md`.
- **💡 Ideia em discussão (2026-07-22, backlog)** — **Moka Premium** (plano pago): assinatura com IA unificada — servidor segura 1 chave de gateway (OpenRouter → 100+ modelos) e o usuário usa sem BYOK; modo grátis BYOK convive. **Vercel AI SDK avaliado e descartado** (a camada multi-provedor já existe em `packages/ai-providers/`). Fórum: `Foruns/forum_moka_premium_20260722.md`. Memória técnica: `Memorias/memoria_moka_premium_20260722.md`.

## 3. Política de backup e rollback (permanente)
**Regra do Miguel (2026-07-20):** NENHUM ARQUIVO PODE SE PERDER. Antes de todo deploy, zip datado do **modelo que está no ar** em `Moka/backups/` (diretório central — fora das pastas de produção). Protocolo completo (P1–P6): `Moka/manifestos/tematicos/PROTOCOLO_SEGURANCA_BACKUP.md`. Rastro de tudo: `Moka/manifestos/MANIFESTO_INDEX.md` + diários.

- **Fonte canônica:** repo git (§0). Deploy = `git push origin main`.
- **Rollback:** `vercel promote <deployment-bom>` (rápido) ou `git revert`+push (estrutural) ou unzip do backup (desastre).
- **Manifesto canônico de rollback:** `Moka/backups/MANIFESTO_ROLLBACK.md`.
- **V 1.4 no ar** (commit `6390121`, deployment `moka-keioxuga0`). Versionamento: V 1.0 (base) → V 1.1 (paginação/perguntas/resumo) → V 1.1.1 (GPT-5) → V 1.2 (TTS) → V 1.3 (merge no repo + fonte A−/A+; 1.3.1–1.3.9 fixes de seleção/zoom/imagens) → **V 1.4 (tradução integral em volumes 🌍 + escritor EPUB + integrador)**.

## 4. Log de trabalho

### 2026-07-20 — Sprint "Páginas + Perguntas" (ZCode/Kimi, com Miguel)
Pedidos do Miguel (voz→texto): EPUB vindo "corrido" sem quebra de páginas; novo ícone microfone+caneta pra "perguntar qualquer coisa"; confirmação nos botões de ação; resumo da página ou do livro inteiro com aviso de tokens.

**Entregue (build ✓, rotas 200 ✓):**
- **Paginação de EPUB** — `Reader.tsx`: `paginateBlocks()` quebra capítulos em páginas de ~2200 chars (corte em fim de frase, heading abre página nova, respeita page-break). Slider/contador/progresso agora são por **página global**; swipe e setas andam página a página.
- **AskModal** (`components/AskModal.tsx`) — janela "❓ Pergunte qualquer coisa": intro convidativa, chips de sugestão, pergunta por **voz** (useSpeechRecognition) ou **escrita**, resposta com streaming, link de pesquisa web, auto-save em notas. Ícone novo: SVG microfone+caneta. Funciona em fullscreen.
- **SummaryModal** (`components/SummaryModal.tsx`) — resumo da **página na tela** ou do **livro inteiro** (compilação de ~12k chars com aviso "mais páginas = mais tokens"). Auto-save como nota tipo `summary`.
- **Confirmações** — 📸 foto agora pede confirmação; 🌐/🧠 traduzir/explicar página **habilitados pra EPUB** (sempre só a página na tela, nunca o livro inteiro); TTS/foto/print também operam na página visível.
- **ai-client** — novas funções `askStream` e `summarizeStream`; `NoteKind` ganhou `"summary"`.
- **i18n** — 18 chaves novas × 12 idiomas (pt-BR, en, es, fr, de, it, ru, zh, ja, ko, ar, hi) via script `/tmp/add-i18n-keys.js`.
- Traduções de página EPUB chaveadas por `cap.pag` (ex.: `2.4`) no mapa de traduções.

**Pendente:**
- Patch de redesign visual do Claude (`Moka-Lab/sugestoes claude/redesign-claude/moka-redesign.patch`, 11 arquivos) **não aplicado** — aguardando decisão.
- Persistir `pageIdx` local na sessão (hoje reabre no início do capítulo).
- Fase 2 (RAG) continua aberta.
- Resolver estrutura git dedicada (ver §0).

**✅ SMTP info@mokareader.com — RESOLVIDO 2026-08-06 ~14:35 BRT (sessão Ceará/Banco, Kimi K3):** credenciais no cofre local `Projeto Cafezinho Agentes/root/.env.unificado` — `SMTP_MOKA_USER`, `SMTP_MOKA_PASSWORD`, `SMTP_MOKA_HOST=smtpout.secureserver.net`, `SMTP_MOKA_PORT=465` (SSL; `smtp.office365.com` **não** funciona — não é M365). Login testado e e-mail real enviado ao Gmail do Miguel. Usado hoje pelo `agente_kimi_busca_imagem.py` (avisos de imagem). Livre para o app Moka (auth/recuperação etc.). Detalhes: CEREBRO_NODE_ATUALIZACOES 06/08 ~14:35.

Fórum do dia: `Foruns/forum_moka_reader_20260720.md`.

### 2026-07-21 — Ideia registrada: Tradução Integral em Volumes (ZCode/Kimi, com Miguel)
Miguel trouxe (voz→texto) a próxima grande feature do Moka: **ícone "traduzir livro inteiro"** na toolbar. Livros grandes são traduzidos **em volumes de ~50 páginas** ("de 50 em 50 é melhor"), cada volume virando um **arquivo EPUB/PDF separado**, e o app ganha um **integrador de volumes** para remontar o livro único. Registro completo:
- Fórum: `Foruns/forum_moka_traducao_livro_volumes_20260721.md`
- Memória técnica (especificação derivada + mapa de reuso no código V 1.3): `Memorias/memoria_moka_traducao_volumes_20260721.md`

Status: **backlog aprovado** — sprint de implementação a agendar com Miguel. Na mesma sessão nasceu a ideia do **Leitor de Vídeo** (2º produto Cafezinho): ver `CEREBRO_INDEX_LEITOR_VIDEO.md`.

### 2026-07-21 (18:00) — V 1.4 EM PRODUÇÃO: Tradução Integral em Volumes 🌍 entregue
Miguel autorizou a sprint na hora. Implementado, testado e deployado no mesmo dia:
- Ícone 🌍 na toolbar (EPUB) + janela com plano (páginas→volumes) e aviso de tokens.
- Motor por volumes com **retomada por página** (localStorage), cancelar/pausar, erro→continuar.
- **Escritor EPUB** novo no `@igot/parser` (EPUB 3 válido): cada volume = arquivo baixado + livro na estante.
- **Integrador de volumes** → livro único (EPUB + estante), fundindo capítulos cortados na fronteira.
- i18n 21 chaves × 12 idiomas. `tsc` ✓, `next build` ✓, teste funcional EPUB ✓.
- Commit `6390121` → deployment `moka-keioxuga0` → www.mokareader.com (200 ✓). Backups V1.4 lab+produção em `Moka/backups/`; rollback imediato = V 1.3.9.
- Pendências da feature: PDF de saída, volume configurável (25/50/100), idioma na hora, suporte a PDF de origem.

### 2026-07-22 — Ideia registrada: Moka Premium (plano pago com IA unificada)
Miguel perguntou se o **Vercel AI SDK** serviria para realizar a ideia: "a pessoa paga e usa vários LLMs com o preço de um, numa API só". Avaliação: **AI SDK descartado** (é só biblioteca de código; a camada multi-provedor já existe em `packages/ai-providers/`). A peça correta é um **gateway tipo OpenRouter** (1 chave → 100+ modelos, cobrança unificada). Arquitetura proposta: servidor segura a chave (env var Vercel), login Supabase, pagamento Stripe/Mercado Pago, cota por assinante; modo grátis BYOK convive. Registros:
- Fórum: `Foruns/forum_moka_premium_20260722.md`
- Memória técnica: `Memorias/memoria_moka_premium_20260722.md`

Status: **ideia em discussão** — nenhuma linha de código escrita; decisões pendentes (preço/tiers, Stripe vs MP, gateway).


### 2026-07-22 (01:50) — V 1.4.1: fix link de doação PayPal (ZCode/Kimi, report do Miguel)
Miguel reportou: "PayPal quebrado no link de doação nas configurações — a página desta organização está quebrada".
- **Causa:** o botão usava `hosted_button_id=<e-mail>` (inválido; hosted_button_id exige ID de botão hospedado criado no PayPal).
- **Cura:** `SettingsForm.tsx` → fluxo clássico `cmd=_donations&business=<email>&currency_code=BRL` (funciona sem botão hospedado; testado, página de doação abre).
- **Protocolo:** backup pré-deploy `Moka/backups/moka-lab_backup_pre_paypal_20260722.zip` ✅, tsc ✅, next build ✅, push `1117c88` → auto-deploy `moka-ks5diqmng` (Production, Ready) ✅, link novo confirmado no bundle em produção ✅.


### 2026-07-22 (05:30) — V 1.5: botão de Parar + timeouts anti-travamento (ZCode/Kimi, pedido do Miguel)
Miguel reportou travamento num livro maior ("fica lendo e não vai adiante") e pediu: "tem que ter um botão de parar, pra proteger o usuário".
- **`/book/[id]`:** após 6s de espera aparece **"✕ Parar e voltar pra estante"**; após 60s para sozinho com mensagem amigável + "↻ Tentar de novo" (antes: spinner infinito sem escapatória).
- **`PdfPageCanvas`:** watchdog de 30s no `loadDoc` do pdfjs — worker do **CDN (cdnjs)** lento/bloqueado ou PDF gigante/corrompido agora vira erro amigável (o CDN do worker é uma suspeita real do travamento original; fix estrutural futuro: servir o worker localmente).
- Backup pré-deploy `backups/moka-lab_backup_pre_stopbtn_20260722.zip` ✅, tsc ✅, build ✅, push `3d4c037` → auto-deploy.
- **Causa do travamento original:** não reproduzida (livro é local no navegador do Miguel). Se repetir com a V 1.5, o usuário escapa pelo botão Parar; investigação segue se houver recorrência (formato/tamanho do livro ajuda).


### 2026-07-22 (06:10) — V 1.6/1.6.1: motor do PDF embutido (fim da lentidão de abertura)
Sequência do caso "livro travou" (The great disruption, 13,9 MB, 372 págs, PDF texto):
- **Diagnóstico:** parse/render do livro em Node = instantâneo (getDocument 93ms). A demora NÃO era o livro: era o **worker do pdfjs (1,4 MB) vindo do CDN cdnjs** — na 1ª abertura, duas vezes (parser + PdfPageCanvas); se o CDN engasga, travava (o que o Miguel viu).
- **V 1.6:** worker local em `PdfPageCanvas` (`/pdf.worker.min.mjs`, cópia do pdfjs-dist 4.10.38). **V 1.6.1:** idem no `packages/parser` (parse ao adicionar). Zero dependência externa pra abrir PDF.
- Backups pré-deploy (`pre_workerlocal_20260722.zip`) ✅, builds ✅, pushes `739abe9`/`0f7a8d8` → produção (worker 200 ✅).
- **Regra pra futuro:** ao atualizar pdfjs-dist, re-copiar `build/pdf.worker.min.mjs` pra `apps/web/public/` (versões casadas).

---


> 💰 **Estratégia de monetização + unificação decidida (2026-07-22):** `Foruns/forum_moka_monetizacao_unificacao_20260722.md` + `Memorias/memoria_moka_monetizacao_unificacao_20260722.md` (PIX Mercado Pago + Paddle; só BYOK grátis; **FUSÃO JÁ FEITA em 22/07 (V 2.0)** — antes do previsto; ordem: i18n → confiança BYOK → página 3 níveis).

### 2026-08-05 — 🎬 MOKA 5.5: seção Vídeo & Transcrição própria nas Configurações (plano aprovado pelo Miguel)

Pedido Miguel: config de vídeo "colada com Quem somos", miúda e confusa; queria destaque, atalhos no topo, Quem somos no fim, respostas claras sobre Whisper/IP. **Fluxo plano→aprovação→implementação.** Entregue: seção `🎬 Vídeo & Transcrição` própria (fora do Quem somos, âncora `#video`, negrito) com 3.1 chave Whisper explicada ("OpenAI normal, nada especial; Groq mais barato"), 3.2 servidor próprio colapsável ("nada a ver com IP"), 3.3 IPRoyal 1 linha; quick-nav no topo (âncoras); Quem somos só o Sobre no fim; textos contextualizados livros×vídeos em **12 idiomas**. Commit `68063f5` (`moka/main`) — **AO VIVO** (chunk produção verificado). Fórum: `Foruns/forum_moka_video_config_reorg_20260805.md`. Memória: `Memorias/memoria_moka_video_config_reorg_20260805.md` (inclui mapa de ambiente: app em `ZCodeProject/igot`, mainline = `moka/main`, verificação de deploy por chunks).

### 2026-07-22 (13:30) — 🚀 MOKA 2.0: FUSÃO — um app só (Reader 📖 + Video 🎬)
Decisão do Miguel: juntar os dois produtos num único aplicativo já. Seção `/video` completa no Moka-Lab (portada do MokaVideo), seletor 📖/🎬 na topbar, SettingsForm unificado (seção 🎬: Whisper + servidor próprio), ingest yt-dlp+Whisper+LNA. Produção ✅ (`moka-pg5ort9mo`). Versão: **V 2.0**. Pendente: i18n da seção vídeo (sprint terreno). O MokaVideo standalone segue como motor local (localhost:3100).

---


> 🔬 **Pesquisa IA + investimento (2026-07-22):** `Memorias/memoria_moka_pesquisa_ia_fornecedores_20260722.md` + `Foruns/forum_moka_pesquisa_ia_investimento_20260722.md` — fornecedores por função, TTS, créditos startup, unit economics (R$ 11-22/assinante), veredito jurídico do modelo 200 sócios.


> 📊 **Plano de Negócios v1 (2026-07-22):** `Memorias/memoria_moka_plano_de_negocios_20260722.md` + fórum — custos calibrados, tiers R$ 19,90/44,90/89,90, metas, trial R$ 2, estratégia financeira, veredito Cripto Moca (não fazer; usar Pontos Moka).


> 📧 **Campanha Sócio-Fundador (2026-07-22):** `Memorias/memoria_moka_campanha_socios_20260722.md` — banco auditado (1.811 contatáveis), ondas em `Outros/banco de emails/campanha_moka_2026/`, minuta do e-mail, dinheiro fora do painel (Pontos Moka).


> ✉️ **E-mail do domínio (2026-07-22, em andamento):** `Memorias/memoria_moka_email_godaddy_20260722.md` + `Foruns/forum_moka_email_godaddy_20260722.md` — DNS (MX/SPF/DKIM GoDaddy) verificado ✅; falta criar a caixa no painel GoDaddy e testar.


> 💳 **Checkout R$5 Mercado Pago (2026-07-23):** `Foruns/forum_moka_checkout_mercadopago_20260723.md` + `Memorias/memoria_moka_checkout_mercadopago_20260723.md` — Pix R$5→100 pts ponta a ponta (12/12 testes E2E com MP mockado); falta só o `MP_ACCESS_TOKEN` do Miguel (placeholders em `.env.unificado`).

## 5. Links rápidos
- Código: `../Outros/Aplicativos/Moka/Moka-Lab/`
- Backups: `../Outros/Aplicativos/Moka/Moka-Backup/`
- Cofre de chaves (canônico): [CEREBRO_NODE_COFRE_CHAVES.md](./CEREBRO_NODE_COFRE_CHAVES.md)
- Índice master: [CEREBRO_INDEX_MASTER.md](./CEREBRO_INDEX_MASTER.md)

### 2026-07-23 (madrugada) — V 2.3 → V 2.3.2 (ZCode/Kimi, executado na conversa do livro por engano de canal)
Backup V1.0 (`f683400`) gravado. **V 2.3:** lupa de modelos destravada, matiz 🎬 sutil na seção vídeo, preços R$/US$ explícitos (`formatPlanPrice`), rótulos 🌐/🧠 "página inteira". **V 2.3.1:** causa raiz da lupa travada (handleEdit limpava a chave) — edição agora carrega do cofre via getConfigById. **V 2.3.2:** 🔊 "Ler em voz alta a página inteira" (12 idiomas). Tudo em produção (`1426acc`, `210e118`, `fdedbef`). Doc de continuidade: `Moka/SPRINT_V2.3_20260723.md`. **Backlog Miguel (V1.1):** Premium default sem API, código promo R$ 3/R$ 5, pontos, página investidores sofisticada.

### 2026-08-01 (tarde/noite) — 🎙️ MOKA 4.0: Transcrição da casa (Transkriptor) — qualquer vídeo, qualquer língua, SEM localhost
Decisões do Miguel na conversa: (1) **localhost banido** do app público; (2) o app **tem que transcrever qualquer vídeo em qualquer língua** (produto de assinatura); (3) usar o **Transkriptor que já tínhamos** em vez de proxy residencial. Investigação provou: IP do internauta é inviável (CORS testado: timedtext ✅, /watch ❌, youtubei ❌) e Transkriptor lê o YouTube nos servidores DELES (bloqueio de IP deixa de ser nosso). **Entregue (`1da872b`):** motor Transkriptor no `/api/ingest` (submit→202→polling "Ouvindo o vídeo… 🎧" com retomada), diarização `[SPK_N]:` nos segmentos, cache cross-usuário no SQLite da API de pontos (endpoints `/transcricao/job` novos, auth `x-moka-motor-key`), **pontos por faixa de duração** (15min=20/1h=45/3h=110 pts, ao vivo em `precos_acoes`), sonda localhost+LNA fora do app, mensagens 100% sem tecniquês. **E2E em produção:** vídeo do Miguel (46min, pt-BR, 4 falantes) via cache em 5,1s = 45 pts; "Me at the zoo" (19s, EN auto-detect) = 20 pts. Backups: `moka_V4.0_pre_transcricao_casa_2026-08-01.zip` + DB/app.py no servidor. **Tema Duplo:** `Foruns/forum_moka_video_transcricao_transkriptor_plano_v2_20260801.md` + `Memorias/memoria_moka_video_transcricao_transkriptor_plano_v2_20260801.md` (log técnico completo: endpoints medidos, trade-offs, débitos técnicos). Pendente Fase 2: X/Twitter/Instagram (motorzinho yt-dlp→S3), push 🔔, systemd unit pro uvicorn da API de pontos. **Também no dia:** fix rótulos 🌐/🧠 "Traduzir/Explicar página inteira" (`0b7b421`) + mensagens do vídeo sem tecniquês (`b72c225`) — bugs registrados em `CEREBRO_NODE_BUGS_RESOLVIDOS.md`.

### 2026-08-01 (noite) — 👁️ MOKA 4.1: fix do menu crônico + modal Anotar c/ slider + modelo da casa trocável
Três frentes a pedido do Miguel. **(1) FIX crônico "menu superior some":** causa-raiz dupla — botão de ocultar menu com ícone ☕ (a marca! usuário tocava sem querer) → agora 👁/🙈; botões de página 🌐 condicionais a `pdfSource` (sumiam em PDF) → sempre renderizados. **(2) Modal ANOTAR (📝) unificado:** Resumir OU Explicar num ícone só (antes 📝+🧠 redundantes) + **barra deslizante de tamanho** — resumo 5–50% das palavras da página (máx. metade, regra do Miguel), explicação 30–100%; livro mantido no resumo; streaming + auto-save; 12 idiomas (`pa_*`). **(3) Modelo da casa:** formalizado **deepseek-v4-flash como default de todo o sistema** (já era o default do gateway), agora **trocável pelo usuário nas ⚙️** (allowlist no gateway: flash ×1, pro ×4 pontos) com **info de tokens/ponto** (~90 mil vs ~8 mil); admin troca default via `MOKA_DEEPSEEK_MODEL`. Deploy gateway (multiplicador testado ao vivo: 30×1 e 20×4=80 pts ✅) + app `498c93d`. **Tema:** `Foruns/forum_moka_modelo_casa_deepseek_v4_flash_20260801.md`; bug do menu em `CEREBRO_NODE_BUGS_RESOLVIDOS.md`. Nota de arquitetura de API do Miguel (fila, rate limits, chave no backend, teto financeiro) registrada no fórum §6 pra fase futura do gateway.

### 2026-08-02 — 🪟 MOKA 4.1.1: janela Anotar vira POPUP flutuante (livro sempre inteiro)
Report do Miguel: a janela Resumir/Explicar "cortava quase metade inferior do livro" — era overlay de tela cheia com fundo escuro (herdado do SummaryModal). Fix (`677e25b`): popup flutuante **sem fundo escuro** (cliques passam pro livro) — desktop: card na lateral direita sobre a margem; celular: folha inferior compacta (máx. 58vh); **botão minimizar ➖** vira pilula no canto enquanto a IA trabalha ou durante a leitura. A página do livro fica inteira e brilhante o tempo todo. Registrado também no fórum 4.1 (`forum_moka_modelo_casa_deepseek_v4_flash_20260801.md` §5).

### 2026-08-02 (2) — 🪟 MOKA 4.1.2: janela Anotar não tapa o zoom + flexível
Report do Miguel: o popup cobria o controle de zoom (canto superior direito) e "não estava flexível". Fix (`6bddf4c`): encaixe padrão na lateral ESQUERDA (zoom livre), **arrastável pelo título** no desktop (pointer fine — posiciona onde quiser), **redimensionável pelo canto** (resize: both, mín. 300×220); celular segue folha inferior (não cobre o zoom). Regra viva da janela de IA: nunca cobrir controles do leitor (zoom, nav, menu).

### 2026-08-03 — 📖 MOKA 4.2: EPUB de calibre sem texto + PDF travado no PWA velho (dois bugs do Miguel, mesmos arquivos)
Miguel carregou "Trickster Makes This World" (OceanofPDF): EPUB "só veio algumas páginas" e PDF "carregando há vários minutos". **Bug A (EPUB, todo mundo):** parser só lia `<p>/<h>/<blockquote>` — calibre marca parágrafos como `<div><span><span>` (1 tag `<p>` no arquivo inteiro) → capítulos de texto descartados pelo filtro de "trivial"; sobravam ~12 páginas de imagem. Fix: elemento sem filho de bloco vira parágrafo agregado → **prova real no navegador com o arquivo do Miguel: 12→27 capítulos completos** (rota de teste temporária, removida depois). **Bug B (PDF, PWA instalado):** arquivo saudável e pipeline <1s — quem travava era o **service worker cacheando o próprio sw.js com cache-first** (armadilha clássica): o PWA nunca via a versão nova e ficava preso no código pré-22/07 (worker de PDF do CDN que engasga). Fix estrutural: bypass `sw.js` no fetch handler + `Cache-Control: no-cache` em /sw.js (2 vercel.json); presos se recuperam em ~24h e nunca mais. Commit `a248755`. Bugs: `CEREBRO_NODE_BUGS_RESOLVIDOS.md` (BUG-20260803-MOKA-EPUB-CALIBRE-SEM-TEXTO, BUG-20260803-MOKA-SW-CACHEIA-SI-MESMO-PWA-PRESA).

### 2026-08-04 — 🌐 MOKA 4.3: tradução de página EPUB invisível + espera explícita + failover da casa
Miguel: "cliquei no 🌐 do Confúcio, veio a ampulheta e não traduziu". TRÊS problemas empilhados, todos resolvidos (`8be6d63` + deploy gateway): **(1) UI:** em EPUB a tradução de página NUNCA era renderizada (só PDF tinha overlay) — o artigo agora troca pro texto traduzido; e a espera ficou explícita na área da página (spinner grande + "pode levar até 1 minuto", 12 idiomas, EPUB+PDF); erro "⚠️" agora permite RE-TENTAR (antes ficava preso como se fosse tradução salva). **(2) Chave morta:** a COFRE ÚNICO trocou a DEEPSEEK_API_KEY do .env da Tencent (válida, e41d) mas o uvicorn seguia com a velha (de04, inválida) — restart resolveu. **(3) deepseek-v4-flash MUDO na DeepSeek:** /models 200 mas /chat/completions pendurava >120s (pro responde ~1s; saldo $8,74 OK) → gateway ganhou **failover automático flash→pro** (auditoria marca "pro(failover de flash)", usuário paga o preço do modelo pedido) + **débito só no sucesso** (antes: debitava e a chamada falhava = ponto perdido — regra do Miguel "nunca cobrar por fracasso"). Teste ao vivo: 28s, ok, 20 pts, log correto. Bug registrado: BUG-20260804-MOKA-TRADUCAO-EPUB-NAO-APARECE.

### 2026-08-04 (2) — 🏢 D-U-N-S RECEBIDO: 943494728 (lojas desbloqueadas!)
No MESMO dia do pedido: Miguel fez a consulta+pedido no portal Apple (guiado campo a campo pelo ZCode com os dados EXATOS do cartão CNPJ — razão `MIGUEL G B DO ROSARIO SERVICOS DE INFORMACOES`, CNPJ 22.193.457/0001-00, EI 213-5, e-mail `comercial@ocafezinho.com` escolhido por ser o domínio do grupo) e a Apple Developer Relations respondeu com o número **943494728**. Guardado no COFRE (`MOKA_DUNS_NUMBER` no `.env.unificado` — nunca em fórum). Fórum de trabalho atualizado: `Foruns/forum_duns_moka_lojas_20260728.md` (checklist fechado + dossiê cadastral canônico). **Desbloqueia:** Play Console organização (US$ 25 — pula o teste de 20 testadores/14 dias) e Apple Developer organização (US$ 99/ano, publica como Cafezinho Media Group). Próximo: checklist das lojas do doc 16 (`PLANO_NEGOCIOS_MOKA/documentos/16_lojas_play_store_app_store.md`): assetlinks.json pro TWA, ícone 512, screenshots, Data Safety; iOS via Capacitor + build em nuvem.

### 2026-08-04 (3) — 🔀 PIVÔ ESTRATÉGICO: versão PAGA congelada → fase GRATUITA (BYOK) com doação
Decisão do Miguel: "a gente não vai poder começar com esse pago — fase experimental com tudo gratuito; numa segunda etapa cobra a taxa de uso". **BACKUP COMPLETO antes de mexer:** tag git `pre-pivot-pago-v4.3` (commit `8be6d63`) + zip app 9MB + `pontos_api_pre_pivot_20260804.tar.gz` (gateway + .env + SQLite) + backups no servidor + **MANIFESTO**: `Moka/backups/MANIFESTO_PRE_PIVOT_PAGO_V4.3_20260804.md` (estado pago itemizado, decisões da fase gratuita, aviso de segredos no tar.gz). **A fase gratuita (a implementar):** tudo grátis só BYOK (chave do usuário, privacidade BYOK enfatizada); fora preços/pontos/checkout/licença/seletor de modelo; **rodapé em todas as páginas (12 idiomas)** com doação (PayPal mundo / Pix Brasil) + info@mokareader.com + Quem Somos; help caprichado (como pegar a API key, custo estimado pra o usuário, e que **vídeo precisa de API de transcrição de áudio** — nem toda API serve); botão esquerdo do topo sempre volta pra capa. Fase 2 = reativar cobrança a partir deste backup/tag.

### 2026-08-04 (4) — 🆓 MOKA 5.0: FASE GRATUITA (tudo BYOK + doação) — versão paga congelada
Decisão do Miguel: adiar a cobrança — "fase experimental com tudo gratuito; numa segunda etapa cobra a taxa de uso". **Backup ANTES de mexer:** tag git `pre-pivot-pago-v4.3` + zips + gateway/.env/SQLite + `MANIFESTO_PRE_PIVOT_PAGO_V4.3_20260804.md`. **Implementado (`1076c67`, em produção ✅):** fora planos/pontos/checkout Pix/licença/seletor de modelo/ContaButton/gates 401-402; BYOK é O modo (SettingsForm abre na chave; ai-client sem fallback pro gateway — erro guia pra ⚙️); Transkriptor da casa DESLIGADO com flag `MOKA_CASA_TRANSCRICAO=1` pra Fase 2 (código intacto); vídeo sem legenda → mensagem honesta; **rodapé SiteFooter em todas as páginas públicas (12 idiomas)** com doação PayPal + Pix (⚠️→✅ **chave Pix decidida 07/08:** `info@mokareader.com` — entrada (14), 5.7.1 `a85007d`) + info@mokareader.com + Quem Somos; capa e /experimente reescritos; bloco BYOK (12L): chave segura no dispositivo, custo estimado pro usuário, e aviso "vídeo sem legenda precisa de API de transcrição de áudio". Gateway Tencent segue rodando intacto (só a UI parou de chamar — Fase 2 religa). **Tema:** `Foruns/forum_moka_fase_gratuita_byok_doacao_20260804.md`.

### 2026-08-05 — 🔐 MOKA 5.1: cadastro duplo (Google + e-mail) + biblioteca sem flash e com capas bonitas
Duas entregas do Miguel. **(1) Auth dupla** (`d4917e4`): AuthModal com Google OU e-mail+senha — criar conta por e-mail manda link de CONFIRMAÇÃO ("clica, chega, confirma"), "esqueci a senha" manda link → `/auth/atualizar-senha` (callback passou a honrar `?next=`); AuthGate substitui AuthButton na capa e no Reader; 16 chaves ×12 idiomas; e-mails dos cadastros caem em `auth.users` (Supabase) = lista de newsletter do Miguel. **(2) Biblioteca:** o "flash desconfigurado" era **CLS das capas sem dimensão** → moldura 2:3 fixa + placeholder + fade-in (verificado no navegador); e "livros feios" = as **capas neon do Project Gutenberg** (candide/quixote/dante/kafka) + SVG tosco (confúcio/maiakovsky) → **6 capas SVG elegantes desenhadas sob medida** (sol de Eldorado, moinho de La Mancha, 3 estrelas de Dante, cinza Kafka, laca chinesa 論, construtivismo russo); mantidas Casmurro (Garnier antiga) e Austen (pavão) — lindas. ⚠️ Pendência operacional: SMTP padrão do Supabase (limite baixo de e-mails de confirmação) — configurar SMTP próprio (GoDaddy info@mokareader.com) no dashboard quando o volume crescer.

### 2026-08-05 (2) — ⚡ MOKA 5.1.1: o flash da biblioteca era FOUC do styled-jsx (causa-raiz da classe)
Miguel confirmou: "ficou bonito mas o flash ainda está lá". A 5.1 matou metade do problema (CLS das capas sem dimensão); a outra metade era **FOUC de estilo**: na navegação client-side, o `<style jsx>` injeta DEPOIS do primeiro paint → página aparece sem estilo por um átimo. Fix (`31bd898`): `.bib-*` migrados pra `globals.css` (carrega com o layout raiz em qualquer navegação). **Dívida registrada:** o mesmo padrão styled-jsx existe em estante/video/sobre/ajuda/experimente/settings — o "probleminha que tem de vez em quando" do Miguel provavelmente é ESSA MESMA CLASSE em outras páginas; migrar na próxima leva.

### 2026-08-05 (3) — 🏆 MOKA 5.2: Ranking de Preços das IAs + limpeza da era paga no /ajuda e /premium
Miguel: "ainda tem páginas atrasadas com preço" (o robô do /ajuda respondia com pontos/R$/Pix/licença) + "faz um ranking de preços das LLMs, vai ficar simpático, e explica que vídeo é outro sistema". **(1) FAQ do /ajuda reescrito pra era gratuita** (grátis BYOK, custo estimado, chave segura, conta opcional, vídeo=áudio). **(2) 🏆 Ranking de Preços** (`components/LlmPriceRanking` + `lib/llm-prices.ts`): 12 modelos com preços do catálogo oficial do Cérebro (jul/2026), ordenados por custo de "resumir 1 livro" (15k in/1k out) + coluna "traduzir 1 livro inteiro" (150k tokens) — DeepSeek V4 Flash $0,0024 → Claude Opus $0,10; bloco separado de transcrição por hora (Groq $0,042/OpenAI mini $0,18/padrão $0,36); labels nos 12 idiomas; aparece no /ajuda e no /premium (que era a vitrine de assinatura — backup em /tmp/premium_assinatura_backup.tsx). Commit `68201e0`.

### 2026-08-05 (4) — 🏆 MOKA 5.3: ranking canônico unificado (Aiatolah News + Moka) + config de vídeo separada
Miguel: unificar o ranking entre os dois sites, atualizar as chinesas e os preços de tudo, e separar a config de vídeo da config do Reader. **(1) Aiatolah News** (`src/data/ranking.json`, commit `e8958d6`): 25 modelos revalidados contra o catálogo oficial do Cérebro — DeepSeek V4 Pro sai da promoção ($0.20/$0.80 → **$1.74/$3.48**), NOVO **DeepSeek V4 Flash $0.14/$0.28**, Kimi K2→K2.6 $0.95/$4.00 + NOVO Kimi K3 $3/$15, NOVOS GLM-4.7 $0.42/$1.68 e GLM-5.1 $1.40/$4.40, Qwen3 Max →$0.78/$3.90, Gemini 2.5 Flash →$0.30/$2.50, GPT-5 →$1.25/$10, Claude Opus →4.7 $5/$25; usd_brl 5.80→**5.55** (harmonizado com o Moka). **(2) Moka** (`lib/llm-prices.ts`, `c042a32`): MESMOS preços — **GLM-4 Flash ($0.07) novo #1**; entram Llama 3.3 (Together) e GLM-5.1 → 15 linhas. **(3) Config de vídeo separada** (⚙️, 12 idiomas): bloco "🎬 Vídeo — configuração de transcrição (diferente do texto)" — texto usa a chave do ranking, vídeo sem legenda é outro sistema (Whisper/OpenAI); link direto pra chave OpenAI + preço/hora (Groq $0,04/mini $0,18/padrão $0,36) + nota avançada **IPRoyal** (proxy residencial pra servidor próprio).

### 2026-08-05 (5) — 📚 MOKA 5.4: /tutorial — tutorial completo do usuário BYOK com a matemática do custo
Miguel: "tem que ter um tutorial bem legal para os usuários" com estimativa de quanto vai custar. Nova página **`/tutorial`** (12 idiomas, `9c18b43`): 5 passos — (1) escolher a IA no ranking; (2) pegar a chave com **links diretos de 8 provedores** (DeepSeek, Z.ai, OpenAI, Qwen, Kimi, Anthropic, Gemini, Groq) + dica "US$ 5 duram semanas"; (3) colar nas ⚙️ (criptografada, só no dispositivo); (4) **"Quanto vai custar? (a matemática)"** — o que é token + exemplos com DeepSeek V4 Flash (página <1 centavo, livro ~R$ 0,02/~R$ 0,15, vídeo ~R$ 0,01) e "premium multiplica ~40, continua centavos"; (5) acompanhar o gasto no painel do provedor + dica de ouro (ativar LIMITE de gasto). Nota vídeo (outro sistema, por hora). Capa: card BYOK agora aponta pro /tutorial.

### 2026-08-05 (6) — 💛 MOKA 5.4.1: convite de feedback no rodapé global ("Encontrou um bug? Fale com a gente")
Miguel: app experimental agradece opinião/críticas — em TODA parte, com íconezinho. Novo elemento no SiteFooter (presente em todas as páginas públicas): pilula amigável "🚧🐛 Moka experimental — achou um bug, tem um elogio ou uma crítica? Fale com a gente: seu feedback conserta o app. ☕💛" → mailto:info@mokareader.com com assunto pré-preenchido. 12 idiomas. Commit `dda5849`.

### 2026-08-05 (7) — 📱 MOKA 5.4.2: janela de login cortada no celular (botão Google inalcançável)
Miguel testando no celular: "a caixa de entrada cortado em cima e não tem o botão do Google, só tem e-mail e senha". Causa: o AuthModal usava overlay com centralização flex **sem altura máxima** — quando o conteúdo (título + botão Google + divisor + form + links) passa da altura do celular, o TOPO (o "Continuar com Google") fica cortado e inalcançável. Fix (`0fbb2e9`, após rebase sobre o `68063f5`/Moka 5.5 do Claude): overlay com `overflow-y: auto`; card com `margin: auto` (centraliza quando cabe, rola quando não cabe) + `max-height: calc(100dvh - 40px)` com fallback `100vh` + rolagem interna. Os demais modais (Settings/Ask/Summary/TranslateBook/VideoAsk) conferidos: já têm max-height + rolagem interna — sem a doença. NOTA de processo: o Moka 5.5 (`68063f5`, seção Video & Transcrição própria + atalhos no topo) veio de OUTRA SESSÃO KIMI K3 (branch auto-nomeada `claude/foragido-...` — o prefixo 'claude/' induz ao erro e NÃO é o agente Claude; correção registrada 05/08 a pedido do Miguel). Nasceu daí a seção `MONITORAMENTO_DE_TRABALHO.md` (quem faz o quê, pra evitar conflitos).

### 2026-08-05 (8) — 🧹 MOKA 5.5.1: Configurações SIMPLES + a correção do episódio "Claude" (era outra sessão Kimi)
Miguel: "configurações tá complicada, texto demais, tá exagerado". Simplificação (`5d87eae`): **(1)** título da seção virou **"Sua chave de IA"** (era "Configurações avançadas"); **(2)** novo bloco **"🗝 Três jeitos de usar"** (12 idiomas): texto = qualquer chave do ranking · **voz neural (ler em voz alta — livros E vídeos) = OpenAI** ("voz perfeita") · vídeo sem legenda = OpenAI (Whisper) — e a MESMA chave OpenAI cobre as duas; **(3)** FORA **"servidor próprio"** (Miguel: "não entendi o que é isso" — dormente em config.ts pra power users) + nota IPRoyal; **(4)** FORA as seções Ajuda e Quem somos do fim das configurações (vivem em /ajuda e /sobre + rodapé); **(5)** FORA **Moka Premium** (banner + ⭐ na estante; /premium redireciona pro /ajuda). **EPISÓDIO "CLAUDE":** Miguel questionou — a verdade: Moka 5.5 (`68063f5`) e o selo (`4033ba7`) vieram de **OUTRA sessão Kimi K3** (branch auto-nomeada `claude/foragido-...`; o prefixo "claude/" é da ferramenta, não o agente). Nasceu a seção **`MONITORAMENTO_DE_TRABALHO.md`** (criada hoje por ordem do Miguel: quem faz o quê, pra evitar conflitos — e já se pagou na 2ª colisão do dia, com rebase limpo).

### 2026-08-05 (9) — 🚪 MOKA 5.5.2: janela de login virava FAIXA CORTADA no topo ("probleminha meio grave")
Miguel (com print): "você clica lá para entrar… entrou uma página atrás, cortada, coisa bizarra". Causa: `position:fixed` do modal inline quebrado por ancestral com containing block (transform/filter/contain) — overlay cobria só uma tira. Cura (`b69a3a8`): **createPortal(document.body)** + guarda SSR + centrado à prova de corte (`align-items:flex-start` + `margin:6vh auto`). Padrão-irmão do BUG-20260801-MOKA-MENU-SUPERIOR-SOME: modal full-screen nunca inline. Bug completo: `BUG-20260805-MOKA-LOGIN-MODAL-FAIXA-CORTADA`. **Resposta registrada pro Miguel: login Google grava SIM a biblioteca** — EPUB sobe completo (texto parseado incluso, abre em outro aparelho sem o arquivo), PDF sobe metadados/progresso/notas/traduções (reanexa o arquivo no aparelho novo), videoteca é local.

### 2026-08-05 (10) — 🧹 MOKA 5.5.3: "Configurações avançadas" → "Configurações" (12 idiomas) + quicknav sem links mortos
Pedido direto do Miguel: "não bota configurações avançadas, bota configurações só". O atalho do topo ainda dizia "avançadas" e tinha 2 links quebrados (#ajuda/#quem-somos — as seções saíram na 5.5.1, os atalhos ficaram). Cura (`136eca8`): `nav_advanced` renomeado nos 12 idiomas + quicknav só com âncoras vivas (🔧 Configurações · 🎬 Vídeo); Ajuda = banner "❓ Tutorial completo" → /ajuda; Quem somos = rodapé global.

### 2026-08-05 (11) — 📣 MOKA 5.6: marketing GRATUITO sem "nesta fase" + tutorial abre com "O que é API?"
Miguel: "tira essa coisa de esta fase — bota: o Moka é grátis, é gratuito, você só tem que colocar a sua API, a API da sua inteligência artificial. E tem que ter um bom tutorial sobre o que é API." Cura (`48bcd60`): `free_title` ×12 sem "fase" ("Moka é gratuito ☕"…); /tutorial abre com cartão **"🔑 O que é essa tal de API?"** ×12 (API = ponte entre o Moka e a IA que você escolhe; chave = senha criada de graça no provedor; quem cobra é o provedor, centavos; o Moka é gratuito); /ajuda FAQ: 4 respostas sem "fase". Varredura: zero "fase" user-facing (só comentários internos — a memória do pivô fica no Cérebro, não no marketing).

### 2026-08-05 (12) — 🚪 MOKA 5.6.1: botão Entrar em TODAS as páginas
Miguel: "na página Moka Livros não tem o botão de entrar, mesma coisa na Moka Video — tem que ter esse botão de entrar, de login tem que estar em tudo". O AuthGate (Google + e-mail) só existia na capa e no Reader. Cura (`803007b`): AuthGate no topo de /estante, /video, /biblioteca, /ajuda, /tutorial e /sobre — sempre antes da bandeirinha de idiomas, mesma posição da capa.

### 2026-08-05 (13) — 🔐 MOKA 5.7: botão Entrar neutro (sem logo Google) + página "✅ E-mail confirmado"
Miguel testou o cadastro (tvcafezinho@gmail.com) e achou 2 problemas: **(1)** o botão do topo tinha logo do Google — "a pessoa pode entrar com e-mail normal, bota só Entrar; o Google fica dentro da janela" → AuthButton deslogado agora é neutro (`ba918da`). **(2)** clicar em "Confirmar acesso" no e-mail caía numa "página estranha com interrogação" (era a home, sem aviso) → signUp agora manda `next=/auth/confirmado`; nova página "✅ E-mail confirmado! Sua conta está ativa…" + botão "Entrar no Moka →" ×12; link expirado vira ?erro=1 com explicação amiga. **(3) Pendente SMTP:** e-mails de auth saem do remetente padrão Supabase (limite 2/hora) — meta: `info@mokareader.com` (GoDaddy, smtpout.secureserver.net:465). Faltam: senha do e-mail (não está no Cofre) + alguém colar no Supabase Dashboard → Authentication → Emails → SMTP. Guia entregue ao Miguel no chat. **↳ ERRATA 07/08 (Kimi K3):** senha RECEBIDA e SMTP **ATIVO desde 06/08 ~14:35** — credenciais `SMTP_MOKA_*` no cofre (`Projeto Cafezinho Agentes/root/.env.unificado`), login testado :465 SSL/:587 TLS, e-mail real enviado ao Gmail do Miguel (registro: CEREBRO_NODE_ATUALIZACOES 06/08 ~14:35). **Resta só 1 sub-passo: colar o SMTP no Supabase Dashboard** (ação do Miguel; agentes sem token admin Supabase). ⚠️ Senha trafegou no chat — recomendado trocar no GoDaddy por precaução.

### 2026-08-06 (noite) — 🎬 DECISÃO: motor de vídeo LONGO (+1h) na Central NYC + mapa dos 3 Moka + pontos_api no failover (ZCode/Kimi K3, ordens do Miguel)

**Contexto:** sessão "Mapa de Servidores/Central de Alertas/Droplet Utilitário". Miguel perguntou "o Moka Video não tem servidor próprio?" → depois: "vou querer processar vídeos de mais de uma hora, o Moka Video é pra isso mesmo, uma das funções principais é resumir vídeos de mais de uma hora. É melhor ser eu no Nova York... acho melhor usar Nova York, DigitalOcean, que não vai ter trava."

**Mapa dos 3 Moka (auditado e canonizado hoje):**
| Produto | Frontend | Backend | Servidor próprio? |
|---|---|---|---|
| **Reader** | Next.js→Vercel (repo `moka`, clone `Moka-Lab`) | `pontos_api` Python na **Tencent :8420** (compartilhada) | ❌ |
| **Video** | Next.js→Vercel (repo `moka-video`) | API routes serverless (`runtime nodejs`, `maxDuration 300`) | ❌ |
| **Writer** | Estático→Vercel (repo `mokawriter`) | 1 function (`api/kimi.js`) | ❌ |

**🔴 Descoberta crítica (lendo `route.ts` do moka-video):** na Vercel o Moka Video **só lê vídeos do YouTube COM legenda** (`SERVERLESS_NOTE`: "Para vídeos sem legenda (Whisper), X/Twitter e Instagram, rode o Moka Video local ou no servidor com yt-dlp"). O caminho Whisper está **desligado em serverless** por design. Ou seja: a função principal que o Miguel quer (resumir vídeo longo/sem legenda) **não funciona no site hoje** — só localhost.

**Contrato do `/api/ingest` mapeado (para o worker espelhar):**
- `step:"meta"` → yt-dlp `-j` → `meta{title, channel, durationSec, thumbnail, platform, description(≤1200), webpageUrl, uploadDate}` + `hasCaptions`
- `step:"transcript"` → 1) legendas oficiais/auto (grátis) → `{meta, transcriptSource:"captions", segments:[{start,end,text}]}`; 2) Whisper: áudio em chunks de **5 min** (`WHISPER_CHUNK_SEC=300` — chunks de 10min pulavam falas), modelos **`gpt-4o-transcribe`→`whisper-1`** (fallback), chave OpenAI **BYOK** via header `x-openai-key` (nunca persistida)
- IPRoyal já integrado (`src/lib/iproyal.ts`, `runYtDlp`, desde 03/08 — `MOKA_PROXY_MODE=off` desliga)

**Decisões (Miguel, 06/08):**
1. **Motor de vídeo longo roda na Central NYC 142.93.48.252** (droplet utilitário montado hoje — yt-dlp+IPRoyal provados ao vivo; ffmpeg 6.1 presente). Alibaba descartado (GFW trava YouTube no país todo). NYC "não tem trava".
2. **`pontos_api` (Tencent :8420) = dependência crítica** do Reader (auth/pontos/créditos) → obrigatório no plano de **failover NYC↔Tencent** (reconstrução = lembrete pendente do Miguel).

**Estado da missão (para retomar em qualquer conversa):**
- ✅ Contrato lido; central com ffmpeg/yt-dlp/IPRoyal operacionais; decisão registrada
- ⏳ **FALTA construir:** worker FastAPI na central — endpoint `POST /ingest` espelhando 1:1 o contrato acima (steps meta/transcript, captions→Whisper chunks 5min, `x-openai-key` BYOK repassada, auth `x-worker-key` cujo token fica no cofre local), systemd `moka-video-worker.service`, bind 0.0.0.0 com auth obrigatória
- ⏳ Testar com vídeo real +1h (candidato: entrevista longa do Lex Fridman)
- ⏳ SÓ DEPOIS, com prova: integrar `route.ts` do moka-video → delegar ao worker quando sem legenda/longo (commit no repo `moka-video` → auto-deploy Vercel). **Nada no Moka em produção foi alterado hoje.**
- 📋 Custo estimado de transcrição: whisper-1 ~$0,36/h de áudio (gpt-4o-transcribe mais caro, melhor qualidade); roadmap já tinha "migração p/ Groq whisper-turbo (-85%)" — o worker aceita os dois (Groq é OpenAI-compatible).

**Relacionados desta sessão:** `Foruns/forum_mapa_servidores_ecossistema_20260806.md` · `Foruns/forum_central_alertas_20260806.md` · `Foruns/forum_droplet_utilitario_20260806.md` (+ memórias irmãs) · `Memorias/manifesto_faxina_discos_20260806.md`.

### 2026-08-07 (14) — 💰 MOKA 5.7.1: chave Pix definida — `info@mokareader.com`
Miguel, sobre a chave `migueldorosario2@gmail.com` (hardcoded nas Configurações pela sessão anterior): "não, eu mudei o pix para info@mokareader.com". Cura (`a85007d`): `PIX_KEY`/`PIX_HOLDER` como fonte única em `lib/donate.ts`; SettingsForm importa (fim do hardcoded; linha "Banco: Nubank" saiu — banco da chave nova não confirmado); SiteFooter ganhou alerta de confirmação da cópia (antes silencioso) — o botão 🟢 PIX agora APARECE no rodapé global (antes escondido com chave vazia); /ajuda sem "Pix em breve". Verificado AO VIVO na home (HTTP 200 + botão presente). ⚠️ p/ sessão de lojas: o tapinha PIX_KEY já foi.

### 2026-08-07 — 🧠 CONSOLIDAÇÃO CÉREBRO (ordem expressa do Miguel: "grava tudo, a gente está perdendo comunicação")
Tema Duplo da sprint 5.5.2→5.7 criado: `Foruns/forum_moka_sprint_pos_pivot_552_57_20260805.md` + `Memorias/memoria_moka_sprint_pos_pivot_552_57_20260805.md`. Pontes novas: bloco ☕ Moka no topo do NODE_SPRINTS_ATIVOS + bloco "Onde o Moka parou" no INDICE_DESPERTAR_LEVE (qualquer conversa nova acorda orientada) + catalogação no INDICE_FORUNS_SEMANAL. Bloqueadores vivos (corrigido 07/08 ~13h): ① ~~SMTP~~ ✅ resolvido 06/08 pela sessão Ceará/Banco (`SMTP_MOKA_*` no cofre — confirmar uso no Supabase Dashboard) ② ~~Pix~~ ✅ 07/08 ~12h (info@mokareader.com, 5.7.1 `a85007d`) ③ reteste login ④ lojas: sessão irmã ativa 07/08 ~12:00 (contas US$25/US$99 + assets).

### 2026-08-07 — 📱 MOKA TWA ANDROID PRONTO PARA A PLAY STORE (5.7.1)
Sprint do deploy Android (aprovada "pode montar sim!"): TWA Bubblewrap `com.mokareader.app` (vc1/v5.7.1) — APK assinado + AAB de loja prontos em `Moka-Lab/apps/twa`; keystore nos dois cofres (`MOKA_TWA_KEYSTORE_PASSWORD`, Regra 4); `assetlinks.json` publicado e NO AR (HTTP 200, commit `8790c9a`); prova no emulador Android 34 em curso. **Falta:** conta Play Console organização (US$25, Miguel) + upload do AAB; iOS depois. Detalhes: `Foruns/forum_moka_twa_android_play_store_20260807.md` + `Memorias/memoria_moka_twa_android_play_store_20260807.md`.

### 2026-08-08 — 🧹 MOKA 1ª FASE PÚBLICA: correções de comunicação + deploy 09/08
Sessão GLM-5.2 (`f442edd`): Quem somos sem jargões, avatar Google fix, Sócios FORA da navegação (rota preservada p/ fase 2), rodapé sem "experimental" (12 idiomas), fix FOUC — **deployado só em 09/08** pela sessão Qwen 3.8 Max, que também reescreveu o convite de feedback com ELOGIO PRIMEIRO ("Tem um elogio? Uma sugestão? Uma crítica? Achou um bug? Fale com a gente.", commit `23f521d`, verificado ao vivo). Detalhes: `Foruns/forum_moka_primeira_fase_publica_correcoes_20260808.md` (+ adendo 09/08).

### 2026-08-09 — 📖 FIX: slider de páginas travava em "Carregando página…" (reporte do Miguel)
Corrida de renders no `PdfPageCanvas` (render zumbi no canvas compartilhado durante arrasto do slider → pdf.js "Cannot use the same canvas..." → spinner eterno). Cura em `000762e`: guarda de sequência anti-zumbi + clamp de página + retry de colisão + debounce 120ms no slider do Reader. Deploy no ar; teste real pendente com o Miguel. Bug: `BUG-20260809-MOKA-SLIDER-RENDER-RACE` (resolvidos). Detalhes: `Foruns/forum_moka_fix_slider_carregando_20260809.md` + `Memorias/memoria_moka_fix_slider_carregando_20260809.md`.

### 2026-08-09 (3) — 🔧 MOKA 5.8.1: seletor de parágrafo funciona no PDF + aviso amigável de voz neural sem chave
Missão 3 do dia (voz do Miguel): **(1)** os botões ⇤ "Do começo" e ¶ "Parágrafo" do menu de seleção não faziam nada em PDF — raiz: `closest("p,h1..li")` não existe na camada de texto do pdf.js (só spans). Fix: `pdfParagraphSpanRange()` detecta o parágrafo VISUAL por geometria das linhas (indento, espaço vertical, tamanho de fonte, linha curta antes da margem); EPUB segue no `closest()`. **(2)** ler em voz alta sem chave OpenAI (ou chave inválida → 400/401/403) agora avisa **na língua do usuário** — nova chave `tts_neural_hint` nos 12 idiomas ("Para ouvir com voz natural, configure a sua chave da OpenAI nas Configurações ⚙️"), 1× por sessão; a voz gratuita do dispositivo segue como fallback (`speakNeural` agora retorna `{ok, status}` em vez de cair em silêncio). Commit `f42efbc` (tsc+build verdes; verificado ao vivo nos chunks de produção). Tema Duplo: `Foruns/forum_moka_fix_seletor_pdf_aviso_tts_20260809.md` + `Memorias/memoria_moka_fix_seletor_pdf_aviso_tts_20260809.md`. Bugs: `BUG-20260809-MOKA-SELETOR-PARAGRAFO-PDF` + `BUG-20260809-MOKA-TTS-SEM-CHAVE-401`.

### 2026-08-09 (4) — 🧹 MOKA 5.8.2: fora o pop-up e o recadinho de "instalar o aplicativo" do /video
Miguel: "não quero mais isso" — o cartão `InstallPrompt` embaixo do /video ("Para usar o Moka Video, instale…") e a nota do herói ("não passa por loja") são da fase PWA; a estratégia agora é app de verdade nas lojas (TWA/Play Store, sessão irmã). Removidos os 2 usos (`a12f998`); componente fica dormente no repo. **📋 Pendente (Miguel quer discutir):** depois do app nas lojas, janelinha "Baixe o aplicativo" — formato/gatilho/texto a combinar antes de implementar.

### 2026-08-09 (5) — 🔊 MOKA 5.8.3: fala sem alerta cru "deepseek respondeu 401" — aviso amigável ×12
Miguel ainda via "deepseek respondeu 401:" ao clicar Falar num trecho. Não era o TTS (corrigido na 5.8.1): com idioma da fala ≠ idioma do livro, o Moka TRADUZ antes com a chave ativa (DeepSeek dele, rejeitada com 401) e o erro cru subia pro alert. Fix (`750f0d9`): nova chave `reader_speech_translate_error` nos 12 idiomas com as duas saídas (conferir a chave ⚙️ / ouvir no idioma original); erro cru só no console. Parentes inline (fullscreen e traduzir-página) seguem com erro cru — próxima leva.

### 2026-08-09 (6) — 🔧 MOKA 5.8.4: botão "Atualizar" embaixo do campo da chave
Miguel (voz): na edição da chave, um botão "Atualizar" (testar) logo embaixo do campo — sem caçar nas ações do fim. Olhinho 👁 inalterado. Nova chave `set_refresh_key` ×12 idiomas. Commit `0140af7`. Backup `backups/moka_lab_pre_key_refresh_20260809/`.

### 2026-08-09 (7) — 🐛 MOKA 5.8.5: SettingsModal via createPortal (cura candidata pro "menu do site some após config")
Miguel: "voltei pra página, o menu sumiu" — a topbar do site (não a do Reader) some após fechar ⚙️ Configurações; bug recorrente. Cura aplicada (`b94bfac`): `SettingsModal` agora renderiza via `createPortal(document.body)` (escapa de ancestral com `transform`/`filter`/`contain` que criava containing block e quebrava o overlay `position:fixed` — mesmo padrão do BUG-20260805-MOKA-LOGIN-MODAL-FAIXA-CORTADA). Bug marcado **ATIVO** no `CEREBRO_NODE_BUGS_ATIVOS.md` até confirmação do Miguel; se persistir, próxima leva = migrar os 9 componentes de `<style jsx>` pra `globals.css`.

### 2026-08-09 (8) — 🏠 MOKA 5.9: página própria /configuracoes + ranking integrado (fim do pop-up)
Miguel (voz): "reformula tudo nas configurações — em vez de pop-up, cria uma página própria; a pessoa vê suas IAs, edita, apaga, testa; bota o ranking de preço e qualidade nessa mesma página; bota o Grok (tem voz neural)". **Escopo dividido** (crédito no último da cadeia): esta leva = página + ranking + organização; Grok/Groq = 2ª leva. **Feito (`5e7c0d8`):** (1) nova página `/configuracoes` (corpo largo 760px, topbar, intro amigável, seção "Suas chaves de IA" reusando `SettingsForm`, seção "Ranking de preço e qualidade" com `LlmPriceRanking` integrado); (2) engrenagem das 3 páginas (estante, vídeo, Reader) navega pra `/configuracoes` em vez de abrir pop-up — **cura o BUG-20260809-MOKA-MENU-SITE-SOME-APOS-CONFIG na raiz** (pop-up removido do fluxo); (3) fix de sync da lista de entries no SettingsForm (`useEffect([initial])`); (4) 4 chaves i18n ×12. tsc+build verdes. Tema Duplo `*_moka_pagina_configuracoes_20260809`. Pendência: teste do Miguel + 2ª leva (Grok/Groq).

### 2026-08-09 (9) — 🔊 MOKA 5.9.1: modal de primeira vez (voz neural vs mecânica) + preferência nas Configurações
Miguel (voz): o aviso de voz da primeira vez era um alert() sem opção — a pessoa fica sem saber o que fazer. Agora é um **modal com 2 botões de ação**: "⚙️ Configurar voz neural" (→ `/configuracoes`) ou "Seguir com voz mecânica gratuita" (só fala); + "Não mostrar de novo" (grava no localStorage). E a preferência fica acessível **depois** nas Configurações: novo bloco "🔊 Preferência de voz" com botão "🔔 Mostrar de novo o aviso de voz" (reseta `moka.ttsWarned`). 8 chaves i18n ×12. Commit `158151d`. Detalhe técnico: CSS do modal foi pro `globals.css` (styled-jsx `panic` do `visitor.rs` dentro de bloco condicional — dívida FOUC conhecida se manifestando).

### 2026-08-09 (10) — 🐛 MOKA 5.9.2: cura definitiva do menu do Reader que some + voz neural detecta OpenAI inativa
Miguel (reporte): "menu superior travou de novo" (o do Reader, com traduzir/expandir) ao mexer no campo de fala + "botei a chave OpenAI mas tá com voz mecânica, não tem como mudar". **(1) Cura do BUG-20260801-MOKA-MENU-SUPERIOR-SOME (crônico, 4ª ocorrência):** o botão 👁/🙈 de ocultar menu agora **só funciona em fullscreen** (modo imersivo explícito). Fora de fullscreen, o menu **nunca some** — acaba o "menu travou sem querer". `useEffect` reforçado: reexibe menu em qualquer interação (settings, modal fala, traduzir-livro, ajuda, resumo). **(2) Voz neural detecta OpenAI inativa:** se há OpenAI no cofre mas outra IA está ativa, o Moka avisa "Você tem uma chave OpenAI, mas ela não está ativa. Ative a OpenAI nas Configurações" (nova chave `tts_neural_activate` ×12) — em vez de ficar mudo em mecânica. Commit `b7576b1`. **Decisão de produto registrada (Miguel):** ecossistema OpenAI — quando quer voz neural, o ideal é o OpenAI traduzir E falar (ou travar que só OpenAI faz neural); a debater.

### 2026-08-09 (11) — 🐛 MOKA 5.9.3: 3 modais do Reader via createPortal (cura menu cortado + microfone quebra livro)
Miguel (reporte, iPad): "menu superior travou/cortou de vez" + "microfone abre caixa que quebra o livro, era pra ser pop-up flexível por cima". **Raiz comprovada:** `AskModal`, `TranslateBookModal`, `SummaryModal` moravam inline no Reader (que tem `transform`/`backdrop-filter` = containing block) → overlay `fixed` quebrava. Mesmo padrão do bug do login (AuthModal) e SettingsModal — já curados com `createPortal`. **Fix (`93ac844`):** os 3 modais agora via `createPortal(document.body)` + guarda SSR. **Com isso, TODOS os 5 modais do Reader estão portalizados.** Bug `BUG-20260809-MOKA-MENU-CORTADO-3-MODAIS-CONTAINING-BLOCK` no RESOLVIDOS. Nota: a cura anterior do 👁/🙈 (só em fullscreen) resolveu o toque acidental — esta cura resolve o containing block. **Decisão de produto (Miguel):** voz neural multi-provedor — OpenAI E Grok (com K) fazem TTS; Grok também pra transcrição/escuta; 2ª leva.

### 2026-08-09 (12) — 🏆 MOKA 6.0: reforma /configuracoes + Grok/Groq + fim FOUC + propaganda neutra
Grande reforma (pedido do Miguel: "refaz tudo, tá bagunçado"). **(1)** Grok (xAI) + Groq adicionados como provedores (8→10) — ambos têm TTS+STT (pesquisado e confirmado: Grok 5 vozes/20+ línguas). **(2)** TTS estendido: `providerId === "openai"` → `["openai","grok","groq"]` (helper `getNeuralTtsConfig`). Allowlist `/api/tts` +api.x.ai/api.groq.com. **(3)** Ranking 15→17 modelos + Grok STT. **(4)** `/configuracoes` reorganizada: lista de chaves no TOPO + botão "+ Adicionar nova chave" (form escondido) + tirado o quicknav (loop "configurações dentro de configurações"). **(5)** Propaganda neutra: "voz perfeita"/"MESMA chave OpenAI" eliminados dos 12 idiomas → "algumas IAs servem (OpenAI, Grok, etc.)". Textos hardcoded PT → i18n. **(6)** Cura FOUC: 734 linhas de CSS dos 2 `<style jsx>` migradas pro `globals.css` — acaba o flash desconfigurado. Commit `7405d65` (+970/−806). tsc+build verdes. Tema Duplo `*_moka_6_reforma_config_20260809`.

### 2026-08-09 (13) — 🤖 MOKA 6.1: ranking de preços DINÂMICO + agente atualizador diário (ecossistema)
Miguel: "preços têm que ser dinâmicos, atualizados a cada 24h, cria um agente — vamos usar no ecossistema inteiro". **(1) Agente Python** `atualizador_precos_llm.py` (Projeto Cafezinho Agentes): raspa OpenRouter + tabela canônica, cotação USD-BRL, monta ranking, escreve `ranking_llm.json`, loga diff. `py_compile` verde; LEIA-ME com cron Tencent diário. **(2) Moka consome dinâmico:** `fetchLlmPrices()` com cache 24h + fallback hardcoded (`LLM_PRICES_DYNAMIC_URL` vazio até endpoint público). `LlmPriceRanking` mostra "↻ atualizado em DD/MM". Chave `rank_updated` ×12. Commit `e7e2d86`. Tema Duplo `*_moka_agente_precos_llm_20260809`. **Pendências fase 2:** deploy do cron na Tencent (SSH), endpoint público do JSON (Miguel escolhe repo/nginx/edge), scraping individual.

### 2026-08-11 — 🎉 MOKA ENVIADO PARA A PLAY STORE!
Após sessão maratona de ~14h (09/08 12:00 → 11/08 02:40), o Moka foi enviado para revisão do Google Play. Conta Play Console criada (Cafezinho Media Group, D-U-N-S 943494728), AAB v5.7.1 uploaded (827KB, 176 países), 10 declarações preenchidas, ícone+banner (preto+dourado+xícara). EM ANÁLISE (1-3 dias). Próximo: quando análise terminar, clicar "Iniciar lançamento completo". iOS depois (Apple Developer US$99/ano).

### 2026-08-11 (2) — 🍎 PESQUISA APPLE STORE: guia completo gravado
Pesquisa profunda sobre lançar o Moka na Apple App Store. Registrado em `Foruns/forum_moka_apple_store_pesquisa_20260811.md`. Resumo: Apple NÃO aceita TWA (diferente do Google) — precisa Capacitor (WKWebView). Requer Mac (Xcode), US$99/ano Apple Developer, Bundle ID `com.mokareader.app`. Risco principal: Guideline 4.2 (Minimum Functionality) — mas Moka tem funcionalidade real (IA, offline, login). Próximos passos: decidir Mac (comprar/cloud) → Apple Developer → Capacitor → build → upload → review.

### 2026-08-16 — 🔍 MOKA SEO: alerta GSC "Página com redirecionamento" curado + infraestrutura de indexação nova
E-mail GSC (WNC-20237597): 3 páginas "não indexadas — página com redirecionamento". Diagnóstico: redirects intencionais (variantes http/apex → www; /premium → /ajuda) + infraestrutura ausente (robots.txt 404, sitemap 404, zero canonical, /premium em 307 sem Location). Fix no ar (commit `434691d`): robots.ts + sitemap.ts novos (7 URLs canônicas www), metadataBase, canonical em todas as páginas públicas (home reestruturada em wrapper server + Capa.tsx; layouts pass-through p/ ajuda/experimente/tutorial), /premium vira 308 permanente no next.config. Verificado em produção. Pendência Miguel: enviar sitemap.xml no GSC. Tema Duplo `Foruns/forum_moka_gsc_alerta_redirect_seo_20260816.md` + `Memorias/memoria_moka_gsc_alerta_redirect_seo_20260816.md`.

### 2026-08-16 (3) — 📢 ESTUDO: banners animados Moka Reader no Cafezinho + 8 temáticos
Estudo completo (read-only) de como publicar os 4 banners HTML animados (300x250/728x90, PT/EN, ~135 KB autossuficientes, link mokareader.com) de `Outros/mokareader/banners/` no Cafezinho (GAM/Taboola/Teads/MGID via Ad Inserter + AMP 64% das views) e nos 8 temáticos (AdSense auto ads ca-pub-8991943608456423). Plano: slot novo no tema do Cafezinho (nunca Ad Inserter na home) + `wp-content/moka-banners/` nos 2 servidores; temáticos via `public/banners/` + componente `MokaBanner.astro`, idioma casado (Aiatolah bilíngue). Sem tocar no inventário de receita, zero CLS, rollback trivial. Aguarda decisões do Miguel (posições, posts, AMP) + "vai". Tema Duplo: `Foruns/forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md` + `Memorias/memoria_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md`.

- 17/08/2026 ~01:10 — Banners Moka NO AR no Cafezinho (home + single posts, PT, espelho+canônico) — `Foruns/forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md` §adendo 2.

- 17/08/2026 ~01:30 — Moka entra na rede de cross-promo como SUPERFÍCIE: PT→banner Cafezinho, EN→banner GSN (ordem Miguel); prompts P3/P6 no fórum `forum_banners_cross_promo_rede_cafezinho_media_group_20260817.md`.

### 2026-08-18 — 📊 QUADRO DE AUDIÊNCIA + CAIXA info@ (snapshot, pedido do Miguel)
Snapshot completo do estado de medição do Moka Reader e da caixa info@mokareader.com, por ZCode/DeepSeek. Achados: **nenhum analytics instalado no site** (sem GA4/Plausible/Vercel); tabelas de métricas do Supabase **nunca criadas** (socios-schema.sql segue pendente do Miguel desde 01/08 — pings de visita/instalação falham em silêncio); pontos_api com 7 usuários (todos teste, dormente desde 04/08); INBOX do info@ com 21 e-mails (sistema/testes/bounces, **zero e-mails de usuário real**; 6 bounces de 12/08 = gabrielbarbosa@ocafezinho.com → habresult@aol.com rejeitado). Detalhes: `Foruns/forum_moka_quadro_audiencia_emails_20260818.md`.

### 2026-08-18 (~18:30) — 🔴 URGENTE (ordem Miguel): instalar GA4 no Moka Reader
Pendência registrada como urgência máxima. Snapshot mostrou site sem analytics nenhum + tabelas do Supabase ausentes. Passos: propriedade GA4 no console (Miguel, ~2 min) → tag gtag no layout.tsx (ZCode) → push/deploy Vercel → validar Realtime. Bloco no SPRINTS_ATIVOS + aviso no MASTER §5.

### 2026-08-18 (~18:45) — 📊 GA4 INSTALADO NO MOKA READER (ordem Miguel, urgente atendida)
Propriedade "Moka Reader" criada pelo Miguel no console (G-43CSQVKW6N, fluxo Web mokareader.com). ZCode/DeepSeek: componente `GoogleAnalytics.tsx` (gtag.js oficial) no `<head>` do root layout; tsc+build verdes; backup `moka_lab_pre_ga4_20260818.zip`; commit `87c76c6` push main → Vercel; **tag verificada no ar**. Tema Duplo `*_moka_ga4_instalado_20260818`. Pendência correlata aberta: `socios-schema.sql` do Supabase (painel /socios).

### 2026-08-31 — 🎨 MOKA BUTTON DESIGN SYSTEM v1.0 & AUDITORIA VISUAL DE DESIGN
Auditoria completa de elegância e usabilidade visual do Moka App em 10 páginas em Desktop (1366px) e Mobile (375px) via Puppeteer.
- **Diagnóstico Estético:** Elegância classificada em 7.2/10 (tema porcelana, madeira e cobre).
- **Kit de Botão Unificado MOKA (v1.0):** Definidos e implementados os tokens de raio, transição tátil e elevações de sombra em 2 camadas (`--btn-shadow-rest`, `--btn-shadow-hover`) em `apps/web/src/app/globals.css`.
- **Hierarquia de Botões:** `.moka-btn-primary` (CTAs de gradiente azul profundo), `.moka-btn-secondary` (cards/elevações), `.moka-btn-ghost` (navegação/topbar), `.capa-launch-btn` (reformas táteis dos 6 módulos da Capa), `.reader-big-btn` (formato pílula rounded-full).
- **Micro-contêineres para Emojis (`.capa-launch-ico`):** Fundo suave de opacidade 8% (`background: rgba(30, 64, 175, 0.08)` e `border-radius: 12px`) eliminando distorções de renderização entre sistemas operacionais (iOS vs Android vs Windows).
- **Resposta Tátil (`Press Effect`):** `:active { transform: scale(0.98); }` em todos os botões e interativos.
- Parecer documentado em `artifacts/parecer_design_moka_20260831.md` e re-captura de telas validada com 100% de sucesso.


### 2026-09-14 — 🌐 MOKA: sync canônico→espelho→ousadia + cura do seletor de idiomas (bug do Miguel)
Ordem do Miguel (14/09): sincronizar os 3 ambientes a partir do canônico e consertar o menu de idiomas NO OUSADIA primeiro. **Sync:** canônico `2164349` intocado; espelho `428c570` (merge `-s ours`, árvore = canônico, cherry-picks preservados); ousadia fast-forward `5b2d739→2164349` (main+ousadia). Provado: 3 domínios 200 com `/privacidade` (string do commit). **Bug:** dropdown de idiomas com nomes cortando as primeiras letras + bandeirinhas de árabe/híndi picadas. Causa-raiz (medida no DOM): a regra de grupo `.igot-topbar-actions button` (44×44, fonte 20px, center, `!important`) esmagava os `.lang-option` (mesma guerra de especificidade do botão Entrar 06/09) e `max-height: 320px` cortava a lista (clientH 318 × scrollH 558). **Cura (`5d80145`, SÓ ousadia):** seletor triplo de escape `.igot-topbar-actions .lang-switcher .lang-option` (0,3,0) + dropdown `max-height: min(70vh, 460px)` com `overscroll-behavior: contain`. Provas: tsc+build verdes; antes 44×44/20px → depois 170×34/14px; lista 438=438 inteira (12 idiomas), reproduzido AO VIVO na produção do ousadia. **Pendência:** OK do Miguel → promover espelho+canônico. Tema Duplo: `Foruns/forum_moka_bandeirinhas_idiomas_20260914.md` + `Memorias/memoria_moka_bandeirinhas_idiomas_20260914.md`.


### 2026-09-15 — 📐 MOKA: cabeçalho estoura com fonte ampliada + olhinho fora da tela (bug do Miguel 14/09 ~23:30)
Screenshots do Miguel (23:29/23:30, /configuracoes e /telemetria): ao subir a fonte nas configurações o menu de cima cortava palavras dos DOIS lados; clicar no olhinho sumia TUDO até o olho (sem como reabrir). **Causa-raiz (medida no DOM, produção canônica):** a escala de acessibilidade é `body { zoom: var(--ui-font-scale) }` (slider Aa 85–140%) e a TopNav full-bleed usa `margin-inline: calc(50% - 50vw)` (2 definições, ~9066 e ~9751) — unidades `vw` NÃO reescalam com zoom, então @140% numa viewport 1164px a barra media x=-237…1392 (1629px): logo em -209 (fora à esquerda), último botão em 1364 (fora à direita), e no modo oculto o olhinho caía em -209…-148 (100% fora da tela, inclicável — o "sumiu tudo, até o olho"); `body { overflow-x: clip }` cortava sem scroll. De quebra: a 2ª `.topnav` (`space-between`, padronização 31/08) neutralizava em cascata o `flex-end` do `.topnav-hidden` (olho oculto pulava pra esquerda). **Cura (`a7f05a3`, ousadia, NO AR no laboratório):** `margin-inline: calc(50% - 50vw / var(--ui-font-scale, 1))` nas 2 definições + `.topnav-hidden { flex-end }` re-declarado após a 2ª `.topnav`. Provas no ar (browser real, sem injeção): topnav = viewport exata; os 7 controles medidos um a um `visivel: true`; modo oculto olho 1069,5–1131,1 (dentro, canto direito); mobile 390px @140% tudo dentro; escala 85% full-bleed preservado. **Deploy:** push `ousadia-mirror` branch `ousadia` E `main` (🔴 productionBranch do projeto Vercel `moka-ousadia` é `main` — push só no ousadia NÃO deploya). **Pendência:** OK do Miguel (`moka-ousadia.vercel.app/configuracoes`, fonte 140% + olhinho) → promover espelho (`merge -s ours`) + canônico (FF). Tema Duplo: `Foruns/forum_moka_topnav_fonte_estouro_20260915.md` + `Memorias/memoria_moka_topnav_fonte_estouro_20260915.md` (+ prints em `Memorias/provas_moka_topnav_20260915/`).
- 15/09 15/09/2026 11:11 — 🌐 TopNav GLOBAL no ousadia: menu visível por padrão (fim do CLEAN 31/08, chave nova), 🏠 home em toda parte, prateleira book/[id] ganha menu (ordem Miguel) — fórum: Foruns/forum_moka_topnav_global_20260915.md · AGUARDA OK p/ promover
- 15/09 15/09/2026 18:43 — 🛡️ FAROL-MOKA no ousadia: contador da casa no MokaReader (pixel→relevo HTTPS Cafezinho→coletor Tencent, humanos×bots por UA) — fórum: Foruns/forum_farol_moka_20260915.md · aguarda visita real + OK p/ promover
