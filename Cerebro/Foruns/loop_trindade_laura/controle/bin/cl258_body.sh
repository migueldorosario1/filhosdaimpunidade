
echo "=== CL-20260910-010 / cl258 — 269713 para 19:45 ==="
TZ=America/Sao_Paulo date
$W post get 269713 --field=post_content > /tmp/c269713.html
sed -i 's/encerrou nesta quarta-feira (9)/encerrou na quarta-feira (9)/' /tmp/c269713.html
$W post update 269713 --post_content="$(cat /tmp/c269713.html)" >/dev/null && echo "CORPO_OK"
$W post get 269713 --field=post_content | head -c 110; echo
capa 269713 "https://upload.wikimedia.org/wikipedia/commons/9/91/Aldeia_Campista_subesta%C3%A7%C3%A3o.JPG" "Muro da subestação de Aldeia Campista, da Light, no Rio de Janeiro. Foto: Junius/Wikimedia Commons (CC BY-SA 3.0)" "Muro verde de subestação elétrica com a marca da Light e aviso de alta tensão"
selo 269713 "Sentenca da Justica do Rio de 09/09/2026 encerrando a recuperacao judicial da Light S.A. (LIGT3) e fato relevante da propria companhia declarando cumpridas as obrigacoes do plano no periodo de fiscalizacao; a peca mantem a ressalva de que ha etapas pendentes (conversao de debentures, bonus de subscricao e repasse do aumento de capital a Light Servicos de Eletricidade) — encerrar a fiscalizacao nao e encerrar a reorganizacao; marca temporal ajustada para «na quarta-feira (9)»"
entra 269713 "2026-09-10 19:45:00"
echo "post=269713 thumb=$($W post meta get 269713 _thumbnail_id) evento=$(tem_evento 269713)"
