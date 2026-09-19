
echo "=== CL-20260911-001 / cl273 — 269846 para 11/09 14:30 ==="
TZ=America/Sao_Paulo date
capa 269846 "https://upload.wikimedia.org/wikipedia/commons/b/b7/Cnh_brasil_2007_generica.png" "Modelo de Carteira Nacional de Habilitação com os dados apagados, em imagem de arquivo. Imagem: Wikimedia Commons (domínio público)" "Documento de habilitação brasileiro com os campos de dados pessoais borrados"
selo 269846 "Dados do Ministerio dos Transportes sobre os primeiros nove meses do programa CNH do Brasil (regras em vigor desde dezembro de 2025): pedidos de nova habilitacao de 2,3 milhoes para 7,3 milhoes entre janeiro e agosto (+216% sobre 2025), mais de 2 milhoes de habilitados no periodo e economia de R$ 9,64 bilhoes aos condutores ate agosto; capa e modelo generico de CNH com os dados APAGADOS — documento de identidade nunca vai a capa com dado legivel"
entra 269846 "2026-09-11 14:30:00"
echo "post=269846 thumb=$($W post meta get 269846 _thumbnail_id) status=$($W post get 269846 --field=post_status) date=$($W post get 269846 --field=post_date) evento=$(tem_evento 269846)"
