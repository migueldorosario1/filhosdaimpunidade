# 🧠 MEMÓRIA — Plano de emergência 4 níveis + aplicação do Mínimo (log técnico, 11/09/2026)

Companion do `Foruns/forum_plano_emergencia_4_niveis_20260911.md`. Executor: ZCode/GLM-5.3, sessão 11/09 09:40→. Ref ZM-20260911-EMERGENCIA. Continuação do `forum_freio_gasto_deepseek_20260911.md` (primeira leva do freio).

## Mudanças por host (todas com backup + prova)

**Dell** (backup `~/crontab.bak_pre_plano_minimo_20260911`):
- COMENTADOS (tag `# PAUSA_PLANO_MINIMO_20260911`): ronda_30min.sh (DS Miguel, já estava 0 */4) · consumidor_gsn_fila.py.
- Cofres: `Projeto Cafezinho Agentes/root/.env.unificado` e `Outros/chaves/agentes_labs/.env.unificado` — DEEPSEEK_API_KEY → canônica (sk-a20c…, sha8 2b0569ed) + linha nova `DEEPSEEK_API_KEY_DSN=` (sk-3d49…, sha8 f5ee9259, referência). Backups `.bak_pre_chave_ds_20260911`.

**Tencent ubuntu** (backup `~/crontab.bak_pre_plano_minimo_20260911`):
- Flags `.pause` criadas em `v6_data/controles/`: dsn_chefe, dsn_ideias, dsn_youtube, dsn_revisor1, dsn_revisor2, cafezinho_hourly, v41_player, v42_investimento (+ alimentador_yt depois que o cron ganhou guard `[ -f …alimentador_yt.pause ] && exit 0`). Guards provados.
- Chaves: `~/.dsh/deepseek_env` + `~/.env.unificado` → DSN nova (robôs pausados, nada gasta); `~/.dsh/llm_env` += `DEEPSEEK_API_KEY_VIGIA=<canônica>`.
- Vigia P11: patch `k = chave("DEEPSEEK_API_KEY_VIGIA") or chave("DEEPSEEK_API_KEY")`; prova: "verde: saldo 4.25" 09:49:46 (saldo ÚNICO da conta — as 2 chaves novas são da mesma conta).
- NOVO: `/home/ubuntu/bin/plano_uso.sh {status|pro|basico|minimo|zero}` — flags tencent + checklists impressos NYC/Dell/159 + histórico `v6_data/controles/plano_uso_historico.log`.

**Tencent root** (backup `/root/crontab.bak_pre_plano_minimo_20260911`):
- `monitor_chaves_api.py` — `--test-api` REMOVIDO (fazia 96 chamadas LLM reais/dia, uma por chave ativa; linha corrigida p/ manter redirecionamento de log — `#` em crontab engole o resto da linha, 1ª versão minha quebrou o >>log).

**NYC root** (backup `/root/crontab.bak_pre_plano_minimo_20260911`; flags em `/root/controles_pause/`):
- v41_ciclo geral: `25 */2` → `25 7,19` com guard v41_ciclo.pause; economia: `35 1-23/2` → `35 13` com mesmo guard (flag = kill do Zero; NÃO criar flag no Mínimo — eu criei por engano e removi na hora).
- COMENTADOS: verticais ciência (45 */2), geopolitica (55 * — 24×/d da ordem 09/09), meio_ambiente, esporte, saúde, digital, cultura + `ciclo_v42.py --tema auto --publicar` + `agente_validador_modelos.py` (fio: chamadas reais/dia).
- Flags: comentarista, auditor_titulos, manchete, repetidor_estatal, media_promoter, media_expander, cicero_tematicos.
- Chave canônica aplicada em `/root/chaves.sh` + `/root/.env.unificado` (`.bak_pre_chave_ds_20260911`); prova: chat flash RESPOSTA OK; saldo conta US$ 4,25.
- Ligados: dsn_imagem (capas), autocura_fila (ordem Miguel "feira nunca vazia"), youtube_v2_pipeline+ingestor (canônico), v42 coletores+ingestor (dados), tendencias_intake, SEO/GSC/GA4, fiscal, autocura.

**159** (backup `/root/crontab.bak_pre_plano_minimo_20260911` no próprio 159, via ssh tencent→159 com id_ed25519_telemetria_159): cicero_cron_rotativo ×2 + cicero_remote_publish COMENTADOS; indexador segue.

## Lições/armadilhas
- Comentário inline em crontab: tudo após `#` MORRE (inclusive >>log) — tag de pausa deve ir no FIM da linha.
- eu criei flag v41_ciclo.pause junto com a cadência mínima — flag kill ≠ nível mínimo; removida no mesmo minuto (a fábrica Mínima precisa PRODUZIR 2-3/dia).
- A chave DSN "pendente" foi gravada nos cofres tencent porque robôs DSN estão 100% pausados por flags — gravar não gasta; religação nasce certa.
- Saldo das 2 chaves novas é o MESMO (conta única) — P11 na canônica cobre tudo.

## Provas de aceite pendentes
- Ciclo fábrica 13:35 (economia) e 19:25 (geral) de hoje: 2-3 posts saindo + eventos no banco_custos com chave nova.
- 12:00/16:00: rondas chefe/DS Miguel PULAM (flag/cron comentado) — silêncio esperado nos logs.

## Estado
MÍNIMO no ar (11/09 ~10:0x). Saldo conta US$ 4,25 → recarregar (Miguel). Tudo reversível por `plano_uso.sh` + backups datados.
