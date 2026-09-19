# Memória técnica — Emenda 7 v3: §130 humano + brecha IA na troca de capa (11/09/2026)

Log técnico completo da missão do fórum `Foruns/forum_emenda7_v3_capa_botao_humano_brecha_ia_20260911.md`.

## Ambiente e acesso

- Produção: alias SSH `cafezinho-wp` → root@190.89.239.65:51439 · WP `/var/www/ocafezinho` · wp-cli `sudo -u www-data wp --path=/var/www/ocafezinho`.
- Espelho: `root@159.65.177.60` → `/var/www/cafezinho-news` (WP 7.0, DB própria `cafezinho_news`, Basic Auth no front). ⚠️ O caminho `/var/www/cafezinho-news` NO HOST de produção NÃO existe (o /var/www de produção tem só ocafezinho + rioocafezinho=W5.2 arquivado + infra).
- Plugin: `wp-content/mu-plugins/cafezinho-gate-visao-capa.php` v1.1.0 (v2) → **v1.2.0 (v3)** nos dois hosts.

## Diagnóstico (comandos e evidências)

1. `wp post get 270135` → autor 5786, publish; `_thumbnail_id`=270133; `_cafezinho_img_check`="ok" (string não-JSON → decode falha → carimbo_ok sempre false); `_cafezinho_img_isenta`={"ts":"2026-09-11 22:57:53",…} SEM media_id (→ isenta_ok sempre false).
2. `wp option get _cafezinho_gate_visao_log` → 7 bloqueios `por:2018 post:270135` entre 21:16 e 22:57 de 11/09 + casos históricos 268406 (31/08) e 268763 (03/09, caso DiCaprio do Adendo 74 do forum_maestro). Padrão recorrente: robô 5786 bloqueado a cada 3h no post 268379 desde 08/09 (worker quer trocar capa sem carimbo — comportamento do gate, não bug).
3. Leitura dos 3 plugins correlatos: gate-imagem-checada (só publish/revert de status), real-image-gate (só home/manchete), meta-img-check-rest (só registra meta REST) → o trava-troca é SÓ o gate-visao-capa.

## v3 — mudanças de código

- `cafezinho_e7_conta_agente_user()`: lista explícita [5786,5742,5785,5470,5486,5801,5787–5798]. Motivo: TODAS as contas-agentes são administrator → `current_user_can('edit_others_posts')` não filtra robô; a lista filtra.
- `cafezinho_e7_log()`: fun extraída (v2 logava inline só bloqueio); agora loga também `acao_humana_130` e `brecha_ia_liberacao` (passes auditáveis). Mesma option `_cafezinho_gate_visao_log`, mesmos campos, últimos 100.
- `cafezinho_e7_liberacao_valida()`: decode da meta `_cafezinho_capa_liberacao`; valida ts/expira parseáveis, janela ≤24h+300s, agora<expira, media_id 0=qualquer ou ==alvo.
- Filtro `update_post_metadata`: ordem = carimbo casado/isenta casada (original) → §130 humano (uid>0, não-agente, edit_others_posts) → brecha → bloqueia (return 0).
- Metabox `cafezinho_e7_capa` (side/high) com nonce `cafezinho_e7_liberar_nonce` + hidden `cafezinho_e7_present`: estado (protegido? carimbo casado? liberação ativa até?) + checkbox `cafezinho_e7_liberar` (24h, media_id 0) + `cafezinho_e7_liberar_motivo`. Save em `save_post_post` com DOING_AUTOSAVE skip, nonce, uid>0, não-conta-agente, edit_post.
- `register_post_meta('_cafezinho_capa_liberacao')` show_in_rest com auth_callback = humano não-agente com edit_others_posts (contas-agente não autogravam liberação via REST; wp-cli grava direto — caminho das sessões IA).

## Provas executadas

- **Espelho, v2 instalada, repro (script repro_v2.php):** post autor 5786 publish; robo(uid0)=false · humano(2018)=false · thumbnail_final=0 → bug reproduzido.
- **Espelho, v3 (teste_v3.php): 10/10** (T1 bloqueia robô · T2 humano passa · T3 conta-agente logada bloqueia · T4 brecha válida passa · T5 expirada bloqueia · T6 carimbo casado passa · T7 post humano passa · T8a alvo passa · T8b fora do alvo bloqueia · T9 teto 24h bloqueia). Log com motivos novos confirmado. Posts de teste apagados (wp_delete_post --force).
- **Produção (prova_producao.php, NÃO-destrutivo — apply_filters só consulta):** P1 0 · P2 NULL · P3 0 · P4 true · P5 capa 270133 intocada · P6 NULL. Log: 23:11:46 acao_humana_130 por 2018; 23:11:47 brecha_ia_liberacao por 0.
- **Brecha gravada no 270135:** expira 2026-09-12 23:11:47, media_id 0, por wp-cli:ZCode-GLM-5.3, motivo citando a ordem do Miguel.
- Backups/rollback: produção `.bak_pre_v3_20260911` (md5 0dd466bc4a6f2f0ebb1fbcf00b6cd5e2 = v2 íntegra); espelho sem .bak próprio (antes da missão não tinha o arquivo; v2 de referência preservada em /tmp/emenda7/ dos dois hosts).

## Armadilhas da missão (novas, para lições futuras)

1. **update_post_meta retorna int quando a meta ainda não existia** (caminho add_metadata) — assert `=== true` dá falso negativo. Na bateria v3 inicial T2/T7 "falharam" por isso; corrigido para `false !== $ok` + conferir valor gravado. O PLUGIN estava certo (o log provava).
2. **apply_filters('update_post_metadata') manual precisa do 5º arg** (`$prev_value`, '') — o `cafezinho-manifesto-fotos.php` tem closure com exactly 5 expected → ArgumentCountError. No fluxo real o WP sempre passa 5.
3. **Espelho mudou de host** — checar `CEREBRO_NODE_COFRE_CHAVES.md` (espelho = 159.65.177.60), não o /var/www do host de produção.
4. Contas-agentes são administrator → capability check NÃO serve para separar humano de robô; lista explícita obrigatória.

## Estado final

- v3 no ar em produção e no espelho. Gate íntegro para a fábrica (T1/T3), humano destravado (§130), brecha IA 24h auditável funcionando.
- Pendências registradas no fórum (worker do 268379; sync dos demais mu-plugins do espelho).
- Arquivos de trabalho: `/tmp/emenda7v3/` no Dell (plugin v3, scripts de teste) e `/tmp/emenda7/` nos dois servidores.

— ZCode/GLM-5.3 · 11/09/2026 ~23:12 BRT
