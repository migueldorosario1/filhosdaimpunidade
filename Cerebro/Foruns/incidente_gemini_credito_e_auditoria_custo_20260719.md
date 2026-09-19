# Incidente Gemini — crédito esgotado e auditoria de gasto

**Registro:** 2026-07-19 BRT  
**Informação confirmada por Miguel:** o HTTP 429 do Gemini ocorreu porque a conta estava sem crédito.  
**Valor informado:** aproximadamente R$ 98 gastos em 18/07/2026.

## Classificação

- Credencial: válida; listagem de modelos funcionou.
- Geração: indisponível por falta de crédito/quota financeira.
- Erro esperado no V4: `gemini_quota_or_billing_unavailable`.
- Proibido classificar como sucesso, resposta vazia, falha genérica ou fallback silencioso.

## Auditoria aberta

Objetivo: atribuir os R$ 98 a agente, produto e execução, distinguindo:

1. Repetidor Estatal;
2. testes e sprints do V4;
3. sites temáticos;
4. qualquer processo não identificado.

Evidência exigida: horário, modelo, tokens/unidades, custo, agente, `run_id/call_id`, arquivo/serviço de origem e recibo. Ausência de vínculo será registrada como lacuna de telemetria.

## Resultado

O banco de produção atribuiu 88,7% do custo Gemini registrado ao `motor_coletor:curadoria` do portal principal: 1.946 de 2.431 chamadas. O Repetidor Estatal respondeu por somente seis chamadas Gemini. Os testes editoriais locais do V4 não usaram Gemini; o `autocura_v4_consenso` automático respondeu por 6,8%. A estimativa interna de US$ 2,676617 ainda não concilia os R$ 98 informados. Relatório: `auditoria_gasto_gemini_98_reais_20260719.md`.
