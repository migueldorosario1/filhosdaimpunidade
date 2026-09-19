---
name: feedback-janitor-banco-midia-protocolo-20260621
description: "Protocolo de janitor do banco de mídia Tencent: SQL isolado em arquivo (não heredoc SSH), algoritmo em 3 níveis (órfãs/cascade/dedup/cap), swap atômico com rollback 7d, backup triple local+tar.gz+B2 antes de qualquer DELETE."
metadata:
  type: feedback
  originSessionId: 831ab0d8-9f43-4146-9bf9-65f536fabdf7
---

Protocolo de janitor do banco de mídia (`/root/agent_data/banco_midia/banco_imagens_reais.db` em Tencent `43.156.151.165`) — janitor aplicado com sucesso 21/06 22:20 BRT reduzindo 535M→372M (-30,5%, 168.791 imagens órfãs +30d removidas).

**Why:** Caso fundador 21/06 — Miguel pediu *"backup e tente produzir uma versão limpa desse banco de mídia"*. Bypassando todas as etapas que aprendi no erro: heredoc SSH com `datetime("now", ...)` falha com parse error `unrecognized token: "\"` porque aspas duplas outer do SSH fecham nas aspas duplas inner do SQL. Solução é **subir arquivo `.sql` separado via scp** (`scp -P 38422 janitor.sql ubuntu@...:/home/ubuntu/`, **NÃO `/tmp/`** que falha com "No such file or directory" — usar `$HOME` sempre) e aplicar com `sudo sqlite3 .clean < /home/ubuntu/janitor.sql`. Já cp local era 535M mas perdi 1h até descobrir que o DELETE tinha rollbackado porque o parse error matou a transação inteira.

**How to apply (Protocolo OBRIGATÓRIO):**

1. **Backup TRIPLE antes de qualquer operação destrutiva:**
   - `cp` local em `/root/backups/midia/banco_imagens_reais.db.pre_janitor_YYYYMMDD_HHMM` (mesma partição, instantâneo)
   - `tar.gz` em `/root/backups/midia/banco_imagens_reais.db.pre_janitor_YYYYMMDD_HHMM.tar.gz` (compresso, ~5x menor)
   - B2 offsite em `b2:failover-cafezinho1/cingapura/backups/janitor_midia/YYYYMMDD_pre_janitor/` (rclone copy — bucket **failover-cafezinho1** é o único autorizado pela chave)

2. **Trabalhar SEMPRE em cópia `.clean`, jamais no original direto:**
   - `sudo cp /root/agent_data/banco_midia/banco_imagens_reais.db /root/agent_data/banco_midia/banco_imagens_reais.db.clean`
   - Aplicar SQL na `.clean` apenas.
   - Validar com `PRAGMA integrity_check` + sample de busca via `buscar_por_entidade_inteligente`.
   - SÓ THEN swap atômico.

3. **SQL em arquivo separado (NÃO heredoc SSH):**
   ```sql
   PRAGMA journal_mode=DELETE;
   BEGIN;
   DELETE FROM imagem_entidade WHERE NOT EXISTS (SELECT 1 FROM imagens WHERE imagens.id = imagem_entidade.imagem_id);
   DELETE FROM imagens WHERE NOT EXISTS (SELECT 1 FROM imagem_entidade WHERE imagem_entidade.imagem_id = imagens.id) AND coletado_em < datetime('now','-30 days');
   COMMIT;
   VACUUM;
   PRAGMA integrity_check;
   PRAGMA journal_mode=WAL;
   ```
   Subir via `scp` + aplicar com `sudo sqlite3 .clean < /home/ubuntu/janitor.sql`.

4. **Algoritmo em 3 níveis (Miguel decide o quão agressivo):**
   - **Nível 1 — VACUUM** (sem perda de dados, só rebuild páginas): sempre fazer.
   - **Nível 2A — DELETE órfãs +30d** (imagens sem vínculo, coletadas há mais de 30 dias): seguro, preserva janela pra agentes vincularem ainda. **APLICADO 21/06.**
   - **Nível 2B — Cascade órfãos reversos** (vínculos `imagem_entidade` sem pai em `imagens`): seguro, schema consistente. **APLICADO 21/06 (0 afetados — schema já estava íntegro).**
   - **Nível 2C — Dedup por descrição** SÓ EM ÓRFÃS (preserva TODAS as fotos vinculadas): **APLICADO via cron 22/06.** CUIDADO: versão anterior mantinha só 1 foto por descrição duplicada, causou perda de 17.612 vínculos (Lula 7983→1964) — REVERTIDA. Versão correta só deleta ÓRFÃS com descrição duplicada.
   - **Nível 3 — Hard cap 500M suave**: se banco >500MB após steps anteriores, entidades com >2000 vínculos perdem as mais antigas. **APLICADO via cron 22/06** (não disparou — banco 352MB).

5. **Swap atômico via sudo bash -c:**
   - `sudo bash -c "cd /root/agent_data/banco_midia/ && mv banco_imagens_reais.db banco_imagens_reais.db.pre_janitor_swap_YYYYMMDD_HHMM && mv banco_imagens_reais.db.clean banco_imagens_reais.db && sqlite3 banco_imagens_reais.db 'PRAGMA integrity_check;'"`
   - Manter rollback local 7 dias (deletar manualmente após).
   - B2 offsite já é o backup de longo prazo.

6. **Validação produção pós-swap:**
   - Rodar `buscar_por_entidade_inteligente(ent, top_k=2)` em Python direto (NÃO o smoke CLI que é fixo em "Lula").
   - Confirmar retorno de resultados relevantes para 3+ entidades canônicas (Lula, Bolsonaro, Alemanha funcionaram).
   - Confirmar vínculos por entidade preservados via `SELECT count(*) FROM imagem_entidade WHERE entidade_id=?`.

**Caveats:**
- `/tmp/` no Tencent rejeita `scp` do ubuntu com "No such file or directory" — usar `/home/ubuntu/`.
- Script `banco_midia_busca.py` NÃO é CLI real (ignora `--entidade`, roda smoke fixo). Importar como módulo em Python direto.
- WAL/SHM regeneram sozinhos quando agente acessa (`PRAGMA journal_mode=WAL` no fim do SQL garante modo correto).
- 200.810 órfãs restantes são <30d (janela de graça pra agentes vincularem — não devem ser tocadas).

Relacionado: [[feedback-relatorios-53-deploy-alibaba-b2-cada-tick]] (B2 bucket failover-cafezinho1, mesmo usado aqui).
