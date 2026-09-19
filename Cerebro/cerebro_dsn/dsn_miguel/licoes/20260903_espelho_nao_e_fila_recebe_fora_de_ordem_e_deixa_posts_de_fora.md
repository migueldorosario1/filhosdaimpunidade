# 2026-09-03 · O espelho não é fila — recebe fora de ordem e deixa posts de fora

**O quê.** O espelho cafezinho.news não é uma fila cronológica atrasada do principal: recebe posts FORA de ordem e deixa outros de fora por horas. Prova per-ID da série DS-Dell (2ª confirmação em 14:31): o Ceará/AtlasIntel 268841 (principal 13:56) CHEGOU ao espelho (200) enquanto o HPV 268544 (principal 11:57 — 2h34 ausente), Netflix 268413 (12:37), Hepatite 268407 (12:57), Planta 268427 (13:17), Clipto 268557 (13:37) e ConvergeLab 268697 (13:58) seguem 404. Na 1ª confirmação (107º/108º, ~13:05-14:04): o TSE 268821 (12:17) chegou ao espelho com o HPV (11:57, ANTERIOR) ainda ausente. Um post posterior presente + um anterior ausente por 2h+ = não é atraso de fila, é seletividade/falha por post.

**Por quê.** O padrão se repete com leituras espaçadas (~30-60 min) e o espelho recebe alguns posts (TSE, Ceará) e descarta outros (HPV, Netflix, Hepatite, Planta, Clipto, ConvergeLab) sem relação com a ordem cronológica — mesmo com o principal 200 em todos. Causa-raiz é do dono (ZM acatou o watch: "registrar diagnóstico em sessão própria"); a lição aqui é do VIGIA: o sintoma "espelho atrasado" tem pelo menos 3 diagnósticos possíveis (stall seco, fila atrasada, seletividade por post) e só a sonda per-ID em série distingue.

**Como aplicar.**
1. Gap no espelho se prova com sonda per-ID (200/404 em `https://cafezinho.news/wp-json/wp/v2/posts/<ID>`), NUNCA com lista top-N (não mostra buraco no meio da série).
2. Distinguir "recente ausente" de "perdido": post com poucos minutos de vida 404 = em propagação (inconclusivo — o TSE levou ~48 min-1h18 para chegar; o Ceará 8-35 min) — só vira "perdido" com o par "anterior ausente + posterior presente" ou ausência >1-2h.
3. Marco de re-checagem em ~30 min (aqui: 15:00) para separar propagação de perda; registrar por post, não por janela.
4. Alerta sem alarme: registrar o padrão na ponte com prova per-ID e dono nomeado (ZM), sem re-alertar a cada leitura.

**Refs:** blocos DS-20260903-027/028/029 da ponte (de_dell.md) · ZM-20260903-075 (dono acatou o watch).
