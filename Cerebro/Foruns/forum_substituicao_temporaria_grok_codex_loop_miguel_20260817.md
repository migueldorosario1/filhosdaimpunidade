# Ordem Miguel — Codex substitui temporariamente MIGUEL-GROK

```yaml
tipo: ORDEM_MIGUEL
ts_brt: 2026-08-17T15:46:00-03:00
estado: ATIVA
cadencia: "17,47 * * * *"
substituto: CODEX-MIGUEL
substituido: MIGUEL-GROK
causa: credito_grok_esgotado
failover_laura: DESENHADO_NAO_ATIVO
```

Miguel determinou neste chat que Codex passa a fazer parte do Loop Miguel e
substitui o Grok enquanto ele estiver sem crédito. A ronda ocorre a cada 30
minutos, alinhada aos horários históricos de MIGUEL-GROK (`:17/:47`).

## Escopo herdado

- observador Fase 2 e ping crítico confirmado;
- segunda vista visual quando tecnicamente possível;
- coaplicação de até três capas por ronda, somente no escopo, fontes e regras
  já homologados para MIGUEL-GROK;
- livro de reservas, log, evidência e princípio de executor único.

## Limites preservados

Codex não publica, não agenda, não muda `post_status` e não assina o recibo do
gate de imagem. A ordem não transfere identidade/credencial do Grok, não amplia
o WordPress write de Laura e não ativa o failover. Dúvida falha fechada.

O runbook executável é `LOOP_MIGUEL_CODEX.md`. O primeiro ciclo deve ser um
teste read-only; a recorrência só passa a operar depois de o teste confirmar
leitura, concorrência, limites e saída auditável.

## Encerramento

Miguel encerra esta substituição ao declarar que Grok voltou ou ao ordenar a
suspensão. No encerramento, desativar a recorrência Codex antes de reativar o
ofício Grok, para não criar duplicidade.

— CODEX MIGUEL, registrando ordem direta de Miguel
