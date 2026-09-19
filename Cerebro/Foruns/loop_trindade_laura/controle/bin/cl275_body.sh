
echo "=== CL-20260911-004 / cl275 — 269892 para 17:15 ==="
TZ=America/Sao_Paulo date
$W post get 269892 --field=post_content > /tmp/c269892.html
sed -i 's/pediu nesta quarta-feira (9)/pediu na quarta-feira (9)/' /tmp/c269892.html
$W post update 269892 --post_content="$(cat /tmp/c269892.html)" >/dev/null && echo "CORPO_OK"
$W post get 269892 --field=post_content | head -c 120; echo
titulo 269892 "Defesa de Cilia Flores pede prisão domiciliar por problemas cardíacos"
capa 269892 "https://upload.wikimedia.org/wikipedia/commons/9/97/Cilia_Flores_2013.jpg" "Cilia Flores em foto de 2013, quando era deputada na Venezuela. Foto: Wikimedia Commons (CC BY-SA)" "Mulher de óculos, cabelo escuro e echarpe vermelha, em retrato de meio corpo" "628x440+0+80"
selo 269892 "Peticao da defesa de Cilia Flores apresentada a Justica dos EUA na quarta-feira (9), pedindo substituicao da detencao no Centro Metropolitano de Detencao de Brooklyn por prisao domiciliar: 69 anos, perda de mais de 11 quilos, arritmias, dores no peito e dificuldade para respirar, com episodio de pressao no peito em 29 de julho e quatro medicamentos diarios, segundo os advogados; o pedido AINDA NAO FOI JULGADO e a peca diz isso; ela esta presa desde a operacao militar americana em Caracas de 3 de janeiro, quando foi capturada junto com Nicolas Maduro. CRITERIO: o fato e de quarta, mas processo pendente nao envelhece como evento — ontem barrei um jogo de futebol com dois dias pela razao inversa; marca temporal ajustada de «nesta quarta-feira» para «na quarta-feira (9)»"
entra 269892 "2026-09-11 17:15:00"
echo "post=269892 thumb=$($W post meta get 269892 _thumbnail_id) status=$($W post get 269892 --field=post_status) date=$($W post get 269892 --field=post_date) evento=$(tem_evento 269892)"
