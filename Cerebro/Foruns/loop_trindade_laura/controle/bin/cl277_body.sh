
echo "=== CL-20260911-031 / cl277 — correcao POS-PUBLICACAO em 269892 (achados 1, 2 e 3 do XM-20260911-033, acatados pela CL) ==="
TZ=America/Sao_Paulo date
TS=$(TZ=America/Sao_Paulo date +%Y%m%d_%H%M%S)
B=/root/backups_cl; mkdir -p "$B"
$W post get 269892 --field=post_content > "$B/269892_antes_$TS.html"
echo "backup=$B/269892_antes_$TS.html sha_antes=$(sha256sum "$B/269892_antes_$TS.html" | cut -c1-16)"
cp "$B/269892_antes_$TS.html" /tmp/269892_novo.html

# 1. conclusao clinica na voz do narrador -> atribuida a defesa
sed -i 's|<p>A permanência no presídio eleva o risco de agravamento|<p>Segundo a defesa, a permanência no presídio eleva o risco de agravamento|' /tmp/269892_novo.html
# 2. comparacao sem base ("mais rigida do que em muitos casos") -> sai a comparacao, fica o fato
sed -i 's| O desenho proposto reduz o argumento de risco de fuga ao aceitar uma custódia privada mais rígida do que as condições aplicadas em muitos casos de liberdade sob fiança\.| A defesa apresentou essas medidas para responder ao argumento de risco de fuga.|' /tmp/269892_novo.html
# 3. previsao sobre sequencia judicial sem documento -> fato verificavel
sed -i 's|<p>A decisão sobre a prisão domiciliar virá antes dessa disputa mais ampla\.|<p>O pedido de prisão domiciliar aguarda decisão.|' /tmp/269892_novo.html

N=$(grep -c "Segundo a defesa, a permanência\|A defesa apresentou essas medidas\|O pedido de prisão domiciliar aguarda decisão" /tmp/269892_novo.html)
echo "trocas_aplicadas=$N (esperado 3)"
if [ "$N" -ge 3 ]; then
  $W post update 269892 /tmp/269892_novo.html && echo "APLICADO"
  $W post meta update 269892 _cafezinho_revisao_pos "{\"ref\":\"CL-20260911-031\",\"origem\":\"XM-20260911-033 achados 1,2,3\",\"decidiu\":\"CL\",\"backup\":\"$B/269892_antes_$TS.html\",\"ts\":\"$TS\"}"
else
  echo "ABORTADO: so $N das 3 trocas casaram — NADA gravado, post intacto"
fi
echo "--- readback (tem de mostrar as 3) ---"
$W post get 269892 --field=post_content | grep -nE "Segundo a defesa|A defesa apresentou essas medidas|aguarda decisão" | cut -c1-190
echo "--- a peca NAO pode ter mudado de status nem de capa ---"
echo "status=$($W post get 269892 --field=post_status) thumb=$($W post meta get 269892 _thumbnail_id) date=$($W post get 269892 --field=post_date) autor=$($W post get 269892 --field=post_author)"
