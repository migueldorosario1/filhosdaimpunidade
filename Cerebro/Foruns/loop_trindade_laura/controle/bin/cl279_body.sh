
echo "=== CL-20260911-041 / cl279 — 269846: sai o endosso do jornal a fala do ministro ==="
TZ=America/Sao_Paulo date
TS=$(TZ=America/Sao_Paulo date +%Y%m%d_%H%M%S)
B=/root/backups_cl; mkdir -p "$B"
$W post get 269846 --field=post_content > "$B/269846_antes_$TS.html"
echo "backup=$B/269846_antes_$TS.html sha_antes=$(sha256sum "$B/269846_antes_$TS.html" | cut -c1-16)"
cp "$B/269846_antes_$TS.html" /tmp/269846_novo.html

# O jornal chancelava a fala do ministro. Os numeros regionais ja estao dois paragrafos acima;
# o leitor tira a conclusao sozinho. A fala continua atribuida a ele.
sed -i 's| Os números regionais sustentam a leitura, já que o salto se concentrou justamente nas regiões mais pobres do país\.||' /tmp/269846_novo.html

if grep -q "sustentam a leitura" /tmp/269846_novo.html; then
  echo "ABORTADO: a frase continua no arquivo — NADA gravado, post intacto"
else
  $W post update 269846 /tmp/269846_novo.html && echo "APLICADO"
  $W post meta update 269846 _cafezinho_revisao_pos "{\"ref\":\"CL-20260911-041\",\"origem\":\"auditoria propria CL — fila congelada do Astra; endosso do jornal a fala de autoridade\",\"decidiu\":\"CL\",\"backup\":\"$B/269846_antes_$TS.html\",\"ts\":\"$TS\"}"
fi
echo "--- readback: 0 = frase removida ---"
$W post get 269846 --field=post_content | grep -c "sustentam a leitura"
echo "--- a fala do ministro TEM de continuar la (1) ---"
$W post get 269846 --field=post_content | grep -c "George Santoro"
echo "status=$($W post get 269846 --field=post_status) thumb=$($W post meta get 269846 _thumbnail_id) date=$($W post get 269846 --field=post_date) autor=$($W post get 269846 --field=post_author)"
