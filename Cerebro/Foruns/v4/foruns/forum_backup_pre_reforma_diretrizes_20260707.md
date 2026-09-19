# Fórum — Backup Pré-Reforma de Diretrizes 2026-07-07

**Data:** 2026-07-07  
**Responsável:** Codex  
**Status:** backup local de controle criado; upload Backblaze B2 completo em andamento  
**Motivo:** preservar o estado atual antes da nova grande reforma de diretrizes editoriais.  

---

## 1. Escopo

Miguel pediu backup de tudo antes de qualquer mudança na reforma de diretrizes.

Escopo protegido:

- workspace local `Antigravity Google`;
- Cérebro;
- fóruns;
- inboxes;
- diretrizes recém-criadas;
- estado de trabalho sujo do git;
- plano de rollback;
- manifesto/checksums de arquivos críticos.

Nenhum arquivo de produção, cron, pipeline, Tencent ou WordPress foi alterado nesta etapa.

---

## 2. Backup Local de Controle

Diretório:

`Backups/pre_reforma_diretrizes_20260707_171801/`

Arquivos:

- `MANIFESTO_BACKUP.md`
- `ROLLBACK.md`
- `git_status_short.txt`
- `git_diff_stat.txt`
- `arquivos_cerebro_diretrizes_foruns.txt`
- `sha256_criticos.txt`

Validação:

- pacote de controle enviado ao B2;
- `rclone check --one-way --size-only --exclude 'rclone_*.log'` retornou `0 differences found`.

Destino B2 do controle:

`b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/controle/`

---

## 3. Backup Completo do Workspace no B2

Comando usado:

```bash
rclone copy . \
  b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/workspace/ \
  --fast-list \
  --transfers 6 \
  --checkers 16 \
  --progress \
  --stats 30s \
  --log-file /tmp/rclone_full_pre_reforma_diretrizes_20260707_171801.log \
  --log-level INFO
```

Política de segurança:

- `copy`, não `sync`;
- nenhuma exclusão destrutiva;
- nenhum delete remoto;
- logs fora do workspace para evitar arquivo mutante no backup;
- validação final pendente após término.

Destino B2:

`b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/workspace/`

Status atual:

- em andamento;
- estimativa inicial do rclone: cerca de 35 GB efetivos;
- workspace local total por `du -sh .`: 141 GB;
- a diferença será investigada no manifesto final com `rclone size`/contagem.

---

## 4. Rollback

Arquivo principal:

`Backups/pre_reforma_diretrizes_20260707_171801/ROLLBACK.md`

Regra de rollback:

1. baixar do B2 para `/tmp/restore_pre_reforma/`;
2. comparar com arquivo vivo;
3. só então substituir manualmente;
4. nunca usar `rclone sync` para restore;
5. não sobrescrever produção sem autorização explícita.

Exemplo:

```bash
rclone copy \
  b2:failover-cafezinho1/Antigravity_Google/backups/pre_reforma_diretrizes_20260707_171801/workspace/Cerebro/Foruns/forum_super_luxo_editorial_v4_espelhado_20260707.md \
  /tmp/restore_pre_reforma/Cerebro/Foruns/
```

---

## 5. Observabilidade Antes da Reforma

Checagem feita antes do backup:

- Prometheus Alibaba Managed responde a PromQL a partir de Cingapura;
- local desta máquina recebe `401 Unauthorized`, coerente com whitelist;
- Cingapura Tencent `43.156.151.165`: cron e `node_exporter` OK, push recente `OK: 613 metricas`;
- Alibaba Cérebro `39.106.184.215`: cron e `node_exporter` OK, push recente `OK: 482 metricas`;
- NYC Failover `198.199.121.136`: métricas de publicações e LLM OK; `serverdoin` falha por `prometheus_client/dotenv ausente`;
- NYC YouTube `142.93.48.252`: cron ativo, mas `node_exporter` em `127.0.0.1:9100` recusando conexão;
- Beijing Tencent `82.156.167.218`: não verificado agora por timeout SSH.

Conclusão:

> Prometheus central funciona, mas a telemetria de todos os nós não está 100%.

---

## 6. Próximos Passos

1. Aguardar fim do `rclone copy` completo.
2. Rodar validação com `rclone size` e amostras.
3. Atualizar este fórum com resultado final.
4. Atualizar `Cerebro/CEREBRO_NODE_BACKUPS_BACKBLAZE.md`.
5. Só depois iniciar a nova grande reforma de diretrizes.

---

## 7. Checkpoint em Andamento - 2026-07-07 18:51:30 -03

- Backup principal ainda em execução via `rclone copy`, sessão Codex `14643`.
- Último progresso observado: aproximadamente `12.421 GiB / 36.032 GiB`, `34%` por volume, `31436` arquivos listados e `2380 / 12402` no contador de transferidos do rclone.
- Sem erro fatal observado até este checkpoint.
- O log registra avisos `Can't follow symlink without -L/--copy-links` em índices antigos `por_tag`; validar ao final se esses symlinks devem ser preservados, seguidos ou apenas documentados como índices derivados.
- Checkpoint operacional detalhado criado em `Backups/pre_reforma_diretrizes_20260707_171801/CHECKPOINT_EM_ANDAMENTO.md` para envio à área `controle/` do Backblaze.

---

## 8. Pausa Manual - 2026-07-07 19:00:32 -03

- Backup pausado manualmente a pedido do usuário.
- Processo `rclone copy` saiu com código `130`, esperado para interrupção manual.
- Último progresso de terminal antes da interrupção definitiva: aproximadamente `13.194 GiB / 36.032 GiB`, `37%` por volume.
- Medição do destino após pausa: `2381` objetos, `1.902 GiB`.
- O volume remoto confirmado é menor que o volume tentado porque vários arquivos grandes estavam em upload multipart e foram cancelados antes do commit final no Backblaze.
- As linhas `ERROR ... context canceled` no log são consequência da pausa manual, não diagnóstico de corrupção.
- Checkpoint específico: `Backups/pre_reforma_diretrizes_20260707_171801/CHECKPOINT_PAUSA_20260707_190032.md`.
- Retomada: repetir `rclone copy` no mesmo destino; não usar `rclone sync`.

---

## 9. Fórum de Retomada Aberto - 2026-07-07 19:03:22 -03

Fórum operacional específico para não esquecer o backup e a retomada:

```text
Cerebro/Foruns/forum_backup_retomada_backblaze_pre_reforma_20260707.md
```

Função:

- registrar destino Backblaze;
- registrar ponto de pausa;
- registrar comando seguro de retomada;
- lembrar que a reforma grande de diretrizes só deve começar depois de backup completo e validado.
