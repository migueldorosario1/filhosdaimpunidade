---
name: feedback-processo-autoaprendizado-ler-memoria-todo-ciclo-20260815
description: "Regra de meta-processo Miguel 15/08/2026 11:35 BRT — todo erro DEVE ser (1) registrado no JSONL, (2) indexado no MEMORY.md, (3) transformado em diretriz permanente (memory + contratos V4), (4) lido ANTES de cada ciclo. Sistema deve autoaprender: erros de ontem viram gates de hoje."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 15/08/2026 11:35 BRT (após incidente 265876 utm_openai): "todo erro precisa ser registrado, indexado, e a solução transformada em diretrizes, acrescenta um resumo nas diretrizes do v4 e voce mesmo sempre le a memoria antes de executar o loop para termos um processo de autoaprendizdo."

## Ciclo completo do autoaprendizado

Todo erro passa por **5 fases obrigatórias**:

### 1. REGISTRO (imediato, no momento da detecção)
- Log em `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl`
- Uma linha JSON com: `ts`, `tipo`, `post_id` ou entidade, `descricao`, `causa`, `detectado_por`, `impacto`

### 2. INDEXAÇÃO (no mesmo ciclo)
- Nova entrada topo do `MEMORY.md` (arquivo de memória Claude Code, sempre carregado)
- Link `[[nome-slug]]` pra arquivo de memória detalhado

### 3. DIRETRIZ PERMANENTE (mesmo ciclo)
- Arquivo `feedback_<slug>.md` ou `reference_<slug>.md` no diretório de memória
- Formato: fato + Why + How to apply + relacionados

### 4. INTEGRAÇÃO NA FÁBRICA V4 (mesmo dia)
- Adendo/resumo no `README.md` do diretório de contratos V4 (`Cerebro/Foruns/loop_trindade_laura/README.md` OU `v4_labs/contratos/README.md` OU criar `V4_DIRETRIZES_APRENDIDAS.md`)
- Todo contrato de vertical pode referenciar essa síntese
- **ZCode/worker upstream** também consome esse resumo pra manter fix estrutural alinhado

### 5. LEITURA ANTES DE CADA CICLO (para todo agente Trindade)
- **RITUAL OBRIGATÓRIO INÍCIO SLOT A/B**: primeira ação do ciclo = ler `MEMORY.md` (pelo menos o topo — últimas 10 entradas)
- Sem essa leitura, corro risco de repetir erro de ontem por já ter esquecido a regra
- Aplica-se a Claude Miguel, Claude Laura, Grok Miguel, Grok Laura, Codex, ZCode — todos que operam sobre Cafezinho

## Novo ritual de ciclo Vigília V6 (a partir de agora)

```
1. date +"%H:%M" (identifica Slot A/B)
2. **LEIA MEMORY.md TOPO** (últimas 10 entradas — reancorar regras aprendidas)
3. grep ABERTO em fila_para_claude.md
4. tail em inbox_trindade/claude.md (canal antigo)
5. wp post list --status=future (fila real WP)
6. wp post list drafts autor 5786 cutoff 2h
7. Pra cada draft: aplicar pipeline v5 (agendar) COM gates aprendidos
8. Log JSONL + ciclos_vigilia_MD
9. Se bug novo detectado: aplicar 5 fases do autoaprendizado
```

## Como isso muda meu comportamento operacional

**ANTES** (até 15/08 11:35): eu lia MEMORY.md só no início da sessão. Confiava na memória curta pra manter regras aplicadas ao longo dos ciclos. Se surgisse regra nova durante a sessão, aplicava mas nem sempre reancorava.

**DEPOIS** (a partir de agora): TODO Slot começa com re-leitura das últimas entradas MEMORY.md (barato — arquivo já sincronizado localmente). Custo LLM baixo (200 linhas de texto), ganho enorme (nunca esqueço regra recente).

**Meta:** o sistema Trindade deve ficar mais inteligente a cada dia, não mais burro. Erros passados viram infrastructure — gates preventivos rodam automaticamente, sem depender de eu lembrar.

## Auditoria de conformidade

Uma vez por semana: revisar `bugs_encontrados/*.jsonl` — pra cada bug detectado, confirmar que:
1. Existe entrada MEMORY.md correspondente
2. Existe arquivo de detalhe `feedback_/reference_/project_.md`
3. Existe menção em `V4_DIRETRIZES_APRENDIDAS.md` (a criar)
4. Pipeline `agendar()` tem gate ativo pra detectar recorrência

Se qualquer um dos 4 faltar → bug do processo (não do worker), retroalimentar.

## Relacionados

- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]] — corrige NA CAUSA-RAIZ
- [[feedback-gate-metalinguagem-deve-inspecionar-href-nao-so-texto-20260815]] — exemplo vivo aplicado
- [[feedback-migracao-canal-fechar-loop-no-antigo]] — outra regra derivada de erro
- [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]] — regra derivada de observação

## Regra âncora

**"Erro registrado, indexado, virado diretriz, integrado à fábrica, lido no próximo ciclo. Sem essas 5 fases, o erro volta."** — Miguel, 15/08 11:35 BRT
