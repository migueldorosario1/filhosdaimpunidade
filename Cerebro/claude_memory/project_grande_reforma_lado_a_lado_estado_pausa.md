---
name: project-grande-reforma-lado-a-lado-estado-pausa
description: "Estado da Grande Reforma frente Lado a Lado pausada 13/06 ~23:50 BRT. 5 Dilemas VOTADOS 5/5 pela Trindade, aguardam sanção Miguel. Staging sem patches, gap arquitetural pendente A/B/C. Testes 5-8 BLOQUEADOS."
metadata: 
  node_type: memory
  type: project
  originSessionId: 417ea1cb-f7cb-41c7-b869-848cc256e49c
---

**Estado em 2026-06-13 23:50 BRT (ponto de pausa atualizado pós-síntese 5 dilemas):**

Grande Reforma frente Lado a Lado (migração Tencent `/root/cafezinho/`) **PAUSADA** com bloqueio ativo. Sprint decisório dos 5 dilemas **FECHADO** pela Trindade (5/5 votado), aguarda sanção Miguel.

**O que está feito:**
- ✅ Backup snapshot `/root/snapshot_root_pre_reforma_20260613.tar.gz` FINALIZADO (6.4GB, terminou às 14:36 BRT, PID 274072 encerrou naturalmente)
- ✅ Permissões ajustadas por Claude: legado `/root/agent_data/banco_midia/` 777→750 (pasta) + 640 (SQLite); staging `/root/cafezinho/dados_agentes/banco_midia/` 750/640
- ✅ Banco SQLite 17MB preservado no staging (`/root/cafezinho/dados_agentes/banco_midia/banco_imagens_reais.db` — 17825792 bytes, permissões `rw-rw---- root:ubuntu`)
- ✅ Estrutura física criada: `dados_agentes/{banco_midia,logs,relatorios_janitor,backups_frios}` + `portal_cafezinho/` (LIMPO) + `sites_tematicos/` (vazio)
- ✅ **Kimi limpou `portal_cafezinho/` em 16:02 BRT** (`rm -rf /root/cafezinho/portal_cafezinho/*`) — removeu cópia errada do legado, preservou banco e pastas
- ✅ Patches Codex/Antigravity validados no workspace local `A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/`: `WP_STATUS_PERMITIDOS={"draft","pending","private"}` (publish nem entra na lista), `BANCO_MIDIA_DB` via env
- ✅ Unificação do Cérebro aprovada (voto final Claude no fórum)
- ✅ EC1 sancionada (teto canal 100/300 sprint especial)
- ✅ EC2 sancionada (~22:00 BRT) — WebSearch obrigatório quando info diverge do treinamento
- ✅ **5 Dilemas Antigravity VOTADOS 5/5** (DeepSeek+Qwen+Codex+Kimi+Claude). Decisão finalíssima consolidada por Codex (sec 9-10 do fórum), endossada por Claude com cláusula TTL 24h (sec 11)

**5 Dilemas — decisão consolidada (aguarda sanção Miguel):**
1. Fact-check: **HÍBRIDO** — fail-close coleta para eleicoes/nacional (matéria fica `duvidoso`/`bloqueada_factcheck`), fail-open produção demais. Claude propôs TTL 24h — após isso, publicar com flag `auditoria_pendente` (preserva `feedback_soltar_posts_nao_prender`)
2. Jaccard: **48h default + overrides** (24h eleicoes, 7d fantastico, 30d evergreen, 48-72h geopolitica)
3. SQLite: **WAL + BEGIN IMMEDIATE + busy_timeout + retry backoff + Maestro serial** (consenso total 5/5)
4. Quotas: **P0 eleicoes, P1 nacional/lula/geopolitica, P2 soberania/seguranca/ia, P3 fantastico/sobrenatural/esportes**
5. Autocura: **Camada 1 (pipeline SQLite) agora + Camada 2 (WordPress) pós-deploy gate**

**Pendências artefatos antes de codar (Codex sec 9.4):**
- `Config/criticidade_editorias.json`
- `Config/dedup_jaccard_editorias.json`
- `Config/prioridade_quotas.json`
- Smoke local WAL + transações + retry
- Estados fechados no pipeline: `unica`, `similar_alerta`, `duplicata_bloqueada`, `duvidoso`, `bloqueada_factcheck`

**Bloqueio ativo (testes 5-8 PROIBIDOS até resolução):**
- `portal_cafezinho/` está LIMPO (vazio) — espera código patcheado
- `sites_tematicos/` está vazio
- `.env.unificado` INEXISTENTE no staging
- Gap arquitetural A/B/C pendente decisão Miguel + Antigravity

**Gap arquitetural pendente decisão Miguel + Antigravity:**
- Maquete local tem estrutura rica: `Sistema/`, `Cerebro/`, `Config/`, `manifestos/`, `indices/`, `Keys/`, `Backups/`, etc.
- Plano de servidor prevê apenas: `portal_cafezinho/`, `dados_agentes/`, `sites_tematicos/`
- Opções: A (maquete vira raiz inteira — risco colisão `/root/Cerebro/` global) / B (subset `Sistema/` vira `portal_cafezinho/` — perde config) / **C (Claude recomenda: adiar até Antigravity publicar mapa definitivo)**

**Why:** Kimi (Maestro Diagnóstico) executou Fase 1-4 dos smoke tests com cópia errada do legado, parou e documentou antes de rodar testes 5-8 (que enviam drafts/posts ao WP). Transparência dela evitou incidente de publish ao vivo.

**How to apply (próxima sessão):**
- Verificar se snapshot PID 274072 terminou (`ssh tencent 'sudo ps -p 274072'`)
- Checar fórum principal: `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/forum_plano_migracao_duplicada_lado_a_lado_tencent_20260613.md` (parecer Claude 14:50 BRT é o mais recente)
- Checar fórum balanço: `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/forum_grande_reforma_balanco_geral_e_consolidacao_20260613.md`
- Aguardar Miguel/Antigravity decidir Opção A/B/C antes de qualquer rsync para `/root/cafezinho/portal_cafezinho/`
- Enquanto pausado, NÃO rodar testes 5-8 (dry-run maestro, drafts WP, painel WP, dry-run GSN)

**Tick §53 13/06 10:49 (consolidado antes da pausa):**
- 20/20 posts auditados, 1 correção (#257914 entities título), 1 ping §93 (#257940 gap), 4 gaps §95 não-bloqueantes
- Padrão Cláudia 12/06+11/06: hiperlink 80%+ é bug estrutural top-1
- Relatório: `Foruns/monitoramento/2026/06/relatorio_qualidade_20260613_10h49.md`

**Relacionado:** [[feedback_kimi_transparencia_impediu_incidente_publish]], [[feedback_deploy_gate_92]], [[project_baseline_banco_midia_s9]], [[project_grande_reforma_frente_deduplicacao_pautas]], [[feedback_emenda_constitucional_1_teto_canal]].
