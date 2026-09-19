
echo "=== CL-20260910-027 / cl270 — 269801 para 11/09 10:00 ==="
TZ=America/Sao_Paulo date
capa 269801 "https://upload.wikimedia.org/wikipedia/commons/9/9e/Mammographe_et_un_paravent_plomb%C3%A9_de_protection_contre_les_rayon-X_dans_un_h%C3%B4pital_au_B%C3%A9nin.jpg" "Aparelho de mamografia e biombo de proteção contra raios X em um hospital, em imagem de arquivo. Foto: Wikimedia Commons (CC BY-SA 4.0)" "Equipamento de mamografia branco e rosa ao lado de um biombo de proteção, em sala de exame" "2788x1900+0+900"
selo 269801 "Decisao da ANS de 03/09/2026, anunciada em 10/09: a partir de 1o de outubro os planos de saude passam a cobrir mamografia digital para qualquer pessoa com indicacao medica, caindo o limite de 40 a 69 anos — alcanca homens, mulheres e pessoas nao binarias; origem na Comissao de Atualizacao do Rol de Procedimentos; capa e aparelho de mamografia em hospital, declarado na legenda como imagem de arquivo e SEM pacientes"
entra 269801 "2026-09-11 10:00:00"
echo "post=269801 thumb=$($W post meta get 269801 _thumbnail_id) status=$($W post get 269801 --field=post_status) date=$($W post get 269801 --field=post_date) evento=$(tem_evento 269801)"
