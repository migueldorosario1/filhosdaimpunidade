
echo "=== CL-20260910-007 / cl255 — tarde do dia 10 ==="
TZ=America/Sao_Paulo date
echo "--- marcas temporais 269697:"; $W post get 269697 --field=post_content | tr ">" ">\n" | grep -nE "nesta|hoje|ontem|quarta|quinta" | head -4

# --- 269696 Santos x Atletico-MG — 14:30
$W post get 269696 --field=post_content > /tmp/c269696.html
sed -i 's/venceu o Atlético-MG por 2 a 0 nesta quarta-feira (9)/venceu o Atlético-MG por 2 a 0 na quarta-feira (9)/' /tmp/c269696.html
$W post update 269696 --post_content="$(cat /tmp/c269696.html)" >/dev/null && echo "CORPO_OK 269696"
$W post get 269696 --field=post_content | head -c 120; echo
capa 269696 "https://upload.wikimedia.org/wikipedia/commons/f/fb/Est%C3%A1dio_Urbano_Caldeira_-_Vila_Belmiro.jpg" "A Vila Belmiro, em Santos, em foto de 2015: foi ali que o Santos venceu o Atlético-MG por 2 a 0 na ida das quartas da Sul-Americana. Foto: Wikimedia Commons (CC BY-SA 4.0)" "Estádio de futebol vazio com arquibancadas em preto e branco e gramado iluminado"
selo 269696 "Jogo de ida das quartas de final da Copa Sul-Americana, 09/09/2026, Vila Belmiro: Santos 2 x 0 Atletico-MG, gols de Willian Arao e Oliva, com Gabigol participando dos dois; a peca ja traz a VOLTA (16/09, Arena MRV) e o saldo que o Santos pode perder — regra da casa para mata-mata; marca temporal ajustada para «na quarta-feira (9)» porque sai no dia 10"
entra 269696 "2026-09-10 14:30:00"

# --- 269697 Dmitriev x Financial Times — 16:00
titulo 269697 "Enviado de Putin acusa o Financial Times de sabotar diálogo com os EUA"
capa 269697 "https://upload.wikimedia.org/wikipedia/commons/2/2b/Kirill_Dmitriev_2018.jpg" "Kirill Dmitriev, enviado especial da Presidência russa e diretor do Fundo Russo de Investimento Direto, em foto de 2018. Foto: Wikimedia Commons (CC BY 4.0)" "Homem de terno cinza, gravata vermelha e óculos, em retrato de meio corpo" "856x600+0+150"
selo 269697 "Publicacao de Kiril Dmitriev na plataforma X reagindo a reportagem do Financial Times sobre John Ratcliffe (CIA) assumir papel maior nas negociacoes; a Casa Branca tambem rejeitou o relato e reafirmou Witkoff e Kushner; titulo passou a NOMEAR o jornal (era «jornal britanico»)"
entra 269697 "2026-09-10 16:00:00"

echo "=== FILA ==="
$W post list --post_status=future --fields=ID,post_date,post_title
