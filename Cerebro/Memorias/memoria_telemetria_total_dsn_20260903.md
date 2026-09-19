# Memória técnica — Telemetria TOTAL DSN (03/09/2026, ZCode/Kimi K3)

Log técnico completo da sessão. Fórum irmão: `Foruns/forum_telemetria_total_dsn_20260903.md`.

## Arquitetura de custo (mapa final provado)

```
TENCENT (43.156.151.165, ubuntu)
├─ robôs Python (ds_youtube, revisor1/2, escuta chefe, maira, publicador)
│    → import telemetry_log (~/dsn_financeiro) → log_llm/log_tokens
│    → ~/cafezinho/v6_data/custos/banco_custos_tencent.jsonl
├─ rondas dsh headless (chefe */30, ideias 13,43)
│    → sessions zstd ~/.dsh/sessions/**/session-*/session.jsonl.zstd
│    → coletor dsh_telemetria_colhe.py (hook no fim de cada ronda_*.sh)
│    → mesmo banco (data REAL do evento + corr_id=sha1 linha)
├─ roteador agente_roteador_llm → gerenciador_tokens
│    → Projeto Cafezinho Agentes/root/agent_data/banco_custos_YYYY-MM.jsonl
└─ DSN Financeiro (*/15) lê TUDO → financeiro_7d.json / financeiro_llms.json
   / financeiro_cobertura.json / relatório diário md → painel + canal + Telegram

NYC (198.199.121.136, root)
├─ V4.1 inteiro + youtube_v2 materializador → agente_roteador_llm ✅ (já era)
├─ factory media_vision_providers.py (qwen/deepseek/gemini) ← PATCH hoje
│    cobre dsn_imagem, olho_apurado, auditor gráficos v42
│    (agente = sys.argv[0] automaticamente)
├─ redator_economia_v4.chamar_llm ← PATCH hoje (v42_redator_economia)
└─ flusher_ao_vivo */1min → ao_vivo_nyc.jsonl na Tencent; banco_custos_YYYY-MM
   vai por rsync/self-heal

TEMÁTICOS (159.89.185.209, root)
├─ roteadores cicero/gsn: gerenciador_tokens estava =None de propósito
│    ("até o módulo estabilizar") → mini-gerenciador FAIL-NEVER instalado
│    (/root/gerenciador_tokens.py + ponte cicero_gerenciador_tokens.py)
│    + try/import reativado nas 2 funções geradoras
└─ grava /root/agent_data/banco_custos_YYYY-MM.jsonl → rsync 1min da Tencent
   → ao_vivo_tematicos.jsonl
```

## Arquivos tocados (todos com .bak_pre_telemetria_dsn_20260903 ou _fN)

**Tencent:**
- `/home/ubuntu/ds_youtube/ds_youtube.py` — log após r.json() (texto corrigido)
- `/home/ubuntu/dsn_revisor1/dsn_revisor1.py` — patch no `_req_json` (cobre tudo)
- `/home/ubuntu/dsn_revisor2/dsn_revisor2.py` — idem
- `/home/ubuntu/ds_nuvem_chefe/escuta.py` — log após resp DeepSeek
- `/usr/local/bin/maira_bot.py` — log após r DeepSeek (via sudo; dono root mantido)
- `/home/ubuntu/ronda_dsn.sh` + `/home/ubuntu/dsn_ideias/ronda_dsn_ideias.sh` — hook coletor no fim (bash -n OK)
- `/home/ubuntu/dsn_financeiro/telemetry_log.py` — cache_read_tokens (0,26×) + data_utc
- `/home/ubuntu/dsn_financeiro/dsh_telemetria_colhe.py` — NOVO (zstd → usage; dedup hash; janela)
- `/home/ubuntu/dsn_financeiro/dsn_financeiro.py` — F4: guarda snapshot banco tencent; lacuna 159 atualizada; debug tg; F5: TELEGRAM_TOKEN; F6: bot próprio @Dsnfinancas_bot
- cofre `/home/ubuntu/.env.unificado` — TELEGRAM_TOKEN_DSN_FINANCAS (sha8 1bbc9514)

**NYC:**
- `/root/v4_labs/codigo/media_vision_providers.py` — helper `_telemetria_visao` + 3 providers
- `/root/v4_labs/codigo/agente_economia/redator_economia_v4.py` — log em `chamar_llm`

**159:** `/root/gerenciador_tokens.py` (NOVO), `/root/cicero_gerenciador_tokens.py` (NOVO ponte), patches em `cicero_agente_roteador_llm.py` + `gsn_agente_roteador_llm.py` (try/import).

**Dell:** cofres `Projeto Cafezinho Agentes/root/.env.unificado` e `Outros/chaves/agentes_labs/.env.unificado` (mesma chave, hash igual).

## Provas E2E
- banco_custos_tencent.jsonl nasceu 07:39 (370→reimport 1627 eventos com data real)
- Painel `/telemetria/v1/ultimos?n=500`: janela 1h = $0.7473, 66 chamadas; agentes novos visíveis (dsn_ideias $0.41, dsn_revisor2 $0.22, youtube_v2_materializador $0.12)
- DSN-F ronda 73: tencent aparece no por_servidor ($0.41 após apagão; guarda posta depois)
- Telegram: 2 envios TRUE (bot antigo curado + bot novo @Dsnfinancas_bot)

## Incidentes da sessão
1. **Apagão do banco tencent ~08:0x** (1627→56 linhas) — mesmo mistério do incidente 02/09 ("alguém apaga jsonl em v6_data/custos"). Não é cron conhecido (caetano 06:00, janitor domingo). Mitigado: snapshot/restore no self-heal do DSN-F. PENDENTE: achar o apagador (sugestão: auditd ou inotifywait pontual em v6_data/custos).
2. **Dedup do agregador colapsava** registros sem corr_id (id(r) reutilizado por GC + mesma data) — curado na fonte (corr_id+data real).
3. **Medição dsh × âncora de saldo divergem ~7×** ($14,5 por evento em 2h20 × ~$2 pela âncora) — hipótese: usage do dsh por turno acumula contexto. DSN-F mantém os dois lados (evento + âncora sem 2×); refino pendente.

## Comandos de verificação rápida
```
ssh tencent 'tail -3 ~/cafezinho/v6_data/custos/banco_custos_tencent.jsonl'
ssh tencent 'curl -s "http://127.0.0.1:8084/telemetria/v1/ultimos?n=100" | head -c 400'
ssh tencent 'tail -5 ~/dsn_financeiro/log/$(date +%F).log'
```


## ADENDO 08:5x — Repetidor Estatal descido (ordem Miguel)
- `/root/agente_repetidor_estatal.py` (NYC, `.bak_pre_repetidor_ds_20260903`):
  import ganha `gerar_texto_modelo_especifico`; ranker (top 3) e reescrita
  (`contexto="padrao"` → deepseek-chat forçado, fallback `contexto="economico"`).
- Smoke: deepseek-chat respondeu OK (temp forçada a 0.1 pelo anti-alucinação do roteador).
- Tabela de preços do DSN-F ganhou gpt-5-mini/gpt-5-nano/grok-4 (61 modelos).
- Mapa tese/curadoria provado: `_tese_frontier` (knob dados/ultra_luxo.json["geral"]=gpt-5.6-sol);
  cadeia verifier do ciclo = GLM→DeepSeek→Moonshot; FC com busca viva (Perplexity fora por ordem).

## ADENDO 2 — curadoria deepseek-chat: estágio 0 em `_verifier_llm_json` (âncora = merge full_env; fallback intacto; env V4_CURADORIA_MODEL; smoke provado no ledger calls_*.jsonl).

## ADENDO 3 — cascata curadoria: loop 4 estágios (DS-chat→GLM5.3→Mistral→K3) substituiu estágio único; max_tokens 8000 (BUG-DS-102); Mistral billing 402 anotado; `.bak_pre_curadoria_cascata_20260903`.
