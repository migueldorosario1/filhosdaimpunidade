---
name: feedback-diferenciar-kimi-api-vs-kimi-desktop-ao-mencionar
description: "Sempre que mencionar 'Kimi', especificar se é Kimi API (Modo B autônomo, Claude resolve sozinho) ou Kimi K3 Desktop (Modo A humano-mediado, Miguel acompanha) — regra Miguel 28/07/2026 18:20 BRT"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Toda menção a "Kimi" em chat/canal/inbox/fórum/cartinha/memória deve especificar qual modalidade da ponte está em jogo:

| Modalidade | Nome canônico | Como agir |
|---|---|---|
| **Modo B autônomo** | **Kimi API** (ou "Kimi K3 API") | Claude chama direto via `consulta_kimi_memoria_total.py` → paygo `api.moonshot.ai/v1` primário / assinatura Coding `api.kimi.com/coding/v1` fallback. **Miguel NÃO precisa acompanhar.** Resolvido em segundos, custo R$ 0.02/consulta, cap 20/dia |
| **Modo A humano-mediado** | **Kimi K3 Desktop** (ou "Kimi Desktop") | Claude pontua fórum + canal + inbox → **Miguel abre Kimi K3 Desktop** → ele lê e responde no fim de sessão. **Miguel PRECISA acompanhar** — é bloqueio no fluxo dele |

**Como aplicar:**
- **Chat com Miguel:** ao dizer "Kimi vai fazer X", "Kimi já tem Y na fila", "escalado ao Kimi" — sempre qualificar: "Kimi API vai...", "Kimi Desktop já tem...", "escalado ao Kimi Desktop"
- **Canal `[TAG]`:** manter tags atuais (`[CLAUDE-KIMI-*]`) mas adicionar sufixo modalidade quando ambíguo: `[CLAUDE-KIMI-API-CONSULTA-*]` vs `[CLAUDE-KIMI-DESKTOP-ESCALADO-*]`
- **Inbox/cartinha:** já usam padrão "Kimi K3 Desktop" — manter
- **Memórias/fórum:** sempre nome canônico (nada de "Kimi" solto)

**Racional (Miguel 28/07 18:20 BRT):** *"quando você mencionar o Kimi, você tem que falar se é o Kimi API, que você pode chamar aqui e aí vocês resolvem de maneira totalmente autônoma. Ou o Kimi Desktop mediação humana, em que eu tenho que acompanhar"*.

**Why:** Miguel precisa saber em cada momento se um problema/pendência está NA CARGA COGNITIVA DELE (Modo A — ele tem que abrir Kimi Desktop, ler, decidir) ou NA MINHA (Modo B — eu chamo API sozinho e resolvo). Sem qualificação, Miguel fica sem saber se algo depende dele ou se já tá tocando autônomo. Isso é a razão fundamental de existir Modo B — tirar bloqueio dele.

**Anti-pattern:** "Kimi já tem esse pattern na fila via cartinha 27/07" (ambíguo — quem tem? API pode consultar cartinha? não; Kimi Desktop tem via inbox). Correto: "Kimi K3 Desktop já tem esse pattern na fila via cartinha 27/07 (Modo A — aguarda Miguel abrir)".

**Escopo:** vale pra outros LLMs análogos daqui pra frente conforme forem ganhando modo B autônomo — GLM API vs GLM Desktop, Codex API vs Codex CLI etc. Extensão natural de [[feedback-diferenciar-llm-desktop-cli-mobile]].

**Regras irmãs:**
- [[feedback-diferenciar-llm-desktop-cli-mobile]] — regra mãe (Desktop vs CLI vs Mobile). Este feedback especializa pra Kimi + modalidade da ponte
- [[feedback-cartinha-como-md-com-link-no-final]] — cartinhas são Modo A por definição (Miguel medeia)
