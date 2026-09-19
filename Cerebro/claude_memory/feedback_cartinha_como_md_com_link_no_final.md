---
name: cartinha-como-md-com-link-no-final
description: "Toda cartinha (\"carta\"/\"cartinha\") escrita pro Kimi/Trindade/agentes deve ser salva como arquivo .md em Cerebro/Foruns/cartinhas/ e o link do arquivo colocado no final da resposta no chat com Miguel — pra ele copiar só o link e passar pros outros agentes"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f333da72-7610-439d-ab22-49569ae85b4a
---

**REGRA:** Quando escrever "cartinha" (ou "carta") pra Kimi K3, Trindade, ou qualquer agente do ecossistema, seguir fluxo:

1. **Escrever a cartinha humanizada no chat** com Miguel (pra ele visualizar em tempo real)
2. **Salvar cópia exata como arquivo `.md`** em `Cerebro/Foruns/cartinhas/cartinha_<destinatario>_<slug_curto>_YYYYMMDD_HHMM.md`
3. **Espelhar/apontar no fórum canônico** correspondente ao sprint (regra antiga [[canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]])
4. **Terminar a resposta no chat com o link do arquivo `.md`** — bloco destacado tipo *"📮 Link da cartinha: `Cerebro/Foruns/cartinhas/cartinha_...md`"* — assim Miguel copia só o link e passa pros outros agentes sem re-copiar carta inteira

**Formato do arquivo `.md`:**
- Cabeçalho: `# Cartinha ao <destinatario> — <data> <hora> BRT`
- Subtítulo com autor (`Claude Code, opus-4-7`)
- Corpo: exatamente o que foi escrito no chat, formatado com seções markdown
- Rodapé: assinatura + link pro fórum canônico do sprint (se houver)

**Nomenclatura:**
- `cartinha_kimi_<slug>_YYYYMMDD_HHMM.md` (Kimi K3)
- `cartinha_trindade_<slug>_YYYYMMDD_HHMM.md` (Codex+Agy+GLM)
- `cartinha_codex_<slug>_YYYYMMDD_HHMM.md` (Codex individual)
- `cartinha_agy_<slug>_YYYYMMDD_HHMM.md` (Agy individual)
- `cartinha_glm_<slug>_YYYYMMDD_HHMM.md` (GLM individual)
- `cartinha_miguel_<slug>_YYYYMMDD_HHMM.md` (raro — se precisar comunicação assíncrona com o próprio Miguel)

Slug curto = 2-4 palavras kebab-case descrevendo o assunto. Ex: `coleta-enriquecida`, `deploy-nyc-tencent`, `webverify-brave`, `protocolo-comunicacao`.

**Why:** Miguel 26/07 15:35 BRT: *"para a nossa comunicação com o Kimi ficar mais fácil ainda, com todo mundo, quando escrever essa cartinha nesse fórum, termina com o link da cartinha, transforma essas cartinhas humanizadas... transforma essas cartinhas humanizadas no arquivo MD, aí você publica a cartinha, mas no final você bota assim só passar esse link pra ele, o link é esse da cartinha, eu clico no link, passo lá pro Kimi passo lá pros outros em vez de copiar a cartinha toda"*.

Contexto: Hoje 26/07 fiz várias cartinhas pra Kimi (webverify-brave, coleta-enriquecida). Miguel teve que copiar carta inteira do chat pra passar via prompt do Kimi. Trabalhoso. Se eu salvo cada uma como arquivo .md, ele copia só o path e cola no chat do Kimi — Kimi lê direto do disco.

**How to apply:**
- SEMPRE que Miguel disser "carta"/"cartinha" → cria arquivo `.md` na pasta cartinhas + termina chat com link
- Se cartinha for pra múltiplos destinatários (Trindade), 1 arquivo com nome `trindade_*` ou N arquivos individuais (a decidir por contexto — se conteúdo idêntico → 1 arquivo; se personalizado → N)
- Se atualizar cartinha existente com correção, gerar novo arquivo com timestamp maior (não sobrescrever histórico)
- No fórum canônico do sprint, apontar pro arquivo `.md` da cartinha (não colar conteúdo inteiro de novo — evita duplicação)

Regras irmãs: [[canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]] (canal/inbox = ponteiro, fórum = single source of truth), [[nunca-chave-literal-em-forum]] (chaves nunca em texto claro).
