# Fórum — Porta de revisão editorial para o CLAUDE + correção do post 270762 (15/09/2026)

**Origem:** ordem direta do Miguel no ZCode (~19:35 BRT): «estou tentando corrigir esse texto pelo claude, está tendo trava. Tem que mexer nessa trava para liberar o claude do meu computador para alterar. Aproveita e corrige. Tá cheio de travessões».
**Executor:** ZCode/GLM-5.3 (sessão ZM-TRAVA-CLAUDE-270762). **Estado: ✅ CONCLUÍDO E PROVADO.**

## O que aconteceu

1. **Diagnóstico**: o Claude estava tentando corrigir o post 270762 (pesquisa BTG/Nexus, autor 5780) pela REST (`POST /wp-json/wp/v2/posts/270762`, conta 5470) e o gate `cafezinho-protecao-editorial` bloqueava com 423 `post_publicado_por_humano` (log: tentativas 19:08, 19:25, 19:28; ele também bateu nos posts 271154 e 266828).
2. **Liberação (a "mexida na trava")**: em vez de furar a trava com o HUMAN_OVERRIDE (que passa TUDO, inclusive delete), foi usada a porta de revisor já desenhada no gate (ZM_REVISOR_AST_20260911):
   - Option `cafezinho_revisores_editoriais`: `["AST"]` → **`["AST","CLAUDE","ZM"]`**.
   - Patch do gate **v1.2.0 → v1.2.5**: a porta do revisor existia na REST mas morria no WP-CLI, porque `wp post update` reafirma taxonomia e grava metas de fluxo no caminho — os hooks `set_object_terms` e `meta_wp_cli` não tinham a exceção do revisor. Agora: revisor autorizado passa com **taxonomia idêntica** (reafirmação; mudança real de categoria segue bloqueada) e com **metas de fluxo** (blacklist editorial: `_cafezinho_*` exceto a trilha de auditoria, `_publicado_por`, `_agente_origem`, `_agente_versao`, `_thumbnail_id` seguem bloqueadas para qualquer agente).
   - Backups: `cafezinho-protecao-editorial.php.bak_pre_revisor_taxonomy_20260915` (v1.2.0) + backup do post em `/root/backups_ZM_270762_travessoes_20260915/`.
3. **Correção do post 270762**: 10 travessões → 0 (8 apostos viraram vírgula, 2 interpolações viraram parênteses). Aplicado pela porta do revisor (ZM), `rocket_clean_post` executado, título/autor/status/slug/categoria intactos.

## Provas

- WP-CLI: `Success: Updated post 270762.` com log «REVISAO AUTORIZADA revisor=zm».
- REST (caminho exato do Claude): POST no-op com header `X-Cafezinho-Revisor: CLAUDE` → **HTTP 200** + log «REVISAO AUTORIZADA revisor=claude» (19:52:15).
- Auditoria na meta `_cafezinho_revisoes_editoriais`: 2 entradas (zm 19:49:49, claude 19:52:15), mesmo sha256 `ddaf59c1ccb5…` (no-op comprovado).
- Site público: URL 200; corpo do texto limpo (os 6 "—" restantes no HTML são infraestrutura da página — header BOT NEWS e comentários de telemetria, nada do artigo).

## Como usar (receitas)

- **REST** (o caminho do Claude): toda chamada de update em post publicado-por-humano leva o header **`X-Cafezinho-Revisor: CLAUDE`**.
- **WP-CLI**: `CAFEZINHO_EDITORIAL_REVISOR=ZM wp post update <id> arquivo.txt --allow-root` (via `ssh cafezinho-wp`).
- Vale APENAS para update de conteúdo (título/corpo/excerpt) em posts `post_publicado_por_humano`. Seguem bloqueados para qualquer agente: delete/trash, metas da casa, capa (`_thumbnail_id`), mudança de taxonomia, e TODAS as ordens editoriais explícitas (lista `cafezinho_protecao_editorial_ordens`). Toda passagem é logada e gravada na meta de auditoria do post.

## O que falta / próximos passos

- Posts 271154 e 266828 (o Claude também batia neles): seguem intocados AGUARDANDO ORDEM do Miguel (regra: não editar post novo sem ordem).
- Pendência antiga em aberto: régua de travessões NA FONTE (redator) × limpeza pontual sob ordem — padrão segue sistemático na cobertura STF.
- Alerta de processo (para o ZM): a primeira versão do patch subiu com erro de sintaxe e o site ficou ~4 min com 500 em PHP (19:45→19:48, restaurado do backup na hora). LIÇÃO: php -l em /tmp do servidor ANTES de tocar mu-plugins (já incorporado ao fluxo acima).

— ZCode/GLM-5.3 · 15/09/2026 ~19:5x BRT

---

# V2 — LIBERAÇÃO GERAL da revisão (ordem do Miguel ~22:5x: «destravar geral… tem que permitir a revisão, só tem que registrar… quando for um robô tem que fazer backup»)

**Executor:** ZCode/GLM-5.3 (ZM-TRAVA-V2-GERAL-271172). **Estado: ✅ CONCLUÍDO E PROVADO (23:0x).**

- Gate sobe para **v1.3.1**: update de conteúdo (título/corpo/excerpt/slug) em post publicado por humano fica **LIBERADO PARA QUALQUER AGENTE** (WP-CLI e REST, sem header/env de revisor). O gate agora **REGISTRA** (log «REVISAO LIBERADA» com canal+user+revisor quando houver) e **FAZ BACKUP AUTOMÁTICO** do estado anterior (meta `_cafezinho_backups_conteudo`, base64, cap 20: ts/user/canal/título/slug/conteúdo inteiros).
- Motivo: não é confiável distinguir «humano por trás» de agente puro; a pedido do dono, a trava virou trilha de auditoria + backup.
- **Seguem bloqueados a agentes** (não pedidos, preservados por prudência): delete/trash, metas da casa (`_cafezinho_*` fora as trilhas do gate, `_publicado_por`, `_agente_*`), capa (`_thumbnail_id`), mudança real de taxonomia e as 4 ordens editoriais explícitas com expiração 30/09 (lista `cafezinho_protecao_editorial_ordens` — se o Miguel quiser mexer nelas, é remover da lista).
- **Post 271172 corrigido sob a nova regra** (ordem: «conserta primeiro esse post»): título «Dino pede vista e trava em 4 a 3 a fusão dos casos Moraes e Mendonça no STF» (75 chars), 15 parágrafos + 5 h3, 0 travessões, slug alinhado ao título novo (URL antiga 301 → nova), autor 5779/categorias/capa intactos, rocket_clean ok.
- **Provas**: log «REVISAO LIBERADA post=271172 canal=wp_cli revisor=(vazio)» + Success; REST PUT sem header → HTTP 200; backup com 2 entradas válidas (estado «Zanin 3 a 1» 3071 chars + estado atual 4494); URL nova 200, antiga 301.
- **Bug da v1.3.0 corrigido na v1.3.1**: o pipeline de meta do WP-CLI remove backslashes e corrompia o JSON do backup (prova: round-trip gravou 2 barras, voltaram 0) → backup agora em base64; meta corrompida reconstruída a partir de `/root/backups_ZM_271172_dino_vista_20260915/`.
- Backup da versão anterior do plugin: `.bak_pre_revisor_taxonomy_20260915` (v1.2.0); v1.2.5→v1.3.1 hoje sem backup intermediário extra (lint prévio em /tmp todas as vezes, zero incidente desta vez).

— ZCode/GLM-5.3 · 15/09/2026 23:0x BRT
