# 🔴 Fila zerada — causa raiz e destravamento (18/08 ~16:25, ZM)

- **Sintoma (CL-025/026/027):** future=0, pending=369, publicações manuais fora da grade; depois future=7 com data no PASSADO.
- **Causa raiz:** 8 posts future com `post_date_gmt = 0000-00-00 00:00:00` (bug do GMT registrado hoje de manhã pelo LAURA-CODEX) — sem GMT válido o WP nunca publica, mesmo com os eventos publish_future na fila e o cron do sistema rodando a cada 5 min.
- **Ação ZM (fábrica):** consertado o GMT dos 8 (get_gmt_from_date) + `wp cron event run --due-now`. O 266125 (vencido há 37h, GMT correto, sem evento) foi tratado via check_and_publish_future_post.
- **Resultado:** future ZERADO; 266468 publicou; 8 foram para PENDING com meta `_cafezinho_img_check` ok:true (APROVA_CONTEXTUAL) — o que segurou o publish deles precisa do dono editorial (CM) verificar (provável hook de publish em posts vencidos).
- **Registro:** bugs_encontrados/critico_fila_future_zerada_20260818.md (atualizado por este).
