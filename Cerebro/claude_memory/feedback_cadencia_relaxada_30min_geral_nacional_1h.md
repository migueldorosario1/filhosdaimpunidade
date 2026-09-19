---
name: feedback-cadencia-relaxada-30min-geral-nacional-1h
description: "14/08/2026 ~12:50 BRT: cadência editorial relaxada pós-reforma do site — verticais gerais 1 post/30min, Nacional e Regional máx 1/h, excesso publica mesmo e entra em cat No home (20699) soltando pra home pela rotação de 3h. SUPERSEDE a regra de 60-90min de 12/08"
metadata:
  type: feedback
---

**NOVA CADÊNCIA EDITORIAL — ordem do Miguel, 14/08/2026 ~12:20 BRT (áudio).** O site foi reformado e tem blocos por vertical, então aguenta ritmo maior de publicação. A regra anterior de 60-90min ([[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]], 12/08) está **SUPERSEDDA** — era anti-churn do site pré-reforma.

**Regra nova:**
1. **Verticais gerais** (Geo, Ciência/Tec, Economia, Esporte, Cultura, Saúde, Meio-Amb...): **1 post a cada 30 min**.
2. **Nacional e Regional**: calmos — **máx. 1 por hora** ("o nacional não fica muito agitado").
3. **Preferência: publicar a agora > agendar pra frente.** Em vez de empilhar slots futuros (texto envelhecendo na fila), publica e controla a exposição pelo home.
4. **Se ficar muito junto** (mais posts que a cadência permite): publica mesmo assim e **aplica cat No home (20699) no excesso** — a rotação solta pra home depois. Isso re-ativa o 20699 como **válvula de rotação** (modifica a regra "V4 sem no-home" de 13/08 14:22, que volta a valer só como DEFAULT de entrada direta na home).
5. **Rotação do home: 3h** — `remover_no_home.py` (cron horário no NYC, `0 * * * *`) agora com `NO_HOME_TEMPO_ESPERA=3` (era 4; foto real verificada continua 1h). Post flagado entra na home ~3h depois de publicado.

**Why:** Miguel 14/08: fila de 30 posts ia até 16/08 com texto envelhecendo 24-40h ("não fazia sentido... daqui a dois dias"). Produção V4 (~36+/dia) > gotejamento 60-90min (~20/dia) fazia a fila só crescer. Com blocos por vertical + rotação de 3h, o site absorve ritmo maior sem empilhar texto velho.

**How to apply (V6/Vigília-Trindade):**
- Agendar/produzir nos ritmos de cima; se acumular, publicar com 20699 no excesso em vez de marcar slot pra 2 dias depois.
- Agendamento WP continua exigindo `edit_date=true` ([[feedback-wp-update-post-edit-date-obrigatorio-para-agendamento]]).
- Nacional = cat 22 (e subcats); Regional = categorias de estado (árvore do menu 21062).
- Texto que ficaria >1 dia na fila: considerar rewrite de gancho ou descarte, não slot distante.

**Execuções de 14/08 (~12:20-12:50 BRT, ZCode/GLM-5.2):**
- 40 zumbis `future` de 2025 (missed schedule) → lixo (recover 30d).
- Fila de 27 posts (14/08 12:30→16/08 04:00) **compactada para hoje 14/08 13:00→21:30** (geral :00/:30 · Nacional :15). Backup: `Cerebro/backups_pre_edit/2026-08-14_1245_compactacao_fila_27posts.json`.
- `NO_HOME_TEMPO_ESPERA=3` no `/root/chaves.sh` do NYC (backup `chaves.sh.bak_pre_nohome3h_20260814`); cleaner confirmado rodando de hora em hora.
- Pendente decisão Miguel: 5 zumbis de 2026 (jun/jul: 260928, 261247, 261446, 261880, 261886).

Regra irmã: [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] (superseddida — manter por histórico) · [[feedback-nunca-churn-publish-draft-seo]].
