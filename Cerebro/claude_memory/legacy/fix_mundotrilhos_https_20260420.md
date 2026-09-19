---
name: Fix MundoTrilhos redirect POST→GET + Google Indexing — 2026-04-20
description: Cross-post do ferroviário retornava sempre wp_id=12 (post antigo) porque .env tinha MUNDO_TRILHOS_WP_SITE=http:// — redirect 301 convertia POST em GET e WP devolvia lista. Google Indexing agora LIVE para mundotrilhos.com. VALIDADO em produção 21:54 BRT: post NOVO ID=25 publicado (antes era ID=12 falso repetido) + cross-post Cafezinho 237409 + Indexing disparado pros DOIS.
type: project
originSessionId: c4ce2046-925d-4cef-9df8-6970e904a43e
---
**Deployado 2026-04-20 10:14 BRT em Cingapura.**

## Bug A — wp_id=12 repetido no JSONL de publicadas

**Sintoma:** Desde 2026-04-19 ferroviário rodava no cron das 02h/04h UTC mas todos os posts "publicados" no MundoTrilhos apareciam com `wp_id=12` e link `/linha-17-ouro-...` (post antigo de 16/04). Site real tinha só 4 posts (IDs 1, 6, 10, 12).

**Causa raiz:** `/root/.env` linha 59 definia `MUNDO_TRILHOS_WP_SITE=http://mundotrilhos.com` **sem s**. `/root/.env.unificado` tinha `https://` correto, mas `.env` sobrescrevia. `carregar_chaves` carrega ambos e o último valor vence.

**Cadeia do bug:**
1. Agente POSTa em `http://mundotrilhos.com/wp-json/wp/v2/posts`
2. WP redireciona 301 → `https://...`
3. `requests` segue redirect mas **converte POST em GET** (comportamento padrão pra 301)
4. GET `/wp-json/wp/v2/posts` retorna **lista** dos posts mais recentes
5. Código lê `r.json()` — se lista, `data = data[0]` (post mais recente = ID 12)
6. `r.status_code==200` então não entra no branch de erro
7. JSONL grava `wp_id=12` e link antigo

**Fix duplo (defesa em profundidade):**
1. Servidor: `sed -i 's|http://|https://|'` em `/root/.env` linha do MUNDO_TRILHOS_WP_SITE. Backup `/root/.env.bak_pre_https_fix_20260420`.
2. Código: `agente_ferroviario_v2.py` linha 81 mudou default de `"http://mundotrilhos.com"` pra `"https://mundotrilhos.com"`. Assim mesmo sem env var correta, URL parte com https.

**Validação end-to-end no servidor:** `_publicar_em_site` chamada com título novo retornou **ID 18** (novo), link `/fix-validated-post-novo-pos-https-2026-04-20/`. Bug eliminado.

## Bug B — Google Indexing API 403 "Permission denied"

**Sintoma:** Log `❌ Erro na resposta do Google Indexing: Status 403 - Failed to verify the URL ownership` toda vez que ferroviário publicava no MundoTrilhos.

**Causa raiz:** Service account `agente-ga4@gen-lang-client-0314850052.iam.gserviceaccount.com` não está adicionada como **Owner** do domínio `mundotrilhos.com` no Google Search Console.

**Fix aplicado:** whitelist de domínios autorizados em `agente_ferroviario_v2.py`:

```python
INDEXING_ALLOWED_DOMAINS = ("ocafezinho.com",)
```

MundoTrilhos pula silenciosamente com log informativo `🔇 Google Indexing pulado (...) — domínio não na whitelist.` Sem mais erros de stack trace no log.

**Reativação futura:** Quando Miguel verificar o domínio `mundotrilhos.com` no Search Console + adicionar o service account como Owner, basta editar a tupla `INDEXING_ALLOWED_DOMAINS` pra incluir `"mundotrilhos.com"`. Uma linha.

## Testes de limpeza feitos

Durante debug criei posts 13-17 no MundoTrilhos. Depois do fix rodou teste que criou 18. Todos (13-18) já foram deletados via `DELETE .../posts/{id}?force=true`. MundoTrilhos está de volta com IDs 1, 6, 10, 12 — estado original.

## Pendências conhecidas relacionadas

- Media ID 227658 (fallback de imagem do MundoTrilhos via `FEATURED_IMAGE_ID_TRILHOS` no env) **não existe** no site. WP ignora silenciosamente (seta featured_media=0). Não crítico mas um dia dá pra uploadar uma imagem real.
- Primeira validação do fix em produção será no cron 02h UTC de 2026-04-21.
