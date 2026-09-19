---
name: Orçamento de tokens antes + custo real depois (Claude_Financas)
description: Antes de toda missão, estimar tokens e dar preço em USD/BRL. Depois de entregar, anotar custo real em Financas/Claude_Financas/Claude_Financas.md.
type: feedback
originSessionId: 194b7409-a046-4f3f-8022-79c63cec32c0
---
**Regra:** toda missão (qualquer pedido não trivial do Miguel) começa com uma **estimativa de custo** e termina com uma **anotação do custo real** no arquivo `Financas/Claude_Financas/Claude_Financas.md` (na raiz do projeto).

**Why:** Miguel quer disciplina de custo e visibilidade do consumo computacional ao longo do tempo. Ele está na **assinatura Max 20** (não paga por token), então os valores são *equivalentes-API* — referência de consumo, não cobrança real. Mas o registro serve pra: (1) calibrar minhas próprias estimativas, (2) detectar missões caras pra discutir trade-off, (3) histórico de uso.

**How to apply:**

0. **Antes de orçar:** ler a seção **"📚 Heurísticas calibradas por categoria"** em `Financas/Claude_Financas/Claude_Financas.md`. Identificar em qual categoria a missão se encaixa (criar .md, fix de bug, investigação, deploy, refatoração, etc.). Se nenhuma categoria existente cabe, criar linha nova na tabela com a primeira medição (marcando "provisório — 1 amostra").

1. **Antes de codar (resposta inicial):** estimar `input ≈ X tokens, output ≈ Y tokens` partindo da heurística da categoria (ajustando pra mais/menos por contexto). Multiplicar pela tabela vigente, dar **USD e BRL** e **citar a categoria**. Exemplo:
   *"Categoria: investigação multi-arquivo. Estimativa: ~40k input + 2k output ≈ US$ 0,25 ≈ R$ 1,25."*
   - Pular esta etapa para tarefas triviais (responder uma pergunta curta, 1 leitura de arquivo). Usar bom senso: se vou usar mais de ~3 tool calls ou criar/editar arquivos, vale orçar.

2. **Tabela de preços vigente (Opus 4.7, abr/2026):**
   - Input: US$ 5/M • Output: US$ 25/M • Cache write: US$ 6,25/M • Cache read: US$ 0,50/M
   - Sonnet 4.6: $3 / $15 / $3,75 / $0,30
   - Haiku 4.5: $1 / $5 / $1,25 / $0,10
   - Fonte canônica: `monitor_gastos_claude.py` (raiz do projeto) — se mudar preço, atualizar lá primeiro.

3. **Cotação USD→BRL:** puxada **1× por dia** (na primeira mensagem do dia ao Claude) com `curl -s --max-time 5 "https://open.er-api.com/v6/latest/USD" | python3 -c 'import json,sys; print(json.loads(sys.stdin.read())["rates"]["BRL"])'` e usada por 24h. A cotação do dia fica registrada na seção **"💱 Cotação USD→BRL do dia"** no topo de `Financas/Claude_Financas/Claude_Financas.md` — sempre **ler de lá primeiro**; só rodar o curl se não houver registro do dia atual ou se a data registrada for de outro dia.

4. **Depois de entregar:** rodar `python3 monitor_gastos_claude.py` na raiz, pegar o número REAL da sessão atual (linha do Opus 4.7), e anotar nova linha na tabela de **Histórico** em `Financas/Claude_Financas/Claude_Financas.md`. Colunas: data/hora, missão, modelo, estim USD, estim BRL, real USD, real BRL, Δ%, notas.

5. **Calibração (loop de aprendizado):**
   - Se Δ ≥ 30% (pra mais ou pra menos): atualizar a linha da categoria em "📚 Heurísticas calibradas" com a média ponderada das últimas 3 amostras daquela categoria.
   - Se Δ ≥ 100%: atualizar imediato (não esperar 3 amostras), e investigar por que a estimativa errou tanto.
   - O objetivo é que estimativas convirjam em ±20% do real depois de ~5 missões da mesma categoria.

6. **Localização canônica do arquivo:** `~/Downloads/Antigravity Google/Financas/Claude_Financas/Claude_Financas.md`. NÃO criar duplicatas em outros lugares.
