---
name: escalar-autocura-kimi-inbox
description: Autocura complexa que Claude não consegue sozinho → inbox do Kimi (não Codex). Claude avisa Miguel que tem ação pendente. Miguel dá tique e Kimi resolve.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 23db8fb8-ae8e-4d0f-a1e7-3645e7d8bbc6
---

Quando autocura for complexa demais para resolver sozinho (§51), escalar via **inbox do Kimi** (não Codex).

**Why:** Miguel quer treinar mais o Kimi, que é muito bom. Codex fica de backup. Fluxo: Claude detecta → coloca no inbox Kimi → avisa Miguel "tem ação pro Kimi" → Miguel dá tique → Kimi resolve.

**How to apply:**
1. Bug simples (§51): Claude corrige sozinho
2. Bug complexo: escrever recado no `Foruns/inbox_trindade/kimi.md` com:
   - Descrição do problema
   - Diagnóstico feito até agora
   - Arquivos envolvidos
   - Sugestão de fix (se tiver)
3. Avisar Miguel na conversa: "Tem uma ação pro Kimi no inbox"
4. Se Kimi não existir ou não resolver, fallback para Codex (`Foruns/inbox_trindade/codex.md`)
