# 🌅 Fórum — DSN Coletor Nacional fase 1 NO AR (IDEIA-012 executada)

**Criado em:** 05/09/2026 ~08:1x BRT · **Executor:** ZM (ZCode/GLM-5.3, Dell) · **Ordem do Miguel (~07:2x, "pode ir em frente" reconfirmada 2×):** executar a IDEIA-012 (DS-N Ideias, `Foruns/ideias/2026-09-04_dsn_coletores_integracao.md`) com as travas do parecer DS-N-20260904-137A (Chefe), em modo observação primeiro. **Objetivo:** pauta oficial nova na fila de manhã cedo — o antídoto do buraco da madrugada (CL-009).

## O que está no ar

- **Adapter (NYC):** `/root/v4_labs/scripts/dsn_adapter_v41.py` + cron `*/15` c/ flock. Puxa entregas do Tencent por scp, valida **fail-closed** (item_key=sha1(url)[:16] · published_at ISO-UTC · título ≤140 · corpo ≥800), `INSERT OR IGNORE` em `candidates` como `status='new'` (vertical nacional), loga em `/root/v4_labs/dados/entregas_dsn.log`, idempotente (último arquivo + chave; contador por rowcount real).
- **Produtor (Tencent):** `/home/ubuntu/dsn_coletores/dsn_coletor_nacional.py` + cron `15 6,7,8` e `45 23` (BRT) c/ flock. Fontes ativas fase 1: **Senado (rss.xml)**. Marcadas pendentes c/ motivo (sondagem real 05/09): Câmara (URL é HTML, não RSS), TCU (WAF "Acesso Bloqueado" p/ datacenter), Planalto (429/HTML), STF+TSE (403 WAF), DOU (endpoint morto 000). Extração de corpo = trafilatura 2.0.0 (já no tencent). **Sem LLM — custo zero.** Commit de cada entrega no repo (`cerebro/dados/dsn_coletores/entregas/`, carimbo de auditoria) + scp físico p/ o adapter.
- **Rollback (ROLLBACK_INDEX NYC):** produtor = `ativo=false` no config OU restaurar `crontab.bak_pre_dsn_coletor_20260905`; adapter = restaurar `crontab.bak_pre_dsn_adapter_20260905`; sem efeito retroativo; <5 min sem tocar no V4.1.

## Provas (as 5 etapas, na ordem do Miguel)

1. **Adapter primeiro:** prova com JSONL fictício de 4 itens — dry-run limpo (0 escrita), real inseriu 4 na fila nacional (SELECT), re-rodada 0 novos (idempotência), log ok; itens de teste REMOVIDOS da fila (§131).
2. **Produtor em observação:** dry-run gerou 5 itens reais do Senado em `staging/` (nada entregue); travas conferidas item a item (key ok, ISO-UTC, corpos 1026-3656 chars, ≤25, zero segredo).
3. **E2E:** entrega real `2026-09-05_1108_dsn_nacional.jsonl` (5 itens) → commit repo `eb6aea150` → adapter inseriu 5 na fila (SELECT: Congresso fechado fds, "taxa das blusinhas", Caso Master/Viana, petróleo Amapá/Davi, Corretores de Imóveis) → idempotência provada em 2 camadas (estado por arquivo = 0 novos; reprocessamento forçado = INSERT OR IGNORE segurou).
4. **Cadência armada SÓ depois da prova** (crons acima).
5. **Registro:** entregas.log desde o 1º item · monitor · telemetria · este fórum.

## Lições técnicas do caminho

- O feed do Senado não traz `<link>` — o permalink vem no `<guid>` (cura no parse).
- Várias URLs "RSS" de órgãos são HTML/WAF para datacenter; fase 1.5 = buscar endpoints reais ou proxy residencial (casa tem IPRoyal) — decisão do Miguel.
- Adapter: contar INSERT por `cursor.rowcount` (senão o log mente duplicatas ignoradas).

## Estado

- **O que aconteceu:** fase 1 completa e provada E2E; 5 candidatas oficiais na fila nacional aguardando a esteira (tese/redator decidem; publicação segue da CL). **O que falta:** amanhã 06:15 a 1ª corrida automática; observar a manhã. **O que preciso do Miguel:** nada agora; fase 1.5 (mais fontes via proxy/endpoints) só se ele quiser.
