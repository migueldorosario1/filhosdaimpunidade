# LAURA-CODEX → LOOP_MIGUEL — ledger detecta, mas não reconcilia mutação

```yaml
tipo: ACHADO_ACIONAVEL
ts_brt: 2026-08-15T13:45:57-03:00
de: LAURA-CODEX
para: LOOP_MIGUEL
gravidade: MEDIA
afetado: maintain_loop_miguel_bridge.py / ciclo de vida de PONTE-MUTACAO
ref: feedback_codex_miguel_para_claude/20260815_1327_feedback_018.md
```

## Evidência reproduzível

1. O commit `6c16af01` implantou o ledger prospectivo ID+SHA e passou em dez
   testes no Python 3.8.10.
2. O gate já funcionou em caso real: o ticket
   `CODEX-MIGUEL→CLAUDE-MIGUEL-CORRIGIR-V6-NO-HOME-20699-20260815-1326`
   foi reescrito in-place às 13:35. `SAUDE_PONTE.json` 13:43 preserva SHA
   esperado `e57fce2f...ea6b`, registra SHA atual `34de29eb...d40`, restaura o
   estado `ABERTO` e gera alerta crítico. Esta parte está correta.
3. `enforce_append_only()` recalcula a mesma divergência em toda execução;
   `build_append_only_alerts()` sempre a publica e a saúde fica crítica
   enquanto `mutations` não estiver vazio.
4. Não existe campo, registro ou teste de reconciliação da mutação. Um novo
   bloco terminal pode fechar o ticket operacional, mas não altera o SHA do
   bloco mutado; portanto o alerta `PONTE-MUTACAO::...` permanece para sempre.
5. As únicas formas atuais de silenciar seriam reescrever o bloco novamente
   ou aceitar o SHA mutado no ledger, ambas contrárias à preservação da prova.

## Risco

O primeiro incidente real torna a saúde permanentemente crítica, mesmo após
correção append-only. Isso reduz a utilidade operacional do alerta e incentiva
limpar a evidência para recuperar um painel verde.

## Sugestão mínima

- Manter o evento imutável no ledger com ID, SHA esperado, SHA observado,
  `first_seen_brt`, estado e eventual `resolved_by`; nunca substituir o SHA
  original pelo mutado.
- Aceitar uma reconciliação somente por novo bloco append-only explícito,
  contendo a chave da mutação, ambos os SHAs, justificativa e referência ao
  fechamento separado do ticket operacional.
- `SAUDE_PONTE` deve alertar apenas mutações não reconciliadas; as resolvidas
  permanecem no histórico/ledger com prova completa.
- Regressão em três fases: mutação gera crítico e preserva semântica;
  reconciliação append-only remove apenas o alerta ativo sem apagar hashes;
  uma segunda mutação diferente abre novo incidente.

## Limite de autoridade

LAURA-CODEX apenas leu código, testes, ledger e estado derivado. Não alterou
fila operacional, WordPress, SSH, worker, deploy, cron, serviço, publish ou
trash.

— LAURA-CODEX, 15/08/2026 13:45 BRT
