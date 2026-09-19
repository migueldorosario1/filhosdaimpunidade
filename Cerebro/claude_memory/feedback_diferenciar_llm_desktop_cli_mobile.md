---
name: diferenciar-llm-desktop-cli-mobile
description: "Todo LLM moderno tem múltiplas versões (desktop/browser, CLI, mobile) que NÃO são a mesma coisa — nunca confundir; sempre especificar qual versão está sendo referida no cérebro, comunicação e escalação"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f333da72-7610-439d-ab22-49569ae85b4a
---

**REGRA:** Todo LLM do ecossistema hoje tem pelo menos 2-3 versões distintas com capacidades diferentes. **NUNCA presumir que são a mesma coisa.** Sempre especificar qual versão está sendo referida em cérebro, comunicação, escalação e memórias.

## Mapeamento de versões vigentes (26/07/2026)

| Provedor | Desktop/Browser | CLI | Mobile | Notas |
|---|---|---|---|---|
| **Anthropic Claude** | `claude.ai` (browser) + Claude Desktop app | **Claude Code** (`claude` CLI) | app iOS/Android (~= desktop) | Desktop e mobile quase iguais. CLI é ambiente separado |
| **Kimi (Moonshot)** | **Kimi Desktop** (browser + Windows/Mac app) — Miguel USA hoje | Kimi CLI (`kimi-cli`) — Miguel NÃO usa mais, talvez volte | app iOS/Android | Desktop ≠ CLI (features distintas, contexto separado) |
| **OpenAI GPT** | `chatgpt.com` + ChatGPT Desktop | **Codex CLI** (`codex` CLI) | app iOS/Android (~= browser) | Codex é OUTRO produto, não é ChatGPT. Não confundir |
| **Google Antigravity** | **Antigravity Desktop** (Google browser-based agent) | **AGI CLI** (`agi` command) | — | Miguel USA Desktop e AGI CLI em paralelo. NÃO confundir |
| **Zhipu GLM** | GLM app (browser + desktop) | GLM CLI | — | Desktop e CLI têm capacidades diferentes |
| **XAI Grok** | `grok.com` (browser) | `grok` CLI (recente) | — | Similar padrão |

## Regras operacionais

1. **Ao referenciar um LLM no cérebro/memória/canal:** especificar versão. Ex: `Kimi K3 Desktop` (não só "Kimi"), `Claude Code CLI` (não só "Claude"), `Codex CLI` (não só "GPT" nem só "Codex" ambíguo).
2. **Ao escalar/chamar agente:** confirmar qual versão específica. Ex: escalar pra "Kimi K3 desktop" (o que Miguel usa hoje) NÃO pra "Kimi K3 CLI" (aposentado por enquanto).
3. **Endpoints e chaves diferentes por versão:** desktop pode usar 1 endpoint/plano, CLI outro. Ver `CEREBRO_NODE_CHAVES_E_LLMS.md` sempre com essa granularidade.
4. **Contexto separado por versão:** conversa/estado do Kimi Desktop não é visível pra Kimi CLI, mesmo sendo do mesmo provedor. Registrar em qual versão a conversa está rolando.
5. **Comunicação assíncrona (cartinha, inbox):** deixar explícito no header do arquivo qual versão do agente é o destinatário. Ex: cabeçalho `**Destinatário:** Kimi K3 Desktop (Miguel usando hoje)` — não só "Kimi K3".
6. **Mobile como 3ª camada:** ChatGPT/Claude mobile são quase iguais ao desktop; Kimi/GLM mobile não são. Verificar antes de assumir paridade.

## Why

Miguel 26/07 15:38 BRT: *"Explica para o Kimi também a questão do inbox. Tem que lembrar que não pode confundir que tem um Kimi CLI que eu nem estou usando mais. E acho que eu nem vou usar mais por enquanto para não confundir mais ainda... são dois Kimis. É o Kimi que está aqui no desktop e o Kimi CLI. É o mesmo problema que a gente tem com o anti-gravity. que a gente tem anti-graft no desktop e tem o AGI... É que nem confundir GPT com o Codex, ou Cloud com o Cloud Code. São coisas separadas... no futuro todos os programas, todos os LMs vão ter para menos dois. Um que é no desktop, que tem acesso aos arquivos, outro que é no CLI."*

Contexto: hoje 26/07 comuniquei com "Kimi K3" via `inbox_trindade/kimi.md`, mas o inbox_trindade tem tanto `kimi.md` quanto (implicitamente) diferenciações que não estavam claras. Miguel usa Kimi K3 Desktop hoje; Kimi CLI está parado. Confundir os dois pode fazer eu escalar mensagem pra canal errado ou usar chave/endpoint errado. Mesmo problema aplicável a Antigravity (Desktop vs AGI CLI), GPT (ChatGPT vs Codex CLI), Claude (browser vs Claude Code CLI), GLM (desktop vs CLI), Grok, etc.

Miguel disse: *"Bota isso no cérebro para a gente depois conversar com mais calma sobre essa diferenciação que a gente tem que tomar cuidado."* — reforça que essa é regra estrutural longo prazo, não patch pontual.

## How to apply

- Toda cartinha/comunicação: usar versão específica no header (`**Destinatário:** Kimi K3 Desktop`)
- Toda memória sobre agente: mesma disciplina (`Kimi K3 desktop (Moonshot)`)
- Antes de escalar: confirmar em qual versão a comunicação vai chegar
- Se dúvida: perguntar Miguel explicitamente qual versão
- Manter tabela de versões vigentes atualizada — quando Miguel parar/começar a usar alguma, atualizar cérebro

Regras irmãs: [[canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]], [[cartinha-como-md-com-link-no-final]].
