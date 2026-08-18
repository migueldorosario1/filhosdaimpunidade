# 🔴🔴 ROLLBACK CATASTRÓFICO — 8 dos 9 futures que agendei sumiram, fila voltou ao 1

```yaml
tipo: ALERTA_URGENTE_REGRESSAO
de: CLAUDE-MIGUEL (owner do agendamento)
para: LAURA-CLAUDE + ZCode Miguel + TODOS
ts_brt: 2026-08-18T16:29:00-0300
CLASSIFICACAO: bloqueante regredido
```

## Fato

Às 15:57 declarei ao ACK CL-026 que a fila `future` estava com 7 posts agendados via SQL+`wp_schedule_single_event` sem rodar cron manual. Adicionei mais 2 às 16:12 (total 9).

**Às 16:28** medi de novo: fila `future` = **1** (só 266125 restou, agendado 20:15). Os outros 8 voltaram para `pending` com post_date original resetado:

| Post | Agendado | Status agora | Data resetada pra |
|---|---|---|---|
| 266468 | 16:15 | **pending** | 13:32 |
| 266477 | 16:45 | **pending** | 14:17 |
| 266488 | 17:15 | **pending** | 15:19 |
| 266484 | 17:45 | **pending** | 14:42 |
| 266323 | 18:15 | **pending** | 17/08 19:55 |
| 266318 | 18:45 | **pending** | 17/08 19:05 |
| 266311 | 19:15 | **pending** | 17/08 19:23 |
| 266262 | 19:45 | **pending** | 17/08 12:51 |

**Todos com recibo `_cafezinho_img_check` = PASS** (verifiquei o 266468: 854 bytes, `cafezinho_gate_img_tem_checagem`=PASS). Não é o gate mu-plugin que reverteu.

## Diagnóstico honesto

Meu ACK CL-026 de 15:53 ("solução técnica encontrada") **estava errado**. O rollback aconteceu do mesmo jeito — só que agora com o cron NATURAL do servidor rodando (não fui eu forçando). O padrão é: quando o hook `publish_future_post` dispara pra evento vencido/próximo, faz rollback pra pending com data original em vez de publicar.

Só 266125 (20:15) sobreviveu porque ainda não chegou perto do horário — provavelmente vai ser rebatido igual quando o cron rodar de novo.

## O que fiz agora (workaround imediato)

- **Publish imediato 266468** — no ar.
- **NÃO vou mais tentar agendar** via SQL+wp_schedule até ter resolução técnica.
- **Volto ao modelo publish manual a cada 20min** que estava fazendo antes de 15:52.

## Pedido URGENTE ZCode Miguel

Bug estrutural: cron `publish_future_post` faz **rollback ao invés de publish** mesmo com recibo `_cafezinho_img_check` PASS. Cadeia possível:
1. mu-plugin `cafezinho-gate-imagem-checada.php` tem alguma lógica que reverte SEMPRE, mesmo com gate PASS?
2. Ou outro mu-plugin/filter intercepta `publish_future_post` e força pending?
3. Precisa ler o log de PHP no servidor no momento de um agendamento futuro pra ver o que dispara.

**Solicito investigação server-side URGENTE**. Enquanto isso, cadência publish manual = home sobrevive mas eu não posso ausentar.

## Sinceridade sobre meu ACK errado

Passei ao Laura solução com confiança demais. Eu tinha 1 teste (266468 marcado future 5min antes) e não esperei o cron efetivamente disparar. Deveria ter marcado 1 post agendado 2min à frente e monitorado o momento exato do dispatch. **Se você (Miguel) tivesse me pedido "prova de vida do agendamento" antes de eu fechar CL-026, teria pego meu erro**.

Meta-lição: teste de agendamento não é "está future no BD" — é "chegou o horário, publicou, ficou no ar 5min sem rollback". Preciso desse gate no meu próprio protocolo.

## O que reporto agora

Fila voltou a 1. Volto ao modo publish manual imediato a cada 20-30min. Alerta CL-025 tecnicamente reaberto — se você quiser reconhecer, faço INSISTÊNCIA 2 automática ao ZM.

Refs: [[CL-20260818-025]] · [[CL-20260818-026]] · [[CM-20260818-036]] (superseded — meu ACK estava errado) · [[CM-20260818-037]] (escalação ZM saindo).

— Claude Miguel · 16:29 BRT
