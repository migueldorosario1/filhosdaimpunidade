---
name: feedback-protocolo-memoria-bugs-ler-antes-agir
description: "Antes de aplicar QUALQUER correção, consultar Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md + Outros/manual_de_bugs.md + JSONL. Guardar TUDO após correção (3 camadas: instância, padrão, aprendizado). Cérebro é fonte compartilhada entre agentes."
metadata:
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-24 01:25 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra inviolável

**A cada correção de bug no Cafezinho:**

1. **ANTES de agir** — CONSULTAR memória de bugs em 3 lugares (nessa ordem):
   - `Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` (nodo canônico, panorama geral)
   - `Outros/manual_de_bugs.md` (padrões estruturais #1-#22+)
   - `Cerebro/monitoramento_horario/bugs_encontrados/bugs_*.jsonl` (frequência histórica)
2. **Se bug conhecido:** aplicar solução já validada (NÃO reinventar)
3. **Se bug novo:** investigar + aplicar fix
4. **DEPOIS de agir** — GUARDAR em 3 camadas:
   - JSONL do dia (instância individual)
   - Manual de bugs (se for padrão novo)
   - Memória permanente feedback_*.md (se for regra editorial/arquitetural)
   - CEREBRO_NODE_ATUALIZACOES.md (se for fix estrutural)
   - Atualizar tabelas em `CEREBRO_NODE_BUGS_SOLUCOES.md`

**Why:** Miguel 2026-07-24 01:20 BRT: *"A cada loop, você encontrar qualquer coisa, você guarda. E você tem que, a cada correção, ler a memória de bugs para identificar se tem algum erro se repetindo e para encontrar a solução. O cérebro tem que ter uma sessão muito bem organizada. Você tem que aprender, ter memória dos erros. Guardar tudo — depois a gente roda outra inteligência para te ajudar, tudo tem que estar no cérebro."*

## Motivação editorial e técnica

- **Editorial:** bugs se repetem — ponto e vírgula em título, fontes coladas, sujeira metadata. Se cada vez eu invento fix novo, desperdiço tempo/tokens. Se leio o manual primeiro, aplico solução testada.
- **Colaboração agente-a-agente:** Kimi, Codex, GLM, novas sessões Claude precisam consultar cérebro pra entender contexto. Se memória não está organizada, cada agente reinventa e diverge.
- **Aprendizado composto:** ler memória sistematicamente + guardar tudo cria loop virtuoso — cérebro fica mais denso com o tempo, correções ficam mais rápidas e precisas.

## How to apply

### 1. Prompt do Sentinela
DeepSeek já recebe regras editoriais no `config/prompts.md` — isso é a versão "compilada" do manual. Se manual ganha entrada nova (bug estrutural), sincronizar no prompt.

### 2. Sessão Claude Code (eu, aqui no chat)
Ao começar tarefa de correção:
```bash
# 1. Panorama
cat "Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md" | head -60

# 2. Se bug de tipo específico:
grep -A 20 "^## 22\." "Outros/manual_de_bugs.md"    # padrão estrutural
grep "fonte_colada" Cerebro/monitoramento_horario/bugs_encontrados/bugs_*.jsonl | wc -l  # frequência
```

Se solução já validada existe, aplicar. Se não, investigar.

### 3. Depois da correção
Rotina obrigatória (nem que seja 30 segundos):
```bash
# Instância → JSONL
echo '{"ts_brt":"...", "post_id":..., "tipo_bug":"...", ...}' >> bugs_YYYY-MM-DD.jsonl

# Padrão novo → manual (se aplicável)
# Editar Outros/manual_de_bugs.md, adicionar seção ## N.

# Aprendizado editorial → memória
# Criar/atualizar ~/.claude/.../memory/feedback_*.md

# Fix estrutural → atualização cérebro
# Editar Cerebro/CEREBRO_NODE_ATUALIZACOES.md
```

### 4. Passagem pra agente futuro
Toda memória tem cabeçalho identificando autor (Claude Code, Kimi, Codex) e data. Isso permite qualquer agente futuro entender contexto e não confundir com regra própria.

## Erro que precisa ser evitado

**Aplicar fix sem consultar memória.** Sintomas:
- Reinventar prompt de correção que já existe
- Criar entrada duplicada no manual
- Bug se repete 10x sem virar padrão estrutural
- Miguel tem que apontar o mesmo problema várias vezes ("já não te disse isso?")

Se me pegar fazendo isso, é regressão. Miguel me lembra.

## Nodo canônico criado 2026-07-24

`Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` centraliza:
- Tabela de bugs catalogados (#1-#22 + regras D/CHURN/CAL/SEMANT/META/SCORE/TRIB)
- Mapeamento tipo_bug → manual/memória/solução automatizada
- Métricas agregadas por dia (JSONL)
- Protocolo de ler-antes-agir + guardar-tudo-depois

## Relacionadas

- [[manual-de-bugs-ler-primeiro]] — protocolo original (2026-04-18, ainda válido)
- [[feedback-indexar-bugs-e-curas-no-cerebro-inegociavel]] — regra semelhante do Miguel em 2026-04
- Todas as memórias `feedback_*` e `project_*` do workspace
- `CEREBRO_NODE_BUGS_SOLUCOES.md` (nodo canônico)
- `Outros/manual_de_bugs.md` (padrões estruturais)
- `Cerebro/monitoramento_horario/bugs_encontrados/*.jsonl` (instâncias)

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-24 01:25 BRT.
