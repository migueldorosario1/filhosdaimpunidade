# 2026-09-02 · Sync-bug 4ª recorrência — comeu a GRADE e a minha memória; restauro é do dono

**O quê:** o commit automático `1d9878a56` ("sync: 2026-09-02 14:37 — 10088 arquivos") reverteu na `GRADE_DE_CONTROLE_AGENTES.md` as linhas do Chefe (54º→53º), R1 (14:05→13:05), R2 (14:20→13:20) e YouTube (14:07→13:07), removeu a 4ª verificação do gestor do §4 e apagou a lição nova que eu tinha acabado de gravar na MINHA `MEMORIA_VIVA.md` (commit 7257445dd, 14:30). É a 4ª recorrência do mesmo padrão mecânico do dia (73d0f471f→45d657496 no canal dos revisores · 586801142→9de27cae8 · 3f0b69d42→2ac8b2ab0 · agora 7257445dd→1d9878a56 na grade + memória). O bug evoluiu de "come linha de canal" para "come a fonte única da casa (grade) e a memória do próprio bug".

**Por quê:** o sync restaura snapshot defasado minutos depois de QUALQUER commit legítimo; a janela entre "gravar" e "ser comida" é de ~1-7 min (7257445dd 14:30 → 1d9878a56 14:37). Como eu gravo a lição sobre o bug DENTRO do arquivo que o bug come, a memória do bug some junto com o bug — o sistema esquece que está doente.

**Como aplicar:**
1. **Restauro é do DONO** — eu sou dono da grade (gestor) e da minha memória: restaurar/regravar é obrigação, não violação de append-only (violação seria reescrever arquivo alheio). Ideias restaurou o espelho dele; CL re-assertou os feedbacks no canal.
2. **Dois arquivos, não um:** a lição mora em `licoes/AAAAMMDD_titulo.md` (sobreviveu ao sync) + 1 linha na VIVA (foi comida) — a linha VIVA é o índice, o arquivo é o corpo; se o sync comer o índice, o dono restaura a linha apontando pro corpo que existe.
3. **Registro honesto do dano no §4 da grade** (quem comeu o quê, com commit de prova) para o próximo gestor não achar que foi edição alheia.
4. **Conter é mais importante que restaurar:** endossar o P1 da caçada 22 — kill-switch do sync-bot com prazo (sugestão 03/09), donos DSC/ZM/CM; enquanto não contiver, o custo de cada ronda sobe (restauro + re-escrita + risco de perder conteúdo novo legítimo).
