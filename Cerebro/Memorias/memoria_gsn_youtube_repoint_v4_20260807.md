# Memória — GSN YouTube repoint V4: diagnóstico, patch, incidente de bancada e prova ao vivo

> **Data:** 2026-08-07 11:20–11:45 BRT · **Autor:** Kimi K3 / ZCode · **Fórum:** `Foruns/forum_gsn_youtube_repoint_v4_20260807.md`
> **Ordem do Miguel (voz):** "dar uma força pro Global South News, botar os vídeos, botar o agente YouTube pra funcionar, com aqueles canais que já te passei — vê se você tem a lista"

## 1. Diagnóstico (o que estava de fato acontecendo)

- **O agente YouTube do GSN estava VIVO** no droplet 142.93.48.252 (revivido 06/08): coletor `0 6,14,22` + publicador `35 6,14,22` (crons `GSN_YT_*_CENTRAL_20260806`). Coletor rodou hoje (1 vídeo novo transcrito, 37.622 chars, $6.00 Transkriptor diarizado).
- **MAS publicava no repo errado:** `GSN_REPO_DIR = ../gsn` → `/root/gsn` = clone do repo **LEGADO** `global-south-news.git` (último commit local 05/06, **183 commits atrás do origin**, que segue recebendo "Publish GSN hourly batch **(0)**" vazios do bot antigo no NYC `gsn_remote`). O site globalsouth.news é servido pelo repo **`globalsouth-v4.git`** (engine V4 — posts de hoje no ar). Resultado: os posts YouTube viravam commits num beco sem saída e **nunca apareciam no site**.
- **Morte silenciosa do post "Gary" (06/08 22:35 UTC):** pipeline Editor OK (cascata ZHIPU 429 → DEEPSEEK) → "Redator escrevendo..." → `deepseek-v4-pro` retornou vazio e o código fazia `return None, None` **sem logar erro** → item pegou 1 tentativa falha → próxima janela do cron era 8h depois → transcrição **expirou (>6h)** e foi arquivada sem nunca ter tido 2ª chance. Falha invisível até hoje.
- **Lista de canais** (`/root/gsn_agentes/canais_youtube.json`): 4 com ID real ativo + **2 placeholders** (`UCxxxx…`, nota "buscar no YouTube"): Neutrality Studies e MFA Russia.
- Outros achados: `[cost_guard] No module named 'gerenciador_tokens'` (custo não registra — não trava); flags OK (`AUTONOMO_ENABLED=1`, `STATUS=published`, `INBOX_MAX_IDADE=6h`, `MAX_TENTATIVAS=5`).

## 2. Patch aplicado (`gsn_agente_youtube_publicador.py`)

Backup: `gsn_agente_youtube_publicador.py.bak_pre_v4_repoint_20260807`. py_compile OK (local + droplet).

1. `GSN_REPO_DIR` → `os.getenv("GSN_REPO_DIR", "/root/gsn_v4/globalsouth-v4")` (clone novo, identidade `GSN Agent <agente@globalsouth.news>`).
2. `_gerar_frontmatter` no schema V4 (`src/content.config.ts` conferido — todos os campos novos são opcionais no zod, build seguro): **+`hero_legenda`** (título — fallback canônico), **+`hero_credit`** (`YouTube / <canal>`), **+`source_name`** (`<canal> (YouTube)`), **+`source_url`** (URL do vídeo); `pubDate` date-only (`2026-08-07`) no padrão V4.
3. `_git_push` ganha **commit-guard** (lição 06/08: "Push OK em log não é prova — prova é HEAD==origin"): após push, compara `rev-parse HEAD` com `rev-parse origin/main`; divergência = falha + log explícito.
4. **Logs de falha explícitos** nos 3 estágios LLM (Editor/Redator/Revisor): "❌ <estágio> retornou vazio — falha registrada, item segue na fila" (o item já era re-enfileirado pelo mecanismo de tentativas; agora a falha fica visível).
5. Estrutura mantida: blog dir `src/content/blog` (idêntico no V4), heroes em `public/hero/youtube-<id>.jpg` (o layout V4 do GSN inclusive tem schema VideoObject especial p/ heroes `youtube-*`), iframe do vídeo no corpo, anti-metalinguagem, contrato Zizilinda, memória de estilo.

## 3. Incidente de bancada (meu erro, corrigido em minutos)

- Setup da 1ª bancada: `git clone --depth 30 … && git push … && git remote set-url origin /tmp/gsn_bare.git` — o push inicial foi rejeitado ("shallow update not allowed"), o **`&&` curto-circuitou e o `set-url` nunca rodou** → o origin ficou apontando pro **GitHub real** → o teste Python commitou e **empurrou `e298ef3` ("TESTE Kimi repoint") pro origin de produção**.
- **Contenção:** verificado que o commit era a ponta (ninguém mais commitou no meio) → `git reset --hard 03cc051` + `git push --force origin main` → HEAD==origin limpo, arquivo de teste removido, `/tmp` nukado. O commit era `draft: true` (nunca renderizaria) e o force-push aconteceu ~4 min depois do push. Vercel não serviu nada errado.
- **Lição canonizada:** bancada = **`set-url` para o bare local ANTES de qualquer operação de push** (ou bare preexistente), nunca depender de cadeias `&&` em setup de teste; e commit-guard sempre — foi ele que mostrou exatamente onde o commit tinha ido parar (`HEAD==origin e298ef32`).
- Bancada refeita correta (clone full + `set-url` primeiro + bare local): frontmatter V4 validado, push isolado OK, **GitHub confirmado intacto em `03cc051`**.

## 4. Canais: 6/6 com ID real

Backup: `canais_youtube.json.bak_pre_ids_20260807`. IDs extraídos do feed RSS oficial da página de cada canal (`feeds/videos.xml?channel_id=`):

| Canal | channel_id | Status |
|---|---|---|
| Judging Freedom | `UCDkEYb-TXJVWLvOokshtlsw` | ativo (já estava) |
| Glenn Diesen | `UCZFCDIHTe9HGxtIuVDpBz7g` | ativo (já estava) |
| Dialogue Works | `UCkF-6h_Zgf9zXNUmUB-MzTw` | ativo (já estava) |
| Daniel Davis / Deep Dive | `UCWDN5zr5ttctoIAhZwW6tcQ` | ativo (já estava) |
| **Neutrality Studies** | `UCHdLVKdAeG6zAeZMGZh91bg` | **resolvido hoje** |
| **MFA Russia** | `UCIULQ7Y_Y5UiH2Rqqw8Tl7w` | **resolvido hoje** |

## 5. Prova de fogo (run real manual, 14:22–14:23 UTC)

Item pendente da inbox: `1mco7F7ZzA4` (Dialogue Works, 37.622 chars, baixado há 0,3h).

- Editor: ZHIPU 429 ×2 → cascata DEEPSEEK OK → *"Ambassador Chas W. Freeman: 'It's basically a declaration of independence from American tutelage'"* | cat=Geopolitics | tags=[Dialogue Works, Nima Alkhorshid, Ambassador Chas W. Freeman]
- Redator: DEEPSEEK OK · Revisor: ALIBABA qwen-max OK
- Thumbnail 245.897 B → `public/hero/youtube-1mco7F7ZzA4.jpg` · Markdown `brief-202608071423-ambassador-chas-w-freeman-….md` (draft: false)
- **Push verificado: HEAD==origin `8453943c`**
- **AO VIVO (~2 min depois, build Vercel):** `https://www.globalsouth.news/blog/brief-202608071423-ambassador-chas-w-freeman-its-basically-a-declaration-of-independence/` → **HTTP 200**; `<img src="/hero/youtube-1mco7F7ZzA4.jpg">` renderizado; iframe `youtube.com/embed/1mco7F7ZzA4`; legenda "YouTube / Dialogue Works" na página; post listado na **home**.

## 6. Estado final + pendências (decisão Miguel)

- **Pipeline GSN YouTube 100% funcional no site correto.** Crons inalterados (publicador roda 6/14/22 UTC :35 — próximos runs já saem no V4).
- Pendências sinalizadas: (a) bot legado "hourly batch (0)" no NYC segue girando vazio (log 143MB e subindo) — candidato a desligar na faxina; (b) ZHIPU/GLM sem saldo no roteador GSN (429) — cascata segura, mas convém recarregar/remover; (c) janela de expiração da inbox (6h) × cron espaçado = 1 falha mata o item (foi o que matou o "Gary" 06/08) — avaliar 12h; (d) `[cost_guard]` sem `gerenciador_tokens` — custo LLM do GSN não está registrando no banco.
