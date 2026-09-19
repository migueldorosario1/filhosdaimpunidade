# Memória — Ronda ZM 1/1h do ecossistema (log técnico, 03/09/2026)

**Autor:** ZM (ZCode/GLM-5.3, Dell) · **Irmã:** Foruns/forum_ronda_zm_loop_ecossistema_20260903.md

## Contexto levantado antes de criar (provas)

- Contrato da ponte: `Foruns/ponte_laura_completa/CONTRATO_PONTE_COMPLETA.md` — 8 agentes, refs por prefixo (ZM-), de_dell/de_laura disjuntos por máquina, publish exclusivo CM, Adendos v2.1/v2.2/v2.3, Emenda Pontes 2+2 (push duplo).
- Runbook 1h de referência: `Foruns/ponte_laura_completa/runbook_grok_miguel_1h.md` (GM ~:50, GL :37, AGY-M :35 — âncoras que a nova ronda evita usando :05).
- Fila DSC-024: `telegram_dc/…/README_PROTOCOLO.md` (na pasta `telegram_dsc/`) — DSN 1º, DS Laura 2º, ZM 3º; resposta em RESPOSTAS.md + "JÁ_RESPONDI O MIGUEL (ref)".
- Caixa de agentes no Tencent: `/home/ubuntu/cafezinho/v6_data/caixa_agentes.jsonl` (verificada por SSH; último registro 02/09 11:02 respondido pelo ZM na "rede de segurança 12h" — precedente do papel).
- Relatórios do Chefe: `Cerebro/Relatorios/ds_nuvem_chefe/` (diários; último na criação: 2026-09-02.md).
- Sync: `~/cerebro-miguel/scripts/sync_cerebro_to_github.py` (SOURCE=~/Downloads/Antigravity Google → TARGET=~/cerebro-miguel, push origin) + `scripts/ponte_push.sh` v1.1 (push duplo origin+nyc, carimba `estado/ponte_health.md`, retry 5/15/45s, 2 vias mortas = MODO_ILHA).
- `loop_ativo.json` = laura (22/08) — a ronda engaja mesmo assim por ordem expressa, sem violar ofícios.

## O que foi criado

- Automação ZCode `automation-877aeabb-e3f2-4874-98c6-fd7b4140349a` — cron `5 * * * *`, intervalo horário, recorrente, ATIVA; primeira execução 14:05 BRT 03/09. Prompt com 5 pernas (loop, DSC, ponte us65, DSNs/robôs, demandas) + regras de publicação e limites.
- Fórum + esta memória (Tema Duplo); anúncio `ZM-20260903-072` em de_dell.md; estado/heartbeat/ledger do ZM; linha ✅ no MONITORAMENTO; catálogo em CEREBRO_NODE_AGENTES.md; linha em CEREBRO_NODE_ATUALIZACOES.md; memória do ZCode Desktop espelhada.

## Lições/armadilhas para a ronda

- Ler com `git -C ~/cerebro-miguel pull --ff-only origin main` ANTES (repo pode estar mais fresco que o canônico; considerar a cópia mais nova).
- de_dell.md tem 4MB+ → append via heredoc, nunca reescrever o arquivo.
- Refs ZM-/ZD-: grep da última do dia, NUNCA reusar número.
- Commit seletivo (nunca `git add -A`); push recusado = fetch+rebase preservando os dois lados.
- Telegram: texto limpo (sem `**`/`#`), só com novidade; ronda quieta não spam.
- Se o hook de crédito der 🔴 no provedor da sessão, a ronda deve registrar no fórum e seguir com o que der; troca de modelo é sempre manual do Miguel.

## Resultado da publicação (13:03-13:04)

- sync OK (push GitHub tentativa 1); ponte_push ZM: github=OK, nyc=FALHOU (commit 8c2956fe6). NYC degradada desde ~10:05 (GM 10:05/11:12 também falharam) — fail-open, registrada como pendência de investigação.

## Comunicação dupla 2 canais (03/09 ~13h15 — ordem Miguel)

- ponte_push.sh v1.2 (backup ponte_push.sh.bak_pre_gdrive_20260903): ativas = GitHub (fetch+rebase autostash, retry 5/15/45s) + G-Drive (rclone copy com --include de de_dell/de_laura/loop_ativo/estado/**/ledger/** → gdrive:ponte_laura_completa; ponte_zm_dsc → gdrive:ponte_zm_dsc/latest); reservas automáticas NYC→Tencent (tar-pipe ssh tencent "sudo -n tar -C /root/Cerebro/Espelhos/ponte_laura_completa -xf -"); health push_duplo_v2; exit 1 só com TUDO morto (MODO_ILHA).
- Diagnóstico NYC: git push nyc main rejeitado non-ff desde ~10h de 03/09 — o espelho bare tem commits que o origin não tem (herança da divergência estrutural 392×428). Cura exige sessão dedicada (git fetch nyc; git log nyc/main --not origin/main); JAMAIS force-push.
- Lição E2E: às 13:12 o origin tinha andado 14 commits desde 13:04 (DS-N/Chefe/YouTube empurram a cada ~30 min) — push sem fetch+rebase cai. O v1.2 rebasa sozinho (autostash).
- Provas: health 13:12 (github=FALHOU|gdrive=OK|tencent_reserva=OK) e 13:13 (github=OK|gdrive=OK); rclone lsf confirma espelho; ssh confirma /root/Cerebro/Espelhos/.
