---
name: feedback-re-sincronizar-antes-de-postar-coordenacao
description: "Antes de postar coordenação cross-agente (Trindade) em sprint paralelo, fazer tail do canal + grep \"^## \" do fórum vivo para confirmar que estou olhando o último estado — não o de 30min atrás. Caso fundador 18/05 19:53 BRT sprint LLM."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4c52d90e-06f8-4198-8f65-dc7d7dc0c759
---

# Re-sincronizar canal+fórum ANTES de postar coordenação cross-agente

**Regra:** em sprint paralelo onde Codex/DeepSeek/Antigravity produzem rápido (vários §s/hora), **antes de postar qualquer mensagem coordenando frentes** (handoff, atribuição de tarefas, mapa de "quem faz o quê", esclarecimento sobre estado atual), fazer dois cheques de 5 segundos:

```bash
tail -20 Foruns/canal_trindade.md                           # últimas msgs do canal
grep -n "^## [0-9]" Foruns/forum_<sprint_vivo>.md | tail -5  # últimas seções do fórum
```

Sem esses cheques, posso citar §31 quando já existe §35, ou propor coordenação que outro agente já refutou enquanto eu pensava.

**Why:** caso fundador 2026-05-18 19:53 BRT sprint LLM. Miguel pegou em flagrante a possibilidade de eu ter postado coordenação desatualizada: "cuidado para não postar nada desatualizado. leu com atenção ultimas noticias do canal e foruns?" Dessa vez por sorte estava alinhado (canal: última msg era a minha; fórum: §32 era a última seção e eu citei §31/§32 corretamente), mas o risco era real porque entre minha leitura (DS 19:50) e meu post (19:53) eu não verifiquei se Codex tinha postado mais alguma coisa nos 3min. Em sprint com 8-12 §s/hora, 3min de atraso é suficiente pra desencontro.

**How to apply:**

- **Sempre antes de:** post de handoff (quem assume o quê), mapa "quem faz o quê agora", esclarecimento sobre estado atual, resposta a pergunta sobre o que outros agentes estão fazendo, fim/início de fase de sprint
- **Frequência mínima de re-cheque:** se o último `tail` foi há mais de ~5min E você está prestes a postar coordenação cross-agente, refaça o `tail`
- **Não precisa pra:** mensagens só suas (status próprio, achado, vou fazer X) — essas você é fonte primária, sem risco de desencontro
- **Sinais de desatualização:** Codex tem ticks `:05/:15/:25/:35/:45/:55`, DeepSeek pode postar a qualquer hora, AG idem. Se você está fora há >10min, é quase certo que tem algo novo
- **Comando útil pra Trindade-multi-fórum:**
  ```bash
  for f in Foruns/forum_sistema_notas_llm_20260518.md Foruns/forum_comparativo_monitoramento_llm_20260518.md; do
    echo "=== $f ==="; grep -n "^## [0-9]" "$f" | tail -3
  done
  ```

Relacionado: [[feedback_verificar_premissa_antes_decisao]] (irmão semântico — verificar state atual antes de propor; aqui verificar fluxo atual antes de coordenar), [[feedback_registrar_tudo_canal_sempre]] (canal é forum oficial — não posso assumir que minha versão lembrada bate com a versão atual).

— Incidente 2026-05-18 sprint sistema-de-notas LLM (não chegou a virar erro real porque o estado bateu, mas o padrão de risco foi sinalizado por Miguel).
