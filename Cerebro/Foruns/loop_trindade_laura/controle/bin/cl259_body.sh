
echo "=== CL-20260910-013 / cl259 — 269727 para 21:00 ==="
TZ=America/Sao_Paulo date
titulo 269727 "Blairo Maggi diz que Bolsonaro pôs o agro em risco ao enfrentar a China"
capa 269727 "https://upload.wikimedia.org/wikipedia/commons/4/4a/Blairo_Maggi_em_junho_de_2019.jpg" "Blairo Maggi em audiência na Câmara dos Deputados, em junho de 2019. Foto: Cleia Viana/Câmara dos Deputados (CC BY 3.0)" "Homem de terno azul e gravata vermelha falando ao microfone em mesa de audiência"
selo 269727 "Fala de Blairo Maggi (acionista do Grupo Amaggi e ex-ministro da Agricultura) no painel «O agro brasileiro visto de fora», no Agro Summit do Bradesco BBI, Hotel Rosewood, Sao Paulo, hoje 10/09/2026 — evento, painel e local identificados no corpo; contexto do atrito com Pequim sob Ernesto Araujo («comunavirus», 2020) conferido no proprio texto; titulo passou a NOMEAR quem fala (era «Ex-ministro diz»), regra de nome + imputacao"
entra 269727 "2026-09-10 21:00:00"
echo "post=269727 thumb=$($W post meta get 269727 _thumbnail_id) evento=$(tem_evento 269727)"
echo "=== FILA ==="; $W post list --post_status=future --fields=ID,post_date --allow-root 2>/dev/null | head -12
