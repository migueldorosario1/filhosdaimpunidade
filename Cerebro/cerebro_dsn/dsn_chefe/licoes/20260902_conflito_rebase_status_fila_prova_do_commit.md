# Conflito de rebase em fila de STATUS: resolve pela PROVA do commit, não pela ordem de chegada

**Data:** 2026-09-02 (ronda 64º)
**O quê:** no `git pull --rebase` da ronda 20:00, a fila `youtube/queue_youtube.md` conflitou com duas versões do MESMO vídeo (BWAEcQThHGE e mnQ-Cf5YphQ): um lado dizia `STATUS: ERRO`, o outro `STATUS: BAIXADO`, trocados entre as linhas. Cada lado parecia "a verdade" na sua máquina.

**Por quê:** dois robôs (DS YouTube aqui + sync/origin) escreveram status diferentes nas mesmas linhas em janelas próximas; o 3-way merge não tem como saber qual é o estado real do download — status é dado de MUNDO EXTERNO (o arquivo baixou?), não de texto.

**Como aplicar (a técnica):**
1. Nunca resolver "olhando" qual lado parece mais novo — status de fila não é opinião, é FATO de mundo.
2. Procurar a prova: `git log --oneline --all -S <videoId> -- <arquivo>` + `git show <commit> --stat` → o commit com mensagem `porta-download: <id> -> BAIXADO` É a prova de que o download terminou (o robô só commita BAIXADO depois do arquivo fechado).
3. No caso, os dois vídeos tinham commit-mensagem de BAIXADO (942233402 para BWAE, edba17bf4 para mnQ no origin) → resolver mantendo `BAIXADO` nos dois (estado terminal bom; o robô re-verifica se algo falhou depois).
4. Registrar a resolução no bloco da ronda (append-only) para o próximo conflito não repetir a dúvida.

**Verificação:** `git log --oneline -1` limpo pós-rebase + fila com os dois BAIXADO + push aceito.
