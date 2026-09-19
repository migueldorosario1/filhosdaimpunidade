# ERRATA — o Codex NÃO estava silencioso (corrige o consolidado 127)

```yaml
tipo: ERRATA
de: LAURA-CLAUDE (chefe)
relogio_ronda: "Monday, 17/08/2026 17:17:25 -0300"
corrige: relatorios_chefe/20260817_171121_relatorio_chefe_127.md
ref_erro: memoria_loop_laura/2026-08-17.md ERRO-1717
gravidade: ALTA — a afirmação errada foi levada a Miguel no chat
```

## O que eu afirmei (errado)

Que LAURA-CODEX estava `SEM_RELATORIO` por 2 ciclos (16:27 e 16:57) e
que havia "suspeita de esgotamento de crédito" — e concluí que o Loop
Laura poderia estar reduzido a um agente. **Relatei isso a Miguel.**

## O que é fato (medido agora)

LAURA-CODEX trabalhou normalmente na janela:

- **Ronda 117 — 16:29** (commit `90f112a0`): acompanhou o atraso do
  266225 (72 min), confirmou que o caso tem dono no Loop Miguel e não
  duplicou; verificou 1 post novo limpo e o das 16:45 limpo antes de ir
  ao ar.
- **Ronda 118 — 16:59** (commit `77bd700a`): 266225 em 103 min de
  atraso, caso crítico e do Loop Miguel; post das 16:45 publicou limpo;
  e — com razão — registrou **SEM_RELATORIO do chefe** na janela
  seguinte às 16:17 (eu estava na tarefa do ZCode).

**Ou seja:** quem ficou em silêncio na janela fui eu, não ele. Ele
registrou isso corretamente, sem acusar causa.

## Por que errei

Calculei o delta a partir do **meu último push** em vez do `head_lido`
da ronda anterior. Entre uma coisa e outra houve um `git pull` fora de
ronda (para a tarefa do ZCode) que já havia absorvido os commits do
Codex — então o diff veio vazio e eu li "vazio" como "ninguém
trabalhou". Detalhes e prevenção: ERRO-1717 no diário, lição 8 no INDEX.

## Estado correto do Loop Laura

- **LAURA-CODEX: ATIVO** e em dia (rondas 117 e 118).
- **LAURA-GROK: suspenso** por crédito (esse fato permanece).
- **Cobertura:** 2 de 3 ativos. A redundância técnica **não** foi
  perdida; a lacuna real continua sendo só a conferência de imagem.

Peço desculpas ao ofício e ao dono pelo susto. A suspeita foi minha, o
trabalho dele estava lá.

— LAURA-CLAUDE, chefe do Loop Laura, segunda-feira 17/08/2026 17:17 BRT
