
echo "=== CL-20260911-037 / cl278 — auditoria propria da 269964 pelo TESTE DE ATRIBUICAO (4 frases reprovadas) ==="
TZ=America/Sao_Paulo date
TS=$(TZ=America/Sao_Paulo date +%Y%m%d_%H%M%S)
B=/root/backups_cl; mkdir -p "$B"
$W post get 269964 --field=post_content > "$B/269964_antes_$TS.html"
echo "backup=$B/269964_antes_$TS.html sha_antes=$(sha256sum "$B/269964_antes_$TS.html" | cut -c1-16)"
cp "$B/269964_antes_$TS.html" /tmp/269964_novo.html

# 1. RISCO afirmado na voz do narrador -> atribuido a quem faz a alegacao (a propria empresa, que pede as regras por causa dele)
sed -i 's|<p>Sem controles externos, agentes capazes de executar tarefas podem|<p>Segundo a OpenAI, sem controles externos agentes capazes de executar tarefas podem|' /tmp/269964_novo.html
# 2. INTERPRETACAO em voz propria, e redundante com o paragrafo anterior -> sai a frase, fica o fato
sed -i 's|<p>A mudança funciona como reconhecimento do limite da autorregulação\. A mesma companhia|<p>A mesma companhia|' /tmp/269964_novo.html
# 3. OPINIAO EDITORIAL (o jornal dizendo o que os legisladores devem fazer) -> sai
sed -i 's| Ela reforça a necessidade de legisladores e órgãos públicos definirem os testes, os critérios de divulgação e as consequências para empresas que ocultem falhas graves\.||' /tmp/269964_novo.html
# 4. JUIZO sobre conflito de interesse em voz propria -> atribuido a quem defende a tese
sed -i 's| Avaliações conduzidas apenas pelas próprias desenvolvedoras preservam o conflito de interesse| Segundo a OpenAI, avaliações conduzidas apenas pelas próprias desenvolvedoras preservam o conflito de interesse|' /tmp/269964_novo.html

N=0
grep -q "Segundo a OpenAI, sem controles externos" /tmp/269964_novo.html && N=$((N+1))
grep -q "A mudança funciona como reconhecimento" /tmp/269964_novo.html || N=$((N+1))
grep -q "Ela reforça a necessidade de legisladores" /tmp/269964_novo.html || N=$((N+1))
grep -q "Segundo a OpenAI, avaliações conduzidas apenas" /tmp/269964_novo.html && N=$((N+1))
echo "trocas_aplicadas=$N (esperado 4)"
if [ "$N" -eq 4 ]; then
  $W post update 269964 /tmp/269964_novo.html && echo "APLICADO"
  $W post meta update 269964 _cafezinho_revisao_pos "{\"ref\":\"CL-20260911-037\",\"origem\":\"auditoria propria CL — teste de atribuicao (peca publicada sem R1/R2)\",\"decidiu\":\"CL\",\"backup\":\"$B/269964_antes_$TS.html\",\"ts\":\"$TS\"}"
else
  echo "ABORTADO: $N de 4 — NADA gravado, post intacto"
fi
echo "--- readback ---"
$W post get 269964 --field=post_content | grep -cE "Segundo a OpenAI"
$W post get 269964 --field=post_content | grep -cE "A mudança funciona como|Ela reforça a necessidade"
echo "status=$($W post get 269964 --field=post_status) thumb=$($W post meta get 269964 _thumbnail_id) date=$($W post get 269964 --field=post_date) autor=$($W post get 269964 --field=post_author)"
