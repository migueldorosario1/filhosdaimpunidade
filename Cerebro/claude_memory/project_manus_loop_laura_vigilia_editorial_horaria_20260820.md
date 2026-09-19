---
name: project-manus-loop-laura-vigilia-editorial-horaria-20260820
description: "5º agente ativo — Manus AI (IA da Manus) conta 'Manus 2' (migueldorosario2) rodando 'Loop Laura — vigília editorial horária' 1x/h append-only via GitHub + Google Workspace (ordem Miguel 20/08 02:18-02:19 BRT)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# Manus 2 — IA da Manus rodando Loop Laura — Vigília Editorial Horária (20/08/2026 02:18 BRT — ordem Miguel)

**O que é:** **Manus AI** (plataforma de IA agentic; https://manus.im ou similar). Miguel confirmou 02:19 BRT: *"que é uma IA da manus"*.

**Conta usada:** **Manus 2** — Miguel confirmou 02:19: *"esse é do manus 2 (migueldorosario2"*. Email vinculado: `migueldorosario2@gmail.com` (mesma conta que aparece no meu system prompt Claude Code).

**Inferência não confirmada:** existe **Manus 1** (talvez `migueldorosario@gmail.com`, dona do Google Drive `PONTE_DRIVE_LAURA`) rodando outros loops. Verificar com Miguel se relevante.

**Ordem textual Miguel 02:18 BRT** (chat CLI direto): configurou no Manus 2 uma tarefa agendada horária chamada "Loop Laura — vigília editorial horária".

## Configuração

| Parâmetro | Valor |
|---|---|
| Nome | Loop Laura — vigília editorial horária |
| Intervalo | 3600s (1h); escalável a 7200s (2h) via mesmo agendamento |
| Fuso | America/Sao_Paulo |
| Estado | Ativo |
| Conectores | GitHub + Google Workspace (Gmail e Calendar REMOVIDOS) |
| Execução | Preserva contexto (não isolada) |

## Escopo do agente Manus

**PODE (a cada ciclo):**
- Ler Cérebro canônico
- Ler minuta do contrato
- Verificar fila V4 últimas 24h para autor 5786
- Procurar problemas editoriais
- Registrar achados de forma **append-only**

**NÃO PODE (fail-close):**
- Publicar
- Alterar status
- Criar agendamentos WP
- Apagar dados
- Executar SQL
- Forçar alterações no Git

## Impacto na composição da Trindade

Antes (Miguel confirmou 01:01): 4 agentes ativos (CM+GM Loop Miguel · CL+GL Loop Laura).

**Agora: 5 agentes ativos:**
- CM (eu) — publish, Vigília V6 `*/20` A/B
- GM (Grok Miguel) — observador Fase 2 Emenda 4
- CL (Claude Laura) — SHADOW_EDITORIAL_WRITE via `laura_ed25519`
- GL (Grok Laura) — §128 capas pós-publish + Slot B
- **Manus (novo)** — Loop Laura vigília editorial 1h READ+ANALYZE+APPEND (nunca WRITE em produção)

## Como Manus se encaixa nas missões da CM-20260820-001

- **Missão A** (backfill editorial Claude Laura, últimas 12h): Manus pode **INDICAR** posts problemáticos (título >80, §127, canibal, regência) mas **NÃO CORRIGE** — passa achado pro CL executar.
- **Missão B** (dedup canibal): Manus é ideal — 1h de cadência bate com necessidade. Pode gravar achados em arquivo texto/markdown na ponte ou Drive; CM ou CL usa como sinal.
- **Missão C** (imagens): fora do escopo Manus (não mexe em fm).

## Convenção CM-20260820-006 estendida

Meta `_cafezinho_descartado_canibal` (introduzida por mim 02:13) — Manus NÃO PODE gravar via SQL, mas pode gravar via file append num log de análise (ex: `Cerebro/Foruns/manus_achados_canibais.jsonl`). Depois CM/CL leem e aplicam a meta se concordarem.

## Onde Manus escreve

Sem instrução explícita do Miguel. Sugestões (aguarda decisão):
- `Cerebro/Foruns/manus_vigilia_editorial/achados_YYYYMMDD.md` (append-only por dia)
- Google Drive `PONTE_DRIVE_LAURA/manus_achados.md`

Se Manus não escrever proativamente, tratar como observador silencioso — CM e CL verificam periodicamente se ele gerou output útil.

## Régua sucesso 24h

- Se Manus produz achados úteis (canibais detectados, títulos >80 encontrados, §127 catches) → mantém 1h
- Se produz ruído (falsos positivos, análises redundantes) → escalar 2h
- Se silencia (nenhum achado por >6h) → verificar se agendamento não caiu

## Refs

- [[project-trindade-reduzida-apenas-loop-laura-claude-grok-20260820]] (composição anterior 4 agentes)
- [[feedback-comunicacao-miguel-agentes-hibrida-20260820]] (Manus lê Cérebro mas não recebe recado direto — é polling)
- [[CM-20260820-001]] missões Loop Laura
- [[CM-20260820-006]] convenção meta descartado_canibal
