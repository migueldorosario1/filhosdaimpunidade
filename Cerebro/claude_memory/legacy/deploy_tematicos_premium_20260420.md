---
name: Temáticos Premium (Caminho C) deployados 2026-04-20
description: publicador_tematicos.py ganhou publicar_wp_premium + factcheck_cascata. Pipeline agora equivale ao motor_publicador da Trindade. Crontab ainda não reativado.
type: project
originSessionId: c4ce2046-925d-4cef-9df8-6970e904a43e
---
**Deployado 2026-04-20 ~14:20 BRT em Cingapura.**

## Pipeline premium em `publicar_wp_premium`
Ordem de execução (espelho do motor_publicador):
1. **Sanitizador pré-publicação** (`sanitizador_publicacao.sanitizar_antes_publicar`) — aborta se shrink >20%
2. **Imagem em cascata:**
   - og:image da `url_fonte` → Flux Pro → Ideogram → DALL-E (via `gerador_imagem_editorial.generate_editorial_image` que já tenta banco SQLite com Tribunal Visual Gemini primeiro)
   - Fallback final garantido: `FEATURED_IMAGE_ID=227448`
3. **Atribuição "Com informações de [Fonte]"** (via `_injetar_atribuicao_fonte`; usa `util_fonte.nome_amigavel_fonte` ou hostname)
4. **Cross-link "Leia também"** (via `interlink_interno.injetar_link`; respeita `INTERLINK_DRY_RUN`)
5. **Caixa newsletter AJAX** (import direto de `motor_publicador.CAIXA_NEWSLETTER_AJAX`)
6. POST WP com `categoria_id` + `featured_media`
7. **Comentarista bot** (subprocess, só se `status=publish`)
8. **Google Indexing** via `util_indexing.disparar_indexacao`

## Fact-check cascata em `factcheck_cascata`
Perplexity (fail-open em timeout/erro) → se REPROVA explícito, apela pra Claude via `motor_publicador.auditar_com_claude` → se Claude também reprova, aborta.

## Agentes atualizados
Os 4 ativos passam por `publicar_wp_premium` com `categoria_id`, `tags_str`, `url_fonte=primeira_fonte_do_bruto(dados)`, `secao`, `status="draft"`:

- `agente_ia.py` — cat 5008 (inteligência artificial), secao="tecnologia"
- `agente_matriz_energetica.py` — cat 5052 (FOSSIL) ou 98 (TRANSICAO); secao="geopolitica" ou "economia"
- `agente_mercado.py` — cat 5064 (mercado), secao="economia". **Fail-fast yfinance** mantido.
- `agente_inflacao.py` — cat 43 (economia), secao="economia", sempre draft. **Fail-fast SIDRA** mantido.

## Helper novo
`primeira_fonte_do_bruto(texto)` — regex `(?:FONTE|URL):\s*(https?://...)` no material coletado por `coletar_rss_24h` + `coletar_brave`. Os agentes chamam isso antes de passar `url_fonte` pro premium.

## Validação em produção
Teste manual Matriz Energética FOSSIL (14:22 UTC):
- og:image da OilPrice carregada na 1ª tentativa da cascata (media_id=237248)
- Atribuição "Com informações de OILPRICE" adicionada
- Cross-link achou matéria Venezuela-Petrobras (Jaccard OK, mesma categoria fóssil)
- Draft criado id=237249. Painel: `/wp-admin/post.php?post=237249&action=edit`

## Posts de teste pra limpar manual (sandbox bloqueia DELETE via API)
- 237233, 237243, 237249 no Cafezinho — todos rascunhos do caminho C em testes

## Estado crontab
**NÃO reativado.** Os 4 agentes seguem dormentes no crontab_server.txt. Linhas comentadas (em versão anterior do forumtematicos.md Seção 6.3) estão como documentação — não aplicadas via `crontab -`. Rodada manual fica como teste sob demanda até Miguel autorizar staging 48h.

## Arquivos criados/atualizados
- `root/util_indexing.py` (NOVO) — whitelist unificada `("ocafezinho.com",)`
- `root/publicador_tematicos.py` (estendido) — `publicar_wp_premium`, `factcheck_cascata`, `primeira_fonte_do_bruto`, 5 helpers internos
- `root/agente_matriz_energetica.py` (NOVO) — fusão petróleo+energias com `MATRIZ_FOCO` env
- `root/agente_ia.py`, `root/agente_mercado.py`, `root/agente_inflacao.py` — chamam premium + fail-fast onde aplica
- `root/agente_petroleo.py`, `root/agente_energias.py` — DORMENTES (não deletados pra rollback)
- `root/agente_ferroviario_v2.py` — refatorado pra usar `util_indexing`
