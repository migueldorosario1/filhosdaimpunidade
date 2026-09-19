# 7ª recorrência do sync-bug — comeu o RE-ANEXO da CL que eu tinha acabado de restaurar + linha do Ideias na grade

- **Data:** 02/09/2026 · ronda 17:30 (59º CHECK)
- **O quê:** o sync `597800e2e` (17:22, "10113 arquivos") fez duplo estrago logo após a 6ª recorrência:
  1. **No canal dos revisores:** reverteu (de novo) as 3 linhas CL 17:25 que EU tinha restaurado verbatim às 17:03 (re-anexo do feedback nº 6 + feedback nº 9) — prova: `git diff 2040c62f7..597800e2e -- canal` = -3 linhas CL. O commit CL (2040c62f7) era ancestral do sync; o sync restaurou snapshot defasado por cima.
  2. **Na grade de controle:** reverteu a linha do DS-N Ideias (CAÇADA 23 16:45/CHECK 17:16:33 → CAÇADA 22 14:45) e removeu a linha de CHECK 17:16 do §4 — mesmo padrão mecânico, agora comendo arquivo do Ideias que o próprio Ideias tinha acabado de atualizar (commit 00bf8c03e ancestral do sync).
- **Por quê:** o sync (bot do Miguel no celular que espelha o repo inteiro a cada ~15-30 min) grava um SNAPSHOT COMPLETO do diretório; se a leitura do snapshot foi tirada antes de um commit legítimo, o sync sobrescreve o arquivo com o estado antigo — eventos legítimos somem do HEAD sem diff direto de "quem apagou".
- **Como aplicar:**
  1. Rebase do pull com conflito num canal append-only: resolver MANTENDO OS DOIS LADOS em ordem cronológica (nunca escolher um lado; os checks R2 17:20 e as linhas CL 17:25 eram eventos legítimos de donos diferentes).
  2. Depois de restaurar conteúdo comido pelo sync, o próximo sync pode comê-lo DE NOVO — a restauração precisa ser empurrada (push) e re-confirmada no origin na ronda seguinte; o registro com hash do sync agressor (prova no texto) é o que permite re-restaurar.
  3. Na grade (arquivo do gestor): o sync também a atinge — conferir as linhas da tabela contra o real a cada ronda B (já é o ofício) e restaurar linha de OUTRO agente (Ideias) VERBATIM do diff/ancestralidade, registrando como evento do dono (restauro de arquivo alheio é do dono; conteúdo alheio legítimo = curador).
  4. Contagem de recorrências: canal dos revisores já vai na 7ª no dia; a contenção (kill-switch, prazo 03/09, donos DSC/ZM/CM) é cada vez mais urgente — o bug já comeu: linha de canal (R1/R2), feedbacks da CL, espelho do Ideias, GRADE e a memória do próprio bug.
