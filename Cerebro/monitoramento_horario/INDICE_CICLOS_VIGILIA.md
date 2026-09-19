# 📇 ÍNDICE — CICLOS VIGÍLIA V5 (Loop Opus 4.7)

> Índice-mestre dos registros diários dos ciclos Vigília. Miguel vai juntar tudo depois — este arquivo dá o mapa.
> Criado 2026-08-06 04:25 BRT por Claude Code (regra `feedback_indexacao_cerebro_e_pedir_decisao_com_contexto`, Miguel 04:20: "tudo tem que estar indexado no cérebro. Bem indexado").
> **Atualização:** ao final de cada dia (último ciclo NOITE 06:17) OU ao início do dia seguinte (07:17), adicionar 1 linha da data anterior.

## 📂 Estrutura de registros (por dia)

Cada dia D deixa 4 tipos de rastro, em locais distintos:

| Tipo | Caminho | Formato | Conteúdo |
|---|---|---|---|
| Bugs JSONL | `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl` | JSON máquina, 1 linha/wp_post | `ts_utc, pid, vertical, pipeline, fixes, websearch, revisor_ds, revisor_gpt, backup, sha256, status_final` |
| Snapshots pré-publish | `Cerebro/Backups/vigilia_v5/YYYY-MM-DD/<pid>_pre_<tag>_YYYYMMDD_HHMMSS.json` | JSON completo WP | Estado do post ANTES de qualquer alteração — permite rollback |
| Ciclos MD legível | `Cerebro/monitoramento_horario/ciclos_vigilia/ciclos_vigilia_YYYY-MM-DD.md` | Markdown humano | 1 seção por ciclo com timestamp + decisões editoriais + aprendizados |
| Relatório revisores | `Cerebro/monitoramento_horario/relatorios_revisores/YYYY-MM-DD.md` | Markdown | DeepSeek + GPT custos/chamadas/latência/recomendações |

Além disso, pings consolidados 1×/hora no `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` com tag `[CLAUDE-VIGILIA-PING-CONSOLIDADO-HHH]` — histórico completo lá.

## Memória editorial do Claude Miguel

- Índice: `memoria_bugs_claude_miguel/INDEX.md`
- Gates permanentes: `memoria_bugs_claude_miguel/MEMORIA_FIXA.md`
- Diário: `memoria_bugs_claude_miguel/YYYY-MM-DD.md`
- Índice completo de bugs: `bugs_encontrados/INDEX.md`
- Leitura obrigatória em todo loop antes de revisar ou agendar WordPress.

## 📅 Registro por dia

### 2026-08-06 (NOITE em curso desde 23:17 de 05/08)

- **Ciclos MD:** `ciclos_vigilia/ciclos_vigilia_2026-08-06.md` (5 ciclos NOITE até 04:17 + 2 rodadas C05 backup + correção in-place 264426)
- **Bugs JSONL:** `bugs_encontrados/bugs_2026-08-06.jsonl` (10+ eventos)
- **Backups:** `Backups/vigilia_v5/2026-08-06/` (snapshots pré-publish, pré-correção, pré-pending)
- **Publicados até 04:20 BRT:** 9 (3 Geo + 3 Nacional + 3 Ciência-Tec). Pending: 264428 (Lula gafes Folha — ignorado por regra editorial nova), 264458 (digest Hormuz duplicata).
- **C05 backup Google Drive:** ~42% (4,62 GiB / 3.231 arqs). Janela 3 rodando 03:43→04:08.
- **Regras novas gravadas hoje:**
  - `feedback_fonte_estrangeira_qualificar_instituicao_geograficamente.md` (00:15 BRT — flag Miguel 264426 Tesouro)
  - `feedback_gravacao_datada_por_ciclo_e_ponte_kimi_regular.md` (02:20 BRT — Miguel: gravação sempre + ping Kimi)
  - `feedback_indexacao_cerebro_e_pedir_decisao_com_contexto.md` (04:20 BRT — Miguel: bem indexado + pedir decisão com contexto + gafes Lula Folha ignorar)

### 2026-08-05

- **Ciclos MD:** `ciclos_vigilia/` — arquivo não criado (regra da gravação MD legível surgiu apenas 06/08 02:20 BRT; ciclos de 05/08 têm registro apenas em bugs JSONL + backups). Retroativa possível se Miguel quiser.
- **Bugs JSONL:** `bugs_encontrados/bugs_2026-08-05.jsonl` (~40 eventos — dia completo, incluindo noite de retomada com 14 publish + 3 pending)
- **Backups:** `Backups/vigilia_v5/2026-08-05/` (snapshots do dia inteiro)
- **Publicados no dia:** 39 (18 Geo + 11 Nacional + 4 Ciência-Tec + 3 YT-esteira + 3 pending por duplicata)
- **Marco:** primeira noite do Loop Vigília V5 automático (cron NOITE `17 23,0-6 * * *` + DIA `17,47 7-22 * * *` criados 04/08 22:xx)
- **Baleia Azul retomado** após 8 dias: `Projeto Cafezinho Agentes/boletim_baleia_azul_20260805.md`
- **Relatório revisores 04/08:** `relatorios_revisores/2026-08-04.md` (R$ 0,068/dia — 8 DS + 2 GPT)
- **Backup Total 100%:** C01-C04 concluídos pelo Kimi; C05 (11G legacy) reservado ao Claude como teste da ponte — iniciado 23:30

### 2026-08-04

- **Baleia Azul:** parado (retomado 05/08)
- **Bugs JSONL:** `bugs_encontrados/bugs_2026-08-04.jsonl` (19 eventos — Vigília V5 rodando manualmente antes do cron automático)
- **Publicados no dia:** 19 (dado no ponto de retomada 16:01 BRT)
- **Marco:** Miguel abriu a regra da duplicata pré-publish 22:50 BRT (5+ posts sobre Lulinha saturaram)

## 🔗 Pontos de retomada

- Última retomada: `Cerebro/Foruns/ponto_retomada_claude_sessao_20260804_1601.md`
- Retomada anterior: `Cerebro/Foruns/ponto_retomada_claude_sessao_20260731_2215.md`

## 🌉 Ponte Kimi

- Canal vivo: `Projeto Cafezinho Agentes/Foruns/canal_trindade.md`
- Inbox Claude: `Cerebro/Foruns/inbox_trindade/claude.md`
- Inbox Kimi: `Cerebro/Foruns/inbox_trindade/kimi.md`
- Fórum missão backup: `Cerebro/Foruns/forum_ponte_backup_reforco_20260805.md`

## 💾 Backup Total 100% (missão paralela)

- ESTADO vivo: `Cerebro/backup_total_2026/ESTADO.md`
- PLANO canônico: `Cerebro/backup_total_2026/PLANO_BACKUP_TOTAL_100.md`
- MAPA arquivos: `Cerebro/backup_total_2026/MAPA_GERAL_ARQUIVOS_E_BACKUPS_20260805.md`
- Memória: `Cerebro/Memorias/memoria_backup_total_2026.md`
- Logs rclone: `Cerebro/backup_total_2026/logs/C0X.log`
