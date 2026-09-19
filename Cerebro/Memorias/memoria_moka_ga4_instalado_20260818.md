# Memória — GA4 instalado no Moka Reader (log técnico, 18/08/2026)

**Missão (ordem do Miguel, 18/08 ~18:25):** "a gente tem que instalar o ga4 no moka! coloca isso como pendência urgente!" → após o Miguel criar a propriedade no console, o ZCode/DeepSeek executou a instalação ponta a ponta.

## Arquivos tocados

| Arquivo | Mudança |
|---|---|
| `Moka-Lab/apps/web/src/components/GoogleAnalytics.tsx` | **NOVO** — `GA_MEASUREMENT_ID = "G-43CSQVKW6N"` + componente com `<script async src=gtag.js>` e `<script dangerouslySetInnerHTML>` config (padrão dos scripts inline do layout). |
| `Moka-Lab/apps/web/src/app/layout.tsx` | import + `<GoogleAnalytics />` no `<head>` (linha 109, antes de `</head>`). Vale para todas as páginas. |

## Comandos e provas

- Backup pré-deploy (regra): `zip -rq Moka/backups/moka_lab_pre_ga4_20260818.zip Moka-Lab -x node_modules/.next` → 58 MB ✅
- `npx tsc --noEmit` → exit 0 ✅
- `npx next build` → verde, 19/19 páginas ✅
- Commit `87c76c6` (autor `ZCode/DeepSeek <migueldorosario1@users.noreply.github.com>`, padrão identidade-da-mensagem) + `git push origin main` ✅
- Verificação no ar: `curl https://www.mokareader.com/` → contém `googletagmanager.com/gtag/js?id=G-43CSQVKW6N` ✅ (~75 s após o push — deploy Vercel automático)

## Notas técnicas / lições

- **Tentativa de criação via API falhou (UNAUTHENTICATED):** a service account do Tencent (`cing_sync/ga4.json`) só tem escopo da Data API do Cafezinho (propriedade 374552425); `google-analytics-admin` foi instalado no Tencent mas a Admin API não aceita essa credencial. Caminho console confirmado como o de menor atrito para o Miguel.
- **ID de medição é público** — embutido no HTML de todas as páginas por design do GA4; sem necessidade de variável de ambiente/secreto.
- **Aviso pip no Tencent:** `google-analytics-admin` instalado com `--break-system-packages` gerou conflito de protobuf com `google-ai-generativelanguage` (0.6.15 pede protobuf <6, instalado 6.33.6). O auditor GA4 do Cafezinho não usa essa lib — mas se algo do generativelanguage quebrar no Tencent, o protobuf é o 1º suspeito.
- **Pendência aberta correlata:** `socios-schema.sql` do Supabase segue SEM rodar (medição interna do painel /socios — item 1 do MASTER Moka, pendente do Miguel desde 01/08).

**Tema Duplo:** fórum `Foruns/forum_moka_ga4_instalado_20260818.md` · Catalogado em `CEREBRO_INDEX_MOKA_LOG.md` + `CEREBRO_NODE_ATUALIZACOES.md` + status atualizado no `CEREBRO_INDEX_MOKA_MASTER.md` §5 e `CEREBRO_NODE_SPRINTS_ATIVOS.md`.
