# Raio-X — `motor_coletor.py` legado ativo em NYC

**Auditoria:** 2026-07-19 09:05 BRT  
**Coordenador:** Codex (OpenAI)  
**Escopo:** origem, ativação, consumidores, servidor e relação com V4

## Resposta direta

Sim. `motor_coletor.py` é um motor comum do pipeline legado, anterior ao V4. A auditoria de migração de 13/06 já o classificava como **“motor comum do legado”** e determinava que o estado final deveria ter **zero imports do motor antigo**, substituído por `coletor_geral.py` e pelo novo banco estruturado.

Ele não foi iniciado pelos testes editoriais do V4. Está ativo em **Nova York**, no servidor `Cafezinho-failover-vigia` (`198.199.121.136`). O Tencent está silenciado: sem cron root desses coletores e sem processo coletor ativo no momento da auditoria.

## Como reviveu

Em 01/07/2026, o failover promoveu NYC a servidor principal. O script `/root/failover_armar_completo.sh` substituiu o cron de espera pelo template `/root/crontab_failover_primary_complete.txt`. Esse template reativou todos os coletores legados.

Ao mesmo tempo, no `maestro_distribuicao.py`, os agentes consumidores `soberania`, `militar`, `latam`, `sheinbaum`, `ia` e `matriz` permanecem comentados como pausados por Miguel em 23–26/06. Resultado: produtores ligados e consumidores desligados.

## O que ele faz

`motor_coletor.py` não é um agente editorial único. É uma biblioteca compartilhada chamada por vários robôs antigos. Para cada item de RSS ele:

1. baixa e extrai o texto;
2. verifica duplicidade;
3. envia título e até 2.000 caracteres a uma LLM para pontuar e classificar;
4. grava aprovados em arquivos JSON `banco_artigos_brutos_<tema>.json`;
5. não publica diretamente no WordPress.

Os robôs ativos em NYC incluem soberania, militar, América Latina, Sheinbaum, IA/tecnologia, Fantástico, turismo e sobrenatural, além de outros coletores com implementação própria.

## O que está alimentando

Ele alimenta filas JSON legadas em `/root/agent_data/`, não o banco novo do V4. Estado observado:

| Fila | Itens | Pendentes | Consumidor no maestro |
|---|---:|---:|---|
| IA | 8.052 | 6.936 | pausado |
| matriz energética | 988 | 813 | pausado |
| soberania | 406 | 400 | pausado |
| militar | 137 | 136 | pausado |
| Latam | 267 | 242 | pausado |
| Sheinbaum | 68 | 46 | pausado |

Há também filas legadas de Fantástico, turismo e sobrenatural. Esses nomes são editorias/robôs do portal principal; não devem ser confundidos automaticamente com a infraestrutura separada dos sites temáticos. O GSN possui cron próprio e não é o acionador deste motor.

## Por que gastou tanto

Os coletores rodam em alta frequência: diversos deles quatro vezes por hora. Cada candidato novo ou rejeitado pode gerar uma chamada de LLM. Como os consumidores estão pausados e a identificação de chamadas é genérica, houve uma tempestade de triagem. Em 18/07, 1.946 chamadas Gemini foram registradas sob o mesmo nome `motor_coletor:curadoria`, principalmente entre 18h e 23h.

## Relação com o V4

- Não pertence ao pipeline novo V4.
- Não foi necessário para os testes reais de coleta V4.
- Não alimenta o banco estruturado de conteúdos do V4.
- O componente `autocura_v4_consenso` aparece separadamente na telemetria.
- A coincidência temporal com os testes não significa causalidade: o legado já estava agendado desde a promoção de NYC em 01/07.

## Falha de telemetria confirmada

Todos os robôs que usam a biblioteca gravam o mesmo `agente_nome="motor_coletor:curadoria"`. Assim, a telemetria identifica a biblioteca, mas perde o verdadeiro chamador, tema, cron, feed, `run_id`, item e destino. Além disso, o custo estimado não está conciliado com o Google Billing.

Correção necessária:

1. registrar `caller_agent`, `pipeline_version`, `host`, `run_id`, `call_id`, `cron_id`, `tema`, `feed`, `item_id`, banco de destino, provedor, modelo e motivo do fallback;
2. impedir biblioteca compartilhada de sobrescrever a identidade do agente chamador;
3. ligar cada custo ao conteúdo produzido ou ao descarte;
4. conciliar diariamente a estimativa com Google Billing por projeto e SKU;
5. alertar quando houver produtor ativo com consumidor pausado e quando uma fila crescer sem consumo;
6. separar explicitamente produção V3/legado, V4, Repetidor Estatal e sites temáticos.

## Estado da decisão

Miguel autorizou a pausa emergencial em 19/07. Os 11 coletores foram comentados no cron de NYC, os processos presos foram encerrados e não restou rota lateral ativa. Evidências completas: `execucao_pausa_coletores_legados_nyc_20260719.md`.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO — 2026-07-19 09:05 BRT
