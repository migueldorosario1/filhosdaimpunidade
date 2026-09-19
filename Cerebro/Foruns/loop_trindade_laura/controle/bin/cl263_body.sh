
echo "=== CL-20260910-019 / cl263 — 269716 corrigido e armado para 11/09 00:30 ==="
TZ=America/Sao_Paulo date
$W post get 269716 --field=post_content > /tmp/c269716.html
sed -i 's|A provável visita do presidente chinês, Xi Jinping, a Nova Délhi no fim de semana de 12 e 13 de setembro pode abrir|A visita do presidente chinês, Xi Jinping, a Nova Délhi no fim de semana de 12 e 13 de setembro, confirmada pelo Ministério das Relações Exteriores da China, pode abrir|' /tmp/c269716.html
sed -i 's|Xi é esperado na cúpula anual do BRICS, em sua primeira viagem à Índia desde 2019. Pequim ainda não confirmou a presença do presidente nem um encontro bilateral com o primeiro-ministro Narendra Modi, decisão que definirá o alcance político da visita.|Xi participará da cúpula anual do BRICS em sua primeira viagem à Índia desde 2019, com chegada prevista para 12 de setembro. Pequim ainda não anunciou um encontro bilateral com o primeiro-ministro Narendra Modi, decisão que definirá o alcance político da visita.|' /tmp/c269716.html
grep -c "provável visita\|ainda não confirmou a presença" /tmp/c269716.html
$W post update 269716 --post_content="$(cat /tmp/c269716.html)" >/dev/null && echo "CORPO_OK"
$W post get 269716 --field=post_content | head -c 210; echo
titulo 269716 "Xi vai à Índia na cúpula do BRICS e testa degelo com Nova Délhi"
entra 269716 "2026-09-11 00:30:00"
echo "post=269716 thumb=$($W post meta get 269716 _thumbnail_id) evento=$(tem_evento 269716)"
