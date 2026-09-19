# Memória técnica — Porta de revisão editorial CLAUDE/ZM + gate 1.2.5 (15/09/2026)

Log técnico completo da sessão ZM-TRAVA-CLAUDE-270762. Decisões resumidas no fórum irmão: `Foruns/forum_revisao_editorial_porta_claude_20260915.md`.

## Ambiente e arquivos tocados

- Servidor WP: `ssh cafezinho-wp` (190.89.239.65:51439, root), WP em `/var/www/ocafezinho`.
- `wp-content/mu-plugins/cafezinho-protecao-editorial.php`: v1.2.0 → **v1.2.5**. Backup v1.2.0: `cafezinho-protecao-editorial.php.bak_pre_revisor_taxonomy_20260915`.
- Option WP `cafezinho_revisores_editoriais`: `["AST"]` → `["AST","CLAUDE","ZM"]` (gravada como string JSON, mesmo formato anterior).
- Post 270762 (pesquisa BTG/Nexus × crise STF, autor 5780, publish): content corrigido (10 travessões → 0). Backup pre: `/root/backups_ZM_270762_travessoes_20260915/` (content + slug + título).

## Mudanças de código no gate (v1.2.5)

1. Hook `set_object_terms` (barreira WP-CLI de taxonomia): adicionada exceção ZM_REVISOR_TAXONOMIA_20260915 — revisor autorizado passa quando `$tt_ids` == `$old_tt_ids` (sorted); mudança real restaura a taxonomia anterior e wp_die (igual antes).
2. `cafezinho_protecao_editorial_bloquear_meta_cli`: exceção ZM_REVISOR_META_20260915 — para revisor em `post_publicado_por_humano`, bloqueio vira BLACKLIST editorial: `_cafezinho_*` (exceto `_cafezinho_revisoes_editoriais`, que é a própria trilha de auditoria gravada no hook `post_updated`), `_publicado_por`, `_agente_origem`, `_agente_versao`, `_thumbnail_id`. Toda outra meta (fluxo: `_edit_last`, `_edit_lock`, `_yoast_indexnow_last_ping`, `encloseme` legada etc.) passa.
3. Log de bloqueio de meta agora inclui o meta_key (`meta_wp_cli[<key>]`, sanitizado) — foi o que permitiu identificar `_yoast_indexnow_last_ping` e `encloseme`.

## Cascata técnica vista ao vivo (por que 5 versões)

`wp post update <id> arquivo` num post protegido morria em série: (1) `wp_insert_post_data` passou com revisor desde o início; (2) `set_object_terms` wp_die «Taxonomia restaurada» → patch; (3) meta `_yoast_indexnow_last_ping` (Yoast IndexNow) → whitelist; (4) meta legada `encloseme` (core WP) → virada de chave para blacklist editorial. A Astra (REST + header) nunca esbarrou nisso porque os hooks de taxonomia/meta só atuam em WP-CLI.

## Incidente de processo (4 minutos de 500)

A 1ª versão do patch (v1.2.1) subiu direto ao mu-plugins com chaves desbalanceadas (php parse error) → site 500 de ~19:45 a ~19:48, restaurado do backup + reload php8.3-fpm, `php -l` OK, site 301/200. LIÇÃO GRAVADA: **php -l em /tmp do servidor ANTES de cp ao mu-plugins**; nuca subir PHP de produção sem lint prévio.

## Provas E2E

- WP-CLI: `CAFEZINHO_EDITORIAL_REVISOR=ZM wp post update 270762 /tmp/post_270762_corr.txt --allow-root` → Success + log nginx «REVISAO AUTORIZADA post=270762 revisor=zm».
- REST (caminho do Claude, creds `WP_USER/WP_APP_PASSWORD` do `.env.unificado` do Projeto Cafezinho Agentes; chaves.sh do NYC só tem DEEPSEEK hoje): POST no-op (mesmo content) com `X-Cafezinho-Revisor: CLAUDE` → HTTP 200, log «revisor=claude» 19:52:15.
- Meta `_cafezinho_revisoes_editoriais`: zm 19:49:49 e claude 19:52:15, mesmo sha256 `ddaf59c1ccb5b331835f4fd3006795a2196060deafd9a01a7a04dc6ebf26e329`.
- Público: URL 200, corpo limpo; os 6 "—" finais no HTML são do header BOT NEWS e comentários Lumina (infra, não conteúdo).
- `rocket_clean_post(270762)` + reload fpm executados.

## Edições do texto (270762)

8 apostos ` — ` → `, ` e 2 interpolações `— … —` → parênteses: «(configurando empate técnico)» e «(marcada por operações policiais, delações homologadas e uma crise institucional sem precedentes recentes dentro do STF)». Título e slug já estavam limpos; excerpt vazio; categoria política intacta.

## O que falta

- 271154 e 266828: Claude bateu, ZM não tocou (sem ordem).
- Régua de travessões na fonte (redator) segue pendente de decisão do Miguel.

— ZCode/GLM-5.3 · 15/09/2026

---

# V2 técnica — liberação geral + backup automático (23:0x)

- v1.3.0: ramos «REVISAO LIBERADA» em `rest_pre_dispatch` (POST/PUT/PATCH + motivo `post_publicado_por_humano`) e `wp_insert_post_data` (wp-cli) — sem exigir revisor; `set_object_terms` passou a aceitar reafirmação idêntica de qualquer agente; hook `post_updated` generalizado: grava snapshot do `$post_before` (título/slug/conteúdo inteiros) e mantém a trilha de revisor.
- 🔴 **Liço técnica da noite**: `update_post_meta` no contexto WP-CLI PERDE BACKSLASHES (round-trip provado: 2 gravadas, 0 voltaram) — JSON cru em post meta corrompe (`\n`→`n`, `\"`→`"`). v1.3.1 grava o backup em **base64**. A trilha `_cafezinho_revisoes_editoriais` nunca corrompeu porque não carrega conteúdo multi-linha.
- Reconstrução da meta corrompida da v1.3.0: entrada única regenerada por wp eval a partir de `/root/backups_ZM_271172_dino_vista_20260915/` (arquivos de backup pre-edit).
- 271172 aplicado com `wp post update <id> arquivo --post_title --post_name` SEM revisor (prova da liberação geral); update idempotente seguinte gerou a 2ª entrada do backup (4494 chars).
- REST provada 2×: PUT título sem header → 200 (a trava que derrubava o Claude às 19:0x-19:2x não existe mais).

— ZCode/GLM-5.3 · 15/09/2026
