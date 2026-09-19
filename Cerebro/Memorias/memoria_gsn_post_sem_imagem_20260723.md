# MEMÓRIA TÉCNICA — GSN post sem imagem (Libéria) + correção estrutural anti-"sem hero"

**Data:** 2026-07-23 ~04:00–05:30 BRT · **Agente:** ZCode (Kimi)
**Fórum resumido:** `Cerebro/Foruns/forum_gsn_post_sem_imagem_20260723.md`
**Gatilho:** Miguel: "postagem sem imagem. isso não pode acontecer. corrige o post, mas faz uma correção estrutural."

---

## 1. Investigação (rastro completo)

1. URL viva confirmada sem hero: og:image = `https://www.globalsouth.news/_astro/blog-placeholder-1.Bx0Zcyzv.jpg` (fallback do template).
2. O post **não** estava no repo antigo `migueldorosario1/global-south-news` (nem em `origin/main`, nem no clone do NYC `/root/gsn_remote/gsn`). Posts daquele repo (brief-2026xxxx) dão **404 no site** — o repo antigo não alimenta mais o ar.
3. O site é servido pela Vercel a partir de **`migueldorosario1/globalsouth-v4`** (arquitetura V4, migrada em 2026-07-20). Clone local: `Projeto Cafezinho Agentes/sites-v4/globalsouth`.
4. Post `20260722-liberia-...md` sem `heroImage` no frontmatter; schema `src/content.config.ts` tem `heroImage: z.string().optional()` → build passa sem imagem.
5. Git log mostrou: `bec321a post: Liberia...` (22/07) → depois `dd56e50`/`bd28817` "fix: heroes em 1 posts sem imagem (varredura)" — varreduras manuais da sessão "Refatoracao V4" pegaram UNCTAD mas **deixaram a Libéria**.
6. Pipeline vivo: cron local `orquestrador.py --all` (03:00 e 13:00) em `agentes_tematicos/v4/` → coletor → produtor → publicador → push → Vercel.
7. `publicador.py` docstring original: *"sem imagem adequada = publica sem hero"* — **causa raiz por design**.
8. Log `agent_data/v4/cron_v4.log` (23/07 03:00): `git commit ... falhou: Please tell me who you are` → identidade git ausente em **aiatolah, globalsouth, mapario** (a sessão Refatoracao V4 de 22/07 configurou só 5 dos 8 repos; `~/.gitconfig` global não tem user.* — 20 bytes). Posts ficavam **staged e não publicados, em silêncio**.
9. Estado staged encontrado: globalsouth (ECOWAS hero+md, Morocco md sem hero), aiatolah (GigaToken hero+2md, SIMD 2md sem hero). Banco auditado: 4 artigos "aprovado" sem desfecho → risco de duplicação na próxima rodada.
10. Juiz visual: `nucleo_visao.py` chamava só Gemini. Teste direto: **HTTP 429 "prepayment credits are depleted"**. Chaves Kimi/Moonshot locais: **401** em api.moonshot.cn e api.kimi.com. Qwen-VL (`qwen-vl-plus` via DashScope compatible mode): **200 OK** — virou o fallback.
11. Banco da Libéria: aprovado 16:11:22, publicado 16:11:59 (22/07) — 37s, busca de hero falhou e publicou sem.

## 2. Correções aplicadas (código)

### 2.1 `agentes_tematicos/v4/publicador.py`
- Docstring atualizada: regra estrutural 2026-07-23 — **sem hero, não publica**.
- `_garantir_identidade_git(repo_path)`: se `git config user.name` vazio → grava "Refatoracao V4 <refatoracao-v4@local>" **no repo** (não toca global).
- `_alertar(titulo, corpo, chave, horas)`: Telegram (`nucleo_telegram.enviar_relatorio`, bot antigravity) com throttle em `agent_data/publicador_alerta_throttle.json`.
- Trava de hero: sidecar `agent_data/hero_tentativas.json` (uid→n). Sem hero → `_adiar_por_falta_de_hero()`: n<6 adia (tenta próxima rodada); n≥6 → `marcar_auditado(uid,"reprovado_sem_imagem")` + alerta 24h. Sucesso → `_limpar_tentativa_hero()`.
- Guarda git antiga (hero não versionado → strip do frontmatter e publica sem) substituída por: `git reset` + remove mds escritos + adia (mesmo fluxo de falta de hero).
- Falha em `git add`/`commit`/`push` → alerta Telegram (6h/site).

### 2.2 `agentes_tematicos/v4/nucleo_visao.py` (reescrito)
- Cascata: `_julgar_gemini` → `_julgar_qwen` (DashScope `QWEN_BASE_URL_2` ou default compatible-mode, modelo `qwen-vl-plus`).
- Prompt ganhou: *"ATENÇÃO a homônimos: lugar/pessoa com mesmo nome em outro país NÃO serve"* (caso Monrovia-Indiana).
- Erros de API agora são logados com a mensagem real (antes: `'candidates'` críptico).
- Todos fora → fail-open + `_alerta_throttle("juiz_visual_down", 24h)` + Telegram.

### 2.3 `agentes_tematicos/v4/resgate_hero.py` (NOVO)
- `--arquivo` (relativo ao blog_dir ou absoluto) e `--varredura` (todo o site).
- Usa o MESMO funil do publicador: `_buscar_hero` (Commons ns 6, ≥1200px, licença CC/PD, blocklist, relevância por token, juiz visual, `padronizar_hero` 1200×675 blur-fill) + `_registrar_hero_usada` (anti-reuso em `agent_data/heroes_usadas.json`).
- `heroImage`/`hero_credit` injetados após `pubDate:`/`date:`; aspas duplas do crédito → simples.
- Fallbacks de busca: visual_prompt do banco → termos extra CLI → category → tokens longos do título.
- **Bug encontrado e corrigido durante a operação:** checagem de hero existente montava path sem o `public/` (usava raiz do repo). Causou: (a) falso backlog no Aiatolah (~100 posts que tinham hero válida `youtube-*`); (b) substituição indevida da hero curada do post Iguaçu (discoverbrazil) — **revertida** (`git checkout <pai> -- <md>`, push). Fix: `_caminho_local_hero()` usa `hero_dir` do config em `resgatar()` e `varredura()`.

### 2.4 Guarda de build — `sites-v4/globalsouth`
- `scripts/verificar_heroes.mjs` (NOVO): varre `src/content/blog/*.md`, ignora `draft: true`, exige `heroImage` + arquivo em `public/` (remotas http(s) passam). Exit 1 com lista de infratores e dica de correção.
- `package.json`: `"prebuild": "node scripts/verificar_heroes.mjs"` → roda antes de todo `astro build` (Vercel inclusive).
- Testes: positivo OK; negativo (heroImage removida) → exit 1; `npm run build` completo: **259 páginas**, verde.

## 3. Operações git (tudo pushed)

| Repo | Commits |
|---|---|
| globalsouth-v4 | `f749524` post ECOWAS · `5f760d1` post Morocco · `132b482` fix hero Libéria · `0499b51` guarda prebuild + 2 heroes institucionais |
| aiatolah-v4 | `657b141` post GigaToken · `77358f0` post SIMD · `5b4f23c` heroes religadas (pcjs, apollo) |
| discoverbrazil-v4 | `7bcc7b6` heroes (varredura) + revert Iguaçu |
| riocarta-v4 | `defb69d` heroes religadas |
| railpost-v4 | `59a5c41` heroes (fixes pendentes da sessão 22/07) |

Identidade git local gravada em: aiatolah, globalsouth, mapario.

Banco auditado: desfecho "publicado" registrado (com `resgate_manual: zcode 2026-07-23`) para ecowas/morocco (globalsouth) e gigatoken/simd (aiatolah) — evita re-publicação duplicada.

## 4. Verificação ao vivo

- `curl` post Libéria: `og:image = .../hero/liberia-seizes-...jpg` + `<img .../hero/liberia...jpg>` ✅
- ECOWAS e Morocco: og:image próprios ✅
- Aiatolah SIMD (en): HTTP 200 ✅

## 5. Escolha editorial da hero da Libéria

1ª tentativa automática pegou "Monrovia, Indiana.jpg" (juiz fora do ar, fail-open) — **descartada manualmente**. Com o juiz Qwen-VL ativo: 1ª candidata rejeitada ("sem relação"), aprovada `File:Monrovia, Liberia - panoramio (86).jpg` — mercado de rua de Monróvia, Libéria, CC BY 3.0, autor blk24ga. Vida cotidiana da cidade da matéria = arquivo de lugar/contexto (critério editorial do juiz).

## 6. Backlog residual (não resolvido nesta sessão)

- ~18 posts antigos (mai/jun): discoverbrazil (4), riocarta (4), railpost (6), mundotrilhos (6) — Commons não retorna nada para termos em PT; juiz reprova genéricos. Precisa tradução de termos→EN ou curadoria manual (`resgate_hero.py --site X --arquivo Y --termos ...`).
- Aiatolah: 9 PT + 7 EN (posts 20–22/07) — **resolvidos**: 9 PT resgatados com termos curados em inglês (2 precisaram de 2ª rodada de termos), 7 EN espelhados dos pares PT; commit `42c6fc3`.
- Guarda prebuild existe só no globalsouth-v4 (replicar adaptando ao estilo pages).

## 7. Achados colaterais (registrar no Boletim)

- **NYC `/root/gsn_remote/gsn` (cron horário) publica no repo antigo que não vai pro ar** — 6 briefs quase idênticos de Ormuz em 2 dias (custos LLM + spam de commits). Recomendado desligar ou apontar para o v4.
- Gemini sem créditos; Kimi local 401 — atualizar `CEREBRO_NODE_CHAVES_E_LLMS.md`.
- `~/.gitconfig` global sem user.* — intencional? A autocura agora cobre os repos v4.

## 8. Adendo (~11:10 BRT, mesmo dia) — discoverbrazil: Indian Hotels sem imagem

- Miguel reportou https://www.discoverbrazil.news/blog/20260722-indian-hotels-eyes-switzerland-and-southeast-asia-after-fran/ sem imagem (escapou da varredura da madrugada).
- Resgate: `resgate_hero.py --site discoverbrazil --arquivo ... --termos "IHCL Taj hotel" ...` → hero Taj Tower (detalhes arquitetônicos), CC BY-SA 4.0, autor iMahesh, aprovada pelo juiz Qwen-VL. Commit `b824a1d`.
- **Novo bug estrutural encontrado:** no discoverbrazil, `BlogPost.astro` chamava `<BaseHead>` **sem** `image={heroImage}` e o `BaseHead.astro` só aceitava `ImageMetadata` → og:image/twitter:image **sempre** caíam no `blog-placeholder-1.jpg`, mesmo com hero presente. riocarta/railpost/mundotrilhos já passam `image={heroImage}`; globalsouth tem BaseHead que trata string.
- **Fix:** portada a lógica de string do BaseHead do globalsouth (versão simples, sem r2.dev) para o discoverbrazil + `image={heroImage}` no BlogPost.astro. Build local verde (97 páginas), og:image validado no dist e ao vivo. Commit `4cf35c3`.
- **Pendência mapeada:** `mapario` também chama `<BaseHead>` sem `image` (mesmo bug) — corrigir na próxima sessão. Verificar aiatolah (estilo pages).

## 9. Adendo 2 (~11:20 BRT) — varredura do bug de og:image nos demais repos v4

Autorização do Miguel para corrigir mapario + aiatolah (mesma família de bug do discoverbrazil).

- **mapario-v4** (commit `0339795`): mesmo fix do discoverbrazil — BaseHead aceita `ImageMetadata | string` com resolução de URL + `image={heroImage}` no BlogPost.astro. Build 15 páginas verde; og:image validado no dist (URL remota http passa direto). ⚠️ mapario ainda é **scaffold**: só fake-posts, `site: example.com` no astro.config, sem domínio de produção — nada ao vivo para verificar; fix é preventivo.
- **aiatolah-v4** (commit `8581556`): bug era **pior** — o `Layout.astro` não emitia **nenhuma** tag og:image/twitter (só og:title/description). Adicionado prop opcional `image?: string` no Layout (resolve contra `https://aiatolah.com` hardcoded, pois não há `site:` no astro.config) + og:image/og:url/twitter:card/twitter:image condicionais + PostLayout passa `image={heroImage}`. Build 219 páginas verde; **validado ao vivo**: og:image correto no post modelos-chineses (pt).
- Estado final da família v4: globalsouth ✅ (já tinha), riocarta ✅, railpost ✅, mundotrilhos ✅, discoverbrazil ✅ (4cf35c3), mapario ✅ (0339795), aiatolah ✅ (8581556). Faltam checar: os 2 repos restantes dos 8 v4 (se usarem BaseHead padrão Astro, mesmo risco).
