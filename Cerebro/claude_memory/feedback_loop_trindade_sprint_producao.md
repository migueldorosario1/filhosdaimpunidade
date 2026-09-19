---
name: Loop Trindade = Sprint de Produção
description: Loop Trindade serve pra avançar sprint de código/arquitetura, não monitoramento técnico; default Codex coda, Claude supervisiona+ajuda, Antigravity arquiteta+supervisiona
type: feedback
originSessionId: 7ebc1fdb-8b69-448d-9b24-9dd71245a752
---
# Regra: Loop Trindade = Sprint de Produção

**Propósito:** Loop Trindade é pra avançar a frente ativa de código/arquitetura. **NÃO é monitoramento técnico** (sangria, sentinela, posts) — isso é outro instrumento.

**Sequência obrigatória do tick:**
1. Olhar `Foruns/canal_claude_antigravity.md` → identificar sprint ativo + última msg.
2. Olhar fórum correspondente (ex: `forum_youtube_autonomo_textos.md`, `forum_zizilinda.md`).
3. **Avançar a sprint** conforme o estado.

**Default (sem ordem específica):**
- **Codex coda sozinho** — executor.
- **Claude supervisiona + ajuda** — audita, valida, dá parecer, sugere patches.
- **Antigravity ajuda na arquitetura + supervisão** — propõe desenho, ratifica.

**O que cada tick deve fazer:**
- Codex pediu parecer/auditoria → dar.
- Codex pediu validação → validar (smoke, py_compile, leitura linha-a-linha).
- Antigravity propôs arquitetura → ratificar ou contraproposta.
- Sprint travada → propor próximo passo concreto.
- Sprint pausada e sem demanda → monitor compacto e seguir.

**Anti-padrões proibidos:**
- Tick gastando tokens em monitoramento técnico denso quando sprint exige avanço de código.
- Claude codando em produção (default sprint é Codex coda).
- Esperar autorização explícita pra cada passo se Codex já está dentro do escopo aprovado.

**Why:** Miguel observou que ticks estavam saindo do propósito da sprint e indo pra checagens técnicas defensivas. Loop é pra **PRODUZIR**, não pra checar se sangria voltou. Monitoramento entra como verificação de fundo compacta, não como foco.

**Origem:** Miguel 2026-05-06 08:18 BRT. Registrado em `CEREBRO_NODE_GOVERNANCA.md §19`.
