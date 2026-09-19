# Memória técnica — Auditoria Top 10 Tendências v4 + remoção páginas V6 loops/autoria (15/09/2026)

Log técnico completo. Decisões e provas resumidas: `Foruns/forum_auditoria_top10_velocidade_v4_20260915.md`.

## Arquivos tocados (todos com backup datado)

1. NYC `/root/top_tendencias_push.py` — v4 (backup `.bak_pre_auditoria_20260915`; cópia local de trabalho no Dell: `~/ZCodeProject/tmp_auditoria_top10/`). Mudanças: `ga4_por_hora()` única consulta pagePath×dateHour com `dimension_filter` BEGINS_WITH "/20" e `limit=10000` (ANTES: 2 consultas por dia civil `hoje+ontem` para volume + 1 por hora `limit=1000` truncando); `_janela(por_hora, max_h, horas)` deriva 6h e 48h da mesma tabela; idade via `date_gmt` (ANTES `date` local BRT tratado como UTC, +3h); `sincronizar_categoria_e_pagina(top, fonte)` (ANTES `fonte` indefinido → NameError em toda rodada desde a v3 24/08 → página /top10 congelada); 423 → log INFO "post humano, protegido — regra da casa"; espelho 401 → 1 linha; `log()` só print (cron redirect grava o arquivo — antes duplicava).
2. Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (backup `.bak_pre_loops_autoria_20260915`): NAV sem `/v6/loops` e `/v6/autoria`; card "Loops Laura & Miguel" fora da home; dispatch GET `/loops` e `/autoria*` → 404 explícito "página removida (ordem Miguel 15/09/2026)"; POST `/autoria/corrigir` removido; rótulo Top10 → "(ao vivo no Canônico · espelho em lockdown pós-hack)". Funções `pagina_loops`/`pagina_autoria*` ficaram como código morto (edição mínima). JSON `/v6/api/loops` MANTIDO (sem consumidores encontrados nos crontabs Dell/NYC/Tencent/bin).
3. Mu-plugin WP `cafezinho-top-tendencias.php` — NÃO precisou de mudança (receptor/renderer estavam sãos; trava da manchete e anti-repetição ok).

## Comandos e provas-chave (reprodutíveis)

- GA4 filtro: `FULL_REGEXP "^/20\d\d/"` = 0 linhas (GA4 exige casar a string inteira) × `BEGINS_WITH "/2026/"` = 4.400 × sem filtro = 6.520 (→ limit=1000 antigo truncava; bug ativo semanas).
- Sonda GA4 no NYC exige `. /root/chaves.sh` (ADC vem do env); urllib direto morre no proxy pago (402 Tunnel) — usar ProxyHandler({}) + UA navegador (senão WAF 403).
- Idade: 270762 date_gmt "2026-09-14T12:21:29" → 30,5h reais às 18:48 UTC; endpoint exibiu 30,4h (antes: 33,1h).
- E2E 18:46: log limpo com "GA4 por hora: 1853 slugs", categoria +/- ok (423 normal), "/top10 atualizada (ok)", push canônico ok.
- Painel: `/usr/bin/python3 -m py_compile` NO TENCENT (python local 3.10 do Dell rejeita f-strings do painel 3.12 — falso erro); `sudo systemctl restart cctv-v6`; testes internos SEM prefixo /v6 (nginx o remove): /loops 404, /autoria 404, /autoria/x 404, /baleia /tendencias /audiencia /foruns /api/loops 200, home 0 links mortos, label novo no /tendencias.
- Home canônica: carrossel renderiza o novo #1; /top10 mostra "v4 15/09".
- Job espelho diário (`atualizar_top10_espelho.py`, 09:00 UTC) segue ok (9/10 com URL público) — independente do 401 do push horário.

## Fatos para lembrar

- Latência GA4 por hora ~6h em 15/09 (max_h geral 09:00): v/h=0 é dado REAL; janela relativa ao max_h mantém comparação justa entre posts.
- Redundante §118 morto (1 snapshot em autoria_views_snapshots.jsonl; coleta de autoria parou junto com a página retirada) — failover existe no código mas sem fonte viva.
- O carrinho de testes: cron WARM_CACHE usa `127.0.0.1:8084/baleia` (sem /v6) — padrão para todos os testes internos do painel.

## Rollback

- NYC: `cp /root/top_tendencias_push.py.bak_pre_auditoria_20260915 /root/top_tendencias_push.py`.
- Tencent: `cp /home/ubuntu/cafezinho/v6/painel_cctv_v6.py.bak_pre_loops_autoria_20260915 ... && sudo systemctl restart cctv-v6`.

— ZM · ZCode/GLM-5.3 · 15/09/2026 15:5x BRT
