
echo "=== CL-20260911-002 / cl274 — 269858 para 16:00 ==="
TZ=America/Sao_Paulo date
# corrige o <p> duplicado na abertura (defeito de formatacao da fabrica)
$W post get 269858 --field=post_content > /tmp/c269858.html
head -c 12 /tmp/c269858.html; echo " <- antes"
sed -i '1s|^<p><p>|<p>|' /tmp/c269858.html
$W post update 269858 --post_content="$(cat /tmp/c269858.html)" >/dev/null && echo "CORPO_OK"
$W post get 269858 --field=post_content | head -c 12; echo " <- depois"
capa 269858 "https://upload.wikimedia.org/wikipedia/commons/c/c4/Edson_Fachin_%28cropped%29.jpg" "O ministro Edson Fachin, presidente do Supremo Tribunal Federal, em foto de 2018. Foto: Wikimedia Commons (CC BY 3.0 BR)" "Homem de toga preta, óculos e gravata vermelha, em retrato de rosto" "800x560+0+120"
selo 269858 "Pedido de Edson Fachin, presidente do STF, ao ministro Andre Mendonca em 10/09/2026, para levantamento PARCIAL do sigilo nos procedimentos do caso Banco Master que tramitam na Corte — mantendo sob reserva apenas o que possa comprometer diligencias futuras; o pedido nao retira o sigilo automaticamente (a decisao e do relator) e antecede a sessao extraordinaria de terca, 15/09, que examinara relatorio da PF; a casa vem cobrindo a serie (269650 de 09/09 e 268973 de 04/09), e esta e continuacao, nao repeticao; CORRIGI um defeito de formatacao da fabrica: o corpo abria com <p><p> duplicado"
entra 269858 "2026-09-11 16:00:00"
echo "post=269858 thumb=$($W post meta get 269858 _thumbnail_id) status=$($W post get 269858 --field=post_status) date=$($W post get 269858 --field=post_date) evento=$(tem_evento 269858)"
