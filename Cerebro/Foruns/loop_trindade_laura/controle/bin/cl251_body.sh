
echo "=== CL-20260910-002 / pacote cl251 — capa do 269670 ==="
capa 269670 "https://upload.wikimedia.org/wikipedia/commons/3/33/Pioneer_Building%2C_San_Francisco_%282019%29_-1.jpg" "O Pioneer Building, em San Francisco, em foto de 2019, quando abrigava os escritórios da OpenAI e da Neuralink. Foto: HaeB/Wikimedia Commons (CC BY-SA 4.0)" "Prédio histórico de três andares em esquina arborizada de San Francisco, com o nome Pioneer Building pintado na fachada"
entra 269670 "2026-09-10 08:30:00"
echo "=== FILA FINAL ==="
for id in 269672 269661 269659 269671 269670; do echo "post=$id thumb=$($W post meta get $id _thumbnail_id) status=$($W post get $id --field=post_status) date=$($W post get $id --field=post_date) evento=$(tem_evento $id)"; done
