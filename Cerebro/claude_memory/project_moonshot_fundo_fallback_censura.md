---
name: moonshot-fundo-fallback-censura
description: Moonshot (Kimi) foi deliberadamente posto no FUNDO da cascata de fact-check por causa do content filter/censura agressivo — não é bug de roteamento
metadata:
  node_type: memory
  type: project
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

O `moonshot-v1-128k` está **ativo** no `llm_catalog.json` (tarefas: revisao, auditoria, fact_check, periferico), mas é a **4ª e mais profunda camada** da cascata de fact-check (`Perplexity sonar → Gemini 2.5 Flash → Qwen → Moonshot`). Isso é **deliberado**, não acidente de roteamento.

**Why:** o Moonshot tem content filter/censura agressivo. Nos logs ele rejeita muito com `400 — "considered high risk / content_filter"`, justamente em pauta geopolítica/militar/anti-imperialista (ex.: matéria sobre Hezbollah/Líbano barrada → "TODOS OS MODELOS DA FAMÍLIA MOONSHOT FALHARAM" → cascata cruzou pra Anthropic). Ironia: é modelo chinês, mas o filtro derruba exatamente o tipo de pauta pró-Sul-Global que o Cafezinho publica. Miguel confirmou (02/06 ~09:20 BRT): "a gente afastou ele pro fundo do fallback porque ele tem muita censura".

**How to apply:** NÃO tratar o baixo uso do Moonshot como bug a "consertar" nem propor promovê-lo pra papel primário em pauta editorial sensível — o filtro dele é incompatível com a [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]]. Posição de fundo da cascata é intencional. Se algum dia mover, só pra tarefa neutra (não-geopolítica).
