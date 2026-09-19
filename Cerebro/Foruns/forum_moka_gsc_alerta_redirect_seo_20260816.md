# Fórum — Moka Reader: alerta GSC "Página com redirecionamento" + infraestrutura de indexação (16/08/2026)

**Status: ✅ RESOLVIDO E NO AR (commit `434691d`, deploy Vercel verificado em produção).**
Memória técnica (log completo): `Memorias/memoria_moka_gsc_alerta_redirect_seo_20260816.md`.

## O que aconteceu

Miguel recebeu e-mail do Google Search Console (16/08 16:28, WNC-20237597): "Novo motivo que impede a indexação — Página com redirecionamento", 3 páginas afetadas. Baixou o export de cobertura em `Outros/mokareader/alertas/mokareader.com-Coverage-2026-08-16.zip`.

## Diagnóstico (o que o alerta SIGNIFICA)

- O export CSV só traz o resumo: **3 páginas "não indexadas" por redirect, 1 indexada** (gráfico 09/08). O Google conhece pouquíssimas URLs do site — o alerta é de um site novo começando a ser descoberto.
- As URLs com redirect são **intencionais e corretas**: variantes de domínio/esquema (`http://mokareader.com`, `http://www.mokareader.com`, `https://mokareader.com` → 301 → `https://www.mokareader.com/`) e `/premium` → `/ajuda`. Páginas que redirecionam NÃO são indexadas mesmo (o destino é) — comportamento esperado. O próprio Google diz: "se o motivo não for intencional, corrija".
- **MAS a infraestrutura de indexação do site estava fraca** (causa real da indexação lenta):
  1. **Não existia robots.txt** (404) → Google sem declaração de sitemap.
  2. **Não existia sitemap.xml** (404) → Google descobria URLs sozinho.
  3. **Sem canonical tags** em nenhuma página (nem metadataBase).
  4. **`/premium` redirecionava com 307 TEMPORÁRIO e SEM header Location** (`redirect()` do Next em página estática) → o Google não consolida 307 e fica reportando a página como "com redirecionamento" indefinidamente.

## O que foi feito (commit `434691d`, push `b5cd786..434691d`, NO AR)

1. **`apps/web/src/app/robots.ts`** (novo): allow `/`, disallow áreas logadas (`/api/`, `/auth`, `/book/`, `/biblioteca`, `/estante`, `/configuracoes`) + `Sitemap: https://www.mokareader.com/sitemap.xml`.
2. **`apps/web/src/app/sitemap.ts`** (novo): 7 URLs públicas canônicas (/, /sobre, /video, /ajuda, /experimente, /tutorial, /privacidade). Fora de propósito: `/premium` (redirect), `/socios` (fora da navegação pública na fase 1), áreas logadas.
3. **`next.config.mjs`**: `/premium → /ajuda` agora é redirect de roteamento **308 permanente com Location** (antes era 307 sem Location do `redirect()` na página; `premium/page.tsx` ficou só de fallback).
4. **`layout.tsx`**: `metadataBase: https://www.mokareader.com` (base p/ canonical/og).
5. **Canonicals em todas as páginas públicas**: home (reestruturada — `page.tsx` virou wrapper server + `components/Capa.tsx` client, JSX idêntico), `/sobre` e `/privacidade` (metadata nas próprias), `/ajuda`, `/experimente` e `/tutorial` (layouts pass-through novos, pois as páginas são client). **`/video` ficou SEM canonical de propósito**: o `video/layout.tsx` existente é client (matiz no body) e envolve também `/video/[id]` — canonical ali vazaria errado para as páginas de vídeo; o sitemap cobre.
6. Build verde, commit, push, deploy Vercel verificado em produção: robots.txt ✅, sitemap.xml ✅, 6 canonicals ✅, `/premium` → **308 Location: /ajuda** ✅, home reestruturada renderizando normal (título/links intactos).
7. Backup local: `backups/moka_pre_seo_gsc_redirects_20260816/` no repo (originais via git HEAD).

## O que falta / próximos passos

- **Miguel (2 min, no GSC):** Indexação → Sitemaps → enviar `sitemap.xml` (o robots.txt novo já declara, mas o envio manual acelera). Opcional: Inspeção de URL na home → "Solicitar indexação".
- **Miguel (opcional):** no relatório "Página com redirecionamento" dá pra ver as 3 URLs exatas — se quiser me mandar a lista eu confirmo o diagnóstico (esperado: variantes http/apex e/ou /premium).
- Não precisa clicar em "Validar correção": os redirects são intencionais (consolidação de domínio); o problema se resolve sozinho nas próximas recrawls com sitemap+canonical+308 no lugar.
- Observar nas próximas 1-2 semanas: páginas indexadas devem subir de 1 → 7+.

## Decisões registradas

- Canônico do site = **https://www.mokareader.com** (apex faz 301; Vercel).
- `/premium` é redirect permanente (308), não volta a ser página na fase gratuita.
- Áreas logadas ficam fora do sitemap e bloqueadas no robots (sem valor de busca).
