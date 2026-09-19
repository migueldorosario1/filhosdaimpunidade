---
name: feedback-cortar-assinatura-estagiario-agencia-brasil
description: "Cafezinho republica Agência Brasil sob assinatura editorial própria — sempre CORTAR frases tipo `*Estagiário da Agência Brasil sob supervisão de X` no rodapé. Não interessa se foi estagiário. Fix aplicado no `agente_repetidor_estatal.py` (3 regex antes do return de extrair_html_e_titulo) + limpeza in-place em posts existentes."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-24 11:35 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

## Regra

**Sempre cortar** do corpo de posts republicados assinaturas do tipo:
- `*Estagiário da Agência Brasil sob supervisão de <Nome>`
- `Estagiária sob supervisão de <Nome>` (com ou sem `<p>`, com ou sem asterisco)
- Variações genéricas: `sob supervisão de`, `sob orientação de`

**Why:** Miguel 2026-07-24 11:20 BRT: *"bota na diretriz do repetidor estatal para cortar esse tipo de frase no final. não interessa se foi estagiário que escreveu."* Cafezinho republica sob sua assinatura editorial — assinatura de agência-origem (EBC/Agência Brasil, futuros: Radioagência Nacional, TV Brasil, etc.) é ruído, não crédito. O crédito canônico ao veículo original já vem no bloco "Fonte:" com link.

**How to apply:**

### 1. Upstream (agente republicador)
Todo agente que republica conteúdo de agências estatais (`/root/agente_repetidor_estatal.py` no NYC) deve ter, na função de extração final do corpo (`extrair_html_e_titulo`), 3 regex antes do return removendo:
- `<p>\s*\*?\s*Estagi[áa]ri[oa].{0,120}?sob\s+supervis[ãa]o[^<]{0,200}?</p>\s*`
- `<p>\s*\*?\s*Estagi[áa]ri[oa].{0,120}?sob\s+supervis[ãa]o[^<]{0,200}?(?=<p|<!--|\Z)` (sem `</p>`)
- `^\s*\*?\s*Estagi[áa]ri[oa].{0,120}?sob\s+supervis[ãa]o[^\n]{0,200}\s*$` (linha nua)

Aplicado em `/root/agente_repetidor_estatal.py` 24/07 11:34 BRT. Backup `.bak_pre_claude_estagiario_20260724_1132` SHA-256 `b52ea08a5f744370821b52630285acc15e6e7e37f89bb16e8fd412b1863c9227`.

### 2. Downstream (posts já publicados)
Ao detectar essa assinatura em post publicado (via Sentinela ou scan), remover in-place via `POST /wp-json/wp/v2/posts/{id}` preservando `status=publish` (regra CHURN — nunca rebaixar). Fazer scan retroativo 30d periódico.

Casos fundadores 24/07: 262732 (Miguel identificou), 262726 (scan), 262249 (scan). Todos limpos in-place.

### 3. Ampliação futura
Se aparecer padrão novo de assinatura de agência estatal (`Reportagem produzida em parceria com...`, `Sob supervisão do editor <X>`, `Redação apoiada por...`, `Estágio patrocinado por...`), acrescentar aos `_PADROES_ASSINATURA_ESTAGIARIO` no repetidor + rodar scan retroativo. Considerar futuramente ampliar pra padrões genéricos `sob orientação de`, `produzida por estagiários` etc.

## Erro que precisa ser evitado

Deixar passar assinaturas de agência-origem — quebra a linha editorial do Cafezinho (parece que o Cafezinho tem estagiário quando é o estagiário da EBC).

## Relacionadas

- [[feedback-protocolo-memoria-bugs-ler-antes-agir]] — protocolo de correção 3 camadas
- Manual bugs: entrada #25 em `Outros/manual_de_bugs.md`
- Nodo canônico: linha `assinatura_estagiario_agencia_brasil` em `CEREBRO_NODE_BUGS_SOLUCOES.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-24 11:35 BRT.
