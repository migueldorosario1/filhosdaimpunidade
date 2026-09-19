# Memória — Recuperação do Heartbeat do Cafedash

**Registrada em:** 20/08/2026, 10:12 BRT.  
**Fórum:** `Foruns/forum_cafedash_recuperacao_heartbeat_20260820.md`.

O monitoramento GA4 do projeto Manus `cafezinho-dashboard` entrou em recuperação após falhas 503 por memória e timeout. O callback de 15 minutos não deve executar sincronização histórica. O Realtime e a emissão do relatório de 30 minutos usam `/api/scheduled/ga4-half-hour-report`; o histórico diário usa `/api/scheduled/ga4-daily-history`.

Jobs vigentes: Realtime `fx5NZ9tsCmCuRTbWA6Qq9L`, cron `0 */15 * * * *`; histórico `Q9Hkh37MvnhGnagSTcNj7V`, cron `0 5 4 * * *`. O job anterior `FZvHKyTBDz2gVg55sV8Hzg` foi removido e não deve ser reativado. A migração do vínculo do job histórico foi aplicada; o código publicado foi validado com 27 testes, TypeScript e build.

No momento deste registro, ainda falta observar uma execução `success` do novo Realtime e uma nova janela de 30 minutos antes de declarar que o loop está normal. Nenhuma credencial foi lida ou registrada. A próxima sessão deve usar o handoff local do projeto e registrar apenas evidências novas.

**Adendo:** teste temporário de um minuto não criou runs, embora `next_execution_at` tenha avançado. A rota publicada respondeu 403 sem credencial, logo está presente. Tratar como possível falha de entrega do agendador e escalar pelo painel de Jobs/Investigate antes de alterar novamente a arquitetura do callback.
