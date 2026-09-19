# 🌉 PONTE KIMI ↔ LOOP SENTINELA — LEIA PRIMEIRO

**Criada:** 2026-07-26 ~15:20 BRT por Kimi K3 (ZCode), a pedido direto do Miguel.
**Propósito:** ponte de conversa permanente entre o loop Sentinela do Claude (ciclo 30/30min, autocura) e o Kimi K3 (ZCode, sessões sob demanda do Miguel).

## Para o Kimi da próxima sessão (você)

**SEMPRE que o Miguel disser "dá uma olhada no loop", "como está o Cafezinho/temáticos", ou ANTES de qualquer missão de ecossistema, faça nesta ordem:**

1. Leia `ESTADO_ATUAL.md` (neste diretório) — minha última radiografia + pendências.
2. Leia `CONTRATO_PONTE_CLAUDE_KIMI.md` — os endereços canônicos dos arquivos do loop (se o Claude mudar algum path, ele atualiza o contrato).
3. Leitura viva rápida (2 min):
   ```bash
   tail -3 ~/ferramentas/sentinela/logs/ciclos.jsonl          # últimos ciclos (JSON)
   ls -t "Cerebro/Foruns/sentinela/$(date +%Y-%m)/" | head -3  # relatórios de ciclo recentes
   tail -20 "agent_data/v4/cron_v4.log"                       # coleta temáticos V4
   tail -5 "Cerebro/monitoramento_horario/bugs_encontrados/bugs_$(date +%Y-%m-%d).jsonl"
   ```
4. Atualize `ESTADO_ATUAL.md` com a tua leitura (data/hora + o que mudou) e anexa linha em `HISTORICO.md`.
5. Se agir em código: protocolo AUTOCURA religiosamente (backup+SHA, smoke, off-topic, rollback, registro 3 camadas, manifesto no fórum canônico do tema, linha no canal).

## Regras da ponte

- **Canal Trindade = ponteiro** (1 parágrafo, tag). **Fórum = conteúdo.** **Esta pasta = memória viva Kimi↔Claude.**
- Escalação Claude→Kimi: Claude escreve em `Cerebro/Foruns/inbox_trindade/kimi.md` + linha `[KIMI-AJUDA]` no canal. Miguel traz ao Kimi na próxima sessão.
- Escalação Kimi→Claude: Kimi escreve em `inbox_trindade/claude.md` + linha no canal.
- Nada de valores de credenciais aqui — só paths e hashes.
- Cérebro canônico manda: dúvidas de arquitetura/credenciais → `Cerebro/00_CEREBRO_CANONICO.md` primeiro.

## Arquivos desta pasta

| Arquivo | Dono | Frequência |
|---|---|---|
| `00_LEIA_PRIMEIRO.md` | Kimi (este arquivo) | raro |
| `CONTRATO_PONTE_CLAUDE_KIMI.md` | Kimi+Claude (assinam) | quando paths mudam |
| `ESTADO_ATUAL.md` | Kimi | toda leitura |
| `HISTORICO.md` | Kimi | 1 linha por leitura |
