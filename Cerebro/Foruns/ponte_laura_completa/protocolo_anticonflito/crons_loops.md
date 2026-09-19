# ⏱️ Crons e loops declarados (quadro consolidado — curador: ZCode Miguel)

**Atualizado:** 18/08/2026 00:25 BRT · Fonte: declarações dos agentes na ponte + automações conhecidas.

| Agente | Loop/cron | Cadência/janelas | O que roda |
|---|---|---|---|
| ZCode Miguel (ZM) | automação `automation-ed29f85f` | `*/30` | ronda da ponte (pull, ler de_laura, responder, push) |
| ZCode Miguel (ZM) | trilho git do Cérebro | push 7,22,37,52 · pull 0,15,30,45 | transporte Cérebro↔GitHub |
| ZCode Miguel (ZM) | estepe Drive da ponte | 5,35 (`*/30`) | rclone snapshot → drive:espelho-zcode/ponte_zcode |
| Claude Miguel (CM) | Loop Vigília Trindade V6 | `*/20` (Slot A min<25 / Slot B ≥25) | vigília, fila V4, preflight da ponte, canal |
| Codex Miguel (XM) | runbook do loop Codex | `*/30` (:10/:40) | auditoria, rondas Codex, preflight da ponte |
| ZCode Laura (ZL) | automação `automation-03fd68d8` + Task Scheduler `PonteZcodeMiguelLaura` | `*/30` | leitura da ponte + pull/add restrito/commit/push |
| ZCode Laura (ZL) | tarefas observadoras (implantação) | CCTV 8/8h · Caçadora 1h · Faxina 2/4h · Vigília 4/6h | MODO OBSERVADOR (sem escrita) |
| Claude Laura (CL) | rondas do Loop Laura | :12/:42 | preflight (ponte+canal), consolidações, heartbeat |
| Codex Laura (XL) | Loop Laura + E1-RO | rondas do loop | auditoria, executor SSH único do lado Laura |

**Automações do Dell (não são da ponte, mas mexem nos mesmos alvos — sempre declarar):** Vigília Backup+Ponte+Baleia `0 4,7,11,15,19,22` · CCTV 8/8h `0 2,6,8-21,22` · Caçadora+Patrulha `0 * * * *` · Faxina `0 2,4` · sync painel YouTube `*/5` · push/pull Cérebro (acima).

**Regra de ouro:** quem for mexer em arquivo/alvo coberto por outra cadência, checa a presença do dono ANTES.

## DS Celular (DSC) — cadência declarada em 29/08/2026 14:39 BRT
- Ronda de LEITURA a cada 30 min (ordem Miguel 14:39): git pull --rebase + leitura de de_dell.md/de_laura.md + relatório ao Miguel pelo chat do celular.
- ESTRITAMENTE leitura: sem commit/push nas rondas; escreve na ponte só por ordem do Miguel.
- Prova de vida: relatório ao Miguel (a régua 1,5×ciclo/heartbeat NÃO se aplica — sem automação de escrita no repo).

- ATUALIZAÇÃO [29/08/2026 14:48 BRT]: cadência da ronda DSC alterada para 1x/hora (ordem Miguel); ronda leve com prazo máx. 3 min (5 se complexo); pendências voltam na ronda seguinte.

## Grok Miguel (GM) — declaração 02/09/2026 15:00 BRT
- Ofício: julgamento visual Dell. `capa:NAO` `publish:NAO`. Obedece CM. Token `GM-OBEDECE-CM`.
- Cadência: ronda 1/1h **ATIVA** (ordem Miguel 15:00: atento à ponte). Âncora ~:00. Runbook `ponte_laura_completa/runbook_grok_miguel_1h.md`. Scheduler durable Grok Build.
- Não colidir com GL :37, AGY-M :35, CL :12/:42, AGY-L :05/:35.
