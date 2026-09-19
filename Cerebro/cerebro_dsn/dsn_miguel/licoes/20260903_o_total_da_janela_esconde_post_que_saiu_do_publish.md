# 2026-09-03 · O total da janela esconde o post que saiu do publish

**O quê.** O X-WP-Total (e qualquer contagem de saldo) NÃO mostra o post publicado que saiu do publish — o dígito fica estável porque a janela "absorve" o furo: entra 1 (post novo), sai 1 (post removido do publish) e o total não muda. Prova da ronda DS-030 (03/09 15:00): o ConvergeLab 268697 (publicado 13:58:12, topo da home às 14:00, 200 no canônico às 14:30) saiu do publish entre ~14:31 e 15:00 — `hoje=42` às 14:31 (com ele) e `hoje=42` às 15:00 (com o Natura 268394 das 14:39 entrando) = exatamente 1 post sumiu no meio e NENHUM total denunciou; a janela 3h também seguiu "normal" (11→8 = janela deslizante). Só a comparação da LISTA de IDs (o ConvergeLab esperado na janela não estava) + a sonda per-ID (401 rest_forbidden) revelaram.

**Por quê.** Contagem de volume mede fluxo (saldo da janela deslizante), não INTEGRIDADE da composição — "post publicado que sai do publish" é a recorrência do padrão INCIDENTE-1154/Emenda 5 (regra permanente da CL-119: post publicado não sai; dono ZM, hotfix pendente) e esse tipo de furo é invisível para o total justamente porque a esteira continua produzindo (o Natura entrou no mesmo intervalo). O vigia que lê só o dígito confirma "tudo normal" no exato momento em que a regra do dono foi violada.

**Como aplicar.**
1. Além do X-WP-Total, conferir a COMPOSIÇÃO da janela: a lista de IDs (topo + 3-5 anteriores + presença dos IDs esperados da ronda anterior) — furo aparece como ID esperado ausente.
2. Aritmética de consistência: total estável + 1 post novo na janela = 1 post saiu (verificar qual); usar o par "o que entrou × o que saiu" antes de declarar janela normal.
3. Sonda per-ID para confirmar: `GET /wp-json/wp/v2/posts/<id>` — 200 = publish · 401 rest_forbidden = não-público (future/draft/private/trash — anônimo NÃO distingue; future também dá 401, testado) · 404 = inexistente; `include=<id>` com o filtro publish padrão voltando [] = não está publicado.
4. Registrar na ponte com prova + dono nomeado (ZM/AL têm WP-CLI para ver status/date/evento e restaurar) e NÃO mexer em produção — o vigia reporta, o dono restaura.

**Refs:** blocos DS-20260903-029/030 da ponte (de_dell.md) · INCIDENTE-1154 (trava Emenda 5, dono ZM) · regra CL-119 ("post publicado não sai") · lição-irmã 20260903_espelho_nao_e_fila_recebe_fora_de_ordem_e_deixa_posts_de_fora.md (mesmo princípio: lista per-ID > total, agora no canônico).
