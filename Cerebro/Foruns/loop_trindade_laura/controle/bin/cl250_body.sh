
echo "=== CL-20260910-002 / pacote cl250 — capas nas pecas que o guard §86 barrou ==="
TZ=America/Sao_Paulo date

# 269661 — perdeu 00:30 por falta de capa (guard §86 reverteu para draft); volta para 03:30
capa 269661 "https://upload.wikimedia.org/wikipedia/commons/2/23/Iwafune-oki_oil_platform_in_Japan.jpg" "Plataforma de petróleo no campo de Iwafune-oki, no Japão, em imagem de arquivo: a Chevron anunciou que dobrará o número de plataformas que opera na Venezuela. Foto: tsuda/Wikimedia Commons (CC BY-SA 2.0)" "Plataforma de petróleo isolada no mar, com torre de perfuração vermelha e branca"
entra 269661 "2026-09-10 03:30:00"

# 269659 — 05:30
capa 269659 "https://upload.wikimedia.org/wikipedia/commons/6/6c/Snellen_Chart_in_Nigeria_Hospital.jpg" "Tabela de acuidade visual na parede de um consultório de hospital na Nigéria: é o exame que muitas crianças autistas não conseguem concluir quando o ambiente não está adaptado. Foto: Beendy234/Wikimedia Commons (CC0)" "Quadro luminoso com letras em tamanhos decrescentes preso à parede de um consultório"
entra 269659 "2026-09-10 05:30:00"

# 269671 — 07:00 (retrato vertical recortado para paisagem)
capa 269671 "https://upload.wikimedia.org/wikipedia/commons/b/b7/Official_portrait_of_Secretary_Marco_Rubio%2C_January_2025.jpg" "Marco Rubio em retrato oficial de janeiro de 2025, quando assumiu a Secretaria de Estado dos EUA. Foto: Departamento de Estado dos Estados Unidos/Wikimedia Commons (domínio público)" "Homem de terno azul-escuro e gravata azul diante de uma bandeira dos Estados Unidos" "2182x1500+0+250"
entra 269671 "2026-09-10 07:00:00"

echo "=== CONFERENCIA ==="
for id in 269661 269672 269659 269671 269670; do echo "post=$id thumb=$($W post meta get $id _thumbnail_id) status=$($W post get $id --field=post_status) date=$($W post get $id --field=post_date)"; done
