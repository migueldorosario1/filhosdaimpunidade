
echo "=== CL-20260910-034 / cl272 — 269813 para 11/09 13:00 ==="
TZ=America/Sao_Paulo date
titulo 269813 "Secas põem 1.699 municípios, 30% do país, sob risco de falta d'água"
capa 269813 "https://upload.wikimedia.org/wikipedia/commons/e/e8/CAATINGA_bioma_brasileiro.jpg" "Vegetação de caatinga, bioma que cobre boa parte do Nordeste, em foto de 2017. Foto: Arturalveees/Wikimedia Commons (CC BY-SA 4.0)" "Paisagem de caatinga com árvores sem folhas, cactos e solo pedregoso"
selo 269813 "Analise do Observatorio do Clima a partir do AdaptaBrasil, plataforma do Ministerio da Ciencia, Tecnologia e Inovacao: 1.699 dos 5.569 municipios brasileiros (30,5%) com risco alto ou muito alto de falta d agua em periodos de seca; os 15 municipios de risco MUITO alto estao todos no Nordeste, em oito dos nove estados; a peca traz a ressalva metodologica correta — a classificacao mede RISCO (ameaca climatica + exposicao + capacidade de reagir) e nao falta d agua ja instalada; capa e caatinga brasileira, nao deserto estrangeiro"
entra 269813 "2026-09-11 13:00:00"
echo "post=269813 thumb=$($W post meta get 269813 _thumbnail_id) status=$($W post get 269813 --field=post_status) date=$($W post get 269813 --field=post_date) evento=$(tem_evento 269813)"
