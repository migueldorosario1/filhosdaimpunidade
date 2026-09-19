
echo "=== CL-20260909-020 / pacote cl249 — 269670 para 10/09 08:30 ==="
TZ=America/Sao_Paulo date

# ajuste da marca temporal: o fato e de quarta (9), a peca sai na quinta (10)
$W post get 269670 --field=post_content > /tmp/c269670.html
sed -i 's/nomeou nesta quarta-feira, 9,/nomeou na quarta-feira (9)/' /tmp/c269670.html
grep -c "nesta quarta-feira" /tmp/c269670.html
$W post update 269670 --post_content="$(cat /tmp/c269670.html)" >/dev/null && echo "CORPO_OK"
$W post get 269670 --field=post_content | head -c 130; echo

titulo 269670 "OpenAI põe Paul Christiano no comitê que decide lançamento de modelos"
selo 269670 "Busca propria 09/09 23:0x: o nome «Jacob Coxon» que o R1 deu como inexistente esta CORRETO — manchetes de Business Insider, Fortune e The Verge («Anthropic Researcher Jacob Coxon Resigns, Warns AI Industry Is Gambling With Our Lives»); a casa ja publicou o caso no 269570 (09/09 11:30). Nomeacao de Paul Christiano para o conselho da Fundacao OpenAI e para o Comite de Seguranca confirmada pelo R2, que sugeriu o nome no titulo. Marca temporal ajustada de «nesta quarta-feira, 9» para «na quarta-feira (9)» porque a peca sai no dia 10"
entra 269670 "2026-09-10 08:30:00"

echo "=== FILA FINAL ==="
$W post list --post_status=future --fields=ID,post_date,post_title
