---
name: project-monitoramento-editorial-humano-claude-leitor
description: "Claude é leitor designado do Doc de revisão editorial Miguel (Google Doc público). Ciclo recorrente: lê → fórum diário → BUGs no Cérebro → trindade opina → consenso 3/3 obrigatório antes de patch. Override do §51 (sem autocura solo). Formalizado 2026-05-19 08:00 BRT."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4c52d90e-06f8-4198-8f65-dc7d7dc0c759
---

# Monitoramento Editorial Humano — Claude é leitor designado

**Fato:** Miguel mantém revisão editorial diária do Cafezinho num Google Doc compartilhado público (https://docs.google.com/document/d/1yZe_bG8hl1_sqxMfuXAiNrMvFczpQu59HrVjK7tI4EY/edit). Em 2026-05-19 (07:50-08:02 BRT) instituiu ciclo recorrente formalizado: cada dia revisado vira insumo pra ajustar agentes de produção, **Claude é o leitor designado**, e mudanças exigem **consenso 3/3 Trindade técnica antes de qualquer patch**.

**Why:**
- Detectar problemas editoriais (títulos cara-IA, capitalização, imagens em inglês, duplicadas, curtas, formatação) e transformar em correção sistêmica nos agentes
- Erro de hoje deixa de aparecer amanhã (ciclo de melhoria contínua)
- Claude tem vantagem em leitura+síntese pra primeira passada; Trindade entra pra validar diagnóstico+patch

**How to apply:**

### Quando trigger acontece (Miguel sinaliza "doc atualizado" ou cron diário 09:00 BRT)

1. **WebFetch o doc:**
   ```
   WebFetch URL = https://docs.google.com/document/d/1yZe_bG8hl1_sqxMfuXAiNrMvFczpQu59HrVjK7tI4EY/export?format=txt
   ```
   (Pode redirecionar — seguir redirect)

2. **Comparar com `Foruns/forum_monitoramento_editorial_humano.md` §4** (índice de datas processadas). Só processar datas NOVAS.

3. **Pra cada data nova:**
   - Criar `Foruns/forum_monitoramento_editorial_<YYYYMMDD>.md` (1 fórum por dia, não acumular)
   - Detalhar itens: número, descrição, categoria (taxonomia §73.2), status [CORRIGIDO/PENDENTE]
   - Pra cada item crítico ou recorrente, criar entrada em `CEREBRO_NODE_BUGS.md`:
     - ID: `BUG-YYYYMMDD-MONITOR-CATEGORIA-DESCRITIVO`
     - Assinatura: `— Claude, YYYY-MM-DD HH:MM BRT (monitoramento editorial Miguel)`
     - Status inicial: `ABERTO — aguardando consenso Trindade`
   - Atualizar §4 do fórum-mãe com data + nº itens + link pro fórum do dia

4. **Pontuar no canal trindade:**
   ```
   [HH:MM BRT] Claude → Trindade (monitoramento editorial — data YYYY-MM-DD indexada):
   N itens detectados, M classificados como [CATEGORIA], K já corrigidos no dia, P abertos.
   Fórum do dia: Foruns/forum_monitoramento_editorial_YYYYMMDD.md
   BUGs novos no Cérebro: BUG-YYYYMMDD-MONITOR-*
   Convoco Codex+DS+AG a postar parecer no §X do fórum do dia.
   Sem patch sem consenso 3/3.
   ```

### Taxonomia (6 categorias, §73.2 Cérebro)

- 🅐 **Títulos cara-IA** → patch: prompt manchete + few-shot
- 🅑 **Capitalização** → patch: expandir `_NOMES_PROPRIOS` em `titulo_utils.py`
- 🅒 **Imagens em inglês ou incongruentes** → patch: Tribunal Visual + gate OCR
- 🅓 **Matérias duplicadas** → patch: dedup robusto (NER ou hash semântico, não só Jaccard >0.60)
- 🅔 **Matérias curtas demais** → patch: `MIN_CHARS_MATERIA`
- 🅕 **Formatação** → patch: linter pós-publicação

### REGRA CRÍTICA — consenso obrigatório (§73.5.4 Cérebro)

**Override do §51 padrão pra esta frente:** mesmo bugs simples (5 linhas, expandir dicionário) exigem **Trindade técnica 3/3 (Codex+DS+Claude) endossando** antes do patch entrar.

Sem consenso = item fica ABERTO. Não há autocura solo aqui.

Hierarquia:
- 3/3 → CODAR + DEPLOYAR direto
- 2/3 → CODAR localmente, espera 3º
- 1/3 só (Claude isolado) → **não coda**
- Veto chinês de risco → escala Miguel imediato
- Override Miguel ("aplica agora") → autoriza sem esperar

### Estado inicial (19/05/2026)

- 2 datas indexadas: 14/05 (23 itens) + 19/05 (21 itens)
- 6 TASKs ME-1 a ME-6 abertas no fórum-mãe §7
- Achado mais grave: 🅓 6 duplicatas no dia 19/05 = filtro Jaccard vazando, patch urgente

### Arquivos a tocar

- `Foruns/forum_monitoramento_editorial_humano.md` — HUB/ÍNDICE (não acumular conteúdo aqui)
- `Foruns/forum_monitoramento_editorial_<YYYYMMDD>.md` — 1 por data nova
- `CEREBRO_NODE_GOVERNANCA.md` §73 — protocolo formal
- `CEREBRO_NODE_BUGS.md` — BUG-YYYYMMDD-MONITOR-*
- `Foruns/canal_trindade.md` — pontuação

Relacionado: [[feedback_re_sincronizar_antes_de_postar_coordenacao]] (sempre re-sync canal antes de coordenar cross-agente), [[feedback_verificar_premissa_antes_decisao]] (verificar state atual antes de propor decisão).

— Protocolo formalizado por Miguel 2026-05-19 07:58-08:00 BRT.
