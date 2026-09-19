# Memória — Moka 1ª FASE PÚBLICA: correções (log técnico completo)

> Data: 2026-08-08 · Autor: ZCode (GLM-5.2) · Fórum: `Foruns/forum_moka_primeira_fase_publica_correcoes_20260808.md`
> Repo: `Outros/Aplicativos/Moka/Moka-Lab` (git `migueldorosario1/moka`, branch main)
> Commit: `f442edd` (a partir de HEAD `8790c9a` / Moka 5.7.1)

## Contexto

Diretriz do Miguel para a 1ª fase pública do Moka Reader (produto gratuito, simples e limpo). Quatro frentes de correção + investigação de um flash de layout. Decisões de produto já tomadas pelo Miguel; implementação direta.

## Arquivos tocados (9)

| Arquivo | Frente | Mudança |
|---|---|---|
| `apps/web/src/app/sobre/page.tsx` | 1 + 3 | Removido BYOK/jargões (linguagem simples); comentado link /socios no rodapé |
| `apps/web/src/lib/ui-strings.ts` | 4 | "experimental" removido em 12 idiomas (`footer_feedback`) |
| `apps/web/src/components/SiteFooter.tsx` | 4 | Comentário de código atualizado (tirou "experimental") |
| `apps/web/src/app/video/page.tsx` | 3 | Comentado link /socios no rodapé |
| `apps/web/src/lib/auth.ts` | 2 | `refreshSession()` quando metadados incompletos no boot |
| `apps/web/src/components/AuthButton.tsx` | 2 | `onError` no `<img>`, fallback email, `referrerPolicy`, reset flag |
| `apps/web/src/components/AuthGate.tsx` | 2 | Passa `userEmail` ao `AuthButton` |
| `apps/web/src/app/socios/page.tsx` | 2 | Passa `userEmail` ao `AuthButton` (consistência) |
| `apps/web/src/app/layout.tsx` | FOUC | Removidas cores inline "café"; CSS crítico inline (light+dark) no `<head>` |

## Detalhes técnicos

### Frente 2 — Avatar Google `?` (causa-raiz)

O bug: após login Google, às vezes aparecia `?` no lugar da foto; sair e entrar resolvia.

**Raiz:** em `AuthButton.tsx`, o avatar fazia `(userName ?? "?").charAt(0)`. O `userName` vinha de `auth.user?.user_metadata?.full_name`. No 1º login via OAuth (redirect do Google), o `getSession()`/primeiro `onAuthStateChange` podia entregar um **JWT sem `user_metadata` completo** (`full_name`/`avatar_url` ausentes) → `userName = null` → `?`. O Supabase só atualiza os metadados após um **refresh do token**. "Sair e entrar" forçava esse refresh (token novo), por isso resolvia.

**Agravante:** o `<img>` do avatar não tinha `onError`, então se a URL do avatar existia mas o Google retornava 403/lento (CDN), mostrava imagem quebrada em vez de fallback.

**Correção (2 partes):**

1. `auth.ts` — no `getSession().then()` do boot:
   ```ts
   const u = data.session?.user;
   const meta = u?.user_metadata ?? {};
   const needsMeta = !!data.session && (!meta.full_name || !meta.avatar_url);
   if (needsMeta) {
     supabase.auth.refreshSession().then(({ data: refreshed }) => {
       setUser(refreshed.session?.user ?? u ?? null);
       setStatus("authed");
     });
   }
   setUser(u ?? null);
   setStatus(data.session ? "authed" : "anon");
   ```
2. `AuthButton.tsx`:
   - Nova prop `userEmail`; estado `imgFailed`.
   - `<img onError={() => setImgFailed(true)} referrerPolicy="no-referrer" />`.
   - Fallback: `(userName ?? userEmail ?? "?").charAt(0)` — usa inicial do email quando nome falta.
   - `useEffect` reseta `imgFailed` quando `avatarUrl` muda.
   - `title` e header do dropdown usam `userName ?? userEmail ?? t("auth_user")`.

### FOUC — Flash de layout (causa-raiz GERAL)

O Miguel relatou flash desconfigurado antes da página de Sócios carregar, e pediu para investigar a causa geral (aparece em outras páginas).

**Raiz:** `layout.tsx` tinha cores inline **hardcoded do tema antigo "café"**:
```tsx
<html style={{ backgroundColor: "#faf8f5" }}>   // bege
<body style={{ backgroundColor: "#faf8f5", color: "#2b2015", margin: 0 }}>  // marrom
```
Mas o `globals.css` real (tema atual "azul") define `:root { --bg: #f0f4f9; --text: #0f172a; }` e `@media (prefers-color-scheme: dark) { --bg: #0b132b; --text: #f1f5f9; }`. O navegador pinta o bege inline **imediatamente** (antes do CSS parsear/aplicar) e depois troca para azul → **flash visível**. Em dark mode, pior: bege claro → azul-noite escuro.

Por que Sócios acentuava: a página depende de `auth.status` (client-side), então tinha um **segundo flash** (loading → conteúdo) por cima do primeiro.

**Correção:** removidas as cores inline do `<html>`/`<body>` e adicionado CSS crítico inline no `<head>`:
```tsx
<head>
  <style dangerouslySetInnerHTML={{ __html: `
    html, body { background: #f0f4f9; color: #0f172a; }
    @media (prefers-color-scheme: dark) {
      html, body { background: #0b132b; color: #f1f5f9; }
    }
  `}} />
</head>
```
Estas cores são **idênticas** às do `globals.css` e aplicadas imediatamente (antes do resto do CSS), respeitando light/dark via media query → sem flash. Afeta TODAS as páginas, não só Sócios.

## Comandos executados (provas)

```
# Backup pré-mudança (regra do Miguel)
mkdir -p backups/moka_lab_pre_correcoes_fase1_20260808_1027
cp -r apps/web/src backups/.../src   # 1,7M

# Typecheck
cd apps/web && npx tsc --noEmit   # exit 0

# Build
npm run build --workspace=apps/web
# → ✓ Compiled successfully, 19/19 páginas, type-check OK

# Commit
git commit -m "feat(Moka): 1ª fase pública — ..."  # f442edd

# Verificação pós-mudança
grep -c "experimental" apps/web/src/lib/ui-strings.ts       # 0
grep -c "BYOK" apps/web/src/app/sobre/page.tsx              # 0
# links /socios só em comentários {/* */}
```

## Reversão

- Restaurar backup `backups/moka_lab_pre_correcoes_fase1_20260808_1027/` OU `git revert f442edd`.
- Nenhuma mudança destrutiva foi feita (sócios comentados, não apagados; código da fase 2 intacto).

## Pendências

- ~~⏳ Deploy Vercel (`www.mokareader.com`) — pendente ordem do Miguel.~~ ✅ **FEITO 09/08** (adendo abaixo).
- ⏳ Confirmação visual do Miguel (avatar em login fresco + ausência de FOUC).
- Decisão técnica do Miguel: 2 perguntas (nível de robustez do fix de avatar / abordagem do FOUC) não foram respondidas — prossegui com as opções recomendadas.

## Estado da missão (para próxima conversa retomar)

- **O que aconteceu:** 4 frentes + FOUC implementados, commitados (`f442edd`), build verde.
- **O que falta:** deploy + confirmação visual + (talvez) decisão sobre nível de robustez.
- **O que preciso do Miguel:** autorizar deploy e testar login Google fresco.

---

## Adendo 2026-08-09 — feedback "elogio primeiro" + DEPLOY (ZCode Qwen 3.8 Max)

### Contexto

Ordem do Miguel por voz (09/08 ~11:35): tirar o link do Painel de Sócios de qualquer lugar público ("não vamos divulgar agora"), tirar o nome "experimental" ("é feio") e reescrever o convite de feedback com o ELOGIO primeiro: "Tem um elogio? Uma sugestão? Uma crítica? Achou um bug? Fale com a gente."

### Descoberta-chave

O commit `f442edd` **nunca tinha sido deployado**: `git status -sb` mostrou `main...origin/main [à frente 1]` e `origin/main` parado em `8790c9a`. O site no ar (`www.mokareader.com`) ainda exibia a string velha "🚧🐛 Moka experimental — achou um bug, tem um elogio ou uma crítica?..." e os links de Sócios em /sobre e /video. Por isso o Miguel ainda via tudo que pediu para tirar.

### Mudanças (commit `23f521d`)

1. `apps/web/src/lib/ui-strings.ts` — chave `footer_feedback` reescrita nos 12 idiomas (pt-BR, en, es, fr, de, it, ru, zh, ja, ko, ar, hi), sempre **elogio → sugestão → crítica → bug → fale com a gente**. pt-BR: "Tem um elogio? Uma sugestão? Uma crítica? Achou um bug? Fale com a gente. ☕💛"
2. `apps/web/src/components/SiteFooter.tsx` — assunto do mailto reordenado: `Moka — elogio, sugestão, crítica ou bug` (antes: `bug, elogio ou crítica`); comentário do código atualizado (ordem 09/08: elogio primeiro).

Backup pré-mudança: `Outros/Aplicativos/Moka/backups/ui-strings_pre_feedback_elogio_20260809.ts`.

### Provas

```bash
# 0 ocorrências de "experimental" no código da web app
grep -rn "experimental" apps/web/src   # exit 1 (nada)

# Build
npx tsc --noEmit && npx next build     # ✓ 23 rotas geradas

# Push (levou f442edd + 23f521d)
git push origin main                   # 8790c9a..23f521d main -> main

# Verificação AO VIVO (~12:00, www.mokareader.com)
grep -c "Tem um elogio"      home/sobre/video   # 1 em cada ✅
grep -ci "experimental"      home/sobre/video   # 0 em cada ✅
grep -o 'href="/socios"'     home/sobre/video   # 0 em cada ✅
curl -o /dev/null -w '%{http_code}' .../socios  # 200 (rota preservada p/ fase 2) ✅
```

### Reversão

- Texto do feedback: `git revert 23f521d` ou restaurar o backup `ui-strings_pre_feedback_elogio_20260809.ts`.
- Fase 1 inteira: `git revert 23f521d f442edd` (push de novo) — nada foi apagado, só comentado/reescrevido.

### Estado da missão (09/08 ~12:05)

- **O que aconteceu:** feedback elogio-first nos 12 idiomas + deploy da 1ª fase completa (f442edd+23f521d) no ar e verificado ao vivo.
- **O que falta:** confirmação visual do Miguel (avatar Google em login fresco, ausência de FOUC, texto do feedback).
- **O que preciso do Miguel:** só conferir o site; se algo não agradar, é 1 revert.
