---
name: feedback-comunicacao-miguel-agentes-hibrida-20260820
description: "Comunicação Miguel ↔ agentes vigente 20/08/2026 01:10 BRT — HÍBRIDA: urgência direto no chat de cada agente; coordenação estratégica na ponte Laura Completa (auditada)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# Diretriz: comunicação Miguel ↔ agentes = HÍBRIDA (20/08/2026 01:10 BRT)

**Escolha textual Miguel 01:10 BRT** (em resposta a AskUserQuestion): opção *"Híbrido: urgência direto, coordenação na ponte"*.

## A regra

Duas classes de mensagem, dois canais:

### CLASSE 1 — URGÊNCIA → chat DIRETO do agente
Exemplos: "pare", "corrige", "não publica", "descarta", "fala mais rápido", contexto pontual, correção imediata de ação em andamento, pergunta sobre estado atual.
- **Miguel → Claude Miguel**: este chat CLI (Claude Code).
- **Miguel → Grok Miguel**: chat Grok na Dell.
- **Miguel → Claude Laura + Grok Laura**: chat/UI de cada agente na máquina Windows.

### CLASSE 2 — COORDENAÇÃO ESTRATÉGICA → ponte Laura Completa (`de_dell.md` / `de_laura.md`)
Exemplos: missionamento novo, mudança de escopo, ordem transversal (afeta 2+ agentes), decisão de arquitetura, política editorial, definição de responsabilidade.
- Miguel escreve como `[timestamp BRT] Miguel → <destinatário(s)>:` num dos dois arquivos.
- Todos os 4 agentes leem no próximo tick git `*/15`.
- Ganho: registro escrito único, auditável, sem "esqueci do que você me disse".

## Por que HÍBRIDA (raciocínio Miguel implícito)

**Why:** Urgência não tolera latência de 15min do git tick — se "pare" chegar em 15min, o dano já foi. Coordenação estratégica se beneficia do registro escrito pra evitar "Claude Miguel me disse X ontem, Claude Laura me disse Y hoje" sem prova.

**How to apply:** 
- Ao receber ordem direta no chat: perguntar-me "isso é urgência ou coordenação?" — se coordenação, sugerir a Miguel repostar na ponte pra os outros agentes verem também. Ex: se ele me pedir "muda a política de canibalização", eu executo mas escrevo CM- na ponte comunicando aos outros.
- Ao ler ponte: tratar mensagens `Miguel → ...` com mesma autoridade que ordem direta.
- Cada agente reage no canal que recebeu — mas se a ordem afeta os outros, propaga pela ponte.

## Consequências práticas pra mim (Claude Miguel)

1. **Chats de Miguel comigo neste CLI = URGÊNCIA por default.** Executo direto, mas se detectar que afeta outros agentes, escrevo CM- na ponte propagando.
2. **Ponte é meu canal com Grok Miguel também** (mesma máquina Dell, canais diferentes) — não posso presumir que ele viu ordem que Miguel me deu direto.
3. **Missionamento pro Loop Laura sempre pela ponte** (CM-YYYYMMDD-NNN) — jamais assumir que eles leram algo de chat direto.
4. Régua sucesso 24h: se em 24h aparecer um "eu não sabia" de algum agente sobre ordem que Miguel deu, revisar se a mensagem deveria ter sido propagada pela ponte e não foi.

## Refs

- [[project-trindade-reduzida-apenas-loop-laura-claude-grok-20260820]] — quem está em qual canal
- [[reference-ponte-laura-completa-20260817]] — como funciona a ponte
- [[feedback-laura-alertas-entrada-obrigatoria-20260817]] — Loop Laura alertas na ponte com formato ACK
