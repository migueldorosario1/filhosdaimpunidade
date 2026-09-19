
echo "=== CL-20260910-020 / cl265 — colchao de 11/09: 02:30 e 05:30 ==="
TZ=America/Sao_Paulo date

capa 269758 "https://upload.wikimedia.org/wikipedia/commons/9/9d/Departure_lounge_of_Terminal_3_of_Sao_Paulo_Guarulhos_International_Airport_in_2025.jpg" "Sala de embarque do Terminal 3 do Aeroporto de Guarulhos, em foto de 2025. Foto: Wikimedia Commons (CC0)" "Corredor de terminal de aeroporto com passageiros e placas de portões de embarque"
selo 269758 "Politica Nacional Setorial de Identificacao Biometrica criada pelo Ministerio dos Portos e Aeroportos (MPor) para padronizar o uso de biometria em aeroportos, portos e terminais hidroviarios; execucao pelo Comite Tecnico Interinstitucional de Identificacao Biometrica, com plano em ate 90 dias; a peca registra que a norma tambem preve acompanhar a aplicacao e fiscalizar o tratamento dos dados — ressalva necessaria em materia de dado biometrico"
entra 269758 "2026-09-11 02:30:00"

capa 269719 "https://upload.wikimedia.org/wikipedia/commons/2/26/Sparkles_Beckett_LeClair_Better_Images_of_AI.png" "Ilustração de um servidor com o símbolo hoje usado para marcar recursos de inteligência artificial. Imagem: Beckett LeClair / Better Images of AI (CC BY 4.0)" "Desenho em traço preto de um gabinete de servidor com um post-it amarelo colado, com o ícone de brilhos"
selo 269719 "Peca sobre agentes de IA da OpenAI que usaram sites de terceiros para trocar mensagens entre si; RETIDA por mim as 09:42 de 10/09 por saturacao — teria sido a 3a peca sobre OpenAI/risco de IA em 24h, depois do 269570 (09/09) e do 269670 (10/09 08:30); liberada para 11/09 porque a dieta do dia muda; capa do projeto Better Images of AI, que existe justamente para ilustrar IA sem clique de robo"
entra 269719 "2026-09-11 05:30:00"

echo "=== COLCHAO 11/09 ==="
for id in 269716 269758 269719; do echo "post=$id thumb=$($W post meta get $id _thumbnail_id) status=$($W post get $id --field=post_status) date=$($W post get $id --field=post_date) evento=$(tem_evento $id)"; done
