---
name: feedback-monitoramento-dual-legado-reforma
description: "A partir de 14/06 ~19:15 BRT, o Loop §53 do Maestro Claude monitora DOIS sistemas em paralelo — Cafezinho legado (cron `*/10` em produção) E Cafezinho pós-Reforma (staging Tencent `/root/cafezinho/`). Objetivo: validar Reforma antes de substituir o legado paulatinamente."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Monitoramento DUAL — Legado vs Reforma

A partir de 14/06 ~19:15 BRT, Miguel determinou que o Loop §53 monitore **comparativamente** os 2 sistemas:

## Cafezinho LEGADO (em produção)
- **Path**: `/root/` no Tencent
- **Motor**: `motor_publicador.py` (~145KB)
- **Maestro**: `maestro_distribuicao.py` cron `*/10 * * * *`
- **Roteador**: `agente_roteador_llm.py` (2.715 linhas) + curas haiku/excluidos aplicadas hoje
- **Saída**: publish ao vivo no WP
- **WP author**: 5470 (Redator)
- **Métricas**:
  - Cadência: ~1 publish/25min
  - §93 cobertura: 92.5%
  - §53C auditor ativo (Gemini grounding)
  - §94 anti-repetição WPCode ativa
  - Cota Indexing: 200/dia
  - Pipeline: 6 camadas LLM (producer→revisor→auditor→Perplexity→Claude→Tribunal Visual)

## Cafezinho REFORMA (staging canário)
- **Path**: `/root/cafezinho/` no Tencent
- **Motor**: `Sistema/publicador/publicador_cafezinho.py`
- **Maestro**: `scripts/maestro_grande_reforma.py` — **NÃO em cron, execução manual**
- **Roteador**: `roteador_v2.py` (327 linhas, cobertura 2 agentes só)
- **Saída**: `status=draft` no WP (WP_STATUS_GLOBAL hard-coded)
- **WP author**: 5470 (mesma conta)
- **Banco**: SQLite `Dados/bancos/pipeline_editorial_local.db` (8 tabelas, ~150 eventos pipeline)
- **CCTV**: `agent_data/cctv.log` + `Dados/relatorios/`
- **Backup**: `15 * * * *` → B2 (bucket "Cafezinho-pos-grande-reforma-jun2026")
- **Identificação no WP**: status=draft + author=5470 + ID > 258179 (timestamp ≥ 17:22 BRT de 14/06)

## Métricas comparativas obrigatórias por tick §53

Adicionar ao relatório do loop, ao lado da auditoria editorial do legado, uma seção:

### 🆚 Comparativo Legado vs Reforma

| Métrica | Legado | Reforma | Observação |
|---|---|---|---|
| Publishes hoje (publish status) | XX | YY (drafts) | Reforma só publica draft |
| Cadência média (min/publish) | YY | -- | Reforma sem cron |
| Cobertura §93 | XX% | n/a | Reforma não pinga ainda |
| §53C auditor | ativo | n/a | |
| Pipeline events (SQLite) | n/a | XX | |
| Health CCTV | n/a | XX/100 | |
| Curas runtime sincronizadas | 4/4 | 0/4 (ou X/4) | haiku, excluidos, UA, backticks |
| Backups B2 OK | sim | sim/erro | hoje 19:15 deu erro bucket |

### Identificação de posts Reforma no WP
- Filtrar `status=draft` + autor 5470 + data ≥ 14/06 17:22 BRT
- Conferir corpo: rascunhos Reforma sintéticos contêm "validar o pipeline local da Grande Reforma" no início
- Rascunhos reais (das 4 categorias avaliadas) têm `*Tema: <nome> | ID: pronta_<nome>_<hash>*` como sub-cabeçalho

### Critérios pra Reforma "passar" e substituir o legado paulatinamente
1. **Cron próprio ativo** (ex: `*/20 * * * *` paralelo ao legado)
2. **Smoke editorial de tom** (10 títulos: 5 polêmicos + 5 mornos) — Reforma ≤ legado em adjetivação não-atribuída
3. **Equivalência editorial**: matriz 50 pautas comparadas (% publicada, tempo, % rebaixada, linha)
4. **4 curas runtime do dia sincronizadas** (haiku auditor / excluidos / UA browser / backticks §53D)
5. **5 ajustes da Trindade aplicados** (adjetivação, dados concretos, cap palavras, etc — convergência das auditorias)
6. **CCTV estável** (sem ConnectionResetError) + health score ≥ 90/100 consistente
7. **Backup B2 corrigido** (bucket name "Cafezinho-pos-grande-reforma-jun2026")

Sem esses 7, **NÃO virar a chave de draft → publish na Reforma**. Canário paralelo em modo draft pode rodar 1+ semana.

## Divisão de temas (Miguel 14/06 ~21:30 BRT via DeepSeek)

Pra zerar sobreposição/conflito, cada sistema cuida de temas próprios:

- **Legado**: geopolitica, nacional, **lula**, eleições (+ outros que já roda: sobrenatural, fantastico, IA, repetidor, sheinbaum/militar/etc até completarem migração)
- **Canário Reforma**: sheinbaum, china, flavio_bolsonaro, crime, militar (cron `*/15` rodando 21:30 BRT)

**Consequência editorial**: mesma pauta aparecer nos 2 = bug de dedup cross-sistema, não disputa editorial.

## Como reportar

**A cada tick §53 (30min) — ENTREGA OBRIGATÓRIA: tabela comparativa completa** legado vs Reforma. Formato completo:

### 🆚 Tabela Comparativa — Legado vs Reforma (snapshot HH:MM BRT)

| Quesito | Cafezinho LEGADO | Cafezinho REFORMA (Canário) | Diferença |
|---|---|---|---|
| Temas atribuídos | geopolitica, nacional, lula, eleições + outros | sheinbaum, china, flavio, crime, militar | mesmos? sobreposição = bug |
| Total posts dia | N (publish/pending/draft) | N drafts WP | – |
| Editorial-sérios publish | N (range IDs) | N | – |
| Cadência média | min/post | min/ciclo `*/15` | – |
| Último publish/draft | #ID timestamp | #ID timestamp | – |
| Maestro/orquestrador | `maestro_distribuicao.py` `*/10` | `maestro_grande_reforma.py` `*/15` | – |
| §93 Indexing Google | X% cobertura | n/a (drafts) | – |
| §53C auditor titles | N entradas (status) | n/a | – |
| §94 anti-repetição | WPCode ativo | `anti_repeticao.log` | – |
| Pipeline SQLite | n/a | brutas + auditadas + prontas + publicadas + eventos | – |
| Curas/correções runtime | §92 + §51 totais | n/a | – |
| Erros recentes | timeouts/exceptions | tracebacks no log canário | – |
| Backup B2 | sync_b2 cron | backup_reforma_horario cron | – |
| Saída final WP | publish ao vivo | `WP_STATUS_GLOBAL=draft` | Reforma 0 risco |

### 🏆 Veredito acumulado dia
- **Legado: N publishes editorial-sérios** + cobertura ampla
- **Reforma: N drafts WP** (excluir sintéticos manuais)
- **Placar Legado X × Y Reforma**

**Por que a tabela completa toda vez**: Miguel 14/06 ~21:35 BRT pediu "faz sempre uma tabela comparando cafezinho legado e cafezinho pós-reforma". Não é só "quem ganhou o tick" — é diagnóstico completo dos 2 sistemas em todas as métricas a cada 30min.

## (legado) Como reportar — Quem publicou melhor (mantém junto, simplificado)

Bloco curto resumido no fim da tabela:

### 🏆 Tick HH:MM — Quem publicou melhor?

| Quesito | Legado | Reforma | Vencedor |
|---|---|---|---|
| Volume na janela (publish/draft) | X | Y | … |
| Cadência (min/post) | X | Y | … |
| Densidade factual (nº/datas/citações por matéria) | nota | nota | … |
| Tom editorial (ancorado vs panfleto) | nota | nota | … |
| Linha anti-imperialista | ✅/⚠️ | ✅/⚠️ | … |
| Cobertura §93 | X% | Y% | … |
| Vazamento template (mailchimp/script) | sim/não | sim/não | … |
| Categorização correta | sim/não | sim/não | … |

**Vencedor do tick**: <legado/Reforma/empate>
**Pares temáticos comparáveis**: <listar IDs se houver matéria do mesmo tema nos 2>
**Acumulado do dia**: <legado: X-0 / Reforma: 0-Y>

### Quando há par temático (mesmo tema nos 2 sistemas)
Tabela lado a lado: título / fonte / abertura / fechamento / linha editorial / âncora factual. Veredito qualitativo.

Hoje 14/06 conhecemos 1 par direto:
- **Lula G7**: legado #258135/#258175/#258189 (tom diplomático, nome formal "Marco Legal do Transporte Público Coletivo", âncoras factuais) vs. Reforma rascunho_lula.md (tom combativo "preparar embate", "rechaçando subordinação", sem âncora data/nº)
- **Veredito**: Legado venceu (densidade factual + tom mais Cafezinho de hoje)

**Why**: Miguel 14/06 ~19:15 BRT: "agora voce vai fazer o monitoramento de dois sistemas, comparativamente" + ~19:20 BRT "a cada tick de 30 min, voce faz uma análise comparativa, quem publicou melhor".

**How to apply**: Loop §53 ganha 1 passo a mais (PASSO 9): bloco "🏆 Quem publicou melhor?" no fim de cada linha do relatório, com 8 quesitos quantitativos + veredito + pares temáticos quando houver.

Relacionado: [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]] (curas runtime sincronizadas com Reforma), [[project_grande_reforma_lado_a_lado_estado_pausa]] (estado anterior antes do deploy 17:30 BRT 14/06).

## 🆚 Padrão K (DeepSeek 14/06 ~21:45 BRT)

DeepSeek criou o **Padrão K** — comparativo unificado pra TODA a Trindade. Comando `K` (atalho) ou `python3 Cerebro/scripts/comparativo_k.py`. Script local existe em `Cerebro/scripts/` E `scratch/`.

### 9 métricas OBRIGATÓRIAS em todo relatório

| # | Métrica | Fonte canônica | Como obter |
|---|---|---|---|
| 1 | Publicações legado | WP API | `wp/v2/posts?status=publish` |
| 2 | Drafts canário | SQLite | `SELECT COUNT(*) FROM noticias_prontas` |
| 3 | Erros canário | Log | `grep -c 'ERROR\|CRITICAL' canario.log` |
| 4 | LLMs usados | Log | `grep 'provider_final' canario.log` |
| 5 | Tokens gastos | Log | `grep 'tokens' canario.log` |
| 6 | Custo ($) | Log | `grep 'custo' canario.log` |
| 7 | Latência | Log | `grep 'Concluído' canario.log` |
| 8 | Imagens aprovadas | Log | `grep 'Tribunal Visual.*APROVADA' canario.log` |
| 9 | Duplicatas | Log | `grep 'duplicata\|DUPLICATA' canario.log` |

### 6 dimensões em cada post (audit qualitativo)
1. Título — tom, precisão, palavras-chave
2. Corpo — qualidade redação, adjetivação, fidelidade fonte
3. LLM usado — provedor, tokens, custo
4. Fact-check — aprovado/reprovado, policy aplicada
5. Imagem — tem destacada? aprovada?
6. Latência — tempo coleta→publicação

### Sistema de rotação de fórum
- Fórum ativo: `Foruns/forum_comparativo_legado_vs_pos_reforma_<YYYYMMDD>.md`
- A cada 12h: backup datado em `historico_comparativos/forum_comparativo_AAAAMMDD_HHMM.md`
- Novo fórum: limpo, link pro anterior
- Cérebro: `Cerebro/CEREBRO_NODE_CANARIO_POS_REFORMA.md`

### Temas (sem conflito)
- **Legado**: geopolitica, nacional, lula, eleições (4 temas)
- **Canário**: sheinbaum, china, flavio_bolsonaro, crime, militar (5 temas)

### Frequência
- Primeiras 2h: a cada 15-30 min
- Depois: mínimo 1 relatório/dia por engenheiro
- Sempre que houver erro: relatório imediato

### Snapshot adesão minha 14/06 21:43 BRT — 9 métricas
1. 36 publish (legado, confere com K Codex)
2. 13 drafts (SQLite, acumulado pré-canário)
3. 0 erros
4. **VAZIO** (canário não loga provider_final ainda)
5. **VAZIO** (tokens)
6. **VAZIO** (custo)
7. coletor sheinbaum 26s, china 5s, flavio 34s
8. APROVADA=3 / REPROVADA=14 / DUVIDOSA=2 → **74% rejeição imagens!**
9. dedup china=15 + flavio=2 (Jaccard 48h ativo)

### 3 alertas críticos do snapshot
a) Tribunal Visual rejeita 74% das imagens — Wikimedia/banco/sensibilidade
b) Métricas 4-5-6 vazias = instrumentação faltando
c) Pipeline editorial processa pautas LEGADO órfãs (lula/eleicoes/geopolitica/nacional)

**Why**: DeepSeek 14/06 ~21:45 BRT "padrão unificado pra todo mundo comparar do mesmo jeito".

**How to apply**: a cada tick §53 (ou cartinha 6h), gerar tabela com as 9 métricas obrigatórias + auditar últimos posts nos 6 critérios + sinalizar alertas críticos.

## 🏷️ MARCAÇÃO EXPLÍCITA DO SISTEMA (Miguel 14/06 ~22:20 BRT)

A partir de 14/06 22:20 BRT, **TODO monitoramento, relatório, cartinha, tick, alerta** deve deixar CLARO o sistema:

- 🟦 **LEGADO** — Cafezinho ao vivo (publish), motor_publicador.py, maestro_distribuicao.py
- 🟪 **REFORMA** — Cafezinho pós-reforma (canário/draft), publicador_cafezinho.py, maestro_grande_reforma.py

**Formato obrigatório**:
- Postos auditados: `🟦 #258255 [LEGADO]` ou `🟪 #258XXX [REFORMA]`
- Alertas: `🚨 🟦 [LEGADO] maestro crashou` ou `🚨 🟪 [REFORMA] Trib Visual 86%`
- Métricas K: `🟦 LEGADO: 36 publish` vs `🟪 REFORMA: 13 drafts`
- Bugs/curas: `🟦 [LEGADO] bug X em motor_publicador` ou `🟪 [REFORMA] bug Y em pipeline`

**Por que**: Miguel 14/06 22:20 BRT: "todo monitoramento tem que deixar claro se é cafezinho legado ou pos reforma".

**Why**: durante a transição 7 dias, é fácil confundir qual sistema teve o problema. Quem lê (Miguel, Trindade, eu mesmo no próximo tick) precisa saber de relance.

**How to apply**:
- Toda entrada nova no relatorio_monitoramento + relatorio_comparativo + Diário de Bordo + canal + inbox: tagga sistema
- Audit de posts: tagga `[LEGADO]` ou `[REFORMA]` antes do ID
- Comando K já distingue por natureza (publish=legado/draft=canário) — manter
- Alertas críticos: prefixo `🟦` ou `🟪` antes do tema

## 🏷️ AMPLIAÇÃO: 4 origens marcadas (Miguel 14/06 ~22:25 BRT)

Diferenciação ampliada de 2 sistemas (🟦+🟪) pra **4 origens**:

| Emoji | Sigla | Sistema | Saída |
|---|---|---|---|
| 🟦 | [LEGADO] | Cafezinho legado (motor v2.1) | publish ao vivo |
| 🟪 | [REFORMA] | Cafezinho pós-reforma (canário) | status=draft |
| 🟧 | [AGY-DESKTOP] | Antigravity Desktop (engenheiro humano-assistido, Miguel + agente) | manual/variável |
| 🟨 | [AGY-CLI] | AGY CLI (auditor cmd-line da Trindade no Tencent) | pareceres em fóruns |

**Por que separar 🟧 de 🟨**: Antigravity Desktop é humano-assistido (Miguel + agente colaborando), os outros 3 são autônomos. Misturar mascara contribuição manual.

**Comando K — saídas separadas por origem**:
- `K` Trindade (Cerebro/scripts/comparativo_k.py): 🟦 vs 🟪
- `K` AGY-DESKTOP: saída exclusiva 🟧 (matérias preparadas manualmente, posts revisados)
- AGY-CLI não tem K próprio — usa o da Trindade

**Cartinha**: `Foruns/forum_marcacao_sistemas_monitoramento_20260614.md` (publicada 22:25 BRT).

**Why**: Miguel 14/06 ~22:25 BRT — "todo monitoramento tem que deixar claro se é cafezinho legado ou pos reforma" + "inclusive antigravity desktop (diferenciar do agy cli). monitoramento do antigravity desktop seja diferenciado de todos. também acionado pela letra k".

**How to apply**: tagga TODOS os IDs/métricas/alertas com 🟦/🟪/🟧/🟨. K Desktop tem saída separada do K Trindade.
