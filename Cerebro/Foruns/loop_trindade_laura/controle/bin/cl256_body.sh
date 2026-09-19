
echo "=== CL-20260910-008 / cl256 ==="
TZ=America/Sao_Paulo date
# sem sigla no titulo (ordem do Miguel): Atletico-MG -> Atletico Mineiro
titulo 269696 "Gabigol lidera Santos em vitória por 2 a 0 sobre o Atlético Mineiro"

# --- 269700 Petrobras/gasolina — 17:15
titulo 269700 "Gasolina não sobe na bomba: corte de tributos anula alta de R$ 0,63"
capa 269700 "https://upload.wikimedia.org/wikipedia/commons/9/9c/Petrobras-Rio.jpg" "A sede da Petrobras no centro do Rio de Janeiro, em foto de 2008. Foto: galio/Wikimedia Commons (CC BY-SA 2.0)" "Prédio modernista de fachada quadriculada com bandeiras hasteadas em frente e árvores ao redor" "960x700+0+150"
selo 269700 "Anuncio da Petrobras de 09/09/2026 confirmado por busca propria (InfoMoney/E-Investidor/Poder360: retirada do abatimento de R$ 0,44/L, acrescimo de R$ 0,19/L, preco de R$ 3,24/L as distribuidoras) e decreto federal que reduz PIS/Pasep e Cofins em R$ 0,63/L por 30 dias — o R1 marcou INCERTO por «escada de busca» indisponivel e a conferencia propria sustentou os numeros (3o caso do dia); titulo passou a dar a consequencia para o leitor (nao sobe na bomba) em vez do jargao de reajuste"
entra 269700 "2026-09-10 17:15:00"
echo "=== FILA ==="
$W post list --post_status=future --fields=ID,post_date,post_title
