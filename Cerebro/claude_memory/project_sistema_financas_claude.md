---
name: Sistema de Finanças do Claude — visão geral
description: Sistema completo de controle de gastos com Claude (cotação 1x/dia, estimativa+real, heurísticas, footer, loops com auto-stop). Construído 2026-04-27.
type: project
originSessionId: 194b7409-a046-4f3f-8022-79c63cec32c0
---
**Fato:** existe um sistema integrado de **controle de gastos do Claude** no projeto Cafezinho, construído em 2026-04-27 numa sessão de ~R$ 57 que custou caro mas estabeleceu disciplina financeira pro mês inteiro.

**Why:** Miguel está na assinatura **Max 20** (não paga por token), mas quer **disciplina de custo** equivalente-API pra: (1) calibrar suas próprias intuições sobre consumo, (2) detectar missões caras pra discutir trade-offs antes de tocar, (3) construir histórico de uso ao longo do mês.

**How to apply (ritual de toda missão não-trivial):**

1. **Cotação USD→BRL do dia:** ler topo de `Financas/Claude_Financas/Claude_Financas.md`. Se data ≠ hoje, rodar curl da `open.er-api.com` 1× e atualizar a tabela. Válida 24h. Detalhe em [`feedback_orcamento_antes_e_real_depois.md`](feedback_orcamento_antes_e_real_depois.md).

2. **Estimativa antes:** consultar tabela "📚 Heurísticas calibradas por categoria" em `Financas/Claude_Financas/Claude_Financas.md`. Identificar categoria da missão. Multiplicar tokens × preço × cotação, dar **USD e BRL**. Citar a categoria.

3. **Footer no fim de cada msg:** rodar `python3 scripts/cost_session.py` (na raiz do projeto). Cola o footer pronto. Detalhe em [`feedback_footer_custo_por_mensagem.md`](feedback_footer_custo_por_mensagem.md).
   - Importante: o script foi consertado em 12:21 BRT pra distinguir `user` real de `tool_result` (antes estava subestimando "essa msg").

4. **Custo real depois:** rodar `python3 monitor_gastos_claude.py` (raiz), pegar delta de Opus 4.7 da sessão, anotar linha nova em "📊 Histórico" em `Claude_Financas.md` com Δ%.

5. **Loop de calibração:** se Δ ≥ 30%, atualizar a linha da categoria em "Heurísticas calibradas". Se Δ ≥ 100%, atualizar imediato + investigar por que errou tanto.

**Tabela de preços canônica:** vive em `monitor_gastos_claude.py` (raiz do projeto). Atualmente (abr/2026):
- Opus 4.7: $5/$25 input/output (cache wr $6,25 / cache rd $0,50 por M tokens)
- Sonnet 4.6: $3/$15 ($3,75 / $0,30)
- Haiku 4.5: $1/$5 ($1,25 / $0,10)

**Heurísticas atuais (calibradas com dados reais de 2026-04-27):**
- Categoria 1 (criar/atualizar .md grande + memórias, 1 turno): ~R$ 5–10/turno (4 amostras)
- Categoria 7 (investigação tool-pesada + criar script + memórias, multi-turno): ~R$ 19–23/turno
- Categorias 2–6 ainda pendentes de calibração — preencher conforme aparecerem.

**Aprendizados-chave de 2026-04-27 (sessão fundadora):**
- **Subestimei MUITO** estimativas iniciais — preços que usei (Opus $15/$75) eram da geração legada Opus 4.1; preço atual Opus 4.7 é $5/$25 (3× mais barato). Sempre conferir tabela vigente.
- Loops em cadência 2m rodando paralelos por horas geram gasto Haiku surpreendente (R$ 49,20 em 3h33min hoje cedo). Por isso a regra `feedback_loops_regras_cadencia_e_duracao.md`: cadência mín 5m, duração máx 1h.
- Tool calls em série (5+ por turno) custam mais do que parece — categoria 7 deu R$ 19/turno num único turno com 8 tool calls.
- O script `cost_session.py` original tinha bug no agrupamento de turnos (tratava tool_results como mensagens reais do user). Consertado.
- Cache_read é a categoria mais barata ($0,50/M Opus) e a maioria do contexto é cache. Sessões longas ainda assim acumulam por causa do output (fala do Claude).

**Arquivos canônicos do sistema:**
- `Financas/Claude_Financas/Claude_Financas.md` — registro humano-legível (cotação, protocolo, heurísticas, histórico, resumo mensal)
- `monitor_gastos_claude.py` (raiz) — calcula custo real lendo JSONLs de `~/.claude/projects/`
- `scripts/cost_session.py` — gera footer de cada mensagem
- Memórias de feedback relacionadas:
  - `feedback_orcamento_antes_e_real_depois.md`
  - `feedback_footer_custo_por_mensagem.md`
  - `feedback_loops_regras_cadencia_e_duracao.md`

**Status do roteador Haiku→Opus:** ✅ IMPLEMENTADO em 2026-04-27 12:32. Memória [`feedback_router_classificador_haiku.md`](feedback_router_classificador_haiku.md) tem regras completas: tabela TRIVIAL/MÉDIO/COMPLEXO, trava de DÚVIDA via Sonnet, override manual com prefixos `[OPUS]`/`[SONNET]`/`[HAIKU]`, regras especiais (deploy/produção sempre Opus), e seção "Lições aprendidas" que cresce com erros. **Para ativar:** Miguel roda `/model haiku` (decisão manual dele). Economia esperada ~80%.
