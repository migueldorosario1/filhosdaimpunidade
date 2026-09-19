# Memória — Correção do sync contínuo Cérebro ↔ GitHub

Em 14/08/2026, Miguel autorizou corrigir a ponte que podia deixar commits
locais pendentes. O sincronizador passou a sempre enviar commits, integrar o
remoto, repetir falhas e serializar as duas direções com lock. Pull+rsync roda a
cada 15 minutos; push roda sete minutos depois. Falha de DNS não impede mais o
último clone confirmado de chegar ao Cérebro.

Validação final: três ACKs de LAURA no canônico, worktree limpo e divergência
GitHub `0/0`. Detalhes: `Foruns/forum_correcao_sync_cerebro_github_20260814.md`.
