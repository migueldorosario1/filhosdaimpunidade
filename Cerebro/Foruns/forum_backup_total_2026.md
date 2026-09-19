# 🗣️ FÓRUM — BACKUP TOTAL 100% (Local → Drive → B2)

> **Decisão:** Miguel, 2026-08-05 ~12:40 BRT — *"Faz backup de tudo, 100% no Google Drive e 100% no Backblaze.
> Primeiro Google Drive; Backblaze depois. De 30 em 30 min um pouquinho; em 1-2 dias faz tudo. Depois vou limpar o computador."*
> **Memória técnica:** `Cerebro/Memorias/memoria_backup_total_2026.md` · **Plano:** `Cerebro/backup_total_2026/PLANO_BACKUP_TOTAL_100.md`

## Decisões registradas

1. **Escopo "tudo":** todos os dados locais fora do que é lixo regenerável (excluídos documentados: pesos `.deepseek` 22G, caches, `node_modules`, instaladores, tooling). Segredos (`cofre_intake`, `gcloud_indexing_keys`) NÃO sobem — ficam no rito do Cofre.
2. **Ordem:** FASE 1 = Google Drive (agora). FASE 2 = Backblaze B2 (🔒 só com ordem expressa do Miguel após FASE 1 = 100%).
3. **Ritmo:** janelas de ~25 min a cada 30 min (cron ZCode + loop do Claude, quem chegar primeiro pega o próximo chunk — protocolo de estado anti-dupla em `ESTADO.md`).
4. **Destinos Drive:** espelhos existentes recebem top-up (`pautas…`, `novo livro`, `Dados_Frios`); workspace vivo vai para o NOVO `drive:Workspace_Vivo/` (o `backup 20260717` fica congelado); tudo fora do workspace vai para o NOVO `drive:Backup_Total/`.
5. **Não duplicar:** `orlando diniz` (64,3G, incl. Lawfare29) e `Jornais do dia` (27,5G) já estão na raiz do Drive — excluídos dos re-syncs.
6. **Critério de conclusão FASE 1:** C01–C15 CONCLUÍDO + C16 (verificação) limpo → tag `[BACKUP-TOTAL-100-FASE1-DRIVE-CONCLUIDA]` no canal_trindade + aviso ao Miguel. Só então ele limpa o disco.

## Perguntas em aberto para o Miguel (não bloqueantes)

- FASE 2 (B2): bucket novo único `backup-total-local-2026` ou distribuir pelos buckets temáticos existentes? (sugestão: bucket novo único — simples de auditar e de apagar depois da limpeza)
