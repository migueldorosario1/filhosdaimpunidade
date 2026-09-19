---
name: feedback-usar-ponte-zcode-para-ajuda
description: "ZCode pode me ajudar sempre - corrigir bugs, construir conhecimento, decidir editorial. Usar inbox_trindade/zcode.md com tag [CLAUDE-XXX-ZCODE-YYYYMMDD-HHMM]. Miguel 11/08 03:37 BRT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

Sempre que estiver com dúvida técnica/editorial não trivial, **usar a ponte ZCode** — não me limitar a resolver sozinho.

**Como:** escrever cartinha em `inbox_trindade/zcode.md` com tag `[CLAUDE-<slug>-ZCODE-YYYYMMDD-HHMM]` — 3-5 linhas: (a) contexto, (b) dúvida específica, (c) opções que considero, (d) qual info do ZCode ajudaria. ZCode roda Kimi K3 / GLM 5.2 / Qwen 3.8 alternadamente.

**Quando escalar pra ZCode:**
- Bug complexo em código que não estou seguro de fix
- Decisão editorial ambígua (post com dúvida ética/factual)
- Análise de padrão em muitos bugs (ZCode pode ver logs V4 no NYC que eu não vejo diretamente)
- Refatoração/arquitetura de sistemas (V4, sentinela, worker, banco de mídia)
- Verificação factual em português/idioma que exija leitura fina de fonte estrangeira

**Não escalar quando:**
- Task trivial que resolvo em <5min sozinho
- Ciclo Vigília padrão (DS+GPT+meu WebSearch já é o pipeline)
- Comando ad-hoc simples do Miguel

**Why:** Miguel 11/08 03:37 BRT: "usa a ponte com o zcode. ele pode te ajudar sempre. [...] o zcode pode te ajudar a corrigir as coisas, e a construír um bom conhecimento." Reforço explícito de que trindade Claude+ZCode+Miguel é o modo de operação, não fluxo Claude-só.

**How to apply:** Antes de responder ao Miguel com "não sei" ou "tem risco desconhecido", verificar se cartinha ZCode resolveria. Também: ZCode consome logs V4 diretamente no NYC via SQLite — pode fazer análises que eu não faço (padrões de bug worker, drift de schema, etc.).

Regras irmãs: [[feedback-nomenclatura-zcode-ambiente-nao-kimi]] · [[feedback-proveniencia-modelo-ambiente-papel-separados]] · [[feedback-ponte-claude-kimi-arquivo-por-turno]] · [[feedback-ponte-imagens-v3-regime-autonomo]]
