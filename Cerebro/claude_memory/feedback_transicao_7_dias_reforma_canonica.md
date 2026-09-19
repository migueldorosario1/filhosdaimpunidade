---
name: feedback-transicao-7-dias-reforma-canonica
description: "A partir de 14/06 19:40 BRT, transição programada de 7 dias até o Cafezinho pós-Reforma virar canônico (21/06/2026). Monitorar comparativamente legado vs Reforma a cada tick §53, fazer backup B2 a cada 30min, indexar tudo sempre, e ir alinhando estrutura pro caminho da Reforma."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Transição 7 dias — Cafezinho pós-Reforma vira canônico em 21/06/2026

Miguel determinou em 14/06 ~19:40 BRT:
> "cafezinho pós-reforma será o canonico depois de 7 dias. vamos fazer a transição."

## Cronograma

- **Dia 0 (14/06 19:40 BRT)**: deploy Reforma no Tencent já feito (Codex 17:30 BRT). #258179 confirmado como teste sintético draft. SQLite editorial tem 13 matérias prontas + 16 publishes guardião (3 dry-run + 13 reais). 4 rascunhos avaliados pela Trindade (Claude 6.4 / Kimi 6.5 / Qwen 7.5 / AGY 8.13 / GLM 7.75).
- **Dia 1-3 (15-17/06)**: Reforma roda em paralelo, smoke editorial de tom (10 títulos: 5 polêmicos + 5 mornos). Auditoria do que sai vs legado.
- **Dia 4-5 (18-19/06)**: Trindade aplica os 3 ajustes na prompt do redator (adjetivação / dados concretos / cap palavras). Sincronizar 4 curas runtime do dia 14/06 com `Sistema/`.
- **Dia 6 (20/06)**: Matriz equivalência editorial 50 pautas (% publicada, tempo, % rebaixada, linha).
- **Dia 7 (21/06)**: Vira a chave. Reforma canônica.

## Backup triplo + indexação total — INFRAESTRUTURA CRIADA HOJE

Já implementado em 14/06 19:40 BRT:
- **Script local autônomo**: `~/bin/sync_foruns_maestro_b2.sh`
- **Indexador**: `~/bin/indexar_foruns_maestro.py` (sha256 + mtime + categoria)
- **Cron local**: `5,35 * * * *` (a cada 30min, alinhado com tick §53)
- **Destino B2**: `reforma_tencent_cafezinho:Cafezinho-pos-grande-reforma-jun2026/foruns_maestro_claude/`
- **Estrutura**:
  - `ProjetoCafezinhoAgentes_Foruns/` (legado, 31 MB)
  - `Cerebro_Foruns/` (Reforma, 504 KB)
  - `indices/indice_foruns_YYYYMMDD_HHMM.json`
- **Log**: `~/log/maestro_claude/sync_foruns_YYYY-MM.log`
- **Estado**: `~/.maestro_claude/indices/` (últimos 20 índices)

**Volume retroativo subido em 14/06 19:37 BRT**: 929 arquivos / 18.91 MB.

## A partir de agora, criar relatórios primariamente em `Cerebro/Foruns/por_data/2026/06/`

Estrutura Reforma adotada como caminho de SAÍDA:
- Relatórios de monitoramento: `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-14/relatorio_monitoramento_<tema>.md`
- Curas/bugs: `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-14/forum_cura_<tema>.md`
- Cartinhas: `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-14/cartinha_claude_<tema>.md`

**MAS** durante a transição (14-21/06), continuar mantendo cópia em `Projeto Cafezinho Agentes/Foruns/` (compatibilidade com legado). Quando virar canônico em 21/06, parar de escrever no legado e apenas redirecionar.

## Relatório comparativo a cada tick §53 (30min)

Diretiva Miguel 14/06 ~19:20 BRT: "a cada tick de 30 min, voce faz uma análise comparativa, quem publicou melhor + vai gravando relatorios".

Modelo de bloco no relatório do tick:

### 🏆 Quem publicou melhor (Tick HH:MM)
- **Legado**: N publishes na janela (cita IDs + qualidade resumida)
- **Reforma**: M drafts na janela (cita IDs + qualidade resumida)
- **Vencedor do tick**: <legado/Reforma/empate> em 8 quesitos
- **Pares temáticos diretos**: <listar IDs se houver mesma pauta nos 2>
- **Acumulado dia**: legado X × Y Reforma

Arquivo dedicado vivo: `Foruns/relatorio_comparativo_legado_vs_reforma_<YYYYMMDD>.md` (recriado a cada dia, atualizado a cada tick).

## Cláudia Beatriz — assimilação obrigatória

Tracker: `Foruns/estado_leitura_doc_claudia_beatriz.md`. Última leitura: 12/06 (lida 13/06 10:49 BRT).
- **Atraso atual**: 2 dias (13/06 + 14/06 não lidos)
- **Plano**: ler dia 13/06 e 14/06 nos próximos 2 ticks (19:42 + 20:12 BRT) — cruzar com os 22 publishes editorial-sérios do dia + 4 curas §92 aplicadas + 1 §51 (#258186 mailchimp) + 1 cat correção (#258166)

## Sincronizar 4 curas runtime do dia 14/06 com Sistema/ da Reforma

Pra Reforma virar canônica em 21/06 sem regredir, as 4 curas runtime aplicadas hoje precisam estar no `Sistema/` da Reforma:
1. **Haiku auditor websearch** (`agente_roteador_llm.py:1174`) ↔ Reforma usa rodízio Gemini→DeepSeek→Qwen→Perplexity, então essa cura pode não ser necessária; confirmar
2. **Honrar `excluidos` em `_prefixar_gemini_grounding_obrigatorio`** ↔ Reforma tem rodízio próprio, idem
3. **UA browser + status_code em `gerenciador_imagens.py:309`** ↔ Reforma usa `Sistema/midia/agente_midia.py` — **CONFIRMAR herança**
4. **Backticks `"\\\`\\\`\\\`"` em `agente_eleicoes_produtor.py:1364`** ↔ Codex disse "parser JSON robustecido" 10:59 BRT, provavelmente cobre

A AGY já recebeu pedido de auditoria do bug do classificador `util_categorizador_rigido.py:46` (inbox 14/06 16:55 BRT).

## Bucket B2 Reforma Tencent — bug do Codex pra corrigir

`backup_reforma_horario.sh` no Tencent (cron `15 * * * *`) está falhando hoje com erro:
```
Failed to create file system: you must use bucket "Cafezinho-pos-grande-reforma-jun2026" with this application key
```
O remote `reforma_tencent_cafezinho:` no Tencent precisa usar **diretamente o bucket name `Cafezinho-pos-grande-reforma-jun2026/<sub-path>`**, não a raiz do remote. Codex/DeepSeek é dono dessa frente — sinalizar no canal.

**Why**: Miguel 14/06 ~19:15 BRT: "agora voce vai fazer o monitoramento de dois sistemas, comparativamente, sabendo que o cafezinho pós-reforma irá substituir paulatinamente o cafezinho legado" + 19:40 BRT: "cafezinho pós-reforma será o canonico depois de 7 dias. vamos fazer a transição".

**How to apply**:
1. A cada tick §53: bloco "🏆 Quem publicou melhor" + atualizar `relatorio_comparativo_<YYYYMMDD>.md`
2. Backup B2 automático a cada 30min via cron local (já configurado)
3. Estrutura Cerebro/Foruns/por_data adotada como destino padrão dos novos arquivos
4. Cláudia Beatriz: assimilar 13/06 + 14/06 nos próximos 2 ticks
5. Acompanhar sincronia das 4 curas runtime com Sistema/
6. Reportar diário ao Miguel: "Dia N/7 da transição — Reforma X% pronta"

## Diário de Bordo do Canário (DeepSeek 14/06 ~21:25 BRT) — frente nova

**Fórum vivo**: `Foruns/forum_diario_bordo_canario_20260614.md`
**Cérebro node**: `Cerebro/CEREBRO_NODE_CANARIO_POS_REFORMA.md`

Regra: TODO agente, ao acordar, POSTA aqui um relatório comparativo.
- **Frequência primeiras 2h**: cada 30min
- **Depois**: mínimo 1/dia + sempre que houver erro/novidade
- **Formato**: cartinha humanizada + tabela técnica de métricas obrigatórias
- **Métricas**: posts legado, drafts canário, erros, duplicatas, latência, fact-check aprovados/reprovados

Como **Maestro / comparador oficial**, eu posto a cada tick §53 (30min) durante as primeiras 2h e depois pode ser cada 6h + cartinha humanizada pro Miguel. **1ª entrada postada 14/06 21:25 BRT** confirmando canário operacional pós-fix path DeepSeek + primeiro par direto Lula/Marco Transporte Reforma vs #258189 legado.

Relacionado: [[feedback_monitoramento_dual_legado_reforma]] (estrutura comparativa), [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]] (autonomia §92), [[reference_doc_claudia_beatriz_monitoramento]] (monitor humano).
