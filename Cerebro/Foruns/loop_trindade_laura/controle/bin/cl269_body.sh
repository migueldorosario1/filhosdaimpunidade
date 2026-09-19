
echo "=== CL-20260910-025 / cl269 — 269798 para hoje 19:00 ==="
TZ=America/Sao_Paulo date
capa 269798 "https://upload.wikimedia.org/wikipedia/commons/7/7d/Sede_do_Tribunal_Superior_Eleitoral%2C_em_Bras%C3%ADlia.jpg" "Sede do Tribunal Superior Eleitoral, em Brasília, em imagem de arquivo. Foto: Wikimedia Commons (CC BY-SA 4.0)" "Edifício curvo de vidro escuro com duas cúpulas brancas à frente, em Brasília"
selo 269798 "Sessao virtual do TSE de 09/09/2026, conduzida pelos ministros Dias Toffoli e Antonio Carlos Ferreira: registros aprovados de Renan Santos e Aroldo Medina (Missao), Clariana Barao e Fabiana Torquato (Democracia Crista) e Wilson Grassi e Sued Haidar (Democrata) — 11 das 13 chapas presidenciais ja tem registro, e faltam Augusto Cury/Julio Delgado (Avante) e Pablo Marcal/Leonardo Avalanche (PRTB); publicada HOJE, no dia seguinte a sessao, em encaixe as 19:00: fato de vespera em pauta eleitoral nao espera mais um dia"
entra 269798 "2026-09-10 19:00:00"
echo "post=269798 thumb=$($W post meta get 269798 _thumbnail_id) status=$($W post get 269798 --field=post_status) date=$($W post get 269798 --field=post_date) evento=$(tem_evento 269798)"
