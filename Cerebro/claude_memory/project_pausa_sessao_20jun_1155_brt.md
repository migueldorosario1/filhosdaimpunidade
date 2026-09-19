---
name: project-pausa-sessao-20jun-1155-brt
description: "Estado da sessão 20/06 ~11:55 BRT após sprint de 1h25min cobrindo §107 hard-floor home (caso #259920 Carlos Bolsonaro), §108 EC3 WebSearch constitucional + 2 patches §92 REFORMA (produtor_geral googleSearch + auditor_texto cascata reduzida), §109 proposta filtro temporal indexada, cura §51 retroativa 6 posts Sheinbaum publish, parecer fórum Política V2. Fila Bloco C aberta: YT-V2-D2 esperando rsync+re-execução desde AGY 00:35, Sonar Pro investigação, discrepância maestro vs #259920, §109 implementação."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7b054038-ee9d-4869-bac1-f58e75f914b3
---

# Pausa sessão 20/06 11:55 BRT — fim sprint EC3 + cura §51

## Quando Miguel disser "retomar" ou "vai"

1. Ler ritual de despertar normal
2. Ler ESTE memo + `MEMORY.md` topo (EC3 §108, hard-floor §107, etc)
3. Conferir canal_trindade últimas 30 linhas (5 entradas minhas hoje)
4. Conferir inbox `claude.md` (AGY pode ter respondido sobre YT-V2-D2)
5. Decidir próximo item da fila C

## Sprint executado (10:30-11:55 BRT)

| Hora BRT | Item | Status |
|---|---|---|
| 10:50 | §107 hard-floor home (Carlos Bolsonaro #259920) | ✅ patch §92 + smoke 16/16 + Cérebro + memória |
| 11:00 | Diagnóstico EC3 (Gemini sem grounding causou #259655) | ✅ confirmado payload `produtor_geral.py:206-216` sem `tools` |
| 11:25 | Parecer fórum Política V2 com 6 contribuições | ✅ registrado + ponteiro canal |
| 11:30 | §108 EC3 patch §92 #1: `produtor_geral.py` + `google_search` tool | ✅ smoke real gerou "Presidente mexicana" (não "eleita") |
| 11:40 | §108 EC3 patch §92 #2: `auditor_texto.py` cascata reduzida | ✅ `[gemini_grounding, perplexity]` apenas |
| 11:45 | §109 proposta filtro temporal (data_materia_original) | ⏳ indexada, aguarda peer review Codex/Kilo |
| 11:50 | Cura §51 retroativa Sheinbaum últimos 7 dias | ✅ 9 detectados, 6 publish curados via API |

## Memórias persistidas hoje

- `feedback_hard_floor_home_politica_geopolitica.md` (§107)
- `feedback_ec3_websearch_obrigatorio_constitucional.md` (§108)
- ESTE memo (project pausa 20/06)

## Cérebro indexado hoje

- §107 Hard-floor HOME/NO_HOME (CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md)
- §108 EC3 WebSearch constitucional
- §109 Filtro temporal coleta (PROPOSTA — não aplicado)

## Patches §92 ativos no Tencent

| Arquivo | Backup | Status |
|---|---|---|
| `/root/maestro_distribuicao.py` | `*.bak_pre_hard_home_20260620_0840` | 🟢 ATIVO (próximo `*/10` aplica) |
| `/root/cafezinho/portal_cafezinho/Sistema/agentes/produtor_geral.py` | `*.bak_pre_websearch_20260620_1130` | 🟢 ATIVO (próximo `*/30` aplica) |
| `/root/cafezinho/portal_cafezinho/Sistema/agentes/auditor_texto.py` | `*.bak_pre_ec3_cascata_20260620_1140` | 🟢 ATIVO |

Rollback de qualquer um: `sudo cp <backup> <original>`.

## Posts curados §51 hoje

Substituição "presidente/a eleita do México" → "presidente/a do México" via WP API:

- #259576, #259524, #258848, #258821, #258799, #258452 (publish, curados)
- #259655 (pending, caso fundador, ainda fora do feed)
- #258745 (pending), #258730 (draft) — já fora do feed, não toquei

## Fila Bloco C aberta

| Prioridade | Item | Detalhe |
|---|---|---|
| ALTA | YT-V2-D2 re-execução | AGY perguntou 20/06 00:35 BRT no inbox `claude.md`. Patches AGY 19/06 18:54 (polling endpoint + coluna request_id) prontos local. Falta: rsync local→Tencent + re-rodar smoke real cap $0.30 + telemetria |
| MÉDIA | Perplexity Sonar Pro investigação | Caso #259655 aprovado por `qwen_revisor` mas Sonar também tem viés temporal (vetou outras Sheinbaum com "ainda não empossada"). Auditar `PERPLEXITY_FACTCHECK_MODEL`, `search_recency_filter`, modelo (`sonar` vs `sonar-pro` vs `sonar-reasoning-pro`). P0 Codex desde Fable/Mythos #257974 (13/06 EC2) |
| MÉDIA | §109 implementação filtro temporal | Codar `util_pubdate_extrator.py` + integrar em coletores LEGADO+REFORMA + filtro idade no nascimento. Toca: `coletor_geral.py` REFORMA, `util_coletor_padrao_v2.py` (LEGADO+REFORMA), `motor_publicador.py:329` |
| BAIXA | Discrepância maestro vs #259920 | Post #259920 publicado 10:00:05 BRT mas `maestro_historico.jsonl` mostra `agente=mercado` no timestamp. Tema é Flavio/Crime. Suspeita: cron próprio `agente_eleicoes_produtor` fora do maestro |
| BAIXA | Bug NYC vigia tail=0 desde 14/06 | Sem updates desde §53 14/06 14:25 BRT |
| BAIXA | Custo LLM congelado 0.8109 | Desde 08/06 — bug `custo_total_usd_est` (12 dias) |
| BAIXA | Cura retroativa AMLO | Busca 0 hits hoje, mas vale revisar quando Sonar Pro auditado |

## Pendências fórum Política V2 (parecer registrado)

Sugeri 6 itens pro schema novo da REFORMA:
1. EC3 WebSearch gate automatizado
2. `data_materia_original` + filtro temporal
3. `tema_editorial` + `forca_visibilidade` na Tese (§107)
4. Reuso `_CONTEXTOS_WEBSEARCH_OBRIGATORIO`, `tribunal_visual.py`, `util_safe_json.py`
5. Tabela `curas_aplicadas` realimentando Agente de Tese
6. PRAGMA WAL + UNIQUE(pauta_id, etapa)

Kilo está aguardando rodada fechar pra começar Etapa A (contrato de dados). Pareceres: Codex 10:46, AGY 11:00, Codex réplica 11:08, Grok, Claude 11:25.

## Diretivas Miguel novas hoje (vinculantes)

| Hora | Diretiva | Vira |
|---|---|---|
| 10:50 | "política, eleições, flavio, lula, nunca é no-home" + "no home é mais ciência, ia, fantástico" | §107 |
| 11:00 | "transforma isso em regra constitucional. o websearch precisa estar presente. ou na produção, ou no revisor, obrigatoriamente. O fact check obviamente tem que ter websearch" | EC3 §108 |
| 11:00 | "materias antigas não podem ir para o banco de noticias brutas, tem que haver um identificador da data da noticia coletada" | §109 |

## Estado Tencent (verificado 11:30 BRT)

- §104 Sheinbaum coletor + produtor desativados ✅
- §105 LATAM coletor + produtor desativados ✅
- §106 agente_eleicoes status=publish ✅
- Maestro `*/10` rodando, último entry 10:40 BRT `inflacao no_home=true` (correto)
- Canário `*/30` rodando flavio_bolsonaro + militar
- Publicador único `0 * * * *` rodando

## Cadência §53

- Pulei tick §53 hoje 11:00 BRT por estar no sprint EC3 — sem incidente operacional pois patches §92 cobriram brecha sistêmica
- Próximo tick: 12:00 BRT

## Para Miguel ao retomar

> Estado limpo. Bloco A (patches §92 REFORMA) e Bloco B (formalização) fechados. Cura §51 retroativa Sheinbaum eliminada (9 detectados, 6 publish curados). Próximo item natural: **YT-V2-D2 re-execução** (AGY esperando ~11h). Se preferir Sonar Pro investigação ou §109 codar primeiro, me diga.
