# Memória técnica — Moka Reader: alerta GSC "Página com redirecionamento" + SEO de indexação (16/08/2026)

Fórum (decisões resumidas): `Foruns/forum_moka_gsc_alerta_redirect_seo_20260816.md`.
Assinatura: ZCode/Kimi K3 (sessão no workspace ZCodeProject, pedido direto do Miguel via e-mail GSC).

## Contexto

E-mail GSC 16/08 16:28 (WNC-20237597): "Página com redirecionamento" impedindo indexação no mokareader.com. Miguel baixou o export `Outros/mokareader/alertas/mokareader.com-Coverage-2026-08-16.zip` e pediu ajuda para corrigir.

## Investigação (comandos/provas)

1. **Export CSV** (extraído em `coverage_20260816/`): gráfico 2026-08-09 = 3 não indexadas / 1 indexada / 0 impressões; problema crítico = "Página com redirecionamento, Site, validação não iniciada, 3 páginas". O export NÃO lista as URLs (só o relatório no UI lista).
2. **Cadeias de redirect como Googlebot:**
   - `http://mokareader.com/` → 2 hops → `https://www.mokareader.com/` (200)
   - `http://www.mokareader.com/` → 1 hop → idem
   - `https://mokareader.com` → 301 → idem
   - Trailing slash: `/sobre/`, `/video/`, `/ajuda/` → **308** → sem barra (normal do Next App Router)
   - `/pt`, `/en`, `/index.html` → 404 (não existem rotas de locale; i18n é client-side via `ui-strings.ts`)
3. **Rotas públicas (todas 200 no www):** /, /sobre, /video, /estante, /ajuda, /configuracoes, /socios, /experimente, /tutorial, /privacidade, /biblioteca. `/login`, `/app`, `/reader`, `/auth` → 404. **`/premium` → 307** (única rota com redirect interno).
4. **`robots.txt` = 404** (HTML de erro do Next) e **`sitemap.xml` = 404** — o site não tinha nenhum dos dois. Home sem `<link rel=canonical>` e sem `og:url` (grep no HTML).
5. **`/premium` a fundo:** `curl -I` → `HTTP/2 307`, `x-matched-path: /premium`, **sem header Location**; corpo = HTML com redirect JS. Causa: `redirect("/ajuda")` do Next em página estática (prerender) sai como 307 sem Location. Para o Google, 307 = temporário → não consolina e mantém a URL na fila como "página com redirecionamento".
6. Repo: `Moka-Lab` branch `main`, HEAD pré-mudança `b5cd786`. Next `^14.2.15` (file conventions `app/robots.ts`/`app/sitemap.ts` suportadas). Páginas server vs client: SERVER = sobre, premium, privacidade; CLIENT = home, video, ajuda, experimente, tutorial, socios, estante, biblioteca, configuracoes. `video/layout.tsx` já existia (client, matiz `section-video` no body; envolve `/video/[id]` também).

## Mudanças (commit `434691d`, push `b5cd786..434691d`, 12 arquivos +141/−112)

| Arquivo | Mudança |
|---|---|
| `apps/web/src/app/robots.ts` (novo) | allow `/`; disallow `/api/`, `/auth`, `/book/`, `/biblioteca`, `/estante`, `/configuracoes`; `Sitemap: https://www.mokareader.com/sitemap.xml` |
| `apps/web/src/app/sitemap.ts` (novo) | 7 URLs www canônicas: /, /sobre, /video, /ajuda, /experimente, /tutorial, /privacidade (lastModified = build time) |
| `apps/web/next.config.mjs` | `redirects()`: `/premium → /ajuda` permanent:true (308 + Location no nível do roteamento) |
| `apps/web/src/app/layout.tsx` | `metadataBase: new URL("https://www.mokareader.com")` |
| `apps/web/src/app/page.tsx` | reescrito: wrapper SERVER exportando `alternates.canonical: "/"` + renderiza `<Capa/>` |
| `apps/web/src/components/Capa.tsx` (novo) | JSX da home movido daqui (idêntico, "use client") |
| `apps/web/src/app/sobre/page.tsx` | `alternates.canonical: "/sobre"` no metadata existente |
| `apps/web/src/app/privacidade/page.tsx` | `alternates.canonical: "/privacidade"` |
| `apps/web/src/app/ajuda/layout.tsx` (novo) | layout pass-through server c/ canonical (página é client) |
| `apps/web/src/app/experimente/layout.tsx` (novo) | idem |
| `apps/web/src/app/tutorial/layout.tsx` (novo) | idem |
| `apps/web/src/app/premium/page.tsx` | só comentário atualizado (fallback; redirect real agora no next.config) |

**Não tocado:** `video/layout.tsx` (client; canonical ali vazaria para `/video/[id]` — o sitemap cobre `/video`). `/video` fica sem canonical por ora.

**Backup:** `backups/moka_pre_seo_gsc_redirects_20260816/` no repo (originais dos 6 arquivos alterados via `git show HEAD:` — pasta fica local, não versionada, como nas sessões Moka anteriores).

**Build:** `npm run build` verde; rotas `/robots.txt` e `/sitemap.xml` apareceram na tabela de rotas (○ static).

## Verificação em produção (pós-deploy, ~17:45)

- `GET /robots.txt` → texto correto c/ Sitemap ✅
- `GET /sitemap.xml` → 7 `<url>` canônicas ✅
- Canonical no HTML: `/` → `https://www.mokareader.com` ✅; /sobre, /privacidade, /ajuda, /experimente, /tutorial ✅; /video sem canonical (proposital)
- `GET /premium` → **HTTP/2 308 + `location: /ajuda`**; seguindo → 200 em /ajuda ✅
- Smoke da home: 200, `<title>` intacto, links /sobre /estante /video presentes ✅

## Pendências / próximos passos

1. **Miguel:** enviar `sitemap.xml` no GSC (Indexação → Sitemaps) + opcional "Solicitar indexação" na home via Inspeção de URL.
2. Opcional: Miguel me manda as 3 URLs exatas do relatório (confirmação do diagnóstico — esperado: variantes http/apex e/ou /premium).
3. Observar 1-2 semanas: indexadas deve subir de 1 → 7+.
4. Futuro (não pedido): títulos/descrições próprios para /video, /ajuda, /experimente, /tutorial (hoje herdam o título genérico da home); og tags; canonical de `/video` quando houver metadata por página de vídeo.

## Lições

- `redirect()` do Next em página prerenderada sai como **307 sem Location** — para redirects permanentes de rota, usar `redirects()` no next.config (308 limpo no edge).
- Site novo sem robots.txt/sitemap = Google descobre sozinho e devagar, e reporta variantes de domínio como "página com redirecionamento".
- Client components não exportam metadata: wrapper server (página fina) ou layout pass-through resolvem canonical por rota.
- Layout com canonical vaza para subrotas (caso `/video/[id]`) — conferir hierarquia antes.
