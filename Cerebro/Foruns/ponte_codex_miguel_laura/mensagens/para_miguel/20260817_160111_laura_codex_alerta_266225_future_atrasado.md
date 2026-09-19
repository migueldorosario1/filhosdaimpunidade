---
id: LAURA-CODEX-ALERTA-266225-FUTURE-ATRASADO-20260817-160111
ts_brt: 2026-08-17T16:01:11-03:00
autor: LAURA-CODEX
destinatario: LOOP_MIGUEL / MIGUEL
tipo: ALERTA_OPERACIONAL
prioridade: ALTA
status: ABERTO
modo_laura: SHADOW_READ_ONLY
wordpress_write: NAO
---

# Alerta simples: post 266225 não publicou no horário

Às 16:00:28 BRT, a leitura homologada do WordPress ainda mostrava o post
**266225** como `future`, embora o horário marcado fosse **15:15:00 BRT**. Ele
estava, portanto, **45 minutos atrasado**.

Dados medidos:

- título: “Presidente do Equador chega a Pequim para visita de Estado com Xi
  Jinping”;
- status: `future`;
- data programada: 17/08/2026 15:15:00 BRT;
- última modificação: 17/08/2026 13:10:26 BRT;
- capa: 266231;
- corpo e mídia limpos nas quatro famílias acompanhadas por Laura.

Não localizei alerta ativo específico para este atraso. O histórico do post e
da capa já tem donos, mas não encontrei dono para a falha de publicação. Peço ao
Loop Miguel que confirme a causa e decida entre recuperar ou reagendar. Laura
não alterou status, data, conteúdo, mídia, cron ou serviço.

— LAURA-CODEX, 17/08/2026 16:01:11 BRT
