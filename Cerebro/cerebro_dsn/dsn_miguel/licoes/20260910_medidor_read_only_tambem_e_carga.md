# 20260910 — Medidor read-only também é carga: `+` em PHP não sobrescreve chave

**O quê (fato datado).** No primeiro medidor da ronda 399ª DS-Dell (10/09/2026, ~15:31 BRT), na
torneira `ssh cafezinho-wp` (`sudo -u www-data wp`), montei o «top 6» de publicados com
`$q = new WP_Query($base + ['posts_per_page'=>6])`. O script morreu no meio com
`RedisException: read error on connection to 127.0.0.1:6379` em
`wp-content/object-cache.php:1936`, dentro de `has_post_thumbnail()` → `get_post_meta()` →
**object cache**.

**Causa-raiz (provada).** Em PHP, **`+` entre arrays é UNIÃO e mantém a chave do operador da
ESQUERDA**. O `posts_per_page => -1` do `$base` **sobreviveu** ao «override» — o «top 6» virou
**a tabela inteira** e, a cada item, pediu a thumbnail ao cache, empurrando o Redis até o timeout
de leitura. **Prova controlada (2 linhas, mesma torneira):**
`$base + ['posts_per_page'=>6]` → `query_vars['posts_per_page'] = -1`, **devolvidos 2.448**;
`array_merge($base, ['posts_per_page'=>6])` → `posts_per_page = 6`, **devolvidos 6**.

**O que NÃO aconteceu (importa para não culpar o host).** O Redis **não caiu**: `PING` = `PONG`,
`used_memory` 178,46 MB de `maxmemory` 1 GB, política `allkeys-lru`, `evicted_keys` = 0,
`rejected_connections` = 0; home e `/wp-json/` responderam **200** com cache-bust. O cache **foi
empurrado**, não faliu — e o sintoma («RedisException») aponta para o alvo errado se a gente não
olhar a consulta que o precedeu.

**Como aplicar (régua).**
1. **`array_merge` para mesclar config de `WP_Query`; NUNCA `+`.** `+` é união de arrays e
   preserva a chave da esquerda — é o override que não sobrescreve.
2. **Medidor read-only também é carga.** Inventário por `--format=count`/`--format=ids`
   (e, para volume, `WP_Query` + `date_query`); `has_post_thumbnail()` (ou qualquer meta por post)
   **só nos poucos IDs da fila, um a um** — nunca dentro de varredura de tabela.
3. **Teste de controle do tamanho da resposta:** se a contagem parecer o total do site, conferir
   `query_vars['posts_per_page']` antes de acreditar no número (irmã do BUG-190: número plausível
   sem erro que o denuncie).
4. **Diagnóstico de cache:** antes de declarar «Redis caiu», ler `PING`, `info memory` e
   `info stats` — `evicted`/`rejected` zerados com o serviço ativo significam **pressão**, não queda.

**Família:** instrumento que mente ou que machuca o que mede — BUG-190 (`--after` aceito e
ignorado), BUG-191 (sticky prependido), BUG-192 (data declarada), BUG-195 (teste de controle sem
sinal). Todos respondem à mesma pergunta: **eu sei o que o meu instrumento NÃO faz?**

**Ref:** bloco `DS-Dell-20260910-025` (ronda 399ª) + `BUG-20260910-DS-198`.
