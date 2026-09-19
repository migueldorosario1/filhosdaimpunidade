# Protocolo Modo Ilha — queda do GitHub (ponte Laura)

```yaml
versao: 1.0
criado: 29/08/2026 11:05 BRT
autor: LAURA-CLAUDE (chefe), proposta aprovada por Miguel (chat 29/08 ~10:50) e AGY (AL-372)
estado: VIGENTE
aplica_se: todos os agentes do PC LAURA (Claude, AGY, Grok, ZCode) e, por adesao, Dell/ds
```

## Regras

1. **Deteccao:** `git push` ou `git pull` falhando 2 vezes seguidas = GitHub presumido fora.
2. **Bandeira:** quem detectar primeiro cria `PONTE_OFFLINE.flag` na raiz da ponte
   (`ponte_laura_completa/`) com hora BRT e agente; os demais param de tentar push ao ver a flag.
3. **Trabalho nao para:** todos declaram `MODO_ILHA` no proprio estado e SEGUEM commitando
   localmente nos arquivos proprios. Nada de segurar trabalho em memoria.
4. **Comunicacao de emergencia Laura->Miguel:** escuta/Telegram (daemon local, independente do
   git). Pendente teste comprovatorio ("teste ilha") em dia saudavel.
5. **Volta:** quem notar o GitHub de volta remove a flag, e os pushes se reconciliam na ordem do
   lock de sempre. Como cada agente so escreve nos arquivos proprios, nao ha conflito estrutural.
6. **Espelho secundario (camada 3):** remote adicional (GitLab/Bitbucket) a criar por Miguel;
   quando existir, `git push espelho main` passa a ser o passo 2a antes de declarar ilha total.

## O que este protocolo NAO autoriza
Nenhuma permissao nova: sem WordPress, sem publish extra, sem mexer em launcher alheio. E so
conduta de sincronizacao.
