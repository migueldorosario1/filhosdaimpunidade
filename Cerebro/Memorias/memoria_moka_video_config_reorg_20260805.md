# MEMÓRIA — Moka 5.5: reorganização da área de Vídeo nas Configurações
**Data:** 2026-08-05 · **Agente:** Kimi 3 (ZCode) · **Commit:** `68063f5` (`moka/main`) · **Live:** www.mokareader.com ✅
**Contexto:** pedido do Miguel (05/08) com **aprovação prévia de plano** — primeira vez nesta série que o fluxo foi plano→aprovação→implementação.

---

## 1. Descobertas de ambiente (importantes p/ próximas sessões)

- **App do Moka fica em `/home/migueldorosario/ZCodeProject/igot`** (working copy com DOIS remotes: `origin`=igot.git antigo, `moka`=moka.git NOVO-canônico). **O mainline é `moka/main`** (Moka 5.x, App Router) — a `main` do origin/igot é ANTIGA (pages router).
- **"o 2 a gente deixa para laboratório" (Miguel, 05/08):** o repo `moka` (2º criado hoje, junto com `mokawriter`) é o laboratório do ecossistema Moka; `mokawriter` = produto Writer.
- **Deploy:** Vercel projeto `moka` → www.mokareader.com, segue `moka/main` por webhook (git push → auto-deploy ~2-3 min). OrgId: `team_QQzbgQTC569AoQxaur7tNLGj`. **Vercel CLI logado** (`npx vercel whoami` = migueldorosario1).
- **Verificação de deploy sem token:** o app é client-rendered — strings NÃO aparecem no HTML; grep nos **chunks JS** (`/_next/static/chunks/*.js`) por chaves i18n (ex.: `vid_section_title`). Chunks compartilhados têm hash determinístico — bater hash local × produção confirma o deploy.
- **i18n:** 12 dicionários (PT, EN, ES, FR, DE, IT, RU, ZH, JA, KO, AR, HI) em `apps/web/src/lib/ui-strings.ts` — o TYPE `LangStrings` exige TODAS as chaves em TODOS os idiomas (tsc pega se faltar).

## 2. O que foi mudado (arquivos)

- `apps/web/src/components/SettingsForm.tsx`:
  - **Extraído** o bloco de vídeo de dentro de `about-section` (era `<details className="settings-section">` com `vid_cfg_title`).
  - **Nova `<section id="video" className="video-section">`** após o `</details>` do BYOK: título `🎬 {t("vid_section_title")}` + sub (`vid_cfg_diff`) + 3.1 chave Whisper (campos salvar/testar mantidos, `vid_whisper_title` novo) + 3.2 servidor próprio em `<details className="video-advanced">` (`vid_server_title/hint/desc`) + 3.3 linha IPRoyal (`video-iproyal`).
  - **`about-section` agora é só o Sobre** (com `id="quem-somos"`), no fim (já tinha Saiba mais/Privacidade dentro).
  - **Quick-nav no topo** (`.settings-quicknav`) com âncoras; `id="advanced-settings"` no details BYOK; `id="ajuda"` na help-section.
  - **CSS** novo no 1º bloco styled-jsx: `.settings-quicknav`, `.video-section`, `.video-section-title/sub`, `.video-block-title/note`, `.video-advanced(-hint)`, `.video-iproyal`.
- `apps/web/src/lib/ui-strings.ts`: 9 chaves novas (`vid_section_title`, `vid_whisper_title`, `vid_server_title/hint/desc`, `nav_advanced/video/help/about`) + `byok_video_note` contextualizada — **em 12 idiomas** (traduções feitas uma a uma, não máquina de copiar).
- Git: branch local `mokavideo` (de `moka/main`) → push `moka mokavideo:main` → `68063f5`.

## 3. Respostas embutidas na UX (dúvidas do Miguel)

- IA de texto = chave principal BYOK (ranking) ✓ (escrito na nota).
- Whisper = chave OpenAI NORMAL, sem config especial; à parte porque é pra vídeo; Groq Whisper = alternativa barata (escrito em `vid_whisper_title`).
- Campo de IP = NÃO (app usa o contexto da pessoa); "Servidor próprio" opcional e IPRoyal = 1 linha p/ quem hospeda (escrito em `vid_server_desc`).
- Transkriptor mantido.

## 4. Validação

tsc EXIT 0 · `npm run build` OK · produção: chunk 543-…js com `vid_section_title` ×12 e `vid_whisper_title` ×12 · chunk compartilhado idêntico ao build local.

---

## 5. FOLLOW-UP (~07:10) — Quem somos fora das Configurações (`5dd26b2`, AO VIVO)

- Miguel: "quem somos fora da Configuração, no início da página".
- Removido o bloco about-section do SettingsForm; link "👥 Quem somos" (→ /sobre) no `igot-topbar-actions` da Capa + `.topbar-about` em globals.css; quicknav com 3 âncoras.
- **Concorrência:** outro agente publicou 5.6.1/5.7 no meio (Entrar em todas as páginas + fim das paredes de texto — removendo inclusive o about-section). Push rejeitado → rebase → conflito em SettingsForm.tsx resolvido com a versão deles (já cobria a remoção) → meu commit ficou: page.tsx + globals.css. **Lição:** moka/main está multiagente ativa — sempre `git fetch` antes de commitar e esperar rebase.
- Validação pós-merge: tsc EXIT 0 · build OK (19/19) · produção: `topbar-about` no chunk `app/page-*.js` (www.mokareader.com).
