---
name: Deploy dos 5 agentes temáticos (2026-04-17)
description: 5 novos agentes (IA, Petróleo, Mercado, Energias, Inflação) + helper publicador_tematicos.py deployados em 17/04/2026 em ambos os servidores, iniciam em DRAFT.
type: project
originSessionId: 93db6fe5-f066-444c-a650-a18d8993d5e9
---
Em 2026-04-17 foram deployados 5 agentes temáticos novos no ecossistema do Cafezinho:

**Arquivos (em `/root/` dos 2 servidores, MD5 idênticos):**
- `publicador_tematicos.py` — helper compartilhado (LLM com fallback, prompt V9, RSS 24h + trafilatura, Brave News, anti-duplicação por tema, fact-check Perplexity fail-open, publicador WP + indexador)
- `agente_ia.py` — TechCrunch/Wired/Google News + Brave
- `agente_petroleo.py` — Google News + OilPrice + Brave
- `agente_mercado.py` — yfinance (^BVSP + USDBRL=X) + RSS + Brave
- `agente_energias.py` — RSS Brasil + Electrek + Brave
- `agente_inflacao.py` — SIDRA/IBGE tabela 7060 c315 por subitem (mapeamento D2N/D3C/D4N, lista de 13 produtos) + RSS + Brave

**Agenda no Tencent (9 linhas adicionadas, total 46 ativas):**
- agente_ia: 8h17, 13h17, 19h17 (3x)
- agente_petroleo: 9h07, 15h07 (2x)
- agente_mercado: 10h37 + 18h07 só dias úteis (2x)
- agente_energias: 16h27 (1x)
- agente_inflacao: 11h47 (1x) — DRAFT permanente

**Status de publicação:** TODOS os 5 em `status="draft"` no primeiro rollout para revisão humana. Trocar para `"publish"` depois de validar qualidade. O "Caetano" (@caetanoechicobot) pode ser usado pra editar via API antes de promover.

**Credenciais WP:** agentes usam usuário `redatorcafezinho` (não o `Redator` master). Chaves ficam em `/root/chaves.sh` (WP_USER_FALLBACK/WP_PASS_FALLBACK) E em `/root/.env` (apêndice feito no deploy, necessário para cron sem `source chaves.sh`).

**Modelos LLM:** lê `agent_data/modelos_vivos.json` — atualmente `openai_luxo=gpt-5-search-api-2025-10-14` (primário, sem `temperature`) + `gemini_luxo=gemini-pro-latest` (fallback). Deps Python instaladas: `yfinance`, `google-generativeai` (pip install com `--break-system-packages --ignore-installed`).

**Anti-duplicação:** arquivos `agent_data/tematicos_postados_{tema}.json` por agente (ia, petroleo, mercado, energias, inflacao), Jaccard ≥ 0.55.

**NYC failover:** espelhado mas com crons NOVOS não adicionados (conforme §8 do CLAUDE.md — NYC só ativa em emergência). 241 arquivos top-level com MD5 match. No deploy, limpei `/root/.openclaw`, `.local`, `.cache`, `.npm`, `.pip`, `.config` que tinham vazado do Tencent por descuido em rsync anterior (4GB recuperados).

**Why:** completar o quinteto temático pedido pelo Antigravity (IA, Petróleo, Mercado, Energias + Inflação). O helper compartilhado evita a duplicação de ~200 linhas × 5 agentes que o código inicial do Antigravity tinha.

**How to apply:**
- Se precisar promover para publish: editar `status="draft"` → `status="publish"` nos 4 (inflação fica draft sempre).
- Para desligar temporariamente: comentar as 9 linhas no crontab do Tencent.
- Rollback rápido: `sudo crontab -l | grep -v "agente_\(ia\|petroleo\|mercado\|energias\|inflacao\)\.py" | sudo crontab -`.
- Backup do crontab pré-mudança: `/root/crontab_backup_20260417_094140.txt` no Tencent.
