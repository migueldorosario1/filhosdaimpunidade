# Memória técnica — Parecer ZM Três Pontes (15/09/2026)

Log técnico completo da missão de análise (nada implementado). Decisões resumidas em `Foruns/forum_ponte_tres_vias_parecer_zm_20260915.md`. Bloco na ponte: ZM-20260915-011 (de_dell.md).

## O que aconteceu

Miguel colou no chat ZM a análise da Astra (AST-TRES-PONTES-20260915) + prompt endereçado a @ZM + o esclarecimento dele: GitHub principal, GDrive e NYC alternativas, comunicação SEMPRE por duas vias (par vigente conforme queda), terceira via completa o par. Pedido: analisar, dar parecer e devolver PROMPT DE RETORNO PARA ASTRA; Miguel decide quem coda depois.

## Inspeção realizada (read-only, sem deploy)

1. `Cerebro/MONITORAMENTO_DE_TRABALHO.md` lido; linha `ZM-TRES-PONTES-PARECER` registrada via `Cerebro/Ferramentas/monitor_update.py` (protocolo v2) às 19:50.
2. `Cerebro/Relatorios/astra/ronda_horaria/AST-TRES-PONTES-20260915.md` lido na íntegra.
3. Blocos citados conferidos no `de_dell.md` (repo/canônica): ZM-20260914-009 (reativação NYC, push duplo, força do espelho documentada), ZM-20260914-017/018 (ronda 4/4h, automation-7bfdd5e5), ZM-20260915-008-PONTE-RONDA (sync travado por porta_voz), ZM-20260915-010 (cura LEDGER_DIR na canônica).
4. `scripts/sync_cerebro_from_github.sh` (52 linhas, lido completo): fetch origin 6 tentativas com backoff 2/4/8/16/30s + ff-only; depois rsync clone→canônica SEMPRE; exit 75 se GitHub falhou. Sem NYC/Drive.
5. `scripts/sync_cerebro_to_github.py` (792 linhas, lido completo): fluxo `sync_locked` = integrate_remote (ensure_clean_worktree + fetch_with_retry + ff-only/rebase) → reconciles LAURA/memórias vivas → copy_tree → verify → git_commit_push (add seletivo 3 árvores + commit + push_with_retry). `push_with_retry`: push origin até 6×; integra remoto em rejected/non-ff; na última tentativa chama `push_mirror_nyc` ANTES de levantar. `push_mirror_nyc`: `push --force nyc HEAD:main`, best-effort. Exclusões de copy_tree incluem `ponte_laura_completa` (append-only por GIT exclusivo — bug ZL-027).
6. `scripts/ponte_push.sh` v1.2 (62 linhas): GitHub (fetch+rebase autostash+push 3×) → GDrive via `gdrive:ponte_laura_completa` (include sem de_astra.md) → reservas NYC (git push nyc) e Tencent (tar-pipe sudo) se uma ativa caiu; exit 1 só se TODAS falharem; health em `estado/ponte_health.md`.
7. Crons Dell conferidos (`crontab -l`): sync push `7,22,37,52` (CEREBRO_DRY_RUN=0); pull `0,15,30,45`; estepe GDrive `5,35` = `rclone copy Cerebro/Foruns/ponte_laura_completa → drive:espelho-zcode/ponte_zcode` (pasta inteira, SEM --delete); foruns→Tencent `7,37` (rsync --delete); rclone listremotes: drive:, gdrive:, b2..., gdrive-astra:, r2:.
8. NYC via ssh: crontab tem `*/5 /root/bin/mirror_to_github.sh` (CAMADA2_PONTE_V2); script lido: push github main; em non-ff/rejected → fetch; se mirror é ancestral do github-main = «github à frente, nada a reconciliar» exit 0; senão «main reescrito (rotina de rebase) — Dell re-alinha com force no próximo sync — sem ação» exit 0; falha real só com github inacessível. Mirror main `53653ed28` 19:37:30 «sync: 12171 arquivos» (sincronizado).
9. `rclone lsf drive:espelho-zcode/ponte_zcode/`: estrutura completa da ponte presente (de_astra.md, de_dell.md, baleia_azul/, escuta/, ledger/, estado/...).
10. Confirmada a existência de `de_astra.md` (402.987 bytes, mtime 14/09 20:31 — Astra muda ~25h, consistente com telemetria da ronda 16:00).

## Conclusões técnicas (resumo; detalhe no fórum)

- 7/7 achados da Astra confirmados; nuances em 3 e 6; agravos novos ZM-8 (queda total do GitHub aborta o sync ANTES do commit local — fallback NYC inalcançável) e ZM-9 (dois espelhos GDrive paralelos, remotes `gdrive:`×`drive:`, recortes distintos).
- Proposta recomendada: separar DISTRIBUIÇÃO (main espelhável com force + snapshots) de MENSAGEM (caixas append-only por emissor, arquivo imutável nomeado pelo ID da casa, branch `caixas` FF-only no origin e no mirror NYC — nunca no main do mirror; caixa/ no Drive é estável sob rclone copy; ACK como arquivo ACK-<id> na caixa do destinatário; entrega 2-vias com readback; leitura 2-vias; exit 2 = DEGRADADO).
- Cenários de queda, testes T1-T7 em fixtures, critérios de aceitação e divisão ZM (transporte Dell+NYC) × Astra (leitores+acesso Windows) documentados no fórum §5-§8.

## Arquivos tocados (somente análise + registros)

- Criados: `Cerebro/Foruns/forum_ponte_tres_vias_parecer_zm_20260915.md`, `Cerebro/Memorias/memoria_ponte_tres_vias_parecer_zm_20260915.md` (este).
- Append: `cerebro/Foruns/ponte_laura_completa/de_dell.md` (bloco ZM-20260915-011, no repo — rito append-only por GIT), `CEREBRO_NODE_ATUALIZACOES.md`, `CEREBRO_NODE_ARQUITETURA.md` (catalogação), linha no monitor.
- Nenhum script alterado; nenhum cron tocado; nenhum push forçado; credenciais não expostas.

## O que falta / o que preciso de você (Miguel)

1. Ler o parecer (fórum §3-§4) e DECIDIR: aprova o desenho das caixas imutáveis 2-vias? 
2. Definir QUEM CODA (sugestão §8: ZM transporte E2-E5, Astra leitores E6; pode ser só um dos dois).
3. Janela de ACK (sugestão: 60 min; rondas são 30-60min).
4. Decidir se CL/AGY-LAURA (Windows) ganham rclone Drive/ssh nyc (depende do levantamento da Astra).
5. «Vai» explícito para começar a implementação — esta etapa parou ANTES, como pedido.

— ZCode Miguel (ZM) · GLM-5.3 · 15/09/2026 ~19:5x BRT
