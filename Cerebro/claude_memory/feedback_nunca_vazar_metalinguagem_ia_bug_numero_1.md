---
name: feedback-nunca-vazar-metalinguagem-ia-bug-numero-1
description: BUG
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**REGRA ULTRA-CRÍTICA — sem exceção.**

Miguel 13/08/2026 ~12:15 BRT: *"Obviamente não cite jamais nenhuma IA na parte de crédito. Bug número 1 de todo o ecossistema, vazamento de qualquer texto meta linguagem, interno, que informe sobre nosso metodo de redação com uso de IA."*

## O que NUNCA pode aparecer em texto público (title, content, excerpt, caption de mídia, meta pública)

**Nomes de modelos/serviços de IA:**
- Claude, ChatGPT, GPT, GPT-4, GPT-5, GPT-4o, gpt-4o-mini
- DeepSeek, DeepSeek-V3, DeepSeek-V4
- Gemini, Gemini Flash, Gemini Pro, Gemini-3.6
- Kimi, Kimi K3, Moonshot
- Qwen, Qwen 3, Qwen 3.8
- GLM, GLM 5.2, Zhipu, Z.ai
- Grok
- Anthropic, OpenAI, xAI, Alibaba (como fornecedor de IA — como TEMA de notícia OK)
- LLaMA, Meta AI, Mistral

**Termos genéricos que denunciam origem:**
- "IA", "inteligência artificial" (quando se refere ao processo interno)
- "LLM", "modelo de linguagem"
- "robô", "agente", "bot"
- "worker", "pipeline", "cron"
- "revisor automático", "gerado por IA", "editado por IA", "com auxílio de IA"
- "algoritmo redigiu", "sistema gerou"
- "V4", "vertical V4", "worker V4"

**Meta-referências ao método editorial:**
- "coletor RSS", "curador automático"
- "checagem tripla DS+GPT", "auditor GPT"
- "modo enxuto", "Vigília V5/V6"
- "Trindade", "ZCode", "Codex" (quando não é jornalisticamente relevante como TEMA)
- Nomes internos: "agente_repetidor_estatal", "agente_manchete.py", etc

## O que PODE aparecer (é jornalismo legítimo)

Quando a IA é **TEMA da matéria** (não método interno):
- "Alibaba reduz tempo de obra de data centers de IA para 100 dias" ✅ (fato do mercado)
- "Flávio Bolsonaro defende no TSE uso de IA sem autorização" ✅ (fato político)
- "Metade dos brasileiros quer banir IA da eleição" ✅ (pesquisa)
- "Anthropic lança modelo Claude 4" ✅ (notícia de negócios/tech)

A diferença: quando "IA" ou nome de modelo aparece como **assunto da reportagem**, é legítimo. Quando aparece como **método/atribuição do próprio texto**, é vazamento.

## Nota de edição correta (quando aplicável)

Se preciso identificar que o Cafezinho editou/enriqueceu texto do repetidor com informações complementares (regra irmã [[feedback-nota-edicao-cafezinho-repetidor-estatal]]):
- **CORRETO**: *"Editado com informações complementares pelo Cafezinho, às 12h05."*
- **ERRADO**: *"Editado com auxílio de IA"* · *"Enriquecido por Claude"* · *"Revisado por LLM"* · *"Curadoria automática"*

O sujeito da nota é sempre **"Cafezinho"** (a redação), não a ferramenta.

## Auditoria retroativa 13/08/2026 12:20 BRT

Grep executado em 18 posts revisados nesta sessão (title+content+excerpt) contra lista completa de termos proibidos: **0 vazamentos**. Verificado:
- Ciclo Vigília V5 ontem 22:26: 265322, 265311, 265318, 265353, 265339, 265329, 265196, 265370 — limpos.
- Repetidor 13/08 madrugada: 265450, 265452, 265459, 265462, 265467, 265475 — limpos.
- Repetidor backlog: 265402, 265381 — limpos.
- Repetidor novos 13/08: 265492, 265391 — limpos.

Regra vigente daqui pra frente: rodar mesmo grep antes de cada `wp_update_post` que toque conteúdo.

## Aplicação prática — checagem antes de todo publish/patch

Antes de qualquer `wp_update_post` que toque `post_content` ou `post_title`, rodar mental grep pelas palavras-chave acima. Se aparecer, remover ou reformular. Se é ambíguo (ex: "IA" como assunto vs método), pesar contexto — se pode confundir leitor, remover.

**Nenhuma exceção.** Nem em rodapé, nem em legenda, nem em código HTML de metadados, nem em `alt=""` de imagem, nem em `author=` de bio. NUNCA.

Regras irmãs: [[feedback-nota-edicao-cafezinho-repetidor-estatal]] · [[feedback-repetidor-estatal-regras-e-bugs]] · [[feedback-charges-sem-texto-dentro-flux]] (similarmente proíbe vazar meta em imagem gerada).
