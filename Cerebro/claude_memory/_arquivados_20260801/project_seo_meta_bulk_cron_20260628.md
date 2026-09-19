---
name: seo-meta-bulk-cron-20260628
description: "Cron bulk meta description Cafezinho ativo Tencent 02:00 BRT, 1000/dia, Gemini Flash, 74.270 posts, ~75 dias, custo US$ 22, painel HTML disponível local."
metadata: 
  node_type: memory
  type: project
  originSessionId: 595de6c5-a613-4f51-b42d-e3bc009de9ef
---

# Cron bulk meta description SEO — ATIVO 28/06 ~23:40 BRT

**Status**: ✅ deployado e rodando (primeira execução 29/06 02:00 BRT)

## Configuração ativa

- **Script Tencent**: `/root/util_seo_meta_retroativo.py` (Gemini 2.5 Flash, com checkpoint + retry)
- **Cron**: `0 5 * * *` (05:00 UTC = 02:00 BRT) → `--limit 1000 --resume`
- **Sentinela**: `CRON_SEO_META_RETROATIVO_GLM_20260628`
- **Modelo**: `gemini-2.5-flash` com `thinkingConfig: {thinkingBudget: 0}` + `maxOutputTokens: 1024` (sem isso corta em ~30 chars)
- **Validador**: se meta >155 chars → 2a chamada Gemini pedindo encurtar; se ainda >160 → hard truncate em 152+"..."
- **Backup pré-deploy**: `/root/crontab_backup_pre_seo_meta_20260628_2339.txt`

## Estado do bulk

- **Total alvo**: 74.270 posts sem meta description
- **Pace**: 1000/dia (75 dias corridos)
- **Custo projetado**: US$ 22 total (US$ 0,0003/post médio)
- **Cron paralelo**: `*/5 * * * *` gera painel HTML
- **Checkpoint**: `/root/agent_data/seo_meta_checkpoint.json` (resume automático em falhas)
- **Logs**: `/root/agent_data/seo_meta_logs/run_gemini_*.jsonl` + `cron_bulk.log`
- **Painel**: `/root/agent_data/seo_meta_painel.html`

## Como ver progresso

- **Painel HTML** local: `bash "/home/migueldorosario/Downloads/Antigravity Google/Outros/painel_seo_meta/sync_painel_seo.sh"` — baixa + abre no browser
- **Painel mostra**: barra % crescendo, custo acumulado, sucesso/falha hoje, últimos 15 posts com meta gerada + tamanho + custo + status, log cron
- **Auto-refresh**: 60s no browser

## Estratégia Miguel-sanctioned (híbrido)

- 🆕 **NOVOS posts humanos**: GPT-5 via AI Engine + Automation no wp-admin (configurar manualmente, **pendente**)
- 📚 **RETROATIVO 74.270**: Gemini Flash via cron bulk (**ativo**)

## Decisões preservadas

- **Por que não GPT-5 no retroativo**: Miguel pediu inicialmente, mas custo US$ 700 vs US$ 22 do Gemini Flash (30x mais barato). Confirmado por Miguel.
- **Por que não SSH Tencent → ServerDo.in**: risco de segurança — se Tencent hackeado, ServerDo.in comprometido. Miguel optou por REST API (Opção A, mais segura).
- **Por que não snippet PHP custom no functions.php**: Miguel escolheu AI Engine (UI visual,_logs, escolher modelo por tarefa).

## Pendência paralela (não bloqueia bulk)

AI Engine precisa ser configurado manualmente no wp-admin: add chaves OpenAI + Gemini, criar Automation "On post save → generate Yoast meta description" com GPT-5. Passo a passo em `Foruns/forum_execucao_p0_wordpress_seo_20260628.md`. Chaves em `/root/.env.unificado` Tencent.

## Validações feitas (28/06 23:30 BRT)

- ✅ Piloto 5 com GPT-5 (3 sucesso, 2 falha reasoning → fix max_tokens 2000)
- ✅ Piloto 10 com Gemini Flash (100% sucesso após fix thinking + validador tamanho)
- ✅ Cron deployado com backup + sentinela
- ✅ Painel HTML gera OK
- ✅ Sync local → browser OK

## Próxima verificação

- **29/06 manhã (após 02:00 BRT)**: validar que cron disparou e processou ~1000 posts
- **28/09/2026**: bulk completo, comparar baseline Ahrefs

## Cross-references

- Snapshot sessão: `Projeto Cafezinho Agentes/Ponto de Retomada/GLM Coding/20260629_015600_sessao.md`
- Fórum execução: `Foruns/forum_execucao_p0_wordpress_seo_20260628.md`
- [[project-seo-monitoramento-fase0-20260628]] — context baseline
- [[feedback-ponto-retomada-checkpoints]] — cadência snapshots
