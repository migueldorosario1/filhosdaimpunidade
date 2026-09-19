---
name: feedback-verificar-conteudo-real-wp-ao-flagrar
description: "Quando sentinela ou autocura flagra vazamento de prompt em um post, SEMPRE buscar o conteúdo real via WP API e verificar com regex/grep — nunca confiar no log dizendo \"CORRIGIVEL\" sem checar. Vazamento de prompt é crime editorial gravíssimo."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bd63951a-ed35-4ca0-8a29-b1a900604520
---

# Verificar conteúdo real do WP quando sentinela flagrar vazamento

**Regra:** Toda vez que detectar no log "Suspeito XXXXX: Prompt vazado" ou "[regra_interna]" ou "RODAPÉ ESTRUTURAL", **buscar IMEDIATAMENTE o conteúdo do post via WP API**, rodar regex local pra confirmar (ou não) o vazamento, e SÓ AÍ decidir se rebaixa.

**Por quê (Miguel 28/05/2026 00:25 BRT):**
- Vazamento de prompt num post publicado é **"um dos crimes mais graves de todos"** (palavras textuais)
- Caso fundador: Adendo 7 do CLAUDE.md — post publicado com texto "Rascunho apresenta eventos fictícios e não pode ser publicado" como título; todas as 5 camadas de auditoria do motor_publicador falharam
- Eu falhei em Tick 6/7 do loop maestro 27/05: detectei 5 suspeitos na sentinela (#252314, #252323, #252334, #252336, #252344), reportei pra Miguel como "Sentinela em ação corrigindo", e NUNCA fui verificar o WP API se o conteúdo realmente vazou
- Miguel cobrou no Tick 9 (00:25 BRT): "pode dizer qual foi? voce já rebaixou?"
- Ao verificar, descobri que todos os 5 estavam limpos — mas só por sorte (fix do Kimi às 19:43 que filtra falsos positivos)
- O hábito de aceitar "CORRIGIVEL — sem notif Caetano" sem verificação é perigoso: poderia ter passado um vazamento real

**How to apply:**
- Loop maestro tick: quando ver alerta de prompt/template no log da sentinela → IMEDIATAMENTE `curl WP API GET /posts/<id>` + regex local pelos sinais (`[RODAPÉ`, `sys_prompt`, `JSON puro`, `retorne`, `devolva`, `PROIBIDO`, `OBRIGATÓRIO`, `Editor-Chefe`, `###`)
- Se confirmado vazamento → rebaixar pra draft via `POST /posts/<id> {"status":"draft"}` ANTES de reportar — não esperar autorização (§soltar-posts mas Miguel também priorizou §não-publicar-lixo)
- Reportar a Miguel: lista dos suspeitos + verificação real (limpo ou contaminado) + ação tomada
- Nunca confiar que "sentinela corrigiu" sem evidência empírica no WP

**Sinais comuns de vazamento real:**
- `[RODAPÉ ESTRUTURAL: …]` (placeholder template não substituído)
- `[NEWSLETTER`, `[SCRIPT`, `[INTERLINK`
- "Você é o Editor-Chefe", "Você é o Auditor"
- "RETORNE UM JSON PURO COM:", "Devolva o JSON"
- "PROIBIDO X", "OBRIGATÓRIO Y" em CAPS
- "###" markdown headers no corpo (raro em artigo legítimo)
- "instrução interna", "diretriz editorial", "regra inviolável"
- Cabeçalhos tipo "RASCUNHO:", "AJUSTES DO AUDITOR:", "PADRÃO DE OURO"

**Falso positivo conhecido:** Kimi deployou em 27/05 19:43 BRT um second-pass regex em `agente_observador.py` que descarta alertas DeepSeek auditor quando regex local não confirma. Pós-fix: alertas em sentinela.log podem ser falsos positivos. Mas mesmo assim, verificação no WP continua obrigatória — não confiar que o filtro do Kimi pegou tudo.
