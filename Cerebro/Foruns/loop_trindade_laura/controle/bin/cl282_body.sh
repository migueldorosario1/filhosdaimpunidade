
echo "=== CL-20260912-006 / cl282 — 270204 reescrita com os numeros da pesquisa e armada para 13:00 ==="
TZ=America/Sao_Paulo date
B=/root/backups_cl; mkdir -p "$B"; TS=$(TZ=America/Sao_Paulo date +%Y%m%d_%H%M%S)
$W post get 270204 --field=post_content > "$B/270204_antes_$TS.html"
echo "backup=$B/270204_antes_$TS.html"

# corpo novo: a peca da fabrica nao trazia UM UNICO numero da pesquisa que era o proprio assunto
$W post update 270204 /tmp/270204_novo.html >/dev/null && echo "CORPO_TROCADO"
echo -n "confere_numeros(esperado 5+)="; $W post get 270204 --field=post_content | grep -oE "18%|10%|7%|6%|1\.204|RJ-09217/2026" | wc -l

titulo 270204 "Benedita lidera com 18% a disputa por duas vagas ao Senado no Rio"

capa 270204 "https://upload.wikimedia.org/wikipedia/commons/d/d0/Brazilian_National_Congress.jpg" "As duas torres e as cupulas do Congresso Nacional, em Brasilia, sede do Senado Federal e da Camara dos Deputados, em foto de 2006. Foto: Wikimedia Commons (CC BY-SA 2.5)" "Vista do Congresso Nacional em Brasilia, com as duas torres ao centro e as cupulas dos plenarios dos lados, sob ceu nublado"

selo 270204 "Datafolha divulgado em 11/09/2026, contratado pela Globo e pela Folha de S.Paulo, com 1.204 entrevistados no Rio de Janeiro entre 8 e 10 de setembro, margem de 3 pontos para mais ou para menos, 95% de confianca, registro na Justica Eleitoral RJ-09217/2026. Cenario estimulado: Benedita da Silva (PT) 18%; Carlos Jordy (PL) e Carlos Portinho (PL) 10% cada; Pedro Paulo (PSD) e Marcelo Crivella (Republicanos) 7% cada; Monica Benicio (PSOL) 6%. Rodada anterior, de 21/08: Benedita 15%, Jordy e Portinho 8%. MOTIVO DA REESCRITA INTEGRAL: o rascunho da fabrica falava de uma pesquisa eleitoral SEM UM UNICO NUMERO - sem percentuais, sem entrevistados, sem margem, sem periodo e SEM O REGISTRO NO TSE, que a lei exige para divulgar pesquisa - e ainda dizia que faltavam «mais de dois meses» para o primeiro turno de outubro, o que e falso a 12 de setembro. Tirei tambem a especulacao em voz propria sobre o que Benedita «coloca em posicao de influenciar» e sobre o que «pode reorganizar o campo». Fontes: Poder360, Exame, Diario do Grande ABC e Agenda do Poder, 11/09/2026. DEDUPE: a casa nao publicou esta pesquisa."

entra 270204 "2026-09-12 13:00:00"

echo "--- depois ---"
echo "titulo=$($W post get 270204 --field=post_title)"
echo "thumb=$($W post meta get 270204 _thumbnail_id) status=$($W post get 270204 --field=post_status) date=$($W post get 270204 --field=post_date)"
echo -n "cl_manual="; $W post meta get 270204 _cafezinho_txt_check | grep -c cl_manual
echo "evento_db=$(tem_evento 270204)"
echo "--- a peca das 07:00 continua intacta ---"
echo "269908 status=$($W post get 269908 --field=post_status) date=$($W post get 269908 --field=post_date) thumb=$($W post meta get 269908 _thumbnail_id)"
