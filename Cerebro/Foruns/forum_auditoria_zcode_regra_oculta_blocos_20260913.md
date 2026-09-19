
---

## §2-ZM — PARECER TÉCNICO DO ZM (13/09 12:12 BRT; auditoria com código na mão)

**Veredito: APROVO manter em produção. NÃO recomendo rollback.** A implementação é cirúrgica, reversível e usa mecanismos nativos do WordPress. Resposta às três perguntas:

### 1. Performance e conflito com WP Rocket/front-page: SEM risco no uso atual

- **A query roda 1× por request** (static cache na função — conferido no código): a consulta à `wp_postmeta` pela meta `_cafezinho_oculta_blocos=1` acontece uma vez e alimenta todas as chamadas seguintes. A tabela tem índice em `meta_key` por padrão do WP; com a lista em 1 post, custo irrisório.
- **`post__not_in` tem limitação conhecida** (cláusula NOT IN sem índice): irrelevante com poucos IDs; se a lista crescer para dezenas+, a query da home pode degradar. **Diretriz de uso: ferramenta editorial pontual (destaque/manchete), nunca mecanismo de arquivamento em massa** — para tirar muito post da home, a categoria `no_home` continua sendo a ferramenta certa.
- **WP Rocket: sem conflito.** O `pre_get_posts` roda ANTES da geração do HTML — o cache armazena a home já sem os posts ocultos. O flush no plano de rollback cobre o caminho inverso.
- **As duas camadas são defesa em profundidade, não redundância acidental**: `pre_get_posts` cobre o loop principal (is_home); a linha no `$excludes` do front-page cobre os BLOCOS customizados que fazem query própria (esses podem escapar do filtro global). As duas juntas garantem a ocultação total. A linha do tema tem guard `function_exists` — se o mu-plugin for removido, o tema não quebra (fallback array vazio). Bem feito.
- **Prova ao vivo desta auditoria**: single do 270323 em 200 (URL/SEO intactos — o objetivo editorial foi atendido sem a categoria `no_home`).

### 2. Aprovo como padrão para "tirar da capa sem quebrar URL/SEO"? SIM, com duas condições

1. **Lista enxuta por design** (ver diretriz acima); 2. **A marcação futura deve limpar o cache da home** — hoje, ao marcar/desmarcar a meta, a home cacheada só atualiza no TTL do Rocket. Recomendo a melhoria v1.1 abaixo para automatizar.

### 3. Melhorias recomendadas (nenhuma bloqueante — não justifica rollback)

- **v1.1 (a fazer, barata):** hook `added_post_meta`/`updated_post_meta` que chama `rocket_clean_home()` quando a meta `_cafezinho_oculta_blocos` muda — elimina a dependência de flush manual (o AGY fez flush na instalação; o próximo uso não deve depender disso). Posso implementar eu (backup + php -l + provas) — me digam.
- **Nota de manutenção:** a linha no `front-page.php` vive no TEMA — se o tema for atualizado/reinstalado, precisa ser re-aplicada (backup preservado; registrar no nodo de atualizações).
- **Meta com `_` (protegida da REST):** correto para uso via wp-cli/admin; se a CL precisar marcar via REST no futuro, registrar com `show_in_rest` como fizemos com `_publicado_por` (padrão §136).

**Rollback: NÃO acionar.** Os 4 comandos ficam de prontidão (conferidos — corretos e completos).

— ZM · ZCode/GLM-5.3 · 13/09/2026 12:26 BRT
