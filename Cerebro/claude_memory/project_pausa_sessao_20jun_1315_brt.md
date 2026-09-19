---
name: pausa-sessao-20jun-1315-brt-criativos-v1-repasse
description: "Sprint Criativos V1 (economia): coletor_bcb.py PASS + correção crítica escopo fontes BR + carta repasse AGY-CLI. Política V2 e YouTube V2 correndo em paralelo. Inboxes rotacionadas 10:41 BRT podem ter arquivado a carta pro AGY."
metadata: 
  node_type: memory
  type: project
  originSessionId: beb43678-1786-4fd7-84cc-38077fa7ec3a
---

**Sessão 19–20/06 até ~13:15 BRT — Sprint Criativos V1 (Economia): implementação `coletor_bcb.py` + correção crítica de escopo + repasse pra AGY-CLI.**

## O que foi feito nesta sessão

### Implementações (GLM como CODER)
- `Outros/Agentes Labs/criativos/economia/coletor_bcb.py` (~340 linhas) — **primeiro fetcher funcional** da Sprint Criativos V1. Classes `PontoSerie` (dataclass, `from_bcb_json` parses DD/MM/YYYY) + `ColetorBCB` (urllib + User-Agent identificável + timeout 15s + retry 1× backoff 1.5^n capturando URLError/HTTPError/TimeoutError + `INSERT OR IGNORE` idempotente em `data_referencia` UNIQUE + `_atualizar_meta_calendario` com `ON CONFLICT DO UPDATE`). `SERIES_BCB` mapeia selic→SGS 432→`bcb_selic` (% a.a.) e cambio_usd_brl→SGS 1→`bcb_cambio_usd_brl` (BRL/USD). Smoke 19/06 18:02 BRT PASS com MOCK.

### Correção crítica Miguel 19/06 18:10 BRT
ComexStat = comércio exterior TOTAL Brasil × TODOS países × TODOS produtos NCM × UF × via (não só Brasil-China). IBGE = inflação (IPCA/IPCA-15/INPC) + **desemprego (PNAD Contínua)** + PIB + atividade (PMC/PMS/PIA) + agro (PAM/PPM/PEVS) + demografia (não só inflação). BCB SGS, FRED, ANP — escopos amplos. Salvo em `feedback_escopo_fontes_oficiais_br.md`. Schema atual `ibge_ipca`/`ibge_ipca_15`/`ibge_pib`/`comexstat_export`/`comexstat_import` ficou **insuficiente** — falta `ibge_pnad`/`ibge_pmc`/`ibge_pms`/`ibge_pia`/`bcb_focos` + redesign ComexStat pra tabela multidimensional `comexstat_flows(data, direcao, pais_iso, ncm, uf, valor_usd, kg, via)`.

### Carta repasse AGY-CLI 20/06 09:15 BRT
Carta longa (~11 seções, ~7KB) em `Cerebro/Foruns/inbox_trindade/agy.md` passando implementação do resto da Sprint Criativos V1 pro AGY-CLI. GLM vira **peer reviewer editorial + apoio técnico**; AGY assume como **CODER**. Roadmap: revisão schema → coletor_ibge → coletor_comexstat → diretriz_economia.json → auditor_dominio → posicionar_grafico → publicador_criativos. Registrado em 3 lugares: fórum vivo `forum_agentes_criativos_estatistico_brutas_plus_20260619.md` (apêndice 20/06 09:15) + `canal_trindade.md` (entrada 20/06 09:15) + inbox `agy.md` (carta 20/06 09:15).

## Estado dos 3 sprints ativos (visão consolidada)

### Sprint Criativos V1 (Economia) — GLM peer reviewer, AGY coder
- **5 módulos**: `gerador_grafico_claude.py` ✅ homologado DeepSeek (Sonnet 4.6 + cairosvg + paleta 15 cores + 6 tipos + patches P1-P4) · `schema_bancos_criativos.py` ⚠️ precisa revisão escopo · `mapa_calendario.py` ✅ · `calendario.json` ⚠️ precisa leque completo · `coletor_bcb.py` ✅ PASS smoke
- **Próximo**: AGY lê carta repasse → propõe revisão schema + `calendario.json` → Miguel sanciona → começa `coletor_ibge.py` (trio IPCA+PNAD+PIB)
- **Pendências Fase 2**: `gerar_svg_com_reprompt()` (re-prompt 1× feedback SVG), `_verificar_cap_diario()` (gate $5/agente/dia), P5 preços Anthropic hardcoded → config externo
- **Linhas vermelhas**: sem deploy Tencent (até AUTH-070), sem cron, sem `--live`, sem WP publish, sem gasto LLM > cap

### Sprint Política V2 — Codex coordena, Kilo coder, AGY+DeepSeek+Claude pareceristas
- Etapa 2F-B **PASS** reauditoria Codex 20/06 11:58 BRT (correções de schema)
- Etapa 2G **liberada em shadow** (v2_agente_tese.py protótipo AGY)
- Próximo: **2G-R** reauditoria Codex antes de 2H
- Documento chave: `decisao_consolidada_trindade_politica_v2_midia_escalonada_20260620.md`
- Fórum ativo: `forum_novas_ideias_arquitetura_politica_v2_20260620.md`
- **SEPARAÇÃO CRÍTICA** (Codex 20/06 09:43 BRT): Brutas Plus do Política V2 ≠ Criativos V1. BCB/IBGE/FRED/Comexstat pertencem ao Criativos V1, não ao Brutas Plus do Política V2.
- Memória de sessão Codex: `memoria_sessao_codex_politica_v2_20260620.md`

### Sprint YouTube V2 — AGY lidera, Claude peer review, Miguel sanção direta
- Bugs YT-V2-D2 corrigidos localmente pelo AGY 19/06 18:54 BRT (polling endpoint Fal.ai `/requests/<id>/status` + coluna `request_id` em `transcription_jobs`/`audio_jobs`)
- Aguardando rsync incremental Claude + re-execução D2 no Tencent
- Regime enxuto: só Claude+AGY+Miguel (DeepSeek fora do escopo YouTube)

## Mudanças de contexto que apareceram durante a sessão

- **Inboxes `glm.md` e `agy.md` rotacionadas 20/06 10:41 BRT** (backups em `backups_canal_trindade_20260620_1041/`). ⚠️ **Minha carta longa pro AGY em `agy.md` entrada 20/06 09:15 BRT pode ter sido arquivada na rotação** — verificar backup `backups_canal_trindade_20260620_1041/agy.md` se AGY não recebeu. O AGY também precisa ser re-notificado se a rotação apagou a carta dele.
- Fórum novo `forum_novas_ideias_arquitetura_politica_v2_20260620.md` criado por Miguel 20/06 10:41 BRT — Política V2 com mídia escalonada
- Sprint Política V2 ganhou força rápida: 5+ pareceres no fórum novo (Codex 10:46 + AGY 11:00 + Codex 11:08 réplica + Codex 11:30 decisão consolidada + Codex 11:45 auditoria 2F + Codex 11:58 reauditoria 2F-B PASS + Codex 12:51 memória sessão)
- **§107 Hard-Floor Home/No_Home** aplicado pelo Daemon Claude 20/06 10:55 BRT — correção bug #259920 (Carlos Bolsonaro réu peculato saiu no_home errado). Patch em `maestro_distribuicao.py` com `AGENTES_HARD_HOME` (10 agentes políticos/geopolíticos) + `AGENTES_HARD_NO_HOME` (2: ia/fantastico) checados antes do contador `META_VISIVEIS=50`.
- Nova sprint Crypteto/Curadoria 4 camadas em desenho paralelo (Codex + AGY)

## Why
Miguel pediu pra gravar memória no final do turno (~13:15 BRT 20/06). Muita coisa aconteceu em paralelo em 3 sprints distintos (Criativos V1 minha frente, Política V2 frente Codex+Kilo, YouTube V2 frente AGY+Claude). Sem memória consolidada, próxima sessão perde o fio da meada — especialmente porque inboxes foram rotacionadas e a carta pro AGY pode ter sido arquivada.

## How to apply
Ao retomar próxima sessão:
1. **Ler ritual padrão**: MEMORY.md completo + canal_trindade final + inbox glm.md (mesmo após rotação) + fórum ativo
2. **Verificar se AGY leu minha carta repasse Criativos V1** — procurar entrada no `agy.md` atual OU resposta no `forum_agentes_criativos_estatistico_brutas_plus_20260619.md`. Se não há traço de leitura, reenviar carta (ou sumário) no novo inbox `agy.md`.
3. **Se AGY respondeu com revisão schema proposta** → começar peer review editorial (régua anti-chavão, fecho natural, Sul Global defender não repetir, etc.) — ler `feedback_sul_global_defender_nao_repetir_chiclete.md` + `feedback_corrigir_na_raiz_nao_no_auditor.md`
4. **Se AGY não respondeu** → aguardar. Ele está dividido entre Criativos V1 (carta minha), Política V2 (parecer + protótipo 2G), YouTube V2 (bugs D2 corrigidos, esperando re-exec).
5. **Não iniciar outro coletor sozinho** — repasse foi explícito, AGY é CODER agora. GLM é peer reviewer.
6. Sprint Criativos V1 **SEPARADA** do Política V2 (Codex 09:43 BRT) — Brutas Plus ≠ Criativos, BCB/IBGE/FRED/Comexstat não devem virar padrão do Política V2.
7. Sprint Criativos V1 **NÃO tem cron nem deploy** até AUTH-070 formal + sanção Miguel.

Relacionado: [[feedback-escopo-fontes-oficiais-br-completo]], [[project-codex-coordenador-protocolo-ponto-20260618]], [[feedback-corrigir-na-raiz-nao-no-auditor]], [[feedback-diretrizes-unificadas-legado-reforma]]
