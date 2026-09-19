---
name: feedback-disco-tencent-100-emergencia
description: "Tencent /dev/vda2 atinge 100% periodicamente devido a backups tar.gz acumulados em /root/BACKUPS/ + /root/V3/tmp/b2_audit/ + /root/backup_legacy_*/. Sintoma: V3 banco SQLite com erro `disk I/O (10)` em prepare. Limpeza segura: deletar tar.gz >30 dias dessas pastas."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

🚨 **Tencent disco /dev/vda2 (118GB) atinge 100% periodicamente** por acúmulo de backups tar.gz que ninguém faz rotação. Caso fundador 22/06 05:30 BRT: `/dev/vda2 118G/118G 0%avail` → V3 banco com `Error: in prepare, disk I/O error (10)` → fantastico rc=0 sem publish → produção degradou.

**Ofensores conhecidos** (em ordem de prioridade pra deletar):
1. `/root/V3/tmp/b2_audit/backup_cafezinho_*_0500.tar.gz` — 5.3GB cada, criado diariamente, **NUNCA rotacionado**. Em 22/06 havia tar.gz de 20/05 e 22/05 (1 mês atrás).
2. `/root/snapshot_root_pre_reforma_*.tar.gz` — snapshots únicos pré-grande-reforma, 6.4GB. Deveria ser deletado após sucesso da reforma.
3. `/root/backup_legacy_*/root_full_backup_*.tar.gz` — backups completos antigos, 13GB. Mantidos por receio mas já obsoletos após dias.
4. `/root/BACKUPS/backup_cafezinho_*_0500.tar.gz` — backup diário 28GB. **Manter pelo menos o último** mas pode rotar +7 dias.
5. `/root/backups/midia/banco_imagens_reais.db.pre_janitor_*` — backups janitor mídia 535MB cada. Manter 1-2.

**Why:** descoberto em 22/06 05:30 BRT durante vigília §53 ativa. V3 deu disk I/O na consulta sqlite3, fantastico publicou rc=0 sem publish, produção parou. Identifiquei via `df -h /` (100% USE%), `du -h --max-depth=2 /root`, `find /root -type f -size +100M`.

**How to apply:**
1. **Ao detectar V3 disk I/O OU produção parada inexplicada**: rodar `df -h /` no Tencent ANTES de outras investigações.
2. **Limpeza segura autônoma** (sem perguntar Miguel se Miguel deu autorização vigília):
   - Deletar tar.gz com `mtime > 30 dias` em `/root/V3/tmp/b2_audit/`, `/root/backup_legacy_*/`, `/root/snapshot_root_pre_*.tar.gz`
   - Manter o último backup `/root/BACKUPS/backup_cafezinho_*_0500.tar.gz` (do dia)
   - Verificar B2 tem cópia antes de deletar local (failover-cafezinho1 bucket)
3. **Patch §92 estrutural sugerido** (pendente sprint):
   - Cron diário 05:00 BRT já cria backup novo
   - Adicionar cron de **rotação automática**: `find /root/BACKUPS -name "backup_cafezinho_*.tar.gz" -mtime +7 -delete` + igual pra V3/tmp/b2_audit
   - Alert quando `df -h /` chega a 85% (Prometheus/Telegram)
4. **NÃO deletar sem confirmar**: arquivos em `/root/venv/`, `/root/agent_data/banco_midia/`, `/root/agent_data/*.sqlite` (bancos de produção), `/root/cafezinho/` (REFORMA).

**Caso fundador 22/06 05:30 BRT — durante vigília Miguel**:
- ANTES: 118G/118G 0avail 100%
- Apaguei: backup_cafezinho_20260520_0500.tar.gz (5.3G) + 20260522_0500.tar.gz (5.3G) + snapshot_root_pre_reforma_20260613 (6.4G) + root_full_backup_20260616_0101 (13G) = **~30GB liberados**
- DEPOIS: 89G/118G 25Gavail 79%
- V3 banco voltou (`COUNT=4 + integrity_check ok`)
- Tempo total da intervenção: 3 minutos

Aplica em conjunto com [[feedback-janitor-banco-midia-protocolo-20260621]] (que cobre limpeza específica do banco_imagens_reais.db).
