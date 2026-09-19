
echo "=== CL-20260912-002 / cl280 — 269908 resgatada do retido, vestida e armada para 07:00 ==="
TZ=America/Sao_Paulo date
echo "--- antes ---"
echo "titulo=$($W post get 269908 --field=post_title) status=$($W post get 269908 --field=post_status) thumb=$($W post meta get 269908 _thumbnail_id)"

titulo 269908 "Brasil negocia status de parceiro pleno do bloco do Sudeste Asiático"

capa 269908 "https://upload.wikimedia.org/wikipedia/commons/8/84/Containers_no_Porto_de_Salvador%2C_BA.jpg" "Conteineres empilhados no terminal do Porto de Salvador, na Bahia, com o casario da cidade ao fundo, em foto de 2023. Foto: Wikimedia Commons (CC BY-SA 4.0)" "Pilhas de conteineres coloridos e porticos de um terminal portuario a beira-mar, com colina, casario e uma igreja ao fundo"

selo 269908 "Viagem do chanceler Mauro Vieira ao Sudeste Asiatico para negociar a elevacao do Brasil a Parceiro de Dialogo Pleno da Asean, com escala em Singapura e pedido de reabertura do mercado tailandes a carne brasileira, fechado desde 2024. A PENDENCIA DO R1 FOI RESOLVIDA A MAO NESTA MADRUGADA: a cupula de 10 a 12 de novembro nas Filipinas esta confirmada, e o governo avalia que a aceitacao pode sair nela ou a partir de janeiro de 2027, quando Singapura assume a presidencia do bloco (Agencia Brasil, 10/09/2026: https://agenciabrasil.ebc.com.br/internacional/noticia/2026-09/brasil-vai-ao-sudeste-asiatico-mirando-virar-parceiro-pleno-da-asean). CRITERIO: peca RETIDA em 11/09 05:21 por falta de capa e pelo dado nao confirmado, nao por qualidade - o texto declara a propria limitacao ao comparar cinco mercados da Asean com cinco do G7, o que e o oposto do que corrigi ontem em outras pecas. TITULO trocado para tirar a sigla e nao prometer adesao: e parceiro de dialogo pleno, NAO membro do bloco. DEDUPE: a casa nao publicou este fato."

entra 269908 "2026-09-12 07:00:00"

echo "--- depois (tem de estar tudo preenchido) ---"
echo "titulo=$($W post get 269908 --field=post_title)"
echo "thumb=$($W post meta get 269908 _thumbnail_id) status=$($W post get 269908 --field=post_status) date=$($W post get 269908 --field=post_date)"
echo -n "cl_manual_gravado="; $W post meta get 269908 _cafezinho_txt_check | grep -c cl_manual
echo -n "isenta="; $W post meta get 269908 _cafezinho_txt_isenta | head -c 80; echo
echo "evento_db=$(tem_evento 269908)"
