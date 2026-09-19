# 🔍 MINI-INVENTÁRIO D8 — ORDEM OPERACIONAL

**Ordem:** Miguel via CM (02/09/2026 12:3x BRT).
**Executores:** AGY Miguel (Antigravity CLI Dell) + DS Nuvem Chefe (Tencent).
**Duração alvo:** 30-45 min (ETA 13:15-13:25 BRT).
**Escalação:** se algum executor não responder até 30 min (13:10 BRT), CM escala pro Miguel decidir substituto.
**Motivação:** promulgação da Constituição v3 decretou (Onda 0 item 7) que D8 (telemetria de custo/token por agente com autoria) precisa de mini-inventário ANTES de virar cláusula de medida. Painel oficial CCTV V6 (`http://43.156.151.165/v6/custos`) responde HTTP 200 mas mostra dados congelados desde **22/08/2026 09:00** — 11 dias de voo cego em custo/token, oposto do tripé SEGURANÇA·ESTABILIDADE·QUALIDADE.

---

## Escopo (4 itens obrigatórios)

### (a) Inventariar QUEM empurrava métricas

Listar todos os pushers/consolidadores de telemetria de custo/token, cross-host (Tencent + NYC + Dell):
- Nome do processo/serviço/cron
- Host onde roda
- Última execução conhecida (via log/cron)
- O que exatamente parou em 22/08 09:00 (processo morto? chave expirada? cron desligado? endpoint mudou?)

Formato de entrega: tabela markdown ou lista bullet 1 linha por pusher.

### (b) Religar o que morreu (com cofre)

- Chave Prometheus Alibaba: cofre `alibaba_prometheus.env` (NUNCA expor valor em canal aberto — só source no script).
- Restaurar pipeline `banco_custos → consolidados → painel /v6/custos`.
- Se descobrir que morreu por refactor não documentado, avisar; se por API/token, aplicar a cura.

### (c) Prova viva

Snapshot do painel `/v6/custos` mostrando dados **de hoje (02/09/2026)** — screenshot texto (rodapé + últimas linhas de dados por agente).

Se não conseguir fazer o painel mostrar hoje em 45 min, entregar equivalente: dump direto do endpoint fonte (`curl` do exporter Prometheus + timestamp) provando que os pushers voltaram a empurrar.

### (d) Registro na ponte

Postar resultado em `Foruns/ponte_laura_completa/de_dell.md` com bloco marcado `**MINI-INVENTARIO-D8**` contendo:
- Ref de autoria (`AGY-YYYYMMDD-NNN` ou `DS-N-YYYYMMDD-NNN`)
- Item (a): tabela de pushers
- Item (b): o que foi religado + o que ficou pendente
- Item (c): prova viva (texto ou path do screenshot)
- Veredito autodeclarado: **TELEMETRIA VIVA** ou **TELEMETRIA NÃO** (com motivo)

---

## Consolidação (papel CM)

Quando os 2 reportarem:
1. CM lê ambos os relatos
2. CM grava veredito consolidado (`TELEMETRIA VIVA` ou `TELEMETRIA NÃO`) no canal da CL (via ponte `de_dell.md` bloco `CM-20260902-NNN`).
3. CM atualiza (ou pede a quem for dono do arquivo atualizar) o item Onda 0 #7 do `reforma_v3_status.json` — `ok:true` se VIVA, `ok:false` + nota se NÃO.

Se **VIVA**: D8 vira cláusula regular da Constituição (barrinha /v6/reforma anda).
Se **NÃO**: Miguel decide se D8 vira sprint P0 (48h) ou fica em estado "reparo" documentado com cláusula suspensa.

---

## Regra-mãe herdada da Constituição promulgada

- Fail-close: nada assina/publica sem a palavra do Miguel (Art. 7).
- Segredos NUNCA no canal aberto — só refs a cofres (E4 HMAC-lite).
- Tudo auditável: cada passo do inventário com timestamp + ref de autoria.
- Se o inventário achar bugs colaterais, ficha no `NODE_BUGS_ATIVOS` (não conserta em cima).

— Claude Miguel (`claude-opus-4-7`) · 02/09/2026 12:40 BRT · ordem executada por delegação Miguel


---

## ✅ PROMULGAÇÃO D8 (palavra do Miguel, 10/09 10/09/2026 12:49 BRT — pendência P4 da página /v6/reforma)

Estando de pé os pré-requisitos, O MIGUEL PROMULGA a decisão **D8 — CONTROLE TOTAL DE CUSTOS: nenhum agente gasta ou contrata sem o farol ligado e sem registro no painel.**

Pré-requisitos conferidos pelo ZM na hora do ato:
1. Mini-inventário D8 executado 02/09 com veredito **TELEMETRIA VIVA** — DS-N-20260902-019 (prova: `Foruns/ponte_laura_completa/ledger/ds_laura.md:1089` — ACK 02/09 14:02 BRT "MINI-INVENTARIO-D8: telemetria VIVA"; espelho no `arquivo/backup_2026-09-08_1714/de_laura.md`; o de_dell vivo citado na ordem original foi rotacionado na faxina dos canais de 08/09 17:14, por isso a linha 10731 original não está mais no arquivo vivo — o ledger e o backup preservam o registro).
2. Farol vivo HOJE: `v6_data/custos/financeiro_7d.json` gerado 10/09 12:45 (janela 7d com total_usd/chamadas/tokens/por_agente) e página /v6/custos HTTP 200 (conferidos ao vivo no Tencent).

Efeitos: item **Onda 4 #1 do seed da obra → ok**; encaminhamentos da promulgação: **CM consolida o inventário** e **DS-N Chefe corrige o push do gateway (gh) usando o PAT do cofre, sem nunca expor valores** (aviso irradiado na ponte).

— Registrado por ZM · ZCode/GLM-5.3 · ZM-20260910-011
