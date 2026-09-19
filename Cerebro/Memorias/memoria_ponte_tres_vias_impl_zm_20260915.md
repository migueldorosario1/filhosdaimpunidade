# Memória técnica — Implementação ZM Três Pontes (15/09/2026, noite)

Log técnico da implementação aprovada pelo Miguel. Decisões: `Foruns/forum_ponte_tres_vias_impl_zm_20260915.md`. Parecer prévio: `forum_ponte_tres_vias_parecer_zm_20260915.md`. Bloco na ponte: ZM-20260915-014.

## Linha do tempo e comandos-chave

1. Monitor: linha `ZM-TRES-PONTES-IMPL` (início 20:06, nota de pausa, fim 23:1x) via `Cerebro/Ferramentas/monitor_update.py`.
2. Backups: `.bak_pre_pontetresvias_20260915` para ponte_push.sh, sync_cerebro_to_github.py, sync_cerebro_from_github.sh (Dell, `scripts/`) e mirror_to_github.sh (NYC, `/root/bin/`). Aos pares com rollback de 1 linha documentado no fórum.
3. E3: criada árvore `caixa/` direto no repo (rito da ponte — copy_tree a exclui por design): CONTRATO_CAIXAS.md (regra 2 vias, formato MSG/ACK, FF/nunca force, pares por queda) + LEIA-ME por emissor (zm/astra/cl/agy_laura/cm). Commit c57d214ac; branch `caixas` criado e alinhado ao main por FF; push duplo origin+nyc; ls-remote confirma c57d214ac nos dois.
4. E4 (sync_cerebro_to_github.py): função `ingest_caixas()` (fetch refs/heads/caixas:refs/remotes/bridge/<r>-caixas de origin/nyc; ls-tree da CAIXA_TREE; git show → working tree; idempotente; colisão denunciada), degrau DEGRADADO-A (try integrate_remote; só exceções com «git fetch origin» viram degradado), `push_attempts=1` no degradado, exceção `PushFailed` (push_with_retry) capturada apenas no degradado. py_compile OK.
5. E5 (sync_cerebro_from_github.sh v2): contingência NYC (fetch nyc main + ff-only OU merge-base is-ancestor) + ingest bash dos arquivos novos do nyc/caixas; exits: 74 DEGRADADO-B, 75 clone congelado (como antes). Env overrides para fixtures. bash -n OK.
6. E2 (ponte_push.sh v1.3): PONTE_REPO/PONTE_DRIVE_DEST/PONTE_SKIP_TENCENT; GDrive → drive:espelho-zcode/ponte_zcode com includes completos; readbacks (ls-remote main==HEAD; rclone ls de_dell.md==stat; ssh stat no tencent); conf=rb_gh+rb_gd, reservas nyc/tc até conf=2; exits 0/2/1; health `push_2vias_v1.3 | gh=rb/ok | ... | confirmadas=N/2`. bash -n OK.
7. NYC: mirror_to_github.sh v2.1 (passo caixas FF best-effort no início; `git show-ref --verify refs/heads/caixas` guard). scp + prova ao vivo: «2026-09-15 23:10:17 caixas: reconciliadas ao github (FF)».
8. Fixtures v3 (`/tmp/fixture_tres_pontas.sh`): bares origin.git/nyc.git com `symbolic-ref HEAD refs/heads/main` (git 2.25.1 não tem init -b), clone dell com as 3 árvores do add (projeto_cafezinho_agentes/foruns e global_south_news incluídas), trava anti-produção (aborta se dell/.git não existe). RESULTADO 13/13: T1a/b/c, T2, T3a/b/c, T6, T7a-d.
9. Provas reais: sync manual 23:11 (12213 arquivos, GitHub 1/6, NYC alinhado, LAURA 1474) · ponte_push real exit 0 `gh=1/1 gdrive=1/1 confirmadas=2/2 commit=79206f88d por=ZM` · rclone lsf do estepe: de_astra.md + caixa/ completos.
10. Commits de implementação: c57d214ac (caixa/), ad88c641f (E2/E4/E5 + baks), 8b246b8b6 (fix PushFailed) — todos pushados na hora.

## Incidente e lição (importante para a casa)

Pausa do Miguel 20:13→~22:55. Na retomada, os 3 scripts editados sem commit estavam REVERTIDOS no working tree do repo compartilhado (e os .bak untracked apagados) — reset/checkout de sessão paralela ou de rebase autostash de outro runner; exatamente a classe do incidente XM (ZM-20260914-009). Primeira rodada de fixtures com o clone de teste quebrado + script sem override → T7 executou o v1.2 contra o REPO REAL (pushes origin/nyc + rclone gdrive normais; sem dano funcional, mas teste inválido e 3 carimbos health extras 22:58-59). Recuperação completa + regra reforçada: escrever no repo compartilhado e NÃO commitar = perder; sempre commit+push imediato (agora cumprido: cada mudança foi commitada no minuto).

Bug próprio pego nos fixtures: o primeiro `except RuntimeError` do degradado engolia erro de `git add` (pathspec morto no fixture) imprimindo 🔴 falso — corrigido com `PushFailed` (subclasse) capturada somente no degradado; erros de staging abortam sempre.

## O que falta / preciso de você (Miguel)

1. Pedir a auditoria da Astra quando quiser (material: fórum impl + parecer + retorno ZM-RETORNO-ASTRA-TRES-PONTES + CONTRATO_CAIXAS.md no repo/Drive).
2. E6 (leitor 2-vias com dedupe + pendências de ACK) é a parte da Astra.
3. Pendências menores: unificar o gdrive: do ponte_zm_dsc no drive:; oficializar janela de ACK (60min?); levantamento de acesso Windows (CL/AGY-LAURA).
4. Adoção gradual pelas equipes: ao escrever bloco na ponte, gravar também o MSG- na própria caixa (contrato publicado no repo e no Drive).

— ZCode Miguel (ZM) · GLM-5.3 · 15/09/2026 23:1x BRT
