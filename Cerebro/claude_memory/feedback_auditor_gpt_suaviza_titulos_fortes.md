---
name: auditor-gpt-suaviza-titulos-fortes
description: "Auditor GPT-4o (agente_auditor_titulos_gpt.py) tem padrão de tentar SUAVIZAR/DILUIR títulos fortes do Cafezinho — alucinação reversa frequente. Guard em \"monitorar\" segura, não corrige. Reportar ao Codex/Kimi pra revisar prompt do auditor."
metadata: 
  node_type: memory
  type: project
  originSessionId: 622ef7ab-42d7-4d24-acca-49f4fff09603
---

## Padrão de alucinação reversa do auditor GPT

**Observado em 2026-06-05 (2 casos em ~6h no loop §53):**

1. **#256552 (17:10 BRT) "Putin revela segredo de Estado sobre uso do míssil Oréshnik na Ucrânia"**
   - Auditor classificou: `verbo_distorcido`
   - Sugestão: "Putin fala sobre testes do míssil Oréshnik na Ucrânia"
   - **Por que é alucinação reversa:** o corpo diz literalmente "O presidente revelou um segredo militar de Estado ao detalhar que os alvos foram escolhidos com base em critérios de visibilidade." Título sustentado. Sugestão dilui protagonismo do Kremlin → contraria linha editorial anti-imperialista do Cafezinho ([[feedback_linha_editorial_anti_imperialista_russia_inegociavel]]).

2. **#256564 (17:35 BRT) "Google pagará US$ 920 milhões mensais à SpaceX por supercomputação de IA antes de IPO bilionário"**
   - Auditor classificou: `numero_inflado`
   - Sugestão: "Google firma contrato de US$ 920 milhões mensais com SpaceX para supercomputação"
   - **Por que é alucinação reversa:** o número $920mi/mês está EXATO no lide ("contrato com o Google no valor de US$ 920 milhões por mês"). `numero_inflado` é classificação errada. Sugestão suaviza "pagará"→"firma contrato" e corta "antes de IPO bilionário".

**Padrão observado:** GPT-4o tende a:
- Substituir verbos jornalísticos fortes ("revela", "pagará") por neutros ("fala sobre", "firma contrato")
- Cortar contexto factual de qualidade ("antes de IPO bilionário")
- Aplicar categorias de erro errantes (`verbo_distorcido`, `numero_inflado`) quando o título está literalmente sustentado pelo corpo

**Por que o sistema NÃO aplicou as correções:**
- Guard do `agente_auditor_titulos_gpt.py` decide `acao=monitorar` (não `corrigido`) quando confiança não bate threshold ou contradição é estrutural
- `loop_correcao_count=0` em ambos os casos
- `titulo_corrigido=""` no JSONL

**Recomendação registrada no canal_trindade 17:45 BRT:** Codex/Kimi avaliarem revisar prompt do auditor pra reduzir false positives nas categorias `verbo_distorcido` e `numero_inflado` quando título está SUSTENTADO PELO CORPO.

**Why:** auditor que suaviza títulos vai contra a estratégia editorial Cafezinho (vocabulário chamativo permitido — [[feedback_nao_censurar_vocabulario_so_principios]]; "revela" desejado — [[feedback_revela_nao_e_proibido_e_desejado]]). Se algum dia o guard ceder e aplicar essas "correções", quebra a linha editorial em escala.

**How to apply:** ao auditar tick §53, sempre cruzar `acao_gpt=corrigir` com sustentação do título no corpo. Se sugestão dilui linha editorial mas guard segurou (`acao=monitorar`) → reportar como alucinação reversa BLOQUEADA. Se algum dia aparecer `acao=corrigido` aplicando suavização → escalar P0 imediato pro Miguel + Codex.

**Status auditor GPT em 2026-06-05:** 39 entries, $0.14 (longe do limite $3), 1 correção real válida (#256549 "Banco Central"→"Banco Master"), 2 alucinações reversas barradas. Sistema funcional, padrão precisa ser corrigido no prompt do auditor.
