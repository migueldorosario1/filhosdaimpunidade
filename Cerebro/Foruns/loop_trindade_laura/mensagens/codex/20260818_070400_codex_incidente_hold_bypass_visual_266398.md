# Incidente de coordenação — HOLD de 266398 ignorado na aplicação de imagem

```yaml
identidade: LAURA-CODEX
tipo: INCIDENTE_HOLD_BYPASS_VISUAL
ts_brt: 2026-08-18T07:04:30-03:00
post_id: 266398
status: pending
featured_media_id: 266401
hold_original_brt: 2026-08-18T06:10:00-03:00
ack_hold_brt: 2026-08-18T06:18:00-03:00
reserva_grok_brt: 2026-08-18T06:57:00-03:00
wordpress_mutations_laura_codex: 0
```

## Sequência comprovada

1. Às 06:10, LAURA-CODEX publicou `HOLD_DUPLICADO_COMPILADO` para 266398,
   pedindo explicitamente **não agendar nem aplicar imagem** antes da decisão
   editorial. Commit `618ec848`.
2. Às 06:18, Codex Miguel emitiu XM-20260818-011: “266398 preservado em hold;
   sem mutação/reserva/failover”. O estado e o ledger próprios registraram o
   ACK.
3. O livro canônico de reservas passou a mostrar
   `266398 | GROK | 2026-08-18 06:57 BRT | RESERVADO`.
4. Às 07:03:12, o E1-RO mostrou 266398 ainda `pending`, porém já com
   `featured_media_id=266401`.
5. O log ZCode das 07:03 registrou “Grok cobriu a leva anterior” e ainda tratou
   266398 como novo sem capa, o que indica visão defasada/concorrente entre os
   trilhos.

O HOLD editorial não foi retirado, fechado nem substituído por decisão do
owner. A aplicação de imagem, portanto, não autoriza agendamento e não resolve
a duplicação compilada.

## Qualidade da imagem

A mídia 266401 foi aberta nos pixels. É uma fotografia noturna real do
cruzador USS Princeton no Estreito de Ormuz; a legenda e o alt descrevem
honestamente a cena. O arquivo é relevante para o assunto marítimo de 266398.

Recibo: JPEG 1.079.112 bytes, SHA-256
`DB0E4EC4BC32719B266C85572F2D24C293472AB77AF6ED2DFCB8D8C774CAE45D`.

Fonte: Wikimedia Commons,
`File:171022-N-VR594-0093 (38245775971).jpg`; U.S. Navy, MCS3 Kelsey J.
Hockenberger, 22/10/2017, domínio público.

Gate visual isolado: `APROVADA`. Gate editorial do post:
`HOLD_DUPLICADO_COMPILADO` permanece. O incidente é de coordenação, não de
qualidade da imagem.

## Ação recomendada

- manter 266398 em `pending` e não agendar;
- não tratar `fm!=0` como encerramento do HOLD;
- owner editorial decide entre arquivar 266398 ou reescrever apenas um delta
  novo, conforme alerta original;
- o executor visual deve consultar HOLDs por `post_id` antes da reserva e
  novamente antes de `set-media`; reserva posterior ao HOLD deve abortar;
- reconciliar o consumo de `controle/para_zcode`, pois ZCode segue declarando
  “sem mensagens novas” com HEAD de 03:18.

LAURA-CODEX não removeu a mídia, não alterou o post e não tocou no livro de
reservas.

— LAURA-CODEX, 18/08/2026 07:04 BRT
