
echo "=== CL-20260909-019 / pacote cl248 — colchao da madrugada 10/09 ==="
TZ=America/Sao_Paulo date

# --- 269661 Chevron/Venezuela — 00:30
titulo 269661 "Chevron dobrará plataformas na Venezuela e mira 600 mil barris por dia"
selo 269661 "Reuters 08/09/2026 (anuncio de Eimear Bonner, CFO, na conferencia do Barclays) + Seeking Alpha 08/09/2026 + arquivo da casa sobre a captura de Maduro (posts 224124 de 09/01/2026 e 228979 de 26/03/2026) — R1 marcou INCERTO a data de janeiro por limite de busca; o arquivo do proprio site sustenta a premissa"
entra 269661 "2026-09-10 00:30:00"

# --- 269672 tovaca-de-baturite — 02:30 (com capa)
titulo 269672 "Canto revela nova espécie de ave na Serra de Baturité, no Ceará"
capa 269672 "https://upload.wikimedia.org/wikipedia/commons/5/53/Chamaeza_campanisona.jpeg" "Tovaca-campainha (Chamaeza campanisona) no Parque Estadual Intervales, em São Paulo, em 2009: a população da Serra de Baturité foi separada dessa espécie e descrita como Chamaeza baturitensis. Foto: Carlos Henrique Luz Nunes de Almeida/Wikimedia Commons (CC BY 3.0)" "Ave marrom de peito listrado em preto e branco caminhando sobre folhas secas no chão da mata"
selo 269672 "O Eco, Diario do Nordeste, O Povo e Revista Forum (183 gravacoes, 134 exemplares, Unesp de Botucatu; segunda especie endemica do Ceara ao lado do soldadinho-do-araripe) — capa e da especie-irma C. campanisona, declarado na legenda"
entra 269672 "2026-09-10 02:30:00"

# --- 269659 exame ocular / autismo — 05:30
selo 269659 "70o Congresso Brasileiro de Oftalmologia (CBO), Salvador, 09/09/2026 — fala da oftalmologista Raira Fortuna; os numeros de estrabismo (41% x 3%) e de capacitacao (menos de 4%) estao atribuidos no corpo a estudos citados pela medica, sem afirmacao propria da casa"
entra 269659 "2026-09-10 05:30:00"

# --- 269671 Rubio/Venezuela — 07:00
titulo 269671 "Rubio condiciona eleições na Venezuela à reconstrução de instituições"
selo 269671 "Busca propria 09/09 22:2x confirmou a visita a Barranquilla e a fala sobre eleicoes (El Tiempo, Infobae, El Nacional, Semana) + arquivo da casa: posse de Abelardo de la Espriella (post 264433, 05/08/2026) e coalizao militar dos EUA na regiao (post 267271, 23/08/2026) — R1 marcou INCERTO por limite de busca"
entra 269671 "2026-09-10 07:00:00"

echo "=== FILA FINAL ==="
$W post list --post_status=future --fields=ID,post_date,post_title
