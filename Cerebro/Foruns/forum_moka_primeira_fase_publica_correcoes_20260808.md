# Fórum — Moka 1ª FASE PÚBLICA: correções de comunicação, avatar, sócios e rodapé

> Data: 2026-08-08 · Autor: ZCode (GLM-5.2) · Status: ✅ **NO AR desde 09/08** (commits `f442edd`+`23f521d`, deploy Vercel verificado ao vivo — ver adendo 09/08 abaixo)
> Repo: `Outros/Aplicativos/Moka/Moka-Lab` (git `migueldorosario1/moka`, branch main; HEAD `8790c9a` → `f442edd`)
> Backup pré-mudança: `Outros/Aplicativos/Moka/backups/moka_lab_pre_correcoes_fase1_20260808_1027/`

## Decisão do Miguel (diretriz da 1ª fase pública)

O Moka Reader será lançado inicialmente como um produto **gratuito**, com experiência simples e limpa. Por isso, nesta versão:

1. **Quem somos** — remover sigla **BYOK** e jargões técnicos; explicar o que o Moka faz em **linguagem simples**.
2. **Login/autenticação** — revisar avatar Google intermitente (`?` no lugar da foto).
3. **Página de Sócios** — **FORA da 1ª fase**: remover da navegação/home qualquer link, botão, chamada ou referência (inclusive "0 de 200" / Sócios Fundadores). **Código e rota preservados** para a 2ª fase (não apagar). Como sai da navegação, o fluxo de login/redirect específico de sócios deixa de ser prioridade.
4. **Rodapé** — remover "experimental" do botão/mensagem de feedback (não apresentar o Moka como provisório). Manter mensagem simples tipo "Encontrou um bug ou tem uma sugestão? Fale com a gente."
5. Preservar código reaproveitável e evitar mudanças destrutivas.

## O que foi implementado (commit `f442edd`)

### 1. Quem somos (`/sobre`, `sobre/page.tsx`)
- **Removido:** "Cada usuário pode usar sua própria chave de API (BYOK) de qualquer provedor de IA — DeepSeek, OpenAI, Kimi (Moonshot), Qwen, Z.ai, Together, Anthropic ou Google Gemini. As chaves ficam criptografadas no próprio dispositivo."
- **Novo (linguagem simples):** "Toda a inteligência artificial fica no seu controle: você escolhe o provedor de IA que prefere usar, e a chave de acesso fica guardada e criptografada no seu próprio aparelho — nunca no servidor do Moka. Assim, a privacidade das suas leituras é total e o custo depende só do que você consome."

### 2. Avatar Google intermitente — `?` (`auth.ts` + `AuthButton.tsx` + `AuthGate.tsx`)
- **Causa-raiz encontrada:** no 1º login via OAuth (redirect do Google), o JWT às vezes vinha **sem `user_metadata` completo** (`full_name`/`avatar_url` ausentes) → `userName` chegava `null` → caía no fallback `?` (`(userName ?? "?").charAt(0)`). "Sair e entrar" resolvia porque forçava um token novo com metadados completos.
- **Correção dupla:**
  - **`auth.ts`:** no boot, se há sessão mas os metadados estão incompletos, força **UM `refreshSession()`** para obter dados frescos (antes de renderizar o avatar).
  - **`AuthButton.tsx`:** `onError` no `<img>` (CDN do Google 403/lento) cai para a inicial; fallback da inicial agora usa **e-mail** quando `userName` falta (em vez de `?`); `referrerPolicy="no-referrer"` para evitar bloqueio de referrer do Google; reset do flag de imagem quando o avatar muda (troca de usuário).
- `AuthGate.tsx` e `socios/page.tsx` agora passam `userEmail` ao `AuthButton`.

### 3. Sócios FORA da navegação pública (rota preservada)
- **2 links públicos comentados** (não apagados — voltam na fase 2):
  - `sobre/page.tsx` — "🤝 Painel de Sócios →" no rodapé (JSX dentro de `{/* */}`).
  - `video/page.tsx` — "🤝 Sócios" no rodapé (JSX dentro de `{/* */}`).
- A **home** (`page.tsx`) já não linkava para /socios (confirmado).
- A **rota `/socios`** e o componente `socios/page.tsx` permanecem **intactos e funcionais** (acessíveis só via URL direta — para a fase 2).

### 4. Rodapé — "experimental" removido (`ui-strings.ts`, 12 idiomas)
- **Antes:** "🚧🐛 Moka experimental — achou um bug, tem um elogio ou uma crítica? Fale com a gente: seu feedback conserta o app. ☕💛"
- **Depois:** "Encontrou um bug ou tem uma sugestão? Fale com a gente. ☕💛"
- Reescrito em **todos os 12 idiomas**: pt-BR, en, es, fr, de, it, ru, zh, ja, ko, ar, hi.
- Comentário do código em `SiteFooter.tsx` atualizado (tirou "experimental").

### 5. Flash de layout (FOUC) — corrigido na RAIZ, TODAS as páginas (`layout.tsx`)
- **Causa-raiz encontrada (geral — não só Sócios):** as cores inline no `<html>`/`<body>` do `layout.tsx` eram do **tema antigo "café"** (`backgroundColor: "#faf8f5"` bege, `color: "#2b2015"` marrom), mas o `globals.css` real é **tema "azul"** (`--bg: #f0f4f9`, `--text: #0f172a`). O navegador pintava o bege inline primeiro e, ao aplicar o CSS, trocava para azul → flash visível. Em dark mode era pior (bege → azul-noite escuro).
- **Correção:** removidas as cores inline do `<html>`/`<body>` e adicionado **CSS crítico** inline no `<head>` com as cores reais (light + dark via media query) — aplicadas imediatamente, antes do resto do CSS parsear, sem flash. Afeta TODAS as páginas.

## O que NÃO foi tocado (de propósito)

- Rota `/socios`, tabela de métricas, SQL de sócios, gateway da Tencent — tudo intacto para a fase 2.
- `/privacidade` ainda menciona "Chaves de IA (BYOK)" no título de seção (não foi pedido — é documento técnico/legal, não apresentação do produto; deixar como está).
- `page.tsx` (home) e `experimente/page.tsx` ainda usam as strings `byok_*` no JSX — são instruções funcionais de uso, não jargão de marketing; a diretiz era sobre a **apresentação do produto** (/sobre) e a **sensação de provisório** (rodapé).

## Provas

- **Build `next build`:** ✓ Compiled successfully, 19/19 páginas geradas, type-check OK.
- **`tsc --noEmit`:** exit 0.
- **Verificação pós-mudança:** 0 ocorrências de "experimental" em `ui-strings.ts`; 0 de "BYOK" em `sobre/page.tsx`; links `/socios` só em comentários `{/* */}` (ocultos da UI).

## Estado da missão

- **O que aconteceu:** 4 frentes + FOUC implementados e commitados (`f442edd`); build verde; backup feito.
- **O que falta:** ⏳ **Deploy para a Vercel** (produção `www.mokareader.com`) — pendente ordem explícita do Miguel (ação externa). ⏳ **Confirmação visual** do Miguel após o deploy (especialmente avatar Google em novo login e ausência de FOUC). ⏳ **Decisão do Miguel:** as perguntas técnicas (nível de robustez do fix de avatar / abordagem do FOUC) não foram respondidas — prossegui com as opções recomendadas (refresh de metadados + CSS crítico inline).
- **O que preciso de você (Miguel):** (1) autorizar o deploy (`git push` + Vercel, ou eu mesmo via CLI); (2) após o deploy, fazer login Google fresco e confirmar que o avatar aparece sem `?`; (3) navegar entre páginas e confirmar que o flash sumiu.

## Registros relacionados

- Pivô pra fase gratuita (Moka 5.0): `Foruns/forum_moka_fase_gratuita_byok_doacao_20260804.md`
- Sprint pós-pivô 5.5.2→5.7: `Foruns/forum_moka_sprint_pos_pivot_552_57_20260805.md`
- TWA Android + Play Store: `Foruns/forum_moka_twa_android_play_store_20260807.md`
- Memória técnica completa: `Memorias/memoria_moka_primeira_fase_publica_correcoes_20260808.md`

---

## Adendo 2026-08-09 — feedback "elogio primeiro" + DEPLOY (ZCode Qwen 3.8 Max, sessão ~11:40)

**Ordem do Miguel (voz, 09/08 ~11:35):** (1) tirar o link do Painel de Sócios de qualquer lugar público — *"não vamos divulgar agora"*; (2) tirar o nome "experimental" — *"é feio"*; (3) reescrever o convite de feedback com o **ELOGIO primeiro**: *"Tem um elogio? Uma sugestão? Uma crítica? Achou um bug? Fale com a gente."*

**Diagnóstico:** o commit `f442edd` (1ª fase completa) **nunca tinha sido deployado** — origin/main estava parado em `8790c9a`. O Miguel estava vendo o site velho, que ainda mostrava "🚧🐛 Moka experimental" e os links de Sócios. O código já estava limpo (sócios comentados, 0 "experimental" na UI) — faltava deploy + a nova redação do feedback.

**Feito (commit `23f521d`):** `footer_feedback` reescrito nos **12 idiomas** com elogio primeiro + assunto do mailto reordenado (`Moka — elogio, sugestão, crítica ou bug`). Backup `backups/ui-strings_pre_feedback_elogio_20260809.ts`. `tsc` + `next build` verdes (23 rotas).

**Deploy:** push `8790c9a..23f521d` → Vercel. **Verificado AO VIVO (~12:00):** home, /sobre e /video com o texto novo ✅; 0 ocorrências de "experimental" ✅; 0 links para /socios ✅; rota `/socios` segue HTTP 200 (preservada para a fase 2) ✅.

**Estado da missão:** TUDO NO AR. Falta só a confirmação visual do Miguel (avatar Google em login fresco + ausência de FOUC + texto do feedback do jeito que ele ditou).
