---
name: Fórum Lula auditado — 6 ajustes aceitos por Antigravity
description: Forum_lula.md (proposta Agente Lula "Olhar do Stuckert") auditado por Claude Code com 6 ajustes (F1-F6); Antigravity aceitou; aguarda aval Miguel pra codar
type: project
originSessionId: da85d7d2-f66a-4b5a-b9db-6d27f8e11791
---
Antigravity propôs em 2026-04-20 o **Agente Lula** ("Olhar do Stuckert") em `root/forum_lula.md`: regra editorial é que post só existe se houver foto Flickr oficial pareada. Trindade-style (coletor + master separados).

Claude Code auditou e anexou §4 com 6 ajustes obrigatórios:
- **F1** Schema real do `banco_imagens_reais.db` é `(id, origem, url_alta, data_foto, titulo, descricao, tags, termo, coletado_em)` — não `data_upload` como Antigravity escreveu.
- **F2** Waiting Room é overengineering — `robo_coleta_flickr_rapido.py` já roda /10min (80 fotos Lula/Planalto no banco hoje). Master só re-tenta no próximo ciclo.
- **F3** Falta gancho com `taxonomia_wordpress.json` (categoria `politica` + tag `lula`).
- **F4** Conflito real com `agente_master_nacional.py` + `agente_repetidor_estatal.py`. Regra dura: Lula tem prioridade SE sujeito gramatical = Lula/Presidente/Planalto E foto Stuckert ≤36h. Antiduplicação Jaccard ≥0.6 vs trends + últimos 20 posts WP categoria política.
- **F5** Persona "Testemunha Ocular" choca com regras V9 (proíbe adjetivos vagos). Reescrever como tom factual descritivo da imagem.
- **F6** "Veto Flickr 90% do tempo" arbitrário → regra binária: doméstica=Flickr obrigatório; internacional=libera Wikimedia/contas oficiais estrangeiras.

**Plano de execução proposto** (após aval Miguel):
1. `robo_coleta_lula.py` — RSS Planalto + Agência Brasil + Brave "Lula" 24h. Banco `banco_artigos_brutos_lula.json` com `origem="lula"`.
2. `agente_master_lula.py` — anti-dup, classifica doméstica/internacional, query SQLite por foto compatível, roteia LLM, motor_publicador.
3. Drafts em controle.ocafezinho.com primeiro, sem deploy direto.
4. Cron `0 8,12,16,20 * * *` (4x/dia, fora da madrugada).

**Status 2026-04-20**: Antigravity aceitou os 6 ajustes. Miguel ainda não deu aval explícito pra começar a codar. Nada foi escrito ainda em `robo_coleta_lula.py` ou `agente_master_lula.py`.
