# YT-PATRULHA / CCTV — 5 posts "future" travados por wp-cron inoperante (RESOLVIDO 17/08 ~17:20)

**Tag:** YT-PATRULHA (CCTV ronda 17:00) · **Achado por:** shadow Laura (evidência 266225) + diagnóstico ZCode/DeepSeek
**Status:** ✅ RESOLVIDO

## Sintoma
Post 266225 (Presidente do Equador em Pequim) ficou `future` 1h46 além do horário (15:15).
Varredura mostrou MAIS 4 na mesma condição: 265985 (16/08 09:00), 266027 (16/08 15:30),
266080 (17/08 00:00), 266197 (17/08 03:15). Todos com gate `_cafezinho_img_check` ok:true.

## Causa raiz
`DISABLE_WP_CRON=true` no canônico exige disparo externo. O cron de sistema (mutirão
ZCode 17/08) batia em `wp-cron.php?doing_wp_cron=1` via wget — respondia HTTP 200 em
~0,1s mas NÃO executava os eventos (resposta engolida por cache/camada HTTP). Prova:
eventos devidos do `publish_future_post` só rodaram quando executados direto via
wp-cli. Posts agendados cuja data foi editada depois de agendar perdem o evento
(bug clássico do WP) e, sem cron executando, ficam presos para sempre.

## Correção (ZCode/DeepSeek, 17/08 ~17:20)
1. Reagendou os eventos via função oficial `wp_schedule_single_event()` e executou
   `wp cron event run publish_future_post` → **5/5 publicados** (decisão editorial era
   do Claude — datas já vencidas, gate ok).
2. Cron de sistema do canônico trocado: wget → `*/5 * * * * sudo -u www-data
   /usr/local/bin/wp --path=/var/www/ocafezinho cron event run --due-now` (backup em
   `/tmp/cron_backup_*_20260817_*` no servidor). Testado: executa eventos em ~2,6s.
3. Observação: evento que tenta gravar meta no post 266287 (publicado por humano) é
   bloqueado pelo mu-plugin cafezinho-protecao-editorial — comportamento CORRETO da
   proteção; erro silenciado no cron (sem impacto).
4. Claude avisado na inbox (ele estava diagnosticando o 266225).

**Ação Miguel:** nenhuma.
