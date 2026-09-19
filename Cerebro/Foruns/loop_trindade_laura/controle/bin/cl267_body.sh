
echo "=== CL-20260910-023 / cl267 — Brent hoje 17:45 e Cerrado amanha 07:00 ==="
TZ=America/Sao_Paulo date

titulo 269772 "Brent sobe 6,34% com guerra ao Irã e pressiona combustíveis"
capa 269772 "https://upload.wikimedia.org/wikipedia/commons/7/7d/Blue_hour_fog_over_Preemraff_oil_refinery_by_Brofjorden.jpg" "Refinaria de petróleo de Preemraff, em Brofjorden, na Suécia, ao anoitecer, em imagem de arquivo. Foto: Wikimedia Commons (CC BY-SA 4.0)" "Refinaria iluminada à beira de uma baía, refletida na água, no fim da tarde" "5700x3204+2600+0"
selo 269772 "Fechamento de 10/09/2026: Brent para novembro +6,34% a US$ 107,63 na ICE de Londres (maior valor desde maio de 2026) e WTI para outubro +6,7% a US$ 102,48 em Nova York; alta acumulada de 18% em setembro; causa declarada no texto: perspectiva de guerra prolongada dos EUA contra o Ira. NAO e boletim de mercado seco: a peca liga o preco internacional ao repasse a combustiveis e fretes no Brasil, com a ressalva do cambio e da capacidade das refinarias — e completa o 269700 das 17:15 (corte de tributos que segura a bomba). Ordem do Miguel sobre nota de banco respeitada: entra pelo gancho e pela consequencia, nao pela cotacao"
entra 269772 "2026-09-10 17:45:00"

titulo 269770 "Centro de dados de IA de 1 gigawatt ameaça a água do Cerrado em Paracatu"
capa 269770 "https://upload.wikimedia.org/wikipedia/commons/9/98/Cern_datacenter.jpg" "Corredor de servidores do centro de dados do CERN, na Suíça, em imagem de arquivo: o projeto anunciado para Paracatu terá 1 gigawatt de potência. Foto: Wikimedia Commons (CC BY-SA 3.0)" "Fileiras de racks de servidores em sala de centro de dados"
selo 269770 "Projeto da Atlas Renewable Energy para um centro de dados de IA de 1 GW em Paracatu, noroeste de Minas Gerais; a peca contrapoe o argumento da empresa (agua abundante) a fala do ex-prefeito Almir Paraca sobre conflitos hidricos antigos e ao dado de que cerca de 80% do territorio do municipio enfrenta conflito pela agua, com demanda acima das reservas subterraneas; capa e ilustracao declarada (data center do CERN), porque nao ha foto do projeto"
entra 269770 "2026-09-11 07:00:00"

echo "=== CONFERENCIA ==="
for id in 269772 269770; do echo "post=$id thumb=$($W post meta get $id _thumbnail_id) status=$($W post get $id --field=post_status) date=$($W post get $id --field=post_date) evento=$(tem_evento $id)"; done
