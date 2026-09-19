# Auditoria do gasto Gemini informado em R$ 98

**Auditoria:** 2026-07-19 08:43 BRT  
**Período:** 2026-07-18  
**Servidor:** NYC (`Cafezinho-failover-vigia`)

## Confirmação

- Miguel confirmou que o Gemini ficou sem crédito.
- A chave era válida para listar modelos, mas a geração retornava HTTP 429 por falta de crédito/quota faturável.
- O gasto informado no painel/fatura foi de R$ 98.

## Telemetria encontrada

O banco mensal de produção registrou 2.431 chamadas Gemini: 2.416 ao `gemini-2.5-flash`, 15 ao `gemini-2.5-pro`, 8.088.680 tokens de entrada, 87.926 de saída e custo interno estimado de US$ 2,676617.

| Agente | Chamadas | US$ estimados | Participação |
|---|---:|---:|---:|
| `motor_coletor:curadoria` | 1.946 | 2,374095 | 88,7% |
| `autocura_v4_consenso` | 382 | 0,180832 | 6,8% |
| `agente_comentarista` | 65 | 0,071104 | 2,7% |
| `tribunal_visual` e crosscheck | 30 | 0,034077 | 1,3% |
| `curador_social` | 2 | 0,008376 | 0,3% |
| `Repetidor Auditor` | 6 | 0,008133 | 0,3% |

## Atribuição

O responsável principal registrado foi o `motor_coletor:curadoria` do portal principal. Ele chama o roteador para classificar cada conteúdo capturado. O pico ocorreu entre 18h e 23h, com centenas de chamadas Gemini por hora.

- **Repetidor Estatal:** não foi o causador; usou majoritariamente DeepSeek e apenas seis auditorias/fallbacks Gemini.
- **Testes editoriais locais do V4:** não foram o causador; usaram OpenAI e Anthropic. O `autocura_v4_consenso` automático fez 382 chamadas, equivalentes a 6,8% do custo Gemini registrado.
- **Sites temáticos:** não lideram o gasto no banco auditado. O grande volume veio da curadoria do portal principal, contexto `economico`.

## Lacuna revelada

A telemetria identificou autoria e volume, mas não conciliou o dinheiro: estimou US$ 2,676617, enquanto Miguel informou R$ 98. O relatório financeiro declara ausente a `conciliacao_cartao`. Logo, ainda não é possível provar que as chamadas registradas explicam sozinhas os R$ 98. A diferença pode envolver cobrança não registrada, preço incorreto, impostos, recarga/crédito ou outra máquina/projeto compartilhando a credencial.

**Culpado operacional mais provável:** `motor_coletor:curadoria`.  
**Confiança na atribuição das chamadas:** alta.  
**Confiança na conciliação dos R$ 98:** baixa até confrontar o detalhamento real do Google Billing.

## Identificação posterior do componente

Auditoria aprofundada confirmou que `motor_coletor.py` é a biblioteca comum do pipeline legado, não um componente do V4. Os coletores antigos foram reativados em NYC pelo failover completo de 01/07, embora seus consumidores no `maestro_distribuicao.py` continuassem pausados. Eles alimentam filas JSON antigas em `/root/agent_data/`. Detalhes: `raio_x_motor_coletor_legado_nyc_20260719.md`.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO — 2026-07-19 08:43 BRT
