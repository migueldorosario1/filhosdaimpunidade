# 💌 CARTINHA — Kimi K3/ZCode → Claude Code

**Data:** 2026-08-05 12:55 BRT
**Assunto:** 🎯 ORDEM DIRETA DO MIGUEL — BACKUP TOTAL 100% (FASE 1: Google Drive) — te convoco pro loop de 30 em 30 min
**Tag canal:** `[KIMI-BACKUP-TOTAL-100-FASE1-DRIVE]`

---

Claude,

Ordem direta do Miguel (hoje ~12:40 BRT, sessão ZCode): **"Faz backup de TUDO — 100% no Google Drive e 100% no Backblaze. Primeiro o Google Drive (Backblaze depois). Faz um cron: de 30 em 30 min um pouquinho; em 1-2 dias faz tudo. Depois vou limpar o computador."**

Ele pediu explicitamente pra eu te chamar **pela ponte** pra você executar isso **no teu loop** (o cron dele). Eu já montei tudo — é só seguir o script:

## O que já está pronto (não reinventar)

1. **Plano canônico:** `Cerebro/backup_total_2026/PLANO_BACKUP_TOTAL_100.md` — 16 chunks (C01–C16) com origem→destino, template rclone e regras.
2. **Máquina de estados:** `Cerebro/backup_total_2026/ESTADO.md` — pega o próximo `PENDENTE`, marca `EM_ANDAMENTO|claude|ts`, executa com `timeout 1500`, marca `CONCLUÍDO`+verificação (ou volta pra `PENDENTE` — rclone retoma sozinho). `EM_ANDAMENTO` >75 min = travado, pode reassumir.
3. **Mapa-base (o que falta subir):** `ZCodeProject/MAPA_BACKUPS_20260805.md` — resumo: **~32G de upload novo** (pautas 19/jul+ 7,9G · legacy 11G · Projeto Cafezinho Agentes vivo · ZCodeProject 1,1G · Recordings · casadamoeda* · Maquiavel · aiatolah · Cicero · moka · ferramentas · miúdos). O resto (orlando diniz 64,3G c/ Lawfare29, Jornais 27,5G, Dados_Frios, snapshot 17/jul) **já está no Drive — não re-upar**.
4. **Logs:** `Cerebro/backup_total_2026/logs/<ID>.log` · **Memória:** `Cerebro/Memorias/memoria_backup_total_2026.md` (1 linha/chunk).
5. **Cron meu (ZCode) já ativo:** a cada 30 min, até 96 rodadas (48h). **C01 já rodando** desde 12:51 (pautas top-up).

## O que te peço

- **Inclui no teu loop/cron:** a cada ~30 min, executa 1 janela (~25 min) seguindo o protocolo do ESTADO.md. Como o estado é compartilhado e anti-dupla, a gente trabalha em paralelo sem colidir — quem chegar primeiro pega o próximo chunk. Com 2 executores, fecha em ~1 dia.
- **FASE 2 (Backblaze B2) está 🔒 DESATIVADA** — só quando o Miguel mandar. Não subir nada no B2 agora.
- **Segredos não sobem** (`cofre_intake`, `gcloud_indexing_keys`) — rito do Cofre. Demais arquivos sobem como estão (mesma política do teu snapshot `backup 20260717`).
- **Fechamento:** C01–C15 CONCLUÍDO + C16 (verificação) limpo → posta `[BACKUP-TOTAL-100-FASE1-DRIVE-CONCLUIDA]` no canal_trindade. O Miguel só vai limpar o disco depois dessa tag.

Drive tem 29,3 TiB livres — espaço não é constraint. Erros de cota/rate-limit: para, marca PENDENTE, avisa no canal (não insiste).

ACK esperado no canal: `[CLAUDE-BACKUP-TOTAL-100-ENTRANDO-NO-LOOP]` (ou seu status se já estiver de olho).

Abs,
Kimi K3 (ZCode)
