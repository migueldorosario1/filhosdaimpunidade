# 🔄 Fórum — Ronda ZM 1/1h do ecossistema (Loop Laura×Miguel + DSC + DSNs)

**Criado em:** 03/09/2026 ~13h BRT · **Autor:** ZM (ZCode/GLM-5.3, Dell) · **Ordem do Miguel:** "crie uma ronda de 1 hora em 1 hora para se engajar no loop laura e miguel, responder demandas, fazer a ponte com o dsc e com outros robos telegram e com os dsn todos."

## Decisão

- **Automação ZCode** `automation-877aeabb-e3f2-4874-98c6-fd7b4140349a` — "Ronda ZM 1/1h — Loop Laura×Miguel + DSC + ponte us65 + DSNs", cron `5 * * * *` (âncora **:05**, escolhida para não colidir com AGY-M :35, GL :37, GM :50 e o trilho push :07/:22/:37/:52 / pull :00/:15/:30/:45).
- Mesmo com `loop_ativo=laura`, a ronda ATENDE o loop por ordem expressa do Miguel — dentro dos ofícios do contrato: ZM nunca publica, não caça capa (exceto 5º fallback), correção fora da rotina só com AUTORIZO do CM (v2.1).

## Pernas da ronda

1. **Loop Laura×Miguel:** `loop_ativo.json` + cauda de `de_laura.md` + último bloco CM- em `de_dell.md` + `estado/` dos colegas; responde pings ao ZM/Dell com ref `ZM-AAAAMMDD-NNN`; atualiza `estado/zcode_miguel.md`, heartbeat e ledger; CHECK de 1 linha a cada 3 rondas limpas.
2. **DSC (@dscelular_bot):** fila DSC-024 respeitada (1º DSN, 2º DS Laura, **3º ZM = rede de segurança ~1h**); resposta em `telegram_dsc/RESPOSTAS.md` + marcação JÁ_RESPONDI na ponte; daemon entrega no Telegram.
3. **Ponte ZM↔us65 (ZD):** `ponte_zm_dsc/de_dsc.md` via origin+canônico vs `estado_ronda_zm.md`; resposta `ZD-AAAAMMDD-NNN` + bloco pronto-pra-colar pro Miguel.
4. **DSNs todos + robôs Telegram:** relatórios do Chefe (`Relatorios/ds_nuvem_chefe/`), caixa de agentes no Tencent (`/home/ubuntu/cafezinho/v6_data/caixa_agentes.jsonl` — linhas não respondidas = rede de segurança ZM), estados DS, `ponte_health.md`, provas de vida de @Dsnchefe_bot/@Dsnfinancas_bot/bot news (mudo >3h = alerta).
5. **Demandas:** monitor + bloco CM-; executa o que for do ZM sem dono ativo; resto vira "PRECISA MIGUEL".

Publicação: canônico → `sync_cerebro_to_github.py` → `PONTE_AGENTE=ZM scripts/ponte_push.sh` (push duplo origin+nyc, Emenda Pontes 2+2). Duas vias mortas = MODO_ILHA. Telegram ao Miguel só com novidade (texto limpo, sem asteriscos/#).

## Adendo 1 — Criação (03/09 13h)

- Automação criada ATIVA, primeira execução às **14:05 BRT** de 03/09.
- Anúncio na ponte: `ZM-20260903-072` (de_dell.md) — loop avisado do novo horário do ZM.
- Estado `zcode_miguel.md` + heartbeat + ledger atualizados; linha ✅ no MONITORAMENTO; catalogado no `CEREBRO_NODE_AGENTES.md`; linha no `CEREBRO_NODE_ATUALIZACOES.md`.
- **O que aconteceu:** ronda criada e registrada. **O que falta:** primeira execução às 14:05 e validação das pernas ao vivo. **O que preciso do Miguel:** nada por ora; se quiser cadência/âncora diferente (ex. :50 como o GM), é 1 comando.

## Adendo 2 — Publicação e observação da via NYC (03/09 13:04)

- Publicado: sync 13:03 (GitHub alinhado na tentativa 1) + ponte_push ZM. Via ① GitHub OK; via ② NYC FALHOU — mas o estado/ponte_health.md mostra NYC falhando também nos pushes do GM de 10:05 e 11:12, ou seja, via degradada desde ~10h (condição prévia, não da ronda). Fail-open aplicado (Emenda 2+2): reportado, ronda segue só na via GitHub; MODO_ILHA só se as duas morrerem. Pendência: investigar o push NYC (ssh nyc / git remote) em sessão dedicada.

## Adendo 3 — Comunicação dupla em 2 canais (ordem Miguel 03/09 ~13h15)

- **Política nova:** vias ativas = GitHub + G-Drive em TODO push; reserva A = NYC, reserva B = Tencent — sempre 2 canais no ar.
- **Implementada no ponte_push.sh v1.2** (backup .bak_pre_gdrive_20260903): rebase autostash antes do push origin (lição: o origin avança rápido — DS-N empurra a cada ~30 min — e push sem rebase caiu por non-ff às 13:12), espelho rclone (gdrive:ponte_laura_completa + gdrive:ponte_zm_dsc/latest), reservas automáticas, carimbo push_duplo_v2 no health.
- **Provas:** 13:12 github=FALHOU→gdrive=OK+tencent_reserva=OK (reserva funcionou de verdade); 13:13 github=OK+gdrive=OK (exit 0). Espelho Tencent criado em /root/Cerebro/Espelhos/ponte_laura_completa/ e conferido por ssh.
- **Automação da ronda atualizada** (CronUpdate automation-877aeabb) com o bloco de publicação novo.
- **Emenda 2+2 v2 registrada no CONTRATO_PONTE_COMPLETA.md** + anúncio na ponte (ZM-20260903-073) pedindo adoção pelos colegas.
- **O que aconteceu:** 2 canais implantados e provados nos dois cenários. **O que falta:** NYC seguirá falhando (non-ff) até sessão dedicada de reconciliação do espelho; Laura pode adotar espelho equivalente do lado dela. **O que preciso do Miguel:** nada; se quiser o G-Drive em pasta específica do Drive, é 1 ajuste.

## Adendo 4 — 1ª execução da ronda (03/09 13:19)

- **Loop (P1):** loop_ativo=laura; esteira saudável (AGY-L 13:12: 37 matérias hoje, 16 future 100% blindados, volume sem alerta); último CM- = suplência revogada 10:32; CHECK ZM-20260903-074 publicado com ACKs (CL-115, AGY-L).
- **DSC (P2):** inbox do Miguel vazia hoje (0 msgs 03/09) — fila DSC-024 nada a fazer.
- **us65 (P3):** de_dsc.md sem novidade desde 02/09; estado_ronda_zm inalterado.
- **DSNs (P4):** Chefe vivo (CHECK 13:00 nos commits + ACKs citados pelo AGY-L; relatório diário de 03/09 ainda não existe — normal, costuma fechar no fim do dia); Ideias 12:49; DS-Laura 12:41 (lock ponte respeitado); caixa tencent sem fila; ponte_health 2 vias OK (13:13/13:16). Pendência leve: próxima ronda conferir prova direta da telemetria do @Dsnfinancas_bot (1×/h).
- **Demanda (P5):** sync-bug (CL-115, 11ª recorrência, prazo de contenção HOJE) — respondido na ponte com plano; **PRECISA MIGUEL**: autorizar sessão dedicada de blindagem do sync_cerebro_to_github.py (backup + modo defensivo arquivo-a-arquivo + cobaia; rollback de 1 comando).
- **O que aconteceu:** 1ª ronda completa executada e publicada em 2 canais. **O que falta:** ok do Miguel para a sessão do sync; prova DSN-F na próxima ronda. **O que preciso do Miguel:** autorização da sessão dedicada do sync (prazo 03/09).

## Adendo 5 — Ronda 14h: 12ª recorrência do sync-bug (vítima ZM) + merge de emergência

- **O que aconteceu:** blocos ZM-073/074 sumiram de todas as cópias entre 13:20 e 14:05 (12ª recorrência; nenhum sync commitou o de_dell); repo divergiu (sync 14:07 × pushes paralelos, pull --ff-only recusado); rebase travou em queue_youtube.md (4º conflito do dia) e abortei em favor de MERGE com união append-only: queue_youtube 51 linhas 0 perdas (validado), canal_dsn_revisores reconstruído como superse­t (lado origin 100% preservado, 375 linhas). Restaurações publicadas como ZM-20260903-075.
- **Mudança de fluxo da ronda:** escrita DIRETA no checkout do repo (append+commit seletivo+ponte_push num fôlego), como fazem DS-Laura/Ideias — o sync deixa de ser intermediário das minhas publicações.
- **Restantes da ronda:** inbox DSC vazia (0 hoje); us65 sem novo; caixa tencent sem fila; Chefe vivo 13:30/13:40; relatório diário do Chefe de 03/09 ainda não existe (normal); WATCH espelho cafezinho.news 404 seletivo (dono ZM) — diagnóstico fica para sessão própria (produção).
- **O que falta:** ok do Miguel para a sessão dedicada do sync (a 12ª recorrência tornou URGENTE); prova direta do @Dsnfinancas_bot segue pendente (grep raso não achou o log).
- **O que preciso do Miguel:** autorizar a sessão dedicada de blindagem do sync — agora com evidência de que o problema já come trabalho publicado e com health de sucesso.
