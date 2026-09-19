# PROVA NEGATIVA — identidade de escrita da Laura, executada do lado Laura

```yaml
tipo: PROVA_NEGATIVA
executada_por: LAURA-CLAUDE (chefe do Loop Laura)
ts_brt: 2026-08-18T09:22:16-0300
alias: cafezinho-wp-write
metodo: verbos proibidos testados contra ID INEXISTENTE (999999999) — nenhum post real tocado
autoridade: ORDEM_MIGUEL 18/08 ~09:15 ("preciso que vocês tenham acesso às chaves para terem autonomia")
```

## Resultado, comando a comando

| # | comando | resposta do servidor | leitura |
|---|---|---|---|
| 1 | `health` | `{"ok":true,"mode":"editorial_write_restricted",...}` | canal vivo e **declara o próprio modo** |
| 2 | `publish 999999999` | `{"ok": false, "error": "command_denied"}` | **publicar é recusado pelo servidor** |
| 3 | `delete 999999999` | `command_denied` | **apagar é recusado** |
| 4 | `eval 'echo 1;'` | `command_denied` | **execução arbitrária recusada** |
| 5 | `status 999999999 publish` | `command_denied` | **mudar status é recusado** |
| 6 | `update-title 999999999 …` | `{"ok":false,"error":"post_not_available"}` | verbo **permitido** pela whitelist; alvo inexistente barrado |

## O que isso prova, e o que não prova

**Prova:** a restrição é **do servidor**, não da minha disciplina. Mesmo que
eu quisesse — ou que um erro meu tentasse — publicar, apagar, executar código
ou mudar status **não passa**. O comando 6 mostra o outro lado: o que me foi
autorizado (corrigir título, conteúdo, resumo, taxonomia, mídia e o carimbo
do gate) é aceito, e a inexistência do alvo é tratada sem tocar em nada.

**Não prova:** que eu use bem o que me foi permitido. Isso se mede no uso, com
reserva antes de tocar, foto do "antes", motivo escrito e trilha depois — o
runbook que publiquei antes de ter a chave.

## Método, para quem for repetir

Testes negativos foram feitos contra **ID inexistente** de propósito: se
algum verbo proibido tivesse passado, não haveria post real para estragar.
É a forma segura de testar recusa em produção, e recomendo como padrão.

## Estado declarado

- Modo: `CORRECAO_SEM_PUBLISH` — agora com canal capaz de executá-lo.
- Primeiro uso de escrita: **ainda não houve**. Este documento é anterior a
  qualquer correção minha em produção, por escolha: a prova vem antes do uso.

— LAURA-CLAUDE, chefe do Loop Laura, 18/08/2026 09:22 BRT
