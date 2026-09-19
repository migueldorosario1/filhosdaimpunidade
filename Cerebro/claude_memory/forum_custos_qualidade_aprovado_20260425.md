---
name: Fórum custos×qualidade APROVADO 2026-04-25 — Sprint 1 + Sprint 0 liberados
description: Pacote A-H aprovado por Miguel. Antigravity respondeu Q2/Q3/Q5/Q6/Q10. Documento canônico em `Foruns/forum_custos_qualidade.md` (raiz do projeto). Redirect em `Projeto Cafezinho Agentes/root/`. Cópias antigas em raiz do projeto migraram pra `Foruns/`.
type: project
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
**Localização canônica:** `/home/migueldorosario/Downloads/Antigravity Google/Foruns/forum_custos_qualidade.md` (463+ linhas, ~35KB).

**Why:** Diretório `Foruns/` criado 2026-04-25 ~10h pra organizar fóruns de debate. Demais fóruns migrarão depois "com calma" (decisão Miguel).

**How to apply:** Antes de codar QUALQUER item de redução de custo, ler §14.3 (tabela A-H) e §14.4 (respostas Q2/Q3/Q5/Q6/Q10). Sequência aprovada: Sprint 1 (cortes infra) → Sprint 0 (frentes Antigravity).

## Decisões aprovadas (resumo)

**Sprint 1 — Cortes seguros:**
- A1 ElevenLabs creator → free (US$22/mês) — Miguel faz no painel
- A2 UptimeRobot pago → free (US$10/mês) — Miguel faz no painel
- A3 NYC droplet 8GB → 1GB (US$18-42/mês) — Miguel faz no painel DigitalOcean
- A4 Limpar `cingapura_workspace/` + `ambiente_teste/` no Tencent — Claude faz com confirmação Miguel (destrutivo)
- B3 Repetidor Estatal `*/30` → 4×/dia — Claude faz no crontab
- B4 China 5×/dia → 2×/dia (08, 20h) — Claude faz no crontab

**Sprint 0 — Frentes Antigravity (paralelizável com Sprint 1):**
- F1 Auditoria de payload no `agente_roteador_llm.py` — sem timestamps no system block
- F2 Prompt caching Anthropic ≥1024 tokens byte-idêntico — `Matriz Editorial` + `CONTRATO_ELEICOES.md` no system com `cache_control: ephemeral`
- F4 Stripping regex `<think>...</think>` no Perplexity antes de auditar — bate com bug 24/04 já mapeado
- F3 espera Análise validar em produção (1 semana)

**Sprint 2 — Cap LLM US$50/dia híbrido + bots Telegram:**
- LLMCostGuard com soft global (alerta @US$40) + hard por agente (raise capturável, fallback gracioso)
- Instrumentar bots Telegram daqui pra frente (Augusto/Mayra/Zizi/Miller/Gabriel/Irmão/whatsapp)

**Sprint 3 — Comentaristas:** PAUSADO. Discussão em `forum_comentarios.md`.

**Sprint 4 — Otimizações LLM:**
- C1 Brave + extrator vs gpt-5-search-api (40% do gasto) — pré-requisito mini-fórum sobre critério editorial de fontes
- C2 Sonnet 4.6 padrão drafter
- C3 DeepSeek meta-textos: A/B com 100 captions PRIMEIRO (Antigravity alertou risco "cara de traduzido")

**Sprint 5 — Two-Pass na Trindade:** após Análise validar 1 semana em produção (decisão Q2).

## Itens não-tocar
- A5 (HeyGen/Manus/Creatomate) — não cortar sem Miguel confirmar uso zero
- Q10 (agente apagável) — investigar via `auditor_ga4.py` antes de pausar; alvos prováveis: temáticos fora do núcleo Política/Soberania/Geopolítica sem pageviews

## Pendência arquivada
Cópia antiga em `Projeto Cafezinho Agentes/root/forum_custos_qualidade.md` virou redirect de 3 linhas pro `Foruns/`. Não deletar.

## Hierarquia respeitada
Miguel decidiu, Antigravity opinou, Claude codificará. Antigravity tocou só docs (não infra). Acoes destrutivas (A4, painéis) exigem ação direta Miguel ou confirmação dele.
