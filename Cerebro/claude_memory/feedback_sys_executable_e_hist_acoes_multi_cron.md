---
name: sys-executable-e-hist-acoes-multi-cron
description: Duas regras estruturais para Sentinela — sys.executable em subprocess Python multi-ambiente (ENV) + post_ids no histórico quando múltiplos crons escrevem mesmo JSONL (HIST)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a0935816-574e-4c24-a84b-340dede75e48
---

**Regra ENV (Bug #27):** em qualquer `subprocess.run(["python3", ...])` de scripts que rodam em cron/systemd/harness diferentes, usar `sys.executable` no lugar de `"python3"`. `python3` do PATH depende do processo pai — cron com PATH limitado (`/usr/bin:/bin`) resolve pra `/usr/bin/python3` (Ubuntu 20.04 = 3.8.10 = sem `zoneinfo`), enquanto shell interativo com pyenv resolve pra `.pyenv/versions/3.10.13/bin/python3` (com zoneinfo). Discrepância silenciosa: subprocess falha só em cron. `sys.executable` = MESMO interpreter que roda o processo pai — passa o pyenv corretamente. Zero dependências novas.

**Why ENV:** 25/07 01:00-01:36 BRT, Kimi K3 detectou padrão de intermitência — ciclos Sentinela hora cheia (00:00, 01:00) falhavam com `ModuleNotFoundError: zoneinfo` em `coletar_uptimerobot` + `coletar_auditor_titulos`; ciclos meus via `/loop` (00:17, 00:39, 01:09) passavam. Diagnóstico bateu: dois ambientes Python distintos, cron nativo herda PATH sistema (sem pyenv), harness herda meu PATH interativo. Fix aplicado em `sentinela_ciclo.py` linhas 142+158. Backup `sentinela_ciclo.py.bak_pre_claude_zoneinfo_20260725_0130` SHA-256 `efc1418e...ed1f8`.

**How to apply ENV:** ao ver `subprocess.*python3` no diff/patch, sempre trocar por `sys.executable`. Exceção: quando *intencionalmente* se quer usar outro interpreter (ex: teste cross-version). Nesse caso, comentar por quê. Auditoria futura sugerida: grep `subprocess.*python3` em todos os agentes NYC + local.

---

**Regra HIST (Bug #28):** quando múltiplos agentes/crons escrevem no MESMO log estruturado (JSONL), o histórico passado ao LLM analisador precisa incluir **identificadores das entidades tocadas** (post_id, ticket_id, ID), não só sumário textual. Sumário serve pra humano; LLM precisa referência exata pra reconciliar estado atual com ações passadas — senão vai reportar "permanece" quando ação já foi aplicada por outro escritor.

**Why HIST:** 25/07 01:00 BRT, cron sistema Sentinela aplicou `corrigir_grafia` no post 262819 ("aumenta"→"aumentam"). 01:09 BRT, cron do meu `/loop` Sentinela leu o mesmo `ciclos.jsonl`, viu apenas `{ts_brt, severidade, resumo_executivo}` no histórico — sem post_id da ação. LLM (DeepSeek V4 Pro) analisou post 262819 no WP (já corrigido) mas o resumo textual do histórico não deixou claro que ele já tinha sido tocado; LLM reportou "permanece". Kimi K3 detectou pela leitura dos 6 ciclos passados. Fix: novo helper `_extrair_detalhes_acoes(resultado)` filtra ABORT/skip/erro e devolve `[{tipo, post_id, acao}]`; `gravar_log_jsonl` grava campo `acoes_detalhes` (backward-compat); `coletar_historico` propaga; `config/prompts.md` seção "Sua missão a cada ciclo" ganhou regra explícita citando caso 262819. Backup `prompts.md.bak_pre_claude_acoes_recentes_20260725_0135` SHA-256 `07e7c6e1...45f2c`.

**How to apply HIST:** ao adicionar 2º escritor no mesmo log estruturado (JSONL, DB row, TSV), verificar se o consumidor (LLM ou agente) recebe **IDs**, não só resumo. Se resumo é texto livre, adicionar campo estruturado `<acao>_ids: [...]`. Regra derivada: **bandeira vermelha** = relatório do ciclo diz "permanece"/"pendente" mas ação de mesmo tipo/entity_id apareceu em `acoes_aplicadas`/`acoes_detalhes` dos últimos N ciclos = incoerência automática. Detecção futura pode virar assert no `gerar_resumo_deterministico` (mata o ciclo se inconsistente).

**Bandeira vermelha genérica:** dois agentes com mesmo poder de escrita + zero coordenação = eventualmente vão contradizer um ao outro. Sempre que criar 2º agente com poder de escrita compartilhado, projetar contexto rico primeiro (IDs, timestamps precisos, tipo de ação), não deixar o LLM reconstruir a coerência de resumos.

**Regras irmãs:** [[protocolo-memoria-bugs-ler-antes-agir]] (protocolo geral), [[consulta-kimi-k3-3h-autonomia-claude]] (autoria do diagnóstico).
