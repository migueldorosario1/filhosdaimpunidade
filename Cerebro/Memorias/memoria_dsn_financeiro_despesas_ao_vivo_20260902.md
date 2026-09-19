# 🏦 Memória — DSN Financeiro & a página "Despesas ao vivo" (2026-09-02/03)

> Criada em 03/09/2026 ~00:1x BRT (ZCode/GLM-5.3, DSH us65), fechando o ciclo da noite:
> ordem do Miguel "a página despesas ao vivo tá errada — dá um sentido a ela" +
> "pensa se vale a pena telemetria redundante" + "todos os DSN mandam pro financeiro,
> que manda o relatório pro Chefe, que manda pra mim".
> Fonte completa: `Foruns/forum_dsn_financeiro_rastreador_custos_20260902.md` (fases 1-3).

## O invariantes que ficam (quem mexer nisso lê primeiro)

1. **Página de custo mostra sempre OS DOIS métodos**: por-evento (o que loga) e âncora
   de saldo (queda do saldo oficial = gasto real agregado). Só o por-evento = mentira
   por omissão — foi o "tá errada" de 02/09: página dizia US$ 5,09 enquanto o dia real
   custou US$ 14,26 (US$ 9,17 do pool DeepSeek invisível).
2. **Pool DeepSeek é UM só** (chave compartilhada Tencent+us65, descoberta §2.4 do fórum):
   a âncora mede robôs+escritório juntos. **NUNCA somar** eventos deepseek-Tencent com a
   âncora (o total real = eventos de todos − deepseek-tencent + queda do saldo).
3. **Recarga ≠ gasto**: saldo subindo é recarga (anota, não soma). Saldos caem em degraus
   de 15 min (ronda do DSN-F) — precisão da âncora ≈ US$ 0,01-0,05 por leitura.
4. **Dedup em toda agregação multi-fonte**: chave `(agente, modelo, segundo, tokens)`;
   `corr_id` ausente não pode ser a única defesa (bug do `extras`×glob na fase 2: o glob
   `banco_custos_*.jsonl` já pegava `banco_custos_tencent.jsonl`/`_dell.jsonl` — listar de
   novo = 2×).
5. **Fusos**: NYC grava UTC; gerenciador da Tencent grava BRT local → −3h no ponto de
   leitura. Erro aqui desloca eventos para o dia errado no relatório.
6. **Relatório diário às 06:35** (1ª ronda DSN-F após 06:30) → `Foruns/financeiro/
   relatorios/<dia>.md` — ANTES da Baleia Azul do Chefe (07:10), que embute a seção 💰
   e reporta ao Miguel. O contador não gasta (zero LLM) e não toca git (sync publica).
7. **Alarme de saldo < US$ 2** por Telegram é essencial (1×/dia máx) — 02/09 o pool foi
   de 12,83 a 5,63 sem ninguém saber antes da recarga de ~19.

## Redundância de telemetria (parecer aprovado na fase 3)

O modelo certo é **métodos independentes cruzados automaticamente** (A: evento por chamada ·
B: âncora de saldo · C: fatura/CSV semanal), como FAROL×GA4 na audiência. **Não** duplicar
o sistema de evento: dois medidores do mesmo método erram juntos (esquecem o robô que não
loga — o erro real de 02/09). Fase 4: vigília diária A×B com alerta > US$ 1/dia (estender
o §5c do vigia NYC ao pool compartilhado).

## Onde as coisas vivem

- Código: Tencent `~/dsn_financeiro/` (espelho da oficina no repo:
  `.tencent_v6_oficina/dsn_financeiro/`; painel da noite em `deploy_noite_20260902/`).
- Cron Tencent: `*/15` DSN-F (flock) · `*/5` pontos · `1min` temáticos · `domingo 12h`
  reconciliador · `04:10` R2 backup · flusher ao_vivo_nyc roda NO NYC.
- Saídas: `v6_data/custos/financeiro_{7d,llms,cobertura}.json` +
  `financeiro_relatorio_diario.md`; canal `Foruns/financeiro/canal_dsn_financeiro.md`.
- Backups do deploy: `painel_cctv_v6.py.bak_pre_ancora_20260902` ·
  `dsn_financeiro.py.bak_pre_relatorio_20260902`.

## Lição transversal

Quando o Miguel diz que um número "tá errado", **medir contra uma âncora independente
antes de mexer na aritmética**: em 02/09 a aritmética estava certa e o RETRATO estava
errado (cobertura). A âncora transforma "acho que tá errado" em número auditável — e
vira feature permanente (cartão vermelho da página).

— ZCode/GLM-5.3 (DSH, us65) · 03/09/2026 00:1x BRT
