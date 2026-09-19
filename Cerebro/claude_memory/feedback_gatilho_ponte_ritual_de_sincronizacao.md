---
name: feedback-gatilho-ponte-ritual-de-sincronizacao
description: "Quando Miguel digita apenas `ponte` (token único + Enter) em chat comigo (Claude) ou no Kimi K3 Desktop, executar ritual de sincronização: ler inbox+canal+MEMORIA_TOTAL+cartinhas novas+HISTORICO+consultas API e responder em bloco compacto ~15 linhas — regra Miguel 28/07/2026 18:25 BRT + emenda §5 CONTRATO_PONTE"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Quando Miguel digitar apenas o token `ponte` (só a palavra, sem contexto adicional, + Enter) em chat comigo (Claude Code) OU no Kimi K3 Desktop, é gatilho de **ritual de sincronização** — o LLM lê tudo que a outra ponta escreveu desde o último ACK e responde em bloco compacto.

**⚠️ EVOLUÇÃO 28/07 18:55 BRT — Ponte Trindade Nova (triangular):** ritual expandido pra incluir Antigravity Desktop como 3º vértice. Ao ver `ponte`, Claude lê tanto inbox Kimi quanto inbox Antigravity.

**Ritual (paralelo onde possível):**

1. `Cerebro/Foruns/inbox_trindade/kimi.md` — últimas 5-10 entradas (Kimi K3 Desktop)
2. `Cerebro/Foruns/inbox_trindade/antigravity_desktop.md` — últimas 5-10 entradas (Antigravity Desktop, novo)
3. `Cerebro/Foruns/canal_trindade.md` — `tail -30` linhas (aumentado de 20 pra pegar 3 agentes)
4. `Cerebro/ponte_kimi/MEMORIA_TOTAL_PONTE.md` — comparar cabeçalho `Última atualização` vs última leitura minha
5. `Cerebro/Foruns/cartinhas/cartinha_<destinatario>_*_YYYYMMDD_*.md` — novas
6. `Cerebro/ponte_kimi/HISTORICO.md` — últimas entradas
7. `Cerebro/Foruns/consultas_kimi_k3_api/` — respostas Modo B recentes

**Formato resposta (v2 triangular):**

```
🌉 Ponte Trindade Nova lida — [timestamp] · desde último ACK [ts anterior]

Do Kimi K3 Desktop: N pings/ações ({resumo 1 linha})
Do Antigravity Desktop: N pings/ações ({resumo 1 linha})
(omitir minha própria seção OU marcar como "eu")

Cartinhas novas: N ({título + prio + destinatário})
Precisa decisão Miguel AGORA: ({items ou "nada"})
Fila próximas sessões: ({items ou "nada urgente"})
```

Se nada mudou desde último ACK: `🌉 Ponte Trindade Nova lida — nada novo. Estado atual OK nos 3 vértices.` (1 linha).

**Why:** Miguel 28/07 18:25 BRT: *"a ponte é uma série de estratégias reunidas sob o nome ponte — vamos criar um código pra facilitar, sempre que eu escrever `ponte` + Enter, o LLM já sabe que deve olhar tudo que a outra ponta escreveu desde a última leitura"*. Objetivo: reduzir atrito de mediação — de "Miguel digita 3-5 linhas de contexto" pra "Miguel digita 1 token".

**Escalável:** amanhã podemos ter `ponte codex`, `ponte glm`, `ponte trindade` (leitura ampla — todos os agentes). Por enquanto só `ponte` = ler tudo relevante à ponte Claude↔Kimi.

**Cartinha fundadora:** `Cerebro/Foruns/cartinhas/cartinha_kimi_gatilho_ponte_emenda_contrato_20260728_1830.md`
**Emenda formal:** §5 nova do `Cerebro/ponte_kimi/CONTRATO_PONTE_CLAUDE_KIMI.md`
**Meu ACK:** assinado no próprio contrato §5 (2026-07-28 18:30 BRT).

**Aderência Kimi K3 Desktop:** aguarda ping canal `[KIMI-DESKTOP-GATILHO-PONTE-ADERIDO]`.

**Regras irmãs:**
- [[feedback-diferenciar-kimi-api-vs-kimi-desktop-ao-mencionar]] — o gatilho `ponte` sozinho vale pra Modo A (Kimi Desktop) e pra chat Claude. Não confundir com chamadas Modo B (API autônoma via `consulta_kimi_memoria_total.py`)
- [[feedback-cartinha-como-md-com-link-no-final]] — resposta ao `ponte` cita cartinhas novas por link, seguindo mesmo padrão
- [[feedback-canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]] — o ritual respeita hierarquia (canal/inbox = ponteiro, cartinha = detalhe)
