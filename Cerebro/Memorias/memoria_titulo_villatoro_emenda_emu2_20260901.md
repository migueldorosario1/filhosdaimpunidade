# 🧠 Memória técnica — Correção do título 268482 + EMU-2 (títulos do portal)

**Data:** 2026-09-01 ~17:36 BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · Fórum irmão: `Foruns/forum_titulo_villatoro_emenda_emu2_20260901.md`

## Log técnico completo

### 1. Localização e diagnóstico

- `ssh cafezinho-wp "sudo -u www-data wp --path=/var/www/ocafezinho post list --s='Villatoro'"` → **268482**, `publish`, 2026-09-01 12:39:03, slug `villatoro-defende-excecao-de-bukele-e-restringe-imagens-do-cecot`.
- Origem: meta `_cafezinho_origem` = via REST/python-requests, user 5470; `zizi_job_id` = `v41_nacional_9b39f2cf2c57`; `_v4_versao` = 4.1. Fact-check `_v41_fc` confirmava "Gustavo Villatoro é ministro de Justiça e Segurança Pública de El Salvador".
- Violações: regra título 2 (duas orações com "e"), regra 4/EMU-1 ("Cecot" sigla não consagrada) + sobrenome desconhecido (ponto novo → EMU-2).

### 2. Correção

```bash
ssh cafezinho-wp "sudo -u www-data wp --path=/var/www/ocafezinho post update 268482 --post_title='Ministro de Bukele defende regime de exceção do país'"
# Success: Updated post 268482.  (rollback = revisão WP / título antigo no fórum)
```

### 3. Cache — lição principal

1. `/root/rollback_canonico_20260727/purge_rocket.php` (docado no NODE_COFRE) **não purga**: rodado de /tmp standalone, PHP não carrega WordPress, `rocket_clean_domain()` não existe → saída vazia silenciosa. **Cura definitiva:** `sudo -u www-data wp --path=/var/www/ocafezinho eval 'rocket_clean_domain(); rocket_clean_minify();'` → "domain OK minify OK".
2. Mesmo após purge, HTML velho por ~5 min em cache de URL exata (Cloudflare DYNAMIC não era o culpado; origem direta via `curl --resolve www.ocafezinho.com:443:190.89.239.65` já servia o novo). Query string (`?v=2`) contornava. Resolveu sozinho ao expirar/regenerar.
3. Suspeitas descartadas na investigação: meta `_yoast_wpseo_title` (não existe no post), fastcgi_cache nginx (não há), Cloudflare cache (DYNAMIC).

### 4. Provas finais (curl público)

- `<title>Ministro de Bukele defende regime de exceção do país - O Cafezinho</title>` ✅
- og:title novo ✅ · h1 novo ✅ · `grep -c 'Villatoro defende exceção'` = **0** ✅ · home exibe título novo ✅
- URL/slug **preservado** (não quebra links/SEO de share).

### 5. Arquivos tocados

| Arquivo | Mudança |
|---|---|
| WP post 268482 | título trocado (wp-cli) |
| `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md` | 7→8 regras de título (regra 8 = cargo p/ desconhecido) · checklist item 9 ampliado · Apêndice I EMU-2 |
| `Cerebro/CEREBRO_NODE_ESTILO.md` | linha de catalogação do fórum/memória EMU-2 |
| `Cerebro/CEREBRO_NODE_ATUALIZACOES.md` | linha do tempo 01/09 |
| `Cerebro/MONITORAMENTO_DE_TRABALHO.md` | linha da sessão ✅ |

### 6. Pendências (próxima sessão com frente NYC/Tencent)

- **Enforcement no v41_ciclo** (NYC `/root/v4_labs`): o auditor de títulos deixou passar regras pré-existentes — reforçar prompt/regex (proibir " e " concatenando assunto no título + lista de siglas consagradas + exigência de cargo para pessoa sem fama nacional) e replicar a EMU-2 na diretriz que o V4.1 lê (`nyc:/root/v4_labs/dados/diretriz_qualidade_viva.md` + cópia do manual).
- Robôs irmãos geradores de título (dsn_publicador / ds_youtube / dsn_ideias, Tencent): idem — **não tocados nesta sessão** (sessão urgente patcheava o dsn_publicador 17:35, anti-colisão §112).
- Atualizar a receita de purge no NODE_COFRE/NODE_PUBLICACAO: purge_rocket.php standalone morto → usar `wp eval`.

### 7. O que preciso de você (Miguel)

Nada obrigatório. Se quiser conferir: https://www.ocafezinho.com/2026/09/01/villatoro-defende-excecao-de-bukele-e-restringe-imagens-do-cecot/
