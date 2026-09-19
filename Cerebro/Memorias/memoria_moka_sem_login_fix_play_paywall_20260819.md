# Memória — Moka 6.7: app sem cadastro obrigatório (fix paywall do Play) (19/08/2026)

**Missão (ordem do Miguel, voz 19/08 ~09:00):** consertar o app ANTES de apelar; mudança mais segura possível pro Google; recado no site via bandeiras de idioma; resposta EN+PT preparadas no chat.

## Arquivos tocados (repo `migueldorosario1/moka`, commit `cc5f236`)

| Arquivo | Mudança |
|---|---|
| `apps/web/src/app/estante/page.tsx` | removido import+wrapper `<RequireAuth>` (login opcional) |
| `apps/web/src/app/book/[id]/page.tsx` | idem (leitura de livro sem login) |
| `apps/web/src/components/RequireAuth.tsx` | mantido, marcado OBSOLETO no docstring (reversão 13/08→19/08; não reimportar sem ordem) |
| `apps/web/src/app/ajuda/page.tsx` | FAQ pt+en: "Preciso criar conta?" → Não (opcional/gratuita); nova 1ª entrada "O Moka tem paywall ou cobrança?" (recado 100% gratuito, sem paywall/assinatura/compra/cadastro; IA via chave do usuário) |

## Comandos e provas

- Backup: `Moka/backups/moka_lab_pre_sem_login_20260819.zip` ✅
- `npx tsc --noEmit` exit 0 ✅ · `npx next build` verde (22/22) ✅
- Commit `cc5f236` + push main → Vercel auto-deploy ✅
- **Prova ao vivo:** chunk `app/estante/page-*.js` em produção com **0** ocorrências de "precisa estar logado"/"need to be signed in"; chunk `app/ajuda/page-*.js` com "100% gratuito" + "100% free" ✅

## Contexto-chave (para a próxima sessão)

- **Causa-raiz da rejeição Play (19/08 00:54):** login era OBRIGATÓRIO desde 13/08 (commit `b5cd786`) — o revisor leu como paywall. Miguel hoje: "a pessoa pode abrir o site e usar sem nem cadastro" — agora É verdade.
- **Só /socios segue com login** (por desenho, fora da navegação pública).
- **Resposta ao Google: NÃO enviar antes da aprovação do Miguel.** Rascunhos EN+PT no chat (e no fórum). App access field: "No login required — all content is freely accessible without an account." (Play Console → Policy → App content).
- **Mapa Rio:** GA4 já instalado pela sessão vigília (propriedade 550738207, tag G-GLEBSP5MGC no ar; nome "Mapa Rio" corrigido no painel, 0 ocorrências de "Mapa Rio").
- **Supabase socios-schema.sql:** sem credencial de escrita em cofre nenhum (sem service role, sem token Vercel, sem CLI) — caminho escolhido: **Miguel roda no SQL Editor do dashboard (2 min)**; posso colar o SQL pronto no chat se ele pedir. (Necessário também p/ conta de teste premium caso queiramos dar uma ao Google.)

**Tema Duplo:** `Foruns/forum_moka_sem_login_fix_play_paywall_20260819.md` · monitor + ATUALIZACOES + INDEX_MOKA_LOG atualizados.
