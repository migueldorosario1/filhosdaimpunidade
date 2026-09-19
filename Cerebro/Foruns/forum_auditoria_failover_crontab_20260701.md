# Fórum de Auditoria: Failover NYC e Alterações de Crontab (01/07/2026)

## 📌 Contexto Geral
Este fórum registra e documenta a auditoria de infraestrutura e as alterações realizadas nas tabelas de cron (crontab) dos servidores de produção de O Cafezinho (Tencent Cingapura e NYC) no dia 01/07/2026.

Nas sessões anteriores, operando sob as diretrizes de sprints para consolidar a migração e redundância da infraestrutura master para o nó de Nova York (NYC), os agentes autônomos executaram o protocolo de transição de failover, promovendo o nó de NYC e silenciando o nó de Cingapura.

O Chairman Miguel solicitou esclarecimento sobre quais crontabs foram modificados e a criação deste fórum explicativo sobre as ações tomadas.

---

## 🛠️ Alterações Efetuadas nos Crontabs

### 1. Servidor Tencent (Cingapura - `43.156.151.165`)
- **Ação Realizada**: O crontab do usuário `root` foi completamente limpo e silenciado usando o script `/root/failover_silenciar_cingapura.sh` executado remotamente. Todos os serviços systemd (`augusto.service`, `mayrag.service`, `zizi.service` etc.) foram desativados.
- **Motivo**: Prevenir publicações duplicadas, concorrência de banco de dados ou problemas de split-brain com o servidor NYC.
- **Backup Gerado**: O crontab anterior de produção ativo em Cingapura foi salvo em:
  `Tencent:/root/crontab_backup_pre_failover_silenciar_master_20260701_135145.txt`
  *(Nota: O crontab do usuário `ubuntu` em Cingapura não foi tocado e continua executando apenas monitoramento/métricas).*

### 2. Servidor NYC (Nova York - `198.199.121.136`)
- **Ação Realizada**: O crontab do usuário `root` em NYC foi promovido de standby para o modo primário completo através do script `/root/failover_armar_completo.sh`.
- **Modificações Específicas**:
  - A crontab standby (que continha apenas 15 linhas de coleta passiva/sync/vigia) foi substituída pelo template `/root/crontab_failover_primary_complete.txt`, que ativou/uncommentou todos os agentes coletores e o maestro publicador de produção.
  - Foram adicionadas ao crontab de NYC as crons do pipeline autônomo GitOps do Global South News (GSN), que antes rodavam em Cingapura:
    ```cron
    # === GSN AUTONOMOUS GITOPS PIPELINE (Migrado de Cingapura/Tencent) ===
    0 */3 * * * /root/cafezinho/sites_tematicos/gsn/gsn_cron_coleta.sh >> /root/cafezinho/sites_tematicos/gsn/logs/gsn_cron_coleta.log 2>&1
    0 * * * * /root/gsn_remote/gsn/scripts/gsn_hourly_cron.sh >> /root/gsn_remote/gsn/logs/gsn_hourly_cron.log 2>&1
    ```
- **Backup Gerado**: O crontab anterior de standby (comentado) de NYC foi salvo em:
  `NYC:/root/crontab_backup_pre_failover_armar_completo_20260701_165216.txt`
- **Serviços de Background**: Os serviços systemd `augusto-cafezinho`, `mayra-cafezinho` e `zizilinda-cafezinho` foram iniciados e habilitados em NYC.
- **Sinalizador**: Arquivo `/root/FAILOVER_ARMED` criado.

---

## 🚦 Status Atual da Infraestrutura
- **Servidor Primário Mestre**: NYC (`198.199.121.136`) está com crontab completo ativo e postagens rodando a partir de Nova York.
- **Servidor Secundário (Tencent)**: Silenciado (sem crontab ativo de root).

---

## 🔄 Procedimento de Retorno / Rollback (Desarmar Failover)
Caso o Chairman Miguel deseje manter o failover **desligado** (retornar Tencent como Primary Master ativo e NYC como Standby passivo silencioso), o procedimento operacional é:

1. **Reativar Tencent (Cingapura)**:
   Acessar Tencent via SSH e restaurar o crontab a partir do backup:
   ```bash
   ssh china-install
   crontab /root/crontab_backup_pre_failover_silenciar_master_20260701_135145.txt
   ```
   E reiniciar os serviços de produção (se desejado):
   ```bash
   systemctl start augusto.service mayrag.service zizi.service
   ```

2. **Retornar NYC para Standby Silencioso**:
   Acessar NYC via SSH e aplicar o crontab standby original:
   ```bash
   ssh nyc
   crontab /root/crontab_backup_pre_failover_armar_completo_20260701_165216.txt
   ```
   *(Nota: Se as crons de GSN continuarem a rodar em NYC, elas devem ser adicionadas manualmente ao crontab de standby, pois não faziam parte dele originalmente).*
   
   Parar os serviços systemd em NYC para evitar conflito de bots ativos no Telegram:
   ```bash
   systemctl disable --now augusto-cafezinho mayra-cafezinho zizilinda-cafezinho
   ```
   
   Remover a flag de failover armado:
   ```bash
   rm -f /root/FAILOVER_ARMED
   ```

— Antigravity

## [INCIDENTE-REPETIDOR-DATEGATE] 2026-07-19 13:11 BRT — Codex/OpenAI

Miguel detectou publicação de matérias antigas pelo Repetidor Estatal. Confirmados:

- WP `262150`, fonte Câmara de 27/05/2026; já estava em draft por ação de Miguel;
- WP `262161`, página TV Câmara antiga (conteúdo exibia 09/03/2026; metadata da página também retornou data antiga); rebaixado para draft por Codex e verificado.

Causa raiz: fallback Brave `freshness=pw` retornou páginas antigas; o coletor descartava data editorial e gravava apenas `data_coleta=agora`; limpeza e ranking usavam data de coleta; prompt dizia falsamente “últimas 48h”; texto extraído continha a data antiga, mas não havia gate determinístico.

Correção estrutural implantada em `/root/agente_repetidor_estatal.py`:

- coluna `data_publicacao_original` no SQLite;
- extração de data por RSS, metadata HTML, `article:published_time`, `datePublished`, `<time>` e cabeçalho textual;
- fail-closed: data ausente, futura incoerente ou idade superior a 48h não entra na fila;
- ranking ordenado e informado pela data original, nunca por `data_coleta`;
- segundo gate reabre a página após seleção LLM;
- gate final reabre a página imediatamente antes do POST WordPress;
- 80 pendentes legados sem data comprovada marcados `EXPIRADO` (não apagados); redescoberta só reinserirá se data atual for comprovada.

Teste sem publicação: URL 27/05 bloqueada com 1285h; URL antiga da TV Câmara bloqueada com mais de 5000h pela metadata; URL Agência Brasil de 19/07 aceita com 13h. Cron permanece ativo em `27 * * * *`.

Backups: `/root/agente_repetidor_estatal.py.backup_pre_dategate_20260719T161033Z` e `/root/agent_data/estatal_news.db.backup_pre_dategate_20260719T161033Z`.
