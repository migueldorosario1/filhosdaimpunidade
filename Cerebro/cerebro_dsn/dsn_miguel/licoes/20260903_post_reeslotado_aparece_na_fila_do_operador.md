# Lição DS-Dell · 2026-09-03 — Re-slot de post publicado deixa rastro na fila do operador

**Contexto:** o ConvergeLab 268697 «Computação federada pode levar IA ao SUS…» foi publicado 13:58:12 (topo da home às 14:00 na DS-028; 200 no canônico às 14:30) e saiu do publish entre 14:31 e 15:00 (DS-030). Nesta ronda (15:30), a sonda per-ID segue dando **401 rest_forbidden** — mas a lista da operadora (AGY-L AL-567, 15:15) mostrou o post **FUTURE 20:38 com blindagem 100%** (thumbnail/img/txt/evento_cron). Ou seja: **o post não se perdeu — foi RE-SLOTADO** (publish → future 20:38).

**O quê:** re-slot de post publicado deixa RASTRO no calendário de quem opera. O vigia vê só o sumiço do publish (401); o operador vê o novo slot no future. O par das duas fontes fecha o diagnóstico sem WP-CLI.

**Por quê:** 401 no REST anônimo só diz "não-público" — não distingue perda (trash/delete) de re-slot (future) nem de draft. E o gatilho provável do re-slot: o 268697 subiu ~75s após o Ceará 268841 (13:56:57) — gap < 20 min da Emenda 5 → o filtro recuou o post na sequência (~14:3x-15:00), o MESMO mecanismo do 268763 (INCIDENTE-1154; regra permanente da CL-119 "post publicado não sai"). Publicar 2 posts quase juntos = convite ao filtro corrigir depois, com o link já no ar.

**Como aplicar:** (1) ao flagrar post publicado fora do publish, cruzar NA MESMA RONDA com a lista future/draft de quem opera (AGY/ZM têm WP-CLI); (2) re-slot blindado (com capa/selos/evento) = provável filtro automático → pedir restauro ao dono (CL-119) e registrar; (3) a pergunta que FECHA o incidente é "re-slot intencional (decisão editorial) ou automático (filtro)?" — automático = restaurar para publish (o permalink já saiu), intencional = registrar o motivo e encerrar a vigília; (4) sem resposta do dono, o registro fica aberto — não declarar perdido nem resolvido.

**Refs:** DS-20260903-030/031 (de_dell.md) · AL-20260903-567 (de_laura.md) · INCIDENTE-1154 · CL-119 · CL-122 (268763) · licoes/20260903_o_total_da_janela_esconde_post_que_saiu_do_publish.md · BUG registro no nodo.
