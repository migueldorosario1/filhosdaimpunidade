
echo "=== CL-20260910-003 / pacote cl252 — manha do dia 10 ==="
TZ=America/Sao_Paulo date

# --- 269678 Anvisa/meningite — 10:00
capa 269678 "https://upload.wikimedia.org/wikipedia/commons/e/e6/Neisseria_meningitidis_CSF_Gram_1000.jpg" "Neisseria meningitidis vista ao microscópio em amostra de líquido cefalorraquidiano, com coloração de Gram: é a bactéria contra cujos sorogrupos A, C, W e Y a vacina protege. Imagem: Microman12345/Wikimedia Commons (CC BY-SA 4.0)" "Micrografia com bactérias em pares, em roxo, entre células de defesa coradas em rosa"
selo 269678 "Bahia Noticias e MSN/Agencia Brasil 09/09/2026 (ampliacao da indicacao da MenQuadfi para bebes a partir de 6 semanas); R1 aprovou com fatos centrais confirmados; o texto ja traz a ressalva de que aprovacao na Anvisa nao e incorporacao ao SUS"
entra 269678 "2026-09-10 10:00:00"

# --- 269679 Netanyahu x Haaretz — 11:30
$W post get 269679 --field=post_content > /tmp/c269679.html
sed -i 's/disse nesta quarta-feira (9)/disse na quarta-feira (9)/' /tmp/c269679.html
$W post update 269679 --post_content="$(cat /tmp/c269679.html)" >/dev/null && echo "CORPO_OK"
$W post get 269679 --field=post_content | head -c 120; echo
titulo 269679 "Netanyahu processará o Haaretz por reportagem sobre alerta antes do 7 de Outubro"
capa 269679 "https://upload.wikimedia.org/wikipedia/commons/8/82/Donald_Trump_and_Benjamin_Netanyahu_at_White_House_2025_%283%29_%28cropped%29_%28cropped%29.jpg" "Benjamin Netanyahu em reunião na Casa Branca, em 2025. Foto: Dan Scavino/Casa Branca (domínio público)" "Homem de terno escuro e gravata vermelha sentado em poltrona, de perfil" "430x560+0+290"
selo 269679 "Anuncio do processo feito por Netanyahu em 09/09/2026 (quarta-feira), contra o Haaretz e os autores Shlomi Eldar e Ruth Yaval, sobre reportagem de 08/09; marca temporal ajustada de «nesta quarta-feira» para «na quarta-feira (9)» porque a peca sai no dia 10; titulo passou a nomear o fato (reportagem sobre alerta antes do 7 de Outubro) em vez de «relato sobre alerta»"
entra 269679 "2026-09-10 11:30:00"

echo "=== FILA ==="
$W post list --post_status=future --fields=ID,post_date,post_title
